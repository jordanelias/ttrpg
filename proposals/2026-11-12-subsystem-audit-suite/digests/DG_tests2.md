# Digest tests2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: 54 files under `engine/season/tests/` (about 1.1 MB), read in assignment order. Finding ids `F-TEST-NN` are from `proposals/2026-11-12-subsystem-audit-suite/audits/01_CORE_audit_addendum_C_tests.md` (addendum C: it states ~120 season files were scanned by instrument only, so every file here is a reading it did not make, except `test_in22_shortfall_reach.py`, `test_march.py`, `test_in12_step9.py`, `test_interactions_log.py`, `test_loops_instrument.py`, `test_in62_decision_spread.py`, which it opened at flagged tests). R-01..R-09 as the addendum lists them: R-01 decisions propagate, R-02 decisions affect later decisions, R-03 seasons tick scene by scene, R-04 strategic/management acts, R-05 all verbs built out, R-06 robust characters, R-07 memory/feeling/attitude, R-08 not omniscient, R-09 probabilistic chains. "Falsifier present" below means the file runs the mechanism and also removes its cause (planted control / mutation / arm swept to zero) and asserts the difference.

Cross-file pattern noticed early: most files in this family carry a long docstring naming a plan position (`IN-nn`, `LB-n`, `REM-nn`, `CP-Txx`) and "MUTATION run" notes; the assertions are behavioural on hand-built `tiny_world` fixtures. Re-pin logs (revert-stack comments of the form "(a, b) -> (c, d), A RE-RECORD WITH THE UNIT THAT MOVED IT") live inside the tests.

