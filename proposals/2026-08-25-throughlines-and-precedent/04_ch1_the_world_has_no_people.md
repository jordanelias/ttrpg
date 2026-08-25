# Chapter 1 — The World Has No People In It

**Verification note.** Every locator in this chapter was opened at HEAD `571ae14` unless marked
otherwise. Twenty-two were spot-checked by me directly against the working tree rather than taken
from a lane report; two structured claims were re-derived by parsing (`references/npc_registry.yaml`,
`create_world`'s settlement population); `tools/m1_acceptance.py --summary` was executed; and the
central cost claim of this chapter was established by a **controlled campaign probe with a matched
control arm**, reported in §5. One locator handed to me by the run's own briefing did **not** check
out; §11 reports it.

---

## 1. The claim

Valoria has four working resolution engines and no populated world to run them on. One absent
object — a persistent named person instantiated at world-gen — is the largest connected cause of the
disconnected substrate. That absence is not schedule state; it is a considered, documented, reviewed
disposition, reclassified into permanence and held there by two guards. Its stated blocker is
answerable today from 46 authored `status: canonical` records by a manoeuvre the tree has already
performed once.

That is the thesis. On its own it is nearly vacuous — *"an unfinished game is unfinished"* is a
better description of most pre-integration codebases than it is a diagnosis, and a list of uncalled
functions predicts nothing. Three discriminators are what convert it from an observation into a
finding, and they must travel with it (§4): the emit/consume asymmetry is **one-directional and
extreme**, the absence is **guarded**, and ratification-outrunning-execution is an independently
measured standing class rather than a backlog. The concession that must travel with it too: **nobody
was careless.** Every refusal that composes into an empty world is individually correct
anti-fabrication discipline. The defect is the composition, and nothing in the tree measures it.

One correction to the framing this chapter inherited, established by execution in §5 and material to
every recommendation below: **the two named guards do not guard what they are said to guard.** They
pin the *generator's call counter*, not the world's population. A loader can put people in the world
with both guards green — and will still move four seeded golden constants, through a channel nobody has
named. The repair is cheap and the cost is real; both halves matter.

---

## 2. What is built, so that the absence is legible

The corpus's absences are easy to misread as an unbuilt game. It is not one.

| Subsystem | Executable Python | Scale |
|---|---:|---|
| `systems/mass_battle/sim` | 11,612 | unit / battle |
| `engine/` (substrate, autoload, cross_scale, mc_v18) | 8,942 | spine |
| `systems/combat/combat_engine_v1` | 7,901 | personal |
| `systems/social_contest/sim` | 7,045 | personal |
| `systems/factions/sim` | 2,744 | faction / political |
| `systems/settlements/sim` | 1,012 | settlement / territory |

(Counts from `L0d_engine_census.md`; they are `wc -l` including comments, and this tree comments
heavily. The argument rests on the ratios, which a comment-stripped recount would have to move
materially to overturn. `[UNVERIFIED — I did not re-run the counts]`.)

The three scales that resolve **events** are heavily built. The two scales that hold **persons and
their offices** are the thinnest in the tree; settlements is one-eleventh the size of mass battle.
Valoria has invested in *how a contest resolves* and not in *who is contesting and what they lose*.

---

## 3. The core, narrowed: seven rows, two classes

L0's central evidence was a ten-row table of primitives with zero production callers, presented as
one pattern. It is not one pattern. Under the no-pattern-matching rule — shared **state**, shared
**invariant**, or shared **failure topology by construction**, never grouped by consequence — seven
rows belong and three do not. Narrowing it *strengthens* the finding, because it raises the evidence
class from "grouped by consequence" to "shared invariant, by construction."

**Class (b) — one invariant, four sites.** The invariant is *a personal-scale actor is instantiable
from strategic state*. It is currently false. Flip it and all four change by construction.

| # | Primitive | State at HEAD | Locator (checked by me) |
|---|---|---|---|
| 1 | `npe.generate_npc` — territory-conditioned two-tier generator | works; zero production callers | `systems/world/sim/npe.py:226`; the only non-test mentions are the deferral stub and its telemetry comment, `engine/mc_v18.py:183,195` |
| 2 | `references/npc_registry.yaml` — 46 authored officeholders | zero runtime loaders | parsed: 46 characters, 46 with `role`, 36 with `arc_trajectory`, 7 with `title`; the only `.py` naming it is `tests/valoria/test_references_yaml_parse.py` |
| 3 | `valoria_geography_v30.yaml` `provinces:` block | no production reader | `populate_from_geography` reads only the `settlements:` map (`systems/settlements/sim/registry.py:216-248`); grep for a `provinces` reader in `engine/`+`systems/` returns comments only |
| 4 | `succeed_governor` | zero callers | `systems/settlements/sim/registry.py:199`; grep across every `.py` returns exactly two hits, the `def` and the module-docstring listing at `:24` |

**Class (c) — one failure topology, four sites.** A declared schema field with a production
reader-path and no production writer, all on `Settlement`, all serialized (so they look
implemented), all inert.

| # | Field | State at HEAD | Locator |
|---|---|---|---|
| 5 | `Settlement.add_tag` / the whole relational ledger (`TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}`, `systems/settlements/sim/ledger.py:30`) | zero callers — grep across every `.py` in the tree returns exactly one hit: its own `def` at `registry.py:100` | `registry.py:100-102` |
| 6 | `Settlement.legitimacy` / `.popular_support` | never read or written; the source comment says so itself | `registry.py:69-75` |
| 7 | `Settlement.suspicion` | zero writers; the only other `suspicion` in any `.py` is an unrelated contest-mode comment | `registry.py:78`; `systems/social_contest/sim/contest/modes.py:184` |
| +8 | **`Settlement.pressure: float = 4.0`** — the Π homeostat's own state variable | **zero readers and zero writers** anywhere in `engine/` or `systems/`; I executed `create_world(42)` and every one of the 37 settlements carries the untouched default `4.0` | `registry.py:79`, serialized `:122`; the only other `.pressure` in the tree is `contest/resolver.py:241`, an unrelated venue field |

Row 8 was missing from L0's table and is the sharpest item in the set. Π is the variable behind the
corpus's single most-measured failure — the `PI_RUNAWAY_SUSTAINED` ceiling pin converged on by four
independent measurements. **That runaway is unreachable on `main`, because the meter has no writer.**
The most thoroughly measured defect in Valoria's history sits behind an inert float. (Chapter 4 owns
the accrual/restoration throughline itself; this row is here only as an instance of the writer gap.)

