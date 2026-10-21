# v9 remediation plan — closing what the adjudication found, against THE NINE (rev. 4: three rulings recorded; settlement hunger designed)

## Status: PROPOSED. Merging this file ratifies nothing: every item, ask and edit below is HELD BACK (ED-1094's loud exception). Jordan ratifies or adopts item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2: one active plan per lane). On adoption its items become v9 positions and these files are deleted with a `FORK:` row.
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. It moves no row of THE NINE; a row moves only on its own `measured:` block.
## Parts, in reading order: `2026-10-21-v9-remediation-01-verdict-and-coverage.md` → `2026-10-21-v9-remediation-02-items-rb0-to-rb3.md` → `2026-10-21-v9-remediation-03-items-rb4-rb5-and-index.md` → `2026-10-21-v9-remediation-04-asks-edits-measurement-and-risks.md`.

**Provenance.** Produced in one session on 2026-10-21 by agonist–antagonist relay: four readers, two independent critics on the findings, an Opus adjudication, an Opus design, and two read-only Fable critiques of the design, each folded in (change logs in §0). `SP/…` in these files names that session's scratch files. They are **not in the repository**; every figure that matters carries the command that reproduces it (§5), and the evidence it rests on is the repository's own files at HEAD `b70b5af`. Figures marked `[RELAYED]` come from commit bodies and were not re-run.

**Placement, and a conflict named.** `CLAUDE.md` §0 bars audit documents that create work for a future session, and v9's plan-edit idiom says a scratch plan is never committed. Jordan asked for this to be committed and pushed (2026-10-21), so it is, under `proposals/` (unratified work is surfaced by location, `CLAUDE.md` §3) as PROPOSED. What it changes in `engine/season/` until adopted: nothing.


Repo `/home/user/ttrpg`, HEAD `b70b5af` (shallow), 2026-10-21. Inputs:
- `SP/v9_adjudication_report.md` ("the report");
- `SP/HANDOVER_v9_findings.md` ("the brief");
- `SP/v9_remediation_plan_critique.md` ("critique 1", C-01 … C-15);
- `SP/v9_remediation_plan_critique2.md` ("critique 2", D-01 … D-11, I-01 … I-14);
- **Jordan's rulings of 2026-10-21** (D-1, D-2, L1-6), and his new requirement: *"hunger should be a thing for settlement
  cohorts"*, clarified as *"ie a settlement attribute that responds to settlement population"*.

Rev. 1, 2 and 3 are kept unchanged at `SP/v9_remediation_plan_draft.md`, `SP/v9_remediation_plan.md` and
`SP/v9_remediation_plan_rev3.md`. `SP/` = `/tmp/claude-0/-home-user-ttrpg/839b7e95-8d4d-519a-b75d-8b36aae0c7cc/scratchpad/`.
Paths without a prefix are under `engine/season/`. P1 = `workplans/valoria_master_workplan_v9.md`, P2 = `_part2`, and so on.

## 0. Verdict, and how to read this plan

**Verdict.** Even fully executed, this plan cannot make THE NINE `met`. The table below says so row by row.

- **R-01, R-02 and R-03 stay `met`.** R-01 and R-02 are re-taken twice and could fall. No item moves R-03.
- **R-04, R-05 and R-07 move upward, but no item guarantees their `met`.**
- **R-06, R-08 and R-09 are made honest, not `met`.**

**Scope.** Every input finding maps either to one of **40 items in 7 batches** or to a declined or deferred row with its
ladder step. The batches are RB-0, RB-1, RB-2a, RB-2b, RB-3, RB-4 and the new RB-5 (HUNGER); RB-3 and RB-4 each run as two
sub-batches.

**Rulings recorded (Jordan, 2026-10-21, §0.2):**
- **D-1 yes.** An agent lands unmarked Layer 0/1 text in the PR, stated openly.
- **D-2 yes.** RB-3 builds; the two designs stay PROPOSED and held, and their release is an optional JQ-5.
- **L1-6 option B.** `subsistence` leaves `Sensation` and the whole call chain (REM-44).

**Settlement hunger is designed (§2.5b, RB-5).**
- *What it is:* a **derived settlement Query**, `world_q.hunger(w, S)`, over the population's demand and the
  settlement's food on hand.
- *How it reaches people:* as an **observation riding MATTER's existing larder and body writes**, and through the
  **H-125 body clock shipped live at 10**.
- *What is measured:* at today's magnitudes the realm holds 21.7 → 41.7 seasons of food per settlement (run this session).
  So hunger binds only before the first yield and in scarce worlds, until Jordan sets the yield-to-demand ratio (JQ-6).

**Critical path:** RB-0 → RB-1 → {B-P ∥ RB-5} → RB-2a → RB-2b → B-Q → B-R → B-S → B-Y → RB-3b. No row of THE NINE waits on
RB-5, which runs beside B-P and must merge before RB-2a.

### THE NINE: confirmation

**Status** is from `python -m engine.season.harness.register --requirements` at HEAD `b70b5af`, run this session (exit 0:
met 3 · partial 5 · not_met 1).

**What that command checks (I-06, D-10).** `register --requirements` (`harness/register.py:657-715`) accepts
**syntactically only**: a status in the set; a non-empty `measure:` whose `-k` selects some test or whose `python <path>.py`
exists with `__main__` (a `python -m` command is not validated); a non-empty `measured:` at `met`/`partial`; a non-empty
`statement:`. It never reads what a `measured:` line says. **So the named gate for every row below is the batch critic's
read of the `measured:` line against the printed figure.**

**Move key:** **↑** toward `met`; **=** held; **↓** from a false `met` (the text becomes able to read false); **vis**
visibility only (an instrument can now see it, but the row does not move); **—** no item moves it.

