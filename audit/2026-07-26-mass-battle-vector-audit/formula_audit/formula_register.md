# Formula register — L1 quantity-dependency layer (module_contracts.yaml + descriptor_registry.yaml)

Deterministic, working-tree only. **Measures; does not gate.** **Scope: CONTRACT-level formula structure only** — built from `references/module_contracts.yaml` `derivations[]` and `references/descriptor_registry.yaml` aggregates/`derived_from`. Does **not** parse `params/*.md` prose tables, so it cannot catch a formula contradiction that lives only in prose (e.g. the Prosperity x50-vs-x10 family) — see the script docstring for why that specific example does not collide as a same-output multi-definition at this layer. A real params-table/formula extractor is deliberately deferred, not attempted here.

**Scorecard:** nodes=30, edges=25 (15 module_contracts.derivations, 10 descriptor_registry), roots(pure inputs)=17, leaves(final outputs)=11, isolated=0, max-depth=2, cycles=0 exact(+1 paren-normalized), orphan-inputs=2(+0 notional/placeholder-only), multi-def-outputs=0(+0 notional/placeholder-only).

## Orphan inputs — referenced as a derivation input, not resolvable via the registry, and not itself the output of any derivation

**Triage before acting — not every row is a genuine missing definition** (same caveat as the G_pointer register). This is the FA-A-01/`cascade_alignment_modifier` class *in principle*, but at the contract level it mixes three kinds: (a) a genuine referenced-but-undefined quantity (real defect); (b) a `quantity_registry` false negative — the name is unresolved only because of a leading/trailing qualifier word the resolver does not strip (e.g. `settlement Prosperity` vs registered `Prosperity`); and (c) an internal/intermediate quantity with no registry-eligible identity that A17 itself calls "expected backlog, not a bug" (e.g. `cumulative_damage`; or a formula-local intermediate like `W_s`, defined inside its own derivation formula). Do not assume a class — inspect each row against its home contract before filing (this note is generic; it is NOT a computed claim that every current row is (b)/(c)).

- `W_s` — 1 occurrence(s), e.g. `settlement_layer` derivation #4
- `cumulative_damage` — 1 occurrence(s), e.g. `personal_combat` derivation #0

## Multi-definition outputs — the same quantity is a `derivations.output` in more than one place
(none)

## Cycles — a quantity transitively depends on itself (Tarjan SCC > 1, or a self-loop)

Reported in **two passes** (Fable-5 2026-07-14 audit, finding F — previously this was a disclosed-but-unfixed blind spot; now detected):
- **Exact-identity cycles** — SCCs over the raw derivation strings.
- **Paren-normalized cycles** — a SECOND pass over a loose-form-collapsed view that strips trailing `(...)` annotations, so a cross-module feedback whose legs spell the same quantity differently DOES close. Concretely this catches the live Mandate↔Legitimacy loop (`faction Mandate (cross-module → faction_state)` emitted, `faction Mandate` consumed). Raw node identity is preserved everywhere else (roots/leaves/orphans); only cycle detection uses the collapsed view, and collapse-induced self-loops are dropped to avoid the annotation-shadowing false-positive the docstring warns about.

**Exact-identity:** (none)

**Paren-normalized (cross-module feedback the exact pass misses):** 
- faction Mandate -> set.legitimacy -> set.popular_support

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
