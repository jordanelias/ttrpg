# Interrogation working log — "how do we break the infrastructure recursion?"

## Status: REFERENCE — raw evidence log for `2026-08-18-breaking-the-recursion.md`. Delete with it.

## Date: 2026-08-18 · Lane: IN (cross-cutting) · ED: none — the ledger cap blocked allocation

> **Why this file exists and why it is not more apparatus.** The session was asked to run its
> orchestration and interrogation on Fable 5; both Fable agents terminated on an account usage limit
> and the work was re-run on Opus 5. This is the verbatim evidence log so Fable can resume by
> *adjudicating* rather than re-deriving — every measurement carries its command, every agent finding
> is recorded including the ones that refuted my own claims. It is a scratch artifact with a stated
> death date: **it is deleted in the same commit as the proposal it supports, once that proposal is
> ruled.** It does not get a register row, a freshness gate, or a test.

---

## Executed on: Opus 5 (claude-opus-5). REASON: Fable 5 usage limit hit on first dispatch.
## INTENT: hand back to Fable 5 when usage returns. Everything below is the state Fable needs.

### Fable-5 resumption contract
Two agents were dispatched to Fable 5 and terminated on `You've reached your Fable 5 limit`
before producing output. They were relaunched on Opus. When Fable 5 usage returns, re-run
these two nodes on Fable and diff against the Opus findings recorded here:

- NODE F1 — causal-mechanism interrogation (prompt archived below, §P1)
- NODE F2 — adversarial attack on `proposals/2026-08-18-culling-plan-v1.md` (prompt §P2,
  run as subagent_type `valoria-critic` for structural read-only independence)

Opus results for both are recorded verbatim in §R. Fable's job on resumption is NOT to redo
the retrieval — it is to adjudicate: confirm, refute, or sharpen the Opus diagnosis, and rule
on the open questions in §Q.

---

## §M — Direct measurements taken by the orchestrator (not delegated)

| measurement | value | command |
|---|---|---|
| CLAUDE.md size | 70,349 chars / 658 lines | `wc -c -l CLAUDE.md` |
| CLAUDE.md size as stated *inside* CLAUDE.md §11 | 48,612 chars | quoted in §11's token-bleed math |
| → governing doc has grown **+44.7%** past its own audited figure | | |
| CLAUDE.md growth curve | 469 (2026-06-22) → 19,744 (07-02) → 32,013 (07-16) → 40,464 (07-17) → 49,396 (07-26) → 56,384 (08-05) → 70,349 (08-17) | `git log --format=%H -- CLAUDE.md` + `git show $sha:CLAUDE.md \| wc -c` |
| tools/ python modules | 107 (72 at top level) | `find tools -name '*.py' \| wc -l` |
| tools/ LOC | 29,106 | `find tools -name '*.py' \| xargs wc -l` |
| game code LOC (engine/ + systems/) | 33,235 | `find engine systems -name '*.py' \| xargs wc -l` |
| **tools LOC : game LOC** | **0.88 : 1** | — |
| tests/valoria files | 168 | `ls tests/valoria/*.py \| wc -l` |
| skills | 13 | `ls skills/` |

### CLAUDE.md section budget (chars) — what the governing doc spends attention on
| section | chars | subject |
|---|---:|---|
| §3 Repository map | 16,028 | repo's own history/structure |
| §10 Model tiering | 9,318 | agent orchestration |
| §4 Conventions | 8,602 | process |
| §0 How we work | 6,746 | process |
| §8 Enforcement | 6,568 | apparatus |
| §5 Data→Godot | 3,888 | **game-adjacent** |
| §9 Task routing | 3,679 | apparatus |
| §11 No self-scheduling | 3,438 | process |
| §6 Godot port | 2,885 | **game-adjacent** |
| §1 Currency | 2,611 | process |
| §2 How repo is worked | 2,279 | process |
| §7 Sim/balance | 2,151 | **game-adjacent** |
| §5-7 restore banner | 847 | process |
| **GAME-adjacent total** | **8,924 (12.7%)** | |
| **PROCESS/APPARATUS total** | **61,425 (87.3%)** | |

FINDING M1: the single document every session is forced to read spends 87% of its budget on
the repo's own machinery. Zero sections describe the game's design, fiction, or mechanics.
The three "game" sections are all about *how to safely read numbers out of the apparatus*.

---

## §R — Agent results (appended as they land)

### M2 — the immediate predecessor commit, read directly
`audit/2026-08-17-weekly-review/00_findings.md` (471 lines) + `01_consolidation.md` (484 lines).
19 findings (F1–F19), 5 throughlines (TL-1..TL-5).

**Decisive quote, TL-5 (`00_findings.md:172`):** the week produced
> "the week's only finding that is about the game rather than the repository"

i.e. **1 of 19 findings had the game as its subject.** That finding: *"Valoria has a complete,
numerate engine for characters and factions getting **worse**, and no engine for them getting
**better**."* — the actual game-design hole, surfaced once, as a by-product.

**TL-3 (`00_findings.md:134`) names the real constraint and is the strongest evidence in the tree:**
the 2026-08-14 batched ruling session closed ten calls in one sitting and was "the highest-leverage
act of the week by a wide margin." Of those ten rulings: **4 executed, 1 part-built, 5 not started.**
Two ruled 2026-08-15 are still unexecuted at HEAD. Verdict recorded in the tree itself:
> "rulings are being produced faster than they are propagated into the registers that carry them"

**TL-1's headline was refuted by its own consolidation pass** (`01_consolidation.md §1.1`):
"the great majority is apparatus" was FALSE — measured, 53.8% of the week's churn is
machine-generated artifacts and `references/glossary/glossary.json` alone is **44.5% of the entire
week's diff**, rewritten in 8 of 15 commits. NOTE FOR FABLE: this is a *different and worse* finding
than the one it corrected — the diffstat is not measuring work at all.

**F11 / culling-plan header:** `registers/editorial_ledger_in.jsonl` has ~108 tokens of headroom
under a **blocking** cap. The ledger that records the work is now too full to record the work.
The culling plan could not allocate itself an ED number. This is the mechanism eating itself.

### M3 — commit-attention census (whole history, orchestrator-measured)

| surface touched | commits | ratio vs game code |
|---|---:|---:|
| **total commits** | 3,728 | — |
| executable game code (`engine/`, `sim/`, `systems/*/sim/`, `combat_engine_v1/`) | **123** | **1.0× (3.3% of all commits)** |
| `tools/` | 179 | 1.5× |
| `audit/` | 570 | 4.6× |
| `registers/` + `references/` + `canon/` + HANDOFF + CURRENT + workplans + proposals | **1,341** | **10.9×** |

Commands: `git log --oneline -- <paths> | wc -l`.

### M4 — the tool ratchet, measured
- `tools/*.py` files **ever created: 128**. **Ever deleted: 21.** Net 107 — exactly the live count.
- Deletion rate across the repo's entire life: **16%**.
- Per-month creations: 03:5 · 04:16 · 05:6 · 06:18 · **07:67** · 08:16. Deletions: 04:1 · 05:1 · 07:14 · 08:5.

