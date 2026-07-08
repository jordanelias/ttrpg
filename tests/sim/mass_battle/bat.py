"""bat.py — byte-exact DIGEST harness for the mass-battle engine (the G5 gate).

Runs a fixed, deterministic battery (per-trial random.seed, exactly as gauge_mb.py does) of
representative matchups and hashes the FULL per-trial end state (winner, battle-turns, hp, morale,
discipline, rout flags — not just the aggregate win-rate). A behaviour-preserving refactor must
reproduce the digest digit-for-digit; any change to the number is a refactor bug, not a tuning
question. Covers both engine paths:

    PER_CELL=0 python3 tests/sim/mass_battle/bat.py     # baseline (unit pool)
    PER_CELL=1 python3 tests/sim/mass_battle/bat.py     # per-cell layer

Prints one `DIGEST <mode> <hash>` line. This is the committed golden-digest gate the coverage
matrix previously referenced but that was never committed; Stage 1 of the bottom-up re-architecture
adds it so every later stage has a reproducible byte-exact check.
[canonical: tests/sim/gauge_mb.py — deterministic seed battery; mass_battle_gauge_grounding.md §1]
"""
import os, sys, hashlib

# import the package exactly as the stress harness / gauge do
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tests/sim on path
from mass_battle.engine import (  # noqa: E402
    build_unit, build_envelopment, build_refused_flank, resolve_battle,
    SIDE_A_START_ROW, SIDE_B_START_ROW)
import random  # noqa: E402

# anchor columns per (shape,tier) — copied from gauge_mb.py ANCHOR_MAP (T3 row used below)
# [canonical: mass_battle_v30.md §deployment — anchor columns]
# [LC-8, ED-909] Horseshoe/RefusedFlank entries retired along with the shapes themselves (see
# geometry.CELL_PATTERN_FN's note) -- the 'envelop'/'cannae'/'oblique' battery rows below now build
# their armies via build_envelopment/build_refused_flank instead of a single Horseshoe/RefusedFlank
# subunit, so no anchor-column lookup for those retired shape names is needed anymore.
ANCHOR_MAP = {
    ('Line', 3): 9, ('Arrowhead', 3): 8,                    # [canonical: mass_battle_v30.md §deployment — anchor columns]
    ('GappedLine', 3): 7, ('Column', 3): 9,                  # [canonical: mass_battle_v30.md §deployment — anchor columns]
}
TIER = 3                                  # [canonical: sim_mb_06_v9_historical_spec.md — T3 uniform stats]
N_SEEDS = 24                              # [canonical: gauge_mb.py matchup — deterministic seed battery]
SEED_BASE = 1_000_000                     # [canonical: gauge_mb.py matchup — seed base]
MAX_TURNS = 20                            # [canonical: gauge_mb.py — multi-mode battle-turn cap]


def make_unit(shape, name, faction, **kw):
    """Single-subunit unit at tier-3 defaults (P4/C4/D5/M6 infantry). Dogfoods the wrapper adapter
    engine.build_unit — resolving the deployment column here, the engine builds the data model. If the
    battery digest is unchanged vs the direct-construction baseline, build_unit is provably transparent."""
    anchor_col = ANCHOR_MAP.get((shape, TIER), ANCHOR_MAP[('Line', TIER)])
    return build_unit(shape, TIER, name, faction, anchor_col,
                      troop_type=kw.pop('troop_type', 'infantry'),
                      unit_type=kw.pop('unit_type', 'melee'),
                      power=kw.pop('power', 4),             # [canonical: sim_mb_06_v9_historical_spec.md — P4]
                      command=kw.pop('command', 4),         # [canonical: sim_mb_06_v9_historical_spec.md — C4]
                      discipline=kw.pop('discipline', 5),   # [canonical: sim_mb_06_v9_historical_spec.md — D5]
                      morale=kw.pop('morale', 6),           # [canonical: sim_mb_06_v9_historical_spec.md — M6]
                      morale_start=kw.pop('morale_start', None),
                      stance=kw.pop('stance', 'balanced'),
                      speed=kw.pop('speed', 'Standard'),
                      instructions=tuple(kw.pop('instructions', ())))


