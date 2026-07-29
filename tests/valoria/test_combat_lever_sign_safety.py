"""SIGN-SAFETY of every MULTIPLICATIVE ability lever — M5 / F5, batch E1a (ED-PC-0045).

audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md §4 (E1a).

THE DEFECT. Two lever sites in `combat_systems` composed the ability modulator as a RATIO multiplying a
SIGNED differential:

    bind_sigma :  (leverage(agg) - leverage(def)) * eff_cw(agg,'leverage')/eff_cw(def,'leverage')
    reach_sigma:  (gap*REACH_FRAC + foot_meas)   * eff_cw(def,'measure') /eff_cw(agg,'measure')

A factor > 1 AMPLIFIES a negative difference, so investing in the lever made its owner WORSE exactly
when they were behind on the differential it multiplied — the one situation the technique exists for.
`leverage()` is signed — 14 of the 53-entry WEAPONS roster are negative (rapier -0.0792 ... scimitar
-0.0041; the plan's "14 of 51" counts balance.py's roster, which omits the two half-sword forms, and
it is the same 14 weapons) — and `gap` is signed by construction, so this was not a corner case. Live for every invested build; invisible only because `equipped=[]` by default, and
invisible to `balance.py`/`armour_participation.py`, which never set `equipped` at all (plan §13.5).

RED-ON-MAIN, measured on 6a4549a (2026-07-29) — the falsifiers for every claim below:
  · combat_systems.bind_sigma   dagger + staerke_schwaeche(german) vs poleaxe : -1.05624   -> -1.19040
  · combat_systems.reach_sigma  spear aggressor vs dagger + misura(italian) defender:
                                                                   -1.374648  -> -1.5808452
  Parameterised sweep, min(probe(L) - probe(0)) over L in {0.5,1,2,4,8}, on unmodified main:
      staerke_schwaeche / bind-as-aggressor  -2.213517      misura / reach-as-defender  -2.830432
      atajo             / bind-as-aggressor  -1.850643      (all three non-monotone in level)
  The other 8 (ability x scenario) rows were already GREEN: they scale a NON-NEGATIVE own-side
  magnitude (spine, grab-hazard, a probability), which is structurally sign-safe. That asymmetry is
  the point of parameterising — the guard states the property for the whole class, not for two sites.

THE FIX. `combat_systems.lever_log_edge(own, opp) = log(own) - log(opp)`, ADDED to the channel's sigma
instead of multiplying its signed differential. In the bind this is EXACTLY the win-probability form:
`bind_dominance_p(s) = core.logistic(s)`, so adding `log(f_own/f_opp)` multiplies the owner's ODDS of
dominating the bind by exactly `f_own/f_opp`, whatever the sign of the physical differential. In the
measure channel the same shift rides the monotone sigma->outcome map, so it raises the owner's win
probability monotonically (it is not literally an odds multiplier there — the resolver shifts a roll
rather than a log-odds; stated rather than overclaimed).

WHY NOT THE ALTERNATIVES (review R-4, binding):
  · "scale each side's own contribution" — `leverage()` is SIGNED, so a factor > 1 on a negative own
    term recreates the defect. Verified on the plan's canonical pair: -0.67344 against a -0.67080 base,
    i.e. RED on this file's own guard.
  · "clamp leverage at 0 inside bind_sigma" — changes DEFAULT-build behaviour and destroys the batch's
    byte-identity safety argument.
  · a magnitude form `|d| * r**sign(d)` — sign-safe, but EXACTLY ZERO whenever the differential is
    zero, which is every mirror matchup; `leverage()` reads only the weapon, so the acceptance
    instrument (`workbench/build_levers.py abilities`, whose ability rows are all mirrors) could not
    see it at all. A fix the only instrument that can observe it reports as a no-op is an A7d-class
    no-op, not a fix.

THE VACUITY TRAP (review R-7 / ED-PC-0028). An equipped technique OUTSIDE the fighter's known
tradition is INERT, so a guard that forgets to set the tradition passes on broken code — verified:
`misura` on a default-tradition fighter moves `reach_sigma` not at all. Every scenario here sets the
teaching tradition, and `test_multiplicative_lever_probe_is_live_and_tradition_gated` asserts BOTH
that the probe moves when taught AND that it is exactly inert when untaught. A probe that silently
stops reaching its lever therefore fails loudly instead of going quietly green.

MUTATION RECORD (§13.3 — a guard that has never failed is decoration). Run 2026-07-29, each mutation
applied to the working tree, `__pycache__` purged, and the mutant asserted present before running:
  M1  reinstate the RATIO form in `bind_sigma`  -> 3 failed / 24 passed; staerke_schwaeche and atajo
      (bind-as-AGGRESSOR) plus the named bind pin, all naming `combat_systems.bind_sigma`
  M2  reinstate the RATIO form in `reach_sigma` -> 2 failed / 25 passed; misura (reach-as-DEFENDER)
      plus the named reach pin, naming `combat_systems.reach_sigma`
  M3  own-side scaling in `bind_sigma` (the R-4 forbidden form) -> 5 failed / 22 passed; it breaks
      BOTH roles for both leverage abilities, which the ratio form did not — the measurement that
      makes R-4's prohibition concrete rather than asserted
  M4  `lever_log_edge` returns 0.0 always (an INERT "fix") -> 9 failed / 18 passed; the anti-vacuity
      half fires for every leverage/measure case ("VACUOUS PROBE ... does not move")
  M5  delete the tradition gate in `ability_primitives._invested` -> 11 failed / 16 passed; the gate
      assertion fires for EVERY multiplicative ability, i.e. the R-7 trap is watched, not narrated
All five killed; none survived. Byte-identity of default builds is pinned below from the UNMODIFIED
tree and was additionally verified exhaustively in-session (53x53 bind_sigma + 53x53x4 reach_sigma =
14,045 `float.hex()` values, zero diff, plus 400 seeded whole fights); it is NOT an approx
comparison — `pytest.approx` on an exactness claim is an absent test, not a weak one.
"""
import math
import os
import sys
from collections import namedtuple

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import ability_primitives as ABIL  # noqa: E402
import combat_systems as S  # noqa: E402
import contact as CT  # noqa: E402
import tradition as TR  # noqa: E402
from combatant import Combatant, WEAPONS  # noqa: E402
from config import CFG  # noqa: E402

