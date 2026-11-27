"""B15.09 (`18_DET`): the riposte replaces the post-hoc upset flip -- no matchup is certain, and it is a blow the trackers record.

At the felling that decides a round, before the trackers are final, ONE keyed draw (a sub-key of the fight's own `Draw`,
`H2(rng.key, "upset:<scene>:<round>")`) turns the blow with probability `CFG['UPSET_FLOOR']`: the blow is not applied, so the
would-be-felled fighter's tracker stays as it stood before it; he lands the damage the blow carried back through the one damage site
(`wound` source `finalblow_riposte`), the event `finalblow_riposte(round, by)` is emitted and the fight goes on. The `result` integer is
whatever the continued fight ends with.

  (1) a riposte event leaves the would-be-felled fighter below Health though the blow would have felled him, the counter lands through
      `_wound`, and the result names a fighter the trackers have down;
  (2) at `UPSET_FLOOR` 0 there are no ripostes in 1,000 fights, and the draw takes no position of the fight's stream: a fight with
      no riposte is the floor-0 fight, event for event;
  (3) at the season, the light fighter against the heavy fells or survives in some fights, and the fold's `Event.ending` shows it.
"""
from engine.dice_engine import draw
from modules.combat import combatant as C
from modules.combat import wrapper
from modules.combat.config import CFG

KEY = "finalblow_riposte"
_HIGH = dict(CFG, UPSET_FLOOR=0.5)   # a floor high enough that 200 fights show the mechanism; the shipped one is read in (2) and (3)


def _fight(seed, cfg, pair=('arming', 'arming')):
    """One lethal fight on `seed`. Returns (result, trace, A, B, rng); each event also carries `_cum`, both trackers' damage as it stood
    when the event was emitted."""
    A, B = C.Combatant('A', weapon=pair[0]), C.Combatant('B', weapon=pair[1])
    trace = []
    rng = draw.seeded(draw.H2(KEY, seed))
    result = wrapper.fight(A, B, cfg, rng, trace=lambda e: trace.append(dict(e, _cum={'A': A.wt.cumulative_damage, 'B': B.wt.cumulative_damage})))
    return result, trace, A, B, rng


def _round_of(trace, i):
    return sum(1 for e in trace[:i + 1] if e['kind'] == 'round_start')


def test_finalblow_riposte_event_changes_the_tracker():
    """Each riposte leaves its by-party on the tracker he had, below Health though the damage the counter carries (the blow's) would have
    felled him, and is answered by a `wound` of source `finalblow_riposte` on the other fighter; some are followed by more fight. The
    fight's result is the continued fight's own: it names a fighter the trackers have down, and the `wound` events still sum to the tracker."""
    checked = continued = 0
    for seed in range(200):
        result, trace, A, B, _ = _fight(seed, _HIGH)
        for i, e in enumerate(trace):
            if e['kind'] != 'finalblow_riposte':
                continue
            counter, by = trace[i + 1], {'A': A, 'B': B}[e['by']]
            assert counter['kind'] == 'wound' and counter['source'] == 'finalblow_riposte', (seed, counter)
            assert (counter['by'], counter['victim']) == (e['by'], 'B' if e['by'] == 'A' else 'A'), (seed, counter)
            assert e['_cum'][e['by']] + counter['damage'] >= by.wt.health_full, (seed, e, counter)   # the blow turned would have felled him
            assert e['_cum'][e['by']] < by.wt.health_full, (seed, e)                                 # and he is not felled
            assert e['_cum'] == trace[i - 1]['_cum'], (seed, e)                                       # the turned blow moved no tracker
            assert e['round'] == _round_of(trace, i), (seed, e)
            continued += any(x['kind'] in ('wound', 'round_start') for x in trace[i + 2:])
            checked += 1
        yielded = next((e['by'] for e in trace if e['kind'] == 'yield'), None)   # a failed yield roll (B15.10) ends the scene with the yielder standing
        if yielded is None:
            assert result != 1 or (B.felled and not A.felled), (seed, result)
            assert result != -1 or (A.felled and not B.felled), (seed, result)
        else:
            assert result == (-1 if yielded == 'A' else 1) and not (A.felled or B.felled), (seed, result, yielded)
        for c in (A, B):
            assert sum(e['damage'] for e in trace if e['kind'] == 'wound' and e['victim'] == c.label) == c.wt.cumulative_damage, seed
    assert checked >= 50, checked
    assert continued >= 1, "no riposte was followed by more fight: it ended the fight by fiat"


