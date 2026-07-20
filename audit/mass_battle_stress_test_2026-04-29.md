# Mass Battle NERS Stress Test — Batch 1 & 2
<!-- generated: 2026-04-29 | scope: mass_battle_v30.md, params/mass_combat.md, military_layer_v30.md -->

## CRITICAL

### [S-FAIL-01] PP-297 Stalemate Break — canonical conflict
mass_battle_v30 §A.12: 3-turn zero-damage → Tactical Withdrawal, inconclusive, no Rout.
params §PP-297: same trigger → Discipline Ob 1 → Morale −1 → Rout possible, battle continues.
Two files, two outcomes. Strike one.

### [S-FAIL-02] BG Health / TTRPG Size formula breaks its own table
§B.5: TTRPG Size = BG Health / 1.5. Result: LightInf=6 (table=4), Levy=5 (table=3), HI=7 (table=5).
Formula irreconcilable with §B.2 table. One must be struck.

### [S-FAIL-03] PP-530 Overwhelming Size Advantage — wrong phase, undefined stat
Bonus in "Phase 4 only" — no Offence pool in Phase 4 (Thread Ops). Move to Phase 5.
"Opposing unit's Command score" — units have no Command stat. Define as enemy general's Command.

### [S-FAIL-04] §A.5 personal combat pause vs PP-506 bilateral — unqualified contradiction
§A.5 unqualified: "Mass battle pauses." PP-506: bilateral = does NOT freeze. Must disambiguate.

### [S-FAIL-05] Discipline between-battle recovery — unspecified [GAP]

### [S-FAIL-06] Morale reset between battles — not stated [GAP]

### [MATH-FAIL-01] §1.9 Siege calibration is mathematically impossible
Fort3 Military4 = Ob5 from 4 dice: P=0%. Doc claims 2%. Reverse: ~2% needs pool=7 Ob=6 TN7. [GAP]

### [MATH-FAIL-02] H "fixed" contradicts Discipline degradation mid-battle
PP-233: H fixed. H = min(Discipline, Command) + DR. Discipline degrades Phase 6 Step 2.
Resolution: H computed once at battle start, frozen for battle duration.

### [S-FAIL-13] Muster initial Size — §1.2 defaults irreconcilable with §1.4 formula
§1.2: LI=4, HI=5. §1.4: Size = 2 + Prosperity modifier, max=4. HI Size 5 unreachable.

### [S-FAIL-14] Reserve unit first-engagement Off/Def split — no declaration window
Off/Def declared Phase 1. Reserve commits Phase 3 Turn N+1, missing Phase 1 window.

### [S-FAIL-20] Crown/Church tactic cards — design doc vs params conflict
§B.4 Crown: Royal Guard (+3D), Ducal Call. params §ED-019: Royal Authority, Diplomatic Shield.
PP-283 canonises §B.4. Params versions not STRUCK.

## MODERATE

### [S-FAIL-07] 5-phase Support Thread Leap order unspecified
### [E-FAIL-01] TroopCount scaling vs PP-233 — dual damage formulas unreconciled
### [N-FAIL-01] 5-phase has no Godot implementation value — recommend documentation-only
### [S-FAIL-08] Idle army Morale symmetric in fortified siege — terrain carve-out needed
### [S-FAIL-09] Levy home-territory undefined after conquest [GAP]
### [E-FAIL-02] Army Morale modifier values absent (cross-file: derived_stats_v1 §8.2)
### [S-FAIL-16] Rout contagion brake at Morale 0 — rout vs freeze undefined
### [S-FAIL-17] §A.12 Morale Cascade "immediate" conflicts with Phase 6 sequence — assign to Step 3
### [S-FAIL-18] Artillery destruction vs rout — §A.12 trigger scope ambiguous
### [E-FAIL-03] Military 7 Veteran Experience peaks at Power 6 not 7. Military 1/2: 0 gain possible.
### [S-FAIL-19] Shadow Intel vs simultaneous BG tactic reveal — irreconcilable UX
### [S-FAIL-21] Mercenary Surge — type, persistence, source undefined
### [S-FAIL-22] Martial Law — undefined mechanic (Loewenritter card)
### [S-FAIL-15] Siege final Assault — resolution procedure absent
### [R-CONCERN-01] Experience on draw — potential grind; confirm design intent
### [S-FAIL-11] Player Morale Effect during personal combat pause — ambiguous presence
### [S-FAIL-12] Crossbow reload conflict (ED-094 every turn vs PP-301 every other)

## MINOR / ELEGANT

- Morale starting unit quality modifier formula absent
- Command halving rounding direction unspecified (Stage 1)
- NPC general Stage 1 — who executes Medicine check
- Skirmish -1D vs HI — which pool (Off / Def / total)
- Wedge negation — removes +2D Off only, or also -1D Def drawback
- BG commander bonus 0 at Military 1 (no floor stated)
- Partial: Discipline -15 = Stability -1.5 (not cleanly -1)
- Fort: BG pool bonus vs TTRPG +3 DR — no bridge rule
- Templar Vanguard pushes Discipline to 8 (stated cap 7)
- Home territory post-conquest undefined for Levy
- Military 1/2: Experience unreachable (base = ceiling)

## PROVISIONALS (PROV-01 through PROV-27)

PROV-01/02: TTRPG Size/Morale defaults all unit types (§B.2)
PROV-03: Discipline degradation trigger (§A.4)
PROV-04: Volley TN 6 (§A.7)
PROV-05: Lock phase assignment 4 vs 6 (params §PP-191)
PROV-06: Shield Wall +2D scope — all pools vs per-engagement (params §PP-500)
PROV-07: Thread-destroyed unit Phase 5 participation (params §PP-505)
PROV-08: Bilateral general personal combat (params §PP-506)
PROV-09: Splitting doctrine (params §PP-508)
PROV-10: Command per sub-unit (params §PP-504)
PROV-11: Muster output Size=2 (§A.13)
PROV-12: Coherence depletion math (§A.10)
PROV-13: MS<24 Rupture threshold (params)
PROV-14: Dissolution campaign impact (params)
PROV-15-19: PP-222/224/227/229/231 Thread x battle (params)
PROV-20: H frozen at battle start (§A.4, PP-233)
PROV-21: Siege pool formula (§1.9)
PROV-22: Reserve first-engagement Off/Def default (§A.6)
PROV-23: Artillery destroy vs rout §A.12 scope (§A.12)
PROV-24: Shadow Intel UX — peek or sequential (§B.4)
PROV-25: Mercenary Surge unit spec (§B.4)
PROV-26: Martial Law definition (§B.4)
PROV-27: Rout vs destroyed definitional boundary (§A.4, §A.12)
