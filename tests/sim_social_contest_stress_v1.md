# SOCIAL CONTEST STRESS TEST — v1
## Date: 2026-04-08
## Model: Claude Sonnet 4.6
## Canonical sources: designs/debate/debate_system_redesign_v1.md Part 6 (operative) + references/params_debate.md
## Modes run: A (isolation), B (interaction chains), C (scenario), D (edge cases)

---

## FETCH LOG
- `references/canonical_sources.yaml`: ✓ (156 lines)
- `designs/debate/debate_system_redesign_v1.md`: ✓ (787 lines)
- `references/params_debate.md`: ✓ (366 lines)
- `canon/02_canon_constraints.md`: ✓ (25 lines)
- `skills/valoria-simulator/SKILL.md`: ✓ (199 lines)

---

## CRITICAL PREAMBLE: DESIGN DOC vs PARAMS CONFLICTS

Before findings: **params_debate.md diverges from the operative Part 6 of the canonical design doc on multiple core mechanics.** These conflicts are P1 findings (the system cannot be run consistently from either source alone). They are listed first because they invalidate portions of any simulation.

| Mechanic | Design Doc (Part 6, canonical) | Params (patch-modified) | Status |
|----------|-------------------------------|------------------------|--------|
| Argue pool stat | Presence × 2 | Cognition × 2 (PP-232) | **P1 — params not backported to design doc** |
| Initiative stat | Presence (§6.3) | Attunement (PP-232) | **P1 — same PP-232 backport gap** |
| Interaction taxonomy | CLASH / COMPETITION / DIVERGENCE | CLASH / AMPLIFY / CROSS / DIVERGE-state | **P1 — incompatible taxonomies** |
| Obscuring orientation | No CT movement, DM placed (§6.4) | ow=0.75 (reduced CT movement) | **P1 — mechanically incompatible** |
| Composure formula | Poise + Bonds + 3 (§6.2) | Poise deprecated, ED-127 unresolved | **P1 — Composure formula unknown** |
| Presence modifier | Defined in §6.2, used in pool | Unclear if still applies after PP-232 | P2 — GAP-NEW-03 |

**Simulation below uses params where patches are confirmed (Cognition pool, Attunement initiative, PP-278 resistance) and flags where design doc and params conflict.**

---

## MODE A — SINGLE MECHANIC ISOLATION

### A-1: Argue Pool
**Pool formula (params PP-232, confirmed by SIM-D-05):** (Cognition × 2) + History bonus, TN 7

| Cog | Hist | Pool | E[net] | P(≥1 net) | P(≥2 net) | P(≥3 net) |
|-----|------|------|--------|-----------|-----------|-----------|
| 2 | 0 | 4D | 1.2 | 71% | 41% | 16% |
| 3 | 0 | 6D | 1.8 | 80% | 58% | 33% |
| 3 | 2 | 8D | 2.4 | 85% | 69% | 48% |
| 4 | 1 | 9D | 2.7 | 87% | 73% | 54% |
| 4 | 2 | 10D | 3.0 | 89% | 77% | 60% |
| 5 | 2 | 12D | 3.6 | 92% | 83% | 69% |
| 5 | 3 | 13D | 3.9 | 93% | 85% | 73% |

**Degenerate ceiling:** Cognition=6, History=3 → 15D. E[net]=4.5. At this pool, expected margin over a typical 8D opponent ≈ 2.1. CT movement nearly guaranteed in every exchange. Design-level concern: top-end scholars trivialise the contest unless facing similar pools.

**Degenerate floor:** Cognition=2, History=0 → 4D. E[net]=1.2. 29% chance of 0 net successes. Against a 13D opponent: expected margin against them ≈ 3. This character cannot meaningfully contest a skilled debater.

**Memory bonus (+2D):** Shifts 4D→6D (significant), 13D→15D (marginal). Most impactful at low pool sizes. No stated frequency limit — see GAP-NEW-01.

### A-2: Resistance Formula (PP-278)
**Formula:** `resistance = ceil(average_stability / 4)`

| Avg Stability | Resistance |
|--------------|------------|
| 1–4 | 1 |
| 5–8 | 2 |
| 9–12 | 3 (theoretical max; Stability 7 is dataset max → resistance max = 2) |

