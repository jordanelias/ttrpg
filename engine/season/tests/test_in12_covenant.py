"""Plan position IN-12 step 7 (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.4 step 7 --
`covenant`: a seat mints a `dispensation` whose `terms` is an uttered Proposition (K-54), hands it on by
`give`, and the addressee accepts by his own `commit`, FORMED FROM THE HELD DISPENSATION.

⚠ A PROPERTY, NOT A REALM COUNT. Every test drives the chain on a HAND-BUILT world through the real
formation (`questions_for` -> `opening_set`), the real packer (`pack_scenes`) and the real fold
(`SeasonDriver.resolve`), and WITNESS's real content deposit; NO TEST HERE ASSERTS THAT `covenant`
EXECUTED IN THE SEED-0 REALM (v9 §0.5, RULED 2026-10-13 *"Relax exit rules"*).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROW: resolvable, `remit:issue` only, counterparty `to`, mints through the shared mint (so it
     opens the maker's `hold`), declared `uncelled:` with its reason (not celled by the producer).
  2. THE MINT, THROUGH THE REAL FOLD: a `covenant` exercised through a seat granting `issue` writes
     `covenant.offered` and a `dispensation` whose `terms` is the Proposition and whose `to` is the
     counterparty, held by the maker alone. CONTROLS, each ONE change: the subject is no Proposition
     (a person); the counterparty is the maker; no seat exercised.
  3. THE FALSIFIER (#453 §10.4 step 7, verbatim: *"the addressee's `commit` to the covenant's
     Proposition, formed from the held dispensation after a `give`"*): utter -> covenant -> give ->
     WITNESS -> the addressee's own `questions_for` -> `opening_set` -> `pack_scenes` -> the fold, and
     `commitment.made` on the Proposition is in `w.log` with his live `commit` edge. CONTROL: the same
     addressee BEFORE the give forms no `commit` on it (the route is the held Record, not the
     utterance).
  4. THE ROUTE IS A ROSTER LINE, AND THE LOADER POLICES IT: `rosters.yaml: terms_sourced` names `commit`;
     with it emptied the falsifier's formation is gone (the MUTATION, run in-test); a line naming a kind
     no held writ is stamped as, no kind, or no verb is refused by its loader.

MUTATIONS, run at the build 2026-10-20 (each RED, then restored and GREEN):
  * `decision/options.py::opening_set`'s `terms_sourced` widening deleted (equivalently `TERMS_SOURCED`
    emptied, which block 4 does in-test) -> block 3's falsifier RED (no `commit` Candidate on the
    Proposition).
  * `loop/effects_information.py::_eff_covenant` minting with the content's `terms` replaced by the
    counterparty -> block 2's mint assertion and block 3's falsifier RED.
"""

from __future__ import annotations

import pytest

from ..data import verbs as VERBS
from ..data.matrix import WriteClass
from ..data.rosters import PURSUIT_AXES, table, table_meta
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..decision import assemble
from ..decision import options as OPT
from ..decision.options import opening_set
from ..gaps import Forbidden
from ..harness import probes as P
from ..queries import world_q
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..queries.world_q import hold_force, questions_for
from ..state.carriers import Act
from .test_in10_record_operands import _acts, _resolve

SEAT, DUKE = "off_duke", "p_high"          # grants `issue`; seated at S
OTHER = "p_king"                           # the counterparty, moved to S so a `give` can reach him


def _kinds(events):
    return [e.kind for e in events]


def _world():
    """`tiny_world` at a MATTER barrier, the counterparty standing where the Duke stands (S) so the
    `give`'s `with` conjunct admits him -- the one edit to the fixture, made on his own edges."""
    w = P.tiny_world()
    for t in w.persons[OTHER].tenures:
        if t.live and t.kind in ("contain", "reside"):
            t.object = "S"
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _utter(w, d, key="cv_u"):
    assert _kinds(_resolve(w, d, Act(id=key, actor=DUKE, verb="utter"))) == ["proposition.uttered"]
    return f"prop:{key}"


def _covenant(subject, to=OTHER, via=SEAT, key="cv_c", actor=DUKE):
    return Act(id=key, actor=actor, verb="covenant", via=via, payload={"subject": subject, "to": to})


def _live(w, pid, obj):
    return sorted(t.kind for t in w.persons[pid].tenures if t.object == obj and t.live)


# ======================================================================================
# 1 -- THE ROW
# ======================================================================================

def test_covenant_is_a_resolvable_remit_issue_verb_that_opens_hold_and_is_declared_uncelled():
    row = VERB_TABLE["covenant"]
    assert row.eligibility == ("remit:issue",), "an `own` alternative would let anyone mint a treaty (K-14)"
    assert row.beneficiary == "to" and row.counterparty == "to"
    assert row.stratum == "social", "a `binding_decision` row's kinds are chronicled by kind"
    assert row.writes == ("Record.exists", "Record.stages")
    assert row.emits == ("covenant.offered",)
    assert "covenant" in resolvable_verbs()
    assert "covenant" in _OPENERS_FROM_EFFECTS["hold"], _OPENERS_FROM_EFFECTS["hold"]
    assert row.requires_typed.known_person_operands() == ("to",), "the counterparty fans over known persons"
    # IN-08: declared `uncelled:` with a reason, and keyed on no axis
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    assert str(uncelled.get("covenant") or "").strip()
    assert not [ax for ax in PURSUIT_AXES if "covenant" in cells[ax]]


# ======================================================================================
# 2 -- THE MINT, THROUGH THE REAL FOLD
# ======================================================================================

