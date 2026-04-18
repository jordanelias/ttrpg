# Coverage Matrix — Archive
# Active summary: tests/coverage_matrix.md
# Last updated: 2026-04-14

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
| F-RM-01 | SIM-VAR-01 | RM Community Organising 42% fail rate + PP-403 creates elimination risk before first Presence (resolved by PP-460) | Resolved — PP-460 |
| F-DB-01 | SIM-VAR-03 | Forced-CLASH stalemate systemic: near-equal pools, resistance ≥ 2, ~0 CT movement per exchange | Open — ED-330 |
| F-LW-01 | SIM-VAR-04 | PI = 0 post-coup permanently blocks Löwenritter Regency (PI ≥ 4 required; Parliamentary Manoeuvre gated PI > 0) | Open — ED-331 |

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
| DOCREVIEW-BG-01 | Full BG doc review + arc review: Wealth sink, Overwhelming, params gaps PG-09/10/12, ED-048 [UNNAMED — ED-416], conviction texts, AER, P-14 gaps | BG+ALL | PRES/CROSS | RS, TC, IP, PI | All factions | All named NPCs | All | COMPLETE | PP-178 Wealth sink; PP-179 Overwhelming 2xOb; PG-09/10/12 resolved; ED-048 resolved; ED-077 resolved; ED-080-086 logged |
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
| SIM-ARC-03 | Parliamentary Vote, Torben Loyalty Clock, Maret Loyalty, Southernmost Ritual [UNNAMED — ED-416] (POP Foundational), Guilds financing, Lenneth channel, RS×3 consequence, IP threshold | TTRPG primary | Multi-season, 1-scene windows | IP, TC, RS, Torben Loyalty, Maret Loyalty, Mandate, Stability, Influence, Wealth, Thread Sensitivity | All eight | Almud, Lenneth, Torben, Vaynard, Maret, Baralta | NG-G–NG-L new non-greedy archetypes | Complete | F-ARC3-01–F-ARC3-18; 3 systemic findings |
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

## 2026-04-08 Social Contest Stress Test
| ID | Description | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|----|------------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-D-06 | Social Contest full stress test: pool isolation, CLASH, 3-exchange Formal Debate, Tribunal, strain, edge cases (Modes A+D) | A+D | TTRPG | CT, Concentration, Composure, Strain, Doubt Marker | Church, Hafenmark | Generic archetypes | Scholar, Diplomat, Advocate, Novice | COMPLETE | P1: CONFLICT-1 Obscuring incompatibly defined in design vs params; P2: EC-02 off-genre+res2 dead play; EC-05 Spent guaranteed every Grand Debate; EC-08 pivot freq CONFLICT-2; EC-11 Att1-2 mislead 44-61%; CT-01 halved resistance null at res=1; CONFLICT-3 Composure formula ED-127; P3: EC-03 initiative +8.8pp; EC-04 39% decisive first exchange; SIM-DEBT-03/04/05 opened |
| SIM-SC-02 | Social Contest: audit A–E + sim A+D on patched system (PP-449–468). Formula validation, number systems, interaction chains, gap detection, principles compliance, genre weight model verification, new mechanic edge cases. | A+D+AuditA-E | TTRPG/BG/Hybrid | CT, Concentration, Composure, Strain, Doubt Marker, Refute, Deadlock State | Crown, Church, Hafenmark, Varfell, Guilds, Restoration | COMPLETE | P1: 0 remaining (Refute Ob fixed PP-465). P2: 1 noted design intent (Concentration range). SIM-DEBT-02 open. System simulation-clean. |
| SIM-VAR-01 | RM BG arc — Community Organising, Weaving, Warden Emergence, RS | BG | 20-season arc | Mandate, Stability, RS, Presence, WC, CV | Restoration | — | RM hardest mode | Complete | F-RM-01 (P1 ED-327→resolved PP-460), F-RM-02/03/04 (P2), F-RM-05 (P3) |
| SIM-VAR-02 | Threadwork at RS 22 — Leap, Mending, Dissolution edges | TTRPG | Single scene | RS, Coherence, Ob, TPS | None | Maret Uln | TS 50 at Critical RS | Complete | F-RS-01 (P1 recovery timeline), F-RS-02/03/04 (P2/P3 ED-328) |
| SIM-VAR-03 | Debate forced-CLASH — Klapp vs Baralta, 5 exchanges | TTRPG | 5 exchanges | Composure, CT, Strain, Doubt | Church, Hafenmark | Klapp, Baralta | Matched pools, institutional authority | Complete | F-DB-01 (P1 ED-330), F-DB-02/03 (P2 ED-329), F-DB-04/05 (P3) |
| SIM-VAR-04 | Löwenritter post-coup arc S8–S16 | BG | 8-season arc | TC, RS, PI, TCV, Coup Counter | Löwenritter, Church, Hafenmark, Varfell | — | Conditional faction first run | Complete | F-LW-01 (P1 ED-331), F-LW-02/03/04/05 (P2 ED-332/333), F-LW-06 (P3) |
| SIM-VAR-05 | Hybrid Crown Zoom In — S6 T9 assault, state transfer | HYB | 2-turn battle + personal | Health, Wounds, Military, TCV, Domain Echo | Crown, Church | Marshal Edren, Inquisitor Vald | General assault + personal combat | Complete | F-HY-01 (P1 mutual annihilation), F-HY-02/03 (P2 ED-334), F-HY-04 (P3) |
| SIM-VAR-06 | Mass combat wound cascade → capture chain | TTRPG+HYB | 2 turns + personal | Health, Wounds, Size, Cohesion, Mandate | Crown, Church | Maret Elstov, Jarnstal | General capture arc | Complete | F-MC-01/02/03/04 (P2 ED-334/335/336), F-MC-05/06 (P3) |
| SIM-NEW-01 | Conviction Yield + TC cascade — formula, AER 3 bypass, TC 75 nullification | BG | Seasonal | TC, CV, AER | Church | — | Conviction Yield calibration | Complete | F-CY-01 (P1 late-game), F-CY-02/03/04 (P2) |
| SIM-NEW-02 | Partition Victory — Church + Hafenmark, S11 race | BG | 11-season arc | TC, TCV, PI, Mandate | Church, Hafenmark, Crown, Varfell | — | Partition mechanics first run | Complete | F-PT-01 (P1 TC binding), F-PT-02/03 (P2 ED-338), F-PT-04 (P3 ED-339) |
| SIM-NEW-03 | IP crisis + AER threshold — Vanguard chain | BG | 20-season arc | IP, AER, TC | All | — | IP threat calibration | Complete | F-IP-01/02 (P1 ED-340), F-IP-03/04 (P2 ED-341), F-IP-05 (P3) |
| SIM-NEW-04 | Resistance decay (new) + Crown/Hafenmark co-victory | BG + Debate | S2–S8 | CT, resistance, TCV, PI, TC | Crown, Hafenmark, Church | Klapp, Baralta | Resistance decay first test | Complete | F-RD-01 (P1 decay works), F-RD-02 (P2), F-CV-01 (P1 ED-342), F-CV-02 (P2) |
| SIM-NEW-05 | Patience Protocol full arc → VTM → Revelation Token | BG | 12-season arc | PC, VTM, Tribune, Revelation | Varfell, Crown, Hafenmark, Church | — | Varfell Intel arc first run | Complete | F-PP-01 (P1 saturation), F-PP-02/03 (P2 ED-343), F-PP-04 (P2 ED-344) |
| SIM-NEW-06 | Cultural Uprising full run (new RM win condition) | BG | 23-season arc | CV, RS, TC, T9 control | RM, Church, All | — | RM Cultural Uprising first run | Complete | F-CU-01 (P1 ED-345), F-CU-02/03/04/05 (P2/P3) |
| F-IP-01 | SIM-NEW-03 | Altonian Vanguard deployment (IP 75) has no defined mechanical effects — endpoint undefined | Open — ED-340 |
| F-CV-01 | SIM-NEW-04 | Crown/Hafenmark co-victory achievable from S2 — Hafenmark needs 1 territory; Church has no counter-play at that timeline | Open — ED-342 |
| F-CU-01 | SIM-NEW-06 | Cultural Uprising pool undefined — Weaver TS 18 cannot Leap; Uprising pool formula needed | Open — ED-345 |

