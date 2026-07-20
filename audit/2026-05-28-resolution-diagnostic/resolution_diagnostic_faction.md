# Resolution Diagnostic — Faction Action Layer

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stage 1)
**Scope:** faction action layer per skill INITIAL HYPOTHESES — covers faction_layer_v30, factions_personal_v30, military_layer_v30, ci_political_v30, with cross-references to victory/peninsular_strain (L1 collapse loop) and mass_battle (Trigger 5 gate).
**Status:** Audit output. Commits blocked (B6) — staged inline.
**Session token:** c93a36df1d98ea45

## §0 Pre-flight & citations

**Files consulted this session** (per audit gate "All mechanical values must be cited with source file + section"):

- `references/canonical_sources.yaml` — full (system → doc mapping)
- `canon/02_canon_constraints.md` — full (P-01–P-15 Foundations + GD-1/2/3 game-design constraints)
- `skills/valoria-mechanic-audit/SKILL.md` — full (audit gate prereq)
- `designs/audit/2026-05-16-faction-ners-all-directions.md` — ~9k chars (§0–§2 throughlines T-1..T-6); prior content-coverage audit
- `tests/audit/all_directions_ners_v27.md` — ~9k chars; methodology precedent (weapon system, not faction prior-art)
- `designs/provincial/faction_layer_v30.md` — full + sections §1.2 Triggers, §1.3 Recovery, §1.4 Accounting Check, §1.5 Collapse, §6.2 Trigger5
- `designs/provincial/factions_personal_v30.md` — full + sections §8.1 Stats/Starting/Domain Actions, §8.11 Parliamentary Vote, §8.12 Seasonal Accounting
- `designs/provincial/military_layer_v30.md` — full + sections §1.4 Muster Output, §1.5 Prereqs, §2.1 Pool Formula, §2.2 Battle Outcome
- `designs/provincial/ci_political_v30.md` — full + sections §2 CI 0-100, §3.2–3.4 CI Bonus/Obstacle/Pool, §4.1 How Stats Change
- `params/factions.md` — full (index file)
- `params/factions/stats_1_7_scale.md` — first ~7k chars including Domain Action Rules / PP-403 / CI Passive

**NERS source:** PI `<definitions>` block (canon/definitions.yaml returns HTTP 404; tree match for 'definition': NONE). `[GAP: canon/definitions.yaml — referenced by skill Stage 3 and architecture <reference_files_pattern>, file does not exist in repo. Using PI <definitions> as authoritative project terminology per architecture <layer_ownership>.]`

**Relationship to prior audit:** `2026-05-16-faction-ners-all-directions.md` is content-coverage (does the surface model the right political dynamics? Verdict: PARTIAL — gaps A-1..A-8). This diagnostic is resolution-and-balance fitness (does it hold up at the extremes?). The two lenses are complementary; overlap is noted per finding.

## §1 Phase 0 — Resolution component decomposition

The faction action layer is a **composite**:

| Component | Mechanism | Quantity category (skill's three-category table) |
|---|---|---|
| **A · NPC Domain Action roll** | Roll relevant stat as d10 pool at TN 7 (params/factions/stats_1_7_scale.md §Domain Action Rules); player adds own stat as bonus dice if leader (factions_personal §8.1) | **Dice-resolved** (base parameter used as bare pool) |
| **B · Domain Ob** | Ob = target stat (factions_personal §8.1) OR Ob = floor(target/2)+1 (params) — **conflicting canon, see F2** | Base parameter |
| **C · Parliamentary Vote** | Best-of-3 single-roll exchanges; pool = Mandate (legitimacy) or Influence (procedural); Ob = opponent's stat (factions_personal §8.11) | Dice + **shallow clock** |
| **D · Accounting Stability Check** | Pool = Stability as d10s TN 7; Ob 1–5 by season pressure; Ob 4 floor at Stab ≤ 2 (factions_personal §8.12) | Dice + base parameter |
| **E · Stability Triggers 1–5** | Deterministic event consequences (faction_layer §1.2) | Deterministic-accounting |
| **F · Collapse Exit (Stab → 0)** | Deterministic faction-elimination procedure (faction_layer §1.5) | Deterministic-accounting + terminal |
| **G · Muster + Battle pool** | Pool = Σ Martial of engaged units + floor(Military/2) (military_layer §2.1) | Dice (aggregated, not bare) |
| **H · Trigger 5 gate** | Three-condition gate: Mil pool ≥ 4 AND Failure AND severity (faction_layer §6.2) | Deterministic gate |
| **I · CI accrual** | 0–100 milestone clock with passive +1/season + Assert/Suppress modifiers (ci_political §2.1, §3.2–3.4) | **Discrete accumulator** (legitimate multi-threshold clock; **exempt L2/L6**) |
| **J · Wealth-Zero cascade** | Wealth 0 → Mil −1/Accounting + Mil doesn't auto-recover (military_layer §1.7 / §6.2) | Deterministic-accounting + terminal-degrading |
| **K · Seasonal cap** | ±2 per stat per season from any single source (PP-242) | Damper (clamp) |
| **L · CI seasonal cap + Baralta** | ±5 CI/season cap + Hafenmark −1 CI/season structural suppression | Damper (rate + clamp) |

**Three-category classification of key quantities:**

- **Base parameters (1–7):** Legitimacy, Popular_Support, Influence, Wealth, Military, Intel, Stability — fed into dice pools when used as bare-stat-pool. Lesson 2 (uniform-impact) applies; Lesson 3 (don't roll bare on load-bearing binaries) applies.
- **Discrete accumulators (clocks):** CI 0–100, Public Instability 0–10, Mending Stability 60→0 (shared loss), Institutional Pressure 20. Lessons 2/6 exempt.
- **Continuous resources:** None at the faction layer per se (the system has no faction-scale equivalent of personal Health/Coherence/Composure). Lessons 2/6 apply to the base parameters only insofar as they're rolled as pools.

## §2 Phase 1 — Stress points

### 1a · Smallest pool by design, and after degradation

**By design** (starting Mil values, factions_personal §8.1 Starting + stats_1_7_scale §Starting Stats):

| Faction | Mil | Sta | Wealth | Notes |
|---|---|---|---|---|
| Guilds | **2** | 5 | 6 | lowest Mil baseline |
| Hafenmark | 3 | 4 | 5 | second-lowest Mil |
| Crown / Church / Varfell / RM* / Löwenritter | 4–5/6 | 4–5 | 4–5 | higher pools |

Pool floor by-design: **Mil 2** (Guilds). With leader-bonus (own Mil 2 + own Mil 2 from leader = 4D for own-faction-attacking-other), still small. NPC roll bare = **2D**.

**After degradation** — converging sources:
- Wealth 0 → Mil −1/season (military_layer §1.7) — terminal cascade, no auto-recovery
- Failed Domain Action → −1 Stab (PP-403) — feeds Trigger-5 pathways
- Active Occupation → −1 Stab/Accounting (faction_layer Trigger 1)
- Combined Embargo+Blockade → −1 Stab/season ongoing (Trigger 3)
- Treaty Capitulation → −3 Stab (Trigger 2)

A faction starting at Mil 3 (Hafenmark) under Wealth-Zero for 2 seasons → Mil 1. Pool after-degradation: **1D**.

### 1b · Exposure frequency

| Stress case | Exposure path | Likelihood |
|---|---|---|
| Guilds Mil 2 acting on a military Domain Action | starting state | **routine** (any game state where Guilds takes a military Assert/Suppress) |
| Any faction at Stab ≤ 2 rolling Accounting Stability Check | reached via any Trigger cluster | **routine** under pressure |
| Faction at Mil 1 from Wealth-0 cascade | 2 seasons of Wealth 0 (deniable via Trade, but Embargo+Blockade locks it) | **plausible** (sustained Embargo is a strategic option) |
| Faction at Mil 2 + Capital lost (T1/T8/T9/T12) | combat loss to capital → −2 Stab + territory loss penalty | **scenario** (mid-game outcome) |

`[FREQUENCY SIGNAL: design doc declares faction collapse as a "campaign dramatic possibility" (faction_layer §1.5 Crown doctrine note); but the route to collapse from Guilds Mil 2 starting state is shorter and more mechanical than the "dramatic structural fragility" language implies — i.e., the design rhetoric treats collapse as narrative beat, the mechanics treat it as small-pool dice outcome.]`

## §3 Phase 2 — What the stress point decides

### 2a · Outcome type at the floor

| Action @ floor | Outcome type | Depth |
|---|---|---|
| Assert / Suppress (Domain Action) | **Binary**: Success / Partial / Failure → −1 Stab on Failure (PP-403) | shallow (single roll) |
| Parliamentary Vote | Best-of-3 single-roll exchanges → win/loss/abstention | **shallow clock** (3 binary exchanges) |
| Accounting Stability Check | **Binary**: Pass / Fail → −1 Stab on Fail | shallow |
| Trigger 5 military engagement | Failure + severity → −1 to −2 Stab (gated by Mil pool ≥ 4) | gated, but binary inside the gate |

### 2b · Stakes & reversibility

| Outcome | Reversibility |
|---|---|
| Failed Domain Action | −1 Stab (recoverable +1/clean-season, but additional triggers stack faster than recovery) |
| Parliamentary motion loss (Censure/Outlawry) | −1 to −2 Stab, −1 to −2 Mandate (slow recovery — Govern OW once/season, max=starting) |
| Accounting Stability Failure at Stab ≤ 2 | Cascade to Stab 0 within ~2–3 seasons; **terminal** |
| Stab 0 collapse exit (§1.5) | **Irreversible** — faction eliminated |
| Wealth 0 Mil-degradation | Wealth recovery does NOT restore Mil — **military stat permanently degraded** until re-mustered (which itself requires Wealth) |

### 2c · Risk profile (worst stress cases)

| Scenario | Impact | Exposure | Irreversibility |
|---|---|---|---|
| Guilds Mil 2 vs neutral target on Assert (pool 2D vs Ob 3–4) | H | H (routine) | M (DA cost −1 Stab on Failure) |
| Any faction at Stab 2, Accounting Ob 4 (floor) | H | H (any stress) | **H** (cascade to collapse if it fires) |
| Mil-2 faction in Wealth-0 → Mil 1 after 1 season | H | M | **H** (Mil doesn't auto-recover) |
| Capital lost → −2 Stab + Trigger 1 ongoing | H | M (mid-game) | **H** (capital recapture rarely simple) |

**Triple-H findings:** 2 (anti-death-spiral floor scenarios; capital-loss cascade). The Guilds-floor scenario is H/H/M but elevated via Trigger pathway to H/H/H over 1–2 seasons.

## §4 Phase 3 — Effect-curve checks

### 3a · Impact uniformity (dice + base-parameter components)

**Stat damage is absolute** (−1 Mil/Sta/etc. per Trigger). Probability impact at TN 7:

Each d10 ≥ 7 has p = 0.4. P(≥k successes | n dice) ≈ Binomial(n, 0.4) ≥ k.

| Mil | Pool | Mean successes | P(≥3 hits) | Δ from −1 |
|---|---|---|---|---|
| 6 | 6D | 2.4 | 0.456 | (5D) 0.317 → Δ −0.139 abs / −30.5% rel |
| 4 | 4D | 1.6 | 0.179 | (3D) 0.064 → Δ −0.115 abs / **−64% rel** |
| 2 | 2D | 0.8 | 0.000 | (1D) 0.000 → Δ 0 (already floor) |

**Non-uniform impact across scale.** A −1 stat damage is much sharper at mid-pool than at high-pool, and meaningless at the 2D floor (P=0 either way). Per skill Lesson 2 ("Continuous resources and base parameters take uniform-*impact* steps") — **violation**.

### 3b · Threshold cliffs

| Cliff | Location | Stacking risk |
|---|---|---|
| Stab → 0 (collapse) | faction_layer §1.5 | single boundary — but feeds L1 loop |
| Wealth → 0 (Mil −1/season) | military_layer §1.7 | single boundary — but feeds J cascade |
| Mil pool ≥ 4 gate (Trigger 5) | faction_layer §6.2 | gate, not cliff (intended) |
| CI milestones 40/55/65/80/100 | ci_political §2.1 | **legitimate clock thresholds** — discrete accumulator, exempt L6 |
| Public Instability ≥ 8 (revolt risk) | factions_personal §8.1 | single boundary; cascade brake (PP-281) present |
| Anti-death-spiral floor at Stab ≤ 2 | factions_personal §8.12 | **safeguard that doesn't save** — see F3 |

**No accidental cliff-stacking at a single point.** The cliffs that exist are mostly intended and segmented across systems. The intended CI milestones are exempt per the discrete-accumulator rule. **Phase 3b: clean.**

### 3c · Role conflation

**Stability** carries: faction-cohesion state (the value itself) + Accounting-check pool basis + collapse-trigger threshold. Three apparent roles.

**Assessment:** the three roles form a **single causal narrative** (cohesion → resistance under check → collapse if check fails repeatedly). Per Lesson 1: "Split a variable only where it genuinely carries two independent jobs. *(Apply minimally — over-splitting harms Elegance.)*" These are not independent jobs; they're sequential expressions of one variable's meaning. **NOT a Lesson 1 violation.** *(Departs from skill worked-example.)*

**Wealth** carries: economic-capacity state + muster-funding gate + mercenary-upkeep cost. Similar narrative chain. Same call — not a true conflation.

`[ASSUMPTION: skill worked-example's "Stability carries both 'political health' and 'collapse trigger' — role conflation candidate" was a flag for confirmation, not a verdict. On close read against §1.5 + §8.12, the chain is coherent. — basis: Lesson 1's own "apply minimally" constraint; an independent reviewer would catch over-splitting as harming Elegance.]`

## §5 Phase 4 — Loops

### 4a · Loop catalog (cross-system)

| ID | Loop | Damper present? | Cap present? |
|---|---|---|---|
| **L1** | Stab → territory loss → muster reduced → Mil engagement failure → Trigger 5 → Stab loss → collapse | §1.3 Recovery (+1/clean season, seasonal cap ±2) — **weak vs. ≥2 trigger stacks** | **Stab=0 is termination, not a bound** |
| **L2** | Mass-battle defeat → Trigger 5 (gated at pool ≥4) → Stab loss → muster capacity | Trigger 5 gate (only fires above pool 4 — protects skirmishes); §1.3 recovery | Stab=0 termination |
| **L3 (CI)** | CI accrual → +floor(CI/20) Church bonus dice → easier Parliamentary win → Mass Seizure milestone @ CI60 → territory → CI gain | CI seasonal cap ±5, Baralta −1/season, CI 100 ceiling | **CI 100 max** — bounded |
| **L4** | Conviction/Coherence knot propagation (P-12 personal-scale) | n/a faction-layer; tracked at threadwork | — |
| **L5** | Peninsular_strain / Turmoil ↔ victory gating (Pol-Stability ≤ 6) | Turmoil Mandate check, strain table | victory threshold = boundary |
| **L6** | Territorial neglect → Insurgency (GD-3) → promoted faction → invades parent | L≥3, 2+ territories, Accord ≥4 thresholds; season-counts | promotion gate |
| **L7 (new)** | Wealth 0 → Mil −1/Accounting → can't muster → can't recover Mil from Wealth recovery | damped on Wealth dimension (Trade restores Wealth); **undamped on Military dimension** (Mil doesn't auto-recover) | Mil 1 floor (effectively non-functional) |

### 4b · Damper + Cap analysis

**L1 (skill priority loop):** damper exists, weak. Recovery rate +1/clean-season requires "no hostile Domain Actions targeted any faction's Stability that season" (PP-281 framing applied to PI; analogous for §1.3). In a contested mid-game, "clean seasons" are unusual. Trigger rate routinely produces 1–3 Stab losses per season vs. recovery rate +1 (and only if conditions hold). **Net rate negative.** Cap: Stab=0 terminates rather than bounds. **Loop is damped + unbounded → Lesson 5 candidate.**

**L7:** damper is decoupled — Wealth recovery doesn't restore Military. The "Mil 1 floor" exists but is functionally non-operative (can't conduct meaningful military action). **Loop is undamped (on the degrading dimension) + bounded-to-uselessness → Lesson 5 candidate.**

**L3 (CI):** Damped (±5/season cap + Baralta −1/season) + bounded (CI 100). The +5 inward / −1 Baralta = net +4 trajectory cap; over ~25 seasons CI can drift 0→100, but is realistically blocked by opposing Suppress actions and Wealth/action-slot costs. **Loop OK.**

**L6 (GD-3 insurgency):** Gated and season-counted. Intentional emergent-faction engine. **Loop intentional.**

**Cross-system observation:** L1 and L7 share an undamped-amplification pattern — a degrading stat (Mil or Stab) feeds further degradation through deterministic accounting before any roll can be made. Both are at the highest severity tier.

## §6 Phase 5 — Intent gate

| Finding | Intent evidence | Safeguard present | Adequate? | Result |
|---|---|---|---|---|
| F1 (bare-stat pool on pivotal DA) | None in design docs declaring "faction actions intentionally roll bare stats at high stakes." Inheritance from TTRPG-era design pre-videogame-pivot. | None | n/a | **`[INTENT UNDETERMINED]` → true finding** |
| F3 (anti-death-spiral floor) | factions_personal §8.12: "Prevents immediate cascade; gives players a window to intervene." | Yes (Ob 4 cap at Stab ≤ 2) | **[SUPERSEDED-BY ED-867 / F2-ruling]** — under the erroneous "Ob capped at 4" reading the floor looked inactive (P≈0.01); under **canonical Ob = floor(stat/2)+1** the Stab-2 check is 2D vs Ob 2 = **~0.26**, i.e. FUNCTIONAL. | **F3 effectively CLOSED post-F2-ruling; confirm Accounting Check uses floor(stat/2)+1** |
| F4 (non-uniform stat damage) | None — absolute-form is convention, not stated intent | None | n/a | **true finding** |
| F5 (decrease > increase asymmetry) | Implicit in trigger surface vs. recovery sparseness; no design doc states "decline should outrun recovery as default." | §1.3 Recovery, Institutional consolidation note | **NO — recovery rate too low vs. trigger rate** | **true finding** |
| F6 (L1 collapse loop terminal-irreversible) | Yes — faction_layer §1.5 ED-675 explicitly canonicalizes the collapse procedure; GD-3 RM-emergence requires collapse pathways for territorial freeing. | §1.3 recovery; Trigger 5 gate; anti-death-spiral floor | **YES (collapse exists)** but **NO (speed-from-mid-game-to-extinction unbounded)** | **deliberate (existence) + inadequate (rate) → true finding** |
| F7 (Wealth-0 Mil-cascade) | military_layer §6.2: "makes sustained Blockade + Embargo an existential threat to Guilds and Hafenmark (Wealth-primary factions)." **Intent is stated.** | Wealth recovery via Trade | **YES on Wealth dimension; NO on Military dimension (decoupled)** | **deliberate + safeguard inadequate (on Military) → true finding** |
| F9 (shallow Parliamentary clock) | Best-of-3 IS Lesson 4 routing attempted. | The clock itself | **partially — provides some averaging but not enough for P=0 floors** | **deliberate + execution-shallow → true finding** |
| F11 (CI political amp) | ci_political §3.2: "by design. A Church operating at CI 80 is historically comparable to the papacy of Julius II..." | Seasonal cap ±5, Baralta −1, CI 100 ceiling | **YES** | **deliberate + adequate → PASS** |
| F12 (GD-3 RM emergence) | canon/02_canon_constraints.md GD-3, fully spec'd | L threshold, season-counts, parliamentary-status flag | **YES** | **PASS** |

## §7 Phase 6 — Triage

Findings carried to Stage 2, severity worst-first:

| # | Finding | Component | Impact | Exposure | Irreversibility | Phase | Severity |
|---|---|---|---|---|---|---|---|
| F1 | Bare-stat pool on pivotal/irreversible Domain Actions | A · NPC DA roll | H | H | M | 1+2 | **P1** |
| F3 | Anti-death-spiral floor non-functional | D · Accounting Check | H | H | H | 5 | **P1** |
| F6 | L1 collapse loop unbounded (Stab=0 terminal, damper weak) | E·F·G·K | H | H | H | 4 | **P1** |
| F7 | L7 Wealth-0 → Military undamped on Mil dimension | J · Wealth-Zero cascade | H | M | H | 4 | **P1** |
| F5 | Decrease > increase asymmetry feeds L1 | E · Triggers + K · Cap | H | H | M | 4 | **P1** |
| F2 | Conflicting canonical Ob formulas | B · Domain Ob | H | H | M | 0 | **P1 (canon defect)** |
| F8 | PP-686 v2 stat-schema drift in design doc | A·B | H | M | M | 0 | **P1 (canon defect)** |
| F4 | Absolute stat damage non-uniform impact | A · DA roll | M | H | L | 3a | **P2** |
| F9 | Best-of-3 Parliamentary clock too shallow | C · Vote | M | M | M | 2 | **P2** |
| F10 | Stab triple-role (not a true conflation — surfaced for note) | E · Triggers | L | L | L | 3c | **note** |
| F11 | CI political amplification (PASS) | I · CI accrual | — | — | — | 4 | — |
| F12 | GD-3 RM emergence (PASS) | L6 | — | — | — | 4/5 | — |

## §8 Stage 2 — Lesson mapping

| # | Finding | Lesson(s) | Remediation direction |
|---|---|---|---|
| F1 | Bare-stat pool on pivotal DA | **L3 (master)** — keep dice off small-pool / load-bearing / binary decisions | Route consequence through deterministic accounting OR aggregate pool when roll is needed (e.g., factor leader stat into NPC pools the way player factions get it; add per-action Composure-style continuous resource that absorbs roll variance) |
| F3 | Anti-death-spiral floor non-functional | **L3 + L4** | Make the floor active: either (a) replace Ob 4 cap with a deterministic "Stab ≤ 2 → no Accounting check fires; cumulative pressure ticks a recovery-clock instead" — route through clock per L4; OR (b) cap the floor by pool-augmentation (e.g., "Stab ≤ 2 → roll Stab + 2 bonus dice") so the pool can actually meet the Ob |
| F6 | L1 collapse loop unbounded | **L5** — bound the loop short of extinction, or strengthen recovery rate | Options: (a) add Stab=1 as a hard floor that cannot tick to 0 except by Trigger 5 or specific narrative-flagged events (not by Accounting drift); (b) raise recovery rate at low Stab (e.g., +2/clean-season at Stab ≤ 3); (c) introduce a recovery-from-collapse path (RM-pipeline-style: collapsed faction can emerge as Restoration variant — this is partially what GD-3 already does, formalize as an explicit damper) |
| F7 | L7 Wealth-0 Mil undamped | **L5** — couple the damper to the degrading dimension | Make Wealth recovery restore some Military (e.g., +1 Mil per 2 seasons of Wealth ≥ 1, capped at original) so the loop has a damper on the dimension that's actually degrading |
| F5 | Decrease > increase asymmetry | **L5** | Either reduce trigger-rate at low Stab (composes with F3 floor fix) or add a recovery-source per faction (currently only Church Absolution and Löwenritter endorsement provide +1 to other factions — broaden the surface so non-Church factions can recover without external faction help) |
| F2 | Conflicting Ob formulas | (canon defect — not a NERS lesson) | **Editorial ledger candidate**: ED-NEW Domain Ob formula reconciliation. Decide between `floor(stat/2)+1` (params) and `stat directly` (design doc §8.1). Cite ratification. Update both docs to match. |
| F8 | PP-686 v2 / ED-787 stat-schema drift | (canon defect) | **Editorial ledger candidate**: ED-NEW factions_personal_v30 §8.1 stat-table refresh to 7-stat L+PS+Intel per PP-686 v2 + ED-787. Add `[SUPERSEDED 2026-05-01 PP-686 v2]` marker on the old 6-stat table per supersession discipline. |
| F4 | Absolute stat damage non-uniform | **L2** — uniform-impact steps for base parameters | Option (a): convert stat-damage events to *proportional* damage when stat is being rolled (e.g., −20% of pool, floor 1). Option (b): leave absolute, but document the asymmetry as intentional and add a Phase 5 intent statement justifying it (e.g., "low-Mil factions are *meant* to be sharply punished per stat loss to model brittleness"). Note (b) is a documentation fix, not a mechanical fix. |
| F9 | Best-of-3 clock too shallow | **L4** — deepen the clock | Move to best-of-5 OR accumulator-based (Vote Track 0–10, +1 per won exchange, threshold @ 6 wins motion) so averaging reduces small-pool variance enough to give 2D pools a non-zero chance |
| F10 | (note, no lesson) | — | — |

## §9 Status

Stage 1 complete. Findings carried to Stage 3 verdict in `ners_verdict_faction.md`.

**Departures from skill worked example:**
1. F10 — Stab "role conflation" downgraded to not-a-finding (single causal narrative).
2. F7 — Wealth-0 cascade added as a new loop (L7) not in skill catalog.
3. F2/F8 — canon defects (conflicting Ob formulas; PP-686 v2 drift) surfaced as resolution-blocking finds beyond NERS scope.

**Open questions for Jordan:**
- F2: which Ob formula is canonical — `floor(stat/2)+1` (params) or `stat directly` (design doc §8.1)?
- F8: should factions_personal_v30 §8.1 be updated to 7-stat per PP-686 v2 + ED-787, or has §8.1 been deliberately left at the 6-stat predecessor for a reason?
- F6/F10 disagreement with skill worked example: confirm or correct.
