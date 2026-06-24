"""stage_engine.py — regenerate the instrumented engine copy `_engine/` used by stress_matrix.py.

`_engine/` is a verbatim copy of designs/scene/combat_engine_v1/ with TWO inert per-fighter isolation
hooks (derived_scale['pool'|'health'], default empty so the mirror stays 50/50). It is .gitignored
(test instrumentation, not canon); run this once after checkout to (re)create it. Idempotent.
"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "designs", "scene", "combat_engine_v1"))
DST = os.path.join(HERE, "_engine")

os.makedirs(DST, exist_ok=True)
for f in os.listdir(SRC):
    if f.endswith(".py"):
        shutil.copy2(os.path.join(SRC, f), os.path.join(DST, f))


def patch(fn, old, new):
    p = os.path.join(DST, fn)
    s = open(p, encoding="utf-8").read()
    if new.split("[STRESS-HARNESS]")[0].strip() in s or "derived_scale" in s and fn == "combatant.py" and "[STRESS-HARNESS]" in s:
        pass
    assert s.count(old) == 1, f"{fn}: expected 1 match for hook anchor, got {s.count(old)}"
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


# combatant.py — declare the per-fighter isolation hook dict (default empty = inert)
patch("combatant.py",
      "        self.health_full=self.wt.health_full",
      "        self.health_full=self.wt.health_full\n        self.derived_scale = {}   # [STRESS-HARNESS] per-fighter derived-score isolation (default empty = inert)")

# wrapper.py — pool isolation at the two resolution-pool sites
patch("wrapper.py",
      "                pool=max(1, core.resolution_pool(longer.history))",
      "                pool=max(1, int(round(core.resolution_pool(longer.history)*getattr(longer,'derived_scale',{}).get('pool',1.0))))")
patch("wrapper.py",
      "        pool=max(1, core.resolution_pool(aggressor.history))",
      "        pool=max(1, int(round(core.resolution_pool(aggressor.history)*getattr(aggressor,'derived_scale',{}).get('pool',1.0))))")

# wrapper.py — health isolation at the per-bout wound-tracker reset (canon-faithful re-init kept; scale layered on)
patch("wrapper.py",
      "    A.wt.__init__(A.end); B.wt.__init__(B.end)   # reset wounds",
      "    A.wt.__init__(A.end); B.wt.__init__(B.end)   # reset wounds (canon-faithful re-init)\n"
      "    for _c in (A,B):                              # [STRESS-HARNESS] Health-isolation hook (inert at scale 1.0)\n"
      "        _hs=getattr(_c,'derived_scale',{}).get('health',1.0)\n"
      "        if _hs!=1.0: _c.wt.health_full=int(round(_c.wt.health_full*_hs))")

print(f"[staged] {DST} (verbatim combat_engine_v1 + 2 inert isolation hooks)")
