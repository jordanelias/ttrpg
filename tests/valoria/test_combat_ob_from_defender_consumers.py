"""PC-03 (ED-PC-0058 critique): the three readers of the per-defender Ob that ED-PC-0058 left behind.

`core.resolve` bands a roll at `core.ob_from_defender(defender, cfg)` (`opposed_ob(score, rate)`, rate `MU_PER_DIE` since B15.03, control 0.5; History / 2 until CR-85) on the owner ladder
(`engine.dice_engine.dice_engine.degree_from_net`, migrated at PC-02). Three things downstream of that
change kept reading the retired fixed `core.DECISIVE_OB = 3`:

 1. `workbench/probabilities.py` banded every displayed distribution at `DECISIVE_OB` on the pre-ruling
    ladder. Its two trace inputs (the wrapper's 'roll' / 'stophit' events) carried no `ob`, so it could
    not do otherwise. Falsifier: the workbench's band probabilities for a defender whose skill score (History before CR-85) is NOT
    the default, against `core.resolve`'s observed band frequencies over N seeds. On the pre-PC-03 tree
    they differ far beyond sampling noise; after it they agree.
 2. `core.strike`'s overwhelming-hit quality measured its severity tail `z` from `net - 2*DECISIVE_OB`,
    i.e. from a fixed net of 6, while the band it qualifies starts at the owner's bar for THIS defender's
    Ob. So q sat clamped at the tail floor for every overwhelming net between the bar and 6, and the
    tail's start moved with nothing the ladder reads. The workplan's "likely fix" `2*ob` is the PRE-ruling ladder's bar (`net >= 2*Ob`),
    which the 2026-08-14 ruling RULED OUT (`degree_from_net`'s docstring); it would start the tail
    below the bar for ob < 3 and clamp again above it for ob > 3. The fix reads the bar off the owner.
 3. Observation (PC-03), RULED by CR-85's build (ED-IN-0330): History reached the roll through two channels, the Ob
    and the net sigma, and PC-03 held that as a strict xfail. CR-85 renamed the input `faculty` and deleted its five
    sigma reads, so `test_faculty_enters_the_roll_through_exactly_one_channel` is now a plain passing assertion.
    [ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays] (the CR-85 design is
    UNRATIFIED, ED-IN-0351).
"""
import math
from engine.dice_engine import draw

import pytest

from modules.combat import combatant as C          # noqa: E402
from modules.combat import combat_systems as S     # noqa: E402
from modules.combat import core                    # noqa: E402
from modules.combat import tradition as TR         # noqa: E402
from modules.combat import wrapper                 # noqa: E402
from modules.combat.config import CFG         # noqa: E402
from engine.dice_engine import dice_engine as DE          # noqa: E402
from engine.dice_engine import sigma_leverage as SL       # noqa: E402

BANDS = ('fail', 'partial', 'success', 'overwhelming')
DEFAULT_SCORE = C.Combatant('probe').score


# ── finding 1: the workbench's distributions against the resolver's frequencies ──────────────────

def test_trace_events_carry_the_ob_their_roll_was_banded_at():
    """Every 'roll' and 'stophit' event names the Ob the roll was banded at, and it is the STRUCK party's
    `ob_from_defender` — the input finding 1's distribution needs and could not get before PC-03."""
    rolls = stophits = 0
    # spear vs dagger supplies the stop-hits (it rarely closes); longsword vs arming the exchanges
    for weapon_a, weapon_b in (('spear', 'dagger'), ('longsword', 'arming')):
        for seed in range(20):
            events = []
            A = C.Combatant('A', weapon=weapon_a, score=5)
            B = C.Combatant('B', weapon=weapon_b, score=2)
            wrapper._TRACE = events.append
            try:
                wrapper.fight(A, B, cfg=None, rng=draw.seeded(draw.H2("test_combat_ob_from_defender_consumers", seed)))
            finally:
                wrapper._TRACE = None
            r, s = _check_events(events, {'A': A, 'B': B})
            rolls += r
            stophits += s
    assert rolls >= 50 and stophits >= 1, (rolls, stophits)


def _check_events(events, who):
    rolls = stophits = 0
    for ev in events:
        if ev['kind'] == 'roll':
            struck = who['B' if ev['aggressor'] == 'A' else 'A']
            rolls += 1
        elif ev['kind'] == 'stophit':
            struck = who[ev['shorter']]
            stophits += 1
        else:
            continue
        assert 'ob' in ev, f"{ev['kind']} event carries no ob: {ev}"
        assert ev['ob'] == core.ob_from_defender(struck, CFG), ev
    return rolls, stophits


# ── finding 2: the overwhelming-hit severity tail starts at the owner's bar ───────────────────────

