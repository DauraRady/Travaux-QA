#!/usr/bin/env python3
"""Contrôle et construction des cas de test du QC agent.

Trois commandes :
  check  RAPPORT.md                 contrôle le format et les règles d'écriture (sans IA)
  build  RAPPORT.md --us ID --out DOSSIER [options]
                                    construit un fichier JSON-Patch par cas, prêt pour curl
                                    (--data-binary @fichier), plus un manifest.json
  csv    RAPPORT.md --us ID --out FICHIER.csv [--area --assignee --state]
                                    construit un CSV à importer dans Test Plans
                                    (Import test cases from CSV), sans aucune écriture par l'API

Le rapport est le fichier qc-reports/US-<id>.md produit par l'agent puis relu par un humain.
Le script ne lit que la section « 4- Cas de test ». Aucun appel réseau ici.

Codes de sortie : 0 = OK, 1 = erreurs dans le rapport, 2 = usage ou fichier introuvable.
"""
import argparse
import csv
import json
import os
import re
import sys
from xml.sax.saxutils import escape

CASE_HEADER = re.compile(r"^###\s+(TC-\d+)\s+-\s+(.+?)\s*$")
SECTION_CASES = re.compile(r"^##\s+4-\s")
SECTION_ANY = re.compile(r"^##\s+\d+-\s")
PARAM_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
STATE_OK = re.compile(r"^(Exécutable|Bloqué\s*:\s*Q-\d+(\s*,\s*Q-\d+)*)$")
FAMILIES = {"Nominal", "Négatif", "Limite", "Bord"}

GIVEN = ("Étant donné", "Etant donné", "Soit")
WHEN = ("Quand", "Lorsque")
THEN = ("Alors",)
AND = ("Et", "Mais")

# Mots qui rendent un résultat attendu invérifiable (cherchés hors des textes entre guillemets)
BANNED = [r"\bcorrectement\b", r"\bnormalement\b", r"\bavec succès\b", r"\bcomme prévu\b",
          r"\bbien\b", r"\betc\b", r"\bselon le cas\b", r"\bselon le rôle\b", r"\bdoit fonctionner\b",
          r"\bou\b"]
# Indices qu'un refus vérifie aussi l'état inchangé de la donnée
UNCHANGED = [r"inchangé", r"toujours", r"\baucun", r"\baucune", r"n'est pas créé", r"n'est pas créée",
             r"n'a pas été", r"reste", r"pas de nouvelle", r"n'est pas affiché", r"n'est pas visible",
             r"non affiché", r"conserv"]


def starts(line, words):
    return any(line == w or line.startswith(w + " ") or line.startswith(w + ":") for w in words)


def strip_quotes(text):
    return re.sub(r"[\"«“][^\"»”]*[\"»”]", "", text)


