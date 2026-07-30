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
    # needs yielding=True — no 'yield' order, PC_YIELD_EMERGENT off:
    'PC_YIELD_EMERGENT', 'PC_YIELD_RALLY', 'YIELD_RALLY_MORALE_FRAC',
    'PC_YIELD_POCKET', 'YIELD_POCKET_REACH', 'D_YIELD', 'YIELD_POOL_MULT',
    # no-ops while PC_FACING_MODEL is pinned '0':
    'PC_FACING_ATTENTION', 'PC_FACING_SLEW_BASE', 'PC_FACING_FOV_GATE', 'PC_FACING_ROUT',
    # needs the flag AND an overextended state the battery never produces:
    'PC_FEIGNED_RETREAT', 'FEIGNED_RECOGNIZE_OB', 'FEIGNED_RETREAT_OB', 'OVEREXTEND_PENALTY',
    # self-gated OFF, no reserve-commit scenario in the battery:
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


def test_pins_match_source_defaults():
    defaults = _source_defaults()
    checked = 0
    mismatches = []
    for name, pinned in FIELD_PINS.items():
        if name in _NON_SOURCE_PINS:
            continue
        assert name in defaults, (
            f"pin {name} has no environ.get default in tests/sim/mass_battle — "
            f"renamed or retired? Update tools/ci_golden_modes_check.py deliberately.")
        if defaults[name] != pinned:
            mismatches.append(f"{name}: pinned {pinned!r} vs source default {defaults[name]!r}")
        checked += 1
    assert not mismatches, (
        "pin/default drift — a default flip is a golden-moving change and must "
        "update the pin list + re-record deliberately:\n  " + "\n  ".join(mismatches))
    expected = len(FIELD_PINS) - len(set(FIELD_PINS) & _NON_SOURCE_PINS)
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
    assert set(MODES) == {'unit_field', 'cell_field', 'cell_cm'}
    for mode, sel in MODES.items():
        want_field = '1' if mode.endswith('_field') else '0'
        assert sel['FIELD_MOVEMENT'] == want_field, mode
        assert sel['PC_NODE_COHESION'] == want_field, mode
        assert sel['PER_CELL'] == ('1' if mode.startswith('cell') else '0'), mode
    # the §4a mode is the ONLY one that overrides the PC_CELL_MORALE pin, and it must
    assert MODES['cell_cm']['PC_CELL_MORALE'] == '1'
    for mode in ('unit_field', 'cell_field'):
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
