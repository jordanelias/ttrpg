# LAYER-1 CONFORMANCE, THEN THE GATE, THEN THE R-WORK — EXECUTION PLAN

## Status: **PROPOSED. REFERENCE under `CLAUDE.md` §0.05 — delete this file and the game behaves identically.** Nothing here may be cited as the reason a behaviour is correct. It ratifies no design call; the one call it *records* was ruled by Jordan and is filed in `registers/editorial_ledger_sc.jsonl`.
## Lane: IN. ED-IN-0206 (the Layer-1 gap this closes) · ED-SC-0037 (ruled, see §4) · ED-IN-0203 (the decomposition it inherits).

> **What produced this.** A read-only assessment of PRs **#383**, **#384** and **#385** against the
> working tree at `8b79440`, with every execution claim re-run rather than read. The instrument
> outputs are §1. Where a merged commit's prose is wrong about the tree, §2 and §3 say so with the
> command that shows it.
>
> ⚠ **TIER DRIFT, DECLARED.** Jordan assigned this node to **Fable 5.1** (§10's planner/audit tier).
> `get_session` reports `configured_model` and `last_served_model` both `claude-opus-5`, effort
> `xhigh`, so the assessment and this plan were produced on **Opus 5**. Recorded because §10 makes the
> tier part of the method: **§9's review gates name `model: "fable"` and the Agent tool honours it, so
> the reviews asked for are reachable even though this planning node was not** — §15 is one. A later
> session must not read this document as a Fable product.

---

## §0 · WHAT THIS IS, AND WHAT IT IS NOT

**It is not a second R-plan.** `workplans/2026-09-09-r-execution-plan.md` is the single owner of the
nine R-rows, their dependency graph, and units U1–U10. This document **cites it and does not restate
it** — the de-duplication ruling #384 applied to its own U0 binds here (`CLAUDE.md` §8, *every rule
lives once*). What is here is only what that document does not have: the assessment of what the three
PRs left on `main` (§1–§3), Jordan's ruling (§4), the two arcs that must precede U1 (§5–§7), the
handoff to whoever runs Arc 3 (§8), and the method and fix-on-error rule binding every unit (§9–§10).

**Everything in §6 and §7 is engineering against a written spec.** `04_CODE_ARCHITECTURE.md` is
RATIFIED (ED-IN-0204) and already decided every item. **No unit here is an escalation** — §0's five
tests close all of them at test 3.

---

## §1 · THE ASSESSMENT — every execution claim re-run, not read

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
  Reproduce: `git log --format='%h %ci %s' -6`. ⚠ This checkout is **shallow**, so a reader who cannot
  see those commits cannot check this and must not treat it as verified from the tree.
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
| §C.2 F3: AX-4 clause 2 — `kind is Tenure ⇒ actor == subject(id)` … *"otherwise raise `NotYours`"*, and `via` MUST be present for T-o | **no `actor`, no `via`, no `NotYours`** (grep → 0 engine-wide; the one `actor` hit at `state/world.py:377` is a string inside a `raise`). ⚠ The gate does carry two PARTIAL who-wrote-it discriminators — `driver: str` (`:296`, checked at `:352`/`:362`/`:373`) and `subject:` (`:300`) — so this is a missing OWNERSHIP check, not a missing attribution channel | grep + read |
| §C.2 F9: `before == after ⇒ raise NoOpReceipt` | absent | grep, 0 hits |
| §A.3 row 6 (`04:175`) and `04:402`: *"**no `subject`.** `changes[]` are gate receipts; place is a Query"* / *"No `actor`, no `target`, no `subject` on `Event` — STRUCTURAL: the fields do not exist"* | **`Event.subject : str` EXISTS** (`state/carriers.py:81`) and `test_season_shape.py:684` pins it INTO the field set by exact equality. ⚠ The carrier's own docstring names three absent fields and `subject` is **not** among them — the code and `04` disagree about which three | read both |

**And AX-4 clause 2 cannot be built without `Act.via`, which is `H-108` and is separately R-04's
hard blocker** (R-plan §4). One unit closes both. That is the reason Arc 2 is worth its cost rather
than being deferred into the R-units: `04` PART E puts the gate at **step 3**, ahead of RESOLVE
(step 6) and ahead of step 8, *"THE BAR"*.

### §3.2 · Overcounted — item (2) contradicts `04 §A.2:133` for two of its four symbols

ED-IN-0206 item (2) reads: *"`queries/person_q` DOES NOT EXIST. §A.1's AX-2 row assigns the
person-side family to `queries/person_q` [vs `queries/world_q`]; step 7 put
budget/opening_set/assemble/entrenchment in `decision.py` instead."* (The bracketed clause is in the
row and was dropped from a first quotation of it without an ellipsis.)

