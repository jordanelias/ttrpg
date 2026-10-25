"""Coverage check for the v10 plan directory (one-off; not a guard).

usage: python coverage_check.py SCRATCH PLAN_DIR
Checks: (1) EVERY hole-register row (read from the register, run from the repo root), and every in-scope hole id, ED id and v9 state-index handle is the first cell of a row in -06;
(2) every REM and CP handle is a row in -07; (3) every handle -06 names is a key the batch map knows;
(4) every id the queue (-05) cites as a v10 handle exists."""
import sys, os, re, json, glob
SC, PLAN = sys.argv[1:3]
sys.path.insert(0, os.path.join(SC, "ctl"))
import batch_map as B
inv = json.load(open(os.path.join(SC, "ctl", "static_inventory.json")))
def rd(n): return open(os.path.join(PLAN, n)).read()
led = rd("2026-10-24-v10-06-row-ledger.md"); xw = rd("2026-10-24-v10-07-crosswalk.md")
if os.path.exists(os.path.join(PLAN, "2026-10-24-v10-06-row-ledger_part2.md")): led += "\n" + rd("2026-10-24-v10-06-row-ledger_part2.md")
if os.path.exists(os.path.join(PLAN, "2026-10-24-v10-06-row-ledger_part3.md")): led += "\n" + rd("2026-10-24-v10-06-row-ledger_part3.md")
def first_cells(text): return {m.group(1) for m in re.finditer(r"(?m)^\| ([^| ]+) \|", text)}
fc = first_cells(led); fx = first_cells(xw)
holes = [h["id"] if isinstance(h, dict) else h for h in inv["hole_scope"]]
eds = [e["id"] if isinstance(e, dict) else e for e in inv["ed_open_since_v9"]]
sidx = [s["handle"] if isinstance(s, dict) and "handle" in s else (s.get("id") if isinstance(s, dict) else s) for s in inv["state_index"]]
bad = 0
def rep(name, missing, total):
    global bad
    print(f"{name}: {total - len(missing)}/{total}" + ("" if not missing else f"  MISSING {sorted(missing)}"))
    bad += bool(missing)
print("hole rows (first cell H-nnn) in -06:", len({c for c in fc if re.match(r'^H-\d+$', c)}))
rep("hole rows in -06", [h for h in holes if h not in fc], len(holes))
import yaml
reg_ids = [r["id"] for r in yaml.safe_load(open("engine/season/hole_register.yaml"))["rows"]]  # run from the repository root
rep("EVERY hole-register row in -06 or -06 part 2", [h for h in reg_ids if h not in fc], len(reg_ids))
rep("ED ids in -06", [e for e in eds if e not in fc], len(eds))
named = inv.get("ed_open_not_named", [])
rep("the other open editorial ids in -06 part 3", [e for e in named if e not in fc], len(named))
rep("state-index rows in -06", [s for s in sidx if s not in fc], len(sidx))
rep("REM in -07", [k for k in B.REM if k not in fx], len(B.REM))
rep("CP in -07", [k for k in B.CP if k not in fx], len(B.CP))
known = fx | set(B.REM) | set(B.CP) | set(B.V9) | set(B.CR) | set(B.NM) | set(B.CL) | set(B.DEF) | set(B.ALIAS) | set(B.STALE)
PAT = re.compile(r"\b(REM-[0-9A-Z]{2}|CP-T\d\d-\d\d|CR-\d\d|NM-W\d|CL-[A-Z]+|DEF-\d+)\b")
unk = sorted({m.group(1) for m in PAT.finditer(led)} - known)
print("handles named in -06 that the batch map does not know:", unk or "none"); bad += bool(unk)
for f in sorted(glob.glob(os.path.join(PLAN, "*.md"))):
    t = open(f).read()
    u = sorted({m.group(1) for m in PAT.finditer(t)} - known)
    if u: print(os.path.basename(f), "unknown handles:", u)
sys.exit(1 if bad else 0)
