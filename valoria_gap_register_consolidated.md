# Valoria Gap Register — Consolidated
## Updated: 2026-03-25 (Session 7)
## Total items: 108
## Editorial blockers: 0

---

## STATUS KEY
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
| G-105 | GAP-UC-06-A: §8.3 ×3 TT combat multiplier and §11.1 ×3 territorial multiplier stack ambiguously during Zoom In — personal Thread op in mass combat scene | Unplanned combinations sim | Patch §8.3 + §11.1: personal-scale ops during Zoom-in use §11.1 multiplier only, not §8.3 |
| G-106 | BUG-004: Intelligibility/Coherence/ThS naming inconsistency across compilation stages — same track referred to by multiple names | Batch 3+4 | Audit all stage files; standardise to Coherence throughout |
| G-107 | E-TAINT resolved: Taint track abolished. Replaced by Intelligibility then renamed Coherence. Stage3 still contains "Taint" and "Taint Track" header at §5.10 — must be purged | Search (2026-03-27) | Remove all Taint references from stage3 + CP14; §5.10 header = Coherence / Epistemic Seduction |
| G-108 | F-25: ThS hits Crisis (≤5) by Season 3 at standard play rate (1 Thread op/session). No GM warning or pacing note | Batch 3+4 | Add pacing note to §5.9: ThS Crisis typical onset ~Season 3 at standard play |
| G-109 | F-26: §4.5 (Intelligibility/Coherence — no Thread bonus at low track) conflicts with §5.10 (bonus dice at low Coherence). Two sections contradict directly | Batch 3+4 | Clarify: bonus dice are from Coherence (transformation), not Intelligibility decay |
| G-110 | F-27: ThS Crisis + Certainty Rendering Crisis simultaneous — resolution conditions contradict (one requires retreat from practice, other requires Belief engagement) | Batch 3+4 | Add priority rule: Certainty Crisis resolves first; ThS Crisis is secondary |
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
| P1 | 43 | 12 | 31 | 0 | 0 | 0 |
| P2 (main) | 63 | 18 | 29 | 8 | 7 | 0 |
| P2 (consolidation) | 5 | 5 | 0 | 0 | 0 | 0 |
| Hybrid (G-074–G-095) | 22 | 5 | 14 | 0 | 0 | 0 |
| P3 | 4 | 0 | 0 | 1 | 0 | 3 |
| **Total** | **137** | **40** | **74** | **9** | **7** | **3** |

**Editorial blockers: 0**
**Design needed: 74 items**
**Resolved awaiting compilation: 40 items**
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
