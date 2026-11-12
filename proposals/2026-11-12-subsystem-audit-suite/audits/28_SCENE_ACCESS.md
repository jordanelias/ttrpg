# SCENE ACCESS — how a visit occupies a person, how office orders visitors, how an appointment is made, and how a petition kept waiting grows

## Status: REFERENCE (an audit and a plan for future execution; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: e1d6180 (working tree)

Serves Jordan's rulings **A-63** (*an interaction occupies its counterparty: his scene budget is debited or
he is unavailable to a second visitor that round*) and **A-64** (*"B also speaks towards the ability to have
rung of office prioritized by others when visiting, and for appointments to be made. leads to situations
where someone is trying to petition but can't get through to person meanwhile the petition content
intensifies"*), `unified/DECISIONS_ANSWERED.md`. Governed by A-9 (a scene is a short sequence), A-12 (a seat
carries a modifier), A-13 (seat facts: clerks), A-21 (decrees proclaimed), A-22 (command), A-62 (budget is a
Query). The edits are carried by three proposals:
`proposals/28_CORE_scene_access_A_occupancy_and_precedence.md`,
`proposals/28_CORE_scene_access_B_appointments.md`,
`proposals/28_CORE_scene_access_C_the_petition_that_waits.md`. No code was edited. All runs
`PYTHONHASHSEED=0`; scripts and outputs in
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/SCENE_ACCESS/`.

## 0. Verdict

**A-63 and A-64 can be built on owners the engine already has, with no new verb, no new Record kind, no
stored schedule and no clock; but the baseline the ruling was given measures something else, and at the
shipped realm occupancy has almost nothing to occupy.** The 62-of-87 figure reproduces exactly at this
tree (same content hash, `bacd687f…`), and it counts every act whose payload holds another person's id:
`create_record` 46, `utter` 28, `reconstruct` 25, `issue` 30. Those are acts *about* a person, not meetings
with him. Read by the verb row's own `counterparty:` column the figure is 32 of 50; read by the rows that
require the two to be in one place (the cell asks `with` of the counterparty: `tell`, `argue`, `lie`,
`give`, `challenge`, `accept`, `capture`) the whole realm executes **24, 42 and 31 face-to-face
interactions in two seasons at seeds 0, 1, 2, of about 1,700 acts**, because four attempts in five are
refused before any question of the other man's time arises, the largest named cause being that the two
are not in one place (`with` read False in 125, 136 and 82 refusals). A crude occupancy
arm (one scene per person per round, the visitor always yielding to the host's own business) halves the
face-to-face class (24 → 11, 42 → 21, 31 → 15) and moves the realm's executed acts by 0.5% to 3.9%; the
minimal arm (one visitor per person per round) turns away 2, 7 and 4 visitors. **The single largest
obstacle is therefore not throughput lost but traffic absent**: the story Jordan names (a petitioner who
cannot get through while his petition grows) needs visits that form on believed co-location
(`14_VERBS_SOCIAL1_A_formation.md`) and petitions that reach a holder
(`14_VERBS_SOCIAL2_B_a_word_with_content.md` §3) before occupancy, precedence and appointments have
enough cases to be seen. The plan is decided and ordered on that dependency.

**What is decided (the detail is §2 to §7 and the three proposals).**

1. **Occupancy** is one rule at two grains. Per round: a person is in one scene, his own or one he is
   received in (a fold-local read of the scenes already folded this round; nothing stored). Per season:
   the scene he is received in is a scene action of his, so the budget Query subtracts scenes received
   beside scenes opened (#353's Query, A-62: no field, no receipt, no `changes[]`).
2. **Precedence** is a draw over the rival claims on one person's round (his own scene among them),
   weighted by office rank read by the one existing rank reader and by a kept appointment. It orders
   access; it refuses nobody by rank and adds nothing to any contest roll. `04` PART D row 36 (*rank
   never breaks a tie*) is narrowed by A-64; the amendment text is owed and drafted, not applied.
3. **An appointment** is the host's own `commit` (the existing Tenure kind, with a declared term MATTER
   already matures) to an audience Proposition the visitor utters. The formal appointment already exists
   as a docketed petition's dated slot. Honoured, missed and broken are reads of Events that exist.
4. **A petition kept waiting** intensifies by three reads and one draw: the grievance is computed when
   read from the petitioner's own turned-away claims and lapsed papers (the clause
   `20_NARRATIVE_B_what_he_was_owed.md` left owed); the urgency is the present size of the need the
   petition names; the demand, the addressee and the register of his next paper are his sampled choice
   and its drawn band. Nothing moves from the bare passing of time.
5. **The measurement that must precede shipping** is stated as a gate with five arms and a floor
   (§7): the crude arms here are an order of magnitude, not that measurement.

**On the standing rule.** Who is seen first is a draw; whether a host grants an appointment is his sampled
choice and a drawn `commit`; what a kept-waiting petitioner does is his sampled choice and that act's
draw. That a person cannot be in two scenes in one round is bookkeeping of the same kind as a larder
that cannot be drawn twice (`AUDIT_BRIEF.md`: *conservation of stores*), and it decides nothing without
the draw that orders the claimants.

## 1. The baseline, re-verified and corrected

### 1.1 What was run

| probe | what it reads | seeds × seasons |
|---|---|---|
| `occ.py` | the PES_CORE P1e reading re-run (any person id in an executed act's payload), then the row reading (the operand the row's `counterparty:` names) | 0 × 2 |
| `face.py` | face-to-face rows only (derived: the row's typed cell asks the `with` relation of its counterparty operand) | 0, 1, 2 × 2 |
| `arms.py` | BASE (replay control), V1 (one visitor per individual per round), V2 (one scene per person per round, crude) by wrapping `SeasonDriver._admits` in the scratch process | 0, 1, 2 × 2 |

World: `harness/populated.py::build_realm(seed)`, 83 persons (46 individuals, 37 cohorts), the shipped
chooser, no player. The control for every figure: the BASE arm's hash at seed 0 equals PES_CORE's
(`bacd687f1470883b412be9638d0b0f88`), so the tree between `d161a61` and `e1d6180` moved nothing the
probe reads and the wrappers moved nothing.

### 1.2 The 62-of-87 figure

| reading (seed 0, 2 seasons, 1,703 acts, 805 executed) | pairs | counterparty also executes an act of his own that round |
|---|---|---|
| **PES_CORE P1e** (`knock.py:126-146`): any person id in an executed act's payload | 87 | 62 (71%) |
| **row reading**: the operand the verb row's `counterparty:` column names | 50 | 32 (64%) |
| of the row reading's 63 acts: `petition` 20, `issue` 19 (papers; neither cell asks `with`) | | |
| of the row reading's 63 acts: `argue` 10, `tell` 7, `lie` 6, `give` 1 (face to face) | 24 acts | see §1.3 |

The P1e verbs, from its own output (`knock_s0_k2.txt:15`): `create_record` 46, `issue` 30, `utter` 28,
`reconstruct` 25, `petition` 20, `dispatch` 10, `tell` 10, `argue` 10, `lie` 9. A record written about a
person, a proposition uttered about him and a reconstruction of his deed do not need him. **The figure is
true as a count and wrong as a measure of people being in two meetings at once.** F-PES-CORE-06's claim
(*a scene has one person in it*) stands; its size is restated.

### 1.3 Face-to-face interactions (the class A-63 binds)

`face.py`, two seasons each. A face-to-face row is derived, not listed: its typed cell asks the `with`
relation of the operand its `counterparty:` names (`verb_table.yaml`; today `accept`, `argue`, `capture`,
`challenge`, `give`, `lie`, `tell`). Office rank is the highest `rung_kinds` index among the rungs of the
seats a person holds (0 for the seatless), read at the end state.

| reading | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| executed face-to-face acts whose counterparty is another person | 24 | 42 | 29 |
| (round, counterparty) pairs | 22 | 37 | 25 |
| of those, the counterparty executes an act of his own that round | 16 (73%) | 24 (65%) | 16 (64%) |
| of those, the counterparty releases any act that round | 19 | 35 | 24 |
| pairs with two or more distinct visitors | 2 | 5 | 4 |
| of those, visitors of differing office rank | 1 | 3 | 3 |
| executed visits upward / level / downward by office rank | 9 / 9 / 6 | 13 / 17 / 12 | 15 / 8 / 6 |
| **attempted** face-to-face acts (any outcome) | 185 | 214 | 148 |
| attempted pairs / with two or more distinct visitors / of differing rank | 137 / 31 / 13 | 144 / 48 / 24 | 106 / 26 / 14 |
| refused attempts whose recorded read `with` is False | 125 | 136 | 82 |
| refused attempts carrying no False read (an UNKNOWN read or an earlier clause; not separated, `[UNVERIFIED]` which) | 96 | 108 | 113 |
| individuals by office rank (0 / 3 / 4 / 6 / 7) | 14 / 2 / 17 / 9 / 4 | same | 14 / 2 / 16 / 9 / 4 |

(`arms.py` counts face-to-face acts by verb and reads 31 at seed 2; two of them name a person removed
before the run's end, which `face.py` reads at the end state and drops.)

Three readings follow. **(a)** The proportion PES_CORE reported holds on the right class: about two in
three hosts are doing something of their own in the round they are spoken to. **(b)** The class is
small: 22 to 37 meetings in two seasons among 46 individuals. **(c)** Rival visitors exist mostly as
*attempts*: 26 to 48 attempted pairs have more than one visitor against 2 to 5 executed, and about half
of the attempted rivalries are between visitors of differing office rank. Precedence by rank therefore
has a subject once visits form on believed co-location, and almost none before.

### 1.4 Crude occupancy arms (an order of magnitude; not the shipping measurement)

| arm | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| BASE: executed acts / face-to-face executed | 805 / 24 | 830 / 42 | 894 / 31 |
| V1 one visitor per round: executed / face executed / visitors turned away | 800 / 23 / 2 | 824 / 39 / 7 | 892 / 29 / 4 |
| V2 one scene per person per round: executed / face executed | 801 / 11 | 808 / 21 | 859 / 15 |
| V2: visitors turned away (host in his own scene / another visitor first) | 30 / 0 | 39 / 3 | 22 / 5 |
| V2: host's own act displaced by an earlier visitor | 8 | 7 | 8 |
| change in executed acts, V1 / V2 | −0.6% / −0.5% | −0.7% / −2.7% | −0.2% / −3.9% |
| change in face-to-face executed, V1 / V2 | −4% / −54% | −7% / −50% | −6% / −52% |

Limits, stated: V2 refuses a displaced host's own act where the design defers it to his next round, and
lets the host's own scene win whenever it folds first in hash order, with no precedence draw and no
appointment; both overstate the loss. The arms hold the chooser fixed, so nobody yet books, waits or goes
through a clerk. The reading that survives those limits: **occupancy costs the realm a few percent of
its acts and about half of its meetings when the host's own business always wins**, which is why the
design does not let it always win (§3).

## 2. Occupancy (decided; carried by proposal A §1 to §3)

**The rule.** A row occupies its counterparty when its own typed cell asks `with` of the operand its
`counterparty:` names (derived, seven rows today, no list in code). In a round a person is in one
scene: his own, or one he is received in. The read is a local of `resolve()`; nothing is stored. A
visitor who finds the person engaged, or with no scene action left this season, is refused at a new
clause `occupied` and the Event `visitor.kept_waiting` names the person he came to see. A person
received before his own scene folds has that scene deferred to his next round. For the season, the
budget Query subtracts scenes received beside scenes opened (`loop/deliberate.py:175-176`); the set of
received scene ids is kept on the driver beside `_realised` and reset each season, and the number is
computed when asked.

**Within a round and across rounds.** Within: the `engaged` read. Across: only what already crosses,
which is the budget remainder (so a person whose scenes are spent receives no one until the season
turns), the deferred scene in his own queue, and an appointment. No per-person timer exists.

**Steelman of leaving it (J-U5a-05's option A), and the attack.** The steelman: the realm keeps its
throughput and a `Scene` stays one person's budget unit. Attacked by measurement: the throughput at
stake is 0.2% to 3.9% of executed acts (§1.4), so option A protects almost nothing; and by premise: a
player told a thing while he is elsewhere reads it as a defect (PES_CORE §1.1). The steelman fails.

**Steelman of the ruling's reading as built here, and the attack.** The attack: at shipped traffic the
rule fires on 22 to 37 rounds in two seasons, so it may be apparatus for a case that barely occurs. What
survives: the same attack is the finding (§0). The rule is cheap (one derived property, one local, one
set), costs nothing at its control, and is the precondition of the other three parts of A-64.

**Stated limits.** A cohort is never occupied. `interview` names no `counterparty:` and asks no `with`
(`verb_table.yaml`: *"the person questioned exists"*), so a questioning does not occupy the questioned
until the row's owner (`14_VERBS_SOCIAL2_C_case_question_confession.md` §3) declares both; named for that
lane. An office-holder's budget already exceeds the round count (`loop/deliberate.py:97-120`, H-92);
occupancy neither repairs nor worsens that.

## 3. Precedence by rung of office (decided; proposal A §4, §5)

**The reader.** `world_q.office_rank(w, pid)`: the highest `rung_kinds` index among the rungs of the
seats he holds (`rosters.yaml: rung_kinds`: person, hearth, community, settlement, territory, province,
duchy, realm), 0 for the seatless. It is the `rank` stem's ordinal (`world_q.py:4634-4643`) asked of a
seat's rung; the realm's individuals read 0, 3, 4, 6 or 7 (§1.3).

**How it orders.** The scenes that claim one person's round (his own included) form a rivalry group in
the fold order and are re-ordered among the positions they already hold by one drawn net each, with a
level per step of office rank above the lowest claimant and a level for a kept appointment. A higher
rung is usually seen first. It is an ordering of access: it refuses nobody, enters no pool or obstacle,
and is not an input to the visit's own roll.

**No double count.** Rank reaches a visit by three channels with three subjects: the order of access
(this), the `rank_gap` obstacle member, and the `office` leverage source of A-12 before a bench or body
(`U5c_SC_one_obstacle_form.md` §2 member 6, §3). Regard reads stance rows only (*"never rank or
heritage"*, ibid. §2 member 7) and is deliberately not read by precedence; it reaches access through
the host's own choice to grant an appointment. Proposal A's gate row 8 is the execution check that the
roll's inputs do not change with precedence and that a stance sweep leaves every precedence net
unchanged.

**What a lower-rung visitor can do.** Seven routes, each an existing act (proposal B §4): call again;
ask for an appointment; send someone who can get in; the clerk's hand where the seat declares
`passes_through` (A-13); carry the paper to the room; write over the host's head; other means or giving
up.

**Steelman and attack.** The strongest objection is Layer 1's own: `04` PART D row 36, *"rank never
breaks a tie"*, and the standing rule's *"not 'the senior office always wins'"*. A sort by rank would
violate both. A weight on a keyed draw violates neither: row 36's defect is *a hidden turn order*, and
this one is declared data plus the draw. A-64 narrows the row's last clause; the amendment text is
drafted (proposal A edit 8), not applied. Second attack: the host as one of the claimants lets visitors
of rank take a person's round, against S26.3's triage. It survives as a consequence A-63 chose
(*"debited"*); the alternative was measured (arm V2: meetings halve) and the starvation check is a gate
row.

## 4. Appointments (decided; proposal B)

- **The act that books.** The visitor `utter`s an ask (`OUGHT`, subject the host, predicate `receives`,
  value himself); the host answers by his own `commit` to it. No new verb.
- **How it is held.** As the host's `commit` Tenure (an existing kind) with a `Term` the opening act
  declares, which MATTER's existing branch matures (`loop/matter.py:428-434`). No schedule is stored, no
  `Date` is made, nothing happens at CENSUS (`holonic_ARCHITECTURE.md` §29).
- **Honoured, missed, broken.** Reads of the log (`appointment_outcome`): kept; withdrawn by the host's
  `release` (a witnessed `commitment.ended`); lapsed with the visitor turned away (the visitor's
  grievance clause); lapsed unused.
- **Its draws.** `utter`'s (is the ask credited), `commit`'s (does the host bind himself; its band is the
  edge's `degree`), and the precedence draw each round it is relied on. An appointment raises the odds
  of being seen; it is never a certainty.
- **The formal kind already exists**: a docketed petition's dated slot. A sitting seats its attendees by
  the same read as a visit.

**Decided between two carriers.** The alternative is a writ of leave by `issue`: the invitation limb
`admits_audience` already reads (`world_q.py::admits_audience`, limb 4), honoured by `comply`. It would
make appointments an instrument of office: only a seat with the `issue` remit could grant one, and only
within its purview. The `commit` carrier is taken on A-64's own assumption (*a commitment between two
persons*) and because it lets any person promise his time. The writ limb is untouched and still admits a
summoned man to a guarded place.

## 5. The petition that cannot get through (decided; proposal C)

- **What is read.** Rebuffs, not rounds: the Events in which the man or his paper was put off
  (`visitor.kept_waiting`, `carry.refused`, `matter.lapsed`, and the clerk's kinds when they land). No
  Event carries a round and a person may not know the round, and Jordan's ruling on clocks
  (ED-IN-0345) is that such a thing accumulates world events and conditions a choice.
- **Computed when read.** The grievance (`person_q.kept_waiting`, fading with the claims; `dues_unmet`'s
  owed second clause for lapsed papers and promises); the present state of what the petition complains
  of (`world_q.petition_state`: `then` against `now`); the rebuff count (`world_q.rebuffs`).
- **Drawn.** The force of the paper changes only as levels on drawn acts (the leverage source `waiting`,
  on `carry`, `speak` and the hearing's closing draw); the petitioner's next move is his sampled choice
  and that act's draw. No state is stepped.
- **What intensification does.** The grievance: lower regard for the one who kept him waiting. The
  demand: his next paper states today's want. The stakes: a larger ask stands against a larger `stakes`
  term with more `waiting` levels behind it. Other means: lower regard and, through CR-88's
  `grievance_against`, the existing gates of `challenge`, a released oath, refusal, migration, a cohort's
  riot, and A-16's rare attempt.
- **Who sees it.** The person petitioned (the Event names him and he is present); those present; the
  bench or clerk (the roll's named terms); the chronicle (one line per petition, and the story class
  *kept waiting, then …*).

**Steelman and attack.** The steelman for a per-round step (the plain reading of *intensifies while
kept waiting*): it is simple and always visible. Attacked on three grounds, each a citation: the
petition's content is immutable (`04` PART D row 30b; `Record` content written once), a per-round step
is a timer (ED-IN-0345), and a fixed step is the form the standing rule forbids. It fails. The attack
on the decided form: with rebuffs rare, `waiting` levels are rare; this is the dependency of §0 again
and is why proposal C's gate 4 is read on six seasons with A and B live.

## 6. NPC and chooser reads (proposal B §6, proposal C §4)

One chooser serves the player's person and an NPC (`decision/choose.py::score_terms`, sampled by
`_sample_order`); nothing here adds a rule to it. What it reads, all person-side:

| moment | read | owner |
|---|---|---|
| seeks an audience | a `need` or a landed claim; whom he believes holds the seat; where he believes the man is | `14_VERBS_SOCIAL2_B…` §3; `14_VERBS_SOCIAL1_A_formation.md` |
| books | his own `visitor.kept_waiting` claim of that host | proposal B §1 |
| grants | the ask's lean on his pursuits; his regard for the asker; his believed chance of the `commit` | existing score terms |
| waits | `admission_weight` on the remembered refusal | `16_PESSIMIST_CORE_a_refusal_is_remembered.md` |
| escalates | regard lowered by `kept_waiting` and `dues_unmet`; a seat above he knows; a clerk's body | proposal C §1; S2-B |
| gives up | the claims fade (D-48) or the need is met; a drawn `forgive` | `01_CORE_claim_fade_as_read.md`; `14_VERBS_SOCIAL1_D…` §2 |

Characterful means distinguishable: proposal B's gate row 5 (two hosts alike but for their stance grant
at different rates, neither at 0 or 1) and proposal C's gate row 4 (the verbs the kept-waiting take
differ from the control's spread). Legible afterwards: the kept-waiting Event sits in the later act's
cause chain through the scene's occasion, which is what the chronicle's story class reads. No scripted
NPC rule is added anywhere (the AUDIT_BRIEF's scripting-drift test): every row above is an input to the
one score.

## 7. Throughput: baseline, the measurement owed, movers, gates, falsifiers, order

**Baseline (measured here, §1).** Per two seasons at seeds 0, 1, 2: executed acts 805 / 830 / 894;
face-to-face executed 24 / 42 / 31; attempted 185 / 214 / 148; rounds with rival visitors 2 / 5 / 4
executed and 31 / 48 / 26 attempted.

**What the measurement must show before A ships** (proposal A's gate, on the tree where A-9 and
believed co-location have landed, seeds 0 to 4, four seasons): executed acts not below 95% of the
control at any seed; admitted meetings not below 60% at four seeds of five (the crude host-first arm
reads 46% to 50%, and a design no better than that fails); kept-waiting Events above zero; no
individual whose scenes were only ever deferred; the Query reading falls by one per scene received and
no Event carries a budget change. If the 60% floor fails, the dials are `precedence_level` and the
formation proposals, not `scenes_per_round`.

**Declared hash movers.** `occupancy` off its control; `precedence_level` / `appointment_level` off
`None` in a world with a rivalry group; `appointments: on` where a host commits to an ask;
`waiting_valence` and `waiting_level` off their controls where the log holds a rebuff. Every one ships
at its control in its first commit, so each re-pin is one declared step. A-9's re-pin precedes them.

**Gates and falsifiers** are in each proposal; each gate row is an execution artifact (a seeded run, a
planted 400-seed distribution, or a hash equality), none a document.

**Order.**

1. Prerequisites owned elsewhere: A-9's edits 1 to 4; `18_DETERMINISM_rival_acts_in_one_fold.md`
   (`rival_key`); `U5c_SC_one_obstacle_form.md` (the leverage composer); `14_VERBS_SOCIAL1_A_formation.md`.
2. Proposal A, three commits: the derived `occupies`, the clause, the Event and the `engaged` read at
   `occupancy: seat`; then the received set and the Query (`seat_and_debit`); then `office_rank` and the
   precedence key.
3. The measurement (proposal A's gate rows 2, 3, 5, 10) and the ship decision on it.
4. Proposal B (after `14_VERBS_SOCIAL2_B…` §1), then proposal C (regard terms after
   `20_NARRATIVE_B_what_he_was_owed.md`'s first commit).

**Cost on the hot path.** `rebuffs` and `appointment_outcome` scan the log (about 37,000 Events after
two seasons at seed 0); they are read by the chronicle and by a few draws per season, and where a draw
reads them they go through the barrier cache (`queries/cache.py`), not a new store.

## 8. Layer 1 rows graded

| row | what it says | this plan | grade |
|---|---|---|---|
| `04` PART D 36 | the canonical key is declared data plus a hash; *rank never breaks a tie* | **narrowed by A-64**: among the scenes claiming one person's round, office rank is a weight of a keyed draw. Amendment text drafted (proposal A edit 8), owed, not applied | MECHANICAL (the planted 400-seed row: neither share 0 or 1) |
| `04` PART D 35 | a new draw is `H(seed, tick, subject, purpose)` | `precedence:<scene id>` | MECHANICAL; CONVENTION on purpose uniqueness |
| `04` PART D 33; §B.7 | no seat with a modifier | amended by A-12 (text owed by unification). Precedence adds no modifier to a roll | STRUCTURAL (no field); the gate's row 8 |
| `04` PART D 34 | a cache is a local of the step call | `engaged` | STRUCTURAL for lifetime |
| `04` PART D 41, 41a | DELIBERATE is a pure map | seating and deferral are in RESOLVE and the driver; the permutation falsifier is a gate row | MECHANICAL |
| `04` PART D 51; A-62 | a refused act is priced; budget is a Query | the `occupied` refusal costs its scene at release; the received debit is the Query's; no receipt, no `changes[]` | CONVENTION, as `_spent` is today |
| `04` PART D 10a | a write by a non-owner needs a declared basis | none added: the host's `commit` is opened by him and closed by him or by his declared term | MECHANICAL (the gate's existing check) |
| `04` PART D 17, 21; `holonic` §25.1, §29 | three licensed clocks; no rung with a clock; nothing generated at CENSUS | none added: the only time read is an act-declared `Tenure.term` at MATTER | MECHANICAL at load (invariant 5) |
| `04` PART D 25 | no subsystem-specific Event family | one kind, `visitor.kept_waiting`, declared on the seven rows that can emit it | MECHANICAL (derived kind roster) |
| `04` PART D 28 | no branch on a rung-kind member | `office_rank` reads the ordinal | CONVENTION; the synthetic-kind falsifier applies |
| `04` PART D 30b, 44 | a Proposition is immutable; a belief is a `commit` to an `OUGHT` | relied on: the petition is never rewritten; an appointment is such a commit | STRUCTURAL |
| `holonic` §26 | `budget : (Person, View) -> int`, a Query, never a field | `decision/budget.py` unedited; the remainder is computed in `ask_budget` | STRUCTURAL by signature |
| `holonic` §26.3 | petitions: *"No dedup, no cap, no per-venue limit"*; S26.3: the engine does not truncate | conform: a paper is still unlimited; what closes is a person's round, by scarcity at RESOLVE (the section's own close rule); a displaced scene is deferred, not dropped | CONVENTION |
| `holonic` §27 | `order` is a Query: declared, inspectable, no new state | the precedence draw is keyed and pure | MECHANICAL |
| AX-2; S19.3 | a person reads his own ledger; an Event carries no actor | `kept_waiting`, `dues_unmet` person-side; the doer is the holder's attribution | STRUCTURAL under the `decision/` scan |

Two amendments are owed to Layer 1 and are drafted, not applied: row 36 (above) and the sentence added
to #353 §27's order (already owed under A-9). Neither is to be made by an implementation lane.

## 9. Research used, and what the tree does not hold

Used (opened at the line; tier as the tree grades it):

- `research/by_lane/SC_social_contest.md:59` and `:282` (T-SC-3): Liudprand, *De ceremoniis*, Callières,
  Nizām al-Mulk: *"Seating, precedence and audience are negotiated before speech; ceremony absorbs
  contests over standing, not substance"*; graded **sound** as a pattern, two independent lines. It is
  the ground for making access a contest of its own, ahead of and apart from the argument (§3's three
  channels).
- `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §8.1 (`:298-307`): the English
  petition corpus; *who carried the petition (proctors, intercessors, well-placed patrons) shaped its
  success*; royal and church petitions in parallel systems. Ground for the intermediary and clerk
  routes (proposal B §4). Its `:245`, `:342`: the *salutatio* is rank-indexed; *"form is rank-indexed"*.
