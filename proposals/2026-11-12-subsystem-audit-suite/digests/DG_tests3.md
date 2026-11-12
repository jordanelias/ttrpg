# Digest tests3

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: 15 season test files under `engine/season/tests/`. Cited findings are `F-TEST-nn` of
`audits/01_CORE_audit_addendum_C_tests.md`. Of its 7 hash tests that apply here, see per-file notes.

### engine/season/tests/test_record_kind_fold.py
- **What it is:** pytest file, plan position `15` (v9-v10 era): `Petition`/`Dispensation` as kinds of `Record`, not two dicts on `World`.
- **Status:** no Status line (test file; docstring only). Reading: live.
- **Bears on:** CORE, SC, FA (documents/writs), CHAR (ledger deposit).
- **Content that matters:**
  - `World` has no `petitions`/`dispensations` attribute and neither is in `_STATE_COLLECTIONS`; `records` is (:65-71). Assertion can fail on a re-introduced store.
  - A `hold` on a dispensation lands on a `Record` the invariant sweep's `I._entities` sees; `rec.rung` comes from `Act.via` seat's rung `"D"` (:74-87). Uses `_mint` at a synthetic RESOLVE barrier with the real `EFFECTS`.
  - L35: `Record` refuses missing key, extra key, unknown kind, non-mapping `subject_matter`; control = exact key set, keyless `text` kind (:94-112). Guards its own vacuity (`assert keys`, :96).
  - `petition`, `issue`, `carry` are all in `resolvable_verbs()`; `VERB_TABLE["carry"].writes` pinned to 4 cells, `issue`/`petition` to `("Record.exists",)` (:119-137). Pins the verb table's write-column text (a hand-copied roster).
  - A filed petition deposits `content:petition` (verbatim, frozen/hashable) in the petitioner's ledger only; control: `create_record` text kind deposits nothing, with `assert texts` (:158-190). Seeded `tiny_world` driven by a scripted `choose`.
  - `issue` run through the real precondition: via `None` -> `issue.unauthorized`, mints nothing; via `off_duke` -> `dispensation.issued` with `subject_matter == {"terms","to":[...],"at":None}` (:193-228). `to` is ONE id, not a list (cell asks about one executor).
  - Two-sided (ED-IN-0210 r2): no Candidate petitions its own petitioner; control clears `counterparty:` and the self-addressed one forms (:248-258). Loader refuses `counterparty: site` the typed cell does not bind (:276-288).
- **Conflicts / stale:** Docstring block 3 and the renamed test docstring (:119-125) narrate two flips (positions `19`, v9 IN-45): docstring "`issue` is NOT [resolvable]" at :14 is now false while the assertion (:129) says resolvable; a stale module docstring. Citations to "r2 `05:671`/`05:1245`", `04` PART A row 11, `ED-IN-0210` are archived/prose referents, not opened [UNVERIFIED]. Not a hash test; no hash pin. Does not hit F-TEST-02.
- **Open items:** none in file. R-04 (strategic acts) bears: this is a hand-built-act file, the F-TEST-01 shape (writes via `_mint` and scripted `choose`, not shipped realm).

### engine/season/tests/test_rem14_predicates_trace_clause.py
- **What it is:** pytest file, REM-14 (v10): each refusing branch of five predicates leaves one DECISION `TRACE` row naming the clause.
- **Status:** no Status line. Reading: live.
- **Bears on:** CORE (trace/report), FA (release/revoke/dispatch/convene/march predicates).
- **Content that matters:**
  - `_req_release`: admitted act leaves `rows == []` (control), non-owner leaves exactly one `refuse` row whose clause contains "does not own"; the no-subject clause is a different string (:43-62).
  - `_req_revoke`: all four refusals plus an admitted control on `test_g3_not_yours._gov_world`; the conferral-basis clause is reached only by hand-mutating `Office.conferral` after construction (:65-97). Imports a fixture from another test file (coupling).
  - `_req_dispatch`, `_req_convene` (both refusals; `World(world_seed=1)` with two planted rungs), and `sides_of` at a non-marchable target on `build_realm(0)` with `p_npc_033`, `off_spymaster`, `r_valoria`/`set_s_002` control (:100-140).
  - Predicate answer asserted a bare `False`/`True`, because a `Verdict` with observed reads would deposit claims and move the hash (:9-13 docstring). It asserts `ok is True`, so a `Verdict` return would red it.
  - Records its mutation run in the docstring (:15-18): deletion of `_refuse(...)` reds the ownership test.
