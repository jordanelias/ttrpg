# Resolution Diagnostic — Mass Battle

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stage 1)
**Scope:** mass battle per skill INITIAL HYPOTHESES — covers `designs/provincial/mass_battle_v30.md` (canonical 2026-04-17), `designs/provincial/mass_battle_integration_v30.md` (sim integration spec, Pass 2n authoring 2026-05-17), `params/mass_combat.md`. Cross-references: faction_layer Trigger 5, threadwork Substrate Saturation, peninsular_strain (RS/MS), victory (ED-743 IP/Strain).
**Status:** Audit output. Commits blocked (B6) — staged inline.
**Critical pre-flight observation:** the **2026-04-29 audit trio** (`mass_battle_stress_test_2026-04-29.md` + `mass_battle_interdependency_2026-04-29.md` + `mass_battle_patch_proposals_2026-04-29.md`) IS a comprehensive prior audit of this system. It surfaced ~50 findings across MATH/S/INTER severities and produced 8 auto-approvable patch proposals + 8 Jordan-decisions. **This diagnostic does NOT duplicate those findings.** Per `<work_discipline>` no-duplication and skill audit-gate "check tests/audit/ for prior audit outputs," I cite the prior audit as canonical, lift only the **resolution-fitness-lens subset**, and surface what the prior audit missed (MB5).

## §0 Pre-flight & citations

**Files consulted this session:**

- `designs/provincial/mass_battle_v30_index.md` — full (heading map of 43 sections)
- `designs/provincial/mass_battle_integration_v30.md` — full first 11k chars (v22 sim feature inventory, port plan)
- `params/mass_combat.md` — full first 11k chars (Core Formula PP-233, Battle Plan templates, 7-phase structure, Discipline degradation, Morale triggers, DR tables, Power tier reference)
- `designs/audit/mass_battle_stress_test_2026-04-29.md` — full (~5.4k); the resolution-and-consistency stress test produced 1 month ago
- `designs/audit/mass_battle_interdependency_2026-04-29.md` — full first 10.5k chars (cross-system stress test: 3 INTER-CRIT findings, 17 INTER significant findings, confirmed-consistent block)
- `designs/audit/mass_battle_patch_proposals_2026-04-29.md` — full first 10.7k chars (8 auto-approvable patches + 8 Jordan-decisions)
- prior turns' substrate: `02_canon_constraints` (P-01–P-15), `references/canonical_sources.yaml`, `skills/valoria-mechanic-audit/SKILL.md`

**NERS source:** PI `<definitions>` block per Turn B.

**Files NOT deep-read this pass (transparency):**
- `designs/provincial/mass_battle_v30.md` canonical body sections (read via index only — 12,601 tokens uncovered; the 2026-04-29 prior audit cites it extensively, mitigating direct read need)
- `tests/sim/sim_mb_06_v22.py` (2143-line implementation; sampled via integration spec only)
- `designs/provincial/mass_battle_v30_infill.md` (rationale/examples, not mechanics)
- `tests/sim/sim_mass_battle_SIM-MB-01..05.md` (simulation outputs)

`[ASSUMPTION: the 2026-04-29 prior audit's findings on canon-internal consistency are still valid unless commit history shows patch proposals applied; resolution status of MB1/MB3/MB9 between 2026-04-29 and 2026-05-28 not verified this turn — basis: <effort_levels max> would require commit-log read which exceeds this turn's scope; flagging for surface verification.]`

## §1 Phase 0 — Resolution component decomposition

