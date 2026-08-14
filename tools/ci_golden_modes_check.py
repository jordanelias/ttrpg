#!/usr/bin/env python3
"""Field-golden byte-exact gate — the shipped configuration's regression oracle (plan-v2 A1b).

Runs `tests/sim/mass_battle/bat.py --check` in the two FIELD_MOVEMENT=1 modes
(`unit_field` PER_CELL=0, `cell_field` PER_CELL=1) with the FULL digest-relevant
toggle vector pinned. Complements tests/valoria/test_mass_battle_byte_exact.py,
which covers only the two LEGACY-LATTICE modes — before this gate existed, both field
goldens sat red for 5 days undetected (PRs #235/#236 re-recorded the lattice arm only;
bisected and re-recorded in plan-v2 A1a).

PIN DOCTRINE (ED-1089, ED-MB-0045 A1b): every pin below is the value the field
goldens were RECORDED at — mostly the shipped defaults, pinned explicitly so an
ambient env var in the runner can't silently check a different battle against
the golden (minimal pinning is how ED-1089 went wrong). The pin list covers
every env read classified digest-relevant OR default-inert-but-reachable by the
A1b inventory + its adversarial critic pass (85 unique env names swept twice,
independently); the residue is the provably battery-inert set, enumerated
EXPLICITLY in tests/valoria/test_field_golden_pins.py's _KNOWN_INERT — the
completeness direction is asserted there, not claimed here. Re-classify before
trusting this if bat.py's battery ever grows a yield/feign/ordered-volley row.

DRIFT GUARD: tests/valoria/test_field_golden_pins.py asserts every pin here
equals the source-level environ.get default — a default flip in config.py
without a deliberate, golden-re-recording edit here fails that test loudly.

Mutation check: `--perturb NAME=VALUE` overrides one pin so the job's ability
to fail can be demonstrated (a gate that cannot fail is not a gate, G2).

Exit 0 iff both modes print [BYTE-EXACT OK].
"""
import os
import subprocess
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
BAT = os.path.join(REPO, 'tests', 'sim', 'mass_battle', 'bat.py')

# ── The single owner of the field-mode pin vector ──────────────────────────────
# Keyed by ENV NAME (note SIGMA_HEAD, not SIGMA_HEAD_ENABLED — config.py:292).
# Sources: _PINNED_OFF's non-mode members (test_mass_battle_byte_exact.py:74-89)
# + the A1b inventory's digest-relevant groups A (shared code, all modes),
# B (PER_CELL-gated) and C (field/node-gated) + the critic pass's five
# default-inert-but-reachable flags, values = environ.get defaults.
FIELD_PINS = {
    # determinism (empirically hash-order-independent per A1a's runs; pinned anyway)
    'PYTHONHASHSEED': '0',
    # _PINNED_OFF carry-over (lattice dict minus the two field-mode selectors)
    'FIELD_CONTACT': '0', 'PC_FACING_MODEL': '0', 'CONTACT_REACH': '0.0',
    'PC_OCTAGON_DMG': '1', 'PC_CELL_MORALE': '0',
    # Group A — unconditional in shared code (digest-relevant in all four modes)
    'SIGMA_HEAD': '1', 'MORALE_FIX': '1', 'PC_STOCHASTIC_ROUT': '1',
    'ROUT_CASCADE_FRAC': '1.0', 'REFORM_CHECK_ENABLED': '0',
    'PC_CONVERGENCE_NORM': '1', 'PC_CELL_DAMAGE': '0', 'MULTI_SIDE_SHOCK': '0.5',
    'OCTAGON_LOCAL_REACH': '2.0', 'FACING_REACTION_TICKS': '2',
    'LANCHESTER_ENABLED': '1', 'K_LINEAR': '12', 'K_SQUARE': '0.25',
    'LANCHESTER_STRENGTH_REF': '4', 'LANCHESTER_DENSITY_REF': '100',
    'POOL_QUALITY_MODEL': '1', 'POOL_QUALITY_SCALE': '0.5',
    'PC_VOLLEY_DENSITY_ENABLED': '1', 'PC_VOLLEY_DENSITY_REF': '80',
    'PC_VOLLEY_DENSITY_FLOOR': '0.5', 'PC_VOLLEY_DENSITY_CAP': '2.0',
    'CASUALTY_SCALE': '4',   # unreachable while LANCHESTER_ENABLED=1; defense-in-depth
    # Group B — PER_CELL-gated (inert in unit_field; pinned uniformly so the dict
    # is mode-agnostic and copy-pasteable)
    'PC_REFUSE': '1', 'PC_ENVELOP_MOD': '-1.0', 'PC_ENVELOP_DEPTH_RESIST': '0.3',
    'PC_POCKET_MOD': '-1.0', 'PC_POCKET_REACH': '2', 'PC_FIXING_FLANK': '1',
    'PC_ROLLUP_PER_RANK': '0.4', 'PC_ROLLUP_MARGIN': '1.0', 'PC_ROLLUP_REACH': '1.6',
    'PC_ROLLUP_CAP': '-1.0', 'PC_ROLLUP_FLANK_REACH': '1.0', 'PC_ROLLUP_MIN_DEPTH': '2.0',
    'PC_ENVELOP_SHOCK': '1', 'PC_BRACE_ENABLED': '1', 'PC_RECOIL_FRONTAL': '1',
    'PC_CHARGE_RECOIL': '6', 'PC_BRACE_SETUP_DELAY': '1', 'PC_RECOIL_CHARGER_GATE': '1',
    # Group C — field/node-gated
    'PC_ENVELOP_SPEED_MULT': '2.0', 'ENVELOP_STANDOFF': '8.0', 'ENVELOP_ORBIT_CAP': '10',
    'PC_REACH_FACING_GATE': '1', 'PC_WHEEL': '1', 'PC_ENVELOP_PATH': '1', 'PC_SWEEP': '1',
    # Critic-pass additions (2026-07-29): default-inert but REACHABLE at these pins —
    # an ambient flip produces a loud spurious red, so pin them for hermeticity.
    # (PC_FRICTION_CEV enabling shifts the RNG stream — orchestration.py's own comment;
    # PC_INTENT_RESOLUTION is live via the battery's stance='hold' rows; PC_CLOSE_RANKS
    # via the PER_CELL lifecycle; PC_TROOP_DENSITY_CAP via the cavalry rows.)
    'PC_FRICTION_CEV': '0', 'PC_FRICTION_SIGMA': '1.1', 'PC_FRACTIONAL_POOL': '0',
    'PC_INTENT_RESOLUTION': '0', 'PC_CLOSE_RANKS': '0', 'PC_TROOP_DENSITY_CAP': '0',
    # [ED-MB-0059, 2026-07-29] Same-side cell exclusion. Default ON, and STRONGLY digest-moving on
    # the two field modes (it is a no-op on the legacy-lattice modes — the pass lives inside
    # resolve_toi_and_commit, which only runs under FIELD_MOVEMENT). Pinned at its shipped default
    # for the same reason every Group C entry is: an ambient flip must produce a named red here,
    # not a mystery digest mismatch.
    'PC_CELL_EXCLUSION': '1',
}

