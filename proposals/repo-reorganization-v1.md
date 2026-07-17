# Repository Reorganization (v1) — content-class taxonomy + phased migration

## Status: RATIFIED (plan-of-record) — execution pending (ED-IN-0071 · Lane: IN, cross-cutting all lanes · ratified on merge of PR #150, 2026-07-16). The taxonomy + all §5 forks are ratified per ED-1094 (Jordan's merge of #150 + his direct in-conversation rulings 2026-07-15/16). **No files have moved.** The migration (P0–P5, §4) is authorized but not executed; sequencing ruled P0-first. ⚠ **Scope correction (§4):** P0's `canon`→`registers` move is **not** low-blast — it touches ~70 load-bearing hardcoded path references in the enforcement layer, so it is done via a verified path-rewrite pass (§3), never a hand-move.

**Provenance.** Jordan raised, in conversation, reorganizing the repo around its code architecture/schema. A corpus search found it recorded **nowhere** — no ED, proposal, or decision-queue row (only workplan v6 §5 "queue 21–23", tier T2-H3, narrow ledger-path cleanup). It fell through the same continuity gap that (same session) left the workplan board a week stale and mis-filed a workplan-reconciliation under `designs/audit/`. This doc is the register hook.

---

## §1 — Adversarial critique of the current structure

Current top-level: `archives · canon · deprecated · designs · docs · engine · handoffs · params · references · research · sim · skills · tests · tools · versions`.

| # | Current placement | What it actually is | The incoherence |
|---|---|---|---|
| 1 | `archives/` vs `deprecated/` | archives = dead **content**; deprecated = dead **code/machinery** | Leaks: `deprecated/canon/` holds dead ledger content; `archives/audit/` is indistinguishable from `designs/audit/`. Two graveyards, one unenforced rule. |
| 2 | `references/` vs `research/` | references = internal **index layer**; research = external **inbound source material** | `references/` is an overloaded junk drawer (`arcs/`, `historical/`, `engine_params/`, a workplan, `npc_registry.sql`, `effort-guide.md`); `research/historical/` overlaps `research/`. |
| 3 | `params/` | A parallel **numeric-truth layer** | Prose tables, not typed data → can't be ingested, and duplicate numbers already in the design docs (§5 drift risk). Content masquerading as data. |
| 4 | `tests/` at root + `tests/sim` + `tests/sim_framework` vs root `sim/` | `sim/` = real oracle; `tests/sim/` = narrative records; `tests/sim_framework/` = retired harness; only `tests/valoria/` executes | Worst offender: `tests/` is ~5% executable, ~95% historical prose. Naming collision (sim ×3) + category collision. |
| 5 | `designs/godot/` vs `designs/videogame/` | Same subsystem, two folders + a 3rd home (`designs/audit/2026-06-10-godot-conversion-strategy/`) | Pure accretion — three homes for one port. |
| 6 | `workplans/` | The live steering surface | Process/steering nested inside `designs/` as if a design artifact. |
| 7 | `engine/` (2 files) | Sigma-leverage *armature* prose | Vestigial; overlaps `designs/architecture/`; the real "engine" (executable model) is `sim/`. |
| 8 | `designs/arcs/` | Generated **narrative content** | Neither system-mechanics nor world-canon; split from its `references/arc_register*` registers. |
| 9 | audit subfolders **everywhere** (24 in `designs/audit`, +`archives/audit`, `tests/audit`, `skills/*-audit`) | "Audit" is both a place and an activity dumping artifacts wherever the session ran | Findings never promoted-then-archived → the landfill. |
| 10 | editorial/patch **registers** under `canon/` | Object-level world-truth mixed with meta-level process ledgers | The editorial ledger is *about* canon — it isn't canon. Constitution + legislative record in one folder. |

**Through-line:** no distinction between an artifact's *content class* and the *activity that produced it*, and no lifecycle (produce → promote → archive). Folders accrete by "where the session worked," not "what kind of thing this is."

---

## §2 — Target taxonomy (13 primaries)

**✓ RULED** = decided by direct Jordan input 2026-07-15.