def _owner_overwhelming_bar(ob):
    """The smallest float the OWNER ladder reads as Overwhelming at `ob` — a test-local bisection, kept
    independent of core's own helper so it can check that helper rather than restate it."""
    lo, hi = ob - 64.0, ob + 64.0
    while True:
        mid = (lo + hi) / 2
        if mid <= lo or mid >= hi:
            return hi
        if DE.degree_from_net(mid, ob) is DE.Degree.OVERWHELMING:
            hi = mid
        else:
            lo = mid


def _quality_at(net, pool, defender, monkeypatch):
    seen = {}
    real = core.damage

    def spy(*a, **kw):
        seen['q'] = kw.get('q')
        return real(*a, **kw)
    monkeypatch.setattr(core, 'damage', spy)
    core.strike(C.Combatant('A', weapon='longsword'), defender, 'overwhelming', CFG, net=net, pool=pool)
    monkeypatch.setattr(core, 'damage', real)
    return seen['q']


@pytest.mark.parametrize('score', [2, 3, 5, 6, 8])
def test_overwhelming_quality_tail_is_measured_from_the_owner_bar(score, monkeypatch):
    """At the bar, q is the tail floor (`QUAL['overwhelming']`); past it, z is exactly the distance past the
    bar in sigma_n units. On the pre-PC-03 tree the tail started at net 6 for every defender, so at every
    faculty but 6 the first assertion past the bar fails (or, for faculty 8, the floor is not at the bar)."""
    defender = C.Combatant('D', score=score)
    ob = core.ob_from_defender(defender, CFG)
    pool = core.resolution_pool(DEFAULT_SCORE)
    bar = _owner_overwhelming_bar(ob)
    assert DE.degree_from_net(bar, ob) is DE.Degree.OVERWHELMING
    assert DE.degree_from_net(math.nextafter(bar, -math.inf), ob) is DE.Degree.SUCCESS
    assert _quality_at(bar, pool, defender, monkeypatch) == core.QUAL['overwhelming']
    for delta in (0.25, 1.0, 2.5):
        z = ((bar + delta) - bar) / SL.sigma_n(pool)
        want = 1.5 + (core.OW_MAX - 1.5) * math.tanh(z / core.OW_Z)
        assert _quality_at(bar + delta, pool, defender, monkeypatch) == want, (score, delta)


def test_band_floor_reads_the_owner_edges():
    """`core.band_floor` is the one place combat reads a band EDGE (the workbench's thresholds and strike's
    tail start). Each edge is the exact float where the owner ladder changes band."""
    checked = 0
    for ob in (0.5, 1.0, 1.5, 2.5, 3.0, 4.25):
        for band in BANDS[1:]:
            edge = core.band_floor(band, ob)
            below = core.degree(math.nextafter(edge, -math.inf), ob)
            assert BANDS.index(core.degree(edge, ob)) >= BANDS.index(band) > BANDS.index(below), (ob, band, edge)
            checked += 1
        assert core.band_floor('overwhelming', ob) == _owner_overwhelming_bar(ob)
    assert checked == 18


# ── finding 3: one channel (PC-03's observation, ruled by CR-85) ───────────────────────────────────

def _defender_side_sigma(aggressor, defender, mode):
    """The net-sigma terms of one exchange that once read the defender's History, assembled through the same
    `combat_systems` owners the wrapper sequences (`wrapper.engagement`, the net-sigma assembly): the
    initiative emphasis (into attack_sigma) and the defence sigma for `mode` (mode_sigma -> defence_sigma).
    Fatigue 0, read won, commit 3."""
    init = S.init_emphasis_sigma(aggressor, defender, CFG, TR)
    msig = S.mode_sigma(mode, aggressor, defender, 3.0, True, 0.0, CFG)
    dsig = S.defence_sigma(defender, msig, 0.0, 0.0, CFG)
    return init - dsig


def test_faculty_enters_the_roll_through_exactly_one_channel():
    """PC-03's strict xfail, converted by CR-85's build (ED-IN-0330): the defender's faculty reaches the main roll
    through the Ob ONLY. Before CR-85, History +2 also moved the net sigma (`mode_sigma`'s `tech` for parry/wind,
    `reading()`'s READ_HISTORY_K for all three modes, `init_emphasis_sigma`'s INIT_HISTORY_K); this assertion was red
    on that tree. The other rolls that read History -- the bind and the counter -- read none of it now either."""
    aggressor = C.Combatant('A')
    lo, hi = C.Combatant('D3', score=3), C.Combatant('D5', score=5)
    for c in (aggressor, lo, hi):
        wrapper._init_live(c, CFG)
    channels = {'ob': core.ob_from_defender(hi, CFG) - core.ob_from_defender(lo, CFG)}
    for mode in ('parry', 'dodge', 'wind'):
        channels[f'net_sigma[{mode}]'] = (_defender_side_sigma(aggressor, hi, mode)
                                          - _defender_side_sigma(aggressor, lo, mode))
    assert len(channels) == 4
    assert channels['ob'] == DE.MU_PER_DIE * 5 - DE.MU_PER_DIE * 3   # two points of skill score at the rate the fight opposes at (A-71)
    # each mode is a separate exchange; the claim is per exchange: Ob plus that mode's sigma
    for mode in ('parry', 'dodge', 'wind'):
        live = [k for k in ('ob', f'net_sigma[{mode}]') if abs(channels[k]) > 1e-12]
        assert live == ['ob'], f'score +2 moves {live}: {channels}'
    assert S.bind_sigma(aggressor, hi, CFG, TR) == S.bind_sigma(aggressor, lo, CFG, TR)
    assert S.counter_success_prob(hi, CFG, TR) == S.counter_success_prob(lo, CFG, TR)


