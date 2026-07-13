# Vectorized Settlement Generation (VSG v1) — a vertical stack of weighted paradigms with noisy throughlines

## Status: PROPOSAL / working notes, Jordan-vetoable
## Date: 2026-07-13 · Lane: SE · Reference draw: `goldenfurt_slice/` · Reifies: `goldenfurt_slice/generation_methodology.md §6`

**What this is.** A generator design that reifies the tacit authoring stack that produced Goldenfurt
(`goldenfurt_slice/generation_methodology.md`) into an explicit, seeded, reproducible procedure. A
settlement — and, two layers deeper, its characters and event deck — is generated as one **noisy line
drawn top-to-bottom through a stack of weighted paradigm-layers**, each conditioned on the layers
above and sampled with a fixed seed. It claims no new canon; it is a generator *over* existing
canonical tables (`settlement_layer_v30`, `territory_temperaments_v30`, `valoria_geography_v30.yaml`,
`political_hierarchy_v30`) plus the 2026-07 comparative-governance proposals. It depends on the
`governance_consolidation_v1 §6` D1–D5 rulings landing (L5/L8 read them).

---

## §0 Thesis

Coherence is not authored post-hoc — it is (a) *conditioned in* (plausibility flows down the stack)
and (b) *threaded in* by explicit collision constraints. Formally:

```
P(settlement) = P(L0) · ∏ᵢ P(Lᵢ | L₍<ᵢ₎)
```

sampled at temperature τ, with `seed = sha256(map_point ‖ layer_index ‖ campaign_salt)` truncated to
64 bits — the cross-platform determinism rule the churn engine already mandates
(`designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md §3`), never a
salted builtin hash. Weights *bias*; noise *chooses*; τ tunes sharpness (τ→0 = argmax deterministic,
τ→∞ = uniform). A campaign re-rolls identically; a re-seed re-individuates.

Goldenfurt is the calibration instance the generator must reproduce from its seed (§5), exactly as the
arc-vector engine must reproduce its 138 register arcs (churn-engine v2 §2).

---

## §1 The vertical stack (10 paradigms)

Ordered by causal precedence — each paradigm's weights read the realized draws above it.

| # | Paradigm | Axis it samples | Conditioned by | Canon / proposal source |
|---|---|---|---|---|
| **L0** | **Seed (Geography)** | map point → province frame: faction, region/sub, `fort_level 0–4`, `spiritual_weight 0–2`, `proximity_calamity 0–5`, `starting_pros`, adjacency degree, breadbasket/port/mineral flags, thread-proximity | — (root) | `valoria_geography_v30.yaml`; `political_hierarchy_v30 §1` |
| **L1** | **Type** | settlement type (§4 taxonomy fix: 11 types) → stat priors, natural manager, facility ceiling, `base(Type)` Weight | L0 | `settlement_layer_v30 §1.2`, `§1.8` |
| **L2** | **Economy** | primary product (grain/toll/trade/mineral/mixed), grain-route dependency, Prosperity, Assessment/Compact posture | L0, L1 | `§1.3`, `§4.3b`, `§1.3a` (ED-SE-0018/19) |
| **L3** | **Religion** | the 4 independent Church-infra axes (Building/Templar/Inquisitor/Governor) + Pastoral-Assumption risk | L0 (`spiritual_weight`, faction, Himmelenger distance) | `§1.5`, `§1.6`, `§1.7` |
| **L4** | **Culture / Temperament** | 5-typology α/β — **promoted to settlement grain** with noise around the province mean (closes the Stage-6b deferral) | L0 (region, calamity drift), province baseline | `territory_temperaments_v30 §1–4` |
| **L5** | **Governance** | Provincial Authority; subnational claimant strengths (Guild/Church/RM/Niflhel/Ministry/Löwenritter/Wardens); `facility_tier → AP`; Clerk Capacity; Charter/Za/Seggio structures; initial suspicion | L0–L4 | `governance_play_redesign_v1 §1`; `settlement_layer_v30 §3.3`, `§1.1a`, `§3.3a-c` |
| **L6** | **L/PS · Weight · Mandate** | L (0–7), PS (0–7), Weight, faction-Mandate contribution; seeded via Entry-Terms fork | L0–L5 | `§1.8`, `§1.8a`, `§5.3` (⚠ inert substrate, ED-FA-0004) |
| **L7** | **Actor roster (→ characters)** | NPC cast: role · `power_base` · Standing · ethic α/β · conviction · ambition+trajectory · leverage · Knots | L4 (ethic spread), L5 (present factions) | `governance_play_redesign_v1 Part 3`; rise-to-power "Ascendancy" `power_base` |
| **L8** | **Event deck (→ events)** | per-family card set (Petition/Friction/Opportunity/Crisis/Intrigue/Ambition/Thread) + Π homeostat seed + Directive priors | L2/L3/L5 (pressure sources), L7 (collisions) | `governance_play_redesign_v1 Part 2`; `2026-07-12-governance-compendium/43_directive_types.md` |
| **L9** | **Verify (gate)** | 4-lens adversarial pass — *part of the generator, not optional* | the full draw | `goldenfurt_slice/verification_findings.md` |

