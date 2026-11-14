"""CR-76 (workplan v11, batch B11-S3): THE WORLD READING -- `queries/world_q.py`'s `flows_in`, `concluded`,
`within`, `presented`, `commensurate`, and `harness/strife.py`'s opening-to-terminal route check.

Every falsifier runs on a HAND-BUILT world (P9): the shipped realm, before B10-11, holds no live `detain` beyond
`arrest`, no `at_war` pair and no docketed matter a strand names, so those arms are exercised only here.

  1. Two realm-wide events while an era is open read as ONE era (two strands, one era holding both).
  2. A terminal move at the realm rung with no open referent concludes the era and frees the realm slot; the
     terminal missing leaves it open; a live `detain`, a docketed matter or (through a stand-in for the owner) an
     `at_war` pair among its parties leaves it open; a strand never concludes on its own opening move.
  3. A person within the realm flow whose ledger holds none of its moves is listed as within; a person under a
     root outside the realm is not.
  4. Two petitions sharing a matter open a strand holding both; two on different matters open none. The move
     that content-opens is never terminal (a third keeps the strand open; a later `matter.determined` closes
     it); a linking content opener still takes its earlier same-matter move, and merges the strand that move
     links to.
  4a. The era: a move on the foreign root is within none; a terminal at a duchy, or a lone realm-wide
     terminal, leaves it open. Rule (b): a later linked non-terminal move reopens a concluded strand; two
     factions not at war (the real `at_war`) leave it concluded. `presented` types a duchy's two slots and
     groups the rest under the era (hand-built reading); `incompatible_span` reads a `true` pair.
  5. `commensurate`: +1 (a `false` pair; a shared affiliation), -1 (a `true` pair), 0 (only `null`; none held).
  6. The route check names a planted gap: a verb removed from the resolvable set loses its pairs. The pair
     profile pairs only adjacent single-code moves.

CR-77 (same batch): THE PERSON READING -- `flows_known`, `concluded_known`, `open_referents_known`, over a
ledger built by hand (the witness's claims minted by the real deposit rule, `epistemic.claim_subjects`).
  7. A witness and a hearsay holder of the same events read different flows; an empty ledger reads none; a
     person within the realm flow whose ledger holds none of its moves reads none.
  8. Lacking the terminal claim, or holding only a `field.won`, he reads the strand open while the world's
     `concluded` reads it closed.
  9. The person-side open-referent test (named gap (1)): an arrest of a custody edge with no later release
     keeps his strand on that edge open, and the arrester is never read as restrained; the docket and war arms
     have no ledger source and are dropped, so a world docketed or at war does not hold his strand open.
 10. Named gap (2): a succession's deposit names its seat and joins a strand of his own on the seat; a
     petition's names no matter and joins nothing on it; neither opens a strand.
 11. His own two deeds link; two strangers' deeds do not. NO ACT STORE IS READ: with the act store and the
     log replaced by stubs that raise, and their readers patched to raise, both functions still answer.
 12. CONTROL: after one season of `build_realm(0)`, `flows_in` (with `terminal_for`) and `presented` leave the
     hash and the log length where they were, and the reading of a few planted holders is the same read twice
     and leaves the hash where it was. His reading of a record claim does not move when the
     record changes hands, and a dead arrester is no phantom restraint.
 13. The study's 16 links (`strife_moves.yaml: links`): the loader reads 6 robust and 10 stable and refuses each
     bad document; the windowed count skips an uncoded move and stops at 3 coded moves; strands planted in a link's
     order read above the seeded shuffled-order control and the same strands scrambled read lower; the
     leave-and-rejoin profile is exact on hand-built strands; `strands_block` prints the lines on a real run.

CR-78 (batch B11-S4): THE STAMP -- `flow_stakes`, appended to `questions_for`'s splice behind `Fixtures
stamp_flow_stakes`, built off at commit (1) and SHIPPED ON at commit (2).
 14. EXIT (planted): a person aware of a rising at his settlement finds that rung and its holder among his occasions
     (classed on the question he answers, and verbs form on them) with the switch on, and not with it off; a strand
     he reads concluded stamps nothing; the opening kind does not change what is stamped.
 15. MUTATION: a stake of a class outside the closed set (`Enemy`, an unrostered class, or none) is refused; the
     same stake under the whole roster would have been stamped, so the refusal is the closed set's.
 16. CONTROL: the switch set off explicitly reproduces the base `build_realm(0)` hash and the one-season seed-0
     hash (EQUAL checks only: both are taken where the switch's effect is nil), with the term never computed and
     the switch read, which are what discriminate.
 17. `Strand.rung` is not a source of stakes: a strand naming only a person stamps that person, not the place where
     he lives now (the rung is stamped only when a strand names it as a referent).
 18. The closed set stamps an Office a strand names and refuses a Record it names.
Each loop asserts that it asserted (`CLAUDE.md` §0.1 pt 2).
"""
import pytest

from engine.season.data import affiliations as A
from engine.season.data.rosters import DETAIN_KIND
from engine.season.epistemic import act_refs, claim_subjects
from engine.season.harness import probes as P
from engine.season.harness import strife as H
from engine.season.queries import world_q as W
from engine.season.state.carriers import Act, Claim, Event, Person, Record, Rung, StateChange, Tenure
from engine.season.state.ids import ROOT


def _world():
    """`tiny_world` (R realm > D duchy > S settlement > Hh hearth) plus three more duchies, each with a settlement,
    so a move naming two settlements in two duchies is realm-wide; and a root `F` outside the realm with `p_far`."""
    w = P.tiny_world()
    n = [0]

    def edge(sub, obj, kind):
        n[0] += 1
        w.add_tenure(Tenure(f"t_cr76_{n[0]}", sub, obj, kind, 0))
    for d, s in (("D2", "S2"), ("D3", "S3"), ("D4", "S4")):
        w.rungs[d] = Rung(d, "duchy")
        w.rungs[s] = Rung(s, "settlement")
        edge(d, "R", "contain")
        edge(s, d, "contain")
    w.rungs["F"] = Rung("F", "territory")
    w.persons["p_far"] = Person("p_far", "a foreigner")
    w.rungs["p_far"] = Rung("p_far", "person")
    edge("p_far", "F", "contain")
    return w


def ev(w, eid, kind, subjects, actor=None, verb="tell", payload=None, tick=1):
    causes = [ROOT]
    if actor is not None:
        aid = f"a_{eid}"
        w.acts.append(Act(id=aid, actor=actor, verb=verb, payload=payload or {}))
        causes = [aid]
    e = Event(eid, kind, [StateChange(s, "set", "Event", "exists") for s in subjects], causes, tick)
    w.log.append(e)
    return e


def revert_cr78(monkeypatch):
    """CR-78 OFF, in process: the stamp's term stamps nobody (`flow_stakes` reads `()`), which is what the switch
    `stamp_flow_stakes` off does. A test that pins a hash from before CR-78 flipped it ON (a declared mover) calls this."""
    monkeypatch.setattr(W, "flow_stakes", lambda w_, p_, classes=None: ())


def _ceded_world():
    """`_world()` with a realm-wide defeat and its cession, both naming two parties: `(w, e1, e2)`."""
    w = _world()
    e1 = ev(w, "e1", "field.lost", ["S", "S2", "p_low", "p_mid"])
    e2 = ev(w, "e2", "rung.ceded", ["S", "S2", "p_low", "p_mid"], tick=2)
    return w, e1, e2


