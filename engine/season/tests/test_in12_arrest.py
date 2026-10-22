"""Plan position IN-12 steps 5 and 5a (`workplans/valoria_master_workplan_v9_part5.md`), #453 §10.4 step 5 --
`arrest` and `pardon`, the loader's CLOSER CLAUSE, K-02's PARTY-GAP FOLD EDIT, and the charge (step 5a).

⚠ A PROPERTY, NOT A REALM COUNT. Every test drives the verbs on a HAND-BUILT world (`tiny_world`) through
the real fold (`SeasonDriver.resolve`); formation through the real `opening_set` / `pack_scenes`. The
realm and corpus executions are the batch's reading, not pinned here (v9 §0.5, *"Relax exit rules"*).

What each block proves, and the control that stops it passing vacuously:

  1. THE ROWS: resolvable, typed, `uncelled:`; `arrest` opens `detain`; `pardon` declares `[detain, ban]`.
  2. THE CLOSER CLAUSE (#453 §8.2): the load is red without `pardon`'s `[detain, ban]` (each kind named),
     and red on a domain naming a kind that needs no declared closer. CONTROL: the shipped table loads.
  3. K-02: a contested row may key two refusal kinds only where it keys `counterparty`; and the fold's
     party gap (S27.4, a pool under 1D, through the real fold) emits `arrest.refused` -- the counterparty
     kind -- never the union. CONTROL: the same act at pool 30 resolves to a band.
  4. THE OBSERVABLES, through the real fold: a warrant issued by `off_duke`, handed to a watchman, and his
     `arrest` through HIS seat opens `detain : prisoner -> off_duke` (THE ISSUING SEAT); the prisoner's
     `move` is `travel.blocked`; the Duke's `pardon` through `off_duke` ends it with `detention.ended` in
     `w.log`, and the same `move` then executes. CONTROLS: no warrant held -> `arrest.refused`; the
     watchman's `pardon` through his own seat is refused (no bench, and the edge is not his seat's).
  5. FORMATION: `arrest` forms on a referent a held warrant names and on no other.
  6. STEP 5a, THE CHARGE: a hand-built `HOLDS` Proposition about the accused, a petition naming it (its
     `terms`), and a witness's `commit` to it executing; the witness FORMS no such `commit` from the held
     petition -- the named residue `hole_register.yaml` H-227 records, observed rather than assumed.

MUTATIONS, run at the build 2026-10-22 (each RED, then restored and GREEN):
  * `loop/resolve.py::_refuse_party_gap` back to `row.emits_on_refusal` (the union) -> block 3's fold test
    RED (`['arrest.unauthorized', 'arrest.refused']`).
  * `data/verbs.py`'s K-02 narrowing dropped (`and COUNTERPARTY_CLAUSE not in by_clause`) -> the shipped
    table refuses to load (`arrest` keys two kinds): every test RED at import.
  * `pardon`'s `domain:` deleted -> block 2's first assertion IS that mutation, applied to the shipped
    table's own text (`_loads`), so it is run on every run rather than once by hand.
  * `loop/effects_migration.py::_eff_move`'s custody refusal (SC-03a's `restrained(..., DETAIN_KIND)`)
    switched off -> block 4's `travel.blocked` assertion RED (`['travel.moved']`).
  * `_eff_arrest`'s `_issuing_seat` replaced by `a.via` -> block 4's issuing-seat assertion RED.
"""

from __future__ import annotations

import copy
from unittest import mock

import pytest
import yaml

from ..data import verbs as VERBS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.rosters import PURSUIT_AXES, RESTRAINT_KINDS, table, table_meta
from ..data.verbs import _OPENERS_FROM_EFFECTS, COUNTERPARTY_CLAUSE, VERB_TABLE, WRITE_CLAUSE
from ..harness import probes as P
from ..loop import resolve as R
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..state.carriers import Act, Claim, Office, Question, Tenure
from .test_in10_record_operands import _acts, _formed, _hold_document

SEAT, DUKE = "off_duke", "p_high"
WATCH, WATCHMAN = "off_watch", "p_other"       # a second seat granting `dispatch` only, at `S`
PRISONER, FAR = "p_mid", "p_king"              # inside the duchy (Hh) / outside it (R)
OPENS = ("Overwhelming", "Success", "Partial")


