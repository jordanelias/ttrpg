# Resolution Diagnostic — Personal Combat

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stage 1)
**Scope:** personal combat per skill INITIAL HYPOTHESES — covers `designs/scene/combat_v30.md`, `params/combat.md`, `designs/scene/derived_stats_v30.md` §4.1 (Health AUTHORITATIVE) + §4.2 (Stamina). Cross-references: threadwork (Pool Floor 5 universal), mass_battle (wound penalty universal per PP-716), faction_layer (Trigger 5 cross-scale coupling).
**Status:** Audit output. Commits blocked (B6) — staged inline.
**Standing caveat:** open handoff `2026-05-17-scene-combat-redesign-exploration` — 5 directions under analysis, Jordan-decision-owned. This diagnostic runs as **defect-surface only**: maps findings to lessons and stops. Does NOT prescribe among the 5 directions. Convergence between any finding's remediation and an open direction is flagged as `[OPEN TRADE-OFF: defers to handoff resolution]`, not recommended.

## §0 Pre-flight & citations

**Files consulted this session:**

- `designs/scene/combat_v30.md` — full + sections §1 Combat Pool, §2 Round Structure, §3 Initiative, §4 Actions, §5 Weapon System (head; truncation at ~10k of 38k for working-set focus, key formulas captured)
- `params/combat.md` — full + sections Pool Formula, Weapon System, Damage Formula, Initiative, Fibonacci, Wounds/Incapacitation, Mass Mismatch, Armour, Ranged
- `designs/scene/derived_stats_v30.md` — full + sections §1 Core Architecture, §4.1 Health (AUTHORITATIVE per PP-716), §4.2 Stamina
- `tests/audit/pp717_ners_all_directions.md` — full (Mode A formula validation + Mode C interaction chains + NERS per D1–D5 + 6-directional balance)
- `tests/audit/combat_integration_session_a_ners.md` — full (chassis validation, internal-consistency check, STR-multiplier ambiguity flagged)
- `tests/audit/all_directions_ners_v27.md` — partial (~9k of 17k; Throughlines + Meta-Throughlines + NERS per direction)
- `canon/02_canon_constraints.md` — full (P-01–P-15 + GD-1/2/3)
- `references/canonical_sources.yaml` — full
- `skills/valoria-mechanic-audit/SKILL.md` — full

**NERS source:** PI `<definitions>` block (canon/definitions.yaml HTTP 404 per Turn B).

**Prior-art relationship:**
- `pp717_ners_all_directions.md` is the **most recent ratified-state audit** — D1 (MW cap 3), D2 (Pool DR above Agi 4), D3 (Crit ≥ 4), D4 (mace commitment +2D), D5 (defense triangle). Validates Modes A/C; assigns NERS per change. My diagnostic builds on it rather than redoing — I check the ratified state for residual issues under the resolution-fitness lens.
- `combat_integration_session_a_ners.md` is the chassis spec validation. Confirms canonical-citation discipline + phase machine + Pool Floor + Health/MW/WI. Surfaces STR-multiplier ambiguity (C6 below).

## §1 Phase 0 — Resolution component decomposition

Combat is a **composite**:

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Combat Pool** | `(Agility × 2) + Hist + 3, min 5` per current canon — but **PP-717 D2 ratified as `min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3` per audit** (see C2) | Dice (aggregated, floored) |
| **B · Pool split (Offence/Defence)** | Each round, declare allocation; lower-init declares first, higher-init declares with information | Dice allocation |
| **C · Action selection** | Strike / Feint / Defend (Burning Wheel triangle) + Establish Distance / Tie Up / Disarm / Rescue / Dodge | Discrete choice, action-triangle loop |
| **D · Hit roll** | Pool dice vs weapon-derived TN (base 7.0, adjusted by reach/weight/type/2H) | Dice resolution |
| **E · Damage** | `net hits + STR × multiplier + weapon modifier vs armour tier` | Deterministic + crit-doubling at net ≥ 4 |
| **F · Wound tracking** | Wounds at `floor(cum_damage / WI)`, WI = End+6 | Discrete accumulator on a continuous resource |
| **G · Health** | `(End+6) × (MW+1)`, MW = `min(floor(End/2)+1, 3)` per PP-717 D1 (AUTHORITATIVE §4.1) | **Continuous resource** |
| **H · Stamina** | `End × 5`, drains by per-action cost (5 std / 8 heavy / 3 def); OOB at 0 → −2D | **Continuous resource** |
| **I · Wound penalty** | `−1D to ALL Pools` per PP-716, capped by per-Pool floor (Combat 5 / Thread 5) | Modifier on dice pool |
| **J · Initiative** | Information advantage (declare-last), not action speed | Discrete state |
| **K · Feint sub-game** | Allocate N≥3 to Offence, contest vs Defence, margin reduces opponent pool next round; non-stacking, expires on incapacitation | Dice + state-effect (single-round) |
| **L · Stage 1/2 incapacitation STRUCK (ED-130)** | Health → 0 = incapacitated. No staged dying. | Simplification |

