"""Driver for the field-based mass-battle stress test (2026-07-22).

Runs S0–S5 and prints a full report. Flag A/B isolation (S3) and off-by-default activation (S4)
shell out to `mb_fieldbased_stress.py --emit` in fresh subprocesses, because every gate in
`mass_battle/config.py` + `hierarchy/units.py` is read from os.environ ONCE at import time — the
only correct way to A/B a flag is a clean process per env (the same reason the byte-exact CI test
spawns bat.py per mode).

Usage:  python3 run.py [n_fuzz=200] [--json out.json]
"""
import os
import sys
import json
import subprocess
import statistics
import random

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, '..', '..'))
_SIM = os.path.join(_REPO, 'tests', 'sim')
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import mb_fieldbased_stress as S            # noqa: E402
import mass_battle.config as C              # noqa: E402
import mass_battle.hierarchy.units as HU    # noqa: E402
import mass_battle.orchestration as ORCH    # noqa: E402
from mass_battle.engine import mechanics_selftest, MECHANICS  # noqa: E402
import mass_battle.validators as V          # noqa: E402

STRESS_PY = os.path.join(_HERE, 'mb_fieldbased_stress.py')
REPORT = {}


def hr(t):
    print("\n" + "=" * 92 + f"\n{t}\n" + "=" * 92)


def emit_under(env_overrides, scenario, seeds=12):
    """Run the --emit runner in a clean subprocess with env overrides; return its parsed vector."""
    env = dict(os.environ)
    env["PYTHONHASHSEED"] = "0"
    env.update({k: str(v) for k, v in env_overrides.items()})
    out = subprocess.run([sys.executable, STRESS_PY, "--emit", scenario, str(seeds)],
                         capture_output=True, text=True, env=env, cwd=_HERE)
    if out.returncode != 0:
        return {"error": out.stderr.strip().splitlines()[-1] if out.stderr.strip() else f"rc={out.returncode}"}
    return json.loads(out.stdout.strip())


