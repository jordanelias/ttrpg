"""v11 CR-87 -- VIOLENCE MADE EXCEPTIONAL (ED-IN-0335 to ED-IN-0337, ED-IN-0340; commit `c7145842`).

Six parts, each read here through the code that carries it:
  (1) `rosters.yaml: violence_contexts` -- a person-side formation decline: `fight` forms on a subject only where the actor
      holds a context against him (`decision/options.py::violence_context_of`: war, crime, duel, defence);
  (2) `fight`'s alignment cells -0.3 on all seven axes, `accept` takes `fight`'s, `challenge` keeps its own;
  (3) the grudge's bound: `decision/choose.py::stance_term` reads `Fixtures hostile_stance_gain` on a violent opponent row;
  (4) a computed duel is fought to `blood` (`rosters.yaml: duel_terms`' `accept` line), and `challenge` asks a DISPUTE
      (`data/requires.py`'s `dispute` stem, `person_q.holds_dispute`);
  (5) build-time loyalty writes toward the creed, never its head person, no lower than the member band;
  (6) the coercion rows keep their gates (`capture` is not declined).

  FALSIFIER: seed 0, season 1, read through `harness/interactions.py`'s own run: `fight` formations on same-faction persons
  at stance >= -3 are 0 (read on the base, PC-10b's tree: 110 `fight` formations, 68 same-faction, 65 of them at stance
  >= -3; the plan's 104 / 74 were read on an earlier tree), and the Cardinal->Senior-Inquisitor and
  Spymaster->King formations are 0; hand-built war, crime (a warrant addressed to him; a detainee), duel and defence
  contexts each form a `fight`, and with none it does not.
  MUTATION: the decline emptied (`VIOLENCE_CONTEXTS` = {}), the realm forms `fight` on same-faction persons again.
  CONTROL: the block empty and every value at its revert reproduce the pre-item hash exactly (`build_realm(0)` and one
  season at seed 0, the hashes given at the base, after PC-10b).
"""
from __future__ import annotations

import dataclasses

import pytest

from ..data import verbs as V
from ..data.cast import MEMBER_BAND, loyalty_in_band
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.requires import WORLD_ONLY_STEMS, AllOf, TypedRequires
from ..data.rosters import PURSUIT_AXES, roster_map
from ..decision import choose as CH
from ..decision import options as O
from ..decision.options import opening_set
from ..epistemic import Seen
from ..harness import interactions as I
from ..harness import populated
from ..harness import probes as P
from ..loop.witness import content_value
from ..queries import person_q, world_q
from ..queries.person_q import SEEN_PREDICATE
from ..seam.wrappers import combat
from ..state.carriers import Claim, Proposition, Question, Tenure, View
from .test_cp_t03_02_band_ending_and_body import revert_cp_t03_02
from .test_cr85_faculty_replaces_history import revert_cr85
from .test_cp_t03_04_arms import revert_cp_t03_04
from .test_cp_t03_07_body_ceiling import revert_cp_t03_07

A, B = "p_mid", "p_low"          # `probes.tiny_world`: both at the hearth `Hh`
BASE_BUILD = "837d0f83c62917b88d69da3daa3ea027"     # build_realm(0).content_hash(), after PC-10b (the pre-item base)
BASE_SEASON = "0fb73bc805ae699a0a13b8d09e130e1c"    # one season, seed 0, after PC-10b
CARDINALS = {"off_cardinal_fortitude", "off_cardinal_justice", "off_cardinal_prudence", "off_cardinal_temperance"}


# ------------------------------------------------------------------------------------------------
# (1) THE DECLINE, ON A HAND-BUILT WORLD


def _q(*classes) -> Question:
    return Question("q:cr87", "need", (B,), B, classes=tuple(classes))


def _fights(w, q) -> list:
    p = w.persons[A]
    v = View(A, [], w.fixtures.get("view_k"), q)
    return [c for c in opening_set(p, v, q, w.fixtures) if c.verb == "fight" and c.subject == B]


def _hold(w, holder: str, rid: str, kind: str, content: dict) -> None:
    """A held Record as `held_record_claims` reads it: the holder's live `hold` and his content claim."""
    w.add_tenure(Tenure(f"t_{rid}", holder, rid, "hold", since=0))
    w.persons[holder].ledger.append(Claim(f"c_{rid}", holder, rid, f"content:{kind}", content_value(content), 0,
                                          "firsthand", 100, "own"))


