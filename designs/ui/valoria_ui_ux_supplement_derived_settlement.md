# UI/UX Integration Supplement — Derived Stats + Settlement Map
# Phase 2.10 (AUD-UI-01/02)
# Date: 2026-04-18
# Integrates into: designs/ui/valoria_ui_ux_v4_1.md Part 3 and Part 11

---

## Part 11 Supplement: Derived Stats Display (AUD-UI-01)

Per derived_stats_v30 §3.3, the faction overview displays:

```
FACTION OVERVIEW (Part 11.x)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mandate ████████░░ 5      Legitimacy: 87/100  [▲ +5/season]
Wealth  ██████░░░░ 4      Treasury:  340/400  [▼ −60/season net]
Military ████████░░ 5     Levies: 7/10 fielded
Influence █████████░ 5    Reputation: 62/75   [▲ +5/season]
Stability ████████░░ 4    Cohesion: 35/40     [▲ +10/season]
```

### Implementation Notes (Godot)

**Stat bars:** 7-segment bar (1 segment per stat point). Current stat filled, max 7. Color: faction-specific.
**Resource numbers:** Derived value / maximum. Net income/drain shown as [▲/▼ ±N/season]. Green = positive, red = negative.
**Income/drain breakdown on hover:** Tooltip showing all income sources and drain sources for the hovered derived value. Example:
```
Treasury: 340/400 gold
  Income:
    Prosperity income: +210/season (13 settlements)
    Haushalt bonus: +50/season (Competence 2)
  Drain:
    Unit upkeep: −50/season (2 professional)
    Campaign Supply: −100/season (1 army hostile)
  Net: −60/season → Treasury 0 in ~6 seasons
```

**Levies Available:** Not a bar — shows "X/Y fielded" where Y = Military × 2. If over cap after Military drop, show in red with "DISBAND REQUIRED" indicator.

---

## Part 3 Supplement: Settlement Map (AUD-UI-02)

Province-level zoom replaces flat territory view with settlement node graph.

### Settlement Node Display

Each settlement node shows:
- **Type icon:** Seat (crown), City (tower), Town (house), Fortress (shield), Cathedral (cross), Port (anchor), Mine (pickaxe), Outpost (flag)
- **3 stat bars:** P/D/O as small horizontal bars (0-5 scale, color-coded: green/blue/yellow)
- **Governor name:** Small text below node
- **Church infrastructure:** 4 small icons (Religious Building, Templar, Inquisitor, Governor) — filled if present, outline if absent

### Interaction

- **Click settlement:** Opens settlement detail panel
- **Detail panel shows:** Full stats, derived values (Local Economy, Garrison Strength, Public Order), facility slots, governor, Church infrastructure axes, available governance actions
- **Province Accord:** Displayed at province level above the settlement graph as "Province Accord: N (derived from settlement Order)"

### Godot Implementation

- **Scene:** SettlementMapView extends ProvinceView
- **Nodes:** PackedScene per settlement type with dynamic stat bar TextureProgress
- **Data:** settlement_data.tres (36 entries, per Phase 5.3 schema)
- **Transitions:** Click province on peninsula map → zoom to SettlementMapView → click settlement → detail panel overlay
