# module_contracts — history

Companion to `references/module_contracts.yaml`. **That file is the CONTRACT SET; this one is HISTORY.**

## Why the split (B-X, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement."* The precedent is `references/id_reservations_history.md`. What moved
here is the **comment** narrative of the contract file: the v1-v4 build notes, the retired-at-plan-position
write-ups, the `OI-54` per-row `sim_module:` provenance, the repeated `doc:` rationale, and the long
inline derivations on `state:` rows.

**Nothing was deleted.** Every block below is the comment text that used to sit in the YAML, moved
verbatim; each block names the module row (or section) it came from and the line it was on before the
move. Where a reader still needs the fact to use the row correctly today, the YAML keeps a one-line
summary in its place; that summary is a rewrite, and the verbatim original is here.

**What stayed in the YAML, deliberately:** the schema and the DISCIPLINE block (instructions to editors),
the composition-role and `entry:` field definitions, every data value (including the `gap_notes`,
`sources` and `wiring.note` text and `foundation_gaps`, which are data a contract reader sees and
which no code reads by key), the `wiring_vocabularies` definitions, and the short field-level comments
that define a value (`[ASSUMPTION]`, `[verification ...]`, `prose display-names`).

**What reads this file:** every loader found by grep over `tests/`, `tools/`, `engine/`, `skills/` and
`.claude/` uses a YAML loader, which discards comments, so the move is invisible to them. The one
reader of the raw text is `tests/valoria/test_flow_skeletons.py` (`leaf in _read(target)`), which
requires a symbol cited by a frozen skeleton to occur anywhere in the file: that is why the retired
role names (`parliamentary_vote`, `territory_transfer_proposal`, ...) stay in a retained comment under
`composition_roles:`. `tools/export_composition.py --check` is the blocking round-trip over
`composition_roles:` and the `wiring:` vocabularies.

**Adding here, not there.** New narrative about a contract row belongs in this file or in the ED chain;
the YAML comment stays one line.

---

## File head

*Full-line comment, was at lines 22-30.*

```text
#
# v2 (2026-06-10) — Stage-1 extraction pass: registry emitting/consuming_systems
# matrix parsed wholesale (38 typed entries, 29 named systems); 5 of 7 v1 stubs
# extracted; political_dynamics CONSOLIDATED into npc_behavior (doc-12 = PP-687
# npc-procedure Keys migration); 10 registry-named systems added as new modules;
# personal_combat deferred (canonical-candidate, handoff-owned); campaign_architecture
# reclassified (consolidation doc, retirement recommended).
# v1 seeded 2026-06-09/10 from key_substrate_v30 §8 / key_type_registry_v30 /
# scale_transitions_v30 / derived_stats_v30 (commit cdbd1b50).
```

*Full-line comment, was at lines 32-44.*

```text
# v3 (2026-06-10) — gates + per-system calculations folded into the contract so the
# enforcer checks them (A10 gates / A11 derivations / A12 sequence). Migrated verbatim
# from the cited contract_flowchart.py literals; the flowchart now READS these from here
# (single source of truth). settlement_layer Mandate↔L/PS loop annotated with its §1.8
# canon damper. schema_version 1 -> 2.
# v2 (2026-06-10) — Stage-1 extraction pass: registry emitting/consuming_systems
# matrix parsed wholesale (38 typed entries, 29 named systems); 5 of 7 v1 stubs
# extracted; political_dynamics CONSOLIDATED into npc_behavior (doc-12 = PP-687
# npc-procedure Keys migration); 10 registry-named systems added as new modules;
# personal_combat deferred (canonical-candidate, handoff-owned); campaign_architecture
# reclassified (consolidation doc, retirement recommended).
# v1 seeded 2026-06-09/10 from key_substrate_v30 §8 / key_type_registry_v30 /
# scale_transitions_v30 / derived_stats_v30 (commit cdbd1b50).
```

*Inline comment on `status: EXTRACTED_STAGE1`, was at line 48.*

```text
# campaign_architecture stub remains; personal_combat EXTRACTED 2026-06-23 (v4, below)
```

*Full-line comment, was at lines 50-55.*