| row | status | items (as in §2.9) | move | evidence when it moves (command → the `measured:` line it writes) | what still blocks `met` | owner of the block | conf. |
|---|---|---|---|---|---|---|---|
| R-01 decisions propagate | met | REM-16 | = (could fall to `not_met`) | `corpus_run` R3 + planted control; P2 §11's `wd_chunk` ×36 cells + `wd_collect` (M-7 and M-10 only) → "R-01 re-take <date>, tree <sha>: R3 n/n NPC, n/n ARC, control False→True; actor x % < 96 % at `2x3`, `none ≥ default`" | nothing, if both re-takes (after FI-01/FI-03; after RB-2b) stay < 96 % | agent | medium |
| R-02 decisions affect later decisions | met | REM-16 | = (could fall) | the same `wd_collect` run → "R-02 re-take <date>: none/actor/total x/y/z % at `2x3`" | nothing, if it stays < 96 % | agent | medium |
| R-03 scene-by-scene ticking | met | — | — | its own `measure:` (`requirements.yaml:728`: `headless --case NPC-088 --seasons 2 --seed 0`, which prints and asserts nothing, + `-k test_u2_`, five tests) is re-run at each batch close touching `loop/driver.py`/`deliberate.py` → a dated re-run line | nothing. **Rev. 3:** REM-43 is cut (DEC-11), so no item can regress it. The rev. 2 claim that R-03 was REM-43's falsifier is withdrawn: `-k test_u2_` never exercises the filter (critique 2 §1) | — | high |
| R-04 strategic/management at scales | partial | REM-03, REM-08, REM-11, REM-14, REM-22, REM-27, REM-28, REM-30, REM-31, REM-32, REM-50, REM-51, REM-52 | ↑ conj. (3); vis on conj. (1) | `aperture 4 0` per-verb lines with `Act.via` (conj. 1: P2:211-213's nine verbs); conj. (2) `mc_v18.py` absent + `test_faction_q.py` green (true today); each `scales:` row's `in_loop` with its artifact; **for the settlement row (rev. 4), REM-50's `hunger` reading in `census` and REM-51/52's seeded comparison** → "R-04 <date>: conj. (1) <each verb att/ex, via read>; conj. (2) holds; conj. (3) <rows in_loop, artifact each; settlement row: hunger bands by settlement, cohort deaths and acts against the hunger-off control>" | **Conj. (1), no item fixes it** (detail below). **Conj. (3):** the IN-46/IN-47 builds executing (D-2 is now yes, so RB-3 is scheduled); a fought field (REM-27); works (ED-IN-0297); the settlement row's owner stays IN-07 (B-T), and hunger makes that row consequential at today's magnitudes only before the first yield (JQ-6) | agent (conj. 1 readings and residues; the field; the builds); **Jordan** (ED-IN-0297, JQ-6) | low |
| R-05 all verbs built out | not_met | REM-02, REM-09, REM-10, REM-11, REM-16, REM-22, REM-23, REM-25, REM-2C, REM-28, REM-29, REM-2B | ↑ (REM-2B: three rows leave "no predicate/effect"; `examine` may leave "always refused"); sideways elsewhere | `corpus_run` "WHERE THE 46 GO" zeros, or each verb executing ≥ 1 in `aperture 4 0` → "R-05 <date>: n/n/n/n, reclassifications named" | `work`/`found`/`build` before ED-IN-0297; `succeed` (B-R), `tie / knot`, `thread_read` (B-S); an execution in computed play, which no position can promise (P1 §0.5); the roster size (D-V) | **Jordan** (ED-IN-0297, D-V); agent (v9 owners) | low |
| R-06 goals, convictions | partial | REM-05, REM-08, REM-12, REM-16, REM-51 | ↓ + vis; REM-51 = (contributor) | `decision_spread --decisions` at seeds 0-2 (the tie/outvoted split, the vectorless count) beside `corpus_run` RANKING, the `ambitions or cast` tests and `conviction_spread` → "R-06 <date>: pursuit decides p %, draw outvoted o %, vectorless v of n" | IN-38 (B-V); JQ-1's threshold; the cohorts' vectors (ED-IN-0296 (2)). **Rev. 4:** hunger gives cohorts held claims about their own settlement, but no conviction or goal. The fifth conjunct (vectorless actors) still reads false | **Jordan** (JQ-1, ED-IN-0296 (2)); agent (IN-38) | medium |
| R-07 memories, feelings, imperfect knowledge | partial | REM-04, REM-11, REM-27 | ↑ conj. 3 | the row's `measure:` + `test_told_by_channel.py::test_r07_realm_regard_differs…` (`:1945`) + **REM-11's per-kind count line** (`field.won`/`field.lost` per world, keyed by act; aperture does not print emitted-kind counts today, `aperture.py:155-169`) → "R-07 <date>: fought fields won/lost w/l at seeds 0-2; M4 stance writes n" | a `Won`/`Lost` field in computed play (REM-27, low); conj. 1 depends on `chronicle` staying (H-214) | agent | low |
| R-08 not omniscient, not perfectly rational | partial | REM-05, REM-12, REM-16, REM-51 | vis; REM-51 = (contributor) | `corpus_run` RANKING + tie ordering, U4 test, `decision_spread --decisions` over **vectored** persons → "R-08 <date>: ties among candidates with a reason t, all between equal nonzero scores: yes/no" | [UNVERIFIED at HEAD] whether celled candidates still tie at zero for vectored persons; if they do, the cells are the CELL-VALUE pass's. **Rev. 4:** cohorts and governors act on HELD and possibly stale hunger claims (REM-51), which is non-omniscience by construction (AX-2). No `met` conjunct reads it | agent (the reading); **Jordan** (cells) | low |
| R-09 chains probabilistic | partial | REM-06, REM-08, REM-13, REM-15 | ↓ + vis | `pytest -k test_we_only_a_verb_that_declares_contests_can_be_graded_today`; `headless --seasons 2 --seed 0` (two persons, different pools); `corpus_run` DEGREES RESOLVED BY VERB + BANDS THAT DIFFER; `storybar --draw-seeds` (choice only) → "R-09 <date>: …" | J-13's remainder with JQ-2; `determine` at ≥ 2 differing bands in the corpus (mostly Failure, `[RELAYED]`); the `headless` world seats no `capability` (P2:409) | **Jordan** (J-13, JQ-2); agent | medium (that it stays partial) |

**R-04 conjunct (1), in detail.** At HEAD, `aperture 2 0` (realm, att/ex): `requisition` 4/0, `confer` 0/0,
`establish` 0/0, `revoke` 5/0, `convene` 3/0, `determine` 0/0 (`SP/aperture_2_0.txt:92-120`). The dated 4-season reading
(`requirements.yaml:807-808`, an older tree) had `convene` 12/2 and `determine` 20/1. `via` is read for `issue` only
(`:812`). At HEAD's 4-season horizon this is unmeasured until M-13. REM-11 and REM-14 make each refusal's deciding
clause a repo reading (I-05). Any KIND failure among them closes under REM-28 (a); a STATE failure stays v9's residue
(H-163, H-207, IN-10 lineage).

**Honest summary.** No row moves to `met` by this plan's items alone. R-03 has no item. R-04 conjunct (1) has only
readings. The `vis` rows gain an instrument that can observe the failure, which is what (c)-class items buy, and nothing
more.

### 0.0 Change log, rev. 4 (Jordan's rulings and his hunger requirement, 2026-10-21)

| id | what | evidence opened | what changed, and where |
|---|---|---|---|
| R4-1 | **D-1 RULED yes** | Jordan, 2026-10-21; `CLAUDE.md:16` ("(RULED) marks a rule as Jordan's, not agent-revisable") | Unmarked `CLAUDE.md` and `architecture/` text is agent-landable in the PR, stated openly in its body. (RULED) text stays Jordan's. **Rev. 3's conditionality is removed:** DEF-9, L0-1, L1-1, L1-3 and L1-4 land as items' hunks (§4.2) |
| R4-2 | **D-2 RULED yes** | Jordan, 2026-10-21; P4:34, :41 | RB-3 is scheduled with no gate. **[ASSUMPTION]** The two designs stay PROPOSED and held under ED-1094's loud exception until Jordan ratifies them, and each build PR lists both as held back. JQ-5 is reduced to that one optional, non-blocking release |
| R4-3 | **L1-6 RULED option B** | Jordan, 2026-10-21; `state/carriers.py:387-399` (`Sensation`: "EXACTLY TWO SCALARS", `standing` raises at use); `loop/deliberate.py:434-470` (`_inputs_fingerprint` carries `subsistence`); `harness/probes.py:142-149` (`SUBSIST` reads the home larder) | REM-44 is rewritten: one commit deletes `urgency`, `benefits_me` and the whole `subsistence` chain, with every edit site listed, the re-pin declared, and a falsifier and control. Its Layer 1 amendments (04 §B.10, §C.3; 01 §D.10) ship in the same PR (L1-6, L1-7) |
| R4-4 | **New requirement: settlement hunger** | `loop/matter.py:340-470` (the draw, the shortfall record, the body pass); `queries/world_q.py:900-1040` (`subsistence_draw`, `demanded`, `delivered`), `:1145` (`population`), `:1193` (`capacity`); `data/fixtures.py:567` (`body_step=0`, H-125 swept 0/10/67); `decision/budget.py:59-76` (the body band cuts the scene budget); `cohorts.yaml` header (weight 2, authored, ED-WR-0011 option A); `01_AXIOMS.md` T-a (`:325-331`) and §D.10 (`:1115-1124`); the IN-22 live-arm tests (3 passed, run this session); a realm measurement run this session (§2.5b.1) | §2.5b designs it. RB-5 holds three items (REM-50, REM-51, REM-52). New ask JQ-6 (the magnitude). The coverage, index, K-rows, critical path and confirmation table are updated |
| R4-5 | **The analysis was moved by Jordan's clarification** ("a settlement attribute that responds to settlement population") | as above | **Before the clarification**, the routes weighed were per-cohort: the body only; a `need` question source; a candidate-dependent term on the person's interior; a pursuit or temperament vector per SE-06. **After it**, hunger is a derived SETTLEMENT Query, and two routes are dropped as no longer fitting: the interior term (a per-person value, not a settlement attribute) and the vector (an attribute of persons, and ED-IN-0296 (2)'s). The body route survives as hunger's physical consequence. The question-source route survives only as an alternative needing a ruling (§2.5b.3) |
| R4-6 | the counts | self-check §8 | 37 → 40 items; 6 → 7 batches |

### 0.1 Change log, rev. 3 (critique 2: D-01 … D-11, I-01 … I-14)

Each finding was re-opened at HEAD before acting. Totals: **ACCEPTED 19 · NARROWED 6 · REJECTED 0** (25 ids: D-01 … D-11, I-01 … I-14; a combined row counts once per id).

| id | verdict | evidence re-opened | what changed, and where |
|---|---|---|---|
| D-01 / I-01 | ACCEPTED (cut) | `loop/deliberate.py:305-359`: the filter is "the one the one-pass loop had by construction, made explicit because the tick removed the construction"; the measured cost without it (`:314-317`); it is keyed `(verb, subject[, counterparty])` and records only what was realised (`driver.py:330-351, :438, :483-498`; `data/verbs.py:1124-1161`; T4b at `tests/test_told_by_channel.py:1052-1121`). `03_VERBS_AND_LOOPS.md:136-140` ("no cap, no dedup … no already-before-this-body rule") was written for the one-pass loop, in which `pack_scenes` already spent each scene on a distinct candidate | **REM-43 is cut**, as DEC-11 (step 4: U2's own record; B4's third disposition on `03:136-140`). Removed: L1-5, M-15's REM-43 cell, the conditional ask, the R-03 claim, and every other mention. Reason: its falsifier could not observe its harm, which is an R-01/R-05 variety regression, not an R-03 break |
| D-02 / I-03 | ACCEPTED | P4:34: "deferring every fight moves the hash of any seeded season that fights, so the build re-records the seeded goldens and says so" | REM-31's hash is a **declared mover**; replay equality (AUTOMATED vs PLAYABLE) is its control; REM-31 is in K1 |
| D-03 / I-04 | ACCEPTED | `tests/test_season_shape.py:911` (`"attempt.refused" in inspect.getsource(SeasonDriver.resolve)`); `harness/probes.py:2795-2802` (`kinds.count("attempt.refused") == 1`); `tests/test_g1b_attribution.py:260` (`_FOLD_PURPOSES` names `act.ineligible:{act}`); `tests/test_season_shape.py:5493`; `harness/delta.py:94` prints `PROBE FLIPS` | All four join REM-40's declared re-records. REM-41's measure-first step runs `report && delta`. Expected: **1 flip** (the S27.4 probe) before that probe's assertion is re-recorded, and **0** after. A 0 before the re-record means `delta` cannot see the change, and is the finding |
| D-04 / I-02 | NARROWED | `verb_table.yaml:1165-1176` (`examine`: `existence` of `site` kind `Site`); `:1208-1216` (`research`: `existence` of `subject` kind `Record`); realm refusals 65 and 110 (brief §4); `SP/aperture_2_0.txt:101` (`examine` att 0) | `examine` joins REM-22 (the `Site` own-referent stamper). `research` is the new **REM-2C**, on the question's own `Record` referents (REM-21 (iv)'s body), **not** a ledger-named Record stamp. A ledger-named stamp would put every known Record on `comply`, which shares the class. REM-2C carries a stop rule over the Record-sharing rows |
| D-05 / I-13 | ACCEPTED | `SP/realm_2_0_undefined.json` §D (49), `SP/spine_2_0_undefined.json` §D (61); intersection 47; realm-only `date.scheduled`, `establish.refused` | §2.6 lists exactly the 47; the two spine-emitted kinds are dropped |
| D-06 / I-09 | ACCEPTED | `data/verbs.py:1330-1340` (`RUNG_REMIT_ACTS` from every `remit:` on a `Rung`-classed row); `verb_table.yaml:697` (`march`: `remit:dispatch`); `SP/aperture_2_0.txt:98` (25 dispatch-eligible) | REM-27 names the widening (`{issue}` → `{issue, dispatch}`, so `larders_in_purview` offers larders to dispatch holders). Its stop rule reads `requisition`'s formed count before and after. K4 names it |
| D-07 / I-14 | NARROWED | `decision/choose.py:115, :127, :217-238` (`urgency` is `subsistence`'s only reader in `decision/`); `tests/test_season_shape.py:946-952` pins `sense(p, w, subsistence)`; **04 §B.10 declares `Sensation := (subsistence, standing)`, and §C.3 lists DELIBERATE's input as "two scalars"** | Deleting `subsistence` through `sense`/`season()` would change a Layer-1-declared type, so it is not done. REM-44 removes it from `deliberation_memo` and `attribute_top` only. `Sensation.subsistence` stays declared with no reader in `decision/`, and that is recorded as L1-6 (a ruling: does `Sensation` keep `subsistence`?) |
| D-08 | ACCEPTED | P3 §B.1 B-S row: shared files include `manifest/registry.py` | K2 lists `manifest/registry.py`: RB-2a (REM-21 (v)) first, then B-S re-runs (§C.2) |
| D-09 | NARROWED | `harness/storybar.py:163` is `def drive(...)`; `tests/test_season_shape.py:2769` is `test_w5_f2s_third_term_cannot_change_any_decision`; `hole_register.yaml:368`'s cite **does** carry "EVERY CLAUSE-4 DROP IN THE WHOLE CORPUS, IN EVERY CELL, IS THE VERB `move`" (read this session) | The `drive` and `:2769` anchors are fixed. REM-29's `:368` cite stands, and `:1627` is added beside it |
| D-10 / I-06 | ACCEPTED | `harness/register.py:657-715` | §0's table preamble, §0.4 and §5.0 state the syntactic acceptance, and name the batch critic's read as the gate |
| D-11 | ACCEPTED | the coordinator's correction, 2026-10-21: the "proposed text only" wording was the orchestrator's, not the user's | §0.2 D-1 is restated neutrally with the ladder result for each side. DEF-9, L0-1, L1-1 and L1-3 are conditional on D-1. Every attribution of that instruction to the user is removed, including rev. 2's C-03 row |
| I-05 | ACCEPTED | `SP/aperture_2_0.txt:117, :120`; `predicates.py:401` | REM-28's reading list gains `requisition` and `revoke` |
| I-07 | ACCEPTED | REM-07 is the E-11 text, REM-16 its run; REM-20 is a comment that REM-40 makes true | REM-07 is folded into REM-16, and REM-20 into REM-40. The comment is corrected in REM-40's commit, so no interim text goes stale. Items 39 → 37 (with D-01's cut and D-04's REM-2C) |
| I-08 | ACCEPTED | rev. 2's RB-2 budget ⚠ ~160k against P3 §B.1's ~150k ⚠ line | RB-2 is split into RB-2a {REM-21, REM-22, REM-23, REM-24, REM-25, REM-2C} and RB-2b {REM-26, REM-27, REM-28, REM-29, REM-2A, REM-2B}, each with its own base `aperture 1 s` |
| I-10 | NARROWED | `harness/aperture.py:155-169` prints per-verb att/ex/refusal kinds, not emitted-kind counts | **Not** the scratch scan, which is no repo instrument (§0.05). REM-11 (iii) gains one count line per emitted kind per world, keyed by act; M-11 reads it |
| I-11 | ACCEPTED | `hole_register.yaml:1620-1624` (H-111: `default:` "SKIP at WITNESS for the inquiries' `finding.none`", RS-21 item 1) | DEC-12 in §1.4 |
| I-12 | ACCEPTED | `decision/choose.py:478-482, :495-497` (`declare_intents` takes `draw`); `data/fixtures.py:773` (`intent_disclosure=0.0`) | REM-15's τ = 0 control is stated to hold only at the shipped `intent_disclosure = 0.0`, and the anchor is `drive` |
| REM-32 (critique 2 §3, layer note) | ACCEPTED | 04 PART D row 38 ("every fixture injected by name from a register row") | REM-32 appends one `hole_register.yaml` row for its fixture (kind NUMBER, owner Jordan, JQ-4) |

### 0.1b Change log, rev. 2 (critique 1: C-01 … C-15), kept for the record

Each finding was re-opened at HEAD before acting. Totals: **ACCEPTED 10 · NARROWED 5 · REJECTED 0.**

| id | verdict | evidence re-opened | what changed, and where |
|---|---|---|---|
| C-01 | ACCEPTED | `state/ids.py:16-19` hashes `world_seed` into every id; `harness/storybar.py:171-174` mints act ids and builds the draw from `w.world_seed`; `rosters.yaml:579-583` (`q.id` a content hash is the last tiebreak); `seam/wrappers/combat.py:222` and `queries/world_q.py:864` draw from `w.world_seed` | REM-15 redesigned: only `draw_factory` takes the draw seed; `w.world_seed` and the act-id mint are untouched. The residue is recorded: seam and weather draws stay keyed to `world_seed`, so the arm varies the chooser's sampling only, not rolls. The `[UNVERIFIED]` tag is deleted. E-10's fourth conjunct is re-worded to match |
| C-02 | ACCEPTED | `loop/resolve.py:978` emits `("attempt.refused",)`; no `engine/season/*.yaml` declares it (only `requirements.yaml:384, :387` mention it); it is exercised by `test_season_shape.py`, `test_in50_refusals_carry_the_occasion.py`, `test_g1b_attribution.py`; `:711`'s `row is None` fallback. A grep of `loop/` and `seam/` for kind literals passed to `_act_events`/`ev(` finds only `act.ineligible` (`:75, :216`), `act.refused` (`:289, :308, :494, :711, :1175`) and `attempt.refused` (`:978`). The other literals (`matter.py`, `witness.py`, `census.py`, `calendar.py`, `effects_governance.py`) are `emits=` arguments naming matrix or row kinds | REM-40 declares the S27.4 refusal (an `OBSTACLE_CLAUSE` keyed per row), and `:711`'s `row is None` branch raises (04 PART D row 26). REM-41's measure-first step adds `python -m pytest engine/season/tests -q`. Its falsifier now plants an S27.4 act |
| C-03 | NARROWED | `CLAUDE.md:16` "(RULED) marks a rule as Jordan's, not agent-revisable"; `:30` "EDIT THIS FILE"; §2 ED-1094; `04:134-141` (an agent in-place amendment); P8:412 (IN-44: "no batch edits these files; Jordan does") | The conflict is named in §0.2 (D-1). **Rev. 3 `[CORRECTION]`:** rev. 2's resolution rested on a "proposed text only" instruction it attributed to the user. The user gave none (D-11), so D-1 is open and stated neutrally, and the four hunks that depend on it are conditional. Rev. 2 pairing DEF-9 with L0-1 as one change stands on both sides |
| C-04 | ACCEPTED | P4:41 "The hold on ratification-on-merge is released only by Jordan"; P4:34 "ratification held for Jordan"; P5:428-433, the delegated rows J-16, J-17, IN-14 and IN-52, none a held design | The step-4 precedent claim was wrong and is withdrawn. RB-3's gate is now Jordan's release (JQ-5, asked at RB-0). The default if unanswered is to wait. Named as D-2 in §0.2; REM-30/31 require the PR body to list the design as held back |
| C-05 | ACCEPTED | P5:400 (J-13: "pool only it is …"; "It's a derived score … not a character attribute in and of itself"); P5:410 "Your 2026-09-06 constraints … bind any answer" | JQ-2 re-formed: it first asks whether the constraints extend to combat and mass battle. Option (i) as a stored attribute read directly is dropped; it is re-worded as a derived pool term |
| C-06 | ACCEPTED | `loop/driver.py:71`, `decision/__init__.py:21, :96` import `urgency`; `tests/test_governance_build.py:920-935` calls `benefits_me`; `decision/choose.py:238` (`urgency = subsistence / condition_scale`) | REM-44 lists every edit site and the test that tests `benefits_me` directly; REM-12's `field_zero` is defined over the candidate-dependent terms only |
| C-07 | ACCEPTED | P3:342 "B-V against whichever of B-O…B-R is open (`rosters.yaml`)"; P3:183 | K2 gains B-V; RB-2 merges first and B-V re-runs its exit on the merged tree (§C.2). **Also found:** B-T's IN-52 edits `verb_table.yaml`'s `march` row (P3 §B.1, B-T), which collides with REM-27 and RB-4b. Added to K2 |
| C-08 | ACCEPTED | `massbattle.py:183` is `command=4`, `:196` is `_SEASON_FORCE_POWER = 4`; `verb_table.yaml:710` is `Lost`; `:948-951` are `speak`'s bands; `data/requires.py:805` `CELL_STEMS`, `:867` `LEDGER_DERIVED_STEMS = {"claim.held"}`; `hole_register.yaml:1627` (refusal reads deposited at `observation_deposit_mode: actor`; every clause-4 drop is `move` on a `contain.path` belief) | Anchors fixed in REM-32, JQ-2, JQ-4, C9, REM-06, E-7, E-10. REM-29 names the real route (`Event.observed` → WITNESS at mode `actor` → the actor's own ledger → `LedgerReader` → clause 4) and the stale-belief consequence |
| C-09 | ACCEPTED | brief findings 1, 12, 17, 21, 23, 24; `hole_register.yaml` H-185 (FORMULA), H-191 (WIRING), H-195 (WIRING); `loop/deliberate.py:116` (`_in_parallel_map`) | §1.1 gains rows for each. H-185, H-191 and H-195 are WIRING/FORMULA, so they are not JQ-3 asks; each is mapped to an owner or deferred. REM-31 gains the permutation falsifier with a scripted human callback (D-41a). REM-11 keys on the act, never the trace's `act` column |
| C-10 | NARROWED | callers of `attribute`: `aperture.py:161`, `corpus_run.py:819`, `soak.py:369`, `tests/test_fa01_head_seats.py:97` (passes `SimpleNamespace(resolved=[a])`), `tests/test_sc01_the_bar.py:161` | Worse than the critique says: five callers, one a stub. REM-10 redesigned: `attribute(w, d, n)` is unchanged; a sibling `attempts(w, n)` iterates `w.acts` through ONE shared body; the extras are separate readers. Only `aperture` and `run_case` switch |
| C-11 | NARROWED | P2:381-382 (`met` text "equal *nonzero* score (the draw breaks only true indifference)"); P2:385 (G-1: an uncelled candidate's zero "is not a tie the person has a reason to break"); 04:123 (T-l) | Both readings are stated. The plain reading is taken on G-1's precedent (ladder step 4): an all-zero field is true indifference, so the cohorts do not break R-08. **The draft's stricter reading is withdrawn.** The cohort finding moves to R-06, as a visibility conjunct (vectorless actors), still gated by ED-IN-0296 (2). R-08 is no longer conditional on it |
| C-12 | NARROWED | `sigma_leverage.py:74-80` (`PER_DIE` keyed by TN); `:197-200` ("coincide (sigma_per_die[7] = 0.800 = SIGMA_N_COEFF = 0.8)") | `SIGMA_N_COEFF` is a different quantity that coincides at TN 7, so the draft's "same alias" is withdrawn: it stays. Sonnet decides `:78`/`:112-113`; Haiku does the replacement only |
| C-13 | ACCEPTED | `grep -rl PP-624` finds it in `proposals/2026-08-23-suite-01-rulings-and-execution.md`, `proposals/2026-08-15-character-and-faction-stats-and-progression.md` and three more `proposals/` files | REM-45 names them as the hand-verification sites (resolvable, not authority). The stop rule fires only if none quotes PP-624's text |
| C-14 | ACCEPTED | P3:207 (R5: "a record file") | REM-03 (iv) and REM-16 name `engine/season/requirements.yaml` as the file each edit lands in, under R5 |
| C-15 | NARROWED | `state/carriers.py:503-506` refuses a pair carried twice; `world_q.py:2254-2256` dedups pairwise; `state/world.py:385-387`: `_entity_stores` names `Person`, `Rung`, `Office`, `Site`, `Record`, `Proposition` | The `class_of` half is verified, so its `[UNVERIFIED]` is removed. REM-21 gains one global dedup of `(id, class)` pairs across the registry, in registration order |

### 0.2 Decisions recorded as rulings (Jordan, 2026-10-21)

| id | question (as rev. 3 put it) | ruling, 2026-10-21 | what the plan now does |
|---|---|---|---|
| D-1 | Who lands Layer 0 and Layer 1 text that carries no (RULED) mark? | **Yes: an agent may land unmarked `CLAUDE.md` and `architecture/` text in the PR, stated openly. Anything marked (RULED) stays Jordan's.** | Every §4.2 row lands as a hunk of the item PR it names, and that PR's body lists it under "Layer 0/1 hunks". The rev. 3 conditionality on DEF-9, L0-1, L1-1 and L1-3 is removed. Rev. 3's `[CORRECTION]` stands: the "proposed text only" wording was never the user's |
| D-2 | May RB-3 build IN-46 and IN-47 while their designs' ratification is held? | **Yes: the builds may proceed.** | RB-3 has no gate beyond its file order. **[ASSUMPTION; medium; Jordan to correct]** The designs (`proposals/2026-10-07-grid-mode-suspension.md`, `proposals/2026-10-07-character-sheet-spaces.md`) stay PROPOSED and held under ED-1094's loud exception until Jordan ratifies them. Both build PR bodies list both designs as held back. Jordan can release the holds separately (JQ-5, optional; nothing waits on it). Revert: Jordan says the build merge ratifies the designs, and JQ-5 is deleted |
| L1-6 | Does `Sensation` keep `subsistence`? | **Option B: remove `subsistence` from the sensation and the call chain.** | REM-44 deletes `urgency`, `benefits_me` and the chain in one commit. L1-6 (04 §B.10, §C.3) and the new L1-7 (01 §D.10) are agent-landed in that PR, citing this ruling (D-1) |

### 0.3 How to read it

- **This is a plan, not an execution artifact** (`CLAUDE.md` §0.2): grade `paper`. Nothing here moves a row of THE NINE.
  A row moves only on its own `measured:` block. **`register --requirements` accepts that block syntactically only**
  (`harness/register.py:657-715`: the status is in the set; the `measure:` resolves; the `measured:` text is non-empty).
  It never reads the content, so the content's gate is **the batch critic's read of the `measured:` line against the
  printed figure** (rev. 3, D-10/I-06).
- **Handles are provisional** (`REM-nn`). **None allocates a ledger id**, exactly as v9 P1 §0.3 says of its own handles.
  On adoption into v9 each `REM-nn` becomes the next handle in its lane's run (IN-73 onward, SE-07 onward, …), and an
  `ED-<LANE>-NNNN` id is allocated only when the position is built (`references/id_reservations.yaml`, `CLAUDE.md` §4).
- **Owner class** follows the report: **(a)** plan edit an agent can make; **(b)** Jordan-owned ruling (survived the
  five-step ladder); **(c)** instrument or measurement defect; **(d)** tied to none of THE NINE.
- **Layer field** on every item (the user's binding requirement, relayed 2026-10-21): which layer the artifact binds
  (L0 agent · L1 how code is written · L2 the game), the `04_CODE_ARCHITECTURE.md` row / loader invariant / axiom it
  touches, whether it crosses a seam, and the one module that owns the rule (`CLAUDE.md` §8).
- **Tags:** `[ASSUMPTION]`, `[GAP]`, `[UNVERIFIED]`, `[CONFIDENCE: medium|low]`, `[CORRECTION]` as the brief uses them.
  `[VERIFIED HEAD]` = re-opened at `b70b5af` by this session.
- **Batches** follow v9's `methodology-execute` idiom (P3 §B): file-affinity, one session per batch, full suite once at
  the batch close (`CLAUDE.md` §0.4), finished positions deleted from the plan at the boundary (`CLAUDE.md` §2). The
  remediation batches are named `RB-0`…`RB-4` here; on adoption each takes a v9 batch slot by P3 §B.0's R1–R9 (stated
  per batch in §2), so no second batch scheme survives adoption.
- **This plan is a proposal for edits to v9, not a second plan.** `CLAUDE.md` §2 allows one active plan per lane; v9 is
  it. Adopting this draft means landing §4's text into v9's parts and §2's items as v9 positions, then deleting these
  files with a `FORK:` row. They are committed as a PROPOSAL, at Jordan's request (2026-10-21); see the status lines.

### 0.4 Corrections this session made to its inputs (each re-opened at HEAD)

| # | input claim | what HEAD shows | consequence |
|---|---|---|---|
| C1 | brief §4 B: acts whose verb is not a table row are "not tested through the act store (iteration unavailable)" | `state/acts.py:111` defines `ActStore.__iter__` (a tuple copy). Iteration IS available | `[CORRECTION]` Bucket B is closable by measurement (REM-10) |
| C2 | report §4 edit 9 / F-I: "v9 schedules `chronicle`'s deletion (P1:208-209)" | P1:208-210 says the deletion "is held, `hole_register.yaml` H-214: it waits on the `<rung kind>` reach channel"; H-214's `default:` is "kept, unchanged" | `[CORRECTION]` Edit 9's gate already exists. What is owed is a dependency note on R-07 conjunct 1 (REM-04), not a new gate |
| C3 | report F-L: seven MATTER/WITNESS kinds "declared only in `write_matrix.yaml`" read as a defect | `04` PART D row 25 derives the kind roster from "the matrix's `on_write`/`on_condition` **and** the table's `emits`/`emits_on_refusal`" | `[CORRECTION]` Those seven are conformant. Only `act.ineligible` is undeclared (04 §F.20b names it) |
| C4 | report F-B: extend `referent_class:` to `give` | v9 B-R's `give` + Rung step (P3 §B.1, B-R row) widens `give`'s subject to a Rung hold. A `referent_class:` is ONE class per row (`data/verbs.py:243`, `Question.referents_for`), so `Record` would forbid that widening | `give` is excluded from REM-25 and handed to B-R's step with its measured refusals (§6 risk K3) |
| C5 | report F-B, implicit: adding the column is the whole fix | a classed row forms ONLY on referents a stamper put on the question (`queries/world_q.py:2251-2259`, `_stamped`). `Site`, `Proposition` and `Person` are not in `rosters.yaml: referent_classes` (`:586`) and no stamper produces them | a class needs a roster member AND a stamp source (REM-21). Without it the row forms on nothing |
| C6 | report F-F: R-09's tightened conjunct reads `DEGREES RESOLVED` per verb | `harness/corpus_run.py:864` counts `str(e.degree)` over every Event, with no verb. The existing line cannot say WHICH verb graded | R-09's third conjunct is not machine-readable today even as written. REM-13 adds the per-verb split |
| C7 | brief finding 4: aperture "counts attempted only over `SeasonDriver.resolved`" | true. `requirements.yaml:995` already names the fix: "`w.acts` holds every one". `w.acts.append(a)` precedes `_survives` and the contest branch | REM-10 changes the iteration at the single owner, `corpus_run.attribute` (`:745-786`) |
| C8 | report F-I / brief 16: deleting `chronicle` breaks R-07 conjunct 1 | holds, but only if the deletion lands. H-214 holds it | no gate is owed (C2). R-07's row records the dependency |
| C9 | brief §6: R-07 conjunct 3 needs mass battle to resolve, which "routs on contact" | `verb_table.yaml:709-710`: `march`'s `Lost` band (`:710`) writes `Person.stance`, as `Won` (`:709`) does. A rout is a `Lost`, and it reaches `_eff_march`'s stance write | G3's weight→troop VALUE does not gate R-07 conjunct 3. Only a fought (not `Unopposed`) field does (REM-27) |

## 1. Coverage — every input finding or gap, mapped to an item or to a declined/deferred row

Key: **→ REM-nn** = an item in §2. **DEF-n / DEC-n** = deferred or declined, with the ladder step that decides it, in §1.4.
**v9** = already owned by a named v9 position; the item only edits the plan so the ownership is visible.

### 1.1 The report's findings F-A … F-L, and the brief's findings 1–25

| input | short | disposition |
|---|---|---|
| F-A (brief §2) | three rows unmeetable plus R-05 conditional; P2:38 "Both" | → REM-01 (count). Substance: R-04 → REM-03, REM-30, REM-31. R-07 → REM-04, REM-27. R-09 → JQ-2. R-05 → REM-02 |
| F-B (scan ii) | wrong-kind referents; `restore` 0/27 | → REM-21 … REM-26, REM-28. `give` → B-R (C4) |
| F-C (finding 10) | the draw decides; the `met`s cannot see it | (c) → REM-12, REM-05. (b) → JQ-1. Cohorts → ED-IN-0296 (2), already asked |
| F-D (finding 1) | denominator 46 vs 92 | (a) → REM-02. (b) → DEF-1 (D-V, held by the suite) |
| F-E (findings 6, 7) | no per-person capacity; chain not instrumented | (b) → JQ-2, JQ-3. (c) → REM-15 |
| F-F (finding 8) | graded social acts write nothing | (a) → REM-06. (c) → REM-13 |
| F-G (finding 4) | instruments undercount contested refusals | → REM-10 |
| F-H (findings 17, 19, 21, 22) | R-04's scales built, not running | IN-46/47 → REM-03, REM-30, REM-31. Fields → REM-27. Works → ED-IN-0297 (held). `seize` → v9 (IN-12 step 6's residue). Handoffs → DEF-2. Proceedings ordering → DEF-3. Investigation trail → DEF-4. `restore` → REM-22 |
| F-I (findings 15, 16) | deaths never become questions; `chronicle` sole `told_by` | → REM-04 (H-209 named on R-07). Its code → v9 B-R (H-209 `owner:`). `chronicle`: C2, C8 |
| F-J (finding 12) | character change ships dark | → JQ-3 (magnitudes). `refusal_axis` → v9 (G-3, P5:362). IN-65 → DEC-1 |
| F-K finding 5 | 44/45 stale; 21 → 17 → 16 | → REM-02 |
| F-K finding 2 | three scale vocabularies, no mapping | → DEF-5 (H-89, J.2 rank 5). REM-03 records the pointer |
| F-K finding 3 | V.2.1, V.2.2, V.2.8, V.2.12, V.2.14 | V.2.1 → DEC-2. V.2.2 → REM-2A (candidate cause). V.2.8 → DEF-1. V.2.12 → DEC-3. V.2.14 → DEF-4 |
| F-K finding 13 | FA-05, goal direction | ED-IN-0296 (1), already asked. No item |
| F-K finding 14 | self-knowledge infallible | → DEC-4. `01_AXIOMS` wording → L1-5 (§4.2) |
| F-K finding 23 | R-01/R-02 readings predate FI-01/FI-03 | → REM-16 (rev. 3: REM-07 folded in) |
| F-L finding 9 | resolution non-monotone; per-die literals | literals → REM-42 (G2a). Diagonal → DEC-5 |
| F-L finding 20 | `explain(p, v)` has no code | → DEF-6 |
| F-L finding 25 | NERS fixes not landed | → §1.3 |
| F-L `act.ineligible` | undeclared kind; false comment | → REM-40 (with the comment, rev. 3: REM-20 folded in), REM-41 |
| F-L seven matrix kinds | declared only in `write_matrix.yaml` | C3: conformant. Included in REM-41's derived roster |
| finding 11 | outcome-blindness | dropped by the report; stays dropped (ruled, `ARCHITECTURE_V2.md:510-525`) |
| finding 24 | R-03 unexamined | dropped by the report; stays dropped (rev. 3: REM-43 is cut, DEC-11, so no item touches R-03) |
| finding 18 | troop chain; season force routs | G3 form → REM-32, value → JQ-4. LF-1 vs Jordan's 2026-10-16 wording → DEF-7 |
| finding 21, second half (rev. 2, C-09) | SC-01 s11's vote-quorum conjunct unbuilt (H-161, J-4) | v9: P2:249 holds it on J-4. No item. Not on an M1 conjunct beyond R-04 conjunct (1)'s `determine`, which the THE NINE table names as v9's residue |
| finding 17, H-212 (rev. 2, C-09) | occupation counts residents, so a seat could `seize` a settlement without battle | v9: B-T's tail by R3 (P3:227-228), `absent` |
| finding 1, the R-10 rename batch (rev. 2, C-09) | renaming verbs moves goldens (act ids and draw streams hash the verb name, #482) | DEF-1: the renames are the suite's D-V decisions. When Jordan rules one, the rename is a declared golden mover in the batch that lands it (K1) |
| finding 12, `marry`/`defect`/kin (rev. 2, C-09) | uncarried | DEF-1 (suite verbs with no row) |
| finding 23, IN-71's h9 assertion (rev. 2, C-09) | the rate no longer rose above control | REM-16 records whether the arm's observable still reads above its control |
| finding 24's residue (rev. 2, C-09) | the human callback runs inside the per-person map (`loop/deliberate.py:116`); nothing specifies how it blocks | REM-31: D-41a's permutation falsifier with a scripted callback |
| F-E's H-185, H-191, H-195 (rev. 2, C-09) | an OUGHT's `predicate` read by nothing (FORMULA); intent reconciliation (WIRING); the `holder` operand under `declared` polarity (WIRING) | not NUMBER holes, so not JQ-3. H-195 matters only under `stance_polarity: declared`, which rides ED-IN-0296 (1). H-185 and H-191 → DEF-12 |

### 1.2 The report's §4 edits 1–11, §3's R-rows and §5's limits

| input | item |
|---|---|
| edit 1 (count) | REM-01 |
| edit 2 (IN-46/IN-47 builds) | REM-03 (plan text), REM-30, REM-31 (builds) |
| edit 3 (march referent; G3 row) | REM-27 (referent), REM-32 (form), JQ-4 (value) |
| edit 4 (R-05 rows; IN-53 extension; 44/45) | REM-02 (rows, fix), REM-21 … REM-26 (extension) |
| edit 5 (R-05 scope; attempted fix) | REM-02 (scope), REM-10 (instrument) |
| edit 6 (draw split; cohorts annotation) | REM-12 (instrument), REM-05 (`met` text) |
| edit 7 (§J.2 rows) | REM-08 → JQ-1, JQ-2, JQ-3 |
| edit 8 (R-09 conjunct) | REM-06 (text), REM-13 (instrument) |
| edit 9 (`chronicle` gate) | REM-04. C2: the gate exists; the dependency note is what is owed |
| edit 10 (P2:182 stale) | REM-03 |
| edit 11 (R-01/R-02 re-take) | REM-16 |
| R-01, R-02 | REM-16 (re-take), then again at RB-2b's exit (§5) |
| R-03 | holds; no item (rev. 3) |
| R-04 | REM-03, REM-22, REM-27, REM-30, REM-31, REM-32; rev. 4: REM-50, REM-51, REM-52, JQ-6 |
| R-05 | REM-02, REM-10, REM-21 … REM-2B |
| R-06 | REM-05, REM-12, JQ-1, JQ-3; rev. 4: REM-51 (contributor) |
| R-07 | REM-04, REM-27 |
| R-08 | REM-05, REM-12; rev. 4: REM-51 (contributor) |
| R-09 | REM-06, REM-13, REM-15, JQ-2 |
| limit: one run, one seed | REM-16: seeds 0, 1, 2 at the TEST HORIZON (§5) |
| limit: F-C on the harness slice | REM-12 extends the split to `--season` (in-play) |
| limit: relayed figures (THE BAR, FI-03 trail, IN-72 deaths, `chronicle` 879→0, obstacle 842/844) | REM-16 re-runs each through the command that produced it, or marks it unreproducible |
| limit: F-B uses the last read | REM-11 prints the failing clause where the fold names one (`refusal_for`), else the last observed read flagged `last-read` |
| limit: "33 unmatched verbs" is a text match | DEF-1. A semantic audit of the suite is the suite's own D-V work |
| limit: files not read (suite bodies, PR bodies, diffs) | not closable by measurement. Each batch's READ-FIRST names the sites it needs |

### 1.3 The failure scan, the NERS fixes and the Layer 1 drift

| input | item |
|---|---|
| 1,102 refusal events (realm 984, spine 118); 583 (52.9 %) end on `exists:<Kind> = 0` | REM-11 (reproducible in aperture), REM-21 … REM-28; rev. 3 adds the #2 and #3 wrong-kind refusers, `research` 110 (REM-2C) and `examine` 65 (REM-22) |
| a refused inquiry re-forms every round (brief 22) | DEC-12 (rev. 3, I-11) |
| **Jordan's requirement, 2026-10-21:** hunger for settlement cohorts, as a settlement attribute that responds to population | §2.5b; RB-5: REM-50 (the Query), REM-51 (its reach), REM-52 (the body clock live); JQ-6 (the magnitude that makes it bind in the realm) |
| Jordan's rulings, 2026-10-21: D-1, D-2, L1-6 | §0.2; §4.2 (D-1); RB-3's entry (D-2); REM-44 (L1-6) |
| 244 + 8 failed writes (`NoOpReceipt`) | migrate 116 → REM-29. move 19 → REM-26. survey/forge `Record.exists` 79 + 7 → REM-28. transfer 30 → REM-2A. restore 1 (spine) → DEC-6 |
| UNKNOWN reads: `work` condition (82 + 5) | REM-22. The S12.1 dwelling/garrison residue is measured there |
| UNKNOWN reads: `move` `contain.path` (7) | REM-26 |
| UNKNOWN reads: `tell` `with` (5) | REM-11 measures it, then DEC-7 (by design, `data/requires.py:777-793`) unless the reading shows non-person `to` |
| refusals with no read: `release`, `revoke`, `dispatch`, `convene`, `march` | REM-14 (trace the deciding clause), then REM-28 (convene, release) |
| six rows the fold cannot carry | `construe`, `evade / defy`, `exchange` → REM-09 + REM-2B (restores). `succeed` → v9 IN-61 (B-R). `thread_read`, `tie / knot` → v9 B-S |
| thirteen emission-only rows | REM-13 prints the class; R-09 consequence → REM-06. `speak`'s empty bands → REM-13's decision rule (04 D-30a) |
| `act.ineligible`; false comment at `verb_table.yaml:89-91` | REM-40, REM-41 |
| 47 declared kinds never emitted in both worlds | REM-11 prints the line. Owner map in §2.6 |
| bucket B untested | REM-10 (C1) |
| NERS G2a | REM-42 |
| NERS G4 | DEC-11 (rev. 3: cut on evidence) |
| NERS G5 | REM-44. ED-IN-0261's weighting → DEC-8 |
| NERS G7 | REM-45 |
| NERS X1 | REM-46 |
| NERS X2 | DEF-8 |
| NERS X3 | DEF-9 (Layer 0 edit L0-1 first) |
| NERS X4 | REM-09 (a park note in P7) |
| NERS X5 | DEF-10 |
| NERS X6 | DEC-9 |
| NERS X7 | DEC-10 |
| NERS X8 | REM-47 |
| NERS G1, G3, G9 (cited by the report) | G1 → JQ-2. G3 → REM-32, JQ-4. G9 → REM-16 |
| Layer 1: §C.2 lists nine bases, code has twelve | already IN-44's row (P8:426). Carried as L1-2 |
| Layer 1: loader invariant 5 unbuilt (no `writer:` column in `write_matrix.yaml`, grep 0) | DEF-11. L1-3 records the honest grade |
| Layer 1: loader invariant 7 unbuilt (`state/log.py:64-104` checks no kind) | REM-41. L1-1 |
| Layer 1: §C.11 `explain` | DEF-6 |

### 1.4 Declined and deferred, each with its ladder result (`CLAUDE.md` §0)

| id | what | step that decides it | result |
|---|---|---|---|
| DEF-1 | the 46-vs-92 roster; the suite's 33 unmatched verbs (incl. `bribe`, V.2.8) | 1–4 silent; 5: a 46-verb and a 92-verb game differ materially | **held**, already queued as the suite's D-V decisions. The suite's Status line holds itself back (`…verbs-01…md:3`). No new ledger row |
| DEF-2 | the eight handoff rules (`requirements.yaml:55-58`) | 3: R-04's `met` (P2:211-217) reads no handoff; they are NERS **S** tests | deferred out of M1. SM-6 (IN-46) is the one on a row's path (REM-31). H-56 stays J.2 rank 6 |
| DEF-3 | THE BAR's ordering (4 of 72 determinations dated) | 3: P1 §1 M2 names THE BAR a candidate M2 gate, not an M1 conjunct | deferred to M2. REM-16 re-runs the figure so it stops being `[RELAYED]` |
| DEF-4 | FI-03 trail reachable only by a plant; V.2.14 inquiry yield | 3: FI-03's own design keeps the realm-finding test red on purpose (`46ec000` body) | deferred to the FI lane's owner. R-04's investigation row is re-read by REM-03 on FI-01's executions, not on the trail |
| DEF-5 | a mapping between the three scale vocabularies | 1: H-89 (J.2 rank 5) holds the `scale:` column's fate; a stored verb×scale column is refused (`verb_table.yaml:66-75`) | held at J.2 rank 5 |
| DEF-6 | `explain(p, v)` (04 §C.11) | 4: precedent "only with its first reader" (#445 K-2, P1:346); a Query no caller reads is ID-13 | deferred to M3, where the UI is its first reader |
| DEF-7 | LF-1 (troops bounded by treasury) vs Jordan's 2026-10-16 wording | 1: LF-1 is DELEGATED-RULED (P5 J.2 ask-then, IN-52) and tagged revertible | carried; IN-52 ships OFF. Not an M1 conjunct |
| DEF-8 | NERS X2 (move R-01/R-02 narrative out of `requirements.yaml`) | 5: it would rewrite the `measured:` blocks RB-1/RB-2b must append to | deferred until after RB-2's R-01/R-02 re-take |
| DEF-9 | NERS X3 (delete `params_tables.yaml`) | `CLAUDE.md` §5 names the file; deleting it alone leaves Layer 0 pointing at nothing | **rev. 4: no longer deferred (D-1 RULED yes).** The deletion, its `FORK:` row and L0-1's sentence land as one agent-landed change in RB-4a's PR, stated openly. It is listed here only for the record; it is RB-4a's work, not a deferral |
| DEF-12 (rev. 2) | H-185 (an authored OUGHT's `predicate` does nothing) and H-191 (intent reconciliation read by nothing) | 3: neither is read by any R-row's `met`; both are `hole_register.yaml` rows with named owners (`queries/world_q.py` Q4; `decision/options.py::record`) | deferred to their owners; not M1 |
| DEF-10 | NERS X5 (move `build_realm` out of `harness/`) | 5: no module owns world-gen yet (04 PART E step 9), and "no new directory" binds | deferred; not M1 |
| DEF-11 | loader invariant 5 (`writer:` column) | 3: 04 §B.13 decides it, so it is agent work; but it is on no R-row's path and `CLAUDE.md` §0 scopes session work to M1 junctures | deferred. L1-3 states the honest grade meanwhile |
| DEC-1 | IN-65's pursuit-scar writes read by nothing at the shipped shift | 1: H-187 (the shift's magnitude) owns it | no item; JQ-3 carries H-187 |
| DEC-2 | V.2.1 (value term reads the verb only, `decision/choose.py:149`) | 3: the score shape is ruled Layer 1 (`ARCHITECTURE_V2.md:510-525` §F2) | declined |
| DEC-3 | V.2.12 (`faction_q.at_war` has no reader) | 2/3: 04 §B.10-12 declares the Query; its readers arrive with faction war (FA-07, LEAVE). No R-row reads it | declined; not dead by defect |
| DEC-4 | the actor's own deposit is unrefracted (`loop/witness.py:599-606`) | 3: AX-7 row (2) permits a self-reading mechanism and does not owe one | declined. L1-5 proposes G6's narrowing text |
| DEC-5 | non-monotone P(Partial+) along the equal-score diagonal | 1: Jordan's ruled "score/2" (`roll.py:67-69`); G2d is the PC lane's [medium] | declined here; bears on none of THE NINE |
| DEC-6 | the one spine `restore` `NoOpReceipt` (a Site already at its band) | 4: 04 §C.4 "a refusal emits"; the WRITE clause carries a declared kind | declined: a lawful refusal, one case |
| DEC-7 | `tell`'s `with` = UNKNOWN (5) | 3: `data/requires.py:777-793`, "UNKNOWN is never a contradiction … the fold refuses an absent hearer" | declined unless REM-11 shows a non-person `to` (then it joins REM-24's class) |
| DEC-8 | ED-IN-0261's self/other weighting (G5's condition) | 5 survives, but nothing on a row waits on it | not asked; REM-44's deletion is reversible and decides nothing |
| DEC-9 | NERS X6 (move 1,017 ED rows to archives) | `CLAUDE.md` §0.1 pt 5: load-bearing on process only; §0 scope | declined |
| DEC-10 | NERS X7 (retire process checks) | changes the protected branch's blocking set: a PR Jordan reviews | declined from this plan; it is not on THE NINE |
| DEC-11 (rev. 3) | NERS G4: delete `_drop_what_was_already_done` (was REM-43) | 4: the filter is "the one the one-pass loop had by construction, made explicit because the tick removed the construction" (`loop/deliberate.py:308-312`), and its absence was measured as one person repeating their top three five times a season, with seven verbs gone from the world (`:314-317`). B4's third disposition on `03_VERBS_AND_LOOPS.md:136-140`: "no dedup" was written for the one-pass loop, in which a person never spent two scenes on one identical opportunity either. The filter bars only a REALISED identical opportunity, keyed `(verb, subject[, counterparty])` (`data/verbs.py:1124-1161`) | declined. If a later reading shows the filter barring a non-identical opportunity, re-open it with that reading |
| DEC-12 (rev. 3) | brief 22: a refused inquiry re-forms every round (`research` formed 83, refused 110) because nothing is learned | 1: H-111's `default:` (`hole_register.yaml:1620-1624`) is "SKIP at WITNESS for the inquiries' `finding.none`" (RS-21 item 1, [medium; Jordan to correct], built at FI-01) | declined. It is REM-29's learn-by-failing channel deliberately off for `finding.none`. REM-22 and REM-2C remove the wrong-kind half of these refusals; the right-kind re-forming stays by that ruling's design |
