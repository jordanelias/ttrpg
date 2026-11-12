# GO — one draw owner: a single uniform primitive, owned samplers, one constructor

Reconciled: 2026-11-12, U5d closure — folded **A-30** (port randomness: one draw per key; no recorder) and **A-5** (the bell curve everywhere; the port carries one sampler). Kept: one constructor (`draw.seeded`), every unseeded fallback refuses (R6, R8). Withdrawn: the steps that re-specify GO-16 as a recorder of the one primitive and that test the port by replay (R7, R9); the port implements the same keyed hash as the oracle, so there is nothing to record. "Owned samplers as functions of one uniform" narrows to the one sampler A-5 leaves (`roll_net_continuous`'s family); the whole-dice samplers are deleted with the exact-odds table, not ported. The carrying text for the keyed draw is `16_PESSIMIST_GO_keyed_draw_no_recorder.md`; the Layer 1 row (`04` §C.12, "a seeded `RandomNumberGenerator` threaded like `World`") is rewritten by the ruling (text owed, not applied). One re-pin of every seeded result, declared.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — the body is brought to its head: rows applied: `R1_READ.md` §1.4 and §2 row A-30 (`Draw.u()` is a function of `(key, n)` by an owned mix, `16_PESSIMIST_GO_keyed_draw_no_recorder.md`'s body, never CPython's Mersenne Twister; the recorder hook, gate 3's replay wording and the GO-16 recorder row are removed; one constructor and the refusals kept), §1.4's `rngsource` row (AMBIGUOUS; Option A taken: the field's `Draw` is threaded as `resolve_field`'s `rng` parameter, as `fight` takes its stream, matching `04` §C.12 rejection 4 and `R1_READ.md` 7b-13's reasoning for the config; `rngsource` is retired, with GO-12's no-default item as the interim), `U3_CONFLICT_LEDGER.md` C3-Y10 (co-lands with the pessimist file in B06; that file's key function is this body), C3-D3 (lands before the task draw, B07); `U5b_PC_residue.md` §4 as reconciled (`wrapper.py:565`'s fallback is removed by a signature with no default stream, not a raise); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`). **Placement note:** the pessimist file puts `H2` in `engine/season/state/ids.py` beside `H`; `draw.py` is a leaf under `engine/dice_engine/` and may not import `engine/season`, so `H2` is defined once in `draw.py` (`hashlib`'s blake2b) and `ids.py` imports it `[ASSUMPTION: the leaf's import rule decides the home — basis: this file's own "imports `random` and `fmath` only" and CLAUDE.md §3; reported for R5's lane]`.

Reconciled: 2026-11-12, U6 repair lane R-C (`unified/U6_VERDICT_AND_REPAIRS.md` finding 5, A-30): the `Draw` docstring states once, at the owner, that the index `n` is part of the key, so "one draw per key" holds and a keyed draw is a function of its key alone; `16_PESSIMIST_GO_keyed_draw_no_recorder.md` points here. `H2`'s home is R-A's and is not touched.

**Depends on:** `U5a_DICE_owed_edits.md` §1 (B05: the one sampler); `11_GO_float_contract.md` Part A (`fmath`, B06); `16_PESSIMIST_GO_keyed_draw_no_recorder.md` (B06, co-land).
**Lands in batch:** B06 (`B06-keyed-draw`, IN/GO), with `11_GO_float_contract.md`, `16_PESSIMIST_GO_keyed_draw_no_recorder.md`, `U5d_GO_owed_edits.md` and `11_GO_pointer_and_stale_text_resolutions.md` item 5; before B07's task draw (C3-D3).

## Status: PROPOSED

Carries audit findings F-GO-03 and part of F-GO-01 (`audits/11_GO_audit.md`). Lane: GO, IN (PC and MB
touch one line each). Not ratified by being written (CLAUDE.md §2).

## What it changes in `engine/season/` at runtime

