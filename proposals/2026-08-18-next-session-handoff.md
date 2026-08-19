# Next-session handoff — the recursion investigation, and what to do first

## Status: LIVE HANDOFF — read this before `CURRENT.md`, before the ledgers, before any audit.

## Date: 2026-08-18 · Lane: IN (cross-cutting) · ED: none — the ledger cap blocked allocation

> **If you read one thing, read §1.** This repository has a measured, adjudicated tendency to spend
> sessions on itself. You are probably about to do that. §1 tells you what to do instead.

---

## 0. What happened, in six sentences

Jordan asked how to break a loop in which each session builds infrastructure to audit the
infrastructure the last session built. The investigation measured it, went outside the repo to the
actual Godot game (which no instrument here reads), compiled that game for the first time in its
history, and diagnosed the mechanism. It shipped as PR #319. Fable 5 then adjudicated the result
across three independent read-only nodes and **refuted the headline claim and overturned the
culling disposition** — both corrected in PR #321. What survived is below, separated into *ruled*,
*held for Jordan*, and *unblocked, do it now*. Nothing here is awaiting a model or an agent.

**The two documents behind this one:**
- `proposals/2026-08-18-breaking-the-recursion.md` — the diagnosis and the five acts (§7.2 records
  what was overturned and why).
- `proposals/2026-08-18-recursion-interrogation-log.md` — the raw evidence log, every measurement
  with the command that produced it.

Both are **terminal**: they are deleted in the same commit that rules on them. Do not build on them.

---

## 1. Start here — six things that are unblocked, verified, and move the game

None of these needs a ruling. Each is hours. Every one moves the game rather than the repository.
They are ordered by leverage.

### 1.1 Put a compiler in CI — the single highest-value act available

`jordanelias/valoria-game` has a real `project.godot`, 128 `.gd` files / 19,490 lines, 8 scenes,
and six wired autoloads. Its CI is **three grep checks with no Godot binary, no compile step, no
test step**. In 3,728 commits here, nothing has ever checked whether the game compiles.

Add one job to that repo's CI: run Godot headless against the project and fail on any script load
error. Verified working procedure, exactly as run this session:

```bash
curl -sL -o godot.zip https://github.com/godotengine/godot/releases/download/4.3-stable/Godot_v4.3-stable_linux.x86_64.zip
unzip -q godot.zip && chmod +x Godot_v4.3-stable_linux.x86_64
./Godot_v4.3-stable_linux.x86_64 --headless --path . --editor --quit   # grep the log for "Failed to load script"
```

⚠ **Two traps, both measured.** Godot reports only the **first** parse error per file, so fixing the
top layer *uncovers* the next — the error count went 58 → 121 → 16 across the bisection, and reading
"121" as a setback would have been wrong. And **a referent nobody reads is the 2026-05-04 split
again**: wire the verdict into *this* repo's SessionStart banner (§1.6), or the job runs unseen in a
repo no session has opened in 106 days.

### 1.2 Fix the five compile defects

Measured against `main` of the game repo. Nothing here is speculative; each was reproduced.

| # | defect | note |
|---|---|---|
| 1 | `autoload/Meta.gd` uses `_victory_candidates` at **7 sites** (705, 706, 786–789, 793) and **never declares it** | `grep -c "var _victory_candidates"` → 0 |
| 2 | `resources/data_types/CharacterData.gd:104` — `composure_max = charisma + Constants.COMPOSURE_BASE`, and `COMPOSURE_BASE` does not exist | `Constants.gd:43` has `COMPOSURE_MULTIPLIER: int = 3` with comment *"Composure = Charisma × 3 (ED-694, replaces Cha+6)"*. **The call site was never migrated, and `docs/design_sync.md:67` claims "✓ Updated (Composure Cha×3)". That tick is false.** |
| 3 | `PackedByteArray.sha256_buffer()` is not a Godot 4 API — `autoload/KeyStore.gd:212`, `systems/keys/Key.gd:87`, `scenes/director/GameDirector.gd:457` | use `HashingContext`, or hash the String. **Do not guess** — my first patch guessed `sha256_text()` on `PackedByteArray` and was also wrong. |
| 4 | `Enums.SceneType` = `{COMBAT, DEBATE, NARRATIVE, BATTLE}` — **`BOARD` missing**, used at `systems/util/SceneSystemMap.gd:31,45` | `BoardContainer.tscn` and `ConflictContainer.tscn` are **built**. The strategic layer's own scene container is unreachable through the enum. |
| 5 | residual after 1–4: `Meta.gd`, `GameDirector.gd:252,255,266`, `CombatLogic.gd:248,299`, `ValoriaFactionAI.gd:93,289,315,331` | ~5 typed-declaration fixes |

