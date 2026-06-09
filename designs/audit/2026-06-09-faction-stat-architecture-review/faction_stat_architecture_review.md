# Faction Statistics — Architecture Review Across Scales & Substrates
**Audit deliverable · 2026-06-09 · objective review per Jordan's hypothesis (faction stats as dynamic derivation; retire stats-derived-from-faction-stats)**

Grounded in a session read of the *current* mechanisms — the Universal Key Substrate (`key_substrate_v30` PP-687),
the Domain Echo implementation (`sim/cross_scale/domain_echo.py` + `scale_transitions_v30 §5`), the Zoom In/Out
rippling (`scale_transitions_v30 §3–§4`), the d+σ resolver (`domain_action_resolver_spec` / ED-874), the LPS-2e
Mandate aggregation (`settlement_layer §1.8`), and the 2026-06-09 attribute flattening. This is a review, not a
ratification: it states where the hypothesis holds, where it needs qualification, and what it costs.

---

## 0 — Verdict (first)

**The hypothesis is largely correct and NERS-positive, with one real qualification.**

- **Part (a) — "we may no longer need stats *derived from* faction statistics":** **Confirmed.** The `derived_stats §14`
  capital layer (Reputation/Treasury/Levies/Discipline, and the stale Legitimacy) is a depleting-resource layer built for
  a *bare-stat-pool* resolution economy that **two later changes obsoleted**: the d+σ resolver (uses the raw 1–7 stat as
  leverage, needs no ×k gauge) and the settlement/territory substrate (where the real economy/manpower already live).
  The capitals are subsumed — relocate their genuine semantics down to the settlement substrate; retire the rest.
- **Part (b) — "faction statistics as a dynamic derivation from settlement/territory aggregates + national actions/events":**
  **Confirmed as the right direction**, and it is simply the LPS-2e Mandate model generalized to the whole lineup.
  **Qualification:** the generalization is clean for **Mandate, Wealth, Military, Stability** (each has an obvious
  settlement/territory basis) but **not uniform** — **Influence** and **Intel** have weak settlement bases and are more
  *national/institutional*; they need an explicit derivation basis (national-event-driven), not a forced settlement sum.

The unifying move: **invert primacy.** Today faction stats are primitive and settlements partly feed one of them
(Mandate). The proposal makes the **settlement/territory substrate primitive** and **every faction stat a derived
readout** of it plus a **national-event modifier ledger**. LPS-2e already did this for one pair; the rest are the
backlog of the same inversion.

---

## 1 — The current architecture (three stacked, partly-contradictory models)

Faction stats today sit at the intersection of three layers built at different times:

**Layer 1 — base stats as d+σ leverage inputs (current, ED-874, 2026-05-30).**
Faction stats `Influence / Wealth / Military / Intel / Stability` (1–7) and `Mandate` are the **acting_stat** in the
resolver: `M = acting_stat − difficulty`, `P_success = clamp(0.50 + 0.10·M, 0.05, 0.90)`. The 0.10 slope is the
leverage — a flat +10%/stat-point. Examples: Assert = Influence vs Ob 2; Suppress = Mandate vs `floor(Church-L/2)+1`;
§1.4 Accounting Stability Check = Stability. **The resolver consumes the raw 1–7 integer.** It has no use for a ×k gauge.

**Layer 2 — base stats as the *max* of a depleting "capital" gauge (`derived_stats §14`, pre-ED-874).**
Each base stat sets the ceiling of a resource that depletes in play:

| Base stat | Capital | Max | Semantics today |
|---|---|---|---|
| Wealth | Treasury | ×100 | spendable gold; at 0 → cannot Muster/Fortify; max drops if Wealth drops, current retained |
| Military | Levies Available | ×2 | fielding **cap** (not spendable); "X/Y fielded" |
| Influence | Reputation | ×15 | depletes; at 0 → diplo/Intel +1 Ob; sustained 0 → Influence −1 |
| Stability | Discipline | ×10 | depletes; at 0 → Stability check, Stability −1 |
| **Mandate** | **Legitimacy** | **×20** | **STALE — inverted by LPS-2e (see Layer 3)** |

This is a coherent "current/max resource economy" — it predates d+σ, when faction actions rolled **bare stat pools** and
needed a spendable/erodable currency to give the abstract 1–7 stats texture.

