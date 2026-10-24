"""One-off (not a guard) dependency check over -03's position tables (the 'needs' column): handles that need a handle in a later batch, and cycles.
usage: python graph_check.py PLAN_DIR"""
import sys, re, os, collections
D = sys.argv[1]
t = open(os.path.join(D, "2026-10-24-v10-03-batches.md")).read().split("\n")
HANDLE = re.compile(r"\b(REM-[0-9A-Z]{2}|CP-T\d\d-\d\d|CR-\d\d|NM-W\d|CL-[A-Z]+|DEF-\d+|(?:IN|SC|SE|MB|PC|FI|GO|FA|WR)-\d+[a-z]?)\b")
ALIAS = {"IN-09": "REM-2B", "IN-33": "REM-2B", "IN-46": "REM-31", "IN-47": "REM-30", "SE-05": "IN-30", "FA-02": "IN-30", "FI-05": "IN-32"}
batch = None; rows = {}; order = []
for l in t:
    m = re.match(r"^### (B10-[0-9Z]+)", l)
    if m: batch = m.group(1); order.append(batch) if batch not in order else None; continue
    if batch and l.startswith("| ") and not l.startswith("| handle") and not l.startswith("|---"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 5 and HANDLE.fullmatch(c[0]):
            rows[c[0]] = (batch, [ALIAS.get(h, h) for h in HANDLE.findall(c[4]) if ALIAS.get(h, h) != c[0]], l)
idx = {b: i for i, b in enumerate(order)}
print("positions in -03 tables:", len(rows), "batches:", len(order))
bad_order = []; graph = collections.defaultdict(set)
for h, (b, needs, _) in rows.items():
    for n in needs:
        if n in rows:
            graph[h].add(n)
            nb = rows[n][0]
            if idx[nb] > idx[b] and nb != "B10-Z": bad_order.append((h, b, "needs", n, nb))
            if nb == "B10-Z" and b != "B10-Z": bad_order.append((h, b, "needs HELD", n, nb))
# cycles (Tarjan-free DFS)
cyc = []; state = {}
def dfs(u, path):
    state[u] = 1
    for v in sorted(graph.get(u, ())):
        if state.get(v) == 1: cyc.append(path[path.index(v):] + [v] if v in path else [u, v])
        elif state.get(v) is None: dfs(v, path + [v])
    state[u] = 2
for h in sorted(rows):
    if state.get(h) is None: dfs(h, [h])
print("needs on a LATER batch or a HELD handle:", len(bad_order))
for x in bad_order: print("  ", x)
print("cycles:", len(cyc))
for c in cyc: print("  ", " -> ".join(c))
