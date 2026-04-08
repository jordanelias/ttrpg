# Valoria Simulation Coverage Matrix
## Single canonical source. Updated by sim-orchestrator after each test batch.
## 7 dimensions tracked per test: Mechanic | Mode | Temporal | Tracks | Factions | NPCs | Archetypes

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-X-01 | Personal Combat + W-24 | C+B | Single scene | Health, Wounds, Stamina, Coherence, RS | None | Mira, Kaspar | Practitioner-combatant | Complete |
| SIM-X-02 | Debate + W-41 | C+B | Single scene | Composure, Coherence, RS, Belief | Church | Vessa, Aldric | Asymmetric Debate | Complete |
| SIM-X-03 | Mass Battle + W-30 + W-33 | C+B | 2 turns | Size, Cohesion, Morale, Coherence, RS | Lowenritter, Rebel | Solmund | Thread-supported Mass Battle | Complete |
| SIM-X-04 | Mass Battle + Personal Combat (General Duel) | C+D | 3 turns | Size, Cohesion, Morale, Health, Wounds, CR | Lowenritter, Rebellion | Harnak, Davan | General Duel | Complete |
| SIM-X-05 | Grand Debate + W-41 + W-42 + Audience | C+B | 5 exchanges | Composure, Coherence, RS, TC, Knots | Church, Hafenmark | Baralta, Himlensendt, Klapp | Institutional Grand Debate | Complete |
| SIM-X-06 | Personal Combat + Wound −1D + CE arc | C+D | 4 rounds | Health, Wounds, Stamina, CE | Lowenritter, Church | Ehrenwall, Haelmund, Vald, Maret | Named NPC duel + Inquisitor arc | Complete |
| SIM-X-07 | Mass Battle + W-30 + P-31 + General Duel + Stage 1/2 | C+D | 3 turns | Size, Cohesion, Morale, Coherence, RS, CR, Coup Counter | Lowenritter, Church | Ehrenwall (killed), Jarnstal, Maret | Named-NPC mass battle + Thread + deadlock | Complete |
| SIM-X-08 | Seasonal Accounting cascade | D+E | 1 season | All faction stats, TC, RS, Knots | All | Baralta, Klapp, Ehrenwall (dead), Vald | Full cascade | Complete |
| SIM-X-09 | Social (Vaynard/Almud) + Discovery Event + Domain Echo + Zoom | C+B | 1 scene | Composure, TS, TK, TC, IP | Crown, Varfell, Church | Vaynard, Almud, Klapp | Social → Thread → Faction zoom | Complete |
| SIM-X-10 | Sovereign Authority Doctrine + Olafsson Evidence Chain + TC cascade | C+B | 1 season | TC, Church Stability, Mandate, Baralta penalty | Church, Hafenmark | Baralta, Himlensendt, Olafsson | Domain Action chain + clock cascade | Complete |
| SIM-X-11 | Maret infiltration → Thread Diagnosis → Domain Echo → Inquisitor advance | C+B | 1 scene | TK, TC, CE, Coherence, RS, Investigation stages | Church, Varfell | Maret, Klapp, Vald | Personal→Thread→Faction zoom sequence | Complete |
| SIM-X-12 | 3-season full cascade | D+E | 3 seasons | All clocks, all faction stats, all NPC states | All | All named | Full cascade accounting | Complete |

| SIM-X-13 | FR-D-01 Dissolution + Past-Oriented Pulling (hypothetical TS 70) | C+B | Single scene | RS, Coherence retention, Temporal Disjunction, Certainty | None | Maret Uln, Haelmund (Disjunction witness) | Evidence erasure, PO-Pull prerequisites | Complete |
| SIM-X-14 | Mode 2 Monstrous Entity + W-06b + Vaynard Discovery + Domain Echo | C+D | Single scene | RS, Coherence, Certainty, TC, Locked Zone proximity | Varfell, Niflhel, Crown | Vaynard, Maret, Niflhel Envoy, Crown Diplomat | Political scene interrupted by entity | Complete |
| SIM-X-15 | Knot crisis (Klapp/Ansel) + Certainty + Inspiration attack + Call a Knot | C+D | 3 exchanges | Coherence, Certainty, Knot strain, Composure, Inspiration | Church | Klapp, Olafsson, Ansel | Practitioner under interrogation + Knot crisis | Complete |
| SIM-X-16 | Collective Weave (Maret anchor + Klapp helper) + Rendering Crisis | C+B | Single scene | Coherence retention (both), Certainty (Klapp→0), RS, Knots | Varfell | Maret, Klapp | First collective operation + Rendering Crisis | Complete |

> Pre-v3 batch coverage archived in `deprecated/sim_coverage_matrix_legacy.md`.

## P1 Findings — Editorial Decisions Required

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-11 | X-03 | W-33 broken for Size≤2 units: Cohesion=2 insufficient when Size is binding constraint | RESOLVED — ST-TW-02 applied to threadwork_redesign_v25.md |
| F-27 | X-07 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution rule | PATCHED — Add to mass_battle_v3: at 3+ consecutive turns with 0 damage dealt, units with no tactical option may withdraw one zone (costs movement, does not trigger pursuit). |
| F-30/F-33 | X-07/08 | Coup Counter: no successor rule on Grandmaster death | PROVISIONAL — On Grandmaster death with Coup Counter ≥ 1: Löwenritter selects highest-CR surviving named officer as acting Grandmaster. Coup Counter resets to 0. Provisional pending user approval. |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap on TC | PROVISIONAL — TC change cap: ±3 per season from Domain Actions (±5 from all sources combined). Provisional pending user approval. |
| F-45 | X-10 | Church Stability brake scope — suppresses Mandate-based TC only or all TC sources? | EDITORIAL — ED-049 added to ledger |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability | PROVISIONAL — Stability recovery: +1 Stability per season of no hostile Domain Actions targeting that faction + Stability ≤ 3 (slow natural recovery). Provisional pending user approval. |

## Rules Gaps (No Patch Needed — GM Ruling Acceptable)

| ID | Source | Description |
|----|--------|-------------|
| F-38 | X-09 | Discovery Event mid-Debate: no interrupt rule; conservative ruling taken |
| F-41 | X-09 | No formal Impression rule for NPC TS-perception events during social scenes |
| F-48 | X-11 | CE track has no upper-ceiling distinction beyond Trajectory at CE 3 |

## Terminology Correction Applied

All prior SIM-X-01 through X-08 references to "Strength" as mass battle headcount stat corrected to **Size** in this index. Source files retain original text; correction is notional for tracking purposes only.

## New P1 Findings (SIM-X-13 through X-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-58 | X-14 | RS 22 is 2 points from Dormant (Leap-disabled) threshold — any failed Weaving crosses the line globally | Open — campaign awareness item |

## New P2 Findings (SIM-X-13 through X-16)

| ID | Source | Description |
|----|--------|-------------|
| F-54 | X-13 | Past-Oriented Pulling TS 70+ hard gate correctly blocks TS 50 — gate works as designed |
| F-55 | X-13 | PO-Pulling "+1 additional" Coherence cost = +1 Ob on retention roll sum — correctly maps under new system |
| F-62 | X-15 | Certainty (Spirit=3) depletes to 1 after 2 Leaps — one more Leap triggers Rendering Crisis for low-Spirit practitioners |
| F-63 | X-15 | Knot strain from Dissonant Coherence reaches crisis threshold near-inevitably without recovery; Conversion makes recovery unlikely — correct self-reinforcing arc |
| F-66 | X-16 | Rendering Crisis fires post-Leap, not during contact — no interrupt rule; crisis doesn't retroactively affect the operation |
| F-69 | X-16 | Territorial Weave success (−1 Ob territory-wide) may be disproportionately powerful at low RS when Thread operations are most precious |

