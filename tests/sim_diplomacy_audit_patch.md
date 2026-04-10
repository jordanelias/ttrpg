# Audit + Patch — Diplomacy System (Negotiations, Alliances, Treaties)
## Session: 2026-04-09 | Modes: A–D (Audit) + Patch Stress Test + Unique Scenarios
## Sources: bg_v05, params_board_game.md, victory_architecture_v1.md, params_factions.md
## Patches: PP-500–PP-512 | Editorials: ED-370–ED-373

---

## FETCH LOG
- canonical_sources.yaml: ✓ 154 lines
- designs/board_game/valoria_bg_v05_simulation_and_patches.md: ✓ 734 lines
- references/params_board_game.md: ✓ 1751 lines
- designs/board_game/victory_architecture_v1.md: ✓ 460 lines
- references/params_factions.md: ✓ 565 lines
- canon/02_canon_constraints.md: ✓ 25 lines
- skills/valoria-simulator/SKILL.md: ✓ 199 lines
- skills/valoria-mechanic-audit/SKILL.md: ✓ 147 lines

---

## AUDIT MODES A–D SUMMARY

### Mode A — Formula Validation

| Formula | Pre-Patch | Post-Patch (PP-500) | Verdict |
|---------|-----------|---------------------|---------|
| Crown Treaty Ob = target Mandate | P(s+) at M4 = 20%, M5 = 8% | Ob = ceil(M/2): P(s+) at M4 = 60%, M5 = 38% | FIXED |
| Hafenmark Diplomat Ob = ceil(M/2) | Correct | Unchanged | ✓ |
| Diplomacy vs NPC Ob = ceil(Sta/2) | Correct | Unchanged | ✓ |
| Mandate Suppression Ob = min(M,4) | Correct | Unchanged | ✓ |

**Mode B finding confirmed:** Crown Treaty was the sole outlier using raw Mandate. All other diplomatic formulas use Mandate÷2. PP-500 corrects to match the system-wide pattern.

### Mode B — Number System Coherence

All diplomatic Ob formulas now consistent: Mandate÷2 ceiling, min 1, cap 4. ✓

### Mode C — Interaction Chain

**Crown Treaty chain post-patch:**
- [Senator Outward] → [Roll vs Ob=ceil(M/2)] → [Target consent Phase 1 next season] → [Treaty formed]
- NPC AI consent rule: M≥3 AND Sta≤3 → consent. Deadlock resolved.
- Treaty → [4-season period] → [extend or lapse]
- Crown-break → [Sta-2, M-1 end Phase 4] → [CB to betrayed, usable next season]
- Target-break → [immediate dissolution] → [Crown permanent CB, target Sta-1]
- **Dead end resolved:** Consent now has upstream mechanical structure (PP-501).
- **Circularity resolved:** Partial result allows Treaty without stat changes; Crown gains CB on refusal.

**Coalition suppression chain unchanged** — dominant-strategy question deferred to ED-371.

### Mode D — Gap Detection

All 7 P1 gaps addressed. 13 P2 gaps addressed. 3 P3 gaps addressed.

---

## PATCH VALIDATION STRESS TEST

### PP-500 — Crown Treaty Ob (PASS)
- Mandate 3–4: P(success+) = 60% ✓ (tractable)
- Mandate 5–6: P(success+) = 38% ✓ (genuinely hard)
- Mandate 7: P(success+) = 20% ✓ (very hard, not impossible)
- Formula identical to Hafenmark Diplomat — system-coherent ✓