- **Conflicts / stale:** clause strings are asserted verbatim, so a wording edit reds it (brittle, not wrong). Hard-codes `p_npc_033`, `r_valoria`, `set_s_002` of the seeded realm: a realm re-roll that renames them breaks the march test [UNVERIFIED].
- **Open items:** none.

### engine/season/tests/test_rem30_character_sheet.py
- **What it is:** pytest file, v10 REM-30 (IN-47): the character sheet's three spaces (`decision/sheet.py`): creation, development, chronicle.
- **Status:** no Status line. Reading: live; the hash pins are a re-pin log.
- **Bears on:** CHAR (sheet/creation/development), CORE (hash goldens), GO (play surface `dispatching_chooser`).
- **Content that matters:**
  - `PRE_BUILD` pins `build_realm(s).content_hash()` at 1 season, seeds 0-2: `256606154c30542f9456b2fe15c76f09` / `aa58ef0b71c947ce5ff9f0a75ffd8ca6` / `a21ab6e12e356ccc4261bec1c93ca3b4` (:70-74), under `revert_cr79` for seed (:98-101). Re-pin log runs :32-69 with a control named for each of ~10 entries. This is one of the six files holding the `25660615…` trajectory: F-TEST-02. Seeds 1/2 equal the addendum's shipped hashes (its probe-12 list), seed 0 is the reverted-cr79 figure, not the shipped `5ab73af2…`.
  - Control: the creation arm off (`seat(rows, None, …)`) reproduces the pre-build hash; the arm on with `take_ranked` equals the automated chooser (equal hash) and asserts the space was called with candidates, `max(seen) >= 1` (:111-121). Falsifier: a reversed pick moves the hash with `assert max(seen) >= 2` (:124-130).
  - Refusals: creation seats only a builder-seated person; the sheet row is a read-only copy; a pick outside the formed set raises `Forbidden` (:133-150).
  - Chronicling writes nothing: hash equal after reading every chronicle between seasons, with `assert any(c.ledger …)` to prove it observed (:153-159).
  - Chronicle splits `scar` by roster and by holding (held vs unheld affiliation), `beliefs` is one claim per subject (:162-178).
  - "THE WRITE FALSIFIER is not here": points to `test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` (:15-16).
- **Conflicts / stale:** Pins one seed-0 hash that exists only with `revert_cr79` applied, so the seed-0 literal pins a world nobody plays (F-TEST-02, 20 of 28). The docstring says "seed 0 fights nothing" etc. in the log; those statements are hash-log claims [UNVERIFIED]. Comment at :32 says "The parent tree's realm hash"; the figure is the CR-79-reverted one.
- **Open items:** `person_id=None` creation arm is "the shipped state" (:5): the player-creation arm is not enabled in play.

### engine/season/tests/test_rem31_grid_suspension.py
- **What it is:** pytest file, v10 REM-31 (IN-46): the grid mode's suspension at ENCOUNTER, three-arm falsifier on `build_realm(0)`, one season.
- **Status:** no Status line; the design `proposals/2026-10-07-grid-mode-suspension.md` is cited as "PROPOSED, held back". Reading: live (but world-reverted).
- **Bears on:** PC (fight at ENCOUNTER, decider), CORE (host/PlayHost, determinism), GO (playable host).
- **Content that matters:**
  - Autouse fixture reverts CR-87, CR-85 and CP-T03-04 so a fight reaches ENCOUNTER on `build_realm(0)`: on the shipped tree "no `fight` formed … every arm vacuous" (:46-60). So the whole file runs on a world the shipped game does not play (F-TEST-02 shape; the addendum names `revert_cr87` in F-TEST-12).
  - Three arms: automated; PLAYABLE with a scripted equal chooser and a decider engaging every turn; PLAYABLE withdrawing after turn 1. Asserts `hash(1)==hash(2)`, equal mint counts, `hash(3)!=hash(1)` (:175-211).
  - Non-vacuity guards: `assert calls` ("no fight reached the engine at ENCOUNTER"), `max turn >= 2`, and `len(census claimants) > len(rec claimants)` so the automated branch of the party test is exercised (:149-186).
  - Two mutations that must be seen: a decider that consumes a draw reds the hash, one that mints a token reds the count (:214-218). Draw and mint stand still across a suspension (:191-204).
  - Permutation falsifier: `deliberation_order` shuffled, PLAYABLE on and off (control), and a callback writing shared state reds the permutation (:221-247). Decider answer outside the closed set raises `ValueError` (:250-255).
  - Monkeypatches module attributes `driver_mod.mint_token` and `deliberate_mod.deliberation_order` (restored in `finally`) and caches arms with `lru_cache`.
