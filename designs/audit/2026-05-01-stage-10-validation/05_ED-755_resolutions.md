# ED-755 Resolutions — Doc 17 §6 Jordan-Decision Sweep

**Session:** 2026-05-01-stage-10-validation
**Source ED entry:** `canon/editorial_ledger.yaml` ED-755
**Source decision queue:** `designs/audit/2026-04-30-architecture-session/02_workplan_v3_addendum.md` §D.1 + §D.2
**Original audit:** `designs/audit/2026-04-28-political-dynamics-session/16_session_close_observations.md`

---

## §1 Scope and method

ED-755 has been the single P1 blocker in the editorial register since 2026-04-29. It bundles nine Jordan-decision items, each with a proposed default in doc 17 §6. This document evaluates each item against the current canonical architecture (PP-684, PP-685, PP-686 v2, PP-687, PP-688) and applies the proposed default where appropriate, or surfaces the item to Jordan with framing where a default cannot be applied.

The original audit findings (E-38-A/B, E-TOP-A, ST-31-B, R-41-A) are scored against `12_development_specification.md`, which the architecture redesign (PP-686 v2 + PP-687 + PP-688) has substantively superseded. Several findings are therefore **architecturally resolved** by the redesign rather than requiring a fresh spec patch — the document records this where applicable.

Items in §2 below are applied (default accepted; ledger updated). Items in §3 are surfaced to Jordan with framing and options — they cannot be defaulted and are spun out to new ED entries.

---

## §2 Resolved by default application

### §2.1 D1.1 — E-38-A symbolic_effects table — KEEP

**Original audit (16_session_close_observations §2 row E-38-A):** "symbolic_effects | E | Design-Fail | Consumed by no procedure — 210-entry table mechanically inert."

**Architectural status:** the symbolic_effects table lives in `12_development_specification.md` (audit-archived). It has not been migrated into any Phase 5a canonical doc. The table itself is **content data** (210 entries) that has authoring value even if its mechanical hookup was deferred at the time of the audit.

**Default applied:** KEEP. Cutting would require 210 inline definitions at use sites, which is strictly worse for maintenance and discoverability. The table is preserved as a referenceable data resource until D1.2 specifies its mechanical consumption.

**Action taken:** none on the table itself (it was not at risk of being cut in any active branch). Editorial note recorded.

---

### §2.2 D1.2 — E-38-B symbolic_effects mechanical hookup — DEFINE as Concern salience modifier

**Original audit (16_session_close_observations §2 row E-38-B):** "symbolic_effects | N | Design-Fail | 210 authored entries with zero mechanical output — waste if uncorrected."

**Audit-proposed mechanism:** "Concern salience modifier" (per the same session-close observations: "Decision: define symbolic_effects consumption (Concern salience modifier) OR cut the 210-entry table").

**Architectural status:** PP-688 articulation layer §2 specifies Concern salience as the surfacing mechanism for Tier 1 protagonist UI. Concern salience is computed from Key payload + protagonist context. The 210-entry symbolic_effects table maps event archetypes to (Conviction-axis, polarity) pairs — exactly the data structure needed to drive a Concern salience modifier.

**Default applied:** DEFINE. The canonical mechanical consumption of `symbolic_effects` is:

> When a Key fires whose `type` matches a `symbolic_effects` table row, the
> articulation layer reads the row's `(axis, polarity, intensity)` triple and
> applies it as an **additive modifier to the protagonist's Concern salience**
> for that Key. The modifier is added to the §3.2 significance components
> before the §3.5 protagonist extensions but does not contribute to the
> universal-track significance used for Tier 3 chronicle ranking.

**Implementation note:** this modifier should be added as a new §3.2 component (`symbolic_effect_weight`) when the symbolic_effects table is migrated into canonical scope (a follow-up session — the table itself remains in audit-archived territory until that migration). Until then the Tier 2 significance formula in `ArticulationLayerV30.compute_significance` is correct as-built; the symbolic_effect_weight component is a 0-valued slot waiting for the table migration.

**Forward gate:** the symbolic_effects migration is not blocked by ED-755 closure — it can proceed independently when the political-dynamics-spec migration sequence reaches it (likely after Mandate OQs settle and §3.6 mechanical work runs).

---

### §2.3 D1.3 — E-TOP-A diagonal-chain opacity stance — SURFACE

**Original audit (16_session_close_observations §2 row E-TOP-A):** "Player intuition | E | Gap | Design stance needed: opaque-by-design vs legible-by-design."

**Architectural status:** ALREADY IMPLEMENTED via Phase 5a session 4 (`scenes/diagnostics/WhyDiagnostic.tscn` + `systems/diagnostics/WalkBackQuery.gd`, valoria-game commit cd3051c). PP-687 §5.4 specifies the "Why?" diagnostic as a player-facing legibility surface for backward causal walks; the Phase 5a implementation realizes the SURFACE default end-to-end (visibility-filtered walks, Tree-control rendering of cause chain).

