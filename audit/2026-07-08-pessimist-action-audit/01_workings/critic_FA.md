# FA Lane — Inverted Critic Pass (Sonnet, independent)

Method: for each condemned action (verdict != KEEP) I attempted the strongest honest case for KEEP, judged as-if-built per the charter's cardinal rule, then checked every verdict (condemned and KEEP alike) for any reliance on build-state as evidence. Findings below.

## Build-state audit (all 18 actions)

No verdict was found to rest on build-state as evidence. The dossier is disciplined about this: `build_state_note` is used correctly as routing metadata on Muster, the da.* taxonomy, and the Faction-unique cluster, and in each case the actual `criterion`/`one_line` cites a design-intrinsic fact (dampers as-specified, catalog duplication, prose-catalog completeness) rather than what's currently wired. No correction needed on this axis.

## Condemned actions — steelman attempts

### 1. da.* Key contract taxonomy — REFINE → **UPHELD** (reasoning partially corrected)
Steelman: `module_contracts.yaml` (domain_actions module, lines 479–501) shows the `da.*` tags are Key-emission types on the substrate's event bus — the same pattern every other module in the file uses (`env.population_change`, `scene.draft_da`, etc.) to let downstream consumers (faction_state, npc_behavior) subscribe generically without knowing every emitting verb. That is **not** a second catalog of the *player's* decision space; it serves a different consumer (inter-module routing) than the prose Standard Action tables serve (player choice), the same relationship March/Conquest has to the MB resolver (which the dossier itself KEEPs as "intentional layering, not duplication"). Framing this as "N: Duplicate coverage" overstates it — the taxonomy is architecturally necessary and analogous to other emits: no other module's Key-type list gets flagged as a duplicate catalog.
However, the steelman does **not** dissolve the dossier's sharper point: bucket-boundary ambiguity (is Suppress economic_intervention or public_governance?) is a real, as-specified Q-elegant defect independent of the duplication framing — a crosswalk from ~35 concrete verbs to 5 buckets is currently undeclared, and that gap would remain even fully built. That alone earns REFINE.
**Verdict stands at REFINE, but on Q-elegant grounds (undeclared verb→bucket crosswalk), not "duplicate coverage."** The remedy is smaller than the dossier's framing suggests: author the crosswalk table, not re-architect domain_actions as an independent system.

### 2. Investigate/Intel + Spy (Tribune) — REFINE → **UPHELD**
Steelman: cross-lane overlap with FI's Observe/Surveil is speculative on the dossier's own admission, and most actions in this lane don't spell out an explicit failure branch either (Govern/Trade don't get flagged for this) — "failure = no information gained" could be read as an adequate implicit consequence, with the action-slot spend itself satisfying Ω-d's "pays what it buys." That's a real mitigating point for Investigate/Intel generally.
But Spy is called out specifically, by name, as the one entry with **no stated Failure branch at all**, in explicit contrast to Survey (which has one) in the same dossier row. Where a sibling action in the same design space (Survey) demonstrates the corpus's own convention of specifying Failure, Spy's silence is a real, as-specified gap, not a house style the dossier is inventing. The ask (add an explicit Failure clause to Spy) is narrow and doesn't threaten the action's existence.
**REFINE stands**, severity P2 is appropriate — this is spec-completion, not existential.

### 3. Diplomacy between players (informal, no roll) — DISTILL → **UPHELD**
Steelman attempted: is the Standard Action row a lighter-weight, non-binding lever distinct from formal Treaty-initiation (i.e., relationship-building talk that never becomes a Treaty)? `phases.md` lists "Diplomacy" as its own Social-priority action type alongside Decree/Parliamentary Manoeuvre, which could support a standalone reading. But `faction_layer_v30` §3.2 frames Treaty-initiation itself as an unnamed "Senator (Social) action," and §3.3/§3.8's own prose states verbatim "Treaty Phase 2 (Concession declaration) = player negotiation at table; no roll" — textually identical to `core.md`'s "Diplomacy between players | Negotiated | Not a roll." I could not find textual support for a distinct standalone-Diplomacy use case that doesn't collapse into Treaty's Concession phase; my best case required speculating past what the corpus actually says.
**DISTILL stands** — fold the row into Treaty §3.3 Phase 2 rather than retaining a separate Ob-table listing.

### 4. Parliamentary Motion — punitive cluster (Censure/Embargo/Blockade/Combined/Outlawry) — DISTILL → **UPHELD**
Steelman: the five cards are not perfectly homogeneous — Blockade uniquely gates on Military 3 (not just Mandate), targets a different resource mix (Wealth *and* Military garrison), and Outlawry uniquely grants Casus Belli to *all* factions (a categorically different effect — it changes who can act militarily against the target, not just how hard the target is hit). These are real, non-cosmetic differences, and for a moment they looked like grounds to pull at least Outlawry and Blockade out of a "just a severity dial" framing.
On reflection, though, none of these differences resist parameterization: eligibility gate (Mandate-only vs Mandate+Military), duration (one-time/ongoing/permanent), vote threshold (Majority/Supermajority), and a special-clause slot (CB-to-all for Outlawry) are exactly the kind of fields a single parameterized "Sanction" action template carries without loss — and the design's own "Combined Embargo+Blockade" entry is direct textual proof it already treats severity as compositional/stackable, not five independently-invented mechanics. A one-paragraph restatement of the unified template ("propose a Motion at a chosen severity tier, gated by Mandate/Military threshold, costing the proposer resources scaling with tier, lasting until lifted or permanently") is genuinely Q-elegant in a way five separate named rules are not.
**DISTILL stands.** One refinement to the remedy: the unified template's "special clause" field must explicitly preserve Outlawry's CB-to-all effect and Blockade's Military-gate as first-class parameters, not silently drop them — the dossier's own retires_downstream language ("without losing any real choice") already anticipates this, so no verdict change, just an execution note.

