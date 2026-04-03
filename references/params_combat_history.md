# params_combat — Patch History
## Container: references/params_combat.md
## Auto-maintained — appended by valoria-orchestrator on patch application
## Do not read this file in simulations — it is history, not values

---

## PATCH SUMMARY (PP-086–092, applied 2026-04-02)

### PP-086 — Mass Combat Base Damage
Damage = max(0, net_successes_over_Ob + disposition_modifier)
Disposition modifiers: Offensive +2 flat, Defensive +4 flat (add to base).

### PP-087 — Formation Break Ob Stacking
+1 Ob per break, cumulative, persists through rally. Cap: 3 breaks = Dispersed (permanent rout).
All attachments lost on any Formation Break.

### PP-088 — Siege Assault Linkage
Mass combat win during declared Assault = Fortification −1.
Overwhelming win = Fortification −2.
Field victory ≠ breach — must declare Assault next season.

### PP-091 — Artillery Bombard
Roll Artillery CP vs Ob (Short=1, Med=2, Long=3). No melee exchange.
Success = flat 1 Str damage. Overwhelming = flat 2.
Cannot Bombard at melee range.

### PP-092 — Personal Combat Clarifications (P2-B11 series)
- Defence split: defender allocates blind before any attacker declares
- "Same range" = shorter weapon at Close zone = Short range achieved
- Stunt + chain die: both effects independent, apply simultaneously
- Tie Up: blocks escape for one round only
- Rescue fails with no incoming attack (action lost)
- Incapacitation: complete resolving action, fall at end of that priority step
- Commander in personal combat: cannot also Rally/order same round
- Routed units hold position during scene resolution

## PENDING EDITORIALS AFFECTING THESE PARAMS
- ED-033: Commander bonus formula (three conflicting formulas — BG/TTRPG/Hybrid)
- ED-037: Volley TN 6 vs TN 7 (mass combat)
- ED-038: Coherence stat definition in mass battle
- ED-040: Artillery Balanced disposition lock (intentional?)

## PP-172 (2026-04-02) — Ranged Weapon Subtypes
Source: SIM-001
Changes:
- Weapon table: replaced single 'Projectile' row with LP/HP/LBl/HBl rows (distinct TN/mod/Def TN)
- Def TN: ranged weapons now defend at TN8 at Close zone (full pool to Defence, no Offence split)
- Armour table: added Ranged DR table (4 types × 4 armour tiers)
- Environmental factors: terrain table added (rounds to close + penalties)
- Cover table: added type-specific DR by ranged weapon type
- STR minimum: HBl requires STR 2 (new)
- Reload: LP/LBl/HBl fire every round; HP requires Reload action (unchanged from PP-105)
Editorials raised: ED-085 (pool split ruling), ED-086 (HBl availability)
Propagation pending: mass_battle_v3.md, params_mass_combat.md, bg_v05

## PP-174 (2026-04-02) — Stale HBl Note + Damage Formula Fix
Source: SIM-004
Changes:
- Removed stale "No personal HBl" line (contradicted PP-172)
- Replaced with HBl personal vs siege distinction paragraph
- Damage Formula updated: removed STR, added ED-092 provisional note
- Version: v0.14-AUD3 → v0.14-AUD4
