"""Drift guard for the field-golden CI gate's pin vector (plan-v2 A1b, §0.1 #5).

tools/ci_golden_modes_check.py is the single owner of the golden-mode pin list.
Its values are the goldens' recorded values — which today equal the source-level
`environ.get` defaults. The hazard this guards: someone flips a default in
config.py (a golden-moving change) without deliberately updating the pin list
and re-recording; the CI gate would then silently check the new-default battle
against the old-default golden pin — or vice versa. Either way THIS test goes
red first, naming the drifted flag.

Also guards the name mapping (every pinned name is genuinely read via
os.environ somewhere under tests/sim/mass_battle — catches renames like
SIGMA_HEAD_ENABLED's env name being SIGMA_HEAD, and pins that rot when a flag
is retired).

Mutation-verified at introduction: editing PC_WHEEL's default '1'→'0' in the
source (or the pin '1'→'0' in the tool) fails test_pins_match_source_defaults;
deleting a pinned flag's environ.get read fails test_every_pin_is_read.
"""
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_MB = os.path.join(_ROOT, 'tests', 'sim', 'mass_battle')

import importlib.util

_spec = importlib.util.spec_from_file_location(
    'ci_golden_modes_check', os.path.join(_ROOT, 'tools', 'ci_golden_modes_check.py'))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

FIELD_PINS = _mod.FIELD_PINS
MODES = _mod.MODES

# pins that deliberately do NOT mirror an environ.get default:
_NON_SOURCE_PINS = {'PYTHONHASHSEED'}

# The provably battery-inert residue (critic-verified, each with the reason it cannot
# move a bat.py digest at the FIELD_PINS values). This set is load-bearing:
# test_no_unclassified_env_reads asserts every engine env read is pinned, a mode
# selector, or listed HERE — so a new env-read flag added to the engine and left
# unpinned fails that test until someone classifies it deliberately (§0.1 #5; the
# missing direction the A1b critic pass named B1).
_KNOWN_INERT = {
    # dead while POOL_QUALITY_MODEL=1 (pinned); derive_command needs charisma/cognition
    # the battery never sets:
    'COMMAND_SIGMA_ENABLED', 'COMMAND_POOL_MULT', 'CMD_CHA_WEIGHT', 'CMD_COG_WEIGHT',
    # needs an explicit order/target the battery never issues:
    'PC_VOLLEY_TARGETING',
    # [MEASURED-INERT 2026-07-30, ED-MB-0061] needs yielding=True, which the battery never orders.
    # ⚠ The previous rationale was CIRCULAR — "no 'yield' order, PC_YIELD_EMERGENT off" — i.e. the flag
    # was inert because the flag was off. Jordan's flags-ON ruling turned it ON and the rationale went
    # false while the classification was inherited unchanged. Re-established by MEASUREMENT instead:
    # cell_field at 6 seeds is digest-IDENTICAL with these five ON vs OFF
    # (71fdb844b8c8007f2d27a24f40572fa6393eff8d73c72aa58edb98f91c9ac949 both arms), so they cannot move
    # a bat.py digest at the shipped defaults. Note this is a claim about the BATTERY only — PC_YIELD_RALLY
    # is demonstrably NOT behaviourless in general (test_dg2_yield_residuals fails at the new defaults).
    'PC_YIELD_EMERGENT', 'PC_YIELD_RALLY', 'YIELD_RALLY_MORALE_FRAC',
    'PC_YIELD_POCKET', 'YIELD_POCKET_REACH', 'D_YIELD', 'YIELD_POOL_MULT',
    # no-ops while PC_FACING_MODEL is pinned '0':
    'PC_FACING_ATTENTION', 'PC_FACING_SLEW_BASE', 'PC_FACING_FOV_GATE', 'PC_FACING_ROUT',
    # [MEASURED-INERT 2026-07-30, ED-MB-0061] needs an overextended state the battery never produces;
    # same measurement as the yield family above (digest-identical ON vs OFF). Previously circular.
    'PC_FEIGNED_RETREAT', 'FEIGNED_RECOGNIZE_OB', 'FEIGNED_RETREAT_OB', 'OVEREXTEND_PENALTY',
    # [MEASURED-INERT 2026-07-30, ED-MB-0061] no reserve-commit scenario in the battery. The old
    # reason began "self-gated OFF", which was circular; same measurement as above.
    'PC_RESERVE_COMMIT', 'RESERVE_COMMIT_TURN',
    # dead behind PC_CELL_MORALE (pinned '0'):
    'CELL_BREAK_ROUT_FRAC', 'CELL_MORALE_PULL',
}