**Three-category classification of key quantities:**

- **Continuous resources:** Health, Stamina. Multipliers (×10 effective for Health via MW+1, ×5 for Stamina) per derived_stats §3 Multiplier Tiers. Lessons 2/6 apply.
- **Base parameters:** Agility, Endurance, STR, History (1–7 except History which is 0–4 or higher), fed into Combat Pool / Health / Stamina formulas. Lesson 2 applies at formula level.
- **Discrete accumulators:** Wound counter (0 → MW+1), crit threshold (binary trigger at net hits ≥ 4). Per skill three-category table — Lessons 2/6 exempt.

**Stamina round-count cliffs note (per v27 Meta-Throughline B):** Stamina is continuous, but discrete action costs (5/8/3) produce round-count cliffs at integer Stamina boundaries (24→25 = 4→5 rounds at cost 5). v27 audit: "real but invisible — a teaching/UI problem, not a mechanics problem." Per skill: continuous quantity has continuous behavior; the cliff is in the *consumption* arithmetic, not the *quantity*. Phase 3b note, not violation.

## §2 Phase 1 — Stress points

### 1a · Smallest pool by design, and after degradation

**By design** — Combat Pool minimum is 5 (floor). This is by explicit safeguard:

| Build | Agi | Hist | Pre-floor pool | Floored | Status |
|---|---|---|---|---|---|
| Untrained low-Agi | 1 | 0 | 2+0+3=5 | 5 | floor active |
| Untrained avg-Agi | 3 | 0 | 6+0+3=9 | 9 | above floor |
| Trained low-Agi | 1 | 3 | 2+3+3=8 | 8 | above floor |
| **PP-717 D2 audit formula at Agi 6 Hist 3** | 6 | 3 | 4×2 + 2×1 + 3 + 3 = 16 | 16 | above floor |
| **Current canon formula at Agi 6 Hist 3** | 6 | 3 | 12 + 3 + 3 = 18 | 18 | above floor (drift, see C2) |
| Agi 0 (impossible — attribute floor 1 per Foundations, but for completeness) | 0 | 0 | 0+0+3=3 | 5 | floor active |

**Pool floor 5 IS the safeguard against the small-pool problem in combat.** Distinct from the faction layer where no floor exists.

**After degradation** — convergent pressure sources:
- Wound penalty: −1D per wound, **capped by Combat Pool floor 5** (derived_stats §4.1: "Cumulative; capped by per-Pool floor")
- OOB (Out of Breath at Stamina 0): −2D to all rolls until Take-a-Breath. **Interaction with Pool floor 5 UNDEFINED in canon** (C3 below)
- Stunt arena penalty: GM may apply (TTRPG residue; videogame removes per PP-717)

At Agi 4 Hist 3 = pool 11 (current) or 11 (audit — `4×2+0+3+3=11`, same). With 3 wounds and OOB:
- Per current canon: 11 − 3 (wounds) − 2 (OOB) = 6, still above floor
- Per audit formula: same arithmetic, same result

The floor's role is most active at low-Agi builds in stress. A trained Agi-3 character with 3 wounds: 9 − 3 = 6. With OOB additionally: depends on C3.

### 1b · Exposure frequency

| Stress case | Path | Likelihood |
|---|---|---|
| Pool at floor 5 with 1+ wound (no impact due to floor) | Low-Agi build + sustained engagement | M (build-dependent) |
| Pool at floor 5 with OOB (impact undefined per C3) | Low-Agi + extended duel + no Take-a-Breath | M |
| Heavy armour + low End → OOB in ~2–3 rounds | High-loadout build (v27 audit Vertical: "End 4 Heavy: 20/(5+2)≈2-3 rounds") | M (player choice) |
| Crit-firing at net ≥ 4 | High-pool + good roll | "~5–24%" (pp717_ners D3 Smooth analysis) |
| Floor-pool character incapacitated by damage | Any wound damage exceeds remaining Health pool | M (depends on Health-vs-pool build) |

