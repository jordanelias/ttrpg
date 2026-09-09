# `engine/season/shape.py` — DECOMPOSITION PLAN v2 (steps 7–10, executable)

## Status: **PROPOSED. Reference under §0.05 — delete this file and the game behaves identically.**
## Lane: IN, ED-IN-0203. Supersedes `workplans/2026-09-06-shape-decomposition-plan.md` for steps 7–10 and 0a.

**Why a v2 rather than an edit.** v1 was written 2026-09-06 against a 6,771-line `shape.py`. Six
steps have landed since; `shape.py` is **2,803** (`wc -l`). v1's §1 table now describes a tree that
does not exist, three of its artifacts cannot fail, and one of its placements contradicts ratified
architecture. Patching it in place would leave a reader unable to tell which rows were re-derived
and which were merely survivors. v1 stays as the record of steps 0b–6; **rows 1–6 of its §1 table
are history, not instructions.**

**Method that produced this.** A read-only planner (fable tier, §10) audited v1 against the tree; a
read-only adjudicator (opus) ruled the `sense` placement; a read-only inventory (sonnet) enumerated
the step-7 set. Every number below carries the command that produces it. Where a claim is a *reading*
of an assertion rather than a *run*, it says so.

---

## 0 · What v1 got wrong, so the next reader knows why this exists

| # | v1 says | measured | cost if followed |
|---|---|---|---|
| 1 | `sense` → `decision.py` (`v1:106,:176`) | `04:116` *"`sense()` called by the loop, never by the decision"*; `04:133` enumerates `decision/`'s four members without it; `04:158` grants `loop/deliberate` the frozen World *"for `sense` only"* | `decision.py` names `World`; AX-2 violated in the commit that creates the island |
| 2 | step-7 artifact `grep 'import.*\(world\|queries\)' decision.py` → 0 (`v1:235`) | matches `import world`; **misses** `from .state.world import World` and `from .queries.world_q import presence` — the package's only idiom | a real violation prints 0. **Verified empirically** |
| 3 | step 9 → a flat `loop.py` (`v1:109,:237`) | `engine/season/loop/` is a **package**; a sibling `loop.py` is shadowed | step 9 unbuildable as specified → `loop/driver.py` |
| 4 | `decision.py` owns `_load_alignment`/`ALIGNMENT*`/`alignment_at` (`v1:106`) | they have lived in `data/verbs.py` since step 3 | moves a loader out of `data/`, against `04:131`'s "the ONE loader" |
| 5 | step 10 = "delete the facade" (`v1:238`) | `rg -c '\bS\.[A-Za-z_]\w*' engine/season` → test **627**, `corpus_run` **53**, `headless` **17**; and `test_season_shape.py:35` reads `files.SHAPE_PY` **at module level** | the 186-test module stops collecting the moment the file is gone |
| 6 | v1 §0's rebind list names `ALIGNMENT`, `_LADDER`, `belief_contradicts`, `probes._s.contest` | **`pack_scenes` is rebound too** — `arm9_forking.py:115`, `arm9_subj.py:115`, `arm7_flexibility.py:66,82` — and the suite imports the first two (`test:7300`, `:7626`) | a silent no-op in a fork measurement the suite reads |
| 7 | 0a runs first (`v1:227`) | `HANDOFF_IN.md:140,:395` already re-filed it as step-10 debt | converting to `shape.py::symbol` now and `<owner>.py::symbol` later is double work |

**Also corrected here, from this session's own shipped prose:** `belief_contradicts` is rebound at
**8 assignment lines in 2 files (4 install, 4 restore)**, not "six sites"; step 7's person-side bill
is **45 live call expressions** (47 including two in a frozen self-contained snapshot that resolves
against its own `Query`); and the rebind hazard is **not silent** — all three names are caught by an
existing assertion. The residue is two *script-only* rebinds (`wd_acceptance.py`, `arm7_flexibility.py`)
that cannot fail the suite and would mismeasure on re-run.

---

## 1 · Standing constraints — every step, stated once

