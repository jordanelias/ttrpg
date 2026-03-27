session_close: 2026-03-27
checkpoint: 14-batch5
model: claude-sonnet-4-6
completed_stages:
  - Batch 5 simulation: M-01 through M-09 (core combat engine)
  - Modes: A isolation, B interaction, D edge cases
  - 9 mechanics tested, 11 findings total

commits:
  batch5: 542821d91a00

findings_summary:
  P1: 1
    - B5-M07-A: §1.9 and §8.1 group bonus tables contradict at 3+ attackers — §8.1 must be removed
  P2: 7
    - B5-M03-A: Stamina "in a row" qualifier allows infinite reset exploit — remove qualifier
    - B5-M04-C: Projectile range closing Ob undefined — add Agility check
    - B5-M07-C: Single ally nullifies all group bonuses (all-or-nothing) — reduce by one tier per ally
    - B5-M08-B: Beginner's Luck "first mark" on unestablished History undefined
    - B5-B02-B: Defence splitting across 3+ attackers needs explicit declaration rule
    - B5-D01: No combat escape / Flee procedure defined
    - B5-D03: Mutual full-guard stalemate has no mechanical escape — add Stamina fatigue for consecutive full guard
  P3: 3
    - B5-M03-C: Catch Breath timing unspecified
    - B5-M05-B: Thread contact across zone transitions not stated
    - B5-M06-B: Late entrants to combat have no insertion rule

passes:
  - Pool split dynamics (M-01): lethal exchange, initiative advantage, full-guard all correct
  - Wound gate system (M-02): cascade math, carryover, cap all clean
  - Zone movement (M-05): narrative design correct
  - Momentum (M-09): Thread exclusion, spend math clean

mechanics_now_tested: 9 (M-01 through M-09) + all prior batches
remaining_untested: ~21 (down from 30)

next_action:
  task: Apply P1 fix (§8.1 group bonus table removal) and P2 fixes to CP14 + stage8_combat.md
  model: Sonnet 4.6 (mechanical judgment on wording)
  then: Batch 6 — social mechanics (M-38 through M-41) or History Resonance / Certainty blast radius
