# POST-ADOPTION EXECUTION PLAN — the nine, and the retirement

## Status: **RULED 2026-09-05 (ED-IN-0202). This is a WORKPLAN, not doctrine.** Layer 1 doctrine is
`architecture/`; the mechanism is `engine/season/`. This file says what to build and in what order,
and it is superseded by its own completion — not by a successor plan.

> **Adjudicated at the top tier, read-only, against the working tree.** Every claim below was
> verified by opening the file cited. Where it corrects an earlier published claim, the correction
> is marked ⚠ and the earlier claim is named rather than quietly replaced.

---

## §0 · Four corrections to the record, because three of them shipped

| published claim | the tree | consequence |
|---|---|---|
| *"`npc_ai.select_action`'s stub hits fail `m1_acceptance` row 1"* | `select_action` is **not on the campaign path** (pinned only by `engine/tests/test_pipeline_reach.py:789`). The two stub hits are `engine/mc_v18.py:194` (`generate_npc`) and `:212` (`form_knot`) | the CONCLUSION survives and is stronger: both stubs cite *"personal-scale actor fields absent from the aggregate strategic World"* — exactly what `engine/season/` supplies. The mechanism named was wrong |
| *"the four registries the code reads at runtime"* (`CLAUDE.md` §3, ED-IN-0202's commit body, PR #371) | `shape.py` opens **three** — `rosters.yaml:449`, `verb_table.yaml:1407`, `write_matrix.yaml:292`. It never opens `hole_register.yaml`, whose readers are `register.py`, `exercises.py`, `run_cases.py` | under §0.05 the register is **mechanism for the corpus grader and reference for the game**. Its stale `:NNN` citations are reference-grade drift, which is why item 0.1 fixes them by hand and mints no guard |
| `requirements.yaml` R-03: *"There is no scene container. `W17` … is unbuilt"* | `class Scene` exists (`shape.py:2289`), `deliberate` packs scenes and stamps `a.scene` (`:5675-5728`), `PLAN.md:1315` records W17 landed | R-03's `measured:` is **wrong about the mechanism and right about the requirement**. What is absent is a scene-granular TICK: `SeasonDriver.season` (`:6470-6486`) runs deliberate→resolve→witness once per season and flattens every scene's acts into one batch. The work item is not W17 |
| `requirements.yaml` R-06: *"GOALS and AMBITIONS have no field and no verb"* | `headless.py:74-81` — Carin's motive is a `commit` Tenure to an OUGHT Proposition, and it is the Q4 source. That **is** the ambition mechanism | missing is a READ (`ambitions(p)`) and a cast (W27). R-06 is closer than its row says |

Two further findings, recorded so no one re-derives them:

- **`register.py --requirements` is an INDEX, not a gate.** `check_requirements` validates the status
  vocabulary, that `measure:` is non-empty, that a `-k` names a real test and a `python X.py` exists.
  **It never compares `status:` to a measurement.** Editing a row to `met` passes. Do not grow it
  (§6 trap 2) — the tests are the gate.
- **`LINEREF_RE` (`register.py:475`) ends in `\b`,** so a 5-digit `:NNN` produces *no match* rather
  than a mis-parse, and no file in the package is over 7,500 lines. Not load-bearing. Dropped, no
  guard (§0.1 pt 5).

---

## §1 · THE FRAME — one engine, two strata

The season loop is the person-scale layer `engine/` has stubbed. But the work is **not a merge**, and
saying "join" without saying *where* is how this gets built wrong.

| stratum | contents | disposition |
|---|---|---|
| **SUBSTRATE** | `autoload/dice_engine.py`, `autoload/sigma_leverage.py`, `substrate/{keys,descriptors,composition,stubwire,canon_buckets}.py`, `engine_params/` | **permanent.** The season loop and the three retained subsystems both sit on it. The join is real HERE, and it is a CALL |
| **OLD DRIVER** | `mc_v18.py`, `autoload/{game_state,engine_clock,season_manager,victory,scene_slate,npc_ai}.py`, `cross_scale/*`, `engine/tests/` goldens | **transitional — this is what Jordan's *"at this moment"* licenses.** The only faction-scale execution artifact today. **Superseded, not joined**, once the loop expresses faction scale in its own shape (R-04) |

**The case against a merge, which is decisive.** `game_state.World` is a stored-aggregate,
institution-acts, globally-reachable state container: `faction_take_action` is dispatched per faction
(`mc_v18.py:138`) and L/Sta/W/I/Mil are stored fields. Layer 1 PART D rows 1, 8 and 14
(`architecture/meta/04_CODE_ARCHITECTURE.md:883,:890,:897`) forbid each of those, and §C.12 rejection 1
forbids `World` reachable by a global name. **You cannot import `game_state` into `shape.py` without
breaking the architecture ratified the same day.** Three further blocks: two drivers is D-17/D-21's
second clock; the `engine/tests` goldens are the only campaign-scale control and a join re-pins them;
and a default-OFF `campaign_seam.py` is §0.3's named failure mode — a document in code form.

**What the loop already proves the direction.** `shape.py:6604` calls `dice_engine.degree_from_net`;
`combat_seam.py:93-96` calls `systems/combat/`. Both declared in `PATH_SEAM_ALLOWED`. Every retained
subsystem **already rolls through the substrate** — `systems/social_contest/sim/contest/resolver.py:24,:307`
calls `degree_from_net`, `parliamentary_vote.py:178` calls `roll_pool`. R-09's producer exists three
times in the tree and zero times in the loop.

---

## §2 · DECISION 1 — the retirement, in two steps

**Ruling: Jordan's two clauses are compatible** once *"retain /engine"* reads as **substrate
permanently, old driver at this moment**.

**Blast radius, corrected.** Of the 65 `systems.*` modules a seeded 1-season probe loads —
mass_battle 22 · social_contest 18 · factions 10 · overview 6 · settlements 5 · world 4 — **40 are in
the RETAIN set.** The retire-set hot-path footprint is **25 modules across four subsystems**. But
`references/module_contracts.yaml:70-193` declares 27 composition roles and **19 target the retire
set** (5 hot-path, 10 `snapshot_state.*` on restore, 2 `scene_resolver.fieldwork/investigation`,
1 `rs_track_delta`, 1 world-gen) — so the retirement also breaks `restore_world` and
`tools/export_composition.py --check`, which the first reading missed.

**§0's five tests.** (1) *Superseded?* No later ruling — but the 2026-09-05 ruling itself supersedes
§0.05's *"does not license deleting design docs"* for these twelve. (2) *Irrelevant?* No — 25 modules
run today. (3) **Answered by a design document — this is the test that closes it.** §C.12 names the
ladder, Key substrate and `engine_params/` as project shapes that port as plain code: the substrate
stratum. PART D rows 1/8/14 forbid `game_state.World`'s shape: the driver stratum cannot be joined,
only superseded. `10_FACTIONS_AND_DEPLOYMENT.md` already defines how a faction appears in the loop.
(4) *Precedent?* `combat_bridge` → `combat_seam`; the culling waves' `FORK:` row after a deletion
rehearsal. (5) *Architecture?* Delete when nothing retained resolves into it, not before.

**Nothing escalates.** Two items are **loud notifications** for the PR body per §2/ED-1094:
(i) the doc-only subsystems' `.md` go to the fork in step B; (ii) step B replaces `mc_v18` as the
Godot oracle — which *"adopt in full"* already ruled.

**STEP A — now (item 0.5).** Make the ruling legible to the mechanism, deleting nothing.
**STEP B — after R-04 (item 4.3).** One commit. Pre-condition: a season-loop campaign artifact
exists in CI (4.2). ⚠ One live hazard first: `systems/social_contest/sim/contest_legacy_stub.py:240`
imports `systems.characters` function-locally and is re-exported by `contest/__init__.py:35` — the
only retain→retire edge. Verify dead or cut.

---

## §3 · DECISION 2 — the nine are not siblings

Two are outcomes, three are producers, the rest hang off the producers.

```
R-09 (a roll)  ──┬──▶ R-05b (contests on person verbs) ──┐
                 ├──▶ R-08 (non-rational choice)         │
H-46 (13 axes) ──┘                                       ├──▶ R-01 / R-02  (MEASURED, not built)
R-03 (scene tick) ──────────────────────────────────────┤
W-F  (outcome → stance) = R-07 ─────────────────────────┘
R-05a (20 verbs) ── parallel from day 1 ──▶ R-04 (scale) ──▶ retirement step B
R-06 (goals read + cast) ── sibling of R-07, feeds R-08's discrimination
```

- **R-09 is the root.** With no roll an act's outcome is a deterministic function of the world, so a
  fork's consequences are identical and propagation is **structurally unobservable**. That is why
  2,403 forks reconverged and W-A/W-B bought ~4%. R-01/R-02 cannot be moved by building on them.
- **R-03 is a prerequisite of R-02 in Jordan's own words** (*"what occurs after one scene can impact
  the next scene"*). Today a decision reaches the *next season's* deliberation. Scene-round ticking
  makes the channel intra-season.
- **R-01 and R-02 are measurements.** No item builds them; wave 3 measures them.
- **R-05 splits:** (a) predicates/effects for the 20 dead verbs, parallel from day one; (b) `contests:`
  on person verbs, which needs R-09.
- **R-04 is last and largest**, and it is what unblocks retirement step B.

**Two structural calls, both closed at §0 without Jordan.** *Scene-round tick* — Jordan's R-03
statement is newer than #353 S26.2's one-freeze-per-season (test 1); `mc_v18` already resolves scenes
sequentially within a season (`scene_dispatch.py:402-414`, test 4). *Pool/Ob derivation* — Jordan
ruled it 2026-08-14 and `dice_engine.py:241-247` records it *"implemented nowhere"*; which
`Person.capability` key a verb rolls is a **roster**, assumption-grade and swept, which is the
doctrine the register already runs on.

---

## §4 · THE PLAN — agonist→antagonist relay

Every antagonist is dispatched `subagent_type: valoria-critic` (read-only **by tooling**,
`.claude/agents/valoria-critic.md:4`), receiving the producer's **output and diff, never its
reasoning** (§10: the relay is stateless). Parallel write lanes take `isolation: worktree`.
"Artifact" is what proves it under §0.2 — an execution result, never a document. `opus` is justified
per item; the default is `sonnet`; `haiku` where the task is transcription.

### WAVE 0 — make the tree legible (all parallel, one day)

| id | deliverable | §0.2 artifact | producer | antagonist brief | moves |
|---|---|---|---|---|---|
| **0.1** | `hole_register.yaml`: every `<file>.py:NNN` → `<file>.py::<symbol>`; drop `:NNN` for non-#353 files. **No new checker.** | `grep -cE '\.py:[0-9]+'` → 0; `--verify-citations` unchanged | `haiku` — find/replace with one grep per symbol | `sonnet`: sample 15 rewrites, `grep -n "def \|class "` each; a symbol that does not exist is a fabrication | unblocks wave 1's `shape.py` edits from re-rotting cites |
| **0.2** | Correct `PLAN.md:145,:1315` ("143"), `00_ADOPTION_README.md:27,:99` ("54"), `CLAUDE.md` §3:490 (four→three registries) | each replaced number becomes a **command** per G11 | `haiku` | `sonnet`: run each command; the printed number must match nothing typed | hygiene |
| **0.3** | Retire `verify_transcription` + `v2_rows` (`register.py:163,:658`): post-adoption the register is the owner and V2's Part VII is reference (§0.05) | `--check` no longer opens `ARCHITECTURE_V2.md`; suite green | `sonnet` | `sonnet`: confirm no other caller; the diff must be net-negative | apparatus −, authority direction corrected |
| **0.4** | `requirements.yaml`: correct R-03 and R-06 `measured:` per §0; repoint R-09's `measure:` to the producer scan | `--requirements` green; **no `status:` changes in the diff** | `sonnet` | `sonnet`: each corrected sentence must cite a line the critic can open | honesty of the index |
| **0.5** | **Decision 1 step A.** CLAUDE.md §3 `systems/` row (three subsystems are the design source; twelve SUPERSEDED, retained pending R-04); `evacuation_plan.py` rule `R-SUPERSEDED-RETAINED-PENDING-R04`, verdict `keep`, reason inline; `RETIRE_SET_ROLES` = the 19 role names, **shrink-only**; verify/cut `contest_legacy_stub.py:240` | `test_engine_does_not_import_systems` green with the new ceiling; `test_partition_is_total` green | `sonnet` | `sonnet`: add a fake role targeting `systems.factions` in a scratch copy → ceiling must FAIL; remove one → must pass. Confirm the evacuation verdict is `keep`, not a coined word (§4) | executes the ruling's first half |

### WAVE 1 — the three producers (parallel worktrees)

| id | deliverable | §0.2 artifact | producer · why | antagonist brief | deps | moves |
|---|---|---|---|---|---|---|
| **1.1** | **R-09 — the margin producer.** One function in `shape.py`: `margin(w, act) -> {"net","ob"}` deriving pool from `Person.capability` via a new `verb_capability` roster (assumption-grade, swept), ob from `Act.obstacle` or the subject's score/2 (the 08-14 ruling), rolling `dice_engine.roll_pool(..., rng=random.Random(H(seed,tick,actor,act)))` — **threaded per §C.12 rejection 4, never global**. `_fold` grades through the existing `degree_of`. `contest()`'s `:6766` refusal becomes the non-combat path. | (a) the producer-scan test goes red **by design** and is rewritten to assert exactly one producer site; (b) two seeds → different degree histograms over ≥50 acts; same seed → same content hash; (c) **`mc_v18` goldens byte-identical** (the negative control) | `opus` — the capability→verb roster and contested-Ob derivation are competing-considerations design; the wiring is ~60 lines | `opus`: demand a cite or an `assumption` grade + sweep for every `verb_capability` cell; attack the seed for collision (two acts by one actor in one tick must draw differently — S33); attack S27.4 (an uncontested act with `obstacle=None` must hit the gate, never an Ob=0 roll) | 0.1, 0.4 | **R-09**; unblocks R-05b, R-08 |
| **1.2** | **R-03 — the scene-round tick.** `SeasonDriver.season` becomes `calendar → matter → for r in rounds: freeze → deliberate(ONE scene per person, View sees rounds < r) → resolve → witness → thaw → census`. Draw ordinal keyed by (tick, round). **No flag, no old path.** | `headless.py --case NPC-088 --seasons 2 --seed 0` shows per-round events; a planted round-1 deposit from `p_a` changes `p_b`'s round-2 candidate set against a control without it; `delta.py` records the hash move | `opus` — structural change to the driver against S26.2's freeze invariant and D-17/D-21 | `opus`: find any person-side read crossing a round boundary outside WITNESS; a person with budget 5 must get exactly 5 scene actions across rounds; two same-seed runs must hash identically; **a round counter stored on a carrier is D-21's fourth clock** | 0.1 | **R-03**; prerequisite of R-02 |
| **1.3** | **H-46 — the 13 and the 4.** `conviction_axes` → the registry's 13 convictions + 4 ethical axes (`descriptor_registry.yaml:235-258`), the 13×4 matrix (`:259`, PP-687) as a swept `assumption`; `align(verb, axis)` over the 4; author `alignment` for 32 verbs × 4 axes (sparse allowed, **no verb with zero cells**). Delete the 4-value stand-in. | loader raises on the old 4 names; `corpus_run` RANKING DISCRIMINATION moves off `2..7 of 22` (recorded, **not targeted**); `headless` still runs | `haiku` transcribes roster+matrix; `opus` authors the 128 cells — **this is game content, which is what freed capacity is for** | `opus`: every cell survives *"why this sign?"* against #353 §14 and the verb's `writes:`; any all-zero verb is reported (it can never discriminate); values trace to PP-687 or a grade — **never lifted from the retired `values_master`** | 0.1 | R-06 closer; prerequisite of R-08 |

### WAVE 2 — choice and consequence

| id | deliverable | §0.2 artifact | producer | antagonist brief | deps | moves |
|---|---|---|---|---|---|---|
| **2.1** | **R-08 — non-rational choice.** `choose` (`:3494`) ranks then samples softmax(score/τ) with the threaded RNG; τ a swept fixture; **τ→0 reproduces today's argmax as the control arm.** Ties no longer alphabetical. | same person/view, 20 seeds → ≥2 distinct top acts; τ=0 arm identical to HEAD; `corpus_run` DISTINCT EXECUTED SETS rises from 2 | `sonnet` — bounded single-scale reasoning | `sonnet`: the RNG must be the driver's (no `random.random()`); τ=0 must be byte-identical to the pre-change chooser; the sort key must still be deterministic *before* sampling | 1.1, 1.3 | **R-08** |
| **2.2** | **R-07 — W-F: outcome → `Person.stance`.** Degree-keyed interior writes through the existing `writes:` Degree column (H-62's supplied shape). `stance_toward` (`:3437`) finally gets a writer. | after `headless` 2 seasons ≥1 person has a nonzero `stance` row; 1.2's fork test now shows stance-driven divergence | `opus` — AX-3 drift risk | `opus`: stance must be per-referent rows, **never a summed field** (stored aggregate, D-8); no write outside the gate; sign conventions against #353 `:333` | 1.1, 1.2 | **R-07** |
| **2.3** | **R-05b — the social-contest seam.** `social_seam.py` (precedent: `combat_seam.py`): persons → `build_contest` → `resolve_contest` → degree via the kernel's own `DEGREE_ORDINAL`. Reuse the global-`random` reseed pattern (`scene_dispatch.py:297-303`). Add `contests:` to `petition`, `repudiate`, `speak`/`tell` where #353 contests them. `PATH_SEAM_ALLOWED` +1, declared. | a `petition` **in the corpus** emits `contest.resolved` with a kernel-read degree; same seed → same hash; the contested set moves off `{kill / wound}` | `opus` — persons→faculties/sides is design synthesis across the kernel's contract | `opus`: does every `Person` field the seam reads exist, or is a side fabricated? (combat_bridge's rule: **return the gap**); **any band computed in the seam rather than read is a second resolver**; attack the RNG restore | 1.1 | R-05 partial |
| **2.4 ×N** | **R-05a — the 20 dead verbs**, grouped by blocker (PLAN W31), one worktree per group: each gets a `requires_typed` cell or predicate, an effect, and a corpus execution. | `corpus_run` "20 have no predicate/effect" falls by the group size; each verb executes ≥1 time **in the corpus**, not only in a hand-built test | `sonnet` per group — table-driven | `sonnet` per group: an `effect` that special-cases a name is **scripting drift**; the verb's `writes:` must all be matrix rows; refusal emits `emits_on_refusal`, never raises | 0.1 (from day 1) | **R-05** at 32/32 |

### WAVE 3 — measure R-01 / R-02 (the gate on waves 1–2)

| id | deliverable | §0.2 artifact | producer | antagonist brief | deps |
|---|---|---|---|---|---|
| **3.1** | Re-run fork-and-follow (`wd_chunk.py` + `wd_collect.py`) **at the shipped fixture**. Flip R-01/R-02 only on the number. | reconvergence strictly < 100% at default; `observation_deposit_mode=none` control higher; `runs/wd_cells.json` committed | `sonnet` | `sonnet`: the fixture must be shipped defaults, **not the 2×1 cell**; `arm9_forking.fork_case` imported unmodified; **if reconvergence ≥ 96%, report which channel is still closed** | 1.1, 1.2, 2.1, 2.2 |
| **3.2** | **R-06 goals.** `ambitions(p)` Query over commit-Tenures to OUGHT propositions; W27 cast from the case. | DISTINCT EXECUTED SETS > 2; a case with 11 actors runs | `sonnet` | `sonnet`: no person-side read of world truth; `one_line` must be parsed, **not token-pattern-matched** (the W10 router lesson) | 1.3 |

### WAVE 4 — scale, the campaign artifact, the retirement

| id | deliverable | §0.2 artifact | producer | antagonist brief | deps |
|---|---|---|---|---|---|
| **4.1** | **R-04 — faction and world scale in the loop**, per `10_FACTIONS_AND_DEPLOYMENT.md` and PART D rows 1/14: a Faction is a type with **no verbs**; `holdings` is a Query over members' `hold` Tenures; seats act through `Act.via`. W28 re-scales the 44, rules the 10. | `corpus_run` unrepresentable scales → `{}` or world ≤ what W28 rules out; ≥1 faction-scale ARC ends; a `levy` executes through a seat | `opus` — the port of a SCALE, not a class | `opus`: **a stored L/Sta/Mil field, a faction passed where a PersonId is required, or a write by a banner is a REJECTION** (PART D 1/8/14); attack for `game_state` vocabulary leaking in | 2.4, 3.2 |
| **4.2** | **The season-loop campaign artifact:** N seasons over a multi-settlement realm, seeded hash pinned in `engine/season/tests`; the mass-battle seam lands here. **Replaces `mc_v18`'s goldens as the campaign control.** | a pinned hash in CI; a two-arm run (n≥30) showing the realm does not degenerate to one holder | `opus` for the mass-battle party derivation; `sonnet` for the harness | `opus`: as 2.3 for the mass seam; **attack the pin for being a golden with no control** | 4.1 |
| **4.3** | **Decision 1 step B.** One commit: fork the old driver, seven code subsystems, five doc-only ones, 46 tests, 19 tool readers. `FORK:` rows; `PATH_SEAM_ALLOWED` = `season/*`; `composition_roles` ≤ 8; `m1_acceptance` retargeted or retired. | CI green with `systems/ = {combat, social_contest, mass_battle}`; every retired path resolves via `pathres.fork_pointer()` | `sonnet` — mechanical under `evacuation_plan` | `sonnet`: `grep -rE "systems\.(factions|overview|…)"` over survivors → 0; `git cat-file -e` on 20 sampled fork pointers; the PR body must name §2's two held-back notifications | 4.2 |

**Critical path:** `0.1 → 1.1 → 2.3 → 3.1 → 4.1 → 4.2 → 4.3`, with `1.2` and `1.3 → 2.1 → 2.2`
merging at `3.1`, and `2.4` running beside everything from day one.

---

## §4a · THE SCALES OF PLAY — the roster this plan must accommodate (Jordan, 2026-09-05)

> *"we need to enable all scales of play that the game calls for, which includes character
> creation/development/chronicling, grand strategy politics, social contests/debates, mass
> battles/strategy warfare, personal combat/grid-based map combat with units,
> investigations/detective/interactive fiction"* — and, the same day, *"oh and management games and
> city builders. like, the repository outlines all of this pretty explicitly at the different
> scales. the proposal since it's becoming adopted now and real needs to accommodate it all."*

**THIS SECTION EXISTS BECAUSE THE PLAN'S §4 WAS SCOPED TOO NARROWLY AND WOULD HAVE DELIVERED A
ONE-SCALE GAME.** Wave 4's R-04 was framed as "faction and world scale" — two of seven. Work was
PAUSED mid-wave-1 to fix this rather than build further on it; the machine roster is
`engine/season/requirements.yaml`'s `scales:` block, and this section is what it means for the work.

### The seven, against what exists

| scale | subsystem(s) | retention | in the loop | the honest state |
|---|---|---|---|---|
| character creation / development / chronicling | `characters` (5 py), `npcs` (0 py, 19 md) | retire-set | **no** | `Person` holds convictions/beliefs/ledger/stance/capability and NOTHING creates or develops one. ⚠ `capability` is EMPTY on every corpus person |
| grand strategy politics | `factions` (18 py), `settlements`, `world` | retire-set | **no** | 44 of 143 cases unrepresentable at faction scale, 10 at world. `mc_v18` runs it; the loop does not |
| **settlement management / city building** | `settlements` (8 py), `overview` | retire-set | **no** | `domain_actions` and `settlement_economy` are BOTH `doc: null` — two of the nine unimplementable contracts. The loop has `Site`/`stores`/`condition`, no economy, no build, no domain action |
| social contests / debates | `social_contest` (21 py) | **RETAINED** | seam unbuilt | kernel is real and already rolls through the substrate. 1 of 32 verbs declares `contests:` |
| mass battles / strategy warfare | `mass_battle` (33 py) | **RETAINED** | seam unbuilt | wave 4 item 4.2 |
| personal combat / **grid-based map combat with units** | `combat/combat_engine_v1` (29 py) | **RETAINED, NOT DONE** | duel only | Jordan: *"combat engine isn't done."* The duel is a CONTINUOUS-RANGE two-party model; **grid/hex/tile combat with units EXISTS NOWHERE** — no such module in `systems/` or `engine/` |
| investigations / detective / interactive fiction | `fieldwork` (5 py, 19 md) | retire-set | **no** | six investigation acts, NONE declaring `contests:` — not ungraded, UNGRADEABLE |

**Three of seven are retained subsystems the loop cannot reach. Four map entirely to the retire
set.** That is the finding: "superseded by `engine/season/`" means the loop must EXPRESS the scale.
It never meant the scale goes away, and Step B cannot touch a subsystem whose scale the loop has not
subsumed.

### What canon already specifies, and the loop honours none of it

`systems/_architecture/scale_transitions_v30.md` (Status: **CANONICAL**) is the surface Jordan means
by *"the repository outlines all of this pretty explicitly"*:

- **§1 three modes** — TTRPG (scene-by-scene, rounds) · **Hybrid** (strategic layer + personal
  scenes via Zoom In/Out) · BG (faction Domain Actions, seasonal Accounting). The loop has one tick
  granularity and no zoom. **R-03's scene tick is the precondition of Hybrid mode**, not a local nicety.
- **§2 five scales** — Object · Personal · Relational · Territorial · Structural. ⚠ Its "Base Ob"
  column is **THREAD-ONLY and must be ignored as a general obstacle source** (Jordan, 2026-09-05).
  I misread it as R-09's Ob source and sent it to a live producer as canon before that correction —
  recorded here because the scoping was visible in the table's own sibling columns ("Min Thread
  Sensitivity", "Coherence auto-cost"). What survives is the SCALE SET: the loop's
  `person`/`realm`/`settlement` vocabulary is not canon's five and **no mapping exists**.
- **§3 eight handoff rules** — Personal→Thread, Personal→Faction, Personal→Scene (Contest),
  Scene→Faction (Domain Echo), Thread→Faction and three more. These are NERS **S**'s concrete tests
  (§0.06: *zooms out and in well across scales*, *transitions and sequences cleanly*). The loop
  implements none.

⚠ `systems/_architecture/` is in the retire set and holds ZERO `.py`. Step A's split kept it under
"the document IS the spec" — and this is the worked case for why that rule mattered: **the spec the
adopted system must satisfy lives in a tree the ruling marked superseded.**

### What this changes in the plan

1. **R-04 is not a wave-4 item. It is the plan's spine**, and 4.1 as written ("faction and world
   scale") covers two of seven. Wave 4 splits per scale, each with its own seam or its own
   authoring, and each gated on the loop's scale vocabulary being mapped onto canon's first.
2. **R-05's second clause is now answered.** *"Requires planning out all the different scales of
   play required in a season"* — this roster is that plan. The verb build-out is scoped BY it: a
   32-verb set serving one scale is not R-05 met.
3. **THREE ITEMS THE PLAN DID NOT HAVE, and one is not a seam at all.** Grid-based map combat with
   units is **unbuilt design**, not unwired code — it needs a design pass before any wiring item can
   exist, and it is the only scale in this table with nothing to point at. Settlement management /
   city building needs `domain_actions` and `settlement_economy` authored (both `doc: null`).
   Character creation/development needs W27's cast and a progression model.
4. **The eight handoffs are the S-axis acceptance test** and belong in the falsifiers, not as an
   afterthought.

⚠ **NOTHING ABOVE IS A LICENCE TO WRITE SEVEN DESIGN DOCUMENTS.** §0.2 still binds: a scale is done
when it EXECUTES in the loop. The roster is scope, not a deliverable — and §6's fourteen traps apply
to it exactly as they apply to everything else in this plan.

---

## §5 · THE FALSIFIERS (§0.1 pt 3 — named before the work, not after)

| wave | it failed if | control |
|---|---|---|
| 0 | `--requirements` or `--verify-citations` output changes for any reason but the four corrected sentences; net lines of `tools/` + `register.py` go **up** | `git diff --stat` |
| 1 | (1.1) two seeds give identical degree histograms, **or `engine/tests` goldens move**; (1.2) a planted round-1 deposit does not change a round-2 candidate set, or same-seed runs differ; (1.3) any verb has zero alignment cells | `mc_v18` goldens byte-identical is the negative control |
| 2 | executed-verb count and distinct-executed-sets do not **both** rise; `stance` still has zero writers after 2 seasons; the contested set is still `{kill / wound}` | HEAD's `results.json` via `delta.py` |
| 3 | reconvergence at the shipped fixture is still ≥ 96% — **then waves 1–2 opened nothing and R-01/R-02 stay `not_met`, honestly** | the `none` arm ≥ the default arm |
| 4 | a faction-scale case is still UNREPRESENTABLE; the campaign pin has no two-arm control; after 4.3 anything retained imports a forked module | `test_engine_does_not_import_systems` + `test_partition_is_total` |
| **the process** | in any wave, **more than half the diff lands outside** `engine/season/{shape.py, *_seam.py, *.yaml}` and `engine/season/tests/` — that is §0.3's 10.8:1 reappearing | `git diff --numstat <wave-base>..HEAD` bucketed by path |

---

## §6 · WHAT NOT TO DO — the apparatus this plan must not generate

§0.3 measured this repo's failure mode: 68% of tracked files machinery, commits 10.8:1
machinery-to-content in August. These are the specific traps *this* plan could fall into.

1. **A third seam bridging the two Worlds** (`campaign_seam.py`, default-OFF). The join is at the
   substrate by direct call; the driver is superseded, never bridged.
2. **Growing `register.py --requirements` into a measurer.** It is an index. The tests are the gate;
   a second `m1_acceptance` is the T3 generator in a new coat.
3. **A multi-file line-number citation checker, or fixing `LINEREF_RE`.** Item 0.1 removes the class;
   §0.1 pt 5 forbids the guard because the register is not a runtime input of the game.
4. **New `H-` rows for findings.** 113 → 150 is the loop's carrier in YAML. A wave may close rows,
   open one the code itself raises (`Unspecified` with a `site:`), or open a `needs_jordan`. Nothing else.
5. **A join document** (`architecture/meta/11_JOIN.md`). §C.12 and `10_FACTIONS` already say it.
6. **Re-pinning `mc_v18` goldens in waves 1–3.** They are the negative control. If they move, the
   season loop has leaked into the campaign RNG.
7. **Committing regenerated `runs/*.md` as evidence.** `results.json` + `TRACE.txt` through `delta.py`
   is the artifact; nine generated markdown files per commit is §0.3 by volume.
8. **Splitting the oversized `architecture/` docs.** Prose work, no game yield.
9. **Converting `engine/season` to dotted imports "while in there."** It moves no requirement.
10. **Adding `composition_roles` for the loop to reach `systems/`.** The loop's pattern is the
    declared shrink-only seam; roles are the old driver's mechanism.
11. **Building R-04 as a port of `game_state.Faction`.** PART D rows 1/8/14 reject it at review.
12. **A flag preserving the old path for scene-round ticking.** Replace the body; `delta.py` records
    the hash move. Flag-off is the trap by name.
13. **Coining a `retire-when` verdict** in `evacuation_plan.py`. `keep` plus a reason string is
    §4-compliant and needs no reader change.
14. **Parking the `verb_capability` roster or the alignment cells on Jordan.** Inject, declare
    `assumption`, sweep. Jordan changes cells; he does not author them.
