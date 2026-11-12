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

