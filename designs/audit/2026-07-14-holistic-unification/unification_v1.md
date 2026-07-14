# Holistic Unification — WS0 Observatory + WS1 Registry, reconciled against the Five North Stars

## Status: PROPOSED (audit synthesis; ED-IN-0065, 2026-07-14)

This document is the single reconciled record of the WS0 (Structural Observatory) + WS1 (registry
reader) increment built across 2026-07-13/14, subjected to a **holistic adversarial pass** (five
independent read-only critics, tiered per CLAUDE.md §10 — four Sonnet on bounded surfaces, one Opus on
program coherence) whose findings are dispositioned here as **FIXED-in-this-pass** or
**TRACKED-for-Jordan**. It supersedes nothing; it indexes what is true now. Per ED-1094, merging this
doc ratifies its dispositions unless a line is marked *held back*.

The governing program is `/root/.claude/plans/…patterson.md` — repository realignment to five North
Stars: **NS1** human legibility, **NS2** pointer-based data / one vocabulary, **NS3**
repo-structure-mirrors-code-architecture, **NS4** v40 transition, **NS5** Godot portability.

---

## 1. What exists (built + merged)

| Surface | State | Files |
|---|---|---|
| **L0 prose layer** | runnable pipeline (110 design docs, 176 registry-derived tokens, P1/P2/P3 validation → FAILED 1/3, a real finding) | `skills/valoria-vector-audit/scripts/vector_audit.py` |
| **G_code + L2 module wiring** | AST import graph (173 modules, 268 edges, 3 cycles, 14 cut-vertices) + 27-module Key IN/OUT closure (6 dangling emits, 9 `doc:null`) | `…/structure_audit.py` |
| **G_pointer** | registry-resolution meter — see §3 for the honest reading | `…/pointer_audit.py` |
| **L1 formula DAG** | contract + descriptor dependency graph (30 nodes, 25 edges) — now with cross-module cycle detection | `…/formula_audit.py` |
| **G_generation** | live-vs-historical currency partition | `…/gen_audit.py` |
| **WS1 registry reader** | genuine read-only facade over `names`/`descriptor_registry`/`quantity_registry` (no §8 violation), + new bare-structural-key coverage | `tools/registry.py` |
| **WS1 target/analysis docs** | both **PROPOSED**, unexecuted migration + pointer-debt worklist | `references/registry/{README,pointer_debt_worklist}.md` |
| **Test coverage** | 140 observatory+registry tests green | `tests/valoria/test_{vector,structure,pointer,formula,gen}_audit.py`, `test_registry.py` |

**Merged:** PRs #132 (observatory), #135 (audit reconciliation batch 1), #137 (batches 2–4), plus the
ED-IN-0063 ratification. This document + its fixes are the follow-up increment (ED-IN-0065).

---

## 2. The headline finding: the instrument violated its own cardinal rule

The observatory's governance contract states, verbatim, **"never a silent cap — every exclusion
logged."** The adversarial pass proved this **false in 2 of the 5 scripts** — the exact "sophisticated
structure presented as verified truth" failure the plan's own Observatory-verdict warned is *"its own
worst failure mode."* This was the most important result of the pass, and it is now **fixed**:

| # | Defect (verified against the working tree) | Disposition |
|---|---|---|
| Obs-1 | `vector_audit.py` Mode C sliced `[:25]` **before** any total was recorded — true count (~9.3k notional edges) destroyed; scorecard read "25" as complete | **FIXED** — records `C_notional_total`, discloses "… N more" |
| Obs-2 | `structure_audit.py` `section()` dropped rows with no "… N more" line (87 import-orphans, 20 shown) unlike its sibling scripts | **FIXED** — parity disclosure added |
| Obs-3 | `vector_audit.py` `write_outputs` `section()` same bug (Mode B 34→20); Mode D total absent from the scorecard entirely | **FIXED** — totals recorded + disclosed; scorecard gains a `cascade-sinks` field |

**Verdict retained:** the "measures, never gates" claim itself **survived** adversarial grep — no
observatory output is wired into the branch-protected CI gate. That governance claim is true; the
"never a silent cap" claim was not, and now is.

---

## 3. The meter integrity correction (NS2's real number)

`G_pointer`'s headline "**52.7% resolved**" was an overstatement by ~2.4×. `resolve()` returns
matched-not-None even for a `not_descriptors` entry — a name the registry *deliberately declines to
key* (tracks/clocks/derived values: `Mandate`, `Treasury`, `CI`, …). Counting those as "resolved"
answers "did the name match anything," not the question the tool is named for: **does it point to a
registry KEY.**

