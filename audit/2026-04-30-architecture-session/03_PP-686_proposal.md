<!-- [PROVISIONAL: 2026-04-30 — PP-686 draft, faction behavior architecture] -->
<!-- STATUS: PROVISIONAL — design proposal, not canonical mechanic -->
<!-- TITLE: PP-686 — Faction Behavior Architecture: Mission, Cascade, Public Expectation, Legitimacy, Popular Support -->
<!-- AUTHORITY: drafted under PP-674 vetting framework. Class A new subsystem. -->

# PP-686 — Faction Behavior Architecture

**Status:** PROVISIONAL — proposal pending Jordan review.
**Class:** A (new subsystem replacing/superseding existing Ethical Framework Modifiers and Mandate-as-single-scalar).
**Supersedes:** `params/bg/core.md` §Ethical Framework Modifiers; partial supersession of Mandate scalar.
**Depends on:** PP-684 Conviction taxonomy revision (10-12 Convictions); PP-685 Conviction migration roster.
**Co-files:** `designs/provincial/faction_behavior_v30.md` (new); updates to `params/bg/core.md`, `params/factions.md`, `params/factions_personal.md`, `params/bg/tracks.md`, `references/glossary.md`, `references/alias_registry.yaml`.

---

## §0 Abstract

Faction behavior is currently determined by a single authored scalar (Mandate, 1-7) and a set of philosophical-tradition-labeled Ethical Framework Modifiers that produce ±1/±2 Ob adjustments on Domain Actions. This proposal replaces both with a four-piece architecture:

1. **Mission** — what the faction is trying to accomplish (telos, authored, evolves)
2. **Cascade** — how the faction conducts itself (modus, derived from leadership Convictions through hierarchical α-weighted blending)
3. **Public Expectation** — what the populace expects from the faction's role (Conviction-shaped, derived from role + Mission consistency)
4. **Legitimacy + Popular Support** — populace acceptance and active backing (separately tracked, modulating Public Expectation strictness)

Domain Action Ob is computed from action alignment with all four. Mandate becomes a derived value during transition, retired when consumers refactor.

The architecture eliminates the philosophical-tradition vocabulary problem (Categorical Imperative, Rawlsian, etc., are anachronistic for the Renaissance period), unifies vocabulary across personal and faction scales (same Conviction labels at both), and produces dynamic faction behavior from a small authored input set (Mission + leader + tier α-weights + role) rather than per-faction static authored tables.

## §1 Motivation

The current system has four problems:

**1.1 Vocabulary clash.** Ethical Frameworks use philosophical-tradition labels (Virtue Ethics, Divine Command, Categorical Imperative, Epistemic Reason, Rawlsian, Military Honor) — meta-ethical schools imported from 18th-21st century philosophy. NPC Convictions use historical-institutional labels (Faith, Order, etc.). The two registers fight for the same semantic slot ("ethics") at different scales without sharing vocabulary.

**1.2 Static modus.** A faction's "ethical framework" is authored and constant. In historical reality, the Tudor court behaved differently under Henry vs Elizabeth not because the institution's ethics changed but because the cascade from leadership shifted. The current system cannot represent this without re-authoring the framework on every leadership change.

**1.3 Mandate conflation.** A single 1-7 scalar collapses three distinct populace relationships: acceptance of right-to-act (Legitimacy), active desire-for-success (Popular Support), and expectation of role-appropriate conduct (Public Expectation). Existing consumers of Mandate are using it for different things — Church Excommunication Ob (Legitimacy), Hafenmark Parliamentary Sovereignty victory (Legitimacy + Popular Support combined), AER advancement (Legitimacy). The conflation is invisible to the player and unprincipled mechanically.

**1.4 No authored expression of role-expectation.** The expectation that "the Crown should act virtuously *because* it leads the country" is not currently representable. Public Expectation is implicit in the Ob modifiers but not surfaced as state. A Crown that acts un-virtuously and a Crown that acts virtuously through different means produce different mechanical results, but the *populace's expectation* — the modulator that makes either choice consequential — is not modeled.

## §2 Design Goals

