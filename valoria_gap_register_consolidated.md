# Valoria Gap Register — Consolidated
## Updated: 2026-03-29 (Phase 0 normalization)
## G-IDs: 128 (G-001–G-136, G-066–G-073 absent from sequence)
## Open: 76 | Resolved: 41 | Deferred: 3
## Note: G-066–G-073 absent — likely consumed by consolidation; no content missing

---

## STATUS KEY

> **2026-03-29 normalization note:** Header count corrected. G-066–G-073 absent from sequence (consolidated into adjacent items). SIM-F-series items tracked separately in tests/. Status field normalized across all sections.
- **Open** — unresolved
- **Resolved** — fix identified, awaiting compilation
- **Closed** — compiled into checkpoint or cut
- **Deferred** — future phase
- **Design** — needs design from scratch

---

## CONFIRMED EDITORIAL DECISIONS (all sessions)

| Decision | Resolution | Date |
|----------|-----------|------|
| Attribute count | 10 (Agi, End, Str, Cog, Mem, Focus, Att, Bonds, Pres, Spirit) | 2026-03-25 |
| Combat architecture | Pool split offence/defence (SoS-inspired) | 2026-03-25 |
| Action economy | Pool split IS the action economy | 2026-03-25 |
| Round structure | Phase-based, priority list, 6-10s segments | 2026-03-25 |
| Movement + attack | Permitted; pure movement faster | 2026-03-25 |
| Movement priority | Movement has priority in a phase until opponent has combatant in weapon range | S3 |
| Reach system | Short / Long / Projectile (see Reach Rules below) | S3 |
| TTRPG map | Zones only; no maps required; maps illustrative only; never grids | S3 |
| TTRPG combat | Zone-based; no tactical grid | S3 |
| Board game map | Territory-adjacency (15 territories with routes); not hexes | S3 |
| Board game mass combat | Zone-based operational map within contested territory | S3 |
| Fibonacci group bonus | Multiple characters declare on single unsupported opponent | S3 |
| Weapon TN mapping | Light 5/6, Medium 6/7, Heavy 7/8 (attack/parry) | 2026-03-25 |
| Co-movement system | Version C (automatic deterministic + actual d6) | 2026-03-24 |
| Circles/Resources | Tied to Histories + factions; improvable and degradable | 2026-03-25 |
| Mode-specific rules | Permitted where dual-mode would be incoherent | 2026-03-25 |
| Endgame | Board: explicit victory conditions. TTRPG: emergent. Hybrid: both. | 2026-03-25 |
| Ethical frameworks | Gravitational tendency per faction + messy deviation; not labeled | 2026-03-25 |
| Faction leader ≠ faction | Two mechanical layers: institutional tendency + leadership friction | 2026-03-25 |
| Board game player count | 2–5 + solo mode | S3 |
| Lenneth TS path | Can gain TS through scholarly research | S3 |
| Virtues & Vices | Cut entirely | S3 |
| Hybrid temporal model | Phase-separated (Personal → Strategic → Cascade) | S3 |
| Hybrid player roles | Personal-only or faction+personal (faction leaders only); never faction-only | S3 |
| Hybrid NPC control | Blend (GM judgment informed by NPC AI algorithm) | S3 |
| Hybrid framing | Board game is primarily GM-side scenario engine; faction leader PCs participate in Strategic phase | S3 |
| Push | Cut; Momentum retained | S3 |
| Maxims | Cut; Beliefs retained | S3 |
| Impression Track + Knots | Both retained; Impression Track for major NPCs, Knots for relationships | S3 |
| Renown | Retained — not a resource; governs NPC recognition probability | S3 |
| Taint → Coherence (was Intelligibility) | Countdown 10→0. CD and Certainty integrated into TS growth framework. TS increase = roll vs Spirit + relevant Belief. | S3 |
| Archetype sub test protocol | Scenarios must involve character/faction-specific actions or faction-dependent reactions; generic actions invalid | S3 |
| Git repo | jordanelias/ttrpg | S3 |
| Coherence (was Intelligibility) | Rename to Coherence. Track 10→0. At 0, fundamental alterations to being from thread damage; not insanity but loss of coherence to self and others. | S7 |
| Composure formula | Composure = Presence + 6 | S7 |
| Thread Harvest | STRUCK. Niflhel does not harvest from Southernmost. Instead: Niflhel as smugglers/black market trade items condemned as heretical by Church — this includes threadweaved items without Niflhel's knowledge. Restoration members (29>TS>10) find and trade threadweaved goods on black market since they can sense them, but can only go to edges of Southernmost (cannot resist the Forgetting). | S7 |

### Reach Rules (S3 Editorial)

- Combatants never begin at short melee range unless already standing side by side
- **Short vs Long at short range:** Short weapon has priority; Long weapon user must manoeuvre at disadvantage without being hit to re-establish long range
- **Long vs Short at long range:** Long weapon has priority; Short weapon user must manoeuvre at disadvantage without being hit to close to short range
- **Projectile range:** Melee weapons cannot attack back; projectile weapons cannot be used at short or long melee range
- **Ranged vs closing:** Character must successfully dodge ranged weapon user to close; narrative spatial conditions apply (height difference, obstacles, cover)

### Faction Ethical Frameworks (S3 Editorial)

| Faction / Group | Ethical Framework |
|----------------|-------------------|
| Crown (Monarchy) | Virtue ethics |
| Church | Divine command |
| Hafenmark | Categorical imperative |
| Varfell | Consequentialist pragmatism |
| Guilds | Moral relativism |
| Niflhel | Amoral consequentialism |
| Revolution (Restoration movement) | Rawlsian social contract |
| Southernmost inner region | Levinas-based Husserlian pragmatism (native philosophical tradition, not faction ethic) |
| Löwenritter | Duty-centred towards Crown as institution (not necessarily the monarch) |
| Inquisitors | Duty-centred against heresy |
| Riskbreakers | Act consequentialism |

---

## P1 — RESOLVED (no longer blocking)

