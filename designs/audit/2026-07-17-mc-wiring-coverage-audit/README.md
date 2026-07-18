# Monte-Carlo Engine — Wiring & Build-State Coverage Audit

## Status: ANALYSIS-ONLY — filed 2026-07-17 (ED-IN-0074). No canon ratified. Defects register (§6) is `needs_jordan`.

> **Path note (post-merge).** This audit was captured against branch `claude/monte-carlo-wiring-question-thpxul` *before* the ED-IN-0071 P3/P4 restructure (`sim/` → `engine/`, `designs/{combat,social_contest,fieldwork,world,settlements,threadwork,npcs,articulation,ui,architecture}` → `systems/`) merged to `main`. The `file:line` citations below reflect the **pre-restructure** layout; findings, counts, and structure are unchanged — only paths moved. (Originally allocated `ED-IN-0073`; renumbered to `ED-IN-0074` at merge — `main` PR #167's character-decision audit claimed `0073` first.)

**Scope.** A full accounting of what the Valoria simulation engine actually wires together at runtime, versus what the design corpus says *should* wire, versus what exists as code but is never reached. Built as an interactive, depth-toggleable map (`wiring_map.html`, this folder) and verified against the working tree by **six adversarial verification lanes + four coverage vectors** — not by reading alone. Every quantitative claim below was either executed (`run_campaign` over 7 seeds) or grep/AST-verified with a `file:line` citation in the lane reports.

The companion interactive map is `wiring_map.html` (open in a browser): one tree, every node anchored on a **stable registry tag** (`module:` / `adapter:` / `key:` / `ed:` / `q:`) rather than a file path — so it survives restructures like the `sim/→engine/` move. Toggleable across the 9-tier ladder **Wrapper → System → Subsystem → Module → Adapter → Mechanic → Submechanic → Routine → Subroutine**; each unit carries two axes — a **build badge** (this node's runtime wiring state) and a **gd badge** (the tagged unit's Godot-port state). Click any `key.type`, `State.field`, tag, or port-list unit to trace it across the tree. The **◧ Godot port view** renders the ranked port work-list.

**This map is now backed by a machine layer (the reusable utility) — see §9.** Its tags, coverage, and both axes are checked against the live registries by a committed validator, so the map can't silently drift as the code moves.

---

## 1. Headline

**The live `mc_v18` campaign loop runs roughly ~15% of the designed game.** It drives the strategic spine (faction actions → accounting → GD-1 victory) and one gated personal scene (an emergency-council contest that fires 0× in ~half of seeds). Almost everything else — the character/attribute foundation, the strategic Key-wiring layer, the board-game layer, most canonical quantities, and a second (richer) mass-battle engine — is **built-but-unwired, stubbed, or design-only.**

The single most important structural fact: **there is no `Character`/`Actor` dataclass anywhere in `World`.** The attribute → derived-stat foundation that every personal-scale roll depends on has no runtime home; resolvers either duck-type `getattr(actor,'strength',3)` or bypass character state entirely.

---

## 2. The pipeline (what actually runs)

```
run_campaign(seed)                                   sim/mc_v18.py
  └─ create_world(seed)                              game_state.py   (the World IS the game state; no DB)
  └─ while not world.winner:  run_season(cb)         peninsular/season.py
       ① advance_season(world)                       season_manager.py   (emits NO Key)
       ② _faction_actions_callback(world)            mc_v18.py
            ├─ faction_take_action ×4                 faction_action.py   (d6 _successes; d10 dice_engine for uniques)
            │    └─ conquest → resolve_mass_battle    massbattle.py       (~30–45 battles/campaign; single-encounter only)
            ├─ run_scene_phase                        scene_dispatch.py   (1 of 8 triggers fires; combat branch is dead code)
            └─ run_parliamentary_scene                parliamentary_bridge.py (every season; emits 13–65 Keys/campaign)
       ③ run_accounting(world)                        accounting.py       (CI · MS · insurgency · NPC drift)
  └─ check_all_factions → GD-1                        victory.py
  └─ CampaignResult
```

Three dice regimes are live and two fire in a single faction turn: `_successes` (d6 ≥4), `dice_engine.roll_pool` (d10), `sigma_leverage` (d+σ). Keys are emitted (13–65/campaign) but the pub/sub `subscribe()` channel has **zero subscribers** (`articulation`, the intended reader, is a stub); the only live Key-consumption path is a paired `apply=` closure that writes `Faction.L/I` ±1/±2 at `accounting_boundary`.

---

## 3. Methodology

**Six verification lanes** (adversarial — each mandated to falsify the map, defaulting to "the claim is wrong until proven"):

| Lane | Target | Outcome |
|---|---|---|
| Topology refutation | every call edge + status label | refuted 6 claims (see §5) |
| Stub census | every `NotImplementedError`/no-op in `sim/` | 36 `NotImplementedError` across 23 files |
| Designed-catalog | the full designed action/mechanic surface | ~45 design-only mechanics catalogued |
| Reachability + data-flow | wired-vs-unwired + state read/write sets | corrected 4 items; extracted the `rd`/`wr` graph |
| Subsystem observatory (pre-existing, `2026-07-14`) | the 27-module graph | cross-checked; supplied edge counts |

**Four coverage vectors** (set-difference — enumerate the corpus, diff against the map, return only the delta):

1. **Code symbols** — every `sim/` module/function absent from the map.
2. **Contract & Key graph** — the 27 `module_contracts.yaml` modules + ~50 `key_type_registry` edges.
3. **Design surface** — whole designed *layers* a runtime trace can't see (the attribute layer, board-game layer, clock/track registry).
4. **State & quantities** — every `World`/`Faction`/`Territory` field + every canonical clock/track/pool.

---

## 4. Coverage scorecard (before → after grafting the deltas into the map)

| Vector | Before | After |
|---|---|---|
| Contract modules represented | 15 / 27 | **27 / 27** |
| Intended Key-type edges drawn | 3 / ~50 | **~50 / 50** |
| Character / attribute layer | absent | represented (design) |
| Canonical clocks/tracks | ~8 / ~50 | ~50 (grouped by category) |
| World registries charted | 3 | + 6 dead-reg registries (~10 dataclasses) |
| Board-game systems | ~1 (CI Seizure) | ~11 |
| Mass-battle engines | 1 (shallow) | 2 (+ the unwired richer one under `tests/`) |

**The 12 contract modules that were entirely missing** (all now grafted at their attach points): `faction_state` (the in-degree-13 hub — consumes 20 of the 47 edges), `faction_politics`, `peninsular_strain`, `piety_track`, `territorial_piety`, `ci_political`, `npc_memory`, `npc_behavior` Procedures B/C/D/E, `game_director`, `scene_timer`, `audit`, `clock_registry`. (`settlement_economy` is a phantom flagged for retirement.)

**The ~47 Key edges** span `da.*` (5), `env.*` (4), `mechanical.*` (6), `state.*` (9), `meta.*` (6), `scene.*` (16), `scene_outcome.*` (1). The map draws all of them as traceable chips; only 3 were present before.

---

## 5. Corrections the audit forced on the running map

The verification lanes refuted the map repeatedly — recorded here so the process is auditable:

1. **"≈0 Keys flow in the loop" was false** — it's 13–65/campaign (parliamentary echo path; verified live).
2. **`advance_season` emits no Key** — `mechanical.season_change` belongs to the code-less `engine_clock`.
3. **`resolve_mass_battle` is live, not standalone** — ~30–45 battles/campaign.
4. **The combat branch is dead code**, not "deferred" — nothing queues `scene_type="combat"`, and it targets the *deprecated* `sim/personal/combat.py`; the canonical `combat_engine_v1` has zero path from the loop.
5. **The `module_contracts` combat ledger is stale** — 7 "PENDING" modules are built in Python; `feint` is retired, not unbuilt.
6. **"Keys are write-only" was false** — the paired `apply=` closure is a real (narrow) consumer.
7. **`treaty` / `home_sanctuary` / `infrastructure_reclamation` are stubs**, not built-but-unwired; **`adjacency` is actually wired**; **`simulate_npc_actions` is wired-but-vacuous** (`world.npcs` is never populated).

---

## 6. Defects register (`needs_jordan` — genuine bugs / canon-vs-code gaps, independent of the diagram)

| # | Finding | Evidence | Class | Candidate lane |
|---|---|---|---|---|
| D1 | **`Turmoil` (Political Stability) is write-dead.** Initialised at 0.0, read once by victory (`PS ≤ 6`), assigned by no live module — so the PS victory condition is trivially always satisfied. | `victory.py:73`; no writer in `sim/` | correctness | WR / IN |
| D2 | **`IP` (Institutional Pressure) is not a `world.clocks` key at all.** `create_world` never initialises it; the occupation-phase era ladder (`peninsular_strain` gates) can never fire. | `game_state.py:222`; `clock_registry_v30.md:18` | correctness | WR |
| D3 | **Latent one-way Mandate penalty.** `parliamentary_vote` writes `Faction.L` directly (outside Keys) on a Total Victory; its "restoration deferred to `season_manager`" promise is unimplemented. | `parliamentary_vote.py:213`; `season_manager.py` (no such logic) | correctness | SC (relates to ED-SC-0015) |
| D4 | **`fac.intel` ratified with a floor (2026-07-08) but the `Faction` dataclass has no `intel` field.** | `descriptor_registry.yaml:96`; `game_state.py:90-107` | canon-vs-code | FA (relates to ED-FA-0007) |
| D5 | **A second, richer mass-battle engine (`tests/sim/mass_battle/`) is actively developed (through 2026-07-08) but mislabeled by `sim/README` as a "frozen archive"** and is fully disconnected; the wired `resolve_mass_battle` collapses to one-line-vs-one-line. | `sim/README.md`; `tests/coverage_matrix.md`; `massbattle.py:1824-1825` | wiring + doc | MB / IN |
| D6 | **Wired-but-vacuous chain.** `generate_npc` has zero callers → `world.npcs` is always `{}` → `simulate_npc_actions` no-ops every season. Same shape for `world.knots` (`form_knot` uncalled) and `world.settlements` (`register_settlement` uncalled). | `npe.py:198,308`; `knots.py:172`; `registry.py:111` | inert-registry | IN |
| D7 | **Silent action-error swallowing.** Every `faction_take_action` is wrapped in `try/except Exception: pass`. | `mc_v18.py:94-97` | robustness | IN |
| D8 | **Two incompatible "canonical" attribute rosters coexist** — 9-attribute (`descriptor_registry`, IN-FLUX) vs 10-attribute (`params/core.md`) — and neither is wired; there is no `Character` dataclass. | `descriptor_registry.yaml:32-58`; `params/core.md:135-152` | schema | IN / PC |

Already-filed relatives (not re-raised here): `scene_outcome.battle_concluded` fabricated emit (**ED-MB-0010**), parliamentary total-victory Mandate stacking (**ED-SC-0015**).

**Correction status (2026-07-18).** **D2 / D4 / D5 / D7 are fixed and merged** (PR #180 landed D2/D5/D7; PR #182 landed D4). The four remaining — **D1, D3, D6, D8** — change campaign balance or need a schema ruling, so each is held for separate, sign-off-gated work. A companion brief, **`held_defects_brief.html`** (this folder), gives an executive summary + full detail for those four: the bug, the mechanism, the fix, and the catch (e.g. D3's restoration is verified correct but flips ~72% of campaign winners; D8 needs the 9- vs 10-attribute roster ruled first).

---

## 7. Residual limits (honest)

- The map represents every *system* and every *Key edge*, but **fine-grained scalars are grouped** under their owning system — itemising all ~80 dead-reg dataclass fields + ~50 quantities as individual nodes would add ~130 leaves for little navigational gain.
- The `by_reference` taxonomy (13 Convictions, the 13×4 axis matrix, contest styles, temperaments) is noted, not enumerated.
- Two source docs disagree on what counts as a "clock" (`clock_registry_v30` vs `descriptor_registry`) — flagged, not silently reconciled.
- `combat_engine_v1` internals and the second battle engine are represented at the system level, not function-by-function.
- Sampling for the runtime numbers (contest-fire frequency, Key counts, battle counts) is 7 seeds × 50 seasons — indicative, not exhaustive.

---

## 8. Provenance

Interactive companion: `wiring_map.html` (this folder). Verified against the working tree on branch `claude/monte-carlo-wiring-question-thpxul`. Primary anchors: `sim/mc_v18.py`, `sim/peninsular/{season,accounting,ci_track,ms_track}.py`, `sim/provincial/{faction_action,massbattle,parliamentary_action,crown_initiative}.py`, `sim/cross_scale/{scene_dispatch,parliamentary_bridge,echo_transport}.py`, `sim/autoload/{game_state,season_manager,victory,dice_engine,sigma_leverage}.py`, `sim/personal/contest/`, `references/module_contracts.yaml`, `references/{descriptor_registry,key_type_registry_v30}.*`, `designs/provincial/clock_registry_v30.md`, `designs/architecture/{player_agency,scale_transitions}_v30.md`, and the `2026-07-14` gameplay-subsystem observatory.

---

## 9. Machine layer — the reusable utility (not just a briefing)

The map is no longer a static one-off. It is now driven by a committed data source + validator, so it doubles as a **Godot-port work-driver** that stays honest as the code moves:

| Piece | What it is |
|---|---|
| **`references/wiring_manifest.yaml`** | The single source of truth: all **27 modules + 7 adapters**, each anchored on a stable registry **tag** (never a file path), carrying a `build` state (runtime wiring: `live / gated / deferred / unwired / stub / design`) and an orthogonal `godot` state (port axis: `gd-ported / typed-exported / python-oracle / no-oracle / retire`) + `port_rank`, `parity`, and a note. Plus the `golden_path` and three `foundation_gaps` that block whole tiers. |
| **`tools/wiring_map_check.py`** | The machine side. `--check` (default) is a **CI-ready gate**: it fails if any tag stops resolving in its live registry (`references/module_contracts.yaml`, `engine/cross_scale/`, the key registry), if coverage isn't 27/27 + 7/7, or if any vocab value is invalid — so a rename or a moved adapter is a *caught error*, not silent drift. `--work-list` emits the ranked port work-list; `--summary` the build/godot counts; `--json` / `--emit-map-json` the machine dumps. |
| **`wiring_map.html`** | The human view. Its godot axis (the **gd** badges + the **◧ Godot port view** panel) is **generated** from the manifest via `--emit-map-json` — the embedded `const PORT` block — so the picture a reader sees is the same data the gate checks. |

**The two axes are deliberately orthogonal.** `build` answers *"is this wired into the running `mc_v18` game?"*; `godot` answers *"what porting artifact exists?"*. This is what surfaces the sharpest fact for the port: **`personal_combat` is `unwired` + `gd-ported`** — the one unit with a GDScript port is *not* on the live Python loop (the combat branch is dead code, §5.4), so its end-to-end parity is unvalidated. The port work-list therefore reads: 1 ported · **16 units have a Python oracle awaiting GDScript** (ranked) · 15 blocked on canon-authoring first (`engine_clock` the T0 blocker) · 2 to retire.

Regenerate the map's data after any manifest edit: `python3 tools/wiring_map_check.py --emit-map-json` → paste into the `const PORT=` block. Run the gate: `python3 tools/wiring_map_check.py --check`.