def test_upset_floor_zero_gives_zero_of_1000_and_the_draw_takes_no_stream_position():
    """`UPSET_FLOOR` 0: no riposte in 1,000 fights. At the shipped floor a fight with no riposte is the floor-0 fight event for event and
    draw for draw, and one with a riposte is the floor-0 fight up to it: the draw is keyed, so it consumes nothing of the stream."""
    zero = dict(CFG, UPSET_FLOOR=0)
    ripostes = 0
    for seed in range(1000):
        _, trace, _, _, _ = _fight(seed, zero)
        ripostes += sum(e['kind'] == 'finalblow_riposte' for e in trace)
    assert ripostes == 0, ripostes
    whole = prefix = 0
    for seed in range(300):
        r0, t0, _, _, g0 = _fight(seed, zero)
        r1, t1, _, _, g1 = _fight(seed, CFG)
        i = next((j for j, e in enumerate(t1) if e['kind'] == 'finalblow_riposte'), None)
        if i is None:
            assert (r1, t1, g1.n) == (r0, t0, g0.n), seed
            whole += 1
        else:
            assert t1[:i] == t0[:i], seed            # up to and including the felling blow, the floor-0 fight
            prefix += 1
    assert whole >= 200 and prefix >= 1, (whole, prefix)


def test_light_fells_or_survives_heavy_in_some_season_fights(monkeypatch):
    """The E5 probe at the season: a light-armoured actor against a plated subject, 1,000 seeded scenes through the module entry and the
    fold. The actor is not felled (he fells the plated man or the scene stands undecided) in a share above 0, a riposte at his own
    felling is in some of the scenes' traces, and `Event.ending` names him `prevailed` in some -- the fold's Events show it."""
    from engine.season.data.matrix import Step, WriteClass
    from engine.season.harness import probes as P
    from engine.season.loop.driver import SeasonDriver, mint_token
    from engine.season.queries import world_q
    from engine.season.seam import Resolution, degree_of
    from engine.season.seam.wrappers import combat
    from engine.season.state.carriers import Act, Rung, Tenure

    actor, subject = "p_low", "p_mid"
    monkeypatch.setattr(world_q, "ARMS_KINDS", {"t_plate": ("armor", "heavy", 3)})
    SeasonDriver(P.tiny_world())     # the registrar fills the combat module entry at driver construction
    not_felled = prevailed = riposted = 0
    for i in range(1000):
        w = P.tiny_world()
        w.rungs["Arsenal"] = Rung("Arsenal", "hearth", stores={"t_plate": 1})
        w.add_tenure(Tenure("t_hold_arsenal", subject, "Arsenal", "hold", since=0))
        d = SeasonDriver(w)
        w.step, w.frozen = Step.RESOLVE, False
        raw = combat.resolve(w, [actor, subject], [f"riposte{i}"], combat._PRIZE, verb="fight")
        assert raw["status"] == "RESOLVED", raw
        res = Resolution(degree_of(raw, subject, w.fixtures), raw)
        out = d._fold(w, mint_token(w, WriteClass.ACTS), Act(id=f"a{i}", actor=actor, verb="fight", payload={"subject": subject}), res)
        ending = {dict(e.ending)[actor] for e in out if e.ending}
        assert len(ending) <= 1, ending
        not_felled += bool(ending) and ending != {"felled"}
        prevailed += ending == {"prevailed"}
        riposted += any(e["kind"] == "finalblow_riposte" and e["by"] == actor for e in raw["trace"])
    assert riposted >= 1, "no scene shows the actor's felling turned"
    assert not_felled > 0 and prevailed > 0, (not_felled, prevailed)
