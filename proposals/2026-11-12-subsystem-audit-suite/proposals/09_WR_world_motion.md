# WR · The world moves, and its endings can be reached

Reconciled: 2026-11-12, U5d closure — folded **A-40**, **A-54**, **A-55** and **A-57 / A-58**. Edit 1 (the Calamity's source as an authored initial condition): A-40 rules the wearing-down a real condition of places, one Site per territory, no new entity kind, so the source is a Site of the territory and the edit's form stands; its flip waits on `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edits 1–2 (`U5d_WR_owed_edits.md` §2) and its wear is drawn on the four-band ladder (A-54). Edit 2 (an unheld place is taken by occupation) stands: ground no party holds is outside the land ruling, so `seize` remains its act. The note under edit 3 ("`seize` admits a held, occupied territory") is rewritten: held land is taken by `seize` on the occupation licence, as the note says, by a victor who chooses to (A-66), and the seats anchored on it pass with it (`U5d_FA_land_and_seats_pass_on_a_won_march.md`); a faction present by the holder's leave does not occupy. Edit 3's victory selector counts places on the fixed map (A-55) and is reached by a draw.

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 (A-15 rules natural death on, after the 46 ages are authored): the Status sentence "decided by nobody but Jordan" and edit 4 now carry A-15's condition (`age_at_build` authored first by `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edit 1, per `U5d_WR_owed_edits.md` §2 (c); then `illness_rate`/`age_step` flip as one declared mover); C3-N1 (the territory count gets its qualifier, T-8); tier and batch added (R3 7b-0; U3 B12, edit 4 with B37).

## Status: PROPOSED

Lands in batch: B12 (world motion and ground) for edits 1–3, **before** `09_WR_B_draws_not_thresholds.md` edits 1–3, which re-mechanise this file's edit 1 crossing and edit 3 reaching on top of the wound row and the settled selector (U6 R-A, `U3_DEPENDENCY_ORDER.md` §1.2); edit 1's `lattice_coupling` flip after `16_PESSIMIST_WR_B` edits 1–2 in the same batch; edit 4's flip in B37 (happenings) after `22_HAPPENINGS_A` edit 1.
Depends on: nothing proposed for edits 1–3 (the draws file depends on this one, not the reverse); `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edits 1–2 (B12) for edit 1's coupling flip; `22_HAPPENINGS_A` edit 1 (B37, the ages) for edit 4.

Carries findings F-WR-04 and F-WR-06 of `audits/09_WR_audit.md`, and its §6 resolutions R-03, R-04, R-05
and R-07. Evidence ids (E-nn) are that file's §12. Edit 4 (natural death) is ruled: A-15, on after the 46
ages are authored.

## What it changes in `engine/season/` at runtime

Three things, each its own declared hash mover with a control arm that reproduces the base hash:

1. the lattice coupling has a source in the built realm, so a non-zero `lattice_coupling` moves a front
   outward from Askeheim instead of dragging every territory alike (edit 1);
2. a place nobody holds can be taken by the faction that occupies it (edit 2), so land a dead holder
   leaves does not stay unheld for ever;
3. the victory row selects the fifteen settled territories, so it can be reached (edit 3).

Edit 4 (natural death off the control) and CL-EVENTS commit (2) (the weather draw, already scheduled in
B10-18) are the other two motions; neither is built here.

## The problem

The design's own frame is two contests at once: who governs the peninsula, and whether it survives
(`victory_v30.md` "Core Frame", intent only). In code the second contest has machinery and no motion, and
the first has an ending nobody can reach.

| observation | run or line |
|---|---|
| `season_factor_draw=()`, `age_step=0.0`, `illness_rate=0.0`, `lattice_coupling=0` | `data/fixtures.py:535,690,691,700` |
| shipped fixtures, seed 0, three seasons: 0 deaths, 0 band crossings, `restore` attempted 0 times | E-07 |
| coupling 250 with **no source**: still 0 band crossings and `restore` attempted 0 times in three seasons | E-11, E-16 |
| T15 holds no Site, no settlement, no holder; `build_realm` mints Sites at settlements and hearths only | E-13; H-236 |
| a holder's death closes his `hold`; no verb opens a hold on a place nobody holds | `state/world.py::remove_person`; `effects_information.py:1061`; H-166, H-186 |
| with forcing on, three seasons: unheld territories stay at 1 at seeds 0 and 1 (no land-holder died); vacant offices go 0, 3, 5 of 35 at seed 0 and 0, 0, 1 of 34 at seed 1; one hold is opened in each run | E-16 |
| `peninsular_sovereignty` selects 16 territories (`T16` excluded; `T15` unsettled; C3-N1, T-8); 15 are settled and held at build; GD-1 and the design both say 15 | E-13; `rosters.yaml: endings`; `victory_v30.md` §0 (intent) |

## The resolution, decided

**The Calamity's source is world truth, authored once; its spread is the rule already built; holding it
back is persons' acts already built.** #457's gate is answered (D1: a consequence of held configurations
failing; D-3: tensile), and canon states the wound at Askeheim as a standing fact. A standing fact is an
initial condition, which is data. What an act adds to it (a working's strain) is B10-15's and waits there.

**An unheld place is taken by occupation.** `seize`'s licence is already occupation
(`_seize_rung`: "THE LICENCE IS OCCUPATION"); the one decline that makes unheld land permanent is "nobody
holds the settlement (H-166: who holds an unheld place is unruled)". Ladder step 4, precedent: the rule the
effect already states for held land is the rule for unheld land. The second half of that decline (the
seat's own faction already holds it) stays.

**Victory counts settled territories.** Ladder step 3: GD-1's own number.

## The edits

### Edit 1 · the wound at Askeheim (data, and one build switch)

Owner: the geography registry `harness/populated.py::build_realm` reads (the same file whose
`radiation_bands:` and `adjacency:` blocks `data/geography.py` already loads). Add to T15's row:

```yaml
    wound: {kind: <a `site_kinds` member that has `band_floors`>, condition: 0}   # [ASSUMPTION; medium; Jordan to correct; revert: delete the row]