# Investment levels swept by the non-worsening assertion. 0.0 is the UNEQUIPPED baseline (not
# `{ability: 0.0}`, which is a different code path already pinned by test_combat_tradition_levers).
LEVELS = (0.0, 0.5, 1.0, 2.0, 4.0, 8.0)


def _eq(ability, level):
    return {} if level <= 0.0 else {ability: level}


# ── channel probes ────────────────────────────────────────────────────────────────────────────────
# Each probe returns "goodness FOR THE INVESTING OWNER" on that channel, in a configuration where the
# owner is BEHIND. Each `reference` returns the same probe for an owner mirrored onto the OPPONENT's
# build, so `probe(0) < reference()` is a computed proof that the scenario really is disadvantaged —
# a non-worsening assertion in an ADVANTAGED configuration would be vacuous.

def _bind_as_aggressor(ability, tradition, level):
    """Owner attacks the bind with a LOW lever-arm weapon (dagger, leverage -0.0132) against a HIGH
    one (poleaxe, +0.6576): the leverage differential the ability multiplies is NEGATIVE for it."""
    return S.bind_sigma(Combatant('own', weapon='dagger', tradition=tradition, equipped=_eq(ability, level)),
                        Combatant('opp', weapon='poleaxe'), CFG, TR)


def _bind_as_aggressor_ref():
    return S.bind_sigma(Combatant('m', weapon='poleaxe'), Combatant('o', weapon='poleaxe'), CFG, TR)


def _bind_as_defender(ability, tradition, level):
    """+ve bind_sigma favours the AGGRESSOR, so the owner-as-DEFENDER's goodness is its negation."""
    return -S.bind_sigma(Combatant('opp', weapon='poleaxe'),
                         Combatant('own', weapon='dagger', tradition=tradition, equipped=_eq(ability, level)),
                         CFG, TR)


def _bind_as_defender_ref():
    return -S.bind_sigma(Combatant('o', weapon='poleaxe'), Combatant('m', weapon='poleaxe'), CFG, TR)


def _spine_as_aggressor(ability, tradition, level):
    """Spine-press: the owner must actually HAVE a spine or the lever is physically absent and the
    assertion is vacuous — katana 0.85 against glaive 1.00 is behind AND live."""
    return S.bind_sigma(Combatant('own', weapon='katana', tradition=tradition, equipped=_eq(ability, level)),
                        Combatant('opp', weapon='glaive'), CFG, TR)


