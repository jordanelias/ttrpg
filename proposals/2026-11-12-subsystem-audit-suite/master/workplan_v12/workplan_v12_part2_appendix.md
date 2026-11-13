# Valoria master workplan v12 — part 2, the tables: appendix, the scripts

## Status: PROPOSED (the appendix of `workplan_v12_part2.md`; reference: the text of the scripts that generated part 2's tables, kept so any check lane can re-run them; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the plan's other work files when v12 is adopted, its tables then regenerated or edited by each expunge)

**How to re-run.** In a scratch directory (not committed: CLAUDE.md §0.1 pt 5, these are no guard), save each script under its name and run them in this order with `python3` (3.10 or later; standard library only): each reads the parts at `proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/` by absolute path and writes its JSON beside itself. `PYTHONHASHSEED` does not matter: nothing here is drawn, and every ordering is by an explicit key. The run behind part 2 used the tree at HEAD `7257911` with this lane's edits applied (part 2 §11); `gates.py`, re-run after those edits, prints a matching after-list for every block.

| order | script | what it makes |
|---|---|---|
| 1 | `parse_parts.py` | parses the 79 body files into batches, positions, item fields (`parts.json`) |
| 2 | `summ.py` | positions by state and hash per batch; duplicates; rows with no item and items with no row (§0) |
| 3 | `graph.py` | the batch graph S, G, R, M; waves, slack, chains, the lane schedule, E-15 hours (§1; `graph.json`) |
| 4 | `gates.py` | boundary rows and `GATE: Batch` lines against the after-lists (§2; `gates.json`) |
| 5 | `hashinfo.py` | movers per batch from the position rows; the structure §2.2 tag (`hashinfo.json`) |
| 6 | `t1.py` | table 1 (the batch table) and table 3 of part 2 (the hash movers) |
| 7 | `census.py` | the file census and the same-step shared files from every `WHERE` line (§5; `census.json`) |
| 8 | `t23.py` | table 2 (the gate index) and the §5 tables |
| 9 | `tests_tbl.py` | U3 §6.1 and §6.2 matched to items; NEW test files and their creators (`tests.json`) |
| 10 | `t6.py` | the §6 tables |
| 11 | `xref.py` | cited handles that exist in no position table; `STOPS IF` and `gates on` cells naming a later batch (§2, §11) |
| 12 | `ids.py` | the id and row blocks, with the control that reproduces `workplan_v12.md` §12 (§9) |
| 13 | `req.py` | the requirement map and the milestones (§10) |
| 14 | `held_extract.py` | the intake's held entries and the trigger lines of their carry-forward blocks (§8, hand-read after) |
| 15 | `dials.py` | the dump of every block-level `DIALS AT CONTROL` line (§4, hand-made from it) |
| 16 | `totals.py` | lane H3: plan-wide positions by state (both normalisers), movers by kind, mover/EQUAL batches, hours, waves and chains (§1.2) |
| 17 | `names.py` | lane H3: every rename (`NAMES` lines) and every `NEW` name, with the flags (§12; `names.json`) |
| 18 | `carriers.py` | lane H3: `MISSING` entries, `EXISTS-IN-TREE` tokens not in the tree, `V12` handles cited before they land, U3 §6.3's rows (§13; `carriers.json`) |
| 19 | `t13.py` | lane H3: the markdown of §12 and §13's generated tables |
| 20 | `residue.py` | lane H3: gate arms that read a `## Status:` line, a document count or a document's statements (§11.2) |
| 21 | `sizes.py` | lane H3: item sizes against E-12's 6 KB cap (`V12_FOR_JORDAN.md` J-04) |

**Lane H3's edits to the scripts above** (2026-11-13): `graph.py`'s `stnorm` reads a state cell's leading word first (it had read "BUILD (HELD if …)" as HELD and B98's "BLOCKED (… reading …)" as READING); `t1.py` writes B98's and B99's rows from their positions now that part 44 gives them. Scripts 16 to 21 are new, below; run them after 1 to 5 (`names.py` before `carriers.py` and `t13.py`).

## `parse_parts.py`

```python
"""Parse the v12 body parts (workplan_v12_part3.md .. _part43_cont.md) into batches, positions and items.
Output: parts.json. Read-only over the parts."""
import re, glob, json, os, sys
D = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'            # batch number: B00..B99, B03g, B21b, B11F1, BA1, B16L
HI = HB + r'\.\d\d'                                 # item handle
def key(f):
    m = re.match(r'workplan_v12_part(\d+)(_cont(\d*))?\.md$', os.path.basename(f))
    n = int(m.group(1)); c = 0 if not m.group(2) else (1 if m.group(3) == '' else int(m.group(3)))
    return (n, c)
files = sorted([f for f in glob.glob(f'{D}/workplan_v12_part*.md') if re.search(r'part\d+(_cont\d*)?\.md$', f)], key=key)
files = [f for f in files if key(f)[0] >= 3]
def short(h):
    m = re.match(r'(' + HB + r')', h); return m.group(1) if m else None
BLOCK_LABELS = r'(INVOCATION|IN-FLIGHT ROW|GATE|REQUIREMENT|BATCH GATE|RE-PIN|IDS|DIALS AT CONTROL|C\([^)]*\)|SERIAL EDGES|FILE CENSUS|PARALLEL|COST|EST|UNDECIDED|BACKGROUND RUN|SOFT EDGE|EXPECTED RED UNTIL|RULES)'
batches, items, order = {}, {}, []
for f in files:
    fn = os.path.basename(f); cur = None; curitem = None; field = None; ifield = None
    for ln, l in enumerate(open(f, encoding='utf-8'), 1):
        l = l.rstrip('\n')
        m = re.match(r'^## Batch (' + HB + r')(\S*)(.*)$', l)
        if m:
            cur = m.group(1); curitem = None; field = None
            b = batches.setdefault(cur, {'handle': cur + m.group(2), 'heads': [], 'files': [], 'fields': {}, 'gates': [], 'positions': []})
            b['heads'].append((fn, ln, l))
            if fn not in b['files']: b['files'].append(fn)
            if cur not in order: order.append(cur)
            continue
        m = re.match(r'^### (' + HI + r')\b(.*)$', l)
        if m:
            h = m.group(1); curitem = h; ifield = None; field = None
            bb = short(h)
            if cur != bb:   # item outside its batch block: note it
                cur = bb
                b = batches.setdefault(cur, {'handle': cur, 'heads': [], 'files': [], 'fields': {}, 'gates': [], 'positions': []})
            if fn not in batches[cur]['files']: batches[cur]['files'].append(fn)
            it = items.setdefault(h, {'heads': [], 'fields': {}, 'files': []})
            it['heads'].append((fn, ln, l))
            if fn not in it['files']: it['files'].append(fn)
            continue
        if l.startswith('## ') or l.startswith('### '):
            curitem = None; field = None; ifield = None
            # a heading like "## Readings" ends the item
            continue
        m = re.match(r'^\| (' + HI + r') \|(.*)$', l)
        if m:
            cells = [c.strip().replace('\x00', '|') for c in l.strip().strip('|').replace('\\|', '\x00').split('|')]
            bb = short(m.group(1))
            if bb in batches:
                batches[bb]['positions'].append({'pos': cells[0], 'cells': cells, 'file': fn, 'line': ln})
            field = None; continue
        if curitem is None and cur:
            m = re.match(r'^' + BLOCK_LABELS + r'( \([^)]*\))?:(.*)$', l)
            if m and not l.startswith('- '):
                lab = m.group(1); field = lab
                if lab == 'GATE':
                    batches[cur]['gates'].append((fn, ln, l))
                    field = None
                else:
                    batches[cur]['fields'].setdefault(lab, []).append([fn, ln, l])
                continue
            if field and l.startswith(' ') and l.strip():
                batches[cur]['fields'][field][-1][2] += '\n' + l
                continue
            if not l.strip() or l.startswith('|'): field = None
        if curitem:
            m = re.match(r'^- ([A-Z][A-Z &-]+?)( \([^)]*\))?:(.*)$', l)
            if m:
                ifield = m.group(1); items[curitem]['fields'].setdefault(ifield, []).append([fn, ln, l]); continue
            if ifield and l.startswith(' ') and l.strip():
                items[curitem]['fields'][ifield][-1][2] += '\n' + l; continue
            if not l.strip(): ifield = None
json.dump({'order': order, 'batches': batches, 'items': items, 'files': [os.path.basename(x) for x in files]}, open('parts.json', 'w'), indent=0)
print('files', len(files), 'batches', len(batches), 'items(headed)', len(items))
print('order', ' '.join(order))
```

## `summ.py`

```python
import json,re,collections
P=json.load(open('parts.json'))
B=P['batches']; I=P['items']
def stnorm(s):
    s=s.upper()
    for k in ['DESIGN-FIRST','POINTER','READING','HELD','BLOCKED','CONTENT','BUILD','GIT']:
        if k in s: return k
    return 'OTHER:'+s[:20]
def hnorm(s):
    u=s.upper()
    if 'ENCODING' in u and 'BEHAV' in u: return 'MB+E'
    if 'ENCODING' in u: return 'ME'
    if 'BEHAV' in u: return 'MB'
    if 'MOVER' in u or 'RE-PIN' in u: return 'M?'
    if 'EQUAL' in u: return 'EQ'
    return '-'
for b in P['order']:
    ps=B[b]['positions']
    seen=collections.OrderedDict()
    dups=[]
    for p in ps:
        if p['pos'] in seen: dups.append(p['pos'])
        seen[p['pos']]=p
    st=collections.Counter(stnorm(p['cells'][3]) if len(p['cells'])>3 else 'X' for p in seen.values())
    hs=collections.Counter(hnorm(p['cells'][4]) if len(p['cells'])>4 else 'X' for p in seen.values())
    heads=[h for h in I if h.startswith(b+'.') and re.match(re.escape(b)+r'\.\d\d$',h)]
    nohead=[p for p in seen if p not in I]
    noprow=[h for h in heads if h not in seen]
    print(b, len(seen), dict(st), dict(hs), 'heads',len(heads), 'dup',dups[:5], 'rowNoItem',nohead[:6], 'itemNoRow',noprow[:6], '99' , (b+'.99') in seen)
```

## `graph.py`

