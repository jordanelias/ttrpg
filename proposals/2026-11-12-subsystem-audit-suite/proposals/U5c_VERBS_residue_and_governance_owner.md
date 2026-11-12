# U5c · VERBS — the residue: two shapes for a drawn act with nobody opposite, one prize roster for the governance rows, and four closings

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — applied `unified/U3_CONFLICT_LEDGER.md` C3-C9 (§4 edit 1 replaced: the fold declines resolver-side, formation reads the party's own ledger; text of `unified/work/R4_READ.md` 7b.1), C3-C11 (the failed draw's durable write, A-81), C3-R1 (18-A's loader edit is the dependency), the U3 batch split (§4.1 rows 28 to 31), R4 §2 on `succeed` (A-19: a docketed rival opposite), U1 D-U1-01 (`rank_gap` is the against-half of the seat's two channels) and D-U1-11i (`graded_tasks`); R4 7b.0 implementation block added. No design change beyond those rows. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "patient" → "counterparty" (glossary *party*).

## Status: PROPOSED (written by the U5c closure lane; a plan for a later implementation lane, executed by nobody here; not ratified by being written, `CLAUDE.md` §2)

Lands in batch: B07 for §1, §2 and §4 (`unified/U3_DEPENDENCY_ORDER.md` §3.1); §3 in B09 with `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (U3 §4.1 row 28); §6 and the `audience_of` readers that name `present_persons` / `holders_named` in B11 after `08_FI_01`/`08_FI_02` build them (rows 29, 30); the hearing's `a verdict` row in B24 with `05_SC_playable_hearing_B.md` (row 31).
Depends on: `18_DETERMINISM_task_draw_for_uncontested_verbs.md` items 1, 2 and 4 (B07; item 4 edits the two loader refusals at `engine/season/data/verbs.py:848-876` that refuse a band-keyed route row, C3-R1); `U5c_SC_one_obstacle_form.md` §4 steps 0 to 2 and `05_SC_obstacle_difficulty_and_modifiers_B.md` (B05).
Lane: IN (rosters, registry, loader); each verb lane lands its own rows. Tier (R4 7b.0 (1)): §1 and §2 loaders and rosters `sonnet` producer, effort `high`, then one `opus` read of the gate output; §3 and §4 `sonnet` producer plus the `opus` gate read. Test file: `engine/season/tests/test_vres_task_and_prize.py` (one function per gate below).
Draw key: the `a task` prize's draw takes `H(w.world_seed, w.tick, <actor id>, "<verb>.task")` (A-30; `04` PART D 35) through the one draw owner (`11_GO_one_draw_owner.md`, B06).

Carries the rows of `unified/U5_FINDINGS_CLOSURE_U5c.md` Part 4 whose carrier column reads **VRES**, and
conflicts C-22, C-23, C-25, C-30, C-34 and the fourth row of C-10 in `unified/U5_CONFLICTS_U5c.md`.
Sources: `audits/14_VERBS_SOCIAL1.md` §15, `14_VERBS_SOCIAL2.md` §11.4, `14_VERBS_BINDING.md` §0.2 and
§13.4, `14_VERBS_MATERIAL.md` D-1 and D-4. Conformed to `unified/DECISIONS_ANSWERED.md` (A-12, A-14, A-21,
A-22, A-24, A-37, and the ladder closings D-31 and D-46). It edits no verb proposal's design: where it
changes one, that file carries a `Reconciled:` line pointing here.

## What it changes in `engine/season/` at runtime

§1: nothing by itself; it fixes which of two loadable shapes a drawn row takes. §2: three prize rows and
two audiences, hash-equal until a verb row names them. §3: a refused act teaches its actor that the person
he sought was not there. §4: a party cannot close an edge a bench imposed on him. §5, §6: nothing beyond
their sources. Declared movers: §3, §4, and each verb row as its own proposal lands it.

## §1 A drawn act with nobody opposite takes one of two shapes (C-22, C-23; MATERIAL D-1, D-4)

`04` §B.13 invariant 12 and §C.4: a `Degree`-keyed `writes:` belongs to a row that declares `contests:`.
The loader refuses the other shape (`engine/season/data/verbs.py:848-851`). Four verb proposals put
band-keyed writes on a route row (`graded_acts`); `18_DETERMINISM_task_draw_for_uncontested_verbs.md`
(18-A) had the same shape and was rewritten by U5a (its C-U5a-10). One decision across both families:

| shape | when | the row | the failed draw |
|---|---|---|---|
| **(a) route row** | the act has one effect, and the band changes how much of it or how good it is | a member of the route roster (18-A's `graded_tasks`); **flat** `writes:` and `emits:`; each effect reads the band through `task_fraction` or a quality table | the row's keyed `emits_on_refusal` clause `draw`; nothing is written |
| **(b) contest row** | two bands must write different cells | `contests: "a task"`; `writes:` and `emits:` keyed by band (invariant 12's own shape) | the Failure branch |
| **inquiry** | the product is a deposit to the actor (`research`, `examine`, `surveil`, `reconstruct`) | a route row that writes nothing and keys `emits:` by band, as today | `finding.none` |

Exact edits:

1. `engine/season/rosters.yaml: contest_subsystems.prizes` gains `"a task"`: `module: social_contest`,
   `provider: social_contest`, `module_entry: social_contest.roll`, no `heard_by`, no `step`. The module
   name is whose roll it is, not a claim that a task is social; the roll is the one pool-against-obstacle
   draw. `references/module_contracts.yaml` binds the entry to the first verb that names the prize
   (`manifest/registry.py::check_contest_prizes`), so the row lands with that verb, not before.
2. The route roster has one name. 18-A item 2 renames `graded_inquiries` to `graded_tasks`; the MATERIAL
   proposals' `graded_acts` is that roster and is not added beside it.
3. The share table has one name and one set of first values: `task_fraction`, 1 / 1 / 0.5 / 0
   (Overwhelming / Success / Partial / Failure). `14_VERBS_MATERIAL_A_mending.md` §2's `effect_share`
   1000 / 700 / 350 / 0 is the same roster; its values are a sweep arm.
4. Which shape each row takes is one test applied at the row by its owner: *do two bands write different
   cells?* Applied here to the rows this lane can decide from the band maps it read: `commit` (the band is
   the value of `Tenure.degree`: one cell) is (a); `conceal`, `forge`, `create_record` (the band is a
   quality on one Record or cover) are (a); `tend`, `work`, `restore`, `requisition`, `transfer` (one
   magnitude) are (a); a row whose Partial opens a different edge or writes a different field than its
   Success is (b). No row is left on a flat fold: 18-A item 1's loader refusal is the check.

**A failed draw still moves the world (A-81; C3-C11).** "Nothing is written" above means no typed cell. The
refusal Event of shape (a) and the Failure Event of shape (b) are witnessed: those present hold a claim of
the failure (the Event's kind, through WITNESS's `co_located` channel), and an actor alone deposits his own
firsthand claim `(self, <verb>.failed, True)` by his own Observation. That deposit is the band's durable
write, which the no-null-scene reading counts; each verb proposal names it per row.

Gate: the loader accepts every converted row and refuses three planted ones (a band-keyed `writes:` on a
route row; a flat `writes:` on a `contests:` row; a row that writes and is in no class). Falsifier: a route
row whose Failure writes a cell. Hash: none from this section; each row is its own proposal's mover.
Lanes: IN and CORE (roster, loader), each verb lane (its rows). Order: with or after 18-A items 1 and 2.

## §2 The contested governance rows: one prize roster, one roll, one obstacle composer (C-25; BINDING §0.2)

`audits/14_VERBS_BINDING.md` §0.2 made nine rows contested; five proposals then named four new prizes and
asked `contest_input` for a different audience per verb. The owners, each existing:

| fact | single owner |
|---|---|
| what is contested, and who hears it | `rosters.yaml: contest_subsystems.prizes` (the row and its `heard_by:`) |
| the roll | `modules/social_contest/roll.py` through the composition role the prize row names |
| the obstacle | `roll.py::obstacle` over `rosters.yaml: obstacle_terms` (`U5c_SC_one_obstacle_form.md` §1, §2) |
| the audience a room name means | one host function beside `HEARD_BY_ROOMS` (`manifest/registry.py:276`), read by `seam/wrappers/sigma.py` |

A prize row exists for each distinct pair of (who hears, when it is fought), and for nothing else. That is
why some proposed prizes are kept and some are not:

| prize | `heard_by` | fought | rows | status |
|---|---|---|---|---|
| `a standing` | none (one person opposite) | RESOLVE | `issue`, `dispatch`; the person-to-person verbs | existing; `an order` is **not added** (same hearer, same step) |
| `a matter` | `bench` | RESOLVE | `pardon`; `speak` | existing |
| `a verdict` | `bench` | ENCOUNTER, entry `social_contest.hearing` | `determine` | new, with `05_SC_playable_hearing_B.md`; the ballot is inside it (A-14; `U5c_SC_proceedings_residue.md` §6) |
| `a seat` | `seat_body` | RESOLVE | `confer`, `revoke`, `succeed`, `establish` | new (`14_VERBS_BINDING_A_formation.md` edit 11) |
| `a holding` | `residents` | RESOLVE | `surrender` | new (`14_VERBS_BINDING_E_war_seats.md` edit 6) |
| `a task` | none (nobody opposite) | RESOLVE | §1 shape (b) rows | new (§1); `a cover` is **not added** |

The nine rows, read through that roster (each row's bands, classes and filters stay its proposal's):

| row | prize | opposite | obstacle members beyond `difficulty` and `opposition` | carrier |
|---|---|---|---|---|
| `confer` | `a seat` | the incumbent when displacing, else the stand-in | `stakes`, `rank_gap`, `reception` | `14_VERBS_BINDING_C_turnover.md` §1 |
| `revoke` | `a seat` | the holder | `stakes`, `rank_gap`, `reception` | same, §2 |
| `succeed` | `a seat` | a docketed rival claimant where one exists (A-19: heir, consort, princess and both houses' heads may claim; odds from what others believe of each deed), else the stand-in | `rank_gap`, `reception` (each audience reading `legitimacy(q, claimant, seat)`, `15_INSTITUTIONS_BYZANTINE_E` e1) | same, §3 |
| `establish` | `a seat` | the stand-in | `rank_gap`, `reception` | `14_VERBS_BINDING_A_formation.md` §2 |
| `determine` | `a verdict` | the other party's case | the hearing's own (`standard`, `reception`, `first_heard`, `plea`) | `14_VERBS_BINDING_B_sittings.md` §2; the hearing |
| `pardon` | `a matter` | the stand-in | `stakes`, `standard`, `reception` | same, §3 and §4 |
| `issue` | `a standing` | the addressee where one person is named, else the stand-in | `rank_gap`, `regard` | `14_VERBS_BINDING_D_orders.md` §1 |
| `dispatch` | `a standing` | the man ordered | `rank_gap`, `regard` | same, §2 |
| `surrender` | `a holding` | the stand-in | `reception` | `14_VERBS_BINDING_E_war_seats.md` §2 |

Reconciliations this table makes, each on the losing file's head:

- **`rank_gap`, not `standing`.** The word `standing` already names a prize, a Sensation field and two
  content keys. A-12 licenses the term; the name is this lane's. U1 D-U1-01 fixes the two channels: the
  seat a counterparty holds above the actor's stands against the act as `rank_gap` (fixture `rank_step`,
  OBS §2 member 6); the seat the actor exercises helps him only as the `office` leverage source read off the
  seat row's `modifier:`; no row reads one seat twice.
- **`regard` or `reception`, never both** (`U5c_SC_one_obstacle_form.md` §2 members 7 and 8). A row heard by
  an audience reads `reception`; a row with one person opposite and no audience reads `regard`. So
  `revoke` drops `regard`: the holder's resistance is already the `opposition` term.
- **The band a document was drawn up at is the content key `force`**, read by the answer rows
  (`comply`, `evade / defy`), never `standing`.
- **Whom an order may address is A-22's predicate** (command: sworn men, holders of seats the issuer may
  revoke, the unseated in his land), which `14_VERBS_BINDING_D_orders.md` commit D2 builds. It is
  eligibility, read at formation; it is not an obstacle term.
- **The audience is a cell on the prize row.** `14_VERBS_BINDING_A` edit 14, `_B` edit 12, `_C` edit 3 and
  `_E` edit 9 each ask `contest_input` for an audience by verb. Read them as one edit:

Exact edits (one commit, no verb row using them, so hash-equal):

1. `manifest/registry.py`: `HEARD_BY_ROOMS = frozenset({BENCH, SEAT_BODY, RESIDENTS})`; `_check_heard_by`
   unchanged.
2. One host function, `seam/wrappers/sigma.py::audience_of(w, act, room) -> tuple[str, ...]`, a table
   keyed by room and nothing else: `bench` is `world_q.judging_set` at the act's rung (today's read);
   `seat_body` is the members of the body the act's seat belongs to, else the seated persons at that
   seat's rung; `residents` is the persons residing at the act's place. `world_q.reception` and
   `world_q.proofs` take the tuple. No branch names a verb.
3. `rosters.yaml: contest_subsystems.prizes`: `"a seat"` with `heard_by: seat_body` and `"a holding"`
   with `heard_by: residents`, each with the `a proposition` row's module, provider and entry. `"a
   verdict"` lands with the hearing, not here.