| Primary | Contents | Status |
|---|---|---|
| `canon/` | World/design truth ONLY (philosophy, amendments, timeline, constraints). Registers move out. | core |
| `registers/` | All process ledgers (`editorial_ledger*`, patch/supersession registers, `id_reservations`, collision/naming/apparatus/audit registries) **+ handoffs** (RULED) **+ `mechanics_index`** (RULED). Generated registers (`mechanics_index`, `apparatus_registry`, `audit_registry`) carry a **freshness gate** — kept current, not left to rot (§7). | ✓ RULED |
| `systems/` | Design docs by **subsystem**, laid out per §2a; `ui/` lives here. | ✓ RULED axis (§2a) |
| `arcs/` | Narrative content + `references/arc_register*`. | ✓ RULED — own primary |
| `proposals/` | Unratified proposals (from `proposals/`). | ✓ RULED — own primary |
| `research/` | External source material + `research/historical/`. | ✓ RULED — own primary |
| `engine/` | Executable model (Python): `sim/mc_v18.py`, `params/`, typed `engine_params/`, **+ the substrate code `sim/substrate/` + `sim/cross_scale/`** (RULED). | ✓ RULED |
| `godot/` | The Godot port, consolidated (strategy + `skeleton/` + `designs/{godot,videogame}`); **is** the `res://` project (§6). | ✓ RULED — own primary |
| `audits/` | In-flight audits, filed **by category** (audit-type, controlled vocab) + a **subsystem frontmatter tag**; **auto-deprecated after 1 month** → `deprecated/content/audits/<category>/` (RULED §7). | ✓ RULED |
| `workplans/` | Master workplan + progress board. | core |
| `infrastructure/` | `skills/`, `tools/`, CI, hooks, structural-observatory; also `scene_timer`/`audit` telemetry (§7). | core |
| `dashboard/` | Published status site (`dashboard/`). | core |
| `deprecated/` | Everything dead — `archives/` merged, split `content/` vs `code/`. | core |

### §2a — `systems/` is subsystem-organized (RULED, evidence-backed)

The axis was a real fork — **scale** (matches the `sim/` package layout) vs **subsystem** (matches the ID lanes / CURRENT.md / handoffs). Decided **subsystem**, on two grounds:

1. **Isomorphism.** One subsystem = one folder = one ID lane = one CURRENT.md row = one `HANDOFF_<LANE>.md` = one Godot module tree (§6). This aligns all five indices that today agree with each other but not with the folder tree.
2. **The co-location cost is measured and small.** Co-locating each subsystem's `sim/` beside its design `.md` requires splitting the scale-packaged `sim/`. From the vector-audit import graph (`g_code.json`, §6): of 178 `sim.*→sim.*` edges, **104 stay intra-subsystem, 60 point at shared homes (`engine`), and only 14 become cross-folder** — all real, already-existing couplings. 14 explicit import rewrites, not a shatter.

Layout — design `.md` at each subsystem's root, a `sim/` subfolder for its scripts:

```
systems/
  combat/            { *.md ; sim/ ← sim/personal/combat.py }
  social_contest/    { *.md ; sim/ ← sim/personal/contest/ + parliamentary_vote/stay }
  factions/          { *.md ; sim/ ← sim/provincial/ (faction+domain actions) }
  fieldwork/         { *.md ; sim/ ← sim/personal/{fieldwork,investigation,knots} }
  mass_battle/       { *.md ; sim/ }
  settlements/       { *.md ; sim/ ← sim/territory/ }
                     #   + the PER-TERRITORY "Piety Track" (territorial_piety, the settlement
                     #     Church-Influence stat) lands here — renamed piety_track (ED-644),
                     #     distinct from character conviction below
  character/         # RULED: umbrella for character-sheet systems; generation is a subfolder
    generation/      { *.md ; sim/ }                    # chargen questionnaire / roster
    conviction/      { *.md ; sim/ ← sim/personal/conviction + piety_track }
                     #   the CHARACTER "piety_track" module (registry system IS conviction_track,
                     #   home conviction_track_v1.md) is renamed and folded in here as the piousness
                     #   axis of conviction (RULED) — breaks the 3-way "Piety Track" name collision
    beliefs/         { *.md ; sim/ ← sim/personal/beliefs }
    companion/       { *.md ; sim/ ← sim/personal/companion }
  threadwork/        { *.md ; sim/ ← sim/thread/ }
  world/             { *.md ; sim/ ← sim/world/ + sim/peninsular/ tracks }
  npcs/              { *.md ; sim/ }
  articulation/      { *.md ; sim/ }
  ui/                { *.md ; sim/ (starts empty — not Key-emitting, §7) }
  _architecture/     # substrate DESIGN DOCS: Key substrate, propagation_spec, holonic_doctrine,
                     # scale_transitions, player_agency, clock_registry, narrative_engine.
                     # Its executable substrate (sim/substrate, sim/cross_scale) lives in engine/ (RULED).
```

