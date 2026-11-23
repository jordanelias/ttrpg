"""v9 SC-01 steps 13 + 15, ONE change (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the
CARRIED block's *Step 13* and *Step 15*): the social contest scene's contest provider, and the
three social prize rows repointed to it.

WHAT IS BUILT, each asked of the real manifest, the real registrar, the real fold and the real seam:
  * THE REPOINT (step 13, ED-SC-0033 clause (2)): `a standing`, `a proposition` and `a matter` drop
    `interim: true` and name `provider: social_contest` -- a ROW change. Three rows, not the plan's two:
    step 12 added `a matter` (`speak`'s prize) as an interim row.
  * THE PROVIDER (step 15): `@provider("contest", "social_contest")`, the host adapter in
    `seam/wrappers/sigma.py`, reached by the prize rows' STRING; it calls the module entry the rows name
    (`module_entry: social_contest.roll`, registered by `30`'s registrar at driver construction, never
    imported by the host) and holds the entry to a `Margin` at the boundary -- a margin, never a winner
    (`08_SEAM.md`'s provider rule, intent only). The automated mode stays the σ-leverage roll: SC-05's
    decision, recorded in `modules/social_contest/roll.py`'s docstring, keeps it over the kernel.
  * THE RUNG (C-8): a contested act on a non-`mass_battle` prize dispatches at the actor's place
    (`world_q.place_of`), where it dispatched at the placeholder `"R"`.

THE FALSIFIERS (each run red before the build, 2026-10-16, base `29af7354`):
  * the rows name the scene's provider -- RED at base (`sigma_leverage`).
  * the provider is registered by importing the seam and the driver constructs -- RED at base.
  * THE HALF-STATE: the rows repointed with no provider registered refuse at driver construction naming
    the first such prize (`30`'s refusal (c)); a misspelled `provider:` and a deleted composition row
    each refuse naming the row. This is why 13 and 15 are one change.
  * the entry returns a `Margin`; an entry returning the kernel's winner shape, or a dict carrying a
    winner, is refused at the host boundary naming the entry -- RED at base (no `Margin` type).
  * a hand-built `speak` and `tell` resolve end to end through the new provider, the Event's degree the
    one ladder's reading of the provider's own pair -- RED at base (no `social_contest` provider).
  * C-8: a contested `speak` by the Duke dispatches at his settlement `S`, the copyist's at the hearth
    `Hh` -- RED at base (both `"R"`).
  * SCRIPTING DRIFT: the arrangement-id scan first written here MOVED at step 16, which owns the
    closure test (`tests/test_sc01_the_bar.py`, its one home).
No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit).
"""

from __future__ import annotations

import random
from engine.dice_engine import draw

import pytest

from ..data.rosters import roster_map
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..manifest import MODULE_ENTRIES, PROVIDERS
from ..manifest.registrar import ModuleEntry
from ..queries import world_q
from ..queries.inputs import Margin, SocialContestInput
from ..queries import person_q
from ..queries.person_q import said_of
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim
from engine.substrate import composition
from .test_sc01_speak import _docket
from .test_u7_remit import _fold, _world

PROVIDER = "social_contest"
ENTRY = "social_contest.roll"
SEAT, DUKE = "off_duke", "p_high"
SPEAKER, PARTY = "p_low", "p_mid"


def _social_rows() -> dict:
    return {k: r for k, r in roster_map("contest_subsystems", "prizes").items()
            if isinstance(r, dict) and r.get("module") == "social_contest"}


def _recording(monkeypatch) -> list:
    """Wrap the registered provider so each call's verb, rung and return is seen. The wrapper calls the
    real provider, so what is folded is what the provider returned."""
    real = PROVIDERS[("contest", PROVIDER)]
    calls: list = []

    def rec(w, claimants, causes, prize, **kw):
        out = real(w, claimants, causes, prize, **kw)
        calls.append(dict(verb=kw.get("verb"), rung=kw.get("rung"), prize=prize, out=out,
                          claimants=list(claimants), causes=list(causes), kw=dict(kw)))
        return out
    monkeypatch.setitem(PROVIDERS, ("contest", PROVIDER), rec)
    return calls


# ================================================================================================
# STEP 13: THE ROWS
# ================================================================================================

def test_sc01_s13_the_social_prize_rows_name_the_container_provider():
    rows = _social_rows()
    assert rows, "no prize row names the social_contest module"
    for prize, row in sorted(rows.items()):
        assert row["provider"] == PROVIDER, (prize, row["provider"])
        assert row["module_entry"] == ENTRY, (prize, row.get("module_entry"))