```text
# v4 (2026-06-23) — personal_combat EXTRACTED (deferral resolved: combat_engine_v1 ratified CANONICAL
# by ED-900/904 + docket ED-1029; the stale README 'canonical-candidate' line that gated the trigger is
# corrected). Shaped as CombatEngine (BaseEngine, d_sigma) hosting the 11-action module set; combat.strike
# + combat.wound ported to the Godot skeleton (slice). F3 resolved (scene.combat_* outcome Key family).
# Model corrected off the v30 placeholder (Agi×2/TN-7/mult-STR) to the canonical sigma engine + ED-1041
# bilateral-Ob wounds. See the personal_combat entry below + the 2026-06-22 personal-combat audit.
```

## composition_roles

*Full-line comment, was at lines 58-63.*

```text
# WHY THIS IS HERE AND NOT IN engine/. The premise this repo works from is that `systems/` stems
# from `engine/` and `references/`. Until 2026-08-20 the campaign driver `engine/mc_v18.py` named
# its subsystems directly (`from systems.factions.sim.faction_action import faction_take_action`),
# which inverts that: the root named its own dependents, and the package graph acquired a cycle.
#
# These rows move the naming to where the premise says it belongs — a registry under `references/`.
```

*Full-line comment, was at lines 71-102.*

```text
  # ── RETIRED AT PLAN POSITION `28-iii` (SPINE-DELETE, 2026-10-01) ─────────────────────────────────
  # Seventeen rows went with the callers that were their only readers, deleted the same commit:
  #   `faction_action`, `season_driver` -- `engine/mc_v18.py`;  `accounting` -- `engine/autoload/engine_clock.py`;
  #   `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a`, `contest_side.b` --
  #   `engine/cross_scale/scene_dispatch.py`;  the ten `snapshot_state.*` rows -- `game_state.py::restore_world`.
  # The deleted files are retrievable through their `references/restructure_ledger.md` rows (ref `5c5d8ec6`).
  #
  # THE "KEPT NAMED" RULING FOR THE THREE ORPHANS EXPIRES HERE, AND ITS EXPIRY IS RECORDED RATHER THAN
  # SILENT. `rs_track_delta`, `territory_transfer_candidate` and `territory_transfer_proposal` were kept
  # after 2026-09-16 (ED-IN-0232) on the argument that an orphaned role is more useful named than deleted:
  # the target resolves, the exporter imports it, and deleting would hide an orphaned mechanic behind a tidy
  # registry. `architecture/meta/01_AXIOMS.md` `ID-13` answers it -- a declared field that reaches no reader
  # is not declared -- and the exporter importing three dead targets every run was the price of the name.
  # WHAT THE DELETION DOES NOT DO: it does not give the mechanic a driver. The §§1-4 CB-gated parliamentary
  # TERRITORY TRANSFER motion in `systems/factions/sim/parliamentary_transfer.py` is untouched and still
  # nothing drives it; `engine/season/` has no replacement (its `transfer` verb is an unrelated store-to-store
  # rung move). That file leaves with its tree at `29b`, which is where the mechanic's fate is decided.
  #

  # ── RETIRED AT PLAN POSITION `29b` (2026-10-01): four rows, with the tree that was their only reader ──
  #   `parliamentary_vote`, `parliamentary_motion`, `parliamentary_vote_declaration` -- read by
  #   `systems/factions/sim/{parliamentary_transfer,parliamentary_action}.py`; their targets in
  #   `systems/social_contest/sim/parliamentary_vote.py` (and its sibling `parliamentary_stay.py`, which imported
  #   only `parliamentary_vote`) went with the readers. Faction acts are person acts `via` seats in the season loop; the
  #   vote's verb content is `levy`/`open_case`/`determine`/`issue` + `march`.
  #   `world_gen_settlements` -- read by `game_state.create_world`; the season's world is built by
  #   `engine/season/harness/populated.build_realm`. `systems/settlements/sim/registry.populate_from_geography`
  #   lost its only role there and was deleted with the rest of that tree at `29c` (2026-10-01).
  # The deleted files are retrievable through their `references/restructure_ledger.md` rows.
  #
  # Exactly one role remains. ID-13 applies to the next row added: a role no caller requires is not declared.
  #
```

*Full-line comment, was at line 111.*

```text
  # `verb: march` at `31c`. No production row carries `entry:` yet -- the first is `31a`'s.
```

## modules: `faction_state`

*Inline comment on `sim_module: none`, was at line 123 (with its continuation lines, to line 127).*