def test_a_covenant_mints_a_dispensation_naming_the_proposition_held_by_its_maker_alone():
    w, d = _world()
    pid = _utter(w, d)
    assert _kinds(_resolve(w, d, _covenant(pid))) == ["covenant.offered"]
    rec = w.records["rec:cv_c"]
    assert rec.kind == "dispensation"
    assert rec.subject_matter["terms"] == pid
    assert list(rec.subject_matter["to"]) == [OTHER]
    assert rec.rung == w.offices[SEAT].rung, "drawn up at the exercised seat's rung"
    assert rec.stages, "the term is wound (H-80's default for an act declaring none)"
    assert hold_force(w, "rec:cv_c").subject == DUKE, "the mint holds only the maker (K-54)"
    assert _live(w, OTHER, "rec:cv_c") == []
    assert [e for e in w.log if e.kind == "covenant.offered"]


def test_control_a_subject_that_is_no_proposition_is_refused_and_mints_nothing():
    w, d = _world()
    n = len(w.records)
    assert _kinds(_resolve(w, d, _covenant("p_mid"))) == ["covenant.refused"]
    assert len(w.records) == n


def test_control_a_covenant_with_oneself_is_refused():
    w, d = _world()
    pid = _utter(w, d)
    n = len(w.records)
    assert _kinds(_resolve(w, d, _covenant(pid, to=DUKE))) == ["covenant.refused"]
    assert len(w.records) == n


def test_control_no_seat_exercised_is_not_a_covenant():
    w, d = _world()
    pid = _utter(w, d)
    n = len(w.records)
    assert _kinds(_resolve(w, d, _covenant(pid, via=None))) == ["covenant.refused"]
    assert len(w.records) == n


# ======================================================================================
# 3 -- THE FALSIFIER: THE ADDRESSEE'S `commit`, FORMED FROM THE HELD DISPENSATION AFTER A `give`
# ======================================================================================

def _commits_formed(w, pid):
    """The addressee's own deliberation, as the loop runs it: his questions (`questions_for`, which
    stamps the writs he holds), each one's option set, the `commit` Candidates naming `pid`."""
    p = w.persons[OTHER]
    out = []
    for q in questions_for(w, p):
        out += [c for c in opening_set(p, assemble(p, q, 12), q, w.fixtures)
                if c.verb == "commit" and c.subject == pid]
    return out


def _covenant_then_give(w, d):
    pid = _utter(w, d)
    assert _kinds(_resolve(w, d, _covenant(pid))) == ["covenant.offered"]
    # CONTROL, BEFORE THE GIVE: the addressee holds nothing, so nothing names the Proposition to him.
    assert _commits_formed(w, pid) == [], "a commit formed before the instrument reached him"
    gave = _resolve(w, d, Act(id="cv_g", actor=DUKE, verb="give",
                              payload={"subject": "rec:cv_c", "to": OTHER}))
    assert _kinds(gave) == ["record.given"]
    d.witness(mint_token(w, WriteClass.INTERIOR), gave)       # the receiver reads what he was handed
    assert hold_force(w, "rec:cv_c").subject == OTHER
    return pid


def test_the_addressees_commit_to_the_covenants_proposition_forms_from_the_held_dispensation():
    w, d = _world()
    pid = _covenant_then_give(w, d)
    cands = _commits_formed(w, pid)
    assert cands, "the addressee formed no commit on the covenant's Proposition after the give"
    (act,) = _acts(w, OTHER, cands[:1])
    assert act.verb == "commit" and act.payload["subject"] == pid
    assert _kinds(_resolve(w, d, act)) == ["commitment.made"]
    made = [e for e in w.log if e.kind == "commitment.made"]
    assert made, "no `commitment.made` in w.log"
    assert "commit" in _live(w, OTHER, pid), _live(w, OTHER, pid)


# ======================================================================================
# 4 -- THE ROUTE IS A ROSTER LINE, AND THE LOADER POLICES IT
# ======================================================================================

def test_mutation_without_the_terms_sourced_line_the_addressee_forms_no_commit(monkeypatch):
    """THE NAMED MUTATION, RUN IN-TEST: `terms_sourced` emptied (the reader in `opening_set` then
    widens nothing) and the falsifier's formation is gone -- the route is that line, nothing else.
    Since v10 CP-T02-05 a SECOND route reaches the same addressee: the held dispensation names the covenant's
    OUGHT Proposition, so `world_q.oughts_named` stamps it as a cause he has heard of and `commit` forms on it
    from that stamp too. This test isolates the `terms_sourced` route by stubbing the OTHER one for both its
    arms; the heard-of route has its own falsifier (`test_cp_t02_05_oughts_named.py`)."""
    w, d = _world()
    monkeypatch.setattr(world_q, "oughts_named", lambda *a, **k: ())
    pid = _covenant_then_give(w, d)
    assert _commits_formed(w, pid), "precondition: the shipped route forms it"
    monkeypatch.setattr(OPT, "TERMS_SOURCED", {})
    assert _commits_formed(w, pid) == [], "a commit on the Proposition formed with the route removed"


def test_a_terms_sourced_line_naming_no_held_writ_kind_is_refused_at_load():
    """The loader `TERMS_SOURCED` is built by (`data/verbs.py::_load_terms_sourced`), on planted maps.
    `petition` is a kind `record_sourced_operands` maps `subject` for but `writs_held` never stamps (no
    row declaring `referent_class: Record` asks for it), so a commit routed through it would form for
    nobody. CONTROL: the shipped line loads to what the module holds."""
    assert VERBS._load_terms_sourced({"commit": ["dispensation"]}) == VERBS.TERMS_SOURCED
    assert VERBS.TERMS_SOURCED == {"commit": ("dispensation",)}
    for planted in ({"commit": ["petition"]}, {"commit": []}, {"no_such_verb": ["dispensation"]}):
        with pytest.raises(Forbidden, match="terms_sourced"):
            VERBS._load_terms_sourced(planted)