def _world(**fx):
    """`tiny_world` plus a watch seat (`off_watch`, rung `S`, grant `dispatch`) held by `p_other`, the
    Duke knowing the prisoner (so his `issue` passes its `terms` conjunct), one MATTER barrier run."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    w.offices[WATCH] = Office(WATCH, "Watch", "S", ["dispatch"], faction="Crown")
    w.add_tenure(Tenure("t_watch", WATCHMAN, WATCH, "hold", since=0))
    for who in (PRISONER, FAR):
        w.persons[DUKE].ledger.append(Claim(f"c_knows_{who}", DUKE, who, "exists:Person", 1, 0,
                                            "firsthand", 100, "own"))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _act(key, verb, actor, via, **payload):
    return Act(id=key, actor=actor, verb=verb, via=via, payload=payload)


def _warrant_to_watchman(w, d, names=PRISONER):
    """The Duke ISSUES a warrant through `off_duke` whose `terms` names `names` (the real `issue`, so the
    Record has a creating Event), and it is handed to the watchman -- planted, as `give`'s own tests own
    the handing: the Duke's maker's `hold` closes and the watchman's opens."""
    assert _kinds(_fold(w, d, _act("w1", "issue", DUKE, SEAT, subject=names, to=PRISONER))) \
        == ["dispensation.issued"]
    rid = "rec:w1"
    for t in w.tenures:
        if t.kind == "hold" and t.object == rid and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_w_watch", WATCHMAN, rid, "hold", since=w.tick))
    return rid


def _restraints(w, who=PRISONER, kind="detain"):
    return [t for t in w.tenures if t.kind == kind and t.subject == who]


# ======================================================================================
# 1 -- THE ROWS
# ======================================================================================

def test_in12_5_arrest_and_pardon_are_resolvable_typed_uncelled_rows():
    rv = resolvable_verbs()
    assert {"arrest", "pardon"} <= rv
    a, p = VERB_TABLE["arrest"], VERB_TABLE["pardon"]
    assert a.eligibility == ("remit:dispatch",) and a.counterparty == "subject" and a.contests == "a standing"
    assert a.writes_at("Success") == ("Tenure.since",) and a.writes_at("Failure") == ()
    assert a.refusal_for(COUNTERPARTY_CLAUSE) == ("arrest.refused",)
    assert set(a.emits_on_refusal) == {"arrest.unauthorized", "arrest.refused"}, "K-02: two kinds"
    assert "arrest" in _OPENERS_FROM_EFFECTS["detain"], _OPENERS_FROM_EFFECTS["detain"]
    assert p.eligibility == ("remit:determine",) and not p.contests and p.writes == ("Tenure.until",)
    assert p.emits == ("detention.ended", "ban.ended") and p.emits_on_refusal == ("pardon.refused",)
    assert p.requires_typed is not None, "typed on seize's precedent"
    cells, uncelled = table("alignment"), table_meta("alignment")["uncelled"]
    for verb in ("arrest", "pardon"):
        assert verb in uncelled and not [ax for ax in PURSUIT_AXES if verb in cells[ax]], verb


# ======================================================================================
# 2 -- THE CLOSER CLAUSE, AND 3a -- K-02 AT THE LOADER
# ======================================================================================

_SRC = yaml.safe_load(VERBS.VERB_TABLE_YAML.read_text())


def _loads(mutate):
    """`_load_verb_table` over the shipped table with `mutate` applied; the SystemExit text, or None."""
    doc = copy.deepcopy(_SRC)
    mutate(doc)
    with mock.patch.object(VERBS, "VERB_TABLE_YAML") as fake:
        fake.exists.return_value = True
        fake.read_text.return_value = yaml.safe_dump(doc, allow_unicode=True)
        try:
            VERBS._load_verb_table()
        except SystemExit as e:
            return str(e)
    return None


def _row(doc, verb):
    return next(r for r in doc["verbs"] if r["verb"] == verb)


def test_in12_5_the_closer_clause_is_green_only_while_pardon_declares_detain_and_ban():
    assert _loads(lambda doc: None) is None, "CONTROL: the shipped table loads"
    msg = _loads(lambda doc: _row(doc, "pardon").pop("domain"))
    assert msg and "['ban', 'detain']" in msg and "closer clause" in msg, msg
    msg = _loads(lambda doc: _row(doc, "pardon").update(domain=["detain"]))
    assert msg and "['ban']" in msg, msg
    msg = _loads(lambda doc: _row(doc, "pardon").update(domain=["detain", "ban", "hold"]))
    assert msg and "'hold'" in msg and "needs a declared closer" in msg, msg
    assert RESTRAINT_KINDS == frozenset({"detain", "ban"})