_ENV_READ = re.compile(r"environ\.(?:get|setdefault)\(\s*['\"](\w+)['\"](?:\s*,\s*['\"]([^'\"]*)['\"])?")


def _source_defaults():
    """{env_name: default_string} for every simple environ.get under the MB tree,
    excluding standalone harnesses that bat.py never imports."""
    skip = {'lanchester_signature.py', 'test_persubunit_stress.py'}
    out = {}
    for dirpath, _dirs, files in os.walk(_MB):
        for f in files:
            if not f.endswith('.py') or f in skip:
                continue
            text = open(os.path.join(dirpath, f), encoding='utf-8').read()
            for m in _ENV_READ.finditer(text):
                name, dflt = m.group(1), m.group(2)
                if dflt is not None:
                    # first definition wins; conflicting defaults are their own defect
                    out.setdefault(name, dflt)
    return out


# [ED-MB-0061, 2026-07-30] THE ONE LEGITIMATE PIN/DEFAULT DIVERGENCE, AND WHY IT IS DECLARED RATHER
# THAN FIXED. FIELD_PINS' values are "the GOLDENS' recorded values", which normally equal the source
# defaults because a default flip and a re-record ship together. Jordan's flags-ON ruling broke that
# coupling ON PURPOSE and in one direction only: every default flipped at once, while the goldens
# still record the pre-flip configuration, because re-basing the oracle BEFORE fixing the defects the
# flip exposed would bake nine of them into the definition of correct (00_lessons.md §4.2).
#
# So the pins must keep certifying what the goldens actually are, and the honest guard is not
# "pins == defaults" but "every divergence is DECLARED and the list is exactly the transition set".
# Adding a 16th flag fails; silently resolving one without updating both sides fails.
#
# ⚠ THIS SET MUST BE EMPTY AFTER THE RE-BASE. It is transition debt with a defined end, not a
# permanent exemption — that is the whole difference between this and simply deleting the guard.
# Only the TEN of the fifteen that are actually PINNED can diverge from a pin. The other five
# (PC_FEIGNED_RETREAT, PC_RESERVE_COMMIT, PC_YIELD_EMERGENT/POCKET/RALLY) live in _KNOWN_INERT, and
# that is its own problem — see test_known_inert_reasons_are_not_self_referential below.
_PENDING_REBASE = {
    'PC_CELL_DAMAGE', 'PC_CELL_MORALE', 'PC_CLOSE_RANKS', 'PC_FRACTIONAL_POOL', 'PC_FRICTION_CEV',
    'PC_INTENT_RESOLUTION', 'PC_TROOP_DENSITY_CAP', 'FIELD_CONTACT', 'PC_FACING_MODEL',
    'REFORM_CHECK_ENABLED',
}


def test_pending_rebase_set_is_exactly_the_transition():
    """The declared divergence must match reality in BOTH directions.

    Every name in _PENDING_REBASE must genuinely diverge (pin != source default) — otherwise it is a
    stale exemption hiding a pin nobody re-checked — and every actual divergence must be declared.
    This is what keeps the exemption from becoming a place to park drift."""
    defaults = _source_defaults()
    actually_diverging = {n for n, pinned in FIELD_PINS.items()
                          if n not in _NON_SOURCE_PINS and n in defaults and defaults[n] != pinned}
    stale = _PENDING_REBASE - actually_diverging
    undeclared = actually_diverging - _PENDING_REBASE
    assert not stale, (
        f"declared as pending-rebase but no longer diverging — resolve the pin AND remove it from "
        f"_PENDING_REBASE, or the exemption outlives the transition: {sorted(stale)}")
    assert not undeclared, (
        f"pin/default divergence that is NOT declared — a default was flipped without deciding the "
        f"golden question: {sorted(undeclared)}")
    assert len(_PENDING_REBASE) == 10, (
        "Jordan's 2026-07-29 ruling flipped 15 flags, but only these TEN are pinned and can therefore "
        "diverge from a pin. A different size means the transition changed shape and the re-base scope "
        "needs re-deciding, not silent editing.")


