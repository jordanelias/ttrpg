session_close: 2026-03-27
checkpoint: post-batch5-simulation
model: claude-sonnet-4-6
completed_stages:
  - BUG-004 / G-097 closed: Heart/Poise attribute names replaced across 8 compilation stages (1,3,6,8,9,10,13,16)
  - Stage17 confirmed exempt (historical audit record)
  - NPC Composure recalculated: Almud=11 (Pres 5+6), Lenneth=10 (Pres 4+6), Vaynard=11 (Pres 5+6), Himlensendt=12, Baralta=11
  - Certainty recovery rule added: Spirit TN7 Ob2, one attempt per downtime scene (stage2 §4.6 + stage3 cross-ref)
  - Stage2 §4.6 old automatic recovery (seasonal) replaced with Spirit roll model
  - Batch 5 Mode A simulation complete: M-001 through M-009 (M-005 eliminated — Maxims cut)
  - Batch 5 Mode B simulation complete: interaction chains B-02 through B-07
  - Two P1 fixes applied inline: M002-01 (Wound cap clarified in stage1), M009-01 (Certainty recovery in stage2/3)

editorial_decisions_applied:
  - Certainty recovery: Spirit TN7 Ob2 (not automatic rest-based)
  - Certainty depletion confirmed as TS-growth pressure, not pure damage
  - NPC Presence scores: Almud 5, Lenneth 4, Vaynard 5

gap_register_delta:
  closed:
    G-097: BUG-002 Heart/Poise naming — CLOSED
  added:
    G-105: Intelligibility + low Spirit = permanent Rendering Crisis loop (P1)
    G-106: Inspiration + Fork pool inflation, 20D+ uncapped (P1)
    G-107: Inspiration on Thread ops unruled (P2)
    G-108: Incapacitated character in social scene hybrid unruled (P2)
    G-109: Rendering Crisis no mechanical enforcement (P2)
    G-110: Non-combat pool floor undefined — negative pool possible (P1)
  totals_after: 143 total (3 new P1s open: G-105, G-106, G-110)

commits:
  - compilation/stage1_core_engine.md: BUG-004 (Heart ref), M002-01 Wound cap
  - compilation/stage2_characters.md: Certainty recovery rule, NPC Presence scores
  - compilation/stage3_thread_operations.md: BUG-004 (Heart), Certainty recovery cross-ref
  - compilation/stage6_factions.md: BUG-004
  - compilation/stage8_combat.md: BUG-004
  - compilation/stage9_social.md: BUG-004
  - compilation/stage10_advancement.md: BUG-004
  - compilation/stage13_npcs.md: BUG-004, NPC Composure values
  - compilation/stage16_reference.md: BUG-004
  - tests/valoria_stress_tests_batch5.md: Mode A results
  - tests/valoria_stress_tests_batch5_modeB.md: Mode B results
  - valoria_gap_register_consolidated.md: G-097 closed, G-105-G-110 added

open_p1s:
  - G-105: Intelligibility → permanent Certainty max reduction loop
  - G-106: Inspiration + Fork pool ceiling (max 1 Inspiration/roll, max 2 Forks/roll)
  - G-110: Minimum 1D pool floor for all non-combat rolls

editorial_still_pending:
  - B03-02: Stunt auto-success cap — Inspiration value or full attribute? (EDITORIAL)
  - S-08 Einhir site name
  - E-01 assassination perpetrator
  - Vaynard Private Collection transfer procedure
  - Niflhel primus inter pares structure
  - Restoration NPCs
  - Territory names (15 territories)

next_action:
  options:
    a: Apply 3 open P1 text fixes (G-105 Intelligibility note, G-106 Inspiration/Fork cap, G-110 pool floor minimum)
    b: Resolve B03-02 editorial (Stunt auto-success cap) then apply all text fixes together
    c: Continue simulation — Batch 6 (remaining untested mechanics)
  priority: B — resolve editorial first, then batch all text fixes in one push; then Batch 6
  untested_mechanics_remaining: History Resonance, Certainty blast radius, Diagnosis standalone, Co-Movement Cards (BG), Impression Track, Reading Exchange, Defection, Fortification, BG turn structure, Victory conditions, Hollow victory, plus M-010 through M-056 (all Thread + faction + combat specifics)