```text
# was `engine/autoload/game_state.py` (the `Faction` dataclass, OI-54): deleted at plan
      # position `29b` (2026-10-01) with `systems/factions/`. No season counterpart holds a faction stat vector, by
      # architecture (`architecture/meta/04_CODE_ARCHITECTURE.md`: `faction_q.resolve` builds a view that is NEVER a field of its own), so this
      # contract's `state:` block now describes no code. The row is kept, not deleted: it is a registry row other
      # contracts' `with:` joins name, and removing it is its own change.
```

## modules: `npc_behavior`

*Inline comment on `sim_module: none`, was at line 159 (with its continuation lines, to line 170).*

```text
# OI-54 (ED-IN-0097, W4): re-verified — systems/npcs/ has ZERO .py files
      # (matches this entry's own consumes: comment above, "npc_behavior has no runtime"). Doc is
      # real (not doc:null) but there is no code home yet; the NPC family lane is unresolved (§5
      # row 9 / OI-59).
      # NEAR-MISS DISCLOSED (W4 gate, adj finding 8 / critic Q-8 — the mechanics_index cross-check
      # this row's first draft skipped): mechanics_index.yaml:192-196 carries
      # `npc_ai_service -> engine/autoload/npc_ai.py`, whose own docstring declares entry points
      # `select_action` / `evaluate_priority_stack` — i.e. exactly this contract's stated role.
      # Still `none`, deliberately: that module was converted to `stubwire` in W1 (ED-IN-0093,
      # OI-17 armature-stub batch), so it is an explicitly-flagged not-built shell, not an
      # implementation of this contract. Declaring it would make the join report a code home that
      # answers no Key. Recorded rather than silently omitted; revisit when the NPC lane resolves.
```

## modules: `npc_memory`

*Inline comment on `sim_module: none`, was at line 216 (with its continuation lines, to line 217).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified
      # (find/grep for npc_memory* across the tree returns nothing).
```

## modules: `piety_track`

*Inline comment on `sim_module: systems/characters/sim/conviction.py`, was at line 240 (with its continuation lines, to line 244).*

```text
# OI-54 (ED-IN-0097, W4): matches
      # mechanics_index.yaml's `certainty_track`/`conviction_scar` entries (same file); content
      # verified directly (apply_conviction_scar, per-Conviction Scar thresholds — §2 of this
      # module's own doc). This is the PERSONAL piety_track, not territorial_piety below (3-way
      # name collision noted in gap_notes) — do not conflate the two sim_module: values.
```

## modules: `territorial_piety`

*Inline comment on `sim_module: none`, was at line 278 (with its continuation lines, to line 280).*

```text
# was `systems/overview/sim/ci_track.py` (the CI half) and `Territory.pt` in
      # `engine/autoload/game_state.py` (the CV half): both deleted at plan position `29b` (2026-10-01). The Accord / CI /
      # IP / RS clocks have no season analogue (`engine/season/loop/census.py`: no clock generates anything).
```

*Full-line comment, was at lines 286-289.*

```text
      # "TC (Theocracy Counter)" row STRUCK 2026-07-08 (ED-IN-0029 docket, OPT-AV-7): TC is CI's
      # retired predecessor name, not a second live clock (conviction_track_v30.md's glossary
      # note, corrected same pass). This entry was carrying it as a separate, still-writable state
      # slot alongside CI itself — pure propagation of an already-decided rename, no new ruling.
```

## modules: `threadwork`

*Inline comment on `sim_module: systems/threadwork/sim/operations.py`, was at line 321 (with its continuation lines, to line 326).*

```text
# OI-54 (ED-IN-0097, W4): matches
      # mechanics_index.yaml's `thread_leap`/`thread_weaving`/`thread_pulling`/`thread_locking`/
      # `thread_dissolution`/`thread_mending` entries (all this file — the operation-roll
      # resolver this contract's `resolver: dice_pool` names). Coherence/Fatigue state and the
      # co_movement/collective/opposing/rendering/threadcut siblings are separate mechanics_index
      # entries under systems/threadwork/sim/ — not this module's own state:, not cited here.
