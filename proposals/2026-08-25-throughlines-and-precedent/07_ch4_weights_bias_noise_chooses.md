# CHAPTER 4 — Weights Bias, Noise Chooses

*The Vectorized Slice Generator: what it is, what survived audit, what did not, and the gate that makes it shippable.*

---

## 0. The verdict, before the evidence

Valoria's generation method — **VSG**, the Vectorized Slice Generator reified from how Goldenfurt was hand-authored — divides into two things that must be judged separately, because the evidence judges them oppositely.

> **The architecture survived every audit thrown at it. The calibration survived none.**

The architecture is the pipeline: *geography seed → conditioned weighted slices → noise → thread → verify*, factorized as `P(settlement) = P(P1) · ∏ᵢ P(Pᵢ | parents(Pᵢ))` (`systems/settlements/settlement_generator_v1.md:24`; the conditioning graph is declared "a DAG, not a chain" at `:33`). That is not a homegrown bet needing defence. Dwarf Fortress worldgen, Caves of Qud's abstract-then-reify model and Ultima Ratio Regum's culture stack arrived at the same layered conditioned structure independently (P4 §1, §2.2, §3.1) — and the *rival* paradigm converged on it too: WFC/Model Synthesis's documented homogenization at map scale was rediscovered and fixed the same way by two unrelated teams, both adding **a conditioning layer above the local solver** (P4 §S4.2). VSG's vertical stack is not competing with constrain-and-solve; **it is the layer constrain-and-solve itself needs and has no general answer for** (P4 §S3). Say this plainly, because the corpus never does: the architecture is the field's consensus answer, arrived at four times.

The calibration is the weights, the thresholds and above all the restoring terms. Its one measured instance failed catastrophically, and did so at *both* boundaries in succession. `sim_build_spec.md §10` says it in the design's own words: **"the weights are guesses pending a sim sweep."**

A third fact governs everything below: **almost none of it executes.** The kernel does not exist; the runtime it feeds does not exist. Under CLAUDE.md §0.05 both halves are *reference*. So this chapter is careful about tense — and it will not present the 298/300 pin as a live bug, because it is not one.

---

## 1. The method, as an implementable algorithm

### 1.0 Kernel / Data / Wrapper

The design already commits to the split that makes everything else possible (`settlement_generator_v1.md:168-183`):

| Layer | Contents | Where it should live `[INFERRED]` |
|---|---|---|
| **KERNEL** (content-blind) | DAG stepper, seeded weighted sampler, constraint solver, verify harness | `engine/generation/` |
| **DATA** (versioned, CI round-tripped) | weight tables + parent lists, collision rules, coupling groups, τ, Π constants | `systems/settlements/generation/*.yaml` |
| **WRAPPER** | loads a pack, emits into `Settlement` | `systems/settlements/sim/generate.py` |

`:174-176` states the load-bearing property: **"the weight tables ARE the authorial surface"** — Jordan revises weights as data, no engine change. That earns the E verdict in §6 and makes S conditional in the way §6 states.

### 1.1 SEED

A map point on the 1920×2880 canvas resolves to one of 17 provinces and inherits ⟨`anchor`, `polygon`, `fort_level` 0–4, `spiritual_weight`, `proximity_calamity` 0–5, `starting_pros`, `faction`, `region/sub`⟩. I parsed `systems/settlements/valoria_geography_v30.yaml`: **17 provinces, 37 settlements**, every province carrying the full scalar set. Goldenfurt is `S-006`, `territory: T2`, `type: Town`, `controller: Crown` (`:287-292`).

Two facts about this step matter more than the vector.

**(a) A range defect, verified numerically.** `settlement_generator_v1.md:45` declares P1's `spiritual_weight` as `0–2`. The live data has **T9 = 4, T15 = 5** (parsed from the YAML; `generation_sourcebook_v1.md:82,86` agrees). A sampler written from the doc clamps Himmelenger — the Cathedral City, the most spiritually-weighted province in the setting — to 2, silently destroying the exact conditioning that makes P4 draw *Cathedral*. Small, checkable, invisible until someone asks why the Church's seat generated as a Town.

**(b) The seed data has no runtime reader.** `populate_from_geography` (`systems/settlements/sim/registry.py:216-241`) reads only the `settlements:` map and documents field-by-field that "every other Settlement field … is left at its dataclass default." Grepping every `.py` under `engine/` and `systems/` for `provinces` returns **two hits, both comments**. The block VSG's seed conditions on is dead data at runtime — the seam fact §7's matrix cells turn on.

### 1.2 CONDITIONED SLICES

Fifteen paradigms in precedence order (`settlement_generator_v1.md:43-59`): P1 Location → P2 Faction (4-enum +Schoenland) → P3 Size → P4 Type (11-enum) → P5 Piety 0–5 → P6 Altonian exposure → P7 Infrastructure ⟨facility 0–3, church vector ⟨building, templar, inquisitor, governor⟩, fort, granary, roads⟩ → P8 Economy ⟨grain, toll, trade, mineral⟩ → P9 Caste ⟨Northern, Central, Southern-Einhir⟩ → P10 Governance type → P11 Allegiance → **P12 Temperament ⟨α,β⟩** → P13 Actor roster → P14 Event deck → P15 Verify. `base(Type)` is real: **Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1** (`settlement_layer_v30.md:160`).

**Exactly one weight table is authored in the entire corpus** (`settlement_generator_v1.md:63-73`):

```
weight(Type | P1,P3) = base_prior(Type, size=P3)
  + 3·[fort_level ≥ 3]                          → Fortress, Fortress-City
  + 3·[spiritual_weight ≥ 2 ∧ church_adjacent]  → Cathedral, Cathedral-City
  + 2·[breadbasket_flag]  → Town, Village     + 2·[port_geometry]  → Port
  + 2·[capital_region ∧ starting_pros ≥ 5]      → Seat, City
  + 2·[mineral_flag]      → Mine              + 1·[frontier ∧ low_pros] → Outpost, Village
→ sample at temperature τ
```

The other fourteen do not exist. **That gap is the largest distance between VSG-as-written and VSG-as-code** — larger than the missing kernel, because the kernel is a few hundred lines of content-blind machinery and the tables are the game.

### 1.3 NOISE — where, and with what distribution

