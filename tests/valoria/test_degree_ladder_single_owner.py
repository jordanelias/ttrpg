"""[ED-IN-0187 sweep] One degree ladder for the whole game, and a guard that fails on a second.

WHY THIS EXISTS. Jordan ruled the degree ladder on 2026-08-14: the margin `net - ob` decides the
band, `3 or more is always overwhelming`, and meeting the obstacle without exceeding it is a
Partial. Before the ruling the census at `audit/2026-08-12-degree-vocabulary-census/` found EIGHT
importable ladders in SEVEN behavioural equivalence classes, disagreeing on up to 45.6% of the
(net, ob) domain — `faction_action` vs the mass-battle engines — while every one of them was
documented as "the standard dice-engine semantics". Renaming them would not have found that; only
evaluating them did.

⚠ AND THE CENSUS ITSELF UNDERCOUNTED, which is the more useful lesson. Two adversarial critics
independently found a NINTH live ladder the census never enrolled — `sigma_leverage.degree`, the
social-contest surface, sitting in the SAME PACKAGE as the owner. An instrument's roster is a
claim about the tree, not a measurement of it: this file's roster is therefore paired with a
source sweep (`test_no_new_hand_rolled_ladder`) so a ladder that nobody enrolled still fails
something. Six ladders are migrated; two are declared HOLDs with measured reasons; the tree does
NOT collapse to a single implementation and this file must not be read as claiming it does.

THE UNIT OF REPAIR IS THE PATTERN, NOT THE EIGHT SITES (CLAUDE.md 0.1 point 5). A ladder is four
lines of `if`, which is exactly why it kept being retyped: writing one is cheaper than finding the
owner. So this module does two different jobs, and it needs both.

  * `test_every_ladder_is_behaviourally_the_owner` evaluates each ladder over the integer AND
    quarter-step domains and fails unless they collapse to ONE class. This is what lets the canon
    mass-battle engine (`tests/sim/mass_battle/`) keep its deliberate no-`engine.*`-imports
    property: its ladder is spelled out rather than imported, and equivalence is held by
    measurement instead of by an import edge nobody has decided to add.
  * `test_no_new_hand_rolled_ladder` fails when a file starts PRODUCING two or more distinct bands
    (returning or assigning them) outside the registry below. Without it the first test only proves
    that today's ROSTER agrees, and an unenrolled ladder arrives next week -- which is exactly what
    happened here: the census missed `sigma_leverage.degree` entirely.

THE FRACTIONAL DOMAIN IS NOT OPTIONAL. `audit/2026-08-12-degree-vocabulary-census` recorded that
checking integers alone gave a WRONG answer: a continuity correction is invisible at integer nets,
which is the one domain a continuous resolver never runs on. Nets come off the continuous engine
already, so the fractional cells are where the game actually lives.

⚠ Do NOT read this file as saying obstacles are score/2 plus modifiers. Jordan RULED that, and it
is implemented NOWHERE -- every call site still passes a hand-set Ob. An earlier draft of this
paragraph asserted it as fact, which is the failure mode this module exists to guard against,
committed in the guard's own docstring.
"""
import importlib
import importlib.util
import os
import pathlib
import re
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from engine.autoload import dice_engine  # noqa: E402

# Ordinal bands, so vocabulary differences (enum / Title-Case / lower-case) cannot masquerade as
# behavioural ones. Unknown spellings raise rather than defaulting to a band.
FAIL, PARTIAL, SUCCESS, OVER = 0, 1, 2, 3
_BAND = {
    'failure': FAIL, 'Failure': FAIL, 'fail': FAIL,   # 'fail' is combat_engine_v1's spelling
    'partial': PARTIAL, 'Partial': PARTIAL,
    'success': SUCCESS, 'Success': SUCCESS,
    'overwhelming': OVER, 'Overwhelming': OVER,
}


def band(value):
    label = getattr(value, 'value', value)
    if label not in _BAND:
        raise KeyError(f'unmapped degree label {value!r}')
    return _BAND[label]


def _load(rel, name):
    path = REPO / rel
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# ── the ladders under guard ────────────────────────────────────────────────────────────────────
# Each entry yields a callable (net, ob) -> band. A module that cannot be imported is REPORTED,
# never reconstructed here: a transcribed copy would measure this file's idea of the ladder and
# agree with itself, which is the defect the guard exists to catch.
def _owner():
    return lambda net, ob: band(dice_engine.degree_from_net(net, ob))


