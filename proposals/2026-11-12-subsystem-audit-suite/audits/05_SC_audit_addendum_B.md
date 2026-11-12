# SC — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: daa1fb1 (working tree; code, registers and workplans are as at `601e715`, the first audit's read point — the commits between touch only `proposals/2026-11-12-subsystem-audit-suite/`)

This addendum continues `audits/05_SC_audit.md` (§0–§17; findings F-SC-01 to F-SC-14; resolutions
G-01 to G-35; proposals SC-P1 to SC-P8). It edits neither that file nor its proposals. Short names as
there: `es/` = `engine/season/`; `K/` = `systems/social_contest/sim/contest/`; `PS/` =
`proposals/2026-09-05-proceedings-subsystem/`; `PD/` = `proposals/2026-10-29-parliament-and-debate/`;
`P4` = `PD/2026-11-01-social-contest-proposal-4-authority-staged.md`; `3L/` =
`.audit/2026-08-06-social-contest-three-lens-audit/`. A file name ending `_B` supersedes the first
lane's proposal of the same stem; `SC-Bn` names this lane's additional proposals (§B6).
Every run is `PYTHONHASHSEED=0`; outputs are in the scratchpad named in §B7.

## B0. Verdict of the addendum

**The first audit's verdict on the code stands; its design answer to the standing requirement does
not, because it contradicts a ruled item it did not list.** Jordan ruled on 2026-10-03 (`ED-IN-0285`,
statements 13 and 16, verbatim in §B2) that a social contest is its own container with its own game
state, called by the season loop through its verbs, with non-player contests resolved by an automated
mode *in the module*. SC-P3 makes the played hearing the season loop on a fixture with *"no nested
bout engine … no suspension inside a provider"*. The full evidence settles the kernel question
differently from both "adopt" and "retire whole, forward nothing": the kernel's **code** retires
(ruled, measured unadoptable), and the kernel's **exchange game** is the specification of the
module's second entry, a sitting, of which today's one-draw roll is the degenerate case with no
exchanges. That is one code path with two modes on the suspension shape `ED-IN-0349` already ratified
for combat. The reading also produced one measured defect the first audit did not have: at the
shipped ceiling arm, cited proofs change nothing against a strong opponent (§B2, F-SC-16).

## B1. What was read

