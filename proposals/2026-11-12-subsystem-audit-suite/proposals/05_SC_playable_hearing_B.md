# The hearing as the social-contest module's scene: a sitting of exchanges whose closing draw is today's roll

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-02, D-03 — `answer` is now a rolled move with graded board effects; `silence` adds levels to the closing draw instead of conceding the rung; `forgery_found` only on an Overwhelming answer; D-06 — the NPC decider samples through the one chooser's sampler instead of taking the top score.

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-04) — edit 4's assumption (*`PlayHost.decide` is called with whichever view the provider builds*) is replaced by the one `PlayHost` shape of `01_CORE_one_scene_contract.md` Edit 1: `deciders` keyed by module role, so the hearing's decider is `deciders["social_contest.hearing"]` and the stated revert (a second field) is not needed.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-11, C-25) — the ballot has one owner, this file's `HearingOutcome.ballots` at the hearing's close: each seat's ballot is a draw on that voter (Jordan, A-14), his public commits entering as `lean` levels, and the host's `vote` conjunct is deleted (`U5c_SC_proceedings_residue.md` §6; `13_SC_draw_for_unrolled_contests.md` edits 3 and 4 yield). `determine` names the prize `a verdict` (entry `social_contest.hearing`, fought at ENCOUNTER; `U5c_VERBS_residue_and_governance_owner.md` §2).

Folded: 2026-11-12 by `audits/28_SCENE_ACCESS.md` (rulings A-63, A-64). Nothing here is deleted; the sitting's attendees are no longer assumed free. (1) **A sitting seats those who move in it.** When `social_contest.hearing` runs at ENCOUNTER, each attendee who makes a move is engaged in the sitting for that round by the read that engages a visit's counterparty, and the sitting counts as a scene received in his budget Query; an attendee already engaged in another scene that round is absent, and this file's own `silence` rule (levels on the closing draw) applies to his side (`28_CORE_scene_access_A_occupancy_and_precedence.md` §2, §3). The host builds the attendees from that read; the module is not edited and holds no state. `[UNVERIFIED: how `HearingInput` lists attendees was not opened at the field; the statement binds the host-side builder, whichever shape it has.]` (2) **The petitioner's side may carry `waiting` levels** in the closing draw, one per rebuff the log records of the petition behind the matter, through the one leverage form (`28_CORE_scene_access_C_the_petition_that_waits.md` §2).

## Status: PROPOSED — supersedes `05_SC_playable_hearing.md` (SC-P3). Design-first for edits 6 and 8; the rest are small builds.

Source: `audits/05_SC_audit_addendum_B.md` §B2 (F-SC-15, F-SC-17, F-SC-20), §B3, §B4;
`audits/05_SC_audit.md` F-SC-01, F-SC-05, F-SC-07. Kept from SC-P3: the fixture, the case file as
the hearing's persistent record, a filing that writes (so the chooser prices it), choices as
Candidates. Changed: where the played game lives.

## What it changes in `engine/season/` at runtime

With the new fixture `sitting_exchanges` at its control (0) and nothing filed: nothing; a `determine`
is the single draw it is today, through the same `roll`. At the shipped arm a `determine` on a
docketed matter is deferred to ENCOUNTER (as `fight` and `march` are) and resolved by a new module
entry, `social_contest.hearing`: the attendees exchange moves over the items filed on the case file,
then the determiner's draw reads what is left standing. A declared mover wherever a `determine`
executes with items on file.

## The problem (evidence)

- **A ruling places the played contest in the module** (`ED-IN-0285`, 13 and 16; addendum C-1), and
  the suspension that serves it is ratified and built for combat (`ED-IN-0349`, REM-31:
  `queries/inputs.py::PlayHost`; `loop/driver.py::season(..., host=)` threads it to ENCOUNTER only).
  `seam/wrappers/sigma.py::resolve` accepts `host` and ignores it (`:459-460`).
- **Nothing is decided inside a social contest** (first audit F-SC-07) and the plan's target
  specification concedes the cost: P4 §9, *"speech kinds differ by hundredths of a sentence in the
  pool grid"*; its critic finds about five robust choices, all made outside the room.
