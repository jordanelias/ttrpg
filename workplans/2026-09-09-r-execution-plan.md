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
> `harness/`, `tests/`, `shape.py` (4,153 lines), `combat_seam.py`, `gaps.py`, `trace_log.py` and
> nothing else. Sentences about #383 state carry the marker **[#383]**.

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

**And 14 citations in this document's own first draft were wrong and were fixed before publication**,
found by re-reading §4 and §6 against the tree a second time: seven `04_CODE_ARCHITECTURE.md` invariant
and section line numbers (`§B.13`'s twelve had shifted, `§C.5.1` was `:711`/`:717` and is `:699`),
`§C.4`'s fold and `Failure: []` spans, `03 §E.1`, `combat_seam.py:141-144`, two `rosters.yaml` lines,
`test_season_shape.py:7869`, `corpus_run.py:487`, and a `TRACE.query` call written with the wrong
arity. **A writer stage that reports zero defects in its own output has not run one.**

**The seven unverifiable ones, all the same cause:** `pytest` is not installed in this session's
environment (`python -m pytest` → *"No module named pytest"*), so no test outcome below is asserted as
observed. Test *existence*, *name* and *body* were all read directly and are verified; only "it is green
today" is not. Affected: the 186-test season suite result, the 17-test import-probe result, the
`tests/valoria` suite result, `test_export_sim_params.py::test_sim_params_current`'s current outcome,
and the three per-step falsifier outcomes in U0.

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
ARE among them and MUST be directories (§E.1, quoted in §5); `epistemic` is a step-6 convenience with no
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
  `systems/characters/conviction_taxonomy_v30.md §2` — **Faith, Authority, Order, Scholastic, Utility,
  Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor.** These are **CONVICTIONS.**
- The same file, `:257`, declares separately: `{key: "axis.*", kind: ethical_axis, name: "4 ethical
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
**R2** (`register.py:28`, `rule_R2` at `:196`): *"an `assumption` row carries a `site:` and at least
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
`[UNVERIFIED: whether that test is green today — pytest is not installed here.]`

### §2.9 · **`sim_params.json`'s live coverage, and `CLAUDE.md` §0.05's number**

Read from the file, not from a sentence:
`python3 -c "import json;print(json.load(open('engine/engine_params/sim_params.json'))['citation_coverage'])"`
→ `{'cited': 166, 'total': 418, 'uncited': 252, 'of_which_assumption_grade': 11}`. The planner's
166/418/252/11 is **exact**. `CLAUDE.md` §0.05's `415` total / `248` uncited is stale by 3 and 4.
**Cite the file.**

### §2.10 · **`dice_engine.py` line spans, and a quote that was a paraphrase**

- The canonical die rule (`_die_result`, *"1 = -1 success, 2-6 = 0, 7-9 = +1 success, 10 = +2
  successes. No chain."*, cited to `params/core.md §Die Rule, PP-246`) is **`:151-158`**.
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
| *"the no-producer scan (`:7891-7900`)"* | the scan block is **`test_season_shape.py:7887-7899`**, inside `test_we_only_a_verb_that_declares_contests_can_be_graded_today` (`:7849`); `_code_only_lines` is `:7900` |
| *"`test_w15`"* | there are **two**. The one meant is `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` (`:1266`); `test_w15_the_run_cases_entrypoint_writes_nothing` is `:1252` |
| *"`test_w5_the_alignment_table_is_swept_at_three_points`"* | full name is `…_at_three_points_and_every_flip_is_printed` (`:2291`); a `-k` on the short form still selects it |
| *"`rosters.yaml:442-446`" for Jordan's granularity constraint* | that block is *"IT ENABLES EVENTS WITHOUT A SCENE"*. The granularity ruling is **`rosters.yaml:455-460`**, ending *"Do not implement the tick as \"every person gets a scene per round\"."* |
| *"`rosters.yaml:485-490`" for investigation's unruled seam* | the seam table's `investigation | UNRULED` row is **`:479`**; the *"INVESTIGATION MUST NOT BE MADE A CONTEST"* note is **`:502-505`** |
| *"`proceedings/08_SEAM.md` PART B"* | path is **`proposals/2026-09-05-proceedings-subsystem/08_SEAM.md`**, PART B at `:46`, *"registers the `if` as a shim"* at `:51` |
| *"the `AX-5` three motions are seasonal"* for keeping CALENDAR once per season | AX-5's three are **matter, bodies, the fading of memory** (`01_AXIOMS.md:151`). It licenses **MATTER**. CALENDAR stays seasonal on `04 §C.1`'s barrier 1 plus D-17/D-45, not on AX-5 |
| ED-SC-0033's own cites (`shape.py:6740`, `rosters.yaml:441-446`) | stale; the literal is **`shape.py:4122`**, the prizes **`rosters.yaml:539-543`** |

---

## §3 · ENTRY STATE

**`main` = `f41f20a1`.** `engine/season/` holds `shape.py` (4,153), `combat_seam.py` (189), `gaps.py`,
`trace_log.py`, `data/`, `state/`, `harness/`, `tests/`, and four YAML files: `rosters.yaml` (1,036),
`verb_table.yaml` (555), `write_matrix.yaml` (372), `hole_register.yaml` (2,746), plus
`requirements.yaml` (289) and `ENDINGS_CLASSIFIED.yaml`.

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
  a verb declaring `contests:`. Today that is `kill / wound` alone —
  `test_season_shape.py:7866` asserts `contested == {"kill / wound": "the body"}` — and no corpus
  person can form one, because `W23` requires *"the target must be a PERSON"* while *"today a question's
  referent is a rung or a Proposition"* (`architecture/PLAN.md:1516-1518`). A producer with no
  contested verb is a carrier with no reader; a contested verb with no producer hits
  `raise Unspecified("the degree ladder's margin model", "S39.4", …)` at `shape.py:4148`.
  **They land in one unit.**
- **R-09 → R-07 — HARD.** `H-62` (`hole_register.yaml:715`) records the supplied shape: *"an interior
  write is a CONSEQUENCE OF AN OUTCOME, which is what the new Degree-keyed `writes` column declares"*,
  matching `04 §F.20a:1083`. No degree on a corpus-reachable verb ⇒ `Person.stance` has a writer that
  never runs. `write_matrix.yaml:203-209` already carries the row — `steps: [RES]`, `class: ACTS`,
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
  ACTOR AND DELEGATION IS UNBUILDABLE HERE."* Verified: `state/carriers.py:306-344` (the whole `Act`) has no `via` field.
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

Steps 7, 8 and 9 of the decomposition are pure moves of exactly the modules R-07/R-08/R-09 land in.
Landing R-work in `shape.py` first and moving it a step later edits the same lines twice and re-runs the
guard-blinding recurrence, which has now been measured three times (steps 2, 4, 5 — PR #383's body
records step 5's: *"Three gates read `files.SHAPE_PY` alone and did narrow"*).

Landing it **after** the carve puts each mechanism in its Layer-1 directory from its first commit, which
`04 §E.1:1047` requires for `decision/` in terms:

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

**Preconditions.** PR #383 merged to `main`. Checkable: `git ls-tree origin/main engine/season/` lists
`loop/`, `queries/` and `epistemic.py`, and `wc -l engine/season/shape.py` reads **2,803**.

**Step 7 → `decision/` + `queries/person_q.py`.** Moves: `make_chooser`; `align` / `ALIGNMENT*` /
`alignment_at` **whole and together** (the H-66 sweep rebinds `S.ALIGNMENT` at
`test_season_shape.py:2302` and restores it at `:2317`); `stance_toward`, `urgency`,
`person_side_eligible`, `operands_for`, `pack_scenes`, `sense`, `view_ids`, `aggregate_questions`,
`body_band_penalty` (`shape.py:1908`), and the four person-side statics as functions.
**`decision/` is a DIRECTORY** (§5).

**Step 8 → `seam/`.** Moves: `contest_subsystem` (`shape.py:3875`), `_LADDER` + `_LADDER_ERROR` +
`degree_ladder` + `ladder_error`, `Resolution`, `combat_degree`, `degree_of` (`:4040-4065`), `contest`,
`ContestError`. `combat_seam.py` moves in and imports `decision.body_band_penalty` by dotted path.
⚠ **Grep the moving functions for `global` before the carve**: `degree_ladder` executes
`global _LADDER, _LADDER_ERROR` at `shape.py:3979`.

**Step 9 → `loop/driver.py`.** Moves: `SeasonDriver` (`shape.py:2724`) **including the witness deposit
body, whole** (§2.2), `as_scenes`, `stratum_of`, `resolvable_verbs`, `names_a_verb`,
`SOURCE_353_TEXT` (`:2276`) + `_S353_CACHE` (`:2273`).

**Acceptance — verbatim, after EVERY step:**

```
python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD
python -m pytest engine/season/tests -q
python -m pytest tests/valoria/test_engine_does_not_import_systems.py -q
```

**Expected observable:** `CONTENT HASH: ee0383bf3f4606e56b80cd07c0284f0a`; `PROBE FLIPS 0`;
186 passed; 17 passed. ⚠ **`report` before `delta`, in that order and in one command.** `delta.py:8-12`:
*"THIS COMPARISON IS VACUOUS UNLESS YOU REGENERATE `results.json` FIRST … `PROBE FLIPS 0` is TRUE BY
CONSTRUCTION rather than measured. It cannot fail."* `[UNVERIFIED: the 186/17 counts are test-function
counts read from source (`grep -c "^def test"`), not observed pytest outcomes.]`

**Falsifiers, per step.**

- **(7)** `grep -E 'import.*(world|queries\.world_q|state)' engine/season/decision/*.py` → 0, **and**
  `test_w5_sense_is_still_the_only_world_taking_non_decision_function` (`test_season_shape.py:2224`)
  still passes its vacuity floor — `assert len(found) >= 5, "the AST walk found only … it is not
  seeing person-side code"` at `:2279`. And the H-66 sweep
  (`test_w5_the_alignment_table_is_swept_at_three_points_and_every_flip_is_printed`, `:2291`) must
  still flip ≥1 verdict, which requires `alignment_at` to read `ALIGNMENT` through the **owning
  module's globals**, not a copied binding.
- **(8)** `test_we_the_ladder_is_the_trees_own_and_not_a_copy_of_it` (`:7798`) still moves every band
  when `S._LADDER` is replaced (`:7837-7845`) — so `degree_of` must read `_LADDER` through `seam`'s
  globals and the facade must alias the **module attribute**, never copy it.
- **(9)** every `inspect.getsource(SeasonDriver.<step>)` resolves to a real body, and the **D-45
  AST falsifier is written at this step**: exactly one assignment to `w.tick` in `loop/driver.py`
  (`04 PART D row 45`, `:979` — *"`t += 1` occurs once, in the driver"*).

**Control.** `python -m pytest engine/tests -q` byte-identical — the `mc_v18` campaign goldens. The
season package never enters the campaign RNG; verified structurally by
`test_engine_does_not_import_systems.py::test_importing_engine_pulls_in_no_subsystem`.

**Hash: does not move.** A pure move that moves it is not a pure move.

---

### U1 · R-09's producer + R-05b minimal — ONE UNIT

**Rows.** R-09 `not_met` → `partial` (§7 says why not `met`). R-05 stays `not_met`; its measured line
moves from *"1 of 32 declares `contests:`"* to *"3 of 32"*.

**Preconditions.** U0 step 8 merged. Checkable: `engine/season/seam/__init__.py` exists and
`python -c "from engine.season.seam import contest, degree_of"` succeeds.

**New file — `engine/season/seam/dice_seam.py`.** Full intended shape:

```python
"""THE DICE PROVIDER — the seam's wrapper around the tree's ONE die rule.

Layer 1 `04 §A.2` types `seam/wrappers/*` as writing "nothing, ever", reading "the projection",
returning "a Margin", holding token "none". This module is that row. It DECIDES NOTHING: it derives
a pool and an obstacle from what the actor and the subject genuinely have, calls
`engine.autoload.dice_engine.roll_pool` (`:196-206`, TN 7 refused otherwise), and returns the
net/ob pair. It NEVER returns a band -- `seam.degree_of` reads one by calling `degree_from_net`,
which is the single owner (`dice_engine.py:227`).

⚠ THE PRECEDENT IS `combat_seam.py` AND IT IS FOLLOWED, NOT REINVENTED: derive exactly what the
actor genuinely has, leave every other operand at its registered fixture, and return a typed gap
rather than fabricate a party.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/`. It reaches `engine.autoload.dice_engine`, which
`shape.py` already calls (`:3986`), so NO entry is added to
`tests/valoria/test_engine_does_not_import_systems.py::PATH_SEAM_ALLOWED` (`:220`), which stays at
its two shrink-only members.
"""
from __future__ import annotations
import random
from typing import Any, Optional

from engine.autoload.dice_engine import roll_pool
from .providers import provider


@provider("dice")
def resolve(w: Any, claimants: list[str], causes: list[str], prize: Any, *,
            verb: str, subject: Optional[str], rng: random.Random) -> dict:
    """Roll for one contested act. Returns net/ob, NEVER a band.

    RESOLVED -> dict(status, module, resolver, pool, ob, net, rolls, seed)
    REFUSED  -> dict(status, why, pool, ob)     # S27.4: ob > obstacle_refusal_multiple x pool
    """
```

**What it may import:** `engine.autoload.dice_engine`, `.providers`, `..data.fixtures`, and the
`state/` carrier types **for reading only**. **What it may not:** anything under `systems/`; anything
under `..decision`; anything that mints a write token.

**What enforces each, structurally.**

| discipline | enforced by |
|---|---|
| **no write, ever** | **the signature has no token parameter.** `World.write` refuses without one, and `world.py:325` refuses a step class not in the row. A wrapper with no token cannot reach the gate at all — `04 §A.2`, `04 PART D row 22` (`:952`) |
| **no second ladder** | it produces **no band string**. `tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` (`:452-474`) flags a file producing **≥2** band strings; a file producing zero cannot trip it, and cannot drift either |
| **no `systems/` reach** | `test_engine_does_not_import_systems.py`, 17 tests; `PATH_SEAM_ALLOWED` at `:220` stays `{'cross_scale/combat_bridge.py', 'season/combat_seam.py'}` |
| **AX-2** | `dice_seam` is in `seam/`, not `decision/`; it takes `w`, which `decision/` may never |

**New file — `engine/season/seam/providers.py`.** `PROVIDERS: dict[str, Callable]` filled at import by
a `@provider(name)` decorator, on the `@effect_for` pattern (`shape.py:2320`). `combat_seam.resolve`
gains `@provider("personal_combat")`. The table is a **module-level rebindable** and is exposed from
its owner, per guard rule 4 (§9).

**Changed — `engine/season/seam/contest.py`.** The literal
`if _sub["module"] == "personal_combat":` (**`shape.py:4122`** today) is **deleted** and replaced by
`PROVIDERS[row.provider]`. ED-SC-0033 (`registers/editorial_ledger_sc.jsonl:33`) rules exactly this:
*"the seam dispatches by manifest ROW rather than the hardcoded `personal_combat` literal"*;
`proposals/2026-09-05-proceedings-subsystem/08_SEAM.md:51` *"registers the `if` as a shim"*.

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
        provider: "dice"
        interim:  true
        cite:     "ED-SC-0033 (2026-09-06) rules the proceedings subsystem owns all social contests
                   and the orphaned tree retires. Wiring `systems/social_contest/` now wires a
                   retired tree. `dice` is the interim provider; this is A ROW CHANGE when
                   proceedings lands, not a code change (02 §D.4)."
      "a proposition":
        module:   "social_contest"
        provider: "dice"
        interim:  true
        cite:     "as `a standing`"
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
*"contest prizes ⊆ the subsystem roster"* (`04:467`) — is extended: **every named `provider:` must be
registered in `PROVIDERS` at load, or the load refuses naming the row.**

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
`contests:` (`04:470-472`). See §7 for which bands and why no Event kind is invented.

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
(`test_season_shape.py:7887-7899`, inside `test_we_only_a_verb_that_declares_contests_can_be_graded_today`
at `:7849`) is **rewritten** to assert the producer set is exactly `{seam/dice_seam.py}` — the
`\bnet\b\s*=|roll_pool|\bsuccesses\b` regex unchanged, `_code_only_lines` (`:7900`) unchanged, the
corpus still `files.package_modules()`. **Red today** (the set is empty and the assertion is
`assert not producers`), **green after**, **red again on any second site**. In the same commit,
`:7866`'s `assert contested == {"kill / wound": "the body"}` becomes the three-verb set, and
`:7872` moves to the row schema.

Plus, per §2.5: an AST count of `random.Random` construction sites over
`files.package_modules()` minus `tests/` returns exactly `{loop/driver.py, combat_seam.py}`.
Plus `test_w9_check1_the_run_is_reproducible` (`:2652`) green: two runs of one seed are hash-identical.
Plus seed 0 and seed 7 degree histograms differ — **if they do not, the RNG is not seeded from the run
seed**, which is the failure a same-seed determinism test cannot see.

**Controls — three, and (a) is the strong one.**

- **(a) BYTE-IDENTITY, PRODUCER-WITH-NO-CALLER.** Land `dice_seam.py`, `providers.py`, the dispatch
  and the fixtures **with `contests:` NOT yet declared on `tell`/`speak`**. The headless hash must
  still read `ee0383bf3f4606e56b80cd07c0284f0a`. **A producer no verb calls is byte-invariant.** This
  separates *"the roll exists"* from *"the roll is called"*, and it is the only arm in this unit that
  can fail for the right reason.
- **(b)** `python -m pytest engine/tests -q` byte-identical.
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
4. **COST CONTROL, AND IT IS A THEOREM.** A person is re-deliberated in round `r` **only if** a claim
   landed for them since their last deliberation **or** `sense(p, w)` changed. `Query.opening_set`
   (`shape.py:561-630`) depends only on `(p, v, q, fx)` and `p.ledger`; with no new claim and the same
   Sensation the candidate set is **identical by construction**, so re-running it is provably wasted.
   Otherwise the person takes the next scene of their standing ranking.
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
             sourced from systems/characters/conviction_taxonomy_v30.md §2 and exported to
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
    source: "references/descriptor_registry.yaml:257 -- 4 ethical axes; engine/substrate/keys.py::AXES"
```

```yaml
  tables:
    conviction_projection:         # NEW. 13 x 4.
      source: "systems/characters/conviction_axis_matrix_v30.md / PP-687, registered by reference at
               references/descriptor_registry.yaml:257"
      row: H-46
      default_cell: 0.0
      sweep: [declared, uniform, sign_only]
      keys: [convictions, conviction_axes]
```

**`tables.alignment` is UNCHANGED in shape** — `keys: [conviction_axes, verb_table]`, 32 × 4 = **128
cells**, which is the figure the planner quoted and which is only correct under this reading. Loader
invariant 8 (`04:472`, *"alignment keys ⊆ axes × verbs, and not all zero"*) continues to hold with no
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

**Expected observable.** The import succeeds (the twelve invariants fire at import); `corpus_run`'s
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

**`decision/` from its first commit** — `04 §E.1:1047`, quoted in §5. Not drafted in `loop/` and moved.

**Acceptance — verbatim:**

```
python -m pytest engine/season/tests -q -k 'sampling or w5_sense'
python -m engine.season.harness.corpus_run
```

**Expected observable.** The same person and view over **20 seeds** yields **≥2 distinct top acts**;
`corpus_run`'s `DISTINCT EXECUTED SETS` rises from 2; the tie-ordering line changes.

**Falsifier — and it is a byte-identity one.** **`tau = 0` must be BYTE-IDENTICAL TO HEAD** for
`build_world(0)`: same content hash, same Event multiset. A sampler whose zero-temperature limit is not
the old `argmax` changed two things at once. Both prior plans name this arm independently.

**Control.** The `tau = 0` arm above, **and** the structural one:
`test_w5_sense_is_still_the_only_world_taking_non_decision_function` (`:2224`) still finds no `World`
in any `decision/` signature.

**Hash: MOVES at shipped `tau`; DOES NOT MOVE at `tau = 0`.** Both recorded; the second is the control.

---

### U5 · R-07 — W-F: an outcome moves `Person.stance`

**Rows.** R-07 `partial` → `met` on its measure. R-08's *"inclination"* gains a live input.

**Preconditions.** U1 merged. Checkable: `corpus_run` prints a non-empty `DEGREES RESOLVED:` line.

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

**Control — byte-identity, on the harm-model pattern already in the tree.** `rosters.yaml`'s
`wound_harm_models` roster (`:360`, registered at `H-125`; the magnitude row is `H-123`) carries two
declared control arms and names both: *"⚠ `total` IS THE CONTROL AND IT IS THE CODE AS IT STOOD"*
(`:371`) and *"`none` is the SECOND control and isolates the other half: a wound writes nothing"*
(`:375-377`). **`stance_delta` copies the `none` shape.** The **`none` arm**, where every
`stance_delta` cell is zero, must leave `Person.stance` **empty** and the log **without** any
`stance.moved`. If a zero table still moves stance, the delta is not the mechanism.

**Hash: MOVES on the `declared` arm; DOES NOT MOVE on the `none` arm.** Both recorded.

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

**Controls.** `observation_deposit_mode=none` arm ≥ the default arm; `fan_out_mode=total` arm as R7's
control (its own falsifier,
`test_r7_two_persons_hold_different_things_and_at_total_they_cannot`, is named in
`requirements.yaml:248`).

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
`harness/exercises.py:12-20` records. `[UNVERIFIED: exercises.py:12-20's exact wording was not read
this session.]`

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
  (`scale_transitions_v30.md §2` — **THE SCALE SET ONLY**; its *"Base Ob"* column is thread-only and is
  **not an obstacle source**, Jordan 2026-09-05).
  `[UNVERIFIED: scale_transitions_v30.md §2's contents were not opened this session.]`
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
write by a banner is a **rejection at review** (`04 PART D rows 1/8/14`). `grep -rn 'superior\|liege\|rank'
engine/season/state/` shows **no field**. The permuted-`rung_kinds` run (`row 28`, `:959`) stays green.

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

**Owner: `engine/season/seam/dice_seam.py`.** Layer-1 `seam/wrappers/*` — `04 §A.2:150`, whose row
reads, verbatim: **`| seam/wrappers/* | nothing, ever | the projection | a Margin | none |`**. It has no
token and writes nothing; it returns the subsystem's own result, which `degree_of` (moving to `seam/` at
step 8) grades through **the one ladder** — `shape.py:4050-4061`, `label[degree_from_net(result["net"],
result["ob"])]`.

The "subsystem" it wraps is the substrate's root primitive `engine/autoload/dice_engine.py::roll_pool`
(**`:196-206`** — §2.10), whose die rule is the tree's only one (`_die_result`, `:151-158`, *"1 = -1
success, 2-6 = 0, 7-9 = +1 success, 10 = +2 successes. No chain."*, cited to `params/core.md §Die Rule,
PP-246`) and which refuses any TN but 7 via `_require_tn7`. The shape precedent is `combat_seam.py`:
derive exactly what the actor genuinely has, return a typed gap rather than fabricate.

### Why this is not the second resolver `T-k` refuses, and not the "generic roll" the roster refuses

`rosters.yaml:514` opens the `contest_subsystems` note with *"⚠ A CONTEST IS A DISPATCH, NOT A GENERIC
ROLL."* Two separate answers:

1. **The provider returns `net`/`ob`, NEVER a band.** The band is read by `degree_of` calling
   `degree_from_net`, and that identity is already pinned:
   `test_we_the_ladder_is_the_trees_own_and_not_a_copy_of_it` (`:7798`) asserts
   `lad[0] is degree_from_net and lad[1] is DEGREE_LABEL` and then **replaces `S._LADDER` and requires
   every band to move with it**. A wrapper producing no band string also cannot trip
   `tests/valoria/test_degree_ladder_single_owner.py::test_no_new_hand_rolled_ladder` (`:452-474`),
   which flags a file producing **≥2** band strings.
2. **The roster's refusal is of routing by `if`, and this is a provider resolved by ROW.**
   `04 §C.5:682`, verbatim: `provider = manifest.resolve("contest", prizes[prize])   -- by string, at
   boot`. Dispatch by row is the shape the note **asks for**, and ED-SC-0033 rules it.

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
`REFUSED` to the **existing** `attempt.refused` Event at `shape.py:3471-3487` — **which today is
unreachable**, because `Act.obstacle` defaults to `None` (`state/carriers.py:332`) and nothing sets it.
S27.4's refusal is therefore evaluated **on the derived pair inside the provider**, and that gate finally
has a reachable input.

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
  (`requirements.yaml:72-74`; one writer, `probes.py:432`, which zeroes it — §2.3), and `08 §3` gives
  assumption ⇒ inject-declare-sweep, **never refuse the whole corpus**.
  `[UNVERIFIED: 08_DATA_AND_KEYS.md §3's exact wording was not read this session.]`
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
rejection 4** (`:854-859`), verbatim: *"When R-09's producer is built … **its generator must be
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

It is also **the exact spelling `combat_seam.resolve` already uses** — `combat_seam.py:153`,
`seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)`,
consumed at `:160`. That function is refactored to **take** `rng` rather than build its own; **the same
seed string ⇒ byte-identical combat results, and that identity is the refactor's own test.**

**After U1 there are exactly two `random.Random` construction sites in the package** —
`loop/driver.py::resolve` and `combat_seam.py:160` — and the falsifier counts call sites, not text
(§2.5).

**Determinism controls that must hold.** `test_w9_check1_the_run_is_reproducible` (`:2652`);
`test_r4_event_ids_are_unique_per_draw_and_reproducible` (`:1143`);
`test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` (`:1266`); and the campaign
goldens under `engine/tests` **untouched** — the season package imports `engine.autoload.dice_engine`
(lazily, at `shape.py:3986`) and nothing imports the season package into `mc_v18`, which
`test_engine_does_not_import_systems.py`'s subprocess walk verifies.

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
`news.untold`. **Both kinds are already declared on the row**, so **loader invariant 7** — *"the
Event-kind roster is **derived** from every emission column, and the log accepts no other kind"*
(`04:466`) — admits them and **no Event kind is invented.** `writes:` stays `[]` at every band, and a
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
python -c "import engine.season.shape"              # the twelve invariants fire at import
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
   and a flat `glob` would silently drop eight of them."* **A new directory — `seam/`, `decision/` — is
   scanned the day it exists, with no edit anywhere.** The margin-producer scan already reads
   `files.package_modules()`, which is why U1's falsifier needs no corpus change.
2. **EVERY DERIVED-CORPUS GATE CARRIES A VACUITY FLOOR** in the `test_h115` form
   (`test_season_shape.py:452`, floor at `:556`): `assert len(mods) >= 8, f"model set collapsed to
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
   `python -m engine.season.harness.register --requirements` (`:375`). **No gate this arc writes needs
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
| step B retirement; the Godot port | — | gated on R-04 (`CLAUDE.md` §3). `04 §C.12` rejection 4 is the **only** port constraint this arc must honour, and U1 does — it is what makes it load-bearing | after U9 |
| the `systems/` constant migration (252 uncited) | §0.05 backlog | **outside the loop's data path**; touched only where a seam reads a constant, and U1 and U9 read none | per-seam, as seams land |

⚠ **Two numbering schemes collide and a session will trip on it.** `references/design_rulings_2026-09-06.md`
numbers **R1..R8**; `engine/season/requirements.yaml` numbers **R-01..R-09**. **Design-ruling R8
(partial observation, `:198-320`) is not `R-08` (non-rational choice).** Commits `c3dca09` and `01141b4`
are ruling-numbered. Design-ruling R8's work has not started, so there is no live collision today.

---

## §11 · WHAT NEEDS JORDAN — AFTER THE FIVE TESTS

**Every candidate closes. ZERO escalations**, matching both prior plans' counts. Recorded so a later
session does not re-open them — the ED-IN-0185 failure `CLAUDE.md` §0 names.

| candidate | closes at | by |
|---|---|---|
| where the pool comes from (`verb_capability`, `pool_default`) | test 5 | `08 §3`: assumption ⇒ inject-declare-sweep; post-adoption §6 trap 14 |
| how `ob` is derived | tests 1 + 3 | Jordan 2026-08-14, *"their corresponding score/2 plus whatever specific modifiers exist for them in that instance"* (`dice_engine.py:242-245`); *"Base Ob by scale"* struck by Jordan 2026-09-05. ⚠ Registered as an nth site, not a single owner (§2.10) |
| a dice provider vs. wiring the old social kernel | tests 1 + 5 | **ED-SC-0033** (`registers/editorial_ledger_sc.jsonl:33`) rules the proceedings subsystem owns all social contests and the orphaned tree retires — *"wiring it now wires a retired tree"*. The provider is resolved by row and repoints when proceedings lands: **a row change, not a code change** |
| which verbs gain `contests:` first | test 5 | the smallest corpus-executing set that makes R-09 measurable; the alternative is stated in §7 |
| scene tick shape (rounds; player granularity) | tests 1 + 4 | R-03's statement is **newer** than #353 S26.2; `rosters.yaml:455-460` records Jordan's granularity constraint verbatim |
| whether the tick may skip a person with no news | test 5 | **a theorem** of AX-2 (U2 decision 4), with its own falsifier (U2 falsifier b) |
| softmax sampling for R-08 | tests 1 + 5 | R-08 **is** the ruling; `tau` is assumption with `tau = 0` as the byte-identity control; both prior plans converge |
| the 13 convictions replacing the 4-axis stand-in | tests 3 + 4 | `references/descriptor_registry.yaml:235-251` already declares them and exports them behind a **blocking** `--check` (`valoria-ci.yml:137`). ⚠ **Narrowed by §2.6:** what closes is *may we READ the tree's own single-owner roster* — yes, and `H-46`'s own cite calls that a data edit. **`H-46` stays OPEN and its `absent` grade does not move**, on Jordan's *"may be modified in future"*. Populating is not closing |
| the 10 world-scale cases | test 5 | `PLAN.md:1613-1617` decides ≥2 realm rungs and records it on `H-95`. *"Jordan may overturn it; that is a ruling, not an open question this plan waits on."* |
| investigation: a contest or its own kind | test 5, **and de-scoped** | `04 §C.4` gives a degree only through `contests:`; a single-claimant provider is lawful (only combat refuses <2 — `combat_seam.py:142-145`); `rosters.yaml:502-505`'s *"not a contest"* is a note on the mechanism's shape, and `03 §E.1:220`'s *"an examination"* is not clearly the detective sense. **Nothing in this arc needs the answer**; the row stays UNRULED with this disposition recorded so it is not escalated by default |

---

## §12 · CRITICAL FILES

- **`engine/season/shape.py`** — the driver (`SeasonDriver`, `:2724`), the chooser (`:773-818`), the
  seam (`:3875-4153`) until steps 7–9 move them. **Every unit's entry state is a line here**, and every
  line number here is against `main` `f41f20a1` (4,153 lines), **not** #383 (2,803).
- **`engine/season/combat_seam.py`** (189) — the precedent `dice_seam.py` copies: derive one field,
  return the gap, per-draw `H` seeding at `:130, :153, :160`.
- **`engine/season/verb_table.yaml`** (555, 32 rows) — `contests:` and the degree-keyed
  `writes` / `emits` columns (U1, U5, U7); the seven-form `requires_typed` cells.
- **`engine/season/rosters.yaml`** (1,036) — `contest_subsystems` (`:510`, prizes at `:539-543`),
  `conviction_axes` (`:145`) and `tables.alignment` (`:975`) for U3, the seam table at `:474-482`, the
  granularity ruling at `:455-460`, and the new `verb_capability` / `stance_delta` / `scale_of_rung`
  rows.
- **`engine/season/write_matrix.yaml`** (372) — the `Person.stance` row at `:203-209`, already declared,
  already emitting `stance.moved`, and listed at `:50` among the RES-stepped rows with no producer.
- **`engine/season/tests/test_season_shape.py`** (8,078; 186 test functions) — `_model_modules()`
  (`:491`), the no-producer scan (`:7887-7899`), the AST guard (`:2224`), and the rebind sites
  (`:2302`, `:7012`, `:7837`) every carve and every R-unit must keep honest.
- **`engine/autoload/dice_engine.py`** — `_die_result` (`:151-158`), `degree_from_net` (`:227`),
  `roll_pool` (`:196-206`). The single owner, imported and called, never mirrored.
- **`architecture/meta/04_CODE_ARCHITECTURE.md`** — §A.2 `:127`, §C.1 `:502`, §C.2 `:520`, §C.4 `:573`,
  §C.5 `:677`, §C.5.1 `:699`, §C.7 `:743`, §C.12 `:810` (rejection 4 at `:854`), PART D `:923` (header
  `:928`), §E.1 `:1038`, F.15 `:1077`, F.20a `:1083`, §F.24a `:1090`, §B.13 `:441`, G.2.9 `:1317`,
  G.3.1 `:1355`, G.3.5 `:1414`.

---

## §13 · SIZE — measured, and over the convention's threshold

**Measured, not estimated:** 1,520 lines, **24,868 tokens** at
`tools/ci_common.py::tokens` — the repo's single owner of that estimate, characters ÷ 4. ⚠ **Say
which character count**: Python `len()` gives **99,474** and `wc -c` gives **100,697 bytes**, and
the gap is this file's own `§`, `⚠`, `→` and `≥`. `tokens()` divides the first. Both are true of
their own basis, which is the failure mode `CLAUDE.md` §0.1 names and which PR #383 paid for once
already (*"One instrument, named, for numbers that get compared."*). That is
**over** `references/atomization_rules.yaml`'s `sequential_chunk_tokens: 15000`, and the first
drafting of this section claimed it was under. It was not; the claim is retracted here rather than
left standing, which is the only move available to a document whose whole subject is citation fidelity.

**What that means in practice, stated so the next session does not re-derive it.** The threshold is a
`WARNING`-level convention (`CLAUDE.md` §4), not a blocking gate: the sibling
`workplans/2026-09-06-season-loop-execution-plan.md` is **23,206 tokens** and sits on `main` with CI
green. So this file is *at the same size as its closest peer and subject to the same convention*, and
shipping it as one part is a deliberate choice, not an oversight.

**Where it splits, when someone does split it.** At the §6/§7 boundary: §1–§6 are verification and
sequence, §7–§12 are the deep placement argument and the repeatable procedure. `_part2` would open at
§7 and the break is a reading-order break, not a filing one. Do not split at §2 — the corrections are
what license every citation reproduced downstream of them, and separating them from the units would
recreate the index+infill shape `CLAUDE.md` §4 retired.
