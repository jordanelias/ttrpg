session_id: 2026-03-29T_COMBAT_GROUP_SIM
phase: Combat Group Simulation — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Group combat simulation: Fibonacci + zone collapse (sim_combat_group.py)
- Rescue / multi-engagement simulation (sim_combat_rescue.py)
- Tie Up / bind exhaustive proposition testing (sim_combat_tieup.py)
- Exhaustive group combat matrix (sim_combat_exhaustive.py)
- v11 single combat sim with mass mismatch penalty (sim_combat_v11.py)

### Key findings
- 3v1 universally decisive (99-100%) regardless of weapon/armour
- 2v1 is the tactically interesting zone — weapon type and armour matter
- LightCut vs Heavy armour at 2v1: only 56% attacker win (contested)
- HeavyBlunt is correct weapon for armoured targets at any numerical parity
- 3v2 produces 40-87% draw rate — parallel engagements resolve simultaneously
- Survival/rescue window: 2-3 rounds (after round 3, 75-80% of losers have fallen)
- HeavyCut dominates 1v1 (75% vs LightCut); HeavyBlunt is armoured specialist
- Tie Up mechanic not needed — Option A accepted (system correct without it)
- Mass battle abstraction confirmed: Fibonacci → flanking modifier,
  zone collapse → formation break, rescue → reserve timing,
  weapon type → unit specialisation, DR → unit armour rating

### Files pushed
- tests/sim_combat_group.py
- tests/sim_combat_rescue.py
- tests/sim_combat_tieup.py
- tests/sim_combat_exhaustive.py
- tests/sim_combat_v11.py
- compilation/valoria_combat.docx (previous session)

### Design notes logged
- Mass battle abstraction: 5 unit stats + 2 rolls per engagement
- Heavy armoured elite unit holds 2v1 vs wrong weapon type (56%)
- Requires 3v1 or correct weapon (HeavyBlunt) to break reliably
- Reserve timing critical: 2 battle turns = rescue window

### Resume instruction
Combat system fully simulated and validated. Next:
- Integrate group combat mechanics into valoria_combat.docx
- Design mass battle unit stat block (weapon type, armour tier,
  pool/cohesion, DR, Fibonacci modifier)
- Phase 0 user actions 0.19-0.22 still pending
