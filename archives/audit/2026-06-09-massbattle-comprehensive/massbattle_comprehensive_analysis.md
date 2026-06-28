# Mass Battle System — Comprehensive Analysis (All Workings, All Scales)
**Date:** 2026-06-09 · **Auditor:** Claude (session token 821e65334d345e1b) · **Effort:** max
**Skill protocols:** valoria-resolution-diagnostic (Stages 0–4) + valoria-mechanic-audit (consistency lens)
**Prior audits consumed:** 2026-05-28 resolution diagnostic + NERS verdict; 2026-06-01 stub-wiring completeness audit; 2026-06-05 breakthrough validation; 2026-06-09 session-consolidation master.

---

## §0 — VERDICT

**The mass battle resolution core is NERS-compliant and materially stronger than at the 2026-05-28 audit.** The Lanchester-signature engine (opposed Command-pool exchange + Δσ leverage head + frontage-capped linear melee / square-law volley) passes Necessity, Robustness, and Elegance at the engine level, with three named open gates (G8 low-Command leverage ED-875; Lane-C evaporation validation ED-872; dormant ratified reform ED-905). **Sufficiency is PARTIAL at system level — but the composition of the debt has changed:** the 05-28 backlog of mechanical defects (MB4 siege math, MB7 morale reset, MB9 H-freeze, stalemate, stratagem) is now closed in canon; the remaining debt is **tri-strata documentation drift** (design doc and params lag the ledger-decided, engine-led canon per ED-899's still-unapplied FOLLOW-UP) plus two P2 canon-hygiene defects found this session: a Jordan-decided volley pool change implemented nowhere (F1, ED-800) and an open ledger recommendation grounded on a control surface the live engine does not have (F2, ED-910).

No P1 findings. Twelve findings F1–F12 registered (§7), two staged as ledger-ready candidates (§8). All mechanical values below are cited to source file + section per the audit gate.

**Scales/configurations covered:** unit-duel tick engine (Company scale, BLOCK_SIZE=100) · per-cell formation layer (PER_CELL) · multi-unit battle orchestrator (cascade/pursuit/contagion) · 7-phase TTRPG procedure (doc layer) · BG strategic single-slot resolution (Part B / military_layer §2) · hybrid B.5 handoff · campaign layer (§A.13–A.14) · world bridge & Battle Consequences (Parts C–E) · Thread integration (A.10, stub at engine level) · cross-system muster/Accord/Wealth couplings (military_layer §1, §4).

## §0.1 — Citations (canonical sources read in full this session)

| Source | Coverage |
|---|---|
| designs/provincial/mass_battle_v30.md (v4.8, 936L) + _infill.md | full [READ] |
| params/mass_combat.md (542L) · params/core.md | full [READ] |
| designs/provincial/military_layer_v30.md (405L) | full [READ] |
| designs/provincial/mass_battle_integration_v30.md (474L) | full [READ] |
| canon/02_canon_constraints.md · canon/editorial_ledger.jsonl (65 MB-relevant entries extracted) | full [READ] |
| tests/sim/mass_battle/: config.py, resolution.py (full); orchestration.py (2580L — pool/hook/engagement/volley/run_battle/pursuit/cascade bodies); percell.py (function map); geometry/engine/validators (maps) | [READ] |
| designs/audit/2026-05-28-resolution-diagnostic/* · 2026-05-28-engine-replacement/engine_replacement_reconciled.md · 2026-06-01-massbattle-stub-wiring/* · mass_battle_breakthrough_validation_2026-06-05.md · 2026-06-09-session-consolidation-master.md | full [READ] |
| skills/valoria-resolution-diagnostic/SKILL.md (repo, 352L) · skills/valoria-mechanic-audit/SKILL.md | full [READ] |

[GAP: canon/definitions.yaml — file does not exist; NERS criteria taken from PI <definitions>.]
[NULL: tests/audit/ checked for priors — four prior MB audits found and consumed; no other MB-scoped priors.]

---

## §1 — SYSTEM MAP: THREE CANON STRATA, ALL WORKINGS

Mass battle canon currently lives in three strata. Drift between them is **acknowledged canon process** ("engine leads, docs follow" — ED-899 follow-up note), not silent corruption; this audit's job is to map the drift precisely, not re-litigate it.

### 1a. Design-doc stratum (LAGGING)
`mass_battle_v30.md` Part A: 7-phase battle turn (Orders→Volley→Manoeuvre→Thread→Engagement→Cascade→Reform); Pool = min(Size,Command)+Command (PP-233); Off/Def pool split at Orders; TroopCount = Size×block_size (§A.3 scale table: Skirmish 10 → War 5000 per Size); deterministic Discipline degradation (PP-502/251); Morale triggers (50%/25% Size loss, broken, general lost) cap −3/phase with encirclement exception (PP-683), floor 1 with general present, rout contagion brake, Morale Cascade Ob 1 (ED-688); Command = ⌈(Cha+Cog)/2⌉ with two-stage general incapacitation (ED-898); formation table §A.6 with **flat dice mods**; tactics §A.8; terrain §A.9; Thread §A.10; rout/pursuit §A.12; campaign layer §A.13–14 (Reinforcement +1 Size/season to TARGET, Morale resets between battles PP-711, Discipline persists PP-712, Supply −100 Treasury/season, Levy restriction); §A.3b imposed geometry (41×21 grid). Part B: BG strategic resolution — pool = Σ(Martial)+floor(Mil/2), TN 7, margin ≥+2 win / ≤1 partial, tactic cards incl. Varfell Stratagem (PP-690). B.5 hybrid handoff with 3-point phase-lock (PP-103/250). Parts C–E: officer capture (1d20 ≤ Size lost), Battle Consequences (ED-542/743: MS −1/−2, Accord→1 on conquest, deferred IP/Strain via Accord≤1 territory counts, caps §E.4).

### 1b. Ledger stratum (DECIDED)
ED-899 (Jordan, 2026-06-02): PP-233 pool **set aside**; base exchange pool = COMMAND_POOL_MULT×Command = 2×Cmd; **Size enters outcomes only via Lanchester frontage**; Command DERIVED = clamp(round((2·Cha+Cog)/3),1,7); melee linear law p≈1.0 / volley square law p≈2.0 validated; constants class-B; **FOLLOW-UP: doc reconciliation not yet applied.** ED-905 (ratified 06-05): discipline decoupled from speed; reform_check wired with PP-241 gate; envelop/surge maneuvers; unit→subunit→cell targeting. ED-907 (provisional): FM three-level command architecture (doctrine/formation/role; 5–20 intervention windows). ED-909 (closed): formation taxonomy (unit-level Envelopment/RefusedFlank; subunit Line/Arrowhead/GappedLine; Horseshoe retired); residual: §A.6 dice-mods ↔ geometry mapping. ED-910 (open): recommendation against importing FM IP/OOP. ED-875 (OPEN, Gate G8). ED-876 resolved (Trigger-5 cliff → smooth escalator). ED-872 resolved-as-design-intent (no Pool-Floor-5; unit-deletion floor; Lane-C balance validation open). ED-800 closed (Volley pool = min(Size,Power)+Power) + ED-812 closed (volley dmg = net−DR, no ×(1+Power)). ED-898 canon (two-stage incapacitation).

### 1c. Engine stratum (LEADING)
`tests/sim/mass_battle/` package. Live resolution [READ: orchestration.py L978–1110, 1374–1700, 1776–2010, 2133–2320; config.py full]:

- **Pool:** `base_combat_pool` = 2×Command + discipline penalty (0/−1/−2/broken at ≥5/3–4/1–2/0) + stamina penalty, floor 1D (L1031–1110; COMMAND_POOL_MULT=2, config L140). Legacy min(Size,Cmd)+Cmd path retained behind COMMAND_SIGMA_ENABLED.
- **Exchange:** opposed contest — each side `roll_pool(pool) + σ_boost`, degree judged against the opponent's net (`compute_degree(a_net, max(1,b_net))`, L1680). **No Off/Def pool split exists in the engine.**
- **Δσ leverage head (Instance A):** octagon angle (×SIGMA_PER_D=0.2), puncture (momentum, defender-depth-absorbed, cap 3), charge shock + envelopment shock (du Picq, prep-gated), charge recoil vs braced wall (PC_CHARGE_RECOIL=6, Courtrai-calibrated), encirclement (−1), ranged-in-melee (−1.0σ), graded morale σ, fatigue σ, envelopment σ — summed, tanh-softcapped ±1.5σ, converted via ×0.8√pool (L1588–1666).
- **Casualties (melee):** K_LINEAR(12) × Lanchester linear strength (engaged contact columns × min(troops/cell,CELL_CAP=200)/100, /STRENGTH_REF=4) × max(0, DAMAGE_BY_DEGREE[deg](Power) − DR). Frontage-capped by construction (L1374–1392, 1689–96).
- **Volley:** pool = Power − volley discipline penalty, TN 6; dmg = max(0,net−RANGED_DR_DEFAULT=2) × K_SQUARE(0.25) × shooter effective_size × target density mult (floor/cap 0.5–2.0) — square law (L1776–1875).
- **Hooks (phase boundary, every TICKS_PER_PHASE=6 ticks):** stamina rotation by formation depth → deterministic cumulative discipline degradation (threshold 1.0 Size, asymmetry-gated) → morale (canonical 50%/25% Size-fraction triggers, +broken, +exhaustion term; cap −3; **no general floor at duel level** — Jordan directive 2026-06-03) → rout at morale ≤0 → rally (EMPTY, G-7) → reform (wired per PP-241, **default OFF** via REFORM_CHECK_ENABLED env pending re-baseline) → threadwork (EMPTY, G-9) (L245–440).
- **Battle loop:** run_battle max 18 ticks = 3 phases/turn (Jordan cap); simultaneous resolution (cached centroids, v21); volley+engagement damage applied together at turn end; volley HP conversion at ceil(h_per_size/2) (L1898–2010).
- **Between turns:** stamina +30; **morale +0** (recovery is a battle-boundary rule, PP-711, not turn-level) (L2133–34).
- **Multi-unit orchestrator:** morale cascade (Discipline check Ob 1), rout contagion (−1), freed-attacker flank (−1D), pursuit (Fast only; routing Slow/Standard no defence; Fast rearguard −2D; dmg = CASUALTY_SCALE(4)×net×(1+Power)−DR — non-Lanchester path), recall Ob 2 (L2229–2320).
- **Cell model (Jordan 2026-06-03):** CELL_FLOOR 40 / CELL_CAP 200 / SUBUNIT_ROUT_FLOOR 80 / MAX_UNIT_TROOPS 10000; battlefield 50×(30 deploy/10 gap); BLOCK_SIZE=100 (Company scale — **one scale realized**; §A.3's Skirmish→War table is a presentation mapping not yet parameterized in the engine).
- **FM scaffold:** troop_type→role gating present, data-only INERT (ED-907 route).
- **Formations:** flat shape mods RETIRED 2026-06-02 — "formations grant NO flat bonuses — effects emerge from geometry" (engine comment; ED-909-consistent).

**Validated state:** breakthrough validation 2026-06-05 (battery digest 7655743e5a91b238): command-dominates 100%; ShieldWall stops Wedge 97%; braced infantry stops frontal cavalry 100%; wedge correctly loses the frontal grind (Goldsworthy); casualty asymmetry winner ~6–16% vs loser ~37–55% (Sabin); Lanchester exponents melee p≈1.0 / volley p≈2.0 (ED-899 validation field).

---

## §2 — STAGE 0: CALIBRATION TABLE (skill §Stage 0)

| Row | Expected state | Verified |
|---|---|---|
| Pre-resolver faction engine NON-COMPLIANT (binary verdicts) | ED-874 ratified | ✓ ledger |
| Post-resolver compliant (graded margins) | domain_action_resolver_spec | ✓ [READ] |
| ER-2 sub-5D continuous divergence (no Ob−0.5 term) | engine_replacement_reconciled §2 | ✓ [READ] + reproduced §3.4 below |
| ED-884 Ob-floor resolution | ledger resolved | ✓ ledger |
| ED-876 Trigger-5 internals (cliff removed → smooth escalator) | commit 2327adc4 | ✓ ledger + Stage-0 row check |

**Stage 0: PASS** — calibration priors hold; the diagnostic instrument is sound.

---

## §3 — STAGE 1: RESOLUTION DIAGNOSTIC (Phases 0–6)

**Engine classification (skill §Instances):** the live exchange is **Instance A** (sigma-leverage rolling engine): stat differentials and situational advantages enter as Δσ on net successes over a pool-scaled noise floor. Volley is a TN-pool engine with a deterministic square-law multiplier (Instance B hybrid). Phase-boundary discipline is **deterministic** (Instance B). BG Part B is a margin-system TN-pool engine (unchanged since 05-28; re-verified, not re-derived).

### 3.1 Phase 0–1 — Identity & state space
State per unit: troops (continuous HP = TroopCount), effective_size = hp/100, Command 1–7 (derived (2Cha+Cog)/3 when Cha/Cog supplied [orchestration L978–988]), Discipline 0–7, Morale, Stamina 0–100, Power, DR, speed, shape/cells. Resolution variable: opposed net successes on d10 pools (TN 7; 1=−1, 10=+2 [params/core §die rule]). All state transitions graded; no binary verdicts anywhere in the live path. **P-i (graded outcomes): PASS.**

### 3.2 Phase 2 — Command leverage (exact convolution, live pool = 2×Cmd, opposed exchange)

P(win exchange) vs a fixed healthy Cmd-4 opponent; per-point derivative:

| Cmd | pool | P(win exch) | dP/pt |
|---|---|---|---|
| 1 | 2 | .176 | — |
| 2 | 4 | .286 | +.110 |
| 3 | 6 | .397 | +.111 |
| 4 | 8 | .500 | +.103 |
| 5 | 10 | .592 | +.092 |
| 6 | 12 | .671 | +.079 |
| 7 | 14 | .737 | +.066 |

Head-to-head +1-Command edge over mirror: Cmd2v1 +.152 → Cmd7v6 +.077 (ratio 1.97).

**Reading:** leverage is hotter at low Command — **ED-875's direction is CONFIRMED** — but in the operationally relevant opposed-exchange frame the non-uniformity is ≈2× low-vs-high, not the ~0.500/pt of ED-875's single-roll armature frame. Per-point heat at the bottom of the ladder (+.110–.152) is large but smooth (no cliff). Canon axiom "Generalship dominates; Command asymmetry is intentional" (mass_battle §A.1) is explicit intent evidence that elevated low-end leverage may be the intended early-game texture. **G8 remains Jordan's call (ED-875 open); this table is the decision input.** The deterministic+stochastic alternative recorded in ED-875 remains viable if the answer is "flatten it."

### 3.3 Phase 3 — Modifier leverage (P-ii) and the discrete/continuous split

A single small modifier (one YELLOW flank = −0.2σ on the defender), exact convolution at mirror pools:

| pool | discrete dP | P(tie)/2 | continuous-limit dP |
|---|---|---|---|
| 2 | +.124 | .124 | .056 |
| 4 | +.088 | .088 | .056 |
| 6 | +.072 | .072 | .056 |
| 8 | +.062 | .062 | .056 |
| 10 | +.056 | .056 | .056 |
| 14 | +.047 | .047 | .056 |

**Mechanism (verified exactly):** in the discrete engine the σ-boost (1.5·tanh(Δσ/1.5)·0.8·√pool ≈ 0.22–0.60 for one flank) is **sub-lattice** — nets are integers, so a sub-unit boost can only convert exact ties. Measured dP equals P(tie)/2 to three decimals at every pool. The continuous target implementation (Normal sampling, Godot) gives the uniform probit shift dP≈.056 by construction. So: **P-ii holds in the continuous target; the discrete sim's small-modifier leverage is tie-mass-driven** — hotter below pool ~10, cooler above. Stacked modifiers that cross the lattice (e.g. −2.5σ raw → capped −1.43σ → boost 1.6+) shift beyond tie conversion: measured dP +.33–.36 across pools 2–14 — **the tanh softcap bounds stacking (P-iii: PASS).** Consequence registered as F5: SIGMA_PER_D and friends were calibrated against discrete tie-breaking; a continuous re-baseline will shift effective flank/shock strength, and the Godot port needs the ER-2 correction (§3.4) for the same small-pool region. [CONFIDENCE: high — exact convolutions, decomposition verified.]

### 3.4 Phase 3b — ER-2 exposure inside mass battle

The engine rolls real dice (no exposure). The **Godot continuous implementation** of the same pools, without the Ob−0.5 continuity term (params/core §Continuous Engine — term not yet landed):

| pool | Ob | discrete | continuous raw | continuous +0.5 |
|---|---|---|---|---|
| 2 | 2 | .260 | .144 | .268 |
| 4 | 2 | .512 | .401 | .525 |
| 4 | 3 | .279 | .191 | .287 |
| 6 | 3 | .470 | .380 | .480 |
| 14 | 3 | .851 | .807 | .850 |

Cmd 1–2 generals fight at pools 2–4 **by design** — uncorrected continuous resolution would weaken low-Command armies by ~45% relative at the worst corner. The correction restores agreement to 1–3%. **F5 (P3): land the Ob−0.5 term before the Godot mass-battle port; mass-battle exposure is now quantified.**

### 3.5 Phase 4 — Floor and corner behavior
Worst corner: Cmd 1–2 with full penalty stack (disc 1–2 → −2, stamina 0 → −1) floors at 1D [orchestration L1031–1110] and still wins the exchange vs a healthy Cmd-4 12.5% of the time — graded, never zero. No Pool-Floor-5 by design (ED-872 resolved: unit-deletion floor is the protection); **Lane-C validation that units do not evaporate degenerately fast remains the open item** (ED-872 residual; the 06-05 casualty-asymmetry results are consistent with non-degenerate evaporation but were not a targeted Lane-C sweep). Morale floor-with-general (§A.4) is deliberately absent at duel level (no general entity in the duel; Jordan 2026-06-03) — a scoping decision, not drift; the floor's home is the multi-unit/battle level where ED-898 incapacitation lives (engine GAP, see F10).

### 3.6 Phase 5 — Casualty envelopes (all scales)
- **Melee (Lanchester linear):** E[degree payoff − DR] = 1.90 (mirror pool 8, Power 4, DR 1). Full-frontage lines: 19 cols @100 troops/cell → 108 dmg/tick; 10 cols @200 → 114 (density-compensating — frontage cap working); 5 cols @40 → 11.4. At 4,000-troop lines that is ~3%/tick → rout via the 50%/25% morale triggers decides battles well before annihilation. Matches the validated winner ~6–16% / loser ~37–55% asymmetry.
- **Volley (square law):** E[net | pool 3, TN6] = 1.59; E[max(0,net−2)] = .323. Casualties/tick = .323×0.25×eff_size×density: 1,000 archers ≈ 0.8–1.6; 10,000 archers ≈ 8.1–16.2. Over a 3-phase turn ≤ ~290 from a max-size unit — an attrition contributor, not a melee substitute (ED-812 intent holds). But the square law rewards **massing** ranged superlinearly and the kiting primitive can sustain the volley band: **ED-822 (ranged-composition balance) stays open with these sharper numbers.**
- **Pursuit/freed-attacker:** non-Lanchester flat paths (CASUALTY_SCALE×net×(1+Power)−DR) [L2229–2320]. Defensible — pursuit casualties are historically rout-driven, not frontage-driven (du Picq) — recorded as deliberate model boundary, not defect.

### 3.7 Phase 6 — Determinism boundaries
Deterministic subsystems behave per spec: discipline degradation (cumulative threshold 1.0 Size, asymmetry-gated [L329–346]) — note the engine uses **cumulative** loss vs the doc's per-turn framing (PP-502/251); equivalence under multi-phase turns is plausible but unproven (folded into F3 reconciliation, P3). Morale cap −3/phase enforced [L303]; encirclement exception (PP-683) is a doc-layer rule not surfaced in the duel hook (F10 scope note). Stamina drain 1/contact-cell/tick, depth-gated rotation recovery — graded fatigue, no cliffs.

**Stage 1 summary: P-i PASS · P-ii PASS-in-target (discrete tie nuance F5) · P-iii PASS · P-iv (state-space closure) PASS at engine level · P-v (no hidden binaries) PASS.**

---

## §4 — STAGE 2: LESSON MAPPING (skill lessons 1–6)

| Lesson | Status in live system |
|---|---|
| 1 — One variable, one role | PASS: numbers-in-contact lives only in the Lanchester term (run_battle opp_frac post-scaler skipped under LANCHESTER_ENABLED [L1689 comment]); Command lives only in the pool; quality lives only in degree payoff. |
| 2 — Graded everywhere | PASS (Phase 0–6 above). |
| 3 — Leverage uniformity | PASS in continuous target; discrete tie nuance (F5); Command-ladder heat is the open G8 *design* question, not a violation. |
| 4 — Softcap stacking | PASS (tanh ±1.5σ verified at stack). |
| 5 — Floors protect, not distort | PASS with Lane-C validation outstanding (ED-872). |
| 6 — Determinism where canon demands | PASS (discipline, reform gate, cell lifecycle); reform dormant by flag (F10). |

---

## §5 — STAGE 3: NERS VERDICT

### Engine level (unit-duel + multi-unit orchestrator, Instance A aggregate)
- **N (Necessity): PASS.** Every live mechanism earns its place: Command pool (generalship axiom), Δσ head (situational leverage), Lanchester pair (numbers, historically signed), degree spine (quality), hooks (state evolution). The retired flat formation mods were the necessity failure; their removal ("effects emerge from geometry") closed it.
- **E (Elegance): PASS.** One exchange primitive serves every melee interaction; advantages compose through one Δσ channel with one softcap; formations are geometry, not tables. Command ladder is smooth and legible (§3.2). The FM three-level architecture (ED-907) extends, rather than forks, this grammar.
- **R (Robustness): PASS WITH FLAGS.** Verified: floor corners graded, stacking capped, frontage-capped melee, density-bounded volley, simultaneous resolution (no first-arg bias), validated historical battery. Flags: (i) G8/ED-875 low-Command heat awaiting Jordan; (ii) Lane-C evaporation sweep not yet run (ED-872 residual); (iii) reform ratified-but-dormant and rally empty mean prolonged battles understate recovery (F10).
- **S (Sufficiency): PASS at engine level** for the engagement scale it models — every §A.4/§A.12 state variable has a live, graded transition. Declared-tactics/terrain/general-event remain GAP at engine level (06-01 audit recs 1–3 stand), **partially re-framed**: ED-907/ED-909 route tactics through roles/geometry rather than the doc's §A.8 table, so the gap is now "land FM modulation," not "port the table."

### System level (all strata, all scales)
- **S: PARTIAL.** Cause is no longer mechanical: it is tri-strata drift. The doc stratum teaches PP-233 pools, Off/Def splits, flat formation mods, ⌈(Cha+Cog)/2⌉ Command, 41×21 geometry, and a volley rationale (ED-753) that argues **against** a decision Jordan already made (ED-800) — while ledger+engine canon has moved (ED-899/905/909). A GM or implementer reading only the doc builds the wrong game. ED-899's FOLLOW-UP (doc reconciliation) is the named, still-open remedy; F1–F4 below give it a concrete worklist.
- **N/R/E at system level:** inherit engine PASS; BG Part B and the campaign/consequence layers (§A.13–14, Parts C–E, military_layer §1/§4) re-verified consistent with the 05-28 mapping plus the since-landed fixes (siege PP-715, PP-711/712, stalemate, stratagem, ED-743 caps). Cross-system loops bounded: Wealth-0 → HI/Cav Disc decay (military_layer §1.7, damped, recoverable); battle loss → Military −1 capped ±2/season (Part E §E.4); Accord ladder (§4.1) gates muster, no runaway found. [NULL: cross-system loop sweep — examined the six 05-28 MBL loops against current canon; no new unbounded loop found.]

**Hybrid B.5 note:** the 3-point phase-lock (PP-103/250) is written against the 7-phase doc procedure; the engine resolves in ticks×phases and ED-907 specifies 5–20 intervention windows. The phase-lock surface must be re-mapped onto intervention windows (add to the ED-909-residual class; F3 item 7).

**Overall verdict: COMPLIANT-WITH-BACKLOG → the backlog is now documentation + three named gates, not mechanics.** Materially stronger than 2026-05-28.

---

## §6 — STAGE 4: RE-TEST SPECIFICATION

1. **G8 decision test (after Jordan rules on ED-875):** re-run §3.2 table under the chosen model; acceptance = per-point dP profile matches the ruling (status quo: monotone declining, no cliff; flattened: ratio ≤1.3).
2. **Lane-C evaporation sweep (ED-872 residual):** mirrored armies Cmd 1–7 × disc 1–7, measure ticks-to-rout and loser casualty fraction; acceptance = no configuration routs in <1 phase from full strength and loser fraction stays in the validated 37–55% band ±10.
3. **Reform re-baseline:** REFORM_CHECK_ENABLED=1, re-run battery 7655743e…; acceptance = 13/13 scenarios hold or deviations are ratified as improvements; then flip default ON (closes F10a).
4. **Continuous-engine parity (post ER-2 landing):** Godot resolver vs discrete sim at pools 2/4/6, Ob 1–3 and one-flank scenarios; acceptance = |ΔP| ≤ 3% absolute (catches both §3.3 and §3.4).
5. **Doc reconciliation regression:** after F1–F4 edits, mechanic-audit pass over mass_battle_v30 + params/mass_combat; acceptance = zero contradictions with ED-899/905/909-era ledger on the F3 worklist items.
6. **ED-822 composition probe:** all-ranged vs balanced vs all-melee at equal troop budgets with and without kiting; deliver win-rate surface to the ED-822 thread.

---

## §7 — FINDINGS REGISTER (worst-first; none rise to P1)

| ID | Sev | Finding | Action |
|---|---|---|---|
| **F1** | **P2** | **ED-800 closed-but-unpropagated.** Jordan-decided Volley pool (min(Size,Power)+Power, 2026-05-11) implemented in NEITHER doc nor engine; doc §A.7 retains ED-753 rationale actively defending the superseded Power-only rule; engine implements Power-only pool **plus** square-law ×K_SQUARE×effective_size [orch L1867] — which delivers ED-800's purpose (massed ranged firepower) by a different, validated mechanism. | Jordan-visible reconciliation entry: ratify square-law route as superseding the ED-800 pool mechanism (or order the pool change). Staged §8 (ED-970). |
| **F2** | **P2** | **ED-910 grounded on absent control surface.** The open recommendation against importing FM IP/OOP cites the per-turn Off/Def pool split ("continuous dial… re-declarable at intervention windows") — that split exists only in the lagging doc stratum; the live engine has no Off/Def split (opposed single-pool exchange, §1c). The conclusion may survive via stance/roles, but the stated ground is false in leading canon. | Flag before adoption; re-ground or amend ED-910. Staged §8 (ED-971). |
| F3 | P2/P3 | **ED-899 FOLLOW-UP worklist (doc reconciliation), concretized:** (1) §A.4 pool formula → 2×Command; (2) Command derivation → (2Cha+Cog)/3 and resolve the **three NPC-Command sources** (doc §A.5 direct · military_layer §2.3 =Military · engine derived); (3) §A.6 flat mods vs retired-principle vs ED-909 taxonomy (ED-909 residual); (4) geometry trifecta 41×21 (doc §A.3b) / 25×25 (integration) / 50×30+10 (engine); (5) params "General killed −2" vs ED-898 two-stage; (6) params "Power derived from Size" header; (7) B.5 phase-lock → ED-907 intervention windows; (8) Off/Def split language (ties to F2); (9) discipline per-turn vs cumulative framing (§3.7). | Single reconciliation pass on mass_battle_v30 + params/mass_combat against the ED-899/905/907/909 ledger set. |
| F4 | P3 | mass_battle_integration_v30.md partially superseded (battlefield 25 vs 50; morale 30/50 vs canonical 50/25 restored; stamina constants drifted; LETHALITY route → K_LINEAR/CASUALTY_SCALE). | Mark PARTIALLY SUPERSEDED with pointer to engine package + ED-899. |
| F5 | P3 | **Small-pool fidelity pair:** (a) ER-2 Ob−0.5 term unlanded — mass-battle exposure quantified §3.4; (b) discrete sub-lattice modifiers act purely as tie-breakers (dP = P(tie)/2, §3.3) — class-B σ constants are calibrated against that behavior and will shift under continuous resolution. | Land ER-2 term in params/core; record the tie-breaking note beside SIGMA_PER_D; re-test #4. |
| F6 | status | ED-875/G8 quantified in the opposed frame (§3.2): direction confirmed, magnitude ≈2× low-vs-high (not 0.500/pt). Canon axiom supports "intended texture" as a defensible ruling; d+s alternative stands. | Attach table to ED-875 for Jordan. |
| F7 | P3 | params/mass_combat internal strata contradictions: PP-233 damage ×(1+Power) vs PARAMS-GAP-05 net+DmgMod−DR; thread-phase fragments (Phase 2/4/5 disagree); stale morale row; stale header comments. | Params consolidation pass (document_consolidation trigger). |
| F8 | P3 | military_layer §1.4 Prosperity tiers (1–3/4–5/6–7) contradict §5 PP-667 resolution (1–2/3–4/5). | One-line fix to whichever PP-667 ratified (ledger says §5 row is the resolution). |
| F9 | P3 | infill PP-MB-01 cites damage application at "Phase 5 Step 1"; skeleton says Phase 6 Step 1. | Typo fix. |
| F10 | P3 | Dormant/empty canonical mechanics: (a) reform ratified (ED-905) but default OFF pending re-baseline; (b) rally empty (G-7); (c) threadwork stub (G-9); (d) declared tactics/terrain/general-event engine GAPs (06-01 audit) re-framed by FM route; (e) §A.4 morale floor + PP-683 encirclement exception live only above duel level. | Re-test #3; FM modulation milestone tracks (b)–(d). |
| F11 | P3 | Ledger hygiene: ED-811 status open though superseded (04_ed811_superseded.md); ED-872 resolved with jordan_decision:pending field inconsistency. | Field fixes during the ★ID-conflict adjudication pass. |
| F12 | note | Test scenarios use Discipline 8 (>7 canon range); engine lacks a 1–7 stat clamp validator. | Add validator check; cosmetic. |

**Drift register summary:** doc↔ledger drift = F1, F3(1–8); doc↔doc = F7, F8, F9; ledger↔engine = F2, F10a, F11; spec↔engine = F4, F5b. All drift is mapped to an owner-action; none is silent.

---

## §8 — LEDGER-READY CANDIDATES (staged, NOT appended)

No P1 findings → no mandatory ledger append fired. F1/F2 are P2 canon-hygiene items that warrant entries; per the session-consolidation counsel (★ID-conflict backlog: pull clean lane-C IDs only, minimize churn pending adjudication), they are **staged here** for Jordan or the adjudication pass to append verbatim. Lane-C clean IDs used (next free per consolidation master: ED-970).

```jsonl
{"id":"ED-970","date":"2026-06-09","status":"open","severity":"P2","scope":"mass_battle/volley","title":"ED-800 closed-but-unpropagated — volley pool decision vs square-law implementation","finding":"Jordan-decided volley pool min(Size,Power)+Power (ED-800, 2026-05-11, status closed) is implemented in neither mass_battle_v30.md (§A.7 retains ED-753 rationale defending Power-only) nor the engine (Power-only pool, orchestration.py volley_phase). Engine delivers the decision's purpose (massed ranged firepower) via the validated Lanchester square-law term ×K_SQUARE×effective_size (ED-899, p≈2.0).","action":"Jordan ruling: (a) ratify square-law route as superseding the ED-800 pool mechanism and amend ED-800 resolution text + doc §A.7 rationale, or (b) order the pool change into engine+doc. Either closes the strand.","refs":["ED-800","ED-753","ED-812","ED-899"],"source":"designs/audit/2026-06-09-massbattle-comprehensive/massbattle_comprehensive_analysis.md §7 F1"}
{"id":"ED-971","date":"2026-06-09","status":"open","severity":"P2","scope":"mass_battle/fm_architecture","title":"ED-910 recommendation grounded on Off/Def split absent from leading canon","finding":"ED-910 (open) argues against importing FM IP/OOP partly on the per-turn Off/Def pool split as an existing 'continuous dial' re-declarable at intervention windows. The live engine has no Off/Def split (opposed single-pool exchange, base_combat_pool + sigma head); the split exists only in the lagging doc stratum (§A.7 Phase 1/5, PARAMS-GAP-04).","action":"Re-ground ED-910 on live control surfaces (stance, roles, ED-907 windows) or amend before Jordan adoption.","refs":["ED-910","ED-907","ED-899"],"source":"designs/audit/2026-06-09-massbattle-comprehensive/massbattle_comprehensive_analysis.md §7 F2"}
```

---

## §9 — CONSOLIDATED OPEN-JORDAN ITEMS (mass-battle scope)

| Item | Source | What Jordan decides |
|---|---|---|
| G8 low-Command leverage | ED-875 + §3.2 table | Intended texture vs flatten (d+s alternative) |
| ED-800 reconciliation | F1 / ED-970 | Square-law supersession vs pool change |
| ED-910 grounding | F2 / ED-971 | Re-ground or amend before adoption |
| ED-907 ratification | provisional | FM three-level architecture → canon |
| ED-909 residual | open class | §A.6 dice-mods ↔ geometry mapping; + B.5 phase-lock → windows (F3.7) |
| Lane-C evaporation sweep | ED-872 residual | Accept re-test #2 spec & run |
| Reform re-baseline | ED-905 / F10a | Authorize battery re-baseline, flip default |
| ED-822 ranged composition | open | Accept re-test #6 probe spec |
| ★ ID-conflict adjudication | consolidation master | Unblocks F11 + ledger appends incl. §8 |

---

## §10 — CONFIDENCE & LIMITS

[CONFIDENCE: high] on everything cited to read source + exact convolution (§§1–3, 5, 7). [CONFIDENCE: medium — sampled, not exhaustively re-run] on the 06-05 validation battery (cited at digest 7655743e5a91b238, not re-executed) and on percell.py internals (function map + call-site reads; not line-audited — its mechanisms are exercised by the validated battery). [GAP: live Lane-C sweep and reform re-baseline — specified in §6, not executed this session; running them was out of audit scope without a Jordan-authorized baseline change.] [GAP: canon/definitions.yaml absent — NERS criteria per PI.] BG Part B re-verified against 05-28 mapping rather than re-derived (no ledger or engine activity touches it since).

**Audit trail:** [READ] entries §0.1 · [NULL] tests/audit priors + cross-system loop sweep (§5) · [CORRECTION: §3.3 decomposition — initial tie/2+Normal additive prediction rejected; measured dP = P(tie)/2 exactly for sub-lattice boosts] · [ASSUMPTION: BLOCK_SIZE=100 = Company scale is the single engine-realized scale; §A.3 multi-scale is presentation mapping — basis: config.py L38 comment + no scale parameter in engine] · no fabricated findings; F-register strength matches evidence per entry.