def _threadwork_operations():
    m = importlib.import_module('systems.threadwork.sim.operations')
    return lambda net, ob: band(m._compute_degree(net, ob))


def _faction_action():
    # Ob is pre-subtracted at this module's call sites, so the same subtraction is applied to
    # bring it onto the shared (net, ob) domain.
    m = importlib.import_module('systems.factions.sim.faction_action')
    return lambda net, ob: band(m._degree(net - ob))


def _massbattle_twin():
    m = importlib.import_module('systems.mass_battle.sim.massbattle')
    return lambda net, ob: band(m.compute_degree(net, ob))


def _massbattle_canon():
    sys.path.insert(0, str(REPO / 'tests' / 'sim'))
    m = _load('tests/sim/mass_battle/resolution.py', 'mb_resolution_probe')
    return lambda net, ob: band(m.compute_degree(net, ob))


def _combat_engine():
    sys.path.insert(0, str(REPO / 'systems' / 'combat' / 'combat_engine_v1'))
    m = _load('systems/combat/combat_engine_v1/core.py', 'combat_core_probe')
    return lambda net, ob: band(m.degree(net, ob))


def _contest_surface():
    from engine.autoload import sigma_leverage
    # Pool-less form: the contest kernel's unit-test contract. The pool-aware branch is a
    # different function of (net, ob, pool) and is not on this two-argument domain at all.
    return lambda net, ob: sigma_leverage.degree(net, ob)


def _dice_model_skill():
    m = _load('skills/valoria-dice-model/valoria_dice.py', 'valoria_dice_probe')
    return lambda net, ob: band(m.classify_outcome(net, ob))


LADDERS = {
    'engine/autoload/dice_engine.py (OWNER)': _owner,
    'systems/threadwork/sim/operations.py': _threadwork_operations,
    'systems/factions/sim/faction_action.py': _faction_action,
    'systems/mass_battle/sim/massbattle.py': _massbattle_twin,
    'tests/sim/mass_battle/resolution.py': _massbattle_canon,
    'skills/valoria-dice-model/valoria_dice.py': _dice_model_skill,
}

# ── the TWO declared HOLDs ──────────────────────────────────────────────────────────────────────
# A hold is not an exemption. It is a divergence with a measured reason and an owner, and it is
# asserted to STILL DIVERGE below — so when it is resolved, this file fails and forces the update.
# Silence would let a resolved hold sit here forever looking like a live exception.
HELD = {
    'systems/combat/combat_engine_v1/core.py': (
        _combat_engine,
        "⚠ RULED 2026-08-15 — THE HOLD IS RESOLVED IN PRINCIPLE AND THE SEQUENCE IS FIXED. Jordan: "
        "'systems should not need different degree bands', and separately 'DECISIVE_OB for combat is "
        "stupid as hell and is dead because Ob should be determined by your opponent more than "
        "anything'. So this site MIGRATES. It is still held here because the ORDER is now settled and "
        "is the opposite of the obvious one: derive Ob from the defender FIRST (score/2 + that "
        "instance's modifiers), THEN the owner's ladder applies directly. Migrating the bands against "
        "the fixed Ob first is precisely the wasted work core.py's own docstring predicted. Delete "
        "this entry when the Ob derivation lands, not before. Original reason follows, still true of "
        "the fixed-Ob form: "
        "Migrating it moves the Failure edge two whole successes (at DECISIVE_OB=3: fail <0.5 -> "
        "<2.5) and breaks a ratified invariant — guandao, armour-defeat capability 0.13, goes from "
        "settling 2.5% of plate fights to 47.5% against a 40% ceiling "
        "(test_plate_participation_tracks_armour_defeat_capability, ED-PC-0038/0039). The engine's "
        "damage constants were calibrated against the old placement, and the same ruling's "
        "score/2 Ob derivation would move the bands again, so calibrating the fixed-Ob form first "
        "is wasted work. Held for Jordan — ED-IN-0187."),
    'engine/autoload/sigma_leverage.py': (
        _contest_surface,
        "⚠ RULED 2026-08-15 — MIGRATES. Jordan: 'systems should not need different degree bands. it "
        "should be consistent in application. if a system does require any modification or extension, "
        "then the wrapper needs to inject the engine in such a manner that it can be modified "
        "cleanly.' That answers the question this hold was waiting on: the unified ladder DOES "
        "override the deliberate pool-aware bar, and if the contest still needs pool-awareness it "
        "becomes an explicitly injected extension over the owner rather than a private re-banding. "
        "Not executed yet — it flips degree(3,3) from 2 to 1, which is pinned by the 151 groundup "
        "tests and _kernel_tests.py, so it is a measured change with real fallout, not a refactor. "
        "Original reason follows: "
        "The social-contest surface. Two lower boundaries contradict the ruling — net==ob returns "
        "Success where the ruling says Partial, and 0<net<ob returns Partial where it says Failure "
        "— but its TOP band is a deliberate POOL-AWARE bar (pool mean + OVERWHELM_SIGMA*sigma) "
        "chosen to hold the Overwhelming rate ~uniform across pool sizes. Migrating means ruling "
        "on whether the unified ladder overrides a contract picked on purpose, and it is pinned by "
        "the 151 groundup tests plus _kernel_tests.py's degree(3,3)==2 — the exact cell the ruling "
        "flips. Held for Jordan — ED-IN-0187."),
}