| Goal | Means |
|---|---|
| Unify vocabulary across personal and faction scales | Convictions are the same labels at both scales |
| Replace anachronistic vocabulary with period-correct equivalents | Mission (telos) and Cascade (modus) instead of Ethical Framework |
| Derive faction modus dynamically from leadership | Cascade math: leader Convictions → tier α-blends → ground-level effective Convictions |
| Separate populace acceptance from populace backing | Legitimacy and Popular Support as independent scalars |
| Produce role-expectation as explicit mechanical state | Public Expectation derived from role + Mission, modulated by Legitimacy + Popular Support |
| Preserve compatibility with existing Mandate-consuming mechanics | Transitional Mandate as derived f(Legitimacy, Popular Support); refactor consumers opportunistically |
| Allow dynamic faction evolution | Mission can shift on major state change; Cascade re-resolves on succession; Legitimacy / Popular Support move continuously |
| Compose with proposed Conviction taxonomy revision | All Conviction references read from the same authoritative taxonomy |

---

## §3 Specification

### §3.1 Mission

A faction has one **Mission**: a short statement of telos.

```yaml
faction.mission:
  text: "Consolidate sovereign authority over Valoria"
  primary_objective: "expand_PV"          # links to victory-condition or DA-category
  beneficiary: "crown_aligned_populace"   # who counts as Mission-served
  authored_at: 2026-XX-XX
  prior_mission: null  # populated on Mission shift
```

**Mission shift.** Mission may shift on major state change (loss/gain of victory-track milestone, leader replacement under exceptional circumstances, mission_failure_threshold reached). Authored: at engine start, then per shift event.

**Mission alignment evaluation per DA:**

```
mission_alignment(da, mission):
  if da.category in mission.aligned_categories:
    return -1  # bonus Ob
  if da.category in mission.contradicted_categories:
    return +1
  return 0
```

`aligned_categories` and `contradicted_categories` are authored as part of the Mission spec.

### §3.2 Cascade

Each NPC has two Conviction states:

- **personal_convictions**: weights across the canonical Conviction set; what the NPC personally believes (set per character creation, drift via Conviction Scars)
- **effective_convictions**: weights actually expressed in faction-role behavior; derived

Cascade computation:

```
effective_convictions(npc) =
    α(npc) × personal_convictions(npc)
  + (1 - α(npc)) × effective_convictions(supervisor(npc))
```

where:

- `supervisor(npc)` = the NPC's direct organizational superior; for the leader of a faction, supervisor is null and the cascade root is `effective_convictions(leader) = personal_convictions(leader)`.
- `α(npc) ∈ [0, 1]` = autonomy coefficient. Senior NPCs have higher α (more independent expression); junior NPCs have lower α (more deferent).

**Setting α.** Three contributions:

```
α(npc) = clamp(
    α_base
  + α_seniority(npc.standing)
  + α_institution(faction.institutional_culture)
  , 0, 1)
```

| Component | Range | Notes |
|---|---|---|
| `α_base` | 0.4 | Default starting point |
| `α_seniority` | -0.2 to +0.4 | Standing 1: -0.2; Standing 7: +0.4. Senior NPCs more independent |
| `α_institution` | -0.2 to +0.2 | Hafenmark = -0.2 (rigid procedural cascade); Crown = 0; Restoration = +0.1 (looser, principles-driven); Löwenritter = -0.1 (military discipline) |

**Cascade re-resolution.** Effective Convictions recompute at each Accounting (season boundary). A leader change triggers an immediate re-resolution. Effective Convictions damp toward the new equilibrium over 1-2 seasons rather than snapping (per-NPC drift parameter; default 0.3 toward new value per season).

**Cascade visibility.** A faction's *organizational cascade map* is queryable in UI: "show me where leader's Authority gets diluted to Order at Tier 2 because Captain Almud has personal Order Conviction." This is a debugging/strategy aid; only top-level effective_convictions distribution surfaces by default.

### §3.3 Public Expectation

Each faction has an **expected Conviction profile** derived from role:

```
expected_convictions(faction) = role_template(faction.role)
```

Authored once per role-type, not per faction:

| Role | Expected Convictions (weighted distribution) |
|---|---|
| sovereign | Virtue: 0.4, Authority: 0.4, Honor: 0.2 |
| ecclesiastical | Faith: 0.5, Authority: 0.3, Scholastic: 0.2 |
| mercantile-procedural | Order: 0.4, Utility: 0.3, Scholastic: 0.3 |
| intelligence-diplomatic | Scholastic: 0.4, Utility: 0.4, Authority: 0.2 |
| reformist | Equity: 0.4, Liberty: 0.3, Community: 0.3 |
| military-order | Honor: 0.4, Authority: 0.3, Virtue: 0.3 |

**Public Expectation = expected Convictions + Mission consistency check.** A faction whose stated Mission contradicts its role's expected Convictions reads as "incoherent" to the populace and pays a Legitimacy cost (see §3.5).

**Cascade Fidelity** (used by §3.4):

```
cascade_fidelity(faction) = cosine_similarity(
    aggregate_effective_convictions(faction),
    expected_convictions(faction.role)
)
```

Range [-1, 1]. 1 = perfect role fidelity; 0 = orthogonal; -1 = inverse (rare; means the faction is acting opposite to its kind).

### §3.4 Popular Support

A scalar [0, 7] tracking active populace backing. Updates per Accounting:

```
ΔPopular_Support per season =
    α_temperament × mission_outcome_for_public(faction)
  + β_temperament × cascade_fidelity(faction)
  + γ × (random shock; events)
```

where:

- `mission_outcome_for_public(faction)` ∈ [-1, +1]: +1 if mission-aligned DA succeeded with measurable benefit to faction.beneficiary; -1 if action harmed beneficiary; 0 if neutral
- `cascade_fidelity(faction)` ∈ [-1, +1]: as defined §3.3
- `α_temperament`, `β_temperament` ∈ [0, 1] with `α + β = 1`: relative weight populace places on outcomes vs conduct
- `γ`: scaling for major events (see §3.6)

**Public temperament** is authored per-territory, not per-faction. It captures whether the local populace prioritizes results (high α) or proper conduct (high β):

| Public temperament | α (outcomes) | β (conduct) | Period example |
|---|---|---|---|
| pragmatic | 0.7 | 0.3 | Florentine merchant class |
| traditional | 0.3 | 0.7 | rural devout populace |
| balanced | 0.5 | 0.5 | mixed urban populace |
| principled | 0.2 | 0.8 | reformist enclaves |
| outcomes-only | 0.9 | 0.1 | hardship populations under direct threat |

A faction's effective temperament weight is the population-weighted average of its territories' publics.

**Initial value.** Popular Support starts at the value derived from current Mandate at engine init: `Popular_Support_init = Mandate × 1.0` (preserves continuity for existing scenarios). After first season, dynamics replace static value.

### §3.5 Legitimacy

A scalar [0, 7] tracking populace acceptance of the faction's right to act. Slower-moving than Popular Support; integrates over many seasons.

```
ΔLegitimacy per season =
    +λ_continuity × seasons_in_role_uninterrupted
  + λ_procedural × procedural_event_score(faction, this_season)
  + λ_expectation × cascade_fidelity(faction)         # slow integration
  - λ_violation × violation_event_score(faction, this_season)
```

with `λ_continuity ≪ λ_procedural ≪ λ_violation` (small per-season gains, large per-event events).

**Procedural events** (build Legitimacy):
- successful succession or coronation
- ratified treaty
- legitimate election or appointment
- religious sanction (relevant to ecclesiastical faction)
- formal acknowledgement by foreign power

**Violation events** (erode Legitimacy):
- exposed covert action contradicting Mission or role expectation
- coup or contested succession
- excommunication / heresy declaration / similar disqualifying event
- public failure of role-defining obligation (Crown unable to defend; Church visibly schismatic; etc.)
- broken oath or treaty witnessed publicly

**Initial value.** Legitimacy starts at the value derived from current Mandate at engine init: `Legitimacy_init = Mandate × 1.0`. Like Popular Support, replaces the seed value after first season.

**Mandate (transitional).**