**Layer 3 — one stat already inverted to a settlement aggregate (LPS-2e, `settlement_layer §1.8`, 2026-05-30).**
`Mandate = size-weighted saturating aggregate of settlement (0.5·L + 0.5·PS)`. Here the settlement stats (L, PS) are
**primitive** and Mandate is **derived**. This is the exact opposite of Layer 2's Mandate→Legitimacy treatment, and is
why the flattening found C-1 (the derivation arrow reversed between docs) and C-2 (Mandate declared derived yet written
at 78 sites + read as a d+σ input).

**Layer 4 — the upward ripple writes faction stats directly (Domain Echo, `scale_transitions §5`).**
A scene that meets Sufficient Scope (§7) emits a Domain Echo: Overwhelming ±2 / Success ±1 / Failure −1 to the target
faction's **`most_relevant_stat`** at scene end (cap ±2/stat, PP-329 one Echo/faction/scene). **This writes the faction
stat as a scalar delta** — the literal F1 mechanism, and the upward half of the bidirectional ripple.

**Layer 5 — the substrate underneath is vectorized, not scalar (`key_substrate_v30` PP-687).**
Every event is a Key with an `impact_vector` (signed projection onto the 4 Conviction axes) + `symbolic_dimensions`,
feeding actor `armature_position`. Effects on *actors* are axis-projected vectors. Faction-stat scalar deltas (Layers 2/4)
are a **scalar idiom layered on a vector substrate** — they coexist but were not designed together.

---

## 2 — Provenance: why Layers 2 and 4 are vestigial

Jordan's "these decisions predate the σ-leverage and the existence of settlements/territories" is the load-bearing
observation, and it checks out:

- **Layer 2 (capitals) predates the d+σ resolver.** When faction actions were **bare-stat pools** (roll N=stat d10s),
  a faction needed spendable/erodable resources (gold, troops, standing) to feel like more than an integer. The ×k
  capitals supplied that economy. The d+σ resolver (ED-874) made the **raw 1–7 stat itself** the leverage term — the
  scaled gauge no longer participates in resolution. Its only remaining job is the depletion economy.
- **The depletion economy predates settlements/territories.** Before the settlement layer, a faction *was* its abstract
  stats, so "Treasury = Wealth × 100" was the only place economy could live. **Once settlements exist** — each with
  Prosperity → Local Economy (gold), Defense/Fort → Garrison Strength (manpower), Order → Public Order (compliance) —
  the faction's economy, manpower, and order are **already represented, concretely, one scale down.** The faction-level
  ×k gauges are now a *second, parallel* representation of the same things the settlement substrate holds (and C-3, the
  Treasury double-source, is exactly this collision surfacing).
- **Layer 4 (Domain Echo direct write) predates LPS-2e.** A scene→faction scalar delta was the natural upward ripple
  when faction stats were primitive. Once Mandate became a settlement aggregate (LPS-2e), a direct `Mandate ±1` write
  became incoherent — and by the proposal, every faction-stat direct write becomes incoherent for the same reason.

So Layers 2 and 4 are not wrong-as-built; they are **artifacts of an earlier substrate** that the d+σ resolver, the
settlement layer, and LPS-2e have each independently undercut. LPS-2e already paid the inversion for one pair and left
the rest stranded — that stranding *is* the C-1/C-2 contradiction.

---

## 3 — The proposed architecture

**One model for every faction stat:**

```
faction_stat[s]  =  AGGREGATE_s( relevant settlement / territory stats over holdings )
                 ⊕  Σ_k  national_event_modifier_k     (decaying Key-ledger contributions)
```

- **The aggregate** is the structural base — what you hold and how well you hold it. Re-derived (cached at load, not
  per-frame — K8) whenever a constituent settlement/territory stat changes. This is the LPS-2e formula generalized:
  size-weighted, saturating, per stat.
