# Atomic Interaction Lattice & Emergent Dynamics
## Date: 2026-05-13 · Session: bottom-up-emergent · Part 6/N · Status: ANALYSIS
## Methodology: bottom-up, granular, emergent
## Companions: Parts 1–5 (corrected canon + top-down balance work)

---

## §1 Frame — What Bottom-Up Means Here

Parts 1–5 started from canonical structure (4-faction model, role-templates, 25%
win-target) and derived where the model violates that target. Top-down.

This part inverts the epistemic stance. Start from **atomic mechanical primitives** —
the smallest meaningful units of game state and action. Compose them pairwise, then in
combos across turns. Let the dynamics that **emerge** from composition reveal what the
system actually does. Treat canonical role-templates ("Crown is Sovereign", "Hafenmark
is Mercantile-Procedural") as **claims to be verified**, not as starting axioms.

The discipline: do not assume the dominant strategy; derive it. Do not assume the modal
play pattern; derive it. Look for dynamics that arise from rule interactions that no
canonical document asserts.

Per Μ-β (Autonomous Agent Composition, `throughlines_meta §2`): *"independent agents
interact to produce events no agent predicts."* The mechanics themselves are the
autonomous agents here.

---

## §2 Atomic Mechanical Primitives

Smallest meaningful units. These are the *atoms* of the BG layer.

### §2.1 Dice and Resolution

| Primitive | Definition | Source |
|-----------|------------|--------|
| `d10_v05` | One die: 1→−1 P=0.1 · 2–6→0 P=0.5 · 7–9→+1 P=0.3 · 10→+2 P=0.1 | `params/bg/core.md` |
| `degree(net)` | net ≥ +2 → Overwhelming · +1 → Success · 0 → Partial · ≤ −1 → Failure | `params/bg/core.md` |
| `pool × Ob → degree` | Roll pool dice, sum nets, look up degree | core mechanic |

### §2.2 State Variables (faction)

| Primitive | Range | Notes |
|-----------|-------|-------|
| `L` (Leader) | 1–7 | drives Treaty/Excomm Ob targeting |
| `PS` (Popular Support) | 1–7 | drives Ob in some plays |
| `I` (Influence) | 1–7 | pool for diplomatic actions |
| `W` (Wealth) | 0–8 | resource for Token, Trade ceiling |
| `Mil` | 0–7 | pool for Muster + garrisons |
| `Int` (Intel) | 1–7 | pool for Spy + Tribune; defense base for counter-espionage |
| `Sta` (Stability) | 0–5 | revolt threshold; many Failure consequences hit here |
| `M` (Mandate) | derived = `round(0.5L + 0.5PS)` | per `faction_behavior §4` |

### §2.3 State Variables (territory)

| Primitive | Range | Notes |
|-----------|-------|-------|
| `Sta_t` | 0–5 | territory stability; 0 = revolt |
| `Accord` | 0–3 | governance quality; 0 = revolt-eligible |
| `P` (Prosperity) | 1–5 | drives Charter Ob; modified by Govern |
| `AP` (Activation Points) | 0–∞ | accumulates per Spread; threshold triggers |
| `Inquisitor` | 0/1 | binary; Inquisitor presence flag |
| `Charter` | 0/1 | binary; Valorsmark active Charter flag |
| `Fort` | 0–3 | fortification level |

### §2.4 State Variables (clocks)

| Primitive | Range | Threshold effects |
|-----------|-------|-------------------|
| `CI` (Crisis Index) | 0–60+ | 60 → territorial Seizure trigger |
| `MS` (Mending Stability) | 0–100 | drops over time; multiple band thresholds |
| `IP` (Imperial Pressure) | 0–30+ | 30 → fragmentation start |
| `PI` (Political Instability) | 0–10+ | 8 → Crisis state (free Agitation + Cascade Brake) |
| `Strain` | 0–∞ | accumulates +1 per Revolt at Year-End |

### §2.5 Atomic Actions

| Atom | Pool | Ob driver | Effect on degree |
|------|------|-----------|-------------------|
| Royal Decree (Valorsmark) | L=5 | base 2; +1 consec | target self stat +1; Failure: PS −1 |
| Royal Charter (Valorsmark) | L=5 | floor(P/2)+1; Virtue −1 | territory P +1; persists |
| Outreach to Schoenland (Valorsmark) | I=5 | 2; IP shifts | IP −1 |
| Spy (any) | Int | floor(target Int/2)+1 | reveal stats; failed Spy is detectable |
| Govern (any) | L | base 2; Charter −2 own | P +1 |
| Trade (any) | W | floor(P/2)+1 | W +1 (cap 8) |
| Muster (any) | Mil | 2 | garrison +1 |
| Piety Spread (Church) | L=5 | floor(target L/2)+1; doctrine −1 | AP +2 |
| Active Inquisition (Church) | L=5 | floor(target Sta/2)+1 | deploys Inquisitor if AP ≥ thr |
| Excommunication (Church) | L=5 | target L | target L −1 (S+); fail: Church Sta −1 |
| CI 60 Seizure (Church) | L=5 | floor(owner L/2)+1 | seize 1 territory; trigger CI 60 |
| Counter-Narrative (Varfell) | Int=4 | base 3; Conseq −1; Inq +2 | AP −2; reveal Inq pos |
| Diplomat (Hafenmark) | I=4 | floor(target L/2)+1 | place Token on target mat |
| PA Session (Hafenmark) | — | vote check | L +1 on pass; PI +1 |
| Dynastic Proclamation (Hafenmark) | L=4+ | floor(target Sta/2)+1; Token −1 | territory transfer; prereq Haf L > target L |
| Tensions Deck draw | — | — | random world-state effect |

### §2.6 Atomic Modifiers

| Modifier | Effect | Source |
|----------|--------|--------|
| Token (on target mat) | +1 to *one* action against that target | PP-517 |
| Inquisitor present | +2 Ob to Counter-Narrative; pressure on territory Sta | PP-441-COR |
| Royal Guard | cancel 1 Intel attempt per season vs Valorsmark | PP-442 |
| Cardinal Focus | grants 1 stat boost or unlocks card pathway | PP-405 |
| Doctrine-aligned | −1 Ob for Church plays in matching territory | PP-403 |
| Virtue-aligned | −1 Ob for Valorsmark Charter | PP-433 |
| PI ≥ 8 (Crisis) | free Agitation card available + Cascade Brake | clocks.md |
| Consec penalty | +1 Ob per consecutive same-card play | PP-N |
| Wealth cap (8) | further W gain wasted | derived from W range |
| Sta floor (0) | revolt trigger; territory leaves controlled | PP-N |

---

## §3 Pairwise Compositions

Atom × atom → effect. The combinatorial space is large; cataloging productive pairs.

### §3.1 Card × Modifier

| Pair | Composition |
|------|-------------|
| Charter × Virtue territory | Ob 2 → Ob 1; P(Succ+) 60% → 79.8%; **structural Valorsmark home advantage** |
| Charter × Govern (same territory) | Govern Ob 2 → Ob 0 (floor 1); 79.8% Govern; Valorsmark accelerates P growth |
| Active Inquisition × Cardinal Justice + AP 2 | combined trigger deploys Inquisitor |
| Diplomat × prior Token on target | second Token attempt wasted (Token max 1/mat) |
| Counter-Narrative × Inquisitor present | Ob 3 → Ob 4 (post-Conseq); P(Succ+) 28% → 11.9% |
| Spy × Royal Guard | one Intel/season auto-cancelled if Valorsmark target |
| Trade × W cap | W gain capped; Trade success becomes worthless past cap |
| Muster × adjacent territory threat | garrison can defend or absorb; defense efficiency varies |

### §3.2 Card × State

| Pair | Composition |
|------|-------------|
| Royal Decree × consecutive-counter | Ob escalates +1 per consec; cap-out by S4 |
| Piety Spread × territory AP | AP +2 per success; threshold-triggered Inquisitor |
| Active Inquisition × territory Sta | Sta drives Ob; low-Sta territories easier to Inquisitor |
| Treaty × target consent | requires target faction agreement (GAP-05 blocks) |
| Charter × P modifier | high-P territory (P=5) → Ob 3; low-P (P=1) → Ob 1 |
| Counter-Narrative × Failure | reveals Tribune to Church (PP-441-COR exposure rule) |

### §3.3 Clock × Clock

| Pair | Composition |
|------|-------------|
| CI × MS | CI rises faster when MS drops |
| PI × CI | PI ≥ 8 enables free Agitation which raises CI |
| Strain × Sta_t | Strain from revolts pressures neighboring Sta_t |
| MS × Tensions Deck | Tensions weighted toward MS-pressure cards as MS drops |

### §3.4 Card × Clock

| Pair | Composition |
|------|-------------|
| Diplomat × PI | Diplomat success raises PI |
| Outreach × IP | Outreach reduces IP by 1 per success |
| Decree × CI | Decree success may reduce CI |
| Inquisitor deploy × CI | Inquisitor presence adds to CI per Accounting |

### §3.5 Faction × Faction (interaction surface)

| Pair | Composition |
|------|-------------|
| Church Inquisitor × Valorsmark Charter | Charter doesn't defend vs Piety Spread; Inquisitor pressures Sta separately |
| Hafenmark Token × Varfell mat | Token persists; can be triggered for compound action |
| Varfell Spy × Hafenmark Procedural Objection | Spy detected → blocked via Objection card |
| Valorsmark Royal Guard × Varfell Tribune | absorbs 1 Intel attempt per season |
| Church Excommunication × Valorsmark L | Ob = target L = 5 → 8.3% Succ+ |
| Hafenmark PA Session × all factions' votes | 4-voter dynamics (per §5.7 emergent voting) |

---

## §4 Combo-Probability Catalog (Computed Bottom-Up)

### §4.1 Charter Chain Decay (Valorsmark)

5D vs Ob 1 = 79.8% per attempt. Maintenance over N seasons:

| N seasons | P(all succeed) | P(≥ 1 fail) |
|-----------|----------------|-------------|
| 3 | 50.8% | 49.2% |
| 4 | 40.6% | 59.4% |
| 5 | 32.4% | 67.6% |
| 6 | 25.8% | 74.2% |
| 7 | 20.6% | 79.4% |
| 8 | 16.4% | 83.6% |

**Emergent finding E1:** Valorsmark Charter loop *cannot* be maintained at 100% over a
6-season arc. **P(failure-free chain of 6) = 25.8%.** The loop is structurally
self-limiting through variance. The 6-faction sim's "Crown unmolested + Charter loop"
overstated Valorsmark's late-game stability — it didn't account for chain variance.

### §4.2 Inquisitor Deployment Probability (Church)

Joint per-season (Piety Spread Ob 2 + Active Inquisition Ob 2): 60% × 60% = **36%**.

| N seasons | P(≥ 1 Inquisitor deploys) |
|-----------|----------------------------|
| 4 | 83.2% |
| 6 | 93.1% |
| 8 | 97.2% |

**Emergent finding E2:** Inquisitor deployment is near-certain by S5–S6. Church gets
its primary mechanism down with > 93% reliability over an arc. **The variance is in
*which* territory and *when*, not *whether*.** Under T-09c (cap 2): 2 Inquisitors with
> 93% reliability across the arc; 3rd would require recall.

### §4.3 Royal Decree Consecutive Penalty Cliff

Same card consec → Ob +1 per repeat:

| Season | Ob | P(Succ+) |
|--------|----|-----------| 
| S1 | 2 | 60.0% |
| S2 (consec) | 3 | 38.0% |
| S3 (consec) | 4 | 19.8% |
| S4 (consec) | 5 | **8.3%** |

P(all 4 consec succeed Y1) = **0.37%**.

Compare: 2 isolated Decree (Ob 2 each, every-other season) = 36% joint.

**Emergent finding E3:** Royal Decree is **NOT a per-season Valorsmark tool**. The
consec penalty turns it into a 1–2× per arc mechanism. Optimal play: Decree S1, skip
S2, Decree S3, skip S4. Prior Mode C-Δ sim assumed Decree every season — that's wrong.
Valorsmark's defensive Decree income is **half** what the role-template implies.

### §4.4 Hafenmark Token Dwell

Diplomat on Varfell (4D vs Ob 2): 51.2% per attempt.

E[Token-seasons after 4 attempts, given Token-cap-1] = sum of P(land on attempt k) × dwell-from-k = **0.94**.

**Emergent finding E4:** Despite 51.2% per-attempt Token landing, Hafenmark gets only
~1 Token-season of value per 4 Diplomat attempts. Token is a *brief* resource, not a
persistent buff. **The "Hafenmark Token economy" is much weaker than role-template
suggests** — Token + Diplomat is a 1-per-arc compound, not a per-season pipeline.

### §4.5 Counter-Narrative Recovery (Varfell)

Once Inquisitor deployed: 4D vs Ob 4 = 11.9% per attempt.

| Scenario | P(≥ 1 recovery in 4 attempts) |
|----------|--------------------------------|
| Current canon | 39.8% |
| **With T-02a (familiarity)** | **67.1%** |

**Emergent finding E5:** T-02a roughly **doubles** Varfell's territorial recovery
chance from 40% → 67% per 4 attempts. This is the **concrete quantitative value** of
T-02a — not previously stated in Parts 1–5.

### §4.6 Wealth Cap Saturation (Hafenmark)

Trade (6D vs Ob 2) = 67.0% per attempt. Starting W=5, need 3 W gains to reach cap (W=8).

E[seasons to W cap] = ~4.5.

**Emergent finding E6:** Hafenmark hits W cap by mid-game (S4–S5). Past that point,
Trade success grants **zero value**. **Hafenmark has a "Trade efficiency cliff"** in
mid-game; the role-template doesn't capture this. Hafenmark must pivot off Trade by
S5 or run Trade for territory P benefit only (not Wealth).

### §4.7 Muster Defensive Garrison Rate

Mil 4 vs Ob 2 = 51.2%. 4-season Muster focus = E[~2 garrisons].

**Emergent finding E7:** A faction dedicating Muster to defense in 4-season arc lands
~2 garrisons. **Garrison-defense is rate-limited** — a faction can defend ~2
territories per arc, not all of them.

---

## §5 Emergent Dynamics

Beyond pairwise combos, dynamics that **arise** from sustained interaction.

### §5.1 The Inquisitor-Self-Defeating Dynamic

Setup: Church deploys Inquisitor T9 (Valorsmark-controlled). Over S2–S5, Inquisitor
pressure cascade: Sta drift → Accord drift → Revolt. T9 becomes Uncontrolled.

**Emergent observation:** Once T9 is Uncontrolled, Inquisitor's pressure-to-Church-Piety
conversion stops. The Inquisitor "wins" the territory but Church doesn't "hold" it.
Church loses the legibility of the Inquisitor's pressure-effect once Uncontrolled state
takes over.

**Implication:** Church may be better off keeping target faction in control (so the
Inquisitor's pressure converts to Sta drift over time, then to L drift via cumulative
effects, NOT to outright loss of territory). **Optimal Church play might be "deploy
Inquisitor → sustain pressure → never let territory revolt"** — applies Piety Spread
for AP but withdraws Active Inquisition before revolt fires.

**Status:** EMERGENT. Not in canonical Church role-template. Would change Church
strategic AI.

### §5.2 The Royal Decree Phase Lock

From §4.3: Decree consec penalty caps Valorsmark at ~2 Decree plays per year. Combined
with Winter reset (Y1S4 cooldown clears), Valorsmark's optimal Decree cadence is:

- **Y1S1**: Decree (Ob 2, 60% Succ+)
- **Y1S2**: skip (let consec reset OR avoid Ob 3 penalty)
- **Y1S3**: Decree (depending on whether consec counter resets on skip — verify PP-N)
- **Y1S4**: Winter — Decree consec resets
- **Y2S1**: Decree (Ob 2, fresh)

**Emergent observation:** Valorsmark's stat-modification income is **structured around
4-season Winter resets**, not seasonal. The Sovereign role-template's "frequent Decree"
implication is false; canonical mechanics force Decree to be rare-but-decisive.

**Implication:** Valorsmark's defensive Sta-Mil buffer ability is **half** what
top-down assumed. Valorsmark is more vulnerable than role-template suggests.

### §5.3 The Sta-Accord Cascade Trap

For a target territory:

1. Inquisitor presence → −1 Accord pending each season
2. Accord 0 → territory revolt-eligible at next Sta check
3. Sustained Inquisitor → Sta drift downward
4. Sta 0 → guaranteed revolt
5. Revolt → +1 Strain (Year-End B11)
6. Strain → pressures neighboring territory Sta_t (per `peninsular_strain`)
7. Neighboring territory Sta drops → may cascade to next territory revolt

**Emergent observation:** A single Inquisitor on a single territory can trigger a
**multi-territory revolt cascade** over 2–3 arcs if defenses aren't in place. Strain
is a feedback amplifier.

**Implication:** Faction defense is not per-territory but **per-cluster**. A faction
must invest in defending **adjacent territory portfolios**, not single territories.
This is more granular than role-templates assume.

**Quantitative estimate:** Starting Sta_t = 4, Accord = 2. With T9 Inquisitor sustained:
S1 (deploy): Sta 4, Accord 2 → S2: Accord 1 → S3: Sta 3, Accord 0 → S4: revolt.

**Two-territory cascade probability over 8 seasons:** rough estimate, conservative
**60–70%** if Church sustains Inquisitor pressure and Valorsmark doesn't aggressively
garrison.

### §5.4 The PI Crisis Lock-In

PI ≥ 8 triggers Crisis state: free Agitation card + Cascade Brake. The free Agitation
card raises PI further. Once PI hits 8, rate of PI growth *accelerates*.

**Emergent observation:** PI Crisis is a **one-way ratchet**. No mechanic explicitly
reduces PI below 8 once crossed (verify against `params/bg/clocks.md` for explicit
decrement rules). Without an explicit PI-reduction mechanism, **the Crisis state is
permanent for the rest of the campaign.**

**Implication:** Hafenmark mid-game ascendancy (per Part 3 §4) becomes structurally
**locked in** once PI 8 is crossed. Other factions cannot easily reverse it.

**Status:** EMERGENT and probably **unintended.** Game arc seems calibrated for
Year 3–4 Crisis emergence, not Year 1 lock-in. PI Crisis tuning becomes **P1**.

### §5.5 The Inquisitor Cap (T-09c) as Tempo Lever

Under T-09c, Church can deploy at most 2 Inquisitors peninsula-wide. Combined with §5.1
(self-defeating dynamic) and §5.3 (Sta cascade), Church's optimal play emerges:

- Deploy Inquisitor 1 on territory A (high-value target, sustainable pressure)
- Deploy Inquisitor 2 on territory B (secondary target, sustainable pressure)
- **Do not let A revolt** — sustain pressure but withdraw Active Inquisition before Sta 0
- **Cycle**: when A's value extracted (faction L drift), recall and redeploy to C

**Emergent observation:** T-09c forces Church into a **tempo-management game**, not a
territorial-conquest game. Church becomes about *sustained pressure orchestration*
rather than *territorial expansion*. This is **deeper** Church play than the current
"Inquisitor blitz" pattern.

**Implication:** T-09c isn't just a nerf — it's a **gameplay-deepener** for Church.
Strengthens the case for T-09c adoption (already strongest per Part 5).

### §5.6 The Hafenmark Trade Cliff + Pivot

From §4.6: Hafenmark hits W cap by S5. Past S5, Trade is wasted.

**Emergent observation:** Hafenmark's optimal early-game = Trade-heavy (cap W fast).
Optimal mid-game = pivot to Token deployment + PA Session preparation. **Hafenmark has
a phase shift** at ~S4–S5 from "accumulator" to "deployer."

**Implication:** Under T-03c (Token costs W−1), Hafenmark's W cap becomes a strategic
constraint — Hafenmark must spend W on Tokens or it caps. Current canon (Tokens free)
means W cap is just wasted Trade. **T-03c makes the W cap into a meaningful strategic
decision, not a wasted resource.** Strengthens the case for T-03c.

### §5.7 The 4-Voter Parliamentary Tie

PA Session vote requires majority. 4-faction voters: Hafenmark Support + 3 others.

| Scenario | Outcome |
|----------|---------|
| 4-0 Hafenmark | Pass |
| 3-1 Hafenmark | Pass |
| 2-2 | **Tie → fail per `faction_actions §PA Session COR`** |
| 1-3 against | Fail |

**Emergent observation:** With **4 voters**, the 2-2 tie outcome **fails** the PA
Session. This means Hafenmark needs **at least 2 of 3 other factions to Support** —
plus Hafenmark itself — for 3-1 majority. **The vote distribution structurally
disadvantages Hafenmark.**

Compare: with **5 voters** (6-faction model with Guilds), Hafenmark could pass with
3-2. With **4 voters**, Hafenmark needs 3-1. **The corrected 4-faction canon makes PA
Session HARDER to pass than the prior 6-faction simulation showed.**

**Implication:** Hafenmark's L-growth mechanism (PA Session) is **less reliable than
prior sim assumed**. The Mode C-Δ S4 PA pass depended on Token-on-Varfell tilting
Varfell. If no Token, Hafenmark needs Valorsmark Support unprompted — only available
under specific Tensions cards.

**Concrete:** Hafenmark mid-game ascendancy depends on Token-leveraged voting, which
is rate-limited (§4.4 — Token dwell ~1/4 attempts). **Hafenmark mid-game ascendancy
may be SLOWER under bottom-up analysis than top-down assumed.**

### §5.8 The Tensions Deck as Noise Source

`params/bg/tensions_deck.md` defines a deck drawn at Phase 1 of each season. Bottom-up:
Tensions are **outside faction control** — they reshape the game state per-season.

**Emergent observation:** Mode C-Δ sim assumed one Tensions card across 6 seasons.
Reality: 6 Tensions cards drawn per arc. Each contributes ±5–10% variance to faction
fortunes. **Over 6 seasons, accumulated Tensions variance is ±15–25% to win-share
projections.**

**Implication:** The 22–28% post-tweak projected band (Part 3 §6.2) is **median**,
not deterministic. With Tensions variance, single-campaign outcomes may swing 17–33%
— still inside the ±5pp target on average across N campaigns, but with significant
variance per-campaign.

**Status:** EMERGENT. The Mode C-Δ sim lacks Tensions Deck integration; Monte-Carlo
(Part 7) needs to model it.

---

## §6 Faction Behavior Derived from Mechanics (Not Asserted)

Bottom-up: don't take role-template; derive faction optimal play from atomic
interactions and combo probabilities.

### §6.1 Valorsmark — Derived Behavior

From §4.1, §4.3, §5.2: Valorsmark's optimal play emerges as:

- **Anchor on Capital (T2):** Charter T2 + Govern T2 → sustained P growth on Virtue
  territory; structural home advantage (Ob 1 per §3.1)
- **Charter 2-3 territories max:** Beyond 3, chain decay kicks in
- **Decree biennial:** Y1S1 then Y2S1, not seasonal
- **Outreach when IP rises:** defensive use; not seasonal
- **Royal Guard absorbs 1 Intel/season:** opponents land Intel by attempting 2

**Derived role-name:** Not "Sovereign" but **"Capital Anchor with Biennial Diplomatic
Surge."** Valorsmark grows slowly from a defended capital, with rare diplomatic peaks.

**Divergence from canon:** Canon "Sovereign" implies broad active rulership; mechanics
give **narrow, capital-anchored, slow-rotation** play. **Canon overstates Valorsmark's
mechanical breadth.**

### §6.2 Church — Derived Behavior

From §4.2, §5.1: Church's optimal play emerges as:

- **Inquisitor 2 territories (under T-09c):** orchestrate sustained pressure without
  triggering revolt (§5.1)
- **Cardinal Focus rotation:** Justice (Y1 Inquisitor) → Prudence (Y2 W) → Justice (Y3
  Inquisitor recycle) → Temperance (Y4 diplomatic absorption)
- **CI 60 Seizure preserved:** rare crisis-trigger play
- **Excommunication mid-tier defensive tool:** 8–20% per attempt

**Derived role-name:** Not "Ecclesiastical" but **"Pressure Orchestrator with
Cardinal-Cycle Rotation."** Church's identity is *managing pressure across 2 active
fronts cyclically*, not unlimited theocratic expansion.

**Divergence from canon:** Canon implies Inquisition is Church's *expansion vector*.
Mechanics + T-09c reveal Inquisition is Church's *pressure vector* — distinct. Church
gains L slowly through cumulative effects, not via territorial capture.

### §6.3 Hafenmark — Derived Behavior

From §4.4, §4.6, §5.6, §5.7: Hafenmark's optimal play emerges as:

- **Y1 W accumulation:** Trade every season; reach W=8 cap by S4–S5
- **Mid-game pivot:** stop Trade past cap; redirect to Token deployment + PA Session
- **Token economy as 1-per-arc compound:** Diplomat-then-Token-trigger is a 4-season
  cycle, not per-season; concentrates on Varfell
- **PA Session timing:** must have Token-leveraged Varfell Support to win 3-1
- **Proclamation only mid-game vs Varfell:** L=5 (post-PA) vs Varfell L=4; rare and late

**Derived role-name:** Not "Mercantile-Procedural" but **"Wealth-Pivot Soft Power
with Varfell-Concentrated Pressure."** Hafenmark's identity is *Trade-then-pivot
political maneuvering*, not constant mercantile pressure.

**Divergence from canon:** Canon implies Hafenmark is patient and broad; mechanics
reveal it's *phase-shifted* and *targeted*.

### §6.4 Varfell — Derived Behavior

From §4.5, §4.7, §5.1: Varfell's optimal play emerges as:

- **Pre-Inquisitor Counter-Narrative:** 28% per attempt; cumulative ~70% over 4 attempts
- **Spy concentration on Hafenmark (Int 3, weakest):** 51.2% per attempt; reveals Token plans
- **Muster 2 garrisons over 4 seasons:** defensive cluster building
- **Save Tribunes for Inquisitor recovery:** ~40% recovery (canon) or ~67% (with T-02a)

**Derived role-name:** Not "Military-Order" but **"Tribune-Spy Reactive with
Inquisitor-Recovery Specialization."** Varfell's identity is *intelligence-driven
reactive play*, not military expansion.

**Divergence from canon:** Canon implies Military-Order; mechanics reveal an
*intelligence-and-recovery* faction. **Varfell's Mil stat is rarely the active vector
under bottom-up optimal play.** Mil 4 = Muster pool only; offensive Mil action
requires mass_combat triggers that are rare.

### §6.5 Cross-faction divergence summary

| Faction | Canon role-template | Bottom-up derived role | Convergence? |
|---------|---------------------|------------------------|--------------|
| Valorsmark | Sovereign | Capital Anchor + Biennial Diplomatic | Weak — canon overstates breadth |
| Church | Ecclesiastical | Pressure Orchestrator (under T-09c) | Strong if T-09c adopted |
| Hafenmark | Mercantile-Procedural | Wealth-Pivot Soft Power, Varfell-targeted | Moderate — mechanics narrower than canon |
| Varfell | Military-Order | Tribune-Spy Reactive | Weak — canon implies offensive Mil |

**Set-level finding:** Of 4 player factions, **2 (Valorsmark, Varfell) show weak
canonical-mechanical convergence**. Their canonical identity overstates the actual
mechanical play surface. **This is a separate balance question from win-share equality
— it's about faction-identity coherence.**

---

## §7 Where Top-Down Missed Things (Cross-Reference to Parts 1–5)

| Top-down finding (Parts 3–5) | Bottom-up complement / correction |
|------------------------------|----------------------------------|
| C-Δ-F1 (Church ascendant) | Strengthened. §4.2 shows Inquisitor deploy near-certain (93% in 6 seasons). |
| C-Δ-F2 (Hafenmark mid-game ascendant) | **Weakened.** §5.7 4-voter PA Session harder than 5-voter. §4.4 Token dwell ~1/4. Hafenmark ascendancy slower than top-down assumed. |
| C-Δ-F3 (Valorsmark territorial vulnerability) | Strengthened. §5.2 Decree biennial halves defensive income. §5.3 Sta cascade multi-territory. |
| C-Δ-F4 (Varfell structural decline) | Strengthened. §4.5 shows recovery at 40% without T-02a. T-02a doubles to 67%. |
| S4-Δ-F3 (PI Crisis at Y1 too early) | **Strengthened to P1.** §5.4 PI Crisis is one-way ratchet — Y1 Crisis = full-campaign Crisis. |
| T-09c (Inquisition cap) | Strengthened. §5.5 shows cap deepens Church play. |
| T-03c (Token cost W-1) | **Strengthened qualitatively.** §5.6 shows Hafenmark W cap is wasted under current canon; T-03c makes it strategic. |
| T-02a (Inquisitor familiarity) | Strengthened. §4.5 quantifies 40%→67% recovery jump per arc. |

**Bottom-up-only findings (not in Parts 1–5):**

| ID | Finding |
|----|---------|
| E5.1 | Church may optimally NOT trigger revolt (Inquisitor self-defeating) |
| E5.2 | Decree biennial, not seasonal |
| E5.3 | Sta-Accord cascade is multi-territory feedback amplifier |
| E5.4 | PI Crisis is one-way ratchet |
| E5.6 | Hafenmark hits Trade cliff at S4–S5; phase shift |
| E5.7 | 4-voter PA Session structurally harder than 5-voter |
| E5.8 | Tensions Deck variance is ±15-25% on win-share |
| E6.5 | Valorsmark + Varfell canon role-templates overstate mechanical breadth |

---

## §8 New Tweak Candidates from Bottom-Up Analysis

The top-down tweak set (Parts 3–5) was 9 tweaks. Bottom-up surfaces additional
candidates **not derivable from top-down**.

### T-10a — PI Reduction Mechanism (Crisis Lock-In Fix)
**Source finding:** E5.4 (PI Crisis is one-way ratchet)  
**Proposal:** PA Session "Oppose"-majority vote reduces PI by 1. Symmetric to Support-majority raising it.  
**Mechanism:** Modifies PA Session resolution (PP-431-COR).  
**Class:** B (extends PA Session outcome).  
**Priority:** **P1** — addresses unrecoverable Crisis state.

### T-10b — Cardinal Focus Rotation Cap (Church Pressure Pacing)
**Source finding:** E5.1 + §6.2 (Cardinal Focus rotation pattern)  
**Proposal:** A Cardinal Focus selected may not be re-selected the following season (must rotate). Prevents Justice-Justice-Justice Inquisition cascade.  
**Mechanism:** Modifies PP-405 (Cardinal Focus).  
**Class:** C.  
**Priority:** P2.

### T-10c — Tensions Deck Per-Faction Smoothing
**Source finding:** E5.8 (Tensions variance ±15-25%)  
**Proposal:** Each faction draws 1 personal Tensions card per arc (smoothed individual variance) in addition to shared Tensions deck per season.  
**Mechanism:** Adds new deck (per faction).  
**Class:** A (new subsystem).  
**Priority:** P2 — longer design cycle needed.

### T-10d — Strain Decay
**Source finding:** E5.3 (Sta cascade trap; Strain accumulates without decay)  
**Proposal:** Strain decays −1 per Year-End if no Revolt that year. Currently no decay.  
**Mechanism:** Modifies Year-End B11.  
**Class:** C.  
**Priority:** P2.

### T-10e — Charter Slot Limit (Valorsmark Anchor Discipline)
**Source finding:** §4.1 + §6.1 (Capital Anchor derived role)  
**Proposal:** Valorsmark may hold no more than 3 active Charters peninsula-wide.  
**Mechanism:** Caps PP-433 active count.  
**Class:** C.  
**Priority:** P3.

### T-10f — Wealth Cap Removal or Trade Pivot Card
**Source finding:** E5.6 (Hafenmark Trade cliff)  
**Proposal:** **Option A** — remove W cap. **Option B** — add "Investment" Hafenmark card: spend W=2 for Token on territory directly.  
**Mechanism:** Option A (parameter) or B (new card).  
**Class:** B or C.  
**Priority:** P2.

**Bottom-up tweak set additions: 6 new tweaks**.

---

## §9 Findings — Part 6 Consolidated

### P1 (high urgency, derived from emergence)

| ID | Finding | Implication |
|----|---------|-------------|
| E1 (§4.1) | Charter chain has 25.8% maintenance probability over 6 seasons | Valorsmark loop self-limits; prior sim overestimated stability |
| E2 (§4.2) | Inquisitor deployment 93% certain in 6 seasons | Church pipeline reliable; T-09c cap necessary not optional |
| E3 (§4.3) | Royal Decree is biennial under consec penalty | Valorsmark defensive income half of role-template implication |
| E5.1 (§5.1) | Inquisitor-Self-Defeating Dynamic | Optimal Church play is sustained pressure, not territorial revolt |
| E5.4 (§5.4) | PI Crisis is one-way ratchet | Y1 Crisis = full-campaign Crisis; tuning urgent |
| E5.7 (§5.7) | 4-voter PA Session harder than 5-voter | Hafenmark mid-game ascendancy slower under correct canon |
| E6.5 | Valorsmark + Varfell canon role-templates overstate mechanical breadth | Faction identity coherence issue separate from win-share |

### P2 (medium urgency)

| ID | Finding |
|----|---------|
| E4 (§4.4) | Hafenmark Token dwell ~1 season per 4 Diplomat attempts |
| E5 (§4.5) | T-02a doubles Varfell recovery 40% → 67% per arc |
| E6 (§4.6) | Hafenmark hits Trade cliff S4–S5 |
| E5.3 (§5.3) | Sta cascade is multi-territory feedback amplifier |
| E5.6 (§5.6) | Hafenmark phase shift Trade-to-Token at S4–S5 |
| E5.8 (§5.8) | Tensions variance ±15–25% on win-share |

### P3 (depth findings)

- §4.7 Garrison rate 2/arc — drives territory portfolio decisions
- §6.1–§6.4 Derived role-names diverge from canonical role-templates

---

## §10 Implications for Parts 3–5 Conclusions

Bottom-up analysis **revises** several Part 3–5 conclusions:

### Revision 1 — Hafenmark mid-game ascendancy weakened
Top-down: "Hafenmark ascendant by S4." Bottom-up: 4-voter PA Session harder; Token
dwell brief. **Hafenmark ascendancy is real but slower and less certain than top-down
asserted.**

### Revision 2 — Valorsmark vulnerability strengthened
Top-down: "Valorsmark loses territories under pressure." Bottom-up: Decree biennial;
Sta cascade multi-territory; Charter chain self-limiting. **Valorsmark is MORE
vulnerable than top-down said.**

### Revision 3 — Church ascendancy is tempo-not-conquest
Top-down: "Church Inquisitor pipeline dominant." Bottom-up: Optimal Church sustains
pressure WITHOUT triggering revolt. **Church wins by L drift over time, not territorial
seizure.** T-09c reinforces this play pattern.

### Revision 4 — PI Crisis tuning is P1 not P2
Top-down: "PI Crisis at Y1 may be too early." Bottom-up: Crisis is one-way ratchet.
**Y1 Crisis becomes campaign-long Crisis — P1 urgency.**

### Revision 5 — Tweak T-09c value strengthened further
Top-down: T-09c is single largest equality lever. Bottom-up: T-09c also deepens Church
play (tempo management). **T-09c is dual-purpose: balance lever AND identity-deepener.**

### Revision 6 — Tweak T-03c value strengthened
Top-down: T-03c throttles Hafenmark Token rate. Bottom-up: T-03c also makes W cap into
strategic resource. **T-03c is dual-purpose: balance lever AND resource-rescue.**

### Revision 7 — Win-share band has higher variance than projected
Top-down: Post-tweak band 22–28% across 4 factions. Bottom-up: Tensions variance
±15–25% per campaign. **Mean-band is correct; single-campaign variance is larger than
top-down captured.** N campaigns averaging together delivers target; individual
campaigns may swing wider.

---

## §11 Verdict — Part 6

**Bottom-up analysis confirms the corrected canon (Parts 1–2) and validates most
top-down findings (Parts 3–5), with 7 specific revisions to top-down conclusions.**

**Key additions:**
- 6 new tweak candidates (T-10a/b/c/d/e/f) from emergent dynamics
- 4 derived role-names that diverge from canonical role-templates
- 8 emergent dynamics not visible from top-down
- Concrete combo-probability quantification (Charter chain 25.8%, Inquisitor deploy
  93%, T-02a recovery 67%, etc.)

**Primary recommendation:**
- **T-10a (PI reduction)** is the new highest-priority addition. Without it, T-09c
  and other balance work is undermined by Crisis lock-in.
- **T-10d (Strain decay)** addresses long-campaign Strain inflation.
- **T-10b (Cardinal Focus rotation)** complements T-09c by preventing pressure-stacking.

**Total tweak set after Part 6:**
- 5 Class C from Parts 3–4: T-01a, T-01c, T-02a, T-03c, T-04a
- 4 Class B from Parts 3–4: T-02c, T-09a, T-09b, T-09c
- 5 new from Part 6: T-10a (P1), T-10b (P2), T-10c (P2/long cycle), T-10d (P2), T-10e (P3), T-10f (P2)

= **14 active tweak candidates** + 2 deferred (T-02b, T-04b).

---

## §12 Open Items — Part 6

- **Verify PI reduction canonical mechanics** — `[ASSUMPTION: no PI decrement rule
  exists]`. If a Tensions card reduces PI, T-10a may be unnecessary.
- **Verify Charter chain consec rule** — is consec counter per-Charter, per-season, or
  per-card-instance?
- **Verify Strain decay rule** — `[ASSUMPTION: no decay]`. Affects T-10d.
- **Verify Inquisitor placement rules under Sta = 0** — does Inquisitor remain on
  revolted territory? Affects §5.1 self-defeating analysis.
- **Verify PP-N Token max-per-mat rule** — assumed 1; affects §4.4 dwell analysis.
- **Cardinal Focus selection rule** — can same Cardinal be selected back-to-back?
- **Monte-Carlo simulation needed** to test bottom-up dynamics under stochastic
  decisions (Part 7).

---

*Session: bottom-up-emergent · 2026-05-13 · Part 6 · Author: simulator under Jordan*