def test_with_no_context_fight_does_not_form_and_the_question_still_forms_other_acts():
    w = P.tiny_world()
    assert not _fights(w, _q())
    p = w.persons[A]
    q = _q()
    others = opening_set(p, View(A, [], w.fixtures.get("view_k"), q), q, w.fixtures)
    assert others, "the question formed nothing at all: the decline's absence-of-fight would read nothing"


def test_war_context_an_enemy_stamp_forms_fight():
    w = P.tiny_world()
    assert _fights(w, _q((B, V.ENEMY_CLASS)))


def test_crime_context_a_warrant_addressed_to_him_forms_fight_and_one_he_only_made_does_not():
    w = P.tiny_world()
    kind = next(iter(set(V.WARRANT_SOURCED.values())))
    _hold(w, A, "rec:w1", kind, {"terms": B, "to": (B,), "at": None})       # he made it; it charges B's addressee
    assert not _fights(w, _q()), "the maker of a writ about B is not charged with it (the addressee test)"
    _hold(w, A, "rec:w2", kind, {"terms": B, "to": (A,), "at": None})
    assert _fights(w, _q())


def test_crime_context_a_detainee_stamp_forms_fight():
    w = P.tiny_world()
    assert _fights(w, _q((B, V.DETAINEE_CLASS)))


def test_duel_context_a_held_challenge_naming_both_forms_fight_and_one_naming_a_third_does_not():
    w = P.tiny_world()
    _hold(w, A, "rec:c0", "challenge", {"terms": "p_other", "to": ("p_other",), "stakes": None, "challenger": A})
    assert not _fights(w, _q())
    _hold(w, A, "rec:c1", "challenge", {"terms": B, "to": (B,), "stakes": None, "challenger": A})
    assert _fights(w, _q())


def _attacked(w, when: int, doer: str = B) -> None:
    """What WITNESS deposits when `doer` wounds A where A sees it: the deed claim on its patient and the sighting."""
    led = w.persons[A].ledger
    led.append(Claim(f"c_wound_{when}", A, A, "body.changed", True, when, "firsthand", 100, "own"))
    led.append(Claim(f"c_seen_{when}", A, A, SEEN_PREDICATE, Seen(stratum="contested_physical", who=doer), when,
                     "firsthand", 100, "own"))


def test_defence_context_an_attack_he_saw_this_season_forms_fight_and_an_older_one_does_not():
    w = P.tiny_world()
    _attacked(w, when=0)
    w.persons[A].ledger.append(Claim("c_later", A, "Hh", "stores:grain", 8, 1, "firsthand", 100, "own"))
    assert not _fights(w, _q()), "an attack in an older season than his newest claim is no defence"
    w = P.tiny_world()
    _attacked(w, when=0)
    assert _fights(w, _q())
    assert person_q.attackers_of(w.persons[A].ledger, A, O._OPPONENT_DEED_KINDS) == {B}


def test_mutation_the_decline_emptied_forms_fight_with_no_context(monkeypatch):
    w = P.tiny_world()
    assert not _fights(w, _q())
    monkeypatch.setattr(O, "VIOLENCE_CONTEXTS", {})
    assert _fights(w, _q()), "with the decline deleted, the context-free fight forms again"


def test_the_roster_is_refused_at_import_for_an_unknown_verb_and_the_reader_set_is_closed():
    from ..gaps import Forbidden
    with pytest.raises(Forbidden):
        V._load_violence_contexts({"no such verb": ["war"]})
    with pytest.raises(Forbidden):
        V._load_violence_contexts({"fight": []})
    assert set(V.VIOLENCE_CONTEXTS["fight"]) <= set(O.VIOLENCE_CONTEXT_READERS)
    assert V.VIOLENT_VERBS == {v for v, r in V.VERB_TABLE.items() if r.contests in set(V.roster("violent_prizes"))}


# ------------------------------------------------------------------------------------------------
# (1) THE WAR STAMP, ON THE REALM, DRIVEN BY A WAR PROPOSITION AND A LIVE COMMIT


