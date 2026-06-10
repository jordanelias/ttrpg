---
name: valoria-module-adjudicator
description: >
  Module-contract adjudicator for the Valoria engine architecture. Treats every game
  system/mechanic as a module wrapper — IN(consumed Keys) → resolver → OUT(emitted Keys)
  plus owned, bucket-classified state — records each wrapper's contract in
  references/module_contracts.yaml, and actively enforces conformance with
  scripts/contract_adjudicator.py (checks A1–A9): emit/consume closure against the Key
  Type Registry, derived-value write protection, cross-scale edge coverage via the
  scale_transitions handoff rules, module-graph loop annotation, and registry self-checks.
  Produces per-module and whole-graph verdicts mapped to NERS and the canonical
  "all directions" definition. ALWAYS use this skill when checking whether a system is
  keyed/wired correctly, whether inputs/outputs close over the registry, or whether the
  interdependency graph holds across scales. Trigger on: "module contract", "wrapper
  conformance", "is this system keyed", "input/output keys", "adjudicate the
  architecture", "interface audit", "key wiring", "interdependency check", "does the
  graph close", "scale coverage", "enforce the wrappers", or when the orchestrator
  routes an architecture-conformance task.
---

**Prerequisite:** Bootstrap complete — `assert_bootstrap()` via `quick_bootstrap()` before invoking. This skill reads canonical architecture docs; never adjudicate from memory or chat-session maps. Fetch this session, index-first: `designs/architecture/key_substrate_v30.md` (§2.3, §4.1, §4.6, §8), `designs/architecture/key_type_registry_v30.md`, `designs/architecture/scale_transitions_v30.md` (§3, §5), `designs/scene/derived_stats_v30.md` (§1, §11, §14 — PROPOSAL status; re-verify before relying), plus the target module's canonical doc via `references/canonical_sources.yaml` lookup.

**Model:** Opus (whole-graph cross-referencing); Sonnet acceptable for single-module Stage 1 extraction.

**Naming note (collision guard):** "armature" is a canonical term (Conviction armature, `armature_position`, Faction Meta-Armature — key_substrate §8.2). This instrument is therefore the *adjudicator*, never "the armature." It audits modules that *use* the Conviction armature; it does not modify that system.

**Relationship to sibling skills.** `valoria-mechanic-audit` checks a system's *internal* consistency; `valoria-resolution-diagnostic` checks *resolution and balance fitness under stress* (NERS verdict on behavior); `valoria-vector-audit` checks the *corpus* (vocabulary, isolates). This skill checks the *seams*: whether each system honors its wrapper contract and whether the contracts compose into one closed, scale-coherent graph. Run mechanic-audit first on an unverified system; run this when the question is "do the modules wire together, in all directions and at all scales."

---

## WHY THIS SKILL EXISTS

The engine's architecture commitment (key_substrate §1, §4.1) is that **everything consequential crosses system boundaries as a Key under the single update rule** — `validate → append → observers interpret → consume → causal edge`. The architecture fails silently in four ways: a system emits a type the registry never defined (the F2 class); a system has no outcome type at all and its results vanish at the seam (the F3 class); a writer mutates a derived aggregate directly instead of routing the delta to its substrate (the F1/Mandate class, derived_stats §11); and a cross-scale effect travels out-of-band instead of through a scale_transitions §3 handoff or §5 Domain Echo. None of these is visible inside any single system doc — they live *between* docs. This skill makes the seams first-class objects (contracts), makes the contracts machine-checkable (the assessor script), and makes the check repeatable per commit (the proposed gates in Stage 4).

---

## THE MODULE CONTRACT (load-bearing — read first)

Every system/mechanic at every scale is recorded as one **module wrapper**:

```
IN (consumed Key types) → resolver (archetype) → OUT (emitted Key types)
                          owns: state quantities, each bucket-classified
                          crosses scales only via declared transitions
```

Contract record (one per module, in `references/module_contracts.yaml`):