### engine/season/tests/test_governance_build.py
- **What it is:** pytest file, 3,119 lines / 81 tests; the "covering test file" for the 2026-09 governance/settlements/decisions build programme (LB-n falsifier ids, plan positions 13d-i, 13e, 13f, 8a, 13d-iii, 24d-i, H2); split out of `test_season_shape.py` so a mid-session run is cheap (`:1-15`).
- **Status:** none (module docstring only). Reading: live; mixed. Some blocks are historical commentary kept in place (LB-1's long "HISTORY, SUPERSEDED" paragraph `:127-219`).
- **Bears on:** FA, SE, CORE, CHAR.
- **Content that matters:**
  - Offices as data: `offices.yaml` has 31 authored seats; conferral census pinned `{appointed 18, elected 8, inheritance 1, None 4}` and revocation census `{rung_above_same_faction 13, rung_above_in_holdings 2, None 16}` (`:1975-1991`); realm builds 34 offices (33 anchored, 1 unanchored `off_npc_084`) (`:2421-2430`); 8 minted seats incl. two Altonian (`:2459`). Counts are file-derived but literal (`== 31`, `== 34`, `== 33`).
  - Revocation rule test (LB-10c re-pointed): ten candidate revokers, exactly one admitted (the King on the rung directly above, same faction); a Crown duke two rungs above an empty parent is refused ("parent", not "nearest ancestor") (`:1662-1750`). The loop asserts `checked >= 10`. This is a deterministic eligibility check, not a resolution draw (consistent with the brief's carve-out for eligibility).
  - `establish` (13f): founding an office re-stamps sitting holders' `granted_acts` and emits `tenure.payload_set`; hand-mutating `Office.remit_acts` reaches nobody (snapshot not mirror) (`:1209-1247`); includes a mutation that runs the retired `_req_establish` through the full pipeline and shows an uncaught `NotYours` (`:1250-1316`). AST scan: no `Office.remit_acts` attribute read outside four allow-listed functions (`:1559-1604`).
  - Subsistence: a hearth with no larder draws from its settlement; cohort eats by `weight`; two eaters cannot spend one unit; a starving cohort's body falls and its `decision.budget` falls in the same season (read/write asymmetry test, §0.1 pt 1) (`:485-684`); `body_step = 0` arm is the control (`:714-741`); individuals (duke, king) are exempt from the draw (ED-IN-0255).
  - The beneficiary column: every verb declares a rostered beneficiary; `fight` benefits the actor not the victim (proves the column cannot be derived from `writes:`); one test runs a real `populated.run(seasons=1, seed=0)` with a spy and asserts `len(seen) > 1000` and `resolved > len(seen)//4` (`:1014-1072`). It admits its own `holes == []` assertion is structural, not measured (`:1051-1061`).
  - Pins: `len(VERB_TABLE) == 67` with a 25-line re-record log (`:883-913`); the dwelling test pins `(out["acts"], cout["acts"]) == (749, 747)` at one seed/one season under ~40 stacked re-record comments (`:2957`) - a trajectory count (F-TEST-02/03 family) - though the property assertions beside it (no dwelling question answered first; `deposited(w) > deposited(cw)`) stand independently.
- **Conflicts / stale:** the `heads`/dwelling test's comment still says "`11a`... 1632 questions" etc. - historical. `test_lb1_bo10_gate_closed_by_in11...` was weakened at v9 IN-45/§0.5 (execution assertions deleted; it now asserts only formation and that attempts name a Proposition) - so "`commit` executes in the realm" has no test here (`:197-203`). One docstring says `test_lb3c` uses `inspect.getsource(_eff_kill)` and asserts `"t.until = w.tick" not in body` - a source-text assertion beside a behaviour test (F-TEST-09 class, but the behaviour is also checked at `:769-774`).
- **Open items:** none stated. `test_h2_*` block (`:2971-3119`) is the deontological refusal gate (`refusal_axis` ships unset = no-op control, `:3021-3037`; refusal axis not live in the shipped game).

### engine/season/tests/test_h10_affiliations.py
- **What it is:** IN-08 H10 test file (affiliation roster, `incompatible` half-matrix, `Person.conviction`, derived `confliction(p)`); v9 era.
- **Status:** none. Reading: live.
- **Bears on:** CHAR, WR.
- **Content that matters:**
  - Plan's falsifier: each strained (`incompatible: true`) pair at full intensity gives `confliction == AFFILIATION_CEILING` (the `min` reading); `false`/`null` pairs, one affiliation alone, none at all give 0 (`:92-116`). Loop asserts `checked >= 1`; control asserts `pairs` non-empty.
  - Loader refusals: unrostered pair, self-pair, double-keyed pair, table with no `true`, non-bool value (`:62-80`); shipped half-matrix keys every unordered rostered pair exactly once (`:83-89`).
  - `(Person, conviction)` writable only at RESOLVE: WITNESS refused by law S9.3, MATTER by S3-L4 (`:130-148`).
  - World builder fill test plants every cast row's affiliations via `monkeypatch.setattr(cast, "row", ...)` so a non-empty fill cannot be the authored vector by accident (`:151-173`).
  - Exporter refusal for open/unbounded scale (`:176-194`).
- **Conflicts / stale:** none noticed. `confliction` is a deterministic function of holdings (a derived read, not a consequence draw).
- **Open items:** none.

### engine/season/tests/test_h11_affiliation_scar.py
- **What it is:** IN-08 H11: an observer takes one `Person.scar` count per held affiliation an observed act violates, via `rosters.yaml: tables.affiliation_engagement`.
- **Status:** none. Reading: live, but its subject is dormant in the shipped realm - the docstring says no verb with a negative cell lands through the fold today (`:6-8`), so every positive arm runs on a PLANTED table.
- **Bears on:** CHAR, WR, FI.
- **Content that matters:**
  - End-to-end falsifier over every `fan_out_mode`: no holdings -> no scar; holdings + shipped table (where `fight` has no cell) -> no scar; holdings + rebound table -> each observer scarred on exactly the violated holdings, the non-observer not, `conviction` unwritten (`:86-117`). Asserts `scars` non-empty so the arms are not vacuous (`:106`).
  - Per-affiliation cell scars only that holding (`:120-129`); a `Failure` band scars nobody, with a landed `fight` in the same world as the control (`:132-151`).
  - Loader refuses magnitudes (must be a sign), overlap between shared and per-affiliation cell, unrostered column/verb, None, and a name on both the affiliation and pursuit rosters (`:160-193`).
  - WITNESS cannot write the scar row (`:196-204`).
- **Conflicts / stale:** R-07 (feeling/attitude) bears: this is the affiliation-scar half; the addendum says feeling/attitude/relationship have "no test" (§3 R-07) - this tests a mechanism whose shipped table has no live negative cell, so on the shipped realm it observes nothing (the file says so).
- **Open items:** the shipped table's negative cells are absent for landing verbs, so the scar never fires in play; nothing here answers whether that is intended.

### engine/season/tests/test_h206_a_death_at_matter_is_witnessed.py
- **What it is:** H-206 regression file; `world_q.event_place` places an Event about a removed person where `remove_person` took him out, if on the same tick; plus H-129 chain.
- **Status:** none. Reading: live.
- **Bears on:** CORE, WR, FI.
- **Content that matters:**
  - Falsifier: a MATTER-written `person.died` for a seat-holder deposits claims on every person standing at his place and none elsewhere, each count asserted `>= 1` / `len(far) >= 1` in the direction needed (`:75-93`); the mutation (put `_OLD_PLACE` back) reddens the positive half (`:96-103`).
  - Control: a RESOLVE death by a killer deposits exactly what it did before the fix (ledgers equal with `event_place` reverted) (`:177-193`).
  - Narrowing: act-caused Events of the dead actor in the dying tick are not placed (`:124-134`); `place_of` of the dead stays None (`:106-121`).
  - H-129: a killer's later MATTER death chains to his own death (`[ROOT]`), not his victim's (`:196-212`).
- **Conflicts / stale:** `_killing_act_index` does `pytest.skip` when the combat engine is absent (`:161-162`) - an instance of F-TEST-11 (thirteen skips on an absent combat engine; addendum lists nine sites in `test_season_shape.py` plus four other files; this file is plausibly one of the four, `[UNVERIFIED]`). Also searches act ids 0..39 for one that kills, asserting one exists (`:178`).
- **Open items:** none.

### engine/season/tests/test_home_presence_index.py
- **What it is:** equivalence test for the barrier-cached HOME and PRESENCE indexes against the scans they replaced (the IN-54 pattern); performance item (a season 15.0 s -> 6.5 s, same content hash).
- **Status:** none. Reading: live.
- **Bears on:** CORE.
- **Content that matters:**
  - Index equals `home_of(w)` on `build_realm(0)` including a person with two live `contain` edges (last wins), `place_of(w,x,homes)==place_of(w,x)` for every id kind; asserts `checked >= 100` and that some place is non-None (`:36-52`).
  - `presence_map == {r: presence(w, r)}` rung for rung; `populated >= 5` guard (`:55-63`).
  - Cache is a per-barrier cache: stale until `discard_caches()` (`:66-75`); trace stream unchanged: one `home_of` row per `place_of`, one `presence` row per rung (`:78-91`).
- **Conflicts / stale:** the docstring quotes a one-season pin hash `056584ed...`, long superseded (not asserted here). 
- **Open items:** none.

### engine/season/tests/test_hunger.py
- **What it is:** REM-50 tests of `world_q.hunger(w, S)` - a settlement's hunger as a derived Query and its line in `census` (bands `fed/lean/hungry/starving`, floors `(1, 2)`).
- **Status:** none. Reading: live as an instrument, but the docstring says `hunger` has NO caller in the loop (REM-51 cut): only `census` reads it, "so a wrong band moves nothing in play" (`:16-18`).
- **Bears on:** SE, WR.
- **Content that matters:**
  - Cover is an exact `Fraction` of stores/need; raising a cohort's weight monotonically raises D, lowers cover, moves band toward `starving`; `starving` is exactly `unmet > 0` (`:58-78`). Expectations recomputed from `DEFAULT_FIXTURES.subsistence_weight`, not copied.
  - Mutation named: compute D from `population` instead of `demanded` -> test (c) red (`:98-109`).
  - Stated limits read as they are: stores above the settlement feed but are not counted in A; stores beneath on an un-walked rung are counted though never drawn; non-eaten kinds are not cover; A and D sum unlike kinds so a surplus of one masks a shortage of another (`:171-197`) - i.e. a known imprecision pinned, not fixed.
  - Sweep row `H-242` arms `(), (1,2), (2,4)` read from the register; malformed floors refuse (`:137-153`).
  - Realm test: every populated settlement is `starving` before the first yield (asserts `checked >= 30`) (`:211-223`).
- **Conflicts / stale:** `test_g` pins the A/D unlike-kinds masking as correct behaviour. `hunger` is a read with no consumer in play, so R-03/R-04 do not touch it.
- **Open items:** REM-51 (a loop caller for hunger) is "cut" per the docstring; nothing here says what replaces it.

### engine/season/tests/test_in08_cells.py
- **What it is:** IN-08 cells commit (B-G) tests: the alignment table density rule (every verb celled on every pursuit axis or declared `uncelled:`), retired `faith`/`warden` pursuit tokens, `challenge`/`accept` rows, and the H7 doctrine-pair cosine instrument.
- **Status:** none. Reading: live; the last block is explicitly "RECORDED, NOT GATED" (`:144-239`).
- **Bears on:** CHAR, DICE, PC.
- **Content that matters:**
  - Shipped alignment table is dense: celled keys and `uncelled` partition `VERB_TABLE` exactly (`:39-51`); planted copies refuse a missing cell, an uncelled verb that carries a cell, an unrostered axis/verb (`:54-90`).
  - No `faith`/`warden` pursuit anywhere in roster, projection rows, templates or NPC `conviction:` text; `checked >= 40` weighted entries (`:102-118`).
  - `accept` carries `fight`'s degree-keyed writes and emits except `duel.yielded` in `Wounded`; no `kill`/`wound` verb row (`:121-141`).
  - Doctrine pair cosine: computed through `to_axes` on the shipped table, goes red only when the instrument cannot compute; the planted-table test proves it can fail (zeroed row, absent row), and `test_a_moved_doctrine_cosine_does_not_turn_the_pair_test_red` proves a moved value stays green (`:185-238`). The `approx` use at `:238` is a `!=` (inequality), not an exactness claim.
- **Conflicts / stale:** cites a "retired pursuit-cells draft (its FORK: row)" - retired reference. The recorded +0.229 cosine lives in `rosters.yaml` note / R-06 `measured:`; the test deliberately does not pin it (a design decision: RS-3 `doctrine` row PROVISIONAL).
- **Open items:** the doctrine row's cell values are "judged in the CELL-VALUE AND COSINE PASS" (`:13-14`) - nothing gates it, so a moved cosine is invisible to CI by design.

### engine/season/tests/test_in09_dispensation_answer.py
- **What it is:** v9 IN-09 / v10 REM-2B: `comply`, `evade / defy`, `construe` - the three acts answering a dispensation (a held writ), formed only on a writ the person holds and whose terms his ledger names.
- **Status:** none. Reading: live (restored at v10 REM-2B after a v9 revert; the docstring records H-203).
- **Bears on:** FA, SC, CHAR.
- **Content that matters:**
  - The three rows are typed, resolvable, emission-only (`writes == ()`, not in `EFFECTS`), carry `referent_class: Record`, `referent_named: True` (`:108-117`); the loader refuses a Record row naming no Record `existence` kind (planted on each of three, shipped rows as control) (`:154-171`).
  - Carried falsifier through the real fold: no claim of the terms -> `compliance.impossible` / `construal.impossible`; with the claim -> `compliance.given` / `compliance.withheld` / `terms.distorted` (`:176-185`). These are deterministic admit/refuse; the outcome of `comply`/`evade` is emission-only - **no draw decides whether a writ binds** (relevant to the brief's "a decree binds" known case).
  - Formation: `writs_held` stamps only a held dispensation the person is the addressee of; a witness or a non-addressee custodian is offered none of the three, each with a control that flips a set (`RECORD_REFERENT_KINDS`, `HOLDING_RECORD_KINDS`) to show the assertion could fail (`:238-279`).
  - Crowd-out control: rows declaring no `referent_class` form exactly what they form with classed referents stripped; `checked >= 3 * len(w.persons)` (`:298-328`).
  - The test at `:120-151` pins `record_rows == {comply, evade/defy, construe, carry, found, build, research, accept}` and `RECORD_REFERENT_KINDS == {dispensation, challenge}` under an ~30-line re-record log.
- **Conflicts / stale:** realm falsifier "(7) RETIRED 2026-10-13 ... No test asserts that a verb executed in the seed-0 realm" (`:30-33`) - so whether `comply` ever executes in computed play is untested here (consistent with F-TEST-01).
- **Open items:** none.

### engine/season/tests/test_in10_record_operands.py
- **What it is:** IN-10 (#453 §10.1) tests of the held-record operand channel (`rosters.yaml: record_sourced_operands`): a held dispensation's `terms`/`to` answer `subject`/`to`; `issue` fans over known persons; a held commission forms a `confer`; H-71 leak.
- **Status:** none. Reading: live. Its helpers (`_hold_document`, `_formed`, `_acts`, `_resolve`) are imported by about ten later test files (in12_*, in09?), making it a shared fixture owner.
- **Bears on:** FA, CHAR, SC, CORE.
- **Content that matters:**
  - Explicit stance: "NO TEST HERE ASSERTS THAT ANY VERB EXECUTED IN THE SEED-0 REALM" (v9 §0.5, 2026-10-13) (`:7-9`) - the channel is a property on hand-built worlds (this is the origin of the F-TEST-01 gap, deliberately ruled).
  - Disclosed gap: the `held=` SUBJECT branch of `_derive_operand` "is exercised only by direct calls" - in production `operand_bags` skips any Record whose own answer differs, so the hook "is kept, not observed in play" (`:34-37`).
  - Every claim paired with a named mutation and a control (e.g. `pack_scenes` minting `via=None` reddens blocks 3/4/5; `issue` without `via` is `issue.unauthorized`, `:238-241`).
  - A commission held by `p_king` forms `confer` of a seat on a person he knows only through the document; a commission about another seat adds nothing (`:276-296`); `confer` onto a held office displaces the incumbent and leaks no claim about the outgoing tenure id, with a non-vacuity control (`:337-364`).
  - `held_record_claims` picks by `LedgerReader._best`'s comparator (most recent, then most confident) not a second ladder; anti-vacuity `assert sure.when == unsure.when` (`:179-192`).
- **Conflicts / stale:** the `issue`/`confer` outcomes are admit/refuse (eligibility), with no draw: "a decree binds" in the brief's list of deterministic cases is not tested as a draw anywhere here.
- **Open items:** none.

### engine/season/tests/test_in10a_oblige_formable.py
- **What it is:** IN-10(a): `oblige` formable on a seat the person has been told of (`world_q.seats_named`), via `referent_class: Office` + `referent_named: true` (H-203, DECISION 2026-10-13, marked `[ASSUMPTION; medium; Jordan to correct]`).
- **Status:** none. Reading: live.
- **Bears on:** FA, CHAR.
- **Content that matters:**
  - `seats_named` reads deposits about the seat and the `terms` of a held document, not its addressee (`:64-77`); questions carry the named seat as an `Office` class and are unchanged otherwise (`:82-93`).
  - A formed `oblige` folds to `duty.taken` and `establishment_of` reads it; the duke told of his own seat forms it and the fold refuses it (`duty.refused`) (`:98-139`).
  - `test_in10a_the_declarations_as_built` pins `{v: referent_named} == {oblige, comply, evade / defy, construe, accept}` with re-record comments (`:154-164`).
  - Crowd-out control with every person told of every seat; `checked >= 3` (`:167-188`).
  - Realm falsifier explicitly retired as circular (`:17-20`).
- **Conflicts / stale:** none.
- **Open items:** the H-203 decision is flagged `[ASSUMPTION; Jordan to correct]` in the docstring.

### engine/season/tests/test_in10b_termed_seat.py
- **What it is:** IN-10(b): `confer` + `Tenure.term` - a termed seat-hold matures at MATTER under gate basis `T-n`, leaving the seat vacant.
- **Status:** none. Reading: live.
- **Bears on:** FA, CORE.
- **Content that matters:**
  - `confer`'s `writes == ("Tenure.until", "Tenure.since", "Tenure.term")` (`:44-45`); declared term rides as `Term(tick+n, act)`; malformed (0, -1, "2", 1.5, True) raises `InstrumentDefect` (`:48-55`).
  - Through the real `SeasonDriver.season`: a termed conferral matures, closure cites the act that wound it, seat vacant; the untermed control still holds after the same seasons (`:83-95`).
  - Term length is "the payload's `term`, a length in seasons" `[ASSUMPTION; medium]`; a computed `confer` declares none, so computed play never mints a termed seat (`:6-8`).
- **Conflicts / stale:** none. Bears on the brief's `succession` note: term expiry is a fixed tick maturity, not a draw (arithmetic by definition, arguably in carve-out).
- **Open items:** none.

### engine/season/tests/test_in12_arrest.py
- **What it is:** IN-12 steps 5/5a: `arrest` and `pardon`, the loader's closer clause, K-02 party-gap fold edit, and the charge.
- **Status:** none. Reading: live.
- **Bears on:** FA, SC, FI, CORE.
- **Content that matters:**
  - Closer clause: loading is red without `pardon` declaring `[detain, ban]`, and red on a domain naming a kind needing no closer, with the shipped table as control (`_loads` mutates a yaml copy and captures `SystemExit`) (`:177-185`).
  - K-02: party-gap under pool 0 emits `arrest.refused` (counterparty kind), never the union; pool 30 resolves to a band as the control (`:205-225`).
  - `arrest` is contested (`contests == "a standing"`): the observable test uses `pool_default=30` and asserts only `degree in OPENS` (`Overwhelming/Success/Partial`) (`:236`); a second arrest is folded at a PINNED band via `R._fold(... Resolution(band, {}))` so the write-clause decline is observed instead of a lost roll (`:95-101`). So `arrest.made` at tests' pool is not forced to a single band; the draw is seeded and the band set is asserted, not a probability.
  - Custody opens on the ISSUING seat (not the arresting watch); the issue-only-seat (`off_notary`, no `determine`) warrant opens nothing, while the Duke's does (`:278-304`). `pardon` is not contested (`not p.contests`) and ends custody by seat bench with no draw (`:144, :252`).
  - Step 5a: the witness addressed by a held petition forms `commit` on the charge (H-227 closed); the old tripwire was re-pointed so it can redden (`:376-386`).
- **Conflicts / stale:** `test_in12_5a...` comment records REM-23 turning "first half gone by design" (commit forms only on Proposition-classed referents). Deterministic: `pardon` ends a restraint with no resolution roll (brief's "binds with no resolution roll" class) - noted for FA/SC.
- **Open items:** realm execution of `arrest`/`pardon` is not pinned (v9 §0.5); the docstring for interrogate says no live `detain` exists in the realm, so the row is never attempted there.

### engine/season/tests/test_in12_conceal.py
- **What it is:** IN-12 step 10: `conceal` mints a `cover` Record whose `terms` is the actor; while held and a stage unmatured, `anchor_of` answers the cover id for his acts.
- **Status:** none. Reading: live.
- **Bears on:** FI, WR, CHAR, SC (identity and attribution).
- **Content that matters:**
  - Falsifier (#453 §10.4 step 10 verbatim): after conceal + `convene`, the Event anchors on the cover id, the far King's `told_by` chronicle claim names the alias and not the Duke, while a stranger present holds `seen` whose `who` is the Duke (`:172-182`); control without cover anchors on the Duke; in-test mutation (`live_cover -> None`) reddens it (`:185-201`).
  - `_ch_witness_key` changes with it: a knot-partner stops witnessing by key while the cover is live (`:208-222`).
  - Cover lapses when MATTER ripens every stage; a logged covered Event keeps its alias after lapse (`World._covers_logged`) (`:235-265`); a cover about another or not held hides nobody (`:268-277`).
  - Person-side decline (`held_document_declines`): after holding a cover he forms no second `conceal` (`:293-299`).
  - B-Q batch-close alias reads: CENSUS raises nothing for a dead covered actor's demand; a covered move's deposit names the alias; `travel.ended` chains to his move (`:312-346`).
- **Conflicts / stale:** the cover's staged ripening is a fixed-tick lapse. Concealment is entirely deterministic (a cover always hides; no draw to be seen through). Relevant to the brief's FI/noir intent (an alias that is never pierced except by presence).
- **Open items:** none.

### engine/season/tests/test_in12_covenant.py
- **What it is:** IN-12 step 7: `covenant` mints a dispensation whose `terms` is an uttered Proposition, handed on by `give`; the addressee accepts by his own `commit` FORMED FROM THE HELD DISPENSATION.
- **Status:** none. Reading: live.
- **Bears on:** FA, SC, CHAR.
- **Content that matters:**
  - Row: `remit:issue` only (an `own` alternative "would let anyone mint a treaty", K-14), counterparty `to` (`:92-105`); mint holds only the maker (K-54) (`:112-124`); controls: subject not a Proposition, covenant with oneself, no seat exercised each `covenant.refused` (`:127-147`).
  - Falsifier utter -> covenant -> give -> WITNESS -> addressee's `questions_for` -> `opening_set` -> `pack_scenes` -> fold -> `commitment.made` with a live `commit` edge; control: no commit formed before the give (`:165-188`).
  - Mutation in test: `TERMS_SOURCED` emptied reddens; `world_q.propositions_heard` stubbed to `()` in both arms because CR-28 made a second route to the same `commit` (`:195-206`).
  - Loader refuses a `terms_sourced` line naming a kind no held writ is stamped as; shipped line `commit: [dispensation, petition]` (`:209-224`).
- **Conflicts / stale:** the covenant binds nothing by draw: acceptance is the addressee's own `commit` (a deliberate choice, so it is a choice not a bound outcome). Whether the covenant's terms then compel anything is not tested.
- **Open items:** none.

### engine/season/tests/test_in12_forgive.py
- **What it is:** IN-12 step 13: `forgive` removes a person's own negative stance rows against a referent (K-41/K-49), closer of the grudge `march` plants on every loser of a lost field.
- **Status:** none. Reading: live.
- **Bears on:** CHAR, MB, WR (feeling/attitude).
- **Content that matters:**
  - Falsifier: after a lost field, `stance_toward(p, WINNER) == -1.0 * grudge`, a `forgive` leaves 0, logs `stance.moved` citing the forgive act, leaves the morale row and others' rows (`:155-172`); every row against the referent ends (a mutation that ends only the first reddens) (`:205-215`).
  - Refused where nothing is held: second forgive, referent held only positive, referent in no row (`:179-190`).
  - Person-side decline `own_stance_declines`: forms `forgive` only on a referent he holds a row against (`:228-234`).
  - Realm counter `field_planted_forgivenesses` is proven non-vacuous (1 for field grudge, 0 for a seeded row), and its docstring records a hand reading that on the realm the count is 0 ("the realm fights no field, H-149 / H-175") (`:9-13, :248-261`).
  - No fade: "nothing else ends a stance row" (#453 R-9(a)) (`:3-4`) - a grudge is permanent unless forgiven, relevant to R-07.
- **Conflicts / stale:** the grudge test sweeps `field_grudge_weight` to 3 to separate it from the morale weight (`:88`) - a test setting, not the shipped value. `forgive` is deterministic (no draw to forgive). 
- **Open items:** B-Q reading: only 1 `forgive` executed in two realm seasons, on a loyalty-seeded row, no field-planted one - i.e. the grudge/forgive loop is not exercised by computed realm play (docstring `:9-13`).

### engine/season/tests/test_in12_give_rung.py
- **What it is:** v9 IN-12 `give` widened to Rung (#453 §9.6): a rung `hold` changes hands by `give` (event `rung.ceded`).
- **Status:** none. Reading: live.
- **Bears on:** SE, FA.
- **Content that matters:**
  - Falsifier: receiver holds the rung, donor's edge closed at the cession, diff is exactly those two edges, one live holder (`:46-62`).
  - Refusals each one change from the control: giver does not hold, rung nobody holds, receiver not present, a seat is not ceded by `give` (`:65-99`); a Record still earns `record.given` (`:102-107`).
  - `own_hold_declines`: the loosened cell forms only on what a person holds, observed through `opening_set` (mutation named) (`:117-132`).
- **Conflicts / stale:** the cession is a gift: deterministic given eligibility; no draw. Fine as an act of voluntary transfer.
- **Open items:** none.

### engine/season/tests/test_in12_interrogate.py
- **What it is:** v10 IN-12 steps 5/5a remainder: `interrogate` (contested, `counterparty: subject`, `Detainee` class, one `confession.*` kind per band) and the charge.
- **Status:** none. Reading: live.
- **Bears on:** SC, FI, FA.
- **Content that matters:**
  - Row: contests "a proposition", four bands each with exactly one distinct emitted kind (`confession.made`/`withheld`...), `[]` writes at every band (`:94-106`) - so a confession is an Event only; no state consequence yet (relevant to the brief's SC interrogation intent).
  - Falsifier: Duke holds `determine`, clerk detained to it, docketed petition names him -> clerk stamped `Detainee`, Duke forms `interrogate`, the fold emits exactly one `confession.*` kind from ONE draw (`draws == 1` via a counting spy on `R.draw_factory`) (`:124-138`) - a real draw-count assertion.
  - Controls: free man never offered; unrefused hand-built act refused `interrogation.refused` with `draws == 0`; custody without charge refused with `draws == 0`; custody at another seat not offered (`:154-178`).
  - Planted failure: withdraw `counterparty` and the row leaves `resolvable_verbs()` (`:109-117`).
  - Step 5a witness-commit tests; `held_edge_declines` stops a second `commit` from the held petition (`:215-227`).
- **Conflicts / stale:** the realm reading in the docstring: `interrogation.refused` 0 because "the row is never attempted while no live `detain` exists" (`:7-8`).
- **Open items:** nothing consumes a confession (writes `[]`).

### engine/season/tests/test_in12_raze.py
- **What it is:** v9 IN-12 step 11: `raze` (a rung destroyed), licensed by OCCUPATION (the seat's faction `mustered` at a settlement another faction holds), on `build_realm(0)` with a real `march`.
- **Status:** none. Reading: live; H-228 limbs pinned "as it reads" (cascade leaves the razed town's population placeless and Sites with a dangling `rung` id), to redden when H-228 closes (`:10-13, :165-184`).
- **Bears on:** SE, MB, FA.
- **Content that matters:**
  - Entry falsifier: `w.rungs` shrinks by one and the Event names the town; a raze with no army present is `raze.refused` (`:57-79`); only the cascade (Layer 1) closes edges, each admitted under `T-m` for the razer's own `contain` else `cascade` (`:82-102`).
  - Declines each one change from admitted: a territory above, the razer's own town, an unheld place (`:105-141`).
  - Witnessing: razer's own `contain` closes in the razing write, so `event_place` is None and only the razer (`witness_key`) learns - the others in the town learn nothing (`:150-155`) - a measured legibility gap.
  - Single seed 0, one occupant army; the actor `p_npc_033` and town `set_s_016` are specific to the cast.
- **Conflicts / stale:** `raze` destroys a settlement with certainty: no contest, no draw (brief's "fight that kills with certainty" class). The population left placeless is an unresolved gap (H-228).
- **Open items:** H-228 (re-homing what stood in a razed town).

### engine/season/tests/test_in12_seize.py
- **What it is:** IN-12 step 6: `seize` (Record half) and the gate's eleventh basis `seizure`.
- **Status:** none. Reading: live (Rung half is IN-13's).
- **Bears on:** FA, CORE.
- **Content that matters:**
  - Row celled on all seven axes (not `uncelled`), `hierarchical_equal.seize < 0` the one non-null cell (`:101-115`).
  - Observable: a seizure over a held warrant moves the hold in one write; gate verdicts: close under `SEIZURE`, open under `T_M` (spy on `G.tenure_write_basis`) (`:122-147`). Controls: no warrant, warrant naming another Record, warrant held by a third person, record already the actor's (`:150-179`).
  - A seat cannot be seized (since IN-13 refused at `authority`; planted past the precondition at the gate: `NotYours`); the `seat is None` conjunct is an EQUIVALENT mutant, disclosed (`:33-35`).
  - Authority: no seat, seat without `issue`, purview that does not reach the holder each refused (`:253-301`).
- **Conflicts / stale:** `seize` is deterministic once admitted (no contest) - a confiscation always succeeds; no draw for resistance.
- **Open items:** none.

### engine/season/tests/test_in12_step9.py
- **What it is:** IN-12 step 9 tests: `sabotage`, `tend`, `argue`, `train`, `Person.capability` unretired, `work` delta restricted to >= 0; the file the addendum opened (cited by F-TEST list as read at flagged tests).
- **Status:** none. Reading: live.
- **Bears on:** SE, CHAR, SC, FI.
- **Content that matters:**
  - `sabotage` lowers `Site.condition` and `site.damaged` cites the act; a `restore` and a `sabotage` in one tick cancel and BOTH are refused after the fact (S27.3 one accumulator) (`:125-174`); `work` negative delta declined (K-09) (`:182-191`).
  - `tend` raises body to scale deterministically, whole body and absent patient refused (`:207-231`).
  - `argue` (contested, `a proposition`): a won band moves hearer's pursuits toward the arguer, lost nothing; `pursuit_shift 0` control; 40 act ids on fresh worlds with `checked == 40`; mutation `argued_pursuits -> None` makes won bands refuse (`:241-310`). Overwhelming moves twice Success (`:320-331`, `approx` at `:329` on a derived expression, not an exactness claim). This is a conditional-by-band loop (`for ... in won` / lost) but with `assert won` and `checked == 40` guards.
  - `train`: the vocation range is `VOCATIONS == set(VOCATION_ATTRIBUTE)`, `len == 4`; Carin forms one `train` Candidate per vocation (four incl. `arms`) with distinct act ids (`:420-482`). Formation never reads the actor's capability (a capability gate not built: #353 §9.2 probe P11) (`:387-396`).
  - `sigma.faculty` varies by person only through `capability` (Carin 4 vs `pool_default` others) and through `register_pool_addend` (`:351-384`) - R-06/R-09 second half has a mechanism here.
- **Conflicts / stale:** `tend`/`sabotage`/`train` are deterministic effects (a tend always heals fully; sabotage's fall `_fall` fixed) - brief's deterministic-outcome rule. The addendum's F-TEST list read this file for hash/approx flags only.
- **Open items:** J-13 (iii) "forms only where a case names a vocation" half NOT built (receipt names it).

### engine/season/tests/test_in18_obligee_report.py
- **What it is:** v10 IN-18 tests of `harness/obligee_report.py`, the M0e reader (G5's trigger: do obligees report to their seat-holder), on `tiny_world` with `off_duke` re-seated to `p_low`.
- **Status:** none. Reading: live; tests an instrument that "prints a figure and grades nothing (rule V2)" (`:3-4`).
- **Bears on:** FA, CORE (instrument), WR.
- **Content that matters:**
  - Falsifier: with the `oblige` edge the telling reads `m0e == 1`; the same world and telling without the edge reads 0 on every line while `tells_all == 1` (so 0 is the missing duty, not a missing telling) (`:63-79`).
  - Clauses each moved by one change: hearer not the holder, lost telling (`news.untold`, degree `Failure`) is an attempt not a report, refusal counted as attempt, edge not yet live at the telling tick (`:82-123`).
  - In-test mutations patch the reader's `_live_at` three ways (window, holder side, obligee side) and require `m0e` to drop to 0 (`:126-142`).
- **Conflicts / stale:** none. Subject is a measuring reader (process-load-bearing only, §0.1 pt 5) - it is the thing it tests.
- **Open items:** what a realm run reads is deliberately not asserted.

### engine/season/tests/test_in22_shortfall_reach.py
- **What it is:** v9 IN-22 carry-shortfall: a larder shortfall reaches governors whose seat purview contains the drained larder (`scarce.governed` world); plus the PAYING half (`transfer` out of the seat's treasury via `Act.via`) and the live `body_step` arm. The addendum opened this file as a flagged test (hash/approx) and found it sound.
- **Status:** none. Reading: live.
- **Bears on:** SE, FA, CHAR, CORE (R-01/R-02 propagation of a claim; R-04 management act).
- **Content that matters:**
  - Isolation precondition asserted: neither reeve stands at or holds the hungry town, both hold a seat with a rung, exactly one seat's purview contains the town (`:72-84`).
  - Falsifier both ways: inside-purview reeve holds every shortfall MATTER recorded at the recorded units with the seat channel's source (`inferred`); far reeve holds none; counted (`:87-102`). Arms that remove the cause: `observation_deposit_mode: none` and `fan_out_mode: presence_only` deposit nothing to the governor (`:141-151`); an actor's own reads stay the actor's (`:154-173`).
  - Paying half: the reeve's computed `transfer` EXECUTES `via` his seat out of the seat's rung (`terr_march`), not his home; matter conserved exactly against a twin with nobody acting (`moved == {MARCH: -amount, HUNGRY: amount}`) (`:209-233`). The chooser's `verbs=` is narrowed to `transfer` as an instrument choice, stated in the docstring; "which verb a person prefers is the chooser's score" so this is a chain test, not a play claim (`:181-194`).
  - Refraction: claim confidence is 100 at `refraction_gain` 0 and 50 at 0.5 (`:360-372`) - exact equality on small ints.
  - Live arm: `body_step` falls the cohort's body by `step * shortfall` exactly; at 67 the cohort dies in the barrier but the claim is still deposited; both branches asserted (`fell >= 1 and died >= 1`) (`:390-424`); shipped arm narrows the cohort's budget by exactly the bands crossed (read from floors, `:482-510`).
- **Conflicts / stale:** `[ASSUMPTION; medium; Jordan to correct]` that an `own` verb may be exercised through a seat (H-158's eligibility remedy) (`:27-28`). Assertions use a `_one_season()` that pins `steward_holds=False`, a planted configuration.
- **Open items:** H-160 limit (3) ruled "a balance number, not a blocker" (`:376`).

### engine/season/tests/test_in23_legitimacy_stability.py
- **What it is:** v9 IN-23: `person_q.legitimacy`, `stability`, `recent_claims` as Queries over one person's own stance and claims, no stored value (ruling R7); read only by `harness/storybar.py`.
- **Status:** none. Reading: live but the consumer is an instrument: "H-224: a chooser consumer was built and reverted" (`:5-7`). So legitimacy and stability influence no decision.
- **Bears on:** CHAR, FA, WR (R-07 attitude, R7 "a ruler can be wrong about their own standing").
- **Content that matters:**
  - Two ledgers read two estimates; twin ledger under another id reads identical (control) (`:63-83`); a ruler and a subject who saw his deed read his legitimacy differently (`:86-93`).
  - Window: age 0..2 counts at window 3, age 3 does not; windows 0, -1, True, 1.5, nan, None raise `ValueError` matching "H-224" (`:105-123`).
  - Writes nothing: snapshot (hash, log, writes, ledger sizes) unchanged, and a planted write in the read path MUST move the snapshot (`:137-166`). AST scan: no `World` attribute or dataclass field holds a legitimacy/stability value (`len(attrs) > 10` floor) (`:169-182`).
  - The instrument calls both Queries (spied) in a seeded capped season (`:187-199`).
- **Conflicts / stale:** `fx.get("estimate_window_seasons") == confidence_default // claim_decay_per_season` ties the window to claim decay (`:55-58`).
- **Open items:** no consumer in the decision layer, so legitimacy is observed but never acted on (R-07 attitude has no behavioural test here).

### engine/season/tests/test_in27_endings.py
- **What it is:** v9 IN-27 (END-VICTORY; H-176, GD-1): the ending vocabulary as a Query (`world_q.endings_reached`) over holds and seats that the season reports as `endings`; vocabulary in `rosters.yaml: endings`.
- **Status:** none. Reading: live.
- **Bears on:** CORE, FA, SE (end conditions; the brief's "stable continuation or ending").
- **Content that matters:**
  - Exit: the built realm's King releases the Crown and commits to the Church by two real `own` acts; `theocracy` is reached, antecedents `("in27_commit",)` and the `commitment.made` Event (`:78-97`).
  - Falsifier T-b: each condition planted by direct Tenure construction (no act) is TRUE (`_ending_edges` non-empty asserted first) and reports nothing; three arms including an Event caused by `[ROOT]` and a re-grant that merely names a seeded hold (`:224-262`). Redundant `commit` to a faction already held is not credited (`:201-217`).
  - Peninsular sovereignty (GD-1's sole victory row): reached by the last Crown-less territory holder's own `commit`; selected set excludes the foreign root `terr_T16` (`:145-171`).
  - Loader refuses 11 malformed rows naming them and a second victory row (`:326-350`); shipped roster has exactly one victory (`peninsular_sovereignty`).
  - Two seasons of the built realm call the step and report `endings == []` at hashes `BASE_HASHES[1]`, `[2]` - taken with `revert_cr79` applied, i.e. a reverted world (F-TEST-02) (`:357-385`).
- **Conflicts / stale:** the ending is a threshold-over-state reported by a Query; the requirement of an act among its antecedents is a bookkeeping filter, not a draw. In the shipped realm no ending is reached in two seasons; whether an ending is reachable by computed play is not asserted anywhere (the King's conversion is hand-folded).
- **Open items:** the end-condition/stakes legibility for "playable alone" is the Query only.

### engine/season/tests/test_in31_revocation_cost.py
- **What it is:** v9 IN-31 (H-100): what a revocation costs by the seat's provenance (`state/gate.py::REVOCATION_DISPOSAL`): `appointed` -> permanent `ban : him -> Act.via`; `elected`, `annex`, `None` -> nothing (Jordan 2026-10-21).
- **Status:** none. Reading: live.
- **Bears on:** FA, CORE.
- **Content that matters:**
  - One hand-built `revoke` per provenance through the fold: only `appointed` leaves a ban; outcomes differ across provenances (`:75-90`). Exit on the built realm with NPC-020 holding two duchies: Lord Steward (appointed) banned, Varfell (elected) and Hafenmark (None) not; without the placement the dukes are not revocable; with `REVOCATION_DISPOSAL["appointed"]` removed the outcomes collapse (`:290-304`).
  - A computed `revoke` executes 0 times (ORCH amendment, H-207 ruling (A)) - the exit is on hand-built acts (`:9-11`).
  - Mapping is total and names restraints (import-time check, `G.check_revocation_disposal`); unreadable provenance refuses (`:95-128`).
  - Gate enforces the mapping for a non-judging seat (a ban with no revocation, beside elected closure, on another seat, or a second ban each `NotYours`, store put back); a judging seat admits a ban by `determination` (pinned, "flip deliberately") (`:162-195`).
  - The ban bars seating (`confer.refused`) and service (`_req_oblige`) (`:200-212`).
- **Conflicts / stale:** the revocation cost is deterministic (appointed -> ban always).
- **Open items:** none; consequence of ban is limited to two readers.

### engine/season/tests/test_in33_exchange.py
- **What it is:** v9 IN-33 (H-58) restored at v10 REM-2B: `exchange` with two coined operands `return_kind`, `return_amount`.
- **Status:** none. Reading: live.
- **Bears on:** SE, FA.
- **Content that matters:**
  - Closed operand roster still binds: a cell naming an unlisted operand refuses at load (`:58-65`).
  - Fold on a hand-built world: both sides move, each kind conserved; refusals (kind nobody holds, kind for itself, rung with itself, either side short, a person-rung) move nothing (`:103-131`).
  - Formation reads `default_return_kind` and `default_transfer_amount` from fixtures; swept fixtures (timber/coin, 3) change operands so a literal equal to the shipped value would fail (`:155-180`). Crowd-out control: no other row's formation moves (`:183-198`).
  - Realm half deliberately absent: v9 built `exchange`, measured 0 executions through the chooser, reverted; REM-2B restored it without requiring one (P9) (`:17-21`).
- **Conflicts / stale:** exchange is a fixed-ratio, always-succeeds swap (no price/negotiation); the amounts are fixtures not valuations.
- **Open items:** whether `exchange` ever executes in computed play is unmeasured here.

### engine/season/tests/test_in34_bodies_clock.py
- **What it is:** v9 IN-34 FORCE-BODIES: ageing and illness via the bodies pass at MATTER (`Person.born`, `world_q.age_of`, `world_q.body_hazard = illness_rate + age_step*age` capped at 1, none for a cohort); one keyed draw per living person.
- **Status:** none. Reading: live but SHIPPED DARK - `age_step`, `illness_rate`, `age_at_build` all ship at 0 and "are Jordan's" (#457 D2 gate) (`:14-16, :104-108`). In the shipped game nobody ages or falls ill.
- **Bears on:** CHAR, WR, SE (death), CORE.
- **Content that matters:**
  - Control: at shipped rates a realm with every individual 4000 old runs the same MATTER events in the same order and loses nobody (floors `len(people) >= 10`, `len(want) >= 100`) (`:149-165`).
  - Seat-holder's death by age: persons at his place hold claims naming him, none elsewhere (floors on both); acquaintance-seeded build claims set aside (`:169-208`); at step 0 control, CR-81 acquaintances make the same holder die by a `fight` (measured 2026-11-04) so the control weakened to "every death has a causing act" plus a `acquaintances=False` arm (`:211-235`).
  - Draws are KEYED per person, not a shared stream: skipping one person's draw leaves the others' deaths unchanged (`:322-346`); `illness_rate` 1 kills every individual exactly once and no cohort; the same seed twice gives the same set (`:302-319`) - so deaths are probabilistic but seeded (consistent with the brief's carve-out).
  - `Person.born` has a reader (older dies, younger lives) (ID-13) (`:266-278`); H-129 `body.changed` chaining via `written=True` (`:370-411`).
- **Conflicts / stale:** the test arms (`AGE_ARMS = (0.01, 0.25)`, `ILL_ARMS = (0.5, 1.0)`) are marked `[JUSTIFIED: test arms]`. Certainty arms (hazard 1.0) are the only way age tests reach a death, so no test pins a game-relevant mortality curve.
- **Open items:** vacancy claims about the OFFICE or the closed HOLD after a death are "H-206's NOT DONE" per the docstring (`:23-26`) - but the sibling file `test_h206_a_death_at_matter_is_witnessed.py` covers a different half (placing the death), so the office-vacancy claim fan-out may remain open `[UNVERIFIED]`.

### engine/season/tests/test_in35_lattice_coupling.py
- **What it is:** v9 IN-35 FORCE-HAZARD: the Calamity re-expressed as a coupling rule `loop/matter.py::_lattice_strain` (a Site loses `lattice_coupling/condition_scale` of its gap to the weakest Site of its own or a bordering territory); mending is persons' `restore`.
- **Status:** none. Reading: live but SHIPPED DARK (`lattice_coupling == 0`, `:264-265`); and the source is a PLANT: "no act strains the lattice AT ASKEHEIM and the built realm holds no Site there" (H-236) (`:30-33`).
- **Bears on:** WR, SE (a Calamity/disaster clock), GO (geography `radiation_bands`).
- **Content that matters:**
  - Unmanaged: lattice condition falls and crossings reach territories in order of distance, checked against an independent oracle (`radiation_bands:` in the geography file) - bands 1..5 strictly ordered (`:146-165`); front advances one ring a season (parallel-map read of opening conditions) (`:168-177`).
  - Managed: menders `restore` through the real RESOLVE fold; holding ring 1 makes ring 1 cross every MATTER (limit cycle) and nothing beyond; `restored >= len(RING_1)*SEASONS` asserts the arm executed (`:184-207`). Mending the SOURCE does not recall a ring already pulled (`:210-222`).
  - Weight 0 is wear alone; non-zero differs (control that can fail) (`:229-239`); weight outside [0, scale] and NaN refused (`:253-256`).
  - The realm-level hash identity is historical (`@23b33e9e`); the live control is `test_the_thread_read_withheld_arm_is_pinned...` (`:20-26`).
- **Conflicts / stale:** the Calamity has no natural source in play (H-236): world clocks/hazards (WR) exist as a mechanism but shipped inert.
- **Open items:** H-235 sweep points (250, 500) are unchosen test arms.
