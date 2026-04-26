---
atom_id: valoria_session_master_2026-04-25__02__context-window-2-session-b-secondary-session-c
source_file: valoria_session_master_2026-04-25.md
source_section: "Context Window 2 — Session B Secondary + Session C"
section_index: 2
total_sections: 5
line_count: 39
char_count: 2523
source_sha256: 8b5f5049f7c1710a
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## Context Window 2 — Session B Secondary + Session C

### Session B Secondary Propagation

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 7 | `6e952c3` | designs/architecture/conflict_architecture_proposal.md, params/bg/victory.md, designs/provincial/baralta_crown_claim_v30.md, references/canonical_sources.yaml | conflict_architecture_proposal PROPOSAL → CANON. Coup → Autonomy in victory + baralta_crown_claim |
| 8 | `3cfa81f` | designs/npcs/npc_roster_v30.md, params/bg/npcs_special.md, references/canonical_sources.yaml | Dalla Virke → independent intelligence broker. npcs_special Niflhel → settlement-level refs |

### Session C — Tensions Deck + Royal Assassination

**Tensions Deck** — 6 cards, draw 1 at game start. Each amplifies one faction-friction point and triggers an S8+ event if not averted.

| # | Card | Amplifies | S8+ Event |
|---|------|-----------|-----------|
| 1 | Royal Crisis | Crown-Church friction + succession | Royal family member assassinated (sub-roll for target) |
| 2 | Feldmark Famine | Crown breadbasket | Prosperity collapse in Crown food supply |
| 3 | Cardinal Independence | Church internal | Rogue Cardinal appoints bishop-governor unilaterally |
| 4 | Guild Fracture | Hafenmark-Guild friction | S017 Guild schism, Market Quarter contested |
| 5 | Einhir Incident | Varfell-RM friction | Public cultural confrontation, all factions declare position |
| 6 | Ministry Crisis | Crown-Löwenritter + governance | Ministry bureaucracy collapses, Church fills vacuum |

**Fuse model:** Visible from S1 (NPC dialogue, atmospheric events). Player can investigate S1–S7. Event fires S8–S12 if not averted.

**Royal Assassination Fuse** — fires on Royal Crisis card.

| Roll | Target | Consequence Arc |
|------|--------|-----------------|
| 1–2 | Lenneth | Almud revenge arc — Crown governance suffers, investigation opens |
| 3–4 | Torben | Elske retrieval — military deployment to Varfell territory, Altonian crisis |
| 5–6 | Almud | Lenneth takes throne — Crown identity inverts (pro-Einhir, pro-Thread-research) |

| Commit | SHA | Files Modified | What |
|--------|-----|----------------|------|
| 9 | `d29d8b6` | params/bg/tensions_deck.md (NEW), params/bg/royal_assassination.md (NEW), references/canonical_sources.yaml | Standalone params files for both specs |
| 10 | `238cf45` | params/bg/phases.md, references/canonical_sources.yaml | Game Setup section: Tensions Deck draw, starting settlements, assassination target determination |

---