# ================================================================================================
# STEP 15: THE PROVIDER, REGISTERED; AND THE HALF-STATE THAT SPLITTING 13 FROM 15 WOULD SHIP
# ================================================================================================

def test_sc01_s15_the_provider_is_registered_and_the_driver_constructs_on_the_shipped_rows():
    assert ("contest", PROVIDER) in PROVIDERS, sorted(PROVIDERS)
    # No provider stays registered that no row names: the interim one went with the repoint.
    assert ("contest", "sigma_leverage") not in PROVIDERS, sorted(PROVIDERS)
    SeasonDriver(P.tiny_world())
    assert ENTRY in MODULE_ENTRIES, sorted(MODULE_ENTRIES)


def test_sc01_s13_s15_the_rows_repointed_without_their_provider_refuse_at_driver_construction(monkeypatch):
    """THE HALF-STATE: step 13 landed and step 15 not. Every social row names `social_contest` and
    nothing registered it -> `30`'s refusal (c), naming the first such prize in roster order."""
    for row in _social_rows().values():
        monkeypatch.setitem(row, "provider", PROVIDER)
    monkeypatch.delitem(PROVIDERS, ("contest", PROVIDER), raising=False)
    with pytest.raises(Unspecified, match=r"prize 'a standing' names provider 'social_contest', "
                                          r"which nobody registered"):
        SeasonDriver(P.tiny_world())


def test_sc01_s15_a_misspelled_provider_row_refuses_at_driver_construction_naming_the_row(monkeypatch):
    monkeypatch.setitem(_social_rows()["a matter"], "provider", "social_contst")
    with pytest.raises(Unspecified, match=r"prize 'a matter' names provider 'social_contst'"):
        SeasonDriver(P.tiny_world())


def test_sc01_s15_a_deleted_composition_row_refuses_at_driver_construction_naming_the_row(monkeypatch):
    SeasonDriver(P.tiny_world())                       # the control: the shipped rows construct
    monkeypatch.delitem(composition.ROLES, ENTRY)
    with pytest.raises(Unspecified, match=ENTRY.replace(".", r"\.")):
        SeasonDriver(P.tiny_world())


# ================================================================================================
# LENS B: A MARGIN, NEVER A WINNER
# ================================================================================================

def _record(**kw) -> SocialContestInput:
    # B05.14: nobody opposite composes `difficulty + opposed_ob(pool_default)`: 0 + 0.5 x 4 = 2.0, the stand-in these records were read at
    base = dict(pool=4, opposition=None, obstacle_ceiling=2.0, obstacle_refusal_multiple=2.0, leverage=0.0,
                difficulty=0.0, pool_default=4, pool_add=0, opposition_rate=0.5)
    base.update(kw)
    return SocialContestInput(**base)


def test_sc01_s15_the_entry_returns_a_margin_and_nothing_that_names_a_winner():
    SeasonDriver(P.tiny_world())                       # the registrar fills MODULE_ENTRIES
    got = MODULE_ENTRIES[ENTRY].fn(_record(), draw.seeded(draw.H2("test_sc01_provider", 7)))
    assert isinstance(got, Margin), type(got)
    assert set(Margin.__dataclass_fields__) == {"net", "ob", "terms"}, sorted(Margin.__dataclass_fields__)      # B05.14: and no winner, band or side


@pytest.mark.parametrize("winner", [
    (("a", "win"), None),                              # the kernel's own return, `((band, reason), bout)`
    dict(status="RESOLVED", winner="p_low", net=3.0, ob=2.0),
])
def test_sc01_s15_an_entry_returning_a_winner_is_refused_at_the_host_boundary(monkeypatch, winner):
    w, _d = _world()
    real = MODULE_ENTRIES[ENTRY]
    # THE CONTROL: the shipped entry passes the same boundary, on the same world and act.
    ok = sigma.resolve(w, [SPEAKER, PARTY], ["c"], "a standing", verb="tell", subject=PARTY,
                       rng=draw.seeded(draw.H2("test_sc01_provider", 3)))
    assert ok["status"] == "RESOLVED" and ok["module"] == PROVIDER, ok
    monkeypatch.setitem(MODULE_ENTRIES, ENTRY,
                        ModuleEntry(real.role, real.entry, real.verb, real.target, lambda inp, rng: winner))
    with pytest.raises(Unspecified, match=r"social_contest\.roll.*not a `Margin`"):
        sigma.resolve(w, [SPEAKER, PARTY], ["c"], "a standing", verb="tell", subject=PARTY,
                      rng=draw.seeded(draw.H2("test_sc01_provider", 3)))


