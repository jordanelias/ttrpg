# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_PP104_PROJECTILE_AND_PARAMS
phase: Phase 11b — PP-104 (projectile categories + params gap resolution)
status: CLOSED

completed:
  - PP-104 applied. Commit: 19a5c30
  - Str corrections: all units −2, Ranged/Artillery −3 (user audit)
  - Projectile single category → 4 categories:
      LP: Light Pierce (arrows) — ✓ vs None/Light, ✗ vs Medium/Heavy
      HP: Heavy Pierce (bolts) — ✓✓ vs None/Light, ✓ vs Medium, ✗ vs Heavy
      LBl: Light Blunt (sling) — ✓ vs None, ✗ vs armoured
      HBl: Heavy Blunt Siege — ✓✓ vs all (= HeavyBlunt at range)
  - DR table expanded: 4 projectile DR columns added to mass combat table
  - Ranged unit weapon: Projectile → LP (arrows, default)
  - Artillery unit weapon: HeavyBlunt → HBl (siege, ranged)
  - PARAMS-GAP-04 resolved: pool split declared Phase 1, default equal
  - PARAMS-GAP-05 resolved: Str loss = max(0, net hits + Dmg Mod − DR)
  - PARAMS-GAP-06-MC resolved: BG Battle Partial (margin ≤1, Attacker Stability −1)
  - Reference card v1.1: Str/weapon corrections applied
  - mass_battle_v3.md → v4.3
  - params_mass_combat.md → ST5

editorial_items_added:
  - ED-061: Confirm 4 projectile categories and DR values; consider Ranged sub-types
  - ED-062: Confirm unit Dmg Mod values and Morale starting values
  - ED-063: Confirm BG Battle Partial threshold (margin ≤1) and Stability cost

all_provisional:
  - DR values for LP/HP/LBl/HBl (ED-061)
  - Unit Dmg Mod column (ED-062)
  - Unit Morale starting values (ED-062)
  - BG Battle Partial outcome (ED-063)
  - Pool split default (no editorial blocker — mechanically defensible)
  - Damage formula (no editorial blocker — derived from existing Phase 5 formula)

open_from_prior:
  - ED-056: Zoom In TC win-delay exploit
  - ED-058: Debate stalemate forced resolution
  - ED-059: RS=0 at Zoom In gap-rule priority
  - ED-060: Composure restoration between scenes
  - ED-061–063: New from PP-104 (all P2, non-blocking)

next_action:
  task: "Resolve ED-061/062/063 via editorial (confirm projectile categories, Dmg Mod, Partial threshold) or proceed to next simulation target. Hybrid and mass combat mechanics now have a complete provisional parameter set."
  note: "No P1 blockers open. All hybrid simulation gaps resolved provisionally. Design is simulatable end-to-end."
```
