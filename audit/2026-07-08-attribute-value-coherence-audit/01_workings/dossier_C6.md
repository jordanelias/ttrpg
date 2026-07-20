# Dossier C6 — Code constants & the export pipeline

**Headline.** The one CI-blocking, actually-verified oracle→export link in the whole repo
(`config.py` → `combat_engine_v1.json`, `tools/export_engine_params.py --check`) is real and currently
green — but it covers only `config.CFG`, a single dict inside `config.py`; the ~15 co-equal
`[canonical: ...]`-tagged constants that live one file over in `core.py` (pool formula, `DECISIVE_OB`,
`DMG_SCALE`, `QUAL`, `DELIVERY`, `RESIST`, `COVERAGE_GAP`, `OW_MAX`/`OW_Z`) are invisible to that
exporter and reach `combat_config.gd` by hand with **zero** round-trip check of any kind — today they
happen to match byte-for-byte, but nothing would catch it if they didn't. Inside `config.CFG` itself,
7 of 181 keys (`CHOKE_GRIP_MIN`, `CONC_BASE_K`, `EXPOSE_CHOKE_K`, `EXPOSE_MOMENT_REF`,
`POLE_CLOSE_PENALTY`, `REACH_ADV_K`, `RESIDUAL_REACH_FRAC`) are genuinely dead — never read by any
engine module — yet still get exported into the typed JSON as if live, the same failure shape as the
repo's own documented `DAMAGE_SCALE=4.0` precedent. Separately, one row the census flagged as dead
(`STAMINA_REF`) is demonstrably alive (`wrapper.py:361`) — a real census error, not a real finding — while
the sigma-leverage constant families (`PER_DIE`, `LEVEL_SIGMA`, `M_MAX`, `SIGMA_N_COEFF`, `TN_STANDARD`)
verify verbatim-identical across `params/core.md`, `m1_dice_sigma_core.py`, and `sigma_leverage.py`, and
the frozen `m1_dice_sigma_core.py` the latter claims to retire is still a live import for two workbench
tools. The sharpest finding is structural, not numeric: `sim/substrate/keys.py`'s `KeyLog._validate`
enforces `impact_vector` axis names against the canonical 4-axis set (invariant 6) but applies **no
check whatsoever** to `stat_deltas` key names — any string can ride into the Key log as a "stat," with no
registry, no warn, no block — a key-binding-gap the armature's own invariant discipline should already
cover and doesn't.

---

## Trace narrative

### 1. Dice/sigma primitives — prose → two parallel oracles (COHERENT, verified live)

`params/core.md:113-115` (canonical die table) → `sim/autoload/dice_engine.py:43-51` (`_die_result`,
byte-exact 1/-1, 2-6/0, 7-9/+1, 10/+2) and `:58-62` (`_CONTINUOUS_PARAMS`, TN6/7/8 μ/σ) both match the
prose table exactly. `sim/autoload/sigma_leverage.py:73-77` (`PER_DIE`), `:79` (`TN_STANDARD=7`),
`:85-90` (`LEVEL_SIGMA`), `:92` (`M_MAX=1.5`), `:93` (`SIGMA_N_COEFF=0.8`), `:96` (`OB_MIN=1`),
`:100-101` (`MU_PER_DIE`/`SD_PER_DIE`), `:104` (`OVERWHELM_SIGMA=0.85`, cross-checked against
`designs/audit/2026-06-03-contest-groundup/engine.py:14`) all reproduce
`tests/sim/v32-combat-balance/m1_dice_sigma_core.py:26-62` **verbatim** (same dict literals, same
`[canonical: ...]` tags) — the census's COHERENT verdict for this whole family holds under direct
byte comparison, confirming CLAUDE.md's own framing that the stdlib port is parity-tested against the
numpy original (`sim/tests/test_sigma_leverage_parity.py:1-30`).