**IMPORTANT NUANCE / CORRECTION TO THE USER'S FRAMING — Fable should adjudicate this.**
`comm -12` of (tools ever deleted) ∩ (tools live now) is **EMPTY**. No tool has been deleted and
then re-created at the same path. So the loop is **not** literally "rebuild the thing the last agent
tore down." The actual mechanism is **monotonic layer accretion**: each session leaves the previous
layer standing and adds a *new layer above it* that observes it. The demolitions (21 files) are real
but rare; the recursion is in the *stack height*, not in the churn. The culling plan's own measured
"worst chain is five layers deep" is the correct description; "build/demolish cycle" is the
felt experience of a monotonically deepening stack, not a literal oscillation.
This matters because it changes the cure: a *cull* attacks the wrong axis. You cannot fix an
accretion problem with a one-time subtraction — you fix it by removing the thing that makes the
next layer the obvious move.

## §R1 — GODOT READINESS (agent, sonnet, completed)

**THE SINGLE MOST IMPORTANT POSITIVE FINDING IN THIS ENTIRE INVESTIGATION:**
`engine/mc_v18.py` was executed live. `run_campaign(seed=1, max_seasons=2)` **completed in 2.47s**,
ran to season 50, produced 35 battles, 168 scenes resolved, **217 Keys emitted**, full faction /
territory / settlement state with 37 named settlements. `tests/valoria` collects 1,971 tests in 3s.
**The game simulation is real, deterministic, and runs end to end today.**
(Anomaly to chase: `max_seasons=2` did not truncate — ran to 50 regardless. Possible dead parameter.)

**THE SINGLE MOST IMPORTANT NEGATIVE FINDING:**
- `project.godot` files in the tree: **0**
- `.tscn` scene files: **0**
- `.gd` scripts: **8** (all in `godot/skeleton/`), `.tres`: 12
- The 8 `.gd` files `extends` `BaseEngine` / `EngineModule`; grep for `class_name` across the whole
  repo finds **8 declarations, all the skeleton's own**. `BaseEngine`, `EngineModule`, `Key`,
  `KeyBus`, `GameState`, `Resolver` are **defined nowhere in this checkout.**
- **`godot open` fails immediately** — no project.godot. There is no Godot project. There never was.
- 1 of 27 modules (personal_combat) has any port at all.
- Gate-0 (G0.1–G0.5): **0 of 5 executed.** Strategy doc still `PROPOSED`, 8 `[OPEN — Jordan]` items.
- The real Godot implementation lives in a **separate repo `valoria-game`, frozen since 2026-05-04** —
  i.e. **106 days frozen** as of today.

**Engine inventory (measured):** `engine/` 27 files / 8,047 LOC. `combat_engine_v1` + `combat/sim`
27 files / **8,220 LOC, zero `NotImplementedError`** — the deepest, cleanest module.
`social_contest/sim` 7,045 · `factions/sim` 2,666 (6 files with `NotImplementedError`) ·
`mass_battle/sim` 2,398 · `threadwork/sim` 1,405 · `settlements` 1,012 · `world` 739 · `overview` 591 ·
`characters` 549 · `fieldwork` 497. Repo-wide: 21 files with `NotImplementedError`, 39 with stub markers.

**Typed data layer is FURTHER ALONG than CLAUDE.md §5 admits.** `engine/engine_params/sim_params.json`
= **323 typed computational constants**, AST-extracted, round-trip-checked. But its own
`citation_coverage`: **83/323 (25.7%) cited to canon; 240 (74.3%) uncited, 8 assumption-grade.**
And **zero `.tres`/`.tscn` consume any of these JSON files** — the export half exists, the ingest half
does not.

**`module_contracts.yaml`:** 27 modules · **9** `doc: null` (CLAUDE.md says 10 — stale by one) ·
**11** `[ASSUMPTION]`-grade resolvers. `engine_clock`, the temporal spine, is one of the `doc: null` nine.