Names normalized to **singular** to match the ID lanes. Scale becomes a frontmatter tag, not a folder level. `character/` is the one subsystem with internal subfolders (it bundles several distinct character-sheet mechanics); the rest stay flat.

---

## §3 — Migration risk (why this is not `git mv`)

Paths/names are load-bearing (~16k citations, `canonical_sha__*` pins, co-file pairs). A move breaks: `canonical_sources.yaml` pins + `module_contracts.yaml` `doc:` paths; `workplan_status.py` `RELEVANT_PREFIXES`, `audit_staleness.py` `artifact_paths`, `dashboard.yml`/`audit-refresh.yml` filters, `.githooks/`; `audit_registry.jsonl`/`apparatus_registry.yaml` path fields; thousands of in-doc citations + co-file pairs; and the sim import graph (the 14 cross-folder edges from §2a, rewritten in lockstep). So: **tooling, not moves** — a path-rewrite pass + alias map, a citation-rewrite pass, an import-rewrite pass, a CI-path update, a co-file re-check — CI green at every step. The §6 vector-audit artifacts are the inputs.

---

## §4 — Phased plan (RULED sequence: cheapest / highest-value first)

Each phase independently mergeable, CI green throughout.

1. **P0 — Registers out of `canon/`** → `registers/` (+ handoffs + `mechanics_index`). ⚠ **Scope corrected 2026-07-16:** *not* low-blast. The register paths are hardcoded in ~**70 load-bearing sites** across the enforcement layer (`obs_core`'s `(repo/"canon").glob(...)`, `ci_register_size_check`'s ~15-key size dict, `validate_ed_citations`, `broken_dependency_checker`'s `LANE_LEDGER_PATHS`, `audit_staleness` `artifact_paths`, `canonical_sources` pins, + ~15 more tools/skills). Doc citations are ID-based and safe; the tool path-refs are not. Execute via a **built + verified path-rewrite pass** (the actual proof-of-tooling) scoped to live files (excluding archives/deprecated/audit records, which are historical), regenerating generated outputs, + the generated-register **freshness gate** (fork 3). Iterate to green locally before push. ✓ **EXECUTED 2026-07-16 (this PR):** the 16 `canon/` register files → `registers/`; 234 refs rewritten across 77 live files + 8 dir-construction opens + 3 test-fixture fixes + the `gen_audit` classifier; `restructure_ledger.md` alias map added; obs/apparatus outputs regenerated; integrity gate + `valoria_local` + 294 pytest all green. **Deferred to P0b:** the `handoffs/` → `registers/` move and the generated-register freshness gate (separate blast radii). ✓ **P0b part 1 EXECUTED 2026-07-16 (separate PR):** `handoffs/` → `registers/handoffs/` (10 lane files; root `HANDOFF.md` index stays at repo root so the SessionStart banner is unaffected); 84 refs across 23 files via a path-boundary regex that protects `deprecated/session_machinery/handoffs/`; `workplan_status.RELEVANT_PREFIXES` + `gen_audit._HISTORICAL_PATH_PREFIXES` retargeted; alias rows + obs regen; CLAUDE.md §1/§3 updated. **Still deferred:** the generated-register freshness gate (fork 3) — net-new CI tooling, its own follow-up.
2. **P1 — Promote easy primaries**: `workplans/`, `proposals/`, `arcs/`, `dashboard/`, `research/` (+`research/historical`), `infrastructure/` (`skills`+`tools`). ✓ **EXECUTED 2026-07-16:** `proposals/` + `research/`/`dashboard/`/`workplans/` landed in PR #153. **`arcs/` landed separately (this PR)** — the largest slice, held for its own PR: `designs/arcs/` → `arcs/` (narrative content + `gm_ref/`) and the 7 arc registers (`references/arc_register{,_infill}.md` + `references/arcs/*`) → `arcs/registers/` (46 files moved); 31 live refs across 16 files; `ci_editorial_checker` + `ci_register_size_check` functional path/key edges verified against the real moved files; append-only ledgers + frozen reports excluded (alias-resolved); `restructure_ledger.md` rows + obs regen. This PR also **repairs a fork #5 regression** the P2 blanket-rewrite introduced (the `designs/godot` vs `designs/videogame` critique text was collapsed to `godot/ vs godot/`) and hardens the migration convention: the proposal's own critique text (before-state) is excluded from blanket path-rewrites. `infrastructure/` (`skills`+`tools`) still pending. 
3. **P2 — Collapse Godot's three homes** → the `godot/` primary; sigma-leverage armature → `systems/_architecture/`; shells → `deprecated/`. ✓ **EXECUTED 2026-07-16 (this PR):** the three homes (`designs/godot/`, `designs/videogame/`, `designs/audit/2026-06-10-godot-conversion-strategy/`) → top-level `godot/` (27 files moved); 29 live refs rewritten across 18 files (append-only ledgers + frozen report snapshots excluded — they alias); `build_decisions.py` `SWEEP_DIRS` + GO lane-map fixed; obs outputs regenerated (decisions/proposals/graph/lexicon; net delta = 19 godot path-relabels, no content loss); `restructure_ledger.md` alias rows (27 files + 3 dir prefixes) added; CLAUDE.md §3/§6 + `godot/README.md` updated. **Deferred (correctly, to later phases):** the `sigma-leverage armature → systems/_architecture/` and `shells → deprecated/` sub-clauses depend on `systems/`/`engine/` existing (P3/P4) and are NOT part of this slice.
4. **P3 — `engine/` assembly**: `sim/mc_v18.py` + `params/` + `engine_params/` + `sim/substrate/` + `sim/cross_scale/`; rewrite `mc_v18` imports in lockstep with P4. ✓ **P3 seed EXECUTED 2026-07-16 (separate PR):** `references/engine_params/` → `engine/engine_params/` (the typed Class-C export; 14 refs across 12 files; `export_engine_params.py` `OUT_PATH` dir-join edge + the round-trip CI gate verified against the new path). ✓ **`params/` EXECUTED 2026-07-16 (separate PR, "go big + use pointers"):** `params/` (43 files) → `engine/params/`. `params/` is DATA (markdown tables, not imported) → **zero sim-oracle/import risk**; the care was the functional surface. Per the pointer directive, only the **machine-read functional layer** was rewritten (253 refs across 38 `tools/`+`references/*.yaml`+`registers/*.yaml` files — incl. `ci_co_file_checker` path-construction, `build_decisions` lane-map, `patch_propagation_checker` regex, `atomization_rules`/`lane_assignments` path-matches, `sim_harness` reads, and the 16 `canonical_sha` pins which migrated same-SHA since params content stayed byte-identical); **prose provenance** (sim comments, design-doc mentions, append-only ledgers, and the tables' own internal cross-refs) was **left to the `restructure_ledger.md` alias pointer**. ✓ **Phase A EXECUTED 2026-07-16 (the oracle-risky piece, done carefully):** the sim engine **core** — `sim/{substrate,autoload,cross_scale}` + `sim/mc_v18.py` → `engine/` (making `engine/` a Python package). The split is **acyclic** (autoload is a leaf; mc_v18/cross_scale → per-subsystem one-way; per-subsystem → autoload one-way), so no import cycles. 49 files' `sim.{core}` imports rewritten to `engine.{core}` (per-subsystem `sim.personal` etc. left as `sim.`, staying for P4). **The sim regression caught two real issues, both fixed:** (1) the top-level `engine` package collided with the parity test's ground-up reference `engine.py` (cached in `sys.modules`) → loaded it by explicit path via importlib; (2) rewriting a frozen `tests/sim/` file tripped the co-file + sim-fabrication gates → reverted it (frozen files → alias, not rewrite). **Verified:** live mc_v18 campaign runs; `sim/tests` **419 passed / 0 failed**; `tests/valoria`+`tests/contracts` **335 passed**; all gates green. **Still pending:** P4 — `designs/`→`systems/` by subsystem + distributing the per-subsystem `sim/` packages into `systems/<subsystem>/sim/` (they already depend upward on `engine.*`, so this is now a mechanical rehome).
5. **P4 — `systems/` by subsystem + intra-system sim** (§2a): rehome `designs/*` → `systems/*` (incl. the `character/` nesting and the piety split); distribute `sim/` subpackages; apply the 14 cross-folder import rewrites. Full citation + import tooling. Do last.
6. **P5 — `tests/` disentangle + `audits/` lifecycle + `archives/`→`deprecated/`** (#1, #4, #9). Keep `tests/valoria/`; relocate narrative prose. Stand up the `audits/` **by-category filing + 1-month auto-deprecation** (fork 5): a CI/tooling gate that (a) requires each audit under a controlled category folder + a subsystem frontmatter tag, (b) **rejects a folder with no assignable audit category as not-an-audit** (routes it to `research/`/`proposals/`/`systems/`), (c) moves any audit >1 month old to `deprecated/content/audits/<category>/`, (d) fails a `*workplan*`/reconciliation artifact misfiled under `audits/`. ✓ **Fork #1 (`archives/`→`deprecated/`) EXECUTED 2026-07-16 (separate PR):** the two graveyards merged — `archives/` (199 files) → `deprecated/archives/`, so `deprecated/` now holds dead **content** (`deprecated/archives/`) beside dead **code** (`deprecated/{tools,skills,engine,…}`). 66 refs across 30 files via a path-boundary regex; the two functional edges (`validate_ed_citations` `ARCHIVE_GLOBS`, `ci_register_size` cap key) verified retargeted; general historical-prefix lists become redundant-but-correct (`deprecated/` already covers the moved content). **Still pending:** the `tests/` disentangle and the `audits/` by-category lifecycle gate.

---

## §5 — Forks: all RULED (2026-07-15, direct Jordan input)

Round 1 (axis + primaries): subsystem axis (§2a, evidence-backed); `arcs`/`proposals`/`research`/`godot` each own primary; `ui` under `systems`, mapped at Godot conversion (§6); `params`+`mc_v18` → `engine`; per-scale sim → `systems/<subsystem>/sim/`; npcs/articulation own folders; singular names; `_architecture/` substrate tier.

Round 2 (the six held-back):
1. **Cross-scale sim** (`sim/substrate`, `sim/cross_scale`) → **`engine/`** (with mc_v18/params). `_architecture/` keeps the substrate *docs* only.
2. **Handoffs** → **`registers/`** (with the ledgers).
3. **`mechanics_index`** → **`registers/`**, and it (with the other generated registers) **must be kept fresh** — a freshness gate lands in P0.
4. **`piety_track`** (character) → **renamed `conviction`** (RULED: "call it conviction or piousness") and folded into **`systems/character/conviction/`** as its piousness axis — it already *is* the conviction_track system (registry `conviction_track`, home `conviction_track_v1.md`). The **per-territory Piety Track** (`territorial_piety`, mis-named `conviction_track_v30.md`) → **`systems/settlements/`**, renamed `piety_track` (executes the deferred **ED-644** rename). The two renames + folder split fully resolve the "Piety Track"/"conviction" cross-wiring `module_contracts.yaml` flags OPEN. ("piousness" is the alternative name if the character religious-devotion track should stay distinct from the broader conviction taxonomy — defaulting to conviction.)
5. **`audits/` lifecycle** → **filed by category**, **auto-deprecated after 1 month**. Enforced by a P5 CI/tooling gate.
6. **Sequencing** → **P0→P5 as written** (Jordan: "whatever makes most sense").

**Audits category axis — RULED by category (audit-type), 2026-07-15.** An adversarial pass confirmed it over by-subsystem: most audits are cross-cutting (governance / multi-agent / observatory / vector span many subsystems), so by-subsystem would pile the majority into an `_cross/` mini-landfill; category is the audit's stable identity and matches the audit skills. Refinements adopted: (a) a **controlled category vocabulary** (the audit skills — vector / mechanic / canon-guard / resolution-diagnostic / module-adjudicator — plus a short recurring set; one `thematic/` bucket for genuine one-offs — not free-text); (b) a **subsystem frontmatter tag** so "audits touching combat" is a metadata query, not a folder (category = folder, subsystem = tag, mirroring scale-as-tag); (c) a **not-an-audit gate** — a folder with no assignable audit category is not an audit and routes to `research/` / `proposals/` / `systems/` (directly attacks the #9 landfill). The 1-month TTL keeps live `audits/` small, so the category grouping mainly organizes the `deprecated/` archive (same path carried through).

---

## §6 — Migration data sources + Godot conversion map

**Repo-shape inputs (reuse, don't re-derive).** The 2026-07-14 `valoria-vector-audit` / observatory runs left the machine-readable shape under `designs/audit/2026-07-14-{governance-vector-audit,gameplay-subsystem-observatory}/`:

| Artifact | Drives |
|---|---|
| `data/g_code.json` (import graph) | The sim-split / import-rewrite (the §2a 14-edge measurement) |
| `data/g_cite.json` + `degrees.json` | Boundary placement + hub/substrate identification |
| `vector_audit/data/corpus_manifest.json` | The migration work-list (every file → target home) |
| `data/tokens.json` | Sequencing (biggest movers) |
| `graphs/module_flowchart.mermaid`, `structure/data/g_pointer.json` | Post-move stat-vocabulary resolution check |

**Godot conversion is a *map*, not a mirror.** Godot separates headless logic / presentation / singletons / typed data; the repo organizes by subsystem. The `ui`-under-`systems` fork (RULED) resolves at conversion:

| Repo | → Godot `res://` |
|---|---|
| `systems/<sub>/*.md` | design source — not shipped |
| `systems/<sub>/sim/` (Python oracle) | `res://engine/modules/<sub>/` — GDScript `EngineModule` per module (1:1 oracle→port, ED-1050) |
| `systems/_architecture/` + `engine/`'s substrate code | `res://autoloads/` — `KeyBus`, `GameState`, `Resolver`, `EngineClock` singletons |
| `systems/ui/` | `res://scenes/` + `res://ui/` |
| `engine/engine_params/` | `res://resources/*.tres` — the `combat_engine_v1.json` pattern → Godot Resources |
| `engine/` (mc_v18, params) | not shipped — Python-side oracle/balance; typed exports are the bridge |
| `godot/` (primary) | **is** the `res://` project root + strategy doc + skeleton |

**Payoff:** `godot/engine/modules/<subsystem>/` becomes a folder-for-folder mirror of `systems/<subsystem>/sim/`; the oracle-parity check is a per-folder diff. Second independent argument for the subsystem axis.

---

## §7 — Module-census notes (from `module_contracts.yaml`, 27 modules)

- `ui` and `character/generation` map to **zero** engine modules (not Key-emitting) — their `sim/` starts empty. Legitimate; named so it isn't mistaken for an error.
- **`piety_track` is dual** (RULED §5.4): the personal module (doc `conviction_track_v1.md`, registry system `conviction_track`) is renamed **conviction** and folds into `systems/character/conviction/` as its piousness axis; the per-territory "Piety Track" (`territorial_piety`, mis-named `conviction_track_v30.md`) is renamed **piety_track** under `systems/settlements/` (executes ED-644). The renames + folder split resolve the OPEN 3-way "Piety Track"/"conviction" collision `module_contracts.yaml` flags.
- `scene_timer` and `audit` are **telemetry, not gameplay** → `infrastructure/`, not `systems/_architecture/`.
- `campaign_architecture` is a stub already dissolved into 4 folders → **no folder**.
- `settlement_economy` flagged **RECOMMEND RETIRE** (phantom — no doc/state/logic).
- Data bug to fix in passing: `mass_battle.scales = [scene]` (should be provincial).
- Coupling note: `faction_state` (13 producers) and `npc_behavior` (11) are terminal accounting **sinks** — every axis leaves them importing widely. The tree is optimized for navigation + lane isomorphism, not edge-minimization (unwinnable).
