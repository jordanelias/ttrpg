# Vectorized Settlement Generation (VSG v1) — a vertical stack of weighted paradigms with noisy throughlines

## Status: PROPOSAL / working notes, Jordan-vetoable
## Date: 2026-07-13 · Lane: SE · Reference draw: `goldenfurt_slice/` · Reifies: `goldenfurt_slice/generation_methodology.md §6` · Grounding sweep: `generation_sourcebook_v1.md` (settlement + faction + territory stacks, canon tables, blocker register)

**What this is.** A generator design that reifies the tacit authoring stack that produced Goldenfurt
(`goldenfurt_slice/generation_methodology.md`) into an explicit, seeded, reproducible procedure. A
settlement — and, three paradigms deeper, its characters and event deck — is generated as one **noisy
line drawn top-to-bottom through a stack of weighted paradigm-layers**, each conditioned on the layers
above and sampled with a fixed seed. It claims no new canon; it is a generator *over* existing
canonical tables (`settlement_layer_v30`, `territory_temperaments_v30`, `valoria_geography_v30.yaml`,
`political_hierarchy_v30`, `clock_registry_v30`, `faction_politics_v30`) plus the 2026-07
comparative-governance proposals. It depends on the `governance_consolidation_v1 §6` D1–D5 rulings
landing (P10/P14 read them).

---

## §0 Thesis

Coherence is not authored post-hoc — it is (a) *conditioned in* (plausibility flows down the stack)
and (b) *threaded in* by explicit collision constraints. Formally:

```
P(settlement) = P(P1) · ∏ᵢ P(Pᵢ | parents(Pᵢ))
```

sampled at temperature τ, with `seed = sha256(map_point ‖ paradigm_index ‖ campaign_salt)` truncated
to 64 bits — the cross-platform determinism rule the churn engine already mandates
(`designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md §3`), never a
salted builtin hash. Weights *bias*; noise *chooses*; τ tunes sharpness (τ→0 = argmax deterministic,
τ→∞ = uniform). A campaign re-rolls identically; a re-seed re-individuates.

The conditioning graph is a **DAG, not a chain** — each paradigm names its parents. Goldenfurt is the
calibration instance the generator must reproduce from its seed (§5), exactly as the arc-vector engine
must reproduce its 138 register arcs (churn-engine v2 §2).

---

## §1 The vertical stack — twelve settlement paradigms + three downstream

Ordered by conditioning precedence. Each paradigm's weights read the realized draws of its parents.