# [ED-MB-0053 / plan-v2 §4a, 2026-07-29] Renamed from ci_field_golden_check.py: this tool is the
# single owner of "run bat.py --check in a pinned configuration, outside the tests/valoria budget",
# and that is no longer only about the FIELD modes. The fifth digest mode is a GRID mode, so keeping
# the field-only name would either have misfiled it or spawned a second owner for the same job.
#
# Why the fifth mode lives here rather than in pytest: it is a full ~4-minute battery, and the
# unit-tests job already measures ~9-11m43s against a 16-minute cap. Adding it there buys a
# mysterious mid-run cancellation, not coverage. What stays in pytest is the cheap half — that
# bat._mode_key is INJECTIVE over the toggle cube, which is the trap this mode actually walked into.
MODES = {
    'unit_field_mor0': {'FIELD_MOVEMENT': '1', 'PC_NODE_COHESION': '1', 'PER_CELL': '0'},
    'cell_field_mor0': {'FIELD_MOVEMENT': '1', 'PC_NODE_COHESION': '1', 'PER_CELL': '1'},
    # The §4a fifth mode. The other four all run at PC_CELL_MORALE=0, where the three cell-morale
    # maps are EMPTY — so they pin float-order over every per-cell map EXCEPT the three whose
    # desync motivates the ownership work, and "if a digest moves, you changed behaviour" was
    # vacuous over exactly the state B1a is about to refactor. This overrides FIELD_PINS'
    # PC_CELL_MORALE='0' deliberately; the mode-key assertion below is what makes that safe.
    'cell_legacy_mor1': {'FIELD_MOVEMENT': '0', 'PC_NODE_COHESION': '0', 'PER_CELL': '1',
                'PC_CELL_MORALE': '1'},
}


def main(argv):
    perturb = {}
    args = list(argv[1:])
    while '--perturb' in args:
        i = args.index('--perturb')
        if i + 1 >= len(args) or '=' not in args[i + 1]:
            print("usage: --perturb NAME=VALUE")
            return 2
        name, _, value = args[i + 1].partition('=')
        perturb[name] = value
        del args[i:i + 2]
    failures = 0
    for mode, selectors in MODES.items():
        env = dict(os.environ)
        env.update(FIELD_PINS)
        env.update(selectors)
        env.update(perturb)
        try:
            # 300s/mode: the slowest observed single-mode run is ~150s on ordinary dev
            # hardware (test_mass_battle_byte_exact.py's budget rationale); 2x300s fits
            # the job's 12-minute ceiling with room for setup.
            r = subprocess.run(['python3', BAT, '--check'], cwd=REPO, env=env,
                               capture_output=True, text=True, timeout=300)
        except subprocess.TimeoutExpired:
            print(f"[FAIL] {mode}: timed out after 300s — treat as a gate failure, not a flake")
            failures += 1
            continue
        # The mode assertion closes the one false-OK path (critic C1): a perturbation of
        # PER_CELL/FIELD_MOVEMENT would re-target bat.py's EXPECTED lookup and print
        # BYTE-EXACT OK against a DIFFERENT golden — ED-1089's exact shape. Requiring the
        # child to name the mode we asked for makes that impossible.
        ok = '[BYTE-EXACT OK]' in r.stdout and f'DIGEST {mode} ' in r.stdout
        print(f"[{'OK' if ok else 'FAIL'}] {mode}: {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-200:]}")
        if not ok:
            failures += 1
    if perturb:
        print(f"(ran with perturbation {perturb} — a FAIL above is the expected mutation result)")
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