def test_pins_match_source_defaults():
    defaults = _source_defaults()
    checked = 0
    mismatches = []
    for name, pinned in FIELD_PINS.items():
        if name in _NON_SOURCE_PINS:
            continue
        if name in _PENDING_REBASE:
            continue   # [ED-MB-0061] declared divergence; see the block above and its own guard
        assert name in defaults, (
            f"pin {name} has no environ.get default in tests/sim/mass_battle — "
            f"renamed or retired? Update tools/ci_golden_modes_check.py deliberately.")
        if defaults[name] != pinned:
            mismatches.append(f"{name}: pinned {pinned!r} vs source default {defaults[name]!r}")
        checked += 1
    assert not mismatches, (
        "pin/default drift — a default flip is a golden-moving change and must "
        "update the pin list + re-record deliberately:\n  " + "\n  ".join(mismatches))
    expected = (len(FIELD_PINS) - len(set(FIELD_PINS) & _NON_SOURCE_PINS)
                - len(set(FIELD_PINS) & _PENDING_REBASE))   # [ED-MB-0061] declared divergences skipped
    assert checked == expected, f"pin sweep collapsed — {checked} checked vs {expected} expected"


def test_no_unclassified_env_reads():
    """The completeness direction (critic B1): every env read in the engine must be a
    pin, a mode selector, or an explicitly-classified inert flag. A new environ.get
    added to the engine fails here until deliberately classified."""
    defaults = _source_defaults()
    unclassified = set(defaults) - set(FIELD_PINS) - {'PER_CELL', 'FIELD_MOVEMENT',
                                                      'PC_NODE_COHESION'} - _KNOWN_INERT
    assert not unclassified, (
        f"env reads with no classification (pin it, or add to _KNOWN_INERT with the "
        f"reason it cannot move a digest): {sorted(unclassified)}")
    # and the inert list must not rot: every member still read somewhere
    ghost = {n for n in _KNOWN_INERT if n not in defaults}
    # non-literal-default reads (e.g. YIELD_POOL_MULT's str(PC_SHOCK_HOLD_BRACE)) are
    # invisible to the regex — verify those by raw-text presence instead of dropping them
    for n in sorted(ghost):
        found = False
        for dirpath, _dirs, files in os.walk(_MB):
            for f in files:
                if f.endswith('.py') and n in open(os.path.join(dirpath, f), encoding='utf-8').read():
                    found = True
                    break
            if found:
                break
        assert found, f"_KNOWN_INERT member {n} no longer appears anywhere in the engine (rot)"


def test_mode_selectors_cover_every_out_of_budget_golden_mode():
    """[ED-MB-0053 / §4a] Extended from the two field modes to the three this tool now owns.

    Deliberately an EXACT-SET assertion rather than a superset: this tool is the single owner of
    "golden modes checked outside the tests/valoria budget", so a mode appearing or vanishing must
    be a deliberate edit, not silent drift. Each selector is also checked against what its mode NAME
    claims, because a selector disagreeing with its key is the ED-1089 shape — a run checked against
    the wrong golden.
    """
    assert set(MODES) == {'unit_field_mor0', 'cell_field_mor0', 'cell_legacy_mor1'}
    # ED-MB-0062: keys are now absolute — <geometry>_<movement>_<morale>, every axis present
    # with its value — so the selector check reads the axis out of the key rather than guessing
    # from a suffix that only appeared when a flag was on.
    for mode, sel in MODES.items():
        geometry, movement, morale = mode.split('_')
        want_field = '1' if movement == 'field' else '0'
        assert sel['FIELD_MOVEMENT'] == want_field, mode
        assert sel['PC_NODE_COHESION'] == want_field, mode
        assert sel['PER_CELL'] == ('1' if geometry == 'cell' else '0'), mode
        # A mode naming mor1 must actually pin the flag on, and vice versa — a key that
        # disagrees with its own selector is the ED-1089 shape this file exists to catch.
        if morale == 'mor1':
            assert sel.get('PC_CELL_MORALE') == '1', mode
    # the §4a mode is the ONLY one that overrides the PC_CELL_MORALE pin, and it must
    assert MODES['cell_legacy_mor1']['PC_CELL_MORALE'] == '1'
    for mode in ('unit_field_mor0', 'cell_field_mor0'):
        assert 'PC_CELL_MORALE' not in MODES[mode], (
            f"{mode} must inherit the FIELD_PINS PC_CELL_MORALE='0'; overriding it here would "
            f"silently re-target its golden")


def test_every_pin_is_read():
    defaults = _source_defaults()
    unread = [n for n in FIELD_PINS
              if n not in _NON_SOURCE_PINS and n not in defaults]
    assert not unread, f"pins never read by the engine (rot): {unread}"