Rows 5–8 are also **downstream** of rows 1–4: nothing writes a Grudge because there is no pair of
persons to hold one; nothing writes `suspicion` because the officer it accrues against does not
exist. Two classes, one root.

**Three rows removed, and why removing them is a win.** `hidden_allegiance` is a *dropped write
inside an existing caller*, not a missing caller — the opposite topology, a different repair, a
different guard; it gets its own treatment in §7. `Standing` was a vocabulary collision promoted to
a mechanism claim; **Chapter 2 owns that correction**, and the run's orchestrator has published a
retraction of its own version of it (`L0g_RETRACTION_standing.md`). It is worth one sentence here
because it is this chapter's method under test: a document arguing that the tree's characteristic
hazard is mistaking a shared word for a shared mechanism has an obligation to record that its own
orchestrator did exactly that, and was caught by the adversarial stage working as designed. The third
removed row — that the ledger's authored tag keys are already intra-polity — is a true statement
about prose data, not a state of the code.

---

## 4. Why this is a pathology and not a schedule

The counter-case is strong and must be stated at full strength: every pre-integration codebase
contains modules written before their call sites; "zero production callers" is the definition of
not-yet-wired; M1 is open, the board is a known-defective instrument, and converting "we have not
finished" into "we have discovered a defect" is precisely the move CLAUDE.md §0.3 identifies as this
repository's characteristic failure.

It is defeated, but only by three discriminators, and any assertion of the thesis without at least
the first two is asserting the vacuous version.

**Discriminator 1 — the asymmetry is one-directional and extreme.** Ordinary integration debt is
roughly symmetric and usually top-down: a caller exists, its callee is stubbed. Valoria's is the
inverse and lopsided. `tools/contract_runtime_conformance.py` at seeded n=2 measured **EMITS declared
60 / observed 3 / matched 0; CONSUMES declared 82 / observed 13 / matched 0; 397 emissions from
exactly three call sites** (`L2` §D.2, quoting suite-07 §4.2) `[not independently re-run by me]`.
Independently, `L1` §A4-24 traced **108 outputs against 7 key-typed inputs, with no gameplay
subsystem taking a Key as input.** A project that is merely unfinished does not declare 60 emitters
and observe 3. That ratio is a fact about *which half of every seam gets written*, not about how far
along the work is.

