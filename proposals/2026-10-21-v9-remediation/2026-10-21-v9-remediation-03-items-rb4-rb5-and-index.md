# v9 remediation proposal, part 3: items: RB-4, RB-5 (hunger), owner map, ordering, index

## Status: PROPOSED. Merging this file ratifies nothing: every item, ask and edit below is HELD BACK (ED-1094's loud exception). Jordan ratifies or adopts item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2: one active plan per lane). On adoption its items become v9 positions and these files are deleted with a `FORK:` row.
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. It moves no row of THE NINE; a row moves only on its own `measured:` block.
## Parts, in reading order: `2026-10-21-v9-remediation-01-verdict-and-coverage.md` → `2026-10-21-v9-remediation-02-items-rb0-to-rb3.md` → `2026-10-21-v9-remediation-03-items-rb4-rb5-and-index.md` → `2026-10-21-v9-remediation-04-asks-edits-measurement-and-risks.md`.

### 2.5 RB-4 · LAYER 1 CONFORMANCE AND THE NERS FIXES (class d)

**RB-4a (pre-B-S, hash-neutral or golden-only; R9 lanes, no shared files):** REM-42, REM-45, REM-46, REM-47. Opens after
RB-1; merges before B-S, because B-S plugs `systems/threadwork` and should plug the corrected formula. **RB-4b (after
B-Y, beside B-T; R1 because it edits `verb_table.yaml` and `loop/resolve.py`):** REM-40 → REM-41 → REM-44.
**Tier:** Sonnet producers; Opus critic on REM-40 and REM-41 (a runtime refusal on the log).

**REM-40 · Retire the fold's body literals: every row declares its refusal kinds (rev. 2, C-02).** closes F-L
`act.ineligible`, 04 §F.20b (F13), the `act.refused` fallbacks (`resolve.py:289, :308, :494, :711, :1175`, emitted 0
times), and the S27.4 `attempt.refused` literal (`:978`) the draft missed. R: none. class (d). Layer: Layer 2 code and
data. It touches loader inv. 4 widened (F7: "each conjunct … and any eligibility alternative that can decline"), ID-12
("a definition living as a literal in a body"), 04 §F.20b's first option ("declared columns") and PART D row 26 ("every
table lookup raises on a missing key"). No seam. Owner = `data/verbs.py::_load_verb_table` (the load refusal) and
`VerbRow.refusal_for`.
**The literal census (grep of `loop/` and `seam/` for kind literals passed to `_act_events` and `ev(`):** `act.ineligible`
`:75, :216`; `act.refused` `:289, :308, :494, :711, :1175`; `attempt.refused` `:978`. Nothing else. Every other kind
literal in `loop/` (`matter.py`, `witness.py`, `census.py`, `calendar.py`, `effects_governance.py`) is an `emits=`
argument naming a matrix or row kind, and REM-41's report-mode run checks those against the derived roster.
change:
(i) The three rows with an empty `emits_on_refusal` (`create_record` `verb_table.yaml:206`, `tie / knot` `:1291`,
`utter` `:1323`) each declare one, in the house form `<verb>.refused`, with the coinage defined in the row's note
(`CLAUDE.md` §4).
(ii) The loader refuses a row whose `emits_on_refusal` is empty.
(iii) `_survives` (`:75`) and `_admits` (`:216`) emit `row.refusal_for(ELIGIBILITY_CLAUSE)`.
(iv) **S27.4:** a new `OBSTACLE_CLAUSE` beside `ELIGIBILITY_CLAUSE`/`WRITE_CLAUSE`. `:978` emits
`row.refusal_for(OBSTACLE_CLAUSE)`. A flat row answers its flat tuple; a KEYED row must key `obstacle`, and the loader
refuses one that does not (the per-clause half of inv. 4, `data/verbs.py`). [UNVERIFIED]: how many keyed rows need the key;
the builder reads them at load. [ASSUMPTION; medium] that a per-row kind is right for an attempt-level refusal. The
alternative is one declared `attempt.refused` kind in every row's keyed or flat column, and it is rejected because it
re-creates one kind for every verb under 46 names.
(v) `:711`'s `row is None` branch **raises** `Unspecified` (PART D row 26), instead of emitting the literal or an empty
tuple (a silent drop). An act naming no verb row is a defect in the act; REM-10's `unrowed_acts` reads 0 in play.
(vi) The `or ("act.…",)` fallbacks become unreachable and are deleted, not kept as dead code (ID-13).
falsifier:
- A planted row with an empty `emits_on_refusal` refuses at load.
- A hand-built act whose actor a predecessor killed emits the row's refusal kind.
- A hand-built act with `obstacle > multiple × pool` emits the row's `OBSTACLE_CLAUSE` kind.
- A hand-built act with verb `"zz_not_a_row"` raises at `_refuse_party_gap`.
- Mutation: restore any literal, and REM-10's `foreign_kinds` reader shows it again.
- Control: base realm 31 `act.ineligible` and spine 1; after, 0.
- **Re-records, declared (rev. 3, D-03 — every site that names a retired literal):**
  - `tests/test_season_shape.py:911` (a SOURCE pin: `"attempt.refused" in inspect.getsource(SeasonDriver.resolve)`)
    becomes a pin on `OBSTACLE_CLAUSE`.
  - `tests/test_season_shape.py:5493` (`"attempt.refused" not in kinds`) names the row's obstacle kinds.
  - `tests/test_g1b_attribution.py:260` (`_FOLD_PURPOSES = ("{kind}:{act}", "act.ineligible:{act}")`) loses its
    second member, since `{kind}:{act}` covers the row kinds.
  - `harness/probes.py:2795-2802`, a PROBE asserting `kinds.count("attempt.refused") == 1` on an `utter` act. It
    re-records to `utter`'s new `OBSTACLE_CLAUSE` kind (REM-40 (i) gives `utter` one).
  - `test_in50_refusals_carry_the_occasion.py` and the rest of `test_g1b_attribution.py` (the S27.4 kind).
  - The Event id changes with the kind (`requirements.yaml:387`).
- **The comment at `verb_table.yaml:89-91` is corrected in this commit (E-13; rev. 3, I-07: REM-20 folded in).** It
  then describes the code as it stands after the commit.
hash: **mover** in the realm (the `act.ineligible` Events change kind and WITNESS deposits claims on them). The S27.4 path
is hash-neutral in computed play, since the chooser never sets an obstacle (`resolve.py:976`). revert: one commit.

