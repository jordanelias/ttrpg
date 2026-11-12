# SC-B3 — The social capabilities as rows: rhetoric, law, insight, deception, and what each move and verb draws on

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-02 — `answer` moved from the draw-free moves to a rolled move with a capability.

## Status: PROPOSED — extends SC-P7 (`05_SC_capability_surface.md`; one of its rows replaced) and sequences after CORE's and DICE's capability surfaces

Source: `audits/05_SC_audit_addendum_B.md` §B5, G-52, G-53. It adds **rows** to the surface others
own and no table of its own except `hearing_moves`' `capability:` column, which is SC's fact. The
definition row is the one `01_CORE_capability_authoring_surface.md` (its `capabilities:` block) and
`10_DICE_capability_axiom_map.md` §B (`tables.capabilities`) propose field for field; they differ
only in the file, and, as `02_CHAR_capability_definitions.md` does, this proposal names the table and
not the path. Use rows go in `tables.capability_uses` (DICE §C, which absorbs
`02_CHAR_capability_uses_table.md`'s three rows and its `about_mid` / `at_least` forms).

## What it changes in `engine/season/` at runtime

Nothing in the shipped realm until a cast row holds one of the new keys or an attribute: every new
skill is `untrained: default`, so a non-holder rolls `pool_default` exactly as today, and at seed 0
no person holds an attribute on these bases that differs from today's read (`aperture 2 0`: pools
`[2]` for every actor; first audit §12). The verb re-pointings change which key a holder's practice
counts toward and which attribute opposes. With the cast as shipped, the content hash is expected
unchanged; the gate measures it.

## The problem (evidence)

1. The social roll has four vocations (`copying`, `argue`, `inquiry`, `arms`), and a liar rolls
   either `pool_default` (no `verb_capability` row for `lie` today) or, under SC-P7 and CORE's edit 8,
   `copying`, the copyist's skill (CORE edit 8: *"a lie is a telling of a false value"*). A tribunal's
   `determine` rolls `argue` under CORE's edit 8: a judge's competence is a debater's.
2. The hearing's moves (`05_SC_playable_hearing_B.md`) roll on "his capability for the rung"; no row
   says which.
3. What a person can read of a bench has no capability at all; the kernel's `appraise.py` ladder was a
   second information roll (addendum §B3, carried as an idea).
4. The RPG axioms a designer expects for a social game — deception opposed by perception, legal
   knowledge as its own skill, a passive read of a room — have no row (first audit §14 (d)).

## The resolution, decided

### Four new definition rows (`kind: skill`, `untrained: default`, `grows_by: [train, practice]`, scale 0–7)

