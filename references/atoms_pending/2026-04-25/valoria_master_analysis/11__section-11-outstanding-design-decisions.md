---
atom_id: valoria_master_analysis__11__section-11-outstanding-design-decisions
source_file: valoria_master_analysis.md
source_section: "Section 11 — Outstanding design decisions"
section_index: 11
total_sections: 13
line_count: 16
char_count: 1927
source_sha256: 23f5dbb51819c542
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## Section 11 — Outstanding design decisions

**1. Compound cascade ordering.** Bank Failure + Mercenary Defection + Plague + Financial Cascade + Peninsular Strain + Territorial Amalgamation all route through Wealth/Stability with cascade potential. Explicit ordering and trigger-priority required before any implementation. **Open design decision.**

**2. M-4 continuous-contestation as named commitment.** Valoria's acceptance of unresolved-contest as baseline game-state is deliberate and aligned with project intent but unusual for games preferring clear-victory. **Should be documented as explicit design commitment** rather than emergent-property-of-mechanics.

**3. Player-visibility cut.** Many proposals pass historical-N but may fail player-visibility (e.g., per-NPC ransom values add complexity without producing frequently-differentiated player choice in typical seasons). A player-visibility cut at throughline level would further reduce ~14 mechanics to ~8-10 most-differentiated. **Open design decision.**

**4. Retention vs consolidation tradeoff.** Consolidation to ~14 mechanics sacrifices some historical-texture richness (e.g., distinct Arbiter, Karō, Bugyō, Metsuke, Yoriki NPC types collapsed to Sub-Faction Actor framework loses lens-specific flavor). **Tradeoff: elegance against lens-specific richness.** Current recommendation favors elegance.

**5. T-α Authority Devolution variant parameterization.** Single unified track must express: military-emergency-grant (*zhou mu*) vs central-decay-devolution (*shugodai*) vs territorial-withdrawal-sovereignty (Hospitaller) vs multi-generation-accumulation (Sima). Parameter design open.

**6. M-3 Material-infrastructure three-component: acceptable partial states.** "Partial control = contested claim (−2 Mandate cap)" — requires specification of what happens when 1 of 3 components controlled, 2 of 3 controlled, transitional states during contest.

---
