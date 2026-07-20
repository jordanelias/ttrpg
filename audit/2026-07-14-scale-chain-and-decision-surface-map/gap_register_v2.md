# Gap Register (v2) — Scale-Chain & Decision-Surface, Consolidated + Adversarially Classified

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** The single consolidated gap register for the 2026-07-14 governance docket. It folds
the three fresh maps (chain / decision-surface census / churn), the 2026-07-14 vector audit
(structure/generation/weakness registers), and the fresh #136 L/PS spec into — and **extends, does not
duplicate** — the 2026-07-13 `gap_register_v1.md` (ED-IN-0051). Every gap is **keyed to a chain-map edge**
(V1–V9 vertical, H1–H6 horizontal, §3 synthesis edges), **evidence-traced** (`code:` / `doc:` / `audit:`),
**classified before any fix**, and carries a **one-line MoH-free fix-direction** that is a *specific
read/write dependency*, never a thematic resemblance.

### Classification (mirrors the 2026-07-13 two-tier doctrine exactly)
- **[COMPLETE-THE-CHAIN]** — an unbuilt link in an otherwise-built chain; the fix is *derived from the
  logic of its surroundings* (ED-1050 doctrine). Precedent is confirmatory only; nothing is imported.
- **[GENUINE-GAP]** — the surrounding logic does not determine the answer; only here is an
  imported-and-adapted precedent load-bearing.

State legend (from chain_map_v1): **WIRED · HOOK-NEEDED · BROKEN · INERT · SPEC-ONLY · DOCTRINE-ONLY.**

> **BINDING — Mandate of Heaven is NOT a proposed Valoria mechanic.** The 2026-07-13 docket grounded the
> two-signal collision (GAP-E1/E2) and the Mandate-collapse relief-valves (GAP-B2) on Mandate-of-Heaven.
> This pass **re-grounds both on non-MoH precedent** (§7) per the design-lead ruling; every surviving MoH
> reference is tagged **"historical grounding only."**

---

## §0 · What #136 (`lps_wiring_v1.md`) advanced — read before the tables

`doc:designs/territory/lps_wiring_v1.md` (**PROPOSED buildable spec, Lane SE**, executes E5 / ED-FA-0004
Stratum-B / ED-SE-0007) is a closed-form, D.6-disjoint spec for the whole settlement→Mandate→settlement
loop. It **explicitly does not edit `sim/` and flips no `## Status:`** (`doc:lps_wiring_v1 §10`). Its net
effect on the 2026-07-13 register is to move three gaps from *undesigned* to **SPEC-ONLY (designed, pending
one impl PR)** — the fix-direction is now "code §5 into `sim/`," not "author a mechanism":

| 2026-07-13 gap | Was | #136 advanced it to | Class (unchanged) |
|---|---|---|---|
| **GAP-B1** L/PS inert 100/100 | undesigned wiring | **SPEC-ONLY** — full LPS-2e aggregation + consent-gate + deferred-apply boundary authored | [COMPLETE-THE-CHAIN] |
| **GAP-A2** accord-echo `compute_accord_echo` zero callers | BROKEN | **SPEC-ONLY** — now the spec's **write-source #1** (`doc:lps_wiring_v1 §4.1`) | [COMPLETE-THE-CHAIN] |
| **GAP-A4** cross-tick convergence unproven | UNPROVEN | **SPEC-ONLY** — the **D.6-disjoint artifact is designed** (`doc:lps_wiring_v1 §5` M_prev snapshot at step 0, drift at step 4; §9 test 4 convergence) | [GENUINE-GAP] (proof still to be *proven*, not just asserted) |
| **GAP-B4** ΔLegitimacy no decay term | undesigned | **SPEC-ONLY** — the **Mandate→L mean-reverting drift** IS the decay term (`doc:lps_wiring_v1 §4.4` `ΔL_drift = sign(M_prev−L)·1` when `|M_prev−L|≥2`) | [COMPLETE-THE-CHAIN] |

