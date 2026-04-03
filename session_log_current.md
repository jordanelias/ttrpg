# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_RANGED_WEAPONS_PROPAGATION
phase: Phase 14 — Ranged weapon type propagation and simulation complete
status: CLOSED

completed:
  - PP-172: personal combat ranged subtypes (LP/HP/LBl/HBl), TN8 defence, environmental factors, HBl STR min
  - PP-173: mass combat ranged DR table split (Projectile → 4 columns), HBl personal distinction, LBl anti-levy note
  - PP-174: params_combat stale HBl note removed; Damage Formula STR inconsistency provisional (ED-092)
  - PP-175: mass combat ranged DR scaled ÷2 from personal DR (provisional ED-096) — P1 fix
  - SIM-001: personal combat ranged test battles (6 scenarios)
  - SIM-002/003: mass combat and BG ranged scenarios
  - SIM-004: full personal combat test suite (Mode A/C/D/J)
  - SIM-005/006: full mass combat and BG battle scenarios
  - Commits: d30e47b (PP-172), 8ea42f3 (PP-173), c397de0 (PP-174), a496722 (PP-175)

patches_applied:
  - PP-172 through PP-175 (4 patches)

editorial_status:
  open_provisional: 84+ (prior) + ED-085/086/087/092/093/094/095/096 = 92+
  new_this_session: ED-085, ED-086, ED-087, ED-092, ED-093, ED-094, ED-095, ED-096

key_provisional_decisions:
  ED-085: Ranged pool split at melee range — Offence forbidden, Defence only at TN8
  ED-086: HBl availability by faction — provisional: all factions
  ED-092: STR in damage formula — provisional: STR is wield-requirement only, not damage addition
  ED-093: Fibonacci group bonus for ranged — provisional: does not apply
  ED-094: HP reload at mass combat scale — provisional: no reload (unit staggers)
  ED-095: Ranged units in Engagement weapon — provisional: Light Cut sidearm
  ED-096: Mass combat ranged DR scaling — provisional: ÷2 rounded up

outstanding_propagation:
  - ED-092: if confirmed STR is not in damage, update combat_design_v1.md formula text
  - ED-093: if confirmed no Fibonacci for ranged, add explicit rule to combat_design_v1.md §8
  - ED-094/095: add HP reload note and Engagement weapon note to mass_battle_v3.md §Phase 2/5
  - ED-096: confirm ÷2 scaling before treating PP-175 as final

sim_debt:
  - SIM-DEBT-01: Debate pool re-calibration (unchanged — not ranged related)
  - No new SIM-DEBT items

next_actions:
  1. User reviews ED-085/086/092/093/094/095/096 provisional decisions
  2. If confirmed: propagate as non-provisional patches to design docs
  3. Mass combat ranged unit roster update (faction unit blocks need ranged subtypes)
  4. Consider: ranged unit availability and cost differentiation by faction
```