`[FREQUENCY SIGNAL: combat_integration audit Horizontal: "Heavy armour: not tested. The stamina drain interaction needs validation." Stress cases at high-loadout × low-End builds remain untested under the current chassis.]`

## §3 Phase 2 — What the stress point decides

### 2a · Outcome type at the floor

| Action @ floor (pool 5) | Outcome type | Depth |
|---|---|---|
| Strike at floor pool | **Continuous magnitude** (net hits → damage formula → Health drain) | shallow per exchange; deep across rounds (Stamina-bounded clock) |
| Wound accrual | Discrete (every WI damage = +1 wound) | clock-like (each wound is a tick) |
| Crit fires (net hits ≥ 4) | Binary trigger | rare at floor pool (5D — P(≥4)=0.087 at p=0.4) |
| Incapacitation (Health 0) | Binary terminal | clock-deep (Health × multiplier means many ticks before fire) |

The combat **outcome is graded-magnitude**, not binary — damage accrues continuously, Health drains continuously, wounds tick discretely. Per skill Phase 2a: "Graded-magnitude outcomes at a small pool are *also* dangerous (magnitude swings violently)." At floor pool 5D, magnitude swing per hit: net hits range 0–5, typical 1–2. Damage swing: +STR×mult + weapon mod = +4 to +12 typical. Variance is high relative to Health pool (40 at End 4) — a single high-magnitude hit can cross a wound threshold.

### 2b · Stakes & reversibility

| Outcome | Reversibility |
|---|---|
| Wounds accrued | Clear at session end (canonical per §4.1); stabilised characters return after one scene of rest |
| Incapacitation (Health 0) | Recoverable IF stabilised in scene (Medicine Ob 2; PP-269 says stabilised survives) |
| Death | Stage 2 (Dying) STRUCK per ED-130. Currently Health 0 = incapacitated, not dead. **No mechanical death in current canon outside of GM narrative.** |
| Capture (named officer NPC) | Feeds faction Trigger 5 (cross-scale; covered in faction L1) |
| Damage to lower Health build at floor pool | Single fight may incapacitate, but recovery is structurally available |

**Reversibility is high** in current combat compared to faction layer. ED-130 STRUCK Stage 1/2 dying — no incremental walk to death; just incapacitation. This is a deliberate simplification.

### 2c · Risk profile (worst stress cases)

| Scenario | Impact | Exposure | Irreversibility |
|---|---|---|---|
| Floor-pool build vs higher-pool opponent in extended duel | M | M | L (recovery available) |
| Heavy armour + low End → OOB chain | M | M (player choice) | L |
| Crit landing on already-wounded floor-pool character | H (1 hit can finish) | L (low crit prob at floor pool) | L |
| Named officer captured → Trigger 5 → faction Stab loss | M | L (per-engagement) | M (cross-system; covered in faction diagnostic L1) |

**No H/H/H findings.** Highest is single-H (impact); the combat system's safeguards (Pool floor 5, MW cap 3, ED-130 strikes, wound clearance at session end) prevent the kind of "fragile binary on irreversible outcome" that the faction layer exhibits.

## §4 Phase 3 — Effect-curve checks

### 3a · Impact uniformity

**Combat Pool scaling per Agi:**

Per current canon `Pool = Agi×2 + Hist + 3, min 5`:
- Agi 1 → pool 5 (floor; effective +0)
- Agi 2 → pool 7 (+2)
- Agi 3 → pool 9 (+2)
- Agi 4 → pool 11 (+2)
- Agi 5 → pool 13 (+2)
- Agi 6 → pool 15 (+2)
- Agi 7 → pool 17 (+2)

Linear +2D per Agi above 1 (after floor). **Non-uniform impact in probability terms** (each +2D adds less probability at higher pools, classic √N scaling).

Per **PP-717 D2 audit-ratified formula** (Pool DR above Agi 4):
- Agi 1–4 → +2D per point above floor
- Agi 5–7 → +1D per point