def _fake_war(monkeypatch, war=True):
    """Stand-ins: `p_low` and `p_mid` of two factions and, with `war`, the two at war. `at_war` is False for every
    pair the tree can build, and its own falsifier drives the real fold (`test_faction_q.py`); here the arm's
    WIRING is read through stand-ins for the owners."""
    monkeypatch.setattr(W, "faction_of", lambda w_, x: {"p_low": "fac_a", "p_mid": "fac_b"}.get(x))
    if war:
        monkeypatch.setattr(W, "at_war", lambda w_, a, b: {a, b} == {"fac_a", "fac_b"})


def test_two_realm_wide_events_while_an_era_is_open_read_as_one_era():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    ev(w, "e2", "field.lost", ["S3", "S4"], tick=2)
    fl = W.flows_in(w)
    assert len(fl.strands) == 2, fl.strands                         # they share no referent and no step
    assert all(s.rung == "R" for s in fl.strands)
    assert len(fl.eras) == 1 and not fl.eras[0].concluded
    assert set(fl.eras[0].strands) == {s.id for s in fl.strands} == {"e1", "e2"}
    assert W.open_era(fl) is fl.eras[0]


def test_a_terminal_move_with_no_open_referent_concludes_the_era_and_frees_the_slot():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    open_only = W.flows_in(w)
    assert W.open_era(open_only) is not None                        # the terminal missing: open
    ev(w, "e2", "rung.ceded", ["S", "S2"], tick=2)                  # `concludes` kind, realm-wide, links by S
    fl = W.flows_in(w)
    assert [e.concluded for e in fl.eras] == [True] and W.open_era(fl) is None
    (s,) = fl.strands
    assert W.concluded(w, s)
    ev(w, "e3", "field.lost", ["S3", "S4"], tick=3)                 # a realm-wide event after: a new era
    fl = W.flows_in(w)
    assert [e.concluded for e in fl.eras] == [True, False]


def test_a_strand_never_concludes_on_its_own_opening_move():
    w = _world()
    ev(w, "e1", "rung.seized", ["S"])
    fl = W.flows_in(w, terminal=lambda e, a: True)
    (s,) = fl.strands
    assert len(s.moves) == 1 and s.moves[0].terminal and not W.concluded(w, s)


def test_a_move_outside_the_realm_is_within_no_era():
    w = _world()
    ev(w, "e1", "field.lost", ["F"])                                # on the foreign root
    fl = W.flows_in(w)
    assert len(fl.strands) == 1 and fl.strands[0].rung == "F"       # a strand of its own
    assert fl.eras == ()                                            # foreign is never within an era
    ev(w, "e2", "field.lost", ["S", "S2"], tick=2)                  # control: a realm-wide move opens one
    (era,) = W.flows_in(w).eras
    assert [m.event for m in era.moves] == ["e2"]


def test_a_terminal_at_a_duchy_does_not_conclude_the_era():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    ev(w, "e2", "rung.ceded", ["S"], tick=2)                        # terminal, links by S, placed under D
    fl = W.flows_in(w)
    (s,) = fl.strands
    assert s.moves[-1].terminal and s.moves[-1].place != "R" and W.concluded(w, s)
    assert [e.concluded for e in fl.eras] == [False]                # the strand ends; the era does not


def test_a_one_move_realm_wide_terminal_leaves_the_era_open():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    fl = W.flows_in(w, terminal=lambda e, a: True)
    assert fl.strands[0].moves[0].terminal and fl.strands[0].moves[0].place == "R"
    assert [e.concluded for e in fl.eras] == [False]


def test_a_later_linked_move_reopens_a_concluded_strand():
    """Rule (b): the LATEST move decides. A terminal, then a linked non-terminal move: open again."""
    w = _world()
    ev(w, "e1", "field.lost", ["S"])
    ev(w, "e2", "rung.ceded", ["S"], tick=2)
    (s,) = W.flows_in(w).strands
    assert W.concluded(w, s)                                        # control: the terminal is latest
    ev(w, "e3", "field.lost", ["S"], tick=3)
    (s,) = W.flows_in(w).strands
    assert len(s.moves) == 3 and not s.moves[-1].terminal and not W.concluded(w, s)


def test_factions_not_at_war_leave_the_strand_concluded(monkeypatch):
    """The `at_war` arm's control: the parties have two factions, and the REAL owner finds them not at war."""
    w, _, _ = _ceded_world()
    _fake_war(monkeypatch, war=False)
    (s,) = W.flows_in(w).strands
    assert not W.at_war(w, "fac_a", "fac_b")
    assert W.open_referents(w, s.parties, s.referents) == [] and W.concluded(w, s)


def _mv(eid, ix, refs, place):
    return W.Move(eid, ix, "field.lost", None, frozenset(refs), place, True, False)


def _st(rung, *moves, parties=()):
    return W.Strand(moves[0].event, rung, tuple(moves), frozenset().union(*(m.referents for m in moves)),
                    frozenset(parties))


def test_presented_types_a_duchy_s_two_slots_and_groups_the_rest_under_the_era():
    """A1, A2 on a hand-built reading (`flows_in` merges any strand sharing a referent with an era move into
    that move's strand, so a duchy tributary is built here by hand). At duchy D: a TRIBUTARY (shares S2 with
    the era's realm-rung move), an ISOLATE that outranks it on moves, and a third strand that outranks the
    tributary on recency. Untyped, the top two by rank would be the isolate and the third; typed, the
    tributary and the isolate are presented and the third is grouped under the open era."""
    w = _world()
    era_move = _mv("e0", 0, {"S2", "S3"}, "R")
    era_strand = _st("R", era_move)
    trib = _st("D", _mv("t1", 1, {"S2"}, "S"))
    iso = _st("D", _mv("i1", 2, {"Hh"}, "Hh"), _mv("i2", 3, {"Hh"}, "Hh"))
    third = _st("D", _mv("x1", 4, {"D"}, "S"))
    era = W.Era("e0", (era_move,), ("e0",), False)
    fl = W.Flows((era_strand, trib, iso, third), (era,))
    assert sorted((trib, iso, third), key=W.slot_rank) == [iso, third, trib]
    slots, grouped = W.presented(w, fl)
    assert set(slots["D"]) == {"t1", "i1"} and len(slots["D"]) == W.flow_capacity("duchy") == 2
    assert grouped["x1"] == "e0" and grouped["e0"] == "e0"
    assert W.flow_capacity(W.REALM_KIND) == 1 and "R" not in slots


def test_incompatible_span_reads_a_true_pair_among_the_living_parties():
    w = _world()
    w.persons["p_low"].conviction = {"solmund_orthodoxy": 3}
    w.persons["p_mid"].conviction = {"thread_truth": 3}
    s = _st("D", _mv("m1", 0, {"S"}, "S"), parties=("p_low", "p_mid"))
    assert W.incompatible_span(w, s)
    w.persons["p_mid"].conviction = {"solmund_orthodoxy": 2}        # control: a shared affiliation
    assert not W.incompatible_span(w, s)


