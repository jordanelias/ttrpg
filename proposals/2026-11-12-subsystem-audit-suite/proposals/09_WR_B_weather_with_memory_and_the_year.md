# WR · Weather with memory and neighbours, a journey priced before it is chosen, and the Rupture as an ending

## Status: PROPOSED

Carries findings F-WR-19 and F-WR-20 of `audits/09_WR_audit_addendum_B.md` (§5.3, §5.4), its resolutions
R-23, R-26 and R-27, and step 4 of its §3.8. Sits beside the first lane's `09_WR_world_motion.md` (the
wound at Askeheim, occupation of unheld land, the settled-territory victory selector) and supersedes none of
it. CP-T10-03's per-season terms (`season_terms`: yield, want, illness by season of the year) stay the
plan's (B10-18) and are not restated here.

## What it changes in `engine/season/` at runtime

- **Edit 1, edit 2:** nothing at the shipped fixtures. Both are new or changed *arm* values; the control
  (`season_factor_draw = ()`, `season_spell_draw = ()`) is today's tree, byte-identical. When B10-18 flips
  the weather arm, the flip's hash movement is the plan's declared mover, and these edits change what it
  moves to.
- **Edit 3:** nothing until `route_pricing` flips (CP-T10-01 ships it off).
- **Edit 4:** nothing: a loader grammar and a Query branch, with no roster row using them.

## The problem

**The scheduled weather cannot make the incident the design names** (a drought, then a famine; strife
opening A, natural shock). `queries/world_q.py:1178-1205`, `season_factor_of`: the factor is
`season_factor × choice(season_factor_draw[season_of_year])`, drawn from `draw_factory(world_seed, tick)`
keyed on the territory. Read off the code (F-WR-19):

- *no memory:* `tick` is in the key, so successive seasons are independent; with the swept arm
  `((0.5, 1.0, 2.0),) * 4` (`data/fixtures.py:535`'s comment) two low seasons in a row come one time in
  nine;
- *no neighbours:* the territory is in the key, so adjacent territories draw independently and relief from
  next door is almost always there;
- *a mean above one:* (0.5 + 1.0 + 2.0) / 3 = 1.167, and yield is linear in the factor
  (`modules/settlements/produce.py:19`), so the arm raises the long-run harvest by a sixth over its control
  in a realm whose stores already grow (#457 §8, not re-measured here).

The year itself is half-built, which the addendum's §5.1 understated: `season_of_year(w)` (`:1169-1175`)
reads the season of the year as `tick % len(season_factor_draw)`, so a declared table *is* the calendar.
What is absent is everything a season of the year should change besides yield (EB-06: `season_terms`,
`year_length` in no file).

**A journey's price is invisible to the person choosing it.** CP-T10-01 ships `route_pricing` off with
"[GAP: unowned]: no position gives a chooser a person-side reading of a leg's price". Today every leg costs
one scene point; `move` executes 21 of 78 at seed 0 over three seasons with 77 `travel.blocked` (§5.2).

**The world's survival has no end.** `rosters.yaml: endings`' grammar is `{post: …}` or `{rung_kind: …}`
(`data/rosters.py:1444`, `ENDING_SELECTORS = ("post", "rung_kind")`; `world_q.py:2675-2683`), selectors over
holds, so the design's survival terminal (the Rupture: "all factions lose", `wc_survival_spine.md`;
`threadwork_v30.md` §5.3, intent only) cannot be written (F-WR-20).

## The resolution, decided

- **R-27 · a spell.** Weather gains a second keyed draw on a coarser clock and a coarser place: the
  **year** (`tick // len(season_factor_draw)`) and the territory's **parent rung** (`state/containment.py::parent_of`, the
  one owner `state/gate.py` already imports). The spell is a multiplier drawn once per (seed, year, region), shared by every
  territory under that region for the whole year; the season's own draw stays per territory and per
  season. Factor = `season_factor × spell × choice(season entry)`. Duration and neighbourhood come from the
  key, and no state is stored: the spell a territory is in is a function of `(world_seed, year, rung)`, as
  the season of the year already is.
- **Mean one.** Every arm's members are chosen with arithmetic mean one, so a forcing moves variance and
  not the long-run harvest. A bias, if wanted, is `season_factor` (the constant), declared as such.
- **R-23 · the leg's price is not world state.** It is a pure function of two settlement ids and the
  loaded geography (`data/geography.py`'s adjacency and terrain matrices: identical for every person,
  changed by no act). `decision/budget.py::budget(p, v, k, fx)` (`:18`) already takes `fx` on exactly that
  ground (`:53`: "not world state"). The price is handed to `decision/` beside `fx`; whether the road is
  open stays a World read at the fold, and a priced journey refused there is `travel.blocked`, which is how
  a person learns the road is shut. No person-side World read is introduced.