Every generator the loop or a module draws from is built by one function and is one type, whose only
primitive is a uniform in `[0, 1)` computed from its key and an ordinal by an owned mix. Integer, normal,
beta and pick draws become that type's own functions of the uniform. *(W3-1, A-30:)* every draw site
changes stream once, because the uniform's source changes from CPython's generator to the owned mix: **one
declared re-pin of every seeded result** (a golden re-record, not a balance claim).

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

### The type (new file `engine/dice_engine/draw.py`, a leaf: it imports `hashlib` and `fmath` only)

```
class Draw:
    """One keyed draw. `u()` is the only primitive, a function of (key, n) by an owned mix (A-30); every
    other method is this class's own function of `u()`, so the same key gives the same values in any
    language that implements the mix. The index `n` is part of the key: the n-th uniform is the draw keyed
    `(H(seed, tick, subject, purpose), n)`, so A-30's "one draw per key" holds with the index counted in the
    key, and no uniform depends on anything but its key. No recorder: there is nothing to record."""
    key: str                       # the 16-hex `H(seed, tick, subject, purpose)` it was built from
    n: int = 0                     # uniforms taken from this key
    def u(self) -> float           # the n-th uniform: n = 0 is the key itself, later ones H2(key, n);
                                   # (word >> 11) / 2**53  (16_PESSIMIST_GO_keyed_draw_no_recorder.md's body)
    def random(self) -> float      # alias of `u`, so the 37 existing `.random()` sites are unedited
    def below(self, n: int) -> int # int(u() * n); refuses n < 1
    def die(self, lo: int, hi: int) -> int      # lo + below(hi - lo + 1)
    def pick(self, seq)            # seq[below(len(seq))]; refuses an empty seq
    def normal(self, mu: float, sigma: float) -> float   # one fixed transform of two uniforms (via fmath)
    def beta(self, a: float, b: float) -> float          # one fixed algorithm over u() (via fmath)

def H2(key_hex: str, n: int) -> str  # blake2b(f"v1d|{key_hex}|{n}", digest_size=8); defined here (leaf), imported by ids.py
def seeded(key_hex: str) -> Draw     # the ONE constructor: Draw(key_hex)
```

`normal` and `beta` name their algorithm in the docstring and in `oracle_pins.json`'s `primitives` block
(GO-08), with vectors: inputs, the uniforms consumed, the output bits; GO-08 also gains twelve
`(key, n) → u` vectors (IEEE-754 hex), including `n = 0`, `n = 1` and a key at or above 2^63. Which algorithm is a tuning-free
choice with no game reading; take Box–Muller (two uniforms, no cache) and Cheng's BB/BC or
Marsaglia–Tsang for the gammas, whichever the builder can state exactly `[ASSUMPTION; low; revert: the
other algorithm, one more re-pin]`.

### The edits, by owner

