# Gap Register (v1) — Cross-Scale Governance

## Status: FILED (in progress) — 2026-07-13 · Lane: IN · ED-IN-0051

Every gap / break / dead-end / friction on the governance nexus, keyed to a graph edge, evidence-traced,
and **classified before any fix is proposed** per the two-tier doctrine (Jordan, this turn):

- **[COMPLETE-THE-CHAIN]** — an unbuilt link in an otherwise-built chain; the fix is **derived from the
  logic of its surroundings** (ED-1050 doctrine). Precedent is *confirmatory only*.
- **[GENUINE-GAP]** — the surrounding logic does not determine the answer; **only here** does an
  imported-and-adapted precedent supply the solution.

Evidence types: `code:` grep/caller-check (from the 3 code-verified exploration passes) · `audit:` audit/
ruling ID · `doc:` design-doc section · `ledger:` ED/PP. Edge codes map to the five graph cuts in
`governance_grounding_v1.md`. Fix-direction is one line; full treatment in `precedent_fix_catalog_v1.md`.

Legend for status of the broken thing: **BROKEN** (should fire, doesn't) · **INERT** (declared, never
read/written) · **DOCTRINE-ONLY** (ruled, uncoded) · **UNRECONCILED** (multiple live definitions) ·
**ORPHAN** (real mechanics lost from the currency index) · **STUB** (self-declared placeholder).

---

## A · Spatial containment spine (aggregate-up / distribute-down)

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-A1** | `faction → named settlement/territory` transfer **BROKEN** | `code:` `parliamentary_transfer.py` never called from the live loop | **COMPLETE-THE-CHAIN** | Wire it: `parliamentary_bridge.py` already fires the seasonal vote → connect its output to the existing transfer resolver. No import. |
| **GAP-A2** | Accord echo aggregation **BROKEN** | `code:` `compute_accord_echo()` has **zero callers** | **COMPLETE-THE-CHAIN** | Invoke the existing function from the Accounting boundary; the aggregation math already exists. |
| **GAP-A3** | Territory tier **DOCTRINE-ONLY** | `doc:` `scale_hierarchy_v1 §3` ruled Settlement→Territory→Province→Duchy→Country; `code:` only Settlement↔code-"Province" floor-mean/sum aggregation is live | **COMPLETE-THE-CHAIN** (blocked on B11 `engine_clock`) | Extend the one live aggregation pattern to the ruled tiers; unblock via `engine_clock` authoring (H3). |
| **GAP-A4** | Cross-tick convergence **UNPROVEN** | `doc:` `propagation_spec_v1` proves per-tick/per-cascade, not cross-tick-convergent; `audit:` D.6 double-count flag | **GENUINE-GAP** | Termination artifact (aggregate-up/distribute-down + convergence proof, doctrine ED-1083 §4) — surrounding logic doesn't imply convergence. |

## B · Legitimacy–consent spine (the headline)

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-B1** | **L/PS INERT (100/100)** — the whole consent-cascade has no consequence | `audit:` `lps_inert_check` 100/100, tracked **E5**; `doc:` `scale_hierarchy_v1 §6` calls it "single highest-priority open item" | **COMPLETE-THE-CHAIN** | Wire from surrounding logic: aggregation (LPS-2e) + consent-gate (`§4`) + deferred-apply Accounting boundary + `Field`/`Gauge` shape all exist. **Do NOT import CK3.** Precedent (Vic3 legitimacy-loop, EU4 estate loyalty) is confirmatory. |
| **GAP-B2** | Mandate has **no withdrawal/collapse** path | `doc:` `settlement_layer §1.8` `round(7T/(T+6))` monotone; `audit:` D4 "masks peripheral collapse" | **GENUINE-GAP** (collapse mechanism) | Import the **Mandate-of-Heaven** structure: collapse = a **two-signal collision** (material + interpretive) whose output is **power devolution**, not a floor-crossing. D4 rules the carrier retires → floor-avg Order + fracturing + Standing Keys; the *interpretive/withdrawal layer* is the genuine gap. |
| **GAP-B3** | **Three competing** "faction political power" formulas | `doc:` franchise National-Influence · `valoria_political_hierarchy §2.4` `political_value()` (scalars **TBD**) · `settlement_layer §1.8` Mandate | **COMPLETE-THE-CHAIN** | One reconciliation item, determined by D4's ruling — not three independent gaps. |
| **GAP-B4** | ΔLegitimacy has **NO decay term** | `doc:` `faction_behavior_v30 §3.5` — event-builds + uncapped `+λ×seasons_in_role`, no entropy | **COMPLETE-THE-CHAIN** | Add the decay term via the deferred **OF-3 `decay()`**. Anacyclosis/regime-cycle theory *confirms* the need (not imported). |
| **GAP-B5** | Standing ladder's cross-scale role under-wired | `doc:` `faction_politics_v30` Skyrim-Eight exists; appointment-eligibility & secession-scale mapping absent | **Mixed** | Ladder itself = **COMPLETE-THE-CHAIN** (exists). The **rank = secession blast-radius** mapping = **GENUINE-GAP** → import ROTK (Prefect=city / Viceroy=division). |

