# Canonical Nomenclature — namespaced identifiers for every named thing

## Status: PROPOSED — not ratified. Nothing in this document renames anything.
## Version: v0.1 (plan only)
## Lane: IN (cross-cutting) · **no ED allocated** — see note below
## Author: planning pass 2026-08-11, at Jordan's direction
## Supersedes: nothing. Executes the item HELD in `registers/handoffs/HANDOFF_IN.md`
##   ("Dotted-namespace nomenclature for canonical identifiers", ED-IN-0152).

> **No ED is allocated and `references/id_reservations.yaml` is deliberately NOT bumped.** This
> document is surfaced by *location* (`proposals/`, per `tools/observability/build_proposals.py`),
> so it needs no ID to be visible. Claiming `ED-IN-0153` here without allocating it is precisely
> the same-lane collision that hit PR #298/#299 last week — the `ED-<LANE>` tag prevents cross-lane
> collision by construction, not same-lane. An ID is allocated **when Phase 0's rulings land**, at
> which point the scope is known and worth an ID.

> **Jordan's framing, verbatim from the session that opened this:** *"We need to rename an
> incredible number of attributes, scores, concepts, names, terms and definitions so that
> grepping/pattern matching/regex do not produce noise. For example, Almud Almqvist should be
> `npc.almud_almqvist` in all code for clarity. Each category/class of values requires its own
> nomenclature."* Worked examples given: `settlement.piety_track`, `world.invasion_pressure`.

---

## 1. The headline finding: this is an ADOPTION problem, not a rename problem

The dotted namespace **already exists**. `references/names_index.yaml` has carried 113 dotted keys
since before the v40 generation — `attr.mind.acuity`, `set.legitimacy`, `clock.ip`,
`world.king_almud_almqvist`. `references/definitions/definitions.yaml` (117 records),
`references/proper_noun_registry.yaml` (62, already snake_cased under category sections) and
`references/glossary/glossary.json` (1,537 terms) all key off it.

**It was never adopted as the identifier form.** Measured 2026-08-11 — for each of the 51
non-proper-noun dotted keys, the count of files outside the generated registries
(`references/`, `dashboard/`, `registers/`, `audit/`) that contain the dotted string:

| where the dotted form actually appears | keys | note |
|---|---:|---|
| Nowhere outside the generated registries | **16** | the key exists only to index itself |
| Only in `tools/`, `tests/`, `skills/`, `engine/tests/`, `engine/engine_params/` | **32** | tooling scaffolding, not game code |
| In engine code or a live design doc | **3** | see below |
| | **51** | all non-proper-noun keys |

All three of the last row, in full — this is the entire real-world adoption of the quantity namespace:

- `substrate.key` — 7 files, genuinely load-bearing (`engine/substrate/__init__.py`,
  `engine/cross_scale/articulation.py`, two `systems/factions/sim/` modules, three flow skeletons).
- `fac.intel` — 1 file (`engine/autoload/game_state.py`).
- `clock.mending_stability` — 2 files, both **design docs**, no code.

So one key is adopted, one is a single mention, one is prose. The engine otherwise runs on bare
`self.order` / `self.defense` / `world.clocks['MS']`. The corpus is not carrying 10,000 mis-named
identifiers that must be rewritten — it is carrying **a naming layer nobody plugged in**.

> **Reproduce it** (§0.1 point 3 — a result claim ships with the check that would falsify it): for
> each non-`world.` key in `names_index.yaml`, `grep -rlI -F <key> .` excluding the generated
> registries (`references/ dashboard/ registers/ audit/ deprecated/`) **and excluding this document**,
> which cites 13 of the keys and would otherwise inflate its own numbers. That exclusion is not
> cosmetic: without it the measurement reads 9 / 24 / 18 and the finding inverts.

That changes the shape of the work: **rule the grammar, fix the roster's axis, then adopt on a
ratchet** — rather than a single flag-day rewrite across ~10k references.

### 1.1 The noise is real and measured

