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
