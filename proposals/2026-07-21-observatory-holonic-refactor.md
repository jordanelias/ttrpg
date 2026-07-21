# The Observatory — Holonic Refactor into Assay / Atlas / Augur

## Status: PROPOSED (r2) — HELD FOR JORDAN. Architecture + issue-resolution + operations proposal for the vector-audit / ripple observability tooling. Nothing here is ratified; the P2 and validation changes below are explicitly loud-not-silent (ED-1094) and must not be auto-adopted on merge.

**Date:** 2026-07-21 (r2 same day — see Revision log)
**Lane:** IN (cross-cutting observatory)
**Class:** design (tooling architecture) — no game-canon change
**Supersedes:** nothing; *reorganizes* `skills/valoria-vector-audit/scripts/{vector_audit,ripple_audit,structure_audit,formula_audit,pointer_audit,gen_audit}.py` under one contract, and *integrates with* (not replaces) `tools/observability/build_graph.py`, `tools/review_core.py`, `tools/audit_staleness.py`, and the dashboard.
**Source:** the 2026-07-21 vector-audit session + its adversarial passes (an opus critic on `ripple_audit`, a ground-truth backtrace that refuted the run's own P2 verdict, a self-review that found code entities scored in a prose corpus, and an r1→r2 pass that found r1 duplicating four existing infrastructure surfaces).

---

## 1. Motivation — one tool doing three jobs badly

The observatory grew by accretion into a single pipeline that conflates **three jobs with three different trust profiles**:

1. an **audit** (verdicts that could gate merges),
2. a **connectivity/observability** tool (navigate how anything connects to everything), and
3. a latent **design-hypothesis** surface (Mode B "implied-but-missing", surprising impact paths).

Conflating them produced every issue the session surfaced: a *validation verdict* (P2 FAILED) that was an instrument artifact; a *connectivity* query sold as *causal* impact; *code entities* scored in a *prose* corpus; and a drift toward *auto-generating and auto-gating work*. The r1 draft of this proposal then repeated the repo's other classic failure — designing new apparatus that duplicates existing single-owner infrastructure (§4).

The fix is **holonic**: three components, each a self-contained whole with its own contract and artifact (callable alone), composing into the larger whole (callable in sequence) over **one shared substrate** — with the three holons *differing in how much autonomy they may be trusted with*, and the architecture encoding that difference.

**Governing principle (non-negotiable):** *the Observatory informs judgment; it never replaces it.* The loop is `observe → human → act → observe`, never `observe → act → observe`. The human is the damping term. This applies to the refresh pipeline itself (§5): even the scheduled freshness run lands as a branch a human merges.

---

## 2. Architecture

```
                 ┌────────────────────────────── THE OBSERVATORY ──────────────────────────────┐
                 │                                                                              │
  shared body →  │  SUBSTRATE: the Corpus Graph (composes EXISTING layers; owns nothing twice)  │
                 │    prose G_cite (influence-oriented) ∪ build_graph payload (systems/Keys/    │
                 │    scalars) ∪ structure_audit L2/G_code ∪ formula_audit L1 ∪ pointer_audit   │
                 │    G_pointer ∪ measured bridge edges (confidence-tagged)                     │
                 │    • every token homed ∈ {prose, code, unbuilt}                              │
                 │    • deterministic build-on-demand (no committed blobs); small committed     │
                 │      SUMMARY (counts + provenance stamp) for staleness/dashboard             │
                 │                                                                              │
  three holons → │  ┌────────────┐      ┌────────────┐      ┌────────────┐                      │
                 │  │ A · ASSAY  │      │ B · ATLAS  │      │ C · AUGUR  │                      │
                 │  └─────┬──────┘      └─────┬──────┘      └─────┬──────┘                      │
                 │        │ review_core       │ atlas.json +      │ questions.json +            │
                 │        │ SIGNALS           │ dashboard bundle  │ dispositions memory         │
                 └────────┼───────────────────┼───────────────────┼─────────────────────────────┘
                          ▼                   ▼                   ▼
                   the ONE existing      on-demand human     ranked design QUESTIONS
                   verdict rollup        navigation + Pages  (never tasks; new/changed only)
```

### 2.1 Substrate — the Corpus Graph

The single source all three holons consume. **It is a composition point, not a parser** (CLAUDE.md §8): every layer comes from its existing owner — `vector_audit`'s prose `G_cite`, **`tools/observability/build_graph.py`'s payload** (the systems/Keys/scalars propagation graph the dashboard console already renders), `structure_audit`'s L2/G_code (modules tracing), `formula_audit`'s L1 DAG and `pointer_audit`'s G_pointer (primitives tracing), joined by bridge edges. Root fixes:

- **Three-home token model (resolves A6, A7).** Every token carries `home`, assigned by **actual presence**, not scale: `prose` (appears in ≥1 design `.md`), `code` (appears in `module_contracts`/sim — resolved via `tools/quantity_registry.resolve()` and the definitions store, not a new presence rule), `unbuilt` (in *neither* — e.g. the `Muster`/`March` actions pending `domain_actions`, ED-FA-0002; `doc:null` modules with no sim). `both` allowed. A token is scored *only* in the graph that can see it. **`unbuilt` is a first-class signal** — the honest coverage boundary, which is also the authoring frontier (§2.4).
- **One reconciled influence direction (resolves A1).** `G_cite`'s `A→B` ("A depends on B") and the contract producer→consumer ("M influences N") are *opposite*; the substrate inverts `G_cite` into one canonical `source → influences → target` orientation. This re-reads Mode A "change-impact" and Mode D "sinks" — a **versioned semantic change**, not a quiet reorder.
- **Measured, multi-signal bridge.** Token↔module joined by (a) normalized name, (b) shared design doc, (c) `canonical_sources` system-key; every edge **confidence-tagged**; coverage reported ("N/27 bridged; unbridged: engine_clock[doc:null], …") and **cross-checked against `references/wiring_manifest.yaml`** (the 27/27-module wiring surface `review_core` already validates). Precision hand-validated on a ~15-pair sample **before** any holon trusts a cross-graph result. **Granularity:** module-level for Keys; **value-level precision comes free from the already-composed L1/G_pointer layers** (this partially resolves r1's scale-mismatch fork); descending Keys below module level via G_code stays an explicit deferred option.
- **Determinism over blobs (REVISES r1; resolves A2 correctly).** r1 proposed committing the graph artifact — but this very session showed committed graph data tripping the names-drift lint (`tokens.json` → "EventImpact") and bloating diffs. Instead: the substrate is **deterministic, working-tree-only, build-on-demand** (measured baseline ~1m38s at 276 tokens; identifier tokens excluded from the O(n²) prose pass caps it — budget ≤2 min, fine for any workflow). What *is* committed is a **small canonical-name summary** (`observatory_summary.json`: counts, coverage, verdict tiers, provenance stamp = head SHA + token/edge counts) — the thing staleness tracking and the dashboard actually need. The full graph is *published* (Pages/data bundle), never committed.

### 2.2 Holon A — ASSAY (audit face) — **feeds review_core; is not a second aggregator**

**Job:** measure corpus health under strict gate discipline. **Trust profile: gates are earned, not assumed.**

- **Registers as `review_core.py` signals** (`observatory.assay`, tier `report_only`) — the Repository State Armature (ED-IN-0077) stays the *single* verdict rollup behind the banner, the CI job, and the artifact. Assay inherits review_core's existing **baseline/regression machinery** (`review_baseline.yaml`) instead of inventing its own.
- **Fixes P2 (v4, held for Jordan).** Current P2 is unsatisfiable by construction (convictions route through the aggregate `conviction_track` slug → throughline-degree permanently `[0,…,0]` → `cv=999`). Fix: measure conviction symmetry on the axis where convictions are represented (cite), and make the `mean==0` sentinel report *not-measurable*, never *asymmetric*. **Precondition:** re-derive the conviction cite-CV with a capitalization-noise check (A8 — the CV=0.11 figure was never independently verified for common-word tokens like `Order`, `Faith`).
- **Tier-3 gate admission test (resolves the Goodhart trap).** A metric may *gate* only if it is (i) validated, (ii) has a known direction-of-goodness, (iii) is non-gameable. **Today almost nothing qualifies and the Assay says so**: symmetry CVs, notional counts, drift meters ship report-only with caveats and their *intended-or-not* ambiguity labeled. (The four-bloc win-probability symmetry is a **sim-layer** invariant for the balance harness — cross-referenced, not faked from a documentation graph.)
- **Output:** the review_core signal payload (each metric `{value, tier, direction_known, caveats[]}`), summarized into `observatory_summary.json`.

### 2.3 Holon B — ATLAS (connectivity/observability face) — **extends the dashboard, not a new UI**

**Job:** answer "how is X connected to everything" on demand. **Trust profile: high — pull-based, human-initiated, no autonomous action.** Highest day-one value; first build.

- **Directional impact query** over the influence-oriented unified graph: `--impact X --direction {affected-by | depends-on}` — true blast radius vs provenance, with bridge crossings shown and the surprise flag calibrated against the measured path-length distribution (resolves A1/A3).
- **Three-home coverage map** — the live "documented / implemented / aspirational" view per subsystem.
- **Dashboard integration:** publishes via `obs_core.py`'s existing `window.VALORIA_X` JS-bundle writer as `window.VALORIA_OBSERVATORY`; `tools/dashboard_data.py` gains a `build_observatory()` section beside `build_workplan`/`build_audits`/`build_currency`; the coverage map and per-entity connectivity **complement the ED-IN-0079 "By value" browse surface** (each value page links to its dependencies/dependents) and the existing `console.html` graph viewer (which keeps rendering `window.VALORIA_GRAPH`; long-term unification of the two graph payloads is a held decision — §6).
- **Diff-mode** (before/after a change → connections appeared/vanished) as a later optional PR-comment surfacing; **reverse-impact** ("if I delete X, what orphans?").
- **Output:** `atlas.json` + on-demand CLI. Never emits tasks or gates.

### 2.4 Holon C — AUGUR (design-hypothesis face) — **questions with memory, never tasks**

**Job:** surface latent structure as **questions for the designer**. **Trust profile: lowest autonomy — human judgment required by construction.**

- **Hypotheses, not tasks.** Mode B pairs ("Clocks↔Victory is structural but unwritten") and surprising impact paths become *questions* — "intended mechanic or accident?" — each with evidence and ambiguity labeled. The `unbuilt` set surfaces as ranked **triage questions** with exactly three answers — **author / delete (vestigial) / defer (intended)** — never as auto-generated EDs.
- **Question memory (resolves the scheduled-noise failure).** Every question gets a **stable ID** (hash of kind + entities + evidence shape). Human answers live in `references/observatory_dispositions.yaml` (`{id: {answer, note, date}}` — the same forward-only disposition discipline the vector-audit SKILL already mandates for findings). On each run Augur diffs against dispositions and **surfaces only new or materially-changed questions**, capped top-N by rank. A scheduled Augur without this is a noise machine that trains the human to ignore it.
- **Register boundary (no duplication):** `DECISIONS.md` = marker-level debt; `PROPOSALS.md` = unratified docs-by-location; **Augur = latent-structure questions** — a third, disjoint register. Augur never files an ED, never edits a doc; answers become ledger entries *by the human*.
- **Output:** `questions.json` (+ the dispositions file it reads).

---

## 3. Composition (holonic: individual + sequential)

- **Individually:** `python tools/observatory.py assay | atlas [--impact X] | augur` — a **thin dispatcher in `tools/`** (so CI/workflows call `tools/`, per the §8 invariant) that imports the skill-owned scripts; each verb builds or loads the substrate and runs alone.
- **Sequentially:** `observatory all` = substrate once → Assay → Atlas → Augur, each consuming the prior stage's *artifact*, never its internals.
- **Holonic property:** each holon is a whole (own contract, own artifact, standalone) and a part (composes upward), over a shared body (the substrate).
- **Deterministic and model-free:** no LLM/agent calls anywhere in the pipeline — Augur's questions are templates over graph evidence. This is what makes scheduled runs free, reproducible, and safe.

---

## 4. Integration with existing infrastructure (NEW in r2 — the layer r1 missed)

| Existing surface | Observatory relationship |
|---|---|
| `tools/review_core.py` (ED-IN-0077, the single verdict aggregator) | Assay = new **signals** (`observatory.assay`, report_only), baselined via `review_baseline.yaml`. Never a parallel rollup. |
| `tools/observability/build_graph.py` + `graph.json` + `console.html` (`window.VALORIA_GRAPH`) | Substrate **consumes** its payload as the systems/Keys/scalars layer. One-builder unification is a held decision, not a silent takeover. |
| `tools/audit_staleness.py` | The **registered-but-empty `vector-audit` slot (ED-IN-0032)** becomes the Observatory's freshness signal, keyed on `observatory_summary.json`'s provenance stamp — the SessionStart banner then shows observatory staleness like every other audit. |
| Dashboard (`tools/dashboard_data.py`, `dashboard.yml`, ED-IN-0079 values surface) | `build_observatory()` section in `data.json`; `window.VALORIA_OBSERVATORY` bundle via `obs_core.py`'s writer; coverage map + questions panel; per-value connectivity linked from the "By value" pages. |
| `references/audit_registry.jsonl` (+ size caps in `ci_register_size_check`) | **Manual/skill runs append** (SKILL.md mandate, unchanged). **Scheduled runs do NOT append** — freshness is the staleness tracker's job; an append-per-cron would grow the register into its own CI cap. |
| Primitives tracing (`pointer_audit` G_pointer, `formula_audit` L1) and modules tracing (`structure_audit` L2/G_code, `wiring_manifest.yaml`) | Consumed as substrate layers; the A17/wiring **gates stay where they are** — the Observatory measures, never re-gates. |
| `DECISIONS.md` / `PROPOSALS.md` (audit-refresh outputs) | Augur is the disjoint third register (latent-structure questions); refreshed by the same workflow, same cadence. |

## 5. Freshness & operation (NEW in r2)

- **Workflow:** extend **`.github/workflows/audit-refresh.yml`** with an `observatory` job (same monthly `cron` + `workflow_dispatch`), running `observatory all` and refreshing: `observatory_summary.json`, the dashboard bundles, and `questions.json`. It **commits to a branch and pushes** exactly as the existing refresh does — the refresh itself lands as a PR a human merges, preserving the damping term even in automation. `dashboard.yml` publishes the full graph payload to Pages on merge (published, not committed).
- **Failure semantics:** the observatory job is **report-only and never part of the `All Gates Green` needs list**. Promoting it to blocking is a held-for-Jordan decision that would follow the Tier-3 admission test, not precede it.
- **Cadence honesty:** monthly + on-demand dispatch; between runs the staleness banner (§4) tells every session exactly how stale the observatory view is — the same contract every other audit surface already has.
- **No new hand-maintained registry:** freshness derives from git facts (the staleness tracker's design principle), the summary's provenance stamp, and the dispositions file (which is human-authored by definition).

## 6. Issue-resolution matrix (all passes: session A1–A9 + r1→r2)

| # | Issue | Resolved by |
|---|---|---|
| A1 | impact query undirected, sold as causal | §2.1 direction reconciliation + Atlas `--direction` |
| A2 | reads gitignored `data/` — not reproducible | **r2 revision:** determinism + committed *summary* + published graph (r1's committed-blob answer retracted — it re-created the lint/bloat failure) |
| A3 | surprise threshold arbitrary | Atlas: calibrated against measured path-length distribution |
| A4/A5 | symmetry CVs noisy; doc-weight ≠ importance | Assay: report-only + caveats + intended-or-not labeling |
| A6 | code entities scored in a prose corpus | §2.1 three-home model |
| A7 | prose-absent tokens inflate; O(n²) cost | §2.1 identifier exclusion from the prose pass; ≤2 min budget |
| A8 | conviction CV=0.11 unverified | Assay precondition: re-derive with capitalization-noise check |
| Goodhart | symmetry-as-gate gameable | Tier-3 admission test; gates earned |
| Control-loop | tool auto-generating/auto-gating work | Augur human-in-the-middle; branch-PR refresh (§5) |
| P2 | unsatisfiable by construction | Assay v4 fix, held for Jordan |
| Bridge | fuzzy join; `doc:null` gaps; scale fork | Multi-signal + confidence + wiring-manifest cross-check + validated sample; L1/G_pointer give value-level precision |
| **r2-1** | r1 substrate duplicated `build_graph.py` (a 4th graph) | Substrate composes its payload; unification held for Jordan |
| **r2-2** | r1 Assay duplicated `review_core` (2nd verdict surface) | Assay = review_core signals; one rollup |
| **r2-3** | scheduled Augur with no memory = noise machine | Stable question IDs + dispositions file + new/changed-only + top-N cap |
| **r2-4** | no freshness/trigger/loop design | §5: audit-refresh job, branch-PR commits, staleness slot, Pages publish |
| **r2-5** | per-run registry appends vs size caps | Scheduled runs don't append; manual runs keep the SKILL mandate |
| **r2-6** | dashboard/values-surface complement unstated | §4: `build_observatory()`, `window.VALORIA_OBSERVATORY`, ED-IN-0079 linkage |
| **r2-7** | nothing barred LLM calls in a cron pipeline | §3: deterministic, model-free by contract |

## 7. Phasing (value-first, fail-fast, integration-from-day-one)

0. **Substrate three-home tagging + Atlas coverage map + integration floor** — non-breaking; ships with the dashboard section, the staleness slot keyed on `observatory_summary.json`, and the `tools/observatory.py` dispatcher. Retires the false-isolate findings by disclosure. **Ships first, alone.**
1. **Direction reconciliation + directional impact query**; re-derive the symmetry CVs (A8) in the same stroke.
2. **Measured bridge + cross-graph Atlas** — gated on the hand-validated precision sample and the wiring-manifest cross-check; *fail here, not at the demo*.
3. **Assay as review_core signals** (report-only) + the P2 v4 packet to Jordan with before/after numbers.
4. **Augur** with question memory + dispositions.
5. **Held-for-Jordan closures:** P2 flip, any gate promotion, `build_graph`/substrate unification, whether the observatory job may ever block.

If only Phase 0 ships: the tool stops lying about orphaned Keys, gains on-demand navigation, and is already fresh-tracked and dashboard-visible — so it is the floor.

## 8. Held back for Jordan (loud, per ED-1094 / §2)

- The **P2 redefinition + `mean==0` sentinel fix** (flips a published verdict; touches locked validation) — preceded by the A8 noise re-derivation.
- Any Assay change that **alters P1 medians** (show before/after).
- **`unbuilt` dispositions** — Augur only asks; author/delete/defer is Jordan's ruling per entity.
- **Elevating any symmetry probe to a Tier-3 gate**; **making the observatory workflow blocking**.
- **Unifying `build_graph.py` with the substrate** (one graph builder, two views) — a consolidation on the ED-IN-0068 pattern, decided explicitly, not absorbed silently.
- The **four-bloc win-probability** gate (sim/balance harness; §7's unmonitored ~87% degenerate win-share) — separate proposal.

## 9. Non-goals

- Not a control system: never edits the corpus, files ledger entries, or gates on unvalidated metrics.
- Not a second verdict aggregator, graph builder, or debt register — review_core, build_graph, DECISIONS/PROPOSALS keep their jobs.
- Not a prose parser of `.py` and not an LLM pipeline: code connectivity comes from the existing tracers; questions are templates over evidence.
- Not a replacement for judgment: it makes the design *legible* — including its own staleness — then gets out of the way.

---

## Revision log

- **r1 (2026-07-21):** initial three-holon architecture + session issue matrix.
- **r2 (2026-07-21):** adversarial pass on r1. Retracted the committed-graph-artifact design (recreated the session's own lint/bloat failure); substrate redefined as a composition of the existing layers incl. `build_graph.py` (r1 was building a fourth graph); Assay redefined as `review_core` signals (r1 was a second verdict surface); added Augur question memory + dispositions (scheduled noise), the freshness/operation section (audit-refresh branch-PR pattern, staleness slot ED-IN-0032, Pages publish, report-only job), the registry-append policy vs size caps, dashboard/ED-IN-0079 integration, and the model-free contract.
