# THE NINE R-ROWS — EXECUTION PLAN, UNIT BY UNIT

## Status: **PROPOSED. REFERENCE under `CLAUDE.md` §0.05 — delete this file and the game behaves identically.** Nothing here may be cited as the reason a behaviour is correct. The mechanisms it names live in `engine/season/`'s registries, in the code, and in `engine/season/tests`. Merging it ratifies no design call; the calls it *records* were closed by the tests named in §11, not by this document.
## Lane: IN. Written 2026-09-09.

> **Scope of the verification behind it.** A read-only Fable planner produced the sequence; this file
> is the writer stage of a `CLAUDE.md` §10 relay. **Every `file:line`, `file::symbol` and quoted string
> below was opened and checked against the working tree at `origin/main` `f41f20a1`** before being
> reproduced. Where the planner was wrong, §2 says so with evidence rather than deferring. Where a
> claim could not be confirmed it is marked `[UNVERIFIED: …]` and is not asserted. The tally is §1.

> ⚠ **PR #383 IS OPEN, NOT MERGED** (verified 2026-09-09: `state: open`, `merged: false`, head
> `4d98bcae`, base `f41f20a1`). Every statement about `loop/`, `queries/` or `epistemic.py` describes
> **that branch**. A reader on `main` will not see those directories — `main` has `data/`, `state/`,
> `harness/`, `tests/`, `cases/`, `runs/`, `shape.py` (4,153 lines), `combat_seam.py`, `gaps.py` and
> `trace_log.py`; the full listing is §3.
>
> **Marker discipline, scoped so it is kept rather than claimed.** Sentences asserting something about
> **#383's STATE** — what it contains, what it does not, its line count — carry **[#383]**. The three
> module names it introduced (`loop/`, `queries/`, `epistemic.py`) then appear unmarked throughout
> §6-§8, because §3 establishes once and for all that they are #383's and repeating the marker at every
> file list would be noise. ⚠ The first draft asserted the marker as a blanket rule and kept it at two
> sites; this is the rule it actually follows.

**What it supersedes.** Nothing. `workplans/2026-09-05-post-adoption-execution-plan.md` forbids its own
supersession by a successor plan and is unchanged here; `workplans/2026-09-06-season-loop-execution-plan.md`
is PROPOSED and held back, and this file agrees with it where the code confirms it and corrects it where
the tree has moved. `architecture/` (Layer 1, RATIFIED 2026-09-05, ED-IN-0204) is cited throughout and
never overridden.

---

## §1 · CITATION VERIFICATION REPORT — the `CLAUDE.md` §0.1 pt 3 artifact

Every citation in the planner's 570 lines was opened and checked — **approximately 190 distinct
`file:line`, `file::symbol`, section references and quoted strings.** The count is approximate because
some citations are ranges checked as a block; the outcome counts below are exact.

| outcome | count | where |
|---|---|---|
| **verified exactly as written, and reproduced** | the large majority | cited inline throughout; not re-listed |
| **corrected** — line, span, symbol, or a paraphrase presented as a quote | **19** | §2.3, §2.4, §2.7, §2.9, §2.10 (×3), §2.11, §2.13 (×3), §2.15 (×9) |
| **materially wrong — the claim does not survive and a unit changes** | **7** | §2.1, §2.2, §2.5, §2.6, §2.8, §2.12, §2.14 |
| **could not verify in this environment** | **7** | marked `[UNVERIFIED: …]` at each site |

> ### ⚠ **AND THEN A STRUCTURALLY-INDEPENDENT CRITIC ATTACKED THIS DOCUMENT AND FOUND MORE. SECOND
> ROUND, 2026-09-09 — the full log is §14.**
>
> | outcome of the critic pass | count |
> |---|---|
> | **HIGH — a unit changes, the claim does not survive** | **5** (F1-F5) |
> | **HIGH — elevated from LOW by ruling: a Layer 1 conformance violation** | **1** (the provider registry belonged in `manifest/`) |
> | **MEDIUM — a control, an edge or an invariant misdescribed** | **8** (F6-F13) |
> | **LOW / line-level, verified one by one before applying** | **12** (L1-L12) |
> | **rejected after checking — the critic was wrong or overstated** | **1** (see §14) |
> | **found by the reconcile stage itself, not by the critic** | **3** (see §14) |
>
> **One of the five HIGH findings was a FABRICATED QUOTE used to close the plan's only genuine
> escalation** (F3, §11.0). **A writer stage that reports zero defects in its own output has not run
> one — and neither has an adversarial stage that finds only what it was already looking for.**

