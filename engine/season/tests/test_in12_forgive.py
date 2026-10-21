"""Plan position IN-12 step 13 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.4 step 13 --
`forgive`: a person removes his own stance rows held against a referent (#453 §9.4, K-41, K-49), the
closer of the grudge `march` plants on every loser of a lost field (`loop/effects_combat.py::_eff_march`).
No fade (#453 R-9 (a), adopted by the plan): nothing else ends a stance row.

⚠ A PROPERTY, NOT A REALM COUNT. Every test drives a HAND-BUILT world (`build_realm(0)`, the fixture
`test_march.py` fights its 2-v-6 lost field on) through the real fold (`SeasonDriver.resolve` /
`.encounter`) and the real formation (`opening_set`); NO TEST HERE ASSERTS THAT `forgive` EXECUTED IN THE
SEED-0 REALM (v9 §0.5, RULED 2026-10-13 *"Relax exit rules"*). The realm count the plan keys to
field-planted rows is `field_planted_forgivenesses`, below: proven non-vacuous here on a hand-built world
(it reads 1 for the field's grudge and 0 for a seeded row), and READ, not asserted, on the realm (the
realm fights no field, H-149 / H-175, so it is expected 0).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW: resolvable, `own`, `beneficiary: subject`, no precondition, writes `Person.stance` (the
     matrix row `march` already produces), emits `stance.moved` (so `KIND_VERB` maps that kind here),
     refusal `forgive.refused`, declared `uncelled:` with its reason.
  2. THE FALSIFIER (#453 §10.4 step 13, verbatim: *"a hand-built `forgive` after a `field.lost` leaves
     `stance_toward(p, F) == 0` and a `stance.moved` in `w.log`; refused where no negative row exists"*):
     `p_npc_033` marches on `set_s_036` and loses; he holds a grudge row against the winner F; his
     `forgive` naming F leaves `stance_toward(p, F) == 0` and logs a `stance.moved` whose change is his
     stance and whose cause is the forgive act. CONTROL: before the forgive, `stance_toward(p, F) < 0`;
     the other loser's grudge, the forgiver's morale row toward his own faction and his seeded rows stay.
  3. REFUSED WHERE NO NEGATIVE ROW EXISTS: a second forgive of F, a forgive of a referent held only in a
     positive row, and of one held in no row, each `forgive.refused`, and the stance does not move.
  4. EVERY ROW AGAINST THE REFERENT ENDS (K-49): beside the field's grudge, a second negative row toward F
     (a seeded disloyalty's shape) ends with it. MUTATION, run in-test: the effect ending only the first
     row it holds against F leaves `stance_toward(p, F) != 0`.
  5. THE PERSON-SIDE DECLINE (`rosters.yaml: own_stance_declines`): before the field, `p_npc_033` forms no
     `forgive` of F; after it he does; a referent held only in positive rows forms none. The loader refuses
     a member naming no verb or a verb that writes no `Person.stance`.
  6. THE REALM COUNTER, KEYED TO FIELD-PLANTED ROWS (#453 §9.4's falsifier, K-49): 1 after the field case,
     0 after a forgive of a seeded row only.

MUTATIONS, run at the build 2026-10-21 (each RED, then restored and GREEN):
  * `loop/effects_combat.py::_eff_forgive` returning `NO_CHANGE` always -> blocks 2, 4 and 6 RED.
  * `queries/person_q.py::held_against` dropping its `valence < 0` clause (every row naming the referent)
    -> block 3's positive-row arm and block 5's positive-row arm RED.
  * `decision/options.py::opening_set`'s `own_stance_declines` narrowing deleted -> block 5 RED.
  * block 4's mutation is run in-test (`monkeypatch`).
"""

from __future__ import annotations

import pytest

from ..data import verbs as VERBS
from ..data.matrix import Step, WriteClass
from ..data.rosters import PURSUIT_AXES, table, table_meta
from ..data.verbs import KIND_VERB, VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness.populated import build_realm
from ..loop import effects_combat
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries import person_q as PQ
from ..queries.world_q import holder_faction_of
from ..state.attribution import causing_act
from ..state.carriers import Act, Question
from ..state.gate import seat_faction

LOSER, OTHER_LOSER = "p_npc_033", "p_npc_035"     # Crown, mustered at set_s_014: the 2 of the 2-v-6
TARGET, VIA = "set_s_036", "off_npc_033"          # the Church of Solmund holds it with 6 defenders
WINNER, OWN = "fac_church_of_solmund", "fac_crown"
SEEDED = "p_npc_020"                              # LOSER's seeded rows name him negative, OTHER_LOSER's positive
FIELD_KINDS = ("field.won", "field.lost")