- **Layer 1's argument layer is absent**: no named fault, no issue ladder (F-SC-17).
- **The design the code itself points at was never built**: `world_q.proofs`' docstring, *"the
  design spends proofs one at a time inside a nested run (`21_RECONCILIATION.md` step 15, unbuilt),
  which is where hoarding one becomes a choice"*.
- **The kernel's menu must not be what is carried**: a constant policy solves it (F-SC-18).

## The resolution, decided

**Around the room, verb rows (the plan's). In the room, one module entry with two modes. One closing
draw, the existing `roll`, by the determiner.** Ladder: step 1 (`ED-IN-0285`, `ED-SC-0013`); step 3
(`PS/05` PART B; `holonic` T7 and §39); step 4 (REM-31); step 5 (the roll as the sitting with no
exchanges).

### The module's interface (structure; `queries/inputs.py` holds the records, as for every module)

```python
@dataclass(frozen=True)
class Exhibit:                 # one item on the case file (see 05_SC_evidence_and_rebuttal_B.md)
    id: str; side: str         # "for" | "against" the party
    kind: str                  # a `rosters.yaml: proofs` member, derived at filing
    rung: str                  # the `issue_rungs` member it bears on
    cell: tuple                # (subject, predicate, value) as filed
    weight: float; origin: str # weight by remove and hops; origin = the root of its chain
    forged_found: bool         # a filed finding names this Record forged

@dataclass(frozen=True)
class Speaker:                 # a party or an advocate
    id: str; side: str
    pools: tuple               # ((capability id, dice), ...) from the one pool reader
    score: float               # what the other side halves (R-5's form)
    effort: int                # exchanges he will spend: his own act's `effort`
    levels: tuple              # (for, against): named sigma levels from the advantage roster

@dataclass(frozen=True)
class Seat:                    # one bench member
    id: str; pool: int; weight: float   # office weight (FA's row)
    lean: float                # his public commits about the party (SC-02's commit term), signed

@dataclass(frozen=True)
class HearingInput:
    closing: SocialContestInput        # today's record for the determiner's draw, unchanged
    rung: str; bears: str              # the stage tried, and which side bears it
    speakers: tuple; bench: tuple; exhibits: tuple
    moves: tuple; faults: tuple; admits: tuple; order: str    # the row's data
    proof_step: float; argument_step: float; fault_step: float

@dataclass(frozen=True)
class HearingTurnView:         # the one record handed outward, to a decider
    n: int; mover: str; rung: str
    board: tuple               # standing and struck exhibits, as the row discloses them
    hand: tuple                # the mover's own unplayed exhibits
    effort_left: int; legal: tuple     # moves the module will accept

@dataclass(frozen=True)
class Exchange:
    n: int; mover: str; move: str; exhibit: Optional[str]; target: Optional[str]
    margin: Optional[Margin]; entered: tuple; struck: tuple; fault: Optional[str]

@dataclass(frozen=True)
class HearingOutcome:
    exchanges: tuple; standing: tuple; faults: tuple; rung: str
    margin: Margin             # the closing draw: a margin, never a winner
    ballots: tuple             # ((seat id, Margin), ...) on a `declared` row, else ()

def hear(inp: HearingInput, rng, decide: Callable[[HearingTurnView], tuple]) -> HearingOutcome: ...
def closing_odds(inp: HearingInput, standing: tuple) -> tuple: ...     # pure; exact, no draw
```

No `World`, no token, no state between calls; the generator is a parameter; the module grades its
own in-run draws by calling the one ladder owner (`degree_from_net`) and returns margins.

### The six moves (data: a roster `hearing_moves`, one row each; the arrangement's rite lists those it admits)

| move | needs | draw | board effect by outcome |
|---|---|---|---|
| `present` | an unplayed exhibit of his side, of an admitted kind | none | stands on the tried rung at `weight`; on another rung, at half (the `irrelevance` fault counts it) |
| `answer` | an exhibit whose `cell` contradicts a standing one, or a filed finding that the target is forged | one `roll`: the mover's `speak` pool against `answer_ob + proof_step × (w_target − w_answer)` (impeachment: `− finding confidence`), plus the room's modifiers | per `05_SC_evidence_and_rebuttal_B.md` `standing` rules 1–2: Failure the target stands; Partial both halved; Success the target struck; Overwhelming struck, and on a forgery every exhibit of its origin with `forgery_found` |
| `argue` | — | one `roll`, his `capability` for the rung against the other side's `score` | Overwhelming or Success: an argument stands (`argument_step`); Partial: half, and a subsidiary matter is named for the docket; Failure: nothing |
| `impugn` | a filed deed-claim about the person an opposing exhibit originates from | one `roll` | Success or better: every exhibit of that origin halved; Failure: a level against the mover for the sitting |
| `concede` | — | none | the rung descends one step; the mover's exhibits on the conceded rung leave the board |
| `rest` | — | none | nothing; all resting in turn closes the sitting |

A bench member's moves are `rule` (close now) and `adjourn` (hold the stage to the next sitting).

### Faults (data: a roster `hearing_faults`; the rite lists those that apply)

`self_contradiction` (two standing exhibits of one side disagree: the lighter is struck, one level
against that side); `silence` (the bearing side rests with nothing standing on the rung, or the other
side rests under an unanswered standing exhibit: two levels against that side on the closing draw,
never an automatic concession — the bench may still find for a silent party, at long odds);
`forgery_found` (recorded only by an `answer` graded Overwhelming: every exhibit of the forged Record's
origin is struck); `irrelevance` (the rite may set a strike count
after which further off-rung items do not enter). Each is a condition on the typed board. None names
a winner.

### How a sitting runs

1. Order the attendees by the row's `order`. 2. For the mover: build the view, call `decide`, apply
the move's row, check faults, record the `Exchange`. 3. Stop when all rest in turn, when no attendee
has effort left, or when the ladder cannot descend. 4. The closing draw: `roll(closing', rng)`, where
`closing'` is `inp.closing` with its room term set from the board (`proof_step` × the net standing
weight, signed by side, plus `fault_step` per fault), composed by `roll.py::obstacle`, the one owner.
On a `declared` row each `Seat` is balloted with its own pool, weight and lean. With no exhibits and
no effort, steps 1 to 3 do nothing and step 4 is today's draw.

### Who decides

`decide` is one callable for every attendee. The host adapter builds it: for a person in
`PlayHost.persons`, the host's callback; for anyone else, a decider built from that person's own
interior (owner: `decision/`, CHAR's lane). The NPC decider treats each legal move as a Candidate and
scores it with the chooser's own terms: the believed verdict after the move (`closing_odds` on the
board the move would leave, weighed by what each band's disposal means to him), less the move's
cost in his own terms (an item exposed, an enemy made, a concession witnessed, effort). It reads the
person and the view; it is handed no `World` and writes nothing, the convention REM-31 states for a
combat decider. *(Reconciled, D-06: it does not take the top score.)* It picks by the one chooser's
sampler (`decision/choose.py::_sample_order`, `softmax(score / choice_temperature)`), on a keyed
stream the host hands it (`draw_factory(seed, tick)(person, f"hearing:{matter}:{n}")`), so what an
NPC does in the room is a draw whose odds his interior sets, never a fixed function of the board.

## Exact edits, by owner

1. `engine/season/rosters.yaml`: rosters `issue_rungs` (`procedure`, `fact`, `definition`,
   `justification`), `hearing_moves`, `hearing_faults`; the note on `ladder_rungs` corrected to
   *the charge ladder (Fig. 27)*; prize row `a matter` gains `module_entry: social_contest.hearing`,
   `step: "ENCOUNTER"`, `declares: "Declared"` (`the body`'s and `a field`'s pair).
2. `engine/season/verb_table.yaml`: `determine` contests `a matter` (CP-T05-01 already moves its
   prize to a bench-heard one) and gains `Declared` cells (`writes: []`), on `march`'s precedent;
   its four bands are unchanged. `speak` stays an undeferred single draw (`social_contest.roll`):
   it is the filing act (`05_SC_evidence_and_rebuttal_B.md`).
3. The rite block CR-60 lands (`arrangements.yaml: rites`): keys `bears:` (rung → side), `moves:`,
   `faults:`, `disclosed:` (whether the other side's filings are on the mover's board). Until CR-60,
   one default rite carries them.
4. `engine/season/queries/inputs.py`: the records above. `PlayHost.decide` is called with whichever
   view the provider builds `[ASSUMPTION; medium; revert: a second field, `decide_hearing`]`.
5. `modules/social_contest/hearing.py`: `hear`, `closing_odds`. `references/module_contracts.yaml`
   `composition_roles`: `social_contest.hearing`, `entry: verb_call`.
6. `engine/season/seam/wrappers/sigma.py`: `hearing_input(w, act)` (the host builder: the case file's
   stages → exhibits; `judging_set` → seats; `faculty` and `_opposition_of` → speakers; SC-02's commit
   term → `lean`) and a `@provider("contest", …)` path that calls the entry with the dispatching
   decider. It reads the case file, seats and interiors; no ledger (F8).
7. `engine/season/loop/effects_information.py::_eff_determine`: under its own token, append the
   exchange list to the case file (`Record.stages`: one stage per entered, struck or conceded item)
   and carry it on the Event's `ending` (SC-P1's carrier), so the sitting is witnessed and saved.
8. `engine/season/decision/`: the NPC decider (CHAR's file; SC states the interface above).
9. `engine/season/harness/governance_spine.py::build_hearing(seed)` (SC-P3's fixture, plus three
   filed items per side) and `harness/headless.py --world hearing [--play <id>]`.
10. `engine/season/data/fixtures.py`: `sitting_exchanges` (0 control / shipped: the attendees'
    effort), `argument_step`, `fault_step`, each with a NUMBER row and a three-point sweep.

## What a player sees

On entry: the arrangement, the rung tried and who bears it, the disposal each band opens (the
stakes), his own filed items, the bench's public commits about each party. Each turn: the board, his
hand, his effort, the legal moves, and his believed chance of the verdict in the words the first
audit's G-34 decided (what his character believes, never the room's truth). What he sees of each
seat's leaning is gated by `insight` (`05_SC_hearing_capabilities.md`). Afterwards: the Events he
witnessed, and the roll of his own act (SC-P1).

## Gate (execution artifacts)

1. `hear` with no exhibits and effort 0 returns exactly `roll(inp.closing, rng)`'s margin for the
   same generator (unit), and `build_realm` hashes at seeds 0 to 2 are EQUAL at `sitting_exchanges` 0.
2. `PYTHONHASHSEED=0 python -m engine.season.harness.headless --world hearing --seed 0 --auto`,
   twice: identical content hash; the log holds a `matter.determined` whose `ending` lists exchanges.
3. The same with `--play` and two scripted stdins that differ in the first move: different standing
   sets and a different closing obstacle.
4. Parity: a scripted player that returns the NPC decider's own pick each turn reproduces the
   `--auto` hash (REM-31's shape: the mode is recorded nowhere).
5. The stationary-menu run: three constant deciders (always the heaviest `present`, always `argue`,
   always `rest`) against the chooser's decider over 200 seeded sittings on each of three hands.

## Falsifier

If one constant decider obtains the best verdict share on all three hands in run 5, the menu is
stationary and the design fails as the kernel's did. If run 3's two scripts leave the same closing
obstacle, the moves are not load-bearing. If run 4's hashes differ, there are two code paths. If a
fault can be shown to fix the band (a hand-built board on which the closing draw cannot land in two
bands), the module has named a winner.

## NERS reading

- **N**: top-down a trial is evidence answered before a bench; bottom-up every part exists (the
  roll, the case file, the bench query, the suspension); lateral it is combat's two modes;
  diagonal the disposal is read by governance. Narrowed in one direction, stated: a sitting cannot
  be interrupted from outside (addendum §B4.7).
- **R**: strategy (what to file, what to hold, when to concede), variety (the rite's moves and
  faults), impact (which items stand on the record afterwards); without a player the same sitting
  runs between NPC deciders. Complete at its extremes: no exhibits is today's draw; a fault never
  ends the game by fiat.
- **S**: one roll owner, one obstacle owner, one ladder; pauses as combat does, at ENCOUNTER.
- **E**, last: six move rows, four fault rows, one module file, against a subsystem that can be
  played and whose automated and played forms are the same function.

## Cost class

Small builds (edits 1 to 5, 7, 9, 10), design-first for the NPC decider's terms (8) and the host
builder's reading of the rite (6, after CR-60 and CR-61).
