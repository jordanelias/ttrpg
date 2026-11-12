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

### engine/season/tests/test_sc01_obstacle_ceiling.py
- **What it is:** pytest file, v9 SC-01 step 14 (2026-10-16) with CP-T01-03/04/06 re-measures: the social contest's obstacle CEILING (`H-213`) and the per-pool `chance_floor` arm.
- **Status:** no Status line. Reading: live; the shipped arm is `ceiling_per_pool True`.
- **Bears on:** SC (obstacle composition), DICE (`band_odds`, M-7), CORE (fixtures, seam).
- **Content that matters:**
  - Owner is `modules/social_contest/roll.py::obstacle` (opposition halved, `obstacle_default` stand-in, bounded by the ceiling); the host builder `seam/wrappers/sigma.py::contest_input` composes nothing; `SocialContestInput` has no `ob` field (:4-12, :200-218).
  - M-7: at the 1D floor against Ob 4..11 the chance of a non-Failure band must not be below `EFFECTIVELY_ZERO = 0.001`; the instrument is `1 - band_odds(1, ob)[0]`, checked against an EXACT forced-face count of the ten d10 faces through the real entry (`_Face` rng) at `abs < 1e-12` (:106-127). Control: with `None` ceiling M-7 FAILS, asserted (:141-144) -- the test can observe its own failure.
  - Sweep `[1,2,3]` from register row `H-213` straddles M-7 (`not all(verdict.values())`, :187); the shipped arm is 2 (chance 0.1, 1 of 10 faces); arm 3 reads 0.0 (:25-39).
  - Per-pool arm (CP-T01-06): composed Ob capped at the highest Ob keeping 10 % Partial-or-better; enumeration over pools {0,0.5,1..8} x Ob 0..20 in quarters with count asserts (:314-345); the inversion detector returns 0 on the solved cap and `>= 300` on the rejected `2*pool` cap (:348-353): a planted control on the detector.
  - `test_the_cap_is_the_floor_met_exactly...` uses `pytest.approx(CHANCE_FLOOR, abs=1e-9)` (:362) on a numerically solved cap, paired with `cap+0.05 < floor-1e-6`; also pins literals `2.842 / 3.6 / 4.23` (:364). The addendum names this file as flagged-and-read; not an exactness-on-approx failure but pinned figures.
  - Seam injection tests on `tiny_world`: ob 2.0/3.0/1.5/2.0 for four (ceiling, subject) pairs with capability set to `copying: 10` and `3` as roster-exempt fixtures (:221-242); 300-seed band-distribution test requires `differ > 0 and hits[2] > hits[3]` (:245-256).