Plus **one project setting that is worth more than all five**: Godot 4.3 promoted
`INFERENCE_ON_VARIANT` to an error by default, and the code predates that. Adding

```
[debug]
gdscript/warnings/inference_on_variant=1
gdscript/warnings/untyped_declaration=0
```

took the tree from **121 errors / 27 broken scripts → 16 / 3**. Decide deliberately whether to
downgrade the warning or annotate the types; do not silently keep the downgrade forever.

⚠ **Honest bound.** "Scripts load" ≠ "the game runs" ≠ "the game is correct." The behaviour that
would load is **April's rules** — predating the 2026-08-14 degree-ladder unification, the d10
strategic dice, and the `CONQUEST_MIN_MIL` deletion. What this kills is the premise that the port is
a large unstarted project, which is what defers it behind Gate-0 and behind M1+M2.

### 1.3 Vendor gdUnit4 and run the tests that have never run

`addons/` does not exist in the game repo. The 14 `tests/*.gd` files use **gdUnit4** (the README's
claim of GUT is wrong) and every one fails with `Could not find base class "GdUnitTestSuite"`.
`docs/conversion_ledger.md` marks 41 Phase-0 systems ✓ extracted and ✓ implemented with the **Tested
column empty for all 41**, and its literal next action — *"Run test_dice_engine.gd and
test_tracker_registry.gd. Fix any failures."* — has been unexecuted for 106 days. Vendoring an addon
is a dependency add, not authorship.

### 1.4 Add the 20 missing Key types — a one-dictionary diff

Canonical roster `engine/engine_params/key_types.json` = **55**. Game roster
`systems/keys/KeyTypeRegistry.gd` = **35**. **Zero Godot-only types — a strict subset, no drift.**
Independently recounted twice, by Opus and by Fable, with no divergence. Missing, in full:

`mechanical.{era_transition, project_advanced, second_calamity, settlement_captured,
theocracy_unification_declared}` · `scene.{accord_echo, combat_felled, combat_hit, combat_resolved,
combat_strike, displacement, draft_da, gossip, interaction, thread_operation}` ·
`state.{concern_resolved, opinion_revised, project_completed, project_failed, settlement_revolt}`