- **The national-event modifier ledger** is the agency layer — treaties, decrees, campaigns, successions, and
  scene/Thread Domain Echoes **routed here instead of writing the stat**. Each is a Key (it already fits the PP-687
  schema); contributions decay so events fade rather than permanently ratcheting the stat. This preserves
  faction/national-level choice (the half of Jordan's hypothesis that is *not* about settlements).
- **Domain Echo is reconceived, not deleted.** A scene's outcome ripples up by (i) changing the **settlement/territory
  stat at the scene's locus** (the natural, located effect) and/or (ii) appending a **national-event modifier Key**; the
  faction stat then **re-derives**. The ripple still flows up — but *through* the substrate, one scale at a time, rather
  than teleporting to a faction integer. This is strictly more consistent with "ripples moving both up and down."
- **The d+σ resolver is unaffected in form.** It reads `acting_stat` at resolution time; reading a *derived* value is
  fine — only *writing* a derived value was the defect. `M = acting_stat − difficulty` still holds; `acting_stat` is now
  a derived readout.

### 3.1 Per-stat derivation map (proposed)

| Faction stat | Settlement/territory basis (aggregate) | National-event modifiers | Clean? |
|---|---|---|---|
| **Mandate** | size-weighted Σ settlement (0.5·L + 0.5·PS) — **already LPS-2e** | recognition, decrees, collapse | ✅ done |
| **Wealth** | Σ settlement Local Economy (Prosperity×50) | trade deals, war indemnities, sanctions | ✅ clean |
| **Military** | Σ settlement Garrison Strength (Defense×20+Fort×30) + territory count | muster orders, casualties, mercenary hire | ✅ clean |
| **Stability** | f(Σ settlement Order, province Accord) | successions, coups, suppressions, treaty breaches | ✅ clean |
| **Influence** | weak — partial f(settlement L/PS reach, capital prominence) | **dominant**: diplomacy, alliances, parliamentary standing | ⚠ national-leaning |
| **Intel** | very weak — no natural settlement basis | **dominant**: spy networks, institutions (Council of Ten, nuncios) | ⚠ national/institutional |

The **qualification is real and must not be papered over**: Influence and Intel do not reduce to a settlement sum. For
them the derivation is *mostly the national-event ledger* over a thin (or zero) structural base — which is fine, and
still "a dynamic derivation," but the basis is institutional, not territorial. Forcing a settlement aggregate on Intel
would be a fabricated mechanic.

### 3.2 What happens to the §14 capitals (part a)

| Capital | Disposition under the proposal |
|---|---|
| **Treasury** (spendable gold) | **Relocate down.** Spendable gold is the Σ of settlement Local Economy; spend against the settlement substrate, not a faction-level `Wealth×100`. C-3 dissolves (one source). |
| **Levies Available** (fielding cap) | **Relocate down.** Fielding capacity = Σ settlement Garrison/Population, not `Military×2`. |
| **Reputation** (Influence gauge) | **Retire as a separate gauge.** Its movement is now *the derived Influence moving* (a bad diplomatic event lowers the national modifier → Influence drops). Re-home the one threshold effect ("at 0 → diplo +1 Ob") to a low-Influence band. |
| **Discipline** (Stability gauge) | **Retire as a separate gauge.** Same logic — derived Stability already moves; re-home "at 0 → Stability check" to a low-Stability band. |
| **Legitimacy (=Mandate×20)** | **Delete the row** — it is the inverted-arrow artifact (C-1). Legitimacy is a *settlement* base stat (LPS-2e). |

Net: the entire `derived_stats §14` faction-stat→capital table is reconceived. The genuine semantics (spendable gold,
fielding cap, low-stat penalties) survive — **re-homed to the settlement substrate or expressed as bands on the derived
stat** — and the redundant scalar scalings disappear.

---

## 4 — How this resolves the flattening contradictions

- **C-1 (Mandate arrow inverted)** → resolved: there is one direction (substrate → faction). `§14`'s Mandate/Legitimacy
  row is deleted; the model is uniform.
- **C-2 (Mandate derived but written 78×)** → resolved: nothing writes a faction stat. The 78 sites become either a
  settlement/territory stat change at the locus or a national-event modifier Key; the stat re-derives. The d+σ reads it.
- **C-3 (Treasury double-source)** → resolved: Treasury is the settlement Local Economy aggregate, full stop.
- **C-4 (6 vs 7 stat count)** → orthogonal but clarified: the lineup is whatever set of *derived readouts* the design
  keeps; settle it during the migration (the `factions_personal §8.1` vs `stats_1_7_scale` discrepancy is a labelling
  cleanup, not affected by primacy).
- **C-5 (Prosperity level)** → resolved by construction: Prosperity is unambiguously a settlement base; "Effective
  Prosperity" is its province-level aggregate readout — the same primitive→derived pattern.

It also closes the **vector/scalar mismatch (Layer 5)**: routing ripples through Key modifiers + settlement stats keeps
faction-stat change inside the Key-emitting substrate, rather than a bespoke scalar `most_relevant_stat += N` channel.

---

## 5 — NERS verdict on the proposal

- **N (Necessary):** **Pass, net-removing.** It deletes a whole redundant layer (the §14 capitals as separate gauges)
  and a bespoke write channel (Domain Echo scalar deltas), replacing two parallel economies with one. The added
  apparatus (a national-event modifier ledger) is *necessary* to preserve faction agency and is just Keys — no new
  primitive. Watch that the ledger does not itself bloat into per-event special cases.
- **R (Robust):** **Pass.** Derived stats hold at extremes — a faction with few/weak holdings has low stats, emergently
  and correctly; d+σ's flat 0.10 leverage already handles the small-stat regime without a fragile pool. No stat can be
  silently desynced from its basis because there is only one basis.
- **S (Smooth):** **Pass, improving.** One derivation idiom across all faction stats; the upward ripple flows through
  the settlement layer (scene → settlement → faction) instead of skipping scales; faction-stat change lives in the Key
  substrate it shares with everything else.
- **E (Elegant):** **Pass.** The player intuition becomes "govern your settlements and act nationally → your faction
  strength follows," which is legible and emergent, versus an opaque base-stat-plus-scaled-capital ledger. One formula,
  two inputs (hold + act).

**The proposal is NERS-compliant and improves S and E specifically.** The only NERS risk is **N-overreach on the
ledger** and the **Influence/Intel basis** (§3.1) — both are design-decisions to make, not flaws in the direction.

---

## 6 — Risks, open questions, and what must be decided

1. **[DECIDE] Influence & Intel derivation basis.** They are not settlement sums. Define each explicitly — most likely a
   thin structural base (capital prominence; institutional presence) plus a dominant national-event ledger. Do **not**
   force a settlement aggregate. This is the one place the generalization breaks and needs an authored answer.
2. **[DECIDE] National-event modifier semantics.** Decay shape (linear/exponential, half-life), stacking/cap, and which
   Key types contribute. Without decay, the ledger ratchets and the stat never falls; with too-fast decay, national
   agency feels weightless. This is the lever that replaces 78 direct writes — it has to be tuned, ideally by sim.
3. **[DECIDE] Aggregation function per stat.** LPS-2e gives Mandate a size-weighted saturating form. Wealth/Military/
   Stability each need their weight + saturation chosen (a faction shouldn't scale linearly without bound in holdings).
4. **[RISK] Authoring shift.** Designers/scenarios stop setting faction stats directly and set the **settlements +
   initial national modifiers**; the stats derive. `faction_state_authoring_v30` already authors L/PS per faction for
   Mandate — this generalizes that pattern, but every authored faction stat in canon becomes a derived value to verify.
5. **[RISK] Performance.** Re-derivation on every settlement change — handle with cached aggregates invalidated on
   constituent change (the registry's bind-at-load discipline; K8), not per-frame recompute.
6. **[RISK] Re-homing the capital threshold effects.** "Treasury 0 → no muster," "Reputation 0 → diplo +1 Ob,"
   "Discipline 0 → Stability check" each encode a real low-resource penalty. They must be re-expressed (low-settlement-
   economy → muster block; low-derived-Influence band → diplo Ob) so the migration doesn't silently drop a mechanic.
7. **[SCOPE] This is a large migration.** It touches `derived_stats §14`, `faction_canon`/`faction_behavior`,
   `faction_layer`, `ci_political`, `victory`, `strategic_layer`, `scale_transitions §5` (Domain Echo), the d+σ inputs,
   and `faction_state_authoring` — and the 78 write-sites from the flattening become the migration worklist. Stage it;
   do not attempt atomically.

---

## 7 — Recommendation

Adopt the inversion as the **target architecture**: settlement/territory substrate primitive; every faction stat a
derived readout = aggregate(holdings) ⊕ national-event ledger; retire the §14 capital layer (re-homing its genuine
semantics down); reconceive Domain Echo as a substrate ripple rather than a scalar write. Resolve the two structural
DECIDE items first (Influence/Intel basis; national-event-modifier semantics) — those are yours, and the rest of the
migration is mechanical and stageable behind them.

This does not touch metaphysics, world, or characters; it is a mechanical re-grounding of how faction strength is
*computed*, consistent with LPS-2e, the Key substrate, the d+σ resolver, and the bidirectional ripple — i.e. it
finishes a direction the project already committed to for Mandate.

---
*Review only. Grounded in `key_substrate_v30`, `scale_transitions_v30 §3–§5`, `sim/cross_scale/domain_echo.py`,
`domain_action_resolver_spec` (ED-874), `settlement_layer §1.8`, `derived_stats §14`, and the 2026-06-09 flattening.
The two [DECIDE] items are structural-ontology calls reserved for Jordan.*