def test_in12_5_k02_a_contested_row_keys_two_kinds_only_where_it_keys_counterparty():
    def strip_counterparty(doc):
        r = _row(doc, "arrest")
        r.pop("counterparty")
        r["emits_on_refusal"].pop("counterparty")
    msg = _loads(strip_counterparty)
    assert msg and "'arrest'" in msg and "keys no `counterparty`" in msg, msg
    # and a row that keys it may carry two kinds (`determine` given back its pre-SC-03b split)
    msg = _loads(lambda doc: _row(doc, "determine")["emits_on_refusal"].update(
        eligibility=["determine.unauthorized"]))
    assert msg is None, msg


# ======================================================================================
# 3b -- K-02 IN THE FOLD
# ======================================================================================

def test_in12_5_the_party_gap_emits_the_counterparty_kind_not_the_union():
    """S27.4 (a pool under 1D) reaches `_refuse_party_gap` through the real fold; the act was admitted
    (eligible, a person, a second party), so the kind is the counterparty clause's, `arrest.refused`, and
    not the union that would publish `arrest.unauthorized` for a seat that WAS authorized. CONTROL: the
    same act at pool 30 resolves to a band (the refusal is the pool's)."""
    for pool, refused in ((0, True), (30, False)):
        w, d = _world(pool_default=pool)
        _warrant_to_watchman(w, d)
        out = _fold(w, d, _act("a1", "arrest", WATCHMAN, WATCH, subject=PRISONER))
        assert len(out) == 1, _kinds(out)
        if refused:
            assert _kinds(out) == ["arrest.refused"] and out[0].degree is None, _kinds(out)
            assert not _restraints(w)
        else:
            assert out[0].degree is not None, _kinds(out)
    # the one body, asked directly: a keyed row's counterparty kind; a flat row's union, unchanged
    w, d = _world()
    a = _act("pg", "arrest", WATCHMAN, WATCH, subject=PRISONER)
    assert _kinds(R._refuse_party_gap(d, w, a)) == ["arrest.refused"]
    t = _act("pg2", "speak", WATCHMAN, None, subject=PRISONER)
    assert _kinds(R._refuse_party_gap(d, w, t)) == list(VERB_TABLE["speak"].emits_on_refusal)


# ======================================================================================
# 4 -- THE OBSERVABLES, THROUGH THE REAL FOLD
# ======================================================================================

def test_in12_5_arrest_opens_custody_on_the_issuing_seat_blocks_move_and_pardon_ends_it():
    w, d = _world(pool_default=30)
    _warrant_to_watchman(w, d)
    out = _fold(w, d, _act("a1", "arrest", WATCHMAN, WATCH, subject=PRISONER))
    assert _kinds(out) == ["arrest.made"] and out[0].degree in OPENS, (_kinds(out), out[0].degree)
    assert [e for e in w.log if e.kind == "arrest.made"]
    edge, = _restraints(w)
    assert edge.live and edge.object == SEAT, edge          # THE ISSUING SEAT, not the watch's
    # the prisoner's own journey is refused while the custody is live (SC-03a's reader)
    assert _kinds(_fold(w, d, _act("mv", "move", PRISONER, None, to="S"))) == ["travel.blocked"]
    # a second arrest of a man already held is declined at the write (one live `detain` per prisoner)
    again = _fold(w, d, _act("a2", "arrest", WATCHMAN, WATCH, subject=PRISONER))
    assert _kinds(again) in (["arrest.refused"], ["arrest.resisted"]), _kinds(again)
    assert len(_restraints(w)) == 1
    # CONTROL: the arresting seat cannot pardon -- no bench (no `determine`), and not the edge's object
    assert _kinds(_fold(w, d, _act("p0", "pardon", WATCHMAN, WATCH, subject=PRISONER))) \
        == ["pardon.refused"]
    assert edge.live
    # the issuing seat's bench pardons: `detention.ended`, and the prisoner travels again
    assert _kinds(_fold(w, d, _act("p1", "pardon", DUKE, SEAT, subject=PRISONER))) == ["detention.ended"]
    assert not edge.live and [e for e in w.log if e.kind == "detention.ended"]
    assert _kinds(_fold(w, d, _act("mv2", "move", PRISONER, None, to="S"))) == ["travel.moved"]
    # a pardon with nothing left to end is refused at its write
    assert _kinds(_fold(w, d, _act("p2", "pardon", DUKE, SEAT, subject=PRISONER))) \
        == list(VERB_TABLE["pardon"].refusal_for(WRITE_CLAUSE))