This is **Lesson 2 mitigation: diminishing returns implemented above the median**. Per pp717_ners D2 Smooth: "DR only affects the Combat Pool formula. All other Agi uses (initiative, distance ED, Thread reactions) use raw Agi. No friction with other systems." Pass.

**But** — see C2: this formula is **NOT propagated to the design doc or params file.** Active drift. Sim against stale params produces wrong builds (Agi 6 = 17 pool against canon, 15 against audit).

**Health super-linear at low End:**

Per derived_stats §4.1 reference table:

| End | WI | MW | Health | ΔHealth per End-point |
|-----|----|----|--------|----------------------|
| 1 | 7 | 1 | 14 | — |
| 2 | 8 | 2 | 24 | **+10 (+71%)** ← MW threshold 1→2 |
| 3 | 9 | 2 | 27 | +3 (+12%) |
| 4 | 10 | 3 | 40 | **+13 (+48%)** ← MW threshold 2→3 |
| 5 | 11 | 3 | 44 | +4 (+10%) |
| 6 | 12 | 3 | 48 | +4 (+9%) |
| 7 | 13 | 3 | 52 | +4 (+8%) |

**PP-717 D1 (MW cap 3) fixed the top end** — Health-per-End-point smoothed from End 4 onward (consistent +4 HP). **Low-end (End 1→2 and 3→4) still has jumps** at MW thresholds.

Per Lesson 2 scope (continuous resources + base parameters take uniform-impact steps): Health max is a continuous-resource capacity derived from a base parameter (End). The +71% jump at End 1→2 is non-uniform-impact at the low end. **C5: residual Lesson 2 candidate at low-End builds.**

Exposure low — players rarely invest at End 1–2 in builds. Per pp717_ners D1 Robust: PP-717 D1 was specifically calibrated to address the high-end (End 6+ dominance); low-end was not in scope. Severity M/L/L → P2.

**Wound penalty −1D uniform-form, non-uniform-impact** (Binomial(n, 0.4) ≥ 3 — "decent hit count" benchmark; verified):

| Pool | P(≥3 hits) | After −1D | Δ absolute | Δ relative |
|---|---|---|---|---|
| 17D (Agi 7 Hist 3 — pre-DR) | 0.989 | (16D) 0.982 | −0.007 | −0.7% |
| 11D (Agi 4 Hist 3) | 0.881 | (10D) 0.833 | −0.048 | −5.4% |
| 7D (Agi 2 Hist 1) | 0.580 | (6D) 0.456 | −0.124 | −21.4% |
| 6D (Agi 1 Hist 1) | 0.456 | (5D, floor) 0.317 | −0.139 | −30.5% |
| **5D (floor — Agi 1, Hist 0)** | 0.317 | **(floor 5D, unchanged)** | **0** | **0%** |

