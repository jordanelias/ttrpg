# The grid mode's suspension at ENCOUNTER's barrier

## Status: PROPOSED (2026-10-07) · design-only, builds nothing · reference under `CLAUDE.md` §0.05 · re-read against the moved `combat` container at B-L (`## Re-read at B-L`, HOLDS WITH CORRECTIONS); the hold on ratification-on-merge (ED-1094) lapsed at that re-read, and the PR body lists it as held back until Jordan reads it
## Position: IN-46 (= SM-6), `workplans/valoria_master_workplan_v9_part4.md` · Lane: IN (PC) · IDs: none allocated
## Measured at HEAD `4558f85`; every `file:line` below re-derived by symbol at `36b40ee2` (B-L, after IN-04 moved `combat`), see `## Re-read at B-L`. A path without a top-level directory is under `engine/season/`.

A-25 (`_part5` §A, `workplans/valoria_master_workplan_v9_part5.md:315-318`) says the PLAYABLE mode is a
`game/` scene "for which the driver suspends", and that the host gets "the same typed output either way".
This document says where it suspends, what it holds, what it exchanges and why the two modes replay
equal. It does not decide either question #445 `05` holds for Jordan (§4.1, §4.2: J-15). The suspension point (§1-§2)
works the same however those are answered; §3-§4 design the whole-`fight()` variant, and M-2's per-act
`engagement()` variant is re-read at B-L. One suspension covers **one provider call for one deferred act**.
Whether that call runs one engagement or `fight()`'s whole loop is a §4.1 / M-2 question, and so is
whether a grid fight spans several acts. It does not build the map. No grid exists in the tree
(`requirements.yaml:146-153`), and the map belongs to the scene.

---

## 1. Where the driver suspends

**At ENCOUNTER, inside its one contest call, at the one line where the combat module's entry calls the engine.**
The call chain, each link opened:

| frame | site |
|---|---|
| the driver mints ENCOUNTER's token and calls the step | `loop/driver.py:460-461` |
| ENCOUNTER fights each declared act in canonical order | `loop/encounter.py:65`, `:72` (`self._contest(...)`) |
| `_contest` takes the dispatch branch because `w.step` is now the declared step | `loop/resolve.py:711-713`, `:773-775` (`contest(...)`) |
| the seam calls the provider the prize row names | `seam/contest.py:163` (`_run(...)`) |
| the host adapter builds the typed record and the seed, then calls the module entry | `seam/wrappers/combat.py:217` (`combat_input`), `:222` (seed), `:226` (`entry.fn(inp, random.Random(seed))`) |
| the module entry builds both parties, then calls the engine | `modules/combat/fight.py:45`, **`:52`** (`wrapper.fight(A, B, rng=rng)`) |

**The suspension replaces the call at `fight.py:52` and nothing else.** AUTOMATED keeps that call.
PLAYABLE hands the same arguments to the scene (§3). Since IN-04 that call is inside the module, not the
host adapter; the adapter's `combat.py:226` is where the host hands over (`## Re-read at B-L`).

**Precondition the build must meet: every fight is deferred to ENCOUNTER, in both modes.** Today the
`the body` prize has no `step:` (`rosters.yaml:1116-1120`), so a `fight` is fought at RESOLVE,
mid-fold. Only `a field` is deferred (`:1121-1126`). The build gives `the body` the same
`step: "ENCOUNTER"` / `declares: "Declared"` pair. `manifest/registry.py:237-268` (`_check_step_declares`,
called from `check_rows`) already validates that pair. Every verb contesting `the body` gets `Declared`
cells for `writes:` (empty) and for `emits:`, following `march`'s precedent (`verb_table.yaml:662-672`):
`fight` (`:460`) and `accept` (`:585`), since the deferral is the prize's and `accept` contests it too.