- **True keyed pointer rate: 12/55 = 21.8%** (now reported alongside the 52.7% matched rate).
- **Category A's 45.8%→52.7% gain was text editing, not registration** — 6 shorthand strings deleted
  and replaced with already-resolvable spellings, 2 known display-names added; **zero** previously-
  unresolved identifiers were newly registered. Legitimate hygiene, but not debt paid down.
- **Asymmetry exposed:** a `not_descriptors` match scored as *success* while a structurally-identical
  "computed/internal, no key needed" quantity scored as *failure* — the only difference being whether
  someone had already typed the name into a YAML list.

**FIXED:** `pointer_audit.py` now reports **keyed vs matched vs declared-non-pointer** side by side;
`pointer_debt_worklist.md` carries both honesty corrections. Treat **keyed** as the NS2 meter.
Category-A provenance was independently re-verified as **real (no fabrication)** — that part is clean.

---

## 4. Fixing my own fig-leaves (findings F & H from the prior Fable-5 reconciliation)

The prior reconciliation (ED-IN-0063) resolved two findings by *disclosure*. This pass showed both
disclosures were weaker than presented; both are now **real fixes**:

- **Finding F (formula cycle):** the live Mandate↔Legitimacy feedback (`faction Mandate (cross-module
  → faction_state)` emitted, `faction Mandate` consumed) was disclosed as an undetectable "lower
  bound." The `_loose_form()` machinery to catch it already existed. **FIXED** — `formula_audit.py`
  now runs a second **paren-normalized cycle pass** (raw identity preserved everywhere else;
  collapse-induced self-loops dropped) and correctly reports
  `faction Mandate → set.legitimacy → set.popular_support`.
- **Finding H (§8 L2 closure disclosure):** my disclosure claimed the module-adjudicator is a
  "per-module gate" and this layer needs a "corpus-wide" view — but `contract_adjudicator.adjudicate()`
  **already runs corpus-wide**, and my layer is not equivalent (it *skips* all wildcard consumes the
  adjudicator resolves via family-inhabitance). **FIXED** — the disclosure now states the honest truth:
  a strict-subset, registry-unaware, corpus-wide **measure** that will *miss* any wildcard-only closure
  defect; true single-sourcing (import `adjudicate()`) is the tracked end-state, blocked only because it
  returns prose verdicts, not the structured edge list this graph needs.

Also fixed this pass: **Obs-6** `deprecated/` was content-substring-matched (would wrongly *drop* a live
doc citing a deprecated path) → path-anchored; **Obs-8** `formula_audit` cycle list now `sorted()` for
determinism parity; **Obs-9** `pointer_audit` resolved-buckets truncation disclosed. **Test defects**
(vacuous status test, decorative symmetry assertion, dead `ip_track` assertion, trivial determinism
assertion) replaced with mutation-catching tests; the silent-cap fixes, keyed split, paren-cycle, and
path-anchoring are each pinned. **140 tests green.**

---

## 5. The Five North Stars — honest state

The sobering coherence finding: this is **one genuine WS0→WS1 increment**, not seven moving
workstreams. Only **one** end-to-end seam is live: `G_pointer` → pointer-debt worklist → contract
canonicalization. The other four observatory layers **measure** NS3/NS4 gaps that nothing has yet
closed.

| NS | Real movement this program | Honest state |
|---|---|---|
| **NS1 legibility** | the observatory + this doc | **thin** — the two highest-leverage artifacts (`REPO_MAP.md`, `head_pointers.yaml`) do **not exist** |
| **NS2 pointers/vocab** | `G_pointer` drove a real (if small, and over-stated — §3) contract cleanup; `registry.py` facade built | **genuine but early** — true keyed rate 21.8%; no `vocabulary.yaml`, no `ci_vocabulary_consistency`; facade has **zero production consumers** |
| **NS3 structure↔architecture** | `structure_audit` *measures* scale-mismatch | **scaffolding only** — no reorg folders, no `REPO_MAP.md`; **dammed** behind un-started `scale_hierarchy_v1.md §6` propagation |
| **NS4 v40** | `gen_audit` *measures* currency drift | **scaffolding only** — no `_v40` file, no `head_pointers.yaml`, no rename tooling |
| **NS5 Godot** | protected as a constraint; no rename touched the port | **intact, untouched** — a guardrail, not a build target this session |