```python
"""Batch graph for workplan v12 part 2 (H2): structure §2.1's `after` column (S) + every part's `GATE: Batch` lines (G)
+ the 20 edges H2_DECISIONS.md recommends (R); the five edges it advises against become merge-order constraints (M).
Prints acyclicity, waves, slack, the lane schedule, the critical path by steps and by E-15 hours. Writes graph.json."""
import re, json, sys
from collections import defaultdict, Counter
D = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
P = json.load(open('parts.json'))
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
def short(h):
    m = re.match(r'(' + HB + r')', h); return m.group(1) if m else None
# --- S: structure §2.1
rows, name, lane, s_wave, s_step = [], {}, {}, {}, {}
for l in open(f'{D}/V12_STRUCTURE.md', encoding='utf-8'):
    m = re.match(r'^\| (B\S+) \| ([A-Z+]+) \| W(\d+) \| S(\d+)[^|]*\| (\d+) \| (.*) \|$', l)
    if not m: continue
    b = short(m.group(1)); rows.append(b); name[b] = m.group(1); lane[b] = m.group(2)
    s_wave[b] = int(m.group(3)); s_step[b] = int(m.group(4))
    aft = m.group(6)
    S_after = set() if aft.strip() in ('—',) else ({x for x in rows if x not in ('B99',)} if 'every batch' in aft else {short(a) for a in re.findall(HB, aft)})
    name[b + '_after'] = sorted(S_after - {b})
S = {(a, b) for b in rows for a in name[b + '_after']}
# B98: every batch but B99; B99: every batch
S = {(a, b) for (a, b) in S if b not in ('B98', 'B99')}
S |= {(a, 'B98') for a in rows if a not in ('B98', 'B99')} | {(a, 'B99') for a in rows if a != 'B99'}
# --- G: GATE: Batch lines in the parts
G = set(); Gsrc = defaultdict(list)
for b, bb in P['batches'].items():
    for fn, ln, l in bb['gates']:
        for a in re.findall(r'Batch (' + HB + r')', l)[:1]:
            if a != b: G.add((a, b)); Gsrc[(a, b)].append(f'{fn}:{ln}')
# --- R: the 20 recommended edges (H2_DECISIONS.md HD-01..HD-16)
R = {('B11','B16'):'HD-01', ('B04','B08'):'HD-02', ('B05','B08'):'HD-02', ('B06','B08'):'HD-02', ('B16','B34'):'HD-05',
     ('B22','B30'):'HD-07', ('B29','B19'):'HD-09', ('B17','B41'):'HD-10', ('B20','B41'):'HD-10', ('B29','B37'):'HD-11',
     ('B34','B20'):'HD-12', ('B21d','B40'):'HD-13', ('B21d','B33'):'HD-13', ('B27','B28'):'HD-14', ('B24a','B21s'):'HD-14',
     ('B29','B21s'):'HD-14', ('B21s','B33'):'HD-14', ('B20','B31'):'HD-15', ('B22','B31'):'HD-15', ('B24a','B28'):'HD-16'}
M = {('B11','B21'):'HD-03', ('B12a','B21b'):'HD-04', ('B28','B32'):'HD-06', ('B25','B27'):'HD-08', ('B12c','B24a'):'HD-17'}
LANE_ORDER = [('B29', 'B18'), ('BA1', 'B08')]      # D-20 (PC lane: B29 before B18); IS-A §12.3 item 1 (IN lane: BA1 before B08); lane order, not edges
EXCLUSIVE = {'B03a', 'B05'}                        # structure §2.3: alone in their step
CAP = 6                                            # structure §2.3: at most six open batches in a step
nodes = list(rows)
def analyse(E, label):
    after = defaultdict(set); succ = defaultdict(set)
    for a, b in E: after[b].add(a); succ[a].add(b)
    indeg = {h: len(after[h]) for h in nodes}; ready = [h for h in nodes if indeg[h] == 0]; topo = []
    while ready:
        h = ready.pop(0); topo.append(h)
        for s in sorted(succ[h], key=nodes.index):
            indeg[s] -= 1
            if indeg[s] == 0: ready.append(s)
    if len(topo) != len(nodes):
        return {'acyclic': False, 'cycle': [h for h in nodes if indeg[h] > 0]}
    wave = {}
    for h in topo: wave[h] = 1 + max((wave[a] for a in after[h]), default=-1)
    W = max(wave.values()); latest = {}
    for h in reversed(topo): latest[h] = min((latest[s] - 1 for s in succ[h]), default=W)
    slack = {h: latest[h] - wave[h] for h in nodes}
    def chains(h):
        preds = [a for a in after[h] if wave[a] == wave[h] - 1]
        return [[h]] if not preds else [c + [h] for a in sorted(preds, key=nodes.index) for c in chains(a)]
    allc = [c for e in nodes if wave[e] == W for c in chains(e)]
    lanes = lambda h: set(lane[h].split('+'))
    pri = sorted(nodes, key=lambda h: (slack[h], s_step[h], nodes.index(h)))   # least slack first (critical path), then the structure's step order
    done, step, sched, left = {}, 0, [], list(pri)
    while left:
        used, opened, grew = set(), [], True
        while grew:                                # repeat: a merge-order or lane-order pair may open later in the pass
            grew = False
            for h in left:
                if h in opened or not all(a in done and done[a] < step for a in after[h]): continue
                if any(y == h and x not in done and x not in opened for x, y in LANE_ORDER): continue
                if any(y == h and x not in done and x not in opened for (x, y) in M): continue
                if lanes(h) & used or len(opened) >= CAP: continue
                if opened and (h in EXCLUSIVE or any(o in EXCLUSIVE for o in opened)): continue
                opened.append(h); used |= lanes(h); grew = True; break
        for h in opened: done[h] = step; left.remove(h)
        sched.append(sorted(opened, key=nodes.index)); step += 1
    stepof = {h: i for i, s in enumerate(sched) for h in s}
    return {'acyclic': True, 'wave': wave, 'W': W, 'slack': slack, 'chains': allc, 'sched': sched, 'step': stepof,
            'after': {h: sorted(after[h], key=nodes.index) for h in nodes}, 'topo': topo}
# --- positions and E-15 estimates
def stnorm(s):                                      # the state cell's leading word (lane H3: "BUILD (HELD if …)" is BUILD); else the first listed word anywhere
    u = s.upper(); ks = ['DESIGN-FIRST', 'POINTER', 'READING', 'HELD', 'BLOCKED', 'CONTENT', 'BUILD', 'GIT']
    for k in ks:
        if u.lstrip('*` ').startswith(k): return k
    for k in ks:
        if k in u: return k
    return 'OTHER'
pos = {}; states = {}
for b in nodes:
    if b not in P['batches']: continue
    seen = {}
    for p in P['batches'][b]['positions']: seen.setdefault(p['pos'], p)
    pos[b] = len(seen); states[b] = Counter(stnorm(p['cells'][3]) for p in seen.values())
CALIB = {'B02', 'B05', 'B15', 'B19', 'B19a', 'B98', 'B99'}   # B98: its probes (part 44 EST); B99: the long re-take (repair lane R1)
est = {b: round(0.4 * pos[b] + 2.5 + (2 if b in CALIB else 0), 1) for b in pos}
est.setdefault('B98', 8.0); est.setdefault('B99', 5.0)   # the structure's guesses, kept only for a batch with no positions (repair lane R1: part 44 gives both)
def hours_path(res):
    best, prev = {}, {}
    for h in res['topo']:
        ps = res['after'][h]
        if ps:
            p = max(ps, key=lambda a: best[a]); best[h] = best[p] + est[h]; prev[h] = p
        else: best[h] = est[h]; prev[h] = None
    end = max(best, key=best.get); path = [end]
    while prev[path[-1]]: path.append(prev[path[-1]])
    return round(best[end], 1), path[::-1]
out = {}
for label, E in [('S', S), ('S+G', S | G), ('S+G+R', S | G | set(R)), ('S+G+R+M', S | G | set(R) | set(M))]:
    r = analyse(E, label)
    if not r['acyclic']: print(label, 'CYCLIC', r['cycle']); continue
    hp = hours_path(r)
    print(f"{label}: edges {len(E)}; acyclic; waves W0..W{r['W']} ({r['W']+1}); steps {len(r['sched'])}; longest chains {len(r['chains'])}; hours path {hp[0]} h: {' > '.join(hp[1])}")
    out[label] = r; out[label]['hours'] = hp
r = out['S+G+R']
print('serial sum', round(sum(est.values()), 1), 'h; makespan (longest batch per step)', round(sum(max(est[h] for h in s) for s in r['sched']), 1))
print('G edges not in S:', sorted(G - S)); print('G-S not in R:', sorted((G - S) - set(R)))
print('R edges already in G:', sorted(set(R) & G))
for i, s in enumerate(r['sched']): print(f'S{i}', ' '.join(f'{h}({lane[h]})' for h in s))
print('chains (steps):'); [print('  ', ' > '.join(c)) for c in r['chains']]
print('merge-order pairs, steps:', [(a, b, r['step'][a], r['step'][b]) for a, b in M])
print('wave changes vs structure:', [(h, s_wave[h], r['wave'][h]) for h in nodes if s_wave[h] != r['wave'][h]])
print('step changes vs structure:', [(h, s_step[h], r['step'][h]) for h in nodes if s_step[h] != r['step'][h]])
json.dump({'nodes': nodes, 'name': {b: name[b] for b in nodes}, 'lane': lane, 's_wave': s_wave, 's_step': s_step,
           'S': sorted(S), 'G': sorted(G), 'Gsrc': {f'{a}>{b}': v for (a, b), v in Gsrc.items()}, 'R': {f'{a}>{b}': v for (a, b), v in R.items()},
           'M': {f'{a}>{b}': v for (a, b), v in M.items()}, 'pos': pos, 'states': {b: dict(v) for b, v in states.items()}, 'est': est,
           'res': {k: {kk: vv for kk, vv in v.items() if kk != 'topo'} for k, v in out.items()}}, open('graph.json', 'w'), indent=0, default=list)
```

## `gates.py`

```python
"""Table 2: boundary rows and GATE: Batch lines per batch, checked against the recomputed graph (S+G+R)."""
import json, re, glob, os
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
D = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
r = G['res']['S+G+R']; nodes = G['nodes']; name = G['name']
stops = {}
for f in P['files']:
    for ln, l in enumerate(open(f'{D}/{f}', encoding='utf-8'), 1):
        m = re.match(r'^\| STOP\. Batch (\S+) closes here', l)
        if m: stops.setdefault(re.match('(' + HB + ')', m.group(1)).group(1), []).append((f, ln, l.strip(), m.group(1)))
rows = []
for b in nodes:
    if b in ('B98', 'B99'): continue
    gl = P['batches'][b]['gates']
    named = []
    for fn, ln, l in gl:
        a = re.findall(r'Batch (' + HB + r')', l)
        if a: named.append(a[0])
    after = set(r['after'][b]); later = [a for a in named if r['step'].get(a, 99) >= r['step'][b]]
    st = stops.get(b, [])
    exact = [s for s in st if s[2] == f'| STOP. Batch {name[b]} closes here |']
    rows.append((b, st, exact, named, sorted(after - set(named), key=nodes.index), sorted(set(named) - after), later))
    print(b, 'STOP', [(s[0], s[1]) for s in st], 'exact' if exact else ('NOT EXACT: ' + (st[0][2][:80] if st else 'NONE')),
          '| gates', len(named), '| missing', sorted(after - set(named), key=nodes.index), '| extra', sorted(set(named) - after), '| later', later)
json.dump({b: {'stop': st, 'exact': bool(ex), 'named': nm, 'missing': mi, 'extra': xt, 'later': la} for b, st, ex, nm, mi, xt, la in rows}, open('gates.json', 'w'))
```

## `hashinfo.py`

```python
import json,re
P=json.load(open('parts.json')); G=json.load(open('graph.json'))
D='/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
s22={}
for l in open(f'{D}/V12_STRUCTURE.md',encoding='utf-8'):
    m=re.match(r'^\| (B\S+|BA1) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (\d+) \|$',l)
    if m: s22[re.match('('+HB+')',m.group(1)).group(1)]=m.group(4)