**REM-41 · Build loader invariant 7 at the log: `append` refuses an undeclared kind (rev. 2, C-02).** closes Layer 1
drift (inv. 7 unbuilt; PART D row 25 graded MECHANICAL without a check). class (d). Layer: **a runtime refusal in game
code against a ratified invariant.** Its subject is Layer 2 and it is load-bearing on the game: an undeclared kind reaches
WITNESS and the ledgers. So it is licensed by `CLAUDE.md` §0.1 pt 5 and the skill's A3. It is not tree-wide. Owner of the
roster: ONE derived set in `data/` (verb columns ∪ the matrix's emission columns, read from their own loaders,
`data/verbs.py` and `data/matrix.py`). The log reads it through a thunk passed by `World`, the `act_ids` precedent
(`state/log.py:50-56`), so `state/log.py` imports nothing. change: `EventLog.__init__` gains `kinds=`; `append` raises
`Forbidden` naming the kind and the row it is missing from.
**Measure before landing (stop rule), in report mode (log, do not raise):**
(a) seeds 0-2 at `aperture 1 s`;
(b) one `corpus_run`;
(c) **`python -m pytest engine/season/tests -q`**, which reaches the hand-built paths no seeded run does: S27.4,
ENCOUNTER, CENSUS and the planted probes (C-02);
(d) **`python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD`** (rev. 3, D-03), in that
order, so `delta` compares against a regenerated `results.json`. **Expected `PROBE FLIPS`:** 1 (the S27.4 probe at
`harness/probes.py:2795-2802`) on REM-40's tree before that probe's assertion is re-recorded, and 0 after. A 0 before the
re-record means `delta` cannot see the change: stop and find out why (`delta.py:12-15` names its control as weak).
[CONFIDENCE: medium] on whether `delta` counts a probe assertion failure as a flip or as an error; read off `delta.py:94`
when it runs.
Any undeclared kind found is declared at its owner first, or the item stops. Run (c) is a measurement on an uncommitted
change and does not replace the batch close's one suite run (`CLAUDE.md` §0.4).
falsifier: plant `Event(kind="zz.undeclared")` → `Forbidden`. A full seeded season AND run (c), with the check raising,
complete with no raise. Run (c) is the arm that can observe the S27.4 literal, so the falsifier is not vacuous on that
path (`CLAUDE.md` §0.1 pt 2). Control: the same plant with the thunk removed appends silently. hash: equal to REM-40's.
revert: drop the thunk.

