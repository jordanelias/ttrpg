# Valoria — Integrated Mechanics Design Document

**Version:** 3.1
**Date:** 2026-05-25
**Status:** PROPOSAL — pre-canon, pending Sprint 0 audit completion + Jordan review + sim Stage 10 validation
**Scope:** 31 mechanics across settlement / province / faction / scene layers covering politics, factions, territorial dynamics, religion, secession, foreign pressure, horizontal cohort dynamics, and postwar political settlement
**GD compliance:** preserves GD-1 (peninsula-only victory), GD-2 (mandatory threat response), GD-3 (insurgency pipeline)
**Historical grounding:** validated against `institutional_persistence_pre1600.md` (13 case studies)
**Companion:** `valoria_workplan_v1.md`

---

## §0 Reading this document

This is a **testable specification**, not a narrative description. Each proposal has the structure:

1. **Header** — ID, name, phase, audit status
2. **Modifies** — which existing canon docs this touches
3. **Mechanic** — the actual rule(s)
4. **Effects** — what changes when the mechanic fires
5. **Calibration** — numeric values marked as starting-values, with sim-validation flags
6. **Supersession** — what existing canon this replaces or modifies
7. **Composition** — how this interacts with other proposals
8. **Historical anchor** — cited source case
9. **NRES verdict** — Necessary / Robust / Smooth / Elegant check
10. **Test conditions** — what sim should verify

**Phase ordering:** proposals are sequenced A → B → C → D by interaction risk. Phase A commits first; Phase D requires prior phases to stabilize in sim.

**Audit statuses:**
- **COMMIT** — passed bottom-up canon audit + four-interrogation NRES audit + source-doc audit
- **COMMIT-REVISED** — revisions applied; commit-ready
- **COMMIT-WITH-CALIBRATION-FLAG** — sim work needed on specific parameters
- **DEFER-PENDING-AUTHORING** — cannot commit until specific follow-up authoring complete
- **UN-NRES-AUDITED** — has not been through four-interrogation NRES audit
- **`[AUDIT-FLAG]`** — supersession claim against canon NOT yet verified by canon-reading

**Three composition layers:**

| Layer | Function | Proposals |
|---|---|---|
| 1 — Military costly at settlement scale | Military victory cheap to execute, expensive to consolidate | P1, P2, I3, F3 |
| 2 — Non-military institutions gain granular relevance | Player feels institutional dynamics at scale-of-play | P3, P4, P6, P8, R3, R4, F2, H2, H3, PT2 |
| 3 — Alternative non-military reorganization paths | Political change without military force | P7, P9, I1, I2, PR3, PT1, Crown Legitimacy Contestation |

---

## §1 Framing and design intent

Three concerns drive the set:

**1. Military conflict without rendering institutions useless.** Conquest stays cheap to execute; consolidation becomes expensive. Non-military institutions (parliament, treaty, league, mediator, confessor) gain granular settlement-scale and personal-scale expression so the player feels their relevance at the scale of play, not just as faction-stat readouts.

**2. Substrate-as-political-medium.** Settlement primitives carry political weight that propagates upward through articulation tiers. Faction-scale aggregates (Mandate, Stability, CI, IP) do not capture the spatial and individual-scale heterogeneity that historically determined persistence under armed internal conflict.

**3. Graduated states between binary positions.** Where canon currently has binary states (concur/refuse, vassal/sovereign, hostile/allied, orthodox/heterodox, treaty-bound/unbound), the historical reality was a gradient. Most proposals add intermediate states with discrete transition rules.

---

## §2 Three-condition framework alignment

The integrated set addresses each of the three necessary conditions for institutional persistence under armed internal conflict (per `institutional_persistence_pre1600.md` Part IV):

| Condition | Definition | Proposals |
|---|---|---|
| **(a) Substrate thickness** | Dense lower-level institutions continuing while state-level is contested | P1, P2, P3, P4, R1, R3, I3, F1, F3 |
| **(b) Shell legitimating value** | The contested institution worth controlling rather than destroying | P6, P7, P10, R4, F2, H2, H3, PT1 |
| **(c) Accommodation form** | Constitutional codification or implicit toleration | I1, I2, P8, P9, PR3, Crown Legitimacy Contestation |

All three conditions are necessary; none alone is sufficient.

---

## §3 Proposal inventory

**31 proposals total**, distributed across four phases.

### Phase A — Pure additions (lowest risk) — 7 proposals
P1, P7, P10, P11, R1, I3, F1

### Phase B — Calibration risk — 4 proposals
P2, P3, P4, F3

### Phase C — Modifying existing canon (medium risk) — 12 proposals
P6, P8, R2′, R3, R4, F2, H1′, H2, H3, PR1, PR3, PT2

### Phase D — Highest-interaction (sim-validation required) — 8 proposals
P9, I1, I2, F4, PR2, PR4′, PT1, Crown Legitimacy Contestation

### Special status proposals
- **PR2** (Phase D): DEFER-PENDING-AUTHORING (postwar tribunal procedure must be authored first)
- **PT1, PT2, Crown Legitimacy Contestation**: UN-NRES-AUDITED (require four-interrogation NRES audit before sim)

---

## §4 Pre-execution work required (Sprint 0)

**Before Phase A commits can begin**, the following audits must complete:

### S0.1 — Supersession verification (3 of 13 complete)

**Verified ✓** (mechanic-text confirmed in canon):
- P8 — `faction_layer §3.5` CB expiration rule
- R4 — `worldbuilding §6.2` Motion of No Confidence concurrence
- H3 — `victory §3.6a` Post-Coup Ministry freeze

**Remaining `[AUDIT-FLAG]`** (canon read required to verify):
- P6 — `settlement_layer §3.3` Contested management
- R2′ — `social_contest §7.1` Excommunication Tribunal outcomes
- R3 — `solmund §12` Seam Text mechanic
- F1 — `worldbuilding §7.2` Altonian Cultural Imperialism activation
- F2 — `march_layer §6.3` + `valoria_political_hierarchy §1.2` Schoenland passage
- F4 — `insurgency_pipeline §5.2` Promotion branching
- I1 — `peninsular_strain §6.1` Effective hegemony
- P10 — `treaty_expiration §1.1` Treaty continuation (extension)
- P11 — `mass_battle §E` Battle Consequences (extension)
- F3 — `mass_battle §A.14b` Campaign Supply (extension)

### S0.2 — Compounding case enumeration (NOT EXECUTED)

High-risk pairs requiring canon-cross-check:

| Pair | Shared state | Risk |
|---|---|---|
| P1 + F3 | Wealth/Disposition on settlements under stress | Compounded cost during border crisis |
| P11 + H1′ | Cascade Fidelity inputs | Compound on battle loss |
| H1′ + H2 + H3 | Fire during faction transitions | Three propagation systems on one event |
| R2′ + H2 + H3 | Inner Circle Ministry-running NPC excommunication | Triple compounding |
| PR1 + PR3 + PR4′ | Fire on Repulsion | Event-set timing |
| F1 + F4 + F3 | Cultural Orientation + Border state | Cascading foreign pressure |
| CLC + H1′ | CLC feeds H1′ input | Verify additive vs multiplicative |
| I3 + PR4′ | Generational threshold | PR4′ modifies I3 parameter |
| P8 + PR2 | CB decay rules | PR2 carve-out from P8 |

### S0.3 — Operational definition audit (NOT EXECUTED)

Verify each numerical value has trigger / measurement / units explicit:
- Court Maintenance Wealth −2/arc (which Accounting?)
- H1′ thresholds X/Y/Z (measurement procedure?)
- 75% legitimating value (PT1) — which specific effects degraded?
- 30% Conviction shift probability (PT2) — measured how?

### S0.4 — Selection principle audit (NOT EXECUTED)

State explicit selection principle for proposals with option lists:
- R4 concession types
- PR3 reform list (✓ has principle)
- P9 League terms
- I1 Charter advancement paths
- F4 suppression tiers

### S0.5 — NRES audits required

**Three proposals are UN-NRES-AUDITED**; require four-interrogation NRES (duplication / compounding / operational definition / principled selection):
- PT1 Puppet Title Mechanic
- PT2 Generational Acculturation via Resident Heirs
- Crown Legitimacy Contestation Track

---

## §5 Canonical canon references

The supersession map and composition graph reference the following canon documents. Bottom-up audit work requires reading these.

| Canon document | Path |
|---|---|
| canon constraints (GD-1/2/3) | `canon/02_canon_constraints.md` |
| philosophical foundations | `canon/00_philosophical_foundations.md` |
| canonical timeline | `canon/03_canonical_timeline.md` |
| articulation layer | `designs/articulation/articulation_layer_v30.md` |
| faction systems overview | `designs/factions/faction_systems_overview_v30.md` |
| baralta crown claim | `designs/provincial/baralta_crown_claim_v30.md` |
| CI political | `designs/provincial/ci_political_v30.md` |
| faction behavior | `designs/provincial/faction_behavior_v30.md` |
| faction layer | `designs/provincial/faction_layer_v30.md` |
| faction politics | `designs/provincial/faction_politics_v30.md` |
| faction succession split | `designs/provincial/faction_succession_split_v30.md` |
| franchise | `designs/provincial/franchise_v30.md` |
| mass battle | `designs/provincial/mass_battle_v30.md` |
| military layer | `designs/provincial/military_layer_v30.md` |
| parliamentary transfer | `designs/provincial/parliamentary_transfer_v30.md` |
| peninsular strain | `designs/provincial/peninsular_strain_v30.md` |
| treaty expiration | `designs/provincial/treaty_expiration_v30.md` |
| varfell path B | `designs/provincial/varfell_path_b_v30.md` |
| victory | `designs/provincial/victory_v30.md` |
| conviction track | `designs/scene/conviction_track_v30.md` |
| social contest | `designs/scene/social_contest_v30.md` |
| march layer | `designs/territory/march_layer_v30.md` |
| settlement layer | `designs/territory/settlement_layer_v30.md` |
| territory temperaments | `designs/territory/territory_temperaments_v30.md` |
| calamity radiation | `designs/world/calamity_radiation_v30.md` |
| geography | `designs/world/geography_v30.md` |
| insurgency pipeline | `designs/world/insurgency_pipeline_v30.md` |
| southernmost | `designs/world/southernmost_v30.md` |
| worldbuilding | `designs/world/worldbuilding_v30.md` |