The deferral is the same in both modes, and §4 depends on that. If only PLAYABLE fights were deferred,
the two arms would emit different Events by construction. The cost: any seeded season that reaches a
fight moves its `World.content_hash()`, because it gains a declaration Event and the fight now sees the
round's settled world. **The build re-records those goldens and says so** (`CLAUDE.md` §7). This is the
shape `rosters.yaml:1127-1141` already rules for a deferred prize, so it needs no ruling.

Why ENCOUNTER and not RESOLVE: a suspension inside RESOLVE would hold the fold half-done, with RESOLVE's
loop part-way through the round's acts (`loop/resolve.py:912`). ENCOUNTER runs only after the whole
round has folded, and it holds less (§2). It is the step that exists to fight deferred contests
(`architecture/meta/04_CODE_ARCHITECTURE.md:177`). It is also where mass battle's playable mode would
suspend, through the same `_contest`, so the design adds no second site.

## 2. What the driver holds, and what resumes it

**The suspension is a call-out, not a return.** The scene runs inside the provider's frame, and the
driver stays on the stack below it. Nothing is serialized, and no carrier, field or clock is added.

| held while suspended | where |
|---|---|
| round `r`, the round's `acts`, RESOLVE's `events`, `pending_matter` | `loop/driver.py:440-453` |
| the ENCOUNTER token, minted **once**, as an argument expression | `loop/driver.py:460` |
| `w.step == ENCOUNTER`, set at entry | `loop/encounter.py:49` |
| `declared`, `out`, and the position in `_canonical_order` | `loop/encounter.py:55-65` |
| the typed record `inp` and `seed` (the host adapter's frame) | `seam/wrappers/combat.py:217`, `:222` |
| `A`, `B`, the trace list, the previous `_TRACE` hook (the module entry's frame) | `modules/combat/fight.py:45-47` |

**No token is minted twice.** `Token` is a frozen `(write_class, tick)` value (`state/gate.py:58-84`).
`mint_token` is its only constructor (`loop/driver.py:80-98`). The suspension calls neither, and the
scene holds no token. A resumable form that **returned** from `season()` and re-entered it was
rejected: re-entry must either mint ENCOUNTER's token a second time or keep one alive past its call,
which `loop/driver.py:429-431` rules out ("MINTED HERE, PASSED IN, NEVER KEPT").

**No draw is consumed or skipped.** The per-tick ordinal resets at `loop/driver.py:423`. Its only game
consumer is `World.new_draw()` (`state/world.py:1276-1279`), which `World.write` calls for a gate
emission's id (`:1161`). The scene holds no `World` and no token, so it cannot reach `World.write`.
An act's own Events use a non-ordinal id (`loop/resolve.py:1090`, `_act_events`). The fight's randomness is a separate
stream, `random.Random(seed)` with `seed = H(world_seed, tick, a_id, "contest:…")`
(`seam/wrappers/combat.py:222`, `:226`). **The scene draws from that stream only, and in the engine's
order** (§4 c). It never uses its own entropy.

**What resumes it:** the scene returning the typed output of §3. That return is the only resume.
There is no re-entry, no timeout and no second call for the same act. In the port the same frame is
held by an `await` on the scene's completion. That is reference here: the Python oracle's scripted arm
is a plain synchronous call.

## 3. The typed input the host builds and the typed output it takes back

The pair is the one AUTOMATED already uses at `modules/combat/fight.py:52`. The build keeps it and
adds no field to the typed record.

- **Input:** the host's `PersonalCombatInput` (`queries/inputs.py:44-59`: the claimants, each one's
  derived `end`, the wound quantities to lift), built by `combat_input` (`seam/wrappers/combat.py:141-151`,
  from `party_end`, `:130-138`; called at `:217`), and an `rng` seeded from the seed at `:222`
  (`random.Random(seed)` is built inline at `:226`). The entry turns the record into `Combatant`s `A`
  and `B` (`modules/combat/fight.py:45`) and calls `wrapper.fight(A, B, rng=rng)` (`:52`).
- **Output:** the engine's `int` (`+1`/`-1`/`0`, `wrapper.fight`, `modules/combat/wrapper.py:487-532`).
  The other part is the post-fight `WoundTracker` state on `A` and `B`, which the entry lifts
  (`modules/combat/fight.py:56-69`) and the adapter refuses-by-name and returns as the `RESOLVED` dict
  (`seam/wrappers/combat.py:217-253`). `_contest` folds that dict through `degree_of`
  (`loop/resolve.py:800`).

Everything before and after `fight.py:52` is shared code. The output's shape cannot diverge between modes,
so there is no scale-local dialect.

**What PLAYABLE runs instead of `fight.py:52`:** the engine's own turn loop (`wrapper.py:504-523`), with the
per-turn choice given as a parameter. Today that choice is fixed: engage every turn until someone is
felled or `max_bouts` is reached. The parameter's default reproduces it exactly, and AUTOMATED is that
default. The seam never re-implements the loop. Because of this, the build edits the engine's
`wrapper.fight` (`modules/combat/wrapper.py`) and the module entry that calls it (`modules/combat/fight.py`),
alongside the host's two (`loop/driver.py`, `seam/wrappers/combat.py`); see `## Re-read at B-L`.

The decider's contract:
- It reads the turn index and a read-only view of `A` and `B`.
- It returns one member of a closed set. **[ASSUMPTION: the set is {engage, withdraw}.]** "Withdraw" is
  the loop's existing unresolved exit, taken early. The set is Jordan's *"you choose to attack"*
  (`05:8-11`), and PC's Plan layer (M-4) may widen it without moving the suspension.
- It draws nothing from `rng` and mutates nothing. `_TRACE` already keeps this discipline
  (`wrapper.py:9-19`; `modules/combat/fight.py:47-54`).

**The mode is chosen by a party test at the seam** (A-25, `_part5:317`): does either claimant
(`seam/wrappers/combat.py:212-216`) belong to a person the host plays? The host is one optional argument.
It is threaded along the path `contest_max_depth` and `rng` already take: `season`
(`loop/driver.py:355-357`), then `encounter` (`:460-461`; `loop/encounter.py:72`), then `contest`
(`loop/resolve.py:773-775`; `seam/contest.py:163`), then the provider (`seam/wrappers/combat.py:179-182`),
then the module entry (`:226`; `modules/combat/fight.py:32`). If the argument is
absent, every fight is AUTOMATED, which is today's behaviour. The world surface's player mode uses the
same shape, a host-supplied `choose` passed into `season` (`loop/driver.py:355`).

## 4. Why PLAYABLE and AUTOMATED replay equal when the choices are equal

Six conditions together make the two arms the same computation. Each one names its site.

| | condition | site |
|---|---|---|
| a | **Same step.** The deferral does not depend on mode. | §1; `rosters.yaml:1116-1126` |
| b | **Same input.** It is built by shared lines. The mode enters neither the provider's seed purpose nor `_contest`'s generator purpose. | `seam/wrappers/combat.py:217`, `:222`; `loop/resolve.py:760` |
| c | **Same stream.** The decider draws nothing, so equal choices produce the identical sequence of `rng.random()` calls: `first`, each engagement, then the upset floor. | `modules/combat/wrapper.py:514`, `:516`, `:529` |
| d | **Same output, mode unrecorded.** The `RESOLVED` dict gains no mode field. No Event, id purpose or carrier names the mode. | `seam/wrappers/combat.py:232-253` |
| e | **Same order.** The scene runs where its act falls in canonical order. The host never reorders, for example by putting the player's fights last. | `loop/encounter.py:65` |
| f | **No write, no mint, no draw during the suspension.** | §2 |

When a choice differs (withdraw on a turn where the default engages), fewer engagements run. The wound
state, the degree `degree_of` reads and the fold all change, so the hash moves. That is why the
instrument can fail.

## The falsifier the build must pass

Verbatim from the entry (`_part4`, IN-46): **"at the build, one seeded season run twice — AUTOMATED, and
PLAYABLE with scripted choices equal to the chooser's — ends at one `World.content_hash()`, and a
scripted choice that differs from the chooser's moves it (the instrument can fail); a suspension that
consumes a draw or mints a token twice reds the first"**

As a test the build must pass, the run makes three arms on one seed:
1. AUTOMATED (no host).
2. PLAYABLE, with a scripted decider that returns the default every turn.
3. PLAYABLE, with a scripted decider that withdraws after turn 1.

It asserts all of the following:
- `hash(1) == hash(2)`.
- `hash(3) != hash(1)`.
- The count of `mint_token` calls is equal in arms 1 and 2.
- The PLAYABLE arms entered the suspension at least once, and at least one suspended fight ran two
  or more turns under the default decider. Without that, arm 3 cannot differ (`CLAUDE.md` §0.1 pt 2).

Arms 1 and 2 must not be identical by construction (`CLAUDE.md` §7). So arm 2 must actually route
through the scene path, and the test asserts the suspension ran.

## Not decided here

- #445 `05` §4.1 and §4.2 (J-15).
- The grid map.
- M-1 (returning the trace).
- Whether the Godot port's combat module reproduces Python's `random.Random` stream. That is the port's
  parity question (`CLAUDE.md` §6). Replay equality in the port depends on it, and this design does not
  answer it. The port-seam audit records it (`ED-IN-0017`'s last row, finding F5).

## Re-read at B-L

A terminal record, kept where its subject lives (`CLAUDE.md` §0); it dies with this document.

**Date:** 2026-10-12, at HEAD `36b40ee2` (the seam files are unchanged since `5422ed1e`, IN-05's close). Every `combat.py` line cited in this document was re-derived by symbol again at HEAD `175384fc`, after later B-L commits (the `/simplify` pass among them) moved the adapter's lines; the cites below carry the HEAD `175384fc` numbers.
**Verdict: HOLDS WITH CORRECTIONS.** The design was re-read against the moved `combat` container
(IN-04, plan position `31b`): the host adapter `seam/wrappers/combat.py` is now an input builder
(`combat_input`) plus an adapter (`resolve`), and the fight is the module entry `modules/combat/fight.py`,
reached by string through `MODULE_ENTRIES`. Every site was re-derived by symbol and opened at that HEAD.

**The four answers.**
1. *Where it suspends:* **holds.** Still ENCOUNTER, still inside one provider call for one deferred act.
   The call it replaces has moved one frame down, from the adapter to the entry (`fight.py:52`); the
   chain gains two frames (`seam/contest.py:163`, `fight.py:32`). `the body` still has no `step:`, so the
   precondition is unchanged.
2. *What it holds:* **holds.** It is still a call-out with the driver on the stack. The Combatants, the
   trace list and the `_TRACE` hook now sit in the entry's frame, which A-25 makes transient (`fight.py:12-14`:
   no `World`, no token, no state between calls). That makes the "no write, no mint" condition
   structural where it was observed.
3. *The typed pair:* **holds, corrected.** The pair is no longer `(A, B, rng) -> int`. It is
   `PersonalCombatInput` plus `rng` into the entry, and the entry's dict (`fight.py:67-69`) that the
   adapter turns into the `RESOLVED` dict. That dict now also carries `surrender` (`combat.py:243`; §11.4
   yield, PC-01). No field is added for the mode, and the record gains no field.
4. *Replay equality:* **holds.** All six conditions re-sited. (c) survives the new §11.4 yield path:
   a declared yield fires before every draw of its turn and draws nothing (`wrapper.py:505-513`), and
   AUTOMATED passes no `yield_decl` (`fight.py:52`).

**Where the split changes the build.**
- The per-turn choice parameter lands in `modules/combat/` now, in TWO files: the engine
  (`wrapper.py::fight`, `:487`) and the entry that forwards it (`fight.py::fight`, `:32`). The host's
  two files are unchanged in role. The build also edits `rosters.yaml` (`the body`'s `step:`/`declares:`),
  `verb_table.yaml` (`Declared` cells on `fight` AND `accept`) and threads the host keyword through
  `seam/contest.py:163`'s uniform provider call. Every provider accepts and ignores it (`sigma.py:152-154`,
  `mass_battle.py:150-152`), on `rung`'s precedent. The IN-46 entry's EDITS list names three files.
- **The decider now crosses the module boundary outward.** It is host code, either the scene or the
  scripted arm, and the module calls it. The module builds `A` and `B` (`fight.py:45`), so a decider
  handed the "read-only view of `A` and `B`" would read module objects. The build types that view.
  [ASSUMPTION: on the quantities the record already names (`wound_quantities`) plus the turn index,
  never a `Combatant`.]
- The decider is a parameter, never a module attribute. `fight.py:47-54` rebinds `wrapper._TRACE` for
  the call, and that is the precedent NOT to follow (`ED-IN-0017`'s last row, F4).
- **The engine now has a second early exit.** The §11.4 yield (`yield_decl`, `wrapper.py:487-513`)
  ends the scene with `result != 0` and no upset draw. "Withdraw" as written is the UNRESOLVED exit
  (`result == 0`). The [ASSUMPTION] set is unchanged. Whether the decider's set gains `yield`, or
  whether withdraw is that path, is PC's Plan layer (M-4) and #445 `05` §4.1 (J-15). It is not decided here.
- The three entries share one call shape, `(inp, rng)` (`roll.py:30`, `fight.py:32`,
  `massbattle.py:297`). The decider is a keyword with a `None` default, so the AUTOMATED call is
  byte-identical. Mass battle's playable mode would take the same keyword rather than a second shape.

**Corrected cites (old -> new, all re-opened):** `driver.py:459-460` -> `:460-461`; `:459` -> `:460`;
`:440-452` -> `:440-453`; `:428-430` -> `:429-431`; `resolve.py:514-516` -> `:711-713`; `:576-578` ->
`:773-775`; `:563` -> `:760`; `:603` -> `:800`; `:784` -> `:912`; `:881` -> `:1090`; `combat.py:177` ->
`fight.py:52` (adapter hand-over `combat.py:226`); `combat.py:165` -> `:217` (`combat_input`); `:170` ->
`:222`; `:108-120` (`derive_party`, retired) -> `:130-151` (`party_end`, `combat_input`) and `fight.py:45`;
`:186-206` -> `fight.py:56-69` and `combat.py:158-176`, `:230`; `:208-219` -> `:232-253`; `:174-176` ->
`fight.py:47-54`; `:160` -> `:212-216`; `:124-126` -> `:179-182`; `:165-176` (held state) -> `combat.py:217,222`
and `fight.py:45-47`; `systems/combat/combat_engine_v1/wrapper.py:465-496` -> `modules/combat/wrapper.py:487-532`;
`wrapper.py:477-484` -> `:504-523`; `:478`/`:480`/`:493` -> `:514`/`:516`/`:529`; `:16-19` -> `:9-19`;
`rosters.yaml:1107-1110` -> `:1116-1120`; `:1111-1115` -> `:1121-1126`; `:1122-1131` -> `:1127-1141`;
`:1107-1115` -> `:1116-1126`; `manifest/registry.py:229-262` -> `:237-268`; `verb_table.yaml:604-612` ->
`:662-672`; `state/world.py:1239-1242` -> `:1276-1279`; `:1132` -> `:1161`; `_part5:411-414` -> `:315-318`;
`_part5:413` -> `:317`. Unchanged and re-opened: `driver.py:80-98`, `:355-357`, `:423`;
`encounter.py:49`, `:55-65`, `:65`, `:72`; `state/gate.py:58-84`; `04_CODE_ARCHITECTURE.md:177`;
`requirements.yaml:146-153`; `05_two_modes_of_one_bout.md:8-11`.

**Not decided here.** The re-read is done. Status stays **PROPOSED**. The hold on ratification-on-merge
was set "until the B-L re-read" (`workplans/valoria_master_workplan_v9_part4.md:34`, IN-46), so it lapsed
at this re-read; "released only by Jordan" is IN-47's rule (`part4:41`), not IN-46's.
