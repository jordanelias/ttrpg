# Tutorial: Threadwork — act directly on the substrate of things, and pay for it in distance from being human

Repo `jordanelias/ttrpg`, HEAD `a4ca9a5`. Every behaviour claim cites a path:line opened for this tutorial, or a command run (§9).
Revised in round 3 against `51d7b05` and the precedent suite (`research/game_precedent_suite/`, reference only); changes are listed in
§8 "Round-3 corrections". Line numbers in files PR #494 touched (`rosters.yaml`) were re-opened at `51d7b05`.

## 0 Before you start

**The frame.** In the code there is no player character and no GM. Every person is a chooser that each season spends a scene
budget (5 at base: `budget()` returns scene actions, `engine/season/decision/budget.py:18-20`) on acts from a closed table of verbs.
A scene holding more than one act (up to `interactions_per_scene` = 3) costs `extended_scene_cost` = 2 (`data/fixtures.py:488-489`),
and a chunk is cut to one act when only 1 budget is left (`decision/choose.py:643-657`), so a budget of 5 buys 3 + 3 + 1 = 7 acts
(costs 2 + 2 + 1). "You" below means the acting person (a player's character if one is later seated, an NPC today).
This tutorial therefore teaches what a practitioner can do, what the rules do with it, and what a practitioner must arrange to reach a
goal. Rules that exist only in a proposal are labelled **[PROPOSED]** and are kept in §7.

**The season loop never reaches threadwork.** Nothing under `engine/season/` (outside its tests) imports or calls
`systems/threadwork/`: a grep of `engine/season/**/*.py` for `threadwork|coherence|attempt_*` returns only the write-gate guard at
`engine/season/state/world.py:1010-1019`, and after `headless.run(seasons=2, seed=1)` `sys.modules` holds no module whose name contains
`threadwork`, `knots` or `coherence` (§9). The one threadwork verb row in the table, `thread_read`, is not among the 47 resolvable
verbs (`resolvable_verbs()` → `'thread_read' in r` is `False`), and the chooser keeps only candidates whose verb is in
`resolvable_verbs()` (`engine/season/harness/populated.py:1531`, filter at `decision/choose.py:438-439`), so the chooser never forms a `thread_read` act (the claim is about the chooser; a hand-built act
submitted through a callback was not tried). The control runs agree (no line in `ctl/realm_seed{0,1,2}_2seasons.txt` at any of seeds 0, 1, 2), but their "attempted" column counts only
acts that reached the fold, so by itself it could not show that an act was never formed (suite file 13: Part 2 C2; round-2 audit G F1).
So **"Playing it today" (§§1-6) teaches the standalone Python oracle**: functions a test or script calls directly with an actor
object, a target dict and a seeded random generator. §7 teaches the proposed wiring into the loop.

**What you need from other subsystems.** Nothing, today: the oracle reads only the caller's actor and target objects and the shared
dice roller `engine/dice_engine/dice_engine.py` (`roll_pool`, `degree_label`). It reads no YAML or JSON (C11 §5; every constant is a
Python literal). The designed version needs a Thread Sensitivity field on `Person`, a write path for `(Person, coherence)`, knots
(fieldwork), Sites (settlements) and the Calamity (§6, §7).

**Terms from outside this subsystem, each in one clause.** A `Person` is the season loop's record of one individual; a `Site` is a
place-record with a `condition` value; a `Tenure` is the loop's one edge type (a held relation with an optional end `Term`); a `Claim`
is one belief in a person's own ledger, deposited at **WITNESS**, the step that fans Events to observers; **RESOLVE** is the step where
acts take effect; a **seam Event** is the only driver allowed to write `(Person, coherence)` (`state/world.py:1010-1019`). The
**Calamity** is, in canon, "an over-drawing of the substrate … What came through the resulting fracture were threadcut beings"
(`canon/00_philosophical_foundations_rules.md:83`); **no code defines it**. The only code that named it,
`check_calamity_threshold(world) -> CalamityState`, read the world-level Rendering/Mending Stability bands down to the Rupture and is
struck for want of a carrier (`systems/threadwork/sim/rendering.py:33-37`); in the proposals ([PROPOSED]) the Calamity gets an ongoing
level, which territorial strain from live weaves and locks feeds and `mend` lowers (IN-35; D05:202; §5(e), §7). A **Locked Zone** is, in
canon, "a place where becoming has been precluded … Persists indefinitely, because the process that would undo it is the one
precluded" (`canon/philosophy/09_terminology.md:117`); **no code defines it**. The name is registered twice as a mechanic with no
definition (`references/alias_registry.yaml:374-377`; `references/definitions/vocab_source.yaml:361-364`) and appears as a Mending
target ("Locked Zone border", Ob 8+, TS 70+) in the frozen prose capture `engine/engine_params/params_tables.yaml:5628-5630`
(reference, CLAUDE.md §5). Python mentions it once, in a docstring, as an example of a place where a mender is not in equilibrium: a
default of True "would hand recovery to a mender standing in a Locked Zone" (`operations.py:544-548`). The caller-supplied flag
`environment_in_equilibrium` is False there, and False everywhere else out of equilibrium too, so the flag does not pick out a Locked
Zone; canon separates a Locked Zone from "a region drawn toward a worse equilibrium" (`09_terminology.md:117`).
`grep -rni 'locked.zone' --include=*.py` finds nothing because that one Python mention breaks across `operations.py:547-548`. No
Site field or flag represents one. **Exposure** (the fieldwork sense; not the E-2 sense, presence near a drifting being, which develops
Thread Sensitivity, `coherence.py:41-42` and `canon/philosophy/07_drift.md:311-316`, the sense suite file 01 uses) is, in fieldwork canon,
a per-territory tally of investigative visibility, which canon raises by 2 for Surveil and by 1 for Thread-Read (ED-FI-0009 row 1, `registers/editorial_ledger_fi.jsonl`).
The same row's retraction answers it in code terms: conspicuousness is the size of an Event's observer set, which WITNESS already
computes (`architecture/meta/01_AXIOMS.md:1100-1101`), and a per-territory meter "was the wrong shape to begin with"; **no code
carries the tally**. The
`thread_read` row says its co-movement and Coherence cost "ARE NOT EXPRESSED HERE" and carries "the Exposure gap" on ED-FI-0009
(`engine/season/verb_table.yaml:1423`), and the loader forbids `exposure` as a bare axis name because the word has three senses
(`engine/season/rosters.yaml:504`, `:526-528`). **Precedent citations** (reference only, tier 3) use three aliases:
"sanity_a" and "sanity_b" are `research/game_precedent_suite/tutorials/T08_sanity_a.md` and `.../T09_sanity_b.md`, and "magic-sanity
table" is `research/game_precedent_suite/tables/R7_magic_sanity_travel.md`; each is cited by game and section. Process ids: `H-` hole-register rows
(`engine/season/hole_register.yaml`), `M1`-`M12` the threadwork lexicon's mechanic gaps, `TW-G` gap-register rows, `R-` verbs-proposal
rulings, `REM-` remediation items, `J-T` open template questions, `ED-`/`PP-` ledger entries. None of these ids is a built rule.

**Status, under the audit's grade rule (ERRATA G1).** **TESTS-ONLY** for the seven operations, the Coherence store, collective and
opposed workings (they execute under `engine/tests/test_thread_mending_ed871.py` and four `tests/valoria/` files); **TESTS-ONLY** also
for co-movement and threadcut, which are implemented and execute only when an oracle script calls them — no unit test does; this
tutorial's `t07/cm_tc.py` ran both (§9). **DESIGN-ONLY** for rendering (a docstring, no executing code) and for `thread_read` and every
other threadwork verb in the loop (a row with no executing path; nothing to cite). Nothing here is RUNS-IN-LOOP at any seed. G1:
RUNS-IN-LOOP = a non-refusal outcome inside `SeasonDriver.season` over `build_realm`; TESTS-ONLY = wired or implemented but executing
only under tests, fixture worlds or oracles, or with zero successful executions in the realm run; DESIGN-ONLY = no executing code.

## 0a How it plays

What a practitioner does with threadwork from the first turn, as built; the **[PROPOSED]** block comes last. Numbers are from §§1-3 and §7
unless a cite is given. Precedent aliases are defined in §0.

**Setup choices.** *At world build:* none. `build_realm(seed)` seats no threadwork state: `Person` declares no TS or Coherence field and
`(Person, coherence)` is "unproduced" (`engine/season/write_matrix.yaml:185-192`); the `ts:` values in `references/npc_registry.yaml` are
read by no season code (§6). The seed changes nothing here. *At the callback:* the delegate `auto` it is handed never proposes a thread
verb, because the chooser keeps only candidates in `resolvable_verbs()` and that set lacks `thread_read` (`harness/populated.py:1531`;
`decision/choose.py:438-439`). The callback itself may return any Act, since the seam does not validate what it returns
(`harness/play_surface.py:21-25`), and a hand-built `thread_read` was not tried (§0). *In the oracle*, the only place threadwork runs, the caller chooses the practitioner's Spirit, TS and history
(pool `spirit × 2 + min(3, history + 3) + ts // 10`, `operations.py:235-247`), the target dict (`scale`, `recency`, `configuration_of`) and
whether the environment stands in equilibrium (`environment_in_equilibrium`, `operations.py:512`; `coherence.py:341`).

**The loop.** A season runs CALENDAR, MATTER, five rounds of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS, then CENSUS and a read-only
ending report (overview §2.1; `loop/driver.py:514-518`); none of these steps calls threadwork. The oracle's own cycle is a sequence of
caller calls, nothing automated:
1. Leap (optional): TS < 30 is an automatic Failure with no roll; otherwise a roll at Ob 2 (TS 30-49) or 1 (TS 50+) (`operations.py:351-372`).
2. Working: one roll of the pool at TN 7 against the scale's Ob (`operations.py:290-348`).
3. Charge: the scale cost, the solo surcharges and −1 more on Partial or Failure, written by `apply_coherence_delta`: stress on the stretch,
   the excess past 6 into the resting point (`coherence.py:298-338`).
4. Mend (optional): another's configuration refunds 1-2 elastic units if the caller says the environment is in equilibrium; your own moves
   the resting point in by 1 on a Success or better and is refused past the crossing (`operations.py:494-509`, `:512-580`, `:592-611`).
5. Rest: `recover(seasons, environment_in_equilibrium)` returns 6 a season of elastic only (`coherence.py:341-377`). No clock calls it (K-WR-8).

**The choice menu** (grade by ERRATA G1; every row except the first is TESTS-ONLY).

| verb | cost | effect | when a person picks it |
|---|---|---|---|
| `thread_read` (season verb) | none | none: the row writes `[]` (`verb_table.yaml:1410-1423`); DESIGN-ONLY | never: the chooser cannot form it |
| Leap | 0; −1 on Partial or Failure | gate only | never on its own: the lattice rolls its own Leaps and solo operations need none (§2.5, §8 item 5) |
| weave, pull | scale cost s; s−1 on Partial or Failure | a degree; nothing written to the target | small work: Object or Personal fails 4-8% at pool 14 (§2.1) |
| past-pull | s−1; s−2 | a degree | reaching a past moment by recency |
| lock, dissolve | s−1; s−2 | identical to each other | only when weave would not do: one unit dearer |
| mend another | 0 | mender's elastic −1 or −2, only in equilibrium | after a working, to repay stretch |
| mend self | 0 | resting point −1 on Success or better (0.85 at pool 14) | to walk back set before the crossing |
| rest (`recover`) | a season in equilibrium | elastic −6 | between workings |
| collective | each participant's Leap, then the scale cost each | + `cognition // 2` dice per helper whose Leap held | deep work that one pool would fail |
| opposed | bare scale cost; the loser −1 flat | outcome text; composure and knot penalty reported only | against a rival practitioner |

**First season, step by step.** *In the loop (seed 0):* the realm builds; the chooser draws on the 47 resolvable verbs (46 once
`destroy_record` is withheld, suite file 13 G3) and none is a thread verb; 1,132 acts reach the fold over two seasons with 74 persons alive
at the end, and no line of the per-verb table names a thread verb (`ctl/realm_seed0_2seasons.txt:1-59`). After a two-season run
(`headless.run`, seed 1) no threadwork module is imported (§9). A practitioner's first season in the game is therefore empty. *In the
oracle*, take practitioner A (Spirit 4, TS 30, pool 14), taking three workings (they cost no act in the oracle, §4; under §7 each would be one of his roughly 7 acts, suite file 13, Part 2 C1), with the
dice of §3 steps 1-3: Relational weave, Success, −1 → resting 0, elastic 1, Stable; Structural weave, Failure, −3 → 0/4, Fragmented;
Structural lock, Failure, −4 → 8 > 6, so resting 2, elastic 6, Fractured. A season's rest in equilibrium then empties the stretch
(`coherence.py:374-375`) and leaves resting 2, present 2, Dissonant: rest will not lower the resting point (`coherence.py:341-377`). One
own-aim Mending Success (§3 step 6) takes resting 2 → 1, at no cost.

**What changes later.** In the loop, nothing. In the oracle, only the resting point accumulates: TS is never written (TW-G42, P-08), history
adds a flat 3 dice for every history ≥ 0 (`operations.py:246`), the elastic range is the same 6 for every being and never hardens
(`coherence.py:31-34`, `:114-115`), and resilience resists nothing at the shipped gain 0 (`operations.py:156-157`).

**Failure and ending.** There is none in the loop. The season reports endings as a read and never halts on one (`loop/driver.py:514-518`;
`queries/world_q.py:1764`). None was reached in seeds 0-2 over two seasons (suite file 13 R-F12; uncommitted round-3 probe). At build the
realm reaches none, and one opening act would suffice (`world_q.py:1789-1791`). No ending condition reads threadwork
(the conditions read holds and faction commits, `world_q.py:1771-1773`). In the oracle, a resting point past 5 is the crossing: every band
reads "Coherence failure", self-Mending is refused, the report latches once, and stress arithmetic continues; nothing else follows
(`coherence.py:215-227`, `:400-404`, `:411-432`; what follows has no carrier, `:67-70`). Where Sunless Sea's mutiny, Bloodlines' frenzy
(triggered by hunger, pain or humiliation, with a risk that depends on Humanity; the floor's effect is [CONTESTED]) and Darkest Dungeon
II's Meltdown take something away (sanity_a, Sunless Sea §2 step 6 and Darkest Dungeon II §2 step 7 and §6; sanity_b, Bloodlines §2 and
§8), the crossing takes away only the way back.

**Consequential vs cosmetic choices.** Consequential (oracle only): the scale, which raises Ob and cost together; resting between workings
(stretch stacks, and set is taken only past 6); own-aim Mending, the only inward move on set; the equilibrium flag, which gates every
recovery. Dominant: Mending, free at every degree (`operations.py:322`, `:449-451`); aimed at another it pays the worker 1-2 elastic in equilibrium
(`:494-509`), aimed at oneself it walks set back (`:159-167`): one or the other per cast (`:572-577`). Cosmetic or dead:
Locking against Dissolution (identical), history (a flat 3), breadth and distance (unread), band labels (read by nothing), resilience at
gain 0, the MS delta (reported, dropped), co-movement cards (text only).

**[PROPOSED] As proposed.** In the remediation plan (`proposals/2026-10-21-v9-remediation/`), batch B-S "plugs `systems/threadwork`" (part 03, lines 10-11); RB-3a (REM-30, IN-47, a character-sheet space) opens after B-S merges and RB-3b (REM-31, IN-46, the
played fight) after B-Y (part 02, lines 548-551, :559, :570); D-2 is ruled yes (suite file 13 G16). The seam a seated player would use
is built and run only by tests (`harness/play_surface.py:41-52`; `engine/season/tests/test_play_surface_dispatch.py`; suite file 13
R-F4). Under the verbs lexicon (§7), a working would be one act
of the ordinary scene economy (7 acts a season at budget 5), pass a Leap stage, and write `(Person, coherence)` through a seam Event at
RESOLVE, the only writer `state/world.py:1010-1019` admits.

| verb [PROPOSED] | cost | effect | when | grade |
|---|---|---|---|---|
| `thread_read` | one act; −1 Coherence at Relational+ | a Claim at WITNESS; +1 Exposure (canon) | to learn a site or a person's displacement | DESIGN-ONLY |
| `weave` | one act; the oracle's scale cost | a held-load Tenure; strain toward the Calamity | to make a thing cohere | DESIGN-ONLY |
| `lock` | one act; the oracle's scale cost −1 | a Locked Zone on a Site, refused by the write gate until mended | to stop a place changing | DESIGN-ONLY |
| `dissolve` | one act; the oracle's scale cost −1 | Site condition to the floor; a residue mark | to end a thing | DESIGN-ONLY |
| `mend` | one act; 0 | closes a lock, raises a lattice Site, moves a resting point; repays the mender | to repair, and to recover | DESIGN-ONLY |
| `ward` | one act | a one-season protecting Tenure | against a hostile working | DESIGN-ONLY |
| `knot` | one act; TN 7, Ob 2 | a directed knot Tenure; rupture costs Coherence −1 | to bind to a partner | DESIGN-ONLY |

In that table, the **Calamity** is canon's over-drawing of the substrate, to which the proposals give an ongoing level, fed by territorial strain from live weaves and
locks and lowered by `mend` (IN-35; D05:202); a **Locked Zone** is a place where becoming has been precluded, which in code today has no
representation (its one docstring mention is an example of a place where a mender is not in equilibrium, and the flag
`environment_in_equilibrium` is False elsewhere out of equilibrium too); **Exposure** is the per-territory fieldwork tally that
`thread_read` would raise by 1, which the ED-FI-0009 retraction reads as the size of an Event's observer set, not a per-territory meter
(all three: §0). Open before any of it plays: the TS carrier (H-85, build B4), the seam (M1), a
recovery clock or rest verb (K-WR-8), and what follows the crossing (K-WR-5, TW-G11) (§7).

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| practitioner (actor) | any object the caller passes; read by attribute name ("duck-typed"). No Person field holds any of these | reads `.spirit`, `.ts`, `.history`, `.actor_id`/`.name`, `.resilience`, `.cognition`, `.max_wounds`, `.wounds` | `systems/threadwork/sim/operations.py:15-19` (`[ASSUMPTION]`: "World has no practitioner stat schema yet") |
| thread / target | **there is no Thread entity.** A target is a plain dict | keys read: `scale` (all ops), `recency` (Past-Pulling), `configuration_of` (Mending). `breadth`, `distance` are named in a docstring and read by nothing | `operations.py:375-385`, `:397-414`, `:583-589` |
| Thread Sensitivity (TS) | the practitioner's access to threadwork; the design's "one class gate" | 0-100 (docstring). Gate: TS ≥ 30 for a Leap. **Default 30 in the pool, 0 in `attempt_leap`** | `operations.py:238`, `:242`, `:358-366`; `engine/season/hole_register.yaml:1052-1062` (H-85: no carrier) |
| Thread Pool Score (TPS) | the TS term in dice | `ts // 10` | `operations.py:244`; `references/descriptor_registry.yaml:65` |
| Spirit | the main pool attribute; doubled | docstring "1-7"; default 4 | `operations.py:238`, `:241`, `:247` |
| history | "relevant points" toward the pool | term is `min(3, history + 3)` = **3 for every history ≥ 0** (defect, §8) | `operations.py:243-246` |
| pool | number of d10s rolled | `spirit×2 + min(3, history+3) + ts//10`; defaults 8+3+3 = **14**; floor 1 die | `operations.py:235-247`; `engine/dice_engine/dice_engine.py:202` |
| die face | value of one d10 | 1 → −1; 2-6 → 0; 7-9 → +1; 10 → +2; net = sum | `dice_engine.py:150-161` |
| TN | target number | **7, always**; any other value raises | `operations.py:51-73`; `dice_engine.py:196-199` |
| Ob (obstacle) | what net must reach | by operation and scale (tables below) | `operations.py:77-124`, `:406-408` |
| degree | the result band, on margin = net − Ob | ≥ 3 Overwhelming; ≥ 1 Success; 0 Partial; < 0 Failure | `dice_engine.py:227-241` (single owner), `:304-306` |
| scale (depth) | how deep in the substrate the target sits; sets Ob and cost | Object, Personal, Relational, Field, Structural, Foundational (+ Territorial in the cost table only) | `operations.py:77-84`, `:128-136` |
| `DEPTH_OB` | Ob for Weaving, Pulling, Locking, Dissolution | 1 / 2 / 3 / 5 / 8 / 13 | `operations.py:77-84` |
| `MENDING_OB` | Ob for Mending | Relational 2, Field 4, Structural 7, Foundational 12; any other scale is priced as Relational | `operations.py:87-92`, `:452`, `:463-468` |
| Leap Ob | Ob for the Leap | 2 at TS 30-49; 1 at TS 50+ | `operations.py:123-124`, `:369` |
| recency Ob | Ob for Past-Pulling | same scene 3; 1-2 seasons 4; 3-5 → 5; 6-10 → 6; 10+ → 7; unknown → 3 | `operations.py:406-408` |
| `COHERENCE_COST_BY_SCALE` | base Coherence cost of a working | Object 0, Personal 0, Relational −1, Field −1, Territorial −1, Structural −2, Foundational −2 | `operations.py:128-136` |
| `FR_SURCHARGE` | extra cost on Locking and Dissolution (solo only) | −1 | `operations.py:140`, `:429`, `:438` |
| blanket penalty | extra cost on a Partial or Failure | −1, every operation except Mending (also hits the Leap) | `operations.py:321-323` |
| resilience | practitioner-side resistance to cost (R-14) | `RESILIENCE_GAIN = 0` shipped, so it does nothing; sweep arms (0, 1, 3) | `operations.py:142-157`, `:250-274` |
| Coherence | **a distance** from the human equilibrium, not a pool that drains. Two stored numbers per practitioner | starts 0 / 0 | `systems/threadwork/sim/coherence.py:1-56`, `:194-219` |
| resting point | where you sit when fully recovered; moves out only by permanent set | integer ≥ 0 | `coherence.py:22-24`, `:203` |
| elastic displacement | the stretch on top of the resting point; recovers | 0 to `ELASTIC_RANGE` = 6 | `coherence.py:25-27`, `:115`, `:204` |
| present displacement | resting point + elastic; what the bands read | — | `coherence.py:210-213` |
| `HUMAN_BAND_LIMIT` | the farthest resting point that is still human | 5; resting point **6+ = crossed** | `coherence.py:118`, `:215-219` |
| bands | label on present displacement | 0-1 Stable; 2-3 Dissonant; 4-5 Fragmented; 6+ Fractured; any crossed state "Coherence failure" | `coherence.py:124-139`, `:154-162`, `:221-233` |
| recovery | elastic return | 6 per season of rest, **only if the caller says the environment is in equilibrium**; never touches the resting point | `coherence.py:129-133`, `:341-377` |
| Mending-Stability (MS) delta | a per-working side-effect number | **reported in the result, written nowhere** | `operations.py:211-213`, `:327-336` |
| `OperationResult` | what every solo operation returns | degree, net, pool, tn, ob, `coherence_delta`, `mending_stability_delta`, `coherence_restored`, `resting_point_mended`, notes | `operations.py:200-222` |
| lattice / Anchor | collective working: the highest-TS participant anchors, others help | helper adds `cognition // 2` dice (falls back to spirit, default 3); fracture → Ob +1 | `systems/threadwork/sim/collective.py:43`, `:62-68`, `:71-229` |
| opposed working | two practitioners contest one target | your Ob + `max(1, opponent TPS // 2)`; 9-branch outcome table | `systems/threadwork/sim/opposing.py:48`, `:79-84`, `:102-269` |
| co-movement card | a side-effect card drawn from a 15-card deck | each card carries an MS number and text; effects not executed; no caller | `systems/threadwork/sim/co_movement.py:42-59`, `:94-134` |
| threadcut being | an entity outside Coherence that maintains its own rendering | rendering strain +1 per external operation; de-actualisation rounds 1-3; perception banded by observer TS | `systems/threadwork/sim/threadcut.py:37-56`, `:92-195` |
| rendering | strain on reality, Calamity threshold | **docstring only**; both functions struck | `systems/threadwork/sim/rendering.py:1-41` |
| store | where Coherence state lives | `world.practitioners` if the caller's world has it, else a module-level dict | `coherence.py:141-151` |

## 2 How it works

Threadwork is the setting's magic-like layer. A practitioner suspends his own "self-rendering" (the **Leap**) and acts on the substrate
of a thing: makes it cohere (Weaving), opens it (Pulling; Past-Pulling reaches a past moment), prevents it becoming (Locking), ends it
(Dissolution), or repairs the substrate (Mending) (`operations.py:376`, `:389`, `:418`, `:435`, `:514`). In the oracle every one of these
is **one roll that returns a degree and charges the worker's Coherence**. No operation writes anything about its target (§8).

### 2.1 The roll (every operation)

1. **Build the pool.** `pool = spirit × 2 + min(3, history + 3) + ts // 10` (`operations.py:241-247`). Spirit is the big lever (2 dice
   per point); TS adds 1 die per 10 points; history adds a flat 3. Defaults (Spirit 4, TS 30, history 0) give 14 dice.
2. **Roll at TN 7.** Each d10 scores 1 → −1, 2-6 → 0, 7-9 → +1, 10 → +2; net is the sum (`dice_engine.py:150-161`, `:196-206`).
   Per die the mean is +0.4 and the variance 0.64, so 14 dice average net 5.6 (s.d. ≈ 3.0) — arithmetic of the face rule.
3. **Read the degree off the margin** net − Ob: ≥ 3 Overwhelming, 1-2 Success, 0 Partial, < 0 Failure (`dice_engine.py:227-241`).

Exact odds for the default 14-die pool (computed by convolution of the face rule, `t07/odds.py`, §9):

| Ob | used by | Failure | Partial | Success | Overwhelming |
|---|---|---|---|---|---|
| 1 | Object op; Leap at TS 50+ | 0.041 | 0.042 | 0.161 | 0.756 |
| 2 | Personal op; Leap at TS 30-49; Mending at Relational | 0.082 | 0.067 | 0.212 | 0.638 |
| 3 | Relational op; same-scene Past-Pulling | 0.149 | 0.094 | 0.249 | 0.507 |
| 4 | Mending at Field | 0.244 | 0.118 | 0.262 | 0.377 |
| 5 | Field op | 0.362 | 0.131 | 0.248 | 0.260 |
| 7 | Mending at Structural | 0.623 | 0.117 | 0.162 | 0.097 |
| 8 | Structural op | 0.740 | 0.094 | 0.113 | 0.053 |
| 13 | Foundational op | 0.988 | 0.007 | 0.004 | 0.001 |

A weak practitioner (Spirit 1, TS 30: pool 8) fails a Leap at Ob 2 with probability 0.228 and a Relational working at Ob 3 with 0.386.

### 2.2 The price (every operation except Mending)

`_resolve_operation` (`operations.py:290-348`) charges, in this order:

1. the operation's **base cost**: the scale cost from `COHERENCE_COST_BY_SCALE` (0 / 0 / −1 / −1 / −2 / −2), plus `FR_SURCHARGE` −1 for
   Locking and Dissolution, plus −1 for Past-Pulling (`:383`, `:409`, `:427-429`, `:437-438`); the Leap's base is 0 (`:371`);
2. **−1 more if the degree is Partial or Failure** (`:321-323`) — a poor result costs more;
3. resilience resistance, which is the identity at the shipped gain 0 (`:269-274`);
4. the write: `apply_coherence_delta` (`coherence.py:298-338`), the only thing that moves your Coherence outward.

It also computes an MS delta (Weaving/Pulling on Partial = scale cost, on Failure = scale cost − 1; Locking/Dissolution −1 at every
degree; `operations.py:331-336`) and returns it without storing it.

| operation | Ob | cost on Success/Overwhelming | cost on Partial/Failure |
|---|---|---|---|
| Leap | 2 (TS 30-49) / 1 (TS 50+); TS < 30: automatic Failure, no roll | 0 | −1 (defect C-TW-3; docstring says 0) |
| Weaving, Pulling | `DEPTH_OB` | scale cost (0, 0, −1, −1, −2, −2) | scale cost − 1 |
| Past-Pulling | recency 3-7 | scale cost − 1 | scale cost − 2 |
| Locking, Dissolution | `DEPTH_OB` | scale cost − 1 | scale cost − 2 |
| Mending | `MENDING_OB` | 0 | 0 |

Expected cost per attempt at pool 14 (arithmetic from the table above): Relational Weaving −1.24, Structural Weaving −2.83, Structural
Locking −3.83.

### 2.3 Coherence: a resting point and an elastic stretch

Coherence is modelled as distance from the human equilibrium (`coherence.py:16-20`: "not a resource that runs out"). A cost of −k is a
stress of k. The two stored numbers behave like a spring with a permanent-set limit (`coherence.py:328-336`):

- **Stress stacks on the stretch.** `elastic += k`. If that would exceed `ELASTIC_RANGE` = 6, the excess moves into the
  **resting point** exactly and elastic stays pinned at 6. Example: elastic 4, stress 4 → 8 > 6 → resting point +2, elastic 6.
  Precedent handle: Sunless Sea caps Terror at 50 on return to London and converts the excess into 0-4 Nightmare's Strength,
  proportional to Terror (sanity_a, Sunless Sea §2 step 7 and §8), where Valoria keeps the excess exactly. Pathologic 2's per-death
  max-Health penalty lasts the whole save file, removed only by starting a new file or by the Fellow Traveler's deal at an undisclosed
  cost (sanity_b, Pathologic 2 §1, §6); Valoria's set, unlike it, walks back under own-aim Mending until the crossing (§2.4).
- **Stretch recovers; set does not.** `recover(seasons, environment_in_equilibrium, mending)` lowers elastic by `6 × seasons + mending`,
  floored at 0, **only if the environment is in equilibrium**; it never assigns the resting point (`coherence.py:369-377`). Time never
  adds displacement (`coherence.py:35-38`).
- **The resting point moves inward only by Mending aimed at yourself** (`mend_resting_point`, `coherence.py:380-408`), floored at 0.
- **The bands read present displacement** (resting + elastic): Stable 0-1, Dissonant 2-3, Fragmented 4-5, Fractured 6+
  (`coherence.py:154-162`). So a fresh practitioner at full stretch (0 + 6) already reads Fractured, and rests back to Stable.
- **A band is a label and nothing else.** No pool, Ob, perception or act reads it: the pool is `spirit × 2 + min(3, history + 3) +
  ts // 10` with no Coherence term (`operations.py:235-247`), and no code outside `coherence.py` reads `band` or `resting_band` (grep of
  the tree; only `tests/valoria/test_coherence_elastic_plastic.py:156-161` reads them). Before the crossing, displacement changes only
  the label and the headroom left before set. By contrast, each sanity or stress meter in the six sampled precedent titles delivers its
  cost during play: Eternal Darkness's room-entry effects below 50% and Health drain at 0, Don't Starve's shadow creatures at low
  Sanity, Darkest Dungeon II's Meltdown at Stress 10, Sunless Sea's mutiny at Terror 100, Pathologic 2's per-death penalties and
  Bloodlines' Humanity-weighted frenzy risk and dialogue tone (sanity_a, Eternal Darkness §2 steps 5-6, Darkest Dungeon II §2 step 7 and
  §6, Sunless Sea §2 step 6; sanity_b, Don't Starve §2 step 5, Pathologic 2 §6, Bloodlines §2 and §7; aliases in §0).
- **Crossing the band.** When the resting point exceeds `HUMAN_BAND_LIMIT` = 5, `crossed` is true (`coherence.py:215-219`). From then
  on: every band reading is "Coherence failure", whatever the stretch (`:221-227`); `mend_resting_point` **refuses** ("restoring a
  remembered state — manipulation, not Mending", `:400-404`), so the set can never come back; `check_coherence_failure_transition`
  reports the crossing exactly once and never clears it (`:411-432`); stress arithmetic keeps running (`:316-318`). **Nothing else
  happens**: what follows the crossing has no carrier (`coherence.py:67-70`; TW-G11). The fastest route there from 0/0 is 12 units of
  stress without rest — for example three Structural Lockings at Failure (−4 each): 4 → elastic 4; 8 → resting 2, elastic 6;
  12 → resting 6, crossed.

The rule the code's own docstring draws (`coherence.py:48-56`): stretch from separate workings stacks until it is recovered, so "a
practitioner who recuperates between workings never yields from small ones", and one who keeps working takes permanent set.

### 2.4 Mending: the working that pays its worker

`attempt_mending` (`operations.py:512-580`) rolls against `MENDING_OB` and costs **0 Coherence at every degree** (ED-871, `:449-451`;
the blanket penalty is skipped, `:322`). Then it routes on `target['configuration_of']` (`:583-589`):

- **Another's configuration** (absent, `None`, or any other id): if the degree is not Failure, the **mender** is offered a restorative
  term = the scale cost read backwards (Relational/Field 1, Structural/Foundational 2; `:471-491`), delivered through
  `recover(seasons=0, mending=term)` — so it only lands if the caller passes `environment_in_equilibrium=True` (default False,
  `:544-548`). Nothing about the target changes: "being mended BY someone else" is not routed (`:561-563`).
- **Your own configuration** (`'self'` or your id): on Success or Overwhelming the resting point moves in by 1
  (`RESTING_POINT_MEND_BY_DEGREE`, `:168`); Partial and Failure move nothing; past the crossing it is refused and noted, not raised
  (`:592-611`). No elastic term on this path. The code flags this itself as a gap: an attempt "costs nothing (ED-871), so repeated
  casts can walk a permanent set to 0" (`:159-167`).

### 2.5 Working together: the collective lattice

`attempt_collective_operation(actors, op_type, target, …)` (`collective.py:71-229`):

1. Rank participants by TS; the highest is the **Anchor**, the rest helpers.
2. **Every participant rolls a full Leap** (`collective.py:116`) and pays its own Leap cost. A Leap "succeeds" if its degree is not
   Failure — so a Partial Leap counts, and still costs −1.
3. If the Anchor's Leap failed, no lattice forms and nothing more happens.
4. Pool = the Anchor's own pool + `cognition // 2` for each helper whose Leap succeeded (`:62-68`). If that pool is below half of what
   it would be with every helper, the lattice is **fractured**: Ob +1 (`:159-175`).
5. One roll against `DEPTH_OB` (or `MENDING_OB` for Mending). Every participant whose Leap succeeded pays the scale cost, −1 more on
   Partial/Failure. **No FR surcharge and no Past-Pulling −1 in collective form** — `op_type` only chooses the Ob table.
6. Collective Mending pays each participant the restorative term; a collective Mending aimed at anyone's own configuration raises.

Co-movement in the brief's sense — several workers moving one target — is this lattice. The code's "co-movement" (`co_movement.py`) is
something else: the side-effect deck in §2.7.

### 2.6 Opposition

`resolve_opposing_operations(actor_a, actor_b, op_type, target, …)` (`opposing.py:102-269`): each side's Ob is the base Ob +
`max(1, opponent's TPS // 2)` (`:79-84`, `:154-155`), so a high-TS opponent makes your working harder. Both roll their own pool; each
degree is folded to Meets (Success or better), Partial or Failure; a nine-branch table (`:175-239`; an inline comment at `:172` says "6 rows")
returns an outcome text, an MS number and per-side consequences. Losers take composure 2 (4 for Locking/Dissolution) and a knot Ob
penalty; Partial/Partial rolls a d6 and on 1-2 produces "Shifting Object one scale below". **Only each side's Coherence is written**
(`:117`); composure, knot strain and MS are returned. Costs use the bare scale cost: no FR surcharge here either (observed, §3).

### 2.7 Side systems with no caller

- **Co-movement deck** (`co_movement.py:42-134`): 15 cards (CM-01 Temporal Drift … CM-15 Dissolution Wake). A draw is "actualised" iff
  the depth is not Object/Personal, which selects the card's actualised MS column. That column is equal to or further from 0 than
  the other: more negative on the negative cards (CM-09 −3 against −2), +2 against +1 on CM-10, equal on CM-05, -07, -11, -12
  (`co_movement.py:44-58`). Card effects are text; `apply_comovement_effects` is struck (`:15-21`); nothing in the tree calls
  `draw_comovement_card`. Passing a world whose `comovement_deck` is an empty dict raises `KeyError: 'remaining'` (`:79-80`, `:115`);
  with no world it uses a module-level deck.
- **Threadcut beings** (`threadcut.py`): a registry of beings outside Coherence (`:23-24`). Each external operation *by* one adds
  rendering strain 1; when strain ≥ `max_wounds` or wounds ≥ `max_wounds // 2` it advances a de-actualisation round 1 → 3, whose Ob
  penalties (+2, +4) exist only as note text (`:150-185`). Observers perceive them by TS band: < 10 "nothing or vague unease" … ≥ 70
  "full perception" (`:37-43`, `:105-111`). No caller and no unit test; `t07/cm_tc.py` ran it: a threadcut being with
  `max_wounds` 6 and 3 wounds takes strain 1 from one working and enters round 1 ("all operations +2 Ob", a note only).
- **Rendering** (`rendering.py`): a docstring recording that `apply_rs_strain` and `check_calamity_threshold` were struck.

## 3 A worked example

Run read-only with `python -I` against the real oracle (`t07/worked.py`, §9). One world object `W = SimpleNamespace(practitioners={})`
holds all Coherence state; each step gets its own `random.Random(seed)`, and the dice shown are the first `pool` draws of that seed,
which is exactly what `roll_pool` consumes. Three practitioners:

| | Spirit | TS | history | pool | Leap Ob |
|---|---|---|---|---|---|
| A | 4 | 30 | 0 | 8 + 3 + 3 = 14 | 2 |
| B | 1 | 30 | 0 | 2 + 3 + 3 = 8 | 2 |
| C | 4 | 20 | — | (no roll) | — |

**Step 1 — A weaves at Relational scale.** Ob 3, base cost −1. Seed 2 rolls
`1 2 2 6 3 5 5 10 4 10 1 10 3 7`: two 1s (−2), three 10s (+6), one 7 (+1) → net 5. Margin 5 − 3 = 2 → **Success**. Cost −1 (no
penalty). State A: resting 0, elastic 1, present 1, **Stable**. Log: `stress 1, "Weaving Success"`.

**Step 2 — A weaves at Structural scale.** Ob 8, base −2. Seed 5 rolls `10 5 6 9 1 8 4 1 3 2 6 8 4 7`: 10 (+2), 9 8 8 7 (+4), two 1s (−2)
→ net 4. Margin −4 → **Failure**. Cost −2 −1 = **−3**; MS delta −3 reported. Elastic 1 + 3 = 4 ≤ 6 → state A: resting 0, elastic 4,
present 4, **Fragmented**. Nothing is recorded about the target.

**Step 3 — A locks at Structural scale, without resting.** Ob 8, base −2 + FR −1 = −3. Seed 4 rolls `4 5 2 7 8 3 2 2 1 7 9 5 1 4` → net
4 − 2 = 2. Margin −6 → **Failure**. Cost −3 −1 = **−4**. Stretch 4 + 4 = 8 > 6: the excess 2 becomes **permanent set**. State A:
resting **2**, elastic 6, present 8, **Fractured**, not crossed (2 ≤ 5). Log: `stress 4, resting 0 → 2, elastic 4 → 6`.

**Step 4 — B tries a Leap and fails.** Ob 2 (TS 30-49). Seed 2 rolls `1 2 2 6 3 5 5 10` → −1 + 2 = net 1. Margin −1 → **Failure**.
Base cost 0, but the blanket −1 applies: **B is charged −1** (defect C-TW-3; the docstring at `operations.py:355` says a failed Leap
costs nothing). State B: resting 0, elastic 1. **C tries a Leap**: TS 20 < 30, so `attempt_leap` returns Failure with pool 0, Ob 0,
cost 0 and the note "Eligibility failure: TS < 30" — no dice, no cost, nothing logged.

**Step 5 — A mends another's Relational configuration.** Ob 2. Seed 5 again (same dice as Step 2): net 4, margin 2 → **Success**,
cost 0. Restorative term = −(−1) = 1.
- Called with the default `environment_in_equilibrium=False`: `coherence_restored = 0`; A is unchanged (resting 2, elastic 6).
- Called again with `environment_in_equilibrium=True`: `coherence_restored = 1`. State A: resting 2, elastic **5**, present 7, Fractured.
  Log: `recover 1, "Mending Success at Relational: restorative feedback"`.

**Step 6 — A mends his own configuration** (`{'scale': 'Relational', 'configuration_of': 'self'}`). Ob 2. Seed 6 rolls
`10 2 8 5 1 1 3 10 8 6 6 1 5 8`: two 10s (+4), three 8s (+3), three 1s (−3) → net 4. Margin 2 → **Success**. Cost 0;
`resting_point_mended = 1`. State A: resting **1**, elastic 5, present 6, Fractured. No elastic term on this path.

**Step 7 — A rests one season in equilibrium** (`recover('A', seasons=1, environment_in_equilibrium=True)`). Offered 6; elastic 5 → 0
(floored). State A: resting 1, elastic 0, present 1, **Stable**. `check_coherence_failure_transition('A')` → `failed=False`.

What the seven steps leave: A carries 1 unit of permanent set that rest will never remove, and B carries 1 elastic unit from a Leap
that did nothing. The Step-6 Success had probability 0.85 at pool 14 (Ob 2: Success 0.212 + Overwhelming 0.638), at zero cost — so a
second attempt would very likely return A's resting point to 0.

**Two more runs from the same script, for §2.5-2.6.**
- *Collective Field Weaving.* Anchor (Spirit 4, TS 50: pool 16, Leap Ob 1), helpers h1 (cognition 4) and h2 (cognition 6), seed 7:
  all three Leaps succeed; pool 16 + 2 + 3 = 21 against Ob 5; net 15 → **Overwhelming**; each of the three is charged −1 (resting 0,
  elastic 1). Exact odds for pool 21 at Ob 5: Failure 0.143, Overwhelming 0.592 (against 0.362 / 0.260 alone at pool 14).
- *Opposed Relational Locking.* P (Spirit 4, TS 50: pool 16) against Q (Spirit 3, TS 40: pool 13), seed 3: base Ob 3; P's Ob 3 +
  max(1, 4 // 2) = 5, Q's Ob 3 + max(1, 5 // 2) = 5. P nets 11, Q nets 6: both **Meets** → "Shifting Object at target's scale (both
  meet Ob)", MS −1. Each side is charged **−1** (the bare Relational cost; a solo Locking at Relational would charge −2) and is
  reported composure 4 and knot Ob penalty 2 — values returned, not stored.

## 4 What you can do

There are no threadwork verbs in the loop, so "your turn" today is one call to an oracle entry point. None consumes a scene, a store
or a body; the caller decides how often to call. Who may act: anyone the caller passes; the only check on the actor is the Leap's
TS ≥ 30, and **only the Leap and the collective path apply it** — the six solo operations roll for any TS (§8).

| entry point | prerequisites | Ob | cost (S/O · P/F) | by degree | writes |
|---|---|---|---|---|---|
| `attempt_leap(actor, target_state)` `operations.py:351` | TS ≥ 30, else automatic Failure, no roll | 2 / 1 | 0 · −1 | degree only; no effect | Coherence (on P/F) |
| `attempt_weaving(actor, target)` `:375` | none | `DEPTH_OB[scale]` | s · s−1 | degree; MS reported on P/F | Coherence |
| `attempt_pulling(actor, target)` `:388` | none | `DEPTH_OB[scale]` | s · s−1 | same as Weaving | Coherence |
| `attempt_past_pulling(actor, target_moment)` `:397` | none | recency 3-7 | s−1 · s−2 | degree; no MS (scale not passed, `:413`) | Coherence |
| `attempt_locking(actor, target)` `:417` | none | `DEPTH_OB[scale]` | s−1 · s−2 | degree; MS −1 always | Coherence |
| `attempt_dissolution(actor, target)` `:434` | none | `DEPTH_OB[scale]` | s−1 · s−2 | identical to Locking | Coherence |
| `attempt_mending(actor, target, *, environment_in_equilibrium)` `:512` | none | `MENDING_OB[scale]` | 0 · 0 | other's config: S/O/P → mender's elastic −1/−2 if in equilibrium; self: S/O → resting point −1 | mender's Coherence (inward only) |
| `attempt_collective_operation(actors, op_type, target)` `collective.py:71` | Anchor's Leap not Failure | depth or Mending Ob (+1 if fractured) | each Leap's cost, then s · s−1 per successful participant (Mending 0) | degree; no lattice if Anchor fails | every participant's Coherence |
| `resolve_opposing_operations(a, b, op_type, target)` `opposing.py:102` | none (no Leap rolled) | base + max(1, opponent TPS // 2) | from the nine-branch table (bare scale cost, −1 flat on Failure) | outcome text, composure, knot penalty, MS — reported | both sides' Coherence |
| `recover(actor, *, seasons, environment_in_equilibrium, source)` `coherence.py:341` | none | — | — | elastic −6 per season if in equilibrium | elastic only |
| `check_coherence_failure_transition(actor)` `coherence.py:411` | none | — | — | reports crossed / first observation | the reporting latch |
| `draw_comovement_card(op_type, depth)` `co_movement.py:94` | none | — | — | a card; actualised iff depth beyond Personal | deck store |
| `resolve_threadcut_interaction(actor, target_id, op_type)` `threadcut.py:114` | actor or target marked threadcut | — | — | strain +1 and rounds, if the actor is threadcut | threadcut registry |

`s` = the scale cost (Object/Personal 0, Relational/Field −1, Structural/Foundational −2). In the loop: `thread_read`
(`engine/season/verb_table.yaml:1410-1423`) has a row — eligibility own + presence at a site, `requires: "Thread Sensitivity >= 30"`,
`requires_typed: none`, `writes: []`, emits `finding.made` / `finding.none` — but it is outside `resolvable_verbs()` and cannot be
attempted.

The brief's list also names **sever, loosen, heal, ward, anchor**. None of these is a code operation. In the proposed lexicon, `sever` is
renamed `dissolve` (R-10), `loosen` folds into `release` (own shape) or `mend` (another's), `heal` folds into `mend`, `ward` is a new
build-gated verb, and `anchor` is culled (L13 §5). "Anchor" in `collective.py` is only the name of the highest-TS participant.

## 5 Pursuing goals here

### (a) The goals, and how the code represents them

| goal | represented in code as | represented nowhere (yet) |
|---|---|---|
| make a working **take** (cohere, open, preclude, end, repair a target) | the returned `degree` | any change to the target: no Site, Person, Tenure or Claim is written (§8) |
| **stay human** | `CoherenceState.resting_point ≤ 5` (`coherence.py:215-219`). Crossing changes exactly three things: every band reads "Coherence failure" (`:221-227`); own-aim Mending is refused, so the set can never come back (`:400-404`; `operations.py:605-610`); the failure report latches (`:411-432`). Nothing outside `coherence.py` and `operations.py:607` reads `crossed`, and `check_coherence_failure_transition` is called only by `tests/valoria/test_coherence_elastic_plastic.py` (grep) | any consequence in the world: no death, change of side, loss of acts or effect on others is wired (TW-G11). In the precedent set the threshold can take control or end the run: Bloodlines' frenzy (triggered by hunger, pain or humiliation, with a risk that depends on Humanity; the floor's effect is [CONTESTED]), Sunless Sea's mutiny at Terror 100, Darkest Dungeon II's Meltdown (sanity_b, Bloodlines §2 and §8; sanity_a, Sunless Sea §2 step 6 and Darkest Dungeon II §2 step 7 and §6) |
| **recover** stretch | `elastic_displacement` → 0 via `recover` or Mending feedback | a clock or rest verb that calls `recover` in a season (K-WR-8) |
| **undo** permanent set | own-aim Mending, −1 resting point per Success+ | a harder Ob or a cost for it (`operations.py:159-167` `[GAP]`) |
| work at larger scale than you can alone | the collective lattice (bigger pool) | breadth (`BREADTH_OB` is unread) |
| prevail over a rival practitioner | `OpposingResult` | its composure, knot and MS consequences (returned only) |
| grow stronger | nothing: TS is never written; history is inert | TS is fixed by design (TW-G42, P-08: no thread competence "by study alone") |

The resource you manage is **headroom**, not a pool you spend: the code models Coherence as a distance (`coherence.py:16-20`), and what
you protect is the gap between your resting point and 5. Elastic stretch is borrowed and repaid by rest; permanent set is spent for good.

### (b) The plays

1. **Work small, rest between.** Keep each working's stress plus current elastic ≤ 6 and recover before the next. A Relational working
   costs 1 or 2; a fresh practitioner can take three Relational Partials (6) and still take no set. One season of equilibrium rest
   empties the stretch (`ELASTIC_RETURN_PER_SEASON` 6). This is the play the docstring itself describes (`coherence.py:55-56`).
2. **Pick the scale with the best odds per unit of cost.** At pool 14 an Object or Personal working fails 4-8% of the time and costs 0
   (−1 on a bad roll); Structural fails 74% and costs a likely −3. Raising Spirit by 1 adds 2 dice; raising TS by 10 adds 1.
3. **Prefer Weaving/Pulling to Locking/Dissolution** when either would do: same Ob, one unit cheaper.
4. **Pool with others for deep work.** A lattice adds `cognition // 2` dice per helper, but every participant pays a Leap (−1 on a
   Partial or Failure) and the working's cost. Put the highest-TS practitioner first: his TS sets the Anchor's Leap Ob (1 at TS 50+).
5. **Mend after you work.** Mending another's configuration costs nothing and, in equilibrium, returns 1-2 units of elastic stretch.
6. **Mend yourself to walk back set.** Own-aim Mending at Relational (Ob 2) succeeds 0.85 of the time at pool 14 and 0.61 at pool 8,
   costs nothing, and removes 1 unit of permanent set per Success or better — only while you are not yet crossed.

### (c) Costs, risks, counter-play, blocks

- **Bad rolls cost more.** Every non-Mending working pays −1 extra on Partial or Failure, so a deep working you are likely to fail
  carries most of its expected cost in the failure.
- **Stacking without rest takes set.** Three Structural Locking Failures in a row cross a fresh practitioner (§2.3).
- **The environment gate.** Recovery and Mending's feedback land only when the caller says the environment is in equilibrium; the
  Mending default is False. A practitioner working in a Locked Zone (one place, among others, where the equilibrium condition fails, §0; Mending's ordinary
  workplace, per `operations.py:546-548`) recovers nothing.
- **A failed Leap still costs** (−1), and in a lattice a Partial Leap counts as success *and* costs −1.
- **An opponent's TS is your Ob.** Your Ob rises by `max(1, opponent TPS // 2)`: +1 against TS below 40, +2 at TS 40-59, +3 at
  60-79 (`opposing.py:79-84`, `:140-155`).
- **The crossing is one-way.** Past resting point 5, self-Mending is refused.
- **What blocks you:** TS < 30 blocks the Leap and therefore the lattice; nothing blocks the solo operations.

### (d) What the mechanics structurally reward or punish

- **Mending dominates.** It is the only working with no cost at any degree, it pays the worker (`coherence_restored`), and aimed at
  yourself it is the only inward move on the resting point, with no cadence limit. The code names this as a gap: "repeated casts can
  walk a permanent set to 0" (`operations.py:166`). Permanent set is therefore not permanent for anyone not yet crossed.
  No title in the verified sanity and stress set has an ungated, unlimited-rate free repair (an absence claim, not exhaustive): Eternal Darkness's free Sanity refund needs a downed enemy and
  returns about what that enemy's gaze took, and a reviewer calls the game, played that way, "strategically gentle"; Darkest Dungeon II
  recovers Stress per Inn; Sunless Sea's free family time (−20 Terror) is gated by Something Awaits You, once per SAY [V2], and SAY
  re-rolls each minute at zee; and Don't Starve's Tent has six uses [V2] (sanity_a, Eternal Darkness §3 and §7, Sunless Sea §2, §7
  and §8; sanity_b, Don't Starve §3 and §8; magic-sanity table §1 (Darkest Dungeon II Inn rows, `:18`, `:27`), §2 (`:46`) and §4
  (`:74`)).
- **Locking and Dissolution are identical in code** (same Ob, same cost, same MS); with no target written, choosing between them
  changes nothing (TW-G23).
- **Past-Pulling at Object/Personal**: the `max(-1, …)` cap at `operations.py:412` changes nothing, since 0 − 1 is already −1.
- **History is a dead lever**: any history ≥ 0 gives the same 3 dice (defect, §8). **Breadth and distance are dead levers**:
  no operation reads `BREADTH_OB` or `DISTANCE_OB` (both are exported to `sim_params.json`, §8 item 7). **No operation reads
  `DEPTH_TS_MINIMUM`**, so a TS-30 practitioner may attempt a
  Foundational working (it fails 98.8% of the time at pool 14 and then costs −3).
- **Opposed workings are cheap for the loser**: the failing side pays −1 flat regardless of scale (`opposing.py:199`, `:223`), where a
  solo Structural Failure pays −3 to −4.
- **Collective Locking skips the FR surcharge**, so binding work is cheaper per person in a lattice than alone.

### (e) What success leaves in the world

Today: only Coherence entries in the store, a log line per change (`coherence.py:240-253`), and returned numbers. A successful Weaving
leaves no woven thing; a successful Locking leaves no Locked Zone (§0: nothing in code or in a Site's fields represents one); the MS delta, co-movement card and opposing composure are reported
and dropped.

What the design says the world should do in response **[PROPOSED]** (L13 §4.3, §5; D05:202): live weaves and locks become territorial
strain feeding the Calamity (§0), which `mend` holds back (IN-35); witnessed threadwork moves convictions — the rosters already carry sign
cells such as `solmund_orthodoxy: thread_read: -1` ("witnessed threadwork violates orthodoxy", `engine/season/rosters.yaml:2738`);
heresy persecution needs a thread act to witness, charge and arrest (TW-G31); a Leap opens an involuntary knot to its target
(`[ASSUMPTION]`, L13 §2 claim 31); co-movement cards put side effects into the territory.

### (f) Precedent handles (reference only)

The repo's research index records no game source for threadwork (`research/00_INDEX.md:178`, `:258`); these handles come from the
precedent research (tier 3: reference, not mechanism). Names are the aliases defined in §0.

| Valoria piece | nearest verified precedent | the difference |
|---|---|---|
| elastic stretch, repaid by rest | Don't Starve's Codex Umbra: 55 max Sanity rented for 2.5 days (magic-sanity table §4) | DS repays on a timer; Valoria only when the caller passes `environment_in_equilibrium=True` (`coherence.py:374`) |
| excess over the range becomes set | Sunless Sea: Terror capped at 50 in London, the excess converted to 0-4 Nightmare's Strength (sanity_a, Sunless Sea §2 step 7) | Valoria keeps the excess exactly; SS converts it in bands |
| lasting set | Pathologic 2: per-death max-Health penalty (sanity_b, Pathologic 2 §1, §6) | P2's lasts the save file (a new file or the Deal only); Valoria's walks back until the crossing (§2.4) |
| Mending pays the mender | Eternal Darkness finishing refund (sanity_a, Eternal Darkness §2 step 4); Bloodlines reconciliation grants Humanity (magic-sanity table §6) | ED ties the refund to the loss its source caused; VtMB gates it by a dialogue feat; Valoria by a roll and the equilibrium flag |
| cost charged to the identity meter | Eternal Darkness: casts cost MP, but steering a summoned Horror drains Sanity (sanity_a, Eternal Darkness §3, §8); Bloodlines: powers cost blood (sanity_b, Bloodlines §3) | Valoria has one channel: a working's cost is its Coherence charge (C-2, `coherence.py:48-51`) |
| what the threshold does | Darkest Dungeon II's Meltdown/Resolute fork; Bloodlines' frenzy (triggered by hunger, pain or humiliation, with a risk that depends on Humanity; the floor's effect is [CONTESTED]); Sunless Sea's mutiny (sanity_a, Darkest Dungeon II §2 step 7 and §6 and Sunless Sea §2 step 6; sanity_b, Bloodlines §2, §8) | Valoria's crossing relabels the bands, latches a report and blocks self-Mending, nothing more (§2.3) |

## 6 How it connects

| other subsystem | what flows today | what is designed |
|---|---|---|
| season loop / write gate | nothing. `(Person, coherence)` is declared at RES, class ACTS, "unproduced" (`engine/season/write_matrix.yaml:185-192`); `world.py:1010-1019` refuses that write from any driver but "Seam"; `Person` has no coherence or TS field (grep of `engine/season/state/carriers.py`) | a thread-operation seam writes `(Person, coherence)` (M1) |
| fieldwork / knots | `systems/fieldwork/sim/knots.py:368-379`: a knot **rupture** charges −1 Coherence through `apply_coherence_delta`, in a `try/except` that swallows import errors; `knots.py` is imported only by `engine/tests/test_knots_ed912.py` | `thread_read` as an inquiry yielding findings (R-13: TW owns the gate and cost, FI the finding shape); `trace` through a held knot; `knot` as a TW verb (R-02) |
| mass battle | `modules/mass_battle/orchestration.py:333-334` `threadwork_check` is an empty hook ("threadwork lands in a future cycle (G-9)"), called at every phase boundary (`:346`) | Formation-breadth hand-off of weave/lock/dissolve/mend (TW-G30, PARKED) |
| convictions / social | sign-only `thread_read` cells: −1 for `solmund_orthodoxy`, +1 for `inner_tradition` and `thread_truth` (`rosters.yaml:2737-2742`) — unread, since `thread_read` never resolves | orthodoxy scars on witnessed workings (M4) |
| settlements / sites | nothing | `lock` on a Site = Locked Zone (§0); `dissolve` drives `Site.condition` to the floor; `mend` raises a lattice Site through `_rise`; `restore` stays fabric repair (R-26) |
| NPC data | `references/npc_registry.yaml` authors `ts:` on 32 rows (some as ranges, "75–80") and one `coherence: 9`; no season code reads them | TS seated on `Person` by `seat_template` (B4 in the verbs plan, D06) |
| dice | `roll_pool` and the degree ladder are the shared owners; threadwork adds no second ladder (`test_degree_ladder_single_owner.py`) | J-T6: one practice-to-dice ladder across subsystems |

Combinations available today are only inside the oracle: a Mending after a working (cost then repayment), a lattice before a deep
working, a Leap gate before a lattice. Nothing crosses into another subsystem's state except the knot-rupture charge under its test.

## 7 Playing it as proposed

Everything in this section is **[PROPOSED]** (`proposals/2026-10-16-verbs/…-13-lexicon-threadwork.md`, status PROPOSED; D04 §TW;
D05:202). Rulings already applied inside that proposal: R-02 (`knot` is TW's), R-10 (`sever` → `dissolve`), R-13 (TW owns
`thread_read`), R-26 (`mend` is Mending; `restore` stays fabric repair). Mechanic gaps M1-M12 are the lexicon's own ids (L13 §6).

**What a working would cost you in a season.** A thread verb would be one act in the ordinary scene economy, like every other row.
The verbs plan lists a working's cost as "a scene · stores · body · coherence (thread, planned)" (D05:38), and no proposal gives
a thread verb its own scene price. With a budget of 5 you get 3 + 3 + 1 = 7 acts a season (§0); the seed-0 realm run averages about
7.6 resolved acts per person per season (1,132 resolved acts / ~74 living persons / 2 seasons, `ctl/realm_seed0_2seasons.txt`). So
each working uses one of those slots, and a whole scene (cost 1) if it is the only act in that scene. It displaces a `tell`, a
`forge` or a `march`, and it puts on Coherence a charge that today only rest or Mending repays. Repaying a full stretch takes one
season of rest in equilibrium (6 units), but nothing proposed yet says how a season of rest is bought: a recovery clock or a rest
verb is an open decision (K-WR-8, §3.9 item 1). A practitioner working at the scale table's −1 to −4 per act could take 1 to 4
stretch units per act, so two deep workings a season are enough to need that rest.

**How a turn would go.** A practitioner would spend one act of that budget on a thread verb. Every operation verb passes through a
**Leap stage** first — not a verb of its own — that checks TS ≥ 30, rolls the Leap and, on success, opens an involuntary directed knot
to the target `[ASSUMPTION]`. The working then rolls the oracle's pool and writes `(Person, coherence)` through a seam Event at RESOLVE.
Unlike today, each verb would also write its target:

| verb | what you would do | what it would write | waits on |
|---|---|---|---|
| `thread_read` (hosts `trace`, `diagnose`) | perceive the substrate at a site; `trace` follows a knot you hold; `diagnose` reads a person's displacement | a Claim at WITNESS in your own ledger; −1 Coherence at Relational+ and +1 Exposure (the per-territory fieldwork tally of §0, which the ED-FI-0009 retraction reads as the size of an Event's observer set; the row's co-movement and Coherence cost "ARE NOT EXPRESSED HERE" and it carries "the Exposure gap" on ED-FI-0009, `verb_table.yaml:1423`) | M2 TS carrier and gate (H-85; build B4), M1, M3, FI-G01 content yield |
| `weave` | make a thing cohere | your Coherence; a held-load Tenure `weave` that stands while you hold it; strain for the Calamity (§0) | M1, M2, M3, M5 (IN-35), M6 held shapes |
| `lock` | preclude a thing becoming; on a Site, a Locked Zone (§0) | Tenure `lock` read by the write gate as a refusal, until mended | M1, M2, M3, M6; Sites first (person-target form not designed) |
| `dissolve` | end a thing | Site `condition` to the floor, a held shape closed destructively, a residue mark | M1, M3, M6, M10; built after weave/mend/lock (TW-G23) |
| `mend` (hosts `heal`) | repair: close a lock or another's weave, raise a lattice Site, move another's resting point, heal a body | the target by kind; your elastic return or own resting point; 0 Coherence | M1, M5, M6, M7 (being mended by another, today unrouted) |
| `ward` | protect a person or Site for one season | Tenure `ward` with a one-season `Term`; hostile workings on it routed to `opposing.py`, you as second practitioner, paying its cost | M8; ships only with the first hostile operation the loop executes |
| `knot` | bind yourself to a partner (Disposition ≥ 5, Bonds ≥ 5, either TS ≥ 30; TN 7, Ob 2) | a directed knot Tenure; strain −5..+5, rupture at 5 (Disposition −3, Coherence −1) | M3, H-182 partner operand, ED-912 strain carrier, V-2a (TW-G36) |
| `pull` (with past-pulling) | open a thing; reach a past moment by recency | a displaced-claim deposit, append-only (K-WR-2) | PARKED on M9 (P-09 orphan carrier), TW-G14/G15 |

`loosen` folds into `release` (your own shape) or `mend` (another's); `anchor` is culled — equilibrium stays a fact supplied to
`recover` (L13 §5). The THREAD-WORKER actor class in D05 lists these seven as "stubs" (R-C-18); at HEAD only `thread_read` has a row
(and `tie / knot`, outside TW).

**How the world would answer.** `mend` would be "the canonical act that lowers the Calamity" (D05:202); live weave and lock loads and
dissolution residue would count as territorial strain (IN-35, M5); witnessed workings would fire orthodoxy cells (M4) and give heresy
persecution something to act on (TW-G31).

**Open decisions the proposals name** (none ruled): how elastic return enters the season loop — a licensed clock or a rest verb,
against `write_matrix.yaml`'s "three licensed clocks are exhaustive" (§3.9 item 1, K-WR-8, TW-G29); whether knots are permanent
(§3.9 item 2); what follows the crossing (§3.9 item 3, K-WR-5, TW-G11); own-aim Mending difficulty (`operations.py:162` `[GAP]`);
resilience gain 0/1/3 (R-14); the history-term fix `min(3, history) + 3` (REM-45, gated on hand-verifying PP-624); the Leap's blanket
−1 (C-TW-3, ED-WR-0005); the Leap vulnerability window (TW-G21, M11).

**Stubbed, inert at shipped defaults, or refused.**

| item | state | evidence |
|---|---|---|
| `thread_read` row | exists; not resolvable, so never formed (the chooser keeps only `resolvable_verbs()`); reaches the fold 0 times at seeds 0, 1 and 2 (2 seasons each) | `verb_table.yaml:1410-1423`; `resolvable_verbs()`; `harness/populated.py:1531`; `ctl/realm_seed{0,1,2}_2seasons.txt` (no thread line) |
| resilience | inert: gain 0 returns the cost unchanged | `operations.py:157`, `:269-270` |
| MS delta, opposing composure/knot penalty, co-movement MS | computed and dropped | `operations.py:211-213`; `opposing.py:117` |
| co-movement, threadcut | TESTS-ONLY by G1: implemented, no caller and no unit test; run only by `t07/cm_tc.py` | grep of the tree for `draw_comovement_card`, `resolve_threadcut_interaction` |
| rendering | docstring only, struck | `rendering.py:1-41` |
| MB hook | empty body, called every phase | `orchestration.py:333-346` |
| knot rupture → Coherence | runs only under `engine/tests/test_knots_ed912.py` | `knots.py:368-379` |

## 8 Common mistakes and traps

1. **"The season runs threadwork."** It does not (§0). `rosters.yaml:2390` labels it `loop_resident`; that is a label, not a call.
2. **"Coherence is a mana pool that drains to 0."** The retired 10 → 0 track is superseded (ED-WR-0010, `coherence.py:9-20`); Coherence
   is a distance that grows. `references/npc_registry.yaml` still carries one `coherence: 9` in the old shape, which `from_dict` would
   refuse (`coherence.py:262-272`).
3. **"An operation changes its target."** No operation writes anything but Coherence, the deck and the threadcut registry (C11 §5).
4. **"A failed Leap is free."** The docstring says so (`operations.py:355`) and L13 §4.1 repeats it; the code charges −1 on Partial or
   Failure (`:321-323`). Only the TS < 30 eligibility Failure is free.
5. **"Solo operations need a Leap and TS ≥ 30."** Only `attempt_leap` and the collective path check TS. The six solo entry points never
   call `attempt_leap` and roll for any TS; and an actor with no `.ts` pools as TS 30 but Leaps as TS 0 (`:242` vs `:358`).
6. **"History adds dice."** `min(3, history + 3)` is 3 for every history ≥ 0 (TW-G26, REM-45); only a negative history would move it.
7. **"`DEPTH_TS_MINIMUM`, `BREADTH_OB` and `DISTANCE_OB` apply."** Defined, and no operation reads them at runtime
   (`operations.py:95-119`). But they are **exported** into the port contract: `engine/engine_params/sim_params.json:3131`, `:3185`,
   `:3203` and `value_pointer_links.json:233`, `:528`, `:689`. A port reading those files would get constants the oracle ignores.
7a. **"A caller can raise the Leap gate."** `attempt_leap`'s docstring says `target_state` takes an optional `ts_minimum` (default 30)
   (`operations.py:354`), but the code hard-codes `ts < 30` and never reads it (`:358-360`).
8. **"Locking costs the FR surcharge everywhere."** Only solo. Collective and opposed workings use the bare scale cost (§3 run).
9. **"Mending heals the person you mend."** It moves nothing of the target; it pays the mender (`operations.py:561-563`).
10. **"Rest always recovers."** Only with `environment_in_equilibrium=True`; Mending defaults to False.
11. **"The crossing kills or transforms."** It only relabels the band, latches a report and blocks self-Mending.
12. **"Co-movement is several practitioners moving together."** In code, co-movement is the side-effect card deck; joint work is the
    collective lattice.
13. **"sever / loosen / heal / ward / anchor are operations."** They are verb names in a proposal (§4), not code.
14. **NPC data vs code gate.** `npc_registry.yaml:172` calls TS 25 "above practitioner threshold"; the code's Leap gate is 30.
15. **Corrections to the draft (A4).** (a) A4 says no G20 gap extract exists; `extract/G20_gaps_SC_GV_FI_TW.md` exists and carries
    TW-G01..G42 (42 rows). (b) A4 counts collective helpers "whose Leap succeeded" without noting that a Partial Leap counts as success
    and still costs −1 (`collective.py:116-118`). (c) A4 lists the missing FR surcharge for collective form only; opposed form omits it
    too (`opposing.py:175-239`, observed −1 at Relational).
16. **Dice-engine path.** The roller is `engine/dice_engine/dice_engine.py`; `engine/autoload/` does not exist at HEAD (`ls`), though
    `CLAUDE.md` §5 and `coherence.py:75-78` name `engine/autoload/…`.
17. **"Leaving the human band" is a Humanity score.** It is not a conduct meter. Only stress events a caller names move it outward: a
    working's cost through `charge_working` (`operations.py:277-287`) or a knot rupture (`systems/fieldwork/sim/knots.py:368-379`,
    test-only). No act's conduct toward others (kindness, killing) enters it: a working's cost is set by its scale, kind and degree, not
    by whom it helps or harms; conduct is the scar/conviction carrier (ERRATA G7, suite file 13). Vampire: Bloodlines' Humanity, which
    falls for killing innocents and rises for kindness, is the false friend, and its powers cost blood, not Humanity (sanity_b,
    Bloodlines §2, §3 and §7; aliases in §0).

### §8 Round-2 corrections

Each was checked against the cited line before being applied.

1. **Scene economy (X1, F4, CROSS C1).** Was: "picks up to 5 scene actions per season" and "one of his 5 scene actions". Now: a budget
   of 5 scenes, extended scenes of up to 3 acts costing 2, so 7 acts at budget 5 (`budget.py:18-20`, `fixtures.py:488-489`,
   `choose.py:643-657`). §7 now says what a working costs a practitioner in a season.
2. **Grade rule (F6, X12, CROSS C12).** Was: the draft's "the loop reaches it" rule, with co-movement and threadcut graded DESIGN-ONLY.
   Now: ERRATA G1. Co-movement and threadcut are TESTS-ONLY (implemented, executed by an oracle script, no unit test); rendering and
   the loop verbs stay DESIGN-ONLY; nothing is RUNS-IN-LOOP at any seed.
3. **"6 rows" (F7).** It is an inline comment (`opposing.py:172`), not the docstring.
4. **Dead constants cross into the port (F9).** `DEPTH_TS_MINIMUM`, `BREADTH_OB` and `DISTANCE_OB` are exported to
   `sim_params.json` and `value_pointer_links.json` (§8 item 7).
5. **Leap gate is not caller-adjustable (F10).** The `ts_minimum` key in the docstring is never read (§8 item 7a).
6. **Co-movement columns (F14).** Was: "the card's larger MS number". Now: the actualised column is equal to or further from 0, which
   on most cards means more negative (`co_movement.py:44-58`). Added: an empty `comovement_deck` dict on the world raises `KeyError`.
7. **Line count scope (F15).** 1,950 is `sim/*.py`; 1,955 includes the package `__init__.py` (§9).
8. **Undefined terms (L: primitives; CROSS C11).** Calamity, Locked Zone and Exposure are now defined in §0 from canon, with a plain
   statement that no code defines or carries any of them. Person, Site, Tenure, Claim, WITNESS, RESOLVE, seam Event and the
   process-id prefixes are also defined there.
9. **"Stay human" (L note).** §5(a) now lists the three things a crossing changes in code, and says no consequence in the world is
   wired; `crossed` is read only in `coherence.py` and `operations.py:607`, and the failure check only by a test.
10. **Seed rule (CROSS C2).** §0 and §7 now say per seed that `thread_read` reaches the fold at none of seeds 0, 1, 2.

### Round-3 corrections

Each was checked against the cited line at `51d7b05` before being applied. Precedent handles are reference only (tier 3).

1. **`thread_read` and the control runs (§0, §7 table).** Was: "no `thread_read` act reaches the fold at any seed (... "attempted" there
   counts admitted acts)" and "attempted 0 times". Now: the chooser keeps only `resolvable_verbs()` (47, no `thread_read`), so it never
   forms the act; the `ctl` column counts only acts that reached the fold and cannot show non-formation
   (`engine/season/harness/populated.py:1531`, `decision/choose.py:438-439`; suite file 13 Part 2 C2, round-2 audit G F1).
2. **Calamity, Locked Zone, Exposure (§0, with glosses at §5(c), §5(e), §6, §7, §0a).** Was: "no code defines" each, with a grep for
   `locked.zone` "finding nothing". Now: the code reading is stated. The Calamity's only code was the struck `check_calamity_threshold`
   (`rendering.py:33-37`). The Locked Zone is a registered name with no definition (`alias_registry.yaml:374-377`) and one docstring
   mention, as an example, which the `.py` grep misses because it breaks across lines (`operations.py:544-548`). Exposure's tally has
   no carrier: the row carries "the Exposure gap" on ED-FI-0009 (`verb_table.yaml:1423`), whose retraction reads it as an observer-set
   size (`architecture/meta/01_AXIOMS.md:1100-1101`); the loader forbids it as a bare axis name (`rosters.yaml:504`, `:526-528`).
3. **Bands (§2.3, new bullet).** Added: a band is a label; the pool has no Coherence term (`operations.py:235-247`) and only
   `tests/valoria/test_coherence_elastic_plastic.py:156-161` reads `band` or `resting_band` outside `coherence.py` (grep).
4. **Permanent set (§2.3, "Stress stacks" bullet).** Added: Sunless Sea's cap-and-convert and Pathologic 2's per-death penalty as
   precedent handles (`coherence.py:331-334`, `:400-404`).
5. **"Mending dominates" (§5(d)).** Added: no title in the verified sanity and stress set has an ungated, unlimited-rate free repair
   (an absence claim, not exhaustive); Sunless Sea's family time is gated once per SAY [V2], and SAY re-rolls each minute at zee [V3]
   (`operations.py:159-167`).
6. **"Stay human" (§5(a)).** Added: in the precedent set the threshold can take control or end the run (`coherence.py:67-70`).
7. **Trap 17 (§8, new).** Added: "leaving the human band" is not a Humanity score (`operations.py:277-287`;
   `systems/fieldwork/sim/knots.py:368-379`).
8. **§5(f) (new).** Added: the precedent-handles table; the research index records no game source for threadwork
   (`research/00_INDEX.md:178`, `:258`).
9. **§0a (new).** Added: how it plays, as built and [PROPOSED]. The ending line reflects PR #494: the season now reports endings as a
   read and does not halt on one, and none was reached in seeds 0-2 (uncommitted round-3 probe; `loop/driver.py:514-518`;
   `queries/world_q.py:1764`, `:1789-1791`).
   The remediation sentence was corrected from the critic draft: RB-3a (REM-30) builds IN-47, and IN-46 is RB-3b (REM-31)
   (`proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-02-items-rb0-to-rb3.md:548-551`, `:559`, `:570`).
10. **Stale line numbers after PR #494.** `rosters.yaml:2672` -> `:2738`; `:2671-2676` -> `:2737-2742`; `:2670-2676` -> `:2736-2742`
    (the `thread_read` cells moved +66); `tools/export_game_constants.py` "lines 60, 133" -> "60, 134".

#### Audit fixes

Each was checked against the cited line before being applied (independent round-3 audit of this file; finding numbers are the audit's).

1. **Exposure (§0, §0a, §7; audit 1).** "No code carries it" alone -> adds that the ED-FI-0009 row's own retraction reads conspicuousness as the size of an Event's observer set (`registers/editorial_ledger_fi.jsonl` row 1; `architecture/meta/01_AXIOMS.md:1100-1101`).
2. **Locked Zone gloss (§0, §0a, §5(c); audit 2).** "A place where `environment_in_equilibrium` would be False" -> no code representation; the docstring names it as one example and the flag is False elsewhere too (`operations.py:544-548`; `canon/philosophy/09_terminology.md:117`).
3. **Sunless Sea free reduction (§5(d), item 5; audit 3, partly).** "Once per voyage [V2, not re-checked in v3]" -> once per SAY [V2], and SAY re-rolls each minute at zee [V3] (`R7_magic_sanity_travel.md:46`; `T08_sanity_a.md:110`, `:175`); the V2 tag stays on "once per SAY" because v3 corrected only the re-roll cadence.
4. **Pathologic 2 (§2.3, §5(f); audit 4).** "The fully permanent case" -> lasts the save file, removed only by a new file or the Fellow Traveler's deal (`T09_sanity_b.md:79`, `:128`; `R7_magic_sanity_travel.md:103`).
5. **Missing section names (§2.3, §5(d); audit 5).** Magic-sanity table "Delivery of the cost" and "Comparison" (absent from the in-repo file) -> in-repo sections by number (`R7_magic_sanity_travel.md:18`, `:27`, `:46`, `:74`; `T08_sanity_a.md` and `T09_sanity_b.md` sections as cited).
6. **`verb_table.yaml:1423` wording (§0, §7, item 2; audit 6).** "+1 Exposure ... NOT EXPRESSED HERE" -> the row says its co-movement and Coherence cost "ARE NOT EXPRESSED HERE" and carries "the Exposure gap" on ED-FI-0009.
7. **Locked Zone grep (§0, item 2; audit 7).** "Finds nothing only because the mention breaks across lines" -> scoped to `--include=*.py`, plus the two registrations and the frozen `params_tables.yaml:5628-5630` Mending row (`references/alias_registry.yaml:374-377`, `references/definitions/vocab_source.yaml:361-364`).
8. **Ending (§0a, item 9; audit 8).** "Its docstring says the realm as built reaches none" -> none was reached in seeds 0-2 (uncommitted round-3 probe, suite file 13 R-F12); at build none, and one opening act would suffice (`queries/world_q.py:1789-1791`).
9. **Callback menu (§0a; audit 9).** "A seated person's menu holds no thread verb" -> the delegate `auto` never proposes one, while the callback may return any Act and a hand-built `thread_read` was not tried (`harness/play_surface.py:21-25`).
10. **Exposure sense (§0; audit 10).** One unmarked sense -> "the fieldwork sense; not the E-2 sense" used by suite file 01 (`coherence.py:41-42`; `canon/philosophy/07_drift.md:311-316`; `rosters.yaml:526-528`).
11. **Worked-example acts (§0a; audit 11).** "Spending three of his roughly 7 acts" -> three workings that cost no act in the oracle (§4), each one act under §7.
12. **Index lines (§5(f), items 8, §9; audit 12).** `research/00_INDEX.md:177`, `:257` -> `:178`, `:258`.
13. **Eternal Darkness power pool (§5(f); audit 13).** "Power has its own pool" -> casts cost MP, but steering a summoned Horror drains Sanity (`T08_sanity_a.md:209`, `:247`).
14. **Don't Starve Tent (§5(d); audit 14).** "Six uses" untagged -> tagged [V2] (`T09_sanity_b.md:32`, `:70`).
15. **Bloodlines frenzy (§0a, §5(a), §5(f); audit 15).** Frenzy as the threshold's effect -> triggered by hunger, pain or humiliation with a risk that depends on Humanity, the floor's effect [CONTESTED] (`T09_sanity_b.md:161`, `:204`; `R7_magic_sanity_travel.md:116-117`).
16. **Calamity (§0, §0a; audit 16).** "The proposals turn it into territorial strain" -> an ongoing level that strain from live weaves and locks feeds and `mend` lowers, as §5(e) and §7 already said (`canon/00_philosophical_foundations_rules.md:83`; IN-35; `2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md:70`).
17. **Mending (§0a; audit 17).** "Free, paying its worker and walking set back" as one cast -> free at every degree, and one of the two paths per cast (`operations.py:322`, `:449-451`, `:494-509`, `:159-167`, `:572-577`).
18. **Leap (§0a menu; audit 18).** "Before a lattice" -> never on its own: the lattice rolls its own Leaps and solo operations need none (`collective.py:115-116`).
19. **History (§0a; audit 19).** "A flat 3 dice whatever its value" -> "for every history ≥ 0", matching trap 6 (`operations.py:246`).
20. **Meltdown cost (§0a, §5(a), §5(f); audit 20).** Cited at DD2 §2 step 7 (the 80/20 fork) alone -> adds §6, where the quirk chance and 3 Affinity per bond are stated (`T08_sanity_a.md:76`).
21. **Dispatch seam (§0a [PROPOSED]; audit 21).** "A seated player would be one person's decision procedure" -> the seam is built and run only by tests (`harness/play_surface.py:41-52`; `engine/season/tests/test_play_surface_dispatch.py`).
22. **Reviewer quote (§5(d); audit 22).** The reviewer calls "the meter" strategically gentle -> calls the game, played that way, "strategically gentle" (`T08_sanity_a.md:241`).

## 9 Checks

- `git rev-parse --short HEAD` → `a4ca9a5`; `wc -l systems/threadwork/sim/*.py` → 1,950 (the eight `sim/` files);
  all `.py` under `systems/threadwork/` including the package `__init__.py` → 1,955 (the figure in ERRATA G14).
- Opened `systems/threadwork/sim/operations.py:1-611` (all); `coherence.py:1-445` (all); `collective.py:60-70` and grep of `:116`,
  `:140`, `:159-175`; `opposing.py:140-200` and grep of `:48`, `:79-84`, `:199`, `:212`, `:223`; `threadcut.py:150-185` and grep of
  definitions; `co_movement.py` grep of definitions.
- Opened `engine/dice_engine/dice_engine.py:150-245`, `:300-306`.
- `grep -rniE 'threadwork|coherence|attempt_(leap|weaving|mending)' engine/season --include=*.py | grep -v /tests/` → only
  `state/world.py:1010-1019`.
- `grep -rln systems.threadwork --include=*.py .` → tests, `systems/fieldwork/{__init__,sim/knots}.py`, `tools/export_game_constants.py`
  (comment/text lines 60, 134), one `.audit/` script; nothing under `engine/season/`.
- `python -I -c "…headless.run(seasons=2, seed=1)…"` → no `threadwork`/`knots`/`coherence` module in `sys.modules`.
- `python -I -c "…resolvable_verbs()…"` → 47 verbs, `'thread_read' in r` False.
- `grep -i 'thread|knot' ctl/realm_seed*_2seasons.txt` → no lines.
- `grep -rln 'draw_comovement_card\|resolve_threadcut_interaction' --include=*.py .` → only their own two files.
- Opened `engine/season/verb_table.yaml:1410-1423`; `write_matrix.yaml:183-196`; `rosters.yaml:2736-2742`;
  `hole_register.yaml:1052-1062`; `systems/fieldwork/sim/knots.py:365-382`; `modules/mass_battle/orchestration.py` grep `:250`, `:333`,
  `:346`; `references/npc_registry.yaml:50-56`, `:138-143` and `grep -c` of `ts:` (32) and `coherence: <n>` (1).
- Ran `t07/worked.py` (`python -I`; seeds 2, 5, 4, 2, 5, 6, 7, 3): every number in §3, including the Coherence log entries.
- Ran `t07/odds.py` (exact convolution of the face rule): every probability in §2.1, §3 and §5; it reproduces the code comment's
  "roughly 0.6 likely at pool 8 and 0.85 at pool 14" (`operations.py:165`) as 0.614 and 0.850.
- Round 2: ran `t07/cm_tc.py` (`python -I`; co-movement draws at Personal and Structural, one threadcut interaction, two perception
  bands); opened `opposing.py:170-174`, `co_movement.py:42-92`, `operations.py:351-360`; `sim_params.json`/`value_pointer_links.json`
  grep for the three constants; `decision/budget.py:18-30`, `data/fixtures.py:484-503`, `decision/choose.py:643-657`;
  `canon/00_philosophical_foundations_rules.md:83`, `canon/philosophy/09_terminology.md:117`, `rosters.yaml:504`, `:524-530`, the
  ED-FI-0009 rows; grep of the tree for `check_coherence_failure_transition|.crossed` and for `locked.zone`/`calamity` in `.py`.
- Scripts: `t07/`. Not opened: threadwork test bodies,
  canon `06_operations.md` / `07_drift.md`, the lexicon proposal itself (taken from extract L13), `co_movement.py`/`threadcut.py`
  bodies beyond the lines cited (from extract C11).
- Round 3 (at `51d7b05`): re-opened `engine/season/harness/populated.py:1525-1536`, `decision/choose.py:407-445`, `loop/driver.py:508-526`,
  `queries/world_q.py:1764-1812`, `rosters.yaml:2736-2742` and `:495-535`, `write_matrix.yaml:183-196`, `state/world.py:1010-1019`,
  `systems/threadwork/sim/operations.py:142-167`, `:235-247`, `:276-288`, `:468-611`, `coherence.py:25-56`, `:64-72`, `:112-120`,
  `:298-377`, `:398-406`, `rendering.py:1-41`, `systems/fieldwork/sim/knots.py:366-380`, `references/alias_registry.yaml:370-380`,
  `canon/philosophy/09_terminology.md:117`, `research/00_INDEX.md:178`, `:258`, the ED-FI-0009 rows; ran `resolvable_verbs()` (47,
  `thread_read` absent) and grepped the tree for readers of `band` and `resting_band`. Precedent claims were checked against the precedent
  research text, not the games.