- **Where:** at every paradigm's sample. *"each slice sampled stochastically — the weights BIAS, they do not DETERMINE"* (`generation_methodology.md:37`); *"Weights bias; noise chooses; τ tunes sharpness (τ→0 = argmax, τ→∞ = uniform)"* (`settlement_generator_v1.md:30-31`).
- **Distribution:** temperature-parameterized weighted categorical. **The functional form is written nowhere.** `[INFERRED]`: `wᵢ^(1/τ) / Σⱼ wⱼ^(1/τ)`. A power form and a softmax both satisfy the stated limits and differ materially at mid-τ — a real underdetermination.
- **Seeding:** `sha256(map_point ‖ paradigm_index ‖ campaign_salt)` truncated to 64 bits, *"never a salted builtin hash"* (`:28-31`). A campaign re-rolls identically; a re-seed re-individuates.
- **Second noise site (runtime drift):** `temperament_drift = clamp(drift + 0.1 × strain_delta, −1, +1)` (`territory_temperaments_v30.md §4`) — **this one executes**, §2.
- **Third (cross-scale):** each scale's temperament is *"partially derived by aggregating its children's realized temperaments"*, noise-on-top left as authoring detail (`:189-197`).

Purpose, stated in Compton's terms independently: *"Noise is the anti-oatmeal defense. Identical type + identical temperament still diverge… Without noise you get 8 template towns; with it, individuated ones"* (`generation_methodology.md:95-97`). §5 takes up why reaching the idea is not having the fix.

### 1.4 THREAD

Three kinds, and distinguishing them is the claimed advantage over naïve independent slicing (`settlement_generator_v1.md:81-108`): **conditioning** throughlines are the DAG edges (plausibility flows down for free); **collision** throughlines are hard constraints the generator must satisfy — every settlement carries ≥1 **Hold-Court collision** (two actors whose convictions make any ruling wrong one), every opposed subnational pair shares a Friction card, ethic spread ≥ Δ (**Δ is never quantified**); **coupling** throughlines are the anti-bug rule — P5↔P9↔P1, P6↔P1↔P8, P8(grain)↔P14(Crisis), P11-vs-P2 as the deliberate fracture seed. Independent sampling of coupled slices is the *structural cause* of the seven missing-field defects the Goldenfurt verification pass found (`verification_findings.md` sim-F1/2/3/5/7/9).

The threading rule with teeth is the **churn invariant**: *"every card has ≥1 response that emits a Π delta, and every player-action response writes ≥1 Ledger tag — no card can leave the player unable to change the world"* (`event_deck.md:5`). And the honest limit: threading *"is authored judgment, not sampling"* (`generation_methodology.md:103`).

### 1.5 The runtime seam

- **Draw count** `n = 1 + ⌊Π/3⌋`, clamped ≥1 — the anti-stall floor (`sim_build_spec.md:122`).
- **Card weight** `base + pressure_scaling(family, Π) + tag_modifiers` (`:124`). **No cap on `tag_modifiers` is named anywhere.** A card's outcome writes tags; tags re-weight the deck. That is unbounded positive feedback on the weight vector — §3's topology, one level up, on the sampler rather than the state. This chapter's addition to the register.
- **Deck:** 28 cards, 7 families — Petition 3 / Friction 5 / Opportunity 3 / Crisis 4 / Intrigue 5 / Ambition 6 / Thread 2 (`event_deck.md:11-19`); a robust deck estimated at 60–100 per settlement type.
- **The Π homeostat** (`sim_build_spec.md:130-145`), quoted because §3 depends on it:

```
Π_next = clamp( Π + Σ_unserved_needs + Σ_active_grudges(+0.5 ea)
              + Σ_ambitions_in_motion(+0.5 per NPC with progress>0 not firing)
              + external_shock − Σ_player_releases + restore_toward(3), 0, 10)
restore_toward(3) := sign(3 − Π) · min(1, |3 − Π|)
```

### 1.6 VERIFY (P15)

Four lenses — deck-balance, NPC-collision, churn-integrity, sim-completeness — run as *a gate inside the generator, not an optional pass* (`settlement_generator_v1.md:149`); on Goldenfurt they produced 32 findings, 15 high. Plus a calibration fixture: seeded at S-006's map point the stack must reproduce Goldenfurt's draws, cast and family distribution — *"If it can't reproduce the hand-authored exemplar, the weights are wrong"* (`§5`). **The right idea with no instrument.** §5 supplies one.

---

## 2. What actually executes — the honest three-part answer

I ran the chapter's falsifier: *if any `.py` samples a weighted slice table to produce a settlement, a cast or an event, VSG executes and this chapter's premise is wrong.* At HEAD, `random.choices` / `np.random.choice` / `weighted_sample` / `rng.choices` return **zero hits** across `engine/` and `systems/`; all ten `rng.choice(...)` calls are bare uniforms (eight in `systems/world/sim/npe.py`, two in `systems/factions/sim/faction_action.py:457,566`). **The premise holds.** But the useful answer has three parts.

**(a) The temperament slice executes — and exceeds its own doc.** `systems/settlements/sim/temperaments.py:33-38` carries the five-typology ⟨α,β⟩ vector as live code including Goldenfurt's exact authored draw (`"traditional": {"alpha": 0.3, "beta": 0.7}`), and `:126-131` implements runtime drift toward outcomes-only under strain. I executed it:

```
T2 temperament: traditional
T2 base:              {'alpha': 0.3,  'beta': 0.7,  'drift': 0.0, 'drift_applied': False}
after strain_delta=3: {'alpha': 0.48, 'beta': 0.52, 'drift': 0.3, 'drift_applied': True}
```

Goldenfurt's own province, its authored vector, a live drift dynamic. **This is the proof the method is implementable**, and the remaining distance is a weight table and a sampler, not a research programme.

**Two corrections to how this is usually stated.** First, the module is **executable but not executed**: grepping every `.py` for `temperament_of`, `apply_strain_shock` or `from systems.settlements.sim.temperaments` returns **one hit, a comment** (`engine/autoload/game_state.py:291`), and no test in `tests/valoria` mentions temperament. Under §0.2 that is a module that runs when you run it, not behaviour the game performs. Second, the drift is one-directional by the code's own admission — `if drift > 0` (`:126`), commented *"canon doesn't spec negative-drift semantics"* — a restoration-free accumulator, which puts it in §3's class.

**(b) The conditioning half of the kernel already exists in miniature.** `generate_npc` (`systems/world/sim/npe.py:226-330`) is documented as *"Tier 1: Archetype seed — ecology weights for the territory populate the 5 axes with locally-typical values. Tier 2: Deviation roll."* That is condition-then-noise, shipped: ecology nudges stance (`prosperity_high → +1 Church authority`, `:262-268`), faction is drawn with a **60% bias toward the controlling faction** (`FACTION_DEFAULT_WEIGHT_PCT = 60`, `:76`), volatility takes an ecology offset.

But `_ecology_weights` (`:186-208`) returns **flags, not weights** — 0/1 — and every *categorical* axis falls back to uniform: convictions `:273`, compromise `:280`, the deviation flip `:322`, whose own comment states the case exactly — a grounded opposition model exists on paper (the 13×4 conviction-axis matrix) *"but that matrix is prose and is not cooked into any artifact code reads. Until it is, a uniform draw over the other twelve is the honest deviation"* (`:317-320`).

