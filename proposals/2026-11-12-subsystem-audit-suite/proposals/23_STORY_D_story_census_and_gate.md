# STORY-D — the story census: a story named by its beats in the cause graph, its rate, its spread and its control; and the gate every enablement batch is read on

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` (the standing charges on eras, momentum, A-80, A-81, A-83). Nothing here is deleted; `Shape`, `Beat`, `stories`, the seven clauses and `--pin-rolls` are used as written. `30_WR_E_cascade_chains_and_the_census.md` extends this census: (1) **shapes** E-01 to E-13 in this file's format (a reign ends; a vacancy fought over; a war inside the realm with an end; a conquest; a schism; a famine's end; a regime moves; the side thins; a strand revived; the man who would not do as his house does; an era turns; a cascade of depth four across three kinds of write; another means after a failed attempt), each with its plants in `tests/test_storybar.py`; (2) **clauses** C7 to C13 beside C0 to C6: C7 compounding by the fork lift on one built world; **C8 a held world still moves** (the `entrenched` arm, in which every contested draw falls to the holder, must still show three of ten pressure shapes at two seeds or more and at least half the free arm's executed acts per person-season); **C9 no scene is still** (`null_scenes`, expected 0, with a planted null as its control; baseline on the shipped engine above 0); C10 the pull is felt and resisted (arms `custom_off`, `custom_on`); C11 an era can end and not on a timer; C12 strands stay several; C13 regimes are more than one and move. (3) The `entrenched` arm reuses this file's `--pin-rolls` wrapper, restricted to rows that declare `contests:`. (4) The cascade chains K-1 to K-9 in that file's §1 are sequences of this audit's story ids, link by link; they add no story.

Reconciled: 2026-11-12, U5d closure — folded the answers to the audit's §8.3 defaults. Batches re-read: E-2 completes S-67 (A-9: a scene is a short sequence); E-3's natural-death gates read the live rate, not the `bodies` instrument arm, once the ages are authored (A-15); E-5 reads the deed race (A-19), the head's strip (A-35) and custody (A-23), and its S-16 reads the Split as a strife move (A-46); E-7 gates on `enmity` behind its control (A-16) and a verdict that names the petitioner (A-38); E-8 gains "a place and its seats change hands by arms" when a victor seizes after a won march, and its two other tellings, an occupation and a raid that goes home (A-57, A-58, A-66); E-9's crisis and scruple are drawn (A-24). Every census reading is taken after the five-year prologue (A-51). The one default still standing is the form of fortune in a field (D-34, open).

## Status: PROPOSED

Source: `audits/23_STORY_ENABLEMENT.md` §1 (what counts as a story), §2 (the 73), §6.1 (the seven
clauses). Composes on, and does not restate: `09_WR_story_instruments_that_can_fail.md` (the forcing
arms, `edge_null`, the shape line, the reason trail), `20_NARRATIVE_F_story_inventory_and_gate.md` (the
crossings block and `tests/test_storybar.py`), `16_PESSIMIST_GAME_consequence_reading.md`,
`09_WR_B_readings_of_closure_and_tension.md`, `16_PESSIMIST_CORE_the_record_holds_what_changed.md`
(receipts with a value), `07_SE_valley_scenario.md` (a small world a gate can afford 20 seeds of).
Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

**Nothing.** Every edit is under `engine/season/harness/` or `engine/season/tests/`, which no step of
the loop imports. No content hash moves. It mints no carrier, field, Event kind or register row for an
arc, story or thread (`ED-IN-0225`, quoted in `harness/storybar.py`'s own docstring): a story here is a
reading of the log the loop already writes, as `strands_block` is.

## The problem, with evidence

- The suite's gates are link gates: a verb executes, a band occurs, a claim is held. No gate reads a
  chain that crosses lanes, and a story is such a chain (`audits/23_STORY_ENABLEMENT.md` §0).
- The story bar reads depth of the cause graph and cannot fail (`09_WR_audit.md` F-WR-03, as that lane's
  proposal states it); `20_NARRATIVE_F` adds six crossing classes, which count a pull meeting an act,
  not whether anything was opened, turned, paid for and closed.
- Every instrument that walks `causes[]` is blind to the closing acts and none compares against a null
  arm (`16_PESSIMIST_GAME.md` §3.8), so a realm that corresponds cannot be told from a realm that
  changes.
- The pessimist lanes each enumerated stories by hand, in scratch probes that die with the session
  (`CLAUDE.md` §1).

## The resolution, decided

One block, `--stories`, on the instrument that already owns "does the engine produce stories". A story
is a **shape**: four beats and the links between them. The block prints counts, variants and arms; it
grades nothing (the story bar's standing rule, V2). The seven clauses of the audit's §6.1 are read off
its output by the session that closes a batch. No CI job, no guard, no second bar beside WR's and
NARR-F's (ladder step 4: `strands_block` and NARR-F's `crossings` are the precedents for a block behind
a flag; step 5: one owner for the reading).

## Exact edits, by owner

**1. `engine/season/harness/storybar.py` — `Shape`, `SHAPES`, `stories()`.**

```python
class Beat(NamedTuple):
    kinds: tuple          # Event kinds, any of
    role: str = "any"     # "any" | "other" (actor differs from the opening's) | "same" | "patient"
                          # (the Event's subject is the opening's actor) | "world" (no act emitted it)
    bands: tuple = ()     # degrees admitted; () is any