def read_cases(path):
    """Découpe la section 4 en blocs de cas."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    in_section, cases, current = False, [], None
    for raw in lines:
        if SECTION_CASES.match(raw):
            in_section = True
            continue
        if in_section and SECTION_ANY.match(raw):
            break
        if not in_section:
            continue
        m = CASE_HEADER.match(raw)
        if m:
            current = {"id": m.group(1), "title": m.group(2), "lines": []}
            cases.append(current)
        elif current is not None:
            current["lines"].append(raw)
    return in_section, cases


def parse_case(case):
    """Extrait métadonnées, ligne Détecte, étapes Gherkin et Exemples."""
    meta, detect, technique, steps, examples = {}, "", "", [], []
    lines = case["lines"]
    i = 0
    # tableau de métadonnées : première ligne d'en-tête qui commence par | AC
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("| AC"):
            header = [c.strip() for c in ln.strip("|").split("|")]
            if i + 2 < len(lines):
                values = [c.strip() for c in lines[i + 2].strip().strip("|").split("|")]
                meta = dict(zip(header, values))
            i += 3
            continue
        if ln.startswith("Détecte"):
            detect = ln.split(":", 1)[1].strip() if ":" in ln else ""
        if ln.startswith("Technique"):
            technique = ln.split(":", 1)[1].strip() if ":" in ln else ""
        if ln.startswith("```gherkin"):
            i += 1
            in_examples = False
            while i < len(lines) and not lines[i].strip().startswith("```"):
                g = lines[i].strip()
                if g.startswith("Exemples"):
                    in_examples = True
                elif in_examples and g.startswith("|"):
                    examples.append([c.strip() for c in g.strip("|").split("|")])
                elif g and not g.startswith("#") and not starts(g, ("Scénario", "Plan du scénario")):
                    steps.append(g)
                i += 1
        i += 1
    return meta, detect, technique, steps, examples


def group_steps(steps):
    """Regroupe pour Azure Test Plans : préconditions | action Quand | résultats Alors."""
    pre, action, expected, phase = [], [], [], "given"
    for s in steps:
        if starts(s, GIVEN):
            phase = "given"
        elif starts(s, WHEN):
            phase = "when"
        elif starts(s, THEN):
            phase = "then"
        target = {"given": pre, "when": action, "then": expected}[phase]
        target.append(s)
    return pre, action, expected


def check_case(case, seen_titles):
    errors, warnings = [], []
    cid = case["id"]
    meta, detect, technique, steps, examples = parse_case(case)
    case.update(meta=meta, detect=detect, technique=technique, steps=steps, examples=examples)

    for field in ("AC", "Règle", "Famille", "Priorité", "État"):
        if not meta.get(field):
            errors.append(f"{cid} : champ « {field} » absent du tableau de métadonnées")
    if meta.get("Famille") and meta["Famille"] not in FAMILIES:
        errors.append(f"{cid} : Famille « {meta['Famille']} » inconnue (Nominal, Négatif, Limite, Bord)")
    if meta.get("Priorité") and meta["Priorité"] not in {"1", "2", "3", "4"}:
        errors.append(f"{cid} : Priorité doit valoir 1, 2, 3 ou 4")
    if meta.get("État") and not STATE_OK.match(meta["État"]):
        errors.append(f"{cid} : État doit être « Exécutable » ou « Bloqué : Q-n »")
    if case["title"] in seen_titles:
        errors.append(f"{cid} : titre en double avec {seen_titles[case['title']]}")
    seen_titles[case["title"]] = cid
    if not detect:
        warnings.append(f"{cid} : ligne « Détecte : » absente (quelle anomalie ferait échouer ce cas ?)")
    if not technique:
        warnings.append(f"{cid} : ligne « Technique : » absente")
    if not steps:
        errors.append(f"{cid} : aucun bloc ```gherkin")
        return errors, warnings
    if len(steps) > 8:
        warnings.append(f"{cid} : {len(steps)} étapes (8 au plus : le cas mélange-t-il plusieurs comportements ?)")

    whens = [s for s in steps if starts(s, WHEN)]
    if len(whens) != 1:
        errors.append(f"{cid} : {len(whens)} étape(s) Quand, il en faut exactement une")
    pre, action, expected = group_steps(steps)
    if any(starts(s, AND) for s in action[1:]):
        errors.append(f"{cid} : un Et ou Mais prolonge le Quand ; une seule action par cas")
    if not any(starts(s, THEN) for s in steps):
        errors.append(f"{cid} : aucune étape Alors")
    if not pre:
        warnings.append(f"{cid} : aucune précondition Étant donné")
    for s in pre:
        if not re.search(r"[\"«“]", s) and not re.search(r"<[a-z_0-9]+>", s):
            warnings.append(f"{cid} : précondition sans valeur concrète entre guillemets : « {s} »")
    for s in expected:
        bare = strip_quotes(s).lower()
        for pat in BANNED:
            if re.search(pat, bare):
                word = pat.replace("\\b", "")
                errors.append(f"{cid} : résultat invérifiable (« {word} ») : « {s} »")
                break
    for s in expected:
        if re.search(r"\b(message|erreur)\b", s.lower()) and not re.search(r"[\"«“]", s):
            warnings.append(f"{cid} : message sans texte exact, vérifier que la question du texte est posée : « {s} »")
    if meta.get("Famille") == "Négatif":
        text = " ".join(expected).lower()
        if not any(re.search(p, text) for p in UNCHANGED):
            warnings.append(f"{cid} : cas négatif sans vérification de la donnée inchangée")
    if meta.get("État", "").startswith("Bloqué") and "[À VALIDER PO]" not in " ".join(steps):
        warnings.append(f"{cid} : cas bloqué sans marqueur [À VALIDER PO] sur la valeur à trancher")

    used = set(re.findall(r"<([^<>\s]+)>", " ".join(steps)))
    if used or examples:
        if not examples:
            errors.append(f"{cid} : paramètres {sorted(used)} sans bloc Exemples")
        else:
            header = examples[0]
            for name in header:
                if not PARAM_NAME.match(name):
                    errors.append(f"{cid} : nom de paramètre « {name} » invalide (minuscules, chiffres, _)")
            missing = used - set(header)
            unused = set(header) - used - {"cas"}
            if missing:
                errors.append(f"{cid} : paramètres absents des Exemples : {sorted(missing)}")
            if unused:
                errors.append(f"{cid} : colonnes d'Exemples jamais utilisées : {sorted(unused)}")
            if len(examples) < 3:
                warnings.append(f"{cid} : une seule ligne d'Exemples, un Scénario simple suffit")
            rows = [tuple(r) for r in examples[1:]]
            if len(rows) != len(set(rows)):
                errors.append(f"{cid} : lignes d'Exemples en double")
    return errors, warnings


def run_check(path):
    found, cases = read_cases(path)
    errors, warnings = [], []
    if not found:
        errors.append("section « ## 4- Cas de test » introuvable")
    elif not cases:
        warnings.append("aucun cas dans la section 4")
    seen = {}
    for case in cases:
        e, w = check_case(case, seen)
        errors += e
        warnings += w
    prios = [c.get("meta", {}).get("Priorité") for c in cases]
    n = len(prios)
    if n >= 4:
        p1 = prios.count("1")
        if p1 / n > 0.25:
            warnings.append(f"priorité 1 sur {p1}/{n} cas (plafond conseillé : 25 %)")
        if (p1 + prios.count("2")) / n > 0.60:
            warnings.append(f"priorités 1 et 2 sur {p1 + prios.count('2')}/{n} cas (plafond conseillé : 60 %)")
    return cases, errors, warnings


def cell(text):
    """Cellule d'étape ADO : HTML stocké dans du XML, donc double échappement, une ligne par <br/>."""
    return "&lt;br/&gt;".join(escape(escape(line)) for line in text.split("\n"))