**REM-42 · NERS G2a: one owner for the per-die mean and σ (rev. 2, C-12).** closes F-L finding 9 (literals). class (d).
Layer: `engine/` Layer 2 math; `CLAUDE.md` §8 ("every rule lives once"); no seam. Owner =
`engine/dice_engine/dice_engine.py:174-175` (`_MU_PER_DIE`, `_SIGMA_PER_DIE`, TN 7).
change: `sigma_leverage.py:112-113` (`MU_PER_DIE`, `SD_PER_DIE`) and `:78` (`PER_DIE = {7: (0.40, 0.800)}`) read the
owner's values, through a public alias where the owner's names are private. `PER_DIE` stays a TN-keyed dict, because
`:74-76` says a stray TN must fail loudly with a `KeyError`. Only its TN-7 entry's values come from the owner.
**`SIGMA_N_COEFF` (`:105`) is NOT aliased.** `:197-200` says it coincides with `sigma_per_die[7]` at TN 7 and is a
different quantity (σ_N's coefficient), so the draft's "same alias" is withdrawn.
**Tier split (C-12, `CLAUDE.md` §10, never tier down on a judgment node):** Sonnet decides whether `:78`'s entry is the
same quantity as the owner's and records the decision in the commit. Haiku performs the replacement.
falsifier: `rg -n '0\.40\b|0\.800\b' engine/dice_engine` finds the per-die pair defined once (the owner) and
`SIGMA_N_COEFF` once, with its coincidence docstring. A test asserts `PER_DIE[7] == (owner μ, owner σ)`. Mutation: change
the owner's μ, and `sigma_leverage` follows. `python tools/export_engine_params.py --check` round-trips. Run
`GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python tools/ci_sim_fabrication_check.py`, because a moved constant can
look new to that gate. Control: `engine/tests` goldens equal before and after (same values). hash: equal. revert: the
import.

**REM-44 · Delete `urgency`, `benefits_me` and the whole `subsistence` sensation chain in one commit (rev. 4: L1-6
RULED option B, Jordan, 2026-10-21; NERS G5).** closes G5, D-07/I-14, L1-6. class (d).
**Layer:** Layer 2 code plus the Layer 1 text that declares it, landed in the same PR per D-1 (L1-6, L1-7). 04 §A.2
(`decision/` owns nothing; it may read `Sensation`), §B.10 (`Sensation := (subsistence, standing)`), §C.3 ("two
scalars"), PART D rows 2 and 41 (no `World` in a decision), AX-2; 01 §D.10 ("a need | a `Sensation` plus a Query"). No
seam. Owner = `state/carriers.py::Sensation` (the type) and `loop/deliberate.py::sense` (its one constructor).
**What is left after it.** `Sensation` keeps one field, `standing`, which raises at its point of use
(`carriers.py:395-398`). The type therefore carries nothing readable, which is AX-2's island at its narrowest. Deleting
the type outright is not this item: the ruling names `subsistence`. That residue is recorded in L1-6's text.
**Every edit site.** Enumerated by grep this session, by file and count, and re-run by the builder before the edit:
- **the type and its constructor:** `state/carriers.py:387-399` (`Sensation`, its docstring "EXACTLY TWO SCALARS");
  `loop/deliberate.py:525-537` (`sense(p, w, subsistence)` → `sense(p, w)`), `:70` and `:119` (the `deliberate`
  parameter and call), `:465` and `:515` (`_inputs_fingerprint`'s `subsistence` term and its docstring entry);
- **the driver:** `loop/driver.py:365` (`season(self, choose, question, subsistence, …)`), `:461` (the `deliberate`
  call), and `:71` (the `urgency` import);
- **the chooser:** `decision/choose.py:112, :127` (`_URGENCY`), `:115` (`deliberation_memo`'s `subsistence`
  parameter), `:195` (`benefits_me`), `:217-238` (`urgency`), and `:448` (`deliberation_memo(p, s.subsistence, fx)`);
  `decision/__init__.py:21, :96`;
- **the harness:** every `subsistence=` keyword to `SeasonDriver.season`: `aperture.py` 1, `corpus_run.py` 2,
  `decision_spread.py` 1 (plus `attribute_top`'s parameter, `:174, :180`, and REM-12's `field_zero`, which stops
  subtracting `urgency`), `populated.py` 1, `probes.py` 3 (and `SUBSIST`, `:142-149`, deleted with its last caller),
  `scarce.py` 1, `soak.py` 1, `storybar.py` 1; `headless.py:134, :168`; `play_surface.py:6`;
- **the tests:** every `subsistence=` keyword and every `Sensation(<int>)` constructor (`Sensation(0)` → `Sensation()`).
  - `test_season_shape.py`: 8 keywords and 7 constructors, including `:946-952`. The pinned
    `sense(p, w, subsistence)` there becomes `sense(p, w)`, and `"choose(p, v, s, ask_budget)"` stays.
  - `test_season_shape.py:2769-2800`, `test_w5_f2s_third_term_cannot_change_any_decision`, is deleted with `urgency`,
    the subject it tests (P1 §0.5's precedent).
  - One keyword each in `test_6f_score_confliction.py`, `test_demand_delivery.py`, `test_fi03_trail.py`,
    `test_g2_token.py`, `test_governance_build.py`, `test_in10b_termed_seat.py`, `test_in25_stance_gain.py`,
    `test_in50_refusals_carry_the_occasion.py`, `test_in62_decision_spread.py`, `test_in71_doctrine_conviction.py`,
    `test_information_cluster.py`, `test_sc01_the_bar.py`, `test_told_by_channel.py` and `test_u8_ambitions.py`;
    2 in `test_give.py`.
  - The `Sensation(…)` constructors: `test_march.py` 2, `test_told_by_channel.py` 2, `test_in53_vacancy_need.py:409`,
    `test_governance_build.py` 1, and `harness/probes.py:1057, :1059`.
  - `test_governance_build.py:920-935`, `benefits_me`'s direct assertions, deleted with the function.
- **The Layer 1 text, in the same PR (D-1):**
  - L1-6: 04 §B.10 becomes `Sensation := (standing)`, and its GDScript `Vector2` note becomes "a single scalar"; §C.3's
    "two scalars" becomes "one scalar".
  - L1-7: 01 §D.10's "a need | a `Sensation` plus a Query" becomes "a need | a Query (for a settlement, `world_q.hunger`;
    REM-50) plus the claims a person holds about it", citing the 2026-10-21 ruling.
**Hash, declared and measured, not assumed.**
- `urgency` was one value per person per deliberation, so removing it from the score changes no order (a constant
  shift under the Gumbel sampler). That part is hash-neutral.
- **But `_inputs_fingerprint` loses its `subsistence` term.** A person whose home larder changed between rounds while
  `q_ids` did not was re-deliberated before and is released after (the skip, `deliberate.py:434-450`). That can move
  scenes, so REM-44 is a **declared candidate mover**: the realm 2-season hash (base 89bc9c0ac2a0 at HEAD) is read
  before and after at seeds 0-2. If it moves, it is re-pinned old → new in the commit body, with the count of
  re-deliberations the skip saved.
falsifier:
- `rg -n 'subsistence' engine/season/{decision,state/carriers.py,loop/deliberate.py,loop/driver.py}` returns only
  comments that record the deletion. No code path reaches `Sensation.subsistence`; it is a `TypeError` by construction.
- `test_choose_receives_no_world` pins `sense(p, w)`.
- U2's fingerprint test (`test_u2_the_inputs_fingerprint_is_complete_for_the_skip_it_licenses`) stays green: with
  `subsistence` gone, equal fingerprints still imply equal candidate sets, because no chooser term reads it.
- Mutation: re-add a chooser term that reads a per-person scalar, and the fingerprint test reds.
Control: the base commit's hashes at seeds 0-2; `aperture 1 0`'s per-verb counts (equal, unless the fingerprint skip
moved them, which is then the declared mover). tier: Sonnet producer; Opus critic (a Layer 1 type changes). revert: one
commit (code and the two Layer 1 hunks).

**REM-45 · NERS G7: `operations.py:246` caps the history term, not the sum (rev. 2, C-13).** closes G7. class (d).
Layer: `systems/threadwork/sim/` (an oracle; `CLAUDE.md` §7); no `engine/` import added. **Gate:** PP-624, which the
docstring quotes (`:245`), is verified by hand first. `grep -rl PP-624 registers/` returns nothing at HEAD, and PP
provenance is unvalidated (`CLAUDE.md` §0). The hand-verification sites are where PP-624 is quoted:
`proposals/2026-08-23-suite-01-rulings-and-execution.md`, `proposals/2026-08-15-character-and-faction-stats-and-progression.md`,
`proposals/2026-10-16-character-template_part3.md` and two `proposals/2026-10-16-verbs/` parts (grep this session). They are
resolvable, not authority (§0.05). **The stop rule fires only if none of them quotes PP-624's formula**, or if they
disagree about whether "capped +3D" caps the term or the sum. change: `min(3, history + 3)` → `min(3, history) + 3`.
falsifier: one test where the pool at history 0 differs from the pool at history 3. Mutation: revert the line, and the two
pools are equal (both 3 + spirit term), so the test can fail. hash: `engine/season` equal (threadwork is unplugged until
B-S); `engine/tests` goldens **[UNVERIFIED]** (declare a re-pin if `sim-regression` moves). `CURRENT.md:27`'s re-point
is L0-2 (D-1). revert: one line.

**REM-46 · NERS X1: untrack `engine/season/runs/TRACE.txt` and the eight `.md` logs.** closes X1. class (d). Layer:
generated artifacts (`CLAUDE.md` §0.1 pt 5: process-only, so delete rather than guard); owner = `harness.report`, which
regenerates them. change: `git rm --cached` plus `.gitignore`; keep `results.json` until its two tests regenerate it.
Any plan line that re-records a TRACE-derived artifact names the regenerated file instead. falsifier: `report && delta`
on a clean checkout gives the same deltas (`PROBE FLIPS 0`). Order: after RB-1, since REM-14 changes `TRACE.txt`. hash:
none. revert: re-add.

**REM-47 · NERS X8: delete `tools/evacuation_plan.py` and its test, with a `FORK:` row.** closes X8. class (d). Layer:
`tools/` (process). **Gate [UNVERIFIED]:** no ED-IN-0125 evacuation pending, and no caller in
`references/ci_checks_registry.yaml` or `.github/workflows/valoria-ci.yml`. change: delete both; one exact-file `FORK:`
row in `references/restructure_ledger.md` (`CLAUDE.md` §1). falsifier: `python tools/pathres.py
tools/evacuation_plan.py` → FORKED; the CI workflow names no deleted file. hash: none. revert: `git revert`.

---

### 2.5b RB-5 · HUNGER — a settlement attribute that responds to settlement population (rev. 4, new)

Jordan, 2026-10-21: *"hunger should be a thing for settlement cohorts"*, clarified: *"ie a settlement attribute that
responds to settlement population"*.

#### 2.5b.1 What exists today (read at HEAD `b70b5af`; figures run this session with `PYTHONHASHSEED=0`)

**How a cohort eats.** `queries/world_q.py::subsistence_draw` (`:900-978`) is the one owner of the draw.
- Only a cohort eats (`Person.is_cohort`; plan position `24f`, ED-IN-0255: *"it's a territorial issue"*).
- `want = subsistence_weight[k] × Person.weight` (`rosters.yaml: subsistence_weight`, grain 2 and salt 1, H-11's
  "invented" weights).
- The food comes from `nearest_store` up the larder ladder: `take = min(want, held)`.
- `demanded(w, S)` and `delivered(w, S)` (`:980-1040`) sum the draw over S's subtree. They are already Queries, owned by
  Nobody (01 §D.10, T-a).
- MATTER calls the draw (`loop/matter.py:344`), writes the draws on each larder's `stores` through the gate, and records
  the shortfall per person (`:348-354`, `w._subsistence_shortfall`, "never read by the loop").

**Where hunger can occur.** Only where a cohort's walk finds less than it wants.
- MATTER attaches a `shortfall:<kind>` Observation to the drained larder's own `stores.changed` write (plan position `19d`,
  `:356-405`). WITNESS deposits it to whoever stands at or holds the larder, and since IN-22 to every governor whose seat's
  purview contains it (`witness.py:60`, `SEAT_CHANNEL`).
- A governor's `claim_landed` question then forms a `transfer` to the hungry rung carrying the claim's kind and amount
  (`decision/options.py::_from_shortfall_claim`; IN-22's live arm, `tests/test_in22_shortfall_reach.py:380-470`, **3 passed
  this session**).

**What a starving cohort does, and cannot do.**
- With `body_step > 0`, MATTER falls the cohort's body by `body_step × units short` (`matter.py:442-467`). It emits
  `body.changed` and the band crossings, and removes the cohort at 0 (`_die`).
- `decision/budget.py:59-76` cuts the cohort's scene budget by the body bands it has fallen (person-side, `p.body`, no
  World), so a starving cohort acts less, then dies.
- **Shipped `body_step = 0`** (`data/fixtures.py:567`, H-125, swept 0/10/67). So today nothing physical follows hunger.
- The cohort's only decision-side trace of hunger is `Sensation.subsistence` (`probes.py:142-149`, `SUBSIST` reads the
  home larder) feeding `urgency`. That term is constant across one person's candidates, so it changes no choice, and
  REM-44 deletes it (L1-6, option B).