# ================================================================================================
# END TO END: A HAND-BUILT `speak` AND `tell` THROUGH THE NEW PROVIDER, AND C-8's RUNG
# ================================================================================================

def test_sc01_s15_a_docketed_speak_resolves_through_the_provider_at_the_speakers_place(monkeypatch):
    w, d = _world()
    _docket(w, d)
    calls = _recording(monkeypatch)
    folded = 0
    for actor, place in ((SPEAKER, "Hh"), (DUKE, "S")):
        assert world_q.place_of(w, actor) == place, (actor, world_q.place_of(w, actor))
        out = _fold(w, d, Act(id=f"sp_{actor}", actor=actor, verb="speak", payload={"subject": PARTY}))
        assert len(out) == 1, [(e.kind, e.degree) for e in out]
        call = calls[-1]
        assert call["verb"] == "speak" and call["prize"] == "a matter", call
        # C-8: the seam dispatched at the actor's place, never the `"R"` placeholder.
        assert call["rung"] == place, (actor, call["rung"])
        assert call["out"]["status"] == "RESOLVED" and call["out"]["module"] == PROVIDER, call["out"]
        assert out[0].degree == ladder.degree_of(call["out"]), (out[0].degree, call["out"])
        folded += 1
    assert folded == 2 and len(calls) == 2


def test_sc01_s15_a_tell_resolves_through_the_provider(monkeypatch):
    w, d = _world()
    calls = _recording(monkeypatch)
    w.persons[SPEAKER].ledger.append(
        Claim("c_s15", SPEAKER, "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    tell = Act(id="s15_tell", actor=SPEAKER, verb="tell",
               payload={"subject": "Hh", "to": PARTY,
                        "said": said_of(w.persons[SPEAKER].ledger, "Hh", w.fixtures)})
    out = _fold(w, d, tell)
    assert len(calls) == 1, calls
    call = calls[0]
    assert call["verb"] == "tell" and call["prize"] == "a standing" and call["rung"] == "Hh", call
    assert call["out"]["module"] == PROVIDER, call["out"]
    graded = [e for e in out if e.degree is not None]
    assert graded and all(e.degree == ladder.degree_of(call["out"]) for e in graded), (
        [(e.kind, e.degree) for e in out], call["out"])


# ================================================================================================
# B05.10 -- THE LEVERAGE CHANNEL IS SIGNED, AND THE `capability` SOURCE READS THE `edge` ROWS (ADV Edit A, MAP §G edit 6)
# ================================================================================================
# A row planted in a copy of the shipped table and loaded by the real loader; the shipped table (no `edge` row) is the control.
# `when: {plea: ...}` (`05_SC_capability_surface`'s gate) cannot be planted: `capability_when_keys` is `rank_at_least` alone and no
# act operand carries a plea, so `when` is exercised through the one key that exists.

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, record_odds       # noqa: E402
from engine.substrate import descriptors                                      # noqa: E402

SUBJECT, SKILL = "p_mid", "copying"          # `tell`'s skill (asserted in the first test below)


def _edge_world():
    import copy                                                               # noqa: F401  (the planter below)
    from ..data.fixtures import DEFAULT_FIXTURES
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)
    for p in w.persons.values():
        p.capability, p.attributes = {}, {}
    return w, Act(id="edge_tell", actor=SPEAKER, verb="tell", payload={"to": SUBJECT})


def _plant_edge(monkeypatch, **columns):
    """Append one `social_roll` `edge` row (`columns`) to a copy of the shipped table, loaded by the real loader."""
    import copy
    from ..data import rosters
    from ..data.fixtures import DEFAULT_FIXTURES
    rows = copy.deepcopy(list(rosters._TABLES["capability_uses"]["rows"]))
    rows.append(dict(use="social_roll", role="edge", **columns))
    monkeypatch.setattr(rosters, "_CAPABILITY_USES", rosters._load_capability_uses(rows, dict(DEFAULT_FIXTURES._v)))