def to_ado_param(text):
    return re.sub(r"<([a-z][a-z0-9_]*)>", r"@\1", text)


def steps_xml(pairs):
    out, sid = [], 1
    for action, expected in pairs:
        sid += 1
        kind = "ValidateStep" if expected else "ActionStep"
        out.append(f'<step id="{sid}" type="{kind}">'
                   f'<parameterizedString isformatted="true">{cell(action)}</parameterizedString>'
                   f'<parameterizedString isformatted="true">{cell(expected)}</parameterizedString>'
                   f'<description/></step>')
    return f'<steps id="0" last="{sid}">' + "".join(out) + "</steps>"


def params_xml(names, rows):
    params = "<parameters>" + "".join(f'<param name="{n}" bind="default"/>' for n in names) + "</parameters>"
    cols = "".join(f'<xs:element name="{n}" type="xs:string" minOccurs="0" />' for n in names)
    data = "".join("<Table1>" + "".join(f"<{n}>{escape(v)}</{n}>" for n, v in zip(names, r)) + "</Table1>"
                   for r in rows)
    source = ('<NewDataSet><xs:schema id="NewDataSet" xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" '
              'xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">'
              '<xs:element name="NewDataSet" msdata:IsDataSet="true" msdata:Locale="">'
              '<xs:complexType><xs:choice minOccurs="0" maxOccurs="unbounded">'
              '<xs:element name="Table1"><xs:complexType><xs:sequence>' + cols +
              '</xs:sequence></xs:complexType></xs:element></xs:choice></xs:complexType></xs:element>'
              '</xs:schema>' + data + '</NewDataSet>')
    return params, source