## C · Governance-type cascade

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-C1** | Two senses of "governance type" **CONFLATED** | `doc:` `scale_hierarchy §3` mixes *manager*-type (who governs) with *decision-procedure mode* | **COMPLETE-THE-CHAIN** | Split the two senses; the manager enum is built, the mode taxonomy needs enumeration (C2). |
| **GAP-C2** | Governance-**mode** taxonomy under-specified | Jordan directive: consensus / deliberative / landholder-franchise / oligarchic / royal-appointment / … not enumerated as a FLAG domain | **GENUINE-GAP** | Import the taxonomy from precedent (Aristotle regime types; Athens sortition; Roman *comitia*; consensus polities — research thread B3). Domain + which are start-active vs latent. |
| **GAP-C3** | Does an imposed type **stick**? + is the cascade too **hard**? | `doc:` `scale_hierarchy §3` hard top-down cascade, gated by inert L/PS | **Mixed** | "Does it stick" = **COMPLETE-THE-CHAIN** once B1 wired (**CK3 Administrative** broadcast+local-attenuation *confirms* the surrounding logic). The **hardness** (forcing an identical type down) = **GENUINE-GAP-novel** — no game forces it (Imperator/Stellaris/EU4/ACOUP); reconsider hardness. |
| **GAP-C4** | Mode ↔ deliberative-game binding; **Consensus game STUB** | `code:` `wrapper.py` GAMES `consensus: STUB` (raises `NotImplementedError`) | **COMPLETE-THE-CHAIN** | Each mode selects its resolving contest-game (binding is derivable); the Consensus game is a known STUB to build (unanimity/holdout/veto). |

## D · Chain-bypass authorities

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-D1** | Monarch + Parliament both bypass, **UNRANKED** | `doc:` `scale_hierarchy §5.3` two unconditional chain-bypass authorities, no precedence | **GENUINE-GAP** | **Bodin's** exact warning (→ French Wars of Religion). Import: **(1)** nest one inside the other (Tokugawa/English constitutional-monarchy), OR **(2)** make Monarch-vs-Parliament collision a **named designed crisis mode**. |
| **GAP-D2** | Bypass has **no metered cost** | `doc:` bypass acts are free | **GENUINE-GAP** | Import **Imperator Tyranny**: meter the bypass against the same fragility/secession-risk pool. |

## E · Collision-of-stresses (simultaneous multi-scale)

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-E1** | Collision primitive **not unified** | `doc:` MS distance-falloff + Calamity radiation + Peninsular Strain + Π cooling-cascade exist un-unified; `audit:` D.6 + OF-3 fork (down-`stat_deltas` ∧ up-aggregates → oscillation) | **GENUINE-GAP** | Unify into a collision primitive grounded in **Mandate-of-Heaven two-signal resonance** + **EU4 Court-and-Country** (independent top-down ∧ bottom-up crossing together); true *parallel* collision is a Valoria departure. |
| **GAP-E2** | Collision needs **two independent signals** | not modeled; a famine would read as a lone settlement problem | **GENUINE-GAP** | Import: a Mandate-tier event requires a **material threshold AND an independently-arriving interpretive trigger** (portent/rumor/interdict) — a court social-contest scene adjudicates whether it "counts" (Xunzi contestability). |
| **GAP-E3** | Collapse-is-a-dial (recovery/decay) partial | `code:` E11 suspicion-decay exists; not systematized as an anti-cascade dampener | **COMPLETE-THE-CHAIN** | Extend existing E7/E11 counters into the general dampener (RimWorld/DF *confirm* collapse must be a dial). |