- **Conflicts / stale:** Imports `revert_*` helpers from three other test files (coupling across files). The `lru_cache` shares state between tests. No hash literal, so it does not need re-pinning; it breaks when a later item changes which fights form.
- **Open items:** The suspension is proved on the CR-87/85-reverted world only; on the shipped world no fight reaches ENCOUNTER in one season (own docstring :48-52), so the suspension is not observed at the shipped configuration (bears on F-TEST-01 / R-04 integration of the playable host).

### engine/season/tests/test_rem32_scale.py
- **What it is:** pytest file, REM-32 (B10-10 Phase 1 close): `troops_per_weight` scale in `modules/mass_battle/massbattle.py::resolve_field`.
- **Status:** no Status line. Reading: live.
- **Bears on:** MB (field sizing), CORE (seam).
- **Content that matters:**
  - Headcount sides are sized `weight * troops_per_weight`: (15,6) x3 -> (45,18); x1 is the identity (:48-53).
  - Fed troops (`troops_a`) are scaled after the provisioning bound: `troops_a=4.0` -> 12; `troops_a=0.0` -> crash floor 1.0 (:55-60).
  - A side with an order of battle and the headcount side facing it are NOT scaled; the facing side is `under_arms_cap(weight)` (:63-81). Spy replaces `_weighted_unit` to raise and `_oob_unit` to record `("A", False, 15.0), ("B", True, 6.0)`.
  - The battle itself is stubbed (`_run_and_grade`, `river_crossed`, `terrain_row_for_territory` monkeypatched): "nothing is resolved" (:7-8). Loads `modules.mass_battle` by `importlib` to satisfy the engine-names-no-module test (:17-24).
- **Conflicts / stale:** Tests private names of the module (`_weighted_unit`, `_oob_unit`, `_run_and_grade`): a refactor reds it without a behaviour change (white-box). Assertions are exact `==` on floats built by multiplying; fine for exactness, no `approx`. States a design decision "D5 of the Phase 1 close: the knob reaches only fields where NEITHER side holds an order of battle" (:65-66), i.e. the scale is silently inert for armied fields [UNVERIFIED against `massbattle.py`].
- **Open items:** the knob's inert case (armied field) is a pinned limitation, not a game decision; MB lane should decide whether that is intended.

### engine/season/tests/test_sc01_fired_slot.py
- **What it is:** pytest file, v9 SC-01 fired-slot step (2026-10-16): `convene` gives the Date a holder, `open_case` fills a fired slot, judges are asked about docketed matters.
- **Status:** no Status line; "No test here asserts execution in the seed-0 realm (v9 §0.5's relaxed exit)" (:35). Reading: live.
- **Bears on:** SC (proceedings, docket, bench), FA (convene/seat), CORE (CALENDAR step, write gate).
- **Content that matters:**
  - A convened date is held by the convener's seat; a vacant date (`holder=None`) fires and lapses with `date.fired` but no `docket.formed` (:95-109). Control inside the same test.
  - `open_case` with no open slot holding the matter still appends the dateless item, including a sibling settlement `S2` whose slot does not hold the venue (:116-134); with a slot it fills the nearest and appends nothing (:137-151).
  - A bench question names exactly the docketed matters of a sitting its judge heard fire: 5 controls (empty slot, dateless item, off-bench King, off-bench `p_low` given the claim so only `judging_set` excludes him, judge who never heard the firing) (:158-195). `q.source == "claim_landed"`, `q.about == heard.id`.
  - `matter` that is a rung fills no slot and raises no bench question (:198-214); each sitting cites its own firing's claim (:217-235); a slot refilled in one RESOLVE is asked under a new question id (:238-251).
  - W26 proof: convene, fire, witness, open_case, `determine` with causes walking back to `date.fired`; same seeded run twice gives equal `content_hash()` (:258-295). Only a self-consistency hash, no literal.
  - Matrix-cell test: `DocketItem.arrangement` and `.petition` writes are declared by `open_case`/`carry`, admitted at RESOLVE and refused at CALENDAR (:302-322). A docket item dated by a rung is no sitting; includes `checked >= 3` (:325-339).
- **Conflicts / stale:** Imports its whole world from `test_u7_remit` (`_world`, `_fold`, ...), so it is coupled to that fixture. The `determine` is "contested, so the bench is a strong judge `JUDGE`" (:161-162): a deterministic-looking `determine` needs a strong judge to open, an interaction to flag against the standing no-deterministic rule (SC lane) [UNVERIFIED]. Cites `workplans/valoria_master_workplan_v9_part6.md` (may be retired) and `architecture/PLAN.md` W26 (intent only).
- **Open items:** SC-01's relaxed exit: no test of the fired-slot path in the played realm (consistent with F-TEST-01).