def build_patch(case, args):
    meta = case["meta"]
    pre, action, expected = group_steps(case["steps"])
    pairs = []
    if pre:
        pairs.append(("\n".join(to_ado_param(s) for s in pre), ""))
    pairs.append(("\n".join(to_ado_param(s) for s in action), "\n".join(to_ado_param(s) for s in expected)))
    acs = [a.strip() for a in meta["AC"].split(",") if a.strip()]
    blocked = meta["État"].startswith("Bloqué")
    tags = ["QC-agent", f"US-{args.us}"] + acs + [meta["Famille"]] + (["Bloqué"] if blocked else [])
    description = "<br/>".join(escape(x) for x in [
        f"US {args.us} | AC : {meta['AC']} | Règle : {meta['Règle']} | Famille : {meta['Famille']}",
        f"Technique : {case['technique'] or '-'}",
        f"Détecte : {case['detect'] or '-'}",
        f"État : {meta['État']}",
    ])
    ops = [
        {"op": "add", "path": "/fields/System.Title", "value": f"{case['id']} - {case['title']}"},
        {"op": "add", "path": "/fields/Microsoft.VSTS.TCM.Steps", "value": steps_xml(pairs)},
        {"op": "add", "path": "/fields/System.AssignedTo", "value": args.assignee or ""},
        {"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": int(meta["Priorité"])},
        {"op": "add", "path": "/fields/System.Tags", "value": "; ".join(tags)},
        {"op": "add", "path": "/fields/System.Description", "value": description},
    ]
    if args.area:
        ops.append({"op": "add", "path": "/fields/System.AreaPath", "value": args.area})
    if args.iteration:
        ops.append({"op": "add", "path": "/fields/System.IterationPath", "value": args.iteration})
    if case["examples"]:
        header = case["examples"][0]
        keep = [i for i, n in enumerate(header) if n != "cas"]
        rows = [[r[i] for i in keep] for r in case["examples"][1:]]
        params, source = params_xml([header[i] for i in keep], rows)
        ops.append({"op": "add", "path": "/fields/Microsoft.VSTS.TCM.Parameters", "value": params})
        ops.append({"op": "add", "path": "/fields/Microsoft.VSTS.TCM.LocalDataSource", "value": source})
    return ops


CSV_HEADER = ["ID", "Work Item Type", "Title", "Test Step", "Step Action", "Step Expected",
              "Area Path", "Assigned To", "State", "Priority", "Tags"]
MAX_TITLE = 128  # limite de Test Plans pour un titre importé


def expand_examples(case):
    """Plan du scénario : l'import CSV ne gère pas les paramètres, donc une variante par ligne d'Exemples."""
    if not case["examples"]:
        return [(case["title"], case["steps"])]
    header, rows = case["examples"][0], case["examples"][1:]
    variants = []
    for row in rows:
        values = dict(zip(header, row))
        steps = [re.sub(r"<([a-z][a-z0-9_]*)>", lambda m: values.get(m.group(1), m.group(0)), s) for s in case["steps"]]
        label = values.get("cas") or ", ".join(v for k, v in values.items() if k != "cas")
        variants.append((f"{case['title']} ({label})", steps))
    return variants


