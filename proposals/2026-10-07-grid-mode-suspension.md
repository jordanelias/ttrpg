# The grid mode's suspension at ENCOUNTER's barrier

## Status: PROPOSED (2026-10-07) · design-only, builds nothing · reference under `CLAUDE.md` §0.05
## Position: IN-46 (= SM-6), `workplans/valoria_master_workplan_v9_part4.md` · Lane: IN (PC) · IDs: none allocated
## Measured at HEAD `4558f85`. Every `file:line` below was opened at that HEAD; a path without a top-level directory is under `engine/season/`.

A-25 (`_part5` §A, `workplans/valoria_master_workplan_v9_part5.md:411-414`) says the PLAYABLE mode is a
`game/` scene "for which the driver suspends", and that the host gets "the same typed output either way".
This document says where it suspends, what it holds, what it exchanges and why the two modes replay
equal. It does not decide either question #445 `05` holds for Jordan (§4.1, §4.2: J-15). The suspension
works the same however those are answered. One suspension covers **one provider call for one deferred act**.
Whether that call runs one engagement or `fight()`'s whole loop is a §4.1 / M-2 question, and so is
whether a grid fight spans several acts. It does not build the map. No grid exists in the tree
(`requirements.yaml:146-153`), and the map belongs to the scene.

---

## 1. Where the driver suspends

**At ENCOUNTER, inside its one contest call, at the one line where the combat provider calls the engine.**
The call chain, each link opened:

| frame | site |
|---|---|
| the driver mints ENCOUNTER's token and calls the step | `loop/driver.py:459-460` |
| ENCOUNTER fights each declared act in canonical order | `loop/encounter.py:65`, `:72` (`self._contest(...)`) |
| `_contest` takes the dispatch branch because `w.step` is now the declared step | `loop/resolve.py:514-516`, `:576-578` (`contest(...)`) |
| the provider builds both parties and the seed, then calls the engine | `seam/wrappers/combat.py:165`, `:170`, **`:177`** (`wrapper.fight(A, B, rng=random.Random(seed))`) |

**The suspension replaces the call at `combat.py:177` and nothing else.** AUTOMATED keeps that call.
PLAYABLE hands the same arguments to the scene (§3).

**Precondition the build must meet: every fight is deferred to ENCOUNTER, in both modes.** Today the
`the body` prize has no `step:` (`rosters.yaml:1107-1110`), so a `fight` is fought at RESOLVE,
mid-fold. Only `a field` is deferred (`:1111-1115`). The build gives `the body` the same
`step: "ENCOUNTER"` / `declares: "Declared"` pair. `manifest/registry.py:229-262` already validates that
pair. The `fight` verb row also gets `Declared` cells for `writes:` (empty) and for `emits:`, following
`march`'s precedent (`verb_table.yaml:604-612`).

The deferral is the same in both modes, and §4 depends on that. If only PLAYABLE fights were deferred,
the two arms would emit different Events by construction. The cost: any seeded season that reaches a
fight moves its `World.content_hash()`, because it gains a declaration Event and the fight now sees the
round's settled world. **The build re-records those goldens and says so** (`CLAUDE.md` §7). This is the
shape `rosters.yaml:1122-1131` already rules for a deferred prize, so it needs no ruling.

Why ENCOUNTER and not RESOLVE: a suspension inside RESOLVE would hold the fold half-done, with RESOLVE's
loop part-way through the round's acts (`loop/resolve.py:784`). ENCOUNTER runs only after the whole
round has folded, and it holds less (§2). It is the step that exists to fight deferred contests
(`architecture/meta/04_CODE_ARCHITECTURE.md:177`). It is also where mass battle's playable mode would
suspend, through the same `_contest`, so the design adds no second site.

## 2. What the driver holds, and what resumes it

**The suspension is a call-out, not a return.** The scene runs inside the provider's frame, and the
driver stays on the stack below it. Nothing is serialized, and no carrier, field or clock is added.

| held while suspended | where |
|---|---|
| round `r`, the round's `acts`, RESOLVE's `events`, `pending_matter` | `loop/driver.py:440-452` |
| the ENCOUNTER token, minted **once**, as an argument expression | `loop/driver.py:459` |
| `w.step == ENCOUNTER`, set at entry | `loop/encounter.py:49` |
| `declared`, `out`, and the position in `_canonical_order` | `loop/encounter.py:55-65` |
| `A`, `B`, `seed`, the trace list, the previous `_TRACE` hook | `seam/wrappers/combat.py:165-176` |

**No token is minted twice.** `Token` is a frozen `(write_class, tick)` value (`state/gate.py:58-84`).
`mint_token` is its only constructor (`loop/driver.py:80-98`). The suspension calls neither, and the
scene holds no token. A resumable form that **returned** from `season()` and re-entered it was
rejected: re-entry must either mint ENCOUNTER's token a second time or keep one alive past its call,
which `loop/driver.py:428-430` rules out ("MINTED HERE, PASSED IN, NEVER KEPT").