| # | Paradigm | Axis it samples | Parents | Canon / proposal source | Goldenfurt draw |
|---|---|---|---|---|---|
| **P1** | **Location** (seed/root) | province · region/sub · coords · adjacency degree · pass/coast/river proximity · `spiritual_weight 0–2` · `fort_level 0–4` · `proximity_calamity 0–5` · `starting_pros` | — | `valoria_geography_v30.yaml`; `political_hierarchy_v30 §1` | Kronmark T2 heartland, river **ford**, `spiritual_weight 1`, `prox_cal 4` |
| **P2** | **Starting faction** | Provincial-Authority owner: Crown / Hafenmark / Varfell / Church (+Schoenland foreign) | P1 (duchy) | `political_hierarchy_v30 §1`; geo `faction` | **Crown** |
| **P3** | **Size** | population / Weight tier (Village→…→City); `base(Type)`+Prosperity+facility scale | P1, P2 | `settlement_layer_v30 §1.8` Weight | small–mid (breadbasket spoke) |
| **P4** | **Type** | 11-type set (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost/Village/Fortress-City/Cathedral-City) → stat priors, natural manager, facility ceiling | P1, P3, P2 | `§1.2` (+ §4 taxonomy fix) | **Town** |
| **P5** | **Piety ↔ Restoration** | Piety Track 0–5 (0 = RM pole / 5 = Solmund-orthodoxy); RM presence (PT≤2 gate); Church-infra baseline | P1 (`spiritual_weight`, Einhir region), P2 | `clock_registry_v30 §PT`; `§1.5`; `§3.3` RM | mid-low PT: devout Crown, **RM old-rite undercurrent in hamlets** |
| **P6** | **Altonian influence** | foreign-power exposure: pass proximity (T3 Lowenskyst / T10 Spartfell), containment placement, Schoenland sea trade; IP≥75 route opens | P1 (border/coast) | `march_layer_v30 §6.3`; `political_hierarchy_v30 §1.2`; `valoria_map_v30.svg` | **negligible** (deep interior) |
| **P7** | **Infrastructure** | facility tiers (Wing/Suite/Chamber/Billet); Church-infra 4 axes; `fort_level`; granary; roads/adjacency | P4, P3, P1 (fort), P5 (church) | `§1.4`, `§1.5`, `§4.3a` | facility_tier 1 (**AP 3**), **Chapel**, no garrison, ford works |
| **P8** | **Economy** | product mix (grain/toll/trade/mineral); grain-route dependency; Prosperity; Assessment/Compact posture | P1 (breadbasket/port/mineral), P4, P7, P6 (trade) | `§1.3`, `§4.3b`, `§1.3a` (ED-SE-0018/19) | **breadbasket grain + tolled ford** |
| **P9** | **Caste / demographics** | Northern/Central/**Southern Einhir** (stigmatized, higher baseline TS, economically suppressed); composition | P1 (region → Einhir heritage), P2 | `faction_politics_v30 §3` | Crown-Latinate majority + **Einhir-heritage hamlets** (Greta) |
| **P10** | **Governance type** | dual-authority config: PA + subnational manager (§3.3); Charter/Za/Seggio; Clerk Capacity; governance mode | P4, P2, P8, P7 | `governance_play_redesign_v1 §1`; `§3.3`, `§3.3a-c`, `§1.1a` | Crown PA; **Guild/Church/RM/Niflhel** claimants; no formal charter |
| **P11** | **Political allegiance** | faction the elite/populace actually back (≠ owner → fracturing); L toward PA | P2, P10, P5, P9, P6 | `political_hierarchy_v30 §2.3`; `§1.8` L | nominally Crown, **strained** (defiance path viable) |
| **P12** | **Sociopolitical sympathies** | temperament α/β + finer leanings (reform / tradition / guild-power / church / autonomy / RM) | P9, P5, P8, P11, province temperament | `territory_temperaments_v30 §1` | **traditional α0.3/β0.7** + a spread (Hedda-reform · Orsk-commerce · Greta-restoration) |
| **P13** | **Actor roster** (→ characters) | NPC cast: role · `power_base` · Standing · ethic α/β · conviction · ambition+trajectory · leverage · Knots | P12 (ethic spread), P10 (present factions), P9 | `governance_play_redesign_v1 Part 3`; rise-to-power "Ascendancy" `power_base` | Hedda · Orsk · Wessel · Tomas · Greta · Konrad + 3 Local Actors |
| **P14** | **Event deck** (→ events) | per-family card set (Petition/Friction/Opportunity/Crisis/Intrigue/Ambition/Thread) + Π homeostat seed + Directive priors | P8/P5/P10 (pressure sources), P13 (collisions) | `governance_play_redesign_v1 Part 2`; `2026-07-12-governance-compendium/43_directive_types.md` | the 28-card deck (7 families) |
| **P15** | **Verify** (gate) | 4-lens adversarial pass — *part of the generator, not optional* | the full draw | `goldenfurt_slice/verification_findings.md` | the 32-finding pass |

**Illustrative weight table (P4 Type, conditioned on P1–P3)** — to make "weighted paradigm" concrete:

```
weight(Type | P1,P3) = base_prior(Type, size=P3)
  + 3·[fort_level ≥ 3]                          → Fortress, Fortress-City
  + 3·[spiritual_weight ≥ 2 ∧ church_adjacent]  → Cathedral, Cathedral-City
  + 2·[breadbasket_flag]                        → Town, Village   (agrarian)
  + 2·[port_geometry]                           → Port
  + 2·[capital_region ∧ starting_pros ≥ 5]      → Seat, City
  + 2·[mineral_flag]                            → Mine
  + 1·[frontier ∧ low_pros]                     → Outpost, Village
→ sample at temperature τ
```

Goldenfurt: `spiritual_weight 1`, breadbasket, Crown heartland, tolled ford → **Town** wins, the ford
biasing P8 toward a toll economy and P10 toward a Guild claimant. The seed produces the collisions
organically, not by hand.

---

## §2 The noisy-throughlines formalism

**Throughlines** = the constraints that thread values across paradigms into one coherent, dramatic
settlement. Three kinds — and distinguishing them is what makes VSG better than naïve independent
slicing:

1. **Conditioning throughlines (vertical, the DAG edges).** `P(Pᵢ | parents)` — plausibility flows
   down. A devout heartland draws Chapel-not-Cathedral; a calamity frontier drifts temperament to
   outcomes-only; a pass-town draws high Altonian influence.
2. **Collision throughlines (load-bearing).** Hard constraints the generator MUST satisfy, per
   `governance_play_redesign_v1 §3.3` speccing-for-friction: **every settlement carries ≥1 Hold-Court
   collision** (two P13 actors whose convictions make any ruling wrong one); **every opposed
   subnational pair present (P10) shares a P14 Friction card**; **ethic spread ≥ Δ across the roster**.
   These take the noisy roster and *thread guaranteed conflict through it* — the "noisy throughline"
   proper. (Hedda-law vs Orsk-commerce is the canonical instance.)
3. **Coupling throughlines (horizontal — the anti-bug rule).** Where two paradigms are mechanically
   coupled, they must be **jointly sampled or explicitly linked**, never sampled independently — the
   direct fix for verification findings sim-F1…F9 (independent sampling of coupled slices is what left
   Goldenfurt's spec missing 7 fields). The load-bearing couplings in THIS axis set:
   - **P5 ↔ P9 ↔ P1** — Restoration sympathy, Einhir heritage, and low PT co-vary; a stigmatized-Einhir
     hamlet region *is* where RM seats (PT≤2 gate). Goldenfurt's Greta is exactly this triple.
   - **P6 ↔ P1 ↔ P8** — Altonian influence, border/coast geography, and trade economy co-vary (P6 also
     feeds P11: a pass-town's allegiance is pulled foreign).
   - **P8(grain) ↔ P14(Crisis)** — grain dependency arms the Dearth fuse (`§4.3a-b`).
   - **P11 vs P2 is the fracturing engine** — when political allegiance diverges from the starting
     faction, `political_hierarchy_v30 §2.3` fracture fires; the generator can *seed a contested
     settlement deliberately* by drawing P11 off-owner.

---

## §3 The downstream paradigms (events & characters), in detail

The same machine, run deeper — the payoff of a *stack* rather than a settlement-only generator:

- **P13 — Characters.** Draw a roster sized by type (facility slots + Local-Actor count, §4.5), then
  per NPC sample: role (from P10's present factions), **`power_base`** (the Ascendancy field —
  patronage/merit/kinship/bureaucratic/military/purchased/ideological, which *types the NPC's built-in
  downfall*, satisfying Ω-d), Standing on the shared ladder, ethic from P12's spread, and the Part-3
  `ambition`+`trajectory`+`leverage`+`Knots`. Sampled **under collision throughlines**, not
  per-NPC-independently.
- **P14 — Events.** The deck is *generated, not hand-authored*: each present collision (P13) and each
  pressure source (P8/P5/P10) **emits its own cards** — Ambition cards one-per-NPC (G60x), Friction
  cards from Directive×Need conflicts, family weights biased by the paradigm draws (grain-dependent →
  more Crisis/famine; smuggling ford → more Niflhel Intrigue; Chapel + ambitious priest → the
  Geneva-trap chain; high Altonian influence → foreign-intrigue/border-Friction). Directive priors
  drawn from the expanded taxonomy (Extract/Tax/Suppress/Install/Host/Cede + Embargo/Recall/Quarter).
- **The runtime seam.** VSG *is* the **L0 GENERATOR** of the arc-vector churn engine (churn-engine v2
  §8). Its output settlement is the *binding substrate* the ~13 throughline templates bind to at
  runtime. Generation makes the world; the churn engine animates it.

---

## §4 Anti-failure invariants baked in (the lessons, made structural)

The stress-sim + verification passes converge on a small defect set; VSG fixes each *at the generator
level*, so no settlement is patched individually:

- **Death-spiral fix as a generator invariant.** P14 seeds the **bidirectional Π restoring term**
  `sign(3−Π)·min(1,|3−Π|)` (Goldenfurt CG-1) + a subsistence-floor clamp + a G606-style
  survivable-recall escape — already designed in Goldenfurt, now defaults not per-settlement authoring.
  (The single highest-leverage move every analysis converged on — cf. `2026-07-12-settlement-season-
  stress-sim/reconciliation_with_existing_territory_work.md`.)
- **Coupling throughlines** (§2.3) eliminate the sim-F1…F9 missing-field class by construction.
- **Taxonomy reconciliation is a precondition** (P4). VSG's Type paradigm must operate on ONE canonical
  type set — this proposal folds `Village`, `Fortress-City`, `Cathedral-City` into `§1.2` (they already
  appear in `§1.8`/`§2.1`), closing the cross-confirmed H3/F1 drift that roots 7 downstream findings.
- **`Compact` reconciliation** (governance_consolidation D3): P8/P10 treat Compact as a recurring
  `Debt` subtype, not a colliding 6th `ledger.py` family.
- **Verify is P15**, not optional — the 4-lens pass runs on every generated settlement before trust.

---

## §5 Calibration requirement (must reproduce Goldenfurt)

VSG's acceptance test, mirroring the churn engine's "reproduce the 138 arcs" fixture: **seed at S-006's
map point → the stack reproduces Goldenfurt** — the twelve draws in §1's rightmost column: Crown Town /
breadbasket-toll economy / Chapel-with-Geneva-path / mid-low PT with RM undercurrent / negligible
Altonian influence / traditional α0.3-β0.7 sympathies-with-a-spread / Guild-Church-RM-Niflhel
collisions / the Hedda-Orsk-Konrad cast (P13) / the 28-card deck's family distribution (P14). If it
can't reproduce the hand-authored exemplar, the weights are wrong.

**Precondition:** fix S-006's tri-booking first — the seed itself is currently ambiguous across
`valoria_geography_v30.yaml` (T3 Lowenskyst), `settlement_layer_v30 §2.1` (Goldenfurt Town, Kronmark)
and `§5.1` (Lowenskyst Fortress). See `goldenfurt_slice/generation_methodology.md §7`.

---

## §6 Where it lives (modularity)

Per the churn engine's kernel/data/wrapper contract (v2 §7):

- **KERNEL** (content-blind): the DAG stepper, the seeded sampler, the throughline-constraint solver,
  the verify harness. Zero content literals.
- **DATA** (versioned, schema-validated, CI round-tripped — **the weight tables ARE the authorial
  surface**, like the Light-Function weight set): per-paradigm weight tables + parent lists, the
  collision-throughline rules, the coupling groups, the type taxonomy, temperature τ, the Π constants.
  Jordan revises weights as data, no engine change.
- **WRAPPER:** loads a settlement pack; feeds `sim/territory/registry.py`'s `Settlement`.

**Build sequence:** taxonomy fix + S-006 reconcile (preconditions) → P1–P4 sampler + Goldenfurt-
reproduction fixture → P5–P12 (the coupling groups authored together) → P13–P14 (reuse Goldenfurt's
cast/deck as the calibration set) → P15 verify harness. Rides the existing `sim/territory/` code (G1
already closed).

---

## §7 Open Jordan calls this proposal surfaces

- **Settlement-grain temperament** (P12) — promote α/β from province to settlement grain? (Stage-6b was
  deferred; VSG needs it.)
- **Political allegiance as a first-class generation axis** (P11) — is deliberately seeding an
  off-owner (contested/fracture-prone) settlement in scope, or does allegiance only emerge from play?
  (bears on `political_hierarchy_v30 §2.3` fracture triggers, still unspecified.)
- **Which paradigms are load-bearing vs cut** — does settlement identity come from the full twelve, or
  a smaller core (the ripple-substrate R-1 question)?
- **Weights are a taste surface** — τ and per-paradigm weights need a sim sweep against "ever boring /
  ever an unsurvivable spiral" before trust (the same open question `governance_play_redesign_v1 §5.3`
  and the death-spiral finding raise).
- Depends on `governance_consolidation_v1` D1–D5 (Compact, event-architecture, AP) landing first.

---

**Status:** PROPOSED, no ED allocated yet (SE lane; would take `ED-SE-NNNN` on landing). A generator
design over existing canonical tables + the July proposals; ratification tracks ordinary merge review.
