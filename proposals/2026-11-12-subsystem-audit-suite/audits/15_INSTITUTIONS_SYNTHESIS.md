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
institutional verbs that execute with no draw), and (b) twenty-eight collisions among the lanes themselves and with the
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
| X-30 | **The currency of a stipend.** `[BYZ B]` bills the court in `coin`; `[VEN B]` denominates every instrument by `kind` because `coin` has no producer and no holder in the built world | `upkeep` is owed in units of whatever matter the paying `transfer` carries; the bill's shortfall claim names `default_store_kind` until SE gives `coin` a producer (§7.5) | 5 (one currency model) | BYZ B |

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

**Thirty rows; twenty-eight collisions decided, two shown not to be collisions (X-16, X-17).** Outside
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

---

## 5. The interlock map

Seven parties. None is a type: each is a set of seats under a faction or a body, and each row below is
made of the kit's primitives and existing verbs. Exact edits for the crossings that need one:
`proposals/15_INSTITUTIONS_SYNTHESIS_C_crossings.md`.

| | party | its seats today or by a family proposal | what only it holds |
|---|---|---|---|
| **C** | the crown | `off_king`, `off_heir`, the Inner Circle, the Lord Treasurer | the realm rung's purview; the `homage` instruments' grantor side; dignities to give |
| **N** | nobility by deed and the conquest-founded ducal houses | `off_duchess_hafenmark`, `off_duke_varfell`, the Jarls, dignity-holders, wardens of a `march` | deeds; ground; men sworn to them |
| **Ch** | the Church | the Confessor, four Cardinals, the Inquisitor, the Representative; sees; exempt houses | benches whose reach follows the person (CR-60); the archive; believers' answers |
| **B** | the bureaux and the court | Ministries, Court Parliament, Imperial Court dignities; Altonia's court, Doux, Katepano, Kommerkiarios | the hands paper passes; the Settlement's custody; the gate |
| **M** | merchant republics and houses | Schoenland's seats; Hafenmark's commune council; house heads on a hearth | stocked chests; bonds; rolls kept by warrant |
| **G** | guilds and orders | the guild roll, comptroller and leader; the Löwenritter; the Templars' houses | a roll that gates other bodies' seats; an armed body sworn to a seat |
| **K** | chartered companies and the peoples under them | farmers, factors, wardens, rectors; cohorts and hearths; the southern Einhir | the ground itself: stores, hands, testimony, and the choice to stay |

### 5.1 Pair by pair

"Gives" is a named primitive or verb one side supplies that the other cannot supply for itself.
"Sanction" and "favour" are what crosses when the relation is used as a weapon or a gift. Every sanction
is a drawn act whose effect on third parties is their own drawn answer.

