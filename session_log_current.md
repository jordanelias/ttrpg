session_id: 2026-03-29T_COMBAT_SIMULATION
phase: Combat System Design — complete
status: CLOSED

## SESSION SUMMARY

### Completed
- Full combat system redesigned and simulated from scratch
- Binary weapon system confirmed: Light/Heavy × Cut/Blunt × Short/Long
- TN gradient: LightCut 5/6, HeavyCut+LightBlunt 6/7, HeavyBlunt 7/8
- Versatile weapon category removed
- Establish Distance: TN7 vs opponent offence successes; auto-succeeds if opponent not attacking
- Feint vs Establish Distance: direct contest (feint TN-1 vs TN7), tie goes to feint
- Initiative: structural (correct range) > hit-and-not-hit > Agi Ob2 roll
- Disarm: offence vs defence; retrieve on TN7 vs opponent offence successes
- Stamina system: OOB + Full Guard both give opponent +2D
- Critical hits: excess >= 3, weapon modifier doubled
- Mass mismatch penalty: -1 defensive success when Light splits vs Heavy (not Full Guard, not Long-at-Close)
- Wound system: Variant B selected — HP=End (flat), armour=DR per weapon type
- DR table: varies by weapon type vs armour tier (LightCut/HeavyCut/LightBlunt/HeavyBlunt)
- Long weapons at Close zone: -1D offence, half damage, type unchanged
- Group combat: zone collapse (first closer opens zone for allies) + Fibonacci bonus
- Historical manual analysis: Fiore, Silver, Liechtenauer, Talhoffer, Meyer
- Simulation: 400+ matchups, 2000 fights each, randomised character parameters
- Key finding: offence% has near-zero correlation with winning (r≈0.01)
- Heavy weapons confirmed as situationally powerful — correct in armoured and group contexts

### Files pushed
- compilation/valoria_combat.docx — complete combat system write-up

### Simulation files (local /home/claude/)
- combat_v6.py through combat_v11.py — progressive rule iterations
- combat_v8_matrix.py — full weapon×armour matrix

### Key decisions
- No versatile weapons
- No medium weapon category
- Cut/Blunt as primary damage type axis (not weight alone)
- STR stays in damage formula
- No bind mechanic (too granular)
- No cutting/blunt TN split beyond weight
- Puncture not a separate axis
- Heavy weapons situationally powerful, not generally dominant

### Resume instruction
Combat system complete and compiled. Next: group combat simulation (Fibonacci + zone
collapse together), then push combat mechanics into main compilation checkpoint.
Pending user actions 0.19-0.22 from Phase 0 still outstanding.