**All four remain uncoded** — `audit:lps_wiring_v1` cites `Settlement.legitimacy`/`popular_support` as
*"NEVER READ OR WRITTEN anywhere in sim/"*, `lps_inert_check` 100/100 red. Coding #136 is the highest-leverage
single PR in the docket; it makes chain_map §3's canon-column and sim-column agree on 4 of 8 edges at once.

---

## §1 · NEW findings this pass (not in the 2026-07-13 register)

| ID | Gap · edge · state | Evidence | Class | MoH-free fix-direction (read/write dependency) |
|---|---|---|---|---|
| **NG-1** | **scale_signature enum is 4-of-6** — caps the vertical axis at `territory`; V4 (territory→province→duchy→country) BROKEN at the substrate | `code:key_substrate_v30.md:57` enum = `{personal,settlement,territory,peninsula}`; ratified ladder is 6-level (`doc:scale_hierarchy_v1 §1`); `audit:key_substrate_v30 §12 invariant 7` rejects non-canonical members | **[COMPLETE-THE-CHAIN]** (names determined by ratified ladder) **+ genuine sliver** (peninsula↔ladder reconciliation = WS2) | Add `province/duchy/country` to the `scale_signature` FLAG domain so a Key can *stamp* those bands; the aggregate_fn is the existing floor-mean/pop-weighted pattern (V2). Genuine sliver: rule whether `peninsula` is a scale-ladder rung or an orthogonal world-layer (WS2). **Blocks V4 + everything above territory.** |
| **NG-2** | **Field Investigation has zero live dispatch** — H6 BROKEN; H4/H5 cannot fire downstream | `code:scene_dispatch.py:129-215` branches only on `combat`/`contest`, else→"not live"; `audit:structure_register.md:80-81` `investigation.py`/`fieldwork.py` are import-orphans; only Stability-Crisis of the 8 §4.3.2 zoom-in triggers is live and it routes to `contest`, never FI (`code:scene_dispatch.py:64-83`) | **[COMPLETE-THE-CHAIN]** | Add a `"fieldwork"`/`"investigation"` `scene_type` branch to `code:scene_dispatch.py` that imports the existing orphan resolvers; the read/write dependency is `scene.scene_type == "fieldwork"` → `investigation.resolve(...)`. Code exists; it needs one dispatch edge. |
| **NG-3** | **#136 L/PS pipeline is SPEC-ONLY-but-uncoded** — V1/V3/V7 (the whole Mandate loop) designed, zero `sim/` | `doc:lps_wiring_v1 §4/§5` complete; `audit:lps_wiring_v1` L/PS 100/100 inert; live sim substitutes scalar `Faction.L` placeholder (`code:parliamentary_vote.py:20` PRE-LPS-1/PORT-BLOCKING) | **[COMPLETE-THE-CHAIN]** | Code `doc:lps_wiring_v1 §5`'s Accounting-boundary sequence into `sim/` (new `sim/territory/legitimacy.py` + rewire `parliamentary_bridge`/Treasury/AP to read the aggregate, not `Faction.L`). Closed-form + oracle-safe per §10. |
| **NG-4** | **Thin decision surfaces** — council member ~2, territory bureaucrat ~2–3, Parliament-as-body ~3–4 verbs (false choice vs the ~4–5 scene-budget bar) | `audit:decision_surface_census_v1 §1,§2,§6` | **[GENUINE-GAP]** (the *fills* — no corpus verb set exists) | Author verb sets from the research corpus's **non-MoH** fills (all cited `research/governance/`): council = propose-ordinance/second-block-peer/petition-up/audit-peer/vote (Signoria+*intercessio*); bureaucrat = dispatch-paired-audit/certify-at-resurvey/allocate-Competence/leak/impeach (*missi*+*transvectio*+*repetundae*); Parliament = Reichsexekution/sequential-curiae-veto/impeachment/mediatization (HRE). Each fill must **emit a down-tier Key** (§5-thinness) or it is decorative. |
| **NG-5** | **Parliament's ruled reach has no built verbs** — §5.3 grants "forcibly impact any province/territory/settlement"; mechanics give a once/arc vote | `audit:decision_surface_census_v1 §6(e)`; `doc:scale_hierarchy_v1 §5.3`; the "armature-binding gap" (`gap_register_v1` Addendum) is its cross-scale-claiming twin | **[GENUINE-GAP]** (verb) **+ [CTC]** (armature binding) | Author a `Reichsexekution`-shaped Domain Action that **emits a coercive Key onto a named settlement/territory** (the down-propagation read/write the census flags absent); bind it to an armature/substrate channel (the RULED-but-unbound §5.2/§5.3 authorities). Widest ruled-reach / built-verbs gap in the census. |
| **NG-6** | **`id_reservations.yaml` duplicate-IN-key hazard persists** | `code:references/id_reservations.yaml:201` — *"⚠ DUPLICATE IN-key hazard persists (a second IN block below, pre-existing) — both synced to next_free=65 so YAML last-key-wins cannot regress; flagged for a proper single-block repair"* | **[COMPLETE-THE-CHAIN]** (hygiene) | Collapse the two `IN:` blocks into one (mirroring the 2026-07-07 FI/SC/FA/WR repair, same file); `next_free` = union max. Until repaired, last-key-wins could silently regress the IN allocation counter — the exact ED-SC-0002 collision class the 2026-07-07 note records. |