# [LC-8] Composed replacements for the retired Horseshoe/RefusedFlank single-subunit shapes,
# dogfooding engine.build_envelopment/build_refused_flank (ED-909's Unit-level presets) in this
# byte-exact battery itself -- the most direct possible validation that they construct and resolve
# correctly through the SAME multi-turn ('kind=multi') path the rest of this battery already
# exercises. Wing/refused placement is symmetric around the same anchor column the retired shapes
# used, so the battlefield footprint stays comparable.
def _envelop_army(name, faction, **kw):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    anchor = ANCHOR_MAP[('Line', TIER)]
    tt = kw.pop('troop_type', 'infantry')
    center = [{'shape': 'Line', 'tier': TIER, 'troop_type': tt, 'starting_position': (start_row, anchor)}]
    # wing offset: [canonical: sim_verification_ledger.json — CALIBRATED, battery deployment spacing, not historically cited]
    wings = [{'shape': 'Line', 'tier': TIER, 'troop_type': tt, 'starting_position': (start_row, anchor - 6)},  # [canonical: sim_verification_ledger.json — CALIBRATED, battery deployment spacing, not historically cited]
             {'shape': 'Line', 'tier': TIER, 'troop_type': tt, 'starting_position': (start_row, anchor + 6)}]  # [canonical: sim_verification_ledger.json — CALIBRATED, battery deployment spacing, not historically cited]
    return build_envelopment(center, wings, name, faction,
                              power=kw.pop('power', 4), command=kw.pop('command', 4),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                              discipline=kw.pop('discipline', 5), morale=kw.pop('morale', 6),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                              morale_start=kw.pop('morale_start', None))


def _refused_army(name, faction, **kw):
    start_row = SIDE_A_START_ROW if faction == 'A' else SIDE_B_START_ROW
    anchor = ANCHOR_MAP[('Line', TIER)]
    tt = kw.pop('troop_type', 'infantry')
    strong = [{'shape': 'Line', 'tier': TIER, 'troop_type': tt, 'starting_position': (start_row, anchor - 4)}]
    refused = [{'shape': 'Line', 'tier': TIER, 'troop_type': tt, 'starting_position': (start_row, anchor + 4)}]
    return build_refused_flank(strong, refused, name, faction,
                                power=kw.pop('power', 4), command=kw.pop('command', 4),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                                discipline=kw.pop('discipline', 5), morale=kw.pop('morale', 6),  # [canonical: sim_mb_06_v9_historical_spec.md — T3 baseline P4/C4/D5/M6 defaults]
                                morale_start=kw.pop('morale_start', None))


