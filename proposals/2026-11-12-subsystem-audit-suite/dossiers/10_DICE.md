# Dossier 10 · DICE — Resolution substrate: dice engine, sigma-leverage, engine_params exports

> Built by script (`collate.py`, deterministic) from the working tree. **An index, not a verdict.** Classification is by path rule, lane tag, batch card or keyword and is marked `class:` where it is not a path; overrule it when the source says otherwise. Counts are readings at generation time (CLAUDE.md §1). Design documents are reference, not mechanism (§0.05).

## Code inventory (path — lines — module docstring line) — 19

- `engine/engine_params/battle_orders.json` — 27 lines
- `engine/engine_params/combat_engine_v1.json` — 460 lines
- `engine/engine_params/composition.json` — 119 lines
- `engine/engine_params/descriptors.json` — 193 lines
- `engine/engine_params/game_constants.json` — 53 lines
- `engine/engine_params/names.json` — 273 lines
- `engine/engine_params/sim_params.json` — 3641 lines
- `engine/engine_params/value_pointer_links.json` — 827 lines
- `engine/substrate/__init__.py` — 17 lines — engine.substrate — the engine's leaf readers.
- `engine/substrate/battle_orders.py` — 24 lines — engine.substrate.battle_orders -- the standing order of battle's closed sets, read from the cooked artifact.
- `engine/substrate/combat_kit.py` — 33 lines — engine.substrate.combat_kit -- what the personal-combat engine can be armed with, read from its export.
- `engine/substrate/composition.py` — 69 lines — engine.substrate.composition — resolve a ROLE to a subsystem callable, without naming it.
- `engine/substrate/descriptors.py` — 196 lines — engine.substrate.descriptors — the SOLE runtime reader of the descriptor registry.
- `engine/substrate/names.py` — 108 lines — engine.substrate.names — canonical naming, read from references/. One owner for a TERM.
- `engine/substrate/pc_engine.py` — 50 lines — engine.substrate.pc_engine — THE ONE PATH SEAM into modules/combat/ (the personal-combat engine).
- `engine/substrate/stubwire.py` — 84 lines — engine/substrate/stubwire.py — the single owner of "explicitly-flagged not-built".
- `engine/dice_engine/__init__.py` — 17 lines — engine.dice_engine — the DICE ENGINE: the d10 chain, degree_from_net and sigma leverage, which the host and
- `engine/dice_engine/dice_engine.py` — 311 lines — engine/dice_engine/dice_engine.py — d10 dice pool, TN values, degree of success, continuous engine
- `engine/dice_engine/sigma_leverage.py` — 468 lines — engine/dice_engine/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.

## Tests that exercise this subsystem (by filename rule; unclassified tests are in 99_cross_cutting.md) — 12

- `engine/season/tests/test_odds_of.py` — 290 lines
- `engine/tests/test_band_odds.py` — 119 lines
- `engine/tests/test_knots_ed912.py` — 175 lines
- `engine/tests/test_sigma_leverage_parity.py` — 619 lines
- `tests/valoria/test_band_extension_seam.py` — 183 lines
- `tests/valoria/test_degree_boundary_epsilon.py` — 180 lines
- `tests/valoria/test_degree_ladder_single_owner.py` — 477 lines
- `tests/valoria/test_dice_engine_properties.py` — 150 lines
- `tests/valoria/test_engine_params_bridge.py` — 297 lines
- `tests/valoria/test_fractional_pool.py` — 76 lines
- `tests/valoria/test_knot_pool_formula.py` — 57 lines
- `tests/valoria/test_per_die_one_owner.py` — 48 lines

## Hole-register rows, primary (full row at the register line; `closed?`/`open?` is a keyword hint on the cite, NOT a verdict — verify) — 9

- **H-31** (reg line 334) tier 1 · assumption · FORMULA · open? · class:path — the degree ladder's margin model | owner: params (the one ladder) | site: engine/dice_engine/dice_engine.py::degree_from_net (`margin = net - ob`), read through eng | unblocks: every contest
    - cite: PLAN §3.2. Shape ruled by #353 :1400-1401 VERBATIM: "There is one degree ladder for every scale of the game -- four bands read off the margin, never off the obstacle's size. A duel, a debate, a siege and an examination all use it." ⚠ THE SWEEP WAS ON THE WRONG AXIS AND IS CORRECTED. It swept three b