**Discriminator 2 — the absence is guarded, and this is the decisive one.**
`engine/tests/test_pipeline_reach.py:625-628` holds `test_world_npcs_populated_after_a_seeded_campaign`
at `@pytest.mark.xfail(strict=True)`, under a section header at `:619-623` reading *"world-npcs/
world-knots are Wave-2-RECLASSIFIED to `honest-deferral` — permanently xfail, not 'until a later
wave'"*. Its manifest row (`:135-152`) states the reasoning in full and calls `world.npcs` *"a
PERMANENT deferral until canon specifies a trigger, not a to-do for a later wave."*
`engine/tests/test_f7_smoke_oracle.py:335` asserts `npcs == 0` with the message *"generate_npc may
have live call sites; update the golden."* Both verified verbatim. An ordinary unfinished project
does not ratify its own emptiness in a reviewed manifest and install two guards to hold it there.
This converts "not yet called" into a **design** state rather than a **schedule** state — exactly the
distinction §0.2 exists to force.

The counter-case's best evidence is real and cuts the other way: the same file is a live burn-down
list that **four rows retired in one wave, each confirmed XPASS by execution rather than
inspection**, including `world-settlements` (`test_pipeline_reach.py:638-644`). The backlog is not
ignored. The finding is narrower and worse: **the population of the world with persons was removed
from the backlog by reclassification rather than closed by wiring**, on a ground that is explicitly
conditional — *permanent until canon changes* — and that canon change is a decidable question with
an answer already in the tree.

**Discriminator 3 — ratification outrunning execution is a measured standing class.** Three
instances across three months, each load-bearing on the game: the octagon damage partition ruled
2026-07-30 and still absent (`systems/mass_battle/sim/config.py:210`) `[per L6, not re-checked by
me]`; the opponent-derived-obstacle derivation ruled 2026-08-14, whose own owner's docstring says
*"THAT DERIVATION IS IMPLEMENTED NOWHERE"* (`engine/autoload/dice_engine.py:104-123`) — Chapter 3
owns the obstacle; and Ruling B unexecuted at `operations.py:48-50`. Five lanes, three corpora, one
shape.

**And the concession.** `populate_from_geography`'s golden-safety, the strict xfail's honesty,
`scene_dispatch`'s explicit refusal to invent actors, and OI-05's refusal to fabricate a population
count are all the anti-fabrication discipline of CLAUDE.md §5/§7 working exactly as demanded. **The
defect is that a chain of individually correct refusals composes into a world with nobody in it, and
nothing in the tree measures the composition.**

---

## 5. The composition, measured

Here is what the composition looks like when you execute it rather than describe it.

`systems/overview/sim/accounting.py:139` calls `npe.simulate_npc_actions(world)` **every season**,
under a comment citing `investigation_systems_v30.md` SYSTEM 1 §Persistence. The function
(`npe.py`, `def simulate_npc_actions`) walks `world.npcs`, pairs NPCs in the same territory with an
overlapping worldview and an adjacent stance, and rolls `rng.randint(1, 6)` against their averaged
Volatility to drift them toward each other. It is a real social-drift simulator with a real
consequence, wired into the live loop, and it has been running over an empty dict for its entire
life: 50 seasons × 8 campaigns = **400 invocations per seeded golden batch, zero iterations.** The
engine ticks; there is nobody to tick.

That is the picture. The measurement that follows from it is the load-bearing one, and it corrects
what this run had assumed.