## 2026-04-08 BG Full Stress Test
| ID | Description | Mode | Status | Date | Findings |
|----|------------|------|--------|------|---------| 
| STR-BG-STRESS-01 | Board Game full stress test — Modes A+D, all mechanics | BG | COMPLETE | 2026-04-08 | P1x5 (Overwhelming threshold, TCV numbering, Crown TCV, Torben start, Seizure Ob), P2x10 (AER dominant, Challenge<structural, Weaving Ob, Conviction Yield dead zone, AER/Challenge, Total Domination, Accounting crunch, Church unreachable, Crown early TCV, Diplomatic Token), P3x4. New ED-327-330. New PP-469-475. SIM-DEBTx6. See tests/sim_stress_bg_2026_04_08.md |

## 2026-04-08 RM Founding Mechanic (PP-478)
| ID | Description | Mode | Status | Date | Findings |
|----|------------|------|--------|------|---------| 
| DESIGN-RM-01 | RM Founding Mechanic — design propagation | BG+Hybrid | COMPLETE | 2026-04-08 | PP-478 applied. RM not playable in BG. Hybrid: mid-game founding via PW track. Co-victories restricted to Hybrid post-Founding. WA emergence struck. |

## 2026-04-08 BG Remaining SIM-DEBT (BG-03 through BG-06)
| ID | Description | Mode | Status | Date | Findings |
|----|------------|------|--------|------|---------| 
| SIM-DEBT-BG-03 | Co-victory pairings reachability | BG | COMPLETE | 2026-04-08 | P1-08 (Crown+Hafen passive S1-2 — ED-343), P2-07 (Partition tracking — PP-479), P2-12 (Löw+Hafen zero PI margin). |
| SIM-DEBT-BG-04 | Faction unique action balance | BG | COMPLETE | 2026-04-08 | F-Church-01 (Cardinal Focus dominant), P2-09 (VTM TC — ED-345), P2-10 (Decree Fragmentation — ED-344). |
| SIM-DEBT-BG-05 | Ministry NPC AI interaction | BG | COMPLETE | 2026-04-08 | P2-08 (Priority 3 dead — ED-346), P2-11 (Domain conflict — PP-480). |
| SIM-DEBT-BG-06 | RS decay 20-season projection | BG | COMPLETE | 2026-04-08 | CLEAN — system healthy. WC >= 2 critical S8+. Thread-RS-RM feedback loop confirmed intentional. |


## SIM-GS-01 — Church Graduated Seizure (PP-494) — 2026-04-09
Modes: A + D + J + L
Source: tests/sim_graduated_seizure_SIM-GS-01.md
P1 findings: 5 (ED-365, ED-366, ED-368, L2-Casus Belli GAP, J3-Fort Level vs ED-355)
P2 findings: 7
Status: COMPLETE

### P1 Findings Summary
| ID | Finding |
|----|---------|
| ED-365 | Graduated Seizure pre-TC 75 availability gate ambiguous |
| ED-366 | PP-421 vs PP-494 OW CV cap contradiction |
| ED-368 | Battle trigger on Graduated Seizure unspecified |
| J3/ED-355 | Fort Level omitted from PP-494 Ob — conflict with PP-421 |
| GAP-CB | Casus Belli undefined — mechanic entirely missing from ruleset |


## SIM-MB-01 — Mass Battle (mass_battle_v3.md + params_mass_combat.md) — 2026-04-09
Modes: A + D
Source: tests/sim_mass_battle_SIM-MB-01.md
P1 findings: 3 (ED-351, ED-352, ED-353)
P2 findings: 12
P3 findings: 3
Status: COMPLETE

### P1 Findings Summary
| ID | Finding |
|----|---------|
| ED-351 | Discipline degradation: 3 conflicting trigger definitions |
| ED-352 | Volley Phase pool: "Effective Power" undefined |
| ED-353 | Command per sub-unit: explicit rule text needed |

## SIM-DIPL-01 — Negotiations, Alliances, Treaties — 2026-04-09
Modes: A + D + J + L | Source: tests/sim_negotiations_alliances_treaties.md
P1: 7 | P2: 13 | P3: 3 | Status: COMPLETE

### P1 Findings
| ID | Finding |
|----|---------| 
| A-01-F1/D-17 | Crown Treaty Ob = target Mandate → inaccessible + negative EV vs Mandate ≥ 3 |
| A-01-F2/D-07 | Consent mechanism undefined; path deadlocked by unanimous opponent refusal |
| A-05-F1/D-08 | Non-Crown diplomacy pure social contract — undeclared design choice |
| D-12 | Coalition Pairs references Guilds/Niflhel — non-existent factions |

## SIM-TERR-01 — Territory Operations (2026-04-09)
| System | Modes | P1 Findings | P2 Findings | Patches | Status |
|--------|-------|-------------|-------------|---------|--------|
| Casus Belli | A+D+J+L | 3 | 3 | PP-500,501,517,518,524 | Applied |
| Invading Territory | A+D+J+L | 1 | 4 | PP-502,503,504,514,515 | Applied |
| Seizing Territory | A+D+J+L | 4 (carry) | 2 | PP-507,508,509,510,522,523 | Applied |
| Claiming Territory | A+D+J+L | 1 | 2 | PP-502,516 | Applied |
| Conceding Territory | A+D+J+L | 2 | 2 | PP-505,506,519 | Applied |
| Trading Territory | A+D+J+L | 1 | 2 | PP-505,520 | Applied |
| Developing Territory | A+D+J+L | 1 | 5 | PP-504,511,512,513,521 | Applied |

**Total P1: 14 | Total P2: 22 | Patches applied: PP-500–PP-524**
**Editorials raised: ED-370–ED-376 (7 items, all P2 except ED-373 P1)**

### SIM-DEBT after SIM-TERR-01
- ED-373: Altonian Vanguard stats undefined (P1) — blocks invasion simulation
- ED-370: CB gate model confirmation needed
- ED-371: Diplomatic Transfer card cost confirmation
- ED-372: Voluntary withdrawal mechanic design decision

## SIM-DIPL-02 — Diplomacy Audit + Patch Stress Test — 2026-04-09
Modes: Audit A–D + Patch Validation + Unique Scenarios
Source: tests/sim_diplomacy_audit_patch.md
Patches: PP-500–PP-512 | Editorials: ED-370–ED-373
P1 findings resolved: 7 | P2 findings resolved: 18 | P3 findings resolved: 3
New findings from unique scenarios: 2 (both absorbed into PP-503/PP-504)
Status: COMPLETE — 46/46 pre-commit checks passed

### P1 Findings Resolved
| Finding | PP |
|---------|-----|
| Crown Treaty Ob inaccessible + negative EV | PP-500 |
| Consent mechanism undefined / path deadlocked | PP-501 |
| Non-Crown diplomacy structureless | PP-503 |
| Coalition Pairs references non-existent factions | PP-504 |

## SIM-DB-STRESS-01 — Social Contest System v2 Full Stress Test — 2026-04-09
Modes: A + D + J + L
Source: tests/sim_debate_stress_01.md
P1 new: 3 (D-04, D-05, L-05) | P2 new: 9 | P3: 3 | CLEAN: 4
Patches applied: PP-525, PP-526, PP-527, PP-528
Editorials raised: ED-377 through ED-382

### P1 Findings
| ID | Finding | Action |
|----|---------|--------|
| D-04 | TIE/CROSS no-strain exception missing from params Interaction Types table | PP-525 applied |
| D-05 | OBSCURING WIN "any exchange" conflicts with CROSS no-winner structure | PP-526 applied |
| L-05 | §11 Hybrid text does not cite PP-256; BG layer resolution path appears open | PP-527 applied |

## SIM-TERR-02 — Territory Operations Round 2 (2026-04-09)
| Scenario | Modes | P1 | P2 | Patches | Status |
|----------|-------|----|----|---------|--------|
| CB under campaign conditions | A+D | 1 | 3 | PP-533,535 | Applied |
| Diplomatic Transfer exploitation | A+D | 2 | 4 | PP-531,532 | Applied |
| Contested territory cascade | A+D+J+L | 4 | 4 | PP-527,528,534,536 | Applied |
| Post-Battle retreat chain | A+D | 2 | 3 | PP-529,530 | Applied |
| Church Graduated Seizure updated Ob | A | 0 | 2 | PP-537 | Applied |
| TCV audit | — | 2 | 1 | PP-525,526 | Applied |