Raw corpus hits for canonical display names that are ordinary English words (`.py`/`.md`/`.yaml`/`.json`,
`deprecated/` excluded):

| canonical name | registry key | raw hits | files |
|---|---|---:|---:|
| Order | `set.order` **and** `conv.order` | 1,630 | 414 |
| Authority | `ppt.authority` | 1,366 | 279 |
| Standing | `mech.standing` | 1,234 | 285 |
| Evidence | `ppt.evidence` | 1,193 | 296 |
| Discipline | `mass.discipline` | 1,151 | 274 |
| Military | `fac.military` | 1,092 | 191 |
| Reason | `conv.reason` | 964 | 287 |
| Pressure | (settlement field) | 784 | 227 |
| Power | `mass.power` | 744 | 213 |
| Will | `attr.mind.will` | 665 | 246 |
| Precedent | `conv.precedent` | 635 | 198 |
| Command | `mass.command` | 564 | 136 |
| Legitimacy | `set.legitimacy` | 513 | 124 |

Corroborated independently by `references/ENGINE_ATLAS.md` §5 (generated, stays current): the 27
**contract names** have a median of **131** bare occurrences — worst `audit` at 2,174,
`mass_battle` 2,075, `victory` 1,929 — and **zero** qualified uses anywhere. The 56 **key types**
are the control group: dotted by construction, median **24** occurrences, and nobody has ever
complained about finding them.

**The control group proves the thesis.** Nothing about this repo makes names unfindable. The keys
that carry a namespace are findable; the ones that don't, aren't.

---

## 2. The decision that gates everything: which axis?

Three namespace axes are live in the tree **right now**, and they contradict each other:

| axis | where | example | population |
|---|---|---|---|
| **A. Kind/category** | `names_index.yaml` | `clock.ip`, `set.legitimacy`, `attr.mind.will` | 51 quantities |
| **B. Event domain** | `key_graph.json` / key type registry | `scene.combat_hit`, `state.succession`, `da.public_governance` | 56 keys |
| **C. Owner/scale** | Jordan's three examples | `npc.almud_almqvist`, `settlement.piety_track`, `world.invasion_pressure` | — |

They are not compatible where they overlap:

- **`clock.ip` (axis A) vs `world.invasion_pressure` (axis C)** — same value, different prefix,
  and axis C also demands the abbreviation be spelled out.
- **`world.king_almud_almqvist` (current) vs `npc.almud_almqvist` (asked for)** — today `world.*`
  is a 62-entry grab-bag holding NPCs, factions, territories, realms, peoples *and* concepts, with
  the real category demoted to an optional `token_class:` field that is populated on only 30 of 113
  entries. Axis C promotes `token_class` to the prefix and frees `world.` for world-scale state.

### RECOMMENDATION — a two-axis grammar, not one

Jordan's three examples all name **owner/scale**, and the instruction *"each category/class of
values requires its own nomenclature"* is the tell: one flat namespace was never the ask. Propose:

> **Axis C (owner/scale) governs entities and owned state. Axis B (event domain) is retained
> unchanged for Key types. Axis A is retired** — its information moves into the leaf or into
> registry metadata, not the prefix.

Why axis B survives: a Key is an **event**, not a value owned by an entity, so it is a different
category and gets its own nomenclature — which is exactly what the instruction asks for. It is
also the one part of the corpus already measured as working (median 24 hits). Per CLAUDE.md §0.1
point 5, **fix what is broken, do not sweep what is working**.

---

## 3. The proposed roster

### 3.1 Grammar

```
<namespace>.<leaf>                    settlement.piety_track
<namespace>.<group>.<leaf>            character.mind.will      (only where a group is canonical)
```

Five rules, each with a stated reason:

1. **Namespaces are spelled out, never abbreviated.** `set.` → `settlement.`, `fac.` → `faction.`,
   `agg.` → `aggregate.`, `conv.` → `conviction.`, `ppt.` → `pressure_point.`, `mass.` → `unit.`.
   *Reason: `set.` is a Python builtin — `grep "set\."` is unusable, which defeats the entire
   purpose. `fac.`/`agg.`/`ppt.` are not words and cannot be read without the legend.*