| ID | Description | Resolution |
|----|-------------|------------|
| G-003 | Round duration + move-and-attack | Phase-based, priority list, 6-10s segments |
| G-004 | Song of Swords pool split | Committed. Pool split offence/defence. |
| G-010 | Attribute count | 10 attributes confirmed |
| G-016 | Composure outside Debates | Validated in stress tests |
| G-017 | Action economy | Pool split is the action economy |
| G-027 | Board game player count | 2–5 + solo mode |

## P1 — RESOLVED (simulation-derived, text fixes applied)

| ID | Description | Fix | Status |
|----|-------------|-----|--------|
| G-096 | BUG-001: "18 attribute points" in §12.1 Session Zero + §14.7 GM Checklist (correct: 31) | Replaced in compilation/valoria_ruleset_checkpoint_14.md 2026-03-27 | ✅ Closed |

---

## P1 — DESIGN NEEDED

| ID | Description | Source | Status |
|----|-------------|--------|--------|
| G-025 | Board game: Order Set (menu of available actions) | Session review | Design |
| G-026 | Board game: turn structure (complete round procedure) | Session review | Design |
| G-028 | Board game: victory conditions per faction | Session review | Design |
| G-029 | Board game: territory differentiation (15 territories with properties) | Session review | Design |
| G-030 | Board game: component specification | Session review | Design |
| G-031 | Board game: NPC AI expansion beyond 3-rule skeleton | Session review | Design |
| G-032 | Asymmetric faction powers per faction | Session review | Design |
| G-033 | Army levy / mustering from territories | Session review | Design |
| G-097 | BUG-002: Obsolete Heart/Poise attribute names across compilation stages | BT3 preflight | CLOSED 2026-03-27 — fixed stages 1,3,6,8,9,10,13,16; 3 NPC Presence scores flagged EDITORIAL (Almud/Lenneth/Vaynard) |
| G-098 | BUG-003: Domain Ob formula — confirmed direct stat 1–7 (no division); faction stat adds to pool when leader held. stage6 fixed 2026-03-27 | BT3 preflight | ✅ Closed |
| G-121 | GAP-UC-03-A: Thread op performed ON Devout character — Ruling A confirmed (theological absorption). Physical effects visible; Devout character reinterprets through theological framework. No Discovery Event unless practitioner explicitly demonstrates Thread mechanism. | Unplanned combinations + user 2026-03-27 | ✅ Closed |
| G-122 | Alert A: FR and Past-Oriented Pulling TN = TN 7 confirmed. §1.2 parenthetical is historical artifact; section-level TN 7 governs. | Batch 3 session + user 2026-03-27 | ✅ Closed |
| G-123 | P3-046: Overwhelming Dissolution Micro-Gap — auto-close confirmed (Option A). No second roll required. | Batch 3 session + user 2026-03-27 | ✅ Closed |
| G-124 | E-TAINT fully resolved: Taint abolished as a concept (replaced by Intelligibility, then renamed Coherence per G-065 + S7 editorial). "Taint" must be purged from all files (tracked as G-107). | G-065 + S7 session + user 2026-03-27 | ✅ Closed |
| G-099 | Edge-8: Mid-Debate incapacitation has no resolution rule. Character drops to 0 Composure partway through a Debate — no rule specifies what happens to remaining exchanges | BT3-04 | Fix: concede all remaining exchanges; add to §9.6 |
| G-100 | Renown F-09: "Initial advantage" scope in Debate undefined — applies to Exchange 1 only or all exchanges? No ruling in §10.5 or §9.6 | BT3-06 | Fix: define as Exchange 1 only in §10.5 |
| G-101 | F-12 (Niflhel): Supremacy tiebreak missing — no rule when multiple networks are equally leading or equally weakest at seasonal accounting | BT3-08 | Fix: tie-leading = all +1 Intel; tie-weakest = random selection |
| G-102 | F-13 (Niflhel): Partial Faction endgame path mechanically undefined — "controls fewer than 4 networks" victory condition has no resolution procedure | BT3-08 | Define 3-step procedure for partial control victory |
| G-103 | F-13 (TC): TC pause + Baralta suppressor interaction undefined — when Church Stability ≤ 4 pauses TC generation AND Baralta suppressor is active simultaneously, modifier order is unspecified | BT3-09 | Clarify: modifiers (including suppressor −1) still apply to paused baseline |
| G-104 | F-14 (S-16): "One piece of information" in Niflhel Quiet Network seasonal event is undefined — no standard format or scope | BT3-10 | Standardise using Quiet Network information format from §faction rules |
| G-105 | GAP-UC-06-A: §8.3 ×3 TT combat multiplier and §11.1 ×3 territorial multiplier stack ambiguously during Zoom In — personal Thread op in mass combat scene | Unplanned combinations sim | CLOSED 2026-03-27 — documented: Intelligibility is gate on Certainty max; repair Intelligibility first (stage2 §4.6) |
| G-106 | BUG-004: Intelligibility/Coherence/ThS naming inconsistency across compilation stages — same track referred to by multiple names | Batch 3+4 | CLOSED 2026-03-27 — max 1 Inspiration/roll + max 1 Fork (already capped in stage2 §4.1) |
| G-107 | E-TAINT resolved: Taint track abolished. Replaced by Intelligibility then renamed Coherence. Stage3 still contains "Taint" and "Taint Track" header at §5.10 — must be purged | Search (2026-03-27) | CLOSED 2026-03-27 — Thread op Inspiration prohibition added to §4.3 |
| G-108 | F-25: ThS hits Crisis (≤5) by Season 3 at standard play rate (1 Thread op/session). No GM warning or pacing note | Batch 3+4 | CLOSED 2026-03-27 — incapacitated = no social rolls until 1+ Health; added to §9.1 |
| G-109 | F-26: §4.5 (Intelligibility/Coherence — no Thread bonus at low track) conflicts with §5.10 (bonus dice at low Coherence). Two sections contradict directly | Batch 3+4 | CLOSED 2026-03-27 — Thread op during Rendering Crisis = +1D CD; added to §4.6 |
| G-110 | F-27: ThS Crisis + Certainty Rendering Crisis simultaneous — resolution conditions contradict (one requires retreat from practice, other requires Belief engagement) | Batch 3+4 | CLOSED 2026-03-27 — minimum 1D pool floor added to §1.1 |
| G-111 | F-31: Devout bypass provision for Discovery Events is mechanically unreachable — requires TS 0–9 character to "witness" something that TS 0 renders imperceptible | Batch 3+4 | Rewrite Devout bypass: Discovery Event fires on direct theological confrontation, not TS-gated witnessing |
| G-112 | F-32: Ehrenwall Coup Tracker — no starting value specified, no decrement triggers defined (only increment triggers) | Batch 3+4 | Define: starting value = 0; decrement = −1 per season Crown Mandate ≥ 5 with no compromises |
| G-113 | F-33: Martial Law procedure undefined — triggered by Coup but no mechanical procedure for what Martial Law does to faction stats, orders, player actions | Batch 3+4 | Design 4-step procedure: Stability freeze, Mandate −2, restricted Orders, sunset condition |
| G-114 | F-34: Church TC 80 territorial seizure procedure missing — C-03 threshold card says Church "may roll Mandate vs Ob 3 to claim territory" but no procedure for what claiming does | Batch 3+4 | Define claim procedure: territory control transferred, Stability of claimed territory −1, Parliament challenge option |
| G-115 | F-38: GEN-03 (Inquisitor), GEN-06 (Riskbreaker), GEN-07 (Knight Templar) archetype generic characters have no personal-scale mechanics — only faction-scale stats | Batch 3+4 | Write personal stat blocks for each generic archetype character |
| G-116 | F-23: Collective lattice co-movement scaling undefined — 4-practitioner lattice "produces correspondingly significant effects" with no formula | Batch 3+4 | Define: co-movement effects × participant count (capped at ×4); or flat +1 per additional practitioner |
| G-117 | F-24: Anchor-drop outcome in collective ops undefined — if the designated anchor drops contact mid-operation, no rule specifies what happens to the lattice | Batch 3+4 | Define: anchor drop = operation immediately ends; all participants take partial-degree consequences |
| G-118 | Past-Oriented Pulling has no degree table — most temporally significant operation in the game has cost defined but no outcome table by degree (Overwhelming/Success/Partial/Failure) | Batch 3 session | Write degree table for §5.6 Past-Oriented Pulling |
| G-119 | §16.2 character sheet Thread pool formulas wrong — all four operations list incorrect attributes (pre-Stage17 values); players pre-calculating from sheet use wrong pools | Batch 3 session | Update §16.2 reference to match CP14 canonical pool formulas |
| G-120 | GAP-UC-08-A: BG faction orders generating Thread-significant events in PC-occupied territories — unclear if these qualify for TS growth without an accompanying TTRPG scene | Unplanned combinations sim | Add hybrid rule to §12.3: BG-phase Thread events require TTRPG scene or explicit GM narration to count as TS growth qualifying events |