**The received account** (from `L0b` D7, and carried into PART 3's cell-1 cost paragraph): the
loader is *golden-safe by construction*, on the precedent of `populate_from_geography`, whose own
docstring reads *"Deterministic: no RNG draw, so this cannot move any RNG-derived campaign golden
(win_share / battles_mean / scenes_resolved all read `world.rng`, never touched here)"*
(`registry.py:216-221`, verified verbatim). Its stated cost is that the strict xfail and the
`npcs == 0` golden must be re-pinned in the same commit.

**That account is wrong in both directions, and I established it by execution.**

I ran a seeded campaign at `seed=42`, then re-ran the identical campaign with **two** NPC objects
placed into `world.npcs` at world-gen — constructed directly, without calling `generate_npc`, which
is exactly the shape a registry loader would have.

```
BASELINE                     scenes=139  npcs_generated=0  winner=Crown
LOADED (2 NPCs, no generate)  scenes=139  npcs_generated=0  winner=Hafenmark
```

Two people entered the world and the campaign's winner changed. Then the control arm, because a
number without a control is not a measurement: the same loaded world with `simulate_npc_actions`
replaced by a no-op:

```
LOADED + simulate_npc_actions NEUTERED   scenes=139  npcs_generated=0  winner=Crown
```

Byte-identical to baseline. The channel is isolated exactly.

**Three conclusions, all falsifiable and all consequential.**

1. **Neither named guard fires.** `npcs_generated` is `world.npc_counter` (`mc_v18.py:100,307`),
   incremented only in `npe._next_npc_id` (`npe.py:116-122`), which is called only from
   `generate_npc` (`:335`). A loader that constructs `NPC(...)` from authored records and assigns
   the registry's own ids leaves the counter at 0. The `strict=True` xfail still xfails; the
   `npcs == 0` golden still passes. **The world can be populated with both guards green.** The
   guards pin the *generator's call count*, not the *world's population* — a read/write asymmetry
   in the guards themselves, and precisely the §0.1 pt 2 failure: *an assertion must be able to
   observe the failure it excludes.*
2. **The loader is not golden-safe.** `GOLDEN_WIN_SHARE`, `GOLDEN_WINNERS`, `GOLDEN_BATTLES_MEAN`
   and `GOLDEN_SCENES_RESOLVED` (`test_f7_smoke_oracle.py:267-272`) will all move, because
   `simulate_npc_actions` draws from the *shared* `world.rng`, shifting the stream every downstream
   consumer reads. The settlements precedent was safe for a reason nobody stated: **settlements have
   no per-season RNG-drawing consumer wired; `world.npcs` does.** That is the discriminator between
   the two cases, and it was invisible to everyone — including to me until I ran the control.
3. **The fix that restores golden-safety is one function's RNG source.** If
   `simulate_npc_actions` drew from its own deterministic substream instead of `world.rng`, the
   loader would be genuinely golden-safe and the population could land without re-recording
   anything. See recommendation R1.

---

## 6. NERS verdicts

Per BRIEF.md: NERS applies to rolling engines only. Two of the three subjects my commission names are
rolling engines; one explicitly is not, and saying so is the verdict.

**`npe.generate_npc`'s two-tier deviation roll — R FAIL.**
`npe.py:290-334`. `dev_roll = rng.randint(1, 6)`; on `>= 5` (one third of NPCs) a
`flip_choice = rng.randint(0, 4)` selects one of five deviation branches. Branch 2 computes
`hidden_allegiance = rng.choice(other)` at `:327` and the `NPC(...)` constructor at `:336-347` does
not pass it.
- **N — pass.** The roll is not redundant: the four live branches each move a distinct axis.
- **R — FAIL.** A uniform draw over five branches where one is a no-op is a **20% silent-null rate
  within the deviation population, ≈6.7% of all generated NPCs** — a deviation that is rolled,
  recorded in `deviation_roll`, and has no effect. This is invisible to any test that asserts the
  draw happened rather than that its effect landed (§0.1 pt 2 exactly). Graded recoverable output
  fails on that branch: the output is not graded, it is void.
- **S — pass.** The generator is consistent with its sibling conditioning layers; it reads the
  territory's own aggregate state through `_ecology_weights` (`npe.py:186-224`) the same way the
  temperament layer does.
- **E — n/a.** No player surface exists; nothing is intuited from these odds today.

**The loader — NOT A ROLLING ENGINE. NERS does not apply; routed to consistency.**
A `populate_from_registry` would read authored records and register them. There is no draw and there
must not be one. Adding a draw to it — randomising which of the 46 load, or jittering their stats —
would be the **N-inverse**: apparatus added to a mechanism that does not need it, buying variance
Valoria has an entire generator for, and destroying the one property that makes the manoeuvre
citable rather than fabricated (every record has `status: canonical` and a `source`). The correct
verdict here is a refusal to issue one.

**`_emergency_council_parties`' derived contest — a rolling engine whose ENGINE is sound and whose
INPUTS are degenerate.**
`engine/cross_scale/scene_dispatch.py:121-138`, verified verbatim:
`side_a = max(1, round(f.L))`, `side_b = max(1, round(7.0 - f.Sta))`.
- **N — pass.** The contest is not redundant; it is the game's one live intra-faction confrontation.
- **R — pass at the engine level.** Both sides floor at 1; the kernel floors the rolled pool at 5
  regardless of faculty; the derivation carries an explicit `[SEED]` flag rather than pretending to
  be canon.
- **S — FAIL, on inputs.** Both sides are derived from the *same faction's* aggregate stats, both are
  played by identical default policies (`logos_spammer` vs `logos_spammer`, and the module's own
  comment at `:311-316` notes that this makes every verdict deterministically Memory-genre), and the
  echo returns to the same faction (`actor_faction == target_faction`, `:267-268`). A contest whose
  two sides are two projections of one number, resolved by two copies of one policy, is not smooth
  across the seam it sits on — it is a scale transition that transitions nothing.
- **E — FAIL.** There are no legible odds for a player to weigh, because there is no player-visible
  party on either side. Nobody is arguing.

**The verdict that matters:** this is not an engine defect and must not be fixed as one. Migrating
it to deterministic-odds Mode B would be over-correction — it is a healthy resolver being fed two
scalars. **Give the two sides persistent identities and the mechanism is correct as built.**

---

## 7. T-03 — the dropped write

`hidden_allegiance` is the only field in the executable tree whose entire purpose is to model an
agent whose interest diverges from its own faction's. Verified at HEAD: declared at `npe.py:137`,
round-tripped through `to_dict` (`:153`) and `from_dict` (`:169`), computed at `:327`, and omitted
from the `NPC(...)` call at `:336-347`. **Zero reads anywhere in the tree.**

Five lanes independently reported "no executing code models intra-faction divergence." All five
filed it under *absence*. It is not absence — it is a **severed write**, which is a different
finding with a different repair, a different guard and a different detection story. It is also
CLAUDE.md §0.1 pt 1's named characteristic hazard (read/write asymmetry) with a guard template
already in the tree: `tests/valoria/test_morale_write_sweep.py`'s field-parameterized `_CELL_OWNED`
registry, which inherits a new cell-owned field by adding one key.

This is the cheapest verified fix in the entire register: **one constructor argument.** It is also
inert until a loader exists, since nothing reads the field — which is the chapter's thesis restated
at the smallest possible scale.

---

## 8. T-13 — provenance ancestry has one honest writer

`Key.causes` is read by four consumers (corroboration independence, case-board known-unknowns,
evidence quality, `Holding.independent_support`) and populated honestly by one emitter. The one
honest writer is `_apply_accord_echo`'s `scene.accord_echo` Key construction
(`engine/cross_scale/echo_transport.py:328`), whose comment states the discipline exactly: `causes=[caused_by_key_id]` *"when the sibling §5.2 leg fired for
this SAME scene (genuinely already in-log by construction), `[]` when it did not (no genuine
upstream Key exists to cite — never fabricated)"* — verified verbatim in the `scene.accord_echo`
Key construction. Two other sites pass `causes=[]` `[per L1 §C-4; I verified the honest writer, not
the two empty ones]`.

Class (a) — shared state — and it is the one throughline in this chapter that genuinely qualifies as
(a) today, because the field exists and is written. It is also the mechanism by which a person's
history would become queryable: Wildermyth's legacy binding and the Nemesis persistent-encounter log
(P4 §9.1, §9.2) are both, structurally, an ancestry chain on a durable individual record. Valoria
has the chain and not the individual.

---

## 9. Cross-scale: four cells, four verdicts

My commission's assigned cells, each with what crosses, in which direction, and whether it executes.

| Cell | Mark | What crosses | Executes? | Locator |
|---|---|---|---|---|
| **SETTLEMENT → PERSONAL** | **EMPTY** | nothing | no | I executed `create_world(42)`: 37 settlements, **all 37 with `governor_id is None`**, all 37 with `npc_ids` empty. Nothing queues a scene from a settlement. `registry.py:61`, and `populate_from_geography`'s docstring (`:238-241`) states the omission deliberately: *"a later system (charter assignment, governor appointment) is what populates"* |
| **FACTION → PERSONAL** | **BROKEN** | one integer | no | `engine/cross_scale/combat_bridge.py:103-111`: `history = max(1, round(f.Mil))`, then `Combatant(label=fid, history=history)` — every other field a constructor default. Gated behind `DISPATCH_COMBAT_BRIDGE`, default OFF, and unreachable even ON: grep confirms the only production `queue_scene` caller is the generic `queue_triggered_scenes` (`scene_dispatch.py:106`), corroborated at `tools/build_execution_map.py:112`. No `queue_scene("combat", …)` exists |
| **PERSONAL → FACTION** | **EXECUTED (degenerate)** | one stat delta, self-addressed | **yes, by default** | `ECHO_TRANSPORT` default ON (`mc_v18.py:65-75`, Jordan ratification quoted in the docstring). `ctx["echo"] = {"actor_faction": winner_fid, "target_faction": winner_fid, "most_relevant_stat": "Mil", …}` (`scene_dispatch.py:267-268`) — actor and target are the same value |
| **PERSONAL → SETTLEMENT** | **BROKEN** | `scene.accord_echo` → `settlement.order` | carrier yes, producer no | `echo_transport._apply_accord_echo` (`engine/cross_scale/echo_transport.py:211-360`) is fully wired through the accounting boundary (Key construction, `targets[]`, deferred `_apply` closure, registry-clamped write). `classify_scene_outcome`'s own docstring records the dormancy: *"no live producer in the campaign loop sets `echo['scene_outcome']` today (scene_dispatch.py's emergency_council/combat branches, parliamentary_bridge.py's vote ctx — none do)"* |

**Read the four together and the pattern is not subtle.** The one cell that executes is a faction
arguing with itself. Every cell that would require a person is EMPTY, BROKEN, or flag-off. This is
the run's organising sentence and it survives the strongest counter-evidence available: the crossings
that execute are exactly the ones that need no person.

**Cell 1 (S→P, jointly with F→P) unlocks six cells** — with named persons instantiated at world-gen,
P→F stops being degenerate (real actors replace `round(L)` vs `round(7−Sta)`); P→S gains a producer
that can set `echo['scene_outcome']` about somebody; U→P gains a commander to zoom into; S→S gains
pairs for `add_tag` to write Grudges and Leverage about; F→P gains the "concrete duck-typed actors"
whose absence is the literal stated reason `scene_dispatch` defers (`scene_dispatch.py:19-24`); and
F→F gains sub-faction agents.

**Its honest re-pin cost, corrected by §5's probe.** Not what this run believed:

| Guard | Trips on a registry loader? | Why |
|---|---|---|
| `test_pipeline_reach.py:625` `xfail(strict=True)` on `r.npcs_generated > 0` | **NO** | asserts the generator's call counter |
| `test_f7_smoke_oracle.py:335` `assert npcs == 0` | **NO** | same counter |
| `GOLDEN_WIN_SHARE`, `GOLDEN_WINNERS`, `GOLDEN_BATTLES_MEAN`, `GOLDEN_SCENES_RESOLVED` | **YES** | `simulate_npc_actions` (`accounting.py:139`) draws `world.rng.randint(1,6)` per adjacent-stance pair per season, shifting the shared stream |

So the cost of the loader as currently shaped is **a four-constant golden re-record on the seeded
8-campaign oracle** — which CLAUDE.md §7 names as the uncontrolled path (nothing verifies a golden
regeneration was intended), and which this very file demonstrates rotting: `GOLDEN_SCENES_RESOLVED`
is `975` while its own provenance comment trail ends at `967` (`test_f7_smoke_oracle.py:272`), the
2026-08-24 engine swap never having been appended. R1 removes that cost rather than paying it.

---

## 10. Recommendations

Each names the module and function that changes, and states its cost honestly. **R1 must precede
R2**; everything else is independent.

### R1 — Give `simulate_npc_actions` its own RNG substream. *(This is the enabling commit.)*
**Changes:** `systems/world/sim/npe.py::simulate_npc_actions` — replace `rng = world.rng` with a
locally constructed `random.Random` derived deterministically from the world seed and season; and
`engine/autoload/game_state.py::create_world` (`:304`) — store the seed on the world, which it
currently accepts and discards.
**Why:** it is the sole channel by which a population moves a seeded golden, proven by the §5
control arm. Isolating it makes the person loader genuinely golden-safe rather than nominally so.
**Cost:** on today's empty world, the behaviour is byte-identical — `simulate_npc_actions` makes zero
draws over zero pairs, so no golden moves. This is verified in the same probe: the neutered arm
reproduced baseline exactly. **Zero re-pin.** It is also a general hardening: any future subsystem
that populates a collection with a per-season stochastic consumer inherits the same hazard.
**Falsifier:** run the seeded 8-campaign oracle before and after; all four constants must be
unchanged.

### R2 — Write `populate_from_registry`, modelled line-for-line on `populate_from_geography`.
**Changes:** `systems/settlements/sim/registry.py` gains a sibling loader — or, better, a new
`systems/world/sim/npc_loader.py::populate_from_registry(world, path=None)` — reading
`references/npc_registry.yaml`'s 46 `status: canonical` records into `world.npcs` keyed by
`territory`, and setting `Settlement.npc_ids` and `Settlement.governor_id` where a record's `role`
names a governorship. Called from `engine/autoload/game_state.py::create_world` alongside
`populate_from_geography`.
**Why:** OI-05's stated blocker is *"no world-gen initial count … exist[s] in canon to cite"*
(`mc_v18.py:196-200`). Forty-six citable records with per-record `source` fields are a count, and
loading them fabricates nothing — which is the exact value the deferral was protecting. Under
CLAUDE.md's five-test ladder this is test #4, **answered by precedent**, not a `needs_jordan` item.
Copy `populate_from_geography`'s field-mapping discipline exactly: every mapping carries an inline
citation, and a stray value raises rather than silently registering something illegal.
**Cost, honestly:** with R1 landed, **zero golden movement** — the loader draws no RNG and the
per-season consumer no longer shares the stream. Without R1, four constants re-record. Neither named
guard fires either way (§5), which means **the two guards must be rewritten in the same commit, not
because they break, but because they will silently stop meaning what they say.** Rewrite
`test_pipeline_reach.py:625`'s probe to assert on `len(world.npcs)` rather than `npcs_generated`,
and retire its manifest row by execution per the file's own Wave-2 convention. Also: the registry's
own enforcement line — *"No character name may appear in design docs without an entry here"*
(`npc_registry.yaml:5`) — is currently violated by the entire Goldenfurt cast (Konrad Ems, NPC-G06,
is absent; the only "Konrad" in the file is an unrelated archetype reference at `:736`). Loading the
registry makes that violation load-bearing; decide whether the loader is the enforcement point.

### R3 — Pass `hidden_allegiance` to the `NPC(...)` constructor.
**Changes:** `systems/world/sim/npe.py:336-347` — one keyword argument. Plus one key added to
`tests/valoria/test_morale_write_sweep.py`'s `_CELL_OWNED` registry so a future bare assignment
fails the sweep.
**Why:** it converts a 20%-of-deviations silent null into a live branch, and it is the only
divergent-interest primitive in the executable tree.
**Cost:** nothing today (`generate_npc` has no production callers, so no golden observes it). Once
R2 lands and the generator is called, the field becomes observable and the guard earns its place.
Note the guard is justified under §0.1's amended predicate — this artifact's output crosses into the
engine — and the guard is one dictionary key, not a new module.

### R4 — Activate the `accord_echo` producer: set `echo['scene_outcome']` at the one live scene.
**Changes:** `engine/cross_scale/scene_dispatch.py`'s emergency-council branch (around `:308-316`,
where `ctx["echo"]` is already composed) — add a `scene_outcome` member drawn from the closed §5.5
vocabulary (`'governance' | 'destabilisation' | 'territorial_transfer' | 'violence'`), plus a
`target_settlement`. `classify_scene_outcome` already validates against the closed vocabulary and
refuses anything else; `_apply_accord_echo` already clamps the write to the registry-declared
`set.order` bounds.
**Why:** it is the cheapest genuine cross-scale unlock in the matrix — no new mechanism, no ruling,
no new state — and it converts the corpus's one "wired but organically dormant" leg into the first
personal→world consequence in the game. P→S then feeds S→province, which already executes.
**Cost:** the echo's own delta moves `GOLDEN_SCENES_RESOLVED`'s downstream state — a real golden
re-record, argued separately. **And the caveat must travel with it:** this closes a *channel*, not a
*game*. Until R2 lands, what crosses is still a scalar from a scene with nobody in it.
**Ruling needed first:** which §5.5 outcome an emergency-council verdict is, and which settlement it
targets. That is a genuine design call, not an engineering one — it should go to Jordan as one
sentence, not a document.