def _spine_as_aggressor_ref():
    return S.bind_sigma(Combatant('m', weapon='glaive'), Combatant('o', weapon='glaive'), CFG, TR)


def _spine_as_defender(ability, tradition, level):
    return -S.bind_sigma(Combatant('opp', weapon='glaive'),
                         Combatant('own', weapon='katana', tradition=tradition, equipped=_eq(ability, level)),
                         CFG, TR)


def _spine_as_defender_ref():
    return -S.bind_sigma(Combatant('o', weapon='glaive'), Combatant('m', weapon='glaive'), CFG, TR)


def _reach_sigma(aggressor, defender):
    er = {aggressor: S.reach_base(aggressor, CFG), defender: S.reach_base(defender, CFG)}
    return S.reach_sigma(aggressor, defender, er, 0.0, 0.0, CFG, TR)


def _reach_as_defender(ability, tradition, level):
    """reach_sigma is the measure-domain sigma the DEFENDER's reach imposes on the aggressor, so it IS
    the defender's goodness. A dagger defending against a spear is behind on the gap."""
    own = Combatant('own', weapon='dagger', tradition=tradition, equipped=_eq(ability, level))
    return _reach_sigma(Combatant('opp', weapon='spear'), own)


def _reach_as_defender_ref():
    return _reach_sigma(Combatant('o', weapon='spear'), Combatant('m', weapon='spear'))


def _reach_as_aggressor(ability, tradition, level):
    own = Combatant('own', weapon='dagger', tradition=tradition, equipped=_eq(ability, level))
    return -_reach_sigma(own, Combatant('opp', weapon='spear'))


def _reach_as_aggressor_ref():
    return -_reach_sigma(Combatant('m', weapon='spear'), Combatant('o', weapon='spear'))


def _grab(ability, tradition, level):
    """The owner seizes a LIVE double edge (arming, grab_hazard 1.0) bare-handed — the self-hazard the
    'edge_grab' mitigator exists to reduce."""
    return CT.grab_sigma(Combatant('own', weapon='dagger', tradition=tradition, equipped=_eq(ability, level)),
                         Combatant('opp', weapon='arming'), CFG)


def _grab_ref():
    return CT.grab_sigma(Combatant('m', weapon='arming'), Combatant('o', weapon='arming'), CFG)


class _ProbeRng:
    """Fixed-uniform stand-in: `counter_select` consumes exactly one `rng.random()` in `u < p`."""

    def __init__(self, u):
        self._u = u

    def random(self):
        return self._u


def _counter_p(defender):
    """The exact selection probability behind `counter_select`'s single draw, recovered by bisection
    (deterministic — no seeds, no sampling noise)."""
    lo, hi = 0.0, 1.0
    for _ in range(64):
        mid = (lo + hi) / 2.0
        if S.counter_select(defender, CFG, _ProbeRng(mid), TR):
            lo = mid
        else:
            hi = mid
    return lo


def _counter(ability, tradition, level):
    """An AGGRESSIVE disposition (disp 6) bleeds the in-tempo counter — the owner is behind on the
    channel, and the multiplicative lever is what buys it back."""
    return _counter_p(Combatant('own', weapon='arming', disp=6, tradition=tradition,
                                equipped=_eq(ability, level)))


def _counter_ref():
    return _counter_p(Combatant('m', weapon='arming'))


Scenario = namedtuple('Scenario', 'label site probe reference')

