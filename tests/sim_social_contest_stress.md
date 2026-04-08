# Social Contest — Stress Test
## Mode A (Isolation) + D (Edge Cases) + J (Cross-Mode) + L (Precedent)
## Date: 2026-04-08
## Sources: debate_system_redesign_v1.md Part 6 v1.5 (canonical) + params_debate.md v0.14+design-ST4-R1

---

## FETCH LOG
- designs/debate/debate_system_redesign_v1.md: ✓ 787 lines
- references/params_debate.md: ✓ 366 lines
- canon/02_canon_constraints.md: ✓ 25 lines
- skills/valoria-simulator/SKILL.md: ✓ 199 lines

**Canonical source:** designs/debate/debate_system_redesign_v1.md (Part 6 operative)
**Note:** Significant divergence between canonical design doc and params_debate.md on interaction type names and mechanics. Design doc treated as authoritative per canonical_sources.yaml; divergences flagged as P1.

---

## MODE A — Argue Pool Isolation

Pool formula (PP-232): (Cognition × 2) + History bonus, TN 7

| Pool | Expected Net | P(≥1) | P(≥2) | P(≥3) | P(≥4) |
|---|---|---|---|---|---|
| 2D (Cog 1, H0) | 0.66 | ~47% | ~18% | ~5% | ~1% |
| 4D (Cog 2, H0) | 1.32 | ~80% | ~50% | ~25% | ~9% |
| 6D (Cog 2, H1) | 1.98 | ~92% | ~70% | ~45% | ~22% |
| 8D (Cog 3, H1) | 2.64 | ~97% | ~82% | ~60% | ~35% |
| 10D (Cog 4, H1) | 3.30 | ~99% | ~90% | ~73% | ~50% |
| 11D (Cog 4, H1+Mem) | 3.63 | ~99% | ~93% | ~79% | ~57% |
| 13D (Cog 5, H1+Mem) | 4.29 | ~99% | ~97% | ~87% | ~70% |

Memory bonus (+2D): significant. ~+0.66 expected net. Strong incentive to cite every exchange.
Momentum spend (1 auto-success): equivalent to ~3D value at TN7. Very high value.

### Conviction Track Movement Table
effective_margin = floor(margin × genre_weight × orientation_weight)
CT move = effective_margin − resistance (if positive)

| Margin | GW 1.0, OW 1.0, R=1 | GW 1.5, OW 1.0, R=1 | GW 0.5, OW 1.0, R=1 |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 2 | 0 |
| 3 | 2 | 3 | 0 |
| 4 | 3 | 5 | 1 |
| 5 | 4 | 6 | 1 |

---

## MODE D — Edge Cases

### FINDING D-01 [P2] — Genre ×0.5 Near-Inert Against R=1
**Setup:** Off-primary genre (GW 0.5) exchange, any audience with R=1.
**Mechanism:** Margin 3 in GW 0.5 → floor(1.5)−1 = 0 CT movement. Margin must reach 4+ for CT+1.
**Severity:** P2 — produces bad play experience (genre diversity collapses).
**Frequency:** Every debate with R=1 audience (majority of proceedings).
**Proposed fix:** Reduce R by 1 for off-primary genre exchanges (incentivises genre diversity vs. always CLASHing in primary), or raise GW floor to 0.75.

### FINDING D-02 [P2] — Doubt Marker Scale-Dependency
**Setup:** Obscuring win against opponent with low pool vs. high pool.
**Mechanism:** Doubt Marker reduces winner's next effective_margin by 2. At low margins this denies all movement; at high margins it's meaningful but not canceling.
**Severity:** P2 — Obscuring is dominant counter against evenly-matched opponents, weak against significantly stronger ones.
**Frequency:** Moderate — every Obscuring strategy.
**Proposed fix:** Confirm as intended asymmetry; document in GM reference.