---

## §2 · Vertical-axis gap table (keyed to chain_map §1.2 edges V1–V9)

| Edge | State | Evidence | Class | MoH-free fix-direction |
|---|---|---|---|---|
| **V1** char scene → settlement L/PS (aggregate-up) | SPEC-ONLY | `doc:lps_wiring_v1 §4.1` write-source #1 (extend `compute_accord_echo` to carry ΔPS/ΔL); zero callers | [COMPLETE-THE-CHAIN] | Code #136 §4.1; the read/write is the scene-echo emitting a settlement-scoped ΔL/ΔPS Key consumed at the Accounting boundary. |
| **V2** settlement Order → province Accord | **WIRED** | `code:registry.py` floor-mean over real members; `audit:module_contracts.yaml:587` | — | The one live vertical aggregation; extend its pattern to V4's new bands. |
| **V3** settlement L/PS → faction Mandate (LPS-2e) | SPEC-ONLY | `doc:settlement_layer_v30 §1.8` + `audit:module_contracts.yaml:604`; L/PS dead; scalar `Faction.L` placeholder (`code:parliamentary_vote.py:168`) | [COMPLETE-THE-CHAIN] | Code #136 §5 step 3 (W-weighted mean → Mandate); route the vote pool through the aggregate, not raw `Faction.L`. |
| **V4** territory → province → duchy → country | **BROKEN** | `code:key_substrate_v30.md:57` — no enum members exist; `doc:governance_ripple §7 R-3` Territory is "the currently-UNBUILT scale" | [COMPLETE-THE-CHAIN] (blocked on NG-1 + `engine_clock`) | NG-1 enum extension + instantiate each band as a scale instance with the V2 aggregate_fn; blocked on `engine_clock` (H3/doc:null) for tick-ordering. |
| **V5** faction → peninsula (correlated shock) | **WIRED** (contract) | `audit:module_contracts.yaml:64-66,509-518` — `env.peninsular_strain_shock`/`disaster`/`population_change` | — | Live; the one supra-territory scale that IS in the enum. |
| **V6** peninsula → settlement (Cooling pushes Π down) | HOOK-NEEDED | `doc:key_substrate_v30 §12.4` 8 down-seams whose emitters don't populate sub-scale `targets[]`; §12.3 discipline unfulfilled | [COMPLETE-THE-CHAIN] | Populate the emitter's `targets[]` with sub-scale Key addresses; mechanism present, targets sparse. |
| **V7** Mandate → settlement L/PS (mean-reverting drift) | SPEC-ONLY | `doc:lps_wiring_v1 §4.4` `ΔL_drift`; §5 D.6-disjoint sequence; `audit:module_contracts.yaml:608` | [COMPLETE-THE-CHAIN] | Code #136 §4.4/§5 (this IS the GAP-B4 decay term; reads `M_prev` snapshot, writes ±1/Accounting). |
| **V8** char scene → faction stat (Domain Echo) | INERT (WIRED under flag) | `code:scene_dispatch.py:223` + `code:echo_transport.py:118` — fires only if `world.echo_scheduler` attached; default OFF | [COMPLETE-THE-CHAIN] | Attach the echo_scheduler in the default campaign + build the ED-SC-0006 items 1–2 actor-derivation bridge so personal-scale scenes stop deferring. |
| **V9** combat scene → faction (`scene.combat_resolved`/`_felled`) | **BROKEN** (double) | `audit:structure_register.md:18-19` both **dangling emits, no consumer**; `code:scene_dispatch.py:137-145` combat path **always defers** | [COMPLETE-THE-CHAIN] | Add `scene.combat_resolved/_felled` to `npc_behavior`/`faction_state` contract `consumes[]` (the registry already *declares* them, `audit:module_contracts.yaml:861`); author the aggregate→personal-actor bridge for the combat dispatch path. Dangling emit + always-defers = two edges. |