# THE REGISTRY. Keyed by LEVER, so a NEW multiplicative ability inherits this guard by construction:
# `test_every_multiplicative_lever_has_a_sign_safety_scenario` fails until its lever has a probe here.
# KNOWN LIMIT (adversarial gate, 2026-07-29): lever-keyed means a SECOND consumer of an already-
# covered lever passes silently — and one exists: `init_hold_decay` (combat_systems ~:1062) multiplies
# the SIGNED initiative state by an eff_cw('measure')-derived retention factor, so `misura` makes a
# fighter BEHIND on initiative keep the deficit longer. Live today, pre-existing, small (per-beat
# ~0.05 on a ±1.5-capped state through tanh); filed open in ED-PC-0045's ledger entry rather than
# widened into this batch (§0.1 #5). A probe for it belongs under 'measure' with an init-state
# scenario when that fix batch runs.
SCENARIOS = {
    'leverage': [
        Scenario('dagger binds poleaxe, owner is the AGGRESSOR', 'combat_systems.bind_sigma',
                 _bind_as_aggressor, _bind_as_aggressor_ref),
        Scenario('poleaxe binds dagger, owner is the DEFENDER', 'combat_systems.bind_sigma',
                 _bind_as_defender, _bind_as_defender_ref),
    ],
    'measure': [
        Scenario('spear out-reaches dagger, owner is the DEFENDER', 'combat_systems.reach_sigma',
                 _reach_as_defender, _reach_as_defender_ref),
        Scenario('dagger closes on spear, owner is the AGGRESSOR', 'combat_systems.reach_sigma',
                 _reach_as_aggressor, _reach_as_aggressor_ref),
    ],
    'spine_press': [
        Scenario('katana spine vs glaive spine, owner is the AGGRESSOR', 'combat_systems.bind_sigma',
                 _spine_as_aggressor, _spine_as_aggressor_ref),
        Scenario('katana spine vs glaive spine, owner is the DEFENDER', 'combat_systems.bind_sigma',
                 _spine_as_defender, _spine_as_defender_ref),
    ],
    'edge_grab': [
        Scenario('dagger seizes a live double edge', 'contact.grab_sigma', _grab, _grab_ref),
    ],
    'counter_select': [
        Scenario('aggressive disposition bleeds the in-tempo counter', 'combat_systems.counter_select',
                 _counter, _counter_ref),
    ],
}

MULTIPLICATIVE = tuple(sorted((n, a['lever'], a['tradition'])
                              for n, a in ABIL.ABILITIES.items() if a['op'] == '*'))
_CASES = [(n, lever, trad, sc)
          for n, lever, trad in MULTIPLICATIVE
          for sc in SCENARIOS.get(lever, ())]
_IDS = [f"{n}-{sc.label}" for n, _lever, _trad, sc in _CASES]


# ── the guard ─────────────────────────────────────────────────────────────────────────────────────
def test_every_multiplicative_lever_has_a_sign_safety_scenario():
    """THE INHERITANCE MECHANISM (review R-7). A new multiplicative ability on a lever with no probe
    would otherwise be silently unguarded — the exact shape of the defect being fixed. This fails
    until the new lever gets a channel-appropriate probe above."""
    assert MULTIPLICATIVE, "no multiplicative abilities found — the whole parameterisation went vacuous"
    missing = sorted({lever for _n, lever, _t in MULTIPLICATIVE} - set(SCENARIOS))
    assert not missing, (
        f"multiplicative lever(s) {missing} have NO sign-safety scenario in {__file__}. "
        f"Every '*'-op ability lever must ship a probe returning goodness-for-the-owner in a "
        f"configuration where the owner is BEHIND on that channel, plus a mirrored reference. "
        f"Without one the lever is unguarded against M5/F5 (ED-PC-0045).")
    assert len(_CASES) >= len(MULTIPLICATIVE), "every multiplicative ability must reach >=1 scenario"


@pytest.mark.parametrize('ability,lever,tradition,scenario', _CASES, ids=_IDS)
def test_multiplicative_lever_never_worsens_its_disadvantaged_owner(ability, lever, tradition, scenario):
    """THE GUARD (M5/F5). Equip the lever on the DISADVANTAGED side and assert the channel term never
    moves against its owner, at any investment level. Red on unmodified main for
    staerke_schwaeche/atajo (bind-as-aggressor) and misura (reach-as-defender)."""
    base = scenario.probe(ability, tradition, 0.0)
    ref = scenario.reference()
    assert base < ref, (
        f"scenario {scenario.label!r} is NO LONGER DISADVANTAGED for the owner "
        f"(baseline {base!r} >= mirrored reference {ref!r}). A non-worsening assertion in an "
        f"ADVANTAGED configuration cannot observe the failure it excludes — re-pick the builds.")

    vals = [scenario.probe(ability, tradition, L) for L in LEVELS]
    for level, v in zip(LEVELS[1:], vals[1:]):
        assert v >= base, (
            f"SIGN-BLIND LEVER at {scenario.site}: investing in {ability!r} (lever {lever!r}) at "
            f"level {level} makes its DISADVANTAGED owner WORSE — {v!r} < {base!r} "
            f"[{scenario.label}]. A multiplicative lever must modulate a POSITIVE quantity "
            f"(win-probability / magnitude); it must never scale a SIGNED differential. "
            f"See M5/F5, ED-PC-0045.")
    assert vals == sorted(vals), (
        f"NON-MONOTONE investment at {scenario.site} for {ability!r} (lever {lever!r}): {vals!r}. "
        f"Deeper investment must never be worth less than shallower [{scenario.label}].")