**Illustrative weight table (L1 Type, conditioned on L0)** — to make "weighted paradigm" concrete:

```
weight(Type | geo) = base_prior(Type)
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
biasing L2 toward a toll economy. The seed produces the collisions organically, not by hand.

---

## §2 The noisy-throughlines formalism

**Throughlines** = the constraints that thread values across layers into one coherent, dramatic
settlement. Three kinds — and distinguishing them is what makes VSG better than naïve independent
slicing:

1. **Conditioning throughlines (vertical).** `P(Lᵢ|L₍<ᵢ₎)` — plausibility flows down. A devout
   heartland draws Chapel-not-Cathedral; a calamity frontier drifts temperament to outcomes-only.
2. **Collision throughlines (load-bearing).** Hard constraints the generator MUST satisfy, per
   `governance_play_redesign_v1 §3.3` speccing-for-friction: **every settlement carries ≥1 Hold-Court
   collision** (two actors whose convictions make any ruling wrong one); **every opposed subnational
   pair present shares a Friction card**; **ethic spread ≥ Δ across the roster**. These take the noisy
   roster and *thread guaranteed conflict through it* — the "noisy throughline" proper. (Hedda-law vs
   Orsk-commerce is the canonical instance.)
3. **Coupling throughlines (horizontal — the anti-bug rule).** Where two paradigms are mechanically
   coupled, they must be **jointly sampled or explicitly linked**, never sampled independently.
   Religion↔Governance couple through `church_attention`; Economy↔Crisis through grain dependency.
   **This is the direct fix for verification findings sim-F1…F9** — independent sampling of coupled
   slices is what left Goldenfurt's spec missing 7 fields.

---

## §3 Extending the stack to events & characters

The same machine, run deeper — the payoff of a *stack* rather than a settlement-only generator:

- **L7 — Characters.** Draw a roster sized by type (facility slots + Local-Actor count, §4.5), then
  per NPC sample: role (from L5's present factions), **`power_base`** (the Ascendancy field —
  patronage/merit/kinship/bureaucratic/military/purchased/ideological, which *types the NPC's built-in
  downfall*, satisfying Ω-d), Standing on the shared ladder, ethic from L4's spread, and the Part-3
  `ambition`+`trajectory`+`leverage`+`Knots`. Sampled **under collision throughlines**, not
  per-NPC-independently.
- **L8 — Events.** The deck is *generated, not hand-authored*: each present collision (L7) and each
  pressure source (L2/L3/L5) **emits its own cards** — Ambition cards one-per-NPC (G60x), Friction
  cards from Directive×Need conflicts, family weights biased by the paradigm draws (grain-dependent →
  more Crisis/famine; smuggling ford → more Niflhel Intrigue; Chapel + ambitious priest → the
  Geneva-trap chain). Directive priors drawn from the expanded taxonomy (Extract/Tax/Suppress/Install/
  Host/Cede + Embargo/Recall/Quarter).
- **L(∞) — the runtime seam.** VSG *is* the **L0 GENERATOR** of the arc-vector churn engine
  (churn-engine v2 §8). Its output settlement is the *binding substrate* the ~13 throughline templates
  bind to at runtime. Generation makes the world; the churn engine animates it.

---

## §4 Anti-failure invariants baked in (the lessons, made structural)

The stress-sim + verification passes converge on a small defect set; VSG fixes each *at the generator
level*, so no settlement is patched individually:

- **Death-spiral fix as a generator invariant.** L8 seeds the **bidirectional Π restoring term**
  `sign(3−Π)·min(1,|3−Π|)` (Goldenfurt CG-1) + a subsistence-floor clamp + a G606-style
  survivable-recall escape — already designed in Goldenfurt, now defaults not per-settlement authoring.
  (The single highest-leverage move every analysis converged on — cf. `2026-07-12-settlement-season-
  stress-sim/reconciliation_with_existing_territory_work.md`.)
- **Coupling throughlines** (§2.3) eliminate the sim-F1…F9 missing-field class by construction.
- **Taxonomy reconciliation is a precondition.** VSG's Type paradigm must operate on ONE canonical type
  set — this proposal folds `Village`, `Fortress-City`, `Cathedral-City` into `§1.2` (they already
  appear in `§1.8`/`§2.1`), closing the cross-confirmed H3/F1 drift that roots 7 downstream findings.
- **`Compact` reconciliation** (governance_consolidation D3): VSG treats Compact as a recurring `Debt`
  subtype, not a colliding 6th `ledger.py` family.
- **Verify is Layer 9**, not optional — the 4-lens pass runs on every generated settlement before trust.

---

## §5 Calibration requirement (must reproduce Goldenfurt)

VSG's acceptance test, mirroring the churn engine's "reproduce the 138 arcs" fixture: **seed at S-006's
map point → the stack reproduces Goldenfurt** — Town / breadbasket-toll economy / Chapel-with-Geneva-
path / traditional α0.3-β0.7 / Crown-PA-with-Guild-Church-RM-Niflhel collisions / the
Hedda-Orsk-Konrad cast / the 28-card deck's family distribution. If it can't reproduce the
hand-authored exemplar, the weights are wrong.

**Precondition:** fix S-006's tri-booking first — the seed itself is currently ambiguous across
`valoria_geography_v30.yaml` (T3 Lowenskyst), `settlement_layer_v30 §2.1` (Goldenfurt Town, Kronmark)
and `§5.1` (Lowenskyst Fortress). See `goldenfurt_slice/generation_methodology.md §7`.

---

## §6 Where it lives (modularity)

Per the churn engine's kernel/data/wrapper contract (v2 §7):

- **KERNEL** (content-blind): the stack stepper, the seeded sampler, the throughline-constraint solver,
  the verify harness. Zero content literals.
- **DATA** (versioned, schema-validated, CI round-tripped — **the weight tables ARE the authorial
  surface**, like the Light-Function weight set): per-layer weight tables, collision-throughline rules,
  the type taxonomy, temperature τ, the Π constants. Jordan revises weights as data, no engine change.
- **WRAPPER:** loads a settlement pack; feeds `sim/territory/registry.py`'s `Settlement`.

**Build sequence:** taxonomy fix + S-006 reconcile (preconditions) → L0–L1 sampler + Goldenfurt-
reproduction fixture → L2–L6 → L7–L8 (reuse Goldenfurt's cast/deck as the calibration set) → L9 verify
harness. Rides the existing `sim/territory/` code (G1 already closed).

---

## §7 Open Jordan calls this proposal surfaces

- **Settlement-grain temperament** (L4) — promote α/β from province to settlement grain? (Stage-6b was
  deferred; VSG needs it.)
- **Which paradigms are load-bearing vs cut** — does settlement identity come from the full stack, or
  purely from the subnational-faction roster? (the ripple-substrate R-1 question.)
- **Weights are a taste surface** — τ and per-layer weights need a sim sweep against "ever boring /
  ever an unsurvivable spiral" before trust (the same open question `governance_play_redesign_v1 §5.3`
  and the death-spiral finding raise).
- Depends on `governance_consolidation_v1` D1–D5 (Compact, event-architecture, AP) landing first.

---

**Status:** PROPOSED, no ED allocated yet (SE lane; would take `ED-SE-NNNN` on landing). A generator
design over existing canonical tables + the July proposals; ratification tracks ordinary merge review.