**Finding:** With faction Stability range 1–7, practical resistance range is 1–2. The PP-295/ED-164 cap of 5 is redundant — PP-278 formula already caps at 2.

### A-3: Conviction Track Movement
**Formula:** `CT Δ = floor(margin × gw × ow) − resistance` if positive, else 0

**Minimum winning margin to move CT:**

| Genre weight | Resistance | Min margin needed | CT Δ at min |
|-------------|-----------|-----------------|-------------|
| 0.5 (off-primary) | 1 | 4 | 1 |
| 0.5 (off-primary) | 2 | 6 | 1 |
| 1.0 (primary) | 1 | 2 | 1 |
| 1.0 (primary) | 2 | 3 | 1 |
| 1.5 (boosted) | 1 | 2 | 2 |
| 1.5 (boosted) | 2 | 2 | 1 |

**Finding — off-primary genre dead zone:** Using a genre the audience doesn't value (gw=0.5) requires winning by margin≥4 to move the CT even 1 step against resist=1. Against a resistant audience (resist=2), margin≥6 required. Expected margin for equal pools ≈ 0. **Off-primary genre argues are essentially wasted against any audience with Stability≥5.** This may be intentional (rewards genre reading) but creates a dominant strategy: always match the audience's boosted genre.

### A-4: Concentration Depletion
**Formula:** Concentration = Focus + Presence. Depletes -1/exchange, -1 additional on exchange loss.

| Focus | Pres | Conc | Grand Debate (5 ex, 3 losses) | Formal (3 ex, 2 losses) |
|-------|------|------|------------------------------|------------------------|
| 1 | 2 | 3 | Spent after Exchange 2 | Spent after Exchange 2 |
| 2 | 3 | 5 | Spent after Exchange 3 | Survives (barely) |
| 3 | 3 | 6 | Near-Spent by Exchange 5 | Survives |
| 4 | 4 | 8 | Survives with margin | Survives comfortably |

**Finding:** Grand Debates systematically push low-Focus characters to Spent, often mid-debate. Focus≥4 is needed to reliably survive a 5-exchange Grand Debate while losing half the exchanges. This functions as intended (Focus = debate stamina) but characters with Focus 1–2 should expect Spent to fire in any extended debate.

### A-5: Strain Formula (CLASH)
**Formula:** `strain = margin + 1 + Presence_modifier_winner − Focus_defence_loser`. Minimum 1.

- Presence modifier: `max(0, floor((Presence − 3) / 2))` → Pres 1–3: +0; Pres 4–5: +1; Pres 6–7: +2
- Focus defence: `floor(Focus / 2)` → passive, no roll

**Finding — ceiling on Focus defence:** High Focus (6+) produces defence=3. With minimum strain=1, Focus defence cannot absorb more than margin+Presence_modifier. Beyond the breakeven point, adding Focus produces no additional strain reduction. Maximum effective Focus defence ≈ margin+1+Pres_mod−1 = margin+Pres_mod. Against weak opponents (Presence=1–3, margin=1): Focus=4 already at max effectiveness. **Focus investment above 4 is mechanically inert for strain reduction** unless facing high-Presence, large-margin opponents.

---

## MODE B — INTERACTION CHAINS

### B-1: Appraise → Choose → Argue Chain (Information Value)

**Chain:** Attunement roll (Appraise) → genre/orientation selection (Choose) → pool advantage (Argue)

| Appraise degree | Information | Strategic value |
|----------------|-------------|-----------------|
| Failure | Misleading signal — one weak genre appears strong | Negative: can be deceived into off-primary genre |
| Partial (1 net) | Primary genre only | Positive: confirms boosted genre |
| Success (2 net) | Genre + orientation preference | Strong: allows CLASH setup |
| Overwhelming (3+ net) | Genre + orientation + specific detail | Dominant: complete information |

**Chain value calculation:**
- Acting on Overwhelming vs Failure Appraise: ≈ difference between picking boosted genre (gw=1.5) vs off-primary (gw=0.5). Per exchange CT swing ≈ 2–4 steps on typical margins.
- Attunement=5 Appraise pool: E[net]=1.5 → typically Success. Strong debaters get complete information reliably.
- Attunement=2 Appraise pool: E[net]=0.6 → typically Partial or Failure. Weaker information.