def vectors_differ(v1, v2):
    """A/B: do two result vectors differ materially (flag is live/non-inert)?"""
    if "error" in v1 or "error" in v2:
        return None
    keys = ("winA", "winB", "draw", "meanA", "meanB")
    return any(abs((v1[k]) - (v2[k])) > (1e-4 if k.startswith("mean") else 0) for k in keys)


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S0 — WIRING CENSUS
# ──────────────────────────────────────────────────────────────────────────────────────────────
def s0_wiring_census():
    hr("S0  WIRING CENSUS + FIELD-CONFIG ACTIVATION")
    ok, missing = mechanics_selftest()
    print(f"mechanics_selftest: ok={ok}  missing={missing}  ({len(MECHANICS)} registered mechanics)")

    field = {"FIELD_MOVEMENT": HU.FIELD_MOVEMENT, "PC_NODE_COHESION": C.PC_NODE_COHESION, "PER_CELL": C.PER_CELL}
    grid_oracle_active = not any(field.values())
    print(f"field triad: {field}   -> field-based={all(field.values())}  grid-oracle-active={grid_oracle_active}")

    # roster: every mechanic, its toggle, and whether that toggle is at its all-on field value
    def flag_val(name):
        if name is None:
            return "(always)"
        for mod in (C, HU, ORCH):
            if hasattr(mod, name):
                return getattr(mod, name)
        return "?"
    print(f"\n{'mechanic':24} {'fn':28} {'toggle':22} {'live':8} status")
    off = []
    for name, spec in MECHANICS.items():
        tv = flag_val(spec["toggle"])
        print(f"{name:24} {spec['fn']:28} {str(spec['toggle']):22} {str(tv):8} {spec['status']}")
        if spec["toggle"] and tv in (False, 0, "0"):
            off.append((name, spec["toggle"]))
    print(f"\nWIRED mechanics whose gate is OFF under field defaults: {off or 'none'}")

    # full env-gate roster (beyond MECHANICS): the field vs off-by-default split
    on_flags = {k: flag_val(k) for k in
                ["FIELD_MOVEMENT", "PC_NODE_COHESION", "PER_CELL", "LANCHESTER_ENABLED", "POOL_QUALITY_MODEL",
                 "COMMAND_SIGMA_ENABLED", "MORALE_FIX", "SIGMA_HEAD_ENABLED", "VOLLEY_ENABLED", "CASCADING_ENABLED",
                 "PC_BRACE_ENABLED", "PC_RECOIL_FRONTAL", "PC_BRACE_SETUP_DELAY", "PC_RECOIL_CHARGER_GATE",
                 "PC_WHEEL", "PC_REFUSE", "PC_VOLLEY_DENSITY_ENABLED", "PC_KITE_ENABLED", "PC_ENVELOP_PATH", "PC_SWEEP"]}
    off_flags = {k: flag_val(k) for k in
                 ["PC_FACING_MODEL", "FIELD_CONTACT", "REFORM_CHECK_ENABLED"]}
    print(f"\nfield gates ON by default   : {on_flags}")
    print(f"gates OFF by default        : {off_flags}")
    print(f"do-not-enable (unratified)  : PC_FACING_SLEW_BASE={HU.PC_FACING_SLEW_BASE} "
          f"(CALIBRATED-DEBT, left OFF deliberately)")
    REPORT["s0"] = dict(selftest_ok=ok, missing=missing, n_mechanics=len(MECHANICS),
                        field=field, field_based=all(field.values()), gates_off_under_field=off,
                        on_flags={k: bool(v) if isinstance(v, bool) else v for k, v in on_flags.items()},
                        off_flags=off_flags)
    return ok and not off


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S1 — AGGREGATE FUZZ
# ──────────────────────────────────────────────────────────────────────────────────────────────
def s1_fuzz(n):
    hr(f"S1  AGGREGATE FUZZ  (n={n}, field defaults, full input surface)")
    f = S.aggregate_fuzz(n, seed_base=42000, max_turns=40)
    print(f"constructed & ran : {f['built']}   (rejected at construction: {f['rej']}  "
          f"[incl. {f['over_cap']} over-cap ValueError — correct SUBUNIT_CAP={S.SUBUNIT_CAP} enforcement])")
    print(f"ENGINE FAILURES   : {f['engfail']}    <- defect surface (exceptions during run_battle)")
    print(f"INVARIANT VIOL.   : {f['viol']}    <- defect surface (NaN/hp-range/cell!=hp/bad-winner)")
    print(f"made contact      : {f['contact']}/{f['built']} ({f['contact_rate']})   "
          f"<- post-DG-10-fix closing health (rest are hold/retreat/never-in-range, legitimate)")
    print(f"outcomes          : {f['wins']}   mean turns: {f['mean_turns']}")
    for nm, msg, last in f["fail_ex"]:
        print(f"    FAIL  {nm}: {msg}  | {last}")
    for iss, sa, sb in f["viol_ex"]:
        print(f"    VIOL  {iss}  A={sa} B={sb}")
    REPORT["s1"] = f
    return f["engfail"] == 0 and f["viol"] == 0