- `research/governance/political_hierarchy_standing.md:125`: the Roman *salutatio* and *commendatio*: a
  patron's morning reception and his letter as the currency of access. Ground for standing leave as a
  favour held (proposal B §2) and for the intermediary route.
- `unified/RESEARCH_MAP_INSTITUTIONS_A.md` rows `:57`, `:58`, `:71`: the Byzantine material as a *"graded
  protocol of precedence, gifts, and staged audience"*; reception *"maximises distance"*. The first is
  `[CONFIDENCE: high]` in its source for §12.5; the second is a study held back in full, used as
  vocabulary only.
- `proposals/15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md`: the clerk's hand and its backlog
  term reading his scene budget; `…_BYZANTINE_A_dignities_and_the_roll.md`'s U5d line: a dignity's
  precedence step *"may return as a named term"* under A-12. It returns here as the weight of access,
  not as an obstacle member.

Not held by the tree, so not relied on: the *epi ton deeseon* (master of petitions) appears once, in
`audits/15_INSTITUTIONS_BYZANTINE.md:165`, in a roster that audit itself marks memory-grade; the tree has
no sourced account of how an audience was requested, queued or refused at the Byzantine court, nor of
any court's waiting procedure. I do not know those procedures from the repository. No number in this
plan comes from history.

