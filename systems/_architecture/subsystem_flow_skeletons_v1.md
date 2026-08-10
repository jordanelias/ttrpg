# Subsystem Flow Skeletons — index, format spec, and roster (v1)

## Status: REFERENCE — traced structure only; authors no design content

> **What a flow skeleton is.** The *base logical flow* of one subsystem: entry points, the
> ordered steps the code actually executes, the branches and gates between them, what comes
> in, what goes out, where it touches its peers, and where the flow is declared but absent.
>
> **What it is not.** Not mechanics, not formulas, not constants, not balance, not prose.
> A skeleton carries **no infill**. If a statement would still be true after every number in
> the subsystem changed, it belongs here; otherwise it belongs in the subsystem head
> (`CURRENT.md`) or its params, not here.
>
> **How it is built.** By tracing **code**, not by reading design docs. Design prose states
> intent; the skeleton states structure-as-built. Where the two disagree, the skeleton records
> the code and files the divergence in §7 — it never silently adopts the doc's version.

**Owner of the format:** this file. **Owner of the roster:** the table in §3 below — the guard
test parses it, so adding a subsystem here is what makes the guard demand its skeleton.
**Guard:** `tests/valoria/test_flow_skeletons.py`.

---

## 1. The anchor rule (the anti-fabrication device)

Every factual line in a skeleton ends with an **anchor**:

```
`relative/path/to/file.py:123 symbol_name`
```

- backtick-delimited, repo-relative path, `:`, a 1-indexed line number, optionally a space and
  the symbol the line is about. A span is written `path:123-140`.
- The guard asserts: the file exists · the line(s) exist · and, when a symbol is given, that the
  symbol **names those lines**, in one of exactly two forms:
  - **definition-site** — `path:215 generate_npc` cites where the symbol is declared. The symbol
    must appear within ±3 lines.
  - **body-region** — `path:250-259 generate_npc` cites a region *inside* the symbol, which is
    how a flow step points at the one branch it describes rather than at the whole function. The
    nearest preceding `def`/`class` of that name must enclose the region.

  Both are checked against the tree, so neither is a loophole: a body-region anchor still has to
  land inside the right function.
- **One anchor per backtick span.** A comma list (`` `path:113,196,212-213` ``) is **not** an
  anchor — the guard's pattern does not match it, so it parses as *zero* anchors and the claim
  goes unchecked while still looking cited. Split into one span per location. Likewise the symbol
  slot takes an **identifier only**; descriptive prose goes outside the backticks, where it is
  honestly unverifiable rather than dressed as evidence.
  Both shapes are enforced: `test_no_unparseable_anchor_lookalikes` fails any span that *looks*
  like an anchor but does not parse as one. That test exists because the comma form was found in
  10 of 15 skeletons at first review, silently degrading 87 citations to unguarded prose — a
  guard that ignores malformed input fails in the worst direction.

That third assertion is the point. A skeleton assembled from plausible-sounding recall rather
than from the tree fails it, because invented line numbers do not land on their symbols. The
guard is mutation-verified — see the test's own docstring.

**Corollary:** never cite a line you did not open. An unanchored claim is either a §7 gap or
does not go in.

## 2. The per-subsystem file format

Path: `systems/<subsystem>/<subsystem>_flow_skeleton_v1.md`. Sections are **required and
ordered**; the guard fails on a missing or reordered heading. Empty is a legitimate state — an
empty section says "traced, found nothing", which is information; deleting it says nothing.

```markdown
# <Subsystem> — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/<x>/` · **Lane:** `<XX>` · **Contracts:** `<module names>`
**Code roots traced:** `<paths actually opened>`
**Traced at:** `<commit sha>`