- Branch-bound to `claude/shape-py-refactor-6f7uiu`.
- Every carve is a **pure move**; each step's declared exceptions are listed in its own row and
  nowhere else.
- `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` →
  **`ee0383bf3f4606e56b80cd07c0284f0a`**, unchanged.
- **`report.py` BEFORE `delta.py`, always** (`__init__.py:29-32`). `delta.py` compares a committed
  artifact against an unchanged working copy and prints `PROBE FLIPS 0` whatever changed.
- The eight `runs/` artifacts byte-identical, **except two declared diffs**: step 7's
  `results.json` `_probes.P28.detail` and step 10's one line in `PROBES.md`. Never hand-edit `runs/`.
- `register.py --requirements` reads **6 `not_met` · 3 `partial`** throughout. **Zero game yield is
  expected and is not a failure**; a step that moves it has done something else.
- `pytest engine/season/tests` **and** `pytest tests/valoria` at every step — not the subset v1 named.
- **One new test *function* in the whole remaining plan** (step 7, AX-2). Zero new test files.
  Steps 1–6 added zero; §0.1 pt 5 binds every addition.
- Counts: **state the command and the basis.** `wc -l` for line counts — `len(split("\n"))`
  over-counts a newline-terminated file by one, which has now cost two corrections.

### 1.1 · The three instruments that must be run, and what each cannot see