class Shape(NamedTuple):
    id: str               # "S-32"
    name: str
    opening: Beat
    turn: Beat
    close: Beat
    cost: tuple           # matrix fields a party must lose on: ("Person.body", "Rung.stores", …); () = none asked
    window: int           # seasons from opening to close
    variant: str          # what the close is read by: "kind" | "band" | "kind+band" | "party"

def stories(w, d, bounds, shapes=SHAPES, seat=None) -> dict:
    """{shape id: [Instance(season, opening, turn, close, parties, variant)]} — pure, over the log,
    `d.act_of`, the act store and the Tenures. A beat matches an Event of one of its kinds whose role
    constraint holds. Beats are LINKED: the turn has the opening among its ancestors and the close has
    the turn, through `causes[]`, an act and the Events it emitted being one node (`read`'s graph) and
    a `claim.deposited` Event a pass-through (so 'the news reached him and he acted' is a link).
    An instance is counted once, at its close. `cost` holds when a receipt with a non-None `delta` on
    one of the named fields falls on a party between opening and close."""
```

- A shape any of whose kinds no verb row and no MATTER pass emits prints `n/a (no emitter)`, computed
  from the loaded kind table (`data/verbs.py`), never from a hand list: an absent reader is not a zero
  (NARR-F's rule).
- `cost` prints `n/a` until `16_PESSIMIST_CORE_the_record_holds_what_changed.md` edit 1 lands (0 of
  36,586 receipts carry a value today), and the instance is then counted without it and marked
  `(cost unread)`.
- `SHAPES` is data in this module, as `ARMS` is. It is an instrument's reading table, not a fact the
  game reads (§0.05: delete it and the game behaves the same).

**2. The first table: the control set, and one shape per family.** Each later batch adds the shapes of
the stories it claims, with their plants (edit 5), in the commit that closes the batch.

| id | opening | turn | close | cost | variant |
|---|---|---|---|---|---|
| C-a (control: the petition that lapses) | `petition.filed` | `docket.formed` (any) | `matter.lapsed` (world) | — | kind |
| C-b (control: the march that meets nobody) | `march.declared` | — | `field.unopposed` or `field.lost` | — | kind |
| C-c (control: a stale store corrected) | `transfer.refused` | — | a `claim.deposited` on the refused actor naming the store | — | kind |
| S-32 a famine | `yield.taken` (world) with a later `body.changed` (world) on a cohort under the same rung | `stores.changed` by an act of another (`transfer`, `requisition`, `exchange`), or `residence.changed` | `weight.changed` on that cohort, or `body.changed` rising | `Person.body`, `Person.weight` | kind+band |
| S-04 a contested succession | `tenure.closed` on a seat | `succession.claimed` or `succession.contested` (other) | `tenure.opened` on that seat | `Tenure.until` | party |
| S-02 a death reported | `person.died` | a `claim.deposited` of it in a ledger whose holder was not present, with a `told_by` chain of length 1 or more | an executed act by that holder with the claim among its causes | — | kind |
| S-43 / S-44 a verdict, an acquittal | `petition.filed` or a case opened | `matter.advanced` or `matter.turned` (other) | `matter.determined` / `matter.dismissed` | `Tenure.since` on a disposal edge | kind+band |
| S-27 a duel | a challenge issued | its acceptance (patient) | the fight's closing Event | `Person.body` | kind+band |
| S-33 blame | `term.matured`, `matter.lapsed` or a dearth Observation | — | an executed `petition`, `speak`, `tell`, `challenge` or `release` by the wronged whose subject is his believed holder (`20_NARRATIVE_B`'s reader) | `Person.stance` | kind |
| S-68 the disaster | any drawn act on a staked row | — | its Failure Event with `shortfall_step` 3 (`23_STORY_A`) | the row's stake field | kind |

Kind names in the last seven rows that do not exist today (`succession.contested`, `matter.dismissed`,
`weight.changed`, the challenge and acceptance kinds as PC names them) are the carrying proposals'; such
a row prints `n/a (no emitter)` until they land, which is the bar reading "absent" honestly.

**3. CLI.** `--stories` prints, per arm: per seed the count and variants of each shape; pooled, the
seeds with one or more, the variant shares, and the instance rendered once per shape per seed by
`chronicle.lines` (so a person can read whether it is that story: NARR-F's third falsifier). Three
switches, each composed from what exists:
- `--world realm|valley`: `valley` calls `harness/valley.py::build` (`07_SE_valley_scenario.md`); the
  default stays the realm;
- `--draw-seeds` (exists, REM-15) for clause C5;
- `--pin-rolls BAND`: a `draw_factory` wrapper, harness-only, under which every graded draw returns
  `BAND`: the planted failure of clause C6. With `--null` the shapes are also counted over
  `edge_null(rows, seed)` (WR's edit 2).

**4. `--seat PID`** (the `seat` argument): the same shapes over one person's ledger: a beat counts only
if that person holds a claim deposited from it. This is S-73's reading (a story a seat can follow) and
`16_PESSIMIST_GO.md` §3.8's *"the story bar from a seat"*.

**5. `engine/season/tests/test_storybar.py`** (the file NARR-F edit 4 opens). Per shape, planted logs:
the full plant reads 1; each single beat removed reads 0; the plant's causes re-drawn by `edge_null`
read 0; a shape with an unemitted kind reads `n/a`. One test asserts that it asserted
(`assert checked >= len(SHAPES)`, §0.1 pt 2). The block changes no hash.

## The gate (execution artifact) — for this proposal, and the form of every batch's

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 3 --arms off off --stories
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 20 --seasons 8 --arms <control> <on> --stories --world valley
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --seasons 6 --draw-seeds 0 1 2 3 --stories
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 6 --arms <on> <on> --stories --pin-rolls Success --null
```

