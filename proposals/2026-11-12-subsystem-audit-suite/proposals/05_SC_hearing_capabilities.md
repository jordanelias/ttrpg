# SC-B3 — The social skills as rows: law, insight, deception, and what each move and verb draws on

Reconciled: 2026-11-12 by `audits/18_DETERMINISM_SWEEP.md` D-02 — `answer` moved from the draw-free moves to a rolled move with a capability.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-B3, §2 rows `bench_reading`, §7, §7b-10, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-01, D-U1-03, D-U1-07, ledger C-09, C-10, S-05; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2, §5; `unified/U3_CONFLICT_LEDGER.md` §9 (the `bench_reading` row adopted); `unified/U3_DEPENDENCY_ORDER.md` §4.1 row 13). Changed: **`rhetoric` is struck** (D-U1-03; the title drops it): three new rows, `deception`, `law`, `insight`; `insight` is an `aptitude` with `untrained: none` (U1 §2); `hearing_moves` cells are `argue` (rungs `fact`, `justification`) and `law` (rungs `procedure`, `definition`), `impugn` → `argue`, `answer` → as `argue`; `arrest` is `arms` (U1 §5); the definition home is named (`references/descriptor_registry.yaml: capabilities`); **`bench_reading` is rewritten from a threshold reveal to a drawn deposit** (`04` §B.2 / AX-2 and A-11 and the standing rule *we do not do deterministic*: R2 graded the threshold form VIOLATES; fixture `insight_bench_threshold` deleted); the seat's place on the roll follows D-U1-01; named tests, lands-it and tier added. For another lane (U1's own file): `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3's `bench_reading` row and ledger C-22 still carry the threshold form. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "faculty" → "capability"; "vocation" → "capability" (glossary *faculty*, *capability*).

**Lands in batch:** B04 (definition rows; verb cells), B24 (the `hearing_moves` column and `bench_reading`, with `05_SC_playable_hearing_B.md`; U3 §4.1 row 13). **Depends on:** `01_CORE_capability_authoring_surface.md` (B04), `02_CHAR_capability_uses_table.md` (B04), `05_SC_playable_hearing_B.md` (B24, for the moves and the turn view).

## Status: PROPOSED — extends SC-P7 (`05_SC_capability_surface.md`; one of its rows replaced) and sequences after CORE's and DICE's skill surfaces

Source: `audits/05_SC_audit_addendum_B.md` §B5, G-52, G-53. It adds **rows** to the surface others
own and no table of its own except `hearing_moves`' `capability:` column, which is SC's fact. The
definition row is `references/descriptor_registry.yaml: capabilities` (U1 §1–§2, D-U1-07). Use rows go in
`rosters.yaml: tables.capability_uses` (U1 §3, whose `role` column implies the factor form).

## What it changes in `engine/season/` at runtime

Nothing in the shipped realm until a cast row holds one of the new keys or an attribute: every new
skill is `untrained: default`, so a non-holder rolls `pool_default` exactly as today, and at seed 0
no person holds an attribute on these bases that differs from today's read (`aperture 2 0`: pools
`[2]` for every actor; first audit §12). The verb re-pointings change which key a holder's practice
counts toward and which attribute opposes. With the cast as shipped, the content hash is expected
unchanged; the gate measures it.

## The problem (evidence)

1. The social roll has four skills (`copying`, `argue`, `inquiry`, `arms`), and a liar rolls
   either `pool_default` (no `verb_capability` row for `lie` today) or, under SC-P7 and CORE's edit 8,
   `copying`, the copyist's skill (CORE edit 8: *"a lie is a telling of a false value"*). A tribunal's
   `determine` rolls `argue` under CORE's edit 8: a judge's competence is a debater's.
2. The hearing's moves (`05_SC_playable_hearing_B.md`) roll on "his capability for the rung"; no row
   says which.
3. What a person can read of a bench has no skill at all; the kernel's `appraise.py` ladder was a
   second information roll (addendum §B3, carried as an idea).
4. The RPG axioms a designer expects for a social game — deception opposed by perception, legal
   knowledge as its own skill, a passive read of a room — have no row (first audit §14 (d)).

## The resolution, decided

### Three new definition rows (scale `[0, 7]`, `grows_by: [train, practice]`; U1 §2)

| id | `kind` | `untrained` | `gloss` (the sentence CHAR's `02_CHAR_capability_definitions.md` asks every row to carry) | `base` | `opposed_by` |
|---|---|---|---|---|---|
| `law` | skill | default | Knows and applies the rules of a forum: procedure, definition, precedent; a judge's skill. | `attr.mind.acuity` (Reason) | — |
| `insight` | skill (A-98; was `aptitude`) | none | Reads what a person or a bench is disposed to; never rolled. | `attr.social.attunement` | — |
| `deception` | skill | default | Makes another believe what one knows to be false, by word or by paper. | `attr.social.grace` | `attr.mind.perception` |

`rhetoric` is **not created** (D-U1-03): it would share `argue`'s governing attribute, untrained rule and
growth rules and differ only in audience, which already reaches the roll as the obstacle term `reception`
and the `favour` level; a second skill for one act would split one person's skill score in two. `argue`
(persuasion, base Presence) carries the hearing's argument to a bench as to one person. All bases are
`grade: assumption`; a designer re-points one by editing one cell. Ladder step 4 (the existing row shape)
for the form; step 5 for the three values.

### What draws on what (the `capability:` column on verb rows, CORE's; on `hearing_moves` rows, SC's)

| row | skill | replaces | ground |
|---|---|---|---|
| verb `lie` | `deception` | SC-P7 and CORE edit 8: `copying` | a lie is opposed by the hearer's perception, a telling by nothing of his; one key for both would make a scribe a liar |
| verb `determine` | `law` | CORE edit 8: `argue` | a judge rules on procedure, definition and fact; persuasion is the parties' |
| verb `interrogate` | `inquiry`, `opposed_by: attr.mind.will` | — (CORE edit 8 already; SC-P7 edit 2) | unchanged, cited |
| verb `arrest` | `arms` | CORE edit 8's first `argue` | U1 §5: FA (the verb's lane), DICE and lane A agree; `capture`'s precedent |
| move `argue` | by rung: `procedure`, `definition` → `law`; `fact`, `justification` → `argue` | — | the rung argued is what is in issue (D-U1-03) |
| move `impugn` | `argue` | — | an attack on a source made to the room (D-U1-03) |
| move `answer` | by rung, as `argue` (Reconciled, D-02: `answer` is a rolled move) | — | answering an item before the room is argument about it; the weights set the obstacle, the answerer's skill the pool |
| moves `present`, `concede`, `rest`, `offer`, `accept` | none (no contest roll: filing and the party's own choices; `offer`/`accept` are sampled choices, D-06) | — | the loader refuses a `capability:` on a draw-free move and its absence on a rolled one |

**Sequencing, not a conflict.** CORE's edit 8 (as reconciled to U1 §5) ships `lie: none` (noted) and
`determine: argue` (interim) until this proposal's `deception` and `law` rows land in the same batch (B04);
each re-pointing is then one cell with its own revert. Ladder step 5: the order decides nothing the other
needs.

### Insight is a use, not a roll

`insight` is a `judgement`-role skill at the use site `bench_reading` (role `judgement`, factor form
`about_mid`, U1 §3): its factor scales the **confidence** of the claim WITNESS deposits in a viewer's ledger
about each seat's lean, never a threshold on what is shown. At the turn view
(`seam/wrappers/sigma.py::hearing_input`, the site's one reader) every seat's public commits are shown;
each seat's lean sign enters the viewer's ledger as a claim `(seat, leans, ±1)` deposited with a keyed draw
`H(seed, tick, viewer, f"bench_read:{seat}")` (A-30) whose probability of showing the true sign rises with
`capability_factor(viewer, "bench_reading", fx)`. A wrong sign is possible at every insight. The row:
`{use: bench_reading, role: judgement, key: insight, side: actor, gain: insight_gain}` (fixture
`insight_gain`, control 0: at 0 the factor is 1 and the probability is the fixture `bench_read_base`,
NUMBER row, three-point sweep `[ASSUMPTION: base 0.5, i.e. a guess, at control — basis: no reveal before
this proposal]`). Fixture `insight_bench_threshold` is **deleted** (never created). Reason: a threshold
reveal carries another person's interior to the viewer by a fixed rule (`04` §B.2, AX-2: a decision may
not read world truth), makes a skill a gate on what he may know (A-11), and decides by threshold (the
standing rule). It is still the kernel's appraisal ladder with no second roll, now drawn.

### What stays elsewhere

A seat reaches the roll in two ways only (D-U1-01): the seat the actor exercises helps him as one level
from the leverage source `office`, read off that seat row's `modifier:` (`offices.yaml`); a seat held above
his by the person acted on stands against him as the obstacle term `rank_gap` (OBS §2 member 6). Neither
is a skill or a use row, and neither enters `score()`. Traits that harden or soften a hearer are
`edge` rows of `capability_uses` with `side: subject` (SC-P7 edit 3 as superseded; NPC-001's *unmoved by
argument* is the worked example).

## Exact edits, by owner

1. `references/descriptor_registry.yaml: capabilities`: the three rows above (B04).
2. `engine/season/verb_table.yaml` (CORE's `capability:` column): `lie: deception`,
   `determine: law`, after CORE edit 8.
3. `engine/season/rosters.yaml: hearing_moves` (`05_SC_playable_hearing_B.md` edit 1): a
   `capability:` column, a single id or a map from `issue_rungs` member to id; `data/rosters.py`
   refuses an unknown id, a map missing a rung, a skill on a draw-free move.
4. `tables.capability_uses`: the `bench_reading` row; `capability_use_sites` gains `bench_reading`
   (reader `sigma.py::hearing_input`); `data/fixtures.py`: `insight_gain` (control 0), `bench_read_base`;
   WITNESS's deposit of the `(seat, leans, ±1)` claim at the turn view's draw (B24, with HEAR_B).
5. SC-P7 edits 1–3 are superseded by U1 (`05_SC_capability_surface.md` as reconciled); its edit 4 stands.

## Gate (execution artifacts)

1. `build_realm(0..2)` one season before and after edits 1 to 3: content hashes EQUAL (no holder);
   a planted cast row holding `deception: 4` and a hearer with `attr.mind.perception: 5`:
   `sigma.odds_of` for that person's `lie` follows the planted values, and a planted `copying: 4` no
   longer moves it.
2. A hand-built sitting with one seat leaning against the player's party, over 400 seeds: the share of
   seats whose lean the viewer holds with the true sign is strictly between 0.5 and 1 at insight 2 and
   at 5, and higher at 5 (at `insight_gain` above 0).
3. `fed_by` on a graded `determine` (DICE's returned record) names `law`.

**Named tests** (new, `engine/season/tests/test_sc_hearing_capabilities.py`):
`test_rhetoric_is_not_a_capability_row`; `test_lie_odds_follow_deception_and_perception_not_copying` (gate 1);
`test_bench_reading_is_drawn_and_can_be_wrong_at_every_insight` (gate 2);
`test_fed_by_on_determine_names_law` (gate 3); `test_a_rolled_move_with_no_capability_is_refused`.

## Falsifier

A holder of `copying` whose `lie` odds move after edit 2; a rolled move the loader admits with no
skill; a turn view that shows any seat's true lean with certainty (share 1.0), or that reads a seat's
lean from World rather than from the viewer's own claim. **Control.** Hash EQUAL at the shipped cast
(no holder; `insight_gain` 0).

## NERS reading

- **N**: the provided characters are specified by exactly these distinctions (a jurist, a liar, a
  reader of rooms); top-down a designer adds a social skill as a row; lateral combat already
  tells its skills apart.
- **R**: characters differ in what they are good at in a room, by data; the no-player half: an NPC
  forger and an NPC judge differ by rows, not code.
- **S**: one definition shape, one uses table, one pool reader; insight read through the same
  `about_mid` judgement form as the told-claim credit, on a drawn deposit.
- **E**, last: three rows, one column, one use row, against a social game whose skills have names.

## Cost class

Edit (rows and column), after CORE's part one lands; the `bench_reading` deposit is a small build.

**Lands it.** B04: the definition rows and verb cells, an SC `valoria-author` session on `sonnet` (`high`) in
the capability batch. B24: the `hearing_moves` column and `bench_reading`, a `methodology-execute` batch with
HEAR_B on `sonnet`, closed by `methodology-close` with its terminal `opus` critique once. **Hash movers.**
None at the shipped cast (control: the batch's base tree).