def _true_odds(w, act, leverage):
    """What the record's own pool and obstacle give at `leverage`: the number a signed channel must reproduce."""
    inp = sigma.contest_input(w, [act.actor, SUBJECT], verb=act.verb, subject=SUBJECT)
    return inp, record_odds(inp.pool, sigma._composed_obstacle(inp), leverage)


def test_the_shipped_table_brings_no_edge_and_the_channel_names_capability():
    from ..data.verbs import VERB_CAPABILITY
    from ..data import rosters
    assert VERB_CAPABILITY["tell"] == SKILL
    # B05.99 re-pin: B05.17 (`proofs`, `favour`), B05.20 (`office`) and B05.60 (`wounds`) joined the roster; was [effort, capability]
    # (read off the roster and compared member by member: a literal copy of the whole roster would be the duplicate
    # `test_jordan_no_definition_is_hardcoded_in_a_body` (retired) refuses)
    sources = tuple(rosters.roster("advantage_sources", ordered=True))
    assert sources[:2] == ("effort", "capability") and len(sources) == 6
    assert sources[2:] == ("proofs", "favour", "office", "wounds")
    assert set(sigma.ADVANTAGE_SOURCES) == set(sources)
    w, act = _edge_world()
    inp, odds = _true_odds(w, act, 0.0)
    assert inp.leverage == 0.0 and sigma.odds_of(w, act) == odds                    # CONTROL: no row, no level, the pool's own odds


def test_a_level_against_lowers_odds(monkeypatch):
    """ADV Edit A: a source returning `([], ["minor"])` is a level AGAINST the roller: `record_odds(pool, ob, -0.25)`."""
    w, act = _edge_world()
    inp, before = _true_odds(w, act, 0.0)
    assert sigma.odds_of(w, act) == before
    monkeypatch.setitem(sigma.ADVANTAGE_SOURCES, "capability", lambda fx, operands: ([], ["minor"]))
    assert sigma.advantage_sigma(w.fixtures, {}) == -LEVEL_SIGMA["minor"] == -0.25
    after = sigma.odds_of(w, act)
    assert after == record_odds(inp.pool, sigma._composed_obstacle(inp), -0.25)
    assert after[0] > before[0] and after[2] + after[3] < before[2] + before[3]     # more Failure, fewer Success-or-better
    monkeypatch.setitem(sigma.ADVANTAGE_SOURCES, "capability", lambda fx, operands: (["minor"], []))
    assert sigma.advantage_sigma(w.fixtures, {}) == 0.25                             # the same level FOR the roller is the mirror


def test_a_planted_edge_row_moves_odds_only_where_its_when_holds(monkeypatch):
    """A `when`-selected `edge` row (against the roller, one `moderate` level, once held) on the subject's skill, selected by
    `rank_at_least: 3`: with a subject at rank 5 the odds are the pool's own at -0.5; at rank 2 `when` fails and the odds equal the
    no-row odds; with the row removed they equal them again."""
    w, act = _edge_world()

    def at(rank):
        w.persons[SUBJECT].capability = {SKILL: rank}
        return sigma.odds_of(w, act)
    plain = {r: at(r) for r in (2, 5)}
    _plant_edge(monkeypatch, key=SKILL, side="subject", per="held", against=True, level="moderate", when=dict(rank_at_least=3))
    assert at(2) == plain[2]                                                       # `when` fails: nothing moves
    moved = at(5)
    assert moved != plain[5]
    inp, expected = _true_odds(w, act, -0.5)
    assert inp.leverage == -0.5 and moved == expected                              # `moderate` once, against
    assert moved[0] > plain[5][0]
    monkeypatch.undo()
    assert at(5) == plain[5]                                                       # the row removed: equal again


def test_a_planted_trait_row_counts_for_the_actor_and_against_him_through_the_subject(monkeypatch):
    """A trait is held (1) or not (0). `side: subject, against: true` counts a level against the roller when the SUBJECT holds it
    and nothing when he does not; `side: actor` counts for him when HE holds it. A trait nobody holds changes no odds."""
    trait = next(iter(descriptors.TRAITS))
    w, act = _edge_world()
    plain = sigma.odds_of(w, act)
    _plant_edge(monkeypatch, key=trait, side="subject", per="held", against=True, level="moderate")
    assert sigma.odds_of(w, act) == plain                                          # nobody holds it
    w.persons[SUBJECT].traits = frozenset({trait})
    inp, expected = _true_odds(w, act, -0.5)
    assert inp.leverage == -0.5 and sigma.odds_of(w, act) == expected != plain
    monkeypatch.undo()
    _plant_edge(monkeypatch, key=trait, side="actor", per="held", level="strong")
    w.persons[SUBJECT].traits = frozenset()
    assert sigma.odds_of(w, act) == plain                                          # the actor does not hold it
    w.persons[SPEAKER].traits = frozenset({trait})
    inp, expected = _true_odds(w, act, 0.75)
    assert inp.leverage == 0.75 and sigma.odds_of(w, act) == expected


