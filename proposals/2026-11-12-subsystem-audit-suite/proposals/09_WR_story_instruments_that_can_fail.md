# WR · Story instruments that can fail

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` (F-30-08). Nothing here is deleted. This file's `edge_null` shows that a chain's links are not coincidence of count; it cannot show that the first act made the second likelier. `30_WR_E_cascade_chains_and_the_census.md` §2 adds the third control, the **fork lift**: one built world forked under several draw seeds before an event that is itself a draw, comparing what follows where it occurred and where it did not (`fork_lift`, on `storybar.fork` and `draw_seed_arm`). It also adds two arms to edit 1's roster (`entrenched`, and `custom_off` / `custom_on`) and the `--null-scenes` reading. Edit 3's shape line prints per strand its state and subject once `30_WR_C` commit 2 lands. Edit 5's `why` gains `era`, `story` and `left` (`30_GO_F`).

## Status: PROPOSED

Carries findings F-WR-01 (edit 4), F-WR-03 (edits 1 to 3) and the reason-trail need of audit §5.5
(edit 5) of `audits/09_WR_audit.md`. Evidence ids (E-nn) are that file's §12.

## What it changes in `engine/season/` at runtime

**Nothing.** Every edit is under `engine/season/harness/` or `engine/season/tests/`; no step of the loop
imports either. No content hash moves. It changes what the project can learn from a run.

## The problem

The one instrument that answers "does the engine produce stories" (`harness/storybar.py`, the M2 instrument)
cannot report a failure, compares an arm with itself, and counts refusals in its headline; the control
that guards the chronicle's story reading (`harness/chronicle.py::consequence_chains`, CR-69) points the
wrong way on a real log; and the strife reading says "concluded" of a declared march (see
`09_WR_strand_conclusion.md` for that half).

| observation | reading | run |
|---|---|---|
| `ARMS = ("off",)`; the CLI compares `off` with `off` | EQUAL, by construction | `storybar.py:87`; E-03 |
| three forcing fixtures are built | `season_factor_draw`, `age_step`/`illness_rate`, `lattice_coupling` | `data/fixtures.py:535,690,691,700` |
| headline counts refusals | cross share 23.4% over all acts, 14.4% over executed; 355 of 616 deep acts refused | E-07 |
| forcing on, headline does not follow | seed 0: 23.4% → 22.1%; seed 1: 22.3% → 24.4%, while deaths go 0 → 8 and 1 → 4 | E-11, E-12 |
| CR-69's shuffled-causes control | real 29, 44 chain ends against null 86 to 97, 104 to 114: the null reads ABOVE | E-05, E-07 |
| the test of that control | asserts `null < real` on a plant of six disjoint chains; on a real seed asserts `!=` | `tests/test_cr69_chains.py:99-112`, `:174-185` |
| an edge-count-preserving null | executed chains exceed it (36 against 10.8; 27 against 9.0); consequence chains do not (2 against 1.2; 0 against 1.1) | E-10 |

## The resolution, decided

1. The story bar gets the arms it was specified with, built from fixtures that already exist.
2. Its control is a null that keeps what the log has (how many cross antecedents each act has) and breaks
   only which acts they are.
3. It reports, beside its present lines, a small **shape reading**: per seed, how many strands have an
   opening, an escalation and a close. A reading, with no pass bar (V2 stands), but one whose zero is
   visible.
4. The strife route check prints how often each route was taken.
5. The chronicle prints why an act was taken where the log can say.

No new file, no new gate, no CI job. Each edit is to an existing owner.

## The edits

### Edit 1 · forcing arms (`engine/season/harness/storybar.py`)

Old (`:85-87`):

```python
#: Every forcing setting this tree can run. `off` is the shipped loop; no `on` is built (see the
#: module docstring). A forcing position adds its own arm here.
ARMS = ("off",)
```

New: `ARMS` becomes a mapping from arm name to the fixture sweep it applies, the idiom `harness/arms.py`
already owns (`_resolve_arm`, `w.fixtures.sweep`), so the story bar holds no second sweep rule:

```python
#: arm name -> {fixture name: value}; each value is a member of that fixture's own declared `sweep:`
#: (hole_register H-26, H-208, H-235), never a number invented here. `off` is the shipped loop.
ARMS = {
    "off":      {},
    "weather":  {"season_factor_draw": ((0.5, 1.0, 2.0),) * 4},      # H-26's swept arm
    "bodies":   {"illness_rate": <H-208's test arm>},                 # read from the row, not typed here
    "lattice":  {"lattice_coupling": 250},                            # H-235's swept arm
    "all":      <the union of the three>,
}
```

`drive()` applies the arm with `w.fixtures.get(name)` then `w.fixtures.sweep(name, value)` on the freshly
built world before the chooser is made (the two lines `harness/arms.py:205-207` already uses). The module
docstring's "No forcing source is built yet … so there is no `on` arm" is deleted. `--arms off off` stays
the control and must still read EQUAL.

Typed interface: unchanged. `drive(seed, seasons, arm, cap=None, …) -> (world, driver, bounds)`.

⚠ `illness_rate` and `age_step` are deferred by ruling (ED-IN-0317) **as shipped values**. An instrument
arm that sweeps a fixture on a copy of the world ships nothing; H-208's own row lists test arms. If Jordan
reads the deferral as covering instrument arms too, drop `bodies` and `all`; the other two stand.

### Edit 2 · the null (`engine/season/harness/storybar.py`, `chronicle.py`, `tests/test_cr69_chains.py`)

Add to `storybar.py`, beside `_depths`:

```python
def edge_null(rows: dict, seed: int) -> dict:
    """`rows` (as `read` returns them) with each act's cross antecedents RE-DRAWN: the same number,
    chosen uniformly among earlier-logged acts by another actor (`random.Random(seed)`). Depth is
    recomputed by `_depths`. A reading that does not exceed this is what any log with that many
    cross edges would show."""
```

`chronicle.consequence_chains` gains `null_seeds: tuple = ()` and, when given, returns
`"null_chain_ends": [..]` beside `"chain_ends"`; `render_chains` prints `chain_ends=N (edge null: mean M,
range a..b)`. `arc.shuffled_causes` is kept for `read_arcs`, where it does hold (arc reader 21 to 23 persons
against 0 or 1, E-05, E-07); it is removed as the control of the chain reading.

`tests/test_cr69_chains.py::test_the_shuffled_causes_null_reads_below_the_linked_log` is replaced by a
test over `edge_null` on the same plant (four depth-3 chains: the edge null reads below 4 at every seed),
and `test_the_reader_on_a_real_seed…`'s `null != real` becomes: `edge_null` over the real rows preserves
the number of cross edges exactly and changes at least one antecedent.

### Edit 3 · the shape reading (`engine/season/harness/strife.py::strands_block`)

One line per seed, after `concluded N of M`:

```
  shape: opened O · escalated E · closed C · closed-and-stayed S (of M strands)
```

- *opened*: the strand holds an `opens` move (always true; printed as the denominator's check);
- *escalated*: it holds a move by a doer other than its first doer, later in the log than its opening;
- *closed*: its latest move is terminal, is **not** an opening move, and `world_q.concluded` holds;
- *closed-and-stayed*: reported only by the two-reading form, `strands_block(w, seed, earlier=…)`, where
  `earlier` is the set of strand ids `concluded` at the previous season boundary: how many of those are
  still concluded strands now.

It reads `Flows` and `Move` fields that exist (`doer`, `opens`, `terminal`, `index`); it adds no roster.

### Edit 4 · routes taken (`engine/season/harness/strife.py::opening_routes`, `strands_block`)

`opening_routes` stays static. `strands_block` already holds the world; beside `route check: X of Y pairs
have no act route` it prints, per terminal code with a static route, the executed count of that route's
verbs over the run (from `corpus_run.attempts`, the one owner of made and refused), and marks a code whose
every terminal verb executed 0 times `ROUTE, NEVER TAKEN`. At seed 0, three seasons, that mark would stand
on every code whose route is `determine`, `covenant`, `fight`, `pardon` or `seize` (E-07).

### Edit 5 · the reason trail (`engine/season/harness/chronicle.py::lines`, `render`)

`soak._occasion_row(d, act)` already returns the question an act answered (`source`, `about`, `referents`);
`arc.py` reads it. The chronicle renders `answers N. <actor> <verb>` for a cross-person antecedent and
nothing for an act that answered a standing ambition. Add a `why` field to each line: for a `need`
question, `pursuing <Proposition id, and its predicate where the store holds one>`; for `claim_landed`,
`on learning <claim predicate> about <subject name>`. It reads the driver's `Scene`, as `arc.py` does.

**Interface this lane needs from CORE** (not an edit here): the occasion is recoverable today only from a
live `SeasonDriver`; a saved log cannot be chronicled with reasons. `Event.observed` is the field for
"what was read to reach this Event" (`loop/matter.py:619-621`); an act's first Event carrying
`(question.source, question.about)` there would make the reason part of the record. That is a hash mover
in `loop/resolve.py::_act_events` and is CORE's to weigh.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 3 --arms off all --executed-only
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 3 --arms off off
PYTHONHASHSEED=0 python -m engine.season.harness.chronicle --seed 0 --seasons 3 --chains --min-depth 3
PYTHONHASHSEED=0 python -m engine.season.harness.strife 3 0 1 2 --strands
```

Passes when: the first prints `DIFFER` and a per-seed `person.died` count above the `off` arm's; the second
prints `EQUAL`; the third prints an edge null beside the chain ends; the fourth prints a `shape:` line and a
`ROUTE, NEVER TAKEN` mark. `build_realm(0)`'s content hash and the one- and two-season pins are unchanged
(the control that nothing in the loop moved).

## The falsifier

- Edit 1: an arm that reads EQUAL to `off` on every pooled season reading. That is a fixture the loop does
  not read, and is a finding about the fixture.
- Edit 2: `edge_null` over the planted world reading at or above the plant's four chains.
- Edit 3: a plant of one opened, escalated, closed strand reading `closed 0`.
- Edit 4: a planted executed `determine` leaving `ROUTE, NEVER TAKEN` on XS.

## NERS reading

- **N.** Without edits 1 and 2 the project has no measurement of its central claim; removing them is how
  the tree stands today, and F-WR-03 is what that costs. Edits 3 to 5 are narrower: 3 and 4 hold in the
  top-down direction (does the world close what it opens) and bottom-up (did this verb ever run); 5 holds
  lateral to the CHAR lane's reason trail.
- **R.** No player is involved; this is the no-player half's instrument. Completeness: the null is defined
  for an empty log (no rows, no edges) and for a log with no cross edge (it returns the rows).
- **S.** One methodology for "is there structure": the edge null replaces two controls that disagreed
  (shuffled-causes for chains, shuffled-order for code pairs). The strife block's adjacent-pair and
  sixteen-link controls stay; they answer a different question (order within a strand).
- **E, last, as a ratio.** About sixty lines of harness against the only numbers that say whether stories
  occur. High.

## Cost class

Edit (1, 4, 5) and small build (2, 3). One session. No design decision is needed except the reading of
ED-IN-0317 flagged at edit 1.