## Editorial Items (Open)

| ID | Source | Description |
|----|--------|-------------|
| F-70 | X-16 | Klapp Rendering Crisis: Belief revision content requires user input |
| F-45 | X-10 | Church Stability brake scope: suppresses only Mandate-based TC, or all TC sources? |
| F-52 | X-12 | Faction Stability recovery rate for externally damaged Stability — no rule defined |
| F-30 | X-07 | Coup Counter successor on Grandmaster death — no rule defined |
| F-27 | X-07 | Mass battle stalemate resolution — no rule defined |
| F-11 | X-03 | W-33 broken for CP≤2 units — EDITORIAL PENDING |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season — no seasonal TC cap |
| SIM-D-01 | Debate: Argue/Read/CLASH/COMP/DIVERGE/TIE/Track/Composure/Concentration/Doubt/Regroup | TTRPG | CROSS | Composure, Concentration, Conviction Track | Generic (all factions modelled) | Generic archetypes | High-Pres orator, History-specialist, Low-social, Balanced social | Complete | F-D-01 (P1), F-D-02 (P2), F-D-03 (P2), F-D-04 (P2), F-D-06 (P2); SIM-DEBT-01 recalibrated |

| SIM-D-02 | Debate: Full scenario C+J — Himlensendt vs Baralta, 3-exchange Parliament, Diverge chain | TTRPG | PRESENT | TC, Composure, Concentration | Church, Hafenmark | Himlensendt, Baralta | Institutional authority, Legalist-constitutionalist | Complete | F-C-02 (P2 PP-100), F-C-04 (P1 ED-051), F-C-05 (P2 ED-052), F-C-06 (P1 cognitive load); SIM-DEBT-01 RESOLVED |

| AUDIT-D-01 | Debate system Modes A–G — formula validation, number systems, interaction chains, gaps, principles, burden, cross-mode | TTRPG+BG+HYB | CROSS | Composure, Concentration, TC | All | Generic | All debate archetypes | Complete | FA-01/02/03/04 (P2 patched PP-101/102/103/104), GAP-DS-09–20, C-01/C-02/G-01/G-03 (P1), ED-053–059 logged |
| SIM-D-03 | Debate subsystem G2 (Tribunal dominant strategy) + K1 (cross-mode delta) + K2 (transition) | TTRPG+BG+HYB | CROSS | Composure, TC | Church, Hafenmark | Generic Inquisitor, Generic Accused | Institutional authority, disadvantaged accused | Complete | G2-F-01 (P1 PP-109), K1-01/K1-02 (P1 ED-056/053), K2-F-02 (P1 PP-105 ext) |

| SIM-D-04 | Debate gap-fill stress test — §§6.11-6.15, PP-112-118, BG Vote, Hybrid, Coalition, Beliefs, Total Victory | TTRPG+BG+HYB | CROSS | TC, Composure, Concentration, Debate Fatigue | Church, Hafenmark, Crown, Varfell | Himlensendt, Baralta, Klapp | Coalition, BG delegate, Hybrid | Complete | C-01/02/03 coalition confirmed; A.2-03 PP-117 (BG zero-zero); K2 PP-118 (Hybrid exchange count); SIM-DEBT-02 flagged |

| SIM-HYB-01 | G1 Mass Combat, G2 Debate, G3 Threadwork, G4 Faction Seasonal, K2 Transition, C Full Scenario | HYB | PRES | TC, RS, IP, Stability, Coherence, Composure, Wounds, Unit Str/Morale/Cohesion | Church, Varfell, Crown, Hafenmark | Vaynard, Cardinal Klapp, Templar Sergeant | Practitioner-Scholar, Institutional Legalist, Church Militant | COMPLETE (Session A + B) | F-HYB-01 (P1→PP-101), GAP-K2-01 (P1→PP-101), F-HYB-02 (params stale→params_debate fixed), F-HYB-03 (P2→ED-054); 7 params gaps logged |

| AUDIT-D-02 | Debate system v1.5 re-audit + all modes + Thread temporal axes | TTRPG+BG+HYB | PAST/PRES/FUT/CROSS | TC, Composure, Concentration, RS, Coherence | All | Himlensendt, Baralta, Klapp, Maret, Vaynard | All debate archetypes | Complete | PP-119-123 applied; HD-F-01 P1 (PP-120 Hybrid clamp); TT-F-04 P1 (PP-123 temporal conflict); ED-087-091 logged |
| SIM-D-05 | Thread in all temporal axes during debate — Past/Present/Future axis tests | TTRPG | PAST+PRES+FUT | RS, Coherence, TC, Conviction Track | Church, Varfell | Maret, Klapp, Vaynard | Practitioner-orator, institutional | Complete | TT-F-01-05; 3 P1 findings patched PP-120/122/123; 2 P2 ED-097/089 |
| SIM-X-17 | POP + paradox window (PP-193) | TTRPG | PAST | Coherence, RS, TD | None | Generic TS70, TS30+ opponent | Veteran practitioner, adversary | Complete | 1 gap (sequential POP on paradoxed thread) |
| SIM-X-18 | Rendering Crisis arc (PP-194) | TTRPG | CROSS | Coherence, Thread Sensitivity, Bonds | None | Generic practitioner, Close Knot | Late-campaign veteran | Complete | 2 findings: stability disruption gap; TS30-31 TS loss risk |
| SIM-X-19 | Mass battle ×3 RS multiplier (PP-192) | TTRPG+Hybrid | PRES | RS, Coherence | Generic | Generic TS70 practitioner | Combat practitioner | Complete | P1: 3 Dissolution attempts = campaign-ending RS drain; RS<24 Rupture threshold |
| SIM-X-20 | Hybrid Coherence 10-session (PP-198) | Hybrid | CROSS | Coherence, Thread Sensitivity | All | 2 PC practitioners | Hybrid practitioner-strategist | Complete | Co-declaration tie-break gap; GM guidance needed on sustainable op rate |


## SIM-DEBT Register

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-02 | SIM-D-04 | **STRUCK** — superseded by PP-234 (Social Contest System v2 redesign). Corroboration mechanics rebuilt. Subsumed by SIM-DEBT-03. |

*(old SIM-DEBT register entries above)*


| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-01 | Debate system | RESOLVED. Mode C (SIM-D-02) confirmed: resistance dominates track movement; genre weight > pool size adjustments; 3-exchange Formal Debate → Compromise ~95%. CLASH strain calibration (2-3/exchange) analytically confirmed, scenario validation pending forced-CLASH run. | RESOLVED |
| AUD-TTRPG-01 | Modes A–G: Formula, Number Systems, Interaction Chains, Gap Detection, Core Principles, Playtest Burden, Cross-Mode | TTRPG | — | All tracks | All factions | All named NPCs | Full TTRPG mode | Complete | 11 P1s, 14 P2s, 4 P3s — see tests/aud_ttrpg_01.md |

## Provisional Decisions (from coverage matrix findings)

| Finding | Provisional Rule | Status |
|---------|-----------------|--------|
| F-27 | Mass battle stalemate: 3+ turns 0 damage → may withdraw one zone | Provisional — apply to mass_battle_v3 |
| F-30/F-33 | Coup Counter successor: highest-CR officer, Counter resets | Provisional — apply to designs/combat |
| F-43 | TC change cap: ±3/season Domain Actions, ±5 all sources | Provisional — apply to stage5_clocks or designs |
| F-52 | Stability recovery: +1/season with no hostile actions when Stability ≤ 3 | Provisional — apply to faction rules |


## New P1 Findings (SIM-D-01)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-D-01 | SIM-D-01 | DIVERGE+TIE: both score 0, different genres — Tie rule fires (any interaction type). | PP-097 PROVISIONAL |

