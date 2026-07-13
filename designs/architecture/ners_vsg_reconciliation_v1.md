# NERS-Review / VSG Reconciliation (v1) — merging the harness-verification empirical branch with the generation-methodology design branch

## Status: D1–D6 RATIFIED (D1–D5: ED-IN-0046; D6+B1: ED-IN-0047) · B2 context-gathered, awaiting Jordan · B12 surfaces a real conflict with existing Class A canon, unresolved — 2026-07-13 · Lane: IN (cross-cutting SE, FA) · Extends `governance_consolidation_v1.md` (now itself updated to record the same rulings) and folds `generation_sourcebook_v1.md`'s blocker register into one surface. See §5 for the full, twice-updated ruling record — nothing was inferred or fabricated for B2/B12; both await direct Jordan input.

**What this is.** Two independent PRs landed on `main` within the same session window and were never
cross-read against each other:

- **PR #127** (`designs/audit/2026-07-12-pr119-harness-verification/`) — the **empirical branch**. 19
  `tools/sim_harness/` adapters that ran PR#119's twelve authored items, the governance-compendium's
  Ascendancy system and proactive-governance menus, and all 9 promote-ready-but-unlanded proposals
  against **real, executing code** (`sim/territory/registry.py`, `ledger.py`, `infrastructure.py`) and
  the real Goldenfurt fixture — then NERS-audited every one of the 29 tested proposals (narrative
  emergence review + N/Ω/Q audit + inverted-critic steelman) in `narrative_ners_review.md`.
- **PR #128** (`designs/territory/settlement_generator_v1.md` + `generation_sourcebook_v1.md` +
  `goldenfurt_slice/generation_methodology.md`) — the **design branch**. A retrospective account of how
  Goldenfurt was actually authored (a vectorized-slice-stack with noisy throughlines), reified into
  **VSG v1**, a proposed 15-paradigm generator, plus a grounding sourcebook proposing parallel faction
  and territory generator stacks and a 10-item blocker register (B1–B10).

Both branches independently converge on **`designs/architecture/governance_consolidation_v1.md`**
(D1–D5 decisions, E1–E7 extensions) as their shared ancestor — PR#127's harness README cites its
reconciliation memo verbatim as the grounding mandate; VSG's death-spiral invariant is a direct port of
its E1. Neither branch, however, ever read the other's actual output. **This document is that read.**
It does three things: (1) cross-checks VSG's design claims against PR#127's execution evidence and
flags where they agree, sharpen each other, or disagree; (2) merges `governance_consolidation_v1`'s
D/E register with `generation_sourcebook_v1`'s B register plus new items PR#127's execution surfaced,
into one deduplicated blocker list; (3) proposes a single sequenced workplan across both branches.

Per CLAUDE.md §1 (ED-1094): nothing here is silently held back — every place this document disagrees
with an existing PROPOSED call is marked **CHALLENGES**, not quietly overridden, and every open item
routes to an explicit Jordan-facing ask in §5.

---

## §1 · Where execution confirmed the design (convergent findings)