| pair | first gives second | second gives first | sanctions that cross | favours that cross |
|---|---|---|---|---|
| **C · N** | re-issue of `homage` at each succession; forbearance on ducal ground (`forbears`: `requisition`, `revoke`, `seize`); dignities (`confer` citing a deed) and their `upkeep` | an untermed `oblige` to `off_king` (so the realm's purview reaches the duchy, and `obligation` sits in every royal ask); a relief (`due`) at each succession; their `legitimacy` readings in the `reception` of every `succeed` | crown: a levy inside the duchy (a breach each ducal ledger can hold), `quo_warranto` on the homage, a dignity unpaid. Noble: `release` of the oath (the duchy leaves the purview), the relief withheld, `march` | a new deed recited in a grant (`land_grant`, `march`); a dignity; confirmation without a fee |
| **C · Ch** | the `immunity` (the containment charter) and its confirmation; leave for sees and tithe on crown ground; CR-37's concurrence partner | consecration (a certificate for the seat, `evidence` at `succeed` and at any deposition); commemoration (`tell`); alms, tending, teaching and judging in crown settlements | Church: a `ban` on a crown seat-holder and its `avoidance` writ to his sworn men; an `interdict` on a rung; consecration refused, or given to a rival. Crown: a levy or seizure in Himmelenger (breach of the immunity); its own man pressed into a see; `quo_warranto` against a grant two centuries old | absolution (`pardon` after a served penance); a see for a royal clerk |
| **C · B** | seats and their `upkeep`; `confer` and `revoke` | the hands every royal writ passes (`carry`); collection (`requisition` through the treasury seat); custody of the Settlement; the route by which a new deed is enrolled | bureau: a writ held over or returned; a petition never entered. Crown: recall; a purge, after which every writ lapses at the hand | a gift (`give`) that moves a clerk's regard; a dignity for a clerk |
| **C · M** | a `charter` (a commune's self-rule), a `staple`, a bench for `debt_suit` | a `debt` (the loan against the throne; the forced loan is the same paper with the treasury as debtor); `staple` rents; what their factors have surveyed | house: the next loan refused on the `evidence` of the last; the bond handed (`give`) to the throne's rival; the lapse told. Crown: default; a successor who does not commit; a market's `standard` raised; `quo_warranto` | an extension (a new stage on the bond); a charter confirmed |
| **C · G** | a `charter` for the body; exemption by `immunity` | the Löwenritter's oath to the **seat**, not the man; a guild roll that gates commune office | order: `release` (canon's "deed-logic enforcement mechanism", `:145`). Crown: `quo_warranto`; the Church's own procedure borrowed against an order it owes money (§5.2 e) | a fee remitted at succession |
| **C · K** | `farm`, `march`, `land_grant`, `staple`, each conferring a seat with `audit_at_exit`; inspectors (`dispatch`) | an advance and a rent (`due`); a kept garrison; a founded settlement; from the people: yield, testimony, petitions | crown: recall (drawn at `remove`), the `audit`, a calling-in. Grantee: rent withheld, the recall not obeyed, local oaths taken. People: `requisition.resisted`, `petition`, `migrate`, an oath to somebody else | renewal; a quittance; a deed recited |
| **N · Ch** | a see's ground and its stores; the right to invest where `patronage` admits it | consecration of a ducal claimant; a bench and alms on ducal ground; tithe collected through the see | Church: **excommunication against a duke** (§5.2 a). Duke: his own bishop invested; a see-holder kept loyal against an interdict; the tithe withheld | a benefice for a son (composed, and findable) |
| **N · B** | (nothing owed) | the clerk's hand on any petition to enrol a deed; custody of the two ducal certificates | bureau: the petition returned; the paper withheld from a hearing. Noble: `purge_altonia` acted on; the minister struck | a deed entered quickly |
| **N · M** | a `charter` for a town; protection (the `protected` variant of `tribute`) | a `debt` for a campaign; hired captains (an `oblige` kept by `upkeep`, the advance a `debt`) | house: suit and the debt-bar inside its commune; both sides funded (ARC-15). Noble: default; a town's charter called in at his succession | arrears forgiven (the bond handed back) |
| **N · G** | ground for a house | an order's arms; a roll that decides who sits for a commune on the duke's council | order: a house sworn to a Cardinal and not to the lord on whose ground it stands. Noble: the house's stores levied | — |
| **N · K** | a `land_grant` or a `march` in his gift | a new house: a warden's won field, then a certificate for his seat, is how nobility by deed is made again | people: oaths to the warden outnumber oaths to his grantor; revolt. Lord: the levy | — |
| **Ch · B** | schooling (`train`) and its own archive | (Altonia's) the original containment grant; (the Crown's) entry of Church petitions | two keepers: a deed certified in one house and contested in the other (§5.2 d). A Church bench trying a clerk for a forged entry | — |
| **Ch · M** | benefices; lawful instruments (a debt in another kind at another place leaves no usury to find) | credit; carriage of the tithe as a bond payable at Himmelenger instead of a convoy | Church: usury tried as a derived fact; an `avoidance` naming a commune's members, which bites on their goods and bonds abroad. House: the next advance refused | a prelate's debt extended |
| **Ch · G** | the head seat's purview through every house sworn to it | houses on other lords' ground; arms (`dispatch` on the Templars' Cardinal's row) | head: discipline (if ruled, §10). Arm: acts through a Cardinal's seat against the Confessor's held writ; `release`, house by house | — |
| **Ch · K** | alms to hearths in shortfall; a bench that hears a hearth's complaint | believers' answers to every writ; the tithe's yield | `interdict` (what stops is what the engine can see: alms, judging); a parish that defies it | a mission's ground (`land_grant`) |
| **B · M** | a `staple` at the gate (the Kommerkiarios issues, renews or withholds it); a hand on every exception | duties; dispatches and `survey` Records the other side wants to read | bureau: the market's `standard` raised. Merchants: withdrawal together | a gift |
| **B · G** | entry of a body's charter | — | a charter left unentered | — |
| **B · K** | the far superior's orders, late; the inspector; the bench of an `audit` | reports that arrive in a person | recall that does not arrive; a governor who construes | — |
| **M · G** | a roll by warrant; council seats by lot from it | members' oaths; the gate to office | the keeper lets a member's term lapse (the quiet purge); the league's order to withdraw, and a breaker put out | enrolment |
| **M · K** | capital: the advance on a `farm` is a `debt`; a share is a `debt` | the factor at distance under a `commission`, audited at exit | settlers against the centre's levy; a factor trading on his own account | — |
| **G · K** | apprenticeship: the one route from a hearth to a roll | labour at a site | — | — |

### 5.2 The crossings the work order names, as chains of drawn acts

Each step is one existing verb by one person; each has four bands; none is a rule about a duke, a throne
or a charter.

**(a) Excommunication against a duke.**
1. A churchman who holds a deed claim the Church's goals act against `open_case`s; the matter is carried
   to a bench with realm `scope` (`carry`, drawn).
2. `determine` under `excommunication_deliberation`: each member's ballot is drawn; at two thirds of the
   ballots cast the sentence passes, and its band disposes: Overwhelming or Success a `ban`
   (`ban.opened`); Partial an `oblige` of the duke to the bench (monition); Failure an acquittal, which
   is itself news and costs the bench with those bonded to him.
3. A Church seat with `issue` publishes: a `dispensation` of form `avoidance` naming him. The writ's
   `force` is drawn, with `remove` to each see.
4. **Each addressee answers by his own draw.** For a man sworn to the duke the terms are hostile to
   compliance: his `obligation` toward the duke, his `regard` for him, `stakes`. A complier holds an
   obedience (`oblige` carrying `OBEYED_WRIT`) and his `forborne` set declines the named dealings.
5. **What the sanction does to the duke's power is one line in one reader**: while a live `ban` stands on
   him from a seat of the faction whose writ a man has complied with, that man's `obligation` toward him
   reads zero (`[VEN A]`'s lift). His asks, musters and writs to that man lose the term. CR-88's duty
   decline no longer bars that man's own `release`; whether he takes it is his own score, and those who
   already held a grievance take it more often (`[PAP D]`'s gate).
6. The duke's answers: submit (swear a termed `oblige` to the sentencing seat; at its maturity `pardon`
   reads `penance_weight`); appeal; defy and hold his men by their regard; invest his own bishop in the
   see on his ground; strike at the bench.

**(b) A loan against a throne.**
1. The holder of a crown seat `petition`s a house head (the ask: the lender's `regard`, the `evidence` of
   debts met or lapsed, `stakes` by the amount).
2. `covenant` mints a `debt`: the borrower commits through his seat; the house holds the bond.
3. The advance is a `transfer` (drawn carriage). `dues` puts each stage on the debtor's question.
4. At a stage's maturity the house, or a factor sworn to it, presents the bond: the reckoning, with the
   debtor's `obligation` (his live `commit`) in the creditor's favour. Paid, paid, part paid and extended,
   or refused.
5. `debt.lapsed`. **The benches that sit over a throne's holder are two kinds only**: his own judges,
   whom he seats and may recall, and (once CR-60 gives three Church benches a realm `scope`) the
   Church's. A `debt_suit` before the first is drawn against his own appointees' disposition; before the
   second it can end in a `ban` on a king. So a king's creditor has one court worth going to, and it is
   the Church's, which is how a banker's bond becomes an excommunication. Short of a suit the house has
   what Florentine bankers had: it can refuse the next loan; tell; and `give` the bond to someone who can
   use it (a duke, the Church, Altonia), who then holds a king's paper. A successor is not bound until he
   commits, so every accession is a default the house can see coming, and its members' readings are part
   of that accession's `reception` where they sit in the audiences.
6. The crown's side of the same instrument is the forced loan: the treasury seat issues the realm's
   paper to a lender whose answer is `comply` or not.

**(c) A charter against a rival.**
1. A grantor issues a `staple` to one body for a kind at a place where another body holds an older one.
   The first grant's `forbears` clause (the grantor: no second `staple` there) is now breached, and the
   older holder's `kept` reads below zero as soon as he hears of it.
2. His `breaches` occasion offers him the grantor and the newcomer's factor: `petition`; a suit;
   `exchange` at worse odds than he had; withdrawal with his league.
3. Or the grantor clears the ground first by `quo_warranto` against the older grant. The holder cites
   his instrument, and because the form `hardens` its age held adds weight (`prescription_seasons`), up
   to the cap. The bench's draw decides; every other holder of a like grant hears of it at the row's
   `disposal_reach` and judges the mover by it.
4. Two grantors over one ground (a ducal `land_grant` inside a Church `immunity`; a crown `farm` over a
   ducal liberty) are the same conflict with nobody above both: each holder cites his paper as `evidence`
   in every levy and seizure on that ground until a hearing or a field settles it.

**(d) A deed certified by one body and contested by another.**
1. A claimant petitions the Church for consecration to a seat; the bench's `reception` is hostile;
   Failure, known because the floor is open.
2. She petitions the Court Parliament instead. The petition passes the chancery's hand (`carry`: entered,
   held over or returned); the body determines; a `resolution` recites her deeds for the seat, kept by the
   clerk.
3. When the seat falls vacant two certificates stand for two claimants, kept in two houses. Each is
   `evidence` at the `succeed` draw only if its keeper cites it, gives it or testifies. The audiences'
   readings are their own ledgers'. A provisional hold on Partial is a reign that must be earned twice.
4. The same shape holds between the Crown's Settlement, which recites one deed for Varfell, and what the
   Skald-Chief tells in the south.

**(e) An order suppressed with the Church's hands.** A crown seat owes a `debt` to an order's house. The
order is exempt from the local bishop and answers to the head seat alone. The crown's road is therefore a
Church bench: a denunciation, `inquisition_hearing`, a `ban` on the order's officers, and the bond is
paper nobody can present. Exemption protects an order from bishops and not from the power that protects
it (`[PAP]` §3.8). No rule; every step is a person's.

### 5.3 What every institution needs from another, in one sentence each

- The **crown** needs the nobles' oaths for reach, the Church's certificate and the clerks' paper for its
  heir, the houses' credit for its bill, and somebody on the spot for every far levy.
- The **nobles** need the court for a deed to be told and paid, the chancery or the Church for it to
  outlast them, and the crown's forbearance on their ground.
- The **Church** needs the crown's immunity and the lords' ground for its sees, and every believer's
  answer for any sanction to mean anything.
- The **bureaux** need a holder who will not purge them and have nothing but the hand and the chest of
  papers.
- The **houses** need a bench that will hear a suit and a debtor who can be sued, which a throne is only
  before the Church.
- The **guilds and orders** need a charter from someone who can call it in.
- The **people** need a room where what was done to them counts, and have the levy's odds, their
  testimony and their feet.

---

## 6. Structural conflicts that generate story by themselves

Each is a pattern an observer reads off the log. "Arises when" states conditions on persons' states and
on what the draws have already produced; nothing fires. "Reading" is a fold over the Event log that the
one report prints (proposal D); "fails to show" is what would prove the conflict did not occur. Every
reading is of the kind `harness/strife.py` is: read-only, no assertion that a story occurs, no guard.

| conflict | the two things that cannot both be kept | arises when | the draws in it | reading | how it fails to show | built by |
|---|---|---|---|---|---|---|
| **investiture** | a lord's ground and the Church's office on it | a seat whose `patronage` lists both `purview` and `own_faction` is vacant, and lord and head each know a man | two `confer` draws, each with the other's incumbent as `opposition` | `tenure.opened` on one seat with alternating `Act.via` factions | no see ever empties; one side never forms the act | `[PAP B]`, `[PAP E]` |
| **succession by deed against blood** | a title-holder's presumption and a rival's fresh deeds | a founding seat falls vacant with an heir whose own deeds are few and a rival whose deeds are in many ledgers; sharper where a keeper has stopped telling the founder's | `succeed` (the BINDING lane's), its `reception` reading `legitimacy`; `determine` under `consecration` | `succeed` attempts by band and by whether the claimant held the title; provisional holds confirmed or lapsed; per audience, the mean `legitimacy` gap between the two | no seat empties (today: `succeed` formed 0, `[BYZ]` §8); every claim is by the title-holder | `[BYZ E]`; proposal B |
| **debt against sovereignty** | a creditor's bond and a debtor nobody can sue | a seat-holder at the realm or a duchy rung holds a `commit` to a `debt` that matures while his rung's stores are short, or he dies | the reckoning; the successor's `commit`, his choice; the next loan's ask | `debt.lapsed` whose debtor held a realm or duchy seat; then the bond's `record.given` chain; the successor's `commit` or its absence | no bond is ever minted (the chooser does not lend: M-AIM's finding, not this kit's) | `[VEN A]`, `[VEN B]` |
| **charter against charter** | two papers over one ground or one trade | a second grant is made where a first forbears it; or a grantor's successor wants a revenue an old grant took | `quo_warranto`'s `determine`; every levy and `exchange` on the ground, each citing a paper | cases under `quo_warranto` whose holder cites an instrument with age weight of one or more, and their bands; two live `staple`s of one kind at one place; other holders' regard for the mover afterwards | no succession at a grantor's seat; every successor confirms for the fee | `[COL A]`, `[COL C]` |
| **schism** | one creed and two heads | a `conclave` stays undetermined for seasons, or carries by a margin the losers will not accept, and the dissenters hold seats that grant `establish` | each ballot; `establish`; each person's `commit` | two live seats of the head's post under different faction Propositions | design-first: no verb mints a faction Proposition in play (FA's emergent-faction carrier) | `[PAP B]`, `[PAP E]` §6 |
| **tax revolt** | a fixed demand and a short store | a rent, a stipend bill or a tithe falls due on a seat whose ground had a lean season; the collector asks a larger share; the cohort's `regard` falls; the next levy's odds fall | `requisition` (the MATERIAL lane's), with `stakes` by share, `regard`, `remove` | `requisition.resisted` followed within two seasons by a `march.declared` or a `petition.filed` naming the collector, in the same territory | the collector remits; stores never run short (today every treasury rung is empty and hunger occurs in season 0 only) | `[BYZ B]`, `[COL B]`, `[COL E]`; SE's stores |
| **bureaucratic capture** | who holds the seat and who holds the hand, or the roll | most hands of a body resolve to one person; or one person with no seat on a bench holds live edges of more than half its members | `carry`; every ballot, with `obligation` | per body: the share of entries made by its busiest seat-holder and the writs returned in a season he is absent; per bench: the largest share of members with a live edge to one person, against the `obligation_step: 0` control | every writ is entered; no share ever passes the control world's | `[BYZ C]`; `[VEN A]`, `[VEN C]` |
| **colonial revolt** | a grant's terms and the grantee's own following | a grantee at `remove` from his grantor collects well and pays his men; or the governed hold breaches and a rival offers | `issue` at `remove` (a recall that does not arrive); `requisition`; `oblige` and `release`; the field | `oblige` edges to a conferred seat from residents of its ground against those to the grantor's; a `tenure.closed` by `release` followed by `duty.taken` to another faction's seat; `compliance.withheld` on a writ naming the holder's own seat | no grant is ever made; every recall lands and is obeyed | `[COL A]` to `[COL E]` |

Four more the interlocks produce that no single family named:

| conflict | arises when | reading | fails to show |
|---|---|---|---|
| **the keeper's silence** | a keeper's regard for a house is low, or his goals run against it, and he stops telling what its paper recites | per season, the mean chain term of `legitimacy` for each founding seat, beside the count of tellings of recited deeds by each keeper | the chain term does not fall faster when tellings stop (proposal B gate 4) |
| **the unpaid court buys a creditor** | the stipend bill exceeds the fisc and the holder borrows to meet it | `transfer.made` renewing a sworn term within a season of a `debt` minted through the same seat; then that bond's fate | the bill is always met by levy, or never met |
| **the sanction that needed an army** | a `ban` and its `avoidance` are published against a lord whose men hold no grievance | compliance and release shares among his sworn men, split by prior grievance; it must depend on it | release does not depend on prior grievance (the sanction would be a switch) |
| **the paper that changed hands** | a certificate, a bond or a charter is seized, given or forged and then cited by its new holder | `record.seized`, `record.given` or `record.forged` on an instrument, then a hearing whose `evidence` term cites it | no hearing ever cites a held Record (SC's evidence interface not landed) |

**Why these arise without a script.** `20_NARRATIVE_CHURN.md` §7.1 finds that every stage of a plot point
is built except the first, a pull: two things a person stands on that cannot both be kept. An instrument
is a stored pull. A `homage` and a stipend bill, an `immunity` and a short fisc, a bond and an empty
rung, a certificate and a rival's deeds: each sits in a person's ledger as two claims that disagree about
what he should do, and the kit's three occasions (`dues`, `breaches`, `audits_due`) are how the pull
reaches his question. What he does is sampled and then drawn.

---

## 7. The commensuration test

Jordan: *"all need to be adapted made commensurate expressed within play."* Five tests; each is stated
with what was found against it and what the kit does about it.

### 7.1 One roll form

Every institutional procedure resolves through `seam.contest` or the graded route into
`social_contest.roll`, and through no other roller.

| route | the verbs on it | owner |
|---|---|---|
| prize `a proposition` | `determine` (bench), `argue`, `covenant` | SC; `13_SC` |
| prize `a standing` | `arrest`, `interview` | SC; `13_SC`; FA-P6 |
| prize `a seat` | `confer`, `revoke`, `succeed`, `establish` | `14_VERBS_BINDING_A`, `_C` |
| prize `an order` | `issue`, `dispatch`, `comply`, `evade / defy` | `14_VERBS_BINDING_D`; `14_VERBS_SOCIAL1_B` |
| the graded route (no prize) | `carry`, `open_case`, `requisition`, `transfer`, `exchange`, `seize`, the inquiries | `13_SC`; `14_VERBS_MATERIAL_B`, `_D`; DETERMINISM-A |
| a ballot | one draw per member, inside `determine` under a `declared` row | `13_SC` |
| the lot | `draw(off.id, "lot")`, the one draw owner (`state/ids.py`); not a roll: a draw among the eligible | `[VEN C]` |

Found against it: none of the four families added a roller. Two wrote private obstacle compositions
(X-19, X-20) and one a second ballot (X-15); all three are folded into the one composer.

### 7.2 One ladder

Overwhelming, Success, Partial, Failure, by `degree_from_net`. The four families' Partial bands are five
shapes, and that is one too many only once:

| Partial means | for | owner of the shape |
|---|---|---|
| provisional: a termed hold | `confer`, `succeed` | VB-C (`provisional_term`) |
| less than whole: half the remit, half the recited deeds, half the term | `establish`, `consecration`, `comply` | VB-A; `[PAP C]`; SOCIAL1-B |
| a smaller amount | `requisition` (the magnitude ladder), `transfer` (the delivery ladder) | MATERIAL-B: one function, two tables, which that file asks S to tolerate and this kit accepts |
| delayed one term | `carry`, a ballot short of its pass mark, a `revoke` that closes at the season's end | `13_SC`; X-15; `[BYZ E]` |
| a lesser disposal | every band-mapped `disposes:` | SC-P4 |

Failure is recoverable everywhere: nothing is written but the Event of the attempt, and the act may be
tried again. `[VEN C]`'s bar on a failed motion was the one exception and is withdrawn (X-15).

### 7.3 One set of scales

The eight `rung_kinds`. An institution's scale is its seat's rung and nothing else:

| the brief's scale | rung kinds | institutional things at it |
|---|---|---|
| person | person | a deed, an oath, a debt, an answer to a writ |
| settlement | hearth, community, settlement | a house and its branch; a guild chapter; a commune council; a farmed toll; a parish |
| faction | territory, province, duchy | a see; a march; a duchy under `homage` |
| realm | realm, and a foreign root | the throne; the Church's realm-scope benches; the Altonian court at `border_hops` |

Found against it: no seat sits on a `hearth` today and the anchor resolver has no form for one (`[VEN]`
E-1); the kit adds the `{venue:}` form. There is no `province` rung in the built realm and the kit needs
none.

### 7.4 One cadence

The season. Two clocks only, both matured at MATTER: `Tenure.term` and `Record.stages`. Every duration in
the kit is a whole number of seasons on one of the two.

| duration | unit | on which clock |
|---|---|---|
| the pay year (`oblige_term`), a rotating seat's `term`, `cooling_off` | seasons (4 shipped or proposed) | `Tenure.term` |
| `provisional_term` | seasons (2) | `Tenure.term` |
| a hand's patience (`hand_term`, `office_bodies.term`) | seasons (1 to 2) | `Record.stages` |
| an instrument's `term`, a clause's `every`, a `debt`'s stages | seasons | `Record.stages` |
| `prescription_seasons` | seasons (8) | read off `Tenure.since` of the holder's `hold` on the Record |

Found against it, and not this kit's to repair: **the engine has no year.** `season_of_year` is `None` at
shipped fixtures (`20_NARRATIVE_CHURN.md` W1). "Yearly" in every family file means "every four seasons"
by the value of `oblige_term`, not by a calendar. When WR's year lands
(`09_WR_B_weather_with_memory_and_the_year.md`), the kit's fours should read that owner; until then they
are independent numbers that happen to agree. No transit clock and no message queue exist or are added
(X-14).

### 7.5 One currency model, and a unit for every number

Stores of a `matter_kinds` member at a rung, conserved by `_shift`. A `debt` and a `due` move no stores
by themselves; a payment is a `transfer`.

**X-30, found by this test.** `[BYZ B]` denominates the stipend bill in `coin` (`shortfall:coin`).
`[VEN B]` denominates every instrument by `kind` because `coin` "is produced by no site and held by"
nobody (`data/fixtures.py:613-632` `[via VEN]`). Decision: `upkeep` is owed in units of whatever matter
the paying `transfer` carries (H-158's own stated limit `[via BYZ]`), and the bill's shortfall claim names
`default_store_kind` until SE gives `coin` a producer. `[BYZ B]` edit 4 is reconciled; the `roga`
scenario's stores are seeded in that kind.

Every number the kit proposes, with unit, owner and sweep, is the table of §3.6 (fixtures) and the rows
named there (content). There is no number in the kit without those three. Family numbers that had two
values are resolved in X-07, X-21 and X-30. Numbers outside the kit that this test found in two values,
listed for unification lane U3: `regard_step` (0.04 in `05_SC_obstacle_difficulty_and_modifiers_B.md`,
1.0 in `13_SC_tuning_tables.md`); the distance step (X-27).

### 7.6 How the test is run

Not by a new guard (CLAUDE.md §0.1 pt 5). By the refusals the loaders already owe each data family, each
named in its own proposal: `roll.py::obstacle` refuses a term off the roster (SC-B edit 5); `data/verbs.py`
refuses a writing row that is neither contested, graded nor declared bookkeeping (DETERMINISM-A);
`data/instruments.py` refuses a clause kind off `DEED_KINDS`; the `offices.yaml` loader refuses an unknown
key. And by one reading in the first playable's report (proposal D): per run, the roll routes used, the
bands seen per verb, the term names seen, the matter kinds moved, and the two clocks' maturations.

---

## 8. Layer 1 conformance, and where Jordan's intent meets Layer 1

Read against `architecture/meta/04_CODE_ARCHITECTURE.md` at §0, §A.1, §A.2, §B.7 and §B.8 (opened this
session at those sections; the rest by the family lanes' citations, marked). Grades are that document's:
STRUCTURAL (the defect has no spelling), MECHANICAL (one path, and it refuses), CONVENTION (a reader
notices).

### 8.1 The statement, for the whole kit

| Layer 1 row | what the kit does | grade | where it would break |
|---|---|---|---|
| **AX-1** only a person acts; a seat enters through `Act.via` (§A.1) | no institution acts. Every procedure is one person's existing verb through a seat. A company, a house, a see and a bureau are seats; a faction stays a Query return (§B.6.1) | MECHANICAL (`Act.actor` is a person id) | a rule that names "the Church" or "the Crown" as a doer. None is written; the CH signature keys on a role template, never a name (`[PAP A]`) |
| **AX-2** the decision is compiled where `World` is not a name (§A.1) | `legitimacy`'s chain, `kept`, `forborne`, `owed_to` read the person's own ledger and Tenures. The occasions (`dues`, `audits_due`, `hands_open`) are `world_q` functions in `vacancies`' shape that stamp referents; `breaches` reads only the asker's ledger | STRUCTURAL for the `person_q` four (no `World` parameter); CONVENTION for the occasions | see 8.2, L-4 |
| **AX-4**, §A.2: a module holds no token and writes nothing; typed in, typed out; no held state (`holonic_ARCHITECTURE.md` §43, §45 to §47 `[via CLAUDE.md §3]`) | **no module is added.** The one module the kit touches is `social_contest`: its typed input gains raw operands (the two `owed_to` counts, `records_dissent`, the hop count) and its typed output gains the term names. The host sums nothing; the module stores nothing | STRUCTURAL (no token parameter exists on a module entry) | a host that composes `obligation` or `remove` itself (two composers) |
| **T-k** one resolver, one ladder (§A.1) | §7.1, §7.2: every procedure on `social_contest.roll` and `degree_from_net`; the ballot is many draws of that kind; the lot is the one draw owner | MECHANICAL (`manifest/registry.py::check_contest_prizes`; the graded route's check) | a second roller for ballots or levies |
| **AX-5**, **T-n** a matured term cites the act that wound it (§A.1, §B.8) | a hand's stage, a debt's stage, a provisional hold, a stipend term: all on the two existing clocks; `cooling_off` is computed from a closed Tenure's `until` | MECHANICAL | a MATTER pass that decides anything; none is added (`[COL A]` edit 7) |
| **AX-6**, ID-14 what an act can open an act can close (§B.8) | no Tenure kind is added; an obedience closes by its term or the owner's `release`; a `debt` is a Record, and the debtor's undertaking is his own `commit` | MECHANICAL at load | an obligee-side closer. D-5 forbids it and the kit has none: the creditor's recourse is the ask, the suit, telling and assignment |
| **§B.7** there is no `Title` type; `establishment` is a Query over `oblige`; a seat does not know its holder | a dignity is a seat row with an empty remit (the `off_heir` precedent); a roll is `establishment_of` a seat (X-04); a certificate names a seat, never "the holder" | STRUCTURAL | a `roll` Record read for membership (two homes for one fact): withdrawn by X-04 |
| **§B.7** a seat adds no verb and no modifier | no seat-row key of the kit is read by any roll. The dignity "precedence" step is withdrawn (X-19) | STRUCTURAL as the kit stands | see 8.2, L-1: two terms from other lanes |
| **§B.8** `Tenure.conferrer` is deleted; "who raised whom" is a fact about two people, carried by the opening Act or by an `oblige` | a Cardinal's creatures, a patron's clients: read off the act store (who conferred) and off `oblige` plus `regard`; no field. The key `patronage:` means the right of appointment (advowson), which is a property of the seat; it is not the patron and client relation and should not be read as one | STRUCTURAL | a `patron` pointer on a Tenure or a seat |
| no stored social quantity (`state/world.py:64-107` `[via COL]`; ED-IN-0343 to 0345) | legitimacy, presumption, `kept`, what is `owed`, suspicion, prescription, a house's standing, a body's capture: every one a fold, computed when read. The stored numbers are row content: a grade, an upkeep, a term | STRUCTURAL (no field exists) | a `prestige`, `piety`, `suspicion` or `credit` stock |
| no trigger; no threshold that acts (T-c; `strife-00` R1 `[via 20_NARRATIVE]`) | where a reading meets a number (`kept < 0`, `owed > 0`, a pass mark) the only effect is that a referent is offered or a tally is read; the person samples and the act is drawn | CONVENTION | an effect written at MATTER from a count |
| §B.13 one loader per data family, cross-validated; a declared row has a reader (ID-13) | `instruments.yaml` has one loader, checked against `DEED_KINDS`, `REMIT_ACTS` and the rosters; each of the eight seat keys and each form key has exactly one named reader (§3.1, §3.3) | MECHANICAL at load | a form row no reader reads: SC-P4's rule applies (it leaves with the batch) |
| §C.11 the explanation contract | every roll's term list is on its Event (SC-P1); every `due` and breach names its instrument and clause; the reason trail runs from the act to the occasion (`01_CORE_reason_trail_in_the_act_store.md`) | MECHANICAL once SC-P1 lands | — |
| ED-1050 / §C.12: the port validates against the oracle; data crosses as typed artifacts | the kit's facts are YAML rows code reads, never prose; nothing here is bound to a Godot resource | — | — |

**Scripting drift, checked.** No rule names a person, a seat, a faction or an outcome. Every authored row
that names one is content with a revert (`[ASSUMPTION; Jordan to correct]`). The rename test applies:
renaming every faction and seat in the seeded rows changes no behaviour.

**Shape divergence, checked.** One clause schema at every rung (a hearth's debt and a realm's tribute);
one seat row for a throne and a counting-house; one obstacle composer for a ballot, a levy and a plea.

### 8.2 Where Jordan's stated intent and Layer 1 meet — named, not resolved

| # | Jordan's intent | the Layer 1 row | where the suite stands |
|---|---|---|---|
| **L-1** | the brief: every piece of an institution states "what roll and what modifiers (personality, affiliation, **office**, evidence, publicity)" | §B.7, graded STRUCTURAL: "a seat adds no verb and no modifier … no bonus field; no modifier column" | the kit adds no office modifier. Two other lanes do: `14_VERBS_BINDING_C`'s `standing` (how far the person stands above or below the exercised seat) and `13_SC_tuning_tables.md` T4's `standing_dice` (a die for a seat on the bench), the latter on the tree's own line "Rank supplies dice and gates nothing". The kit's rows read `standing` as that lane wrote it. Whether rank may be in the odds at all is between the brief and §B.7 |
| **L-2** | institutions "expressed within play" through seats that are paid, routed and audited | §B.7's `Seat` tuple: `id, post, body?, scope?, remit(acts[], binds), conferral, revocation, upkeep, exists` | five of the eight keys are values of fields the tuple has (`upkeep`; `patronage`, `eligible_from`, `cooling_off` say how it is filled; `dignity` says its remit is empty and grades its upkeep). Three say something the tuple does not: `passes_through` and `hand_term` (whose hands its paper needs), `audit_at_exit` (what follows its close). The spec is not edited to match (CLAUDE.md §0.05); earlier changes to this tuple were Jordan's rulings (`RR-B` limb `B-1`) |
| **L-3** | "we do not do deterministic": a vote may not be a count of commitments | AX-1 and AX-2: only a person acts, and his choice is made by the one chooser where `World` is not in scope | the ballot (SC's) draws each member's vote inside one person's `determine`; the member did not choose to cast it. It is conformant if a ballot is read as a draw on the member's interior, as his score is when he is opposed; it is not if a vote must be a member's own act, in which case each ballot is a verb he forms and the tally reads those |
| **L-4** | characters who are not omniscient (the nine requirements, R-08) | AX-2; §C.11 ("a person who holds nothing about a place is owed nothing") | `dues`, `audits_due`, `hands_open` and FA-P1's `recalls` read the World to hand a person a referent, as `vacancies` does today. `[COL A]` narrows `dues` to instruments the person holds or holds a content claim of, which keeps it nearly person-side; `audits_due` is narrowed the same way here (he must hold the `tenure.closed` claim). The idiom itself is CONVENTION |
| **L-5** | the standing requirement: every subsystem "a registered module (typed input, typed outcome, no held state, reached by composition row)" | PART D rows 1 and 47 `[via FA §11 item 2]`: an institution acting is refused; ED-IN-0283: the faction scale "has no code of its own" | the kit takes FA's option (A): institutions are the loop's own verbs and data, their standalone game is a scenario on the season loop, and no `modules/governance` is built. FA lists the two options for Jordan and this lane does not re-raise it |

---

## 9. The implementation plan

One plan across the four families and the proposals they touch. Full edge list, per-batch gates and the
family-file-to-batch map: `proposals/15_INSTITUTIONS_SYNTHESIS_E_implementation_plan.md`. Cost classes:
**edit** (data or a few lines at one owner), **small build** (one reader or loader with its test file),
**design-first** (needs a decision or another lane's shape).

### 9.1 What must land first, and is nobody's in this family

Nothing institutional plays until five things other lanes own have landed. They are the same five every
family lane named.

| upstream | proposal or plan position | what the kit cannot do without it |
|---|---|---|
| the obstacle as named terms, recorded on the Event | `05_SC_obstacle_difficulty_and_modifiers_B.md`; `05_SC_contest_record_on_event.md`; `13_SC_tuning_tables.md` | `obligation`, `remove`, every term in §3.4 |
| the institutional verbs draw | `18_DETERMINISM_task_draw_for_uncontested_verbs.md`; `14_VERBS_BINDING_A`, `_C`, `_D`; `13_SC_draw_for_unrolled_contests.md`; `14_VERBS_MATERIAL_B`, `_D`; `14_VERBS_SOCIAL1_B` | every band in every family file |
| a writ reaches its addressee and is answered | `06_FA_decree_binds.md`; `14_VERBS_BINDING_D` | hands, sanctions, tithe, recall |
| seats grant by row, end on a term, and can be played | `06_FA_remit_grant_by_row.md`; `06_FA_seat_terms_and_turnover.md`; `06_FA_seat_terms_by_body_B.md`; `06_FA_playable_scenario.md`; `06_FA_shortest_loop_B.md`; `06_FA_office_capabilities.md` | rotation, cooling-off, the runner every scenario uses |
| stores exist where seats sit | `07_SE_treasury_granary_B.md`; `07_SE_ground_and_granaries.md` | the fisc, the debt, the levy, the farm |

And from the plan: CR-29 (reach), CR-35 and CR-36 (elected seats; the `resolution` Record and its
disposal site), CR-60 and CR-61 (bench scope; the docketed row and case file), CR-88 (the duty decline),
CR-74 (the CH signature).

### 9.2 The batches

| batch | what lands | family proposals | this lane's | needs | hash | cost |
|---|---|---|---|---|---|---|
| **I-1 the owners** | `instruments.yaml` and its loader and readers, empty; record kinds and content keys; the eight seat keys and their loader; roster members; fixtures at control; the `{venue:}` anchor | COL-A; the key and roster halves of BYZ-A, -B, -C, PAP-B, VEN-B, -C, -D | A | `covenant` and `issue` formation (`14_VERBS_SOCIAL2_A`, `14_VERBS_BINDING_D` D1) for the `form` choice only | EQUAL | small build |
| **I-2 ties and distance in the odds** | `obligation`; `remove`; (`standing` beside them) | VEN-A; COL-B §1 | — | SC-B, SC-P1; `14_VERBS_BINDING_C` C1 | EQUAL at ship; each fixture flip a mover | small build |
| **I-3 the deed ledger** | the chain in `legitimacy`; prehistory; four seeded Records; `recites`; dignity rows and the dignity conjuncts on `confer`; Hafenmark's heir title; the `annex` basis | BYZ-A (edits 3, 4, 7); COL-D (edits 4, 5); PAP-C (as reconciled) | B | I-1; CR-36's kind row; `12_ARCS_case_on_the_realm.md`; `14_VERBS_BINDING_C`; `06_FA_remit_grant_by_row.md`; `06_FA_office_capabilities.md` | mover (build) | small build |
| **I-4 the purse** | `upkeep`, `upkeep_owed`, the bill; `debt`, the reckoning, `debt_suit`; `homage`, `farm`, `tribute` read by `dues`, `kept`, `breaches` | BYZ-B; VEN-B; COL-A's rows in use | A (X-09, X-30) | I-1 to I-3; `14_VERBS_MATERIAL_B`; `07_SE_treasury_granary_B.md`; `13_SC` (the `covenant` draw); `14_VERBS_SOCIAL1_B` §3; SC-P4, SC-P6 | movers | small build ×3 |
| **I-5 paper and distance** | hands and `carry`; `issue`'s terms and band-gated deposit; the Altonian court, the Doux, the gate's keeper; `altonian_civics` cells; reach rows | BYZ-C; BYZ-D; COL-B §2 to §5 | A (X-13, X-14, X-24, X-25) | I-2; `06_FA_decree_binds.md`; `14_VERBS_BINDING_D`; `13_SC` (`carry`); CR-29; CP-T09-03, CP-T09-08 | movers; foreign arm only for the court | small build + content |
| **I-6 turnover** | rolls by warrant, `eligible_from`, the lot, `cooling_off`; the Church on its ground; `patronage`; `conclave` and `quorum_share`; the one tally; `succeed`'s audiences; `acclamation` | VEN-C; PAP-A; PAP-B; BYZ-E | A (X-15) | I-1, I-3; `06_FA_seat_terms_and_turnover.md`, `_by_body_B`; `14_VERBS_BINDING_C`; CR-35, CR-36, CR-60; the `13_SC` ballot | EQUAL for the keys; the tally a mover | small build; the tally design-first with SC (it changes CR-34's shipped conjunct) |
| **I-7 sanction, audit and the calling-in** | `ban.opened`; `avoidance`, `interdict`; `forborne`; the ban's lift of `obligation`; penance; `consecration`; `audit`, `quo_warranto`, prescription; `audits_due` | PAP-D; PAP-C §2; COL-C | C | I-1, I-2, I-6; `14_VERBS_SOCIAL1_B` (`comply`); `06_FA_decree_binds.md`; SC-P4, SC-P6; `05_SC_evidence_and_rebuttal_B.md`; `05_SC_playable_hearing_B.md`; CR-60, CR-61, CR-88, CR-74 | EQUAL until docketed or issued | small build |
| **I-8 content** | houses, a commune council, Schoenland's seats and benches; sees, the tithe, an exempt house, a legate; the remaining forms in use; the seeded trade treaty | VEN-D; PAP-E 1 to 4; COL-A's other rows | — | I-1 to I-7 as each row needs; `06_FA_remit_grant_by_row.md`; WR's place for Schoenland; `14_VERBS_MATERIAL_B` (`exchange`); Jordan's names | movers per row | edit + small build |
| **I-9 the playables** | each family's standalone on FA's runner; the integrated first playable in three cuts; the one report | BYZ-F; PAP-F; VEN-D §5; COL-E | D | cut 1: I-4. Cut 2: I-5, I-7. Cut 3: I-7 | none (harness and a case) | small build |
| **I-10 held** | schism; the council; the head's discipline; a `corvee` form; the kin-bar; BYZ's batch G | PAP-B item 4; PAP-E 5, 6; VEN (the kin-bar); BYZ §12 G | — | Jordan (§10); FA's emergent-faction carrier; `02_CHAR_relations_have_a_ground.md`; readings from I-4 to I-7 | — | design-first |

Order: I-1, then I-2 and I-3 in either order, then I-4; I-5 and I-6 beside each other after I-4; I-7
after I-6; I-8 as its rows' needs land; I-9 cut by cut. A batch closes with the test files covering it
and the suite once (CLAUDE.md §0.4); every gate on a draw reports band frequencies over seeds with a
control, never a single run (§0.1 pt 4).

### 9.3 The first playable: "The Treasurer's Year"

One scenario that cannot be played without crossing institutions. Exact edits and gates:
`proposals/15_INSTITUTIONS_SYNTHESIS_D_first_playable.md`.

**Situation.** The realm as built, eight seasons. The player-proxy holds the Lord Treasurer's seat
(NPC-037's: the one seat the Byzantine, Venetian and colonial lanes each gave a part to). At tick 0, by
the game's own acts under the pinned roll: dignity-holders sworn to the crown whose terms fall due within
the year; a fisc that holds less than the bill; two duchies with stores, each under a seeded `homage`
whose `forbears` clause the Treasurer can breach; a house with a stocked chest; the tolls of Stillhelm
unlet; Himmelenger's stores inside a seeded `immunity`.

**The choice, each season.** How to meet the bill:
- **tax a duchy** (`requisition` at `remove`, against the cohort's `regard`): a breach of the `homage`
  the duke's ledger can hold, and his answer is his own;
- **borrow** (`petition` to the house head, then `covenant`): a `debt` against the treasury, a reckoning
  at each stage, a lapse if the rung is short;
- **farm the southern tolls** (`covenant`, form `farm`): an advance now, a rent later, a farmer over an
  uneasy people, and an `audit` when his hold closes;
- **levy in Himmelenger**: a breach of the `immunity`, which the Church's goals act against; a sentence
  and its `avoidance` writ are then drawn against the Treasurer himself;
- **leave men unpaid**: their terms mature and the crown's purview no longer reaches them.

**What is shown.** The bill, the fisc and who is owed; each instrument he is party to and `kept` as he
reads it; each roll's term list.

**Endings.** The court kept or lapsed; the bond met, extended or lapsed; the audit's band; the Treasurer
recalled, banned or still seated at eight seasons. Each is a Query over Tenures and the log.

**Seats to play.** The Treasurer; a Duchess under a breached homage; the house head (lend, refuse, hand
the bond on); a Stillhelm hearth head; in the third cut a Church bench member.

**Three cuts.** Cut 1 (after I-4): tax, borrow, or leave unpaid. Cut 2 (after I-5 and I-7): the farm and
its audit, and writs that pass the Ministries' hand. Cut 3 (after I-7): the immunity, the sentence and the
answers.

**What it merges.** `[BYZ F]`'s `roga` (the bill, the fisc, whom to pay) on the realm instead of the
spine; `[VEN D]`'s first cut of The Counting-House (one loan, one harvest, one reckoning), from the
borrower's seat and playable from the lender's; `[COL E]`'s Farm of the Southern Tolls as its second
cut; `[PAP]`'s third scenario (The Sentence) as its third. `[PAP F]`'s Vacant Chair and `[BYZ F]`'s
`chancery` remain their families' standalone games and are not merged: each family keeps one scenario
that exercises it alone (the standing requirement), and this one exercises them together.

**One code path.** `harness/governance_spine.py::play(..., world="realm")` (FA-B4), `play_surface.py`,
the season loop. The scenario adds seeded rows, tick-0 acts and a reader.

**Gate.** Seeds 0 to 9, eight seasons, the shipped chooser in every seat: at least three of the five ways
of meeting the bill are attempted across the seeds; at least two different endings occur; in at least one
seed-season an act by a person who is not the Treasurer is occasioned by an Event of his (a duke's
`petition` or `release`, a house's `give` of the bond, a hearth's `migrate`). Control: the same seeds
with `seeded:` empty and the fixtures at control. Planted failure: every roll pinned to Success; the
seeds must then agree on the ending, or the variety was not the draws'.

---

## 10. Survivors for Jordan

Four. Each was put through the five steps; none is superseded, irrelevant, answered by a design document,
by precedent, or by what the architecture needs.

**1. The south's part in the Secession War.** (`canon/03_canonical_timeline.md:76`, `:96`: ratified
text. All four family lanes named it: `[BYZ]` §14 item 2, `[PAP]` §13 item 4, `[VEN]` §4.4 item 1, `[COL]`
§11 item 1.) Jordan's statement makes the first Duke of Varfell the third-ranked victor; canon calls the
south peripheral and excluded from the coalition's leadership.
- *(A) Fought, ranked third, relegated despite it.* Canon is reworded as §4.6 A1 to A3. The founding is
  one story the whole realm holds; the caste is the grievance of a house whose deed was certified last
  and whose men were kept out of the settlement's councils. Vaynard is a claimant inside the order, on
  the same ledger as Baralta.
- *(B) Acknowledged late and grudgingly.* Canon stands with one sentence added. Varfell's founding deed
  is held at full in the south and thinly in the north (the seeding tells it only under Varfell's ground
  and in the chancery). The caste is a gradient in legitimacy itself, and Vaynard is a revolutionary
  against the order.
The kit is written for (A) and needs one seeding change for (B). They are different games for every
southern character.

**2. May the head of the Church strip a Church officer?** (The seven seats are ruled `revocation: null`,
2026-10-11; FA §11 item 3; `[PAP]` §13 item 1.)
- *(A) Keep `null`.* Cardinals leave by death, resignation or a ban that bars new seats without
  unseating. The Church is a set of barons for life; an over-mighty arm can only be outlived.
- *(B) `head_of_faction`.* The Confessor disciplines by a `revoke` the officer can resist. The Church has
  internal politics and purges; NPC-038's removal on exposure becomes possible. `[PAP B]` item 4 carries
  it, shipped off.

**3. Can anyone judge the Confessor?** (`[PAP]` §13 item 2.)
- *(A) Nobody.* He leaves by death or resignation; a bad Confessor is answered by a rival seat or by
  violence. The Church is the one institution with no check.
- *(B) A council, with the throne's concurrence.* The mirror of CR-37 (the throne stripped by a motion
  and the Holy See's concurrence). Crown and Church are each the other's check.

**4. Forced labour keyed on caste.** (`[COL]` §11 item 3.)
- *(A) A form `corvee`*: a cohort's seasons of work owed to a grantee's site, issuable over southern
  ground. The caste becomes an institution with seats and an audit, and its abolition is a fight over an
  instrument.
- *(B) No instrument.* The caste stays what canon calls it, informal, acting only through `regard`.
A decision about the tone of canon.

**Closed here and not escalated**, with the step that closed each:

| the family lane's item | closed by | step |
|---|---|---|
| `[BYZ]` §14 item 1: is an order answerable at issue or at entry? | a per-row key: a seat that declares `passes_through` has hands, one that does not has none. Both games are data. FA's own §11 item 1 (proclaimed or delivered) stays FA's | 5 |
| `[BYZ]` §14 item 3: the names at the empire's centre | the shape is decided (X-13); names are content Jordan authors when he chooses, and placeholders ship marked | 4 (ARCS row 12) |
| `[BYZ]` §14 item 4: do the bureaux have a barred order? | no bar is built. A clerk has no deed, no certificate and no chain behind him, so his `legitimacy` in every audience is low and his claim to a founding seat is drawn at poor odds. The deed order bars him as the standing rule bars anything: by odds | 5 |
| `[PAP]` §13 item 3: is lay investiture lawful on ducal ground? | per-row content: sees `[purview, own_faction]`, Himmelenger's seats `[own_faction]`. The work order itself names investiture as a structural conflict to be designed | 3 |
| `[VEN]` §14.2 item 1: is a roll ever closed by blood? | no: the fixed point | 3 |
| `[VEN]` §14.2 item 2: Schoenland's constitution | a power beyond the map is persons in seats (ARCS row 12); the seats are authored as marked assumption | 4 |
| `[VEN]` §14.2 item 3: may a house be its own faction? | every house belongs to a faction now; a house that leaves its guild needs a faction Proposition minted in play, which is the same carrier schism waits on (FA's) | 5 |
| `[COL]` §11 item 2: may an office be sold? | purchase is composed (a `transfer`, then a `confer`), by the precedent of #453 row 38, and is findable for that reason. No `purchase` form is authored; a heritable, unaudited seat can be written from the existing form keys if Jordan wants one as content | 4 |

---

## 11. Evidence log and what was not read

**Run.** Nothing was run on the engine by this lane: no season, no `aperture`, no `pytest`. Every reading
of computed play in this file is quoted from the lane named beside it. Two read-only commands:
`git rev-parse --short HEAD` (`8948603`); `sed -n 525,570p engine/season/queries/person_q.py` and a
`grep -n` for the reader names of §4.2 (they exist at the lines `[BYZ]` and `[COL]` cite).

**Opened this session:** `CLAUDE.md`; `INSTITUTIONS_BRIEF.md`, `AUDIT_BRIEF.md`, `UNIFICATION_BRIEF.md`,
in full; the four family audits in full; all twenty-one family proposals in full;
`05_SC_obstacle_difficulty_and_modifiers_B.md`, `05_SC_arrangement_rows_that_bind.md`,
`13_SC_draw_for_unrolled_contests.md`, `13_SC_tuning_tables.md` (T4, T5 and the edits),
`18_DETERMINISM_task_draw_for_uncontested_verbs.md`, `14_VERBS_BINDING_A`, `_C`, `_D`,
`14_VERBS_MATERIAL_B`, `14_VERBS_SOCIAL1_B`, `06_FA_decree_binds.md`, `06_FA_levy_through_the_seat_B.md`,
`06_FA_seat_terms_by_body_B.md`, `06_FA_office_capabilities.md`, `12_ARCS_case_on_the_realm.md`, in
full; `audits/20_NARRATIVE_CHURN.md` to its §7; `canon/03_canonical_timeline.md:70-149`;
`architecture/meta/04_CODE_ARCHITECTURE.md` §0, §A.1, §A.2, §B.7, §B.8; `audits/06_FA_audit.md` §11.

READ_LOG_PLACEHOLDER

<!-- append-point -->