**Total P1: 9 | Total P2: 22 | Patches: PP-525–PP-537 (13 patches)**
**Editorials raised: ED-377–ED-381 (5 items; ED-377 is P1 — CV starting values)**

### Cumulative SIM-DEBT after SIM-TERR-01 + SIM-TERR-02
- ED-373: Altonian Vanguard stats (P1 — blocks IP clock sim)
- ED-377: CV starting values (P1 — blocks Church/RM simulation)
- ED-370: CB gate model confirmation
- ED-378: Contested state decay decision
- ED-379: Diplomatic Transfer card cost
- ED-380: Voluntary strategic withdrawal
- ED-381: CV ratchet (intentional design confirmation)

## SIM-MB-02 — Mass Battle Scenario + Patch Audit — 2026-04-09
Modes: C (scenario) + Mode A re-run with provisional decisions
Source: tests/sim_mass_battle_SIM-MB-02.md
P1 findings: 1 (ED-358 — §A.8 claim contradicted by simulation)
P2 findings: 3 (Coherence warning, PP-273 applicability, Shield Wall differential)
PP applied: PP-500 through PP-504
ED resolved: ED-351 (PP-502), ED-352 (PP-503), ED-353 (PP-504), ED-356 (PP-500), D-15-F1 (PP-501)
Status: COMPLETE

## SIM-DIPL-03 — Unique Scenarios Batch 2 + Interdependency — 2026-04-09
Modes: C + D | Scope: Post-patch interdependency chains
Source: tests/sim_diplomacy_batch2.md
Remediation: PP-512–524 register + pbg blocks (PP numbering collision fixed)
New patches: PP-525–528
P1 resolved: 1 | P2 resolved: 3 | Clean scenarios: 4 of 8
Status: COMPLETE — 36/36 pre-commit checks passed

### Findings
| ID | Sev | Finding | Patch |
|----|-----|---------|-------|
| S9 Crown-break trigger | P2 | Crown-break trigger undefined | PP-525 |
| S10 Parliamentary motion | P1 | Diplomatic Alignment effect inoperable | PP-526 |
| S13 Closed Pledge witnesses | P2 | Revelation witnesses ambiguous | PP-527 |
| S15 Treaty lapse timing | P2 | Lapse timing within Accounting undefined | PP-528 |

## SIM-MB-03 — Mass Battle Blocker Resolution (ED-354/355/357/358) — 2026-04-09
Modes: A (stress per blocker) + post-patch validation
Source: tests/sim_mass_battle_SIM-MB-03.md
P1 findings: 0 (all blockers resolved)
PP applied: PP-505 through PP-508
ED resolved: ED-354, ED-355, ED-357, ED-358
Open mass battle P1 blockers: 0
Status: COMPLETE

## SIM-COMPREHENSIVE-01 — Comprehensive Multi-System Batch — 2026-04-10
| ID | Description | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|----|------------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-WOUND-01 | Wound Ob penalty: pool-reduction calibration, multi-session carry-over, pool floor ambiguity | A+D | PRES | Health, Wounds, Pool | None | Generic combatants | All combat archetypes | COMPLETE | F-WOUND-01(P3 clean), F-WOUND-02(P2 GAP-WOUND-01), F-WOUND-03(P2 GAP-WOUND-02). ED-candidate-F reclassified P3. No patch. |
| SIM-AMPL-01 | AMPLIFY stalemate: low pool + non-primary genre irresolvable deadlock | A+D | PRES | Conviction Track, Composure | Crown, Church, Hafenmark | Himlensendt, Almud, Baralta | Alliance debaters, institutional authority | COMPLETE | F-AMPL-01(P1→PROVISIONAL AMPL-01), F-AMPL-02(P2), F-AMPL-03(P2 design paradox). |
| SIM-CMD-01 | Command cap: Size > Command glass cannon, no pool boost mechanism | A+D | PRES | Unit Health, Power, Pool | Generic | Generic General | Levy Horde, disciplined unit | COMPLETE | F-CMD-01(REVISED — not zero-benefit), F-CMD-02(P1→PROVISIONAL CMD-01), F-CMD-03(P2). |
| SIM-CR-01 | Calamity Radiation cross-mode integration: BG Thread tags, Hybrid echo, Surge timing, Forgetting boundary | A+G | CROSS | RS, Domain Action Ob, Thread Ob, CV | All | Generic practitioners | All archetypes | COMPLETE | F-CR-01(P1→PROV CR-01), F-CR-02(P1→PROV CR-02), F-CR-03(P2), F-CR-04(P2), F-CR-05(P3 CLEAN). GAP-CR-01 blocks RS decay precision. |
| SIM-CLK-01 | Clock Registry interaction chains: RS/TC/IP/PI/WC/WR/AER interdependency | B+G | CROSS | All shared clocks | All | — | — | COMPLETE | F-CLK-01(P2), F-CLK-02(P2 AER/AEA), F-CLK-03(P1→PROV CLK-01), F-CLK-04(P2). |
| SIM-VIC-01 | Victory Architecture endgame race: 4-player Season 10 projection | C+D | FUT | TCV, TC, PI, RS, Mandate | Crown, Church, Hafenmark, Varfell | — | All faction archetypes | COMPLETE | F-VIC-01(P2→PROV VIC-01), F-VIC-02(P1 EDITORIAL), F-VIC-03(P2), F-VIC-04(P2), F-VIC-05(P1 CLEAN), F-VIC-06(P1 GAP-VIC-02). |
| SIM-VIC-02 | Co-victory pairings stress test post PP-528: exclusivity, timing, feasibility, cognitive load | D+L | CROSS | All | All | — | All | COMPLETE | F-CO-01(P2), F-CO-02(P1 EDITORIAL), F-CO-03(P3). 3 clean scenarios. |
| SIM-VIC-03 | RM Cultural Uprising: Phase 1 conflict, Phase 2 calibration, RS prerequisite | A+C | CROSS | CV, TC, RS, WC, WR | RM, Church | Pontifex | RM hardest mode | COMPLETE | F-VIC-RM-01(P1→PROV VIC-RM-01), F-VIC-RM-02(P2 GAP-VIC-RM-01), F-VIC-RM-03(P2 CLEAN), F-VIC-RM-04(P3). |

| BAL-VIC-01 | Victory path balance — solo + co-victory timeline normalisation | ALL | CROSS | TCV, PI, VTM, TC, CV | All | — | All | COMPLETE | PP-540–546 applied. Solo 12–16 seasons all factions. Co-victory 10–14 seasons. 7 patches. |

## NPC Behavior System — Simulation Debt (2026-04-13)

| ID | Description | Priority | Status |
|---|---|---|---|
| SIM-NPC-01 | Full BG simulation with all NPC priority trees active | P1 | OPEN |
| SIM-NPC-02 | Contest: Resonant Style +1D stacking validation | P2 | OPEN |
| SIM-NPC-03 | Arc emergence: 3-season TTRPG Almud+Himlensendt | P2 | OPEN |
| SIM-NPC-04 | Framework Drift: 6-season BG runaway check | P2 | OPEN |
| SIM-NPC-05 | Belief Scar cascade: 3+ Scars playability | P3 | OPEN |

## Arc System v8 — Simulation Debt (2026-04-13, PP-575)

All v8 additions unsimulated. Required before any v8 arc is referenced in a mechanical ruling.

| Range | Description | Status |
|---|---|---|
| TE-01 to TE-34 (31 active) | Territory Event arcs | Not simulated |
| ARC-P09 | Royal Debt | Not simulated |
| ARC-S35/S37-S40/S44/S45/S47-S49/S52/S54-S57 | New Secondary arcs | Not simulated |
| ARC-T20-T26 | New Tertiary arcs | Not simulated |
| NPC-ARC-VAY | Vaynard Unchecked | Not simulated |
| BG-CV-01 to BG-CV-05 | BG Conviction Events | Not simulated |
| COLLISION J | Church Siege of the Southern Gates | Not simulated |

## SIM-ARC-B01 — Cluster B TC Fracture (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| ARC-S29 Cardinal Schism | C+D | COMPLETE | Olafsson autonomous AP in non-Church territory; 2 consecutive schism seasons → Inquisitor in Crown military hinge |
| ARC-S56 Lions' Table Fracture | C+D | COMPLETE | P(fires | T26 triggers) ≈ 50%; sequentially dependent on T26 outcome |
| ARC-T26 Martial Honour Violation | C+D | COMPLETE | P1-B03 resolved (PP-576); priority sequence validated |
P1 findings: 1 (P1-B03 → PP-576 applied)
P2 findings: 4 (P2-B01/B02 → PP-577; P2-B03/B04 confirmed design intent, no patch)