@pytest.mark.parametrize("arm", ["detain", "docket", "at_war"])
def test_an_open_referent_keeps_the_era_open(arm, monkeypatch):
    w, _, _ = _ceded_world()
    assert W.open_era(W.flows_in(w)) is None                        # control: with nothing open it concludes
    if arm == "detain":
        w.add_tenure(Tenure("t_cr76_held", "p_low", "off_duke", DETAIN_KIND, 0))
    elif arm == "docket":
        w.docket.append({"date": None, "matter": "S2", W.DOCKET_ARRANGEMENT: None, W.DOCKET_PETITION: None})
    else:
        _fake_war(monkeypatch)
    fl = W.flows_in(w)
    assert W.open_era(fl) is not None, arm
    assert W.open_referents(w, fl.strands[0].parties, fl.strands[0].referents), arm


def test_a_person_within_the_realm_flow_need_not_hold_any_of_its_moves():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    era = W.open_era(W.flows_in(w))
    persons, offices, _ = W.within(w, "R")                          # the era's rung is the realm
    moves = {m.event for m in era.moves}
    assert "p_other" in persons and not any(c.subject in moves or c.subject in {"S", "S2"}
                                            for c in w.persons["p_other"].ledger)
    assert "p_far" not in persons                                   # control: outside the realm, never within
    assert "off_duke" in offices


def _petition(w, rid, actor, terms, tick):
    w.records[rid] = Record(rid, "S", "petition", subject_matter={"terms": terms, "to": "p_high", "from": "S"})
    ev(w, f"e_{rid}", "petition.filed", [rid], actor=actor, verb="petition", payload={"subject": terms}, tick=tick)


def test_two_petitions_on_one_matter_open_a_strand_and_on_two_matters_none():
    same = _world()
    _petition(same, "rec_1", "p_low", "S", 1)
    assert W.flows_in(same).strands == ()                           # a lone petition is civic life
    _petition(same, "rec_2", "p_mid", "S", 2)
    (s,) = W.flows_in(same).strands
    assert [m.event for m in s.moves] == ["e_rec_1", "e_rec_2"] and s.moves[1].opens
    other = _world()
    _petition(other, "rec_1", "p_low", "S", 1)
    _petition(other, "rec_2", "p_mid", "S2", 2)
    assert W.flows_in(other).strands == ()


def test_a_content_opened_strand_is_open_at_birth_and_closes_on_a_later_terminal():
    """Both content-opener kinds are also `concludes` kinds; the move that content-opens is an opening move and
    is never terminal, so the movement two petitions make is open, a third keeps it open, and a later
    `matter.determined` on the matter (a `concludes` kind) with nothing open concludes it (the control)."""
    w = _world()
    assert set(W.CONTENT_OPENING_KINDS) <= W.CONCLUDING_KINDS            # the overlap the rule answers
    _petition(w, "rec_1", "p_low", "S", 1)
    _petition(w, "rec_2", "p_mid", "S", 2)
    (s,) = W.flows_in(w).strands
    assert len(s.moves) == 2 and not s.moves[-1].terminal and not W.concluded(w, s)
    _petition(w, "rec_3", "p_other", "S", 3)
    (s,) = W.flows_in(w).strands
    assert len(s.moves) == 3 and not W.concluded(w, s)
    ev(w, "e_det", "matter.determined", ["S"], tick=4)
    (s,) = W.flows_in(w).strands
    assert s.moves[-1].kind == "matter.determined" and W.concluded(w, s)


def test_a_linking_content_opener_still_takes_its_earlier_same_matter_move():
    """(i) The second petition links to a strand already open (same doer); the first petition, parked, is taken
    into that strand with it."""
    w = _world()
    ev(w, "e_seize", "rung.seized", ["S3"], actor="p_mid", verb="seize")
    _petition(w, "rec_1", "p_low", "S", 2)
    _petition(w, "rec_2", "p_mid", "S", 3)
    (s,) = W.flows_in(w).strands
    assert [m.event for m in s.moves] == ["e_seize", "e_rec_1", "e_rec_2"]


def test_a_taken_earlier_move_merges_the_strand_it_links_to():
    """(ii) The first petition (p_low) parks; p_low then seizes another rung (a strand of his); the second
    petition (p_mid) opens the movement and takes the first, which links to p_low's strand: ONE strand."""
    w = _world()
    _petition(w, "rec_1", "p_low", "S", 1)
    ev(w, "e_seize", "rung.seized", ["S3"], actor="p_low", verb="seize", tick=2)
    _petition(w, "rec_2", "p_mid", "S", 3)
    (s,) = W.flows_in(w).strands
    assert [m.event for m in s.moves] == ["e_rec_1", "e_seize", "e_rec_2"] and s.id == "e_rec_1"
    # The pulled prior is the earliest move but not the one the strand opened on: the harness prints the
    # first OPENING move's kind, on the strand's line and on its era's, never `moves[0]`'s.
    assert not s.moves[0].opens and s.moves[1].opens
    out = H.strands_block(w, 0, resolvable=frozenset())
    (line,) = [ln for ln in out if ln.startswith("    e_rec_1 ")]
    assert "opening rung.seized " in line, line
    (era_line,) = [ln for ln in out if ln.startswith("  era ")]
    assert era_line.endswith("opening kinds beneath: rung.seized"), era_line


def test_a_pulled_earlier_move_is_an_opening_move_and_never_closes_the_era():
    """A content opener's pulled prior is one of the movement's opening moves, so it is never terminal, though
    its kind is in `concludes`. p1 is placed at the realm (its terms under D3, the petition at S4) and links to
    nothing while the era `e1` is open; p2 on the same terms content-opens and pulls p1. The era stays open."""
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    w.records["rec_1"] = Record("rec_1", "S4", "petition", subject_matter={"terms": "S3", "to": "p_high", "from": "S4"})
    ev(w, "e_rec_1", "petition.filed", ["rec_1"], actor="p_low", verb="petition", payload={"subject": "S3"}, tick=2)
    fl = W.flows_in(w)
    assert len(fl.strands) == 1 and [(e.id, e.concluded) for e in fl.eras] == [("e1", False)]   # p1 parked
    _petition(w, "rec_2", "p_mid", "S3", 3)
    fl = W.flows_in(w)
    (s,) = [s for s in fl.strands if s.id == "e_rec_1"]
    assert [m.event for m in s.moves] == ["e_rec_1", "e_rec_2"] and s.moves[0].place == "R"   # at the realm
    assert [(e.id, e.concluded) for e in fl.eras] == [("e1", False)]
    assert not s.moves[0].terminal


@pytest.mark.parametrize("a, b, want", [
    ({"inner_tradition": 3}, {"thread_truth": 3}, 1),              # a `false` pair
    ({"altonian_civics": 2}, {"altonian_civics": 4}, 1),           # a shared affiliation (its pairs all null)
    ({"solmund_orthodoxy": 3}, {"thread_truth": 1}, -1),           # a `true` pair
    ({"solmund_orthodoxy": 3, "inner_tradition": 3}, {"thread_truth": 2}, -1),   # a `true` pair beside a `false`
    ({"solmund_orthodoxy": 3, "thread_truth": 1}, {"thread_truth": 2}, -1),      # a `true` pair beside a shared one
    ({"inner_tradition": 3}, {"einhir_restoration": 3}, 0),        # only `null` pairs
    ({}, {"thread_truth": 3}, 0),                                  # one holds none
    ({"thread_truth": 0}, {"solmund_orthodoxy": 5}, 0),            # 0 is not held
])
def test_commensurate(a, b, want):
    w = _world()
    w.persons["p_low"].conviction, w.persons["p_mid"].conviction = a, b
    assert W.commensurate(w, "p_low", "p_mid") == want == W.commensurate(w, "p_mid", "p_low")