```
Mandate(faction) = round(0.5 × Legitimacy + 0.5 × Popular_Support)
```

Mandate remains queryable for backward compatibility. Existing consumers (Church Excommunication Ob, AER advancement, victory conditions, etc.) continue to function. Refactoring of consumers to read directly from Legitimacy or Popular Support is a separate, opportunistic task.

### §3.6 Public Expectation strictness

Public Expectation is the Conviction-profile from §3.3. *Strictness* is the modulator that determines how much deviation costs:

```
strictness(faction) = clamp(
    base_strictness
  + 0.5 × Legitimacy
  - 0.3 × Popular_Support
  , 0, 1)
```

Interpretation:

| Legitimacy | Popular Support | Strictness | Effect |
|---|---|---|---|
| high | high | 0.4 | strong but elastic — populace gives benefit of doubt |
| high | low | 0.7 | strong and brittle — violations stick |
| low | high | 0.2 | weak — faction operating outside institutional acceptance, less to lose |
| low | low | 0.4 | weak again — faction in collapse zone, expectation moot |

This non-monotonicity captures the Renaissance reality: factions with secure standing and active backing can act unconventionally without consequence; factions with secure standing but no enthusiasm are punished severely for any deviation; populist factions are *expected* to be unconventional and pay less for it.

### §3.7 Domain Action Ob calculation

Per DA submission:

```
Ob_modifier(da, faction) =
    mission_alignment_modifier(da, faction.mission)               # ±1
  + cascade_alignment_modifier(da, faction.aggregate_effective_convictions)  # ±1
  + expectation_alignment_modifier(da, faction)                    # ± strictness × {1, 2}

# Final clamp
Ob_modifier = clamp(Ob_modifier, -3, +3)
```

Examples:

| DA scenario | Mission | Cascade | Expectation × strictness | Total |
|---|---|---|---|---|
| Crown public ceremony aligned with Virtue | -1 | -1 | -1 × 0.4 = -0.4 → -1 | -3 |
| Crown covert betrayal aligned with Mission | -1 | 0 | +1 × 0.4 = +0.4 → +1 | 0 |
| Restoration radical reform aligned with all | -1 | -1 | -1 × 0.2 = -0.2 → 0 | -2 |
| Hafenmark ad-hoc emergency intervention | 0 | +1 | +1 × 0.7 = +0.7 → +1 | +2 |
| Church reform aligned with new Mission, contradicting old role expectation | -1 | 0 | +1 × 0.4 = +0.4 → +1 | 0 |

Modifier function rounds .4 and below to ±1 thresholds; ≥.5 rounds to ±1; ≥1.5 rounds to ±2.

### §3.8 Faction state summary

```yaml
faction:
  # Authored
  id: crown
  role: sovereign
  mission:
    text: "..."
    primary_objective: "..."
    beneficiary: "..."
    aligned_categories: [...]
    contradicted_categories: [...]
  leader: npc_almud
  organizational_hierarchy: [...]   # tier graph
  institutional_culture: 0          # α_institution adjustment
  
  # Stateful
  legitimacy: 5                     # 0-7 scalar; slow drift
  popular_support: 4                # 0-7 scalar; faster drift
  
  # Derived (recomputed each Accounting)
  aggregate_effective_convictions: {...}
  cascade_fidelity: 0.73
  expected_convictions: {...}        # from role_template
  strictness: 0.4
  mandate: 5                         # transitional, derived
```

---

## §4 Migration Plan

### §4.1 Required prior work

- **PP-684** (Conviction taxonomy revision to 10-12 entries) — must be ratified first
- **PP-685** (Conviction migration roster — assign existing Reason/Continuity-tagged characters to new taxonomy)

### §4.2 Implementation sequence

