# Digest tests1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane `tests1`: 70 files under `engine/season/tests/` (test files and three helper modules), read in assignment order. `F-TEST-nn` ids are those of `audits/01_CORE_audit_addendum_C_tests.md` (read first). Where a file is a hash pin or a count pin that is stated per entry.

### engine/season/tests/_closure_scan.py
- **What it is:** helper module (not a test), SC-01 step 16 / v9 FI-03 (`ED-FI-0002`); the one AST walk for scripting drift on literal ids.
- **Status:** none stated; reading: live.
- **Bears on:** CORE, FI, SC, PROCESS.
- **Content that matters:**
  - `branches_on_ids(tree, ids)` reports `(line, id)` for an `ast.Compare` or `MatchValue` whose operand is a string literal (or tuple/list/set of them) in `ids` (:20-38). Nothing here asserts; callers (`test_sc01_the_bar.py`, `test_fi03_trail.py`) keep their own floor, membership assert and planted falsifier (:5-6).
  - Declared blind spots: a dict keyed by the id, `.get("<id>")`/any call argument, a named constant, a runtime-built id, an f-string (:9-11). "A lookup is not a branch." So the scan observes branching, not data-keyed special-casing.
  - `game_code()` scope: every `.py` under `engine/season/` outside `tests/` (harness included) plus `modules/**/*.py`; `engine/` outside `season/` is NOT scanned (:41-45).
- **Conflicts / stale:** none found. Scope excludes `engine/substrate` etc., so a branch there is unseen.
- **Open items:** none.

### engine/season/tests/_fresh_process.py
- **What it is:** helper module; shared runner for the three module-entry tests (social_contest, combat, mass_battle).
- **Status:** none; live.
- **Bears on:** CORE, PC, MB, SC (the "reached by composition row, not by import" seam).
- **Content that matters:**
  - `entry_target(prize)` resolves the composition row a contest prize row names in `module_entry:` and returns `(role, composition.ROLES[role]["target"])`; asserts the row still names one (:15-19).
  - `probe(script, target, timeout)` runs a formatted script in a fresh interpreter at the repo root, asserts return code 0 and `eval`s the last stdout line (:22-29): the only way to observe which repository files an import loaded.
- **Conflicts / stale:** `eval` of subprocess stdout is its own probe's repr, noted at :29. None.
- **Open items:** none.

### engine/season/tests/_scar_helpers.py
- **What it is:** helper module for the IN-08 scar tests (H3, H11, H13) and G4/6f; shared builders.
- **Status:** none; live.
- **Bears on:** CORE, PC, CHAR (scars), FA (affiliations/engagement tables).
- **Content that matters:**
  - `party_state(...)` builds one party's `wound_state` entry in the shape `seam/wrappers/combat.py::_wound_state` lifts it; CP-T03-00 note: `_eff_kill` reads each party's band off the scene (`party_degree`), so a hand-built scene carries both parties (:19-24).
  - `fight(w, aid)` folds `p_low fight p_mid` with a `wounded()` resolution through the real `SeasonDriver._fold` and an ACTS token (:33-39): the common "hand-built Act through `_fold`" shape F-TEST-01 counts.
  - `rebound(**cells)` overlays columns on `A.ENGAGEMENT`; `incompatible_pairs`/`compatible_pairs` read `A.INCOMPATIBLE` and `rosters.AFFILIATIONS` (:47-63).
- **Conflicts / stale:** none.
- **Open items:** none.

### engine/season/tests/test_aperture.py
- **What it is:** test file for `harness/aperture.py` (the populated-realm formability-and-execution instrument), REM-10/11, CR-14, CR-18 additions; v10 era.
- **Status:** none; live (addendum C keeps it on purpose as an instrument-grader tested on known data).
- **Bears on:** CORE, FA, FI, CHAR (instrument over the funnel; death census, wrong-kind refusals).
- **Content that matters:**
  - Pins the instrument, never its numbers (:5-8). Control: `A.measure_world(populated.build_realm, 0, 1)` ends in the same `content_hash()` and act count as `populated.run` (:73-83), so watching does not perturb; the same on the governance spine (:119-127). Asserts `attempted` non-empty so the funnel check cannot be vacuous (:96-103).
  - Counterfactual honesty: re-aggregating delivered questions under the shipped rule reproduces the chooser's question at every deliberation, `rule_mismatch == 0` (:86-93).
  - `corpus_run.attempts` reads the ACT STORE and sees an admission-refused `speak` that `d.resolved` never holds; test asserts the fold set lacks it so the assertion can fail (:165-183), with a recorded mutation (:172-173).
  - Graded loss (HR-8): a lost `tell` is NOT a graded loss since CP-T05-03 split `tell.refused` off (`news.untold` on `emits:` alone) (:246-263, :410); a `Failure` `research` (`finding.none`) is; swept over 80 act ids with a raise if the band is never drawn (:233-243).
  - CR-14 wrong-kind refusal classes (`collection`, `record_in_collection`, `absent`, `docket`, `after`) asserted per act on four planted attempts, classes sum to refused (:531-554); a person present until a `person.died` precedes the act, a death after leaves him present (:557-590); death census reads seats as of season start (:607-623). `test_cr14_death_census_names_the_killing_acts_verb...` needs `wound_harm_model="total"` to get a kill (:636).
  - Hard-coded: `test_aperture_seats_agrees...` relies on `build_realm` seating NPC-020 twice (King and Duke of Valorsmark, `13d-iii`), asserts `len(table) < seats` (:106-117). CR-18: pools line reads the rolled pool; a season-1 run reads only `pool_default` (:752).
- **Conflicts / stale:** imports test helpers across files (`test_fi01_graded_inquiries`, `test_u7_remit`, `test_in45_carry`, `test_h206_...`, `test_migrate_capacity`): a rename in any breaks this file. Docstring at :628 says "Skipped where the personal-combat engine is absent" but the test has no skip, it asserts `i is not None` (cf. F-TEST-11, skip vs fail).
- **Open items:** none.

### engine/season/tests/test_belief_contradicts_actor.py
- **What it is:** unit test, v9 IN-15 / H-201, `epistemic.belief_contradicts(..., actor=)`.
- **Status:** none; live.
- **Bears on:** FI, SC, CHAR (belief reader).
- **Content that matters:**
  - Three spy-on-`evaluate` tests: default binds the person as `actor` (:41-45); `actor=` rebinds the cell's `actor` operand (:48-52); the ledger read stays the witness's own, the reader's `_claims` equal the person's ledger (:55-61). Docstring names the three mutations that must redden it (:6-8). Every assertion has `len(spy.calls)==1` first so it asserts it reached `evaluate`.
  - `_typed_row()` picks the first verb row in sorted order with `requires_typed` not None, so which verb is exercised depends on table order [UNVERIFIED which].
- **Conflicts / stale:** none. Reads a private `_claims` attribute of the reader.
- **Open items:** none.

### engine/season/tests/test_arrangements.py
- **What it is:** loader/unit test for `data/arrangements.py` (plan position 18 PROC-A part 3), edited through SC-03a, SC-04, v10 SC-04, CR-34, SC-08.
- **Status:** none; live.
- **Bears on:** SC, FA (proceedings arrangements), CORE (loader refusals).
- **Content that matters:**
  - Pins the seeded set exactly: nine arrangements (`arbitration, parliamentary_debate, council_of_state, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation, negotiation`) with key-by-key rows; `len == 9` is a COUNT PIN that must be re-edited each time a row is seeded (:31-71). `succession` is asserted ABSENT (:71) and `test_a_hold_disposing_row...` (:286-323) shows why: `determine` has no site that opens a `hold`, so C-1 would name it.
  - Three disposal kinds appear: `bench`, `declared` (only `excommunication_deliberation`, `quorum: 2`), `mutual` (only `negotiation`, `bench_basis: none`, deciders are the parties) (:54-70). `records_dissent:false` on negotiation is "cited rather than re-decided" (:62).
  - Loader refusals each planted by a single edit with the loader's own `SystemExit` message matched: unknown key (`scale`), `declared` row with no `quorum:`, `quorum:` on a non-declared row, a speech kind with a `reachable_bands` outside the ladder (:144-240). Only `impugn_motive` carries a cap, `("Partial",)`; the other five speech kinds have none (:86-95).
  - C-1 report `arrangements_without_a_disposal_opener()` is `[]` today, the "red as designed" at plan position 19 (:243-262); a control empties `_OPENERS_FROM_EFFECTS["oblige"]` and the report names `["arbitration","negotiation"]` (:265-283). Whether C-1 should now be a LOAD REFUSAL is left open (:256-258).
  - SC-08: two subprocess tests prove the loader fires in the headless production run: control reads `sys.modules` before import; plant adds a `scale:` key to a scratch copy of the YAML and the headless run exits non-zero naming row and key, while the unplanted run prints `CONTENT HASH:` (:354-387).
- **Conflicts / stale:** docstring :7 says "NINE seeded games ... SIX seeded speech kinds"; test name "a_fifteenth_key" (:144) is a stale count of keys (the row now has more). Test names carry history ("another", "fifteenth").
- **Open items:** C-1 as load refusal (:256-258); `succession` arrangement not seedable until a `determine` site opens a `hold` (:286-299), which touches the ruled-in succession noted in the brief (a deterministic heir order risk, to be checked by SC/FA lanes).

### engine/season/tests/test_ax7_refraction.py
- **What it is:** behaviour tests for AX-7 refraction (`decision/options.py::refracted_confidence`, `loop/witness.py::_refract`), v9 IN-15 and H-201; ED-IN-0244.
- **Status:** none; live.
- **Bears on:** FI, CHAR, CORE (knowledge model; R-02, R-07).
- **Content that matters:**
  - Formula in docstring: `confidence' = floor(confidence*(1-g*remove(channel))*(1-g*dissent)*competence + 1/2)`, `g = refraction_gain` (H-199, control 0, shipped 0.5), `competence` 1 (H-200 absent) (:7-14). Receiver-side only; emission never distorted (H-36).
  - Every test runs at the control gain 0 AND above it and counts `checked == 2`, so a test that cannot see refraction cannot pass (:16-19). Concrete numbers: told confidence 37 -> 31 for a knot hearer, event-kind claim 100 -> 83 (:101); dissent halves 37 -> 19 (:126); document-key hearer 100 -> 67 (:172); doubt of a transfer out of a known-empty granary 67 -> 33 (:239).
  - `channel_remove` is read off the roster: co_located 0, witness_key 1/3, document_key = chronicle 2/3, post_remit 1 (:86-88); the actor is never refracted (:163-186); observation claim is refracted under `observation_deposit_mode: total` only (shipped `actor` mode hands non-actors no read) (:189-209).
  - H-201: the act-level prior binds the ACTION'S actor, never the witness (:282-306); a refusal is not doubted by a belief the act could not happen (`_happened` clause) (:309-337). The `tell` prior is PLANTED: "in a run no ledger makes `tell`'s `requires` known-false", so that clause is guarded here and nowhere else (:315-319).
  - Every test records a MUTATION run date (2026-10-09), reverted; none of the mutations are in the suite as executable controls except through the gain-0 arm.
- **Conflicts / stale:** the realm-hash half is "a scratch reading recorded in the commit" (:17-19), so no test observes refraction in a played realm; consistent with F-TEST-01 (fixtures not the shipped world). Brief's R-07 (feeling/attitude: no test) is untouched by this file; only confidence is refracted.
- **Open items:** `competence` factor (H-200) absent, so two receivers of different competence hear alike; no content distortion (value never moves).

### engine/season/tests/test_cl_thrust_b01_arc_reader.py
- **What it is:** instrument test for `harness/arc.py`, the driver-side ARC reader and its two rosters `ARC_SELF`/`ARC_WORLD` (CL-THRUST B0.1, TL §1.2/§8, G-28).
- **Status:** none; live.
- **Bears on:** ARCS, CORE (narrative-arc instrument; R-01).
- **Content that matters:**
  - Six planted worlds: (i) linked self+world chain reads TRUE; (ii) no `causes` link FALSE; (iii) no writes FALSE; (iv) a witnessed `move` FALSE; (v) a witnessed `tell` FALSE; (vi) a `petition` answered by the conferrer's `confer` of the petitioner TRUE through clause (4) (:176-240). Each FALSE has a control with its missing piece restored or `unrestricted=True`.
  - Rosters must be `MATRIX` cells with a RESOLVE step, no WITNESS step, never `claim_ledger`, `Person.travel_leg`, `Person.exists`; `validate_roster` raises `ArcRosterRefused` per pair and `>= 20` entries asserted (:141-169).
  - Refusal null: a `petition.refused` Event in the log turns a TRUE arc FALSE; derived path and planted `refused=` set agree (:247-261). Deaths counted apart (`person.died` Event, and a `tenure.closed` seat Receipt on the office id are not world effects) (:277-297).
  - Nulls: shuffled-`causes` null reads below the linked log over 8 seeds, bookkeeping null reads HIGHER than restricted (STOP-IF) (:337-366). `test_dropping_the_exclusions...` monkeypatches `validate_roster` away and shows (iv),(v) turn TRUE (:322-334).
  - Realm run is PRINTED, not asserted; asserts only `u.count() >= r.count()` and no hash change (:388-404).
- **Conflicts / stale:** "no thrust authored" test relies on `SB.drive(0, 1, "off", None)` (storybar) as the realm. Arc reader reads Receipt writes, so an arc exists only where a RESOLVE-step matrix cell is written; arcs that turn on belief changes (WITNESS) are excluded by design (:148, :222).
- **Open items:** none stated.