- **R-26 · an ending over the condition of Sites.** The grammar gains `{site_band: <band>, of: <site kind
  or all>}`, reached when every selected Site under the realm reads at or below that band of its kind's
  `band_floors`. A row using it carries `victory: false` and no `under:`. #457's END-VICTORY handle rules
  the form ("a Query over holds and seats that the season reports, never an actor"); the cut that removed
  the stored stability scalar (#457 §5) changes what the Query reads, not whether the ending exists. The
  roster's act-credit clause is not applied: a ruin nobody caused is what the row reports. **The row itself
  (which band, which kinds) is Jordan's content and ships absent.**

## The edits

### Edit 1 · the spell (`engine/season/data/fixtures.py`, `queries/world_q.py::season_factor_of`)

`fixtures.py`, beside `season_factor_draw`:

```python
    season_spell_draw=(),        # R-27: the year's regional multipliers, equally likely, mean one;
                                 # swept () (control) / (0.6, 1.0, 1.4)  [ASSUMPTION; medium; Jordan to correct]
```

`season_factor_of` gains, after `s = season_of_year(w)` and before the season draw:

```python
    spells = w.fixtures.get("season_spell_draw")
    spell = 1.0
    if spells:
        year = w.tick // len(w.fixtures.get("season_factor_draw"))
        region = parent_of(w, territory) if territory else None   # `state/containment.py`; "world" if none
        region = region or "world"
        spell = draw_factory(w.world_seed, lambda: year)(region, "season_spell").choice(spells)
    return base * spell * draw.choice(outcomes)
```

A spell table with no season table refuses at load (a spell needs a year to last). The docstring's
"two territories at one tick draw independently" becomes "their season draws are independent; their spell
is shared when they share a parent rung".

### Edit 2 · arm members with mean one (B10-18's arm, `fixtures.py:535`'s sweep comment)

The swept live arm `((0.5, 1.0, 2.0),) * 4` becomes `((0.5, 1.0, 1.5),) * 4`. One value moves; the
control is untouched. Recorded in the B10-18 card as the arm it flips to. `[ASSUMPTION; medium; Jordan to
correct; revert: restore 2.0]`

### Edit 3 · the leg's price reaches the chooser (`decision/budget.py`, `loop/driver.py`)

`route(a, b)`'s cost (CP-T10-01, over the loaded geography) is exposed as `leg_price(a, b, geo) -> int`, a
pure function in `data/geography.py`. The driver hands `geo` to `choose` beside `fx`, as it hands `k`.
`decision/` prices a `move`/`travel` candidate with it when `route_pricing` is on and charges one point
when it is off (today). No `World` crosses: `test_w5_sense_is_still_the_only_world_taking_non_decision_function`
stays green. The flip of `route_pricing` then waits only on its own paired arm.

### Edit 4 · the `site_band` selector (`data/rosters.py`, `queries/world_q.py::_ending_edges`)

`ENDING_SELECTORS = ("post", "rung_kind", "site_band")`. The loader admits `site_band` with a required
`of:` (a `site_kinds` member with non-empty `band_floors`, or `all`, meaning every kind that has floors) and
refuses `under:` beside it, refuses `victory: true` with it, and refuses a band name not in the kind's
floors. `_ending_edges` gains the third branch: the Sites under the realm of the selected kinds, each
compared with the floor of the named band; the edges returned are the Site ids, and `endings_reached`'s
antecedents are the `condition.band_crossed` Events that took each Site there. The roster's prose head
gains one sentence naming the selector. **No member row is added.**

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 0          # control: hashes unchanged (one short run)
python -m pytest engine/season/tests/test_season_weather.py engine/season/tests/test_season_weather_per_territory.py \
       engine/season/tests/test_in27_endings.py -q                     # covering files, at the close
```

Passes when: (1) every control reproduces `build_realm(0)` and the one- and two-season pins; (2) under
`season_spell_draw = (0.6, 1.0, 1.4)`, two territories under one parent rung read the same spell in every
season of a year and may differ the next year, and two under different parents may differ in the same
season; (3) the spell is a function of `(seed, year, region)` only (same inputs, same spell, from two
processes); (4) under the live arm with spells, at three seeds over eight seasons, at least one territory
reads `shortfall` in two consecutive seasons, using CR-73's reading (`[UNVERIFIED]` until run; the
falsifier below says what failing looks like); (5) a planted world whose every harbour sits below its
lowest floor reports a planted `site_band` row, and reports nothing with one harbour above it; (6) the
loader refuses `site_band` beside `under:` and beside `victory: true`.

## The falsifier

For edit 1: the spell differs between two territories of one region in one season (the key leaked the
territory), or is the same for every year (the year is not in the key). For edit 2: the realm's stores at
season 8 under the live arm exceed the control's by more than the control's own seed-to-seed spread. For
edit 3: any `World` reaching `decision/`. For edit 4: a `site_band` row reached while any selected Site
stands above its band.

## NERS reading

- **N.** Without a spell the scheduled weather is a one-season event by construction (apparatus C9;
  Sylvester's "the richness comes when several events interact"), and the strife study's natural-shock
  opening cannot occur. Without the ending, the survival contest the design calls the game's strategic
  architecture has no loss. Holds top-down (a region's bad year), bottom-up (a governor relieving his own
  settlement), laterally (SE's larder, FA's `transfer` and `requisition`, SC's `petition` at the shortfall
  rung) and diagonally (a regional famine reaching a seat's vacancy through deaths under the illness arm).
- **R.** Drama with nobody watching: a dry year in one duchy makes "whose grain" into "there is no grain
  nearby". A priced journey makes going yourself or sending someone a strategic choice.
- **S.** One draw primitive, one more key; the year already read off the table's length; the leg's price
  on `fx`'s precedent; the ending on the roster's own grammar. Calculations consistent: the spell and the
  season draw are both multipliers on the one factor owner.
- **E, last.** Two fixture values, one keyed draw, one pure function and one selector, against the
  incident the design names first and the end it names last. High.

## Cost class

Edits 1, 2: edit (data and four lines). Edit 3: small build. Edit 4: small build, no row.