Mass battle is a **composite** of:

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Unit combat pool** | `Pool = min(Size, Command) + Command` per PP-233; ranges roughly 2D (Size=Cmd=1) to 14D (Size=7, Cmd=7) | Dice (aggregated, **no floor**) |
| **B · TroopCount / Size / Health** | `H = min(Discipline, Command) + DR`; `Total Health = Size × H`; `Size after = floor(remaining Health ÷ H)` per PP-233 | Continuous-derived (with H frozen per PP-PROP-MB-01) |
| **C · Damage formula** | `Damage per success = 1 + Power`; `Damage dealt = successes × (1+Power)`; simultaneous resolution (v21 BIAS-1) | Deterministic, simultaneous |
| **D · Discipline track** | 1–7 stat; degrades by Phase 6 Step 2 trigger; cliff at 0 = "formation broken, cannot attack" | Base parameter with binary cliff at 0 |
| **E · Morale track** | 1–7 stat; 8 trigger paths down per turn (cap −3/cascade, general death uncapped); recovery +1/Reform OR Rally; rout at 0 | **Clock** (multi-threshold, intended) with rout cliff |
| **F · Phase machine (7-phase)** | Strategy → Volley → Manoeuvre → Off Thread → Engagement → Cascade → Reform | Deterministic state machine |
| **G · Battle Plan templates** | 5 plan options (Advance/Hold/Pincer/Withdraw/Screen); General Command override (TN 7 Ob 1) | Discrete choice + dice |
| **H · Rout contagion** | Adjacent friendlies Discipline Ob 1 → fail = Morale −1; brake prevents same-turn re-cascade | Discrete cascade, braked |
| **I · Cavalry pursuit (v22b G-11)** | Fast victors pursue routing unit; pursuit damage; rearguard −2D; recall TN 7 Ob 2 | Discrete state + dice |
| **J · Substrate Saturation Counter** | ≥3 Thread ops/battle turn → +Ob/+Coherence (cap +2 per battle); ≥3 cumulative → +2 Ob remainder + RS −1 (cap −1/battle) | Discrete accumulator + cap |
| **K · Trigger 5 cross-scale → faction** | faction_layer §6.2: three-condition gate (Mil pool ≥4 + Failure + severity) | Deterministic gate (covered in faction L1) |
| **L · IP/Strain accounting** | mass_battle §E.1/§E.2 immediate + per-season consequences (ED-743 canonical) | Discrete accumulator (clock) |
| **M · Domain Echo timing** | Battle result queued to Accounting, no mid-battle stat change (Hybrid-clean) | Deferred state propagation |

**Three-category classification:**
- **Base parameters (1–7):** Size, Power (derived from Military), Discipline, Morale, Command (derived from `⌈(Cha+Cog)÷2⌉`)
- **Discrete accumulators (clocks):** Morale 1–7, Substrate Saturation Counter, IP/Strain
- **Continuous-derived:** Total Health per unit (= Size × H), where H is frozen at battle start

## §2 Phase 1 — Stress points

### 1a · Smallest pool by design

**No Pool Floor exists at mass scale.** Pool = `min(Size, Command) + Command`. Floor cases:

| State | Size | Cmd | Pool | Effective |
|---|---|---|---|---|
| Levy + Cmd-1 general (worst NPC faction) | 4 (Lvl) | 1 | min(4,1)+1 = 2 | 2D |
| Wounded unit (Size 1, Cmd 1) | 1 | 1 | min(1,1)+1 = 2 | 2D |
| Standard early-campaign (LI, Cmd 2) | 4 | 2 | min(4,2)+2 = 4 | 4D |
| Mid-campaign (Prof, Cmd 3) | 5 | 3 | min(5,3)+3 = 6 | 6D |
| Veteran (Cmd 4) | 6 | 4 | min(6,4)+4 = 8 | 8D |

**By design:** Cmd-1 general or Size-1 unit produces 2D pool. At typical Ob 3 vs TN 7, **P(≥3 hits | 2D) = 0.0** under Binomial. Identical math shape to the faction layer F1 finding. **MB5 (NOVEL).**

**By degradation:**
- Volley + simultaneous damage Phase 6 Step 1 → Size loss → Pool drops if Size > Command (per PP-233 "Pool reduces when Size > Command")
- Discipline degradation (Phase 6 Step 2) → −1D or −2D Power penalty depending on Discipline band
- Stamina exhausted → −1D pool penalty (v22)
- Wound penalty (cross-system PP-716): −1D to all Pools (mass-battle Command checks affected per derived_stats §4.1 wound penalty universality)

Multiple modifiers stack. A Cmd-2 general with Discipline 3 and stamina-exhausted state: 4D − 1D (Disc 3–4 penalty) − 1D (stamina) = 2D before Command check Ob. Below 3-hit threshold at typical Ob.

### 1b · Exposure frequency

| Stress case | Path | Likelihood |
|---|---|---|
| Cmd-1 general (Charisma+Cognition = 1–2 = Cmd 1) | Low-Cha/Low-Cog faction or weakened officer | M-L (build/state dependent) |
| Size-1 unit (97% casualties) | Heavy combat round | M |
| Levy unit at low pool | Mass mobilization (low-Mil factions, war emergency) | M |
| Discipline + stamina + wound stack | Sustained battle, mid-late campaign | M |