def test_enemies_heard_stamps_the_other_faction_only_once_he_knows_of_a_live_war():
    w = populated.build_realm(0)
    me = "p_npc_033"                                    # the Spymaster (a Valorsmark officer)
    mine = world_q.faction_holding(w, me)
    other = next(f for f in sorted({world_q.faction_holding(w, x) for x in w.persons} - {None, mine}))
    assert world_q.enemies_heard(w, w.persons[me]) == ()
    w.propositions["prop:war:test"] = Proposition("prop:war:test", world_q.WAR_MOOD, mine, "", other, 0)
    assert world_q.enemies_heard(w, w.persons[me]) == (), "no live commit: no war"
    w.add_tenure(Tenure("t_war_commit", "p_npc_020", "prop:war:test", "commit", since=0))
    assert world_q.enemies_heard(w, w.persons[me]) == (), "a live war he has not heard of is no context"
    w.persons[me].ledger.append(Claim("c_war_heard", me, "prop:war:test", "proposition.uttered", True, 0,
                                      "firsthand", 100, "own"))
    foes = world_q.enemies_heard(w, w.persons[me])
    assert foes and all(world_q.faction_holding(w, f) == other for f in foes)
    q = world_q.questions_for(w, w.persons[me])[0]
    assert set(q.referents_for(V.ENEMY_CLASS)) == set(foes)


# ------------------------------------------------------------------------------------------------
# (2) A COST ON EVERY AXIS; (3) THE GRUDGE'S BOUND; (4) BLOOD AND THE DISPUTE


def test_fight_and_accept_cost_on_every_axis_and_challenge_keeps_its_own_cells():
    for ax in PURSUIT_AXES:
        assert V.ALIGNMENT[ax].get("fight") == -0.3, ax
        assert V.ALIGNMENT[ax].get("accept") == -0.3, ax
    assert V.ALIGNMENT["grandiose_humble"]["challenge"] == -0.6
    assert V.ALIGNMENT["deontological_instrumental"]["challenge"] == -0.3


def _grudge(w, valence=-1, weight=4):
    w.persons[A].stance.append((B, valence, weight))


def test_the_grudge_on_a_violent_row_reads_hostile_stance_gain_and_on_any_other_row_one_plus_stance_gain():
    w = P.tiny_world()
    _grudge(w)
    p = w.persons[A]
    from ..state.carriers import Candidate
    fx = DEFAULT_FIXTURES.sweep("hostile_stance_gain", 0.5)
    fight = Candidate("fight", B)
    arm = CH._stance_arm(p, fight, fx, None)
    assert arm > 0, "a grudge pulls `fight` up under `declared` (CR-16's sign kept)"
    assert CH.stance_term(p, fight, fx) == 0.5 * arm
    revert = DEFAULT_FIXTURES.sweep("hostile_stance_gain", None)
    assert CH.stance_term(p, fight, revert) == (1.0 + revert.get("stance_gain")) * arm
    speak = Candidate("speak", B)                      # an opponent row, not violent: untouched
    assert CH.stance_term(p, speak, fx) == (1.0 + fx.get("stance_gain")) * CH._stance_arm(p, speak, fx, None)


def test_a_grudge_in_a_war_context_still_ranks_fight_first_at_the_shipped_bound():
    """The reading rule's second arm: at the shipped `hostile_stance_gain`, a -4 grudge in a war context still makes
    `fight` the person's best-scored act on the question about his enemy."""
    w = P.tiny_world()
    _grudge(w)
    p, q = w.persons[A], _q((B, V.ENEMY_CLASS))
    fx = w.fixtures
    cands = opening_set(p, View(A, [], fx.get("view_k"), q), q, fx)
    memo = CH.deliberation_memo(p, fx)
    scores = {id(c): sum(CH.score_terms(p, c, fx, memo, None)[:2]) for c in cands}
    best = max(cands, key=lambda c: scores[id(c)])
    assert best.verb == "fight" and best.subject == B, [(c.verb, c.subject, scores[id(c)]) for c in cands]


def test_a_computed_duel_is_fought_to_blood_and_named_stakes_still_govern():
    assert combat.duel_terms_of("accept", None) == "blood"
    assert combat.duel_terms_of("accept", "death") == "death"
    assert combat.duel_terms_of("fight", None) is None, "an unchallenged fight keeps the engine's lethal default"


def test_the_dispute_is_a_world_only_stem_answered_off_the_actors_own_judgement():
    """A deed claim of B's that A's own pursuits score against him is a dispute; one they score for him is not.
    `fight.declared` names its doer as its subject (no pairing), and `liberty` judges it -0.33, `honour` +0.93."""
    assert "dispute" in WORLD_ONLY_STEMS
    w = P.tiny_world()
    rd = world_q.WorldReader(w, A)
    assert rd.read(B, f"dispute:{A}") is False, "no deed claim of B's: no dispute"
    assert rd.read(B, f"dispute:{B}") is world_q.UNKNOWN, "the stem is asked of the actor's own ledger only"
    p = w.persons[A]
    p.ledger.append(Claim("c_deed", A, B, "fight.declared", True, 0, "firsthand", 100, "own"))
    p.pursuits = {"honour": 1.0}
    assert rd.read(B, f"dispute:{A}") is False
    p.pursuits = {"liberty": 1.0}
    assert sum(person_q.deeds_judged(p, B)) < 0
    assert rd.read(B, f"dispute:{A}") is True