| Field | Values | Grounding |
|---|---|---|
| `module` | snake_case name | — |
| `doc` | canonical design-doc path | must appear in `canonical_sources.yaml` (check A8) |
| `scales` | one or more of `personal · scene · settlement · territory · provincial · peninsula · thread` | `[ASSUMPTION: enum from PI scale framing + designs/ tree + Key scale_signature examples — Jordan-confirmable; unknown values are warnings, not violations]` |
| `resolver` | `dice_pool · d_sigma · deterministic_accounting · clock_advance · armature_dot_product · state_reader · manifest` | five archetypes per the 2026-06-09 engine map; `state_reader`/`manifest` cover Victory and clock_registry degenerate forms. `[ASSUMPTION — same basis]` |
| `consumes[]` | `{type, from: [modules] or engine}` | Key types exactly as canon writes them |
| `emits[]` | `{type, terminal: bool}` | `terminal: true` = deliberately unconsumed (e.g., telemetry) |
| `state[]` | `{name, bucket: pool·derived_value·track·clock, writable: bool}` | derived_stats §1/§11/§14 buckets |
| `transitions[]` | `{via: "scale_transitions §3.x …" or "§5 Domain Echo"}` | required when any edge crosses scales |
| `loops[]` | `{with: module, damper: …, cap: …}` or `[OPEN — Jordan]` | resolution-diagnostic Lesson 5 discipline at graph level |
| `status` | `extracted · stub` | `stub` = pointer only; **no edges may be invented for a stub** |
| `sources[]` | `[READ:]-grade citations for every extracted edge | honest-findings discipline |

**The quantity buckets are not interchangeable with the resolution-diagnostic's three categories.** That skill's continuous-resource / discrete-accumulator / base-parameter taxonomy classifies *behavior under stress*; the four buckets here (derived_stats) classify *write legality*. A quantity carries both classifications; conflating them produces false findings in both skills.

---

## STAGE 0 — SCOPE

Operator provides: one module, a scale slice (e.g., "everything at scene scale"), or `full graph`. Resolve target docs via `canonical_sources.yaml`. Run `h.task_gate('audit')` for adjudication work; `('infrastructure')` for registry-maintenance-only work.

## STAGE 1 — EXTRACT (bottom-up, per module)

For each in-scope module:
1. Index-first read of its canonical doc (`read_index` → `read_sections`); cross-check key_substrate §8's integration statement for that system. Emit `[READ:]` per source.
2. Record the contract **exactly as canon states it** — emit/consume type strings verbatim, including types canon names but the registry lacks (those are findings, not transcription errors to silently fix).
3. Bucket-classify each owned quantity from derived_stats §11/§14; where the doc predates the bucket taxonomy, classify from observed write paths and flag `[ASSUMPTION]`.
4. A module whose doc cannot be located gets `status: extracted` only if every edge is grounded in another canonical source (e.g., key_substrate §8); otherwise `status: stub` with **zero** edges. An extracted module with no located home doc carries a `[GAP: doc path]` note (assessor warning W-DOC).

**Never** seed a contract from a chat-session map, a handoff summary, or memory. Canon over recollection — the 2026-06-09 session's F2 list included an emit string the current canon does not contain; transcribing canon, not the chat, is what caught that.

## STAGE 2 — ADJUDICATE

**Machine pass** — run the assessor:

```
python3 skills/valoria-module-adjudicator/scripts/contract_adjudicator.py \
    --contracts references/module_contracts.yaml \
    --registry  designs/architecture/key_type_registry_v30.md \
    --sources   references/canonical_sources.yaml
```

Exit 1 on any violation; warnings alone exit 0. Fixture suite at `tests/contracts/test_contract_adjudicator.py` — run it after any assessor change.

| Check | Verdict class | What it catches |
|---|---|---|
| A1 schema validity | violation | malformed contract records |
| A2 emit-closure: every emitted type is registered | violation | **F2 class** — unregistered emissions |
| A3 consume-closure: consumed type registered AND produced by ≥1 module or `engine` | violation | reads of nothing |
| A4 orphan emission: non-terminal emit with zero consumers | warning | dead-letter outputs; **F3 surfaces here** as a missing-emit gap note |
| A5 derived-write guard: `bucket: derived_value` + `writable: true` | violation | **F1 class** — direct aggregate writes (route to substrate; derived_stats §11) |
| A6 cross-scale edge where neither endpoint module declares any `transitions` entry | violation | out-of-band scale crossings (module-level existence check; whether the cited handoff fits *this* edge is J2's question) |
| A7 module-graph cycle lacking a `loops[]` damper/cap annotation | violation | undamped+unbounded loops at graph level (Lesson 5) |
| A8 extracted module's `doc` absent from canonical_sources | violation (W-DOC warning when doc is an explicit `[GAP]`) | contracts detached from canon |
| A9 registry self-check: §9 declared family counts vs parsed type_ids | warning | registry-internal drift (the 37-vs-38 / section-vs-prefix housing finding, 2026-06-09) |

Family is always derived from the `type_id` **prefix**, never from the registry section a type is housed under (§8 of the registry houses Class-B types outside their count families).

**Judgment pass** — what the script cannot check:
- **J1 bucket fitness:** is each quantity's bucket *right* (a "track" that only climbs is a clock; a stored "pool" is a violation of pool semantics)?
- **J2 transition semantics:** does the cited §3 handoff actually carry this edge's payload, or is the citation decorative?
- **J3 necessity:** is every edge load-bearing (NERS-N)? An edge nothing reads and a type no system emits are both removal candidates — over-coupling is a defect, same as under-coupling.

Apply the resolution-diagnostic's **intent gate** before flagging: a deliberate, safeguarded coupling with design-doc statement passes; accidental or intent-undetermined couplings are findings.

## STAGE 3 — VERDICT

Per module and for the whole graph, verdict-first, severity-ranked, no false balance:

```
MODULE: <name>   STATUS: extracted|stub   RESOLVER: <archetype>
VERDICT: CONFORMANT | NON-CONFORMANT — <one-line reason>
  A-findings: <violations, then warnings>
  J-findings: <judgment items>