```

*Inline comment on `- {name: "Coherence", bucket: track, writable: true}`, was at line 330.*

```text
# bucket pool->track RATIFIED 2026-07-08 (ED-IN-0029 docket, OPT-AV-3/D7): propagates the already-resolved-but-never-applied ED-830 ruling ("Coherence reclassified from Derived Value to Track"); now also registered in descriptor_registry.yaml not_descriptors.tracks. Prior [ASSUMPTION bucket] tag struck (canonical pool notice PP-616/618/619/624/625 was about the depletion MECHANIC, not the bucket taxonomy)
```

## modules: `fieldwork_knots`

*Inline comment on `sim_module: systems/fieldwork/sim/knots.py`, was at line 356 (with its continuation lines, to line 362).*

```text
# OI-54 (ED-IN-0097, W4): matches
      # mechanics_index.yaml's `knots` entry directly (module alias is literally "Knots"); this
      # module's gap_notes already flag it as needing a rebuild (C-TW-12) — real code, imperfect
      # fidelity, still a genuine G_code join. The Evidence/Disposition Track rows of this
      # contract's state: are implemented in the SIBLING systems/fieldwork/sim/fieldwork.py
      # (mechanics_index `disposition_track`/`evidence_track`), not in knots.py — disclosed, not
      # papered over; knots.py is picked as primary because the module/alias name matches it.
```

## modules: `scene_slate`

*Inline comment on `sim_module: none`, was at line 409 (with its continuation lines, to line 414).*

```text
# RETIRED AT PLAN POSITION `28-iii` (2026-10-01). It was engine/autoload/scene_slate.py,
      # a 59-line queue, deleted (its restructure_ledger row, ref 5c5d8ec6). The season loop's counterpart is
      # `engine/season/loop/deliberate.py` + `pack_scenes`, and this row is NOT re-pointed at it: this contract's
      # resolver is the 7-priority slate GENERATOR, which the wiring note below records as never built.
      # (Until then OI-54, ED-IN-0097 had recorded the row as DISCREPANT with the W4 preflight's "no-sim" list,
      # because the file was real, scanned code. With the file gone the preflight's characterization holds.)
```

## modules: `game_director`

*Inline comment on `sim_module: none`, was at line 437 (with its continuation lines, to line 447).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified —
      # grep for mechanical.scene_entered/scene_exited/scene_skipped across systems/+engine/ finds
      # NO emitter anywhere. engine/autoload/season_manager.py implements a season-loop
      # (advance_season/check_arc_boundary) but is not a zoom-stack orchestrator and emits none of
      # this module's declared Keys — a partial behavioral analog, not this contract's code home.
      # SECOND NEAR-MISS DISCLOSED (W4 gate, adj finding 8 / critic Q-8): engine/cross_scale/
      # scene_dispatch.py is the closer analog for the "zoom-stack orchestrator" half of this
      # contract's resolver: manifest — it routes scene entry/exit across scales. Still `none`:
      # it is NOT in mechanics_index.yaml at all (grep: zero hits, so there is no indexed
      # precedent to cite) and it emits none of this module's `mechanical.scene_*` Keys either.
      # Both analogs named so the `none` is a measured absence, not an unexamined one.
```

## modules: `scene_timer`

*Inline comment on `sim_module: none`, was at line 468 (with its continuation lines, to line 469).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified
      # (find for scene_timer* across the tree returns nothing).
```

## modules: `audit`

*Inline comment on `sim_module: none`, was at line 490 (with its continuation lines, to line 492).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified —
      # this is the observability/QA-tooling "audit" module (see resolver comment), distinct from
      # the tools/ audit apparatus outside the gameplay runtime; no runtime consumer code found.
```

## modules: `social_contest`

*Inline comment on `sim_module: systems/social_contest/sim/contest/`, was at line 513 (with its continuation lines, to line 515).*

```text
# OI-54 (ED-IN-0097, W4): directory path —
      # matches mechanics_index.yaml's `social_contest` entry verbatim (the live contest kernel
      # package, contest_rebuild Stages 0-3 landed per that entry's own note).
```

## modules: `mass_battle`

*Full-line comment, was at lines 540-546.*