**Form: uniform −1D. Impact: highly non-uniform** — sharpest at the 6D → 5D-floor edge (−30.5% relative, identical math to the faction layer's Mil 6→5 case), zero at floor. Per skill: "Goal over form. Target uniform impact, not the surface form." This is a **Lesson 2 candidate by skill discipline**.

**BUT**: the Pool floor IS the Lesson 3 safeguard against death-spiral at low pools. Removing the floor to "fix" the wound impact non-uniformity would re-introduce the small-pool collapse pattern. **Trade-off, not strict violation** — flagged as C1.

`[ASSUMPTION: per skill "Small pools are primarily architectural. Route through Lessons 3/4 (don't roll it, or clock it) or aggregate the pool" — the floor IS architectural pool-aggregation. The trade-off (Lesson 3 mitigated → Lesson 2 violated at floor) is a legitimate engineering choice. — basis: the L2 violation is only at the floor, where L3 is most needed; favoring L3 over L2 at extremes is the correct priority per the skill's own master-lesson framing.]`

### 3b · Threshold cliffs

| Cliff | Location | Status |
|---|---|---|
| Crit at net hits ≥ 4 | combat_v30 + PP-717 D3 | **Discrete trigger** on integer-valued net hits. Per skill three-category table: "Discrete accumulator — legitimately 100% linear and stepped. Equal increments are correct; multiple thresholds are intended and legible. **Exempt from Lessons 2 and 6.**" Crit is a discrete trigger, not a continuous-resource cliff. **PASS.** |
| Wound at every WI damage | §4.1 | Discrete wound counter — legitimate accumulator. **PASS.** |
| OOB at Stamina 0 → −2D | params/combat §Pool modifiers + derived_stats §4.2 | Single cliff (Stamina = 0). v27 Meta-B: "Stamina 24→25 = 4→5 rounds = outcome flip (~50pp swing)" — but the swing is in round count, emergent from action costs, not in Stamina itself. **PASS-with-flag** (teaching/UI). |
| Incapacitation at Health 0 | derived_stats §4.1 | Single boundary, well-defined, recoverable via stabilise (PP-269). **PASS.** |
| Pool floor 5 | combat_v30 §1 | Soft cliff: pool clamped at 5 from below. **By design — Lesson 3 safeguard.** PASS. |

**No stacked accidental cliffs.** Phase 3b clean.

### 3c · Role conflation

**Agility carries:** Combat Pool (statistical) + Initiative (tactical, declare-last) + Distance Establish (tactical) + Thread reactions (cross-system).

Per pp717_ners D2 Robust: "DR creates a meaningful choice: invest in Agi for initiative control and distance (full value) or for raw combat dice (diminishing). This **splits Agi's utility into two channels — tactical (raw Agi) and statistical (pool) — giving players more to think about.**" Per Lesson 1 ("split a variable only where it genuinely carries two independent jobs"): Pool DR effectively *did* the L1 split, by making the two uses of Agi mathematically distinct. **PASS** — L1 implemented via DR mechanism.

**Endurance carries:** Health pool + Stamina pool + Take-a-Breath recovery rate (`(End+Hist)×2`).

Three roles in one variable. Same question as Stab in the faction diagnostic — is this independent jobs or a single causal narrative? "Endurance = body durability" expresses through hit-soak (Health), action-economy (Stamina), and recovery (TaB). Causal chain: tough body → both takes damage well and recovers well. **Coherent narrative, not Lesson 1 violation.** Per L1 "apply minimally — over-splitting harms Elegance": leaving End as one variable preserves Elegance. **PASS.**

**STR carries:** Damage (per weapon multiplier) + Disarm Ob (gate) + Mass-mismatch (defensive penalty when Light vs Heavy).

Single causal narrative ("body power"). PASS.

**No true role conflation in combat.** Phase 3c clean.

## §5 Phase 4 — Loops

### 4a · Loop catalog

| ID | Loop | Damper | Cap |
|---|---|---|---|
| **CL1 (round timer)** | Strike → Stamina drain → action constraint → Take-a-Breath restores → continues | Take-a-Breath: `(End+Hist)×2` per use; competing with action-cost drain | OOB at 0 (−2D); duration cap = pool exhaustion |
| **CL2 (wound spiral)** | Damage → wound → −1D pool → less defense → more damage | Pool floor 5 caps wound stacking; wounds clear at session end | Health 0 = incapacitation (recoverable per ED-130 strike of dying) |
| **CL3 (action triangle)** | Higher-init sees lower-init split → counters → wins exchange → keeps initiative → sees again next round | Initiative transfers to exchange winner; tie keeps current holder; per round both players make pool-split decision | Bounded by round count + Stamina |
| **CL4 (feint chain)** | Feint commits N dice → margin reduces opponent pool next round → opponent forced to defend → can feint back | **Non-stacking** (PP-293): successive Feints reset, don't accumulate. Expires on incapacitation. Pool reduction floor 1D. | Bounded by Stamina cost per Feint |
| **CL5 (cross-scale → faction)** | Named officer killed/captured in personal combat → faction_layer §6.2 Trigger 5 → faction Stab loss | Trigger 5 three-condition gate (Mil pool ≥ 4 AND Failure AND severity) | Stab cascade handled in faction L1 |

### 4b · Damper + Cap analysis

**CL1 (Stamina round timer):** damper present (Take-a-Breath) and cap present (OOB threshold). Per v27 Throughline 5: "Stamina is the round timer." Loop bounded. **PASS.**

**CL2 (wound spiral):** damper present (Pool floor 5 caps wound stacking; wounds clear at session end) and cap present (Health 0 = incapacitation, not death). Loop bounded. **PASS.** Note: this is the loop the faction-layer Lesson-5 finding (F6) would push against — combat has the floor and clear-at-session safeguards; faction does not.

**CL3 (action triangle):** damped by per-round pool-split decision being independent each round; capped by round count. PP-717 D2 (Pool DR) further damps by limiting top-end pool advantage. **PASS.**

**CL4 (feint chain):** explicitly damped by PP-293 non-stacking + PP-293 expiration. Cap: pool reduction floor 1D. **PASS** — designed loop, well-bounded.

**CL5 (cross-scale combat→faction):** handled in faction L1. Trigger 5 gate is the per-event damper. Combat-side: no additional remediation needed.

**No undamped+unbounded loops in combat.** Phase 4 clean. Contrast with faction layer where L1 was undamped+unbounded.

## §6 Phase 5 — Intent gate

| Finding | Intent evidence | Safeguard | Adequate? | Result |
|---|---|---|---|---|
| C1 (Pool floor + wound penalty non-uniformity trade-off) | Pool floor explicitly stated as min 5 (combat_v30 §1); wound clearance at session end (§4.1) | Floor + clearance | YES (Lesson 3 safeguarded) | **deliberate + adequate → trade-off, not violation** |
| C2 (PP-717 D2 not propagated) | PP-717 ratification per pp717_ners — but propagation pending | Audit-ratification commit, propagation not done | n/a (canon drift) | **defect — canon needs to catch up** |
| C3 (OOB-floor undefined) | Neither doc explicitly states whether OOB respects floor | None — gap | n/a | **defect — canon ambiguity** |
| C4 (crit ≥ 4) | PP-717 D3 explicit; pp717_ners D3 PASS verdict | discrete-by-design | YES | **PASS** |
| C5 (Health super-linear low-End) | PP-717 D1 calibrated for high-end (End 6+) only; low-end out of scope | MW cap 3 fixed top; bottom untreated | partial | **note — low exposure mitigates** |
| C6 (STR multiplier ambiguity) | combat_integration audit flagged as "editorial open" — surfaced, not resolved | None — Jordan ruling required | n/a | **defect — canon needs ruling** |
| C7 (cross-scale L1) | faction_layer §6.2 Trigger 5 three-condition gate explicit | Gate IS the safeguard | YES | **PASS** |
| C9 (action triangle) | combat_v30 §4 + PP-294 Feint + Burning Wheel heritage explicit | Round-bound + Stamina-bound | YES | **PASS** |
| C10 (Stamina cliffs) | v27 Meta-B explicit: "the cliffs are the actual balance levers" | UI surfaces the cliffs (recommended); not a mechanics fix | YES (UI-domain) | **PASS-with-flag** |
| C11 (wound penalty universality) | PP-716 explicit unification | Cross-system smoothness | YES (S+) | **PASS** |
| C12 (TaB recovery) | derived_stats §4.2 explicit formula + design rationale | Tradeoff between pool + recovery rate | YES | **PASS** |
| C8 (5 convergent observations from handoff) | open handoff text; standing Jordan-decision | n/a — defers to handoff resolution | **OPEN TRADE-OFF** | **defers** |

## §7 Phase 6 — Triage

Findings carried to Stage 2, severity worst-first:

| # | Finding | Component | Impact | Exposure | Irreversibility | Phase | Severity |
|---|---|---|---|---|---|---|---|
| C2 | PP-717 D2 Pool DR formula not propagated to combat_v30 / params/combat | A · Pool | H | H | M | 0 | **P1 (canon defect)** |
| C6 | STR multiplier text vs example contradiction (Heavy Blunt ×3 vs Mace=6) | E · Damage | M | M | M | 0 | **P2 (canon defect)** |
| C3 | OOB vs Pool Floor 5 interaction undefined | A · Pool + H · Stamina | M | M | L | 0 | **P2 (canon gap)** |
| C5 | Health super-linear at low End (MW threshold jumps) | G · Health | M | L | L | 3a | **P2 (residual L2)** |
| C1 | Pool floor + wound penalty Lesson 2 trade-off (L3 PASS, L2 non-uniform at floor) | A · Pool + I · Wound | L | L | L | 2+3a | **note (trade-off)** |
| C4 | Crit threshold ≥ 4 cliff | E · Damage | — | — | — | 3b | **PASS** |
| C7 | Cross-scale L1 (combat → faction Trigger 5) | CL5 | — | — | — | 4 | **PASS (gated)** |
| C9 | Action triangle loop | CL3, CL4 | — | — | — | 4 | **PASS** |
| C10 | Stamina round-count cliffs | CL1 + B · split | — | — | — | 3b | **PASS-with-flag (UI)** |
| C11 | Wound penalty universality (PP-716) | I · Wound | — | — | — | meta | **PASS (S+)** |
| C12 | TaB recovery formula | CL1 | — | — | — | 3a | **PASS** |
| C8 | 5 convergent observations (handoff scope) | meta | — | — | — | meta | **OPEN TRADE-OFF (defers)** |

## §8 Stage 2 — Lesson mapping

| # | Finding | Lesson(s) | Remediation direction |
|---|---|---|---|
| C2 | Pool DR formula not propagated | (canon defect, not NERS lesson) | **Editorial ledger candidate**: ED-NEW Pool DR propagation. Update `combat_v30.md §1` and `params/combat.md §Pool Formula` to `min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3` per PP-717 D2 ratification per pp717_ners. Cite. |
| C6 | STR multiplier ambiguity | (canon defect) | **Editorial ledger candidate**: ED-NEW STR multiplier reconciliation. Jordan ruling: is Mace 6 (×1.5 implied) or 12 (×3 per formula)? Update params and worked example to match. |
| C3 | OOB-floor undefined | (canon gap) | **Editorial ledger candidate**: ED-NEW OOB vs Pool Floor 5 interaction. Two options to choose: (a) OOB respects floor (5−2 → 5, no impact at floor — extends Pool-floor safeguard to OOB), or (b) OOB ignores floor (5−2 → 3, OOB always bites). Per the design philosophy of Pool floor as Lesson 3 safeguard, (a) is the consistent choice — but Jordan-decision-owned. |
| C5 | Health super-linear at low End | L2 (base-parameter) | Direction (a, mechanical): smooth Health-per-End at low End (e.g., reduce End 1 Health from 14 → 10, End 2 from 24 → 18, smoother curve). Direction (b, documentation): document the non-uniformity as intentional brittleness for low-End builds; players choosing End 1–2 know they're at sharp disadvantage. (b) is the lower-cost fix; exposure is low. |
| C1 | Pool floor + wound non-uniform impact | (trade-off, not violation) | No remediation needed. The trade-off (L2 violated at floor in exchange for L3 working) is the right priority. Note in design doc. |
| C8 | 5 convergent observations | (handoff scope) | **OPEN TRADE-OFF — defers to handoff resolution.** If a redesign direction is selected that addresses initiative-as-state / engagement-profile / bind-distance / asymmetric-commitment / reading-opponent, the resolution-fitness verdict on this diagnostic must be re-run on the NEW chassis. Until then, the current chassis is the system under audit and the verdict stands. |

**No remediation prescribes among the 5 open directions. Per standing handoff instruction.**

## §9 Status

Stage 1 complete. Findings carried to Stage 3 verdict in `ners_verdict_combat.md`.

**Confidence calibration:**
- `[CONFIDENCE: high]` — C2 (drift verified by reading both audit and current docs), C4/C7/C9–C12 (audit-validated)
- `[CONFIDENCE: medium]` — C1, C5 (mathematical reasoning, not externally cited; probabilities computed from Binomial)
- `[CONFIDENCE: medium]` — C3 (canon gap I discovered this session — not in prior audits; possible I missed where canon resolves it; flagged for Jordan-side check)

**Files NOT deep-read this pass:**
- `combat_v30.md` beyond §5 head (weapon table read; later sections §6+ on Stunt/Stamina detail, §7+ on advanced mechanics not opened)
- `tests/audit/all_directions_ners_v27.md` beyond ~9k (Meta-Throughlines + 6-direction balance partial)
- `designs/scene/derived_stats_v30.md` §5+ (Composure/Social — covered when running Social Contest diagnostic in Turn G)
- `designs/audit/2026-05-17-scene-combat-contest/**` — intentionally not read (the open handoff's exploration work; reading it would risk influencing direction-among-5 prescription)

**Departures from skill INITIAL HYPOTHESES:**
- Skill hypothesis: "Personal combat — likely mostly compliant; watch the flat −1D wound at the 5D floor (Lesson 2 candidate)." → **confirmed as a trade-off (C1)**, not a violation. The floor is the L3 safeguard; the L2 non-uniformity is the trade-off price. **Surfaced and reframed.**
- New canon-defect findings (C2, C3) not predicted by skill — discovered via cross-checking audit vs current docs.
