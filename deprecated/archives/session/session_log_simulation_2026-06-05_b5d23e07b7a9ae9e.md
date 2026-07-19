session_id: simulation_b5d23e07b7a9ae9e
session_close: 2026-06-05
status: complete
last_stage: commit all — targeting extensions (3faa2b4bc8), stress harness + ledger (3778d6e6), handoff (9de15625)
next_action: PC_NODE_COHESION fix (continuous-path _node_pos coverage) or GappedLine/Horseshoe closing investigation; fetch tests/sim_verification_ledger.json → /home/claude/ before next orchestration.py commit
blockers: none active — all session work committed; PC_NODE_COHESION and shape non-closing are next-session engineering items

---

## Session 2026-06-05 — mass-battle engine validation + targeting

### Commits (this session)
- 1f9361fb  breakthrough validation NULL finding (designs/audit/)
- 8b1ec4eb  handoff — Stream B breakthrough resolved
- 3faa2b4b  targeting extensions: target_delay_ticks + target_condition (weakest/in_range:N) added to Subunit + assign_targets
- 3778d6e6  stress_random.py (randomised stress harness, designs/audit/) + sim_verification_ledger.json (tests/)
- 9de15625  handoff full-session update

### Key findings
- Engine ROBUST: 0 failures / 0 degenerate across 180+ randomised/multi-subunit/varied-location trials; mirror symmetric
- Flanking works: rear charge B HP 0.86→0.51 vs frontal; envelopment layer (facing + wrap) fires correctly
- Cavalry: 2x closing speed; frontal charge not dominant vs steady infantry; square near-immune (0/8)
- stance=retreat: pre-contact lure mechanic works; vector-halt blocks post-contact disengage (historically correct)
- PC_NODE_COHESION: crashes in continuous path (KeyError _node_advance); off by default; correctly non-functional
- Targeting built: target_delay_ticks (countdown hold), target_condition=weakest/in_range:N, order_target_idx (direct); stress-tested 0 failures; historical counters unchanged

### Open items
- PC_NODE_COHESION: fix _node_pos coverage for continuous-mode cells
- GappedLine/Horseshoe: parameter-sensitive non-closing (advance/closing for dispersed shapes)
- sim_verification_ledger.json bootstrap: future sessions must fetch tests/sim_verification_ledger.json → /home/claude/ before committing to tests/sim/mass_battle/orchestration.py
