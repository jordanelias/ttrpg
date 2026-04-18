<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: calamity_radiation_v30_infill.md -->

<!-- v30 baseline — renamed from designs/setting/calamity_radiation.md on 2026-04-13 -->
# VALORIA — Calamity Radiation Framework
## Status: CANONICAL — approved 2026-04-06
## Scope: Geographic graduation of Rendering Stability (RS) threshold effects by node distance from Askeheim (T15)
## Cross-references: designs/ttrpg/threadwork_redesign_v25.md §5.3, §6; designs/setting/geography_design.md §Calamity Bleed Gradient

---

## Design Principle

The RS threshold system (threadwork_v25 §5.3) defines **what** effects occur at each RS band. This document defines **where** those effects manifest, based on node distance from Askeheim (T15) — the epicenter of the Einhir Catastrophe.


---

## Settlement-Type Radiation Modifier (Throughline T1)

Within a province, different settlement types experience radiation effects at different MS bands:

| Settlement Type | Radiation Modifier |
|----------------|-------------------|
| Outpost (near Askeheim: S-011, S-033, S-034) | Effects manifest one MS band earlier than province level |
| Town, Mine (distance-1/2 provinces) | Effects manifest at province level (no modifier) |
| Fortress, City, Seat | Effects manifest one MS band later (institutional buffer) |
| Cathedral | Population Certainty preserved one band later (psychological buffer). Physical substrate effects at province level. |

The radiation creeps inward from the periphery. Frontier outposts fall first. The Seat is the last to feel the Catastrophe's reach.

---

## Node Distance Map (from Askeheim T15)

| Distance | Territories |
|---|---|
| 0 | T15 Askeheim |
| 1 | T6 Stillhelm, T13 Oastad |
| 2 | T5 Feldmark, T12 Sigurdshelm |
| 3 | T1 Valorsplatz, T14 Ehrenfeld, T4 Grauwald, T11 Halvardshelm |
| 4 | T2 Kronmark, T16 Schoenland, T9 Himmelenger, T7 Rendstad, T10 Spartfell |
| 5 | T3 Lowenskyst, T8 Gransol, T17 Halvarshelm |

---

## Radiation Matrix

Each cell describes the instability state for that combination of RS band and node distance. Effects are cumulative downward (lower RS bands include all effects from higher bands).

### RS 100–80 (Stable)

| Distance | State | Effects |
|---|---|---|
| 0 (Askeheim) | Wound persists (contained) | Gaps and tears from the Calamity remain open. Wardens maintain active Mending operations. Forgetting active (see §Forgetting below). Micro-Gap emergent beings present intermittently (non-combat, Thread Sensitivity (TS) 20–40). No effects radiate beyond Askeheim at this band. |
| 1–5 | Normal | No Calamity effects. |

### RS 79–60 (Strained)

| Distance | State | Effects |
|---|---|---|
| 0 (Askeheim) | Wound strained | As Stable, plus: all non-Thread orders +1 Obstacle (Ob). Micro-Gap emergent beings more frequent. Forgetting active. |
| 1 | Folklore | Strange happenings. Non-practitioners uneasy near old Einhir sites. Oral traditions of the Calamity survive. Church Influence +1 Ob (cultural resistance). No mechanical instability. |
| 2–5 | Normal | No Calamity effects. |

### RS 59–40 (Fragile)

| Distance | State | Effects |
|---|---|---|
| 0 (Askeheim) | Consistent minor presences | Shifting Objects common (1d3 per season at Accounting). Standard Gap emergent beings present (TS 50–70, non-hostile unless provoked). +1 Ob all non-Thread orders (stacks with existing +1 = total +2 Ob). |
| 1 | Minor instability begins | Spontaneous Shifting Objects (1 per season at Accounting, 1d10: fires on 1–2). Thread operations +1 Ob. Non-practitioners with TS 10+ sense unease. |
| 2 | Folklore begins | Strange happenings. Inconsistent memories near Einhir ruin sites. No mechanical effects. |
| 3–5 | Normal | No Calamity effects. |

### RS 39–20 (Fractured)

| Distance | State | Effects |
|---|---|---|
| 0 (Askeheim) | Persistent beings | Persistent standard Gap emergent beings (multiple, TS 50–70). Gaps open spontaneously (1 per season, automatic). Expedition Ob +1 (stacks with all other modifiers). |
| 1 | Consistent instability | Spontaneous Shifting Objects (1 per season, automatic). Spontaneous Gaps possible (1d10 per season at Accounting: fires on 1–2). Non-practitioners experience rendering failures — inconsistent memories, déjà vu, objects in wrong places. |
| 2 | Minor instability | Spontaneous Shifting Objects (1d10 per season: fires on 1). Thread operations +1 Ob. Non-practitioners with TS 10+ sense wrongness. |
| 3 | Folklore | Strange happenings begin. Oral reports of unsettling events. No mechanical effects. |
| 4–5 | Normal | No Calamity effects. |

### RS 19–1 (Critical)

| Distance | State | Effects |
|---|---|---|
| 0 (Askeheim) | Catastrophic instability | Multiple persistent beings (including rare catastrophic Gap emergent, TS 80+). Gaps open spontaneously (1d3 per season). Expedition Ob +2 (stacks). Mending Ob +1 (substrate resistance). |
| 1 | Persistent presences | Micro-Gap emergent beings present (TS 20–40, intermittent). Spontaneous Gaps semi-regular (1d10 per season: fires on 1–4). All Thread operations +1 Ob. All non-Thread orders +1 Ob. Non-practitioners experience consistent rendering failures. |
| 2 | Consistent instability | Spontaneous Shifting Objects (1 per season, automatic). Spontaneous Gaps possible (1d10: fires on 1–2). Thread operations +1 Ob. Rendering failures for non-practitioners begin. |
| 3 | Minor instability begins | Spontaneous Shifting Objects (1d10: fires on 1). Non-practitioners sense wrongness. Discovery Events possible (TS growth checks for witnesses). |
| 4 | Folklore | Strange happenings. Oral reports. No mechanical effects. |
| 5 | Normal | No Calamity effects. |

