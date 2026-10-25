"""P6 -- a machine-checkable subset of "NPC cases with no authored terminus". Reads the 46 NPC cases
through the repo's own loader (harness/run_cases.load_cases("NPC")) and classifies `ends_when` by
lexical markers only (no judgement): type; NEVER markers; EXTRACTOR-PRESUMED markers; a branch list
(>=2 disjuncts separated by ';' or ' or ' or a list type). Also cross-reads ENDINGS_CLASSIFIED.yaml
(an agent's prose classification, its own weakest-evidence label) for the same ids.

  python3 -I probes/p6_case_termini.py
"""
import re
import sys
from collections import Counter

sys.path.insert(0, "/home/user/ttrpg")
import yaml

from engine.season.harness.run_cases import load_cases

NEVER = re.compile(r"\bnever\b|no natural (conclusion|end)|names no (natural )?(end|conclusion|terminus)|"
                   r"open[- ]ended|does not end|no (defined|stated) end|ongoing", re.I)
PRESUMED = re.compile(r"\[ASSUMPTION|presum|infer|extract|not stated|unstated|the source (does not|gives no|names no)", re.I)

cs = load_cases("NPC")
rows = []
for c in cs:
    e = c.get("ends_when")
    t = type(e).__name__
    s = e if isinstance(e, str) else yaml.safe_dump(e)
    branches = (len(e) if isinstance(e, (list, dict)) else
                len([x for x in re.split(r";| or |, or ", s) if x.strip()]))
    rows.append({"id": c["id"], "type": t, "never": bool(NEVER.search(s)), "presumed": bool(PRESUMED.search(s)),
                 "branches": branches, "text": s[:140].replace("\n", " ")})

print("cases", len(rows), "ends_when types", dict(Counter(r["type"] for r in rows)))
print("never-marked", sum(r["never"] for r in rows), "presumed-marked", sum(r["presumed"] for r in rows),
      "either", sum(r["never"] or r["presumed"] for r in rows))
print("branch count >=2:", sum(r["branches"] >= 2 for r in rows), " ==1:", sum(r["branches"] == 1 for r in rows))
try:
    ec = yaml.safe_load(open("/home/user/ttrpg/engine/season/ENDINGS_CLASSIFIED.yaml"))
    print("ENDINGS_CLASSIFIED top keys:", list(ec)[:8] if isinstance(ec, dict) else type(ec))
except Exception as ex:
    print("ENDINGS_CLASSIFIED read failed", ex)
for r in rows:
    flag = ("NEVER " if r["never"] else "") + ("PRESUMED " if r["presumed"] else "")
    print(f"{r['id']:9s} {r['type']:4s} br={r['branches']} {flag:16s} | {r['text']}")

# STRICT subset (the one the register cites): NONE = the text says no terminus/arc/goal/end condition
# is authored, or UNCLEAR; PRESUMED = the extractor wrote "presumably". Everything else names at least one
# authored terminus in the text (not checked for whether the engine can observe it).
NONE_S = re.compile(r"no (defined )?terminus|no (authored )?(personal )?(arc|goal|end condition)|"
                    r"no (stated |authored )?resolution condition|no natural conclusion|UNCLEAR|"
                    r"not specified to conclude|names no defined terminus|no removal, exposure, or resolution", re.I)
PRES_S = re.compile(r"presumabl", re.I)
strict = [(c["id"], bool(NONE_S.search(c["ends_when"])), bool(PRES_S.search(c["ends_when"]))) for c in cs]
none_ids = [i for i, n, p in strict if n]
pres_ids = [i for i, n, p in strict if p and not n]
print("STRICT none:", len(none_ids), sorted(none_ids))
print("STRICT presumed-only:", len(pres_ids), sorted(pres_ids))
print("STRICT none-or-presumed:", len(none_ids) + len(pres_ids), "of", len(cs))