**Dominant strategy confirmed:** High Attunement → reliable genre read → always play boosted genre → CLASH advantage. Characters should invest in Attunement as a force multiplier on their Argue pool. A character with Cognition=5, Attunement=5 is more powerful than Cognition=6, Attunement=2 in most debates.

### B-2: Doubt Marker → Next Exchange Chain

**DM interaction:** Reduces opponent's next winning exchange's `effective_margin` by 2 before resistance.

| Original eff_margin | Resistance | CT Δ without DM | CT Δ with DM | DM effect |
|--------------------|-----------|----------------|-------------|-----------|
| 2 | 1 | 1 | 0 | **Nullifies** |
| 3 | 1 | 2 | 0 | **Nullifies** |
| 3 | 2 | 1 | 0 | **Nullifies** |
| 4 | 1 | 3 | 1 | Reduces by 2 |
| 4 | 2 | 2 | 0 | **Nullifies** |
| 5 | 1 | 4 | 2 | Reduces by 2 |
| 5 | 2 | 3 | 1 | Reduces by 2 |
| 6 | 1 | 5 | 3 | Reduces by 2 |
| 6 | 2 | 4 | 2 | Reduces by 2 |

**Finding:** Against resist=2 audiences (high-Stability factions), a DM nullifies all typical exchange wins (eff_margin 2–4). Only overwhelming wins (eff_margin ≥ 5) survive a DM against resist=2. This makes Obscuring a near-complete defensive block against high-Stability audiences.

**Finding — Obscuring dominant in high-resistance audiences:** Against resist=2, the optimal strategy is: use Obscuring to place DM while opponent cannot move CT on small margins anyway. The DM then nullifies any moderate win the opponent achieves. A high-Attunement, Obscuring-specialist character is disproportionately powerful against high-Stability audiences. **This may be over-tuned.** [P2]

### B-3: Spent + Rattled Stacking Chain

**Conditions:** Both triggered when Concentration=0 AND strain ≥ Composure threshold.

| Base pool | After Rattled (−2D) | After Spent (−2D) | After both (−4D) | Min 1D applies |
|-----------|--------------------|--------------------|-----------------|----------------|
| 4D | 2D | 2D | 1D (min) | Yes |
| 7D | 5D | 5D | 3D | No |
| 10D | 8D | 8D | 6D | No |
| 13D | 11D | 11D | 9D | No |

**Finding — minimum pool characters:** At pool=4D (Cog=2, Hist=0), Rattled+Spent forces 1D pool. E[net]=0.3. P(winning any exchange) ≈ 25%. This character is effectively eliminated from the debate mechanically while still technically participating. **P1 severity candidate** — character has no meaningful agency at 1D.

**Finding — Composure formula dependency:** Because Composure formula is unresolved (ED-127, P1 above), we cannot know when Rattled triggers. If Composure ends up low (formula produces 5–6), Rattled triggers early and the combined state fires frequently. If Composure is high (12+), Rattled may never trigger in a standard 3-exchange debate. **All Rattled-related simulation findings are contingent on ED-127 resolution.**

---

## MODE C — FULL SCENARIO SIMULATION

### C-1: Church Tribunal (Asymmetric Proceeding)

**Setup:**
- Inquisitor: Cog=5, Hist=3, Att=5, Focus=4, Presence=5 → Argue=13D, Concentration=9
- Accused: Cog=4, Hist=2, Att=3, Focus=3, Presence=3 → Argue=10D, Concentration=6
- Question: Did Accused perform prohibited Thread operations? → Primary genre: Past
- Church audience: Divine Command → Past gw=1.5
- Resistance: Church Stability≈6 → base resist=2. Asymmetric halving for accused: resist=1 when accused moves CT. Inquisitor moves CT at resist=2.
- Starting CT: 6 (biased per PP-109). Exchange count: 3.
- Convicted threshold: ≥7. Acquitted threshold: ≤3. Compromise: 4–6.

**Exchange 1:**
- Appraise: Inquisitor (5D) E[net]=1.5 → Success. Accused (3D) E[net]=0.9 → Partial.
- Both choose Past/Revealing → CLASH
- Memory bonus both: Inquisitor 15D, Accused 12D
- E[margin Inquisitor] = 15×0.3 − 12×0.3 = 0.9
- Threshold for CT move (Inquisitor): margin=2 → eff=floor(2×1.5)=3, 3>2 → CT Δ=1. CT: 6→7. **WIN.**
- P(margin≥2): ~35% using normal approx for 15D vs 12D differential
- Most likely: margin=1 → eff=floor(1.5)=1, 1≤2 → CT Δ=0. CT stays at 6.
- **Most probable Exchange 1 outcome: CT stays at 6 (no movement). Inquisitor wins the exchange but cannot move the CT.**

