"""B11.65, B11.66 -- THE `public:` COLUMN ON EVERY VERB ROW AND THE NOTICE DRAW (`18_DETERMINISM_notice_is_a_draw`).

B11.65 (Exact edits 1). A deed is public only when its verb row says so, and the column is required: a row without it, or with a value
that is not a boolean, never loads. Each test plants the defect in a copy of `verb_table.yaml` and observes `_load_verb_table` refuse it;
the unplanted copy is the control.

B11.66 (Exact edits 2 to 7). At `notice_arm: on` a bystander admitted to a deed draws once whether he saw it (`epistemic.notice`); the arm
SHIPS `off`, and each test below sets the arm it reads. The hand world is `harness/scenarios.py`'s forging (`FORGER` forges in the room of
two non-party witnesses, `p_low` and `p_mid`), flat-folded so the forging lands; `notice` is asked of the logged Event over many world
seeds (the key is `H(seed, tick, pid, "notice:" + event id)`, so the seed is the sample), and the realm tests read the seeded realm.
"""
from __future__ import annotations

from collections import Counter

from engine.season import epistemic
from engine.season.data import rosters
from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.data.rosters import WITNESS_CHANNELS
from engine.season.harness import probes as P
from engine.season.harness.scenarios import ABOUT, FAC, FORGE_ID, FORGER, INVESTIGATOR, conceal_forger, hear, step
from engine.season.loop import resolve as R, witness as W
from engine.season.loop.driver import SeasonDriver
from engine.season.queries import cache
from engine.season.state.attribution import live_cover
from engine.season.state.carriers import Act, Event, Proposition, StateChange, Tenure
from engine.season.harness.flat_fold import flat_fold
from engine.season.tests._realm_goldens import SHIPPED
from engine.season.tests.test_u1_capability_surface import _planted_verb_load, _refused, _row, _shipped_rows

ON = DEFAULT_FIXTURES.sweep("notice_arm", "on")
OFF = DEFAULT_FIXTURES.sweep("notice_arm", "off")
BANDS = ("Failure", "Partial", "Success", "Overwhelming")
HEAD = WITNESS_CHANNELS[0]
SEEDS = range(200)

#: THE ARM-OFF WORLD'S PINS: the realm content hash at seeds 0 to 2, one season, `notice_arm: off` set explicitly. `notice_arm` ships `off` (B11.67 flipped nothing), so the arm-off world
#: IS the shipped realm and the three values are `_realm_goldens.SHIPPED[(s, 1)]`, read from it rather than copied (one pin, re-pinned once). ⚠ The coupling is deliberate while the arm
#: ships `off`: the day it ships `on`, the shipped pins stop being the arm-off world's and this test must take its own values again (the B11.66 values are in `git log`).
ARM_OFF_PINS = {s: SHIPPED[(s, 1)] for s in (0, 1, 2)}


def test_public_column_absent_is_refused_at_load():
    """A planted row without `public:` is refused, naming the row; the same copy unplanted loads (the control)."""
    assert _planted_verb_load(lambda doc: None) is None
    msg = _planted_verb_load(lambda doc: _row(doc, "argue").pop("public", None))
    assert msg is not None and "argue" in msg and "public" in msg, msg


def test_public_column_not_a_boolean_is_refused_at_load():
    """`public: "yes"` (and an integer, which `bool` would also admit) is refused, naming the row."""
    for bad in ("yes", 1, None):
        msg = _planted_verb_load(lambda doc, bad=bad: _row(doc, "speak").update(public=bad))
        assert msg is not None and "speak" in msg and "public" in msg and "boolean" in msg, (bad, msg)


# --------------------------------------------------------------------------------------------------------------------------
# B11.66 -- the notice draw
# --------------------------------------------------------------------------------------------------------------------------

def _forged(fixtures, seed: int = 1, covered: bool = False, plant=None):
    """`(w, d, e)`: the tiny world flat-folded, the forger (in the room of `p_low` and `p_mid`) forging a sheet on `ABOUT`; `e` is the one Event `record.forged`. `covered`: he takes a cover first.
    `plant(w)`: what a test puts on a witness's sheet before the forging."""
    w = flat_fold(P.tiny_world(fixtures))
    w.world_seed = seed
    if plant is not None:
        plant(w)
    w.propositions[FAC] = Proposition(FAC, "HOLDS", "Valorsmark", "is a faction of this world", True, 0)
    for pid in (INVESTIGATOR, ABOUT):
        w.add_tenure(Tenure(f"t_commit_{pid}", pid, FAC, "commit", since=0))
    d = SeasonDriver(w)
    hear(w, FORGER, ABOUT)
    if covered:
        conceal_forger(w, d)
    (e,) = step(w, d, Act(id=FORGE_ID, actor=FORGER, verb="forge", payload={"subject": ABOUT}))
    assert e.kind == "record.forged"
    return w, d, e


