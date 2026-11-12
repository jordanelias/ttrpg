# WR · Readings of closure, open situations and idleness, and character ablation as a standing control

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` (A-80, A-81). Nothing here is deleted. (1) Beside edit 3's `idle` line, `storybar --null-scenes` (`30_WR_E_cascade_chains_and_the_census.md` instruction 1) counts acts that left no durable write: idleness is a person with no act; a null scene is an act with no trace. This lane's probe read 59 of 821 at seed 0, one season, all refused inquiry verbs. (2) Edit 1's `closes` (by act, by term, by threshold) is the reading clause C12 uses, and a strand's closure is printed with its state (`open`, `concluded`, `dormant`, `revived`; `30_WR_C` commit 2). (3) Edit 2's `situations` are what an entrenched world must keep producing: the entrenched arm (`30_WR_E` instruction 2) prints them beside the free arm. (4) Edit 4's `flat` control stays the control for character; the pressure-off arm `custom_off` (`30_WR_G`) is a different control and does not replace it.

Reconciled: 2026-11-12, U5d closure — folded **A-45**. The readings count strands as several (the bounded link of `09_WR_strand_conclusion.md` edit 3 is the ruled form), so "closed by act / by clock" (edit 1) is reported per strand and the one-river reading is kept as the control column.

## Status: PROPOSED

Carries findings F-WR-13, F-WR-15, F-WR-16 and F-WR-21 of `audits/09_WR_audit_addendum_B.md`, its
resolutions R-29 and R-30, and steps 1 and 7 of its §3.8. Evidence ids (EB-nn) are that file's §9; E-nn are
the first audit's §12. Adds to the first lane's `09_WR_story_instruments_that_can_fail.md` and supersedes
nothing in it.

## What it changes in `engine/season/` at runtime

**Nothing.** Every edit is a reading under `engine/season/harness/`, which the loop never imports. The
gate's first line is that `build_realm(0)` and the one- and two-season hashes are EQUAL.

## The problem

1. **The engine cannot tell an ending someone did from one a clock did.** Over six seasons at seeds 0 to 2,
   `matter.determined` (an act) occurs 1, 2, 0 times and `matter.lapsed` (MATTER, at `docket_lapse` 4) 8, 8, 7;
   the season-5 `tenure.closed` spike (27, 27, absent at the seed whose duties were taken a season late) is
   the `oblige_term` maturing (§3.2, EB-02). The first lane's strand-shape reading counts `closed` as one
   thing. A world whose closures are expiries has the eventfulness of none of Schmid's properties as
   Lessard and Paré-Chouinard use them, and nothing in the tree says so.
2. **Nothing reads what is open between whom.** No function under `engine/season/` computes a set of open
   conflicts (EB-03). The pieces exist as per-person World-first stampers in `queries/world_q.py`:
   `vacancies` (`:3121`), `holdings_to_found` (`:3524`), `at_war` (`:3566`), `detainees_held` (`:3602`),
   `matters_awaiting` (`:3633`), `ambitions` (`:2797`), and the docket through `docketed` (`:208`).
   Narration-mechanisms §3.4 said starvation "is detected outside the sim, as a group-by over
   `storybar.read` rows"; no such group-by exists. Apparatus rows F3 and F4 (a tension variable with named
   inputs; an alarm when suitable content runs out) have no observable.
3. **The wear signal is mostly zeros.** 248 of 322 Sites are wear-0 kinds and emit a `condition.worn` of no
   change every season (EB-07, F-WR-21). Any count of world motion over the log reads 322 where 74 moved.
4. **The one control that asks whether character matters is not standing.** Flattening every person to the
   realm mean (`harness/decision_spread.py::apply_control`, `no_goals()`) lowers no story reading at two
   seeds and raises the world-changing ones (§3.5, EB-01). That was found by a scratch probe; no instrument
   in the tree runs it.

## The resolution, decided

- **A close is classified by its emitter, structurally (R-29).** `SeasonDriver.act_of` maps every Event an
  act's fold emitted to that act, and nothing else. A closing Event is **by act** when `e.id in act_of`,
  and **by clock** otherwise (MATTER's own emission: a term maturing, a matter lapsing, a body falling),
  even when its causes walk back to the act that declared the term. A closing Event is one whose Receipts
  write a *closing cell*: `("Tenure", "until")`, `("Person", "exists")`, `("DocketItem", "matter")`,
  `("Rung", "exists")`, `("Office", "exists")`. The set is declared once, in `harness/arc.py` beside
  `ARC_SELF` and `ARC_WORLD` (the one owner of which cells a story reading counts), and asserted at import
  to be a subset of their union plus `("Person", "exists")`.
- **A situation is a referent stamped for two or more persons, or a stamp that names another person's
  edge** (§3.1's definition, computed from the stampers that already exist; no new World read). Four kinds,
  each one existing stamper: `seat` (`vacancies`, and `ambitions` naming an Office), `matter`
  (`matters_awaiting`), `custody` (`detainees_held`), `war` (`at_war` over the faction pairs of persons
  present together). A kind with no stamper is not invented here.
- **A wear Event counts as motion only when its change is non-zero; a crossing counts as an incident
  (R-30).**
- **The ablation is a control of `storybar`, beside its forcing arms, not a forcing arm.** It changes who
  the persons are, not what the world does; the ARMS tuple stays the forcing roster.

## The edits

### Edit 1 · closes by act and by clock (`engine/season/harness/arc.py`, `harness/storybar.py`)

`arc.py` gains:

```python
CLOSE_CELLS = frozenset({("Tenure", "until"), ("Person", "exists"), ("DocketItem", "matter"),
                         ("Rung", "exists"), ("Office", "exists")})