```text
    # sim_module: DELIBERATELY NOT ADDED HERE (OI-54, ED-IN-0097, W4): this module's rows are
    # MB-owned per the plan's shared-file single-writer table ("module_contracts.yaml: MB owns
    # rows [mass_battle] and its E1 deletion; IN owns the rest") — the join lane does not touch
    # MB's rows even to add a field. The join-verified checker (structure_audit.py) therefore
    # reports this module as `undeclared` (not `unresolvable` — the field is legitimately absent,
    # not wrong) until the MB session adds it. LEAD for MB: mechanics_index.yaml already carries
    # `mass_battle -> systems/mass_battle/sim/massbattle.py`.
```

## modules: `domain_actions`

*Inline comment on `sim_module: none`, was at line 580 (with its continuation lines, to line 594).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified —
      # grep for every da.* Key-type string literal (antinomian_action/covert_betrayal/
      # diplomatic_alliance/economic_intervention/public_governance) across systems/+engine/ finds
      # ZERO emitter code (only engine/cross_scale/articulation.py's consumer constant list). The
      # accounting_sequence's "select_proposal()/execute_proposed_domain_actions()" prose (below,
      # DA_proposal phase) names no function that exists in systems/factions/sim/faction_action.py
      # (checked directly) — descriptive doc-12 prose, not a code pointer.
      # NEAR-MISS DISCLOSED (W4 gate, adj finding 8 / critic Q-8 — the mechanics_index cross-check
      # this row's first draft skipped): this entry's OWN `aliases: ["Domain Echo"]` above matches
      # mechanics_index.yaml:899-903's `domain_echo -> engine/cross_scale/domain_echo.py`, a real
      # scene->faction stat-propagation module. Still `none`, deliberately: domain_echo.py
      # TRANSPORTS the echo (it is the cross-scale carrier wired under ECHO_TRANSPORT, ED-IN-0028)
      # and emits none of the five `da.*` Key types this contract declares — the alias is a naming
      # collision between "Domain Echo (§5 transport)" and "domain actions (the DA framework)",
      # not a shared code home. Recorded rather than silently omitted.
```

## modules: `peninsular_strain`

*Inline comment on `sim_module: systems/overview/sim/`, was at line 620 (with its continuation lines, to line 629).*

```text
# OI-54 (ED-IN-0097, W4): DIRECTORY — this module's
      # state: block splits across several files with no single owner: MS is
      # systems/overview/sim/ms_track.py (this module's own state: comment already names it as
      # "the canonical MS-arithmetic surface", cross-checked with mechanics_index.yaml's `ms_track`
      # entry), IP WAS systems/overview/sim/ip_track.py (deleted 2026-10-01, plan position 29a: two stubs, no
      # production caller; the mechanics_index `ip_track` row is left standing). Turmoil has
      # NO tracker file anywhere (verified: grep for a Turmoil writer finds none) — this is the
      # open §5 row 7 fork (Turmoil writer unruled), not papered over by pointing at a directory.
      # A directory join is honest disclosure of the split, not a claim that every file in it
      # implements this contract.