def test_grid_pin_dict_consistency():
    """The six non-selector _PINNED_OFF members must agree with FIELD_PINS —
    two pin dicts disagreeing about a shared flag is the two-regimes hazard."""
    sys.path.insert(0, os.path.join(_ROOT, 'tests', 'valoria'))
    from test_mass_battle_byte_exact import _PINNED_OFF
    shared = set(_PINNED_OFF) & set(FIELD_PINS)
    diffs = {k: (_PINNED_OFF[k], FIELD_PINS[k]) for k in shared
             if _PINNED_OFF[k] != FIELD_PINS[k]}
    # FIELD_MOVEMENT/PC_NODE_COHESION legitimately differ (mode selectors, and
    # they live in MODES here, not FIELD_PINS) — anything else must match.
    assert not diffs, f"grid vs field pin dicts disagree on shared flags: {diffs}"
    assert len(shared) >= 5, f"expected ≥5 shared pins, got {sorted(shared)}"


def test_known_inert_reasons_are_not_self_referential():
    """[ED-MB-0061] A flag may not be its own inertness rationale, and five of them were.

    `_KNOWN_INERT` justified the yield/retreat/reserve family with reasons like "needs yielding=True —
    no 'yield' order, PC_YIELD_EMERGENT off" and "self-gated OFF". Those are CIRCULAR: the flag is
    inert because the flag is off. Jordan's flags-ON ruling turned all five ON, every rationale went
    false, and the classification was inherited unchanged — which is how a stale exemption survives a
    policy change invisibly.

    RESOLVED BY MEASUREMENT, not by assertion: cell_field at 6 seeds is digest-identical with the five
    ON vs OFF, so they genuinely cannot move a bat.py digest at the shipped defaults. (That is a claim
    about the BATTERY only; PC_YIELD_RALLY is not behaviourless in general — test_dg2_yield_residuals
    fails at the new defaults.)

    This guard now holds the thing that can actually rot: the MEASURED-INERT marker. A flag defaulting
    ON may sit in _KNOWN_INERT only while a measurement is recorded beside it. Delete the marker, or
    add a sixth ON-by-default flag on a hand-waved reason, and this fails."""
    src = open(os.path.abspath(__file__), encoding='utf-8').read()
    defaults = _source_defaults()
    # Scope: the flags whose inertness reason was WRITTEN ASSUMING THEY WERE OFF and which Jordan's
    # 2026-07-29 ruling then turned ON. Flags that were always ON (COMMAND_SIGMA_ENABLED,
    # CMD_COG_WEIGHT, PC_VOLLEY_TARGETING) are deliberately OUT of scope: their reasons cite ANOTHER
    # pinned flag or absent battery data, never their own state, so they were never circular and the
    # flip did not invalidate them. An earlier draft of this guard demanded provenance from them too
    # and was over-broad — a guard that fires on correct code teaches people to silence guards.
    _FLIPPED_BY_THE_RULING = {'PC_FEIGNED_RETREAT', 'PC_RESERVE_COMMIT',
                              'PC_YIELD_EMERGENT', 'PC_YIELD_POCKET', 'PC_YIELD_RALLY'}
    on_and_inert = {n for n in _KNOWN_INERT & _FLIPPED_BY_THE_RULING if defaults.get(n) == '1'}
    assert on_and_inert, (
        "scope collapsed — none of the ruling-flipped flags is both ON and claimed inert, so this "
        "guard is now vacuous (§0.1 point 2). Re-derive the scope set against _KNOWN_INERT.")
    # every ON-by-default flag claimed inert must be covered by a MEASURED-INERT block
    marker = 'MEASURED-INERT'
    assert marker in src, "the MEASURED-INERT provenance for the ON-by-default inert flags is gone"
    unmarked = []
    for n in sorted(on_and_inert):
        i = src.index(f"'{n}'")
        # the nearest preceding comment block must carry the marker
        if marker not in src[max(0, i - 1400):i]:
            unmarked.append(n)
    assert not unmarked, (
        f"flags default ON and are claimed battery-inert with no MEASURED-INERT provenance above them: "
        f"{unmarked}. An inertness reason may not be the flag's own OFF-ness (that is circular, and it "
        f"is what let this classification survive the flags-ON ruling unexamined). Measure digest "
        f"motion ON vs OFF and record it, or pin the flag.")
