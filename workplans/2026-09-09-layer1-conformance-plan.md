# LAYER-1 CONFORMANCE, THEN THE GATE, THEN THE R-WORK — EXECUTION PLAN

## Status: **PROPOSED. REFERENCE under `CLAUDE.md` §0.05 — delete this file and the game behaves identically.** Nothing here may be cited as the reason a behaviour is correct. It ratifies no design call; the one call it *records* was ruled by Jordan and is filed in `registers/editorial_ledger_sc.jsonl`.
## Lane: IN. ED-IN-0206 (the Layer-1 gap this closes) · ED-SC-0037 (ruled, see §4) · ED-IN-0203 (the decomposition it inherits).

> **What produced this.** A read-only assessment of PRs **#383**, **#384** and **#385** against the
> working tree at `8b79440`, with every execution claim re-run rather than read. The instrument
> outputs are §1. Where a merged commit's prose is wrong about the tree, §2 and §3 say so with the
> command that shows it.
>
> ⚠ **TIER DRIFT, DECLARED.** Jordan assigned this node to **Fable 5.1** (§10's planner/audit tier).
> `get_session` reports `configured_model: claude-opus-5`, `last_served_model: claude-opus-5`,
> effort `xhigh`. The assessment and this plan were produced on **Opus 5**, not Fable. It is
> recorded rather than hidden because §10 makes the tier part of the method: **the review gates in
> §9 name `model: "fable"` explicitly and the Agent tool honours it, so the reviews Jordan asked
> for are reachable even though this planning node was not.** A later session must not read this
> document as a Fable product.

---

## §0 · WHAT THIS IS, AND WHAT IT IS NOT

**It is not a second R-plan.** `workplans/2026-09-09-r-execution-plan.md` is the single owner of the
nine R-rows, their dependency graph, and units U1–U10. This document **cites it and does not restate
it** — the de-duplication ruling #384 applied to its own U0 binds here (`CLAUDE.md` §8, *every rule
lives once*). What is here is only:

1. what the three merged PRs actually left on `main` (§1),
2. the one thing #383 got wrong and the tree already records (§2),
3. the Layer-1 gaps **ED-IN-0206 does not carry**, found by this assessment (§3),
4. Jordan's ruling closing ED-SC-0037 (§4),
5. the **two arcs that must precede U1**, unit by unit (§6, §7), and what changes in the R-plan (§8),
6. the method binding every unit (§9), and the fix-on-error rule for broken paths (§10).

**Everything in §6 and §7 is engineering against a written spec.** `04_CODE_ARCHITECTURE.md` is
RATIFIED (ED-IN-0204) and already decided every item. **No unit here is an escalation** — §0's five
tests close all of them at test 3 (answered by a design document). Do not open a `needs_jordan` row
for anything in §6 or §7.

---

## §1 · THE ASSESSMENT — every execution claim re-run, not read

Environment note: `pytest` and `numpy` are **absent from a fresh container** and were installed
(`pip install pyyaml pytest numpy`, per `CLAUDE.md` §8). A session reporting a suite result without
having installed them has not run one.

| claim, from the merged PR bodies | instrument re-run here | outcome |
|---|---|---|
| content hash `ee0383bf3f4606e56b80cd07c0284f0a` | `python3 -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` | **HOLDS** |
| all eight `runs/` artifacts byte-identical | `python3 -m engine.season.harness.report` then `git status --short` | **HOLDS** — clean tree |
| `PROBE FLIPS 0` | `python3 -m engine.season.harness.delta HEAD` | **HOLDS** — 122→122 probes, 66→66 gap events |
| 187 season tests | `python3 -m pytest engine/season/tests -q` | **HOLDS** — 187 passed |
| `pytest tests/valoria` green | `python3 -m pytest tests/valoria -q` | **1,776 passed · 2 failed** — `test_forked_status.py` ×2, the documented shallow-clone pair (`git rev-parse --is-shallow-repository` → `true`). Not a regression |
| requirements 6 `not_met` / 3 `partial` | `python3 -m engine.season.harness.register --requirements` | **HOLDS** — unchanged |
| local gates pass | `python3 tools/valoria_local.py` | **HOLDS** — "all local gates passed" |
| freshness / currency / ED citations clean | `freshness_gate.py`, `currency_consistency_check.py`, `validate_ed_citations.py` | **HOLDS** — 109 FRESH / 0 STALE; "all current"; 0 violations |
| `shape.py` is gone | `python3 -c "import engine.season.shape"` | **HOLDS** — `ModuleNotFoundError` |

**Verdict on the execution half of #383: it is sound.** Ten steps of pure move with a stationary
content hash, byte-identical artifacts and zero probe flips is a real result and the instruments
reproduce it independently. **#385 is sound and small** — the escalation it filed is the row that
should have existed, and its `id_reservations` walkback is honest.

⚠ **Two non-blocking measurement notes, so neither is re-derived as a defect.** `headless` prints
*"verbs the fold can execute: 12 of 32"* while `requirements.yaml:202` reads *"6 of 32 verbs
execute"*. These are **different quantities** — `resolvable_verbs` (declared-and-foldable) versus
corpus-executed — and `loop/driver.py:91` says so at the site. Not a contradiction.

---

## §2 · WHAT #383 GOT WRONG, AND IT IS ONE THING

**Steps 7 and 8 executed the superseded plan, not the ratified spec, and the corrected spec was
already on `main` when they landed.**