def kind(c):
    u=c.upper()
    if 'MOVER' not in u: return None
    b='BEHAV' in u; e='ENCOD' in u
    return 'B+E' if b and e else 'E' if e else 'B' if b else '?'
info={}
for b in G['nodes']:
    if b not in P['batches']: continue
    seen={}
    for p in P['batches'][b]['positions']: seen.setdefault(p['pos'],p)
    mv={'B':[],'E':[],'?':[]}
    for h,p in seen.items():
        c=p['cells'][4] if len(p['cells'])>4 else ''
        k=kind(c)
        if not k: continue
        if h.endswith('.99') or 're-pin' in c.lower(): continue   # the re-pin row itself is not a mover
        if k=='B+E': mv['B'].append(h); mv['E'].append(h)
        else: mv[k].append(h)
    head=P['batches'][b]['heads'][0][2] if P['batches'][b]['heads'] else ''
    hh=re.search(r'HASH (.*)$',head); hh=hh.group(1) if hh else ''
    has99=(b+'.99') in seen
    info[b]={'mv':mv,'head':hh,'s22':s22.get(b,''),'has99':has99}
    print(b, '| head:',hh[:50],'| s22:',s22.get(b,'')[:40],'| B',len(mv['B']),'E',len(mv['E']),'?',mv['?'][:4],'| .99',has99)
json.dump(info,open('hashinfo.json','w'))
```

## `t1.py`

```python
"""Table 1 (the batch table) and table 4 (the hash movers), generated from parts.json, graph.json, hashinfo.json."""
import json, re
P = json.load(open('parts.json')); G = json.load(open('graph.json')); H = json.load(open('hashinfo.json'))
r = G['res']['S+G+R']; nodes = G['nodes']; name = G['name']; lane = G['lane']
S = {tuple(e) for e in G['S']}; GG = {tuple(e) for e in G['G']}; R = {tuple(k.split('>')): v for k, v in G['R'].items()}
M = {tuple(k.split('>')): v for k, v in G['M'].items()}
def pf(f):
    m = re.match(r'workplan_v12_part(\d+)(_cont\d*)?\.md', f); return m.group(1) + (m.group(2) or '')
def files(b):
    fs = list(P['batches'][b]['files'])
    for p in P['batches'][b]['positions']:
        if p['file'] not in fs: fs.append(p['file'])
    return ', '.join(pf(f) for f in sorted(set(fs), key=lambda f: (int(re.search(r'part(\d+)', f).group(1)), f)))
def aest(b):
    v = [re.search(r'EST(?: \([^)]*\))?:\s*(?:about |~)?(\d+(?:\.\d+)?)', t) for _, _, t in P['batches'][b]['fields'].get('EST', [])]
    v = [float(x.group(1)) for x in v if x]
    return '+'.join(f'{x:g}' for x in v) if v else '—'
ab = {'BUILD': 'B', 'POINTER': 'P', 'READING': 'R', 'HELD': 'H', 'BLOCKED': 'BL', 'CONTENT': 'C', 'DESIGN-FIRST': 'DF', 'GIT': 'G', 'OTHER': '?'}
def hashtag(b):
    if b not in H: return 'MOVER (B98: every realm pin)' if b == 'B98' else 'EQUAL (a reading batch)'
    mv = H[b]['mv']; nb, ne, nq = len(mv['B']), len(mv['E']), len(mv['?'])
    if nb + ne + nq == 0: return 'EQUAL'
    k = []
    if nb: k.append(f'behaviour {nb}')
    if ne: k.append(f'encoding {ne}')
    if nq: k.append(f'conditional {nq}')
    return 'MOVER (' + ', '.join(k) + ')'
s22 = lambda b: 'EQUAL' if H.get(b, {}).get('s22', '').startswith('EQUAL') else ('MOVER' if 'MOVER' in H.get(b, {}).get('s22', '') or 'mover' in H.get(b, {}).get('s22', '') or 're-pin' in H.get(b, {}).get('s22', '') else H.get(b, {}).get('s22', '—')[:20])
rows = []
rows.append('| batch | lane | wave (§2.1 → now) | step (§2.1 → now) | slack | part files | positions: total (by state) | hash, from the position rows (§2.2 said) | est. h (E-15) | after: every `GATE: Batch` it needs (`+G` a part\'s GATE line §2.1 lacked; `+R` an edge H2 adopts) |')
rows.append('|---|---|---|---|---|---|---|---|---|---|')
tot = 0
for b in nodes:
    w0, w1 = G['s_wave'][b], r['wave'][b]; s0, s1 = G['s_step'][b], r['step'][b]
    wv = f'W{w1}' if w0 == w1 else f'W{w0} → **W{w1}**'
    st = f'S{s1}' if s0 == s1 else f'S{s0} → **S{s1}**'
    if b in ('B98', 'B99') and not G['pos'].get(b):   # lane H3: part 44 gives both positions; this row only for a batch with none
        aft = 'every batch but B99' if b == 'B98' else 'every batch'
        rows.append(f"| {name[b]} | {lane[b]} | {wv} | {st} | {r['slack'][b]} | 44 (lane A44, not yet written) | — (A44) | {hashtag(b)} | {G['est'][b]:g} (the structure's figure; no positions yet) | {aft} |")
        continue
    stc = G['states'][b]; n = G['pos'][b]; tot += n
    sts = ' '.join(f"{ab[k]}{v}" for k, v in sorted(stc.items(), key=lambda x: list(ab).index(x[0])))
    aft = [] if b not in ('B98', 'B99') else ['every batch but B99' if b == 'B98' else 'every batch']
    for a in (r['after'][b] if b not in ('B98', 'B99') else []):
        t = a
        if (a, b) in R: t += ' +R'
        elif (a, b) in GG and (a, b) not in S: t += ' +G'
        aft.append(t)
    hs = hashtag(b); old = s22(b)
    hcell = hs if (old == 'EQUAL') == (hs == 'EQUAL') else f'**{hs}** (§2.2: {old})'
    if not H[b]['has99']: hcell += '; no `.99` row (C-01)'
    rows.append(f"| {name[b]} | {lane[b]} | {wv} | {st} | {r['slack'][b]} | {files(b)} | {n} ({sts}) | {hcell} | {G['est'][b]:g} | {', '.join(aft) if aft else '—'} |")
open('t1.md', 'w').write('\n'.join(rows) + '\n')
print('positions total', tot, '| rows', len(rows) - 2)
# table 4: hash movers per batch
h4 = ['| step | batch | behaviour movers (position handles) | encoding movers | conditional movers | the re-pin position and what its text says | merge position in its step |', '|---|---|---|---|---|---|---|']
def repin_text(b):
    it = P['items'].get(b + '.99')
    if not it: return None
    t = ' '.join(x[2] for v in it['fields'].values() for x in v) + it['heads'][0][2]
    return ('re-pin' in t.lower() or 're-record' in t.lower(), 'EQUAL' in t)
for i, stepb in enumerate(r['sched']):
    movers = [b for b in stepb if b in H and sum(len(v) for v in H[b]['mv'].values())]
    for b in stepb:
        if b in ('B98', 'B99'):
            h4.append(f"| S{i} | {b} | (A44) | — | — | `{b}.99` (A44 writes it) | {'alone' if len(stepb) == 1 else ''} |"); continue
        mv = H[b]['mv']
        if not any(mv.values()):
            rp = repin_text(b)
            h4.append(f"| S{i} | {b} | — | — | — | {'`'+b+'.99` records the EQUAL reading' if rp else 'no `.99` (C-01): the last item records the EQUAL reading'} | any (EQUAL, §7.4) |"); continue
        rp = repin_text(b)
        if rp: rpc = f'`{b}.99`' + ('' if rp[0] else ' — its text names no re-pin (check)')
        else:
            last = P['batches'][b]['positions'][-1]['pos']; rpc = f'no `.99`: the re-pin rides `{last}` (C-01)'
        pos = movers.index(b) + 1
        h4.append(f"| S{i} | {b} | {', '.join(x.split('.')[1] for x in mv['B']) or '—'} | {', '.join(x.split('.')[1] for x in mv['E']) or '—'} | {', '.join(x.split('.')[1] for x in mv['?']) or '—'} | {rpc} | {pos} of {len(movers)} movers |")
open('t4.md', 'w').write('\n'.join(h4) + '\n')
nb = sum(len(H[b]['mv']['B']) for b in H); ne = sum(len(H[b]['mv']['E']) for b in H); nq = sum(len(H[b]['mv']['?']) for b in H)
mb = [b for b in H if any(H[b]['mv'].values())]
print('movers: behaviour', nb, 'encoding', ne, 'conditional', nq, '| mover batches', len(mb), '| EQUAL batches', len(H) - len(mb))
print('mover batches without .99:', [b for b in mb if not H[b]['has99']], '| EQUAL without .99:', [b for b in H if b not in mb and not H[b]['has99']])
print('.99 with no re-pin word:', [b for b in mb if H[b]['has99'] and not repin_text(b)[0]])
```

## `census.py`

```python
"""Tables 3 and 6: the file census from every item's WHERE line, the serial edges between batches that share a file,
the tests and probes items create, and the tools/exporters/modules/harness files created. Writes census.json."""
import json, re
from collections import defaultdict, OrderedDict
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
r = G['res']['S+G+R']; nodes = G['nodes']; step = r['step']
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
SEASON_DIRS = ('data/', 'loop/', 'queries/', 'decision/', 'seam/', 'state/', 'harness/', 'boot/', 'tests/', 'cases/', 'runs/')
SEASON_FILES = {'rosters.yaml', 'verb_table.yaml', 'offices.yaml', 'write_matrix.yaml', 'hole_register.yaml',
                'requirements.yaml', 'arrangements.yaml', 'npcs.yaml', 'goals.yaml', 'worldgen.yaml', 'telling.yaml'}
def norm(p):
    p = p.strip().strip('`').split('::')[0].split(' ')[0].rstrip(',;:')
    if not re.search(r'\.(py|yaml|yml|json|md|jsonl|gd|tres|txt|csv)$', p) and not p.endswith('/'): return None
    if p.startswith('S/'): p = 'engine/season/' + p[2:]          # part 41's abbreviation
    if p.startswith('engine/season/'): return p
    if p.startswith(SEASON_DIRS): return 'engine/season/' + p
    if p in SEASON_FILES: return 'engine/season/' + p
    return p
def batch_of(h): return re.match('(' + HB + ')', h).group(1)
def posidx(h):
    b = batch_of(h); ps = [p['pos'] for p in P['batches'][b]['positions']]
    return ps.index(h) if h in ps else 999
edits = defaultdict(list); new = defaultdict(list); dele = defaultdict(list)
for h, it in P['items'].items():
    b = batch_of(h)
    if b not in step: continue
    w = ' '.join(x[2] for x in it['fields'].get('WHERE', []))
    for m in re.finditer(r'(NEW |DELETE |new |delete )?`([^`]+)`', w):
        f = norm(m.group(2))
        if not f or f.startswith(('http',)) or ' ' in f: continue
        (new if m.group(1) and m.group(1).strip().lower() == 'new' else dele if m.group(1) and m.group(1).strip().lower() == 'delete' else edits)[f].append(h)
        if m.group(1) and m.group(1).strip().lower() in ('new', 'delete'): edits[f].append(h)
