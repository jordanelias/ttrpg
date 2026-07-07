# Key & Echo Armature v1 — seam contracts + the Echo Matrix, all directions, all scales

## Status: PROPOSED (Jordan-vetoable throughout; §5 is a needs_jordan fork docket that merge does NOT ratify — ED-1094 exception clause, called out in the PR body)
## Date: 2026-07-07 · Lane: IN · ED anchor: ED-IN-0018 · Branch: `claude/fable5-audit-coverage-gaps-22nz7i`
## Authored at the Fable synthesis tier (CLAUDE.md §10 canonical-contract & propagation-spec authorship node)

**Mandate (Jordan, 2026-07-07):** *a harness/armature that properly shapes the subsystems so they
fit into the systems together properly, and improves/perfects the keys required for the domain
echoes — all directions, all scales* — drawing from the same-PR comprehensive audit
(`designs/audit/2026-07-07-unaddressed-areas-audit/`, ED-IN-0017) where relevant.

**What this document is.** The single per-seam contract layer between the philosophical canon
(P-01..15, GD-1..3), the transport canon it BINDS and never forks (`propagation_spec_v1.md`
[CANONICAL, ED-1093], `key_substrate_v30.md`, `key_type_registry_v30.md`, `scale_transitions_v30.md`
§3/§5/§7/§9/§12), the module registry (`references/module_contracts.yaml`, schema-2), and the
executable substrate this PR introduces (`sim/substrate/keys.py`). Its unit of specification is the
**seam-contract row** (§1); its core content is the **Echo Matrix** (§2 — the normative
all-directions × all-scales completion of the Domain Echo family); its registry work is §3; its
enforcement mapping is §4; its open forks are §5; its staging is §6.