```

`build_realm(wound=False)` (the idiom of `guards=`, `foreign=`, `tensions=`) mints that one Site on
`terr_T15` when the switch is on. Off, the realm is byte-identical. The kind is Jordan's content; the
falsifier world of `test_in35_lattice_coupling.py` used a harbour, which is a precedent for the test and
not a claim about Askeheim.

Then, as its own commit and its own mover: `lattice_coupling` 0 → 250 (H-235's swept arm) with `wound=True`
the default. H-235's unblock names a second precondition, the wear-0 kinds (dwellings and garrisons ride
down behind worn kinds with no rate of their own); that is H-165/H-07's and is not decided here, so the flip
waits on it. The switch and the row do not.

### Edit 2 · an unheld place is taken by occupation (`engine/season/loop/effects_information.py::_seize_rung`)

The decline "nobody holds the settlement (H-166 …) or the seat's own faction already does" becomes "the
seat's own faction already holds it". With no closure to make, the write is the opening alone, admitted by
`T-m`; `may_seize` is asked only when there is a holder to seize from. Docstring bullet rewritten to match;
H-166's and H-186's cites updated at their rows.

What this does not do: it gives no one a reason to march on unheld land. `march` forms on a `Rung` a
person's ledger names (`places_named`), and a death at a place deposits claims naming it (H-206), so the
occasion exists where someone saw the holder die.

### Edit 3 · victory counts settled territories (`engine/season/rosters.yaml: endings`, `queries/world_q.py::_ending_edges`)

```yaml
      peninsular_sovereignty:
        victory: true
        holds: {rung_kind: territory, settled: true}     # was {rung_kind: territory}