order_key = lambda h: (step[batch_of(h)], nodes.index(batch_of(h)), posidx(h))
census = OrderedDict()
for f in sorted(edits, key=lambda f: (-len(set(edits[f])), f)):
    its = sorted(set(edits[f]), key=order_key)
    bs = list(OrderedDict.fromkeys(batch_of(h) for h in its))
    census[f] = {'items': its, 'batches': bs, 'hot': len(its) >= 20, 'new': sorted(set(new.get(f, [])), key=order_key), 'delete': sorted(set(dele.get(f, [])), key=order_key)}
multi = {f: c for f, c in census.items() if len(c['batches']) >= 2}
print('files named in WHERE:', len(census), '| in two or more batches:', len(multi), '| hot (>=20 items):', sum(c['hot'] for c in census.values()))
# serial edges: consecutive batches on a file; same-step pairs
pairs = defaultdict(set); same = defaultdict(set)
for f, c in multi.items():
    bs = c['batches']
    for a, b in zip(bs, bs[1:]):
        pairs[(a, b)].add(f)
        if step[a] == step[b]: same[(a, b)].add(f)
print('serial pairs:', len(pairs), '| same-step pairs:', len(same))
for (a, b), fs in sorted(same.items(), key=lambda x: (step[x[0][0]], nodes.index(x[0][0]))):
    print(f'  S{step[a]} {a} -> {b}:', ', '.join(sorted(fs))[:300])
json.dump({'census': census, 'same': {f'{a}>{b}': sorted(v) for (a, b), v in same.items()}, 'pairs': {f'{a}>{b}': sorted(v) for (a, b), v in pairs.items()}}, open('census.json', 'w'))
```

## `t23.py`

```python
"""Table 2 (boundary rows and GATE lines) and table 3 (serial edges; the file census), from gates.json, census.json, graph.json."""
import json, re
from collections import OrderedDict
G = json.load(open('graph.json')); GT = json.load(open('gates.json')); CJ = json.load(open('census.json'))
r = G['res']['S+G+R']; nodes = G['nodes']; step = r['step']; name = G['name']
U3 = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/unified/U3_DEPENDENCY_ORDER.md'
pf = lambda f: re.sub(r'workplan_v12_part(\d+)(_cont\d*)?\.md', r'\1\2', f)
EDITED = {'B19': 'B29', 'B28': 'B24a', 'B33': 'B21d, B21s', 'B37': 'B29', 'B40': 'B21d', 'B41': 'B17, B20'}
t2 = ['| batch | its boundary row (part:line) | exact text | `GATE: Batch` lines | equal to its after-list in §1 | names a batch closing at or after its own step | H2 added |', '|---|---|---|---|---|---|---|']
for b in nodes:
    if b in ('B98', 'B99'):
        t2.append(f'| {name[b]} | part 44 (A44) | — | — | — | — | — |'); continue
    g = GT[b]; st = g['stop'][0] if g['stop'] else None
    t2.append(f"| {name[b]} | {pf(st[0]) + ':' + str(st[1]) if st else 'NONE'} | {'yes' if g['exact'] else 'NO'} | {len(g['named'])} | {'yes' if not g['missing'] and not g['extra'] else 'missing ' + ', '.join(g['missing'])} | {', '.join(g['later']) or 'none'} | {EDITED.get(b, '—')} |")
open('t2.md', 'w').write('\n'.join(t2) + '\n')
PERM = {'engine/season/hole_register.yaml', 'engine/season/requirements.yaml', 'unified/U1_GLOSSARY.md', 'references/id_reservations.yaml', 'references/restructure_ledger.md', 'CURRENT.md'}
REPIN = {'engine/season/tests/_realm_goldens.py'}
perm = lambda f: f in PERM or f.startswith('registers/')
C = CJ['census']
# same-step pairs (serial edges inside a step), excluding the permanent surface and the pin file (§7.4 handles it)
t3a = ['| step | earlier → later (merge order: §2.1 order) | files both edit (permanent surface and the pin file left out) | hot files among them |', '|---|---|---|---|']
n3a = 0
for k, fs in sorted(CJ['same'].items(), key=lambda x: (step[x[0].split('>')[0]], nodes.index(x[0].split('>')[0]), nodes.index(x[0].split('>')[1]))):
    a, b = k.split('>'); fs = [f for f in fs if not perm(f) and f not in REPIN]
    if not fs: continue
    hot = [f.split('/')[-1] for f in fs if C[f]['hot']]
    t3a.append(f"| S{step[a]} | {a} → {b} | {', '.join('`' + f.replace('engine/season/', '') + '`' for f in fs)} | {', '.join(hot) or '—'} |"); n3a += 1
open('t3a.md', 'w').write('\n'.join(t3a) + '\n')
# census
u3 = {}
for l in open(U3, encoding='utf-8').read().split('\n')[1046:1194]:
    m = re.match(r'^\| `([^`]+)` \| (.*?) \| (.*?) \|', l)
    if m: u3[m.group(1).split('/')[-1].rstrip('?')] = [x.strip().split(' ')[0] for x in m.group(3).split('→')]
rows = ['| file (`engine/season/` dropped) | items that edit it, in landing order (a hot file: count per batch) | batches in landing order | hot | U3 §5.1 |', '|---|---|---|---|---|']
multi = [(f, c) for f, c in C.items() if len(c['batches']) >= 2 and not perm(f)]
multi.sort(key=lambda x: (-len(x[1]['items']), x[0]))
for f, c in multi:
    if c['hot']:
        cnt = OrderedDict()
        for h in c['items']: cnt[re.match(r'(\S+)\.', h).group(1)] = cnt.get(re.match(r'(\S+)\.', h).group(1), 0) + 1
        its = f"{len(c['items'])}: " + ', '.join(f'{b} {n}' for b, n in cnt.items())
    else:
        its = ', '.join(c['items'])
    base = f.rstrip('/').split('/')[-1]
    u = 'listed' if base in u3 else '**not listed**'
    rows.append(f"| `{f.replace('engine/season/', '')}` | {its} | {' → '.join(c['batches'])} | {'hot' if c['hot'] else ''} | {u} |")
open('t3b.md', 'w').write('\n'.join(rows) + '\n')
single = [f for f, c in C.items() if len(c['batches']) == 1]
named_bases = {f.rstrip('/').split('/')[-1] for f in C}
u3_absent = sorted(b for b in u3 if b not in named_bases)
print('t2 rows', len(t2) - 2, '| same-step pairs kept', n3a, '| census rows', len(multi), '| single-batch files', len(single),
      '| U3 §5.1 rows', len(u3), '| U3 rows no item names:', u3_absent, '| not in U3:', sum(1 for f, c in multi if f.rstrip('/').split('/')[-1] not in u3))
json.dump({'single': len(single), 'u3_absent': u3_absent, 'n_u3': len(u3), 'multi': len(multi), 'notu3': sum(1 for f, c in multi if f.rstrip('/').split('/')[-1] not in u3)}, open('t3meta.json', 'w'))
```

## `tests_tbl.py`

```python
"""Table 6: U3 §6.1 test files and §6.2 probes matched to v12 items; every NEW test file and its creator;
tools/exporters/modules/harness files an item creates. Writes tests.json."""
import json, re
from collections import defaultdict
P = json.load(open('parts.json')); G = json.load(open('graph.json')); C = json.load(open('census.json'))['census']
U3 = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/unified/U3_DEPENDENCY_ORDER.md'
L = open(U3, encoding='utf-8').read().split('\n')
sec = lambda a, b: L[a - 1:b]
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
def text(it): return ' '.join(x[2] for v in it['fields'].values() for x in v) + ' ' + ' '.join(h[2] for h in it['heads'])
alltext = {h: text(it) for h, it in P['items'].items()}
r61, r62 = [], []
for l in sec(1197, 1229):
    m = re.match(r'^\| `([^`]+)` \| (.*?) \| (\w+) \| (.*) \|$', l)
    if m: r61.append((m.group(1), m.group(2), m.group(3), m.group(4)))
for l in sec(1230, 1307):
    m = re.match(r'^\| `([^`]+)` \((\S+)\) \| (.*) \|$', l)
    if m: r62.append((m.group(1), m.group(2), re.findall(r'`([^`]+)`', m.group(3))))
out61 = []
for name, by, status, must in r61:
    stem = name.split('/')[-1]
    hits = sorted([h for h, t in alltext.items() if stem in t], key=lambda h: (G['res']['S+G+R']['step'].get(re.match('(' + HB + ')', h).group(1), 99), h))
    out61.append({'file': name, 'by': by, 'status': status, 'items': hits[:6], 'n': len(hits)})
out62 = []
for prop, b, probes in r62:
    pitems = [h for h, t in alltext.items() if prop in t]
    for pr in probes:
        hits = [h for h, t in alltext.items() if pr in t]
        out62.append({'proposal': prop, 'batch': b, 'probe': pr, 'items_naming_probe': sorted(hits)[:5], 'items_of_proposal': len(pitems)})
print('6.1 rows', len(out61), 'unmatched', [o['file'] for o in out61 if not o['n']])
print('6.2 probes', len(out62), 'named by no item', len([o for o in out62 if not o['items_naming_probe']]),
      '| proposal carried by no item', sorted({o['proposal'] for o in out62 if not o['items_of_proposal']}))
newtests = {f: c['new'] for f, c in C.items() if c['new'] and re.search(r'(^|/)test_[^/]*\.py$', f)}
dup = {f: v for f, v in newtests.items() if len(v) > 1}
created = {f: c['new'] for f, c in C.items() if c['new'] and not re.search(r'(^|/)test_[^/]*\.py$', f)}
json.dump({'u61': out61, 'u62': out62, 'newtests': newtests, 'dup': dup, 'created': created}, open('tests.json', 'w'))
print('NEW test files', len(newtests), 'dup', dup)
```

## `t6.py`

```python
"""Table 6: tests and probes to write; tools, exporters, modules and harness files created, with the caller each item names."""
import json, re
P = json.load(open('parts.json')); G = json.load(open('graph.json')); T = json.load(open('tests.json'))
step = G['res']['S+G+R']['step']; nodes = G['nodes']
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'
bo = lambda h: re.match('(' + HB + ')', h).group(1)
txt = {h: ' '.join(x[2] for v in it['fields'].values() for x in v) for h, it in P['items'].items()}
key = lambda h: (step[bo(h)], nodes.index(bo(h)), h)
a = ['| test file a gate names (U3 §6.1) | named by (batch) | v12 items naming it | reading |', '|---|---|---|---|']
NOTE = {'test_fa01_head_seats.py': 'not written: B21 `UNDECIDED` u-6 (part 14) records W3-3\'s replacement by the two files that read head seats',
        'test_obligees.py': 'not written: dropped at `FORK:217340fc` (ED-IN-0314), B10 second half (part 13_cont) rewrites the rows that cited it',
        'test_scene_access_occupancy.py': 'renamed `test_scene_access_engagement.py` by 28A (B28 batch gate, part 35)',
        'test_referent_class_stamps.py': '**unmatched**: B36\'s `16_PESSIMIST_WR_D` item names `test_in12_step9.py`\'s tests as its control and writes no file of this name (C-17)'}