## New P2 Findings (SIM-D-01)

| ID | Source | Description |
|----|--------|-------------|
| F-D-02 | SIM-D-01 | Regroup at Concentration=0: Spent ambiguous. PP-098: Regroup consumes Spent without penalty. |
| F-D-03 | SIM-D-01 | Obscuring in Divergence: orientation_weight undefined. PP-099: Doubt Marker rule applies. |
| F-D-04 | SIM-D-01 | Presence 1 cannot participate meaningfully in formal debate. Institutional gatekeeping implied. |
| F-D-06 | SIM-D-01 | Grand Debate + Corroboration: ~90 resolution steps. No GM reference card. Tooling gap. |


## Board Game Mode Audit (2026-04-02)

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| AUDIT-BG-01 | BG Mode: Modes A+B+C+D+E+F+G | BG+Hybrid | Structural audit | TC RS IP PI Faction-stats Cohesion | All BG | N/A | N/A | Complete | GAP-BG-01 (P1) GAP-BG-02 (P1) GAP-BG-14 (P1); 9xP2; PP-112-122 applied |

### P1 Findings — AUDIT-BG-01

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| GAP-BG-01 | AUDIT-BG-01 | Faction collapse exit condition undefined | PP-117 PROVISIONAL |
| GAP-BG-02 | AUDIT-BG-01 | Simultaneous RS=0 + IP>=80 resolution undefined | PP-118 PROVISIONAL |
| GAP-BG-14 | AUDIT-BG-01 | params_board_game.md: Majority-1s override stale (struck from design) | PP-112 APPLIED |

### P2 Findings — AUDIT-BG-01

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| GAP-BG-03 | AUDIT-BG-01 | PI floor/ceiling undefined | PP-115 PROVISIONAL (ED-055) |
| GAP-BG-04 | AUDIT-BG-01 | TC ceiling post-TC-80 undefined | PP-116 PROVISIONAL (ED-056) |
| GAP-BG-06 | AUDIT-BG-01 | IP above 80 undefined | PP-114 PROVISIONAL |
| GAP-BG-07 | AUDIT-BG-01 | BG unit Cohesion undefined in params | PP-119 PROVISIONAL |
| GAP-BG-09 | AUDIT-BG-01 | TC cap vs seizure interaction | PP-116 PROVISIONAL |
| GAP-BG-11 | AUDIT-BG-01 | Reformed Settlement +1 Ob — confirm no reversal | PP-121 PROVISIONAL (ED-058 open) |
| G-BG-03 | AUDIT-BG-01 | BG Thread Ops: no Coherence — confirm intentional | PP-120 PROVISIONAL (ED-057) |
| G-BG-05 | AUDIT-BG-01 | CP awards in Hybrid: no worked example | PP-122 PROVISIONAL |
| A-BG-03 | AUDIT-BG-01 | Overwhelming threshold TTRPG vs BG conflict | ED-031 PROVISIONAL ongoing |

## SIM-BG-01 — Collapse Exit + Simultaneous Catastrophe (2026-04-02)

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-BG-01 | PP-117 (collapse exit) + PP-118 (simultaneous catastrophe) | BG | 2-4 seasons | Stability Mandate RS IP PI | Restoration Church Crown | N/A | Collapsed faction, end-game multi-clock race | Complete | SIM-BG-01-03 (P1 PP-118 step error — PP-118-rev1 applied); SIM-BG-01-01/02/04 (P2) |

### P1 Findings — SIM-BG-01

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-BG-01-03 | SIM-BG-01 | PP-118 Step 5 reference wrong — Restoration victory is Step 12 not Step 5; pre-check added at Step 5 explicitly | PP-118-rev1 APPLIED |

### P2 Findings — SIM-BG-01

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-BG-01-01 | SIM-BG-01 | Collapsed faction card access at Mandate 0 — depends ED-001 | Provisional: card access retained for recovery |
| SIM-BG-01-02 | SIM-BG-01 | Recovery Govern Partial/Failure outcome undefined in PP-117 | Provisional: Partial = no recovery this season |
| SIM-BG-01-04 | SIM-BG-01 | Church TC 65 at Step 3 vs Restoration Step 5 win: sequence clarification | PP-118-rev1 documents: Restoration Step 5 pre-empts Step 12 |

## Session B Findings (SIM-HYB-01)

| ID | Severity | Description | Action |
|----|----------|-------------|--------|
| F-HYB-04 | P2 | Zoom In as TC win-delay exploit | ED-056 |
| F-HYB-05 | P2 | Unit ghost state during Zoom In window | ED-057 |
| F-HYB-06 | P2 | Debate stalemate with no forced resolution | ED-058 |
| F-HYB-07 | P2 | COMPETITION + TIE interaction undefined on equal successes | PP-103 pending |
| F-HYB-08 | P1 | Military 1 faction has no deployable unit in B.2 (no CP-1 unit type) | PP-104 pending |
| F-HYB-09 | P1 | Zoom In/Out cognitive load = 14/10; novice time 12m | ED-055 (GM reference card) |
| GAP-D-01 | structural | RS=0 at Zoom In: which gap rules fire first | ED-059 |
| GAP-D-02 | structural | Composure restoration between debate scenes not specified | ED-060 |
| Mode J Debate | P2 | Debate load = 11/10; novice time 5m per exchange | Covered by ED-055 scope |

## PP-103 Resolution Note (2026-04-02)

PP-103 (Phase-Lock Protocol + Levy unit) resolves:
- F-HYB-08 (P1): Military 1 Levy unit added to B.2 ✓
- F-HYB-09 (P1): ED-055 reference card created ✓
- ED-057 (P2): Ghost-unit state eliminated by Phase-Lock ✓

Remaining open from SIM-HYB-01: ED-056, ED-058, ED-059, ED-060, PARAMS-GAP-04/05/06-MC.

## PP-104 Resolution Note (2026-04-02)

PP-104 applied: 4 projectile categories, Str corrections, pool split, damage formula, BG Battle Partial.
- PARAMS-GAP-04: resolved (pool split declared Phase 1) ✓
- PARAMS-GAP-05: resolved (Str loss = net hits + Dmg Mod − DR) ✓
- PARAMS-GAP-06-MC: resolved (BG Battle Partial, margin ≤1) ✓
- User Str audit: all units −2, Ranged/Artillery −3 ✓
Open for editorial: ED-061, ED-062, ED-063.