@pytest.mark.parametrize('ability,lever,tradition,scenario', _CASES, ids=_IDS)
def test_multiplicative_lever_probe_is_live_and_tradition_gated(ability, lever, tradition, scenario):
    """THE ANTI-VACUITY ASSERTION (review R-7, ED-PC-0028). Verified: `misura` equipped on a
    DEFAULT-tradition fighter moves `reach_sigma` not at all, so a guard that forgot the tradition
    would pass on broken code. Two halves, both required: the probe MOVES when the technique is
    taught, and is EXACTLY inert when it is not."""
    untaught_off = scenario.probe(ability, 'none', 0.0)
    untaught_on = scenario.probe(ability, 'none', 1.0)
    assert untaught_on == untaught_off, (
        f"{ability!r} is NOT tradition-gated at {scenario.site}: equipping it on a fighter whose "
        f"tradition does not teach it moved the probe {untaught_off!r} -> {untaught_on!r}. "
        f"ability_primitives._invested must gate ACCESS by tradition (ED-PC-0028).")
    taught_off = scenario.probe(ability, tradition, 0.0)
    taught_on = scenario.probe(ability, tradition, 1.0)
    assert taught_on != taught_off, (
        f"VACUOUS PROBE: {ability!r} (lever {lever!r}, tradition {tradition!r}) does not move "
        f"{scenario.site} at all [{scenario.label}] — the sign-safety assertion for this case cannot "
        f"observe the failure it excludes (CLAUDE.md §0.1 #2). Either the lever site stopped reading "
        f"eff_cw/ability_factor, or the probe's build lacks the physical feature the lever modulates.")


# ── the two named M5 defect pins ──────────────────────────────────────────────────────────────────
def test_m5_bind_sigma_pin_dagger_staerke_vs_poleaxe():
    """THE PLAN'S CANONICAL PAIR (§13.2a). On unmodified main this read -1.05624 -> -1.19040: the
    German Stärke-Schwäche specialist bound WORSE than the untrained twin because the bind's leverage
    differential was negative for the dagger. The UNEQUIPPED value is byte-pinned too — it must not
    move, since every eff_cw is exactly 1.0 for a default build."""
    opp = Combatant('opp', weapon='poleaxe')
    base = S.bind_sigma(Combatant('x', weapon='dagger', tradition='german'), opp, CFG, TR)
    inv = S.bind_sigma(Combatant('y', weapon='dagger', tradition='german',
                                 equipped={'staerke_schwaeche': 1.0}), opp, CFG, TR)
    assert base.hex() == '-0x1.0e65bea0ba1f5p+0', (
        f"the UNINVESTED baseline moved ({base!r}) — E1a must be byte-identical at defaults")
    assert inv > base, (
        f"M5 REGRESSION at combat_systems.bind_sigma: staerke_schwaeche made its owner worse "
        f"({inv!r} < {base!r}); on unmodified main this read -1.19040 < -1.05624 (ED-PC-0045)")
    assert inv == pytest.approx(base + math.log(ABIL.ABILITIES['staerke_schwaeche']['value']), abs=1e-12), (
        "the leverage lever must enter as log(f_own) - log(f_opp), i.e. multiply the owner's ODDS of "
        "dominating the bind by exactly the ability factor (bind_dominance_p is logistic(bind_sigma))")


def test_m5_reach_sigma_pin_misura_on_the_outreached_defender():
    """The second site. On unmodified main the out-reached defender's measure sigma read
    -1.374648 -> -1.5808452 when they invested in Misura — distance control made them worse at
    distance. The uninvested value is byte-pinned."""
    agg = Combatant('agg', weapon='spear')
    base = _reach_sigma(agg, Combatant('d', weapon='dagger', tradition='italian'))
    inv = _reach_sigma(agg, Combatant('d', weapon='dagger', tradition='italian',
                                      equipped={'misura': 1.0}))
    assert base.hex() == '-0x1.5fe8ee6b8305ep+0', (
        f"the UNINVESTED baseline moved ({base!r}) — E1a must be byte-identical at defaults")
    assert inv > base, (
        f"M5 REGRESSION at combat_systems.reach_sigma: misura made its owner worse ({inv!r} < "
        f"{base!r}); on unmodified main this read -1.5808452 < -1.374648 (ED-PC-0045)")