def s1b_movement():
    hr("S1b  MOVEMENT CENSUS  (DG-10 field-closing fix — isolation proof per troop type)")
    print("Every canonical troop type, plain Line, balanced stance, must CLOSE to contact on the field")
    print("path. Pre-fix: all disc<5 types (levy/light_inf/heavy_inf/archers/crossbow/sling/artillery)")
    print("froze at advance-step 0 and never met the enemy. Post-fix: all close.\n")
    rows, all_closed = S.movement_census()
    print(f"{'troop_type':16} {'eff_disc':>8}  closed?  defender_hp_left")
    for tt, disc, closed, bhp in rows:
        flag = "yes" if closed else "NO (still frozen!)"
        print(f"{tt:16} {disc:>8}  {flag:20} {bhp:.0f}")
    print(f"\nall troop types close: {all_closed}")
    REPORT["s1b"] = dict(all_closed=all_closed, rows=[(t, d, c, h) for t, d, c, h in rows])
    return all_closed


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S2 — ISOLATION VALIDATORS (field mode)
# ──────────────────────────────────────────────────────────────────────────────────────────────
def s2_validators():
    hr("S2  ISOLATION VALIDATORS  (per-mechanic historical-goal probes)")
    print("Combat-mechanic validators run under the ambient FIELD default (PER_CELL=1, node path).")
    print("Movement-instruction validators (V-ENVELOP/V-SWEEP) are reported on BOTH the grid arm")
    print("(their regression default) and the field/node arm (the live path, known-flaky — xfail in CI).\n")
    res = {}
    # combat validators — field-side (they never touch _set_movement_path)
    for g in (V.v_cannae, V.v_fixing, V.v_shock, V.v_brace, V.v_reform, V.v_archer):
        r = g()
        res[r.name] = r.passed
        print(f"[{'PASS' if r.passed else 'FAIL'}] {r.name:10} measured={r.measured}  | {r.anchor}")
    # maneuver validators — grid arm + field(node) arm
    for g, nm in ((V.v_envelop, "V-ENVELOP"), (V.v_sweep, "V-SWEEP")):
        rg = g(path='grid', seeds=12)
        rn = g(path='node', seeds=12)          # 'node' == the field coordinate path
        res[nm + "/grid"] = rg.passed
        res[nm + "/field"] = rn.passed
        print(f"[{'PASS' if rg.passed else 'FAIL'}] {nm:10} grid  measured={rg.measured}")
        print(f"[{'PASS' if rn.passed else 'FAIL'}] {nm:10} field measured={rn.measured}   "
              f"(field/node arm — ED-MB-0002..0005 known-flaky)")
    REPORT["s2"] = res
    # gate S2 on the combat validators + the grid maneuver regression; field maneuver arm is reported, not gated
    gated = [k for k in res if not k.endswith("/field")]
    return all(res[k] for k in gated)


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S3 — PER-FLAG A/B ISOLATION (subprocess)
# ──────────────────────────────────────────────────────────────────────────────────────────────
# (flag, scenario, default_env, flipped_env, expectation)  expectation: 'live' | 'inert-ok'
FLAG_AB = [
    ("PER_CELL",              "charge_vs_brace", {"PER_CELL": 1}, {"PER_CELL": 0, "PC_NODE_COHESION": 0, "FIELD_MOVEMENT": 0}, "live"),
    ("LANCHESTER_ENABLED",    "big_vs_small",    {"LANCHESTER_ENABLED": 1}, {"LANCHESTER_ENABLED": 0}, "live"),
    ("POOL_QUALITY_MODEL",    "big_vs_small",    {"POOL_QUALITY_MODEL": 1}, {"POOL_QUALITY_MODEL": 0}, "live"),
    ("COMMAND_SIGMA_ENABLED", "mirror",          {"POOL_QUALITY_MODEL": 0, "COMMAND_SIGMA_ENABLED": 1},
                                                 {"POOL_QUALITY_MODEL": 0, "COMMAND_SIGMA_ENABLED": 0}, "live"),
    ("MORALE_FIX",            "mirror",          {"MORALE_FIX": 1}, {"MORALE_FIX": 0}, "live"),
    ("SIGMA_HEAD",            "mirror",          {"SIGMA_HEAD": 1}, {"SIGMA_HEAD": 0}, "live"),
    ("PC_BRACE_ENABLED",      "charge_vs_brace", {"PC_BRACE_ENABLED": 1}, {"PC_BRACE_ENABLED": 0}, "live"),
    ("PC_RECOIL_FRONTAL",     "charge_vs_brace", {"PC_RECOIL_FRONTAL": 1}, {"PC_RECOIL_FRONTAL": 0}, "live"),
    ("PC_BRACE_SETUP_DELAY",  "charge_vs_brace", {"PC_BRACE_SETUP_DELAY": 1}, {"PC_BRACE_SETUP_DELAY": 0}, "live"),
    ("PC_CHARGE_RECOIL",      "charge_vs_brace", {"PC_CHARGE_RECOIL": 6}, {"PC_CHARGE_RECOIL": 0}, "live"),
    ("PC_WHEEL",              "envelop",         {"PC_WHEEL": 1}, {"PC_WHEEL": 0}, "live"),
    ("PC_REFUSE",             "envelop",         {"PC_REFUSE": 1}, {"PC_REFUSE": 0}, "live"),
    ("PC_VOLLEY_DENSITY_ENABLED", "ranged_dense", {"PC_VOLLEY_DENSITY_ENABLED": 1}, {"PC_VOLLEY_DENSITY_ENABLED": 0}, "live"),
    ("PC_ENVELOP_MOD",        "envelop",         {"PC_ENVELOP_MOD": -1.0}, {"PC_ENVELOP_MOD": 0.0}, "live"),
    ("K_LINEAR",              "big_vs_small",    {"K_LINEAR": 12}, {"K_LINEAR": 24}, "live"),
    ("POOL_QUALITY_SCALE",    "mirror",          {"POOL_QUALITY_SCALE": 0.5}, {"POOL_QUALITY_SCALE": 1.0}, "live"),
]