`[FREQUENCY SIGNAL: Mass battle's exposure to floor-pool is M-frequency at MOST — units that hit floor pool are typically already losing the engagement (Size near 0, Discipline degraded, etc.). The floor-pool case is the death-spiral phase, not the engaging phase.]`

## §3 Phase 2 — What the stress point decides

### 2a · Outcome type

| Action @ floor | Outcome | Depth |
|---|---|---|
| Unit attack at 2D pool | **Continuous magnitude** (net hits → damage formula); typically near-zero hits → near-zero damage to enemy | Shallow per round; battle is multi-turn |
| Discipline check at low Command | Binary pass/fail → degradation trigger | Shallow |
| Morale check at floor | Binary pass/fail → potential rout (Morale 0) | Multi-step clock (Morale 7→1→0) |
| Unit destroyed (Size 0) | Discrete — unit removed Phase 6 Step 1 | Binary |
| Discipline 0 | Discrete cliff: "formation broken, cannot attack; Reform or rout" | Binary |
| Morale 0 = Rout | Discrete cliff with cascade (§A.12 Morale Cascade + ROUT_CONTAGION_MORALE_HIT) | Discrete + chain |

**The mass-battle outcome is graded-magnitude** (continuous damage accumulation, like personal combat). Variance at 2D pool: net hits 0–2, typical 0–1. Damage swing per success: 1 + Power (Power 1–7). Magnitude swing per hit at floor pool: 0–8 damage. Relative to typical H (3–9), can be significant — but the unit at floor pool is typically near-Size-0 already. Recoverability is therefore narrow.

### 2b · Stakes & reversibility

| Outcome | Reversibility |
|---|---|
| Unit destroyed (Size 0) | **Permanent for battle.** Replaced via muster between battles (with Treasury cost + delay) |
| Unit routed (Morale 0) | **Limited recovery via Rally** (Command check; recovers Morale 1 if general present). Rout contagion damages adjacent allies — partly irreversible cascade. |
| Discipline 0 ("formation broken") | Reform Phase recovery (+1 Discipline, requires Command ≥ current Discipline + 1) — recoverable but slow |
| Cross-scale CL5 (combat → faction Trigger 5) | faction L1 territory + Stab loss — covered in faction diagnostic |
| Battle won/lost (campaign-scale) | Persistent: stat shifts to faction Military, Mandate; territory control; ED-743 IP/Strain accounting (with the propagation gap MB3 below) |

### 2c · Risk profile

| Scenario | Impact | Exposure | Irreversibility |
|---|---|---|---|
| Cmd-1 general's army → 2D Pool floor (MB5) | H | M | M (recoverable via reinforcement) |
| Rout cascade chain (3+ units rout same turn) | H | L | M (brake prevents same-turn re-cascade; battle continues) |
| Wealth-0 faction's Mil 1 → can't muster → enters battle at default Cmd 1, low Disc | H | M | H (cross-scale to faction L7 cascade) |
| Campaign-scale defeat (mass_battle §A.14: Disc −30, Mandate −1) | H | L | M (recoverable but slow at faction layer) |

## §4 Phase 3 — Effect-curve checks

### 3a · Impact uniformity

**Pool scaling per Command (with Size held = Command, the typical mid-battle case):**

| Cmd | Pool | Δ per +1 Cmd |
|---|---|---|
| 1 | 2 | — |
| 2 | 4 | +2 |
| 3 | 6 | +2 |
| 4 | 8 | +2 |
| 5 | 10 | +2 |
| 6 | 12 | +2 |
| 7 | 14 | +2 |

Linear +2D per Command (when Size ≥ Command). **Non-uniform-impact in probability terms** (√N scaling — Lesson 2 micro-flag at high Cmd, but exposure low — Cmd > 5 is rare). Same shape as combat Combat Pool, but mass-battle has **no L2 mitigation analogous to PP-717 D2 Pool DR.** Note this; not a blocker because Cmd 5+ generals are themselves rare.

**Stat damage form:** Power penalty from Discipline degradation is absolute (`Power penalty −1D / −2D`). Non-uniform-impact across Discipline range (same shape as faction F4).

### 3b · Threshold cliffs