## F · Internal-population layer (franchise · caste · intrapopulation conflict)

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-F1** | `franchise_v30` **ORPHAN** through every currency layer | `code:` absent from CURRENT.md, `canonical_sources.yaml`, `mechanics_index`; `doc:` DRAFT | **COMPLETE-THE-CHAIN** | Re-index + reconcile pre-PP-726 nomenclature; the caste→territory→national-power cascade (Franchise 0–5) is fully specified — the "expand franchise" spine. |
| **GAP-F2** | Caste **cross-scale cascade** under-wired | `doc:` `faction_politics Part 3` caste gating is personal-scale; settlement-composition VECTOR → territory advancement → national franchise-suppression not wired | **COMPLETE-THE-CHAIN** | Wire the cascade from existing caste keys + franchise caste-gradient. |
| **GAP-F3** | Caste **circumvention** general mechanism absent | `doc:` only `§2.5a` Entry/Mastership Forks (PROPOSED) instance | **GENUINE-GAP** | Import (varna *jajmani* patronage; Byzantine *Book of the Eparch* guarantor; *limpieza* passing — B4): capital/social-collateral routes around caste gates. |
| **GAP-F4** | Intrapopulation-conflict → fracturing under-integrated | `code:` `insurgency_pipeline_v30` (world/) + `faction_succession_split_v30` ORPHAN-vs-CURRENT; `doc:` P11-vs-P2 "fracturing engine" needs in-world causal justification (Jordan ruling) | **COMPLETE-THE-CHAIN** | Re-index; wire the fracturing engine with the causal-justification constraint; adopt the two-stage split resolver (dice=who-leads, gap G=whether-splits). |
| **GAP-F5** | Fracture **RESOLUTION** absent | `doc:` `scale_hierarchy §5.2` Independence-at-any-tier has **no resolution roll**; `fractional_province_ownership` Fragmentation Check + Consolidation Action orphaned | **COMPLETE-THE-CHAIN** | Adopt the orphaned **Fragmentation Check** (recurring hold/collapse roll) + **Consolidation** Domain Action; anchor dissolution on the RAND-grounded 4-path model (sponsor-withdrawal modal). |

## G · Religious / cultural orthodoxy

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-G1** | Orthodoxy↔heresy↔non-orthodoxy not a **nexus axis** | `doc:` Church keys (CI/Piety/Excommunication/Inquisition/Heresy-Lifecycle/RDT) exist but aren't integrated cross-scale | **COMPLETE-THE-CHAIN** | Lift existing Church keys into the registry as an **ideological-consent axis parallel to L/PS**: individual belief → settlement doctrinal composition → territory piety → national CI. |
| **GAP-G2** | Cultural suppression / genocide as a **costed consequence-bearing action** | `doc:` conquest Storm/Sack fork + Entry-Terms "Impose Administration" exist; the suppression→backlash→insurgency cross-scale consequence under-wired | **GENUINE-GAP** | Import the **backfire structure** (Reconquista/Morisco expulsion; Shimabara; iconoclasm — B5): high-cost action → severe L/PS collapse + intrapopulation conflict + durable resistance identity feeding the insurgency pipeline. Never consequence-free. |

## H · Currency / hygiene meta-gaps

| ID | Edge · state | Evidence | Class | Fix-direction |
|---|---|---|---|---|
| **GAP-H1** | 5+ docs: `## Status: CANONICAL` header vs `PROVISIONAL/DRAFT` body | `doc:` franchise, fractional_province_ownership, faction_succession_split, territory_temperaments, valoria_political_hierarchy | **COMPLETE-THE-CHAIN** | Header/body reconciliation (currency-hygiene). |
| **GAP-H2** | Cited/pinned docs **ORPHAN from CURRENT.md** | `code:` franchise, fractional_province_ownership, insurgency_pipeline, faction_succession_split relied-on but unindexed | **COMPLETE-THE-CHAIN** | Re-index into CURRENT.md's subsystem table. |
| **GAP-H3** | `domain_actions` module **doc:null** (strategic-turn home) | `doc:` `module_contracts.yaml` 10/27 doc:null incl. `engine_clock` | **GENUINE-GAP** | Author the home doc (blocks the governance-verb coding of GAP-A3 and Territory-tier of GAP-A3/A4). |

---

## Summary

**~24 gaps across 8 categories.** Classification tally: **[COMPLETE-THE-CHAIN] 14** · **[GENUINE-GAP] 8** ·
**Mixed 2** (B5, C3 — a built spine with a genuinely-gapped extension). The chain-completions cluster on the
**wiring** spine (L/PS inert, unwired transfer/echo, orphaned-but-real franchise/insurgency/caste
mechanics, no-decay ΔLegitimacy); the genuine gaps cluster on **mechanisms the corpus never implied** —
the Mandate *withdrawal* layer, the governance-*mode* taxonomy, unranked bypass authorities, the *unified
collision* primitive, caste *circumvention*, cultural-*suppression* backfire, and the `domain_actions`/
`engine_clock` home docs. This is the intended shape: **most of the "missing" governance is unbuilt wiring
on sound logic; a minority needs an imported-and-adapted mechanism** — and the adversarial gate (Phase F)
must defend every one of the 8 [GENUINE-GAP] imports against an available chain-completion, and every
precedent against surface-analogy.
