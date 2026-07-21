# The Observatory — Holonic Refactor into Assay / Atlas / Augur

## Status: PROPOSED — HELD FOR JORDAN. Architecture + issue-resolution proposal for the vector-audit / ripple observability tooling. Nothing here is ratified; the P2 and validation changes below are explicitly loud-not-silent (ED-1094) and must not be auto-adopted on merge.

**Date:** 2026-07-21
**Lane:** IN (cross-cutting observatory)
**Class:** design (tooling architecture) — no game-canon change
**Supersedes:** nothing; *reorganizes* `skills/valoria-vector-audit/scripts/{vector_audit,ripple_audit,structure_audit,formula_audit,pointer_audit,gen_audit}.py` under one contract.
**Source:** the 2026-07-21 vector-audit session + its three adversarial passes (an opus critic on `ripple_audit`, a ground-truth backtrace that refuted the run's own P2 verdict, and a self-review that found the tool mixes code entities into a prose corpus and conflates three different jobs).

---

## 1. Motivation — one tool doing three jobs badly

The observatory grew by accretion into a single pipeline that silently conflates **three jobs with three different trust profiles**:

1. an **audit** (verdicts that could gate merges),
2. a **connectivity/observability** tool (navigate how anything connects to everything), and
3. a latent **design-hypothesis** surface (Mode B "implied-but-missing", surprising impact paths).

Conflating them produced every issue the session surfaced: a *validation verdict* (P2 FAILED) that was an instrument artifact; a *connectivity* query sold as *causal* impact; *code entities* scored in a *prose* corpus; and a drift toward *auto-generating and auto-gating work* — a measurement instrument acting as a control system on its own noisy signal.

The fix is **holonic**: split the tool into three components, each a self-contained whole with its own contract and output (callable alone), that also compose into the larger whole (callable in sequence) over **one shared substrate**. Crucially, the three holons differ in *how much autonomy they may be trusted with*, and the architecture must encode that difference rather than hide it.

**Governing principle (non-negotiable):** *the Observatory informs judgment; it never replaces it.* The loop is `observe → human → act → observe`, never `observe → act → observe`. The human is the damping term. Auto-generation and auto-gating are the failure mode, not the goal.

---

## 2. Architecture

```
                    ┌─────────────────────────── THE OBSERVATORY ───────────────────────────┐
                    │                                                                        │
   shared body →    │   SUBSTRATE: the Corpus Graph                                          │
                    │     • token universe, each token homed  ∈ {prose, code, unbuilt}       │
                    │     • unified graph = prose G_cite (influence-oriented)                │
                    │                     ∪ code/contract graph (ripple)                     │
                    │                     ∪ measured bridge edges (confidence-tagged)         │
                    │     • persisted as a committed artifact (reproducible; provenance-stamped) │
                    │                                                                        │
   three holons →   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐              │
                    │   │  A · ASSAY   │   │  B · ATLAS   │   │  C · AUGUR   │              │
                    │   │  (audit/gate)│   │ (observe/nav)│   │ (hypothesize)│              │
                    │   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘              │
                    │          │ verdict.json     │ atlas.json       │ questions.json       │
                    └──────────┼──────────────────┼──────────────────┼──────────────────────┘
                               ▼                  ▼                  ▼
                         gates (Tier 3,       on-demand human   ranked design
                         validated only)      navigation        QUESTIONS (never tasks)
```

Each holon reads the substrate and writes **one machine-hookable artifact**. Loose coupling via artifacts means each runs standalone; sequential composition is just "next holon reads the previous artifact." A holon never mutates the corpus and never calls another holon's internals — only its artifact.

### 2.1 Substrate — the Corpus Graph (built once, shared by all three)

The single source of truth all holons consume. Resolves the deepest issues at the root:

- **Three-home token model (resolves A6, A7).** Every token carries `home`, assigned by **actual presence**, not scale:
  - `prose` — appears in the ≥1 design `.md` (paragraph_count > 0);
  - `code` — appears in `module_contracts.yaml` / sim (a Key, mechanic, derivation value);
  - `unbuilt` — in *neither* (e.g. the `Muster`/`March` actions with no `domain_actions` home yet, ED-FA-0002; a `doc:null` module with no sim).
  `both` is allowed (an attribute like `Charisma` is prose *and* code). A token is scored *only* in the graph that can see it. **`unbuilt` is a first-class signal, not noise** — it is the honest coverage boundary (see §2.4).
- **Unified graph with reconciled direction (resolves A1).** `G_cite`'s `A→B` = "A depends on B"; the contract's producer→consumer = "M influences N" — *opposite* orientations. The substrate picks ONE canonical **influence** orientation (`source → influences → target`) and inverts `G_cite` into it, so a cross-graph walk means one consistent thing. This is a **semantic re-version of every directional claim** (Mode A "change-impact", Mode D "sinks" re-read) and therefore a versioned change, not a quiet reorder.
- **Measured, multi-signal bridge (resolves the bridge fuzziness + names the scale fork).** Token↔module joined by three signals, best-first: (a) normalized name match, (b) shared design doc, (c) `canonical_sources` system-key↔doc. Every bridge edge is **confidence-tagged**; the substrate emits a **bridge-coverage report** ("N/27 modules bridged; unbridged: engine_clock[doc:null], …"). Bridge precision is **hand-validated on a ~15-pair sample before any holon trusts a cross-graph result** — if precision is low we stop, because a cross-graph query on a bad join invents connections. **Default granularity is module-level** (a Key query lands on its module); reaching finer (key-level) requires consuming `structure_audit`'s G_code, an explicit, deferred option — not silently taken (avoids §8 duplication).
- **Reproducible + reused (resolves A2, §8).** The graph is built from the working tree and **persisted as a committed artifact** with a provenance stamp (head SHA, token count, bridge coverage), so a clean clone can run Atlas/Augur without a prior local run. Reuses `names.py`, `structure_audit.build_l2`, `formula_audit.build_contract_edges`, `broken_dependency_checker._resolve_remap`, `vector_audit.banner_classify` — no rule re-derived.
- **Bounded cost (resolves the O(n²) runtime).** Prose-absent identifier tokens (Keys, cross-module value-identifiers) are excluded from the prose `G_cite` build (they can never match prose) and live only in the code graph — which both fixes A6 *and* caps the quadratic prose pass. Full-run target < 30s.

### 2.2 Holon A — ASSAY (the audit / gate face)

**Job:** measure corpus health and emit verdicts, under strict gate discipline. **Trust profile: gates are earned, not assumed.**

- **Runs P1/P2/P3 + symmetry probes** over `home=prose` tokens only (code entities are not prose-isolates).
- **Fixes P2 (v4, held for Jordan).** The current P2 is structurally unsatisfiable: convictions route through the aggregate `conviction_track` slug in `throughlines_meta_infill.md`, so their throughline-degree is permanently `[0,…,0]` → `cv=999` → FAIL by construction. Fix = measure conviction symmetry on the axis where convictions are represented (cite), **and** fix the `mean==0 → cv=999` sentinel to report *not-measurable* rather than *asymmetric*. **Before adopting, re-derive the conviction cite-CV with the capitalization-noise check (A8)** — the CV=0.11 figure came from a subagent and was never independently verified for common-word tokens (`Order`, `Faith`).
- **Gate discipline — Tier 3 admission test (resolves the Goodhart trap).** A metric may *gate* only if it is (i) **validated** (measures the thing it claims), (ii) **direction-of-goodness known** (we can say which way is better), and (iii) **non-gameable** (no cheap way to satisfy it that degrades the corpus). **Today almost nothing qualifies**, and the Assay says so: symmetry-CVs, notional counts, and "drift meters" ship **report-only** until they pass the test. A "drift meter" whose good direction is undefined (more edges ≠ more coherent) is *not* a gate — that is the exact P2 error and the Assay must refuse to repeat it.
- **Symmetry as report, not gate (resolves A4/A5).** Conviction / attribute / four-bloc symmetry are surfaced with their noise caveats and their *intended-or-not* ambiguity labeled; they are **candidates for gates, not gates**. (The four-bloc win-probability symmetry is a **sim-layer** invariant — the Assay cross-references it to the balance harness and does *not* pretend to measure win-rate from a documentation graph.)
- **Output:** `verdict.json` — each metric with `{value, tier: gate|report, direction_known: bool, caveats[]}`.

### 2.3 Holon B — ATLAS (the connectivity / observability face)

**Job:** answer "how is X connected to everything" on demand. **Trust profile: high — pull-based, human-initiated, no autonomous action, no Goodhart surface.** This is the highest day-one value for a single maintainer and the first thing to build.

- **Directional impact query (resolves A1).** Over the influence-oriented unified graph: `--impact X --direction {affected-by | depends-on}`. "affected-by" = what changes when X changes (the true blast radius); "depends-on" = X's provenance. No longer the undirected connectivity walk the session shipped.
- **Blast radius + path**, ranked by graph distance, with the bridge crossings shown (so a result reveals when it left prose and entered code).
- **Three-home coverage map** — the live "real vs implemented vs aspirational" view (prose / code / unbuilt per subsystem).
- **Reverse-impact / orphan-simulation** ("if I delete X, what orphans?") and **diff-mode** (before/after a change → which connections appeared/vanished — a structural review aid).
- **Surprise flagging, validated (resolves A3).** The "far + cross-subsystem" flag is calibrated against the measured path-length distribution and reported *with its basis*, not asserted.
- **Output:** `atlas.json` + on-demand CLI. Never emits tasks or gates.

### 2.4 Holon C — AUGUR (the design-hypothesis generator)

**Job:** surface latent structure as **questions for the designer**, never as tasks. **Trust profile: lowest autonomy — every output requires human judgment, by construction.** This is the reframing the adversarial pass earned: the tool's highest use is provoking the design questions no one thought to ask, not queuing work.

- **Hypotheses, not tasks.** Mode B ("Clocks↔Victory is structural but unwritten") and surprising impact paths ("Clocks→Factions→Key→Game Director") are emitted as *questions*: "intended mechanic or accident?" — each with its evidence and its **ambiguity explicitly labeled**.
- **The `unbuilt` set as candidate questions, NOT a backlog (resolves the "backlog verbatim" overreach).** An isolate means one of three things — **author it / delete it (vestigial) / it is correctly deferred** — so Augur presents each unbuilt entity as a triage question with those three options, never as an auto-generated ED. It *ranks* candidates (by blast radius, by whether they gate M1) but the human decides author/delete/defer.
- **Contradiction detection.** A pair that is *both* Mode B (metadata-linked, uncited) and Mode C (cited, unsupported) is a genuine inconsistency worth a question.
- **Human-in-the-middle enforced.** Augur writes questions; a human answers them; answers become ledger entries or edits *by the human*. Augur never files an ED or edits a doc. This is the damping term that keeps the observatory from thrashing as a control loop.
- **Output:** `questions.json` — ranked, evidenced, ambiguity-labeled design questions.

---

## 3. Composition (holonic: individual + sequential)

- **Individually:** `observatory assay` · `observatory atlas --impact X` · `observatory augur` — each builds/reads the substrate and runs alone.
- **Sequentially:** `assay → atlas → augur`. Assay's `home`-partition and validity flags refine what Atlas maps; Atlas's reachability + coverage feed Augur's hypotheses. Each stage consumes the prior stage's *artifact*, not its code.
- **Substrate-once:** all three share one built Corpus Graph (cached artifact), so a full sequential run builds the graph once. A holon called alone builds (or loads the cached) substrate itself.
- **Holonic property satisfied:** each holon is a *whole* (own contract, own artifact, runnable standalone) and a *part* (composes upward into the Observatory), over a shared *body* (the Corpus Graph).

---

## 4. Issue-resolution matrix (everything the session's adversarial passes found)

| # | Issue | Resolved by |
|---|---|---|
| A1 | impact query undirected, sold as causal | Substrate §2.1 direction reconciliation + Atlas `--direction` |
| A2 | reads gitignored `data/` — not reproducible | Substrate: graph persisted as committed provenance-stamped artifact |
| A3 | surprise threshold arbitrary/unvalidated | Atlas: calibrate against measured path-length distribution, report basis |
| A4/A5 | symmetry CVs noisy; documentation-weight ≠ importance | Assay: symmetry is **report-only** with caveats; not a gate |
| A6 | code entities scored in a prose corpus → false isolates | Substrate: three-home model; prose metrics on `prose` tokens only |
| A7 | hardcoded action list; prose-absent tokens inflate | Substrate: actions homed `unbuilt`; identifier tokens excluded from prose graph |
| A8 | conviction CV=0.11 unverified (common-word noise) | Assay: re-derive with capitalization-noise check **before** P2 flip |
| A9 / scope | merges + scope creep muddied the PR | Clean holon boundaries + one-artifact-per-holon contract |
| Goodhart | symmetry-as-gate gameable / assumes symmetry always wanted | Assay Tier-3 admission test; gates earned, most metrics report-only |
| Control-loop | tool auto-generating + auto-gating work → thrash | Augur human-in-the-middle; `observe→human→act`, never `observe→act` |
| P2 | unsatisfiable-by-construction; `mean==0→cv=999` sentinel | Assay P2 fix (v4, held for Jordan) |
| Bridge | fuzzy join; `doc:null` gaps; scale-mismatch | Substrate: multi-signal + confidence + coverage report + validated sample; module-granularity ceiling; G_code deferred |
| Perf | O(n²) prose pass at 276 tokens (~1m38s) | Substrate: prose-absent identifier tokens excluded from `G_cite` |
| "backlog verbatim" | isolates ≠ tasks (author/delete/defer) | Augur: unbuilt as ranked triage *questions* |

---

## 5. Phasing (value-first, fail-fast, non-breaking-first)

0. **Substrate three-home tagging + Atlas coverage map** — *non-breaking, zero methodology change, highest value/risk.* Immediately retires the false-isolate findings (A6) by disclosure and stands up the trustworthy Tier-1 navigation. **Ships first, alone.**
1. **Direction reconciliation + directional impact query (Atlas core).** The prerequisite that unblocks honest blast-radius; re-derive the symmetry CVs in the same stroke (A8).
2. **Measured bridge + cross-graph Atlas.** Gated on the hand-validated precision sample — *fail here, not at the demo*.
3. **Assay P2 fix + Tier-3 gate discipline** — the v4 methodology change, to Jordan, loud, with before/after numbers.
4. **Augur** — hypotheses + unbuilt-as-questions, once Atlas's graph is trustworthy.

If only Phase 0 ships, the tool stops lying about orphaned Keys and gains on-demand navigation — so it is the floor.

---

## 6. Held back for Jordan (loud, per ED-1094 / §2)

- **The P2 redefinition + `mean==0` sentinel fix** (flips a published verdict FAILED→VALIDATED; touches locked validation).
- **Any Assay change that alters P1 medians** by excluding code tokens (show before/after).
- **Whether `unbuilt` entities are authored, deleted, or deferred** — Augur only *asks*; the ruling is Jordan's.
- **Elevating any symmetry probe to a Tier-3 gate** — only after it passes the admission test and the noise re-derivation.
- **The four-bloc win-probability gate** belongs to the sim/balance harness (§7's unmonitored ~87% degenerate win-share), not the graph Assay — flagged as a parallel, separate proposal.

## 7. Non-goals

- Not a control system: the Observatory never edits the corpus, files a ledger entry, or gates on an unvalidated metric.
- Not a prose parser of `.py`: code connectivity comes from `structure_audit`/contracts, consumed — not re-derived.
- Not a replacement for judgment: it makes the design *legible*, then gets out of the way.