def test_lever_log_edge_is_the_single_owner_and_is_exactly_inert_at_defaults():
    """The composition primitive lives ONCE (CLAUDE.md §8 'every rule lives once'), and returns
    EXACTLY 0.0 — not approximately — for the default build, which is what makes `x + shift == x`
    bit-for-bit and the batch's byte-identity argument true rather than asserted."""
    assert S.lever_log_edge(1.0, 1.0) == 0.0
    plain = Combatant('p', weapon='arming')
    for channel in sorted({a['lever'] for a in ABIL.ABILITIES.values()} |
                          {'measure', 'leverage', 'tempo', 'tactile', 'balance', 'visual', 'precommit'}):
        assert TR.eff_cw(plain, channel) == 1.0, channel
        assert S.lever_log_edge(TR.eff_cw(plain, channel), TR.eff_cw(plain, channel)) == 0.0, channel
    # sign-safety of the primitive itself, over the full clamped factor range ability_factor can emit
    grid = (ABIL.ABIL_FACTOR_FLOOR, 0.4, 0.9, 1.0, 1.15, 1.2, 4.3, 43.0, ABIL.ABIL_FACTOR_CEIL)
    checked = 0
    for opp in grid:
        prev = None
        for own in grid:
            e = S.lever_log_edge(own, opp)
            assert math.isfinite(e)
            if prev is not None:
                assert e > prev, (own, opp)          # strictly increasing in the OWNER's factor
                checked += 1
            prev = e
        assert S.lever_log_edge(opp, opp) == 0.0
    assert checked == len(grid) * (len(grid) - 1), checked   # the loop asserted what it claims to


