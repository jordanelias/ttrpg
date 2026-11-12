# Workplan v12 — part 15: Batch B21-fa-governance, second half (B21.51 to B21.99, and the boundary row)

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A15 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2. Every item is written against the tree as B00 to B10 and the first half of B21 will leave it; a symbol that does not exist at `aa31fd2` names the item or batch that makes it.

**What this part holds.** The second half of one batch. The first half (U3 §1 item 21 from `06_FA_seat_terms_and_turnover` through `06_FA_decree_binds` edit 3, positions `B21.01` to `B21.50` at most) is the other author's, with the batch block's head (the §5.2 lines from `INVOCATION` to `EST`). This part continues U3 §1 item 21's order from `16_PESSIMIST_FA_A` (`16_PESSIMIST_FA_A` → `14_VERBS_BINDING_D` → `06_FA_war_lives_in_seats_B` edits 1–3 → `06_FA_levy_through_the_seat_B` → `16_PESSIMIST_FA_B` → the rest of `U5d_FA_owed_edits` → `06_FA_playable_scenario` → `14_VERBS_BINDING_C`'s flip → `06_FA_shortest_loop_B`), with the instruction items `V12_STRUCTURE.md` §2.2 places here (`IS-B3-FA-05` after `14_VERBS_BINDING_D`; `IS-B3-FA-06` with the rest of `U5d_FA_owed_edits`; `IS-B3-FA-07` after `14_VERBS_BINDING_C` and `U5d_FA_owed_edits` §3–§4; `IS-B3-FA-01` after `06_FA_shortest_loop_B`), the intake's B21 entries (`master/eval/V12_INTAKE.md:168` and `:231`), the re-pin position `B21.99` (`V12_STRUCTURE_part4.md` E-1) and the boundary row. A part cites another part's batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`; a person's numbers are an attribute, a skill and its skill score, a derived score (A-98); a *lap* is one pass of the season's scene budget, a *round* one engagement of a fight (A-101). Source text that says "obligee" is copied as "sworn man" (glossary *sworn*; the tree key `obligees` keeps its name); "ladder" for a chain of seats is "chain of seats" (glossary *rung*). Where a copied sentence used a retired word, the correction is said beside it.

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `IS-B3` is `master/instructions/IS_B3_FA_SE_WR_GO.md`. Member proposals are under `proposals/` of the suite and are named by file stem. A path under `engine/`, `tools/`, `references/`, `registers/`, `tests/`, `systems/` is the repository's; an `engine/season/` path may drop that prefix where the item has already named it.

---

## Batch B21-fa-governance (continued) · lane FA · wave W12 · step S12 · HASH MOVER, one re-pin

The batch block's head lines (`INVOCATION`, `IN-FLIGHT ROW`, the six `GATE: Batch` lines, `REQUIREMENT`, `BATCH GATE`, `RE-PIN`, `IDS`, `DIALS AT CONTROL`, `C(B21-fa-governance)`, `SERIAL EDGES`, `PARALLEL`, `COST`, `EST`) are the first half's. This half adds the lines below, which the head merges (H2 collects them by script, `V12_STRUCTURE_part3.md` §7.2):

IDS (this half): ED-FA 0; H 2 (B21.61's NUMBER row for `cross_chain_step`; B21.69's NUMBER row for `faction_power_step`)
DIALS AT CONTROL (this half):
  `cross_chain_step` = 0; set by B98; target: none stated (`16_PESSIMIST_FA_B` edit 2: "control 0, proposed 2"; no reading named), so B98 writes it `BLOCKED (design: no target reading)` (D-22);
  `faction_power_step` = 0; set by B98; target: none stated (`IS-B3-FA-07`: "set by Jordan or the B21 calibration"; B21 runs no calibration), so `BLOCKED (design: no target reading)`;
  `provisional_term` = its control (Partial = Success, `14_VERBS_BINDING_C` C1) from the first half's BIND_C landing; set by this batch's B21.73 (BIND_C's flip) to 2, the source's proposed value; the source's later re-setting ("the joint re-centring (OBS §4 step 5) or the story census sets it") has no scheduled owner after B21 and is listed here for B98 with target: none stated;
  `rosters.yaml: tables.territory_weight` = `{}` (every territory reads 1.0, the source's control); set by content (D-19: "the numbers are content `[ASSUMPTION; Jordan to author]`", `U5d_FA_owed_edits` §4); target: none stated.
BATCH GATE (this half's additions, read at B21.99 on the closing tree; each is an arm the source gates on and this part moved to the close, §5.8): listed in B21.99's GATE.
EST (this half): 0.4 h × 29 positions = 11.6 h, the close counted once in the head's EST `[estimate: V12_STRUCTURE_part4.md E-15, the formula of V12_STRUCTURE.md §2.4 over positions]`.
UNDECIDED (this half; each reading taken is the one that changes less, `V12_STRUCTURE_part2.md` §5.1):
  (U1) **What "BIND_C's flip" is** (U3 §1 item 21 schedules it after the scenario; no file defines the word). Readings: (a) the commit that moves BIND_C's own setting off control, `provisional_term` control → 2, with C3's gate arms read on the scenario's situations (OBS §4 step 6+: "each with its step at control 0 first … a declared mover when the step ships"); (b) no flip in B21, `provisional_term` left for B98. Taken (a), because U3 schedules a position and C3's gate world is the scenario (U3 §1.2 B21 row 6: "the scenario is BIND_C's gate world"); `rank_step` (BIND_A's fixture, the first half's) is not flipped here (no source states its value).
  (U2) **`IS-B3-FA-05` and `14_VERBS_BINDING_D` commit D4.** D4 makes `dispatch` contested and relocates the man in the sender's act at O/S/P; `IS-B3-FA-05` (b) (A-24) has the sender's act deposit the order and the man's own `comply` relocate him. Taken: `IS-B3-FA-05` as written, with no contest on `dispatch` (D4 edit 11's `contests:` cell is not added: a draw on the sender's act and the man's own answer would be two ladders for one quantity). D4 is closed by B21.57.
  (U3) **`CP-T09-07` (b) in two batches.** The intake places `CP-T09-07` whole in B21b (`:245`); `IS-B3-FA-05` carries (b) into B21 (the intake `:246`: "after CP-T09-07 (b) lands via IS-B3-FA-05"). Taken: B21.57 lands (b)'s `may_muster` clause only (the clause CP-T09-08 needs, the only one `IS-B3-FA-05`'s WHERE names); (b)'s `loop/sides.py` claimant union stays with `CP-T09-07` in B21b. **(Patched: P-24, decided by the ladder, step 4.)** B21b's author read the union as B21's (B21b.02 and B21b.04 DEPENDS ON "V12 Batch B21 (`IS-B3-FA-05`: … the `sides_of` union)"), so neither part carried it; B21b.02's flip and B21b.04's obligee arm need it before they land, and the intake `:246` puts it with `IS-B3-FA-05`: the union lands in B21 as B21.79, before B21.57.
  (U4) **`U5d_FA_owed_edits` §3 and `IS-B3-FA-07`.** `IS-B3-FA-07` and D-01 read §3 as a B21 member; U3 §4.1 row 77 and the source's own "Lands in" put §3 in B32. Taken: §3 stays in B32; B21.69 reads no symbol §3 adds (it reads `may_revoke`, `revoke`'s contested row from BIND_C C2 and C3, and §4's `faction_q.weight`), so no back edge.
  (U5) **`U5d_FA_owed_edits` §5** is placed after `06_FA_shortest_loop_B` (B21.75), not in U3's slot for "the rest of U5d", because its precondition reads `loop_closed`, which B21.74 adds.
  (U6) **`IS-B3-FA-01` needs B11** (`IS-B2-CORE-01`'s `scenarios.py`, `IS-B3-GO-01`'s `kinds` and `unreached`, `IS-B2-CORE-02`'s `season_ending`), which is not in B21's `after` list (§2.1). Taken: the source's own rule (IS-B3 §3.2: "If B21 merges first, `IS-B3-FA-01` lands as the first item of B23 instead"), written as a `STOPS IF` line; no edge is added to §2.1.
  (U7) **The intake's B21 entries.** M8, §1b-3, A2-14 (E3 Block 1) describe CR-36 and CR-37, which the intake itself places in B21c (`:270`, `:271`); by `V12_STRUCTURE_part4.md` E-8's exception (the dependency lands later) they join B21c, noted here as POINTER B21.77. M38 (E3 Block 2, E5 Block D5) has no edit ("edit set: none beyond CR-38"; "gate: n/a"); POINTER B21.78.
  (U8) **`U5d_FA_owed_edits` §7's third clause** ("the plan card CP-T09-06 reads `null → inheritance`") edits v11's text, which v12's adoption retires; the edit it names is B21.51. Not carried.
  (U9) **`16_PESSIMIST_FA_A` says "No hash moves at build"**; `Office.conferral`, `.rung` and `.remit_acts` are values of a carrier `World.content_hash()` folds (`state/world.py::World._STATE_COLLECTIONS` holds `"offices"`), so B21.51 to B21.53 are declared movers here.

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B21.51 | the Duchy of Valorsmark passes with the throne | `16_PESSIMIST_FA_A` edit 1 | BUILD | MOVER(behaviour) | the first half's `22_HAPPENINGS_B` edits 1–2 and BIND_C at control |
| B21.52 | six council seats anchored one rung below their duchy | `16_PESSIMIST_FA_A` edit 2 | BUILD | MOVER(behaviour) | B21.51 |
| B21.53 | a dismissing ducal seat may also pardon | `16_PESSIMIST_FA_A` edit 3 | BUILD | MOVER(behaviour) | B21.52 |
| B21.54 | what a writ orders: a Proposition, and the asker's ambitions | `14_VERBS_BINDING_D` commit D1 | BUILD | MOVER(behaviour) | B21.53 |
| B21.55 | `issue` and `dispatch` form only on those the seat commands | `14_VERBS_BINDING_D` commit D2 | BUILD | MOVER(behaviour) | B21.54; the first half's `16_PESSIMIST_FA_C` items |
| B21.56 | the draw on `issue`: a writ at every band, its `force` written | `14_VERBS_BINDING_D` commit D3 | BUILD | MOVER(behaviour) | B21.55; the first half's `06_FA_decree_binds` items; Batch B05 |
| B21.79 | the seat's obligees present are its people: `seat_people_at`, and `sides_of` reads it (Patched: P-24) | CP-T09-07 (b)'s union, with AM-F-13 | BUILD | MOVER(behaviour) | B21.56 |
| B21.57 | a `dispatch` that sends: the order deposited, the man's `comply` moves him | `IS-B3-FA-05` (closes D4; CP-T09-08; CP-T09-07 (b)'s gate clause) | BUILD | MOVER(behaviour) | B21.79 |
| B21.58 | a war lives in the seats that wage it | `06_FA_war_lives_in_seats_B` edits 1–3 | BUILD | EQUAL | B21.57 (U3's order) |
| B21.59 | men are levied through a seat | `06_FA_levy_through_the_seat_B` edits 1–6 | BUILD | EQUAL | B21.58 |
| B21.60 | a seat is held by an individual | `16_PESSIMIST_FA_B` edit 1 | BUILD | EQUAL | B21.59 |
| B21.61 | no self-conferral across chains of seats; `cross_chain` priced | `16_PESSIMIST_FA_B` edit 2 | BUILD | EQUAL | B21.60; the first half's BIND_C C3 |
| B21.62 | a war has two parties and a declarer who can wage it | `16_PESSIMIST_FA_B` edit 4 | BUILD | EQUAL | B21.61, B21.58 |
| B21.63 | joining a faction is answered by the faction | `16_PESSIMIST_FA_B` edit 3 | BUILD | MOVER(behaviour) | B21.62 |
| B21.64 | two register rows closed, as text | `U5d_FA_owed_edits` §7 | BUILD | EQUAL | B21.51 |
| B21.65 | a person's opinion of a faction regards its present head | `U5d_FA_owed_edits` §8 | BUILD | MOVER(behaviour) | B21.64; the first half's `06_FA_seat_terms_by_body_B` edit 4 |
| B21.66 | a successor confirms his predecessor's writs or lets them lapse | `IS-B3-FA-06` (replaces `U5d_FA_owed_edits` §9) | BUILD | MOVER(behaviour) | B21.65 |
| B21.67 | someone may always claim an empty throne: the test | `U5d_FA_owed_edits` §1 | BUILD | EQUAL | B21.66; the first half's REMIT edit 1 and `22_HAPPENINGS_B` edits 1–3 |
| B21.68 | a faction's weight reads where its members live | `U5d_FA_owed_edits` §4 | BUILD | EQUAL | B21.67 |
| B21.69 | a reduction of a sitting holder's grant is a revocation | `IS-B3-FA-07` (H-132; A-105) | BUILD | MOVER(behaviour) | B21.68, B21.61 |
| B21.70 | one purse per rung | `U5d_FA_owed_edits` §6 | HELD (a computed `requisition` on a rung seating two factions) | — | its trigger reading at B21.99 |
| B21.71 | the governance test world's seats get conferral and revocation bases | `06_FA_playable_scenario` (the fixture edit) | BUILD | MOVER(behaviour): the spine's own build hash only | B21.69 |
| B21.72 | a governance scenario that plays: situations, digest, menu, `play` | `06_FA_playable_scenario` (the harness edits) | BUILD | EQUAL | B21.71 |
| B21.73 | BIND_C's flip: a Partial seat-opening is provisional | `14_VERBS_BINDING_C` C1's setting off control, C3's gate | BUILD | MOVER(behaviour) | B21.72 |
| B21.74 | the shortest playable loop: `recall`, `--world realm`, `loop_closed` | `06_FA_shortest_loop_B` | BUILD | EQUAL | B21.73 |
| B21.75 | what an order orders | `U5d_FA_owed_edits` §5 | HELD (`loop_closed` reads `answered > 0` at two dice seeds) | — | B21.74 |
| B21.76 | the spine's situations and the realm as scenario rows | `IS-B3-FA-01` | BUILD | EQUAL | B21.74; V12 Batch B11 (`STOPS IF`) |
| B21.77 | a living top-seat holder can be removed (joint concurrence) | the intake M8, §1b-3, A2-14 | POINTER | — | V12 Batch B21c-fa-seats |
| B21.78 | the marquis question | the intake M38 | POINTER | — | — |
| B21.80 | a refused `confer` says which clause refused, in its kind (Patched: P-26) | `01_CORE_predicates_name_their_clause` step two, row `confer` | BUILD | MOVER(behaviour) | the first half's B21.14; Batch B09 (B09.18, B09.19) |
| B21.81 | a refused `establish` says which clause refused, in its kind (Patched: P-26) | the same, row `establish` | BUILD | MOVER(behaviour) | B21.80; the first half's B21.09 |
| B21.82 | a refused `revoke` says which clause refused, in its kind (Patched: P-26) | the same, row `revoke` | BUILD | MOVER(behaviour) | B21.81 |
| B21.83 | a refused `oblige` says which clause refused, in its kind (Patched: P-26) | the same, row `oblige` | BUILD | MOVER(behaviour) | B21.82 |
| B21.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B21.51 to B21.83 |

Not in this half, and where each is: `U5d_FA_owed_edits` §2 (the first half, before BIND_C); §3 (B32, with `15_INSTITUTIONS_PAPACY_B` item 4, U3 §4.1 row 77); §10 (B39, with `21_PROCEDURAL_B`, row 78); `06_FA_war_lives_in_seats_B` edit 6 (B23, first) and edits 4, 5, 7 (applied, plan clauses, follow-ons: no item); `16_PESSIMIST_FA_B`'s `may_seat` form (B32, U3 §4.1 row 73); `IS-B3-FA-02` (B34); `IS-B3-FA-03` (B38); `IS-B3-FA-04` (B23); `14_VERBS_BINDING_D` edit 10 (cross-lane, "listed for FA (not edited)"); `CP-T09-07` (a) (B21b); (b)'s `sides_of` union is B21.79 (Patched: P-24).

### B21.51 — the Duchy of Valorsmark passes with the throne · `16_PESSIMIST_FA_A` edit 1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` "The resolution, decided" row 1, "Exact edits" 1, "Gate" G2; rulings A-19; U3 C3-K9; closes F-PES-FA-02 (part); carries CP-T09-06's edit (`U5d_FA_owed_edits` §7).
- ADVANCES: R-04.a (`revoke` after a succession; with B21.52, B21.53); FA standalone S5.
- INSTRUCTION: written after the first half's `22_HAPPENINGS_B` edit 2 (the set-of-titles shape), C3-K9.
  1. First, NEW `engine/season/tests/test_fa_dismissal.py` with `test_heir_holds_both_titles_after_one_succeed` (G2), read red: "after the King's death and the heir's one `succeed`: `off_king` and `off_duke_valorsmark` are both held by the heir; `strippable(w)` equals its value at build; the new King's `revoke` of the Marshal through `off_duke_valorsmark` closes the hold. Today: empty set, `revoke.refused`." `strippable(w)` is a test-local helper over `state/gate.py::may_revoke` for every live seat-`hold` and every seat `via` `[ASSUMPTION: helper shape; the item creates it — basis: the source's `pf1` was "grant-filtered", scratch not in the tree, U3 §6.2]`. With BIND_C's `revoke` a draw, the arm "closes the hold" is read over dice seeds as a share (`assert checked >= N`): it carries at some seed and the refusal is gone at every seed.
  2. "**`engine/season/offices.yaml`, row `off_duke_valorsmark`**: `conferral: null` → `conferral: inheritance`. **`engine/season/rosters.yaml: successions`** (the `{seat: [title, …]}` shape of `22_HAPPENINGS_B` edit 2, which lands first): add `off_duke_valorsmark` with **the same title list as `off_king`** (`[off_heir, off_widow_regent, off_princess, off_duchess_hafenmark, off_duke_varfell]` as HAP_B edit 2 writes it), so whoever takes the throne in the deed race (A-19) takes the duchy with it: a list is eligibility, the claim is the draw. (`claimable_seats` already returns every vacant seat whose title is the claimant's; `_eff_succeed` already opens all of them in one write. No code edit.)" Read `off_king`'s row on the tree at the item's open and copy its list as it stands, not the list quoted here, if they differ; name the difference in the commit body.
  3. "`offices.yaml`'s header counts and `engine/engine_params/` exports that carry the rows are re-derived with the repo's own exporter (`--check`), not by hand." Find the exporter with `grep -rln "offices.yaml" tools/export_*.py` and run its `--check` after re-deriving.