def test_set_attr_score_7_reads_pool_13_ob_mu_per_die_x_7_and_no_sigma_moves():
    """PC-14's exit, re-based by CR-85 and re-pinned at B15.03 (A-71): a skill score of 7 reads pool 13 and Ob `MU_PER_DIE x 7`
    (the rate the fight opposes at; not typed as 2.8, the product is 2.8000000000000003), and no sigma term moves."""
    aggressor, d = C.Combatant('A'), C.Combatant('D')
    for c in (aggressor, d):
        wrapper._init_live(c, CFG)
    before = {m: _defender_side_sigma(aggressor, d, m) for m in ('parry', 'dodge', 'wind')}
    d.score = 7
    assert (core.resolution_pool(d.score), core.ob_from_defender(d, CFG)) == (13, DE.MU_PER_DIE * 7)
    assert {m: _defender_side_sigma(aggressor, d, m) for m in ('parry', 'dodge', 'wind')} == before


# ── B05.58 (29-2): the fight's Ob is the owner's `opposed_ob` at the cfg's rate ────────────────────

def test_the_fight_obstacle_is_opposed_ob_at_the_cfg_rate():
    """A fight run with `cfg=dict(CFG, OPPOSITION_RATE=0.3)` and skill scores 2 and 3: every `roll` event's `ob` is
    `0.3 x` the struck party's skill score (`sigma_leverage.opposed_ob`, A-71), not the module's own rate (`MU_PER_DIE`, 0.4 since B15.03:
    a planted rate equal to it could not show the override read)."""
    checked = 0
    for seed in range(8):
        events = []
        A, B = C.Combatant('A', score=2), C.Combatant('B', score=3)
        wrapper._TRACE = events.append
        try:
            wrapper.fight(A, B, cfg=dict(CFG, OPPOSITION_RATE=0.3), rng=draw.seeded(draw.H2("test_combat_ob_from_defender_consumers", seed)))
        finally:
            wrapper._TRACE = None
        for ev in events:
            if ev['kind'] != 'roll':
                continue
            struck = B if ev['aggressor'] == 'A' else A
            assert ev['ob'] == SL.opposed_ob(struck.score, 0.3) == 0.3 * struck.score != SL.opposed_ob(struck.score, DE.MU_PER_DIE), ev
            checked += 1
    assert checked >= 1, checked


# ── B15.02 (IS-PC-05): the combatant's skill score is the skill table's, never an attribute ────────

def test_the_combat_pool_reads_the_skill_table():
    """A planted change to one person's skill score (`PersonalCombatInput.scores`, the skill table's number) moves his fight pool, and the
    Ob his opponent is struck at; a planted change to an attribute alone does not move the pool's base (A-7)."""
    from engine.season.queries.inputs import PersonalCombatInput
    from modules.combat import fight as entry

    def read(scores, attributes=()):
        """A's `roll` pools and the Ob of B's `roll`s over six seeds of one fixed record."""
        a_pools, b_obs = set(), set()
        for seed in range(6):
            inp = PersonalCombatInput(claimants=('A', 'B'), ends=(4, 4), wound_quantities=('wounds',), scores=scores, attributes=attributes)
            out = entry.fight(inp, draw.seeded(draw.H2("test_combat_ob_from_defender_consumers.skill_table", seed)))
            for ev in out.trace:
                if ev['kind'] == 'roll' and ev['aggressor'] == 'A':    # A strikes B: A's pool, B's Ob
                    a_pools.add(ev['pool'])
                    b_obs.add(ev['ob'])
        return a_pools, b_obs

    base_pools, base_obs = read((5, 3))
    moved_pools, _ = read((7, 3))
    attr_pools, _ = read((5, 3), attributes=({'attr.body.strength': 7, 'attr.body.agility': 7}, {}))
    assert base_pools == {core.resolution_pool(5)} and moved_pools == {core.resolution_pool(7)}, (base_pools, moved_pools)
    assert attr_pools == base_pools, (attr_pools, base_pools)
    assert base_obs == {SL.opposed_ob(3, core.OPPOSITION_RATE)}, base_obs
    _, moved_obs = read((5, 6))
    assert moved_obs == {SL.opposed_ob(6, core.OPPOSITION_RATE)}, moved_obs
