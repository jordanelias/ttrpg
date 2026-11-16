"""P7: case_rows. Every (faction, rung, matter, bench size) -> row_for_case.  PYTHONHASHSEED=0 python lane2/p7_caserows.py"""
from collections import defaultdict
from common import *
from scmodel.host import row_for_case
named = defaultdict(list)
for fac in ("Crown", "Parliament", "duchy", "Church", "Guild", "Other"):
    for rung in data.RUNG_KINDS:
        for matter in ("person", "proposition", "record"):
            for bs in (1, 3):
                try:
                    r = row_for_case({"faction": fac, "rung": rung}, matter, bs)
                except LookupError as e:
                    r = "LookupError"
                named[r].append((fac, rung, matter, bs))
for r, cs in named.items():
    print(f"{r:22s} {len(cs):3d} e.g. {cs[:3]}")
print("never named:", [r for _, r in data.CASE_ROWS if r not in named])
print("proposition cases ->", sorted({row_for_case({'faction': f, 'rung': 'realm'}, 'proposition', 3) for f in ('Crown','Church','Guild')}))