def test_the_held_site_still_diverges_and_the_hold_is_still_needed():
    """When combat is migrated or recalibrated, this fails — which is the point.

    A hold that has quietly become unnecessary is indistinguishable from a hold that is still
    load-bearing, and the tree has a documented habit of the former outliving the latter.
    """
    owner = _owner()
    for label, (loader, _reason) in HELD.items():
        fn = loader()
        diverging = [(n, o) for n, o in DOMAIN if fn(n, o) != owner(n, o)]
        assert diverging, (
            f'{label} no longer diverges from the owner. If it was migrated, move it into LADDERS '
            f'and delete its HELD entry; if it was recalibrated, re-measure the invariant named in '
            f'the hold before deciding.')

INT_DOMAIN = [(n, o) for n in range(-4, 26) for o in range(1, 21)]
FRAC_DOMAIN = [(i / 4, o) for i in range(-8, 81) for o in range(1, 11)]
# ⚠ FRAC_DOMAIN's obstacle is an INTEGER at every cell — it sweeps fractional NETS only. That was a
# real hole: the ruling's other half is "fractional obstacles" (Ob = score/2 + modifiers, so
# half-integers are the expected case), and the one axis the ruling ADDS was the one the guard did
# not cover. HALF_OB_DOMAIN closes it.
HALF_OB_DOMAIN = [(i / 4, o / 2) for i in range(-8, 81) for o in range(1, 21)]
DOMAIN = INT_DOMAIN + FRAC_DOMAIN + HALF_OB_DOMAIN


def test_every_ladder_is_behaviourally_the_owner():
    """All ladders agree with the owner cell-for-cell, over integers AND quarter steps."""
    owner = _owner()
    mismatches, checked = [], 0
    for label, loader in LADDERS.items():
        fn = loader()
        for net, ob in DOMAIN:
            checked += 1
            got, want = fn(net, ob), owner(net, ob)
            if got != want:
                mismatches.append(f'{label}: net={net} ob={ob} -> {got}, owner says {want}')

    # ⚠ `assert checked == len(LADDERS) * len(DOMAIN)` USED TO STAND HERE, described as the
    # CLAUDE.md 0.1 point 2 non-vacuity guard. It was itself vacuous: `checked` is incremented
    # unconditionally inside the very double loop whose extent defines the right-hand side, so the
    # equality is arithmetically forced and cannot fail. The failure it claimed to exclude — "an
    # import that silently yielded nothing" — is unreachable anyway, because a broken loader RAISES
    # and errors the test. Deleted rather than reworded: a guard that cannot fail is worse than no
    # guard, because it is counted as one.
    #
    # What genuinely can drift is the ROSTER (a ladder quietly dropped) and the DOMAIN (narrowed
    # until it no longer covers fractional cells). Both are real, and both are checked.
    assert len(LADDERS) >= 5, f'only {len(LADDERS)} ladder(s) enrolled — the roster shrank'
    assert len(DOMAIN) >= 1_000, 'the shared domain collapsed — the guard is not measuring'
    assert any(isinstance(n, float) and n % 1 for n, _ in DOMAIN), \
        'the domain lost its fractional NETS — the one place a continuity defect is visible'
    assert any(isinstance(o, float) and o % 1 for _, o in DOMAIN), \
        'the domain lost its fractional OBSTACLES — the axis the 2026-08-14 ruling actually adds'
    assert not mismatches, (
        f'{len(mismatches)} cell(s) diverge from the single owner '
        f'(engine.autoload.dice_engine.degree_from_net). First 10:\n  '
        + '\n  '.join(mismatches[:10]))


