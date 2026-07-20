# 03 — Nature-C: loose provisional canon heads (disposition)

## Status: REFERENCE (recommendations only; every item is needs_jordan — no status flipped by this file)

Three standalone canon heads read PROVISIONAL/DRAFT. Unlike Nature A they are **not** subordinate to a
ratified capstone, and unlike Nature B they don't conflict with each other — each is an independent
ratify/hold call for Jordan. Per the approved plan, **no status line is flipped here**; these are
recommendations. Each carries `needs_jordan: true`.

---

### C-1 · `designs/npcs/character_canon_v30.md` — PROVISIONAL (2026-05-07, 439L) · lane PC/NPC

**What it is.** A *consolidation* head that references (does not duplicate) already-ratified substrate —
PP-684 (13-Conviction), PP-685 (migration roster), PP-681 (Piety Track), PP-688 (Articulation), plus
`npc_behavior_v30 §§1–12`, roster, analyses, histories. PART A (Framework) is complete; PART B (per-NPC
sheets) is explicitly "pending Q1 scope decision."

**Recommendation — SPLIT.**
- **PART A → RATIFY** (needs_jordan). It creates no new mechanical canon; it indexes ratified PPs into one
  lookup surface. Low risk. On ratify, flip the doc banner + `## Status:` and add to `CURRENT.md` as the
  character-canon consolidation head.
- **PART B → HOLD.** Gated on the Q1 scope decision (how many/which NPC sheets to author) — a genuine
  authoring-scope call only Jordan makes.
- **Blocking?** No. Part A can ratify independently; keep Part B's PROVISIONAL marker until the scope call.

---

### C-2 · `designs/provincial/franchise_v30.md` — DRAFT (2026-05-04, 205L) · lane FA

**What it is.** A **new mechanic**: a per-territory `Franchise` (0–5) stat giving each territory's
delegation distinct parliamentary weight, aggregating to national influence, with caste-system territorial
expression. Genuinely new design (new stat; touches geography, faction_behavior, parliament, settlement,
faction_politics + several Godot libraries).

**Recommendation — HOLD, with a mandatory cross-check first (needs_jordan).** This is a real design call,
not bookkeeping. **Before it is ratified it must be reconciled against the Nature-B governance cluster** —
specifically `territory/lps_wiring_v1.md` (Legitimacy/Popular-Support per settlement) and
`territory/scale_hierarchy_v1.md` (the new Settlement→Territory→Province tiering, ED-IN-0047 B12): "per-
territory political weight" strongly overlaps L/PS and the territory tier, and the newer (2026-07)
governance work may already subsume or contradict Franchise's 2026-05 model. **Recency-vs-depth reading:**
Franchise is older (05-04) and moderately deep; the governance cluster is newer and deeper on the same
ground → default is that the governance work is the head, and Franchise should be re-expressed as a *derived
view* over L/PS + territory tier rather than a parallel new stat, unless Jordan wants it as-is. Flagged in
`01_reconciliation_map.md §Held-back` as a cross-lane (FA↔SE) reconciliation, not a clean ratify.

---

### C-3 · `designs/world/solmund_master_document.md` — DRAFT (584L) · lane WR/world

**What it is.** A cultural/worldbuilding guide — voice registers, artifact taxonomy, philosophical
frameworks, Solmund's nature, faction-engagement pathways — grounded in real source traditions. **Lore, not
mechanics** (the one "mechanical audit" section aside). Explicitly "pending Jordan editorial approval."

**Recommendation — HOLD for Jordan editorial review (needs_jordan).** Low mechanical risk; no conflict with
any other proposal. This is a pure editorial/voice call — exactly the setting/lore-authorship judgment the
model-tiering table reserves for Jordan. It can likely ratify wholesale once Jordan approves the voice;
no reconciliation work is needed, just a read. (Naming gate note: confirmed it uses **Solmund**, not the
deprecated Galbados — CI-clean.)

---

## Summary

| Doc | Lane | Call | needs_jordan |
|---|---|---|---|
| `character_canon_v30.md` PART A | PC | ratify (consolidation of ratified PPs) | yes |
| `character_canon_v30.md` PART B | PC | hold (Q1 scope decision) | yes |
| `franchise_v30.md` | FA | hold — reconcile vs L/PS + scale-hierarchy first (recency/depth → governance is head) | yes |
| `solmund_master_document.md` | WR | hold — editorial read only, likely ratify-as-is | yes |