```

`_ending_edges`' `rung_kind` branch gains one conjunct when the row says `settled: true`: the rung has a
`settlement` rung among its `descendants`. The loader (`ENDING_SELECTORS`) admits the optional key and
refuses any other. The row's `assumption_note` drops "UNREACHABLE IN COMPUTED PLAY whoever holds what" and
keeps the three clauses that have no carrier (Accord, Turmoil, two Accountings). H-176's cite is corrected:
`march_target_kinds` is `[settlement, territory]` and `seize` admits a held, occupied territory.

A structural predicate, not an entity: no territory id is named.

### Edit 4 · natural death (ruled A-15: on, after the 46 ages are authored)

ED-IN-0317's deferral is superseded by A-15. The order: first `age_at_build` is authored for the cast
(`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edit 1, per `U5d_WR_owed_edits.md` §2 (c); the
research lane file's T-WR-8: no source authors an age, so ageing from 0 at tick 0 would be a different
mechanism); then `illness_rate` and `age_step` flip in `data/fixtures.py` together, as **one declared
mover** in their own commit (values from H-208's row and `22_HAPPENINGS_A`, one fixture set, U1 ledger
F-42). The evidence that bears on the size: with `illness_rate` 0.05, deaths over three seasons go 0 → 8
(seed 0) and 1 → 4 (seed 1), `tenure.closed` 2 → 10 and 6 → 8, `oblige` executed 42 → 146 at seed 0
(E-11, E-12).

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 4 --arms off lattice   # after 09_WR_story_instruments edit 1
PYTHONHASHSEED=0 python -m engine.season.harness.strife 4 0 1 2 --strands
PYTHONHASHSEED=0 python -m engine.season.harness.aperture 4 0                                                   # the `restore` and `seize` lines
python -m pytest engine/season/tests/test_in35_lattice_coupling.py engine/season/tests/test_in27_endings.py -q  # covering files, at the close
```

Passes when: (1) with the wound and coupling 250, `condition.band_crossed` appears in the territories at
breadth-first distance 1 from T15 before any at distance 2, and `restore` is attempted and executed at
least once at a crossed Site; (2) with edit 2, a planted unheld settlement occupied by a faction's mustered
members is seized, and the same plant unoccupied is refused; (3) with edit 3, `endings_reached` on a realm
whose fifteen settled territories are held under one faction, at least one by an act, reports
`peninsular_sovereignty`, and reports nothing when one settled territory is held by another faction.
Controls: every switch off reproduces `build_realm(0)`'s hash and the one- and two-season pins.

## The falsifier

- Edit 1: crossings appear at every distance in the same season (the rule is coupling ordinary wear, H-236's
  present state), or `restore` is never attempted (the loop is open: decay with no mender).
- Edit 2: a seat whose faction does not occupy an unheld place seizes it.
- Edit 3: the row is reached with T15 unheld **and** a settled territory unheld.

## NERS reading

- **N.** Without edit 1 the survival contest has no first move; without edit 2 the death of a land-holder
  would shrink the governed map for ever (a ratchet in the live-edge set, the shape L3 refuses in Queries).
  That ratchet is structural and was **not observed** in E-16, where no land-holder died in three seasons
  at either seed; H-186's cite records it from an earlier tree (11 of 16 territories unheld after one
  season). Edit 2 is therefore the lowest-ranked of the three. Without edit 3 the game has no reachable
  victory. Each
  holds top-down (the realm's end states), bottom-up (a person's `restore`, `march`, `seize`), and
  laterally (SE's fabric, FA's holds, MB's occupation).
- **R.** The no-player half: a front that advances unless persons hold it, and land that changes hands
  after a death, are drama nobody scripts. Completeness: at coupling 0 and with nobody dead the realm is
  today's.
- **S.** No new clock, verb, kind or carrier. The band scheme is `band_floors`, the occupation rule is
  `occupies`, the selector grammar is the roster's.
- **E, last.** One data row, one switch, one deleted decline, one selector key, against the realm's two
  end states and its only world-first threat. High.

## Cost class

Edit 1: small build, plus a content assumption that is Jordan's to correct. Edit 2: edit. Edit 3: edit.
Edit 4: two values, one declared mover, after the ages (A-15). Tier: `sonnet` (R3 7b-0). The wound's Site
kind stays INCOMPLETE as Jordan's content.
