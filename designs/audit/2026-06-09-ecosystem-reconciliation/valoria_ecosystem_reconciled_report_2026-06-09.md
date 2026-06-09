# Valoria — Ecosystem / Organisation / Data-Management Reconciled Report
**2026-06-09 · scope: full project, both repos · effort: max**

`[SELF-AUTHORED — bias risk: this consolidates analysis lines that prior sessions (incl. sessions I ran) produced. Mitigation: every load-bearing claim below is re-verified against live `main` this session with a `[READ:]` handle; where my own prior output was wrong, it is struck here by name.]`

---

## VERDICT (first, no false balance)

**The ecosystem is in materially good health and is *already governed by a consolidation plan that answers most of this request.*** A capstone **Master Workplan** dated **2026-06-06** exists in-repo (`designs/audit/2026-06-06-architecture-map/valoria_master_workplan.md`), is **Jordan-approved through Waves 0–1 + the K8 commission**, and **today's session has already executed 9 of its items** (W0.1, W0.3–0.5, W0.7, W0.8, W1.4, W1.5, W1.13). 

So the honest finding that reframes everything else: **this task is substantially the same task that 2026-06-06 scoped and today is executing.** Producing a fresh, parallel nth workplan would itself be the project's signature failure mode — artifact pile-up in competing states (`<document_consolidation>`). The correct deliverable is **reconciliation against the existing master + the delta of what it misses or what has drifted since**, which is what this report and its companion delta-workplan are.

**Net state by layer:**

| Layer | Health | One-line |
|---|---|---|
| Enforcement (hooks/ops) | **Strong** | Code is the authority and is ahead of the spec; 33 hook gates live; R4/R7 landed today. |
| External CI (Level 5) | **Now real** | `valoria-ci.yml` (7.3 KB) mirrors local gates outside Claude in both repos — the long-standing `[GAP]` is closed. |
| Editorial data | **Clean** | `editorial_ledger.jsonl`: 639 entries, **0 duplicate IDs**, ED-867 the only contested ID open. The "~94-ID-conflict backlog" is **resolved and stale**. |
| Spec/text accuracy | **Drifted (low sev)** | PI `<task_manifests>` + bootstrap-script step-3 still name deprecated YAML stores; live code uses JSONL. Cosmetic but recurring. |
| Repo organisation | **Drift, not disorder** | `designs/audit/` (431 files) is the live-design-in-audit-folder problem Jordan named 2026-06-05; promotion plan exists, not executed. |
| Handoff state | **Stale** | Both active handoffs carry struck claims (94-ID backlog, IDR pending). Consolidation/refresh overdue. |
| Bootstrap hot path | **Heavy, fix queued** | `canonical_sources.yaml` at interim 12 k cap; SHA-split (`canonical_freshness.yaml`) specced (W1.9), not built. |

---

## PART 1 — CRITIQUE (failure surface, severity-ranked)

### P1 — Two parallel "where are we" surfaces disagree, and the handoffs are the stale one
The roadmap (`roadmap_state.yaml`) was reconciled **today** (commit `aeaa87ff`): IDR struck, FR/d+σ confirmed canonical, ledger counts corrected. But **the two active handoffs were not** — `weapon-physics-stage2-2026-06-05` still lists *"~94-ID-conflict backlog, pull a clean ID"* and the index master still implies the IDR renumber is pending. 
- **Live truth (verified):** ledger has **0 duplicate IDs** across 639 entries; ED-865/866/868/874 all `resolved`; only **ED-867** (add `[SUPERSEDED-BY]` markers) is `open`. 
- **Defect:** a reader resuming from the handoff inherits a false backlog. This is the project's core failure mode (stale-state propagation) reproduced in its own coordination layer. 
- `[READ: editorial_ledger.jsonl ID-scan; roadmap_state.yaml pending_decisions; bootstrap active-handoffs report]` `[CONFIDENCE: high]`