**Default applied:** SURFACE — and it is built. Diagonal causal chains are legible-by-design via the WhyDiagnostic UI, filtered by the observer's visibility list per PP-687 §3 visibility model.

**Action taken:** WhyDiagnostic.tscn already in valoria-game (cd3051c); 12 GdUnit tests pass. This item is closed and the implementation reference is the authoritative answer.

---

### §2.4 D1.4 — ST-31-B NPC self-monitoring scope — PARTIAL

**Original audit (16_session_close_observations §2 row ST-31-B):** "NPC self-monitoring | Design choice | No Concern generated on sensitive information disclosure."

**Architectural status:** the redesign keeps NPC awareness driven by Key visibility (PP-687 §3) and Concern surfacing (PP-688 §2). NPC self-monitoring — i.e. an NPC noticing themselves disclosing sensitive material — is not currently wired. PP-688 §2 protagonist Concerns are surfaced based on Key visibility from the protagonist's perspective; NPCs do not yet have a parallel surfacing pipeline.

**Default applied:** PARTIAL. Canonical stance:

> NPCs self-monitor on **Tier-2-trigger-firing Keys involving themselves as
> actor or target** (the same set of Keys that fire cut scenes per
> ArticulationLayerV30 §3.1). They do **not** self-monitor on every Key
> that mentions them — that would be cost-prohibitive and produces no
> player-facing benefit (NPCs whose self-monitoring never surfaces in UI
> is dead computation).

**Implementation note:** when NPC Concern surfacing is built (post-Phase-5a, Item 14 territory of the next_action queue), the layer should reuse `ArticulationLayerV30.evaluate_trigger_ruleset` to gate NPC self-monitoring rather than introducing a parallel rule set. This guarantees Tier 2 cut-scene events and NPC self-monitored events stay in lockstep.

---

### §2.5 D1.5 — R-41-A crisis masking persistence — PERSISTENT FLAG WITH DECAY

**Original audit (16_session_close_observations §2 row R-41-A):** "Crisis masking | R | Design choice | Player can suppress anomaly detection via manufactured crises; persistence counter optional."

**Architectural status:** crisis masking is not wired in any current canonical doc. The session-close categorization explicitly lists it as "Document as featured behavior (no spec change required)" (item 42 in §10).

**Default applied:** PERSISTENT FLAG WITH DECAY. Canonical stance:

> When a player or faction action manufactures a crisis sufficient to mask
> ongoing anomaly detection, the engine sets a **persistent crisis-mask
> flag** on the affected detection layer. The flag decays linearly over a
> spec-defined window (default: one year from the masking event). During
> the active window, anomaly detection is suppressed for the masked
> category; during decay, detection probability ramps back from 0 to
> nominal proportional to (time-since-mask / decay-window).

**Implementation note:** the crisis-mask flag should attach to the `anomaly_detection` layer when that layer is implemented (post-Phase-5a). It does not affect any Phase 5a built code. Recorded as featured behavior; no patch needed against current canon.

---

### §2.6 D2.3 — Knot Formation During Play — APPLY default procedure

**Doc 17 §6 default (per workplan_v3_addendum §D.2 D2.3):** "Disposition+5+TS≥30 → Spirit/TN7/Ob2 procedure approve or revise."

**Architectural status:** PP-688 wires the Key (`meta.knot_formed`) and the cut-scene picker for trigger 6 (`_pick_knot_formed` in `ArticulationLayerV30.gd`, valoria-game e6772a4). What is missing canonically is the **trigger procedure** — the conditions under which the Key emits.

**Default applied:** the doc 17 §6 procedure is accepted. Canonical procedure:

> **Knot Formation During Play.** When two characters' Disposition rises
> by ≥5 within a Trust Score window of TS ≥ 30, the engine triggers a
> Knot-formation contest:
>   - Stat used: **Spirit**
>   - Target Number: **TN 7**
>   - Obstacle: **Ob 2**
> On success, `meta.knot_formed` Key emits with both characters in
> `actors`. On failure, Disposition is locked at +4 (no Knot formed,
> no further Knot attempts that season).

**Cross-reference notes:** Disposition / Trust Score are PP-686-era personal-scale metrics. PP-684 13-Conviction taxonomy includes Spirit; PP-687 Key registry includes `meta.knot_formed` (Class B); PP-688 articulation layer §6.1 cites the Key. The procedure above is consistent with those canonical surfaces and does not patch any existing Phase 5a doc.

**Forward gate:** when a `designs/personal/knot_v30.md` doc is authored (currently no canonical home), this procedure is its §1.1 (Knot Formation During Play) content. Until then the procedure is recorded here and listed in the editorial ledger as resolved.

---

### §2.7 D2.4 — Accord propagation to settlement Order — APPLY default formula

**Doc 17 §6 default (per workplan_v3_addendum §D.2 D2.4):** "`Province Accord = floor(mean settlement Order)` approve or revise."

