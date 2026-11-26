"""B15.10 (`PC_A`, A-24): the yield is a roll -- whether a wounded fighter gives up is his, and is drawn.

At the end of any round in which a wound gate was crossed on a standing party, that party makes one yield roll to fight on
(`wrapper._yield_roll`): the one pool rule on his skill score, his Spirit as `minor` levels from the scale's mid-point, his wounds as a
level against him and the host's `decisiveness` as a σ, against `CFG['YIELD_OB'][terms]`. Failure: he yields; Partial: he is shaken and
fights on; Success: he fights on; Overwhelming: he rallies. The draw is a sub-key of the fight's own `Draw`,
`H2(rng.key, "yield:<scene>:<round>:<party>")`.

  (1) under `yield` and `blood` terms fighters across the line sometimes fight on, and some yield above the `yield` line;
  (2) under `death` terms a scene sometimes ends with both parties alive, the yield event's `accepted` is `None`, and fellings stay;
  (3) a Spirit 7 fighter yields less often than a Spirit 1 fighter (shares outside each other's Wilson interval at n 1,000);
  (4) the roll is keyed by the round and the party, and the partial and overwhelming bands show as `shaken` and `rallied`.
"""
from math import sqrt

from engine.dice_engine import draw as KD
from modules.combat import combatant as C
from modules.combat import wrapper
from modules.combat.config import CFG

_PAIR = ('arming', 'arming')


def _fight(seed, terms, cfg=CFG, pair=_PAIR, spirit=(None, None)):
    """One fight on `seed` under `terms`; returns `(result, trace, A, B)`. `spirit` sets each fighter's Spirit where given."""
    A, B = C.Combatant('A', weapon=pair[0]), C.Combatant('B', weapon=pair[1])
    for c, s in zip((A, B), spirit):
        if s is not None:
            c.set_attr('spirit', s)
    trace = []
    result = wrapper.fight(A, B, cfg, KD.seeded(KD.H2("test_combat_yield_draw", seed)), terms=terms, trace=trace.append)
    return result, trace, A, B


def _wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def test_fighters_across_the_line_sometimes_fight_on():
    """Gate 1. Under `blood` and `yield` a round the burst-breaker cut at a crossing (`separation` reason `terms`) is sometimes
    followed by another round (the roll passed), and under `yield` some fighters yield with Health still above the line."""
    fought_on = yielded = above = 0
    for terms in ('blood', 'yield'):
        for seed in range(150):
            _, trace, A, B = _fight(seed, terms)
            ylds = [e for e in trace if e['kind'] == 'yield']
            assert len(ylds) <= 1
            yielded += len(ylds)
            for i, e in enumerate(trace):
                if e.get('reason') == 'terms':   # the burst-breaker cut a round at a crossing: did the fight go on past it?
                    fought_on += any(x['kind'] == 'round_start' for x in trace[i + 1:])
            if terms == 'yield' and ylds:
                y = A if ylds[0]['by'] == 'A' else B
                above += y.wt.health_remaining > CFG['YIELD_HEALTH_FRAC'] * y.wt.health_full
    assert yielded > 0 and fought_on > 0 and above > 0, (yielded, fought_on, above)


def test_death_terms_leave_both_alive_sometimes():
    """Gate 2. Under `death` terms the share of scenes ending with both parties alive is strictly between 0 and 1; the yielder
    stands and the event's `accepted` is `None` (the victor's choice is the host's); fellings stay reachable."""
    both = felled = 0
    n = 200
    for seed in range(n):
        result, trace, A, B = _fight(seed, 'death')
        ylds = [e for e in trace if e['kind'] == 'yield']
        if ylds:
            assert ylds[0]['accepted'] is None and ylds[0]['terms'] == 'death' and ylds[0]['degree'] == 'fail'
            assert not (A.felled or B.felled) and result == (-1 if ylds[0]['by'] == 'A' else 1)
        both += not (A.felled or B.felled) and result != 0
        felled += A.felled or B.felled
    assert 0 < both < n and felled > 0, (both, felled)


def test_spirit_seven_yields_less_than_spirit_one():
    """The falsifier's second clause: `yield` terms, A varied against a default B, n 1,000 each: A's yield share at Spirit 7 lies
    wholly below A's at Spirit 1 (the Wilson intervals do not meet)."""
    n = 1000
    share = {}
    for s in (1, 7):
        k = sum(1 for seed in range(n) if any(e['kind'] == 'yield' and e['by'] == 'A' for e in _fight(seed, 'yield', spirit=(s, None))[1]))
        share[s] = (k, _wilson(k, n))
    assert share[7][1][1] < share[1][1][0], share


def test_yield_roll_is_keyed_by_turn_and_party(monkeypatch):
    """Each roll takes the sub-key `H2(rng.key, "yield:<scene>:<round>:<party>")`: one per party per round with a wound gate crossed,
    never two on one key, and a round's roll does not move with what the stream took before it."""
    seen = []
    real = wrapper._yield_roll
    monkeypatch.setattr(wrapper, '_yield_roll', lambda c, terms, sigma, cfg, draw: (seen.append((c.label, draw.key)), real(c, terms, sigma, cfg, draw))[1])
    checked = 0
    for seed in range(40):
        seen.clear()
        rng = KD.seeded(KD.H2("test_combat_yield_draw", seed))
        A, B = C.Combatant('A', weapon='arming'), C.Combatant('B', weapon='arming')
        trace = []
        wrapper.fight(A, B, CFG, rng, terms='blood', trace=trace.append)
        rounds = [e['round'] for e in trace if e['kind'] == 'round_start']
        keys = [k for _, k in seen]
        assert len(set(keys)) == len(keys)
        assert all(k in {KD.H2(rng.key, f"yield:0:{t}:{p}") for t in rounds for p in 'AB'} for k in keys), seed
        checked += len(keys)
    assert checked >= 40


def test_the_partial_and_overwhelming_bands_are_shaken_and_rallied():
    """Partial and Overwhelming rolls are told in the trace: across 120 fights under `death` terms some fighter is `shaken` and some `rallied`."""
    shaken = rallied = 0
    for seed in range(120):
        _, trace, A, B = _fight(seed, 'death')
        kinds = [e['kind'] for e in trace]
        shaken += kinds.count('shaken')
        rallied += kinds.count('rallied')
    assert shaken > 0 and rallied > 0, (shaken, rallied)
