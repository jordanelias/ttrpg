# The Reconciliation Program — engine↔prose iteration as the design workflow

## Status: PROPOSED — HELD FOR JORDAN. One program consolidating every open plan-fragment from the 2026-07-21 observatory sessions. On acceptance it AMENDS the merged observatory proposal's §7 phasing (2026-07-21-observatory-holonic-refactor.md) — flip both docs' Status lines in the accepting merge (ED-1094), nothing auto-ratifies before that.

**Date:** 2026-07-21
**Lane:** IN (cross-cutting observatory / vocabulary / dashboard)
**Class:** design (program plan) — no game-canon change; implementation phases allocate `ED-IN-*` at execution per `references/id_reservations.yaml`
**Consolidates (and supersedes as separate work items):** the "Phase 0 capability registry" sketch, the canonical-identifier convention sketch, the flow-workbench sketch, the A8/P2 decision packet, and the observatory-amendment note — previously five floating fragments; this doc is now their single home.

---

## 0. North star (Jordan, 2026-07-21)

> *"I am literally looking to adjust the prose-based design work based upon what the code/engine is surfacing so that I can better curate, articulate and orchestrate all the primitives/actions/effects that flow through the game."*

With the governing correction: **engine and prose are complementary and iterative.** The engine is faithful to what *runs*; the prose to what's *intended*; the design process is the loop that reconciles them — in **both** directions. Divergences are iteration points, never auto-resolutions; the direction of each reconciliation (fix the prose, or fix the engine) is always the human's call. The prose was largely authored **per-silo**; the engine is where the systems actually interoperate — so the engine's wiring is the best available *map of real integration*, and the tool's job is to hold both views side by side and make every gap between them a workable card.

## 1. The unified divergence model (one model, two axes)

Replaces the overlapping "three-home" and "quadrant" framings with a single model.

**Node axis — where an entity lives** (assigned by actual presence, resolved via `quantity_registry`/`names_index`/the definitions store):
- `prose` — appears in ≥1 design doc
- `engine-live` — in contracts/sim with a real resolver/implementation
- `engine-notional` — in contracts but `doc:null` / `[ASSUMPTION]`-grade / stubbed (§6-§7 caveats)
- `unbuilt` — in neither (e.g. the action verbs pending `domain_actions`, ED-FA-0002)

**Edge axis — how each engine relationship is articulated in prose.** For every engine edge (emit→consume Key, derivation input→output):
- `articulated` — prose names both endpoints **and** the relationship
- `mentioned` — endpoints appear in prose; the relationship is never stated (the Mode B fingerprint: Clocks↔Victory)
- `silent` — one or both endpoints absent from prose

**Divergence classes → iteration cards** (each card carries evidence, confidence, and the *both-directions* resolution set):
| Class | Signature | Card question |
|---|---|---|
| **Unspecced wiring** | engine-live edge, prose `mentioned`/`silent` | "The engine wires this — articulate it, or should the engine not do this?" |
| **Unrealized intent** | prose claim with no engine edge | "The design intends this — build it, or revise the intent?" |
| **Notional shadow** | engine-notional edge, any prose state | down-ranked: "this contract row is itself unratified — confirm before reconciling *to* it" (guards the ED-MB-0010 fabricated-emit class from masquerading as reality) |
| **Vestigial** | `unbuilt` node, no prose beyond a name | "author / delete / defer" (the Augur triage, unchanged) |

**Anti-Goodhart rule:** per-doc "responsiveness" (share of touching edges articulated) is a **curation lens and a report-only trend, never a gate** — the moment it gates, authors will pad prose with mechanical restatements to satisfy it.

## 2. The product — the Loom (reconciliation workbench)

Not a fourth holon: the Loom is the **composition** of Atlas (the two-sided view) + Augur (cards with memory) over the observatory substrate, with the §1 divergence detector added to the substrate. Named for what it does: warp (engine wiring) and weft (prose intent), crossed.

- **Two-sided entity/edge view:** for any primitive/action/effect/module — the engine's real chain (`action → Key → module → primitive → cascade`, from contracts/ripple, provenance-tagged live/notional) beside the prose's claims about it, with every §1 divergence flagged in place.
- **Cards with memory (mandatory, day one):** stable card IDs (hash of class+endpoints+evidence shape); human answers in `references/observatory_dispositions.yaml` (shared with Augur — one dispositions file, not two); only new/changed cards surface; **resolved-tracking** so a doc revision visibly closes its card on the next run; the open-card count is a report-only trend.
- **Engine-fact sidecars:** a deterministic generator emits, per subsystem, a committed generated file (`systems/<sub>/ENGINE_FACTS.md`, banner-marked GENERATED, refreshed by the audit-refresh workflow like DECISIONS.md) stating exactly what the engine currently wires for that system — so the engine's reality is *in the author's editing context*, not only on a dashboard.
- **No migration dependency:** the Loom matches prose via today's display-name + disambiguation-context patterns (confidence-tagged). The §3 ID migration is a *precision upgrade* it benefits from, never a prerequisite.
- **Order, later:** topology now; cascade *order* (the orchestration view) requires the clock/resolution spine — explicitly phased after the ED-1051 engine_clock ruling, which the Loom's own biggest divergence cluster will evidence.
- Deterministic and model-free, like the rest of the observatory.