### P1 — `canonical_sources.yaml` sits on the hot bootstrap path at its interim cap
Bootstrap fetches `canonical_sources.yaml` every session; it is **8,587 tokens against a raised-interim 12 k threshold** (was 9 k at 99.5%). It carries ~115 `canonical_sha` freshness fields that have nothing to do with the *declarations* bootstrap actually needs. 
- **Fix is specced** (W1.9 / roadmap 2.4): split the SHA fields → `references/canonical_freshness.yaml` (owner `tools/freshness_gate.py`), dropping the hot file to ~5 k. **`canonical_freshness.yaml` does not yet exist** (verified absent). 
- **Defect:** every bootstrap pays a ~3× token tax on a file whose bulk is cold data. `[READ: TOKEN_THRESHOLDS; tree key-path existence — canonical_freshness.yaml NO]` `[CONFIDENCE: high]`

### P2 — Spec/code text drift (PI + architecture vs live hooks)
Confirmed divergences where **code is authoritative** (architecture V2.5 conflict-rule #11):
- PI `<bootstrap_script>` step-3 lists `canon/editorial_ledger_summary.yaml` + `references/file_index_summary.md` as fetched paths. Live `quick_bootstrap` fetches **neither summary** — it uses `editorial_ledger.jsonl` and the SQL index. `editorial_ledger_summary.yaml` is **gone** (verified). 
- PI `<task_manifests>` lists `propose_mechanic` / `design_proposal` as requiring `editorial_ledger_summary.yaml`; the **live `TASK_REQUIRED_FILES` correctly uses `editorial_ledger.jsonl`.** 
- PI `<commit_convention>` describes M4 citation enforcement as "never built / soft-warn proposed." [CORRECTION: evening pass — whole-file scan of live `valoria_hooks.py` confirms the PI text is **correct**: no Citations-block regex exists in `pre_commit_gate`/`commit_message_gate`; L1980/L2001 are the sim fabrication scan and L2341–2375 is the context_gate 60% warn. M4 remains **unbuilt** (= register item W1.12). The morning draft of this report inverted the finding by misattributing those line ranges.]
- **Defect:** the governing text names files that are deleted (e.g. `editorial_ledger_summary.yaml` in the manifest list, vs the live `.jsonl`). Low runtime impact, high confusion cost, recurring. `[READ: valoria_hooks.py grep citation/soft_warn; quick_bootstrap fetch set; tree existence]` `[CONFIDENCE: high]`

### P2 — Live design work still lodged in `designs/audit/` (Jordan's 2026-06-05 flag, unexecuted)
`designs/audit/` holds **431 files across ~32 date-keyed dirs**; several are *active design surfaces* (combat-engine, contest-engine, weapon-physics), not closed audit logs. Jordan's own framing (2026-06-05): *iterative audit work where mechanics get improved is a flag that design work is occurring* — and `simulation`/`audit` folders should hold logs and ratified simulators, not living design. The promotion plan was catalogued; **not executed** (the session held for Jordan's pause). Two index-drift orphans persist (`weapon_axes_v2.md`, `ners_verdict_combat_v32.md` registered to no concept). 
- `[READ: tree family counts designs/audit=431; bootstrap index-drift report]` `[CONFIDENCE: high]`

### P2 — Three disconnected "where are we" / "what's open" computations, none unified
Open-item state is scattered across: `roadmap_state.yaml` (decisions), handoffs (per-stream blockers), the editorial ledger (`open` status × 55), and the master-workplan §1 register. **W1.1 (`report_open_items()` — a single typed, topological union) is specced and is the keystone fix, but not built.** Until it exists, every session re-derives "what's open" by hand and they disagree (P1 above is a symptom). `[READ: master_workplan §1; ops def inventory — no report_open_items]` `[CONFIDENCE: high]`

### P3 — Tooling duplication: superseded index generators co-resident with the SQL pipeline
`tools/` carries **`index_gen.py`, `doc_index_gen.py`, `mechanics_index_gen.py`** alongside the enshrined SQL pipeline (`regenerate_file_index.py` + `index_bootstrap.py` + `valoria_index.sql`). Architecture V2.5 declares the SQL pipeline the 2026-05-28 successor; the CI workflow still `py_compile`s `index_gen.py`. **Retirement bias-to-keep flagged but not actioned** (`<retirement>`). `[READ: tools/ inventory; valoria-ci.yml import list]` `[CONFIDENCE: high]`