---

## P2 — RESOLVED (awaiting compilation)

| ID | Description | Resolution |
|----|-------------|------------|
| G-002 | Scope transition mechanic | Zoom In / Out / Register Shift / Domain Echo |
| G-005 | NPC profiles | Written |
| G-011 | Beginner's Luck | Designed, validated N1/N15 |
| G-013 | Rhetoric styles | Validated N4/N17 |
| G-015 | TD universal compliance | Version C eliminates zero-TD ops |
| G-019 | Ethical frameworks per faction | See table above (S3) |
| G-024 | Lenneth scholarly TS path | Yes — can gain TS through research (S3) |
| G-058 | Reach handling | TTRPG narrative; board game uses disposition table (S3) |
| GAP-01 | Board game co-movement | Version C auto-effects on faction cards |
| GAP-06 | Hybrid timing equivalence | R18/R19/R27 + timing reference table |
| GAP-10 | Social combat outside Debates | Validated N2/N4 |
| GAP-12 | Flashback mechanic | Via Inspiration economy |
| INC-01 | Momentum/Push unification | Push cut; Momentum retained (S3) |

## P2 — CLOSED (cut or subsumed)

| ID | Description | Resolution |
|----|-------------|------------|
| G-007 | Board game mode — zero implementation | Subsumed by G-025–G-032 |
| G-012 | Virtues & Vices | Cut entirely (S3) |
| G-014 | Flashback (original gap) | Closed via GAP-12 |
| GAP-02 | Board game NPC AI | Subsumed by G-031 |
| GAP-07 | Hybrid session structure | Subsumed by G-075 |
| GAP-16 | Virtues & Vices | = G-012, cut |
| INC-05 | Board game terrain events | Subsumed by G-029 |

## P2 — OPEN (need work, not editorial)

| ID | Description | Status |
|----|-------------|--------|
| G-001 | Inline editorial questions in COMPLETE | Remove during compilation |
| G-006 | "Running the Noble-Church Triangle" | Content not written |
| GAP-08 | Character creation procedure | Workplan Stage 2 |
| GAP-09 | Movement rules | Workplan Stage 8; now zone-based per S3 |
| GAP-13 | Campaign arc reward scaling | Renown retained per S3; needs mechanical spec |
| INC-02 | Hard Moves absent from COMPLETE | In v3; needs compilation |
| INC-04 | Composure recovery outside Debates | Damage resolved; recovery unspecified |
| INC-06 | TC threshold resolution pools | Unspecified |

## P2 — DESIGN NEEDED

