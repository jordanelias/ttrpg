# Census (REST) 3 — text corrections: stale pointers, false registry notes, a header that claims a check that does not exist, and the census script's own defects

## Status: PROPOSED

Author: Fable census lane, PART=REST. Source: `audits/17_CENSUS_REST.md` §3, §4, §5, §10. Read at
`4995824` (working tree). Every item is a text edit; none moves a hash or a verdict of a gate.

## What it changes in `engine/season/` at runtime

**Nothing.** `hole_register.yaml`'s `site:` and `owner:` are read for non-emptiness only
(`harness/register.py:215`); `module_contracts.yaml`'s `modules:` notes and `wiring.build` are read by
`tools/export_composition.py` for vocabulary membership only; `write_matrix.yaml`'s header is comment.
The reason to make the edits is the next reader: a pointer that names the wrong file sends a session to
code that is not the owner (CLAUDE.md §0.1 pt 3, "open `F` at `:L`").

## A. `engine/season/hole_register.yaml` — 26 pointers, exact substrings

One cause covers fifteen of them: `loop/effects.py` was split into
`loop/effects_{army,combat,economy,founding,governance,information,migration,shared}.py`; `effects.py`
now holds the registry import and three re-exports (`_renewals`, `_oblige_term`, `_eff_kill`).

