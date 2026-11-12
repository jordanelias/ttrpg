# SC-05 decided on the full evidence: retire the kernel's code, carry its exchange game as the module's second entry

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-09) — three checks in the carry table (rebuttal, defeat by named fault, who bears the question) asserted a fixed outcome; each now asserts a share over seeds, as the sweep's D-01 and D-03 already made the mechanisms they test (`05_SC_evidence_and_rebuttal_B.md` rule 2; `05_SC_playable_hearing_B.md`: silence adds levels and concedes nothing). The carry list and the retirement are unchanged.

## Status: PROPOSED — supersedes `05_SC_sc05_kernel_retirement.md` (SC-P2), which it keeps in every edit it does not restate

Source: `audits/05_SC_audit_addendum_B.md` §B2 (C-2, C-3, F-SC-18), §B3; `audits/05_SC_audit.md`
F-SC-02. Executes `ED-SC-0033` clause 2 (RULED: *"orphaned social contest code: retire it"*) and
`ED-IN-0285` statements 11, 13 and 16 (RULED: the social contest is a module container with an
automated and a playable mode). Carries `workplans/valoria_master_workplan_v11_part5.md` SC-05.

## What it changes in `engine/season/` at runtime

Nothing by itself. The deletion is unreachable code (hash EQUAL). What it changes is what the
deletion waits for and what must exist before it: SC-P2 waited for a season fixture with a player
callback; this waits for `social_contest.hearing`, the module's second entry
(`05_SC_playable_hearing_B.md`), and for one check per carried mechanism.

## The problem (evidence)

SC-P2's seven points stand (two owners; four test importers; the entry has no generator, moves the
global stream and returns a winner; the plan's carried block describes an extension path the loop
never had; the stale registry row; 31 exported parameters; the only played mode lives in the
kernel). Three things it did not have:

1. **Its replacement was specified against a ruling.** SC-P2's order is *"after SC-P3's `hearing`
   entry and its play harness are green"*, and SC-P3 is the season loop on a fixture. `ED-IN-0285`
   (13): *"social contests occur within their own Godot container, ie they are their own unique game
   state that does not occur on overview/season loop … when non-player social contests occur, they
   will be routed through an automated resolution in the module that does not call forward a playable
   scene"*. The replacement of a played kernel is a played module mode.
2. **Its carry list is four items; the kernel has eleven the loop lacks** (addendum §B3, table),
   among them the two Layer 1 itself names for the argument layer: resolution by named fault
   (`holonic_ARCHITECTURE.md` §2, T7) and the issue ladder (§54.3). The Proceedings design's own
   provider (`PS/19_PLAN.md` step 14, `21_RECONCILIATION.md` step 15: a nested run with in-run
   aggregates, unbuilt) is the same object under another name.
3. **Its "not carried" list leaves a question for Jordan that the ladder answers.** Audit §11 item 2
   asks whether the Gate ratifications lapse. They do, item by item (below), by rulings later than
   they are.

Measured for this proposal (`runs/SC_B/kernel_probes.txt`, addendum §B7 run 1): `build_contest` has
no `armature` parameter and `resolve_contest` no `rng`; one `resolve_contest` call moves the global
`random` stream and returns `('committee', 'win')`; `hard` and `advance` give the same gain at the
same seed in 400 of 400 with `hard` costing two more; no non-comment line of `resolver.py` names the
Doubt Marker; a policy that plays the venue's home appeal every turn wins 0.71 to 1.00 against every
other scripted policy at `court` and `disputation` (seed 7, 600 bouts per cell; one seed, so counts).

## The resolution, decided

**Retire `systems/social_contest/sim/contest/` whole, as code. Carry its exchange game as the
specification of `modules/social_contest/hearing.py`, re-derived on the loop's owners (typed input,
a seeded generator passed in, margins out, no state between calls), with today's `roll` as the
sitting's closing draw.** "Adopt" (Jordan's indirect lean, A1-58) and "retire" (`ED-SC-0033`) are
both met: the design is adopted, the code is retired. `ED-SC-0013`'s sentence (*"auto = the contest
kernel run headless, played = the same kernel run interactively"*) becomes literally true of the
module.

Ladder: step 1 (`ED-SC-0033`, `ED-IN-0285`, `ED-SC-0013`); step 3 (`PS/05` PART B and `19_PLAN` step
14 already design the provider as a run of exchanges that never writes); step 4 (REM-31 and
`ED-IN-0349`: the suspension shape exists for combat); step 5 (the roll as the degenerate sitting is
what makes it one path). Nothing here is Jordan's to answer.

### What is carried, where, and the check that shows it arrived

| mechanism | kernel source | home | check (one test each, `engine/season/tests/test_sc_hearing_*.py`) |
|---|---|---|---|
| a run of exchanges, one move each | `Bout.resolve` | `hearing.py::hear` | two scripted deciders that differ in one move leave different standing sets |
| the issue ladder and descent | `Stasis`, `shift` | roster `issue_rungs`; the case file's stage | a `concede` moves the tried rung one step and is witnessed |
| held evidence: relevance, weight, diminishing corroboration | `Dossier`, `EvidenceItem` | `05_SC_evidence_and_rebuttal_B.md` | an item off the live rung enters at half; a second item of one origin adds less than the first |
| rebuttal that removes a standing point | `rebut` | the `answer` move | over 200 seeds an `answer` strikes the item in a share strictly between 0 and 1; a struck item adds no `proofs` level to the closing draw and a standing one does |
| defeat by named fault, per venue | `DefeatCatalogue` | roster `hearing_faults`, the row's `faults:` | a row with `silence` in its list adds levels against a resting bearer in the closing draw and a row without adds none; in neither is the rung conceded without the draw |
| who bears the question | `ProofBar`, `GraceThreshold` | the row's `bears:` | swapping `bears:` on one hand-built world moves the closing draw's odds toward the other side over 200 seeds; no single result is fixed by the swap |
| a ballot per seat that can cross the room | `VoteAtClose`, `ED-1057` | `HearingOutcome.ballots` on `declared` rows | a seeded bench where the board favours one side and one seat votes the other |
| what moves this judge, read in bands | `armature.py`, `appraise.py` | SC-P7 trait rows; the turn view's `insight` gate | a trait row changes one seat's ballot odds and no other's |
| effort as the attendee's budget | `Reserve` | `Act.effort` | an attendee at effort 0 makes no move |
| the run's shape (rout, reversal, collapse, split) | `narrative.py` | a reader of `HearingOutcome.exchanges` in the harness | the four shapes are each produced by a hand-built exchange list |

