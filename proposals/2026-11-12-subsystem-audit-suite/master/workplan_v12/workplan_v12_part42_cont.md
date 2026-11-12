# Workplan v12 — part 42, continued: Batch B39-procgen-and-cases, items B39.18 to B39.99

## Status: PROPOSED (the continuation of a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head, its position table and items B39.01 to B39.17 are in the part this file continues. Short names (`PROC_A` to `_E`, `CORE_case`, `ARCS_case`, `STORY_B`, `_C`, `_E`, `U5d_STORY`, `SYN_B`, `COL_D`) are that part's.

---

### B39.18 — the docket, and an arrival binding a card · `PROC_D` §5 and (g′) · HELD (PG-6's openings-per-season reading past season 8)
`PROC_D` §5 (decision D-3, "RULED B behind a test (A-52)") and (g′) are not built here. The trigger is the source's own: "built only after PG-6's reading shows cards read at build run dry (openings per season falling to zero in a long game)"; "read the openings-per-season curve past season 8, and decide on that reading." That reading is past the two-season cap before B99 (D-17), so it cannot be taken by any close of this plan before B99: the position leaves for the held table (§7.9) at this batch's expunge, with this trigger. When it fires, the item is: the docket's carrier is "a Proposition or Record the seat-holder utters at `convene`, which the bound persons' choosers then meet as a classed referent (`propositions_heard`, CR-28)", never goal rows minted on other persons (design-first for that carrier, `opus`; needs `14_VERBS_BINDING_B_sittings`, B32); (g′) takes the same carrier; plan text "B10-18:183" and "B10-19:95" are amended then, by the ruling. Files it would touch: `engine/season/world_cards.yaml` (`family: docket`), `engine/season/loop/resolve.py` or the `convene` effect, `engine/season/worldgen.yaml` (`docket_size`, `arrival_card`).

### B39.19 — a besieged town's larder · `U5d_STORY` §1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_STORY` §1 (R-07; owed to SE and MB); its head (`besiege` "joins in CP-T04-06's own declared-mover commit, so this section waits on it"); `V12_STRUCTURE_part2.md` §5.7 DEP-NOCARRIER ("`besiege` is `IS-MB-02` (B22)"); `IS_B1_PC_MB_DICE_part2.md` row IS-MB-P7 ("unblocked by IS-MB-02 | B22, then B39").
- ADVANCES: none of the nine; S-22's siege (`audits/23_STORY_ENABLEMENT.md`).
- INSTRUCTION:
  1. **STOPS IF** `besiege` is not a member of `engine/season/rosters.yaml: march_postures` at the item's open (B22.12's mover commit "is not made" when besieging first wins at least as often at every seed, per `IS-MB-02`'s gate): then the item is `BLOCKED (MB: B22.12 did not add `besiege`)` and nothing below ships; the commit body of the batch close says so.
  2. "While an `Invested` field stands on a rung, the walk for cohorts beneath it stops at that rung (eligibility: which rungs may feed whom). The besieger's ration is `07_SE_campaign_supply_and_muster.md`'s standing ration, once a season." Owner: "The larder ladder's walk in `modules/settlements/subsist.py` (the walk `07_SE_ground_and_granaries.md` §4 d edits)"; the band is `data/rosters.py`'s `INVESTED` (`FIELD_BANDS`).