def _fold(w, *acts, encounter=False):
    """Fold `acts` through the real driver (RESOLVE, then ENCOUNTER where asked) and LOG what it emits --
    `test_march.py::_fold_one`'s sequence, with the events appended to `w.log` as a season does."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    depth = w.fixtures.get("contest_max_depth")
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts), depth)
    if encounter:
        out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, depth)
    w.log.extend(out)
    return out


def _lost_field():
    """`build_realm(0)` with the grudge weight swept off the morale weight (so the two rows differ by
    value, `test_march.py`'s reason), after `LOSER` marches on `TARGET` and loses."""
    w = build_realm(0)
    w.fixtures = w.fixtures.sweep("field_grudge_weight", 3)
    out = _fold(w, Act(id="m1", actor=LOSER, verb="march", payload={"subject": TARGET}, via=VIA),
                encounter=True)
    assert ("field.lost", "Lost") in [(e.kind, e.degree) for e in out], "precondition: no field was lost"
    return w


def _forgive(w, subject, key="f1", actor=LOSER):
    return _fold(w, Act(id=key, actor=actor, verb="forgive", payload={"subject": subject}))


def _kinds(events):
    return [e.kind for e in events]


def field_planted_forgivenesses(w) -> int:
    """THE REALM COUNT #453 §9.4 KEYS TO FIELD-PLANTED ROWS (K-49): the `forgive` executions -- logged
    `stance.moved` Events -- whose actor was a LOSER of an earlier logged field (a `field.won` /
    `field.lost` Event naming his stance among its changes) and whose `subject` is one of that field's two
    sides (`seat_faction` of the march's seat, `holder_faction_of` its target). A bare count would observe
    only morale and seeded rows (CLAUDE.md §0.1 pt 2). The losers are the field Event's changes that name a
    casualty field (`_eff_march`'s `fields`, whose first entry the change carries). The sides are read when the count is taken, not as
    the field was fought [ASSUMPTION; medium; Jordan to correct; revert: carry the planted referents on the
    field Event] -- a holder moving between the field and the forgiveness would miss a row."""
    planted: set = set()
    n = 0
    for e in w.log:
        a = causing_act(w, e)
        if a is None:
            continue
        if e.kind in FIELD_KINDS:
            sides = {seat_faction(w, a.via), holder_faction_of(w, (a.payload or {}).get("subject"))} - {None}
            # A loser's change names the FIRST field the casualty writes (`body`, or `stance` under the
            # `none` casualty model); an arriving mover's change names no field, and he planted nothing.
            for c in e.changes:
                if c.field in ("body", "stance"):
                    planted |= {(c.subject, s) for s in sides}
        elif e.kind == "stance.moved" and a.verb == "forgive":
            n += (a.actor, (a.payload or {}).get("subject")) in planted
    return n


# ======================================================================================
# 1 -- THE ROW
# ======================================================================================

def test_forgive_is_a_resolvable_own_verb_writing_stance_and_is_declared_uncelled():
    row = VERB_TABLE["forgive"]
    assert row.eligibility == ("own",)
    assert row.beneficiary == "subject" and not row.counterparty and not row.contests
    assert row.stratum == "social"
    assert row.writes == ("Person.stance",)
    assert row.emits == ("stance.moved",) and tuple(row.emits_on_refusal) == ("forgive.refused",)
    assert row.requires_typed is None, "no precondition (#453 §9.4)"
    assert "forgive" in resolvable_verbs()
    assert KIND_VERB.get("stance.moved") == "forgive", "`stance.moved` has one emitter, this row"
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    assert str(uncelled.get("forgive") or "").strip()
    assert not [ax for ax in PURSUIT_AXES if "forgive" in cells[ax]]


# ======================================================================================
# 2 -- THE FALSIFIER
# ======================================================================================

def test_a_forgive_after_a_lost_field_leaves_stance_toward_the_winner_zero_and_logs_stance_moved():
    w = _lost_field()
    p, other = w.persons[LOSER], w.persons[OTHER_LOSER]
    grudge = w.fixtures.get("field_grudge_weight")
    assert PQ.stance_toward(p, WINNER) == -1.0 * grudge, "control: the lost field planted no grudge"
    assert all(float(v) < 0 for ref, v, _ in p.stance if ref == WINNER), "a positive row would confound"
    kept = [row for row in p.stance if row[0] != WINNER]
    assert (OWN, -1.0, w.fixtures.get("field_morale_weight")) in kept, "control: no morale row"
    other_before = list(other.stance)

    out = _forgive(w, WINNER)
    assert _kinds(out) == ["stance.moved"], _kinds(out)
    assert PQ.stance_toward(p, WINNER) == 0, f"the grudge outlived the forgive: {p.stance}"
    assert list(p.stance) == kept, "a row not held against the winner moved"
    assert list(other.stance) == other_before, "another person's rows moved"
    (e,) = [e for e in w.log if e.kind == "stance.moved"]
    assert [(c.subject, c.field) for c in e.changes] == [(LOSER, "stance")]
    assert causing_act(w, e).id == "f1"


# ======================================================================================
# 3 -- REFUSED WHERE NO NEGATIVE ROW EXISTS
# ======================================================================================

@pytest.mark.parametrize("actor,subject,why", [
    (LOSER, WINNER, "a second forgive of a grudge already ended"),
    (OTHER_LOSER, SEEDED, "a referent held only in positive rows"),
    (LOSER, TARGET, "a referent held in no row"),
])
def test_a_forgive_with_nothing_held_against_the_referent_is_refused(actor, subject, why):
    w = _lost_field()
    if why.startswith("a second"):
        assert _kinds(_forgive(w, subject, key="f0", actor=actor)) == ["stance.moved"]
    before = list(w.persons[actor].stance)
    assert _kinds(_forgive(w, subject, actor=actor)) == ["forgive.refused"], why
    assert list(w.persons[actor].stance) == before, why


# ======================================================================================
# 4 -- EVERY ROW AGAINST THE REFERENT ENDS (K-49)
# ======================================================================================

def _two_rows_against_the_winner():
    w = _lost_field()
    p = w.persons[LOSER]
    p.stance = list(p.stance) + [(WINNER, -2, 1)]       # a seeded disloyalty's shape beside the grudge
    assert len(PQ.held_against(p, WINNER)) == 2
    return w, p


def test_every_row_held_against_the_referent_ends_whatever_wrote_it():
    w, p = _two_rows_against_the_winner()
    assert _kinds(_forgive(w, WINNER)) == ["stance.moved"]
    assert PQ.held_against(p, WINNER) == () and PQ.stance_toward(p, WINNER) == 0


def test_mutation_ending_only_the_first_row_fails_the_falsifier(monkeypatch):
    monkeypatch.setattr(effects_combat, "held_against", lambda p, r: PQ.held_against(p, r)[:1])
    w, p = _two_rows_against_the_winner()
    assert _kinds(_forgive(w, WINNER)) == ["stance.moved"]
    assert PQ.stance_toward(p, WINNER) != 0, "the mutation did not observe the second row"


# ======================================================================================
# 5 -- THE PERSON-SIDE DECLINE
# ======================================================================================

def _forgives_formed(w, pid, referent):
    p = w.persons[pid]
    q = Question("q:forgive", "claim_landed", (referent,), None)
    return [c for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "forgive"]


def test_a_person_forms_forgive_only_on_a_referent_he_holds_a_row_against():
    w = build_realm(0)
    assert _forgives_formed(w, LOSER, WINNER) == [], "a forgive formed before any grudge was held"
    w = _lost_field()
    assert [c.subject for c in _forgives_formed(w, LOSER, WINNER)] == [WINNER]
    assert _forgives_formed(w, OTHER_LOSER, SEEDED) == [], "formed on a referent held only in positive rows"
    assert _forgives_formed(w, LOSER, TARGET) == [], "formed on a referent held in no row"


def test_an_own_stance_declines_member_naming_no_verb_or_a_verb_not_writing_stance_is_refused_at_load():
    assert VERBS._load_own_stance_declines(["forgive"]) == VERBS.OWN_STANCE_DECLINES == {"forgive"}
    for planted in (["no_such_verb"], ["tend"], [""]):
        with pytest.raises(Forbidden, match="own_stance_declines"):
            VERBS._load_own_stance_declines(planted)


# ======================================================================================
# 6 -- THE REALM COUNTER, KEYED TO FIELD-PLANTED ROWS
# ======================================================================================

def test_the_field_planted_count_reads_the_fields_grudge_and_not_a_seeded_row():
    w = _lost_field()
    assert field_planted_forgivenesses(w) == 0
    assert _kinds(_forgive(w, SEEDED, key="f_seeded")) == ["stance.moved"], "control: a seeded row ends"
    assert field_planted_forgivenesses(w) == 0, "a seeded row's forgiveness counted as a field's"
    assert _kinds(_forgive(w, WINNER)) == ["stance.moved"]
    assert field_planted_forgivenesses(w) == 1