for o in T['u61']:
    its = sorted(o['items'], key=key)
    a.append(f"| `{o['file']}` | {o['by']} | {', '.join(its[:4]) + (' …' if o['n'] > 4 else '') if its else '—'} | {NOTE.get(o['file'], 'named by an item' if its else '**unmatched**')} |")
probes_none = sorted({o['probe'] for o in T['u62'] if not o['items_naming_probe']})
b = ['| test file created (NEW in a WHERE line) | created by | step |', '|---|---|---|']
for f, hs in sorted(T['newtests'].items(), key=lambda x: key(sorted(x[1], key=key)[0])):
    hs = sorted(hs, key=key)
    b.append(f"| `{f.replace('engine/season/tests/', 'S/tests/')}` | {', '.join(hs)}{' **(two creators: C-03)**' if len(hs) > 1 else ''} | S{step[bo(hs[0])]} |")
c = ['| path created | item | caller the item names (searched in the item\'s own text) |', '|---|---|---|']
for f, hs in sorted(T['created'].items(), key=lambda x: key(sorted(x[1], key=key)[0])):
    if not re.match(r'(tools/|engine/engine_params/|engine/season/harness/|modules/|engine/season/boot/|engine/substrate/|engine/dice_engine/)', f): continue
    h = sorted(hs, key=key)[0]; t = txt[h]; base = f.rstrip('/').split('/')[-1]
    callers = []
    if 'ci_checks_registry' in t: callers.append('a `ci_checks_registry.yaml` row')
    if 'valoria-ci.yml' in t or 'workflow' in t: callers.append('the CI workflow (named)')
    if 'valoria_local' in t or '.githooks' in t: callers.append('the local tier')
    if 'composition' in t and f.startswith('modules/'): callers.append('a composition row')
    if re.search(r'python -m engine\.season\.harness\.' + re.escape(base.replace('.py', '')), t) or re.search(re.escape(base) + r'.{0,40}--check', t): callers.append('a gate command')
    if f.startswith('engine/engine_params/'): callers.append('its exporter\'s `--check` (named in the item)' if '--check' in t else 'none found')
    lib = re.match(r'(modules/|engine/dice_engine/|engine/season/boot/|engine/substrate/)', f)
    cell = '; '.join(dict.fromkeys(callers)) or ('code: imported by the items that consume it (a library file, no CI caller owed)' if lib else '**none found in the item text** (accretion pass)')
    c.append(f"| `{f}` | {', '.join(sorted(hs, key=key))} | {cell} |")
open('t6.md', 'w').write('\n'.join(a) + '\n\nPROBES\n\n' + '\n'.join(b) + '\n\nTOOLS\n\n' + '\n'.join(c) + '\n')
json.dump({'probes_none': probes_none, 'n62': len(T['u62']), 'n61': len(T['u61'])}, open('t6meta.json', 'w'))
print('6.1', len(a) - 2, '| probes named by no item', len(probes_none), '| new tests', len(b) - 2, '| created files', len(c) - 2,
      '| no caller', sum('none found' in x for x in c))
```

## `xref.py`

```python
"""Conflict checks: item handles cited that exist in no position table; `STOPS IF` lines and position-table
`gates on` cells naming a batch that closes at a later step (or the same step without a merge order)."""
import json, re
from collections import defaultdict
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
r = G['res']['S+G+R']; step = r['step']; nodes = G['nodes']
HB = r'B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)'; HI = HB + r'\.\d\d'
M = {tuple(k.split('>')) for k in G['M']}
known = set()
for b, bb in P['batches'].items():
    for p in bb['positions']: known.add(p['pos'])
bo = lambda h: re.match('(' + HB + ')', h).group(1)
missing = defaultdict(set)
for h, it in P['items'].items():
    for lab in ('DEPENDS ON', 'GATE', 'TESTS', 'STOPS IF', 'INSTRUCTION', 'SOURCE'):
        for fn, ln, t in it['fields'].get(lab, []):
            for c in re.findall(r'(?<![\w.])(' + HI + r')(?!\d)', t):
                if c not in known and bo(c) in step and not c.endswith('.99'): missing[c].add(f'{h} ({lab})')
for b, bb in P['batches'].items():
    for p in bb['positions']:
        for c in re.findall(r'(?<![\w.])(' + HI + r')(?!\d)', ' '.join(p['cells'][5:])):
            if c not in known and bo(c) in step: missing[c].add(f"{p['pos']} (gates on)")
print('cited handles in no position table:', len(missing))
for c in sorted(missing, key=lambda c: (nodes.index(bo(c)), c)): print('  ', c, '<-', sorted(missing[c])[:4])
later = []
for h, it in P['items'].items():
    b = bo(h)
    if b not in step: continue
    for fn, ln, t in it['fields'].get('STOPS IF', []):
        for a in set(re.findall(r'Batch (' + HB + r')', t) + re.findall(r'(' + HB + r')\.\d\d', t)):
            if a in step and a != b and (step[a] > step[b] or (step[a] == step[b] and (a, b) not in M)):
                later.append((h, a, step[b], step[a], fn, ln))
print('STOPS IF naming a batch that closes later or in the same step without a merge order:', len(later))
for x in later: print('  ', x)
cells = []
for b, bb in P['batches'].items():
    if b not in step: continue
    for p in bb['positions']:
        g = ' '.join(p['cells'][5:])
        for a in set(re.findall(r'Batch (' + HB + r')', g)):
            if a in step and a != b and (step[a] > step[b]) : cells.append((p['pos'], a, step[b], step[a]))
print('gates-on cells naming a later batch:', cells)
json.dump({'missing': {k: sorted(v) for k, v in missing.items()}, 'stops_later': later, 'cells_later': cells}, open('xref.json', 'w'))
# every `STOPS IF` sentence anywhere in an item (not only the `- STOPS IF:` field): a batch it names that closes later
n, out = 0, []
for h, it in P['items'].items():
    b = bo(h)
    if b not in step: continue
    t = ' '.join(x[2] for v in it['fields'].values() for x in v) + ' ' + it['heads'][0][2]
    for m in re.finditer(r'STOPS IF[^.;]*(?:[.;]|$)', t):
        n += 1; s = m.group(0)
        for a in set(re.findall(r'(?<![\w.])(' + HB + r')(?![\w])', s)):
            if a in step and a != b and (step[a] > step[b] or (step[a] == step[b] and (a, b) not in M)):
                out.append((h, a, f'S{step[b]}', f'S{step[a]}', s[:170]))
print('STOPS IF sentences:', n, '| naming a later or same-step batch:', len(out))
for x in out: print('  ', x)
```

## `ids.py`

```python
"""Table 9: id and row blocks. Reproduces workplan_v12.md §12's table from its own declared counts and readings
(control), then re-derives it with IN next_free = 363 (ED-IN-0362 is the adoption's) and the parts' final IDS counts."""
import json, re
G = json.load(open('graph.json')); nodes = G['nodes']; lane = G['lane']; name = G['name']
D = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
# H1's table, parsed
h1 = {}
for l in open(f'{D}/workplan_v12.md', encoding='utf-8'):
    m = re.match(r'^\| (B\S+) \| ([A-Z+]+) \| (.*?) \| H-(\d+)\.\.H-(\d+) \((\d+)\+5\) \|$', l)
    if m:
        b = re.match(r'(BA1|B\d\d(?:[a-z]|F\d|L|M)?)', m.group(1)).group(1)
        eds = re.findall(r'ED-([A-Z]+)-(\d+)\.\.(\d+) \((\d+)\+2\)', m.group(3))
        h1[b] = {'ed': [(x[0], int(x[1]), int(x[2]), int(x[3])) for x in eds], 'h': (int(m.group(4)), int(m.group(5)), int(m.group(6)))}
def alloc(nf, hstart, edc, hc):
    nf = dict(nf); hn = hstart; out = {}
    for b in nodes:
        lanes_ed = edc.get(b, {}); own = 'SE' if lane[b] == 'SE+WR' else lane[b]
        lanes_ed = dict(lanes_ed); lanes_ed.setdefault(own, 0)
        blocks = []
        for L in [own] + sorted(k for k in lanes_ed if k != own):
            n = lanes_ed[L] + 2; blocks.append((L, nf[L], nf[L] + n - 1, lanes_ed[L])); nf[L] += n
        hk = hc.get(b, 0) + 5; out[b] = {'ed': blocks, 'h': (hn, hn + hk - 1, hc.get(b, 0))}; hn += hk
    return out, nf, hn
edc0 = {b: {L: c for (L, s, e, c) in v['ed']} for b, v in h1.items()}
hc0 = {b: v['h'][2] for b, v in h1.items()}
nf0 = {'MB': 82, 'PC': 60, 'FI': 10, 'SC': 41, 'FA': 40, 'WR': 13, 'IN': 362, 'GO': 3, 'SE': 57}
ctrl, nfc, hc_ = alloc(nf0, 363, edc0, hc0)
diff = [b for b in h1 if (ctrl[b]['ed'], ctrl[b]['h']) != ([tuple(x) for x in h1[b]['ed']], h1[b]['h'])]
print('control: H1 table rows', len(h1), '| rows the method reproduces differently:', diff)
# final counts: H1's, with the parts' corrections
edc = json.loads(json.dumps(edc0)); hc = dict(hc0)
hc['B12c'] = 12            # part 28 B12c IDS: H 12 (B12c.32's `larder_stock_read`, A-116), H1 took 11
nf1 = dict(nf0); nf1['IN'] = 363
fin, nff, hnext = alloc(nf1, 363, edc, hc)
over = []
seen = {}
for b, v in fin.items():
    for (L, s, e, c) in v['ed']:
        for i in range(s, e + 1):
            k = f'ED-{L}-{i:04d}'
            if k in seen: over.append((k, seen[k], b))
            seen[k] = b
    for i in range(v['h'][0], v['h'][1] + 1):
        k = f'H-{i}'
        if k in seen: over.append((k, seen[k], b))
        seen[k] = b
print('overlaps', over, '| next_free after:', nff, '| next H', hnext)
moved = [b for b in fin if (fin[b]['ed'], fin[b]['h']) != (ctrl[b]['ed'], ctrl[b]['h'])]
print('rows that change against H1:', len(moved))
rows = ['| batch | lane | ED block (declared + spare) | H block (declared + spare) | against H1 §12 |', '|---|---|---|---|---|']
for b in nodes:
    v = fin[b]; eds = '; '.join(f'ED-{L}-{s:04d}..{e:04d} ({c}+2)' for (L, s, e, c) in v['ed'])
    ch = []
    if v['ed'] != ctrl[b]['ed']: ch.append('ED shifted')
    if v['h'] != ctrl[b]['h']: ch.append('H shifted' if v['h'][2] == ctrl[b]['h'][2] else 'H count 11 → 12')
    rows.append(f"| {name[b]} | {lane[b]} | {eds} | H-{v['h'][0]}..H-{v['h'][1]} ({v['h'][2]}+5) | {', '.join(ch) or 'same'} |")