| instrument | sees | **cannot** see |
|---|---|---|
| headless content hash | any change to campaign-reachable state | module layout (invariant by construction) |
| `report.py` + `git status runs/` | any artifact byte moving | *why* it moved |
| `delta.py HEAD` | probe **verdict** flips | a changed probe **detail** string (step 7's P28) |

---

## 2 · Step 7 — `engine/season/decision.py`

**Flat file at the package root**, precedent `epistemic.py`. Layer 10.

### 2.1 Moves (`shape.py` line, HEAD `e03abff2`)

⚠ **Basis, stated because two sources gave figures differing by one:** every line number below is the **`def` line**, not the `@staticmethod` decorator line above it. `budget`'s decorator is `:324` and its `def` is `:325`. Reproduce with `ast`, not by eye.

`Query.budget` :325 · `Query.opening_set` :371 · `Query.assemble` :443 · `Query.entrenchment` :466
— all four as **module functions** · `align` :543 · `stance_toward` :549 · `urgency` :561 ·
`make_chooser` :583 · `person_side_eligible` :631 · `containing_rung_of` :696 · `store_kind_of` :758 ·
`_derive_operand` :783 · the comment block :850-864 **including its `# roster-exempt:` line at :862**
· `_REFERENT_OPERANDS` :865 · `operands_for` :868 · `agreement` :957 · `standing_of` :988 ·
`_payload_of` :1012 · `pack_scenes` :1026 · `aggregate_questions` :1163 · `view_ids` :1193 ·
`body_band_penalty` :1224.

**Does NOT move, against v1:** `sense` (:1239 — step 9, §0 row 1) and the alignment block (stays in
`data/verbs.py`, §0 row 4).

**`class Query` (:295-468) is deleted whole.** Ruling: paying the renames once beats a facade that
owns a class for three steps while `v1:110` says it "owns nothing". Renames, both families:

```
Query.<world-first>(  -> world_q.<name>(     48 call expressions
Query.<person-side>(  -> decision.<name>(    45 call expressions (live)
```

Command: `rg -c 'Query\.(parent_of|descendants|r1_aggregate|aggregate_guard|single_holder_counter|commit_count_guard|lateral|verbs|hold_force|judging_set|presence)\(' --glob '*.py' engine/season`
and the person-side equivalent. Plus three non-call sites: `probes.py:455`
(`signature(Query.opening_set)` → `decision.opening_set`, same parameters), `probes.py:796`
(`dir(Query)` → the public names of `decision` — **this changes P28's detail string**, §2.4), and the
`Query` entries in the import lists at `test:31` and `probes.py:36`.

**The one edit inside a moved body, declared:** `:610` `Query.opening_set(` → `opening_set(`.

### 2.2 Imports — exactly

`typing` · `.data.rosters` (`CONVICTION_AXES, ELIGIBILITY_KINDS, PERSON_PREDICATES,
QUESTION_AGGREGATION, SCENE_PACKING_RULES, VIEW_BUILDER_RULES`) · `.data.verbs` (`ALIGNMENT,
ALIGNMENT_DEFAULT_CELL, VERB_TABLE`) · `.epistemic` (`belief_contradicts` — **module-level,
UNALIASED**) · `.gaps` (`Forbidden, InstrumentDefect, Unspecified`) · `.state.carriers` (`Act,
Candidate, Person, Question, Scene, Sensation, View`) · `.trace_log` (`TRACE`).

⚠ **`.state.carriers` is a RUNTIME need** — `Act`, `Scene`, `Candidate`, `View`, `Question` and
`Sensation` are constructed, not merely annotated. `04:570`'s *"`decision/` … does not import
`state/`"* describes the idealized store layer; do not try to satisfy it literally by deleting a
constructor's import.

**Never:** `state.world`, `queries.*`, `loop.*`, `seam`, `combat_seam`, `shape`.

### 2.3 Hazards to clear BEFORE cutting

- `global` statements in the set: **none** (`shape.py`'s only one is `:2629`, in `degree_ladder`).
- `globals()` in the set: **none**.
- Decorator registries in the set: **none**.
- **Rebinds — re-point all of these in the same commit:**

| name | sites | to |
|---|---|---|
| `ALIGNMENT` | `test:2354, :2357, :2401, :2415` | `decision.ALIGNMENT` |
| `belief_contradicts` | `test:7069, :7080, :7097, :7107` | `decision.belief_contradicts` |
| `pack_scenes` | `arm9_forking.py:60,:115,:119` **and its byte-identical twin lines in `arm9_subj.py`** | one alias added in `sweep_core.py` |

⚠ `test:7630-7636` asserts `arm9_subj.py` differs from `arm9_forking.py` in **exactly one line** (the
fingerprint) and that both have equal line counts. Edit both identically or that test fires — which
is the guard, not a risk.

**Leave and record:** `wd_acceptance.py:283,:288,:401,:405` and `arm7_flexibility.py:66,:69,:82,:90`
— nothing imports either, so they cannot fail the suite; both would mismeasure on re-run.

- **Home-claim sweep** over `hole_register.yaml`, `requirements.yaml`, `rosters.yaml`, `CLAUDE.md`,
  `CURRENT.md`, `HANDOFF_IN.md`, **and `architecture/`** (frozen `> ### LANDED` blocks excepted).
  Both spellings — `shape.py … <symbol>` and `shape.<symbol>` — **file-scoped, not line-scoped**
  (YAML block scalars wrap). Verify each new home against `__module__`, never by grep.

### 2.4 Artifacts

Hash · eight artifacts byte-identical **except `results.json`'s `_probes.P28.detail`, which changes
from "(15 functions)" because `dir(Query)` is gone — diff that field by JSON, since `delta.py`
compares verdicts only and will print `PROBE FLIPS 0` regardless** · `PROBE FLIPS 0` · identity
`getattr(shape, n) is getattr(decision, n)` for every moved name · `_code_only(src)` then `\bQuery\b`
→ **0** across every `.py` under `engine/season/` (a bare grep misses `dir(Query)` and
`signature(Query.x)`).

**The one new permanent test function** — in `test_season_shape.py`, no new file. AST over
`decision.py`: no `Import`/`ImportFrom` resolving to `state.world`, `queries`, `loop`, `seam`,
`combat_seam` or `shape`; no `Name`, `Attribute` or string `Constant` equal to `World`.
**Earns its place under §0.1 pt 5:** `decision.py` is Layer-2 game code, AX-2 is ratified, `04:1046`
asserts *"the isolation scan matches by path"* and **no such scan exists** — the axiom's only
enforcement today is a grep that cannot fire. The existing `test:2261` checks signatures only.

### 2.5 Falsifiers — reproduce verbatim

```
a  leave test:2354 as `S.ALIGNMENT = ...`                    -> RED at test:2376
b  leave test:7069 as `S.belief_contradicts = counted`       -> RED, shipped=[]
c  plant `from .epistemic import belief_contradicts`         -> RED  (UNALIASED; `as _bc` PASSES)
     as the first line of decision.opening_set
d  plant `from .state.world import World` in decision.py     -> the new AX-2 test RED
   plant `def _x(p: Person, w: "World"): pass`               -> test:2309 RED
e  run `pytest -k test_wd_` BEFORE editing the arms          -> RED proves the arm edit is load-bearing
```

⚠ **(e) GREEN is itself a finding**, not a pass: it would mean the test never observed the fork
(§0.1 pt 2). Make the arm edit either way, for the sweep's reproducibility.

⚠ **(c) is the step-6 lesson.** `from X import Y as Z` binds `Z`; the aliased form leaves the call a
global lookup and **passes**. A recipe that omits the call-site swap teaches the next session the
opposite of the truth.

### 2.6 Tier

**Sonnet executes** — every judgment call is ruled above. **Opus critic** — this step carries the
three rebinds and the arm edit.

---

## 3 · Step 8 — `engine/season/seam.py`

`combat_seam.py` does **not** move: moving it edits `PATH_SEAM_ALLOWED`
(`test_engine_does_not_import_systems.py:220`) and `files.py:134` for zero yield.

**Moves:** `ContestError` :1268 · `contest_subsystem` :2525 · the S39.4 block :2563-2616 · `_LADDER`
:2618 · **`_LADDER_ERROR` :2619** · `degree_ladder` :2622 *with its `global` and its root insert
as-is* · `ladder_error` :2645 · `Resolution` :2651 · `combat_degree` :2663 · `degree_of` :2685 ·
`contest` :2722 *with its local `from . import combat_seam` at :2773*.

**`combat_seam.py` co-edit, same commit:** `:122-123` → `from .decision import body_band_penalty`;
`:137,:153` → `from .state.ids import H` at module level (the deferral existed only for the cycle).

**Facade re-exports** everything above **except `_LADDER` and `_LADDER_ERROR`** — a rebound value
cannot be re-exported correctly, the facade would hold a stale snapshot, and nothing reads
`S._LADDER_ERROR`.

### 3.1 Hazards

- `global _LADDER, _LADDER_ERROR` — **both move or the second is silently duplicated.** `global`
  creates a module binding on first assignment, so a missing `_LADDER_ERROR` raises nothing and the
  facade's copy stays `""` forever.
- ⚠ **Blocking repo test co-edit:** `tests/valoria/test_import_cycle_game_state_npe.py:108` asserts
  `len(cycles) == 4` and `:121-122` pins `{engine.season.combat_seam, engine.season.shape}` by exact
  member set. Step 8 dissolves that cycle → **change 4 to 3, delete the `seam_shape` family, amend
  the docstring at `:71-78`, in the same commit.** Omit this and `main` goes red.
- **Do NOT re-point `probes.py`'s A39 spy here** (v1:236 says to). Its reader is
  `SeasonDriver.resolve`, still in `shape.py` at step 8; re-pointing makes the spy a no-op →
  `captured` empty → `AssertionError` → `INSTRUMENT-ERROR` → a probe flip. **It belongs to step 9.**
- Do not do PLAN 1.6's composition half here.
- Home-claim sweep as step 7.

### 3.2 Artifacts & falsifiers

Hash · artifacts · `PROBE FLIPS 0` · identity for every moved name ·
`rg -c '^_LADDER_ERROR' engine/season/shape.py` → **0** and `engine/season/seam.py` → **1** ·
`test_engine_does_not_import_systems.py` (seams still exactly two) ·
`test_import_cycle_game_state_npe.py` green at **3**. One-off; no new test.

```
a  leave test:7896 as `S._LADDER = ...`      -> RED at :7898
b  build seam.py WITHOUT _LADDER_ERROR       -> everything stays GREEN. That IS the demonstration;
                                                the grep pair above is what goes red
c  skip the combat_seam co-edit              -> cycle test RED (a 3-cycle that is not the pinned pair)
   do it without the test co-edit            -> cycle test RED (3 != 4)
d  re-point A39's spy here                   -> A39 flips to INSTRUMENT-ERROR in delta.py
```

**Tier:** Sonnet executes; **Sonnet critic** suffices — the one silent item is fully specified and
grep-checked.

---

## 4 · Step 9 — `engine/season/loop/driver.py`

**Not `loop.py`** — `engine/season/loop/` is a package and a sibling module is shadowed (§0 row 3).
`loop/__init__.py:12` already names `driver.py`.

**Moves:** `stratum_of` :471 · `resolvable_verbs` :485 · `as_scenes` :1141 · **`sense` :1239**
(re-routed from step 7) · the comment blocks :1281-1308 and :1361-1371 · `names_a_verb` :1309 ·
`_S353_CACHE` :1333 · `SOURCE_353_TEXT` :1336 · **`class SeasonDriver` :1374-2518 whole, bodies
byte-identical to HEAD** (its `Query.*` sites were already renamed at step 7).

⚠ **§3's "module functions the methods delegate to" is struck.** `test:146` asserts `driver="Event"`
is in `getsource(witness)`; `:320` asserts the comparator string; `:720` is a **negative** assertion
over witness's own source. A delegating stub fails the first two and vacates the third. **Whole
bodies, no delegation.**

Add `LOOP_DIR` and `DRIVER_PY` to the one anchor (`data/files.py`).

### 4.1 Hazards

- **A39's spy, now:** `probes.py:2445` → `from ..loop import driver as _s`.
- **Four `files.SHAPE_PY` readers break HERE, not at step 10** — v1:237 tells the step-9 session they
  are green: `test:613` (positive, subject is `SeasonDriver.resolve`) → a `DRIVER_CODE`;
  `test:1709` `_write_call_sites` → `_model_modules()` + `PROBES_PY` (the non-narrowing choice; the
  `("Person","claim_ledger")` coverage travels with `witness`); `test:1723-1726` (`_apply_write`
  span) → `files.DRIVER_PY` **and the file component of each `"file:line"` in `dynamic`**;
  `test:6264` (`StopIteration` otherwise) and `test:6413` → `files.DRIVER_PY`.
- `wd_extra.py:75,:80` rebind `S.questions_for` — imported by nothing; record.
- Home-claim sweep: `hole_register.yaml` names `shape.py` as home for `SeasonDriver.*` at `:760,
  :909, :1350, :1353, :1363-1379, :1462, :1525-1528, :1755-1765, :1843-1850, :1999`.

### 4.2 Artifacts & falsifiers

Hash · artifacts · `PROBE FLIPS 0` · `shape.SeasonDriver is driver.SeasonDriver` ·
every `inspect.getsource(S.SeasonDriver.*)` test green unchanged (`:146, :320, :596, :617, :651,
:720, :1052, :2445`) · **the textual-purity instrument the step-6 handoff said did not exist**:
extract the `SeasonDriver` class source by `ast` node span from `git show HEAD:engine/season/shape.py`
and from `loop/driver.py`, and diff — **must be empty**.

```
a  leave A39 on shape          -> delta.py prints `A39: PASS -> INSTRUMENT-ERROR`
b  leave test:1723 on SHAPE_PY -> RED at :1726;  :6264 -> StopIteration;  :6413, :613 -> RED
c  change one character in the class -> the class-source diff is non-empty
```

**Tier:** Sonnet executes (1,300 lines, but a block move with a byte-diff instrument); **Opus critic**.

---

## 5 · Step 10 — delete the facade, and convert the citations (0a folded in)

**0a is NOT first.** Converting to `shape.py::symbol` now and `<owner>.py::symbol` later is double
work; `HANDOFF_IN.md:140,:395` already re-filed it here.

### 5.1 Code half

Delete `shape.py`; delete `files.py:133`; fix `files.py:111-112` (`shape.degree_ladder()` →
`seam.`). Rewrite every `S.`/bare-name import in `tests/test_season_shape.py`,
`harness/{probes,corpus_run,headless,run_cases,report}.py` and
`proposals/2026-09-04-degree-sweep/sweep_core.py:40` **from a generated name→owner map** — parse the
facade's `ImportFrom` nodes at HEAD, one alias per owner module; the script lives in the scratchpad
and its command goes in the commit message. Delete `test:35` and `:67`. Re-point `test:1872`'s
anti-vacuity set to the files the model was carved *into*. `report.py:148` → name the package
(**declared one-line `PROBES.md` diff**). Fix the stale "keep resolving" sentences at `gaps.py:3`,
`state/ids.py:3`, `state/world.py:6`, `state/carriers.py:7`. Reconcile `CLAUDE.md` §3 and
`CURRENT.md:32` — **28 modules = 20 model + 8 harness**, step 10 of 10, no `shape.py` length.

### 5.2 Prose half (0a)

Basis: `rg -c 'shape\.py:\d+' --glob '!proposals/**'` → **115 lines / 15 files** (v1's 101/19 is
stale and repo-wide). Add the spellings `shape\.py \(line \d+\)` (used at `hole_register.yaml:1775`),
`shape\.py::\w+` and `shape\.<symbol>`; **file-scoped**. Convert to
`engine/season/<owner>.py::<symbol>` from the same map. **Frozen, do not touch:** `proposals/**`,
`registers/*.jsonl` (append-only), `architecture/PLAN.md`'s `LANDED` blocks, dated history sections
of handoffs. A citation to a pre-decomposition line inside a dated finding gets an `(at 480cb43)`
label, not a rewrite. **No checker** — §0.1 pt 5 forbids it and v1 was right about that.

### 5.3 Artifacts & falsifiers

`python -c "import engine.season.shape"` → `ModuleNotFoundError` ·
`pytest tests/valoria/test_engine_does_not_import_systems.py` — **the instrument**, since it imports
every `engine/**/*.py` by dotted path in a subprocess · `_code_only` + `\b(shape|S|_s)\.` → 0 over
`engine/season/**` and the sweep dir · hash · seven artifacts byte-identical, `PROBES.md` differing
in exactly the declared line · `results.json` unchanged · `register.py --requirements` 6/3 ·
before/after counts of the citation command.

```
plant `from .. import shape as S` in headless.py  -> the import gate RED
plant `x = S.Person` in corpus_run.py             -> NameError in the same gate
```

**Tier:** Sonnet executes both halves; **Opus critic** — deletion is where a wrong rename stays
silent until something executes it.

---

## 6 · Order, and what each agent is handed

**Strictly serial: 7 → 8 → 9 → 10.** Each removes a different region of `shape.py` and rewrites its
import block; 8's `combat_seam` edit needs `decision`; 9's driver needs `seam`'s bare bindings; 10
needs every owner to exist. Worktree parallelism is not worth the merge on one file. Within step 10,
the prose half runs after the code half — they share `test_season_shape.py`.

**Relay per step:** producer (Sonnet) → read-only critic (Opus for 7/9/10, Sonnet for 8) →
reconcile → next producer. **The next producer starts only on a reconciled base**, so each step
stays independently revertible.

**Handed to each producer, so nothing is re-derived:** its section of this document verbatim; the
symbol list with `shape.py` line numbers; the destination map; the rebind table with test line
numbers; the falsifier recipes; the instrument commands; and the standing constraints of §1.

**Handed to each critic, additionally:** *re-verify every count with its stated command. A count on
an unstated basis is how v1's call-site figure went wrong, and how this session published "six
sites", "47 calls" and "2,804 lines" — three corrections in two days, all the same error.*

**Touch nothing under `proposals/2026-09-04-degree-sweep/**` except:** `arm9_forking.py:60,:115,:119`,
its twin lines in `arm9_subj.py`, and one alias in `sweep_core.py` (step 7); `sweep_core.py:40`
(step 10).