| id | what it is (the sentence CHAR's `02_CHAR_capability_definitions.md` asks every row to carry) | `base` | `opposed_by` |
|---|---|---|---|
| `rhetoric` | moving a room by argument: the speech made to a bench or an assembly | `attr.social.charisma` (Presence) | — (the other side's score on the same key) |
| `law` | knowing and applying the rules of a forum: procedure, definition, precedent; a judge's faculty | `attr.mind.acuity` (Reason) | — |
| `insight` | reading what a person or a bench is disposed to; never rolled | `attr.social.attunement` | — |
| `deception` | making another believe what one knows to be false, by word or by paper | `attr.social.grace` | `attr.mind.perception` |

`argue` (one-to-one persuasion, base Presence) stays as it is. All bases are `grade: assumption`; a
designer re-points one by editing one cell. Ladder step 4 (the existing row shape) for the form;
step 5 for the four values.

### What draws on what (the `capability:` column on verb rows, CORE's; on `hearing_moves` rows, SC's)

| row | capability | replaces | ground |
|---|---|---|---|
| verb `lie` | `deception` | SC-P7 and CORE edit 8: `copying` | a lie is opposed by the hearer's perception, a telling by nothing of his; one key for both would make a scribe a liar |
| verb `determine` | `law` | CORE edit 8: `argue` | a judge rules on procedure, definition and fact; persuasion is the parties' |
| verb `interrogate` | `inquiry`, `opposed_by: attr.mind.will` | — (CORE edit 8 already; SC-P7 edit 2) | unchanged, cited |
| verb `arrest` | as CORE edit 8 (`argue`) until CR-92 | — | CR-92's design; not decided here |
| move `argue` | by rung: `procedure`, `definition` → `law`; `fact`, `justification` → `rhetoric` | — | the rung argued is what is in issue |
| move `impugn` | `rhetoric` | — | an attack on a source made to the room |
| move `answer` | by rung, as `argue` (Reconciled, D-02: `answer` is a rolled move) | — | answering an item before the room is argument about it; the weights set the obstacle, the answerer's skill the pool |
| moves `present`, `concede`, `rest`, `offer`, `accept` | none (no contest roll: filing and the party's own choices; `offer`/`accept` are sampled choices, D-06) | — | the loader refuses a `capability:` on a draw-free move and its absence on a rolled one |

**Sequencing, not a conflict.** CORE's edit 8 needs no new definition rows and can ship first; this
proposal's re-pointing of `lie` and `determine` follows the day the four rows land, each one cell with
its own revert. Ladder step 5: the order in which the two are applied decides nothing the other
needs.

### Insight is a use, not a roll

One row in `tables.capability_uses`: `{use: bench_reading, role: judgement, key: insight, form:
at_least, gain: insight_bench_threshold}` (CHAR's `at_least` form). The role is the uncertain cell:
DICE's `gate` is closed by ruling to Thread Sensitivity, and its `judgement` is a factor about the
mid-point, not a threshold on what is shown. `judgement` is used as the nearer of the two; if the
holistic merge judges what a person can see to be a role of its own, it is one member of
`capability_roles` and this row changes one cell `[ASSUMPTION; medium]`. `bench_reading` is a new member of
`capability_use_sites` whose one reader is the hearing's turn-view builder (`sigma.py::hearing_input`):
below the threshold the view carries each seat's public commits only; at or above it, the sign of each
seat's `lean`. It is the kernel's appraisal ladder with no second roll, and Disco Elysium's passive
check as the tree sources it (addendum §B4.5). Fixture `insight_bench_threshold` (proposed 3, NUMBER
row, three-point sweep).

### What stays elsewhere

Office weight and title on the roll and the obstacle (R-38 as recorded) are FA's rows
(`06_FA_office_capabilities.md`), read through DICE's `score()` in both roles
(`10_DICE_one_score_two_roles.md`). Traits that harden or soften a hearer are SC-P7's
`trait_advantages` rows, which DICE's map absorbs as `edge` rows with `side: subject` (§E of the
map: NPC-001's *unmoved by rhetoric* is its own worked example).

## Exact edits, by owner

1. The capabilities table (CORE's block or DICE's `tables.capabilities`, whichever lands): the four
   rows above.
2. `engine/season/verb_table.yaml` (CORE's `capability:` column): `lie: deception`,
   `determine: law`, after CORE edit 8.
3. `engine/season/rosters.yaml: hearing_moves` (`05_SC_playable_hearing_B.md` edit 1): a
   `capability:` column, a single id or a map from `issue_rungs` member to id; `data/rosters.py`
   refuses an unknown id, a map missing a rung, a capability on a draw-free move.
4. `tables.capability_uses`: the `bench_reading` row; `capability_use_sites` gains `bench_reading`;
   `data/fixtures.py`: `insight_bench_threshold`.
5. SC-P7 edit 1 (`lie: copying`) is withdrawn by this proposal; SC-P7's edits 2 to 4 stand.

## Gate (execution artifacts)

1. `build_realm(0..2)` one season before and after edits 1 to 3: content hashes EQUAL (no holder);
   a planted cast row holding `deception: 4` and a hearer with `attr.mind.perception: 5`:
   `sigma.odds_of` for that person's `lie` follows the planted values, and a planted `copying: 4` no
   longer moves it.
2. A hand-built sitting with one seat leaning against the player's party: the turn view at
   `insight` 2 shows no lean; at 3, the sign.
3. `fed_by` on a graded `determine` (DICE's returned record) names `law`.

## Falsifier

A holder of `copying` whose `lie` odds move after edit 2; a rolled move the loader admits with no
capability; a turn view that shows a lean below the threshold.

## NERS reading

- **N**: the provided characters are specified by exactly these distinctions (a jurist, a liar, a
  reader of rooms); top-down a designer adds a social skill as a row; lateral combat already
  distinguishes its faculties.
- **R**: characters differ in what they are good at in a room, by data; the no-player half: an NPC
  forger and an NPC judge differ by rows, not code.
- **S**: one definition shape, one uses table, one pool reader; insight read through the same
  `at_least` form as Thread Sensitivity's gate.
- **E**, last: four rows, one column, one use row, against a social game whose skills have names.

## Cost class

Edit (rows and column), after CORE or DICE part one lands.