open('t9.md', 'w').write('\n'.join(rows) + '\n')
json.dump({'nf_after': nff, 'h_next': hnext}, open('ids.json', 'w'))
```

## `req.py`

```python
"""Table 10: the requirement map (which batch's close reads which R-row) and the milestones on the recomputed schedule."""
import json, re
from collections import defaultdict
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
r = G['res']['S+G+R']; nodes = G['nodes']; step = r['step']
reads = defaultdict(list)
for b in nodes:
    if b not in P['batches']: continue
    t = ' '.join(x[2].replace('\n', ' ') for x in P['batches'][b]['fields'].get('REQUIREMENT', []))
    head = t.split('→')[0] if '→' in t else t[:200]
    if re.match(r'REQUIREMENT:\s*none', t) and not re.search(r'R-0\d', head): continue
    for R in sorted(set(re.findall(r'R-0(\d)', t))):
        reads['R-0' + R].append(b)
MS = [('M0 · ground', 'B04', ['B00', 'B01', 'B02', 'B03', 'B03g', 'B03c', 'B16L', 'B03a', 'B13', 'B16M', 'B04']),
      ('M1 · every outcome is drawn', 'B08', ['B05', 'B06', 'B07', 'B08']),
      ('M2 · persons', 'BA1', ['B09', 'B10', 'BA1']),
      ('M3 · every verb', 'B35', ['B11', 'B12a', 'B12b', 'B12c', 'B14', 'B15', 'B21', 'B21b', 'B21c', 'B22', 'B23', 'B24a', 'B25', 'B26', 'B27', 'B28', 'B29', 'B32', 'B35']),
      ('M4 · every scale', 'B36', ['B16', 'B17', 'B19a', 'B19', 'B20', 'B24', 'B30', 'B34', 'B36']),
      ('M5 · the rulings beyond the nine, and the carried positions', 'B40', ['B18', 'B31', 'B33', 'B37', 'B38', 'B39', 'B40', 'B41', 'B11F1', 'B11F2', 'B21d', 'B21s', 'B37p']),
      ('the settings, then the re-take', 'B99', ['B98', 'B99'])]
rows = ['| milestone | closes at (step now) | its batches, with their step now | a batch of it closing after the close? | rows the closing batch reads |', '|---|---|---|---|---|']
for nm, close, bs in MS:
    late = [b for b in bs if step[b] > step[close]]
    rows.append(f"| {nm} | {close} (S{step[close]}; §2.3 S{G['s_step'][close]}) | {', '.join(f'{b} S{step[b]}' for b in bs)} | {', '.join(late) or 'none'} | {', '.join(R for R in sorted(reads) if close in reads[R]) or '—'} |")
rows2 = ['| row | batches whose `REQUIREMENT:` line reads a conjunct of it, in step order | last of them (step) | the milestone that reads it whole (§3 of the structure) |', '|---|---|---|---|']
whole = {'R-01': 'M0 (B04)', 'R-02': 'M0 (B04)', 'R-03': 'M1 (B08)', 'R-04': 'M4 (B36)', 'R-05': 'M3 (B35)', 'R-06': 'M2 (BA1)', 'R-07': 'M2 or M3', 'R-08': 'M2 (BA1)', 'R-09': 'M2 (BA1)'}
for R in sorted(reads):
    bs = sorted(set(reads[R]), key=lambda b: (step[b], nodes.index(b)))
    last = bs[-1]
    rows2.append(f"| {R} | {', '.join(bs)} | {last} (S{step[last]}) | {whole[R]}; `status:` moves only at B99 (A-114) |")
open('t10.md', 'w').write('\n'.join(rows) + '\n\n' + '\n'.join(rows2) + '\n')
print('\n'.join(rows)); print('\n'.join(rows2))
```

## `held_extract.py`

```python
import re,sys
E='/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/eval/'
intake=open(E+'V12_INTAKE.md').read().split('\n')
cov=open('/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/COVERAGE.md').read().split('\n')
held=[]
for l in cov:
    m=re.match(r'^\| `:(\d+)` \| (\w+) \| (.*?) \| HELD-TABLE',l)
    if m: held.append((int(m.group(1)),m.group(2),m.group(3)))
print(len(held))
files={}
def getf(n):
    if n not in files: files[n]=open(E+n+'.md').read().split('\n')
    return files[n]
for ln,lane,iid in held:
    entry=intake[ln-1]
    print('=====',ln,lane,iid)
    print('INTAKE:',entry[:1500])
    for m in re.finditer(r'(E\d) §Carry-forward, line (\d+)',entry):
        f=getf(m.group(1)); k=int(m.group(2))
        blk='\n'.join(f[k-1:k+14])
        trig=[x for x in re.split(r'(?<=[.;|])\s',blk) if re.search(r'[Tt]rigger',x)]
        print(f'  [{m.group(1)}:{k}] TRIG:', ' || '.join(t[:500] for t in trig[:4]))
    for m in re.finditer(r'(E\d) Block (\w+)',entry):
        f=getf(m.group(1))
        for i,x in enumerate(f):
            if re.search(r'Block '+m.group(2)+r'\b',x) and (x.startswith('#') or x.startswith('**')):
                blk='\n'.join(f[i:i+20]); trig=[y for y in re.split(r'(?<=[.;|])\s',blk) if re.search(r'[Tt]rigger|HELD|held',y)]
                print(f'  [{m.group(1)} Block {m.group(2)} @{i+1}] TRIG:',' || '.join(t[:500] for t in trig[:4])); break
```

## `dials.py`

```python
"""Dump every DIALS AT CONTROL line of the parts (block-level, from parts.json) with its part and line, for the
hand-made settings table of part 2 §4. Lines written as `- **DIALS AT CONTROL**`, `**DIALS AT CONTROL (this half):**`
or as an item-level `- DIALS AT CONTROL:` are not block fields to parse_parts.py; they were found by
`grep -n 'DIALS AT CONTROL' workplan_v12_part*.md` and read by hand (parts 5, 8_cont, 13, 20, 27)."""
import json
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
out = []
for b in G['nodes']:
    if b not in P['batches']: continue
    for fn, ln, t in P['batches'][b]['fields'].get('DIALS AT CONTROL', []):
        out.append(f'##### {b} {fn}:{ln}\n{t}\n')
open('dials_raw.txt', 'w').write('\n'.join(out)); print(sum(len(x) for x in out), 'bytes')
```

## `totals.py`

```python
"""H3: plan-wide totals from parts.json, graph.json, hashinfo.json (part 2 §1.2, §1.3 totals, §3). Read-only."""
import json, re
from collections import Counter
P = json.load(open('parts.json')); G = json.load(open('graph.json')); H = json.load(open('hashinfo.json'))
KS = ['DESIGN-FIRST', 'POINTER', 'READING', 'HELD', 'BLOCKED', 'CONTENT', 'BUILD', 'GIT']
def anyword(s):                       # graph.py's / summ.py's normaliser: the first listed word found anywhere in the cell
    u = s.upper()
    for k in KS:
        if k in u: return k
    return 'OTHER'
def leading(s):                       # the state cell's leading word (R1: "BUILD (HELD if …)" is BUILD)
    u = s.upper().lstrip('*` ')
    for k in KS:
        if u.startswith(k): return k
    return anyword(s)
tot_a, tot_l, per = Counter(), Counter(), {}
for b in G['nodes']:
    seen = {}
    for p in P['batches'][b]['positions']: seen.setdefault(p['pos'], p)
    a = Counter(anyword(p['cells'][3]) for p in seen.values()); l = Counter(leading(p['cells'][3]) for p in seen.values())
    tot_a += a; tot_l += l
    if a != l: per[b] = (dict(a), dict(l))
print('positions', sum(tot_a.values()), '| by any word', dict(tot_a), '| by leading word', dict(tot_l))
print('batches where the two normalisers differ:', per)
nb = sum(len(H[b]['mv']['B']) for b in H); ne = sum(len(H[b]['mv']['E']) for b in H); nq = sum(len(H[b]['mv']['?']) for b in H)
mb = [b for b in H if any(H[b]['mv'].values())]
print('movers behaviour', nb, 'encoding', ne, 'conditional', nq, '| mover batches', len(mb), 'EQUAL', len(H) - len(mb), sorted(set(H) - set(mb), key=G['nodes'].index))
print('conditional handles', [h for b in H for h in H[b]['mv']['?']])
print('encoding handles', [h for b in H for h in H[b]['mv']['E']])
print('without B98/B99: behaviour', nb - len(H['B98']['mv']['B']), 'positions', sum(G['pos'][b] for b in G['pos'] if b not in ('B98','B99')))
r = G['res']['S+G+R']
print('est B98', G['est']['B98'], 'B99', G['est']['B99'], 'serial', round(sum(G['est'].values()), 1), 'makespan', round(sum(max(G['est'][h] for h in s) for s in r['sched']), 1))
for k in ('S', 'S+G', 'S+G+R', 'S+G+R+M'):
    x = G['res'][k]; print(k, 'W', x['W'] + 1, 'steps', len(x['sched']), 'chains', len(x['chains']), 'hours', x['hours'][0])
print('slack B17', r['slack']['B17'], 'B03g', r['slack']['B03g'], 'B34', r['slack']['B34'], 'B26', r['slack']['B26'])
```

## `names.py`

```python
"""H3: the names table (part 2 §12). Every rename an item's NAMES line states (old → new) and every new name a NEW
mark introduces (a file, tool, test file, harness module, key), in landing order; flags a name two items introduce
and two spellings of one name. Reads parts.json and graph.json; writes names.json; read-only over the parts."""
import json, re, os
from collections import defaultdict
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
r = G['res']['S+G+R']; step = r['step']; nodes = G['nodes']
order = []                                            # landing order: step, then the structure's row order, then the position table
for b in sorted(nodes, key=lambda b: (step[b], nodes.index(b))):
    seen = []
    for p in P['batches'][b]['positions']:
        if p['pos'] not in seen: seen.append(p['pos'])
    order += seen
rank = {h: i for i, h in enumerate(order)}
TOK = r'`([^`\n]{2,120})`'
def kind(t):
    base = os.path.basename(t.split('::')[0])
    if re.match(r'test_\w+\.py$', base): return 'test file'
    if t.startswith('tools/') or '/tools/' in t: return 'tool'
    if 'harness/' in t: return 'harness module'
    if base.endswith('.py'): return 'module'
    if re.search(r'\.(ya?ml|json)$', base): return 'data file'
    if base.endswith('.md'): return 'design file'
    if '::' in t or re.match(r'^[A-Za-z_][\w.]*$', t): return 'key or symbol'
    return 'other'
def clean(t):
    t = t.strip().rstrip('.,;:')
    t = re.sub(r'^S/', 'engine/season/', t)          # the parts' S/ shorthand
    return t