**M1 "one playable season" — 0 of 7 junctures DONE** (board `as_of` 2026-08-14):
1 strategic decision `not_started` (blocked: `domain_actions` doc doesn't exist — "single largest M1 gap")
2 domain action `not_started` (same gap) · 3 social contest `in_progress` (3 needs-Jordan) ·
4 personal combat `in_progress` · 5 thread operation `in_progress` ·
6 season close **`blocked` on ED-1051 (engine_clock ratification)** · 7 articulation render `in_progress`.
M3 (Godot vertical slice) — all three stages `blocked`, and sequenced to start only after M1+M2 close.
Single T0 blocker for the whole game: **ED-1051, engine_clock**.

**THE BOARD INDICTS ITSELF — quote it to Jordan verbatim:**
> "IN owns 3 of 7 outright (2, 6, 7) and gates a 4th... That is the structural reason M1 sat at 0/7
> through a month in which IN shipped infrastructure: **the lane that owes M1 the most was spending
> itself elsewhere.**"

## §R2 — THE GAME REPO EXISTS AND IS SUBSTANTIAL (orchestrator, direct clone)

`jordanelias/valoria-game` was cloned and inspected directly. **This changes the whole question.**
CLAUDE.md describes it in one line as "separate clone, frozen since 2026-05-04" and nothing in the
design repo's ~338,000 lines of apparatus measures its contents.

**What is actually in it:**
- `project.godot` — real, `config/name="Valoria"`, `run/main_scene="res://scenes/Main.tscn"`, Godot 4.3 features
- **128 `.gd` files, 19,490 lines of GDScript**
- **8 `.tscn` scenes**: `Main`, and six containers — `BoardContainer`, `CombatContainer`,
  `ConflictContainer`, `NarrativeContainer`, `DebateContainer`, `BattleContainer` — plus `WhyDiagnostic`
- **37 `.tres` resources**
- **6 wired autoloads with a documented load-order dependency chain**:
  `Meta` (877 lines, all persistent state) · `EventBus` (107) · **`KeyStore` (265) — "PP-687 universal
  Key substrate (canonical 2026-05-01)"** · `SceneTimer` (353) · `GameStateMachine` (149) ·
  `GameDirector` (season loop, zoom stack, container host)
- `systems/`: engine 2,731 · articulation 1,747 · faction_v30 910 · util 723 · npc 705 ·
  registries 601 · data 597 · faction 581 · keys 343 · situation 321 · trackers 305 ·
  resolution_modes 150 · diagnostics 138 · context 59 · transition 49. **Empty: `ai/`, `threadwork/`.**
- **14 GUT test files** incl. `test_dice_engine.gd`, `test_season_loop.gd`, `test_keystore.gd`,
  `test_integration.gd`, `test_faction_v30.gd`, `test_articulation_v30.gd`
- `.github/workflows/godot-ci.yml` — it has its own CI
- `docs/`: `architecture.md`, `key_substrate.md`, `conversion_ledger.md`, `design_sync.md`,
  `trigger_catalogue.md`

**`docs/conversion_ledger.md` — Phase 0 COMPLETE, Phase 1 COMPLETE, Phase 2 (Combat Container) partial.**
41 Phase-0 systems marked ✓ extracted + ✓ implemented; the **Tested column is empty for all 41**.
Its literal **"Next action:" is: *"Run test_dice_engine.gd and test_tracker_registry.gd. Fix any
failures. Then Phase 1."*** That instruction has been sitting unexecuted for 106 days.

**THE CLOSING EVIDENCE — the last commit ever made to the actual game:**
```
5e01065 [audit] design_sync update — 2026-05-04 audit vs ttrpg HEAD 9057663f
```
**The final act on the game before 106 days of silence was an audit of the game against the design
repo.** The recursion did not begin in the design repo and spread. It began by consuming the game.

**The measured opportunity cost, 2026-05-04 → 2026-08-18 (106 days):**
| | valoria-game (the game) | ttrpg (the design repo) |
|---|---:|---:|
| commits | **0** | **1,596** |
| lines changed | **0** | **+1,040,549 / −766,721** |

**Drift already visible and cheap to fix:** README says "Godot 4.6+", `project.godot` declares 4.3
features. `godot/skeleton/` in ttrpg re-implements `CombatEngine`/`StrikeModule` against
`BaseEngine`/`EngineModule` — classes that **do not exist in either repo** — while
`valoria-game/systems/engine/` (2,731 lines) already has a working `CoreEngine`/`CoreResolver`/
`ResolutionMode` hierarchy. **The ttrpg skeleton is a non-compiling re-draft of code that already
compiles 500 metres away.** This is the recursion in its purest observable form.

## §R3 — ⭐ THE HEADLINE: THE "UNNAMED TENTH ATTRIBUTE" IS **RECALL**, AND IT SHIPPED IN APRIL

This is the single highest-value output of the investigation, and it is a **derivation, not a guess.**

**The design repo's blocking state** — `references/descriptor_registry.yaml:39-43`:
> ⚠ THE COUNT IS RULED; THE ROSTER IS NOT COMPLETE. Jordan, 2026-08-14: "it will be 10 attributes".
> NINE are defined below. **The TENTH IS UNNAMED — naming it is the open workshop**, and it is the
> ONLY thing still open about the count. Do not infer the tenth from the aliases: Spirit folds to
> Will and Perception folds to Attunement by the rows below, so neither is a candidate slot.
> **Until the tenth is named, "IN FLUX" stays and Godot fields stay unbound (CLAUDE.md §5).**

This flag is echoed in the SessionStart banner *every session* ("schema: descriptor roster IN FLUX —
do not bind Godot fields yet") and in CLAUDE.md §5. **It is the standing reason Godot binding is
blocked.**

**The game already answered it.** `valoria-game/scenes/character_creation/CharacterCreationManager.gd:146-151`
allocates 31 points across ten named attributes:
`agility · endurance · strength · cognition · recall · focus · attunement · bonds · charisma · spirit`

**Set difference, applying the registry's own alias rules** (Cognition→Acuity, Spirit→Will):
| game attribute | registry row |
|---|---|
| strength / endurance / agility | `attr.body.*` — identical |
| cognition | `attr.mind.acuity` (alias `Cognition`) |
| focus | `attr.mind.focus` |
| spirit | `attr.mind.will` (alias `Spirit`) |
| attunement / charisma / bonds | `attr.social.*` |
| **recall** | **NO ROW EXISTS** |

Nine map exactly. **The unmatched tenth is `recall`.** It is not excluded by the registry's own
warning (that warning rules out Spirit and Perception; Recall is neither).

**And it is not a stub — it is load-bearing, seeded, and validated (19 references):**
- `resources/data_types/CharacterData.gd:18` — `@export var recall: int = 1`
- `CharacterData.gd:61-68` — `effective_recall(coherence_state)`, with −1D/−2D coherence degradation
- `systems/engine/InvestigationSystem.gd:88,97` — `ctx.base_pool = character.recall` (**it is the
  investigation dice pool**)
- `systems/engine/SkillSparkingSystem.gd:125` — `recall / 2` learning bonus
- `CharacterCreationManager.gd:200` — validates History `dice_bonus ≤ recall`
- `ValoriaDataLibrary.gd:225` — the "Scholar" history tags `["scholarly","cognition","recall"]`
- Seeded in named-character `.tres`: `prudence_cardinal=5`, `peder_almstedt=5`, `doux_laskaris=4`,
  `maret_vossen=3`, `maret_uln=3`, `dalla_virke=3`

**THE FINDING, STATED PLAINLY:** the design repo has held a blocking flag on all Godot field
binding — the flag printed to every session at startup — waiting to name a tenth attribute that has
been implemented, exported, seeded across named NPCs, wired into two systems and validated in the
character creator **since April, in the repo the design exists to serve.**

**Corollary defect (secondary, but real):** the registry *folded* Spirit→Will and Cognition→Acuity.
The game treats `spirit` and `cognition` as distinct live fields. If the fold is ratified, it is a
**breaking rename against shipped Godot code and shipped `.tres` data.** Nothing in the design repo's
338,000 lines of apparatus noticed, because **no instrument in it reads the game repo.**

## §R4 — PRIOR-ATTEMPT AUDIT (agent, sonnet, completed)

**Jordan has given this same instruction FOUR times. Today is the fourth.**
| date | source | quote |
|---|---|---|
| 2026-08-04 | ED-IN-0139 | "params .md are largely useless at this point and I want them gone. **code should have superseded them all by now**" |
| 2026-08-04 | fork-inversion entry | "our fork is going to hold all the outdated largely-prose work that contaminates our code-based work" |
| 2026-08-11 | ED-IN-0159 | "make this project as lean as possible without sacrificing mechanisms… **my concern is with code**" |
| 2026-08-18 | ED-IN-0194 (today) | "if it isn't a primary guardrail, then it's likely useless" · "We need as little as possible" |

**It has never stuck, and the failure is measurable at each interval:**
- 07-15 `obs_core.py` was built explicitly to end duplication (single-owner). By 08-11 it had been
  adopted by **9 of 118 modules (8%)**.
- 08-04 → 08-11 (7 days): the leanness ruling produced an **audit document**, status line
  *"nothing ruled, nothing executed."*
- Its execution commit `ed7d0fd` — shipped under the banner of executing the leanness plan —
  **net-ADDED 3,448 lines.**
- 08-11 → 08-18 (7 days): `tools/` grew 129→130 files, 4,187,573→4,203,761 bytes;
  **CLAUDE.md grew 61,367 → 70,349 bytes** *in the week whose theme was leanness.*
- Earlier precedent, 2026-06-12 `3b503788`: a size **guardrail was widened** 9000→12000 to
  accommodate growth rather than the growth being cut. Seven weeks before the first "lean" ruling.
- As of HEAD, the culling plan ratified today has executed **0 of 6 waves.**

**Open IN-lane ledger items: 46 open of 56.** By subject: **17 game/design (37%) · 29 apparatus (63%).**
Several open apparatus items are themselves layer-3 by the culling plan's own rule:
ED-IN-0071 (the restructure), ED-IN-0079/0103 (centralization programs), ED-IN-0091 (a register of
the repo's own code shape), ED-IN-0159 (the leanness scoping directive), ED-IN-0124 (a Fable-5
steelman *of a plan*), ED-IN-0153 (a methodology record *for an audit's methodology*).

**Unit-mismatch defect found in the setup commit itself:** `HANDOFF_IN.md` is **291,396 bytes**;
the commit describing it cited "3,485" (that is lines). A measurement-discipline error inside the
commit whose subject is measurement discipline.

## §R5 — GAME-CODE SHAPE (agent, sonnet, completed)

**Measurement dispute — FLAG FOR FABLE:** agent measured **44,502 LOC / 170 files** for game code
(engine 8,047 · systems/*/sim 17,212 · combat_engine_v1 7,901 · tests/sim/mass_battle 11,342).
Excluding tests/workbench → ~37,100. **It could find no subset that lands on the culling plan's
29,570.** The plan's headline number is unreproducible.

**Structure (repo's own 2026-08-17 audit):** 273 modules · 419 import edges · **3 import cycles** ·
20 cut-vertices · 63 orphans. Top cut-vertex `engine.autoload.game_state` (in 10 / out 11).
**105 lazy function-level imports** used to dodge cycles — including a genuine bidirectional
cross-subsystem cycle (`fieldwork/sim/knots.py:349,364` ↔ `threadwork/sim/opposing.py:238,245`)
that is invisible to the cycle scanner *because both directions are deferred*, and is wrapped in
`try/except (ImportError, AttributeError): pass` — so a Conviction scar or Coherence delta
**silently no-ops** if the import ever fails.

**The degree ladder is NOT unified, despite the 2026-08-14 ruling.** Honest count post-`9933ff2`:
1 owner (`engine/autoload/dice_engine.py:104`) + 5 verified twins + **2 permanently HELD, live,
diverging implementations** + 5 frozen historical copies ≈ **13 pieces of ladder logic**.
The two divergent ones are the two that matter most: `combat_engine_v1/core.py:57` (personal combat)
and `engine/autoload/sigma_leverage.py:292`. `roll_pool` is independently defined **3 times**.

**Constants are NOT centralized.** 443 module-level `ALL_CAPS = <number>` definitions across 152
non-test game files. Only 8 files reference `engine_params` at all; only **2 load JSON at runtime**.
Every gameplay constant is hand-transcribed Python with a citation comment.

**Godot portability, measured:**
- numpy: 5 files, **all in `workbench/`** (dev harness) — runtime engine is numpy-free. GOOD.
- `@dataclass`: 51 files. **combat_engine_v1 uses ZERO** — plain classes, the most portable shape.
- No metaclasses, no multiple inheritance. GOOD.
- **852 free functions vs 309 methods (73% free). 84 of 142 files define zero classes.**
  ← **the single biggest port mismatch**: GDScript has no module-level function concept.
- `getattr`/`setattr`: 241 occurrences needing per-site review.
- `combat_engine_v1/` is **not a Python package** — every file does `sys.path.insert(...)` and
  imports siblings bare. Invisible to the import scanner (hence most of the 63 "orphans").

**⭐ THE KEY SUBSTRATE INVERSION — cross-reference with §R2, this is a major finding:**
`engine/substrate/keys.py` (601 lines) is good code, but **only 3 files in the whole game code ever
instantiate a `Key`**, and `grep -rn "KeyBus\|class KeyStore"` over the Python returns **ZERO hits.**
The 24 files importing `engine.substrate` are importing **`stubwire`** (a marker for "not built"),
not `keys`. The Python reference is a **call-graph, not an event-bus graph.**
**Meanwhile `valoria-game/autoload/KeyStore.gd` (265 lines) IS a working Key substrate, wired as
autoload #3, with `tests/test_keystore.gd`.** ⇒ The design repo has spent months specifying a
substrate that **the Godot repo already implemented and the Python reference never adopted.**
The `godot/skeleton/` in ttrpg was "speculatively designed to the *intended* Key-bus architecture,
not reverse-engineered from the actual reference" — and both are downstream of a real one that exists.

**Personal-combat slice port assessment:** authoritative source `combat_engine_v1/` = **5,847 LOC /
15 core files**. Existing skeleton = 155 lines ⇒ **<3% ported**, and against the wrong architecture.
Blockers: (1) sys.path hacking, not a package; (2) `core.py:57`'s ladder is *known* to disagree with
the ruled owner and is HELD because damage constants were calibrated to the old bands — moving it
flips guandao armour-defeat 2.5%→47.5%; (3) architecture reconciliation, not translation.

## §R6 — ⭐ SECOND HEADLINE: THE "SINGLE LARGEST M1 GAP" IS ALREADY IMPLEMENTED IN GODOT

ttrpg's M1 board: **junctures 1 AND 2 `not_started`**, blocker recorded as
*"the `domain_actions` design doc doesn't exist — **the single largest M1 gap**"*, and
`domain_actions` is one of the 9 `doc: null` rows in `module_contracts.yaml`.
`HANDOFF_IN.md`'s top open item and the SessionStart banner's "next" both point at it:
*"M1 Strategic decision: author the domain_actions home (ED-FA-0002)"*.

**`valoria-game/systems/engine/DomainActionSystem.gd` — 276 lines, `class_name DomainActionSystem`,
already implements it**, and its module docstring is a cleaner spec than the missing doc would be:
> Phase 1 — `roll(action, meta, rng) → int (Enums.Degree)` — rolls the board dice only, no consequences
> Phase 2a — `scene_for(action, degree, meta) → SceneOpportunity | null` — builds the SceneOpportunity
>   with typed SceneContext and `ob_modifier` **derived from the board degree**; null if it resolves abstractly
> Phase 2b — `resolve_abstractly(action, degree, meta) → Array[Consequence]` — used when the player
>   declines to zoom in
> **"This split enables the core zoom mechanic: board roll → degree → scene difficulty."**

That is the strategic↔personal bridge — the thing Valoria *is* — working, in GDScript, since April.
It is consumed by `FactionTurnSystem.gd`, `ValoriaFactionAI.gd`, `GameDirector.gd` (584 lines),
`DebateContainer.gd`, `BattleContainer.gd`, `SceneOpportunity.gd`, `AccordEffects.gd`.

## §R7 — ⭐ THIRD HEADLINE: THE KEY-TYPE GAP IS EXACTLY 20 ROWS, AND THEY ARE NAMEABLE TODAY

Measured both rosters directly.
- ttrpg canonical: `engine/engine_params/key_types.json`, `type_count: 55`, generated from
  `systems/_architecture/key_type_registry_v30.md`
- Godot live: `valoria-game/systems/keys/KeyTypeRegistry.gd` — **35 types**
- **In Godot but not canonical: ZERO.** The Godot roster is a strict, clean subset. **No drift.**
- **Missing exactly 20**, and here they are:
  `mechanical.{era_transition, project_advanced, second_calamity, settlement_captured,
  theocracy_unification_declared}` · `scene.{accord_echo, combat_felled, combat_hit, combat_resolved,
  combat_strike, displacement, draft_da, gossip, interaction, thread_operation}` ·
  `state.{concern_resolved, opinion_revised, project_completed, project_failed, settlement_revolt}`

**Gate-0 item G0.4** in `godot_conversion_strategy_v1.md` reads: *"register missing Key types
(`scene.combat_resolved`, `scene.thread_operation`), drop `scene.draft_da`."* It named **2 of the 20**.
The real list is above, and it is a **~20-line diff to one GDScript dictionary.**
This is the cheapest unexecuted Gate-0 precondition in the project and it has been "blocked" for 106 days.

**Also refuted: Gate-0's premise that KeyStore must be built.** `valoria-game/autoload/KeyStore.gd`
(265 lines) is already the PP-687 substrate — `emit / subscribe / walk_back / walk_forward /
log_hash / reset_for_replay`, per-emission RNG seed from `(timestamp, type, actor[0])`, stable sort
by `(timestamp, source_system, type)`, cycle blocking (`cycles_blocked` counter), plus
`Key.gd` / `KeyTypeRegistry.gd` / `KeyValidator.gd` and `tests/test_keystore.gd`.
It cites `designs/architecture/key_substrate_v30.md §4` — a **pre-restructure path**, which is why
no ttrpg instrument has ever resolved it.

## §R8 — HONEST COUNTERWEIGHT: THE GAME IS UNVERIFIED, NOT DONE

Do not let the above overstate the game repo's readiness. Measured:
- **`addons/` does not exist — the GUT test framework is NOT vendored.** The 14 `tests/*.gd` files
  (`test_dice_engine`, `test_season_loop`, `test_keystore`, `test_integration`, …) **cannot ever
  have been executed.**
- `.github/workflows/godot-ci.yml` runs **three grep-based checks and no Godot binary**: a
  tabs-vs-spaces indentation scan, a "GameMode enum removed" grep, and a stale-constant grep.
  **No compile step. No test step. No headless run.**
- `docs/conversion_ledger.md`: 41 Phase-0 systems marked ✓ extracted, ✓ implemented — **Tested column
  empty for all 41.** Its literal "Next action:" is *"Run test_dice_engine.gd and
  test_tracker_registry.gd. Fix any failures."* — unexecuted for 106 days.
- `systems/ai/` and `systems/threadwork/` are **empty directories**.
- README says "Godot 4.6+"; `project.godot` declares `config/features=PackedStringArray("4.3", …)`.

**So the true state is: ~19,500 lines of structured, architecturally-coherent GDScript that has
almost certainly never been compiled by a Godot binary in CI, and definitely never had a test run.**
That is a *far* better starting position than the ttrpg `godot/skeleton/` (155 lines, non-compiling,
wrong architecture) — but the very first honest act is **open it in Godot 4.x and see what breaks.**
Nobody has done that. Every one of the 3,728 design-repo commits was made without doing it.

**This is itself the strongest possible evidence for the diagnosis.** The apparatus measures
`references/glossary/glossary.json` freshness on every commit. It has never once checked whether
the game compiles.

## §R9 — ⭐⭐ THE GAME WAS COMPILED FOR THE FIRST TIME IN ITS HISTORY

Downloaded Godot 4.3-stable and ran `--headless --path . --editor --quit` against
`jordanelias/valoria-game`. **No session in this project has ever done this.** 58 error lines.
After separating cascades from roots, the production-code failure set is **FIVE root causes**:

| # | root cause | sites | fix size |
|---|---|---|---|
| 1 | `Meta.gd` uses `_victory_candidates` at **7 sites (705,706,786,787,788,789,793)** and **never declares it** (`grep -c "var _victory_candidates"` → **0**) | 7 | 1 line |
| 2 | `Meta.gd:355` — Variant inferred type, **warnings-treated-as-errors** | 1 | 1 annotation |
| 3 | `CharacterData.gd:104` — `Constants.COMPOSURE_BASE` **does not exist** | 1 | 1 line — see below |
| 4 | `PackedByteArray.sha256_buffer()` **is not a Godot 4 API** — `KeyStore.gd:212`, `Key.gd:87`, `GameDirector.gd:457` | 3 | 3 lines |
| 5 | `Enums.SceneType` = `{COMBAT, DEBATE, NARRATIVE, BATTLE}` — **`BOARD` missing**, used at `SceneSystemMap.gd:31,45` | 2 | 1 enum member |

Everything else cascades: `EventBus.gd`, `GameStateMachine.gd`, `SceneTimer.gd`, `CombatLogic.gd`,
`GameDirector.gd`, `TriggerRuleRegistry.gd`, and `DomainActionSystem` "could not resolve … because of
a parser error" all fail *downstream* of the five. All 5 autoloads fail to load, so the project
cannot boot — on **roughly 12 lines of fix.**

**Defect #3 is a genuine, months-old, undetected design regression — and it indicts `design_sync.md`.**
- `Constants.gd:43`: `const COMPOSURE_MULTIPLIER: int = 3   ## Composure = Charisma × 3 (ED-694, replaces Cha+6)`
- `CharacterData.gd:104`: `composure_max = charisma + Constants.COMPOSURE_BASE`  ← **the OLD additive
  Cha+6 form, against a constant that no longer exists**
- ttrpg canon confirms: `engine/engine_params/params_tables.yaml:3132` — *"Strain scaled ×3 …
  (ED-694, replaces Cha+6)"*
- **`docs/design_sync.md` claims: `Derived scores | params/core.md L119-128 | Constants.gd | ✓ Updated
  (Composure Cha×3)`.** That ✓ is FALSE. The constant was added; the call site was never migrated.
  A cross-repo sync ledger asserted a migration that a compiler would have refuted in one second.

**Defect #5 is the same class:** `scenes/containers/` contains **`board/` and `conflict/`** with
`BoardContainer.tscn` and `ConflictContainer.tscn` built — but the `SceneType` enum was never extended
to name them. `SceneSystemMap` maps `BOARD → "strategic"`/`"peninsular"`. The strategic layer's own
scene container exists and is unreachable through the enum.

**Test suite:** all 14 `tests/*.gd` fail with `Could not find base class "GdUnitTestSuite"`.
The framework is **gdUnit4**, not GUT (the README says GUT — wrong), and `addons/` does not exist,
so it was never vendored. **Not one of the 14 tests has ever run.** Vendoring the addon is a
dependency add, not authorship.

**THE FINDING THAT SUBSUMES THE WHOLE INVESTIGATION:**
This project runs a blocking CI gate that re-verifies `references/glossary/glossary.json` freshness
on every commit — a file rewritten in 8 of 15 commits last week, 44.5% of the week's entire diff.
**In 3,728 commits it has never once checked whether the game compiles.** The five defects above
have been sitting in `main` of the game repo for 106 days, and the apparatus built to catch defects
was structurally incapable of seeing them, because **its subject was never the game.**

## §R10 — GIT FORENSICS (agent, sonnet, completed) — the ratchet, quantified

**Past 7 days (14 commits):** GAME +1,335/−551 (**1.9% of added lines**) · APPARATUS +19,211/−2,695
(26.9%) · PROSE +51,001/−14,849 (71.3%).
- **APPARATUS : GAME added = 14.39 : 1** · **(APPARATUS+PROSE) : GAME = 52.6 : 1**
- **The ONLY executable game code touched all week: `combat_engine_v1/core.py`, +30/−1 lines.**

**Month by month, (APP+PROSE):GAME ratio — rising monotonically since May:**
03: 1.89 · 04: 0.65 · 05: **0.24** · 06: 1.29 · 07: 1.79 · 08 (17 days): **6.42**
The highest ratio in the repo's history is the current month, on its *lowest* commit count (28).

**Current HEAD composition:** GAME 197,606 lines (30.0%) · APPARATUS 126,741 (19.3%) ·
PROSE 333,405 (50.7%). **APPARATUS + PROSE = 69.9% of the repository.**

**Commit `[scope]` counts, all history:** `[infrastructure]` **921** · `[editorial]` 676 ·
`[simulation]` 557 · `[patch]` 251 · `[cleanup]` 119 · `[fix]` 105 · `[skill]` 64 ·
**`[design]` 53** · `[compilation]` 37 · **`[godot]` 11** · no prefix 893.
**→ 921 infrastructure commits : 11 godot commits = 84 : 1.**

**⭐ THE REDUCTION PARADOX, measured.** 191 commits whose subject line contains
consolidat/cull/prune/leanness/retire/evacuat/sweep/audit-of/meta:
**net = +82,020 lines. 149 of 191 (78%) are net INCREASES. Only 20 (10.5%) are net decreases.**
Of ~16 identifiable dated "reduce the apparatus" campaigns, **only 3 were net reductions.**
Examples: 2026-07-15 "Consolidate observability… + **prune**" = **+8,729**. 2026-07-31 "Collapse 25
validator jobs into 2" = **+8,520**. 2026-08-12 "Track G continued" = **+30,759**.
2026-08-17 "Culling plan v1" = **+1,819** — *a plan to cull that adds 1,890 and deletes 71.*
2026-07-19 "Retire `designs/`" — the headline retirement — net **−21** on 250,000 lines of churn.

**Recursion signature, checked precisely: 0 delete-then-recreate in `tools/`, `tests/valoria/`,
`.claude/`.** Confirms §M4: this is **monotonic layer accretion**, not oscillation.
Tools ever added **154**, ever deleted **24**.

## §R11 — CAUSAL MECHANISM (agent, opus; **NODE F1 — Fable must re-adjudicate**)

**⭐⭐ THE CLOSING EVIDENCE. The most valuable game work was never blocked.**
```
workplans/workplan_v6_progress.yaml
  juncture 1 "Strategic decision" | state: not_started | blocked_on: None | owner: FA
  juncture 2 "Domain action"      | state: not_started | blocked_on: None | owner: IN
  next: "author the domain_actions home (ED-FA-0002) — the single largest M1 gap"
```
`ED-FA-0002` filed **2026-07-05**. Since then: **242 commits, 0 of 7 M1 junctures closed.**
Both say **`blocked_on: None`**. No gate, no missing ruling, no dependency. Every session could
have taken it. None did.
*(Cross-reference §R6: and it is already implemented in `valoria-game/systems/engine/DomainActionSystem.gd`.)*

**T1 — what a session SEES.** The SessionStart banner presents ~**389 named units of pending work**
(242 open EDs, 115 needing Jordan, 24 lane items, 6 stale audits, 1 stale board, 1 uncomputed grade).
**Zero concern the game.** The one game line — `M1 0/7 junctures done` — has no imperative verb and
is buried under six `⚠`. The only imperative in the whole banner is `run tools/review_core.py --json`.
CLAUDE.md: **86.9% process / 13.1% game-adjacent** — and the 13.1% is a *prohibition notice*
("Do not bind Godot resource fields to these keys yet"; "Do not represent the skeleton as a runnable
head-start"). Vocabulary: 600 process hits vs 150 game hits (**4:1**), and 37 of the 150 are the word
"Godot" inside the sections explaining why the port hasn't happened. §9's routing table has 20 rows;
**2 produce game.**

**T2 — what a session must PRODUCE to be compliant.** Stop hook = `session_handoff_reminder.py` +
`review_core.py --check`. Rewards: clean tree · HANDOFF updated · board fresh · no repo-state
regression. **All four satisfiable without touching the game; three satisfiable ONLY by writing
process prose. No Stop check asks whether an M1 juncture moved.**

**T3 — what GENERATES work. ⭐ THE SYSTEM MANUFACTURES ~95% OF ITS OWN MANDATE.**
Of 1,233 ledger rows: **59 (4.8%) cite a Jordan ruling.** **152 name an audit/proposal/session
document as their source.** Top source: `2026-07-13-multi-agent-audit` — *an audit of the audit
apparatus* — which generated **14 work items.** Closed loop, gain > 1, no human in it.

**The guard-doctrine chain, depth 5, every rung a correct application of §0.1 point 5:**
`ci_wf_harness_check.py` (583) guards `wf_harness.js` (369); `test_wf_harness.py` (472) guards the
harness; `test_wf_harness_check.py` (294) guards the guard — **1,718 lines guarding the prelude of
scripts that run audits** → every test must appear in `test_register.json` (12,514 lines) →
`--check` blocking → `ci_gate_coverage.py` (210) verifies the check line is present →
`test_gate_coverage.py` (385) tests that → `test_blocking_tier_is_honest.py` (363) — *a test that
the blocking tier's membership is honest.*

**Apparatus population over time (`tools/*.py` · `tests/valoria/*.py` · audit files):**
04-01: 5·0·0 → 05-01: 20·0·161 → 06-01: 25·0·375 → 07-01: 43·13·521 → 08-03: **99·140·1,265** →
now: 107·168·337. *Audit files fell only via the 2026-08-05 mass evacuation, which required a
Jordan ruling.* **Deletion here is never ordinary work — it is always a governance event.**

**`scope_ratchet --check` is RED right now:** `ed.stale` 198 (ceiling 76) **REGRESSED +122**;
`ed.needs_jordan_stale` 83 (ceiling 21) **REGRESSED +62**; `M1 junctures closed: 0/7`.

**The self-consuming moment:** `ci_register_size_check.py:104` caps `editorial_ledger_in.jsonl` at
50,000 tokens, **blocking**. The ED row for this very work reads: *"⚠ THIS ENTRY IS DELIBERATELY
TERSE: filing it hit the 50,000-token BLOCKING cap at 50,048."* And the tool's own comment proposes
the fix: *"a per-lane default would retire it"* — **the reflex to a ratchet symptom is to automate
the ratchet.**

**Apparatus has colonised the game directories** — this defeats the obvious countermeasure.
Last 60 commits, `systems/` gained 32,954 lines: design `.md` 4,413 · game `sim/*.py` **922** ·
`_identifier_census.yaml` (generated, one per subsystem, blocking `--check`) **24,598**.
Churn by tree over the same window: `references` +116,398 · `audit` +80,103 · `tests` +22,392 ·
`tools` **+15,619 (5.5%)** · `godot` **+4**. ⇒ **A permission gate on `tools/` would have stopped
almost nothing.**

**⭐ THE PRIOR EXPERIMENT ALREADY RAN — and this is the decisive evidence on repo-splitting.**
CLAUDE.md:10-11 names `valoria-game` as the implementation repo, "frozen since 2026-05-04."
`godot/` in *this* repo has **14 commits ever** and **+4 lines in the last 60 commits**. The last
`.gd` change here was `248f344a`, titled *"[infrastructure] Meta-review lessons converted to
enforcement."* **The last time anyone touched the game's code, it was to add enforcement.**
⇒ **Splitting the repos did not move work to the game. It moved work to whichever repo had the
apparatus. A second split done the same way produces a second frozen game repo.**

**Doctrine reformulations proposed (Fable: rule on these):**
- §0.1 pt5 → add a subject predicate + disposal branch: *"A pattern defect whose subject is a tool,
  test, register, or document about this repository is not evidence the tool needs a guard — it is
  evidence the tool is not load-bearing enough to be correct. **Delete the tool.**"*
  Preserves `test_morale_write_sweep.py` (subject: game state) verbatim; forbids `test_wf_harness_check.py`.
- §0 adversarial pass → bound the *product*: *"its output is edits to the thing under review and at
  most one paragraph in the commit message. It does not create a directory, a register, or a
  document."* Keeps all four verified catches (all were pre-commit corrections); deletes the
  179,002-line `audit/` corpus **as a category**.
- §0 max effort → supply the missing *selection* term: *"Max effort on the deliverable named by the
  current milestone… If a task is not traceable to an open M1 juncture, it is not this session's
  work."* (Note: "exhaustive" is satisfiable on apparatus — 107 tools are enumerable — and
  unsatisfiable on the game. **A doctrine demanding exhaustiveness drifts to whichever surface is
  enumerable.** And *"the harder-but-correct fix over the local patch"* literally instructs the
  agent to prefer the option that grows the tree.)

**Verdict on the culling plan (agent's):** it is a correct, unusually honest inventory of the
**STOCK**, and leaves the **FLOW** — CLAUDE.md §0/§0.1, the banner, the ledger, the audit doctrine —
explicitly intact. §7 "Keep" ends with `CLAUDE.md`. Its two HELD items (§5.6, §5.7) are precisely
the two that touch the generator. Everything it can decide alone is stock; everything that would
reduce flow is escalated. Executed in full with both held items ruled "keep," it returns the tree to
roughly its 2026-05 state **with the generator running and the 2026-07 growth curve ahead of it.**
Wave 6b even **creates a new 1,150-line register** (`ed_tombstones.yaml`, does not yet exist) and
sequences it **first** — apparatus built to retire apparatus, as step 1.

**Agent's self-refutations (recorded, not buried):**
- F1 "sessions never do real game work" — **FALSE.** ~112 game test files / 19,285 lines;
  `mc_v18.run_campaign(seed=7)` → winner Varfell, season 50, 41 battles, 153 keys, deterministic
  hash, **2.4s**. Corrected claim: real game work happens in *personal combat and mass battle*, and
  essentially none on the M1 critical path or the port.
- F2 "recent churn is overwhelmingly apparatus" — **REFUTED** (also self-refuted by the repo last
  week): hand-authored apparatus ~11.9%, design ~14.1%, **~54% machine-generated**.
  *A different indictment, not a lesser one: most of the tree's motion is machines regenerating
  descriptions of machines.*
- F3 "the apparatus catches nothing real" — **FALSE.** `test_morale_write_sweep.py`,
  `ci_golden_modes_check`, `ci_sim_fabrication_check` are genuinely load-bearing. **Any cut that
  treats all apparatus as equivalent destroys real value.**
- F5 the plan's 81/81 test split — agent's own classifier said 56/112, was **wrong on ~30 files**;
  corrected to ≈86/82. **The plan's figure is right.**

## §R9-CORRECTED — ⭐⭐⭐ THE COMPILE RESULT, PROPERLY BISECTED

**I retract the "~12 lines from booting" estimate in §R9. It was unverified when I wrote it.**
I then verified it, and the truth is both worse and much better than the estimate. Sequence, all
measured with `godot 4.3-stable --headless --path . --editor --quit` on a throwaway copy:

| state | error lines | scripts failing to load |
|---|---:|---:|
| as committed on `main` | **58** | 7 (all 5 autoloads + CombatLogic + GameDirector) |
| after fixing the 5 root causes of §R9 | **121** ⬆ | **27** |
| + one `project.godot` warning setting | **16** ⬇ | **3** |

**Step 2 going UP is the important observation and I nearly mis-reported it as a setback.**
Godot reports only the **first** parse error per file, so fixing the top layer *uncovers* the layer
beneath. A naive reading ("it got worse") is wrong; a naive reading of step 1 ("only 5 defects")
was also wrong. Neither number means anything until you bisect.

**The bisection: the dominant failure class was ONE Godot version change, not 27 defects.**
Adding to `project.godot`:
```
[debug]
gdscript/warnings/inference_on_variant=1     # 1 = warn (Godot 4.3 default is 2 = ERROR)
gdscript/warnings/untyped_declaration=0
```
took it from 121 errors / 27 broken scripts to **16 errors / 3 broken scripts.** Godot 4.3 promoted
`INFERENCE_ON_VARIANT` to an **error by default**; the code was written against earlier semantics
where `var x := some_dict[k]` was legal. Every `.tscn` container, every `systems/` module, and
5 of 6 autoloads then load.

**This is precisely CLAUDE.md §0.1's own definition of a pattern defect:**
> *"the broken code was correct when written and stopped working because something else changed."*
The repo has a doctrine written specifically for this failure class. **It has never been pointed at
the game.** The thing §0.1 exists to catch is sitting, uncaught, in the game repo — because §0.1's
guards are all aimed at the apparatus.

**What actually remains: 3 scripts, ~5 root causes, all small typed-declaration work.**
- `autoload/Meta.gd` — one Compile Error (plus my crude `_victory_candidates` insertion needs doing properly)
- `scenes/director/GameDirector.gd:252,255,266` — `DomainActionSystem` class resolution + 2 inferences
- `scenes/containers/combat/CombatLogic.gd:248,299` — 1 inference + `Could not resolve external class member "resolve"`
- `systems/faction/ValoriaFactionAI.gd:93,289,315,331` — 4 type annotations

**HONEST BOUND — do not overstate this.** "Scripts load" ≠ "the game runs" ≠ "the game is correct."
This measures *parse and load*, not behaviour, and the behaviour is April's rules (pre-dating the
2026-08-14 degree-ladder unification, the d10 strategic dice, the `CONQUEST_MIN_MIL` deletion).
What it establishes is narrower and still decisive: **the premise that the Godot port is a large
unstarted project is false.** It is a day of typed-declaration work away from loading, against a
`godot_conversion_strategy_v1.md` that sequences it behind an unexecuted Gate-0 and behind M1+M2.

## §Q — OPEN QUESTIONS FOR FABLE 5 ON RESUMPTION
1. **NODE F2 was never delivered on any model in this session** — the adversarial attack on the
   culling plan was dispatched to Fable (limit), relaunched on Opus, and had not returned when this
   report was written. **Fable should run it.** Prompt archived in §P2.
2. Adjudicate §M4 vs the user's framing: is "monotonic layer accretion" the right correction to
   "build/demolish cycle"? Evidence: 0 delete-then-recreate across tools/, tests/valoria/, .claude/;
   154 tools added vs 24 deleted; deepest chain 5.
3. Rule on the three doctrine reformulations in §R11. These are the flow fix; the culling plan is
   only the stock fix.
4. Rule on the §R11 "minimum terminating set" — in particular whether repo-split is viable given
   §R11's decisive counter-evidence (the 2026-05-04 split already ran and produced a frozen game repo).
5. Verify §R3's Recall derivation independently. It is a set-difference argument; if it is right it
   closes ED-IN-0193 and unblocks the standing "do not bind Godot fields" flag.
6. Rule on whether the Spirit→Will and Cognition→Acuity folds may proceed, given they are breaking
   renames against shipped `.tres` data (§R3 corollary).

## §R12 — NODE F2 DELIVERED (valoria-critic, opus). Fable should still re-run on Fable.

**Verdict: "the measurements are unusually good — better than this repo's baseline — and the
execution plan is unsafe."** 20 of 24 recounted figures CONFIRMED, several to the digit
(12,514 · 11,280 · 4,220 · 3,485 · 2,322 · 1,069 · 6,839 · 46.3%). All nine cited CI line numbers
and all eight `valoria_local` line numbers exact, including the `--ci` range 23–143.

**BREAKING DEFECTS (each breaks the plan as written):**
- **F1 §6b's load-bearing premise is FALSE.** `ci_claim_provenance_check.py:54-90` — **BLOCKING in CI
  (`valoria-ci.yml:124`) and locally (`valoria_local.py:175`), and the plan KEEPS it** — scans the
  **body text** of all four ledger files for `MEASURED-BY:` and fails if the named instrument is
  absent from the tree. §6b deletes two of its four inputs (62 + 28 markers) and strips closed rows
  from the other two. **Worse: archived rows name ~9 of the tools the cull deletes as their
  instruments** (`ci_wf_harness_check`, `ci_gate_coverage`, `scope_ratchet`, `evacuation_plan`, …).
  Every one of those deletions turns a kept blocking gate red. Not in the plan's risk register.
- **F2/F3 waves 1–3 each red the plan's own post-wave gate.** `test_retired_tree_apparatus.py`
  (deleted wave 3) dynamically `spec_from_file_location`s `audit_staleness` (w2),
  `observability/build_decisions` (w1), `ci_audit_registry_check` (w2), `build_apparatus_registry` (w2).
  `test_scope_ratchet.py` (w2) imports `m1_acceptance` + `dashboard_data` (both w1).
  And **two tests in NO wave, in modules §7 KEEPS**, load wave-1/2 targets:
  `test_ci_common.py:89-91` and `test_ci_common_primitives.py:687-693`.
  **Wave 1's verify grep searches `.github .githooks tools/valoria_local.py` — not `tests/`, not
  `skills/`.** Its own §9 top risk is "load-bearing in a way grep missed"; the mitigation ships with
  the blind spot pre-installed.
- **F4 §5.3's "keep that test regardless" test is broken by waves 2–3.**
  `test_no_polling_triggers.py:94-101` asserts `{'PreToolUse','SessionStart','Stop'} <= set(hooks)`;
  all three hook commands are wave-2/3 deletions.
- **F5 `valoria_local.py` degrades to a SILENT pass.** `:256-258` `if not os.path.exists(path): continue`,
  `:289` still prints "all local gates passed." The only path treating absence as failure is
  `run_ci_validators` — **which wave 3 explicitly deletes (lines 23–143)** — reinstating the §8
  second-owner violation the plan cites as its own authority.
- **F6 a skill §7 KEEPS reads a wave-1 target:** `skills/valoria-vector-audit/scripts/vector_audit.py:1653`
  loads `tools/observability/graph.json`.
- **F8 two of three cited callers are PROSE.** `ci_hooks_verifier:93` is inside a comment block
  documenting a **false positive**; `dead_primitive_census:9` is a module docstring. Likewise
  `session_open_work:18` (docstring; the real import is `:235`). **The plan grepped for filenames and
  reported the hits as callers** — the repo's own named costliest error class.
- **F13 the header's "108 tokens of headroom" is UNVERIFIABLE** — reproducible only by
  `ci_register_size_check.py`, which §6 merges away. A number in the document's most rhetorically
  load-bearing position with no surviving control (§0.1 pt 4).

**⭐⭐ C1 — THE APPARATUS HAS COLONISED THE GAME ENGINE'S SOURCE SHAPE. Most damning finding in the
whole investigation.** `engine/substrate/stubwire.py` sits inside the 29,570-line "Game engine" row
and is therefore **P (keep)** — but its own docstring `:9-11` says its purpose is to be *"composed on
by `structure_audit.py` (the `stub_wired` node attribute) and `review_core.py` (the `stubs.count`
ratchet signal)"*, and `:46-50` justifies its counter design as *"resetting on every call would make
the counter useless for the ratchet signal in `tools/review_core.py`."* It returns a typed no-op and
**does nothing in the game.** Three further kept engine files carry the same, verbatim:
- `engine/cross_scale/articulation.py:26-28` — *"a typed no-op instead of a crash, visible to
  structure_audit's `stub_wired` attribute and review_core's `stubs.count` ratchet by construction"*
- `engine/autoload/npc_ai.py:25-27` — identical
- `engine/cross_scale/scene_dispatch.py:363-365` — *"Visible via stubwire's greppable import +
  structure_audit's stub_wired attribute + review_core's stubs.count ratchet"*
**Game-engine code is now written in a shape chosen to be legible to the audit apparatus.** And
waves 2–3 delete every one of those consumers without noticing the engine-side residue.

**C2** ≈1,423 lines of pure layer-3 process prose scored as "the game" because it lives in
`systems/_architecture/` (`repository_keep_set_v1.md`, `repo_state_armature_v1.md`,
`holonic_container_doctrine_v1.md`, …) — three of them documenting mechanisms the plan deletes.
**C3** `systems/*/_identifier_census.yaml` = **26,275 lines, 15 files**, generated, `--check` blocking
(`valoria-ci.yml:122`) — absent from §2's measurement, from wave 5's untrack list, and from §8.
The largest generated-and-tracked surface the plan does not touch; 26% of everything wave 5 does.

**Q5 — the plan creates 19 NEW artifacts**, incl. `registers/ed_tombstones.yaml` (new file, ~1,150
rows, sequenced FIRST), five merged tool bodies, a new enforced "cap 100 lines per lane" rule,
new `FORK:` rows and tags, .gitignore entries, a new bullet schema for 10 handoff files,
**three new Jordan rulings**, and six PRs. Plus itself.
**Two chains traced through §7 KEEP still contain layer 3→4 with no wave assigned** —
`validate_ed_citations` → `test_ed_citation_integrity` (26 defs) → `test_ed_citation_scope` (12 defs,
*a test of the citation checker's scope*); and `compliance_check` →
`test_compliance_on_exceed_vocabulary` → `tests/coverage_matrix.md` → `test_coverage_matrix_threshold`.
**⇒ §8's "deepest chain 5 → 2" is unsupported by §7's own keep list.**

**Doctrine-orphaning: the plan flags it once (§5.6) and misses it seven times** — CLAUDE.md `:625`
(§11 asserts `ci_hooks_verifier` Check 6 enforcement, wave 3), `:579-611` (§10's whole hCritic
apparatus, wave 3), `:524` (model_router mirror, wave 1), `:270` (§4's Jordan-ruled vocabulary
definition site is `evacuation_plan.py`), `:27` (§0 tells new tooling to reuse obs_core /
audit_staleness / review_core — all deleted), `:45/:108/:170/:408-409` (banner + hooks).

**⭐ Q7 — THE PLAN NEVER MEASURED THE GAME.** `grep -in godot` over its 432 lines returns
**exactly one hit** (line 302, moving four stale `.md` to a fork). `godot/` totals 2,447 lines /
27 files; the shipping artifact `godot/skeleton/` is **717 lines**. **§2's two "the thing" rows
(Python engine; `systems/**.md` + `canon/`) include NEITHER.** §7's Keep list does not name `godot/`.
§8's target table does not contain it. §8's end state is stated entirely in line counts:
*"~29,600 lines of engine · ~58,000 of design and canon · ~10–14k of data · ~1,500 of continuity."*
**No runnable target, no build step, no `project.godot`, no scene, no acceptance criterion a human
could play.** And `rg 'doc: null' references/module_contracts.yaml` = 10 — the named porting
blocker — while 6e touches that very file to reorganise it and authors none of the 10.

**CRITIC'S RECOMMENDATION (adopt): "not reject — execute waves 4, 5, 6a and 6f, which are removals
(~273,000 lines, one-way, create nothing), and refuse waves 1–3 and 6b as written, which break kept
gates (F1–F6) and mint new apparatus."**

**Critic's currency observations (outside its lane):** CLAUDE.md §10 claims `valoria-critic` recurred
in "all three `wf_*.js` scripts" — `Glob .claude/**/*` returns **exactly one**.
CLAUDE.md `:180` claims `tests/` holds ~850KB of narrative `.md` — actual: **8 files / 1,135 lines**.
And `registers/editorial_ledger_in_archive.jsonl:73` cites `MEASURED-BY:
tools/measure_stamp_false_positives.py`, which **exists nowhere in the tree including `deprecated/`**
— so either that blocking gate is red on `main` right now, or the row is excluded. Worth running.
