# Threadwork Resolution Diagnostic — 2026-06-11
**Pipeline:** valoria-resolution-diagnostic (Stage 1 Phases 0–6 → Stage 2 lesson mapping → Stage 3 NERS resolution-fitness verdict → Stage 4 fix re-test), with the two requested lenses — **σ-leverage** and **determinate–stochastic boundary** — built into Phases 2–3.
**Companion files:** `sigma_results_2026-06-11.md` (exact-convolution tables T1–T10, cited as T*n* below), `ners_alldirections_threadwork_2026-06-11.md`, `threadwork_crosssystem_mapping_2026-06-11.md`.

## §0 Evidence trail (this session)
[READ: params/core.md — full (face rule, degree table, Continuous Engine Decision E, Ob ladder, Momentum, PP-255/261)]
[READ: params/threadwork.md — full re-verification (PP-603/604/606/607/616/619/632/633, TN modifiers, Mending block)]
[READ: designs/threadwork/threadwork_v30.md + infill — targeted re-reads: §2.3 Leap, §2.4 ops, §2.5 collective, §2.6 opposing, §3.2–3.7, fatigue ED-694, infill l.38/89/121]
[READ: designs/scene/derived_stats_v30.md — re-fetched (stale); §1 duality, §13, Thread Pool row, wound rule]
[READ: designs/scene/combat_v30.md §10 — full section; designs/scene/social_contest_v30.md §9.4/9.4b; designs/provincial/mass_battle_v30.md §A.7/§A.10; designs/scene/investigation_systems_v30.md Case Board Thread Layer]
[READ: designs/articulation/articulation_layer_v30.md — re-fetched (stale overnight)]
[READ: canon/editorial_ledger.jsonl — ED-911 verbatim; thread-relevant entries re-checked]
[CORRECTION: yesterday's record stated thread TNs as 7/8/9; this session's first pass "corrected" that to 7/8 from params/core's summary line — **that correction was itself wrong.** The full params/threadwork TN Modifiers table (PP-619, four rows, read in full this session) is: standard ops 7; Binding (Lock/Dissolution) 8; POP 8; **POP Binding 9**. Day-1's 7/8/9 stands. New P3: params/core's one-line TN summary and its EV table both omit TN 9 (E[net]=0.2 per params/threadwork's own probability reference; σ=0.748 by the face rule).]

---

## STAGE 1 — DIAGNOSTIC

### Phase 0 — Decomposition (determinate–stochastic map)

| Component | Kind | Category | Notes |
|---|---|---|---|
| Leap roll | dice | pool roll | (Spirit×2)+History+TPS (TPS = TS÷10), min 5, −1D/Wound; TN 7; Ob 2 (TS 30–49) / 1 (TS 50+) — v30 §2.3 |
| Operation rolls (Weave/Pull/Lock/Dissolve/Mend) | dice | pool roll | same pool; TN ladder 7 / 8 / 9 (standard / Binding or POP / POP-Binding, PP-619 four-row table); Ob = Depth(1/2/3/5/8/13)+Breadth(0–4)+Distance(0–3) — params |
| Opposing / collective ops | dice | pool roll | §2.6 engagement mod +floor(opp TPS/2); §2.5 helper +floor(Cog÷2)D |
| Fallout (band entry) | dice | flat d6 | §3.6 — perceptual effects, no numeric stakes |
| Crisis arc (Anchoring + resolution) | dice | pool roll | Bonds TN7 Ob2 ×3; then Bonds+scenes TN7 Ob3 — §3.7 [PROVISIONAL] |
| Dissonance (bystanders) | dice | Spirit check | TN7 vs Dissonance Factor — PP-607/610 |
| Coherence ledger | **determinate** | continuous resource (10→0) | per-op costs §3.2, per-op cap (see RD-2), recovery §3.5 — no roll |
| RS/MS ledger | **determinate** | discrete accumulator (0–100) | breach n, drain n/season, Mending credits, WC track, baseline −1/yr PP-255 — no roll |
| Gap timers | **determinate** | countdown clock | self-closure 1/2/4/8/32 seasons — PP-604 |
| Thread Fatigue | **determinate** | accumulator (Spirit×5) | costs 3/2/4/5/7/10 — ED-694; the per-contact governor |
| Knot strain | **determinate accrual** | accumulator (cap 4/7 [Option A]) | session-paced; rupture stochastic only via triggers |
| Substrate Saturation | **determinate** | accumulator | PP-606 |