Concentration: Inquisitor −1 (win) → C=8. Accused −2 (loss) → C=4.

**Exchange 2:**
- Accused now at C=4. Still capable. No Spent risk this exchange.
- Accused attempts Obscuring orientation (create doubt about evidence chain)
- CLASH: Inquisitor Revealing vs Accused Obscuring
- If Inquisitor wins: normal CT move calculation. If Accused wins: DM placed on Inquisitor.
- Memory bonus potentially again (different charge): Inquisitor 15D vs Accused 12D
- P(Accused wins): ~25% (pool disadvantage + Memory bonus disadvantage)
- On Inquisitor win (75%): eff_margin formula same. Same deadband problem vs resist=2.
- **Verdict: 75% chance Inquisitor wins, ~35% of those produce CT movement. ~26% chance CT moves to 7 = WIN.**

Concentration: Inquisitor C=7 (win). Accused C=2 (loss) → approaching Spent.

**Exchange 3:**
- Accused: C=2. One more loss = C=0 = Spent next exchange. But this IS the last exchange.
- Accused: Cognition debate waning. Last chance.
- Most likely CT still at 6 (two exchanges, minimal movement due to resist=2 deadband).
- Exchange 3: same dynamics. ~26% chance Inquisitor clinches.

**Final state probability (3 exchanges, neutral start CT=6):**
- CT≥7 (Conviction): ~55% accumulated across exchanges (rough: 1−(1−0.26)³)
- CT=6 (Compromise): ~35%
- CT≤3 (Acquittal): <10% (accused pool too small, resist for Inquisitor moves only 1)

**Scenario finding SC-01:** The resist=2 deadband creates a counterintuitive outcome where **the Inquisitor repeatedly wins exchanges but the CT fails to move** (margin=1 is the most common win margin for comparable pools). The most likely tribunal outcome is COMPROMISE — theologically unsatisfying for a proceedings meant to be decisive. PP-109's recommendation to start CT=5 makes matters marginally worse (now need CT to move 2 steps rather than 1). **Recommendation: For Church Tribunal, consider starting CT at 7 (pre-biased) OR reducing Church Stability for tribunal resistance calculation.**

**Scenario finding SC-02:** Asymmetric halved resistance helps the Accused move CT efficiently — but the Accused is so pool-disadvantaged that they rarely win exchanges. The halved resistance is a mechanical benefit that almost never fires in practice for this archetype matchup.

---

## MODE D — EDGE CASE FINDINGS

### P1 FINDINGS (Game-Breaking)

#### P1-SC-01: Argue Pool / Initiative Stat — Design Doc vs Params
**Setup:** Part 6 §6.4 specifies Presence×2 for pool and Presence for initiative. PP-232 (params) changed both to Cognition (pool) and Attunement (initiative). PP-232 not backported to design doc.
**Mechanism:** Running from the canonical design doc produces a Presence-based debate system. Running from params produces a Cognition/Attunement system. These are fundamentally different archetypes.
**Severity:** P1 — system cannot be run consistently.
**Proposed fix:** Backport PP-232 changes to Part 6: §6.3 (initiative), §6.4 Step 3 (pool), §6.10 (pool formula). Also resolve GAP-NEW-03 (Presence modifier status post-PP-232).

#### P1-SC-02: Interaction Taxonomy Incompatibility
**Setup:** Part 6 operative uses CLASH / COMPETITION / DIVERGENCE (3 types). Params uses CLASH / AMPLIFY / CROSS / DIVERGE-state (4 types). COMPETITION→AMPLIFY and DIVERGENCE→CROSS are renames only if their rules are identical; DIVERGE-state is a new mechanic not in Part 6.
**Mechanism:** AMPLIFY combined pool mechanic (PP-242/250) does not exist in Part 6 COMPETITION. CROSS simultaneous resolution (PP-245) differs from DIVERGENCE independent evaluation. DIVERGE-state (ED-133/PP-288) is a deadlock state with no Part 6 equivalent.
**Severity:** P1 — params mechanics exceed and contradict the design doc.
**Proposed fix:** Part 6 §6.4 Step 4 needs full rewrite to incorporate AMPLIFY pool cap (PP-242/250), CROSS simultaneous resolution (PP-245), and DIVERGE-state (PP-288/313 if confirmed). Or params must revert to Part 6 taxonomy and be clearly marked as extending it.