### 5. Claim Masterless units — DISTILL → **UPHELD**
Steelman: Conquest (military_advance) is a *contested* action against a defended, Fort-scaled territory, resolved via the MB mass-battle engine, with a four-degree outcome ladder and no permanent loss on failure (the marker just stays, retry later). Claim Masterless is *uncontested* (units "hold position but take no orders" — no defender, no Fort level, flat Ob 2), binary Success/Failure, and failure **permanently disbands the resource** — a genuinely different risk shape (a race against rival claimants, not a siege against a defender). This is a real difference in decision texture, not pure cosmetics, and for a moment argued against folding it silently into Conquest's ladder.
But the difference is narrowly scoped to one specific, rare trigger window (a faction's collapse aftermath) and doesn't require its own resolver, contest structure, or Fort-level table — it needs one conditional clause ("if target territory holds only Masterless units, use flat Ob 2, binary outcome, Failure = disband instead of retry") layered onto Conquest's target-selection, not a fully independent §1.5 rule. That is squarely what DISTILL's fold-in remedy already describes, and the dossier's own retires_downstream text ("decision content survives inside Conquest's target-selection") already accommodates preserving the distinct failure branch.
**DISTILL stands.**

### 6. "Thread Operation" listed as an FA-scale Standard Action (Pontifex/Weaver) — PRUNE → **DOWNGRADED to REFINE**
Steelman: `core.md` line 220 gives this row an actual FA-scale value — "Ob 2 base... See PP-182 co-movement protocol" — not merely a re-statement of TW's `attempt_*` mechanics. That is analogous to how March/Conquest's FA-owned Fort-level Ob table (§2.2) legitimately sits in FA even though MB owns the actual battle resolution (a relationship the dossier itself KEEPs as "intentional layering, not duplication"). A co-movement/synchronization protocol between a Thread-practitioner's personal-scale movement and the faction's action economy is plausibly genuine FA-scale integration content — the interface point, not a duplicate of TW's resolver — and the dossier's own text concedes "the eligibility rule... is legitimate."
This changes the calculus from PRUNE (remove the row) to REFINE (keep the row, but re-anchor its authoring so it reads unambiguously as a cross-scale interface note — the FA-side slot cost and PP-182 sync rule — with the actual operation mechanics single-sourced to TW, rather than appearing as if FA is independently cataloging the whole action). The dossier's prescribed remedy ("cross-reference instead of re-listing") is in practice identical to this REFINE framing — the label PRUNE overstates what the fix actually does, since no mechanical content is being deleted.
**Verdict changed: PRUNE → REFINE.** Retains the Ob-2/PP-182 content as FA's legitimate interface-layer contribution; the action item is presentation/single-sourcing, not removal.

## KEEP spot-checks (no full steelman required, per charter)

- **Muster** — correctly treats the sim-oracle's missing dampers as build-state (`build_state_note`), and the verdict properly rests on the *design as specified* pairing Muster with a ceiling/Wealth-gate/Accord-decay trio. No over-generosity found; P2 severity appropriately flags that non-dominance is contingent on all three dampers actually shipping together, which is legitimate design-risk language, not a build-state citation.
- **Faction-unique special actions cluster** — explicitly and correctly distinguishes the sim's Crown/Church-only AI wiring (build state) from the prose catalog's full Hafenmark/Varfell/Löwenritter/Restoration rosters (design). Good discipline; no correction needed.
- **March/Conquest** and **Treaty** — both KEEPs are well-supported by explicit textual cross-scale mechanisms (Domain Echo, Grand Debate feedback, Trigger-5/officer-capture cascade) cited in the dossier; spot-checked against the source docs above and found accurate, not inflated.
- **Parliamentary constructive cluster** — Recognition Challenge's flagged "-1 TCV only" thinness is real (confirmed no other stated world-state hook in the reviewed text) but correctly kept at KEEP with a flagged refinement rather than demoted; consistent treatment with the punitive cluster's harsher DISTILL, since the constructive cluster's five levers genuinely target different objects (patronage / war-sanction / treaty-legitimation / legitimacy-contest / succession) rather than one dial.

## Summary of changes from this critic pass

| Action | Dossier verdict | Critic verdict | Outcome |
|---|---|---|---|
| da.* Key contract taxonomy | REFINE | REFINE | UPHELD (criterion re-anchored: Q-elegant crosswalk gap, not "duplicate coverage") |
| Investigate/Intel + Spy | REFINE | REFINE | UPHELD |
| Diplomacy between players | DISTILL | DISTILL | UPHELD |
| Parliamentary punitive cluster | DISTILL | DISTILL | UPHELD |
| Claim Masterless units | DISTILL | DISTILL | UPHELD |
| Thread Operation FA listing | PRUNE | REFINE | **DOWNGRADED** |

All other actions (12) are KEEP, unchanged, spot-checked without full steelman per charter instruction.