def test_incompatibility_keeps_every_cell_and_incompatible_is_its_true_half():
    vals = set(A.INCOMPATIBILITY.values())
    assert vals == {True, False, None}
    assert A._load_incompatible() == A.INCOMPATIBLE


def test_the_route_check_names_a_planted_gap():
    from engine.season.loop.driver import resolvable_verbs
    ok = resolvable_verbs()
    def bare(resolvable):
        return set(H.routeless_pairs(H.opening_routes(H.MOVES, resolvable)))
    base = bare(ok)
    checked = 0
    for r in H.MOVES:
        if r["code"] not in H.terminal_codes(H.MOVES):
            continue
        verbs = {v for v, _ in H.route(r, ok)}
        if not verbs:
            continue
        lost = bare(ok - verbs) - base
        named = {(k, r["code"]) for k in H.opening_kinds() if H.opening_producers(k, ok - verbs)}
        assert named and named <= lost, r["code"]                   # every opening that still exists loses it
        checked += 1
    assert checked >= 10
    lost = bare(ok - {"requisition"}) - base
    assert {k for k, _ in lost} == {"requisition.taken"}             # the opening side, removed


def test_the_pair_profile_pairs_only_adjacent_single_code_moves():
    """C9b: a move with no code or several breaks the run; the codes either side of it are not adjacent."""
    assert H.pair_profile([[["A"], ["B", "C"], ["D"]]], shuffles=5) == []
    got = {p for p, _, _ in H.pair_profile([[["A"], ["B"], [], ["C"], ["D"], ["E"]]], shuffles=5)}
    assert got == {("A", "B"), ("C", "D"), ("D", "E")}               # control: pairs within each run


# --- CR-76: the study's 16 links and the leave-and-rejoin profile -------------------------------------------

def _links_doc():
    from engine.season.data.rosters import load_yaml
    from engine.season.harness import strife_data as D
    return load_yaml(D.STRIFE_MOVES_YAML.read_text(encoding="utf-8"))


def test_the_link_loader_reads_sixteen_links_and_refuses_each_bad_document():
    from engine.season.harness import strife_data as D
    links, flow = D.load_links()
    assert len(links) == 16 == len(D.load_links(_links_doc())[0])
    assert [l["tier"] for l in links].count("robust") == 6 and [l["tier"] for l in links].count("stable") == 10
    assert flow["leave_and_rejoin"] == 74 and flow["cases"] == 102

    def drop_last(d):
        d["links"].pop()

    def dup(d):
        d["links"][1] = dict(d["links"][0])

    def put(i, key, val):
        return lambda d: d["links"][i].__setitem__(key, val)

    bad = [(put(0, "a", "ZZ"), "no row"),                         # a code with no row
           (put(0, "a", "WA-R"), "side suffix"),                   # WA is not split by side
           (put(0, "b", "CA-X"), "side suffix"),                   # a suffix outside A/R/O
           (dup, "twice"),
           (put(0, "tier", "weak"), "tier"),
           (put(0, "cases", 99), "not counts"),                    # cases above `of`
           (drop_last, "not the study's 16"),
           (lambda d: d["links"].append(dict(d["links"][0], b="XE")), "not the study's 16")]
    checked = 0
    for mutate, why in bad:
        d = _links_doc()
        mutate(d)
        with pytest.raises(ValueError, match=why):
            D.load_links(d)
        checked += 1
    assert checked == len(bad) == 8


def test_a_window_of_three_coded_moves_skips_an_uncoded_move_and_reads_a_suffixed_link_at_its_base():
    one = [{"a": "CA-R", "b": "XE-R", "tier": "robust"}]
    def seen(seq):
        return H.link_profile([seq], one, shuffles=1)[0][1]
    assert seen([["CA"], [], ["X"], ["X"], ["XE"]]) == 1             # the empty move is skipped: XE is 3 coded moves on
    assert seen([["CA"], ["X"], ["X"], ["X"], ["XE"]]) == 0          # 4 on: outside the window
    assert seen([["XE"], ["CA"]]) == 0                               # a follows b, not the link's order
    assert seen([["CA", "XE"]]) == 0                                 # one move is not a before b
    assert seen([["CA"], ["XE"], ["CA"], ["XE"]]) == 1               # a strand is counted once, however many instances it holds


def test_a_link_with_an_end_no_strand_move_can_carry_prints_unreachable_and_an_empty_pair_prints_no_strand_carries_both():
    """DR, DA and FA reach no strand move (`_REACHABLE`), so a link on them reads 0 whatever the order: that is not
    `does not beat its control`. A link whose ends are reachable but which no strand shows says so; one that is shown and
    beaten by its control keeps the old words."""
    assert not ({"DR", "DA", "FA"} & H._REACHABLE) and {"CA", "XE", "IN"} <= H._REACHABLE   # the roster's own reach
    links = [{"a": "DR", "b": "IN", "tier": "robust"}, {"a": "CA-R", "b": "XE-R", "tier": "robust"},
             {"a": "WA", "b": "SB", "tier": "stable"}]
    seqs = [[["CA"], ["XE"]], [["SB"], ["WA"]]]
    lines = {ln.split()[0]: ln for ln in H.link_lines(seqs, links, shuffles=20) if " observed " in ln}
    assert len(lines) == 3
    assert "UNREACHABLE: DR" in lines["DR>IN"] and "does not beat" not in lines["DR>IN"]
    assert "UNREACHABLE" not in lines["CA-R>XE-R"] and "does not beat" not in lines["CA-R>XE-R"]
    assert "does not beat its control" in lines["WA>SB"]               # b before a in the one strand: observed 0, control above 0
    assert "no strand shows a then b" in H.link_lines([[["Z"]]], [links[1]], shuffles=5)[1]


def test_a_planted_real_order_reads_a_higher_windowed_count_than_the_same_strands_scrambled():
    """The card's falsifier: for each of the 16 links, strands planted in the link's order read above the seeded
    shuffled-order control, and the same strands scrambled (the pair reversed) read lower."""
    checked = 0
    for l in H.LINKS:
        a, b = H.base_code(l["a"]), H.base_code(l["b"])
        fill = [["Z1"], ["Z2"], ["Z3"], ["Z4"]]
        real = [[[a], [b]] + fill for _ in range(10)]
        scrambled = [[[b], [a]] + fill for _ in range(10)]
        ((_, r_obs, r_ctl),) = H.link_profile(real, [l], shuffles=100)
        ((_, s_obs, s_ctl),) = H.link_profile(scrambled, [l], shuffles=100)
        assert r_obs == 10 and r_obs > r_ctl > 0, (l, r_obs, r_ctl)
        assert s_obs == 0 and s_obs < r_obs, (l, s_obs)
        checked += 1
    assert checked == 16
    # the control is seeded: the same strands read the same control twice
    assert H.link_profile(real, [l], shuffles=20, seed=3) == H.link_profile(real, [l], shuffles=20, seed=3)


