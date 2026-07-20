# Decision-Queue Delta (v1) — Scale-Chain & Decision-Surface DESIGN hand-off

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** The ranked hand-off surface for the governance DESIGN pass, **updating the 2026-07-13
17-item `decision_queue.md`** (ED-IN-0051). It records: (A) what **#136** (`lps_wiring_v1.md`) closes or
advances; (B) items **newly surfaced** this pass (chain-map / census / vector-audit / #136); and (C) the
2026-07-13 **MoH-grounded items RE-GROUNDED** on non-MoH precedent. Ordering = leverage on the L/PS-pressure
spine × 1/cost × novelty. Classes mirror `gap_register_v2.md`: **[CTC]** COMPLETE-THE-CHAIN (execution on
sound logic — usually a ruling-to-unblock, not a design call) · **[GAP]** GENUINE-GAP (a real precedent-informed
design call).

> **BINDING:** Mandate of Heaven is NOT a proposed mechanic. Tier-2 #5 (collision) and Tier-1 #3 (relief-valves)
> are re-grounded below on non-MoH precedent; every MoH mention is **"historical grounding only."** Nothing here
> is executed — merging this docket's PR ratifies the *analysis* (FILED); each fix stays PROPOSED, needing its
> own sign-off (CLAUDE.md §1).

---

## §A · Status changes to the 2026-07-13 queue (what #136 did)

| 2026-07-13 item | Was | Now | Effect |
|---|---|---|---|
| **#1 Wire L/PS (GAP-B1)** | [CTC], undesigned | **SPEC-ONLY — buildable** | #136 is the full buildable spec (LPS-2e + consent-gate + deferred-apply boundary). The Tier-1 call is no longer "approve wiring from surrounding logic" but **"approve the #136 impl PR"** (`doc:lps_wiring_v1 §10` → code §5). |
| **#2 Wire `compute_accord_echo` (GAP-A2)** | [CTC] zero callers | **SPEC-ONLY** — #136 write-source #1 | Folded into the #136 impl PR (`doc:lps_wiring_v1 §4.1`). `propose_transfer` (GAP-A1) is **not** touched by #136 — it stays a separate CTC wiring call. |
| **#9 ΔLegitimacy decay (GAP-B4)** | [CTC] deferred `decay()` | **SPEC-ONLY** — designed | #136 §4.4 Mandate→L mean-reverting drift **is** the decay term. Ratify-and-code, not author. Polybian anacyclosis re-grounds it (confirmatory). |
| **#11 D.6 disjoint + convergence (GAP-A4)** | [CTC] ruling needed | **SPEC-ONLY — artifact designed** | #136 §5 (M_prev snapshot step 0 / drift step 4) + §9 test 4 is the designed termination artifact. Residual [GAP]: the convergence is *asserted*, not yet *proven* — a Fable/opus proof node remains. |

**Net:** the four heaviest Tier-1/Tier-3 spine items now share **one impl PR** (code `lps_wiring_v1 §5` into
`sim/`, turn `lps_inert_check` 100/100 → green). This is the docket's single highest-leverage action.

---

## §B · The updated ranked queue

### Tier 1 — unblock the whole spine (do first)

| # | Item | Class | The call | Why #1-tier |
|---|---|---|---|---|
| **1** | **Approve the #136 L/PS impl PR** (B1+A2+B4+A4-artifact) | [CTC] | Ratify `lps_wiring_v1.md` PROPOSED→canonical and code §5 into `sim/` (new `sim/territory/legitimacy.py`; rewire `parliamentary_bridge`/Treasury/AP to read the aggregate, not scalar `Faction.L`). Closed-form, oracle-safe (§10). | Turns 4 chain_map §3 edges from canon-WIRED/sim-INERT to agreeing at once; every consent/fracturing/emergence arc is dark until L/PS bites. |
| **2** | **Wire `propose_transfer` to the seasonal vote** (GAP-A1) | [CTC] | Connect `parliamentary_bridge.py`'s vote output to the existing `parliamentary_transfer` resolver. No new code, no import. | Ends the one-way-ratchet defect (territory can never be regained); cheapest high-leverage fix. NOT in #136. (The "~87%" it was conflated with is a debunked small-N artifact.) |
| **3** | **Mandate collapse + the two relief-valves — RE-GROUNDED** (GAP-B2) | [GAP] (valves) + [CTC] (devolution) | Confirm D4 (retire `round(7T/(T+K))` as collapse carrier → floor-avg Order + fracturing + Standing Keys), and rule the two valves **on non-MoH precedent (§C)**: scapegoat + self-reproach. | Gives the spine a *downward* consequence (collapse), not just upward aggregation. |

### Tier 2 — the genuine new-mechanism / new-verb surface

| # | Item | Class | The call | Precedent |
|---|---|---|---|---|
| **4** | **Rank the two chain-bypass authorities** (GAP-D1) | [GAP] | Monarch + Parliament both bypass with no precedence. Pick nest-one-inside-the-other OR named-crisis-mode. **New this pass:** also distinguish a **third bypass-adjacent authority** (a standing ideological/juridical seat outside the chain) + an *ad-hoc emergent* non-chartered bypass. | Bodin indivisible-sovereignty; **Ottoman Şeyhülislam fatwa** (third authority); **Roman SCU** (ad-hoc bypass) — all `research:conflicts`. |
| **5** | **Collision-of-stresses two-signal primitive — RE-GROUNDED** (GAP-E1/E2) | [GAP] | Approve a unified collision primitive requiring **two independently-arriving signals** (material threshold AND independent legitimating trigger) to resonate before a rank-appropriate revolt/Mandate-tier event resolves; a bare grievance fizzles. | **Non-MoH (§C):** Roman Gracchi / Year of Four Emperors; Ottoman Janissary+fatwa; Carolingian 887–888. |
| **6** | **Author the thin decision-surface verb sets** (NG-4) | [GAP] | Author council-member (~5), territory-bureaucrat (~5), and Parliament-body (~4) verb menus so each is a real ≥4-5 decision surface. **Guard:** each verb must emit a down-tier Key or it is decorative false depth. | Signoria + *intercessio* (council); *missi*/*transvectio*/*repetundae* (bureaucrat); HRE Reichsexekution + sequential curiae (Parliament) — all `research/governance/`. |
| **7** | **Parliament's ruled-reach verb + armature binding** (NG-5) | [GAP]+[CTC] | Author a `Reichsexekution`-shaped Domain Action emitting a coercive Key onto a named province/territory/settlement; bind the RULED-but-unbound §5.2/§5.3 cross-scale-claiming/bypass authorities to an armature channel. | HRE Reichsexekution; the census's widest ruled-reach/built-verbs gap. |
| **8** | **Governance-mode FLAG taxonomy** (GAP-C2, carried) | [GAP]+[MIX] | Adopt the 8-value `governance_mode` domain (distinct from manager-type); it is the *thinness multiplier* the census runs its per-role verdicts against. | Aristotle/Athens-sortition/Roman-comitia/consensus polities. |
| **9** | **Suppression-backfire + identity-migration** (GAP-G2, carried) | [GAP] | Seven backfire mechanisms; the novel identity-migration hand-off converts a militarily-solvable problem into a Fieldwork/Investigation one. Model a floor, not a zero (Carthage discard). | Reconquista/*limpieza*/Morisco; Rome-vs-Jerusalem; **Carolingian Stellinga** + **Roman Jewish revolts** (non-MoH, `research:conflicts §3.7/§9`). |

### Tier 3 — rulings + authoring that unblock chain-completions

| # | Item | Class | The ruling / authoring |
|---|---|---|---|
| **10** | **Extend the scale_signature enum to 6-of-6** (NG-1) | [CTC]+sliver [GAP] | Add `province/duchy/country` to `key_substrate_v30 §2.1`'s FLAG domain (names determined by the ratified ladder); rule `peninsula`'s relation to the ladder (WS2 vocabulary reconciliation). **Unblocks V4 + the entire vertical axis above territory.** |
| **11** | **Add the Field-Investigation dispatch branch** (NG-2) | [CTC] | Add a `"fieldwork"`/`"investigation"` `scene_type` branch to `scene_dispatch.py` importing the orphan `investigation.py`/`fieldwork.py`. Unblocks H4/H5/H6 (the whole FI horizontal axis). |
| **12** | **Author `engine_clock` + `domain_actions` home docs** (VA-1 / GAP-H3) | [GAP] (author) | Flip the two load-bearing `doc:null` contracts (of 9): `engine_clock` (temporal spine sequencing every V-axis boundary; #136 §5 depends on it; home `propagation_spec_v1`) and `domain_actions` (H1's resolver home; home `governance_play_redesign_v1 §1.3`). |
| **13** | **Wire the combat bottom-up echo** (V9 / VA-2) | [CTC] | Add `scene.combat_resolved`/`_felled` to `npc_behavior`/`faction_state` `consumes[]` (registry already declares them); author the aggregate→personal-actor bridge so the combat dispatch path stops always-deferring. |
| **14** | **Turn ECHO_TRANSPORT on by default** (V8/H2′/H3) | [CTC] | Attach `world.echo_scheduler` in the default campaign + build the ED-SC-0006 items 1–2 context-derivation bridge so personal-scale scenes derive actors instead of deferring. |
| **15** | **`stakes.source_key` predicate — earn or weaken** (chain_map §3, GAP-E-adjacent) | [GAP] | Author the `stakes.source_key` consume-edge on `social_contest §6`, OR downgrade the event→Parliament/SC claim to "a motion may cite the Key." The one edge failing the ripple substrate's own §9 dependency test. |
| **16** | **Carried Tier-3 rulings** (C3 hardness, D2 bypass-metering, B3 formula reconciliation, B5 blast-radius) | [CTC] | Unchanged from 2026-07-13 `decision_queue.md` Tier 3 / addendum; ratify per D4. |

### Tier 4 — hygiene, slivers, held proposals

| # | Item | Class | Note |
|---|---|---|---|
| **17** | **Repair the `id_reservations.yaml` duplicate-IN-key** (NG-6) | [CTC] | Collapse the two `IN:` blocks into one (mirrors the 2026-07-07 FI/SC/FA/WR repair); until then last-key-wins can regress the IN counter. |
| **18** | **Register the 4 unregistered-canonical heads + resolve currency-drift** (VA-3/VA-4) | [CTC] | Register `fractional_province_ownership`/`social_contest`/`march_layer`/`settlement_adjacency` (verify each body `**Status:**` first); drop `combat_v30`'s canonical registration (PARTIALLY SUPERSEDED). |
| **19** | **Re-index orphans + repoint stale pointers** (VA-5 / carried F1/H1/H2) | [CTC] | Add franchise/fractional/insurgency/succession-split to CURRENT.md; 10 stale pointers are mechanical restructure-ledger repoints, 5 need a human. |
| **20** | **Carried Tier-4** (caste cascade/circumvention F2-F5/F3; orthodoxy-axis G1; "elect-inward" propagation shape ⚠ held) | [CTC]/[GAP-held] | Unchanged from 2026-07-13 Tier 4; the elect-inward armature direction stays fable/opus-gated PROPOSED-doc work, not ratified. |

---

## §C · The RE-GROUNDING detail (BINDING — cite when authoring #3 and #5)

**Discipline:** a re-grounding is real only as a specific two-signal **read** dependency (an objective-strain
Key AND an independent legitimating-authority Key co-firing), not a thematic resemblance to MoH.

**#5 — two-signal collision (GAP-E1/E2), non-MoH:**
- **Roman Gracchan rupture** — land/debt crisis (material) + re-election read as kingship (interpretive) → SCU. `research:conflicts §1`.
- **Roman Year of Four Emperors** — no heir + donative solvency (material) + legion acclamation ritual (interpretive). `research:conflicts §4`.
- **Ottoman Janissary deposition** — military/fiscal strain (material) + Şeyhülislam fatwa (independent juridical). `research:conflicts Ottoman §Janissary` (verifier: this is the direct non-MoH precedent for the primitive).
- **Carolingian 887–888** — failure of core deliverable/military protection (material) + matured regional-magnate Standing (interpretive). `research:conflicts §3.8`.
- Roman brief verifier: *"MoH leakage: NONE — confirmed clean"*; mechanism is **army-loyalty fission**, kept endogenous. *(MoH zaiyi — historical grounding only.)*

**#3 — relief-valves (GAP-B2), non-MoH:**
- **Scapegoat** — Venetian graduated-removal ladder + procurator sinecure AND Ottoman grand-vizier-as-scapegoat + Janissary revolt; read/write = an appointee absorbs the hit at the cost of *their* Standing Key. `research:conflicts §synthesis (relief valve)`.
- **Self-reproach** — Roman *recusatio* + imperial penance under Ambrose; read/write = an L/PS-priced ritual spending the ruler's own resource. `research:conflicts hooks "Ritual self-abasement"`. *(Chinese penitential edict — historical-only, explicitly non-proposed in corpus.)*
- **Negative control** — Rome's Crisis of the Third Century cascaded *for lack of any valve* (`research:conflicts §6`).
- **Decay (GAP-B4)** — Polybian anacyclosis is *confirmatory* only; the fix is #136 §4.4's drift term.

**Devolution output** — power devolves national→province/territory (Roman Palmyrene/Gallic recognition-fission,
`research:conflicts §6`), reusing the A1 transfer resolver + F5 fracture-resolution — never MoH warlordism.

---

**Recommended sequence.** Tier 1 (#1–3) unblocks the spine — approve the #136 impl PR first. Tier 2 (#4–9) is
the genuine design surface for Jordan's direct calls (verb-set authoring + re-grounded collision/valves). Tier
3 (#10–16) frees execution — the scale enum (#10) and FI dispatch (#11) are the two structural unblocks the
chain-map headlines. Tier 4 is hygiene. Nothing here executes; the fixes remain PROPOSED, each needing its own
sign-off.

---

## §D — Harvested research hooks (previously orphaned from the hand-off)

The holistic unification (`unification_findings_v1.md` X-2) flagged four `research/governance/` design-hooks
bound to no queue item; they are folded in here so the DESIGN pass carries them:

- **Tetrarchy multi-seat power-share + its MANDATORY charter-Key failure-guard → new Tier-2 #5b.**
  `governance_modes.md §synthesis` offers the multi-seat mechanic (Roman Tetrarchy / Japanese Go-Tairō);
  `conflicts_power_struggles.md §synthesis` supplies its failure-guard — bind army/enforcement loyalty to an
  *impersonal charter-Key*, never a named seat-holder Key, or the structure reproduces single-claimant
  collapse. **Never offer the mechanic without the guard** (the corpus flagged this landmine itself).
- **Dormant-but-live Crown gate** (Roman Senate reasserting after a general's death; non-MoH) → attach to
  **#4** (chain-bypass authorities): the Crown/Parliament consent-gate never zeroes under eclipse and snaps
  back on a two-signal collision.
- **Permanent-grant → collision event-type** (Caesar *dictator perpetuo* → the Ides) → attach to **#5**
  (collision primitive): removing a grant's temporal/recall cap is a *distinguishable event type* that fires a
  collision check among the highest OLIGARCHIC_COUNCIL seats.
- **Reaggregation-adds-a-seat** (HRE Palatinate 1623; Cleisthenes) → attach to **#3**
  (recognition-fission/reaggregation): a Crown action that redraws the allegiance aggregation topology, whose
  resolution can *add* a new seat rather than restore the old one.

All four are non-MoH and grep-confirmed in the corpus; none was previously reachable from this delta or
`gap_register_v2.md`.