def test_per_mid_counts_signed_steps_from_the_scale_midpoint(monkeypatch):
    """`per: mid`: an unauthored attribute is the mid-point (zero steps), above it counts for the side named, below it against;
    `against: true` flips the sign. One `minor` level a step."""
    key = descriptors.ATTRIBUTES[0]
    mid = (descriptors.ATTRIBUTE_FLOOR + descriptors.ATTRIBUTE_CEILING) / 2
    w, act = _edge_world()
    plain = sigma.odds_of(w, act)
    _plant_edge(monkeypatch, key=key, side="actor", per="mid", level="minor")
    assert sigma.odds_of(w, act) == plain                                          # unauthored: the mid-point, zero steps
    for held, steps in ((int(mid) + 2, 2), (int(mid) - 3, -3)):
        w.persons[SPEAKER].attributes = {key: held}
        inp = sigma.contest_input(w, [SPEAKER, SUBJECT], verb="tell", subject=SUBJECT)
        assert inp.leverage == steps * LEVEL_SIGMA["minor"], (held, inp.leverage)
    monkeypatch.undo()
    _plant_edge(monkeypatch, key=key, side="actor", per="mid", level="minor", against=True)
    inp = sigma.contest_input(w, [SPEAKER, SUBJECT], verb="tell", subject=SUBJECT)
    assert inp.leverage == 3 * LEVEL_SIGMA["minor"]                                # held 3 below the mid, `against` flips it


def test_the_believer_reads_the_subjects_row_only_from_a_held_claim(monkeypatch):
    """Mode (b): the roller's own values are his to know; the subject's are `None` without a claim (`CAPABILITY_CLAIM` + the key),
    never a figure, and a held claim gives the same level the true input gives for the same held value."""
    trait = next(iter(descriptors.TRAITS))
    w, act = _edge_world()
    me = w.persons[SPEAKER]

    def claim(predicate, value, n):
        me.ledger.append(Claim(id=f"c{n}", holder=SPEAKER, subject=SUBJECT, predicate=predicate, value=value,
                               when=0, source="told", confidence=5, visibility="own"))
    claim(person_q.CAPABILITY_CLAIM + SKILL, 2, 0)                                 # the opposition's claim the verb already needs
    from ..data.verbs import VERB_TABLE
    claim(person_q.CAPABILITY_CLAIM + VERB_TABLE["tell"].opposed_attribute, 3, 9)  # and, B05.14, the attribute he resists it with
    control = sigma.odds_of(w, act, believer=me)
    assert control is not None                                                     # CONTROL: no row, a believed figure
    _plant_edge(monkeypatch, key=trait, side="subject", per="held", against=True, level="moderate")
    # B05.99 rewrite (B05.62 ships `believed_prior: ordinary`, B05.23 `regard_step` 1.0): at the shipped prior a row he holds no
    # claim on reads an ORDINARY person's (holding nothing: no level), so the figure is the control's; the "unknown, not a guess"
    # rule is the prior's control arm, read with `regard_step` at its own control (else every lone person is unknown, B05.21)
    assert sigma.odds_of(w, act, believer=me) == control
    shipped = w.fixtures
    w.fixtures = shipped.sweep("believed_prior", "none").sweep("regard_step", 0)
    assert sigma.odds_of(w, act, believer=me) is None                              # a row he cannot read: unknown, not a guess
    w.fixtures = shipped
    claim(person_q.CAPABILITY_CLAIM + trait, 0, 1)
    assert sigma.odds_of(w, act, believer=me) == control                           # he believes it not held: no level
    me.ledger.append(Claim(id="c2", holder=SPEAKER, subject=SUBJECT, predicate=person_q.CAPABILITY_CLAIM + trait, value=1,
                           when=5, source="told", confidence=5, visibility="own"))      # the later claim wins (`believed_capability`)
    believed = sigma.odds_of(w, act, believer=me)
    assert believed is not None and believed != control and believed[0] > control[0]