- WHERE: `modules/settlements/subsist.py` (the larder walk); `engine/season/tests/test_endowment.py`.
- TESTS: in `engine/season/tests/test_endowment.py` (`07_SE_ground_and_granaries`' file, B12a), written before the edit: `test_an_invested_rung_stops_the_walk_for_the_cohorts_beneath_it`; red before (the walk climbs past the rung).
- FALSIFIER and CONTROL: "The besieged town drawing from above its rung." Control: "a twin town with the siege lifted eats from the duchy."
- GATE: `python -m pytest engine/season/tests/test_endowment.py -q` → pass; "a hand-built siege" of two seasons (four in the source; A-114): "the town's stores fall and its cohort's body is drawn down by the hunger draw (`09_WR_B_draws_not_thresholds.md` edit 2), while a twin town with the siege lifted eats from the duchy", read over seeds 0 to 4 as a share (`assert checked >= 5`).
- HASH MOVERS: "Runs with an `Invested` field (none in computed play today; `march` by army verbs is withheld). Declared"; B39.99's re-pin.
- DEPENDS ON: V12 Batch B22 (B22.11, B22.12: `besiege`, `Invested`; `07_SE_campaign_supply_and_muster`, the standing ration); V12 Batch B12a (B12a.53, the larder walk; B12a.11, the hungry body drawn); EXISTS-IN-TREE `modules/settlements/subsist.py`, `data/rosters.py::INVESTED`.
- GLOSSARY: none (*invested* has its row).
- COST and TIER: edit; `sonnet` (`U5d_STORY` "Cost class").
- LANDS IT: B39's producer; `Item: B39.19`, `[skip ci]`.

### B39.20 — a burned granary: `sabotage` of a store · `U5d_STORY` §2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_STORY` §2 (R-08; owed to the MATERIAL lane's `sabotage` row).
- ADVANCES: none of the nine; S-36's fire.
- INSTRUCTION: `engine/season/verb_table.yaml`, row `sabotage` ("its drawn form is `14_VERBS_MATERIAL_A_mending.md`'s"): "`sabotage`'s referent class gains a rung's store of a kind beside a Site; the loss is the band's (Overwhelming most of the store, Success half, Partial a tenth and the doer's trail is left, Failure nothing and the trail is left) `[ASSUMPTION; medium; Jordan to correct]`; the trail is `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md`'s." The effect writes the store through the existing two-sided mover (`loop/effects_shared.py::_shift`) and the referent class row; if `store.sabotaged` is the kind the effect emits, it joins `covert_kinds.values` with `leaves: [site_changed, stores_changed]` (`PROC_C` (f)'s intended member, B39.17's maps).
- WHERE: `engine/season/verb_table.yaml` (`sabotage`'s referent class and band writes); the `sabotage` effect (`loop/effects_economy.py`, by symbol at the open); `engine/season/rosters.yaml` (`covert_kinds`, if the kind is new); the test file `14_VERBS_MATERIAL_A_mending.md` names for `sabotage` (B12c).
- TESTS: `test_sabotage_of_a_store_reaches_every_band_and_leaves_a_trail_below_success`, in that file, written first; red before (no store referent).
- FALSIFIER and CONTROL: "A store lost at Failure; a certain loss." Control: a `sabotage` on a Site reads as before.
- GATE: "All four bands occur across 20 dice seeds on one hand-built world" (`assert checked >= 20`); the covering test file → pass.
- HASH MOVERS: "Runs where a `sabotage` forms on a store. Declared"; B39.99.
- DEPENDS ON: V12 Batch B12c (`14_VERBS_MATERIAL_A`, B12c.04: the family's draw); V12 Batch B11 (B11.59, the trail); V12 B39.17 (`covert_kinds.leaves`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`.
- LANDS IT: B39's producer; `Item: B39.20`, `[skip ci]`.

### B39.21 — a lapse under an empty seat is laid on the believed filler · `U5d_STORY` §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_STORY` §3 (R-11; "an amendment to `20_NARRATIVE_B_what_he_was_owed.md`"); rulings A-33.
- ADVANCES: none of the nine; S-33's blame.
- INSTRUCTION: `queries/person_q.py::dues_unmet` (NARR-B's reader, B38.07): "A due that lapses while the owing seat is vacant is attributed to the person the wronged man **believes** holds a seat that may fill it (`may_fill`, read through his own `held_by` claims, `20_NARRATIVE_C`), else to nobody. Under A-33 he may still believe the dead holder holds it: then the dead man is blamed until the death is learned."
- WHERE: `engine/season/queries/person_q.py` (`dues_unmet`); `engine/season/tests/test_narrative_dues.py`.
- TESTS: `test_a_lapse_under_a_vacant_seat_is_laid_on_the_believed_filler`, in `engine/season/tests/test_narrative_dues.py` ("the file `30_WR_D` and NARR-B open"), written first; red before.
- FALSIFIER and CONTROL: "Blame laid by reading World truth." Control: a due lapsing under a held seat is laid as B38's reader lays it.
- GATE: "NARR-F's clause for G2 on a hand-built vacancy: the blamed person is the believed filler"; `python -m pytest engine/season/tests/test_narrative_dues.py -q` → pass.
- HASH MOVERS: "None in the loop until NARR-B lands": NARR-B landed in B38 (B38.07, its valence shipped 0); declared a mover of every world with a lapsed due under a vacant seat once that valence is set; B39.99.
- DEPENDS ON: V12 Batch B38 (B38.07 `20_NARRATIVE_B`; `20_NARRATIVE_C`'s `held_by` claims); EXISTS-IN-TREE `state/gate.py::may_fill`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B39's producer; `Item: B39.21`, `[skip ci]`.

### B39.22 — the opener's edge on an unready victim · `U5d_STORY` §4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_STORY` §4 (R-12; "the ladder's D-41, following A-16").
- ADVANCES: none of the nine; S-09's ambush.
- INSTRUCTION: `rosters.yaml: context_terms` (`14_VERBS_PHYSICAL_A_custody_and_force.md` A3), contexts `enmity` (`22_HAPPENINGS_C`) and `war`: "One entry, `unready`: a named level for the attacker in the first exchange when the victim's notice draw (`18_DETERMINISM_notice_is_a_draw.md`) failed. It modulates one exchange and decides nothing." (A round's first exchange; A-101.)
- WHERE: `engine/season/rosters.yaml` (`context_terms`, `unready`); the reader of `context_terms` that A3 lands (by symbol at the open); the test file `14_VERBS_PHYSICAL_A_custody_and_force.md` names for `context_terms`.
- TESTS: `test_an_unready_victim_gives_the_opener_one_level_in_the_first_exchange_only`, in that file, written first; red before.
- FALSIFIER and CONTROL: "An ambush that always kills." Control: a victim whose notice draw succeeded gives no level.
- GATE: "With the notice draw forced to each band on one hand-built attempt, the first exchange's pool differs by the level and the scene's outcome still varies across dice seeds" (seeds 0 to 19, `assert checked >= 20`); the covering test file → pass.
- HASH MOVERS: "Runs with an `enmity` or `war` scene. Declared"; B39.99.
- DEPENDS ON: V12 Batch B15 (`14_VERBS_PHYSICAL_A` A3, `context_terms`); V12 Batch B37 (`22_HAPPENINGS_C`, `enmity`); V12 Batch B11 (B11.66, the notice draw; B11.67, `notice_arm` on).
- GLOSSARY: *unready* (new: "a person caught unaware, as an unready guard is").
- COST and TIER: edit; `sonnet`.
- LANDS IT: B39's producer; `Item: B39.22`, `[skip ci]`.

### B39.23 — both blows of one exchange land before the felling check · `U5d_STORY` §5 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_STORY` §5 (R-21; "owed at PC's owner"); its head (`modules/combat/wrapper.py`: `if defender.felled: _emit_outcome(...); return defender, closed` follows the aggressor's blow; "the sibling checks … are read by the same edit"); `UNDECIDED` (4) of this block.
- ADVANCES: none of the nine; S-28's double death.
- INSTRUCTION: in `modules/combat/` exchange resolution (`modules/combat/wrapper.py`, the exchange loop; the three `if defender.felled:` checks, by symbol: the one after the aggressor's blow and its two siblings): "Both parties' blows drawn in one exchange are applied before the felling check, so a mutual felling is an outcome of draws already taken. No new draw." Re-derive `engine/engine_params/combat_engine_v1.json` with `tools/export_engine_params.py` only if a key changes (none expected; `--check` read).
- WHERE: `modules/combat/wrapper.py` (the exchange's felling checks); NEW test in `tests/valoria/` beside the combat module's exchange tests.
- TESTS: `test_both_blows_of_one_exchange_land_before_the_felling_check` ("a planted exchange in which each blow fells"), written first; red before.
- FALSIFIER and CONTROL: "0 of 5,000 again." Control: an exchange in which only one blow fells reads as before.
- GATE: the new test → pass; "The PC pessimist's 5,000-duel reading shows mutual fellings above 0", read by `systems/combat/combat_engine_v1/workbench/balance.py` (the combat-balance instrument, CLAUDE.md §9) at 5,000 duels; `python -m pytest tests/valoria -q -m combat` → pass after the combat goldens' re-pin (B39.99); `python tools/export_engine_params.py --check` → exit 0.
- HASH MOVERS: "Every fight's log. Declared"; every season fight and the combat goldens; B39.99's one re-pin. B15's calibration readings (`reading @<sha>`) re-read at the close and any move reported.
- DEPENDS ON: V12 Batch B15 (the PC calibration, A-31); V12 Batch B13 (`modules.combat` as a package); EXISTS-IN-TREE `modules/combat/wrapper.py` (the exchange loop).
- GLOSSARY: none (*exchange*, *felled* have rows).
- COST and TIER: edit; `sonnet`, `high`; the 5,000-duel reading `opus` (a combat number other lanes calibrated).
- LANDS IT: B39's producer; `Item: B39.23`, `[skip ci]`.

### B39.24 — a marriage is a form of instrument · `STORY_B` edit 1 · BUILD · HASH EQUAL
- SOURCE: `STORY_B` "The resolution, decided", "Exact edits" 1; rulings A-75; composes on `15_INSTITUTIONS_COLONIAL_A_instruments.md` and `15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` (B32).
- ADVANCES: none of the nine; S-07 and S-05 (`audits/23_STORY_ENABLEMENT.md` §2).
- INSTRUCTION: `engine/season/instruments.yaml`, the form `marriage` ("a row in SYN-A's registry; the key names are that file's"):
  ```yaml
  marriage:
    parties:   [Person, Person]          # each party's own act; for a party under majority_age, his guardian's
    terms:     {bearer: <one of the parties>}   # authored at formation; the party the birth draw's costs fall on
    dues:      []
    kept:      "both parties live"
    ends_on:   ["a party's death", "release by either party (a deed against the other)"]
    ties:      true                      # counts as a tie for VEN-A's `obligation` term between the parties and their houses' heads
  ```
  "Formed by `covenant` on this form (formation: SOC1-A; the draw: `13_SC`; pool the proposer's standing and what his house offers, obstacle the other party's interest and his house head's regard). Reader: `queries/person_q.py::spouse_of(w, p) -> Optional[str]`, a pure read of live `marriage` instruments naming `p`." The builder seeds a cast row's `spouse:` key as an instrument; no row carries one in this commit (B39.25).
- WHERE: `engine/season/instruments.yaml` (`marriage`); `engine/season/queries/person_q.py` (`spouse_of`); `engine/season/boot/realm.py` (seed a `spouse:` key); NEW `engine/season/tests/test_births.py`.
- TESTS: in the new file, written first: `test_birth_rate_zero_takes_no_draw_and_hash_equal` (green at control) and `test_spouse_of_reads_a_live_marriage` `[ASSUMPTION: test name; the item creates it]` (red before).
- FALSIFIER and CONTROL: a `marriage` that forms without a `covenant` act. Control: no `spouse:` key, hash equal to B39.17's.
- GATE: `python -m pytest engine/season/tests/test_births.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 Batch B32 (`instruments.yaml`, `data/instruments.py`, SYN I-1); V12 Batch B07 (B07.09, the `covenant` draw); V12 Batch B28 (`covenant` formed).
- GLOSSARY: *marriage* (new: "an instrument binding two persons, formed by `covenant`, as a marriage contract is").
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B39's producer; `Item: B39.24`, `[skip ci]`.

### B39.25 — the cast's marriages, drafted · `STORY_B` edit 1 (`spouse:` content) · CONTENT · HASH MOVER(behaviour)
- SOURCE: `STORY_B` edit 1 ("Authored marriages of the cast are seeded as instruments by the builder from a `spouse:` key on the cast row `[content; Jordan's names]`"); `22_HAPPENINGS.md` §1.5 as `STORY_B` quotes it (a consort with standing; a house "unmarried, childless, heirless"); D-19.
- ADVANCES: none of the nine.
- INSTRUCTION: add a `spouse:` key to the cast rows of `references/npc_registry.yaml` (the cast's registry; the row the builder reads through `data/cast.py`) only where canon or the registry already states a marriage between two of the cast; each `status: seed [ASSUMPTION; drafted for Jordan's correction]`; each `terms.bearer` drafted likewise; the PR body lists every pair. Where canon states none, no key is written.
- WHERE: `references/npc_registry.yaml` (cast rows' `spouse:`); `engine/season/data/cast.py` (the key read, if B39.24 did not add it).
- TESTS: none new; `test_spouse_of_reads_a_live_marriage` re-read on the realm.
- FALSIFIER and CONTROL: a marriage seeded between persons whose rows state none. Control: with the keys removed, B39.24's hash.
- GATE: `build_realm(0)`: the number of live `marriage` instruments equals the number of pairs written (printed); `python -m pytest engine/season/tests/test_births.py -q` → pass.
- HASH MOVERS: every seeded world (new instruments at build) when any key is written. Declared; B39.99.
- DEPENDS ON: V12 B39.24.
- GLOSSARY: none.
- COST and TIER: content; drafting `opus`; landing `sonnet`.
- LANDS IT: B39's producer; `Item: B39.25`, `[skip ci]`.

### B39.26 — a birth is drawn on the bodies clock; CENSUS individuates the child · `STORY_B` edits 2–3 · BUILD · HASH EQUAL
- SOURCE: `STORY_B` "Exact edits" 2 and 3 (one commit, "hash-equal at `birth_rate` 0.0"); its `Reconciled:` lines (C3-L13; A-75; the birth as a `person.born` demand Event at MATTER, not a row on the instrument's `stages`; U6 R-C's `birth_level`, `birth_step`); rulings A-30, A-54, A-75.
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. `engine/season/loop/matter.py` — `_births(w, token)`, on the bodies clock, "once a year (the tick the year roster of `20_NARRATIVE_E` edit 1 marks as the year's turn), for each live `marriage` whose parties share a `reside` object and whose `bearer` is of an age inside `fertile_ages`": "taken at all with chance `birth_rate` (keyed draw `H(seed, tick, instrument id, "birth:taken")`, A-30; 0.0 at landing …); then one graded draw through the one sampler, keyed `H(seed, tick, instrument id, "birth")`. Pool: `birth_pool`, plus the leverage level `birth_level` (a `LEVEL_SIGMA` name, applied by `net_boost` under the soft cap, A-25's favourable side) where the home settlement's hunger band is `fed`. Obstacle: `birth_ob`, plus `birth_step` (successes) per `age_bands` step of the bearer above `fertile_peak`, per body band the bearer stands below the top, and where the home is short (A-25's hostile side)." Bands: Overwhelming two births (`person.born` ×2); Success one birth (`person.born`); Partial one birth and "the bearer falls one body band (MATTER's own `(Person, body)` write …; one step of the `body` stake's size, `23_STORY_A`'s `stake_amount`)" (`person.born`, `body.changed`); Failure nothing, "at `shortfall_step` 3 the bearer falls one body band" (`body.changed`). "A birth is the Event `person.born`, emitted at MATTER and citing the marriage instrument: the demand CENSUS reads … `person.born` is a new kind on the matrix row that emits it (`EVENT_KINDS` derives it, inv. 7) [ASSUMPTION: medium; the cell it rides is the one `person.demanded`'s emitter uses — basis: R5 7b; the landing lane reads it at `write_matrix.yaml`]."
  2. `engine/season/data/fixtures.py`: `birth_rate = 0.0`, `birth_pool`, `birth_ob`, `birth_level`, `birth_step` ("starting points: `pool_default` and the `routine` difficulty level; `birth_level` and `birth_step` have none"), `fertile_ages`, `fertile_peak` ("authored in years and converted by `len(SEASONS_OF_YEAR)` … values are calibration content, none given here"), each with its `[JUSTIFIED: …]` or `[ASSUMPTION]` tag for `tools/ci_sim_fabrication_check.py`.
  3. `engine/season/loop/census.py` — for each `person.born`, CENSUS "individuates the child as it individuates any demanded person (the Person, its person rung and its `contain` edge, weight 1), with `born = w.tick` and its `contain` edge at the bearer's home [ASSUMPTION: a `reside` edge beside it is added only if `write_matrix.yaml` admits it at CENSUS]; its name from `generate_person` keyed by the `person.born` Event id. No pursuits, conviction or skill are written at CENSUS … WITNESS deposits the birth to those present; everyone else learns by telling."
- WHERE: `engine/season/loop/matter.py` (`_births`); `engine/season/write_matrix.yaml` (the row that emits `person.born`); `engine/season/data/fixtures.py` (the seven settings); `engine/season/loop/census.py` (individuation on `person.born`); `engine/season/tests/test_births.py`.
- TESTS: in `test_births.py`, written first: `test_person_born_is_read_by_census_as_a_demand`, `test_child_has_born_and_contain_and_parents_hold_a_claim`, `test_census_writes_no_pursuits_or_conviction_for_a_child`; red before.
- FALSIFIER and CONTROL: "A birth with `birth_rate` 0.0 … The same couple bearing at every seed: the draw is not keyed on the tick, or `birth_rate` is read as a threshold." Control: `birth_rate` 0.0, the realm hash at seeds 0 to 2 equal to B39.25's.
- GATE: `python -m pytest engine/season/tests/test_births.py -q` → pass; on the valley fixture with one seeded marriage, seeds 0–19, two seasons (eight in the source; A-114), `birth_rate` 1.0 arm: "a birth at some seeds and none at others; at least three of the four bands' outcomes across seeds" (`assert checked >= 20`), printed beside the 0.0 arm (no `person.born`).
- HASH MOVERS: none at `birth_rate` 0.0.
- DEPENDS ON: V12 B39.24, B39.04 (the census path), B39.03 (`generate_person`); V12 Batch B12a (B12a.02, the year roster); V12 Batch B37 (`22_HAPPENINGS_A`, ages and the spell of illness); V12 Batch B38 (`23_STORY_A`, `stake_amount`, `shortfall_step`); V12 Batch B05 (the one sampler, `net_boost`); EXISTS-IN-TREE `loop/census.py::_individuate`, `state/ids.py::H`.
- GLOSSARY: *birth* event (row: `person.born`, owner pointer to `loop/matter.py::_births`).
- COST and TIER: small build; `sonnet`, `high`; the holonic §29 reading is taken (`opus` in the source's tier line).
- LANDS IT: B39's producer; `Item: B39.26`, `[skip ci]`.