- A cohort has no pursuit vector (ED-IN-0296 (2)) and holds no seat. So its tier-1 attention (`own_purview`,
  `world_q.py:2041`) is empty, and it cannot `requisition` or `transfer` via a seat.

**Measured (realm, `build_realm(0)`, seed 0, two seasons; scripts `SP/hunger/measure_hunger.py`, `cover.py`,
`sweep_weight.py`, scratch and read-only):**

| reading | `body_step` 0 (shipped, the control) | `body_step` 10 |
|---|---|---|
| cohorts / total weight | 37 / 74 (every cohort at weight 2) | 37 / 74 |
| cohorts short, season 0 → season 1 | 37 → 0 (no stock before the first yield) | 37 → 0 |
| lowest cohort body after 2 seasons | 1000 | 940 (= 1000 − 10 × 6 units short in season 0) |
| 2-season realm hash | `89bc9c0ac2a0` (equals this session's baseline: the control reproduces) | `2e699cfb8a15` |
| settlement food cover, after season 0 / 1 (stores at S and below ÷ demand per season) | 21.7 / 41.7 seasons, identical at all 37 | — |
| cohort acts, season 1 (top three) | `migrate` 86, `survey` 44, `work` 39 | `migrate` 85, `survey` 43, `work` 41 |

**Capacity bounds population.** `capacity(w, home)` is 4-9 per cohort home (median 6). Scaling every cohort's weight ×10,
capped at capacity, still records 0 shortfall after season 0.

#### 2.5b.2 What is missing for hunger to be "a thing", as a person or an observer would see it

1. **No settlement has a hunger value anyone can read.** A shortfall exists only for the one season a larder drains, as an
   observation on that write. Nothing says "this town is lean" before it starves, or "fed again" after.
2. **The physical consequence ships off** (`body_step = 0`). A hungry cohort neither weakens nor dies.
3. **At today's magnitudes the realm cannot go hungry after season 0.** Yield runs about 20 seasons of food ahead of demand
   per season, and population is capped at 4-9. Population cannot drive hunger until the ratio is set (JQ-6).
4. **The people at a hungry settlement learn nothing** unless a larder drains while they stand there. The cohort, its
   governors and its neighbours hold no claim about the town's state.

#### 2.5b.3 Candidate routes, with their Layer analysis

| route | what it is | Layer analysis | verdict |
|---|---|---|---|
| **A · derived settlement Query + its observation + the body clock** | `world_q.hunger(w, S)` reads the settlement's population demand against its food on hand. Its band rides MATTER's EXISTING larder and body writes as an Observation; WITNESS deposits it through existing channels; H-125's body clock ships live | Layer 2. **T-a** (01:325-331: "an aggregate cannot be stored … what it can be is a function"), 01 §D.10 ("every aggregate \| a Query, owned by Nobody"), 04 PART D row 8 ("a stored aggregate \| no field slot; a Query is a function"); the IN-23 precedent (legitimacy and stability are Queries over state). **AX-2:** a person learns hunger only as a claim he holds (it may be stale); `decision/` gets no World. **AX-7:** the deposit goes through the channels and their refraction, never unmediated. 04 PART D rows 5 and 25: no new Event, no new kind, nothing written that did not happen (the 19d precedent). AX-5: bodies are one of the world's three motions. No seam | **recommended** |
| B · a hunger question source | the cohort of a hungry settlement gets a standing question about its larder (a `need`-like source in `questions_for`) | Layer 2, `world_q` (resolver-side, as `vacancies` is). But the source reads world truth the cohort never witnessed and turns it into an occasion: AX-7's "the world pushing truth into them" in its mildest form. Making the cohort ATTEND to its own town is the better half, but it changes IN-57's attention tiers for every person, which is RS-22's [ASSUMPTION] and ED-IN-0296 (1)'s territory | **alternative**, only on a ruling: "does a claim about the place a person lives rank in tier 1?" (asked inside ED-IN-0296 (1), not as a new row) |
| C · a person-side hunger value on the interior | a per-person number on `PersonInterior` that `choose` reads per candidate | Dropped by Jordan's clarification: hunger is a SETTLEMENT attribute, not a per-person value. A candidate-independent reading of it is `urgency` again (REM-44 deletes that); a candidate-dependent one needs an axis nobody ruled | **dropped** |
| D · hunger as a pursuit or temperament vector (SE-06) | the cohorts' vectors weight food-seeking verbs | an attribute of persons, not of the settlement; and the vector is ED-IN-0296 (2), Jordan's | **dropped** for this requirement. If ED-IN-0296 (2) is answered yes, a cohort's vector can make it *prefer* to answer hunger (e.g. `migrate`), on top of route A |
| E · a stored settlement field (`Rung.hunger`) | a number written each MATTER | **refused:** T-a / AX-4 (an aggregate over many owners has no single writer), PART D row 8 | **refused** |
| F · a flat per-person decision term | hunger added equally to every candidate's score | refused by the coordinator's constraint and by REM-44's evidence: a constant shift changes no choice (it is `urgency`) | **refused** |

#### 2.5b.4 Recommendation

**Route A is the smallest route that visibly changes what cohorts do and how long they live.** It has three items, in
order:
- REM-50: the Query.
- REM-51: its reach.
- REM-52: the body clock live at H-125's arm 10.

It visibly changes:
- **how long cohorts live**: bodies fall and cohorts die where food is short;
- **how much they act**: the body band cuts their scene budget (`budget.py:59`);
- **what governors do**: hunger claims reach seat holders whose purview contains the town (IN-22), so `transfer` (and
  `requisition`, which drains a larder) acts on a town that is known to be hungry;
- **who stays**: a death lowers the settlement's demand, so hunger falls. That is the "responds" loop:
  population ↔ hunger ↔ bodies.

**What it does not do, honestly:** it does not make a vectorless cohort *prefer* `migrate` or `transfer`. Among a
cohort's candidates the draw still decides (F-C; ED-IN-0296 (2)). The alternative that adds preference is route D on
ED-IN-0296 (2), and route B for attention.

**Interaction with the other verbs.**
- `migrate`'s capacity decline (116 no-ops; REM-29's `room` conjunct) is untouched. Hunger does not change capacity, and
  `migrate` gains no hunger conjunct, since forbidding a move into a hungry town is the engine deciding options
  (03 §C.3, AX-1).