def test_three_band_shorthand_is_a_declared_fold_not_a_ladder():
    """`threadwork/opposing` speaks 3 bands. It must be the owner's 4 folded, nothing else."""
    m = importlib.import_module('systems.threadwork.sim.opposing')
    owner = _owner()
    checked = 0
    for net, ob in DOMAIN:
        checked += 1
        got = m._degree_label(net, ob)
        want = {OVER: 'Meets', SUCCESS: 'Meets', PARTIAL: 'Partial', FAIL: 'Failure'}[owner(net, ob)]
        assert got == want, f'opposing: net={net} ob={ob} -> {got!r}, fold of owner says {want!r}'
    assert checked == len(DOMAIN), f'domain collapsed to {checked} of {len(DOMAIN)} cells'
    assert len(DOMAIN) >= 1_000, 'the shared domain itself collapsed — the guard is not measuring'


# ── the recurrence guard ───────────────────────────────────────────────────────────────────────
# Every file allowed to contain the band vocabulary in a branching context, and why. A NEW file
# reaching for these literals fails the test until it is either routed through the owner or added
# here with a reason -- the same shape as `test_morale_write_sweep`'s `_CELL_OWNED` registry.
_FROZEN_ORACLE = (
    'tests/sim/v32-combat-balance/ is the FROZEN pre-ruling parity reference the sigma layer is '
    'validated against (engine/tests/test_sigma_leverage_parity.py). Its value is that it does NOT '
    'change: rebanding it would silently redefine the baseline every parity claim is measured '
    'against. It carries the old 2*Ob ladder ON PURPOSE and must keep carrying it.')

LADDER_OWNERS = {
    'engine/autoload/dice_engine.py': 'THE owner — the ladder itself and its label map',
}

DECLARED_ADAPTERS = {
    # — spells the ladder out instead of importing it, equivalence held by the test above —
    'tests/sim/mass_battle/resolution.py': (
        'The canon engine (J2), which deliberately takes no engine.* dependency.'),

    # — imports the owner and RELABELS its output; trips the detector only on the fold's labels —
    'systems/threadwork/sim/opposing.py': (
        "The 3-band shorthand. It DOES import and call dice_engine.degree_from_net (opposing.py:88) "
        "— an earlier draft filed it under 'spells the ladder out', which was false — and its own "
        "test above pins it as exactly the owner's four bands folded to three."),

    # — PRODUCE bands from something that is not a dice margin. Not ladders; nothing to route. —
    'engine/cross_scale/echo_transport.py': (
        'Derives a band from a scene RESULT (winner/no-winner), never from net vs ob.'),
    'engine/cross_scale/scene_dispatch.py': (
        'Assigns an echo band from a dispatch outcome, never from net vs ob.'),
    'systems/mass_battle/sim/massbattle.py': (
        'resolve_mass_battle maps ROUT STATE and surviving-size fractions to a band for '
        'faction_action. Its one real net/ob ladder, compute_degree, IS routed through the owner.'),
    'systems/combat/sim/combat.py': (
        'Fixed bands on non-roll actions (Full Guard is always Success). Its _degree IS routed.'),

    # — FROZEN parity oracles. Migrating them would destroy the thing they exist to be. —
    'tests/sim/v32-combat-balance/combat_resolution.py': _FROZEN_ORACLE,
    'tests/sim/v32-combat-balance/damage_model.py': _FROZEN_ORACLE,
    'tests/sim/v32-combat-balance/m4a_bout_state_graph.py': _FROZEN_ORACLE,
    'tests/sim/v32-combat-balance/m4b_subaction_mechanics.py': _FROZEN_ORACLE,
    'tests/sim/v32-combat-balance/r1_sigma_resolution.py': _FROZEN_ORACLE,

    # — this file, which necessarily contains every band literal in order to detect them —
    'tests/valoria/test_degree_ladder_single_owner.py': 'The detector itself.',
}
# EVERY ENTRY ABOVE IS EARNED BY A DETECTOR HIT. That is the rule, and it is the whole reason this
# registry can be trusted: an exemption granted in advance for a file with no ladder is worse than
# no entry at all, because the day that file DOES grow one the guard stays silent.
#
# ⚠ The comment that stood here said the registry was deliberately EMPTY except for one entry, and
# it survived unedited while the registry grew to twelve -- so it sat directly above a list it
# argued against. Both statements were true once: under the earlier SYNTACTIC detector these files
# genuinely did not match, and a draft that pre-listed them was correctly pruned. Rewriting the
# detector to catch band PRODUCTION made them match for real, and each was then verified by hand
# before being added. The stale comment is the point: a claim about a data structure must be
# re-read when the data structure changes, and a targeted string edit never forces that re-read.