**Boundary discipline (the determinate–stochastic finding of merit):** every irreversible or world-scale consequence in threadwork is **determinate** — RS breach, Gap depth, drain, fatigue, Coherence cost are all computed, not rolled. Dice decide only (a) whether contact/effect is achieved and at what degree, and (b) flavor (Fallout, co-movement selection). The two exceptions where dice sit on irreversible outcomes are the **Dissolution degree ladder** (Failure ⇒ Gap at n+2 — a roll *worsening* the world beyond intent, PP-604) and the **Crisis arc** (Failure ⇒ NPC). Both are examined in Phase 2. Additionally, **Momentum is barred from Thread rolls** (params/core: "non-Thread rolls only") — the one safety-valve every sibling system has is deliberately withheld here; the substrate is indifferent to narrative momentum. Architecture-level verdict: the placement of dice vs accounting is *unusually disciplined* — better than any sibling system audited to date.

### Phase 1 — Stress points

**1a. Dice floors.**
- *By design:* Thread Pool min 5 (derived_stats §14 row "Thread Pool, min 5, range 5–17D+") — the formula floor sits exactly at the Normal-approximation boundary the skill names.
- *After degradation:* the floor does **not** survive wounds. Wound −1D is applied to the computed pool (universal rule, derived_stats §4.1 / v30 §2.3 PP-716); engine minimum is 1D (params/core Pool Minimum). A 3-wound floor practitioner Leaps at 2D: P(Success-or-better at Ob 2) = 26% exact, Failure 42% (T4). Leap-failure aftereffect −1D TPS (PP-232) compounds within the scene: a second attempt rolls 1D.
- *Deterministic steepest point:* MS Critical band (19–1): +1 Ob worldwide + doubled spontaneous-Gap risk + faction Stability checks — three couplings keyed to one band (intended, P-14 cumulative, legible).
- *Shallowest clock:* Distant-Knot strain capacity 4 [Option A]; Anchoring-based Coherence recovery charges +1 strain per scene (§3.5) — four recovery scenes break a Distant Knot from zero.

**1b. Exposure.**
- Wounded-practitioner Leaps: routine in any combat-adjacent play (combat_v30 §10 expects practitioners in combat; wounds are the normal combat output). Exposure **High**.
- Crisis arc: reached only at Coherence 0 — a state the fatigue governor and per-op cap make hard to reach accidentally (PP-501 worked example: 9+ consecutive ops from full to reach Severance; mass_battle A.10). Designed-rare. Exposure **Low**, by construction.
- Dissolution Failure ⇒ n+2: exposed every time Dissolution is rolled (TN 8, the hardest roll class). Failure dominates this roll class across the played range: even at TN 7, Ob 8 succeeds only 16.4% at 12D (T1), and TN 8 sits strictly below the TN 7 column at every pool (T3). Exposure **Medium-High** for any campaign featuring FR play.

### Phase 2 — What the stress points decide (+ σ-leverage lens)

| Stress point | Outcome type | Stakes | Risk (Impact/Exposure/Irrev.) |
|---|---|---|---|
| Wounded Leap (1–4D) | graded, mild ladder (worst: fail + −1D TPS scene) | recoverable | L / H / L — **pass**: the Leap's own ladder is the system's safety valve; failure costs tempo, not state |
| Dissolution roll (any pool) | graded with **inverted tail**: Failure ⇒ Gap n+2, breach + decades of drain (PP-604: n=5 ⇒ 155 RS untouched) | world-scale, semi-irreversible (self-closure 32 seasons / Mending Ob 12) | **H / M-H / H — candidate finding RD-1** |
| Crisis arc resolution | 4-degree ladder; Failure ⇒ NPC (permanent) | irreversible-load-bearing | H / L / H — **candidate finding RD-3** (entry gate, not the roll itself) |
| Opposing ops at parity | tie ⇒ Shifting Object + both pay | recoverable | L / M / L — pass (T7: symmetric meet-meet 25–45%; mutual-cost design suppresses thread duels, Einhir-consistent) |