**Prototype (Phase R1, the program's first deliverable):** two vignettes, chosen adversarially —
1. **`settlement_layer`** (doc + 1 emit / 2 consumes / 7 derivations — both sides rich): the full two-sided view with real edge-level divergences.
2. **`Muster`** (prose/seed-only; `domain_actions` is `doc:null` notional): the one-sided card — *unrealized intent* meeting *notional shadow* — demonstrating both the empty-side rendering and the live/notional guard.

## 3. The vocabulary enabler — canonical identifiers (forks resolved)

Three-layer representation per term, mapped solely in `names_index.yaml`:
**id** (namespaced, collision-free) · **display** (what humans/players see) · **match-patterns** (display + disambiguation context, for prose scanning). ID-form tokens are excluded from prose matching (A6/perf consistency).

Resolved forks:
1. **Tag syntax: ID-only `[[conv.faith]]`** — verified collision-free (no `[[` in current prose). The renderer resolves display from `names_index` (change-once preserved — embedding `|Faith` in every tag would denormalize the display into thousands of sites, the exact drift `valoria_rename` exists to prevent). Inflection via adjacent text (`[[conv.faith]]'s`); `|override` escape only for irregulars. Mechanical/structured contexts first (param tables, contract fields, headers); flowing prose opportunistic, per-edit, never big-bang.
2. **Namespace scheme: short dotted prefixes extending the existing habit** (`attr.` `fac.` `set.` stay; existing Key families `scene.` `da.` `mechanical.` stay untouched). New prefixes only for classes lacking them — `conv.` `ppt.` `npc.` `place.` `org.` `ppl.` `concept.` `act.` — authored as a prefix↔silo table in the `names_index` header, with `name_collision_database.yaml` remaining the ratified silo authority. Engine/existing IDs win any conflict.
3. **Enforcement: report-only → `warn` on mechanical contexts only; never `block`.** Same earned-gate discipline as the observatory (Tier-3 admission before any escalation).
4. **Registry topology: no new registry.** `names_index.yaml` is the operational map (grows ~90 → ~250 entries, seeded engine-first); the collision DB stays the historical silo authority. Free synergy: `derive_tokens` already reads `names_index`, so this extension *is* the token-universe extension — one edit, two systems.
5. **Directionality: dissolved.** Conflicts are iteration cards (§1); the human picks the direction per card.

**Precondition to any tag entering the corpus:** one shared **tag-normalizer** utility (single owner, `obs_core` pattern) that every prose-consuming tool (vector audit, co-file checker, naming lints, size caps, the eventual gameplay text renderer) calls to strip/resolve tags — priced in *before* migration, not discovered after.

## 4. The findability enabler — the Repo Atlas (dashboard collation)

Answers: *"integrate every review/audit/check/tool/skill; I don't know what's where or what's called what."*

- **One panel, two tabs, grouped by JOB not kind:**
  - **Capabilities** — extend `build_apparatus_registry.py` (already inventories 99 tools/hooks/workflows/scripts) to fold in the 13 skills (from `SKILL.md` descriptions), the CI checks (`ci_checks_registry.yaml`), and audit types; each entry a routing card — *what it's for / how to invoke / where output lands / when to use* — seeded from CLAUDE.md §9's routing table. Orphans shown as orphans.
  - **Work products** — the artifact index: audits (`audit_registry`), proposals (`build_proposals`), decisions/needs-Jordan (`build_needs_decision` + Loom cards, presented together in one "Decide" super-panel with their kinds distinguished), registers, handoffs.
- **One canonical viewer:** the GitHub-Pages dashboard. The offline `tools/observability/console.html` is relabeled the *dev-local twin* (link + banner), so "two dashboards" stops being its own findability bug.
- Published via `obs_core`'s `window.VALORIA_*` writer; refreshed by the existing workflows; no new viewer, no new registry file.

## 5. The A8 → P2 decision packet (embedded; awaiting ruling)

Re-derivation of conviction symmetry, three measures + per-conviction noise:

| conviction | raw paras | context-gated | noise | cite-degree |
|---|---|---|---|---|
| Faith | 90 | 61 | 32% | 108 |
| Order | 192 | 71 | **63%** | 172 |
| Reason | 36 | 34 | 6% | 114 |
| Equity | 42 | 23 | 45% | 123 |
| Precedent | 61 | 32 | 48% | 138 |
| Autonomy | 65 | 50 | 23% | 124 |
| Continuity | 35 | 26 | 26% | 110 |

CV: cite-degree **0.163** (flattered by neighbor-set saturation) · context-gated **0.403** (marginal pass; note the gate's own co-mention bias — context words are largely *other conviction names*, so roster-adjacent paragraphs inflate it) · raw **0.689** (noise, not asymmetry — `Order` is 63% non-conviction usage).

**Recommendation:** flip P2 FAILED→VALIDATED **on the context-gated presence measure** (not cite-degree), fix the `mean==0 → cv=999` sentinel to report *not-measurable*, and ship the per-conviction spread with the verdict: the pass is **thin**, and "Equity/Continuity/Reason (23–34) are ~2-3× thinner than Faith/Order/Autonomy (50–71)" is a real, mild curation signal — a natural early Loom worklist, not a rubber-stamp. The 0.5 bar is pre-committed and kept; measure-sensitivity is disclosed rather than hidden behind one number.

**RULED — 2026-07-21, Jordan, in-session: Option A. Implemented in this same PR as ED-IN-0080** (methodology v3→v4: `validate()` P2 measure + NOT-MEASURABLE sentinel; `methodology.md` §3.8 amendment; SKILL.md note; regression tests). This item is therefore **no longer held back** — the merge ratifies a decided change.

**Attributes extension (same ruling):** the attribute class (9 today; roster IN FLUX, possibly 10) becomes a **second symmetry probe on the same measure and bar** once two preconditions clear: (1) the descriptor-registry roster stabilizes, and (2) the attributes gain disambiguation contexts — `Will`/`Focus`/`Order`-class common words make ungated counts noise (the session's raw attribute CV 0.46 was borderline *with* that contamination; Charisma/Will-heavy, Body-group underweight). Staged, not implemented; lands with the vocabulary work (§3).

## 6. Phasing (product-first; each phase independently valuable)

| Phase | Deliverable | Depends on |
|---|---|---|
| **R1** | **Loom prototype** — settlement_layer + Muster vignettes, edge-level cards, dispositions, sidecar for one subsystem | existing graphs only |
| **R2** | Vocabulary seed (engine-first `names_index` extension + prefix table) + **tag-normalizer**; token universe upgrades free | — (parallel to R1) |
| **R3** | Repo Atlas panel (capabilities + work products; viewer resolution) | existing registries |
| **R4** | Loom full: all subsystems, sidecars, trend, audit-refresh + staleness-slot + dashboard wiring per observatory r2 §4-5 | R1 |
| **R5** | Migration waves (mechanical contexts via `valoria_rename` ID-mode; report-only lint → warn) | R2 |
| **R6** | Orchestration/order view | ED-1051 ruling |

Observatory r2's §7 phasing is amended accordingly: its "Phase 0 coverage map" is subsumed by R1+R3 (node-axis coverage ships inside the Loom and the Atlas); its Phases 1–3 (direction reconciliation, measured bridge, Assay-as-review_core-signals) proceed unchanged as substrate work under R1/R4.

## 7. Governance & discipline (carried forward, unchanged)

Observe→human→act, never observe→act→observe. Cards and lenses are report-only; gates only via the Tier-3 admission test. Scheduled refreshes ride `audit-refresh.yml`'s branch-PR pattern; staleness via the ED-IN-0032 slot; scheduled runs never append `audit_registry`; the pipeline stays deterministic and model-free. **Held for Jordan:** ~~the §5 P2 flip~~ (**RULED A 2026-07-21, implemented — ED-IN-0080**); any lens→gate promotion; the observatory-r2 §8 items (unchanged); acceptance of this program's phasing amendment. **Parked, explicitly not lost:** the four-bloc win-probability gate (sim/balance harness — §7's unmonitored ~87% degenerate win-share); `build_graph`↔substrate unification; key-level G_code descent.

## Appendix — adversarial findings this rewrite resolves

(1) plan proliferation → one program doc; (2) plumbing-before-product → Loom is R1; (3) open forks → resolved §3; (4) entity-level too coarse → edge axis; (5) "engine=reality" overstated → live/notional split + notional-shadow guard; (6) two overlapping models → §1 unification; (7) `[[id|display]]` change-once violation → ID-only tags; (8) stateless workbench → cards with memory + shared dispositions; (9) empty-sided prototype → settlement_layer + Muster; (10) migration starving the Loom → decoupled, precision-upgrade-only; (11) work-products + two-viewers gap → §4; (12) unpriced tag blast-radius → normalizer precondition; (13) unstated token-universe synergy → §3.4; (14) A8 co-mention bias → disclosed in §5; (15) orchestration-needs-order → R6 tied to ED-1051.