## 1. Entry points
## 2. IN
## 3. Flow
## 4. OUT
## 5. State touched
## 6. Seams
## 7. Traced gaps
```

### Section contracts

| § | Holds | Shape |
|---|---|---|
| 1 | Every callable an outside caller can enter this subsystem through | table: callable · anchor · called-by (anchor, or `—` if uncalled) |
| 2 | What flows in | table: input · kind · origin · anchor. `kind` ∈ `key`, `world-state`, `arg`, `param`, `flag`, `registry`, `file` |
| 3 | The ordered flow | numbered steps `S1`, `S2`, …; branches nest one level as `S1.1`; each step tagged `[gate]`, `[branch]`, `[loop]`, `[emit]`, `[write]` where it applies; each step ends with an anchor |
| 4 | What flows out | table: output · kind · consumer · anchor |
| 5 | State this subsystem reads or writes | table: field · `R`/`W`/`RW` · owning module · anchor |
| 6 | Cross-subsystem edges | table: direction (`up`/`down`/`lateral`/`in`/`out`) · peer · mechanism · anchor |
| 7 | Traced absences | table: gap · evidence anchor. A gap is declared-but-unimplemented, stubbed (`stubwire`), unreachable, default-off, or a code↔contract divergence. **Evidence is required** — an unevidenced suspicion is not a gap |

### Standing rules for authors

1. **Trace where the code is, not where the folder is.** Several subsystems own no code under
   their own folder; their flow lives in `engine/`, `tests/sim/`, or a peer's tree. Follow it.
2. **A subsystem with no code is a legitimate outcome.** Say so in §7 with evidence (an empty
   glob, a contract with no `sim_module`), and keep the other sections empty rather than
   filling them from the design doc.
3. **Never special-case.** If a step reads as "…except for faction X / weapon Y", that is
   scripting drift — record the general step and file the special case in §7.
4. **Default-off flags are structure.** A branch that never executes at default settings is
   still flow; tag it `[branch]` and record the flag's default in §7.
5. **Name the gate, not its value (RULED here 2026-08-10, ED-IN-0152).** Two reviewers split on
   this, so it is settled once rather than per-file. A threshold's *existence* is structure — the
   branch is there because something is compared — and survives the number changing. The *value*
   does not, so by this file's own test it is out of scope. Write "the stamina-collapse gate" and
   cite the line; do not write the number. Naming a `cfg` key is fine (it is an identifier, not a
   value); inlining the literal is not. This applies equally to a bare literal in code and to a
   named constant's value quoted in prose.

## 3. Roster

One row per subsystem folder under `systems/`. The guard reads this table.

| Subsystem | Lane | Skeleton |
|---|---|---|
| `_architecture` | IN | `systems/_architecture/_architecture_flow_skeleton_v1.md` |
| `articulation` | IN | `systems/articulation/articulation_flow_skeleton_v1.md` |
| `characters` | PC | `systems/characters/characters_flow_skeleton_v1.md` |
| `combat` | PC | `systems/combat/combat_flow_skeleton_v1.md` |
| `factions` | FA | `systems/factions/factions_flow_skeleton_v1.md` |
| `fieldwork` | FI | `systems/fieldwork/fieldwork_flow_skeleton_v1.md` |
| `mass_battle` | MB | `systems/mass_battle/mass_battle_flow_skeleton_v1.md` |
| `npcs` | WR | `systems/npcs/npcs_flow_skeleton_v1.md` |
| `overview` | IN | `systems/overview/overview_flow_skeleton_v1.md` |
| `settlements` | SE | `systems/settlements/settlements_flow_skeleton_v1.md` |
| `social_contest` | SC | `systems/social_contest/social_contest_flow_skeleton_v1.md` |
| `threadwork` | WR | `systems/threadwork/threadwork_flow_skeleton_v1.md` |
| `ui` | IN | `systems/ui/ui_flow_skeleton_v1.md` |
| `victory` | IN | `systems/victory/victory_flow_skeleton_v1.md` |
| `world` | WR | `systems/world/world_flow_skeleton_v1.md` |

Lane assignments follow `CLAUDE.md` §4's `ED-<LANE>-NNNN` taxonomy. For the folders that are not
yet formalized 1:1 subsystems, the lane column is the nearest owning lane, not a claim that the
lane exists for them.

**Which those are, measured rather than inherited (corrected 2026-08-10, ED-IN-0152).** Enumerating
`CURRENT.md`'s head-row table and asking which rows name a doc inside each folder gives **four
folders with no row of their own: `characters`, `ui`, `victory`, `world`.** An earlier draft of this
note copied `CLAUDE.md` §3's list (`characters`/`overview`/`victory`) and added `ui`, which was wrong
twice over: it **included `overview`**, which does have a row — *Clocks & tracks (cross-cutting)*,
naming `systems/overview/clock_registry_v30.md` — and it **omitted `world`**, which has none, despite
`systems/world/` holding live code that the season loop reaches every turn. `npcs` also has a row
(*NPC behaviour*), so it is not on the list either.

`CLAUDE.md` §3 still carries the older wording. The discrepancy is recorded here rather than fixed
there, because `overview`'s row is titled for a cross-cutting concern rather than for the subsystem,
so whether it "counts" is a governance call and not a fact this file may settle on its own.

## 4. What these are for

The Godot port's conversion unit is one module contract (`godot/godot_conversion_strategy_v1.md`
Part IV.3), and its per-module ritual consumes "the module's contract, its flatten artifact, and
its param export". The flatten artifacts named there (Part I.5) were written per-system in
2026-06 and are scattered; these skeletons are the same category of object, rebuilt uniformly
from the current tree, anchored, and guarded against rot. They are **not** a port plan and they
ratify nothing: no head moves, no status flips, no contract edits follow from authoring one.

## 5. Relationship to neighbouring surfaces

| Surface | Relationship |
|---|---|
| `references/module_contracts.yaml` | Declares the intended `consumes → resolver → emits` per module. A skeleton traces what the code does; §7 records where the two disagree. Neither edits the other. |
| `references/CONTRACT_INDEX.md` + `KEY_INDEX.md` | **The declared view, generated** (`tools/build_contract_index.py`, ED-IN-0151) — always fresh, because it is rebuilt from the contracts, the key graph and the wiring manifest. These skeletons are **the as-built view, hand-traced**. **Precedence: on any question of what is *declared*, the generated index wins and a skeleton must not restate it; on any question of what the code *does at the traced commit*, the skeleton wins.** Where they disagree, that is usually not an error in either — a declared-but-unbuilt edge is the system's real state, and §7 is where that gap is recorded. A skeleton's `Contracts:` header names contracts the index defines; `test_contract_names_resolve_in_the_generated_index` enforces that the names resolve there, so the two cannot drift in the place they overlap. |
| `godot/skeleton/` | GDScript illustration of one module (personal combat). Different artifact, different language, same word. These are `*_flow_skeleton_v1.md`; that one stays `godot/skeleton/`. |
| The retired index+infill pair | Unrelated. `CLAUDE.md` §4 retired `*_index.md`/`*_infill.md` as a default; "skeleton" there meant a document-atomization half. Here it means structure-without-mechanics. |
| `CURRENT.md` heads | Unchanged by these files. A skeleton is subordinate to its head on every question of design; on questions of what the code does, the code wins and the skeleton cites it. |