def s3_flag_ab():
    hr("S3  PER-FLAG A/B ISOLATION  (each gate flipped in a clean subprocess -> WIRED or inert?)")
    print("A gate is 'WIRED' if flipping it changes the outcome vector on a sensitive scenario.\n")
    rows = {}
    all_ok = True
    for flag, scn, denv, fenv, expect in FLAG_AB:
        v_def = emit_under(denv, scn)
        v_flip = emit_under(fenv, scn)
        diff = vectors_differ(v_def, v_flip)
        if diff is None:
            verdict = "ERROR"
            all_ok = False
        elif diff:
            verdict = "WIRED"
        else:
            verdict = "INERT"
            if expect == "live":
                all_ok = False
        rows[flag] = dict(scenario=scn, verdict=verdict, default=v_def, flipped=v_flip)
        d = "" if diff is None else (f"A:{v_def.get('winA')}/{v_def.get('meanA')} -> {v_flip.get('winA')}/{v_flip.get('meanA')}")
        print(f"[{verdict:5}] {flag:26} ({scn:15}) {d}")
        if "error" in v_def:
            print(f"         default  err: {v_def['error']}")
        if "error" in v_flip:
            print(f"         flipped  err: {v_flip['error']}")
    REPORT["s3"] = rows
    return all_ok


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S4 — ACTIVATE OFF-BY-DEFAULT FIELD GATES
# ──────────────────────────────────────────────────────────────────────────────────────────────
def s4_off_gates():
    hr("S4  ACTIVATE OFF-BY-DEFAULT GATES  (turn ON, check for breakage under field mode)")
    print("These default OFF but are legitimate field-mode gates. Turn each ON (and combined) over")
    print("every probe scenario; a gate is SAFE if no scenario errors or breaks invariants.\n")
    configs = {
        "baseline(field)":        {},
        "PC_FACING_MODEL=1":      {"PC_FACING_MODEL": 1},
        "FIELD_CONTACT=1":        {"FIELD_CONTACT": 1},
        "REFORM_CHECK_ENABLED=1": {"REFORM_CHECK_ENABLED": 1},
        "ALL_THREE_ON":           {"PC_FACING_MODEL": 1, "FIELD_CONTACT": 1, "REFORM_CHECK_ENABLED": 1},
    }
    rows = {}
    all_ok = True
    for label, env in configs.items():
        per_scn = {}
        safe = True
        for scn in S.SCENARIOS:
            v = emit_under(env, scn)
            if "error" in v:
                per_scn[scn] = "ERR:" + v["error"][:40]
                safe = False
            else:
                per_scn[scn] = f"A{v['winA']}/B{v['winB']}/d{v['draw']} viol={v['viol']}"
                if v["viol"]:
                    safe = False
        rows[label] = dict(safe=safe, scenarios=per_scn)
        print(f"[{'SAFE' if safe else 'BROKE'}] {label}")
        for scn, s in per_scn.items():
            print(f"         {scn:16} {s}")
        if not safe:
            all_ok = False
    print(f"\nPC_FACING_SLEW_BASE deliberately NOT activated (config comment: 'NOT ratified -- do not enable').")
    REPORT["s4"] = rows
    return all_ok