```

*Inline comment on `- {name: "MS (Mending Stability)", bucket: clock, writable: `, was at line 635.*

```text
# OI-32a ownership declaration (2026-07-29, W3 item 3): mechanically-determinable GAP-F1 owner. Floor 0 (Rupture) / ceiling 100; baseline decay -1/in-game-year at Year-End Accounting, PP-255 (params/core.md §MS Baseline Decay). Live tick: systems/overview/sim/ms_track.py (apply_ms_baseline_decay / apply_ms_delta, the canonical MS-arithmetic surface), (its former caller, systems/overview/sim/accounting.py, was deleted at plan position `29a`). CORRECTED 2026-07-29 (W3 item 8): the prior version of this comment claimed "accounting.py L36-39 also inlines the same PP-255 decay pending a migration" — that claim is FALSE against the current tree (re-verified directly: accounting.py has no inline decay logic anywhere; :36-39 is drift-probe docstring prose, not code, and the sole decay call fully delegates to ms_track.apply_ms_baseline_decay). The claim was carried over from ms_track.py's own docstring (a stale note predating accounting.py's migration to the delegated call — not corrected there, out of this file's scope; logged per CLAUDE.md §0.1 point 5). No env.ms_delta emit added here — a new emit would itself be a new dangling emit; see gap_notes GAP-F1 residual.
```

## modules: `settlement_layer`

*Inline comment on `sim_module: none`, was at line 682 (with its continuation lines, to line 687).*

```text
# RETIRED AT PLAN POSITION `29c` (2026-10-01). It was `systems/settlements/sim/settlement.py`
      # (OI-54: the §1.3 Prosperity/Order/Local-Economy computation), with the Legitimacy/Popular Support
      # fields in the sibling `registry.py`; the whole `systems/settlements/sim/` tree is deleted (each file has
      # an exact row in `references/restructure_ledger.md`, ref 5c5d8ec6). The season's settlement is a `Rung`
      # with `Site`s (`Site.condition`, `world_q.fortification_of`). The row is kept, not deleted: removing a
      # contract row is its own change, and `doc:` above still resolves.
```

## modules: `settlement_economy`

*Inline comment on `sim_module: none`, was at line 762 (with its continuation lines, to line 764).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified
      # (no settlement_economy*.py anywhere) and consistent with this entry's own gap_notes
      # ("RECOMMEND RETIRE ... phantom module (no doc/state/logic)").
```

## modules: `ci_political`

*Inline comment on `sim_module: none`, was at line 786 (with its continuation lines, to line 791).*

```text
# OI-54 (ED-IN-0097, W4): re-verified — no dedicated code found (grep for
      # political_pool/card_hand/ci_political across systems/+engine/ finds only a docstring
      # listing in systems/factions/__init__.py, not implementation). Matches this entry's own
      # gap_notes ("ZERO Key integration in a CANONICAL doc"). Not the same file as
      # territorial_piety's ci_track.py (CI GENERATION lives there per clock_registry's ownership
      # split; ci_political reads CI for political effects §3-§5, which is unbuilt).
```

## modules: `victory`

*Inline comment on `sim_module: none`, was at line 816 (with its continuation lines, to line 818).*

```text
# RETIRED AT PLAN POSITION `28-iii` (2026-10-01). It was engine/autoload/victory.py, deleted
      # (its restructure_ledger row, ref 5c5d8ec6); disposition (c), no season replacement. The GD-1 requirement
      # it implemented survives as the `ABSENT_RULE` row `H-176` in engine/season/hole_register.yaml.
```

## modules: `engine_clock`

*Inline comment on `sim_module: engine/season/loop/driver.py`, was at line 865 (with its continuation lines, to line 871).*

```text
# RE-POINTED AT PLAN POSITION `28-iii` (2026-10-01). This row said
      # `none` all the while engine/autoload/engine_clock.py existed (ED-IN-0199) -- it never named that file,
      # and that file and engine/autoload/season_manager.py are now deleted (their restructure_ledger rows,
      # ref 5c5d8ec6). It now describes the code that owns the season tick in the adopted game:
      # `engine/season/loop/driver.py` (`SeasonDriver.season`, the ONE `w.tick += 1`) with
      # `engine/season/loop/calendar.py` (barrier 1, `Date.fired`). So `CLAUDE.md` §6's "starting with
      # `engine_clock`" means that driver + calendar pair, not a module. `doc:` stays null pending ED-1051.
```

## modules: `faction_politics`

*Inline comment on `sim_module: none`, was at line 897 (with its continuation lines, to line 900).*

```text
# OI-54 (ED-IN-0097, W4): re-verified — no dedicated code found (a
      # Standing/coup_attempted/succession grep across systems/+engine/ turns up only unrelated
      # substring hits). Matches this entry's own state: comment above ("contract-truth
      # declaration, not a sim build — OI-20's sim half stays DEFERRED to the FA lane, §3.5").
```

*Full-line comment, was at lines 904-906.*

```text
      # ── added 2026-07-29 (W3 item 3, OI-24 contract-truth sweep): top-level state items,
      #    read directly off faction_politics_v30.md's own definitions. Contract truth only —
      #    no sim build (OI-20's sim half is DEFERRED → FA lane, §3.5). ──
```

*Inline comment on `- {name: "Standing", bucket: track, writable: true}`, was at line 907.*

```text
# §1.0 Ladder Architecture: 8-position per-faction rank ladder, 0 (pre-initiation) to 7 (senior-most short of Leadership); one ladder per faction (Crown §1.1, Hafenmark §1.2, Varfell §1.3, Church §1.4) + sub-office ladders (§2.1-§2.7). Bidirectional: demotion (§1.0a, ED-776) drops 1 rank by default, 2-3 for severe institutional-violation triggers — track, not clock (parallels Prosperity/Defense/Order §1.3 pattern elsewhere in this file). Emits state.standing_change.
```

*Inline comment on `- {name: "Coup posture", bucket: track, writable: true}`, was at line 908.*

```text
# §1.1d/§2.1 (Löwenritter Grand Master row): "Coup Counter mechanisms (original factions_ttrpg_v30 §8.9)"; classification per §10.1 ED-POL-09 ("types can combine — a Palace Coup can trigger a Constitutional Crisis response; specific mechanics deferred to faction_layer_v30 update"). This doc does not itself specify the counter's numeric mechanics (deferred, per ED-POL-09, to a faction_layer_v30 update) — declared here as the state item behind state.coup_attempted, not as a ratified formula. NOTE: engine/params/factions_personal.md records the Löwenritter-specific instance of this mechanic as STRUCK/superseded by "Graduated Autonomy" (ED-781/ED-589); faction_politics_v30.md itself has not been migrated off "Coup Counter" terminology — contract reflects the doc as written, migration is a separate (unstarted) editorial item, not fabricated here.
```

*Inline comment on `- {name: "Succession status", bucket: track, writable: true}`, was at line 909.*

```text
# §1.0 intro: Leadership is reached "via the succession mechanisms in Part 2 of the original register (SUC-01-03, LIN-01-04)"; per-faction Standing 6/7 rows are explicitly succession-eligible/succession-prepared states (Crown §1.1 Std 6-7, Hafenmark §1.2 Std 6-7, Varfell §1.3 Std 7, Church §1.4 Std 5); §6 specifies the three Baralta Crown Claim succession-contest outcomes (Outcome A/B/C). Emits state.succession.
```

## modules: `miraculous_event`

*Inline comment on `sim_module: none`, was at line 930 (with its continuation lines, to line 932).*

```text
# RETIRED AT PLAN POSITION `29d` (2026-10-01). It was `systems/world/sim/miraculous_event.py`
      # (OI-54): one `stubwire.stub_resolve` armature stub, no importer, deleted with its tree. The row is kept, not
      # deleted: removing a contract row is its own change, and `doc:` above still resolves.
```

## modules: `scenario_authoring`

*Inline comment on `sim_module: none`, was at line 953 (with its continuation lines, to line 956).*

```text
# OI-54 (ED-IN-0097, W4): doc:null/no-sim per the W4 preflight; re-verified
      # (no scenario_authoring*.py anywhere; tools/mechanics_index_gen.py's one hit is the
      # generator script mentioning the module name in a comment, not runtime code). Matches this
      # entry's own gap_notes ("Execution unbuilt — no Stage-1 compile tooling").
```

## modules: `clock_registry`

*Inline comment on `sim_module: none`, was at line 976 (with its continuation lines, to line 979).*

```text
# OI-54 (ED-IN-0097, W4): by design, per this module's own resolver comment
      # ("catalog of clocks/tracks; owns no state, resolves nothing") and gap_notes ("pure
      # manifest — every listed clock is owned by its source system"). Re-verified: no
      # clock_registry*.py anywhere. Not a gap — a module that is intentionally code-free.
```

## modules: `combat`

*Inline comment on `- module: combat`, was at line 997.*

```text
# plan position `30` (A-25): one identity per module, its directory name. Was `personal_combat`; the prize row `the body` (`engine/season/rosters.yaml` `contest_subsystems`) names it by this key. Its PROVIDER keeps the name `personal_combat` -- a provider name says what runs, not whose module it is.
```

*Inline comment on `sim_module: systems/combat/combat_engine_v1/`, was at line 1000 (with its continuation lines, to line 1003).*

```text
# OI-54 (ED-IN-0097, W4): directory — matches
      # mechanics_index.yaml's `combat` entry verbatim (same doc:/sim_module: path, as expected
      # for the canonical engine). NOTE: this is a module_contracts.yaml edit only — no file
      # under systems/combat/** (the STOP-list path) is touched by adding this pointer.
```

*Inline comment on `- {id: "combat.feint",   resolver: d_sigma,      status: RET`, was at line 1029.*

```text
# ED-PC-0035: NOT pending — the feint was deliberately DISSOLVED into the attack (WS-5, 2026-06-29); FEINT_*/feint_eval are gone. Listing it PENDING invited a re-implementation of a retired design.
```

*Inline comment on `- {id: "combat.grapple", resolver: d_sigma,      status: PAR`, was at line 1033.*

```text
# ED-PC-0035: was PENDING with a note pointing at "the currently-unconsumed `clinch` weapon field" — but that field was DELETED and is actively FORBIDDEN (D9/JD-7; capabilities.py self-tests that `clinch=` is absent from weapons.py), and the contact axis is BUILT and wired (contact.py: grab_sigma + the branching grapple menu, called from the wrapper outcome tail). Residual scope (choke/pin depth) is ED-PC-0007.
```

## modules: `campaign_architecture`

*Inline comment on `sim_module: none`, was at line 1068 (with its continuation lines, to line 1072).*

```text
# OI-54 (ED-IN-0097, W4): status: stub below — RECLASSIFIED 2026-06-10 as a
      # cross-cutting consolidation doc, not a runtime module (this entry's own gap_notes); its
      # contents distribute across victory/threadwork/settlement_layer/peninsular_strain, each
      # already sim_module:-joined above. Retire-candidate per §5 row 9 of this program's Jordan
      # docket (unruled) — recorded, not acted on here.
```

## Wiring, vocabularies and foundation gaps

*Full-line comment, was at lines 1118-1130.*

```text
# WIRING — build state and Godot port status (folded in from references/wiring_manifest.yaml,
# 2026-08-23, plan S5c). Filed ED-IN-0074 (2026-07-17 MC-wiring coverage audit).
#
# WHY IT LIVES HERE NOW. It was a second registry keyed by the SAME 27 module names as `modules:`
# above, so "every wiring tag resolves to a module contract" and "coverage is 27/27" were CHECKED
# invariants that a join makes STRUCTURAL — they cannot fail once the facts sit on the row they
# describe. What the split actually bought was a place for the two registries to disagree, and
# they did: the manifest carried `resolver: armature_dot_product` for articulation_layer, which is
# the reading verification RU-4 had already corrected on the contract row ("the armature
# dot-product is the SUBSTRATE interpretation primitive, NOT a system resolver"). Nothing joined
# them, so the corrected fact and the stale one both shipped. `tier`/`scale`/`resolver` are NOT
# carried here for that reason — the contract row owns them.
#
```

*Full-line comment, was at lines 1133-1136.*

```text
# The `adapters:` block (cross-scale seams, tags resolving to engine/cross_scale/) and its two rules
# were retired at plan position `28-iii` (2026-10-01) with the directory they named.
# Ranked port work-list: WAS `python3 tools/build_contract_index.py --work-list`; that tool
# retired with the Key substrate (2026-09-16, ED-IN-0232) and has no replacement.
```

*Inline comment on `unit: combat`, was at line 1160.*

```text
# the `modules:` row of that name (was `personal_combat`; plan position `30`)
```

## `doc:` comments that repeat verbatim across rows

*The same inline comment sat on the `doc:` line of several rows. Recorded once; the row list follows each block.*

```text
# ED-IN-0231: quarantined, and the pointer kept rather than nulled. `doc:` is read by CODE — workbench node-state, the key graph's authority check, the census — not by an agent hunting canon, and the `.designs/` prefix now carries the NOT-CANON signal that a bare `systems/` path did not. Nulling it broke five tools and lost the provenance without hiding anything.
```

Rows: `faction_state` (line 122), `piety_track` (line 239), `territorial_piety` (line 277), `threadwork` (line 320), `fieldwork_knots` (line 355), `social_contest` (line 512), `mass_battle` (line 539), `peninsular_strain` (line 619), `settlement_layer` (line 681), `victory` (line 815), `miraculous_event` (line 929).

```text
# ED-IN-0231: quarantined, and RESTORED here on purpose. This module has NO CODE, so severing its doc would not hand authority to the code — it would leave the module a bare name with nothing defining it, which tests/valoria/test_key_graph.py rightly refused until it retired with the Key substrate (2026-09-16, ED-IN-0232 — the guard is gone, the reason the pointer was restored is not). Its twelve code-bearing siblings stay null: there the code IS the authority (CLAUDE.md §0.05).
```

Rows: `npc_behavior` (line 158), `ci_political` (line 785), `faction_politics` (line 896), `clock_registry` (line 975), `campaign_architecture` (line 1067).