| Cliff | Location | Status |
|---|---|---|
| Size → 0 (unit destroyed) | PP-233 | **PASS by intent** — unit removal is the floor-substitute (no Pool Floor, but unit deletion serves the same purpose) |
| Discipline → 0 ("formation broken, cannot attack; Reform or rout") | params §Discipline Degradation | **PASS by intent**, but **borderline** — binary cliff on a 1–7 base parameter. Compose with MB5: a Cmd-1 unit hitting Disc 0 enters cliff state at the same time as its Pool degrades. |
| Morale → 0 (Rout) | params §Morale | **PASS by intent**; explicit cascade-bound (§A.12 Cascade Ob 1, ROUT_CONTAGION_MORALE_HIT 1, brake) |
| Discipline degradation trigger PROVISIONAL (PROV-03) | stress-test | **defect** — trigger condition pre-flagged provisional |
| 8 morale trigger paths down vs +1 recovery | params §Morale Degradation Triggers | **decrease > increase asymmetry, MB7** |
| Substrate Saturation Counter triggers (≥3 ops/turn, ≥3 cumulative) | params + threadwork | **PASS** — explicit caps |
| H frozen at battle start (PP-PROP-MB-01 unverified-status) | PP-PROP-MB-01 | **defect-if-not-applied** — without freeze, H formula loops infinitely |

No new accidental cliff-stacking beyond what the 2026-04-29 audit caught. The intent-justified cliffs (Size/Disc/Morale 0) are designed.

### 3c · Role conflation

**Command** carries: pool dice contribution + cap on Size's pool contribution + cap on Discipline's H contribution + Morale floor while general present + sub-unit limit + tactic execution dice + Rally check + Reform restoration gate.

Eight distinct uses. Per Lesson 1 — these all express "general's leadership capacity," but the breadth of use is genuinely *broader* than the Endurance multi-use in personal combat. **However**: per skill L1 "apply minimally — over-splitting harms Elegance." Eight uses of one stat would, if split, produce eight new stats. The conflation reflects that "Command" is the unifying narrative of an army-with-a-general. Marginal — flag for review but not a true L1 violation.

`[CONFIDENCE: medium]` — this is closer to the L1 line than Stability in faction or Endurance in combat. Worth Jordan attention.

**Size** carries: headcount + pool contribution (capped by Cmd) + total Health basis + reinforcement target. Coherent narrative ("how many troops"). PASS.

**Discipline** carries: pool penalty trigger + Discipline-0 cliff + H formula contribution (capped by Cmd) + Reform recovery requirement. Multi-use but coherent narrative ("formation integrity"). PASS.

## §5 Phase 4 — Loops

| ID | Loop | Damper | Cap |
|---|---|---|---|
| **MBL1 (Morale cascade)** | Unit routs → §A.12 Morale Cascade Ob 1 on adjacent friendlies → fail = Morale −1 → potential further routs | ROUT_CONTAGION_MORALE_HIT=1 brake (cannot re-cascade same turn); Discipline check Ob 1 (typically passes); General presence floor Morale=1 | Morale 0 floor on rout; brake prevents intra-turn explosion |
| **MBL2 (Discipline death-spiral)** | Size loss + losing exchange > 1 → Discipline degradation → Power penalty → less damage out → more damage in → Size loss | Reform Phase recovery (+1 Discipline, requires unengaged + Cmd ≥ current + 1) | Discipline 0 cliff (Formation broken, Reform OR rout) — bounded |
| **MBL3 (Cross-scale → faction Trigger 5)** | Battle Failure + severity → faction §6.2 Trigger 5 → Stab loss | Trigger 5 three-condition gate; Domain Echo timing (queued to Accounting, no mid-battle) | Stab cascade per faction L1 (already P1 in faction verdict) |
| **MBL4 (Stalemate, contested per DECISION-MB-01)** | 3-turn zero-damage → resolution unclear (canonical conflict S-FAIL-01) | Damper depends on which version is canonical | Cap depends on Option A vs B |
| **MBL5 (Cavalry pursuit chase)** | Fast victor pursues routed unit; pursued unit takes pursuit damage; if pursued unit Fast: rearguard option | Recall TN 7 Ob 2 (general re-establishes Command); rearguard −2D allows partial defense | Bounded by Recall mechanic; pursued unit eventually destroyed or recalled |
| **MBL6 (Wealth-0 cascade from faction L7)** | Faction Wealth 0 → Mil −1/season → Cmd / Disc reduced at battle start → MBL2 amplified | Faction-side damper (Trade recovers Wealth, slowly); no mass-battle-side damper | Same as L7 in faction diagnostic — **undamped on the Mil dimension** until faction L7 fix |