So the missing kernel piece is sharper than "a generator": it is **one primitive — `weighted_choice(rng, table, tau)` — plus the tables.** The conditioning scaffolding, the seeding discipline and the two-tier archetype/deviation structure already run.

**(c) The runtime half is equally absent — and here tense matters.** `Settlement.pressure: float = 4.0` (`registry.py:79`). Total `.pressure` references across every `.py` in the tree: **two** — the serialization at `:122`, and `systems/social_contest/sim/contest/resolver.py:241` (`self.pr = venue.pressure`), a different object's field entirely. Grep for `sign(3-` or `PI_RUNAWAY`: nothing. **Π is declared with zero writers**, so `1 + ⌊Π/3⌋`, the tag re-weighting and the homeostat all depend on a variable nothing moves. Both halves of what the methodology calls "the two halves of one pipeline" are reference.

**(d) Two corroborations, both found by running something rather than reading it.** Both arrived mid-drafting as orchestrator corrections; I verified both at HEAD before adopting them.

*A guard everyone in this run described as covering something it does not cover.* The claim was that loading persons at world-gen is "golden-safe by construction." **Refuted by controlled experiment** — Chapter 1's author found both guards pin `generate_npc`'s **call counter** (`world.npc_counter`), not `world.npcs`. Two NPCs loaded directly into `world.npcs` left both guards **green at `npcs_generated = 0`** and **moved seed-42's winner from Crown to Hafenmark**; a control arm with `simulate_npc_actions` neutered reproduced baseline byte-exact, identifying the channel as `npe.simulate_npc_actions` drawing `world.rng` at `systems/overview/sim/accounting.py:139` (verified — the call sits inside the accounting step, docstring noting "Side-effect: world.npcs state mutated"). Cite Chapter 1 for the finding; I claim only its relevance. Five lanes, an adversarial audit and the orchestrator all read that guard and all read it wrong; one person ran it and it fell over. **That is this chapter's thesis applied to the apparatus that checks generators: a mechanism nobody exercises is indistinguishable from one that does not work** — the whole argument for §5's gate being an executing test rather than a documented protocol.

*A retracted number propagating through its own provenance record.* The live golden at `engine/tests/test_f7_smoke_oracle.py:267` is `{'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}` (verified; regenerated 2026-08-24 at the mass-battle engine swap, with `GOLDEN_WINNERS = {'Crown': 5, 'Church': 2, 'Varfell': 1}`, `BATTLES_MEAN = 35.1`, `SCENES_RESOLVED = 975`). The value `{37.5, 12.5, 12.5, 37.5}` is a **historical** line at `:75`, headed *"OLD (pre-OI-04, pre-transfer-motion) values."* The file states the rule it earned the hard way (`:262-265`): *"a fabricated history stays green forever and the next re-recorder reasons from it. Rule: a PREVIOUS line is read out of `git show <ref>:<file>`, never copied from the constant you are about to overwrite."* **Same failure class as the retracted ~87% win-share; this run produced two fresh instances in one week.** Filed as a guard belonging beside the precedent failures: *provenance-of-a-retracted-number*. A golden pins the live constants; nothing pins the prose beside them — §0.05 stated as a defect rather than a doctrine.

---

## 3. T-04 — accrual beats bounded restoration

### 3.1 The class

> *In a churn system, any state variable with unbounded or per-season-uncapped accrual and bounded restoration — capped, one-shot, one-directional or absent — converges to a boundary regardless of policy. A restoring term that cannot restore is a NERS-R failure (loop not bounded); its player-facing signature is the **inverted Ω-d**: not the player getting a free win, but the formula dominating the player.*

A class by construction — identical math, identical feedback topology — not by analogy, which is what the no-pattern-matching rule requires. Eleven instances are catalogued; these are the ones I verified at HEAD:

| Instance | Restoration | Verified at |
|---|---|---|
| Π homeostat | capped ±1/season | `sim_build_spec.md:139-145` |
| Settlement Order | *"no unforced decay term of its own"* | `governance_type_registry_v1.md:104` |
| Church Influence | *"no natural decay term"* | `:147` |
| Institutional Pressure | *"no ordinary per-season decay specified"* | `:148` |
| Church Attention Pool | *"No decay — pure accumulator"* | `:151` |
| **Temperament drift** (new, mine) | `if drift > 0` only | `temperaments.py:126` |
| **Deck `tag_modifiers`** (new, mine) | no cap named anywhere | `sim_build_spec.md:124` |

Four are stated as defects *in the registry's own rightmost column*. The corpus diagnosed itself and filed the diagnosis where nothing reads it.

### 3.2 The measured failure, in the correct tense

Four independent measurements converge (`systems/_architecture/ners_vsg_reconciliation_v1.md:43`, verified verbatim): the *unaugmented* `sign(3−Π)·min(1,|3−Π|)` term pins every settlement at the ceiling — **298/300, `PI_RUNAWAY_SUSTAINED`**. Conclusion at `:48-50`: **"E1 cannot ship, in VSG or anywhere else, without E3 and E7 landing in the same commit."** Note the history: the *fix* had itself been mis-signed once (CG-1) and pinned quiet towns at Π=0. **The restoring term was wrong in two different ways in succession, at opposite boundaries.**

**And it is not in the tree.** Verified in §2(c): no homeostat code, no writers on `Settlement.pressure`; the only implementation that executed the term was retired to `FORK:1e4c6f4`. So 298/300 is **a validated lesson about a formula, not a live bug**, and present-tensing it would be exactly the fabrication this analysis condemns. What it *is* is a design constraint waiting for the commit it constrains.

### 3.3 The boundary test, executed

P4 §S1 Step 6: run at zero injected noise and confirm the output does not converge to the boundary — *"a five-minute test that would have caught the historical failure without needing 300 runs."* The upstream lane called R "unfalsifiable-by-execution" because no kernel exists. **That is wrong: the formula is arithmetic, and arithmetic runs today.** I ran it — 50 seasons, Π₀ = 4.0, target 3, clamp [0,10], zero noise:

| accrual/season | Π after 50 seasons | verdict |
|---|---|---|
| 0.00 – 1.00 | 3.00 → 4.00 | stable equilibrium at `3 + a` |
| 1.01 | 4.50, still climbing (pins ≈ season 600) | ceiling pin, slow |
| 1.25 / 1.50 / 2.00 / 3.00 | 10.000 | **PINNED** — 1.50 pins in 12 seasons, 2.00 in 6 |