### FINDING D-03 [P2] — Focus Attribute Source Unconfirmed
**Setup:** Concentration = Focus + Presence. Focus not listed in params_debate.md derived values.
**Mechanism:** If Focus is not a confirmed standard attribute, Concentration is mechanically undefined.
**Severity:** P2 — missing derivation.
**Frequency:** Every debate.
**Proposed fix:** Fetch params_core.md to confirm Focus attribute. Flag: [GAP: Focus attribute source — requires params_core.md verification.]

### FINDING D-04 [P2] — Regroup-on-Spent Dominant When Losing
**Setup:** Character reaches Concentration 0 (Spent). Next exchange they would lose.
**Mechanism:** Regroup consumes Spent without applying −2D/+1D penalty. Cost: CT+1 to opponent. Benefit: escape full Spent penalty. When Spent + about to lose, Regroup cost (CT+1) < Spent exchange penalty (−2D to pool + opponent +1D on an exchange you'd lose anyway).
**Severity:** P2 — rational dominant choice removes risk from Spent mechanic.
**Frequency:** Moderate — any character who reaches Spent while losing.
**Proposed fix:** Apply CT+2 on Regroup-while-Spent (increased cost to preserve Spent as a meaningful penalty state).

### FINDING D-05 [P2] — Focus 1 Regroup Trap
**Setup:** Character with Focus 1 reaches Spent; declares Regroup.
**Mechanism:** Regroup restores Concentration by Focus score = +1. But Regroup counts as exchange loss → Concentration −1 additional. Net: +1−1 = 0 restore. Character gives up exchange for CT+1 against them and zero Concentration gain.
**Severity:** P2 — trap for low-Focus characters; Regroup is mechanically pointless.
**Frequency:** Any Focus 1 character in long debates.
**Proposed fix:** Regroup restores minimum 2 Concentration regardless of Focus score, OR the loss-depletion does not apply during Regroup.

### FINDING D-06 [P3] — Rattled+Spent Terminal State
**Setup:** Character with Cog 2 (4D pool) reaches both Rattled and Spent simultaneously.
**Mechanism:** 4D − 4D = 0D → floored to 1D. P(winning any exchange) near zero. State is functionally terminal.
**Severity:** P3 — intended consequence; character should Unmask. Note as design feature.
**Frequency:** Low but possible in Grand Debates.
**Proposed fix:** No fix needed. Confirm as intended terminal state triggering Unmask.

### FINDING D-07 [P1] — Obscuring Orientation Weight vs Doubt Marker Conflict
**Setup:** CLASH exchange, winner uses Obscuring orientation.
**Mechanism:** Formula uses `orientation_weight_of_winner`. params_debate specifies Obscuring OW = ×0.75. But Obscuring win rule says CT does not move — Doubt Marker placed instead. The OW affects effective_margin formula but then the result is discarded by the Doubt Marker rule.
**Conflict:** Is effective_margin calculated (with OW 0.75) and then discarded? Or does the Obscuring check fire before the formula runs? Resolution sequence undefined.
**Severity:** P1 — ambiguous resolution order in Obscuring CLASH.
**Frequency:** Every Obscuring CLASH exchange.
**Proposed fix:** Specify resolution sequence: Obscuring orientation check fires BEFORE effective_margin formula. If Obscuring wins: skip formula, place Doubt Marker. The OW 0.75 from params_debate is irrelevant and should be struck.

### FINDING D-08 [P2] — DIVERGENCE Fumble Concentration Depletion Undefined
**Setup:** DIVERGENCE exchange where one orator fumbles (negative net successes).
**Mechanism:** DIVERGENCE: "no strain dealt." But §6.4 Step 6: "−1 additional on any exchange loss." Fumbling in DIVERGENCE — is it an "exchange loss"? Undefined. DIVERGENCE produces CT movement if effective_margin > resistance; a fumble produces 0 CT movement for that side. Is 0 CT movement a "loss"?
**Severity:** P2 — missing rule creates inconsistency.
**Frequency:** Any fumble in DIVERGENCE.
**Proposed fix:** Clarify: DIVERGENCE exchange produces no "winner/loser" designation. Concentration depletes −1 per exchange (fixed) for both. The additional −1 on loss does not apply to DIVERGENCE.

### FINDING D-09 [P1] — TIE Override Conflicts With DIVERGENCE No-Strain Rule
**Setup:** DIVERGENCE exchange where both orators roll 0 net successes.
**Mechanism:** TIE override ("any interaction type"): both take 1 strain, CT +1 toward initiative holder. But DIVERGENCE rule: "No strain dealt." These directly conflict. TIE override explicitly states it takes priority.
**Severity:** P1 — confirmed rule conflict; TIE override produces strain in a context DIVERGENCE explicitly prohibits it.
**Frequency:** Low but possible in any DIVERGENCE exchange with weak pools.
**Proposed fix:** TIE override should be scoped to CLASH and COMPETITION only. DIVERGENCE both-zero: neither side's effective_margin exceeds resistance, no CT movement, no strain.

### FINDING D-10 [P3] — Focus Defence Overcapping at Low Margins
**Setup:** Character with Focus 6 (Focus defence = 3) faces winner with margin 1, Presence modifier 0.
**Mechanism:** Raw strain = margin + 1 + 0 = 2. Focus defence 3 would reduce to −1, floored to 1.
**Severity:** P3 — diminishing returns on Focus above ~4 are sharp. Design feature.
**Frequency:** Any high-Focus character in low-margin exchanges.
**Proposed fix:** No fix needed. Document as intended diminishing returns.

### FINDING D-11 [P1] — Interaction Type Name and Mechanic Conflict Between Canonical Docs
**Setup:** Canonical design doc §6 uses: CLASH, COMPETITION, DIVERGENCE, TIE.
params_debate.md uses: CLASH, AMPLIFY, CROSS, DIVERGE.
**Mechanism:**
- COMPETITION (same genre, same orientation): margin-based, strain formula (margin−1, min 1) + 1 + PresModifier.
- AMPLIFY (params): combined pool vs resistance, cap at highest pool × 2 (PP-242/250).
These are mechanically incompatible. CROSS (params) resolves simultaneously (PP-245); DIVERGENCE (design doc) resolves independently with successes halved.
**Severity:** P1 — canonical document diverges from patched params on operative mechanics.
**Frequency:** Every same-orientation exchange, every different-genre exchange.
**Proposed fix:** The design doc must be updated to reflect patches PP-242, PP-245. Until updated, flag: use params_debate.md AMPLIFY/CROSS mechanics as operative, noting canonical source is stale. [EDITORIAL: ED-XXX — design doc Part 6 needs patch sync for AMPLIFY/CROSS/DIVERGE].

### FINDING D-12 [P1] — Resistance Formula Conflict
**Setup:** Design doc §6.1: resistance = ceil(average Stability) − 1, minimum 0, typical range 0–2.
params_debate.md PP-278: resistance = ceil(Stability/4).
**Mechanism:** Stability 5 audience → design doc: ceil(5)−1 = 4; params: ceil(5/4) = 2. Radically different. Design doc formula makes Formal Debates near-impossible for solo orators at typical Stability values. Params formula produces 1–2 for all normal audiences.
**Severity:** P1 — different formula produces different game.
**Frequency:** Every debate with an audience.
**Proposed fix:** Params formula (PP-278) is correct. Design doc §6.1 Step 4 must be updated to `resistance = ceil(average Stability / 4)`.

### FINDING D-13 [P2] — Debate Fatigue Punishes Persisting Over Conceding
**Setup:** Character is Rattled mid-debate and continues (does not Unmask).
**Mechanism:** Winning while Rattled generates Debate Fatigue (−1D on next social roll this session). A character who persists and wins faces a social penalty the rest of the session. A character who concedes or Unmaskes does NOT generate Fatigue (Fatigue only triggers on Rattled, not on concession). Conceding is structurally less costly than persisting-and-winning.
**Severity:** P2 — perverse incentive; winning while hurt is worse than conceding gracefully.
**Frequency:** Any character who reaches Rattled in a meaningful debate.
**Proposed fix:** Debate Fatigue triggers on Rattled regardless of outcome (concede or win). Orators who avoid Rattled entirely never incur it. This removes the perverse incentive.

### FINDING D-14 [P1] — Dominant Strategy: Primary Boosted Genre + Revealing Every Exchange
**Setup:** Any Formal or Grand Debate with identifiable audience ethical mode.
**Mechanism:** GW 1.5 × OW 1.0 is the maximum effective_margin multiplier. Off-primary (GW 0.5) produces zero movement at margins 1–3 against R=1. Appraise (Step 1) reliably identifies primary genre at Success (2 net), achievable with Attunement 2+. Memory bonus available in any genre — no reason to use it in off-primary. The only rational counter is Obscuring (Doubt Marker), which is a damage mitigation play, not a genre pivot.
**Severity:** P1 — game-theoretic dominant strategy exists; genre selection is not a meaningful decision for the winning side after successful Appraise.
**Frequency:** Every debate where one side achieves Appraise Success.
**Proposed fix (options):**
1. Raise off-primary genre weight floor to 0.75 (genre diversity produces CT movement).
2. Cap primary genre CT movement per exchange at +2 (prevents genre-lock being optimal).
3. Introduce a genre-counter mechanic (analogous to weapon type matchups — one genre is strong against another in specific contexts).

### FINDING D-15 [P2] — Memory Bonus Verification Has No Mechanical Enforcement
**Setup:** Any exchange where Memory bonus claimed.
**Mechanism:** "+2D when citing a specific, named, verifiable claim." No roll to verify claim accuracy. No action in Part 6 operative system to contest a Memory bonus claim (Challenge exists in deprecated quaestio only).
**Severity:** P2 — play culture dependency; incentivises unverifiable claims.
**Frequency:** Every exchange where Memory bonus is claimed.
**Proposed fix:** Introduce a Refute action (replaces or adds to opponent's Appraise step) allowing opponent to spend Attunement roll (Ob 2) to contest a Memory bonus claim. Success: bonus denied + opponent takes −1D to next roll from the false claim. Failure: Refute costs challenger 1 strain.

### FINDING D-16 [P2] — Corroboration Knot Requirement Conflict
**Setup:** Character wants to corroborate an orator they have no Knot with.
**Mechanism:** Design doc §3.5 (provisional reference per GAP-DS-12): Knot required. params_debate ED-014 (PP-260): Knot not required, any ally who witnessed relevant event can corroborate. Canonical doc says Knot required; params overrides this.
**Severity:** P2 — canonical doc stale on specific mechanic. Params resolution is better design (more accessible corroboration).
**Frequency:** Any debate with corroborators.
**Proposed fix:** Update design doc §6.4 Step 2b with ED-014 resolution text. Canonical: any witnessing ally may corroborate; Knot holders give full Knot bonus.

### FINDING D-17 [P2] — GM Bookkeeping Load
**Setup:** Any Formal or Grand Debate with audience.
**Mechanism:** GM must track simultaneously: CT position, genre weights (per faction ethical mode), orientation weights, Appraise results, dice pools (variable per character), strain accumulation, Composure thresholds, Concentration per character, Rattled/Spent states, Doubt Markers, initiative holder, exchange count, role structure, Belief alignment check, pre-debate Preparation bonus. ~40 operations per exchange. No reference card exists (acknowledged, deferred to compilation).
**Severity:** P2 — not a rules break but a play-experience break. High cognitive load concentrated in GM.
**Frequency:** Every debate.
**Proposed fix:** Production task: GM ledger card (as acknowledged in ED-141/PP-321). Prioritise before first playtesting session.

### FINDING D-18 [P3] — Belief Alignment Creates Structural Advantage
**Setup:** Character whose Belief aligns with debate question's genre.
**Mechanism:** Winning exchange while arguing for Belief-aligned position = Momentum gain (up to 1 per debate). Characters whose Beliefs align with primary boosted genre get: Genre bonus (GW 1.5) + Belief Momentum on win. Characters misaligned face structural disadvantage unrelated to debate skill.
**Severity:** P3 — minor; Momentum gain is valuable but capped at 1. Intended character-differentiation mechanic.
**Frequency:** Character-specific; varies by Belief and debate context.
**Proposed fix:** No fix needed. Document as intentional character-differentiation.

---

## MODE J — Cross-Mode Consistency

### FINDING J-01 [PASS] — BG Parliamentary Vote Resolution Consistent
BG uses Mandate pool TN7, resistance 0–2 from Abstaining high-Stability factions. Consistent with TTRPG resistance range under PP-278. Thread consequences correctly excluded. ✓

### FINDING J-02 [PASS] — Hybrid Layer RS Propagation Correct
Hybrid debates: TTRPG-layer RS changes apply; BG layer has no RS equivalent. P-14 satisfied via TTRPG personal debate. ✓

### FINDING J-03 [PASS] — Pre-Debate Preparation Cross-Mode Clean
TTRPG/Hybrid use Attunement+History prep roll. BG uses prior Diplomacy domain action. Clean abstraction. ✓

### FINDING J-04 [P1] — §3.8 Thread Consequences Partially Narrated — Possible P-01 Violation
**Setup:** Evidence genre win fires Thread co-movement per §3.8.
**Mechanism:** §3.8 says "The audience re-experiences the cited past. Observers with Thread Sensitivity 30+ perceive a thread-shimmer in the room. Rendering Stability +1." RS+1 is automatic. But the epistemic auto-effect ("audience re-experiences the cited past") and actual auto-effect are described narratively, not as mandatory mechanical triggers with defined outputs.
**Canon constraint P-01:** "Every thread operation MUST produce automatic co-movement effects across all three dimensions... No GM discretion to skip."
**Conflict:** If §3.8 genre-win Thread consequences are treated as Thread operations (which they appear to be, given RS changes), then P-01 requires all three dimensional auto-effects to fire automatically with no GM discretion.
**Severity:** P1 — potential P-01 violation.
**Frequency:** Every debate with genre winner producing Thread consequence.
**Proposed fix:** Clarify whether §3.8 genre-win consequences are full Thread operations (requiring mandatory P-01 auto-effects) or are co-movement consequences that do not trigger the full three-dimensional auto-effect protocol. If the former: codify mandatory epistemic and actual auto-effects for each genre. If the latter: note they are co-movement events distinct from Thread operations.

---

## MODE L — Precedent Check vs Combat

| Feature | Combat | Social Contest | Parity? |
|---|---|---|---|
| Resource arc | Stamina depletes per round | Concentration depletes per exchange | ✓ |
| Recovery action | Take a Breath (round lost, no positional cost) | Regroup (exchange lost, CT+1 permanent cost) | ✗ — Regroup costlier |
| Recovery cost | 0 permanent consequence | CT+1 permanent (cannot be recovered) | Asymmetric |
| Action variety | 7 actions | 5 actions | Acceptable — social is simpler |
| Complexity distribution | Player-side and GM-side roughly even | Heavily GM-side | ✗ |
| Dominant strategy disruption | Multiple (feint, range, guard, disarm) | Partial (Obscuring viable when losing only) | ✗ (see D-14) |
| Group dynamic | Fibonacci bonus (automatic, no constraint) | Corroboration (constrained by witnessing, Knot holders superior) | ✓ — constrained intentionally |

### FINDING L-01 [P2] — Recovery Cost Asymmetry vs Combat Precedent
**Setup:** Regroup vs Take a Breath.
**Mechanism:** Take a Breath costs one round — no permanent positional consequence. Regroup costs one exchange PLUS CT+1 toward opponent (permanent CT position change). Debate recovery is structurally more expensive than combat recovery.
**Severity:** P2 — asymmetry is significant if intentional tension is desired, but may make Formal Debates (3 exchanges) near-unwinnable for anyone who needs to recover.
**Frequency:** Any character who Regroups.
**Proposed fix (options):**
1. Reduce Regroup CT penalty from +1 to 0 (exchange is forfeited but no CT consequence — mirrors Take a Breath cost structure).
2. Or: retain CT+1 but allow Concentration restore to compensate at higher rates (Focus × 1.5 round up on Regroup).

### FINDING L-02 [P3] — No Challenge Equivalent in Part 6 Operative System
**Setup:** Opponent claims Memory bonus with questionable source.
**Mechanism:** Challenge action (§3.4, quaestio) was the verification mechanism. Quaestio deprecated. No Part 6 equivalent.
**Severity:** P3 — play culture dependency for Memory bonus verification.
**Frequency:** Any Memory bonus claim.
**Proposed fix:** Port Challenge equivalent into Part 6 as the Refute action (see D-15 proposed fix).

---

## PRIORITY FINDINGS SUMMARY

| ID | Sev | Description |
|---|---|---|
| D-11 | **P1** | Canonical design doc vs params_debate: incompatible interaction type names and mechanics (COMPETITION vs AMPLIFY; DIVERGENCE vs CROSS). Design doc stale. |
| D-12 | **P1** | Resistance formula conflict: design doc `ceil(Stability)−1` vs params PP-278 `ceil(Stability/4)`. Different results at typical Stability. |
| A-01 | **P1** | Off-primary genre (GW ×0.5) near-inert vs R=1. Dominant strategy: CLASH in primary boosted genre every exchange. Genre diversity collapses. |
| D-09 | **P1** | TIE override "any interaction type" fires in DIVERGENCE both-zero case, producing strain — contradicts DIVERGENCE "no strain" rule. Irresolvable without scoping fix. |
| D-07 | **P1** | Obscuring OW (×0.75 params) vs Doubt Marker rule (replaces CT movement). Resolution order ambiguous; OW calculation may be moot. |
| J-04 | **P1** | §3.8 Evidence/genre Thread consequences partially narrated — potential P-01 (Inseparability) violation if treated as Thread operations. |
| D-14 | **P1** | Dominant strategy confirmed. No effective counters from genre diversity. Structural fix required. |
| D-13 | **P2** | Debate Fatigue triggers on Rattled; winning-while-Rattled generates it but conceding does not. Perverse incentive favours concession over persistence. |
| D-16 | **P2** | Corroboration Knot requirement: design doc says required; params ED-014 says removed. Canonical stale. |
| D-17 | **P2** | GM bookkeeping load ~40 operations per exchange. Reference card needed before playtesting. |
| D-05 | **P2** | Focus 1 Regroup trap: net Concentration restore = 0. Character trapped. |
| D-04 | **P2** | Regroup-on-Spent dominant when losing — rational to always Regroup on Spent, negating Spent penalty. |
| D-08 | **P2** | DIVERGENCE fumble: Concentration depletion from "exchange loss" undefined for DIVERGENCE. |
| D-15 | **P2** | Memory bonus has no verification mechanic in Part 6. Play culture dependency. |
| D-03 | **P2** | Focus attribute source not confirmed in fetched params_debate.md. |
| L-01 | **P2** | Regroup costs CT+1 (permanent); Take a Breath costs only the round. Recovery asymmetry vs combat precedent. |
| D-02 | **P2** | Doubt Marker scale-dependent: denies all movement vs. weak opponents, weak vs. strong. |
| D-06 | **P3** | Rattled+Spent → 1D pool → terminal. Intended. Note as feature. |
| D-10 | **P3** | Focus defence diminishing returns above ~4. Intended. |
| D-18 | **P3** | Belief-aligned characters doubly incentivised (GW bonus + Momentum). Intended differentiation. |
| L-02 | **P3** | No Challenge/Refute equivalent in Part 6 for Memory bonus contestation. |

**P1: 7 | P2: 11 | P3: 3**

**SIM-DEBT-02:** Corroboration in CLASH calibration (noted in params_debate) remains unresolved.
**SIM-DEBT-03 (new):** Dominant strategy (D-14) — genre weight system needs redesign simulation once fix is proposed.