def closes(log, act_of: dict, bounds: list) -> list[dict]:
    """Per season: {"by_act": Counter(kind), "by_clock": Counter(kind)} over Events whose Receipts write a
    CLOSE_CELLS cell; by act iff the Event's id is in `act_of` (the fold emitted it). Reads only."""
```

`storybar.main` prints, under the existing per-season block, one line per season:
`closes season=<s> by_act=<n> by_clock=<n> (term=<n> threshold=<n>) | <kind=n, …>`.

**The clock half is split by the brief's standing rule ("we do not do deterministic").** A close *by term*
is a Tenure whose `until` was set by a declared `Term` (the declaring act chose the length; MATTER only
counts seasons): bookkeeping, which the rule permits. Every other MATTER close is *by threshold*: a matter
lapsing at a fixed age (`docket_lapse`, H-356), a body falling to its last floor, a band crossing that ends
a use. Each is a consequential outcome fixed by state, which the rule forbids; the reading names them so
the owners' repairs can be seen (the line should read `threshold=0` once lapse, death by body and wear are
drawn: SC for the docket, PC/CHAR for the body, WR for wear,
`09_WR_B_draws_not_thresholds.md`). The split is structural: a closing Event whose causes include a
`Term`'s declaring act through `Tenure.term` is `term`; any other non-act close is `threshold`. `strife.py`'s strand-shape line (the first lane's
edit) splits its `closed` count into the same two, by calling `arc.closes` and not by re-deriving it.

### Edit 2 · open situations and the wear rule (`engine/season/harness/storybar.py`)

```python
def situations(w) -> dict:
    """At a season boundary: {kind: frozenset(referent)} for the four kinds above, each a referent stamped
    for two or more persons by its one World-first stamper (or, for `war`, a pair `at_war` admits among
    persons present at one rung). Composes on `world_q`'s stampers; reads only; calls no `new_draw`."""
```

`drive`'s existing `on_season` hook carries it: `storybar.main` gains `--situations`, which collects
`situations(w)` after each season and prints per season `open=<n by kind> opened=<n> gone=<n>`, and
`motion=<non-zero condition changes> crossings=<condition.band_crossed>` (R-30: a `condition.worn` Event
counts only when its Receipt's before and after differ). No pass bar, no threshold: the block is a
reading, as `--chains` is.

### Edit 3 · idleness (`engine/season/harness/storybar.py`)

The same block prints `idle=<persons with no executed act this season> of <persons>` and
`idle_two=<persons idle two seasons running>`, computed from `read(...)["executed"]`'s `actor` field. This
is narration-mechanisms §3.4's group-by; nothing in the loop reads it (strife R1: nothing steers).

### Edit 4 · character ablation as a standing control (`engine/season/harness/storybar.py`)

`storybar.main` gains `--control {none,flat}` (no default other than `none`, which is today's reading;
the seed and season count stay required, `tools/ci_sim_fabrication_check.py`'s scope). `flat` builds the
realm with `build_realm(seed, goals=False)`, calls `decision_spread.apply_control(w)`, and runs `drive(...,
world=w)` inside `decision_spread.no_goals()`. Every reading above, `--chains` and the act mix print for
both. `decision_spread` does not import `storybar`, so the edge adds no cycle.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 6 --arms off --situations
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off --control flat --situations
python -m pytest engine/season/tests/test_storybar*.py engine/season/tests/test_in37_chronicle.py -q   # covering files, at the close
```

Passes when: (1) at seeds 0 to 2, six seasons, `threshold` in season 5 reads at least the `matter.lapsed`
counts of EB-02 (8, 8, 7), `term` the matured `oblige` terms, and `by_act` the `matter.determined` ones; (2) a planted world with one
`determine` executed and one matter left to lapse reads `by_act=1 by_clock=1`; (3) a planted world with two
persons stamped on one vacant seat reads `open seat=1`, and one person alone reads 0; (4) `motion=` reads 74
Site writes a season at seed 0 where `condition.worn` reads 322; (5) the flat control reproduces EB-01's
hashes (`1e202aff…` at seed 0, `e48c989e…` at seed 1); (6) `build_realm(0)` and the one- and two-season
pins are EQUAL with and without each flag.

## The falsifier

A season with `by_act + by_clock` different from the number of Events writing a closing cell (the split
lost one); a `situations` call that moves the content hash or the draw ordinal (it read the World
lawlessly); a `flat` control whose hash equals the shipped arm's (the control did nothing).

## NERS reading

- **N.** Without these, "the world generates drama when nobody is watching" has no observable, and F-WR-13
  was found by hand. Holds top-down (the realm's shape over six seasons), bottom-up (one planted matter,
  one planted seat) and laterally (SC's, FA's and CHAR's closing verbs are judged by the same `by_act`
  line).
- **R.** The no-player half becomes measurable; completeness at the extremes is the planted worlds of the
  gate.
- **S.** One closing-cell set, one emitter rule, the existing stampers, the existing `on_season` seam and
  the existing control. No second definition of "closed" and no second control.
- **E, last.** Four readings and one flag, against the two apparatus rows a no-GM design is asked first.
  High: what it adds is legibility of what already happens.

## Cost class

Small build (harness only), hash EQUAL.
