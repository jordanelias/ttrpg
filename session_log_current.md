# Valoria Session Log - Current

> Resuming instance: read ONLY this file. Archive is in session_log_archive.md.

---

session_close: 2026-03-26-batch2
phase: 3
status: Phase 3 Batch 2 stress tests complete

completed_this_session:
  - 15 stress tests executed (T11-T18 TTRPG, B11-B14 Board, H11-H13 Hybrid)
  - 20 rulings produced and logged
  - All 8 factions covered as active faction
  - 6 named NPCs tested as Primary Actor (Almud, Himlensendt, Baralta, Vaynard, Lenneth, Ehrenwall)
  - 5 new archetypes covered (Inquisitor, Riskbreaker, Löwenritter Knight, Non-TS Scholar, Knight Templar)
  - 22 mechanics newly in progress or completed (see batch2 coverage matrix)

commits:
  - tests/valoria_stress_tests_batch2.md: 2b4ee7b8
  - tests/auditing_matrix.md (updated): b3c549ff

rulings_locked:
  - R-T11-A: CE threshold fires once at CE 3; no retrigger above 3
  - R-T11-B: Doubling Down = +1D to Cognition investigation rolls (needs codification in ruleset)
  - R-T12-A: DD +1 Ob stacks with ethical framework Ob penalties
  - R-T12-B: Parliamentary Inquiry pool = highest-Mandate faction + 2D
  - R-T14-A: Resonant Style tag grants +1D to attacker per exchange
  - R-T15-A: Scholarly TS growers use Ob 1 (not Ob 2) for CE-triggered growth checks
  - R-T16-A: Scholarly arc to TS30 via Einhir texts qualifies as practitioner-adjacent for Approach Training
  - R-T17-A: Resources at 0D = rebuild via 1 season downtime -> 1D base
  - R-T18-A: Muster Ob = 2 standard; Ob 1 special property; Ob 3 contested
  - R-T18-B: Unit damage = net successes - defender Cohesion (minimum 0)
  - R-T18-C: Unit at End 0 Formation Break = Ob 3 check; second break = destroyed
  - R-B11-A: Stat cap (1-7) applied before seasonal cap (+-2)
  - R-B12-A: Factions without Intel stat cannot counter-intel in board game mode
  - R-B13-A: Siege uses faction Military for domain actions; unit Martial for unit actions
  - R-B14-A: Casus belli = Parliamentary Vote (3 exchanges); success/failure Mandate/Stability +-1
  - R-H11-A: Legal personal action creates Disputed territory status; Govern race in next Strategic Phase
  - R-H12-A: Renown removes access barriers only; does not modify any roll
  - R-H13-A: Templar CE3 Spirit TN7 Ob2; success = Certainty -1 + Unprocessed mark
  - R-H13-B: 3 Unprocessed marks = automatic Fractured trajectory

patch_executable:
  - S5.1 Approach Training: add scholarly-arc-to-30 as witness-requirement equivalent (minor drafting fix; no editorial gate)

editorial_pending:
  - TK 4-5 definitions (R-T15-B): TK4 = public articulation (TC+1); TK5 = knowledge breakthrough (TC+2, ally access)
  - Renown permission table tiers 1-4, 6-10 (only tier 5 confirmed)
  - All items carried from prior session (see prior session_log_archive.md entry)

next_action:
  recommended: Apply §5.1 patch (Haiku-tier) then continue Phase 3 Batch 3
  batch3_priorities:
    - NPC arcs not yet tested as Primary Actor: Klapp, Elske, Torben, Maret Uln, Olafsson
    - Mechanics not yet covered: M-33 Impression Track, M-53 Defection, M-60 full war arc
    - Renown tier coverage (1-4, 6-10) pending editorial permission table
    - Casus belli through to combat deployment (B14 tested vote only)
  model: Sonnet 4.6
  input_files:
    - tests/valoria_stress_tests_batch2.md (reference for rulings)
    - valoria_ruleset_checkpoint_14.md (working ruleset)
    - tests/auditing_matrix.md (coverage tracking)

model_routing_notes: Sonnet 4.6 throughout (Phase 3 simulation). §5.1 patch = Haiku-tier.