- `work` does not make food (it advances a works, ED-IN-0297), so it is not a hunger answer.
- `transfer` and `requisition` move `Rung.stores` and so move REM-50's reading the same barrier they execute.

**At today's magnitudes this binds only before the first yield and in scarce worlds** (2.5b.1). Making it bind in the
realm is JQ-6.

#### 2.5b.5 The formula, and the owner of each input

`hunger(w, S)` → `(band, cover, unmet)`, for a settlement-or-lower rung S:
- `D(S)` = Σ_k `demanded(w, S)[k]`. **Owner:** `subsistence_draw`/`demanded`. It is the population term: each housed
  cohort's `Person.weight` (its head count, T-l; the eaters `population(w, S)` counts at `:1145`) times the per-head
  weight. Individuals do not eat (ED-IN-0255).
- `A(S)` = Σ `Rung.stores` at S and beneath it (`_subtree`, `world_q.py:1324`). **Owner:** each `Rung`'s `stores`,
  written only through the gate by MATTER's draw and yield and by `transfer`/`requisition` effects.
- `G(S)` = Σ_k `delivered(w, S)[k]` for the draw that ran. **Owner:** `delivered`.
- `cover = A / D` (seasons of food on hand); `unmet = (D − G) / D` (the share unfed this season); both 0 when `D = 0`.
- `band` = the first entry of a new `rosters.yaml: band_floors["hunger"]` row the reading falls under. Defaults
  **[ASSUMPTION; medium; Jordan to correct; JQ-6]:** `starving` if unmet > 0; `hungry` if cover < 1; `lean` if cover < 2;
  else `fed`. The row joins `band_floors`' existing loader (`data/fixtures.py` reads `band_floors` off `rosters.yaml`), so
  there is one loader.
- **It responds:** D rises with population (a cohort moving in, or heavier weights) and falls with deaths and departures;
  A falls with draws and requisitions and rises with yield.
- **One owner of the rule:** `queries/world_q.py::hunger`, reusing `subsistence_draw`'s record so the band cannot disagree
  with the draw (`CLAUDE.md` §8).

#### 2.5b.6 The items (RB-5)

**Placement:** P3 §B.0 R3 (EDITS in `loop/matter.py`, `data/fixtures.py` body terms, a larder reader in `world_q`). It
needs neither IN-06 nor IN-07, so it is its own batch. It opens after RB-1 (REM-11's per-kind count line is its reading),
runs **beside B-P** (no shared file: B-P edits `data/` loaders and ids, `faction_q`, the write matrix), and **merges before
RB-2a** (both edit `queries/world_q.py` and `rosters.yaml`). It is serial with B-Q, B-S and B-T on `loop/matter.py`
(they merge after it and re-run under §C.2). **Lanes:** 1, serial. **Tier:** Opus producer for REM-51 (it spans MATTER,
WITNESS and the Query); Sonnet for REM-50 and REM-52; an Opus critic at the close. **Budget:** ~90k whole / ~60k working.
**Exit:** M-H1, M-H2 (§5); `register --requirements`; the batch critic's read of R-04's `measured:` line.

**REM-50 · `world_q.hunger(w, S)`: the settlement's hunger as a derived Query, and its reading in `census`.** closes the
hunger requirement's attribute half (2.5b.2 item 1).
- R: **R-04** vis (the settlement row gains a readable, population-responsive attribute). class (a).
- **Layer:** Layer 2, `queries/world_q.py` (04 §A.2: World first, owns nothing, no token parameter); T-a, 01 §D.10,
  PART D row 8. The band table is a registry code reads at runtime, so it is mechanism (§0.05). No seam.
- **One owner:** `hunger`.
- change:
  - `queries/world_q.py`: `hunger(w, S, draw=None)` per 2.5b.5, reusing `demanded`, `delivered` and `_subtree`.
  - `rosters.yaml: band_floors` gains the `hunger` row with its note, coinage defined (`CLAUDE.md` §4).
  - `engine/season/hole_register.yaml` gains one row for the band thresholds (kind NUMBER, `owner:` Jordan, JQ-6;
    04 PART D row 38).
  - `harness/populated.py::census` gains `hunger_by_settlement`, a band histogram. It is a report, never read by the loop
    (the `uncontrolled` precedent at `census`).
  - **It lands in the same commit as its first game caller, REM-51** (ID-13: "a Query nobody calls"; `capacity`'s
    precedent, `world_q.py:1193-1197`).
- falsifier (`engine/season/tests/test_hunger.py`, one new file, on `harness/scarce.build`):
  - Raising the cohort's weight raises D and lowers cover, and the band moves toward `starving`.
  - Removing the town's stores lowers cover; restoring them raises it.
  - Adding a weight-1 individual at S changes nothing (individuals do not eat).
  - Mutation: compute D from `population(w, S)` instead of `demanded`, and the individual test reds.
  - **Control:** every hash is equal with REM-51's reach off. The Query and the census line read and write nothing.
- verify: `python -m pytest engine/season/tests/test_hunger.py -q`. hash: equal. revert: the function, the roster row and
  the census line.

**REM-51 · Hunger reaches people: the settlement's band rides MATTER's existing writes as an Observation, behind
`hunger_reach`.** closes 2.5b.2 item 4.
- R: **R-04** ↑ (the settlement scale has a consequence persons act on); **R-06** = contributor (cohorts hold claims about
  their town; no conviction moves); **R-08** = contributor (they act on held, possibly stale hunger). class (a).
- **Layer:** Layer 2, `loop/matter.py` (MATTER token; 04 §A.2 `loop/matter`) and `loop/witness.py`'s existing channels.
  - 04 PART D row 5 (no success Event for a write that did not happen) and row 25 (no new kind): the 19d shape, "NO NEW
    EVENT, NO NEW KIND, NO NEW WRITE".
  - §C.6: the channels decide who learns; there is no actor (an actorless MATTER Event).
  - AX-2 and AX-7: persons hold a claim, refracted like any deposit. `decision/` gains nothing.
  - L5 (the crossing produces no outcome): nobody is made to act.
  - No seam.
- **One owner:** the predicate `HUNGER_PREDICATE`, beside `SHORTFALL_PREDICATE` in `data/requires.py:134`, via the
  `shortfall_sourced_operands` roster's shape. The fixture `hunger_reach` is registered in `data/fixtures.py` with its
  H-row.
- change:
  - At MATTER, after the draw, compute `hunger(w, S, record)` for each settlement-or-lower rung with demand. Compare it
    with the band computed from the same barrier's pre-draw stores (cover only), so it is a crossing within the barrier
    and nothing is stored.
  - Where the band changed, attach `Observation(S, HUNGER_PREDICATE, band)` to the `stores.changed` Event of S's
    subtree larder write that the draw already emits.
  - When the body clock is live (REM-52), attach the same Observation to each hungry cohort's own `body.changed` Event.
  - A town with no write in that barrier (an unstocked larder, no body fell) is unreported. That limit is registered, as
    H-160 registers it for shortfall.
  - `hunger_reach` off attaches nothing.
  - **[UNVERIFIED]** whether a realm cohort's home is S itself or a building beneath it, which decides whether the
    co-located channel reaches it. The falsifier observes the claim, not the route.
- falsifier (`test_hunger.py`, on `scarce.governed`):
  - With `hunger_reach` on, the reeve whose purview holds the town and the town's cohort hold `(town, hunger, <band>)`
    claims at the band REM-50 reads; the far reeve holds none.
  - The reeve's `questions_for` holds a `claim_landed` question about the town (IN-22's route).
  - Mutation: attach the Observation to a NEW Event, and the no-new-kind assertion (REM-41's roster, or a direct kind
    check before RB-4b) reds.
  - **Control: `hunger_reach` off reproduces today's hash exactly**, on `scarce.governed` and on `build_realm(0)` at
    1 and 2 seasons.