- WHERE: `engine/season/offices.yaml` (`off_duke_valorsmark` `conferral`); `engine/season/rosters.yaml` (`successions`); NEW `engine/season/tests/test_fa_dismissal.py`; any `engine/engine_params/` artifact the grep names (re-derived).
- TESTS: `test_heir_holds_both_titles_after_one_succeed`, written first, red (the duchy stays empty after the claim).
- FALSIFIER and CONTROL: "G2 would fail if a second seat under one title were treated differently from the first." The import-time `state/gate.py::check_successions` loads the edited files (BIND_C C4's load clause refuses an `inheritance` seat with no `successions` key: the row is what keeps it green). Control: `off_king`'s own row and claim unchanged.
- GATE: `python -m pytest engine/season/tests/test_fa_dismissal.py engine/season/tests/test_in61_succession.py -q` → pass; `python -c "import engine.season.state.gate as g; g.check_successions(); print('ok')"` → `ok`; the realm content hash at seed 0 after one season → moved (an `Office` value is folded, UNDECIDED (U9)), recorded in the commit body.
- HASH MOVERS: the realm content hash at build (`Office.conferral` of one seat); every run with a royal death and a claim. Declared; B21's one re-pin at B21.99.
- DEPENDS ON: EXISTS-IN-TREE `state/gate.py::claimable_seats`, `::check_successions`, `::may_revoke`, `loop/effects_governance.py::_eff_succeed`, `offices.yaml` row `off_duke_valorsmark`; V12 the first half's `22_HAPPENINGS_B` edit 2 item (the list shape) and BIND_C C3 item (`succeed`, `revoke` drawn).
- GLOSSARY: none.
- COST and TIER: edit (data) and a test; `sonnet`, `high` (the source's tier).
- LANDS IT: B21's `valoria-author` producer, `isolation: worktree`; `Item: B21.51`, `[skip ci]`.

### B21.52 — six council seats anchored one rung below their duchy · `16_PESSIMIST_FA_A` edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` "The resolution, decided" row 2, "Exact edits" 2, "Gate" G1; rulings A-58; U3 C3-L7; ED-IN-0256 (3) (the basis, untouched).
- ADVANCES: R-04.a (`revoke` within Hafenmark and Varfell).
- INSTRUCTION:
  1. First, in `test_fa_dismissal.py`, `test_strippable_set_at_build_includes_six_council_seats` (G1), read red: "`strippable(w)` at build is a superset of today's six and includes six council seats, each through its duke's seat. Control: `off_king` strips none of the twelve (the rule is unchanged), and the Guild Comptroller is still strippable by nobody."
  2. "**`engine/season/offices.yaml`**, the `rung:` anchor of six rows: `off_legal_advisor_hm`, `off_military_commander_hm`, `off_commune_rep_hm` from `{duchy: "Hafenmark"}` to `{territory: "terr_T8"}` (`off_guild_comptroller` is left where it is: its faction is `Guilds`, so no anchor brings it under the Duchess); `off_senior_jarl_west`, `off_skald_chief`, `off_military_jarl` from `{duchy: "Varfell"}` to `{territory: "terr_T12"}`." The territories are the source's reading of `systems/settlements/valoria_geography_v30.yaml` (T8 holds Gransol, S-018, Hafenmark's constitutional capital; T12 holds Sigurdshelm, S-031, `type: Seat`); re-read both at the item's open and confirm `build_realm(0)` lists `terr_T8` among Hafenmark's children and `terr_T12` among Varfell's. "If the Senior Jarl **of the Western Highlands** is meant to sit on his own highland territory rather than at the ducal seat, his row takes that territory; the rule reaches him either way." `[ASSUMPTION: the ducal seat's territory — basis: the source's text; Jordan may move the Senior Jarl's row in the PR]`.
  3. "Each of the six rows gains one comment line (A-58, C3-L7): *"anchored on `terr_T8` (`terr_T12`): its `revocation:` is `rung_above_same_faction`, not `holder_of_rung`, so a seizure of this territory alone does not carry this seat; it passes with the ducal seat"*." Re-derive the exports as in B21.51 step 3.
- WHERE: `engine/season/offices.yaml` (six `rung:` anchors, six comment lines); `engine/season/tests/test_fa_dismissal.py`.
- TESTS: `test_strippable_set_at_build_includes_six_council_seats`, first, red.
- FALSIFIER and CONTROL: "G1 would fail if a council's body resolved to a faction other than its duke's." `off_guild_comptroller` does not pass (its faction resolves to `Guilds`): if the test finds it strippable, the anchor reached it and the item is wrong. Control: `off_king` strips none of the twelve.
- GATE: `python -m pytest engine/season/tests/test_fa_dismissal.py -q` → the two tests so far pass; `python -m pytest engine/season/tests/test_in31_revocation_cost.py engine/season/tests/test_g3_not_yours.py -q` → pass; the realm hash at seed 0, one season → moved, recorded.
- HASH MOVERS: the realm content hash at build (six `Office.rung` values). Declared; B21.99's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `state/gate.py::may_revoke`, `offices.yaml` rows named, `systems/settlements/valoria_geography_v30.yaml` (S-018, S-031); V12 B21.51.
- GLOSSARY: none.
- COST and TIER: edit (data); `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.52`, `[skip ci]`.

### B21.53 — a dismissing ducal seat may also pardon · `16_PESSIMIST_FA_A` edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` "The resolution, decided" row 3, "Exact edits" 3, "Gate" G3, G4; rulings A-37.
- ADVANCES: R-04.a (`pardon` through a seat that dismissed); `BUILT OUT` reading for `pardon` is B32's.
- INSTRUCTION:
  1. First, in `test_fa_dismissal.py`: `test_dismiss_then_pardon_through_the_ducal_seat` (G3: "the King dismisses the Marshal through `off_duke_valorsmark`, then `pardon`s him through the same seat: `ban.ended`; the reappointment then opens"; with BIND_C's `revoke` and `confer` draws (`pardon` stays undrawn until `14_VERBS_BINDING_B` in B32), read as a share over dice seeds with `assert checked >= N`) and `test_pardon_through_off_king_still_refused` (G3's control: "`pardon` through `off_king` (not the ban's object) is still refused"), read red (the first) and green (the control).
  2. "**`engine/season/offices.yaml`**, rows `off_duke_valorsmark`, `off_duchess_hafenmark`, `off_duke_varfell`: add `determine` to `remit_acts`." "`remit_acts` edits re-stamp nothing at build (the grant is stamped when the hold opens)"; re-derive the exports as in B21.51 step 3.