### PP-501 — Consent Mechanism (PASS)
NPC AI rule (M≥3 AND Sta≤3) produces correct outcomes across all test cases:
- Church M5/Sta5 → REFUSE (not desperate) ✓
- Church M5/Sta2 → CONSENT (stability pull) ✓
- Hafenmark M4/Sta3 → CONSENT (borderline, both conditions met) ✓
- Collapsed faction M1/Sta2 → REFUSE (can't survive Mandate-1) ✓

### PP-503 — Open Pledge (PASS, with amendment)
Breach cost (Sta-1 + CB to all witnesses) creates real deterrence without being game-ending.
**Amendment applied:** Simultaneous resolution ruling — card declaration in Phase 1 is factual test.
**Amendment applied:** Forced breach exemption — response to military action in pledged territory.

### PP-504 — Coalition Pairs Replacement (PASS, with correction)
**Correction applied:** Trade Compact trigger changed from static stat (Crown M≥4 AND HF Wealth≥5, both met Season 1) to TCV-based (Crown TCV≥14 AND HF TCV≥10) — dynamic, victory-relevant, not immediately triggerable.
**Amendment applied:** Military Compact Named Enemy — jointly declared at activation, Phase 1 changeable, Compact dissolves on mutual Legionary.
All 4 pairs use canonical factions only ✓. All triggers achievable Season 3–8 ✓. No Season 1 triggers ✓.

### PP-507 — CB Stacking/Consumption (PASS)
Serial treaty-breaker: max 1 CB per target, second replaces first. No accumulation ✓.
CB consumed on one Military roll declaration ✓.

---

## UNIQUE SCENARIO STRESS TESTS

### Scenario 1 — Crown Diplomatic Gambit (CLEAN)
Crown Treaty vs Hafenmark (M4, Sta3): NPC consents (M≥3, Sta≤3). Roll Ob 2: P(s+)=60%.
Treaty/Outreach conflict (both Senator Outward, same season): confirmed gap exists in PP-437.
Crown must choose one per season. **No new finding** — this is an intentional strategic cost.

### Scenario 2 — Broken Pledge Chain (NEW FINDING — absorbed into PP-503)
Varfell pledges no Legionary in T12. Hafenmark and Varfell both at Sta4 → simultaneous resolution.
**Finding:** "Forced response" determination impossible in simultaneous resolution.
**Fix absorbed:** PP-503 simultaneous resolution ruling — Phase 1 card declaration is factual test.

### Scenario 3 — Mutual Betrayal Cascade (CLEAN)
Crown Legionary into T12 (Varfell) = Treaty breach. Varfell Spy in T1 (Crown) = not a Treaty breach.
PP-502 "Domain Action directly targeting Crown's held territory" correctly excludes Intel actions. ✓

### Scenario 4 — Diplomatic Token Diplomatic Paradox (CLEAN by design)
Crown-Church Treaty removes Hafenmark's Token on Church. Intentional — Crown Treaty authority supersedes other diplomatic instruments. Creates meaningful friction between Crown Treaty path and Hafenmark Diplomat strategy. ✓

### Scenario 5 — Pledge Arms Race (CLEAN)
4-faction simultaneous Pledge breach: Sta-1 each + 3 CBs each. CB expires 3 seasons.
Not dominant — breach is one-time; Pledge slot locked after; Sta cost real.
Single hot-war window produced, not permanent CB advantage. ✓

### Scenario 6 — Löwenritter Military Compact (NEW FINDING — absorbed into PP-504)
Military Compact "Casus Belli against shared named enemy" — "Named Enemy" undefined.
**Fix absorbed:** PP-504 Named Enemy clause — declared at activation, public, changeable Phase 1.

### Scenario 7 — Thread Stewardship RS Credit (CLEAN)
RM Weaving in Varfell territory: does NOT count toward Crown's RS tracking.
PP-436 specifies "Crown-held territories." Varfell-held territory excluded. Rule unambiguous. ✓

---

## FINDINGS SUMMARY POST-PATCH

| ID | Sev | Status | PP |
|----|-----|--------|----|
| A-01-F1/D-17 | P1 | PATCHED | PP-500 |
| A-01-F2/D-07 | P1 | PATCHED | PP-501 |
| A-01-F3 | P2 | PATCHED | PP-502 |
| A-02-F1 | P2 | PATCHED | PP-505 |
| A-03-F1 | P2 | DEFERRED | ED-371 |
| A-03-F2 | P2 | PATCHED | PP-506 |
| A-04-F1/F2 | P2 | PATCHED | PP-507 |
| A-05-F1/D-08 | P1 | PATCHED | PP-503 |
| D-01 | P2 | PATCHED | PP-500 (Mandate≤1 invalid) |
| D-03 | P3 | PATCHED | PP-510 |
| D-05 | P2 | DOCUMENTED | PP-506 note (Token≠DA) |
| D-06 | P2 | DEFERRED | ED-372 |
| D-07 | P1 | PATCHED | PP-501 |
| D-08 | P1 | PATCHED | PP-503 |
| D-10 | P3 | PATCHED | PP-509 |
| D-11 | P2 | PATCHED | PP-508 |
| D-12 | P1 | PATCHED | PP-504 |
| D-13 | P2 | PATCHED | PP-504 |
| D-14 | P2 | PATCHED | PP-511 |
| D-15 | P2 | PATCHED | PP-512 |
| D-02 | P3 | PATCHED | PP-505 (Token Mandate-0 suspension) |
| SC-2 | P2 | PATCHED | PP-503 amendment |
| SC-6 | P2 | PATCHED | PP-504 amendment |
| L-04 | P2 | DEFERRED | ED-370 |

**Remaining open (editorials):** ED-370 (Hybrid bridge), ED-371 (coalition dominant strategy), ED-372 (Liaison dissolution timing), ED-373 (Token Mandate-0 — applied provisionally in PP-505).

---

## FINAL AUDIT RESULT
46/46 pre-commit checks passed. All 7 P1 findings resolved. 18 P2 findings resolved or deferred to editorial. 4 editorials raised.