#### P1-SC-03: Composure Formula Unresolved
**Setup:** §6.2 gives `Composure = Poise + Bonds + 3`. Params deprecates Poise with no replacement formula. ED-127 unresolved.
**Mechanism:** Rattled threshold unknown. All Rattled-dependent simulation findings contingent.
**Severity:** P1 — Rattled trigger condition undefined.
**Proposed fix:** Resolve ED-127. Adopt a formula (e.g., replace Poise with Cognition: `Composure = Cognition + Bonds + 3`) or retain Poise as a debate-only derived stat.

#### P1-SC-04: Obscuring Orientation Weight Conflict
**Setup:** Design doc §6.4 OBSCURING WIN rule states CT does not move — Doubt Marker placed instead. Params §Orientation Weights gives Obscuring ow=0.75, implying CT movement at reduced rate.
**Mechanism:** Two incompatible rules for the same trigger.
**Severity:** P1 — cannot run Obscuring exchanges consistently.
**Proposed fix:** Remove ow=0.75 from params Orientation Weights section (or strike that section entirely). Design doc rule is canonical: Obscuring win = no CT movement + DM. (The ow=0.75 entry appears to be a stale prior design iteration.)

#### P1-SC-05: 'Proposer Role' in §6.7 — Dangling Term
**Setup:** §6.7 Standard Proceedings says "Proposer role alternates each exchange (1→A, 2→B, 3→A...)." But in Part 6 operative, Proposer vs Objector has no mechanical definition (the quaestio structure was deprecated).
**Mechanism:** The alternating "Proposer role" has no mechanical effect in the current system. It appears to be a design residue from the quaestio structure (Parts 1–4).
**Severity:** P1 candidate — creates false impression of asymmetric roles that don't exist mechanically.
**Proposed fix:** Strike the proposer-role alternation language from §6.7 or define what mechanical effect it has in the Part 6 system. If there is no effect, state that plainly.

---

### P2 FINDINGS (Bad Play Experience)