def _bands(w, pid: str, e, ch: str = HEAD, seeds=SEEDS) -> list:
    """`pid`'s notice band of `e` at each world seed: the draw's key carries the seed, so each is one independent sample of the one pair."""
    out = []
    for s in seeds:
        w.world_seed = s
        w.discard_caches()
        out.append(epistemic.notice(w, pid, e, ch))
    return out


def _ledger(w, pid: str) -> list:
    return [(c.subject, c.predicate, repr(c.value), c.confidence, c.source) for c in w.persons[pid].ledger]


def _realm_at_on(monkeypatch=None, spy=None):
    """The seed-0 realm, one season, at `notice_arm: on`; `spy` (a wrapper of `witness.notice`) is installed for the run."""
    from engine.season.boot.realm import build_realm
    from engine.season.harness.populated import run
    if spy is not None:
        monkeypatch.setattr(W, "notice", spy(W.notice))
    w = build_realm(0, fixtures=ON)
    run(1, 0, w=w)
    return w


def test_all_four_bands_occur(monkeypatch):
    """Gate 1, the first clause: at `notice_arm: on` the seed-0 realm, one season, draws the four bands of the one ladder; pairs out of scope exist (`None`) and pairs that drew exist,
    so both halves of the scope were reached. The spy counts what WITNESS asked of `notice`."""
    seen: Counter = Counter()

    def spy(real):
        def asked(w, pid, e, ch, trail=None):
            band = real(w, pid, e, ch, trail)
            seen[band] += 1
            return band
        return asked

    _realm_at_on(monkeypatch, spy)
    assert set(seen) - {None} == set(BANDS), dict(seen)
    assert seen[None] > 0


def test_party_deposits_equal_across_arms():
    """Gate 1, the third clause, at the one barrier where the two arms can be told apart: the same forging witnessed at `off` and at `on`, over 12 world seeds. The DOER'S ledger is
    equal at every seed (a doer who does not know his own act is the falsifier); a non-party's, at `on`, never holds more than at `off`, holds less in sum, and holds something."""
    lower = off_total = on_total = 0
    for seed in range(12):
        (w_off, _d, _e), (w_on, _d2, _e2) = _forged(OFF, seed), _forged(ON, seed)
        assert _ledger(w_on, FORGER) == _ledger(w_off, FORGER) and len(_ledger(w_off, FORGER)) > 0, seed
        for pid in ("p_low", "p_mid"):
            n_off, n_on = len(w_off.persons[pid].ledger), len(w_on.persons[pid].ledger)
            assert n_on <= n_off, (seed, pid)
            off_total, on_total, lower = off_total + n_off, on_total + n_on, lower + (n_on < n_off)
    assert lower > 0 and 0 < on_total < off_total, (lower, on_total, off_total)


def test_a_partial_notice_names_the_event_and_not_the_hand_and_a_failure_nothing():
    """The falsifier's second clause and the graded outcomes: at a seed where a witness draws a Partial, he holds that the deed happened (the sighting's kind, the thing written) and holds
    NO claim about the forger and a `seen` claim whose `who` is withheld, where at `off` he holds both; at a seed where he draws a Failure he holds nothing this Event deposited."""
    seen_partial = seen_failure = 0
    for seed in range(60):
        w_off, _d, e_off = _forged(OFF, seed)
        w_on, _d2, e_on = _forged(ON, seed)
        w_on.discard_caches()
        band = epistemic.notice(w_on, "p_mid", e_on, HEAD)
        held_off, held_on = w_off.persons["p_mid"].ledger, w_on.persons["p_mid"].ledger
        who_off = [c.value.who for c in held_off if c.predicate == epistemic.SEEN_PREDICATE]
        who_on = [c.value.who for c in held_on if c.predicate == epistemic.SEEN_PREDICATE]
        if band == "Partial":
            assert who_off == [FORGER] and who_on == [None], (seed, who_off, who_on)
            assert any(c.subject == FORGER for c in held_off) and not any(c.subject == FORGER for c in held_on), seed
            assert any(c.predicate == e_on.kind for c in held_on), seed
            seen_partial += 1
        elif band == "Failure":
            assert len(held_on) == len(held_off) - len([c for c in held_off if c.predicate in (e_off.kind, epistemic.SEEN_PREDICATE)]), seed
            seen_failure += 1
    assert seen_partial > 0 and seen_failure > 0, (seen_partial, seen_failure)


