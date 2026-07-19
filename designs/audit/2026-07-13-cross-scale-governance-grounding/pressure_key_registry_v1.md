# Pressure-Key Registry (v1) — every governance/legitimacy/authority/standing key, all scales

## Status: FILED (in progress) — 2026-07-13 · ED-IN-0051

**What this is.** The centerpiece registry of the `2026-07-13-cross-scale-governance-grounding` docket
(see the docket `README.md`). It enumerates **every governance / legitimacy / authority / standing
state-variable ("key") found in the corpus, at every scale it exists at**, and binds each one to the
Key & Echo Armature's six propagation directions (bottom-up, top-down, lateral, diagonal/skip-scale,
outward/bend-around, temporal). It is a **read-only synthesis**: it indexes and cross-references
already-written canon, proposals, and rulings; it does **not** flip any source doc's `## Status:` line,
rule any open fork, wire any inert field, or invent a mechanic no cited source already contains. Where a
key is genuinely a collision, a gap, or this registry's own inference rather than verbatim canon, that is
stated explicitly in the row rather than smoothed over — the whole point of the exercise is to make the
corpus's real shape legible, seams included.

Sources read directly for this registry: `designs/architecture/governance_type_registry_v1.md` (the
FLAG/VECTOR census this table operationalizes into per-key rows), `designs/territory/scale_hierarchy_v1.md`
(the ratified hierarchy + consent-gate + cross-scale-authority ruling), `designs/architecture/
key_echo_armature_v1.md` (the six-direction substrate this table binds to), `designs/architecture/
propagation_spec_v1.md` (aggregate-up/distribute-down transforms + the D.6 double-count hazard),
`designs/architecture/governance_consolidation_v1.md` (the D1–D6/E1–E11 rulings), `designs/provincial/
clock_registry_v30.md`, `designs/territory/settlement_layer_v30.md` §1.8/§3, `designs/provincial/
faction_behavior_v30.md` §3–4, `designs/provincial/faction_politics_v30.md` Parts 1–3, `designs/provincial/
franchise_v30.md`, `designs/territory/valoria_political_hierarchy_v30.md` §2.4, `designs/provincial/
peninsular_strain_v30.md`, `designs/provincial/ci_political_v30.md`, `designs/world/ms_trajectory_v1.md`,
`designs/territory/governance_play_redesign_v1.md`, `designs/provincial/faction_canon_v30.md` §7–8, and
`designs/territory/territory_temperaments_v30.md`.

---

## Legend

**Class.** `FLAG` = a discrete, specific policy choice (boolean/small-enum/staged-state-machine), selected
occasionally by an authority, non-accumulating. `VECTOR` = a continuous/multi-dimensional weighted
quantity that accumulates, decays, or aggregates. `BOTH` = the dominant real pattern per
`governance_type_registry_v1.md §1` — a VECTOR body with one or more derived FLAG events riding threshold
crossings.