**MBL1, MBL2, MBL3, MBL5 PASS.** Damped + bounded as designed.
**MBL4 is open** until DECISION-MB-01 ratified.
**MBL6 inherits faction L7 defect** — fixed by faction-side remediation, not mass-battle-side.

**Phase 4 summary:** Mass battle is **well-bounded under its own scope.** The cross-scale loops it participates in (MBL3 = faction L1, MBL6 = faction L7) have their defects in the *faction layer*, not in mass battle. Skill INITIAL HYPOTHESES holds: "well-bounded spiral: small pools exist but the state machine carries the weight; loops appear damped."

## §6 Phase 5 — Intent gate

| Finding | Intent evidence | Safeguard | Adequate? | Result |
|---|---|---|---|---|
| MB1 (8 open DECISION-MB-01..08) | Listed in audit Phase 4 as "Requires Jordan Decision" | None — open | n/a | **defect status** |
| MB2 (RS=MS terminology) | INTER-CRIT-01 pre-flagged | None | n/a | **defect** |
| MB3 (ED-743 propagation gap) | INTER-CRIT-02 pre-flagged | ED-743 is the authority; propagation pending | n/a | **defect** |
| MB4 (Siege math impossible) | MATH-FAIL-01 pre-flagged; DECISION-MB-07 reco Option A | None until ratified | n/a | **defect** |
| MB5 (no Pool Floor at mass scale — NOVEL) | Unit-deletion-as-floor is implicit-by-design (units exit battle on Size 0) | Unit deletion IS the safeguard | YES, but legibility weak | **PASS-with-flag** — architectural choice valid; E (player intuition) weak |
| MB6 (Discipline 0 binary cliff) | Designed as state-machine signal | Reform Phase recovery | YES | **PASS** |
| MB7 (decrease > increase asymmetry on Morale) | Implicit by design (battle is supposed to degrade Morale) | Morale floor=1 while general present; Rally recovery via Command | partial — composes with MB5 floor case | **PASS-with-flag** |
| MB8 (rout contagion) | §A.12 + ROUT_CONTAGION_MORALE_HIT explicit | Brake prevents intra-turn explosion | YES | **PASS** |
| MB9 (H frozen at battle start) | PP-PROP-MB-01 auto-approvable; clarifies PP-233 intent | None until applied | n/a | **defect (canon clarity)** |
| MB14 (27 PROVISIONAL items) | All flagged in stress-test §PROVISIONALS | None — open | n/a | **defect backlog** |
| MB10/12/13/15/17/18 | Audit-validated, intent explicit | Various | YES | **PASS** |
| MBL4 (Stalemate Break canonical conflict) | DECISION-MB-01 pending | None until ratified | n/a | **defect** |

## §7 Phase 6 — Triage

| # | Finding | Component | Impact | Exposure | Irreversibility | Phase | Severity | Source |
|---|---|---|---|---|---|---|---|---|
| MB1 | 8 DECISION-MB-01..08 open | meta | H | H | M | 0 | **P1 (backlog)** | 2026-04-29 |
| MB2 | RS=MS terminology drift | 0 | H | H | L | 0 | **P1** | 2026-04-29 INTER-CRIT-01 |
| MB3 | ED-743 propagation gap (victory_v30, peninsular_strain) | 0 | H | H | M | 0 | **P1** | 2026-04-29 INTER-CRIT-02 |
| MB4 | Siege math impossible | 0/1 | H | M | M | 0 | **P1** | 2026-04-29 MATH-FAIL-01 |
| MB5 | **No Pool Floor at mass scale — NOVEL** | A | H | M | M | 1+2 | **P1 (NOVEL)** | this turn |
| MB9 | H frozen at battle start (PP-PROP-MB-01 auto-approvable) | B | H | H | H | 0 | **P1** | 2026-04-29 MATH-FAIL-02 |
| MB14 | 27 PROVISIONAL items open | meta | M | M | M | meta | **P2 backlog** | 2026-04-29 §PROVISIONALS |
| MB7 | Morale decrease>increase asymmetry | E | M | H | M | 4 | **P2** | this turn (composes with MB5) |
| MB6 | Discipline 0 binary cliff (intent OK; composes w/ MB5) | D | M | M | M | 3b | **P2** | this turn |
| Various INTER-09–17 | cross-system gaps | meta | M | M | M | various | **P2-P3 backlog** | 2026-04-29 |
| MB8, MB10, MB11, MB12, MB13, MB15, MB16, MB17, MB18 | various | various | — | — | — | various | **PASS** | mix |

