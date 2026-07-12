# Simulation & Test Harness Methodology v1

**Status: RATIFIED** (ED-IN-0038, Lane IN — ratified 2026-07-12). §11's four open questions were put to
Jordan directly (not assumed) and are RULED below; everything else in this doc ratifies as originally
proposed. The architecture (§3–§8), the Gate-0 prototype (`tools/sim_harness/` — six rounds of
adversarial review and deliberate stress-testing since initial filing, 34 real bugs found and fixed, see
the package's own README for the full account), and the rollout order are now the plan of record.

**§11 rulings (Jordan's actual answers, not defaults assumed on his behalf):**
1. **Rollout order — extended, not left as originally proposed.** Jordan flagged a real gap: the
   original §8 only sequenced 5 waves and silently omitted settlement/territory, faction actions, and
   threadwork, all of which have real `sim/` code per §1.1. §8 now adds `faction_action.py`,
   `sim/territory/*`, and `sim/thread/*` as waves 5–7 (mass battle stays wave 4), with campaign
   composition last. Field investigation is explicitly excluded, not omitted by oversight — its `sim/`
   implementation is still `[PROVISIONAL]` stub-only, so there is no real resolver to adapt yet.
2. **Wave 1 CI burn-in — the existing ratchet convention applies, no deviation** (Jordan: "Full
   report-only burn-in").
3. **`mc_v18.py` full-campaign runs never gate a PR** (Jordan: "Never gate a PR") — a firm constraint on
   the Wave-8 adapter, not just a deferred question.
4. **The four §9 quick wins are filed as separate lane work, not bundled into this PR** (Jordan: "File
   separately") — tracked as ED-IN-0039.

**Trigger:** a repo-wide sweep of every engine/resolver/simulator/test/Python surface, requested to
evaluate how Valoria manages simulation and testing at this point in the project, and to propose a
harness that can be pointed at *any* subsystem on demand, verified against canon rather than
fabricated values, built modularly (a pluggable "test module" per subsystem), and backed by a logger
that explores probabilistic alternatives at a severity-scaled depth and never lets a gap go
unflagged.

**Relationship to PR #122 ("Audit ecosystem: consolidation, reconciliation, and always-fresh
infrastructure," ED-IN-0032–0037, merged 2026-07-11):** that batch fixed the *audit-tooling* layer —
dead-tool retirement, registry regeneration, a self-checking CI-checks registry, a scheduled
decisions-digest refresh. It explicitly did **not** touch simulation execution or the audit-registry's
live-logging gap; ED-IN-0035 stopped short of building a vector-audit refresh job specifically
*because* the underlying script was found to be a stub, and left "audit_registry.jsonl has 5 backfilled
entries and no live-append path" untouched. This proposal picks up exactly there — it is the next
phase, not a re-do.

---

## 0. Executive summary

Valoria has three genuinely load-bearing simulation/test surfaces (`tests/valoria/`, `sim/tests/`,
`tests/contracts/` — 594 tests, all green) and one real, well-designed universal interface
(`references/module_contracts.yaml`'s IN(Keys)→resolver→OUT(Keys) shape, formalized by the Holonic
Container Doctrine). What it does **not** have is a closed loop connecting them: the one script that
checks architectural closure (`contract_adjudicator.py`) is unit-tested but never run against the live
corpus in CI; the two scripts that produce real Monte-Carlo numbers (`combat_sim.py`, `valoria_dice.py`)
have no asserted thresholds anywhere, only human "Step 6" prose judgment; five of eight audit skills are
pure LLM reasoning with no executable backing at all; the audit trail meant to unify all of this
(`audit_registry.jsonl`) has never been live-appended, only backfilled once; and a working pytest suite
sits under `tests/hooks/`, `tests/index/`, `tests/registry/` that no CI job or local hook executes at
all.

The proposal: a single generic **harness core** — canon-parameter resolver, depth-tiered probabilistic
branch explorer, and a triage-flagging trace logger — plus one thin, mandatory **adapter** per
`module_contracts.yaml` module (the "test module" the request asked for). The harness is subsystem-blind;
only the adapter knows the subsystem. This reuses the repo's own universal shape instead of adding a
28th one, and it is designed to absorb the two real numeric tools (`combat_sim.py`, `valoria_dice.py`)
as adapters rather than compete with them.

A minimal, runnable **Gate-0 prototype** ships alongside this doc at `tools/sim_harness/` (harness core +
logger + one demo adapter over `valoria_dice.py`, chosen because it is the simplest genuinely canon-cited
resolver in the repo and carries no game-balance judgment risk). It is a proof of shape, not a claim that
all 27 modules are covered — see §8 for the actual rollout order.

---

## 1. Inventory (what exists today)

### 1.1 `sim/` — 104 files, ~18k LOC, the Python oracle

| Maturity | Approx. LOC | Examples |
|---|---|---|
| Real / CANONICAL, tested | ~9k | `mc_v18.py`, `substrate/keys.py`, `personal/contest/` (6.4k, largest subsystem), `provincial/massbattle.py` (1905L), `provincial/faction_action.py`, `autoload/*`, `cross_scale/*` |
| Real, populated, **zero dedicated test** | ~3k | `provincial/massbattle.py` (1905L, CANONICAL — only indirect campaign coverage), `thread/*` (~1500L, one narrow regression: `test_thread_mending_ed871.py`), `territory/*`, `provincial/crown_initiative.py`/`council_solmund.py`/`excommunication.py`/`absolution.py` |
| `[PROVISIONAL]` stub, `NotImplementedError` | ~1k | 6 faction-flavor unique actions (`varfell_*`, `hafenmark_equipment.py`, etc. — deliberately blocked on a contamination audit, not neglected), `personal/tribunal.py`, `personal/fieldwork.py`/`investigation.py`/`companion.py`, `world/restoration_movement.py`/`miraculous_event.py`, `cross_scale/articulation.py` |
| Confirmed dead, still importable | 305L | `personal/combat.py` — superseded by `designs/scene/combat_engine_v1/`, banner-marked DEPRECATED 2026-06-23, but nothing prevents an accidental re-import |

`sim/tests/` (9 files, all deterministic-seeded pytest) is the real regression oracle (ED-1053):
`test_mc_v18_regression.py`, `test_f7_smoke_oracle.py` (the file that debunked the "~87% degenerate
win-share" claim as a small-N artifact of one unguarded `run_batch(8, seed=42)` call — its own
docstring states the lesson: *"no balance claim without an oracle + n ≥ 100"*), `test_contest_kernel.py`,
`test_echo_transport.py`, `test_parliamentary_bridge.py`, `test_parliamentary_action.py`,
`test_knots_ed912.py`, `test_thread_mending_ed871.py`, `test_sigma_leverage_parity.py`. 419 passed / 577
skipped (numpy unavailable locally) in the local run.

### 1.2 Test surfaces (`tests/`, 206 .py files + ~2.5MB prose)

| Surface | Real? | CI-wired? | State |
|---|---|---|---|
| `tests/valoria/` | Yes — 24 files, 221 test functions | Yes, blocking | 141 passed / 58 skipped / 1 xpassed |
| `sim/tests/` | Yes — the ED-1053 oracle | Yes, blocking (`sim-regression` job) | 419 passed / 577 skipped (env-only) |
| `tests/contracts/` | Yes — `test_contract_adjudicator.py` | Yes, blocking (un-orphaned 2026-07-07) | 34 passed |
| `tests/sim/` | **No** — frozen historical archive predating `sim/`, held old `mc_v17.py`. Name collision only. | No (except path-string references from `ci_sim_fabrication_check`/`atomization_rules`) | 151 .py / 295 .md / 51 .json, ~8.3MB, history only |
| `tests/sim_framework/` | **No** — a separate, abandoned earlier harness attempt, never consumed by `sim/` | No | ~588KB, dead |
| `tests/hooks/`, `tests/index/`, `tests/registry/`, 2 files under `tests/sim/` | **Yes — real pytest code** | **No job runs them, no local hook runs them** | Silent, actionable coverage gap |
| ~77 narrative `.md` under `tests/` (`emergent_arc_skeleton_test_*`, `tests/audit/`, `tests/stress/`) | No — prose session logs | N/A | ~2.5MB, not specs, don't mine as behavioral contracts |

### 1.3 `tools/` — 44 files, the CI/local validator layer

25 CI jobs, 14 local pre-commit checks, largely well-disciplined (single-reader libraries:
`ci_common.py`, `names.py`, `descriptor_registry.py`, `audit_registry.py`, `audit_staleness.py`,
`workplan_status.py`). Simulation/balance-relevant pieces:

- `export_engine_params.py` — blocking round-trip check, `config.py` → `references/engine_params/combat_engine_v1.json`. The one place a typed export is actually verified against its oracle.
- `ci_sim_fabrication_check.py` — blocking; every numeric literal in `sim/*.py` must be ledger-cited. CLAUDE.md §7 already documents it as leaky (matches by bare value+integer-token split, only scans the changeset).
- `ci_module_shape_check.py` — report-only; container-hygiene (no `sys.path` reach-ins) + INFO-tier constant surfacing. Complementary to fabrication-check, not a duplicate.
- `ci_audit_registry_check.py` — report-only; flags a `designs/audit/` folder newer than the registry's latest entry. Cannot force a live append, only notice a missed one after the fact.
- 3 orphaned-but-not-retired utilities (`propagator.py`, `find_references.py`, `verify_cuts.py`) — no caller anywhere; out of scope for this proposal but flagged for the same `deprecated/tools/` treatment as the 2026-07-09 batch.

### 1.4 The 8 audit/simulation skills

| Skill | Executable backing | Produces |
|---|---|---|
| `valoria-module-adjudicator` | **Yes** — `contract_adjudicator.py` (A1–A12 checks, exit-code), `contract_flowchart.py`, own fixture suite | Machine-checkable pass/fail on contract closure — **but never run against the live corpus in CI**, only its own correctness is CI-tested |
| `valoria-combat-simulator` | **Yes** — `combat_sim.py` (5k–10k trial Monte Carlo) | Real win/loss/draw numbers to `sim/results/` — but threshold interpretation (armor dominance >80%, etc.) is unasserted human judgment |
| `valoria-dice-model` | **Yes** — `valoria_dice.py` (200k-trial Monte Carlo) | Real probability numbers, reused by other skills as a spot-check oracle |
| `valoria-canon-guard` | No | Prose PASS/PARTIAL/FAIL against P-01–P-15 |
| `valoria-mechanic-audit` | No | Prose reports, hand-calculated formulas |
| `valoria-resolution-diagnostic` | No | 383-line NERS procedure, all arithmetic done by hand |
| `valoria-simulator` | No | General stress-test protocol; **Mode G** (Incremental Build Protocol) is a real, valuable scar-tissue safeguard against fabrication, born from the `sim_v2` disaster (24 correct / 15 partial / 8 wrong / 5 fabricated / 19 missing-assumption, one session, unread canon) |
| `valoria-vector-audit` | **No — confirmed stub.** `main()` ends at `# Stage execution dispatcher would go here`; SKILL.md now says outright not to expect output (fixed 2026-07-11, ED-IN-0035/0036) | Nothing runnable |

`references/audit_registry.jsonl`: 5 entries, **all** `"skill": "backfill"`, `"confidence": "inferred"` —
i.e. reconstructed after the fact, none live-appended by an actual skill run, despite every skill's
SKILL.md carrying a "mandatory on completion" logging step.

`references/module_contracts.yaml`: 27 modules, 10 with `doc: null`, 11 `[ASSUMPTION]`-grade resolvers,
2 `status: stub` — i.e. the one real contract linter validates closure over a map that is itself ~37%
unverified, per CLAUDE.md §6.

---

## 2. Evaluation of the current process

**What's genuinely strong** (worth preserving, not replacing):
- The IN(Keys)→resolver→OUT(Keys) contract shape and the Holonic Container Doctrine give the repo one
  real universal interface, with a real linter behind it. Most Godot-port and multi-scale-composition
  repos never get this far.
- `sim/tests/`'s deterministic-seed discipline (ED-1053) and `test_f7_smoke_oracle.py`'s own corrective
  history are a working example of exactly the rigor a harness should generalize: *"no balance claim
  without an oracle + n ≥ 100,"* stated in the file's own docstring.
- Mode G of `valoria-simulator` (one-module-per-session, verification ledger, quoted-text citation for
  every constant) is a real, hard-won anti-fabrication discipline, directly responsive to a documented
  past failure. It should become the harness's default operating mode, not stay skill-only prose.
- The Producer + independent adversarial reviewer pattern (visible throughout recent PRs — #122's six
  phases, the JD-4/JD-9 13-agent adversarial Workflow) is a real, working verification methodology
  already proven on this repo. The harness should be built the same way it's meant to *verify* things.

**Where the process breaks down** — this is the actual gap the request is asking to close:

1. **Nothing closes the loop from "a check exists" to "the check ran against the live corpus and
   something would fail if it were wrong."** `contract_adjudicator.py` is real and correct (its own
   fixture suite proves that) but is never invoked against `module_contracts.yaml` by CI — only a skill
   invocation, by hand, produces that. The dashboard's "audit results" are backfilled prose, not live
   verdicts.
2. **No numeric threshold is ever asserted in CI.** `combat_sim.py` and `mc_v18` can both produce real
   Monte-Carlo output, but "is this balanced" is a human reading a report, every time, from scratch —
   there is no golden range, only golden *point* values in `sim/tests/` (useful for regression drift,
   not for "is this within design tolerance").
3. **Prose-only audits (5 of 8 skills) have no way to be wrong in a way that fails loudly.** A skill
   that hand-computes a probability curve can silently make an arithmetic error; nothing re-derives it
   mechanically to check.
4. **The audit trail is decorative.** Every skill claims to log to `audit_registry.jsonl`; none has ever
   actually done so outside the one-time backfill. Any methodology built on "check the registry for
   drift" is building on a foundation that has never been exercised for real.
5. **Real test code goes silently unexecuted** (`tests/hooks/`, `tests/index/`, `tests/registry/`) —
   the inverse failure of the above: work was done, and then nothing wired it in, and nothing notices
   that nothing wired it in.
6. **Canon-fidelity verification happens at commit time on source text, not at run time on the values
   actually used.** `ci_sim_fabrication_check.py` greps `sim/*.py` for cited literals; it has no
   equivalent for "the number a live simulation run actually plugged in resolves to the current prose
   head via `CURRENT.md`," which is the sharper, run-time version of the same anti-fabrication goal.

**Conclusion:** the repo does not lack rigor or taxonomy — the failure mode is the opposite of Godot
skeleton-not-buildable (§6 of CLAUDE.md): here, the pieces are individually real and correct, but
disconnected. The methodology below is a connective-tissue proposal, not a rebuild.

---

## 3. Proposed methodology — governing principles

1. **One generic harness, many thin adapters — never a 28th interface shape.** A subsystem's "test
   module" is an adapter satisfying a small `Adapter` protocol; the harness core has zero subsystem
   knowledge. This is the modular architecture the request asked for, and it is a direct application of
   the Holonic Container Doctrine's own compliance/convertibility standard rather than an invented one.
2. **Canon resolution happens at run time, not just at commit time.** Before an adapter runs a single
   trial, the harness resolves its declared parameters through the same chain a human would:
   `CURRENT.md` → the cited prose param/design doc → the `PP-NNN`/`ED-NNN` that established the value.
   If that chain doesn't resolve, the harness refuses to fabricate a default and raises a **canon gap**
   triage flag instead of a guessed number (mirrors `sim/substrate/keys.py`'s own OF-CAP discipline:
   *"the sim never silently corrects canon"*).
3. **Depth is a property of the event, not the harness invocation.** See §5 — every resolver call
   ("event") the harness intercepts is tiered 1/2/3 by consequence severity, and branch-alternative
   exploration scales with tier. The harness ships a default classification rubric; an adapter may
   override it per event type, never per outcome (that would be scripting drift).
4. **Nothing is ever silently green.** Every run produces a triage-flag list, even an empty one. A
   flag is never dropped for being "probably fine" — it either resolves to a filed ED or stays open,
   the same forward-only-disposition discipline ED-IN-0036 already added to `valoria-vector-audit` and
   `valoria-simulator`'s output contracts.
5. **The harness absorbs the two real numeric tools rather than competing with them.** `combat_sim.py`
   and `valoria_dice.py` become the first two adapters (§6), not parallel systems.
6. **Ratchet, don't flip.** Every new CI job starts report-only, exactly like `ci_generation_consistency`
   and `canon_coverage_check` did in PR #122, and is promoted to blocking only after a burn-in period
   with a named owner — this repo already has a working precedent for that ratchet, reuse it.

---

## 4. Harness architecture

```
tools/sim_harness/
  harness.py          Harness — orchestrates one run: resolve canon → instantiate adapter →
                       run trials at requested depth → explore alternatives at decision points →
                       feed every event to TraceLogger → emit run summary → append registry record
  canon_resolver.py    CanonResolver — CURRENT.md row → prose doc → PP/ED citation chain;
                       raises CanonGapError (never fabricates) when the chain doesn't resolve
  adapter.py           Adapter (ABC) — the "test module" contract every subsystem implements:
                         .contract_module        # key into references/module_contracts.yaml
                         .resolve_params()        # -> (params: dict, citations: list[str])
                         .decision_points()        # -> list[DecisionPoint] (name, default tier, branches)
                         .run_once(rng, params)   # -> Outcome (one sampled trial)
  depth.py             DEPTH_TIERS (1/2/3) + classification rubric + alternative-exploration policy
  triage.py            TriageFlag taxonomy + collector (CANON_GAP, CONTRACT_VIOLATION, OUT_OF_RANGE,
                       STUB_HIT, DEGENERATE_DISTRIBUTION, FABRICATION_RISK, UNCLASSIFIED)
  trace_logger.py       TraceLogger — per-event probabilistic trace (extends the KeyLog pattern,
                       does not fork it) + live audit_registry.jsonl append via tools/audit_registry.py
  adapters/
    dice_pool_demo.py  Gate-0 demo adapter — wraps skills/valoria-dice-model/valoria_dice.py
```

**Binding to `module_contracts.yaml` is mandatory, not optional.** An adapter's `contract_module` must
resolve to a real entry; if that entry is `doc: null` or `[ASSUMPTION]`-grade, the harness still runs
but every event from that adapter is auto-tagged with a `CONTRACT_GAP` triage flag, surfacing the
same ~37%-unverified problem CLAUDE.md §6 already names, at the point where it actually matters (a live
run) rather than only in a static count.

**Contract closure becomes part of every run, not a separate skill invocation.** The harness calls
`contract_adjudicator.py`'s A1–A12 checks against the adapter's declared module before running trials —
this is the fix for §2 finding 1 (the linter existing but never running against the live corpus): every
harness run *is* a corpus-level adjudicator run, for free, scoped to the one module under test.

---

## 5. The logger: depth-tiered probabilistic exploration + mandatory triage flagging

Every resolver call the harness drives is an **event**. Because resolvers are probabilistic (dice
pools, opposed rolls, weighted branch selection), a single sampled trial says nothing about the shape
of the outcome space around it — that's the same lesson `test_f7_smoke_oracle.py` already learned the
hard way for whole-campaign balance (§1.1). The logger generalizes that lesson to every event, tiered
by how much a wrong answer would cost:

| Tier | Label | Default triggers (harness rubric, adapter may override per event type) | Exploration policy |
|---|---|---|---|
| **1** | Minor | A single skill check, an individual attack roll, any event whose outcome is locally reversible next tick | Record the sampled outcome + the theoretical outcome-bucket probabilities (already computable, e.g. `outcome_probs()`) — no extra trials. Cheap, always-on. |
| **2** | Medium | A contest verdict, a Censure vote, a settlement-scale derived-stat write, anything that emits a Key consumed cross-scale | For each possible outcome bucket at this event, run a bounded number of *conditioned* follow-on trials (one branch level: "given this bucket, what happens next") — surfaces whether a plausible-but-unsampled branch would have produced a contract violation or an out-of-range value. |
| **3** | Major | A campaign-defining event: conquest resolution, succession, mass-battle victory condition, anything gating an ED/PP ratification or feeding `mc_v18`'s victory check | Full bounded branch-and-bound to a fixed depth (or exhaustive enumeration when the outcome space is small enough — e.g. a 4-way Terms/Sack/Storm/Withdraw fork), plus a large-N (≥100, per the f7 lesson) stratified run across the whole decision tree. Every terminal branch is checked against contract closure and declared range. |

Tiering is deliberately **harness discretion within a rubric**, per the request — the rubric above is
the default classifier; an adapter's `decision_points()` may assign a specific event a higher tier (never
lower, to prevent an adapter quietly downgrading its own scrutiny) with a one-line justification string
that the logger records verbatim.

**Triage flagging (mandatory, not best-effort):**

```
TriageFlag(
  event_id, tier, category, detail, source_citation | None
)
```

Categories: `CANON_GAP` (a value or doc reference didn't resolve — §3 principle 2), `CONTRACT_VIOLATION`
(an A1–A12 check failed for this adapter's module), `OUT_OF_RANGE` (an outcome fell outside a declared
clamp/bound), `STUB_HIT` (the adapter's resolver hit a `NotImplementedError` or `[PROVISIONAL]` branch —
this is how the harness would have caught, mechanically, that `provincial/varfell_*.py` etc. are
intentional stubs rather than silently treating "ran without crashing" as a pass), `DEGENERATE_DISTRIBUTION`
(a tier-3 exhaustive/large-N run collapses to a near-single outcome, the generalized form of the
"~87% win-share" bug), `FABRICATION_RISK` (a numeric literal reached the resolver without a citation
the `CanonResolver` could verify — the run-time counterpart to `ci_sim_fabrication_check.py`).

Every run, pass or fail, writes:
1. A full per-event JSONL trace (for replay/debugging — mirrors `KeyLog.serialize()`'s existing
   content-hash pattern, so a trace is independently verifiable, not just trusted).
2. A run summary that calls `tools/audit_registry.append_record(...)` **directly, in-process** — not
   "the skill is supposed to remember to log this afterward." This is the concrete fix for §2 finding 4:
   the registry stops being decorative because the harness, not a human's memory, is the thing writing
   to it, using the audit_type `simulation_balance` the schema already recognizes.
3. If any triage flag is unresolved, the run summary's verdict is `PARTIAL` or `FAIL` (never `PASS` with
   an open flag) — flags cannot be silently swallowed by an otherwise-successful run.

---

## 6. Reuse map — what this absorbs, supersedes, or leaves alone

| Existing surface | Disposition |
|---|---|
| `contract_adjudicator.py` (A1–A12) | **Absorbed as a pre-flight check**, called by the harness before every adapter run. Its own fixture suite (`tests/contracts/`) is untouched — still the thing that verifies the checker's own correctness. |
| `combat_sim.py`, `valoria_dice.py` | **Become adapters.** Their Monte Carlo cores are reused verbatim; the harness adds canon-resolution, depth-tiering, and triage-flagging around them instead of duplicating the trial logic. |
| `sim/tests/` (ED-1053 oracle) | **Left alone**, and used as the model for what a tier-3 golden should look like. The harness does not replace deterministic regression tests — it's for exploratory/stress runs, not pinned goldens. |
| `mc_v18.py` | Eventually the harness's largest adapter (a "campaign" adapter, tier-3 by default), but explicitly **out of scope for the first rollout wave** — see §8, it's the highest-blast-radius target, not the first one. |
| `ci_sim_fabrication_check.py` | **Left alone** — still the commit-time gate. The harness's `FABRICATION_RISK` flag is the run-time complement, not a replacement. |
| 5 prose-only skills (`canon-guard`, `mechanic-audit`, `resolution-diagnostic`, `simulator`) | **Left alone as human/LLM judgment tools.** Not everything should become a script — P-01–P-15 compliance and NERS judgment calls are legitimately reasoning tasks. The harness's job is to make the *numeric* half of what they currently do by hand mechanically checkable, freeing the prose judgment for the parts that actually need it. |
| `valoria-vector-audit` | **Out of scope.** Already correctly identified as a stub needing real engineering (ED-IN-0035/0036); this proposal doesn't change that finding or try to fold it in. |
| `audit_registry.jsonl` / `tools/audit_registry.py` | **Reused, not replaced.** The harness becomes its first live writer. No new registry file. |

---

## 7. CI integration (the ratchet)

Following the exact pattern already proven in PR #122:

1. **Wave 0 (this proposal + Gate-0 prototype):** no CI change. `tools/sim_harness/` exists, is
   run-by-hand only, same footing `combat_sim.py` has today.
2. **Wave 1:** one report-only CI job, `sim-harness-pilot`, running the harness against **one** adapter
   (§8 names the candidate) on every PR touching that module's declared source files (reuse
   `ci_common.get_changed_files()`, the existing single source of truth for "what changed"). Non-blocking,
   `continue-on-error`, excluded from `ci-summary`'s required list — identical wiring to
   `ci_generation_consistency` and `canon_coverage_check`'s own onboarding.
3. **Wave 2:** after a burn-in period with zero false-positive triage flags, promote that one job to
   blocking. Add the second and third adapters as report-only.
4. **Steady state:** each new adapter starts report-only and is promoted independently — never a
   blanket flip. `references/ci_checks_registry.yaml` gains one row per promoted job, exactly like
   every other checker (self-audited by `broken_dependency_checker.py::check_ci_registry_coverage()`,
   already wired).

---

## 8. Phased rollout — adapter order

Ordered by (a) how real and populated the underlying `sim/` module already is, (b) how contained the
blast radius of a false triage flag would be, (c) whether canon citations are clean enough to resolve
without a separate research pass:

1. **`valoria_dice.py`** (dice-pool primitives) — Gate-0, ships with this proposal. Simplest possible
   resolver, canon-cited cleanly to `params/core.md`, zero game-balance judgment risk.
2. **`combat_sim.py`** (personal combat) — the most mature CANONICAL subsystem, already has a verified
   typed export (`references/engine_params/combat_engine_v1.json`, round-trip-checked) to resolve
   canon params from directly rather than re-deriving from prose, and an existing Monte Carlo core to
   wrap rather than write.
3. **`sim/personal/contest/`** (social contest kernel) — largest real subsystem, has its own
   `_kernel_tests.py` (222 seeded checks) to cross-validate the harness's tier-1/2 output against.
4. **`sim/provincial/massbattle.py`** — highest-value target per §1.1's own gap finding (1905 LOC,
   CANONICAL, zero dedicated test today), but held to wave 4 deliberately: it's the largest ungoverned
   surface, so it should go in after the harness has already proven itself on three smaller subsystems.