Null, stated: the game-precedent suite was not searched for a shipped game in which a petition's content
grows while its bearer waits; none is cited and none is claimed. `[SKIPPED: research/game_precedent_suite
— not searched for this question; the design rests on the engine's own owners]`.

## 10. Resolutions decided

| # | inconsistency, gap or unclear passage | resolution | ladder step | carrier |
|---|---|---|---|---|
| 1 | the 62-of-87 baseline counts acts about a person, not meetings | restated on the row's `counterparty:` and on face-to-face rows (§1) | measurement | this audit; `16_PESSIMIST_CORE…own_order.md` `Folded:` line |
| 2 | A-63 offers *debited* or *unavailable* | both, as one rule at two grains; three fixture values tell them apart | 5 | A §2, §3 |
| 3 | A-64's assumption reads *elapsed rounds*; no Event carries a round, a person may not know it, and ED-IN-0345 rules a clock is an accumulation of events | waiting is read as rebuffs | 1 (ED-IN-0345) | C |
| 4 | A-64 (rank orders access) against `04` PART D 36 (*rank never breaks a tie*) | a weight on a keyed draw; the row's amendment drafted | 1 (A-64) | A §4, edit 8 |
| 5 | which act books an appointment | `utter` the ask; the host's `commit` | 1 (A-64's assumption), 4 | B |
| 6 | `Tenure.term` is described as built for `oblige` only (`verb_table.yaml` `release.source`) | MATTER's branch is kind-generic (`loop/matter.py:428-434`); a `commit` may carry one | 4 | B §2 |
| 7 | the word `audience` is already a requires stem meaning *may enter a rung* (`world_q.py:4590-4598`) | this plan's code names are `occupied`, `visitor.kept_waiting`, `receives`; `audience` keeps its one sense (CLAUDE.md §4) | 5 | A, B |
| 8 | `holonic` §26.3 forbids a per-venue limit on petitions | occupancy closes a person's round by scarcity, not a venue to papers | 3 | §8 |
| 9 | the rival-acts draw takes its pool from the act's verb; a claim on a person's time has no skill | for the `("round", person)` key the pool is the ordinary score plus levels; same roller, same re-order | 5 | A §4 |
| 10 | a hearing's attendees and a negotiation's parties are assumed free | a sitting seats those who move in it; an engaged attendee is absent and the sitting's `silence` rule applies | 4 | `Folded:` lines |
| 11 | NARRATIVE_B's petition clause was owed and marked `[UNVERIFIED]` | carried: `dues_unmet`'s second clause | 4 | C §1 |
| 12 | a questioning occupies nobody (no `counterparty:`, no `with` on `interview`) | named for the row's owner; no edit here | 5 | §2 |