**Residual surprise:** `sigma_leverage.py`'s docstring (`:12-16`) claims to retire "the test-dir
dependency (`tests/sim/v32-combat-balance/m1_dice_sigma_core.py`)" and `core.py:4-8` says the same
migration already happened for the *engine* (ED-1085, numpy de-leaked from the runtime). True for
`core.py`/`wrapper.py`. **Not true for the workbench**: `designs/scene/combat_engine_v1/workbench/
presets.py:21` and `workbench/probabilities.py:16-17` still `import m1_dice_sigma_core as m1` directly,
with `probabilities.py:16` commenting "frozen-harness constants... resolved via the insert above." The
"FROZEN...validation station" (core.py:6) is still a live import dependency for dev tooling. Low
severity (workbench is not shipped/consumer-facing) but the "retired" framing in two docstrings
overstates what actually moved.

### 2. Combat Pool formula — 4-way agreement (COHERENT, re-confirms CLAUDE.md baseline)

`core.py:27-28` (`POOL_FLOOR=5 [canonical: params/core.md §Derived Scores]`, `BASE_POOL=6 [class-C:
armature...ED-901]`) → `core.py:32` (`max(POOL_FLOOR, History+BASE_POOL)`) → `references/
module_contracts.yaml:810` (`resolver: d_sigma... pool=max(5,History+6)`) →
`designs/godot/skeleton/engines/combat/resources/combat_config.gd:15-16` (`pool_base: int = 6`,
`pool_floor: int = 5`). Four independent surfaces, one number. This is the CLAUDE.md-cited
"live combat head" resolution of the Combat Pool triple-carry — confirmed intact end-to-end, not
re-litigated as a new finding.

### 3. `config.CFG` → `combat_engine_v1.json` → `combat_config.gd` — verified live, narrower than it looks

Ran `tools/export_engine_params.py --check` live: **"Engine-params round-trip: committed JSON matches
config.py"** — the blocking CI gate is real and currently green (not merely asserted by doc comment).
Field-by-field diff of `combat_config.gd:14-64` against `config.py`/`references/engine_params/
combat_engine_v1.json` confirms exact matches for `m_max`(1.5), `sigma_n_coeff`(0.8),
`wound_atk_ob`/`wound_def_ob`(0.15/0.25, `config.py:65`, ED-1041 — KNOWN-TRACKED, not re-argued),
`adef_w`/`adef_blunt`/`adef_point`/`adef_cut`(`config.py:44`), `adef_threshold`
(`{none:0,light:0.30,medium:0.45,heavy:0.72}`, `config.py:51` — ED-1050 monotone fix, confirmed
byte-identical port↔oracle as the ledger claims), `reach_frac`/`reach_w`(`config.py:18-19`),
`commit_sigma`/`init_k`/`init_reading_k`/`init_history_k`/`attacker_bias`/`read_history_k`
(`config.py:64,66,133`), `upset_floor`(`config.py:161`) — 20+ coefficients, zero drift found.

**But `config.CFG` is not the whole oracle.** `export_engine_params.py:69` exports only
`config.CFG` ("`"cfg": _typed(config.CFG)`"). `combat_config.gd` also carries `decisive_ob`(3.0),
`pool_base`/`pool_floor`, `damage_scale`(1.55), `heft_light`/`heft_heavy`, `qual`, `delivery`,
`resist`, `tier_to_material`, `coverage_gap` — **all of these trace to `core.py`, not `config.py`**:
`DECISIVE_OB=3` (`core.py:25`), `POOL_FLOOR`/`BASE_POOL` (`core.py:27-28`), `DMG_SCALE=1.55`
(`core.py:74`), `QUAL={'graze':0.25,'partial':0.5,'success':1.0,'overwhelming':1.5}` (`core.py:72`),
`DELIVERY` (`core.py:76`), `RESIST` (`core.py:86`), `COVERAGE_GAP` (`core.py:91`), `HEFT_HEAVY=3.0`
(`core.py:63`) — each carrying its own `[canonical: ...]` tag, exactly as authoritative as anything in
`config.CFG`. **None of these pass through `export_engine_params.py` at all.** Values in
`combat_config.gd` currently match `core.py` byte-for-byte (verified by direct comparison above), but
this match is unverified by any tool — `export_engine_params.py --check` cannot see a `core.py` change
because it never reads `core.py`. This is a coverage gap inside the very discipline CLAUDE.md §6 cites
as the ED-1050 fix ("never let a port 'correct' its oracle in-place... fix canon, re-export") — the
"re-export" half of that promise has no teeth for half the oracle's canonical constants.