2. **Leaves are spelled out, never abbreviated.** `clock.ip` → `world.invasion_pressure`.
   *Reason: `references/name_collision_database.yaml` already documents abbreviation collisions as
   a standing hazard, and `IP` is a two-letter token that matches inside prose in any language.*
3. **No leaf may be a bare ambiguous English word.** Test it against the ambiguity floor
   `build_glossary.py` already uses (60 files). `settlement.order` fails on the *leaf* but passes
   as a whole dotted string — so the rule binds on **the dotted form being the citation form**,
   not on banning the word.
4. **The dotted ID is the access path in code, not a decorated comment.** `settlement.piety_track`
   is already what Python gives you when the variable is named for its type and the field is named
   for the leaf. The rule is therefore: *the dataclass field name equals the leaf, and the
   conventional local/parameter name equals the namespace.* Where the owner is not in the
   expression — dict-keyed state such as `world.clocks['MS']` — **the string key becomes the full
   dotted ID**: `world.clocks['world.invasion_pressure']` collapses to a flat
   `world.state['world.invasion_pressure']`, or the clock dict is replaced by fields. That is a
   per-subsystem design call, not a naming call.
5. **One concept, one ID.** `piety_track` is currently *Conviction Track (CV)* **and** *Piety
   Track (PT)* **and** `conviction_track` — three names, one stat, with a rename deferred as "a P2
   cost-benefit decision for a dedicated cleanup pass" since 2026-04-17 (`ED-644`, restated
   `systems/factions/faction_politics_v30.md:787`). **This is that pass.**

### 3.2 Namespace roster (PROPOSED — the part most needing Jordan's eye)

**Entities** — a thing that exists in the world.

| namespace | contents | population today |
|---|---|---|
| `npc.` | named characters | 46 (`npc_registry`) / 25 (`proper_noun_registry`) |
| `faction.` | the six factions + subfactions | 6 + 2 |
| `settlement.` | named settlements | from `settlement_layer` |
| `territory.` | territories / provinces | 17 |
| `realm.` | realms | 3 |
| `region.` | regions | 2 |
| `people.` | peoples | 4 |
| `org.` | organizations | 1 |

**Owned state** — a quantity belonging to an entity class. Prefix = the owner, leaf = the quantity.

| namespace | contents | migrates from |
|---|---|---|
| `character.` | 9 personal attributes + 3 aggregates | `attr.*`, `agg.*` |
| `settlement.` | legitimacy, popular_support, prosperity, defense, order, piety_track | `set.*` |
| `faction.` | influence, wealth, military, intel, stability | `fac.*` |
| `world.` | the 6 world clocks, spelled out | `clock.*` |
| `unit.` | power, discipline, command | `mass.*` |
| `thread.` | thread_fatigue | `thread.*` (unchanged) |

**Non-owned classes** — each its own nomenclature, per the instruction.

| namespace | contents | migrates from |
|---|---|---|
| `conviction.` | the 7 convictions | `conv.*` |
| `pressure_point.` | the 4 pressure points | `ppt.*` |
| `mechanic.` | disposition, standing, stability, mandate, tensions | `mech.*` |
| `contract.` | the 27 module contracts | **bare today** — median 131 noise hits, 0 qualified |
| `key.` *(or unchanged)* | 56 event types | `scene.`/`state.`/`meta.`/`da.`/`env.`/`mechanical.` |
| `substrate.` | Key primitive | unchanged |

**Note the collision `settlement.` must absorb:** it is both an entity namespace and an owned-state
namespace. That is *correct and intended* — `settlement.hafenmark` is an instance,
`settlement.legitimacy` is a field of the class. Same for `faction.`. If Jordan wants them split,
the alternative is `settlements.` for instances vs `settlement.` for fields, which is one character
of distinction and will be mistyped forever. **Recommend accepting the overlap.**