def csv_rows(case, args):
    """Format de l'export Test Plans : une ligne de cas, puis une ligne par pas."""
    meta = case["meta"]
    acs = [a.strip() for a in meta["AC"].split(",") if a.strip()]
    tags = "; ".join(["QC-agent", f"US-{args.us}"] + acs + [meta["Famille"]])
    rows, notes = [], []
    for title, steps in expand_examples(case):
        full = f"{case['id']} - {title}"
        if len(full) > MAX_TITLE:
            notes.append(f"{case['id']} : titre de {len(full)} caractères coupé à {MAX_TITLE}")
            full = full[:MAX_TITLE - 1] + "…"
        pre, action, expected = group_steps(steps)
        rows.append(["", "Test Case", full, "", "", "", args.area, args.assignee, args.state, meta["Priorité"], tags])
        n = 0
        if pre:
            n += 1
            rows.append(["", "", "", str(n), "\n".join(pre), "", "", "", "", "", ""])
        n += 1
        rows.append(["", "", "", str(n), "\n".join(action), "\n".join(expected), "", "", "", "", ""])
    return rows, notes


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("report")
    v = sub.add_parser("csv")
    v.add_argument("report")
    v.add_argument("--us", required=True)
    v.add_argument("--out", required=True, help="fichier CSV à écrire")
    v.add_argument("--area", default="", help="Area Path du plan, obligatoire à l'import sur Azure DevOps Services")
    v.add_argument("--assignee", default="")
    v.add_argument("--state", default="Design")
    v.add_argument("--inclure-bloques", action="store_true")
    b = sub.add_parser("build")
    b.add_argument("report")
    b.add_argument("--us", required=True)
    b.add_argument("--out", required=True)
    b.add_argument("--assignee", default="")
    b.add_argument("--area", default="")
    b.add_argument("--iteration", default="")
    b.add_argument("--inclure-bloques", action="store_true")
    args = parser.parse_args()

    if not os.path.isfile(args.report):
        print(f"ERREUR : rapport introuvable : {args.report}")
        return 2
    cases, errors, warnings = run_check(args.report)
    for w in warnings:
        print(f"AVERTISSEMENT : {w}")
    for e in errors:
        print(f"ERREUR : {e}")
    print(f"BILAN : {len(cases)} cas, {len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    if errors:
        return 1
    if args.cmd == "check":
        return 0

    if args.cmd == "csv":
        out_rows, skipped = [CSV_HEADER], []
        for case in cases:
            if case["meta"]["État"].startswith("Bloqué") and not args.inclure_bloques:
                skipped.append(f"{case['id']} ({case['meta']['État']})")
                continue
            rows, notes = csv_rows(case, args)
            out_rows += rows
            for n in notes:
                print(f"AVERTISSEMENT : {n}")
        folder = os.path.dirname(args.out)
        if folder:
            os.makedirs(folder, exist_ok=True)
        # BOM : Excel affiche les accents ; Test Plans lit l'UTF-8
        with open(args.out, "w", encoding="utf-8-sig", newline="") as fh:
            csv.writer(fh, quoting=csv.QUOTE_MINIMAL).writerows(out_rows)
        n_cases = sum(1 for r in out_rows[1:] if r[1] == "Test Case")
        print(f"CSV : {n_cases} cas dans {args.out}")
        if skipped:
            print("NON EXPORTÉS (bloqués) : " + ", ".join(skipped))
        if not args.area:
            print("AVERTISSEMENT : colonne Area Path vide, à remplir avant l'import (obligatoire sur Azure DevOps Services)")
        return 0

    os.makedirs(args.out, exist_ok=True)
    manifest = []
    for case in cases:
        entry = {"id": case["id"], "title": f"{case['id']} - {case['title']}", "state": case["meta"]["État"]}
        if case["meta"]["État"].startswith("Bloqué") and not args.inclure_bloques:
            entry["skipped"] = "cas bloqué, non publié sans --inclure-bloques"
        else:
            path = os.path.join(args.out, f"{case['id'].lower()}.json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(build_patch(case, args), fh, ensure_ascii=False)
            entry["file"] = path
        manifest.append(entry)
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)
    print(f"CONSTRUIT : {sum(1 for m in manifest if 'file' in m)} fichier(s), manifest dans {args.out}/manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