**σ-leverage (T2, exact).** Per-die statistics (params/core): TN7 E=0.4, σ=0.8. In σ-units a **+1 Ob carries 2.5× the leverage of +1D at every pool** (1/0.8√N vs 0.4/0.8√N), and both decay as 1/√N: at the 5D floor +1 Ob = 0.56σ (−18.2pp on P(Success) at Ob 3); at 17D it is 0.30σ (−6.4pp). Threadwork's penalty design is **almost entirely Ob-sided** (Coherence bands +1/+2, MS bands +1, seasonal Mending fatigue +1, age +1/+2, opposing engagement +1..+5, sequential-failure) — which means penalties bite hardest exactly where pools are weakest, a deliberate regressive curve that matches the Einhir asymmetry (the strained practitioner is punished super-linearly) but must be understood as such: **stacked Ob is the system's true difficulty axis; dice are almost cosmetic against it** (T1: at 5D, Ob 5 ⇒ 8.3%, Ob 8 ⇒ 0.1%). TN as a lever: Binding's TN 8 costs 25–40% of success probability relative to TN 7 across the played range (T3) — a flat-feeling switch with large effect; per-die E drops 0.4→0.3, so in σ-units the TN penalty *grows* with pool (0.125√N σ): the engine's only modifier that punishes large pools more than small ones, which is why Binding stays hard even for masters. This is coherent, not accidental — but no design doc states the Ob-vs-dice-vs-TN leverage hierarchy anywhere; it is implicit. **RD-7 (P3): record the leverage hierarchy in params/core so future modifiers are placed on the intended axis.**

### Phase 3 — Effect curves

**3a. Impact uniformity.** Coherence is a continuous resource; its per-op costs are absolute steps (−1 capped; FR −1..−3). On a 10-point track with thresholds at 8/5/3/2/1/0, a −1 step is *position-dependent* in effect (mid-band: nothing; at a boundary: Fallout roll + new penalties) — but the bands are explicit, spaced, documented thresholds, exempt per Lesson 6's intended-thresholds clause. The genuinely non-uniform instrument is the **permanent −1 TS** from Crisis-arc Success/Overwhelming: at TS 30–31 it is Thread-career-ending (TS 29 < Leap gate), at TS 60 it is a rounding error to TPS. PP-206 documents this exact non-uniformity as **intended** with an informed-choice safeguard (disclosure before the arc). Phase 5: deliberate-with-safeguard → pass, cite PP-206.

**3b. Threshold cliffs.** Checked for *stacked unrelated* cliffs: Coherence boundaries carry one band-transition each; MS bands are cumulative by declared rule (P-14); the one stacking point is MS ≤ 10 (inside Critical) adding NPC coup-trigger bonuses on top of Critical's effects — intended escalation, legible, documented (v30 §5.3). The **A.10 mass-battle scale table** keys thread Ob and Coherence cost to battle scale via the dead Territorial taxonomy (N2's reach extends into mass_battle_v30 §A.10) — a record defect, not a curve defect. **No accidental cliff stack found.** [NULL: cliff-stack scan across §3.3, §5.3, PP-604, A.10 — examined, none beyond intended thresholds.]

**3c. Role conflation.** Coherence carries one role (personal rendering integrity) with radiating expressions (social −D, op +Ob, Knot pacing, Certainty cap) — single axis, single job; not a Lesson-1 case. TS carries **two** roles: capability input (TPS = TS÷10 feeds the pool) and gate (30/50/70 thresholds for Leap/Ob-reduction/POP) — but the gate values are *positions on the same capability axis*, the same pattern as "Bonds caps Disposition": one variable, one meaning, multiple readers. Pass, with a watch-note: if future design adds TS-spend mechanics (TS as currency), the conflation becomes real.

### Phase 4 — Loops (inter-system edges listed explicitly)