---

## §3 · Horizontal-axis gap table (keyed to chain_map §2.1 edges H1–H6)

| Edge | State | Evidence | Class | MoH-free fix-direction |
|---|---|---|---|---|
| **H1** faction-action → domain/management action | **WIRED** | `code:mc_v18.py:89-97` → `faction_action.py:176-241` (ED-FA-0012) | — | Live strategic loop. **But** its resolver `domain_actions` is `doc:null` (NG-5-adjacent / GAP-H3). |
| **H2** domain action → social-contest (Censure) | **WIRED** | `code:faction_action.py:244-269` → `parliamentary_action.py:136` `run_parliamentary_vote`, unconditional, applies §5.4/§10 penalties, **no ECHO_TRANSPORT gate** | — | Corrects the 2026-07-13 "orphan mutator" premise: `parliamentary_vote` mutates live state every season. Retire that label. |
| **H2′** domain action → composed Domain Echo | INERT (WIRED under flag) | `code:parliamentary_bridge.py:90-122`, called `code:mc_v18.py:109-113` only if `echo_scheduler is not None` | [COMPLETE-THE-CHAIN] | Same fix as V8 (attach scheduler by default). |
| **H3** Stability-Crisis → emergency council | INERT (resolves; echo flag-gated) | `code:scene_dispatch.py:64-83,104-122` (ED-SC-0006 [SEED]); echo lands only under ECHO_TRANSPORT | [COMPLETE-THE-CHAIN] | As V8/H2′. |
| **H4** social-contest → field-investigation | DOCTRINE-ONLY | `doc:scale_transitions_v30.md:90` §3.9 Contest→Fieldwork; no `sim/` realization | [COMPLETE-THE-CHAIN] (blocked on NG-2) | Author the Appraise-success → +1 Evidence-Track write once FI has a live surface (NG-2). |
| **H5** domain/mgmt action → field-investigation (ripple §6.1) | HOOK-NEEDED / INERT | `doc:governance_ripple §13` grades event→FI-lead WIRED on canon; no FI dispatch to consume it | [COMPLETE-THE-CHAIN] (blocked on NG-2) | Wire once NG-2 lands; the lead already writes into concealment inventory. |
| **H6** field-investigation → any subsystem (dispatch) | **BROKEN** | `code:scene_dispatch.py:129-215` no FI branch; NG-2 | [COMPLETE-THE-CHAIN] | = NG-2. FI is the horizontal axis's V4: a whole subsystem the live engine cannot enter. |

**Synthesis edge (chain_map §3) still AT-RISK:** §6.2 event→Parliament/SC predicate has **no
`stakes.source_key` consume-edge** (`audit:module_contracts.yaml:513`) — the live parliamentary paths resolve
*derived* motions, not event-Key-cited ones. **[GENUINE-GAP]** (must be *earned* or *weakened*): author the
`stakes.source_key` input on `social_contest §6`, or downgrade the claim to "a motion may cite the Key." This
is the one edge the ripple substrate's own §9 test flags as resemblance-not-dependency.