### 3.3 Four cases this roster does NOT settle — Jordan's call

1. **`piety_track`'s owner.** Jordan's example says `settlement.`. The corpus says otherwise:
   `references/module_contracts.yaml:253` files it under `systems/characters/`, and
   `systems/characters/conviction_track_v30.md:31` calls it a **per-territory** stat. So the
   candidates are `settlement.`, `territory.`, or `character.`, and the three docs disagree with
   each other independently of this proposal. **This is a design ruling, not a naming one.**
2. **Do Key types get a `key.` prefix?** They work as-is. Adding one costs 56 renames + every
   generated join for uniformity's sake alone. **Recommend: leave them.**
3. **Contract names — full rename or citation-form only?** The held ED-IN-0152 note poses exactly
   this. Full rename touches ~10k references and every generated artifact that joins on the bare
   name. Citation-form-only (`contract.victory` in prose/comments, file and YAML keys untouched) is
   additive and the atlas already measures adoption. **Recommend: citation-form only, for
   contracts specifically** — they are module names, not values, and the join surface is enormous.
4. **`world.` reuse.** Freeing `world.` from proper nouns is what lets `world.invasion_pressure`
   exist. It orphans 62 entries that must be re-prefixed in the same pass, or the namespace means
   two things at once during the interim.

---

## 4. A blocker found while planning: the rename executor covers almost nothing

`tools/valoria_rename.py` is the repo's designated "change once" executor — its docstring promises
it "rewrites every word-boundary occurrence of the old name across the design corpus AND the
registries". Its scope is `SCOPE_DIRS = ('designs', 'params', 'references', 'canon')` and
`EXTS = ('.md', '.yaml', '.yml', '.jsonl', '.txt')`.

- `designs/` was **retired 2026-07-19** (ED-IN-0071 P4/P5) — the tree is gone.
- `params/` was moved to `engine/params/` in 2026-07-16 and **evacuated 2026-08-05** (ED-IN-0145).
- `systems/`, `engine/`, `godot/`, `workplans/`, `proposals/` were never added.
- `.py` and `.json` are not in `EXTS` at all.

Measured coverage against the live tree:

| | files |
|---|---:|
| In scope (`references/` + `canon/`, matching extensions) | **67** |
| Silently missed — live design corpus + code docs | **270** |
| Silently missed — `.py`, not in `EXTS` | **261** |
| Silently missed — `.json`, not in `EXTS` | **41** |

`iter_files()` does `if not os.path.isdir(d): continue` — so two of its four roots vanish with **no
error and no warning**. This is the same defect class as the three "gates reporting clean over
nothing" found in one week (ED-IN-0147, ED-IN-0148) and the `build_glossary` silent-coverage trio
(ED-IN-0150): *a reader quietly covering a fraction of its source.* It was correct when written and
stopped working when the tree moved underneath it — **CLAUDE.md §0.1 point 5's exact signature of a
pattern defect.**

**Consequence for this plan: Phase 1 cannot start until this is fixed and guarded.** Per §0.1 point
5, the fix is one owner + a guard that fails on recurrence: the scope roots must be *derived* (or
asserted to exist at startup), and a test must fail if any configured root is absent. Without that
guard, every subsequent phase would report success over a fraction of the corpus.

---

## 5. Phasing

The lifecycle is the one this repo already uses for A1–A17 (`proposed_quantity_armature_extension.md`
§4): **land report-only → burn the backlog → flip to blocking at zero.** Reused, not reinvented.

### Phase 0 — Rulings (Jordan; no code)
Decide §2's axis and §3.3's four open cases. Everything downstream is mechanical once these land.
**Cost: one review sitting.**

### Phase 1 — Grammar, roster, and instruments
- `references/namespace_registry.yaml` — the closed roster of namespaces, single-owned. New
  namespaces are an edit here, not a convention that spreads by imitation (the failure mode
  CLAUDE.md §4 records for the retired index+infill pair).