**Architectural status:** Accord at the province (territory) level is not present in any canonical Phase 5a doc. Settlement Order is a settlement-scale metric used in PP-686-era political dynamics. The formula propagates a settlement-scale value upward to a territory-scale value.

**Default applied:** the doc 17 §6 formula is accepted. Canonical formula:

> **Province Accord propagation.**
> ```
> Province Accord = floor(mean(settlement.Order for settlement in province.settlements))
> ```
> The floor operation is integer floor, not arithmetic floor, applied
> after computing the arithmetic mean across all settlements in the
> province.

**Cross-reference notes:** when Province Accord is consumed by faction_behavior_v30 §3.5/§3.6 (PP-686 v2 cascade fidelity formula), the formula above is its computation method. Until then the formula is recorded here and listed in the editorial ledger as resolved.

**Forward gate:** when `designs/territory/territory_v30.md` (or equivalent province-canon doc) is authored, this formula is its province-level Accord clause.

---

## §3 Surfaced to Jordan — cannot apply default

### §3.1 D2.1 — Intelligence stat as 6th faction stat — DIRECT CONTRADICTION

**Status:** workplan_v3_addendum §D.2 D2.1 explicitly flags this as needing resolution: "c2effdd argued from Renaissance political-infrastructure review; ED-748 had STRUCK it as redundant. **Direct contradiction needs resolution.**"

**Cannot apply default** — there is no proposed default. The two competing positions are:

> **Position A (restore — c2effdd):** Intelligence is a 6th faction stat.
> Renaissance political-infrastructure review identifies intelligence
> capability (gathering, analysis, counterintelligence) as distinct from
> the existing Military / Diplomacy / Economy / Culture / Government axes.
> Treating it as a derived attribute of Government underweights its
> mechanical role in covert action and information asymmetry.

> **Position B (keep STRUCK — ED-748):** Intelligence is redundant.
> Government already covers institutional capability for information
> handling; modeling Intelligence as a separate stat creates a 6th axis
> that must be authored across all 6 factions and tested for cascade
> interactions, with no clear mechanical hook that Government cannot
> already provide.

**Spun out to new entry:** ED-787 (P1 — direct contradiction blocking faction stat schema closure). Jordan picks a position; ED-787 closes with the chosen position and a cross-reference note in either c2effdd or ED-748 (whichever is overridden).

---

### §3.2 D2.2 — LICENSE / GOV-08 — CHOOSE LICENSE

**Status:** workplan_v3_addendum §D.2 D2.2 lists this as a license choice with no default proposed. Common videogame-design license options surfaced: CC-BY-SA, GPL-3, proprietary, CC0.

**Cannot apply default** — license selection is a Jordan-only call and propagates beyond mechanical design (it affects every contribution to the repo permanently).

**Brief framing of options:**

> **CC-BY-SA 4.0** — share-alike copyleft; derivatives must use the same
> license. Common for design-corpus projects. Permissive for non-commercial
> reuse; constrains commercial fork into separate licensing.

> **GPL-3** — strong copyleft; appropriate if Valoria becomes a code-first
> project where source distribution is the sharing surface.

> **Proprietary / All Rights Reserved** — locks the repo as private IP.
> Appropriate if Valoria is a commercial title in development.

> **CC0** — public domain dedication. Maximal reuse, no attribution
> requirement. Appropriate if the project is design-research with no
> commercial intent.

**Spun out to new entry:** ED-788 (P2 — not blocking active mechanical work, but blocks any external contribution or repo publication).

---

## §4 Editorial ledger updates

The companion ledger commits this session apply:

1. `ED-755` → status `closed`, resolution: "7 of 9 sub-items resolved by default application (D1.1, D1.2, D1.3, D1.4, D1.5, D2.3, D2.4); D2.1 and D2.2 spun out to ED-787 and ED-788 respectively. See `designs/audit/2026-05-01-stage-10-validation/05_ED-755_resolutions.md`."
2. `ED-787` (new) — P1 — Intelligence-stat contradiction (Position A vs B).
3. `ED-788` (new) — P2 — LICENSE selection.

P1 blocker count drops from 1 → 1 (ED-755 closes; ED-787 opens). The
substance changes: ED-755 was a 9-item bundle blocking on bundle-scoped
indecision; ED-787 is a single, well-framed binary choice.

---

## §5 What this resolution does NOT do

- Does not migrate the symbolic_effects 210-entry table into canonical
  scope. The table remains in audit-archived territory until the
  political-dynamics-spec migration sequence reaches it.
- Does not patch any Phase 5a doc. All defaults applied land as editorial
  decisions; mechanical specs (§2.6 Knot procedure, §2.7 Accord formula)
  are recorded here for future canonical-doc lift-out, not added to
  existing canon in this session.
- Does not implement the NPC self-monitoring layer or crisis-masking
  layer. Those are featured-behavior records; implementation lands when
  the surrounding system is built.
- Does not pick a position on D2.1 (Intelligence) or a license for D2.2.
  Both are surfaced for Jordan in §3.

---

**End ED-755 resolutions.**