renames, news = [], defaultdict(list)
for h in order:
    it = P['items'].get(h)
    if not it: continue
    for fn, ln, t in it['fields'].get('NAMES', []):
        body = t.split(':', 1)[1]
        for m in re.finditer(TOK + r'\s*(?:\([^)]*\)\s*)?→\s*' + TOK, body):
            renames.append({'item': h, 'old': clean(m.group(1)), 'new': clean(m.group(2)), 'at': f'{fn}:{ln}'})
    for f, v in it['fields'].items():
        if f in ('DEPENDS ON', 'SOURCE', 'GLOSSARY'): continue      # a NEW there cites another item's creation, or a glossary row
        for fn, ln, t in v:
            for m in re.finditer(r'\bNEW\s*' + TOK, t):   # NEW marks the one name after it ("NEW `a`, `b`": `b` is an existing name the item edits)
                for x in [m.group(1)]:
                    x = clean(x)
                    if ' ' in x or len(x) < 3: continue
                    if not any(e['item'] == h for e in news[x]): news[x].append({'item': h, 'field': f, 'at': f'{fn}:{ln}'})
def norm(x):                                          # one spelling key: base name lower case, separators and a plural s dropped; file names keep their extension class
    b = os.path.basename(x.split('::')[-1]); ext = re.search(r'\.(py|ya?ml|json|md)$', b.lower())
    b = re.sub(r'\.(py|ya?ml|json|md)$', '', b.lower())
    return re.sub(r'[^a-z0-9]', '', b).rstrip('s') + ('.' + ext.group(1)[:2] if ext else '')
def same(a, b):                                       # a relative and a full spelling of one path, or a module and a symbol in it
    a0, b0 = a.split('::')[0], b.split('::')[0]
    if '/' not in a or '/' not in b: a0, b0 = a.split('::')[-1], b.split('::')[-1]       # a bare symbol and its qualified spelling
    return a0 == b0 or a0.endswith('/' + b0) or b0.endswith('/' + a0)
twice = {x: v for x, v in news.items() if len({e['item'] for e in v}) > 1}
byn = defaultdict(set)
for x in news:
    if not x.startswith(('-', '__', '[')) and not x.endswith(('*', '=')) and '__init__' not in x and not x.isupper(): byn[norm(x)].add(x)
ok = lambda x: not x.startswith(('-', '__', '[')) and not x.endswith(('*', '=')) and '__init__' not in x and not x.isupper()
for rn in renames:
    if ok(rn['new']): byn[norm(rn['new'])].add(rn['new'])
rtwice = defaultdict(list)                            # one rename stated by two items
for rn in renames: rtwice[(rn['old'], rn['new'])].append(rn['item'])
rtwice = {f'{a} → {b}': sorted(set(v), key=lambda h: rank.get(h, 0)) for (a, b), v in rtwice.items() if len(set(v)) > 1}
spell = {}
for k, v in byn.items():
    v = sorted(v)
    if len(v) < 2 or len(k) <= 3: continue
    if all(same(a, b) for a in v for b in v): continue
    if all(a.lower() == b.lower() or a.lower().rstrip('s') == b.lower().rstrip('s') for a in v for b in v) and not any('/' in a for a in v): continue   # a class and its constant, or a plural: one word
    spell[k] = v
json.dump({'rtwice': rtwice, 'renames': renames, 'news': news, 'twice': twice, 'spell': spell, 'rank': rank}, open('names.json', 'w'), indent=0)
kinds = defaultdict(int)
for x in news: kinds[kind(x)] += 1
print('renames', len(renames), 'from', len({r_['item'] for r_ in renames}), 'items; NAMES lines', sum(len(P['items'][h]['fields'].get('NAMES', [])) for h in P['items']))
print('new names', len(news), dict(kinds))
print('introduced NEW by two or more items', len(twice))
for x, v in sorted(twice.items(), key=lambda kv: rank.get(kv[1][0]['item'], 0)): print('  TWICE', x, [e['item'] for e in v])
print('renames stated by two or more items', len(rtwice)); [print('  RTWICE', k, v) for k, v in rtwice.items()]
print('spelling groups', len(spell))
for k, v in spell.items(): print('  SPELL', v)
# --- the markdown tables (part 2 §12)
tail = lambda x: x.split('::')[-1].split('/')[-1]
first = lambda hs: sorted(set(hs), key=lambda h: rank.get(h, 0))
pairs = defaultdict(list)
for rn in renames: pairs[(rn['old'], rn['new'])].append(rn['item'])
L = ['| old → new | first stated by | also applied by (items) |', '|---|---|---|']
for (o, n), hs in sorted(pairs.items(), key=lambda kv: rank.get(first(kv[1])[0], 0)):
    hs = first(hs); more = hs[1:]
    L.append(f"| `{o}` → `{n}` | {hs[0]} | {', '.join(more[:8]) + (f' … ({len(more)})' if len(more) > 8 else '') if more else '—'} |")
open('names_renames.md', 'w').write('\n'.join(L) + '\n')
L = ['| new name | kind | introduced (NEW) by | also marked NEW by |', '|---|---|---|---|']
for x, v in sorted(news.items(), key=lambda kv: (rank.get(kv[1][0]['item'], 0), kv[0])):
    hs = first([e['item'] for e in v])
    L.append(f"| `{x}` | {kind(x)} | {hs[0]} | {', '.join(hs[1:]) or '—'} |")
open('names_new.md', 'w').write('\n'.join(L) + '\n')
odd = defaultdict(lambda: defaultdict(list))
for rn in renames: odd[tail(rn['old'])][tail(rn['new'])].append(rn['item'])
odd = {o: {n: first(h) for n, h in d.items()} for o, d in odd.items() if len(d) > 1}
json.dump({'pairs': len(pairs), 'odd': odd}, open('names_flags.json', 'w'), indent=0)
print('rename pairs', len(pairs), '| one old name, two new spellings', len(odd))
```

## `carriers.py`

```python
"""H3: the symbols with no carrier (part 2 §13). From each item's DEPENDS ON marks: every MISSING entry with its owner;
every EXISTS-IN-TREE token not found in the tree, classed by whether an earlier item creates it (a mismark), only a
later one does, or none does (no carrier); every V12 handle that lands after the item citing it; and U3 §6.3's 30 rows
matched to the item that now carries each. Reads parts.json, graph.json, names.json and the working tree; read-only."""
import json, re, os, subprocess
from collections import defaultdict
P = json.load(open('parts.json')); N = json.load(open('names.json')); rank = N['rank']
ROOT = '/home/user/ttrpg'
files = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
fset = set(files); bases = defaultdict(list)
for f in files: bases[os.path.basename(f)].append(f)
CODE = [f for f in files if f.startswith(('engine/', 'modules/', 'tools/', 'references/', 'systems/', 'tests/', 'godot/'))
        and re.search(r'\.(py|ya?ml|json|gd|ini|toml|cfg)$', f)]
ident = set(); text = {}
for f in CODE:
    try: t = open(f'{ROOT}/{f}', encoding='utf-8', errors='ignore').read()
    except OSError: continue
    text[f] = t; ident.update(re.findall(r'[A-Za-z_][A-Za-z0-9_]*', t))
PRE = ['', 'engine/season/', 'engine/', 'modules/', 'tools/', 'engine/season/tests/', 'tests/valoria/', 'references/']
def findfile(p):
    p = re.sub(r'^S/', 'engine/season/', p.strip('/'))
    for pre in PRE:
        if pre + p in fset: return pre + p
        if any(f.startswith(pre + p + '/') for f in files[:0]) or os.path.isdir(f'{ROOT}/{pre}{p}'): return pre + p
    c = [f for f in bases.get(os.path.basename(p), []) if f.endswith(p)]
    return c or None
def found(tok):
    """True / False / None (not a checkable name)."""
    t = tok.strip().rstrip('.,;:')
    if re.search(r'[\s(){}<>=,"\'|*…]', t) or t.startswith('-') or len(t) < 3: return None
    if re.fullmatch(r'[0-9a-f]{7,40}', t) or re.match(r'^(\d\d_|U\d|[A-Z][A-Z0-9]*_[A-Z])', t) or re.search(r'\.md\b|^res://|^B(?:A1|\d\d)\w*\.\d\d$', t): return None   # a commit, a design document or an item: not a symbol
    path, sym = (t.split('::', 1) + [''])[:2] if '::' in t else (t, '')
    m = re.match(r'^([\w./-]+\.(?:ya?ml|json|py)):\s*(\S+)$', t)
    if m: path, sym = m.group(1), m.group(2)
    if '/' in path or re.search(r'\.(py|ya?ml|json|md|gd)$', path):
        fs = findfile(path)
        if not fs: return False
        if isinstance(fs, str): fs = [fs]
        if not sym: return True
        last = re.findall(r'[A-Za-z_]\w*', sym)
        if not last: return True
        for f in fs:
            body = text.get(f) or (open(f'{ROOT}/{f}', encoding='utf-8', errors='ignore').read() if os.path.isfile(f'{ROOT}/{f}') else '')
            if re.search(r'\b' + re.escape(last[-1]) + r'\b', body): return True
        return False
    parts = re.findall(r'[A-Za-z_]\w*', t)
    if not parts: return None
    return parts[-1] in ident
creators = defaultdict(list)                           # token tail → items that create it (a NEW mark) or name it in WHERE
def tl(x):                                            # the token's own name: a path's base name, a symbol's last identifier
    x = re.sub(r'^S/', 'engine/season/', x)
    if '::' not in x and ('/' in x or re.search(r'\.(py|ya?ml|json|md)$', x)): return [os.path.basename(x)]
    return re.findall(r'[A-Za-z_]\w*', x.split('::')[-1])[-1:] or [x]
for x, v in N['news'].items():
    for e in v: creators[tl(x)[0]].append(e['item']); creators[x].append(e['item'])
for rn in N['renames']: creators[tl(rn['new'])[0]].append(rn['item']); creators[rn['new']].append(rn['item'])   # a rename creates its new name
for h, it in P['items'].items():
    for fn, ln, t in it['fields'].get('WHERE', []) + it['fields'].get('INSTRUCTION', []):
        for m in re.finditer(r'\b(?:NEW|new|adds?|creates?|writes?)\b[^.;]{0,60}?`([^`]+)`', t):
            creators[tl(m.group(1))[0]].append(h)