### P3 — Reference-registry sprawl (16-of-18 with no Level-4 consumer), partially diagnosed
The 2026-06-04 audit found a heavily-overlapping registry cluster (`collision_registry`, `synonym_registry`, `alias_registry`, `glossary.md`, `mechanical_terms_index.md`, `scope_vocabulary.md`, `silo_overlap_matrix`, `orphan_terms_registry`, `mechanics_index.yaml`, …) with no in-session consumer. Some are Level-3 tool-consumed; the truly-orphaned subset was never isolated (the `tools/` grep was flagged as not-run). **Consolidation+retirement pass outstanding.** `[READ: prior-audit finding carried; not re-walked this session]` `[CONFIDENCE: medium — registry-by-registry consumer trace not re-run here; flagged GAP]` `[GAP: per-registry consumer trace — needs the tools/ grep the 06-04 audit deferred]`

### P3 — Deferred infrastructure subsystems (all specced, none blocking)
Carried in roadmap Phase 2 (0/11 done) and master-workplan W1.9–W1.12: SHA-split (W1.9), per-session-log subsystem D5 (W1.10), CI-subsystem documentation (W1.11), D6 scope-vocab unification (three disjoint scope sets: `TASK_REQUIRED_FILES` keys / `SESSION_SCOPES` / `COMMIT_FORMAT` regex — confirmed still disjoint this session). `[READ: roadmap current_phase=2; SESSION_SCOPES vs COMMIT_FORMAT vs TASK_REQUIRED_FILES — three sets]` `[CONFIDENCE: high]`

### NULL results (examined, clean — recorded for honesty)
- `[NULL: editorial_ledger ID-uniqueness — examined, 0 duplicates across 639 entries]` — the architecture/handoff "94-conflict" class is **resolved**, not live. 
- `[NULL: deprecated YAML editorial stores — examined, all absent]` — `editorial_ledger.yaml`, `_summary.yaml` correctly gone; JSONL is single-source. 
- `[NULL: CI external mirror — examined, present and substantive]` — `valoria-ci.yml` exists in **both** repos with real jobs (syntax, register-size, co-file, editorial, hooks-verifier). The standing `[GAP: Level-5 CI]` is closed. 
- `[NULL: branch-protection-blocks-commits (B6) — examined, 35 direct-to-main commits since 06-06]` — fully struck; D0 holds.

---

## PART 2 — PROPOSAL: one legible, modular, dynamic maintenance discipline

The project does not need a new architecture. It needs **one principle made load-bearing, three keystone builds, and a maintenance cadence** — all already named in the master workplan; this section states them as the *target operating model* so the delta-workplan has a spec to close against.

### The principle: **one computed source per question; everything else is generated or struck**
The recurring defect across every P-finding above is **the same fact maintained by hand in N places, drifting.** The fix is uniform: for each project question, name **one authoritative store**, and make every other view a **generated projection or an explicitly-superseded artifact** — never a hand-kept parallel.

| Question | Single source (target) | Projections (generated, never hand-kept) |
|---|---|---|
| "What's open / where are we?" | `report_open_items()` (**W1.1**, union over roadmap+ledger+handoffs, typed, topological) | Status Block line (W1.2); roadmap `items_done` auto-feed (W1.8) |
| "Is X canonical / what version?" | `canonical_sources.yaml` declarations only | freshness via `canonical_freshness.yaml` (**W1.9**, cold tier) |
| "What editorial decisions exist?" | `editorial_ledger.jsonl` (already single-source ✓) | any summary view = regenerated, not authored |
| "What files exist / index?" | `valoria_index.sql` via the SQL pipeline (already ✓) | retire the 3 legacy `*_index_gen.py` (P3 above) |
| "What's the descriptor taxonomy?" | `descriptor_registry.yaml` (**W1.13**, landed today) typed by KIND, partitioned by DOMAIN | consumers read the registry; multipliers become data-not-code |

**Modularity** is already correct at the engine layer (master-workplan §8: attribute-agnostic core, **one kernel / three regimes** — discrete-pool, continuous-Normal, d+σ — *not* a single universal resolver). The descriptor registry (W1.13) is the missing companion that makes the taxonomy itself modular and data-driven. Nothing here adds apparatus the project lacks a failure for; each build closes a specific live drift (NERS-N/E discipline).