# ------------------------------------------------------------------------------------------------
# (5) LOYALTY AT BUILD


def test_loyalty_in_band_cuts_a_negative_row_to_the_member_band_and_passes_a_positive_one():
    assert loyalty_in_band((-1, 4)) == (-1, 1) and -1 * 1 == MEMBER_BAND
    assert loyalty_in_band((1, 4)) == (1, 4) and loyalty_in_band(None) is None


def test_at_build_no_loyalty_row_names_a_faction_head_below_the_band_and_the_revert_does(monkeypatch):
    w = populated.build_realm(0)
    heads = I.faction_heads(w)
    spy, king = "p_npc_033", "p_npc_020"
    assert king in heads.values()
    assert person_q.stance_toward(w.persons[spy], king) >= 0, w.persons[spy].stance
    creed_rows = [r for p in w.persons.values() for r in p.stance if r[0] in w.propositions]
    assert creed_rows and all(float(r[1]) * float(r[2]) >= MEMBER_BAND for r in creed_rows)
    # THE REVERT, OBSERVED (batch close B3): the same Spymaster, with the fixture at its revert, holds the grudge toward the
    # King the audit found -- so the `>= 0` above is the fix and not an absent row.
    monkeypatch.setattr(populated, "DEFAULT_FIXTURES", DEFAULT_FIXTURES.sweep("loyalty_toward_creed", False))
    reverted = populated.build_realm(0)
    assert person_q.stance_toward(reverted.persons[spy], king) < 0, reverted.persons[spy].stance


# ------------------------------------------------------------------------------------------------
# THE REALM READING (the falsifier), THE MUTATION AND THE CONTROL


_FIGHTS: dict = {}


def _realm_fights(seed: int, seasons: int = 1) -> list:
    """`_run_realm_fights`, once per (seed, seasons, decline on or off): the exit tests and their mutation controls
    read the same realm, and a realm run is the cost of this file (batch close, accretion pass)."""
    key = (seed, seasons, bool(O.VIOLENCE_CONTEXTS))
    if key not in _FIGHTS:
        _FIGHTS[key] = _run_realm_fights(seed, seasons)
    return _FIGHTS[key]


def _run_realm_fights(seed: int, seasons: int = 1) -> list:
    """Every `fight` Candidate formed, through the audit's own run: (actor, subject, same faction, stance, seats)."""
    box, forms = {}, []
    rb, ro = I.build_realm, I.opening_set

    def build(*a, **k):
        box["w"] = rb(*a, **k)
        return box["w"]

    def opening(p, v, q, fx):
        out = ro(p, v, q, fx)
        w = box["w"]
        forms.extend((p.id, c.subject, I.same_faction(w, p.id, c.subject), person_q.stance_toward(p, c.subject),
                      set(I.held_offices(w, p.id)), set(I.held_offices(w, c.subject)))
                     for c in out if c.verb == "fight" and c.subject in w.persons)
        return out

    I.build_realm, I.opening_set = build, opening
    try:
        I.run(seed, seasons)
    finally:
        I.build_realm, I.opening_set = rb, ro
    return forms


def _named_cases(forms) -> tuple:
    """(Cardinal -> Senior Inquisitor formations, Spymaster -> King formations), the audit's two cases."""
    return ([f for f in forms if f[4] & CARDINALS and "off_senior_inquisitor" in f[5]],
            [f for f in forms if "off_spymaster" in f[4] and "off_king" in f[5]])


def test_seed_0_season_1_no_same_faction_fight_forms_at_stance_at_or_above_minus_3():
    forms = _realm_fights(0)
    assert [f for f in forms if f[2] and f[3] >= -3] == []


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_the_cardinal_inquisitor_and_spymaster_king_cases_do_not_form_on_seeds_0_to_2(seed):
    """The plan's exit reads seeds 0-2 for the two named cases; the same-faction reading above is seed 0, as the plan
    words it."""
    cardinal, spymaster = _named_cases(_realm_fights(seed))
    assert cardinal == [] and spymaster == []


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_mutation_the_decline_deleted_restores_the_two_named_cases_on_each_seed(monkeypatch, seed):
    """THE POSITIVE CONTROL for the test above: the absence is only a reading if the instrument sees the cases when
    they are there. With the block emptied, both named cases form on the seed (the audit's 3 and 3 or more)."""
    monkeypatch.setattr(O, "VIOLENCE_CONTEXTS", {})
    cardinal, spymaster = _named_cases(_realm_fights(seed))
    assert cardinal and spymaster, (len(cardinal), len(spymaster))