| SIM-PROJ-01 | LP/HP/LBl/HBl projectile categories | TTRPG+BG | PRES | Unit Str, Wounds, DR, Morale | Generic | Generic unit archetypes | Ranged skirmisher, siege crew, armoured infantry | COMPLETE | F-PROJ-01 (P1→PP-106), F-PROJ-03 (P1→ED-064), F-PROJ-04 (P1→PP-105), F-PROJ-08 (P1→PP-106 sight-line), F-PROJ-02/05/06/07 (P2→EDs) |
| SIM-BG-01 | BG turn sequence, Domain Actions, Seasonal Accounting, Unit Muster, Parliamentary Manoeuvre | BG | PRES | TC, RS, IP, PI, faction stats | Crown, Church, Hafenmark, Varfell, Guilds, Niflhel, Restoration Movement | Generic faction archetypes | Military, Religious, Economic | COMPLETE | F-01 P2->ED-064; F-03 P1->ED-065; F-06 P1 stale compilation; F-07 P2->PP-170; F-08 P2->ED-066; PG-01/02/04/05->PP-169 |
| AUDIT-HYBRID-01 | All hybrid mechanics: Phase-Lock, State Transfer, Domain Echo, Register Shift, Zoom In/Out | HYB | PRES | TC, RS, IP, Unit Str/Cohesion/Morale, Domain Echo queue | All factions | Generic | All | COMPLETE Modes A–G + K2 extended | GAP-HYB-01–12, AUDIT-C-01–03, ST-K2-01–05, AUDIT-E-01–05; PP-107–112 applied; ED-071–076 flagged |
| ED-001-RESOLVE | Card-Hand action economy adoption from stage_bg_proposal_v02.md | BG | PRES | n/a | All factions | n/a | n/a | COMPLETE | PP-177 applied; ED-001 resolved; ED-078 resolved; DESIGN-DEBT-BG-01 logged |
| DOCREVIEW-BG-01 | Full BG doc review + arc review: Wealth sink, Overwhelming, params gaps PG-09/10/12, ED-048 Ceiral, conviction texts, AER, P-14 gaps | BG+ALL | PRES/CROSS | RS, TC, IP, PI | All factions | All named NPCs | All | COMPLETE | PP-178 Wealth sink; PP-179 Overwhelming 2xOb; PG-09/10/12 resolved; ED-048 resolved; ED-077 resolved; ED-080-086 logged |
| SIM-001 | PP-172: LP/HP/LBl/HBl ranged subtypes, TN8 defence, environmental factors | TTRPG | PRES | — | All | Generic | Archer, Crossbowman, Slinger, Melee Fighter | COMPLETE | F1: HBl anti-armour profile confirmed. F2: Cover viable balance. F3: TN8 defence viable but weak (P2 note). F4: ED-085 pool-split ruling. F5: ED-086 HBl availability. |
| AUD-BG-01 | Full BG system audit — formulas, number systems, interaction chains, gaps, principles, playtest burden, cross-mode | BG+HYBRID | CROSS | All BG tracks | All factions | — | All | COMPLETE | PP-180 bundle applied (8 fixes); ED-087 (P1 TC 80 scope); GAP-BG-05 (P1 co-movement protocol) remains open |
| SIM-FF-01 | BG Fail Forward comparative (4-season, 6 factions, fixed rolls) | PP-177 confirmed; ED-085/086/087 flagged | 2026-04-02 | COMPLETE |

| SIM-002 | PP-173: mass combat ranged DR split (LP/HP/LBl/HBl), Volley Phase, Prepared Defence | TTRPG | PRES | — | All | Generic | Archer unit, Crossbow unit, Sling unit, Heavy Infantry | COMPLETE | F1: Old Projectile DR (LightCut) was P1 wrong — HP/HBl massively undervalued vs armour. F2: LBl anti-levy only at mass scale. F3: HBl personal vs Artillery distinction required. |
| SIM-003 | BG ranged weapons: K1 cross-mode delta; BG abstraction confirmed correct | BG/Hybrid | PRES | — | All | Generic | All unit types | COMPLETE | F1: BG correctly abstracts weapon types — no changes needed. F2: ED-087 raised (faction ranged modifier). |
| AUD-BG-02-03+SIM-BG-02-04 | BG audit (no Thread + Thread all axes) + stress tests | BG+HYBRID | CROSS | All | All factions | All NPCs | All | COMPLETE | PP-183 TC80 cap; PP-184 Partial Mend warning; PP-185 AP ceiling; PP-186 Crown Deed2; PP-187 Co-Movement cards |
| SIM-005 | PP-175: mass combat ranged DR scaling (÷2); mass battle scenarios A-D | TTRPG | PRES | Strength/Cohesion/Morale | Crown/Church/Varfell/Hafenmark | Generic commanders | Archer, Crossbow, Heavy Infantry, Sling units | COMPLETE | F1(P1): Unscaled DR made LP/LBl anti-levy-only at mass scale — PP-175 provisional. F2: HP now penetrates Medium (0.6 E[dmg] at CP4). ED-094/095/096 raised. |

| SIM-004 | PP-172 personal combat scenarios: gatehouse LP defence, HP+HBl skirmish, Maret HBl vs Templar | TTRPG | PRES | Health/Wounds/Stamina | Crown, Löwenritter | Maret Uln, Generic Knight | LP defender, HP crossbowman, HBl skirmisher, Heavy melee | COMPLETE | 004A-F1: LP ~2.0 dmg/round vs Heavy (formula correction from SIM-001). 004B-F1: HP+HBl destroys heavy veteran in 3 rounds. 004C-F1: High-pool HBl powerful — terrain is balance. |
| SIM-005 | PP-173 mass combat scenarios: HP vs Heavy armour, LP vs levy, HBl unit test | TTRPG | PRES | Str/Cohesion/Morale | Crown, Varfell | Generic commanders | HP crossbow unit, LP archer unit, HBl unit, Heavy infantry | COMPLETE | 005A-F1: HP units zero damage vs Heavy armour at standard CP (correct — mass combat abstraction). 005B-F1: LP devastates levy. 005C: HBl effective vs Light/Medium. |
| SIM-006 | Hybrid siege: PP-091 Artillery, PP-172 HBl personal, Zoom-In intersection | Hybrid | PRES | Unit Str/Fortification | Löwenritter, Crown | Maret Uln | HBl skirmisher, Artillery crew | COMPLETE | 006-F1: Personal HBl viable anti-artillery sniper archetype in Hybrid mode. |
| PP-188 | Comprehensive params correction from authoritative v04 scan | BG | CROSS | All | Crown/Church/Hafenmark/Varfell/Restoration/Löwenritter | All | All | COMPLETE | Faction list corrected; TC=22, PI=7, Torben=3; Phase4 order corrected; Church/Crown/Varfell victory conditions corrected; Guilds/Niflhel removed as players; ED-088 Ministry gap |
## SIM-DEBT Updates (2026-04-02)
| ID | Status | Notes |
|----|--------|-------|
| SIM-DEBT-TW-01 | RESOLVED (SIM-X-17) | Paradox window mechanic validated. 1 minor gap (D3). |
| SIM-DEBT-TW-02 | RESOLVED (SIM-X-18) | Rendering Crisis arc validated. 2 findings (SIM-18-01, SIM-18-02). |
| SIM-DEBT-TW-03 | RESOLVED (SIM-X-19) | ×3 RS multiplier validated. P1 finding: mass Dissolution is campaign-altering (SIM-19-01). |
| SIM-DEBT-TW-04 | RESOLVED (SIM-X-20) | Hybrid Coherence calibrated — Moderate scenario is correct design intent. 2 minor findings. |
| PP-189 | v05 final corrections over PP-188: TC=28, Church victory TC≥65, TC80 seizure formula, majority-1s struck, Uphold/Appease | BG | CROSS | TC RS IP PI | All | All | All | COMPLETE | PP-189 applied |
| PP-190-193 | Torben 10, Varfell 4/4+fortification constraint, TC80 redesign, Ministry NPC design | BG | CROSS | PI TC RS | All + Ministry | All | All | COMPLETE | ED-088 resolved |
| PP-195 | Territory table reconciliation from physical map + canonical source | BG | CROSS | All | All | All | All | COMPLETE | ED-107 resolved; Hafenmark=T2/T4/T8; Varfell=T9-T12; Crown=T1/T3/T5/T6/T7/T13; Guilds/Niflhel network-only |
| SIM-X-21 | Collective Weaving (§2.5), OA brittleness, Mending cascade | TTRPG | CROSS | Coherence, RS, OA modifier | Crown, Hafenmark | Mira (TS70), Aldric (TS55) | Veteran practitioner-diplomat, junior aide | Complete | Lock vs Weave strategic choice confirmed; OA→Shifting Object carry-through gap || SIM-X-22 | Combat + Mass Battle + Thread + Temporal Axes | TTRPG+Hybrid | PAST/PRES/CROSS | RS, Coherence, Str, Cohesion, Morale, Health, Stamina, Wounds | Lowenritter, Altonian | Mira (TS70), Kaspar, Generic Altonian Commander | Practitioner-general, mass battle+personal overlap, temporal manipulation | Complete | 7 P1, 5 P2, 3 P3. PP-221–231 applied (all PROVISIONAL). ED-120–126 logged. See tests/sim_x_22_combat_massbattle_threadwork_temporal.md |
| AUD-CMB-01 | combat Modes A–G: formula, number systems, interaction chains, gap detection, core principles, playtest burden, cross-mode | TTRPG/BG/Hybrid | CROSS | All combat variables | All factions | All | All | COMPLETE | 8 P1, 19 P2, 6 P3. See tests/audit_combat_2026-04-02.md |
| BAL-BG-02 | Balance analysis 4-player game | BG | CROSS | All | Crown/Church/Hafenmark/Varfell | All NPCs | All | COMPLETE | 5 P1 findings (ED-109-112); stale refs fixed PP-202 |
| PP-203 | Balance fixes + stale refs | BG | CROSS | All | All | All | All | COMPLETE | ED-109-113 resolved || SIM-22 | personal combat post-audit (Run-22) — 5 brackets, 500 fights each — PP-210–218 | TTRPG | CROSS | Health, Wounds, Damage, Armour DR, Fibonacci, Feint, Tie Up, Rescue, Dodge | All | All | All | COMPLETE | 0 P1, 2 P2, 2 P3. See tests/sim_run22_report.md |
| PP-232-PROP | PP-232 propagation — all params + glossary + scale transitions updated | ALL | CROSS | All | All | — | — | Complete | Terminology renames + formula corrections applied |
| PP-233-PROP | PP-233 mass combat unit formula established + propagated | ALL | CROSS | Size, Power, Discipline, Command, H | All | — | — | Complete | Pool/Health/Damage formula committed; SIM-DEBT-03 logged |