### The three keystone builds (highest leverage, all specced, none built)
1. **`report_open_items()` (W1.1)** — collapses the three-disagreeing-surfaces defect into one computed answer. Every downstream "status" view feeds from it. *This is the single highest-leverage build in the project* — it structurally prevents P1-class drift rather than cleaning it up after.
2. **Freshness SHA-split (W1.9 / roadmap 2.4)** — creates `canonical_freshness.yaml`, drops the hot bootstrap file ~3×. Pure cost discipline on a path paid every session.
3. **Lifecycle state machine wired to commit primitives (W1.7 + supersession-citation check W1.6)** — makes "superseded → archived" a tracked transition, so the handoff/artifact pile-up (P1, and the consolidation rule itself) is enforced, not disciplined-by-hope.

### The maintenance cadence (cheap, recurring, mostly already wired)
- **Per session, at bootstrap:** Status Block emits `report_open_items()` + a **decision-aging line** (W1.2) so OWN-4/OWN-5-class decisions cannot silently rot. Freshness checks the ecosystem tier against `ecosystem_versions.yaml` (landed today).
- **Per commit:** the live gates already enforce co-file, size, naming, derived-write (R4), formula co-file (R7). CI mirrors them externally (now real). **No new per-commit apparatus needed.**
- **Drift discipline (standing):** when a hook changes, the matching PI/architecture text updates in the same change. The **P2 spec-text drift is the visible debt of this rule lapsing** — pay it down once (delta-workplan D-items) and hold the rule.
- **Consolidation (standing):** the moment >1 active handoff or any "which of these is current?" arises → collate→reconcile→one master. **This is overdue now** (2 stale handoffs) — delta-workplan T1.

---

## PART 3 — ADVERSARIAL REVIEW

*Attacking the report and proposal above as an independent reviewer would. Where an attack lands, it is carried into Part 4; where it fails, it is reported as survived (not salvaged).*

**A1 — "You're just rubber-stamping the 2026-06-06 plan because it's yours; that's the self-authored bias you flagged, not avoided."** 
*Partially lands.* The master workplan is prior-session output and I am endorsing its structure. Mitigation actually performed: I re-verified its load-bearing claims against live `main` independently (ledger scan, tree walk, hook grep, roadmap read) and found its §0 self-corrections *hold* and its register matches today's commits. But I did **not** independently re-derive whether the *engine-framing* (§8 "three regimes, no universal resolver") is correct — I accepted it. → **Carried: Part 4 records §8 as accepted-not-reverified, a residual bias.**

**A2 — "0 duplicate IDs is a snapshot, not a guarantee; the 94-conflict class could recur."** 
*Survives, with a caveat.* `assert_unique_ids` / `jsonl_ledger_gate` are live Level-4 hooks and CI mirrors ID-uniqueness, so recurrence is *gated*, not merely *currently-absent*. The honest residual: ID **collision across concurrent sessions** before commit is a coordination risk the gate catches at commit time, not before. → **No new finding; the gate is the answer. Noted in Part 4.**

**A3 — "'One source per question' is a nice slogan but `report_open_items()` is unbuilt vapor; you're proposing a target, not a fix."** 
*Lands hard, and is the point.* The proposal is explicitly a *target operating model*; the *fixes* are the delta-workplan items. Calling W1.1 the keystone while it's unbuilt is honest only if the workplan actually schedules it — it does (W1.1, P1, blocked only by W0.3 which is **done today**). → **Carried: delta-workplan must put W1.1 at the front, unblocked.**

**A4 — "You under-rate the `designs/audit/` problem as P2. Jordan named it the *major* issue. 431 files of living design in the wrong folder is a taxonomy failure, not hygiene."** 
*Lands.* I ranked it P2 on *runtime* impact, but on *legibility* impact — the explicit ask — it is closer to P1. The wiring is sound; the *filing* actively misleads (design work masquerading as closed audit). → **Carried: re-rank to P1-legibility in Part 4; delta-workplan promotes the folder-scheme fix.**

