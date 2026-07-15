# Governance / Cross-Scale Proposal Cluster — Unified Reconciliation (v1)

## Status: PROPOSED — 2026-07-15 · Lane: IN (cross-cutting; SE, FA, WR) · ED-IN-0070 · Jordan-vetoable throughout

> **What this is.** The single reconciled record over the governance-play proposal cluster that had
> accumulated as ~7 overlapping PROPOSED docs across 2026-07-11 → 07-14. It **organizes** them under one
> index head and points to the deep sources; it does **not** author new mechanical canon and it deletes
> nothing. Merging this doc ratifies the *organization* (which doc is the index, which are the kept deep
> sources, the one recency supersession in §3) per CLAUDE.md §2 / ED-1094 — but **every design fork in §4 is
> HELD-BACK and remains `needs_jordan`** (this banner is the loud exception the convention requires).
> Full conflict analysis + provenance: `01_reconciliation_map.md` (ED-IN-0069).

---

## §1 · Scope — governance-PLAY only (one of two axes)

The awaiting-ratification scan surfaced 13 governance/cross-scale docs. They fall on **two axes that must not
be merged**:
- **Governance-play design** (this doc) — the mechanics of governing: governance *types*, action verbs,
  directives, institutions, long-fuse stats, L/PS wiring, event decks.
- **Observatory / tooling remediation** — the vector-audit scripts, pointer-debt, module grounding. **Already
  anchored by ED-IN-0064/0065/0066** (`remediation_plan_v1.md` + `2026-07-14-holistic-unification/`), with its
  own D1–D16 held docket. **Not in scope here** — pointer only.

---

## §2 · The unified governance-play surface

