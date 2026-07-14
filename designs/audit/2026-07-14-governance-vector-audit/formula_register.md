# Formula register — L1 quantity-dependency layer (module_contracts.yaml + descriptor_registry.yaml)

Deterministic, working-tree only. **Measures; does not gate.** **Scope: CONTRACT-level formula structure only** — built from `references/module_contracts.yaml` `derivations[]` and `references/descriptor_registry.yaml` aggregates/`derived_from`. Does **not** parse `params/*.md` prose tables, so it cannot catch a formula contradiction that lives only in prose (e.g. the Prosperity x50-vs-x10 family) — see the script docstring for why that specific example does not collide as a same-output multi-definition at this layer. A real params-table/formula extractor is deliberately deferred, not attempted here.

**Scorecard:** nodes=30, edges=25 (15 module_contracts.derivations, 10 descriptor_registry), roots(pure inputs)=17, leaves(final outputs)=11, isolated=0, max-depth=2, cycles=0, orphan-inputs=2(+0 notional/placeholder-only), multi-def-outputs=0(+0 notional/placeholder-only).

## Orphan inputs — referenced as a derivation input, not resolvable via the registry, and not itself the output of any derivation

**Triage before acting — not every row is a genuine missing definition** (same caveat as the G_pointer register). This is the FA-A-01/`cascade_alignment_modifier` class *in principle*, but at the contract level it mixes three kinds: (a) a genuine referenced-but-undefined quantity (real defect); (b) a `quantity_registry` false negative — the name is unresolved only because of a leading/trailing qualifier word the resolver does not strip (e.g. `settlement Prosperity` vs registered `Prosperity`); and (c) an internal/intermediate quantity with no registry-eligible identity that A17 itself calls "expected backlog, not a bug" (e.g. `cumulative_damage`; or a formula-local intermediate like `W_s`, defined inside its own derivation formula). Do not assume a class — inspect each row against its home contract before filing (this note is generic; it is NOT a computed claim that every current row is (b)/(c)).

- `W_s` — 1 occurrence(s), e.g. `settlement_layer` derivation #4
- `cumulative_damage` — 1 occurrence(s), e.g. `personal_combat` derivation #0

## Multi-definition outputs — the same quantity is a `derivations.output` in more than one place
(none)

## Cycles — a quantity transitively depends on itself (Tarjan SCC > 1, or a self-loop)

**Node identity is the raw derivation string, not a resolved registry key** — so a cross-module feedback loop whose two legs spell the same quantity differently is NOT detected here. Concretely: `faction_state`’s `Mandate` is emitted annotated (`faction Mandate (cross-module → faction_state)`) but consumed bare (`faction Mandate`); those are two distinct nodes, so the real Mandate↔Legitimacy feedback does not close into an SCC and is absent below. This is a deliberate under-report: normalizing node ids by stripping the parenthetical would risk collapsing genuinely-distinct disambiguating annotations (see the script docstring). Treat the cycle list as a lower bound, and cross-module `(... → module)`-annotated outputs as known blind spots until a registry-key node identity is built.
(none)

## Malformed derivations — `output` field missing/blank (inputs were routed to a sentinel node so their orphan status still surfaces above)
(none)

## Roots — pure inputs (nothing in this DAG derives them)

- `W_s`
- `attr.body.agility`
- `attr.body.endurance`
- `attr.body.strength`
- `attr.mind.acuity`
- `attr.mind.focus`
- `attr.mind.will`
- `attr.social.attunement`
- `attr.social.bonds`
- `attr.social.charisma`
- `cumulative_damage`
- `faction Mandate`
- `prac.thread_sensitivity`
- `set.defense`
- `set.order`
- `set.prosperity`
- `terr.fort_level`

## Leaves — final outputs (nothing in this DAG consumes them as an input)

- `Garrison Strength`
- `Health`
- `Local Economy`
- `Public Order`
- `agg.body`
- `agg.mind`
- `agg.social`
- `faction Mandate (cross-module → faction_state)`
- `faction Treasury income (cross-module → faction_state)`
- `prac.tps`
- `province Accord`