- Fix + guard `valoria_rename.py` (§4). **Blocking prerequisite.**
- Extend `names_index.yaml` with an **additive** `namespaced_id:` field. Nothing renames yet; both
  forms resolve. `definitions.yaml`, `glossary/`, `dashboard/` regenerate from it.
- `tools/ci_nomenclature_check.py` — **report-only**. Composes `quantity_registry.py` (the existing
  single reader of the merged vocabulary) and `obs_core.py`; does not re-parse a registry. Reports
  three numbers: roster conformance, adoption rate, and per-leaf grep noise against the
  ambiguity floor.
- **Falsifier, per §0.1 point 3:** a test that mutates one roster entry and asserts the checker
  fails. If the checker cannot fail, it is not a checker.

**Deliverable: the noise is measured per identifier and tracked over time. Zero renames.**

### Phase 2 — Migrate the registries
Re-key `names_index.yaml` / `proper_noun_registry.yaml` onto the ruled roster; regenerate the four
generated views. Legacy keys stay resolvable via the existing `aliases`/`legacy` machinery — this
repo already has alias resolution and `references/restructure_ledger.md` precedent for pointer rows.
**Bounded: 113 + 62 entries, all in files that are already single-owned and gate-checked.**

### Phase 3 — Adopt in code, one lane per PR
Per CLAUDE.md §4's session lane-scoping: **one subsystem per PR**, not a flag day. Order by measured
noise, worst first — `settlements` and `factions` lead (`order`, `defense`, `stability`, `military`,
`legitimacy` are all theirs). Each PR: rename fields → route dict-keyed state onto full dotted IDs →
`pytest tests/valoria` + the lane validator → adoption number moves in the report.

**The hazard here is named explicitly, per §0.1 point 1: read/write asymmetry.** Renaming a field
while a writer still assigns the old name makes the writer a silent no-op.
`tests/valoria/test_morale_write_sweep.py` is the existing template and its `_CELL_OWNED` registry
is field-parameterized — **each renamed field is added there as one key.** Grep the field's
*assignments*, not its readers.

Second named hazard: `engine/tests/` is a **seeded** regression + parity suite and there are byte-exact
goldens (`tests/valoria/golden_*.json`, `r3_identity_golden.json`). A rename must be **provably
behaviour-neutral** — goldens re-record only when a diff proves the change was pure naming. §0.1's
retracted-flag incident is precisely a golden re-recorded on a confounded change.

### Phase 4 — Flip to blocking
At zero backlog, `ci_nomenclature_check.py` becomes a blocking gate. New names cannot land off-roster.

---

## 6. What this costs, honestly

| phase | scope | risk |
|---|---|---|
| 0 | 4 rulings | none — but everything blocks on it |
| 1 | ~3 new/fixed tools, 1 registry, additive field | low; nothing renames |
| 2 | 175 registry entries + regenerated views | low; single-owned, gate-checked files |
| 3 | 15 subsystems × (Python fields + docs + string keys) | **the real cost.** Goldens + write-asymmetry |
| 4 | one flag flip | low |

Phase 3 is where this can go wrong, and it goes wrong in exactly two ways that this repo has
already been burned by and already has instruments for. Both are named above with their existing
guard. **No phase re-implements a rule that already lives once** (§8).

---

## 7. What this proposal deliberately does NOT do

- **Does not ratify.** No head moves, no `## Status:` flips, no contract edited.
- **Does not touch Key types.** They are the control group that proves the thesis; §0.1 point 5
  says fix the defect, do not widen the sweep.
- **Does not decide `piety_track`'s owner.** Three docs disagree; that predates this proposal and
  is a design ruling.
- **Does not propose a full contract rename.** Recommends citation-form only, and says why.
- **Does not claim `pytest tests/valoria` validates any of this.** It is a shipping gate, not a
  belief gate (§0.1) — a pure-rename PR that is silently a no-op would pass it green.