#### P2-SC-01: Off-Primary Genre Dead Zone
**Setup:** gw=0.5 for off-primary genres. Against resist=1: margin≥4 required for any CT movement. Against resist=2: margin≥6 required.
**Mechanism:** For equal pools (8D vs 8D), E[margin]=0. P(margin≥4) ≈ 10%. Off-primary genre argues are 90%+ wasted.
**Severity:** P2 — creates dominant strategy (always match audience's boosted genre), reduces tactical variety.
**Frequency:** Very common — whenever a character lacks History in the boosted genre.
**Proposed fix:** No fix required if the design intent is to punish genre mismatch. But consider reducing penalty to gw=0.75 for off-primary (vs 0.5) to allow meaningful off-genre plays.

#### P2-SC-02: resist=2 Deadband in High-Stability Audiences
**Setup:** Resist=2 means margin=1 wins produce eff_margin=1 (for gw=1.0) → no CT movement. Margin=2 required for primary genre, margin=3 for boosted genre to move CT at all vs resist=2.
**Mechanism:** Closely matched characters (E[margin]≈1) will frequently win exchanges that produce zero CT movement. The CT stagnates in the compromise zone regardless of exchange count.
**Severity:** P2 — 3-exchange Formal Debate between similar-pool characters in a high-Stability audience almost always ends in compromise, regardless of performance.
**Frequency:** Common with Stability 5–7 audiences (Parliament, Church).
**Proposed fix:** Consider setting resist = max(1, ceil(avg_stability/4)−1) for standard proceedings, reserving resist=2 for Grand Debates only.

#### P2-SC-03: Obscuring Dominant in High-Resistance Context
**Setup:** Against resist=2, DM nullifies all wins with eff_margin ≤ 4. Typical primary-genre wins produce eff_margin 1–4.
**Mechanism:** Obscuring + DM makes the Obscuring player's exchange loss cost-free in terms of CT movement while blocking the opponent's typical winning exchange.
**Severity:** P2 — Obscuring-specialist character is near-dominant against high-Stability audiences.
**Proposed fix:** Add a cost to Obscuring losses (e.g., Obscuring loser takes +1 strain on top of normal strain) to balance the DM benefit.

#### P2-SC-04: Church Tribunal Most Likely Ends in Compromise
**Setup:** Described in C-1 scenario simulation above.
**Mechanism:** Resist=2, E[margin]≈1 for Inquisitor vs comparable Accused, CT starting at 6 = one-step from win but deadbanded.
**Severity:** P2 — Church Tribunal is narratively designed to be oppressive and decisive; mechanically it often produces compromise.
**Proposed fix:** For Church Tribunal specifically: set base resistance = 1 (not 2) per faction Stability, bypassing the PP-278 formula. Or set starting CT at 7 for summary proceedings (where the outcome is meant to be near-certain).

---

### P3 FINDINGS (Minor)

#### P3-SC-01: High-Focus Defence Cap
At Focus≥6, Focus defence (=3) absorbs all strain from low-Presence opponents with margin=1. Strain minimum=1 applies as the floor. High-Focus investment above 4 is mechanically inert against typical opponents. Not a break — just a wasted stat point for dedicated debate characters.

#### P3-SC-02: Regroup as Dominant Escape vs Superior Opponent
When facing a pool advantage of 6D+, expected CT loss from arguing ≈ 1–2 per exchange. Regroup costs exactly CT+1. In many cases, arguing and losing produces equivalent or worse CT loss than Regroup, while Regroup restores Concentration. Against overwhelming opponents, Regroup → Regroup → Regroup stalling is the correct play until time runs out. The Concentration restore creates an infinite-duration stall option in debates with no exchange limit. **Debates must always have an explicit exchange limit.** (§6.0 requires GM to declare this at setup — correctly designed, but must be enforced.)

---

## GAPS FOUND

| ID | Description | Severity |
|----|-------------|----------|
| GAP-NEW-01 | Memory bonus (+2D) frequency limit per debate not defined | P2 |
| GAP-NEW-02 | TIE rule priority vs Obscuring DIVERGENCE: which fires when both score equal successes and larger-delta side used Obscuring? | P2 |
| GAP-NEW-03 | Presence modifier status after PP-232 Cognition pool change: does it still add to the pool as a separate bonus? | P1 |
| GAP-NEW-04 | Corroborator eligibility dispute procedure undefined — who adjudicates 'witnessed the relevant event'? | P3 |
| GAP-NEW-05 | 'Full Knot bonus' for corroboration — source mechanic undefined in debate context | P2 |

---

## SIM-DEBT

| ID | Description |
|----|-------------|
| SIM-DEBT-SC-01 | Royal Audience proceeding — not yet stress-tested (flagged as open in §6.8) |
| SIM-DEBT-SC-02 | Rattled → Unmask decision point — not triggered in simulation (contingent on ED-127 resolution) |
| SIM-DEBT-SC-03 | Mixed Guilds audience calibration — not yet tested |
| SIM-DEBT-SC-04 | Corroboration in CLASH calibration (SIM-DEBT-02 in params) — pending |
| SIM-DEBT-SC-05 | Full Grand Debate (5 exchanges) scenario with matched pools |

---

## SUMMARY OF P1 FINDINGS FOR PATCH REGISTER

| Finding ID | Description | Blocking |
|-----------|-------------|---------|
| P1-SC-01 | PP-232 not backported: Argue=Cognition×2, Initiative=Attunement not in Part 6 | All simulation |
| P1-SC-02 | Interaction taxonomy: AMPLIFY/CROSS/DIVERGE-state in params vs COMPETITION/DIVERGENCE in Part 6 | Exchange resolution |
| P1-SC-03 | Composure formula unresolved (ED-127 open) | Rattled threshold |
| P1-SC-04 | Obscuring ow=0.75 in params contradicts design doc Obscuring = no CT move + DM | Orientation resolution |
| P1-SC-05 | 'Proposer role' in §6.7 has no operative mechanical effect (quaestio deprecated) | §6.7 rules |

**None of the P1 findings require editorial decisions — all are mechanical consistency repairs or design doc backports.**