| file | old | new |
|---|---|---|
| `engine/season/state/ids.py:88-90` | `return random.Random(int(H(...), 16))` | `return draw.seeded(H(world_seed, tick_of(), subject_id, purpose))` |
| `engine/season/seam/wrappers/combat.py:386-397` | `seed = int(H(...), 16)` … `random.Random(seed)` twice | `rng = draw_factory(w.world_seed, lambda: w.tick)(a_id, f"contest:{prize}:{…}")`, passed at both calls (same key, so the uniform stream is unchanged) |
| `seam/wrappers/sigma.py:533`; `dice_engine.py:210`, `:227`; `modules/combat/wrapper.py:565` | `rng = rng if rng is not None else random.Random()` and kin | *(W3-1: no new raise on a port-reached path, `hol` §53; `U5b_PC_residue.md` §4 as reconciled)* the stream parameter loses its default, so a missing generator is a signature error at the call site, never a fresh stream. Workbench and test callers pass `draw.seeded(...)` |
| `modules/mass_battle/rngsource.py:45`, `:60` | default `_stdlib_random` | *(W3-1, R1 §1.4 Option A)* `resolve_field(inp, rng, *, cfg=None, …)` receives its `Draw` as `rng`, as `fight` does, and threads it to `battle_loop.run_battle`; each draw site keys its draw by purpose (`27_MB_A` §4's `(field, tick, unit, purpose)`); `rngsource` is retired. Interim, until the threading lands: no default, and `get()` outside a `using()` block raises (GO-12's item) |
| the nine non-uniform sites | `rng.randint(1, 10)`, `rng.randrange(n)`, `draw.choice(xs)`, `rng.gauss(m, s)`, `rng.betavariate(a, b)` | `rng.die(1, 10)`, `rng.below(n)`, `draw.pick(xs)`, `rng.normal(m, s)`, `rng.beta(a, b)` |
| GO-16 (plan entry, `workplans/valoria_master_workplan_v11_part5.md:85-95`) | "the factory gains an optional harness-installed recorder …" | *(W3-1, A-30)* "**Not built.** The port implements the same keyed hash (`draw.py::u`, `H2`); parity is the `(key, n) → u` vectors in GO-08 and a `content_hash` comparison at any seed. No recorder, no `export_oracle_draws.py`, no `oracle_draws.json`" |

`Draw` exposes no `randint`, `gauss`, `choice`, `betavariate`, `shuffle` or `sample`: a call to one is an
`AttributeError` at the site, which is how a tenth site announces itself.

## Order

Before GO-08 and GO-15 (GO-16 is not built), after the one sampler (B05), and inside the same re-pin window
as any other declared mover (GO-07's precedent: one position, one re-pin of every hash). It replaces GO-12's
generator item and widens it.

## The gate (execution artifacts)

1. *(W3-1, A-30.)* The realm hash at seeds 0–2, one season: the same seed twice gives the same hash; the
   declared re-pin of every seeded result, with old and new values in the commit body.
2. No generator outside `draw.seeded`: `rg -n "random\.Random\(" engine/season engine/dice_engine modules`
   (tests excluded) prints nothing; written first as the test
   `tests/valoria/test_one_draw_owner.py::test_no_random_Random_in_runtime_code` (the scratch `go_probe.py`
   counting shim is not needed and is not written).
3. A second implementation of `u`, `below`, `die`, `pick`, `normal` and `beta` written from the docstrings
   alone, fed the same keys, reproduces the GO-08 vectors bit for bit (`engine/tests/test_draw.py::test_n_zero_is_the_key_itself`,
   `::test_n_one_remixes_with_h2`, `::test_samplers_match_their_vectors`).

## The falsifier

A generator built outside `draw.seeded` makes gate 2 print a site. A sampler that consumes a different
number of uniforms than its vector states makes gate 3 diverge at the first later draw. A caller handing no
stream fails at the call site instead of drawing.

## NERS reading (§0.06; E last)

- **N.** Cut it and replay parity says nothing about the dice the shipped game rolls; no other object
  carries that. Holds from the vertical direction (oracle to port) and the lateral one (two constructors
  become one); narrowed elsewhere, since no player-facing behaviour changes.
- **R.** Completeness: the unseeded fallbacks are the mechanism failing at its extreme (a `None` becomes a
  different game). They become refusals.
- **S.** *Calculations consistent in methodology*: five samplers, one primitive, one constructor, in
  place of six stdlib methods reached two ways.
- **E.** Against what N and R found: one small class and one owned mix replace a recorder that would have
  had to understand six method signatures. Less to explain to a porter, not more.

## Cost class

Small build. One new leaf file (about 80 lines), about 20 edited lines across `engine/` and `modules/`,
one declared re-pin. **Lands (W3-1):** an IN-lane implementation session under `/methodology-execute` with GO,
PC and MB review; `sonnet` for the edits, `opus` for the re-pin's reading.

## What this does not decide

The Godot side's uniform source (how a `[0, 1)` double is taken from the engine's generator) is
`valoria-game`'s; nothing here asserts an engine API or version.
