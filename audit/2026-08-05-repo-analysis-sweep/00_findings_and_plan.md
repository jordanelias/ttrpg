# Repo analysis sweep — findings register + remediation plan

## Status: ANALYSIS + PARTIAL EXECUTION (ED-IN-0147, 2026-08-05). Four items HELD for Jordan (§4).

**Method.** Six read-only Fable-5 lenses (pointers/indices, centralized values + Keys, import graph,
tools/gates/CI, registers, doc organization) → one Opus-5 adversarial critic that received the
*claims only*, never the producers' reasoning → one Sonnet-5 control that re-derived every published
number independently. Tiering per CLAUDE.md §10: Fable on read-only audit, Opus on the verify/judge
node, Sonnet on mechanical execution and counting.

**The headline is that the checking worked.** The critic REFUTED or REFRAMED **four of six**
load-bearing claims, and the count control corrected **three of eight** published numbers. Both sets
of corrections are recorded below at equal prominence to the findings, per §0.1 point 4 — a sweep that
reports only what it found, and not what it got wrong, is not a measurement.

---

## 1. What the shipping gate cannot see

`pytest tests/valoria` = **1637 passed, 23 skipped, 14 xfailed, 1 xpassed — GREEN** (measured, 9 min).
Every finding below coexists with that green. This is §0.1's warning instantiated: the suite is a
SHIPPING gate, not a belief gate.

One environment note: the preinstalled pytest **INTERNALERRORs at collection** for lack of PyYAML
(`build_decisions.py:27` calls `sys.exit`). The green measurement required a yaml-bearing interpreter.
A local run that appears broken may be this, not the tree.

---

## 2. Executed in this PR