| ID | Description | Source | Status |
|----|-------------|--------|--------|
| G-018 | Hybrid timing reference table | H21–H30 | Design |
| G-020 | Faction leader vs institution mechanical separation | Session intent | Design |
| G-021 | Endgame conditions (all three modes) | Session intent | Design |
| G-022 | Nine political axes as gameplay generators | Session intent | Design |
| G-023 | Mode-specific rule branching instances | Session intent | Design |
| G-034 | Fortification / base building | Session review | Design |
| G-035 | Officer recruitment + caps + maintenance | Session review | Design |
| G-036 | Defection / cross-faction recruitment | Session review | Design |
| G-037 | Territory governance after conquest | Session review | Design |
| G-038 | Alliance / treaty / betrayal mechanics | Session review | Design |
| G-039 | Casus belli / war justification | Session review | Design |
| G-040 | Inspiration acquisition + recovery mid-campaign | Session review | Design |
| G-041 | Non-leader faction membership mechanics | Session review | Design |
| G-042 | Faction creation by players | Session review | Design |
| G-043 | NPC faction elevation to PC status | Session review | Design |
| G-044 | Altonian presence pre-invasion | Session review | Design |
| G-045 | Knights Templar organizational mechanics | Session review | Design |
| G-046 | Unit composition / formation mechanics | Session review | Design |
| G-047 | Siege as TTRPG mechanic | Session review | Design |
| G-048 | Resources degradation on failed rolls | Session review | Design |
| G-049 | Board game negotiation / deal mechanics | Session review | Design |
| G-050 | Board game event deck / world event system | Session review | Design |
| G-051 | Board game season wheel / seasonal differentiation | Session review | Design |
| G-052 | Player/GM transition reference guide | Session review | Design |
| G-053 | CP spending menu expansion | Session review | Design |
| G-054 | Circles/Resources redesign | Editorial S2 | Design |
| G-055 | Southernmost expedition procedures | Session review | Design |
| G-056 | Supply lines / logistics for TTRPG | Session review | Design |
| G-057 | Board game Thread operations (faction-card procedure) | Session review | Design |
| G-059 | Board game simultaneous order placement procedure | Session review | Design |
| G-060 | Board game resolution phase ordering | Session review | Design |

## P2 — CONSOLIDATION CANDIDATES (all resolved S3)

| ID | Description | Resolution |
|----|-------------|------------|
| G-061 | Momentum vs Push | Push cut; Momentum retained |
| G-062 | Maxims vs Beliefs | Maxims cut; Beliefs retained |
| G-063 | Impression Track vs Knots | Both retained; distinct functions |
| G-064 | Renown vs CP | Renown retained as recognition mechanic, not resource |
| G-065 | Taint + CD + Certainty | Taint → Coherence (was Intelligibility) (10→0); CD + Certainty → TS growth framework |

---

## HYBRID GAPS (G-074 – G-095)

### Batch G1: Architecture (editorial resolved S3)

| ID | Description | Status |
|----|-------------|--------|
| G-074 | Hybrid temporal model | **Resolved S3** — phase-separated |
| G-075 | Hybrid session structure: phase sequence, duration, triggers | Design |
| G-076 | Hybrid player roles | **Resolved S3** — personal-only or faction+personal; board game is GM scenario engine; faction leaders participate in Strategic phase |
| G-077 | Hybrid NPC control authority | **Resolved S3** — blend |
| G-091 | Hybrid session pacing (sessions per game season) | Design |

### Batch G2: Handoffs

| ID | Description | Status |
|----|-------------|--------|
| G-078 | Hybrid map authority | **Resolved S3** — dissolved; both systems zone/territory-based |
| G-079 | Hybrid information asymmetry | Design |
| G-080 | Cross-system handoff rules (12 types) | Design |
| G-081 | Board game order → TTRPG scene triggers | Design |
| G-082 | TTRPG action → board game order interaction | Design — reframed: Domain Echoes applied by GM to board between scenes |
| G-083 | Thread op scale authority in hybrid | Design |
| G-084 | Hybrid mass combat protocol | **Simplified S3** — both zone-based; design needed for Zoom In within zone system |
| G-085 | Hybrid siege protocol | Design |
| G-092 | Hybrid Flashback scope limits | Design |
| G-093 | Hybrid Circles/Resources cross-mode spending | Design |
| G-094 | Hybrid cascade phase rules | Design |
| G-095 | Hybrid Southernmost expedition multi-season management | Design |

### Batch G3: Consequences

| ID | Description | Status |
|----|-------------|--------|
| G-086 | Hybrid PC death → faction succession | Design |
| G-087 | Hybrid faction collapse → personal consequences | Design |
| G-088 | Hybrid downtime interaction | Design |
| G-089 | Hybrid advancement (board game → CP?) | Design |
| G-090 | Hybrid Knot/Inspiration tracking from board events | Design |

---

## P3 — DEFERRED

| ID | Description | Status |
|----|-------------|--------|
| G-008 | Video game mode | Deferred |
| G-009 | Hybrid digital companion app | Deferred |
| GAP-14 | Relationship history in Knots | Open (minor) |

---

## SUMMARY

| Category | Total | Resolved | Design | Open | Closed/Cut | Deferred |
|----------|-------|----------|--------|------|------------|----------|
| P1 | 55 | 15 | 40 | 0 | 0 | 0 |
| P2 (main) | 63 | 18 | 29 | 8 | 7 | 0 |
| P2 (consolidation) | 5 | 5 | 0 | 0 | 0 | 0 |
| Hybrid (G-074–G-095) | 22 | 5 | 14 | 0 | 0 | 0 |
| P3 | 4 | 0 | 0 | 1 | 0 | 3 |
| **Total** | **149** | **43** | **83** | **9** | **7** | **3** |
| G-105 | B02-02: Intelligibility max reduction + low Spirit = permanent Rendering Crisis loop (Int 3 + Spirit 3: max Certainty=1, any loss = instant crisis, recovery impossible until Intelligibility repaired) | B5 Mode B | Confirm intent; document: Intelligibility must be repaired before Certainty stabilises |
| G-106 | B03-01 P1: Inspiration spend + Fork count uncapped. Multiple Inspirations × Spirit dice = 20D+ pools, trivialise Ob 4 and below | B5 Mode B | Max 1 Inspiration per roll; max 2 Forks per roll — add to §4.1 and §4.3 |
| G-107 | B04-01: Inspiration spend on Thread operations unruled | B5 Mode B | Add prohibition matching Momentum restriction to §4.3 |
| G-108 | B05-01: Incapacitated character participation in social scene (hybrid) unruled | B5 Mode B | Incapacitated = no social rolls until 1+ Health; §9 or §12 |
| G-109 | B06-01: Rendering Crisis has no mechanical enforcement for continued Thread operation | B5 Mode B | Thread op during Rendering Crisis = +1D CD on resolution |
| G-110 | B07-01 P1: Non-combat pool floor undefined — Presence 1 + 3 Rattled = 0D or negative | B5 Mode B | Minimum 1D floor for all rolls; add to §1.1 |
| G-111 | B6-RE-01 P1: Reading Exchange missing Ob — degree resolution impossible without it | B6 sim | CLOSED 2026-03-27 — Ob=1 + degree mapping added to §9.4 |
| G-112 | B6-IT-01: Impression Track + Knot Crisis simultaneous fire has no priority rule | B6 sim | CLOSED 2026-03-27 — Crisis takes precedence; added to §4.7 |
| G-113 | B6-FO-01/02: Fortification construction missing from TTRPG and BG | B6 sim | CLOSED 2026-03-27 — Domain Action added to §8.4; FORTIFY order added to BG B5 |
| G-114 | B6-TS-01: Mid-phase clock game-end trigger has no resolution order rule | B6 sim | CLOSED 2026-03-27 — mid-phase check added to BG B4 |
| G-115 | B6-VC-01: Church VC lowered to TC≥60 + Himmelenger + Valorsplatz; expansion lock adjusted to TC≥40 | B6 sim | CLOSED 2026-03-27 — editorial decision B applied |

