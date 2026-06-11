# Valoria — Master Workplan v3 (consolidated, three-lane)
**2026-06-10 · status: PROPOSED (Jordan-vetoable throughout) · as_of: ttrpg@695552e3 (HEAD this session; a parallel audit session is committing — re-pin on resume)**

**Supersedes:** `designs/audit/2026-06-06-architecture-map/valoria_master_workplan.md` (the Jordan-approved capstone — its approved content [methodology, Waves 0–1, the K8 commission] is **carried, not reopened**; W-item IDs stay citable) · `designs/audit/2026-06-09-ecosystem-reconciliation/valoria_workplan_R2_2026-06-09.md` (incl. its supersession of the uncommitted same-day delta workplan). The 2026-05-31 workplan-v2's **Three-Lane Operating Model survives as the operating frame** — it lives operationally in `references/lane_assignments.yaml`, whose `source:` pointer and entry queues this consolidation repoints to v3.
**Binds (does not fork):** `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md` (Lane C's governing spec) · `designs/audit/2026-06-10-module-adjudication/verdict_full_graph.md` + `module_map_flat.md` (canon-state inputs) · `references/module_contracts.yaml` v3 schema-2 (the shared spine).
`[SELF-AUTHORED — bias risk: every consolidated input except the verdict's §7 addendum was authored by my sessions. Mitigation: §0 records the adversarial scan per document, including where my own conversion strategy is already stale; each resolution cites live canon read this session.]`

---

## §0 — RECONCILIATION RECORD (adversarial scan + cross-interrogation, resolved with citations)

**Per-document scan (objective, worst finding first):**

| Doc | Verdict | What lands against it | Disposition |
|---|---|---|---|
| **Workplan R2** (live, post-`3da2d9a` approvals) | Sound frame; **stale carried-docket** | Three docket entries copied forward without the as-of verification R2 itself preaches: **combat-v32 ratify** is RESOLVED (roadmap `pending→resolved` [READ this session]; `canonical_sources` resolution_engine = CANONICAL combat_engine_v1, ED-900/904); **OWN-4** is RESOLVED (ED-881; roadmap reconcile `fb1a8af`); **OWN-5** is decided+BUILT (ED-1000/1001) — residual is SIM-DEFECT verification only. Also **A-1's task** (reconcile stale handoffs) was executed by the 06-09 consolidation (`80aa3ae`/`65e91c2`/`2a2ae53` handoff archives + `59622c0` consolidation master; live count = 1) — only its residual survives. | Frame, §0 constraints, budget rule, K-1/2/3, B-2 stop-rule, the approved C-1 trim + D-3 mechanism, and the Deferred/Triggered/Dropped/Principles sets **carry into v3**; docket de-staled in §5. |
| **Delta workplan** (uncommitted) | Superseded (Jordan + R2 header) | Its **D-2 claims M4 BUILT with line cites (L1980–2483)** — falsified by the evening whole-file hook scan (report `[CORRECTION]`; R2 B-3). Verified at code level this review: L1980–2483 is sim-fabrication + checkpoint + context-gate code (the `soft_warn` at L2341–2375 is the context-gate's 60% flag), not citation enforcement — the delta cited real lines but misread the mechanism; M4 stays unbuilt (→ LB-8). Unique TIER-5/S-x detail survives inside R2's Deferred set. | Fully subsumed; nothing carried directly. |
| **Ecosystem reconciled report** | Holds | Its own Part 3 adversarial pass already landed the durable caveats (engine-§8 accepted-not-reverified; CI green-run unverified → A-2; registry-trace `[GAP]` → R-1). Only its handoff-count snapshot aged (2→3→1 within a day) — which proves its own as-of lesson rather than breaking a finding. P1 "canonical_sources at the 12k hot-path cap" remains live (K-2 unbuilt; **6** stale SHAs at this bootstrap). | Findings carried; report stays valid analysis (not superseded). |
| **Module-adjudication verdict** | Sound; one as-of seam | It ran/records against **contracts v2.1** while **v3 (schema-2)** landed 65 min before its commit (`4eeabd8` 20:01 vs `8d8a208` 21:06). The F2/A6/W-DOC classes are version-robust, but the **A10–A12 surface (gates/derivations/accounting-sequence) has no recorded whole-graph verdict yet**; the flat map's "56 warnings" vs the verdict's re-run "58" is matching derived-view drift. §7's `registry_derived` proposal is already absorbed into ED-1009. | Verdict carried as canon-state; a one-call **v3-basis re-run** is queued (LB-5) and the flat map regens with it. |
| **Godot conversion strategy** (this session, `b42aa03`) | Stands as Lane C spec; **three errata within hours** | (a) cites adjudicator **A1–A9** → live is **A1–A12**; (b) cites contracts **v2** → live is **v3 schema-2**; (c) **Gate-0 G0.4's type set is the W3.4 subset** of what is now the consolidated ED-1009 registration decision (7 F2 types + F3 + 2 attribution rulings). | Strategy remains binding; §3 states the corrected Gate-0 inline (authoritative until the strategy's next touch folds the errata — LC-0c). Schema-2 **strengthens** the strategy: contracts now carry per-module gates+derivations, enriching the port packet (see joints below). |
| **README** (strategy companion) | Fine | Inherits the same three errata by reference. | Rides with LC-0c. |

**Cross-interrogation joints (what reading them together surfaces):**
1. **One docket, finally.** ED-1009's decision set ≡ strategy Part VIII items ≡ the R2 docket's live remainder. §5 is that single register; nothing is listed twice under different names.
2. **`module_contracts.yaml` is now the shared spine of enforcement *and* conversion.** v3's header makes the flowchart *read* contracts (single source); the strategy already generates TYPE_SUBSCRIPTIONS from contracts. Consequence: the verdict's proposed registry↔contracts co-file hook rises in value — queued behind the K-budget per R2's rule (LB-8).
3. **Schema-2 enriches the conversion unit.** Gates (A10) and derivations (A11) per module are exactly what a GDScript port must honor: the Lane-C ritual's "port against contract" step now transcribes contract gates/derivations too, and its check step becomes A1–A12-equivalent (§3 ritual note).
4. **The Accounting spine is the statechart.** Flat-map §4.2's nine-step canonical sequence (A12-checked) is the season superstate the strategy's Stage-1 statechart implements — Lane C consumes §4.2 verbatim (LC-2).
5. **D-3 boundary case #1 is de-facto split.** The voice-canon extraction (`d8eeab9`/`b25a08f` → `designs/world/narrative_voice_canon_v30.md`) executed the "split" option for articulation §4.2 — Jordan's confirmation closes it (J-3), and it simultaneously cleans the articulation module for its Wave-4 port.
6. **The Mandate↔L/PS loop is the first property-check seed.** ED-1008's contract-annotated §1.8 damper (saturating + mean-reverting) gives settlement_layer's first-port golden scenario its loop-gain assertion for free.
7. **Vocabulary guard.** "Lane A/B/C" = the operating lanes below (write-disjoint sessions + reserved ID blocks). Distinct from: assessor checks (A1–A12), R2 phase items (A-1…D-3), the VG drift census (D1–D8), and ED ID-lanes. v3 item IDs are lane-prefixed (**LA-/LB-/LC-/J-**) to stay out of every existing namespace.

`[NULL: contradictions between the verdict's per-module findings and the strategy's Part-II dispositions — examined row-by-row, none found; the strategy's wave/blocker columns already encode the verdict's NON-CONFORMANT causes.]`

---

## §1 — OPERATING MODEL (carried; v3 changes queues, not structure)

Three write-disjoint lanes per `references/lane_assignments.yaml` (owns-globs, reserved ED/PP blocks, launch protocol, boundary rule — **all carried unchanged**). Constraints carried from R2 §0: one operator; sessions are the currency; **Lane B WIP = 1**; per-system rituals ride with feature work, never as standalone phases; **budget rule** — no new structural proposal advances while K-1/K-2/K-3 are unbuilt; hooks detect · the model interprets · Jordan decides.

- **Lane A — Canon / Editorial / Design-content** (`editorial`/`design` scope; ED 890–939, PP 727–759).
- **Lane B — Infrastructure / Tooling / Governance** (`infrastructure` scope; ED 940–969, PP 760–779).
- **Lane C — Simulation / Implementation** (`simulation`/`godot` scope; ED 970–999, PP 780–799; owns `sim/**` + the **valoria-game repo** — collision-free with A/B). **Lane C's governing spec is the conversion strategy**; Gate-0 → spine → waves per §3.
- **The Decision Docket (§5) is not a lane** — it is the Jordan-gated register every lane parks against (launch-protocol step 7: park, note, continue).

Lanes run concurrently; a consolidation session (like this one) operates under the sole master handoff, outside lane declaration, and is the only context that edits the lane file itself.

---

## §2 — LANE B QUEUE (Infrastructure / Tooling / Governance · WIP = 1 · single file, in order)

Carried from R2 Phases A–D with live status; the verdict's three hook proposals queue **behind the K-budget** (R2 rule). `5.3-class` full-file restructures of shared infra stay **solo-window** (lane-file rule).

| ID | Item | Provenance / status | Gate |
|---|---|---|---|
| LB-1 | `write_handoff` gains an `as_of: <SHA>` header line (handoff staleness becomes mechanically visible) | R2 A-1 **residual** — A-1's body was executed 06-09 (`80aa3ae`/`65e91c2`/`2a2ae53` + `ebfdd10`; 1 active handoff live) | — |
| LB-2 | One green CI run confirmed per repo, jobs spot-read | R2 A-2 (report adversarial A7) | — |
| LB-3 | Roadmap micro-reconcile (post-06-10 commits) + the `ecosystem_versions.yaml` adjacent-model note | R2 A-3 + §1 residual | — |
| LB-4 | **K-1: `report_open_items()`** co-built with W1.2 (Status-Block decision-aging) + W1.8 (roadmap auto-feed) | R2 A-4; the every-session keystone | — |
| LB-5 | **Adjudicator whole-graph re-run on contracts v3** (one call, ED-1008 model) + regen derived views (closes the flat-map 56-vs-58 drift) + fix the contracts top-comment still saying "A1–A9" | NEW (§0 verdict scan) — cheap as-of hygiene | — |
| LB-6 | **K-2: freshness SHA-split** → `canonical_freshness.yaml`; hot file 12k→~5k | R2 B-1; **solo window** (lane-file 5.3 rule); 6 stale SHAs at this bootstrap | — |
| LB-7 | Derived-graph extraction (Citations/co-file/import edges → K-1 staleness section) | R2 B-2 with its **stop rule** carried verbatim | LB-4 |
| LB-8 | M4 citation **soft-warn** in `pre_commit_gate` (= W1.12; verified unbuilt) | R2 B-3 — and B-7's data source | — |
| LB-9 | JSON Schema validation for hand-authored stores (ledger JSONL + 1–2 authored YAMLs) in CI | R2 B-4 (rides with LB-6's store work) | LB-6 |
| LB-10 | **K-3: W1.6 (supersession-citation warn) + W1.7-trimmed** (one status vocabulary + required `superseded_by`) | R2 C-1 — **trim APPROVED, Jordan 2026-06-09** (`3da2d9a`) | — |
| LB-11 | ED-867 `[SUPERSEDED-BY]` markers | R2 C-2; rides on LB-10's vocabulary | LB-10 |
| LB-12 | Fresh-context review as **soft policy** (`reviewed_by` field, soft-warn) | R2 C-3 (demoted from gate) | — |
| LB-13 | Execute the `designs/audit/` **promotion** (staged `git mv` of living design surfaces; co-file repoints; nothing silently deleted) | R2 D-1; Jordan's 2026-06-05 flag; P1-legibility | — |
| LB-14 | Index-drift orphans + PI text paydown (`.jsonl` naming; manifests) + W0.6 B6-strike sweep | R2 D-2 | — |
| LB-15 | **Ship the D-3 creative-tier soft-warn gate** (mechanism APPROVED `3da2d9a`; prefix set grounded) | R2 D-3 | **J-3** (four boundary rulings) |
| LB-16 | Level-4 co-file: `key_type_registry_v30.md` ↔ `module_contracts.yaml` | Verdict §6 proposal | K-1/2/3 built (budget rule) |
| LB-17 | Level-3 grep: emit-type literals in `designs/**` vs parsed registry `type_id`s (catches F2 at commit) | Verdict §6 ≈ W1.3 (promoted from R2-Deferred once budget clears) | K-1/2/3 built |
| LB-18 | `contract_gate()` wrapping `adjudicate()` at `task_gate('design')` entry | Verdict §6 proposal | K-1/2/3 built |

---

## §3 — LANE C QUEUE (Simulation / Implementation — the Godot conversion)

Governing spec: **the conversion strategy** (Parts V–VI are the dictionary + sequencing; Part II the 27-module wave table — all carried). Corrections below are **authoritative over the strategy text until LC-0c folds them in**.

| ID | Item | Detail / correction | Gate |
|---|---|---|---|
| LC-0a | Gate-0 docs half: `valoria-game/docs/architecture.md` v2 (autoload ruling), supersession banners (G1–G7, serialization framing), `sim/README` repoint; author the **Key v1→v2 field map** (G0.1 spec) | Strategy Part IX S1-successor | J-6a veto-window on the autoload recommendation |
| LC-0b | **Gate-0 registrations — AMENDED G0.4:** the full set is now ED-1009/1007's — register `scene.combat_resolved` (F3/C1) + `scene.thread_operation` (form = old C2) + the four doc-12 §8 npc types (`mechanical.project_advanced`, `state.project_completed`, `state.project_failed`, `scene.displacement`) **or strike them from doc-12 §8**; resolve `scene_outcome.battle_concluded` naming drift; **strike `scene.draft_da`** (DA outcomes keyed `da.*`); plus the two attribution rulings (`state.belief_revised`, `scene.dialogue`). `mechanical.scene_activated` already resolved (→`scene_entered`, `1e98edb`) | **J-2 decides; LA-2 executes registry-side; Lane C consumes.** Combat/thread/mass/npc ports do not emit unregistered types | J-2 |
| LC-0c | Fold the strategy's three errata at next touch: adjudicator A1–**A12**, contracts **v3 schema-2**, G0.4→ED-1009 set | §0 scan; `[DRIFT]`-class text item | rides with next strategy edit |
| LC-0d | K8 verdict consumed (Key Resource-vs-RefCounted; salience/fan-out ceilings) | `[ASSUMPTION: K8 still unexecuted — no evidencing commit through 695552e]`; Waves 1–2 proceed behind the Key factory; Wave 4 waits | K8 |
| LC-1 | **Spine build (S2):** KeyStore v2 (§4.1 verbatim) · kernel 3 regimes · named-draw RNG · **statechart whose season superstate = flat-map §4.2's nine-step Accounting spine (A12-checked)** · generated registry loaders · dice-kernel parity vs `d10_success_probabilities.json` · gdUnit4 + headless CI green | First valoria-game commit since 06-06; re-opens design_sync cadence | LC-0a |
| LC-2 | **Ritual upgrade (schema-2):** step 2 of the per-module ritual now also transcribes the module's **contract gates (A10) + derivations (A11)**; step 5's checks are **A1–A12-equivalent** | §0 joint 3 — contracts v3 enriches the port packet | — |
| LC-3 | **First module ritual end-to-end** (settlement_layer recommended): its golden scenario asserts the **Mandate↔L/PS §1.8 damper** (ED-1008) as the first property check | Strategy VI.3 ×6 steps + LC-2 | J-6b (target pick) · LC-1 |
| LC-4 | Wave order per strategy Part II (1 deterministic → 2 d+σ → 3 dice → 4 actors/read; module 20 fieldwork gated on **LA-1**; module 16 coordinates with the parallel combat session) | carried | per-module gates |
| LC-5 | **OWN-5 SIM-DEFECT cascade sim** — confirm termination; magnitudes become load-bearing only after | Handoff `[BUILT — sim-pending]` (ED-1000/1001) | — |
| LC-6 | Python-corpus oracle discipline: nothing in `sim/` retires until its port holds golden-master + property checks through cross-scale | Strategy V.4 | J-6c rules the end-state |
| LC-7 | Wire `treaty.py` (~157L, unwired) + territory fallback | Victory stream | J-11 go |
| LC-8 | Mass-battle engine-side revamp (shape→echelon per the `46592eb` scoping plan) + weapon-physics S2 build/re-baseline (engine + `tests/sim` side) | Engine halves of the J-9/J-10 dockets | J-9 · J-10 |

---

## §4 — LANE A QUEUE (Canon / Editorial / Design-content)

| ID | Item | Provenance | Gate |
|---|---|---|---|
| LA-1 | **Fix the fieldwork P1 canonical-line split** (Disposition triple-divergence; Thread-Read stat; propagation root cause) — the conversion-blocking cluster | `a11e2fa` diagnostic; gates Lane C module 20 | — |
| LA-2 | Execute the **registry §10 Class-B extensions / strikes** per J-2 (the LC-0b set), incl. the doc-12 §8 strike side and §9 count bump; A9 37-vs-38 reconcile rides along | ED-1006/1007/1009 mechanical half | J-2 |
| LA-3 | The **11 shadow modules**: author home docs **or** ratify `registry_derived` status (then the contracts status-enum field lands as a Lane-B contract edit) | ED-1006/1009; verdict §7.1 | J-4 |
| LA-4 | Naming executions: 3-way piety/conviction collision; CI-clock vs Influence-stat overload | ED-1006; strategy R10 | J-2/J-7 naming rulings |
| LA-5 | Stale-index regens (`settlement_layer` pre-LPS-2e; `victory` RS→MS) + malformed `scene.gossip` registry yaml | ED-1006 mechanical | — |
| LA-6 | **Faction-stat write-side migration** (A.5 staged order: Wealth 35 → Mandate 78 → Stability 97 → Military/Influence/Intel) — re-route by the five archetypes; reads untouched | Consolidation master Part A | J-7 |
| LA-7 | Martial-traditions data tables (D-α…δ outcomes) — **parallel-session-owned; coordinate, don't claim** | Handoff blocker | J (parallel) |
| LA-8 | Mass-battle **canon-side** docket execution (bands, per-cell CAP, ED-910/909, discipline 4-role) in `designs/provincial/mass_battle_v30.md` | Handoff blocker; pairs with LC-8 | J-9 |
| LA-9 | Voice-canon closeout: confirm the executed articulation split (`d8eeab9`/`b25a08f`) as the case-#1 ruling | §0 joint 5 | J-3 |
| LA-10 | Fieldwork §11 five pending decisions → ledger records | `a11e2fa` P2 cluster | J-18 |
| LA-11 | **Game-flow canon-propagation & reconciliation** — propagate *already-decided* canon to lagging docs (gf-F6 `victory_v30 §0` "All 15"→GD-1 11+/15; gf-F7 strike the dead ×3 Thread-in-mass-battle MS multiplier in `videogame_mode_spec §1.5` per `campaign_architecture §3.1` flat −1/−2; gf-F8 CI 15→28 [P-32] + Hybrid Personal Phase 2–3→3–5 scenes [player_agency §6.1]); confirm-anchor then reconcile gf-F9 settlement count 35/36/37 and gf-F5 MS=0 shared-loss residue vs GD-1 sole-victory | game_flow_analysis `6199d83a`/`c005da27` | — |
| LA-12 | **Canon-flatten propagation + rename-residue cleanup** — apply the struck PP-675 still live in `canon/03`; apply ED-061 *Restoration* over residual "Revolution"/"People's Revolution"; resolve the rename-sweep self-clobber + C14q Solmund/Solmund doubled-name; C14p stale paths; Almud TS-28. **Commit the source flatten first** (currently uncommitted; full register = 30 items) | conv `a835dd91` canon flatten (UNCOMMITTED) | — (four-name part → J-21) |
| LA-13 | **Threadwork value reconciliation** — add TN 9/POP Binding to `params/core` TN-summary + EV table; propagate the canonical-marked Gap-drain over `v30 §5.2` flat −4/season; apply the threadcut external-op ×2; fix the §4.4↔§3.2 stale Mending row (N1); record WC2 Gap/Lock-halved as the L2 damper. **Commit the source flatten first** (uncommitted; supersedes 06-10 master-analysis §3) | conv `79e2cad2` threadwork flatten (UNCOMMITTED) | — |

*Integrated 2026-06-11 (this session): findings from the 06-11 **game-flow** (committed `c005da27`/`6199d83a`), **canon-flatten** (conv `a835dd91`, **uncommitted**), and **threadwork** (conv `79e2cad2`, **uncommitted**) analyses routed into §4/§5. Findings are as-reported by those sessions (their `[READ:]` trails stand; not re-verified this session) and Jordan-vetoable. gf-F1 (ED-1006 down-channel) and gf-F2 (faction-stat inversion) were already tracked (J-1/J-7; LA-2/3/6). The two uncommitted flattens are flagged for commit under LA-12/LA-13 so their full finding sets (canon 30 items; threadwork 6 contested cells) become durable beyond the chat record.*

---

## §5 — DECISION DOCKET (Jordan-gated; single register, de-staled; ordered by what each unblocks)

Struck from the inherited docket with citations (§0): **combat-v32 ratify** (resolved — roadmap + `canonical_sources` ED-900/904) · **OWN-4** (resolved ED-881) · **OWN-5 as a decision** (decided+built ED-1000/1001; the sim-verify residual is LC-5, not a docket item).

| ID | Decision | Unblocks |
|---|---|---|
| J-1 | **A6 top-down delivery model** — extend `scale_transitions §3` with a downward Key-delivery rule, **or** declare engine-mediated delivery exempt (then the assessor gains a scale-agnostic-stream carve-out + tests) | the 19 A6 seams' status; assessor correction; strategy IV.2 interim-flag retirement; cross-scale Stage-3 design (ED-1006/1009) |
| J-2 | **Registry §10 type set** — the LC-0b list: 7 F2 types (register-or-strike), F3 `scene.combat_resolved`, `battle_concluded` naming, `draft_da` strike, + `belief_revised`/`scene.dialogue` attribution | LA-2 → Lane C combat/threadwork/mass-battle/npc ports (ED-1006/1007/1009) |
| J-3 | **D-3 four boundary rulings** (articulation — de-facto split already executed, confirm; threadwork philosophical ref; char-gen questionnaire; prose-writer skill) | LB-15 ships the approved gate; LA-9 closes |
| J-4 | **11 shadow modules** — author home docs vs ratify `registry_derived` status | LA-3; those ports' `[PROVISIONAL]` exit (ED-1006/1009) |
| J-5 | **Boundary pair** — `settlement_economy` fold-vs-distinct (vs settlement_layer §1.3) and `faction_politics` vs `faction_state` | Wave-2 modules 14/15; prevents double-implementation (ED-1009) |
| J-6 | **Lane-C starters:** (a) autoload ruling (live-pattern recommendation veto-window), (b) first module target (settlement_layer recommended), (c) Python-corpus end-state (oracle-until-cross-scale recommended), (d) Key runtime form — **decided on the K8 verdict** | LC-0a · LC-3 · LC-6 · LC-0d |
| J-7 | **Faction-stat inversion** + DECIDE-1/2 + Intel expand-vs-fold + CI/Influence naming *(or sim Wealth/Mandate first — Lane C can stage that)* | LA-6 migration; faction_state write-side port completion |
| J-8 | F1 Mandate-echo calibration (a/b/c or sim-first) | Echo-side of the same loop LC-3 property-checks |
| J-9 | Mass-battle set: gauge band realignment (H3/H4), per-cell CAP value, ED-910 phase-dependence, ED-909 mapping, discipline 4-role wiring | LA-8 + LC-8 |
| J-10 | Weapon-physics S2 constants set (three-regime, error params, defender-wound, draw-rate, P3 calibrate-or-cut) | LC-8 build + re-baseline |
| J-11 | Victory: treaty-wiring go + territory fallback | LC-7 |
| J-12 | Composure name (Charisma vs Presence) | carried (R2 docket) |
| J-13 | ED-868 collapse-loop recoverable bound | carried |
| J-14 | D6 unified scope-set target (then the mechanical D-pass) | scope-vocab unification |
| J-15 | Resonant Styles — define members + Conviction→style rule, or mark vestigial | dangling-reference closure (master §8.2 note) |
| J-16 | Filename-versioning convention (lockfile trade-off) | carried |
| J-17 | Classification trio: miraculous_event (system vs event-source) · audit (runtime vs QA) · scenario_authoring (authoring vs runtime) | low; tidies three thin modules' contracts |
| J-18 | Fieldwork §11 five pending decisions | LA-10 |
| J-19 | **Accord range + derivation** — canonical Accord range (0–3 per `peninsular_strain §2`/`clock_registry`, which makes GD-2(a) "Accord ≤ 3 → mandatory Muster" fire always) and the settlement-Order(0–5)→province-Accord(0–3) mapping | gf-F3/F4; LA-11 Accord-side; mandatory-Muster trigger correctness |
| J-20 | **Assert/Suppress failure penalty** — `faction_layer §9` *Stability −1* (track) vs `victory §7` *Discipline −15* (derived); which quantity the failure hits | gf-F10; faction-action resolution consistency |
| J-21 | **Four-name world-track fracture** — which of the four world-track names is canonical; the one doc with inverted TT arithmetic is a mechanical fix once direction is set | canon-flatten GD-class; LA-12 four-name part |

---

## §6 — CROSS-LANE DEPENDENCY MAP (the joints, compact)

`J-2 → LA-2 → LC-4` (dice-engine ports emit) · `J-1 → {assessor carve-out (LB), scale_transitions edit (LA), strategy flag retirement (LC)}` · `J-4 → LA-3 → 11 ports exit PROVISIONAL` · `LA-1 → LC-4(module 20)` · `K8 → {J-6d, LC Wave-4}` · `LB-4(K-1) → LB-7 → every session's status` · `LB-10(K-3) → LB-11` · `J-3 → {LB-15, LA-9}` · `J-7 → LA-6 → faction_state port completion` · `LB-6(K-2) solo-window ↔ Lane-A design-doc co-file traffic` (do not overlap) · `LC-1 → LC-3 → LC-4` · `J-9/J-10 → {LA-8, LC-8}` paired canon/engine halves. · `J-19/J-20 → LA-11` · `J-21 → LA-12` · 06-11 analyses (game-flow `6199d83a` committed; canon/threadwork flattens UNCOMMITTED) integrated into §4/§5.

## §7 — DONE-REGISTER (2026-06-06→10; excluded from all queues above)

Contracts spine v1→v2 (`ebc3669`)→v2.1 (`4c474c5`)→**v3 schema-2** (`4eeabd8`; ED-1008) · module-adjudicator skill (`cdbd1b5`; ED-1005) + derived views (`53f27e1`) + **Stage-3 full-graph verdict** (`8d8a208`; ED-1009) · flatten wave maps: personal combat `6165471`, mass battle `bedbf41`/`43e33b1`, social contest `c8394f3`/`68ad7f6`, settlement `7cf5895`, faction `df48990`, fieldwork `a11e2fa`+`d10389b` · Descriptor Registry `b9d897c` (W1.13) · ecosystem reconciliation + R2 `241d96a` · session-consolidation master `59622c0` + stale-handoff trio archived `80aa3ae`/`65e91c2`/`2a2ae53` + active handoff `ebfdd10` · **Godot conversion strategy** `b42aa03` · W1.7-trim + D-3 mechanism **approved** `3da2d9a` · voice-canon extraction `d8eeab9`/`b25a08f` · mass-battle revamp scoping `46592eb` · OWN-5 cascade built `5a8a546` (ED-1000/1001) · R4/R7 hooks `26b5ece`/`0301d06` · victory corrections (GD-1 sole victory; ED-306/107 deprecated; MS=60) `5c1b8cf`/`de08065`/`2edf643` · 06-09 W-wave (W0.1, W0.3–0.5, W0.7–0.8, W1.4–1.5).

## §8 — CARRIED SETS (verbatim from R2 via its banner; deltas only)

**Deferred** · **Triggered** · **Dropped** · **Principles** — all carried unchanged, with two deltas: W1.3 (emit-type hook) promotes out of Deferred into LB-17 once the K-budget clears; R2 A-1 moves to the Done-register (residual = LB-1). The R2 **budget rule** and **B-2 stop rule** are restated in §1/§2 and remain binding.

## §9 — SEQUENCE & SIZING

- **Lane B** (WIP=1): LB-1→2→3 (one cheap session) → **LB-4 K-1** → LB-5 → **LB-6 K-2 (solo window)** → LB-8 → **LB-10 K-3** → LB-13/14 → gated LB-15 → post-budget LB-16..18. ~**5–7 sessions** amortized (R2's estimate holds; LB-5 adds ~½).
- **Lane C**: LC-0a (1 session) → LC-1 spine (1) → LC-3 first ritual (1) → LC-4 at ~1 session/module; LC-5 anytime. Gate-0's registration half waits only on **J-2**.
- **Lane A**: LA-1 + LA-5 ungated now (1–2 sessions); the rest fires per docket ruling — park-and-continue per launch-protocol step 7.
- **Docket cadence is Jordan's**; highest-leverage first ruling by unblock-count: **J-2**, then **J-1**, then **J-6(a,b)** to open Lane C fully.

---
*v3 is the single working master per PI `<document_consolidation>`: the 06-06 capstone and R2 carry supersession banners pointing here; `lane_assignments.yaml`'s source + entry queues repoint here in the same commit; superseded originals stay in git. Every recommendation is Jordan-vetoable; §5 is the veto surface.*
