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

## PP-188 (2026-04-02) — Ranged Category Redesign (ED-061 resolved)
Source: user editorial decision
Changes:
- Weapon table: LP/HP/LBl/HBl → Piercing (Bow/Crossbow) and Blunt (Throw/Sling)
- Bow: TN6, +2 mod, every round
- Crossbow: TN5, +2 base mod, every other round; post-DR +2 vs Med / +3 vs Heavy (if hit)
- Throwing weapon: TN7, +1 mod, every round
- Sling: TN8, −2D pool, every other round; Clay+1/Stone+2/Metal+3/Lead+4
- DR table: collapsed to 2 columns (Piercing: 0/2/3/5; Blunt: 0/1/2/3)
- Cover table: collapsed to 2 columns
- Fibonacci group bonus: removed for all ranged weapons

## PP-254 (2026-04-04) — Stamina Exhaustion Propagation + Health Formula Conflict (GAP-SIM-X26-01)
Source: combat_design_v1.md §7 (canonical)
Changes:
- Added Stamina Exhaustion rule: Stamina 0 = Out of Breath (−2D all combat), recovery via Take a Breath action
- Struck PP-232 Health formula (Endurance+6)×(wound count+1) — conflicts with design doc
- Confirmed Health = Endurance+6 per §7; at 0 Health take 1 Wound, Health resets to full
- Flagged ED-152: Health formula contradiction PP-232 vs design doc §7 — design doc wins
- Version: v0.14-AUD5-R1 → v0.14-AUD5-R2

## PP-255 (2026-04-04) — Momentum Between-Scene Carry + RS Baseline Decay (GAP-SIM-X26-02, GAP-SIM-X27-01)
Source: bg_v05 Part Seven precedent analysis (RS decay); design intent (Momentum)
Changes:
- Momentum: confirmed reset at session start (not scene start); between-scene carry within session now explicit
- RS baseline decay: −1/year (per 4-season year) confirmed from bg_v05 Part Seven HIS comparison
- Propagated to params_core.md and params_factions.md
- Version: v0.14-AUD1-R1 → v0.14-AUD1-R2

## PP-303 (2026-04-04) — Memory Re-Citation Restriction (GAP-SIM-X29-01)
Source: SIM-X-34 exploit test
Changes:
- Memory bonus (+2D): same named source once per debate only
- Re-citation of same source: no bonus
- Opponent challenge rule added (Step 1 Appraise Ob 2)

## PP-304 (2026-04-04) — Critical Hit Overflow, Weapon Draw, Partial Ob Stack Reset
Source: SIM-X-33 (overflow), SIM-X-34 (stack), GAP-SIM-X33-01/02, GAP-SIM-X30-02/03
Changes:
- Critical Hit overflow: multiple wounds possible from single hit (each Health-track reset counts as 1 wound)
- Ready sidearm draw: free action at round start
- Partial Op Ob stack: resets on success of same type or scene end; system cap 20
- Partial Weaving: no RS change (provisional)
- Partial Leap: establishes contact with Op Ob +1; Failure = no contact
