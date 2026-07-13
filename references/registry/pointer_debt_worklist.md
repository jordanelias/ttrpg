# Pointer-debt work-list — the path from G_pointer 45.8% → higher (WS1)

## Status: PROPOSED (analysis; ED-IN-0059)

`G_pointer` (the observatory's `skills/valoria-vector-audit/scripts/pointer_audit.py`) measures
what fraction of the quantity identifiers in `references/module_contracts.yaml` + `sim/` resolve to
a central registry key. Today: **27/59 unique identifiers (45.8%)**, 35/71 occurrences (49.3%). The
reader (`tools/registry.py`) being complete does **not** move this number — an empirical check
(2026-07-13) confirmed **0 of the 32 unresolved identifiers resolve through the unified reader that
don't already resolve through `quantity_registry` alone**. They are genuinely *unregistered*, not
mis-routed. The meter moves only by **registering** them — which is a design act, so this document
is the evidenced, categorized work-list, not a unilateral edit.

Every mapping in Category A below is backed by the module's OWN `module_contracts.yaml` `state`
prose or a descriptor entry — cited inline. Nothing here fabricates a quantity (CLAUDE.md §5).

---

## Category A — abbreviation/alias of an ALREADY-registered quantity (SAFE alias-add, evidence-cited)

These are the low-risk, no-new-design wins: the quantity already exists in
`references/descriptor_registry.yaml`; the identifier is just an abbreviated / scale-suffixed / prose
form the resolver doesn't yet recognize. Fix = add the form as an `aliases:` entry on the existing
key. **Caveat (why this is a careful follow-up, not done here):** `descriptor_registry.yaml` is
CI-mirrored to `names_index.yaml` by `tools/ci_names_consistency.py` and self-declared IN FLUX, so
each alias-add must be verified green against that mirror gate before landing.

| Unresolved identifier | Existing key | Evidence |
|---|---|---|
| `settlement L`, `L_s` | `set.legitimacy` | settlement_layer contract state: "Legitimacy (**L**)" |
| `PS`, `PS_s`, `PS (Mandate feedback)` | `set.popular_support` | settlement_layer contract state: "Popular Support (**PS**)" |
| `settlement Order` | `set.order` | settlement_layer contract state: "Prosperity / Defense / **Order**" + `set.order` exists |
| `settlement Prosperity` | `set.prosperity` | same contract line + `set.prosperity` exists |

The abbreviation forms carry prose annotations (`PS (Mandate feedback)`, `L_s`) that A17's
normalization may not strip even with the alias present — so after adding aliases, re-run
`G_pointer` and confirm each actually resolves; a few may need the annotation cleaned in the
contract instead (a `module_contracts.yaml` edit, not a registry edit).

---

## Category B — genuine UNREGISTERED scalar (needs a canonical-key decision, verify vs the design doc)

Real quantities with no registry entry anywhere. Each needs (1) a canonical key in the right
`descriptor_registry.yaml` section, and (2) verification against the cited home doc before
registering (§5 anti-fabrication). These are the decisions that actually close the bulk of the debt.

| Identifier | Home module (doc) | Note |
|---|---|---|
| `Wounds`, `Initiative`, `Poise`, `cumulative_damage` | personal_combat (`designs/scene/combat_engine_v1/`) | combat-scale scalars; combat is an active R3 lane — coordinate |
| `Turmoil` | peninsular_strain / victory | appears in 2 modules; a known peninsular mechanic |
| `Accord`, `province Accord`, `PV`, `PT reads` | victory / settlement_layer | victory-condition quantities; `PT` = Piety Track (already a track), `PV`/`Accord` need keys |
| `CV (per-territory Piety)` | territorial_piety | per-territory piety value |
| `knot strain` | fieldwork_knots | thread/fieldwork scalar |
| `conviction scars` | piety_track | |
| `season counter` | engine_clock | the temporal spine — `engine_clock` is itself `doc:null` (author canon first) |
| `faction Mandate`, `faction Treasury income`, `faction political pool`, `faction stats 1-7`, `W_s`, `card hands`, `cooldown` | faction_state / settlement_layer / ci_political | mixed: some (`faction Mandate`) are cross-module pointers already annotated "→ faction_state"; `faction stats 1-7` is a description, not a name; `card hands`/`cooldown` verge on Category C |

---

## Category C — composite / structured STATE, not a scalar registry quantity (OUT OF SCOPE)

These are structured state objects, not scalar quantities the descriptor registry keys. They should
NOT be forced into the quantity registry; flagging them as "unresolved" is arguably a scope mismatch
in what `G_pointer` counts, not real debt. Candidate: exclude them from the pointer-debt denominator
(a `pointer_audit.py` scope refinement) rather than register them.

- npc_behavior: `arc state`, `beliefs`, `concerns`, `opinions`, `projects` — an NPC's relational /
  psychological state graph, not a scalar.

---

## Suggested sequence (each its own careful, gated checkpoint)

1. **Category A alias-adds** (lowest risk, no design call) → re-run `G_pointer`, confirm it climbs;
   verify `ci_names_consistency` green. This is the first real meter movement.
2. **Category C scope refinement** — decide whether composite state counts as pointer-debt; if not,
   refine `pointer_audit.py`'s denominator (with a disclosed, logged exclusion — never a silent cap).
3. **Category B registrations** — one module's quantities per checkpoint, each verified against its
   home design doc and ratified; defer combat's until its R3 lane settles (scheduling rule R7).

Owner note: Categories B/C carry design/scope decisions surfaced for Jordan; Category A is
mechanical-but-gated and can proceed on the cited evidence.