4. The reading's direction is the actor's side by default. A prize row may declare `toward: to`, read by
   the same function, where the audience is asked about the receiver and not the actor; `a holding`
   declares it (the residents' stance toward whoever would hold the place). **Assumption of this lane:**
   the BINDING proposals state the audience and not the direction for `confer`; it ships toward the actor
   and the conferee's standing with the body is a sweep arm of the same cell.

Order: `U5c_SC_one_obstacle_form.md` §4 steps 0 to 2; then this section's four edits; then
`14_VERBS_BINDING_B`, `_A`, `_C`, `_D` (after its command predicate), `_E` (after
`14_VERBS_PHYSICAL` batch B, U5b's), each with its terms' steps at control 0 first.

Gate: (1) the loader refuses a planted `heard_by: nobody` and a verb naming a prize no row claims
(invariant 9). (2) A unit test builds one act twice with the prize row's `heard_by` swapped between
`bench` and `seat_body` and reads two different audiences from `audience_of`: the audience follows the
row. (3) At seeds 0 to 2, three seasons: every Event of the nine verbs carries a `Margin` with `terms`
and `levels`; printed count of governance Events with none, expected 0. Falsifier: a `reception` term on
an act whose prize row has no `heard_by`; a term in a governance `Margin` that is not a member of
`obstacle_terms`; a function in the seam that names a verb to pick an audience. Lanes: IN (roster,
registry), SC (`sigma.py`), FA and the verb lanes (rows).

## §3 A refusal teaches the actor, and only him (SOCIAL1 D2; decision register D-46, taken B)

`audits/14_VERBS_SOCIAL1.md` D2: a man who seeks someone who is not there is refused, learns nothing and
forms the same act again. U5a's closure (F-PES-CORE-01) names this lane as the carrier of the private
belief of absence for the `with` conjunct.

1. Plan CP-T06-04 (B10-14) already deposits a refused act's reads to its actor. Its deposit gains one
   case: a refusal on the `with` conjunct deposits, to the actor only, a firsthand claim that the person
   sought was not at that place at that tick. The predicate is a member of the claim-predicate roster the
   WITNESS deposit keys on; this proposal calls it `absent`.
2. `queries/person_q.py::present_persons` (`08_FI_02` edit 5, the one reader of "who I believe is with me")
   leaves out a person about whom the holder's newest firsthand claim at that place is `absent`, until a
   newer sighting or telling places him there.
3. Nobody else learns anything: the claim's holder is the actor and it is not an Event's public payload.

Gate: `runs/PES_FI/p1b_belief.py`'s shape: 7 candidates naming the absent person before the refusal, 0
after; a later planted sighting restores them. In a realm, seeds 0 to 2: the share of refused acts that
repeat the same `(verb, target)` next season, before and after (U5a quotes 41 % retried). Falsifier: a
second person holding the `absent` claim; a candidate formed on a person the holder's newest claim says
is absent. Hash: declared mover on every world with a `with` refusal. Lanes: FI (deposit), CHAR (reader).
Composes with `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (U5a's): that proposal declines the act;
this one removes the referent.

## §4 A party does not close an edge a bench imposed on him (A-37; closure C-10 row 4)

Jordan, A-37: an imposed service ends by the bench's `pardon` or its term, as detention and banishment
do. This overwrites the earlier ruling that a convict has one free release.

1. *(Replaced by W3-4a under C3-C9; the earlier text read the log from formation, which `04` §B.9 forbids:
   `state/acts` is resolver-side and no person-side Query reaches it.)* `14_VERBS_BINDING_A_formation.md` §1
   keeps `own_edge_declines` (formation reads the row's own `domain:`). A **second** decline, person-side,
   in `decision/options.py::opening_set`: a `release` referent is dropped when the actor's own ledger holds a
   claim of an Event of kind `matter.determined` (T, `verb_table.yaml:406-408`) whose counterparty is the actor
   and whose object is the referent's edge `[UNVERIFIED: the claim's value shape; read `loop/witness.py`'s
   deposit for `matter.determined` before landing]`; the kinds `ban.opened` and `detention.opened` join the
   decline only if `15_INSTITUTIONS_PAPACY_D` lands them (they are not in the tree). The **fold** check is
   resolver-side: `loop/predicates.py::_req_release` (T, `:429`) refuses (`release.refused`, clause `own`) an
   edge whose opening Event was caused by an Act of verb `determine`, read through
   `state/attribution.py::causing_act` (T, `:91`). No field is added to `Tenure`. Order of edits: the fold
   clause first (a planted release is refused), then the formation decline (the candidate is gone).
   Falsifier for the split: the person-side decline removed, the formation returns and the fold still
   refuses (the control).
2. `_eff_determine`'s docstring (`loop/effects_information.py:531-535`) records the price C-1 ruled:
   *"`oblige` is in `release`'s domain, so that price is paid as ruled"*. The sentence is replaced by this
   clause's, citing A-37; the gate basis for closing a disposal stays `determination`, through the seat
   that is the edge's object (`loop/effects_governance.py:377-380`). `detain` and `ban` already decline.
3. What ends it: `pardon` (drawn, `14_VERBS_BINDING_B_sittings.md` §3 and §4) or the term maturing at
   MATTER (`05_SC_arrangement_rows_that_bind.md`). Running from it is `evade / defy`, which is drawn
   (`14_VERBS_SOCIAL1_B_documents_and_obedience.md` §2) and leaves the edge open.

This is eligibility, so nothing is left undrawn: the outcomes around it (the verdict, the pardon, the
evasion) each draw. Gate: at one seed with a determined case, the party's candidates hold no `release` of
the disposal edge; a planted one is refused naming the clause; a `pardon` at Success closes it. Falsifier:
a disposal edge closed by an Event whose actor is its subject. Hash: declared mover wherever a convict
released himself (the pessimist counted the same-season releases; quote that count in the commit).

## §5 A decree is proclaimed; a covenant and a challenge are handed over (A-21; SOCIAL1 D1; C-34)

Jordan, A-21: whoever learns a decree was issued knows its terms and may answer it without holding paper;
covenants and challenges stay in person. So:

- **D1 is closed.** Nothing is minted into an addressee's hand, and `comply` and `evade / defy` on a
  decree form from a held claim that it was issued. The carrier is `06_FA_decree_binds.md` (U5d's).
- **`14_VERBS_SOCIAL1_B_documents_and_obedience.md` §1 narrows.** Its addressed-document occasion for
  `give` stays for a covenant and a challenge. For a writ it is no longer the only road to an answer; a
  writ may still be carried and handed over (the paper is evidence a bench can be shown).
- The measurement this lane had proposed in D1's place (count `record.given` of a writ to its addressee)
  is withdrawn: the question it would have re-opened is answered.

No edit beyond those two files' own. Gate: `06_FA_decree_binds.md`'s.

## §6 Swearing to a seat is a draw against the seat (decision register D-31, taken A under A-24; C-30)

`14_VERBS_SOCIAL2_B_a_word_with_content.md` §4 stands as written on the draw: `oblige` is contested, the
opposite is the seat's holder where the joiner's ledger names one (`person_q.holders_named`) and the
stand-in where it names none, a Partial is probation. Three reconciliations only: the seat news comes from
the one build step `seed_seat_news` (`08_FI_01` edit 6; C-20); the private table `oblige_obstacle` is the
roster member `establishment` (C-21); the control fixture `oblige_admission: fiat` stays the hash-equal
arm. The ruled roster value `members_by_admission` still says whose act admission is. This lane's first
reading (a draw with nobody opposite) is withdrawn.

## Layer 1 reading (`skills/layer-conformance`, Lens B)

§1: invariant 12 and §C.4, both halves of the row read (a `contests:` row keys `writes:`; a row without
does not): conforms; MECHANICAL at load. §2: `04` §C.5 (the seam returns a Margin; a prize names a
subsystem) and PART E step 10 (a misspelled manifest row fails at boot): conforms; the audience function
reads `World` on the host side of the seam, which the provider row allows, and the module reads a typed
record. A-12's amendment to `04` §B.7 is owed by the unification stage; `rank_gap` is written here under
that answer and is not conformant to the row as it stands today, which is said rather than hidden. §3:
the deposit is WITNESS's INTERIOR write into the actor's own ledger (`04` §A.2 `loop/witness`); the reader
opens the holder's ledger only (§B.2). §4: no new gate basis (§C.2). Grades: §1, §2 MECHANICAL; §3, §4
CONVENTION until their gates' tests exist.

## Cost class

§1: edit (one prize row; the rest is 18-A's). §2: small build (one function, two room names, two rows).
§3: small build inside CP-T06-04. §4: edit. §5, §6: none.