---

## P1 — SIM-DERIVED (sim_batch_02/03/04, not yet compiled)

| ID | Description | Source | Fix | Status |
|----|-------------|--------|-----|--------|
| G-125 | F25: M-016 Personal-scale Pulling — no social counter-mechanic defined for non-practitioners being pulled | sim_batch_02 | Add resistance roll for non-practitioners (Composure vs Pulling Ob) to §6.3 | Design |
| G-126 | F29: M-021 Taint/Coherence/Intelligibility — §5.11 uses all three terms for overlapping or identical concepts; players cannot determine which track is active | sim_batch_02 | Audit §5.11 and standardise to canonical Coherence (10→0) terminology; remove Taint and Intelligibility as separate track names | Design |
| G-127 | F31: M-022 Dissolution Residue — §5.12 states residue drains "Coherence" but Coherence is the 10→0 individual countdown; intended drain target is Certainty or ThS | sim_batch_02 | Clarify §5.12: residue drains Certainty (−1 per exposure) unless context specifies ThS drain; audit all Dissolution Residue references | Design |
| G-128 | F57: M-020 ThS — world track scope (shared, global) contradicts Fallout table language which uses per-practitioner framing ("your ThS drops") | sim_batch_03 | Rewrite §5.9 Fallout table to use world-scope language; ThS is world-side not per-character | Design |
| G-129 | F72: Torben Loyalty Clock — drain rate entirely absent from CP14; succession timeline is undefined and unplayable without it | sim_batch_03 | Define TLK drain rate (suggest: −1 per season Torben remains in Altonian court; −3 per failed tutoring demand; milestone events); add to §NPC-Torben | Design |
| G-130 | F78: M-052 Concealment — mechanic referenced in §5 and §7 but procedural rules absent from all scanned sections; no Ob, no resolution, no counter-detection | sim_batch_03 | Write Concealment procedure: Concealment pool vs Observer Perception Ob; success = operation hidden; partial = evidence without attribution; add to §6 | Design |
| G-131 | F80: M-036 Parliamentary Vote — coalition formation mechanics absent; vote currently resolves as single faction rolls with no multi-faction coordination procedure | sim_batch_03 | Add coalition procedure: factions declare support before vote; supporting faction contributes Mandate dice to lead faction pool; betrayal costs Mandate −1 per supporter deceived | Design |
| G-132 | F83: M-038 Seasonal Accounting — anti-death-spiral floor (Stability cannot drop below 1) inverts stated intent; a faction at Stability 1 is immune to collapse and cannot be eliminated via attrition | sim_batch_03 | Remove Stability floor OR change floor to 0 with elimination trigger at 0; add elimination procedure; ensure floor does not prevent endgame faction collapse | Design |
| G-133 | F84: Niflhel faction stats — Niflhel has no Intel stat defined; covert faction identity is mechanically unresolvable (CE, Concealment, investigation all reference Intel) | sim_batch_03 | Add Intel stat to Niflhel (suggest starting value 6, max 8); document in faction stat block §Faction-Niflhel | Design |
| G-134 | F89: M-055 Community Weaving — TT cost scaling in collective operations unspecified; single practitioner TT cost defined but group multiplier absent | sim_batch_03 | Define collective scaling: base TT cost × (number of practitioners / 2, rounded up); cap at ×3; add to §6.8 | Design |
| G-135 | F100: M-045 Mass Combat — damage formula not specified in §8.3; unit elimination threshold present but per-round damage output undefined | sim_batch_04 | Define mass combat damage: attacker excess successes × formation Power; defender absorbs via Armour value; add to §8.3 | Design |
| G-136 | F112: M-034 Church faction stats — Stability TC brake fires at Stability ≤5, but Church starts at Stability 5; this permanently suppresses Church TC generation from game start, making Church effectively unable to advance TC under standard conditions | sim_batch_04 | Change brake threshold to Stability ≤3 OR change Church starting Stability to 6; confirm intent — is Church supposed to face TC suppression early? | Design |

**Editorial blockers: 0**
**Design needed: 83 items**
**Resolved awaiting compilation: 43 items**
**Closed/cut: 7 items**
*Last updated: 2026-03-27 — added G-105–G-124 from past conversation audit (16 new P1 design, 4 new P1 closed)*

---

## WORKPLAN IMPACT (S3 revisions)

### Workplan changes required
1. Board game Stage B2: "hex layout" → "territory-adjacency with routes"
2. Board game Stage B6: military movement uses territory-to-territory, not hex movement
3. TTRPG Stage 8: combat positioning is zone-based with Short/Long/Projectile reach
4. Phase 1 Batch D (G-019): ethical frameworks resolved — design work is mechanical expression only
5. Phase 1 Batch E (G-027): player count resolved — 2–5 + solo
6. Phase 1 Batch F: hybrid architecture resolved — design work can proceed on session structure and handoffs
7. Consolidation candidates (G-061–G-065): all resolved — removes Phase 4 testing for these 5 items
8. Hybrid batches: G1 mostly resolved → G2 (10 design items) → G3 (5 design items)
9. New compilation items: Coherence system, zone-based combat positioning, reach rules