**`04 §A.2:133` names two of those four as `decision/`'s own members:** *"`decision/` AX-2's
island: questions · **opening_set** · choose · **budget**. NO World in scope."* So moving them to
`queries/person_q` on ED-IN-0206's wording would break conformance rather than restore it.
⚠ **And `04` is itself ambiguous on `budget`, so do not resolve that one by assertion either:**
`:133` lists it as a `decision/` MEMBER while the `§A.2` table's `decision/` row lists `budget` in
the **may read** column. `decision.py::budget(p, v, k, fx)` takes person-side inputs only, so
`person_q`'s *"`PersonInterior` snapshot only"* test does not exclude it. **Name the ambiguity in
L3's table and pick with the reason stated; do not report a clean read of a row that has two.** `§A.1`'s AX-2 row governs the **Query
families**, not `decision/`'s named members; `§A.2`'s table gives `queries/person_q` *"owns nothing
… may read a `PersonInterior` snapshot only"*.

**L3 is therefore an adjudication unit, not a move unit** (§6). Per symbol, against `§A.2:133` and
the `§A.2` table, decide `decision/` versus `queries/person_q` and record the reason at the site.
`assemble` (question assembly) reads as `decision/`; `entrenchment` reads as `person_q`; **both are
to be argued from the spec rows, not assumed from this sentence.**

### §3.3 · The stale continuity surface, which is a Layer-0 defect

`registers/handoffs/HANDOFF_IN.md`'s **top two sections** both read
`⏳ PRODUCED 2026-09-09, NOT YET COMMITTED` — for decomposition **step 8** and **step 7**. Both
merged in #383. ✔ **CORRECTED in this document's own commit**, which is why the headers now read
`⭐ DONE … MERGED IN PR #383`; recorded here as what the assessment found, not as outstanding work. `CLAUDE.md` §1 names this file as one of two continuity surfaces a cold session
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
  **net**, which the one ladder reads: `dice_engine.degree_from_net(net, ob, …)` computes
  `margin = net - ob` **inside** itself. §C.5's *"a subsystem returning a winner has not met the
  contract"* holds — nothing here returns a winner. ⚠ **But the `Margin` TYPE and the `veto`
  parameter are NOT closed by this ruling, and a first writing of this section implied they were.**
  §C.5 spells `provider.run(...) -> Margin` and `ladder.degree(margin, veto=provider.veto)`; the
  live seam grades a `{"net", "ob"}` dict and `degree_from_net` has no `veto`. **The R-plan already
  names both as declared deviations** — §7's *"FOLLOWED IN CONTRACT AND NOT IN TYPE"* and its veto
  gap — and §8 of this document says everything else in the R-plan stands, so **those deviations
  stand too.** They are U1's to carry as declared, not this ruling's to close.
- ⚠ **IT DOES NOT ANSWER OPTION A'S COST, AND A FIRST WRITING SAID IT DID.** That claim was
  *"`sigma_leverage` already owns the obstacle model — `eff_ob`, `effective_ob`,
  `sigma_space_ob_shift`"*, and **all three CONSUME an obstacle; none produces one.**
  `eff_ob(base_ob, pool, net_sigma)` takes `base_ob` as an argument and its docstring opens *"DISPLAY
  ONLY (not the resolution value)"*; `effective_ob` is an argument-order alias; `sigma_space_ob_shift`
  is `net_sigma * sigma_n(pool)` and names no obstacle. **So ED-SC-0037's cost is CARRIED, not
  dissolved:** the obstacle still comes from the wrapper — R-plan §7's Operands section specifies
  `act.obstacle` else `score/2` else `fx["obstacle_default"]` and **already registers itself as an nth
  site in a family the tree records as disagreeing.** U1 declares the clause-(3) tension `interim` and
  repoints when proceedings lands. **What the ruling buys is single ownership of the two things
  genuinely open:** the roll's producer, and the ladder that reads it.
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

⚠ **ARC 3 IS A DIFFERENT SESSION'S WORK (Jordan-directed, 2026-09-10).** Arcs 1-2 are this document's;
**Arc 3 and §8's amendments belong to the session that owns it**, so §8 is a HANDOFF, not a task list
for whoever executes L0-G4. Two consequences, because a split across sessions is where §12's invariants
get dropped:

- **The Arc 3 session inherits G3, not a duplicate of it** (§8 amendment 5). Do not land `Act.via` or
  the gate's Tenure branch twice.
