# GO — one draw owner: a single uniform primitive, owned samplers, one constructor

Reconciled: 2026-11-12, U5d closure — folded **A-30** (port randomness: one draw per key; no recorder) and **A-5** (the bell curve everywhere; the port carries one sampler). Kept: one constructor (`draw.seeded`), every unseeded fallback refuses (R6, R8). Withdrawn: the steps that re-specify GO-16 as a recorder of the one primitive and that test the port by replay (R7, R9); the port implements the same keyed hash as the oracle, so there is nothing to record. "Owned samplers as functions of one uniform" narrows to the one sampler A-5 leaves (`roll_net_continuous`'s family); the whole-dice samplers are deleted with the exact-odds table, not ported. The carrying text for the keyed draw is `16_PESSIMIST_GO_keyed_draw_no_recorder.md`; the Layer 1 row (`04` §C.12, "a seeded `RandomNumberGenerator` threaded like `World`") is rewritten by the ruling (text owed, not applied). One re-pin of every seeded result, declared.

## Status: PROPOSED

Carries audit findings F-GO-03 and part of F-GO-01 (`audits/11_GO_audit.md`). Lane: GO, IN (PC and MB
touch one line each). Not ratified by being written (CLAUDE.md §2).

## What it changes in `engine/season/` at runtime

Every generator the loop or a module draws from is built by one function and is one type, whose only
primitive is a uniform in `[0, 1)`. Integer, normal, beta and pick draws become that type's own functions
of the uniform. Uniform-only draw sites keep their stream bit for bit. **The nine non-uniform sites change
stream once: a declared re-pin of every seeded golden that reaches a d10 roll, a fight or a fought
field** (a golden re-record, not a balance claim; the distributions are the same to within 10·2⁻⁵³).

## The problem, with evidence

1. Generators are built in two places. `engine/season/state/ids.py:90` (`draw_factory`) and
   `engine/season/seam/wrappers/combat.py:395`, `:397` (`random.Random(seed)`, the seed from `H` at `:386`).
   Measured, two computed seasons of `build_realm`, `PYTHONHASHSEED=0`: seed 1 builds 2 generators and
   seed 2 builds 4 at `combat.py:397` (53 and 57 draws); none of them passes through the factory GO-16
   plans to record on.
2. Four call sites fall back to an unseeded generator when handed none:
   `seam/wrappers/sigma.py:533`, `engine/dice_engine/dice_engine.py:210`, `:227`,
   `modules/combat/wrapper.py:565`; and `modules/mass_battle/rngsource.py:45`, `:60` falls back to the
   process-global module. None fired in the measured runs. GO-12 names the last one only.
3. Replay cannot test the port's samplers. The oracle calls `randint`, `randrange`, `choice`, `gauss`
   and `betavariate` at nine sites (`queries/world_q.py:1205`; `dice_engine.py:212`, `:233`;
   `modules/combat/wrapper.py:267`, `combat_systems.py:1127`, `:1149`;
   `modules/mass_battle/orchestration.py:1734`, `resolution.py:50`). CPython's versions are not functions
   of a fixed count of uniforms (`randint` uses bit rejection, `gauss` caches a second value,
   `betavariate` is rejection sampling), so a port cannot rebuild them from a uniform stream. Under
   recorded-draw replay the port is handed their *returned values* and its own samplers never run in a
   parity test. In the shipped game they run on every roll.

## The resolution, decided

Ladder step 5 (what makes sense for the architecture), composed on step 4's precedent (`H` is "an OWNED,
VERSIONED mix — never a language built-in", `ids.py:17`; the same argument, one level up). **The oracle
owns its samplers as it owns its hash.**

### The type (new file `engine/dice_engine/draw.py`, a leaf: it imports `random` and `fmath` only)

```
class Draw:
    """One keyed stream. `u()` is the only primitive; every other method is this class's own function
    of `u()`, so a log of uniforms replays the whole stream in any language."""
    key: str                       # the 16-hex `H(seed, tick, subject, purpose)` it was built from
    def u(self) -> float           # [0, 1): the underlying generator's `random()`. THE RECORDER HOOKS HERE.
    def random(self) -> float      # alias of `u`, so the 37 existing `.random()` sites are unedited
    def below(self, n: int) -> int # int(u() * n); refuses n < 1
    def die(self, lo: int, hi: int) -> int      # lo + below(hi - lo + 1)
    def pick(self, seq)            # seq[below(len(seq))]; refuses an empty seq
    def normal(self, mu: float, sigma: float) -> float   # one fixed transform of two uniforms (via fmath)
    def beta(self, a: float, b: float) -> float          # one fixed algorithm over u() (via fmath)

def seeded(key_hex: str) -> Draw   # the ONE constructor: Draw(random.Random(int(key_hex, 16)), key_hex)
```

`normal` and `beta` name their algorithm in the docstring and in `oracle_pins.json`'s `primitives` block
(GO-08), with vectors: inputs, the uniforms consumed, the output bits. Which algorithm is a tuning-free
choice with no game reading; take Box–Muller (two uniforms, no cache) and Cheng's BB/BC or
Marsaglia–Tsang for the gammas, whichever the builder can state exactly `[ASSUMPTION; low; revert: the
other algorithm, one more re-pin]`.

### The edits, by owner

| file | old | new |
|---|---|---|
| `engine/season/state/ids.py:88-90` | `return random.Random(int(H(...), 16))` | `return draw.seeded(H(world_seed, tick_of(), subject_id, purpose))` |
| `engine/season/seam/wrappers/combat.py:386-397` | `seed = int(H(...), 16)` … `random.Random(seed)` twice | `rng = draw_factory(w.world_seed, lambda: w.tick)(a_id, f"contest:{prize}:{…}")`, passed at both calls (same key, so the uniform stream is unchanged) |
| `seam/wrappers/sigma.py:533`; `dice_engine.py:210`, `:227`; `modules/combat/wrapper.py:565` | `rng = rng if rng is not None else random.Random()` and kin | raise `Unspecified`/`TypeError` naming the caller: a missing generator is a defect, never a fresh stream. Workbench and test callers pass `draw.seeded(...)` |
| `modules/mass_battle/rngsource.py:45`, `:60` | default `_stdlib_random` | no default; `get()` outside a `using()` block raises (GO-12's own item, unchanged) |
| the nine non-uniform sites | `rng.randint(1, 10)`, `rng.randrange(n)`, `draw.choice(xs)`, `rng.gauss(m, s)`, `rng.betavariate(a, b)` | `rng.die(1, 10)`, `rng.below(n)`, `draw.pick(xs)`, `rng.normal(m, s)`, `rng.beta(a, b)` |
| GO-16 (plan entry, `workplans/valoria_master_workplan_v11_part5.md:85-95`) | "the factory gains an optional harness-installed recorder that appends, per call, (purpose-key digest, method name, arguments, returned value …) for every method the oracle calls" | "`Draw.u` gains an optional harness-installed recorder that appends `(key, ordinal, the uniform's IEEE-754 bits)`; no other method is recorded, because every other method is a function of `u`" |

`Draw` exposes no `randint`, `gauss`, `choice`, `betavariate`, `shuffle` or `sample`: a call to one is an
`AttributeError` at the site, which is how a tenth site announces itself.

## Order

Before GO-16, GO-08 and GO-15, and inside the same re-pin window as any other declared mover (GO-07's
precedent: one position, one re-pin of every hash). It replaces GO-12's generator item and widens it.

## The gate (execution artifacts)

1. The realm hash at seeds 0–2, one season, **equal** before and after for the uniform-only half (apply
   the type and constructor edits with `die`/`below`/`pick` temporarily delegating to the old methods);
   then the declared re-pin when they stop delegating, with old and new values in the commit body.
2. A counting shim on `random.Random` (the probe at
   `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/GO/go_probe.py`
   is one) over two seasons at seeds 0–2 prints exactly one construction site, `engine/dice_engine/draw.py`,
   and exactly one method drawn, `random`.
3. A second implementation of `below`, `die`, `pick`, `normal` and `beta` written from the docstrings
   alone, fed the recorded uniforms of a pinned fight, reproduces every returned value bit for bit.

## The falsifier

A generator built outside `draw.seeded` makes gate 2 print a second site. A sampler that consumes a
different number of uniforms than its vector states makes gate 3 diverge at the first later draw. A
caller handing `None` raises instead of drawing.

## NERS reading (§0.06; E last)

- **N.** Cut it and replay parity says nothing about the dice the shipped game rolls; no other object
  carries that. Holds from the vertical direction (oracle to port) and the lateral one (two constructors
  become one); narrowed elsewhere, since no player-facing behaviour changes.
- **R.** Completeness: the unseeded fallbacks are the mechanism failing at its extreme (a `None` becomes a
  different game). They become refusals.
- **S.** *Calculations consistent in methodology*: five samplers, one primitive, one constructor, in
  place of six stdlib methods reached two ways.
- **E.** Against what N and R found: one small class replaces a recorder that would have had to
  understand six method signatures. Less to explain to a porter, not more.

## Cost class

Small build. One new leaf file (about 80 lines), about 20 edited lines across `engine/` and `modules/`,
one declared re-pin.

## What this does not decide

The Godot side's uniform source (how a `[0, 1)` double is taken from the engine's generator) is
`valoria-game`'s; nothing here asserts an engine API or version.