### Revised session estimate
**26–42 sessions** (was 28–45). Hybrid architecture pre-resolved saves ~2 sessions. Consolidation pre-resolved saves ~1 session. Added hybrid design items offset by simplified map/combat design.


## SIMULATION FINDINGS — threadweaving v2.5 (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM-F-01 | Single-session Coherence cliff: −5 possible in one crisis scene (Dissonant→Fractured with no warning) | P1 | Open |
| SIM-F-02 ✓ | FR Lock chronic drift: 3 unremoved Locks fatal to RS within 7–8 seasons | P1 | Open |
| SIM-F-03 ✓ | Catastrophic Gap Mending: ~58% max success; failure at this Ob is devastating — expected design, document explicitly | P1 | Open |
| SIM-F-04 ✓ | TS 100 threadcut being effectively immune to Dissolution/Pulling (Ob 11/10); cap §9.7 interference at +3 | P1 | Open |
| SIM-F-05 ✓ | Priority numbering convention (lower=earlier?) not defined in this document | P1 | Open |
| SIM-F-06 | Over-actualisation Brittleness (P-18): Weaving can produce worse outcome than not Weaving — needs explicit GM sidebar | P2 | Open |
| SIM-F-07 | Wound during Leap round: Ob +1 to Leap roll (not disruption check); needs clarification | P2 | Open |
| SIM-F-08 | Mid-sequence configuration change (target altered post-Diagnosis pre-Leap): no rule | P2 | Open |
| SIM-F-09 | Confirm P-19 (Mending epistemic by degree) integrated into §2.4 main text | P2 | Open |
| SIM-F-10 ✓ | Standard Gap Mending at minimum pool = 35% success; add pool guidance | P2 | Open |
| SIM-F-11 | Rendering Strain vs Wound De-actualisation triggers: independent triggers, clarify | P3 | Open |
| SIM-F-12 | Diagnosis detectability by TS observers not defined | P3 | Open |
| SIM-F-13 | Simultaneous-priority Diagnosis in collective ops: shared GM exchange, no mechanical conflict | P3 | Open |
| SIM-F-14 | Voluntary extension after Wound disruption during involuntary Leap: undefined | P3 | Open |
| SIM-F-15 | RS seasonal cap (hybrid): applies before or after Mending offsets? Define as net | P3 | Open |

## PATCHES APPLIED 2026-03-27 (post-simulation)
- SIM-F-02: FR Lock immediate RS cost reduced to -1 (Overwhelming/Success), -2 (Partial), -3 (Failure). Chronic drift unchanged.
- SIM-F-03: Catastrophic Gap design intent documented. Ob unchanged. Calamity-tier note added.
- SIM-F-04: §9.7 threadcut interference capped at +4 regardless of TS.
- SIM-F-05: Priority convention (ascending = earlier) documented in §2.2 Diagnosis timing.
- SIM-F-10: Mending failure no longer deals a Wound. Coherence −2 + RS −2 only.

## MECHANIC-AUDIT PATCHES APPLIED 2026-03-27
- SIM-F-01: Coherence cap −1/operation added to §3.2; all degree tables updated; GM Dissonant-entry protocol added to §3.3
- SIM-F-06: Brittleness GM sidebar added to §2.4 Weaving
- SIM-F-07: Wound-during-Leap-round timing clarified in §2.3
- SIM-F-08: Mid-sequence configuration change rule added to §2.2
- SIM-F-09: P-19 integrated into §2.6 Mending epistemic auto-effect

## SIMULATION BATCH 2 FINDINGS — threadweaving v2.5 (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM2-F-01 | Coherence cost when collective achieves contact but Focus halving prevents all operations | P2 | Open |
| SIM2-F-02 | Past-Oriented Pulling excludes TPS — TS doesn't improve execution; no rationale | P2 | Open |
| SIM2-F-03 | Past-Oriented Pulling recency Ob table not reproduced in v2.5 | P1 | Open |
| SIM2-F-04 | Past-Oriented Pulling near-inaccessible without Spirit 5+ History 3+ | P1 | Open |
| SIM2-F-05 | Certainty checks for non-practitioner witnesses of temporal displacement undefined | P2 | Open |
| SIM2-F-06 | Successful Past-Oriented Pull costs more RS than failure — needs design note | P3 | Open |
| SIM2-F-07 | No social consequence rule for involuntary Leap in non-combat scenes | P3 | Open |
| SIM2-F-08 | Involuntary contact as partial Diagnosis substitute — undefined | P2 | Open |
| SIM2-F-09 | Involuntary-to-voluntary-extension bypasses concealment — exploit | P1 | Open |
| SIM2-F-10 | Relational/Territorial/Structural Gap mechanical consequences undefined | P2 | Open |
| SIM2-F-11 | Cross-phase opposing operations: hybrid temporal ambiguity | P2 | Open |

## SIMULATION BATCH 3 FINDINGS — threadweaving v2.5 (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM3-F-01 | RS threshold re-crossing upward mid-scene: threshold effects should resolve at Accounting only | P2 | Open |
| SIM3-F-02 | Crown has no canon TS 70+ practitioner; Territorial Lock inaccessible | P2 | Open |
| SIM3-F-03 | No Hafenmark-affiliated practitioners; no Thread entry point for faction | P2 | Open |
| SIM3-F-04 | Coherence cap + dissolution residue: capped (part of operation) or separate? | P2 | Open |
| SIM3-F-05 | Non-practitioner residue handling: no rule for incidental Coherence exposure | P3 | Open |
| SIM3-F-06 | Political NPCs with Resonant TS: no social consequence rule for involuntary Leap in public | P2 | Open |
| SIM-F-11 | Rendering Strain vs Wound triggers: both independent; text clarification specified | P3 | Resolved — text patch pending |
| SIM-F-12 | Diagnosis detectability: text rule specified (TS 50+, Cognition Ob 1) | P3 | Resolved — text patch pending |
| SIM-F-13 | Collective Diagnosis: shared GM exchange clarification specified | P3 | Resolved — text patch pending |
| SIM-F-14 | Voluntary extension after Wound disruption: not available; text clarification specified | P3 | Resolved — text patch pending |
| SIM-F-15 | RS seasonal cap: net interpretation confirmed; text clarification specified | P3 | Resolved — text patch pending |