| # | Defect | Fix | Falsifier + outcome |
|---|---|---|---|
| E1 | `e3eab09` deleted CLAUDE.md §4–§9 (219 lines) while its message described only a §3 correction; `ED-IN-0146` justifies eight other removals item-by-item and never mentions these | Restored **§4** and **§8**; re-added the **§9 heading** | `ci_hooks_verifier` warned *"naming rule (Solmund) not documented"* before, and does not after |
| E2 | §9 was never deleted — it lost only its **heading**, so its routing table rendered as a data row of §3's table | Heading re-added | `grep -n '^## '` → 9 sections, table renders |
| E3 | `patch_propagation_checker.py`: BLOCKING gate, measured **0 patches / 0 params files** | RETIRED with all 5 wiring points | `test_gate_coverage.py` 13 passed; both CI YAMLs re-parse |
| E4 | Blanket `designs/audit/ → FORK` row shadowed the live `designs/audit/ → audit/` alias (dict last-wins), resolving ~17 **surviving** files as FORKED | Shadow row removed; per-unit FORK rows back-filled from `git diff`, not recall | `broken_dependency_checker` before/after |
| E5 | Five ED-ratified sections still read `Status: PROPOSED`, 23 days stale — the exact ED-1094 failure recurring *after* the convention landed | Flipped, each ED verified `ratified`/`needs_jordan:false` **before** the doc was touched | `ci_generation_consistency` unchanged; 34 tests pass |
| E6 | `systems/mass_battle/sim/` carried no retirement marker despite J2 | Banner added; **no code touched** — the campaign still runs on it | — |
| E7 | `proposals/repo-reorganization-v1.md` asserted *"No files have moved"* three weeks after every slice executed | Status corrected | `ls systems` / `ls designs` |
| E8 | CLAUDE.md carried a duplicated reconcile date (2026-06-28 vs CURRENT.md's 2026-08-04) | Date removed; CURRENT.md's own stamp is the single owner | — |
| E9 | IN ledger at 99% of cap; **this PR's own append pushed it over** (50,960/50,000) | 7 settled entries archived | Size gate 43,976/50,000; citation gate 0 violations; hygiene 19/19 |

E9 is worth naming as a pattern, not an incident: the register lens predicted "the next IN append
likely turns a routine PR red," and the next IN append was this one.

---

## 3. Corrections to the sweep's own output

**The critic's, on the claims:**

| Claim | Verdict | What it got wrong |
|---|---|---|
| dice `roll_pool` ignores `tn` — "live correctness bug" | SURVIVES on fact, **REFUTED on severity** | **Inert.** Every live caller passes TN 7. The non-7 callers are threadwork (never imported by `mc_v18`) and a file marked DEPRECATED. Zero goldens, zero tests. The better falsifier: `_CONTINUOUS_PARAMS` μ=0.50/0.40/0.30 are only reproducible if TN is a face threshold, so the module's discrete and continuous halves **disagree** for tn≠7 |
| "18 ledger keys resolve differently" | **REFUTED as a measurement** | No reproducible instrument; exactly **one** key confirmed. Single-hop is *deliberate* (`pathres.py:152`). Routing `broken_dependency_checker` through chained resolution converts BROKEN→resolved — **loosening** the anti-fabrication gate, not "moving toward correctness" |
| CLAUDE.md §4–§9 deleted; restore all | SURVIVES, **REFRAMED** | §9 wasn't deleted. §5's subject *was* evacuated. A blanket restore would duplicate 20 live lines and re-import prose about a removed tree |
| Crown Mil 4.0 contradicts ED-869 | SURVIVES, **evidence upgraded** | ED-869 is `struck`. The durable authority is **ED-809**: *"Crown Military is 5, Löwenritter is not a separate faction — it is Crown military arm."* Value is **5.0**, not "5/6" |
| `patch_propagation_checker` vacuous *because of the evacuation* | SURVIVES, **cause REFUTED** | Vacuous **before** it: the register has zero `params/` rows ever, and its `affects:` regex requires inline-flow YAML while the register is block-style — so `affects:` has never been parsed at all |
| Campaign runs on the retired MB tree | SURVIVES, **REFUTED as a finding** | Already fully registered as **ED-MB-0064**. Rediscovery, not discovery |

**The control's, on the numbers:** files citing `CLAUDE.md §8` = **79, not 51** (worse); index
freshness = **2 fresh of 20 pinned, not 0 of 39** (overstated — 19 carry no pin); `needs_jordan` =
**88 by field, 95 via `obs_core`'s text-scan rescue** — the headline decision-queue metric has two
definitions and no owner. Unchanged: 214 open EDs, 106 tools modules, **109/109 `canonical_sha` pins
FRESH**, 1675 tests collected, 5-of-9 dead workplan pointers, 88-name MB duplication.

That last one cuts against the repo's own docs: CLAUDE.md §1 calls the pins "not a trustworthy
integrity signal." The distrust describes a **missing verifier**, not bad data — `freshness_gate` was
ported off the GitHub API by ED-1053 and verifies locally.

---

## 4. HELD for Jordan — four decisions (§2 ED-1094: called out loudly, not bundled)

**H1 — §5–§7 disposition.** Restore, tombstone, or re-home? §5's subject (`engine/params/`) is
evacuated; §6's (`godot/`) and §7's (`engine/` + `systems/*/sim/`) are alive. **327 citations across
176 files** name §4–§9. Not defaulted because a mixed case needs a decision.

**H2 — Crown Mil 4.0 → 5.0.** Contradicts two closed rulings and feeds the live conquest gate
(`faction_action.py:423`) and Mil-only unit construction. **Not executed**: it is a behaviour change
requiring a deliberate golden re-record per §0.1. `systems/world/worldbuilding_v30_infill.md:36`
asserts the opposite and must move in the same change, or the contradiction merely relocates.

**H3 — the PP citation universe.** `validate_ed_citations` is ED-only, and the patch archives left
`main` on 2026-08-05: **433 of 452 distinct `PP-NNN` cited in live surfaces resolve to no register.**
Either declare PP provenance-only (honest, zero code) or restore the archives as the ED archives were
deliberately kept. The current state is an anti-fabrication gate that half-exists.

**H4 — mass-battle J2, plus a governance defect.** Migration is gated on the four `degree` band edges
only (`attacker_wins` is derivable from the 2026-08-04 C2 ruling). **The defect:** that live blocker is
recorded *inside* `ED-MB-0064`, which is `status: resolved, needs_jordan: false` — invisible to every
`needs_jordan` sweep and to the SessionStart banner. This repeats the failure ED-MB-0064 was itself
written to fix.

---

## 5. Work instructions for follow-on execution

Tier per §10. **Every task below states its own falsifier**; a task whose falsifier cannot be written
is not ready to start (§0.1 point 5).

### 5.1 Sonnet-5 — mechanical, bounded, no judgment

**S1 · Sweep the dangling §-citation corpus.** 327 occurrences / 176 files cite §4–§9. **Blocked on
H1** — do not start until §5–§7 are ruled, or the sweep runs twice. Then: repoint each to the restored
section or the ruled successor. *Falsifier:* a re-grep returns only refs to sections that exist.
*Do not* build a §-anchor CI gate for this — see the cut list.

**S2 · Enroll the orphaned report-only signals.** `scope_ratchet` (REGRESSED since 2026-08-01),
`canon_coverage_check`, `mechanics_index_gen --strict`, `ci_workplan_pointer_check --strict` all emit
red into a log nobody is failed by. Add each as a `CHECKS` row in `review_core` with a baseline equal
to today's measured debt. *Falsifier:* `review_core --check` exits nonzero if any regresses.
⚠️ `registers/review_baseline.yaml` is CODEOWNERS-gated — deliberately Jordan's edit.

**S3 · Fix the 5 dead workplan pointers.** Repoint or delete; targets are evacuated.
*Falsifier:* `ci_workplan_pointer_check --strict` exits 0.

**S4 · Add `mass_seizure.py` to the OI-12 orphan census.** One tuple entry; it is an unregistered
orphan the census misses. *Falsifier:* `test_oi12_orphan_census.py` covers it.

**S5 · Give `needs_jordan` one definition.** Two live readings (88 by field, 95 by text-scan rescue).
Pick one in `obs_core`, make the other a documented fallback, and state which the banner reports.
*Falsifier:* a test asserting banner count == `obs_core` count.

### 5.2 Opus-5 — judgment, contested evidence, cross-lane

**O1 · Execute H2 once ruled.** Not a one-token edit. Change `game_state.py:52`, correct
`worldbuilding_v30_infill.md:36` in the same commit, re-record affected goldens **deliberately** with
the diff explained, and cite ED-809 as primary. *Falsifier:* name the specific golden that moved and
show the before/after.

**O2 · Repair the ED-MB-0064 governance defect (H4).** Open a `needs_jordan: true` MB entry scoped to
the four `degree` band edges **only**, so the lane's sole live blocker stops living inside a closed
row. Do **not** re-file the whole J2 finding — it is already registered. *Falsifier:* a `needs_jordan`
sweep surfaces the band-edge decision.

**O3 · Land the `pathres` consolidation in the safe order.** (1) Correct the "SOLE PARSER" comment to
*intended* sole parser naming the four outstanding migrations — done in this PR. (2) Migrate
`ci_claude_workflow_paths` first (lowest risk). (3) Migrate `broken_dependency_checker` **at
`max_hops=1`**, preserving semantics exactly. Only then argue chaining on its own merits, **with a
real instrument** — the "18 keys" number was not one. *Falsifier:* the blocking gate's verdict set is
byte-identical across the migration.

**O4 · Decide the `params_tables.yaml` disposition.** Its generator (`export_params_constants.py`) and
its named falsifier (`test_params_dump.py`) were both deleted in `e3eab09`. It is 1,367 rows that
nothing can regenerate, nothing reads for values, and nothing checks. Either declare it read-only
history (sha-pin it so silent edits fail) or move it under `deprecated/`. Then run the one-time
captured-row-vs-code reconciliation — the Crown Mil, CI-start and Seizure-Ob disagreements are its
seed list. **"Code wins" cannot be applied blind**: it crowned a struck value once already.

**O5 · Add the architecture-direction guard.** "Autoload is a leaf" is false — `game_state` imports
ten `systems.*.sim` modules at 11 sites; the core has 20 downward edges. Pin the current edge set as a
**shrink-only allowlist**. No production change. *Falsifier:* the test fails when a new downward edge
lands. This is the one new guard worth building, because the claim it protects is stated in CLAUDE.md
§3 and is currently false.

### 5.3 CUT LIST — proposed and rejected

Four of six lenses proposed new tooling; two proposed removals. The additions are where the ceremony
is. Rejected, with reasons:

- **A TN-9 row in `_CONTINUOUS_PARAMS`** — mints an uncanonical TN (the table stops at 8) and adds a
  fourth copy of a table that should be *derived*. If the dice fix is ever made, derive μ/σ by
  enumerating the ten faces; every TN then works by construction and the EV table becomes a test
  assertion rather than a second source of truth.
- **`raise on unknown TN`** — guards a path with zero live non-7 callers; dead code the moment the
  derivation lands.
- **Repointing `patch_propagation_checker` at `params_tables.yaml`** — revives a convention with no
  maintainer to serve a register with no params rows. Retired instead.
- **A CLAUDE.md §-anchor CI gate** — nine dangling refs in one file. Fix them and move on. Jordan:
  *"Keep it simple, ie don't build tools unnecessarily."*
- **A fifth die-rule test harness** — one parameterized assertion against the canonical EV table
  replaces the guard, the TN-9 row and the raise together.

---

## 6. Filed, not swept (§0.1 point 5: sweep only what the task is load-bearing on)

- **36 of 106 `tools/` modules have zero automated callers** (28 = the `sim_harness/` prototype
  cluster). Denominator and a 6-module sample verified; the total is not independently re-derived.
- **§2a conformance: 7 of 15 `systems/` folders fail**, and CLAUDE.md's exception note names only 3.
  Unflagged: `threadwork` (files EDs under WR), `world`, `npcs`, `articulation`, `ui`.
- **Authority-by-citation without an index row**: `victory_v30` (CANONICAL, **103 citing files**),
  `peninsular_strain_v30` (79), `knots_v30` (66). The `clock_registry_v30` failure mode as a standing
  condition. Cited-by-nothing orphans: **zero**.
- **97 evacuated `audit/<unit>` dirs cited from live surfaces**; partially addressed by E4, remainder
  filed. Includes `CURRENT.md:31` citing the location of Jordan ruling D1, and **ED-IN-0070's subject
  document** — an open `needs_jordan` item whose subject was evacuated.
- **`glossary.md:92`** binds "Piety Track" to a 0–10 debate tracker citing the wrong doc — wrong scale,
  wrong mechanic, wrong pointer, three errors in one row. The only *actively misleading* terminology
  defect found.
- **Certainty→Truth rename** still unexecuted at 18 days. The count fell 419→282, but that is
  **attrition from evacuations, not the sweep** — a naive reading looks like progress.
- **Three degree-ladder implementations** disagree at boundaries: only the canon MB copy has
  `_DEGREE_EPS` (the 1-ulp defect §0.1 point 2 memorializes), only `dice_engine` has the Ob≥20
  exception. The epsilon fix landed in one copy of three and never swept.
- **`review_core` has zero `blocking`-tier signals**, so its documented "exit 1 on blocking failure"
  branch is vacuous; an `info` signal that fails is counted in neither bucket, so the rollup can grade
  GREEN over a failing signal.
- **3 of 55 Key types** carry default scale signatures the runtime validator rejects; the identity gate
  is green because *both* loaders are broken identically. Only **3 of 55** types are emitted by live code.