---

# PHASE A — Pure additions, no canon conflict (lowest risk)

Commit first. Symmetric primitives with asymmetric effects.

## P1 — Garrison Disposition Cost

**Phase:** A · **Status:** COMMIT · **Layer:** 1 · **`[AUDIT-FLAG]`** mechanism per V3 spec; supersession N/A (pure addition)

**Modifies:** `settlement_layer §4.5` Local Actor Disposition driver table (extension, not replacement).

**Add row:** *"Settlement has occupying-faction professional garrison (≥1 professional unit, occupying faction differs from settlement's `pre_conquest_faction_id`): −1 Disposition per Local Actor per season, cap −3 from this source."*

**Recovery.** Disposition recovers +1/season once garrison removed AND new Local Actor scenes occur in the settlement. Recovery cap +1/season; full reset from −3 requires ~3 seasons of post-withdrawal fieldwork investment.

**Calibration.** [CALIBRATION: -1/season decay, -3 cap; +1/season active recovery] — starting values; tune at sim Stage 10.

**Composition.**
- P2 Pre-Conquest Identity Track — provides the `pre_conquest_faction_id` field this rule reads (P2's field-definition must ship with P1 in Phase A)
- I3 Generational Loyalty Drift — long-term replaces Local Actors but Disposition cost continues
- F3 Border Burden — compounds with this during IP ≥ 60 in border settlements

**Historical anchor.** Spanish Fury at Antwerp 1576 — unpaid garrisons sacking populations produced Pacification of Ghent; Dutch Revolt sustained by garrison-resentment dynamics.

**NRES.** N: closes settlement-scale holding-cost surface; R: creates Disposition rehabilitation activity; S: composes cleanly; E: one row in one table.

**Test conditions.**
1. Faction X conquers settlement S held by faction Y; garrison from X stationed. Local Actor Disposition with X decays −1/season to floor −3, then stabilizes.
2. Garrison withdrawn. Active scenes occur. Disposition recovers +1/season to baseline.
3. Garrison withdrawn but no scenes. Disposition does NOT recover passively.

---

## P7 — Province Fracturing Trigger Specification

**Phase:** A · **Status:** COMMIT · **Layer:** 3 · **`[AUDIT-FLAG]`** closes open item in `valoria_political_hierarchy §5`

**Modifies:** `valoria_political_hierarchy §2.3` (closes the §5 Open Items spec gap).

**Mechanic.** A province *fractures* into named sub-provinces when, at two consecutive Accountings:
- (a) At least one settlement's faction-controller differs from province's Seat-settlement controller, AND
- (b) Differing settlements' aggregate Order ≥ 2 (dissident grouping is governing successfully)

A fractured province *reunifies* when, at two consecutive Accountings:
- (c) All settlements have the same faction-controller, OR
- (d) Dissident settlements' aggregate Order drops to ≤ 1

**Naming convention.** Sub-provinces named by direction or by dominant settlement (e.g., "Northern Hafenmark" / "Southern Hafenmark"). UI presents each sub-province as distinct map region.

**Cascade effects.** Province Accord recalculates per sub-province. Each sub-province carries its own Franchise, Charter (per I1), Cultural Orientation (per F1), Witness Tradition distribution (per R1).

**Calibration.** [CALIBRATION: Order ≥ 2 threshold; 2-Accounting persistence] — starting values; tune at sim Stage 10.

**Historical anchor.** Westphalia 1648 (*cuius regio* operating at territorial granularity); Hussite Bohemia's 130-year confessional partition.

**Test conditions.**
1. Crown holds province with Seat at T2; Hafenmark holds 2 settlements within province. Hafenmark settlements maintain Order ≥ 2 for two consecutive Accountings. Province fractures.
2. Fractured province: dissident sub-province Order drops to 1 for two consecutive Accountings. Province reunifies.

---

## P10 — Coronation-Required Treaty Renewal

**Phase:** A · **Status:** COMMIT-REVISED · **Layer:** 2 · **`[AUDIT-FLAG]`** `treaty_expiration §1.1` extension not verified against canon

**Modifies:** `treaty_expiration_v30 §1.1` — extension adding succession-event trigger.

**Mechanic.** All Crown Treaties involving a faction undergo a **Renewal Check** when that faction undergoes leader change:
- Coronation (formal Succession Scene per `victory_v30 §3.6a` or `faction_succession_split §2`)
- Löwenritter Coup activation
- RM Stage 4 promotion of a player faction
- Magnate Crisis succession-contest resolution (per H1′)
- Any Faction Succession Contest with clear-winner or narrow-winner outcome

Roll: standard treaty-continuation check (90% continuation rate per canonical `treaty_expiration §1.1`). **The roll defaults to continuation;** failure produces lapse.

**Framing note.** Historical pattern: oaths were renewed at succession, with renewal typically succeeding. Mechanical outcome same probability as a lapse-check (90%) but narrative posture correct.

**Re-binding on failure.** Lapsed treaties may be re-bound via Senator Outward action per `treaty_expiration §2`.

**Composition.** H1′ Magnate Crisis succession-contest resolution triggers Renewal Check; F4 Foreign-Backed Insurgency promotion of parent faction.

**Historical anchor.** Roman *foedera* renewal at coronation; Henrician Articles 1573 as constitutional treaty subscription required at each Polish royal election.

---

## P11 — Battle Outcome → Standing Cascade

**Phase:** A · **Status:** COMMIT · **Layer:** 2 · **`[AUDIT-FLAG]`** `mass_battle §E` extension not verified against canon

**Modifies:** `mass_battle §E Battle Consequences` and `faction_systems_overview §2.3` Standing matrix.

**Mechanic.** When Battle resolves between Factions A and B:

| Outcome | Standing changes |
|---|---|
| A defeats B (Success) | A's Standing-with-B drops one step toward Hostile. Any faction X with prior Standing-with-A ≥ Cordial: X's Standing-with-A drops one step |
| A defeats B (Overwhelming) | A's Standing-with-B drops to Hostile. Any faction X whose Mission `contradicted_da_categories` intersect with A's recent action history: X's Standing-with-A drops one step |
| A defeats B with named-officer NPC death on B side | Additional: B's Standing-with-A drops one step beyond standard |

**Mission contradiction check** uses schema in `faction_behavior §3.1` (aligned/contradicted DA categories). No new schema required.

**Composition.** H1′ Magnate Crisis (battle loss feeds Cascade Fidelity input); H2 Standing Cascade on Inner Circle Removal (composes when officer NPCs die).

**Historical anchor.** Italic League resident-ambassador substrate — peer factions had information channels and adjusted alignment based on demonstrated military events.

---

## R1 — Local Actor Witness Tradition

**Phase:** A · **Status:** COMMIT · **Layer:** 1+2 · pure addition; no supersession

**Modifies:** `settlement_layer §4.5` Local Actor profile.

**Add field:** each Local Actor has hidden `witness_tradition` with three values:
- `miracle` — Orthodox-aligned; reads Solmund through Church's Miracle-Witness framework
- `practitioner_curious` — open to heterodox readings; has not encountered TS ≥ 30 contact
- `practitioner_aware` — has Thread experience or TS ≥ 30 content; reads the seam beneath orthodox surface

**Starting distribution at game start (45 AG):**

| Territory PT band | `miracle` | `practitioner_curious` | `practitioner_aware` |
|---|---|---|---|
| PT 4–5 | 90% | 8% | 2% |
| PT 2–3 | 70% | 25% | 5% |
| PT 0–1 | 40% | 40% | 20% |

**Geographic override:** Calamity-proximate territories (T6 Stillhelm, T13 Oastad, T15 Askeheim) use 30% / 40% / 30% regardless of PT.

**Effects.**
- `practitioner_aware` Local Actors halve PT generation from Church infrastructure in their settlement
- RM Community Organizing rolls in settlement with ≥1 `practitioner_aware` Local Actor: +1D
- Heresy Investigation Tier 2 (per R2′) targets only `practitioner_aware` Local Actors

**State transition.**
- `practitioner_curious` → `practitioner_aware` after one scene with TS ≥ 30 character involving Solmund/threadwork content (one-way; comprehension does not reverse)
- `miracle` → `practitioner_curious` requires R3 Seam-Text Network mechanic (province-scale)

**Calibration.** [CALIBRATION: distribution percentages by PT band; geographic override list] — starting values; tune at sim Stage 10.

**Historical anchor.** Cathar Perfecti pattern — outwardly conforming populations holding inward heterodoxy until declared. Persistence requires individuals at the substrate.

---

## I3 — Generational Loyalty Drift

**Phase:** A · **Status:** COMMIT · **Layer:** 1 · pure addition

**Modifies:** `settlement_layer §4.5` Local Actor lifecycle.

**Add field:** each Local Actor carries hidden `generation_origin` timestamp. At game start, all Local Actors share `generation_origin = season 0`.

**Generational replacement.** At each arc boundary, Local Actors with `generation_origin > NATURALIZATION_THRESHOLD seasons ago` are replaced:
- 60% inherit prior-faction-allegiance from settlement's `pre_conquest_faction_id` (per P2)
- 40% inherit current-controller-allegiance
- Replacement Local Actor starts with Disposition +1 with inherited-allegiance faction

**Cultural Reconciliation action.** New Domain Action available to controlling faction:
- Pool: Influence + (Standing with relevant cultural-faction NPCs)
- Ob: 4 − (seasons since conquest ÷ 10), minimum 1
- Success: one Local Actor's `generation_origin` advances to current season
- Overwhelming: two Local Actors advance + settlement Disposition +1
- Failure: settlement Disposition −1

**Cap.** Cultural Reconciliation may target each settlement once per arc.

**Calibration.** [CALIBRATION: NATURALIZATION_THRESHOLD = 24 seasons; 60/40 inheritance ratio] — doc-validated; compound drift across 3 cycles (72 seasons) produces ~22% pre-conquest retention, consistent with two-three generation identity formation timing per `institutional_persistence_pre1600.md` l. 167.

**Composition.** P2 Pre-Conquest Identity Track; F1 Cultural Orientation (Reconciliation reduces it); PR4′ Postwar acceleration.

**Historical anchor.** Welsh-into-Tudor-English absorption over 2 generations; Reconquista *convivencia*.

---

## F1 — Altonian Cultural Penetration as Substrate Track

**Phase:** A · **Status:** COMMIT · **Layer:** 1 · **`[AUDIT-FLAG]`** `worldbuilding §7.2` activation not verified against canon

**Modifies:** `settlement_layer §1.3` Settlement Stats; supersedes `worldbuilding §7.2` Altonian Cultural Imperialism setting-note framing.

**Add stat:** each settlement carries hidden `cultural_orientation` 0–5.

**Starting values:**

| Region | Starting cultural_orientation |
|---|---|
| Schoenland-adjacent (T1 Valorsplatz coastal, T16 Schoenland) | 3 |
| Northern passage-adjacent (T3 Lowenskyst, T10 Spartfell) | 2 |
| Crown core (T2 Kronmark, T5 Feldmark, T14 Ehrenfeld) | 2 |
| Hafenmark commercial (T8 Gransol, T17 Halvarshelm) | 1 |
| Varfell (all) | 0 |
| All other settlements | 1 |

**Advancement (+1 per arc, cap 5):**
- Active Schoenland trade route open AND used by Crown
- Torben Loyalty ≤ 3

**Reduction (−1 per arc):**
- Successful Cultural Reconciliation (per I3)
- Varfell-led action explicitly opposing Altonian influence (requires canon authoring of action spec)

**Effects.**
- `cultural_orientation` ≥ 3: Altonian Alignment NPC events fire at +1D
- `cultural_orientation` ≥ 4: at IP=100 Phase 1 invasion, settlement immediately contested
- `cultural_orientation` = 0: at IP=100 invasion, settlement contributes +2 to Underground Network if RM Presence exists; settlement Order +1 reflexively

**Composition.** F3 Border Burden (Loyalty Check failure advances `cultural_orientation`); F4 Foreign-Backed Insurgency (emergence condition); PR1 Repulsion Settlement Dividend (reduces border `cultural_orientation`).

**Historical anchor.** Habsburg *kultur* penetration of Bohemia preceding political conquest.

---

# PHASE B — Additions with calibration risk

## P2 — Pre-Conquest Identity Track

**Phase:** B · **Status:** COMMIT-REVISED · **Layer:** 1 · complements `peninsular_strain §2.4`

**Modifies:** `settlement_layer §1.3`.

**Add field:** hidden `pre_conquest_faction_id`. Set at game start to current controlling faction.

**Note for Phase A integration:** the *field definition* (initialization at game start, no transition rules) must ship with Phase A so P1 can fire. Full *transition rules* below are Phase B.

**State transitions** (Phase B):
- (a) Current faction holds settlement for NATURALIZATION_THRESHOLD seasons with Order ≥ 3 AND aggregate Local Actor Disposition ≥ +1, OR
- (b) Parliamentary Transfer (Consensual mode), OR
- (c) Crown Treaty cession, OR
- (d) Dynastic Proclamation Overwhelming, OR
- (e) Cultural Reconciliation (per I3) reaches threshold (8 successful Reconciliation actions in settlement)

`pre_conquest_faction_id` does **NOT** change on military conquest, even Overwhelming.

**Effects.**
- Used by I3 for inheritance distribution
- RM Stage 2 Latent emergence *suppressed* where `pre_conquest_faction_id` matches current controller
- RM Stage 2 Latent emergence *enhanced* (Ob −1 on Grassroots Organising) where it differs

**Calibration.** [CALIBRATION: NATURALIZATION_THRESHOLD = 24 seasons (matches I3); 8 successful Reconciliation actions] — starting values.

**Historical anchor.** Bohemian Hussite identity persistence (130 years post-Compactata); Languedoc cultural distinctiveness.

---

## P3 — Local Actor Conviction as Recruitment Vector

**Phase:** B · **Status:** COMMIT-REVISED · **Layer:** 2 · activates unused canon primitive

**Modifies:** `settlement_layer §4.5` Local Actor scene mechanics; integrates with `faction_behavior §3.1` Mission schema.

**Mechanic.** When faction-X representative engages a Local Actor in social contest:
- Check Local Actor's Conviction against faction X's current Mission
- If matches `mission.aligned_da_categories`: faction X gains +1D on social contest
- If matches `mission.contradicted_da_categories`: faction X takes +1 Ob

**Schema integration.** Uses existing Mission tags from `faction_behavior §3.1`. If alignment-relevant Conviction categories not yet exposed in Mission schema, follow-up authoring required.

**Effects propagate.** Successful Mission-aligned social contests increase Cascade Fidelity per `faction_behavior §3.2.6` (canonical).

**Historical anchor.** Polish-Lithuanian *szlachta* class coherence — Privilege of Mielnik (1501) held because substrate class had internal political-Conviction coherence.

---

## P4 — Wing-Holder Faction Affiliation as Standing Bridge

**Phase:** B · **Status:** COMMIT-REVISED · **Layer:** 2 · extends `settlement_layer §1.4.4`

**Modifies:** `settlement_layer §1.4.4` Cross-Faction Wing Allocation.

**Mechanic.** When Wing slot at Seat or Cathedral settlement is occupied by faction-Y officer at controlling faction X's permission:
- Faction Y gains Standing-with-X +1 (pairwise; faction-wide unaffected)
- Faction Y scenes initiated *at that specific settlement* gain +1D while Wing occupied
- Wing cession is treaty concession (cost per existing §1.4.4)

**Caps.** One cross-faction Wing per Seat per faction-pair. The +1D applies only to Y-initiated scenes at the specific settlement.

**Withdrawal.** Controlling faction X may revoke as Domain Action (Influence vs Y's Influence ÷ 2). Cost on revocation: Standing-with-Y drops one step; if during active treaty, Y gains "Treaty Violation" CB.

**Composition.** R4 Confessor Concurrence (Wing is one concession option); PT2 Generational Acculturation (operates at heir scale; P4 at officer scale).

**Historical anchor.** Resident ambassador system; hostage-and-ward court fostering.

---

## F3 — Border Settlement Asymmetric Vulnerability

**Phase:** B · **Status:** COMMIT-REVISED · **Layer:** 1 · **`[AUDIT-FLAG]`** `mass_battle §A.14b` extension not verified

**Modifies:** `mass_battle §A.14b` Campaign Supply; adds border-specific variant.

**Mechanic — Border Burden** applies to march-layer-adjacent-to-Altonian-invasion-route settlements (T3 Lowenskyst, T10 Spartfell, T1 Valorsplatz coastal, T17 Halvarshelm).

**Pre-crisis state (IP < 60).** Border Burden does not fire.

**Crisis bands:**

| IP threshold | Border Burden per border settlement at Defense ≥ 3 |
|---|---|
| IP ≥ 60 | Wealth −1 per arc |
| IP ≥ 80 | Wealth −2 per arc; one Local Actor per border settlement makes Loyalty Check (Disposition pool vs Ob 3); failure = `cultural_orientation` (F1) advances +1 |
| IP ≥ 100 | Wealth −3 per arc; Loyalty Check Ob 4 |

**Repulsion bonus.** When Altonian Repulsion fires per `victory §5.2`: each border settlement Border Burden = 0 for 8 seasons; every Local Actor Disposition with successful defender +1.

**No-stacking rule.** Border Burden NOT additional to normal Campaign Supply. The two cost surfaces apply in different conditions.

**Historical anchor.** Habsburg Military Frontier vs Ottoman pressure; Roman *limes*.

---

# PHASE C — Modifying existing canon, medium risk

## P6 — Governor Conflict as Parliamentary Vote Trigger

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2 · **`[AUDIT-FLAG]`** `settlement_layer §3.3` supersession not verified

**Modifies:** `settlement_layer §3.3` Contested management; adds motion type to `faction_layer §5.4`.

**Mechanic.** When Settlement Governor's faction differs from Provincial Authority's faction AND governor refuses an Order:
- **Governor's faction Mandate < 3:** existing canon route (social contest §7 asymmetric)
- **Governor's faction Mandate ≥ 3 AND Order alters settlement-scale stats** (Prosperity, Defense, Order, infrastructure): escalates to **Governor Confirmation Hearing** parliamentary motion

**Governor Confirmation Hearing:**
- Proposer: Provincial Authority faction
- Pool: vote by all Mandate-bearing factions per §5.3
- Threshold: Majority
- Outcomes:
  - Upholds Provincial Authority: governor complies; governor faction Standing-with-Provincial-Authority drops one step
  - Upholds governor: Order rescinded; Provincial Authority Mandate −1; governor Standing-with-Provincial-Authority +1
  - Tie: Order suspended 1 season; re-resolves at next Accounting

Existing social_contest §7 route remains for sub-Mandate-3 disputes.

**Composition.** I1 Charter Track (Charter ≥ 2 duchies protected); H3 Ministerial Continuity (compound during Ministry transition).

**Historical anchor.** Investiture Controversy (Concordat of Worms 1122); Habsburg cross-jurisdictional bishop-governor conflicts.

---

## P8 — Casus Belli Decay via Reconciliation

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2 · supersession verified ✓

**Modifies:** `faction_layer §3.5` CB expiration rule.

**Supersedes:** "CB is consumed upon first use OR after 1 season of non-use (expires)" — the time-based decay path. The "consumed upon first use" path is preserved; the "1 season of non-use" decay path is replaced.

**New rule:** *a Casus Belli persists in the CB ledger until either consumed in action OR the displaced/wronged faction's Local Actors in the settlements that generated the CB reach aggregate Disposition ≥ +1 with the CB-holding faction for 2 consecutive Accountings.*

**Canon-internal inconsistency to resolve:** `faction_layer §3.5` lists 4 CB sources (treaty breach / Outlawry vote / Hafenmark Diplomatic Token override / Church Excommunication). `parliamentary_transfer §3` lists 8 sources (constitutional restoration / adjacent instability / Einhir Revival Partial / Parliamentary Transfer Partial / Military Conquest / Treaty-violation / Excommunication-related / Conviction Scar accumulation).

**Resolution proposal:** treat `parliamentary_transfer §3` 8-source list as canonical comprehensive list. `faction_layer §3.5` 4-source list should be updated to match in a separate canon-cleanup task. P8 uses 8-source list with `[ASSUMPTION: parliamentary_transfer §3 is canonical; faction_layer §3.5 needs update]`.

**Effect:** war's grievance-state persists until *active settlement-scale reconciliation*. Last-territory protection in `parliamentary_transfer §1.3` remains; P8 changes only decay, not use-eligibility.

**Composition.** I3 Cultural Reconciliation; PR2 Wartime Collaboration CB 16-season carve-out (Phase D).

**Historical anchor.** *Wergild* pattern; Augsburg confessional grievance settled at territorial layer.

---

## R2′ — Martyrdom Marker on Tribunal Conviction

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 1+2 · **`[AUDIT-FLAG]`** `social_contest §7.1` supersession not verified

**Modifies:** `social_contest §7.1` Excommunication Tribunal outcomes; integrates with R1.

**Does NOT restructure Heresy Investigation Lifecycle (§7.3).** Existing 4–6 season lifecycle preserved.

**Martyrdom Marker.** When Excommunication Tribunal produces Conviction verdict against Local Actor or low-Standing NPC (Standing ≤ 3) with `witness_tradition: practitioner_aware`:
- Convicted person removed from settlement
- Settlement Order −1
- Settlement gains Martyrdom Marker for 4 seasons:
  - Disposition modifier −1 against Church for all Local Actors in settlement
  - RM Community Organizing rolls: +1D
  - `witness_tradition` transitions: 1 `miracle` → `practitioner_curious` per arc marker active

**Markers stack** (multiple convictions); effects don't compound beyond listed values, but duration extends.

**Suppression-Eventually-Succeeds branch.** If Church successfully prosecutes 3+ Martyrdom-Marker-eligible cases in same province within 8 seasons, the *next* Martyrdom Marker has inverted effects for its 4-season duration:
- RM Community Organizing rolls: +1 Ob (not +1D)
- Witness Tradition propagation rate halved
- Disposition penalty against Church reduced to −0.5 (rounded)

Captures Albigensian Crusade success / *conversos* eventual assimilation pattern.

**Articulation tier.** Tier 2 propagation event (follow-up authoring required — see §6 follow-up item 1).

**Composition.** R1 Witness Tradition; R3 Practitioner Cell; H2 Standing Cascade (if convicted person Inner Circle).

**Historical anchor.** Jan Hus execution at Constance 1415 triggering Hussite Wars. Inverse: Albigensian Crusade success eliminating Cathars; Spanish *conversos* assimilation under sustained Inquisition.

---

## R3 — Seam-Text Practitioner Cell (province-scale)

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 1 · **`[AUDIT-FLAG]`** `solmund §12` supersession not verified

**Modifies:** `solmund_v30 §12` Seam Text discoverable POI; adds province-scale emergent state.

**Mechanic.** When province has **all three** of:
- ≥ 3 settlements within province each containing at least one `practitioner_aware` Local Actor (per R1)
- ≥ 1 active Seam Text discovered in any settlement within province
- Average province PT ≤ 2

Province gains **Practitioner Cell** status.

**Effects of Practitioner Cell.**
- Inquisitor surveillance in any Cell-province settlement: +1 Ob to RM Community Organizing
- RM Community Organizing in Cell-province: +1D
- Heresy Investigation against `practitioner_aware` Local Actors in Cell-province requires Cardinal-grade approval
- Province-scale propagation: TS ≥ 30 character may, once per season, attempt Seam Text social contest with any `practitioner_curious` Local Actor in province (Ob 3 + (settlement PT − 2)); Success shifts target to `practitioner_aware`

**Loss of Cell status.** Cell dissolves when any formation condition fails for 2 consecutive Accountings.

**Cell Resilience compatibility.** Integrates with existing `settlement_layer §3.3` RM Cell Resilience.

**Historical anchor.** Lollard reading communities; early Reformation circles in Wittenberg, Geneva.

---

## R4 — Confessor Concurrence States (REVISED for narrowed scope)

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2 · supersession verified ✓; scope narrowed from V3

**Modifies:** `worldbuilding §6.2` Motion of No Confidence (Confessor concurrence step).

**Does NOT modify:** `faction_layer §5.3` Sacred Veto. Sacred Veto retains canonical cooldown-gated unilateral-block structure. R4 and Sacred Veto operate independently.

**Mechanic.** Motion of No Confidence step 2 ("Holy See concurrence") is replaced by three-state framework:

| State | Condition | Effect |
|---|---|---|
| **Concurrent** | CI ≥ 30 AND Church Stability ≥ 3 | Confessor concurs. Motion proceeds per canonical §6.2 deposal rules |
| **Conditional** | CI < 30 OR Church Stability < 3 (not both Withheld conditions) | Confessor demands concession. Proposing faction offers ONE of: (a) Wing residency at Seat (per P4); (b) Subsidy ≥ Wealth 2 to Church; (c) Transfer of settlement at PT ≥ 3 to Church control. Concession performed BEFORE vote. Church Mandate −1 per concession-gated concurrence |
| **Withheld** | CI < 15 OR Church Stability < 2 OR active heresy charge against proposer-faction | Confessor refuses regardless of concession. Motion fails. **Canonical effect: CI +3, TT +2** (per `worldbuilding §6.2`). Proposing faction Mandate −1 |

**Interaction with Sacred Veto (preserved from canon):** Sacred Veto operates independently. Confessor may invoke Sacred Veto against 6 eligible motion types (Censure / Embargo / Outlawry / Recognition Challenge / Succession Endorsement / Treaty Ratification) per §5.3 cooldown (once per 4 seasons). Sacred Veto self-interested use costs additional Mandate −1 per canon.

**Composition.** P4 Wing Residency (concession option); PR3 Reform Window (concession cost reductions).

**Historical anchor.** Concordat of Worms (1122); Henry VIII vs Rome — break-with-Rome resulted from sustained negotiation failure on papal dispensation power.

**Test conditions.**
1. CI = 35, Church Stability = 4: Motion step 2 Concurrent. Confessor concurs without concession.
2. CI = 25, Church Stability = 4: Conditional. Proposer offers one of three concessions; Confessor concurs.
3. CI = 10: Withheld. Motion fails; CI +3, TT +2.
4. Concurrent state: Sacred Veto still available against eligible motion types per §5.3 cooldown.

---

## F2 — Schoenland Mediation Stance (with Diplomatic Conference)

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2+3 · **`[AUDIT-FLAG]`** `march_layer §6.3` + `valoria_political_hierarchy §1.2` supersession not verified

**Modifies:** `valoria_political_hierarchy §1.2` Schoenland framing; supersedes binary passage rule in `march_layer §6.3`.

**Mediation Stance (0–5 track):**

| Stance | Schoenland posture | Passage rules |
|---|---|---|
| 0 | Hostile to Valoria; favors Altonian invasion | IP +1/season passive (Schoenland shares intelligence with Altonia) |
| 1 | Cool toward Valoria | Passage to Altonia at IP ≥ 60; IP +0.5/season passive |
| 2 | Standard neutral (game start) | Existing march §6.3 binary: passage to Altonia at IP ≥ 75 |
| 3 | Warm toward Valoria | Passage to Altonia closed; passage to Valoria open (+1D diplomatic/trade) |
| 4 | Active Valoria-aligned mediator | Stance-3 effects + Schoenland eligible to host Diplomatic Conference |
| 5 | Formal alliance | Stance-4 effects + Schoenland counts as treaty-bound for `peninsular_strain §6.1` effective hegemony |

**Advancement:** +1/arc per Fair Trade arc with Crown; +1/arc per Elske Loyalty ≥ 4; +1 per Elske Diplomatic Exchange Success; +1 per Elske Diplomatic Exchange Overwhelming.

**Reduction:** −1/arc during sanctions; −2 on Crown military operation against Schoenland; −1/arc if Standing-with-Schoenland drops below Cordial.

**Diplomatic Conference action** (Stance ≥ 4):
- Senator action available to any peninsula faction
- Cost: Wealth −2 + Senator action slot
- Effect: multi-party social contest at Schoenland
- All peninsula factions invited; refusal costs Standing −1 with attending factions + Schoenland
- Highest-success faction sets Conference Resolution: binding treaty terms among subset / non-aggression pact / joint declaration on third party / Mandate-restoration (cost: Schoenland Mediation Stance −1)
- Conference fires once per arc maximum

**Composition.** F4 Foreign-Backed Insurgency Tier 2 suppression; PR3 Reform Window.

**Historical anchor.** Venice as Italic League diplomatic venue; Switzerland's medieval/modern role as diplomatic neutral.

---

## H1′ — Magnate Crisis as Triggered State

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2 · reuses existing primitives; no new aggregate state

**Modifies:** `faction_succession_split §2` Contest Mechanics — adds trigger condition, reuses existing contest path.

**Trigger.** Magnate Crisis fires when, at any Accounting, all three of:
- Faction Cascade Fidelity (per `faction_behavior §3.2.6`) below threshold X
- Faction Stability below threshold Y
- At least one named Inner Circle NPC has Conviction Scar count ≥ Z (per `npc_behavior §3.3`)

**No new aggregate stat introduced.** Trigger reuses three existing inputs.

**On Magnate Crisis trigger.** Faction Succession Contest fires:
- Incumbent leader: standard contest party
- Pretender Claimant: Inner Circle NPC with highest Scar count meeting threshold Z, IF their Disposition with leader ≤ −1
- If no Inner Circle NPC meets both conditions, trigger logs open vulnerability without escalating

**Contest resolution** per `faction_succession_split §2.3`:
- Clear winner (2+ net successes margin): faction unified under winner; loser takes Standing −2
- Narrow winner: faction splits per `faction_succession_split §2.4`
- **Fallback (audit addition):** if contest produces 0-1 net successes margin, escalate to parliamentary vote (Crown Council / Hafenmark Parliament / Varfell Jarl Assembly / Church Conclave — faction-appropriate body) rather than splitting

**During Magnate Crisis:**
- Faction may not initiate offensive military action
- Faction may not sign new treaties
- Faction may participate in parliament only on motions targeting the faction itself

**Calibration.** [CALIBRATION: thresholds X / Y / Z — UN-CALIBRATED; require sim Stage 10 measurement of Cascade Fidelity / Stability / Scar distributions during Phase A-B testing to set empirically].

**Composition.** P11 (battle losses feed Cascade Fidelity); F3 (Wealth drain feeds Stability); H2 (Inner Circle death feeds Scars); P10 (Magnate Crisis succession resolution triggers Renewal Check); H3 (Magnate Crisis transition triggers Continuity Check).

**Historical anchor.** Fronde 1648–1653; Late Han eunuch-vs-bureaucracy split; Spanish *grandes* withdrawal of confidence from Olivares 1643; English Wars of the Roses.

---

## H2 — Standing Cascade on Inner Circle Removal

**Phase:** C · **Status:** COMMIT-WITH-CALIBRATION-FLAG · **Layer:** 2

**Mechanic.** When named Inner Circle NPC (Standing 5–6 named NPC per `faction_politics §1.Nd`) is removed (death, exile, defection, Dismissed-with-Dishonor, Mass Battle officer-captured-and-unransomed):

- **Faction internal:** each remaining Inner Circle NPC makes Disposition Check (current Disposition with leader vs Ob 2). Failure: Disposition with leader −1. Overwhelming: Disposition +1.
- **Cross-faction Standing:** for each named cross-faction Disposition the removed NPC carried, the faction-pair Standing matrix shifts one step toward neutral
- **Conviction Scar input (per H1′):** Inner Circle removal counts as Scar-event for surviving Inner Circle NPCs

**Removal-cause modifiers:**

| Removal cause | Additional effect |
|---|---|
| Death in combat defending faction | Disposition Check at Ob 1 (cohort rallies more easily) |
| Death by assassination, Niflhel-attributed | Faction gains CB against Niflhel-associated factions |
| Defection to rival faction | Removed NPC's prior cross-faction Disposition effects transferred to rival |
| Exile or Dismissed-with-Dishonor by leader | Surviving Inner Circle Disposition with leader −1 |
| Heresy Tribunal Conviction with Martyrdom Marker (per R2′) | Inner Circle Disposition Check at Ob 3 |

**Calibration flag.** Sim Stage 10 must specifically test multi-propagation compounding on excommunication-class events (H2 + R2′ + potentially H3 firing on same NPC removal).

**Historical anchor.** Sir Thomas More execution 1535; Olivares dismissal 1643; Becket murder 1170.

---

## H3 — Ministerial Continuity vs Faction Authority

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 2 · supersession verified ✓; scope clarified

**Modifies:** Faction Ministry / Parliamentary Committee / Church Dicastery / Varfell Council behavior during faction-transition.

**Supersession (precise):**
- For **Löwenritter Coup case**: supersedes `victory §3.6a` 1-season Ministry freeze
- For **other faction transitions** (Magnate Crisis per H1′; Faction Succession Contest per faction_succession_split §2; Crown Interregnum without coup): extension, not supersession — canon does not specify Ministry behavior in these cases

**Mechanic — Continuity Check.** When a faction enters succession-transition state:

For each Ministry / Committee / Dicastery / Council the transitioning faction operates **AND** which has Readiness ≥ 1 at moment of transition (Varfell-specific gate per `faction_politics §7.4`):
- Continuity Check: Ministry's leadership NPC's Disposition with prior leader vs Ob (Ob 1 if canonical/formal; Ob 2 if standard; Ob 3 if coup / Magnate Crisis / Dismissed-with-Dishonor)
- **Overwhelming:** Ministry serves new authority at +1D for 1 season; Stability +1
- **Success:** Ministry serves new authority normally
- **Partial:** Ministry serves at +1 Ob on Ministry-action rolls for 1 season; Stability −1
- **Failure:** Ministry refuses new authority for 2 seasons; on Accounting 2, leadership NPC makes Conviction Check; failure shifts Ministry to independent state (operates per prior leader's Mission); success returns Ministry to service

**Varfell Council edge case.** Councils per canon convene on need (Readiness 0–3). If Readiness = 0 at moment of transition, no Continuity Check fires. If Council activates during friction period (Readiness rises to ≥ 1), Continuity Check fires at activation with same Ob.

**Ministry-type behaviors** (parameterized by ministry type):
- Treasury/economic: friction expressed as Wealth-extraction Ob +1
- Legal/administrative: friction expressed as scheduling delays
- Religious (Church Dicasteries): friction reduces CI passive generation by 1
- Military (Varfell Councils): friction prevents Mass Battle tactic-card refresh

**Resolution.** Friction clears after 4 seasons stable governance OR new authority may purge: replace leadership NPC at Standing −1 Disposition cost + Stability −2; effective Discipline reduced for 8 seasons.

**Single-Friction rule.** If H2-triggered Friction (NPC death without transition) and transition-triggered Friction would simultaneously apply, longest-duration single period applies (no stacking).

**Composition.** H1′ Magnate Crisis; H2 Standing Cascade; R4 Confessor Concurrence (Church Withheld + Church Dicastery Friction = compound stress).

**Historical anchor.** Roman provincial administration under Year of Four Emperors (69 CE); English chancery under Stephen vs Matilda; Tudor Privy Council under transitions.

---

## PR1 — Repulsion Settlement Dividend

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 1+2+3

**Modifies:** Adds postwar political-settlement event to `victory §5.2`. **Does NOT modify** `treaty_expiration §1.1` 90% canonical rate.

**Mechanic.** When Altonian Repulsion fires (any of four canonical paths in `victory §5.2`), **Repulsion Settlement** event opens at following Accounting. One-time event per occupation cycle.

**Universal effects:**
- All factions with military participation: Mandate +1, Stability +1, Treasury +200
- All factions without military participation: Treasury −100; Standing-with-participating-faction drops one step
- Border settlement effects per F3 Repulsion bonus (referenced, not duplicated)
- Settlements with `practitioner_aware` Local Actors that participated in Underground Network: Disposition with successful defender +1

**Path-specific effects:**

| Repulsion Path | Specific Effect |
|---|---|
| **Military repulsion** (Mass Battle Overwhelming ×2) | Winning faction(s) gain "Defender of the Peninsula" tag: +1D on social contests where military legitimacy at stake, for 12 seasons. Crown specifically (if defender): Cohort Cascade Fidelity input +1 (composes with H1′) for 8 seasons |
| **Diplomatic repulsion** (Elske/Schoenland) | Schoenland Mediation Stance (F2) +1 immediately; Crown Standing-with-Schoenland +1; Schoenland Treaty available; Elske formally shifts to "willing resident" |
| **Resistance repulsion** (Underground Network) | Underground Network factions: Mandate +1, Stability +1, Wealth +2; RM-variant Network factions promote to Stage 4 per GD-3 §5.2; accommodationist factions (signed informal treaty with Altonian forces during Occupation): Mandate −2, Stability −2, Standing drops two steps; collaborator-territory Local Actor Disposition with collaborator faction drops to −2 |
| **Permanent defeat** | All contributing-path effects at half magnitude + "Peninsula Vindicated" marker — all peninsula factions Mandate +1 for one Accounting |

**Articulation tier.** Tier 2 (follow-up authoring required).

**Composition.** F3 Border Burden; F1 Cultural Orientation; H1′ Magnate Crisis; PR2 Settling-of-Accounts; PR3 Reform Window.

**Historical anchor.** Tours 732; Lepanto 1571; Vienna 1683; Battle of Britain 1940.

---

## PR3 — Repulsion Reform Window

**Phase:** C · **Status:** COMMIT-REVISED · **Layer:** 3

**Modifies:** Time-bounded institutional reform availability following Repulsion.

**Mechanic.** For 8 seasons following Repulsion event, **Reform Window** is open.

**Selection principle:** Window-eligible reforms are those that *establish or formalize new institutional structure* OR *reorganize existing structure*. Reforms that *reverse* prior decisions are NOT Window-eligible.

**Window-eligible reforms:**

| Reform | Normal access | Reform Window access |
|---|---|---|
| Parliamentary Recognition (I1 Charter advancement) | Mandate ≥ 4 + Majority | Mandate ≥ 3 + Majority |
| Confessor Concurrence shift to Concurrent (R4) | Standard concessions | Concession Wealth requirement halved; Wing residency requirement remains |
| Cultural Reconciliation (I3) | Standard Ob | Ob −1 in territories where Underground Network operated |
| Province Fracturing reunification (P7) | 2-Accounting threshold | 1-Accounting threshold |
| League formation (P9) | Standard | Influence contribution waived for first 4 seasons |
| Hafenmark Constitutional Amendment | Supermajority + Majority cohort consent | Majority + Cohort Cascade Fidelity ≥ neutral |
| New Ministry/Committee/Dicastery/Council | Standard authorization + Wealth −5 | Streamlined + Wealth −2 |

**Cap.** Each faction may pursue at most 2 reforms during single Reform Window.

**Composition.** I1 Charter Track; R4 Confessor Concurrence; P9 Leagues; PR1 Settlement Dividend (opens Window).

**Historical anchor.** Bismarckian reforms after Prussia's defeat of France 1871; British post-1945 reforms; Russian Tsarist reforms 1856; Habsburg post-1683 Hungarian settlement.

---

## PT2 — Generational Acculturation via Resident Heirs

**Phase:** C · **Status:** UN-NRES-AUDITED · **Layer:** 2

**Requires four-interrogation NRES audit before sim Stage 10.**

**Modifies:** Adds new diplomatic surface; complements P4 Wing Residency at heir scale.

**Mechanic.** Non-Crown duchy may agree, by Crown Treaty, to place designated heir at Crown court for 4-8 seasons. Heir functions as:
- High-Standing resident NPC at Crown court
- Personal-scale character for player scenes
- Subject to Crown court's cultural-acculturation effects

**Crown court acculturation (after 8+ seasons residency):**
- Heir's Disposition with Crown Inner Circle NPCs: +1 baseline shift
- Heir's Conviction may shift toward Crown's framework (Order) at 30% per arc probability
- Heir's `cultural_orientation` (extends F1 to named NPCs) gains modifier toward Crown-court value

**Effects on home duchy (per arc heir resident):**
- Standing-with-Crown +1
- Military operations against Crown: +1 Ob (implicit hostage)
- I1 Charter Track advancement via Parliamentary Recognition: −1 Ob

**Effects on Crown:**
- Diplomatic surface to convert heir over time
- Recall costs: Crown-with-home-duchy Standing drops one step; heir's accumulated acculturation persists on individual

**Calibration.** [CALIBRATION: 8-season threshold; 30% Conviction shift probability; +1 Disposition shift] — UN-NRES-AUDITED.

**Historical anchor.** Tokugawa *sankin-kōtai*; medieval ward exchange; Welsh princes raised at English court.

---

# PHASE D — Highest-interaction (sim-validation required)

## P9 — Leagues (non-bloc-vote)

**Phase:** D · **Status:** COMMIT-REVISED · **Layer:** 3

**Adds:** New treaty type to `faction_layer §3.1`.

**League formation.** 2+ non-Crown duchies/subnational factions may form League. Crown structurally excluded.

**League terms:**
- Each member contributes Influence −1/season to shared "League Capacity"
- Members may declare Joint Embargo or Joint Blockade against non-member targets — single coordinated action, Wealth cost shared by Influence contribution
- Members may declare Joint Parliamentary Motion — co-sponsored (Mandate floor lowered by one), **individual votes remain individual (NOT bloc-summed)**
- Members may not attack each other militarily without first formally exiting (Stability −2 cost on exit)
- Members gain Standing-with-League-peers +1 baseline while membership active

**League fragility to Cultural Orientation:**
- League membership Standing bonus +1 reduced by half if member territories' average `cultural_orientation` (F1) ≥ 3
- Joint Action Wealth cost-sharing increases by 50% if average ≥ 4
- League dissolves automatically if average ≥ 5 (Italic League pattern)

**League dissolution.** Any member may exit at Stability −2. Auto-dissolve at <2 members. Parliamentary Recognition Challenge on Supermajority pass: all members Mandate −1.

**Caps.** Max League membership: 3 factions. Max 1 League at a time on peninsula. League actions consume one Senator action slot per coordinated event.

**Historical anchor.** Hanseatic League (Hansetag pattern — individual ratification, not bloc voting); Lombard League vs Frederick Barbarossa; Italic League (fell to external transformation, matching fragility mechanic).

---

## I1 — Provincial Charter Track (capped at 4)

**Phase:** D · **Status:** COMMIT-REVISED · **Layer:** 3 · **`[AUDIT-FLAG]`** `peninsular_strain §6.1` supersession not verified

**Adds:** New tracked attribute per non-Crown duchy. Charter Track 0–4 (Charter 5 STRUCK to preserve GD-1).

**Charter levels:**

| Charter | Status | Constitutional position |
|---|---|---|
| 0 | Full Crown integration (never default) | — |
| 1 | Standard vassalage (game start) | Crown initiates Govern, military levy, religious decree |
| 2 | Privileged status | Crown cannot initiate Govern actions without duchy consent |
| 3 | Confederate | Duchy signs Crown Treaties as peer; votes separately in Parliament |
| 4 | Sovereign-allied | Duchy may form Leagues without Crown invocation; duchy military operations against Crown allies don't generate CB for Crown |

**Critical GD-1 constraint:** territories within Charter-4 duchy **still count toward Peninsular Sovereignty.** Charter is constitutional path, not territorial exclusion.

**Advancement (+1/arc max, one path per advancement):**
- **Parliamentary Recognition:** Mandate ≥ 4 + vote pass at majority. Crown may invoke Recognition Challenge within 1 arc to reverse
- **Sustained Defiance:** duchy refuses 3 consecutive Crown Domain Actions targeting its province + maintains Mandate ≥ 4 across all 3 seasons. Crown gains CB; duchy gains Charter +1
- **Foreign Recognition:** external power (Schoenland Mediation Stance ≥ 4 / Altonia at IP ≥ 60 / peninsular faction with Mandate ≥ 5) formally recognizes duchy
- **Decisive Military Victory:** Charter advances +1 on Overwhelming military victory against Crown forces with subsequent Treaty signing within 4 seasons. Portuguese pattern (Ourique 1139 + Treaty of Zamora 1143). Without subsequent treaty, no advancement.

**Reverse triggers (−1 per occurrence):**
- **Crown Reconquest:** Crown takes any duchy-seat settlement via military conquest. Permanent in current arc
- **Charter Annulment:** Crown Mandate ≥ 6 + Supermajority parliamentary vote (R4 eligible). Cannot reduce below Charter 1 except via military reconquest

**Composition.** P9 Leagues (Charter 4 enables); PT2 (heir residency = constitutional respect, Ob −1).

**Historical anchor.** Scotland independence (1296–1357); Swiss Confederation; Portugal from León; Polish-Lithuanian Commonwealth.

---

## I2 — Urban Communal Petition (single emergence path)

**Phase:** D · **Status:** COMMIT-REVISED · **Layer:** 3

**Adds:** New settlement-scale subnational entity at City and Port settlements.

**Petition trigger.** City or Port settlement satisfies all of:
- Prosperity ≥ 3
- Order ≥ 3
- Aggregate Local Actor Disposition with controlling faction ≤ 0 for 3 consecutive Accountings

Settlement may generate Urban Communal Petition. One per arc per settlement.

**Petition demands:**

| Demand | If Granted | If Refused |
|---|---|---|
| **Charter of Liberties** | Settlement may not be levied for military without Petition Council consent; Order +1 | Order −1, Disposition −2 |
| **Trade Monopoly** | Settlement Prosperity yield to faction Treasury halved; settlement Prosperity +1/arc until cap; Disposition +2 | Order −1, Disposition −2 |
| **Magistrate Independence** | Settlement governance not overruled by Provincial Authority for 4 seasons; Order +1 | Order −1, Disposition −2 |
| **Religious Tolerance** | Inquisitor Base ineffective (Heresy Investigation +2 Ob); +1 Disposition with `practitioner_aware` Local Actors | Order −1, Disposition −2 |

**Refusal cascade.** If Provincial Authority refuses 3 consecutive Petitions from same settlement, settlement converts to **Communal Status**: Provincial Authority treated as foreign for Disposition; settlement eligible to host Insurgency emergence per `insurgency_pipeline §4.1` (standard, not new path); Promoted Faction inherits unfulfilled Petition demands as starting Mission tags.

**Does NOT add new insurgency emergence path.** Uses existing GD-3 §4.1; distinctive property is *mission inheritance*.

**Historical anchor.** Lombard League cities; Flemish urban revolts (Golden Spurs 1302); Italian communal movement 11th–13th c.

---

## F4 — Foreign-Backed Insurgency (promotion modifier)

**Phase:** D · **Status:** COMMIT-REVISED · **Layer:** 2 · **`[AUDIT-FLAG]`** `insurgency_pipeline §5.2` supersession not verified

**Modifies:** `insurgency_pipeline §5.2` promotion outcome branching; adds status modifier (not new emergence branch).

**Standard emergence preserved.** Insurgencies emerge through canonical GD-3 §4.1 (2+ contiguous Uncontrolled territories sustained 2 seasons).

**Promotion-time modifier.** At Stage 4 promotion, evaluate formation settlements:
- If at least one settlement had `cultural_orientation` ≥ 4 (per F1) at formation time AND IP ≥ 60 at promotion time AND (Schoenland Mediation Stance ≤ 1 OR Altonian Alignment fired on any peninsula NPC faction in last 8 seasons):
- **Probability gate:** Foreign-Backed status materializes with probability based on Altonia's Vanguard Commander engagement state:
  - Vanguard Commander actively focused on Valoria: 75% probability
  - Vanguard Commander aware but not focused: 40% probability
  - Vanguard Commander dormant or distracted: 0% probability

Probability gate captures historical pattern (Polish-Hussite case): foreign sympathy frequently fails to convert to operational backing.

**Foreign-Backed stat profile** (when materializes):
- Military +1 above RM baseline
- Wealth +1 above RM baseline
- Mandate +1 above RM baseline
- Status: extra-parliamentary (overrides PT-based determination)

**Behavior.** AI prioritizes border settlements (per F3) and Schoenland-route settlements; automatic informal treaty offer to Altonian forces if IP=100 Phase 1 fires; other factions have standing "Foreign Alignment" CB.

**Suppression paths** (any one sufficient):
- **Tier 1: Military reconquest** — standard Insurgency suppression
- **Tier 2: Diplomatic resolution via Schoenland Mediator** — Mediation Stance ≥ 3 + Diplomatic Conference invocation (per F2). Foreign-Backed status converts to standard Insurgency
- **Tier 3: Cultural Reconciliation** — Cultural Orientation in held settlements reduced to ≤ 2 across all settlements via I3 actions

**Composition.** F1 Cultural Orientation; F2 Schoenland Mediation Stance; F3 Border Burden; I3 Cultural Reconciliation.

**Historical anchor.** English backing of Dutch Revolt from 1585; Habsburg backing of Stuart pretenders; Aragonese backing of Cathar resistance. Inverse: Polish-Hussite case.

---

## PR2 — Accommodation Settling-of-Accounts

**Phase:** D · **Status:** DEFER-PENDING-AUTHORING · **Layer:** 2

**Cannot commit until:**
1. Postwar tribunal procedure authored as `social_contest §7.1`-parallel canon
2. Conviction Scar +3 magnitude reconciled with `faction_politics §3.6.2` Reformation trigger
3. P8 16-season carve-out for Wartime Collaboration CB explicit

**Spec (held for authoring):**

When Repulsion fires, every faction-and-NPC instance of Altonian Alignment checked.

**Accommodationist factions:**
- Exposed publicly during Occupation: existing effects + Standing-with-all-other-factions drops two steps additionally; faction Conviction Scar count +3 [pending §3.6.2 reconciliation]
- Unexposed during Occupation, discoverable: Repulsion event makes alignment automatically discoverable. All factions roll Investigation (Intelligence pool vs Ob 3); each successful discovery generates "Wartime Collaboration" CB. Multiple CBs may stack. **Non-decaying for 16 seasons** (carve-out from P8) [pending P8 explicit]
- Renounced before Repulsion: accommodationist may renounce at Wealth −2 + Mandate −1; renounced factions take half Standing penalties + no Wartime Collaboration CB; Cohort Cascade Fidelity input +1

**Accommodationist NPCs:**
- Public exposure: NPC Demoted-with-Dishonor per `faction_politics §1.0a`
- Postwar trial process (3 seasons): public scene cycle [pending tribunal procedure authoring]

**Historical anchor.** Post-WWII Liberation purges (France's *épuration*; Norway's *landssvikoppgjøret*; Italian *defascistizzazione*).

---

## PR4′ — Postwar Acceleration of Generational Realignment

**Phase:** D · **Status:** COMMIT-REVISED · **Layer:** 1 · modifies I3 parameter in specific conditions

**Mechanic.** For 16 seasons following Repulsion event, in territories that experienced Occupation:

I3 NATURALIZATION_THRESHOLD reduced from 24 seasons to **12 seasons** in those territories only.

**Effect.** Postwar generational drift operates at twice canonical rate in formerly-occupied territories. Local Actor replacement faster; Cultural Reconciliation actions produce faster integration.

**No new state.** Uses I3's existing `generation_origin` mechanism with temporary threshold modifier.

**Calibration.** [CALIBRATION: 16-season window; 12-season threshold (50% of canonical 24)] — starting values.

**Historical anchor.** Post-1945 European political realignment (Christian Democracy, social democracy); post-Reconquista Spanish consolidation.

---

## PT1 — Puppet Title Mechanic

**Phase:** D · **Status:** UN-NRES-AUDITED · **Layer:** 2+3

**Requires four-interrogation NRES audit before sim Stage 10.**

**Modifies:** Adds shell-substance separation for Crown title (Sengoku/Late Han pattern).

**Mechanic.** Crown title becomes separate asset from effective Crown power.

- **Unified Crown:** standard. Title and effective power held by same faction.
- **Puppet Crown:** title held by designated puppet (named NPC with Standing ≥ 4); effective power held by *administrator* faction. Puppet performs ceremonial functions; administrator operates Crown Domain Actions.

**Entry to Puppet Crown:**
- Crown faction Mandate drops to 0
- A non-Crown faction wins Faction Succession Contest against Crown but does NOT eliminate Crown line (Narrow Winner outcome)
- Magnate Crisis (per H1′) resolves with parliamentary-fallback outcome favoring administrator over incumbent

**Effects of Puppet Crown:**
- Puppet NPC retains Crown title; legitimating substrate for Crown Domain Actions (administrator operates as if controlling Crown)
- Crown title legitimating value persists at 75% of normal: Crown Treaties remain in effect; CI generation continues; international recognition treats title as continuing
- Administrator pays Wealth −2/arc for "Court Maintenance"
- Administrator may NOT pursue I1 Charter advancement
- Other factions may invoke "Restoration" CB against administrator

**Exit from Puppet Crown:**
- **Restoration:** another faction wins Mass Battle Overwhelming against administrator AND puppet NPC publicly endorses restoring faction. Crown returns to Unified under restoring faction
- **Title Consumption:** administrator at Mandate ≥ 5 formally consumes title — Crown line ends; administrator's leader takes Crown title personally. Cost: −2 Mandate, all Crown Treaties enter Renewal Check (per P10), Crown legitimating value drops permanently to 50%. (Late-Han Cao Pi 220 CE pattern.)
- **Death of puppet:** if puppet dies without designated successor in Crown line, Puppet Crown ends with title consumption

**Calibration.** [CALIBRATION: 75% legitimating value during Puppet Crown — which specific effects degraded?; Court Maintenance −2/arc — which Accounting?; Title Consumption cost values] — UN-NRES-AUDITED.

**Historical anchor.** Emperor Xian as puppet (189–220 CE) — Cao Cao as administrator; Cao Pi consumed title 220. Ashikaga shogunate persisting past Nobunaga's deposition (1573–1588).

---

## Crown Legitimacy Contestation Track

**Phase:** D · **Status:** UN-NRES-AUDITED · **Layer:** 2+3

**Requires four-interrogation NRES audit before sim Stage 10.**

**Modifies:** Adds Crown Legitimacy Contestation tracked aggregate.

**Mechanic.** Crown carries **Contestation Count** representing number of non-Crown factions actively claiming Crown legitimacy through structural surfaces.

**Contestation surfaces** (each non-Crown faction contributes 0 or 1):
- Faction holds Charter Track ≥ 2 (constitutional claim, per I1)
- Faction operates active Practitioner Cell in any province (theological claim, per R3)
- Faction has held Mandate ≥ 5 for 4+ consecutive seasons (political-weight claim)
- Faction has won Faction Succession Contest against another faction in last 8 seasons (demonstrated capacity)
- Faction has signed Foreign Recognition from external power (diplomatic claim)
- Faction operates Practitioner Cell with `practitioner_aware` distribution ≥ 30% across its provinces (substrate-truth claim)

**Contestation effects:**

| Contestation Count | Effect on Crown |
|---|---|
| 0–1 | No effect |
| 2 | Crown +1 Ob on Domain Actions in non-Crown territories |
| 3 | Crown +1 Ob on all Domain Actions |
| 4 | +1 Ob on all DAs + Cohort Cascade Fidelity input −1/arc (composes with H1′) |
| 5+ | +2 Ob on all DAs + Cohort Cascade Fidelity input −1/arc + Florence Risk Marker: faction may not initiate Crown Treaty for 4 seasons |

Captures Florence failure-mode pattern: shell legitimating value contested by multiple factions simultaneously.

**Calibration.** [CALIBRATION: surface threshold values; effect band magnitudes; operational measurement procedures per surface] — UN-NRES-AUDITED.

**Historical anchor.** Florence's Republic identity claimed by both Medici-allied and anti-Medici factions; serial regime change 1378–1569.

---

## §6 Follow-up authoring registry

Items to author as separate canon-authoring passes:

1. **Articulation tier authoring** — R2′ Martyrdom Marker, H1′ Magnate Crisis trigger, H2 Inner Circle removal cascade, PR1 Settlement Dividend distribution need articulation_layer tier assignment in coordinated pass
2. **Mission alignment schema completion** — ensure all faction Missions tagged for Local Actor Conviction matching (P3 dependency)
3. **Cultural Reconciliation as Varfell unique action variant** — F1 reduction mechanism references; needs spec
4. **Cohort Cascade Fidelity starting values per faction** — H1′ trigger inputs need pre-computed game-start values
5. **NPC purge mechanism** — H3 includes purge option; canonical procedure needed
6. **Postwar tribunal procedure** — PR2 3-season trial cycle; should compose with `social_contest §7.1` as parallel trial-type (blocker for PR2 commit)
7. **Conviction Scar +3 reconciliation** — PR2 specifies +3; reconcile with `faction_politics §3.6.2` Reformation trigger
8. **P8 Wartime Collaboration CB carve-out** — PR2 specifies 16-season non-decay; make P8 exception explicit
9. **Decisive Military Victory Treaty path implementation** — I1 Treaty-signing-within-4-seasons mechanism
10. **PT1 Puppet Crown UI representation** — major game-state change requires player communication
11. **Crown Legitimacy Contestation UI** — Contestation Count player-visible representation
12. **PT2 heir designation mechanic** — which NPCs qualify as designated heirs
13. **NRES audit of PT1, PT2, Crown Legitimacy Contestation** — required before sim Stage 10
14. **Sim Stage 10 test plan** — comprehensive test scenarios for compounding cases
15. **Canon-cleanup pass** — reconcile `faction_layer §3.5` 4-source CB list with `parliamentary_transfer §3` 8-source list (P8 dependency)
16. **Audit verification of 10 remaining supersession claims** (Sprint 0 continuation)
17. **Compounding case enumeration against canon** (Sprint 0 continuation)
18. **Operational definition audit** (Sprint 0 continuation)
19. **Selection principle audit** (Sprint 0 continuation)

---

## §7 Sim Stage 10 test plan

**Phase A baseline tests:**
1. R1 + P11 + F1 + P1 (with P2 field) in isolation — each proposal's individual effects per Test Conditions, across faction permutations
2. P1 + P2 + I3 composition: occupation-cycle over 30+ seasons
3. R1 composition prep for downstream R2′/R3 testing

**Phase B tests:**
4. P2 + P3 + P4 + F3 in interaction — settlement-political layer compounding
5. F1 + F3 + F4 composition: foreign-pressure substrate cycle (F4 not yet built; baseline data only)

**Phase C tests:**
6. R4 + R2′ + R3 + H2 composition: Church under stress
7. H1′ + H2 + H3 composition: Magnate Crisis cycle
8. PR1 + PR3 composition: postwar settlement event-set

**Phase D tests:**
9. P9 + I1 + Crown Legitimacy Contestation: constitutional contestation cycle
10. F4 + Foreign-Backed suppression paths: all three tiers
11. PT1 entry/exit cycles
12. I2 Communal Petition cycles with refusal cascade

**Compounding stress tests (4 critical cases):**
13. Inner Circle NPC death during faction transition (H1′ + H2 + H3 simultaneous)
14. Tribunal Conviction of Inner Circle Ministry-running NPC (R2′ + H2 + H3 simultaneous)
15. IP=100 invasion with high F1 substrate + active F4 + active R3 Practitioner Cells
16. Magnate Crisis with Contestation Count ≥ 5 (Crown under multiple pressures)

**Acceptance criteria:**
- No campaign reaches unrecoverable state from single-mechanic firing
- Compounding cases produce meaningful pressure but not unrecoverable cascade
- GD-1, GD-2, GD-3 preserved in all simulated scenarios
- All proposals demonstrably contribute to gameplay (no marginal-noise mechanics)

---

## §8 Operational definition for "strategic relevance" (sim variance threshold)

> A rule produces gameplay-significant variance if it changes [specified outcome metric] by ≥10% over baseline-without-rule, in ≥80% of N=20 seeded runs.

**Per-proposal outcome metric:**

| Proposal | Outcome metric |
|---|---|
| P1 | Local Actor Disposition at season 12 post-conquest |
| R1 | Percentage `practitioner_aware` Local Actors generated at game start |
| P11 | Count of Standing-shift events in third-party factions per battle |
| F1 | `cultural_orientation` distribution across settlements after 4 arcs of trade |
| (others) | To be specified during Sprint 3 |

---

## §9 Sim infrastructure scaffolding requirements

Before any tests, sim harness must provide:

- **Per Local Actor:** Disposition with each faction, `witness_tradition`, `generation_origin`, current settlement
- **Per settlement:** Order, Prosperity, Defense, controlling faction, `pre_conquest_faction_id`, `cultural_orientation`, active Local Actors
- **Per province:** Accord, Practitioner Cell status, fracture state
- **Per faction:** Mandate, Stability, Wealth, Treasury, Cascade Fidelity, Conviction Scars per Inner Circle NPC, Standing matrix
- **Per season:** all changes to above, with source attribution
- **Reset-to-state checkpoints:** save scenario state at season 0; replay-from-checkpoint with seeded RNG
- **Statistical aggregation:** N=20 seeded runs; mean and variance on outcome metrics

---

## §10 Supersession map

| Proposal | Canon document | Audit status |
|---|---|---|
| **P8** | `faction_layer §3.5` | ✓ verified; canon-inconsistency flag added |
| **R4** | `worldbuilding §6.2` | ✓ verified; scope narrowed to Motion of No Confidence only |
| **H3** | `victory §3.6a` | ✓ verified; scope clarified as Löwenritter Coup + extension |
| P6 | `settlement_layer §3.3` | `[AUDIT-FLAG]` |
| R2′ | `social_contest §7.1` | `[AUDIT-FLAG]` |
| R3 | `solmund §12` | `[AUDIT-FLAG]` |
| F1 | `worldbuilding §7.2` | `[AUDIT-FLAG]` |
| F2 | `march_layer §6.3` + `valoria_political_hierarchy §1.2` | `[AUDIT-FLAG]` |
| F4 | `insurgency_pipeline §5.2` | `[AUDIT-FLAG]` |
| I1 | `peninsular_strain §6.1` | `[AUDIT-FLAG]` |
| P10 | `treaty_expiration §1.1` (extension) | `[AUDIT-FLAG]` |
| P11 | `mass_battle §E` (extension) | `[AUDIT-FLAG]` |
| F3 | `mass_battle §A.14b` (extension) | `[AUDIT-FLAG]` |
| PT1 | Crown faction operations | `[UN-NRES-AUDITED]` |
| CLC | New Crown stat | `[UN-NRES-AUDITED]` |

**Verified: 3 of 13.** Remaining 10 require canon-reading work before Phase A commits can proceed.

---

## §11 Composition graph

```
P1 ←→ P2 ←→ I3 ←→ F1 ←→ F3 (settlement substrate layer)
                        ↓
                       F4 (foreign-backed insurgency from substrate)

R1 ←→ R2′ ←→ R3 ←→ R4 (religion/confessional layer)
       ↓
      H2 (Inner Circle removal cascade if convicted person is IC)

H1′ ←→ H2 ←→ H3 ←→ P10 (horizontal faction-internal layer)
            ↓
           PT1 (Puppet Crown can emerge from H1′ parliamentary fallback)

P9 ←→ I1 ←→ I2 ←→ F2 (constitutional/lateral layer)
            ↓
   Crown Legitimacy Contestation (aggregates inputs from I1, R3, others)

PR1 ←→ PR3 ←→ PR4′ (postwar layer; fires together on Repulsion)
       ↓
      PR2 (settling-of-accounts; pending authoring)
```

---

## §12 Status declaration

**STATUS: PROPOSAL V3.1 — Pre-canon.**

The integrated set comprises **31 proposals** across four phases, plus Sprint 0 pre-execution audit work that is ~25% complete.

**Pre-execution work remaining (Sprint 0):**
- 10 of 13 supersession claims unverified
- Compounding case enumeration not executed
- Operational definition audit not executed
- Selection principle audit not executed
- NRES audits of 3 candidate proposals (PT1, PT2, CLC)

**Phase A commit gate requires Sprint 0 completion.** Each proposal's authoring depends on its supersession being verified against actual canon text. Unverified supersession claims may assert text that doesn't exist or miss canon text that does.

The set preserves GD-1 (peninsula-only victory), GD-2 (mandatory threat response), GD-3 (insurgency pipeline) in all proposals as currently specified.

**Companion documents:**
- `valoria_workplan_v1.md` — execution plan with Sprint 0 through Sprint 18
- `institutional_persistence_pre1600.md` — historical research underlying design decisions

---

*End of Valoria — Integrated Mechanics Design Document V3.1.*