def test_mutation_the_decline_deleted_restores_same_faction_fight_formations(monkeypatch):
    monkeypatch.setattr(O, "VIOLENCE_CONTEXTS", {})
    forms = _realm_fights(0)
    assert len([f for f in forms if f[2] and f[3] >= -3]) > 0


def _old_cells(monkeypatch):
    table = {ax: dict(row) for ax, row in V.ALIGNMENT.items()}
    # TODAY'S (PRE-CR-87) CELLS, one value at a time: these are the cells' old VALUES, not a roster of axes, so no
    # literal here holds two axis names (`tests/valoria/test_axis_roster_single_owner.py` reads that as a second roster).
    old: dict = {"fight": {}, "accept": {}}
    old["fight"]["grandiose_humble"] = -0.3
    old["fight"]["deontological_instrumental"] = 0.3
    old["accept"]["rigid_flexible"] = -0.3
    old["accept"]["grandiose_humble"] = -0.2
    old["accept"]["deontological_instrumental"] = -0.4
    for verb, cells in old.items():
        for ax in table:
            table[ax].pop(verb, None)
            if ax in cells:
                table[ax][verb] = cells[ax]
    monkeypatch.setattr(V, "ALIGNMENT", table)


def revert_cr87(monkeypatch) -> None:
    """EVERY PART OF CR-87 AT ITS REVERT, for the life of one test: the block empty, today's cells, the reverts of both
    fixtures (`populated.DEFAULT_FIXTURES`, which `build_realm` hands its World), `accept` fought at `death`, and the
    `dispute` conjunct stripped from `challenge`'s cell. The `Enemy` stamp needs no revert: no war, no stamp. A test whose
    subject is an earlier position's realm reading (CP-T03-01's cohort control) calls it to read that position on the
    world it was measured on."""
    monkeypatch.setattr(O, "VIOLENCE_CONTEXTS", {})                                     # (1) the block empty
    _old_cells(monkeypatch)                                                            # (2) today's cells
    monkeypatch.setattr(populated, "DEFAULT_FIXTURES",                                 # (3), (5) the reverts
                        DEFAULT_FIXTURES.sweep("hostile_stance_gain", None).sweep("loyalty_toward_creed", False))
    monkeypatch.delitem(V.DUEL_TERMS_BY_VERB, "accept")                                # (4) death duels
    row = V.VERB_TABLE["challenge"]
    req = row.requires_typed
    kept = tuple(c for c in req.requirement.clauses if getattr(c, "relation", None) != "dispute")
    assert len(kept) == len(req.requirement.clauses) - 1
    monkeypatch.setitem(V.VERB_TABLE, "challenge",
                        dataclasses.replace(row, requires_typed=TypedRequires(AllOf(kept), req.names)))


def test_control_the_block_empty_and_every_value_at_its_revert_reproduce_the_pre_item_hash(monkeypatch):
    revert_cr87(monkeypatch)
    # v10 CP-T03-02 (a later mover of every season that fought: the band's `ending`, the body Observation) is
    # reverted too, so the base tree's reading stands rather than being re-taken.
    revert_cp_t03_02(monkeypatch)
    # v11 CR-85 (`faculty` replaces `history` in the pool and the Ob, a later mover of every season that fought) is
    # reverted too (`revert_cr85`, the seam's faculty at 3 for every party), the same way.
    revert_cr85(monkeypatch)
    # v11 CP-T03-04 (`arms` in the vocation range, a formation mover of every season) is reverted too, the same way.
    revert_cp_t03_04(monkeypatch)
    revert_cp_t03_07(monkeypatch)   # v11 CP-T03-07 (`body_ceiling`, a schema mover of the build), the same way
    assert populated.build_realm(0).content_hash() == BASE_BUILD
    w, _d, _rows = I.run(0, 1, observe=False)          # the audit's own run, which read the base hash
    assert w.content_hash() == BASE_SEASON


def test_the_shipped_build_differs_from_the_base_so_the_control_is_not_vacuous():
    assert populated.build_realm(0).content_hash() != BASE_BUILD