| item (the first audit's NOT READ list, then this lane's additions) | how read |
|---|---|
| `K/_kernel_tests.py` | in full (1–1727) |
| `K/resolver.py`, `primitives.py`, `contract.py`, `policy.py`, `wrapper.py`, `agon_harness.py`, `modes.py`, `armature.py`, `narrative.py`, `faction.py`, `appraise.py`, `degree_extension.py`, `__init__.py` | in full |
| `K/rhetoric.py` | in full, lines cut at 420 characters (long comment lines truncated) |
| `K/dictionaries.py` | header and an outline of every table row (765 lines not paged) `[PARTIAL]` |
| `es/state/gate.py` | head (1–66), every definition by outline, the basis constants (205–283), `sits_over` and `may_determine` (899–980) in full; the rest by outline only `[PARTIAL: about 1,600 of 1,932 lines not paged; they are CORE's and FA's bases]` |
| `es/loop/matter.py` 746–904 | in full (larders, yield, the travel leg's end, wear: nothing of SC's) |
| `research/by_lane/SC_social_contest.md` 143–799 | in full, table rows cut at 430–750 characters |
| `research/game_precedent_suite/tables/R4`, `R5` | §1–§2 of R4 (Disco Elysium, Griftlands), §3–§5 and §7 of R5 (Pentiment, L.A. Noire, Disco Elysium, the cross-game table) in full; Baldur's Gate 3, Kingdom Come, Obra Dinn, Shadows of Doubt and CK3 rows by search only `[PARTIAL]` |
| `…/tutorials/T05`, `T06` | Griftlands, Pentiment and L.A. Noire sections by mechanism search (70 lines read); not paged end to end `[PARTIAL]` |
| `research/by_lane/FI_fieldwork_investigation.md` | not opened `[SKIPPED: context budget; the FI lane's own audit §16 and `08_FI_05` were read instead]` |
| `architecture/holonic_ARCHITECTURE.md` | in full (2,077 lines) |
| `architecture/meta/04_CODE_ARCHITECTURE.md` | §C.5 (the contest seam), §C.12 and the no-second-resolver row only |
| Gate A, B packets (`_workings_joined.md`) | in full; their `verdict_log.json` files not opened `[SKIPPED: raw judge logs]` |
| Gate C packet (`2026-07-01…/GATE_C_packet.md`) and `2026-07-02…/final_build_summary.md` | in full; `GATE_C_packet_raw.json`, `verdict_log.json` not opened |
| `.audit/2026-07-01-contest-player-interaction/…walkthrough_v1.md` | in full |
| `.audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md` | in full |
| `.audit/2026-06-03-contest-groundup/engine.py` | not opened (its content is `degree_extension.py`'s citation) |
| `3L/00_synthesis.md`, `03_…adjudication.md`, `06_adversarial_audit_of_05.md` | in full |
| `3L/04` §0–§5, §14–§16; `3L/05` §0–§6; `3L/07` §1, §3, §5–§9 | by section; `3L/01`, `02`, `sources/` not opened `[PARTIAL]` |
| fourteen cross-cutting `.designs` documents | `conflict_architecture_proposal.md` to the Tensions Deck; for the other eleven, every line naming a contest, debate, hearing, tribunal, negotiation or trial, plus `integration_proposal_v30.md` Mechanism 3 and PART 9 and `videogame_mode_spec.md` §1.2 `[PARTIAL: not read end to end; nothing below rests on an unread passage]` |
| `PS/05_PROCEDURE.md` PART B–C, `07_THE_GAME.md` B.2–C.2, `19_PLAN.md` step 14, `21_RECONCILIATION.md` steps 6–16 | by section |
| `P4` §1, §3.1, §3.3–§3.5, §4 (all), §9 head, §11, §12, the critic's pass | in full for those sections |
| `PD/2026-10-30-social-contest-primitives-and-kinds.md` §1 (rulings R-1 to R-41, S-1 to S-8) | in full |
| `proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md` | §0–§3a |
| `proposals/2026-10-07-grid-mode-suspension.md` | head, §1, start of §2 |
| `registers/editorial_ledger_in.jsonl` `ED-IN-0284`, `ED-IN-0285` | the rows in full |
| completion pass (Opus): `05_SC_evidence_and_rebuttal.md` (SC-P8) and `05_SC_capability_surface.md` (SC-P7) in full; `08_FI_05_evidence-interface_B.md` in full; `10_DICE_capability_axiom_map.md` §A–§C and §G; `01_CORE_capability_authoring_surface.md` part two's edit 8; `02_CHAR_capability_definitions.md` head; `verb_table.yaml` rows of the ten social verbs (parsed); `sigma.py` 117–216; `person_q.py::stance_toward`; `options.py::_pair`; the seeded `negotiation` arrangement row and `data/arrangements.py`'s mutual-disposal report | in full for the ranges given |
| this suite: `audits/08_FI_audit.md` F-FI-09, F-FI-10, §16; `08_FI_audit_addendum_B.md` (a stub at reading); `proposals/08_FI_05`, `12_ARCS_cited_evidence.md`, `02_CHAR_capability_uses_table.md`, `01_CORE_capability_authoring_surface.md` (part one), `10_DICE_advantage_sources_for_the_arcs.md`, `10_DICE_one_score_two_roles.md` (heads); `audits/02_CHAR_audit_addendum_B.md`, `10_DICE_audit_addendum_B.md` (heads) | as stated |
| code opened for this addendum: `modules/social_contest/roll.py`, `es/queries/inputs.py`, `es/seam/wrappers/sigma.py` 100–555, `es/queries/world_q.py` 720–885, `es/loop/driver.py` 388–520, `es/decision/budget.py`, `es/decision/options.py` 1465–1524, the contested rows of `verb_table.yaml` (compact), `rosters.yaml` (capability and proceedings rosters) | in full for the ranges given |

## B2. Corrections to the first audit, and new findings

### Corrections

**C-1 · SC-P3 conflicts with a ruled item the first audit does not list (now F-SC-15).**
`ED-IN-0285` (ledger row, `status: resolved`, RULED BY JORDAN 2026-10-03), statement 13, verbatim:
*"remember that social contests occur within their own Godot container, ie they are their own unique
game state that does not occur on overview/season loop. season loop determines calling of container
through its verbs as well as handles the output of the container results. note that when non-player
social contests occur, they will be routed through an automated resolution in the module that does
not call forward a playable scene"*. Statement 16 lists *social contests* among the containers
playable as a minigame; statement 11 says the module must *"exist on its own"*. The row's decision
text: *"each has an AUTOMATED mode (headless, non-player and Python oracle) and a PLAYABLE mode (a
Godot scene in game/)"*, and it lists *"the suspension design for playable modes"* as open. That
design has since been written and ratified for combat (`proposals/2026-10-07-grid-mode-suspension.md`,
`ED-IN-0349`; built as REM-31): the driver suspends at ENCOUNTER, inside one provider call, as a
call-out to a decider (`es/queries/inputs.py::PlayHost`). `modules/social_contest/roll.py`'s first
line already calls itself *"the AUTOMATED MODE of the social contest scene's contest provider"*, and
`sigma.resolve` accepts `host` and does not use it. The first audit's §5 list of rulings accepted as
binding has none of these, and SC-P3 decides the opposite (*"No nested bout engine, no second
resolver, no suspension inside a provider"*; audit §9: *"There is no pause because there is no scene
to enter"*). Steelman of SC-P3: its three real gains are kept (season acts file the case; the case
file is the hearing's persistent record; choices are Candidates the one chooser scores). What does
not survive is the placement of the played game in the host. Superseded by
`proposals/05_SC_playable_hearing_B.md`.

**C-2 · Audit §11 item 2 (G-24) is answered by the ladder and is not a survivor.** Whether the Gate
ratifications (`ED-1056` to `ED-1062`) lapse was listed for Jordan. Step 1 answers it. (i) Jordan's
2026-09-05 scope ruling (`PS/README.md:102-109`, quoted in the lane research file): the proceedings
design *"will not refer to any previous work concerning social contests"*. (ii) `ED-SC-0033`:
*"orphaned social contest code: retire it"*. (iii) The later statements recorded as R-31 to R-41 in
`PD/…primitives-and-kinds.md` §1 re-state where capability and weight come from (attribute, title,
office and faction by venue and contest type; office weight on roll and obstacle; a pool typically
of five dice or more), which replaces the kernel's faculty, adjudicator-primary and Face-ceiling
rules. (iv) Two of the seven were never executable: `ED-1060`'s Terminal Doubt has no consumer even
in the kernel (probe, §B7 run 1: zero non-comment lines of `K/resolver.py` name it; its own test
asserts *"resolver does not yet consume orientation"*), and `ED-1056`'s `face_current` cannot be
reached through `build_contest` (`K/wrapper.py::_as_contestant` never sets `charisma`; the three-lens
audit's F2, re-read at HEAD). Per item: `ED-1057` (bench ballot weighted by standing) survives as
behaviour in R-38 and is carried (§B3); `ED-1059` and `ED-1061` are row data and a no-GM fix, already
the Proceedings design's premise; `ED-1062`'s armature survives as a judge's leaning expressed in
trait rows (SC-P7) and its numbers were `[SEED]`. Nothing is left for Jordan to choose between.

**C-3 · "What the kernel has that the loop lacks is design, not code" (audit §5) is true and its
list is short by seven items.** The audit names four (a per-exchange choice, defeat by a named fault,
a verdict that can cross the room, a chronicle). The full inventory is §B3.

**C-4 · SC-P8 names the wrong owner for "contradicts".** It cites `decision.agreement`. That
function pairs by predicate on the `person_predicates` roster (claims about oneself,
`es/decision/options.py:1465-1488`). The one pairing step is `_pair` (`:1491-1521`): same key, whole
value, `==`. `08_FI_05` names `_pair`; this lane follows it (§B4, G-43).

**C-5 · The first audit's Victoria 3 entry (§7, "did not transfer") is half right.** The parameters
do not transfer (the lane research file says so). The shape does, and it is already in the plan's
target specification: P4 §3.5's repair (e) holds a failed stage to the next sitting and closes it
against the roller on the third failure (sourced to the Venetian Forty's third ballot). That is a
staged enactment with setbacks. It also meets SC-P6 (§B6, G-55).

**C-6 · The first audit read `PD/` through the batch card only.** The live target specification is
P4 as cut by its own critic (*"the target specification for the choice layer once Proposal 1's core
and the dead core run"*; about five choices robust: proofs, self or advocate, naming mortal enemies,
the warrant duty, appear / evade / defy). All five are choices made *around* the room. Inside the
room P4 has one draw per stage and its own NERS admits *"speech kinds differ by hundredths of a
sentence"*. That is the gap §B4 fills, and it is why the division in G-40 falls where it does.

**C-7 · A provenance caution on R-31 to R-41.** They are quoted as Jordan's words in
`PD/…primitives-and-kinds.md` §1 (*"this session"*, 2026-10-30), a PROPOSED document. A search of
`registers/*.jsonl`, `registers/handoffs/`, `workplans/` and `references/` for three of their phrases
returns nothing (§B7 run 5). They are used below as intent of high weight, never as RULED. The
orchestrator may want them ledgered; that is a process edit and no game fact depends on it here.

### New findings

**F-SC-15 · blocks the standing requirement · The proposed played hearing is on the wrong side of a
ruled boundary.** C-1. Falsifier: a ruling later than 2026-10-03 placing the played social contest on
the season loop; none found in the SC, IN ledgers or the lane handoff. Fix:
`05_SC_playable_hearing_B.md`.

**F-SC-16 · degrades narrative (R-02, R-06) · At the shipped arm, evidence is inert against a strong
opponent.** `modules/social_contest/roll.py::obstacle` subtracts the room's terms and then applies
the ceiling. Measured with the module's own `obstacle` and `band_odds` (§B7 run 3): pool 2 against an
opposing score of 8, proofs 0, 1, 2 and 4 → obstacle 2.842 in all four rows, odds
(0.900, 0.081, 0.019, 0.000) in all four. Against no score, the same four proofs move the obstacle
2.0 → 1.0 and Failure 0.74 → 0.42. So a case made from what is held helps only where the opponent is
weak or absent. The docstring states the clip (*"a room of +1.5 against a base of 4 under a ceiling
of 2 changes nothing"*); P4 §3.3 and its critic's finding 8 name it at design level; nobody had run
it on the shipped function. Control: the same rows at pool 5 and pool 8 against 8, where the base
sits under the cap, move as expected (0.802 → 0.620 and 0.561 → 0.386 Failure over four proofs).
Fix: the bound order in `05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B1 folded there, G-68).

**F-SC-17 · degrades narrative · Layer 1 says the argument layer resolves by named fault; the loop
has no fault and no issue ladder.** `holonic_ARCHITECTURE.md` §2, T7: *"the argument layer resolves
by named fault, not by a persuasion threshold"*; §54.3 records the twelve named faults and the stasis
ladder as scoped out by a declared narrowing (the deferred subsystems), not dropped. In `es/` a
contest ends on a margin and nothing else. `rosters.yaml: ladder_rungs` holds the six concession
speeches (`deny … hand_error_back`) and the lane research file shows its note calls them the issue
ladder (§3.3 #2, K-SC-4). The kernel has both (`DefeatCatalogue`, `Stasis`) and they are among the
things the three-lens audit could not break (`3L/00` §7). Falsifier: any reader of a fault or of an
issue rung under `es/` or `modules/social_contest/` — none (`roll.py` reads eleven numeric fields).
Fix: carried in `05_SC_playable_hearing_B.md`.

**F-SC-18 · hygiene, with a design consequence · The kernel's played menu is solved by a constant
policy, measured.** §B7 run 1, seed 7, 600 bouts per cell, faculty 4 against 4: at `court` a policy
that plays the logos appeal every turn wins 0.83 to 1.00 against every other scripted policy; at
`disputation` 0.71 to 1.00; at `assembly` the roles swap and the constant pathos policy wins 0.99
against it. `hard` and `advance` produce the same gain at the same seed in 400 of 400 and `hard`
costs two more (three-lens F9, re-run). The interactive harness, driven by a script answering 1 to
every prompt, returns a decisive win in three exchanges; answering 2 loses in one exchange on a
barred-device clinch; answering 3 returns a compromise (single runs; the harness seeds nothing, so
these are observations, not rates). The first audit took the "answer 1" result from `D_T05` row 12.
Consequence for SC-05: what is carried is structure (a board, a hand, faults, a closing judgment),
never the seven-verb menu or the Style and appeal picks.

**F-SC-19 · hygiene, a register row · H-56's held half does not block a hearing.** The row's open
half is *a DELIBERATE nested inside RESOLVE*; the lane research file's K-SC-12 sends it to Jordan as
surviving all five steps. For the hearing it is answered at step 4: the ratified suspension is a
call-out from inside one provider call at ENCOUNTER, after the round has folded, and no step of the
loop is re-run. A sitting needs deciders, not a nested DELIBERATE (G-37).

**F-SC-20 · degrades narrative (R-06) · The room averages the bench.** Not a defect of `es/` today
(no bench term reaches `determine`), but of every design on file: the kernel averages member minds in
play and ballots per member only at close; SC-02's commit term sums over the bench; CP-T05-01 puts
one judge's regard on one draw. The provided characters (NPC-001, NPC-071) are individual judges.
Fix: per-seat records in the sitting's input and a per-seat ballot on `declared` rows (§B4, G-50).

## B3. Kernel versus proceedings, settled on the full evidence

**The question as the plan puts it** (`workplans/…v11_part5.md` SC-05): *adopt the kernel as the
social contest scene's automated mode, or keep the interim provider*; Jordan's lean, indirect, is
adopt; A1-58 makes the timing the plan's.

**The evidence, in order of weight.**

1. *Ruled.* The Proceedings subsystem owns all social contests; orphaned code retires (`ED-SC-0033`).
   A social contest is a container with an automated and a playable mode in the module
   (`ED-IN-0285`). Auto and played are one conflict at two fidelities (`ED-SC-0013`). One ladder, a
   margin never a winner, one obstacle owner (`ED-SC-0031`/`0032`/`0033`). A proceeding is defined
   parameters (R-12 in `PD/`'s table; `PS/README.md`).
2. *Measured.* The kernel's entry takes no generator, moves the process-global stream and returns a
   winner (`roll.py` docstring, SC-01 step 15; re-run here: `build_contest` and `resolve_contest`
   signatures, the stream moves, the return is `('committee', 'win')`). Everything ratified at Gate C
   is unreachable from that entry (no `armature=` parameter). Its menu is solved by a constant policy
   (F-SC-18).
3. *Layer 1.* `holonic` §39: a battle, a hearing and two brothers arguing over a barn are the same
   call with different act vocabularies; §27.2 and §44.3: no second resolver, and a wrapper never
   decides or resolves; §39.4: a subsystem that needs more than the general ladder declares, it does
   not fork; T7: argument resolves by named fault.
4. *Design on file.* `PS/05` PART B and `19_PLAN` step 14 already specify the provider as a nested
   run with three in-run aggregates (the rung a matter has reached, proofs told so far, momentum),
   ending when nobody acts, the ladder bottoms out or a term matures, *"the provider never writes"*.
   `world_q.proofs`' docstring says the design spends proofs one at a time inside that run, *"which
   is where hoarding one becomes a choice"*. It was never built; R-03's rounds (U2) and the plan's
   verb-row choices took its place for everything outside the room.
5. *Earlier audits.* `3L/04` §2: under the duality doctrine, if auto and played have equal
   expectation and every output is a scalar, playing is wasted attention; the played mode must change
   *which* consequences occur. `3L/04` §4 reduces the kernel to eleven primitives; `3L/00` §7 lists
   what survived attack (the evidence dossier, the fault catalogue, the per-member ballot, pressure).

**Decided.** The two are neither rivals nor layers. *The proceedings are the host; the sitting is the
module; the kernel was a prototype of the sitting written before the host existed.* SC-05's "adopt"
and "retire" are both satisfied by one move: retire `K/` and implement the sitting as a second entry
of `modules/social_contest/` whose closing draw is today's `roll`. Ladder: step 1 (the rulings in 1),
step 3 (`PS/05`, `19_PLAN` step 14), step 4 (REM-31's suspension), step 5 (the degenerate-case
construction, which is what makes it one code path). Proposal:
`proposals/05_SC_sc05_kernel_disposition_B.md`.

**What the kernel has that the loop lacks, and where each goes.**

| kernel mechanism (file) | in `es/` today | disposition | home after |
|---|---|---|---|
| a run of exchanges with a move per exchange (`resolver.py::Bout.resolve`) | one draw per act | **carry** (structure only) | `modules/social_contest/hearing.py::hear` |
| the issue ladder and reframing (`primitives.py::Stasis`, `shift`) | absent; the charge ladder carries its name | **carry**, four rungs as data | roster `issue_rungs`; the case file's current stage (P4 §3.5) |
| evidence as held items: relevance to the live issue, a hidden weight, diminishing corroboration, a cap (`Dossier`, `EvidenceItem`, `EVIDENCE_CAP`) | one float over a whole ledger | **carry**, on FI's two carriers | `05_SC_evidence_and_rebuttal_B.md` |
| rebuttal that erases an opponent's standing point, bounded (`rebut`, `REBUT_CAP`) | the silent mirror | **carry** as `answer` by a held contradiction | same |
| defeat by a named fault, configured per venue (`DefeatCatalogue`, `FaultState`) | absent | **carry**, as data rows per arrangement | roster `hearing_faults` |
| who bears the question (`ProofBar`, `GraceThreshold`) | absent; biased defaults only | **carry** as the row's `bears:` map (P4's rite) | `arrangements.yaml` |
| the room against the verdict: a per-member ballot that can cross the momentum (`VoteAtClose`, weighted, `ED-1057`) | `declared_votes` counts commits, unweighted, on one row | **carry** per seat, weighted by office | the sitting's `ballots`; `world_q.declared_votes` unchanged |
| what moves this judge, read in bands (`armature.py`, `appraise.py`) | absent | **carry the idea**: a seat's leaning as data, revealed by degree | SC-P7 trait rows; the turn view (§B4) |
| outside pressure on the bench (`Pressure`) | absent | **carry the idea**; the source is R-36's legitimacy and the bench's public commits | SC-02's commit term; FA's lane |
| effort as a spent pool (`Reserve`) | `effort` 0–2, scene slots | **carry** as the attendee's own budget; no second resource | `Act.effort` |
| a chronicle of the run's shape (`narrative.py`: ROUT, REVERSAL, COLLAPSE, SPLIT_DECISION) | absent | **carry** as a reader of the outcome's exchange list | harness / WR lane, over SC-P1's record |
| venue as a row of parameters (`modes.py::PROCEEDINGS`) | `arrangements.yaml`, 13 keys, 3 read | already the host's | — |

**Dead, with the observation that kills each.**

| kernel part | why it dies |
|---|---|
| the seven-verb menu; `hard`; `SelfGating` | solved by a constant policy; `hard` is `advance` at +2 cost (F-SC-18) |
| Style × genre × orientation, CR4's `+1D`, `INTERACTIONS_TABLE` | `3L/00` §2.2: Obscuring dominated, genre empty on seven of eight proceedings, Projection's bonus unreachable; `derive_interaction` is printed as flavour and read by no resolution line (`agon_harness.py:459-465`) |
| Doubt Marker, Terminal Doubt | never consumed (probe) |
| `FaceScale`, `Contestant.charisma`, `split_standing`, audience resistance | unreachable through the public entry or declared metadata-only (`wrapper.py` F10 note) |
| `faction.py` | a faction as a combatant and a vote as a pooled roll: Layer 1's fourth leak and second resolver; `Faction.fixed_lean` is an entity special-case |
| `policy.py`'s eleven policies | a decision procedure beside the chooser (scripting drift) |
| the thirteen venue presets, `RhetoricalWeights`, the adjudicator profiles | `[SEED]` numbers with no producer; the row owner is `arrangements.yaml` |
| `GAMES` stubs, `MECHANICS`, the design-memo dictionaries, `_kernel_tests.py` | apparatus about the kernel |
| `degree_extension.py::PoolDesaturation` | its stated reason is `_advance` using the band as a magnitude; the sitting enters whole items, not band-scaled gains (SC-P2's finding stands) |

**What "wasted attention" requires of the carry.** The sitting must change which consequences occur:
which items stand on the record afterwards (and are citable, forgeable, appealable), which rung the
matter was decided on, which fault is on whom, which seats crossed. `HearingOutcome` therefore
returns those as typed fields and the host writes them to the case file; the closing margin is one
field among them.

## B4. A playable social contest

Detail, typed records, gates and falsifiers are in `05_SC_playable_hearing_B.md`,
`05_SC_evidence_and_rebuttal_B.md` and `05_SC_negotiation_scene.md`. This section states the design
and where each part comes from.

### B4.1 Three places, one path

| where | what a person does | carrier | who decides |
|---|---|---|---|
| **around the room** (the season's rounds) | petition, carry, open a case, appear or evade or defy, choose a forum, retain an advocate, investigate, forge, examine, **file**: a `speak` on the docketed matter naming the items he puts on the record | verb rows (B10-18c's CR-57 to CR-63); the case file `Record` | the one chooser, or the player's callback (`dispatching_chooser`) |
| **in the room** (one sitting, at ENCOUNTER) | present a filed item, answer one, argue, impugn a source, concede the rung, rest; the bench rules or adjourns | the module's own state for the length of one call | a decider per attendee: the player's (`PlayHost`) or the host's NPC decider |
| **after the room** | nothing new: the host writes the outcome to the case file and opens the disposal; WITNESS deposits what was said | Events, `Record.stages`, the disposal Tenure | — |

The sitting is called by the bench's `determine`, deferred to ENCOUNTER as `fight` is; `speak` stays
an undeferred single draw and is the filing act. With nothing filed and no effort the sitting is
today's single draw, bit for bit: that is the control arm and the reason there is one code path.
(P4 §3.5, a design and not a ruling, closes a proof stage by the draw of whoever bears it. Here the
determiner always draws and `bears:` governs the silence fault. The difference is CR-62's to
reconcile when it builds stages; it is named so it is not discovered.)

### B4.2 What the player chooses in the room

Six moves, one surface for every contest type (R-33 as recorded in `PD/`), limited per arrangement
row by data:

| move | needs | resolved by | effect on the board |
|---|---|---|---|
| **present** an item | an unplayed filed item of his side, of a kind the row admits | no draw (an item is what it is) | it stands on the live rung at its weight |
| **answer** a standing item | a filed item that contradicts it (same subject and predicate, different value), or a finding that names it forged | no draw: the heavier stands | the target is struck, or halved if heavier |
| **argue** the live rung | nothing held | one draw on the same `roll`, his capability for the row's speech kind against the other side's score | an argument stands (Success or better), half-stands and brings a subsidiary point forward (Partial), or does not |
| **impugn** a source | a filed deed-claim about the person an opposing item comes from | one draw | every item of that origin is halved; on Failure the impugner carries a level against him for the sitting |
| **concede** the rung | — | no draw | the matter descends one rung; his items on the conceded rung leave the board; witnessed |
| **rest** | — | — | nothing; when all rest in turn, the sitting closes |

Held evidence is deterministic and argument is rolled. That is the classical division the three-lens
audit recovered (`3L/05` §4.2: the orator cannot make a contract more probative, only choose when to
produce it), it is how Pentiment scores an accusation (points for each fact found, plus background),
and it answers the brief's question directly: a case's strength comes from what is held, filed and
left standing; skill decides argument and the closing draw.

### B4.3 How a round resolves without a GM

The module applies the move's row to the board, checks the row's faults, and passes the turn in the
arrangement's `order`. Faults are deterministic conditions on the typed board (data, per row):
*self-contradiction* (a side's own two standing items disagree: the lighter is struck and a level
counts against it); *silence* (the side that bears the rung rests with nothing standing on it, or the
other side rests under an unanswered standing item: the rung is conceded); *forgery found* (an item
struck by a finding: every item of that origin is struck); *irrelevance* (an item presented on a rung
it does not bear on enters at half; the row may count strikes). The sitting ends when all rest, when
every attendee's `effort` is spent, or when the ladder has nowhere to descend. Then **one closing
draw** — today's `roll`, by the calling act's actor — reads the board as its room term through the
module's own `obstacle`, and on a `declared` row each seat is balloted separately. The engine never
names a winner: a fault moves the board and the draw can still go either way.

### B4.4 How the other side chooses

One interface for everyone: `decide(HearingTurnView) -> move`, where the view holds the public board,
the mover's own unplayed items, his effort and the legal moves. A player's person is served by
`PlayHost.decide`. Every other attendee is served by a decider the host builds from that person's own
interior (pursuits, stance toward the other party, appetite) and the module's pure
`closing_odds(board)`: each legal move is a Candidate; its value is the believed verdict after the
move, weighed by what the verdict means to him, less what the move costs him (an item exposed, an
enemy made, a concession witnessed, effort). No policy lives in the module and no person is
special-cased. What makes two advocates differ is data: their capabilities, what they filed, what
they will not give up.

### B4.5 What the precedents contribute, and what is refused

Sourcing marks are the tree's (`R4`, `R5`, `T05`, `T06`, the lane research file §2.2).

| precedent | taken | refused | sourcing as the tree records it |
|---|---|---|---|
| Burning Wheel, Duel of Wits | stakes declared before the first exchange (the row's disposal map is on the entry screen); a compromise scaled to what the winner lost (the loser's standing items raise the judge's obstacle, so they lower the band and with SC-P4 the disposal) ; three volleys to an exchange (`interactions_per_scene` 3) | a fixed manoeuvre matrix | rules T0; the Point-and-Dismiss collapse is one actual-play account, `[UNVERIFIED]` |
| Victoria 3 enactment | a stage that can fail and be held to the next sitting; opposition organising between sittings (answers filed, seats argued with) | its numbers | official wiki T0; counter-mobilisation `[UNVERIFIED against current patch]` |
| Griftlands | arguments that persist on a board and must be answered; a hand that depletes; conceding at the start of a turn to keep what is unspent; relationship setting the opening position | deck-building and the random draw; spending to bend a roll as the core loop | Klei posts and wiki via API (V3, alpha-era pages); the "less fun than fighting" quote T2 |
| Disco Elysium | a passive check with no dice deciding what a character notices (an `insight` threshold on what the turn view shows of the bench); odds shown for an active check (as the character believes them); a failed red check as content | a grader of the player's theory (it has none) | wiki via API (V2/V3); the shown figure equals 2d6 arithmetic |
| Ace Attorney, Danganronpa | testimony on the record; an item presented against one named statement; a price for presenting the wrong item | one authored correct statement per round; any truth oracle | T2; the proceedings relay deleted the lock-and-key conversions (P1, P8) |
| L.A. Noire | an accusation needs a held item; a missing clue removes the option; doubt is pressing without proof | an authored correct answer per question | Wikipedia and wiki (V3) |
| Pentiment | an accusation scored by facts found and background, with no check against the truth; a biased judge; a community that remembers; finite time | — | developer interviews and wiki (V3) |

**Nulls, marked.** No game in the corpus has one simulated person build a case that another answers,
a forged exhibit accepted and later overturned by a finding, or argument content modelled. Nothing
above claims a precedent for those; the gates in the proposals are the only evidence they will have.

### B4.6 The stationary-menu test, applied

The lane research file records that nobody has assessed the Griftlands objection against the
proceedings design. Assessed here. P4's hearing is a loadout chosen once per stage followed by one
draw: the menu does not repeat because there is one turn, and the critic's count (speech kinds
differing by hundredths) is what that structure yields. The sitting's legal moves are a function of
the board and of a hand that only shrinks, three of six moves need a specific held item, and two
faults punish the repeated safe move (resting under a standing item; presenting off the rung). That
is non-stationary on paper. The proposal's gate includes the run that would show otherwise: three
constant deciders against the chooser's decider over seeded hands.

### B4.7 Conflicts with ruled items — named, not resolved

- **`ED-IN-0285` (13) against interruptibility.** A sitting is one provider call and nothing can fall
  inside it. ARC-31's core need (a debate interrupted by an unrelated violent event) is met between
  sittings of a staged hearing and not within one. The first audit's reading of ARC-31 (*"yes by
  construction once a hearing spans scenes"*) holds for the staged hearing only.
- **F8 (`04` §B.2) against a room that needs every hand.** Kept: each attendee's items reach the
  room through his own filing act, and the sitting reads the case file (a World `Record`), seats and
  interiors, never a ledger.
- **No verifier (2026-08-18 Q5).** Kept: a contradiction compares two filed items; a forgery falls
  only to a finding someone made and filed.
- **`ED-SC-0038` per-matter outcomes.** One sitting tries one stage of one matter and returns one
  closing margin; a bundle is several matters on one docket (the first audit's G-25, unchanged).
- **`ED-SC-0034` (3) "pool only".** Items move the obstacle (the built placement, R-5's instance
  modifiers), not the pool; the archived *"+1D per Finding cited"* is not restored.
- **`PS/05` B.1 "there is no turn limit and there must not be".** Kept in substance: the bound is each
  attendee's own `effort`, which he chose, not a round cap.

## B5. Capability-authoring consequences

The merged surface is CORE's (`proposals/01_CORE_capability_authoring_surface.md`: a `capabilities:`
block in `references/descriptor_registry.yaml`, a `capability:` column on the verb's row, the maps
derived). CHAR's `capability_uses` table covers where a capability enters a person's own choice.
DICE's two doors are the signed `advantage_sources` channel and `POOL_ADDENDS`. This lane adds rows
to those and no table of its own, except the roster of hearing moves, which is SC's fact.

1. **Skills are rows, and the social ones are five.** `rhetoric` (argue in a room; base Presence,
   `attr.social.charisma`), `law` (argue procedure and definition, and the bench's own faculty; base
   Reason, `attr.mind.acuity`), `insight` (what a person reads of a bench; base Attunement,
   `attr.social.attunement`), `deception` (lie, and argue from an item he knows to be false; base
   Grace, `attr.social.grace`, opposed by Perception), and the existing `argue` (one-to-one
   persuasion, base Presence). Each is one line in CORE's block; none is code. The bases are
   proposed values (`grade: assumption`); the character surface may re-point any of them by editing
   the row.
2. **A move draws on a capability by declaration.** Each `hearing_moves` row carries `capability:`
   or, where the rung decides, a map from rung to capability (procedure and definition → `law`;
   fact → `rhetoric` with items doing the work; justification → `rhetoric`). The loader refuses a
   rolled move with no capability, as CORE's edit 3 refuses a contested verb with none.
3. **The four undeclared contested verbs get rows.** `determine` → `law`; `interrogate` → `inquiry`
   (SC-P7); `lie` → `deception` (this replaces SC-P7's `copying`, which made a liar's skill a
   copyist's); `arrest` stays CR-92's.
4. **Insight is a use, not a roll.** What the turn view shows of each seat's leaning is gated by an
   `at_least` row in CHAR's `capability_uses` (`use: bench_reading`, `key: insight`): below the
   threshold he sees the seats' public commits only; at it, the direction of each seat's leaning.
   This is the kernel's Appraise ladder without a second information roll.
5. **Office weight and title are FA's rows** (`06_FA_office_capabilities.md`), read by the host when
   it builds a `Seat` or a `Speaker`; R-38's "both roll and obstacle" is one score in two roles,
   which is DICE's `score()` split.
6. **Traits remain SC-P7's rows** on the signed channel; a judge unmoved by rhetoric (NPC-001) is a
   trait row with `when: {move: argue}`, `side: subject`.

Proposal: `05_SC_hearing_capabilities.md`. RPG axioms added to the first audit's §14 (d): *evidence
as an automatic modifier and argument as a test*; *a passive perception threshold*; *an opposed
social test that reads the opponent's passive score* (unchanged); *faults as conditions, not hit
points*. Still contradicted: *trained is at least as good as untrained* (CORE's and DICE's to fix).

## B6. Proposals, resolutions, and the arcs

### Proposals written by this lane (all `## Status: PROPOSED`)

| id | file under `proposals/2026-11-12-subsystem-audit-suite/proposals/` | supersedes |
|---|---|---|
| — | `05_SC_sc05_kernel_disposition_B.md` | `05_SC_sc05_kernel_retirement.md` (SC-P2) |
| — | `05_SC_playable_hearing_B.md` | `05_SC_playable_hearing.md` (SC-P3) |
| — | `05_SC_evidence_and_rebuttal_B.md` | `05_SC_evidence_and_rebuttal.md` (SC-P8) |
| — | `05_SC_obstacle_difficulty_and_modifiers_B.md` | `05_SC_opposed_obstacle_parity.md` (SC-P5, HELD BACK); carries SC-B1 |
| SC-B1 | folded into `05_SC_obstacle_difficulty_and_modifiers_B.md` ("The bound"); no separate file (G-68) | — |
| SC-B2 | `05_SC_negotiation_scene.md` | — |
| SC-B3 | `05_SC_hearing_capabilities.md` | extends SC-P7 (its edit 1 withdrawn) |

SC-P1, SC-P4, SC-P6 and SC-P7 stand, with G-55 and G-53 below as amendments for the orchestrator to
apply when it reconciles; SC-P1's `margin_endings` roster carries `terms` in place of `room` (G-61).
SC-P5 is superseded.

### Resolutions decided (continuing the first audit's numbering)

| # | what | resolution | ladder step | carried by |
|---|---|---|---|---|
| G-36 | SC-P3 puts the played hearing in the host; `ED-IN-0285` (13), (16) rule it a module container | the sitting is `social_contest.hearing`, a module entry with two modes | 1 | `playable_hearing_B` |
| G-37 | H-56's held half (a DELIBERATE nested in RESOLVE) as a blocker of the provider | not needed: deciders are called out to at ENCOUNTER; rewrite the row's held half to say so | 4 (`ED-IN-0349`) | `playable_hearing_B` |
| G-38 | audit §11 item 2 / G-24: do the Gate ratifications lapse | superseded, item by item (C-2); not a survivor | 1 | `sc05_kernel_disposition_B` |
| G-39 | SC-05: adopt the kernel, keep the roll, or retire | retire the code; implement its exchange game as the module's second entry, the roll as its closing draw | 1 + 3 + 5 | `sc05_kernel_disposition_B` |
| G-40 | which choices are verb rows and which are in-room moves | around the room: verb rows (CR-63 and its neighbours); in the room: `hearing_moves` rows | 5 | `playable_hearing_B` |
| G-41 | proofs clipped by the ceiling (F-SC-16) | the ceiling bounds the opposing score and a hostile room; what the speaker brought is subtracted after it | 3 (P4 §3.3) + 5 | `obstacle_difficulty_and_modifiers_B` (SC-B1 folded, G-68) |
| G-42 | three lanes, three shapes for cited evidence (`proofs: [{kind, ref}]`, `cites: (ids)`, an automatic count) | `cites`, ids only; the kind is derived, never stored | 4 (FI owns the carriers) | `evidence_and_rebuttal_B` |
| G-43 | the owner of "contradicts" | `_pair`'s rule (same subject and predicate, whole-value inequality), exposed once and applied by the host to filed items | 4 | `evidence_and_rebuttal_B` |
| G-44 | F8 against a room that needs each party's hand | filing is each party's own act; the room reads the case file | 3 (`04` §B.2; the SC-02 design) | `evidence_and_rebuttal_B` |
| G-45 | mirror, contradiction and corroboration as three rules | same value held by the other side: SC-02's commit mirror, unchanged; different value: an answer, the heavier stands; a second item of the same content from a distinct origin: noisy-OR, FI's ruled corroboration | 4 (`ED-IN-0322` via `08_FI_05`) | `evidence_and_rebuttal_B` |
| G-46 | the issue ladder is absent and its name is on the charge ladder | a roster `issue_rungs` (`procedure`, `fact`, `definition`, `justification`); `ladder_rungs`' note corrected | 3 (`PS/03`; P4 §3.5) | `playable_hearing_B` |
| G-47 | Layer 1's named faults have no carrier | `hearing_faults` rows, listed per arrangement | 3 (`holonic` T7) | `playable_hearing_B` |
| G-48 | who chooses for an NPC inside the room | a host-built decider over the same Candidates and the same view a player gets; no policy in the module | 4 (`PlayHost`; `dispatching_chooser`) | `playable_hearing_B` |
| G-49 | the bound on a sitting (`PS/05`: no turn limit; kernel: a budget) | the attendee's own `effort`; no engine cap | 3 (`PS/05` B.1) | `playable_hearing_B` |
| G-50 | a bench is averaged in every design on file | a `Seat` per member; a ballot per seat on `declared` rows; the determiner's own draw elsewhere | 4 (`ED-1057`'s behaviour; `declared_votes`) | `playable_hearing_B` |
| G-51 | negotiation has no played form and no draw may decide consent | the same surface under `disposal: mutual`; acceptance is the accepter's own `commit` | 3 (R-19, R-23, R-29 as recorded) | SC-B2 |
| G-52 | the social capabilities are not data | five skill rows on CORE's surface; a `capability:` per move row | 4 | SC-B3 |
| G-53 | SC-P7 maps `lie` to `copying` | `lie` → `deception` | 5 | SC-B3 |
| G-54 | the Griftlands objection was never assessed against the proceedings design | assessed (§B4.6); the constant-decider sweep is in the gate | 5 | `playable_hearing_B` |
| G-55 | SC-P6 dismisses on the first failed `determine`; P4 repair (e) holds the stage and closes it on the third | the Failure band writes a stage on the case file (SC-P6's mechanism); the count that dismisses is a row key, `ballots`, default 3; 1 reproduces SC-P6 | 3 (P4 is the batch's target specification) | amendment to SC-P6, for the orchestrator |
| G-56 | the kernel's chronicle shapes have no reader of the loop | derive them from `HearingOutcome.exchanges` in the harness; no new carrier | 4 (SC-P1's record) | `sc05_kernel_disposition_B` |
| G-57 | what the social obstacle is (flat 2 by default; the opponent's score alone where held) | the task's difficulty plus a closed, ordered roster of named modifiers, composed once in `roll.py::obstacle` | 1 (Jordan's clarification of 2026-11-12, relayed by the orchestrator; not yet ledgered) | `obstacle_difficulty_and_modifiers_B` |
| G-58 | where an act's base difficulty lives | a `difficulty:` column on the verb row naming a `difficulty_levels` member; the size in the fixture table `difficulty_ob`; values chosen to reproduce today's 2 at the control arm | 4 (CORE's `capability:` column and its loader refusal) | same |
| G-59 | the ruled `score/2`: kept, and where its divisor lives | kept whole as the `opposition` term; the divisor in `sigma_leverage.opposed_ob`, shared with combat; no social rate fixture | 1 (2026-08-14) + 4 (DICE §G edit 5) | same |
| G-60 | a hearer's regard reaches no social roll (H-267) | `regard` = −`stance_toward(counterparty, actor)` × `regard_step` (0.04; control 0), only where no bench hears; `reception` where one does, never both | 4 (`person_q.stance_toward`, the one owner) | same |
| G-61 | the reason for an obstacle is not kept | `Margin.terms`, summing exactly to `ob`, including the ceiling's clip and the floor's lift; SC-P1's roster carries it | 4 (SC-P1's Event carrier) | same |
| G-62 | how an NPC-versus-NPC contest gets its obstacle | the same host builder with no branch; every operand is read from the persons, the row and the docket | 5 | same |
| G-63 | SC-P5 (HELD BACK) and H-288 against the clarification | option B not adopted; "equal means even" and H-288 as a requirement moot; H-127 superseded; its exact-odds instrument kept | 1 | same |
| G-64 | two proposals name a roster `obstacle_terms` with different members (DICE: `[capability]`) | one roster; DICE's `capability` circumstance sum is one member; the input field is `capability_terms` | 4 | same |
| G-65 | FI's E-6 enters and strikes evidence only at the citing `speak`'s Success; the sitting's `present` and `answer` are draw-free | deterministic entering and standing in the room and out of it; the verdict stays a draw; FI's file to be reconciled by the orchestrator | 5 | `evidence_and_rebuttal_B` |
| G-66 | the module cannot import the owner of "contradicts" | `decision/options.py::contradicts`, exposed once from `_pair`'s rule; the host hands each exhibit its `pairs` as data | 4 | `evidence_and_rebuttal_B` |
| G-67 | CORE's edit 8 (`lie` → `copying`, `determine` → `argue`) against `deception` and `law` | sequenced: CORE's values ship first (no new rows); SC-B3 re-points one cell each when its four rows land | 5 | SC-B3 |
| G-68 | SC-B1 would restate the bound the obstacle proposal must decide anyway | folded: one proposal owns the bound order | 5 | `obstacle_difficulty_and_modifiers_B` |

Resolutions decided in this addendum: **33** (G-36 to G-68). None survives to Jordan. One first-audit
survivor is withdrawn (G-24, by G-38), and the other, H-288 (SC-P5), is answered by Jordan's
clarification of the obstacle (G-63): **the lane has no survivor**.

### Provided arcs and characters — what changes in the first audit's §13

| case | need | first audit | after this addendum |
|---|---|---|---|
| ARC-10 | explosive tangential evidence mid-contest, for a benefit and a wider cost | SC-P3 edit 2 | a late filing (the same round as the sitting, so the other side has no round to answer) presented in the room; the wider cost is the told deposit of a cited item (`08_FI_05`) |
| ARC-42 | cite an established, verifiable fact as a distinct move; an insider's testimony weighs more | SC-P3, SC-P7 | `present` of a `record`; weight by remove and origin (`evidence_and_rebuttal_B`) |
| NPC-085 | citing precedent improves the odds | waits on CR-36/37 | unchanged dependency; the `resolution` Record is then an admitted `record` |
| NPC-001 | unmoved by rhetoric, moved by evidence | SC-P7 | a trait row on `argue`; items are deterministic, so evidence moves him by construction |
| NPC-071 | appeal to rule against appeal to circumstance | SC-P7 | the rung argued (`definition` against `justification`) and a trait row keyed on it |
| EMG-X6 | an asymmetric proceeding | SC-P4 | the row's `bears:`, `admits:`, disclosure and counsel keys gain their reader in the sitting |
| EMG-C4 | a champion substituted mid-contest | SC-P3 | an advocate is a `Speaker` on the party's side; substitution falls between sittings |
| ARC-31 | a debate interrupted by violence | "yes by construction" | between sittings only (§B4.7); stated as a limit |
| SCN-04 | a stress resource with stacking penalties | design-first | the level a failed `impugn` or a fault puts against a speaker for the sitting, on DICE's signed channel; no stored resource (`ED-SC-0035` kept) |

Dependency edges added: SC ← FI (`cites`, the told deposit, a finding that names a Record forged);
SC ← CORE (the `capabilities:` block and the verb column); SC ← DICE (the signed advantage channel);
SC ← CORE (a prize row `step: ENCOUNTER` for the hearing, REM-31's precedent).

## B7. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/SC_B/`.

| # | command or probe | seed | outcome |
|---|---|---|---|
| 1 | `kernel_probes.txt`: signatures of `build_contest` / `resolve_contest`; `hard` against `advance` at one seed; the global stream across one `resolve_contest`; non-comment lines of `K/resolver.py` naming "doubt"; the logos policy against each of eleven policies at three venues | 0–399 (F9); 123; 7 (600 bouts per cell) | no `armature` or `rng` parameter; same gain 400 of 400, reserve 9 against 7; stream moved, return `('committee','win')`; 0 lines; court 0.83–1.00, disputation 0.71–1.00, assembly 0.01 against the pathos policy. One seed per venue: counts, not rates |
| 2 | `agon_harness` under a scripted stdin answering 1, 2, 3, 9 to every prompt (`agon_all_*.txt`) | none (the harness seeds nothing) | exit 0 each; decisive win in 3 exchanges (9 prompts); loss by barred-device clinch in 1 exchange; compromise; decisive win after 135 prompts (invalid answers default to option 1). Single observations |
| 3 | `live_roll_odds.txt`: `modules.social_contest.roll.obstacle` and `sigma_leverage.band_odds` over pools 2, 5, 8 × opposition none, 4, 8 × proofs 0, 1, 2, 4, per-pool ceiling arm, `proof_step` 0.25 | exact, no draw | the tables in F-SC-16. The probe's `reception_gain` was planted at 0.25 with `reception` 0, so it does not enter any row; shipped is 1.0 |
| 4 | shipped fixture values by reading `es/data/fixtures.py` at the lines found (`scene_budget` 5, `interactions_per_scene` 3, `extended_scene_cost` 2, `contest_max_depth` 2, `proof_step` 0.25, `reception_gain` 1.0, `obstacle_ceiling` 2, `ceiling_per_pool` True, `bench_quorum` 1, `docket_lapse` 4) | — | read, not run; a first attempt to read them through `Fixtures()` failed (`Ungraded`: an unregistered bare instance), caught from the output |
| 5 | search of `registers/*.jsonl`, `registers/handoffs/*.md`, `workplans/*.md`, `references/*.md` for three phrases of R-32, R-33 and R-40 | — | no file |
| 6 | `git status --short` | — | this lane's files are untracked additions under `proposals/2026-11-12-subsystem-audit-suite/`; other lanes' files in the same directory are modified by them; nothing outside it |
| 7 | `difficulty_odds.txt`: exact `band_odds` for `Ob = difficulty + opposition/2`, no ceiling, floor `OB_MIN` 1, pools 2, 3, 5, 8, 12 × difficulty 0, 0.5, 1, 2, 3 × opposition none, equal, double; and one 0.5-step of favour at an equal pair with difficulty 1 | exact, no draw | pool 2, difficulty 1, opposition 2: Ob 2.0, Failure 0.74 (today's default pair reproduced); equal pairs at difficulty 1 fail 0.74, 0.71, 0.71, 0.72, 0.73 at pools 2, 3, 5, 8, 12; one obstacle unit of favour brings them to 0.42, 0.51, 0.56, 0.61 at 2, 5, 8, 12; unopposed at difficulty 0 hits the floor (pool 5 Failure 0.20) |
| 8 | (completion pass) the ten social verb rows parsed from `verb_table.yaml` for `contests`, `counterparty`, `requires_typed`; `sigma.py::contest_input` read at `:199-212` | — | `speak` has no `counterparty:` and its subject is a `DocketItem`; `interrogate`, `determine`, `arrest` take `counterparty: subject` (a person); `tell`, `lie`, `argue` take `to`. So the obstacle proposal's first values (`speak` routine, `interrogate` demanding) would have moved every `speak` 2 → 1 and every `interrogate` 2 → 3 at the control arm; corrected in that file and recorded there |
| 9 | (completion pass) `person_q.py::stance_toward` read at `:73-82` | — | Σ valence × weight, each row up to ±25; the first `regard_step` (0.2 per valence point) would have let one row move an obstacle by 5; corrected to 0.04 on `stance_toward`'s own scale |
| 10 | (completion pass) `git status --short` | — | changes by this lane: the addendum and seven proposal files, all untracked additions under `proposals/2026-11-12-subsystem-audit-suite/`; nothing tracked edited by it |

Not run: `pytest` (by instruction); `aperture`, `corpus_run` and the realm probes (the first audit's
readings are used); the three-lens audit's `opponent_is_adjudicator` grep (taken from `3L/00` §1,
not re-run).

## B8. The social obstacle: the task's difficulty and its modifiers (decision-ready)

Jordan's clarification, relayed by the orchestrator on 2026-11-12: *the social-contest obstacle is
the difficulty of the task plus all associated modifiers; not a flat 2, and not the opponent's score
alone.* This lane has not found it in a ledger; recording it is the orchestrator's. The full
specification, with edits by owner, gate and falsifier, is
`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`; this section is the decision an
implementation lane needs, in one place.

**The form.** `Ob = bound(difficulty + opposition + standard + subject + stakes + hostile halves)
− favourable halves`, floored at `OB_MIN` (1). The bound is the existing ceiling rule (H-213); the
favourable halves are subtracted after it so that what a speaker brings is never clipped (F-SC-16,
G-41). One composer: `modules/social_contest/roll.py::obstacle`. Leverage (effort, wounds, traits)
stays a μ-shift on the roll, not an obstacle term.

**Base difficulty: which registry, which keys.** `engine/season/verb_table.yaml`, a `difficulty:`
column on every contested or graded row (the loader refuses its absence, as CORE's `capability:`
column); its value is a member of `rosters.yaml: difficulty_levels` (`plain`, `routine`, `demanding`,
`hard`); the sizes (0, 1, 2, 3) are the fixture table `difficulty_ob`. Proposed values reproduce
today's obstacle of 2 at the control arm: rows with a person counterparty (`tell`, `lie`, `argue`,
`determine`, `arrest`, `interrogate`) `routine`, since a person without a score opposes at
`opposed_ob(pool_default)` = 1; rows with none (`speak`, whose subject is a `DocketItem`; `research`,
`examine`, `surveil`) `demanding`.

**The named modifiers, with units** (closed, ordered roster `rosters.yaml: obstacle_terms`; every
term in obstacle units, net successes):

| term | value | applies to |
|---|---|---|
| `opposition` | the counterparty's score (DICE's `score()`) ÷ 2, by `sigma_leverage.opposed_ob` — the 2026-08-14 ruling, kept as one modifier | a person counterparty that is not the actor |
| `standard` | the room's level (`difficulty_levels`) from a `standard:` key on the docketed arrangement row or rite; `plain` on every seeded row | bench-heard acts |
| `subject` | the examined Record's `forgery_quality` (today's operand) | graded inquiries |
| `stakes` | `stakes_ob[kind]` for the Tenure the act opens or closes (proposed `oblige` 0, `detain` 0.5, `ban` 1) | acts that restrain the counterparty |
| `regard` | −`stance_toward(counterparty, actor)` × `regard_step` (0.04; control 0) | one person counterparty, no bench |
| `reception` | the bench's reception × `reception_gain` (1.0), as SC-02 re-sources it | bench-heard acts, never with `regard` |
| `capability` | DICE's `circumstance` rows of `capability_uses`, summed host-side | as each row's `when:` |
| `evidence` | `proof_step` (0.25) × (standing items against the actor's side − standing items for it), by `05_SC_evidence_and_rebuttal_B.md`'s `standing` | acts whose row admits `cites` |
| `plea` | CR-62's `plea_step` | `speak` |

**How the reason is read.** `Margin` gains `terms: ((name, value), …)` in roster order, plus
`("ceiling", −clip)` and `("floor", +lift)` where a bound acted, summing exactly to `ob`;
`sigma.resolve` copies it; SC-P1's `margin_endings` carries it on the Event, so the log and a saved
game say *Ob 3.5 = difficulty 1 + opposition 2.5 + stakes 0.5 − regard 0.4 − evidence 0.5*. Person-side,
`believed_input` knows the public terms (`difficulty`, `standard`, `stakes`) and fills the rest from
his claims or leaves them unknown (DICE's believed-odds prior).

**NPC against NPC.** No branch: the same builder reads the row, the counterparty's score and stance,
the docket, and the actor's filings. Where each side wants to move the other, each makes its own act
with its own obstacle; there is no shared roll.

**SC-P5 (HELD BACK).** Survives: H-127's inversion is removed (a person without a score is not the
`obstacle_default` stand-in), and its exact-odds tables as the instrument. Moot: option B as a
pending question (the divisor stays the ruled one, in its one owner), "equal parties should be even"
as a target, and H-288 as a survivor for Jordan. Measured (run 7): with difficulty 1, equal pairs
fail 0.71 to 0.74 at every pool from 2 to 12, so the rising disadvantage SC-P5 measured (0.42 to
0.61) is flattened by the base; one unit of favour brings them to 0.42 to 0.61.
