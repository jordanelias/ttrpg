# Valoria master workplan v10 — NERS amendments, part 2 (T08 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception).
## Lane: IN (cross-cutting). Part of `2026-10-24-v10-00-head.md`; continues `2026-10-24-v10-08-ners-amendments.md` (§1 how to read, §2 the table, §3 the entries from B10-01).
## Grade under `CLAUDE.md` §0.2: `paper`. IDs allocated: none.

## 3. The entries (continued)

### CP-T06-07 — REPAIR (B10-14) · AM-D-14

- **Override:** The item's size is M plus three named edits it did not count. (1) `rosters.yaml: record_kinds.values` `cover: [terms, as]`, with `content.read_from` for `as` (a non-operand source, read as declared, absent allowed). (2) `data/rosters.py:505-511`: `(COVER_KEY, COVER_AS) = RECORD_KIND_KEYS[COVER_KIND]` behind a `len != 2` guard, keeping the refusal for a missing kind. (3) `loop/effects_information.py:270` passes `{COVER_KEY: a.actor, COVER_AS: d.get("as")}` (no `"as"` literal: `rosters.py:499` says it is 'never spelt'). `live_cover`'s `terms == actor` read and `held_document_declines` are unchanged; `_cover_for` answers `sm.get("as")` when set, else the cover's id.
- **Taken (ladder step 5):** [ASSUMPTION; medium; Jordan to correct; revert: a second `record_kinds` member in place of the second key, which adds a kind and every reader of the cover kind's name.]
- **Because:** YES — `data/rosters.py:505-511`: `if len(RECORD_KIND_KEYS.get(COVER_KIND, ())) != 1: raise Unspecified(…)` and `(COVER_KEY,) = RECORD_KIND_KEYS[COVER_KIND]` (a two-key cover fails both lines at import).
- **After the attack:** 'Its first key is `COVER_KEY`' was circular (the unpack defines `COVER_KEY`) and would have loosened the exact-arity guard.

### CP-T06-09 — LIMIT (B10-14) · AM-D-16

- **N-line after:** `epistemic` helper that files a covered deed under the hand — cut it and an eyewitness's judgement of a covered deed lands on an alias nobody is, so the deed can never count in the regard a witness (or a judge he tells) holds of the doer. Narrowed to the judging side: `proofs` against a doer stays zero by the mirror.
- **Override:** No code change. Restate F06's consequence claims at three places: §0 fact 2 and §1 row I ("a found claim is already evidence"), §3 rows 07 and 09, §4 step 9 ("his proofs count against the clerk unless the clerk mirrors them"). A found or seen deed reaches a bench through the bench's own regard (`reception`, hence CP-T05-01's `opposed`) and through the witness's own judgement of the doer, not through `proofs`, because the doer always holds his own claim. The helper's falsifier (F06:160) is unchanged.
- **Because:** YES — for the code, relied-on for the measurement — `queries/world_q.py::proofs` (read): `mirror = {(c.subject, c.predicate) for c in opp.ledger}` and it sums `remove_weight` only over held deeds whose `(subject, predicate)` is not in the mirror; the opponent in a charge is the doer, and under the shipped `claim_subject_rule: both` every admitted witness, the doer included (he stands at his own act, channel `co_located`), holds `(anchor, kind, True)` (F06:31, `epistemic.py:185-215`, not opened by me).

### CP-T06-09 — RESEQUENCE (B10-14) · AM-D-17

- **Override:** none.
- **Because:** YES — `-03` B10-14 table: `| CP-T06-07 | … | BUILD | M | CP-T06-09 | no. |` and `| CP-T06-09 | … | EDIT | M | CP-T06-07 | no. |`. The Order line says `CP-T06-09 → CP-T06-07`, and the home says "07 after 09 (without 09, 07 makes eyewitnesses accuse the framed man)" (F06:208).

### CP-T07-02 — REPAIR (B10-15) · AM-E-02

- **N-line after:** the one working host — cut it and a practitioner has no thread act that rolls the Leap, rolls the operation and pays its cost through the seam in one place, so no thread row can be built without a second writer of `(Person, coherence)`.
- **Override:** `thread_scales` maps by target CLASS only: Person -> Personal, Tenure -> Relational, Site -> Field (a Site is a Site: IN-35 couples every kind). No "lattice Site" row. CP-T07-02 itself adds the carrier `Person.coherence` (resting point, elastic displacement; written only by the seam, `state/world.py:1014`) and deletes `unproduced:` from the matrix row in the same commit: a SCHEMA mover on every person's `repr`, declared (H-208). It also owns the actor adapter (AM-E-01) and the `working.failed` Event kind. Counted objects: module, prize row, `thread_scales`, `working.failed`, `Person.coherence`, adapter. Lands in `engine/season/seam/wrappers/threadwork.py`, `state/carriers.py`, `write_matrix.yaml`, `rosters.yaml`.
- **Taken (ladder step 3/4):** [ASSUMPTION; medium; Jordan to correct; revert: Structural for every Site, which prices every Site working at Ob 8 and cost -2]
- **Because:** YES — `loop/matter.py:142` "EVERY SITE, WHATEVER ITS KIND -- the lattice is the territories' fabric, not a kind", so "lattice Site -> Structural" is every Site; the home's own worked example maps a mill (a Site) to Field (T07:396-397), contradicting it.

### CP-T07-02 — REPAIR (B10-15) · HR-6

- **Override:** CR-13 lands first in B10-15, so the oracle CP-T07-02's host rolls no longer charges a Leap that rolls Partial or Failure. The home's step (2) ("on Failure the act ends, `working.failed`, and the Leap's charge stands (the oracle's own −1, C-TW-3, is carried, not fixed here)", lines 120-121), its falsifier ("a Leap Failure writes the Leap's charge and no target change", lines 138-139) and its closing line 463 are replaced: a Leap Failure ends the act with `working.failed`, writes no Coherence change and no target change; a Leap Partial proceeds and writes no Coherence change of its own. The other half of the falsifier (the seam Event's deltas equal the oracle's `OperationResult.coherence_delta` plus the Leap's for the same dice) stands, and the Leap's is 0. Mutation: skip step 2 and the Leap-Failure test still reds. Control: `ts_seed: none`.
- **Taken (ladder step 1):** [ASSUMPTION; medium; Jordan to correct; revert: CR-13 (a) is not built and the home's text stands]
- **Because:** YES — `systems/threadwork/sim/operations.py::attempt_leap` passes `coherence_delta=0` and its docstring says a failed Leap costs no Coherence (§3.2); the −1 comes only from the blanket penalty in `_resolve_operation`, which `operations.py:319-320` records as a known defect (C-TW-3).
- **After the attack:** Found by the editorial-id critic round (CR-13 vs the home text).

### CP-T07-03 — NARROW (B10-15) · AM-E-03

- **N-line after:** `weave` — cut it and a practitioner cannot hold a place against wear by carrying the load herself, so wear suspension remains a repeated unpaid `restore` act each season. `lock` — cut it and a practitioner cannot deny a rival a place (yield 0, no one else can repair it), the only act that destroys a place's use without ending it.
- **Override:** Delete the "strain for IN-35" row and the `strain(w, territory)` Query: `held_load(w, person)` stays (CP-T07-06 floors on it). Locked-Site yield 0 lands where `loop/matter.py` projects `ProduceInput.sites` into `settlements.produce` (skip a locked Site there), not at `matter.py:591`. The staged-delta refusal on a locked Site (`restore`, `work`, `sabotage`) stays; it becomes exercisable once REM-22 lands. `lock` on one's own Site is dominated by not working the Site (yield 0) and is not a designed use. A strain source for IN-35 is not built here (H-236 stays open).
- **Because:** PARTLY — `loop/matter.py:117-121,141-150`: the coupling reads Site conditions only; it takes no strain scalar and its docstring says it "does not build the SOURCE" (`H-236`). `hole_register.yaml` `lattice_coupling` ships 0 and IN-35's rule has no input a `strain(territory)` Query could feed; feeding it would be an edit to IN-35's coupling the home names as a "need" and nothing builds.

### CP-T07-04 — NARROW (B10-15) · AM-E-04

- **N-line after:** `mend` on a locked Site — cut it and nothing can undo a `lock`. `mend` on oneself — cut it and permanent set (which narrows the season, CP-T07-07) has no remedy. `mend` on another person — cut it and a stretched ally cannot be kept under the range inside a season (in-season value only).
- **Override:** Delete the lattice-Site route; IN-35's Mending arm stays `restore`, so the home's "edit to IN-35's text" (`_part5.md:91`) is not made. Routes kept: locked Site (clears `Site.locked`), another person (target's elastic falls; stated as in-season only), oneself (resting point -1, `self_mend_ob_step` swept at 0). The sentence "the Mender holds back the Calamity" in the home's chooser text is struck (no Calamity source exists, H-236). `mend` still cannot form on another's live `weave` or `ward`.
- **Because:** YES — `loop/effects_economy.py:109-138` `_rise` = headroom x share, "`f(degree)` IS NOT BUILT ... the term is therefore the IDENTITY"; `restore` and `work` are uncontested. `systems/threadwork/sim/coherence.py:115,133` `ELASTIC_RETURN_PER_SEASON = 6`, `ELASTIC_RANGE = 6`: one rested season in equilibrium returns the whole elastic range.

### CP-T07-05 — NARROW (B10-15) · AM-E-05

- **N-line after:** `in_equilibrium` — cut it and recovery is free everywhere, so a stretched practitioner has no reason to leave a locked place.
- **Override:** `queries/world_q.py::in_equilibrium(w, person)` is True unless the Site the person is contained at is `locked`. Delete `calamity_band` and the fixture `equilibrium_band_floor`; the control `equilibrium: everywhere` stays. The Calamity half re-opens, as a read of `closed_uses`, when H-236's source lands. The falsifier's locked/unlocked pair stands unchanged.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: gate on `closed_uses(w, territory)` being empty]
- **Because:** YES — `grep -rn calamity_band engine modules systems --include=*.py --include=*.yaml` returns nothing.

### CP-T07-07 — REPAIR (B10-15) · AM-E-07

- **N-line after:** permanent set narrows the season — cut it and set is felt only at the crossing, so a practitioner who overworked pays nothing between stretch and crossing, against the genre's central expectation.
- **Override:** No `coherence_band_penalty` table. Add a `coherence_band_floors` Fixtures tuple (shipped `()`), read as `standing_band_floors` is (H-223); a `band_floors["coherence"]` row would not load (its outer key is `site_kinds`, `rosters.yaml:2645-2655`, and `body` sits there by the H-38 exception). `budget()` subtracts `bands_below(<resting headroom>, fx.get("coherence_band_floors"))` beside `body_band_penalty`, one count per floor passed (higher resting is worse; the sign is handled once, in the caller). Shipped `()`: every arm equals today. The band edges are authored in the tuple, not retyped from `coherence._displacement_band`: the oracle's edges stay its own, and a drift between the two is the tuple's H-row, named [OPEN — Jordan tuning]. Reads `Person.coherence` (CP-T07-02); no World read.
- **Because:** YES — `decision/budget.py:64-83`: `bands_below(value, floors)` counts floors `value` is below; `body_band_penalty` = `bands_below(p.body, fx.get("band_floors")["body"].values())`. The home's `coherence_band_penalty` (T07:272) is a four-entry table indexed by band name, a second ladder method in one function.
- **After the attack:** A `band_floors["coherence"]` row does not load; the tree's method for a band over a derived quantity is a Fixtures tuple, which is also REM-50's.

### CP-T07-08 — NARROW (B10-15) · AM-E-08

- **N-line after:** `coherence.crossed` — cut it and a practitioner can pass the human band without anyone present learning it, so no witness can hold, tell or act on the fact.
- **Override:** The host emits one Event `coherence.crossed` (subject the person; fanned at WITNESS) the first time a seam write carries the resting point past `HUMAN_BAND_LIMIT`. Delete `crossing_outcomes` and `crossing_knot_stress` and the knot arm. The crossed person keeps acting. Falsifier: three Field workings that carry a hand-set resting point past 5 emit it once and a co-located witness holds the Claim; a fourth emits none (the home's "Structural lock Failures" are repriced by AM-E-02: Sites map to Field). The outcome content (queue A1 / A2-08) is reopened when something reads a consequence.
- **Because:** YES — `ctl/census2_s0.json` (and s1, s2) `event_kinds` hold no `arrest.made`; code report line 87 lists `arrest` and `tie / knot` among verbs never attempted over 12 seed-seasons; the slot is a roster whose every entry is `none` (T07:291), which no code reads; `-05` queue A2-08 records the content as ANSWERED-DOC on a PROPOSED canon section (`07_drift.md` §7.6), which is reference, not a mechanism.

### CP-T07-09 — LIMIT (B10-15) · AM-E-09

- **Override:** Add the stated limit: until the JQ-3 cell-value pass authors pursuit cells for `weave`, `lock`, `mend`, `ward`, an NPC practitioner's choice among them is decided by order, not by preference; the "unwatched" claims of T07 §2-§4 hold for witness scars and for execution by a planted or played practitioner, not for an NPC preferring one working. No design change.
- **Because:** YES — `decision/choose.py:129-151` `score_terms` = (pursuit sum over `align(c.verb, ax)`, stance, urgency); the stance and urgency terms do not depend on the thread verb's identity beyond its target; the content report (orchestrator, 16 verbs uncelled) lists no thread row celled; T07:305-312 authors affiliation cells (witness scars) and defers the pursuit axes to JQ-3's pass.

### B10-16 gates, IN-52 and `requisition` — RESEQUENCE (B10-16) · AM-E-21

- **Override:** Record the gap in the batch card and in `-02` and `-06`: no position makes `requisition` execute in computed play; the owner is none. The seat channel carries only MATTER-recorded reads, and the realm records no shortfall after season 1 (`scarce.py:21-24`); no channel gave any issue-granting holder a settlement-larder claim (H-163 limit 3(a): `larders_in_purview` returned `()` in 766 of 766 calls). Until a position takes H-163 limit 3(a) (**[GAP: unowned]**), CP-T08-06's compliance reader, CP-T08-07's collection, CP-T08-08's refill and IN-52's flip are credited on hand-built worlds only, and none counts toward R-04 conjunct (1) (`-02` §5). CP-T08-04 is held at ED-IN-0297; CP-T08-02's `ground` flip waits on a relief path. Nothing is added to fix it: which lift to build (a seat-channel level report, or residence-ladder reach) is a design choice with different information games, and H-163 says it is not this row's to choose. The choice of lift is asked as M17 (`-05`) by the later hole-row pass; until it is answered no position builds either lift.
- **Taken (ladder step 1):** [ASSUMPTION about the gap only: record it, build nothing]
- **Because:** YES — and the cause is not authority. (1) Census: `ctl/census2_s0.json` `event_kinds`: `requisition.unauthorized` 12, `requisition.refused` 4; s1 10/5; s2 9/2; `requisition.taken` never emitted.
- **After the attack:** The causal claim stands. 'Unowned' was not new (IN-52 was already gated on H-163 3(a)); the draft's account of the channel was wrong, and `-02` and `-06` now record the gap in the plan's own shape. The B10-16 card edits the draft listed had not been applied and now are.

### CP-T08-01 — REPAIR (B10-16) · AM-E-12

- **N-line after:** `labour` — cut it and a death, a flight or a cohort's starvation costs a town no output, so there is no famine spiral (fewer hands, less food, more hunger); the battle->output direction is not observable until a march arrives.
- **Override:** `labour(w, rung)` is per RUNG: sum of `weight x body / body_scale` over `presence(w, rung)`; the yield factor is one per rung, `min(1, labour / sum(site_crew[kind] for the rung's producing Sites))`, so a person's hands are spent once however many Sites the rung holds and `site_crew` keeps its meaning (the hands at which the rung's whole fabric reaches its condition-scaled base). It lands as one per-rung ratio on `ProduceInput` (`modules/settlements/produce.py`), built in `loop/matter.py` from `world_q.labour`; `labour_mode: off` is 1. The falsifier (c) person-moves-onto-the-rung stays; a battle falsifier is dropped until a march arrives (stated limit).
- **Because:** YES — `modules/settlements/produce.py:30-52` `produce(inp)` loops each rung's `(site_kind, condition)` pairs and computes `int(base * (condition/scale) * inp.factor)`: the arithmetic is behind `ProduceInput`, not `loop/matter.py:589-591`.

### CP-T08-02 — LIMIT (B10-16) · AM-E-13

- **Override:** Add the limit: `endowment_mode: ground` is built and ships `uniform`, and the flip to `ground` is NOT part of B10-16. It waits for a measured relief path in computed play (`transfer` or `exchange` moving stock to a short town), because under `ground` every non-coastal town is short of salt and every mountain town of grain by construction, which with REM-52's live `body_step` kills cohorts. The flip is its own declared-mover commit when that path executes; the magnitudes are JQ-6's [OPEN — Jordan tuning].
- **Because:** YES — `data/fixtures.py` `SITE_YIELD == {'harbour': {grain 40, salt 30}, 'seam': {ore 50, timber 10}, 'body': {}}` (read from the loaded module); `SUBSISTENCE_WEIGHTS == {'grain': 2, 'salt': 1}`. The home's `field` yields grain only.

### CP-T08-04 — RESEQUENCE (B10-16) · AM-E-15

- **Override:** CP-T08-04 is HELD at ED-IN-0297 (where a works comes from in computed play), with IN-45. It builds nothing in B10-16. When it is released: `smithy`/`mint` Sites are placed by `site_endowment` or built by `build`, whichever ED-IN-0297 rules; recipes stay [ASSUMPTION; medium; Jordan to correct]. CP-T08-05 no longer needs it (AM-E-16).
- **Because:** YES — home CP-T08-04 item 3 raises `smithy`/`mint` "by the shipped `build`"; `hole_register.yaml` H-165 (limits 2-3) and H-166: `build` needs a works Record, "nothing computed declares a works"; `ctl/census2_s0..s2.json` `resolved_by_verb.build` 40/48/47, none executed. The plan already holds IN-45 on the same question (ED-IN-0297, `-04` IN-45 entry).

### CP-T08-05 — REPAIR (B10-16) · AM-E-16

- **N-line after:** `price_of` — cut it and goods move only by authority or gift, so a town in dearth cannot buy; it is paper until an `offer` has a computed producer.
- **Override:** `price_of(w, rung, kind) = price_base[kind] × (need + 1) // (stock + 1)`, where `need = demanded(kind) × price_horizon` and `stock` come from the same draw record and `Rung.stores` reads REM-50 uses: one owner of the reads, no second ratio. The recipe-input term is dropped (CP-T08-04 is held). Lands in `queries/world_q.py` beside `hunger`. The item ships and executes on hand-built worlds only (an `offer` Record needs a producer; H-165's shape); nothing in the shipped realm exercises it.
- **Taken (ladder step 4/5):** [ASSUMPTION; medium; Jordan to correct; revert: the home's `need/stock` formula]
- **Because:** YES — home item 4: "A computed `create_record` mints only `text` today (H-165), so offers form only from a hand-built or played act"; `ctl/census2_s0.json` has no `exchange` in `resolved_by_verb`.
- **After the attack:** 'Per-kind cover' does not exist (REM-50 gives an aggregate integer) and 'inverse of cover' divides by zero at stock 0. The formula now reads the same draw record, and the cross-request to REM-50 is dropped.

### CP-T08-06 — NARROW (B10-16) · AM-E-17

- **N-line after:** `unrest(w, S)` — cut it and an overtaxed but fed town yields to every taker forever; neglect never degrades a place. Reader: the census report now; `requisition`'s compliance when it executes.
- **Override:** Delete home item 2: no `unrest_signs` roster and no clause added to `stability`. `unrest(w, S)` is the sum over cohorts residing at S of `-stability(c, S, unrest_window)` as it already counts (dominance deeds including `requisition.taken`, and shortfall claims); the band is an `unrest_band_floors` Fixtures tuple (shipped `()`), as `hunger_band_floors` is. The falsifier uses `shortfall:grain` claims, not hunger-band claims. Its reader before CP-T08-07 is the census line only (`uncontrolled`'s precedent), so it is a report until `requisition` executes. REM-51 is cut: nothing here reads a hunger-band claim.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: add `rosters.yaml: unrest_signs` with the hunger predicate at `hungry`/`starving`]
- **Because:** YES — `queries/person_q.py:481-505` `stability` = minus the count of claims at the rung that are deed claims of an `UNREST_KINDS` kind (`person.died`, `body.changed`, `field.won`, `rung.seized`, `record.seized`, `requisition.taken`) OR a `shortfall:<kind>` claim.
- **After the attack:** Same banding method as REM-50 and CP-T07-07 (a tuple fixture); the REM-51 premise is struck.

### CP-T08-07 — RESEQUENCE (B10-16) · AM-E-18

- **N-line after:** the `tax` edict — cut it and governing leaves no rule behind (no rate, no slot, no lag), provided a governor can know the stock he rates; until then it is dominated by a bare requisition.
- **Override:** CP-T08-07 is gated on H-163 limit 3(a) (a governor holds a stock claim of the rung he taxes) and does not build before it. Its "one slot per place" is a slot on EDICTS only: a rival seat's bare `requisition` (IN-49) takes regardless; this is stated, not designed away (the home's text implies a slot on takers). It no longer needs CP-T08-08 (the treasury is a join, not a need). Compliance by `unrest` band (item 5) stays as written and ships at 1000.
- **Because:** YES — and stronger than the lane states: home item 4 sizes the collection as `edict.amount x ramp / 1000 x the stock his newest claim gives` and marks the carrier `[UNVERIFIED: which claim carries a rung's stock to its governor]`.

### CP-T08-08 — REPAIR (B10-16) · AM-E-19

- **N-line after:** the upkeep question — cut it and a stocked treasury can never pay its establishment by a chooser's act, so every establishment lapses at its first term.
- **Override:** `upkeep_due` skips any group whose place is the seat's own rung (clause 3 renews nothing there) and forms a Candidate only while the seat's rung holds at least the group's amount of the kind, so a bare treasury forms nothing (no scene crowding, H-156's shape). Delete the Join sentence about IN-49 forming a refill. It forms 0 acts in computed play until a treasury holds stock; its only filler is `requisition` (AM-E-21), so its falsifier runs on `harness/scarce.governed`. CP-T09-05 and CP-T09-07 need this item (CROSS: F): their lapse-and-pay paths are hand-built until the gap closes. Sharpened risk: no computed `oblige` exists to renew (`effects_economy.py:335`; the row is untyped, so there is no term to renew).
- **Because:** YES — `loop/effects_economy.py:301-303` clause 3 (`src == dst` "A transfer from a rung to itself cancels to nothing") and `:342` (`if ... src == dst ... return []`): a same-rung group renews nothing. The home's `upkeep_due` groups obligees by last-known place and forms one `transfer` per group with `from` the seat's rung.
- **After the attack:** The dependence on an `oblige` that never forms is stated.

### CP-T08-10 — RESEQUENCE (B10-16) · AM-E-20

- **N-line after:** the domain limit — cut it and holding more seats is never a cost, so granting a seat away is never a choice; it prices exactly what IN-14 lets buy scenes.
- **Override:** The cap and overhead apply to the same count `budget()` multiplies by `budget_office_bonus`, i.e. the narrowed `offices` after IN-14 (holds with non-empty `granted_acts`), not to every live `hold`. Until IN-14 lands, CP-T08-10 builds nothing. The formula is the home's: `b = k + min(offices, hold_bonus_cap) x bonus - max(0, offices - hold_overhead_from) x hold_overhead`, shipped fixtures reproduce today. Landholdings that are not seats are priced by IN-14's ruling, not twice.
- **Taken (ladder step 4):** [ASSUMPTION; medium; Jordan to correct; revert: count every live hold, as the home does]
- **Because:** YES — `decision/budget.py:57-58`: `offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)`; `b = k + offices * budget_office_bonus`. `effects_information.py:126-140`: `_makers_hold` is the opener for `create_record`, `issue`, `open_case`, `petition`, `survey`, `forge`, `utter`.

### CP-T09-01 — LIMIT (B10-17) · AM-F-16

- **N-line after:** leaving and joining decided by opinion — cut it and the gameplay experience is worse, because a member cannot leave a faction he has come to read below indifference, nor a stranger join one he favours, since no candidate reflects opinion; this is built only if the pre-build reading (members reading own faction below 0; (person, rival creed) pairs passing the join gate, ticks 0-2, hash-equal) finds both a leaver and a gate that is not near-universal.
- **Override:** CP-T09-01's first commit is the reading, not the code: seeds 0-2, ticks 0-2, hash-equal, counts of members with `opinion_of(own) < 0` and of (person, rival creed) pairs with `opinion_of > max(0, own)`. Zero leavers: the leave body is not built. Join gate passing for most of the cast at tick 0: the filter is not built as written. Either residue is recorded and the item closes as MEASURED. The home's own "R-CHOICE … keep my followers" claim is amended as AM-F-14 says.
- **Because:** YES — T09 file `:149-154` (measure first, "both halves": if no member reads own faction below 0 the leave body is not built; if the join gate passes for most of the cast at tick 0 the filter is too loose to build as written). `queries/world_q.py:2294-2327` (`opinion_of` as above) and `:2330-2354` (`opinion_referents`' own gate `< 0`).

### CP-T09-02 — RESEQUENCE (B10-17) · AM-F-10

- **Override:** B10-17 order: CP-T09-04; -01; -05; -02; -03; -07; -08; -09 (the home's §5), with -04 carrying IN-30's exit; CP-T09-06 waits on IN-61 (STOPPED) and IN-53 (no v10 position), so it does not open the batch. Needs: CP-T09-02 swaps `CP-T09-03, CP-T09-07, ED-IN-0298` for `CP-T09-04`; CP-T09-04 drops `CP-T09-07` (AM-F-13 moves the shared count to 07's commit); CP-T09-08 drops `ED-IN-0298`. M11's builder carries a constraint: the replacement for `chronicle` must publish `war.declared` (the one kind CP-T09-02 relies on it for). IN-30 builds with CP-T09-04 (d), as before.
- **Taken (ladder step 3):** [ASSUMPTION; medium; Jordan to correct; revert: restore the plan's order and needs; the cycle then has to be broken some other way.]
- **Because:** YES — for the needs graph as the plan states it; the plan's B10-17 contradicts itself and the home's §5. Plan rows: CP-T09-02 needs `CP-T09-03, CP-T09-07`; CP-T09-03 needs `CP-T09-02` (a two-row cycle); CP-T09-04 needs `CP-T09-07`; the batch's order line puts 02 before 03, 04 before 07 (backward edges).
- **After the attack:** CP-T09-06 was placed first as having no dependency; it needs IN-61 and IN-53.

### CP-T09-02 — LIMIT (B10-17) · AM-F-11

- **N-line after:** `declare` and the war it opens — cut them and the gameplay experience is worse, because no act makes a war a state anyone can read, so a wound across factions cannot become a declared war that members rally to; whether the war's targets are taken is a separate, later claim (`march` and `seize` arriving), made only when an arrival is observed.
- **Override:** CP-T09-02 is reported done for the declaration (a computed `declare` forms, executes and its `war.declared` reaches a ledger) and NOT done for term (c)'s teeth. The teeth are done only when a seeded run shows `army.arrived` ≥ 1 after a computed `march` on a term-(c) target, or `rung.seized` ≥ 1 after a computed `seize` on one. The realm reading records `war.declared`, term-(c) offers, `march` formed / refused / arrived, `seize` formed / executed, at seeds 0-2, and names the first link that failed (formed, offered, attempted, arrived), as REM-27 does. The same clause binds CP-T09-03, -04 and -08 for their own chain links. The B10-17 Exit says so, because the clause otherwise sits only in CP-T09-02's title: CP-T09-02, -03, -04 and -08 count their chain's teeth only on an observed `army.arrived` or `rung.seized` after a computed act on a term-(c) target, seeds 0-2.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: the home's formation-only falsifier.]
- **Because:** YES — the home's falsifier (2) (T09 file `:212-215`) reads: *"With W live, a Crown `dispatch` seat forms `march` on a Hafenmark-held settlement its ledger never named"*: a formation test; its realm reading is `war.declared`, `field.won + field.lost` "base 0, 0, 0" with no pass condition.
- **After the attack:** The clause was written for four items and printed in one; the batch Exit now carries it.

### CP-T09-03 — LIMIT (B10-17) · AM-F-12

- **N-line after:** alliance and peace as acts on the war Proposition — cut them and the gameplay experience is worse, because a third faction cannot be invited in and a war cannot be ended on an offer, only by each committer's unprompted `release`; the item is done as formation until the covenant link executes.
- **Override:** CP-T09-03 is reported done on a hand-built chain plus a realm reading of each link: `covenant` formed / refused / executed with a W subject, `give` of the instrument, the counterparty's `commit` or `release`. It is not reported done for computed alliance or peace until a seeded run executes `covenant` ≥ 1 with a W subject. If the reading shows `covenant` still refused for wrong-kind subjects, the residue names `referent_class` on `covenant` (REM-23's shape) as the next link and the item stays `paper` for the computed chain.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: none needed, the clause only restricts what is reported done.]
- **Because:** YES — `verb_table.yaml:292-312`: the `covenant` row declares `requires_typed` (`existence` of `subject` kind Proposition) and no `referent_class:` (the only classed rows are at `:226, :266, :820, :892, :943`; none is `covenant`), and its note says *"A computed covenant forms on a Proposition referent … on any other referent the `subject` conjunct refuses it in the fold"*: an unclassed row forms on every plain referent, so the 41 refusals are the wrong-kind class REM-23 removed from `commit`.
- **After the attack:** Wording only.

### CP-T09-04 — REPAIR (B10-17) · AM-F-13

- **Override:** CP-T09-04 lands on `mustered` as filed and stops needing CP-T09-07. CP-T09-07's commit adds one reader, `world_q.seat_people_at(w, via, rid)` = `mustered(rid, seat_faction(via))` ∪ the seat's obligees present in `rid`'s subtree, and in the same commit points `sides_of` (`sides.py:115`), `occupying_faction` (`effects_shared.py:149`) and the plurality comparison of CP-T09-04 (b) at it. The one-count claim at T09:515-516 is true after that commit and false between the two. 04's falsifier (2) is re-run in 07's commit with an obligee-only seat: the obligee counts toward the plurality.
- **Taken (ladder step 5):** [ASSUMPTION; medium; Jordan to correct; revert: obligees fight but do not occupy, and the home's S-line is amended to say two counts.]
- **Because:** YES — `loop/effects_shared.py:149-168` `occupying_faction`: the licence tests `mustered(w, rid, mine)`; `loop/sides.py:~115` `claimants = mustered(w, origin, faction)`; `state/gate.py:865-888` `may_muster`: a moved man must hold a live `commit` to the seat's faction.

### CP-T09-04 — LIMIT (B10-17) · HR-4

- **Override:** Two residues of H-151 are CP-T09-04 limits, not LEAVE: a third faction is invisible on an unheld settlement, and two armies on one empty target both arrive. Both fall inside the item's subject (plurality occupation of land with no holder).
- **Because:** H-151's residues 2 and 3 are the same subject as CP-T09-04.
- **After the attack:** Found by the hole-row critic round (H-151 EDIT).

### CP-T09-05 — LIMIT (B10-17) · AM-F-14

- **N-line after:** the fief occasion — cut it and the gameplay experience is worse, because no follower is ever given land in computed play (0 formed at HEAD); it is NOT claimed to keep a follower, which waits on a `deed:rung.ceded` cell.
- **Override:** Add to CP-T09-05's stopping rule: a grantee whose `opinion_of(own faction)` reads below 0 within two seasons of a cession to him and who then `release`s his `commit` counts as a defection the grant drove; if such a defection appears in the seeds 0-2 reading, revert the term. Strike "grant land" as an answer to "keep my followers" in T09's R-CHOICE paragraph (T09:500-501): the intent has no act at HEAD that reaches it (pay upkeep waits on CP-T08-08; do nothing emits the follower's `commitment.ended`). The "no strict dominance" line stays an upper bound and says what it is an upper bound over: rows that do not yet reach the intent.
- **Because:** YES — `rosters.yaml:3199, 3245, 3285, 3342, 3383, 3436` are `give: null` and `:3494` is `give: -0.2` (one axis, "mild"). `data/verbs.py::KIND_VERB` maps `rung.ceded` and `record.given` to `give` (checked by import), so a witnessed cession is judged at `give`'s cells until a `deed:rung.ceded` cell is authored.

### CP-T09-07 — REPAIR (B10-17) · AM-F-15

- **N-line after:** (b) the seat's obligees in its army and its count of people at a place — cut it and the gameplay experience is worse, because a sworn man yields purview and no men, so oaths bind nobody to a field; (a) `recruit` — cut it and no seat can bring a man into service by a contested act, which is claimed only on the uncapped arm.
- **Override:** CP-T09-07 has two exits. (b) the union (`world_q.seat_people_at`, AM-F-13) and `may_muster`'s `oblige` clause: done on an executed hand-built march plus the obligee-only plurality arm; independent of H-213 and of CP-T01-06. (a) `recruit`: reported done only on the uncapped arm with a won `recruit` in a seeded run, and "not shown at the shipped ceiling" otherwise; its obstacle terms are demands on `roll.py::obstacle` and are clipped there at the shipped ceiling. The realm reading counts won recruits of seat-holders separately, as the home's stopping rules ask.
- **Taken (ladder step 4):** [ASSUMPTION as AM-F-13.]
- **Because:** YES — the home (T09 file `:379-383`): at the shipped ceiling (default 2, `data/fixtures.py:416-419`) an added obstacle term is clipped, so falsifier (1) runs on H-213's uncapped arm, owner CP-T01-06; the plan's `-03` row names `CP-T01-06`, `H-213` as needs. `loop/sides.py` is edited by this item (b), by CP-T04-01 and by CP-T04-04 (the same file). The count split is AM-F-13.

### CP-T09-09 — LIMIT (B10-17) · AM-F-17

- **N-line after:** a plot with backers — cut it and the gameplay experience is worse, because backers and the refused invitation cannot exist (a lone killing survives as `fight`); built only if a reading over the realm's persons toward seat-holders at ticks 0-2 finds `legitimacy < 0` for anyone.
- **Override:** CP-T09-09's first commit is a hash-equal reading of `legitimacy(p, H)` for every person toward every seat-holder at ticks 0-2, seeds 0-2. Null (nobody below 0): the item is cut and a CUT row is added to `-07` §2 with the reading as its reason. The obstacle terms on `roll.py::obstacle` are clipped at the shipped ceiling (as CP-T09-07 (a)); the falsifier runs on the uncapped arm only.
- **Because:** YES — T09 file `:449-450` ("Measure first. As CP-T09-01: B-V's foreign prefect read no negative `legitimacy` at three placements") and `:486` ("the first to drop if its measure-first reading is null"); `queries/person_q.py:~452` `legitimacy`. The plan's row has no measure-first mark.

### CP-T10-01 — REPAIR (B10-18) · AM-F-07

- **N-line after:** the journey priced by its route — cut it and the gameplay experience is worse, because where things happen carries no cost for a seated player (IN-47) and distance buys nothing; for an NPC it is an unseen cost, and no position gives a chooser a person-side reading of the leg's price (T10 D-1): **[GAP: unowned]**.
- **Override:** Terrain at a point has one owner: extract the loop at `modules/mass_battle/terrain.py:~189-195` into a public `terrain_type_at(point, *, geography)` that `terrain_row_for_territory` also calls; `route` reaches it as a `query` role (a row in `references/module_contracts.yaml`, an entry in `world_q.QUERY_ENTRIES`), never by import. `route` returns `None` when any entered settlement costs the matrix's `mountain` entry; the journey is `travel.blocked`, as the border is. `route_pricing` ships OFF; the same-place rule ships on both arms. The on-arm default does not flip: no position gives a chooser a person-side reading of leg price (T10 D-1), **[GAP: unowned]**. Falsifier gains: a settlement planted in a `mountain_pass` polygon nested in a `mountain` costs 2.0, not 999.
- **Taken (ladder step 4):** [ASSUMPTION; medium; Jordan to correct; revert: restore a first-match lookup in `data/geography.py` and accept the second copy.]
- **Because:** PARTLY — all cites open: `systems/settlements/valoria_geography_v30.yaml:760-771` (`mountain: 999.0`, `mountain_pass: 2.0`, comment *"Mountain interior is impassable except via embedded mountain_pass polygons"*); `modules/mass_battle/terrain.py:150-195` (the smallest-area match is inline in `terrain_row_for_territory`, keyed on a *territory anchor* and returning a six-row class through `_TYPE_TO_ROW`, not a terrain type; `_point_in_polygon` and `_polygon_area` are private).
- **After the attack:** The 'has a position' gate carried nothing; there is no such position.

### CP-T10-02 — REPAIR (B10-18) · AM-F-08

- **N-line after:** the Calamity costs the traveller — cut it and the gameplay experience is worse, because the Calamity's edge is only scenery to anyone who walks there, since nothing makes a place dangerous to visit.
- **Override:** `band(territory)` is breadth-first distance over `data/geography.py::adjacent_territories()` from the epicentre territory (`terr_T15`), written as one function in `data/geography.py` beside it. `exposure_body` is keyed by that number. The file's `radiation_bands` table stays unread by game code and remains the tests' independent oracle: the falsifier asserts the BFS band equals the file's band for all 17 territories (it does today, measured). Strike "read through `data/geography.py` until then" (T10:166). `radiation_bands` band-0's territory is the only read of that table, for the root, and `geography.py`'s docstring is amended to say so.
- **Taken (ladder step 4):** [ASSUMPTION; medium; Jordan to correct; revert: root named in a `rosters.yaml` row `calamity_epicentre` instead.]
- **Because:** YES — `data/geography.py:43-65`: `adjacent_territories()` is the undirected territory adjacency, and its docstring says *"THE FILE'S `radiation_bands:` IS NOT READ HERE, AND THAT IS THE POINT: a band there is 'node distance' from Askeheim, i.e. a breadth-first reading of these same edges, so reading both would be two owners of one distance.

### CP-T10-03 — REPAIR (B10-18) · AM-F-04

- **N-line after:** the year — cut it and the gameplay experience is worse, because yield and need are the same every season, so stocking before winter and relief before the lean season are never choices.
- **Override:** The `want` multiplier is applied in `world_q._larder_parts` (`world_q.py:~1100`), scaling each `subsistence_weight` entry by `season_terms[season_of_year].want` and rounding to a whole number (half up); it is not applied in `subsistence_draw` or MATTER. `larder_draw` and `subsist` are unedited, so the Query and the draw read one projection. `season_factor_of` returns the bare `season_factor` when `season_factor_draw` is empty, whatever `season_of_year` says. CP-T10-03 no longer needs CP-T10-05. Falsifier gains: `demanded(w, S)` and MATTER's delivered+short agree at a winter tick; a salt weight of 1 under 1.5 is 2, never 1.5; `year_length` 4 with the draw `()` raises nothing.
- **Taken (ladder step 5):** [ASSUMPTION; medium; Jordan to correct; revert: `season_terms.want` entries 1.0.]
- **Because:** YES — `queries/world_q.py:1002-1054` (`subsistence_draw` is `_draw_dict(_entry(LARDER_DRAW)(larder_input(w)))`; its docstring: *"the arithmetic is the `settlements` module's … `larder_draw` owns the cohort exemption, the walk … and `take = min(want, held)`"*); `modules/settlements/larder.py:52` (`want = wt * e.weight`, `wt` from `inp.weights`); `queries/world_q.py:1080-1127` (`larder_input` / `_larder_parts` build `LarderInput(tuple(sorted(weights.items())), …)` from the `subsistence_weight` fixture, `{'grain': 2, 'salt': 1}` at HEAD; `subsist_input` calls the same `_larder_parts`).

### CP-T10-05 — NARROW (B10-18) · AM-F-05

- **N-line after:** a hazard hit wounds and sickness reads where a person stands — cut it and the gameplay experience is worse, because the 46 named persons feel no pressure from the world they stand in and a hit is still a one-shot kill.
- **Override:** CP-T10-05's N-line is items 1 and 2 only: the wounding hit and the world-reading illness term. The age term is `body_hazard`'s existing `age_step × age`, unchanged by this item and unchanged in meaning: a calendar ramp until H-208 gives persons different `born` values. Strike from the home: the sentence "The age half becomes GK2's (DA:#19)" (T10:245) and gap H's "age reaches the body" closure (T10:73): the item does not close DA:#19. Add the needs edge CP-T10-05 → CP-T10-04: the home orders recovery first ("sickness must heal, or it is slow death", T10:497) and the plan omitted it.
- **Because:** YES — `queries/world_q.py:970-999` (`age_of = w.tick - w.persons[pid].born`; `body_hazard = min(1.0, illness + age_step * max(0, age_of))`); `data/fixtures.py:604-609` and the printed defaults (`age_at_build=0`, `age_step=0.0`, `illness_rate=0.0`); `state/carriers.py:687` and `loop/census.py:106` (`born = w.tick - age_at_build` at build, the only writers); `references/npc_registry.yaml:52` etc.

### CP-T10-06 — REPAIR (B10-18) · AM-F-01

- **N-line after:** the `kin` edge — cut it and the gameplay experience is worse, because the game can no longer say who is whose spouse or child, so an estate (CP-T10-07) passes to nobody and `marry` (CP-T10-08) has nothing to open.
- **Override:** Item 1: `kin` is a releasable kind. Add `kin` to `release`'s `domain:` (`verb_table.yaml:1054`); `RELEASABLE_KINDS` derives it from `tenure_kinds` with no edit. Divorce or disowning is the owner's `release` of his own directed edge. It is one-sided: the releaser forfeits his claim on the other's estate, and hers stays live (`_eff_release` closes only edges whose subject is the actor); `marry`'s spouse negation reads live `spouse` edges owned by or naming either party, so a remarriage is refused while she holds the edge. Item 3 (the `kin` witness channel, `kin_news_kinds`) is cut from this item: a sixth channel is a §C.6 Layer-1 row, ED-IN-0298/M11's to authorise. Whoever lands that channel renames `fan_out_mode: all_five` and the roster value. T10:104-105 is corrected: the item touches Layer 1 only through the channel, now removed. Falsifier gains: a `release` of a spouse edge closes it and leaves the other spouse's edge live.
- **Taken (ladder step 3):** [ASSUMPTION; medium; Jordan to correct; revert: restore item 3 and gate CP-T10-06 on M11.] [ASSUMPTION; medium; Jordan to correct; revert: `marry`'s negation reads edges owned only]
- **Because:** YES — opened `data/rosters.py:483` (the one derivation line), `data/verbs.py:1028-1046` (`_release_domain != RELEASABLE_KINDS` is a `SystemExit`; the closer clause adds *"no third excluded set can exist"* and refuses a declared `domain:` member that needs no closer), `verb_table.yaml:1054-1057` (`release` domain `[hold, commit, oblige, succeed, tie, knot]`).
- **After the attack:** 'A released edge forfeits the claim' was true of one spouse only; divorce is one-sided, and the abandoned spouse remains an heir.

### CP-T10-07 — REPAIR (B10-18) · AM-F-02

- **N-line after:** the estate record — cut it and the gameplay experience is worse, because a dead holder's papers and land become nobody's the instant he dies, since his own edges leave with him (`hole_register.yaml:4502`), so no heir can ever be offered them.
- **Override:** `_estates` is renamed `World.estates`, declared in `World._STATE_COLLECTIONS` (`state/world.py:1348`), written once inside `remove_person` beside the `_departed` line (`:758`), value `(tick, sorted object ids)`, keyed by the dead man's id, never cleared and never rewritten. It is a new owner and says so. "Unclaimed" is read, not stored: an object is claimable while `hold_force(obj)` is `None`. `estates_named(w, p)` offers an object only to `p == heir_of(w, dead, obj)` AND who holds a `person.died` claim naming `dead`, from any source (the `told` shape of `places_named`). The kin channel is cut (AM-F-01), so a far heir waits for a `tell`. Falsifier gains: a hash difference between a world with a recorded estate and one without; the entry survives three ticks. `estates_named` is one more term in `questions_for`'s `added` splice beside `larders_in_purview` (REM-21 as amended has no registry, so the home's item 3 has no `STAMPERS` to ride).
- **Because:** YES — `state/world.py:264` and `:758` (`_departed[who] = (t.object, self.tick)`, written in `remove_person`); `loop/driver.py:444` (`w._departed.clear()` at the top of each tick, which is a season); `state/world.py:1358` (the `content_hash` docstring names `_departed` "the one per-tick exception"); `state/world.py:1348-1353` (`_STATE_COLLECTIONS` is a closed tuple).
- **After the attack:** The hash design is sound; the registry it rode is deleted by AM-A-06.

### CP-T10-07 — LIMIT (B10-18) · AM-F-20

- **Override:** CP-T10-07 is reported done for the record and the hand-built claim chain (the falsifier as filed). The realm reading, seeds 0-2, four seasons, records: kin edges at build; `estates` entries written; `heir_of` non-empty; estate `succeed` formed / executed. All zero is the expected base and is recorded as such. The item is not reported done for the live world until an estate `succeed` executes in a seeded run, which on canon alone needs `marry` (CP-T10-08) to have produced a spouse edge first.
- **Because:** PARTLY — the dependency is real and AM-F-01 makes 06 load.

### CP-T10-08 — RESEQUENCE (B10-18) · AM-C-07

- **N-line after:** `marry` — unchanged by this edit.
- **Override:** None to a design. The `individual` stem is a B10-11 first commit (CP-T03-01 and CP-T03-09 use it); CP-T10-08 reuses it and adds its verb row. CP-T10-08's `needs` drops the T03 entry; B10-18's entry gate names the stem beside `body_ceiling`.
- **Because:** PARTLY — B10-11's order line says the stem is built first "because CP-T03-01 and CP-T03-10 use it" and the CP-T10-08 row's `needs` lists `CP-T03-10`. T03's CP-T03-10 is the parked `rescue` (file:254-258); the item that uses the stem is CP-T03-09 `capture` (file:114, "on `fight`, `accept` and `capture`"). The lane's `-09` is right for the order line.

### CP-T10-08 — LIMIT (B10-18) · AM-F-09

- **Override:** No design change. Falsifier: after A releases his spouse edge, A's `marry` to C is refused keyed `spouse` while B's edge naming A is live (divorce is one-sided, AM-F-01). `CROSS: C` — the `individual` stem (`data/requires.py::REQUIRES_STEMS`) is built by CP-T10-08's entry in B10-11 first (the `-03` B10-11 order line).
- **Because:** YES — the `-03` row needs `CP-T03-10, CP-T10-06, ED-IN-0210, IN-08`. AM-F-01 changes one fact it reads: `kin` is releasable, so a spouse edge can be closed by its owner's `release`. The home's "Deliberately not done: divorce … (parked)" (T10:563) stays true of a divorce *verb* and is now untrue of divorce as an act: `release` on the spouse edge.
- **After the attack:** The drafted falsifier ('remarry after release is not refused') is false under the one-sided release the repair of CP-T10-06 adopts.

### CP-T10-09 — NARROW (B10-18) · AM-F-03

- **N-line after:** `_bond`'s kin clause — cut it and the death or wounding of a judge's own kin weighs on him no more than a stranger's, since `_bond` counts only himself and his stance rows.
- **Override:** In `queries/person_q.py::_bond`, `a = 1.0` when `patient == p.id` or the patient is the object of a live `kin` edge in `p.tenures` (a Person carries every Tenure whose subject he is: `state/carriers.py:76-80`, read person-side at `decision/budget.py:57`); otherwise the stance ratio as today. One clause. `patient_valence` and `patient_gain` are not created, and the unpaired kinds (`body.tended`, `record.given`) are dropped from the item: no pairing of a claim to its patient exists for them. CP-T10-06's `heir_of` and `marry` readers are unchanged.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: restore the home's `patient_valence`/`patient_gain` design, or cut the item]
- **Because:** The lane's diagnosis was right: death and wound are already judged through `_bond` (`person_q.py:350-361`), so the home's 'patient-blind' is false for the kinds that carry the kin hook.
- **After the attack:** Rejected as drafted (a cut): the draft held that a kin edge, being a World Tenure, cannot be read person-side. A kin edge the judge owns is in his own `tenures`; only an edge he does not own (the `oblige` precedent, `person_q.py:118-120`) is out of reach. The lane's own narrowing stands.

### CP-T02-04 — CUT (?) · AM-B-10

- **N-line after:** none: cut.
- **Override:** CP-T02-04 leaves B10-09 and is not re-homed in B10-Z. It is a held design with no builder: its remaining build is a vacancy motive for a superior's `revoke`, which H-207's ruling bars as a special case ('just say no for now'), and no position builds the trigger (a computed `revoke` executing: 0 of 19, refused at `verb_table.yaml:1102`). CP-T02-03 loses its second reader and stands alone (AM-B-09). Reopens when a computed `revoke` executes in a seed 0-2 run.
- **Taken:** [ASSUMPTION; medium; Jordan to correct; revert: restore the row to B10-09 after CP-T02-03]
- **Because:** As drafted, AM-B-10 held CP-T02-04 in B10-Z on `BLK:H-207`; a gate on a trigger nothing builds never opens.
- **After the attack:** Rejected as drafted: the gate named a hole whose remaining build is a vacancy motive, not `revoke`, and B10-Z's gate expects a ruling nobody is asked for. Replaced by a cut with a stated reopen condition.

### CP-T02-08 — CUT (?) · AM-B-14

- **N-line after:** none: cut.
- **Override:** CP-T02-08 is removed. Its one live sentence (the Act interface shows the true odds, from `odds_of(w, act)`, through a closure over the client's own World) is already CP-T01-03's N-line and `01:105`. The AQ-X1 row and the "Blocked" line in the Jordan queue stop naming a T02 odds reader; CP-T01-03's believed-odds mode is withdrawn (AM-B-03).
- **Because:** YES — `02:282-295`: "No odds function. T01 owns the one odds reader …; this item is the Act interface's contract for it … the TRUE odds … AX-7's reading"; `01:105`: "This is the **player's Act-interface display**: AX-7 binds the character, not the player, and no state is hidden from the player (`01_AXIOMS.md:299-304`)"; `01:110`: "The Act interface … calls mode (a)".

### CP-T05-05 — CUT (?) · AM-D-06

- **N-line after:** none: cut.
- **Override:** CP-T05-05 leaves B10-13. Nothing is built. Disposition kept at `-07` §2: reopens when IN-12 (B10-09) builds `interrogate` on H-226's route and `arrest` has executed once in a seeded run. One requirement is carried to IN-12's builder, because it costs nothing now and cannot be added later without a row edit: `interrogate`'s band kinds must be one kind per band (not one `confession.made` at two bands), since CP-T05-02's `hearing` counts a kind emitted at several bands as 0. CP-T05-02's `hearing` reads `interrogate` kinds only after that row exists (its home says so); no change to CP-T05-02's code.
- **Because:** YES — `grep -c interrogate engine/season/verb_table.yaml` = 0 (no row). `hole_register.yaml` H-226 (:4760-4771): `interrogate` "HAS NO SITE … SO THE ROW IS NOT BUILT", `grade: measured`, `default: "no interrogate row: confession.made is no event kind"`; route (a) was built and reverted, the choice between (a) and (b) is the orchestrator's.

### CP-T06-06 — CUT (?) · AM-D-12

- **N-line after:** none: cut.
- **Override:** CP-T06-06 leaves B10-14. The capability keys for `research`, `examine` and `surveil` are a naming choice for whichever position first writes them (REM-30; CP-T01-01's `verb_capability` rows wait for that writer, AM-B-01), with R3's explicit-row rule unchanged. The producer problem (capability empty, J-13 / JQ-2) is not FI's. No other handle cites CP-T06-06. Strike F06 §1 row G's last clause and §3 row 06; no code, fixture or roster is touched.
- **Because:** YES — F06:174 itself: "FALSE N-LINE AT HEAD … Its N-line is T01 CP-T01-01's anyway … this item is only the key's name. Without a producer CP-T06-06 is inert"; F06:131 "`Person.capability` is empty on every realm person"; the orchestrator's content note: capability 0 of 83, `VOCATIONS = {'copying'}`, `VERB_CAPABILITY = {tell: copying, speak: copying}`.
- **After the attack:** The cut stands on 'no mechanism: a key name inside T01's rows'. 'Capability is empty on all 83' was dropped from its reason, because CP-T03-03 and -04 rest on the same empty capability and are kept.

### CP-T07-01 — CUT (?) · AM-E-01

- **N-line after:** none: cut.
- **Override:** CP-T07-01's seeding half is deleted; `cast.thread_sensitivity_of` already seeds `Person.thread_sensitivity` (None = UNKNOWN, cannot attempt). The actor adapter (oracle reads `.spirit .focus .ts .history .resilience`) becomes the first function of CP-T07-02's host `seam/wrappers/threadwork.py`: `ts` = `Person.thread_sensitivity`; `spirit` = the oracle default 4 and `history` = 0 until JQ-2 / J-T1 rule a stored Spirit (the T01 `faculty` registration rides CP-T01-01's seam if it lands; the adapter reads it by name, no parallel read); `resilience` absent until WR-01's slot is ruled. JQ-2's gate moves from CP-T07-01 to this adapter. Control for the whole file: `thread_sensitivity_gate` swept to 999, not `ts_seed: none`.
- **Because:** YES — `data/cast.py:283-304`: `thread_sensitivity_of` takes an int, a range (low end, via `_TS_RANGE`), `~N` (via `_TS_APPROX`), and returns `None` for null/absent ("`None` is NOT 0", docstring); `harness/populated.py:1040` calls it once per person at build; `engine/season/tests/test_k3_thread_sensitivity.py:149-155` pins both parse and refusal.

### REM-40 — CUT (?) · AM-A-02

- **N-line after:** none: cut.
- **Override:** REM-40 is withdrawn: its design shipped as SC-02 `23` (`rosters.yaml: fold_kinds`, `data/verbs.py::EVENT_KINDS`, `loop/resolve.py::_act_events`) and loader invariant 4 (`data/verbs.py`, empty `emits_on_refusal` on a failable row). The four rows with an empty column cannot refuse on a declared clause (`conceal`'s no-op mint falls to the flat `act.refused`, `verb_table.yaml:257`), so they declare nothing and reach only `fold_kinds`' flat kinds. `OBSTACLE_CLAUSE` is not built: S27.4 is unreachable from the chooser. The `row is None` branch of `_refuse_party_gap` keeps its fallback. REM-20's comment fix is dropped with it (`verb_table.yaml:89-91` already describes the shipped roster). The REM-40 re-records the home lists (test_season_shape.py:911, :5493, test_g1b_attribution.py:260, probes.py:2795-2802) are not made.
- **Because:** PARTLY — , and what survives does not survive. Opened: `rosters.yaml:1170-1190` (`fold_kinds`: ineligible, refused, attempt_refused) and `loop/resolve.py:88, 229, 302, 321, 507, 738, 1005, 1217` all read `FOLD_*`, so the literals are gone (the home's step (i) of the census). Step (iii) (`_admits` emits `row.refusal_for(ELIGIBILITY_CLAUSE)`) is shipped at `resolve.py:226-229`.
- **After the attack:** The cut stands. 'The four rows cannot refuse' was too strong; reworded.

### REM-41 — CUT (?) · AM-A-01

- **N-line after:** none: cut.
- **Override:** REM-41 is withdrawn. Loader invariant 7 is built where the game's Events are made: `data/verbs.py::EVENT_KINDS` (derived from every emission column plus `rosters.yaml: fold_kinds` and `logged_kinds`) held at `loop/resolve.py::_act_events`. The residual gap H-220 records (probes and tests appending undeclared kinds directly to the log) is accepted, not built: it is load-bearing on process only. No `kinds=` parameter on `EventLog`, no `Forbidden` raise at `append`, no report-mode measurement run. If a game emitter ever appends an undeclared kind, H-220 reopens at that emitter. `matter.py`'s three direct appends (`:105`, `:234`, `:297`) are game emitters that bypass `_act_events`; they emit declared kinds and nothing checks it, so `architecture/meta/04_CODE_ARCHITECTURE.md:496` ('the log accepts no other kind') stays unmet. That is a Layer 1 edit owed, listed under IN-44. `-06` does not mark H-220 ACCEPT.
- **Because:** YES — `engine/season/data/verbs.py:1198` `EVENT_KINDS = derive_event_kinds(VERB_TABLE, MATRIX, FOLD_KINDS, LOGGED_KINDS)`; `loop/resolve.py:1176-1182` raises `InstrumentDefect` when `EVENT_KINDS` does not cover the fold's kinds; `rosters.yaml:1170-1206` declares `fold_kinds` and `logged_kinds` (the matter.py `standing.band_crossed` kind); `hole_register.yaml:4684-4692` (H-220) says the undeclared kinds left are probe/test Events appended directly to the log.
- **After the attack:** The cut stands. The draft's reason, that only a probe or a test could catch an undeclared kind, was false: three game emitters append unchecked. `-07` and `-06` reworded.

### REM-51 — CUT (?) · AM-A-03

- **N-line after:** none: cut.
- **Override:** REM-51 and the `hunger_reach` fixture are withdrawn; no `HUNGER_PREDICATE`, no Observation attached at `loop/matter.py`, no second `transfer` source. Hunger reaches a person only as the shipped shortfall claim (IN-22) and through the body (REM-52, held at M6). Reopen condition: M6 answered with a magnitude at which REM-50's census reading shows a settlement under 2 seasons of cover in the realm, or REM-52 ships `body_step` above 0 (at 10 the producer is the season-0 `body.changed` of all 37 cohorts, and season 0 has no larder write for IN-22's shortfall claim to ride, so the dominance claim holds only at `body_step` 0). The rebuild then compares the band at the post-yield write too, so a recovery is sent, and is measured against the shortfall reach as its control. REM-44's Layer 1 hunk (rem-03:144-145) promises 'the claims a person holds about' hunger; with REM-51 cut only shortfall claims exist, so that sentence is reworded to 'the shortfall claims' when M11 lands it.
- **Because:** YES — Opened `loop/matter.py` (line numbers have drifted; found by symbol): the shortfall Observation rides only `w.write("stores", ...)` of a rung with a debit, `observed=short_seen.get(rid, ())` (:660-672), and the comment at :544-558 states a never-stocked larder drains no rung, so nothing carries the gap.
- **After the attack:** The cut stands. The reopen condition was too narrow (REM-52 is REM-51's producer), and REM-44's hunk could not stay 'true' as drafted.


## 4. Lane findings that changed nothing

| handle | block | why nothing changed |
|---|---|---|
| REM-42 | AM-A-21 | YES — `engine/dice_engine/dice_engine.py:174-175` `_MU_PER_DIE = 0.40`, `_SIGMA_PER_DIE = 0.800`; `sigma_leverage.py:77-78` `PER_DIE = {7: (0.40, 0.800)}` and `:112-113` `MU_PER_DIE = 0.40`, `SD_PER_DIE = 0.80`. Same values (0.80 and 0.800 are equal). `SIGMA_N_COEFF` is a different quantity (`:199`), as the home says. |
| REM-45 | AM-A-23 | YES — `systems/threadwork/sim/operations.py` `history_contrib = min(3, history + 3)`: for any history >= 0 the value is 3, so `history` never changes the pool. The docstring quotes PP-624 as "(History + 3 constant, capped +3D from level)". The home's gate (verify PP-624's formula by hand first) is in the plan card by `B-S`. |
| REM-46 | AM-A-24 | YES — `git ls-files engine/season/runs` lists `TRACE.txt` and the eight `.md` logs (`ASSUMPTIONS`, `CASELOG_ARC`, `CASELOG_NPC`, `DECISIONS`, `PROBES`, `STEPS`, `UNMAPPED_ARC`, `UNMAPPED_NPC`) beside `results.json`, which stays; `harness/report.py:305` writes `TRACE.txt`; the only test references to the others are comments in `test_season_shape.py`. |
| REM-47 | AM-A-25 | YES — `tools/evacuation_plan.py` exists and `tests/valoria/test_engine_params_bridge.py:108` lists `'tools/evacuation_plan.py'`; the card's row already says to remove it from `AUTHORED_PARSERS` there and notes the test fails on a gone entry. |
| REM-26 | AM-A-12 | YES — rem-02:439-448: "measure first with REM-11 at `aperture 1 s`", build only if the non-Rung share is larger than the 7 UNKNOWN reads and a step-5 critic passes the per-row `referent_source:` column; hash none unless built. |
| REM-28 | AM-A-14 | YES — rem-02:475-490: read REM-11's referent classes and REM-14's predicate clause per verb, "decision rule, categorical, no threshold": a KIND failure is a formation defect (class it as REM-22 does, or record the residue where the valid referents span several classes), a learnable STATE refusal stays. |
| REM-2A | AM-A-16 | YES — rem-02:520-531: "No fix is designed here"; the reading names one cause per refusal class or records it. |
| REM-2B | AM-A-17 | PARTLY — rem-02:533-542 names the prior revert ("its refused attempts moved the seed-0 trajectory", IN-33) and requires only the checkpoints' own hand-built proofs plus a declared trajectory move (`Not required: a realm execution`). |
| REM-44 | AM-A-22 | YES — `decision/choose.py::urgency` (`:217-238`) returns `float(subsistence) / condition_scale` with no candidate in it, and its docstring says it is inert by construction; `benefits_me` (`:195-214`) has no multiplier ("NOTHING MULTIPLIES THIS YET"). |
| REM-30 | AM-A-18 | PARTLY — the plan card (B10-10) states the exit (a creation arm switched off reproduces the pre-build hash) and D-2 (the design stays held; the build PR lists IN-46 and IN-47 as held back). The design file `proposals/2026-10-07-character-sheet-spaces.md` was not opened by the lane or by me. |
| REM-31 | AM-A-19 | PARTLY — card and rem-02:570-589 agree on the exit (AUTOMATED and PLAYABLE-with-scripted-choices-equal-to-the-chooser's end at one `content_hash`; the permutation falsifier with a scripted callback). Design `proposals/2026-10-07-grid-mode-suspension.md` not opened. |
| CP-T06-08 | AM-D-15 | YES — F06:150, :176: the item's N-line is "the counter-move to CP-T06-01" (burning the cover Record ends the cover, `attribution.py` "he holds it", and refuses a later `research` of it). AM-D-07 keeps the cover half, which is the half the burn counters, so the contingency survives the narrowing. |
| CP-T07-06 | AM-E-06 | YES — `write_matrix.yaml:190` states the fourth-clock bar; `state/world.py:1014-1017` admits `(Person, coherence)` only with `driver="Seam"`; the projection writes nothing on its own. Its staleness limit is stated at T07:486. |
| CP-T07-10 | AM-E-10 | PARTLY — `verb_table.yaml:1519-1535` `thread_read` forms on a `Rung` referent with `presence:<site>`; the plan already needs CP-T07-02 and CP-T07-03. The reader gap is the same as AM-E-14's for `requisition`: nothing in computed play reads `finding.made` for a decision. Not a design fault of the item. |
| CP-T07-11 | AM-E-11 | YES — T07:374-376 and §7 state the thinness; the plan orders it last and needs CP-T07-03. 4 TS>=30 persons: `cast.py` parse over `npc_registry.yaml` (lane count upheld). |
| CP-T08-03 | AM-E-14 | YES — remediation `-03`:325-345 defines `A(S)` = sum of `Rung.stores` over the subtree and `cover = A / D`; spoilage lowers `stores` through the existing `stores` write at MATTER (`loop/matter.py` wear step), so REM-50's `hunger` sees it with no new reader. Ships all-zero rates. |
| CP-T09-06 | AM-F-18 | YES — home `:336-341` cites `offices.yaml:196-204` (post Duke, `conferral: null`) and `:43-44` (the "JUDGMENT CALL" note); the lane's `confer` count is the code-report's (not re-run). The item is data only and needs IN-53 and IN-61 in the plan. |
| CP-T09-08 | AM-F-19 | YES for the diagnosis — home `:400-410`: `dispatch` is rebuilt to relocate an obligee through `_relocate`; the gate admits it only through the MUSTER basis (`state/gate.py:865-888`, a `commit` to the seat's faction, plus CP-T09-07 (b)'s `oblige` clause). |
| CP-T10-04 | AM-F-06 | YES — the `-03` rows read: CP-T03-07 needs `CP-T10-04, REM-52`; CP-T10-04 needs `CP-T03-07, H-211, REM-29, REM-44`. A two-row cycle. |