| Stage | Task | Effort |
|---|---|---|
| 1 | New canonical doc: `designs/provincial/faction_behavior_v30.md` codifying §3 above | 1 session |
| 2 | Rewrite `params/bg/core.md` §Ethical Framework Modifiers as new triadic Ob calculation | 0.5 |
| 3 | Update `params/factions.md`, `params/factions_personal.md` faction-stat schema to add Legitimacy + Popular Support fields; deprecate Ethical Framework field | 0.5 |
| 4 | Update `params/bg/tracks.md` Mandate definition to derived | 0.2 |
| 5 | Author Mission + organizational_hierarchy + institutional_culture for all 6 factions | 1 |
| 6 | Author public temperament for all territories | 0.5 |
| 7 | Update `references/glossary.md`: deprecate Ethical Framework; canonize Mission, Cascade, Public Expectation, Legitimacy, Popular Support, Cascade Fidelity, Strictness | 0.3 |
| 8 | `references/alias_registry.yaml`: Ethical Framework → Mission + Cascade alias note; Mandate retains canonical status (transitional) | 0.2 |
| 9 | `references/canonical_sources.yaml` updates | 0.2 |
| 10 | Sim verification: compare new Ob calculation against current Ethical Framework Modifier outputs for sample DA set; verify no spurious regressions | 1 |
| 11 | Mandate-consumer audit: list all reads of Mandate; classify each as "Legitimacy", "Popular Support", or "both"; flag candidates for opportunistic refactor | 0.5 |
| **Total** | | ~6 sessions |

### §4.3 Backward compatibility

- Mandate continues to work; all existing victory conditions, Ob calculations, AER mechanics preserved.
- Ethical Framework Modifiers table is replaced; behavior emerges from the triadic calculation. Sim verification (Stage 10) confirms parity for current DA library.
- Existing faction-stat scenarios receive auto-derived initial Legitimacy and Popular Support from current Mandate values.

### §4.4 Deprecation

`canon/supersession_register.yaml` entry:

```yaml
- id: SUPERSESSION-PP686-001
  superseded: "params/bg/core.md §Ethical Framework Modifiers"
  superseder: "designs/provincial/faction_behavior_v30.md §3.7 Domain Action Ob calculation"
  date: 2026-XX-XX
  reason: "Philosophical-tradition vocabulary replaced with period-correct triadic decomposition"
```

---


## §5 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-β, Μ-δ]
  m_ratings:
    M-1: "+"   # extends — Public Expectation introduces a new continuous-pressure source
    M-2: "○"   # geographic neutral
    M-3: "✓"   # substrate consistent — factions act through and on substrate
    M-4: "+"   # extends — institutional substrate-postures become dynamically expressed via Cascade
    M-5: "+"   # extends — adds personal↔faction scale-bridge through Cascade
    M-6: "+"   # extends — new feedback loop between leader Convictions and faction modus
    M-7: "✓"   # consistent
    M-8: "✓"   # consistent
    M-9: "+"   # extends — Mission shift creates new state-evolution dynamic
    M-10: "✓"
    M-11: "+"  # extends — Public Expectation creates new external-modulator pattern
  q: pass