**A5 — "The registry-sprawl finding is P3 with a `medium` confidence and an admitted un-run grep. That's a sham-clear — you're parking work you didn't do."** 
*Lands, and is correctly a `[GAP]` not a `[NULL]`.* I did **not** trace each registry to its consumer; asserting "16-of-18 orphaned" inherits a prior session's claim. The honest status is *flagged, unverified* — which is what the tag says, but the severity should not imply it's understood. → **Carried: delta-workplan adds the consumer-trace as an explicit task before any retirement; no registry gets cut on an un-run grep.**

**A6 — "Your whole report assumes the master workplan's item IDs (W0.x/W1.x) as if canonical. If that doc gets superseded, your delta-workplan dangles."** 
*Survives.* The delta-workplan references master-workplan items *by content*, not only by ID, and its first task is to reconcile the two stale handoffs **into** the master — binding them, not forking. If the master is superseded, the delta folds into its successor by the same consolidation rule. → **No change; binding is deliberate.**

**A7 — "You claim CI 'closes the Level-5 gap' but you only read the workflow head and didn't confirm it runs green or that the jobs do what their names say."** 
*Lands.* I verified the workflow **exists and is substantive** (job names, external-enforcement framing, tool imports) but did **not** confirm a green run or read each job body. "Mirrors local gates" is inferred from job names + imported tools, not proven by a passing run. → **Carried: Part 4 downgrades to "present and substantive; green-run unverified"; delta-workplan adds a one-time CI-green confirmation.**

**A8 — "Over-engineering check: do W1.6/W1.7 (lifecycle state machine + supersession-citation hook) catch a real failure, or are they apparatus for apparatus's sake?"** 
*Survives.* The failure is live and named: artifact pile-up in competing states is the documented `<document_consolidation>` trigger, and it is **firing right now** (2 stale handoffs). A tracked supersession transition is the minimal mechanism that prevents it; it adds one hook + one state field, not a framework. NERS-N/E pass. → **No change.**

---

## PART 4 — RECONCILIATION (critical, unbiased)

Folding Part 3's landed attacks back in:

1. **Severity re-rank (A4):** the `designs/audit/` filing problem is **P1 on the legibility axis** the request foregrounds, even though it is P2 on runtime. Both are true; the report now states both and the delta-workplan treats folder-scheme promotion as a front-rank item, not deferred hygiene.
2. **Self-authored residual (A1):** the engine-framing §8 (three-regimes / no-universal-resolver) is **accepted from prior work, not independently re-derived this session.** This is a declared bias, not a verified claim. *It does not block the delta-workplan* (no delta-item depends on re-opening §8), but it is the one place a future independent audit should look first.
3. **Sham-clear corrected (A5):** registry sprawl is **`[GAP]`, not understood** — the consumer-trace was never run. The delta-workplan makes the trace a prerequisite to any retirement; **nothing is cut on an un-run grep** (`<retirement>` discipline + `honest_findings`).
4. **CI claim tempered (A7):** corrected throughout to **"present and substantive; green-run unverified."** A one-time green confirmation is a delta task.
5. **Keystone confirmed (A3):** `report_open_items()` (W1.1) is the single highest-leverage build and is **now unblocked** (its only dependency, W0.3 roadmap reconcile, landed today). It heads the delta-workplan.
6. **What survived (no change):** ID-uniqueness is gated not just snapshot-clean (A2); the master-workplan binding is deliberate (A6); W1.6/W1.7 are necessary not over-engineered (A8).

**Reconciled bottom line:** the project is **healthy, well-governed, and mid-execution on a plan that already answers this request.** The genuine outstanding work is (a) **reconcile the two stale handoffs into the master** [overdue, T1], (b) **build the three keystones** W1.1 / W1.9 / W1.6–W1.7, (c) **execute the `designs/audit/` promotion** [P1-legibility], (d) **pay down the P2 spec-text drift** in one pass, and (e) **run the deferred registry consumer-trace** before any retirement. Every Jordan-gated design decision (F1 calibration, C2 type-form, Composure name, OWN-4, OWN-5, D6, combat-v32 ratify, ED-868 bound) remains carried as `[OPEN — Jordan]`, untouched.

The companion **workplan (R2, superseding the same-day delta draft)** sequences exactly this, dependency-ordered, with nothing duplicated from what today already shipped.