| Claim | Design-branch source | Empirical-branch evidence | Verdict |
|---|---|---|---|
| **Compact should be a recurring `Debt` subtype, not a 6th ledger family** (D3) | `governance_consolidation_v1 §1 D3` | `pr119_ledger_family_collision.py`: writing `Compact` through the real `ledger_add()` against the built `TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}` silently accepts the unrecognized kind **100/100** trials — no error, no downstream visibility. Independently reconfirmed under VEN-SE-2's Reading A (**59/100** trials route through the same collision). | **CONFIRMED**, and sharpened from "a naming drift to fix" to "a live schema-corruption bug two-thirds of the time under one plausible reading" |
| **§1.0d Performance Audit should merge into the suspicion/recall spine, not run parallel** (D5) | `governance_consolidation_v1 §1 D5` | `pr119_integrated_campaign.py`, 3 regimes × 500 trials: G606 (cumulative suspicion) drives **100% of terminal recalls in the most lenient §1.0d tuning tested** — leniency tuning on §1.0d doesn't move the outcome at all, because G606 alone is sufficient and dominant. | **CONFIRMED**, and sharpened: this isn't "§1.0d duplicates G606," it's "§1.0d currently contributes ~nothing once G606 is live" |
| **L/PS is inert in `sim/`** (E5, `governance_consolidation_v1 §3`) | same | `lps_inert_check`: zero `.legitimacy`/`.popular_support` reads anywhere outside field declarations, **100/100**. | **CONFIRMED** at the same rate the design doc asserted qualitatively |
| **The card-deck is the player-facing engine of record; predicate-sweep is the batch oracle** (D1) | `governance_consolidation_v1 §1 D1` | `event_architecture_fork` check: both `_PREDICATE_SWEEP_DIR` and `_CARD_DECK_DOC` present, **100/100**, and no file anywhere states this division. `pr119_event_deck_engine.py` is the first artifact to actually **build** the card-deck side (13 of 28 cards) rather than assert it should be canonical. | **CONFIRMED as a design call**, but D1's resolution ("kept in sync by a small overlap map") is still **unexecuted** — see §2 B8 |
| **Goldenfurt's Π restoring term + recall escape are "already designed, just needs porting"** (E1) | `governance_consolidation_v1 §3 E1`, framed "No new design — a port" | Four independent measurements (500-seed isolated homeostat test, 1500-trial integrated campaign, the event-deck engine, and two prior methodologies — PR#125's narrative sim and the 500-seed `settlement_mgmt_stress_01` batch) **all** converge: the *unaugmented* `sign(3−Π)·min(1,|3−Π|)` term pins every settlement at the pressure ceiling (`death_spiral_log.py`: **298/300**, `PI_RUNAWAY_SUSTAINED`). It does not de-fang the runaway pattern on its own. | **CHALLENGES** E1's "just a port, no new design" framing and its Phase-P placement (§4 below) — see §3 |

**What this means for VSG specifically:** VSG's §4 "Anti-failure invariants baked in" already bundles
the Π term with "a subsistence-floor clamp + a G606-style survivable-recall escape" (i.e., E3 and an
E7-adjacent element) rather than porting CG-1 alone — so VSG's *design instinct* was already correct
that CG-1 needs company. PR#127's numbers are the missing validation that this bundling is
**necessary, not optional polish**: E1 cannot ship, in VSG or anywhere else, without E3 and E7 landing
in the same commit.

---

## §2 · Merged blocker register (D/E from `governance_consolidation_v1` + B from `generation_sourcebook_v1` + new items from PR#127)

One register, deduplicated. `D` = a Jordan decision; `E` = a design-level extension/fix once decided;
`B` = a generation/build-substrate blocker. IDs preserve the source doc's numbering where they already
existed; new items continue each series.

### Decisions (Jordan-gated, block everything downstream)

| ID | Decision | Source | Status after PR#127 |
|---|---|---|---|
| D1–D5 | Event architecture · AP economy · Compact-as-Debt · Mandate-carrier retirement · §1.0d merge | `governance_consolidation_v1 §1` | D1, D3, D5 empirically confirmed (§1 above); D2/D4 untouched by this pass, stand as recommended |
| **D6 (NEW)** | **Which G606 wiring model ships:** clock advances on *every non-compliant season* (the integrated-campaign reading — recall dominates near-totally) vs. advances only *on a specific card draw* (the event-deck-engine reading — recall cascades almost never fire, `collapsed_repeated_recalls` never triggered even at 30 seasons). These are two meaningfully different felt games, not two implementations of one spec. | `pr119_integrated_campaign.py` vs `pr119_event_deck_engine.py`, both cited in `narrative_ners_review.md`'s closing synthesis | **OPEN — no existing doc rules this.** Feeds directly into D5's "one signal, one recall scene" resolution: D5 can't finish specifying *how* the signal advances without D6. |
| B1 | Faction count 4–8 unreconciled | `generation_sourcebook_v1 §5`; `faction_layer §587` | untouched by this pass; still blocks VSG's F-stack and P2 |
| B2 | S-006 triple-booked across `valoria_geography_v30.yaml` (T3 Lowenskyst), `settlement_layer_v30 §2.1` (Goldenfurt Town, Kronmark/T2), `§5.1` (Lowenskyst Fortress) | `generation_methodology.md §7`; `generation_sourcebook_v1` B2 | **Every PR#127 adapter used the Goldenfurt/T2 identity as unquestioned ground truth** — none of the 19 adapters, nor the NERS review, flagged this. VSG's own calibration test (§5 of `settlement_generator_v1.md`) is gated on resolving it first. Cheap, editorial, and now blocks *two* independent bodies of work — raise its priority. |