**Ratified decision-surface (route through this first) — `designs/architecture/governance_consolidation_v1.md`
(RATIFIED 2026-07-13, ED-IN-0046/0047).** Not in the awaiting-ratification set (it's ratified), but it is the
companion the compendium's own `00_index.md` names as "what to decide": it rules D1–D6 (incl. Compact, §3) and
holds the 12-item PR#119 disposition table. Any authoring off this cluster must check it first or it re-opens
settled ground.

**Structural / taxonomic index head — `designs/architecture/governance_type_registry_v1.md` (2026-07-13).** The FLAG/VECTOR taxonomy
(discrete policy choice vs continuous accumulating quantity; the dominant real shape is
*VECTOR-with-derived-FLAGS*) and a deduplicated registry of every governance type across the ratified
Settlement→Territory→Province→Duchy→Country hierarchy (`scale_hierarchy_v1.md`). It is explicitly an index that
"claims no new mechanical canon by itself" — so it organizes without overwriting the deeper work beneath it.

**Deep-content sources (kept — the index points to them, they are not superseded):**

| Source | Owns |
|---|---|
| `designs/architecture/governance_ripple_substrate_v1.md` (07-11, 559L) | The propagation / accumulation / dissipation ("ripple") model; the Treasury vector (§7) |
| `designs/audit/2026-07-12-governance-compendium/` (42/43/44/45 + `event_cards/00_integration_map` + `00_index`) | 109-verb action catalogue (42); directive types (43); standing institutions (44); hidden long-fuse stats (45); event-card integration — a **research menu**, not yet authored into canon heads |
| `designs/audit/2026-07-11-grounded-event-card-deck/grounded_event_card_deck_v1.md` (07-11) | The grounded 13-card event-deck **engine** — complementary to the compendium's integration *map* (deck vs map, not rivals) |

**Buildable SE head — `designs/territory/lps_wiring_v1.md` (2026-07-14).** The concrete build of the registry's
"consent/resistance VECTOR" (Legitimacy / Popular Support). Most recent and executable; the registry's L/PS row
points here. (Its own SE-lane ratification is a separate call — this doc only places it in the structure.)

---

## §3 · The one recency supersession (a point, not a doc)

**Compact is a Debt subtype, not a 5th ledger family.** The 07-12 compendium (and ED-SE-0018/0019) framed
"Compact" as a new tag-family; the built code (`sim/territory/ledger.py:30`) has `{Precedent, Grudge, Debt,
Reputation, Leverage}`; and **ED-IN-0046 D3 (RATIFIED 2026-07-13)** ruled Compact = a recurring **Debt subtype**.
By recency (a later ratified ruling), D3 governs: **Leverage is the built 5th family; Compact is a Debt subtype
(`Debt(key="compact:<quota>", ttl=term, recurs=True)`); no conflict.** `reeval_jp_se.md` is retained as the
provenance of this catch. **Residual (non-fork, broader than the cluster):** the pre-D3 "5th ledger family"
framing survives in deck C.3, compendium 44/45, **and the current head `governance_play_redesign_v1.md`
§1.3a/§1.6** (Encabezamiento). Propagating D3's Debt-subtype model there executes a ratified ruling — recommend
it run as ED-IN-0046 D3's own SE/IN follow-up, not this PR (it re-models a mechanic in a current head).

---

## §4 · HELD-BACK — the design forks (needs_jordan; nothing below is decided by merging this doc)

1. **`type_registry §4` — add a `Field/Gauge` substrate primitive alongside `Key`?** The cluster's one genuinely-new
   canon proposal: because governance state is mostly VECTOR-with-derived-FLAGS, §4 argues one primitive can't
   serve both halves — a Key for the FLAG moment, a Field/Gauge for the VECTOR body (`key_echo_armature_v1 §1`).
   High-leverage, cross-cutting. **Top decision.**
2. **Tag-family taxonomy** — ratify or collapse the remaining proposed families (Concession, Outlawed,
   Capital-Posture, Muster). Compact is already settled → Debt subtype (§3); the compendium (44 §268) itself flags
   the rest as likely over-proliferated.
3. **Governance-verb selection** — which of the 109-verb catalogue (42) are authored into the canon head over the
   current **8** (`governance_play_redesign §1.3`: Develop/Fortify/Keep Order/Hold Court/Sponsor/Treat/Levy/Investigate).
4. **Directives (43) & standing institutions (44)** — author into `faction_politics_v30` / `governance_play_redesign`,
   or shelve. (Neither is authored today; Part 44's tracked-stat institutions are blocked on #5 first.)
5. **`45_hidden_longfuse_stats` — granularity ruling.** Its own framework recommends track RisingWaterLevel /
   conditionally track SiltLevel / abstract the other six; **StockLevel is blocked on a prior binary: adopt
   Ever-Normal Granary as a mechanic at all, yes/no.**
6. **`governance_ripple_substrate` open rulings R-1 / R-2 / R-4** — settlement-lever scope; NPC contesting a
   player-held seat; the Π 7→8 event-deck band-cliff (hard threshold vs softened band). (R-3 answered by
   `scale_hierarchy_v1`/B12; residual = one sentence on whether the new Territory tier behaves as ripple
   "connective tissue.")
7. **ED-SE-0045 (Treasury ×10 vs ×50)** — already filed; noted because both `ripple_substrate §7` and
   `type_registry §2.4` silently inherit `×10` (surfaced by `lps_wiring §3.1`). Cross-reference, not a new fork.

**Cross-lane coordination:** `franchise_v30.md` (FA, Nature C) proposes a per-territory political-weight stat that
overlaps this cluster's L/PS + scale-hierarchy — reconcile it *against* §2 before ratifying (recency/depth favors
re-expressing Franchise as a derived view over L/PS, not a parallel new stat). See `03_natureC_dispositions.md`.

---

## §5 · What merging this doc does and does not do

- **Does (ratify-on-merge, ED-1094):** establishes `governance_type_registry_v1` as the governance-play **index
  head** over the kept deep sources named in §2; records the §3 Compact recency supersession; separates the
  observatory/tooling axis out (§1).
- **Does NOT:** decide any §4 fork; author any compendium content into a canon head; supersede any deep source;
  ratify `lps_wiring` or `franchise` on their own merits; touch the B-obs (ED-IN-0064/65/66) docket.

On merge, the register step flips this doc's `## Status:` and the ED-IN-0070 ledger entry per the standard gate,
and adds the index-head pointer to `CURRENT.md`'s governance/faction row. The §4 forks stay `needs_jordan` until
explicitly picked.