**No draw is consumed or skipped.** The per-tick ordinal resets at `loop/driver.py:423`. Its only game
consumer is `World.new_draw()` (`state/world.py:1239-1242`), which `World.write` calls for a gate
emission's id (`:1132`). The scene holds no `World` and no token, so it cannot reach `World.write`.
An act's own Events use a non-ordinal id (`loop/resolve.py:881`). The fight's randomness is a separate
stream, `random.Random(seed)` with `seed = H(world_seed, tick, a_id, "contest:…")`
(`seam/wrappers/combat.py:170`, `:177`). **The scene draws from that stream only, and in the engine's
order** (§4 c). It never uses its own entropy.

**What resumes it:** the scene returning the typed output of §3. That return is the only resume.
There is no re-entry, no timeout and no second call for the same act. In the port the same frame is
held by an `await` on the scene's completion. That is reference here: the Python oracle's scripted arm
is a plain synchronous call.

## 3. The typed input the host builds and the typed output it takes back

The pair is the one AUTOMATED already uses at `seam/wrappers/combat.py:177`. The build keeps it and
adds no field.

- **Input:** `(A, B, rng)`. `A` and `B` are `Combatant`s from `derive_party`
  (`seam/wrappers/combat.py:108-120`, called at `:165`), and `rng = random.Random(seed)` (`:170`).
- **Output:** the engine's `int` (`+1`/`-1`/`0`, `wrapper.fight`, `systems/combat/combat_engine_v1/wrapper.py:465-496`).
  The other part is the post-fight `WoundTracker` state on `A` and `B`, which the provider reads at
  `seam/wrappers/combat.py:186-206` and returns as the `RESOLVED` dict (`:208-219`). `_contest` folds
  that dict through `degree_of` (`loop/resolve.py:603`).

Everything before and after `:177` is shared code. The output's shape cannot diverge between modes,
so there is no scale-local dialect.

**What PLAYABLE runs instead of `:177`:** the engine's own turn loop (`wrapper.py:477-484`), with the
per-turn choice given as a parameter. Today that choice is fixed: engage every turn until someone is
felled or `max_bouts` is reached. The parameter's default reproduces it exactly, and AUTOMATED is that
default. The seam never re-implements the loop. Because of this, the build edits the combat module's
`fight` as a third file, alongside the entry's two (`loop/driver.py`, `seam/wrappers/combat.py`).
After IN-04 (B-L) that module lives under `modules/combat/`.

The decider's contract:
- It reads the turn index and a read-only view of `A` and `B`.
- It returns one member of a closed set. **[ASSUMPTION: the set is {engage, withdraw}.]** "Withdraw" is
  the loop's existing unresolved exit, taken early. The set is Jordan's *"you choose to attack"*
  (`05:8-11`), and PC's Plan layer (M-4) may widen it without moving the suspension.
- It draws nothing from `rng` and mutates nothing. `_TRACE` already keeps this discipline
  (`wrapper.py:16-19`; `seam/wrappers/combat.py:174-176`).

**The mode is chosen by a party test at the seam** (A-25, `_part5:413`): does either claimant
(`seam/wrappers/combat.py:160`) belong to a person the host plays? The host is one optional argument.
It is threaded along the path `contest_max_depth` and `rng` already take: `season`
(`loop/driver.py:355-357`), then `encounter` (`:459-460`; `loop/encounter.py:72`), then `contest`
(`loop/resolve.py:576-578`), then the provider (`seam/wrappers/combat.py:124-126`). If the argument is
absent, every fight is AUTOMATED, which is today's behaviour. The world surface's player mode uses the
same shape, a host-supplied `choose` passed into `season` (`loop/driver.py:355`).

## 4. Why PLAYABLE and AUTOMATED replay equal when the choices are equal

Six conditions together make the two arms the same computation. Each one names its site.

| | condition | site |
|---|---|---|
| a | **Same step.** The deferral does not depend on mode. | §1; `rosters.yaml:1107-1115` |
| b | **Same input.** It is built by shared lines. The mode enters neither the provider's seed purpose nor `_contest`'s generator purpose. | `seam/wrappers/combat.py:165`, `:170`; `loop/resolve.py:563` |
| c | **Same stream.** The decider draws nothing, so equal choices produce the identical sequence of `rng.random()` calls: `first`, each engagement, then the upset floor. | `wrapper.py:478`, `:480`, `:493` |
| d | **Same output, mode unrecorded.** The `RESOLVED` dict gains no mode field. No Event, id purpose or carrier names the mode. | `seam/wrappers/combat.py:208-219` |
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
  answer it.