- **Arc 3 starting before Arcs 1-2 finish means U1 lands `manifest/` and the provider into a
  `seam.py` that has to become `seam/` anyway** — the second payment of §2's defect, which is the
  reason these arcs are ordered at all. If the two run concurrently, the Arc 3 session needs
  `isolation: "worktree"` and L2 + L4 must land first.

**Zero game yield is the expected result of Arcs 1 and 2 and is not a failure** (`CLAUDE.md` §0.2).
**The control for that is §12's — the content hash, `PROBE FLIPS 0`, and the 187-test season suite.**
⚠ `register.py --requirements` is **NOT** the control, and a first writing of this section offered it
as one. §13 item 5 says why in this document's own words: that command never compares `status:` to a
measurement, so its 6/3 is hand-edited YAML and **cannot move unless somebody edits the file.** A
doc-derived count offered as evidence is §0.05's own worked example of a non-mechanism. It is kept
only as a **tripwire that nobody edited the board**, which is a different and much smaller claim.
**A unit in Arc 1 or 2 that moves the hash or a probe verdict has done something it was not asked to
do — revert it and say so.**

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

**Artifact — CORRECTED DURING EXECUTION.** A first writing demanded
`rg -n "does \*\*not\*\* move" …v2.md` → **0**. Wrong artifact: this repo's idiom, used throughout
#383, is to **quote the struck claim and refute it**, since a reader who meets only the correction
cannot tell what was corrected — deleting the words to satisfy a grep makes the document worse to pass
a check. **The artifact is: every struck placement directive sits inside a `⚠ SUPERSEDED` block naming
its replacement `04` line and its repair unit, and the Status header carries the same warning.**
`rg -c SUPERSEDED …v2.md` → 3.
**Tier:** `haiku` for the edit, `sonnet` to verify the two files agree afterwards.

### L1 · `decision.py` → `decision/` — the one unit with a spec-mandated *first commit*

`04:1046`: *"`decision/` is a directory from its first commit. The isolation scan matches by path, so
a `choose` drafted inside `loop/` and moved later would have been green while violating AX-2."*

- `engine/season/decision.py` becomes `engine/season/decision/` with `__init__.py` re-exporting its
  public names. **Split by §A.2:133's four members** — `questions`, `opening_set`, `choose`,
  `budget` — not by line count.

⚠ **AND THE SPLIT RE-CREATES STEP 7's SILENT REBIND HAZARD VERBATIM, ONE LEVEL DOWN. THIS IS THE
UNIT'S LARGEST RISK AND A FIRST WRITING OF IT NAMED NOTHING.** Three names are read **bare** inside
`decision.py` and rebound from **outside** as package attributes:

| bare reader | the name it resolves in module globals |
|---|---|
| `decision.py:236` — inside `opening_set` | `belief_contradicts` |
| `decision.py:273` — inside `align` | `ALIGNMENT` |
| `decision.py:354` — inside `make_chooser` | `pack_scenes` |

