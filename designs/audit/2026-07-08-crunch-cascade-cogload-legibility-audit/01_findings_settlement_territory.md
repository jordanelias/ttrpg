# Settlement / Territory — Findings (adversarially verified)

**Canonical head:** `designs/territory/settlement_layer_v30.md` (+ adjacency/temperaments,
`geography_v30.md`), CANONICAL. `governance_play_redesign_v1.md` remains PROPOSAL.

**Currency correction:** the producer claimed the redesign is "gated on unbuilt
`sim/territory/registry.py`," citing the redesign doc's own §5.2 text. The critic pass **refuted**
this specific reason: `sim/territory/registry.py` **is built** (confirmed on disk; `CURRENT.md`
and `HANDOFF_SE.md`/ED-SE-0001 both say so) — the in-doc text is simply stale. The redesign is
still correctly un-firable and still PROPOSAL, but for a different reason: the Ledger-tag/
event-deck/NPC-ambition-tick prerequisites (§5.2 items 2–4) remain unbuilt, not the registry.
ED-SE-0005 (RESOLVED 2026-07-08) is confirmed to have only reconciled internal contradictions
*inside* the still-unratified redesign plus rewritten `player_agency_v30 §9` — it did not ratify
the redesign or touch the ratified §3.2 verb text beyond one annotation.

## 1. Tracker inventory

Prosperity/Defense/Order 0–5 (+ derived Local Economy/Garrison Strength/Public Order, all
"Player Sees"-labeled in the doc); Legitimacy/Popular Support 0–7 per settlement; Settlement
Weight 1–11; Facility Tier 0–3; Standing 0–5; Renown 0–10. **Population, Trade, Naval, Piety
Influence, and Garrison Capacity are named per-settlement-type stats that receive qualitative
"+1/season" effects but never get a numeric range, starting value, or cap anywhere in the
corpus** — the doc's own §1.8 flags Population as "left unscaled (§9 PENDING)."

Removed/merged by ED-SE-0005 (do not double-count as live): Administer (distilled into
Investigate + maintenance), Trade action (pruned into Guild contracts), Fund Development (merged
into Develop's Treasury method), free-no-downside Sponsor event (merged into a single
Debt-bearing Sponsor verb), Grant/Revoke Subnational Management (re-homed to FA's domain_actions,
ED-FA-0002 pending).

## 2. Interaction chain map

- **Governance verb (Develop/Fortify/Pacify/Administer) → province Accord → victory gate** — a
  4-hop chain with **no political tradeoff attached in ratified text**; the redesign's own problem
  statement calls the current loop "roll one die a season and watch numbers."
- **ED-SE-0002: two canonical docs give opposite answers on whether personal-scale Order changes
  stack with governor governance actions in the same settlement/season** —
  `scale_transitions_v30.md:214` ("do not stack — higher Accord wins") vs.
  `peninsular_strain_v30.md:196` ("stack normally, capped ±1/source/settlement/season"). Confirmed
  as a genuine live contradiction, open, needs_jordan.
- **Order 0 → revolt → unmanaged → −1/season** — clamped 0–5 (no numeric runaway) but **no
  automatic recovery procedure**: the settlement sits at Order 0 until a governor is re-assigned,
  with no maximum duration specified anywhere — a time-unbounded soft-lock, not a numeric one.
- **L/PS → Mandate** — the one loop in the lane with an explicit, sim-verified damper
  (30-season bounded convergence, cited in `module_contracts.yaml`).
- **Adjacency (49-edge graph) confirmed NOT connected to the stat cascade** — it governs
  movement/battle terrain only; Order/Prosperity/Defense do not propagate settlement-to-settlement,
  and nothing in the corpus disclaims a future contagion mechanic being wired in without a
  dampening rule already present.
- **Local Actors carry one Conviction and no ambition/goal field** — "what does each actor want"
  is unanswerable at the governor tier; confirmed still true post ED-SE-0004/0005 (neither touched
  the ratified §4.5 Local Actor schema).

## 3. Cascade check

