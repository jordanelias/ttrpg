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