def test_an_overwhelming_notice_is_seen_in_full():
    """The graded outcomes' last two: a witness (`inquiry` 7) whose draw is Overwhelming holds the deed at `confidence_default`, where the same deposit at `off` is refracted below it
    (the receiver is a poor reader, Attunement 1 at a live `competence_gain`, the one factor a presence deposit meets), and one whose draw is a Success holds it at the `off` confidence
    exactly. Over 40 world seeds both bands are met."""
    full = DEFAULT_FIXTURES.get("confidence_default")
    met = Counter()
    attuned = lambda fx: fx.sweep("competence_gain", 0.5)                                              # noqa: E731

    def poor_reader(w):
        w.persons["p_mid"].capability["inquiry"] = 7
        w.persons["p_mid"].attributes["attr.social.attunement"] = 1

    for seed in range(40):
        (w_off, _d, e_off), (w_on, _d2, e_on) = (_forged(attuned(OFF), seed, plant=poor_reader),
                                                 _forged(attuned(ON).sweep("notice_ob", "plain"), seed, plant=poor_reader))
        w_on.discard_caches()
        band = epistemic.notice(w_on, "p_mid", e_on, HEAD)
        kind_conf = lambda w, e: [c.confidence for c in w.persons["p_mid"].ledger if c.predicate == e.kind]      # noqa: E731
        if band == "Overwhelming":
            assert kind_conf(w_on, e_on) and set(kind_conf(w_on, e_on)) == {full} and kind_conf(w_off, e_off) and all(c < full for c in kind_conf(w_off, e_off)), seed
        elif band == "Success":
            assert kind_conf(w_on, e_on) == kind_conf(w_off, e_off) and kind_conf(w_on, e_on), seed
        met[band] += 1
    assert met["Overwhelming"] > 0 and met["Success"] > 0, dict(met)


def test_inquiry_three_notices_more_often_than_default():
    """Gate 2, the first clause: over 200 world seeds a witness holding `inquiry` 3 notices a forging (any band above Failure) more often than one holding none, and neither share is 0 or 1.
    `plain` is the level, so the covert step is the only one on the obstacle (a heavier one saturates at the ceiling and the two pools read alike)."""
    w, _d, e = _forged(ON.sweep("notice_ob", "plain"))
    w.persons["p_low"].capability["inquiry"] = 3
    trained, untrained = (sum(b != "Failure" for b in _bands(w, pid, e)) / len(SEEDS) for pid in ("p_low", "p_mid"))
    assert 0 < untrained < trained < 1, (untrained, trained)


def test_cover_quality_lowers_notice():
    """Gate 2, the second clause: a forger holding a cover of quality 1 (a Success `conceal`) is noticed less often than one whose cover is of quality 0 -- the same world, the same
    Event, the same 200 seeds, only the cover Record's `forgery_quality` differs -- no seed noticing him MORE under the better cover, some noticing him less, and no share 0 or 1."""
    w, _d, e = _forged(ON.sweep("notice_ob", "plain"), covered=True)
    cover = w.records[live_cover(w, FORGER)]
    assert cover.forgery_quality == 1
    rank = {b: i for i, b in enumerate(BANDS)}
    good = [rank[b] for b in _bands(w, "p_mid", e)]
    cover.forgery_quality = 0
    none = [rank[b] for b in _bands(w, "p_mid", e)]
    assert all(g <= n for g, n in zip(good, none)) and any(g < n for g, n in zip(good, none)), (sum(good), sum(none))
    assert 0 < sum(n > 0 for n in none) / len(SEEDS) < 1 and 0 < sum(g > 0 for g in good) / len(SEEDS) < 1