## SIM-ARC-B02 — Season 8 Crown Card Constraint (2026-04-13)
| Arc interaction | Mode | Status | Key Finding |
|---|---|---|---|
| Crown Suppress + Hafenmark Structural TC dependency | B (Interaction) | COMPLETE | Hidden 2-card coordination requirement; PP-579 documents |
| Inquisitor AP in non-Church territory | D (Edge) | COMPLETE | Asymmetry intentional; PP-578 clarifies |

## SIM-ARC-A01 — Cluster A Baralta Programme (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| ARC-S37 Détente | C | COMPLETE | Named state collapse mechanics confirmed functional |
| ARC-S45 Deed Claim Activates | C | COMPLETE | Fires at Counter=2; NPC AI priority shift documented |
| ARC-T14 Consecration Crisis | C+D | COMPLETE | Live at Season 13; consecration→schism cascade P2-B10 |
| ARC-S24 Baralta Succession | D | COMPLETE | Fracture path (PI<4) functionally unreachable; P2-B11 |
P1 findings: 1 (P1-B08/ED-408 — Quaestio trigger definition)
P2 findings: 5 (P2-B05→PP-578; P2-B06→PP-579; P2-B07→PP-580; P2-B09→ED-409; P2-B10→ED-410; P2-B11 confirmed design intent)

## SIM-ARC-C01 — NPC-ARC-VAY Vaynard Unchecked (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| NPC-ARC-VAY | A + C | COMPLETE | Self-repeating expedition; Forgetting strips content not character; net RS zero; WC destroyed |
P1 findings: 1 (P1-C03 → PP-581 Clarity/Forgetting independence)
P2 findings: 4 (P2-C01/C05 → PP-582; P2-C02 design confirmed; P2-C04 design confirmed; GAP-C03 → PP-583)
P3 gaps: 3 (ED-411-413: Maret stats, Edeyja Resonant Style, Mending Ob confirmed)

| SIM-FW-01 | Fieldwork: Survey Ob, Evidence Track, Exposure→AP, Survey vs Consul | A+D | Multi-season | Exposure, AP, Evidence, Cover | Church | None | Exploration calibration | Complete | 2 P1, 1 P2 |
| SIM-NPC-01 | NPC Behavior: Priority Tree (Crown 5 seasons) | A | 5 seasons | TC, PI, Stability, Mandate, CC, TL | Crown | None | BG AI validation | Complete | 0 |
| SIM-NPC-02 | NPC Behavior: Belief Revision Rate | A | 20-contest campaign | Conviction Track, Composure, Scars | All | Named NPCs | Contest calibration | Complete | 0 |
| SIM-CH-01 | Character Histories: Starting skills + spark rates | A | Character creation + 10 scenes | Skills, Recall, Equip slots | None | None | Lifepath calibration | Complete | 0 |

## SIM-ARC-D01 — Cluster D Southern Corridor (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| TE-12 Collector's Chokehold | G+D | COMPLETE | RM excluded; failed negotiations = Vaynard intel; P1-D05 terminal RS path |
| TE-17 Presence at Gate | G+C | COMPLETE | −1 Ob accelerates AP but not Overwhelming; P2-D03 arc text correction |
| TE-18 Fjord Witness | C+D | COMPLETE | Preparation action near-mandatory for any Mending practitioner |
| TE-19/20 Crown Southern Gates | G | COMPLETE | No fire in Seasons 4–8; geographic loading noted |
| ARC-S15 Southernmost Spiral | G+C | COMPLETE | Season 8 activation; Maret resource conflict with Southernmost Ritual [UNNAMED — ED-416] Seasons 13–14 |
| ARC-S25 Warden Cooperation | G+C | COMPLETE | WC 2 doubles available time before Fractured; P1-D06 Forgetting Check TS-gating |
P1 findings: 2 (P1-D05→PP-586; P1-D06→PP-585)
P2 findings: 3 (P2-D01/02/03→PP-587; P2-D04 design observation)

## SIM-ARC-E01 — Cluster E RM Pressure (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| ARC-S47 Cultural Reclamation | G+C | COMPLETE | S47 and S48 mutually limiting (P2-E01/PP-591); PP-590 ambient TS development applies to account-producing communities |
| ARC-S48 Vossen Saturation | G | COMPLETE | Suspended when T6 reaches Presence 3; IDEALIST flaw delays but doesn't resolve S47/S48 tension |
| ARC-S49 Rawlsian Bind | C+D | COMPLETE | Principles Maintained correct NPC AI; Suspended near-impossible Mandate path (~11%/season); RM role confirmed Thread-substrate |
P2 findings: 4 (P2-E01/E04→PP-591; P2-E02→ED-419; P2-E03 design observation)
GAP: ED-418 (Attunement stat undefined P2)

## SIM-ARC-F01 — Cluster F Economic Web (2026-04-13)
| Arc | Mode | Status | Key Finding |
|---|---|---|---|
| ARC-P09 Royal Debt | C | COMPLETE | Charter undeliverable at Wealth 2; weakens S52 Crown offer (P2-F02) |
| ARC-S52 Feldhaus Gambit | C | COMPLETE | Varfell wins by default (Crown undeliverable, Church coercive); P2-F01 Guilds no Intel stat |
| ARC-T24 Tax Revolt | C+D | COMPLETE | Dormant Season 6 (PI < 6); Guilds 70% win rate in Contest; P2-F03 |
| COLLISION I | C | COMPLETE | P09+S52 active; TE-20 not yet (T5+T6 Crown-held); temporal sequence documented P2-F04 |
P2 findings: 4 (P2-F01→PP-593; P2-F02/F04→ED-421; P2-F03 design observation; GAP-F01→ED-420)

## SIM-ARC-G01-G05 — Cluster G Capital Territory Events (2026-04-14)
| Arc | Mode | Status | Key Finding |
|---|---|---|------|
| TE-01 T1 Valorsplatz falls | C | COMPLETE | Seizure blocked at equal Mandate (P2-G01/PP-596); TC freeze ceiling clarified (GAP-G01/PP-596) |
| TE-04 T8 Gransol falls | C | COMPLETE | Baralta 7D pool recovers T8 same season (P2-G02/PP-597); elimination + loss = ARC-S24 PI gate suspended |
| TE-05 Mineral Leverage | G | COMPLETE | Not triggered (Varfell not Church); Church path noted |
| TE-07 Crossroads Consolidates | G | COMPLETE | Suspended when T9 falls; prior VTM gain from TE-07 permanent |
| TE-08 Cathedral Falls | C | COMPLETE | Church M−3 but Seizure/TC intact (P1-G03/PP-594); ED-404 branch reached |
| TE-10 Duchy Falls Silent | C | COMPLETE | All 3 Varfell paths suspended (P1-G04/PP-598); Private Collection contested |
| TE-26 The Hinge (Coup) | C | COMPLETE | Reconstitution unavailable at PI 3 (P1-G05/PP-595); PI−3 blocks Baralta win (P2-G05/PP-597) |
P1 findings: 3 (P1-G03→PP-594; P1-G04→PP-598; P1-G05→PP-595)
P2 findings: 3 (P2-G01/GAP-G01→PP-596; P2-G02/G05→PP-597)
Editorial branches: 1 (ED-423/ED-404 Grand Debate + Quaestio — simulation stopped at branch)

## Thread System Redesign — Session 2026-04-14 (PP-600-623)
| Area | Status | Key Changes |
|---|---|---|
| Thread pool unification | COMPLETE | (Spirit×2)+History+TPS all ops |
| TN system | COMPLETE | Base 7; Binding +1; POP +1; POP Binding +2 |
| Three-axis Ob | COMPLETE | Depth(Fibonacci 1,2,3,5,8,13)+Breadth+Distance |
| Gap self-closure | COMPLETE | 5 scales; RS drain by scale; age modifier |
| RS cap | STRUCK | No ±10 cap; reality takes full consequences |
| Southernmost Ritual | STRUCK | ARC-T04 struck; no ritual exists |
| WR/WC redesign | COMPLETE | Both 0-3; WR gates WC |
| Einhir canon | COMPLETE | Foundational stabilization sites; Calamity mechanism |
| Probability corrected | COMPLETE | TN7=0.4/die; Fibonacci calibrated |
| Dissonance | COMPLETE | Spirit check mechanic; no separate tracker |
| SIM-FW-03 | Fieldwork: Disposition economy 10-session arc | A+D | 10+ sessions | Disposition, Sincerity Gate, Cover | RM | Maret Vossen | Social relationship calibration | Complete | 1 P2 (fixed PP-593) |
| SIM-FW-06 | Fieldwork: Cover derived value calibration | A | Multi-action | Cover, Exposure | None | None | Detection risk calibration | Complete | 0 |