- **Conflicts / stale:** Cites `workplans/valoria_master_workplan_v9_part6.md`, `proposals/2026-09-05-proceedings-subsystem/19_PLAN.md`, `21_RECONCILIATION.md` (some may be retired; [UNVERIFIED]). The docstring's CP-T01-03 `p_success` figures are history. `H-213` sweep value `3` is a declared arm that fails M-7 by design. Obstacle is hard-capped (a rule on difficulty), not an outcome, so it does not conflict with the no-deterministic rule.
- **Open items:** the fixed-arm 1/2/3 sweep is read on the FIXED arm only (`_arm` sets `ceiling_per_pool False`, :223), while the shipped arm is per-pool: the sweep is therefore read at a non-shipped arm (one of the addendum's "two cases at a non-shipped arm" shape).

### engine/season/tests/test_sc01_provider.py
- **What it is:** pytest file, v9 SC-01 steps 13+15 (2026-10-16): the social contest scene's `contest` provider and three prize rows repointed to it.
- **Status:** no Status line. Reading: live.
- **Bears on:** SC (provider), CORE (manifest/registrar, composition rows, seam), DICE (`Margin`).
- **Content that matters:**
  - Rows `a standing`, `a proposition`, `a matter` (three, not the plan's two) name `provider: social_contest`, `module_entry: social_contest.roll` (:86-91); no `sigma_leverage` provider stays registered (:98-103).
  - The half-state: rows repointed with no provider registered refuse at `SeasonDriver` construction naming the first prize; a misspelled `provider:` and a deleted composition row each refuse naming the row; the control constructs first (:106-127). Good non-vacuous refusals.
  - The module entry returns a `Margin` with fields exactly `{net, ob}` and nothing naming a winner; an entry returning the kernel's winner shape or a dict with `winner` is refused at the host boundary, with the shipped entry as control on the same world (:141-163). Matches the rule that a registered module returns a margin, not a verdict.
  - C-8: a contested `speak` by the speaker dispatches at `Hh`, by the Duke at `S`, never the `"R"` placeholder; the Event degree equals `ladder.degree_of(provider out)` (:170-186). A `tell` resolves through it likewise (:189-204). Wraps the real provider via `monkeypatch.setitem(PROVIDERS, ...)`.
  - "The automated mode stays the sigma-leverage roll: SC-05's measurement ... keeps it over the kernel" (:13-14): the contest kernel is off-loop (cf. `05_SC_sc05_kernel_retirement.md`).
- **Conflicts / stale:** Docstring says the arrangement-id scan "MOVED at step 16" to `test_sc01_the_bar.py` (verified, the scan is there at :380-398). Imports `_docket` from `test_sc01_speak` and `_fold`, `_world` from `test_u7_remit` (cross-file fixture chain). Names `30`/`08_SEAM.md` as intent-only refs.
- **Open items:** none; "No test here asserts execution in the seed-0 realm" (:32).

### engine/season/tests/test_sc01_speak.py
- **What it is:** pytest file, v9 SC-01 step 12 (2026-10-16): `speak` as a typed contested cell, `contests: "a matter"`, four bands.
- **Status:** no Status line. Reading: live.
- **Bears on:** SC (speak, docket, bands), CORE (loader, refusal), DICE (ladder).
- **Content that matters:**
  - `speak` row shape: `contests == "a matter"`, requires an `Existence` of `subject` of kind `DocketItem`; `writes_by_degree`/`emits_by_degree` keyed by the four labels; four distinct emitted kinds; `row.writes == ()` and `"speak" not in EFFECTS` (:66-87). A `speak` has NO effect at any band: the speech is a deposit at WITNESS only, so a band changes no state (confirmed by :106-119: `not any(e.changes ...)` over 12 draws).
  - Undocketed `speak` is `speech.unheard` with `degree None`; after `open_case` the same act reaches the seam and draws a degree (:94-103).
  - All four bands occur over 4 pools x 24 act ids = 96 folds (`assert folded == 96`), and the literal map `Overwhelming->matter.carried, Success->matter.advanced, Partial->matter.held, Failure->matter.turned` is asserted so a swapped pair reds (:126-155).
  - Loader refuses a flat `writes:` on a contested cell, a band missing from `emits:`, and a misspelled prize; control = the shipped row loads (:162-176). `_plant` from `test_u7_remit`.
  - A speaker under one die (pool 0 / 0.5) is refused `speech.unheard`, not a crash; pool 1 resolves (:179-191). Seam: `PARTY-GAP`/`REFUSED` return a typed `ContestRefused`, any other non-RESOLVED status raises `Unspecified` (:194-216).
- **Conflicts / stale:** the four band kinds (`matter.carried / advanced / held / turned`) change no state, so a speech is outcome-labelling with no consequence: relevant to the no-deterministic-and-graded-consequence rule and to SC "evidence/argument has no effect on the bench" [UNVERIFIED which later files add the effect]. `speak` is mapped to the `copying` capability (:127-128): a SC verb keyed to an unrelated faculty name, a vocabulary smell for CHAR/SC.
- **Open items:** the row's `writes_note` says writes empty at every band; whether a speech should shift the determination's odds is left to later steps (not in this file).

### engine/season/tests/test_sc01_the_bar.py
- **What it is:** pytest file, v9 SC-01 step 16 "THE BAR" (M2's first gate) with a long re-trace log through v10/v11 (REM-25, CP-T05-04, CR-16, CR-10/28, CR-82, CR-17, REM-30).
- **Status:** no Status line; its own docstring says the bar "as the plan words it is UNMET" (:308-310). Reading: live, but the bar is held by one hand-selected seed.
- **Bears on:** SC (proceedings end to end), CORE (R-01 propagation, hash), CHAR (chooser from conviction), FA (convene/seat).
- **Content that matters:**
  - The bar: a seeded proceeding with ZERO authored acts (`_zero_authored`: every `w.acts` entry is an object the chooser returned), run twice byte-identical, with `causes[]` walking from `matter.determined` back to the `date.fired` that raised it (:248-300). A world-seed dependency: `PROCEEDINGS = (("stability", 35, 7),)` (:179) -- ONE proceeding where the plan wants two.
  - Rate measured by the file: 15 convictions x seeds 0..15, 10 seasons: 240 runs, 72 determinations, 4 walk (:25-26); at SC-03b 360 runs, ONE proceeding walks (:62-63); at CR-82 two in 7215; at CR-17 one in 7215, and nothing in 10800 runs at 6 seasons after REM-30 (:157-178). The proceeding exists only by selecting seed and season count after each unrelated change (re-traced at least 8 times). The docstring says it is "an existence claim, not a rate"; it is also a hash-independent but trajectory-dependent test. Falsifier F-TEST-02/-03 shape (counts re-roll on unrelated changes) without a hash literal.
  - Strong judge: `BAR_FIXTURES = DEFAULT_FIXTURES.sweep("pool_default", 30)` (:180), `H-126` declares `[1,2,4]`; 30 is off the sweep, GLOBAL (every contested verb without a `verb_capability` row falls to `pool_default`, so `speak`, `tell`, and graded inquiries saturate at Overwhelming) and "hides the draw stream from the twice-identical hash check" (:58-82). At the shipped judge (pool 2, obstacle 2) most determinations are `Failure`.
  - Mechanism for the low rate: a matter docketed BEFORE any sitting fires gets a dateless item, `docketed` then declines later `open_case`, no slot ever holds it, and `determine`'s docket conjunct admits a dateless item (:28-39); lifting this is recorded at `hole_register.yaml` H-163 as "a design choice this step does not take".
  - Falsifiers kept: an injected act reddens the bar (`open_case` and `speak`, with `assert injected and injected[0].id in w.acts`, :318-339); a CONTROL run (`stability, 8, 5`) where a determination follows a fired date but its `causes[]` reach no firing (:342-359). Others (different RNG, broken cause link) were run once and "are not re-run at 30" (:70-71).
  - Closure test (scripting drift): static AST scan of all `.py` in `engine/season/` (excluding tests) and `modules/` for comparisons against an `arrangements.yaml` id; floor `len(paths) >= 100`, effects module membership asserted, and a planted `if arrangement.id == "tribunal"` inserted into the real `_eff_determine` source is required to be found (:380-410). It does NOT see an id reached by `.get("<id>")`, a constant, or a dict (:386-388).
- **Conflicts / stale:** Pinned hash fragments inside comments (`213c3aca...` etc.) are history, not asserted (no hash literal is compared; the two-run equality is the only hash assertion). `len(set(hashes)) == len(PROCEEDINGS)` clause is trivial with one (:168). The comments cite `hole_register.yaml H-163`, `H-126`, `H-194`, `H-96` as registers. Test file's own claim that the bar is "UNMET" (2 wanted, 1 held) contradicts any reading of the file as "the proceeding gate passes". [ASSUMPTION; medium; Jordan to correct] markers are inside the test.
- **Open items:** the plan's two-proceeding bar is unmet at HEAD (revert: tau 0.1 restores two, :309-310); the dateless-item ordering that keeps the rate low (H-163) is an unmade design choice; no proceeding is asserted at shipped fixtures (pool_default 2).
