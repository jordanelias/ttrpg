# NARRATIVE-F — the story bar counts crossings: an inventory reading, its controls, and the gate the narrative basis must pass

Reconciled: 2026-11-12, U5d closure — folded **A-45**, **A-46** and **A-15**: the gate's story families gain supply the rulings order (a succession by natural death; a split by leaving a creed or head seat; several strands that can each end), so the clauses that read 0 "by ruling" are re-read after those land. No step changes.

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` §4 (the story inventory), §7.2 (the five pulls), §11 (the probe
`narr_probe.py` this reading is lifted from). Composes on, and does not restate, the WR lane's
`09_WR_story_instruments_that_can_fail.md` (forcing arms, the edge null, the shape line) and
`09_WR_B_readings_of_closure_and_tension.md` (close by act against by clock), and the plan's CR-97 (plot
points per strand) and CR-99 (the strife guard as a function). Reference only (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

**Nothing.** Every edit is under `engine/season/harness/`, which no step of the loop imports. No hash
moves. It changes what a run can be asked: not "how many acts had another person's act among their
causes" but "how many times did two of the eleven things pull against each other in one person, and
what did he do".

## The problem, with evidence

- The story bar reads depth of the cause graph and cannot fail (WR F-WR-03). CR-97 reads plot points
  *per strand* (an opening, a turn, a consequence act); a strand is strife, and by season six the realm
  is one strand (WR F-WR-02). Neither reads a person standing on two things at once.
- The audit's probe did, by hand, at seeds 0 to 2 over four seasons, and found the count of every
  crossing class to be zero or a base rate: no grievance for a due unmet (none can exist), no act on a
  seat that reads its holder (H-195), no member acting on his own side's creed, told claims at one
  `commensurate` sign in two seeds of three, changes of conviction unseen. It also found that clearing
  every conviction at build leaves the executed-verb profile within the seed spread (audit §4.3).
- A reading that exists only in a scratch file is lost with the session (`CLAUDE.md` §1), and the five
  proposals `20_NARRATIVE_A` to `E` each name a class of this reading as their gate.

## The resolution, decided

One block added to the instrument that already owns "does the engine produce stories"
(`harness/storybar.py`), printed per seed and pooled, with arms and with a bar that fails today. No
new module: the readings are lifted from the audit's probe onto `storybar.drive`'s existing
`on_season` hook and the person-side functions the other proposals add. Ladder step 4 (`harness/loops.py`
reads its per-season quantities through the same hook; `strands_block` is the precedent for a block
behind a flag).

## Exact edits, by owner

**1. `engine/season/harness/storybar.py` — `crossings(w, d, bounds, snaps) -> dict`, behind
`--crossings`.** `snaps` is a per-season snapshot taken in `on_season` of the person-side readings (so
a pull is read as it stood when the act was formed, never from the end state). Classes, each counted
over **executed** acts (`corpus_run.attempts`, the one owner of made and refused):

| class | counted when | reads |
|---|---|---|
| G1 a due unmet, answered | an act by `p` whose subject is `x`, within two seasons of a snapshot in which `dues_unmet(p, x) > 0` | `20_NARRATIVE_B` |
| G2 a stand against his own side | an `argue`, `release` or `commit` by `p` whose subject is his own faction's creed (or, for `commit`, another faction's) while `opinion_of(w, p, own) < 0` in the last snapshot | `20_NARRATIVE_D` |
| G3 a new holder meets an old oath | an act by `p` on a seat he is sworn to, within two seasons of his `believed_holder` of it changing | `20_NARRATIVE_C` |
| G4 an enemy with a place | a contested act (the row declares `contests:`) by `p` on a seat or rung whose `believed_holder` he regards below 0 | `20_NARRATIVE_C` |
| G5 across a fault line | an act whose occasion is a told claim, split by `commensurate(hearer, last teller)`: −1, 0, +1 | `20_NARRATIVE_A` |
| G6 a creed broken and seen | a `conviction.moved` Event with at least one deposit in a ledger other than the person's | `20_NARRATIVE_E` edit 3 |
| closes | closing Events by act and by clock | `09_WR_B_readings_of_closure_and_tension.md` (called, not restated) |

Until a proposal lands its class prints `n/a (no reader)`, never 0: an absent reading is not a zero.

**2. The same block prints three lines the audit used and no instrument has:**
- *occasion of the strife verbs*: for `march`, `challenge`, `seize`, `raze`, `arrest`, `petition`,
  `oblige`, `release`, the five commonest `(question source, claim predicate)` of formed and of executed
  acts (the audit's "a challenge formed because the harvest came in");
- *world Event → executed act*, by world kind and verb (what the churn elicits);
- *the reign*: `(year, season of year, believed holder of the realm's head seat by plurality of
  ledgers)` per season, for the chronicle's date line (`09_WR_B_chronicle_that_tells.md` prints it; no
  state is stored, and "by plurality of ledgers" is said in the line, since no world truth is read).

**3. Arms.** `--arms` takes WR's mapping (`off`, `weather`, `bodies`, `lattice`, `all`) and gains two
ablations, composed from fixtures and a builder switch, each a control this lane's gate needs:
`noconv` (every `Person.conviction` cleared at build: `decision_spread.apply_control`'s precedent for a
build-time ablation) and `basis_off` (every fixture of `20_NARRATIVE_A` to `E` at its control).

**4. `engine/season/tests/test_storybar.py`.** Planted logs, one per class: a planted lapsed oath, a
believed holder and an act on him reads G1 = 1; with the belief removed, 0. A planted told claim across
an incompatible pair reads G5(−1) = 1. A class with no reader prints `n/a`. The block changes no hash.

## The gate (the bar; it can fail, and it fails today)

Run, `PYTHONHASHSEED=0`, one process per seed and arm:

```sh
python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 6 --arms basis_off on --crossings --executed-only
python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 6 --arms on noconv --crossings --executed-only
python -m engine.season.harness.storybar --base-seed 0 --seasons 6 --draw-seeds 0 1 2 3 --crossings
python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 3 --arms off all --executed-only
python -m engine.season.harness.strife 4 0 1 2 --strands
```

(`on` is every `20_NARRATIVE` fixture at its proposed live value.) It passes when all of these hold:

1. **A control.** Under `basis_off`, G1 to G4 and G6 read 0 at every seed, and G5 counted between two
   persons who both hold a conviction has one sign at three seeds of five or more (today's reading,
   reproduced). If `basis_off` shows crossings, the reading is counting something else.
2. **Non-degenerate.** Under `on`, pooled over five seeds: at least four of the six classes are above
   zero at three seeds or more; no class holds more than 60% of all crossings; G5 between two convinced
   persons shows all three signs.
3. **Not one run.** The five seeds' class vectors are not all equal, and at least three are distinct.
4. **Not a fixed function of state.** On one built world, the class vector differs between at least
   two of four draw seeds (the chooser's sample and the contests' rolls are what moved it).
5. **The modifiers are load-bearing.** Under `noconv`, G5's −1 and +1 counts and G6 fall to zero and
   G2 falls; if the `on` and `noconv` vectors are within the `on` arm's seed spread, conviction is
   still inert and the bar fails.
6. **Closures by persons.** Closing Events by act exceed closing Events by clock at two seeds or more
   (WR `_B`'s falsifier, adopted as a clause).
7. **WR's bar.** `off all` prints DIFFER with more deaths in `all`; `off off` (run inside the same
   command set) prints EQUAL; the chain reading prints its edge null.
8. **The strife guard.** Over `basis_off` against `on`: every terminal code reached off is reached on,
   and no code's share rises by more than the off arm's seed spread; BLIND (fewer than two codes off) is
   reported as BLIND and the guard is re-read at the horizon the plan's risk 8 names.

**Today** clause 1 holds and clauses 2, 5 and 6 fail (audit §4: every crossing class zero or one-signed;
`noconv` within the spread; 23 closes by clock against 3 by act, WR `_B`). That is the bar failing on
the shipped engine, which is what makes it a bar.

## The falsifier

- Clause 2 passing under `basis_off`: the classes are too loose (they count coincidence). Tighten the
  windows, or the class is not a crossing.
- Clause 4 failing with clause 2 passing: the crossings are scripted by the build (the same people
  cross the same lines every time): the pulls are reading authored state only, and nothing in play
  moves them.
- A class above zero whose acts, read in the chronicle, do not read as that story to a person: the
  class is mis-defined. One rendered instance per class per seed is printed for exactly this check.

## NERS reading

- **N.** Without it, each of five proposals gates on a private reading and the claim "the engine now
  produces crossings" has no instrument. It is the measure of the audit's central finding.
- **R.** It measures the no-player half and nothing else. Complete: an empty world prints `n/a` and 0.
- **S.** It lives in the one story instrument, uses the one made/refused rule, the one closure reading
  and the one strife guard; it adds no second bar beside WR's.
- **E, last.** About a hundred lines of harness for the only numbers that say whether eras, regimes and
  strife meet allegiance, office, obligation, pursuit and conviction in anyone. High.

## Cost class

Small build, one session; clause by clause it can only be read as the proposals it gates land.

## Dependency edges

- **WR:** `09_WR_story_instruments_that_can_fail.md` (arms, edge null: needed first),
  `09_WR_B_readings_of_closure_and_tension.md` (clause 6), `09_WR_B_chronicle_that_tells.md` (the
  rendered instance and the reign line), `09_WR_strand_conclusion.md` (clause 8 needs strands that can
  conclude).
- **Plan:** CR-97 (its per-strand plot points print beside this per-person block; no column is
  duplicated), CR-99 (clause 8), CR-90 (the arc instrument reads bands and wars; this reads persons).
- **FA, CHAR, FI, SC:** every class needs the closing and redress verbs to execute: `13_SC_draw_for_unrolled_contests.md`
  (petition, covenant), `06_FA_decree_binds.md`, `06_FA_seat_terms_and_turnover.md` (G3's supply),
  `02_CHAR_offer_what_can_be_done.md` (fewer foreseeable refusals), `08_FI_02_rumour-that-travels.md`
  (G5's supply), PC's `challenge`/`accept`.
- **CORE:** `01_CORE_reason_trail_in_the_act_store.md` (the Scene the occasion lines read survives the
  driver).