## SIM-DEBT-02
| SIM-DEBT-03 | Full re-simulation under two-genre system with integer bonus dice | PP-234 | All prior SIM-D baselines invalidated | P1 |
| SIM-DEBT-04 | Adjudicator-type pool variation (Cha×2, Att×2) calibration | PP-234 | New pools untested | P1 |
- **Item:** ED-120 — Dissolution at RS<24 Rupture probability
- **Finding:** 90.3% Rupture rate at Relational scale in mass battle is likely miscalibrated
- **Suspected cause:** FR surcharge exemption (PP-196) stacking with mass battle Ob + RS stress modifier
- **Required:** Recalibration simulation isolating FR surcharge contribution at mass battle scale
- **Blocks:** Disclosure/gate ruling for Dissolution at RS<24
- **Registered:** 2026-04-03
| SIM-H-01 | Leap, Diagnosis, Forgetting, Appeal, Debate/CLASH, Circles, Domain Actions, Hybrid Season | Hybrid | PRES | Crown, Church, Guilds, Hafenmark, Revolution, Varfell | Torben, Halvard | Scholar-Practitioner, Soldier-Agent, Church-Renegade, Guilds-Fixer | COMPLETE | F-H01–F-H09 — 9 findings; 5 gaps flagged |
| SIM-H-02 | Forgetting Check stacking, TS cliff at multiples of 20 | TTRPG | PRES | Coherence, TS | None | Practitioner-Scholar | COMPLETE | SIM-H-02-F1/F2; GAP-H-01 |
| SIM-H-03 | Crown covert PP-236 corrected pool, Crown-Lowenritter delegation | Hybrid | PRES | Faction Intel, Crown Influence | Crown, Lowenritter | None | COMPLETE | SIM-H-03-F1/F2; PP-241 |
| SIM-H-04 | Debate AMPLIFY, combined pool, degenerate cap | TTRPG | PRES | Conviction Track | Crown, Church, Guilds | Halvard, Solt | Church-Renegade, Guilds-Fixer | COMPLETE | SIM-H-04-F1; GAP-H-02; PP-242 |
| SIM-H-05 | Locking Structural scale, RS chronic drift 5-season | TTRPG | PRES/FUT | RS, Lock duration | None | None | Practitioner | COMPLETE | SIM-H-05-F1/F2/F3 |
| SIM-H-06 | Momentum auto-success + 1-result cancel, minimum pool edge | TTRPG | PRES | Momentum | None | None | Any | COMPLETE | SIM-H-06-F1/F2; PP-243 |
| SIM-H-07 | Scene-to-Mass transition, Hybrid zoom, AUD-P1-15 | Hybrid | PRES | Health, Stamina, Military | Crown, Lowenritter | Arend | Soldier-Agent | COMPLETE | SIM-H-07-F1/F2; PP-244; ED-151 |
| SIM-ARC-01 | Domain Actions, Debate, RS decay/restoration, TC thresholds, Torben Loyalty Clock, Niflhel docs (provisional), Coup triggers | TTRPG + BG notes | Multi-season, cross-arc | RS, TC, IP, Torben Loyalty, Mandate, Stability, Influence, Military, Coherence | All eight | Almud, Himlensendt, Torben, Elske, Baralta | IP-A–IP-F irrational archetypes | Complete | F-ARC-01–F-ARC-11; 3 GAPs; 1 EDITORIAL pending |
| SIM-H-08 | Debate CLASH conserved resources, solo orator | TTRPG | PRES | Conviction Track, TC | Church | Halvard | Church-Renegade | COMPLETE | SIM-H-08-F1; non-greedy stalemate |
| SIM-H-09 | Circles, Belief conflict, evidence chain | TTRPG | PRES | Momentum, Belief | Crown | Aldric, Torben | Soldier-Agent | COMPLETE | SIM-H-09-F1/F2; Belief rewrite trigger |
| SIM-H-10 | Past-Oriented Pull, TS cliff at 60, non-aggressive withdrawal | TTRPG | PRES/PAST | RS, TS, Coherence, TPS | None | None | Scholar-Practitioner | COMPLETE | SIM-H-10-F1/F2/F3; ED-161 |
| SIM-H-11 | Appeal, Domain Echo PP-252, Belief avoidance CP check | TTRPG | PRES | Guilds Intel, Mandate | Guilds, Hafenmark | Vennrich Solt | Guilds-Fixer | COMPLETE | SIM-H-11-F1/F2/F3; GAP-H-06 |
| SIM-H-12 | PP-248 Discipline degradation validation, Battle Plans PP-235, Domain Echo | Mass/TTRPG | PRES | Size, Discipline, Morale, Military | Crown, Varfell | Arend advisory | Soldier-Agent | COMPLETE | SIM-H-12-F1/F2/F3; PP-248 validated |
| SIM-H-13 | PP-253 Collective Forgetting Anchor, Territorial Mending, Coherence arc | TTRPG | PRES | RS, Coherence, TS, Forgetting | None | Mira, Dagmara | Scholar-Practitioner, Church-Renegade | COMPLETE | SIM-H-13-F1/F2/F3/F4; ED-162 |
| SIM-ARC-02 | TC Territory Seizure, Sovereign Authority Doctrine, Thread Sensitivity growth, Discovery Event, Resonant Style shift, Olafsson evidence chain, Royal Decree, Einhir constraint, Excommunication (partial) | TTRPG primary | Multi-season, cross-arc | TC, RS, Torben Loyalty, Mandate, Stability, Influence, TK | All eight | Almud, Baralta, Himlensendt, Olafsson, Klapp, Vaynard, Elske | NG-A–NG-F non-greedy archetypes | Complete | F-ARC2-01–F-ARC2-16; 2 systemic findings |
| SIM-X-29 | Debate, Exchange structure, Memory bonus, Genre/Orientation, CROSS/CLASH | TTRPG | PRES | Composure, Conviction Track | Church, Hafenmark | Aldric Barr, Selde Mehn | Citation-fisher vs Genre-misreader | COMPLETE | F-29-01 to F-29-05; GAP-SIM-X29-01 |
| SIM-X-30 | Thread operations, Leap, Weaving, RS, Coherence, Partial stacking | TTRPG | PRES | RS, Coherence, Composure, TPS | None | Kael Vorn, Deva Shan | Over-extending veteran, eligibility-blind novice | COMPLETE | F-30-01 to F-30-05; GAP-SIM-X30-01 to X30-03 |
| SIM-X-31 | Mass Battle, Personal Combat, General Duel, Command Pool, wrong-flank PC | Hybrid | PRES | Cohesion, Morale, Health, Wounds, Command Pool | Crown, Varfell | Arend, Vath, Mira Sondhal | Duel-priority general, wrong-flank PC | COMPLETE | F-31-01 to F-31-04 |
| SIM-X-32 | BG Accounting, TC thresholds, Policy Instrument, RS decay, Restoration counter-pressure | BG | PRES | TC, RS, IP, all faction stats, Standing | Crown, Church, Hafenmark, Restoration | None | Threshold-adjacent caution, Policy Instrument delay | COMPLETE | F-32-01 to F-32-05 |
| SIM-X-26R | Personal Combat (re-sim) | TTRPG | PRES | Health, Wounds, Stamina, Momentum | None | Davan, Solmund, Maret | SATISFY, MOMENTUM-HOARDER, MARTYR, RISK-AVERSE | COMPLETE | F01-F05; GAP-G01-G02; ED-171 |
| SIM-X-27R | Hybrid Domain Season (re-sim) | Hybrid | PRES | TC, Mandate, Intel | Crown, Church, Hafenmark | PC (generic) | RITUAL, FACTION-LOYAL, FACTION-OPPORTUNIST, BELIEF-FIXED | COMPLETE | F01-F05; GAP-G01-G02; PP-257-258 |
| SIM-X-28R | BG Multi-Faction (re-sim) | BG | PRES | TC, Mandate, Wealth, Stability, Public Instability | Crown, Church, Hafenmark, Varfell, Restoration Movement | None | FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST, RISK-AVERSE, MARTYR | COMPLETE | F01-F06; GAP-G01-G02; ED-172 |
| SIM-IXC-01 | Canon P-01–P-15, Core Dice, Momentum | ALL | CROSS | Momentum, Coherence | None | None | Practitioner, Combatant | COMPLETE | IXC-01-F2(P2); IXC-01-G1,G2,G3(GAP) |
| SIM-IXC-02 | Core Dice, Threadwork v25, Leap, TPS, RS, Focus | TTRPG | CROSS | RS, Coherence, Composure, TPS, Momentum | None | Generic Practitioner | Practitioner (low/avg/high) | COMPLETE | IXC-02-F1(P1-amended),F2,F4(P2); IXC-02-G1,G2(GAP) |
| SIM-IXC-03 | Core Dice, Personal Combat v1, Weapon Matrix, Damage | TTRPG | PRES | Health, Wounds, Stamina | None | Generic combatants | All weapon archetypes | COMPLETE | IXC-03-F3(P1),G1(GAP-P1); F1,F2,F5(P2); G2(GAP) |
| SIM-COMP-01 | Contest CROSS asymmetry, non-optimal Belief CP, Domain Echo, TC advance, Shifting Object, document-as-target | Full Hybrid | PRES | RS, TC, IP, Composure, Certainty, Conviction Track | Crown, Church, Varfell, Guilds, Niflhel, Lowenritter | Halvard J, Signe M, Elan V, Lotte B | Bureaucrat, Intel-Officer, Doubting-Inquisitor, Enforcer | COMPLETE | F-C01–F-C15; PP-301–303; ED-171–173 |
| SIM-ARC-03 | Parliamentary Vote, Torben Loyalty Clock, Maret Loyalty, Ceiral Ritual (POP Foundational), Guilds financing, Lenneth channel, RS×3 consequence, IP threshold | TTRPG primary | Multi-season, 1-scene windows | IP, TC, RS, Torben Loyalty, Maret Loyalty, Mandate, Stability, Influence, Wealth, Thread Sensitivity | All eight | Almud, Lenneth, Torben, Vaynard, Maret, Baralta | NG-G–NG-L new non-greedy archetypes | Complete | F-ARC3-01–F-ARC3-18; 3 systemic findings |
| SIM-SOC-01 | Grand Contest + CT + AMPLIFY + initiative + Composure + non-optimal archetypes | TTRPG | Single session (7 exchanges) | CT, Composure, Momentum | Church, Crown, Hafenmark | Church Adv, Crown Adv | Status-Preserving, Impulsive, Fatigued | Complete — P1 resistance formula (PP-278), P1 Fatigued AMPLIFY refusal |
| SIM-COMP-02 | Multi-Party Contest PP-280, Feigned Retreat PP-256, Mass Mismatch PP-274, Untrained Leap PP-281, Ethical Framework Ob live, BG Victory Race, Dual Win-Conditions | Full Hybrid+BG | PRES | RS, TC, IP, AER, TD, Composure, Certainty, Conviction Track (×2) | Crown, Church, Hafenmark, Varfell, Guilds, Lowenritter | Ravn, Mads, Elan, Halvard | Parliamentary-Advocate, Untrained-Practitioner, Sincere-Confessor, Survival-Mercenary | COMPLETE | F-S01–F-S11; PP-280–281; ED-177–180; GAP-S-01 |
| SIM-ECON-01 | Domain Actions, Seasonal Accounting, Wealth degradation, anti-death-spiral floor, ethical framework Ob mods, stat caps | TTRPG | 3 seasons | M I W Mil Sta (Crown); Guilds W | Crown (Overextended), Church, Guilds, Varfell | None | Overextended | Complete — P1 DA timing gap (PP-280), P2 Wealth cap asymmetry (PP-281) |
| SIM-IXC-05 | Attributes, Combat Pool, Opposed Resolution, Damage | TTRPG | PRES | Health, Wounds, Stamina | None | Generic combatants | Min/avg/max builds | COMPLETE | IXC-05-F2(P2) |
| SIM-IXC-06 | Spirit/Attunement/Focus → Threadwork, Leap | TTRPG | CROSS | RS, Coherence, TPS, Composure | None | Generic Practitioner | Thread builds | COMPLETE | IXC-06-F2(P2); IXC-06-G1(GAP) |
| SIM-IXC-07 | Charisma/Bonds → Debate/Social | TTRPG | PRES | Composure | None | None | Social builds | PARTIAL-BLOCKED | IXC-07-F1(P1); G1,G2,G3(GAP) |
| SIM-RES-01/02/03/04 | Rescue eligibility, double exposure, payoff calibration, edge cases | TTRPG | PRES | Health, Wounds, Stamina, Momentum, Fibonacci | None | Generic 3v2 actors | SATISFY, MARTYR, RISK-AVERSE | COMPLETE | PP-290 (P1×4); ED-290 (P2, open); RES-02-F02/F03 design-valid |
| SIM-FM-01/02, SIM-RES-05/06/07 | Feint partial commit, Rescue contested roll, payoff calibration | TTRPG | PRES | Health, Wounds, Defence allocation, Momentum | None | Generic actors | GREEDY, RISK-AVERSE | COMPLETE | PP-291 (Feint partial commit); PP-292 (Rescue contest+payoff); ED-291 resolved; FM-02-F02/RES-05-F02/RES-06-F03 design-valid |
| SIM-PLAY-RES-01/02 | Rescue 3v2 full scenario | TTRPG | PRES | Health, Wounds, Momentum, Fibonacci | None | Aldric, Maret, X/Y/Z | MARTYR, SURVIVAL-FLOOR, GREEDY | COMPLETE | RES-PLAY-F01 P2 (TN5 near-impossible); F02 MARTYR pivot gap; F03 OK; F04 ED-292 open |
| SIM-FEINT-A/B/C/D | Feint chains, vs-Feint, minimum commit, incapacitation | TTRPG | PRES | Health, Wounds, Defence ceiling | None | Generic actors | GREEDY, RISK-AVERSE | COMPLETE | FEINT-F01 OK; F02 OK; F03 P1→PP-293; F04 OK; F05 P1→PP-293 |
| SIM-BG-MANDATE | BG Mandate suppression ceiling, coalition viability, endgame lock | BG | PRES | Mandate, Stability, TC | Crown, Church, Hafenmark, Varfell | None | FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST | COMPLETE | F01-F04 P1; ED-293 open (4 options); Church M7 win-lock confirmed |
| SIM-SC-BASELINE | Social Contest new attribute baselines (SIM-DEBT-03/04) | TTRPG | PRES | Composure, Conviction Track | None | Scholar, Diplomat, Demagogue | GREEDY | PARTIAL | SC-F01 OK; SC-F02 P2 GAP (Conviction Track length); SC-F03 P1 (Demagogue non-viable in CLASH) |
| SIM-PI-CASCADE | PI revolt cascade | BG | PRES | Public Instability | All | None | — | BLOCKED | GAP PI-CASCADE-01/02 — threshold values missing; SIM-DEBT-08 opened |
| SIM-DISSONANT | War-scale Dissonant Thread effects | Hybrid | PRES | Coherence, RS | All | Practitioners | — | BLOCKED | GAP DISSONANT-01 — war-scale rates not parameterised; SIM-DEBT-06 carried |
| SIM-FM-03 | Feint versus roll, initiative premium, pool reduction | TTRPG | PRES | Health, Wounds, Defence pool | None | Generic A/B actors | GREEDY, RISK-AVERSE | COMPLETE | FM-03-F01/F02 OK; F03 P1→PP-294 (floor); F04 OK (all-in viable) |
| SIM-RES-08 | Rescue Momentum wound trigger calibration | TTRPG | PRES | Health, Wounds, Momentum | None | Aldric, Maret | MARTYR, GREEDY | COMPLETE | F01 P1→PP-295 (cap 1/round); F02/F03 OK |
| SIM-BG-02 | BG Mandate suppression Options A+B combined | BG | PRES | Mandate, Stability | Crown, Church, Hafenmark, Varfell | None | FACTION-LOYAL, RITUAL, FACTION-OPPORTUNIST | COMPLETE | F01 OK (gradient valid); F02 OK; F03 P2 (coalition auto-trigger); F04 OK — PP-296 applied |
| SIM-DEBT-03 | Contest re-sim: CLASH/REINFORCE/CROSS/AMPLIFY baselines, two-genre system | TTRPG | PRES | Composure, Concentration, Conviction Track | Crown, Hafenmark | Scholar, Diplomat, Demagogue | GREEDY, SATISFY | COMPLETE | SC-03-A F01/F02 P1→ED-295; SC-03-B F01 P1→ED-296; SC-03-C OK; SC-03-D F01 OK; F02 P2→ED-297 |
| SIM-DEBT-04 | Adjudicator pool variation baselines | TTRPG | PRES | Composure, Conviction Track | Crown, Hafenmark | Scholar, Diplomat | GREEDY | COMPLETE | SD-04-F01 OK; SD-04-F02 P2→ED-297 (Crowd/NoAdj indistinct at low Cha/Att divergence) |
| SIM-DEBT-07 | — | Status unverifiable. Referenced in mid-campaign hybrid session (ED-180) as "RS×3 PP-225 trained practitioner in mass combat." No test file committed. If PP-225 RS×3 mechanic is current, re-test under SIM-DEBT-03 scope. |