5. **`sim/provincial/faction_action.py`** (448L, CANONICAL) — real, GD-2 mandatory-action dispatch,
   already exercised indirectly via `mc_v18` regression tests but with no dedicated unit test of its
   own; same maturity/risk tier as mass battle, sequenced right after it.
6. **`sim/territory/*`** (settlement/territory — `adjacency.py` CANONICAL, the rest populated and
   real but unlabeled, no dedicated test in `sim/tests/`) — same profile as faction actions: real,
   untested, ready for an adapter.
7. **`sim/thread/*`** (threadwork, ~1500 LOC — real except `rendering.py`/one branch of `opposing.py`,
   only one narrow existing regression, `test_thread_mending_ed871.py`) — largest remaining real-but-
   thin-tested surface before campaign composition.
8. **`mc_v18.py`** (full campaign) — last, tier-3-only, explicitly the `test_f7_smoke_oracle.py`
   large-N discipline generalized to arbitrary campaign configurations, not just the one pinned seed.
   Composes all of the above, so it has to come after them.

**Field investigation is a different case, not an oversight:** its `sim/` implementation
(`personal/fieldwork.py`/`investigation.py`/`companion.py`, 33L/31L/21L) is still `[PROVISIONAL]`
armature-stub-only per §1.1 — there is no real resolver to adapt yet, only a stub that would
immediately and only confirm `STUB_HIT`. It becomes a rollout candidate once that engineering work
(tracked separately, not by this proposal) lands a real resolver. Faction-flavor `[PROVISIONAL]` stubs
and other deliberately-unauthored modules are excluded from the sequence for the same reason — running
the harness against them would only confirm what's already known and tracked as a contamination-audit
dependency, not a gap this harness needs to rediscover.