# ── byte-identity of DEFAULT builds: the batch's safety argument, pinned not asserted ─────────────
# Recorded from the UNMODIFIED tree at 6a4549a (2026-07-29) by
# scratchpad gen_pins.py. Tuple per weapon: (bind_sigma(w attacking arming),
# reach_sigma(w aggressor vs arming defender @none), the same @heavy). `float.hex()`, so this is bit
# equality — `pytest.approx` on an exactness claim is not a weak test, it is an absent one
# (CLAUDE.md §0.1 #2). These pins read ONLY the two functions E1a edits and are therefore expected to
# survive the serialized E1b/E2/E3 batches, which move damage and armour-defeat, not these terms.
# NOTE: seeded whole-fight determinism was ALSO verified byte-exact in-session (5 weapon pairs x 2
# tiers x 40 seeds, identical result vectors before and after) but is deliberately NOT committed
# here — it would impose a second golden family on E1b..E3b, which legitimately move fight outcomes.
DEFAULT_SIGMA_PINS = {
    'arming': ('0x0.0p+0', '0x0.0p+0', '0x0.0p+0'),
    'bardiche': ('0x1.53b66079bd5adp-5', '-0x1.067affeff5aafp+0', '-0x1.52af39b9c11ebp-2'),
    'bear_spear': ('-0x1.fe5e3f5077ed0p-9', '-0x1.59b96d610dd65p+0', '-0x1.be188d22646f7p-2'),
    'bec_de_corbin': ('0x1.b15d04bdd4e25p-1', '-0x1.29dfcf54afb93p-1', '-0x1.805a97e924cdfp-3'),
    'changdao': ('0x1.e671334902a87p-2', '-0x1.b47e70c681213p-1', '-0x1.199be5a95b915p-2'),
    'cinquedea': ('-0x1.f3387160956bcp-6', '0x1.14707fc4dc3d9p-1', '0x1.64b2314013ec6p-3'),
    'dagger': ('-0x1.075a31a4bdba1p-3', '0x1.fdede474893f3p-2', '0x1.48fc9363f5732p-3'),
    'dangpa': ('0x1.0f760f50d5db6p-2', '-0x1.84fbfbfeb0760p+0', '-0x1.f5ea4d69a9e2ap-2'),
    'estoc': ('0x1.466ad48a30702p-1', '-0x1.74e2fed14d832p-1', '-0x1.e124e5b33ab9cp-3'),
    'estoc_halfsword': ('0x1.46883acc84a88p+0', '-0x1.0a7154e2a0951p-2', '-0x1.57cc0a6ebeafdp-4'),
    'falchion': ('-0x1.b88e5166fae11p-5', '-0x1.0996ef7a89a46p-3', '-0x1.56b23d43463f8p-5'),
    'fauchard': ('0x1.4fb9b16715b8ap-4', '-0x1.6b21ff323c758p+0', '-0x1.d48ef6b46f0b4p-2'),
    'flamberge': ('0x1.0345711aed7d6p-1', '-0x1.7a4fbcba30c1ep-1', '-0x1.e824d27ca2027p-3'),
    'glaive': ('0x1.166ad48a30702p-1', '-0x1.ce6521088d93fp-1', '-0x1.2a51c2bb320cep-2'),
    'goedendag': ('-0x1.4cba5856026b4p-5', '-0x1.c0c080f22c7a8p-2', '-0x1.2184743924f43p-3'),
    'greatsword': ('0x1.4b11c6d1e108dp-2', '-0x1.8c7d7c5794664p-1', '-0x1.ff99a8b312105p-3'),
    'guandao': ('0x1.054de7ea5f84cp-3', '-0x1.9dd8820cb51a1p+0', '-0x1.0aff4ba51a005p-1'),
    'guisarme': ('0x1.db040a50bbda5p-1', '-0x1.b2dd39eafcf56p-1', '-0x1.188eba02f5c7ap-2'),
    'hook_sword': ('0x1.17d2c7b890d5ap-2', '0x1.91a4e5fdf63acp-2', '0x1.03201040bfe3ep-3'),
    'ji': ('0x1.ebfb95373449cp-1', '-0x1.0df55076a96c4p+0', '-0x1.5c554f0cb9940p-2'),
    'jian': ('-0x1.b952d234eb9a1p-4', '0x1.087732668496cp-6', '0x1.553ef6b5d45f8p-8'),
    'kama_yari': ('0x1.7ae685db76b3bp-3', '-0x1.3626ec94428bbp+0', '-0x1.903239857f27ep-2'),
    'katana': ('0x1.b747298a3d055p-3', '-0x1.bfdf7874a8974p-4', '-0x1.20f345748dccfp-5'),
    'longsword': ('0x1.db61bb05faebdp-3', '-0x1.28b0dbaa8b2e3p-2', '-0x1.7ed3b015dce0dp-4'),
    'longsword_halfsword': ('0x1.5b8130164840fp-1', '-0x1.05223e435ca10p-4', '-0x1.50f260db0c2a9p-6'),
    'lucerne_hammer': ('0x1.0ae0c82c541bep-1', '-0x1.29d093a06d32ap-1', '-0x1.8046f008cef70p-3'),
    'mace': ('-0x1.539c0ebedfa45p-3', '0x1.2493fe4f25d8ap-3', '0x1.7985271bcdbccp-5'),
    'main_gauche': ('0x1.0c970f7b9e062p-2', '0x1.016fff6c5c49ep-1', '0x1.4c2d6a9c560ccp-3'),
    'misericorde': ('-0x1.1702602c9081cp-3', '0x1.9ac1318e1785ap-2', '0x1.0900c521dda09p-3'),
    'naginata': ('0x1.26219652bd3c3p-1', '-0x1.c12cd0c37c6bcp-1', '-0x1.21ca552348037p-2'),
    'nandao': ('0x1.0536d655e28aap-3', '-0x1.cbe7dbff973abp-3', '-0x1.28b69e73594f3p-4'),
    'odachi': ('0x1.e3ad18d25edd0p-3', '-0x1.490d2ba665c9ap-1', '-0x1.a8951f8c624e8p-3'),
    'paired_short': ('-0x1.2b9f559b3d07ep-4', '0x1.0d694ccab3edep-1', '0x1.5ba0a52695961p-3'),
    'partisan': ('0x1.f4f2785800722p-2', '-0x1.67e13f5eb2617p+0', '-0x1.d05c72ccc522fp-2'),
    'podao': ('-0x1.4d1a9ab5f94bep-4', '-0x1.172f4f416666ap+0', '-0x1.683d0b6d294aap-2'),
    'poleaxe': ('0x1.daf4f0d844d02p-1', '-0x1.3689f25ca94e2p-1', '-0x1.90b1feeb2d0a0p-3'),
    'pulwar': ('-0x1.aaa7ded6ba8cap-5', '-0x1.7cd49a7f25517p-8', '-0x1.eb64e861fe9aap-10'),
    'ranseur': ('0x1.3b39c7a1eaa0ep-3', '-0x1.65263647a923ap+0', '-0x1.ccd6779645995p-2'),
    'rapier': ('0x1.7837b4a2339c4p-5', '-0x1.8a9db303cdeaep-2', '-0x1.fd2e946801712p-4'),
    'rondel': ('-0x1.0536501e25850p-3', '0x1.dcdefe27b8abdp-2', '0x1.33a8a3f8982cdp-3'),
    'sabre': ('-0x1.b9389b52007eap-6', '-0x1.087732668498dp-4', '-0x1.553ef6b5d4622p-6'),
    'scimitar': ('-0x1.a0f32a2ea7b36p-5', '-0x1.fe78c39057085p-4', '-0x1.49562b96edd3dp-5'),
    'shamshir': ('-0x1.1f127f5e84f08p-5', '-0x1.66fc6d1240e43p-5', '-0x1.cf3531e601267p-7'),
    'sparr_axe': ('-0x1.ca0902de00d1ep-4', '-0x1.741cee225cf71p-1', '-0x1.e025544d5f2e5p-3'),
    'spear': ('-0x1.3126e978d4fe8p-6', '-0x1.34e2cd3f387a0p+0', '-0x1.8e900093a3b64p-2'),
    'spetum': ('0x1.749807c9221d6p-2', '-0x1.5be57249405f2p+0', '-0x1.c0e5fed221830p-2'),
    'staff': ('0x1.cf06f69446739p-2', '-0x1.1545bccda63b9p-1', '-0x1.65c556b6c5fa4p-3'),
    'stiletto': ('-0x1.5cbbc2b94d941p-3', '0x1.bbd017dae8188p-2', '0x1.1e54b48d3ae68p-3'),
    'szabla': ('-0x1.eda6612839047p-5', '-0x1.7a80de61caa06p-3', '-0x1.e86437b7fd320p-5'),
    'tachi': ('0x1.b91dc35f65c13p-3', '-0x1.c529820005130p-3', '-0x1.245cd80003461p-4'),
    'tsurugi': ('-0x1.7f3cc1516e87ap-4', '0x1.17db4f4847006p-5', '0x1.691afaf1e8008p-7'),
    'voulge': ('-0x1.5b0da27ff228cp-4', '-0x1.54d84f58750f9p+0', '-0x1.b7ccc97a657f7p-2'),
    'yari': ('-0x1.4989ec7d6c3c8p-4', '-0x1.675e129591f6bp+0', '-0x1.cfb330c0fe67ap-2'),
}