MARK = r'(EXISTS-IN-TREE|V12|PROPOSED|MISSING(?:-BY-ORDER|-DEP)?)'
missing, absent, later_v12, checked = [], [], [], 0
for h, it in P['items'].items():
    for fn, ln, t in it['fields'].get('DEPENDS ON', []):
        segs = re.split(MARK, t)
        for i in range(1, len(segs) - 1, 2):
            mk, body = segs[i], segs[i + 1]
            if mk.startswith('MISSING'):
                missing.append({'item': h, 'mark': mk, 'text': re.sub(r'\s+', ' ', body.strip(' :;,'))[:260], 'at': f'{fn}:{ln}'})
            elif mk == 'EXISTS-IN-TREE':
                for tok in re.findall(r'`([^`\n]+)`', body):
                    r_ = found(tok)
                    if r_ is None: continue
                    checked += 1
                    if r_: continue
                    key = tl(tok)[0]; cs = [c for c in creators.get(tok, []) + creators.get(key, []) if c != h]
                    early = sorted({c for c in cs if rank.get(c, 1e9) < rank.get(h, 0)}, key=lambda c: rank[c])
                    late = sorted({c for c in cs if rank.get(c, -1) > rank.get(h, 0)}, key=lambda c: rank[c])
                    cls = 'created by an earlier item (mark it V12)' if early else ('created only by a later item' if late else 'no carrier found')
                    absent.append({'item': h, 'token': tok, 'class': cls, 'early': early[:3], 'late': late[:3], 'at': f'{fn}:{ln}'})
            elif mk == 'V12':
                for hh in re.findall(r'\b(B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)\.\d\d)\b', body.split(';')[0]):
                    if hh in rank and rank[hh] > rank.get(h, 0) and not re.search(r'not a depend|note|forward|STOPS IF', body.split(';')[0], re.I):
                        later_v12.append({'item': h, 'cites': hh, 'at': f'{fn}:{ln}', 'text': re.sub(r'\s+', ' ', body.split(';')[0])[:160]})
# U3 §6.3
u3 = []
for l in open(f'{ROOT}/proposals/2026-11-12-subsystem-audit-suite/unified/U3_DEPENDENCY_ORDER.md', encoding='utf-8').read().split('### 6.3', 1)[1].split('\n## ', 1)[0].split('\n'):
    if not l.startswith('| ') or l.startswith('| missing') or l.startswith('|---'): continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    toks = re.findall(r'`([^`]+)`', c[0]) or [c[0]]
    st = []
    for tok in toks:
        key = tl(tok)[0]; cs = sorted(set(creators.get(tok, []) + creators.get(key, [])), key=lambda x: rank.get(x, 1e9))
        st.append((tok, found(tok), cs[:2]))
    u3.append({'row': c[0][:90], 'u3': c[2][:90], 'tokens': st})
json.dump({'missing': missing, 'absent': absent, 'later_v12': later_v12, 'u3': u3, 'checked': checked}, open('carriers.json', 'w'), indent=0)
from collections import Counter
print('MISSING entries', len(missing), '| EXISTS-IN-TREE tokens checked', checked, '| not found', len(absent), Counter(a['class'] for a in absent))
print('V12 handles landing after the citing item (not marked a note)', len(later_v12))
print('U3 §6.3 rows', len(u3))
# --- U3 §6.3: the first item (landing order) whose WHERE or INSTRUCTION names each token, beside the creator match
def naming(tok):
    key = tl(tok)[0]; hs = []
    for h, it in P['items'].items():
        for f in ('WHERE', 'INSTRUCTION'):
            if any(re.search(r'`[^`]*\b' + re.escape(key) + r'\b[^`]*`', t) for _, _, t in it['fields'].get(f, [])): hs.append(h); break
    return sorted(hs, key=lambda x: rank.get(x, 1e9))[:3]
for u in u3: u['named'] = [(t[0], naming(t[0]) if t[1] is not None else []) for t in u['tokens']]
json.dump({'missing': missing, 'absent': absent, 'later_v12': later_v12, 'u3': u3, 'checked': checked}, open('carriers.json', 'w'), indent=0)
```

## `t13.py`

```python
"""H3: the tables of part 2 §12 (names) and §13 (symbols with no carrier) as markdown, from names.json and carriers.json;
writes t12_renames.md, t12_new.md, t13_missing.md, t13_absent.md, t13_later.md, t13_u3.md. Read-only over the parts."""
import json, re
N = json.load(open('names.json')); C = json.load(open('carriers.json')); rank = N['rank']
first = lambda hs: sorted(set(hs), key=lambda h: rank.get(h, 0))
esc = lambda s: s.replace('|', '\\|')
from collections import defaultdict
pairs = defaultdict(list)
for r in N['renames']: pairs[(r['old'], r['new'])].append(r['item'])
L = ['| # | old → new | first stated by | applied again by |', '|---|---|---|---|']
for i, ((o, n), hs) in enumerate(sorted(pairs.items(), key=lambda kv: rank.get(first(kv[1])[0], 0)), 1):
    hs = first(hs); m = hs[1:]
    L.append(f"| {i} | `{esc(o)}` → `{esc(n)}` | {hs[0]} | {', '.join(m[:6]) + (f' and {len(m) - 6} more' if len(m) > 6 else '') if m else '—'} |")
open('t12_renames.md', 'w').write('\n'.join(L) + '\n')
def kind(t):
    import os
    base = os.path.basename(t.split('::')[0])
    if re.match(r'test_\w+\.py$', base): return 'test file'
    if t.startswith('tools/') or '/tools/' in t: return 'tool'
    if 'harness/' in t: return 'harness module'
    if base.endswith('.py'): return 'module'
    if re.search(r'\.(ya?ml|json)$', base): return 'data file'
    if base.endswith('.md'): return 'design file'
    if '::' in t or re.match(r'^[A-Za-z_][\w.]*$', t): return 'key or symbol'
    return 'other'
L = ['| # | new name | kind | introduced (NEW) by | also marked NEW by |', '|---|---|---|---|---|']
for i, (x, v) in enumerate(sorted(N['news'].items(), key=lambda kv: (rank.get(kv[1][0]['item'], 0), kv[0])), 1):
    hs = first([e['item'] for e in v])
    L.append(f"| {i} | `{esc(x)}` | {kind(x)} | {hs[0]} | {', '.join(hs[1:]) or '—'} |")
open('t12_new.md', 'w').write('\n'.join(L) + '\n')
L = ['| # | item | mark | what is missing, and its owner (the item\'s own words) | at |', '|---|---|---|---|---|']
for i, a in enumerate(sorted(C['missing'], key=lambda a: rank.get(a['item'], 0)), 1):
    L.append(f"| {i} | {a['item']} | {a['mark']} | {esc(a['text'])} | {a['at'].replace('workplan_v12_', '')} |")
open('t13_missing.md', 'w').write('\n'.join(L) + '\n')
L = ['| # | item | token marked EXISTS-IN-TREE | not in the tree; class | earliest items naming it as created | at |', '|---|---|---|---|---|---|']
for i, a in enumerate(sorted(C['absent'], key=lambda a: rank.get(a['item'], 0)), 1):
    L.append(f"| {i} | {a['item']} | `{esc(a['token'])}` | {a['class']} | {', '.join(a['early'] or a['late']) or '—'} | {a['at'].replace('workplan_v12_', '')} |")
open('t13_absent.md', 'w').write('\n'.join(L) + '\n')
L = ['| # | item | cites (V12) | landing | the citing clause | at |', '|---|---|---|---|---|---|']
for i, a in enumerate(C['later_v12'], 1):
    L.append(f"| {i} | {a['item']} | {a['cites']} | after the citer | {esc(a['text'].strip())} | {a['at'].replace('workplan_v12_', '')} |")
open('t13_later.md', 'w').write('\n'.join(L) + '\n')
print('renames', len(pairs), 'new', len(N['news']), 'missing', len(C['missing']), 'absent', len(C['absent']), 'later', len(C['later_v12']))
```

## `residue.py`

```python
"""H3: gate-quality residue (part 2 §11). Every item GATE line and every block BATCH GATE / GATE line that reads a
`## Status:` line or counts lines of a document (a `.md` file, or a `proposals/`, `.designs/`, `canon/` path) instead of
an execution artifact. Reads parts.json; read-only. Prints one row per hit with the arm's text."""
import json, re
P = json.load(open('parts.json')); G = json.load(open('graph.json'))
STATUS = re.compile(r"##\s*Status|Status:\s*(PROPOSED|RATIFIED|ACCEPTED)|status line", re.I)
DOCCOUNT = re.compile(r"(grep\s+-[a-zA-Z]*c[a-zA-Z]*|wc\s+-l|grep[^`|;]*\|\s*wc)[^`]*?(\.md\b|proposals/|\.designs/|canon/|CURRENT\.md|HANDOFF)", re.I)
STATES = re.compile(r"(file|design|document)[^.;]{0,40}\bstates\b[^.;]{0,30}\(1\)|exists and states", re.I)
RECORD = re.compile(r"record line|not a gate arm|critic's verdict|not a gate claim|not read as a gate|not readings|not a reading|arm is deleted|is not an execution artifact", re.I)
hits = []
def scan(where, handle, fn, ln, t):
    if RECORD.search(t) and not STATES.search(t): return                       # the line already relabels its document arm (R2a, R2b, R2c, R2d)
    for arm in re.split(r';\s+|\n', t):
        if (STATUS.search(arm) or DOCCOUNT.search(arm) or STATES.search(arm)) and not RECORD.search(arm):
            hits.append({'where': where, 'handle': handle, 'at': f'{fn}:{ln}', 'arm': re.sub(r'\s+', ' ', arm.strip())[:240]})
for h, it in P['items'].items():
    for fn, ln, t in it['fields'].get('GATE', []): scan('item GATE', h, fn, ln, t)
for b, bb in P['batches'].items():
    for fn, ln, t in bb['fields'].get('BATCH GATE', []): scan('BATCH GATE', b, fn, ln, t)
json.dump(hits, open('residue.json', 'w'), indent=0)
print('hits', len(hits), 'items/blocks', len({x['handle'] for x in hits}))
for x in hits: print(x['handle'], '|', x['where'], '|', x['at'], '|', x['arm'][:200])
```

## `sizes.py`

```python
"""H3: item sizes (E-12: about 4 KB, 6 KB hard). An item is its `### Bnn.mm` heading to the next heading; bytes UTF-8.
Prints the count over 6,144 bytes (6 KB) and over 6,000, by part range, and the list. Read-only."""
import re, glob, os, json
from collections import Counter
D = '/home/user/ttrpg/proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12'
P = json.load(open('parts.json'))
sz = {}
for fn in P['files']:
    cur = None; buf = []
    for l in open(f'{D}/{fn}', encoding='utf-8'):
        if l.startswith('## ') or l.startswith('### '):
            if cur: sz[cur] = sz.get(cur, 0) + len(''.join(buf).encode())
            m = re.match(r'^### (B(?:A1|\d\d(?:[a-z]|F\d|L|M)?)\.\d\d)\b', l); cur = m.group(1) if m else None; buf = [l] if cur else []
        elif cur: buf.append(l)
    if cur: sz[cur] = sz.get(cur, 0) + len(''.join(buf).encode())
over = sorted([(h, n) for h, n in sz.items() if n > 6144], key=lambda x: -x[1])
print('items', len(sz), '| over 6,144 bytes', len(over), '| over 6,000', sum(1 for n in sz.values() if n > 6000), '| over 8 KB', sum(1 for _, n in over if n > 8192), '| largest', over[:5])
def part(h):
    for fn in P['files']:
        pass
rng = Counter()
for h, n in over:
    f = P['items'][h]['files'][0]; k = int(re.search(r'part(\d+)', f).group(1))
    rng['3-11' if k <= 11 else '12-20' if k <= 20 else '21-28' if k <= 28 else '29-43' if k <= 43 else '44'] += 1
print(dict(rng)); print(' '.join(f'{h}:{n/1024:.1f}' for h, n in over))
json.dump({'over': over}, open('sizes.json', 'w'))
```