## §8 Stage 2 — Lesson mapping

| # | Finding | Lesson(s) | Remediation direction |
|---|---|---|---|
| MB1 | 8 open DECISION items | (canon backlog) | Ratify decisions per 2026-04-29 audit recommendations (Stalemate Option A, Muster Option C, Morale-reset A, Discipline-recovery B, Rout-brake A, Shadow-Intel A, Siege Option A, Cascade-cap as-is). |
| MB2 | RS=MS drift | (canon defect) | Global RS → MS replace in peninsular_strain_v30. |
| MB3 | ED-743 propagation | (canon defect) | Strike "Battle: IP+2, Strain+1" from victory_v30 §0.4 and peninsular_strain Step 4e. Already-canonical ED-743 supersedes. |
| MB4 | Siege math | L3 + canon-defect | Apply DECISION-MB-07 Option A: Pool = Military + 3 (siege bonus). Validates at 2% target. |
| MB5 (NOVEL) | **No Pool Floor at mass scale** | **L3 — architectural gap** | Three options: (a) Add explicit Pool Floor = 2 or 3 at mass scale (matches combat/thread architectural pattern). (b) Document unit-deletion-as-floor as deliberate, with explicit player-facing communication (E fix). (c) Tie Pool Floor to General Command (e.g., min Pool = Command floored at 2). Recommend **(b) plus consideration of (c)** — the architectural choice (unit deletion is the floor) is legitimate; UI clarity is the cheap fix; (c) is the next-cheaper mechanical reinforcement if (b) proves insufficient. **Do NOT prescribe — Jordan-decision.** |
| MB9 | H frozen | (canon clarification) | Apply PP-PROP-MB-01 verbatim per 2026-04-29 patch proposal. Auto-approvable. |
| MB6 | Discipline 0 cliff | (intent PASS but composes with MB5) | No remediation if MB5 addressed. Otherwise document compounding-floor risk. |
| MB7 | Morale asymmetry | L5 (composes with MB5) | Adjacent to faction F5 — same shape. Either accept asymmetry-by-intent (battle is supposed to degrade Morale) or broaden Rally surface. **DECISION-MB-03 Option A reco (Morale reset between battles) is the prior audit's resolution.** Apply. |
| MB14 | PROVISIONAL backlog | (canon backlog) | Per-item Jordan decisions. Each is small; the count (27) is the issue. |
| INTER findings | mostly canon defects | various | Per 2026-04-29 interdependency audit recommendations. |
| MB8/10/11/12/13/15–18 | PASS | — | No remediation. |

## §9 Status

Stage 1 complete. Findings carried to Stage 3 verdict in `ners_verdict_mass_battle.md`.

**Confidence:**
- `[CONFIDENCE: high]` — MB5 (math verified against PP-233 formula)
- `[CONFIDENCE: high]` — MB10, MB12, MB15, MB17 (audit-validated)
- `[CONFIDENCE: medium]` — MB1, MB3, MB9 (resolution-status verification not done this turn; assumed open per absence of commit-log read)

**Departures from skill INITIAL HYPOTHESES:**
- Skill: "Mass battle — likely compliant, well-bounded spiral: small pools exist but the state machine carries the weight; loops appear damped."
- **Confirmed.** State machine (phase machine, Discipline/Morale tracks, simultaneous resolution) does carry the weight. Loops are damped as designed (MBL1, MBL2, MBL5 all PASS).
- **Skill did not predict MB5 (No Pool Floor at mass scale).** This is the novel resolution-fitness finding — architectural shape different from combat/thread; valid by intent (unit-deletion-as-floor) but weakly communicated.
- **Skill did not predict the existing 2026-04-29 audit's scope.** The system has had recent comprehensive consistency-stress-testing; my role is cross-checking under resolution-fitness lens, not duplication.
