# VALORIA — FIELDWORK SYSTEM v1.1 — §8 Board Game Mode
## Parent: designs/fieldwork/fieldwork_design_v1.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: Board Game / Hybrid

## §8 BOARD GAME MODE

At Board Game scale, fieldwork is abstracted into faction-level actions using existing card types plus one new action variant.

### §8.1 New BG Action: Survey (Consul Inward variant)

**Survey** represents a faction directing resources to explore and develop a territory's hidden assets.

- **Card type:** Consul Inward (uses existing card slot — no new card type required).
- **Pool:** Influence.
- **Ob:** (5 − Proximity Rating) + 1. Minimum 1. Askeheim (Proximity 0) → Ob 6. Lowenskyst (Proximity 5) → Ob 1. Territories closer to the Calamity epicentre are harder to survey safely.
- **Effect on Success:** Reveal one undiscovered POI in the territory. POI provides a territory-level bonus:

| POI Category | BG Bonus |
|-------------|----------|
| Resource | Prosperity +1 in this territory |
| Secret | +1D on next military or intelligence action in this territory |
| Remnant | Thread operation Ob −1 in this territory for 2 seasons; Thread Debt token placed |
| Anomaly | RS −1 at this territory immediately; Warden Cooperation +1 eligible (if Warden Emergence active) |

- **Effect on Overwhelming:** Reveal POI + gain +1 Influence (the discovery enhances the faction's knowledge base).
- **Effect on Failure:** No POI found. +1 Church Attention Pool in this territory if the survey targeted Depth ≥ 3 content.

### §8.2 Existing Actions as Fieldwork

| Fieldwork Activity | BG Action | Already Defined | Notes |
|-------------------|-----------|-----------------|-------|
| Investigation (intelligence) | Tribune Investigate | params_board_game.md §Standard Action Ob | Ob 2. Reveals faction stats. |
| Investigation (espionage) | Tribune Spy | params_board_game.md §Standard Action Ob | Ob = floor(target Intel/2) + 1. |
| Socializing (diplomacy) | Senator Diplomacy | params_board_game.md §Standard Action Ob | Ob = floor(target Stability/2) + 1. |
| Socializing (public) | Senator Decree | Already defined | Disposition shift at faction scale. |
| Exploration (governance) | Consul Govern | Already defined | Prosperity development = territory-level exploration. |
| Thread exploration | Thread Operation | Already defined | Pontifex/Weaver card. |

**No new card types.** Survey uses Consul Inward. All other fieldwork maps to existing actions. This preserves the BG action economy.

### §8.3 BG Social Interaction

At BG scale, inter-faction relationships are modelled by existing mechanics: Senator Diplomacy (Ob = floor(target Stability/2) + 1) and Standing/Reputation tracks (0-5 each, per clock_registry.md). Disposition is a personal-scale track that does not apply at faction scale. Player-to-player faction relationships are negotiated, not rolled. NPC faction behaviour is governed by NPC artificial intelligence rules in bg_v05.

---