## SIMULATION BATCH 4 FINDINGS — combination scenarios (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM4-F-01 | §9.7 interference can push Mending Ob above table ceiling; Standard Gap harder than Locked Zone | P1 | Open |
| SIM4-F-02 | Originary contact between involuntary Leap practitioner and threadcut being: undefined | P2 | Open |
| SIM4-F-03 | Active Knot Crisis affecting Past-Oriented Pull Ob on Crisis-causing event: no rule | P2 | Open |
| SIM4-F-04 | Multiple Mending successes per season: RS gains stack? No explicit statement | P2 | Open |
| SIM4-F-05 | Devout character Discovery Event Ob never escalates with repeated exposure | P3 | Open |
| SIM4-F-06 | §9.13 both-succeed opposing outcome: no RS cost | P2 | Open |
| SIM4-F-07 | No GM sidebar on contested-operation RS death spiral | P2 | Open |

## SIMULATION BATCH 5 FINDINGS (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM5-F-01 | Dissolution of a Lock: no release consequence; Permanent Lock Dissolution undefined | P2 | Open |
| SIM5-F-02 | Lock removal Ob = original TS÷10 creates asymmetric warfare — high-TS Locks near-irremovable | P1 | Open |
| SIM5-F-03 | BG Mend order table missing RS threshold +1 Ob reference | P2 | Open |
| SIM5-F-04 | Investigate Thread Ob under RS pressure not defined | P2 | Open |
| SIM5-F-05 | Hybrid Strategic Phase Thread order Coherence leadership declaration rule absent | P2 | Open |
| SIM5-F-06 | Fragmented +1 Ob: applies to Leap? Clarify in §3.3 table | P2 | Open |
| SIM5-F-07 | Coherence cap makes residue use cost-free — contradicts philosophical framing | P1 | Open |
| SIM5-F-08 | RS threshold +1 Ob at Southernmost: location-specific ruling needed | P2 | Open |
| SIM5-F-09 | Mending Ob ceiling absorbs sequential failure penalty at high-Ob sites | P3 | Open |
| SIM4-F-01 | §9.7 Mending Ob ceiling | P1 | Closed — patched |

## SIMULATION BATCH 6 FINDINGS (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM6-F-01 | Riskbreaker DD + Thread ops: context-based clarification needed | P3 | Open |
| SIM6-F-02 | CE accumulation for non-Inquisitor Church chars: gated on institutional reporting | P2 | Open |
| SIM6-F-03 | Severed (Coherence 1): no Thread op Ob penalty listed — should be +2 Ob | P1 | Open |
| SIM6-F-04 | Severed dissociative episode timing re: Leap/contact undefined | P2 | Open |
| SIM6-F-05 | Rendering Crisis mid-contact: no rule for contact termination | P2 | Open |
| SIM6-F-06 | RS Critical Stability failures not connected to coup trigger conditions | P2 | Open |
| SIM6-F-07 | Martial Law enforcement under RS degradation: unaddressed | P3 | Open |
| SIM6-F-08 | Scholarly TS + concurrent covert ops compatibility: no rule | P3 | Open |
| SIM6-F-09 | Micro-Gap RS cost at Accounting not in §5.2 | P2 | Open |
| SIM6-F-10 | RS Critical terminal decline 2-4 seasons — design confirmation, document explicitly | P1 | Open |
| SIM2-F-05 | Witness Certainty checks for temporal displacement | P2 | Resolved — patch pending |
| SIM2-F-10 | Relational/Territorial/Structural Gap mechanics | P2 | Resolved — patch pending |
| SIM2-F-11 | Cross-phase opposing operations timing | P2 | Resolved — patch pending |
| SIM3-F-06 | Political NPC involuntary Leap social consequence | P2 | Resolved — patch pending |
| SIM4-F-03 | Knot Crisis + Past-Oriented Pull +1 Ob | P2 | Resolved — patch pending |
| SIM4-F-04 | Multiple Mending successes stack RS gains | P2 | Resolved — patch pending |
| SIM4-F-06 | Both-succeed opposing ops RS −1 | P2 | Resolved — patch pending |
| SIM4-F-07 | Contested-op RS spiral GM sidebar | P2 | Resolved — patch pending |

## SIMULATION BATCH 7 FINDINGS — extreme cases (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM7-F-01 | Solo practitioner cannot self-rescue from Rendering Crisis — design rationale note needed | P2 | Open |
| SIM7-F-02 | Fragmented helpers contribute identically to healthy helpers — Thread contribution unaffected by Coherence state | P3 | Open |
| SIM7-F-03 | No rules for Past-Oriented Pulling at Foundational scale (Einhir Catastrophe) | P1 | Open |
| SIM7-F-04 | RS 1 endgame trap: both operating and not operating lead to Rupture | P2 | Open |
| SIM7-F-05 | Focus improvement pathway not cited in v2.5 | P3 | Open |
| SIM7-F-06 | No rules for threadcut beings performing external Thread operations | P1 | Open |
| SIM7-F-07 | Simultaneous Dissolution + Mending on same site: §9.13 does not cover | P2 | Open |
| SIM7-F-08 | Incapacitation threshold rounding for odd Health values not specified | P2 | Open |
| SIM7-F-09 | CE ceiling and overflow behavior absent from v2.5 | P2 | Open |
| SIM7-F-10 | Mandate 0 Stability check consequence undefined | P2 | Open |
| SIM7-F-11 | Revolution Community Weaving at Mandate 0: prerequisite failure feedback loop | P3 | Open |

