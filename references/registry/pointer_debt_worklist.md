# Pointer-debt work-list — the path from G_pointer 45.8% → higher (WS1)

## Status: PROPOSED (analysis; ED-IN-0059)

`G_pointer` (the observatory's `skills/valoria-vector-audit/scripts/pointer_audit.py`) measures
what fraction of the quantity identifiers in `references/module_contracts.yaml` + `sim/` resolve to
a central registry key. Baseline at time of writing (2026-07-13): **27/59 unique (45.8%)**, 35/71
occurrences (49.3%). **After Category A (ED-IN-0060, executed via contract canonicalization): 29/55
unique (52.7%) raw / 53.7% refined once formula-locals are excluded (ED-IN-0061).** The
reader (`tools/registry.py`) being complete does **not** move this number — an empirical check
(2026-07-13) confirmed **0 of the 32 unresolved identifiers resolve through the unified reader that
don't already resolve through `quantity_registry` alone**. They are genuinely *unregistered*, not
mis-routed. The meter moves only by **registering** them — which is a design act, so this document
is the evidenced, categorized work-list, not a unilateral edit.

> **Two honesty corrections (Fable-5 holistic audit, 2026-07-14 — `designs/audit/2026-07-14-holistic-unification/`):**
> 1. **The "52.7% resolved" figure is *matched*, not *keyed*.** `resolve()` matching a name is not the
>    same as that name pointing to a registry KEY — the registry deliberately declines to key ~17
>    identifiers (`not_descriptors`: tracks/clocks/derived values like `Mandate`, `Treasury`, `CI`). The
>    **true keyed pointer rate is 12/55 = 21.8%**, not 52.7%. `pointer_audit.py` now reports both the
>    keyed rate and the matched rate side by side; treat **keyed** as the real NS2 meter.
> 2. **Category A moved the number by *text editing*, not registration.** The 45.8%→52.7% delta is
>    entirely: 6 shorthand strings (`L_s`/`PS_s`/`settlement Order`…) deleted and replaced with spellings
>    that *already resolved*, plus 2 already-known display names added. **Zero previously-unresolved
>    identifiers were newly registered.** It is legitimate document hygiene, but it is not debt paid
>    down — the debt-closing work is Category B (below), still un-executed and Jordan-gated.

Every mapping in Category A below is backed by the module's OWN `module_contracts.yaml` `state`
prose or a descriptor entry — cited inline. Nothing here fabricates a quantity (CLAUDE.md §5).

---

## Category A — abbreviation/alias of an ALREADY-registered quantity — **DONE (ED-IN-0060, dfb9da6)**

**Executed** — but via **contract-side canonicalization**, not the alias-adds proposed below: the
`settlement_layer` `module_contracts.yaml` derivation shorthand was rewritten to the quantities' real
registry names (`L_s`→`Legitimacy`, `PS_s`→`Popular Support`, `settlement Order`→`Order`, etc.), so
the module now references the pointer directly and `descriptor_registry.yaml`/the mirror gate were
never touched (lower blast radius than alias-adds). This moved the meter 45.8%→52.7%. The table below
is the original proposal, retained for provenance.

These were the low-risk, no-new-design wins: the quantity already exists in
`references/descriptor_registry.yaml`; the identifier was just an abbreviated / scale-suffixed / prose
form the resolver didn't recognize. The originally-proposed fix was to add the form as an `aliases:`
entry on the existing key — with the caveat that `descriptor_registry.yaml` is CI-mirrored to
`names_index.yaml` by `tools/ci_names_consistency.py` and self-declared IN FLUX, so each alias-add
would need the mirror gate green. The contract-canonicalization route sidestepped that entirely.

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

## Category C — not a scalar quantity reference (scope refinement, partly DONE)

Two sub-classes the raw meter wrongly counted as pointer-debt:

**C1 — formula-local intermediates — DONE (ED-IN-0061).** A derivation input that its own `formula`
defines (e.g. settlement_layer's `W_s = base(Type)+Prosperity+FacilityTier`) is a variable, not an
external quantity reference. `pointer_audit.py` now detects these rigorously (LHS-of-`=` in the same
derivation's formula), excludes them from a **refined meter**, and **logs every exclusion** (never a
silent cap). Today: `W_s` is the only one; refined meter 53.7% unique / 60.0% occurrences vs the raw
52.7% / 59.2%.

**C2 — candidate non-scalar structured state — needs a DESIGN RULING (not auto-excluded).**
`npc_behavior`'s `arc state`, `beliefs`, `concerns`, `opinions`, `projects` read as an NPC's
relational / psychological state graph, not scalars — but the contract buckets them as `track`/`clock`
(same as real scalars like `Legitimacy`), so they are NOT rigorously distinguishable by tooling.
Whether they are registry quantities at all is Jordan's call. They are left IN the debt list (flagged,
per the pointer register's triage note) rather than silently dropped, pending that ruling.

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