### Extensions / execution items (design-level, once their gating D is ruled)

| ID | Item | Source | PR#127 update |
|---|---|---|---|
| **E1+E3+E7 (RESEQUENCED)** | Port the Π restoring term **together with** the subsistence-floor clamp (E3) and a systemic positive-feedback path (E7) | `governance_consolidation_v1 §3` (originally E1 alone in Phase P, E3 in Phase C, E7 in Phase D) | §1 above: the split sequencing is now known-wrong. These three cannot land independently — E1 without E3/E7 measurably still death-spirals. **Recommend collapsing Phase P and Phase D's E7 item into one bundled port**, see §4. |
| E2 | Author the Mandate-Challenge (political, non-violent Seggio removal) | `governance_consolidation_v1 §3` | `pr119_subnational_factions.py`'s `za_patron_lapse` (66/16/18) independently validates the *sibling* §3.3b mechanic is sound, strengthening the case that §3.3c's missing political off-ramp is a real, isolable gap and not a sign the archetype needs rethinking. No change to E2's scope. |
| E4 | Resolve Compact (rides D3) + the §1.3b population-granularity layer | `governance_consolidation_v1 §3` | `pr119_bind_the_cells.py`: 9 real Goldenfurt actors mod 5-household cells = remainder 4, **100/100**; cascade to "Cell Revolt" in **32/100** trials over 6 seasons. This is non-degenerate, dramatically legible content — the NERS review's REFINE verdict (bind *named actors*, give the remainder an explicit "uncelled" status) is a **sharper, more specific fix than E4's current "define cells over a household layer" framing**, which risks inventing a granularity the engine will never track. Recommend E4 adopt the NERS review's named-actor scoping directly. |
| E5 | Wire L/PS | `governance_consolidation_v1 §3` | Confirmed inert at 100/100 (§1). No change to scope, but now has a hard number backing its priority, and it gates more than governance_consolidation_v1 knew: it also blocks verifying VSG's own P11 (Political allegiance) and P12 (Sociopolitical sympathies) Ω-a claims, since those paradigms are specified to read L/PS-adjacent state. |
| E6 | Close type-taxonomy drift (Village/Fortress-City/Cathedral-City) | `governance_consolidation_v1 §3`; = sourcebook **B3** | Untouched by PR#127's adapters directly, but VSG's P4 paradigm depends on one canonical type set to sample over — this is now a **shared precondition for both branches**, not just a settlement-content cleanup. |
| **E8 (NEW)** | **Reconcile IT-2 Condotta's Aspetto ×0.5 Mil clause against all four real `faction.Mil` read sites** — `_mil_advantage_signal` (`faction_action.py` ~line 142), the `CONQUEST_MIN_MIL` gate (~lines 192/341), the muster-pool formula (~line 416), and `massbattle.py::_faction_to_unit`'s `power=int(faction.Mil)` (~line 1875) | `pr119_promote_ready_fiscal.py`, NERS review | New — none of the source docs named all four sites; the closure register had already named them, but the NERS review adds that **83/100 trials sit in the Lapsed state whose Mil-pool consequence is least defined**, so this is live most of the time, not an edge case |
| **E9 (NEW)** | **Author a Ministry priority-action economy** (what a Ministry's action capability is, where its AP/Competence comes from) before HAB-4 Overlapping Consulta Arbitration can be trusted to generalize beyond the tested domain | `pr119_promote_ready_political.py`, NERS review | New — HAB-4's own two headline probabilities (30/35/35 agenda-set/ratify/paralysis split) are real and non-degenerate, but stand on an unauthored foundation |
| **E10 (NEW)** | **Give HRE-2 Chapter Capture an explicit acquisition cost** (AP spend, Disposition stake, or discovery-exposure risk per season banked) — as pitched it is an 81%-favorable uncosted bet over a 10-season tenure | `pr119_promote_ready_political.py`, NERS review | New — CHALLENGES the closure register's "clean KEEP, Promote as pitched" call specifically on Ω-d; everything else about HRE-2 (N, Ω-a, Ω-c, Q-elegant) is confirmed |

### Generation/build-substrate blockers (from `generation_sourcebook_v1`, updated)

| ID | Blocker | Update after PR#127 |
|---|---|---|
| B4 | Inert L/PS (= E5 above) | Confirmed 100/100, see §1 |
| B5 | No settlement-scale Key vocabulary | untouched |
| B6 | No spatial substrate | untouched |
| B7 | No typed engine-params schema | untouched |
| **B8** | "Event-deck engine S3–S6 unbuilt... zero-code" | **STALE.** `pr119_event_deck_engine.py` is real, committed, working code: a 13-of-28-card subset with trigger/cooldown/response dispatch, the Π homeostat, and per-NPC ambition ticks (`hedda_progress`/`konrad_progress`/`orsk_progress`) wired in, validated across a 6-point skill sweep (skill 0.0 → 82% ruin/18% steady/0% prosper; skill 1.0 → 100% prosper). It is a **test harness proving the S3–S6 concept**, not the production spec (Directive generator, full 28-card set, card-format schema are still unbuilt) — B8 should be re-scoped to "extend the proven 13-card harness to the full 28-card production spec," not restated as zero progress. |
| B9 | Geography YAML `settlements:` block stale 36-scheme | untouched |
| B10 | VSG depends on `governance_consolidation_v1 §6` D1–D5 | now also depends on **D6 (NEW)** above |
| **B11 (NEW)** | `engine_clock` unauthored (`doc: null` in `module_contracts.yaml`, per CLAUDE.md §6) blocks more than previously scoped: it's the sole blocker on Part 41's Relay Tier/Beacon Network — "the single strongest new-state case in the corpus" per the NERS review — and by extension on VSG ever generating a cross-settlement Territory-scale mechanic that actually fires at runtime. | `pr119_proactive_governance_menus.py`: `relay_tier_temporal_dependency` → `contingent_on_unauthored_engine_clock`, **100/100** |
| **B12 (NEW)** | **Naming collision, unconfirmed either way:** `generation_sourcebook_v1 §1.3`'s TERRITORY/PROVINCE stack (R1–R9, a geographic/administrative generation layer — duchy, temperament, calamity exposure) and Part 41's "Territory" **proactive-governance scale** (connective tissue between settlements — Beacon Network, Cordon, shared reserve) use the same word for what may or may not be the same underlying entity. Neither document cites the other. | Surfaced by cross-reading both branches for this document; not tested by any adapter |

---

## §3 · The one place this document overrules a design-branch sequencing call

`governance_consolidation_v1 §4`'s phase plan places **E1 alone in Phase P** ("highest leverage, no
new design — a port") and defers **E3** to Phase C and **E7** to Phase D. That sequencing assumed E1
was sufficient on its own; §1's four-measurement convergence shows it is not — the *isolated* Π term,
ported exactly as specified, still pins every settlement at the ceiling. Shipping Phase P alone would
mean shipping a "fix" that doesn't fix the thing it was ported to fix, and the gap wouldn't surface
until a much later phase's testing caught it — exactly the failure this reconciliation exists to
prevent. **Recommend**: collapse E1+E3+E7 into one bundled Phase-1 deliverable (§4). This is a
sequencing correction, not a reversal of E1/E3/E7's content — none of the three change scope.

---

## §4 · Proposed workplan (single sequence across both branches)

```
Phase 0 — Jordan rulings (unblocks everything; nothing below can start clean without these)
  D1 D2 D3 D4 D5 D6(NEW)   governance decisions, extended with the G606-wiring fork
  B1                        faction count 4–8
  B2                        S-006 identity (cheap, editorial — recommend resolving THIS WEEK,
                             independent of the other rulings; two branches are already blocked on it)
  VSG §7 open calls          settlement-grain temperament promotion · off-owner allegiance as a
                             generation axis · load-bearing-paradigm count · weight/τ calibration

Phase 1 — Bundled death-spiral port (resequenced per §3; no new design, but must land together)
  E1 + E3 + E7               Π restoring term + subsistence floor + recovery/positive-feedback path,
                             ported as one commit, smoke-tested against the death_spiral_log.py
                             thresholds (Π≥9, ruin-rate) before merge, not after
  E6 / B3                    type-taxonomy fix (Village/Fortress-City/Cathedral-City → §1.2) —
                             shared precondition for VSG's P4 paradigm too

Phase 2 — Ratify the clean set (ordinary-merge ratifiable once Phase 0 clears)
  1.0c · 2.5a · 1.3c · 3.3b · substrate · deck-architecture      (governance_consolidation Phase A)
  HRE-4 Borrow · HAB-1 Corregidor · HRE-3 Convene the Circle (refined form) · CHN-6 Gongsuo
  (merged form)               — the promote-ready items PR#127's NERS review returned a clean KEEP on

Phase 3 — Refine-then-ratify (design-level fixes, each independently scoped and now sharper)
  1.0b (+E10 acquisition-cost analogue for HRE-2)
  1.1a (+ the measured CC0–CC1 AP-curve target from pr119_clerk_capacity.py)
  3.3c (+E2 Mandate-Challenge)
  1.3b (+E4, now scoped to named-actor cells per the NERS review, not a household layer)
  VEN-SE-2 Requisition        — resolve the Reading A/B fork (ships as Reading B, immune-directive,
                               unless D3's resolution changes the calculus — see §1 table)
  IT-2 Condotta (+E8)         reconcile the 4 real Mil read sites before the ×0.5 clause ships
  IT-1 Podestà                REFINE the appointer-liability rate/cost structure (not just strip the
                               already-flagged Fair Magistrate clause)
  HAB-4 Consulta (+E9)        author the Ministry action-economy foundation first

Phase 4 — Reconcile-gated (needs its Phase-0 decision landed as actual canon text, not just ruled)
  1.3a (D3 authored into settlement_layer_v30/governance_play_redesign_v1)
  1.0d MERGE (D5+D6 authored into the suspicion/recall spine — D6 determines HOW it advances)

Phase 5 — Author the remaining true structural gaps
  E5 wire L/PS               (also unblocks verifying VSG P11/P12's Ω-a claims)
  B11 author engine_clock    (unblocks Part 41's Relay Tier/Beacon Network — flag per §5 below)
  B9 geography YAML migration (unblocks canonical-population validation)

Phase 6 — Character & proactive-governance authoring (independently ready, per NERS review)
  Author the Ascendancy system (Part 40) into canon as PROPOSED text — the review's single strongest
    validated claim (92/100 downfall-exploitation); ready now, not blocked on anything in Phases 0–5
  Author Proactive Governance Menus (Part 41) for the Organization/Settlement/Faction scales as
    PROPOSED text now; HOLD BACK the Territory-scale Relay Tier/Beacon Network content explicitly
    until B11 (engine_clock) lands AND B12 (the Territory-naming collision, below) is resolved —
    this is the one item in this workplan meeting CLAUDE.md §1's "loud, not silent" exception bar

Phase 7 — VSG build proper (generation_sourcebook_v1 §7's sequence, now dated against Phases 0–6)
  P1–P4 sampler + Goldenfurt-reproduction fixture (blocked on Phase-0 B2)
  P5–P12 coupling groups (blocked on Phase-5 E5 for the L/PS-reading paradigms)
  P13–P14: reuse pr119_event_deck_engine.py's 13-card harness + npc_cast.md's collision map directly
    as calibration input, not re-derived from scratch
  P15 verify harness: adopt narrative_ners_review.md's inverted-critic-steelman-before-verdict
    discipline as P15's actual acceptance procedure, not a separate methodology
  Faction stack (F1–F8) / Territory stack (R1–R9): blocked on B1 (faction count) and — for the
    Territory stack specifically — on resolving B12's naming collision against Part 41 first
```

---

## §5 · Explicit asks for Jordan — updated 2026-07-13 post-ruling

**RULED** (ED-IN-0046, see `governance_consolidation_v1.md §6` for the full record): D1–D5, and the six
items governance_consolidation_v1 §2 already called a clean RATIFY (§1.0c, §2.5a mastership+entry,
§1.3c, §3.3b). Item 3 below (Phase-1 resequencing) is accepted as part of that same ruling — it was
this document's own recommendation and drew no objection.

**RULED, second pass (2026-07-13, ED-IN-0047, direct Jordan input in conversation, not inferred from
"ratify commit all"):**

1. **D6 RULED.** Cumulative per-Defy-season suspicion accrual is canonical (matches the suspicion/
   recall spine's own already-stated spec), **on the explicit condition that E11 lands in the same
   authoring pass** — a new, symmetric, ongoing suspicion-*reduction* mechanic driven by sustained
   compliance/consistency/predictability, not merely the existing one-shot `Submit to audit` escape.
   Jordan: "if there is a way to advance suspicion from non-compliance, there must be a way to reduce
   suspicion by over-compliance and consistency/predictability. Build the counter to cumulative." See
   `governance_consolidation_v1.md §3` E11 for the full ruling. **Unblocks** authoring D5's merge into
   `faction_politics_v30.md`, provided E11 ships with it.
2. **B1 RULED.** Starting faction count = **4** (Valorsmark, Hafenmark, Varfell, Church of Solmund) —
   independently confirmed against `valoria_political_hierarchy_v30.md`'s existing 3-duchy +
   Church-special-entity structure, not an arbitrary pick. Emergent factions are explicitly in scope
   and intentional: Restoration Movement (`insurgency_pipeline_v30`), Löwenritter-style post-coup
   splits (`faction_succession_split_v30`), and an Altonia-usurper archetype are named as valid
   emergence cases, reusing the F-stack's already-designed F6 mechanisms. **Resolves `ED-FA-0001`.**

**Context gathered, still awaiting Jordan's call — not resolved by inference:**

3. **B2.** Not really a design fork — an abandoned mechanical fix. `valoria_geography_v30.yaml` (the
   map source of truth) has no Goldenfurt at all and still says S-006=Lowenskyst Fortress,
   S-007=Lowenskyst Garrison Town. `settlement_layer_v30.md`'s own settlement table already flipped
   this (S-006=Goldenfurt/Kronmark, S-007=Lowenskyst Fortress) via a migration note at lines 488–489 —
   but the same file's line 912 still has a stale reference to the old numbering, and the geography
   YAML was never touched at all (Goldenfurt has zero coordinates/polygon/roads there). Lean: finish
   the already-started fix (line 912's stale ref + actually adding Goldenfurt to the geography YAML),
   since that's what `settlement_layer_v30.md`'s own primary table and all of `goldenfurt_slice/`
   already assume. Awaiting confirmation.

**A NEW finding, surfaces a real conflict with existing Class A canon — do not write anything for this
until Jordan resolves it:**

4. **B12, sharpened.** Jordan's ruling (2026-07-13, in conversation) describes a genuine hierarchy
   expansion: Settlement (people, local factions, local governance) → **Territory** (multiple
   settlements, its own levers/pressures) → **Province** (multiple territories, provincial-scale
   factions, provincial governance) → national (Parliament). This directly conflicts with
   `valoria_political_hierarchy_v30.md` (PP-726, **existing Class A canon**), which states explicitly:
   *"**Territory = Settlement** is the smallest political unit"* — i.e., current canon has NO
   intermediate tier between Settlement and Province at all; "Territory" is currently just a synonym
   for Settlement. Jordan's ruling also specifies that local/provincial/national-scale factions are
   independent tiers (not necessarily nested), that factions hold *people* rather than territory as
   their power base, and that settlements/territories/provinces can become independent of — or be
   claimed directly by — a faction from a different scale (e.g., a single settlement claimed by a
   national faction like the Restoration Movement without an intervening territory/province
   membership). This is real, substantial, well-specified new content — but it needs to land as a
   reconciliation against PP-726, not a silent overwrite. **Two readings offered to Jordan, awaiting
   his pick** (see the session's direct exchange): (a) insert a genuinely new Territory tier between
   Settlement and Province, reworking PP-726 §2.1–§2.5 around it; (b) some other mapping onto PP-726's
   existing Province/Territory=Settlement structure. **Nothing in `generation_sourcebook_v1.md`'s
   R-series or any settlement/territory doc should be edited for B12 until this lands.**
5. **The held-back item (Phase 6), unaffected by the D6/B1 ruling above.** Part 41's Territory-scale
   content (Relay Tier/Beacon Network) remains explicitly NOT bundled into "author Part 41 now" — it
   needs `engine_clock` authored first and B12 resolved. B12's newly-discovered PP-726 conflict makes
   this gate *stronger*, not weaker: Part 41's "Territory scale" may or may not be the same tier
   Jordan just described, and that can't be known until B12 lands.

---

**Status recap:** this document ratifies nothing, authors no canon, and allocates no new `ED-<LANE>-NNNN`
ids (new items above would take one on landing, per each Phase's own scope). It is a reconciliation and
sequencing layer over two already-merged PROPOSED bodies of work — read it alongside
`governance_consolidation_v1.md` and `generation_sourcebook_v1.md`, not in place of either.