- hash: **declared mover with the reach on.** Shipped ON [ASSUMPTION; medium; Jordan to correct; revert: off]. At today's
  magnitudes, the realm's season-0 pre-yield starvation (all 37 cohorts) is the crossing that deposits.
- tier: Opus producer, Opus critic. revert: the fixture to off, then the code.

**REM-52 · Ship H-125's live arm: `body_step = 10` [ASSUMPTION; medium; Jordan to correct; revert: 0].** closes 2.5b.2
item 2.
- R: **R-04** ↑ (hunger has a physical consequence in the realm). class (a); the magnitude is (b), JQ-6.
- **Layer:** Layer 2 data (`data/fixtures.py:567`, one value; its `hole_register.yaml` H-125 row's `default:` line edited
  with it, 04 PART D row 38). AX-5 (bodies are one of the three motions); the write matrix's `(Person, body) [MAT, RES]`;
  04 §A.2 `loop/matter` (MATTER token). Person-side `budget` reads `p.body` with no World (PART D row 2). No seam.
- **One owner:** the fixture.
- change: `body_step=0` → `10`, with its comment, and H-125's `default:`. 67 stays a swept arm: it kills a short cohort
  in the barrier that records the shortfall (`test_in22…:380-415`).
- falsifier:
  - Realm, seed 0: after season 0 the lowest cohort body is exactly `1000 − 10 × 6 = 940` (measured this session).
    Mutation: a body write on a copy (the read/write asymmetry `matter.py:430-436` warns of) leaves it at 1000 and reds.
  - On `scarce.governed` at the new default, the short cohort's `budget` falls by the bands its body crossed
    (`budget.py:59`).
  - **Control:** `body_step = 0` reproduces `89bc9c0ac2a0` (realm, 2 seasons; measured).
- hash: **declared mover**: `89bc9c0ac2a0` → `2e699cfb8a15` (realm, 2 seasons, seed 0, measured). Seeds 1 and 2 are read
  at the batch.