## 2026-04-04 Simulation Backfill
| ID | Description | Mode | Status | Date | Notes |
|----|------------|------|--------|------|-------|
| SIM-D-05 | Debate re-sim under PP-232 pool (SIM-DEBT-01 resolution) | TTRPG | COMPLETE | 2026-04-04 | Corrected pool: (Cognition×2)+History. New baselines committed. |
| SIM-C-01 | Full TTRPG campaign (8 seasons, 4 PCs, all systems) | TTRPG | COMPLETE | 2026-04-04 | Combat, debate, threadwork, mass battle, factions. Satisficing PCs. |
| SIM-MB-01 | Mass battle + Thread integration | TTRPG+HYB | COMPLETE | 2026-04-04 | Thread operations during mass combat. |
| SIM-SOC-01 | Grand Contest — non-optimal archetypes | TTRPG | COMPLETE | 2026-04-04 | PP-278/279 resistance formula fix. |
| SIM-ECON-01 | Seasonal economic cascade — Overextended faction | BG | COMPLETE | 2026-04-04 | Wealth/Stability/Mandate interdependency. |
| SIM-STRESS-04 | Debate stress test | TTRPG | COMPLETE | 2026-04-04 | Multi-archetype. |
| SIM-STRESS-05 | Combat stress test | TTRPG | COMPLETE | 2026-04-04 | Wound/Stamina/pool edge cases. |
| SIM-STRESS-06 | Mass battle + faction play | TTRPG+BG | COMPLETE | 2026-04-04 | PP-285 Rescue finding. |
| SIM-COMP-02 | Full campaign Season 9 | TTRPG | COMPLETE | 2026-04-04 | PP-280-281, 20 editorials closed. |
| SIM-RES-01–04 | Rescue stress test (4 scenarios) | TTRPG | COMPLETE | 2026-04-04 | PP-290 eligibility, double exposure. |
| SIM-RES-05–08 | Rescue+Feint combined (4 scenarios) | TTRPG | COMPLETE | 2026-04-04 | PP-291-292 Feint/Rescue rebuild. |
| SIM-FM-01–03 | Feint+Mandate batch (3 scenarios) | TTRPG+BG | COMPLETE | 2026-04-04 | PP-293-296. |
| SIM-SC-BASELINE | Contest CLASH/REINFORCE/CROSS/AMPLIFY baselines | TTRPG | COMPLETE | 2026-04-04 | SIM-DEBT-03 partial. P1 findings: ED-295/296/297. |
| IXC-05–07 | Attribute propagation chains (3 scenarios) | CROSS-MODE | COMPLETE | 2026-04-04 | ED-194-197 flagged. |
| SIM-X-33–36 | Intensive batch C (4 scenarios, non-optimal actors) | ALL | COMPLETE | 2026-04-04 | 19 findings, 7 gaps resolved, 4 new gaps. |
| SIM-HYB-SEASON | Mid-campaign hybrid season (full, with flowcharts) | HYBRID | COMPLETE | 2026-04-04 | PP-286-335. 88 editorials resolved. |
| SIM-ARC-01–20 | Emergent narrative arcs with irrational players (20 arcs) | ALL | COMPLETE | 2026-04-04 | PP-246-262 applied. Non-optimal decision protocols. |
| SIM-NONOPT-01 | Non-optimal actor simulations across modes | ALL | COMPLETE | 2026-04-04 | 16-protocol library. PP-257-296. |