**28 rebind lines across six files** reach these by package attribute
(`rg 'decision\.(ALIGNMENT|belief_contradicts|pack_scenes)\s*=|PS\.(ALIGNMENT|belief_contradicts|pack_scenes)'`):
`engine/season/tests/test_season_shape.py`, and `sweep_core.py`'s `from engine.season import decision
as PS` feeding `wd_acceptance.py`, `arm7_flexibility.py`, `arm9_forking.py`, `arm9_subj.py`.
**Put `opening_set` in `decision/opening_set.py` — which "split by the four members" instructs — and
`belief_contradicts` resolves in THAT submodule's globals, so every `decision.X = …` on the package
becomes a no-op.** `decision.py:50-60`'s own header records the hazard and ED-IN-0203 records the
consequence: **the suite arm goes RED with `shipped=[]` (loud), and the degree-sweep arms report every
branch identical — a FABRICATED NULL (silent)**, which §0.1 pt 4 calls the worse of the two
directions.

**L1 must therefore state one of two dispositions, explicitly:** (i) the three readers and the three
names stay in **one** submodule together, named — or (ii) **all 28 rebind lines are re-pointed at the
submodule the reader actually lives in, in the same commit**, read-captures included, with
ED-IN-0203's **unaliased** `from .x import belief_contradicts` mutation re-run as the falsifier.
⚠ Re-pointing only the assignments and not the read-captures is the exact defect step 7 almost
shipped: `saved = PS.ALIGNMENT` reads the package while the write lands on the submodule, so the
`finally:` restore puts a stale value into a module that never held it **and the test still passes.**
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
- `combat_seam.py` → `seam/wrappers/combat.py`. ⚠ **D5's own spelling is superseded here:** the
  R-plan gives the new offender as `season/seam/combat_seam.py`, and `04:135` / the `§A.2` table's
  `seam/wrappers/*` row put a wrapper **under `wrappers/`**. Say so rather than silently differing.
- **Co-edits in the same commit:** `PATH_SEAM_ALLOWED`
  (`tests/valoria/test_engine_does_not_import_systems.py:220`) member `season/combat_seam.py` →
  `season/seam/wrappers/combat.py`; `files.COMBAT_SEAM_PY` (`engine/season/data/files.py:138`); and
  **the three relative-import depths at `combat_seam.py:70-72`** — `from .data import files`,
  `from .decision import body_band_penalty`, `from .state.ids import H` all gain a level.
  ⚠ **`_PC` is NOT one of them, and a first writing of this unit said it was.** `_PC =
  files.PC_ENGINE_DIR` — a module constant — and the comment directly above it says it *used to*
  climb four `parents[...]` levels and deliberately no longer does, precisely so the file can move.
  Getting that backwards would have sent a session to fix the one line the tree already fixed.
- **`test_the_one_declared_path_seam_is_still_the_only_one` (`:395`) asserts exact set equality
  (`:424`).** A rename inside a shrink-only set is not a widening. **The set must not gain a member.**
- ⚠ **AND IT MUST NOT LOSE ONE EITHER, WHICH IS THE SUBTLER HALF.** That test finds the seam through
  `_relative_module_files`, whose docstring is explicit — *"Relative imports only, and one hop
  only"* — and which skips any `ImportFrom` with `node.level == 0`. **Write the moved wrapper's
  import absolute and the scan stops seeing the seam at all:** `offenders` shrinks to
  `{cross_scale/combat_bridge.py}` and the equality assertion goes RED with a message ending
  *"Removing one? Delete it from PATH_SEAM_ALLOWED"* — **an invitation to narrow the declared set
  while the seam still exists.** Repair by restoring the relative import, never by deleting the entry.

**Falsifiers:**
```
a  move combat.py, leave PATH_SEAM_ALLOWED  -> :395 RED naming both spellings
b  re-export _LADDER through seam/__init__  -> test_we_the_ladder_is_the_trees_own... RED
   (the read-capture at test:8104 must be re-pointed to seam.ladder regardless -- AttributeError,
    loud -- so b tests the SNAPSHOT hazard, not the rename)
c  rg -c '^_LADDER_ERROR' engine/season/seam/ladder.py -> 1, everywhere else -> 0
d  write the moved wrapper's import ABSOLUTE -> :395 RED reporting the wrapper as NOT an offender.
   Repair by restoring the relative import. Deleting the PATH_SEAM_ALLOWED entry also goes green
   and is the wrong fix -- that is what makes this arm worth running.
```

### L3 · `queries/person_q` + `queries/cache` — ADJUDICATE, then move (∥ with L4)

**Read §3.2 first.** This unit's deliverable is **a per-symbol placement decision argued from
`04 §A.2:133` and the `§A.2` table, with the reason recorded at each site** — not the literal
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

**Falsifier — the unit had none, and it earns one.** `04:171` (§A.3 row 2) requires that *"the second
cannot import the first"*, and **no scan anywhere in the tree enforces it**: L3 moves symbols into
`person_q` with nothing stopping `person_q` importing `world_q` the next day. Add the import scan —
`person_q` may not import `world_q`, `state/`, or `loop/` — and prove it: plant
`from .world_q import presence` in `person_q` → RED, revert → GREEN, with a floor so it cannot pass by
resolving nothing. **It earns its place under §0.1 pt 5**: `queries/` is Layer-2 game code and the
axiom is ratified. Without it L3 satisfies `§A.2`'s *file list* and not `§A.3`'s *property*.

### L4 · `manifest/` — role → provider rows, resolved at boot (∥ with L3)

`§A.1:125` (Stage 2 §D.4), `§A.2:136`, and `04:1031`'s build step 10: *"a misspelled manifest row
fails at boot naming the row."* #384's Layer-1 correction already moved the provider registry here
from the `seam/providers.py` the planner proposed — **honour that; do not re-propose `seam/providers`.**

⚠ **THREE ROLE→PROVIDER PRIMITIVES ALREADY EXIST AND A FIRST WRITING NAMED NONE — so as written this
unit minted a fourth.** Read all three first:

| existing | what it already does |
|---|---|
| `state/world.py:166` `self.manifest: dict[str, str]` — its own comment reads *"role -> provider, resolved AT BOOT"* | and `world.py:573-576`'s `boot()` **already raises `NoProducer` naming the missing role**, already pinned by `test_season_shape.py:793` |
| `seam.py:94-129` `contest_subsystem()` | resolves prize → module through `rosters.yaml: contest_subsystems` + `references/module_contracts.yaml` — **at first call, not at boot** |
| `engine/substrate/composition.py:38` `ROLES` | the seam `CLAUDE.md` §3 names as where `engine/` resolves a ROLE to a MODULE |

**So L4's deliverable is a CONSOLIDATION, not a new mechanism**, and the unit must say **which of the
three it composes on and which it retires.** `2026-09-06-shape-decomposition-plan.md:249-252` already
proposed re-basing `World.boot` on `composition.ROLES` and deleting `World.manifest` — read that
before choosing. `manifest.resolve("contest", prizes[prize])` is the call §C.5 spells; land the
**signature and the boot-time failure** by moving what exists, and land **no provider row yet** — the
row is U1's, and its value is §4's `sigma_leverage`.

**Falsifier:** a misspelled role in the data file **fails at load naming the row**, and passes when
corrected. **A misspelling that fails at first call rather than at boot has not met §D.4** — which is
exactly the gap between `World.boot` (boot) and `contest_subsystem` (first call) today.

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

⚠ **THE SILENT NARROWING THIS UNIT CAUSES, WHICH A FIRST WRITING DID NOT NAME.**
`test_w2_every_write_call_site_names_a_pair_on_the_matrix` (`test_season_shape.py:1766`) walks
`_write_call_sites(files.DRIVER_PY, files.PROBES_PY)` — **two FIXED paths** — and its only non-vacuity
floor is `assert pairs`. Move the `witness` / `matter` / `census` / `calendar` bodies into six step
modules and **their `w.write(` sites leave the scanned corpus**, while `probes.py`'s ~20 sites satisfy
`assert pairs` on their own: **the gate goes green over an unknown number of unchecked writes.**
ED-IN-0203 recorded this exact mechanism when it struck the deposit-body extraction — *"witness holds
3 of shape.py's 12 write call sites while test_w2 reads files.SHAPE_PY by fixed path, so the
extraction would have shrunk that gate's corpus silently."* **This is the fourth recurrence of the
same defect** (steps 2, 4, 5, now). **L5 re-points the scan at every module under `loop/` plus
`PROBES_PY`, and pins that the literal-pair set after the move is a SUPERSET of the set before it** —
a count is not enough, since a lost pair and a gained pair cancel.

⚠ **The `A39` spy moves with its subject, and the plan's own §9 rule 4 is why this is listed.**
`probes.py:2482-2487` does `from ..loop import driver as _s; _s.contest = spy`, which works only
because `loop/driver.py:64-67` binds `contest` in driver's globals and `resolve()` calls it **bare**.
Move `resolve`'s body to `loop/resolve.py` and the spy is a no-op, `captured` comes back empty, and
the probe grades INSTRUMENT-ERROR → a probe flip. `delta.py` catches it (loud), but both
`2026-09-09-shape-decomposition-plan-v2.md` and `HANDOFF_IN.md` had already named it.

⚠ **Five further `getsource` readers go RED on this move** — `test_season_shape.py:640`, `:661`
(`SeasonDriver.resolve`) and `:695`, `:1115`, `:2651` (`SeasonDriver.deliberate`). **All are positive
assertions, so all are loud**, and they are listed only so the unit's bill is not read as three tests.

⚠ **The three `inspect.getsource(SeasonDriver.witness)` readers are the ones that need care**
(`test_season_shape.py:183` `test_d2`, `:363` `test_d9b`'s eviction comparator string, and `:764`
`test_witness_writes_no_belief_and_no_conviction`, a **pure NEGATIVE assertion** that keeps passing
while silently vacating its subject). #383 struck the deposit-body extraction for exactly this reason.
**Re-point all three at the moved function by `getsource`, and prove the negative one live by planting
a belief write and watching it go RED.** A negative assertion not proven by a plant has not been
re-pointed, only relocated.

---

## §7 · ARC 2 — THE GATE CONTRACT

Order is forced: `Receipt` before the token — `04:538`'s `minted[t]` is **the gate's** per-tick set
of minted receipt ids (`04:407`), not a set hanging off the token, and `log.append` asserts against it,
so the receipt has to exist before anything mints into it — then the token before AX-4 clause 2 (the
check reads the token's write class), and `NoOpReceipt` last because it is the one clause that changes
an existing write's outcome.

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

⚠ **IT IS ONE TOKEN TYPE, NOT FOUR, AND A FIRST WRITING SAID FOUR.** `04:198-199`:
`WriteClass := { CALENDAR, MATTER, ACTS, INTERIOR }` and `Token := (write_class, tick)` —
*"constructed by loop/driver and NOWHERE ELSE"*. **One type carrying a write class and a tick; four
VALUES.** `§A.2`'s *"mints all four"* counts values. Getting this wrong builds four classes where the
spec wants one and calls it conformance.

`loop/deliberate` and every `seam/wrappers/*` receive **no token** — which is what makes §C.5's *"a
state write from inside — no token, STRUCTURAL"* true by construction rather than by convention.

⚠ **THE FALSIFIER IS A SCAN, AND A FIRST WRITING OF IT CLAIMED A RUNTIME FAILURE PYTHON CANNOT
PRODUCE.** It read: *"a step constructing its own token must be unable to."* **In Python it can** —
there are no private constructors, which is why `04:206` grades this invariant **MECHANICAL, not
STRUCTURAL**, and names the instrument: *"a test asserts `Token(` appears in `loop/driver` only"*. A
falsifier that predicts an exception here would come back GREEN and be read as the hazard being
overstated — step 6's lesson, one level down. **So:**
```
the guard    an AST scan for `Token(` construction over every *.py under engine/season/
             EXCEPT loop/driver.py -- scope stated so it cannot narrow when a file moves
falsifier a  plant `Token(WriteClass.ACTS, w.tick)` in loop/deliberate.py  -> scan RED
falsifier b  a wrapper or deliberate calling gate.write                   -> fails FOR WANT OF A
             TOKEN (a TypeError on the missing argument), not for want of a matrix row -- that
             distinction is the unit's whole content, so assert on WHICH error
```

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

⚠ **AND IT COLLIDES WITH R-PLAN U9, WHICH SPECIFIES THE SAME TWO THINGS.** U9's Files list gives
`state/carriers.py::Act` gaining `via: Optional[str] = None` **and** `state/world.py::write` gaining
AX-4 clause 2's Tenure branch with `via` required for `T-o` — **not just the field, the whole
branch.** Landed twice, the second lands on the first. **G3 owns both**, and the reason is an
engineering one rather than a preference (§0 test 5): `04` PART E puts the gate at **step 3**, ahead of
RESOLVE at 6 and THE BAR at 8, whereas U9 is R-04 and sits late in the R arc — so deferring to U9
leaves the gate unenforced through the entire arc. §8 gains **amendment 5** so the Arc 3 session
inherits this rather than re-deriving it.

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

⚠ **AND `04` IS IN TENSION WITH ITSELF HERE, SO G4 MUST SAY HOW IT RESOLVES IT RATHER THAN PICKING
SILENTLY.** `04:537` spells the clause as `raise NoOpReceipt`, while `04:668` says of the fold *"a
refusal emits, never raises — no `raise` path after eligibility."* A raise from inside the fold is a
corpus crash, not a refusal. **G4 converts it at the fold boundary — the gate raises, `resolve` catches
and emits the refusal the verb row declares — and the commit states that reading with both lines
cited.** This is Layer 1's own internal tension, not a question for Jordan: §0's test 5 gives it an
obvious engineering answer, and the alternative (a raise reaching the corpus) contradicts a ratified
sentence.

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
   builds, with `dice_engine.degree_from_net` as the ladder — the roll's producer and the ladder each
   in single ownership. ⚠ **The obstacle is NOT** — see §4; U1 carries §7's Operands site and declares
   it `interim` against ED-SC-0033 clause (3). The `Margin` type and `veto` remain §7's declared
   deviations.
5. **U9 drops `Act.via` and the gate's AX-4 clause-2 Tenure branch, and cites G3 instead.** U9's Files
   list currently specifies both, which G3 lands first for the ordering reason in §7 — `04` PART E puts
   the gate at step 3, ahead of RESOLVE and THE BAR. **Two sessions landing one schema change is how a
   split arc pays twice.**

**Everything else in the R-plan stands**, including its §2 corrections, its §4 dependency graph, its
§7 roll placement, its §9 guard-blinding handling and its §10 non-goals. **Do not re-derive the
graph. Do not re-audit its ~190 citations.** It was verified once and the verification is its §1.

⚠ **AND THE ONE PIECE OF CLEAN-UP THIS SECTION ORIGINALLY ASSIGNED TO ARC 3 IS ALREADY DONE.** A
first writing said *"`requirements.yaml` carries 11 stale `shape.py:NNNN` citations … all 11 are
dangling"*, inherited from #384, which was right when it wrote it. **Measured now:
`rg 'shape\.py:[0-9]' engine/season/requirements.yaml` returns 0** — #383's step-10 prose half
converted them, and the single surviving `shape.` mention (`:165`) is a note recording that a
citation *used to* read `shape.py:2289`. **Arc 3 has nothing to convert here.** Kept as a correction
rather than deleted, because a later session reading #384's body will meet the 11 again.

---

## §9 · THE METHOD — AGONIST → ANTAGONIST, BINDING ON EVERY UNIT

**`CLAUDE.md` §10 owns the mechanics** — a relay not a dialogue, and independence made structural by
`.claude/agents/valoria-critic.md`'s `tools: Read, Grep, Glob`. Read it there rather than here; a first
writing restated both paragraphs. **The one thing worth adding is what the critic is handed:** its
**output**, never its reasoning. That is not a formality — the Fable pass on THIS document overturned
four claims in it, and it could do that because it was rebuilding the reasoning from the tree instead
of checking the producer's.

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
4. **A selector is only as good as the paths you point it at.** Four failures in the #383/#384 arc were
   **a sufficient check reported as an exhaustive one**: *"no code opens these docs"* (grepped inline
   `open(...)`, missed a module constant), *"nothing else spells Layer"* (did not grep), *"exactly three
   programmatic readers"* (grepped three directories, missed `engine/season/`), *"eleven home claims"*
   (matched the literal `shape.py`, missed the dominant `shape.<symbol>` spelling). **State the scope of
   every count in the sentence that reports it**, and resolve names with `ast`, never by counting text —
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
| `INVENTED_VERBS` cited as a live symbol that exists nowhere in the tree | `engine/season/hole_register.yaml:750`, inside a `cite:` that already says so. ⚠ `rg INVENTED_VERBS` returns **1**, not 0 — that mention — so a session checking the claim by grep must read the hit before believing either number | delete the stale clause in whichever unit next touches that row |
| ~~`HANDOFF_IN.md`'s two `NOT YET COMMITTED` sections~~ | `registers/handoffs/HANDOFF_IN.md:3`, `:187` | ✔ **DONE** in this document's own commit — not L0's. Row kept so it is not re-opened |
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

**Before fanning out, read `CLAUDE.md` §10's three caching facts** — the Haiku floor, the shared-prefix
race, model-switch invalidation. Restated here in full in a first writing, cited now (§8). Only the
third binds this plan's shape, which is why escalation happens at **arc** boundaries.

**Parallel write lanes need `isolation: "worktree"`** — one repo, colliding trees otherwise — and
return **fixed-format summaries**, not raw context. Only L3 ∥ L4 are parallel here.

---

## §12 · THE STANDING INSTRUMENT SET — run after EVERY unit, in this order

> **Owner: `ED-IN-0203`'s `MEASURED-BY` field and `engine/season/__init__.py`.** Reproduced as a
> checklist with this session's measured values, because a bare pointer is what gets skipped. Where
> this and those owners disagree, they win.

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

**Expected values are §1's table, measured on `8b79440` this session** — hash
`ee0383bf3f4606e56b80cd07c0284f0a`, a clean `git status` after `report`, `PROBE FLIPS 0` at 122 probes
and 66 gap events, 187 season tests, 1,776/2 on `tests/valoria`, 6 `not_met` / 3 `partial`, all local
gates passed. **A unit returning otherwise has broken something rather than revealed a miscount.**

⚠ **`report` BEFORE `delta`, always.** `delta.py:8-12`: *"THIS COMPARISON IS VACUOUS UNLESS YOU
REGENERATE `results.json` FIRST … `PROBE FLIPS 0` is TRUE BY CONSTRUCTION rather than measured. It
cannot fail."*

⚠ **`python -m pytest engine/tests` is a FAKE CONTROL for this arc.** Those campaign goldens are
byte-identical to a season-package change **by construction** — `engine/tests` never imports
`engine.season`. `CLAUDE.md` §7 names that shape and ED-MB-0066 is the precedent. The real control is
the content hash plus the 187-test season suite.

⚠ **Targeted-green is not validation** (`CLAUDE.md` §0.1).

---

## §13 · WHAT MAY NOT HAPPEN

> **Every item is `CLAUDE.md`'s** — §0, §0.05, §0.1 pt 5, §0.2, §11 — reproduced **with its failure
> clause** rather than cited bare: a deliberate §8 exception, on the reasoning `CLAUDE.md`'s own rewrite
> gave for missing its size target. With no context between sessions, the clause naming what goes wrong
> is what stops the rule being re-litigated. §9's and §11's restatements were cut; these are kept, and
> the reason is stated rather than assumed.

1. **No new document.** Arcs 1 and 2 produce **code, tests, and commit messages**. The adversarial
   pass is a **stage, not a deliverable** — no `audit/` entry, no findings file, no per-unit report.
   `audit/` is retired as a category.
2. **No guard whose subject is another guard**, no grader over the gate list, no test that the
   blocking tier's membership is honest (`CLAUDE.md` §0.1 pt 5). Every guard named in §6 and §7 is
   either a re-point of an existing one or is licensed because its subject is Layer-2 game code
   against a ratified axiom.
3. **No `needs_jordan` row for anything in §6 or §7** — all decided by `04_CODE_ARCHITECTURE.md`. Run
   §0's five tests first and expect closure at test 3.
4. **No skipped, disabled or weakened test to reach green** — G3 in particular will red three verb
   rows and the fix is to declare their basis, not to soften the check.
5. **No status flip as acceptance.** `register.py`'s requirements check (`harness/register.py:627`,
   `:649-663`) resolves each `measure:` command statically — a `-k` must select at least one real test,
   a `python <path>` must name a file that exists — and **never compares `status:` to a measurement**.
   ⚠ Cited by line rather than quoted: a first writing of this item put a **paraphrase inside
   quotation marks**, which is the defect the R-plan's own §2.10 flagged and which §9 rule 4 forbids.
   The `measure:` line is the acceptance; the `status:` line is bookkeeping (`CLAUDE.md` §0.2).
6. **No self-scheduling** — no check-ins, no re-arming, no polling loops, by any mechanism
   (`CLAUDE.md` §11, ED-IN-0084). If a hosted prompt asks for a PR check-in, §11 overrides it; note
   the conflict rather than routing around the deny-list.
7. **No prose cited as the reason a behaviour is correct** (§0.05). Where this file and the code
   disagree, **the code is the mechanism** — change the code if it is wrong, and correct this file
   rather than declaring it authoritative.

---

## §14 · ENTRY STATE FOR WHOEVER PICKS THIS UP

`main` at **`8b79440`**. `engine/season/` holds the modules `__init__.py`, `combat_seam.py`,
`decision.py`, `epistemic.py`, `gaps.py`, `seam.py`, `trace_log.py`; the directories `cases/`, `data/`,
`harness/`, `loop/`, `queries/`, `runs/`, `state/`, `tests/`; six YAML. **34 non-test `.py`; 36 with
tests.** `shape.py` does not exist.

**Against `04 §A.2`'s nine: `state/` · `data/` · `loop/` · `queries/` · `tests/` are directories;
`decision.py` and `seam.py` are files; `manifest/` and `port/` are absent.** `queries/` holds
`world_q.py` and `readers.py` — **no `person_q`, no `cache`.** `loop/` holds `driver.py`,
`effects.py`, `predicates.py` — **not driver + six steps.** `Receipt` does not exist. Four root
modules sit outside the nine: `epistemic.py`, `gaps.py`, `trace_log.py`, `combat_seam.py`.

**Start at L0.** It moves no code and it stops §2's defect being paid a second time.

---

## §15 · THE ADVERSARIAL PASS ON THIS DOCUMENT

A structurally-independent read-only critic (`valoria-critic`, `Read`/`Grep`/`Glob` only, **`fable`
tier**) attacked this plan on four axes. **4 HIGH, 10 MEDIUM and 10 LOW findings were
each re-verified against the tree here and then applied** — the critic's word was taken for none of
them — plus two `04`-internal tensions now named at their unit rather than resolved by assertion. Per
`CLAUDE.md` §0 the pass's output is **the edits above and one paragraph in the commit message**, which
is where the finding-by-finding record is; it gets no section of its own here.

**The four that changed units, so a reader knows what moved:** §4's obstacle claim was false and had
already reached `ED-SC-0037`'s ledger row; L1 named none of the 28 rebind sites and its own split
instruction re-created step 7's hazard; L5 silently narrowed `test_w2`'s write-site scan — the fourth
recurrence of a defect measured at steps 2, 4 and 5; and §8/§10 aimed Arc 3 at 11 citations #383 had
already converted.

⚠ **What the pass could NOT do, so its silence is not read as agreement:** no execution tools, so
**not one number in §1 or §12 was reproduced by it** — those rest on this session alone — and it could
not check §2's merge times, this checkout being shallow.
