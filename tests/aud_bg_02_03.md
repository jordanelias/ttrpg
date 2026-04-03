# AUD-BG-02 + AUD-BG-03 + SIM-BG-02/03/04 — BG Audit and Stress Tests
## Date: 2026-04-02
## Status: COMPLETE

### AUD-BG-02: Audit Without Thread Operations
P2 findings:
- A2-01: Guilds Wealth cap hit S1 (NPC). No Guild Wealth sink. Design note.
- A2-02: Church Season 1 Excommunication near-impossible vs full Crown (Ob 4, P=9%). Correct by design.
- A2-03 (P2→PP-186): Crown Deed 2 effectively pre-met at game start. T5 Löwenritter shared control excluded. Deed 2 raised to ≥5 territories.

### AUD-BG-03: Audit With Thread Operations (all temporal axes)
P-01 PASS, P-11 PASS, P-14 PASS across all tested operations.

P1 findings:
- E-01 (→PP-184): Partial Mend creates Thread Wound at 2-marker territory. Undocumented. Warning required.
- D-01 (→PP-185): AP per-territory ceiling undefined. Multi-Inquisitor rules undefined. GAP-BG-17.
- B-02 (→PP-187): Co-Movement card effects not in params. GAP-BG-16.

P2 findings:
- B-01: Repeated Weaving triggers Inquisition (correct design).
- C-01: Past-Pull in T13 nearly impossible without VTM (intended gating).
- C-02: VTM advancement from Tribune on Thread Wound sites is reliable path (note).

### SIM-BG-02: Church TC Race
Church reaches TC 40 (Deed 1) at exactly S12 with Hafenmark suppression active.
Knife-edge timing creates maximum tension. Correct design.
Without Hafenmark suppression (Baralta Excommunicated): TC 40 by S6. Church wins midgame.
Tension correctly hinged on Hafenmark maintaining Baralta's Mandate. ✓

### SIM-BG-03: TC 80 All-Territory Sweep
P1 finding (→PP-183): Unlimited sweep seizes ~6.5 territories in one season. Game-ending.
Capped at 4 territories/season. TC gain from Seizure capped at +4/season.
Church still overwhelmingly powerful at TC 80; other factions have 2-3 seasons to respond.

### SIM-BG-04: Varfell Thread Supremacy
VTM 5 + RS ≥ 50 + T12/T13 achievable by S11-12 at median play.
Requires Restoration to actively maintain RS (mutual dependency — Varfell needs Restoration).
Correct design tension: hardest victory requires not destroying the world. ✓

### Open Gaps Remaining
GAP-BG-16: Resolved by PP-187 (Co-Movement card table).
GAP-BG-17: Resolved by PP-185 (AP ceiling + multi-Inquisitor).
A2-01: Guilds Wealth sink — still no mechanic. Design note logged, not patched.