## Fieldwork System — Simulation Debt Register (2026-04-13)

All SIM-DEBT-FW items resolved in PP-576 through PP-583.

| ID | Description | Resolved By | Key Finding |
|----|-------------|-------------|-------------|
| SIM-DEBT-FW-01 | Ob calibration across Depth 1–5 at 5 pool sizes ± hostile/foreign modifiers | PP-583 | Calibration sound: 5D→D1, 9D→D1–2, 13D→D1–3, 17D→D1–4, 24D challenges D5 |
| SIM-DEBT-FW-02 | Investigation pacing: Evidence Track 5-threshold completion times by pool size | PP-576 partial, PP-583 complete | High-pool (15–19D): 3–5 scenes at D1–3. Low-pool (9D): 4–6 scenes at D1–2. Pacing confirmed. |
| SIM-DEBT-FW-03 | Disposition economy: Neutral→Bonded timeline across 3–4 seasons | PP-583 | ~6–8 actions across 3–4 seasons. Sincerity Gate adds ~37% failure on instrumental Connect. Meaningful investment confirmed. |
| SIM-DEBT-FW-04 | Exposure → Church Attention Pool feedback rate under cap | PP-581 | Fieldwork contributes ~11% of max TC acceleration over 4 seasons. Cap (+1/char/season, +2/territory/season) is sufficient. |
| SIM-DEBT-FW-05 | Survey vs Govern action economy (niche differentiation) | PP-583 | Govern dominates mid-proximity (reliable Prosperity). Survey dominates high-proximity (safe northern territories). Neither dominates. |
| SIM-DEBT-FW-06 | Cover derived value calibration: detection risk by Cover level | PP-583 | Cover 3: detected in 3 scenes. Cover 9: full season before detection. Cover 12+: near-immune to casual detection, threatened by combat+Thread stacking. |
| SIM-DEBT-FW-07 | Transition simulation: all 6 fieldwork ↔ other-system handoff directions | PP-577 | All 6 directions functional. F-TRANS-01 through F-TRANS-12 resolved. |
| SIM-DEBT-FW-08 | Threadwork × fieldwork: Evidence Track advancement from Thread operations | PP-578, PP-579 | All ops may advance Evidence Track contextually. GM determines yield per target and intent. |
| SIM-DEBT-FW-09 | NPC arc stress tests: Domain Echo cascades from fieldwork outcomes | PP-579 | 7 Domain Echo cascades tested. NPC Disposition −2 if investigated; +1 if NPC wanted truth found. |
| SIM-DEBT-FW-10 | Extended threadwork × fieldwork (Knots, Community Weaving, threadcut beings, Mending, Dissonance) | PP-580 | Knot-mediated remote Thread-Read (+1 Knot strain/use). Non-sensitive partner Dissonance (Spirit check). Threadcut being social fieldwork (Testimonial tag). |

P1 findings from fieldwork simulation: 2 (ED-NEW-04 → CONFIRMED SAFE PP-581; ED-NEW-10 → CONFIRMED PROPORTIONAL PP-581)
P2 findings: 5 (ED-NEW-03, ED-NEW-05, ED-NEW-08, ED-NEW-13, ED-NEW-15)
P3 findings: 8 (ED-NEW-01, ED-NEW-02, ED-NEW-06, ED-NEW-07, ED-NEW-09, ED-NEW-12, ED-NEW-14 + G10-F01–F07 Godot validation)
All SIM-DEBT items: RESOLVED.

## Quick Interdependency Tests — 2026-04-13 Comparative Audit

| Test | Systems | Result | Finding |
|------|---------|--------|---------|
| Pool floor 1D consistency | Core, Combat, Contest, Fieldwork | PASS | Rule is consistently implied; formalisation in params_core safe. PP-new. |
| Let It Ride in combat | Combat | PASS | Round structure handles re-attempts. Let It Ride applies to single-declaration manoeuvres (Feint/Rescue) only. Clarifying note added §11.5. |
| Spent trigger timing | Contest | PASS | Spent fires after Step 4; penalty applies next exchange. Clarification added §4. |
| Fieldwork → Combat cross-reference | Combat, Fieldwork | PASS | F-TRANS-01/09 documented in combat §11.5. No contradiction. |
| Fieldwork Findings → Contest (Combined Findings) | Contest, Fieldwork | PASS | +1D/Finding max +2D stacks with §9.1 prep for max +3D Exchange 1 bonus. Appropriate investment reward. Documented §9.1. |
| Thread-Read-as-fieldwork | Threadwork, Fieldwork | PASS | Pool consistent (Spirit×2+Hist+TPS). Co-movement fires. Cross-reference added threadwork §2.3. |
| NPC Recruitment Procedure | NPC Behavior, Fieldwork, Contest | BLOCKED | 3 blockers: Ob formula ambiguous, defection undefined, Hooks undefined. ED-510 raised. Blocked on ED-387. |
| Faction AI decision sequence gap | NPC Behavior | BLOCKED | Gap exists because ED-387 (P1-BLOCKER Priority Trees) is unresolved. No new item; ED-387 note added. |

P1 findings from tests: 0
P2 findings: 4 (ED-510 NPC Recruitment, ED-511 Hooks, ED-512 surrender, ED-514 social initiative)
P3 findings: 1 (ED-513 combat fail-forward)
All PASS tests: patched in same commit (PP-630–634).

## Fieldwork Coverage (2026-04-13)

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-FW-TRANS | Fieldwork (Examine, Interview, Thread-Read) + Combat + Contest + Mass Battle + Thread transitions | C+D | 1 investigation arc, 4 seasonal scenes | Evidence, Exposure, Disposition, Coherence, RS, Health, Composure, TC, IP | Varfell, Crown, Church | Torsten, Signy | Non-sensitive + practitioner field pair | Complete | 5 transition rules validated; §3.9 confirmed; Desperate Trail rare at normal pool sizes (correct) |
| SIM-FW-NPC | Fieldwork + NPC character interactions; thread-read on NPCs; cover mechanics | C+B | Single session | Evidence, Exposure, TS detection tiers, Certainty, Cover | Varfell, Church | Multiple | Practitioner investigator | Complete | TS detection tiers consistent; Cover 3-12 range confirmed |
| SIM-FW-TW | Threadwork-fieldwork integration; Thread-Read pool formula (PP-626) | A+B | Single scene | RS, Coherence, TPS contribution, Contact duration | None | Signy | Practitioner investigator | Complete | Thread-Read = (Spi×2)+Hist+TPS confirmed canonical |

## Fieldwork Ob Calibration Results (SIM-DEBT-FW-01–06, all resolved)
| Item | Finding | Resolution |
|------|---------|------------|
| FW-01 | Ob calibration: 5D→D1, 9D→D1-2, 13D→D1-3, 17D→D1-4, 24D→D5 | Resolved |
| FW-02 | Evidence pacing: 3-5 scenes for threshold 5 | Resolved |
| FW-03 | Neutral→Bonded = 6-8 actions, 3-4 seasons | Resolved |
| FW-04 | AP feedback = 11% of TC max; cap sufficient | Resolved |
| FW-05 | Survey and Govern occupy different niches; neither dominates | Resolved |
| FW-06 | Cover 3 (detected in 3 scenes) vs Cover 12+ (near-immune) | Resolved |

## Session Close — 2026-04-13 Final Propagation Pass