Twelve resolutions.

## 11. For Jordan

Nothing is held. Three choices were decided on his own words and are reversible on a word; each with
its two options and how they differ as games:

1. **Is a host's own business one of the claims on his round?** *Decided: yes, weighted by his own
   office* (A-63: *his scene budget is debited*). The other option: his own scene always stands and
   visitors reach only the idle or the appointed. That game has untouchable schedules and half the
   meetings (measured, §1.4); this one lets a superior's call take a person's round.
2. **Does being kept waiting add force to the paper, or only to the man?** *Decided: both* (A-64: *the
   petition content intensifies*). With the `waiting` levels a ruler pays for delay in the room as well
   as in sentiment; without them (`waiting_level None`) neglect costs only regard.
3. **What an appointment is.** *Decided: the host's own `commit`* (A-64's assumption). The other option,
   a writ of leave by `issue`, makes appointments an instrument of office that the seatless can neither
   grant nor be bound by.

Layer 1 text owed on his amendment only: `04` PART D row 36 (§8).

## 12. Folded into earlier files (a `Folded:` head line each; no finding of another lane deleted)

`proposals/16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`, `01_CORE_one_scene_contract.md`,
`18_DETERMINISM_rival_acts_in_one_fold.md`, `05_SC_playable_hearing_B.md`, `05_SC_negotiation_scene.md`,
`14_VERBS_SOCIAL1_D_grievance_and_settlement.md`, `20_NARRATIVE_B_what_he_was_owed.md`.

## 13. Evidence log

| command | seed, seasons | outcome |
|---|---|---|
| `occ.py 0 2` (first attempt, without the repository on the import path) | — | did not run: `ModuleNotFoundError`; the wrapping shell reported 0. Re-run below |
| `occ.py 0 2` | 0, 2 | hash `bacd687f1470883b412be9638d0b0f88`; P1e 87 / 62 reproduced; row reading 50 / 32; petition-path kinds |
| `arms.py S 2` | 0, 1, 2; 2 | BASE hashes `bacd687f…`, `8aae8412…`, `89109213…`; V1 and V2 as §1.4 |
| `face.py S 2` | 0, 1; 2 | §1.3. Seed 2 first raised `KeyError` on a person removed before the run's end; the probe was corrected to read rank 0 for such a person and re-run (`face_s2.txt`) |
| `git status --short` at the close | — | this audit, the three `28_CORE_scene_access_*` proposals and the seven `Folded:` lines, all inside the suite directory |

No `pytest` was run. No tracked file outside the suite directory was written.