One further residual: `core.py:73` defines `OW_MAX=2.5; OW_Z=1.5` (overwhelming-quality sigma-leverage
tail, read at `core.py:174`). `combat_config.gd`'s `qual` dict caps `overwhelming` at a flat 1.5 and its
own comment (line "## QUALITY[degree] — base quality factor (overwhelming gets a sigma-leverage tail in
StrikeModule)") acknowledges the saturation curve is deferred to an unported module — but `OW_MAX`/
`OW_Z` themselves are not staged anywhere in the typed export or the `.gd` file for that future module
to read. Build-state note per cardinal rule (b): the module being PENDING is routing metadata, not
itself a finding; the finding is that when it *is* ported, its two numeric inputs have no export path
prepared, same gap as above.

### 4. Dead `config.CFG` keys exported as if live — more instances of the `DAMAGE_SCALE=4.0` shape

`combat_config.gd`'s own header comment documents the precedent: a dead `config.py DAMAGE_SCALE=4.0`
that `core.py`'s `damage()` ignored, fixed by folding the *live* `core.DMG_SCALE=1.55` into the `.tres`
instead. Cross-referencing every `config.CFG` key (181 total) against every other `.py` file in
`designs/scene/combat_engine_v1/` for a live read (`cfg['KEY']` / `cfg.KEY` pattern) turns up **7 more**:
`CHOKE_GRIP_MIN` (`config.py:101`; superseded in practice by a hardcoded `GRIP_SHORT=0.30` at
`weapon_physics.py:523`, whose own comment says "calibrated to the old CHOKE_GRIP_MIN" — i.e. the config
key was forked into a literal and then orphaned, not merely unused), `CONC_BASE_K` (`config.py:61`),
`EXPOSE_CHOKE_K` / `EXPOSE_MOMENT_REF` (`config.py:82`), `POLE_CLOSE_PENALTY` (`config.py:54`),
`REACH_ADV_K` / `RESIDUAL_REACH_FRAC` (`config.py:6`). All 7 are present in
`references/engine_params/combat_engine_v1.json` (lines 41, 51, 76, 79, 150, 154, 183) — a future Godot
consumer ingesting the typed export has no way to know these 7 of 181 knobs do nothing.

### 5. Census correction — `STAMINA_REF` is alive, not dead