def test_in12_5_control_no_held_warrant_no_custody():
    """CONTROLS, each one change from the admitted arrest: the warrant names another man; the watchman
    holds no warrant at all (the Duke keeps his); a prisoner outside the watch's purview."""
    w, d = _world(pool_default=30)
    _warrant_to_watchman(w, d, names=FAR)
    assert _kinds(_fold(w, d, _act("a1", "arrest", WATCHMAN, WATCH, subject=PRISONER))) \
        == ["arrest.refused"]
    w, d = _world(pool_default=30)
    assert _kinds(_fold(w, d, _act("w1", "issue", DUKE, SEAT, subject=PRISONER, to=PRISONER))) \
        == ["dispensation.issued"]
    assert _kinds(_fold(w, d, _act("a1", "arrest", WATCHMAN, WATCH, subject=PRISONER))) \
        == ["arrest.refused"]
    assert not _restraints(w)


def test_in12_5_pardon_ends_a_revocation_ban_through_the_revoking_seat():
    """`pardon`'s closure basis reaches every restraint whose object is the exercised seat, not only
    `arrest`'s: a `ban` on `off_duke` (planted, as IN-31's revocation would open it) ends with `ban.ended`
    -- its own kind, so no ended custody is published."""
    w, d = _world()
    w.add_tenure(Tenure("t_ban", PRISONER, SEAT, "ban", since=0))
    assert _kinds(_fold(w, d, _act("p1", "pardon", DUKE, SEAT, subject=PRISONER))) == ["ban.ended"]
    assert not _restraints(w, kind="ban")[0].live


# ======================================================================================
# 5 -- FORMATION
# ======================================================================================

def _arrests(w, referents, who=WATCHMAN):
    q = Question("q:arrest", "claim_landed", tuple(referents), None)
    return [c for c in _formed(w, who, q) if c.verb == "arrest"]


def test_in12_5_arrest_forms_only_on_a_person_a_held_warrant_names():
    w, d = _world(pool_default=30)
    _hold_document(w, w.persons[WATCHMAN], "dispensation",
                   {"terms": PRISONER, "to": [WATCHMAN], "at": None}, rec_id="rec_held")
    (cand,) = _arrests(w, (PRISONER, FAR))
    assert cand.subject == PRISONER
    (act,) = _acts(w, WATCHMAN, [cand])
    assert act.verb == "arrest" and act.via == WATCH, (act.verb, act.via)
    w2, _ = _world()
    assert _arrests(w2, (PRISONER, FAR)) == [], "CONTROL: formed with no warrant held"


# ======================================================================================
# 6 -- STEP 5a, THE CHARGE
# ======================================================================================

def test_in12_5a_a_hand_built_charge_a_petition_naming_it_and_a_witness_commit():
    """#453 §8.1 Charge: no new carrier -- an `utter` of a `HOLDS` Proposition whose `subject` is the
    accused, named by an accusation `petition`'s `terms` (`record_sourced_operands`' petition row), and a
    witness's testimony as his own `commit` to it. Hand-built: a computed `utter` mints `OUGHT` (the
    `mood` source #453 names as the residue). The witness FORMS no `commit` from the held petition: a
    petition is no held-writ occasion (`RECORD_REFERENT_KINDS`), so `terms_sourced` cannot name it --
    H-227, observed here."""
    w, d = _world()
    accuser, witness = DUKE, WATCHMAN
    assert _kinds(_fold(w, d, _act("u1", "utter", accuser, None, proposition="prop_charge",
                                   mood="HOLDS", subject=PRISONER, predicate="murdered the reeve",
                                   value=True))) == ["proposition.uttered"]
    charge = w.propositions["prop_charge"]
    assert charge.mood == "HOLDS" and charge.subject == PRISONER
    assert _kinds(_fold(w, d, _act("pt1", "petition", accuser, None, subject="prop_charge", to=witness,
                                   **{"from": "S"}))) == ["petition.filed"]
    assert w.records["rec:pt1"].subject_matter["terms"] == "prop_charge"
    _hold_document(w, w.persons[witness], "petition", w.records["rec:pt1"].subject_matter,
                   rec_id="rec:pt1")
    q = Question("q:charge", "claim_landed", ("rec:pt1",), None)
    # `commit` forms on the question's own referent (the petition, refused in the fold: no Proposition)
    # and never on what the petition SAYS -- the charge
    assert not [c for c in _formed(w, witness, q) if c.verb == "commit" and c.subject == "prop_charge"], \
        "H-227 closed? a witness now forms `commit` on the charge from a held petition -- update the hole"
    out = _fold(w, d, _act("c1", "commit", witness, None, subject="prop_charge"))
    assert _kinds(out) == ["commitment.made"], _kinds(out)
    assert [t for t in w.tenures if t.kind == "commit" and t.subject == witness
            and t.object == "prop_charge" and t.live]