## 2026-04-07 Comprehensive Multi-System Stress Test
| ID | Description | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|----|------------|------|----------|--------|----------|------|------------|--------|---------|
| SIM-BG-01 | TC pacing: Church vs Hafenmark suppression S1–S20 | BG | PRES/FUT | TC | Church, Hafenmark | Himlensendt, Baralta | Expansion vs Suppression | COMPLETE | P2: Hafenmark suppression worth ~6 seasons; Assert mandatory post-TC50 removes decision cost |
| SIM-BG-02 | Church Seizure Ob range — territory immunity analysis | BG | FUT | TC, CV | Church | Himlensendt | Territorial Expansion | COMPLETE | P1: Fort3+CV0=de facto seizure immunity (Ob 8, <2% success rate); no mechanic to reduce Fort level pre-seizure; ED-candidate-G |
| SIM-BG-03 | Crown TCV 18 bottleneck — late-game victory feasibility | BG | FUT | TCV, IP, PI | Crown | Generic Crown | Hegemonic Expansion | COMPLETE | P1: "Suppress all rivals" undefined — Crown victory unresolvable; ED-candidate-A |
| SIM-BG-04 | PI collapse cascade — Löwenritter coup chain | BG | MID | PI, TC, Coup Counter | Crown, Löwenritter, Church | Ehrenwall, Almud | Institutional Collapse | COMPLETE | P1: PI≤2 TC+2 interacts with frozen TC undefined; coup window narrow at PI 3–4; ED-candidate-B |
| SIM-BG-05 | RS passive decay — time to Rupture without Warden Cooperation | BG | FUT | RS | All | Generic | Passive/Negligent | COMPLETE | P2: RS 40 band entry ~S40–44; Rupture not near-term threat; +2 Ob to all non-Thread is real consequence |
| SIM-HY-01 | Domain Echo stacking — same-scene multiple echoes | Hybrid | CROSS | Faction Mandate, Influence | Crown, Church | Almud, Himlensendt | Politician, Churchman | COMPLETE | P1: Per-echo cap reset enables +4 Mandate in one scene; ED-071 must resolve; ED-candidate-C |
| SIM-HY-02 | Zoom In at illegal phase entry | Hybrid | PRES | Phase state | Any | Generic | Any | COMPLETE | P2: No rule for illegal Zoom In consequence; mid-Phase-6 Domain Echo undefined; ED-candidate-D |
| SIM-HY-03 | Scope shift Inspiration cost interaction | Hybrid | PRES | Inspiration | Any | Generic | Any | COMPLETE | CLEAN: linear Inspiration cost coherent |
| SIM-MC-01 | Command cap degenerate — Size 7 Command 2 horde | TTRPG/BG | PRES | Unit Health, Discipline | Generic | Generic General | Levy Horde | COMPLETE | P1: 7:3 numerical advantage becomes 4D:6D disadvantage; Size>Command has zero offensive benefit; ED-candidate-E |
| SIM-MC-02 | Heavy Infantry vs Light Infantry asymmetric engagement | TTRPG | PRES | Unit Health, Size | Generic | Generic Commanders | Matched Forces | COMPLETE | P2: HI destroys 2:1 LI advantage; flanking counter mechanics unconfirmed |
| SIM-MC-03 | Morale cascade from general death | TTRPG | PRES | Morale, Size | Generic | Generic General | Command Disruption | COMPLETE | P2: cascade over 2–3 rounds; secondary commander Morale floor inheritance undefined |
| SIM-DB-01 | CLASH dominant strategy — Revealing vs Obscuring | TTRPG/Hybrid | PRES | Conviction Track | Crown, Hafenmark | Almud, Baralta | Politicians | COMPLETE | P2: Revealing strictly dominates Obscuring in CLASH; rational players never choose Obscuring in CLASH |
| SIM-DB-02 | AMPLIFY vs high-resistance audience — stalemate detection | TTRPG | PRES | Conviction Track, Composure | Church+Crown, Hafenmark | Himlensendt+Almud, Baralta | Alliance Debate | COMPLETE | P1: low pool + non-primary genre = zero movement AND zero Composure damage = irresolvable stalemate; ED-candidate-H |
| SIM-DB-03 | Composure bleed rate — median pool concession threshold | TTRPG | PRES | Conviction Track, Composure | Crown, Varfell | Almud, Vaynard | Politician, Epistemic | COMPLETE | CLEAN: 13D vs 10D resolves in 2–4 exchanges; resistance correctly calibrated |
| SIM-PC-01 | Weapon TN cliff — TN5 vs TN8 comparative analysis | TTRPG | PRES | Health | Generic | Generic Combatants | Duelists | COMPLETE | P2: Critical Hit frequency advantage TN5 vs unarmoured; TN8 vs armoured — armour-contextual, good design |
| SIM-PC-02 | Initiative information value — flip probability | TTRPG | PRES | Stamina/Health | Generic | Generic | Duelists | COMPLETE | CLEAN: initiative tactical modifier ~15–20% efficiency gain; not decisive |
| SIM-PC-03 | Wound accumulation — non-functionality threshold | TTRPG | PRES | Health, Wounds | Generic | Generic Combatant | Sustained Fighter | COMPLETE | P2: pool floor 5 = zombie fighter at 8+ wounds; Ob penalty at high wound counts needed; ED-candidate-F |