def test_default_builds_are_byte_identical_at_both_lever_sites():
    """THE SAFETY ARGUMENT (plan §4 E1a: "Blast radius: zero for default builds — VERIFY that claim").
    With `equipped=[]` every `eff_cw` is exactly 1.0, so `lever_log_edge` is exactly 0.0 and both
    rewritten terms are bit-identical to the pre-fix ratio form (`x * 1.0` vs `x + 0.0`)."""
    assert set(DEFAULT_SIGMA_PINS) == set(WEAPONS), (
        "the weapon roster moved relative to the byte-identity pins — regenerate them from the "
        "PRE-CHANGE tree, never from the post-change one (a golden re-recorded to go green is not "
        "evidence)")
    checked = 0
    for weapon, (bind_hex, reach_none_hex, reach_heavy_hex) in sorted(DEFAULT_SIGMA_PINS.items()):
        agg = Combatant('a', weapon=weapon)
        light = Combatant('b', weapon='arming', armor='none')
        heavy = Combatant('b', weapon='arming', armor='heavy')
        assert S.bind_sigma(agg, light, CFG, TR).hex() == bind_hex, weapon
        assert _reach_sigma(agg, light).hex() == reach_none_hex, weapon
        assert _reach_sigma(agg, heavy).hex() == reach_heavy_hex, weapon
        checked += 3
    assert checked == 3 * len(WEAPONS), checked