### RS 0 (The Rupture)


---

## Southernmost Surge (Threshold Event: RS ≤ 10)

When RS drops to 10 or below, a Southernmost Surge fires at the next Accounting. This is a one-time event per campaign (does not repeat if RS rises above 10 and drops again).



---

## Threadcut Being Classification by Gap Severity


| Classification | Gap Severity | Thread Sensitivity (TS) Range | Self-Sustaining Capacity | Combat Status |
|---|---|---|---|---|
| Micro-Gap emergent | Micro-Gap (closes within scene) | 20–40 | Hours to days. Intermittent presence — flickers in and out of intelligibility. | Non-combat. Barely perceivable (TS 30+ required). Appears as flicker, unease, or momentary wrongness. |
| Standard Gap emergent | Standard Gap (persists without Mending) | 50–70 | Seasons. Sustained self-rendering. Can interact with the rendered world. | Combat-capable. Observer-dependent rendering per threadwork_v25 §6.2. Health pool = Spirit × 2. |
| Catastrophic Gap emergent | Catastrophic Gap (3+ seasons, Ob 7+ to Mend) | 80+ | Years to indefinite. Structural-scale self-maintenance. | Campaign-level entity. Solmund-class. Capable of external Thread operations. RS cost per scene (PP-197 applies at TS 90+). |


**Behaviour:** Threadcut beings are not hostile by default. They have no relationship to organic life's concerns. They exist. Their existence draws on the same substrate practitioners use, which is why their presence adds +Ob to Mending operations (threadwork_v25 §9.7, P-17). They may be indifferent, curious, or territorial — Game Master determines based on the being's configurational character.

---

## Board Game Mode Implementation

Each territory card includes a **Proximity Rating** (0–5, printed, based on node distance from Askeheim). At Accounting, the Game Master (or facilitator in competitive BG) performs one lookup per territory: current RS band × Proximity Rating → instability state from the radiation matrix.

**Simplified BG Lookup Table:**

| RS Band | Proximity 0 | Proximity 1 | Proximity 2 | Proximity 3 | Proximity 4–5 |
|---|---|---|---|---|---|
| 100–80 | No radiation (Askeheim-only: wound persists, Forgetting active) | — | — | — | — |
| 79–60 | +1 Ob non-Thread; Forgetting active | Folklore (no mech) | — | — | — |
| 59–40 | +2 Ob non-Thread; Shifting Objects | +1 Ob Thread; Shifting Objects (1d10: 1–2) | Folklore (no mech) | — | — |
| 39–20 | Gaps auto; beings present | +1 Ob all; Gaps (1d10: 1–2) | +1 Ob Thread; Shifting Objects (1d10: 1) | Folklore (no mech) | — |
| 19–1 | +2 Ob Mending; beings; Gaps (1d3) | +1 Ob all; Gaps (1d10: 1–4) | +1 Ob Thread; Gaps (1d10: 1–2) | Shifting Objects (1d10: 1) | Folklore (no mech) |

This is a single-page reference card. One lookup per territory per season.

---

## Integration Notes

### Supersedes

### Cross-references requiring propagation
- `designs/ttrpg/threadwork_redesign_v25.md` §5.3: RS threshold table notes geographic graduation per calamity_radiation.md (ED-302 callout present). [DONE]
- `references/params_board_game.md`: RS Effects section rewritten to use Simplified BG Lookup Table; Southernmost Zones replaced with Proximity Rating system. [DONE — 2026-04-06]
- `designs/fieldwork/fieldwork_v30.md` §8.1: Survey action (BG Consul Inward variant) uses Proximity Rating to set Ob. Formula: Ob = (5 − Proximity Rating) + 1, min 1. Askeheim (PR 0) → Ob 6; Lowenskyst (PR 5) → Ob 1. Calamity zone Exposure thresholds apply to fieldwork actions in proximity territories per §6 Exposure Track. [DONE — 2026-04-17]

## Forgetting — Permanent Askeheim Condition (B-03 resolved)




**Interaction with RS decline:** As RS drops, the Forgetting does not worsen (it is already total within Askeheim). What worsens is the radiation of OTHER effects (Gaps, beings, Ob modifiers) outward from Askeheim. The Forgetting remains contained at T15 regardless of RS.

### Hybrid Mode Note (B-09)
Calamity Radiation Ob modifiers apply to both Personal Phase Thread operations (TTRPG rules) and Strategic Phase Thread orders (BG rules) in Hybrid mode. Coherence cost from PC-declared leadership (PP-198) stacks independently with Radiation Ob modifiers. This double cost is philosophically correct — operating near the wound is harder AND degrades the practitioner.

### Open editorial items
- ED-302: Calamity Radiation Framework — this document. RESOLVED.
- B-01: Askeheim effects at RS 100–80 — RESOLVED. Effects contained to Askeheim only at Stable band; no radiation. Band split into 100–80 (Stable) and 79–60 (Strained).
- B-03: Forgetting RS-dependence — RESOLVED. Forgetting is permanent at Askeheim, conditioned on unhealed Gaps/tears, not on RS. Cessation requires full territorial Mending.
- [EDITORIAL: ED-303 — RS track naming: "Rendering Stability" vs alternative. User flagged that "rendering" is a process of consciousness, not reality. Current name measures world substrate stability. Options: keep current (defensible — measures stability of the rendered output), rename to "Substrate Integrity" or "Configurational Stability." Deferred to user decision.]