# WHAT COUNTS AS DEFINING A LADDER. The first version of this detector required an `if` whose
# condition contained the literal word `net`/`margin`/`successes`, immediately returning a quoted
# band. Two adversarial critics measured it against the eleven ladders this very change repaired:
# IT WOULD HAVE CAUGHT FOUR. It missed the ASSIGNMENT form (`degree = 'Overwhelming'`, all three
# inline copies), `net_successes` (a `\bnet\b` word boundary does not match it), a ladder whose
# variable was named `r`, and `Degree.SUCCESS` (the alternation admitted only `[Ss]uccess`, while
# every enum spelling in the tree is ALL-CAPS). A guard weaker than its own docstring is the exact
# §0.1-point-5 failure this file was written to prevent, committed inside the fix for it.
#
# So the test is structural instead of syntactic, and deliberately loose: a file DEFINES a ladder if
# it PRODUCES two or more distinct bands — returns or assigns them. Reading a decided degree (a
# lookup table, a `degree in (...)` gate) does not produce one, which is what separates the eleven
# real ladders from the ~17 files that legitimately name bands.
# ⚠ An earlier draft of this comment added "AND compares something against an obstacle". There is NO
# such term in the code, and never was — the same docstring-stronger-than-guard defect this module
# was written to fix. Stated here rather than implemented, because adding the obstacle term would
# make the detector MISS `sigma_leverage.degree`, which returns integer bands 0-3 with no literal. False positives are handled
# by the registry, which is the right direction for a guard to fail in.
_BAND_RE = r"""['"](?:overwhelming|success|partial|failure)['"]|Degree\.(?:OVERWHELMING|SUCCESS|PARTIAL|FAILURE)"""
# A ladder PRODUCES bands; everything else merely mentions them. `return 'Success'` and
# `degree = 'Success'` produce; `if deg in ('Success', 'Overwhelming')` and `DAMAGE[deg]` consume.
# That distinction is what separates the eleven real ladders from the ~17 files that legitimately
# name bands after the migration — a detector keyed on mention alone flagged all 28.
# The `=` branch needs the lookbehind: without it, `deg == 'Overwhelming'` (a CONSUMER, and the
# commonest line in the tree) matches on the second `=` and every migrated file reads as a ladder.
_PRODUCES_BAND = re.compile(r'(?:return\s+|(?<![=!<>+])=\s*)(?:' + _BAND_RE + r')', re.IGNORECASE)

SCAN_ROOTS = ['engine', 'systems', 'skills', 'tools', 'tests']


def test_no_new_hand_rolled_ladder():
    """A new `if net ...: return 'Success'` outside the registry fails until it is routed."""
    allowed = set(LADDER_OWNERS) | set(DECLARED_ADAPTERS) | set(HELD)
    offenders, scanned = [], 0
    for root in SCAN_ROOTS:
        for path in (REPO / root).rglob('*.py'):
            rel = path.relative_to(REPO).as_posix()
            if 'deprecated/' in rel or '__pycache__' in rel:
                continue
            scanned += 1
            if rel in allowed:
                continue
            text = path.read_text(encoding='utf-8', errors='replace')
            bands = {re.sub(r'^(?:return\s+|=\s*)', '', m.group(0)).strip('\'"').lower().rsplit('.', 1)[-1]
                     for m in _PRODUCES_BAND.finditer(text)}
            if len(bands) >= 2:
                offenders.append(rel)

    assert scanned >= 100, f'sweep scanned only {scanned} files — the walk is broken, not clean'
    assert not offenders, (
        'new hand-rolled degree ladder(s) found. Route them through '
        'engine.autoload.dice_engine.degree_from_net, or add them to DECLARED_ADAPTERS with a '
        'reason:\n  ' + '\n  '.join(sorted(offenders)))