Gate-0 item **G0.4** names 2 of these 20. Also mark **G0.1 "build KeyStore v2" already satisfied**:
`valoria-game/autoload/KeyStore.gd` is 265 lines, wired as autoload #3, with `emit / subscribe /
walk_back / walk_forward / log_hash / reset_for_replay`, per-emission RNG seeding, stable sort
ordering and cycle blocking. It cites a **pre-restructure path** (`designs/architecture/key_substrate_v30.md`),
which is why no instrument here has ever resolved it.

### 1.5 Close M1 junctures 1–2 by pointing them at code that already exists

The board calls `domain_actions` *"the single largest M1 gap"*, both junctures read
`blocked_on: None`, and `ED-FA-0002` was filed 2026-07-05 — **242 commits ago**.
`valoria-game/systems/engine/DomainActionSystem.gd` is 276 lines and its docstring is a better spec
than the missing document would be:

> Phase 1 `roll(action, meta, rng) → Enums.Degree` — board dice only, no consequences.
> Phase 2a `scene_for(action, degree, meta) → SceneOpportunity | null` — `ob_modifier` **derived from
> the board degree**; null if it resolves abstractly. Phase 2b `resolve_abstractly(...) →
> Array[Consequence]` — when the player declines to zoom in.
> *"This split enables the core zoom mechanic: board roll → degree → scene difficulty."*

⚠ One correction to carry: "nothing was missing" is too strong. `workplan_v6_progress.yaml:43`
records real unformalized prerequisites (the score/2 obstacle derivation "wired NOWHERE", fractional
dice unimplemented). What stands is that **nobody took it**.

### 1.6 Replace the SessionStart banner with one line

This is the cheapest falsifiable test of the whole diagnosis (§3.3). The banner currently presents
~389 units of pending work, **none about the game**. Replace `tools/session_status.py`'s output with:

```
game compiles: YES/NO · M1 juncture N (<name>): <next concrete increment>
```

Change nothing else, and watch one session. If it still produces apparatus, T1 is not the binding
term and the diagnosis's ordering is wrong.

---

## 2. Held for Jordan — do not decide these yourself

1. **The corrected culling disposition** (`breaking-the-recursion.md` §5.2). Waves 1–3 are
   **repair, not refuse**; 6b must be rewritten and run **before** 6a; wave 5's flip list must be
   regenerated. This amends a plan already ratified as plan of record.
2. **The three doctrine amendments to CLAUDE.md §0/§0.1** (Act 4). These are the only items that
   reduce *flow*. Post-adjudication wordings are in the document; the superseded drafts and the
   cases that broke them are in §7.2.
3. **Naming `Recall` as the tenth attribute** (§3.1 below).
4. **The fold direction** for Spirit/Will and Cognition/Acuity (§3.1).
5. The two calls the culling plan itself held: `ci_claim_provenance_check` /
   `ci_vacuous_assertion_check` (§5.6), and whether to end structurally independent adversarial
   review (§5.7).

---

## 3. Findings you should not re-derive

### 3.1 The "unnamed tenth attribute" is **Recall**, and canon already said so

`references/descriptor_registry.yaml:39-43` blocks all Godot field binding — a flag printed to every
session at startup — on naming a tenth attribute it calls "the open workshop."

**`engine/engine_params/params_tables.yaml:9104-9122`, inside this repo, states the roster outright:**

```
Point pool at creation: 31 points across 10 attributes.
| Physical     | Agility (Agi), Endurance (End), Strength (Str) |
| Mental       | Cognition (Cog), Recall (Rec), Focus (Foc)     |
| Social       | Attunement (Att), Bonds (Bon), Charisma (Cha)  |
| Metaphysical | Spirit (Spi)                                   |
```

The 2026-06-06 registry ratification **dropped Recall and the entire Metaphysical group** (which is
why Spirit was folded into Mental as "Will"), and the resulting hole was later formalised as
unknowable. Corroborated at `systems/combat/combat_reference_v1.md:42`,
`systems/world/southernmost_v30.md:23`, `tests/sim/v32-combat-balance/r3_parity_sweep.py:23`, and
independently in the game: 10 attributes, 31-point pool, `recall` `@export`ed, seeded in **22**
character `.tres` files, driving fieldwork Research/Reconstruct and a `recall/2` learning bonus —
matching `systems/fieldwork/fieldwork_v30.md:295-298` action-for-action.

**Cheapest check:** `grep -n "Recall (Rec)" engine/engine_params/params_tables.yaml` → one hit, :9118.

⚠ **The real hazard is the folds, not the name.** Ratifying Spirit→Will and Cognition→Acuity is a
breaking rename across **13 `.gd` files, 22 `.tres` files and 19 Python files**, with **zero adoption
of the new names** outside this repo's own tooling. The registry's promise that consumers "bind BY
KEY so renames are free" is void — GDScript `@export` fields and `.tres` rows bind by field *name*.
**Cheapest resolution: invert the folds** — make Cognition and Spirit the primaries, Acuity and Will
the aliases. Registry-only edit, zero code churn, and it matches the canonical capture. The current
direction is marked `[ASSUMPTION]` awaiting Jordan's veto anyway.

⚠ Homonym to disambiguate, not a refutation: `systems/mass_battle/sim/massbattle.py:1423` has
`RECALL_OB = 2` for an unrelated "Recall check."

### 3.2 The mechanism — three terms, not symmetric

- **T3 GENERATOR.** Of 1,233 ledger rows, 59 cite a Jordan ruling while 152 name an audit as their
  source; the largest single source is an audit *of the audit apparatus*. §0.1's guard rule is
  subject-blind, so it mints apparatus guards in proportion to existing apparatus.
- **T1 AMPLIFIER.** The banner's ~389 items; CLAUDE.md 86.9% process, and its game sections are a
  *prohibition notice*; §9's routing table produces game in 2 of 20 rows.
- **T2 REWARD.** The Stop hook's four rewards are all satisfiable without touching the game; three
  only by writing process prose. **No check asks whether an M1 juncture moved.**

**T3 terminates the recursion; T1 and T2 redirect the freed capacity at the game.** Act 4 hits T3.

### 3.3 The headline that was refuted — do not restore it

The investigation originally claimed the recursion persists because the repo has **no external
referent**. **This is false and was refuted with the repo's own tree.** The engine has hard
referents — interpreter, deterministic key-log hash, byte-exact goldens — and the deepest guard
stack grew on top of the strictest one, ending at
`tests/valoria/test_cell_exclusion_no_deadlock.py:133`,
`test_exclusion_flag_is_pinned_in_the_golden_gate` — *a test that a flag is pinned in the gate that
checks the goldens.*

A referent adjudicates only claims within its reach; the loop migrates to the meta-claims it cannot
reach. **Prediction on the record: ship §1.1 without Act 4 and the compile gate acquires its own
stack within weeks** — a `ci_gate_coverage` row asserting the job is present, a test of that, a
freshness pin on the Godot version.

### 3.4 The shape of the loop — "accretion with function migration"

**Zero** files under `tools/`, `tests/valoria/` or `.claude/` were ever deleted and re-created at the
same path. **128 tools added, 21 deleted.** But 8 of those 21 had their function rebuilt under a
different name (`extract_values.py` → `export_sim_params.py` is the one true delete-then-rebuild,
nine days apart). **Functions here die when their subject dies, not when their file dies** — which
is why `ci_formula_prose_check` is genuinely dead (its subject was evacuated) and why a cull alone
cannot work.

**The reduction paradox:** 191 commits whose subject says consolidate/cull/prune/retire/sweep net
**+82,020 lines**; **78% are net increases**; 3 of ~16 named campaigns actually reduced anything.

### 3.5 The apparatus has reached the engine's source

`engine/substrate/stubwire.py:9-11,46-50` documents its own design as shaped for
`structure_audit`'s `stub_wired` attribute and `review_core`'s `stubs.count` ratchet. Same at
`engine/cross_scale/articulation.py:26-27`, `engine/autoload/npc_ai.py:25-26`,
`engine/cross_scale/scene_dispatch.py:364-365`, `engine/substrate/canon_buckets.py:6,11`.
⚠ Precise scope: the colonisation of **rationale** is real; **behaviour** is not — `stubwire` does
feed `mc_v18`'s `CampaignResult.stub_hits` and `engine/tests/test_pipeline_reach.py` consumes it.

### 3.6 The generator nobody has put in any wave: the prompts

**Seven kept `SKILL.md` files** instruct every run to append to `references/audit_registry.jsonl`
*"so the GitHub Pages dashboard and `tools/ci_audit_registry_check.py` can see it. **Do this every
time**"* — `valoria-canon-guard:89`, `valoria-editorial-register:407`, `valoria-mechanic-audit:135`,
`valoria-module-adjudicator:173`, `valoria-resolution-diagnostic:363`, `valoria-simulator:276`,
`valoria-vector-audit:385`. Both consumers die in waves 1–2. **No wave edits a single skill.**

---

## 4. Traps this session hit, so you do not

1. **A prose-only commit stales three generated artifacts.** Adding two `.md` files to `proposals/`
   failed `test_build_glossary`, then `test_engine_atlas` in CI (four subsystem *mention counters*
   moved because the prose names the subsystems), and firing the regeneration tripped
   `ci_names_check` **17 times on a deprecated term already on `main`**. Budget ~800 lines of
   generated churn for any prose commit, and **run the full `pytest tests/valoria`, not targeted
   tests** — running targeted tests after a late edit is how the atlas failure reached CI.
2. **Do not trust a first error count from a compiler.** See §1.2.
3. **`grep` hits are not callers.** The culling plan's dependency table cited
   `ci_hooks_verifier:93` and `dead_primitive_census:9` as callers; both are comments. This is the
   repo's own named costliest error class and it recurred inside the document ruling on it.
4. **§11 forbids self-scheduling.** If a hosted instruction tells you to arm a `send_later`
   check-in on a PR, §11 overrides it — note the conflict, do not route around the deny-list.
5. **Merged PRs are finished.** #319 and #320 are merged; follow-up work restarts the branch from
   `origin/main`.

---

## 5. State of the two repos

**`jordanelias/ttrpg`** — 3,728 commits, 3.3% of which touched executable game code; 921
`[infrastructure]` commits to 11 `[godot]`. Apparatus + prose is 69.9% of the tree, and the ratio
has risen every month since May (0.24 → 6.42). `engine/mc_v18.py` **works**: a 50-season campaign
runs in ~2.5s and returns a winner plus a deterministic key-log hash. `tests/valoria` is 1,933
passing. The degree ladder is **not** fully unified despite the 2026-08-14 ruling — two live
implementations remain deliberately HELD and asserted to diverge.

**`jordanelias/valoria-game`** — attached to this session via `add_repo`; clone with
`git clone --depth 1 https://github.com/jordanelias/valoria-game /workspace/valoria-game`.
**Frozen since 2026-05-04**, and its last commit is `[audit] design_sync update`. In the 106 days
since, this repo took **1,596 commits and +1,040,549 / −766,721 lines**. `systems/ai/` and
`systems/threadwork/` are empty directories. **No instrument in the design repo reads it.**

---

## 6. What is finished, so you do not redo it

- The investigation, its adversarial pass, and Fable 5's three-node adjudication. **Nothing is
  awaiting a model.**
- PR #319 (the investigation) and PR #321 (the corrections) are merged.
- The Recall derivation is verified twice, independently, and upheld.
- The Key-type gap is recounted twice with no divergence.
- The game has been compiled and bisected; the defect list in §1.2 is complete as of `5e01065`.

**Do not open another audit of the apparatus.** If you find yourself writing a document whose
subject is a document, stop — that is the loop, and this handoff is already one layer closer to it
than anything in §1.