def test_the_flow_profile_counts_a_strand_that_leaves_and_rejoins_one_that_never_leaves_and_one_ending_off():
    ab_bc = [{"a": "A", "b": "B"}, {"a": "B", "b": "C"}]
    seqs = [[["A"], ["B"], ["X"], [], ["X"], ["X"], ["A"], ["B"]],     # on, on, off x3, on, on: leaves and rejoins
            [["A"], [], ["B"], ["C"]],                                 # on throughout
            [["A"], ["B"], ["X"], ["X"]],                              # leaves and ends off
            [[], []]]                                                   # no coded move: not a strand of the reading
    f = H.flow_profile(seqs, ab_bc)
    assert (f["strands"], f["left"], f["rejoined"], f["end_off"]) == (3, 2, 1, 1)
    assert f["departures"] == {"B": 2} and f["rejoins"] == {"A": 1}
    assert f["share"] == pytest.approx((4 / 7 + 1.0 + 2 / 4) / 3)
    assert H.flow_profile([], ab_bc)["strands"] == 0


def test_the_strands_block_prints_the_links_and_the_flow_profile_and_no_longer_says_not_transcribed():
    from engine.season.harness import populated
    w = populated.build_realm(0)
    populated.run(seasons=1, w=w)
    before = w.content_hash()
    out = H.strands_block(w, 0)
    text = "\n".join(out)
    assert "NOT TRANSCRIBED" not in text and w.content_hash() == before
    link_ln = [ln for ln in out if " robust observed " in ln or " stable observed " in ln]
    assert len(link_ln) == 16
    dead = [ln.split()[0] for ln in link_ln if "UNREACHABLE" in ln]
    assert sorted(dead) == ["DA>WA", "DR>IN", "WN>DA", "WN>FA"]      # exactly the links on DR, DA and FA
    assert any("strands that leave and rejoin the flow:" in ln for ln in out)
    assert any("the study's own figures (reference): 74 of 102" in ln for ln in out)


# --- CR-77: the person reading ------------------------------------------------------------------------------

_N = [0]


def hold(w, pid, subject, kind, when=1, chain=(), doer=None, value=True):
    """Deposit one claim in `pid`'s ledger in the event-kind shape WITNESS writes (`predicate = kind`)."""
    _N[0] += 1                  # zero-padded: question ids tie-break lexicographically, so deposit order must sort
    c = Claim(f"c_cr77_{_N[0]:06d}", pid, subject, kind, value, when, "told_by" if chain else "firsthand", 50,
              "own", chain=chain, doer=doer)
    w.persons[pid].ledger.append(c)
    return c


def witness(w, pid, e):
    """What a witness of `e` holds: one claim per subject of the real deposit rule (`claim_subjects`, the
    shipped `both`), each stamped `doer` only on his own act, as `loop/witness.py` does."""
    a = W.causing_act(w, e)
    subs = claim_subjects(w, e, "both", act_refs(a))
    for s in subs:
        hold(w, pid, s, e.kind, when=e.emitted_at, doer=pid if a is not None and a.actor == pid else None)
    return subs


def reading(w, pid):
    p = w.persons[pid]
    return [(s.referents, W.concluded_known(w, p, s)) for s in W.flows_known(w, p)]


def read_ids(w, p):
    """His reading by identity: each strand's id, its move ids, and whether he reads it concluded."""
    return [(s.id, tuple(m.event for m in s.moves), W.concluded_known(w, p, s)) for s in W.flows_known(w, p)]


def test_a_witness_and_a_hearsay_holder_of_the_same_events_read_different_flows():
    w = _world()
    e1 = ev(w, "e1", "field.lost", ["S", "S2"])
    e2 = ev(w, "e2", "rung.ceded", ["S", "S2"], tick=2)
    (world_strand,) = W.flows_in(w).strands
    assert W.concluded(w, world_strand)
    assert witness(w, "p_mid", e1) and witness(w, "p_mid", e2)
    hold(w, "p_low", "S", "field.lost", chain=("p_mid",))           # told one claim of the first event
    seen, heard = reading(w, "p_mid"), reading(w, "p_low")
    assert seen and all(done for _, done in seen), seen               # he saw the cession
    assert heard == [(frozenset({"S"}), False)], heard                # he heard only of the defeat
    assert seen != heard
    # the stated limit: the witness's claims of one Event are several moves, one per subject
    assert {r for r, _ in seen} == {frozenset({"S"}), frozenset({"S2"})}


def test_an_empty_ledger_reads_no_flow():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    assert W.flows_in(w).strands                                      # the world holds one
    assert W.flows_known(w, w.persons["p_low"]) == ()
    hold(w, "p_low", "S", "field.lost")                               # control: one claim, one strand
    assert len(W.flows_known(w, w.persons["p_low"])) == 1


def test_a_person_within_the_realm_flow_who_holds_none_of_its_moves_reads_no_realm_flow():
    w = _world()
    ev(w, "e1", "field.lost", ["S", "S2"])
    assert W.open_era(W.flows_in(w)) is not None
    persons, _, _ = W.within(w, "R")
    assert "p_other" in persons                                      # CR-76 lists him as within
    hold(w, "p_other", "S", "travel.moved")                           # a `never` kind on the same rung
    hold(w, "p_other", "S", "field.lost", value=False)                # a told denial is no move
    assert W.flows_known(w, w.persons["p_other"]) == ()
    hold(w, "p_mid", "S2", "field.lost")                              # control: holding a move, he reads it
    assert [s.referents for s in W.flows_known(w, w.persons["p_mid"])] == [frozenset({"S2"})]


def test_lacking_the_terminal_claim_he_reads_the_strand_open_while_concluded_reads_it_closed():
    w = _world()
    ev(w, "e1", "field.lost", ["S"])
    e2 = ev(w, "e2", "rung.ceded", ["S"], tick=2)
    (s,) = W.flows_in(w).strands
    assert W.concluded(w, s)
    hold(w, "p_low", "S", "field.lost")
    assert reading(w, "p_low") == [(frozenset({"S"}), False)]
    witness(w, "p_low", e2)                                           # control: the terminal lands, it closes
    assert reading(w, "p_low") == [(frozenset({"S"}), True)]


def test_holding_only_a_field_won_he_reads_the_strand_open_while_concluded_reads_it_closed():
    w = _world()
    ev(w, "e1", "field.lost", ["S"])
    ev(w, "e2", "field.won", ["S"], tick=2)
    # the world's terminal test is code-level (`harness/strife.py::terminal_for`: WA, the authority winning
    # the field, ends cases); a stand-in reads this `field.won` as that code.
    (s,) = W.flows_in(w, terminal=lambda e, a: e.kind == "field.won").strands
    assert W.concluded(w, s)
    hold(w, "p_low", "S", "field.won", when=2)
    assert reading(w, "p_low") == [(frozenset({"S"}), False)]
    hold(w, "p_low", "S", "field.lost", when=1)                       # both outcomes: still no `concludes` kind
    assert reading(w, "p_low") == [(frozenset({"S"}), False)]
    assert "field.won" not in W.CONCLUDING_KINDS