**And 14 citations in this document's own first draft were wrong and were fixed before publication**,
found by re-reading §4 and §6 against the tree a second time: seven `04_CODE_ARCHITECTURE.md` invariant
and section line numbers (`§B.13`'s twelve had shifted, `§C.5.1` was `:711`/`:717` and is `:699`),
`§C.4`'s fold and `Failure: []` spans, `03 §E.1`, `combat_seam.py:141-144`, two `rosters.yaml` lines,
`test_season_shape.py:7869`, `corpus_run.py:487`, and a `TRACE.query` call written with the wrong
arity. **A writer stage that reports zero defects in its own output has not run one.**

**The seven unverifiable ones, all the same cause:** `pytest` was not installed in the writer stage's
environment (`python -m pytest` → *"No module named pytest"*), so no test outcome was asserted as
observed. Test *existence*, *name* and *body* were all read directly and are verified; only "it is green
today" was not. Affected: the 186-test season suite result, the 17-test import-probe result, the
`tests/valoria` suite result, `test_export_sim_params.py::test_sim_params_current`'s current outcome,
and the three per-step falsifier outcomes in U0.

> ### ✅ **FOUR OF THE SEVEN ARE NOW CLOSED — OBSERVED 2026-09-09, NOT ARGUED.**
> The orchestrator ran the suites in an environment that has pytest:
>
> | command | result |
> |---|---|
> | `pytest tests/valoria -q` | **1,778 passed · 23 skipped · 15 xfailed · 0 failed** |
> | `pytest engine/season/tests -q` | **186 passed** |
> | `pytest tests/valoria/test_engine_does_not_import_systems.py` | **17 passed** |
>
> That closes the season-suite result, the import-probe result, the `tests/valoria` result, and — since
> `test_export_sim_params.py::test_sim_params_current` is inside `tests/valoria` — the export
> round-trip's current outcome. **The 186 and 17 the first draft read from `grep -c "^def test"` are
> confirmed as observed pytest outcomes, not source counts.**
>
> **THE REMAINING THREE STAY UNVERIFIABLE BY CONSTRUCTION, AND THIS IS NOT A GAP TO CLOSE LATER.**
> They are the three per-step falsifier outcomes in U0 — the red-before/green-after arms of
> decomposition steps 7, 8 and 9. **Those steps have not been run and the code they falsify does not
> exist**, so there is no outcome to observe; the falsifiers are *specified* and their *specification*
> is what §0.1 pt 3 requires at this stage. Any session reporting them as green before running the
> steps has fabricated them.
>
> ⚠ **AND THE TALLY OF SEVEN WAS ITSELF SHORT BY THREE.** Three further `[UNVERIFIED: … not read this
> session]` markers stood in the body — `harness/exercises.py:12-20` (U8), `scale_transitions_v30.md`
> §2 (U9), `08_DATA_AND_KEYS.md` §3 (§7) — and were a **different cause** (a document not opened, not
> a suite not run), so §1's *"all the same cause"* did not cover them and the count of seven excluded
> them silently. **All three have now been read and closed at their sites**, and one of them (§2's
> scale vocabulary) turned out to carry a defect in U9. A count that quietly omits a category is the
> failure mode this section exists to prevent, so it is recorded rather than repaired in place.

**One execution artifact WAS produced in this session**, and it is the load-bearing one:

```
$ python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
NPC-088 · 2 season(s) · seed 0
  season 0: acts=7 events=8 deposits=21
  season 1: acts=6 events=29 deposits=19
  verbs the fold can execute: 12 of 32
CONTENT HASH: ee0383bf3f4606e56b80cd07c0284f0a
```

The hash `ee0383bf3f4606e56b80cd07c0284f0a` is confirmed at `main` `f41f20a1`. Every "the hash does not
move" control in §6 is measured against that string.

---

## §2 · CORRECTIONS TO THE PLANNER

Each carries the evidence that overturns it. Seven change what a unit must do.

### §2.1 · **Decomposition step 6 is DONE, and it shipped a FLAT module, not a directory** *(material)*

The planner's U0 lists step 6 (`epistemic/`) as work to be done. PR #383's title is *"Decomposition
steps 5 **AND** 6"* and its commit `4d98bcae` is *"Decomposition step 6: epistemic.py"*. Verified by
`git ls-tree -r origin/claude/shape-py-refactor-6f7uiu engine/season/`: the branch holds
`engine/season/epistemic.py` — **a flat module at the package root**, beside `loop/` and `queries/`,
which ARE directories. `shape.py` on that branch is **2,803** lines.

**Consequence:** U0 is three pure-move PRs, not four. And the planner's §0.3 — *"every module placement
below uses directories"* — is false of `epistemic`, and cannot be repaired by citing `04 §A.2`, because
**`epistemic` is not one of §A.2's nine.** The nine are `state/ data/ queries/ decision/ loop/ seam/
manifest/ port/ tests/` (`architecture/meta/04_CODE_ARCHITECTURE.md:127-139`). `decision/` and `seam/`
ARE among them and are directories here — ⚠ on two DIFFERENT and unequal warrants, which the first
draft merged. `decision/` is a directory *from its first commit* on `04 §E.1:1046-1047`, a rule that
**names `decision/` and nothing else**; `seam/` — and `manifest/`, added in U1 — are directories
because `04 §A.2:127-139` names them among the nine, which is a weaker warrant carrying no
first-commit clause. Cite the right one for each. `epistemic` is a step-6 convenience with no
Layer-1 row, and its flatness is not a defect to fix in this arc.

### §2.2 · **The witness deposit body does NOT move, and the plan that said it should was struck** *(material)*

The planner's U0 step 6 includes *"the deposit body of `witness` (`shape.py:3661-3828`) as one
function"*. PR #383's body: *"The deposit body is struck from the plan, not quietly skipped … the plan's
§1 table assigns it to `epistemic.py`; **the plan's own §3 forbids it** — barrier bodies move *"ONLY AS
THE SAME METHODS"*."* Three tests read `getsource(witness)`, one of them
(`test_witness_writes_no_belief_and_no_conviction`) a **negative** assertion that would keep passing
while ceasing to cover what it polices. **Do not re-propose the extraction.** The body stays in
`SeasonDriver.witness` and travels to `loop/driver.py` at step 9, whole.

### §2.3 · **`Person.capability` has exactly one writer, not zero**

Planner §0.5: *"`Person.capability` has NO writer anywhere in the package (grep -> 0)"*. Measured:
`grep -rn "\.capability\s*=" engine/season --include=*.py` returns **one** site,
`engine/season/harness/probes.py:432` — `p.capability = {k: 0 for k in (list(p.capability) or ["copying"])}`,
which **zeroes** it. `requirements.yaml:72-74` states this exactly: *"only `probes.py::_zero_capability`
touches it, to zero it"*. The substantive claim survives and is what §7 depends on: **no writer gives
anyone capability, and it is empty on every corpus person.** The absolute form is wrong and would fail a
reader who runs the grep.

### §2.4 · **`combat_seam.py`'s per-draw seed is at `:153`, not `:145`**

Verified: `seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)`
is `engine/season/combat_seam.py:153`; `result = wrapper.fight(A, B, rng=random.Random(seed))` is `:160`.
`def resolve` is `:130`. Cite **`combat_seam.py:130,153,160`**.

### §2.5 · **U1's `Random(` falsifier is RED BEFORE AND AFTER as written** *(material)*

Planner U1: *"`grep -rn 'Random(' engine/season --include=*.py | grep -v tests` -> exactly one site"*.
Run it today and it returns **two** lines, both in `combat_seam.py`: `:135` inside the docstring
(*"`wrapper.fight`'s own note says to pass `random.Random(seed)` for determinism"*) and `:160`, the only
call. A falsifier that is red on a green tree is not a falsifier. **Restate it against call sites, not
text:** an AST walk over `files.package_modules()` minus `tests/` counting `Call` nodes whose func
resolves to `random.Random`, asserting the set is exactly `{loop/driver.py, combat_seam.py}` after U1 —
or, cheaper and sufficient, reuse `test_season_shape.py`'s existing `_code_only_lines(path)`
(`:7900`), which is what the producer scan already uses to strip comments and docstrings.

### §2.6 · **U3 is internally contradictory: 13 CONVICTIONS and 13 AXES are different objects** *(material)*

This is the deepest correction and it changes what U3 authors.

- The season loop's roster is **`conviction_axes`** (`rosters.yaml:145-152`), sourced from
  *"#353 §14 `:334` — \"`convictions` | weights over the closed 13 | 1–3 primary + distributed | the
  moral axes\""*. It ships **4** members with `incomplete: {have: 4, target: 13, blocked_by: H-46}`.
  Its own note: *"this roster is NOT the closed 13 and must never be cited as it"*.
- `references/descriptor_registry.yaml:235-251` declares **`conviction_roster`**, `count: 13`, source
  `systems/characters/reference/conviction_taxonomy_v30.md §2` — **Faith, Authority, Order, Scholastic, Utility,
  Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor.** These are **CONVICTIONS.**
- The same file, `:258` (the `by_reference` block), declares separately: `{key: "axis.*", kind: ethical_axis, name: "4 ethical
  axes (hierarchical/sacred/instrumental/traditional)", source: "…conviction_axis_matrix_v30.md /
  PP-687"}`. **The axes are FOUR**, and `engine/substrate/keys.py::AXES` names the same four.
- **Loader invariant 8** (`04:467`): *"alignment keys ⊆ axes × verbs, and not all zero"*.

So the planner's *"`conviction_axes` ← the 13 from `descriptor_registry.yaml:235-252`"* would put
**conviction names into an axis roster**, and by invariant 8 would make `tables.alignment` a 32×13
table — while the same paragraph says *"32 verbs × 4 axes"* and *"the 128 cells"* (= 32×4). Both cannot
hold. **The coherent shape, which is what the tree's own data already supports, is three objects, not
one** — see U3 in §6 for the literal YAML.

`H-46`'s grade also survives U3 and must not be flipped: its `cite:` carries *"⚠ JORDAN, 2026-09-02,
VERBATIM: 'please note that convictions roster and axes etc may be modified in future.' **THIS ROW
THEREFORE STAYS OPEN.**"* Populating a roster from a single-owner export is a data edit — the same row
says *"the roster is a REGISTRY ROW READ AT RUNTIME, never a constant in a body, so changing it is a
data edit and not a code change"* — **and it does not close the row.** `register.py::rule_G12` exists
precisely because `H-46`'s cite once argued for a grade the row did not carry.

### §2.7 · **`register.py` rule G6 is about `absent` rows, not `assumption` rows**

Planner §6 Step 2: *"an assumption row's `cite:` records THE §0 FIVE-TEST RESULT that licensed the
injection (register.py rule G6)"*. Verified at `engine/season/harness/register.py:34` and `:240-243`:
**G6 = *"an `absent` row carries a non-empty `cite:`"***, and it reports
*"`absent` with an empty `cite:` — §0's five tests were never run on it"*. The rule the planner meant is
**R2** (`register.py:28`, `rule_R2` at `:211`): *"an `assumption` row carries a `site:` and at least
three `sweep:` points"*, with `SWEEP_POINTS = 3` and **three DISTINCT** points enforced. Both are used
in §8 Step 3, correctly attributed.

### §2.8 · **`export_sim_params.py --check` IS enforced — by a test, not by the CLI** *(material)*

The orchestrator's finding that the command is absent from CI is **verified and correct**: eight
exporters exist in `tools/`, all eight implement `--check`, **seven** are invoked in
`.github/workflows/valoria-ci.yml` at `:126, :127, :134, :137, :141, :146, :150`, and
`export_sim_params.py` appears in none of them, nor in `.githooks/`, nor in `tools/valoria_local.py`.
It has **no row of its own** in `references/ci_checks_registry.yaml` (one substring hit, at `:349`, and
it names the *artifact* `sim_params.json` inside `export_game_constants`'s `role:` string — the *tool*
name occurs nowhere in that file). **But the round-trip is not unguarded.**
`tests/valoria/test_export_sim_params.py:21` is:

```python
def test_sim_params_current():
    """Committed export == fresh extract. If this fails: run `python tools/export_sim_params.py --build`."""
    ok, msgs = esp.check()
    assert ok, "\n".join(msgs)
```

`esp.check()` **is** `--check`. That file also carries
`test_every_value_is_a_real_literal_from_source`, which re-extracts independently and compares each
record's value to the AST literal at its **definition site** — value fidelity to source, which the
orchestrator's note said was absent. `pytest tests/valoria` runs at `valoria-ci.yml:365` and is
blocking. **So the honest statement in §8 Step 3 is: the round-trip is enforced by a blocking test; the
CLI step is a convenience, and running it by hand tells you sooner, not more.**
**[CLOSED 2026-09-09 — OBSERVED.** `pytest tests/valoria -q` → **1,778 passed · 23 skipped · 15
xfailed · 0 failed**, run by the orchestrator. `test_sim_params_current` is inside that suite, so the
round-trip is green today.**]**

### §2.9 · **`sim_params.json`'s live coverage, and `CLAUDE.md` §0.05's number**

Read from the file, not from a sentence:
`python3 -c "import json;print(json.load(open('engine/engine_params/sim_params.json'))['citation_coverage'])"`
→ `{'cited': 166, 'total': 418, 'uncited': 252, 'of_which_assumption_grade': 11}`. The planner's
166/418/252/11 is **exact**. `CLAUDE.md` §0.05's `415` total / `248` uncited is stale by 3 and 4.
**Cite the file.**

### §2.10 · **`dice_engine.py` line spans, and a quote that was a paraphrase**

- The canonical die rule (`_die_result`, *"1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2
  successes. No chain."*, cited to `params/core.md §Die Rule, PP-246`) is **`:153-161`**, under its canonical-rule
  comment at **`:151-152`** — the quoted words are the comment, the function is the nine lines
  below it.
  **`roll_pool` is `:196-206`**, not `:151-206`. `_require_tn7(tn)` is its first statement, so any TN
  but 7 is refused.
- The 2026-08-14 obstacle ruling is in `degree_from_net`'s docstring at **`:242-245`**, and the words
  are *"their corresponding **score/2 plus whatever specific modifiers exist for them in that
  instance**"*. The planner's *"score/2 plus modifiers"* is a paraphrase presented as a quote.
- ⚠ **And the docstring's own 2026-09-05 correction (ED-IN-0202) is load-bearing on U1** and the
  planner does not carry it: *"there is NO SINGLE-OWNER derivation — most sites still hand-set (Muster
  1, Govern 2, DECISIVE_OB 3, the threadwork table), the three opposed sites disagree"*. Deriving `ob`
  inside `dice_seam` therefore **adds an nth site to a family the tree already records as
  disagreeing**. It is still the right call for this arc (§11 row 2), but it must be registered as an
  assumption with a sweep, not presented as adopting a single owner.

### §2.11 · **`requirements.yaml`'s stale `shape.py:NNNN` citations are 11, not 6 — and ALL of them are stale**

Measured: `requirements.yaml` carries **11** `shape.py:NNNN` citations. **Six exceed the file's 4,153
lines** and cannot resolve at all — `:5727, :6470, :6477, :6478, :6482, :6484`, all in **R-03**. The
remaining five are in range and land on unrelated code:

| cited | claims | actually at |
|---|---|---|
| `shape.py:2289` (R-03) | `class Scene` | `state/carriers.py:261` — **the row already says so** |
| `shape.py:3508` (R-08) | the chooser sorts on `(-score, verb, subject)` | `shape.py:810` |
| `shape.py:3929` (R-06) | the `Q4 -- need` source | `shape.py:1231` |
| `shape.py:3939` (R-08) | the question-tiebreak disposition | `shape.py:1245-1246` |
| `shape.py:3958` (R-08) | the `q.id` within-source tiebreak | `shape.py:1245-1246, :1260` |

**All eleven are stale.** U1's hygiene item is therefore wider than the planner scoped it, and the fix
is the same one: replace every one with `::symbol` — which survives a decomposition step, as the six
out-of-range ones did not.

### §2.12 · **U6 cannot be measured at the shipped fixture** *(material)*

Planner U6: *"`wd_chunk.py` ×4 per arm + `wd_collect.py` **at the SHIPPED fixture** (NOT the 2x1 cell —
the sweep's own correction)"*. The sweep's own correction says the opposite. `wd_acceptance.py:40-51`,
verbatim: *"MEASURED over all nine cells of the cross, 89 worlds, seed 0 (`runs/wd_cells.json`): **2 of
9 are askable — 2 x 1 (1,467 genuine forks) and 2 x 3 (733). The other seven yield 0.**"* — and the
shipped default (`scene_budget 5 × interactions_per_scene 3 = 15 slots`) is one of the seven, because
`H-117` measured that there the act budget **never binds**, so *"every probe is INERT-BY-CONSTRUCTION
and there is NO `x instead of y` moment to flip. The question is unaskable there."* The correction's
actual content is that **`2 x 3`** — one declared-arm change against `2 x 1`'s two — *"was the better
acceptance point and it was never run"*. **U6's acceptance point is `2x3`**, with `narrow` (=`2x1`) and
`default` reported beside it, which is what `wd_acceptance.py:52` already requires: *"ALL THREE fixture
points -- 15 slots, 2 slots, 6 slots -- are run and all three are reported."* A `reconvergence < 100%`
claim read off the `default` arm would be a number from a cell with zero genuine forks.

### §2.13 · **PART D row numbers, and one dropped word**

- Row 1's construction reads *"a seat enters **only** through `Act.via`"* (`04:930`). The planner drops
  *only*, which is the whole force of the clause.
- The planner's *"scripting drift … (02 §C.2, PART D 27/28)"* splits across two rows: **27** is *"a
  roster literal in a body"* (`04:957`) and **27a** is *"a proper noun in the CONTENT layer"*
  (`04:958`), whose scan domain is explicitly *"the RULE-BEARING files — the verb table, the write
  matrix, the register"* and **not** the world roster. **28** is *"a branch on a rung-kind member"*
  (`04:959`). Cite **27a/28** for U7's falsifier.
- Line numbers for every PART D row the plan uses, pinned today: header `04:928`; row 1 `:930`,
  5 `:934`, 8 `:937`, 14 `:944`, 18 `:948`, 27 `:957`, 27a `:958`, 28 `:959`, 35 `:968`, 48 `:982`.
  ⚠ The post-adoption plan's `:883,:890,:897` for rows 1/8/14 no longer resolve; `04` has grown.

### §2.14 · **U5 keys a table on a roster that does not exist, and the near-miss is the wrong one** *(material)*

Planner U5: *"`rosters.yaml` `tables.stance_delta` keyed on degree"*. `rosters.yaml` ships **31 rosters
and 3 tables** (`alignment`, `band_floors`, `site_yield`) and there is **no `degrees` roster** to key
on. The only band-shaped roster is `combat_degree_bands` (`:339`), and its own note at `:349` says
**"⚠ THESE ARE NOT THE LADDER'S FOUR BANDS AND MUST NOT BE CONFUSED WITH THEM."** Since `tell` and
`speak` resolve through the dice provider and the four-band ladder, keying `stance_delta` on
`combat_degree_bands` would silently key it on the wrong three strings. U5 carries the fix: a
**derived** `ladder_bands` roster, populated at import from `dice_engine.DEGREE_LABEL` rather than
retyped, on loader invariant 7's precedent.

### §2.15 · **Smaller corrections, listed so they are not re-derived**

| planner | tree |
|---|---|
| *"both execute in the corpus today (`requirements.yaml:204`)"* | the six executing verbs are listed at **`:203`**; `:204` is the next sentence |
| *"the no-producer scan (`:7891-7900`)"* | the scan block is **`test_season_shape.py:7887-7897`**, inside `test_we_only_a_verb_that_declares_contests_can_be_graded_today` (`:7849`); `_code_only_lines` is `:7900` |
| *"`test_w15`"* | there are **three**, not two — `…_the_run_cases_entrypoint_writes_nothing` (`:1252`), `…_report_py_reproduces_every_committed_artifact_byte_for_byte` (`:1266`, the one meant) and `…_every_case_record_in_the_caselog_equals_results_json` (`:1322`) |
| *"`test_w5_the_alignment_table_is_swept_at_three_points`"* | full name is `…_at_three_points_and_every_flip_is_printed` (`:2291`); a `-k` on the short form still selects it |
| *"`rosters.yaml:442-446`" for Jordan's granularity constraint* | that block is *"IT ENABLES EVENTS WITHOUT A SCENE"*, which opens at **`:443`** and runs to `:447`. The granularity ruling is **`rosters.yaml:455-460`**, ending *"Do not implement the tick as \"every person gets a scene per round\"."* |
| *"`rosters.yaml:485-490`" for investigation's unruled seam* | the seam table's `investigation | UNRULED` row is **`:479`**; the *"INVESTIGATION MUST NOT BE MADE A CONTEST"* note is **`:502-505`** |
| *"`proceedings/08_SEAM.md` PART B"* | path is **`proposals/2026-09-05-proceedings-subsystem/08_SEAM.md`**, PART B at `:46`, *"registers the `if` as a shim"* at `:51` |
| *"the `AX-5` three motions are seasonal"* for keeping CALENDAR once per season | AX-5's three are **matter, bodies, the fading of memory** (`01_AXIOMS.md:151`). It licenses **MATTER**. CALENDAR stays seasonal on `04 §C.1`'s barrier 1 plus D-17/D-45, not on AX-5 |
| ED-SC-0033's own cites (`shape.py:6740`, `rosters.yaml:441-446`) | stale; the literal is **`shape.py:4122`**, the prizes **`rosters.yaml:539-543`** |

---

## §3 · ENTRY STATE

**`main` = `f41f20a1`.** `engine/season/` holds `__init__.py`, `shape.py` (4,153), `combat_seam.py`
(189), `gaps.py`, `trace_log.py`, `data/`, `state/`, `harness/`, `tests/`, **`cases/`** (5 YAML at its
root plus `chain/` and `exercises/`) and **`runs/`** (the committed artifacts `report.py` re-records
and `delta.py` compares), and four YAML files: `rosters.yaml` (1,036),
`verb_table.yaml` (555), `write_matrix.yaml` (372), `hole_register.yaml` (2,746), plus
`requirements.yaml` (289) and `ENDINGS_CLASSIFIED.yaml`. ⚠ `cases/` and `runs/` were omitted from the
first draft's two listings of this tree, one of which said *"and nothing else"* — and `runs/` is what
every *"the hash does not move"* control in §6 is compared against, so the omission was not cosmetic.

**`shape.py` opens three registries at runtime** and never `hole_register.yaml` — so under §0.05 the
register is mechanism for the corpus grader and **reference for the game**.

**Nine rows, today:** R-01, R-02, R-03, R-04, R-05, R-09 `not_met`; R-06, R-07, R-08 `partial`.
Verified against `requirements.yaml`. **`register.py --requirements` is an index, not a gate** — it
validates status vocabulary, non-empty `measured:`, that a `-k` selects a real test, and that a
`python X.py` exists and contains `__main__` (`register.py:648-672`). It never compares `status:` to a
measurement, so **no `status:` flip in `requirements.yaml` is acceptance for anything in this plan**
(`CLAUDE.md` §0.2). The `measure:` line is.

**[#383]** adds `queries/{world_q,readers}.py`, `loop/{predicates,effects}.py`, `epistemic.py` and takes
`shape.py` to 2,803. It creates **no** `decision/`, **no** `seam/`, **no** `loop/driver.py`,
**no** `queries/person_q.py`.

---

## §4 · THE DEPENDENCY GRAPH

`H` = hard (cannot start, or cannot be measured). `S` = soft (cheaper if ordered).

```
  H-46 (13 convictions × 4 axes) ──S──▶ R-08 "inclination breaks a tie"  ┐
        │ = R-06a                                                        │
  R-09 producer ══H══ R-05b (contests: on corpus verbs) ──H──▶ R-07 (W-F) ├─H─▶ R-01 / R-02
        │                                                                 │    (MEASUREMENTS,
        └──S──▶ R-08 "declines the optimum" (sampling) ───────────────────┤     never built)
  R-03 scene tick ──H (R-02's intra-season half) ─────────────────────────┘
  R-05a (20 verbs) ──S──▶ R-04 ("a faction-scale ARC ends") ──▶ retirement step B
  Act.via (H-108, not one of the nine) ──H──▶ R-04
  W28 cast: blocks ──H──▶ R-06b (W27) ──S──▶ R-01
```

**Edge justifications, each verified.**

- **R-09 ⇔ R-05b — HARD, MUTUAL.** `04 §C.4:581-582` is the fold:
  `degree = FULL` then `if row.contests: degree, evs = seam.contest(...)`. A degree exists **only** for
  a verb declaring `contests:` — ⚠ **exact for Layer 1 and for COMPUTED acts, and not exact for the
  live fold**, which reads `list(a.contests or ()) or ([_row.contests] if …)` at `shape.py:3497`:
  `Act.contests` (`state/carriers.py:312`) can open one too. **No chooser sets it**, so no corpus act
  reaches the seam that way and the edge holds where this plan uses it; but a hand-built `Act` does,
  which is how every existing seam test fires and is worth knowing before writing a falsifier that
  assumes the verb row is the only door. Today that is `kill / wound` alone —
  `test_season_shape.py:7866` asserts `contested == {"kill / wound": "the body"}` — and no corpus
  person can form one, because `W23` requires *"the target must be a PERSON"* while *"today a question's
  referent is a rung or a Proposition"* (`architecture/PLAN.md:1516-1518`). A producer with no
  contested verb is a carrier with no reader; a contested verb with no producer hits
  `raise Unspecified("the degree ladder's margin model", "S39.4", …)` at `shape.py:4148`.
  **They land in one unit.**
- **R-09 → R-07 — HARD *UNDER THE CHOSEN SHAPE*, and that qualifier is not decoration.** `H-62`
  (`hole_register.yaml:715`, the shape at `:717`) records it: *"an interior write is a CONSEQUENCE OF
  AN OUTCOME, which is what the new Degree-keyed `writes` column declares"*, matching `04 §F.20a:1083`.
  ⚠ **The MECHANISM does not force it.** `write_matrix.yaml:203-209` admits any `RES`/`ACTS` write, and
  loader invariant 12 (`04:470-472`) requires a **flat** `writes:` on an uncontested verb — so a flat
  `writes: [Person.stance]` on an uncontested verb **would fold today**, with no degree anywhere. The
  edge is therefore hard **because H-62 supplied the consequence-of-an-outcome shape and this plan
  adopts it**, not because the code refuses the alternative. Adopting it is still right — an interior
  move with no outcome behind it is the inert-consequence defect `04 §F.20a` names — but it is a
  DESIGN choice inherited from a register row, and a reader must be able to see that it could be
  unwound without touching the gate. No degree on a corpus-reachable verb ⇒ under this shape
  `Person.stance` has a writer that never runs. `write_matrix.yaml:203-209` already carries the row — `steps: [RES]`, `class: ACTS`,
  `emits: "stance.moved"` — and `write_matrix.yaml:50` lists `Person.stance` among the eleven
  RES-stepped rows with no producing verb.
- **R-09, R-03, R-07, R-08 → R-01/R-02 — HARD for measurement.**
  `proposals/2026-09-04-degree-sweep/README.md:13-19` (THE HEADLINE): *"2,403 scored, all of which
  genuinely changed the act taken and the event stream written. NOT ONE changed any of the next three
  decisions. Reconvergence: 100%."* Outcome is a deterministic function of the world, so a fork's
  consequences are identical. **Measuring R-01/R-02 before a producer exists measures the theorem.**
  Both are measurements; no unit builds them (post-adoption plan §3).
- **R-03 → R-02 — HARD, intra-season half.** R-03's statement, verbatim: *"seasons must tick
  scene-by-scene, so what occurs after one scene can impact the next scene."* Today `questions_for`'s
  Q2 sets `landed = w.tick - 1` and tests `c.when == landed` (`shape.py:1202-1205`), so a decision
  reaches the **next season's** deliberation at the earliest.
- **H-46 → R-08 — SOFT for "non-optimal", HARD for "inclination breaks a tie".**
  `make_chooser` (`shape.py:773-818`) scores `sum(conviction*align)` and ranks
  `sorted(cands, key=lambda c: (-score(c), c.verb, c.subject or ""))` at `:810`, over a sparse table
  with `default_cell: 0.0`, so `corpus_run.py:488-491` prints *"RANKING DISCRIMINATION 2..7 of 22
  candidates carry a nonzero conviction score; the rest TIE and are ordered alphabetically by verb
  name"*. Sampling alone makes the choice non-optimal; only discrimination makes it **the person's**.
- **R-09 → R-08 — SOFT.** R-08's own measure is distinct top acts over seeds and needs no roll. Its
  *contribution* to R-01/R-02 does.
- **`Act.via` → R-04 — HARD.** `04 PART D row 1` (`:930`): *"a seat enters **only** through `Act.via`"*.
  `H-108` (`hole_register.yaml:1470`): *"`Act` CARRIES NO `via : SeatId?`, SO AUTHORITY IS READ OFF THE
  ACTOR AND DELEGATION IS UNBUILDABLE HERE."* Verified: `state/carriers.py:305-339` (the whole `Act`, decorator to last field) has no `via` field.
  `04 §C.4`'s fold already spells the call `gate.write(..., actor=a.actor, via=a.via)`.
- **R-05a → R-04 — SOFT.** Re-authoring (representability) needs no verb; *"a faction-scale ARC ends"*
  needs `levy / oblige / commit / establish / succeed` executing, all in the 20.
- **W28 → R-06b — HARD.** `PLAN.md:1587-1589`: W27's *"**`W28` must merge first** (both the re-scale
  and the `cast:` blocks)"*; `:1602-1607`: *"THE `cast:` BLOCKS — 143 OF THEM — WHICH THE FIRST DRAFT
  ASSIGNED TO NOBODY."*
- **R-06b → R-01 — SOFT.** `build_at` seats three persons per world
  (`corpus_run.py:201`, `for n, pid in enumerate(("p_a", "p_b", "p_c"))`); cross-person edges are
  bounded by cast size.

**Independent of everything, parallel from day one:** R-05a groups 1–2, U3's data authoring, W28's cast
authoring.

---

## §5 · COORDINATION STANCE

Steps 7, 8 and 9 of the decomposition — **owned by `workplans/2026-09-06-shape-decomposition-plan.md`
§4, which this document cites rather than restates (U0)** — are pure moves of exactly the modules
R-07/R-08/R-09 land in.
Landing R-work in `shape.py` first and moving it a step later edits the same lines twice and re-runs the
guard-blinding recurrence, which has now been measured three times (steps 2, 4, 5 — PR #383's body
records step 5's: *"Three gates read `files.SHAPE_PY` alone and did narrow"*).

Landing it **after** the carve puts each mechanism in its Layer-1 directory from its first commit, which
`04 §E.1:1046-1047` requires **for `decision/` and for nothing else** — the rule is scoped, and `seam/`
and `manifest/` are directories on `04 §A.2`'s nine-module list instead:

> **`decision/` is a directory from its first commit.** The isolation scan matches by path, so a
> `choose` drafted inside `loop/` and moved later **would have been green while violating AX-2.**

**So: merge #383; run steps 7 → 8 → 9 as three serial pure-move PRs; start R-work at U1 in `seam/`.**
Step 10 (facade deletion, re-pointing the source-scanning tests) is **deferred to the end of the arc** —
large, mechanical, and no R-unit needs it — under one rule binding from U1 onward:

> **NO NEW SYMBOL IS RE-EXPORTED THROUGH `shape.py`.** Tests import new names from their owning module,
> so the facade only shrinks.

---

## §6 · THE UNITS

Each unit states: **preconditions · files and symbols · new-file shape · new data rows · acceptance
(command + observable) · falsifier · control · hash.**

### U0 · Decomposition steps 7, 8, 9 — PURE MOVES

**Rows advanced: none. Zero game yield, stated.** Licensed as a precondition, not as progress.

⚠ **THIS UNIT CITES; IT DOES NOT RESTATE. The single owner of decomposition steps 7-10 is
`workplans/2026-09-06-shape-decomposition-plan.md`** — its §1 module suite, its §1 *"placements a lazy
pass would get wrong"* table, and its §4 migration order. **Read it for what moves.** The first draft
of this section restated ~126 lines of it — symbol inventories, per-step artifacts — with **zero**
citations of it; two documents describing one migration drift, and `CLAUDE.md` §8's *every rule lives
once* forbids the second copy. What follows is **only what the R-work found that the owner did not
have**, and **three of the five have been written back into the owner rather than kept here.**

**Preconditions.** PR #383 merged to `main`. Checkable: `git ls-tree origin/main engine/season/` lists
`loop/`, `queries/` and `epistemic.py`, and `wc -l engine/season/shape.py` reads **2,803**.

| # | delta | where it now lives |
|---|---|---|
| **D1** | **The owner's `shape.py:NNNN` do not resolve here.** Its banner scopes every citation to PR #371 at `480cb43`, a **6,771**-line file; `main` `f41f20a1` is **4,153**, and every line number in *this* document is against `main`. Cross-read by `::symbol`, which is what the owner's own step 0a exists to establish | here |
| **D2** | **`decision/`, `seam/`, `manifest/` are DIRECTORIES**; the owner's table names flat `decision.py` / `seam.py` / `loop.py`. It predates `architecture/`'s ratification (2026-09-05, ED-IN-0204). `04 §A.2:127-139` names the nine, five of which are these plus `loop/` and `queries/`; PR #383 already shipped `loop/` and `queries/` as directories. **`decision/` must additionally be one FROM ITS FIRST COMMIT** — `04 §E.1:1046-1047`, which names `decision/` and nothing else; `seam/` and `manifest/` are directories on `§A.2`'s list, a weaker warrant. **Where the owner says `loop.py`, read `loop/driver.py`** | here |
| **D3** | **`sense` moves at STEP 9 into `loop/`, not at step 7 into `decision/`** — it takes a `World` (`shape.py:1923`) and `04:133`/`:116`/`:158` place it in the loop. ⚠ **The defect was the OWNER'S**, whose `:155` ruled `decision` on the reasoning *"the guard whitelists the NAME … it must stay where the guard scans"* — inverted, since the whitelist (`test_season_shape.py:2267`) is why the violation goes **undetected**. **A whitelist is not a placement warrant** | **fixed at source**: owner `:85`, `:88`, `:155` |
| **D4** | **Step 7 re-points `test_season_shape.py:2231` in its own commit.** It parses `files.SHAPE_PY` alone and asserts `"budget" in found and "opening_set" in found` (`:2280`) — **both move at step 7** (`shape.py:515`, `:561`), so it is RED there and, repaired lazily, scans no `decision/` code. The owner's step-7 artifact (`grep 'import.*\(world\|queries\)'`) is **decorative** — case-sensitive and order-dependent, blind to `from ..state.world import World` | **fixed at source**: owner §4 step 7 |
| **D5** | **Step 8 renames a `PATH_SEAM_ALLOWED` member and `files.COMBAT_SEAM_PY` in its own commit.** The set is path-keyed and asserted by **exact equality** (`:404-424`); after the move the offender is `season/seam/combat_seam.py`. A rename **inside** a shrink-only set, not a widening. **Step 8's "17 passed" is false without it** | **fixed at source**: owner §4 step 8 |
| **D6** | **The instrument is three commands and the order is load-bearing.** `delta.py:8-12`: *"THIS COMPARISON IS VACUOUS UNLESS YOU REGENERATE `results.json` FIRST … `PROBE FLIPS 0` is TRUE BY CONSTRUCTION rather than measured. It cannot fail."* So **`report` before `delta`**. And every entry point is `python -m engine.season.harness.<x>` since ED-IN-0203; the owner's flat `python engine/season/<x>.py` spellings no longer run | here |
| **D7** | **Step 9 also writes the D-45 AST falsifier** — exactly one assignment to `w.tick` in `loop/driver.py` (`04 PART D row 45`, `:979`). The owner's step-9 artifact is `inspect.getsource` greenness, which a second tick site survives | here |

**Acceptance — verbatim, after EVERY step:**

```
python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD
python -m pytest engine/season/tests -q
python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q
```

**Expected observable:** `CONTENT HASH: ee0383bf3f4606e56b80cd07c0284f0a`; `PROBE FLIPS 0`;
**186 passed** and **17 passed** — both observed on `main` this session (§1), so a step returning
fewer has broken something rather than revealed a miscount.

**Control.** The **headless content hash plus the 186-test season suite**, above. ⚠ **NOT
`python -m pytest engine/tests -q`, which the first draft named here and in U1.** Those campaign
goldens are byte-identical to a season-package move **by construction**, not by measurement:
`engine/tests` never imports `engine.season`. `CLAUDE.md` §7 names that shape a **fake control**
(ED-MB-0066).

⚠ **AND THE FALSIFIER THE FIRST DRAFT NAMED FOR THE SEASON/CAMPAIGN SEPARATION DOES NOT EXIST.** It
wrote `test_engine_does_not_import_systems.py::test_importing_engine_pulls_in_no_subsystem`;
`grep -c "def test_importing_engine_pulls_in_no_subsystem"` returns **0**. The name survives only in
that file's docstring (`:24`), and `CLAUDE.md` §3 reproduces the same wrong name. The real function is
`test_importing_every_engine_module_pulls_in_no_subsystem` (`:358`), **and it asserts a different
thing** — that no module under `engine/` loads a file under `systems/` (`:376-392`), silent on
`engine.season` versus `mc_v18`. **The separation is real and VERIFIED BY INSPECTION:** the only file
outside `engine/season/` referencing `engine.season` anywhere in the tree is
`tests/valoria/test_import_cycle_game_state_npe.py`, and `engine/mc_v18.py` composes through
`sim.peninsular.season`, a different module. Reproduce:
`grep -rln "engine\.season" --include=*.py . | grep -v "^./engine/season/"`. Nothing guards it and,
per `CLAUDE.md` §0.1 pt 5, nothing should — the arc is not load-bearing on it.

**Hash: does not move.** A pure move that moves it is not a pure move.

---

### U1 · R-09's producer + R-05b minimal — ONE UNIT

**Rows.** R-09 `not_met` → `partial` (§7 says why not `met`). R-05 stays `not_met`; its measured line
moves from *"1 of 32 declares `contests:`"* to *"3 of 32"*.

⚠ **THE SECOND HALF OF THIS UNIT IS GATED ON §11.0'S ESCALATION AND MAY NOT BE LANDED BEFORE IT IS
RULED.** Half (a) — the provider, `manifest/`, the dispatch, the fixtures, with no verb calling them —
is unblocked and lands first. Half (b) — `contests:` on `tell`/`speak`, the prize rows acquiring
`provider: "dice"`, the third-gate amendment firing — routes social contests through a generic pool
roll, which is what §11.0 puts to Jordan. **Do not read this unit's acceptance as reachable today.**

**Preconditions.** U0 steps 8 **and 9** merged. ⚠ **CORRECTED — this read *"step 8"* and was
internally inconsistent with its own file list**, which changes `loop/driver.py::resolve` (the RNG
construction, below) and asserts a `random.Random` site set containing `loop/driver.py`; that module
exists only after **step 9**. Checkable: `engine/season/seam/__init__.py` and
`engine/season/loop/driver.py` both exist, and
`python -c "from engine.season.seam import contest, degree_of"` succeeds.

**New file — `engine/season/seam/dice_seam.py`.** Full intended shape:

```python
"""THE DICE PROVIDER — the seam's wrapper around the tree's ONE die rule.

Layer 1 `04 §A.2:164` types `seam/wrappers/*` as writing "nothing, ever", reading "the projection",
returning a Margin, holding token "none". This module is that row. It DECIDES NOTHING: it derives
a pool and an obstacle from what the actor and the subject genuinely have, calls
`engine.autoload.dice_engine.roll_pool` (`:196-206`, TN 7 refused otherwise), and returns the
net/ob pair as a dict, the shape `combat_seam` already returns and `degree_of` already grades.
It NEVER returns a band -- `seam.degree_of` reads one by calling `degree_from_net`,
which is the single owner (`dice_engine.py:227`).

⚠ THIS DOCSTRING NAMES NO BAND, ON PURPOSE AND UNDER A MEASURED CONSTRAINT.
`tests/valoria/test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan (`:447`) reads raw file
TEXT INCLUDING DOCSTRINGS, and flags any file where two or more band names appear in a
produce-shape. A prose line here spelling the four bands would redden a guard this module exists to
stay clear of. Keep it band-free.

⚠ THE PRECEDENT IS `combat_seam.py` AND IT IS FOLLOWED, NOT REINVENTED: derive exactly what the
actor genuinely has, leave every other operand at its registered fixture, and return a typed gap
rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` AND INSERTS NO `sys.path`. It reaches
`engine.autoload.dice_engine` by dotted path, which `shape.py` already does (`:3986`), so NO entry
is added to `tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED` (`:220`).
That set is still shrink-only; step 8 RENAMES one of its two members, which is U0's item, not this
module's.
"""
from __future__ import annotations
import random
from typing import Any, Optional

from engine.autoload.dice_engine import roll_pool
from ..manifest import provider


@provider("contest", "dice")
def resolve(w: Any, claimants: list[str], causes: list[str], prize: Any, *,
            verb: str, subject: Optional[str], rng: random.Random) -> dict:
    """Roll for one contested act. Returns net/ob, NEVER a band.

    RESOLVED -> dict(status, module, resolver, pool, ob, net, rolls, seed)
    REFUSED  -> dict(status, why, pool, ob)     # S27.4: ob > obstacle_refusal_multiple x pool
    """
```

**What it may import:** `engine.autoload.dice_engine`, `..manifest`, `..data.fixtures`, and the
`state/` carrier types **for reading only**. **What it may not:** anything under `systems/`; anything
under `..decision`; anything that mints a write token.

⚠ **DECLARED DEVIATION FROM LAYER 1 — the return type, stated rather than glossed.** `04 §C.5:683`
types the wrapper's return as *"a **MARGIN**. Never a winner"*, and the crossings table at `04:692`
makes it a **type assertion**: *"the subsystem returns a `Margin`; a subsystem returning a winner has
not met the contract."* **`dice_seam.resolve` returns a dict, not a typed `Margin`** — because that is
what the tree does today: `combat_seam.resolve` returns a dict, and `degree_of` (`shape.py:4035-4069`)
grades on the keys `{"net", "ob"}` (`:4050-4061`). Minting a `Margin` type for one provider while the
other returns a dict would give the seam two return shapes, which is worse than either. **What this
arc conforms to is the CONTRACT — no winner, no band, a margin pair the one ladder grades — and not
the TYPE.** Recorded here as a named deviation with its reason; typing `Margin` across both providers
is a `seam/` item of its own, sequenced beside U7 (§10), not smuggled in here.

**What enforces each, structurally.**

| discipline | enforced by |
|---|---|
| **no write, ever** | **the signature has no token parameter.** `World.write` refuses without one, and `world.py:325` refuses a step class not in the row. A wrapper with no token cannot reach the gate at all — `04 §A.2`, `04 PART D row 22` (`:952`) |
| **no second ladder** | it produces **no band string**. `tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` (`:452-474`) flags a file producing **≥2** band strings; a file producing zero cannot trip it, and cannot drift either |
| **no `systems/` reach** | `test_engine_does_not_import_systems.py`, 17 tests. `dice_seam` adds **no** entry to `PATH_SEAM_ALLOWED` (`:220`) — it inserts no `sys.path` at all. ⚠ But the set does **not** "stay": step 8 renames one member, see U0 |
| **AX-2** | `dice_seam` is in `seam/`, not `decision/`; it takes `w`, which `decision/` may never |

**New module — `engine/season/manifest/`, and it is one of Layer 1's NINE, not a file invented here.**
⚠ **CORRECTED after the adversarial pass: the first draft put this table in `seam/providers.py`, which
is a Layer-1 conformance defect in a document whose own preamble says `architecture/` is "never
overridden".** `04 §A.2:136` types the module `manifest/    role -> provider rows, resolved at boot`;
`04:125` (Stage 2 §D.4) types the mechanism *"the seam names a role; a manifest row names the
provider; resolved at boot"*; `04 §C.5:682`'s contest-seam pseudocode spells the call **by that
name** — `provider = manifest.resolve("contest", prizes[prize])   -- by string, at boot`; and build
step 10 (`04:1031`) is literally `seam/contest · manifest/ · a stub wrapper returning a Margin`, whose
proof clause is *"a misspelled manifest row fails at boot naming the row"*. The `04 §A.2` owns/reads
table (`:162-164`) lists exactly three seam rows — `seam/contest`, `seam/ladder`, `seam/wrappers/*`.
**There is no `seam/providers`, and there was never a warrant to mint one.**

So: `manifest/__init__.py` owns `PROVIDERS: dict[tuple[str, str], Callable]`, keyed `(role, module)`,
filled at import by a `@provider(role, module)` decorator on the `@effect_for` pattern
(`shape.py:2320`), and exposes `resolve(role, module)` which **raises naming the row** on a miss —
that raise is `04:1031`'s own proof clause. `combat_seam.resolve` gains
`@provider("contest", "personal_combat")`; `dice_seam.resolve` gains `@provider("contest", "dice")`.
`seam/contest.py` calls `manifest.resolve("contest", prizes[prize]["provider"])` and nothing else.
The table is a **module-level rebindable** and is exposed from its owner, per guard rule 4 (§9).

⚠ **`manifest/` is a directory because `04 §A.2:136` names it among the nine — NOT on `§E.1`'s
first-commit rule, which names `decision/` alone (`04:1046-1047`).** Two different warrants; do not
merge them.

**Changed — `engine/season/seam/contest.py`.** The literal
`if _sub["module"] == "personal_combat":` (**`shape.py:4122`** today) is **deleted** and replaced by
`manifest.resolve("contest", row["provider"])`. ED-SC-0033
(`registers/editorial_ledger_sc.jsonl:33`) rules exactly this, and the words are worth quoting
straight because a later paragraph in this document's first draft did not: *"(1) the seam dispatches
by manifest ROW rather than the hardcoded personal_combat literal at shape.py:6740"*. (`:6740` is the
ruling's own stale line; the literal is at `shape.py:4122` today — §2.15.)
`proposals/2026-09-05-proceedings-subsystem/08_SEAM.md` PART B (`:46`) is titled **THE MANIFEST ROW,
AND WHY THIS DESIGN REFUSES THE `if`-BRANCH** and *"registers the `if` as a shim"* at `:51`. **Both
sources name `manifest`, which is the second reason this arc's registry is `manifest/` and not a
file in `seam/`.**

**New data — `rosters.yaml` `contest_subsystems.prizes`, schema change.** Today (`:539-543`) it is
prize → module string. It becomes prize → row:

```yaml
    prizes:
      "the body":
        module:   "personal_combat"
        provider: "personal_combat"
        cite:     "H-88; the seam already calls it (combat_seam.py:130)"
      "a standing":
        module:   "social_contest"
        provider: "dice"          # ⚠ HELD — SEE §11.0. NOT SETTLED BY THIS PLAN.
        interim:  true
        cite:     "⚠ THIS ROW IS THE ONE ESCALATION IN THIS PLAN (§11.0) AND MUST NOT BE LANDED
                   BEFORE IT IS RULED. ED-SC-0033 (2026-09-06) rules that (2) the two contest
                   prizes that map to social_contest REPOINT TO THE PROCEEDINGS PROVIDER, and that
                   (3) THE OBSTACLE HAS A SINGLE OWNER. An interim `dice` provider derives its own
                   `ob` in-seam, which is a second obstacle site for social contests under a
                   ruling that named one owner. If Jordan rules for the interim, this row is A ROW
                   CHANGE when proceedings lands, not a code change (02 §D.4)."
      "a proposition":
        module:   "social_contest"
        provider: "dice"          # ⚠ HELD — SEE §11.0.
        interim:  true
        cite:     "as `a standing`. HELD on the same ruling."
      "a field":
        module:   "mass_battle"
        cite:     "no provider. Refuses by name as today; sides need faction_q.resolve (04 §C.5.1),
                   which is R-04/U9."
```

⚠ **This schema change breaks a live assertion and the break is intended.**
`test_season_shape.py:7872` reads `assert prizes["the body"] == "personal_combat"` — a string
comparison. It becomes `prizes["the body"]["module"] == "personal_combat"`, in the same commit.
`contest_subsystem` (`shape.py:3875-3908`) reads `roster_map(...).get(str(prize))` and matches it
against `module_contracts.yaml`'s `module:`; it now reads `row["module"]`. **Loader invariant 9** —
*"contest prizes ⊆ the subsystem roster"* (`04:467`) — is extended: **every named `provider:` must
resolve through `manifest.resolve` at load, or the load refuses naming the row** — which is exactly
`04:1031`'s *"a misspelled manifest row fails at boot naming the row"*.

⚠ **AND THERE IS A THIRD BREAK IN THAT SAME TEST, WHICH THE FIRST DRAFT MISSED.**
`test_we_only_a_verb_that_declares_contests_can_be_graded_today` (`:7849`) also carries, at
**`:7877-7883`**, a loop over `prizes.items()` doing `if sub == "personal_combat": continue`,
`assert sub in str(ei.value)` and `assert set(refused) == {"a field", "a proposition", "a standing"}`.
Under the row schema `sub` is a **dict**, so the first two are type-wrong; and once `a standing` and
`a proposition` acquire a provider **they stop refusing**, so the refused set becomes `{"a field"}`.
All three lines move in the same commit as `:7866` and `:7872`. **A unit that lands two of a test's
three breaks leaves the suite red and calls it green.**

**New data — `rosters.yaml` `verb_capability`, a new roster** (verb → capability key), and two
fixtures. Literal shape, with the schema's required fields:

```yaml
  verb_capability:
    source: "03 §A.2 -- \"Rank supplies dice and gates nothing\"; #353 §9.2 -- \"capability supplies
             dice and GATES NOTHING\" (quoted live at shape.py:854-855)."
    open: true
    cite:  "H-NNN (allocate). ASSUMPTION: the verb->key mapping is injected, declared and swept.
            08 §3's inject-declare-sweep; never refuse the whole corpus for a missing key."
    values:
      tell:   "copying"
      speak:  "copying"
```

```yaml
# data/fixtures.py DEFAULT_FIXTURES
"pool_default":     2      # register row H-NNN, grade assumption, sweep [1, 2, 4]
"obstacle_default": 2      # register row H-NNN, grade assumption, sweep [1, 2, 3]
```

Each needs a `hole_register.yaml` row carrying `grade: assumption`, a non-empty `site:` and **three
distinct `sweep:` points** — `register.py::rule_R2` enforces exactly that (`SWEEP_POINTS = 3`, and it
rejects `[2,2,2]` as *"fewer than 3 DISTINCT points"*).

**New data — `verb_table.yaml`: `tell` and `speak` gain `contests: "a standing"`,** and with it a
`Degree`-keyed `writes` and `emits`, which **loader invariant 12** requires of any verb declaring
`contests:` (`04:470-472`). See §7 for which bands and what is and is not true of Event kinds here.

**⚠ CHANGED — `resolvable_verbs()`'s THIRD GATE, AND WITHOUT THIS AMENDMENT U1's OBSERVABLE CANNOT
OCCUR. The first draft of this unit did not name it and was wrong.** `resolvable_verbs()`
(`shape.py:675`, moving to `loop/driver.py` at step 9) ends:

```python
        contested = bool(row.contests)          # shape.py:723
        if gated and effected and not contested:  # :724
            out.add(v)
```

**The moment `contests:` lands on `tell` and `speak`, both DROP OUT of the candidate set** — and
every corpus driver narrows the chooser to exactly this set: `harness/headless.py:123`,
`harness/corpus_run.py:343, :394, :503`, `harness/run_cases.py:240`, plus ~25 sites in
`tests/test_season_shape.py`. So the unamended unit would move R-05's executing count **6 → 4**,
control (a) would pass trivially, and control (c)'s hash would move **for the wrong reason**.
`architecture/PLAN.md:1510-1513` records this same gate as why a computed `kill / wound` never forms.

**The amendment, and it is narrow.** The gate's own comment (`shape.py:703-722`) states its ground:
a contested verb *"is executable only if the SEAM can return"*, and `kill / wound` is excluded
because it is UNTYPED, so `operands_for` yields `{}` and the seam would get one claimant. Neither
clause is about contesting as such. So the third gate becomes:

```python
        contested = bool(row.contests)
        has_provider = contested and manifest.has("contest", PRIZES[row.contests]["provider"])
        resolvable_contest = has_provider and row.requires_typed is not None
        if gated and effected and (not contested or resolvable_contest):
            out.add(v)
```

— *a contested verb is resolvable when a provider is registered for its prize **and** the verb is
typed, so a second claimant can be named.* `kill / wound` still fails it (untyped, `requires: —`),
which is what keeps Jordan's *"you can't just kill or wound imo."* true; `tell` and `speak` pass it
(both carry `requires_typed`, form `own_ledger`, `verb_table.yaml:479-482`). **The gate is now
`manifest`-derived rather than a bare `contests:` refusal**, which is the same
resolution-by-declaration shape the rest of this unit is built on, and it keeps one owner for the
question rather than adding a fourth.

**Falsifier for the amendment specifically:** with `tell`/`speak` declaring `contests:` and the
`dice` provider **unregistered**, `resolvable_verbs()` must still exclude them — i.e. delete the
`@provider("contest", "dice")` registration and R-05's executing count falls to 4. That is the red-before arm;
green-after is 6.

**Changed — `loop/driver.py::resolve`:** constructs the RNG and passes it down. See §7.

**Acceptance — verbatim:**

```
python -m engine.season.harness.corpus_run
python -m engine.season.harness.corpus_run 7
python -m pytest engine/season/tests -q -k dice_seam
```

**Expected observable.** `corpus_run` prints a **new** line
`DEGREES RESOLVED: {Overwhelming: n, Success: n, Partial: n, Failure: n}` with **≥3 nonzero** over the
89 worlds at seed 0, and a **different** histogram at seed 7. R-09's `measure:` is re-pointed to
`python -m pytest engine/season/tests -k 'dice_seam_is_the_only_producer or ladder_is_the_trees_own'`.

**Falsifier.** The existing producer scan
(`test_season_shape.py:7887-7897`, inside `test_we_only_a_verb_that_declares_contests_can_be_graded_today`
at `:7849`) is **rewritten** to assert the producer set is exactly `{seam/dice_seam.py}` — the
`\bnet\b\s*=|roll_pool|\bsuccesses\b` regex unchanged, `_code_only_lines` (`:7900`) unchanged, the
corpus still `files.package_modules()`. **Red today** (the set is empty and the assertion is
`assert not producers`), **green after**, **red again on any second site**. In the same commit,
`:7866`'s `assert contested == {"kill / wound": "the body"}` becomes the three-verb set, and
`:7872` moves to the row schema.

Plus, per §2.5: an AST count of `random.Random` construction sites over
`files.package_modules()` minus `tests/` returns exactly **`{loop/driver.py, seam/combat_seam.py}`**
— ⚠ **`seam/`-prefixed, because step 8 moved that file**, and a set written against the pre-step-8
path is red on arrival.
Plus `test_w9_check1_the_run_is_reproducible` (`:2652`) green: two runs of one seed are hash-identical.
Plus seed 0 and seed 7 degree histograms differ — **if they do not, the RNG is not seeded from the run
seed**, which is the failure a same-seed determinism test cannot see.

**Controls — three, and (a) is the strong one.**

- **(a) BYTE-IDENTITY, PRODUCER-WITH-NO-CALLER.** Land `dice_seam.py`, `manifest/`, the dispatch and
  the fixtures **with `contests:` NOT yet declared on `tell`/`speak`**. The headless hash must
  still read `ee0383bf3f4606e56b80cd07c0284f0a`. **A producer no verb calls is byte-invariant.** This
  separates *"the roll exists"* from *"the roll is called"*, and it is the only arm in this unit that
  can fail for the right reason. ⚠ **It is also the half of U1 that is NOT blocked by §11.0's
  escalation** — it registers a provider and calls nothing, so it commits to no prize routing.
- **(b)** the season suite (`python -m pytest engine/season/tests -q`) plus the headless hash. ⚠ **The
  first draft named `python -m pytest engine/tests -q` here and that is a FAKE CONTROL.** `engine/tests`
  never imports `engine.season` — measured: outside `engine/season/` the only file in the tree that
  references `engine.season` at all is `tests/valoria/test_import_cycle_game_state_npe.py`, and
  `engine/mc_v18.py` reaches `sim.peninsular.season`, a different module. So both arms are identical
  **by construction**, which `CLAUDE.md` §7 (ED-MB-0066) names as the shape to refuse. Running it is
  harmless; **citing it as a control is not**, and it is demoted to a smoke check here.
- **(c)** After the verb rows land, `report.py` re-records `runs/` and `delta.py HEAD` prints the
  flips; **the commit QUOTES that output.** The hash **moves** in the second half of this unit.

**Hash.** Half (a): **does not move.** Half (b): **MOVES**, recorded via `delta.py`, the old value kept
on the ledger row. Never suppressed.

**Hygiene folded in, no separate unit.** `requirements.yaml` R-02's `measure:` (`:154`) is repointed
off `wd_acceptance.py` — whose own docstring (`:54-59`) says *"`main()` … runs every arm in ONE process
and DOES NOT FINISH: two attempts were killed silently at ~18 minutes … **DO NOT CITE `main()` AS A
REPRODUCTION COMMAND**"* — onto the live path,
`wd_chunk.py <mode> <default|narrow|2x3> <a> <b>` ×4 then `wd_collect.py`. And **all eleven** stale
`shape.py:NNNN` citations (§2.11) become `::symbol`.

---

### U2 · R-03 — the scene tick at player granularity

**Rows.** R-03 `not_met` → `met` on its measure. R-02's intra-season channel opens; it is measured at U6.

**Preconditions.** U0 step 9 merged. Checkable: `engine/season/loop/driver.py` exists and
`inspect.getsource(SeasonDriver.season)` resolves inside it.

**Files.** `loop/driver.py` (`season`, `deliberate`, `witness` signatures); `queries/world_q.py::questions_for`
(Q2); `state/carriers.py::Claim` (+`round`); `harness/headless.py` (mint); `harness/corpus_run.py` (same);
`tests/`.

**Seven design decisions, each with its Layer-1 warrant.**

1. **`season()` becomes** `calendar → matter → for r in range(R): freeze → deliberate(r) → resolve →
   log.append → witness(r) → thaw → census → tick += 1`. **MATTER and CALENDAR stay ONCE PER SEASON:**
   MATTER on AX-5, whose three motions — *"MATTER, BODIES, AND THE FADING OF MEMORY"*
   (`01_AXIOMS.md:151`) — are seasonal; CALENDAR on `04 §C.1:504`'s barrier 1 plus D-17/D-21, since a
   docket forming five times a season is a fourth clock. **Rounds subdivide ACTS, not matter.**
   `R = fixtures.get("scene_budget")` (5) — the ruled unit: `state/carriers.py:261-263`,
   *"THE BUDGETED UNIT. Ruled by Jordan, 2026-09-02: **\"5 scenes for a character to play per
   season\"**"*.
2. **Rounds are a PROCEDURE** (`04 G.2.9:1317`: *"if permuting the sub-steps can change the result, the
   order **is** the mechanism and the thing is a procedure"*). Within a round, DELIBERATE stays a
   **pure map** (D-41, D-41a). **The round index is a driver local, never a carrier field** (D-21).
   `w.tick` advances once (D-45, `04:979`).
3. **A person yields ≤1 scene per round** while `spent[pid] < budget`; `ask_budget()` returns the
   remainder. This is what makes the tick player-granular — `rosters.yaml:455-460`: *"⚠ AND THE SCENE
   IS PLAYER GRANULARITY, NOT WORLD GRANULARITY… **Do not implement the tick as \"every person gets a
   scene per round\"**."*
4. **COST CONTROL, AND THE SKIP CONDITION IS WIDER THAN THE FIRST DRAFT'S.** ⚠ **The first draft
   called this a THEOREM on the condition *"a claim landed, or `sense` changed"*, and that condition
   is INCOMPLETE — measured, not argued.** `Query.opening_set` calls `person_side_eligible`, which
   reads **`p.tenures`** (`shape.py:867-870`); and `q` comes from `questions_for(w, p)`, which reads
   `p.tenures` (`:1185`, `:1231-1236`), `w.dates` / `w.docket` (`:1188-1193`), `w.crossings` (`:1225`)
   and `w.propositions` (`:1236`). RESOLVE moves tenures — `move`, `confer`, `revoke`, `transfer` —
   **without necessarily depositing a claim**, and `sense` cannot see it: `sense` returns
   `Sensation(subsistence, standing)`, two scalars (`shape.py:1923-1935`). So a person whose seat was
   revoked in round 1 would be skipped in round 2 with a stale candidate set.

   **The condition, corrected:** a person is re-deliberated in round `r` if, since their last
   deliberation, **(i)** a claim landed in their ledger, **or (ii)** `sense(p, w)` changed, **or
   (iii)** any input `questions_for` or `person_side_eligible` reads has moved for them — their
   `tenures`, or a `Date`/`DocketItem`, `crossing` or `Proposition` naming them. **The cheap
   implementation is a driver-owned dirty set stamped by the gate**, since every one of those is a
   matrix row and the gate is the one write path (`04 §A.2`): a write to `(Person, tenures)`,
   `(World, dates)`, `(World, crossings)` or `(World, propositions)` marks the affected persons
   dirty. That keeps the skip **derived from the write matrix rather than from a hand-kept list**,
   which is the same discipline §9 rule 1 states for gates.

   ⚠ **And it is a CONSTRUCTION, not a theorem.** What is provable is the converse — with none of
   (i)-(iii) and the same Sensation, `opening_set` is identical by construction, so re-running it is
   wasted. That the enumerated set is COMPLETE is a claim about the code as it stands today, and
   falsifier (b) below is what tests it. Otherwise the person takes the next scene of their standing
   ranking.
5. **Q2 reads "landed since I last deliberated".** `questions_for(w, p, since)` where `since` is the
   driver-owned `deliberated_at[pid] = (tick, round)` — a driver dict like `resolved` / `act_of`,
   whose cumulative-across-seasons discipline is stated at `shape.py:3586-3592` — and `Claim` gains
   `round: int = 0`. This **generalises** today's `landed = w.tick - 1` exactly (today `since ==
   (tick-1, 0)`). Eviction (`p.ledger.sort(key=lambda c: c.confidence * (c.when + 1))`,
   `shape.py:3825`) and decay read `when` only and are **unchanged**.
6. **ID COLLISION HAZARD, LOAD-BEARING.** `mint(pid, verb, subj) = H(seed, tick, pid,
   f"act:{verb}:{subj}")` (`headless.py:103`) gives the **same id** to the same verb/subject chosen in
   two rounds. `mint` and `pack_scenes`'s `mint(p.id, "scene", str(n))` (`shape.py:1360`) **must
   include `r` in `purpose`.** `w.new_draw()` (`world.py:495-498`, *"Reset at the start of every tick by
   `season()`"*) continues across rounds within a tick and is already unique.
7. **Keep the pinned spellings** `choose(p, v, s, ask_budget)` and `sense(p, w, subsistence)` in
   `deliberate` — `test_choose_receives_no_world` (`test_season_shape.py:620-626`) asserts both as
   source strings.

**Acceptance — verbatim:**

```
python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0 --log
python -m pytest engine/season/tests -q -k 'round or w9_check1'
```

**Expected observable.** The `--log` output prints Events with a **round column**. A new test plants a
round-1 deposit from `p_carin` about `hearth_ostvik` and asserts `p_bailiff`'s **round-2 candidate set
differs** from a control run without the plant, both arms at the same seed. (All three ids are real in
the NPC-088 world: `headless.py:40` binds `CARIN, BAILIFF, WARDEN`, `:55` the `hearth_ostvik` Rung,
`:63-64` their `contain` Tenures.)

**Falsifiers.**

- **(a)** the plant does not change the round-2 set → the channel is not intra-season, and R-03 is not
  met however the loop is shaped.
- **(b)** doubling the cast of `tiny_world` with **no** cross-person news must **not** double DELIBERATE
  calls. ⚠ **Count them from the trace log's recorded entries, not by calling the recorder:**
  `TRACE.query(name, side)` (`trace_log.py:81`) is a *recorder* returning `None`, so
  `TRACE.query("opening_set")` is both the wrong arity and the wrong direction. If the count doubles,
  decision 4 was not built.
- **(c)** two acts by one person on one subject, in rounds 1 and 2, have **distinct** ids.
- **(d)** AST: exactly one assignment to `w.tick` in `loop/driver.py`; **no `round` attribute on any
  carrier but `Claim`.**

**Control — byte-identity.** `fixtures.sweep("scene_budget", 1)` — one round — must **reproduce
today's Event multiset** for `build_world(0)` (verbs, subjects, kinds). **The single-round arm IS the
old loop.** A rounds implementation whose `R=1` limit is not the current behaviour changed two things at
once.

**Hash: MOVES.** `Claim` gains a field and `_entity_digest` is over the dataclass repr. Recorded via
`report && delta`, old hash kept on the ledger row.

---

### U3 · R-06a — the convictions and the axes (PARALLEL with U1/U2)

**Rows.** R-06 stays `partial`; its measured line's *"only 2–7 of 22 candidates carry a nonzero score"*
moves. Feeds R-08.

**Preconditions.** None. **Data only.** Can start on `main` today.

⚠ **This unit is rewritten from the planner's, per §2.6.** Three objects, not one.

**New data — `rosters.yaml`, three edits.**

```yaml
  convictions:
    source: "references/descriptor_registry.yaml `conviction_roster` (:235-251), count 13, itself
             sourced from systems/characters/reference/conviction_taxonomy_v30.md §2 and exported to
             engine/engine_params/descriptors.json behind a BLOCKING --check
             (tools/export_descriptors.py, valoria-ci.yml:137)."
    open: false
    cite: "READ, NOT RE-TYPED. H-46 stays OPEN and its grade does not move: its own cite carries
           JORDAN, 2026-09-02, VERBATIM -- 'please note that convictions roster and axes etc may be
           modified in future. THIS ROW THEREFORE STAYS OPEN.' Populating from a single-owner export
           is a data edit, which that same cite says is the correct shape; it is not a closure."
    values: [Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent,
             Community, Identity, Warden, Virtue, Honor]

  conviction_axes:                 # UNCHANGED IN COUNT. Four, and they stay four.
    source: "references/descriptor_registry.yaml:258 -- the `axis.*` by_reference row, 4 ethical axes;
             engine/substrate/keys.py::AXES"
```

```yaml
  tables:
    conviction_projection:         # NEW. 13 x 4.
      source: "systems/characters/reference/conviction_axis_matrix_v30.md / PP-687, registered by reference at
               references/descriptor_registry.yaml:259 -- the `map.conviction_axis` row, shape 13x4"
      row: H-46
      default_cell: 0.0
      sweep: [declared, uniform, sign_only]
      keys: [convictions, conviction_axes]
```

**`tables.alignment` is UNCHANGED in shape** — `keys: [conviction_axes, verb_table]`, 32 × 4 = **128
cells**, which is the figure the planner quoted and which is only correct under this reading. Loader
invariant 8 (`04:467`, *"alignment keys ⊆ axes × verbs, and not all zero"*) continues to hold with no
edit. `data/rosters.py`'s loader raises on the old four names being used as a conviction roster.
`decision/align` is unchanged in shape.

**Who authors, and what each cell carries.** The 128 alignment cells and the 52 projection cells are
**GAME CONTENT.** Each carries a one-line reason and a `source:` — `PP-687` /
`conviction_axis_matrix_v30.md §2` where one exists, and the assumption grade where it does not.
Post-adoption plan §6 trap 14: *"Jordan CHANGES cells; he does not AUTHOR them."*

**Acceptance — verbatim:**

```
python -c "import engine.season.shape"
python -m engine.season.harness.register --check
python -m engine.season.harness.corpus_run
python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
```

**Expected observable.** The import succeeds — ⚠ **the loader's cross-checks fire at import, which is
NOT the same as *"the twelve invariants fire at import"*, and the first draft wrote the stronger
sentence.** `engine/season/data/*.py` names exactly one of §B.13's twelve by number (invariant 12,
`data/verbs.py:92`, `:201`); several others are implemented under other names (`data/fixtures.py`'s
register-row refusals are invariant 11's shape, `data/requires.py:532-599` is the seven-form check),
and **invariant 7 is not implemented at all** (`04 §F.20b:1084`). What this acceptance observes is
that the loaders raise on this unit's data, which is what it needs; it is not a twelve-for-twelve
claim. `corpus_run`'s
`RANKING DISCRIMINATION` line changes — **recorded, not targeted**; `headless` still runs.

**Falsifier.** Any verb with **zero** alignment cells can never discriminate and fails the loader. And
`test_w5_the_alignment_table_is_swept_at_three_points_and_every_flip_is_printed` (`:2291`) must still
flip **≥1** verdict between `declared` and `uniform` — **if none flips, the table is inert**, which is
the dead-carrier defect `rosters.yaml:994-998` names: *"a zero matrix makes convictions inert … it
would pass every test while meaning nothing"*.

**Control.** The **`uniform` arm** — every cell equal — which already exists as
`tables.alignment.sweep`'s declared control (`rosters.yaml:999`, *"`uniform` IS THE CONTROL, not a
third opinion"*).

**Hash: MOVES** (person convictions score against a changed table). Recorded via `report && delta`.

---

### U4 · R-08 — non-rational choice

**Rows.** R-08 `partial` → `met` on its measure.

**Preconditions.** U0 step 7 merged **and** U3 landed. Checkable: `engine/season/decision/` is a
directory, and `roster("convictions")` returns 13 members.

**Files.** `decision/` (`make_chooser`), `loop/driver.py` (constructs and passes `draw`).

**The change.** Rank exactly as today, then **sample** `softmax(score / tau)` with a per-person draw.
`tau` is a fixture — assumption, swept `[0, tau_default, 2*tau_default]`. **`choose`'s four-parameter
signature is UNCHANGED**, which `test_choose_receives_no_world` (`:620-626`) pins as a source string.
The RNG reaches the chooser the way `mint` does: a factory
`draw(pid, purpose) -> random.Random(int(H(seed, tick, pid, purpose), 16))`, **closed over the clock by
the driver** and passed into `make_chooser(fx, mint, verbs, draw)`. The precedent argument is
`shape.py:790-795`, in `make_chooser`'s own docstring: *"⚠ `mint` IS HERE BECAUSE §F2 TYPES
`choose -> Act[]` AND GIVES THE PERSON NO WAY TO MINT ONE … Same shape as `fx`, and the AST proof still
sees no `World`."* **The clock is not anybody's interior.** The draw `purpose` includes the round (U2).

**`decision/` from its first commit** — `04 §E.1:1046-1047`, quoted in §5, **which names `decision/`
and nothing else.** Not drafted in `loop/` and moved.

**Acceptance — verbatim:**

```
python -m pytest engine/season/tests -q -k 'sampling or w5_sense'
python -m engine.season.harness.corpus_run
```

**Expected observable.** The same person and view over **20 seeds** yields **≥2 distinct top acts**;
`corpus_run`'s `DISTINCT EXECUTED SETS` rises from 2; the tie-ordering line changes.

**Falsifier — and it is a byte-identity one, with a caveat the prior plans do not carry.**
**`tau = 0` must be BYTE-IDENTICAL TO HEAD** for `build_world(0)`: same content hash, same Event
multiset. A sampler whose zero-temperature limit is not the old ranking changed two things at once.

⚠ **BUT τ→0 IS NOT THE LIMIT OF THIS SAMPLER ON THIS DATA, AND THE ARM MUST SAY WHAT IT ACTUALLY
CONTROLS.** `corpus_run.py:488-490` prints that only *"2..7 of 22 candidates carry a nonzero conviction
score; the rest TIE and are ordered alphabetically by verb name"*. The zero-temperature limit of a
softmax over **tied** scores is **uniform over the tied set**, not the alphabetical
`sorted(cands, key=lambda c: (-score(c), c.verb, c.subject or ""))` at `shape.py:810`. So byte-identity
at `tau = 0` requires a **discontinuous special case** — `if tau == 0: return ranked` — and that case
then exercises the OLD path rather than the sampler's limit. **State it plainly: the `tau = 0` arm
validates the plumbing (the draw is threaded, the signature is unchanged, nothing else moved), not the
sampler.** The sampler's own control is U3's `uniform` alignment arm plus the 20-seed spread above.
Both prior plans name the `tau = 0` arm independently and neither notices this; the error is inherited
and is corrected here rather than reproduced.

**Control.** The `tau = 0` arm above, **and** the structural one:
`test_w5_sense_is_still_the_only_world_taking_non_decision_function` (`:2224`) still finds no `World`
in any `decision/` signature.

**Hash: MOVES at shipped `tau`; DOES NOT MOVE at `tau = 0`.** Both recorded; the second is the control.

---

### U5 · R-07 — W-F: an outcome moves `Person.stance`

**Rows.** R-07 `partial` → `met` on its measure. R-08's *"inclination"* gains a live input.

**Preconditions.** U1 **half (b)** merged — ⚠ **which is gated on §11.0's escalation**, so this unit
cannot start until that is ruled. Checkable: `corpus_run` prints a non-empty `DEGREES RESOLVED:` line.

**Files.** `verb_table.yaml` (the contested verbs' degree-keyed `writes:` gain `Person.stance`; their
`emits:` gain `stance.moved`); `loop/effects.py` (`_eff_tell` / `_eff_speak` — **NEW**, since these verbs
have no effect today; `_eff_kill` gains the same on `Wounded`); `rosters.yaml` `tables.stance_delta`;
`decision/stance_toward` **unchanged**.

**The write.** A stance row `(referent=actor, valence, weight)` on the **subject**, written through
`w.write(...)` under the **ACTS** token at RESOLVE. `write_matrix.yaml:203-209` already carries the row
and needs no edit: `kind: Person`, `field: stance`, `steps: [RES]`, `class: ACTS`, `social: "true"`,
`emits: "stance.moved"`.

**AX-3 warrant.** Stance is *what is held right*; it is moved **by consequence at RESOLVE** —
`01_AXIOMS.md:114`: *"Evidence moves what is held true. **Argument and consequence move what is held
right.**"* The writer takes **no ledger reference** — `04 PART D row 18` (`:948`): *"The INTERIOR write
is performed by a function whose signature takes `PersonInterior` **and no ledger reference**, exactly
as `choose` takes no `World`… **STRUCTURAL by signature**."* **PER-REFERENT ROWS, NEVER A SUMMED
FIELD** (D-8, `:937` — *"a stored aggregate … no field slot"*).

**New data — `rosters.yaml`: a DERIVED band roster, then `tables.stance_delta` keyed on it.**

⚠ **There is no `degrees` roster to key on, and the one that looks like it is the wrong one.**
`rosters.yaml` ships 31 rosters and 3 tables; the only band-shaped roster is `combat_degree_bands`
(`:339`), whose own note at `:349` says **"⚠ THESE ARE NOT THE LADDER'S FOUR BANDS AND MUST NOT BE
CONFUSED WITH THEM."** `tell` and `speak` resolve through the dice provider and the four-band ladder,
so `stance_delta` needs *those* four. **Do not retype them** — that would be a second copy of a
definition `dice_engine` owns, which is what S27.2 and §8's roster rule refuse. **Derive the roster at
import from `DEGREE_LABEL`**, on loader invariant 7's precedent (`04:466`, the Event-kind roster is
*"**derived** from every emission column"*):

```yaml
  ladder_bands:
    source: "DERIVED AT IMPORT from engine.autoload.dice_engine.DEGREE_LABEL -- the single owner of
             the four bands (degree_from_net, dice_engine.py:227). NOT RETYPED: a literal list here
             would be the second resolver S27.2 refuses, and would go on answering after the owner
             changed its mind."
    open: false
    cite: "H-NNN (allocate). ⚠ NOT `combat_degree_bands` (:339), whose note at :349 states these are
           NOT the ladder's four bands."
    values: []          # populated by data/rosters.py at load; the loader raises if it is empty
```

```yaml
    stance_delta:
      source: "H-62's supplied shape (hole_register.yaml:715): an interior write is a CONSEQUENCE OF
               AN OUTCOME. The magnitudes are INVENTED and this row is what makes that lawful."
      row: H-NNN            # allocate; grade assumption
      default_cell: 0.0
      sweep: [declared, none, doubled]      # three DISTINCT points -- register.py::rule_R2
      keys: [ladder_bands, verb_table]
```

**Acceptance — verbatim:**

```
python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0 --log
python -m pytest engine/season/tests -q -k stance
```

**Expected observable.** After two seasons, **≥1 person carries a nonzero stance row**, and
`stance.moved` appears in the log with `causes=[<act id>]`.

**Falsifiers.** An effect that writes stance **outside** `w.write(...)` fails
`test_w2_every_write_call_site_names_a_pair_on_the_matrix` (`:1673`). A stance write attempted under the
**INTERIOR** token is refused by the gate at `state/world.py:325` — the row's `steps` is `[RES]` only,
so `step not in allowed` fires. And the `none` arm below is a falsifier as well as a control.

**Control — on the harm-model pattern already in the tree, but NOT a byte-identity one, and the
first draft got this exactly backwards.** `rosters.yaml`'s `wound_harm_models` roster (`:360`; the
magnitude row is **`H-123`** — ⚠ its `cite:` reads `H-125`, and **`H-125` is not a row**:
`grep -n 'H-125' engine/season/hole_register.yaml` returns nothing. The roster's own citation is
stale; cite `H-123`, and do not propagate `H-125`) carries two declared control arms and names both:
*"⚠ `total` IS THE CONTROL AND IT IS THE CODE AS IT STOOD"* (`:370`) and *"`none` is the SECOND
control and isolates the other half: a wound writes nothing, **the fold's own write-nothing guard
emits the REFUSAL instead of the success**, and what is left is only the difference the SELECTED WRITE
SET makes"* (`:374-376`).

⚠ **READ THAT SECOND CLAUSE — IT IS THE ANSWER, AND IT SAYS THE HASH MOVES.** With `Person.stance` in
`tell`'s degree-keyed `writes`, `row.writes` is non-empty, so the fold takes the effect path
(`shape.py:3320`, `_pairs = row.writes_at(_degree) if row.writes else ()`), **demands an effect**
(`:3321-3331`), and — if the effect changed nothing, which is exactly what a zero `stance_delta`
produces — **returns `emits_on_refusal` instead of the success** (`:3352-3357`). So on the `none` arm
every successful `tell` emits `news.untold` in place of `news.told`, and **THE CONTENT HASH MOVES.**
The alternative shape (a zero-magnitude stance ROW written rather than no write) leaves `p.stance`
non-empty and fires `stance.moved`, so it fails the other half of the arm; and `state/world.py` has no
before-equals-after refusal to fall back on (`04 §F.20b`-adjacent: `04:558-562` records that as
unimplemented).

**So the `none` arm is stated correctly as this, and it is still worth running:** `Person.stance` stays
**empty** (no stance row on any person) and the log carries **no** `stance.moved`; every `tell` that
would have succeeded emits its declared refusal kind instead, and **the hash moves in a way whose
every flip `delta.py` can name.** *"If a zero table still moves stance, the delta is not the
mechanism"* survives unchanged — that is the falsifier. What does not survive is *"byte-identity"*.

**Hash: MOVES on the `declared` arm; MOVES on the `none` arm too, differently and for a stated
reason.** Both recorded via `report && delta`. ⚠ **U5 therefore has NO byte-identity control**, which
is a real weakness and is declared rather than papered over: the nearest thing to one is U1 control
(a), the producer with no caller, which is upstream of this unit.

---

### U6 · R-01 / R-02 — FIRST MEASUREMENT

**Rows.** Flip **only on the number.** No unit builds R-01 or R-02 (post-adoption plan §3:
*"R-01 and R-02 are measurements"*).

**Preconditions.** U1, U2, U4 and U5 all merged.

**Instrument.** `wd_chunk.py <mode> <slots> <a> <b>` ×4 per arm — slices `0 23`, `23 46`, `46 69`,
`69 89` — then `wd_collect.py`. `arm9_forking.fork_case` is imported **UNMODIFIED**
(`wd_acceptance.py:3-7`: *"⚠ THIS FILE BUILDS NO PROBE… a re-implemented probe measuring a different
thing is the confound that would waste the item"*). Plus `corpus_run`'s R3 line and its
`planted_control` (`corpus_run.py:431-453`, printed at `:535-537`).

**⚠ The acceptance point is `2x3`, not the shipped default — see §2.12.** All three fixture points are
run and all three reported, which `wd_acceptance.py:52` already requires.

**Acceptance — verbatim:**

```
cd proposals/2026-09-04-degree-sweep
for m in none actor total; do for s in default narrow 2x3; do \
  for r in "0 23" "23 46" "46 69" "69 89"; do python wd_chunk.py $m $s $r; done; done; done
python wd_collect.py
cd - && python -m engine.season.harness.corpus_run
```

**Expected observable.** Reconvergence **strictly < 100%** at `2x3`; `runs/wd_cells.json` committed;
the R3 count and the planted control both printed.

**Falsifier.** Reconvergence **≥ 96%** → **report which channel is still closed** and leave both rows
`not_met`, honestly. Both prior plans carry this clause and it is not optional.

**Controls.** `observation_deposit_mode=none` arm ≥ the default arm — **that is the only control this
instrument produces**, because `wd_acceptance.py::sweep_arm` (`:132-140`) sweeps
`observation_deposit_mode` and the two slot fixtures **and nothing else** (the three modes are
`rosters.yaml:337`, `[none, actor, total]`).

⚠ **`fan_out_mode` IS NOT U6'S FIXTURE AND `wd_chunk` NEVER VARIES IT.** The first draft listed a
*"`fan_out_mode=total` arm"* here as if this instrument produced it; it does not.
`fan_out_mode` is **R-07's own** fixture (`requirements.yaml:242`), and its control is internal to its
own falsifier — *"`test_r7_two_persons_hold_different_things_and_at_total_they_cannot`, whose control
is the `total` arm inside the same test"* (`requirements.yaml:248-249`). **Cite it where it lives and
do not claim it as an arm of this measurement.** ⚠ Note the value `total` appears in **both** rosters
and means different things in each; that shared spelling is what produced the confusion, and is worth
a `note:` on whichever roster is edited next.

**Hash: not applicable** — this unit changes no code.

---

### U7 · R-05a — the 20 verbs, in blocker groups (PARALLEL from U0 onward)

**Rows.** R-05's `WHERE THE 32 GO` line.

**Preconditions.** Groups 1–2: none beyond `main`. Group 3: the `dispensation` operand row and F.15's
nine terms exist as data (§8's worked instance). Group 4: **de-scoped** (§10).

**Files.** `verb_table.yaml` (`requires_typed` in **one of the seven forms**, `rosters.yaml
requires_forms` at `:880`); `loop/predicates.py` **only where no form fits**; `loop/effects.py`;
`write_matrix.yaml` rows the writes need.

**The 20 rows, exhaustively, and the arithmetic that proves it.** `verb_table.yaml` holds 32 rows.
Six execute today (`requirements.yaml:203`: `create_record, move, speak, tell, transfer, utter`); six
more are foldable-but-unattempted or attempted-and-refused (`confer, convene, dispatch, kill / wound,
revoke, work`). **The remaining 20 are these**, and note `tie / knot`, `evade / defy` and
`the six investigation acts` are each **one row**:

| group | rows | count |
|---|---|---|
| **(1) no hole, merely unbuilt** — `PLAN.md:1649-1651` W31(a) **verbatim** | `commit`, `repudiate`, `oblige`, `tie / knot`, `forge`, `petition`, `carry`, `succeed` | 8 |
| **(2)** — this plan's subdivision of W31(b) | `restore`, `exchange`, `levy`, `establish`, `open_case`, `destroy_record`, `determine` | 7 |
| **(3) the Dispensation four** — W31(b) | `comply`, `evade / defy`, `refract`, `issue` | 4 |
| **(4) the six investigation acts** — W31(b), **DE-SCOPED** | `the six investigation acts` | 1 |

⚠ **`PLAN.md` W31 has TWO groups, not four** — (a) *"No hole, merely unbuilt"* and (b) *"Hole-gated —
each lands only when its row moves by §0's ladder"*. Groups 2–4 above are this plan's subdivision of
(b), and (b)'s own criterion governs each of them.

**`commit` first.** `PLAN.md:1649-1651`: *"⚠ **`commit` first**: `Q4` (a live `commit` to an OUGHT) is
the only question source that fires in a quiet season, and **no verb can create one** — every world
seeds it by hand."* Q4 lives at `shape.py:1231` (**not** `:3929` — §2.11) and moves to
`queries/world_q.py::questions_for` **[#383]**.

**Group 3 is a PROSE→CODE TRANSLATION ITEM, not a wiring item** — see §8's worked instance.

**Acceptance, per verb — verbatim:**

```
python -m engine.season.harness.corpus_run   # 'WHERE THE 32 GO' line
```

**Expected observable.** `corpus_run`'s executed set gains the verb in **≥1 world — in the corpus**,
not merely in a hand-built `Act` handed to `resolve`. `PLAN.md` W31's own Proof line says exactly this.

**Falsifiers.** An effect that branches on a **proper noun** (`04 PART D 27a`, `:958` — scan domain is
the rule-bearing data files: the verb table, the write matrix, the register) or on a **rung-kind
member** (`row 28`, `:959` — the falsifier IS the mechanism: re-run the seeded season with `rung_kinds`
extended by a synthetic kind and permuted; any test that moves branched on a member) is **scripting
drift** and is rejected at review. `writes:` ⊆ matrix rows is **loader invariant 1** (`04:456`), for
every `Degree` branch of a degree-keyed verb. A refusal **emits** `emits_on_refusal` and never raises —
`04 PART D row 7` (`:936`), with **invariant 4** (`04:459-462`) requiring a refusal kind for **each
conjunct** of a `requires`.

**Control.** `report && delta HEAD` **per group** — no probe flips **outside** the group's verbs.

**Hash: MOVES per group.** Recorded per group, never batched into one unattributable move.

---

### U8 · R-06b — `ambitions(p)` and the cast from the case

**Rows.** R-06 toward `met`.

**Preconditions.** U0 step 7 merged (for `queries/person_q.py`) **and** W28's `cast:` blocks authored
for at least the NPC lane. `PLAN.md:1587-1589`: W27's *"**`W28` must merge first**"*, and `:1600-1607`
records that the 143 `cast:` blocks were *"ASSIGNED TO NOBODY"* — median 4 entries, max 11, with
non-actor entries (*"~44 of 97 ARC cases name a player, a PC or the party"*) becoming
`WAITS-ON-PLAYER` **as part of the deliverable**.

**Files.** `queries/person_q.py::ambitions(p) -> list[PropositionId]` — a **READ** over the mechanism
`requirements.yaml` R-06 already names: *"a person's motive is expressed as a `commit` Tenure to an
OUGHT Proposition"*, seeded at `harness/headless.py:72-75` (`S.Proposition("prop_einhir", "OUGHT", …)`
plus `S.Tenure("t_carin_commits", CARIN, prop.id, "commit", since=0)`).
`harness/corpus_run.py::build_at` (`:169`) reads a per-case `cast:` block: `who_acts` → persons /
offices, `one_line` → the OUGHT, `knowledge` → initial Claims. **NPC lane (46 cases) first.**

**Acceptance — verbatim:**

```
python -m engine.season.harness.corpus_run
python -m pytest engine/season/tests -q -k 'ambitions or cast'
```

**Expected observable.** `DISTINCT EXECUTED SETS > 2`; the Q4 `need` source fires for **more than one**
proposition; a case with **11 actors** runs.

**Falsifiers.** `ambitions` is **person-side**: no `World` in its signature — the AST guard
`test_w5_sense_is_still_the_only_world_taking_non_decision_function` (`:2224`). And `one_line` is
**PARSED into a `cast:` block by an author, never token-matched** — the W10 router lesson, which
`harness/exercises.py:12-20` records. **[CLOSED — READ 2026-09-09.** Verbatim: *"the fix is NOT to add
`threat`. Adding the word is what was done at recurrences two, three and four. The fix is `W10`:
delete the router. **A roster of words IS a specification, and nobody ratified this one.**"* — with
`:17-20`'s addendum that a pattern-router's published count *"was a FLOOR, NOT A TOTAL … every figure
derived from routing understated the corpus in the direction that flattered it,"* while *"a row with
no `exercises:` is VISIBLY unauthored."* Both halves support the claim as made.**]**

**Control.** The pre-cast arm: with `cast:` blocks absent, `build_at` still seats three persons
(`corpus_run.py:201`) and the corpus tallies are unchanged. Cast size is the only variable.

**Hash: MOVES** for any case gaining a cast. Per-lane, recorded.

---

### U9 · R-04 — strategic scale

**Rows.** R-04's `unrepresentable scales:` line — 54 of 143 today (44 faction, 10 world).

**Preconditions.** U7 groups 1–2 merged (`levy`, `oblige`, `commit`, `establish`, `succeed` execute)
and U8's NPC-lane cast landed.

**Files.**

- `state/carriers.py::Act` gains `via: Optional[str] = None` — **H-108** (`hole_register.yaml:1470`).
- `state/world.py::write` gains AX-4 clause 2's Tenure branch, with **`via` REQUIRED for `T-o`**:
  `04 §C.2`'s F3 block, *"`via` is a Seat whose `revocation` basis reaches it — `T-o`, and `via` MUST
  be present"*, and *"a revocation with no seat in `Act.via` is"* refused. `04 PART D row 10a`
  (`:940`) grades it MECHANICAL at the gate.
- `queries/world_q.py`: `holdings(w, prop)`, `purview(w, seat)`, `superiors(w, person)`,
  `subordinates(w, seat)`, `at_war(w, a, b)` — **QUERIES, NEVER FIELDS**. `04 PART D row 8` (`:937`),
  `row 14` (`:944` — *"`Faction.holdings` is a Query that READS members' holds and cannot write one"*),
  `row 48` (`:982` — *"`at_war` is a Query over the live ones… There is no boolean between two factions
  to set"*).
- `rosters.yaml`: a `scale_of_rung` mapping from the eight `rung_kinds` to canon's five scales
  (`systems/_architecture/reference/scale_transitions_v30.md` §2, `:26` — **THE SCALE SET ONLY**; its *"Base Ob"*
  column is thread-only and is **not an obstacle source**, Jordan 2026-09-05).
  **[CLOSED — READ 2026-09-09, AND IT RAISES A PROBLEM THIS UNIT MUST SOLVE RATHER THAN INHERIT.**
  §2's five scales are **Object · Personal · Relational · Territorial · Structural**, with columns
  *Scope · Base Ob · Min Thread Sensitivity · Coherence auto-cost · Examples*. ⚠ **That vocabulary is
  not the corpus's.** A case's `scale:` is filtered against `RUNG_KINDS` (`wd_acceptance.py:148`,
  `str(c.get("scale")) in set(S.RUNG_KINDS)`), and `rung_kinds` is the eight
  `person · hearth · community · settlement · territory · province · duchy · realm`
  (`rosters.yaml:89`). **Neither `faction` nor `world` — the 44 + 10 unrepresentable cases — appears
  in EITHER list.** So a `scale_of_rung` mapping from the eight rungs onto §2's five does **not**, by
  itself, make a faction- or world-scale case representable; what those cases need is a scale
  vocabulary that admits them, which is the re-scale/rule decision `corpus_run.py::rescales` (`:74`)
  and `PLAN.md:1613-1617` are about. **U9 must state which of the two problems its mapping solves
  before it is written**; the first draft implied one row solved both.**]**
- `harness/corpus_run.py::rescales` (`:74`): re-scale the 44 faction cases with `why:`; rule the 10
  world cases as **≥2 realm rungs** — `PLAN.md:1613-1617`, *"By §0 test 5… Recorded on `H-95` and
  removed from §9.0's escalation list. Jordan may overturn it; that is a ruling, not an open question
  this plan waits on."* `levy` executes through a seat.

**Acceptance — verbatim:**

```
python -m engine.season.harness.corpus_run   # 'unrepresentable scales:' line
python -m pytest engine/season/tests -q -k 'via or scale_of_rung'
```

**Expected observable.** `unrepresentable scales: {}`, or ≤ what W28 rules out; **≥1 faction-scale ARC
ends**; a `levy` executes with `Act.via` set.

**Falsifiers.** A stored `L`/`Sta`/`Mil` field, a `Faction` passed where a `PersonId` is required, or a
write by a banner is a **rejection at review** (`04 PART D rows 1/8/14`). The permuted-`rung_kinds` run
(`row 28`, `:959`) stays green — **that one is a real falsifier**, because it changes data and observes
behaviour. ⚠ `grep -rn 'superior\|liege\|rank' engine/season/state/` showing **no field** is
**TERM-MATCHING, not structural**: it is green today and blind to a hierarchy field spelled any other
way (`above`, `patron`, `over`, `seat_parent`). Keep it as a cheap smoke check and do not present it
as the guard; the structural version is an AST walk over `state/carriers.py`'s dataclass fields
asserting that no field on any carrier holds a `SeatId`/`PersonId` denoting a superior — **which is
work this arc does not do**, so the honest statement is that this falsifier is weak and named as weak.

**Control.** The loop's existing **person / settlement / realm** cases run **unchanged** under the
mapping. If a mapping that only adds faction and world scale moves a person-scale case, the mapping is
not a mapping.

**Hash: MOVES** for re-scaled cases only; **must NOT move** for the person/settlement/realm cases —
that is the control, stated as a hash claim.

---

### U10 · Second measurement, status flips, THEN step 10

Repeat U6's instrument after U7/U8/U9. Flip `status:` **only on the numbers U6 and U10 printed** — a
`status:` flip is never acceptance (§3). Then run decomposition **step 10**: delete the `shape.py`
facade and re-point the source-scanning tests. `files.SHAPE_PY` (`data/files.py:133`) is deleted with
it, so any survivor raises `NameError`, **which is the good case** (§9 rule 3).

---

## §7 · WHERE R-09's ROLL GOES

**Owner: `engine/season/seam/dice_seam.py`.** Layer-1 `seam/wrappers/*` — `04 §A.2:164`, whose row
reads: `| seam/wrappers/* | **nothing, ever** | the projection | a `Margin` | **none** |`. It has no
token and writes nothing; it returns the subsystem's own result, which `degree_of` (moving to `seam/` at
step 8) grades through **the one ladder** — `shape.py:4050-4061`, `label[degree_from_net(result["net"],
result["ob"])]`.

⚠ **ONE HALF OF THAT ROW IS FOLLOWED IN CONTRACT AND NOT IN TYPE, AND THIS PLAN SAYS SO RATHER THAN
CLAIMING CONFORMANCE IT DOES NOT HAVE.** `04 §C.5:683` types the return *"a **MARGIN**. Never a
winner"*, and the crossings table (`04:692`) makes that **a type assertion**. `dice_seam.resolve`
returns a **dict**, as `combat_seam.resolve` does today and as `degree_of` grades (`{"net", "ob"}`).
What is honoured is the contract — **no winner, no band, a margin pair the one ladder reads** — and
what is deviated from is the type. A typed `Margin` for one provider and a dict for the other would
give the seam two return shapes, which is worse than either; typing both is its own `seam/` item
(§10), not a thing to smuggle in here. **Named deviation, with its reason, so a later reader does not
find it and conclude Layer 1 was ignored.**

The "subsystem" it wraps is `engine/autoload/dice_engine.py::roll_pool`
(**`:196-206`** — §2.10), whose die rule is the tree's only one (`_die_result`, `:153-161`, *"1 = -1
success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain."*, cited to `params/core.md §Die Rule,
PP-246`) and which refuses any TN but 7 via `_require_tn7`. ⚠ **`roll_pool` is not the file's only
net-producer** — `continuous_engine_sample` (`:209-223`) samples a fractional net from
`Normal(μ·N, σ·√N)`, the Godot-canonical continuous mode, and is the second. **Calling the discrete
one is a CHOICE**: the corpus is integer-pooled and `degree_from_net` reads either, so the choice is
reversible behind an unchanged seam. Stated because *"the tree's only one"* is true of the **die
rule** and false of the **net**, and a reader running the grep would find the second. The shape
precedent is `combat_seam.py`: derive exactly what the actor genuinely has, return a typed gap rather
than fabricate.

### Why this is not the second resolver `T-k` refuses, and not the "generic roll" the roster refuses

`rosters.yaml:514` opens the `contest_subsystems` note with *"⚠ A CONTEST IS A DISPATCH, NOT A GENERIC
ROLL."* Two answers below — ⚠ **and they answer only ONE of the two things that note says.** The
note's own continuation is about **calling the owning subsystem**: *"the three subsystems it should be
calling ARE BUILT … So the seam was not missing a ladder; it was failing to dispatch"* (`:515-520`),
and `:529-530` carries Jordan verbatim on these very prizes — *"we don't NEED to worry about them at
this point in time."* **A bare pool-vs-fixture roll standing in for a social contest is the generic
roll that note refuses, whatever the dispatch mechanism around it.** The answers below dispose of the
`if`-routing half and of the second-ladder half; they do **not** dispose of that half, and §11.0 is
where it goes.

1. **The provider returns `net`/`ob`, NEVER a band.** The band is read by `degree_of` calling
   `degree_from_net`, and that identity is already pinned:
   `test_we_the_ladder_is_the_trees_own_and_not_a_copy_of_it` (`:7798`) asserts
   `lad[0] is degree_from_net and lad[1] is DEGREE_LABEL` and then **replaces `S._LADDER` and requires
   every band to move with it**. A wrapper producing no band string also cannot trip
   `tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` (`:452-474`),
   which flags a file producing **≥2** band strings.
2. **The `if`-routing half: this is a provider resolved by ROW, through `manifest/`.**
   `04 §C.5:682`, verbatim: `provider = manifest.resolve("contest", prizes[prize])   -- by string, at
   boot`. Dispatch by row is the shape the note **asks for**, and ED-SC-0033's point (1) rules it:
   *"the seam dispatches by manifest ROW rather than the hardcoded personal_combat literal"*. ⚠ Note
   what the ruling names — **`manifest`**, which is why the registry in U1 is `engine/season/manifest/`
   (`04 §A.2:136`, `04:125`, `04:1031`) and not a file under `seam/`.

### Signature

```python
dice_seam.resolve(w, claimants, causes, prize, *, verb, subject, rng) -> dict
  # RESOLVED
  dict(status="RESOLVED", module="dice", resolver="dice_pool",
       pool=<int>, ob=<int|float>, net=<int>, rolls=[...], seed=<int>)
  # REFUSED -- ob > obstacle_refusal_multiple x pool
  dict(status="REFUSED", why="S27.4", pool=..., ob=...)
```

`degree_of` grades `{"net", "ob"}` **unchanged** (`shape.py:4050-4061`). `SeasonDriver.resolve` maps
`REFUSED` to the **existing** `attempt.refused` Event at `shape.py:3470-3486` — **which no CHOSEN act
reaches today**, because `Act.obstacle` defaults to `None` (`state/carriers.py:332`) and the chooser
never sets one. ⚠ **"Nothing sets it" would be false and the first draft said it:** `harness/probes.py:2373-2374`
builds `speak` Acts with `obstacle=` by hand, and `test_season_shape.py:3125` assigns
`a.obstacle, a.pool` directly to exercise the gate. The gate is reached today **by hand and never by
the loop**, which is the narrower true claim and the one that makes the provider's input new.

⚠ **AND S27.4 THEN HAS TWO EVALUATION SITES UNLESS THEY ARE UNIFIED, WHICH IS §8'S "THE RULE LIVES
ONCE" IN ITS OWN PLAN.** The driver's fold already evaluates `a.obstacle > mult * max(a.pool or 0, 0)`
(`shape.py:3470-3471`) on the ACT's declared pair; the provider would evaluate the same rule on the
DERIVED pair. **One owner:** the provider returns `REFUSED` with its derived `pool`/`ob`, the driver's
branch keeps its existing job (an act arriving with a hand-declared obstacle) and does **not**
re-evaluate what the provider already refused. The commit that lands the provider says which site owns
which input, or the arc has minted the nth obstacle gate while arguing against nth obstacle sites.

⚠ `[GAP: veto — 04 §C.5:684 spells the ladder call `degree = ladder.degree(margin, veto = provider.veto)`,
and the live `degree_from_net(net, ob, extension=None, **context)` (`dice_engine.py:227-228`) has no
`veto` parameter. `04 PART D row 23` (`:953`) grades the widening refusal "STRUCTURAL by signature",
which the live signature does not carry. `dice_seam` returns no veto and needs none — nothing it wraps
can widen an outcome — so this arc does not close the gap. It is named here so a later provider that
DOES need one does not discover it at the seam.]`

### Operands, each with its grade

- **`pool = p.capability.get(VERB_CAPABILITY[verb], fx.get("pool_default"))`.**
  `VERB_CAPABILITY` is a new roster (U1), **assumption, swept**. Warrant: `03 §A.2:28`, *"Rank supplies
  dice and gates nothing"*, and `#353 §9.2` as quoted live in the tree at `shape.py:854-855` —
  *"`capability` supplies dice and GATES NOTHING"*. `pool_default` is a **fixture with a register row
  and a three-point sweep**, because `capability` is **empty on every corpus person**
  (`requirements.yaml:72-74`; one writer, `probes.py:432`, which zeroes it — §2.3; ⚠ that row spells
  the writer `probes.py::_zero_capability` and **no such function exists** — the site is inside `p11`,
  decorated at `probes.py:422`. The row's PROSE is exact; its `::symbol` is not, and §2.3's *"states
  this exactly"* is narrowed to the prose), and `08 §3` gives
  assumption ⇒ inject-declare-sweep, **never refuse the whole corpus**. **[CLOSED — READ 2026-09-09.**
  `architecture/meta/08_DATA_AND_KEYS.md` §3 is at `:50`; its grade table gives `assumption` →
  *"**inject the default · declare the site · sweep three points.** ⚠ A verdict that flips across the
  sweep is itself a finding, and a more important one than the verdict"* (`:56`), and `absent` →
  *"**REFUSE. No default.** An instrument that fills it has invented"* (`:57`). So the licence used
  here is the `assumption` row's, exactly, and the refusal belongs to a grade this fixture does not
  carry.**]**
- **`ob`** = `act.obstacle` if declared; else the 2026-08-14 ruling — *"their corresponding **score/2
  plus whatever specific modifiers exist for them in that instance**"* (`dice_engine.py:242-245`) —
  applied to the **subject's** capability on the same key when the subject is a person; else
  `fx.get("obstacle_default")` (fixture, assumption, swept). **No "Base Ob by scale"** (Jordan
  2026-09-05). ⚠ And per §2.10, register this as an **nth site in a family the tree records as
  disagreeing**, not as adopting a single owner.
- **S27.4's refusal** (`ob > mult * pool`, `mult = w.fixtures.get("obstacle_refusal_multiple")`,
  `shape.py:3471`) is evaluated on the derived pair **inside the provider**.

### Seeding — and why per-draw `H`, not a threaded stream

`SeasonDriver.resolve` — the driver, at the RESOLVE step, holding the ACTS token — constructs

```python
rng = random.Random(int(H(w.world_seed, w.tick, a.actor, f"roll:{prize}:{a.id}"), 16))
```

and passes it to `contest(..., rng=rng)`, which passes it to the provider. This satisfies **`04 §C.12`
rejection 4** (`:857-863`), verbatim: *"When R-09's producer is built … **its generator must be
constructed by the driver from the run seed and passed down exactly as `World` is.** This is the one
rejection that is **not yet load-bearing**, because no roll exists yet."* **U1 is what makes it
load-bearing**, and the plan should say so in the commit that lands it.

⚠ **"Threaded like `World`" in that rejection means *passed by parameter rather than reachable by a
global name*, not *one continuous stream*.** The two readings diverge, and `04 PART D row 35` (`:968`)
settles it: **"a new draw moving unrelated goldens" | `H(seed, tick, subject, purpose)`; no counter, no
service | MECHANICAL (a pinned golden); CONVENTION on `purpose` uniqueness — the chain's own measured
hazard.** A single stream threaded through the season makes every roll depend on the count of prior
draws, so **adding one contested verb would move every other verb's outcome.** Per-draw `H` is the
construction row 35 names.

It is the same **construction** `combat_seam.resolve` already uses — `combat_seam.py:153`,
`seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)`,
consumed at `:160`. That function is refactored to **take** `rng` rather than build its own.

⚠ **BUT IT IS NOT THE SAME SEED STRING, AND THE FIRST DRAFT'S CLAIM THAT IT WAS IS FALSE.** The driver
line above spells `purpose` as `f"roll:{prize}:{a.id}"`, against combat's `f"contest:{prize}:{causes[0]
…}"`, and the third argument differs too (`a.actor` versus `claimants[0]`). **Two different strings ⇒
two different seeds ⇒ every existing combat result moves**, which would silently re-record the
`kill / wound` goldens under cover of a refactor. **So `purpose` is PROVIDER-SPECIFIC, and the driver
asks the provider for it:** the manifest row carries the provider's `purpose(prize, act, causes)`, and
`personal_combat`'s is `f"contest:{prize}:{causes[0] if causes else ''}"` with `subject = claimants[0]`
— **byte-identical to `:153` by construction, which is then the refactor's own test.** `dice`'s is
`f"roll:{prize}:{a.id}"`, new and colliding with nothing. Per-draw `H` needs `purpose` uniqueness
(`04 PART D row 35`, `:968`, *"CONVENTION on `purpose` uniqueness"*); it does **not** need one spelling
across providers, and forcing one costs a golden re-record for nothing.

**After U1 there are exactly two `random.Random` construction sites in the package** —
`loop/driver.py::resolve` and **`seam/combat_seam.py`** (the path after step 8) — and the falsifier
counts call sites, not text (§2.5).

**Determinism controls that must hold.** `test_w9_check1_the_run_is_reproducible` (`:2652`);
`test_r4_event_ids_are_unique_per_draw_and_reproducible` (`:1143`);
`test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` (`:1266`, one of **three**
`test_w15_*` — §2.15); and the campaign goldens under `engine/tests` **untouched** — the season
package imports `engine.autoload.dice_engine` (lazily, at `shape.py:3986`) and nothing imports the
season package into `mc_v18`.

⚠ **THAT LAST SENTENCE IS VERIFIED BY INSPECTION, NOT BY THE TEST THIS DOCUMENT FIRST NAMED.** There
is no `test_engine_does_not_import_systems.py::test_importing_engine_pulls_in_no_subsystem` — the name
lives only in that file's docstring (`:24`), is reproduced wrongly by `CLAUDE.md` §3, and
`grep -c "def test_importing_engine_pulls_in_no_subsystem"` returns **0**. The real function is
`test_importing_every_engine_module_pulls_in_no_subsystem` (`:358`), and what it asserts is that no
module under `engine/` loads a file under `systems/` (`:376-392`) — **a different claim**, silent on
`engine.season` versus `mc_v18`. The separation is real and measured by grep (U0's Control has the
command); **it is guarded by nothing, and under `CLAUDE.md` §0.1 pt 5 it should not be — the arc is
not load-bearing on it.** Because the goldens are therefore identical by construction, they are a
smoke check here and not a control.

### Why R-09 reads `partial` after U1, not `met`

**The roll varies by SEED and by FIXTURE, not by PERSON**, because `capability` has no writer (§2.3).
`met` follows when capability is written — character development, scale row 1, **out of this arc**
(§10) — or when W27's cast (U8) seeds it per case. **Record that sentence in R-09's `measured:`.**

### Which verbs gain `contests:` first, and the test that decides it

**`tell` and `speak`.** Both execute in the corpus today (`requirements.yaml:203`), and both are
social-stratum person-to-person acts that
`test_we_only_a_verb_that_declares_contests_can_be_graded_today`'s own docstring names as the verbs a
degree would matter for: *"`speak`, `tell`, `utter`, `petition` and `the six investigation acts` — the
person-to-person verbs a degree would matter most for — are all in that 31."* Prize: **`a standing`**,
already rostered (`rosters.yaml:542`).

**`tell`'s degree-keyed `emits`:** `Overwhelming`/`Success`/`Partial` → `news.told`; `Failure` →
`news.untold`. **Both kinds are already declared on the row** — `verb_table.yaml:484-485`,
`emits: ["news.told"]` and `emits_on_refusal: ["news.untold"]` — **so this introduces no new Event
kind**, which is the load-bearing property and it is checkable by reading the row.

⚠ **What the first draft wrote instead was that *"loader invariant 7 admits them"*, and that is a
PROSE INVARIANT CITED AS MECHANISM — the §0.05 defect this document's own `## Status:` line invokes.**
Invariant 7 (`04:466`, *"the Event-kind roster is **derived** from every emission column, and the log
accepts no other kind"*) is **SPECIFIED AND UNBUILT**: `04 §F.20b:1084` records that the fold mints
`act.ineligible`, `act.refused` and `contest.resolved` as **body literals**, that *"invariant 7 refuses
all three at `append`"*, and therefore that *"the loop as built cannot run under the loader as
specified … **or the derived roster is not derived**"*. No derived Event-kind roster and no kind check
at `append` exist in `engine/season/data/`. **So nothing admits these kinds; nothing has to, because
they are already on the row.** Do not cite invariant 7 as the reason. `writes:` stays `[]` at every
band, and a
`Failure: []` is **lawful** — `04 §C.4:630-634`: *"**`Failure: []` is the only place in this architecture
where writing nothing is correct**, and it is correct because the act still **emits** … **That is the
difference between a refusal (the precondition failed, no contest occurred) and a loss (the contest
occurred and went against you)**."*

**`speak`'s `Failure`** needs a refusal kind its row must declare (today `emits_on_refusal: []`): add
`speech.unheard` to the matrix's declared kinds, or reuse `news.untold`. **The loader's derived roster
decides, not the body.**

**Decided at §0 test 5** — the smallest corpus-executing set that makes R-09 measurable. The stated
alternative, `petition`/`repudiate`, moves the same number and additionally touches `Petition.exists`
writes, which is more.

---

## §8 · THE PROSE→CODE TRANSLATION PROCESS — a repeatable procedure

`CLAUDE.md` §0.05 governs. **The process runs PER STATEMENT, not per document, and terminates in a form
a LOADER or a FALSIFIER evaluates** — `04 G.3.1:1355`: *"A design statement survives only in a form
something other than a reader can evaluate."*

### STEP 1 — LOCATE AND CLASSIFY, by *"would changing this change the GAME, or how the CODE works?"*

| the prose says | it becomes | where | the reader that makes it DECLARED (ID-13) |
|---|---|---|---|
| a closed set (kinds, sources, forms) | a **ROSTER** | `rosters.yaml` `rosters:` with `source:`, `open:`, `note:` | bound at import by `data/rosters.py`; a body literal of ≥3 identifiers fails `test_jordan_no_definition_is_hardcoded_in_a_body` (`test_season_shape.py:1800`) |
| a mapping keyed on a roster | a **TABLE** | `rosters.yaml` `tables:` with `row: H-NN`, `default_cell`, `sweep`, `keys` | `table()` / `roster_map()`; the loader cross-checks keys against the roster **both ways** (`data/fixtures.py:94::_load_matter_tables` is the template) |
| a free scalar | a **FIXTURE** | `data/fixtures.py` `DEFAULT_FIXTURES` + a `hole_register.yaml` row (`grade`, `site`, **3 distinct sweep points**) | `Fixtures.get(name)` raises on an unregistered name; `test_w9_check3_every_fixture_read_resolves_to_a_register_site` (`:2805`) refuses a read with no `site:` |
| an act | a **VERB ROW** | `verb_table.yaml`: five columns + `requires_typed` (one of the **seven forms**, `04 §F.24a:1090`) + degree-keyed `writes`/`emits` **iff `contests:`** | the fold (`loop/driver::_fold`); `resolvable_verbs()`; **twelve loader invariants at import** (`04 §B.13:441-477`) |
| a precondition no form fits | a **PREDICATE** | `loop/predicates.py`, `@requires_predicate` | **but FIRST ask whether the grammar needs an eighth form.** `§F.24a` closes *"30 of 32 cells"* with seven, and *"two cells are not predicates at all"* |
| what a verb changes | an **EFFECT** | `loop/effects.py`, `@effect_for`, writing **only** through `w.write` | `writes:` ⊆ matrix rows (invariant 1); an effect touching nothing **emits the refusal** (`shape.py:3352-3357`) |
| a consequence per outcome | a **DEGREE BRANCH** | the sixth/seventh columns | `writes_at(degree)` / `emits_at` (`shape.py:3302`) |
| a mechanism | **CODE + A FALSIFIER** | the owning Layer-1 module | the test that is **RED BEFORE and GREEN AFTER** |

### STEP 2 — PROVENANCE, IN THE ROW AND ON THE LINE

Every roster / table / verb row carries `source:` naming a `PP-NNN` / `ED-NNN` / `file §`. A numeric
literal in `.py` carries `# [canonical: path §section]` on the same or previous line **or fails
`tools/ci_sim_fabrication_check.py`**. A number that is **not** a game value carries `[JUSTIFIED: …]`
(the live examples: `test_season_shape.py:555` — *"a VACUITY FLOOR over this package's own module
count, not a game value"* — and `:558`, and `state/carriers.py:327`) or `[GROUNDED: …]` for a measured
sweep point. An **`assumption`** row carries a `site:` and three distinct `sweep:` points —
**`register.py::rule_R2`**, not G6 (§2.7). An **`absent`** row carries a non-empty `cite:` recording
that §0's five tests were run — **that is G6** (`register.py:34, :240`). And `rule_G12` forbids a
`cite:` arguing for a grade the row does not carry.

### STEP 3 — THE GATES THAT PROVE FAITHFULNESS, IN THIS ORDER

```
python -c "import engine.season.shape"              # the loader's cross-checks fire at import
                                                    # (NOT all twelve of 04 §B.13 -- invariant 7 is
                                                    #  unbuilt, 04 §F.20b:1084)
python -m engine.season.harness.register --check    # R2: site + 3 distinct sweep points; G6; G12
python -m pytest engine/season/tests -q             # the no-hardcoding guard, check 3, the H-66 sweep
python tools/ci_sim_fabrication_check.py
python tools/export_sim_params.py --check
# AND THE EXECUTION:
python -m engine.season.harness.corpus_run          # the verb EXECUTES, or the fixture IS READ, in >=1 world
```

⚠ **On the fifth line, stated plainly (§2.8).** `export_sim_params.py --check` is **run by no CI job,
no `.githooks/` hook and no `tools/valoria_local.py` step**, and the tool has no row of its own in
`references/ci_checks_registry.yaml`. Seven of the eight `tools/export_*.py` are invoked in
`.github/workflows/valoria-ci.yml` (`:126, :127, :134, :137, :141, :146, :150`); this one is not.
**The round-trip is nonetheless enforced**, by `tests/valoria/test_export_sim_params.py:21`, which calls
`esp.check()` directly and is inside the blocking `pytest tests/valoria` job (`valoria-ci.yml:365`);
the same file's `test_every_value_is_a_real_literal_from_source` re-extracts independently and compares
each value to the AST literal at its **definition site**. So: **running the command by hand tells you
sooner, not more.** Do not describe it as an unguarded surface, and do not add a CI step for it in this
arc — that would be a second copy of a rule that already lives once (`CLAUDE.md` §8).

**A TRANSLATION THAT LOADS BUT NEVER EXECUTES IS A CARRIER BEFORE ITS READER.**

### STEP 4 — THE REVERSE TEST, APPLIED BOTH WAYS

`04 G.3.5:1414`, verbatim: *"**The single test, applied in both directions.** If this document were
deleted, would the game behave differently? **No** → it is reference. **Yes** → the mechanism is in the
wrong place; move it into data or code and leave a pointer."*

- **DELETE THE PROSE** — the game must behave identically. It is now reference.
- **DELETE THE ROW** — the loader must **REFUSE, naming the row**. It is mechanism.
- **If deleting the row changes nothing, the row has no reader** and is not yet declared.

**How a runtime registry differs from reference prose, checkably.** A registry is opened by **exactly
one loader** — `grep -rln "verb_table.yaml" engine/season` → `data/files.py` plus one loader — and bound
to names code reads. A design document is opened by nothing: the one read of #353, at
`SOURCE_353_TEXT` (`shape.py:2276`), is for gap **attribution**, not resolution. `CLAUDE.md` §3's
`engine/season/` row already draws this line for `hole_register.yaml` — grader mechanism, game
reference.

**The live backlog, sited.** `sim_params.json` is an AST extract of module-scope literals under
`systems/*/sim` and `engine/` (`export_sim_params.py` `SCAN_DIRS`). Its **252 uncited** constants
(§2.9) belong to the retained three subsystems and the retire set, and are reached by this arc **only
where a seam reads one** — **U1 reads none; U9 reads none.** The loop's own constants **never enter
it**: they take the fixture / table route above, which is **stricter** — a register row with three
distinct sweep points, not a citation comment. The *"321 → 415 still inside `systems/`"* sentence in
`CLAUDE.md` §0.05 is about a migration **this arc does not run** (§10).

### WORKED INSTANCE — U7 group 3, the Dispensation four

`issue`'s cell *"scope enumerates executors, not places"* and `open_case`'s *"the act DECLARES the
stages and their terms"* are, per `04 §F.24a:1105-1110`, *"**constraints on the well-formedness of the
Act**, not questions asked of the world. **They belong in the `Act` schema and are refused at
construction**, not evaluated at RESOLVE."* So they are **not** `requires` cells and no predicate is
written for them.

`comply` / `evade / defy` / `refract` need an operand name — `dispensation` — added to the **closed**
`requires_operands` roster (`rosters.yaml:865`) with a `source:`, **and** `F.15`'s nine terms as a
`Record` kind schema **in data** before any predicate can read them. `F.15` (`04:1077`) grades that
absence: *"**the nine dispensation terms** *(§B.5)* — *\"nine typed terms\"* and nothing lists them | a
schema for one Record kind, **unspecified** | **not an assumption so much as an absence: the entire
downward mechanism has no executable content**, and `issue` produces a document nobody can comply
with"*.

**That is the shape of every remaining prose-only mechanism: the roster row precedes the predicate, and
the predicate precedes the effect.**

---

## §9 · THE GUARD-BLINDING HAZARD, HANDLED STRUCTURALLY

**One cause: a gate whose corpus is a hardcoded path is invariant under a move out of that path.** PR
#383's step-5 adversarial pass overturned the claim that no gate narrowed — *"**false**, and my
measurement was invariant by construction. Three gates read `files.SHAPE_PY` alone and did narrow."*
**Six rules, binding on every gate this arc writes.**

1. **THE CORPUS IS DERIVED, NEVER NAMED.** Model gates read `_model_modules()`
   (`test_season_shape.py:491-511`); instrument gates read `files.package_modules()`
   (`data/files.py:148-159`), which is `PACKAGE_DIR.rglob("*.py")` and whose docstring says why:
   *"THE DISCOVERY IS THE POINT … Recursive, because the harness modules now live one directory down
   and a flat `glob` would silently drop eight of them."* **A new directory — `seam/`, `decision/`,
   `manifest/` — is scanned the day it exists, with no edit anywhere.** The margin-producer scan already reads
   `files.package_modules()`, which is why U1's falsifier needs no corpus change.
2. **EVERY DERIVED-CORPUS GATE CARRIES A VACUITY FLOOR** in the `test_h115` form
   (`test_h115_the_fourteen_load_time_raises_are_unchanged`, `test_season_shape.py:513`, floor at
   `:556` — **not** the `:452` `test_h115` sibling, which carries no floor): `assert len(mods) >= 8, f"model set collapsed to
   {len(mods)} — this guard would pass vacuously"`; and where the gate polices a family, assert the
   family is present.
3. **POSITIVE `in` ASSERTIONS NAME A SYMBOL, NOT A PATH** — `inspect.getsource(<module>.<symbol>)`, so
   a move makes the **import fail loudly** rather than the assertion pass vacuously.
   **`files.SHAPE_PY` (`data/files.py:133`) MAY NOT APPEAR IN ANY NEW TEST**; at step 10 the constant
   is deleted, so any survivor is a `NameError`, **which is the good case**.
4. **A MODULE-LEVEL NAME REBOUND BY A TEST OR PROBE IS READ BY ITS CONSUMER THROUGH THE OWNER MODULE'S
   GLOBALS.** The four live rebinds — `S.ALIGNMENT` (`:2302`), `S._LADDER` (`:7837`),
   `S.belief_contradicts` (`:7012`), `probes.py:2450`'s `_s.contest = spy` — are re-pointed at steps
   6/7/8, and **any new rebindable** (the `PROVIDERS` table, the `draw` factory) is exposed from its
   owner and rebound there. PR #383's step-6 commit demonstrated the failure rather than predicting it:
   with a copied binding, *"the game behaves identically and only the instrument goes blind."*
5. **PLANT BEFORE TRUSTING.** Each new gate lands with **the counterfactual in its docstring** — the
   plant that turns it red — on the precedent at `test_season_shape.py:1828-1831`.
6. **NO NEW CI STEP.** The job is `python -m pytest engine/season/tests -q -n auto`
   (`.github/workflows/valoria-ci.yml:370`, recursive) plus
   `python -m engine.season.harness.register --requirements` (`:376`). **No gate this arc writes needs
   one**, and adding one would be the apparatus reflex `CLAUDE.md` §0.1 pt 5 disarms.

---

## §10 · NON-GOALS AND DE-SCOPING

| item | scale / row | why not this arc | what would change that |
|---|---|---|---|
| grid-based map combat with units | scale 5 / R-05 | **unbuilt design.** `requirements.yaml:104` — *"**GRID-BASED MAP COMBAT WITH UNITS DOES NOT EXIST ANYWHERE IN THE TREE**"*; a seam cannot be wired to a subsystem that does not exist | a design pass, then one engine behind an unchanged seam (`T-l`) |
| settlement management / city building | scale 6 / R-04 | `domain_actions` and `settlement_economy` are `doc: null` in `module_contracts.yaml`; the inline economy in `matter()` is *"a mode that never got its seam"* (`rosters.yaml:490-495`) — **the engine behind the seam must be BUILT** | the MATTER seam item, after this arc |
| mass-battle seam | scale 4 / R-05 | `a field` refuses by name; sides need `faction_q.resolve` (`04 §C.5.1:699`) which is R-04 / U9 | after U9 |
| the six investigation acts | scale 7 / U7 group 4 | their seam is **UNRULED** (`rosters.yaml:479`); `rosters.yaml:502-505` — *"**INVESTIGATION MUST NOT BE MADE A CONTEST TO BECOME GRADEABLE** … Giving them a prize so the existing machinery can grade them is scripting drift"* | the fieldwork translation under §8 |
| character creation / development | scale 1 / R-06, R-09's person term | **no writer for `capability`** (§2.3) and no `F.31` world-gen roster; individuation is demand-driven at CENSUS and **nothing demands** (`04 §C.7:743`) | a practice verb and the roster |
| design-ruling **R8**'s `seen` struct | R-07 deepening | its **own** sequencing ruling — `references/design_rulings_2026-09-06.md:287-288`: *"the first thing to build is not the carrier but **the consumer** — a person who forms a candidate because of what they came to believe"*; and R8.3 (`:266`) gates on `Claim.value` having exactly two readers | after U6 shows the claim→decision channel open |
| `Receipt` before/after, `NoOpReceipt` (`04 PART D row 5`, `:934`); the act store as state; the snapshot | not one of the nine | correctness items the 2026-09-06 plan puts on its critical path. **None of the nine's measures moves on them** | its own unit, sequenced beside U7 |
| typing the seam's return as a `Margin` (`04 §C.5:683`, the crossings type assertion at `04:692`) | not one of the nine | ⚠ **A DECLARED DEVIATION, NOT AN OVERSIGHT** (§7). Both providers return a **dict** today, which is what `combat_seam` returns and what `degree_of` grades (`{"net","ob"}`). Typing one and not the other gives the seam two return shapes — worse than either. The **contract** (no winner, no band, a margin the one ladder reads) is honoured; the **type** is not | one `seam/` unit typing both providers together, sequenced beside U7 |
| step B retirement; the Godot port | — | gated on R-04 (`CLAUDE.md` §3). `04 §C.12` rejection 4 is the **only** port constraint this arc must honour, and U1 does — it is what makes it load-bearing | after U9 |
| the `systems/` constant migration (252 uncited) | §0.05 backlog | **outside the loop's data path**; touched only where a seam reads a constant, and U1 and U9 read none | per-seam, as seams land |

⚠ **Two numbering schemes collide and a session will trip on it.** `references/design_rulings_2026-09-06.md`
numbers **R1..R8**; `engine/season/requirements.yaml` numbers **R-01..R-09**. **Design-ruling R8
(partial observation, `:198-320`) is not `R-08` (non-rational choice).** Commits `c3dca09` and `01141b4`
are ruling-numbered. Design-ruling R8's work has not started, so there is no live collision today.

---

## §11 · WHAT NEEDS JORDAN — AFTER THE FIVE TESTS

**ONE escalation. NINE candidates close.** ⚠ **The first draft of this section said *"Every candidate
closes. ZERO escalations"*, and it reached that count by CLOSING THE ONE LIVE QUESTION ON A QUOTE THAT
DOES NOT EXIST.** The row read *"ED-SC-0033 … — \"wiring it now wires a retired tree\""*. That string
appears **nowhere in `registers/editorial_ledger_sc.jsonl`**, and a repo-wide grep found it in exactly
one file: this one. It was a paraphrase of the ruling's retirement clause, promoted to a quotation, and
then used to close the escalation it was invented to answer — **the §2.10 defect class this document
charges the planner with, committed by the document.** It is retracted, the row is below, and the count
is one.

---

### §11.0 · **THE ESCALATION — `needs_jordan: true`. May a generic dice roll stand in for a social contest, now?**

**Blocks:** U1 half (b), and therefore U5 entirely (U5's precondition is a non-empty `DEGREES RESOLVED`
line). **Does not block:** U1 half (a), U0, U2, U3, U4, U7, U8.

**WHAT THE RULING ACTUALLY SAYS.** ED-SC-0033 (2026-09-06, `registers/editorial_ledger_sc.jsonl:33`),
verbatim on the three clauses that bear here:

> *"WHAT THE RULING SETTLES: (1) the seam dispatches by manifest ROW rather than the hardcoded
> personal_combat literal at shape.py:6740; (2) the two contest prizes at rosters.yaml:441-446 that map
> to social_contest **REPOINT to this provider** — the README had recorded that this directory left them
> untouched because repointing supersedes other work by editing one line, which CLAUDE.md section 2 says
> must be loud rather than quiet, and the ruling is that loudness; (3) **THE OBSTACLE HAS A SINGLE
> OWNER**, which dissolves the largest open question in 18_FINDINGS.md …"*

*"this provider"* is **the proceedings subsystem's**, not a dice roll. (The row's own `shape.py:6740`
and `rosters.yaml:441-446` are stale — §2.15 — but its clauses are not.)

**WHY THIS SURVIVES ALL FIVE OF `CLAUDE.md` §0's TESTS.**
**(1) Superseded?** No — ED-SC-0033 is 2026-09-06 and is the most recent ruling on the subject.
**(2) Irrelevant?** No — `a standing` and `a proposition` are exactly the prizes `tell` and `speak`
take, so U1 cannot avoid them. **(3) Answered by a design document?** No, and the two candidate
documents point **opposite ways**: `rosters.yaml:514` *"⚠ A CONTEST IS A DISPATCH, NOT A GENERIC ROLL"*
with Jordan at `:529-530` *"we don't NEED to worry about them at this point in time"*, against
`04 §C.5`/`08_SEAM.md` PART B, which want a provider resolved by row and are indifferent to which
provider. **(4) Answered by precedent?** No — the only precedent is `combat_seam`, which wraps a **real
subsystem that exists**; there is no precedent for a stand-in provider. **(5) Obvious for the
architecture?** **No, and this is the decisive one:** the interim provider derives its own `ob`
in-seam (§7, Operands), and ED-SC-0033 clause (3) rules that **the obstacle has a single owner**. So
the architecturally-obvious move and the ruling disagree, which is precisely the case §0 reserves for
Jordan. **Two defensible options, materially different games.**

| | **A — interim `dice` provider now** | **B — wait for proceedings** |
|---|---|---|
| **what happens** | `a standing` / `a proposition` route to `dice_seam`; `tell`/`speak` declare `contests:`; the third gate opens for them | the two prizes keep refusing by name; `tell`/`speak` stay uncontested |
| **cost** | a **bare pool-vs-fixture roll stands in for a social contest** — the "generic roll" `rosters.yaml:514` refuses in terms; an **nth obstacle site** for social contests, against clause (3)'s single owner; Jordan's *"we don't NEED to worry about them"* is set aside; the corpus goldens re-record against a stand-in model and re-record **again** when proceedings lands | **R-09 stays `not_met`, R-07/U5 stay blocked, R-05b does not move** — no corpus-executing verb can form a contest, because `kill / wound` is untyped and cannot (§4). U1 delivers only half (a): a registered provider nothing calls |
| **buys** | R-09, R-07 and R-05b all become measurable this arc; the repoint is later **one row**, not a code change (`02 §D.4`) | the first social contest the game ever runs is the one its owner designed; no golden is recorded twice; clause (3) holds |
| **reversibility** | high **in code** (a row change) and low **in data** (`runs/` is re-recorded under a model that is then replaced) | total |

**What the plan needs, minimally:** a yes or no on A. If **A**, the prize rows in U1 lose their `HELD`
markers and U1 half (b) proceeds as written, with the `interim: true` flag and the sweep on
`obstacle_default` carrying the assumption. If **B**, U1 ships half (a) only, `tell`/`speak` do not gain
`contests:`, U5 is deferred behind the proceedings subsystem, and **R-09's honest `measured:` line
becomes *"a producer exists and no corpus verb calls it"*.**

⚠ **A third option was considered and is NOT offered, because it is worse than either:** giving the
dice provider a *new* prize outside the closed roster, so nothing collides with the social ruling. That
invents a prize to dodge a ruling, and loader invariant 9 (`04:467`) would have to be widened to admit
it. Named here so it is not re-derived as a compromise.

---

### §11.1 · The nine that close

Recorded so a later session does not re-open them — the ED-IN-0185 failure `CLAUDE.md` §0 names.

| candidate | closes at | by |
|---|---|---|
| where the pool comes from (`verb_capability`, `pool_default`) | test 5 | `08 §3`: assumption ⇒ inject-declare-sweep; post-adoption §6 trap 14 |
| how `ob` is derived | tests 1 + 3 | Jordan 2026-08-14, *"their corresponding score/2 plus whatever specific modifiers exist for them in that instance"* (`dice_engine.py:242-245`); *"Base Ob by scale"* struck by Jordan 2026-09-05. ⚠ Registered as an nth site, not a single owner (§2.10) |
| which verbs gain `contests:` first | test 5 | the smallest corpus-executing set that makes R-09 measurable; the alternative is stated in §7 |
| scene tick shape (rounds; player granularity) | tests 1 + 4 | R-03's statement is **newer** than #353 S26.2; `rosters.yaml:455-460` records Jordan's granularity constraint verbatim |
| whether the tick may skip a person with no news | test 5 | a CONSTRUCTION over AX-2 (U2 decision 4), with its own falsifier (U2 falsifier b). ⚠ **Narrowed by the adversarial pass:** the first draft called it *a theorem* on the condition *"a claim landed, or `sense` changed"*, and that condition is **incomplete** — `questions_for` and `person_side_eligible` also read tenures, dates, docket, crossings and propositions. The corrected three-clause condition is a design call with an obvious engineering answer (derive the dirty set from the write matrix), so it still closes at test 5; it does not close as a proof |
| softmax sampling for R-08 | tests 1 + 5 | R-08 **is** the ruling; `tau` is assumption, swept. ⚠ **Narrowed:** `tau = 0` is a byte-identity arm that validates **plumbing, not the sampler** — the zero-temperature limit over the tied majority of candidates is uniform, not the alphabetical `sorted()` at `shape.py:810`, so the arm needs a discontinuous special case that exercises the old path (U4). Both prior plans name the arm and neither notices this; it does not reopen the ruling |
| the 13 convictions replacing the 4-axis stand-in | tests 3 + 4 | `references/descriptor_registry.yaml:235-251` already declares them and exports them behind a **blocking** `--check` (`valoria-ci.yml:137`). ⚠ **Narrowed by §2.6:** what closes is *may we READ the tree's own single-owner roster* — yes, and `H-46`'s own cite calls that a data edit. **`H-46` stays OPEN and its `absent` grade does not move**, on Jordan's *"may be modified in future"*. Populating is not closing |
| the 10 world-scale cases | test 5 | `PLAN.md:1613-1617` decides ≥2 realm rungs and records it on `H-95`. *"Jordan may overturn it; that is a ruling, not an open question this plan waits on."* |
| investigation: a contest or its own kind | test 5, **and de-scoped** | `04 §C.4` gives a degree only through `contests:`; a single-claimant provider is lawful (only combat refuses <2 — `combat_seam.py:142-145`); `rosters.yaml:502-505`'s *"not a contest"* is a note on the mechanism's shape, and `03 §E.1:220`'s *"an examination"* is not clearly the detective sense. **Nothing in this arc needs the answer**; the row stays UNRULED with this disposition recorded so it is not escalated by default |

---

## §12 · CRITICAL FILES

- **`engine/season/shape.py`** — the driver (`SeasonDriver`, `:2724`), the chooser (`:773-818`), the
  seam (`:3875-4153`) until steps 7–9 move them. **Every unit's entry state is a line here**, and every
  line number here is against `main` `f41f20a1` (4,153 lines), **not** #383 (2,803).
- **`engine/season/combat_seam.py`** (189) — the precedent `dice_seam.py` copies: derive one field,
  return the gap, per-draw `H` seeding at `:130, :153, :160`. ⚠ Its `purpose` string
  (`f"contest:{prize}:{causes[0] …}"`) is **not** the dice provider's and must not be unified with it
  (§7, Seeding). At `seam/combat_seam.py` after step 8.
- **`engine/season/manifest/`** — **NEW in U1, and one of Layer 1's nine** (`04 §A.2:136`,
  `04:125`, `04 §C.5:682`, `04:1031`). Owns `PROVIDERS` and `resolve(role, module)`; the thing
  `seam/contest.py` calls and the thing ED-SC-0033 clause (1) names.
- **`workplans/2026-09-06-shape-decomposition-plan.md`** — **the single owner of decomposition steps
  7-10.** U0 carries only the deltas; three of them were written back into this file on 2026-09-09
  (its `:85`, `:88`, `:155` and its §4 step-7 / step-8 rows).
- **`engine/season/verb_table.yaml`** (555, 32 rows) — `contests:` and the degree-keyed
  `writes` / `emits` columns (U1, U5, U7); the seven-form `requires_typed` cells.
- **`engine/season/rosters.yaml`** (1,036) — `contest_subsystems` (`:510`, prizes at `:539-543`),
  `conviction_axes` (`:145`) and `tables.alignment` (`:975`) for U3, the seam table at `:474-482`, the
  granularity ruling at `:455-460`, and the new `verb_capability` / `stance_delta` / `scale_of_rung`
  rows.
- **`engine/season/write_matrix.yaml`** (372) — the `Person.stance` row at `:203-209`, already declared,
  already emitting `stance.moved`, and listed at `:50` among the RES-stepped rows with no producer.
- **`engine/season/tests/test_season_shape.py`** (8,078; 186 test functions, **186 passed** —
  observed, §1) — `_model_modules()` (`:491`), the no-producer scan (`:7887-7897`) with its **three**
  breaks at `:7866`, `:7872` and `:7877-7883`, the AST guard (`:2224`, whose corpus at `:2231` is
  `files.SHAPE_PY` **alone** and is re-pointed at step 7), its `sense` name-exemption (`:2267`), and
  the rebind sites (`:2302`, `:7012`, `:7837`) every carve and every R-unit must keep honest.
- **`engine/autoload/dice_engine.py`** — `_die_result` (`:153-161`), `degree_from_net` (`:227`),
  `roll_pool` (`:196-206`). The single owner, imported and called, never mirrored.
- **`architecture/meta/04_CODE_ARCHITECTURE.md`** — §A.2 `:127`, §C.1 `:502`, §C.2 `:520`, §C.4 `:573`,
  §C.5 `:677`, §C.5.1 `:699`, §C.7 `:743`, §C.12 `:810` (rejection 4 at `:854`), PART D `:923` (header
  `:928`), §E.1 `:1038`, F.15 `:1077`, F.20a `:1083`, §F.24a `:1090`, §B.13 `:441`, G.2.9 `:1317`,
  G.3.1 `:1355`, G.3.5 `:1414`.

---

## §13 · SIZE — measured, and over the convention's threshold

**Measured, not estimated — RE-MEASURED after the adversarial pass (§14):** **2,057 lines**,
**37,869 tokens** at `tools/ci_common.py::tokens` — the repo's single owner of that estimate,
characters ÷ 4. ⚠ **Say which character count**: Python `len()` gives **151,476** and `wc -c` gives
**153,303 bytes**, and the gap is this file's own `§`, `⚠`, `→` and `≥`. `tokens()` divides the first.
Both are true of their own basis, which is the failure mode `CLAUDE.md` §0.1 names and which PR #383
paid for once already (*"One instrument, named, for numbers that get compared."*).

*(The pre-pass figures, kept so the delta is checkable: 1,520 lines, 24,868 tokens, `len()` 99,474,
`wc -c` 100,697. The pass added **537 lines net** — corrections, the §11.0 escalation and §14 — while
U0 itself SHRANK from **125 lines to 60** by citing its owner instead of restating it.)*

That is **over** `references/atomization_rules.yaml`'s `sequential_chunk_tokens: 15000`, and the first
drafting of this section claimed it was under. It was not; the claim is retracted here rather than
left standing, which is the only move available to a document whose whole subject is citation fidelity.

**What that means in practice, stated so the next session does not re-derive it.** The threshold is a
`WARNING`-level convention (`CLAUDE.md` §4), not a blocking gate: the sibling
`workplans/2026-09-06-season-loop-execution-plan.md` is **23,206 tokens** and sits on `main` with CI
green. So this file is *at the same size as its closest peer and subject to the same convention*, and
shipping it as one part is a deliberate choice, not an oversight. ⚠ **After the adversarial pass this
file is over 60% longer than that peer** (37.7k against 23.2k tokens), so the choice is weaker than it
was and the split below is closer than it was. Say so rather than re-asserting the earlier comparison.

**Where it splits, when someone does split it.** At the §6/§7 boundary: §1–§6 are verification and
sequence, §7–§13 are the deep placement argument and the repeatable procedure. `_part2` would open at
§7 and the break is a reading-order break, not a filing one. Do not split at §2 — the corrections are
what license every citation reproduced downstream of them, and separating them from the units would
recreate the index+infill shape `CLAUDE.md` §4 retired. **§11.0 goes with `_part1`** — an escalation a
reader must see cannot live in a second file — and **§14 goes with whichever part it audits, which is
both, so it stays with `_part1` and `_part2` carries a pointer.**

---

## §14 · ADVERSARIAL PASS — what was attacked, what held, what changed

`CLAUDE.md` §0: *the adversarial pass is a STAGE, not a DELIVERABLE. Its output is edits to the thing
under review.* **This section is the changelog for those edits and nothing else.** It creates no
directory, files no findings document, and appends **one** ledger row — §11.0's, which is the only
finding here that needs a ruling.

**Method.** A structurally-independent read-only critic (`Read`/`Grep`/`Glob` only, no `Write`, no
`Edit`, no `Bash` — the property lives in `.claude/agents/valoria-critic.md`, not in a prompt
sentence) was dispatched with the document and never saw the writer's reasoning. It opened ~120
citations. The orchestrator then **independently re-verified** the five HIGH findings against the
working tree before any edit was made, and this reconcile stage **re-opened every remaining finding
itself** — the critic was treated as authoritative only on those five.

### What changed

| # | finding | what was actually wrong | what the edit did |
|---|---|---|---|
| **F1** | `resolvable_verbs()`'s third gate | `shape.py:723-724` drops any verb declaring `contests:` from the candidate set, and ~30 call sites narrow the chooser to it. **U1's expected observable could not occur**; R-05's executing count would have gone 6 → 4 | U1 now names the gate, lists its call sites, specifies the amendment (`PROVIDERS`-derived, still refusing untyped `kill / wound`) and carries a falsifier for the amendment itself |
| **F2** | a named falsifier that does not exist | `test_importing_engine_pulls_in_no_subsystem` has **no `def`** (`grep -c` → 0); the name lives in a docstring at `:24` and in `CLAUDE.md` §3. The real test (`:358`) asserts a **different** claim | corrected at both sites (U0, §7); the season/campaign separation is now **verified by inspection** with the reproducing grep, and stated as guarded by nothing on purpose |
| **F3** | **an escalation closed on a fabricated quote** | *"wiring it now wires a retired tree"* appears **nowhere** in the ledger — a repo-wide grep found it in this file alone. ED-SC-0033 says the opposite: the prizes *"REPOINT to this provider"* (proceedings), and *"THE OBSTACLE HAS A SINGLE OWNER"* — which the interim provider's in-seam `ob` contradicts | quote deleted; the ruling quoted verbatim; the row **moved out of the closed table into §11.0**, a `needs_jordan` escalation with both options costed; §11's count is now **one**; U1 half (b) and U5 are gated on it |
| **F4** | `sense` in the AX-2 island | `sense` takes a `World`; `04:133` gives `decision/` *"NO World in scope"*. **Both guards stay green on the violation** — the AST test exempts `sense` by name (`:2267`) and the grep falsifier is case-sensitive | `sense` moved to step 9 / `loop/`; the decorative grep demoted and replaced by the re-pointed AST test; `test_season_shape.py:2231`'s re-point moved into the **step-7 commit** |
| **F5** | `PATH_SEAM_ALLOWED` "stays" | the set is **path-keyed** and asserted by **exact equality** (`:404-424`); step 8 moves `combat_seam.py`, so the test is red until the member is renamed. `files.COMBAT_SEAM_PY` goes stale with it | both renames put **in the step-8 commit**; the "stays" claim struck |
| **L2 → HIGH** | the provider registry's module | ⚠ **elevated from LOW by ruling** — a **Layer 1 conformance violation** in a document whose preamble says `architecture/` is *"never overridden"*. `manifest/` is one of the nine (`04 §A.2:136`), Stage 2 §D.4 types it (`04:125`), `§C.5:682` spells the call by that name, build step 10 is `seam/contest · manifest/` (`04:1031`), and the `§A.2` table has **no `seam/providers` row** | `seam/providers.py` → **`engine/season/manifest/`** throughout: U1's module list, the `dice_seam` imports, §7's dispatch subsection, §12 |
| **F6** | U5's `none` control | not satisfiable as written. With `Person.stance` in the degree-keyed writes, `row.writes` is non-empty, the fold demands an effect (`shape.py:3320-3331`), and an effect that changes nothing emits **the refusal instead of the success** (`:3352-3357`) — `rosters.yaml:374-376` says exactly this of the precedent U5 copies | the arm restated: stance stays empty, no `stance.moved`, **and the hash moves**; U5 declared as having **no** byte-identity control |
| **F7** | U2 decision 4 "is a theorem" | `opening_set` → `person_side_eligible` reads `p.tenures`; `questions_for` reads tenures, dates, docket, crossings, propositions. RESOLVE moves tenures without depositing a claim, and `sense` returns two scalars | skip condition widened to three clauses, implemented as a **gate-stamped dirty set** derived from the write matrix; downgraded from theorem to construction, with falsifier (b) as its test |
| **F8** | prose invariants cited as mechanism | *"the twelve invariants fire at import"* — `data/` names one by number; *"invariant 7 admits them"* — `04 §F.20b:1084` records invariant 7 as **unimplemented** | both softened to what the code does; the load-bearing fact restated from the verb row (`verb_table.yaml:484-485`), which is checkable |
| **F9** | U6's `fan_out_mode` control | `sweep_arm` sweeps `observation_deposit_mode` only; `fan_out_mode` is R-07's fixture with its own in-test control. **U6's instrument does not produce that arm** | removed from U6's controls, cited where it lives, and the shared value `total` flagged as the source of the confusion |
| **F10** | the τ=0 byte-identity arm | 15-20 of 22 candidates **tie**; softmax's zero-temperature limit over tied scores is **uniform**, not the alphabetical `sorted()`. Byte-identity needs a discontinuous special case that then exercises the old path | the arm kept and re-scoped: it validates **plumbing, not the sampler**. Error noted as **inherited** from both prior plans |
| **F11** | U1 internally inconsistent | precondition said step 8 while the unit edits `loop/driver.py` (step 9); the Random set named the pre-step-8 path; and the driver's `roll:` purpose string **cannot** yield byte-identical combat against `combat_seam.py:153`'s `contest:` string | precondition corrected to steps 8 **and** 9; set re-pathed; `purpose` made **provider-specific**, carried on the manifest row, with combat's preserved verbatim so its goldens do not move |
| **F12** | R-09 → R-07 "HARD" | the matrix admits any RES/ACTS write; a flat `writes: [Person.stance]` on an uncontested verb would fold today. The edge is hard **under H-62's supplied shape** | softened and attributed to the design choice, with the alternative named |
| **F13** | `pytest engine/tests` as a control | identical **by construction** — `engine/tests` never imports `engine.season`. `CLAUDE.md` §7 (ED-MB-0066) names this a **fake control** | demoted to a smoke check in U0 and U1 |
| **L1, L3-L12** | eleven line-level items | each re-opened against the tree before applying | applied; see below for the one rejected and the corrections to the corrections |

### Found by this stage, not by the critic

1. **The decomposition plan was duplicated, not cited.** U0 restated ~126 lines of
   `workplans/2026-09-06-shape-decomposition-plan.md` §4 with **zero** references to it — a second
   copy of a rule that lives once (`CLAUDE.md` §8), and two documents that would drift. **U0 was
   rewritten to cite: 125 lines → 60**, carrying seven deltas and nothing the owner already says.
2. ⚠ **THE `sense`/AX-2 DEFECT ORIGINATED IN THE OWNER, AND WAS FIXED THERE.** This document had
   **inherited** it. `2026-09-06-shape-decomposition-plan.md:85` listed `sense` in the `decision.py`
   row, and `:155` ruled `decision` on the reasoning *"the guard whitelists the NAME inside the
   scanned file; it must stay where the guard scans"* — **inverted**: the whitelist is why the
   violation goes undetected. **A fix applied only to this copy would have left the executable defect
   live in the document a session actually follows.** Three surgical corrections were made at source
   (`:85`, `:88`, `:155`), plus the step-7 `:2231` re-point and the step-8 `PATH_SEAM_ALLOWED` rename
   in its §4 — each marked inline with its date and evidence, in that file's own amendment style.
   Nothing else in it was touched and its `## Status:` line is unchanged.
3. **§1's tally of seven unverifiables was short by three** — three `[not read this session]` markers
   were a different cause and fell outside its *"all the same cause"*. All three have now been read
   and closed, and one (`scale_transitions_v30.md` §2) turned out to carry a real defect in U9: its
   five scales are `Object · Personal · Relational · Territorial · Structural`, which is **not** the
   corpus's `rung_kinds` vocabulary, and **neither list contains `faction` or `world`** — the 54
   unrepresentable cases. U9 must now say which problem its mapping solves.

### Rejected

- **F4's second half, partly.** The critic wrote that the AST test *"reads no `decision/` code
  afterwards"* as though that were a consequence of the move. It is a consequence of the test's
  corpus being `files.SHAPE_PY` **regardless** of the move — the test never read `decision/` because
  `decision/` never existed. The finding is right that the test goes red at step 7 and blind after a
  lazy repair; it is wrong that the move causes the blindness. **The edit was applied on the correct
  reasoning, not the critic's.**

### What was attacked and held — left alone

All fifteen `test_*` names in `test_season_shape.py` at their exact lines; all seven §2.8 CI lines;
all eleven §2.11 stale citations; every PART D row and its line; the `04` fold, §C.5, §E.1 and
G.2.9/G.3.1/G.3.5 quotations, verbatim; `sim_params` coverage 166/418/252/11; `SWEEP_POINTS = 3`;
`rule_G12`; `DEGREE_LABEL`; both greps in §2.3 and §2.5; `degree_from_net` at `:227` and `roll_pool`
`:196-206` with `_require_tn7` first; U7's 32-row arithmetic; the dependency edges `Act.via`→R-04,
W28→R-06b, H-46→R-08; *"R-01/R-02 are measurements"*; and the finding that **no acceptance in this
plan is satisfiable by writing** (`CLAUDE.md` §0.2) and **no guard is proposed where §0.1 pt 5 forbids
one.**

⚠ **One held property is a live constraint on future edits, so it is recorded rather than assumed:**
`test_degree_ladder_single_owner.py`'s `_PRODUCES_BAND` scan (`:447`) reads raw file text
**including docstrings**, and flags a file naming ≥2 bands in a produce-shape. **`dice_seam.py`'s
module docstring must stay band-free.** It is, and U1 now says why.