GRAPH VERDICT: CLOSED | OPEN — <emit/consume closure %, cross-scale coverage, cycle table>
ALL-DIRECTIONS COVERAGE (canon/definitions.yaml):
  lateral/horizontal (same-scale edges): <count, gaps>
  vertical (cross-scale via §3/§5):      <count, gaps>
  top-down (aggregate → substrate reads): <…>
  bottom-up (substrate → aggregate recompute; A5 guards the inverse): <…>
  diagonal (cross-scale AND cross-family): <…>
NERS MAPPING: S — scale transitions + clean inter-module interaction; R — complete,
error-free wiring; N/E — no redundant edges or types (J3). A passing lint is
necessary, not sufficient, for NERS; behavioral compliance stays with
valoria-resolution-diagnostic.
```

Output: `designs/audit/<YYYY-MM-DD>-module-adjudication/verdict_<scope>.md`. Derived views (flowchart, state graph, flattened pipeline map) are regenerated into the same directory by `scripts/contract_flowchart.py --contracts ... --registry ... --outdir ...` — generated artifacts, never hand-edited. P1/P2 findings that are canonical gaps go to `canon/editorial_ledger.jsonl` via `append_to_register` — compute the next ED id at append time (parallel sessions assign concurrently; the class-#12 collision is live).

## STAGE 4 — ENFORCE & RE-TEST

1. Remediation routes through the owning canon mechanism: unregistered type → registry §10 extension process (Class-B vetting); derived-write → derived_stats §11 conversion; missing handoff → scale_transitions §3 amendment proposal; unannotated loop → damper/cap design (Lesson 5). Mechanical-tier calls need bottom-up + top-down anchors, logged, Jordan-vetoable; creative-layer items escalate.
2. Update `references/module_contracts.yaml`; re-run the assessor until violations = 0 or each residual is `[OPEN — Jordan]`.
3. **Standing hook proposals** (per architecture `<migration_and_growth>`; proposed, not built — building requires tests + spectrum-table + PI updates in the same change):
   - Level 3: pre-commit grep cross-checking emit-type literals in `designs/**` against parsed registry type_ids (the 2026-06-09 R2 candidate).
   - Level 4 co-file: `designs/architecture/key_type_registry_v30.md` ↔ `references/module_contracts.yaml` — a registry change without a contract reconciliation (or vice versa) fails commit.
   - Level 4: `contract_gate()` wrapping the assessor's `adjudicate()` for `task_gate('design')` entry.

---

## GUARDRAILS

- **Stubs stay empty.** A stub with invented edges is fabrication; a stub is a to-do, not a contract.
- **Honest nulls.** A module that passes everything is reported `CONFORMANT` with its trail — examined-and-sound is a finding; do not pad.
- **Canon over chat.** Prior-session maps and handoffs are leads, never sources. Every edge cites a `[READ:]` from the current session.
- **The script is subordinate to canon.** If the assessor and a canonical doc disagree, the doc wins and the script (or the contract) is the defect — fix it; never `--force` past it.
- **Scope the enums.** The `scales` and `resolver` enums are `[ASSUMPTION]`-grade until Jordan ratifies; the assessor treats unknown members as warnings so a wrong enum cannot false-halt work.
- **RuntimeError from any hook = hard halt.** Report verbatim, stop. (Read-ordering errors from `read_sections` prescribe their own remedy — index first — which is compliance, not bypass.)