- **H-88** (reg line 1090) tier 0 · assumption · WIRING · open? · class:path — the seam does not DISPATCH. S39's `contest()` is one generic function that raises on a degree ladder nobody wrote -- but the three subsystems a contest belongs to are BUI | owner: the seam (RESOLVE) -- the subsystems themselves are built and out of this chain | site: seam.contest_subsystem, called by seam.contest before the generic ladder refusal | unblocks: every verb that declares `contests:`, and W7's deg
    - cite: JORDAN, 2026-09-02, VERBATIM: *a contest seems like it can be a call for a different subsystem like personal combat, mass battle or social contest.* He is right and the tree agrees: all three modules exist in references/module_contracts.yaml with real docs, sim modules and declared resolvers -- pers
- **H-98** (reg line 1363) tier 0 · absent · COLLISION · open? · class:path — ⚠⚠ GRADED 2026-10-01 BY WHAT IS STILL OPEN (plan position `8`): TWO OF THIS ROW'S THREE THINGS ARE CLOSED AND ONE IS NOT, SO THE GRADE STAYS `absent` ON THE STRICTEST PAR | owner: S39.4's ladder and the subsystem's return type | site:  | unblocks: every verb that declares `contests:`, and whatever
    - cite: HELD BY IN-43 (batch B-C, 2026-10-08), grade unchanged: the fourth band has no source in the data and is not invented (the row's own text: (a) the margin producer and (b) the wound-count edge are closed, the fourth band alone is open). || PRIOR CITE, KEPT: FOUND BY BUILDING THE CALL Jordan ruled for
- **H-114** (reg line None) tier 0 · measured · FORMULA · open? · class:path — `_eff_kill` (engine/season/loop/effects.py::_eff_kill) TAKES NO DEGREE PARAMETER, so the effect that computes the VALUES cannot honour the branch `writes_at` selected. Wo | owner: `_eff_kill` - the effect signature carries no degree | site: proposals/2026-09-04-degree-sweep/arm3_tree.py::fold_one | unblocks: `H-98`'s outcome model - the bands are unbuildable
    - cite: MEASURED 2026-09-04. SCOPE NARROWED AFTER AN ADVERSARIAL PASS - a first statement claimed every computed act is lethal because §F1's Candidate carries no operands (`H-80`). FALSE - a computed act omits `subject` too, so `_eff_kill` returns early at engine/season/loop/effects.py::_eff_kill and the fo
- **H-115** (reg line None) tier 1 · measured · WIRING · open? · class:path — THE FOUR DEGREE BRANCHES ARE THE ONLY RUN-TIME REFUSALS IN `loop/driver.py` THAT BYPASS THE TYPED GAP TAXONOMY. `writes_at` and `emits_at` raise `SystemExit` (engine/seas | owner: `writes_at` / `emits_at` - the raise type, not the raise | site: proposals/2026-09-04-degree-sweep/arm2_onramp.py::run_2c | unblocks: reporting a degree gap as a gap once the contest b
    - cite: MEASURED 2026-09-04, static and dynamic. Split verified independently by a read-only critic - all 18 raises enumerated at 365, 383, 395, 454, 708, 712, 728, 733, 743, 749, 776, 785, 791, 800, 808, 813, 821, 825; the 14 sit in the three loaders, the 4 in the degree readers.
- **H-152** (reg line 3439) tier 1 · assumption · PRODUCER · open? · class:path — A `total`-CASUALTY-MODEL MARCH LOSS KILLS WITH NO `person.died` EVENT. `_eff_march`'s `total` arm sets a loser's body to 0 and calls `w.remove_person`, on `_eff_kill`'s o | owner: no owner exists yet -- the candidate site is `loop/effects.py::_eff_march`, which would ne | site: engine/season/loop/effects.py -- `_eff_march`'s `total` branch, the `w.remove_person(pid)` | unblocks: a `total`-model march death being visible to anyth
    - cite: FOUND by `valoria-critic`'s second correctional pass, on the review round's own fix. ⚠ ONE HALF OF THAT REPORT'S FINDING IS NOT A REAL DEFECT, CHECKED RATHER THAN REPEATED: the report also read `remove_person` as riding an illegal write against `write_matrix.yaml`'s step column for `(Person, exists)
- **H-244** (reg line 5045) tier 1 · assumption · NUMBER · closed? · class:path — WHAT ONE SLOT OF `effort` IS WORTH (CP-T01-05, B10-08). An act may carry `effort` 0, 1 or 2 in its payload; it fills `1 + effort` of its scene's interaction slots and eac | owner: Jordan, who corrects the assumption; `seam/wrappers/sigma.py::ADVANTAGE_SOURCES` (the `eff | site: Fixtures effort_level (`data/fixtures.py`, CP-T01-05), read ONLY by `seam/wrappers/sigma.p | unblocks: a player who puts a whole scene behind one roll th
    - cite: BUILT at CP-T01-05 (B10-08), hash EQUAL at the shipped chooser, which forms no effort (the channel sums to 0.0 and `Scene.slots == len(acts)`). FIGURES RE-COMPUTED ON THIS TREE with `band_odds` (fraction rule, per-pool ceiling): pool 2 against Ob 2, F / P / S / O in % at effort 0 / 1 / 2: 74.00 / 19
- **H-310** (reg line 5916) tier 1 · measured · RULING · open? · class:path — A CONFESSION IS GRADED BY THE DICE AND NEVER BY WHETHER THERE IS ANYTHING TO CONFESS (premise-check, interrogation). `interrogate`'s verdict reads custody and the charge  | owner: `engine/season/loop/predicates.py::_req_interrogate` (custody and charge are the only read | site:  | unblocks: an interrogation whose result depends on what the 
    - cite: MEASURED at EXECUTES on the `_world` fixture of `engine/season/tests/test_in12_interrogate.py`, n=200 per pool setting, a fixture and not canon. The agent's own count was 381 of 400 at pool 30. Nearest: H-226 (the row writes nothing at any band; K-56 and P58 name the held-object route and are open).
- **H-312** (reg line 5940) tier 1 · measured · WIRING · open? · class:path — `interrogate` HAS NO CONTEST KEY, SO NEITHER THE QUESTIONER'S SKILL NOR THE SUBJECT'S RESISTANCE ENTERS (premise-check, interrogation). `interrogate` is not in `verb_capa | owner: `engine/season/rosters.yaml` (`verb_capability`); `engine/season/seam/wrappers/pool.py` an | site:  | unblocks: an interrogation that a skilled questioner wins mo
    - cite: MEASURED by the agent, exact odds, not re-run by the author. Same class as H-126 (which capability key a contested verb draws from); no `interrogate` instance is named there. The choice of key is an [ASSUMPTION] left to the owner.

## Hole-register rows that touch this subsystem but are primary elsewhere — 3

- H-332 (reg line 6180) — `systems/fieldwork/sim/knots.py` IS CORRECT AND UNPLUGGED, WITH THREE EDGES (premise-check, threads). `form_knot` formed in 216 of (primary: FI)
- H-349 (reg line 6424) — ARMOUR `none` AND `light` DO NOT DIFFER IN A FIGHT, AND LIGHT SURVIVORS ARE HURT MORE OFTEN (premise-check, combat). Against an ar (primary: PC)
- H-361 (reg line 6541) — A STANDING ORDER OF BATTLE'S ROLE MOVES THE FIELD AGAINST ITS ORDERER UNDER THE SHIPPED FRICTION, AND THE INFANTRY MENU IS COSMETI (primary: CHAR)

## Plan entries and sections (parts 2, 4–17), by heading — 6

- part4:84 CR-17 — Believed odds weight the alignment term; τ re-derived as the series' last commit (IN) · LANDED in B10-09 close two (record `55b7543f..1ef8d273`; the Item commit is `3a406d60`) (class:keyword)
- part13:229 CP-T01-01 — REPAIR (B10-08) · AM-B-01 (class:handle)
- part13:236 CP-T01-02 — LIMIT (B10-08) · AM-B-02 (class:handle)
- part13:242 CP-T01-03 — NARROW (B10-08) · AM-B-03 (class:handle)
- part13:249 CP-T01-05 — NARROW (B10-08) · AM-B-04 (class:handle)
- part13:257 CP-T01-06 — REPAIR (B10-08) · AM-B-05 (class:handle)

## Proposals (proposals/): path — size — title — Status line — 2

- `proposals/2026-08-19-roll-and-resolution-inventory.md` — 230 lines — Roll and Resolution Inventory — every dice call, every obstacle, and everything that resolves without the engine — ## Status: FINDINGS — mechanical inventory, AST-extracted. No design, no rulings. No `.py` touched. Compliance bookkeeping light per Jordan  (class:keyword; hits 5)
- `proposals/2026-09-04-degree-sweep/` — 55 files, 28708 lines — Degrees of success across the ARC and NPC corpus — what 143 cases have never exercised — ## Status: **INSTRUMENT HOME — the `wd_*` scripts are R-01 and R-02's `measure:` (`engine/season/requirements.yaml`); the documents are refe (class:keyword; hits 2)

## Research (research/) — 1

- `research/game_precedent_suite/dispositions/D_T01.md` — 59 lines — D_T01: dispositions for T01 (resolution and dice; suite file 02) (class:keyword)

## FULL DESIGN DESCRIPTIONS for this subsystem (quarantined `.designs/`; ARCHIVED-NOT-CANON: READ IN FULL for intent, vocabulary and history; never cite as the reason a behaviour is correct). `_index`/`_infill` files are parts of the document of the same stem — 4

- `.designs/engine/mc_v18_walkthrough.md` — 11 KB — 
- `.designs/engine/sigma_leverage_engine_armature.md` — 26 KB — 
- `.designs/engine/sim_reference_CONVENTIONS.md` — 3 KB — Status: [PROVISIONAL — Pass 2l armature scaffold 2026-05-17]
- `.designs/engine/sim_reference_README.md` — 6 KB — 

## Cross-cutting design descriptions every lane reads (same status as above) — 17

- `.designs/systems/_architecture/reference/auto_manual_resolution_duality_v1.md` — 9 KB — ## Status: Doctrine RULED 2026-07-08 (Jordan) — forks A/B/D resolved; fork C (calibration tolerance) the one residual, c
- `.designs/systems/_architecture/reference/campaign_architecture_v30.md` — 19 KB — ## Status: CANONICAL — approved by Jordan 2026-04-17
- `.designs/systems/_architecture/reference/campaign_architecture_v30_index.md` — 5 KB — 
- `.designs/systems/_architecture/reference/campaign_modes_v30.md` — 10 KB — 
- `.designs/systems/_architecture/reference/campaign_modes_v30_infill.md` — 6 KB — 
- `.designs/systems/_architecture/reference/cogload_moderate_target.md` — 16 KB — 
- `.designs/systems/_architecture/reference/cogload_moderate_target_index.md` — 5 KB — 
- `.designs/systems/_architecture/reference/companion_app_design_note.md` — 2 KB — 
- `.designs/systems/_architecture/reference/complete_systems_reference.md` — 16 KB — ## Status: PARTIALLY SUPERSEDED (combat sections) — banner added 2026-07-01 (ED-1084)
- `.designs/systems/_architecture/reference/conflict_architecture_proposal.md` — 20 KB — ## Status: CANONICAL
- `.designs/systems/_architecture/reference/early_game_ignition_analysis.md` — 36 KB — 
- `.designs/systems/_architecture/reference/engine_atlas_v1.md` — 38 KB — ## Status: REFERENCE — consolidation only; authors and ratifies nothing
- `.designs/systems/_architecture/reference/integration_proposal_v30.md` — 62 KB — 
- `.designs/systems/_architecture/reference/integration_proposal_v30_index.md` — 6 KB — 
- `.designs/systems/_architecture/reference/throughlines_complete.md` — 52 KB — 
- `.designs/systems/_architecture/reference/videogame_mode_spec.md` — 17 KB — ## Status: CANONICAL — single-mode extraction reference for Godot implementation
- `.designs/systems/_architecture/reference/videogame_mode_spec_index.md` — 3 KB — 

## Surviving audit corpus (`.audit/`, HIDDEN; lesser weight than `.designs/`; read for context and referents: what earlier audits found and how, never as authority or as a to-do list) — 2

- `.audit/2026-08-12-degree-vocabulary-census/` — 2 files, 17 KB — Degree-of-success vocabulary — behavioural equivalence census (entry: `.audit/2026-08-12-degree-vocabulary-census/00_findings.md`) (class:keyword)
- `.audit/2026-08-14-degree-reband-consumer-cost/` — 1 files, 1 KB —  (class:keyword)