**The bifurcation sits at accrual = 1.0 exactly**, and the reason is structural, not empirical: `min(1, …)` saturates the restoring term at ±1, so for any `a > 1` the net drift is `a − 1 > 0` and the ceiling arrives in roughly `(10 − Π₀)/(a − 1)` seasons. No noise, tuning or play changes that. **Runtime: under one second. The 300-run campaign was never needed.**

Now put the design's own numbers in. Goldenfurt has six NPCs with ambition clocks, G601–G606 (`event_deck.md:17`), and the ambition term contributes **+0.5 per NPC with progress > 0** — up to **+3.0/season** before a single unserved need or grudge. **`a > 1` is not an edge case in this design; it is the default regime.** The 298/300 result is what the arithmetic predicts, and the arithmetic was legible from the formula the day it was written.

### 3.4 Why E1 genuinely needs E3 and E7 — derived, not asserted

The obvious repair is proportional restoration, `restore = −k(Π − 3)`. I ran that too (Π after 200 seasons):

| | k=0.25 | k=0.5 | k=1.0 | k=1.5 | k=1.9 | k=2.1 |
|---|---|---|---|---|---|---|
| a=1.0 | 7.00 | 5.00 | 4.00 | 3.67 | 3.53 | 7.30 (unstable) |
| a=2.0 | **10.00** | 7.00 | 5.00 | 4.33 | 4.05 | 8.30 (unstable) |
| a=3.0 | **10.00** | 9.00 | 6.00 | 5.00 | 4.58 | 0.00 (unstable) |

Equilibrium is `Π* = 3 + a/k`, and stability requires `k < 2`. So at the design's own `a ≈ 3`, holding Π out of the crisis band needs `k ≥ 1` — a controller that erases the entire displacement every season, at which point the meter stops behaving like a meter (an **E** failure traded for an **R** one). **Proportional restoration alone cannot fix this.** Accrual must be capped first — E3's subsistence floor — and a genuine release path must exist — E7. The reconciliation doc's bundling requirement is not editorial caution; it is what the algebra says, and this is the first place it has been shown rather than asserted.

**The design law generalizing it** is already Jordan's: *"no paradigm's weight table should encode a purely negative or purely positive track; every pressure needs a counter-pressure, every decay needs a growth path"* (`settlement_generator_v1.md §7.4`). The structural home exists too — `governance_type_registry_v1.md:245,265` proposes a `Field`/`Gauge` primitive with a **required `decay_fn`** (`none | linear:rate | homeostat:target,cap | hysteresis | custom`) and a required `aggregate_fn`, converting "every vector needs a bounded loop" from a per-track patch into a schema obligation. Right shape. Prose.

---

## 4. Transposition — the same machine on the other subsystems

All `[INFERRED]`. Each states the stack, the vectors, where noise enters, the collision constraint, and its boundedness check. The anchors are state dependencies, not vocabulary echoes.

**4.1 Faction — blocs, patronage, rivalries.** The F-stack exists as proposal (F1–F8: substrate-posture 6-enum, stat vector ⟨Mandate, Influence, Wealth, Military, Intel, Stability⟩ 1–7, Standing 0–7, nine-axis political vector). Missing is the **intra-faction slice** — Jordan's mandate item 3. Three additions: **F9 Bloc** (parents F1/F5/F7/tier) draws *k* = 2–4 **cascade roots**, licensed by the corpus itself — *"A faction may have multiple parallel cascade roots, one per institutional sub-hierarchy"* (`systems/factions/faction_behavior_v30.md:121`) — each with ⟨conviction-centroid offset, cohesion α-profile, patronage-degree, caste-gate posture, **benefit-when-faction-loses flag**⟩, the last being exactly the divergent-interest primitive the mandate asks for (a war-party that gains from a lost peace). **F10 Officer roster** runs §4.2 per post, conditioned on F9. **F11 Patronage-edge** draws client→patron edges with per-edge weight; noise picks who is whose client. **Collision constraint (the faction-scale Hold-Court rule): every faction carries ≥1 bloc pair such that any Directive pleases one and wrongs the other.**

Noise entry is not invented — the corpus supplies the formula: `effective_convictions(npc) = α·personal + (1−α)·effective(supervisor)`, `α = clamp(0.4 + α_seniority(−0.2..+0.4 by Standing) + α_institution(−0.2..+0.2))` (`faction_behavior_v30.md:139-160`). The generator draws the personal offsets; the cascade *is* the runtime template. **⚠ Verified: this executes nowhere** — `grep -rln "effective_convictions|cascade_root" *.py` returns **zero hits**. The corpus's own named design grammar, "weighted-cascade-with-noise", is entirely prose. **Boundedness:** patronage-degree and bloc influence need counter-pressure or they are the Guild-Influence ratchet one scale up.

**4.2 Officer (the generalized P13).** *Chapter 2 owns the ladder; this is how one is generated.* Vector: ⟨`role` (P10/F5), `power_base` ∈ {patronage, merit, kinship, bureaucratic, military, purchased, ideological}, `Standing` 0–7, `ethic ⟨α,β⟩` drawn near the settlement temperament **with spread**, 2 convictions, `ambition {goal, escalation ladder, timeline 3–5 seasons, fires_card, advance-predicate}`, `Disposition`, `leverage {wants, fears, secret}`, `Knots` (≥2 edges into the collision graph), `trajectory {if-blocked / if-conviction-violated / if-low-Disposition}`⟩. `power_base` is the sharpest field: `governance_type_registry_v1.md §2.2` calls it the flag that **"types the NPC's built-in downfall"** — every officer is generated already carrying the specific way they can be brought down, satisfying Ω-d by construction rather than by later balancing.

**How Goldenfurt actually drew the ethic — the tacit weight table P13 needs:** Kronmark is traditional ⟨0.3, 0.7⟩ and the cast realizes it *as a spread, not a stamp* — β (conduct): Hedda, Wessel, Greta; α (outcomes): Orsk, Tomas, Konrad. Institutions of law, faith and rite draw β; commerce, crime and bureaucratic enforcement draw α. Write that down and P13 is authorable. **Generator invariants** (verification findings made structural so they cannot recur): every officer reachable in a *well-governed* world, not only via failure states; every officer escalates on neglect, so doing nothing is not safe; every advance-predicate has ≥1 player-independent source **and** a per-season cap. **Both directions, one spine:** up = ambition clock → `fires_card`; down = cumulative *capped* censure clock with an always-available survivable escape (`Submit to audit`: 2 AP + Treasury, suspicion −2, `Reputation:Just` lowers the recall Ob, `event_deck.md:94-100`) plus a symmetric decay. **NERS-S caution:** the ladder is a deterministic ledger — dice on the *ticks* is the classic S-failure; the roll belongs only at the resolution fork. Inherit one gap deliberately: `npc.ethic` is currently flavour, read by no card or tick — make ≥1 resolution branch per officer read it, **or drop the field**.