**Single biggest risk (unchanged, now recorded):** NS3 — the largest legibility payoff — cannot even
*begin* until `scale_hierarchy_v1.md §6` territorial-tier propagation is authored (settlement→territory→
province tiers don't yet exist in prose), a task that is **un-started, un-owned, un-scheduled** *and*
gated on Jordan ratifying a contested taxonomy. If it stays "tracked, not executed," the visible NS1
win never lands and `structure_audit` measures a gap nothing closes.

---

## 6. Highest-leverage next action (converges four critics)

**Generate `references/head_pointers.yaml` + `docs/REPO_MAP.md` from `canonical_sources.yaml` +
`CURRENT.md`.** Rationale the pass converged on:

- Both are **Phase-1, deterministic (haiku-tier), and unblocked** — by Jordan *and* by the §6
  propagation dam.
- `head_pointers.yaml` is the pointer indirection the registry facade conspicuously does **not**
  provide: it lets a doc cite "the current combat head" instead of decoding `_v1`-vs-`_v30`, directly
  serving NS1+NS2+NS4, and gives `G_generation` its **first real downstream consumer** (today 4 of 5
  observatory layers have none).
- `REPO_MAP.md` is the largest human-legibility win obtainable with **zero folder churn and zero
  ratification**.

Together they convert the observatory from "measures the gap" to "closes a gap" — the thing this
program has done exactly once (the pointer-debt slice) and needs to do more of, *before* any further
audit-of-audit or the blocked reorg.

---

## 7. Tracked for Jordan (design/scope calls — not unilaterally resolved)

1. **Pointer-debt Category B** — register the genuinely-unregistered scalars (`Wounds`, `Turmoil`,
   `Accord`, `Poise`, `Initiative`, …); each needs a canonical key + home-doc verification (§5
   anti-fabrication). This is the actual debt-closing work.
2. **Category C2** — are `npc_behavior`'s `beliefs`/`concerns`/`projects`/`arc state` registry
   quantities at all, or relational/psychological state outside the scalar registry? (Removing them
   would drop up to 5 identifiers from the denominator — a meter move with no registry work, so decide
   it explicitly.)
3. **`settlement_layer` `Legitimacy / Popular Support` derivation** (`module_contracts.yaml`) — a
   Mandate-feedback drift *loop* with **no `bucket:` tag**: is it a `derived_value` or a track-write?
   Its sibling derivations are tagged; this one isn't, and a reader can't tell whether it computes a
   distinct value or rewrites the base track. (The dropped `(Mandate feedback)` annotation, Meter-3,
   is the surface symptom.)
4. **Observatory CI-refresh decision** — the pipeline is runnable now (the old "it's a stub" rationale
   in `audit-refresh.yml` was stale and is corrected), but it is wired nowhere and persists no
   scorecard, so it risks going stale like the `drift=304` predecessor it replaced. Decide whether a
   monthly **non-gating** refresh job persists scorecards, and where.
5. **Registry migration + `sim/` reconciliation + the Phase-2 taxonomy** — all remain PROPOSED and
   Jordan-gated (unchanged).

---

## 8. Latent risks logged (not yet manifesting — do not treat as closed)

- `pointer_audit` formula-local exclusion keyed `(module, identifier)`, not `(derivation, identifier)`
  — over-excludes if one name is a formula-local in one derivation and a genuine input in another of
  the same module (0 instances today; logged, so auditable, never silent).
- `quantity_registry.resolve()` is a global, context-blind string match — two unrelated concepts in
  different scales sharing a short word (`Order`, `Level`) could silently resolve to the wrong key (0
  collisions today).
- `vector_audit.py`'s analytical core (`diagnostics()` Modes A–H, `validate()` P1/P2/P3) still has **no
  known-answer coverage** beyond the new Mode-C total pin — the classifier and one diagnostic are
  tested; the payload is not.
- A "strictly decreasing pointer-debt" CI gate would be **gameable/noisy** (bundling conventions and
  ordinary new-quantity authoring move the denominator) — if ever wired, gate on **keyed** count with
  disclosed exclusions, never a raw monotonic %.

---

*Method note: the five critics were dispatched as isolated read-only Agent relays (agonist→antagonist,
per CLAUDE.md §10 / holonic doctrine ED-1083) — none saw another's reasoning; reconciliation happened
only on the orchestrator window. Every finding above was verified against the working tree before
disposition; nothing here is inferred from a docstring.*
