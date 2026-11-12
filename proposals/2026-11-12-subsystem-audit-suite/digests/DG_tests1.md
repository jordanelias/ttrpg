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