`Pressure` is carried as an idea only (its source is the bench's public commits, SC-02's term, and
FA's legitimacy): no check here.

### What is dead (evidence in addendum §B3)

The seven-verb menu, `hard`, `SelfGating`; Style, genre, orientation, CR4's bonus die and
`INTERACTIONS_TABLE`; the Doubt Marker; `FaceScale`, `Contestant.charisma`, `split_standing`,
audience resistance; `faction.py`; `policy.py`; the thirteen venue presets, `RhetoricalWeights` and
the adjudicator profiles; `GAMES`, `MECHANICS`, the design-memo dictionaries, `_kernel_tests.py`;
`degree_extension.py::PoolDesaturation`.

### The Gate ratifications, closed by the ladder (replaces audit §11 item 2)

| ledger id | what it ratified for the kernel | disposition | by |
|---|---|---|---|
| `ED-1056` | Face scale-binding (`Charisma × 3`) | lapses; unreachable through the public entry (`_as_contestant` never sets `charisma`) | step 2 |
| `ED-1057` | a bench ballot weighted by standing | behaviour carried (per-seat ballot, office weight) | step 1 (the later statement that office weight enters roll and obstacle, R-38 as recorded in `PD/…primitives-and-kinds.md`) |
| `ED-1059` | Guild Arbitration heard by a panel | a row's data, if such a row is authored | step 3 (`arrangements.yaml` is the owner) |
| `ED-1060` | Terminal Doubt | lapses; never consumed by any resolver line | step 2 |
| `ED-1061` | the Guilds boost derives from the venue, not a GM | the principle is the no-GM rule; the table dies | step 1 |
| `ED-1062` | the armature's fourth axis; the two-genre compression; CR5's scope | the armature survives as seat leanings in trait rows; genre and CR5 die with the Style grid | step 1 (the 2026-09-05 scope ruling; `ED-SC-0033`) |

## Exact edits, by owner

SC-P2's edits 1 to 6 stand (the `git rm`, the three test repoints to a local `BandExtension` double,
the `module_contracts.yaml` row, `sim_params.json` re-derived by its exporter, the SC-05 block's
struck clauses, the handoff and `CURRENT.md` rows). Changed or added:

1. **Order.** After `05_SC_playable_hearing_B.md`'s entry and its `--play` gate are green, and after
   the ten checks above pass. B10-18c's order (CR-60 to CR-62 first) is unchanged.
2. `references/module_contracts.yaml` `composition_roles`: a second row, `social_contest.hearing`
   (`entry: verb_call`), added by the hearing proposal, is what the retiring `module: social_contest`
   row's `sim_module:` and `resolver:` describe after the repoint.
3. `workplans/valoria_master_workplan_v11_part5.md` SC-05, ASKS ATTACHED: replace *"adopt the kernel
   as the social contest scene's automated mode now … or keep the interim provider"* with *"decided:
   the kernel's code retires; its exchange game is the module's `hearing` entry; the roll is that
   entry's closing draw"*, citing this file.
4. `registers/editorial_ledger_sc.jsonl`: one row recording the table above for `ED-1056` to
   `ED-1062` (superseded for the kernel, with the two carried behaviours named). An orchestrator
   edit; this lane writes no ledger.
5. `engine/season/hole_register.yaml` H-56: the held half is rewritten to *"not required by a
   hearing: its deciders are called out to at ENCOUNTER (`ED-IN-0349`); open only for a contest that
   would re-run DELIBERATE"*.

## Gate (execution artifact)

- SC-P2's: one-season content hashes of `headless --case NPC-088 --seasons 2 --seed 0` and
  `build_realm(0)` equal before and after the deletion; `tools/export_sim_params.py --check` and
  `tools/freshness_gate.py` green.
- The ten checks in the carry table green on the commit before the deletion.
- `python -m engine.season.harness.headless --world hearing --play <id>` exits 0 on a scripted
  stdin, on the commit before the deletion (the played mode has moved before its old host goes).

## Falsifier

If a content hash moves on the deletion, something reached the kernel: stop and find the importer.
If any of the ten checks cannot be written against `HearingOutcome` (the field it would read does not
exist), that mechanism was not carried and the deletion waits.

## NERS reading

- **N**: the kernel holds in one direction only (a human at a terminal); cut, nothing the season can
  reach is lost once the sitting exists. What N protects is the carry list, and each row has a check.
- **R**: completeness — one roster of proceedings, one obstacle, one played mode; the no-player half
  gains the same sitting (NPC deciders).
- **S**: removes the second ladder for one quantity (two obstacle sites, two ballots, two evidence
  models) and the second played path.
- **E**, last: about 6,700 lines, 389 script checks and 31 exported parameters out; one module file
  and three rosters in, against eleven mechanisms kept.

## Cost class

Small build (a deletion wave with registry repoints), after a small build it depends on. Cross-lane
on `references/` and the ledger.
