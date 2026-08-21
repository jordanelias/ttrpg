# UI — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/ui/` · **Lane:** `IN` · **Contracts:** none found
**Code roots traced:** `systems/ui/`, `references/module_contracts.yaml`, `references/canonical_sources.yaml`, `CURRENT.md`, `godot/skeleton/`, `dashboard/`, `tools/observability/`, `systems/ui/_identifier_census.yaml`
**Traced at:** `6545067`

## 1. Entry points

_(none — see §7)_

## 2. IN

_(none — see §7)_

## 3. Flow

_(none — see §7)_

## 4. OUT

_(none — see §7)_

## 5. State touched

_(none — see §7)_

## 6. Seams

_(none — see §7)_

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| No code files (`.py` or `.gd`) exist anywhere under `systems/ui/`. Directory listing is design docs and a generated census only. | `systems/ui/valoria_ui_ux_v4.md:1` (representative doc; `find systems/ui -type f` observed at trace time returns 10 files, all `.md`/`.yaml`, zero `.py`/`.gd`) |
| `references/module_contracts.yaml` declares no `ui` / `ui_ux` module. The file's full `module:` roster (27 entries, grepped `  - module:` across the file) contains no UI-named entry — the subsystem has no `consumes`/`emits`/`resolver`/`sim_module` contract at all, not merely an unbuilt one. | `references/module_contracts.yaml:81` (`faction_state`, first of the 27 `- module:` rows; grep of the same pattern across the file returns no `ui` row) |
| `references/canonical_sources.yaml`'s `ui_ux` entry names only design docs (`design_doc`, `valoria_ui_ux_1`) — no `sim_module` or code-pointer key of any kind, unlike entries for built subsystems. | `references/canonical_sources.yaml:446-449 ui_ux` |
| `CURRENT.md` carries no row for the `ui` subsystem or `ui_ux` doc at all (grepped `ui_ux` and `systems/ui` against the full file: zero matches) — consistent with the flow-skeleton roster's own note that `ui` is "not yet formalized" as a 1:1 subsystem. | `systems/_architecture/subsystem_flow_skeletons_v1.md:117-119` |
| `godot/skeleton/` — the one Godot-facing illustration tree in the repo — contains 8 `.gd` files, all under `engines/combat/` or `core/`; none is UI-named, none extends `Control`, and the repo has zero `.tscn` scene files anywhere (`find . -iname "*.tscn"` returns nothing). Apparent `grep -i "ui"` hits inside those files are substring false-positives inside words like "require"/"build", confirmed by opening the matched line. | `godot/skeleton/core/engine_manifest.gd:2` (matched line read directly: "reads data/engines/<id>/<id>.tres..." — the "ui" substring is inside "requires", not a UI reference) |
| `dashboard/` and `tools/observability/` are a **different subsystem**, not this one's code: they are repo/design-process introspection tooling (workplan progress, editorial ledger, CI health, a Key-propagation graph console) — not the Valoria videogame's player-facing UI that `systems/ui/`'s design docs specify. Distinguished by direct evidence, not by name: `tools/dashboard_data.py` opens by describing itself as assembling `dashboard/data.json` for the "Valoria GitHub Pages dashboard...workplan progress, recent activity, audit/simulation verdicts"; `tools/observability/README.md` opens by naming itself a "System Transparency Console...data-management & observability layer" over design data. Neither file tree consumes or is referenced by any `systems/ui/*.md` doc (checked via `grep -rn "systems/ui" .` — the only hits are alias/index/proposal rows, none from `dashboard/` or `tools/observability/`). | `tools/dashboard_data.py:3` (`dashboard_data.py — assembles dashboard/data.json for the Valoria GitHub`); `tools/observability/README.md:1-3` ("Valoria — System Transparency Console...data-management & observability layer") |
| `systems/ui/_identifier_census.yaml` (generated, `tools/build_identifier_census.py`) reports 28 identifiers as `disposition: BUILT` against the UI docs' vocabulary, but every `built_in:` pointer for those rows resolves into **other** subsystems' code (e.g. `systems/combat/combat_engine_v1/combatant.py`, `systems/settlements/sim/settlement.py`, `systems/factions/sim/tribunal.py`, `key_type_registry_v30.md`) or into the unrelated `tools/observability/`/`dashboard_data.py` tooling above — never into `systems/ui/` itself. The census's own documented limitation (BUILT is a name match, not a wiring proof) applies exactly here: these are coincidental name collisions with peer-subsystem mechanics, not UI implementation. | `systems/ui/_identifier_census.yaml:65-71 belief_revised` (built_in: `key:key_type_registry_v30.md`); `systems/ui/_identifier_census.yaml:893-901 max_wounds` (built_in: `py:systems/combat/combat_engine_v1/combatant.py`); `systems/ui/_identifier_census.yaml:1-2` (limitation notice: "BUILT is a NAME match, not a wiring proof") |
| The design docs themselves self-describe as pre-implementation reference specs, not built surfaces: the primary doc's status line calls it "approved for **development reference** use" and frames Godot notes as forward-looking ("How it is built" guidance for future implementers), consistent with zero code existing yet. | `systems/ui/valoria_ui_ux_v4.md:6` (`**Status:** CANONICAL — approved for development reference with editorial permission...`) |
| **The one code artifact in the tree that self-identifies as UI is `engine/cross_scale/articulation.py`**, whose module docstring names "Tier 1 UI Lens" as its first concern and whose `render_protagonist_lens` is that tier's entry point. It is filed under the `articulation` subsystem, not here, and is traced in that subsystem's skeleton — but it is the closest thing to game-UI code that exists, and excluding it silently would misrepresent the search. It is a `stubwire` no-op with no callers, so it does not change this file's §§1–6. | `engine/cross_scale/articulation.py:2` (docstring: "Articulation Layer — Tier 1 UI Lens, Tier 2 Triggers, Tier 3 Chronicle"); `engine/cross_scale/articulation.py:35 render_protagonist_lens`; cross-reference: `systems/articulation/articulation_flow_skeleton_v1.md:1` |

**Conclusion:** `ui` is a subsystem with design documentation and no code of its own — no `.py`,
no `.gd`, no `.tscn`, no module contract, no `sim_module` pointer, and no `CURRENT.md` row.
Sections 1–6 are empty because there is no flow to trace, per standing rule 2.

**Scope boundary, stated because the search would otherwise look narrower than it was.** The one
UI-named code path in the tree (`render_protagonist_lens`, the articulation Tier-1 lens) belongs
to `articulation` by both its file location and its `CURRENT.md` row, and is traced there. This
file's claim is therefore "`ui` owns no code", not "nothing in the tree renders anything" — a
distinction the last row above records rather than leaves to inference. Whether the player-facing
UI specified by `systems/ui/`'s design docs should eventually claim that lens is a design
question, not a traced fact, and nothing here proposes an answer.