| Item | Status |
|---|---|
| PP-633–642 registered in patch_register.yaml | ✓ |
| Opposing ops (PP-641): params_threadwork → threadwork_redesign §2.6 | ✓ |
| NPC Recruitment (PP-642): §9.5 in npc_behavior_v30. Hooks + Defection defined | ✓ |
| Findings citation: params_contest updated | ✓ |
| Surrender/disengage: params_combat updated | ✓ |
| propagation_map: PP-641/642 cross-refs added | ✓ |
| Both checkers: EXIT 0 | ✓ |
| Freshness gate: updated | ✓ |
| Open P1-BLOCKERs: 0 | ✓ |
| Open PROVISIONALs: 0 | ✓ |
| Remaining propagation pending: params_factions (Mandate −1 on recruitment); fieldwork_socializing (Hook acquisition cross-ref) | PENDING (P3, non-blocking) |


## Factions TTRPG Coverage (2026-04-13)

| Test ID | Mechanics | Status | Findings |
|---------|-----------|--------|---------|
| SIM-FAC-01 | Domain Action Ob calibration (1-7 scale) | Complete | Equal-stat NPC: 14% success (correct — PC agency matters). Ethical modifiers: ±15-20% per step. |
| SIM-FAC-02 | Unique action Ob calibration | Complete | All within range. Assassination (5D vs Ob 6) = 4% (appropriately rare). |
| SIM-FAC-03 | Edge cases: partial sheets, anti-death-spiral, TC cap | Complete | No P1. P2: 2 seasons at Stab 2 before collapse (adequate). Reference card needed for 48-step accounting. |

## Southernmost Coverage (2026-04-13)

| Test ID | Mechanics | Status | Findings |
|---------|-----------|--------|---------|
| SIM-STH-01 | Forgetting Check (TN8, Ob 1-4) | Complete | Calibrated. Non-practitioners locked out of core knowledge. TS 40+ meaningful gate. |
| SIM-STH-02 | Expedition procedure Obs | Complete | Planning 62%, Resources 36%, Zone hazards 57-80%. TS gate enforced. |
| SIM-STH-03 | Ritual Ob calibration (Ob 5) | Complete | Lead 18D+4 participants = 92% success. Rare failure is appropriately severe. |
| SIM-STH-04 | Edge cases: crisis timeline, TS gate, ED-048 name | Complete | P2: SIM-STH-E1 applied — combined TT cap (−5/season). PP-635. |

## SIM-DEBT-SOC Results (2026-04-13)
| SIM-DEBT-SOC-01 | COMPLETE | CLEAN | ED-532 resolved |
| SIM-DEBT-SOC-02 | COMPLETE | CLEAN | ED-533 resolved |
| SIM-DEBT-SOC-03 | COMPLETE | P1→PP-633 | ED-534 resolved |
| SIM-ED-519 | COMPLETE | CLEAN | PP-633 documented |

## SIM-NPC-01 Results (2026-04-13 — NPC Priority Tree Validation)
| Test ID | Mechanics | Status | Findings |
|---------|-----------|--------|----------|
| SIM-NPC-01 | Full BG NPC priority trees (5 seeds × 12 seasons) | COMPLETE | F-01 Crown Mandate spiral (PP-NPC-01), F-02 Church Influence ceiling (PP-NPC-03), F-03 Coup deterministic (PP-NPC-02), F-04 No eliminations (expected), F-05 RS slow (expected), F-06 Varfell cooldown (PP-NPC-04), F-07 Interaction loop PASS |
| SIM-NPC-02 | Contest Resonant Style +1D pool calibration | OPEN | — |
| SIM-NPC-03 | Arc emergence 3-season TTRPG | OPEN | — |
| SIM-NPC-04 | Framework Drift 6-season BG runaway | OPEN | Partially addressed by PP-NPC-03 (Church drift fix). Re-run needed. |
| SIM-NPC-05 | Belief Scar cascade playability | OPEN | — |

## Archived 2026-04-17 — Batch 5–8 (ST-21–ST-60)

## Batch 5 Confirmed Working (ST-21 through ST-30)

Victory race convergence, Grand Contest CLASH-always, Torben Conviction emergence,
arc conditioner system (env/cross-NPC/obligation all fire clean), Depth 4-5 fieldwork,
co-victory hold phase robust, TS 30→70 trajectory, 3-Obligation cascade, Church victory
revised, all 6 tactic cards + counter-formations.

## Batch 6 Scope (ST-31 through ST-40)

Settlement mechanics, Guilds victory design, 6-faction Parliamentary sim,
Altonian Vanguard, RM Founding, Elske arc, Thread collective op,
Cardinal restoration, Baralta Arc C, longevity cascade.

## Batch 6 Findings (sim_batch_6_2026-04-16) — ST-31 through ST-40

### New P1
| SIM6-01 | RM Founding mechanic missing from all docs | ED-620 |

### Resolved
| ED-612 | Guilds solo victory (Merchant Hegemony) designed and validated |
| ED-614 | Cardinal restoration conditions specified |

### New P2 EDs (621-627)
BG lobby cap, Varfell Parliamentary constraint, IP rate, Elske arc, Excommunication procedure, Accord/Order distinction, Guilds victory constraint fix.

### Confirmed Working
Guilds Merchant Hegemony (~S15-17), TC bonus equalising Parliament pools, Memory genre advantage, Thread collective op (72D Calamity reversal), Fort defense bonus, Elske pre-coup investment → Regency S17, double Priority 0 Zoom In choice, double longevity death cascade.


## Consolidation — sim sessions 2026-04-16

### Jordan Design Corrections Applied

| Correction | Impact |
|------------|--------|
| Guilds, Niflhel = spoiler/pressure factions; they do not win | ED-612, ED-627 closed as by-design |
| Löwenritter post-coup holds until new monarch faction takes over | ED-613 closed as by-design; §3.6 reframed |

### Propagations to victory_v30.md

| ED | Change | Section |
|----|--------|---------|
| ED-588 | RM holding: PT ≤ 3 (was ≤ 1). Uprising OW: T9 PT −2 added. | §3.5 |
| ED-590 | Church victory: Accord ≥ 3 in ≥ 3 non-capital territories. | §3.2 |
| — | Löwenritter design note: transitional faction, not conventional winner. | §3.6 |


## Batch 7 Summary (sim_batch_7_2026-04-16) — ST-41 through ST-50

### Resolved EDs
ED-589 (Presence marker mechanics), ED-586 (Constrained sub-arc), ED-587 (Stability Crisis Zoom In),
ED-617 (Grand Contest Recall fix), ED-621 (BG lobby cap), ED-622 (Varfell no-Senator note),
ED-626 (Accord/Order distinction), ED-623 (IP rate validated)

### New EDs
| ED-628 | Siege mechanic missing for playable factions | P2 |
| ED-629 | Partition needs Phase 1 declaration | P2 |
| ED-630 | RS Rupture needs Last Declaration scene spec | P2 |

### Batch 7 Confirmed Working
RM Presence markers (Strategy C canonical), Altonian invasion at S25 (revised IP),
Coalition rebuff IP reset, RS Critical Stability checks, HI chain 2-scene → Tribunal,
RM 30-season arc S8→S14→S15, Assert Mandate gate critical, Varfell Path C S14-15,
Intelligence Embargo coalition spoiler.


## Batch 8 (ST-51 through ST-60) — sim_batch_8_2026-04-17

### Resolved (8 + 8 prior re-sync)
ED-542,611,615,618,624,625,629,630 (batch 8)
ED-586,587,589,617,621,622,623,626 (prior sessions, now archived)

### New EDs
ED-631 (Parliamentary Stay vs Church Tribunal), ED-632 (Accord/Order co-fire), ED-633 (Siege propagation)

### Confirmed Working
Niflhel asset placement, Elske Loyalty arc, Schoenland Treaty, Excommunication procedure,
Threadcut being TS-gated, two-scale Uprising, three-faction bilateral sequential,
RM collective Weaving near-infallible, Torben window S1-8, Last Declaration scene,
Partition Phase 1 declaration, battle consequences consolidated.

## Archived from coverage_matrix.md (2026-04-17)

# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM2-01 | ST-01 | 2x Senator Assert engine too fast | ED-572 (resolved) |
| SIM2-05 | ST-06 | Post-combat fieldwork when player fled undefined | Resolved — ED-576 |
| SIM2-06 | ST-07 | Co-Movement Cards 1-15 not in canonical docs | Resolved — ED-577 |
| SIM2-07 | ST-07 | TTRPG mass battle melee damage formula implicit | Resolved — ED-578 |
| SIM2-10 | ST-03 | Social initiative deterministic vs combat rolled | Resolved — ED-581 |
| SIM2-11 | ST-03 | Chain Contest Resistance-2 stall not documented | Resolved — ED-582 |
| SIM3-04 | NPC-03 | Arc state vs Priority 6 at Mandate < 3 | ED-586 |
| SIM3-07 | Zoom In | Stability Crisis Zoom In trigger absent | ED-587 |
| SIM4-01 | ST-14 | RM Phase 2 T9 holding condition unreachable | ED-588 |
| SIM4-02 | ST-14 | RM Presence marker mechanics undefined | ED-589 |
| SIM5-01 | ST-21 | No Parliamentary block on Tribune actions | ED-616 |
| SIM5-02 | ST-22 | Grand Contest Recall: once-per-source fix | ED-617 |
| SIM5-04 | ST-23 | Torben Conviction window: S1-8 formal def | ED-618 |
| SIM5-13 | ST-28 | 3-Obligation GM advisory cap | ED-619 |

## Active P1 EDs Requiring Design Action

| ED | Description |
|----|-------------|
| ED-588 | RM Phase 2 T9 PT ≤ 1 unreachable |
| ED-589 | RM Presence marker mechanics undefined |
| ED-612 | Guilds have no solo victory condition |

## Resolved This Session

| ED | Resolution |
|----|-----------|
| ED-590 | Church victory revised + validated: TC ≥ 65 + Accord ≥ 3 in ≥ 3 non-capitals |
| ED-572 | Assert → Pontifex-exclusive |
| ED-545/551/555/557/559/571/583 | See sim_batch_3 |
| ED-539/585 | See sim_batch_3/4 |

## Throughline Analysis + Propagation — 2026-04-17

Top-down audit across all 8 batches (ST-01 through ST-60).

### Robustness: ✓ working
Victory race convergence, TC/RS pyrrhic collision, Obligation cascade, Torben investment race, Calamity reversal gate, co-victory hold, Elske subversive strategy, Niflhel intelligence market

### Robustness: ✗ gaps addressed
IP rate too mild → revised (+3/battle, +2/season TC60+); No Parliamentary block on Excommunication → Parliamentary Stay added; Guilds solo victory resolved (ED-612)

### Elegance: ✓ working
TC Reform, Church Accord governance condition, Feigned Retreat dual utility, Excommunication fait accompli, Shield Wall/Wedge counter, Depth 5 non-investigative

### Elegance: ✗ gaps addressed
Grand Contest Recall → once-per-source rule; Accord/Order invisible → clarified; IP published wrong → corrected; BG lobby pre-determination → capped at 4-6

### Smoothness: ✓ working
Zoom In/Out (cleanest system), 5-step Cascade, collective co-movement fires once, three-faction bilateral sequential, mass battle tactic cards

### Smoothness: ✗ gaps addressed
Accord/Order co-fire sequence → Order 0 first, Accord 0 second; Partition silent win → Phase 1 declaration required; Siege mechanic absent → §1.9 added; Parliamentary Stay → §10.1 added

### Propagated
social_contest: Grand Contest Recall fix, BG lobby cap, Obligation 3-cap advisory, Parliamentary Stay §10.1
victory_v30: Rupture Scene + Last Declaration, RM Presence vs Phase 1 distinction, Partition Phase 1 declaration
peninsular_strain: IP rate +3/battle +2/season-TC60, Accord/Order distinction §2.4b, co-fire sequence
mass_battle: §E Battle Consequences (canonical consolidation from 4 source docs)
military_layer: §1.9 Siege Action mechanic
scale_transitions: Stability Crisis Zoom In trigger
npc_behavior: Constrained sub-arc state, Torben Conviction window S1-8


## New Findings — sim_npc_player_batch2_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| JUS-SIM-02 | Cardinal Justice | Heresy Proceedings: authorization loop | ✓ Archived — ED-629 resolved 2026-04-17 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Vaynard Path B met at S9 from Season 1 hold — fastest single path | VAY-SIM-04 | ✓ |
| Vaynard S0 Assembly pre-garrisons T13 before Baralta can Proclaim | VAY-SIM-01 | ✓ Reinhard Principle |
| Intelligence auction: 2 major world events from S1 intel, zero Domain Actions | VAY-SIM-05 | ✓ Force multiplication |
| Baralta Sovereign Authority Doctrine = constitutional fortification | BAR-SIM-01 | ✓ |
| Almud institutional ambiguity as governance — Thread absorbed without public acknowledgment | ALM-SIM-03 | ✓ |
| Ehrenwall Counter fires from information failure (withholding RS data), not military failure | EHR-SIM-01 | ✓ Conviction correctly distinguishes |
| Justice winning Proceedings → shared loss conditions more likely | JUS-SIM-01 | ✓ Institutional winner / peninsula loser |
| Reinhard Principle generalizes to all faction leaders | CROSS-01 | ✓ Core strategic principle |
| Conviction = permanent Ob economy on aligned actions | CROSS-02 | ✓ |

### New SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-B2-01 | Vaynard simultaneous 3-path Accounting conflict verification | OPEN |
| SIM-B2-02 | Ehrenwall moral ledger 30-season timing | OPEN |
| SIM-B2-03 | Justice-as-Confessor 10-season Church governance sim | OPEN |


## Editorial Approval — 2026-04-17

All open editorial items approved by Jordan. Propagated this batch:

| Item | Target | Status |
|------|--------|--------|
| ED-620 RM Founding Mechanic | victory_v30 §8 | Propagated |
| ED-624 Elske Loyalty Track | victory_v30 §3.6 | Propagated |
| ED-625 Excommunication Tribunal | social_contest §7.1 | Propagated |
| ED-616 Intelligence Embargo | tc_political_redesign §8 | Propagated |
| ED-591-609 Arc Expansion v1 | npc_behavior §5.2 reference note | Approved + noted |
| ED-634 Faction Politics expansion | faction_politics_expanded_v1 | Approved, propagation pending |


## ED-634 Propagation — 2026-04-17

Faction Politics rank-ladder expansion (PP-660). Propagated to:

| Target | Change |
|--------|--------|
| npc_behavior_v30 §1.2 | Community and Warden added to Conviction taxonomy |
| npc_behavior_v30 §3.3 | Caste-transgressive Scar risk modifier noted |
| npc_behavior_v30 §2.13 | Crown inner circle (Voss/Reichard/Thale/Linder/Kreutz) Stance Triangles |
| npc_behavior_v30 §2.14 | Hafenmark inner council (Heljason/Geirson) Stance Triangles |
| npc_behavior_v30 §2.15 | Varfell Jarl council (Holdar/Stenskald) Stance Triangles |
| player_agency_v30 §3.3 | Initiation Duty category added |
| Ledger | ED-634 resolved; sub-EDs 635-658 and SIM-POL-R01/02/05 registered |

Remaining open sub-EDs: ED-640/642/643/644/645/648/649/650/651/652/655/656/657/658, SIM-POL-R01/02/05. All P2 except ED-643 (Solmund propagation P1) and SIM-POL-R01/02/05 (P1 sim-debt).

# Archived from coverage_matrix — Phase 1

## SIM-POL — Faction Politics Simulation Debt (PP-660 / PP-661, DEFERRED)

Per user instruction 2026-04-17, simulation validation of PP-660 faction politics rank-ladder expansion is deferred. These items are tracked here for discoverability; no active simulation work is scheduled.

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| SIM-POL-R01 | 7-rank progression pacing — validate player from Std 0 can reach Std 5 by S14 and Std 7 by S20 under normal play | P1 | DEFERRED 2026-04-17 |
| SIM-POL-R02 | Caste modifier impact — confirm Southern Einhir rank-advancement gates do not create unwinnable game states | P1 | DEFERRED 2026-04-17 |
| SIM-POL-R03 | Baralta Crown Claim × rank interaction — confirm Hafenmark-to-Crown Recognition Ceremony does not create exploit paths for free Crown Std 5 | P2 | DEFERRED 2026-04-17 |
| SIM-POL-R04 | TC × rank interaction — confirm TC 100 Unification does not trivialize or over-constrain Church rank advancement | P2 | DEFERRED 2026-04-17 |
| SIM-POL-R05 | Generational Shift Disposition outcomes — confirm 5-tier outcome table does not produce degenerate paths (always +3 in 2 seasons) | P1 | DEFERRED 2026-04-17 |

Resume trigger: (a) user-initiated simulation review, or (b) patch to faction_politics_expanded_v1 that changes rank-advancement formulas.