def test_his_restraint_arm_reads_the_custody_edge_and_never_the_arrester():
    """Named gap (1), the restraint arm: the arrest's deposit names the arrester and the custody edge, never
    the prisoner; a release names the edge too. A strand on the edge stays open until a release lands after
    the arrest; the arrester's strand is not held open by his own arrest. The terminal claims are planted:
    nothing that concludes names a custody edge in shipped play."""
    checked = 0
    for release_tick, want in ((None, False), (2, True), (0, False)):
        w = _world()
        w.add_tenure(Tenure("t_cust", "p_low", "off_duke", DETAIN_KIND, 1))
        arrest = ev(w, "e_arrest", "arrest.made", ["t_cust"], actor="p_mid", verb="arrest",
                    payload={"subject": "p_low"})
        subs = witness(w, "p_other", arrest)
        assert set(subs) == {"p_mid", "t_cust"}, subs                # the prisoner is not named
        if release_tick is not None:
            free = ev(w, "e_free", "detention.ended", ["t_cust"], actor="p_high", verb="pardon",
                      payload={"subject": "p_low"}, tick=release_tick)
            assert "t_cust" in witness(w, "p_other", free)
        for x in ("t_cust", "p_mid"):
            hold(w, "p_other", x, "transfer.made", when=3)
        got = {tuple(r): done for r, done in reading(w, "p_other")}
        assert got[("t_cust",)] is want, release_tick
        assert got[("p_mid",)] is True, release_tick                 # the arrester is not restrained
        # C16: an edge is told from a person by its Tenure kind, never by who still lives -- the arrester
        # dead (gone from the cast) is no phantom restraint, and the custody edge reads as before.
        w.persons.pop("p_mid")
        assert {tuple(r): done for r, done in reading(w, "p_other")} == got, release_tick
        checked += 1
    assert checked == 3


def test_his_reading_of_a_record_claim_does_not_move_when_the_record_changes_hands():
    """C17: the person reading places containment referents only. A record's place in the world is its live
    holder's (`place_of`), so moving the record's `hold` to a person under another root must not move his
    strand: no claim landed."""
    w = _world()
    w.records["rec_x"] = Record("rec_x", "S", "petition", subject_matter={"terms": "S", "to": "p_high", "from": "S"})
    hold(w, "p_low", "rec_x", "record.seized")
    before = [s.rung for s in W.flows_known(w, w.persons["p_low"])]
    assert W.place_of(w, "rec_x") == "S"                              # the world places it at its own rung
    w.add_tenure(Tenure("t_cr77_rec", "p_far", "rec_x", "hold", 1))
    assert W.place_of(w, "rec_x") == "F"                              # the world now places it with its holder
    assert [s.rung for s in W.flows_known(w, w.persons["p_low"])] == before == [None]


def test_his_reading_places_a_person_referent_by_the_live_containment_tree():
    """A STATED LIMIT (the CR-77 header, `_StrifeReading.place`), pinned so it is observed: a person referent is
    placed by his LIVE home (`home_map`), so when the arrester travels the holder's strand moves with him though
    no claim landed. The revert is named at the limit; this test fails when it is taken."""
    w = _world()
    hold(w, "p_other", "p_mid", "arrest.made")
    assert [s.rung for s in W.flows_known(w, w.persons["p_other"])] == ["Hh"]
    for t in w.tenures:
        if t.kind == "contain" and t.subject == "p_mid" and t.live:
            t.until = 2
    w.add_tenure(Tenure("t_cr77_travel", "p_mid", "S2", "contain", 2))
    assert [s.rung for s in W.flows_known(w, w.persons["p_other"])] == ["S2"]


def test_a_move_reads_each_record_s_about_key_and_no_other():
    """What a document is about is `person_q.ABOUT_KEYS[<kind>]` (`terms` for a dispensation or petition,
    `proposition` for a faction sheet), read by `_move_referents` and never `terms` off every kind: a faction
    sheet contributes its proposition, a `cover` (keyed `terms`, about nothing) contributes no terms, and a
    dispensation's terms are still read (the control)."""
    from engine.season.queries.person_q import ABOUT_KEYS
    w = _world()
    w.records["rec_sheet"] = Record("rec_sheet", "S", "faction_sheet", subject_matter={
        "proposition": "prop_x", "members": [], "holdings": [], "seats": [], "head": None})
    w.records["rec_cover"] = Record("rec_cover", "S", "cover", subject_matter={"terms": "S3"})
    w.records["rec_disp"] = Record("rec_disp", "S", "dispensation", subject_matter={"terms": "S2", "to": "p_low",
                                                                                     "at": "S"})
    assert ABOUT_KEYS["faction_sheet"] != "terms" and "cover" not in ABOUT_KEYS
    rd = W._StrifeReading(w)
    got = {rid: W._move_referents(rd, Event(f"e_{rid}", "record.seized",
                                            [StateChange(rid, "set", "Event", "exists")], [ROOT], 1), None)
           for rid in ("rec_sheet", "rec_cover", "rec_disp")}
    assert got == {"rec_sheet": {"rec_sheet", "prop_x"}, "rec_cover": {"rec_cover"},
                   "rec_disp": {"rec_disp", "S2"}}, got


@pytest.mark.parametrize("arm", ["docket", "at_war"])
def test_an_arm_with_no_ledger_source_does_not_hold_his_strand_open(arm, monkeypatch):
    """The docket and war arms (named gap (1)): the world reads the strand open, a docketed matter or the parties
    at war; he concludes on the terminal claim alone."""
    w, e1, e2 = _ceded_world()
    assert W.concluded(w, W.flows_in(w).strands[0])                   # control: with nothing open it concludes
    if arm == "docket":
        case = ev(w, "e_case", "case.opened", ["rec_case"], actor="p_high", verb="open_case",
                  payload={"subject": "p_low"}, tick=2)
        w.docket.append({"date": None, "matter": "p_low", W.DOCKET_ARRANGEMENT: None, W.DOCKET_PETITION: None})
    else:
        _fake_war(monkeypatch)
    (s,) = W.flows_in(w).strands
    assert not W.concluded(w, s), arm                                 # the world: open
    witness(w, "p_other", e1)
    witness(w, "p_other", e2)
    if arm == "docket":
        assert "p_low" not in witness(w, "p_other", case)            # the case's deposit names no matter
    seen = reading(w, "p_other")
    assert len(seen) >= 2 and all(done for _, done in seen), (arm, seen)


def test_a_petition_deposit_does_not_carry_its_matter_so_it_never_attaches_on_it():
    """Named gap (2), the petition half: the deposit names the filer and the minted Record, not the `terms`
    (`claim_subjects` adds the act's `subject` only for an Event that wrote nothing), so even with a strand of
    his own on the matter the petitions do not join it. He holds no strand the world opened by content."""
    w = _world()
    _petition(w, "rec_1", "p_low", "S", 1)
    _petition(w, "rec_2", "p_mid", "S", 2)
    assert len(W.flows_in(w).strands) == 1                            # the world opens the movement by content
    checked = 0
    for e in list(w.log):
        subs = witness(w, "p_other", e)
        assert "S" not in subs and any(r in subs for r in ("rec_1", "rec_2")), (e.id, subs)
        checked += 1
    assert checked == 2
    assert W.flows_known(w, w.persons["p_other"]) == ()               # two petitions open nothing for him
    hold(w, "p_other", "S", "compliance.withheld", when=0)            # an `opens` claim on the matter
    (s,) = W.flows_known(w, w.persons["p_other"])
    assert [m.kind for m in s.moves] == ["compliance.withheld"]      # the petitions stay outside it