### R5 — Importance-gate before scaling the cast, and derive rather than track.
**Changes:** design constraint on R2's successor commit, binding on
`systems/world/sim/npe.py::generate_npc`'s eventual production call site.
**Why (precedent):** URR generates every NPC's full vector cheaply and fully simulates only the
~500–700 above a dynamic importance threshold (P4 §3.1) — that is how 46 becomes 460 without a cost
blowup, and it is the reason `simulate_npc_actions`' O(n²) pair loop must not meet an unbounded cast.
Qud's two-phase abstract-then-reify model (P4 §2.2, §S2 row 1) is the general answer to *"how does a
faction-scale event leave a personal-scale trace"* without a script per event: seed the trace as an
abstract annotation at faction scale, reify it only when the personal scale visits — which is also
the anti-scripting-drift shape CLAUDE.md §10 demands. Wildermyth's legacy binding (P4 §S2 row 5, P2
§9.2) is the P→F return leg: a dead or retired officer must leave a **queryable** trace at a higher
scale, and `Key.causes` (§8) is where that trace lives. And P1 A3 (Victoria 3) is the constraint on
all of it: **a top-level number must be derived from the agents backing it, never independently
tracked.** `Faction.standing`, `Settlement.suspicion` and `Settlement.legitimacy` are all currently
independently-tracked top-level numbers with no agents underneath; when persons exist, they should be
derived, not written in parallel.
**Cost:** none yet — this is a constraint on work not yet done, recorded so that R2's success does
not immediately produce the failure P2 §11.4 names as the hardest open problem in the field:
**tracking interior state and expressing it as legible drama are different problems**, and every
precedent that "solves" expression does so by narrowing scope, never generally. Budget for expression
explicitly rather than discovering the Tale-Spin effect after the cast is live.