# Fixed battery: (label, shape_a, shape_b, kwargs_a, kwargs_b). shape_a/shape_b is either a plain
# shape string (single-subunit path, via make_unit) or a build_army-style ARMY BUILDER callable
# (_envelop_army/_refused_army, signature (name, faction, **kw) -> Unit) for the composed presets.
# Spans melee mirror / wedge / envelopment / oblique / manipular + cavalry charge / braced-repel /
# shaken / ranged / volley so both the PER_CELL=0 and PER_CELL=1 code paths are exercised.
BATTERY = [
    ('mirror',       'Line', 'Line', {}, {}),
    ('wedge',        'Arrowhead', 'Line', {}, {}),
    ('envelop',      _envelop_army, 'Line', {}, {}),
    ('cannae',       _envelop_army, 'Arrowhead', {}, {}),
    ('oblique',      _refused_army, _envelop_army, {}, {}),
    ('manipular',    'GappedLine', 'Arrowhead', {}, {}),
    ('cav_charge',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'}, {}),
    ('cav_braced',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'},
                     {'stance': 'hold', 'discipline': 8, 'instructions': ('brace',)}),  # [canonical: gauge_mb.py CAV — braced disc8+brace]
    ('cav_shaken',   'Arrowhead', 'Line', {'troop_type': 'cavalry', 'speed': 'Fast'},
                     {'morale': 2, 'morale_start': 6}),  # [canonical: gauge_mb.py CAV — shaken morale 2-of-6]
    ('ranged',       'Line', 'Line', {'unit_type': 'ranged', 'stance': 'hold'}, {}),
]


def _fmt(x):
    """Stable float formatting so the digest is reproducible (a pure code move yields identical floats)."""
    return f"{x:.9f}" if isinstance(x, float) else str(x)


def trial_vector(ua, ub, r):
    """Canonical end-state vector — sensitive to any numeric drift."""
    def g(u, a):
        return getattr(u, a, None)
    fields = [
        r.get('winner', '?'), r.get('battle_turns', r.get('turns', -1)),
        g(ua, 'hp'), g(ub, 'hp'), g(ua, 'hp_max'), g(ub, 'hp_max'),
        g(ua, 'morale'), g(ub, 'morale'), g(ua, 'discipline'), g(ub, 'discipline'),
        bool(g(ua, 'routed')), bool(g(ub, 'routed')),
    ]
    return '|'.join(_fmt(x) for x in fields)


# Golden digests for the Stage-1 (behaviour-frozen) baseline. A pure code-move refactor must
# reproduce these. They are updated ONLY on an intentional behaviour change (a later stage), with the
# change recorded in tests/coverage_matrix.md — exactly like the gauge digest history (e.g. ED-1032).
# [LC-8, 2026-07-02, Jordan-approved: "correct, retire them. those are emergent outcomes."] Updated:
# Horseshoe/RefusedFlank retired as Subunit.shape values; the 'envelop'/'cannae'/'oblique' battery
# rows now build via build_envelopment/build_refused_flank instead. A byte-exact isolation check (a
# worktree diff at 7 unaffected rows only, both before and after this change) confirmed the
# reset_positions rewrite this required (each subunit now resets to its OWN spawn position, not one
# shared shape-derived anchor for the whole unit) is exactly byte-exact-preserving for every existing
# single-subunit matchup on its own -- the digest below changes ONLY because of the 3 migrated rows'
# real, intentional behaviour change (a different army composition), not a hidden regression.
#
# [DG-3/DG-4, ED-MB-0002, 2026-07-04, ALL FOUR MODES RE-RECORDED] Two deliberate accounting-layer
# changes touch shared combat-resolution code (NOT gated behind FIELD_MOVEMENT/PER_CELL, unlike every
# prior mass-battle fix in this lane -- see the Verification section of designs/audit/
# 2026-07-04-mass-battle-cannae-gauge-audit/README.md for why this one moves all 4 digests): (1) the
# multi-front combat-pool formula (orchestration.py POOL_VARIANT="C-ii" branch) replaced with a
# bottom-up, per-cell troop-density-weighted redistribution (core/exchange.py's
# pair_pool_contribution()) instead of a flat per-pair split -- Jordan's DG-3 ruling ("Combat pool for
# a subunit is misleading. It should be based upon combat pool per cell as per troop type/quality/
# density... bottom-up... solves issues with multiple engagements"); (2) a continuous per-phase
# sibling-morale coupling (core/state.py's morale_check_phase, hierarchy/units.py's new
# Subunit.pull_morale) -- Jordan's DG-4 ruling ("Subunit morale combination of own morale and overall
# morale; more likely to wilt if other subunits losing, more likely to rally if other subunits
# winning"). Both are additive/structural, not magnitude tuning to fit a band. Full rationale,
# verification (bat.py all 4 modes, tests/valoria, gauge_mb.py re-run) in coverage_matrix.md's
# 2026-07-04 entry.
EXPECTED = {
    # [2026-07-08, ED-MB-0004, partition-invariance fix, Jordan-ruled "genuine defect -- fix it"]
    # re-recorded a final time, all 4 modes -- orchestration.py's new `_convergence_scale` renormalizes
    # >=2 of one side's atoms simultaneously, fully engaging the SAME single opposing atom (this
    # battery's 'envelop'/'cannae'/'oblique' rows: a pinning center + 2 wings all converging on one
    # Line/Arrowhead defender) back down to what ONE merged atom of their combined troops would
    # contribute -- see core/exchange.py's new `_pair_engaged_troops` + orchestration.py's
    # `_convergence_scale`/`PC_CONVERGENCE_NORM`. Shared, non-gated combat-resolution code (same as
    # every prior DG-3/DG-4/Step-4 landing in this lane), so all 4 modes move again. Verified live
    # (not just via digest motion): a direct trace confirmed `_convergence_scale` fires on the
    # majority of this battery's ticks (1446/1686 sampled calls non-empty, max simultaneous-convergence
    # group size 3) -- the mechanism genuinely engages, this isn't a no-op digest churn. Gauge re-run
    # (n=60, multi mode) showed the fix does NOT move H3-H6/C4's win/loss/draw split at all (bit-for-bit
    # identical decA/dec_n to the pre-fix baseline) even though exact per-trial hp/turn values changed
    # (confirming the digest move is real but small relative to these rows' other dominant mechanisms,
    # namely envelopment/charge shock) -- disclosed honestly, not claimed as a gauge-band fix. See
    # tests/coverage_matrix.md's 2026-07-08 entry + ED-MB-0004.
    #
    # [2026-07-08, ED-MB-0006, Jordan directive: "abandon combat pools being related to the
    # commander, and instead [derive them] solely from the subunit troop type, quality and
    # numbers"] Re-recorded a final time, all 4 modes -- the base pool term is now
    # `eff_power x eff_size x POOL_QUALITY_SCALE` (POOL_QUALITY_MODEL, default ON), replacing
    # Command entirely; see config.py's POOL_QUALITY_MODEL/POOL_QUALITY_SCALE comments and
    # core/exchange.py's subunit_combat_pool for the full rationale. Shared, non-gated code
    # (every mode moves). Full honest gauge/exponent record: tests/coverage_matrix.md's second
    # 2026-07-08 entry.
    'unit': 'd9ca7c7e8be442eae9d68c19ed248ed1a0f22f50f50ee4c8dab464c758802db4',
    # [2026-07-04, re-recorded a second time, caught by CI not local dev] 'cell' also moved after the
    # adversarial-review fixes (pair_pool_contribution's cell_troops iteration bug; the sibling-morale
    # pull reorder/snapshot fix) -- missed locally because test_byte_exact_cell_mode only hard-fails
    # inside _in_reference_env() (GITHUB_ACTIONS + Linux) and silently SKIPS elsewhere (a documented,
    # legitimate carve-out for genuine cross-platform float non-portability -- but it also means a
    # local dev sandbox can't tell "digest moved, needs re-recording" apart from "still matches" for
    # this one mode). Confirmed NOT a portability artifact: re-running bat.py directly in this same
    # sandbox reproduces CI's exact new hash. Re-verify 'cell' with a direct `bat.py --check` call
    # (not just the pytest suite) after any future orchestration.py/core.exchange/core.state change.
    #
    # [2026-07-05, Step 4 fix, same as 'unit' above] re-recorded again -- same shared, non-gated
    # combat-resolution code, so 'cell' moves too.
    # [2026-07-08, same fix as 'unit' above] re-recorded.
    # [2026-07-08, ED-MB-0006, same as 'unit' above] re-recorded.
    'cell': '88481bbd1a6748325b7aba92e434dd51a21774fcb3f82704213d4daa2f6993f6',
    # [Stage A, 2026-07-01; TOI refactor 2026-07-02; re-recorded 2026-07-02 for LC-8 + ED-1089/1091]
    # The coordinate-field path's OWN golden digests (FIELD_MOVEMENT=1 + PC_NODE_COHESION=1 -- required
    # by run_battle's own assert; since the ED-1089 default flip this is what a BARE invocation runs).
    # NOT byte-exact with the grid digests above by construction (Chebyshev->Euclidean + the
    # true-adjacency standoff halt are intended behaviour changes, not a refactor) -- this is the field
    # path's own regression anchor. Re-recorded 2026-07-02 (a deliberate, Jordan-ratified behaviour
    # change bundle, NOT a regression): (1) the LC-8 battery migration -- three rows now build
    # multi-subunit armies via build_envelopment/build_refused_flank; the prior field digests predated
    # that migration and were stale against the current battery; (2) ED-1091's frontal-only recoil
    # zone-gate (PC_RECOIL_FRONTAL, default ON) -- affects cell_field only in principle (the recoil
    # block is PER_CELL-gated) and the battery's one braced row is frontal, so the grid 'cell' digest
    # above was verified byte-identical after the gate landed. Update ONLY on an intentional field-path
    # behaviour change, same discipline as the grid digests.
    #
    # [Movement/pathing audit, ED-1096/1097, re-recorded 2026-07-02] Re-recorded again for the fix-plan
    # steps 1-7 + decision gates 2/4 landed this session: check_drift/reset_positions node-state
    # corruption fixes, weapon-derived unit_type wiring, restored lateral file-holding, the node WHEEL
    # facing-stall fix, and fix-plan step 7's waypoint primitive (Subunit._resolve_maneuver_goal/
    # _envelop_goal/_sweep_goal), which is the first change to give _node_advance real steering for the
    # 'envelop'/'sweep' instructions at all (every prior recording predates step 7 and reflects the
    # straight-line-only centroid attractor these instructions previously reduced to).
    #
    # [2026-07-02 adversarial-review correction] An earlier version of this comment claimed step 7
    # "alone" drove this digest change -- WRONG, contradicted by a direct worktree bisection across
    # every fix-plan commit (unit_field mode, FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=0):
    # pre-session baseline c79577521010...; step 1/check_drift (c58c03f) -> 7c055cedaf07...; step
    # 4/lateral-file-holding (d143403) -> d547940f9710...; step 5/WHEEL-facing-stall (b5066a4) ->
    # a89def5570bb... (unchanged through step 6); step 7/waypoint-primitive (2911f84) -> the final
    # b1963d03d205... below. FOUR separate steps (1, 4, 5, 7) each independently changed this digest,
    # not step 7 alone -- steps 1/4/5 fix real, pre-existing node-path corruption/regressions
    # (finding 1.5's check_drift bug, the v12 file-holding regression, the WHEEL lerp-degeneracy),
    # each its own deliberate, disclosed behaviour change. The one claim that DOES hold (verified
    # separately, not by this bisection): gate 4's PER_CELL default flip contributes ZERO additional
    # divergence on top of steps 1-7's, since this specific measurement pins PER_CELL='0' explicitly
    # and cannot be reached by that flip. All five changes (steps 1/4/5/7 + gate 4's non-contribution)
    # are deliberate, disclosed behaviour changes -- not a regression.
    #
    # [2026-07-05, D2 fix, mass-battle Cannae gauge follow-up audit] re-recorded again: a Fable-5
    # adversarial audit found `_envelop_goal`'s phase-1/phase-2 transition shared one threshold for
    # entry and exit, producing a permanent limit cycle (wings wheel to the rear_r line, then jitter
    # there forever, never closing to contact) -- confirmed by direct trace. Fixed with a one-shot
    # commitment latch (`Subunit._envelop_committed`) in hierarchy/units.py. This battery's own
    # Horseshoe-cavalry/envelop scenarios exercise the 'envelop' instruction on the field path, so
    # this digest moving is expected and intentional -- wings that previously never reached contact
    # now do. `unit` (grid, PER_CELL=0) confirmed BYTE-IDENTICAL for THIS fix in isolation (this fix
    # only touches the FIELD_MOVEMENT-gated node path) -- see the Step-4 correction above: 'unit'
    # moves again once the Step-4 pool-semantics fix stacks on top.
    #
    # [2026-07-05, Step 4 fix, same rationale as 'unit'/'cell' above] re-recorded again.
    # [2026-07-08, same fix as 'unit' above] re-recorded.
    # [2026-07-08, ED-MB-0006, same as 'unit' above] re-recorded.
    'unit_field': '40649feb7c634509831e4ca124a9ecbd346bd7e3485699480be01961b86c814f',
    # [2026-07-04, re-recorded a second time] cell_field alone moved again after the adversarial-
    # review fixes above (pair_pool_contribution's cell_troops iteration bug; the sibling-morale-pull
    # reorder/snapshot fix) -- unit/cell/unit_field all re-confirmed BYTE-IDENTICAL to their
    # first-round re-record, meaning the current battery/gauge doesn't happen to exercise those bugs
    # on those 3 modes, but cell_field's PER_CELL=1+FIELD_MOVEMENT=1 combination (continuous-scale
    # subunits, multi-subunit envelop/cannae/oblique rows, real morale/rout timing) does.
    # [2026-07-05, D2 fix, same as unit_field above] re-recorded again for the same envelop-goal
    # hysteresis-latch fix; 'cell' (grid, PER_CELL=1) confirmed BYTE-IDENTICAL, unaffected.
    #
    # [2026-07-05, Step 4 fix, same rationale as 'unit'/'cell'/'unit_field' above] re-recorded again.
    #
    # [2026-07-05, D3+D4 fixes, mass-battle Cannae gauge follow-up audit] re-recorded a final time --
    # 'unit'/'cell'/'unit_field' all confirmed BYTE-IDENTICAL to the Step-4 recording above (D3's
    # routed-atom pool-floor fix and D4's row-aware casualty-distribution fix don't happen to be
    # exercised differently by this battery on those 3 modes); only 'cell_field' moves, since D4's
    # `distribute_casualties` is PER_CELL-only code (percell.py) and D3's routed-atom pool fix is
    # only reachable once PER_CELL's morale/rout mechanics are live -- same PER_CELL=1+FIELD_MOVEMENT=1
    # exclusivity this mode's prior re-records have shown throughout this lane.
    #
    # [2026-07-05, D3 CORRECTION, adversarial-review finding] re-recorded again: an independent
    # adversarial reviewer found the D3 fix above was a NO-OP as first written -- `roll_pool`/
    # `_sigma_net_boost` (resolution.py) both independently re-floor their own `pool` argument to a
    # minimum of 1 internally, so zeroing `a_pool`/`b_pool` for a dead atom never reached the actual
    # dice/damage math (confirmed by the reviewer via a revert-and-diff test: byte-identical digest
    # with or without the original fix). The real fix now forces `a_net`/`b_net` to exactly 0 directly
    # for a routed/broken atom (both the SIGMA_HEAD and legacy pool-modifier branches), which correctly
    # resolves to `compute_degree`'s "Failure" -> zero damage. `unit`/`cell`/`unit_field` all
    # re-confirmed BYTE-IDENTICAL to the prior recording (the grid battery/this specific field-mode
    # battery combination don't happen to exercise a mid-battle rout with a still-live opposing pair on
    # those 3 modes); only `cell_field` moves.
    # [2026-07-08, same fix as 'unit' above] re-recorded.
    # [2026-07-08, ED-MB-0006, same as 'unit' above] re-recorded.
    'cell_field': '7b3b0a8d61429e07042dd61095bb14bae208179bf09e67f50bbd5f6546dcbed5',
}


def compute():
    """mode key: 'cell'/'unit' (grid, PER_CELL selects) or '..._field' when FIELD_MOVEMENT is on. Read
    at CALL TIME so the reported mode always matches what this process actually ran, not just PER_CELL
    -- [Stage A] before this, mode was PER_CELL-only, so a FIELD_MOVEMENT default-flip would silently
    run the field path but report/check it as plain 'unit'/'cell', comparing against the WRONG
    (grid-path) golden digest. The comparison would still fail loud (a real behaviour difference), but
    the mismatch would misleadingly read as a regression rather than "you're on the field path, check
    against unit_field/cell_field instead" -- this key naming makes that unambiguous."""
    import mass_battle.hierarchy.units as _u
    # Read the RESOLVED config value, not a second, independently-defaulted os.environ.get -- the
    # latter drifted out of sync with config.PER_CELL's own default the moment gate 4 (ED-MB-0001)
    # flipped PER_CELL's default '0'->'1': a bare invocation would have run the (now-default) 'cell'
    # path while this line's own stale '0' fallback kept reporting/checking it as 'unit', silently
    # comparing against the WRONG EXPECTED entry. Same failure shape the FIELD_MOVEMENT mode-key
    # fix above already guards against -- fixed the same way, by reading the module's own resolved
    # toggle instead of re-deriving it.
    base = 'cell' if _u.PER_CELL else 'unit'
    mode = base + '_field' if _u.FIELD_MOVEMENT else base
    h = hashlib.new('sha256')
    for label, sa, sb, ka, kb in BATTERY:
        # sa/sb: a plain shape string (single-subunit, via make_unit/ANCHOR_MAP) or an army-builder
        # callable (_envelop_army/_refused_army) for the composed Envelopment/Refused-Flank presets
        # that replaced the retired Horseshoe/RefusedFlank shapes (LC-8). resolve_battle's shape_a/
        # shape_b positional is only consulted by reset_positions as a defensive fallback now (every
        # subunit resets to its OWN spawn position first -- see reset_positions) -- 'Line' is a safe
        # placeholder for a callable side, never actually used since build_army-built subunits always
        # carry a real _spawn_position.
        a_is_fn = callable(sa); b_is_fn = callable(sb)
        if not a_is_fn and (sa, TIER) not in ANCHOR_MAP:
            continue
        if not b_is_fn and (sb, TIER) not in ANCHOR_MAP:
            continue
        for s in range(N_SEEDS):
            random.seed(s + SEED_BASE)
            ua = sa('A', 'A', **ka) if a_is_fn else make_unit(sa, 'A', 'A', **ka)
            ub = sb('B', 'B', **kb) if b_is_fn else make_unit(sb, 'B', 'B', **kb)
            shape_a = 'Line' if a_is_fn else sa
            shape_b = 'Line' if b_is_fn else sb
            r = resolve_battle(ua, ub, shape_a, shape_b, ANCHOR_MAP, kind='multi', max_battle_turns=MAX_TURNS)
            h.update((label + '#' + str(s) + ':' + trial_vector(ua, ub, r) + '\n').encode())
    return mode, h.hexdigest()


def main():
    mode, digest = compute()
    print(f"DIGEST {mode} {digest}")
    if '--check' in sys.argv:
        exp = EXPECTED.get(mode)
        if digest == exp:
            print(f"[BYTE-EXACT OK] {mode} matches baseline")
            return 0
        print(f"[BYTE-EXACT FAIL] {mode}: expected {exp}, got {digest}")
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