- `cb28ec9` (#384) merged **2026-09-09 03:17**. `c3b51e3` (#383) merged **08:37**, five hours later.
- #384's own adversarial pass put **D2** on `main`: *"`decision/`, `seam/`, `manifest/` are
  DIRECTORIES … `decision/` must additionally be one FROM ITS FIRST COMMIT"*, citing
  `04_CODE_ARCHITECTURE.md:1046` — and **D5**: step 8 renames the `PATH_SEAM_ALLOWED` member to
  `season/seam/combat_seam.py` and `files.COMBAT_SEAM_PY` in its own commit.
- `workplans/2026-09-09-shape-decomposition-plan-v2.md` §2/§3 — authored **on #383's branch** —
  spells flat `decision.py` and `seam.py`, and `:202` states *"`combat_seam.py` does **not** move:
  moving it edits `PATH_SEAM_ALLOWED`"*. **That is D5 inverted:** the cost D5 priced as a rename
  inside a shrink-only set was read as a reason not to move.
- The tree records the divergence honestly at
  `workplans/2026-09-06-shape-decomposition-plan.md:246`: *"step 8 built `seam.py` as a FLAT module
  and did **not** move `combat_seam.py` … the rename that row demands was **avoided rather than
  performed**."*

**This is not a defect in the carve.** Every line moved correctly and every instrument agrees. It is
a **plan-selection** defect of exactly the shape #383 itself diagnosed and struck at source when
`arm7_flexibility` broke: *"correcting the copies leaves the source able to send it again"*. The
source here is v2 §2/§3, which is still `PROPOSED` on `main` and still says flat files.

**First act of Arc 1, before any code moves:** strike v2 §2's and §3's placement rows in place —
`decision/` and `seam/` are directories per `04:127-139` and `04:1046`, and `combat_seam.py` becomes
`seam/wrappers/combat.py` with the `PATH_SEAM_ALLOWED` member renamed in the same commit. Do not
delete v2; mark the rows superseded and name what replaces them, the way v1 §4 was marked.

---

## §3 · THE GAPS `ED-IN-0206` DOES NOT CARRY

ED-IN-0206 counts **six** structural non-conformances plus the write token as *"related and
larger"*. Measured against `04` PART A/B/C, the count is **higher**, and one of its six is **partly
wrong**. Both directions matter.

### §3.1 · Undercounted — the whole §C.2 gate contract is unbuilt, not only the token

| `04` requires | in the tree | measured by |
|---|---|---|
| §B.9: `Receipt := (id minted BY THE GATE, kind, field, subject id, before, after)`; `Event.changes[] : Receipt[]`; *"only the gate mints a Receipt"* | **`Receipt` does not exist.** `grep -rn "Receipt" engine/season --include=*.py` → **0** | grep, 0 hits |
| §A.2: `state/gate` owns *"the one write path: `write(token, kind, field, id, change) -> Receipt`"*; `state/log` and `state/ledgers` are separate owners | `state/` is `carriers.py` · `ids.py` · `world.py`. The gate is a **method on `World`** (`state/world.py:295`) | `ls engine/season/state/` |
| §C.2: `token.class in classes_of(row.steps)` | `write(thing, wclass: WriteClass, apply: Callable, …)` — the class is a **parameter** and the step is read off `self.step` | `state/world.py:295-300` |
| §C.2 F3: AX-4 clause 2 — `kind is Tenure ⇒ actor == subject(id)` … *"otherwise raise `NotYours`"*, and `via` MUST be present for T-o | **no `actor`, no `via`, no `NotYours`.** `grep -n "actor\|via" engine/season/state/world.py` returns comments only | grep |
| §C.2 F9: `before == after ⇒ raise NoOpReceipt` | absent | grep, 0 hits |

**And AX-4 clause 2 cannot be built without `Act.via`, which is `H-108` and is separately R-04's
hard blocker** (R-plan §4). One unit closes both. That is the reason Arc 2 is worth its cost rather
than being deferred into the R-units: `04` PART E puts the gate at **step 3**, ahead of RESOLVE
(step 6) and ahead of step 8, *"THE BAR"*.

### §3.2 · Overcounted — item (2) contradicts `04 §A.2:130` for two of its four symbols

ED-IN-0206 item (2) reads: *"`queries/person_q` DOES NOT EXIST. §A.1's AX-2 row assigns the
person-side family to `queries/person_q`; step 7 put budget/opening_set/assemble/entrenchment in
`decision.py` instead."*

**`04 §A.2:130` names two of those four as `decision/`'s own members:** *"`decision/` AX-2's
island: questions · **opening_set** · choose · **budget**. NO World in scope."* So `opening_set` and
`budget` are **where the spec puts them**, and moving them to `queries/person_q` on ED-IN-0206's
wording would break conformance rather than restore it. `§A.1`'s AX-2 row governs the **Query
families**, not `decision/`'s named members; `§A.2`'s table gives `queries/person_q` *"owns nothing
… may read a `PersonInterior` snapshot only"*.

**L3 is therefore an adjudication unit, not a move unit** (§6). Per symbol, against `§A.2:130` and
the `§A.2` table, decide `decision/` versus `queries/person_q` and record the reason at the site.
`assemble` (question assembly) reads as `decision/`; `entrenchment` reads as `person_q`; **both are
to be argued from the spec rows, not assumed from this sentence.**

### §3.3 · The stale continuity surface, which is a Layer-0 defect

`registers/handoffs/HANDOFF_IN.md`'s **top two sections** both read
`⏳ PRODUCED 2026-09-09, NOT YET COMMITTED` — for decomposition **step 8** and **step 7**. Both
merged in #383. `CLAUDE.md` §1 names this file as one of two continuity surfaces a cold session
orients from, and its first 430 lines currently tell that session that landed work is uncommitted.
`workplans/workplan_v6_progress.yaml` is stamped `as_of: c75c561, 2026-08-19` — twenty-one commits
back — and is the board `m1_acceptance.py`'s row 4 counts, which is why that row reads `0/7`.

---

## §4 · JORDAN'S RULING, 2026-09-09 — `ED-SC-0037` IS CLOSED

Put to Jordan as the ledger row's two options. **He ruled a third**, verbatim:

> **"we have the sigma leverage d10 resolver in engine to use"**

**The interim contest provider is `engine/autoload/sigma_leverage.py`.** Recorded because it is
better than either option the row costed, and the reasons are checkable:

- `sigma_leverage.roll_net(pool, tn, rng) -> int` / `roll_net_continuous(...) -> float` return a
  **net**, which *is* a `Margin`. §C.5's contract — *"the subsystem returns a `Margin`; a subsystem
  returning a winner has not met the contract"* — is satisfied by the function's return type, not by
  a wrapper's discipline.
- It **answers option A's cost.** ED-SC-0037 priced an interim provider as *"deriving its own
  obstacle in-seam, an nth obstacle site immediately after ED-SC-0033 clause (3) ruled THE OBSTACLE
  HAS A SINGLE OWNER."* `sigma_leverage` **already owns the obstacle model** — `eff_ob`,
  `effective_ob`, `sigma_space_ob_shift` — so the seam derives nothing and clause (3) is honoured.
- It is **not a new seam.** `engine/season/seam.py:205` already imports
  `engine.autoload.dice_engine.degree_from_net` — the single-owner ladder (ED-SC-0031). Reaching one
  module further inside `engine/` adds **no** `PATH_SEAM_ALLOWED` entry, because nothing under
  `systems/` is touched. Option A's *"generic roll the seam roster refuses by name"* does not apply:
  this is the canonical d10 resolver the faction layer already rolls through (PR #311), not a bare
  pool-vs-fixture roll.
- It leaves ED-SC-0033 clause (2) intact: the two prizes still **repoint** to the proceedings
  provider when it lands. The manifest row is the repoint site, which is the whole point of
  `manifest/`.

**Flip the row in the same commit that lands this file** (`CLAUDE.md` §2, ED-1094): `status: ruled`,
`needs_jordan: false`, Jordan's sentence verbatim, and the provider named.

---

## §5 · THE ARCS, AND THE ORDER

**Jordan's ruling on depth: *structure now, gate contract next*.** Three arcs, strictly serial
between arcs, parallel where a unit says so.

```
ARC 1  Layer-1 STRUCTURE      L0 → L1 → L2 → (L3 ∥ L4) → L5        zero game yield, declared
ARC 2  the GATE CONTRACT      G1 → G2 → G3 → G4                     zero game yield, declared
ARC 3  the R-WORK             U1 … U10, per the R-plan               game yield
```

**Zero game yield is the expected result of Arcs 1 and 2 and is not a failure** (`CLAUDE.md` §0.2).
`register.py --requirements` reads **6 `not_met` / 3 `partial`** before and after every unit in Arcs
1 and 2. **A unit in Arc 1 or 2 that moves a requirement status has done something it was not asked
to do — revert it and say so.**

**Arc 1 and Arc 2 are not milestone progress.** They are licensed as the precondition `04` PART E
puts on the critical path, and because §2's plan-selection defect will otherwise be paid a second
time when U1 lands `manifest/` and the provider into a `seam.py` that has to become `seam/` anyway.

---

## §6 · ARC 1 — LAYER-1 STRUCTURE, UNIT BY UNIT

**Every unit is a PURE MOVE plus the co-edits its own hazards name.** The invariant set in §12 holds
at every one. `sonnet` executes L0; `opus` executes L1–L5 (each has a placement judgment in it).

### L0 · Strike the superseded placement rows — no code moves

`workplans/2026-09-09-shape-decomposition-plan-v2.md` §2 and §3, and
`workplans/2026-09-06-shape-decomposition-plan.md:242`'s step-8 row. Mark the flat-file placements
superseded **in place**, name `04:127-139` and `04:1046` as what replaces them, and say that D5's
rename is performed rather than avoided. **Do not delete either document.** Precedent for the form:
v1 §4's own `⚠ STEPS 7-10 LANDED…` note.

**Artifact:** `rg -n "does \*\*not\*\* move" workplans/2026-09-09-shape-decomposition-plan-v2.md` → 0.
**Tier:** `haiku` for the edit, `sonnet` to verify the two files agree afterwards.

### L1 · `decision.py` → `decision/` — the one unit with a spec-mandated *first commit*

`04:1046`: *"`decision/` is a directory from its first commit. The isolation scan matches by path, so
a `choose` drafted inside `loop/` and moved later would have been green while violating AX-2."*

- `engine/season/decision.py` (58,762 bytes) becomes `engine/season/decision/` with `__init__.py`
  re-exporting its public names. **Split by §A.2:130's four members** — `questions`, `opening_set`,
  `choose`, `budget` — not by line count.
- **The AX-2 guard must become the scan `04:1046` specifies.** `test_season_shape.py:2396`
  (`test_decision_module_never_names_world`, `FORBIDDEN_MODULES` at `:2450`) walks the AST of **one
  file** and #383's own step-10 commit corrected its docstring to say so: *"04:1046 specifies a scan
  BY PATH over a directory … this test walks the AST of one file and is structurally blind to
  that."* Re-point it at **every `*.py` under `decision/`**, keep the derived-signature check
  (`\bWorld\b` by token, which is the version that catches `Optional[World]` and the
  future-annotations string form), and keep the `inspected >= 5` floor.
- **Earns its guard under §0.1 pt 5**: `decision/` is Layer-2 game code and the axiom is ratified.
  This is a re-point of an existing guard, not a new one.

**Falsifiers, both arms, reproduced and reverted:**
```
a  plant `from ..state.world import World` in a NEW file under decision/   -> the path scan RED
   (the pre-fix AST test, pointed at __init__.py alone, is GREEN on the same plant — that is the
    blindness 04:1046 names, demonstrated rather than asserted)
b  plant `def f(w: "World")` imported from epistemic into decision/        -> the signature check RED
```

### L2 · `seam.py` → `seam/`, and `combat_seam.py` → `seam/wrappers/` — D5 performed

Per §A.2:135 (`seam/  contest() · ladder · one wrapper per deferred subsystem`) and the §A.2 table's
three rows `seam/contest`, `seam/ladder`, `seam/wrappers/*`.

- `seam/contest.py` — `contest`, `contest_subsystem`, `ContestError`, `Resolution`, `degree_of`.
- `seam/ladder.py` — `_LADDER`, `_LADDER_ERROR`, `degree_ladder`, `ladder_error`, `combat_degree`.
  ⚠ **`_LADDER`/`_LADDER_ERROR` stay out of any re-export**, for the reason #383 established: a
  rebound value re-exported is a stale snapshot, and `degree_ladder`'s guard reads `_LADDER_ERROR`
  on every first call, so both drop-one constructions are **LOUD** (`UnboundLocalError` /
  `NameError`) — verified at step 8, and the brief's "stays green" prediction was wrong.
- `combat_seam.py` → `seam/wrappers/combat.py`. **Three co-edits in the same commit:**
  `PATH_SEAM_ALLOWED` (`tests/valoria/test_engine_does_not_import_systems.py:220`) member
  `season/combat_seam.py` → `season/seam/wrappers/combat.py`; `files.COMBAT_SEAM_PY`
  (`engine/season/data/files.py:138`); and `_PC`'s `sys.path` insert, which is relative to the
  module's own location.
- **`test_the_one_declared_path_seam_is_still_the_only_one` (`:395`) asserts exact set equality
  (`:424`).** A rename inside a shrink-only set is not a widening. **The set must not gain a member.**

**Falsifiers:**
```
a  move combat.py, leave PATH_SEAM_ALLOWED  -> :395 RED naming both spellings
b  re-export _LADDER through seam/__init__  -> test_we_the_ladder_is_the_trees_own... RED
c  rg -c '^_LADDER_ERROR' engine/season/seam/ladder.py -> 1, everywhere else -> 0
```

### L3 · `queries/person_q` + `queries/cache` — ADJUDICATE, then move (∥ with L4)

**Read §3.2 first.** This unit's deliverable is **a per-symbol placement decision argued from
`04 §A.2:130` and the `§A.2` table, with the reason recorded at each site** — not the literal
execution of ED-IN-0206 item (2), which would move `opening_set` and `budget` out of the module
`§A.2` names as their owner.

- `queries/person_q.py` — the **asker-first Query family**; the `§A.2` table constrains it to *"may
  read a `PersonInterior` snapshot only"*, which is itself the test of whether a symbol belongs here.
- `queries/cache.py` — *"barrier indexes: presence, object-side Tenures, subtree aggregates … any
  store, **at a barrier only**"*. `presence` currently lives in `queries/world_q.py`; the barrier
  caches are built in `loop/driver.py`. Both are candidates and both must be named.
- **`queries/readers.py` is a module `§A.2` does not name.** `WorldReader`/`LedgerReader` are
  neither of the two Query families nor the cache. **Decide and record**: either they are `cache`'s
  neighbours by role, or `§A.2`'s list is short by one and the finding goes in the ledger row. **Do
  not silently leave a fourth unnamed module in a directory whose membership the spec enumerates.**

**Artifact:** a table in the commit message, one row per moved symbol: symbol · old home · new home ·
**the `04` line that decides it**. A symbol with no citation has not been adjudicated.

### L4 · `manifest/` — role → provider rows, resolved at boot (∥ with L3)

`§A.1:125` (Stage 2 §D.4), `§A.2:136`, and `04:1031`'s build step 10: *"a misspelled manifest row
fails at boot naming the row."* #384's Layer-1 correction already moved the provider registry here
from the `seam/providers.py` the planner proposed — **honour that; do not re-propose `seam/providers`.**

- `manifest/registry.py` + a data file the **one loader** in `data/` opens (`§A.2:131` — *"the ONE
  loader"*; a second loader is an `§A.2` violation).
- `manifest.resolve("contest", prizes[prize])` is the exact call §C.5 spells. Land the **signature
  and the boot-time failure**; land **no provider row yet** — the row is U1's, and its value is §4's
  `sigma_leverage`.

**Falsifier:** a misspelled role in the data file **fails at load naming the row**, and passes when
corrected. **A misspelling that fails at first call rather than at boot has not met §D.4.**

### L5 · `loop/` — driver + six steps

`§A.2:134`: *"`loop/` driver + six steps. The driver is the ONLY constructor of write tokens."*
`calendar`, `matter`, `deliberate`, `resolve`, `witness`, `census` are today **methods on
`SeasonDriver`** in `loop/driver.py`; the `§A.2` table gives each its own owned state, its own
`emits`, and **its own token**.

⚠ **THIS UNIT IS PARTLY BLOCKED AND MUST NOT BE FORCED.** The tokens are Arc 2's (G2). Land here
only what does not depend on a token: the **six modules**, each holding its step's body, with
`driver.py` reduced to the ordering and the caller. Where a step's body needs the token the driver
does not yet mint, it keeps taking `WriteClass` and **the commit says which of the six are provisional
on G2.** Do not invent a token type here to make the unit look finished — G2 owns it.

⚠ **The three `inspect.getsource(SeasonDriver.witness)` readers survive this unit** (`test_d2`,
`test_d9b`'s eviction comparator string, and
`test_witness_writes_no_belief_and_no_conviction`, which is a **NEGATIVE assertion** that keeps
passing while silently vacating its subject). #383 struck the deposit-body extraction for exactly
this reason. **Moving `witness` to `loop/witness.py` re-points those three at the new module by
`getsource` on the moved function; verify the negative one by planting a belief write and watching it
go RED.** A negative assertion not proven live by a plant has not been re-pointed, only relocated.

---

## §7 · ARC 2 — THE GATE CONTRACT

Order is forced: `Receipt` before the token (the token's `minted[t]` set holds receipts), the token
before AX-4 clause 2 (the check reads the token's class), and `NoOpReceipt` last because it is the
one clause that changes an existing write's outcome.

### G1 · `Receipt`, and `state/gate` as its own owner

`§B.9`: `Receipt := (id minted BY THE GATE, kind, field, subject id, before, after)`;
`Event := (id, kind, changes[] : Receipt[], causes[] NON-EMPTY or [ROOT], emitted_at, degree?)`;
*"only the gate mints a Receipt; the log's append asserts it."*

- `state/gate.py` — the write path moves off `World` and becomes the module `§A.2` names. `state/log`
  and `state/ledgers` follow **in this unit only if the move is pure**; if either drags behaviour,
  split it out and say so rather than widening the unit.
- `Event.changes[]` becomes `Receipt[]`. ⚠ **`R8.4` made `document_key` read `changes[]`** (PR #379)
  — that reader is the first thing to check, and the R8.4 repair must not be undone.

**Falsifier:** an `Event` carrying a hand-built (unminted) receipt **fails `append`**; the same
`Event` with a gate-minted receipt passes.

### G2 · The unforgeable token — `§A.3` row 3, the largest single gap

> *"write class as a **parameter** of the store API"* → *"an **unforgeable token type**, one per
> step, minted only by the driver; DELIBERATE receives none"* — forced by AX-4 + ID-9. *"A parameter
> can be passed by anyone; a token only by whoever was handed it."*

Four token types (CALENDAR · MATTER · ACTS · INTERIOR), constructed **only** in `loop/driver`
(`§A.2` table: *"mints all four"*), consumed by `gate.write`. `loop/deliberate` and every
`seam/wrappers/*` receive **none** — which is what makes §C.5's *"a state write from inside — no
token, STRUCTURAL"* true by construction rather than by convention.

**Falsifier — and it is the whole point of the unit:** a step **constructing its own token** must be
unable to; a `deliberate` or a wrapper calling `gate.write` must fail **for want of a token**, not
for want of a matrix row. Verify with a plant in each of the two places, reverted.

⚠ **This unit rewrites every `w.write(...)` call site.** `probes.py` alone holds ~20
(`grep -rn "\.write(" engine/season --include=*.py`). **The `runs/` artifacts and the content hash
must not move**, so the rewrite is mechanical and the invariant set in §12 is the proof.

### G3 · AX-4 clause 2 at the gate — `NotYours`, `actor`, `via`, and `Act.via` (closes `H-108`)

`§C.2`'s F3 block, which that document calls *"the largest defect in the first publication"*:
`gate.write(token, kind, field, id, change, actor?, via?)`, and for `kind is Tenure` one of the four
lawful bases or **`raise NotYours`**. `T-o` requires `via` **present**, so *"a revocation with no
seat in `Act.via` is refused at the gate"*.

**`Act` carries no `via : SeatId?`** (`state/carriers.py:305-339`) — `H-108`, which the R-plan's §4
records as a **hard blocker for R-04**. Land `Act.via` here. **This unit therefore has game
consequence downstream and is the one place Arc 2 touches Arc 3's graph.**

⚠ **`04` names the three live violations to expect, so they are not discoveries:** `verb_table.yaml`'s
`revoke` and `confer` both write `Tenure.until` on an edge whose subject is somebody else, and
`kill / wound` writes `Tenure.until` on the victim's edges. **Under the current gate all three are
lawful and none is declared as an exception.** Turning the check on will red them. **Declare each as
`T-o`-with-`via` or as its own basis — do not weaken the check to keep them green, and do not remove
a verb from the table to pass.**

### G4 · `NoOpReceipt` — `§C.2` F9

`before = get(); store._set(); after = get(); before == after ⇒ raise NoOpReceipt`.

⚠ **`04` states why the append-side check does not cover this:** *"A receipt with `before == after`
IS minted by the gate — so `work` emitting `site.worked` while accumulating no delta, which is the
instance `ID-9` is written from, passes the check unchanged. The append-side test could not observe
the failure it excludes; the write side can."* That is `CLAUDE.md` §0.1 pt 2 in the spec's own words.

⚠ **This is the one Arc-2 clause that can legitimately move output.** `work` is the corpus's
always-refused verb and a no-op write elsewhere may currently succeed silently. **If the content hash
moves here, that is a finding, not a break** — but it must be *isolated to this clause*, measured
with `delta.py` naming which probes flipped and why, and reported. **A hash move anywhere else in
Arcs 1–2 is a break.**

---

## §8 · ARC 3 — WHAT CHANGES IN THE R-PLAN, AND WHAT DOES NOT

`workplans/2026-09-09-r-execution-plan.md` remains the owner of U1–U10. Four amendments, to be
written **into that file** rather than kept here:

1. **§3 ENTRY STATE is stale.** It was written with #383 open and describes a `main` holding
   `shape.py` at 4,153 lines. Re-state it against the arc-completion tree, and **retire the `[#383]`
   marker discipline** — it marked statements about an open branch that is now `main`.
2. **U0 is DONE, and overshot its own stance.** §5 said *"step 10 … deferred to the end of the arc"*;
   #383 executed it. The rule §5 attached to that deferral — *"NO NEW SYMBOL IS RE-EXPORTED THROUGH
   `shape.py`"* — is satisfied vacuously and should be struck, not carried as live guidance about a
   file that does not exist. Replace U0 with a pointer to Arcs 1–2 as the real precondition.
3. **§11.0's escalation is CLOSED** by §4 above. Rewrite it as a recorded ruling with the provider
   named, and drop the *"may not be landed before it is ruled"* gate on U1 half (b).
4. **U1's provider is `engine/autoload/sigma_leverage.py`**, resolved through the `manifest/` row L4
   builds, with `dice_engine.degree_from_net` as the ladder — the composition §C.5 spells, with the
   margin producer and the ladder each in single ownership.

**Everything else in the R-plan stands**, including its §2 corrections, its §4 dependency graph, its
§7 roll placement, its §9 guard-blinding handling and its §10 non-goals. **Do not re-derive the
graph. Do not re-audit its ~190 citations.** It was verified once and the verification is its §1.

⚠ **`requirements.yaml` carries 11 stale `shape.py:NNNN` citations** — #384 found them, six out of
range even before the file was deleted. **The file is now gone entirely, so all 11 are dangling.**
Convert them by `::symbol` in whichever unit next touches that file (§10's rule).

---

## §9 · THE METHOD — AGONIST → ANTAGONIST, BINDING ON EVERY UNIT

**A relay, not a dialogue** (`CLAUDE.md` §10). Subagents are stateless and isolated: dispatch the
producer, capture its **output**, dispatch the critic **with that output and not the reasoning**,
reconcile in the orchestrator. For an audit that isolation is the *point* — a critic that never saw
the producer's reasoning is more independent.

**Independence is structural, never declared.** `.claude/agents/valoria-critic.md` declares
`tools: Read, Grep, Glob` — no Write, Edit or Bash — so `subagent_type: "valoria-critic"`
**cannot** write whatever its prompt says. A sentence inside a prompt saying *"you are read-only"*
restricts nothing.

### Per unit, four stages. None may be skipped or merged.

| stage | who | tier | what it hands on |
|---|---|---|---|
| **1 · PRE-FLIGHT** | producer | as §11 | the hazard list for *this* unit, derived by `ast` — not read off the brief |
| **2 · CARVE** | producer | as §11 | the diff, the invariant set (§12) re-run, the falsifiers run **and reverted** |
| **3 · ATTACK** | `valoria-critic`, read-only | as §11 | findings against the **working tree**, having seen only stage 2's output |
| **4 · RECONCILE** | producer | as §11 | each finding **applied, or rejected with the measurement that rejects it** |

### The five rules that make it fidelity work rather than theatre

1. **A finding is applied or refuted by measurement — never noted.** #383's arc rejected two critic
   findings correctly (the `decision.` bigram excusing 0 of 78 construction probes; `.state.carriers`
   as a ruled placement) and both rejections carry the number that licensed them. **A rejection with
   an argument and no number is not a rejection.**
2. **A pass that finds nothing has not run.** #383's arc found a real defect at **every** step, and
   three fix passes correctly refuted their own critic. Equally — and this is the symmetric half —
   **do not manufacture a finding to look diligent.** A genuinely clean stage 3 reports the scope it
   examined, the primitives it read, and the attack it tried that failed. *"Examined and found
   sound"* is a finding; *"did not examine"* is incompletion wearing a finding's clothes.
3. **A falsifier is reproduced verbatim, both arms, or it is not a falsifier.** Step 6's recorded
   mutation recipe **did not reproduce** — `from X import Y as Z` binds `Z` and leaves the global
   lookup intact, so a session following the note would have got GREEN and concluded the hazard was
   overstated. **Write the arm that fires and the near-miss that does not, and label which is which.**
4. **A selector is only as good as the paths you point it at.** Four distinct failures in the #383/#384
   arc were **a sufficient check reported as an exhaustive one** — *"no code opens these docs"*
   (grepped inline `open(...)`, missed a module constant); *"nothing else spells Layer"* (did not
   grep); *"exactly three programmatic readers"* (grepped three directories, missed
   `engine/season/`); *"eleven home claims"* (matched the literal `shape.py`, missed the dominant
   `shape.<symbol>` spelling, and was line-scoped over YAML block scalars). **State the scope of every
   count in the sentence that reports it**, and resolve names with `ast`, never by counting text —
   a `law=` string is not code.
5. **Measure at the merge, not at the commit you are standing on.** ED-IN-0203's trail ended in a
   wrong number twice for this reason. Two invariants it pinned were **already stale on `main`**
   because #380 merged 25 minutes after #381.

### The Fable gate — after each ARC, not after each unit

Jordan's instruction: adversarial reviews for correctness using **Fable 5.1, read-only**, after major
stages. **Three gates: end of Arc 1, end of Arc 2, end of Arc 3.** Each is one dispatch:

```
Agent(
  subagent_type: "valoria-critic",
  model: "fable",
  description: "Arc N conformance attack",
  prompt: <the arc's commit messages + the §12 instrument outputs, and NOTHING about how they were produced>
)
```

**What the gate is asked**, and it is deliberately narrow — §10 assigns `fable` the **audit and
guardrail** node, never synthesis:

1. Does the tree now conform to `04 §A.2`, item by item, **by path**? Name every remaining
   divergence and the `04` line that decides it.
2. Is any claim in the arc's commit messages **wrong about the tree**? Reproduce it.
3. Is any guard **narrower than the claim it is offered as proof of** — and specifically, did any
   source-scanning gate silently narrow when a symbol left the file it names? *(This has recurred at
   steps 2, 4 and 5. Assume it recurred again and look for it.)*
4. Which of this arc's falsifiers **fails to reproduce** from its recorded recipe?

**The gate's output is edits to the thing under review and at most one paragraph in the commit
message.** It creates no directory and no document (`CLAUDE.md` §0). It may append **at most one
ledger row, and only if that row requires a human decision.** A finding that needs no ruling is fixed
in that commit or dropped.

---

## §10 · BROKEN PATHS — FIX ON ERROR, NOT BY TRACING (Jordan-directed)

**Do not spend a stage tracing every path before starting. The error names the line.** The standing
rule for the whole plan:

> **When an instrument fails on a stale path, correct the path in the commit that surfaced it, and
> nowhere else.** Do not open a sweep. Do not file a finding. Do not add a guard whose subject is a
> path checker (`CLAUDE.md` §0.1 pt 5 — a pattern defect in an artifact load-bearing only on this
> repository's process is evidence the artifact can be wrong without cost).

**What the assessment already knows is broken, so no one re-discovers it as news:**

| what | where | fix in |
|---|---|---|
| two reproducer commands `python -c "…sys.path.insert(0,'engine/season');import shape as S…"` | `engine/season/hole_register.yaml:763`, `:817` | the unit that next touches either row; rewrite against `data/verbs.py` |
| 11 dangling `shape.py:NNNN` citations | `engine/season/requirements.yaml` | Arc 3, per §8 |
| a comment calling `shape.py` *"a facade"* in the present tense | `engine/season/data/files.py:135` | L2 (it is beside `DRIVER_PY`) |
| `INVENTED_VERBS` cited as living in `shape.py` and existing **nowhere** (`rg` → 0) | recorded by #383 as stale | delete the claim wherever the next unit meets it |
| `HANDOFF_IN.md`'s two `NOT YET COMMITTED` sections | `registers/handoffs/HANDOFF_IN.md:3`, `:178` | L0 — it is Layer 0 and a cold session reads it first |
| `workplan_v6_progress.yaml` stamped `c75c561` / 2026-08-19 | the board `m1_acceptance` row 4 counts | end of Arc 1 |

**Three environment facts that cost time if unknown:**

1. **`pytest` and `numpy` are not installed in a fresh container.** `pip install pyyaml pytest numpy`.
2. **Every season entry point is `python -m engine.season.harness.<x>`.** The flat
   `python engine/season/harness/report.py` spelling raises
   `ImportError: attempted relative import with no known parent package` — confirmed this session.
3. **The anti-fabrication gate is changeset-scoped and a pure rename defeats that scoping.** A
   constant untouched for weeks arrives at the gate looking new because the rename rewrote its line.
   It fired three times in #383. Reproduce CI's own view before pushing:
   ```
   GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
   ```
   ⚠ **The `# [JUSTIFIED: ...]` marker must sit COMPLETE on the line directly above the code.** A
   multi-line reason *ending* in `...]` stays red. Put the prose first and the marker last. And
   **measure the reason** — #383 labelled a constant from a hypothesis and had it wrong; a false
   citation on an anti-fabrication gate is worse than the red it fixes.

⚠ **`git rev-parse --is-shallow-repository` → `true` here.** `tests/valoria/test_forked_status.py`'s
two failures are that, not a regression. `git fetch --unshallow` before treating them as real.

---

## §11 · MODEL TIERING, PER UNIT

Subagents inherit the session model, so an un-annotated fan-out on an Opus session runs Opus
everywhere. **Set it per call** (`CLAUDE.md` §10).

| unit | producer | critic (stage 3) |
|---|---|---|
| **L0** strike the plan rows | `haiku` (mechanical edit) | `sonnet` |
| **L1** `decision/` | `opus` — the guard rewrite is a judgment | `opus` |
| **L2** `seam/` + wrappers | `sonnet` — spec-named split, three co-edits | `opus` (the `PATH_SEAM_ALLOWED` equality is where being wrong is silent) |
| **L3** `person_q` / `cache` | `opus` — §3.2 is an adjudication | `opus` |
| **L4** `manifest/` | `sonnet` | `sonnet` |
| **L5** `loop/` six steps | `opus` — the negative-assertion re-point | `opus` |
| **G1** `Receipt` | `opus` | `opus` |
| **G2** the token | `opus` | `opus` |
| **G3** AX-4 clause 2 + `Act.via` | `opus` | `opus` |
| **G4** `NoOpReceipt` | `opus` | `opus` |
| **arc gates** | — | **`fable`**, per §9 |

`haiku`'s prompt-cache minimum is **4,096 tokens** — the largest on the roster — so a shared preamble
under that floor **silently never caches** on a Haiku stage. And **parallel agents sharing a prefix
cannot read each other's cache**: fire one, await its first token, then fan out. Switching model
mid-conversation invalidates the whole cache, so escalate at **arc** boundaries.

**Parallel write lanes need `isolation: "worktree"`** — one repo, colliding trees otherwise — and
return **fixed-format summaries**, not raw context. Only L3 ∥ L4 are parallel here.

---

## §12 · THE STANDING INSTRUMENT SET — run after EVERY unit, in this order

```
pip install pyyaml pytest numpy                                  # fresh container only
python3 -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0
python3 -m engine.season.harness.report && python3 -m engine.season.harness.delta HEAD
python3 -m pytest engine/season/tests -q
python3 -m pytest tests/valoria -q
python3 -m pytest tests/valoria/test_engine_does_not_import_systems.py tests/valoria/test_import_cycle_game_state_npe.py -q
python3 -m engine.season.harness.register --requirements
python3 tools/valoria_local.py
GITHUB_EVENT_NAME=pull_request GITHUB_BASE_REF=main python3 tools/ci_sim_fabrication_check.py
```

**Expected, measured on `8b79440` this session — a unit returning otherwise has broken something
rather than revealed a miscount:**

| observable | value |
|---|---|
| `CONTENT HASH` | `ee0383bf3f4606e56b80cd07c0284f0a` |
| `git status --short` after `report` | **empty** — all eight `runs/` artifacts byte-identical |
| `delta HEAD` | `PROBE FLIPS 0`, probes 122→122, gap events 66→66 |
| `engine/season/tests` | **187 passed** |
| `tests/valoria` | **1,776 passed · 2 failed** (the shallow-clone pair only) · 23 skipped · 15 xfailed |
| `register --requirements` | **6 `not_met` · 3 `partial`** |
| `valoria_local.py` | `all local gates passed` |

⚠ **`report` BEFORE `delta`, always.** `delta.py:8-12`: *"THIS COMPARISON IS VACUOUS UNLESS YOU
REGENERATE `results.json` FIRST … `PROBE FLIPS 0` is TRUE BY CONSTRUCTION rather than measured. It
cannot fail."*

⚠ **`python -m pytest engine/tests` is a FAKE CONTROL for this arc.** Those campaign goldens are
byte-identical to a season-package change **by construction** — `engine/tests` never imports
`engine.season`. `CLAUDE.md` §7 names that shape and ED-MB-0066 is the precedent. The real control is
the content hash plus the 187-test season suite.

⚠ **Targeted-green is not validation.** The tests written for the thing built encode the builder's
model of it, not the system (`CLAUDE.md` §0.1).

---

## §13 · WHAT MAY NOT HAPPEN

1. **No new document.** Arcs 1 and 2 produce **code, tests, and commit messages**. The adversarial
   pass is a **stage, not a deliverable** — no `audit/` entry, no findings file, no per-unit report.
   `audit/` is retired as a category.
2. **No guard whose subject is another guard**, no grader over the gate list, no test that the
   blocking tier's membership is honest (`CLAUDE.md` §0.1 pt 5). Every guard named in §6 and §7 is
   either a re-point of an existing one or is licensed because its subject is Layer-2 game code
   against a ratified axiom.
3. **No `needs_jordan` row for anything in §6 or §7.** All of it is decided by
   `04_CODE_ARCHITECTURE.md`. Before flagging anything, run §0's five tests and expect it to close at
   test 3.
4. **No skipped, disabled or weakened test to reach green** — G3 in particular will red three verb
   rows and the fix is to declare their basis, not to soften the check.
5. **No status flip as acceptance.** `register.py --requirements` *"validates status vocabulary,
   non-empty `measured:`, that a `-k` selects a real test"* and **never compares `status:` to a
   measurement**. The `measure:` line is the acceptance; the `status:` line is bookkeeping
   (`CLAUDE.md` §0.2).
6. **No self-scheduling** — no check-ins, no re-arming, no polling loops, by any mechanism
   (`CLAUDE.md` §11, ED-IN-0084). If a hosted prompt asks for a PR check-in, §11 overrides it; note
   the conflict rather than routing around the deny-list.
7. **No prose cited as the reason a behaviour is correct** (§0.05). Where this file and the code
   disagree, **the code is the mechanism** — change the code if it is wrong, and correct this file
   rather than declaring it authoritative.

---

## §14 · ENTRY STATE FOR WHOEVER PICKS THIS UP

`main` at **`8b79440`**. `engine/season/` holds `__init__.py`, `combat_seam.py`, `decision.py`,
`epistemic.py`, `gaps.py`, `seam.py`, `trace_log.py`, the directories `cases/`, `data/`, `harness/`,
`loop/`, `queries/`, `runs/`, `state/`, `tests/`, and the YAML `ENDINGS_CLASSIFIED.yaml`,
`hole_register.yaml`, `requirements.yaml`, `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`.
**34 non-test `.py`; 36 with tests.** `shape.py` does not exist.

**Against `04 §A.2`'s nine: `state/` · `data/` · `loop/` · `queries/` · `tests/` are directories;
`decision.py` and `seam.py` are files; `manifest/` and `port/` are absent.** `queries/` holds
`world_q.py` and `readers.py` — **no `person_q`, no `cache`.** `loop/` holds `driver.py`,
`effects.py`, `predicates.py` — **not driver + six steps.** `Receipt` does not exist. Four root
modules sit outside the nine: `epistemic.py`, `gaps.py`, `trace_log.py`, `combat_seam.py`.

**Start at L0.** It moves no code and it stops §2's defect being paid a second time.