---

## §4 · Decision-surface thinness (keyed to census roles; the down-propagation test)

The census applies a second, orthogonal test to every role: does an action **emit a Key that changes the
tier below** (real depth), or only move the role's own stats (**false depth**)? Findings folded as gaps:

| Gap | Role · state | Evidence | Class | MoH-free fix-direction |
|---|---|---|---|---|
| **DS-1** | Council member ~2 verbs; mostly same-scale false depth | `audit:census §1` | [GENUINE-GAP] (fill) | = NG-4 council menu; each verb must emit a settlement-grain `Order`/L-PS or Ledger-tag Key (`doc:settlement_layer_v30 §1.8a`) or it is decorative. |
| **DS-2** | Territory bureaucrat ~2–3; down-reach designed-strong, built-zero | `audit:census §2` | [GENUINE-GAP] (fill) | = NG-4 bureaucrat menu; the *missi*/`repetundae` audit **emits a Demotion-Trigger Key on the governor below** (`doc:faction_politics_v30 §1.0a`) — the corpus's universal non-MoH resolution-quality→standing bridge. |
| **DS-3** | Parliament-as-body ~3–4; ruled reach, no verbs | `audit:census §6` | [GENUINE-GAP] (verb) | = NG-5. |
| **DS-4** | `Develop`/`Fortify` collapse to stat-pumps if the port drops the funding-method sub-choice | `audit:census §3(e)` | [COMPLETE-THE-CHAIN] | Preserve the method sub-choice as the read that hands power to a faction (writes a Precedent tag); the down-propagation lives entirely in the sub-choice. |
| **DS-5** | Same-scale false depth pervasive even in OK roles (Trade/Muster/Diplomacy stat register) | `audit:census §8.4` | [COMPLETE-THE-CHAIN] | Weld a down-propagating side-effect Key onto each Domain-Action verb (the governor tier's Precedent/Grudge/Debt/Reputation-tag template is the model). |

---

## §5 · Vector-audit structural gaps (folded)

| Gap | Finding | Evidence | Class | MoH-free fix-direction |
|---|---|---|---|---|
| **VA-1** | **9 `doc:null` modules**: `engine_clock`, `domain_actions`, `scene_slate`, `game_director`, `scenario_authoring`, `npc_memory`, `scene_timer`, `settlement_economy`, `audit` | `audit:structure_register.md:51-62` | [GENUINE-GAP] (author) | Author home docs. **`engine_clock`** (temporal spine — sequences every V-axis accounting boundary; `doc:lps_wiring_v1 §5` depends on it; candidate home `propagation_spec_v1`) and **`domain_actions`** (H1's resolver home; candidate home `governance_play_redesign_v1 §1.3`, the 13 governor verbs) are the two load-bearing ones. |
| **VA-2** | **4 dangling emits (canon-grade)**: `mass_battle` `scene_outcome.battle_concluded`; `peninsular_strain` `env.crisis`; `personal_combat` `scene.combat_resolved`/`_felled` | `audit:structure_register.md:16-19` | [COMPLETE-THE-CHAIN] | Add each to a consumer's `consumes[]`. The two combat Keys ARE V9 (confirmed dangling from the contract side too). Note: the docket brief's "6 dangling-emit" counts the F2-class unregistered emits (`scene.draft_da`/`scene.displacement`, `audit:module_contracts.yaml:489,147`) which the register does not grade canon — 4 canon + 2 F2-class. |
| **VA-3** | **4 unregistered-canonical heads** — declare CANONICAL, absent/blind-spot in `canonical_sources.yaml`: `fractional_province_ownership_v30`, `social_contest_v30`, `march_layer_v30`, `settlement_adjacency_v30` | `audit:generation_register.md:43-48` | [COMPLETE-THE-CHAIN] (hygiene, but verify body `**Status:**` first) | Register under a `DOC_KEYS`-matching key; the generation register warns several carry a CANONICAL heading contradicted by a later `**Status:** PROVISIONAL` body line — verify before registering. Sibling of 2026-07-13 GAP-H2. |
| **VA-4** | **1 currency-drift**: `combat_v30.md` registered as canonical head AND recorded superseded | `audit:generation_register.md:13` | [COMPLETE-THE-CHAIN] (hygiene) | Resolve via `CURRENT.md` — combat head is `combat_engine_v1/`; drop `combat_v30`'s canonical registration (it is PARTIALLY SUPERSEDED, CLAUDE.md §4 hazard). |
| **VA-5** | `franchise_v30`/`fractional_province_ownership`/`insurgency_pipeline`/`faction_succession_split` orphan from CURRENT.md; 16 stale version-pointers in 7 live heads (10 mechanical repoints, 5 need a human) | `audit:generation_register.md:15-34`; 2026-07-13 GAP-F1/H1/H2 | [COMPLETE-THE-CHAIN] (hygiene) | Re-index into CURRENT.md + repoint the 10 restructure-ledger-mapped citations; the 5 nonexistent-target citations need a human. |

---

## §6 · Carried 2026-07-13 gaps not re-litigated here

The 2026-07-13 register's ~24 gaps (A1–H3, F6/F7) stand as filed; this v2 extends rather than replaces it.
Unchanged-and-still-open highlights the DESIGN pass inherits: **GAP-A1** transfer BROKEN (COMPLETE-THE-CHAIN,
wire `parliamentary_transfer` to the seasonal vote — territory is a one-way ratchet until then, and note the
"~87% win-share" it was conflated with is a **debunked small-N artifact**, corrected golden dist 37.5/12.5/12.5/37.5
per `audit:test_f7_smoke_oracle.py`); **GAP-C2** governance-mode taxonomy (GENUINE-GAP, the 8-value FLAG domain
the census leans on throughout); **GAP-D1** unranked chain-bypass authorities (GENUINE-GAP, Bodin);
**GAP-G2** suppression-backfire (GENUINE-GAP, seven mechanisms). Their classifications and precedents are
authoritative in `gap_register_v1.md` / `precedent_fix_catalog_v1.md` and are **not** duplicated here.

---

## §7 · RE-GROUNDING the MoH-grounded gaps on non-MoH precedent (BINDING)

The 2026-07-13 docket grounded GAP-E1/E2 and GAP-B2 on Mandate-of-Heaven. Per the design-lead ruling, MoH is
**historical grounding only** and must not appear as a proposed Valoria mechanic. The
`research/governance/conflicts_power_struggles.md` corpus supplies clean non-MoH groundings with the *identical
cross-scale structure* — the resolution is real because each is a specific two-signal **read** dependency (an
objective-strain Key AND an independent legitimating-authority Key must co-fire), not a thematic resemblance.

### GAP-E1/E2 · two-signal collision primitive — RE-GROUNDED

The requirement is unchanged (a Mandate-tier event fires only on the **resonance of an independent material
signal AND an independent interpretive/legitimating signal** arriving together), but the precedents are now
endogenous political-military dynamics, no cosmic-mandate theology:

| Non-MoH grounding | Material signal (bottom-up read) | Interpretive/legitimating signal (independent read) | Cite |
|---|---|---|---|
| **Roman Gracchan rupture** (133/121 BC) | land/debt distributional crisis | re-election bid *read by the Senate as a bid for kingship* → SCU (ad-hoc non-chartered emergency bypass) | `research:conflicts §1` |
| **Roman Year of Four Emperors** (69 AD) | no designated heir + treasury (un)able to pay the donative | a legion's **acclamation ritual** (`arcanum imperii`) | `research:conflicts §4` |
| **Ottoman Janissary deposition** (1622/1687/1703) | military defeat / fiscal strain / reform threatening the corps monopoly | an independent **Şeyhülislam fatwa** converting mutiny → legitimate correction | `research:conflicts Ottoman §Janissary` |
| **Carolingian 887–888** | ruler's demonstrated failure of core deliverable (Paris tribute, military protection) | accumulated near-rank-cap Standing of regional magnates who no longer need Crown patronage | `research:conflicts Carolingian §3.8` |

**Verifier-confirmed clean:** the Roman brief carries an explicit "MoH leakage: NONE — confirmed clean"
verdict, framing the mechanism as **army-loyalty fission**, never "legitimacy draining from above." Additional
enrichment for **GAP-D1** (unranked bypass): the corpus surfaces a **third bypass-adjacent authority** — the
Şeyhülislam's *standing ideological/juridical* seat outside the chain (`research:conflicts Ottoman §fatwa`) —
distinct from Monarch and Parliament, plus the Roman SCU as an *ad-hoc emergent* non-chartered bypass. *(MoH
`zaiyi` two-channel resonance — historical grounding only; do not port.)*

### GAP-B2 · Mandate-collapse relief-valves — RE-GROUNDED

Both valves are read/write actions on the same collapse pipeline (they bleed pressure short of an
all-or-nothing uprising), re-grounded off MoH:

- **Scapegoat valve** → **Venetian graduated-removal ladder + procurator sinecure** (soft rebuke → forced
  co-signature → deposition; a subordinate/sinecure *absorbs blame*) **and Ottoman grand-vizier-as-scapegoat +
  Janissary revolt** (`research:conflicts §synthesis "relief valve"`, hooks table row "Graduated removal
  ladder"). Read/write: an appointee absorbs the legitimacy hit at the cost of *their* Standing Key (a
  bend-around onto a named seat). Rome's Crisis of the Third Century, *lacking any such valve*, cascaded — the
  negative control (`research:conflicts §6`).
- **Self-reproach valve** → **Roman *recusatio* + imperial penance under Ambrose** (ritual self-abasement as a
  legitimacy-restoring move a drifting ruler performs; `research:conflicts hooks table "Ritual self-abasement"`).
  Read/write: an L/PS-priced ritual action spending the *ruler's own* resource, distinct from deposition. *(The
  Chinese self-critical penitential edict is historical-only, explicitly flagged non-proposed in the corpus.)*
- **Decay term (GAP-B4)** → **Polybian anacyclosis / regime-cycle** as *confirmatory* grounding that a
  legitimacy which only ratchets up is a modeling error (`research` synthesis; the fix itself is the
  chain-completion #136 §4.4 drift term, precedent confirmatory only).

**Devolution output (not a stat flip):** the collapse's real output is a **cross-scale power devolution**
(national → province/territory), grounded on Roman recognition-fission (Palmyrene/Gallic Empires,
`research:conflicts §6`) and reusing the A1 transfer resolver + F5 fracture-resolution — *not* MoH warlordism.

---

## §8 · Consolidated tally

| Class | Count | Where the mass sits |
|---|---|---|
| **[COMPLETE-THE-CHAIN]** | ~19 | The wiring spine: #136 impl (V1/V3/V7/A2/B1/B4), FI dispatch (NG-2/H4/H5/H6), scale enum (NG-1), echo-by-default (V8/H2′/H3), combat-echo consumers (V9/VA-2), all hygiene (NG-6/VA-3/VA-4/VA-5) |
| **[GENUINE-GAP]** | ~8 | Undesigned mechanism/authoring: thin-surface fills (NG-4/DS-1/DS-2/DS-3), Parliament verbs (NG-5), `stakes.source_key` predicate (§3), `engine_clock`/`domain_actions` doc:null (VA-1), A4 convergence *proof* |
| **carried (2026-07-13)** | ~24 | `gap_register_v1.md` — A1, C2, D1, G2 et al., not re-litigated (§6) |

**Bottom line.** The paper substrate is far ahead of the running one. Everything the docket most wants —
a settlement-grounded Mandate rippling up through province/duchy to country and back down, and Field
Investigation as a first-class response surface — is now either **SPEC-ONLY and ready to code** (#136, the
single highest-leverage PR) or **BROKEN at the substrate** (the 4-of-6 scale enum) or **absent from dispatch**
(FI). Coding #136 + extending the scale enum + adding the FI dispatch branch is what makes chain_map §3's two
columns agree. Nothing here edits canon; this is FILED analysis handing ranked calls to the DESIGN pass
(`decision_queue_delta_v1.md`).