**4.3 Mass battle.** Seed: map point / route edge → ⟨terrain, chokepoint, fort_level, weather prior, calamity band⟩ **plus the strategic cause** (which Directive, fracture or conquest produced this battle). Slices: army composition weighted by faction Mil/holdings/caste; commander = one §4.2 officer with power_base biased military, whose ethic conditions doctrine weights (β discounts atrocity options, α unlocks them at popular-support cost); unit quality ⟨discipline 0–7, morale, cohesion⟩ — the engine already holds the primitives, per-cell morale (`systems/mass_battle/sim/hierarchy/units.py:386-389`) and discipline tiers `1.0/0.7/0.4` at ≥5/≥3/else (`units.py:279`, verified); and a battle-pressure meter seeding a micro-deck drawn `1+⌊p/3⌋`-style. **Collision constraint:** each commander's ambition diverges from the faction-optimal plan on ≥1 decision — the divergent-interest agent as a generator invariant at battle scale. **Boundedness:** rout/morale contagion is a textbook §3 instance — **any contagion term ships with its rally term in the same commit.** **NERS-S caution:** this is the only target with a large executing resolver, so the generator sets **initial state only** and never injects noise mid-loop, or it manufactures dice-on-a-deterministic-ledger at the boundary.

**4.4 Personal-combat opponent.** Seed: scene context. Real state: combat writes Exposure **+1 quiet / +2 conspicuous / +3 public** into the territory (`systems/fieldwork/fieldwork_v30.md:104`, verified), so **the generator reads the field it will later write** — a state dependency, not a vocabulary echo. Slices: archetype weighted by present factions (guild bravo / templar / Niflhel knife / RM zealot / bailiff's men); capability drawn within the archetype's band and conditioned on settlement Weight (a Village tough is not a Seat duelist); intent ⟨lethality, capture, escape⟩ conditioned on ethic (a β-templar arrests, an α-smuggler runs); and a **hook slice** — every opponent carries a post-scene consequence, so no combat is state-inert. That last is the churn rule transposed and the cheapest available fix for the P→S matrix cell. **Verify:** graded recoverable outcomes, no bare-stat binary; leverage in-band across the capability range.

**4.5 Social-contest venue.** **The one target where "weights bias, noise chooses" already executes.** `VoteAtClose` resolves each juror as `sign(sharpness·gap + gauss(0, noise))`, defaults `jurors=7, sharpness=0.6, noise=0.8`, with `weighted_by_standing` aggregation over per-juror bench weights (`systems/social_contest/sim/contest/resolver.py:119-142`, verified). The venue generator's job is to **produce the parameters that resolver already consumes.** Slices: mode; bench vector ⟨k jurors, weight profile, sharpness, noise⟩ — noise is literally the juror-independence dial the resolver owns; stakes read from live Keys; audience temperament ⟨α,β⟩ biasing which proof types land. **Collision constraint:** ≥1 juror with a Knot to a cast NPC. **Boundedness:** VoteAtClose's per-juror noise *is* the anti-pin term — a lopsided room is near-unanimous, not deterministic. §3's fix, already shipped, in a sibling subsystem.

**4.6 Investigation site.** Seed: settlement + trigger; the canon path exists — a negative resolution Key *"raises the concealment inventory the Investigate verb draws from"* (`governance_ripple_substrate_v1.md §6.1`). Slices: site type from P7/P8; **concealment inventory** ⟨secret, holder, concealment Ob, evidence-type yield⟩ generated *from the cast*, since every P13 `leverage.secret` is a node (Goldenfurt's five: Tomas's smuggling, Hedda's shielding, Konrad's coin, Wessel's letters, Greta's organizers); evidence graph with corroboration edges and quality tags; witness slice. **Collision constraints:** ≥1 **keystone** node — a discovery that re-prices the whole cast (G505, `event_deck.md:78-85`) — and ≥1 **counter-lever** node, the pattern where investigating a small corruption neutralizes the institution watching *you*, which emerged accidentally in 12.6–30.8% of trials and **should be designed in, not left to emerge.** **Boundedness:** Exposure and concealment inventory are accumulators; both need burn terms.

**4.7 One anti-transposition, reported as a kill.** `skills/valoria-vector-audit/` is **not** a vectorized-noisy-slice generator: its "vectors" are TF-IDF lexical vectors over the documentation corpus, used for citation-graph diagnostics. No shared state, no shared invariant, no shared failure topology — it shares the word *vector* and nothing else. **Vocabulary collision; do not promote.**

---

## 5. The expressive-range gate — a runnable specification

VSG's pipeline ends in "verify" with four lenses and no instrument. Expressive Range Analysis (Smith & Whitehead 2010, P4 §7) is the instrument, fourteen years old and standard.

**Where it lives.** Kernel, content-blind, one owner: **`engine/generation/expressive_range.py`**, exposing `analyze(generator_fn, n, metrics) -> ERAReport` and `boundary_test(step_fn, noise=0.0, seasons, x0) -> BoundaryReport`. Gated by **`tests/valoria/test_generator_expressive_range.py`**.

**Does this guard earn its existence under CLAUDE.md §0.1 pt 5?** Yes, and the predicate is the reason: a guard earns existence when the defective artifact is load-bearing **on the game**. A generator's output *is* the settlements, casts and decks the engine runs on. This is not apparatus guarding apparatus; it is the category of `export_engine_params.py`'s blocking `--check` — apparatus by subject, producing something the game depends on.

**Step 1 — Metric selection**, the step most likely done wrong. Two to three metrics per slice level, **causally downstream of but not identical to the generation inputs**. The textbook's rule verbatim: *"strive to choose metrics that are as far as possible from the input parameters… Choosing a metric that is highly correlated to one used as an input parameter can only ever provide confirmatory results."* **If a metric is also a knob, it cannot be evidence** — so **do not plot α against β**, and **do not plot Π against Π**. Plot instead: realized pressure after conditioning, noise and thread resolution; the count of throughline-template branches that became eligible; factions with nonzero presence; Hold-Court collisions actually satisfied.

**Step 2 — Sampling with the doubling rule.** N runs per fixed configuration, varying only the seed. Start at N=300 (VSG's own disclosed count), double to 600, to 1,200; **stop when no bin's share moves by more than ~10% relative on a doubling.** Not stabilized by N≈2,400 is a finding, not a sampling failure. 300 was never justified as a sample size; it was a convention.

**Step 3 — Binning** at a resolution proportional to the *meaningful* granularity. For a clamped value like Π, bins must be fine enough near the ceiling to distinguish "clustered near the ceiling" from "pinned exactly at the ceiling" — the distinction a coarse histogram would have hidden at 298/300.

**Step 4 — Numeric collapse thresholds**, the part the literature does not supply off the shelf:
- **Modal-bin share** — fraction of runs in the single most populous bin. **≥50% = hard collapse, reject. ≥25% = soft collapse, design review before shipping the slice.** For scale: 298/300 = 99.3%, which would have failed at **N=30**.
- **Normalized entropy** `H_norm = H(bins)/log(num_bins)`. **Reject `H_norm < 0.4`.** This catches bimodal collapse — 50% at each extreme, nothing in the middle — that a modal-bin check alone misses.

**Step 5 — Controllability.** Re-run after perturbing exactly one upstream weight by a fixed step. **A slice is controllable if the perturbation moves the modal bin or `H_norm` by more than the run-to-run noise floor from Step 2.** A slice that does not respond to a real input change is not conditioned by that input, whatever the code claims — the check that catches fourteen unauthored tables stubbed to uniform.

**Step 5a — And the gate must be a test, not a protocol.** §2(d) is the reason this is stated rather than assumed: a guard that six readers believed covered `world.npcs` and actually pinned a call counter stayed green through a winner-changing perturbation. A verification *procedure* that lives in a design doc has strictly less force than that guard had. **P15 ships as `tests/valoria/test_generator_expressive_range.py` or it does not ship.**

**Step 6 — The boundary test. Build this first.** For any value with a designed equilibrium, run with the noise term at zero and **confirm the output is not deterministic-at-the-boundary**. §3.3 is this test, executed, in under a second, locating the bifurcation exactly. Ten lines, no heatmap, and the one that already found something.

**Step 7 — Report format.** Every shipped slice carries, beside its data file: metric definitions, N and the stabilization evidence, the heatmap, modal-bin share, `H_norm`, and the Step-5 controllability delta. That is exactly the *artifact* CLAUDE.md §0.1 pt 3 demands of an adversarial pass, produced for a generator instead of a diff.

**Two limits, so nobody oversells this.** Beyond 2 metrics, visualization has no standard answer; a full vertical stack exceeds 2D and needs paired projections chosen deliberately. And **ERA cannot certify that a non-collapsed, well-controlled generator produces settlements that feel meaningful** — the field has no measure for that; Compton names "interesting" and "characterful" as real targets with *no proposed measurement at all*. That residual closes only through human design review.

**Which brings the oatmeal in properly.** The methodology reached for the idea independently (*"Noise is the anti-oatmeal defense"*, `generation_methodology.md:95`); P4 supplies the canonical statement and the missing half. Compton distinguishes **perceptual differentiation** (the user can tell two artifacts are not identical — easy) from **perceptual uniqueness** (the artifact has a personality the user can recall — hard), and her conclusion is what VSG has not absorbed: **not everyone can be a main character.** A healthy generator produces mostly differentiated background and *concentrates* its budget on the few instances that carry weight. VSG spreads uniformly — fifteen paradigms for every settlement, thirty-seven times. The fix is P4 §S2's importance-gating: generate every settlement's vector cheaply, run the expensive slices (P13 roster, P14 deck) only above a dynamic importance threshold. And Compton's answer to *what* reads as alive is the lever DF and Qud both pull: **"evidence of process and forces"** — a place is interesting because something *happened* there, traceably. An argument for §4.4's hook slice and for provenance ancestry, not for more paradigms.

---

## 6. NERS on the generator itself

A generator sampling a weighted distribution **is a rolling engine** — a draw resolves the outcome — so NERS applies to the *sampling*. It does not apply to two of the six steps, and saying so is part of the verdict: **thread** is explicitly *"authored judgment, not sampling"* (`generation_methodology.md:103`) and **verify** is a procedure. Both route to consistency/playability discipline.

**N — PASS, with a live prune question.** Every draw does anti-oatmeal work and conditioning replaces a hand-written consistency pass, so no draw is redundant with a deterministic alternative that preserves individuation. But Jordan's ruling asks which paradigms survive a smaller-core cut (`settlement_generator_v1.md §7.3`), so N is not demonstrated per-paradigm. `[INFERRED]` weakest: **P6 (Altonian)**, which collapses to a P1 read for any interior settlement, and **P3 (Size)**, nearly determined by P4+P1 given `W_s = base(Type) + Prosperity + FacilityTier`. Inverse-N check: no over-correction risk — nobody proposes deterministic generation.

**R — CONDITIONAL FAIL at the calibration surface, and the "unfalsifiable" hedge is struck.** The draw mechanics are bounded (clamped categorical, fixed seed); the failure is one level up. The parameters are unvalidated by the design's own admission, and the record shows noise **masks** mis-signed and mis-capped parameters until a seeded sweep runs — twice, at opposite boundaries. R passes **only with P15 plus the per-vector boundedness check in the loop**. **R is falsifiable today (§3.3). It fails today.**

**S — PASS, conditional on one invariant that must be written as a rule.** The design's answer is compositional: *"Each scale is generated by the same machine"*, one content-blind kernel with per-scale data, stacks nesting up the ratified Settlement→Territory→Province chain. The F/R/P stacks differ in *data shape* (F flag-heavy, R vector-heavy) and that is fine. **The invariant: the kernel is single-owner, and a scale is added by adding DATA — tables, parents, constraints — never by forking the stepper.** A per-scale bespoke kernel, or a per-scale slice-table schema, is shape divergence in CLAUDE.md §10's sense and must be refused at review. Two residual S-risks: the two-engines fork whose sync device was never built, and the generation/runtime seam — the `provinces:` block has no production reader, so the two halves of the pipeline do not touch.

**E — PASS, with surface area as the standing risk.** The engine restates in one sentence and the authorial surface is data a designer edits without touching code. The risk is 15 paradigms × coupling groups × collision rules; the prune question is the E-hedge. Note §3.4's E-trap: fixing R by stiffening the controller (`k ≥ 1`) buys robustness by destroying legibility. **The E-preserving fix is capping accrual, not raising gain.**

**Separately, the event deck is its own rolling engine.** **N pass** — the draw does selection only; outcomes resolve through ratified resolvers. **R fail, twice** — the Π 7→8 band cliff flipping Intrigue→Crisis, and **uncapped `tag_modifiers`** (`sim_build_spec.md:124`), unbounded positive feedback on the weight vector. **S pass-shape** — event *selection* is the right place for a draw sitting on a deterministic homeostat. **E partial.**

> **Overall: N pass (prune open) · R conditional-fail, now executably so · S pass on the single-kernel invariant · E pass.** The method's portability to other subsystems is credible exactly insofar as each transposition ships with its own seeded falsifier rather than its own prose.

---

## 7. Cross-scale interaction — my assigned cells

| Cell | Mark | Locator | VSG's relation to it |
|---|---|---|---|
| **S→P** | **EMPTY** | `Settlement.npc_ids` empty on all 37; `governor_id` `None` on all 37; nothing queues a scene from a settlement | **P13 is the generator whose output fills this cell.** Chapter 1 owns the loader; this chapter owns the thing being loaded. Distance: one weight table (§4.2's α/β institution mapping) plus a sampler. |
| **S→S** | **EXECUTED (thin), live hole** | `systems/settlements/sim/adjacency.py:10` — **verified: `T16` appears exactly once, as a value in T1's set, with no key of its own.** The graph's only asymmetry, and T16 is Schoenland, the island republic whose sole edge is coastal | One-line fix, correct edge already in the geography file. Do it in passing; not leverage. |
| **S→F** | **PROSE-ONLY** | `Settlement.legitimacy` / `popular_support` declared at `registry.py:74-75`, zero readers and zero writers | Gates VSG's own P11/P12 verification — you cannot check whether the allegiance slice produces sensible politics when the field it writes is inert. |
| **F→P** | **BROKEN** | `combat_bridge.derive_parties` works and returns `None` rather than fabricating; `DISPATCH_COMBAT_BRIDGE` default OFF; no `queue_scene("combat", …)` call site exists | §4.4's opponent generator is the payload this cell would carry. |

**The seam fact binding all four:** the `provinces:` block VSG's seed reads has no production reader (§1.1b) and `Settlement.pressure`, what the runtime consumes, has no writer (§2c). **The two halves of the pipeline do not touch on `main`.** Every EMPTY or BROKEN cell above is one whose payload would have to be a person, and P13 is the specification of that person — which is the precise relationship between this chapter and Chapter 1: **Chapter 1 owns the missing object; this chapter owns the algorithm that would produce it.**

---

## 8. The blocker register, triaged — and a settled question still blocking a build

Every *decision* row is closed; what remains open is the **execution spine**. Applying the 2026-08-24 five-test ladder, each closure with its citation:

| Row(s) | Disposition | Citation |
|---|---|---|
| D1, B1, B10, B12 | **CLOSED — superseded by ruling** (test 1) | ED-IN-0046 / ED-IN-0047; `scale_hierarchy_v1.md` |
| D2 | **CLOSED — answered by code** (test 5) | `Settlement.ap = 2 + facility_tier (+1 Seat/Cathedral)` is live |
| E6/B3 type-taxonomy | **CLOSED BY CODE** | verified `registry.py:45-48` — `LEGAL_TYPES` includes Village, Fortress-City, Cathedral-City, enforced as a load gate. Per §0.05 the code *is* the taxonomy. |
| B9 geography stale | **CLOSED** | verified: 17 provinces, 37 settlements, S-006 = Goldenfurt |
| D3 Compact schema | **Decision closed; fix never landed — but dormant** | verified `ledger.py:30` declares `TAG_KINDS` and `ledger_add` (`:47-58`) **validates nothing**; the ledger has no production writer, so it cannot fire. **Answer-by-architecture: add the whitelist in the commit that gives the ledger its first writer.** Not a Jordan item. |
| D5, D6, E11 | **Decisions closed; code absent** | no suspicion/recall code on `main`; the executing instance went to `FORK:1e4c6f4` |
| **E1+E3+E7** | **GENUINELY OPEN — highest-leverage build item** | no homeostat code anywhere; §3.4 supplies the arithmetic showing the bundle is necessary, not prudent |
| **E5/B4 L/PS** | **STILL OPEN, unchanged, still #1** | `registry.py:74-75`, verified zero-reader/zero-writer |
| B8 deck engine S2–S6 | **OPEN; re-scope** | the 13-card harness went to `FORK:1e4c6f4`; S0–S1 built, S2–S6 zero code |
| B11 `engine_clock` | **STILL OPEN** | `references/module_contracts.yaml:1387` — "its home doc remains unlocated" |
| E2, E4, E8, E9, E10 | **OPEN-IF-PURSUED** | none authored; blocking nothing on `main` |

**The register defect worth its own paragraph.** Jordan ruled **B2 on 2026-07-13**: S-006 = Goldenfurt, S-007 = Lowenskyst Fortress, followed by a full 37-settlement geography reconciliation. I verified the ruling landed in the data (`valoria_geography_v30.yaml:287-288`). But **four live documents still present the tri-booking as an open precondition**: `settlement_generator_v1.md:162` — *"Precondition: fix S-006's tri-booking first — the seed itself is currently ambiguous"*; `generation_methodology.md:186` — "The seed itself is triple-booked"; `generation_sourcebook_v1.md:173` and `:186`, which list it as open and "cheap, high-leverage" **while the same file's row at `:155` records it as RESOLVED**; and `ners_vsg_reconciliation_v1.md:67`, which says it "now blocks *two* independent bodies of work."

So the calibration fixture of the entire generator is gated, in prose, on a question that was answered — and the sourcebook contradicts itself four rows apart. Under §0.05 this changes nothing about what is true: the code and the data are correct. But it is a live demonstration that **a settled question left in prose keeps blocking work**, which is exactly the failure the five-test ladder exists to end. Close all four with the citation. Session work, not a Jordan item.

---

## 9. Recommendations

**R1 (headline) — Ship VSG behind an executing expressive-range gate.** The architecture is validated by four independent precedents; the calibration is validated by nothing; the gate is what makes shipping the first safe despite the second. Build **`engine/generation/expressive_range.py::boundary_test`** first — Step 6 only, ten lines, no heatmap — gated by **`tests/valoria/test_generator_boundary.py`**, parameterized over a registry of every value carrying a designed equilibrium. Then add `analyze()` for Steps 1–5. *Cost:* half a day, then about a week, plus metric selection, which is a design conversation not a coding task. *Risk if skipped:* the corpus repeats the CG-1 → 298/300 sequence a third time.

**R2 — Build the sampler primitive, not "the generator."** **`engine/generation/sampler.py::weighted_choice(rng, table, tau)`** plus **`seeded_stream(map_point, paradigm_index, campaign_salt)`** for the sha256 rule; then convert `npe.py`'s uniform categoricals (`:273`, `:280`, `:322`) to call it, tables starting uniform and filled in slice by slice. *Cost:* small — the conditioning scaffolding and two-tier structure already exist and run. *Golden risk:* **real, argue it separately.** Any change to a `world.rng` draw can move the seeded goldens; a uniform table reproduces current behaviour only if draw order is preserved. Verify that first, re-pin in its own commit, and say out loud that CLAUDE.md §7 flags the re-pin path as uncontrolled.

**R3 — Author the fourteen missing weight tables as DATA, starting with P12→P13 ethic assignment.** `systems/settlements/generation/p13_ethic.yaml`: §4.2's reconstructed mapping (law/faith/rite → β; commerce/crime/enforcement → α) with a spread parameter Δ. Highest-value single table — the exemplar already demonstrates it, and it feeds `temperaments.py`'s live α/β. *Cost:* authoring, not engineering. *Prerequisite:* fix the P1 `spiritual_weight` range defect (`settlement_generator_v1.md:45`) or Himmelenger generates wrong.

**R4 — Give `Settlement.pressure` a writer, and the E1+E3+E7 bundle in the same commit.** `systems/settlements/sim/pressure.py::step(settlement, world) -> float`, implementing the homeostat **with** a capped accrual term (E3) and a genuine release path (E7). §3.4 gives the acceptance criterion in closed form: **at the design's own accrual (~3.0/season from six ambition clocks alone), no proportional gain in the stable range `k < 2` holds Π out of the crisis band — cap accrual below ~1.0/season first.** Gate with R1's boundary test in the same commit. *Cost:* the code is a day; the calibration is the work. *Do not ship E1 alone* — not caution, arithmetic.

**R5 — Make `decay_fn` a schema obligation, not a per-track patch.** `governance_type_registry_v1.md:245,265` already proposes it; make it real in **`engine/generation/gauges.py`** — a registry entry per continuous track with `decay_fn ∈ {none, linear:rate, homeostat:target,cap, hysteresis:thresholds}`, `none` permitted **only** with an explicit justification field. §3.1's seven instances become seven data rows instead of seven rediscoveries. *Payoff:* retires the T-04 class, not its instances.

**R6 — Cap `tag_modifiers`.** One clamp in the deck's weight computation; closes an unbounded positive-feedback loop on the sampler before it ever runs.

**R7 — Make the golden guards observe the state, not the call counter.** §2(d) shows `npc_counter` is the wrong observable. Pin **`len(world.npcs)`** alongside it in `tests/valoria/test_pipeline_reach.py` and `engine/tests/test_f7_smoke_oracle.py` — a guard must be able to observe the failure it excludes (§0.1 pt 2), and this one guards the game's seeded output, so it passes §0.1 pt 5's load-bearing predicate. *Cost:* two lines and one re-pin. *Corollary for R2:* the golden channel is now **known** — `npe.simulate_npc_actions` drawing `world.rng` at `systems/overview/sim/accounting.py:139` — so R2's "verify draw order first" is a specific instruction, not a caution.

**R8 — Close the four stale S-006 rows with their citation, in one editorial commit.** Zero engineering cost, and it unblocks the generator's calibration fixture in the only place it is still blocked: prose.

---

## 10. Falsifier, verification, coverage

**My falsifier, run.** *If any `.py` samples a weighted slice table to produce a settlement, a cast or an event, VSG executes and this chapter's premise is wrong.* At HEAD: `random.choices` / `np.random.choice` / `weighted_sample` / `rng.choices` → **zero hits** across `engine/` and `systems/`; all ten `rng.choice(...)` calls are bare uniforms. **The premise holds.** The one honest exception is `temperaments.py`, reported in §2(a) with the correction that it has **zero production callers and zero tests** — executable, not executed.

**Second falsifier, run, and it changed a conclusion.** *If the Π boundary test cannot run without a kernel, R is unfalsifiable-by-execution.* I ran it against the formula as arithmetic (§3.3): bifurcation at accrual = 1.0 exactly, in under a second. **R is falsifiable today, and it fails.** The upstream "unfalsifiable" hedge is struck.

**Locators I verified myself at HEAD**, by reading or executing rather than trusting an upstream report: `temperaments.py:33-38` and `:126-131` (plus executed); `registry.py:79` and exactly two `.pressure` references tree-wide; `registry.py:45-48` LEGAL_TYPES; `registry.py:216-241` `populate_from_geography`; `valoria_geography_v30.yaml:287-292` and the parsed 17/37 counts; the `provinces:` block's zero production readers; `ledger.py:30` + `:47-58` (validates nothing); `adjacency.py:10` (T16 as value, never as key); `contest/resolver.py:119-142` (jurors=7, sharpness=0.6, noise=0.8); `units.py:279` (1.0/0.7/0.4); `faction_behavior_v30.md:121,139-160` **plus zero code hits for `effective_convictions`/`cascade_root`**; `governance_type_registry_v1.md:104,147,148,151,245,265`; `ners_vsg_reconciliation_v1.md:43,48-50` verbatim; `sim_build_spec.md:56-57,122-145`; `event_deck.md:3,5,11-19`; `settlement_generator_v1.md:24,28-31,45,63-73,162,174-176`; `settlement_layer_v30.md:160`; `npe.py:76,186-208,226-330`; `fieldwork_v30.md:104`; the four stale S-006 rows; and, adopted mid-draft and re-checked before use, `engine/tests/test_f7_smoke_oracle.py:267` (live `GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}`) against `:75` (the historical line) and `:262-265` (the provenance rule), plus `systems/overview/sim/accounting.py:139` (`simulate_npc_actions` inside the accounting step). That is twenty-plus checked, well past the ten required. **No win-share figure is used as evidence anywhere in this chapter**; the pair above appears only as §2(d)'s worked example of the provenance failure.

**Two that did not check out cleanly, reported rather than smoothed.** (1) **`settlement_generator_v1.md:45` is inconsistent with its own data** — P1 declares `spiritual_weight 0–2`; the live YAML has T9 = 4, T15 = 5. Not a citation error but a **content defect** that would silently mis-generate the Cathedral City; newly located here. (2) **"`temperaments.py` is the one slice that executes" is half right** — implemented, importable, and I ran it, but with no production caller and no test. Under §0.2 that is not "executes," and anyone repeating the claim should repeat the qualification.

**What I did not cover.** The officer *ladder* — rungs, Standing progression, censure/demotion apparatus, ED-FA-0018's flat Crown-Administrative surface (Chapter 2). The person loader's implementation and its golden re-pin (Chapter 1). The dice/degree/obstacle substrate (Chapter 3). The precedent-failure catalogue (Chapter 5). Within my own lane: `settlement_layer_v30.md` read only in targeted excerpts; the archived emergent-narrative-engine corpus cited only through VSG's own quotations; the governance-compendium event cards and the twelve compact deck rows not transcribed. Not verified: whether the D4 Mandate rename executed anywhere, whether PP-726 carries its supersession banner, or the promised 500-seed regime check against the migrated geography — **no artifact found** for the last. I executed the boundary test and `temperaments.py` and parsed the geography YAML; **I ran no campaign**, so every statement about campaign behaviour rests on locators and greps, not `mc_v18` output. Per the run's provenance constraint, this chapter cites no `PP-NNN` as evidence — only `ED-IN-0046` / `ED-IN-0047`, the rulings that closed D1–D6 and B1.
