# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_RANGED_PROPAGATION
phase: Phase 14 — Ranged weapon type propagation and simulation
status: CLOSED

completed:
  - PP-172: ranged subtypes (LP/HP/LBl/HBl) in personal combat, TN8 defence, environmental factors
  - PP-173: mass combat ranged DR split (Projectile column → 4 columns), HBl personal reference updated
  - SIM-001: personal combat ranged test battles (committed d30e47b)
  - SIM-002/003: mass combat + BG ranged scenarios (committed 40f54e0)
  - SIM-004/005/006: TTRPG personal, mass combat, hybrid siege scenarios (committed 3856ab8)
  - ED-097: HP mass combat reload abstraction (provisional: no CP penalty)
  - ED-098: cover declaration timing (provisional: Phase 1 required, GM arbitrates)
  - Propagation complete for personal combat and mass combat
  - BG confirmed: no changes needed (correctly abstracted)

commits:
  - d30e47b: PP-172 personal combat ranged subtypes
  - 40f54e0: PP-173 mass combat ranged DR split
  - 3856ab8: SIM-004/005/006 scenarios + ED-097/098

design_decisions:
  - HP crossbow penetrates all armour tiers at personal scale (historically accurate)
  - Balance mechanism is zone control and terrain, NOT damage numbers
  - HBl (lead sling) = anti-armour ranged; HBl (Artillery) = siege unit — distinct
  - LBl (stone sling) = anti-levy only at mass combat scale
  - Mass combat HP units zero damage vs Heavy armour at standard CP (correct abstraction)
  - Personal HBl (16D Agility 5) = viable anti-artillery sniper in Hybrid mode

open_editorials:
  - ED-085: pool split at melee range for ranged (provisional: Offence forbidden)
  - ED-086: HBl lead sling availability by faction (provisional: all factions)
  - ED-087: BG ranged-specialist faction modifier (provisional: none)
  - ED-097: HP mass combat reload CP penalty (provisional: none)
  - ED-098: cover declaration timing (provisional: Phase 1, GM arbitrates) → propagated to combat_design_v1 v1.3

pending_propagation:
  - None. All propagation complete.
  - BG: no changes needed (confirmed SIM-003)

next_session:
  - Ranged system is fully propagated and tested
  - Propagation map updated, no broken dependencies introduced
  - Available for any subsequent work
```
