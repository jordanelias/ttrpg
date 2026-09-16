#!/usr/bin/env python3
"""Interrogate the 8 state graphs for primitive overlap.
Roles: S=state-defining, T=transition verb, G=guard/condition, O=output artefact, M=resolution modifier
"""
from itertools import combinations
from collections import defaultdict

NAMES = {}
for line in open('political-mechanics-primitives.md'):
    if line.startswith('**P') and ' — ' in line:
        pid = line.split(' — ')[0].replace('**','').strip()
        if not (pid[1:].isdigit()): continue
        nm  = line.split(' — ',1)[1].split('.**')[0].replace('*','').replace('(','').strip()
        NAMES.setdefault(pid, nm)

# system -> {primitive: role}
SYS = {
 'S1 Court': {
   'P5':'S','P6':'T','P7':'T','P8':'T','P9':'G','P10':'T','P12':'T','P14':'T',
   'P19':'G','P41':'O','P1':'M','P3':'M','P16':'O','P22':'T','P25':'G','P26':'G'},
 'S2 Tribunal': {
   'P5':'S','P6':'T','P7':'T','P8':'T','P9':'G','P10':'T','P12':'T','P14':'T',
   'P19':'G','P41':'O','P1':'G','P2':'M','P3':'T','P16':'O','P22':'T','P23':'G',
   'P25':'G','P26':'G','P30':'T','P40':'T','P45':'G'},
 'S3 Inquisition': {
   'P5':'S','P6':'T','P7':'T','P8':'T','P9':'G','P10':'T','P11':'S','P12':'T',
   'P19':'G','P41':'O','P1':'M','P3':'M','P16':'O','P30':'T','P34':'O','P39':'G','P43':'O'},
 'S4 Negotiation': {
   'P5':'S','P6':'T','P7':'T','P8':'T','P12':'T','P39':'G','P40':'T','P41':'O',
   'P42':'O','P43':'O','P44':'G','P1':'M','P3':'M','P16':'O','P2':'M'},
 'S5 Parliament': {
   'P12':'T','P13':'S','P14':'T','P15':'T','P16':'O','P17':'T','P18':'S','P19':'G',
   'P20':'T','P21':'T','P2':'G','P1':'M','P3':'M','P6':'T','P7':'T','P45':'G',
   'P22':'T','P23':'G','P26':'G','P40':'T','P31':'M'},
 'S6 Settlement': {
   'P32':'T','P33':'T','P34':'O','P29':'T','P31':'M','P36':'G','P38':'G','P19':'G',
   'P35':'G','P1':'M','P16':'O','P28':'O','P30':'T','P45':'G'},
 'S7 Territory': {
   'P32':'T','P33':'T','P34':'O','P29':'T','P31':'M','P36':'S','P37':'S','P38':'S',
   'P26':'G','P27':'G','P35':'G','P19':'G','P28':'O','P30':'T','P22':'T','P23':'G',
   'P45':'G','P1':'M','P16':'O','P41':'O','P39':'G'},
 'S8 Diplomacy': {
   'P2':'S','P28':'O','P29':'T','P31':'M','P39':'G','P40':'T','P41':'O','P42':'O',
   'P43':'O','P44':'G','P30':'T','P26':'G','P3':'T','P16':'O','P1':'M','P12':'T','P35':'O'},
}

CALLS = [('S3 Inquisition','S4 Negotiation','abjuration terms'),
         ('S7 Territory','S4 Negotiation','charter of submission'),
         ('S7 Territory','S6 Settlement','per-locality decree resolution'),
         ('S8 Diplomacy','S4 Negotiation','the table itself'),
         ('S8 Diplomacy','S5 Parliament','ratification / instructions'),
         ('S5 Parliament','S2 Tribunal','prosecution of officeholders'),
         ('S2 Tribunal','S5 Parliament','panel drawn from the house')]

n = len(SYS)
freq = defaultdict(list)
for s, d in SYS.items():
    for p in d: freq[p].append(s)

print("=== PRIMITIVE FREQUENCY (of %d systems) ===" % n)
for p in sorted(freq, key=lambda x: (-len(freq[x]), int(x[1:]))):
    roles = sorted({SYS[s][p] for s in freq[p]})
    print(f"{p:5} {NAMES.get(p,'?')[:34]:36} {len(freq[p])}/{n}  roles={''.join(roles):5} ")

print("\n=== TIERS ===")
core   = [p for p in freq if len(freq[p]) >= 7]
broad  = [p for p in freq if 4 <= len(freq[p]) <= 6]
bridge = [p for p in freq if 2 <= len(freq[p]) <= 3]
local  = [p for p in freq if len(freq[p]) == 1]
unused = [p for p in NAMES if p not in freq]
for label, grp in [('CORE (>=7)',core),('BROAD (4-6)',broad),('BRIDGE (2-3)',bridge),('LOCAL (1)',local),('UNUSED',unused)]:
    print(f"{label:14} n={len(grp):2}  " + ", ".join(sorted(grp, key=lambda x:int(x[1:]))))

print("\n=== ROLE-STABLE vs ROLE-SHIFTING (appearing in >=3 systems) ===")
for p in sorted(freq, key=lambda x:int(x[1:])):
    if len(freq[p]) < 3: continue
    roles = {SYS[s][p] for s in freq[p]}
    if len(roles) > 1:
        detail = ", ".join(f"{s.split()[0]}:{SYS[s][p]}" for s in freq[p])
        print(f"SHIFTS  {p:4} {NAMES.get(p,'')[:26]:28} {detail}")

print("\n=== PAIRWISE JACCARD (shared / union) ===")
pairs = []
for a, b in combinations(SYS, 2):
    A, B = set(SYS[a]), set(SYS[b])
    j = len(A & B) / len(A | B)
    pairs.append((j, a, b, len(A & B), len(A | B)))
pairs.sort(reverse=True)
for j, a, b, i, u in pairs:
    print(f"{j:.2f}  {a:16} {b:16} {i:2}/{u:2}")

print("\n=== MATRIX ===")
allp = sorted(freq, key=lambda x: int(x[1:]))
hdr = "      " + " ".join(s.split()[0].rjust(3) for s in SYS)
print(hdr)
for p in allp:
    row = " ".join((SYS[s][p] if p in SYS[s] else '.').rjust(3) for s in SYS)
    print(f"{p:5} {row}  {NAMES.get(p,'')[:28]}")

print("\n=== CALL GRAPH ===")
for a,b,why in CALLS: print(f"{a:16} -> {b:16}  ({why})")
callers = defaultdict(list)
for a,b,_ in CALLS: callers[b].append(a)
print("\nmost-invoked:", sorted(((len(v),k) for k,v in callers.items()), reverse=True))