**What the audit established that this armature exists to fix** (headline evidence, all
working-tree-verified; full dossiers in the audit's `01_workings/`):
- **There is no executable Key substrate at all** — no Key class, no `emit()`, no key log anywhere
  in `sim/`; the 48-type registry and every `targets[]`/`causes[]` discipline exists only as prose
  plus extracted YAML edges `[C-KEY-4, C-INJ-11]`. This PR lands the substrate core (§6.1).
- **Transport is islands, not organs**: contest kernel, threadwork (entire package), knots,
  parliamentary_vote, settlement layer, articulation, domain_echo.py are all built-but-unreachable
  from the campaign loop; only mass battle, faction accounting (CI/MS/insurgency), Crown/Church
  unique actions, and victory are ORGAN-grade `[C-REACH matrix]`.
- **Echo transport is silent even where wired**: `zoom_out({})` drops every resolver outcome; 100%
  of queued contest scenes defer; the one complete echo implementation has zero callers
  `[C-REACH-1, C-EMERGE-4, N-5]`.
- **Emit-clause coverage is the exception, not the rule**: of 19 state-mutating modules, exactly one
  (faction_state) has doc-native emit clauses backing its contract `[C-KEY-1]`.
- **The rendering gate covers ~10 of 48 types**, with the entire scene_event core five, the
  scene_outcome family, and self-described-maximal-significance types (miraculous_event) falling
  to generic salience `[C-KEY-9, EP-3 calibration]`.
- **The diagonal direction has zero executable or exemplified instances** — causes[] guidance
  exists in one doc corpus-wide; the substrate spec self-reports ~15% population `[C-INJ-11, C-KEY-5]`.

---

## §1 · The seam-contract row (the format every crossing must satisfy)

One row per module edge (emitter → consumer(s)) or per echo rule. Fields:

| Field | Obligation | Checker (§4) |
|---|---|---|
| `key_types[]` | The registered type(s) crossing this seam. A crossing with no registered type is a §3 registry-delta candidate, never an ad-hoc channel (§12.2: the substrate is the SOLE channel). | A2/A15 |
| `emit_clause` | Doc § in the emitter's `doc:` head that names the type and its trigger condition. "Contract says emits, doc says nothing" (the C-KEY-1 pattern) fails this field. | **A13** |
| `payload` | Per-type `required_payload_fields` (registry §1) PLUS the universal obligations: `targets[]` w/ role + per-target `stat_deltas`/`impact_vector` on every down-Key (§12.3/D.1); `scale_signature[]` incl. every scale touched; `causes[]` populated whenever the emitter knows prior Keys caused this (§2-diagonal). | substrate validation + **A14** |
| `consumers[]` | Every registry-declared consumer present in the module's `consumes:` list (closes the C-KEY-6 class). Wildcard readers (articulation) are exempt-by-declaration. | A3/A4 |
| `timing` | The accounting phase binding (accounting_sequence spine) + deferred-apply discipline (AU-3.2/OF-7 — **assumes OF-7; provisional/reversible, docket §5.3**): echo Keys log LIVE at scene end, settlement effects land at ACCOUNTING_BOUNDARY. | A12 + substrate |
| `caps` | Per-scene/per-faction/per-season caps with their PP/ED citations (PP-329 etc.). A cap that exists in prose must exist in the row; a row without a cap states NONE explicitly (the C-VERIFY-12 class: per-scene caps that silently lack season caps). | A15 |
| `rendering` | Verdict per type: RENDERED-RICH / RENDERED-GENERIC / UNRENDERED / **DELIBERATE-SILENT** (with intent citation). The §2-outward table is the normative home. | **A15** |
| `FEEDBACK` | One line: what the player sees when this seam fires (ED-IN-0015 made a required field — prevents new silent seams; EP-11/SIG-2 calibration). DELIBERATE-SILENT rows state "none, by design: <citation>". | **A16** |
| `direction(s)` | bottom-up / top-down / lateral / diagonal / outward / temporal (§12.1: direction is emergent from targets[]/scale_signature/visibility — this field is documentation, not a channel). | — |
| `finding_basis` | The audit finding(s) motivating or verifying the row (C-*/EP/ep/N/F/SIG/OF ids). | — |

**Guardrails binding on every row** (holonic doctrine ED-1083 §2): implement the local rule only;
declared I/O only; never special-case an entity/outcome (scripting drift); never grow a scale-local
interface dialect (shape divergence — the C-FA-3 "PS" collision and C-INJ-12 provenance-name split
are the standing examples this rule exists to prevent).

---

## §2 · The Echo Matrix — normative rows, all directions × all scales

### 2.1 Bottom-up (personal/scene → faction/territory/peninsula)

The §5 family (scale_transitions_v30) is the canon; the armature adds the FEEDBACK line each rule
lacks `[EP-11]` and binds each to the substrate:

| Rule | Key type | Cap · timing | FEEDBACK (new, required) | finding_basis |
|---|---|---|---|---|
| Domain Echo (§5.1-5.3, degree-keyed ±2/±1/0/−1, Sufficient-Scope-gated §7) | `scene.contest_resolved` / `scene.battle_concluded` / `scene.investigation_resolved` / `scene.combat_resolved` → faction stat delta at Accounting | 1/scene/faction (PP-329) · deferred (PP-109) | At scene end: "This will echo: <faction> <stat> <±n> at Accounting" + which qualifying act won the tie-break; §5.2 Failure −1 self-echo warned BEFORE the act (the one warning currently lives only in the off-index UI v4 doc) | EP-11, V10/V12 |
| Debate → Domain Echo (§5.4) | `scene.contest_resolved` (Debate genre) → Mandate | per §5.4 band table · deferred | Track-band meter already shows the threshold; add the Mandate consequence line to the Forfeit/close screen | **ED-SC-0002 fork: §5.4 band-keyed vs contest-§6 genre-keyed — §5 docket; this row is written band-neutral and binds to whichever ruling lands** |
| Accord Echo (§5.5, AUD-SET-02 settlement-targeted) | settlement-locus write, deferred-apply target (AU-3.2) | ±1/territory/Zoom-In · Accounting 4c | "Your conduct here will move <settlement> Accord ±1 at season close" | **ED-SE-0002 fork (open, awaiting Jordan ruling): §5.5 no-stack vs strain §2.7 stack — docket §5.9** |
| Thread Echo (§5.6, ED-673) | `meta.thread_woven` + faction-stat echo | 1/scene/faction · deferred | Practitioner sees the echo line at op resolution; NON-practitioner witnesses see the §5.6 witnessed-Scar warning | C-TW narrative-sinks; fires below narration threshold today |
| PC Faction Embedding (§9, ED-075) | (state read, no Key today) → **candidate `mechanical.pc_embedding_applied`** (§3) | 1/season | "+1D: your presence in <territory>" on the faction action card — currently a bare infill header with literally no authored presentation | EP-11 |
| Fieldwork → BG Echo (§3.9) | `scene.investigation_resolved` | per §3.9 rows | Finding screen names the BG track moved (MS/WC per PP-630 — co-file `fieldwork_bg_v30.md` still carries the pre-rename table `[C-FI-4]`) | C-FI-4 |

**Substrate binding:** every bottom-up echo emits ONE Key (AU-3: one Key per echo; empty
`stat_deltas` on faction targets, settlement-locus effects as deferred-apply). The wiring order for
PR-2 (§6.2): `scene_dispatch` outcome → `scene_outcomes` dict (closing the `zoom_out({})` gap) →
`domain_echo.py` (already implements §5.1/5.2/5.5/5.6 degree-keyed, orphaned today) → deferred-apply
at `accounting_boundary()` → faction/territory write. `[C-REACH-1, N-5, AU-5]`

### 2.2 Top-down (strategic/environmental → settlement/personal)

The §12.4/D.4 closure worklist becomes per-emitter contract rows. The transform is D.1: ONE Key,
N `targets[]` entries (role + per-target stat_deltas/impact_vector), `scale_signature` including the
sub-scale — fan-out width never increments cascade_depth.

| Emitter family | Keys | targets[] population spec (the §12.3 obligation, now per-row) | finding_basis |
|---|---|---|---|
| `domain_actions` → npc_behavior, piety_track, settlement_economy† | `da.*` (5 types) | Every da.* Key names the affected settlement(s) and every present/affected named NPC with role (subject/witness/bystander) + per-target impact_vector. Blocked on the domain_actions home doc (ED-FA-0002/workplan §2-3); the armature row IS the targets[] spec that doc must carry. †settlement_economy is RECOMMEND-RETIRE (contract's own verdict) — its consumer slot transfers to settlement_layer. | C-KEY Part 2, EP-2, EP-6 |
| `faction_politics` → npc_behavior | `state.standing_change`, `state.coup_attempted`, `state.succession` | Every standing/coup/succession Key targets the affected office-holders and their knotted/bonded NPCs. Home doc exists (PP-660, `faction_politics_v30.md`) — flip doc:null (ep-14/ED-IN-0016) and add Part-1-ladder emit clauses. | C-FA-6, C-STUB-6 |
| `peninsular_strain` → npc_behavior, settlement_layer | `env.peninsular_strain_shock`, `env.crisis`, `env.disaster` | Shock Keys carry `affected_territories` (already required payload) + settlement-level targets[] with stat_deltas; disasters get a place-specific landing (the §12.4 "disasters with no place-specific landing" loss). | C-KEY Part 2, §12.4 |
| `scenario_authoring` → settlement_layer | `env.disaster` (authored) | Fork 11 ruled compile=authoring-time (**RATIFIED 2026-07-05, ED-IN-0011 — ledger-verified by refuter R4; critic's verification request satisfied**): the compile step (narrative Stage 1) validates authored events against this row — authored Keys must arrive targets[]-populated or fail compile. Contract entry must be updated to reflect the ratified ruling `[C-INJ-4 — three days stale]`. | C-INJ-4/5, ED-IN-0011 |

**Zoom binding:** the §4.3.2/§4.3.3 trigger tables must cite Key `type_id`s, not only natural-language
conditions — today ZERO rows do, so no validator can confirm a trigger and its Key fire in the
intended relationship `[C-KEY-10]`. The armature requires each zoom row to name its observing
type(s); §4.3.3's five world-state rows additionally need adjudicable procedures (ep-29) and a code
path (none exists — `WORLD_STATE_TRIGGER_PRIORITY` is a dangling constant `[C-INJ-7]`).

### 2.3 Lateral (scene-scale, the eight §3 handoffs)

The #81 audit found these the corpus's best seams; the armature binds each to its types and closes
the two structural holes:
- §3.3 Personal→Scene(Contest) is a HEADER-ONLY handoff (no body) — author it or fold it into §3.4
  `[C-KEY Part 4 note]`.
- Combat's internal `_emit()` trace vocabulary (~25 kinds) must map onto the canonical
  `scene.combat_*` types in one table (currently declared only in Godot `.tres` files, reconciled
  nowhere) `[C-KEY-3]`.
- The dispatch seam: `scene_slate`'s contract declares `consumes: []` — by design scenes are queued
  by `queue_scene()` callers, but then EVERY trigger row (zoom tables, injectors) must name its
  queueing call site; today only Stability-Crisis has one `[C-REACH routing census, C-INJ-8]`.

### 2.4 Diagonal (provenance chains)

`causes[]` is the diagonal channel (§12.1) and is currently unauthored in practice (~15%
self-reported population; ONE doc corpus-wide gives emitter guidance) `[C-KEY-5, C-INJ-11]`. Armature
rules:
1. **Populate-when-known is mandatory** (substrate §2.2 "not optional") — operationalized: every
   emit clause (§1 `emit_clause`) must state which prior Keys it cites into causes[]. An emitter
   that cannot know its causes states NONE-BY-CONSTRUCTION in the row.
2. **One name.** `causes[]` (universal) vs `cause_keys` (strain_shock) vs `origin_keys` (env.crisis)
   is three names for one concept `[C-INJ-12]` — §3 registry delta unifies on `causes[]` with the
   per-type payload fields becoming aliases scheduled for Class-A supersession.
3. Consumers walking causes[] (articulation Why?-surface, npc_memory, the future convergence
   detector ED-IN-0003) get the chain depth they need only if rules 1-2 hold — this is the
   emergent-narrative legibility spine, not decoration.

### 2.5 Outward (rendering — the registry × rendering sweep EXECUTED as data; this is the sweep half of the edge-batch "ED-IN-0012", ledger line 599 — cite the line while §5.10's renumber is pending)

The normative table is the audit's **C-KEY Part 4 48-row sweep**
(`designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/cluster_C-KEY.md`), adopted here by
reference as the armature's outward surface — every registered type now has a verdict
(RR/RG/UR + deliberate-silent assessment). Rules layered on it:
1. **Every UR/RG row gets an explicit disposition**: a new Tier-2 trigger, a named Tier-3 slot, a
   zoom-table citation, or a DELIBERATE-SILENT ruling with intent evidence. The sharpest deltas the
   sweep demands: the scene_outcome family (EP-3 class — battle/contest/investigation/combat
   conclusions), `state.standing_change` (its trigger enum includes `death`), the scene_event core
   five, `state.opinion_revised` (whose own registry text claims a Tier-2 role the table doesn't
   give it `[C-KEY-9b]`), and `meta.miraculous_event` (self-described maximal significance, no
   pathway `[C-KEY-9c]`).
2. **Unregistered trigger types are forbidden**: articulation §3.1 #9 cites
   `meta.cascade_cluster_event`, which is not in the registry — register it (§3) or re-key the
   trigger `[C-KEY-8]`.
3. **The unkeyed emitters get keys before triggers**: settlement events (EP-4), ci_political + era
   transitions (EP-5) — §3's candidate types; the C-MBSE B4 census supplies the exact transition
   sites (gates g_ord0/g_def0/g_dv0/g_ms0/g_ms5/g_msrec/g_diss + the gateless siege-surrender,
   L/PS-drift, IP=100 and CI-milestone sites `[C-MBSE-9..13]`).

### 2.6 Temporal (cadence and ordering)

Binds without restating: O.1 phase order · ORD-1/ORD-2 (insertion order; no set() on ordering
paths) · SSI-1..4 (sub_step_index = append-order tiebreak ONLY; cascade_depth is scheduler-internal)
· Theorem A/B termination discipline · A1 ECHO-DEFERRAL + A2 SLATE-FREEZE. **Implemented in the
§6.1 substrate today (critic-corrected scope): ORD-1/ORD-2, SSI, Theorem-B caps, B1 and OF-7
behaviors flag-gated OFF-by-default; Theorem A / A2 SLATE-FREEZE / O.1 phase composition are PR-2
wiring (they require the slate + season loop) and are NOT in the substrate yet.** Open (docket):
ORD-3 observer ordering, ORD-4 slate World-scoping. OF-HYSTERESIS-AUDIT is a hygiene item per
propagation_spec's own triage (NOT a docket ruling) — routed to §6.3 wave 5.

---

## §3 · Registry deltas (via the §10 Extension Process; PROPOSED, Class-B vetting per PP-674 before filing)

**New key types** (payloads aligned with the Godot G0.1 Key-v2 field set so `sim/substrate` remains
the Python oracle for `Key.gd` v2):

| Candidate type | Family | Emitter · transition site | finding_basis |
|---|---|---|---|
| `state.settlement_revolt` | state_transition | settlement_layer g_ord0 (Order→0 revolt) | EP-4, C-MBSE-9 |
| `mechanical.settlement_captured` | mechanical_event | settlement_layer g_def0 (undefended auto-capture) | EP-4, C-MBSE-9 |
| `mechanical.settlement_surrendered` | mechanical_event | siege Order→0 (gateless today — gate first) | C-MBSE B4 |
| `state.settlement_stat_collapse` | state_transition | g_dv0 (derived value held at 0) | C-MBSE B4 |
| `state.legitimacy_drift` | state_transition | §1.8 L/PS mean-reversion (needs a new gate entry) | C-MBSE-10 |
| `mechanical.ci_milestone_crossed` | mechanical_event | ci_political §2.1 thresholds (40/55/65/80/100 — **the 75-vs-80 discrepancy is docket item §5.11**) | EP-5, C-MBSE-11/12 |
| `mechanical.theocracy_unification_declared` | mechanical_event | ci_political CI=100 | EP-5 |
| `mechanical.era_transition` | mechanical_event | victory g_ms0/g_msrec/g_diss + IP=100 phases (gateless — gate first `[C-MBSE-13]`) | EP-5 |
| `mechanical.second_calamity` | mechanical_event | victory g_ms5 — the game's only true terminal deserves its own type | EP-5 |
| `mechanical.ip_milestone_crossed` | mechanical_event | victory §5.2 IP 60/80/90 authored beats (currently stranded prose) | EP-5 |
| `meta.cascade_cluster_event` | system_meta | articulation §3.1 #9 (RETROACTIVE registration of a type a CANONICAL trigger already cites) | C-KEY-8 |
| `mechanical.pc_embedding_applied` | mechanical_event | scale_transitions §9 (ED-075) | EP-11 |

**Payload-field hygiene deltas:** unify provenance naming on universal `causes[]` (§2.4) ·
`state.card_cooldown_expired`/`state.card_played` deferred to the SE deck build (M2 path, not
keyed pre-engine) · registry entries whose ```yaml blocks fail strict YAML parsing get a
syntax-normalization pass (the substrate loader is tolerant by design, but the typed-params export
cannot be — G4 gap-closure supplies the failing-entry list; archived with the audit).

**Registry meta-repairs:** the 44-declared vs 48-physical count drift (KNOWN, A9-tracked) resolves
when the combat STUBs + legacy_event get §9 rows; the CANONICAL-header vs PROVISIONAL-footer
contradiction gets one status line.

---

## §4 · Conformance binding (every §1 field → its checker)

Existing: **A1-A12** (`skills/valoria-module-adjudicator/scripts/contract_adjudicator.py`; report-only,
~21-violation baseline = the ED-1051 backlog) · narrative-v2 **R1-R10 + R-F1/R-F2/R-HB/R-CL/R-AI/R-RL**
(s4_substrate §S4.9; note R2 consumer-closure and R3 total-accounting are the runtime forms of A3/A4,
and R7 is ORD-2's compile-time form).

**New armature checks (specified here; implemented PR-3, report-only first, flip-on-zero-backlog).
Enforceability commitments per the critic's verdict — each check names its mechanical predicate,
its input surface, and the artifact that must exist first:**
- **A13 — emit-clause coverage.** Predicate (mechanical, weak-form): for every module with
  non-empty `emits:`, each emitted `type_id` string appears verbatim in the file named by `doc:`
  OR by a NEW schema-2 field **`doc_emit_ref:`** (to be added to module_contracts — the
  npc_behavior/doc-12 case `[C-KEY-2]` becomes an explicit field). The "trigger condition present"
  half is NOT mechanically decidable and stays a review checklist item, stated as such. Requires:
  adjudicator gains doc-file read access + the schema field.
- **A14 — down-Key targets[] lint.** Runtime predicate (substrate, PR-2): a Key whose
  `scale_signature` contains BOTH a strategic scale (territory/peninsula) AND a sub-scale
  (personal/settlement) with empty `targets[]` warns — the sharpened "spans scales" rule the
  critic required (a single-scale `mechanical.season_change` never fires it). The static
  "population rule documented" half is a §2.2-row review item, not a checker claim.
- **A15 — registry × rendering completeness.** Requires a **machine-readable disposition
  datafile** — `references/rendering_dispositions.yaml` (type_id → {tier2, tier3, zoom,
  deliberate_silent+citation}) — generated once from the C-KEY Part 4 sweep in the rendering wave
  (§6.3-4) and thereafter the checker's input. Predicate: every registry type_id has a row.
  The §10-extension half is docket §5.16 (a process-canon change, Jordan's).
- **A16 — FEEDBACK-line presence.** Input surface is the armature §2 tables themselves (markdown
  column-presence lint, the co-file-checker pattern per the still-open ED-IN-0015's own proposed scoping) — explicitly
  NOT contract_adjudicator (wrong surface, per the critic).

**Consumer-closure repairs the audit hands A3/A4 directly:** add the six npc_behavior `consumes:`
edges ED-935's registrations orphaned (`scene.thread_operation`, `scene.draft_da`,
`scene.displacement`, `mechanical.project_advanced`, `state.project_completed`,
`state.project_failed`) and refresh the stale gap_note `[C-KEY-6]`; the four combat edges remain
tracked by gap_note A4 (sequenced-not-abandoned).

---

## §5 · Consolidated fork docket (needs_jordan — merge does NOT ratify these; each row states the armature default it is written compatible with)

| # | Fork | Default the armature assumes (reversible) | Blocks |
|---|---|---|---|
| 5.1 | **OF-D6 double-count/disjointness** (propagation_spec §3 D.6, HIGH) — do down-targeted settlement stat_deltas overlap what AGGREGATE_s reads? | Assume DISJOINT (deferred-apply targets write substrate cells the aggregate reads once) | cross-tick convergence; PR-2 echo wiring semantics |
| 5.2 | **OF-3 decay()** (AU-4) — the key-log re-derivation decay function | Substrate ships WITHOUT decay (log grows; re-derivation reads full window) | convergence proof; long-campaign memory |
| 5.3 | **OF-7 deferred-apply** (AU-3.2, PROPOSED amendment to key_substrate §4.1 step 4) | Implemented flag-ON in substrate ([PROVISIONAL]) | ratifies the substrate's default |
| 5.4 | **OF-B1 no-synchronous-re-entry** (PROPOSED amendment to §4.1 step 5) | Implemented flag-ON in substrate ([PROVISIONAL]) | ratifies the substrate's default |
| 5.5 | **RNG-MODEL-COLLISION** — single World.rng vs per-emission-seed (§6.1) vs named-draw-service | Substrate takes NO rng dependency yet (no draw in emit path) — the fork must be ruled before any stochastic consumer lands | PR-2 stochastic echo consumers; replay claims |
| 5.6 | **ORD-3 / ORD-4** (observer ordering; slate World-scoping) | Substrate does not implement compute_observers at all until ORD-3 lands | §4.1 steps 3-4; determinism completeness |
| 5.7 | **OF-CAP** — CASCADE_DEPTH_MAX / EMISSIONS_PER_TICK_MAX values | Substrate takes caps as REQUIRED caller parameters; no constant in the repo | Theorem-B constants |
| 5.8 | **ED-SC-0002** — echo keying: §5.4 track-band vs contest-§6 genre (N-4; one name, two referents, three docs N-4b) | §2.1 Debate row written band-neutral | Stage-4 echo wiring; §2.1 |
| 5.9 | **ED-SE-0002** — Accord stacking: §5.5 no-stack vs strain §2.7 stack | §2.1 Accord row carries the cap, not the stacking rule | Step 4c reconciliation |
| 5.10 | **ED-IN-0012/0013 double-allocation renumber** — each ID allocated twice in the merged ledger (PR #83 SC batch vs PR #81/#82 edge batch; independently confirmed `[C-VERIFY-17]`). Proposal: renumber the LATER-FILED edge-playability pair to fresh ED-IN ids at ruling time; fix cross-refs (edge report §7 addendum, HANDOFF_IN). Merged-ledger rewrites are Jordan-reserved (ED-306 precedent). | id_reservations.yaml counters repaired this PR (mechanical half); ledger renumber held back | citation integrity |
| 5.11 | **CI milestone 75-vs-80** — ci_political §2.1 (mechanical: 40/55/65/80/100) vs conviction_track_v30 §11.3 (presentation: 40/55/65/75) `[C-MBSE-12]` | §3's `mechanical.ci_milestone_crossed` carries thresholds as data, not constants | EP-5 keying; presentation sweep |
| 5.12 | **ER-2 substrate scope** — combat's degree() has the −0.5 continuity correction; the shared sigma_leverage.degree() (contest path) does not `[C-SIG-3]`; and combat's fixed 2·Ob Overwhelming bar saturates with pool while contest's pool-aware bar does not `[C-RESPESS-1]`. One band-boundary discipline should govern the substrate — which? | Armature takes no default (genuine design fork: ER-2 everywhere + pool-aware bars everywhere is the symmetric option) | resolution seam under every §2 row |
| 5.13 | **Contest pool formula / live-dispatch** — ED-SC-0004 (N-2) plus the audit's sharper form: the LIVE campaign path resolves contests through the deprecated raw-dice stub `[C-RESPESS-2]` | §2.1 rows bind to outcome degrees, not to either formula | SC consequence spine (ED-SC-0006/0007) |

| 5.14 | **OF-6 / OF-1** (settlement addressability as `targets[].actor_id`; per-stat settlement-locus basis — propagation_spec §2 open flags, triaged "smaller, non-blocking" by its §5 item 8) | §2.1's settlement-locus rows and §3's settlement types ASSUME both; surfaced here per the critic's under-disclosure verdict | §3 filing; keying wave |
| 5.15 | **OF-OWN** — the §6.1 TickScheduler is engine_clock-shaped while engine_clock is doc:null pending ED-1051; the scheduler's ownership formalizes when ED-1051 flips | §6.1 stays substrate-internal until then | ED-1051 (already T0) |
| 5.16 | **A15 process extension** — "no new type registers without a rendering-disposition row" adds a mandatory precondition to the registry's CANONICAL §10 process; flagged as a process-canon change needing explicit ratification, not slipped in as a checker rule (critic overreach-watch) | A15 runs report-only against existing types regardless | §4 A15 flip-to-blocking |

**Ruled-but-unexecuted items are NOT forks** — they are §6.3 remediation with existing authority:
ED-871 (Mending cost=0; doc fix never landed `[C-VERIFY-13]`), fork-2/ARC-T04 strike (ratified,
unexecuted `[C-VERIFY-16]`), fork-11 contract-entry refresh `[C-INJ-4]`, ED-935 consumer edges
`[C-KEY-6]`.

---

## §6 · The harness: substrate, wiring, waves

### 6.1 This PR — `sim/substrate/` (the executable core)
`Key` dataclass (registry §1 + universal fields; cascade_depth deliberately NOT a Key field —
SSI-4) · `KeyLog` (append-order SSI assignment; §2.3 invariants 1-8 enforced at append;
deterministic serialization + sha256 content hash — the R-F2 surface) · `TypeRegistry` (tolerant
line-based parse of the canonical registry markdown — the registry stays the single source of
truth) · `TickScheduler` (ORD-1/2 discipline; Theorem-B runtime asserts with caller-supplied caps
[OF-CAP]; B1 schedule_emission + no-sync-re-entry flag [OF-B1]; OF-7 deferred-apply at
accounting_boundary(); fan-out-width-is-not-depth per D.1). Tests:
`tests/valoria/test_key_substrate.py` (24 cases incl. byte-identical replay). NOT implemented
(docket-blocked): compute_observers/armature interpretation (ORD-3), decay() (OF-3), any RNG
dependency (5.5). **No campaign-loop wiring in this PR** — goldens untouched.

### 6.2 PR-2 — echo transport wiring (flag-gated)
`ECHO_TRANSPORT=0` default with byte-exact legacy pins (the MB FIELD_MOVEMENT/ED-1089 CI-pin
precedent) + a new seeded golden with the flag ON. Contents: resolver outcomes → `scene_outcomes`
(no more `zoom_out({})`) → `domain_echo.py` un-orphaned → deferred-apply at the boundary →
faction/territory writes; `parliamentary_vote` called from the loop; emit `scene.*_resolved` Keys
through the substrate so the KeyLog becomes the campaign's first canonical_key_log. The
context-derivation bridge (actors from aggregate state) stays SC-lane work (ED-SC-0006/0007).
C-EMERGE's F7 smoke-oracle spec (second pinned golden at base_seed=42; named zero-assertions for
scenes_resolved/insurgencies_formed/npcs_generated that flip to feature-assertions as wiring lands;
Hafenmark-lockout assertion; dead-param regression) lands WITH this PR so the wiring is born
guarded.

### 6.3 PR-3+ — shaping waves (one lane per PR, each verified by the extended adjudicator)
1. **Keying wave (SE/WR):** §3 candidate types + gate-differentiated emit clauses per C-MBSE B4
   (executes ED-IN-0014); era/CI beats un-stranded (EP-5).
2. **Down-seam wave (FA/WR):** §2.2 targets[] population per family (executes the §12.4/D.4
   worklist); domain_actions home doc carries its row (ED-FA-0002).
3. **Consumer/contract hygiene wave (IN):** C-KEY-6 edges; fork-11 + miraculous_event gap_note
   refreshes `[C-INJ-2/4]`; faction_politics doc:null flip + citation sweep (ep-14/ED-IN-0016);
   A13-A16 implemented report-only.
4. **Rendering wave (IN/WR):** §2.5 dispositions → articulation §3.1 rows + Tier-3 slots
   (the remediation half of edge-batch "ED-IN-0012", ledger line 599 — §5.10 disambiguation);
   zoom rows get type_id citations `[C-KEY-10]`; ships `references/rendering_dispositions.yaml`
   (A15's input datafile).
5. **Ruled-but-unexecuted sweep (WR/PC):** ED-871 doc fix; fork-2 strike execution; knots
   propagation completion (ED-912 → knots_v30 §6/§11 + mechanics_index `[C-FI-5/6]`).
6. **Godot (M3, deferred by ruling):** `Key.gd` v2 ports FROM `sim/substrate` (G0.1 field set);
   trigger = Gate-0 entry, recorded in HANDOFF_GO.

### 6.4 Adversarial posture (per the audit's method, carried forward)
Every wave lands with its own refuter pass on P1/P2 claims and cites this armature's rows as the
conformance target; the armature itself received an independent critic relay before merge (see the
audit folder's `01_workings/refutations/armature_critic.md`).

---

## §7 · Provenance
Authored by the Fable 5 orchestrator from the 14-cluster comprehensive audit (ED-IN-0017; charter,
dossiers, refutation records in the audit folder), the canon surface (propagation_spec_v1,
key_substrate_v30, key_type_registry_v30, scale_transitions_v30, module_contracts.yaml,
articulation_layer_v30, narrative-v2 s4_substrate), and the prior week's ratified findings
(#77/#80/#81). Read-only on all existing canon: this document ADDS a contract layer and an
executable substrate; it edits no ratified text and rules no fork.