## New Findings — sim_npc_player_batch4_2026-04-17

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALM-SIM-01 | Almstedt | Constitutional irregularity (40-season-old amendment insufficient supermajority): most potent undisclosed institutional information in the game | Open — ED-660 adjacent |
| HAEL-SIM-02 | Haelgrund | Archives are Thread-constituted live objects, not static records — Ministry maintaining a sense organ no one knows is attached to a body | Noted |
| ELS-SIM-02 | Elske | Diplomatic Exchange produced by 8-season relational investment, not tactical argument — relationship is the precondition | Confirmed |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Almstedt certification of thin precedent enables Baralta Grand Contest — enables while constraining | ALM-SIM-02 | ✓ |
| Voss bifurcated intelligence (formal quarterly vs. War Council true picture) creates strategic reserve unknown to Löwenritter | VOSS-SIM-01 | ✓ |
| Klapp fiscal framing of buffer wins College vote where theological framing would lose | KL-SIM-02 | ✓ |
| Stenskald equal-validity ruling makes Maret Uln's claim an Assembly vote, not a blocked path | STEN-SIM-01 | ✓ |
| Haelgrund's Protocol 3 compliance (administrative routine) produces Warden intelligence access without deliberate choice | HAEL-SIM-01 | ✓ |
| Ehrenwall's 8-season relationship investment with Elske produces IP −10, AER +1 | ELS-SIM-01 | ✓ |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B4-01 | Gatekeepers govern through withholding — negative power is the mid-rank character's primary tool |
| CROSS-B4-02 | Institutional memory is catastrophic risk — each character carries a specific piece of dangerous knowledge |
| CROSS-B4-03 | Relationship is political infrastructure — genuine relationship produces disproportionate returns at crisis moments |


## New Findings — sim_npc_player_batch5_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| REICH-SIM-01 | Reichard | Haushalt Competence 3 +2/season has no Wealth cap — unbounded resource generation over long campaigns | Resolved — ED-663 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Reichard bifurcated record-keeping (inquiry notes vs. War Council true picture) preserves institutional memory | REICH-SIM-02 | ✓ |
| Heljason counter-argument addendum: internal preparation without burdening principal | HELJ-SIM-01 | ✓ |
| Father Linder's mutual management with Thale: institutionally stable dual-service without deception | LIND-SIM-01 | ✓ |
| Jarnstal partial compliance with Baralta's Doctrine preserves strongest ecclesiastical immunity ground | JAR-SIM-02 | ✓ |
| Hann's genealogical research produces his own best counter-argument | HANN-SIM-01 | ✓ Correct structural irony |
| Maret Uln's win-win construction: indispensable to Vaynard's success and to post-elimination continuity | MULN-SIM-02 | ✓ |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B5-01 | Advisor as bottleneck — inconvenient truths are managed not delivered; systemic, not individual failure |
| CROSS-B5-02 | Coalition logic is asymmetric — preventing a majority is more efficient than building one |
| CROSS-B5-03 | Long-horizon investment wins mid-range crises — every successful character here invested 2+ seasons ahead |


## New Findings — sim_alternate_branches_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALT-C-01 | Branch C | Path B wins at S9 while other factions 15 seasons from their conditions — speed-run calibration issue | Open — ED-666 |
| ALT-I-01 | Branch I | Coup Counter can fire at S17 before Regency Establishment conditions exist — premature triggering gap | Open — ED-667 |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALT-J-01 | Branch J | Without warden cooperation, RS reaches ~21 at S30 — outside standard campaign window | Open — ED-668 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Almstedt deploys irregularity → forced supermajority → stronger Baralta victory (paradox) | ALT-A-01 | ✓ Constitutional stress-test produces better outcome |
| Voss's reserve makes Coup mechanically impossible without Ehrenwall violating Martial Honour Framework | ALT-B-01 | ✓ Military prep is Counter's check |
| Thale warning Almud produces strongest Crown outcome at highest personal cost | ALT-E-01 | ✓ Spymaster dilemma real |
| Klapp's publication produces Confessor endorsement via casting vote | ALT-D-01 | ✓ Church doctrinal transformation path confirmed |
| Heljason's refusal produces stronger legal brief than compliance | ALT-F-01 | ✓ Obstruction as highest-value advisor function |
| Haelgrund's report enters multi-faction intelligence chains; Niflhel pursues archives | ALT-G-01 | ✓ Silence vs disclosure has institutional cascade |
| Hann winning Assembly produces figurehead Sigurd + factional fragmentation | ALT-H-01 | ✓ Bloodline succession without governance produces POW-01 equivalent |

### Cross-Branch Findings

| Finding | Description |
|---------|-------------|
| CROSS-ALT-01 | Information timing is primary resource — who knows what, when controls outcomes more than military or TCV |
| CROSS-ALT-02 | Premature victory creates shallow worlds — mechanical win before narrative transformation produces stable but incomplete campaigns |
| CROSS-ALT-03 | Irreversible institutional precedent — published documents, legal records, disclosed intelligence cannot be recalled |


## New Findings — sim_mending_coherence_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| MEND-SIM-01 | SIM 2 | OW Mending Coherence cost contradiction | ✓ Resolved — params_threadwork authoritative (0 all degrees); §3.2 corrected |
| MEND-SIM-02 | SIM 6 | ARC-S32 Coherence text wrong | ✓ Resolved — arc_register updated; fatigue mechanics substituted |
| MEND-SIM-03 | SIM 6 | ARC-S34 Edeyja Burnout primary path broken | ✓ Resolved — reframed as overwork/fatigue burnout; TE-15 terminal trigger preserved |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| MEND-SIM-04 | SIM 3–4 | rs_budget.md recovery figures stale | ✓ Resolved — Scenario C updated; Conclusion corrected |
| MEND-SIM-05 | SIM 4 | wc_survival_spine.md Coherence row wrong | ✓ Resolved — resource tension table corrected |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Seasonal fatigue (+1 cumulative Ob, resets each season) throttles Mending effectively — self-correcting at negative E[RS] | MEND-SIM-01 | ✓ |
| WC3-is-singular-endgame conclusion holds; net −3.66/season at WC3 + community Mending survivable to Year 30 | MEND-SIM-04 | ✓ |
| Journeyman practitioners (Spirit 2, TS 50) have negative E[RS] at Field Ob 5; Relational-only targeting is correct | MEND-SIM-06 | ✓ |
| Old system caused permanent Severed equilibrium (Coh ~1, +2 Ob all ops) — new rule eliminates hidden impairment | MEND-SIM-02 | ✓ Design improvement confirmed |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-MEND-01 | Seasonal fatigue is the correct throttle — transparent to player, resets cleanly, no permanent impairment |
| CROSS-MEND-02 | ARC-S32 and ARC-S34 were built on Mending-as-Coherence-drain; both require text revision |
| CROSS-MEND-03 | Community Mending capacity is ~10x RS budget assumption; scenario narratives valid but net figures stale |


## New Findings — sim_alternate_branches2_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| S-01 | Branch S | Ministry census records contain 150 seasons of undeclared Thread-sensitivity data | Open — ED-671 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Olafsson extra-territorial heresy designation as legal shadow outside Hafenmark | K-01 | ✓ |
| Baralta Arc B + Niflhel creates permanent constitutional precedent for criminal network | N-01 | ✓ |
| Unmanaged Arc C begins from absence of support not excess of exposure | Q-01 | ✓ Practitioner relationship structurally required |
| Almud Arc A reform prevents Counter advance via Ehrenwall moral ledger shift | T-01 | ✓ Reform path structurally prevents Coup |
| Haelgrund refusing synthesis → neutrality dataset more consequential than partisan dataset | S-01 | ✓ |
| Linder full RS report → Himlensendt sermon → offhand comment becomes public political theology | P-01 | ✓ |
| Stenskald conservative endorsement → Incapacity Assessment cascade at S28 | O-01 | ✓ |

### Cross-Branch Findings

| Finding | Description |
|---------|-------------|
| CROSS-B2-01 | Institutional neutrality is always political — no institutional act is without political consequence |
| CROSS-B2-02 | Most consequential actions are the smallest ones — addenda, single report decisions, synthesis refusals |
| CROSS-B2-03 | Reform path requires choosing uncertainty before being forced to — only path that permanently prevents the Coup |