## 2026-04-07 Proposed Mechanic Stress Tests
| ID | Description | Mode | Temporal | Tracks | Factions | Status | Findings |
|----|------------|------|----------|--------|----------|--------|---------|
| SIM-PP-01 | PP-428 Piety Spread: CV gain rate vs seizure timeline | BG | FUT | TC, CV | Church | COMPLETE | CLEAN: AP >= 1 gate prevents carpet-bombing; Consul opportunity cost real |
| SIM-PP-02 | PP-429 Active Inquisition: AP accumulation rate | BG | PRES/FUT | AP | Church | COMPLETE | P2: First Inquisitor threshold undefined → ED-322 |
| SIM-PP-03 | PP-431 Parliamentary Challenge: TC suppression stacking | BG | PRES/FUT | TC | Church, Hafenmark | COMPLETE | P1: Stacks with structural suppression → negative TC → correction PP-431-COR |
| SIM-PP-04 | PP-433 Royal Charter: Ob range and charter count | BG | PRES | TCV | Crown | COMPLETE | CLEAN: 3-charter cap appropriate; Seizure +1 Ob defensively meaningful |
| SIM-PP-05 | PP-438 VTM Discretion: TC suppression vs PC cost | BG | FUT | TC, PC | Varfell | COMPLETE | P2: Weak at VTM 3, strong at VTM 5; cost scaling needed → ED-323 |
| SIM-PP-06 | PP-441 Counter-Narrative: TC stacking analysis | BG | PRES/FUT | TC | Varfell, Church | COMPLETE | P1: Stacks with Hafenmark suppression → negative TC → correction PP-441-COR |
| SIM-SC-01 | Social Contest: Argue pool, CT movement, Concentration, Doubt Marker, interaction types, genre weights, cross-mode (BG/Hybrid/TTRPG) | A+D+J+L | TTRPG/BG/Hybrid | CT, Concentration, Composure, Strain, Doubt Marker | Crown, Church, Hafenmark, Varfell, Guilds, Restoration | Partial — TTRPG+BG+Hybrid tested | P1: genre dominant strategy, interaction type doc conflict, resistance formula conflict, TIE/DIVERGENCE contradiction, Obscuring OW ambiguity, §3.8 P-01 risk; P2: Focus trap, Regroup cost asymmetry, GM load, corroboration conflict, Memory bonus unverifiable |

## 2026-04-08 Social Contest Stress Test
| ID | Description | Mode | Status | Date | Findings |
|----|------------|------|--------|------|---------|
| SIM-SC-STRESS-01 | Social Contest full stress test — Modes A+B+C+D | TTRPG+Hybrid+BG | COMPLETE | 2026-04-08 | P1×5, P2×3, P3×2, GAP×5, SIM-DEBT×5. See tests/sim_social_contest_stress_v1.md |