**What is deliberately not recommended.** No new guard on the apparatus. No new register. No document
whose existence would count as progress. R1–R4 are four functions and one constructor argument.

---

## 11. Falsifier — stated and run

*If any runtime module reads `references/npc_registry.yaml`, or if `generate_npc` acquires a
production call site, or if `world.npcs` is non-empty after a seeded `create_world`, this chapter's
central claim fails.*

All three run by me at `571ae14`:

| Check | Result |
|---|---|
| `grep -rln npc_registry --include=*.py .` | **one file**, `tests/valoria/test_references_yaml_parse.py` — the parse test. SURVIVES |
| production call sites of `generate_npc` | **zero.** All non-test mentions in `engine/`+`systems/` are the deferral stub, its telemetry comment, and the guards. SURVIVES |
| `create_world(seed=42).npcs` | `{}` — and all 37 settlements carry `governor_id is None`, empty `npc_ids`, and `pressure == 4.0`. SURVIVES |

**A locator from my commission that did NOT check out, reported as a finding.** The run's briefing
and PART 4's constraint 6 both state that the live seeded golden win-share is
`{Crown: 37.5, Church: 12.5, Hafenmark: 12.5, Varfell: 37.5}`. It is not. That value sits at
`engine/tests/test_f7_smoke_oracle.py:75`, inside a historical `PREVIOUS` comment block. **The live
constant at HEAD is `GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0,
'Varfell': 12.5}`** (`:267`), re-recorded 2026-08-24 when the mass-battle engine was swapped. The
instruction's *intent* — do not propagate the retracted ~87% figure — is correct and I have not; but
the substitute it supplied is itself superseded, which is the same defect one generation down. The
same file documents why this recurs: *"a golden test pins the LIVE constants; nothing pins the prose,
so a fabricated history stays green forever and the next re-recorder reasons from it"* (`:262-264`) —
a lesson recorded in the very file whose stale line the run then propagated. I note without inferring
that Hafenmark wins 0 of 8 at the live pin; n=8 cannot distinguish a balance fact from noise, and the
file says so at `:8`.