1. Order-0 soft-lock: no numeric runaway, unbounded in time (confirmed).
2. §4.7/4.8's Black Market/Intelligence Broker mechanics reference a "settlement Accord" and
   "settlement Wealth" that **do not exist as tracked stats at settlement grain** (§1.3 only
   tracks Prosperity/Defense/Order; Accord is province-level; Wealth/Trade have no defined scale)
   — confirmed a genuine cross-section inconsistency, not cosmetic.
3. ED-SE-0002 stacking contradiction (above) — confirmed live.
4. **Domain Echo season-aggregate ceiling — corrected from "open" to resolved-as-deferred.** The
   critic pass found **ED-IN-0025 is `status: resolved`** (2026-07-07), deferred to a Stratum-B/E
   balance review — the design gap itself (no season-level cap on stacked Echoes) persists, but
   the tracking item is closed, not open.
5. Adjacency: confirmed no cascade exists.

## 4. Cognitive load

Ratified baseline: 1 decision (pick 1 of 4 verbs) + 4–6 tracked values per settlement. A
multi-settlement governor (up to 3, Standing 4+) faces 12–18 items with **no aggregation/
dashboard layer specified** — the only rollups that exist (province Accord, faction Mandate)
destroy per-settlement resolution rather than summarizing it (you cannot tell which of your 3
settlements is about to hit Order 0 from the Accord number alone). If the PROPOSAL ratifies, load
jumps substantially (Directive response + AP allocation across 8 verbs × 2–3 methods + Ledger-tag
bookkeeping + NPC ambition state per NPC) — the redesign itself half-acknowledges this as an open
balance question. Beyond 3 settlements, load scales with total-controlled-settlement count (up to
37 per registry) with no summary UI, only reactive Scene Slate surfacing after the fact.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — ED-SE-0002 stacking contradiction** — confirmed, open, needs_jordan.
- **P1 — Named-but-unscaled trackers** (Population/Trade/Naval/Piety Influence/Garrison Capacity).
- **P1 — §4.7/4.8 reference non-existent "settlement Wealth"/"settlement Accord."**
- **P2 — No player-facing UI model exists** (contrast `peninsular_strain §2.8`, which does have
  a province-scale legibility spec).
- **P2 — No ambition/goal field for Local Actors in ratified canon.**
- **P2 (corrected status) — Domain Echo season-aggregate ceiling gap persists, but the tracking
  item (ED-IN-0025) is resolved-as-deferred, not open** — don't re-file it as a fresh open item.
- **P2 (corrected — stale) — The "Treat chit call-in trigger unspecified" finding was already
  discharged by ED-SE-0005**, which specified the trigger (Debt tag → Friction card). Listing it
  as a live open gap is out of date.
- **P2 (corrected — overstated) — the writable-vs-derived schema distinction is not purely a
  schema-only fact hidden from prose.** `settlement_layer_v30.md §1.3`'s own "Derived Value" table
  column already communicates the writable/derived split in prose; only the explicit
  `writable:true/false` YAML flag terminology is schema-only.
- **P3 — Jargon without translation** (FacilityTier, Weight, T, the Mandate saturating formula —
  no "Player Sees" row unlike the base-stat rows).
- **P3 — `territory_temperaments_v30.md`** operates at province grain only; settlement-level
  deferred to "Stage 6b"; doc's own Stage-6 content is self-labeled PROVISIONAL despite a
  CANONICAL header line — an internal inconsistency worth its own note.

## New findings from adversarial pass

1. **Latent province-Accord cap inconsistency, missed by the producer:** `settlement_layer_v30.md
   §1.3:61` and `module_contracts.yaml:583` both give an **uncapped** `floor(mean settlement
   Order)` for province Accord, while `peninsular_strain_v30.md:196` (and its §2.3 Govern rule)
   **caps Accord at 3**. The producer asserted "capped 3" citing the uncapped sources — a genuine
   cross-doc drift worth its own gap entry, plausibly a sibling to ED-SE-0002.
2. The redesign's registry-gating reason should be corrected in any future work: not "unbuilt
   registry" but "unbuilt Ledger tags / event deck / NPC ambition tick."