- WHERE: `engine/season/offices.yaml` (three `remit_acts`); `engine/season/tests/test_fa_dismissal.py`.
- TESTS: the two above; the file's four tests then pass.
- FALSIFIER and CONTROL: "G3 would fail if the bench asked more than the grant and the object." Control: `pardon` through `off_king` refused.
- GATE (G4): `python -m pytest engine/season/tests/test_fa_dismissal.py engine/season/tests/test_in31_revocation_cost.py engine/season/tests/test_in61_succession.py engine/season/tests/test_in12_arrest.py engine/season/tests/test_g3_not_yours.py -q` → pass; the realm hash at seed 0, one season → moved, recorded.
- HASH MOVERS: the realm content hash (three `Office.remit_acts`; any hold opened at build stamps the grant). Declared; B21.99's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `verb_table.yaml` row `pardon` (`remit:determine`), `loop/effects_governance.py` (`_eff_revoke` opens the ban); V12 B21.52; the first half's BIND_C items (the `revoke` draw).
- GLOSSARY: none.
- COST and TIER: edit (data); `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.53`, `[skip ci]`.

### B21.54 — what a writ orders: a Proposition, and the asker's ambitions · `14_VERBS_BINDING_D` commit D1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `14_VERBS_BINDING_D_orders.md` "The resolution, decided" (terms are a Proposition), "Exact edits" commit D1 (edits 1–2), "Gate" D1, "Falsifier"; rulings A-21, A-22; `unified/U5_CONFLICTS_U5c.md` C-25; closes F-FA-01 (part).
- ADVANCES: R-04.a (`issue`); R-05 (`issue` forms on an OUGHT).
- INSTRUCTION:
  1. "`verb_table.yaml`, `issue`: `referent_class: Proposition` with a note naming VB-D and its revert (delete the column). The typed cell is unchanged."
  2. "`queries/world_q.py::questions_for`: add `tuple(ambition_ids(w, p))` to `added` beside `propositions_heard(w, p)`, where `ambition_ids` returns the Proposition ids of `ambitions(w, p)` (the one owner) — `_stamped` dedups. Declared widening: `argue` (the other `Proposition`-classed row) gains these referents; `commit` does not (`held_edge_declines`). Measure both rows' formed counts." `ambition_ids` is NEW, written beside `ambitions` in `queries/world_q.py` `[ASSUMPTION: its home — basis: "`world_q.ambitions` is that rule's one owner"]`.
  3. The commit body records `argue` and `commit` formed counts before (`reading @<sha>`, the previous item's) and after, from `python -m engine.season.harness.aperture 2 0` and `2 1`.
- WHERE: `engine/season/verb_table.yaml` (`issue`: `referent_class`, its note); `engine/season/queries/world_q.py` (`questions_for`, NEW `ambition_ids`); NEW `engine/season/tests/test_vb_d_orders.py` (the source's test file, "one function per gate D1–D3").
- TESTS: `test_vb_d_orders.py::test_d1_no_writ_terms_name_a_person` `[ASSUMPTION: test name; the item creates it, V12_STRUCTURE_part4.md E-3]`, written first and read red: over `build_realm(1)`, two seasons, every executed `issue`'s `terms` is a Proposition id (today the King's writs carry `terms` = a person, `binding_probe_2_1.txt`).
- FALSIFIER and CONTROL: "Revert D1's class: person-terms return." Control: `commit`'s formed count unchanged (`held_edge_declines`).
- GATE: `python -m pytest engine/season/tests/test_vb_d_orders.py -q` → the D1 test passes; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` and `2 1` → "0 writs whose `terms` is not a Proposition; `argue` and `commit` formed counts recorded before and after"; the realm hash at seed 0, one season → moved, recorded.
- HASH MOVERS: "All are declared movers for the realm." Every seeded run with an `issue` or an `argue`. B21.99's re-pin.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::questions_for`, `::propositions_heard`, `::ambitions`, `verb_table.yaml` row `issue`; V12 B21.53 (U3's order: `16_PESSIMIST_FA_A` precedes BIND_D); Batch B07 (`U5c_VERBS_residue_and_governance_owner` §2: the `a standing` row).
- GLOSSARY: none.
- NAMES: `questions_for(since=…)`'s `(tick, round)` key → `(tick, lap)` (B04, PCR-4), if the edit touches it.
- COST and TIER: small build; `sonnet`, `high` (R4 7b.0 (1)).
- LANDS IT: B21's producer; `Item: B21.54`, `[skip ci]`.

### B21.55 — `issue` and `dispatch` form only on those the seat commands · `14_VERBS_BINDING_D` commit D2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `14_VERBS_BINDING_D_orders.md` "Exact edits" commit D2 (edits 3–6), "Gate" D2; ruling A-22 (command); `16_PESSIMIST_FA_C_under_the_seat.md` edits 1–3 (the one body, the first half).
- ADVANCES: R-04.a (`issue`, `dispatch`).
- INSTRUCTION: edits 3 and 4 and edit 5's basis cell are already on the tree from the first half's `16_PESSIMIST_FA_C` items ("edit 3 no longer writes `state/gate.py::commands`"; edit 4: "FA_C edit 2 makes the same change; whichever of the two lands second finds it made and adds nothing"; FA_C edit 2 flips `issue`'s `basis: purview` → `basis: command`). Open `queries/world_q.py::commands`, `data/requires.py`'s `basis` dispatch and `verb_table.yaml` `issue` at the item's open and record in the commit body that each is present; write no second body. What this item adds:
  1. Edit 5's prose: "`requires:` prose and `refusal_note` amended (*"`issue.unauthorized` -- the SEAT: none exercised grants `issue`, or it does not command the executor"*). `[ASSUMPTION; medium; Jordan to correct; revert: `basis: purview`]`."
  2. Edit 6: "`decision/options.py::operand_bags`: for a row whose `authority` conjunct is `basis: command`, fan `to` over the persons the actor can read as commanded person-side: the men sworn to his own seats (his ledger's `duty.taken` claims naming his seat) and the holders his ledger names of seats beneath his. What he cannot read stays the fold's refusal."
  3. "Until CP-T09-08 lands, D2's fan applies to the current row (`referent_class: Person`, `writes: []`): no order goes up the chain and no self-order forms." (CP-T09-08 lands at B21.57.)
- WHERE: `engine/season/verb_table.yaml` (`issue`: `requires`, `refusal_note`); `engine/season/decision/options.py` (`operand_bags`); `engine/season/tests/test_vb_d_orders.py`.
- TESTS: `test_vb_d_orders.py::test_d2_no_writ_or_order_to_a_person_the_seat_does_not_command` `[ASSUMPTION: test name; E-3]`, first, red: over `build_realm(1)`, two seasons, executed `issue` and `dispatch` whose addressee `world_q.commands` refuses → 0 (the probe's one writ to the King and four orders to him).
- FALSIFIER and CONTROL: "Swap `command` for `purview`: the writ to the King returns." Control: an unseated resident of the seat's land is still addressed (FA_C's clause (iii)).
- GATE: `python -m pytest engine/season/tests/test_vb_d_orders.py engine/season/tests/test_command_basis.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` and `2 1` → "0 writs and 0 orders whose addressee the seat does not command"; executed `issue` and `dispatch` before (`reading @<sha>`) and after, quoted.
- HASH MOVERS: every seeded run where `to` was fanned over a non-commanded person. Declared; B21.99.
- DEPENDS ON: V12 the first half's `16_PESSIMIST_FA_C` items (`world_q.commands`, the `command` basis, `_req_dispatch`'s clause) and `06_FA_decree_binds` edits 1–3; V12 B21.54; EXISTS-IN-TREE `decision/options.py::operand_bags`.
- GLOSSARY: row *command basis* is the first half's (FA_C edit 1); none here.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.55`, `[skip ci]`.

### B21.56 — the draw on `issue`: a writ at every band, its `force` written · `14_VERBS_BINDING_D` commit D3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `14_VERBS_BINDING_D_orders.md` "The resolution, decided" (the draw), "Exact edits" commit D3 (edits 8–9; edit 7 deleted, edit 10 cross-lane), "Gate" D3; the Standing line (pool and draw key); rulings A-21, A-30, A-81 (C3-C11); `unified/U5_CONFLICTS_U5c.md` C-25.
- ADVANCES: R-04.a (`issue` drawn); R-02 (the answer reads a remembered deed).
- INSTRUCTION (after SC-B and FA-P1: Batch B05 and the first half's `06_FA_decree_binds` items):
  1. Edit 8: "`verb_table.yaml`, `issue`: `contests: "a standing"`, `difficulty: routine`; `writes` at every band `["Record.exists"]`; `emits` O/S/P `["dispensation.issued"]`, Failure `["dispensation.ignored"]`; `emits_on_refusal` flattened to one kind, `issue.refused`, keyed under every clause (a contested row keys one kind unless it keys `counterparty`; `determine`'s v9 SC-03b precedent) — `issue.unauthorized` is retired into it, and the refusal's `observed` reads still say which clause failed. **Durable write of the Failure band (A-81; C3-C11):** the writ exists at every band, and `dispensation.ignored` is proclaimed like any decree (A-21): whoever learns of the issue holds a claim of it and of its `force`, so a dead letter is itself a remembered deed against the issuing seat."
  2. The draw: "prize `a standing`, opponent `to`, through the one obstacle composer: `difficulty` `routine`, `opposition` (his skill score, A-79, D-U1-02), `regard` (his stance toward the issuer), `rank_gap` (OBS §2 member 6)." The pool: "the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the issuer's skill score (A-6), the governing attribute as levels (A-7), a wound a level against the roll (A-8); the issuer's exercised seat helps him only as the `office` level (D-U1-01)." Draw key: "`H(w.world_seed, w.tick, <actor id>, "issue.standing")`" (A-30).
  3. Edit 9: "`loop/effects_information.py::_eff_issue`: pass `res.degree` into the content as `force` (a `dispensation` key; `rosters.yaml: record_kinds` gains `force` for that kind)."
  4. Edit 10 is not edited here ("Cross-lane, listed for FA (not edited)"): the answer rows' obstacles reading `force` are named in the commit body as owed to the answer rows' owner.
  5. `issue.refused` and `dispensation.ignored` land with the row: `data/verbs.py::KIND_VERB` is derived from every row's `emits:` and `emits_on_refusal:` (`_derive_kind_verb`), so no kind map is edited by hand; where `rosters.yaml` rosters Event kinds, they are added there as BIND_C edit 8 adds its kinds. `git grep -n "issue.unauthorized"` before the edit, each reader re-pointed to `issue.refused`, the list in the commit body.
- WHERE: `engine/season/verb_table.yaml` (`issue`); `engine/season/loop/effects_information.py` (`_eff_issue`); `engine/season/rosters.yaml` (`record_kinds.dispensation`: `force`; the Event kinds where rostered); `engine/season/tests/test_vb_d_orders.py`.
- TESTS: `test_vb_d_orders.py::test_d3_a_writ_is_minted_at_every_band_with_its_force` `[ASSUMPTION: test name; E-3]`, first, red: a hand-built `issue` resolved at each of four planted bands mints a `dispensation` whose content carries `force` equal to the band, and a Failure emits `dispensation.ignored`.
- FALSIFIER and CONTROL: "Pin the roll: one `force` band only." Control: the `covenant`-minted `dispensation` carries no `force` (the key is written by `_eff_issue` only).
- GATE: `python -m pytest engine/season/tests/test_vb_d_orders.py -q` → pass. D3's scenario arm ("FA-B4's `recall` scenario, 40 seeds: all four `force` bands occur; at every band, Failure included, the Count is offered his answers once he learns of the issue … and the answer's composed obstacle carries `force`") reads a world B21.74 makes: moved to B21.74's GATE (§5.8). Here: over `build_realm(s)`, s = 0 to 2, two seasons, the share of executed `issue` by band, quoted, `assert checked >= 1` per seed.
- HASH MOVERS: every seeded run with an `issue`. Declared; B21.99.
- DEPENDS ON: V12 B21.55; Batch B05 (`U5c_SC_one_obstacle_form` §4 steps 0–2: `difficulty`, `opposition`, `regard`; `pool_of`); V12 the first half's `14_VERBS_BINDING_A` commit A3 (`rank_gap`, `rank_step`) and `06_FA_decree_binds` edit 1 (`proclaimed`); EXISTS-IN-TREE `loop/effects_information.py::_eff_issue`, `rosters.yaml: contest_subsystems.prizes` (`a standing`).
- GLOSSARY: row *force* (if the glossary lacks one: "force: how strongly a writ binds, the band its issue reached, as one speaks of a law in force").
- COST and TIER: build (a contested row and its terms); `opus` producer (R4 7b.0 (1): "D3 (the contested row and its terms) `opus` producer"); one `opus` read of the band table at B21.74.
- LANDS IT: B21's producer; `Item: B21.56`, `[skip ci]`.

### B21.79 — the seat's obligees present are its people: `seat_people_at`, and `sides_of` reads it · CP-T09-07 (b)'s union, with AM-F-13 · BUILD · HASH MOVER(behaviour) · Patched: P-24
- SOURCE: `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-09-factions-war-diplomacy.md` CP-T09-07 "Adds." (b), "Asymmetry.", "Falsifier." (2), "Hash · revert." (`:359-397`); `master/eval/E5.md` Block C22 (AM-F-13, as copied at B21b.04); the intake `:246` ("after CP-T09-07 (b) lands via IS-B3-FA-05"); UNDECIDED (U3) as patched.
- ADVANCES: R-04.c4's line (who fights for a seat); unblocks B21b.02 (`guards` ON: "before CP-T09-07 (b)'s union lands the flip musters nobody") and B21b.04's obligee arm.
- INSTRUCTION:
  1. SITE (`V12_STRUCTURE_part2.md` §5.7): open `loop/sides.py::sides_of` (the claimants line, `sides.py:115` at the source's tree) and `loop/effects_shared.py::occupying_faction` (`effects_shared.py:149` there) and record in the commit body what each reads for the seat's people.
  2. AM-F-13, copied: "CP-T09-07's commit adds one reader, `world_q.seat_people_at(w, via, rid)` = `mustered(rid, seat_faction(via))` ∪ the seat's obligees present in `rid`'s subtree, and in the same commit points `sides_of` (`sides.py:115`), `occupying_faction` (`effects_shared.py:149`) and the plurality comparison of CP-T09-04 (b) at it." The obligees are "`establishment_of(via)`" (CP-T09-07 (b)). The plurality comparison does not exist before B21b.04, which reads `seat_people_at` at its own SITE step; this item points the two readers that exist.
  3. Before the edit, "grep the `oblige` opener list (`data/verbs.py` `_OPENERS_FROM_EFFECTS`)" (CP-T09-07 "Asymmetry."): "`may_muster` and `sides_of` are getters; the openers of `oblige` … are untouched". `may_muster`'s clause is B21.57's step 1, next.
- WHERE: `engine/season/queries/world_q.py` (NEW `seat_people_at`); `engine/season/loop/sides.py` (`sides_of`); `engine/season/loop/effects_shared.py` (`occupying_faction`); `engine/season/tests/test_march.py`.
- TESTS: in `test_march.py`, written before step 2 and read red: `test_a_seats_obligee_at_home_marches_in_its_army` `[ASSUMPTION: test name; the item creates it, E-3]` — falsifier (2) below.
- FALSIFIER and CONTROL (copied): "(2) A hand-built settlement march whose marcher's seat has one obligee, not a faction member, at home: the army is one larger than base. Mutation: drop the union → base." Control: a seat with no obligee present reads `mustered(rid, seat_faction(via))` exactly as before.
- GATE: `python -m pytest engine/season/tests/test_march.py -q` → pass; the realm hash at seed 0, one season → recorded (moved where a seat's obligee stood in an origin's subtree; said which).
- HASH MOVERS: "Mover · … the union" (CP-T09-07 "Hash · revert."). Declared; B21's one re-pin (B21.99).
- DEPENDS ON: EXISTS-IN-TREE `loop/sides.py::sides_of`, `loop/effects_shared.py::occupying_faction`, `queries/world_q.py::mustered`, `::establishment_of`, `state/gate.py::seat_faction`; V12 B21.56.
- GLOSSARY: none (*obligee*, *sworn* already read "a man with a live `oblige` to a seat").
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B21's producer; `Item: B21.79`, `[skip ci]`.

### B21.57 — a `dispatch` that sends: the order deposited, the man's `comply` moves him · `IS-B3-FA-05` (CP-T09-08; CP-T09-07 (b)'s gate clause; closes `14_VERBS_BINDING_D` D4) · BUILD · HASH MOVER(behaviour)
- SOURCE: IS-B3 `IS-B3-FA-05` (`:139-148`); its home `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-09-factions-war-diplomacy.md` CP-T09-08 (`:398-420`) and CP-T09-07 (b) (`:359-375`); `14_VERBS_BINDING_D_orders.md` commit D4 (edits 11–12); rulings A-21, A-22, A-24, A-104; closes `unified/U4_DOCUMENT_STATUS.md` §3.4's "no carrier" for `_eff_dispatch`; UNDECIDED (U2), (U3).
- ADVANCES: R-05 (`dispatch` executes with a consequence); FA integrated; unblocks `15_INSTITUTIONS_BYZANTINE_D`, `15_INSTITUTIONS_COLONIAL_grounding_F`, `15_INSTITUTIONS_SYNTHESIS_E`.
- INSTRUCTION (IS-B3's text, with the three changes it orders):
  1. CP-T09-07 (b)'s clause only: "`es/state/gate.py:865` `may_muster` admits a moved man holding a live `oblige` to `via` as well as one committed to its faction" — `state/gate.py::may_muster`, the clause beside its faction-commitment conjunct. (The `loop/sides.py` claimant union of (b) is not edited here: UNDECIDED (U3).)
  2. CP-T09-08 as IS-B3 amends it: "subject a destination Rung inside the seat's purview, `to` a person" becomes, to keep the row's control: the row gains an optional destination operand, a Rung inside the seat's purview (`purview_reaches`), and `subject` stays the person `_req_dispatch` and the first half's FA_C clause read `[ASSUMPTION: the operand key `dest`, `_relocate(w, a, dest, mover)`'s parameter — basis: IS-B3's WHERE says "the destination operand" and its control "a `dispatch` with no destination operand behaves as today"]`. (a) A-22: "who may be sent is the command predicate of `16_PESSIMIST_FA_C_under_the_seat.md` … read once, so `_req_dispatch` … calls it and holds no second rule" (already so, the first half). (b) A-24: "the man's going is his own answer. The effect does not relocate him. It deposits the order's content to him (A-21, as `06_FA_decree_binds.md` edit 1 does for a writ) and his `comply` is the act that calls `_relocate`; `evade / defy` is the other answer and is read by the recall occasion." So: NEW `loop/effects_governance.py::_eff_dispatch` deposits, when `dest` is present, the order's content (the destination) to the man as the first half's `proclaimed`/`read_to_addressee` route deposits a writ's terms; `verb_table.yaml` `comply`: a branch on an order whose content names a destination calls `loop/effects_migration.py::_relocate(w, a, dest, mover=a.actor)`, which charges him the leg ("which also charges him the journey's leg"), and writes "the `contain` pairs `march` writes". (c) "the row's `writes_note` ("it names a person; their own choose decides") therefore stands and the row's `grade: "ruled"` is not touched." D4's `contests:` cell on `dispatch` is not added (UNDECIDED (U2)). A-104: if CL-MGMT lists `dispatch` as a management order, the sender's act costs no scene budget; "the dispatched man's `comply` is the scene it opens, at an ordinary price".
  3. "Until CP-T09-08 lands" (D4 edit 12) is discharged by this item; the commit body says "closes VB-D commit D4 (as amended by `IS-B3-FA-05`)".
- WHERE: `engine/season/verb_table.yaml` (`dispatch`: the destination operand; `comply`: a branch on an order whose content names a destination); `engine/season/loop/effects_governance.py` (NEW `_eff_dispatch`); `engine/season/loop/predicates.py` (`_req_dispatch`: `dest` in the seat's purview when present); `engine/season/state/gate.py` (`may_muster`, CP-T09-07 (b)'s clause); NEW `engine/season/tests/test_dispatch_sends.py`.
- TESTS: in the new file, written first and red: "`test_a_complied_dispatch_moves_the_man_and_charges_him_the_leg`; `test_a_defied_dispatch_moves_nobody_and_is_read_by_the_issuer`; `test_a_dispatch_to_a_man_outside_the_command_is_refused`". Before writing `_eff_dispatch`, "grep the `oblige` opener list (`data/verbs.py` `_OPENERS_FROM_EFFECTS`)" (CP-T09-07's asymmetry note).
- FALSIFIER and CONTROL: "Control: a `dispatch` with no destination operand behaves as today (`order.given`, nothing moved)." CP-T09-08's stopping rule: "refusals rise and executions do not → revert."
- GATE: `python -m pytest engine/season/tests/test_dispatch_sends.py engine/season/tests/test_command_basis.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` (and `2 2`) → "`dispatch` executed with at least one `comply` that emits a `travel.*` Event caused by it across seeds 0 and 2"; "the spine probe's `dispatch` count (4 resolved in three seasons, P-3) is the baseline" (an example at IS-B3's SHA, quoted, not a target).
- HASH MOVERS: "Every seeded world in which a `dispatch` is complied with; declared, co-pinned at B21's last item" (B21.99).
- DEPENDS ON: V12 the first half's `16_PESSIMIST_FA_C` and `06_FA_decree_binds` items; V12 B21.56; V12 B21.79 (Patched: P-24); EXISTS-IN-TREE `loop/effects_migration.py::_relocate` (`mover` argument), `state/gate.py::may_muster`, `::purview_reaches`, `loop/predicates.py::_req_dispatch`, `verb_table.yaml` rows `dispatch`, `comply`; MISSING none.
- GLOSSARY: none (*sworn* already reads "a man with a live `oblige` to a seat").
- COST and TIER: small build; `sonnet`, `high`; `opus` critic on (b) (IS-B3).
- LANDS IT: B21's producer; `Item: B21.57`, `[skip ci]`.

### B21.58 — a war lives in the seats that wage it · `06_FA_war_lives_in_seats_B` edits 1–3 · BUILD · HASH EQUAL
- SOURCE: `06_FA_war_lives_in_seats_B.md` "The resolution, decided", "Exact edits" 1–3, "Gate", "Falsifier"; ruling A-20 (`L1-A20` APPLIED: `04:460` carries the narrowed sentence); U3 C3-Y1 (edits 1–3 in B21, edit 6 in B23).
- ADVANCES: R-04 (who wages a war); FA standalone.
- INSTRUCTION (one commit: "Nothing else on the game path in the first commit"):
  1. "**`engine/season/state/gate.py`** (owner of what a seat licenses). One predicate beside `may_muster`:
     ```python
     def may_wage(w, person: str, faction: str) -> bool:
         \"\"\"Does `person` hold a seat of `faction` whose grant carries MUSTER_ACT? `faction` is the
         Proposition id; `seat_faction` is the one owner of seat -> faction id.\"\"\"
     ```
     It is `any(_seat_grants(w, person, h.object, MUSTER_ACT) and seat_faction(w, h.object) == faction for h in person's live holds on offices)`. It adds no rule: both conjuncts are `may_muster`'s first two and its faction read."
  2. "**`engine/season/queries/world_q.py::at_war`** (owner of "is this war live"). The last line's test becomes: a live `commit` to the Proposition whose subject `may_wage` for `p.subject` or for `p.value`. The docstring's F.32 paragraph is replaced by the rule above. `enemies_heard` and the `strife` instrument read `at_war` and need no edit."
  3. "**`engine/season/tests/test_faction_q.py::test_at_war_through_the_real_fold_utter_then_commit_then_release`.** Its declarer is `world_q.members(w, "fac_valorsmark")[0]`; he must be chosen as a holder of a Valorsmark seat whose grant carries `dispatch`, and the test gains its control" — the four steps of the source's Gate: "1. a Valorsmark holder of a `dispatch` seat utters WAR(Valorsmark, Guilds) and commits: `at_war` True both ways …; 2. he `release`s that seat's `hold`, his `commit` still live: `at_war` False; 3. an unseated Valorsmark member commits to the same Proposition: still False; 4. a second holder of a `dispatch` seat, of either faction, commits: True; he releases his commit: False."
  Note: `_seat_grants` carries the first half's `U5d_FA_owed_edits` §2 clause (a detained holder wages nothing), which is intended.
- WHERE: `engine/season/state/gate.py` (NEW `may_wage`); `engine/season/queries/world_q.py` (`at_war`); `engine/season/tests/test_faction_q.py` (the named test).
- TESTS: the named test, re-recorded ("Declared mover of one test"): steps 2 and 3 read False after the edit.
- FALSIFIER and CONTROL: "Control: with the `may_wage` conjunct removed, steps 2 and 3 read True. If they read False without the edit, the test is not observing the rule. Mutation: ask `seat_hold` without the grant (drop `MUSTER_ACT`): a seated treasurer's commit then keeps the war alive and step 3's variant with a treasurer reddens." "Hash: realm, spine and corpus one-season hashes EQUAL before and after edits 1 to 3."
- GATE: `python -m pytest engine/season/tests/test_faction_q.py -q` → pass; the realm hash at seed 0, one season → equal to B21.57's reading. "Realm reading after CP-T09-02 lands" (B21b) is not this batch's.
- HASH MOVERS: none ("In every world the tree builds today no WAR Proposition exists").
- DEPENDS ON: EXISTS-IN-TREE `state/gate.py::_seat_grants`, `::seat_faction`, `::may_muster`, `MUSTER_ACT`, `queries/world_q.py::at_war`, `test_faction_q.py::test_at_war_through_the_real_fold_utter_then_commit_then_release`; nothing proposed ("edits 1–3 on nothing proposed").
- GLOSSARY: none.
- COST and TIER: edit (ruled, A-20); `sonnet`.
- LANDS IT: B21's producer; `Item: B21.58`, `[skip ci]`.

### B21.59 — men are levied through a seat · `06_FA_levy_through_the_seat_B` edits 1–6 · BUILD · HASH EQUAL
- SOURCE: `06_FA_levy_through_the_seat_B.md` "The resolution, decided", "Exact edits" 1–6, "Gate", "Falsifier"; rulings A-22 (one gate arm added), ED-IN-0256 (4); `audits/18_DETERMINISM_SWEEP.md` D-07 (eligibility only; turnout is `recruit`'s draw, B22). One item: the source names no commits and all six edits share the gate's test file (E-13; recorded here).
- ADVANCES: R-04 (who raises an army); MB's entry by computed play (B22 lifts the withholding).
- INSTRUCTION:
  1. "**`engine/season/state/gate.py`** (owner of what a seat licenses), beside `may_muster`:
     ```python
     def may_levy(w, actor, via, cohort: str, faction: str) -> bool:
         \"\"\"May `actor`, exercising `via`, put `cohort`'s people under arms for `faction`'s army?
         seat_hold; the grant carries MUSTER_ACT; seat_faction(via) == faction;
         purview_reaches(seat, residence of the cohort); raisable_by(cohort, faction).\"\"\"
     ```
     Each conjunct is an existing owner's (`_seat_grants`, `seat_faction`, `purview_reaches`, `world_q.raisable_by`); `raisable_by` keeps its recorded assumption." The A-22 reading: "the basis is command over the unseated on the seat's ground … a seated person resident on that ground is not levied through it."
  2. "**`engine/season/verb_table.yaml`** … `recruit` and `discharge_troops`: `eligibility: ["remit:dispatch"]`. Their `requires_typed` (the subject is an army Record the actor holds) is unchanged, so the actor must both sit in a muster seat and hold the roll. The other four rows are unchanged."
  3. "**`engine/season/loop/effects_army.py`.** `_eff_recruit` and `_eff_discharge_troops` replace the bare `world_q.raisable_by(w, cohort.id, faction)` test with `may_levy(w, a.actor, a.via, cohort.id, faction)`. `_army` is unchanged."
  4. "**`engine/season/loop/effects_information.py::_army_mintable`.** One conjunct after the membership test: the actor `may_wage` for the faction" (B21.58).
  5. "**`engine/season/harness/military_menu.py::act_for` and `army_presets._commander`.** `act_for` stamps `via` with the actor's seat that grants the muster act (`decision/options.py::seat_of`, the one owner of "which seat grants this"), so the menu's acts are admitted as the chooser's would be. `_commander` already tries leaders in id order against `_army_mintable` and needs no edit. `military_menu.cohorts_raisable(w, faction)` becomes `cohorts_raisable(w, person)`, asking `may_levy` for each cohort."
  6. "**`engine/season/tests/`** (the files that hand-build army acts; find them with `grep -rl "army.recruited\|act_for(" engine/season/tests`). Each hand-built `recruit` gains a `via`; each gains the refused twin of the gate below."
- WHERE: `engine/season/state/gate.py` (NEW `may_levy`); `engine/season/verb_table.yaml` (`recruit`, `discharge_troops`); `engine/season/loop/effects_army.py` (`_eff_recruit`, `_eff_discharge_troops`); `engine/season/loop/effects_information.py` (`_army_mintable`); `engine/season/harness/military_menu.py` (`act_for`, `cohorts_raisable`); the test files the grep lists; NEW `engine/season/tests/test_fa_levy_through_the_seat.py`.
- TESTS: the new file, "written red against the control (today the unseated mint executes) and green after the edits": `test_an_unseated_member_cannot_mint_the_army`, `test_the_duke_through_his_seat_mints_and_recruits_in_his_territory`, `test_a_cohort_resident_in_another_factions_territory_is_refused`, `test_a_seat_without_the_muster_act_is_refused`, `test_army_presets_mint_three_armies_by_seated_leaders`, and the A-22 arm `test_a_seated_resident_is_not_levied_unless_sworn_or_revocable`. Readings: "`p_npc_002` (no seat): the mint is refused"; "`p_npc_052` through `off_duke_varfell`: `record.created`, then `army.recruited` for a cohort in a Varfell-held territory"; "the same seat on a cohort resident in a territory another faction holds: `recruit.refused`"; "a Varfell seat whose grant lacks the muster act: `recruit.refused`"; "`army_presets.install(build_realm(0))` raises the same three armies the MB audit records (Hafenmark 600, Valorsmark 900, Varfell 600, all levy …), now minted by a seated leader; if a count differs, the difference is a cohort outside the minting seat's purview and is reported by name." `recruit`'s turnout is a draw once B22 lands; here the counts are the shipped effect's.
- FALSIFIER and CONTROL: "Control: with `may_levy`'s seat conjuncts removed the first bullet executes as it does today. Mutation: drop `purview_reaches` and the third bullet executes; drop the faction match and a Crown seat raises a Varfell army. Hash: one-season `build_realm(0)` EQUAL (no army verb forms; none is unwithheld here)."
- GATE: `python -m pytest engine/season/tests/test_fa_levy_through_the_seat.py` and every file step 6's grep lists `-q` → pass; the realm hash at seed 0, one season → equal to B21.58's.
- HASH MOVERS: none ("all six army verbs are withheld from every NPC's opening set").
- DEPENDS ON: V12 B21.58 (`may_wage`); V12 the first half's `16_PESSIMIST_FA_C` items (the command predicate the levy reads, U3 §1.2 row 9); EXISTS-IN-TREE `world_q.raisable_by`, `loop/effects_army.py::_eff_recruit`, `::_eff_discharge_troops`, `loop/effects_information.py::_army_mintable`, `harness/military_menu.py::act_for`, `::cohorts_raisable`, `harness/army_presets.py::_commander`, `decision/options.py::seat_of`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`; MB lane reviews edits 2, 3 and 5.
- LANDS IT: B21's producer; `Item: B21.59`, `[skip ci]`.

### B21.60 — a seat is held by an individual · `16_PESSIMIST_FA_B` edit 1 · BUILD · HASH EQUAL
- SOURCE: `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` "The resolution, decided" row 1, "Exact edits" 1, "Gate" G1; rulings A-19, A-58; "Lands it: B21, order 1 → 2 → 4 (after `may_wage`) → 3", one commit per edit.
- ADVANCES: R-04 (who may sit); the extremes of R-06 (a cohort is not a seat-holder).
- INSTRUCTION:
  1. First, NEW `engine/season/tests/test_fa_eligibility.py` with `test_cohort_cannot_be_named_heir` (G1: "the Queen names a cohort heir: `confer.refused`; control, she names an individual: `tenure.opened` (or VB-C's band)"), read red (today `tenure.opened` for the cohort).
  2. "**`engine/season/state/gate.py`**: `def may_sit(w, person_id) -> bool`: the person exists and `not w.persons[person_id].is_cohort`. Asked in the `conferral` and `claim` clauses of `tenure_write_basis` (the subject of the opened seat-`hold`), and by `loop/predicates.py::_req_confer` (of `to`) and `_req_succeed` (of the actor) through the same name, so the fold refuses (`confer.refused`, `succession.refused`) where the gate would raise. `decision/options.py`'s counterparty fan for `confer` drops cohorts through the same predicate (formation follows admission)." "If VENICE-C's `may_seat(w, off, person)` lands first, this is its first conjunct and no second predicate is written" (VENICE-C is B32: it lands after; B32's item composes on this one).
- WHERE: `engine/season/state/gate.py` (NEW `may_sit`; `tenure_write_basis`'s `conferral` and `claim` clauses); `engine/season/loop/predicates.py` (`_req_confer`, `_req_succeed`); `engine/season/decision/options.py` (the `confer` counterparty fan); NEW `engine/season/tests/test_fa_eligibility.py`.
- TESTS: `test_cohort_cannot_be_named_heir`, first, red.
- FALSIFIER and CONTROL: a cohort opens a seat-`hold` by `confer` or `succeed`. Control: an individual conferee is admitted as before. Movers: "(1) … move no shipped run (nothing computed does either today; … for (1) by `tenure.opened` 0)".
- GATE: `python -m pytest engine/season/tests/test_fa_eligibility.py engine/season/tests/test_faction_q.py engine/season/tests/test_in61_succession.py -q` → pass; the realm hash at seed 0, one season → equal to B21.59's.
- HASH MOVERS: none in shipped runs.
- DEPENDS ON: EXISTS-IN-TREE `state/gate.py::tenure_write_basis`, `loop/predicates.py::_req_confer`, `::_req_succeed`, `state/carriers.py::Person.is_cohort`; V12 B21.59 (order).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.60`, `[skip ci]`.

### B21.61 — no self-conferral across chains of seats; `cross_chain` priced · `16_PESSIMIST_FA_B` edit 2 · BUILD · HASH EQUAL
- SOURCE: `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` "The resolution, decided" row 2, "Exact edits" 2, "Gate" G2; `14_VERBS_BINDING_C_turnover.md` "The draw" table row `confer` (`cross_chain`, OBS member 29); `U5c_SC_one_obstacle_form.md` (member 29); rulings A-105 (pricing keeps a foreign holder uncommon).
- ADVANCES: R-04 (`confer` across factions); A-105.
- INSTRUCTION:
  1. First, in `test_fa_eligibility.py`: `test_self_conferral_across_chains_refused` (G2: "the Queen confers the Confessor's seat on herself: `confer.refused` (`self_across_chains`); control, the King confers the heir's title on himself (one chain of seats): admitted as today"), read red.
  2. "**`engine/season/loop/predicates.py::_req_confer`**: after the existing `may_fill` conjunct, refuse (`_refuse("self_across_chains", …)`) when `to == a.actor` and `w.offices[a.via].faction != w.offices[obj].faction` (`Office.faction` is the resolved faction, `gate.py:505-507`)." ("ladder" in the source → "chain of seats", glossary *rung*.)
  3. The term (BIND_C's table row `confer`, landed at control by the first half's BIND_C C3 item, names `cross_chain`; the source "requests the term of that owner"): if the first half's item did not land the member, land it here in `rosters.yaml: obstacle_terms` in OBS §2's order as member 29 with its fixture `cross_chain_step` in `engine/season/data/fixtures.py` ("fixture, control 0, proposed 2"), "a step harder when `office_faction(via) != office_faction(off)`", read by the one obstacle composer, and its NUMBER row in `engine/season/hole_register.yaml` (block slot 1). Open both at the item's open and record in the commit body which half landed it.
- WHERE: `engine/season/loop/predicates.py` (`_req_confer`); where step 3 applies: `engine/season/rosters.yaml` (`obstacle_terms`), `engine/season/data/fixtures.py` (`cross_chain_step`), `engine/season/hole_register.yaml` (one NUMBER row); `engine/season/tests/test_fa_eligibility.py`.
- TESTS: `test_self_conferral_across_chains_refused`, first, red; and `test_cross_chain_term_reads_zero_at_control` `[ASSUMPTION: test name; E-3]`: a `confer` across factions composes an obstacle whose `cross_chain` term is 0 at `cross_chain_step` 0 and one step at 1.
- FALSIFIER and CONTROL: "G2 is wrong if a regency is meant to be exactly this act (a consort taking a vacant seat of another chain of seats); the provided character NPC-032 says she has no action economy of her own, which is why it is refused here." Control: the King's self-conferral of the heir's title inside one chain is admitted; at `cross_chain_step` 0 every `confer`'s composed obstacle equals the previous item's.
- GATE: `python -m pytest engine/season/tests/test_fa_eligibility.py engine/season/tests/test_vb_c_turnover.py -q` → pass; `python -m engine.season.harness.register --check` → exit 0 (the NUMBER row); `python tools/ci_sim_fabrication_check.py` → exit 0; the realm hash at seed 0, one season → equal to B21.60's.
- HASH MOVERS: none at control ("(2) none in shipped runs").
- DEPENDS ON: V12 B21.60; V12 the first half's BIND_C C3 item (`confer` contested, its term table); Batch B05 (the obstacle composer, `obstacle_terms`); EXISTS-IN-TREE `loop/predicates.py::_req_confer`, `state/gate.py::may_fill`.
- GLOSSARY: none (*chain of seats* is the glossary's own phrase).
- IDS: H block slot 1 (the `cross_chain_step` NUMBER row), only where step 3 applies.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.61`, `[skip ci]`.

### B21.62 — a war has two parties and a declarer who can wage it · `16_PESSIMIST_FA_B` edit 4 · BUILD · HASH EQUAL
- SOURCE: `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` "The resolution, decided" row 4, "Exact edits" 4, "Gate" G4; rulings A-20; `04` §F.24a and `:1204-1209` (payload well-formedness).
- ADVANCES: R-04 (war's declaration); the extremes of R-05 (no self-war).
- INSTRUCTION:
  1. First, in `test_fa_eligibility.py`: `test_war_between_same_faction_refused` and `test_war_utterance_without_a_waging_seat_is_not_a_declaration` (G4: "a cohort's, a stranger's and a clerk's `WAR` between Hafenmark and Varfell: refused; the Duchess of Hafenmark's: `proposition.uttered`; `WAR(Hafenmark, Hafenmark)`: refused"), read red.
  2. "**`engine/season/verb_table.yaml`, row `utter`** (`requires: "—"`, `emits_on_refusal: []` today, read 2026-11-12): the `WAR` mood's conditions as **typed** `requires` …: `requires_typed` gains, for mood `WAR`, `Existence(world_q.members(subject))`, `Existence(world_q.members(value))` and `Relation(actor in members(subject) or members(value))`, plus `may_wage`'s conjunct as `06_FA_war_lives_in_seats_B.md` edit 1 writes it. `subject != value` is a payload well-formedness refusal at Act construction (`04` `:1204-1209`), not a predicate. The row gains `emits_on_refusal: [utter.refused]` (the clause that can now fail needs a kind, inv. 4). No `_req_utter` is written." `utter.refused` lands in the Event kinds with the row.
  3. "A member's `WAR` utterance without such a seat is refused as a declaration (it is a call for war, an ordinary utterance of another mood)."
- WHERE: `engine/season/verb_table.yaml` (`utter`: `requires_typed`, `emits_on_refusal`); the Act-construction well-formedness check for `subject != value` (find it with `git grep -n "well-formed\|_well_formed" engine/season/loop engine/season/state` at the item's open; name the site in the commit body); `engine/season/rosters.yaml` (the Event kind `utter.refused`, if kinds are rostered there); `engine/season/tests/test_fa_eligibility.py`.
- TESTS: the two above, first, red; `test_faction_q.py::test_at_war_through_the_real_fold_utter_then_commit_then_release` stays green (B21.58 chose a waging declarer).
- FALSIFIER and CONTROL: `at_war(Hafenmark, Hafenmark)` reads True after a WAR utterance. Control: the Duchess's `WAR` mints. Movers: "verified for (4) by `at_war` empty at every seed".
- GATE: `python -m pytest engine/season/tests/test_fa_eligibility.py engine/season/tests/test_faction_q.py -q` → pass; the realm hash at seed 0, one season → equal to B21.61's.
- HASH MOVERS: none in shipped runs.
- DEPENDS ON: V12 B21.58 (`may_wage`); EXISTS-IN-TREE `data/requires.py` forms `Existence`, `Relation`; `queries/world_q.py::members`; `verb_table.yaml` row `utter`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B21's producer; `Item: B21.62`, `[skip ci]`.

### B21.63 — joining a faction is answered by the faction · `16_PESSIMIST_FA_B` edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` "The resolution, decided" row 3, "Exact edits" 3, "Gate" G3, "Falsifier"; `04` PART D 27a (a proper noun in the content layer is a declaration).
- ADVANCES: R-04 (membership); R-02 (an admission sought, granted, refused).
- INSTRUCTION:
  1. Before the edit, the first reading: "over seeds 0 to 2, three seasons, how many executed `commit`s are a non-member's to a rostered faction (if zero, edit 3 moves no shipped run and its gate is the hand-built pair only)" — written at two seasons (three in the source; A-114), "printed by `harness/aperture.py`'s per-verb census" `[ASSUMPTION: aperture's census can be filtered by verb and membership — basis: the harness listing]`; where it cannot, a test-local count over `w.log`. Recorded in the commit body.
  2. First, in `test_fa_eligibility.py`: `test_non_member_commit_refused_without_admission` (G3: "the King's `commit` to the Restoration Movement with no admission: refused; with a member's admission in his ledger: `commitment.made`. Control: a member's re-commit and every non-faction `commit` are unchanged"), read red.
  3. "**`engine/season/rosters.yaml: terms_sourced`**, cell `commit`: add the admission source (a Proposition of mood `OUGHT` whose `subject` is the joiner and `value` the faction Proposition, held as a claim in the joiner's ledger and `commit`ted to by an admitting member). **`engine/season/data/requires.py`**: `REQUIRES_STEMS` … gains `admitted`, a `Relation` stem asked of `of` and the actor, whose reader is `queries/world_q.py::admitted_to(w, person, prop)`: true when `prop` is not a rostered faction Proposition and has no live member, or the person is already a member, or an admission stands. `commit`'s typed `requires` gains the `relation` cell `admitted` beside its existing "the Proposition exists". **`rosters.yaml: factions`**: a `compatible_with:` list per row, default empty; the rule "two rostered factions are incompatible unless one row lists the other" is the loader's (`data/rosters.py`), stated once in code, and the data carries only the exceptions."
  4. The admitting member: "a live member whose seat-grant carries `confer`, or the faction's `head_seat` holder … Where a faction has no such seat (the Guilds, Schoenland, Altonia, an unrostered party), any live member's admission serves. Leaving stays the member's own `release` (AX-1)."
  5. The stem `admitted` is registered where every stem is (`REQUIRES_STEMS`; `harness/loops.py` reads that set by owner and reports drift).
- WHERE: `engine/season/rosters.yaml` (`terms_sourced.commit`, `factions.*.compatible_with`); `engine/season/data/requires.py` (`REQUIRES_STEMS`: `admitted`); `engine/season/data/rosters.py` (the incompatibility rule); `engine/season/queries/world_q.py` (NEW `admitted_to`); `engine/season/verb_table.yaml` (`commit`: `requires_typed`); `engine/season/tests/test_fa_eligibility.py`.
- TESTS: `test_non_member_commit_refused_without_admission`, first, red; `test_faction_q.py` stays green.
- FALSIFIER and CONTROL: "G3's first reading: if computed play today contains non-member commits to factions that other persons then act on, edit 3 removes live behaviour and its cost must be stated before it lands." Control: a member's re-commit and every non-faction `commit` unchanged.
- GATE: `python -m pytest engine/season/tests/test_fa_eligibility.py engine/season/tests/test_faction_q.py -q` → pass (five tests in the new file); `python -m engine.season.harness.register --check` → exit 0; over seeds 0 to 2, two seasons: executed non-member `commit`s to rostered factions before (step 1) and after, quoted.
- HASH MOVERS: "(3) every run in which a person commits to a faction Proposition he is not in (G3's first reading)". Declared; B21.99. If step 1 reads zero at every seed, the item is EQUAL in shipped runs and the commit says so.
- DEPENDS ON: V12 B21.62; EXISTS-IN-TREE `data/requires.py::REQUIRES_STEMS`, `rosters.yaml: terms_sourced`, `rosters.yaml: factions` (`head_seat`, with the first half's `06_FA_seat_terms_by_body_B` edit 4 rows), `queries/world_q.py::members`.
- GLOSSARY: row *admission* (new if absent): "admission: a faction's acceptance of a person who asks to join, as a club admits a member; leaving stays his own `release`".
- COST and TIER: small build; `sonnet`, `high`; `opus` for the admission default (incompatible by default) only (the source's tier).
- LANDS IT: B21's producer; `Item: B21.63`, `[skip ci]`.

### B21.64 — two register rows closed, as text · `U5d_FA_owed_edits` §7 · BUILD · HASH EQUAL
- SOURCE: `U5d_FA_owed_edits.md` §7 ("Text edits to `engine/season/hole_register.yaml` rows, made in the next FA commit, no code"); rulings ED-IN-0256 (4) (authority is asked of the seat exercised); CR-25 option (b); UNDECIDED (U8).
- ADVANCES: none of the nine; the register agrees with the tree.
- INSTRUCTION: "H-91 closed by precedent (every remit verb is admitted by grant and basis, `state/gate.py:370-375`); H-144 closed (CR-25 option (b), `loop/predicates.py:403-410`)" — cited by symbol: `state/gate.py::_seat_grants` and `loop/predicates.py::_req_establish` clause 5. In the register's own closing form (rows are re-graded, never deleted; `hole:`, `kind:`, `owner:`, `unblocks:`, `source:` left as transcribed, the `H-109`/`H-33` precedent at the rows' own text): each row's `cite:` opens with "CLOSED BY U5d_FA §7 (B21.64): …" and ends "THE PRIOR CITE FOLLOWS. || " before the old text. H-144 keeps `grade: "measured"`. H-91: `grade: "absent"` → `"ruled"` `[ASSUMPTION: the precedent is Jordan's ED-IN-0256 (4), so `ruled` on H-43's precedent ("closed on the ratified … call, graded `ruled`") — basis: the row at `hole_register.yaml` (H-43); if `register --check`'s G12 refuses, `measured` with the tests `test_u7_remit.py` and `test_in31_revocation_cost.py` named]`. The third clause (the v11 card CP-T09-06) is not carried (UNDECIDED (U8)).
- WHERE: `engine/season/hole_register.yaml` (H-91, H-144).
- TESTS: none new.
- FALSIFIER and CONTROL: `register --check` fails G12 (a cite arguing for a grade the row does not carry). Control: `--requirements` loads unchanged.
- GATE: "`python -m engine.season.harness.register --requirements` still loads" → nine lines; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `hole_register.yaml` rows H-91, H-144; V12 B21.51 (CP-T09-06's edit, which the third clause named).
- GLOSSARY: none.
- COST and TIER: edit (text); `sonnet`, `medium`.
- LANDS IT: B21's producer; `Item: B21.64`, `[skip ci]`.

### B21.65 — a person's opinion of a faction regards its present head · `U5d_FA_owed_edits` §8 · BUILD · HASH MOVER(behaviour)
- SOURCE: `U5d_FA_owed_edits.md` §8; closes F-PES-FA-08.
- ADVANCES: R-08 (opinion reads the world as it stands); R-02.
- INSTRUCTION:
  1. First, "`engine/season/tests/test_faction_q.py::test_after_a_succession_opinion_of_regards_the_successor` (hand-built: after a succession the successor is the regarded head)", read red.
  2. "`engine/season/queries/world_q.py::opinion_of`: The "whom `p` regards on its behalf" clause reads `faction_q.head(w, faction)` first and falls back to the creed Proposition's subject." (`queries/` may read `faction_q`; check the import direction at the item's open: if `faction_q` imports `world_q`, read the head through the function's existing owner without a cycle and say how in the commit body.)
- WHERE: `engine/season/queries/world_q.py` (`opinion_of`); `engine/season/tests/test_faction_q.py`.
- TESTS: the named test, first, red.
- FALSIFIER and CONTROL: "A dead leader still regarded as head after his seat is filled." Control: a faction whose head seat is unchanged reads the same opinion as before.
- GATE: `python -m pytest engine/season/tests/test_faction_q.py -q` → pass; the realm hash at seed 0, one season → moved where a faction's head differs from its creed's subject, recorded.
- HASH MOVERS: "The Restoration Movement and the Löwenritter at build once TERMS-B edit 4 lands; every faction after a succession. Declared." B21.99.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::opinion_of`, `queries/faction_q.py::head`; V12 the first half's `06_FA_seat_terms_by_body_B` edit 4 (`head_seat` rows); V12 B21.64.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B21's producer; `Item: B21.65`, `[skip ci]`.

### B21.66 — a successor confirms his predecessor's writs or lets them lapse · `IS-B3-FA-06` (replaces `U5d_FA_owed_edits` §9) · BUILD · HASH MOVER(behaviour)
- SOURCE: IS-B3 `IS-B3-FA-06` (`:150-159`); `U5d_FA_owed_edits.md` §9 (replaced: "Replaces `U5d_FA_owed_edits.md` §9's edit; its gate ("the heir holds the writ") is withdrawn with it"); rulings A-21; `04` §C.2 (reading (i), no Layer 1 change); closes F-PES-FA-09.
- ADVANCES: FA standalone S5 (no dead end at a succession); R-04, R-02.
- INSTRUCTION: "**Decided, reading (i), by ladder step 3:** §C.2's enumeration is complete as ratified, so the writ is not passed. What §9 called a residue is made a played thing.
  (1) `queries/world_q.py`: a reader `writs_inherited(w, p) -> tuple`, beside `writs_held` … and `vacancies` …: the Records for which `world_q.issuing_seat(w, rid)` names a seat `p` now holds, that `p` did not himself issue, and that `p`'s own ledger holds a claim of (A-21: a decree is proclaimed, so he knows its terms if he heard it).
  (2) `questions_for` … stamps them as an occasion, as it stamps `writs_held`.
  (3) The existing `issue` row forms on that occasion with the predecessor's terms as its content: that act is the confirmation. No new verb, no new basis. A writ he does not confirm stays without a holder; its addressees still hold its terms as claims, and a `comply` or `evade / defy` on it is answered by nobody until he issues.
  (4) `06_FA_shortest_loop_B.md`'s `loop_closed.responded` counts a response by "the actor who issued a writ": it reads the confirming `issue` the same way, with no edit."
  With B21.54, `issue` forms on a Proposition: the confirming `issue`'s terms are the predecessor writ's Proposition.
- WHERE: `engine/season/queries/world_q.py` (NEW `writs_inherited`; `questions_for`); `engine/season/tests/test_in61_succession.py`.
- TESTS: in `test_in61_succession.py`, first, red: "`test_an_heir_is_asked_about_the_writs_of_the_seat_he_took`; `test_an_heir_who_heard_of_no_writ_is_asked_about_none` (the occasion is his ledger's, not the world's); `test_a_confirmed_writ_is_his_and_an_unconfirmed_one_has_no_holder`".
- FALSIFIER and CONTROL: "Control: a seat that changes hands with no writ issued through it stamps nothing, and the realm hash at seeds 0 to 2 is equal where no succession follows an `issue`."
- GATE: `python -m pytest engine/season/tests/test_in61_succession.py -q` → pass. The source's "`governance_spine play 0 6 succession` after an `issue` planted through the vacated seat: the digest shows the successor's confirming `issue` or its absence, by seed" reads `play`, which B21.72 adds: moved to B21.72's GATE (§5.8), at two seasons ("six seasons in the source; A-114").
- HASH MOVERS: "Every seeded run with a succession after an `issue`; declared." B21.99.
- DEPENDS ON: EXISTS-IN-TREE `queries/world_q.py::issuing_seat`, `::vacancies`, `::questions_for`; V12 the first half's `22_HAPPENINGS_B` edits 1–2, BIND_C and `06_FA_decree_binds` items (edit 3 renames `writs_held`); V12 B21.54, B21.65.
- GLOSSARY: none.
- NAMES: `world_q.writs_held` → `world_q.writs_addressed` (`06_FA_decree_binds` edit 3, the first half): "beside `writs_held`" and "as it stamps `writs_held`" read `writs_addressed`. `questions_for`'s `(tick, round)` key → `(tick, lap)` (B04, PCR-4).
- COST and TIER: small build; `sonnet`.
- LANDS IT: B21's producer; `Item: B21.66`, `[skip ci]`.

### B21.67 — someone may always claim an empty throne: the test · `U5d_FA_owed_edits` §1 · BUILD · HASH EQUAL
- SOURCE: `U5d_FA_owed_edits.md` §1 ("Edit. None of its own. `06_FA_remit_grant_by_row.md` edit 1's `off_widow_regent: remit_acts: []` and `22_HAPPENINGS_B_the_throne_is_never_stranded.md` edits 1–3 (as reconciled to A-19) are one batch"); rulings A-19; closes R-16's consequence, F-PES-FA-11.
- ADVANCES: R-04 (`succeed` reachable after a royal line fails).
- INSTRUCTION: the ordering constraint is met by B21 itself (both landed in the first half). Write the gate's test, which `pf1_static.py` (scratch, not in the tree, U3 §6.2) stood for: "in the file that covers `succeed` (`engine/season/tests/test_in61_succession.py`): `test_with_king_and_heir_removed_someone_may_claim_the_throne` (the built realm with King and heir removed by hand: at least one person may claim `off_king`)". "May claim" is eligibility (`state/gate.py::may_claim`, with the A-19 claimants), not the draw's outcome.
- WHERE: `engine/season/tests/test_in61_succession.py`.
- TESTS: the named test; green on landing (the first half's edits already make it true); read red with the first half's REMIT edit 1 applied and `22_HAPPENINGS_B` edits 1–3 reverted in a scratch worktree, the reading in the commit body.
- FALSIFIER and CONTROL: "Zero eligible claimants in that world." Control: with the King alive, `off_king` is not claimable (no vacancy).
- GATE: `python -m pytest engine/season/tests/test_in61_succession.py -q` → pass.
- HASH MOVERS: none of its own ("The realm hash (the row's grant is hashed); declared in REMIT", the first half's).
- DEPENDS ON: V12 the first half's `06_FA_remit_grant_by_row` edit 1 and `22_HAPPENINGS_B` edits 1–3; EXISTS-IN-TREE `state/gate.py::may_claim`; V12 B21.66.
- GLOSSARY: none.
- COST and TIER: edit (a test); `sonnet`.
- LANDS IT: B21's producer; `Item: B21.67`, `[skip ci]`.

### B21.68 — a faction's weight reads where its members live · `U5d_FA_owed_edits` §4 · BUILD · HASH EQUAL
- SOURCE: `U5d_FA_owed_edits.md` §4; rulings A-41, A-42, A-14; U1 ledger F-12; `04` §B.3 ("NEVER: any social aggregate" on a Rung).
- ADVANCES: none of the nine at once; the one owner of a faction's weight that B21.69 and B32's ballots read.
- INSTRUCTION:
  1. "the datum's owner is a table keyed by territory id, `engine/season/rosters.yaml: tables.territory_weight` (U1 ledger F-12), loaded and refused at import by `data/rosters.py` (a key that is no territory of the geography; a value that is not a positive number). No `Rung` field is added … An absent key reads 1.0." The table ships empty (`{}`): "The numbers are content `[ASSUMPTION; Jordan to author]`" ("lowered for the southern Einhir territories"); DIALS AT CONTROL (this half).
  2. "`faction_q.weight(w, f) -> float`: the summed `Person.weight` of members, each multiplied by the political weight of the territory he resides in (default 1.0 …). No stored aggregate. First readers: instruments, then the councils and elections of the institutions kit (`15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`), where the weight sets a voter's draw (A-14), never a count."
  3. First, `engine/season/tests/test_faction_q.py::test_faction_weight_at_unit_territory_weights_is_the_unweighted_sum` and `::test_a_territory_weight_key_that_is_no_territory_is_refused` `[ASSUMPTION: test names; E-3]`, read red (no `weight`).
- WHERE: `engine/season/rosters.yaml` (`tables.territory_weight`); `engine/season/data/rosters.py` (its loader and refusals); `engine/season/queries/faction_q.py` (NEW `weight`); `engine/season/tests/test_faction_q.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: "A reader that gates an act on the weight, or a stored copy of it." Control: "with every weight 1.0 it equals the unweighted sum".
- GATE: `python -m pytest engine/season/tests/test_faction_q.py -q` → pass; `python -c` printing `faction_q.weight(w, f)` for each rostered faction at `build_realm(0)` → each equals the summed `Person.weight` of `world_q.members(w, f)`, printed and quoted. The source's print through `harness/governance_spine.py`'s digest reads B21.72's `digest`: that arm is moved to B21.72's GATE (§5.8).
- HASH MOVERS: "None until a chooser term or a ballot reads it."
- DEPENDS ON: EXISTS-IN-TREE `state/carriers.py::Person.weight`, `queries/world_q.py::members`, `rosters.yaml: tables`, `data/files.py::GEOGRAPHY_YAML` (`systems/settlements/valoria_geography_v30.yaml`, whose `provinces` rows are the territories the loader checks keys against); V12 B21.67.
- GLOSSARY: row *weight (of a faction)* (if absent): "a faction's weight: how much its members count, summed over the members and scaled by where each lives, as a vote is weighted".
- COST and TIER: small build; `sonnet`.
- LANDS IT: B21's producer; `Item: B21.68`, `[skip ci]`.

### B21.69 — a reduction of a sitting holder's grant is a revocation, drawn against the two factions' power · `IS-B3-FA-07` (H-132; A-105) · BUILD · HASH MOVER(behaviour)
- SOURCE: IS-B3 `IS-B3-FA-07` (`:161-170`); rulings A-105 (Jordan: *"the amount of power over the foreign officer is determined by the power dynamics between the foreign faction and the host faction … the king's appointee stays in place unless king convinced otherwise"*), A-35; `V12_STRUCTURE.md` D-01 (H-132 lands here; B21b's H-132 entry is a pointer to this item); `L1-A105` APPLIED (`faction_power_step` 0, the draw's power term); closes H-132 (b)'s `[ASSUMPTION]` clause; UNDECIDED (U4).
- ADVANCES: FA standalone S3 (whose officers a lord can touch); R-04.
- INSTRUCTION (the tree at `aa31fd2` matches the source's reading by symbol: `loop/predicates.py::_req_establish`'s last clause, "A REDUCTION IS A PARTIAL REVOCATION", asks `may_revoke`; `state/gate.py::tenure_write_basis` returns `CONFERRAL` for `opened or moved == {"payload"}` under `may_fill`):
  1. "**`state/gate.py::tenure_write_basis`, one clause** before the `CONFERRAL` return …: a payload-only change to a live seat-`hold` whose new grant drops an act the old one carried (`set(was.granted_acts) - set(t.granted_acts)` non-empty) is a partial revocation; it returns `T_O` when `may_revoke(w, actor, via, seat)` and `None` otherwise, never `CONFERRAL`. The gate then says what clause 5 says, and clause 5's "stricter than the gate" sentence is deleted."
  2. "**The draw.** A reduction is carried by `revoke`'s contested row (`14_VERBS_BINDING_C_turnover.md` commit C2 step 6: prize a seat, counterparty the holder, A-35's resistible draw) with one new optional operand, `keeps` (the acts the holder keeps; absent = today's full revocation): on the bands that unseat, `_eff_revoke` (`loop/effects_governance.py`) re-stamps the holder's `granted_acts` to `keeps` instead of closing the `hold`; on a Failure nothing is written and `revocation.resisted` is emitted as for a whole strip. `_req_establish` clause 5 then refuses (`_refuse("reduction_is_revocation", …)`) a re-stamp that narrows a sitting holder's grant, so one verb, one draw, one gate basis carries every revocation." `[ASSUMPTION: the `keeps` operand on `revoke` rather than a contested branch inside `establish` — basis: … A-105 says "judged as a revocation"; revert: keep clause 5 as eligibility only and add no draw]` (the source's).
  3. "**The power term.** `revoke`'s obstacle terms (`rank_gap`, `stakes`, `reception`, BIND_C's table) gain one member, `faction_power`, of the one obstacle owner (`U5c_SC_one_obstacle_form.md`, OBS): zero when the holder's faction (`queries/world_q.py::faction_of(w, holder)` …) equals the host's (`w.offices[a.via].faction` …); otherwise `faction_power_step` times the signed band of the ratio `faction_q.weight(w, holder_faction) / faction_q.weight(w, host_faction)` (… the one owner of a faction's weight; no second power reader), harder when the holder's faction is the stronger. The term is read host-side at RESOLVE (the obstacle composer may read `World`); `state/` reads no Query. Setting `faction_power_step` in `data/fixtures.py`, control `0` (hash EQUAL), with its `hole_register.yaml` row." `faction_q.weight` is B21.68's. "*"Unless the king is persuaded"* is not a branch: persuading the appointing faction's head is that head's own act (his `revoke`, or his `release` of the appointee), reached by the ordinary social verbs." The "signed band of the ratio" is the composer's existing band reader for a ratio where one exists `[ASSUMPTION: the bands are OBS's; where OBS has no ratio band, the producer writes the three bands below 1, 1, above 1 and names them in the commit body — basis: IS-B3 states "signed band" and no table]`.
  4. "**Rarity.** Foreign-faction holders stay uncommon by the routes already proposed: `16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md` decision 2 prices cross-chain conferral (`cross_chain_step`)" (B21.61). The two choices IS-B3 left are taken as written: odds, not refusal, against a stronger faction (`[ASSUMPTION: a large `faction_power_step` approximates "cannot" without a second gate; revert: refuse at eligibility when the holder's faction is the stronger, unless its head consents]`); power is political weight (`faction_q.weight`), not armed strength (`[ASSUMPTION — basis: U5d_FA §4; revert: a second Query of armed strength, read here instead]`).
- WHERE: `engine/season/state/gate.py` (`tenure_write_basis`); `engine/season/loop/predicates.py` (`_req_establish` clause 5, `_req_revoke` for `keeps`); `engine/season/loop/effects_governance.py` (`_eff_revoke`); `engine/season/verb_table.yaml` (`revoke`: the `keeps` operand); `engine/season/rosters.yaml` (`obstacle_terms`: `faction_power`); `engine/season/data/fixtures.py` (`faction_power_step`); `engine/season/hole_register.yaml` (one NUMBER row); NEW `engine/season/tests/test_grant_reduction.py`.
- TESTS: in the new file, first: "`test_a_gate_write_narrowing_a_sitting_grant_needs_a_revocation_basis` (a bare gate write that narrows `granted_acts`, by an actor whose seat may fill but may not revoke: `None`; red before step 1, which admits it as `CONFERRAL`); `test_an_establish_that_narrows_a_sitting_grant_is_refused_and_a_revoke_with_keeps_carries_it`; `test_a_foreign_holders_reduction_is_harder_against_a_stronger_faction` (200 dice seeds per arm, the holder's faction weight above and below the host's, success shares strictly ordered, `assert checked >= 200`)" — the third at `faction_power_step` set to 1 inside the test only (the shipped value stays 0) `[ASSUMPTION: the test's arm value — basis: at 0 the shares cannot order]`.
- FALSIFIER and CONTROL: the tests above; "control: the same-faction arm, whose shares do not move with the weights; and `faction_power_step = 0` reproduces the realm hash at seeds 0 to 2."
- GATE: "`python -m pytest engine/season/tests/test_grant_reduction.py -q`; the realm content hash at seeds 0, 1, 2 equal to B21's base with `faction_power_step = 0`" — read as: equal to B21.68's reading where no `establish` narrowed a sitting grant (step 2's mover, below, is the declared exception, its count quoted); `python -m engine.season.harness.register --check` → exit 0; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: "Step 1: none reachable (clause 5 already refuses every write it narrows) `[UNVERIFIED: not run]`. Step 2: every seeded run in which an `establish` narrowed a sitting grant (it is refused and the `revoke` forms instead); declared, B21's one re-pin. `faction_power_step` above 0: a declared mover", set by B98 (DIALS AT CONTROL).
- DEPENDS ON: V12 the first half's BIND_C items C2, C3 (`revoke` contested, `_eff_revoke` banded); V12 B21.68 (`faction_q.weight`), B21.61 (`cross_chain_step`); Batch B05 (`U5c_SC_one_obstacle_form`: the composer and `obstacle_terms`); EXISTS-IN-TREE `state/gate.py::tenure_write_basis`, `::may_revoke`, `::may_fill`, `T_O`, `CONFERRAL`, `queries/world_q.py::faction_of`, `loop/predicates.py::_req_establish`; `U5d_FA_owed_edits` §3 is B32's and is not read (UNDECIDED (U4)).
- GLOSSARY: none (*revocation* stands; "reduction" is plain English).
- IDS: H block slot 2 (`faction_power_step`'s NUMBER row).
- COST and TIER: small build; `sonnet`; `opus` for the term's form.
- LANDS IT: B21's producer; `Item: B21.69`, `[skip ci]`.

### B21.70 — one purse per rung · `U5d_FA_owed_edits` §6 · HELD (a computed `requisition` lands on a rung seating two factions)
- SOURCE: `U5d_FA_owed_edits.md` §6 ("Decision (kept). One store carrier (`Rung.stores`); a seat row may name `treasury: <rung>`, default its own rung. Built only when a computed `requisition` lands on a rung seating two factions."); closes nothing yet (R-07, H-352).
- What it holds: the decision and its owner when built ("`offices.yaml` row key and `state/carriers.py::Tenure.seat_rung`'s writer"). No edit in B21.
- The trigger reading, taken at B21.99 and quoted in the close: "`requisition.taken` Events whose rung carries seats of two factions, counted over realm seeds 0–2" (two seasons). If it reads above 0, the trigger has fired: by `V12_STRUCTURE_part3.md` §7.9 it becomes an item of this batch (a BUILD of the `treasury:` key, owner as above), or `STOPPED` if B21 has closed; at 0, the entry goes to the held table with this trigger.
- LANDS IT: no commit of its own; the reading is a line of B21.99's commit body.

The batch continues at B21.71 in this part's continuation file (`_cont`), which holds B21.71 to B21.99, the batch's SERIAL EDGES and FILE CENSUS lines for this half, and the boundary row.