**The six armature directions, mapped onto columns** (`key_echo_armature_v1.md`'s vocabulary):

| Armature direction | Column that binds it |
|---|---|
| Bottom-up | **Agg↑ (UP)** — how a parent-scale value derives from child-scale instances |
| Top-down | **Prop↓ (DOWN)** — how a parent-scale value/policy imposes onto child-scale instances |
| Lateral | **Lateral↔** — same-scale, non-hierarchical transfer/contagion/echo |
| Diagonal (skip-scale) + Outward (bend-around) | **Skip/Bend** — one column, per this registry's schema; the two armature directions share a column because both are "the normal chain doesn't apply here," distinguished in-cell by which mechanic (a skip-scale claim vs. an authority bypassing the chain entirely) |
| Temporal | **Decay_fn** — dissipation/persistence over time; a key with `NONE — GAP` here has no temporal binding at all today |

**Collision?** — is this key structurally **drivable top-down and bottom-up in the same tick** (the
"collision of stresses" mode the docket's own README names, distinct from the §8 *naming* collisions
below)? `YES` / `NO`, with a footnote where the mechanism needs explaining.

**Status.** `LIVE` = specified in ratified/CANONICAL prose and reachable by current `sim/` code or an
active resolver path. `INERT` = specified and even ratified, but confirmed **not read or written** by any
code (the `lps_inert_check` class of finding). `DOCTRINE-ONLY` = Jordan has ruled the *concept* true/binding,
but no mechanical formula, calibration, or Key type has been authored yet. `STUB` = a formula or table
exists in prose but is uncalibrated, PROPOSED-not-ratified, or missing a required companion (a decay
curve, a granter rule, etc.).

Wide tables below are wrapped for horizontal scroll; if your viewer doesn't respect the wrapper, scroll the
raw table right — every row keeps the same 13 columns: **Key · Scale(s) · Class · Range · Agg↑(UP) ·
Prop↓(DOWN) · Lateral↔ · Skip/Bend · Decay_fn · Collision? · Derived Flags · Source · Status.**

---

## §1 · Family 1 — Structural / hierarchy

*(who can act on whom, at what scale — not yet the content of what governance-type is imposed; that's §3)*

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Two-Tier Authority (Provincial Authority ↔ Settlement Governor) | Province ↔ Settlement | FLAG | 2-slot structural | none | PA sets rules (tax/military/legal/Domain Actions); Governor executes locally | none | Chain-bypass rows (below) bend around this pair entirely | NONE (structural slot) | NO | disagreement → "tension generates gameplay" (no Key type yet) | `settlement_layer_v30` §3.1 | LIVE |
| Province existence-conditionality | Province (derived from Territory) | FLAG (exists/not) | {exists, does-not-exist} | "exists" iff ALL constituent Territories share one faction holder (AND-gate) | none — a naming convenience over Territories, not an imposing tier | re-forms on faction re-unification | none | NONE — live-recomputed on every control change, not a decaying scalar | NO | none named yet | `scale_hierarchy_v1` §2 (supersedes `valoria_political_hierarchy_v30` §2.3) | DOCTRINE-ONLY [^f1] |
| Faction power-basis (population × positional weight) | Faction-tier (local/provincial/national), independent tiers | VECTOR | unscaled — no canonical formula | implied "sum of people held across scales," not formalized | none stated | tiers are explicitly NOT nested — this row IS that lateral-independence claim | Cross-scale claiming (below) is the operational mechanism | NONE — no formula exists yet | unresolved (no formula to test) | territory-holding becomes a CONSEQUENCE, not the primitive | `scale_hierarchy_v1` §5.1 | DOCTRINE-ONLY |
| Independence eligibility | Settlement / Territory / Province | FLAG | {held, independent} | n/a | n/a — the local tier's own break | re-aggregates under a different faction post-break (see claiming, below) | generalizes PP-726 §2.3's province-only rule down to settlement grain | NONE — discrete event | NO | none named — no Key type registered | `scale_hierarchy_v1` §5.2 | DOCTRINE-ONLY |
| Cross-scale faction claiming | any Settlement, claimed by a faction from a different scale tier | FLAG | discrete claim event | claimed settlement aggregates normally into Territory/Province afterward | none — this IS the diagonal event | none | **DIAGONAL/skip-scale — the canonical example** (e.g. RM claims one settlement without holding its territory/province first) | NONE — one-shot origin event | NO | none named | `scale_hierarchy_v1` §5.2 | DOCTRINE-ONLY |
| Chain-bypass authority (Monarch) | Country acting directly on any lower tier | FLAG | binary exemption | n/a | direct top-down action skipping Duchy/Province/Territory | none | **OUTWARD/bend-around — canonical example**: skips the authority chain, not a spatial scale | NONE | YES — unresolved arbitration if Monarch's order and the normal chain's order collide on one settlement in one season [^f2] | none named | `scale_hierarchy_v1` §5.3 | DOCTRINE-ONLY |
| Chain-bypass authority (Parliament) | Country-level body acting on any lower tier | FLAG | binary exemption | n/a | forcible action despite no chain position | composes with existing Censure mechanics | **OUTWARD/bend-around**, same class as Monarch — and the two bypass authorities can collide with each other, not only with the normal chain | NONE | YES, same unresolved-arbitration gap as Monarch [^f2] | Censure-tier instance is wired live (`faction_take_action`) | `scale_hierarchy_v1` §5.3; `sim/provincial/parliamentary_action.py` | BOTH: concept DOCTRINE-ONLY, Censure instance LIVE |
| Governor Assignment eligibility (Standing-tier → settlement-type gate) | Settlement, assigned by Province-controlling faction | FLAG (4-tier gate) | Standing 0–2 ineligible / 3 Town-Outpost / 4 City-Fortress-Mine / 5 Seat-Cathedral | n/a | Province-faction assigns; Bishop-Governor special-install transfers governance to Church | none | none | NONE | NO | Bishop-Governor install → province-fractionalize-on-mismatch (state-transition FLAG) | `settlement_layer_v30` §3.2 | LIVE — cites the pre-ladder 0–5 Standing scale, see §8 collision |

</div>

[^f1]: Ratified 2026-07-13 (direct Jordan ruling). PP-726's mechanical rewrite (settlement-count-per-territory, political-value formula, governor assignment at territory grain) is tracked, unexecuted work per `scale_hierarchy_v1` §6 item 1.
[^f2]: Two structurally independent authorities (Monarch, Parliament) can each issue a directive that lands on the same lower-tier actor in the same season, alongside the normal chain's own directive (Family 3's Directive key) — no ordering/precedence rule is authored for any of these three sources colliding at once.

---

## §2 · Family 2 — Legitimacy–consent spine (L / PS / Mandate / Standing)

*The single most important cross-scale throughline in the corpus — see `governance_type_registry_v1` §2.3.*

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Legitimacy (L) | Settlement, per controlling faction | VECTOR | 0–7 | W-weighted mean → faction `aggregate_L`; `q_s=0.5L+0.5PS` feeds Mandate's T | Mandate→L mean-reversion (below-Mandate settlements get L+1, capped ±1/season) | none native (Charter/Quo-Warranto echo THROUGH L, not within it) | none native — the governance-cascade consent-gate (Family 3) routes through L/PS wherever contested | **NONE — GAP** [^g1] | **YES** [^g2] | §1.8a threshold-triggered events (Charter+1, Regular-court+1, …) | `settlement_layer_v30` §1.8 | **INERT** [^g3] |
| Popular Support (PS) | Settlement, per controlling faction | VECTOR | 0–7 | W-weighted mean → `aggregate_PS`; feeds Mandate's `q_s` | Mandate→PS mean-reversion (above-Mandate settlements get PS−1, capped) | none native | none native | **NONE — GAP** [^g1] | **YES** [^g2] | §1.8a PS-channel events (Dearth-relieved+2, Festival+1, …) | `settlement_layer_v30` §1.8 | **INERT** [^g3] |
| Settlement Weight (W_s) | Settlement | VECTOR | 1 (Outpost) – 11 (developed Seat) | feeds `T = Σ W_s·(q_s/7)`, the Mandate mass term | none — own composite `base(Type)+Prosperity+FacilityTier` | Weight-as-Exit transfers +0.5-Prosperity-growth to the nearest higher-Order neighbor on the adjacency graph | none | Weight-as-Exit: −1 after ≥2 consecutive Dearth/Order≤1 seasons; +1 per 4 stable seasons, capped at structural ceiling (PROPOSED) | NO | Weight-as-Exit threshold FLAG | `settlement_layer_v30` §1.8, §1.8c (ED-SE-0016) | STUB — downstream of inert L/PS regardless |
| Faction Mandate | Faction-tier (derived from all controlled Settlements) | BOTH | 0–7, `clamp(round(7T/(T+6)),0,7)` | Settlement→Faction direct (skips Territory/Province) | mean-reverting feedback to settlement L/PS | none | **the direct Settlement→Faction aggregation IS a skip** | NONE of its own — pure re-derivation each Accounting, no memory term | **YES — flagship case** [^g4] | consumed as a threshold gate (Excommunication Ob, victory conditions) but has no band-crossing FLAG of its own | `settlement_layer_v30` §1.8; `faction_behavior_v30` §4 | **RULED-RETIRE-as-collapse-carrier** (D4, 2026-07-13) [^g5] |
| Faction aggregate_L / aggregate_PS | Faction-tier (derived) | VECTOR | 0–7 each | `Σ W_s·L_s / Σ W_s` (and PS analog) — simpler weighted mean, not saturating | feeds Strictness (below); not written back down itself | none | same Settlement→Faction skip as Mandate | NONE — pure re-derivation | inherits L/PS's collision | feeds Strictness bands | `settlement_layer_v30` §1.8; `faction_behavior_v30` §3.6 | **INERT** (same root cause) |
| compliance(L) yield function | Settlement | VECTOR | 50–100% of Prosperity yield | none directly — a per-settlement Treasury multiplier | Fiscal Stance (Family 6) is the top-down policy this answers to | none | none | NONE — re-evaluated each Accounting, no persistence of its own | inherits L's status | none of its own | `faction_layer_v30` §5.9 (ED-FA-0008) | STUB — PROPOSED, no Treasury coupling yet, inert-L-dependent |
| Public Expectation Strictness | Faction-tier (derived) | VECTOR | 0–1, `clamp(0.4+0.5·aggL/7−0.3·aggPS/7,0,1)` | reads aggregate_L/PS | modulates Domain-Action Ob for every member NPC/PC | none | none | NONE — pure re-derivation | inherits L/PS/aggregate's collision | none of its own (continuous modifier) | `faction_behavior_v30` §3.6 | **INERT** |
| Settlement-grain L/PS derivation events (§1.8a) | Settlement | FLAG ×~11 | ΔL/ΔPS per event, −2 to +2 | none — these ARE the source events L/PS lacked | none | none | none | n/a (discrete triggers) | NO (explicitly non-stacking with §1.8b's transfer-seed) | is itself the derived-flag layer for L/PS | `settlement_layer_v30` §1.8a (ED-SE-0007) | STUB — PROPOSED, "shape proposals not sim-calibrated," writes into inert fields |
| ΔLegitimacy (faction-grain Δ-formula) | originally Faction-tier, superseded-to-per-settlement by LPS-2e | VECTOR (additive formula) | unbounded delta pre-clamp | n/a | applies uniformly to controlled settlements | none | none | **NONE — GAP, explicitly flagged** [^g6] | n/a (formula-level) | none | `faction_behavior_v30` §3.5 | DOCTRINE-ONLY / superseded-in-part |
| ΔPopular_Support (faction-grain Δ-formula) | originally Faction/Territory-tier, superseded-to-per-settlement | VECTOR | unbounded delta pre-clamp | n/a | applies per controlled settlement | Strain-driven temperament drift (§3.4.2) shifts α/β weights — a lateral cross-clock coupling | none | **NONE of its own** — same shape as ΔLegitimacy, no baseline-reversion term | n/a (formula-level) | `outcome_polarity_gate` (0.5/1.0 threshold-switch) | `faction_behavior_v30` §3.4 | DOCTRINE-ONLY / superseded-in-part |
| Settlement Order | Settlement | VECTOR | 0–5 | `floor(mean(Order))` → Province/Territory Accord | Fiscal Stance / Directive-compliance effects land here | none native (contagion runs via Accord/Turmoil, not Order-to-Order) | none | **NONE stated** — moves only via named triggers (garrison+1, Govern+1/+2, battle−2, occupation−1/season); no ambient decay [^g7] | NO (Accord reads it, doesn't write it) | Order=0 → `g_ord0` Revolt (candidate `state.settlement_revolt`); Defense=0 → `g_def0` (candidate `mechanical.settlement_captured`) | `settlement_layer_v30` §1.3; `key_echo_armature_v1` §3 | LIVE (Key types registered-candidate, not filed) |
| Province/Territory Accord | Territory/Province | VECTOR | 0–3 | `floor(mean(settlement Order))` — the cleanest bottom-up formula in the corpus | Turmoil/Strain bands force Accord down at Fracture/Crisis/Collapse | none native | none | derived — "decay" is whatever decays Order; live-recomputed on any child change | **YES** — bottom-up from Order AND top-down-forced by Strain in the same Accounting; ED-SE-0002 stacking fork OPEN | Accord=0 → Revolt/Uncontrolled | `peninsular_strain_v30` §2; `settlement_layer_v30` §1.3 | LIVE (formula); ED-SE-0002 fork OPEN |
| Standing — **naming collision** | (a) Faction-oscillating 0–5; (b) player-faction-relationship 0–5; (c) ratified 0–7 rank ladder; (d) implied "Standing-6+" higher range elsewhere | FLAG (rank) over VECTOR-like advancement pressure | **0–5 / 0–5 / 0–7 / "6+"-implied — UNRECONCILED** | n/a (personal/NPC-scale) | Demotion-Magnitude cascades (1-rank / 2-3-rank / dismissal) | Rival Cohort (same-rank competing NPC) | cross-rank demotion explicitly SKIPS intermediate ranks (no pass-through) | NONE — event-triggered only | N/A as a driven-value race; **YES as a naming collision** [^g8] | Demotion-Trigger enum; Recognition Fork; Dismissed/Dishonored flag | `faction_politics_v30` Part 1 (PP-660); `clock_registry_v30`; `player_agency_v30` §5.4 | **LIVE but UNRECONCILED** |
| Renown | Personal (PC), persists across faction changes | VECTOR | 0–10 | none (not aggregated upward) | Renown 7+ unlocks independent Domain-Action pool (`floor(Renown/2)`) | Caste modifiers halve public-territory gains for Southern Einhir (Family 4) | Renown 7+ is an explicit bend-around of the whole Standing-ladder requirement | **NONE — explicitly BY DESIGN** ("Renown does not decay naturally") [^g9] | NO | threshold-gated settlement-governance-scope unlocks; Governance-Responsibility risk (−1/season, cap −2) | `player_agency_v30` §5.4 | LIVE |
| Suspicion | Settlement→Faction (a governor's own standing) | VECTOR | unbounded accrual, capped +1/season; threshold → Recall | none (single-governor-scoped) | Defy/Divert Directive-response drives this — bottom-up refusal of a top-down Directive | none | none | **RULED-IN-PRINCIPLE, NOT YET AUTHORED** (E11/D6, 2026-07-13) — a symmetric compliance-decay term is mandated but its curve is unspecified; one-shot `Submit to audit` escape (−2) is live | NO (single-authority track) | threshold → G606 "The Bailiff's Report" → Recall scene | `governance_play_redesign_v1` §1.4; `governance_consolidation_v1` D5/D6/E11 | **DOCTRINE-ONLY** |

</div>

[^g1]: **GAP.** The §1.8a event table is additive-only; the ONLY reversion anywhere in the L/PS system is Mandate's separate bidirectional feedback (a different mechanism, not a decay-toward-baseline or decay-toward-zero term on L or PS themselves).
[^g2]: L/PS are simultaneously bottom-up-sourced (§1.8a events) and top-down-fed-back (Mandate mean-reversion) in the *same* Accounting; no ordering rule states which applies first if both fire on one settlement in one season — the local instance of `propagation_spec_v1` §3 D.6's double-count hazard.
[^g3]: **GAP.** Confirmed 100/100 by `tools/sim_harness`'s `lps_inert_check` (`scale_hierarchy_v1` §4; `governance_consolidation_v1` D4/E5) — fully specified in prose, read/written by nothing in `sim/`.
[^g4]: Mandate is bottom-up-derived from settlement L/PS *and* top-down-feeds-back into those same settlements' L/PS every Accounting — `propagation_spec_v1` §3 D.6's HIGH-PRIORITY double-count risk (is the down-write disjoint from what the up-aggregate reads?) is not ruled.
[^g5]: `governance_consolidation_v1` §1/§6 (D4): retired as the cross-scale collapse signal (it "masks peripheral collapse"); replaced by floor-avg Order + province fracturing + Standing/`resolution_quality` Keys; kept only as the faction/parliamentary meter, renamed to end the two-Mandates collision (§8 below). Downstream of inert L/PS regardless of ratification.
[^g6]: **GAP, explicitly flagged per this docket's brief.** The formula is `+λ_continuity·seasons_in_role + λ_procedural·score + λ_expectation·cascade_fidelity − λ_violation·score` — every term is event-additive; there is no `−λ_decay·L` or mean-reversion term of its own.
[^g7]: `governance_type_registry_v1` §2.3 confirms: "no unforced decay term of its own."
[^g8]: The exact `governance_type_registry_v1` §2.8-class hazard: four docs assume different ranges/subjects for "the same" word. PP-660's 0–7 ladder is the newest/most-elaborated and is read as authoritative for rank purposes in this registry, but nothing has formally retired the other three citations.
[^g9]: Contrast with L/PS/ΔLegitimacy's "NONE" above — this one is a stated design choice, not an omission.

---

## §3 · Family 3 — Governance-mode & franchise

*The content of what governance-type is imposed/negotiated, plus the parliamentary-weight apparatus.*

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Governance-type cascade (the imposed type itself) | Duchy→Province→Territory→Settlement (each sets the tier below) | FLAG | open enum — value-domain per next row | "and vice versa" — settlement conditions feed back up, mechanism unspecified | the cascade itself: noisy-weighted, not deterministic | none native | L/PS is the consent-gate deciding whether an imposed type "sticks" (Family 2) | n/a (a state, not a decaying scalar) | **YES, by design** — explicitly bidirectional | none named — no Key type registered | `scale_hierarchy_v1` §3 | DOCTRINE-ONLY |
| Governance-mode decision-procedure domain | any tier in the row above | FLAG | **consensus / deliberative / landholder-franchise / oligarchic / royal-appointment / meritocratic-bureaucratic** | n/a | n/a — this is the value-space the row above draws from | n/a | n/a | n/a | n/a | none | **THIS REGISTRY'S OWN SYNTHESIS** [^m1] | **STUB** — no single canon doc states this closed six-value domain |
| Subnational-faction manager-type enum | Settlement (granted/revoked by Province) | FLAG (7-way, fully canon-enumerated) | {Church, Guilds, Ministry, Löwenritter, RM, Wardens, Niflhel} | none | each value carries its own Management Effect (+1 Piety/season, +1 Trade/season, Order-decay−1, …) | Quo Warranto's peninsula-wide echo rides this enum | none | n/a (discrete grant/revoke state) | NO (single grantor: Provincial Authority) | Contested-management → social contest; Charter tag on grant | `settlement_layer_v30` §3.3 | **LIVE** — "the literal, already-built implementation" of the row above, per `governance_type_registry_v1` §2.1 |
| Directive (type) + Governor Response | Province → Settlement | FLAG ×2 (6-way issuance + 3-way response) | one Directive/settlement/season | Defy/Divert writes Suspicion + Local-Actor Disposition/PS — the bottom-up half | the Directive itself — top-down half | none | none | n/a (fresh per-season choice) | **YES, by design — "the vise"**: Directive and settlement Needs (Family 6) compete for the same AP in the same season | Defy/Divert → Suspicion+1 → Recall threshold | `governance_play_redesign_v1` §1.4 | PROPOSED/STUB — supersedes `settlement_layer_v30` §3.2's older model pending OPT-16 |
| Franchise | Territory (province-tier node, T1–T17) | VECTOR (mostly-static) + FLAG shift-triggers | 0–5 | feeds National Influence as the weighting term | none (set by history/caste/institutional-presence, not seasonally imposed) | Church infrastructure counts in ANY territory with a Cathedral/parish regardless of controller | none | shift triggers only: ±1 per 4-stable-seasons / Accord-0-revolt / CI-60-seizure / coup / caste-reform(TBD); frozen while PI≤2; floored at 1 once ≥1 | NO (single shift-trigger table) | the shift triggers are the derived-flag layer | `franchise_v30` §2, §5 | **DRAFT — never promoted**; §8 flags a **BLOCKING** Church stat discrepancy |
| Territory Influence (TI) | Territory, per Faction | VECTOR | 0–7, `controller(+2)+infra(0–3)+npc(+1)+governor(+1)` | feeds National Influence's numerator | none | Church parish-network exception — same lateral reach as Franchise | none | NONE stated — recomputed fresh at Accounting | NO | none of its own | `franchise_v30` §3 | DRAFT — starting table itself "deferred to implementation" |
| National Influence | Faction-tier (derived from all territories) | VECTOR | 1–7, `clamp(round(Σ(TI×franchise)/Σ(franchise)),1,7)` | the formula itself — size/prestige-weighted, structurally parallel to Mandate but over Franchise×TI, not Weight×q_s | none — a pure read, used as Domain-Action roll pool | none | none | NONE — pure re-derivation at Accounting, stable within-season | see collision call-out below | none | `franchise_v30` §4 | DRAFT |
| political_value(faction) | Faction-tier (derived from territory-and-province holdings) | VECTOR | unscaled, `Σ(territory_value)+Σ(province_unification_bonus)`, scalars **TBD** | the formula's own aggregation (territory_value from type+Prosperity/Defense/Order) | unification bonus creates a top-down consolidation incentive, doesn't impose a value | none | none | n/a (recomputed from current holdings) | see collision call-out below | none | `valoria_political_hierarchy_v30` §2.4 (PP-726) | **STUB — scalars never calibrated**, doc itself flagged SUPERSEDED-PENDING-REWRITE [^m2] |
| **[CALL-OUT] Three competing "faction political power" formulas** | Faction-tier, three incompatible derivations | n/a — meta-row | n/a | n/a | n/a | n/a | n/a | n/a | **YES — this IS the collision** [^m3] | n/a | `franchise_v30` §4; `valoria_political_hierarchy_v30` §2.4; `settlement_layer_v30` §1.8 | **UNRESOLVED** — see §4 below for the full write-up |
| Charter tag (+ Patron field, Za model) | Settlement, survives succession | FLAG (durable + optional patron sub-field) | {present, absent} + patron_id | none | confers the manager-type's Management Effect | Za patron-lapse: Charter durability derives from a DIFFERENT actor's standing | none | event-triggered lapse only; age INCREASES revocation cost (prescription, ÷8 seasons/season) rather than decaying the Charter | NO | Charter-granted → §1.8a L+1; patron-lapse → "Patron's Rivals Move" Intrigue card | `settlement_layer_v30` §3.3a (ED-SE-0010), §3.3b (ED-SE-0021) | PROPOSED (§3.3a); **RATIFIED 2026-07-13** (§3.3b) |
| Quo Warranto | Settlement (contest) → peninsula-wide echo | FLAG (age-gated ≥16 seasons) | n/a | none | none | **the canonical lateral/dissemination example** — Order−1 in every settlement that faction-type manages peninsula-wide, on success | none | n/a | NO | none beyond the lateral echo | `settlement_layer_v30` §3.3a | PROPOSED, "Jordan-vetoable... the one bold stroke" |
| Recognition Fork (Confirm vs. New-Grant) | Faction-tier, any Formal Recognition Event/Recognized Deed | FLAG (binary) | {Confirm, New-Grant} | repeated Confirm choices are themselves a legible bottom-up-readable signal | Confirm eases Demotion thresholds w/o unlock; New-Grant unlocks Access + new Obligation | none | none | n/a | NO | none | `faction_politics_v30` §1.0b (ED-FA-0019) | PROPOSED — REFINE-THEN-RATIFY (granter rule + orphaned-New-Grant fate undefined) |
| Court Attendance + Hostage-Kin | Territory/Province governor ↔ Faction capital | FLAG (compliance action + optional bond) | n/a | skipping accrues Suspicion at double rate | faction may REQUIRE a hostage-kin | none | none | n/a | NO | hostage capture/threat → off-ladder Duty | `faction_politics_v30` §1.0c (ED-FA-0020) | **RATIFIED** (2026-07-13, no open sub-question) |
| Entry Terms (Confirm/Impose) | Settlement, at faction-control transfer | FLAG (small enum) | n/a | Confirm seeds L directly (non-stacking with §1.8a's ceremony event) | the incoming faction's choice | none | none | n/a (one-shot at transfer) | NO (de-conflicted by §1.8b's composition rule) | feeds a dormant sim proxy read by `faction_action.py`'s ED-FA-0013 conquest fork | `settlement_layer_v30` §5.3 (ED-SE-0011) | PROPOSED — **partly LIVE** via the dormant proxy |
| Seggio bespoke privilege | Settlement (Seat/City only) | FLAG — deliberately outside the uniform manager-type pattern | 1–5 recognized bodies/settlement, each with ONE bespoke gate | all resident Seggi share one joint Eletti-bloc vote | each Seggio gates one specific verb-option (Develop/Fortify/dispute-adjudication) | none | **explicitly exempt from Grant/Revoke/Quo-Warranto** — inherit/marry/seize-by-force only | n/a | NO | none yet — the "Mandate-Challenge" removal path is unauthored | `settlement_layer_v30` §3.3c (ED-SE-0024) | RATIFIED-architecture / Mandate-Challenge is a named GAP (E2) |

</div>

[^m1]: Assembled by cross-reading the four primary ladder headers — Crown = "Valorsmark Monarchy" (royal-appointment, per the deed-monarchy/royal-court worked example in `scale_hierarchy_v1` §5.4), Hafenmark = "Constitutional Duchy" (deliberative — Alderman council votes, Parliamentary committees), Varfell = "Jarl Confederacy" (landholder-franchise-flavored), Church = hierocratic/meritocratic-bureaucratic (Cardinal ladder + Consecration) — plus the Guildmaster Council's explicit "collective leadership by design" (oligarchic, `faction_politics_v30` §2.5). No single canon doc states these six values as one closed domain; this row names the gap the way `key_echo_armature_v1` §4 names the `Field`/`Gauge` gap — a synthesis proposal, not a citation.
[^m2]: `scale_hierarchy_v1` §6 item 1 explicitly lists "§2.4's political-value formula... NOT yet rewritten to match" the new Territory tier as tracked, unexecuted work.
[^m3]: See dedicated write-up, §4 below.

---

## §4 · The three competing "faction political power" formulas

Flagged explicitly per this docket's brief — **not previously named as a three-way collision in any
single source doc** (the two older docs predate the LPS-2e Mandate re-grain and were never reconciled
against it):

1. **Franchise-weighted National Influence** (`franchise_v30` §4) — `clamp(round(Σ(TI×franchise)/Σ(franchise)),1,7)`. Replaces the old scalar Influence stat; used as the roll pool for Domain Actions.
2. **`political_value(faction)`** (`valoria_political_hierarchy_v30` §2.4, PP-726) — `Σ(territory_value)+Σ(province_unification_bonus)`, scalars TBD. Explicitly described as feeding "parliamentary influence **and Mandate-track inputs**" — implying a fourth, never-defined composition with item 3.
3. **Faction Mandate** (`settlement_layer_v30` §1.8) — `round(7T/(T+6))` over settlement L/PS×Weight. Read by Parliament vote tallies (`faction_layer_v30` §5.3) and Church Excommunication Ob.

All three claim to answer "how much political power does this faction have," feed **overlapping**
consumers (Parliament, in particular, has at least two of the three cited as its input at different
points in the corpus), and none formally supersedes the others. `political_value()`'s own document is
additionally flagged SUPERSEDED-PENDING-REWRITE by `scale_hierarchy_v1`, and Mandate is separately
RULED-RETIRE-as-collapse-carrier (D4) while being explicitly **kept** as "the faction/parliamentary
meter" — meaning the retained, ratified formula (Mandate) and the two never-reconciled older formulas
(National Influence, political_value) now coexist with no adjudicating document. This registry does not
resolve the collision (read-only synthesis); it is handed to `gap_register_v1.md` / `decision_queue.md`
as a `needs_jordan` item.

---

## §5 · Family 4 — Caste & internal-population

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Caste composition (Northern/Central/Southern Einhir) | Settlement/Territory/Province | VECTOR | weighted demographic proportions, unscaled | population-weighted aggregation upward (inferred parallel to temperament aggregation — no dedicated formula authored) | baseline-TS differential propagates to individual NPC/PC generation | none native | none | n/a (a composition, not a decaying scalar) | NO | gates every rank-ladder/Renown/Disposition/Conviction row below | `faction_politics_v30` §3.1; `generation_sourcebook_v1` P9 | LIVE (prose); the aggregation formula itself is DOCTRINE-ONLY/inferred |
| Caste × Rank-advancement gate | Personal ↔ Faction-tier ladder | FLAG (per-faction-per-caste enum) | full-access / gated / favored / closed | none | the gate itself is the top-down effect (Ob modifier or hard closure) | none | Niflhel/Riskbreakers explicitly INVERT the gate (Southern Einhir favored) — a bend-around by design | n/a | NO | none beyond the gate table | `faction_politics_v30` §3.2 | LIVE |
| Caste as Renown/Initiation-Duty modifier | Personal | FLAG (rate modifier + Ob delta) | Renown halved (round down) for public Southern-Einhir actions in North/Central territory; Initiation Ob+1 in 4/6 factions | none | n/a — personal-scale only | none | covert actions explicitly UNAFFECTED (Shadow Renown is caste-independent) — bend-around within the same key | n/a | NO | none | `faction_politics_v30` §3.3, §3.4 | LIVE |
| Caste as Disposition-floor / Conviction-transgression risk | Personal | FLAG (starting-value table + threshold-gated crisis arc) | Disposition −2..+1 by NPC×caste; transgression Ob 1→2, Shake 1→2 seasons, self-applied Doubt Marker; 3+/year → mandatory Reformation (Spirit Ob 3) | none | n/a — personal scale | none | none | n/a | NO | Reformation Success/Partial/Failure branches (Renown±1, Standing−1-all, Piety-reset-5/5/5) | `faction_politics_v30` §3.5, §3.6 (ED-777) | LIVE |
| Demotion Magnitude ladder | Personal ↔ Faction-tier rank ladder | FLAG (severity-tiered state machine) | Standing N→N−1 (default) / N→N−2/−3 (severe) / Standing −1 dismissal (total) | none | faction-imposed consequence of a trigger event | none | cross-rank demotion explicitly SKIPS intermediate ranks — a genuine diagonal behavior within one scale | n/a (event-triggered) | NO | 2-season appeal window (faction-internal Piety-Track contest) | `faction_politics_v30` §1.0a (ED-776) | LIVE |
| Guild Entry Fork (Guarantor vs. Sole-patron) | Faction-tier (local), Gu-Std 0→1 | FLAG (binary + durable-tag consequences) | n/a | a triggered Demotion burns ALL 3–5 guarantors' Disposition + a durable Vouched-For grudge tag | none | the guarantor pool is itself a lateral social-collateral resource | none | n/a (durable tags, not decaying) | NO | "Vouches Carelessly" Precedent tag (sole-patron path) | `faction_politics_v30` §2.5a (ED-FA-0023) | **RATIFIED** |
| Guild Mastership Fork (Exam vs. capital buy-in) | Faction-tier (local), Gu-Std 1→2 | FLAG (binary + durable Upstart tag) | n/a | none | none | none | buy-in path explicitly SKIPS the Examination-committee gate above — a bend-around of another key's gate, purchased | Upstart's Disposition/mentorship penalties are TIME-BOUNDED (4 seasons) — the closest thing to a decay term in this family | NO | Upstart tag (peer Disp−2; 4-season Apprentice ban; −1 Ob for accusers) | `faction_politics_v30` §2.5a (ED-FA-0022) | **RATIFIED** |

</div>

---

## §6 · Family 5 — Religious / ideological (CI / Piety / heresy)

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Church Influence (CI) | Global/Peninsula | BOTH | 0–100, starts 28, ±5/season cap | Piety Yield = `Σ(PT-tier×SW-factor)` per Prominent territory — bottom-up | Institutional Weight `⌊CI/20⌋` injected into every Church-touched vote/margin; CI≥80 drifts ALL territory PT+1/Year-End | none native | none | **NONE — GAP** [^r1] | NO (single global scalar, one writer set) | milestones 40/55/65/80/100; a 75-vs-80 discrepancy vs. `conviction_track_v30` §11.3 is OPEN | `ci_political_v30` §2, §3; `clock_registry_v30` | LIVE |
| Spiritual Weight (SW) | Territory, fixed at game start | **VECTOR-but-static** | 0–5 (T15=0, T9=5) | weights CI's Piety-Yield and Church's parliamentary-pool bonus | none — a fixed attribute, not imposed | none | none | **NONE — explicitly intentional** (contrast CI above) | NO | none | `ci_political_v30` §1 | LIVE |
| Piety Track (PT) | Territory | VECTOR (dynamic, oscillating) | 0–5 (0=Restoration pole, 5=Piety pole) | feeds CI's Piety Yield, weighted by SW | CI≥80 drifts all-territory PT+1/Year-End — a top-down push back onto its own bottom-up source | high-SW territories get +1 die on PT-change actions (both directions) | none | **NONE stated** | **YES** — same collision shape as Mandate↔L/PS, not previously named as such [^r2] | none of its own beyond CI's milestone-driven drift | `clock_registry_v30`; `ci_political_v30` §1 | LIVE |
| Church Attention Pool (AP) | Territory | BOTH | 0–10, starts 0 | none | none (an accumulator, not itself imposed) | RM Cell Resilience (+1 Ob to Church suppression at ≥3-settlement Presence) counters Inquisitor pressure from this pool | none | **NONE — GAP** [^r3] | NO | first Inquisitor at AP≥3; second at AP≥6 | `clock_registry_v30`; `params_board_game.md` §Church Inquisitor | LIVE |
| CI Institutional Weight / Political Pool | Global CI → applied per-vote/margin at Faction-tier | VECTOR (derived) | Church +0..+5 votes/margin by band; opponents −0..−3, floored at 0 | none (pure derivation) | applied into every Parliamentary/resolver context Church touches | none | none | n/a (re-derived each use) | NO | none of its own | `ci_political_v30` §3.2–§3.4 | LIVE |
| Certainty | Personal | VECTOR (oscillating) | 0–5 (5=orthodoxy, 0=Thread acceptance) | none named | none | none | none | not specified in sources read — **flag for follow-up** | NO | none identified | `clock_registry_v30`; `params/core.md` §Certainty | LIVE (tracked); decay behavior out of this docket's read scope |
| Nine Political Axes | Faction-tier, echoed at Territory/Province via casus belli | VECTOR (qualitative, not tracked numerically) | 9 axes × 2 poles, positional | none (faction-authored, not derived) | frames Domain-Echo content and casus belli downstream | none | none | n/a (re-authored, not decayed) | NO | none — explicitly "not tracked numerically" | `faction_canon_v30` §7 | LIVE (qualitative framing only) |
| Substrate-posture (F1) | Faction-tier (identity axis, generation-time) | FLAG | 6-way enum, "never a palette-swap" (binding constraint M-4) | none | shapes the faction's whole behavioral posture downstream | none | none | n/a (identity axis) | NO | none | `generation_sourcebook_v1` §1.2 F1; `faction_canon_v30` §7 | DOCTRINE-ONLY — generation-time paradigm, not a runtime-enforced field |

</div>

[^r1]: `governance_type_registry_v1` §2.7: "only passive one-directional increase + an opposing-suppression lever (Baralta −1/season) — no natural decay term." CI runs to 100 with no freeze and no self-correction.
[^r2]: PT is bottom-up-source-of-CI *and* top-down-target of CI's own Ascendant-band effect — structurally identical to Mandate↔L/PS (Family 2) and Turmoil↔Accord (Family 7), just via a different variable pair.
[^r3]: `governance_type_registry_v1` §2.7: "No decay — pure accumulator."

---

## §7 · Family 6 — Economic / fiscal

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fiscal Stance (Light/Standard/Extraction) | Faction-tier or per-Province declaration, effect at Settlement | FLAG (3-way) | n/a | none | pairs with compliance(L) — textbook top-down-policy → yield-function pair | none | none | n/a | NO | stance-broken → §1.8a L-channel −1 event | `faction_layer_v30` §5.9 (ED-FA-0008) | **STILL PROPOSED-only** — no Treasury sim coupling yet |
| Treasury | Faction-tier, aggregated from Settlement Prosperity | VECTOR | unbounded, `Σ settlement Prosperity × 10` | the formula itself — clean bottom-up, no mid-tier | funds Court-Attendance travel, Domain Actions, etc. | none | Settlement→Faction direct (bypasses Territory/Province, same skip shape as Mandate/National Influence) | **NONE stated at the aggregate** | NO (nothing writes it top-down) | Treasury→0 triggers governing-player Renown risk | `governance_ripple_substrate_v1` §7; `derived_stats_v30` §8.1 | LIVE |
| Prosperity — **naming collision** | (a) Settlement, 0–5, LIVE/wired; (b) legacy Territory/province-node, 1–7 (board-game table), unclear if still live | VECTOR at both grains | **0–5 vs. 1–7 — UNRECONCILED** | Settlement Prosperity → Treasury; also feeds Settlement Weight | Prosperity-inheritance on control-transfer (unchanged across conquest, ED-794) | Weight-as-Exit's destination settlement gains +0.5-Prosperity-growth (lateral transfer between neighbors) | none | NONE at either grain (development-only, moves via Govern/Develop, not ambient) | N/A as a driven-value race; **YES as a naming collision** | Prosperity-0 → Dearth-chain entry | `settlement_layer_v30` §1.3 (0–5, live); `clock_registry_v30`/`params_board_game.md` §Territory Table (1–7, legacy); `governance_type_registry_v1` §2.8 | settlement-grain LIVE; territory-grain **status unclear** |
| Ledger-of-Consequence tag family (Precedent/Grudge/Debt/Reputation/Leverage + Compact) | Settlement, per-governor tenure, survives succession | FLAG ×5 canonical + 1 resolved-contested | TTL'd durable tags | none | none (settlement-local memory) | Grudge raises hostile-action weight / seeds Intrigue cards — same-scale contagion | none | TTL-bounded per tag, no general decay function — each family's expiry is bespoke | **RESOLVED 2026-07-13** (D3) [^e1] | Reputation is itself a VECTOR-derived FLAG (Just/Harsh/Generous/Weak/Hated) | `governance_play_redesign_v1` §1.6; `governance_consolidation_v1` D3 | base 5-family ledger LIVE; Compact-as-Debt **RATIFIED** |
| Dearth chain / Grain-route dependency | Granary: Settlement; routes: Territory/Province | Granary=VECTOR(0–3); response=FLAG; route-dependency=FLAG | 0–3 Granary | none | none | **the canonical geographic-lateral example** — cutting a route puts every dependent settlement one season from Dearth, via the adjacency graph, not the scale hierarchy | none | n/a (moves via harvest/consumption events) | NO | Dearth-relieved → §1.8a PS+2; ≥2-consecutive-seasons → Weight-as-Exit trigger | `settlement_layer_v30` §4.3a (ED-SE-0008), §4.3b (ED-SE-0009) | PROPOSED |
| HRE-4 Borrow | Faction-tier / Settlement | FLAG (discrete instrument, own state machine) | n/a | none | none | none | none | n/a (own discovery/clawback state machine) | NO | discovery/clawback events | governance-compendium (ED-FA-0029) | PROPOSED — "NERS-confirmed clean KEEP" |

</div>

[^e1]: PR#119 proposed Compact as a genuine 6th ledger family; RULED instead to model it as a recurring, fixed-term `Debt` subtype (`Debt(key="compact:<quota>", ttl=term, recurs=True)`) — the built `ledger.py` stays 5 families.

---

## §8 · Family 7 — Cross-cutting clocks (MS / Π / CI / IP / Turmoil)

*CI and Church Attention Pool are fully tabled in Family 5 (their religious-content home) — cross-referenced
here, not duplicated, since this family's own name lists CI as one of its members.*

<div style="overflow-x: auto;">

| Key | Scale(s) | Class | Range | Agg↑ (UP) | Prop↓ (DOWN) | Lateral↔ | Skip/Bend | Decay_fn | Collision? | Derived Flags | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mending Stability (MS) | Peninsula/Global, graduated per-territory by node-distance (d1–d5) | BOTH | 0–100, starts 60 (videogame) / 72 (lore, reconciliation pending) | none (a global clock) | distance-graduated territory effects — d1 feels bands earliest/hardest, d5 never affected | Turmoil Collapse-band (9–10) adds MS−1/season — cross-clock coupling | none | **FULLY SPECIFIED — the strongest template in the corpus** [^c1] | NO (single global scalar; territory effects are read-only derivations) | band-crossings at 20/40/60/80, each with independent falling/rising thresholds | `clock_registry_v30`; `ms_trajectory_v1` §5.1 (ED-882) | LIVE |
| Pressure (Π) | Settlement, "Cooling flag" cascades peninsula-wide when triggered | BOTH | 0–10 | none (per-settlement homeostat) | draw-rate scales with Π (`1+floor(Π/3)` cards/season) | none native (each settlement's Π independent) | none | **FULLY SPECIFIED, PARTIALLY PORTED** [^c2] | NO (single-settlement-scoped, all-same-scale inputs) | Π≥8 forces a Crisis card | `governance_play_redesign_v1` §2.1; `governance_consolidation_v1` §3 E1, §6 item 7 | LIVE (base clamp) / DESIGNED-NOT-PORTED (E1 restoring term) |
| Institutional Pressure (IP) | Global, aggregated from per-territory Accord-threshold counts | BOTH | 0–100, starts 20 | stepwise threshold aggregation (0-1→+0; 2-3→+1; 4-5→+2; 6+→+3) + CI≥60→+2/season + faction-elim+2 once | IP≥100 fires `mechanical.era_transition` (registered, currently gateless) | **explicitly NO direct feed with Turmoil** despite sharing the same Accord≤1 source signal — a deliberate non-coupling | none | **NONE specified — GAP** [^c3] | NO (shares a source with Turmoil but the two tracks are explicitly independent, non-double-counting by design) | IP 60/80/90 "authored beats" (stranded prose); IP=100 world-state transition | `peninsular_strain_v30` §3.2, §4.4; `clock_registry_v30` | LIVE (aggregation); beats NOT YET WIRED |
| Turmoil / Strain | Global, aggregated from per-territory Accord | BOTH | 0–10, starts 0 | +1/Accord≤1 territory (capped +3/season) + faction-elim+2 (uncapped) + Revolt+1/event (uncapped) | band-threshold effects force Accord DOWN at Fracture(5-6)/Crisis(7-8)/Collapse(9-10) | Treaty-pair decay (−1/pair, capped −2/season) is explicitly lateral-diplomatic — bilateral relations reduce a global track regardless of a third party's war | none | **FULLY SPECIFIED decay pair — the corpus's other strong template** [^c4] | **YES** — bottom-up from Accord AND top-down-forces Accord in the same Accounting; ED-SE-0002 stacking-with-Domain-Echo fork OPEN | bands 3-4/5-6/7-8/9-10 (Tension/Fracture/Crisis/Collapse); Tension hits a **"Legitimacy −25"** buffer — see bonus collision, §9 | `peninsular_strain_v30` §4 | LIVE |
| `decay()` (OF-3) — substrate infrastructure | substrate-wide, would serve every VECTOR above with no bespoke logic | infrastructure, not itself a key | n/a | n/a | n/a | n/a | n/a | **this row IS the decay mechanism — DEFERRED** [^c5] | n/a | n/a | `key_echo_armature_v1` §5.2 (OF-3); `governance_type_registry_v1` §4.1 | **DEFERRED/OPEN** — the single highest-leverage gap every "NONE — GAP" row above points back to |
| `Field`/`Gauge` primitive proposal | would exist wherever a VECTOR needs continuous read/write between Key emissions | infrastructure proposal | n/a | proposed required `aggregate_fn` field | proposed required `propagate_fn` field | not addressed by the sketch | n/a | proposed required `decay_fn` field — the schema-level fix for every GAP row in this registry | n/a | proposed `derived_flags` field — formalizes the VECTOR-with-derived-FLAG pattern as first-class schema | `governance_type_registry_v1` §4.1–§4.2 | **PROPOSED SKETCH, NOT RATIFIED** |

</div>

[^c1]: Logarithmic recovery force + **hysteresis** (falling edges 20/40/60; rising/recovery edges require the falling edge **+8 MS** — e.g. Critical↔Fractured at 20/28) + a **12-MS leading-warning window** approaching each tip from above + the MS→0 Post-Calamity deepest-tip extension of the same warning logic.
[^c2]: LIVE clamp: `Π_next = clamp(Π + unserved-Needs + active-Grudges + NPC-ambitions + external-shock − player-releases, 0, 10)`. A bidirectional restoring term `sign(3−Π)·min(1,|3−Π|)` (E1/CG-1, from `goldenfurt_slice`) is designed but NOT ported — `governance_consolidation_v1` explicitly blocks greenlighting this port *alone* (needs E1+E3+E7 bundled). Four independent measurements confirm the unaugmented clamp alone does not de-fang the negative-death-spiral bias.
[^c3]: `governance_type_registry_v1` §2.7: "stepwise aggregation specified; no ordinary per-season decay specified."
[^c4]: −1/Accounting if no territory-instability advanced that season; −1 per active Treaty pair (cap −2/season); −1 for public diplomatic resolution (max 1/season, one source).
[^c5]: Jordan's 2026-07-07 ruling (ED-IN-0026, §5.2): substrate ships WITHOUT decay; authorship deferred "to when cross-tick convergence work actually starts." `governance_type_registry_v1` (§2.7, §4) argues this docket IS that trigger — MS and Π now supply two working templates (hysteresis-and-falloff; homeostat clamp) to generalize from.

---

## §9 · Same-name / different-scale collisions (explicit register)

The five collisions `governance_type_registry_v1` §2.8 named, plus one this registry found while
tracing Turmoil's Tension-band effect (bonus, flagged as such — not previously catalogued):

| Name | Colliding definitions | Where in this registry | Status |
|---|---|---|---|
| **Prosperity** | Settlement (0–5, wired) vs. legacy per-Territory (1–7, board-game table, unclear if still live) | §7 (Family 6) | unreconciled |
| **Disposition** | Personal/fieldwork (−5..+5, per-NPC-per-PC) vs. Settlement Local-Actor (−5..+5, same range, different subject pool, no cross-reference found) | not separately tabled above (a fieldwork/personal key, out of this registry's governance/legitimacy/authority/standing core scope) — flagged here for completeness per the docket brief | unreconciled |
| **Guild Favour/Favor** | Per-Territory (0–7) vs. per-Settlement (1–7, different start rule) | not separately tabled above (an economic/fiscal-adjacent track outside this registry's core scope) — flagged here for completeness | unreconciled |
| **Standing/Reputation** | Faction-oscillating (0–5) vs. an apparently-higher-range personal/PC standing implied by "Standing-6+" gates elsewhere | §2 (Family 2) | unreconciled |
| **Mandate** | Settlement-derived faction meter (§1.8, `round(7T/(T+6))`) vs. an unrelated CI-driven `settlement_mgmt` M12 parliamentary meter | §2 (Family 2); D4 already flags this, rename pending | **rename ruled (D4), not yet executed** |
| **Legitimacy** *(bonus find, this registry)* | Per-settlement L (0–7, `settlement_layer` §1.8) vs. the **faction-level derived buffer meter** "Legitimacy (derived) = Mandate × 20" (0–140-ish, `derived_stats_v30` §3) — the SAME word, at the SAME faction scale as Mandate, one field above (L) and one field derived-from-Mandate. `peninsular_strain_v30` §4.3's Turmoil-Tension effect ("Legitimacy −25 at Accounting") hits the *derived buffer*, not the 0–7 settlement value — easy to misread given both are named identically and both live in the same Faction/Turmoil sentence | §2 (Family 2, L row) cross-references; the buffer meter itself is not separately tabled (it is a display derivation of Mandate, not an independently-driven key) | **newly surfaced by this registry** — not in `governance_type_registry_v1`'s five |

---

## §10 · GAP register — inert / no-decay keys, explicit

Per the docket brief's own worked examples, cross-checked against every `NONE — GAP` cell above:

- **L/PS inert 100/100** — `settlement_layer_v30` §1.8's Legitimacy and Popular Support are fully specified in ratified prose (LPS-2e) and consumed by Mandate, Strictness, compliance(L), and the whole governance-cascade consent-gate (`scale_hierarchy_v1` §4) — yet confirmed **100/100 inert** by `tools/sim_harness`'s `lps_inert_check`. This is now named the single highest-priority open wiring gap in the entire governance/generation thread (`scale_hierarchy_v1` §4, `governance_consolidation_v1` E5). Every downstream consumer in §2/§3/§6/§9 above is functionally inert as a consequence, regardless of its own ratification status.
- **ΔLegitimacy has no decay term** — `faction_behavior_v30` §3.5's formula is purely additive/subtractive-on-event (continuity, procedural, expectation, violation terms); nothing pulls L back toward a baseline absent an event. The only reversion anywhere in the L/PS system is Mandate's separate, bidirectional mean-reversion feedback — a different mechanism serving a different purpose (homeostasis around the faction's own aggregate, not temporal decay).
- **OF-3 `decay()` deferred** — the Key & Echo Armature's own generic decay function (`key_echo_armature_v1` §5.2) was explicitly deferred by Jordan's 2026-07-07 ruling "to when cross-tick convergence work actually starts." Every GAP row in §2/§6/§8 above (L, PS, ΔLegitimacy, ΔPopular_Support, Church Attention Pool, CI, IP) is a standing instance of exactly this deferred fork — this registry is direct evidence, per `governance_type_registry_v1` §4, that the deferral now has real downstream cost, and two working templates to generalize from (MS's hysteresis-and-falloff; Π's homeostat clamp).
- **Suspicion's decay is ruled-in-principle but unauthored** — D6/E11 (2026-07-13, ED-IN-0047) mandate a symmetric compliance-decay term as a co-requisite of ratifying cumulative accrual, but "specific decay curve... is authoring-level detail" — the curve itself does not exist yet. Distinct from the pure-omission GAPs above: this one has a ruling, just not a mechanic.
- **Church Attention Pool, CI, IP** — each confirmed "no decay/no natural decay/no ordinary per-season decay" by `governance_type_registry_v1` §2.7 directly; carried into §6/§8 above unchanged.
- **Renown and Spiritual Weight are NOT gaps** — both are explicitly, intentionally non-decaying by design (stated in their own source docs). Listed in §2/§6 for completeness, not as omissions.

---

## What this registry does and doesn't do

**Does:** enumerate every governance/legitimacy/authority/standing key found across the seven read source
docs, at every scale each was found at; bind each to the Key & Echo Armature's six propagation directions
via the column schema above; explicitly surface the five `governance_type_registry_v1` §2.8 collisions
plus one this pass found (Legitimacy's own buffer-meter double-meaning); explicitly name the three
competing faction-political-power formulas and the standing GAP list (inert L/PS, no-decay ΔLegitimacy,
deferred OF-3, unauthored Suspicion-decay curve); mark every key's ratification/wiring status honestly
(LIVE/INERT/DOCTRINE-ONLY/STUB) rather than defaulting to the most-flattering reading.

**Doesn't:** rule any open fork (ED-SE-0002's Accord-stacking question, the political-power three-way
collision, OF-3's `decay()`, Suspicion's decay curve, the Standing-range reconciliation, or any other
`needs_jordan` item surfaced above); flip any source doc's `## Status:` line; wire any inert field; or
invent a mechanic beyond what a cited source already specifies. Open items are handed to this docket's
`gap_register_v1.md` and `decision_queue.md` (both pending, per the docket `README.md` manifest) rather
than resolved here.