### engine/season/tests/test_cl_thrust_b2_schema.py
- **What it is:** loader schema test, CL-THRUST B2.1/B2.2 (batch B10-05): closed `thrust_axes` roster, optional `axis:` on goals, top-level `goal_stages` list, via `data/goals.py`.
- **Status:** none; live (schema only).
- **Bears on:** CHAR, ARCS, WR (goal/ambition data surface, §14 authoring).
- **Content that matters:**
  - ~56 planted refusals, each ONE mutation of a valid base, each asserting loader refusal TYPE (`Unspecified` or `Forbidden`, never the builder's `SystemExit`) and a fragment of `.what`/`.where` naming the row; the base loads first as control (:215-385). `test_the_plants_ran_a_floor...` asserts `len(_PLANTS) >= 51` and `checked >= 56` (:361-373). COUNT-FLOOR pin, not exact.
  - M20 struck: stage `deadline`, row keys `closing`, `successor`, `deal` are refused keys AND absent from the carrier dataclass fields (:12, :424-433).
  - `thrust_axes` is a closed roster including opposite poles (`uphold_church`, `uphold_caste`, `altonian_ascendancy`, `reveal_thread_truth` are members though "not among the ten"); `opposes` map pairs only members (:175-212). An `axis` on an `orientation` goal is Forbidden.
  - Stage predicates must be ledger-answerable: world-only stems (`with`, `audience`, `thread_sensitivity` scalar) and LEDGER_DERIVED stems (`claim.held`, form `own_ledger`) are refused because no claim answers them person-side (:242-260, :354-355). This is the belief-not-truth rule at load time.
  - The shipped `goals.yaml` carries no `goal_stages` and no `axis` (:160-170): the whole stage machinery is schema-only, nothing authored.
- **Conflicts / stale:** `assert checked == len(raw["goals"]) >= 9` and "38 at the base reading" comment elsewhere are count notes. Pursuits named here (`honour`, `stability`) are read from the descriptor registry's PURSUITS.
- **Open items:** no ladder is authored in `goals.yaml`; which arcs need stages is unanswered here (ARCS lane).

### engine/season/tests/test_cl_thrust_b31_current_stage.py
- **What it is:** unit test for `world_q.current_stage(w, p, ambition)` (CL-THRUST B3.1, batch B10-05): the first stage of the ambition's `goal_stages` row not TRUE of each referent, evaluated person-side.
- **Status:** none; live.
- **Bears on:** CHAR, ARCS, FI (belief-not-truth), CORE.
- **Content that matters:**
  - Belief, not truth: person holding the stage-1 claim reads s2; one lacking it reads s1 although `WorldReader` says TRUE (:130-143). Planted failure run in-suite by monkeypatching `LedgerReader` to a world reader (:146-155).
  - UNKNOWN and FALSE both fail to pass a stage (:212-230); the first unmet stage is read, not the last met (:174-179); a passed referent is absent while its sibling is not; a vacant seat names nobody (:182-198). `actor := p.id`: a `held_by` cell is true only on the claim naming the person himself (:237-244).
  - Control (e): with no `goal_stages` row `current_stage` is `None` for every shipped goal and every ambition of `build_realm(0)` (`realm_checked >= 100 and authored >= 10`); and the control can observe the thing it excludes via a row planted on shipped `rung`/`person` goals (`planted >= 3`) (:265-316).
  - Computed when asked, stored nowhere: content hash and ledger unchanged by a call (:323-341).
- **Conflicts / stale:** comments cite counts ("38 at the base reading", "136 ambitions", "12 authored") that are no longer asserted exactly (floors only).
- **Open items:** none stated; nothing authored yet.

### engine/season/tests/test_cl_thrust_b32.py
- **What it is:** tests for `world_q.stage_referents`/`open_stages` and `attention_key` salience (CL-THRUST B3.2, R2, batch B10-09): a stage's referents are added to the question the person answers through the classed stamper; its pursuits join the salience target.
- **Status:** none; live. R3' (the pulse) NOT BUILT (:8).
- **Bears on:** CHAR, ARCS, CORE (decision input surface).
- **Content that matters:**
  - A stage referent rides the tier-1 own-seat claim question as `(p_a,"Person")` in `q.classes`, never the plain referents; no ladder, no stamp; stubbing `stage_referents` removes it (:121-145). Class test is the question's own (`_of_stamped_class`) (:172-177).
  - Stage `pursuits` raise the `need` question's salience only along an axis the person points at; a stage already passed weighs nothing (:191-205).
  - Equal at empty data: realm `questions_for` equal with shipped goals and with `goal_stages: []` (`committed >= 40`) (:212-224).
  - Realm run with one authored ladder on two shipped `seat_holders` goals: `stage>=1`, `formed>=1`, `hit>0` at seed 0, one season (:299-306); stub control falls (stage 89->51, hit 67->48 measured, comment :310-314); `news.told` against no ladder asserted within spread `<= 2` (:334). Hit matching is by (actor, subject), so a later season counts for an earlier deliberation, stated not corrected (:260-262).
  - The ladder goals are hard-coded ids `goal_crown_peninsular_sovereignty`, `goal_church_suppress_restoration` (:231).
- **Conflicts / stale:** `news.told` bound `<= 2` is a tolerance fit to a measured seed spread of 5 seeds, with a long comment recording a CR-87 revert. A hard-coded goal id will break if `goals.yaml` renames.
- **Open items:** R3' (pulse) unbuilt; no ladder authored in `goals.yaml`.

### engine/season/tests/test_combat_band_edges.py
- **What it is:** loader + seam test, `H-98` plan position 8: the wound-count band edge as data (`rosters.yaml: combat_band_edges`, `seam/ladder.py::combat_degree`, `combat_wounded_above` fixture), with CP-T03-00 amendments (both parties take their band; fight band is the worst).
- **Status:** none; live.
- **Bears on:** PC, CORE (seam), DICE (band ladder).
- **Content that matters:**
  - Shipped edges `Felled` and `Wounded` carry an edge (`wounds > 0`), `Untouched` is the residual; ten malformed-edge mutations each refuse at load (:87-143); the loader is exercised through the real YAML via the `rosters.ROSTERS_YAML` patch point, with a `refused == [...]` assertion that the loop looped (:97-117).
  - The old two-line literal is kept in the test as oracle and the shipped edges reproduce it over a 2x6x4x4 grid (`checked == 192`, `seen == set(COMBAT_BANDS)`) and over 12 real fights (`fought == 24`) (:153-190).
  - Edge-unreachable arm (`wounds > 4`) grades every standing fought subject `Untouched`; a Felled subject stays Felled (the engine's verdict is not swept); `WoundTracker.wounds` is capped at `max_wounds + 1`, so a standing subject at the cap still reads Wounded at the `max_wounds` arm (:195-268). `standing >= 1`, `felled >= 1` guard vacuity.
  - A driver fold at two arms writes at two bands (`body.changed` present at the shipped edge, absent at `max_wounds`) and `w.fixtures.reads` shows the fixture was read (:319-341).
  - The `engine_available` fixture does `pytest.skip` if `C.engine()` is None (:48-54): one of the F-TEST-11 engine-absent skips. The comment (:44-47) records that a module-level skipif made `test_importing_every_engine_module_pulls_in_no_subsystem` read a leak.
- **Conflicts / stale:** `_scene` caches fights "deterministic" (:79) = seeded replay, not a rule violation. Fights are `contest(...)` on `tiny_world` with act ids `we0..we23`, i.e. a swept act id is the RNG.
- **Open items:** none.

### engine/season/tests/test_combat_module.py
- **What it is:** module-entry test, plan position 31b (IN-04), A-25: `combat` module entry called on a hand-built `PersonalCombatInput` in a fresh subprocess.
- **Status:** none; live.
- **Bears on:** PC, CORE (module seam, "one path"), MB (duel path).
- **Content that matters:**
  - Entry found the way the host finds it: prize row `the body` -> `module_entry:` -> `composition.ROLES[role]["target"]`; nothing imports the module by name (:13-15, :61).
  - Asserts the files loaded in the fresh interpreter are only an allowlist (`engine/__init__`, `queries/inputs.py`, `substrate/pc_engine.py`, the module dir, `engine/dice_engine/`) (:64-72); this is A-25's "imports what it runs and the record type, nothing else of the host".
  - Three seeded fights; result equals the engine called directly (`wrapper.fight` on two `Combatant`s, the independent oracle), `wound_state` equals the trackers, `trace` non-empty, and same record+seed twice gives one result (:75-83). `entry(inp, rng, decide=lambda view: "engage")` (the playable branch, REM-31) must give the same result (:42, :44-45): evidence the duel branch and the automated branch are one path for an always-engage decider.
  - Asserts the three fights do not all read the same (`len({...}) > 1`) so the comparison can tell parties apart (:84-85).
- **Conflicts / stale:** `eval` of the probe's stdout. The "no module-level state" falsifier is only tested within one process.
- **Open items:** no approach/intensity (aggressive/normal/defensive) input appears in `PersonalCombatInput` here: only `claimants`, `ends`, `wound_quantities` plus a `decide` callback returning "engage". Relevant to the brief's PC intent (PC lane).

### engine/season/tests/test_content_operands.py
- **What it is:** test of plan position 15c content operands: `named(c)` (Q2 clause 3), `_from_content_claim`/`_derive_operand` reading a held writ, `record_sourced_operands`, `works_cost` checks.
- **Status:** none; live. Named in addendum C as a flagged-loop file (F-TEST-07).
- **Bears on:** SC (writs, petitions), FA, CHAR (candidate operand derivation), SE (`works_cost`).
- **Content that matters:**
  - `named()` reads the addressee id set through `record_kinds`'s addressee key, `()` for non-`content:` claim, a None value, or a kind without the key (:64-83). A `content:dispensation` claim naming a person is ASKED (Q2 clause 3) even where he holds nothing and is nowhere near; a control with the same claim held by a non-named person is not asked (:90-109).
  - `to` resolves off a held writ ahead of the referent copy; `kind`/`amount` decline (no live schema carries them) and fall to `default_store_kind`/`default_transfer_amount`; `from` is never read off the writ (r2 ruling) and stays the actor's own containing rung `Hh`; `at` is not an operand (:137-215).
  - Singleton rule: exactly one addressee collapses to that id, two or zero decline (":naming which of several a scalar operand means is a choice nobody has ruled") (:222-236). This is an unresolved design choice, no draw.
  - COUNT PINS: `len(REQUIRES_OPERANDS) == 10` (re-recorded 8 -> 10 at REM-2B, restoring IN-33) (:206); `set(QUESTION_SOURCES) == {"claim_landed","need"}` (:301).
  - Realm loop (:243-290): after one realm season at seed 0 every person's `opening_set` is walked; asserts `len(writ_derived) > 0` and no `to` is a tuple; the second test (:278-290) has NO count: it loops asserting `not isinstance(.., tuple)` over whatever candidates exist (F-TEST-07; addendum measured 245,574 candidates, 194,714 with `to`, so not vacuous today).
  - Per-kind `record_sourced_operands` and `works_cost` load checks each refuse a planted mismatch, with the shipped table as control (:309-387).
- **Conflicts / stale:** comments cite 173 tuple-`to` Candidates found in a populated corpus run (a past defect, no longer asserted as a number).
- **Open items:** the singleton rule leaves multi-addressee writs unreadable (a decision "nobody has ruled", :222-236).

### engine/season/tests/test_cp_t01_05_npc_effort.py
- **What it is:** chooser-level test of CP-T01-05, NPC half (B10-10, `H-249`): the computed chooser forms an `effort` variant on an act (`decision/choose.py::settle_efforts`), priced by the acts it displaces.
- **Status:** none; live.
- **Bears on:** CHAR (chooser), SC (`argue` effort), DICE (believed chance), CORE (Scene.cost).
- **Content that matters:**
  - Where the believed chance RISES with effort (0.1/0.5/0.9) the chooser puts effort 2 on the act; where it is FLAT it never does; a None chance or a View with no query forms none; an uncontested verb forms no variant and the query is never asked (:112-141).
  - Price: with two rivals scored 0.5W the base stays, scored 0.05W effort is formed (net-gain arithmetic in comments :150-158); `per=1` forms none, `per=2` caps at effort 1 (an effort-2 act needs 3 slots) (:174-179).
  - No scene is overspent through `Scene.cost`, budgets 1..6 (`formed >= 1` guard); planted failure (d) monkeypatches `Scene.cost` back to the one-slot price and shows it overspends (:195-225).
  - `npc_effort: off` forms nothing and `settle_efforts` returns its arguments untouched (identity compare); an arm off the roster `npc_efforts` raises `Unspecified` (:161-171).
  - Admits NO realm-level pin of the `off` arm: `test_go07` pins the shipped arm and `on`/`off` read the same hash at every measured horizon (:16-18), so `off` is only tested at the chooser level.
  - On a real `tiny_world`, `sigma.believed_chance` rises strictly with the payload `effort`, with a planted `capability` claim (`VERB_CAPABILITY["argue"]`, score 4) (:241-258).
- **Conflicts / stale:** `_person()` sets pursuits to `{n: 1.0 for n in PURSUITS}` ("roster-exempt"); the `cells` fixture plants an `argue` alignment cell on `V.ALIGNMENT` because `argue` carries none in the shipped table (:58-63) - a CHAR/SC finding: the shipped chooser has no alignment for `argue`.
- **Open items:** none.

### engine/season/tests/test_cp_t02_01_death_names_seats.py
- **What it is:** behaviour test, CP-T02-01 (H-230 limit 1, with HR-1): a death names the seats it empties via a `tenure.closed` Event whose receipts are under the OFFICE id; also the `total`-arm march emits `field.won/lost`, `army.arrived` beside `person.died`.
- **Status:** none; live.
- **Bears on:** FA (seats, succession information), PC (kill), MB (march/field casualty `total`), WR (witness/chronicle), CORE.
- **Content that matters:**
  - A `Felled` seat-holder yields `["person.died","tenure.closed"]`, receipts naming `off_duke`, and after WITNESS EVERY living person holds a claim about the office; `world_q.seats_named` returns it for a far person (:99-105). The dead holder's `hold` leaves with him (`World.tenures` iterates `persons`) so WITNESS could not otherwise expand it (:5-9).
  - Mutation in-suite: `World.seat_holds` -> `[]` removes the emission and the positive half goes red (:107-120). MATTER `_die` of `p_npc_020` (holds `off_duke_valorsmark` AND `off_king`) emits ONE `tenure.closed` with both receipts, `causes` equal to the death's (:123-145). Death emptying no seat earns none, on tiny_world and on the realm (loop `break`s at first find, `checked == 1`) (:148-181).
  - HR-1: total-arm `Won` emits `["field.won","army.arrived","person.died","tenure.closed"]`; mutation `own_kinds -> ()` silences `field.won` (:214-235); `Lost` removes every attacker and names each once (:238-259); control: shipped `scaled_by_degree` arm kills nobody (:262-277).
  - Fixtures use hard ids from the built realm (`p_npc_020`, `p_npc_008`, `set_s_036`, `set_s_014`, `p_npc_033`, `p_npc_037`, `b_s_002_cottage`, `off_spymaster`). `Won` "unreachable at fixture scale", so the result is constructed.
- **Conflicts / stale:** mixed: `Resolution("Felled", ...)` is hand-constructed (no dice). Nothing here observes a probability: kills are constructed outcomes. Note the death consequence (who learns which seat is empty) is deterministic by design (information flow), fine.
- **Open items:** none; succession (who fills the seat) is not in this file.

### engine/season/tests/test_cp_t02_02_seat_ids.py
- **What it is:** builder test, CP-T02-02 (H-230 limit 2): a loop-built seat keeps its authored `offices.yaml` id (`harness/populated.py::_seat_id`).
- **Status:** none; live.
- **Bears on:** FA, CORE (realm build), CHAR.
- **Content that matters:**
  - In `build_realm(0)` every `OFFICES_SEATS` row id is an Office under its own id, census `authored` is the identity map, the unauthored seat (guild leader NPC-084) keeps an `off_npc_*` slug (:55-67).
  - OLD side is built by monkeypatching `_seat_id` back to the slug rule (not a stored copy); `goal_referents` for `goal_crown_peninsular_sovereignty` names the same holders under old and new ids; the multiset of (post, rung, holders) is identical; ids differ (control) (:70-92). Mutation: slug rule leaves row ids unbuilt (:95-98).
- **Conflicts / stale:** hard-coded goal id `goal_crown_peninsular_sovereignty`.
- **Open items:** none.

### engine/season/tests/test_cp_t02_03_aim_state.py
- **What it is:** unit test, CP-T02-03 (B10-09; v10 AM-B-09): `world_q.aim_state(w,p,prop) -> open|met`, rung goals only; Q4 forms no `need` for a `met` goal.
- **Status:** none; live.
- **Bears on:** CHAR, FA (ambition), WR.
- **Content that matters:**
  - A `rung` goal whose rung a member of the org's faction holds forms no `need`; same world with the hold ended or held by another faction's member forms it (:70-81). A holder committed to two factions reads `faction_holding` None: not met, "not guessed" (:94-100).
  - Only `rung` has an `aim:` row in `goal_object_kinds` (:158-159); a kind with no row (e.g. `seat_holders`) is never `met` even if the org's member holds the seat (:105-112). So "ambition met" is defined for one goal kind of five.
  - Loader refuses: `aim:` column dropped, an `aim` row for a nonexistent kind, a rule name with no `AIM_RULES` implementation (at load via `check_aim_rules` and when asked) (:117-153).
  - Mutation in-suite: `aim_state` always `open` reddens the met-world assertion (:84-91).
- **Conflicts / stale:** none.
- **Open items:** `aim` only for `rung` (the Must-not of the item) - other goal kinds never read as met, so a seat-holder ambition keeps forming `need` after it is fulfilled (CHAR/ARCS lead).

### engine/season/tests/test_cp_t02_06_continuations.py
- **What it is:** test of v10 CP-T02-06 (B10-10; M7 taken (b)): the seated person's line continues or ends; `rosters.yaml: continuation_ties [heir_title, sworn]`, `world_q.continuations`, `harness/play_surface.py::carry_on`. Player half only (R-WORLD is IN-61's).
- **Status:** none; live. HASH PIN: `PRE_BUILD` three literals, seeds 0/1/2.
- **Bears on:** CORE (play surface), FA (succession), CHAR (player re-bind), GO.
- **Content that matters:**
  - Query order is fixed by the roster `continuation_ties`, not by the reader table `_TIE_READERS` (monkeypatch swaps both and the read follows the roster) (:118-144); a person both heir and sworn is read once at the earlier tie (:147-151); dead persons' edges leave the view; an `imposed` oblige (a sentence, `Tenure.imposed`/`DETERMINED_BY`) is not a sworn continuation (:251-261).
  - `carry_on`: when the seated person dies it OFFERS the living members of his last reading, in roster order, and binds the callback to the PLAYER'S choice; none alive = extinct (callback dropped); a choice outside the offer is refused with no half-applied change; the next season's DELIBERATE calls the callback for the heir (:188-281).
  - Seat succession here is a PLAYER choice among ties; "R-WORLD" (the world's own succession when no player) is not built by this item (:3 docstring). Relevant to the ruled-in `succession` and the no-deterministic rule: the heir offer is a list, not a rule.
  - Pins `PRE_BUILD = {0:"256606154c30542f9456b2fe15c76f09", 1:"aa58ef0b71c947ce5ff9f0a75ffd8ca6", 2:"a21ab6e12e356ccc4261bec1c93ca3b4"}` (:72-74) compared with `w.content_hash()` after one season, behind `revert_cr79` (imported from `test_strife_credit`) (:286-308). The comment log (:36-71) records 9 re-pins, each naming a revert as control (CP-T03-09, PC-10b, CR-87, CP-T03-02, CR-85, CP-T03-04, CP-T03-07, CP-T03-08, B10-13 batch); one assertion at seed-0 `25660615...` is the same literal addendum C says sits in six files (F-TEST-02).
- **Conflicts / stale:** this pin is "the pre-build" hash, i.e. a reverted-CR-79 world, not the shipped one (F-TEST-02 pattern; with one revert only). Seed 2's log notes NPC-004 leaves the world by season 1 at seeds 0/1.
- **Open items:** none.

### engine/season/tests/test_cp_t03_00_both_parties_take_their_band.py
- **What it is:** behaviour test, CP-T03-00 (REPAIR per `-08` AM-C-01): both parties of a fight take their own band; `combat_degree` is the WORST over `wound_state`; `_eff_kill` writes actor and subject each by his own band; each emitted kind's Event carries only the changes of its earners.
- **Status:** none; live.
- **Bears on:** PC, WR (witness/deposits), CHAR (deed_doer pairing, IN-58), FA (confer per-kind carriage).
- **Content that matters:**
  - 3x3 grid of (actor band, subject band): `party_degree` per party, `combat_degree` the worst (`checked == 9`) (:82-94). Felled actor + Wounded subject emits both `person.died` (actor) and `body.changed` (subject), no ledger holds the living subject as dead (:97-110).
  - IN-58 pairing limit: `person_q.deed_doer` names no killer for an attacker felled by his target; a wounded subject pairs to his wounder; `paired >= 1`, `limited >= 1` guard vacuity (:113-136). `contest.undecided` emitted iff both Untouched (3x3, `checked == 9`) (:162-174).
  - WITNESS runs under `fan_out_mode = total` so a deposit assertion cannot pass by nobody seeing the fight; at the shipped `all_five` a felled actor stands nowhere and the Event is placed via `event_place`/`departed_from` so the co-located subject still holds it (B10-09 D2) (:46-54, :186-199).
  - Per-kind carriage beyond fights: `confer` onto a held seat emits `tenure.opened` with only the new hold and `tenure.closed` only the closed (:202-220); a total-arm `march` `Won` splits receipts per kind (:223-235); shipped arm control publishes one receipt list on both kinds (:238-252).
  - Bands are CONSTRUCTED `Resolution`s via `degree_of`; no dice. Imports `_march`, `_won_total`, `CHURCH`, `CROWN` from `test_cp_t02_01...`.
- **Conflicts / stale:** the "mutation run by hand at the build" (:14-17) is not in the suite (unlike sibling files); the falsifier here is observational only.
- **Open items:** none.

### engine/season/tests/test_cp_t03_01_cohorts_never_fight.py
- **What it is:** behaviour + hash-control test, CP-T03-01: a cohort (`Person.is_cohort`, `weight > 1`) is never a party to a personal fight; `individual` stem (WORLD-ONLY) conjunct on BOTH parties of `fight` and `accept`, refusal kinds `kill.refused` / `accept.refused`.
- **Status:** none; live. HASH PIN: `BASE` three literals (seeds 0/1/2), behind SIX reverts.
- **Bears on:** PC, MB (cohorts as weight>1 units), CORE.
- **Content that matters:**
  - A hand-built `fight`/`accept` on a cohort through `dispatching_chooser` is refused with the row's kind and leaves weight/body/tenures equal to a control season in which nobody chose; actor-side the same; a weight-1 person is admitted (:113-147). `fired` asserts the hand-built act was asked for.
  - `individual` is in `REQUIRES_STEMS` and `WORLD_ONLY_STEMS` but NOT `CELL_STEMS` (a cell stem would be deposited into every witness's ledger); `WorldReader.read` returns `not p.is_cohort`, `UNKNOWN` for an unknown person (:150-163).
  - Realm control: `build_realm(seed)` 2 seasons, with `capture`, `challenge`, `accept` WITHHELD from the chooser (`WITHHELD`), with the `individual` reads stripped from `Event.observed`, equals `BASE[seed]` at seeds 0 and 1 (`reads > 0`, `refused_on_it == 0`); at seed 2 `refused_on_it > 0` and `h != BASE[2]` (:220-260). `BASE = {0: bb5089bc..., 1: a3bd409c..., 2: d1594dae...}` (:181-183); seed 2's value "left at its stale value" and read only as inequality (:178).
  - The hash is only reproduced with SEVEN in-process reverts: `revert_cr79, revert_cr87, revert_cp_t03_02, revert_cr85, revert_cp_t03_04, revert_cp_t03_07, revert_cp_t03_08` (:233-240). This is the "up to seven deep" stack of F-TEST-02. Mutation of the shipped chooser: the test deliberately removes `capture/challenge/accept` verbs, so the shipped duel verbs are untested in that realm.
  - Comment (:19-23): with CR-87 live "no `fight` formed in these realms" so the conjunct would never be read; the control only observes anything with `revert_cr87`. i.e. at the shipped configuration violence is not chosen in two seasons at seeds 0/1.
- **Conflicts / stale:** F-TEST-02 confirmed here: pins a world nobody plays (7 reverts); `BASE[2]` stale by its own comment.
- **Open items:** none.

### engine/season/tests/test_cp_t03_02_band_ending_and_body.py
- **What it is:** behaviour + hash-control test, CP-T03-02: a fight band's success Event carries `Event.ending` `(pid, felled|yielded|undecided)` per party and each wounded party's `body.changed` carries the Observation `(pid,"body",v)`. Marked `[ASSUMPTION; medium; Jordan to correct]` (:8).
- **Status:** none; live. HASH PIN: `PRE_ITEM` three literals. Defines `revert_cp_t03_02` (:195-198), imported by five other files.
- **Bears on:** PC, FI/CHAR (what a witness knows of a body), WR, CORE.
- **Content that matters:**
  - Falsifier: after a Wounded band the actor (the shipped `observation_deposit_mode: actor` observer) holds `(subject,"body",written v)` and a non-witness holds none; the mutation (Observation built before the write) is executed in-suite and reddens (:93-122). `_falsifier_holds` asserts the setup is non-vacuous (the subject was bled; someone did not witness).
  - STATED LIMIT: under `actor` mode only the act's actor holds the body value; bystanders hold `body.changed` but not the value (:12-15, :125-134). So a bystander cannot tell how hurt a man is (relevant to FI/epistemics and to tend-on-the-wounded, CP-T03-08).
  - `ending` per party across four (actor band, subject band, yielder) cases, `checked >= 4`; untouched fight carries no ending/body; felled party carries no body Observation; a `capture` at Untouched stamps `((actor,"undecided"),(captive,"yielded"))` on `person.captured` (:137-180).
  - Hash control: item reverted in process equals `PRE_ITEM[seed]` (`a63b9600..., 938a3aff..., d5d356c7...`) after 1 season, with FIVE other reverts first; with the item live, seeds 1 and 2 move and seed 0 does not (`(moved != PRE_ITEM) == (seed != 0)`) (:183-223). Seed 0 "forms no Felled/Wounded fight".
- **Conflicts / stale:** revert stack depth 5 (+`revert_cr79`) - F-TEST-02. The `PRE_ITEM` literals are the hash of the tree "as it stood several items ago".
- **Open items:** the `[ASSUMPTION ... Jordan to correct]` on the body observation is not resolved here.

### engine/season/tests/test_cp_t03_03_kit.py
- **What it is:** behaviour + loader test, CP-T03-03 (`-08` AM-C-04): kit `(weapon, armor)` reaches the fight; `world_q.kit_of`, `combat_input` fills `PersonalCombatInput.kits`, `rosters.yaml: arms_kinds` validated at load against `engine_params/combat_engine_v1.json` `kit` section (read by `engine/substrate/combat_kit.py`).
- **Status:** none; live. The shipped rosters are EMPTY (":the inventory is Jordan's content").
- **Bears on:** PC, MB (weapon-carry trade-off), CHAR (§14 equipment as capability data), SE (stores as inventory).
- **Content that matters:**
  - `kit_of` = per Combatant field, the highest-RANKED arms kind with positive count in the stores of rungs he `hold`s, else of his `reside` rung, else the engine default; fallback is PER FIELD (holder's armour from an arsenal, weapon from the hearth) (:155-196). A planted mutation (per-person fallback) loses the residence weapon (:199-209). `kit_of` writes nothing; a kit is read, never consumed (:212-217): so there is no wear, loss or carry cost for kit.
  - Armour key list is the engine's own: `combat_kit.WEAPONS`, `ARMOUR_TIERS == {none, light, medium, heavy}`, `DEFAULTS` equal the `Combatant`'s default; `export_engine_params.py --check` is run and a drifted `kit` section fails it (:86-111). Loader refuses 8 malformed `arms_kind` rows, an unregistered matter kind, tied ranks within a field, and bad `arms_at_build` seeds (:114-148).
  - Falsifier through the real seam: n=400 fights, SUBJECT stocked with top armour fells the actor at HOME_RATE 0.975 within TOL 0.04 (justified as 4 sigma); the unarmed control is `< 0.6`; mutation (actor's kit for both) fails the same predicate (:224-292). The tolerance is a derived binomial band, not an exactness `approx`. Note a plated subject vs. a default actor is a 97.5% outcome: near-deterministic from state, relevant to the standing no-deterministic rule (F-PC-04 is the plain-fight case).
  - `fight_estimate` builds the same input so kits reach the display; a record with `kits=()` fights at the default (:264-282). `ARMS_KINDS == {}` and `ARMS_AT_BUILD == {}` asserted for the shipped rosters; every one of >50 persons in the realm reads the default kit (:299-307); seeding with `{settlement: {t_plate: 2}}` moves the hash (:310-320).
  - Kit has no fatigue/speed cost anywhere in this file; it has no unit/mass-battle reach: the only consumer is `combat_input` for personal fights.
- **Conflicts / stale:** brief's MB weapon-carry trade-off (fatigue and speed cost of carrying more weapons) has no counterpart here: kit is a single weapon+armour pair, no secondary weapon, no loadout cost. Empty shipped rosters mean no person ever has a non-default kit in a played game.
- **Open items:** inventory content is Jordan's (`-08` AM-C-04); no secondary-weapon field in `combat_kit.FIELDS`.

### engine/season/tests/test_cp_t03_04_arms.py
- **What it is:** behaviour + hash-control test, v11 CP-T03-04: the `arms` vocation (trained skill, NOT equipment): `verb_capability` maps `fight/accept/capture` to `arms`; reaches combat's pool/Ob through `sigma.faculty` (CR-85's one path, `PersonalCombatInput.faculties`); `train` raises it; fights that draw blood raise it by one on each surviving holder (`effects_combat._grown`). `[ASSUMPTION; low; Jordan to correct]`.
- **Status:** none; live. HASH PINS: `PRE_ITEM` and `POST_ITEM` (six literals, 3 seeds). Defines `revert_cp_t03_04` (:69-77), imported by five other files.
- **Bears on:** PC, CHAR (§14 capability authoring: `arms` is the one skill wired to combat), CORE.
- **Content that matters:**
  - Falsifier: `arms` 5 vs a default party rolls pool 11 against Ob 1.0, the opponent pool 8 against Ob 2.5 (a spy on `core.resolve` sees exactly `{(11,1.0),(8,2.5)}`) (:127-143); with nobody holding it every season roll reads `(8, 1.0)` (:146-151); item off, the same holder rolls the fallback `(2,2)` (:154-159). Faculty -> pool and Ob are therefore set from one integer (`faculties`) in `combat_input`.
  - NOBODY holds `arms` at landing: 0 of >= 240 persons over 3 seeds, no overlay value, no lifepath names it (:97-111); `DEGREE_STEP` for the fight bands is 0 so no practice record can form. So the skill exists in code but no character in the shipped game has it; it can only appear via `train`.
  - `train` raises a held key by one and refuses a non-holder (`train.refused`); a surviving holder of a bloodied fight gains one, a non-holder gains none ("never-mint" check, mutation in-suite); a felled holder does not grow; an untouched fight grows nobody; `capture` and `accept` grow by the same rule (:164-279). `src` check: `'"arms"'` appears in no body in `effects_combat.py` (:93-94).
  - HASH: formation mover even at control (adds one `train` Candidate per formation) so the pre-item hash cannot be reproduced with the item in; `revert_cp_t03_04` plus THREE other reverts (`revert_cr79`, `revert_cp_t03_07`, `revert_cp_t03_08`) read `PRE_ITEM`, and the live arms read `POST_ITEM`, per seed (:284-301). `build_realm(0).content_hash()` is 7266f56b... before and after (comment :52).
  - `test_season_every_person_holding_arms_2` plants `arms: 2` on every person and shows some survivor reaches 3 after a season; growth is attributed to a body verb by `causing_act` (`>= 1`, measured one by `capture`) (:304-319).
- **Conflicts / stale:** F-TEST-02: pins a stack (item + 3 reverts) rather than the shipped realm. The `_engine` fixture skips if `C.engine()` is None (F-TEST-11).
- **Open items:** `arms` has no authored value; CHAR lane's capability authoring surface (verb -> vocation -> attribute `attr.body.agility`, `VOCATION_ATTRIBUTE`) is read from rosters here (:91).

### engine/season/tests/test_cp_t03_05_fight_estimate.py
- **What it is:** statistical behaviour test, CP-T03-05 (`-08` AM-C-02): `combat.fight_estimate` samples the combat module `estimate_samples` times on a private rng for the player's display; `sigma.odds_of` mode (a) returns the shares for a row contesting `the body`.
- **Status:** none; live. Display only ("no loop calls it").
- **Bears on:** PC, GO (odds display), CHAR (chooser view), DICE.
- **Content that matters:**
  - Four endings shares (`actor_felled, subject_felled, yielded, undecided`) sum to 1 (`math.isclose` at 1e-12 on float sums, a legitimate use), asking twice in a tick shows one figure (:104-115).
  - Displayed shares equal REALISED shares over 3000 held-out scenes per matchup across 6 held-out world seeds, within Z=4 standard errors of the difference of two binomials; `MAX_TOLERANCE = 0.11` guards that a loosened Z/sample cannot let a wrong display pass (:118-131). Control: an even fight's display is OUTSIDE tolerance against a lopsided one's realised shares (:136-146). Realised side classifies scenes by trackers' `felled` flags and `surrender`, not the result sign (:72-93).
  - Exact (no-noise) control: replaying the sampler's own key `H(seed, tick, actor, "estimate")` gives shares equal to the trackers' tally exactly, and the result's sign disagrees with the trackers on at least one scene (`wrapper.fight` flips the sign in `UPSET_FLOOR` of decided fights) (:158-193). So the fight's `result` sign and the tracker outcome can disagree: an upset floor exists in the engine.
  - `yielded` is 0 on both sides by construction (no yield term yet) so those comparisons cannot fail (:132-133 comment). The estimate consumes no season draw and writes nothing (draw counter and `content_hash` unmoved) (:213-221). `odds_of` mode (b), `believed_chance` for a fight, is `None`: a believer has no figure for a fight (:200-210). `estimate_samples` bad values (0, -3, 2.5, "400", None, True) refuse with `Forbidden` (:224-239). Party gap -> `PARTY-GAP` refusal (:242-249).
- **Conflicts / stale:** `fight_estimate` is read-only and the chooser's belief for a fight is None, so an NPC chooser cannot weigh a fight by odds (CHAR/PC lead: NPC fight choice has no believed chance).
- **Open items:** `yielded` share untested until CP-T03-09 gave a yield term (that file is below).

### engine/season/tests/test_cp_t03_07_body_ceiling.py
- **What it is:** behaviour + source-walk + hash-control test, v11 CP-T03-07 (P32): `Person.body_ceiling`, the lasting mark a fight leaves on a survivor at the deepest gate (`wounds >= max_wounds`): ceiling falls 1000 -> 799 -> 499 -> 99 (one below the next `band_floors["body"]` floor); `_eff_tend` heals toward the ceiling; `body_mark_model in {none, deepest_gate}`, shipped `deepest_gate` `[ASSUMPTION; medium]`.
- **Status:** none; live. HASH PINS: `PRE_ITEM`, `POST_ITEM`, `CONTROL` (nine literals) plus `BUILD_PRE`/`BUILD_POST` (`7266f56b...` -> `600d8b27...`).
- **Bears on:** PC, CHAR (injury as lasting state), SE (subsistence fall), CORE (schema mover).
- **Content that matters:**
  - Falsifier: a survivor at the deepest gate holds 799 (ceiling), `tend` at body 250 restores him to 799 where an unmarked man gets 1000; `body_band_penalty` sits one below whole (:126-137, :211-212). Mutation in-suite: a `tend` that heals to `condition_scale` goes red; a pre-clamp Observation reports 900 where 799 was written (:153-162, :215-227). The mark is NOT a draw: a survivor at `wounds >= max_wounds` is marked with certainty (a deterministic injury consequence, brief's no-deterministic rule: PC lane).
  - Asymmetry guard (modelled on `test_morale_write_sweep.py`): a regex scan of every bare `body` write under `engine/season/` outside `tests/`+`harness/`; each must be registered in `_BODY_WRITES` as `lowers` or `raises`; a raiser's enclosing function must read `body_ceiling` and not `"condition_scale"` (AST) (:241-318). Has a population floor (`raisers >= 1`, `len(found) >= len(_BODY_WRITES)`) AND "the guard itself can fail" tests with planted sources (:321-351). This is a source-text scan of the code, in the F-TEST kept class (observes what it claims). `assert sorted(set(found)) == sorted(_BODY_WRITES)` means deleting a write forces editing this test.
  - Hash: in-suite `revert_cp_t03_07` (drops the field from `state/world.py::_OBJECT_HEADS` canonical encoding and sets `body_mark_model: none`) reproduces `PRE_ITEM` (:72-80, :356-378); `marked == {0:0, 1:0, 2:1}[seed]` persons carry a mark after one season, i.e. exactly one person in the three realm seasons (:370). Control `none` hash (seed 2 differs from POST). Stack: `revert_cp_t03_08` + `revert_cr79` first. `build_realm(0).content_hash() == "600d8b27..."` is the literal addendum C says sits in six files (:381-384).
  - The field has three writers (`fight`, `accept`, `capture`) via the MATRIX row `("Person","body_ceiling")` (:106-113).
- **Conflicts / stale:** `CP-T10-04` (`tend_share`) "unbuilt"; `_eff_tend` restores the WHOLE headroom with no draw (:12-14).
- **Open items:** `tend_share`; `[ASSUMPTION ... revert: none]` on the shipped `deepest_gate`.

### engine/season/tests/test_cp_t03_08_tend_on_the_wounded.py
- **What it is:** behaviour + hash-control test, v11 CP-T03-08: `tend` forms on the wounded; `world_q.wounded_with` (appended to `questions_for`'s stamp splice) stamps the asker himself below his own `body_ceiling`, plus each living person `with` him whom HIS LEDGER's newest `(person,"body",v)` claim puts below `condition_scale`; `tend` declares `referent_class: Person`. `[ASSUMPTION; medium]`.
- **Status:** none; live. HASH PINS: `POST_ITEM = {0:"256606154c30542f9456b2fe15c76f09", 1:"aa58ef0b...", 2:"a21ab6e1..."}`, `BUILD = "600d8b27..."`; `PRE_ITEM` is imported from `test_cp_t03_07`'s `POST_ITEM`.
- **Bears on:** PC, CHAR, FI/WR (belief of a wound), SE (REM-52 hunger fall).
- **Content that matters:**
  - Lawful-input rule: the stamper reads no other person's TRUE body; `_lawful_input_violations` moves true bodies and beliefs independently across four setups (an unwitnessed wound is not stamped for a stranger; a believed wound beside him is; his NEWEST belief outranks a stale one and the true body; a believed wound elsewhere is not); mutation (a stamper reading true bodies) goes red (:105-149).
  - Case 5: a DETAINED man below his ceiling is stamped for himself, `tend` forms on him, the real fold raises him 450 -> 799 (`body.tended`) (:81-93). A believed wound forms `tend` on the other and the real fold heals him to `scale` (:152-161).
  - Realm reading PINNED (seed 0, one season): REM-52's hunger lowers every short cohort's body in MATTER, `wounded_with` stamps each, `_eff_tend` restores the whole headroom: `(len(short), len(tended)) == (37, 37)` and every short person ends at his ceiling (:180-192). The test's own docstring labels it a finding about `_eff_tend`'s whole-headroom magnitude "not a claim that it is right"; a COUNT PIN of a trajectory (37).
  - Hash: item on equals `POST_ITEM`, `revert_cp_t03_08` reproduces `PRE_ITEM`, after `revert_cr79` (:166-177).
- **Conflicts / stale:** the pin `256606154c...` is the same literal as `test_cp_t02_06::PRE_BUILD[0]` (F-TEST-02: one trajectory in six files). Healing is a deterministic full restore (no draw), against the brief's no-deterministic rule (PC/SE lanes).
- **Open items:** `tend_share` (CP-T10-04) unbuilt.

### engine/season/tests/test_cp_t03_09_capture.py
- **What it is:** behaviour test, CP-T03-09 (`-08` AM-C-03): `capture` takes a beaten man into a seat's custody (a named fold of `fight`): `duel_terms: capture -> yield` is written into `PersonalCombatInput.terms` (default the STRING `'death'`), `_eff_capture` is `fight`'s wounds plus one `detain` edge captive -> the act's `via` seat.
- **Status:** none; live.
- **Bears on:** PC, FA (detain, custody, seats granting `dispatch`/`determine`), SC.
- **Content that matters:**
  - Row: eligibility `remit:dispatch` (same as `arrest`), contests `the body`, `fight`'s typed cell (stems `exists, with, individual`), `emits_on_refusal = capture.refused`; `_OPENERS_FROM_EFFECTS["detain"]` holds `arrest` and `capture` and NOT `fight`/`accept` (:115-133). `DUEL_TERMS_BY_VERB == {"capture": "yield", "accept": "blood"}` ("v11 CR-87 added accept: blood"), checked against the engine's `wrapper.DUEL_TERMS` tuple, not redeclared (:136-152); a `None` default for `terms` raises `ValueError` in the engine (control) (:159-170).
  - Falsifier scans up to 80 act ids (`TRIES`) for a scene where the captive yields: the draw decides whether a capture succeeds, and the test raises if none found (:91-99). Shared predicate `_assert_held` (captive stands, exactly one live `detain` to the actor's `via` seat, `person.captured`, no `person.died`) passes on the shipped effect and FAILS on a mutant routing the yield to `remove_person` (:198-235). A captive's `move` is declined (`travel.blocked`) (:204-206).
  - Eligibility edges: `dispatch` without `determine` opens nothing (captive fought and wounded, `fought >= 1`); no `dispatch` is refused before any fight; a seat whose purview misses the captive's settlement opens nothing; across settlements refused at the cell; a cohort is never captured; yield by the actor opens nothing; a felled party opens nothing; a second capture of a man already in custody opens no second edge (:238-355).
  - Pinned-scene section ("no dice") folds hand-built `Resolution`s with `R._fold` (:298-355); total-arm `wound_harm_model: total` removes the Wounded party, so the effect leaves the base alone (`removed >= 1`) (:362-376).
  - `fight_estimate` for `capture` shows `yielded > 0`, for `fight` `yielded == 0.0`; one `combat_input`, no second `terms` path (:180-191).
- **Conflicts / stale:** `capture` is "fight's typed cell" and a nameable seat-gated verb, yet in two realm seasons violence/`capture` formation depends on CR-87 contexts (see cp_t03_01). Whether a yielded fight resolves by a draw (yes, via `random.Random` in the engine) vs the capture outcome being a fixed function of the surrender record: the draw is the surrender in the engine, so ok.
- **Open items:** none.

### engine/season/tests/test_cp_t04_01_person_subunits.py
- **What it is:** behaviour test, CP-T04-01 (`H-359`): `field_subunits: person` builds one subunit per commanding person and `_eff_march` scales each loser's body by HIS subunit's survivor ratio; `side` (shipped) is the field as it was.
- **Status:** none; live.
- **Bears on:** MB (subunit hierarchy, person-level casualties), CHAR (commanding persons), WR, CORE.
- **Content that matters:**
  - The field is HAND-BUILT: "One season of the shipped realm fights almost no field (seed 0: `field.unopposed` 3, `march.declared` 6; seed 1: unopposed 2, declared 3; seed 2: `field.lost` 1)" (:5-8) - so the natural game exercises the field resolver almost never. Fixture knobs `SEED=8, WEIGHT=1, FIELD_SCALE=200` (weight -> troops 200; `field_troops_per_weight` is REM-32, "a value of THIS TEST, not Jordan's answer to JQ-4"); preconditions asserted; re-picked by MB-07r (depth support cap, `POOL_QUALITY_SCALE` 0.5 -> 0.8).
  - Under `person` two losers end with different bodies (the routed marcher cut, the other untouched); under `side` both take the side ratio; planted failure (side ratio fed to every person) reddens the same check (:64-98). Control: `side` equals the unswept fold, same hash, record holds no `subunits`/`broke_first` (:101-115). `field.lost` carries `(pid,"broke",True)` for exactly one loser (:118-124).
  - Unit shape: `_person_unit` builds one subunit per member sized by his own weight x scale (`[100,300,200]`), total equals the side's, provisioned troops spread by weight (`fed=2.0` -> `[50,150]`); subunit logs its person in the ORDER it breaks, not on a whole-unit sweep (:127-149). Unknown arm raises `ValueError` (:152-156).
  - The module is reached by `importlib.import_module("modules.mass_battle.massbattle")` by string (:21, :36-38): the test keeps `engine/` from naming `modules/` imports.
- **Conflicts / stale:** weight and `field_troops_per_weight` are the only link between persons and troop counts: a character's quality (skills, kit) does not enter the headcount line (MB lead for the brief's Ogre Battle/Bannerlord intent).
- **Open items:** JQ-4 (the weight -> troops scale) is Jordan's, unanswered.

### engine/season/tests/test_cp_t04_02_marshal.py
- **What it is:** behaviour + export test, CP-T04-02 (B10-12; AM-C-09 REPAIR): `marshal`, the standing order of battle. A seat granting `dispatch` mints an `order_of_battle` Record `[at, role, retreat_at]`; `field_input` reads per side the newest by holder edge (`world_q.standing_order`); `resolve_field` maps `role` onto each subunit of a headcount line.
- **Status:** none; live. `[ASSUMPTION; medium; Jordan to correct; revert: gate it]` on the role bypass (:9).
- **Bears on:** MB (orders, roles), FA (seat-gated orders, `dispatch`), CHAR (chooser `operand_bags`), CORE.
- **Content that matters:**
  - THE USER'S RULING: the Stop-if ("friction drowns a role's effect") was met on the roles a headcount line's stand-in troop type (`infantry`) may take (`hole_register.yaml` H-361); built as written with `role` ranging over the whole `ROLE_SPEC`, NOT gated by `registry.role_allowed`; pinned by `test_the_role_is_not_gated_by_role_allowed` (`Shock` not in `infantry`'s menu, the order still sets role, shape `Arrowhead`, instruction `charge`) (:7-9, :279-292).
  - Falsifier on paired seeds (`random.Random(0..199)` in both arms): a `Shock` vs `ShieldWall` order on the attacker changes the band distribution by more than +-7 points and the win share; a defender's order changes a defended WALLS field; two orders in two seasons - the newer governs, the older is kept (:131-153). Planted failures: order ignored by `field_input`, module ignoring role, both leave arms equal (:165-180). Controls: no order = field as it was; other faction's, other place's, closed or seatless-holder's order is not read (:185-210).
  - Field sized by hand: "One shipped season fights no `field.won` or `field.lost` (the aperture reading), and at the shipped `field_troops_per_weight` of 1 every subunit routs at tick 1, so no role could matter" (:11-14). SCALE 30, weights 10 vs `(4,4,3,3,3,3)`.
  - `operand_bags` ranges `role` and `retreat_at` over `battle_orders.ROLES` x `RETREAT_AT` = 45 bags, each a distinct act id; `CHOICE_SOURCED["marshal"] == ("role","retreat_at")` (:237-248) - the chooser can enumerate it. The Spymaster grants `dispatch` but his purview doesn't reach HOME: `marshal.unauthorized` (:215-225). A `create_record` of kind `order_of_battle` is declined: only `marshal` mints (:295-306).
  - Export: `tools/export_battle_orders.py --check` run in a subprocess, drift planted two ways (stale artifact; module `ORDER_ROLES` diverging from `ROLE_SPEC`) (:253-276).
  - Hard-coded ids: `p_npc_020` King, `p_npc_038` Cardinal of Justice, `p_npc_033/035` marchers, `set_s_014/036`, `off_king`, `off_cardinal_justice`.
- **Conflicts / stale:** test_cp_t04_03's docstring says "`marshal` ships WITHHELD" from the chooser, so in the shipped game no NPC issues a standing order of battle; the whole order mechanism is hand-folded. Orders set role/retreat but not mixed weapons or loadout (the brief's MB weapon-carry trade-off has no counterpart).
- **Open items:** H-361 bypass of `role_allowed`; `reserve`/`general` keys absent (":no `reserve`, no `general`", :219).

### engine/season/tests/test_cp_t04_03_retreat.py
- **What it is:** behaviour test, CP-T04-03 (B10-12): retreat in good order. A standing order's `retreat_at` (`none`, `0.5`, `0.25`) becomes per-subunit `own_strength:FRAC` Order with the `retreat` stance; a side every one of whose subunits retreated or routed has CONCEDED (`hierarchy/units.py::unit_conceded`); `run_battle` stops for it; `_grade` never calls it the winner.
- **Status:** none; live.
- **Bears on:** MB (retreat conditions, concession, grading), CHAR, DICE (paired seeds).
- **Content that matters:**
  - Falsifier on 200 paired seeds: an attacker with `retreat_at 0.5` against an equal defender loses fewer troops than with `none` (margin 0.01), and is graded the winner in ZERO seeds where its retreat fired; asserts `fired >= 20` and that every seed where arms differ is a seed the retreat fired in and the attacker kept more troops (:107-120). Person arm: fired >= 5 of 100 seeds (:123-129). A retreating defender leaves the field to the attacker (:132-137).
  - HONEST LIMIT (docstring :18-20): on the natural fold no fired retreat is ever ahead on size, so `_grade`'s concession rule cannot be observed by a fold; observed on hand-set units (`_fake_unit` SimpleNamespace) (:171-197). A `0.25` retreat fires in no seed on a single-subunit side because the rout floor comes first (:140-147).
  - Planted failures: order not read (`_retreat_orders` -> ()), battle not stopping (`unit_conceded` -> False), `_grade` blind to concession - each judged by the very predicate (:152-197). Stop test: 60 `run_battle` runs, `stopped >= 5 and early >= 1`, no rout facing flip (:202-217). `unit_conceded` is keyed on the ORDER's `conceded` mark, not stance/`yielding` (a DG-2 fighting withdrawal is not a concession); `"conceded" in units._ORDER_SAFE_FIELDS` (:220-239).
  - Controls: no order and `none` everywhere equal the field as it was, seed for seed (:244-251); an out-of-set `retreat_at` raises (:254-260). `MB_YIELD_*` yield "untouched".
- **Conflicts / stale:** ties to `orchestration.run_battle` re-export (`ED-1043` "moved verbatim"). The concession is a deterministic grading rule (attacker conceded => never wins) given the state; the draw is in the battle itself.
- **Open items:** none.

### engine/season/tests/test_cp_t04_05_graded_walls.py
- **What it is:** behaviour test, CP-T04-05: graded walls: `field_input` hands the engine `int(field_walls_dr * fort_level)` (floor), `None` (shipped) staying `None`; a worn garrison's walls armour the defender less.
- **Status:** none; live.
- **Bears on:** MB (fortification, terrain), SE (garrison condition), FA.
- **Content that matters:**
  - Falsifier: defender win share falls as garrison condition steps 1.0 -> 0.67 -> 0.33 -> 0 under 200 paired seeds at `field_walls_dr=3` (DR carried `[3,2,0,0]`; steps by at least the +-7 NOISE band; the 0.33 -> 0 step is exactly flat because `int(3*0.33)=0`) (:89-108). Planted failure: flat `walls_dr` reddens the same predicate (:111-120).
  - Control: shipped `field_walls_dr = None` is flat across steps still walled and "fort 0 is no wall"; 3 at full condition is the same field as `None`, seed for seed and through the real driver by hash equality (:132-165). `int` not `round` (banker's) (:123-129).
  - Re-picked by MB-07r (weight 10, scale 60): base share 0.49, steps ~10 points. The measured shares are in a comment, a hand-tuned fixture (:31-35).
  - Shipped season fights almost no field (unopposed 3/2, lost 1), so "THE FIELD IS HAND-BUILT" again (:5-8).
- **Conflicts / stale:** `field_walls_dr` shipped as `None` (walls are flat WALLS rows regardless of condition) - the graded walls are not live in the shipped game.
- **Open items:** none.

### engine/season/tests/test_cp_t04_06_besiege.py
- **What it is:** behaviour test, CP-T04-06 (B10-12; AM-C-11 REPAIR): `besiege`, a march that sits before the walls: `march` gains a `posture` payload key (`rosters.yaml: march_postures`, shipped `[storm]`); an opposed `besiege` fights no field, is graded `Invested` (`siege.pressed`), and `_eff_march` lowers each garrison Site in the target's subtree by `_fall(w, site)` directly through the gate.
- **Status:** none; live but UNSHIPPED: the shipped roster is `[storm]`, so `besiege` is a posture no shipped season declares; it is swept in by a test copy (`swept` fixture) (:7-9, :93-98).
- **Bears on:** MB (siege), SE (garrison condition), FA (war), WR.
- **Content that matters:**
  - Falsifier: after k besieging acts the garrison condition reads the `_fall` iterate (test holds its own integer copy: `c - c*1//n`, with `n` fixed at 3 by crowding two bystanders to the garrison's rung): `[667, 445, 297]` from `condition_scale` 1000 (:101-111); the besieger makes no journey (`travel_leg == []`, body 1000). Second half: a storm after a siege wins more often over 100 paired seeds than a storm at full walls (>= 7-point NOISE; measured 0.37 vs 0.52) (:161-167). The n=100 choice is justified in the docstring by the measured gap versus the standard error (:19-22).
  - Write is DIRECT, never staged via `World.stage` (a monkeypatched `stage` that raises); at the realm's garrison `n=1` so one act zeroes the walls ("the entry's stated limit") (:114-119). A second besiege on dead walls: `march.refused` (nothing left to lose) (:122-127).
  - Controls: a storm with the posture named equals the storm with none, hash-equal; an unopposed `besiege` resolves as the storm would; shipped roster refuses `besiege` (`Unspecified`); `operand_bags` fans no posture with `[storm]` and fans two with `[storm, besiege]` (distinct act ids) (:170-202). Planted failures: posture key repointed so the condition never moves; the same predicate reddens (:130-158).
  - "`restore` is never attempted in a natural run" (:11-12): walls are worn only by acts built in the test; the field is hand-built.
- **Conflicts / stale:** the `Invested` band and siege wear are drawless: `_fall` is an integer formula applied to garrison Sites (deterministic wear; the draw is in the later storm). The siege is not a thing an NPC does in the shipped game (roster `[storm]`).
- **Open items:** none.

### engine/season/tests/test_cp_t04_07_surrender.py
- **What it is:** behaviour test, CP-T04-07 (B10-12; AM-C-12 REPAIR): `surrender`: a seat granting `dispatch` whose faction holds a settlement a `siege.pressed` named THIS SEASON gives the place to the person who pressed the siege (`_eff_surrender` through `_take_hold`, `state/gate.py::may_cede`, new `cession` write basis).
- **Status:** none; live but WITHHELD: `"surrender" in w.fixtures.get("withheld_verbs")` (marshal's precedent) so no Candidate forms in the shipped game (:286-298).
- **Bears on:** FA (war, cession, seats), MB (siege outcomes), SC (terms), CORE (gate bases).
- **Content that matters:**
  - Falsifier: a surrendered and a stormed town (same pair, 20 paired `world_seed`s) both end with the hold moved to the Crown, but only the stormed one writes body and stance rows; "the surrendered arm is a draw-free write, so it must hold in 20 of 20" (:19-27, :107-133). The stormed arm's hold move is `seize`, not the field (a won field moves presence, never title, #453 R-6). So a surrender is a DETERMINISTIC yield by seat-holder act, with no draw and no resolution roll (brief's no-deterministic rule: FA/SC lane check).
  - Refusals: wrong-faction seat -> `surrender.refused` and no hold moves; no `dispatch` or no purview -> `surrender.unauthorized`; no siege this season (stale, or siege of another town) -> refused; a place cannot be yielded to one's own side (:173-214). Gate `cession` basis tests (:219-239) and `may_cede` (:242-248); three planted failures (threat reader blank; `may_cede` always true -> `NotYours` at the gate; gate clause removed) (:253-281).
  - A seeded town is held through its territory (no direct `hold` on the town); surrender opens a direct `hold` to the receiver and closes the yielder's direct hold if any, in one write (:136-168).
  - Hard-coded realm ids: `p_npc_020` King, `p_npc_038`/`013`/`034`/`040` Church cardinals/rep, `off_cardinal_*`, `p_npc_033`, `set_s_036`, `set_s_037`.
- **Conflicts / stale:** `surrender` withheld = the strategic result "a place yields on terms" never occurs in a natural season; "A natural run emits no `siege.pressed`" (:14-15).
- **Open items:** the CP-T04-04 `march` handover is "held" (unbuilt), noted at :148-149.

### engine/season/tests/test_cp_t04_08_field_estimate.py
- **What it is:** statistical + behaviour test, CP-T04-08 (B10-12): `field_estimate`, the field prize's input to the one odds reader: `seam/wrappers/mass_battle.py::field_estimate` runs `resolve_field` `estimate_samples` times on the private stream `(world_seed, tick, actor, "estimate")` (shared `_estimate.py` with `combat.fight_estimate`) and returns shares of `Won`, `Lost`, `Unopposed`; `sigma.odds_of` mode (a) returns them for a row contesting `a field`, found through the ESTIMATE provider role.
- **Status:** none; live (a display; no loop calls it).
- **Bears on:** MB (auto-resolve vs played: the estimate and the resolve share one module), GO (display), CHAR, DICE.
- **Content that matters:**
  - Falsifier 1: over held-out seeds the realised `Won` share (200 scenes per pair by the PROVIDER) lies in the 95% Wilson interval of the 50-sample estimate in at least 19 of 20 pairs (weights 3..16 x open/WALLS x {no order, Shock}); a `MAX_HALF_WIDTH` ceiling guards a later change to `SHOWN`; `len({shown}) >= 8` guards against too few distinct figures (:133-137, :111-128). THE TICK IS THE ONE CHOSEN PARAMETER and "was chosen on the figure": tick 9 is "the first that covers all 20"; ticks 5..24 cover 15-20 of 20 pairs, 375/400 (94%), tick 5 landed on 18 (:56-65). So the bar passes at a tick picked to pass it; the docstring says a miss at one tick is one draw of the 94%.
  - Planted failures: sides swapped -> coverage < 19; estimate that drops the standing order -> order predicate reddens; an estimate that draws from the season -> falsifier 2 reddens (:140-196, :331-340).
  - Falsifier 2: a one-season `build_realm(0)` run whose callback calls `field_estimate` before every act ends at the same `content_hash` and the same `w.draw` as the same run without (`calls >= 100`, `sampled >= 1`) (:324-328). The rng is keyed on exactly `(world_seed, tick, actor, "estimate")`; replayed stream equals the figure exactly (:214-229).
  - A given `FieldOrder` replaces the attacker's held order, the defender's order stays (:163-196). Own-faction target -> `Unopposed` with samples 0; party gaps -> `PARTY-GAP`; bad `estimate_samples` -> `Forbidden` (:232-253). `odds_of` mode (b) (a believer's figure) is not built for a field (`AQ-X1`) (:260-273); `registry.check_estimate_providers()` refuses an unknown provider name and so does driver construction (:275-283).
- **Conflicts / stale:** the estimator and the resolver are asserted consistent only at the display, not at the chooser's believed odds (None for fights and fields): an NPC cannot weigh a battle by believed odds. [ties to cp_t03_05]
- **Open items:** AQ-X1 (mode (b) for fields).

### engine/season/tests/test_cp_t05_02_self_plea.py
- **What it is:** behaviour test, v10 CP-T05-02 parts (ii) and (iii) (batch B10-13; home T05, `-08` AM-D-02): THE ACCUSED ANSWERS: the guard in `sigma.contest_input` and the `subject_may_be_self` column on `speak`. Part (i) (`hearing`, `hearing_step`) is HELD on SC-02's design and not built.
- **Status:** none; live. Defines `revert_cp_t05_02` (:42-46), used by other pin tests.
- **Bears on:** SC (self-plea, accusation, opposition), CHAR (stance sign, `regard`), CORE.
- **Content that matters:**
  - Guard: `contest_input` reads NO opposition when the subject IS the actor ("nobody opposes himself"), so a self-plea rolls at `obstacle_default` at any capability he holds (0 or 3 -> the same obstacle); control: the same person as someone else's subject opposes at his capability, `inp.opposition == 3.0` (:59-77). Capability key is `VERB_CAPABILITY["speak"]`.
  - Self-plea: row column `subject_may_be_self` on `speak` ALONE (`confer` has its own `counterparty_may_be_self`) waives `opening_set`'s self-subject decline; a docketed person holding the docketing claim forms `speak {subject: himself}` and none without the column (:102-113); it executes through the fold at a band (a draw) (:115-119). Loader admits the column only on a row contested against its subject (`opponent_operand() == "subject"`), refuses on `tell` and a string `'true'`; admitted on `determine` (CR-16) (:122-137).
  - Stance sign: `_stance_arm` under `stance_polarity: declared` negates regard on a row contested against its subject; a self-plea reads `+regard` (-3 for a person he dislikes), an accusation of another reads `+3.0` for the same regard; `regard` arm reads -3.0 for both (:144-163). A past B10-13 Phase 1 A1 fix (`subject != p.id`).
  - Planted failures are recorded with dates (2026-11-08, reverted) rather than run in suite, except the revert helper and the `monkeypatch` comparison at the stance test.
- **Conflicts / stale:** the speak/argue contest here has the obstacle fixed at `obstacle_default` regardless of capability for a self-plea: a self-plea is the same fixed-obstacle roll for every pleader, i.e. a pleader's own skill sets only the pool. [UNVERIFIED re brief's evidence-as-input intent: this file shows no evidence enters the self-plea's odds.]
- **Open items:** `hearing`/`hearing_step` HELD on SC-02's design.

### engine/season/tests/test_cp_t05_03_tell_refused.py
- **What it is:** behaviour test, v10 CP-T05-03 (batch B10-13; `-08` AM-D-04): a failed telling is realised: `tell`'s `emits_on_refusal` is `tell.refused`; the Failure band keeps `news.untold` on `emits:` alone. Defines `revert_cp_t05_03` (:41-54).
- **Status:** none; live.
- **Bears on:** FI/CHAR (tell, knowledge spread), SC (contest loss), CORE (realised vs refused; R-07).
- **Content that matters:**
  - A LOST telling (contest ran and went against the teller; roll forced to net 0 vs ob 2 via a `MODULE_ENTRIES["social_contest.roll"]` stub returning `Margin(net, ob=2)`) is attempted once in a season (`news.untold` Failure, one event); a REFUSED one (absent hearer) is `tell.refused` with degree None and re-forms each round (`len(evs) >= 2`); a won telling is `news.told` (:83-102). `asked >= 2` guards that the control can see a re-formation (:79).
  - Planted failure in-suite: `revert_cp_t05_03` restores the old kind for the refusal, and the lost telling is retried every round (:88-91). Consequences: `news.untold` is now a deed (`is_deed`) and `tell.refused` is not; since CR-27 `lie` emits `tell`'s kinds and no kind of its own, so these kinds map to no single verb (:105-117).
  - The roll is FORCED by replacing the social_contest module entry (`dataclasses.replace(real, fn=lambda inp, rng: Margin(...))`), i.e. a stubbed draw: tests the loop's handling of a band, not the odds.
- **Conflicts / stale:** nothing.
- **Open items:** none.

### engine/season/tests/test_cr03_acquaintance_arm.py
- **What it is:** a measurement + one hand-built arm, CR-03 (B10-09 close two): half the persons know no one for four seasons. "NOTHING IN THE SHIPPED TREE CHANGES".
- **Status:** none; live as a measurement record. `[ASSUMPTION; medium; Jordan to correct; revert: use seen claims at CENSUS]` (:66-68).
- **Bears on:** CHAR, FI (known persons gate `tell/argue/give/covenant/issue`), SC, WR (R-01/R-07 reach), CORE.
- **Content that matters:**
  - Measured at the base (4 seasons, seeds 0-2, arm `off`): persons who know nobody 83/83 at build, ~30/75 after four seasons (38-43% still know no one); median/max known 1/7; told claims in all ledgers at s4: 0, 0, 4 (:11-29). `known_persons` has three sources only (an `exists:Person` reading, a `seen` claim's `who`, a told claim's `chain[-1]`) (:8-9).
  - What the block costs: `tell` forms one Candidate per person the teller knows (`to`); `argue`, `give`, `covenant`, `issue` the same (`VerbRow.known_person_operands`); a person who knows nobody forms none. `argue` is blocked twice over: no question in the realm names a Proposition (formed for 0/0/0 persons) (:37-42). At realm scale the control forms `tell` for 0 persons, the arm for 46 (:31-36).
  - The test arm: `seed_acquaintance_from_concerns(w, rows)` (defined in the test file, not shipped) writes the committer's OWN `exists:Person` claim of the person concerned-about, from `npcs.yaml` `concerns` rows (46 rows); a 5-person ring; control forms nothing for anyone (`checked == 5*2`), arm forms `tell`/`argue` for the 4 ring persons and not for the stranger; the arm's ledgers differ from the control's by exactly 4 claims (:136-192).
  - The ask recorded for the close note: "should the realm START with acquaintances?" - a dense versus sparse social graph "changes what the game is"; wiring into `build_realm` is a declared hash mover and NOT done (:62-64).
- **Conflicts / stale:** the shipped realm starts with no acquaintance (83/83 know nobody at build) so `tell`, `argue`, `give` form for nobody at the start, contrary to R-01/R-07 reach; the later CR-81 (realm acquaintances) file may have answered it - see test_cr81. Docstring numbers are a past measurement; the 'tests' assert only the hand-built ring.
- **Open items:** the ask above.

### engine/season/tests/test_cr17_odds_weighting.py
- **What it is:** chooser behaviour + hash/temperature tests, CR-17 (M1, AQ-X1 (b)): a person's believed chance weights the pursuit term of a contested candidate (`decision/choose.py::odds_weight`, `Fixtures.odds_weighting`, H-248). Read to :248 by addendum C; read in full here.
- **Status:** none; live.
- **Bears on:** CHAR (chooser, R-06/R-08), SC (argue), DICE (believed odds), CORE.
- **Content that matters:**
  - Two persons with EQUAL pursuits and believed chance 0.7 vs 0.1 rank `argue` against an uncontested rival `carry` differently at `believed` and alike at `none`; planted factor-1 weighting reddens it (`pytest.raises(AssertionError, match="one ranking")`) (:101-117, :167-171). A believed `None` ranks and scores exactly as `none`; an uncontested verb is not even asked; the bands asked are the row's own non-empty `writes:` lists, a proper subset of the ladder (:119-164).
  - The `cells` fixture plants an `argue` alignment cell (`ALIGNMENT[grandiose_humble][argue] = 1.0`) because "`argue` carries no alignment cell in the shipped table" (:57-63): in the shipped game `argue` has no pursuit alignment, so the pursuit term for `argue` is 0 (CHAR/SC lead).
  - Real reader: pools differing by a `POOL_ADDENDS` entry (monkeypatched) give believed chances equal to `odds_of` mode (b) summed over writing bands, the stronger higher by > 0.2, and rankings part on it; a holder-bound query answers for its holder alone (None for another's act) (:200-230). A driver season hands every View a callable `odds` (`answered >= 1`) (:245-265). `fight` and a foreign actor's act are unknown (None) (:233-242).
  - TEMPERATURE: `test_tau_is_the_largest_grid_value_above_one_half_strict_top_decided_and_zero_is_the_argmax` at seeds 0-2 on the built realm: shipped `choice_temperature` (0.05) reads > 1/2 of vectored readings strict-top-decided (measured 271/297/273 of 498), every larger grid value reads <= 1/2 (0.1 -> 142/162/141), and tau 0 is the argmax (every reading decided) (:272-305). So at the shipped tau roughly 46% of readings are NOT the top-scored (relevant to R-08).
  - HASH PINS (:308-367): with `odds_weighting: none` and `choice_temperature 0.1` the one-season `build_realm(0)` reads `content_hash().startswith("eea8eaf8")` and `len(w.log) == 10397`; with capture/challenge/accept withheld `("c1bf72d0", 11016)`; inequality asserted. The pin is read behind EIGHT in-process reverts (`revert_cr79, revert_cr87, revert_cp_t03_04, revert_cp_t03_07, revert_cp_t03_08, revert_cr78, revert_cp_t03_02, revert_cr85`) and a non-shipped fixture pair - F-TEST-02's "world nobody plays" at maximal depth, plus a re-pin log of 8 entries (:354-358). The `ctl` "card's control" is "executed (it was prose in go07 and weather)".
- **Conflicts / stale:** the hash pin world is not shipped (non-shipped arms, 8 reverts). The "shipped pair does not (685 acts, 11775)" statement ties to a past count.
- **Open items:** none.

### engine/season/tests/test_cr19_competence_gain.py
- **What it is:** behaviour test, v10 CR-19: `AX-7`'s competence reads Attunement (`H-200`): `competence_gain`, SHIPPED AT 0. `decision/options.py::refracted_confidence` gains a swept `competence_gain`; factor `competence(p, g)` monotone in the receiver's Attunement (`Person.attributes`, CR-20), exactly 1 at the scale's middle (`COMPETENCE_MID == 4`) and 1 with no authored Attunement.
- **Status:** none; live code, inert at the shipped gain.
- **Bears on:** FI/CHAR (receiver competence, R-07), CORE.
- **Content that matters:**
  - Shipped gain is 0.0, so in the shipped game receivers of different Attunement hold a told claim at equal confidence (`DEFAULT_FIXTURES.get("competence_gain") == 0.0`, :66-68). Why shipped 0: "a person-side gain cannot separate a lie from a truth" (`ED-IN-0327`), left to CR-27's `lie` and CR-83 (:6-8).
  - Falsifier at a live test-local gain 0.5: Attunement 2 vs 6 hold one told claim on one channel at 25 vs 37 (37 * (1 + .5*(2-4)/3) = 24.67 -> 25; 6 capped at 1) (:70-73); at gain 0 equal; no authored Attunement -> 1. Monotone in attunement over 1..7, floor 0.0 at gain 1; `ValueError` outside the unit interval (:87-101).
  - Realm control: `build_realm(0, cast_attributes=True)` one season equals the world with `competence` made constant 1, by hash and `(kind, id)` log; built with `cast_attributes=True` because otherwise nobody holds Attunement and the equality would be true by construction (:113-128, the B10-10 Phase 3 close).
- **Conflicts / stale:** the only person with an authored Attunement in the whole cast is NPC-001 (see test_cr20), so the factor cannot differ between receivers in the shipped game even at a live gain.
- **Open items:** the flip to a live gain is "a later declared mover".

### engine/season/tests/test_cr20_attributes.py
- **What it is:** behaviour + loader + source-scan test, v10 CR-20: the attribute carrier `Person.attributes` executed (pools and opposition from the ten attributes via `VOCATION_ATTRIBUTE`).
- **Status:** none; live. Part of §14 capability authoring surface.
- **Bears on:** CHAR (attributes, vocations, §14), SC (opposition), DICE (pool), PC (attributes feed `arms`), CORE.
- **Content that matters:**
  - Pools: persons holding 2 and 6 on a vocation's attribute and no held key roll pools 2 and 6 (`sigma.faculty`); opposed at raw 2.0/6.0; the obstacle halves to Ob 1 and then the H-213 chance-floor cap bites: a 6 against a roller of pool 2 reads the CAP (`_chance_floor_cap`), not 3 (:61-78). A person with nothing authored gets `pool_default`; `_opposition_of` is None for him ("never the fallback") (:65-67). Planted failure: removing `pool._authored_attribute` makes the 6 roll 2 (:81-86).
  - Pool is the LARGER of the base attribute and the held (practised) key; opposition the larger of key and attribute; a held key alone (even 0) stands alone (:100-120). A verb with no vocation (`determine`) ignores attributes (:89-93).
  - Roster closed both ways: `set(VOCATION_ATTRIBUTE) == set(VOCATIONS)`, values within `descriptors.ATTRIBUTES` (the ten); loader refuses a vocation with no row, a non-vocation row, a non-attribute, and the retired `attr.social.bonds` (:127-144).
  - Cast: `cast.attributes_of` reads `stats:`; legacy spellings resolve (`cognition`->`attr.mind.acuity`, `presence`->`attr.social.charisma`, ranges take the lower bound); luck, bonds, out-of-1..7, floats, bools, strings, two spellings of one key refuse; `social` as a category refuses (:151-171). The shipped cast has 46 entries and `NPC-001` is the one that authors six attribute values `{acuity 5, focus 5, endurance 4, attunement 3, charisma 3, grace 3}` (:177-181) - `>= 1` person authored, `== 46` rows (count pin).
  - SHIPPED ARM: `build_realm(0)` (`cast_attributes=False`) leaves every person with no attribute; `True` writes the one row (NPC-001) (:213-222). So in the shipped game NO person has any attribute: every pool is `pool_default` unless a practised key (`capability`) is held.
  - No matrix row for `Person.attributes` (gate refuses `matrix_row`, `w.write` raises `Unspecified`) (:188-197); `creation_sheet` carries a read-only copy (`TypeError` on assignment) (:200-206). Setter scan (AST, `scanned > 50`): only `harness/populated.py` assigns `attributes`/`heritage`; `{f for sites} == fields` guards population (:232-257).
- **Conflicts / stale:** the docstring cites `test_k3_thread_sensitivity.py (e)` as the sibling. Attributes: "a written-at-build field with no play-time writer" - no training, aging or injury changes an attribute (R-06 lead: characters cannot grow through attributes; growth is via `capability` keys only).
- **Open items:** attribute authoring is data-only for one NPC; the other 45 cast rows have no `stats:` (CHAR/§14).

### engine/season/tests/test_cr21_cells.py
- **What it is:** data test, CR-21 (M14): the cell-value and cosine pass: pursuit projection (15x7), alignment cells, refusing pole as roster data (H-146 repair).
- **Status:** none; live.
- **Bears on:** CHAR (pursuits, alignment, deontological refusal), SC, FA, CORE (§14).
- **Content that matters:**
  - cos(wealth, happiness) reads 0.818 (was 0.969) computed in the test from the roster's 15x7 `pursuit_projection`, not via `data.pursuits`; control evaluates the OLD cell (`happiness[D/I] = 0.4`) and reproduces 0.969 (:42-55). The `effective_axes` figure moves 3.81 -> 3.93 and `within_60deg` stays `(4, 15)`; `approx(abs=0.01)` on a two-decimal reading (addendum: "tolerance on a two-decimal reading and says so") (:58-73).
  - Named cell values: `V.PURSUIT_PROJECTION["happiness"][DI] == 0.0`, `ROLE_TEMPLATE_PURSUITS["intelligence-diplomatic"]["community"] == 0.10`, `align("restore", PS) == -0.2`, `ALIGNMENT[RF/DI]["deed:commitment.ended"] == 0.4/0.8`; `restore` now celled, `thread_read` CONSIDERED and `null` on all seven axes (so it scores 0.0 and counts as none) (:76-90).
  - A deontological witness of a vow-break reads LOWER regard for the releaser with the `deed:commitment.ended` cells than without; an instrumental witness the other way (control that the cells are read) (:107-125). The most deontological/instrumental pursuits are FOUND on the projection (min/max), not named.
  - `refuses(verb, axis, weight)` reads the refusing pole from `rosters.pursuit_axes.refusing_pole` (the NEG pole refuses, ED-IN-0261); poles swapped inverts both verdicts; an axis with no authored pole, or a malformed one (`0, 2, -2, "negative", None, True`), refuses rather than defaulting; arming the gate on an unruled axis refuses at `refusal_tolerance` (:162-219). Exactly ONE axis has an authored refusing pole (deontological_instrumental) (:151-155).
- **Conflicts / stale:** `doctrine` row is "PROVISIONAL, Jordan's" and its pair is not pinned. Loader refusal `is declared uncelled: and is celled on` tested for `restore`/`thread_read`.
- **Open items:** only one refusing-pole axis is ruled; other axes cannot arm a refusal gate.

### engine/season/tests/test_cr25_computed_establish.py
- **What it is:** behaviour test, v11 CR-25: a computed `establish` founds an office over a holding (CR-11's design; M8's H-132 (b), H-144 (b)).
- **Status:** none; live.
- **Bears on:** FA (offices, governance, territory), SE, CORE.
- **Content that matters:**
  - A King holding territory `T` inside his purview founds `Lord` there (`founded_office_id("T","Lord")`), `w.offices` gains the derived row: post from `TITLE_DOMAINS` (first post in authored order whose kind is the rung's), remit = the seat's less `confer` and `revoke`, `conferral="appointed"`, `revocation="rung_above_in_holdings"`, faction `Valorsmark` (:67-78). Unheld territory refuses (`establish.refused`); planted failure `in_holdings -> True` founds it, so the refusal is conjunct (i)'s (:81-94).
  - Equal rank refuses (the Confessor at `terr_T9`) but the test "CANNOT TELL (iii) AND (iv) APART" and asserts both false (:97-111). A re-remit of a VACANT office outside purview refuses (H-144 (b)), control the seat with purview executes; a REDUCTION of a `revocation: None` seat's grant refuses (H-132 (b)) with a widening and a basis-admitted reduction as controls; the founder revokes the founded Lord through his seat (:114-169).
  - `holdings_to_found` on `build_realm(0)`: COUNT PIN `sum(map(len, found.values())) == 14` (every one a territory under a duchy whose duke holds it) (:183-192). Effect and precondition read one derivation (`office_founded_by is _preds.office_founded_by`) (:172-180).
  - No draw: founding is an eligibility-decided act (outcome fixed by state) and `confer` of the Lord goes through the same non-rolled path.
- **Conflicts / stale:** founding an office has no contest or draw at all (eligibility conjuncts decide) - a bookkeeping/eligibility check by the brief's definition, acceptable.
- **Open items:** (iii)/(iv) indistinguishable by a test.

### engine/season/tests/test_cr27_lie.py
- **What it is:** behaviour test, v11 CR-27 (M9 taken (a); H-357; H-198 rule (i)): `lie`, a spoken falsehood on a held cell claim; `lie_said_of` makes the said false at CHOOSE; same row, contest and kinds as `tell`.
- **Status:** none; live. `Fixtures lie_offered` SHIPPED True. The DEED lie (H-198 rule (ii)) is unbuilt.
- **Bears on:** FI, SC, CHAR (deception, R-07), WR.
- **Content that matters:**
  - A lie to a hearer who holds nothing deposits a false value (8 -> 12, "one whole step of `told_drift_band`'s unit", `ceil(0.5*8)=4` above) with `chain == (T,)` (the liar is the origin), leaves the liar's own cell unchanged, emits only `tell`'s kinds (no `lie.*` kind) (:106-117). A lie to a hearer who holds the cell firsthand lowers the liar's `record(H, T)` below 1.0 while an honest teller's reads >= 1.0 (:120-129). The contest roll is FORCED by stubbing `MODULE_ENTRIES["social_contest.roll"]` to `Margin(net=3, ob=2)` (:70-92): the lie's success is not tested as a draw.
  - False-value rule: a number moves one whole step, sign-preserving, never across zero (`{8:12, 1:2, -8:-4, -1:-2, 3:5, -3:-1}`); a truth value flips; a held zero, band of zero, non-roster value, deed kind, `seen`, and empty ledger give `None` (nothing false to say) (:172-200). Liar's number and the channel's lossy copy share one owner `person_q.drifted` (monkeypatch both and both read the owner) (:203-213).
  - The offer is gated in `opening_set` (`lie_offered`), not in `resolvable_verbs()` (:149-152); at False `lie` is absent and `tell` still offered (:140-146).
  - A deceit's detection is only `record(H,T)` for a hearer holding the cell firsthand; a hearer with no prior can't detect it.
  - Measured gap pinned: at a live `competence_gain` 0.5 a receiver at Attunement 6 holds a LIE with HIGHER confidence than one at Attunement 2 (`got[KNOWNOT] > got[HOLDER]`), "until CR-83" supplies the lie/truth separator; "THIS ASSERT TURNS RED WHEN CR-83 SUPPLIES THE SEPARATOR; invert it then", plan rule P8 forbids a standing xfail (:251-259). A test deliberately asserting the defect.
- **Conflicts / stale:** `lie` has no forged-evidence or concealment link; a "lie" is just a drifted number. Brief's lie/forgery questions: no document forgery here.
- **Open items:** CR-83 (lie/truth separator); deed lie.

### engine/season/tests/test_cr28_propositions_heard.py
- **What it is:** behaviour test, v11 CR-28 (G-04 (a), CP-T02-05's re-take): `world_q.propositions_heard` stamps Propositions a person has heard of from another as class `Proposition` on the question he answers.
- **Status:** none; live.
- **Bears on:** CHAR, WR (narrative propagation), FA (commit), CORE.
- **Content that matters:**
  - A claim another's act left (`proposition.uttered`) names the Proposition and the term returns it; his OWN act's claim (`Claim.doer == p.id`) does not; a non-Proposition id the same ledger names is not returned (:52-68).
  - The stamp: the question carries `(HEARD, "Proposition")` in `q.classes`, and `commit` forms on it; planted failure (term stubbed to `()`) forms no `commit` (H-156 REM-23's tree) (:73-90). With a live `commit` on it `commit` is not formed again (`held_edge_declines`) but `argue` still is (:94-107). Through the real fold the candidate emits `commitment.made` and opens his live `commit` edge on a Proposition another uttered (:112-124).
  - Realm readings are "commit-body readings, never assertions here".
- **Conflicts / stale:** imports fixtures across files (`test_in53_vacancy_need`, `test_works_founding`).
- **Open items:** none.

### engine/season/tests/test_cr30_heritage.py
- **What it is:** data + behaviour test, v10 CR-30: `Person.heritage` as a read-off descent field and the `marks` term's carrier.
- **Status:** none; live.
- **Bears on:** CHAR (identity), FI (what a witness sees), WR (caste/descent politics), ARCS.
- **Content that matters:**
  - A co-located witness's `seen` claim reads `marks == (heritage,)` and `who == actor`; an unauthored actor reads `()`; planted failure (`TERM_READERS["marks"]` stubbed to `()`) (:46-58).
  - Roster: `descriptors.HERITAGES == (northern_einhir, central_einhir, southern_einhir, altonian, schoenlander)`; `HERITAGE_ENGAGES == {southern_einhir: einhir, altonian: altonia}` into `AFFILIATION_CONCERNS`; exporter `export_descriptors.build()` refuses a bad engagement (:65-87). Cast row naming an unrostered heritage refused (`martian`, `Southern_Einhir`, `""`, 3, list, True) (:89-98); no matrix row, gate refuses a write (:101-111).
  - AUTHORED set pinned exactly: `NPC-020` northern_einhir (King Almud, `canon/03_canonical_timeline.md:138`), `NPC-052` southern_einhir (Duke Magnus Vaynard, `:144`), `NPC-011` altonian, `NPC-012` schoenlander (birthplace rows); 4 of 46 persons carry heritage (:118-133).
- **Conflicts / stale:** the comment cites `canon/03_canonical_timeline.md` lines. Heritage is read-only descent; only canon-grounded rows.
- **Open items:** none.

### engine/season/tests/test_cr31_heritage_regard.py
- **What it is:** behaviour test, v11 CR-31: `person_q.heritage_regard`, `regard`'s third term at `Fixtures heritage_gain` (H-358): the caste estimate. A hearer's creed (`conviction`) vs a teller's seen heritage marks.
- **Status:** none; live (shipped `heritage_gain` 0.5, `stance_polarity` `declared`) (:168).
- **Bears on:** CHAR (conviction, bias), FI/SC (credence of a teller), WR.
- **Content that matters:**
  - Two hearers equal in stance toward one teller seen as `southern_einhir`, one holding `einhir_restoration: 5` and one `0`, weight the same told claim differently at gain 0.5 and identically at 0 (:73-80). A hearer who never saw the teller marked, or sees a mark that engages no concern, reads the term 0; an absent conviction key reads 0 (not held), a stored 0 is a held rejection and pulls hardest (`-STANCE_MAX`), 5 reads `+STANCE_MAX`, 2/3 symmetric (:82-106). Planted failure: `conviction_stand` sign flipped reverses the pair (:108-114).
  - The belief is the newest OWN untold `seen` claim marking a heritage (round breaks ties); told or other-person marks don't count (:121-132). The term is in regard's units, scales with the gain, raises on negative/NaN gain, reads the hearer's own ledger alone (:135-154).
  - Polarity arms: `legacy` ignores the term, `regard`/`declared` read it; on an opponent row (`fight`) `declared` NEGATES it (:161-180).
  - The one conviction axis wired to a heritage is `einhir_restoration` (and `altonian_civics` for altonian); `HERITAGE_ENGAGES` has two entries.
- **Conflicts / stale:** the control (`heritage_gain` 0 reproduces the pre-item hash) is "recorded in the commit body, not asserted here: a hash is no pin".
- **Open items:** none.

### engine/season/tests/test_cr33_lifepaths.py
- **What it is:** loader + behaviour + hash-control test, v10 CR-33: the 34 lifepaths as creation templates: capability keys HELD, the lifepath never a field (`R.LIFEPATH_TEMPLATES`, `cast.capability_of`).
- **Status:** none; live. HASH PINS: `BASE` three literals (a64160d4..., 2f6a308e..., 6b7e5242...) behind `revert_cr79` and the expansion stubbed.
- **Bears on:** CHAR (§14 character creation templates, capability authoring), ARCS (cast), CORE.
- **Content that matters:**
  - `len(R.LIFEPATHS) == 34`, the four struck Niflhel ids (`3-NI1..4`) are not members; `set(LIFEPATH_TEMPLATES) == set(LIFEPATHS)`; templates name only `VOCATIONS` values; some map to none (`holds: []`). Loader refusals: unknown vocation, struck id, missing row, duplicate key, empty ground, non-list holds (:89-121).
  - `cast.capability_of(row, pool_default)` holds each key at `pool_default` and silence is no key; a cast row naming no template (`"3-NI1"`, `"3-cr1"`, `3`, `True`...) refused (:128-139). Registry AUTHORED set pinned: NPC-002 `3-VA1`, NPC-004 `3-CH5`, NPC-005 `3-LO3`, NPC-080 `3-LO3`, NPC-088 `3-CF4` (:78-82).
  - A planted `lifepath` on NPC-087 (a row with none) builds `capability == {"inquiry": pool_default}`, rolls the same pool on `research` as NPC-084, `train` on `inquiry` executes for the holder (`capability.raised`) and is refused for the other (`train.refused`); the lifepath id is stored nowhere (not in `repr(Person)` and no field named `lifepath`/`vocation`) (:178-203). In the shipped realm the holders are exactly `{p_npc_004, p_npc_088}` plus the planted one: only TWO shipped persons hold any capability key (:184-186).
  - Control: expansion stubbed reproduces `BASE` (the pre-commit 1-season hash) per seed; expansion on differs at seed 0 (:219-232). The pin comment lists NINE re-pins each with a named revert control.
- **Conflicts / stale:** the "mover is the one row that maps to a key": the lifepath system yields capability for 2 of 46 NPCs; the rest of the 34 lifepaths map to none or are unused. [CHAR lead: capability data is nearly empty in the shipped game.]
- **Open items:** none.

### engine/season/tests/test_cr34_declared_disposal.py
- **What it is:** behaviour test, v11 CR-34 (C-7, `ED-SC-0034`, H-161): the declared disposal is read: `determine` on a matter whose docket item names an arrangement row declaring `disposal: declared` gains a `vote` conjunct counting live `commit` edges of distinct bench members (`judging_set`) to an OUGHT Proposition about the party naming the kind the row `disposes:` (`ban`); `world_q.declared_votes` is computed on read, stored nowhere. `excommunication_deliberation` is the first declared row, `quorum: 2`. `[ASSUMPTION; medium]`.
- **Status:** none; live code, hand-built evidence only.
- **Bears on:** SC (proceedings, bench votes), FA (governance, church bench), ARCS.
- **Content that matters:**
  - REALM REACH IS 0 and the file says so: "no computed `open_case` names an arrangement (H-80), so the realm never meets a declared row" (:10-14). A computed docket item naming an arrangement (petition route or `judging_set` mapping) is the residue. So a vote at a sitting is not reachable in computed play.
  - One bench-member commit -> `determine.refused` on the `vote` clause (`declared.votes` 1, `declared.quorum` 2 in `Event.observed`); two -> `matter.determined` with degree in `(Overwhelming, Success)` and a `ban` opens (:92-104). Not a vote: a creed commit whose subject is the accused (the "loyal-creed hazard"), another subject, mood not OUGHT, predicate not the kind, an ENDED commit, two commits by one member (distinct members), a non-member's commit (:107-157).
  - Sweep: with exactly two votes quorum {1,2,3} admits at 1,2 refuses at 3 (:179-188). Controls: `legal_trial` (bench) admitted with `votes 0, quorum 0`; at quorum 1 with the determiner committed the outcome equals the bench reading (:160-206). Ambiguous docket (two items for one matter, one declared) reads `UNKNOWN` and `_eff_determine` declines (:209-224). Tally stored nowhere: the count follows the edges (:227-238).
  - Voting is deterministic count (>= quorum live commits) with no draw at the vote; the draw is the `determine` degree afterward. [SC lane: per the brief's rule, whether "votes meet quorum => bound" is a fixed function of state - check against G-65 and the proceedings ownership ruling.]
- **Conflicts / stale:** "H-80: no arrangement named" in computed play contradicts the idea that an arrangement is the proceeding's rule set: arrangements are reachable only by hand-planted dockets.
- **Open items:** computed docket naming an arrangement.

### engine/season/tests/test_cr55_matter_lapses.py
- **What it is:** behaviour test, v11 CR-55: a matter lapses visibly: a docket item held beyond `Fixtures docket_lapse` seasons is taken off the docket by MATTER (one gate write, `matter.lapsed`, `causes` the docketing Event); an overdue term stage matures once (`loop/matter.py`).
- **Status:** none; live. Shipped `docket_lapse` is 4 (":the shipped rule (4) cannot fire inside two seasons, so the instrument reads it at 0", :337-341).
- **Bears on:** SC (docket, proceedings), FA, WR (term/stages), CORE.
- **Content that matters:**
  - Three docket facts held an item for ever: a dead party, a venue with no bench, a matter that is no person; all lapse at the barrier opening `t + lapse + 1` (heard through `t + lapse`); seen red with the mechanism removed (planted failures recorded in docstrings, run 2026-11-08, not in suite except via assertions of `_outlives`/`lapsing_items`) (:65-117).
  - Empty slot lapses too, chained on the `docket.formed` that made it (its age is the Date's `due_at`); a slot emptied after a re-slot lapses on the slot-forming Event, not the re-slot's (:119-153); a carried matter ages from the carry, not an older `open_case` (B10-13 Phase 3) (:156-177); an undated matter the lapse is about to take is not re-slotted (:180-198); neighbouring items lapse at their own counts (:201-213).
  - Control `docket_lapse = None`: nothing lapses in 12 seasons; an item with no docketing Event has unknown age and does not lapse (:220-236).
  - Overdue stage matures once: `due != w.tick` never matured it; once-guard reads the last maturation BEFORE the pass; a stage wound by an ACT id (no logged Event names the Record) is guarded via `last_emission_of(..., written=True)` (:243-319).
  - Realm reading at lapse 0 vs None, 2 seasons seed 0: `len(lapsed) >= 1` and none under control; every lapse names a docketing Event in the log, a `matter.lapsed` claim reaches a ledger, hashes differ (:326-351). The shipped lapse 4 is therefore never observed in a played realm by a test.
- **Conflicts / stale:** shipped `docket_lapse = 4` is unexercised; a lapse is a deterministic age rule (bookkeeping, a clock's tick).
- **Open items:** none.

### engine/season/tests/test_cr56_matter_stamped.py
- **What it is:** behaviour test, v11 CR-56: the matter is stamped where it waits: `world_q.matters_awaiting(w, p)` stamps, as `Rung`, the lowest of `p`'s own convening seats containing a waiting undated person-matter's place (so `convene` forms on the tier that can hear it); CALENDAR's re-slot moves each undated person-matter into the open slot `world_q.slot_for` finds. Two `[ASSUMPTION; medium]`s.
- **Status:** none; live.
- **Bears on:** SC (docket, convening, venue), FA (seats' convening acts), CHAR (what questions an officer is handed).
- **Content that matters:**
  - Stamp: control with no docketed person-matter stamps nothing; after `open_case` the Duke is stamped `("D",)` and `convene` forms on `D` (and not before; `places_named` never offers a venue the Duke lives under); a person with no convening seat is offered nothing; of two convening seats the lowest containing the matter is stamped (`("D",)`, then `("D","R")`) (:65-97). A matter outside every convener's seat is neither stamped nor slotted (:90-97).
  - Stamp displaces no question (stop condition): question ids equal with the term stubbed out; `len(without) >= 2` (:100-110).
  - Re-slot: a waiting matter fills a later slot that reaches it; the slotting Event `docket.formed` anchored at `D` and caused by `date.fired`; a non-person matter (a rung) is never re-slotted (:117-138). `CONVENING_REMIT_ACTS == {"convene"}` (count pin, :61-63).
  - Seeded readings are in the item receipt, not pinned.
- **Conflicts / stale:** the helper functions `_convene_at`, `_next_calendar` are imported by `test_cr55`.
- **Open items:** none.

### engine/season/tests/test_cr69_chains.py
- **What it is:** instrument test, CR-69: `harness/chronicle.py::consequence_chains` (`--chains --min-depth D`), the story reading; "A READING, NEVER A GUARD".
- **Status:** none; live (an instrument of the narrative surface).
- **Bears on:** WR (narrative reading, emergent chains), ARCS (arc reading), CORE (R-01 chains).
- **Content that matters:**
  - Planted world with 4 writing chains of depth 3, a writing chain of depth 2 and a non-writing chain of depth 4: `chain_ends == 4` at min-depth 3, 5 at 2 and 1, 0 at 4; `consequence_acts == 14` (the non-writing chain is not one); kinds histogram read off the log (`war.ended`, `heir.named`, a planted `grudge.sworn` appears; the reader holds no roster) (:67-96).
  - Shuffled-`causes` null (8 seeds) reads strictly below (`ARC.shuffled_causes`, the single null shared with `harness/arc.py`) (:99-111); same world twice reads identically; planted failures: counting every act, ignoring min_depth (:125-142). CLI: `--chains` without `--min-depth` refused (exit 2), plain output untouched (:155-169).
  - A real seeded run (`SB.drive(0, 2, "off", 10)`): reads identically twice, writes nothing (hash, log length, `w.writes` unchanged), `consequence_acts > 0 and chain_ends > 0`, null differs (:174-185).
- **Conflicts / stale:** the chain reader counts only chains of acts whose Events write Receipts on the ARC rosters; belief-only changes (WITNESS) aren't consequences (cf. cl_thrust_b01).
- **Open items:** none.

### engine/season/tests/test_cr81_realm_acquaintances.py
- **What it is:** build-property test, CR-81 (B10-09 close two, `ED-IN-0318`): the realm starts with acquaintances (Jordan 2026-11-04: "many characters should already know each other based on faction belonging, and high status characters will know each other (eg Duke Duchess king queen)"): `harness/populated.py::acquaintance_pairs` / `seed_acquaintances`, run last in `build_realm`; `acquaintances=False` is the control arm.
- **Status:** none; live. HASH PINS: `PARENT_HASHES` three build hashes (control arm), `KNOW_NONE_AT_BUILD = 41`.
- **Bears on:** CHAR (social graph), FI (known-person gate on `tell`, R-01/R-07), FA (faction membership), WR.
- **Content that matters:**
  - Measured: persons who know no one at build 83 of 83 -> 41 of 83 on every seed; 236 `exists:Person` claims (226 faction co-member pairs + 10 high-status pairs); `tell` forms for 0 -> 37 persons. The 41 are 37 cohorts (no faction commit, no seat), 3 cast members in no faction, 1 member of Schoenland's one-member faction (:6-17). Derived from two routes in the test (`_expected_pairs` from the person's end `faction_holding`, high set via Jordan's four words `King/Queen/Duke/Duchess` over `OFFICES_SEATS`) (:74-95); `checked == 3*236`.
  - `[ASSUMPTION; medium]`s: "know one another" mutual and complete within a faction; the duchy seats are the high-status set; added claims evict none. IN PLAY THE THIRD IS MEASURED FALSE: ledgers reach `ledger_cap` 200 in season 1, a base claim ranking below an acquaintance claim is evicted (peaks 93/142/152 displaced); acquaintance claims fade (0, 11, 0 of 236 still held at season 4). "A durable acquaintance would need a carrier eviction does not reach: not ruled, not built." (:19-28).
  - Control: `acquaintances=False` reproduces the parent hashes (`b9928b27..., d58a1395..., cb800549...` after re-pins by CR-86/CR-20+30/CR-33/CR-87/CP-T03-07) and the arm's ledger less the added claims equals the control claim by claim; no ledger over `ledger_cap` (:136-154). Planted: `seed_acquaintances` a no-op reddens the exit (:157-165).
  - Hash comment lists SEVEN re-pins of the control arm.
- **Conflicts / stale:** supersedes `test_cr03_acquaintance_arm.py`'s measurement (CR-03 said the realm starts with none; CR-81 wires it in). CR-82 raised the cap so the fade at 200 is now the control arm.
- **Open items:** durable acquaintance carrier (not ruled, not built).

### engine/season/tests/test_cr82_ledger_retention.py
- **What it is:** behaviour test, CR-82 (`ED-IN-0319`): what a person knows of others is kept for years, not seasons: `ledger_cap` raised 200 -> 3200 (Jordan 2026-11-04: "people don't stop knowing people or claims that quickly"); comparator `state/ledgers.py::eviction_key` unchanged.
- **Status:** none; live.
- **Bears on:** CHAR/FI (memory, R-07), CORE (ledger eviction), WR.
- **Content that matters:**
  - At shipped cap (3200) the 236 acquaintance claims are still held at season 2 (`held > HELD_FLOOR 200`, measured 221); at the control cap 200 `held < FADED_CEILING 170` (measured 147) on seed 1, 2 seasons; the bounds are "deliberately loose": the test is about the lever, not a golden (:47-58). Measured elsewhere (H-09's cite): at season 4 seed 1: 6 at cap 200 vs 208 at 3200; through eight seasons 202 and 196 of 236 at 3200 vs 0 and 0 at 200 (:7-11).
  - "this directory no longer builds a four-season realm (the user's v9 section 0.5 ruling, recorded at the `season-tests` CI job's comment), and eight seasons is about six minutes on one seed" (:13-17): the test horizon is two seasons by a runtime cap, the long-horizon claim is not under test.
- **Conflicts / stale:** none. Time horizon: "two years at four seasons to the year, `ED-IN-0332`".
- **Open items:** none.

### engine/season/tests/test_cr85_faculty_replaces_history.py
- **What it is:** behaviour + hash-control test, CR-85 (ED-IN-0330/0331): combat's pool and Ob read `faculty` not `history`: `sigma.faculty` -> `combat.combat_input` -> `PersonalCombatInput.faculties` -> `modules/combat/fight.py`: pool `max(5, faculty + 6)`, Ob the opponent rolls against `faculty / 2`. `[ASSUMPTION; medium; revert: delete the design file; history stays]`, built on `proposals/2026-11-05-cr85-...md`, which is UNRATIFIED (ED-IN-0349 withdrawn by ED-IN-0351). Defines `revert_cr85` (:73-78).
- **Status:** none; live. HASH PINS: `PRE_ITEM`, `POST_ITEM` (six literals).
- **Bears on:** PC (the combat roll's inputs), CHAR (§14 capability -> pool), DICE.
- **Content that matters:**
  - In the shipped game EVERY season fight rolls pool 8 against Ob 1.0 (`(8, 1.0)`), because no verb names a combat key so `faculty` = `pool_default` 2 (:12-14); mutation (faculties dropped, module default 3) reads `(9, 1.5)`; a party holding a test-local combat key at 5 rolls pool 11 and his opponent rolls against Ob 2.5 (:129-168). So persons do not differ in fights in the shipped game. (Later `arms` CP-T03-04 wires the key but nobody holds it; test_cp_t03_04.)
  - `build_realm(0)` forms no fight in one season since CR-87, so the falsifier reads seeds 1 and 2 (:20-22); seed 0's hash does not move (`PRE_ITEM[0] == POST_ITEM[0]`).
  - Control: seam's faculty replaced by 3 for every party reproduces the pre-item hash exactly (the five deleted sigma terms were 0.0 in every season fight: both parties at history 3, empty `skills`) (:136-147); the falsifier test runs behind FOUR reverts (`revert_cr79`, `revert_cp_t03_04`, `_07`, `_08`).
  - Autouse fixture `_engine_available` calls `pytest.skip` if `C.engine()` is None (F-TEST-11) (:44-50).
- **Conflicts / stale:** the item cites an unratified design file; the design's `skills`/`history` fields are "deleted" from the pool but "history stays" as data.
- **Open items:** ratification of `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md`.

### engine/season/tests/test_cr86_realm_structure.py
- **What it is:** build test, CR-86 (ED-IN-0342): the realm's structure: Valorsmark a faction, the vassals sworn by `oblige`, the heads seated.
- **Status:** none; live.
- **Bears on:** FA (factions, heads, vassalage, purview), CORE (realm build), SE (territory).
- **Content that matters:**
  - `faction_q.head` of Valorsmark is the King (`p_npc_020`); Hafenmark `p_npc_050`, Varfell `p_npc_052`, Church `p_npc_021`; `len(HEAD_SEAT) == 4`; a faction with no `head_seat` (Guilds) has head None; vacating the King's seat removes the head (:31-47).
  - `Crown` is an alias of Valorsmark (`cast.resolve_faction("Crown")`, `office_faction`), not a roster member; `>= 5` registry Crown rows, none of the built offices carries `faction == "Crown"`, `>= 8` carry Valorsmark (:50-66). An office whose `body:` implies a faction different from the alias refuses (`Forbidden`) (:56-58).
  - Vassals: the Duchess (p_npc_050), the Duke (p_npc_052) and the Grand Master (p_npc_070) are sworn to `off_king` by live `oblige`; in the as-built realm the King reaches a Varfell territory by containment alone (control); planted: cut `duchy_varfell` out of the realm and only then does the Duke's `oblige` edge decide `purview_reaches`; dropping the edge leaves it unreached; the Duchess's edge does not bring Varfell's ground (:69-100). The Church territory already has its dwelling (:103-107).
  - Everything is keyed on hard realm ids (`p_npc_0xx`, `terr_T12`, `duchy_*`).
- **Conflicts / stale:** none.
- **Open items:** none.

### engine/season/tests/test_cr87_violence_contexts.py
- **What it is:** behaviour + hash-control test, v11 CR-87 (ED-IN-0335..0337, 0340; commit `c7145842`): violence made exceptional. Six parts: `rosters.yaml: violence_contexts` (a person-side formation decline: `fight` forms on a subject only where the actor holds a context against him: war, crime, duel, defence), `fight` alignment cells -0.3 on all seven axes, the grudge's bound `hostile_stance_gain`, a computed duel fought to `blood` and `challenge` asks a DISPUTE, build-time loyalty toward the creed never its head, coercion rows keep their gates. Defines `revert_cr87` (:358-374), imported by many other files.
- **Status:** none; live. HASH PINS: `BASE_BUILD = "837d0f83..."`, `BASE_SEASON = "bcc4ee3f..."`.
- **Bears on:** PC (when fights happen), CHAR (grudge, contexts, NPC chooser), FA (war, warrants, detainees), MB, ARCS (war and crime arcs), WR.
- **Content that matters:**
  - With no context `fight` does not form (but the question forms other acts); each context forms it: war (an `Enemy` class stamp via `enemies_heard`, only once he knows of a live war with a live commit), crime (a held warrant record whose `to` names the actor; the maker is not charged; or a `Detainee` stamp), duel (a held challenge naming both), defence (an attack he saw this season, deed claim on its patient + sighting; older attack no) (:78-131). Emptying `VIOLENCE_CONTEXTS` forms `fight` again (:133-137). Roster refusals: unknown verb, empty list; readers closed (:140-147).
  - Realm falsifier: seed 0 season 1 via `harness/interactions.py`'s own run: `fight` formations on same-faction persons at stance >= -3 are 0 (base: 110 formations, 68 same-faction, 65 of them at stance >= -3), Cardinal->Senior-Inquisitor and Spymaster->King formations are 0 on seeds 0-2; the mutation (decline deleted) restores them (positive control) (:312-337).
  - Costs: `fight` and `accept` -0.3 on every axis; `challenge` keeps -0.6 (grandiose_humble) and -0.3 (deontological_instrumental). A grudge on a violent row reads `hostile_stance_gain` (0.5 in test) and in a war context a -4 grudge still ranks `fight` first at the shipped bound (:176-215). A computed duel is fought to `blood`; named stakes (`death`) still govern; unchallenged `fight` keeps the lethal default (:218-221). `dispute` is a WORLD-ONLY stem read off the actor's own judgement: a deed claim of B's that A's pursuits score against him (:224-238).
  - `loyalty_in_band` cuts a negative loyalty row to the member band (-1,4)->(-1,1); no creed-loyalty row names a faction head below the band; with `loyalty_toward_creed` False the Spymaster holds the grudge toward the King (the audit's finding) (:245-262).
  - Hash: with the block empty and every value at its revert, plus SEVEN more reverts (`revert_cr79, revert_cp_t03_02, revert_cr85, revert_cp_t03_04, _07, _08`), the build and one season equal `BASE_BUILD`/`BASE_SEASON` (:377-393) - F-TEST-02 pattern; `shipped build != BASE_BUILD` so the control is not vacuous.
- **Conflicts / stale:** violence is by a formation decline, a deterministic gate on candidates (eligibility, defensible under the brief's rule), but it means in the shipped game "a fight" appears only with a context; CR-85/CP-T03-01 notes that seed-0 forms no fight in a season.
- **Open items:** none.

### engine/season/tests/test_cr96_opposed_by.py
- **What it is:** loader + behaviour test, v10 CR-96 (AR-44): the OPTIONAL `opposed_by:` column per `vocation_attribute` row (`VOCATION_OPPOSED_BY`), which makes a party oppose with a different attribute than the one his own pool starts from.
- **Status:** none; live code, UNUSED in the shipped roster: `VOCATION_OPPOSED_BY == {}` asserted (:51-60).
- **Bears on:** CHAR (§14 capability axioms: attack/defend attribute pairing), SC (opposition), DICE.
- **Content that matters:**
  - With `opposed_by: attr.mind.will` a party holding Spirit 6 and the verb's own attribute 2 opposes at 6.0 (obstacle 3.0 when the roller's pool is 7 so the H-213 ceiling doesn't cap), without the column at 2.0 (Ob 1.0). The column REPLACES the own attribute (own 9 vs Spirit 6 reads 6.0, not the larger) and moves opposition only, not the pool; a held key still competes (larger of key and the opposing attribute) (:62-105).
  - Shipped roster absent on every row so `_opposing_attribute == _authored_attribute` for every verb and person (`checked >= 10`) - the control for the hash; planted failure (column ignored reads 2.0) (:51-60, :89-96). Loader refuses an attribute outside the ten, a retired `attr.social.bonds`, empty, a non-vocation (:108-120).
- **Conflicts / stale:** infrastructure exists for attack-skill vs defence-attribute pairing (a classic RPG axiom) but no shipped row uses it ("CR-95's, not this position's").
- **Open items:** CR-95 (the shipped opposed_by rows).

### engine/season/tests/test_cr_24_winner_casualties.py
- **What it is:** behaviour test, CR-24 (`H-360`, M4 Ask B (b)): the winners of a fought field take their own engine casualties on `body` only; `field_winner_casualties: engine` SHIPPED, `off` the earlier behaviour.
- **Status:** none; live.
- **Bears on:** MB (casualties, field outcomes), PC (body), CHAR (commanding persons).
- **Content that matters:**
  - A real fold of a hand-built situation (RESOLVE then ENCOUNTER via `test_march._fold_one`): Crown marchers as cohorts weight 10, `field_troops_per_weight` 10, `field_subunits: person`. Seed 0: the attacker WINS, one marcher's subunit cut (survivor ratio 0.982), the other's not; each attacking claimant's body = `max(1, int(body * min(1, his own ratio)))`; no stance row on any winner; the defenders (losers) still take theirs (:86-103). Preconditions asserted.
  - Why `person`: under `side` a winning headcount side's ratio reads >= 1.0, so the `side` arm writes a winner nothing (:13-15).
  - Planted failure: winners written at the loser's ratio reddens the check (:106-120); control `off` writes no winner and `engine` differs in the one marcher's body alone (restore it and the hashes are equal) (:123-136); a winner who marches is one Subject (named whole) and no Subject names a winner's `stance` (:139-159).
  - `field_casualty_model: total` ("any wound is lethal"): a winner who took a casualty is removed by the loser's rule and does not arrive (the ratio-0.982 marcher dies); `none` writes no winner (:162-179); an unknown arm refuses (:182-186).
- **Conflicts / stale:** `total` casualties kill a winner with a 1.8% loss with certainty (deterministic lethality in a non-shipped arm; the shipped `scaled_by_degree` arm is non-lethal): relevant to the brief's no-deterministic rule (MB lane).
- **Open items:** none.

### engine/season/tests/test_demand_delivery.py
- **What it is:** behaviour test, plan position `19d` (DEMAND-DELIVERY; `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` §3.2 row 11): `world_q.demanded`/`delivered`, `subsistence_draw` (host projection of the larder draw; arithmetic owner `settlements.larder_draw` in `modules/settlements/larder.py`), the shortfall Observation on MATTER's `stores.changed`, `_from_shortfall_claim` operands, `harness/scarce.py`.
- **Status:** none; live. The workplan it cites is `retired` in its filename (:2): reference only.
- **Bears on:** SE (subsistence, larder, shortfall), CHAR/FA (steward response), WR, CORE (witness).
- **Content that matters:**
  - `demanded` is the weighted headcount under a rung (`Person.weight` IS the headcount; a cohort of ten wants ten people's share); `delivered` is `min(want, stock)` per kind with the same keys; an individual steward is EXEMPT from the draw (`24f`, ED-IN-0255) so the granary demands nothing; an empty larder still demands (the rejected "walk ends at" reading) (:98-130). MATTER removes exactly what `delivered` said and leaves the rest short in `w._subsistence_shortfall` (:133-145).
  - The shortfall rides on the drained larder's OWN `stores.changed` write as an `Observation` (predicate `SHORTFALL_PREDICATE:<kind>`), nothing else carries one; a never-stocked larder reports nothing but the person is still short ("the crossing, not the state") (:152-179). `tiny_world` and `headless.build_world(0)` have no eater at all (only cohorts draw), so no shipped small world records a shortfall (:182-198).
  - Deposit: the holder who was elsewhere holds the shortfall `told_by` (document channel), the hungry hold it firsthand; without the `hold` edge the steward learns nothing; `observation_deposit_mode: none` deposits nothing; an act's reads still reach only its actor (:220-273).
  - Operands: `kind`/`amount` read off a held shortfall claim ahead of fixtures (`SHORTFALL_SOURCED_OPERANDS == {"kind","amount"}`); a bad amount (0, -3, True, 2.5, "8", None) falls back to `default_transfer_amount`; a non-shortfall claim reads nothing (:290-336). The real chooser executes the claim-sourced `transfer` and matter is conserved against a no-act control; the next season's `delivered` at the hungry town rises against a no-`hold` control (0) (:381-418).
  - The behaviour-equivalence of the extraction "cannot be re-proved by a test inside the tree"; claimed byte-identical hashes out-of-band for 4 worlds.
- **Conflicts / stale:** the season's question is NAMED (the driver's probe override), "WHICH question a person answers is `H-54`'s open rule" (:383-384): the shortfall response needs the question handed to the steward.
- **Open items:** `H-54` (which question a person answers) open.

### engine/season/tests/test_fa06_org_goals.py
- **What it is:** data + builder test, v9 FA-06: every other organization's goals (`goals.yaml`, `data/goals.py`, `harness/populated.py::seed_goals`) and the completeness refusal at seeding (`build_realm(goals_complete=)`).
- **Status:** none; live.
- **Bears on:** FA (organization goals, rivalry), CHAR (conviction/goals), ARCS, CORE (data-driven goals).
- **Content that matters:**
  - Shipped file complete: `goals_missing(shipped, goals.goals()) == []`; every faction with an authored head and every body with a seated member holds a row (`len(heads) >= 6`, `len(bodies) >= 10`); census `(goals, goal_orientation, goal_dropped) == (14, 24, 0)` (ED-IN-0310: two Altonian rows seated by default) - a COUNT PIN (:59-70). Deleting one row lists exactly that org (:73-83); `build_realm(0)` raises `Unspecified` naming the body/faction; control `goals_complete=False` builds; `goals=False` never asks (:90-120).
  - Rival goals carry `stance -1` toward the rival head's seat (Hafenmark vs Confessor `off_confessor`; Church vs Restoration leader `off_restoration_leader`); members take a stance row against `p_npc_021` / `p_npc_003` (:127-139).
  - `establishes`: Inquisitors (`p_npc_004`, `p_npc_038` exactly) hold the narrower heresy goal, the rest of the Church (incl. the Confessor `p_npc_021`) the Church's goal, and the two sets are disjoint (:146-151).
- **Conflicts / stale:** the "Nine Political Axes as data" claim in the docstring ties to the rival-goals file; goals are a typed file read by the loader, satisfying the data-driven requirement.
- **Open items:** none.

### engine/season/tests/test_faction_q.py
- **What it is:** unit test for `queries/faction_q.py`: `resolve, holdings, purview, superiors, subordinates, at_war, head`.
- **Status:** none; live.
- **Bears on:** FA (factions, war, headship, subordination), SE (holdings), CORE.
- **Content that matters:**
  - `faction_q.members is world_q.members` (identity, not equality - "every rule lives once"); `holdings`/`seats` match a set re-derived from `w.tenures` directly (not via `world_q.members`), vary across factions (not a stub), and `holdings(w,p)` is `resolve(w,p).holdings` (:53-97). `purview(w, seat)` is the sorted set `{rung} | descendants(rung)` and agrees with `gate.purview_reaches` for every rung of the world; rungless/unknown seat -> `[]` (:100-120).
  - `superiors`/`subordinates` read a hand-built `oblige` edge both ways (subordinates equal `sorted(world_q.establishment_of(...))`) (:123-143).
  - `head`: control that no live `commit` in `build_realm(0)` carries a `Tenure.degree` (scan, not `head`'s own return); two factions with no `head_seat` (`fac_schoenland`, `fac_guilds`) read None; Valorsmark's head is `p_npc_020` (CR-86); hand-graded live commit picked up; last write wins; a closed edge (`t.live`) is dropped (:150-211). `head` is an old "degree on a commit tenure" reader, vacuous in the realm; the real head is `head_seat`.
  - `at_war` through the real fold: `utter` (mood WAR, subject A, value B) then `commit` to `prop:<act id>` -> war True both directions (unordered pair); `release` -> `["tenure.closed", "commitment.ended"]` (the maker's hold closes too) -> False (:224-261). So war/peace is declared by one person's utter+commit and ended by one release: no contest or draw.
- **Conflicts / stale:** `head` docstring reasoning ("vacuous") is stale once `head_seat` exists; the file keeps both. War declaration with no resolution roll (FA lead): a single actor's `utter`+`commit` makes `at_war` true.
- **Open items:** none.

### engine/season/tests/test_fi01_graded_inquiries.py
- **What it is:** behaviour test, v9 FI-01 (`ED-FI-0009`; J-22 answered option (A)): a degree producer for the inquiries; the deposit half built as the SKIP arm (RS-21 item 1, H-111 ANSWERED [medium; Jordan to correct]). Imported by `test_aperture.py`.
- **Status:** none; live.
- **Bears on:** FI (inquiry grading, evidence deposits), SC (the shared roll owner), CHAR (what is written to ledgers), R-02/R-07.
- **Content that matters:**
  - `graded_inquiries` routing roster: `research`, `examine`, `surveil` (place case) graded; `interview` is a prompt (K-36); `reconstruct`/`thread_read` wait (K-37/H-85) (flat `emits:`) (:45-51, :83-94). Graded rows emit by degree `{Overwhelming, Success, Partial, Failure}`, `Failure` -> `finding.none`.
  - Skip arm: a `Failure` research (act ids swept up to 60 until one draws `Failure` and one a finding band) emits `finding.none` and deposits NO claim (ledgers equal before/after WITNESS); `finding.made` deposits; a REFUSED research (no such Record) emits `finding.none` with degree None and deposits nothing; control: a refused `tell` (`tell.refused`) still deposits (the arm keys on the kind `finding.none`, `UNDEPOSITED_KINDS`) (:97-156). So a failed investigation leaves no trace in anyone's knowledge (no "I looked and found nothing" belief).
  - The route is not a prize: no graded verb declares `contests:`; route keys are exactly `{provider, module_entry}`; loader refusals (routed row that also contests; flat `emits:`; a `module:` key; a misspelled skip kind `finding.nnoe`), and a route to a roll no prize row binds refuses at driver construction (:159-220). Examine at a present Site is graded (sweep 60) (:223-239).
  - ONE roll owner: replacing the `social_contest.roll` module entry with fixed `Margin`s moves the inquiry's band band-for-band (net 5/3/2/0 vs ob 2 -> Overwhelming/Success/Partial/Failure); the inquiry is handed no opposition and `pool_default` (:242-262). An inquiry admits before it rolls (:265-277). Realm: one season of `build_realm(0)` has a `finding.*` Event with a degree and `(kind == finding.none) == (degree == Failure)` (:280-291) - an existence claim, no count.
- **Conflicts / stale:** an inquiry's pool is `pool_default` (no investigator skill; the verb's vocation `inquiry` is held by 2 persons only) and obstacle default 2 (no clue/evidence quality input): fieldwork success is not a function of evidence held (brief's detective-game intent, FI lead).
- **Open items:** `interview` as a prompt (K-36); `reconstruct`/`thread_read` wait on K-37.

### engine/season/tests/test_g1a_act_store_and_receipts.py
- **What it is:** unit test, G1a: the act store (`state/acts.py::ActStore`), the receipt mint (`state/gate.py::Gate.mint/issued`) and the two things the log (`state/log.py::EventLog`) refuses.
- **Status:** none; live. (Part of the gate family addendum C names strongest, F-TEST strongest list.)
- **Bears on:** CORE (AX-4 one write path; provenance of Events).
- **Content that matters:**
  - Act store append-only, refuses duplicate id without half-applying, iteration returns a COPY, refuses non-Acts (:30-55). Gate refuses to mint with no write open; `issued` is an IDENTITY check (a forged `Receipt` `==` to a real one on every field is not issued); closing the window stops the mint (:59-89).
  - OBSERVABLE: a hand-built receipt in an Event fails `append`, a minted one passes (:94-105). FALSIFIER: an act-caused Event appended while the act store is empty fails, and the same Event passes once the act is in the store (:122-135); causes naming a prior Event resolve, an invented one does not, `ROOT` always resolves (:138-150). Log is reversible, indexable, sized (:155-165).
  - `test_a_bare_statechange_is_still_admitted_and_this_is_the_transitional_seam` PINS A WEAKNESS deliberately: `EventLog` admits a bare `StateChange` (probes build one at `harness/probes.py:1797`), so provenance is "checkable but not yet compulsory"; "when `G4` closes the seam this test goes red and has to be deleted ON PURPOSE" (:108-117). [Whether G4 closed it: UNVERIFIED here; test_g4 is the sibling.]
- **Conflicts / stale:** references `world.py:625`, `harness/probes.py:1797` line numbers that may have drifted.
- **Open items:** the transitional `StateChange` seam.

### engine/season/tests/test_gate_remove_person_requires_an_open_write.py
- **What it is:** unit test, `GATE-REMOVE-PERSON` (plan position 7, 2026-09-29): `World.remove_person` refuses with no gate write open (AX-4 "one write path" made mechanical for this function).
- **Status:** none; live.
- **Bears on:** CORE (write gate, death path), PC/MB (removal of persons).
- **Content that matters:**
  - Four arms: (1) a bare `w.remove_person` raises `InstrumentDefect` and mutates nothing; (2) the real callers' pattern `world.write(..., apply=lambda: w.remove_person(...))` succeeds, person gone, edges closed; (3) the REALISTIC case: after a prior successful write the gate has closed again so a later bare call still raises (found at the Phase-1 close: `write()`'s success path did not call `gate.close()` and `is_open` stayed True forever, making arm 1's guard vacuous in any played world; `hole_register.yaml` H-131); (4) a write whose mutation succeeds but raises from its own tail (S33: declared emission with no `subject=`) still closes the gate via the `try/finally`, proven by a second bare call on an unrelated victim (:49-129).
  - A model case of a test catching its own vacuity: arm 3 and 4 exist because arm 1 alone could not distinguish "guard works" from "gate permanently open".
- **Conflicts / stale:** none.
- **Open items:** none.

### engine/season/tests/test_g1b_attribution.py
- **What it is:** unit + corpus test, G1b: attribution without `Event.subject` (the field is deleted); `state/attribution.py::actor_of`/`anchor_of`.
- **Status:** none; live. Plan position 4 (2026-09-26). Addendum C: read in full, strongest family.
- **Bears on:** CORE (event provenance, WITNESS anchoring; R-01 chain walkback), WR.
- **Content that matters:**
  - `Event` has no `subject/actor/target` field and refuses a `subject=` kwarg (executed fact of `04:402`) (:58-66). An act-caused Event attributes to that act's actor; MATTER's wear has no actor (`actor_of` None, `anchor_of` the written thing); the actor channel wins over the change channel; first cause resolving to an act wins; tier 3: a consequence (`condition.band_crossed`) inherits its cause's anchor (:71-126). An Event reaching no tier returns None.
  - Falsifier 1 over every fan-out arm (`sorted(FAN_OUT_MODES)`, sorted so `-n auto` collects the same): an anchorless planted Event (`plague.struck`, no change, `[ROOT]`) is deposited to nobody, control is the same kind carrying a change naming `R` which IS deposited; `total` is why every arm is run (before `claim_subjects` it minted `Claim(subject=None)` into all five ledgers) (:151-198).
  - Falsifier 2: every probe in `P.PROBES` run, every World captured by monkeypatching `World.__init__`: no logged Event anchors on nothing, population floor `anchored >= 5000` (measured 10,559 Events over 111 Worlds) (:203-254).
  - Falsifier 3: four (seed, seasons) pairs: `actor_of` agrees with the id the fold MINTED from the actor (re-derive `H(seed, tick, actor, "{kind}:{act}")`); each tier-2 anchor is a receipt `Gate.issued`; `by_act` and `by_receipt` both nonzero; `len(log) >= 20`; and `>= 10` actorless Events at seed 0 x 2 seasons (:267-330). A tier-3 crossing check against `w.crossings` is RETIRED when `11a` deleted the attribute, carried to `test_season_shape.py::test_w4_a_band_crossing_walks_back_to_the_wear_that_caused_it`.
  - Deleted-on-purpose test `test_tier_4_is_the_field_and_it_is_the_blocker`, noted in a comment at :129-134.
- **Conflicts / stale:** `[JUSTIFIED: A VACUITY FLOOR ...]` and `[JUSTIFIED: SEEDS ...]` comment tags. Count floors (5,000; 20; 10) justified as vacuity guards, not pins.
- **Open items:** none.

### engine/season/tests/test_g2_token.py
- **What it is:** scan + gate test, G2: one `Token`, minted in `loop/driver` only (plan position 5; `04:199`, `04:206`): AST scan, gate refusals, the fold's class check, and DELIBERATE mutating no store by any route.
- **Status:** none; live. Strongest family per addendum C (`test_g2_deliberate_mutates_no_store_by_any_route`).
- **Bears on:** CORE (AX-4, R-03 DELIBERATE pauses/doesn't write; token), CHAR (player spaces), GO.
- **Content that matters:**
  - Scan: no `Token(` outside `loop/driver.py`, no `mint_token(` from game code (harness/tests may call), aliasing/rebinding flagged; floor `len(src) >= 60`, names the seven step modules (`calendar, matter, deliberate, resolve, encounter, witness, census`), positive control: exactly one construction (the driver). Four plants in `loop/deliberate.py` (construct, mint, alias, rebind) must be found; the same plant in the driver must not (:95-133). The scan's blind spots named (`type(t)(...)`, `dataclasses.replace`, `copy.copy`) (:62-65).
  - `season()` hands six steps a `mint_token` in classes `{calendar: CALENDAR, matter: MATTER, resolve: ACTS, encounter: ACTS, witness: INTERIOR, census: MATTER}` and `deliberate` none (:136-160).
  - Gate: a write with a bare class/None/str credential fails as `NoToken` (not `ShapeGap`), the control write with a token applied; a token from another tick is refused; the token is frozen; the order: absent row + no token -> `NoToken`, absent row + token -> `Unspecified` (:175-223). The fold given a MATTER token at RESOLVE is refused with `where == "S30.2"` (:230-249).
  - DELIBERATE mutates no store: `_store_digest` digests EVERY `vars(w)` attribute (except `step`, `_in_parallel_map`) by content (so a new store is covered by default) around every DELIBERATE call; season arm (floors `calls >= 8`, `acts >= 30`); PLANTED arm calls DELIBERATE on a world with an unhomed Tenure (the only state in which the old `_rehome` mutated); the digest is shown to see `_rehome`; a SPACES arm (v10 REM-30 IN-47) runs the player's character-sheet spaces inside DELIBERATE and a planted space that writes `p.scar` reddens it (:308-414).
- **Conflicts / stale:** the scan covers `engine/season/` only.
- **Open items:** none.

### engine/season/tests/test_g4_no_op_receipt.py
- **What it is:** behaviour test, G4: `NoOpReceipt` and the final effect contract (plan position 7; `04 §C.2` F9): the gate compares before/after and refuses a receipt for a subject nothing moved.
- **Status:** none; live. Addendum C: read in full; strongest family.
- **Bears on:** CORE (write gate; effects are `Change` objects), PC (wound scar rider removed IN-08 H3), FA (convene, transfer).
- **Content that matters:**
  - An effect that names a subject and moves nothing is refused (`act.refused`, no `set` receipt on `Hh`); CONTROL in the same test: `World.state_of` patched to always-unequal reproduces the pre-G4 contract and the same plant SUCCEEDS with a receipt (:64-88). An effect on the retired contract (mutate, return ids) is refused by TYPE (`InstrumentDefect` "Change") (:91-99).
  - F3 (NotYours) is asked before F9: an unnamed unlawful closure of `p_high`'s seat is `NotYours` and the seat stays live; control: without the unlawful write it is `NoOpReceipt` (:106-133). A no-op puts back a lawful edge its closure opened; naming the edge (`Subject.edge(t)`) keeps it (:136-160).
  - Per-effect: `fight` is judged on body and existence; a `Wounded` scene that took no health is `kill.refused`, `body.changed` not published, and a refused wound scars NOBODY (IN-08 H3 retired `scar_step`); control: a half-health wound moves `body` to `body // 2` and DOES scar an observer; second identical `convene` in a season is `convene.refused`, a different `when` reschedules; a `transfer` from a rung to itself is refused (628 of 900 corpus `transfer` effect calls were `r_hearth -> r_hearth`) (:174-239).
- **Conflicts / stale:** `test_g1a`'s `StateChange` transitional seam: this file does not close it; `P.about` Events still use bare `StateChange` [UNVERIFIED re whether G4 closed it].
- **Open items:** none.

### engine/season/tests/test_g3_not_yours.py
- **What it is:** behaviour test, G3: `NotYours` at the gate, `Act.via`, purview through `via.scope` (plan position 6; `04 §C.2` F3 / AX-4 clause 2): every Tenure write must be T-m (owner), T-n (declared term maturation), T-o (a seat whose revocation basis reaches it, `via` present), cascade (existence change this act caused), or conferral basis.
- **Status:** none; live. Defines `_gov_world` (imported by `test_cl_thrust_b01_arc_reader.py`, `test_cp_t03_00`, others). Addendum C: gate family, not itself read in full there.
- **Bears on:** FA (governance: confer, revoke, establish, purview, seats), CORE (gate), SC.
- **Content that matters:**
  - Plan's falsifier: revoking the duke THROUGH `off_mayor` (a seat whose basis does not reach) by an actor (`p_king`) who also holds `off_crown` (which would) is refused `NotYours` at `F3`; control: same write through `off_crown` applies. Proves the basis walk reads `via`, not the actor (:111-132).
  - Every live violation refused without basis and admitted with it, counted and set-asserted `{revoke, confer, fight}` with `_admits` bypassed by a `gate_only` fixture so only the write gate can refuse (:145-211). Fifth clause (conferral-basis opener) tested both arms with five refusing cases (no seat exercised; a seat with no purview over S; a seat the actor doesn't occupy; the seat being conferred; a seat declaring no conferral basis) (:218-265). At the precondition `_req_confer` asks the gate's own `may_fill` and, for a held seat, `may_revoke`: the King (R is not S's parent) cannot displace a sitting reeve, the duke (D is S's parent, same faction) can (:268-292).
  - A `revoke` with `via=None` is refused at the gate and, through the shipped fold, `_eligible` declines so it emits `revoke.refused` (defence in depth) (:299-338). T-m never admits self-seating on an unrelated seat (found by an antagonist pass 2026-09-26) nor self-re-stamping one's own grant without a superior's basis; a sole holder's resignation is still T-m (:361-430). `establish` re-stamp of another's grant needs the conferral basis; the refused act's OFFICE write (`remit_acts`) is NOT undone, "the gate restores the tenure store only (`World._restore_tenures`, H-130's class)" - a pinned bound (:438-464). An edge's ends cannot be rewritten (:482-491); a refused opening is removed (:494-503).
  - Purview = ruling (4) (`ED-IN-0256`): reflexive on the seat's rung, every rung inside, King over the duke's ground, nothing upward/sideways, rungless seat nowhere; counted `checked >= 25` (:506-529). The chooser mints `via` from the same grant person-side eligibility admitted on, swept over every verb x person (`admitted >= 20`, `remit_only >= 5`) (:532-561). Six bases (`T_M, T_O, CONFERRAL, CASCADE, HANDOVER`) each observed ADMITTING through a spy on `tenure_write_basis`; `T-n`/`renewal` are in `test_term_upkeep.py` (:564-602).
  - Governance decisions are eligibility/authority checks (no draws) - consistent with the brief's allowed class; but `revoke`/`confer` outcomes between legitimate seats are fully determined by state (an officeholder "always" can revoke): the brief's "binds"/"senior office always wins" lens (FA lane).
- **Conflicts / stale:** the unreleased bound that a refused `establish` still writes the office (H-130).
- **Open items:** none.

### engine/season/tests/test_give.py
- **What it is:** behaviour + gate test, plan position 16 (`15a`): `give`, the `H-84` verb, and the gate's sixth basis `handover`.
- **Status:** none; live. Records `plan position 14` (typed `give` with `with` stem, `_req_give` retired).
- **Bears on:** FA/SC (documents, Records change hands), FI (document channel), CHAR (known-person operands), CORE (gate).
- **Content that matters:**
  - A `give` between two co-located persons closes the giver's `hold` and opens the receiver's in ONE write (the tenure store's diff is exactly those two edges; `hold_force` moves; receipts name the two EDGES, never the Record); the previous holder's `document_key` channel stops firing and the receiver's starts (needs `w.discard_caches()` between asks) (:117-147).
  - Plan's falsifier through two real seasons: the receiver's `content:<kind>` claim is minted in the season of the handover with the giver's exact value and did not exist before (`got[0].when == t_give`); control: undo the widening of WITNESS's deposit trigger (`_hold_tenure_ends`) and the receiver learns nothing (:154-206). The stage clock is set far away (`w.tick + 50`) because the default matures a term the season after the mint and would deliver the content by the Record's id (found by the control failing) (:164-170).
  - Gate: a write opening the receiver's `hold` WITHOUT the release is `NotYours` and put back; two live holders make `hold_force` raise; with the release admitted under `handover` (the last verdict per edge: old `T_M`, new `HANDOVER`); a release in an EARLIER write licenses nothing; one release hands on ONE edge; a seat cannot be handed over; a closure that is not the actor's licenses nothing (:224-324).
  - Precondition: non-co-located `give` refused (control: co-located executes); to oneself, not holding it, no receiver, receiver not a person -> `give.refused` (:331-352). `give` forms per known person (the `to` fan over `known_persons`), none to himself, a giver who knows nobody forms none; the `counterparty:` column is a second guard (planted) (:366-400); loader refuses a counterparty that is no operand (:403-415).
  - A `give` is certain given eligibility (no contest; `contests` empty).
- **Conflicts / stale:** the first `_at_resolve` helper uses a `petition` to make a Record; `ED-IN-0210` ruling 1 cited. 
- **Open items:** none.