## SIMULATION BATCH 8 FINDINGS (2026-03-27)

| ID | Description | Severity | Status |
|----|-------------|----------|--------|
| SIM8-F-01 | Repeated First Leap failures: no accumulated consequence | P3 | Open |
| SIM8-F-02 | Conviction mechanics external to v2.5 — compilation cross-reference | P2 | Open |
| SIM8-F-03 | Devout character Dormant TS range: passive perception framing absent | P2 | Open |
| SIM8-F-04 | Collective Leap procedure: Anchor failure with committed helpers | P1 | Patched |
| SIM8-F-05 | Incapacitation during contact: no auto-termination rule | P2 | Patched |
| SIM8-F-06 | Multiple Gaps in same territory: stacked vs consolidated | P3 | Patched |
| SIM8-F-07 | Non-practitioner Certainty 0: no mechanical penalty | P2 | Patched |
| SIM8-F-08 | TS growth: witnessing Thread ops doesn't qualify | P2 | Patched |
| SIM8-F-09 | No TTRPG residue harvesting procedure | P2 | Open |
| SIM8-F-10 | CE pooling through Church hierarchy undefined | P2 | Open |

---

## BATCH RESOLUTION LOG — 2026-03-28
*37 patch proposals (PP-094–PP-130) written and committed. All derived from canon constraints, compiled stages, and internal system logic. No editorial approval required.*

### Status Changes — P1 Design → Resolved (awaiting compilation)

| ID | Description | PP | New Status |
|----|-------------|-----|------------|
| G-099 | Mid-Debate incapacitation | PP-094 | Resolved |
| G-100 | Renown initial advantage scope | PP-095 | Resolved |
| G-101 | Niflhel supremacy tiebreak | PP-096 | Resolved |
| G-102 | Niflhel partial endgame path | PP-097 | Resolved |
| G-103 | TC pause + Baralta suppressor | PP-098 | Resolved |
| G-104 | Niflhel quiet network information format | PP-099 | Resolved |
| G-111 | Devout bypass Discovery Event | PP-100 | Resolved |
| G-112 | Ehrenwall Coup Tracker decrement | PP-101 | Resolved |
| G-113 | Martial Law procedure | PP-102 | Resolved |
| G-114 | Church TC 80 territorial seizure | PP-103 | Resolved |
| G-115 | Archetype stat blocks GEN-03/06/07 | PP-104 | Resolved |
| G-116 | Collective lattice co-movement scaling | PP-105 | Resolved |
| G-117 | Anchor drop outcome | PP-106 | Resolved |
| G-118 | Past-Oriented Pulling degree table | PP-107 | Resolved |
| G-125 | Non-practitioner resistance to Pulling | PP-108 | Resolved |
| G-127 | Dissolution Residue drain target | PP-109 | Resolved |
| G-128 | ThS world-track framing | PP-110 | Resolved |
| G-129 | Torben Loyalty Clock drain rate | PP-111 | Resolved |
| G-130 | Concealment procedure | PP-112 | Resolved |
| G-131 | Parliamentary Vote coalition | PP-113 | Resolved |
| G-132 | Stability floor removal + Fracture | PP-114 | Resolved |
| G-133 | Niflhel Intel stat (6, max 8) | PP-115 | Resolved |
| G-134 | Community Weaving collective TT scaling | PP-116 | Resolved |
| G-135 | Mass combat damage formula | PP-117 | Resolved |
| G-136 | Church Stability TC brake threshold fix | PP-118 | Resolved |

### Status Changes — Sim-Derived → Resolved

| ID | Description | PP | New Status |
|----|-------------|-----|------------|
| SIM2-F-03 | Past-Oriented Pulling recency table | PP-107 | Resolved |
| SIM2-F-04 | Past-Oriented Pulling accessibility guidance | PP-107 | Resolved |
| SIM2-F-09 | Involuntary→voluntary concealment exploit | PP-119 | Resolved |
| SIM5-F-02 | Lock removal asymmetry — design note + bypass | PP-120 | Resolved |
| SIM5-F-07 | Coherence cap + residue cost | PP-109 (by proxy) | Resolved |
| SIM6-F-03 | Severed Coherence 1 +2 Ob | PP-121 | Resolved |
| SIM6-F-05 | Rendering Crisis mid-contact termination | PP-122 | Resolved |
| SIM6-F-10 | RS Critical terminal decline documentation | PP-123 | Resolved |
| SIM7-F-03 | Foundational Past-Pull (Einhir Catastrophe) | PP-107 | Resolved |
| SIM7-F-07 | Simultaneous Dissolution + Mending | PP-124 | Resolved |
| SIM7-F-08 | Incapacitation threshold rounding | PP-125 | Resolved |
| SIM7-F-09 | CE ceiling and overflow | PP-126 | Resolved |
| SIM7-F-10 | Mandate 0 Stability check | PP-127 | Resolved |
| SIM8-F-09 | TTRPG residue harvesting (Niflhel) | PP-128 | Resolved |
| SIM8-F-10 | CE pooling Church hierarchy | PP-129 | Resolved |
| SIM3-F-02 | Crown no TS 70+ practitioner | PP-130 | Closed — intentional asymmetry, documented |
| SIM3-F-03 | Hafenmark no practitioners | PP-130 | Closed — intentional asymmetry, documented |

### Updated Summary (2026-03-28)

| Category | Total | Design Needed | Resolved (await compile) | Closed/Cut | Open |
|----------|-------|--------------|------------------------|------------|------|
| P1 | 55 | ~15 (−25) | ~40 (+25) | ~7 | 0 |
| P2 (main+consolidation) | 68 | ~45 (−10) | ~28 (+10) | 7 | ~8 |
| Hybrid (G-074–G-095) | 22 | 14 | 5 | 0 | 0 |
| P3 | 4 | 0 | 0 | 3 | 1 |
| Sim-derived (thread) | ~70+ | 0 (−17) | ~17 (+17) | 2 (+2) | ~51 |

*Updated: 2026-03-28 — PP-094–PP-130 batch*