```

### N — Necessity (full justification)

Renaissance political theory is centrally about exactly this triad: what an institution is *for* (Mission, *finis*), how its members actually conduct themselves (Cascade, *mores*), and what the populace expects/accepts (Legitimacy + Popular Support + Public Expectation, the medieval-Renaissance theology of *fides*, *consensus gentium*, and *populus libertas*).

Subject-matter grounding (load-bearing in source material):

- **Florentine governance theory:** Bruni, Salutati, and Machiavelli all treat the same triad — *finis* (Mission), *consuetudo* (Cascade), *opinio* (Public Expectation/Legitimacy). The *Discorsi* explicitly frames political stability as the alignment between these three.
- **Tudor dynastic transitions:** Henry VIII → Edward VI → Mary I → Elizabeth I shows precisely the leader-cascade dynamic. The Privy Council's effective behavior shifted on each succession not because formal institutions changed but because the cascade root changed. This is canonically what historians document.
- **Papal Schism (1378-1417):** legitimacy and popular support diverging — the rival popes maintained strong followings (high Popular Support) while contested Legitimacy collapsed. The Council of Constance resolved the Legitimacy crisis without resolving Popular Support; the resolution mechanism is exactly what §3.5 models.
- **Venetian Republic continuity:** very high Legitimacy from procedural correctness (the Maggior Consiglio's elaborate election rituals) maintained the state's authority across many leaders despite occasional low Popular Support; this is the "principled" public temperament archetype.
- **Cesare Borgia case study:** rapid expansion via consequentialist Mission delivery (high Mission alignment) coupled with anti-role conduct (low Cascade Fidelity to Sovereign-role Honor expectation). The Florentine perspective: high Popular Support from results, contested Legitimacy. Per Machiavelli (*Il Principe* ch. 7): exactly the strong-but-fragile pattern §3.5 produces.

Existing-mechanic coverage check: Mandate alone collapses Legitimacy and Popular Support; existing Ethical Framework Modifiers static and anachronistic. Cascade dynamic from leadership is unrepresentable. The proposal captures dynamics current canon cannot.

Failure-mode check:
- *Fantasy imposition:* No. Directly grounded in repeatable historical patterns.
- *Duplicate coverage:* No. Mandate + Ethical Framework do partial work; this systematizes and extends.
- *Edge case:* No. Faction behavior is the central political-strategic mechanic.
- *Abstractable:* Partial. Could collapse Legitimacy + Popular Support back into Mandate, but that re-introduces the conflation §1.3 flagged.

**N PASSES.**

### Ω — Intent

| Clause | Assessment |
|---|---|
| **Ω-a** Strategic actions produce cross-scale traceable-but-unanticipatable consequences | **Strong.** Leader change → Cascade re-resolves over 1-2 seasons → faction modus shifts → Public Expectation strictness drifts → Ob calculations change → DA outcomes shift → Legitimacy and Popular Support drift → strictness drifts again. Trace is queryable; full prediction requires modeling multiple coupled scalars. |
| **Ω-b** Personal-layer confrontation transforms character through substrate | **Adjacent.** Leader's personal Conviction Scars affect their personal_convictions, which propagate through Cascade. Personal-scale transformation has institutional-scale consequences. |
| **Ω-c** Autonomous agents generate consequential events independent of player | **Defining.** Cascade math runs each Accounting regardless of player input. Legitimacy and Popular Support drift on factor inputs the player only partially controls. |
| **Ω-d** No strategy produces dominance — every action pays what it buys | **Strong.** Acting against expectation costs Legitimacy. Acting with expectation but failing costs Popular Support. Successful covert action costs less than failed but costs proportional to violation. The non-monotonicity in strictness (high Legitimacy + low Popular Support = high strictness) means safe-but-unloved factions are *brittle*, not just stable. |

**Ω PASSES.**

### Μ — Modes served

- **Μ-α (pressure as engagement driver):** primary. Public Expectation creates continuous pressure; the populace is always evaluating.
- **Μ-β (autonomous agent composition):** primary. Cascade derivation runs without player input; faction state evolves continuously.
- **Μ-δ (cross-scale consequence):** primary. Leader Convictions → Cascade → faction modus → DA Ob → strategic outcome.
- **Μ-γ (substrate ontology):** adjacent. Operates through political/institutional substrate, not natural substrate.

No Μ undermined.

### М — Meta-throughlines (highlighted)

- **М-1 Pressure is continuous:** + extends. Public Expectation is a new continuous-pressure source, separate from existing Strain, Standing, etc.
- **М-4 Institutions stake substrate-postures:** + extends. Faction Convictions become *dynamically expressed* through Cascade rather than statically authored. An institution's posture can drift mid-game.
- **М-5 Scales connect through substrate:** + extends. New personal-↔-faction bridge through Cascade math (leader Conviction Scars affect institutional behavior).
- **М-6 Strategic actions have consequences across scales:** + extends. New feedback loop between leader (personal scale) and faction modus (institutional scale).
- **М-9 State evolves under pressure:** + extends. Mission shift, Cascade re-resolution, Legitimacy/Popular Support drift all create new state-evolution mechanisms.
- **М-11 External modulators exist:** + extends. Public Expectation as an external modulator on internal calculation.

No М contradiction.

### Τ — Throughlines (load-bearing)

- T-04 (institutional decay through cascade incoherence) — directly modeled
- T-09 (legitimate vs effective authority) — directly modeled (Legitimacy vs Popular Support)
- T-15 (the persuasive populace) — modeled through Popular Support feedback
- T-23 (succession cascade) — directly modeled
- T-27 (effects real, explanation wrong) — supported via NPC personal vs effective Conviction divergence
- T-31 (institutional posture shifts under leadership) — directly modeled

(Throughline IDs cross-referenced from `references/throughlines.md`; PP-677 mappings updated as part of Stage 7.)

### Q — Quality

**Q-robust.** Authoring inputs scale with faction count: 6 factions × (Mission spec + organizational hierarchy + institutional_culture) ≈ moderate one-time cost. Per-territory public temperament: ~30-50 territories × 1 selection = small. Role templates: 6 role-types × Conviction profile = trivial.

Player customization: Mission can shift on state; Cascade emerges from organic NPC choices; Public Expectation responds to faction's actual track record. All emergent rather than scripted.

Variety: a Crown that delivers through Honor vs through Authority vs through covert Utility produce *different* faction modes despite same role and Mission. Same for every faction. Output space is multidimensional.

Emergent narrative: a new leader rising in a faction with strong Cascade Fidelity inheritance creates institutional drift that either honors the legacy (high Cascade Fidelity maintained) or breaks from it (Cascade Fidelity drops, Legitimacy bleeds). Both are dramatically interesting paths.

**Q-smooth.** Single derivation chain (Mission + Cascade + Expectation → Ob). Existing Mandate consumers continue to work via transitional derivation. New mechanic interfaces with existing faction stats (Standing for α_seniority, faction.beneficiary for outcome targeting). Calibration uses the same 0-7 scale already canonical for faction stats.

Scale-zoom: Cascade derivation aggregates personal-scale Convictions into faction-scale modus; outcomes faction-scale DAs into territorial-scale Popular Support changes. Each scale-bridge has explicit math.

Calculation methodology consistent: dot products, weighted averages, scalar drift. Same primitives the existing armature/EventImpact system uses.

**Q-elegant.** Four independent inputs (Mission, Leader, Hierarchy, Role), all authored at small scale; everything else is derived. The system *adds* mechanical depth (separates Legitimacy from Popular Support; introduces dynamic Cascade) while *reducing* authoring debt (no per-faction Ethical Framework Modifier table; no static Ob lookup; role templates author once and apply universally).

The non-monotonic strictness function is the inelegant but faithful piece: it's not pretty, but it captures the real political dynamic that secure-but-unloved regimes are punished for any deviation while populist regimes are tolerated.

**Q PASSES with the strictness function flagged for empirical calibration during Stage 10 sim verification.**

---

## §6 Open Questions for Decision

Items requiring Jordan call before this proposal can be ratified:

1. **PP-684 dependency confirmation.** This proposal assumes the 10-12 Conviction taxonomy from current discussion. If taxonomy is not ratified, role templates in §3.3 need re-targeting.
2. **Honor as 12th Conviction.** Several role templates assume Honor exists. If Honor is folded into Identity or Virtue, templates change.
3. **α calibration.** The α_base = 0.4 / α_seniority range / α_institution range numbers are placeholders. Sim verification will tune them; initial values acceptable as starting point?
4. **Public temperament authoring.** §3.4's 5-temperament typology is proposed; territories need temperament assignment (~30-50 entries). Approve typology, or revise?
5. **Strictness function form.** The `0.5 × Legitimacy - 0.3 × Popular_Support + base` form is proposed. Empirical sim could prefer different coefficients or non-linear form. Approve provisional, calibrate at Stage 10?
6. **Mandate retention vs replacement.** Proposal recommends transitional retention. Alternative: hard cutover, refactor all consumers in this proposal's scope. Which?
7. **Outcome / cascade weighting (α_temperament + β_temperament = 1).** The constraint that α + β = 1 means outcomes and conduct are full-substitutes. Alternative: independent scalars where extreme weight on either gives high response. Which?
8. **Mission shift triggers.** §3.1 names "major state change" but does not enumerate. Need explicit list: victory-track milestone passes? Leader replacement? Failed mission_failure_threshold? Other?

---

**End proposal.** Ready for review and ratification (PP-686 or next available number) pending §6 decisions.
