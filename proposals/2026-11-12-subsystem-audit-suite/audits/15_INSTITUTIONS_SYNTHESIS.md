# INSTITUTIONS · SYNTHESIS — crown, deed-nobility, Church, bureaux, republics, guilds and companies as one order

## Status: REFERENCE (a design and plan in proposal form under `INSTITUTIONS_BRIEF.md`; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 8948603 (working tree)

Lane: the synthesis lane of `INSTITUTIONS_BRIEF.md` (*"Fable can develop proposals to make these political,
religious and social institutions functional together"*). Subject: the four finished family lanes
(`audits/15_INSTITUTIONS_BYZANTINE.md`, `…_PAPACY.md`, `…_VENICE.md`, `…_COLONIAL.md` and their twenty-one
proposals), reconciled into one kit with one plan. This file changes no code, registry or canon. The
exact edits are in `proposals/15_INSTITUTIONS_SYNTHESIS_A` to `_E` (listed in §9). Where a family file
lost a collision it carries a `Reconciled:` line at its head naming the change; no family finding is
deleted.

Marks: `[BYZ]`, `[PAP]`, `[VEN]`, `[COL]` cite the family audit or proposal at the section named; a code
or canon statement taken from a family file and not re-opened here is marked `[via <lane>]`; a statement
opened here is cited by path. `[ASSUMPTION; Jordan to correct]` marks content this lane had to choose.

---

## 0. Verdict

**The four families are one design drawn four times, and they can be made one order without adding a
primitive that none of them asked for: every institution in them is persons in seats, sworn by `oblige`,
acting through documents, judged in hearings, on one roll.** What stops them functioning together today
is not a disagreement of mechanism but (a) the same four upstream absences each lane found alone (an
order that reaches nobody and is answered by nobody; an obstacle with no named terms; empty stores; six
institutional verbs that execute with no draw), and (b) twenty-nine collisions among the lanes themselves and with the
verb lanes, every one of them a collision of **name, home or shape**, none of method: three encodings of
the founding order of the Secession War, three carriers for a certified deed, two things called a roll,
two things called a charter, two things called `instruments`, two functions for standing, two encodings
of an audit at exit, two shapes for a share in a company, two far superiors for Altonia, and rival
rewrites of `confer`, `revoke`, `succeed`, `issue`, `carry`, `requisition`, `transfer` and `seize`. §2
decides each.

**The single largest obstacle to the order as an order is that no tie, no paper and no certificate
changes any odds.** An oath, a debt, a charter, a consecration and a place on the roll all exist or can
exist as edges and Records, and no roll reads them. The interlocks Jordan names (an excommunication
against a duke, a loan against a throne, a charter against a rival, a deed certified by one body and
contested by another) are all the same event: *one institution's instrument entering another
institution's draw as a term.* So the kit's centre is small: **one closed obstacle-term list** in which
four terms carry every crossing (`obligation`: what the one asked owes; `remove`: how far the actor
stands; `standing`: how the person stands against the seat; `evidence`: what is held and cited, a
certificate included), **one registry of instrument forms and seeded instruments**
(`engine/season/instruments.yaml`), **one new record kind** (`debt`) and **one new content key**
(`recites`, which makes any Record a certificate of deeds), **one standing function**
(`person_q.legitimacy`, extended by one term), and **eight seat-row keys**. Everything else is rows.

**The deed ledger is the shared currency, and it is paper somebody keeps.** A deed is an Event and
fades from memory; a certificate is a Record that recites deeds, made only by a drawn act of a body or a
seat, kept by a named seat, and able to be consulted, retold, forged, seized and burned. Standing passes down the
**seat** (not the blood) at a discount per holder, and only through deeds a person still holds a claim
of; the keepers of rolls are therefore the keepers of every house's past, and each keeper is a different
institution (the Crown's clerks hold the Settlement Roll of the three founders; the Church's archive
holds the consecrations; a guild and a republic hold their own). That is where the order's conflicts come
from, with no rule naming any of them (§5).

**Nothing in the kit is decided by rank, office, count or instrument.** Every procedure is a draw on the
one ladder; what an institution contributes is a term in somebody else's odds.

---

## Contents (appended in this order)

1. What was read, and the four families in one table
2. The collision ledger: every collision and its decision
3. The one kit: registries, record kinds, seat-row keys, obstacle terms, arrangement vocabulary, fixtures
4. The deed ledger in the order of the Secession War; the tree's four disagreements; canon amendment drafted
5. The interlock map: institution by institution, exports, imports, sanctions and favours
6. Structural conflicts that generate story, as draws, with the instrument for each
7. The commensuration test
8. Layer 1 conformance, and where Jordan's intent meets Layer 1
9. The implementation plan: batches, edges, gates, first playable, cost classes
10. Survivors for Jordan
11. Evidence log and what was not read

---

## 1. The four families in one table

Each family lane found the same skeleton and the same absences from its own side. Read across, the rows
are one institution model.

| | BYZANTINE | PAPACY | VENICE | COLONIAL |
|---|---|---|---|---|
| where it sits in the world | Altonia; the Crown's inherited bureaux (Imperial Court, Court Parliament, Ministries, Rectorates, Praefectures) | the Church of Solmund | Schoenland; Hafenmark's communes; the Guilds and their houses | Altonia as metropole; the Church's containment grant; the conquest tenure of crown and duchies; Schoenland and the Guilds as chartered trade |
| what an institution is | seats, some with no remit (dignities), paid yearly, with paper passing named hands | seats filled by its own, benches whose reach follows the person, sanctions that work through other people's answers | seats that rotate from a roll, by lot and ballot, audited at exit; houses; debts | seats conferred by grants; distance; audits; grants called in |
| the absence it found | no upkeep, no hand, no founding order, no superior (`[BYZ]` §0) | no reach, no election, no sanction with a third party, no past (`[PAP]` §0) | no term, no roll, no lot, no debt, no charter, no tie in any odds (`[VEN]` §0) | no cost of distance, no reader of a covenant, no audit, no founders (`[COL]` §0) |
| new primitives it asked for | record kind `roll`; keys `dignity`, `upkeep`, `passes_through`, `hand_term`; section `founding`; row `acclamation` | key `patronage`; arrangement key `quorum_share`; section `instruments`; roster `writ_terms_forms`; rows `conclave`, `consecration`, `general_council` | term `obligation`; record kind `debt`; `members_by_warrant`, `lot`; keys `eligible_from`, `cooling_off`, `audit_at_exit`; rows `debt_suit`, `security_bench`, `exit_audit`, `enrolment_ballot` | term `remove`; registry `instruments.yaml`; key `audited`; rows `audit`, `quo_warranto`; Query `accomplishment` |
| verbs it gave a draw | `confer`, `revoke`, `carry`, `requisition`, `succeed` | (the verb lane's) `determine` ballot outcomes; the believer's answer | the ballot; the reckoning; the lot | `requisition`, `transfer`, `issue`, `seize` |
| first playable | `roga` (the unpaid court); `chancery` | The Vacant Chair | The Counting-House | The Farm of the Southern Tolls |
| the fixed point, as it carried it | founding claims whose subject is the seat, confidence by order, a presumption term in `legitimacy` | three attestation Records in the Church's archive, weights 5, 3, 2; consecration as a hearing | enrolment by a drawn ballot with the deed as evidence; nothing passes by blood | three dead founders with seeded deeds 3, 2, 1; a recursive `accomplishment` down the seat |

Four findings recur in all four and are not this lane's to repair; they are the kit's upstream (§9):

1. **A writ reaches nobody and is answered by nobody** (`06_FA_decree_binds.md`; `14_VERBS_BINDING_D_orders.md`).
2. **The obstacle has no named terms** (`05_SC_obstacle_difficulty_and_modifiers_B.md`).
3. **Every treasury rung is empty at build** (`07_SE_treasury_granary_B.md`; three lanes' probes read `{}`).
4. **The institutional verbs fold with no draw** (`18_DETERMINISM_task_draw_for_uncontested_verbs.md`;
   `14_VERBS_BINDING_A`, `_C`, `_D`; `13_SC_draw_for_unrolled_contests.md`).

---

## 2. The collision ledger

A collision is two lanes giving one thing two names, two homes or two shapes. Each row: the lanes, the
collision, the decision, the ladder step (1 superseded, 2 irrelevant, 3 design document or work order, 4
precedent, 5 architecture), and the family files that carry a `Reconciled:` line for it. "Owner" always
means the single file code would read.

### 2.1 Registries, records and the founding order

| # | collision | decision | step | reconciled in |
|---|---|---|---|---|
| X-01 | **Two things called `instruments`, and a third home.** `[PAP C]` `offices.yaml: instruments:` is a list of Records minted at build. `[COL A]` `engine/season/instruments.yaml` is a closed registry of grant forms. `[BYZ A]` `offices.yaml: founding:` is a third list of world-gen facts, and `06_FA_office_capabilities.md` edit 5 already claims the name `offices.yaml: founding:` for what a founded office is granted | **One file, `engine/season/instruments.yaml`, two sections:** `forms:` (`[COL A]`'s rows; its top-level key `instruments:` is renamed) and `seeded:` (the Records a world begins with; `[PAP C]`'s row schema). `offices.yaml` gains no section from this kit; FA-P6 keeps `founding:` for its own meaning | 5; the work order names the Colonial file as the home | PAP C, BYZ A, COL A |
| X-02 | **A rival roster of forms.** `[PAP D]` edit 5 and `[PAP E]` edit 2 add `rosters.yaml: writ_terms_forms` (`avoid`, `withhold`, `render`) | **Not created.** Three rows of `instruments.yaml: forms`: `avoidance`, `interdict`, `tithe`, written with `[COL A]`'s `forbears` and `due` clauses. Two schema values are added for them: a clause's `by:` may be `addressee`; a clause's `over:` may be `named` (the person or rung the instrument's content names). `[PAP D]` edit 7's person-side decline reads the form's `forbears` clauses whose `by:` is `addressee` | 5 (one registry of what a document obliges) | PAP D, PAP E |
| X-03 | **Three carriers for a certified deed.** `[BYZ A]` a Record kind `roll: [entries]`. `[PAP C]` CR-36's `resolution` with `terms: {seat, attests: n}`. `[COL]` §5.3 (c) a `dispensation` of form `recognition`. (`[VEN]` certifies by a ballot that opens an `oblige`, with no Record) | **A certificate is any Record carrying the content key `recites`**: a list of deed references (Event ids of `DEED_KINDS` kinds) and the seat or person they are recited for. Two kinds may carry it: CR-36's `resolution` (minted by `determine` under a `disposes: Record` row: a consecration, an enrolment by a body) and a `dispensation` whose form row says `recites: true` (a grant that recites the service it rewards: `homage`, `land_grant`, `march`, `charter`). The record kind `roll` is not added; the form `recognition` is not added; `attests: n` is replaced by the length of `recites` | 4 (CR-36 is the plan's one Record a hearing mints; `rosters.yaml: record_kinds` already notes that a covenant "is a dispensation distinguished by what its `terms` names") | BYZ A, PAP C, COL D |
| X-04 | **Two things called a roll.** `[BYZ]` the Roll is a document. `[VEN C]` a roll is the persons sworn by warrant to a keeper seat (`establishment_of`) | **`roll` means `[VEN C]`'s: a membership, carried by `oblige` Tenures under `binds: members_by_warrant`.** It is not a Record kind. What `[BYZ]` called the Roll is *the Settlement*: the seeded papers of 200 AG in the Chief Parliamentary Clerk's keeping (§4.3) | 5 (one name, one thing; a membership list code reads must be Tenures, as `establishment_of` already is) | BYZ A, BYZ F |
| X-05 | **Three encodings of Jordan's order** (king, Hafenmark, Varfell). `[BYZ A]` `order: 1, 2, 3` read as claim confidence 1.0, 0.8, 0.6. `[PAP C]` `attests: 5, 3, 2`. `[COL D]` three, two and one seeded `field.won` Events | **`[COL D]`'s: the number of seeded deeds per founder (3, 2, 1), as Events through the gate in the prehistory block.** The order then exists once, as things that happened, and every other reading (a certificate's weight, a person's estimate) derives from it. `founding_confidence` and `attests` are withdrawn. Only the order is Jordan's; the counts are `[ASSUMPTION; Jordan to correct]` | 4 (`audits/12_ARCS_adjudication.md` §6 row 16: prehistory is "acts and witnessed Events … not constructed Claims" `[via COL]`) | BYZ A, PAP C |
| X-06 | **Two functions for standing, and two shapes of the inherited half.** `[BYZ A]` a third term in `person_q.legitimacy` over claims whose subject is the seat, undiscounted and unaging. `[COL D]` a new `person_q.accomplishment`, recursive down the seat's holders at `presumption_gain` per step. `[PAP]` no term, and a stated limit: a dead founder's deeds are nobody's. `[VEN]` nothing passes by itself | **One function, `person_q.legitimacy`, one added term: the chain.** `legitimacy(p, holder, window, scar_shift, seat, fx)` adds, for the k-th prior lawful holder of `seat` as `p`'s own ledger knows the succession, `presumption_gain^k · Σ deed_term(p, c)` over that predecessor's deeds `p` still holds a claim of. The chain is cut at any holder `p` believes took the seat by force (`[BYZ A]`'s `_took_by_force`). `accomplishment` is not added; its two readers call `legitimacy`. Seat-subject claims are not added: the founders are persons (X-05) and their deeds are ordinary deed claims. `[PAP]`'s limit is thereby answered (R-17): the *house* is the seat's chain of holders | 3 (the brief: "extend it; do not invent a parallel"; canon `:92`, `:145`) and 5 (two ladders for one quantity is an S defect) | BYZ A, COL D, PAP C |
| X-07 | **`presumption_gain` has two owners' values.** `[BYZ A]` ships 0.5, sweeps 0 / 0.5 / 1.0. `[COL D]` 0.5, sweeps 0 / 0.5 / 0.75 | one fixture in `data/fixtures.py`; ships **0** (the control, hash EQUAL; §3.6), proposed 0.5, sweep {0, 0.5, 0.75, 1.0} | 5 | BYZ A, COL D |
| X-08 | **Who keeps the founding papers.** `[BYZ A]` NPC-008 holds the Roll. `[PAP C]` the Cardinal of Temperance holds all three attestations and the charter. `[COL D]` each `homage` is "held by both" parties | **Two keepers, by what canon says each body did** (§4.3): the Church's archive holds the containment charter (form `immunity`) and the first king's consecration (canon `:82`); the Crown's chancery (the Chief Parliamentary Clerk) holds the Settlement: the two ducal `homage` instruments, each reciting its founder's deeds (canon `:88-90`; NPC-008's case is the custody of "the sole surviving record of the founding settlement's terms" `[via BYZ]`). No house holds its own paper. The parties hold content claims, which is all `dues` and `kept` ask. `[ASSUMPTION; Jordan to correct]` | 3 (canon; the case file as the statement of what must be simulated) | BYZ A, PAP C, COL D |
| X-09 | **A debt is a record kind in one lane and an instrument shape in another.** `[VEN B]` kind `debt` with its own readers `debt_state`, `debts_held`, `debts_owed`. `[COL A]` `dues`, `kept`, `breaches` over forms; `[COL]` §4.3 gives a company's subscribers "a `tribute`-shaped instrument", `[VEN]` §12.4 gives them a `debt` | **`debt` stays a Record kind** (K-14's shape; `rosters.yaml:2427` reserves its operands) **and is also a row of `instruments.yaml: forms`** (`record_kind: debt`, `made_by: covenant`, `bearer: true`, one `due`, `lapse: stands`), so the three instrument readers read it and no second occasion source exists. `debts_owed` and `debts_held` are withdrawn into `dues` and `breaches`; `debt_state`'s arithmetic becomes the one amount reader `world_q.owed(w, record, clause)` that `dues` uses for every clause with an amount. One new form key, `bearer:` (the entitled party is whoever holds the Record; the bound party is whoever holds a live `commit` to its terms). **A share is a `debt`** (it is handed on; a `tribute` is not) | 3 (K-14) and 5 | VEN B, COL A |
| X-10 | **Two things called a charter.** `[COL A]` `charter` is a body's self-rule; `staple` is a body's right to trade a kind at a place. `[VEN D]` §3 a "charter" is a `dispensation` naming a market, and a new term `charter` sits on `exchange`'s rate roll | **`charter` is `[COL A]`'s form; `[VEN D]`'s trade privilege is the form `staple`.** No obstacle term is added for it: a held live `staple` cited on an `exchange` at its market is an `evidence` item (SC-B's existing term), as a held assessment is on a levy | 5 (one name; one term list) | VEN D |
| X-11 | **A warrant, a commission.** `[VEN C]` a warrant is "a `dispensation` whose `terms` is that seat"; `[VEN D]` a rector's commission is a `dispensation` | rows `warrant` and `commission` of `instruments.yaml: forms` (`made_by: issue`); `_req_oblige`'s warrant clause asks for a held live instrument of form `warrant` made through the seat | 5 | VEN C, VEN D |

### 2.2 Seat rows, bodies, procedures

| # | collision | decision | step | reconciled in |
|---|---|---|---|---|
| X-12 | **Two encodings of the audit at exit.** `[VEN C]` key `audit_at_exit: <arrangement id>`, row `exit_audit` (`disposes: ban`), occasion on term maturity. `[COL C]` key `audited: true`, row `audit` (band-keyed), occasion on any close of the hold | **Key `audit_at_exit: <arrangement id> | null`** (it names its room). **Row `audit`** (`[COL C]`'s: graded verdicts). **Occasion: any close of a hold on such a row** (a recalled or dead governor leaves an account too), stamped on a person who holds the `tenure.closed` claim and may open (`[VEN C]`'s set: `may_fill` over the seat, or a `determine` seat of its body). `audited` and `exit_audit` are withdrawn. A form's `confers:` block may carry `audit_at_exit` | 5 | VEN C, VEN D, COL C |
| X-13 | **The far superior of Altonia, twice.** `[BYZ D]` `off_altonian_head` (new unnamed person; the Doux a hand; head of faction). `[COL B]` `off_altonian_court`, post "Logothete", NPC-091, `ALT-0` at 3 hops; the Katepano stays faction leader | **One seat, `off_altonian_court`,** anchored `{territory: "ALT"}` (both lanes' reading of `rung_above_same_faction`), post a placeholder (no post name is coined: "Logothete" is `[COL]`'s placeholder and a retired patch's word for a Crown ministry `[via BYZ]`, so it is not used); holder one new cast row (id from `references/id_reservations.yaml` at landing); resident at `ALT-0`, `hops: 3`; `passes_through: [{seat: off_doux}]`; `obligees` the Katepano, the Kommerkiarios and the Doux; `factions.head_seat.Altonia` is this seat (a head is the seat nobody above can strip). `[COL B]`'s goal row stands | 4 (ARCS row 12) and 5 | BYZ D, COL B |
| X-14 | **Two distances.** `[BYZ]` distance is the term of a hand. `[COL]` distance is `remove` on the roll | **Both, and they are different things**: `remove` is space (odds that an act lands); a hand is a person (who may sit on it). `remove` enters the issuer's roll once and each hand's `carry` at the clerk's own remove from where the paper lies | 5 (`[COL]` §10 already states the composition) | BYZ C, COL B |
| X-15 | **The ballot, three ways.** `13_SC_draw_for_unrolled_contests.md` (the owner): each member rolls his own ballot. `[PAP B]` composes on it and adds `quorum_share` and three outcomes. `[VEN C]` edit 5: the proposer rolls against each member; `pledge_step`; `quorum` re-read as presence; a failed matter barred for the holders' terms | **SC's ballot is the ballot.** Each member's draw gains the per-member terms `[VEN C]` wanted, all from the one list (§3.4): his `obligation` toward proposer or rival and his commits, both scaled by `sealed_obligation` under `records_dissent: false`; his `regard` for the proposer; the `evidence` left standing. A commit's size stays SC's `proof_step` (`pledge_step` is withdrawn). `quorum` keeps the code's meaning (fors needed, a head count), or the row carries `quorum_share`. **One tally for every `declared` row**: fors at or above the pass mark: carried (Overwhelming when also two thirds of ballots cast); fors more than againsts and short of it: undetermined, the matter stays docketed (`matter.undetermined`; `election.inconclusive` is withdrawn into it); otherwise dismissed, and the proposer may bring it again (the standing rule's recoverable Failure; `[VEN C]`'s bar is withdrawn) | 1 (SC's proposal and determinism sweep C-14 own it) | PAP B, VEN C |
| X-16 | **`office_bodies.term` and `hand_term`** look like two homes for a hand's patience | not a collision: each is at the owner of the hand (a body's row; a seat's row). Kept as `[BYZ C]`, `[BYZ D]` wrote them | — | — |
| X-17 | **`patronage` against `eligible_from`** | not a collision: the first says through which seats a seat may be **filled** (`may_fill`), the second from which roll a person may be **seated** (`may_seat`). Both are asked by `_req_confer` | — | — |
| X-18 | **`off_duchess_hafenmark.conferral: null`.** `[BYZ]` D-3: content debt. `[COL D]`: `inheritance` with a vacant heir title. `[VEN]`: names the gap | `[COL D]`'s edit 4, as an `[ASSUMPTION]` content edit in FA's file | 4 (`off_king`'s shape, IN-61) | BYZ (audit note only) |

### 2.3 Obstacle terms and fixtures

| # | collision | decision | step | reconciled in |
|---|---|---|---|---|
| X-19 | **`[BYZ]` composes obstacles from `favourable` and `hostile` "steps"**, which are signs, not members of SC-B's roster | every step is re-expressed as a named term (table in §3.4). Two are dropped: the dignity "precedence" step and the founding-confidence step (a dignity acts by publishing its cited deed, `[BYZ]` §6.1; a second path for the same effect is an S defect) | 5 | BYZ A, BYZ B, BYZ C, BYZ E |
| X-20 | **`oath_step` against `obligation`.** `[COL B]` gives the `issue` row "− `oath_step` 0.5 if the addressee holds a live sworn `oblige` to `Act.via`" | that is `[VEN A]`'s `obligation`. `oath_step` is withdrawn | 5 | COL B |
| X-21 | **`provisional_term`**: `[BYZ A]` 4 (sweep 2 / 4 / 8); `14_VERBS_BINDING_C_turnover.md` 2 (sweep 1 / 2 / 4) | the row's owner: VB-C's fixture and value | 5 (one owner per row) | BYZ A, BYZ E |
| X-22 | **The control arm of a new draw.** `[BYZ]` a global `procedure_draws: on | off`. DETERMINISM-A `task_draw_arm: on | off`. VB-C none (its falsifier pins the roll). `[VEN]` ships each size fixture at its control. `[COL B]` declares its rows movers with no equal arm | one style (§3.6). `procedure_draws` is withdrawn: a task row's arm is DETERMINISM-A's `task_draw_arm`; a contest row's control is the pinned roll | 1 (DETERMINISM-A) | BYZ A, B, C, E, F |

### 2.4 Verb rows rewritten by more than one lane

The rule: **a verb row has one owner, the verb lane that built it out; an institution lane supplies terms
and asks for band content.** Detail and the row-by-row outcome are in §3.5.

| # | collision | decision | reconciled in |
|---|---|---|---|
| X-23 | `confer`, `revoke`, `succeed` drawn by `[BYZ A]`, `[BYZ E]` and by `14_VERBS_BINDING_C_turnover.md`, with different band effects and emitted kinds | VB-C's rows. Kinds: `appointment.resisted`, `revocation.resisted`, `succession.contested` (`conferral.declined`, `recall.defied`, `succession.unrecognised` are withdrawn). `[BYZ]`'s terms survive as terms; its two conjuncts on a dignity row (oath first; a cited deed) survive as that row class's eligibility | BYZ A, BYZ E |
| X-24 | `issue`: `14_VERBS_BINDING_D_orders.md` (one roll, a `force` band), `[COL B]` (graded at `remove`, band-gated delivery), `[BYZ C]` (answerable at the last hand), `06_FA_decree_binds.md` (the content deposit) | one roll, VB-D's, with `remove` and `obligation` among its terms; `force` is what `[COL B]`'s four delivery outcomes read; FA-P1's deposit runs at issue for a seat with no `passes_through` and at the last entry for one with | COL B, BYZ C |
| X-25 | `carry`: `13_SC_draw_for_unrolled_contests.md` (docketing a petition) and `[BYZ C]` (entering a document at a hand) | one row, SC's; the hand is its second `requires_typed` alternative; one band shape (entered; delayed one term; returned) | BYZ C |
| X-26 | `requisition`: `[BYZ B]` (contested; `copying`; `requisition.rendered`), `[COL B]` (graded; `stewardship`; `levy_ob`), `14_VERBS_MATERIAL_B_stores.md` §4 (graded; no capability; `stakes_ob.requisition` per third asked; the cohort's `regard`) | the MATERIAL lane's row. The kit adds terms to it (`remove`; `evidence`: a held assessment, a held instrument conferring the seat; `obligation` where the levied cohort is sworn to the seat) and asks for two band contents (Overwhelming emits `requisition.rendered`, outside `standing_routes.dominance`; Partial deposits a shortfall claim for the rest). `levy_ob`, both capability rows and the hunger-band `stakes` are withdrawn (SC's R-6: a lean season reaches a levy through the cohort's `regard` and the share asked) | BYZ B, COL B |
| X-27 | `transfer`: `[COL B]` (rolled only at `remove` ≥ 1; Partial half), `[BYZ B]` ("none: conservation"), DETERMINISM-A (bookkeeping), `14_VERBS_MATERIAL_B_stores.md` §2 (always graded; `carriage`; `delivery_share`) | the MATERIAL lane's row: every `transfer` is drawn, a payment in the room at the floor obstacle. `[BYZ B]`'s stipend payment and `[COL B]`'s tribute are that row. **`carriage` and `remove` are one quantity under two names** (and `14_VERBS_SOCIAL1_B` adds a third, `distance`): this kit uses `remove` and `world_q.remove`, and lists the other two for their lanes and for unification lane U1 | BYZ B, COL B |
| X-28 | `seize`: `[COL B]` and `14_VERBS_MATERIAL_D_paper.md` §6 | the MATERIAL lane's row, plus `remove` | COL B |
| X-29 | the answer to a writ: `14_VERBS_SOCIAL1_B` (the row; `comply` opens an `oblige` carrying `OBEYED_WRIT`), `[PAP D]` (the believer's answer; the complier's decline), `[VEN A]` (`obligation` on the answer), `[COL A]` (a covenant's keeping) | SOCIAL1-B's rows. `[PAP D]` edit 7's decline reads the complier's own live `oblige` carrying `OBEYED_WRIT` (his Tenure, person-side), in place of a search for his newest answer claim. `obligation` counts only edges `gate.py::sworn_to` counts, so an obedience is not an oath for the odds either. A covenant-made instrument is in force by SOCIAL1-B's `world_q.covenant_in_force`, which `dues` and `breaches` ask | PAP D, VEN A, COL A |

**Thirty-one rows; twenty-nine collisions decided, two shown not to be collisions (X-16, X-17).** Outside
the four families and therefore listed, not edited: three names for distance (X-27); `rank_gap`
(`14_VERBS_SOCIAL1_D`) against `standing` (`14_VERBS_BINDING_C`), one quantity; a `dispensation` content
key `standing` (`14_VERBS_SOCIAL1_B` §3) against the obstacle term `standing`; three names for the graded
route roster (`graded_inquiries` in the tree, `graded_tasks` in DETERMINISM-A, `graded_acts` in the
MATERIAL lane); and `20_NARRATIVE_CHURN.md` §7.2's `dues_unmet`, which is the lapsed-oath half of what
`[COL A]`'s `breaches` is the instrument half of.

---

## 3. The one kit

Everything an institution is made of, each with one owner. "New" means new to the tree and asked for by
this kit; "theirs" means another lane's proposal or the plan carries it and the kit composes on it.

### 3.1 The registry: `engine/season/instruments.yaml`

One file, one loader (`data/instruments.py`, unknown keys refused), two sections. Full text:
`proposals/15_INSTITUTIONS_SYNTHESIS_A_one_kit.md`.

**`forms:` — the closed set of what a document can oblige.** Row keys (`[COL A]`'s, plus the three this
synthesis adds, marked †):

| key | values | meaning |
|---|---|---|
| `id` | a name | the form |
| `record_kind` † | `dispensation` (default) \| `debt` | which Record kind carries it |
| `made_by` | `issue` \| `covenant` | down a purview, or across |
| `grantor_act` | a `remit_acts` member | what the making seat must grant |
| `term` | seasons \| null | null: while the grantee holds the conferred seat |
| `renewal` | `grantor` \| `both` \| `none` | who must act for it to run on |
| `confers` | a seat template \| absent | post, `at`, `remit_acts`, `conferral`, `revocation`, and optionally `audit_at_exit` |
| `due[]` | `{by, kind, every, to}` | a deed owed: `by` ∈ grantor, grantee, addressee; `kind` a `DEED_KINDS` member; `every` seasons or `once`; `to` ∈ grantor_rung, grantee_rung, grant_ground, named_rung |
| `forbears[]` | `{by, kind, over}` | a deed forborne: `over` ∈ grant_ground, grantee, named |
| `lapse` | `reverts` \| `stands` | at maturity unrenewed |
| `hardens` | bool | does age held add evidence weight (prescription) |
| `bearer` † | bool, default false | the entitled party is whoever holds the Record; the bound party is whoever holds a live `commit` to its `terms` |
| `recites` † | bool, default false | the instrument may carry a `recites` list (it certifies deeds) |

Two kinds of clause, one schema: a clause whose `by:` is `grantor` or `grantee` is **kept or broken** by a
party who made the bargain (read by `kept` and `breaches`); a clause whose `by:` is `addressee` is
**answered** (the addressee's `comply` or `evade / defy`, his draw, and what he then does or declines).
Neither is ever a gate.

**The sixteen forms.**

| form | from | made by | carrier | what it is |
|---|---|---|---|---|
| `homage` | `[COL]` | covenant | dispensation, recites | the bond of a conquest-founded house to the crown |
| `land_grant` | `[COL]` | issue | dispensation, recites | ground given for settlement; confers a lord's seat |
| `march` | `[COL]` | issue | dispensation, recites | a frontier on wide powers; confers a warden's seat |
| `farm` | `[COL]` | covenant | dispensation | a ground's revenue for a term; confers a farmer's seat, audited at exit |
| `charter` | `[COL]` | issue | dispensation, recites, hardens | a town's or a body's self-rule; confers an elected head |
| `staple` | `[COL]`; `[VEN D]`'s trade charter | issue | dispensation, hardens | a body's right to trade a kind at a place |
| `immunity` | `[COL]`; `[PAP C]`'s settlement charter | issue | dispensation, hardens | a jurisdiction left alone |
| `tribute` | `[COL]` | covenant | dispensation | payment for peace or protection |
| `wardship` | `[COL]` | covenant | dispensation | a person of one house kept at another's court |
| `capitulation` | `[COL]` | covenant | dispensation | terms on which a place is given up |
| `warrant` | `[VEN C]` | issue | dispensation | admission to a roll kept by warrant |
| `commission` | `[VEN D]`; `[PAP E]`'s legate | issue | dispensation | what a seat held at distance may and may not do |
| `avoidance` | `[PAP D]` | issue | dispensation | addressees forbear named dealings with a named person |
| `interdict` | `[PAP D]` | issue | dispensation | the issuer's own seat-holders in a place withhold named services |
| `tithe` | `[PAP E]` | issue | dispensation | addressees render a share each season to a named rung |
| `debt` | `[VEN B]` | covenant | `debt`, bearer | a stated amount of a kind owed at a place by a date |

Not forms, and why: `recognition` (a certificate is the `recites` key, X-03); `purchase` of office
(composed: a `transfer` and then a `confer` or a `warrant`, findable for that reason; `[VEN]` §5.3 by the
precedent of #453 row 38; `[COL]` §11 item 2 is closed by it, §10); `corvee` (§10, for Jordan); a treaty of
alliance (`covenant`'s remaining deferred reader, CP-T09-03).

**`seeded:` — the Records a world begins with.** Row keys: `id`, `kind`, `form`, `via` (the seat it was
made through), `held_at` (the seat whose holder keeps it), `to`, `at`, `terms`, `amounts`, `recites`,
`source`. One builder pass mints each through the existing mint; a vacant `held_at` is skipped and
reported (`[PAP C]` edit 2). A case file's `setup.instruments` (`[COL E]`) uses the same row. §4.3 lists
the seeded rows.

**Readers** (Queries; nothing stored; no MATTER pass):

| reader | side | what it answers | from |
|---|---|---|---|
| `world_q.instrument_of(w, record)` | world | the form a Record names | `[COL A]` |
| `world_q.in_force(w, record)` | world | covenant-made: both parties' live commits (`covenant_in_force`, `14_VERBS_SOCIAL1_B`); issue-made: unmatured stages | this synthesis (one owner of "is it live") |
| `world_q.owed(w, record, clause)` | world | amount named by the clause this period, less what the log counts toward it | `[VEN B]`'s `debt_state`, generalised |
| `world_q.dues(w, pid)` | world (an occasion source, as `vacancies` is) | the clauses that bind `pid` with `owed > 0`, as classed referents | `[COL A]` |
| `person_q.kept(p, record)` | person | what `p` believes of the other side's keeping | `[COL A]` |
| `world_q.breaches(w, pid)` | reads `pid`'s ledger only | where `kept < 0`, the other party and the conferred seat, as referents | `[COL A]` |
| `person_q.forborne(p)` | person | the dealings `p` has undertaken to forbear by his own `comply` (his live `oblige` carrying `OBEYED_WRIT`) | `[PAP D]` edit 7, generalised to read the form |

### 3.2 The record-kind scheme

| the thing | its one carrier | new? | not |
|---|---|---|---|
| a deed | an Event of a `DEED_KINDS` kind; claims of it in ledgers | exists | a stored rank |
| a certificate of deeds | a Record carrying `recites`: a `resolution` (hearing-made, CR-36) or a `dispensation` of a reciting form | content key new; `resolution` is the plan's | a `roll` kind; a `recognition` form; `attests: n` |
| a grant, a treaty, a writ, a warrant, a commission, a sanction published | a `dispensation` naming a form | content keys `form`, `amounts` new | a `Charter` kind |
| a debt, a bond, a share, a fine, an arrear | a `debt` Record | **new** (K-14) | a creditor's lever (D-5 stands) |
| a dignity | a `hold` on a seat row carrying `dignity:` | key new | a `Title` type; a prestige stock |
| an office | a `hold` on a seat row with a remit | exists | |
| a roll (a membership) | the `oblige` Tenures to a seat whose `binds` is `members_by_warrant` | roster member new | a Record |
| a stipend, a wage, a retainer | the seat's `upkeep`, paid by `transfer`, renewing a termed `oblige` | key for an existing field | a salary object |
| an assessment | the `faction_sheet` Record `survey` mints | exists | a cadastre |
| a case file, a quittance, an admonition | the plan's Record of a matter (CR-61); SC's acquittal Record | theirs | |
| a sanction | `ban`, `detain`; closed by `pardon` | exists | an `excommunicate` verb |
| a house, a branch, a chapter, a Kontor | a head seat on a `hearth` rung (`{venue:}` anchor) with stores and sworn dependants | anchor form new | a `Company` faction kind; a `Colony` rung kind |

### 3.3 The seat row

Eight keys are new with this kit. With the three other lanes add, a row can say everything an
institution's office is.

| key | type, default | says | single reader | from | cut test (what dies) |
|---|---|---|---|---|---|
| `dignity` | int 1..`dignity_grades`; absent | this seat is an honour of that grade, with no remit and for life | `world_q.upkeep_owed`; the loader's refusals | `[BYZ A]` | stipends cannot differ by rank; the court is flat |
| `upkeep` | int ≥ 0; `default_upkeep` | what the seat owes each sworn person per term | `world_q.upkeep_of` / `upkeep_owed` | `[BYZ B]` (the field exists) | the unpaid court; the house that keeps clients |
| `passes_through` | list of body names or `{seat: id}`; absent | whose hands this seat's instruments pass | `_declared_stages` | `[BYZ C]` | the clerk's veto; NPC-008, -009, -011 |
| `hand_term` | seasons; `record_stage_term` | how long a paper may wait at this seat when it is a hand | `_declared_stages` | `[BYZ D]` | distance as a person |
| `patronage` | list of `patronage_bases`; `[purview]` | through which seats this seat may be filled | `gate.py::may_fill` | `[PAP B]` | the investiture contest; a Church not a royal department |
| `eligible_from` | a seat id; null | only persons on that seat's roll may be seated here | `gate.py::may_seat` | `[VEN C]` | guild-gated office; capture at the roll |
| `cooling_off` | seasons; null | no re-seating within that long of a hold that ended by term | `gate.py::may_seat` | `[VEN C]` | rotation (else the incumbent returns each term) |
| `audit_at_exit` | an arrangement id; null | when a hold here closes, those who may open that hearing are told | the occasion `world_q.audits_due` | `[VEN C]`, `[COL C]` (X-12) | the account at the end of an office |
| `term` | seasons; null | the hold matures | `_eff_confer` | theirs: FA-P3, FA-B3 | |
| `scope` | an anchor; the rung | where the seat's bench judges | `sits_over` | theirs: CR-60 | |
| `vocation` | a vocation; null | what the post calls on | the conferee ranking | theirs: FA-P6 | |

Roster members the rows draw on: `conferral_bases` gains `lot` (`[VEN C]`); `binds_bases` gains
`members_by_warrant` (`[VEN C]`); a new roster `patronage_bases: [purview, own_faction]` (`[PAP B]`);
`revocation_bases` gains `head_of_faction` only if Jordan rules it (§10 item 2); `FILLED_BY["annex"]`
gains the taking basis (`[COL D]` edit 5; FA's). One anchor form is added to the resolver: `{venue:
<building id>}` (`[VEN D]`).

A hand that is a body takes its patience from `rosters.yaml: office_bodies.<body>.term` (`[BYZ C]`); that
is the body's row and not a second home (X-16).

### 3.4 The obstacle terms

SC-B's roster is the list. Three members are added for institutions; every odds source any family lane
named is one of the thirteen, or is leverage, or is the chooser's.

| term | sign | what it is | owner of the reading | size fixture | from |
|---|---|---|---|---|---|
| `difficulty` | + | the act in itself | the verb row's `difficulty:` | `difficulty_ob` | SC-B |
| `opposition` | + | the person acted against | his score ÷ 2 (`opposed_ob`) | — | SC-B |
| `standard` | + | what the room demands | the arrangement row's or the market venue's `standard:` | `difficulty_ob` | SC-B |
| `subject` | + | what the thing examined puts in the way | `Record.forgery_quality` | — | SC-B |
| `stakes` | + | the weight of what the act would do | `stakes_ob` by the Tenure kind opened or closed, or by the share of a store asked | `stakes_ob` | SC-B; MATERIAL-B |
| `regard` | ∓ | how the one acted upon is disposed to the actor | `person_q.stance_toward` | `regard_step` | SC-B |
| `reception` | ∓ | how the audience is disposed | `world_q.reception` over an `audience`; for the prize `a seat` each member's reading is `person_q.legitimacy(q, person, seat)` | `reception_gain` | SC-B; VB-C; this synthesis |
| `capability` | ∓ | a capability the situation rewards | `tables.capability_uses` circumstance rows | per row | SC-B; DICE |
| `evidence` | ∓ | what is held, cited and left standing | SC's evidence weight; a certificate weighs by its `recites` left standing; a hardening form by its age held | `proof_step`; `prescription_seasons`; `penance_weight` | SC-B; `[COL C]`; `[PAP D]` |
| `plea` | ∓ | a concession's reward | CR-62 | `plea_step` | SC-B |
| `standing` | ∓ | how far the person acted on, or for, stands above or below the seat | the gate's rank reader | `standing_step` | VB-C |
| **`obligation`** | ∓ | what the one acted upon owes, by an edge he owns | `person_q.owed_to` (edges `sworn_to` counts; commits to the terms of a Record the actor holds) | `obligation_step`, `obligation_arrears`, `sealed_obligation` | `[VEN A]` |
| **`remove`** | + | how far the actor stands from what he acts on | `world_q.remove` | `remove_step`, `border_hops` | `[COL B]` |

Also used, from another lane's addition: `backlog` (`14_VERBS_SOCIAL1_D`: items waiting on a desk), which is
`[BYZ C]`'s clerk's backlog.

How each family's odds sources map (the reconciliation of X-19, X-20):

| the lane wrote | it is |
|---|---|
| `[BYZ]` "a cited deed held firsthand"; "a held Record of the matter"; `[PAP]` "the deeds cited and the answers standing"; `[VEN]` "the bond", "deeds cited"; `[COL]` "a held assessment", "the warrant", "the instrument and its age", "a recognition" | `evidence` |
| `[BYZ]` "the conferee's regard for the conferrer"; "the clerk's regard for the maker"; `[VEN]` "the lender's regard" | `regard` |
| `[BYZ]` "the mean regard for the conferee among the body"; "minus the mean `legitimacy` over three sets"; `[PAP]` "`reception` of the seat's body"; `[COL]` "the cohort's regard" where a bench or a body hears | `reception`, with the audience named |
| `[BYZ]` "the maker sworn to a seat the clerk is sworn to"; "a person sworn to the exercised seat resides under the place"; `[COL]` `oath_step`; `[VEN]` every tie | `obligation` |
| `[BYZ]` "by the rung kind of the seat's rung"; VB-C's rank gap | `difficulty` (the row's level) and `standing` |
| `[BYZ]` "one step per open document beyond his scene budget" | `backlog` |
| `[BYZ]` "one step per other living eligible claimant" | `opposition`, when the rival has docketed a claim; otherwise nothing (a rival who does not act opposes nobody) |
| `[BYZ]` "an open floor raises it"; `[PAP]`, `[COL]` publicity | `standard`, authored on the row (SC's R-5) |
| `[BYZ]` "`conviction_stand(altonian_civics)` above zero"; `[PAP]` conviction; `[COL]` temperament | **not an obstacle term**: leverage through CHAR's ground rule (`02_CHAR_which_ground_moves_whom.md`), or the chooser's ranking |
| `[BYZ]` the hunger band as `stakes`; `[COL]` `levy_ob` | withdrawn: the share asked is `stakes` (MATERIAL-B's table); hunger reaches the roll through `regard` |
| `[BYZ]` dignity "precedence"; founding confidence | withdrawn (X-19) |
| `[VEN D]` the `charter` term on `exchange` | `evidence` (X-10) |
| `[COL]` distance | `remove` |

### 3.5 The verb rows: one owner each

No verb is added by any family or by this synthesis. Thirty-one of the 67 rows carry institutional
content. For each, the row's owner and what the kit adds to it.

| verb | row owner | the kit adds |
|---|---|---|
| `confer` | `14_VERBS_BINDING_C` | on a `dignity` row: the conferee's live oath to the conferring seat and a cited deed claim are required, and the cited deed is told at the act's reach at Overwhelming and Success (`[BYZ A]`); `may_fill` reads `patronage` (`[PAP B]`); `may_seat` reads `eligible_from` and `cooling_off`; on a `lot` seat the conferee is drawn (`[VEN C]`); `reception` reads `legitimacy` |
| `revoke` | `14_VERBS_BINDING_C`; FA-P1 | nothing but terms. **Listed for that lane:** its Partial "unseats without the disposal" sets aside the ruled disposal of 2026-10-21 (`gate.py::REVOCATION_DISPOSAL` `[via BYZ]`); `[BYZ E]`'s Partial (the hold closes at the season's end, the disposal with it) keeps the ruling and is the form this kit's gates assume |
| `succeed` | `14_VERBS_BINDING_C` | `reception` over three audiences reading `legitimacy(q, claimant, seat)` (`[BYZ E]`): the seat's body and the seats beneath, the persons sworn to the seat, the residents where its holder last resided; a held certificate naming the seat is `evidence` |
| `establish` | `14_VERBS_BINDING_A` | founds the seat a form `confers:`; a see, a legation, a house's branch are rows |
| `issue` | `14_VERBS_BINDING_D` | `form` as a choice-sourced operand; `remove` and `obligation` among its terms; `force` gates FA-P1's deposit as `[COL B]` tabled it; with `passes_through`, the deposit waits for the last hand |
| `dispatch` | `14_VERBS_BINDING_D`; CP-T09-08 | the inspector, the legate, the commissary are persons sent |
| `carry` | `13_SC_draw_for_unrolled_contests` | the hand as a second `requires_typed` alternative; `backlog`, `regard`, `obligation`, `subject` as terms; bands entered, held over one term, returned (X-25) |
| `comply`, `evade / defy`, `construe` | `14_VERBS_SOCIAL1_B`; FA-P1 | `obligation` toward the issuing seat; `regard` toward a named person (it is hard to shun a friend); the complier's `forborne` set |
| `covenant` | `13_SC` (acceptance); `14_VERBS_SOCIAL1_B` (drafting, in force) | `form`; mints a `debt` when the act names `kind` and `amount` |
| `determine` | SC; `13_SC` (the ballot); SC-P4 (bands) | the tally of X-15; `quorum_share`; rows of §3.7; `ban.opened`, `detention.opened` (`[PAP D]`); a Record disposal may carry `recites` |
| `open_case`, `convene`, `speak`, `argue`, `petition` | SC; `14_VERBS_BINDING_B`; the social lanes | the audit, the calling-in, the suit, the consecration, the candidacy, the ask (`[VEN A]`: `obligation` is the only change) |
| `pardon` | `14_VERBS_BINDING_B` | a matured penance is `evidence` (`[PAP D]`) |
| `oblige`, `release` | `14_VERBS_BINDING_A` | the warrant clause for `members_by_warrant` (`[VEN C]`) |
| `requisition` | `14_VERBS_MATERIAL_B` | X-26 |
| `transfer` | `14_VERBS_MATERIAL_B` | counts toward a `debt` or a `due` when made to the clause's place (`[VEN B]`); `_renewals` pays `upkeep_owed` (`[BYZ B]`) |
| `exchange` | `14_VERBS_MATERIAL_B` | a held `staple` is `evidence`; a market's `standard` |
| `seize` | `14_VERBS_MATERIAL_D`; `14_VERBS_PHYSICAL_A` | `remove`; a lapsed `debt` held by an officer is the warrant's stand-in for a distraint by `requisition` (`[VEN B]`) |
| `give` | `14_VERBS_SOCIAL1_B` | handing a bond on assigns it; handing it to the debtor cancels it |
| `tell`, `research`, `survey`, `forge`, `destroy_record`, `conceal` | FI; `14_VERBS_MATERIAL_D`; `14_VERBS_SOCIAL2_B` | telling what a held certificate recites is commemoration; a forged or burned certificate is the next hearing's missing proof |

### 3.6 One fixture style

Every number the kit proposes obeys five rules. A family number that did not is brought into line by its
`Reconciled:` line.

1. **It is a row of `engine/season/data/fixtures.py`**, read by one named function, with a NUMBER row in
   `hole_register.yaml` graded `assumption`.
2. **It has a unit**: obstacle units (net successes), seasons, whole units of a `matter_kinds` member,
   hops, a dimensionless gain, or a per-mille share.
3. **It ships at its control value** (the value at which the world's hash is unchanged), in the commit
   that lands its reader. The move to the proposed value is its own commit and a declared hash mover.
4. **It has a sweep of three or four points that includes the control.**
5. **A draw replacing a fold has no size fixture as its control.** A task row's control is
   DETERMINISM-A's `task_draw_arm: off`; a contest row's control is the roll pinned to Success, planted in
   the gate. Set-up acts in a scenario run under the pinned roll so the situation is the same at every
   seed (`[BYZ F]`), and play runs unpinned.

| fixture | unit | control (ships) | proposed | sweep | reader | from |
|---|---|---|---|---|---|---|
| `obligation_step` | Ob per live edge | 0 | 0.5 | 0, 0.25, 0.5, 1.0 | `roll.py::obstacle` | `[VEN A]` |
| `obligation_arrears` | fraction of an edge within a season of maturity | 1.0 | 0.5 | 0.5, 1.0 | same | `[VEN A]` |
| `sealed_obligation` | fraction under `records_dissent: false` | 1.0 | 0 | 0, 0.5, 1.0 | same | `[VEN A]` |
| `remove_step` | Ob per hop | 0 | 0.25 | 0, 0.25, 0.5 | same | `[COL B]` |
| `border_hops` | hops across a root | — (inert at `remove_step` 0) | 2 | 1, 2, 3 | `world_q.remove` | `[COL B]` |
| `presumption_gain` | dimensionless, per holder back | 0 | 0.5 | 0, 0.5, 0.75, 1.0 | `person_q.legitimacy` | X-07 |
| `prescription_seasons`, `prescription_cap` | seasons per unit of proof weight; units | cap 0 | 8; 3 | 4, 8, 16; 1, 3, 5 | SC's evidence weight | `[COL C]` |
| `penance_weight` | proof-weight units | 0 | 2 | 0, 1, 2, 4 | the `pardon` host input | `[PAP D]` |
| `dignity_grades` | count | — (loader bound) | 5 | 3, 5, 7 | the `offices.yaml` loader | `[BYZ A]` |
| `credit_terms` | owed ÷ advanced, by the loan ask's band | 1.0 flat | 1.1, 1.25, 1.5 | flat; these; steeper | the computed `covenant` amount | `[VEN B]` |
| `hand_term` default | seasons | `record_stage_term` (1) | per row | 1, 2, 4 | `_declared_stages` | `[BYZ C]` |

Theirs and read by the kit: `provisional_term`, `standing_step` (VB-C); `regard_step`, `stakes_ob`,
`difficulty_ob`, `proof_step` (SC-B); `oblige_term`, `default_upkeep`, `record_stage_term` (exist);
`delivery_share` (MATERIAL-B); `recall_suspicion` (FA-P1); `confer_fit_weight` (FA-P6). Withdrawn by the
ledger: `founding_confidence`, `procedure_draws`, `pledge_step`, `oath_step`, `levy_ob`.

Content numbers are not fixtures and sit on their rows: a seat's `upkeep`, `term`, `cooling_off`,
`hand_term`; a row's `quorum_share`; a seeded instrument's `amounts`; the count of seeded deeds.

### 3.7 The arrangement-row vocabulary

Keys: the thirteen of `arrangements.yaml`, SC-B's `standard:`, SC-P4's band-mapped `disposes:`, and two
this kit asks for: **`quorum_share: [n, d]`** (`[PAP B]`; declared rows only; exclusive with `quorum`) and
one more cell value for a band map, **`release`** (`[COL C]`: a closing disposal; a request to SC, with
`[COL C]`'s data fallback). No other key. SC-P4's warning applies to every row below: a key no reader
reads when B10-18c closes leaves with that batch.

| row | from | disposal | disposes (by band) | what it is |
|---|---|---|---|---|
| `acclamation` | `[BYZ E]` | none | none | a person before a crowd; what it produces is what those present heard |
| `conclave` | `[PAP B]` | declared, `quorum_share: [2, 3]` | hold | the election of a head by its own bench |
| `consecration` | `[PAP C]` | bench | Record (a certificate) | a body attests a claimant's deeds for a seat |
| `general_council` | `[PAP E]` | declared, `quorum_share: [2, 3]` | Record | held until §10 item 3 is ruled |
| `audit` | `[COL C]` (X-12) | bench | O `ban`, S `oblige`, P Record | an officer answers on the ground he governed |
| `quo_warranto` | `[COL C]` | bench | O, S `release`; P `oblige` | by what warrant do you hold |
| `debt_suit` | `[VEN B]` | bench | O `ban` or `detain`, S `oblige`, P a new stage | a creditor's suit |
| `security_bench` | `[VEN D]` | declared | `detain` | the secret bench |
| `enrolment_ballot` | `[VEN D]` | declared | `oblige` (onto the roll) | a body votes a candidate onto its roll |

Enrolment of a house's deed by the Court Parliament needs no new row: it is `determine` under the existing
`parliamentary_debate` once CR-36 gives a Record disposal a site (`[BYZ]` §7.1), and what it mints is a
certificate.

### 3.8 Emitted kinds the kit adds

`ban.opened`, `detention.opened` (`[PAP D]`); `debt.lapsed` (`[VEN B]`); `lot.seen`, `lot.empty`
(`[VEN C]`); `document.entered`, `document.held`, `document.returned` (`[BYZ C]`; SC's `case.declined` is
`document.returned` on a petition, listed for SC); `matter.undetermined` (X-15); and, asked of the
MATERIAL lane, `requisition.rendered`. Withdrawn: `conferral.declined`, `recall.defied`,
`succession.unrecognised`, `election.inconclusive`.

---

## 4. The deed ledger: the shared currency of legitimacy

Jordan, 2026-11-12: *"current kingdom royalty is because of nobility by deed/achievement"*; *"Royalty by
noble conquest, i.e. the first king had the greatest accomplishment in the secession war, followed by
the first Duke of Hafenmark and the first Duke of Varfell."* Exact edits:
`proposals/15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`.

### 4.1 Four layers, one carrier each

| layer | what it is | carrier | whose | does it last? |
|---|---|---|---|---|
| **the deed** | something a person did | an Event of a `DEED_KINDS` kind | the world's | it happened |
| **the memory** | what a person holds of it | a deed claim in his ledger, firsthand or told | each person's | no: claims fade (34,837 `claim.decayed` Events in three seasons at seed 0, `[via PAP]` E-1; `01_CORE_claim_fade_as_read.md`) |
| **the certificate** | a deed a body or a seat has put its name to | a Record carrying `recites` (§3.2) | whoever holds it | yes, while the paper lasts and is honestly kept |
| **the standing** | what a person makes of a holder | `person_q.legitimacy`, computed when read | each person's | as long as the memories under it |

In engine vocabulary a "ledger" is a person's own claims. What Jordan calls the ranked ledger of
accomplishment is therefore two things that must not be confused: **each person's ledger of deeds** (what
he holds; it ranks houses differently for different people and is never stored as a rank) and **the kept
certificates** (what the institutions hold on paper). The second exists to feed the first: a certificate
does nothing by existing. It is cited as `evidence` in a hearing, and its keeper can tell what it recites,
which puts the deed back into living ledgers. That is the whole of what an institution of legitimacy does,
and it is why the keepers matter.

### 4.2 Standing, in one formula

```
legitimacy(p, holder, seat) =
      stance_toward(p, holder)                                               (exists)
    + Σ deed_term(p, c)   over holder's own deeds p holds, from the window     (exists)
    + Σ over k ≥ 1 of  presumption_gain^k · Σ deed_term(p, c)
            over the deeds p holds of the k-th prior lawful holder of `seat`   (new: the chain)
```

- **The chain is `p`'s own.** The prior holders are read from `p`'s claims of `tenure.opened` and
  `tenure.closed` naming the seat (the reader `14_VERBS_BINDING_C` edit 9 and the narrative lane's
  believed-holder reading both need; one reader). A seat whose history `p` does not know contributes
  nothing: an heir is a nobody to a stranger.
- **It is cut by force.** Where `p` holds a `standing_routes: dominance` deed of some holder whose subject
  is the seat or its rung, the chain stops at that holder (`[BYZ A]`'s `_took_by_force`). A man who takes
  a seat by force inherits nothing and starts his own chain with his own deed, which is exactly what the
  first king did.
- **A predecessor's deeds are read whenever held, not from the window.** Their age is the claim's own:
  they fade, and are held again when retold. So presumption is not a number a house has. It is what is
  still remembered of what its seat's holders did, at a discount per holder.
- **It is one methodology.** Scoring is `deed_term`; nothing is weighted that `regard` does not already
  weigh. At `presumption_gain` 0 the function is today's.

What follows without any further rule:

| the fixed point asks | answer |
|---|---|
| what counts as a deed | any `DEED_KINDS` Event; what it is worth is each observer's pursuits against `tables.alignment` (`[BYZ]` §6.2; `[PAP]` §2.2; `[COL]` §5.3 agree) |
| who certifies it | a body or a seat, by a drawn act that cites it (§4.3). Never a rule |
| what it costs to claim | a petition, a sitting, the proofs brought, exposure to rebuttal, and a failed claim is known; for the certifier, a stipend for life where the certificate is a dignity |
| how it passes to heirs | down the **seat**, at `presumption_gain` per holder, and only through deeds a person still holds a claim of. Blood enters only where a seat's `conferral` is `inheritance` and an heir title exists |
| how it fails to pass | the memory fades and nobody retells it; the paper is burned, forged or withheld; the seat was taken by force; the heir does nothing and the discount compounds |
| how it is renewed | the holder's own deeds, witnessed or told; his own certificate; the keeper's telling |
| how a rival's deed unseats it | the rival's fresh deeds in enough ledgers move the `reception` of every `succeed`, election, deposition and recall, and move each sworn man's own choice to `release`. No threshold fires; persons act on their own readings and the draw decides each act |
| how a new accomplishment raises a house | a certificate for the seat: a consecration, an enrolment by the Court Parliament, a grant that recites the deed. From then the deed has a keeper and outlasts the memories |
| what a conquest-founded house owes and is owed | the `homage` form: it owes a relief at each succession and (by the oath itself) the muster and the summons; it is owed re-issue at each succession and the grantor's forbearance on its ground (canon `:88`) |

### 4.3 Who keeps, who certifies

| body | certifies by | leaves | kept by | its leverage |
|---|---|---|---|---|
| **the Church** | `determine` under `consecration`, on a claimant's petition naming a seat | a `resolution` reciting the deeds left standing | the archive (the Cardinal of Temperance's seat) | it can decline to consecrate, decline to tell, and consecrate a rival |
| **the Crown's court** | `confer` of a dignity citing a deed | a `hold` on a dignity seat; the cited deed told at the act's reach | nobody: the dignity is the record and ends with its holder | whom it honours, and whether it can pay them |
| **the Court Parliament** | `determine` under `parliamentary_debate` (CR-36's site), on a petition carried through the chancery | a `resolution` reciting, for a seat | the chancery (the Chief Parliamentary Clerk) | the clerks' hand on the petition; custody of the paper |
| **a grantor** (crown, duke, head of a house) | `issue` or `covenant` of a reciting form | a `dispensation` that recites the service it rewards | its holder | re-issue at each succession; `quo_warranto` |
| **the Skald-Chief** | his endorsement of a deed-claim in Varfell (`offices.yaml:523` `[via BYZ]`) | whatever his `determine` disposes; and his telling | himself: the archived design calls him "keeper of the oral law" (intent only) | a certificate kept in a man dies with him |
| **a guild, a commune, a republic** | `enrolment_ballot` | an `oblige` onto its roll | the roll-keeper's seat | who is put to the ballot; whose term is renewed |

Six certifiers, one act shape: **a drawn act that cites deed claims as `evidence`, and on success tells
them and leaves something durable another hearing can cite.** No certifier is above another. A deed
certified by one body is contested before another by citing against it, by a rival certificate, or by
calling the grant in; which reading a room takes is that room's draw.

### 4.4 The order of the Secession War, as the world begins

The order is carried once, as things that happened (X-05), and twice on paper, in two institutions'
keeping (X-08). Every row is `[ASSUMPTION; Jordan to correct]` except the order itself.

**Prehistory (Events through the gate, before tick 0; ARCS' route):** three founders, dead at build, each
with a `hold` on his seat opened and closed in prehistory, and `field.won` Events as doer: the first
Almqvist three, the first Duke of Hafenmark two, the first Duke of Varfell one. The cast is told them at
build. The first Almqvist's death is a `person.died` with no doer in anyone's ledger (canon `:116`).

**Seeded instruments (`instruments.yaml: seeded`):**

| id | kind, form | made through | to | recites | kept by |
|---|---|---|---|---|---|
| `ins_containment_charter` | `dispensation`, `immunity` | `off_king` (the grant "preserved and expanded" at the settlement, canon `:104`) | the Confessor | — | the Cardinal of Temperance (the archive) |
| `ins_consecration_first_king` | `resolution` | `off_confessor` | — | the first king's three deeds, for `off_king` | the Cardinal of Temperance |
| `ins_settlement_hafenmark` | `dispensation`, `homage` | `off_king` | the Duchess of Hafenmark | her founder's two deeds, for `off_duchess_hafenmark` | the Chief Parliamentary Clerk (the chancery) |
| `ins_settlement_varfell` | `dispensation`, `homage` | `off_king` | the Duke of Varfell | his founder's one deed, for `off_duke_varfell` | the Chief Parliamentary Clerk |

The Grand Master's oath stays a bare oath (`[COL D]`: the Löwenritter's bond is not this kit's to name).
The Altonian trade treaty and Schoenland's privileges are seeded rows of the same schema in the batch that
seats those places (§9, batch I-7).

What this start produces before anyone acts:

- **Three presumptions in Jordan's order**, in most ledgers, each at half its founder's deeds, and not in
  all: a person whose pursuits do not prize a field won ranks them otherwise, and that is correct.
- **A king whose certificate is the Church's to cite or withhold**, and two dukes whose certificates sit
  in a clerk's chest in the capital, in a ministry some persons mean to purge (`purge_altonia`). No house
  holds its own paper.
- **A Duchess with the second deed, no heir and no consecration**; a Duke with the third deed, elected
  by Jarls, whose founder's deed the Settlement recites as one.
- **Founders' deeds that begin to fade from tick 1** unless somebody tells them.

### 4.5 The tree's four disagreements with the fixed point (`[VEN]` §4.4), each decided

| # | the tree says | decision | carried by |
|---|---|---|---|
| 1 | canon `:76`: the coalition is "primarily northern", the south "geographically peripheral"; `:96`: the caste follows "the south's exclusion from the war coalition's leadership". Jordan ranks the first Duke of Varfell's accomplishment third in that war | **Jordan's word governs the world.** The south fought and its commander's deed ranked third; it was then relegated in the settlement despite the deed. Canon is ratified text and is not edited here: the amendment is drafted below for Jordan's hand (§10 item 1 gives the two readings) | §4.6; the seeded count for Varfell |
| 2 | `offices.yaml: off_duke_varfell.conferral: elected` ("first among the Jarls, not a monarch"); whether the present Duke is of the first Duke's line is stated nowhere | **Both stand, and the question of his line does not need an answer.** The deed founded the seat; the Jarls fill it; standing passes down the seat, so whoever the Jarls lawfully seat inherits the presumption at the discount. The seeding assumes one step from founder to present holder for all three seats; intermediate holders are content Jordan may add | no edit; §4.6 amendment A2 says it in canon's words |
| 3 | `off_duchess_hafenmark.conferral: null` and no `successions` row: the second house's seat cannot be filled at all | **`inheritance`, through a title nobody holds at build** (`[COL D]` edit 4, by `off_king`'s precedent). Hafenmark's succession is then open from the first season, which is canon ("unmarried, childless, heirless", `:143`) | proposal B edit 6, in FA's file |
| 4 | nothing in code ranks accomplishment | **nothing should.** The order exists as three founders' seeded deeds and is read by `legitimacy`'s chain, per observer. A stored rank would be a second ladder and a stored aggregate | proposal B edits 1 to 3 |

Two further disagreements the family lanes found, closed here: the archived faction canon's "a war of
unification" (`[BYZ]` D-4) is archived wording and canon's timeline governs; NPC-011's archived placement
over "T11/T12 Altonian provinces" (`[BYZ D]`) cannot stand against the geography file and he is seated off
the map.

### 4.6 Canon amendment, drafted for Jordan — NOT APPLIED

This lane edits no canon. If Jordan takes reading A of §10 item 1, the text below is what
`canon/03_canonical_timeline.md` would say. Old text is quoted from the file at the lines named.

**A1, line 76, last sentence.**
- old: *"The coalition is primarily northern — the southern provinces (Lupicco) are geographically
  peripheral and culturally stigmatised."*
- new: *"The coalition is led from the north. The southern provinces (Lupicco) lie far from the war's main
  theatre and are culturally stigmatised, and they fight: the war's third-greatest accomplishment is a
  southern commander's."*

**A2, line 90.**
- old: *"**Cadet branches as deed-families.** Ducal and ministerial families earned proximity to power
  through Secession-era service, not genealogical relationship to the Almqvist line. The Baralta family's
  ducal status was earned through wartime deeds."*
- new: *"**The founding order.** The crown and the two ducal seats were won by accomplishment in the
  Secession Wars, in this order: the first Almqvist, the first Duke of Hafenmark, the first Duke of
  Varfell. **Deed-families.** Ducal and ministerial families earned their place through Secession-era
  deeds, not genealogical relationship to the Almqvist line. The Baralta family's ducal status was earned
  through wartime deeds, as was the ducal seat of Varfell; in Varfell the deed founded the seat and the
  Jarls choose who sits in it."*

**A3, line 96.**
- old: *"The informal caste relegating southern Einhir to second-class status is the structural
  consequence of the south's exclusion from the war coalition's leadership, not a formal legal act."*
- new: *"The informal caste relegating southern Einhir to second-class status is the structural
  consequence of the settlement's ranking the south's deed last and seating none of its commanders in the
  settlement's councils, not a formal legal act. The south fought, won, and was relegated despite it."*

**Under reading B** lines 76 and 96 stand, and one sentence is added at the end of line 90: *"The first
Duke of Varfell's accomplishment, the third of the war, was acknowledged in the north late and
grudgingly; in the south it was never in doubt."*

**A4, line 92 (hygiene, independent of the reading).** *"the Coup Counter and Motion of No Confidence are
the enforcement mechanisms"* names a counter Layer 1 refuses (`[via PAP]` §2.1). Offered: *"it is enforced
by what a rival's deeds can do: a claim made before those who must accept it, and a Motion of No
Confidence."*

<!-- append-point -->

