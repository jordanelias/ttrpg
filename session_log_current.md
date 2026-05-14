session_id: 2026-05-13_v16_continuous_troop_count
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v16-committed-55952ac_continuous_effective_size_lethality_recal
next_action:
  skill: valoria-simulator
  task: v17 — multi-turn battle orchestrator; LETHALITY_SCALE fine-tuning; per-unit grid architecture; pursuit/cascade mechanics
blockers: []
commits: [651bf7dd3308a808b155afde3511677a8cc649f3, 55952ac6f7078ce2af37c7328337b678ce5a7972]
notes: |
  ## Session summary

  Two commits this session:

  v15 (651bf7d) — G-1 stamina + G-2 rout on phase-boundary hooks.
    Stamina: drain 16/contact-tick, recovery 8/reserve-rank. Pool penalty -1 at exhaustion.
    Battery 11/13 in-band. H5 RF-vs-HS fixed (47.4->50.2%).

  v16 (55952ac) — G-3 continuous effective_size + lethality recalibration.
    Architectural: effective_size as float (not floored). Pool degrades continuously.
    LETHALITY_SCALE=0.10 for ~15% casualties per 3-phase engagement turn.
    max_turns=18 (3-phase cap per engagement turn).
    Casualty-pct morale triggers at 30%/50% replace integer Size triggers.
    Multi-turn validation: rout at ~33% cumulative after 2 turns. 100% rout rate.

  ## Design clarifications from Jordan

  Battle architecture (4 zoom levels):
    1. Peninsula — faction-level grand strategy
    2. Territory — terrain, armies, battle turns (5-8 per battle)
    3. Battlefield — 25x21 grid PER UNIT, 3-phase cap per engagement turn
    4. Scene — duels, thread, personal encounters

  Key constraints:
    - Time is absolute — no different tick durations per unit type
    - 3-phase cap per engagement turn, not per battle
    - Adjacent allies at one depth join (2v1, 2v2, 3v1)
    - Auto-resolve available
    - 30% rout threshold (gameplay, not historical 10-15%)

  ## Throughline/NERS assessment (pre-commit)

  T1 Generalship dominates — strongest throughline, one formula carries it
  T2 Cascading degradation — now producing its dynamic with v16 lethality
  T3 Combined arms — well-served by existing mechanics
  T5 Battles have systemic weight — differentiator from Total War
  M1 General IS the army — meta-throughline
  M3 Strategic composition > tactical execution — strongest for videogame

  NERS verdict: sound at conception level, over-specified at resolution level.
  Weapon effectiveness matrix (48 entries) should collapse to 9-12.
  Morale trigger list should reduce to 4-5.
  Phase structure could simplify (5 phases not 7).

  ## Gap register

  G-1 stamina: IMPLEMENTED (v15)
  G-2 rout-at-threshold: IMPLEMENTED (v15+v16)
  G-3 lethality recal: IMPLEMENTED (v16)
  G-3b multi-turn orchestrator: NOT YET — needs proper state persistence across turns
  Per-unit grid (25x21): NOT YET — sim uses shared grid
  Multi-unit engagement (2v1 etc): NOT YET
  Pursuit damage after rout: NOT YET
  Rout cascade to adjacent units: NOT YET
  H7 GL regression: still present, structural
  Winner/loser casualty ratio 1.4x vs historical 2-5x: needs pursuit/cascade