The census row (`finding_basis: F-SIM-04`) asserts `STAMINA_REF=18.0` (`config.py:56`) is "defined but
never consumed." **This is false.** `wrapper.py:361`: `c.stamina=min(c.stamina_max,
c.stamina+cfg['RECOVERY_FRAC']*(c.stamina_max-c.stamina)*(c.stamina_max/cfg['STAMINA_REF']))` — a live
read inside the inter-bout stamina-recovery step of `fight()`. What's true is that `STAMINA_REF` (and
its neighbors `RECOVERY_FRAC`, `CONC_DRAIN_BOUT`, `CONC_RECOVER_FRAC` — same line, `config.py:56,61`)
are **not yet ported** to `combat_config.gd` at all (no `stamina_ref`/`recovery_frac`/`conc_*` fields
exist there). That is a build-state fact (unported), not deadness in the Python oracle — exactly the
distinction cardinal rule (b) warns against collapsing. The census conflated "not yet in the Godot
skeleton" with "dead," which is the wrong basis; the real, correctly-dead constants are the 7 in §4.

### 6. Class-C tagging discipline — undersold, not absent

`config.py:1` blankets everything as "Class-C — calibrated against the harness, not canon." Counting
explicit provenance tags: `[SIM-CALIBRATE]` ×12, `[FIAT]` ×4, `[ASSERTED]` ×2 — 18 of 181 keys carry one
of the three markers the file's own framework defines; the rest are bare literals with descriptive
prose comments only. Separately, `grep`-ing for ED/Jordan citations inside `config.py` turns up
**7 distinct** direct canon references embedded in a nominally-no-canon file: `ED-1021`, `ED-1041`,
`ED-1050`, `ED-1080`, `ED-PC-0002`, and two dated "Jordan 2026-06-0{3,4}" rulings (e.g. `CONC_SPIRIT=2.0,
CONC_FOCUS=3.0` at `config.py:61`, cross-verified against `derived_stats_v30.md:158-160` and
`social_contest_v30.md:235,256` — matches the ratified ED-902 `(3×Focus)+(2×Spirit)` formula exactly,
confirming this specific constant *is* canon-pinned despite living in the "Class-C, not canon" file).
Not a severity finding on its own (nothing here is wrong), but the blanket disclaimer at the top of the
file undersells how many of its 181 entries are actually ED-ratified rather than free sim-seeds — a
reader auditing "what needs Jordan's sign-off vs. what's an engineer's seed" cannot tell from the tag
alone and must grep for citations by hand, which is what this trace had to do.

### 7. `sim/substrate/keys.py` — `stat_deltas` has no registry binding at all (the sharpest finding)

`Target.stat_deltas` (`keys.py:84`) is a bare `dict` with no schema. `KeyLog._validate`
(`keys.py:300-356`) enforces: id uniqueness (inv. 1), type registration + required-payload-fields
presence via `TypeRegistry.validate_payload` (inv. 2 — checks *presence* of declared field names, not
their contents), `causes[]` existence (inv. 3), season monotonicity (inv. 5), **`impact_vector` axis
names against the canonical `AXES` 4-tuple** (inv. 6, `keys.py:321-327`), target `role` membership in
`ROLES` (§2.2), `scale_signature` membership in `SCALES` (inv. 7), and visibility shape (inv. 8). At no
point does any invariant, nor `TypeRegistry.validate_payload`, nor `apply_defaults`, check that a
`stat_deltas` **key name** corresponds to any registered attribute/derived-value/track/pool. Any string
is accepted. Live confirmation: `sim/cross_scale/echo_transport.py:146`
(`stat_deltas={er.affected_stat: er.delta}`) feeds an arbitrary `affected_stat` string straight into a
logged, validated Key with the same zero check.

This is a real gap in the ratified armature (`key_echo_armature_v1.md`, ED-IN-0018) and its substrate
(`key_substrate_v30.md` §2.3, `propagation_spec_v1.md`), not a stub or an unwired build-state issue — the
code that validates axis names exists and runs; the code that would validate stat names simply was
never written, on the one field of the Key schema this whole audit's QUANTITY taxonomy exists to police.
Checked the existing open-fork register around `stat_deltas` (`propagation_spec_v1.md:205`, OF-1
through OF-7) for overlap: OF-1 is about per-stat locus-basis classification, OF-4 is about whether
`apply_state_changes` should be hardened against non-empty `stat_deltas` on faction observers — neither
is "are stat_deltas key NAMES validated against a registered vocabulary." This appears to be genuinely
uncovered by any existing OF/ED.

### 8. Cross-cluster touchpoints (not re-litigated, cited for the interlock view)

- `sim/autoload/game_state.py:50-51` (not `:50-80` as the census cites — `PT_MAP`/`ACCORD_MAP` are two
  single-line dict literals; the wider span the census cited is mostly unrelated helper code) —
  `canonical_pt`/`canonical_accord` bucketing helpers (`game_state.py:60-76`) exist specifically because
  Piety-Track-keyed lookup tables (`CI_YIELD_BY_PT`, Seizure Ob, Ecology weights, per the file's own
  comment `:55-58`) need the canonical integer, not the continuous stored value — a genuine
  code-level touchpoint into the Piety Track multi-referent collision (C4's row); not independently
  re-verified which Piety Track referent this is, per lane scoping.
- `sim/peninsular/ms_track.py:51` `MS_START=60` matches the params/core.md TTRPG-mode value per its own
  comment; `sim/peninsular/ci_track.py:61` `CI_STARTING=28` — both cited correctly by the census, no
  correction needed here (feeds C4's MS/RS and Church Influence rows respectively).
- Social contest's `Concentration` (`(3×Focus)+(2×Spirit)`, `derived_stats_v30.md:158`,
  `social_contest_v30.md:235,256`, `params/contest.md:140`) and combat's `Concentration`
  (`config.py:61` `CONC_SPIRIT=2.0, CONC_FOCUS=3.0`) share the same name, same max-value formula, AND
  same ED provenance (ED-902) — checked for a possible collision, but this reads as one shared derived
  stat used with context-specific depletion curves (combat: `CONC_DRAIN_BOUT`/`_LOSS`/`_HIT`/
  `CONC_RECOVER_FRAC` at `config.py:61-62`; contest: flat 5/exchange, `social_contest_v30.md:256`) —
  legitimate one-quantity/two-contexts design, not a synonym or collision. Noted, not flagged.
  `social_contest_system_v2.md:217` still states the pre-ED-902 struck formula
  ("Concentration = Focus + Recall") — a stale doc-currency issue for the SC lane (versioning ≠
  currency, CLAUDE.md §4), flagged as a feed to SC, not ruled here.

### 9. Census citation-accuracy audit (adversarial pass on the census itself)

- "Contest Track Starting Position," cited `sim/personal/contest/modes.py:5-6` — **wrong**; those lines
  are venue-description prose. The actual `CANONICAL_TRACK_START=5.0` / `CHURCH_TRIBUNAL_TRACK_START=6.0`
  definitions are at `modes.py:450-451`. Values themselves are correct.
- "Readiness Constants (Contest)," cited `primitives.py:18-31` — **wrong span**; those lines are the
  `Stasis`/`Appeal`/`Standing` classes. Actual definitions are scattered: `MAX`/`REGAIN` at
  `primitives.py:50,52`, `BASE`/`MARGIN` at `:209,214`, `READING_COEFF` at `:226`, `CAP` at `:233`,
  `ETHOS_UNLOCK`/`LEAK_CAP` at `:241-242`, `FLOOR` at `:255`. Values correct, line numbers not.
- "Contest Resolver Constants," cited `resolver.py:38-45` — close; actual span is `:33-42`. Minor.
- "Degree Thresholds (Combat vs Contest)" omits the Ob-20 exception that is both real code
  (`dice_engine.py:104-113`) and real canon (`params/core.md:55`, "Ob 20 exception: Overwhelming
  unavailable, Partial requires net ≥ 10") — an incompleteness in the row's formula description, not a
  wrong value.
- "STAMINA_REF" verdict is substantively wrong — see §5.
- Everything else spot-checked (dice_engine.py, sigma_leverage.py, config.py, massbattle.py, ms_track.py,
  ci_track.py line citations) held up on direct read.

---

## Findings

| ID | Sev | Kind | Calib. | Claim | Evidence |
|---|---|---|---|---|---|
| C6-F1 | P2 | key-binding-gap | NEW | `Target.stat_deltas` (Key substrate) has zero validation against any registered quantity vocabulary — any string is accepted as a "stat," while the sibling `impact_vector` field IS validated against the canonical 4-axis set in the same function. | `sim/substrate/keys.py:82-92` (Target dataclass), `:300-356` (`_validate`, inv. 6 axis check at `:321-327` vs. no stat_deltas check anywhere); live example `sim/cross_scale/echo_transport.py:146`. Checked against open forks `propagation_spec_v1.md:205` OF-1..OF-7 — none cover key-name validation. |
| C6-F2 | P2 | enforcement-gap / export-drift-risk | KNOWN-UNTRACKED (adjacent to ED-1052, not identical) | The blocking round-trip exporter (`export_engine_params.py --check`, verified green live) covers only `config.CFG`; ~15 co-equal `[canonical: ...]`-tagged constants in `core.py` (`DECISIVE_OB`, `POOL_FLOOR`/`BASE_POOL`, `DMG_SCALE`, `QUAL`, `DELIVERY`, `RESIST`, `COVERAGE_GAP`, `HEFT_HEAVY`, `OW_MAX`/`OW_Z`) reach `combat_config.gd` by hand with no round-trip check at all — currently byte-identical, but nothing would catch a future drift. | `tools/export_engine_params.py:55-74` (exports only `config.CFG`); `designs/scene/combat_engine_v1/core.py:25,27-28,63,72,74,76,86,91,73`; `designs/godot/skeleton/engines/combat/resources/combat_config.gd:14-30` (hand-carried values, comment at top crediting itself with "Ported from...config.py" — core.py is not named). ED-1052 ledger entry (`canon/editorial_ledger.jsonl:284`) covers the params/*.md-prose-parsing question; this specific already-typed-oracle coverage gap is not named there. |
| C6-F3 | P2 | dead / stale | NEW | 7 of 181 `config.CFG` keys are unconsumed by any engine module yet are exported into the typed JSON as if live — the same failure shape the repo already fixed once for `DAMAGE_SCALE=4.0` (documented at `combat_config.gd`'s own header). | `CHOKE_GRIP_MIN` (`config.py:101`, forked into a hardcoded literal at `weapon_physics.py:523`), `CONC_BASE_K` (`:61`), `EXPOSE_CHOKE_K`/`EXPOSE_MOMENT_REF` (`:82`), `POLE_CLOSE_PENALTY` (`:54`), `REACH_ADV_K`/`RESIDUAL_REACH_FRAC` (`:6`) — confirmed unreferenced by any `cfg['KEY']`/`cfg.KEY` pattern across every other `.py` in `designs/scene/combat_engine_v1/`; all 7 present in `references/engine_params/combat_engine_v1.json:41,51,76,79,150,154,183`. |
| C6-F4 | P3 | other (census error) | N/A (finding against the census) | Census row "STAMINA_REF" claims the constant is "defined but never consumed" (F-SIM-04) — this is factually wrong; it is live-read. The true status is "not yet ported to `combat_config.gd`," a different (build-state) fact the census mislabeled as deadness. | `sim/autoload — designs/scene/combat_engine_v1/wrapper.py:361`: `cfg['STAMINA_REF']` consumed in the inter-bout stamina-recovery formula; `config.py:56` definition; `combat_config.gd` has no `stamina_ref` field (confirms the unported half, not the dead half). |
| C6-F5 | P3 | other | NEW | Two `workbench/` tools still directly import the "FROZEN" `tests/sim/v32-combat-balance/m1_dice_sigma_core.py`, the exact dependency `sigma_leverage.py`'s docstring and `core.py`'s ED-1085 note both describe as retired/de-leaked. | `designs/scene/combat_engine_v1/workbench/presets.py:21` (`import m1_dice_sigma_core as m1`); `workbench/probabilities.py:16-17`; contrast `sim/autoload/sigma_leverage.py:12-16` and `core.py:4-8` ("previously reached into the FROZEN...validation station via a sys.path hack...The sigma math now comes from sigma_leverage"). |
| C6-F6 | P3 | other | NEW | `config.py`'s blanket "Class-C — calibrated against the harness, not canon" framing (line 1) undersells that ≥7 of its constants carry direct ED/Jordan-ruling citations embedded inline, and only 18/181 keys carry any of the file's own three provenance tags (`[SIM-CALIBRATE]`/`[FIAT]`/`[ASSERTED]`) at all — a reader cannot tell canon-pinned from free-seed without grepping citations by hand. | `config.py:1` (header); citation grep hits `ED-1021`(`:65`), `ED-1041`(`:65`), `ED-1050`(`:51`), `ED-1080`(`:44`), `ED-PC-0002`(`:15,35,165`), "Jordan 2026-06-0{3,4}"(`:61,54`); tag count: `[SIM-CALIBRATE]`×12+bare "SIM-CALIBRATE"×12 total mentions, `[FIAT]`×2 (+2 bare), `[ASSERTED]`×1 (+1 bare) against 181 total keys. |
| C6-F7 | P3 | other (census error) | N/A (finding against the census) | Two census row citations point at the wrong lines: "Contest Track Starting Position" (cited `modes.py:5-6`, real definitions at `:450-451`) and "Readiness Constants (Contest)" (cited `primitives.py:18-31`, real definitions scattered across `:50,52,209,214,226,233,241-242,255`). Values in both rows are correct; line evidence was not. | `sim/personal/contest/modes.py:5-6` vs `:450-451`; `sim/personal/contest/primitives.py:18-32` vs the cited definition lines above. |
| C6-F8 | P3 | other | KNOWN-TRACKED-adjacent | The census's "Degree Thresholds (Combat vs Contest)" row omits the Ob-20 exception, which is both live code and cited canon — an incompleteness, not a wrong value; doesn't change the row's DRIFTED/F-SIM-05 verdict on the two-degree()-functions split, which is correctly flagged as KNOWN-UNTRACKED there. | `sim/autoload/dice_engine.py:94,104-113`; `params/core.md:55`. |

## Unification options

| ID | What | Recommended default | Feeds |
|---|---|---|---|
| C6-U1 | Extend `KeyLog._validate` (or `TypeRegistry`) with a `stat_deltas` key-name check against a registered quantity vocabulary, mirroring invariant 6's `AXES` check for `impact_vector`. | Add a `descriptor_registry.yaml`-backed (or a new lightweight `registered_stats` set unioning descriptor_registry + `not_descriptors`' derived_value/track/clock/pool lists) **warn-tier** check first (matching the repo's existing warn-before-block posture for attr/agg/fac/set names), promotable to block once the roster ratification (workplan v6 T1 queue-13) lands. | Armature §3 registry-key extension; feeds the key_substrate_v30.md §2.3 invariant set (a candidate invariant 9) and workplan queue-13. |
| C6-U2 | Decide the scope fence for `export_engine_params.py`: either (a) widen it to also serialize `core.py`'s canonical module-level constants (a second `sections.core` block) under the same round-trip discipline, or (b) explicitly document in both the exporter's docstring and `combat_config.gd`'s header that `core.py` constants are OUT OF SCOPE and remain hand-transcribed (a named, accepted risk) until a follow-on ED. | (a) — widen the exporter; the constants are equally canonical, equally small in count (~15), and the exporter's own docstring already claims to cover "the ALREADY-TYPED Python oracle," which core.py plainly is. | ED-1052 (typed engine-params scope) as a concrete next slice; ED-1050's re-export discipline (closes the gap that discipline claims to already close). |
| C6-U3 | Prune or explicitly retire the 7 dead `config.CFG` keys (§4) from the exported JSON (or annotate them `_dead: true` in the export) so a future Godot consumer doesn't ingest inert knobs as if tunable. | Prune from `config.CFG` at the next config.py edit pass (each has a clear reason: superseded-by-geometry, retired mechanic, or never-wired) rather than carrying them indefinitely — matches how `DAMAGE_SCALE`/`HANDLE_RANK`/`HEFT_MODE` were already fully removed rather than just marked dead. | Sim/combat-engine hygiene; no open ED currently owns this — a new `IN` or `PC` lane item if Jordan wants it tracked rather than fixed inline. |
| C6-U4 | Retire the two remaining `workbench/` imports of `m1_dice_sigma_core` (presets.py, probabilities.py) onto `sim.autoload.sigma_leverage`, so the "retired" claim in `sigma_leverage.py`'s docstring is actually true repo-wide, or amend that docstring to scope the retirement to the engine runtime only. | Amend the docstring scope (cheapest, avoids workbench churn) unless the workbench tools are about to be touched anyway, in which case fold the import switch into that pass. | Documentation-accuracy only; no ED needed unless Jordan wants the workbench actually migrated. |

## Registry delta candidates

- `stat_deltas`-eligible quantity names generally — the Key substrate needs *some* enumerable set of
  "things a stat_delta key is allowed to name," which does not exist today in any form (not even a
  warn-tier list). The natural candidate is the union of `descriptor_registry.yaml`'s attribute/
  aggregate/faction/settlement keys plus its own `not_descriptors` block's derived_value/track/clock/pool
  lists — but that union itself does not currently exist as a single exposed set anywhere (C6-U1).
- `core.py`'s canonical module-level constants (`DECISIVE_OB`, `POOL_FLOOR`, `BASE_POOL`, `DMG_SCALE`,
  `QUAL`, `DELIVERY`, `RESIST`, `COVERAGE_GAP`, `OW_MAX`, `OW_Z`, `HEFT_HEAVY`) are load-bearing,
  canon-tagged, and cross into Godot today — but sit entirely outside both `config.CFG` (the one thing
  the exporter serializes) and any registry. Not "descriptor" kind (they're `code_constant`/tunables,
  not attributes), but they are exactly the `code_constant` KIND the registry taxonomy already
  provides for — currently zero of them hold a registry key.