This proposal passes when, on the shipped engine: the first prints EQUAL, the three control shapes
above zero at every seed (clause C0), and every other shape 0 or `n/a`; the planted tests pass; pinned
hashes are unchanged. **That is the bar failing on today's engine for 73 stories and reading the control
set**, which is what makes it a bar. A batch then passes when its stories meet C1 to C6 of the audit's
§6.1 in the second, third and fourth commands.

## The falsifier

- C0 failing: the census cannot see a petition lapse, and nothing it reports is evidence.
- A shape above zero under `--null` as often as on the log: its link is coincidence; tighten the link
  or the shape is not a story.
- A shape above zero in the control arm at the on arm's rate: it counts something the mechanism did not
  cause.
- A rendered instance that does not read as that story to a person: the shape is mis-defined.
- Any content hash moving: the block leaked into the loop.

## NERS reading

- **N.** Without it the enablement plan's claim, *a story occurred*, has no instrument and each batch
  gates on its own link. It is the measure of the audit's central finding. Narrowed in one direction:
  it adds nothing a careful reader of a chronicle could not see by hand, at one seed.
- **R.** It measures the no-player half and, with `--seat`, what one player could follow. Complete: an
  empty log prints zeros and `n/a`; a world with one person prints no `other` beat.
- **S.** One instrument, one made-and-refused rule (`corpus_run.attempts`), WR's null, NARR-F's test
  file, the chronicle's renderer. No second bar.
- **E, last.** About a hundred and fifty lines of harness and one table, against the only reading that
  says whether the seventy-three have become possible. High.

## Cost class

Small build, one session; then one table row and one plant per story, in each batch's own commit.

## Dependency edges

Needs first: `09_WR_story_instruments_that_can_fail.md` (arms, `edge_null`); `20_NARRATIVE_F` (the test
file). Better after: PES-GAME (`standing_occasions_carry_their_cause`), without which a closing act on a
standing occasion has no ancestor and reads as an opening; PES-CORE (the receipt's value) for `cost`;
`07_SE_valley_scenario.md` for `--world valley`. Feeds: every batch of the audit's §6.2; `23_STORY_E`.
Batch E-0.
