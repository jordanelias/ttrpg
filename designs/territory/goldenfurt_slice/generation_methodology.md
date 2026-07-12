# Goldenfurt — Generation Methodology (how this slice was made)

## Status: ANALYSIS / working notes (retrospective, Jordan-vetoable)
## Date: 2026-07-12 · Lane: SE (settlements) · Companion to: `README.md`, `npc_cast.md`, `event_deck.md`, `sim_build_spec.md`, `verification_findings.md`

**What this is.** A retrospective, honest reconstruction of the *authoring technique* that produced
this slice — the **vectorized-slice-stack with noisy throughlines**. The other five files describe
the slice's *content* and how it *runs*; this one describes how it was *generated*. It claims no new
canon; it documents provenance and gives a reproduction recipe so the next settlement is a repeatable
procedure rather than a session ritual. (README, honestly: this slice was "authored directly — the
authoring workflow died three times on session/rate/spend limits." That means the stack below was
executed as in-session reasoning over committed tables, **not** as a committed tool. Reifying it is
the recommended next step, §6.)

---

## §1 The technique in one diagram

Conditioned procedural generation by a **factorized weighted-sampling stack**:

```
  SEED       a location on the Valoria map (valoria_geography_v30.yaml, 1920×2880 canvas)
    │
    ▼
  CONDITION  the point lands in a province → inherits its geopolitical frame
             (faction owner · region/sub · fort_level · spiritual_weight · proximity_calamity · starting_pros)
    │
    ▼
  STACK      quasi-independent SLICES, each a weighted distribution over its own variables:
             ├─ settlement-type slice     (8 types × stat/manager profile)         settlement_layer §1.2
             ├─ economy-bias slice        (Prosperity/Trade/resource; toll vs grain vs mine)   §1.3 + geo
             ├─ governance slice          (Provincial Authority + subnational managers; facility_tier→AP)
             ├─ religion slice            (4 independent Church-infra axes + spiritual_weight)  §1.5
             └─ culture/temperament slice (5-typology α/β weight pair)             territory_temperaments §1
    │
    ▼
  NOISE      each slice sampled stochastically — the weights BIAS, they do not DETERMINE
    │
    ▼
  THREAD     the independent draws are woven into ONE coherent settlement:
             collision-wired NPC cast (npc_cast.md) + event deck (event_deck.md) + Π homeostat (sim_build_spec §5)
    │
    ▼
  VERIFY     an adversarial pass tries to break the threaded product (verification_findings.md)
```

- **Vectorized** — each slice is a *vector of weighted variables* (temperament = ⟨α,β⟩; church =
  ⟨building, templar, inquisitor, governor⟩; type = ⟨prosperity, defense, order, manager⟩).
- **Stack** — slices compose as independent layers, so a settlement is a *product of small conditional
  distributions* rather than one hand-authored blob. Additive authoring, combinatorial output.
- **Noisy throughlines** — a *throughline* is one coherent draw threaded through the whole stack (a
  settlement is one line through economy × governance × religion × culture); *noise* is the stochastic
  sampling that individuates each throughline while the geographic conditioning keeps it plausible.

Genre precedent is explicit in `settlement_layer_v30.md` (KOEI ROTK officer-city assignment; CK3
barony→kingdom hierarchy). The Valoria twist: the stack is **conditioned top-down by a real map**,
not generated bottom-up from noise fields.

---

## §2 The slices, grounded — with Goldenfurt as one realized draw

Every slice exists as a canonical weighted table. Goldenfurt is the value each one took:

| Slice | Canonical source | Weighted variables | Goldenfurt's draw |
|---|---|---|---|
| **Geography seed** | `valoria_geography_v30.yaml` | anchor · polygon · `fort_level` · `spiritual_weight` · `proximity_calamity` · `starting_pros` · faction · region/sub | Kronmark (T2), Crown, Eastern-Lowlands Heartland, `spiritual_weight:1`, `proximity_calamity:4`, `starting_pros:4`, "Italian-coded farmland" |
| **Type** | `settlement_layer §1.2` | function × stat profile × natural manager (8 types) | **Town** — agricultural base; Prosperity/Population; Provincial-faction manager |
| **Economy bias** | `§1.3` + geography | Prosperity/Trade/resource weighting; chokepoint rents | **breadbasket grain + a tolled river ford** (the toll is what makes the Guild collide) |
| **Governance** | `governance_play_redesign_v1` + `§1.4` | Provincial Authority owner; subnational claimants; `facility_tier → AP=2+tier` | Crown = PA; Guild/Church/RM/Niflhel subnational; facility_tier 1 → AP 3 |
| **Religion** | `§1.5` four Church axes | Building (None/Chapel/Church/Cathedral) · Templar · Inquisitor · Church-Governor | **Chapel** — the low rung → the "Geneva trap" upgrade throughline (G204→G603) |
| **Culture/temperament** | `territory_temperaments §1` | 5-typology, each an ⟨α,β⟩ pair | Kronmark = **traditional ⟨0.3, 0.7⟩** → "rural devout populace," conduct-weighted |

The coherence is the *conditioning* working, not luck. A `spiritual_weight:1`, `traditional`,
Crown-breadbasket Town on a ford **is** a place where "the Guild wants the toll, the Ministry wants
the levy, the Church wants the souls, the RM keeps the old rites, and Niflhel smuggles under all of
it" (README §Why Goldenfurt). Seeding first and slicing second is what makes those five collisions
*organic rather than bolted on*.

---

## §3 Why it works — the generative shape

The stack is a factorized joint distribution `P(settlement) = P(geo) · ∏ᵢ P(sliceᵢ | geo)`. Three
properties earn its power:

1. **Additive authoring, combinatorial output.** ~6 small weighted slices (a handful of variables
   each) yield `∏` distinct settlements — ≈ 15,000 nominal profiles from ~30 authored rows. This is
   the generation-time twin of the runtime engine's "grammar × lexicon, state binds the slots" load
   argument.
2. **Conditioning buys coherence for free.** Because every slice draws *given the geography*, the
   marginals correlate correctly with no hand-written consistency pass: calamity-adjacent provinces
   (T6/T13/T15) draw `outcomes-only`; a border-fortress province draws high `fort_level`; a devout
   heartland draws Chapel-not-yet-Cathedral. The weights encode *what a geography tends to produce*.
3. **Noise is the anti-oatmeal defense.** Identical *type* + identical *temperament* still diverge —
   the noisy draw picks different subnational-manager strengths, actor rosters, economy weightings.
   Without noise you get 8 template towns; with it, individuated ones.

The **threading** step is where the slices stop being independent and become one playable object: the
NPC cast is authored so the draws *collide* (Hedda/law vs Orsk/commerce is the central rivalry — "any
`Hold Court` ruling pleases one and wrongs another"; `npc_cast.md` §collision map), and the event deck
turns each collision into a card whose responses write Ledger tags and Π deltas (`event_deck.md`
churn rule). Threading is authored judgment, not sampling — it is the step the generator cannot fully
automate (§5.C).

---

## §4 How generation-time feeds the runtime engine

This generator and the runtime **arc-vector / churn engine**
(`designs/audit/2026-07-05-emergent-narrative-engine/`) are the two halves of one pipeline:

- **This stack (generation-time)** produces the *substrate*: a fully-specified settlement with its
  stat vector, temperament, subnational footholds, actor roster, starting religion/governance state.
- **The arc-vector engine (runtime)** *binds its ~13 throughline templates to that substrate* — "a
  template bound to THIS settlement's circumstances … is particular by construction" (churn-engine
  v2 §2). Goldenfurt is exactly the binding that makes a generic template a particular story.

So: **noisy weighted slices generate the world; vectorized throughline templates animate it.**
Goldenfurt is the one place both halves were carried end-to-end far enough to test.

---

## §5 Failure modes — and this slice's own verification as the evidence

The stack produces **plausibility, not correctness**. Coherence is conditioned-in; balance and
playability are *not*, and must be verified out. The 32-finding adversarial pass
(`verification_findings.md`) is a catalogue of exactly what a noisy weighted stack produces when the
weights or the threading are wrong:

- **A. Coupled slices sampled as independent.** Religion and governance are coupled
  (`church_attention` drives the Suppress Directive), yet the threaded spec **omitted 7 fields the
  slices jointly required** (`sim-F1/2/3/5/7/9`: `active_directive`, `religious_building`,
  `church_attention`, `governor_emergence`, `treasury_source`, `open_needs`). Independent sampling of
  coupled slices is the structural cause of that whole finding class.
- **B. Weight-sign / calibration errors hide under noise.** The Π homeostat weight was **mis-signed**
  (`CG-1`: it pinned a quiet town toward Π=0 instead of restoring toward the dramatic band). Output
  variance masks a systematically wrong weight until a *seeded sweep* runs. The 500-seed stress test
  (`tests/sim/settlement_mgmt_stress_01/`) independently confirms the same at scale — a
  **negative-death-spiral bias is the default regime** (mean 3.6 of 4 factions eliminated), and
  nothing flagged it. **The weights are guesses pending a sim sweep** (`sim_build_spec §10`).
- **C. Threading can manufacture dominated choices.** Weaving independent draws into one decision
  surface produced a no-acceptable-out vise — `deck-F3` (G204 Geneva trap), an Ω-d violation. The
  stack has no built-in playability guarantee; it is imposed *afterward* by adversarial verification.
- **D. One-way ratchets from unbalanced slice interaction.** The suspicion track was purely reactive
  (`npc-F1`) and the recall a death-spiral (`deck-F2`) — emergent from threading Crown-authority ×
  NPC-ambition without a restoring term. Caught only by the adversarial pass.

The through-line: **generation gives you a plausible town; verification is not optional.** That is why
this slice ships with a mandatory adversarial stage and why the reconciliation addendum
(`designs/audit/2026-07-12-settlement-season-stress-sim/`) recommends grounding future runs in
Goldenfurt rather than re-inventing settlements.

---

## §6 Reproduction recipe (reify the tacit stack)

To make the next settlement a procedure, not a ritual:

1. **Seed** — pick (or randomly draw) a map point in `valoria_geography_v30.yaml`; read off its
   province frame (faction, region/sub, `fort_level`, `spiritual_weight`, `proximity_calamity`,
   `starting_pros`).
2. **Slice** — for each slice in §2, sample its weighted table *conditioned on* the seed. Record the
   draw and the weights used (so a re-run is reproducible under a fixed seed).
3. **Thread** — author a collision-wired cast (each NPC: ambition = autonomous advance; leverage =
   player grip; a `fires_card`) whose drives collide on the four common verbs (`Hold Court`,
   `Keep Order`, `Levy`, `Investigate`); build the deck so every card writes ≥1 Ledger tag and ≥1 Π
   delta (`event_deck.md` churn rule).
4. **Verify** — run the 4-lens adversarial pass (deck-balance · NPC-collision · churn-integrity ·
   sim-completeness) *before* trusting the output; fold the clear bugs, track the design-revisions.

**Recommended build:** promote steps 1–2 into a committed `settlement_generator` (weighted slice
tables → seeded draw → threaded settlement pack), so the sampler is a tool with a fixed cross-platform
seed, not an in-session process that "died three times."

---

## §7 Honesty notes

1. **The composite sampler is not committed.** Every *slice* is a canonical table (temperament, type,
   church axes, geography); there is no `settlement_generator` doc or tool in `designs/territory/`
   that samples a random map point through the whole stack. The evidence (README) is that the stack
   was executed as in-session reasoning over those tables. §6 is the fix.
2. **The seed itself is triple-booked.** `valoria_geography_v30.yaml` assigns **S-006/S-007 to T3
   Lowenskyst (Border Fortress)**; `settlement_layer_v30.md:330` lists "**S-006 Goldenfurt Town
   spoke**" and `:912` lists "**S-006 Lowenskyst Fortress**"; the temperament rationale + README place
   Goldenfurt in **Kronmark T2**. So the very id/province this slice seeded from is inconsistent across
   three canonical files — an editorial finding worth an ED before any re-run seeds from S-006.