| # | Loop | Path | Damper (gain < 1/cycle?) | Cap | Verdict |
|---|---|---|---|---|---|
| L1 | Personal ambition spiral | op → Coherence loss → band +Ob → more failures → re-attempts → more ops | **Yes, three:** per-op cap −1 (RD-2 establishes the total-cap reading); fatigue governor (ED-694: Dissolution once-per-contact below Spirit 5 — T8); recovery +1/season + Anchoring (§3.5) | Coherence 0 → Crisis arc (a bound **with a recovery path** — unlike the faction-collapse precedent, not bare termination) | **Pass.** Gain per season << 1 under the cap reading; voluntary exit (restraint) always available |
| L2 | World spiral | Dissolution → Gap → drain → MS band ↓ → +1 Ob → more Failures → Gaps at n+2 → … | **Conditional:** self-closure (PP-604), Mending discount (Depth−1), WC track (+1D peninsula-wide at WC1; +2 RS/season at WC3), Sanctuary | MS 0 = Rupture — **termination, not a bound** | **Deliberate-with-safeguard → pass with citation.** The 132-register §F analysis + sim_mending_coherence establish the WC3-or-Rupture endgame as the designed loss condition (intent_of_game's own positive loop). Safeguard is adequate *iff* WC is reachable — re-validated by sims. Baseline decay −1/yr (PP-255) means the do-nothing trajectory loses in ~60 years (T9): the campaign clock is real but slow |
| L3 | Knot-recovery strain loop | Coherence recovery via Anchoring → Knot +1 strain → capacity breach → Broken/Ruptured → (params PP-632: Loss ⇒ −1 Coherence) → need more recovery | Session-paced strain; player-visible budget (4/7); PP-633 caps simultaneous-rupture Composure at floor(Composure×0.75) | Roster-bounded (−1 Coherence × #Knots, Knot Max = floor(Bonds/2)+1) | **Pass** — damped and bounded; the tension is a designed trade (the ladder out of Crisis consumes the rope) |
| L4 | Cross-system: combat ↔ thread | wound → −1D thread pools → weaker Mending → (no return edge: thread failure does not wound, except FR-rupture +1 Wound and co-movement actual results) | one-directional in the dangerous direction | n/a | **Pass** — not a loop; a drain with mostly one-way coupling |
| L5 | Cross-system: MS → faction → ? | MS Critical → faction Stability checks → Mandate loss → Faction Fracture → *(does fracture raise thread activity?)* | engine-AI dependent; no canonical return edge found | — | **[UNGROUNDED return edge]** — no canonical mechanism makes fractured factions perform more Thread ops; flagged for the NPC-doctrine layer (ED-679) to keep it that way |

**The load-bearing negative result:** no loop in threadwork is both undamped and unbounded. [NULL: loop scan incl. cross-system edges per Phase 4a — L1–L5 enumerated; none violate Lesson 5.]

### Phase 5 — Intent gates (rulings used)
PP-206 (TS-30 disclosure) — documented intent. Rupture-as-loss (v30 §5.3 "campaign ends in catastrophe") — documented intent. Einhir asymmetry (philosophical reference: "rewards restraint, punishes ambition") — documented intent anchoring the regressive Ob curve and Momentum exclusion. Dissolution n+2 inverted tail — **no design-doc statement found naming the worse-than-intended-Gap-on-Failure as purposive**; carried as `[INTENT UNDETERMINED]` → RD-1 stands. Crisis-arc relational gate — `[INTENT UNDETERMINED]` (Einhir-coherent but unstated) → RD-3 stands.

### Phase 6 — Findings triage (worst-first)

| # | Finding | Component | Sev | Impact/Exp/Irrev |
|---|---|---|---|---|
| **RD-1** | Engine duality is **not equivalent at degree thresholds**: continuous Normal (params/core Decision E, as specified — no continuity correction) understates P(net≥Ob) vs the discrete engine by up to **10.0pp at the Leap's modal case (5D, Ob 2: 60.0% vs 50.0%)**; divergence is worst exactly in threadwork's operating region (floor pools, high Ob) — T6. ED-836's "statistically equivalent" was validated on mean/std only. **Pre-existing record: ED-873 (2026-05-28, open, P3) already stages the identical one-line fix** — this finding does not duplicate it; it adds exact-convolution confirmation (vs ED-873's MC) and the threadwork exposure case that argues a **severity revisit P3→P1**: the divergence lands on the game's single most common roll, and Godot players would face a measurably harder game than the design tables promise. | continuous engine | **P1 (amends ED-873, currently P3)** | H/H/M |
| **RD-2** | Per-operation Coherence cap is canonical-in-effect but **homeless and contradicted**: cap text lives only in the infill (l.121); four witnesses fix its meaning as *total −1 for non-FR* (infill l.121; §3.4 residue interaction "base operation cost = −1, already capped" at Relational+; TW-05 POP ruling; PP-196 FR-exemption arithmetic) while **mass_battle §A.10's War row (−2/op) and §3.2's own −2 Structural row contradict it**, and A.10 cites the cap to "threadwork_v30 §3.2" where no cap text exists. | Coherence accounting | **P1** | M/H/M |
| **RD-3** | Coherence-0 rule is split and gapped: params/core PP-261 ("at 0: NPC… see params_threadwork for full rule") points at a file containing **nothing** on Coherence 0; the actual arc is v30 §3.7 [PROVISIONAL] (PP-194); the no-Close-Knot case (arc entry impossible → NPC with no attempt) is **unstated**; PP-261-vs-PP-194 sequencing (immediate NPC vs season-end arc) unreconciled. The math is not the defect: Close-Knot formation requires PC Bonds ≥ 5 (knots_v30 §3.2 prereq 5, derived from Disposition-ceiling = Bonds, PP-684; implicit gate surfaced by ED-780 per knots_v30 §3.4), so the live Crisis rows are Bonds 5–7 ⇒ P(NPC) 9–14% (T5); lower-Bonds rows computed for completeness only. | Crisis arc | **P1** | H/L/H |
| **RD-4** | Dissolution Failure ⇒ Gap n+2 (PP-604): a die outcome *escalates* world damage beyond declared intent; at n=3 Failure ⇒ n=5 (32-season, 155-RS object); **n=5 Failure ⇒ n=7, off-table/undefined**. `[INTENT UNDETERMINED]` on the escalation; the n+2>5 cell is a hard gap either way. | Dissolution | **P2** | H/M/H (escalation) + record gap |
| **RD-5** | params/core Quick-Reference P-columns are **inconsistent with the canonical face rule**: exact convolution gives 6D = 83/67/47 vs the table's ~83/63/40 (and similar drift at every row, up to 7pp at P(≥3)); the E[Net] column and the params/threadwork 22D-Ob13≈16% key both match the canonical rule (16.2% exact). The published eyeball-table designers calibrate against is stale. | engine docs | **P2** | M/H/L |
| **RD-6** | Fallout d6 tables each have an undefined face (Fragmented: no 3; Fractured: no 1) — v30 §3.6. A d6 result with no entry. | Fallout | **P3** | L/M/L |
| **RD-7** | Modifier-leverage hierarchy (Ob ≈ 2.5× dice; TN grows with pool) is real, coherent, and **nowhere stated** — future design will misplace modifiers without it. | engine docs | **P3** | guidance |

---

## STAGE 2 — LESSON MAPPING

| Finding | Lesson(s) | Remediation |
|---|---|---|
| RD-1 | **None of the six** — the defect is in the *engine duality contract*, not in resolution architecture. Per the skill's mapping rule this is surfaced explicitly as outside the lesson set: a **seventh-lesson candidate** — *"Two specifications of one engine must be equivalence-tested on the statistics players experience (degree probabilities), not on moments."* | **Execute ED-873's staged one-line edit** (classify on `net ≥ Ob − 0.5`); residual divergence ≤ 1.01pp (T10, exact — confirms ED-873's MC figure). Re-run Phase-5 sim with degree-classification comparison. In-canon precedent: params/threadwork's own probability reference already computes "with continuity correction" (its 16%/22% key values match exact convolution for that reason) — the fix imports existing house practice into core. Severity-revisit P3→P1 staged for Jordan with the T6 exposure case. |
| RD-2 | Lesson 2 (uniform-impact steps on a continuous resource — the cap *is* the uniformity instrument; its absence at A.10 re-introduces −2 steps) + record hygiene | Hoist cap text from infill l.121 into §3.2 (N8 batch); restate as: "non-FR operations: total Coherence cost capped at −1; FR exempt per PP-196; residue interaction per §3.4." Correct A.10 War row to the FR arithmetic it presumably means (−3 if FR, −1 if not) — **Jordan ruling on which** ; fix A.10's dangling §3.2 cite. |
| RD-3 | Lesson 4 (the arc **is** the clock that routes the unavoidable terminal roll — it just needs its entry conditions and fallback stated) + Lesson 6 (the silent no-Knot cliff) | Single canonical home: move §3.7 (de-provisionalized or re-confirmed) into params/threadwork; PP-261 pointer made true; add the explicit no-Close-Knot rule (Jordan: straight-to-NPC per Einhir, or a degraded solo arc). |
| RD-4 | Lesson 3 (dice should not *worsen* an irreversible world outcome beyond declared scale) | Options for Jordan: (a) Failure ⇒ Gap at n (intent scale) + practitioner-side consequence instead of escalation; (b) keep escalation, cap at n=5, define the n+2>5 cell as Foundational; (c) keep as-is + document intent. Math note: under (b) the n=5 Failure cell needs an explicit rule regardless. |
| RD-5 | — (documentation) | Regenerate the Quick-Reference from the canonical rule (T1 column supplies values); annotate generation method. Claude-executable. |
| RD-6 | — (completeness) | Two entries to author (creative-adjacent flavor: **flag for Jordan**, not invented here). |
| RD-7 | — (guidance) | One paragraph in params/core §Expected Value stating the leverage hierarchy with the T2 numbers. Claude-executable. |

---

## STAGE 3 — NERS VERDICT (resolution-fitness lens)

```
SYSTEM: Threadwork    COMPONENTS: dice + deterministic + clock (Phase 0)
VERDICT: NERS-compliant at the resolution-architecture level — with one P1 engine-contract
defect (RD-1) that is not threadwork's own but bites threadwork hardest, and two P1 record
defects (RD-2, RD-3) on canonical homes for rules that are sound in substance.

N: pass — every roll and ledger earns its place; fatigue governor, per-op cap, and Momentum
   exclusion are each load-bearing. No redundant apparatus found.
R: pass-with-findings — holds at its extremes BY DESIGN (wounded-Leap floor degrades
   gracefully; Crisis arc odds reasonable for its reachable population), but RD-1 (engine
   divergence at the floor), RD-4 (undefined n+2>5 cell), and RD-6 (Fallout holes) are
   completeness wounds: "fully formed, error-free" fails on those three cells.
S: pass at the dice layer (Phase-0 boundary discipline is the best audited to date; co-movement,
   visibility, and cross-system fire integrate cleanly) — but inherits yesterday's record-layer
   S findings (N1–N11) unchanged, plus RD-2's homeless cap.
E: pass — the Ob-axis difficulty curve, fatigue throttle, and restraint-rewarding loop economy
   are intuitable from simple choices; the σ-leverage hierarchy is coherent even unstated.
```

## STAGE 4 — RE-TEST OF PROPOSED FIXES
- RD-1 fix (continuity correction): re-tested against Phases 3–4 — introduces no new threshold (the correction is uniform), no loop, no added apparatus (one formula term). Residual 1.01pp max (T10). **Clean.**
- RD-2 fix (hoist + restate cap): re-test catches one hazard — restating the cap in §3.2 while the N2 taxonomy restatement is pending could fossilize Territorial wording; **sequence the cap hoist after or with the N2 ruling** (workplan dependency, Phase A→B).
- RD-3 fix (single home + explicit no-Knot rule): if Jordan picks "straight-to-NPC," re-test flags a Lesson-6 echo (a silent prerequisite becomes an explicit cliff — acceptable because legible and Einhir-grounded); if "degraded solo arc," re-test demands the solo pool be defined off Bonds (else pool 0) — propose Spirit-based, which re-introduces a small-pool terminal roll (Lesson 3 tension) → prefer a deterministic solo outcome (e.g., automatic Coh 1 + permanent −1 TS, no roll). **Carried as the recommended shape.**
- RD-4 options: (a) re-tests clean; (b) re-tests clean with the n=5 cell defined; (c) documentation-only.
- RD-5/RD-7: documentation; no re-test surface. RD-6: content authorship, Jordan.

[CONFIDENCE: high — every probability cited is exact convolution under the canonical face rule, reproducible from sigma_results T-tables; intent rulings cite their design-doc anchors; the two INTENT-UNDETERMINED flags are carried, not resolved by guess.]