---

## 12. What I did not cover

- **The officer ladder's rungs, promotion gates, demotion, censure, recall, and intra-faction blocs.**
  Chapter 2 owns all of it, and owns the `Standing` correction. Every officer recommendation there is
  gated on R1+R2 here; that dependency is real and should be stated in both directions.
- **VSG's generator algorithm, its slice weighting, its calibration, and the Π homeostat's control
  law.** Chapter 4. I cite `Settlement.pressure`'s zero writers only as an instance of the writer
  gap.
- **The dice substrate, the degree ladder, the obstacle derivation, and the rank-1 `Mil` seam as a
  substrate defect.** Chapter 3.
- **The precedent failure catalogue.** Chapter 5. I name a precedent failure only where it directly
  gates a recommendation (R5's importance-gating and expression-budget constraints).
- **Whether the 46 authored records are *good* characters**, or whether 46 is the right number. I
  verified they exist, parse, carry offices, and are citable. Nothing in this chapter measures
  whether the resulting world is interesting — and per P4 §S5, the field has no validated method for
  that.
- **The conviction-taxonomy split** (canonical 13 vs the live validator's 9 vs npe's 8) named by L1
  §A4-21 as R2's blocker. `npe.py:299-319` records that `CONVICTIONS` is now the canonical thirteen
  and that a roster leak was fixed 2026-08-24; whether the registry's authored vectors validate
  against it is **`[UNVERIFIED]`** and is R2's first implementation risk.
- **`world-knots` (OI-07).** It was reclassified in the same wave and under the same header as
  `world-npcs`, but it is not the same case: knot formation genuinely needs a rule nobody has
  specified, while `world.npcs` needs a loader whose data already exists. Bundling them let the
  harder one's justification carry the easier one. Untangling knots is not this chapter's work.
