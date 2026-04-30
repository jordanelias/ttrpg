<!-- [PROVISIONAL: 2026-04-29 — Conviction Track promoted to first-class doc per PP-681, addressing PP-676 v3 §V3-5 multi-graph isolate finding] -->
<!-- STATUS: CANONICAL — extracted from designs/npcs/npc_behavior_v30.md §1.2 + §3.3 + §3.4 -->
<!-- AUTHORITY: PP-681, ED-768. Source authority: ED-663, ED-664 (Thread Operation triggers); ED-672 (Arc A timing) -->

# Valoria — Conviction Track

The Conviction Track is the personal-scale moral-belief mechanic. Every NPC and PC has a primary Conviction (and may have a secondary), accumulates Conviction Scars from witnessing morally-loading events (Thread operations, ethical violations, etc.), and at sufficient Scar count enters a Conviction crisis where their behavior becomes unpredictable.

This document is the canonical reference for the Conviction Track mechanic. NPC priority trees, Resonant Style activation, and arc transitions consume Conviction values from this spec.

---

## §1 Conviction Taxonomy

| Conviction | Grounding Claim | What it values | What it dismisses |
|---|---|---|---|
| Faith | Value is revealed through divine authority | Doctrine, institutional continuity, spiritual obedience | Empirical contradiction, pragmatic objection |
| Order | Value is maintained through structure | Stability, procedure, predictability | Innovation, disruption (even beneficial) |
| Reason | Value is discovered through evidence | Knowledge, investigation, falsifiability | Tradition without justification, appeal to emotion |
| Equity | Value is distributed justly | Access, fairness, dismantling privilege | Institutional prerogative, hierarchical authority |
| Precedent | Value is inherited from what has been established | Legal continuity, constitutional procedure, institutional memory | Ad hoc decisions, revolutionary action |
| Autonomy | Value is chosen by the actor | Self-determination, operational freedom, survival | Universal moral claims, institutional demands |
| Continuity | Value is sustained through practice | The work itself, applied necessity, endurance | Politics, ideology, anything that does not directly serve the ongoing task |
| Community | Value is constituted through collective being | The group, the living tradition, the practice as shared act | Individual claims of authority or exception; hierarchy that displaces communal determination |
| Warden | Value is the maintenance of the boundary between rendering and collapse | The work of holding — Thread practice, Mending, substrate care | Political agendas that interfere with the maintenance work; ideology that claims priority over immediate necessity |

---

## §2 Scar Accumulation and Conviction Effects

| Scars | Effect on Conviction | Effect on Resonant Style | Effect on Behavior |
|---|---|---|---|
| 0 | Default configuration | Default configuration | Stable institutional behavior |
| 1 | Secondary Conviction activates alongside primary. Decision Forks increase. | No change | NPC exhibits internal conflict. Both Convictions influence decisions. |
| 2 | Primary Conviction may shift to secondary (engine judgment based on Scar content). NPC enters arc transition state. | Secondary Resonant Style activates permanently. NPC is now vulnerable on two fronts. | Institutional Tendency may diverge from personal behavior. NPC may take surprising actions. |
| 3+ | Conviction crisis. NPC acts unpredictably for 1 season (engine rolls on Conviction table below to determine each major decision). | All Resonant Styles active. NPC is socially exposed. | The NPC is in full transformation. Their arc has entered a terminal phase — they will either stabilise into a new configuration or be destroyed. |

**Conviction crisis table** (3+ Scars, engine rolls d6 per major decision):

| Roll | NPC acts on... |
|---|---|
| 1–2 | Original primary Conviction (habitual regression) |
| 3–4 | Secondary Conviction (conscious pivot) |
| 5 | Autonomy (survival instinct overrides both) |
| 6 | Whichever Conviction most aligns with the last PC interaction (relational pull) |

---

## §3 Thread Operation → Conviction Scar Triggers (ED-663, ED-664)

Thread operations witnessed by NPCs produce Conviction Scars. Parallels the Certainty Track movement triggers (params_core PP-551) but targets a different track: Certainty = cosmological framework shift; Conviction Scar = moral wound.

**Thread Event × Conviction Scar Matrix:**

| Thread Event Witnessed | Faith | Order | Reason | Equity | Precedent | Autonomy | Continuity |
|---|---|---|---|---|---|---|---|
| Dissolution of living being | **Scar** | **Scar** | **Scar** | **Scar** if powerless victim | **Scar** | **Scar** if unwilling | No |
| POP (history rewrite) | **Scar** | **Scar** | **Scar** | No | **Scar** | No | **Scar** if disrupts work |
| Lock on a being | No | No | No | **Scar** | **Scar** if no legal basis | **Scar** | **Scar** if prevents work |
| Mending a Gap | No | No | No | No | No | No | No |
| Weaving (non-harmful) | **Scar** | No | No | No | No | No | No |
| Rendering Crisis (witnessed) | **Scar** | **Scar** if disrupts environment | **Scar** | **Scar** if harms bystanders | No | **Scar** | **Scar** if disrupts work |

**Conditions:**
- **Witness requirement:** Direct witness (present in scene) or credible testimony (Evidence Track contribution + Disposition ≥ +1).
- **Certainty scaling:** C5: +1 Scar severity. C0: −1 Scar severity. C2–3: standard.
- **Season cap:** Max 1 Scar per season from Thread witnessing per NPC.
- **Mending exception:** Mending never produces Scars.
- **Faith specificity:** Faith NPCs Scar from ANY Thread operation except Mending.

**Player Conviction Checks (ED-664):**
Player witnesses Thread event → Spirit pool, TN 7, Ob 1. Failure: active Conviction shaken (mechanical = NPC Scar 1 effect) for 1 season.

---

## §4 Cross-references

- **Source extraction:** `designs/npcs/npc_behavior_v30.md` §1.2 + §3.3 + §3.4 (PP-681 promotion; original sections retained as redirect stubs)
- **Consumed by:**
  - `designs/architecture/scale_transitions_v30.md` §RS Change Triggers — Thread operation witnessed by NPC whose Conviction Scar fires
  - `designs/npcs/npc_behavior_v30.md` priority trees (Resonant Style activation per Conviction)
  - `designs/architecture/complete_systems_reference.md` §1.4 NPC Almud Arcs (Reformer/Fortress/Overthrown gated on Conviction state)
  - All NPC Conviction declarations (King Almud: Order; Confessor Arne: Faith; etc.)
- **Related mechanics:**
  - `designs/threadwork/threadwork_v30.md` §Certainty Track (parallel mechanic — cosmological shift vs moral wound)
  - `designs/threadwork/threadwork_v30.md` §Resonant Style (consumes Conviction values)
- **Editorial history:**
  - ED-663 (Thread Operation Conviction Scar matrix)
  - ED-664 (Player Conviction Checks)
  - ED-672 (Arc A timing window — Almud reform path uses Conviction state)
  - PP-681 / ED-768 (this promotion — extracted from npc_behavior_v30 into first-class doc)