This still isn't all 27 `module_contracts.yaml` modules — the "many thin adapters" architecture means
every real module eventually gets one, but only these 8 are sequenced concretely here. The rest (e.g.
`scene_slate`, `game_director`, `engine_clock`) get adapters as capacity allows, in whatever order a
future session finds has the best real/populated-vs-tested ratio, using the same three criteria above.

---

## 9. Quick wins found during the sweep (independent of the harness — can be actioned separately)

These don't require the harness at all and are cheap, but are called out here rather than fixed
silently, per §2's own "flag it, don't quietly patch it in a routine batch" doctrine:

- `tests/hooks/`, `tests/index/`, `tests/registry/`, and 2 files under `tests/sim/` contain real,
  currently-passing-if-run pytest code that no CI job or local hook executes. Either wire them in or
  explicitly retire them — right now they're neither.
- `sim/personal/combat.py` is confirmed dead (superseded, DEPRECATED-banner-marked 2026-06-23) but
  remains importable; an accidental re-import is a silent correctness risk with no guard against it.
- `tools/propagator.py`, `find_references.py`, `verify_cuts.py` have the identical orphaned-tool
  profile as the batch already retired 2026-07-09, but weren't caught by that sweep (they don't import
  a dead module or hardcode a path, so the exact retirement heuristic used then missed them).