def test_a_succession_deposit_carries_its_seat_and_attaches_only_to_a_strand_he_opened():
    """Named gap (2), the succession half: the deposit reads the `hold` it opens as its two ends, so it names
    the seat; it joins a strand of his own that names the seat, and opens none."""
    w = _world()
    w.add_tenure(Tenure("t_cr77_claim", "p_mid", "off_duke", "hold", 2))
    e = Event("e_succ", "succession.claimed", [StateChange("t_cr77_claim", "set", "Tenure", "since")], [ROOT], 2)
    w.log.append(e)
    assert "off_duke" in witness(w, "p_other", e)                     # the deposit names the seat
    assert W.flows_known(w, w.persons["p_other"]) == ()               # a joining kind alone opens nothing
    hold(w, "p_other", "off_duke", "record.seized", when=1)           # an `opens` claim naming the seat
    (s,) = W.flows_known(w, w.persons["p_other"])
    assert [m.kind for m in s.moves] == ["record.seized", "succession.claimed"]


def test_his_own_two_deeds_link_and_no_one_elses_do():
    for doer, strands in (("p_low", 1), (None, 2), ("p_mid", 2)):
        w = _world()
        hold(w, "p_low", "S", "rung.seized", when=1, doer=doer)
        hold(w, "p_low", "S3", "record.seized", when=2, doer=doer)
        assert len(W.flows_known(w, w.persons["p_low"])) == strands, doer


class _NoStore:
    """An act store or a log that refuses every read."""

    def _boom(self, *a, **k):
        raise AssertionError("the person reading read the act store or the log")
    __getattr__ = __iter__ = __len__ = __getitem__ = __contains__ = __bool__ = _boom


def test_the_person_reading_reads_no_act_store(monkeypatch):
    w = _world()
    e1 = ev(w, "e1", "rung.seized", ["S"], actor="p_low", verb="seize")
    e2 = ev(w, "e2", "rung.ceded", ["S", "S3"], tick=2)
    witness(w, "p_low", e1)
    witness(w, "p_low", e2)
    hold(w, "p_low", "S4", "record.seized", when=3, doer="p_low")
    # a custody edge he holds an arrest of: its referent is a RESTRAINT edge, so `open_referents_known` runs its
    # ledger scan under the stubs (rung referents return before it)
    w.add_tenure(Tenure("t_cust", "p_other", "off_duke", DETAIN_KIND, 1))
    witness(w, "p_low", ev(w, "e_arrest", "arrest.made", ["t_cust"], actor="p_mid", verb="arrest",
                           payload={"subject": "p_other"}))
    hold(w, "p_low", "t_cust", "transfer.made", when=3)
    p = w.persons["p_low"]
    want = read_ids(w, p)
    assert want and not all(done for _, _, done in want)              # the stubs below meet a real reading, one held open by the scan
    assert W.open_referents_known(w, p, {"t_cust"}) == [("restrained", "t_cust")]
    monkeypatch.setattr(w, "acts", _NoStore())
    monkeypatch.setattr(w, "log", _NoStore())
    from engine.season.state import attribution
    for mod in (W, attribution):
        for name in ("causing_act", "actor_of", "event_by_id"):
            monkeypatch.setattr(mod, name, _NoStore()._boom, raising=False)
    assert read_ids(w, p) == want


def test_concluded_known_refuses_a_strand_of_the_world_reading():
    w = _world()
    ev(w, "e1", "field.lost", ["S"])
    (s,) = W.flows_in(w).strands
    with pytest.raises(W.InstrumentDefect):
        W.concluded_known(w, w.persons["p_low"], s)


def test_control_the_realm_hash_holds_and_the_reading_is_the_same_read_twice():
    """The two readings over a REAL season: a hand-built world would miss the real log, act store and witness
    pipeline (ledgers ordered by landing, evicted, told at second hand), and the harness's code-level terminal
    test on a real log. At seed 0, one season, no ledger holds an `opens` claim (the world opens its strands by
    side and content only, `strife-01` §3 item 3), so every person reading is `()` as shipped (asserted); the
    read-twice control plants one `opens` claim under the first move claim of a few holders, so their real
    joining claims attach, and reads those holders twice."""
    from engine.season.harness import populated
    w = populated.build_realm(0)
    populated.run(seasons=1, w=w)
    before, n_log = w.content_hash(), len(w.log)
    # the world reading, with the harness's code-level terminal test, and its presentation write nothing
    fl = W.flows_in(w, H.terminal_for(w))
    W.presented(w, fl)
    assert fl.strands and w.content_hash() == before and len(w.log) == n_log
    # the measurement, asserted: no ledger holds an `opens` claim, so every person reading is `()`
    assert len(w.persons) > 10 and all(W.flows_known(w, p) == () for p in w.persons.values())
    holders = []
    for pid, p in sorted(w.persons.items()):
        first_move = next((c for c in p.ledger if c.predicate in W.MOVE_KINDS and c.value is True), None)
        if first_move is not None:                                    # landed first: same tick, round 0, front
            c = hold(w, pid, first_move.subject, "field.lost", when=first_move.when)
            p.ledger.remove(c)
            p.ledger.insert(0, c)
            holders.append(p)
        if len(holders) == 8:
            break
    planted, before = len(holders), w.content_hash()
    first = [read_ids(w, p) for p in holders]
    second = [read_ids(w, p) for p in holders]
    assert planted > 0 and any(len(m) > 1 for v in first for _, m, _ in v), planted
    assert first == second
    assert w.content_hash() == before                                 # the reading writes nothing


# --- CR-78: the stamp (commit (1) built it off; commit (2) ships it on) ------------------------------------------

#: Read on the base tree @60c27d08 (before CR-78) and again with the switch off: `build_realm(0).content_hash()`, and
#: the same realm after one season (`populated.run(seasons=1)`; CP-T03-08's `POST_ITEM[0]`).
BASE_BUILD = "03a79b0f76b7a91f09babd18f246be88"   # B01a.99 re-pin (every person's attributes are drawn): was 8480ad84...; B01 re-pin (B11 lane A, both commits rebased): was 600d8b27...
BASE_ONE_SEASON = "5cf205c09f80fd63937d82fc363c2f8a"   # B01a.99 re-pin (every person's attributes are drawn): was d796fd5e...; B01 re-pin (B11 lane A, both commits rebased): was 25660615...; RE-PINNED at the B10-13 pin commit (P15; same value as `test_season_weather.BASE_HASHES[1]`): was d4c83c8c... (CP-T03-08's `POST_ITEM[0]`). A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
STAMP = "stamp_flow_stakes"


def _switch(monkeypatch, w, on):
    monkeypatch.setitem(w.fixtures._v, STAMP, on)


def _rising(opening="rung.seized"):
    """`_world()` with a rising at `S`, the settlement over `p_low`'s hearth: `p_high`, who lives at `S`, holds it
    (a `hold` edge the stamp never reads), and `p_low` witnessed an opening move naming the rung and its holder
    (the real deposit rule, one claim per subject, linked into one strand by `p_high`'s place)."""
    w = _world()
    w.add_tenure(Tenure("t_hold_S", "p_high", "S", "hold", 0))
    assert witness(w, "p_low", ev(w, "e_rise", opening, ["S", "p_high"])) == ["S", "p_high"]
    return w