# ──────────────────────────────────────────────────────────────────────────────────────────────
# S5 — DETERMINISM + MIRROR SYMMETRY
# ──────────────────────────────────────────────────────────────────────────────────────────────
def s5_controls():
    hr("S5  CONTROLS  (determinism + order-cancelled mirror symmetry)")
    # determinism: same seed -> identical vector, twice
    v1 = S.emit_vector("charge_vs_brace", seeds=8)
    v2 = S.emit_vector("charge_vs_brace", seeds=8)
    det = (v1 == v2)
    print(f"[{'PASS' if det else 'FAIL'}] determinism: identical result vector on repeat  ({v1==v2})")

    # mirror symmetry: identical random formation both sides, order swapped -> engine is side-neutral
    from mass_battle.engine import build_army, run_battle
    aw = bw = dr = 0
    for t in range(24):
        rng = random.Random(70000 + t)
        spec = S._rand_subunit_spec(rng, 'A')
        spec.pop("orders", None)               # keep the mirror clean/symmetric
        spec.pop("starting_position", None)
        def mk(fac):
            sp = dict(spec)
            return build_army([sp], fac, fac)
        random.seed(500 + t); w1 = run_battle(mk('A'), mk('B'), max_turns=40).get('winner')
        random.seed(500 + t); w2 = run_battle(mk('B'), mk('A'), max_turns=40).get('winner')  # swapped
        for w, swap in ((w1, False), (w2, True)):
            if w in ('draw', None): dr += 1
            elif (w == 'A') != swap: aw += 1
            else: bw += 1
    tot = aw + bw + dr
    skew = abs(aw - bw)
    # a perfectly side-neutral engine, order-cancelled, has |skew| bounded by RNG noise
    sym_ok = skew <= max(4, int(0.25 * tot))
    print(f"[{'PASS' if sym_ok else 'WARN'}] mirror symmetry: A-favoured {aw}  B-favoured {bw}  draw {dr}  |skew|={skew}/{tot}")
    REPORT["s5"] = dict(determinism=det, mirror=dict(aw=aw, bw=bw, draw=dr, skew=skew, tot=tot, ok=sym_ok))
    return det and sym_ok


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 200
    out_json = None
    if "--json" in sys.argv:
        out_json = sys.argv[sys.argv.index("--json") + 1]

    print("FIELD-BASED MASS-BATTLE STRESS TEST  ·  2026-07-22  ·  engine: tests/sim/mass_battle/")
    results = {}
    results["S0 wiring"]      = s0_wiring_census()
    results["S1 fuzz"]        = s1_fuzz(n)
    results["S1b movement"]   = s1b_movement()
    results["S2 validators"]  = s2_validators()
    results["S3 flag A/B"]    = s3_flag_ab()
    results["S4 off-gates"]   = s4_off_gates()
    results["S5 controls"]    = s5_controls()

    hr("VERDICT")
    for k, v in results.items():
        print(f"  [{'PASS' if v else 'FAIL/ATTN'}] {k}")
    REPORT["verdict"] = {k: bool(v) for k, v in results.items()}
    if out_json:
        with open(out_json, "w") as fh:
            json.dump(REPORT, fh, indent=2, default=str)
        print(f"\nwrote {out_json}")


if __name__ == '__main__':
    main()