| row · field | old substring | new substring |
|---|---|---|
| H-72 · site | `` `queries/readers.py` — `LedgerReader` `` | `` `queries/person_q.py` — `LedgerReader` `` |
| H-138 · owner | ``loop/effects.py -- `_eff_transfer` `` | ``loop/effects_economy.py -- `_eff_transfer` `` |
| H-138 · owner | `` `tests/test_season_shape.py:8103-8112`'s `norm` helper `` | `` `tests/test_season_shape.py`'s `norm` helper (two definitions, in the tests of the semantically-empty mutation) `` — a line range in a 16,000-line file is stale the day after it is written; the two sites today are `:11363` and `:11445` |
| H-148 · site | `` `loop/effects.py::_eff_march` `` | `` `loop/effects_combat.py::_eff_march` `` |
| H-152 · owner | `` `loop/effects.py::_eff_march` `` | `` `loop/effects_combat.py::_eff_march` `` |
| H-152 · site | ``engine/season/loop/effects.py -- `_eff_march` `` | ``engine/season/loop/effects_combat.py -- `_eff_march` `` |
| H-155 · site | ``(`isinstance(held.value, (int, float))`, `witness.py:189`)`` | ``(`isinstance(held.value, (int, float))`, in `loop/witness.py::_told_value`)`` (today `:220`) |
| H-207 · owner | `` `decision/options.py::aggregate_questions` `` | `` `decision/questions.py::aggregate_questions` `` |
| H-210 · owner | ``(`workplans/valoria_master_workplan_v9_part6.md`, B-P)`` | ``(the v9 plan's part 6, B-P; retired, `FORK:c1374059`)`` |
| H-230 · owner | ``(`workplans/valoria_master_workplan_v9_part5.md` IN-61:`` | ``(the v9 plan's part 5, retired, `FORK:c1374059`, IN-61:`` |
| H-238 · owner | `` `workplans/valoria_master_workplan_v9.md` §0.5 (RULED 2026-10-13, *Relax exit rules*)`` | `` `workplans/valoria_master_workplan_v11.md` P9 (RULED 2026-10-13, *Relax exit rules*; first written as the v9 head's §0.5, `FORK:c1374059`)`` |
| H-140 · owner | ``loop/effects.py -- `_eff_move` `` | ``loop/effects_migration.py -- `_eff_move` `` |
| H-156 · owner | ``loop/effects.py -- `_eff_commit` `` | ``loop/effects_information.py -- `_eff_commit` `` |
| H-43 · default | `` `loop/effects.py::_eff_petition` / `_eff_issue` `` | `` `loop/effects_information.py::_eff_petition` / `_eff_issue` `` |
| H-105 · hole | `` `loop/effects.py::_rise` `` | `` `loop/effects_economy.py::_rise` `` |
| H-164 · hole | `` `loop/effects.py::_rise` `` | `` `loop/effects_economy.py::_rise` `` |
| H-164 · owner | ``loop/effects.py -- `_rise` `` | ``loop/effects_economy.py -- `_rise` `` |
| H-158 · site | `` `loop/effects.py::_renewals` `` | `` `loop/effects_economy.py::_renewals` `` |
| H-174 · owner | `loop/effects.py::_renewals` | `loop/effects_economy.py::_renewals` |
| H-159 · site | `` `loop/effects.py::_oblige_term` `` | `` `loop/effects_shared.py::_oblige_term` `` |
| H-126 · site | `seam/wrappers/sigma.py::faculty` | `seam/wrappers/pool.py::faculty` |
| H-245, H-246, H-247 · site | `` `seam/wrappers/sigma.py::faculty` `` | `` `seam/wrappers/pool.py::faculty` `` |
| H-245 · owner | `` `seam/wrappers/sigma.py::register_pool_addend` `` | `` `seam/wrappers/pool.py::register_pool_addend` `` |
| H-172 · owner | `decision/options.py::belief_contradicts` | `epistemic.py::belief_contradicts` |
| H-174 · owner | `queries/world_q.py::home_of` | `state/containment.py::home_of` |

Not edited, with the reason (so the next census does not re-raise them): H-220 (`harness/probes.py::Ev`
exists, `:326`); H-224 (`decision/choose.py::unrest_pull`: the row itself says the function was built
and reverted); H-357, H-358, H-361 ×3 (all exist; the census opened a stale worktree copy); H-79
(`SeasonDriver.witness` is `witness.witness` bound onto the class, `loop/driver.py:574-585`); H-213
(`_obstacle_of`: the row says it was deleted at that step); H-153, H-222 (`19_PLAN.md` resolves uniquely
to `proposals/2026-09-05-proceedings-subsystem/19_PLAN.md`).

**Check after the edit:** `python -m engine.season.harness.register --check` and `--verify-citations`
unchanged; `python scratchpad/census_rest/c5.py` (the corrected resolver; 837 pointers) reports the
eight "Not edited" pointers and nothing else. That script is a one-off and is not to be kept (§0.1 pt 5).

## B. `references/module_contracts.yaml` — two rows a port decision would read

**C-1 · `combat` (`:886-940`).** `wiring.build: unwired` (`:936`) and the note (`:940`) say the combat
engine is reached by nothing: "No trigger anywhere produces a combat scene", citing
`DISPATCH_COMBAT_BRIDGE`, `scene_slate.queue_scene`, `combat_bridge.py:37`, `scene_dispatch.py:37`. None
of those exists. The same file's `composition_roles: combat.fight` (`:58-62`) registers
`modules.combat.fight:fight` as a `verb_call` entry for `fight`, and `fight` executed 13 times in the
corpus run at seed 0 (`corpus_run`'s DEGREES RESOLVED BY VERB: `fight 13 {'Declared': 5, 'Felled': 8}`).

- `build: unwired` → `build: gated`. (`gated` is the vocabulary's word for "runs only under a
  condition": in the three-season realm run at seed 0 no person formed `fight`, and the corpus reaches
  it.)
- Replace the note with: `'built and typed-exported; reached from the season loop through
  composition role combat.fight (engine/season/seam/wrappers/combat.py). BUILD gated: a fight needs a
  challenge accepted or a violence context; the realm at seed 0 forms none in three seasons, the corpus
  executes it. The pre-season campaign driver this note used to describe was deleted at plan position
  28-iii.'`
- `parity:` is `11_GO_pointer_and_stale_text_resolutions.md` row 8's edit, not repeated here.

**C-2 · `mass_battle` (`:488-511`).** The comment at `:492` ("`sim_module:` deliberately absent until
the MB lane adds it") and a note (`:511`) whose body names `systems/mass_battle/sim/massbattle.py` as
the live tree and `faction_action.py:431` as its caller, followed by three bracketed `[SUPERSEDED …]`
corrections.

- Add `sim_module: modules/mass_battle/` (the directory `composition_roles: mass_battle.resolve_field`
  targets, `:64-68`); delete the `:492` comment.
- Replace the note with its last bracket, restated: `'modules/mass_battle/ is the reachable closure
  (moved from systems/mass_battle/sim/ at plan position 31c, which keeps the harnesses and workbench);
  the one caller is engine/season/seam/wrappers/mass_battle.py through resolve_field. BUILD gated:
  the provider runs when ENCOUNTER admits a march at a held target (H-149).'`
- The sentence "none of the realm marches do" is dropped: at this tree, seed 0, three seasons, the realm
  log holds `field.lost` ×1 and `field.unopposed` ×3 (`aperture 3 0`, EMITTED KINDS)
  `[UNVERIFIED: that the `field.lost` Event came through `resolve_field` and not a headcount short-cut;
  the kind is the march contest's degree either way]`.

**Check:** `python tools/export_composition.py --check` → `OK`; `gated` is a member of
`wiring_vocabularies.build_states`.

## C. `engine/season/write_matrix.yaml` — the header (C-3)

The file the gate reads at runtime opens with two statements about code that does not exist.

| line | old | new |
|---|---|---|
| `:3-4` | "`engine/season/shape.py`'s `write()` gate reads it" | "`engine/season/state/world.py::World.write` reads it through `data/matrix.py`" |
| `:28-31` | "The 28 rows carried over are extracted mechanically from §D3's markdown table; `python engine/season/register.py --verify-write-matrix` re-extracts and fails on drift." | "The 28 rows carried over were extracted from §D3's markdown table once. This file is now the head (CLAUDE.md §0.05: prose is reference); nothing re-extracts it, and a difference from §D3 is decided here and recorded in the row." |

`harness/register.py` has five flags (`--check`, `--counts`, `--verify-citations`, `--rule`,
`--requirements`); `--verify-write-matrix` occurs nowhere in the tree but this comment. The correction
removes a claimed safeguard rather than building it: a check that re-derives a code-read registry from a
design document would make the document the head, which §0.05 clause 1 forbids.

## D. Two sentences in other suite documents (C-5, C-6, and one unverified mark resolved)

- **C-5 · `11_GO_player_surface_contract.md` §4.** "The row's `emits:` gains `scar.taken` /
  `conviction.folded`". `write_matrix.yaml` already declares `scar.taken` on `(Person, scar)` and
  `conviction.moved` on `(Person, conviction)`. The edit is at the writers: `loop/resolve.py::_scar_witnesses`
  and `_conviction_crisis` pass `emits=` on the write they already make. Proposed wording: "The rows
  already declare `scar.taken` and `conviction.moved`; the two writers pass them. If the crisis needs a
  kind of its own (`conviction.folded`), that one is the row's only addition." Measured for scale: 883
  `(Person, scar)` writes and 2 `(Person, conviction)` writes in three seasons at seed 0, 0 Events of
  either kind; the scar Event should land after `02_CHAR_scar_cap_and_regard_unit.md`'s cap.
- **C-6 · for the WR lane (`09_WR_story_instruments_that_can_fail.md`), a reading, not an edit.**
  `rosters.yaml: strife_kinds` names `tenure.opened` (in `joins` and `concludes`) and `stance.moved` (in
  `never`). In the Event log those kinds are emitted by one verb each (`confer`; `forgive`), 0 times in
  the run, while `(Tenure, since)` was written 178 times and `(Person, stance)` once under other acts'
  kinds. A reader of the roster who takes `tenure.opened` to mean "an edge opened" is reading
  conferrals only. Eight of the nine `opens` kinds did not occur in the same run.
- **`12_ARCS_adjudication.md` row 19**, "`rosters.yaml: knowledge_kinds` is the owner and the gate
  applies to the kinds it names `[UNVERIFIED: roster not opened at the row]`". Opened: the roster names
  two kinds and nothing reads it. The row's answer ("ordinary") stands; its support becomes
  `17_CENSUS_REST_2_wiring.md` W3.

## E. The census script, for whoever reruns it (`scratchpad/census.py`; not a tracked file)

1. **C5 resolved pointers against the wrong tree.** `census.py:170` falls back to
   `ROOT.rglob(basename)[:1]` when `ROOT / p` is missing. The register writes paths relative to
   `engine/season/`, so nearly every pointer took the fallback, and the first match was a file in the
   locked worktree `.claude/worktrees/agent-a737f996de1fa4752` (commit `1424aa7`) or a same-named file
   elsewhere. Seven of its sixteen rows are artefacts of that; seventeen real stale pointers were not
   reported. Fix: try `engine/season/<p>` before any fallback and never search `.claude/`.
2. **C4 matched nothing.** `census.py:142`'s `emits:\s*["']?([\w.]+)` cannot enter a YAML list
   (`emits: ["petition.carried"]`), and effects do not name kinds in an `emits = "…"` assignment. Use
   `engine.season.data.verbs.EVENT_KINDS` for the emitted set and an Event log for what occurs.
3. **C2 counts only `.field =` as a store.** A positional or keyword constructor argument, `+=`, item
   assignment and `getattr(self, f"…")` are all writes or reads it cannot see: 25 of 72 rows.
4. **The stale worktree itself.** `.claude/worktrees/agent-a737f996de1fa4752` is a locked checkout of an
   older commit inside the repository directory. Any tool that walks the tree with `os.walk`,
   `Path.rglob` or `git ls-files`-independent globbing reads a second, older copy of the game. C1's
   roots do not include it; a future script might. Removing it is the orchestrator's call
   (`git worktree remove`), not a census edit.

## NERS reading

Not a design object; no NERS cut applies. The test that does: *does this document create work for a
future session?* (CLAUDE.md §0). Sections A–D are edits to artifacts that exist and explain a judgment
about each; section E dies with the scratch script.

## Cost class

Edit. One commit, `[cleanup]`, running `engine/season/tests/test_season_shape.py` for the register's
schema and `tools/export_composition.py --check` for the contracts.
