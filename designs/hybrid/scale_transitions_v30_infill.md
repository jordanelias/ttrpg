<!-- INFILL — prose/rationale extracted from scale_transitions_v30.md -->
<!-- Skeleton: scale_transitions_v30.md -->

# Scale Transitions and Mode Bridge Design
## Version: v1.0 | Date: 2026-04-13
## Status: DESIGN — canonical for scale transitions and mode bridging
## Sources: params_scale_transitions.md, PP-089/090, PP-103, PP-107–112, PP-232, PP-261, PP-340–343
## Supersedes: compilation/v0.14/stage11_scale_transitions_deprecated.md
## §1 Three-Mode Architecture
Valoria operates in three modes. TTRPG is the baseline layer — all mechanics are grounded here. Board Game (BG) abstracts to strategic scale. Hybrid bridges between them.
**Frame:** TTRPG ← Hybrid → Board Game. Hybrid is not a third mode — it is the bridge that allows TTRPG scenes to occur within a BG strategic context, and BG outcomes to generate TTRPG scenes.
## §2 Scale Table
## §3 Eight Handoff Rules
These rules govern how actions in one system translate to effects in another. Each handoff is a defined procedure, not a GM judgment call.
### §3.1 Personal → Thread
### §3.2 Personal → Faction
### §3.3 Personal → Scene (Contest)
Personal roll may serve as opening move or Appeal in a Contest (social_contest_system_v2.md). The personal action transitions to structured social resolution.
### §3.4 Scene → Faction (Domain Echo)
Successful Appeal/Debate at sufficient scope (§7) → Domain Echo fires. No extra roll required. The personal-scene outcome directly produces a faction-level consequence.
### §3.5 Thread → Faction
### §3.6 Thread → Mass (Mass Battle Integration)
Combat Thread operations: declared Phase 1, fire Phase 2 (before Engagement). Support Thread operations: declared Phase 1, fire Phase 5 Step 4–5 (Cascade). Binding Operations follow Phase 4 timing (ED-050 resolved).
### §3.7 Mass → Personal (General Duel)
### §3.8 Scene → Mass
### §3.9 Fieldwork ↔ All Systems
Fieldwork scenes (exploration, investigation, socializing) are personal-scale TTRPG actions that can handoff to or receive handoffs from any other system. These are defined procedures, not GM judgment calls.
## §4 Zoom In / Zoom Out Protocol
The Zoom mechanism allows Hybrid mode to transition between BG strategic play and TTRPG personal scenes.
### §4.1 Zoom In
**Definition:** Transition from BG layer to a personal TTRPG scene occurring within the BG strategic context.
**Ordering:** Multiple simultaneous Zoom Ins resolve in Attunement order. Ties: Agility. Further ties: GM. (ED-072, ED-160)
### §4.2 Zoom Out
### §4.3 Arc-Specific Zoom In Triggers (PP-556)
## §5 Domain Echo
Domain Echo is the primary bridge mechanism between personal-scale outcomes and faction-scale consequences.
### §5.1 Trigger
### §5.2 Amount
### §5.3 Timing by Mode
- **Hybrid (Zoom In active):** Domain Echo queues; fires at next BG Seasonal Accounting Step 3 (Cascade Phase).
### §5.4 Debate → Domain Echo (PP-108)
## §6 Mode Transition Procedures
### §6.1 TTRPG → BG (Session Boundary)
Faction stats carry over from TTRPG narrative into BG faction mat. Personal character stats suspended — characters are abstracted into faction identity. Queued Domain Echoes from the TTRPG session apply at first BG Accounting.
### §6.2 BG → Hybrid (Mid-Game Zoom In)
### §6.3 Hybrid → TTRPG (Zoom Out)
Board state updated from personal scene results via Domain Echo. Personal character continues in TTRPG mode if the session is transitioning. BG clock advances only at Accounting (not during personal scenes).
### §6.4 Coherence Initialization (PP-200)
### §6.5 Hybrid Coherence Cost (PP-198)
## §7 Sufficient Scope — Register Shift Trigger
A personal scene qualifies as faction-scope (triggering Domain Echo) when it involves at least one of:
3. An action that would normally require a Domain Action roll (treaty negotiation, formal accusation, territorial claim)
Personal conflicts (brawls, private debates, social introductions) are personal scope only. GM makes final scope determination. (ED-074 resolved)
## §8 Scope Shift Rules
Once per round, declared at turn start. No roll required. Second scope action in same round costs +1 Inspiration. This prevents rapid scale-hopping within a single encounter.
## §9 PC Faction Embedding (ED-075)
## §10 Thread Timing in Hybrid (PP-125, PP-260)
## §11 Contested Figure System (ED-167, ED-168)
A Contested Figure is a named NPC who is simultaneously present in both personal and mass battle contexts during a Hybrid Zoom In.
- CF killed between sequential Zoom Ins → redirected to another named NPC, or Zoom Out with no action consumed if no valid target