- **Re-pins, declared:**
  - `test_in22_shortfall_reach.py`'s `CONTROL_ARM == 0` assertion (it reads H-125's shipped default) and its zero-arm
    control.
  - `tests/test_territorial_subsistence.py` (reads H-125's sweep).
  - Every seeded realm hash pin.
  - The BASE_EVENTS pins in `tests/test_in34_bodies_clock.py` and `tests/test_season_weather.py` (grep this session;
    H-206's cite: "7526 events after 1 season").
  - `results.json` via `report && delta`.
  - The corpus, the spine and `headless` are unaffected: they have no cohort, so no eater (H-171).
- tier: Sonnet; Opus critic. revert: one value.

#### 2.5b.7 Interactions

- **ED-IN-0296 (2), cohort vectors.** Hunger needs none. If Jordan answers yes, a vector can make a hungry cohort prefer to
  answer the claim (route D). R-06's fifth conjunct stays false until then (REM-05).
- **REM-05 and REM-12, cohort sampling.** `decision_spread`'s vectorless count is unchanged by RB-5. Its `--season` arm
  reads cohorts' acts, which REM-52 moves (budget cuts and deaths), so REM-12's `--season` base is re-taken after RB-5.
- **RB-2's stampers.** A hunger claim about S is a plain referent. Rows classed `Rung` (`migrate`, `requisition`,
  `march`) form on stamps, not on it. So RB-5 neither widens nor narrows any classed formation, and RB-2a merges after
  RB-5 on `world_q.py`.
- **REM-44.** It removes `Sensation.subsistence`, the last decision-side hunger plumbing (`SUBSIST`). After both,
  hunger reaches decisions only as claims (REM-51) and through the body (REM-52). This is the route Layer 1 allows, and
  01 §D.10's amended row (L1-7) names it.
- **IN-22.** It is the governors' half, already live. REM-51 adds the settlement band beside the shortfall amount. A
  governor's `transfer` keeps reading kind and amount from the shortfall claim.

#### 2.5b.8 Golden and pin re-records (RB-5)

REM-51 (reach ON) and REM-52 (`body_step` 10):
- the realm seeded hashes, at 1 and 2 seasons and seeds 0-2;
- `test_in22_shortfall_reach.py`'s control assertions;
- `test_territorial_subsistence.py`;
- the BASE_EVENTS pins in `test_in34_bodies_clock.py` and `test_season_weather.py`;
- `results.json`;
- `runs/` (tracked until REM-46).

The corpus, the spine, `headless` and `engine/tests` are unaffected.

### 2.6 Owner map for the 47 kinds declared and never emitted in either world (2 seasons, seed 0; rev. 3: the intersection of `SP/realm_2_0_undefined.json` §D (49) and `SP/spine_2_0_undefined.json` §D (61); `date.scheduled` and `establish.refused` were emitted by the spine and are dropped, D-05)

| kinds | why none is emitted | owner |
|---|---|---|
| `field.won`, `field.lost`, `field.unopposed`, `army.arrived` | no `march` reaches a field | REM-27 |
| `site.built`, `site.restored`, `site.worked`, `rung.founded` | no works exists (ED-IN-0297); `restore`/`work` mis-form | REM-22, ED-IN-0297 |
| `rung.seized`, `record.seized`, `seize.refused`, `seize.unauthorized` | `seize` forms only where a held dispensation names the target | v9 IN-12 step 6 residue (B-R reads it) |
| `matter.carried`, `matter.advanced`, `matter.held`, `matter.determined`, `matter.undetermined` | `speak` is refused at admission; THE BAR closes on hand-built worlds | v9 SC lane; REM-13 (D-30a rule); DEF-3 |
| `tenure.opened`, `office.established`, `heir.designated`, `confer.refused`, `remit.changed`, `succession.refused` | IN-10's verbs form rarely; IN-61 unbuilt | v9 IN-10 lineage, IN-61 (B-R) |
| `record.given`, `record.destroyed`, `destroy.refused` | `give` mis-forms (C4); `destroy_record` unformable | B-R (`give`), v9 IN-26 (B-Q) |
| `requisition.taken`, `requisition.refused` | H-163 limit 3(a) | v9 IN-49 residue |
| `petition.carried` | `carry` mis-forms | REM-25 |
| `exchange.made`, `exchange.refused`, `construal.impossible` | rows uncarried | REM-2B |
| `commitment.made`, `commitment.ended` | `commit` mis-forms; IN-57's own-act screen | REM-23, ED-IN-0296 (3) |
| `compliance.given`, `compliance.impossible`, `compliance.withheld` | `comply` forms only on an addressed writ | v9 IN-09 lineage |
| the rest (`bond.formed`, `confidence.broken`, `duty.refused`, `duty.taken`, `issue.unauthorized`, `person.demanded`, `case.refused`, `tenure.payload_set`, `term.renewed`, `terms.distorted`) | rare at two seasons, or rows not yet reached | REM-11's line re-reads them at each batch; a kind still at 0 after RB-2b at seeds 0-2 is named in the batch's HANDOFF line |

[UNVERIFIED] The bucketing is by the kind's emitting row (`KIND_VERB`), not by a traced cause. REM-11 makes the line
reproducible, and the realm and spine lists (`SP/realm_2_0.out` §D, `SP/spine_2_0_undefined.json`) are the base.

### 2.7 Layer 1 conformance self-check, per batch (narrowest instrument that observes a breach; no new process guard)

| batch | breach it could commit | the existing instrument that sees it |
|---|---|---|
| RB-0 | prose made a mechanism (a `met` that a status edit could green) | `python -m engine.season.harness.register --requirements` (refuses an unrunnable acceptance, `register.py:636-676`); the critic's read |
| RB-1 | instrumentation moving the game | aperture's own control-arm hash-equality line; `report && delta` → `PROBE FLIPS 0`; `test_in62_the_harness_top_is_the_real_choosers_top` |
| RB-1 (rev. 2) | an instrument re-keying ids it claims to hold fixed (REM-15); a shared reader's contract changing under its callers (REM-10) | REM-15's τ = 0 plant (no difference across draw seeds); `engine/season/tests/test_fa01_head_seats.py` and `test_sc01_the_bar.py` green and unchanged |
| RB-1 (REM-14) | a predicate refusal turned into a raise (04 §C.4) | `test_g3_not_yours.py`; `content_hash` equal on and off |
| RB-2a, RB-2b | a decision reading world truth (AX-2, PART D 2) | `test_season_shape.py::test_choose_receives_no_world` (`:946`), `::test_decision_package_never_names_world_anywhere_under_it` (`:2939`), `::test_person_q_cannot_reach_the_world_side` (`:3231`) |
| RB-2a, RB-2b | a second loader or an unvalidated column | `data/verbs.py:655` (undeclared class refused at load); REM-21's `check_stampers` at `SeasonDriver` construction |
| RB-2a, RB-2b | a typed cell and a predicate on one row | `test_season_shape.py::test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` (`:9342`) |
| RB-2b | a branch on a rung-kind member (D-28) | `engine/season/tests/test_scale_of_rung.py::test_a_synthetic_rung_kind_with_no_scale_refuses_at_the_mapping` and the permutation of `march_target_kinds` in REM-27's test |
| RB-3 | `engine/` importing a subsystem; a module writing state | `tests/valoria/test_engine_does_not_import_systems.py::test_importing_every_engine_module_pulls_in_no_subsystem`; IN-46's replay-equality test |
| RB-4 | a refusal that raises (D-7); an undeclared kind (D-25); an unrowed act passing silently (D-26) | REM-40's load refusal and its `zz_not_a_row` raise; REM-41's plant; REM-41's report-mode run over `python -m pytest engine/season/tests -q`, the arm that reaches S27.4; `test_season_shape.py`'s refusal-kind tests |
| RB-5 (rev. 4) | a stored aggregate (T-a, PART D row 8); a decision reading world truth (PART D row 2); a new Event or kind (rows 5, 25) | `rg -n 'hunger' engine/season/state` returns no field (the Query owns it); `test_season_shape.py::test_choose_receives_no_world`, `::test_decision_package_never_names_world_anywhere_under_it`; REM-51's no-new-kind assertion; `hunger_reach` off reproduces today's hash |

### 2.8 Ordering and the critical path

```
RB-0 ─► RB-1 ─► B-P ─► RB-2a ─► RB-2b ─► B-Q ─► B-R ─► B-S ─► B-Y ─► RB-3b ─► (R-04, R-05 re-read)
          │       └─ RB-5 HUNGER (beside B-P; merges before RB-2a) ─┘ │      └─ RB-3a (beside B-Y) ┘
          │              └─ serial with B-U on world_q.py (C.2)            
          ├─► RB-4a (beside B-P; merges before B-S)
          └──────────────────────────────────────────────── RB-4b (after B-Y, beside B-T); REM-32 at B-T's tail
```

**Critical path to THE NINE, one line:** RB-0 → RB-1 → {B-P ∥ RB-5} → RB-2a → RB-2b → B-Q → B-R → B-S → B-Y → RB-3b (IN-46), with RB-3a
(IN-47) beside B-Y. RB-5 (HUNGER) runs beside B-P and merges before RB-2a. **Rev. 4:** RB-3 is no longer gated (D-2 yes).
After that:
- R-04, R-05 and R-07 can read `met` only on measured executions. R-04 conjunct (1) has no item here at all.
- R-06 waits on JQ-1 (τ) and ED-IN-0296 (2) (cohorts).
- R-08 waits on its own RANKING reading, and on cell values if zero ties remain for vectored persons.
- R-09 waits on J-13's remainder with JQ-2 (capacity).
- R-05 also waits on ED-IN-0297 (works).
The per-row table is §0, "THE NINE: confirmation".

### 2.9 Index: every item (40), with its batch, class, row move, Layer, tier and hash

Tier = the model that PRODUCES the item (`CLAUDE.md` §10). The verifier on a judgment node is Opus, named in each batch.
Revert path: the item's own commit, unless the item says otherwise. Layer: **L2** = game code or a data file the game
reads at runtime; **H** = harness (reads L2, binds nothing); **P** = the plan (binds the agent).

| item | batch | class | R rows | direction | Layer · 04 / AX touched | tier | hash |
|---|---|---|---|---|---|---|---|
| REM-01 | RB-0 | a | — | — (the count made true) | P | Sonnet; Opus critic | none |
| REM-02 | RB-0 | a | R-05 | vis | P | Sonnet | none |
| REM-03 | RB-0 | a | R-04 | ↑ (owners named) | P (+ one comment in `requirements.yaml`) | Sonnet | none |
| REM-04 | RB-0 | a | R-07 | ↑ (owner named) | P | Sonnet | none |
| REM-05 | RB-0 | a (b: JQ-1) | R-06, R-08 | R-06 ↓; R-08 vis | P · T-l, AX-2 | Sonnet; Opus critic | none |
| REM-06 | RB-0 | a | R-09 | ↓ | P · §C.4 F6, D-30a | Sonnet; Opus critic | none |
| REM-08 | RB-0 | a (b) | R-04, R-06, R-09 | the asks (JQ-1 … JQ-5) | P | Opus | none |
| REM-09 | RB-0 | a | R-05 | ↑ (scheduling) | P | Sonnet | none |
| REM-10 | RB-1 | c | R-05 | sideways | H · §B.9, D-51; a sibling, five callers untouched | Sonnet | equal |
| REM-11 | RB-1 | c | R-04, R-05, R-07 | vis | H · §C.4, inv. 4; keyed by act | Sonnet | equal |
| REM-12 | RB-1 | c | R-06, R-08 | vis | H · AX-2 untouched | Sonnet; Opus critic | equal |
| REM-13 | RB-1 | c | R-09 | vis | H · §C.4 F6, D-30a, inv. 12 | Sonnet | equal |
| REM-14 | RB-1 | c | R-04 | vis (conj. 1's predicate clauses) | L2 TRACE only · §C.4 | Sonnet | equal (TRACE.txt moves) |
| REM-15 | RB-1 | c | R-09 | vis (choice-driven chains only) | H · §A.2 `state/ids`, D-35 | Sonnet; Opus critic | equal |
| REM-16 | RB-1 (and M-10 at RB-2b) | c (+ E-11) | R-01, R-02, R-05, R-06, R-08 | = (re-take); readings | a run + `requirements.yaml` `measured:` (R5) | Haiku runs; Sonnet reads | none |
| REM-21 | RB-2a | a/c | — | — (primitive) | L2 · §A.2, D-2, AX-2; registry in `world_q` | Sonnet; Opus critic | equal |
| REM-22 | RB-2a | a | R-04, R-05 | R-04 ↑; R-05 sideways or ↑ | L2 data · §C.3 | Sonnet | mover |
| REM-23 | RB-2a | a | R-05 | sideways or ↑ | L2 data | Sonnet | mover |
| REM-24 | RB-2a | a | — | — (`petition` executes; no row moves) | L2 data | Sonnet | mover |
| REM-25 | RB-2a | a | R-05 | sideways (declared) | L2 data + stamper | Sonnet | mover |
| REM-2C | RB-2a | a | R-05 | sideways (`research` executes) | L2 data + stamper · D-2, AX-2 | Sonnet; Opus critic | mover |
| REM-26 | RB-2b | a/c | — | — (a measurement) | H; L2 only if built | Sonnet | none / mover |
| REM-27 | RB-2b | a | R-04, R-07 | ↑ | L2 data + stamper · D-28; `RUNG_REMIT_ACTS` widening named | Sonnet; Opus critic | mover |
| REM-28 | RB-2b | c→a | R-04, R-05 | vis; ↑ only if a KIND failure is classed | H; L2 per row | Sonnet | none / mover |
| REM-29 | RB-2b | a | R-05 | = (stops re-forming) | L2 grammar stem · §C.4, inv. 4, §F.24a | Sonnet; Opus critic | mover |
| REM-2A | RB-2b | c | — | — (a measurement) | H | Sonnet | none |
| REM-2B | RB-2b | a | R-05 | ↑ (3 rows) | L2 data + effects · inv. 4 | Sonnet | mover |
| REM-30 | RB-3a | a | R-04 | ↑ | L2 · §A.2, AX-2, AX-4 | Opus; Opus critic | mover (arm on) |
| REM-31 | RB-3b | a | R-04 | ↑ | L2 · §C.1, §C.5, D-19…24, D-35, D-41a; seam via composition row | Opus; Opus critic | **mover** (every seeded season that fights; P4:34) |
| REM-32 | B-T tail | a (b: JQ-4) | R-04 | ↑ (a contestable field) | `modules/mass_battle` · §A.2 adapter row, D-38 (+ one `hole_register.yaml` row) | Sonnet | equal |
| REM-40 | RB-4b | d | — | — | L2 · inv. 4, ID-12, §F.20b, D-26 (incl. S27.4, `:711` raise, the comment) | Sonnet; Opus critic | mover (realm); tests + one probe re-recorded |
| REM-41 | RB-4b | d | — | — | L2 runtime refusal · inv. 7, D-25 | Sonnet; Opus critic | equal to REM-40 |
| REM-42 | RB-4a | d | — | — | `engine/dice_engine` · `CLAUDE.md` §8 | Sonnet decides `:78`; Haiku replaces | equal |
| REM-44 | RB-4b | d | — | — | L2 + L1 hunks (D-1) · §A.2 `decision/`, §B.10, §C.3, 01 §D.10 (L1-6, L1-7; Jordan's ruling 2026-10-21) | Sonnet; Opus critic | declared candidate mover (the fingerprint skip); measured at seeds 0-2 |
| REM-45 | RB-4a | d | — | — | `systems/threadwork` oracle | Sonnet | `engine/season` equal; `engine/tests` [UNVERIFIED] |
| REM-46 | RB-4a | d | — | — | repository artifacts | Haiku | none |
| REM-47 | RB-4a | d | — | — | `tools/` | Haiku | none |
| REM-50 | RB-5 | a | R-04 | vis | L2 `world_q` Query · T-a, 01 §D.10, PART D row 8; band table in `rosters.yaml` | Sonnet | equal (lands with REM-51) |
| REM-51 | RB-5 | a | R-04, R-06, R-08 | R-04 ↑; R-06 and R-08 = (contributors) | L2 `loop/matter.py` + existing WITNESS channels · PART D rows 5 and 25, §C.6, AX-2, AX-7, L5 | Opus; Opus critic | mover with reach ON; off = today's hash |
| REM-52 | RB-5 | a (b: JQ-6) | R-04 | ↑ | L2 data (`body_step`) · AX-5, write matrix `(Person, body)`, PART D rows 2 and 38 | Sonnet; Opus critic | mover `89bc9c0ac2a0` → `2e699cfb8a15` (realm, 2 seasons, seed 0) |

**Fan-out for this plan's own execution (`CLAUDE.md` §10):** RB-1 runs two worktree lanes, and N−1 would serialise
`decision_spread`/`storybar` behind the `corpus_run.attribute` chain for no shared file. RB-4a runs four lanes on
disjoint files. Every other batch is serial because its items share `verb_table.yaml`. **For this draft, no agent was
spawned:** one reader held every input, and a critic was not dispatched (§0's limits).