- `contract_adjudicator.py` could be wired into CI report-only *today*, independent of this whole
  proposal — it already exists, is already correct per its own fixture suite, and simply has never been
  pointed at the live `module_contracts.yaml` by an automated job.

---

## 10. Gate-0 prototype

A minimal, runnable proof of the architecture in §4–§5 ships alongside this document at
`tools/sim_harness/` — see its `README.md` for exact usage. It wires one adapter
(`adapters/dice_pool_demo.py`, over `valoria_dice.py`), demonstrates canon-parameter resolution,
tier-1/2/3 branch exploration, triage-flag collection, and a live (not backfilled) `audit_registry.jsonl`
append. It is explicitly **not**: wired into CI, a claim of coverage over any subsystem beyond the demo,
or a claim that `combat_sim.py`/contest/mass-battle adapters (§8 waves 2–8) are anything more than
specified here.

**§3's two governing halves — canon-verified simulation AND pluggable provisional test code — are both
now concretely proven, not just claimed.** The demo adapter proves the first half (parameters checked
live against `params/core.md`). The second half was not proven by the demo alone: `Adapter.canon_row`
was a required `str` with no `None`-handling anywhere in `harness.py`, so an adapter for a
proposed-but-not-yet-ratified mechanic would have crashed on its first resolver call — silently
contradicting the "insert/swap in/plug in provisional test code" requirement this proposal was built to
satisfy. `canon_row: str | None = None` now has a real, first-class, harness-recognized path (a
deliberate, logged opt-out — see `Adapter.canon_row`'s docstring), independent of `contract_module`'s
existing nullable axis, and every trace event now carries an explicit `canon_status: "verified" |
"provisional"` field so a provisional run's numbers can never be mistaken for canon-verified ones. See
`tools/sim_harness/README.md`'s "Provisional adapters" section for the worked pattern (a sketch, not a
shipped adapter — the next real provisional adapter is follow-on work, not part of this ratification).

---

## 11. Open questions for Jordan (the loud exception)

Per CLAUDE.md §2's ratification rule, this section is called out prominently because it is a genuine
engineering-process/CI-architecture decision, not routine work that should ride in on a merge:

1. **Does the rollout order in §8 match your priorities?** Mass battle has the largest raw coverage gap
   (1905 LOC, zero dedicated tests) but is deliberately sequenced *after* three smaller subsystems here —
   flag if that tradeoff should reverse.
2. **Should Wave 1's CI job block on introduction, or must it go through the full report-only burn-in
   like every other checker has?** This proposal defaults to the existing ratchet convention; a faster
   path would be a deliberate deviation from it.
3. **`mc_v18.py` as the final, tier-3-only adapter** — is a full-campaign harness run something you want
   gating PRs at all, given campaign runs are the slowest and highest-blast-radius target in the repo?
4. **The four quick wins in §9** are cheap and independent of everything else here — fine to action them
   in the same PR as this proposal, or do you want them filed as separate lane work rather than bundled
   with a PROPOSED architecture doc?