def _occasions(w, pid):
    """The classed referents of the question he answers, and the `(verb, subject)` pairs formed on it."""
    from engine.season.decision import assemble
    from engine.season.decision.options import opening_set
    p = w.persons[pid]
    q = W.questions_for(w, p)[0]
    return set(q.classes), {(c.verb, c.subject) for c in opening_set(p, assemble(p, q, 12), q, w.fixtures)}


def test_cr78_a_person_aware_of_a_rising_at_his_settlement_finds_that_rung_and_its_holder_only_with_the_switch_on(
        monkeypatch):
    w = _rising()
    p = w.persons["p_low"]
    (s,) = W.flows_known(w, p)
    assert s.rung == "S" and not W.concluded_known(w, p, s)          # he holds it open, at his settlement
    assert W.flow_stakes(w, p) == ("S", "p_high")
    stake = {("S", "Rung"), ("p_high", "Person")}
    _switch(monkeypatch, w, False)
    off_classes, off_formed = _occasions(w, "p_low")
    _switch(monkeypatch, w, True)
    on_classes, on_formed = _occasions(w, "p_low")
    assert not off_classes & stake, off_classes
    assert stake <= on_classes, on_classes
    # the stamp changes which verbs form for him: something forms on the holder, which nothing did before
    assert not any(subj == "p_high" for _, subj in off_formed), off_formed
    assert any(subj == "p_high" for _, subj in on_formed), on_formed
    assert off_formed < on_formed
    # nobody else: a person whose ledger holds no move is stamped nothing, the switch on
    assert W.flow_stakes(w, w.persons["p_other"]) == ()
    # the opening kind is never read: another `opens` kind stamps the same stakes
    checked = 0
    for kind in sorted(W.OPENS_KINDS - {"rung.seized"}):
        if kind in W.CONCLUDING_KINDS:
            continue
        wk = _rising(kind)
        assert W.flow_stakes(wk, wk.persons["p_low"]) == ("S", "p_high"), kind
        checked += 1
    assert checked >= 3, checked
    # a strand he reads concluded is not held open, so it stamps nothing
    witness(w, "p_low", ev(w, "e_cede", "rung.ceded", ["S"], tick=2))
    (s,) = W.flows_known(w, p)
    assert W.concluded_known(w, p, s)
    assert W.flow_stakes(w, p) == ()
    on_classes, _ = _occasions(w, "p_low")
    assert not on_classes & stake, on_classes


def test_cr78_a_stake_of_a_class_outside_the_closed_set_is_refused(monkeypatch):
    from engine.season.data.rosters import REFERENT_CLASSES
    from engine.season.data.verbs import ENEMY_CLASS
    assert W.FLOW_STAKE_CLASSES < REFERENT_CLASSES and ENEMY_CLASS not in W.FLOW_STAKE_CLASSES
    assert "Flow" not in REFERENT_CLASSES                             # no `Flow` class exists to be stamped
    w = _rising()
    p = w.persons["p_low"]
    _switch(monkeypatch, w, True)
    real = w.class_of
    checked = 0
    for planted in (ENEMY_CLASS, "Flow", None):
        monkeypatch.setattr(w, "class_of", lambda x, c=planted: c if x == "p_high" else real(x))
        # the same stake under the whole roster is stamped (the mutation the closed set excludes) ...
        if planted in REFERENT_CLASSES:
            assert "p_high" in W.flow_stakes(w, p, classes=REFERENT_CLASSES), planted
        # ... and under the closed set it is refused, and the rung beside it still stamped
        assert W.flow_stakes(w, p) == ("S",), planted
        classes, _ = _occasions(w, "p_low")
        assert ("S", "Rung") in classes and not any(o == "p_high" for o, _ in classes), (planted, classes)
        checked += 1
    assert checked == 3
    monkeypatch.setattr(w, "class_of", real)
    assert W.flow_stakes(w, p) == ("S", "p_high")                    # control: unplanted, the holder is stamped
    # a stake of no class at all: a custody edge's Tenure id, the only referent of an `arrest.made` strand
    w.add_tenure(Tenure("t_cust", "p_other", "off_duke", DETAIN_KIND, 1))
    hold(w, "p_mid", "t_cust", "arrest.made")
    pm = w.persons["p_mid"]
    assert [x.referents for x in W.flows_known(w, pm)] == [frozenset({"t_cust"})]
    assert w.class_of("t_cust") is None and W.flow_stakes(w, pm) == ()
    W.questions_for(w, pm)                                            # and the stamp site does not raise on it


def test_cr78_control_the_switch_off_reproduces_the_base_hash(monkeypatch):
    """The switch set off EXPLICITLY: the built realm and one season at seed 0 read the base tree's hashes (EQUAL
    checks; they hold with the switch on too, since the stamp's effect starts later or elsewhere), the term is
    never computed (a `flow_stakes` that raises is never reached), and the switch was read: those two discriminate."""
    from engine.season.harness import populated
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)
    w = populated.build_realm(0)
    _switch(monkeypatch, w, False)
    assert w.content_hash() == BASE_BUILD

    def _never(*a, **k):
        raise AssertionError("flow_stakes computed with the switch off")
    monkeypatch.setattr(W, "flow_stakes", _never)
    before = w.fixtures.reads.get(STAMP, 0)
    populated.run(seasons=1, w=w)
    assert w.fixtures.reads.get(STAMP, 0) > before
    assert w.content_hash() == BASE_ONE_SEASON


def test_cr78_strand_rung_is_not_a_source_of_stakes(monkeypatch):
    """`Strand.rung` is computed from the live home of every person a strand names (and is the realm root for a
    realm-wide strand, which no test here plants); it is no stake of the person's own reading, so it is not stamped."""
    w = _world()
    p = w.persons["p_low"]
    witness(w, "p_low", ev(w, "e_arrest", "rung.seized", ["p_high"]))
    (s,) = W.flows_known(w, p)
    assert s.rung is not None and s.referents == frozenset({"p_high"}), (s.rung, s.referents)
    assert W.flow_stakes(w, p) == ("p_high",), W.flow_stakes(w, p)      # the place he lives is no stake of its own
    assert s.rung not in W.flow_stakes(w, p)


def test_cr78_the_closed_set_stamps_an_office_and_refuses_a_record_a_strand_names():
    """The exclusions play can reach (`class_of` answers Person, Rung, Office, Site, Record or Proposition): an Office
    a strand names is a stake; a Record it names is not, though `class_of` knows it, so a class added to or removed
    from `FLOW_STAKE_CLASSES` is seen here."""
    w = _world()
    p = w.persons["p_low"]
    w.records["rec_1"] = Record("rec_1", "S", "petition", subject_matter={"terms": "S", "to": "p_high", "from": "S"})
    witness(w, "p_low", ev(w, "e_o", "rung.seized", ["off_duke", "rec_1"]))
    named = set().union(*(x.referents for x in W.flows_known(w, p)))
    assert {"off_duke", "rec_1"} <= named, named                       # the strands name both ...
    assert w.class_of("off_duke") == "Office" and w.class_of("rec_1") == "Record"
    assert W.flow_stakes(w, p) == ("off_duke",), W.flow_stakes(w, p)  # ... and only the Office is a stake
    assert "rec_1" in W.flow_stakes(w, p, classes=W.FLOW_STAKE_CLASSES | {"Record"})