def test_the_scope_of_a_draw():
    """A pair draws iff the Event is a deed and he is neither its doer nor a subject of its changes; a `public` row's deed deposits without a draw to those presence admitted and still
    draws for one a later channel did. Each clause beside its control: the same Event asked of a person in scope reads a band."""
    w, _d, e = _forged(ON)
    assert epistemic.notice(w, "p_mid", e, HEAD) in BANDS                                 # control: a non-party at the head channel draws
    assert epistemic.notice(w, FORGER, e, HEAD) is None                                    # the doer
    subject_event = Event("ev_subject", e.kind, [StateChange("p_low", "set", "Event", field="body")], list(e.causes), w.tick)
    assert epistemic.notice(w, "p_low", subject_event, HEAD) is None                       # a subject of the changes (the forger's act caused it; p_low is what it changed)
    not_a_deed = Event("ev_plain", "claim.deposited", list(e.changes), list(e.causes), w.tick)
    assert epistemic.notice(w, "p_mid", not_a_deed, HEAD) is None                          # not a deed kind
    w.acts.append(Act(id="a_public", actor=FORGER, verb="petition", payload=None))
    public = Event("ev_public", "petition.filed", [], ["a_public"], w.tick)
    assert epistemic.notice(w, "p_mid", public, HEAD) is None                              # a public row's deed, presence-admitted
    assert epistemic.notice(w, "p_mid", public, WITNESS_CHANNELS[1]) in BANDS              # the same deed, admitted by a later channel, draws
    w.acts.append(Act(id="a_private", actor=FORGER, verb="forge", payload=None))
    assert epistemic.notice(w, "p_mid", Event("ev_private", "petition.filed", [], ["a_private"], w.tick), HEAD) in BANDS   # control: the same kind from a row that is not public


def test_a_telling_is_not_a_notice_draw(monkeypatch):
    """The source's "a telling ... is unchanged": a `news.told` Event never reaches `notice` through WITNESS, so its hearers keep the told channel at `on` as at `off`. Observed as the
    spy never being asked of that kind over a realm season that held a telling (the control)."""
    asked = []

    def spy(real):
        def seen(w, pid, e, ch, trail=None):
            asked.append(e.kind)
            return real(w, pid, e, ch, trail)
        return seen

    w = _realm_at_on(monkeypatch, spy)
    assert asked and W.TELLING_KIND not in asked, sorted(set(asked))
    assert any(e.kind == W.TELLING_KIND for e in w.log)


def test_the_notice_site_rows_load_and_move_only_notice(monkeypatch):
    """U1-E's per-site check, `[ASSUMPTION: name, E-3]`. The site's rows load (`dice` on `inquiry`, `edge` on Perception, both the actor's); a planted holder moves only that site's reader's output
    (a Perception of 7 moves `notice_edges`, not `notice_pools` and not the crisis site's net sigma; an `inquiry` of 3 moves `notice_pools`); and the loader refuses the site's rows once the
    site is not registered, naming it (the control: registered, they load)."""
    assert _refused(_shipped_rows()) is None
    dice, edge = (next(r for r in rosters.capability_rows("notice") if r.role == role) for role in ("dice", "edge"))
    assert (dice.key, dice.side, edge.key, edge.side) == ("inquiry", "actor", "attr.mind.perception", "actor")
    w = P.tiny_world(ON)
    p = w.persons["p_low"]
    base_pool, base_edge, base_crisis = cache.notice_pools(w)["p_low"], cache.notice_edges(w)["p_low"], R._crisis_net_sigma(w, p)
    assert base_pool == int(DEFAULT_FIXTURES.get("pool_default")) and base_edge == 0.0
    p.attributes = {**(p.attributes or {}), "attr.mind.perception": 7}
    w.discard_caches()
    assert cache.notice_edges(w)["p_low"] > base_edge and cache.notice_pools(w)["p_low"] == base_pool and R._crisis_net_sigma(w, p) == base_crisis
    p.capability["inquiry"] = 3
    w.discard_caches()
    assert cache.notice_pools(w)["p_low"] == 3
    sites = dict(rosters.CAPABILITY_USE_SITES)
    sites.pop("notice")
    monkeypatch.setitem(rosters._ROSTERS, "capability_use_sites", sites)
    msg = _refused(_shipped_rows())
    assert msg is not None and "notice" in msg and "unregistered site" in msg, msg


def test_arm_off_reproduces_the_pinned_hash():
    """Control: `notice_arm: off`, set explicitly, reproduces the seeds 0 to 2 one-season realm hash pinned in `ARM_OFF_PINS` (read on the tree before this item's edit and equal after it),
    and `on` moves the seed-0 world (the arm is not vacuous)."""
    from engine.season.boot.realm import build_realm
    from engine.season.harness.populated import run
    checked = 0
    for seed, pin in sorted(ARM_OFF_PINS.items()):
        w = build_realm(seed, fixtures=OFF)
        run(1, seed, w=w)
        assert w.content_hash() == pin, seed
        checked += 1
    assert checked == 3
    assert _realm_at_on().content_hash() != ARM_OFF_PINS[0]