# ================================================================================================
# B05.18 -- A SOCIAL ROLL'S EVENT CARRIES THE ROLL THAT DECIDED IT (SC-P1, OBS §4 step 2; closes H-284)
# ================================================================================================
# `Event.ending` is the margin provider's tuple `((key, value), ...)` in `rosters.yaml: margin_endings`' order. Read
# against the provider's OWN return, recomputed with the act's own generator: the tuple follows the roll, never a recomputation.

def _argue_once(monkeypatch, key):
    """One `argue` folded on `tiny_world`: `(events, the provider's call, the act, the world)`."""
    from .test_in12_step9 import _argue, _argue_world
    from .test_in10_record_operands import _resolve
    w, d, pid, _keys = _argue_world()
    calls = _recording(monkeypatch)
    act = _argue(pid, key)
    out = _resolve(w, d, act)
    assert len(calls) == 1, calls
    return out, calls[0], act, w


def _the_act_own_roll(w, act, call):
    """`sigma.resolve` called again with the act's own generator (`loop/resolve.py::_contest`'s purpose) and the seam's own arguments."""
    from ..state.ids import draw_factory
    kw = dict(call["kw"])
    kw["rng"] = draw_factory(w.world_seed, lambda: w.tick)(act.actor, f"roll:{call['prize']}:{act.id}")
    return sigma.resolve(w, call["claimants"], call["causes"], call["prize"], **kw)


def test_a_social_roll_event_carries_its_margin_ending(monkeypatch):
    from ..data.rosters import MARGIN_ENDING
    assert "levels" in MARGIN_ENDING and MARGIN_ENDING[-1] == "leverage", MARGIN_ENDING
    bands, checked = set(), 0
    for i in range(24):
        out, call, act, w = _argue_once(monkeypatch, f"mg_{i}")
        monkeypatch.undo()
        r = _the_act_own_roll(w, act, call)
        assert r["status"] == "RESOLVED" and r == call["out"], (r, call["out"])            # the recomputation is the roll the fold saw
        expected = tuple((k, r["settled_margin" if k == "margin" else k]) for k in MARGIN_ENDING)
        assert out and all(e.ending == expected for e in out), [(e.kind, e.degree, e.ending) for e in out]
        # the tuple grades to the Event's band on the one ladder, through the same dispatcher the fold used
        e = dict(expected)
        assert ladder.degree_of({"net": e["net"], "ob": e["ob"], "settled_margin": e["margin"]}) == out[0].degree
        assert e["margin"] == e["net"] - e["ob"] and sum(v for _n, v in e["terms"]) == pytest.approx(e["ob"])
        from ..harness import chronicle
        assert chronicle.rolled_text(expected).startswith(f"obstacle {e['ob']:.3g} = ")        # the chronicle's one line reads the same tuple
        bands.add(out[0].degree)
        checked += 1
    assert checked == 24 and "Failure" in bands and len(bands) > 1, bands                 # the Failure band's Events carry it too


def test_a_refused_contest_carries_no_margin_ending():
    """`_refuse_party_gap`: no dice were dealt, so the refusal's Event carries no tuple."""
    from .test_in12_step9 import _argue, _argue_world
    from .test_in10_record_operands import _resolve
    w, d, pid, _keys = _argue_world()
    out = _resolve(w, d, _argue(pid, "mg_gap", to="p_nobody"))
    assert out and all(e.ending == () for e in out), [(e.kind, e.ending) for e in out]


def test_no_claim_predicate_is_a_margin_ending_after_witness():
    """Falsifier (b): a hearer must not learn the speaker's pool from the room. After a WITNESS barrier no `Claim` in any ledger has a
    predicate drawn from `margin_endings`."""
    from ..data.rosters import MARGIN_ENDING
    from ..data.matrix import WriteClass
    from ..loop.driver import mint_token
    from .test_in12_step9 import _argue, _argue_world
    from .test_in10_record_operands import _resolve
    w, d, pid, _keys = _argue_world()
    out = _resolve(w, d, _argue(pid, "mg_wit"))
    assert out and all(e.ending for e in out)                                              # the control: the record exists to leak
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    claims = [c for p in w.persons.values() for c in p.ledger]
    assert claims                                                                          # the barrier deposited something to read
    leaked = [c for c in claims if c.predicate in MARGIN_ENDING or c.predicate.split(":")[0] in MARGIN_ENDING]
    assert not leaked, leaked
