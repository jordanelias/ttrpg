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
institutional verbs that execute with no draw), and (b) fifteen collisions among the lanes themselves,
every one of them a collision of **name or home**, none of method: three carriers for the founding order
of the Secession War, three record kinds for a certified deed, two things called a roll, two things
called a charter, two things called `instruments`, two functions for standing, two encodings of an audit
at exit, two shapes for a share in a company, and two competing rewrites each of `confer`, `requisition`
and `issue`. §2 decides each.

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
| X-26 | `requisition`: `[BYZ B]`, `[COL B]`, DETERMINISM-A's default, the MATERIAL verb lane | decided in §3.5 after the MATERIAL lane's text | BYZ B, COL B |

