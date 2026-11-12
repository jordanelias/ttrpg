# GO — the float contract: one accumulation rule, one owner for each transcendental, and a recorded log

Reconciled: 2026-11-12, U5d closure — folded **A-29** (declared floats now). Part C's proposed reading is the ruled one: Layer 1 step 13 is amended to name the float contract (text owed, drafted by the unification stage, not applied by a suite lane), integer state stays possible later, and the audit's §11 survivor is closed. Parts A and B land as written. Consequence recorded for the save: a save is a state snapshot (`U5d_GO_owed_edits.md` §1).

## Status: PROPOSED

Carries audit finding F-GO-02 and F-GO-12 (`audits/11_GO_audit.md`). Lane: GO, IN (PC and MB route
call sites). One part of it touches ratified Layer 1 text and is therefore also in the audit's §11.

## What it changes in `engine/season/` at runtime

Nothing a seeded run can observe on CPython 3.11, where builtin `sum()` already accumulates left to
right: every hash is EQUAL. On 3.12 and later, float sums on the decision path stop depending on the
interpreter's compensated summation. The transcendental functions keep their values; they gain one
owner and an optional recorder that the engine path never installs.

## The problem, with evidence

1. **The hash folds floats.** `state/world.py:300-301` encodes a float as its IEEE-754 bits. One season at
   seed 0 folds 1,245 of them, all `Person.pursuits`; two seasons at seed 2 add 4 in `Person.stance`.
2. **Those floats and the acts chosen are products of arithmetic no pin covers.** Transcendentals on the
   game path: `decision/choose.py:466` (`log`); `engine/dice_engine/sigma_leverage.py:154` (`tanh`), `:249`
   (`erf`); `modules/combat/weapon_physics.py:502`, `:563` (`**` with a float exponent), `:663` (`exp`),
   `:672`, `:679`, `:696`, `:716`, `:723` (`tanh`); 44 calls under `modules/mass_battle/`. These are not
   correctly rounded by any standard; two math libraries may differ in the last bit.
3. **Builtin `sum()` over floats is interpreter-dependent.** CPython 3.12 made it compensated. The tree
   has paid for this once: CR-01, fixed by `modules/combat/weapon_physics.py:42-53::_ltr_sum`. The season's
   decision path still uses `sum()`: `decision/choose.py:215`; `queries/person_q.py:421`, `:502`, `:619`,
   `:621`, `:696`, `:697`; `data/pursuits.py:145-147`. CI pins 3.11; sessions run 3.13.
4. **A cross-interpreter run did not move the hash** (seed 0, one season, 3.11.18 / 3.12.3 / 3.13.18:
   `5ab73af282d0779646c38839fbab85d8` each time). The hazard is latent: a last-bit difference matters only
   when it changes an order or crosses a threshold. A port has a different library and a different
   accumulation habit on every line.
5. **The plan names a pin that does not exist.** "the chooser's `math.log` over them is slice 3's float
   pin" (`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-20.md:177`); no slice 3 is
   defined in the plan or the build files.
6. **Ratified Layer 1 and the adopted plan disagree.** Step 13 is done when "a headless run prints the
   Python oracle's hash in the integer domain" (`architecture/meta/04_CODE_ARCHITECTURE.md:1130`); the
   build file says "Slice 1 is **not integer-domain**" (`:175`).

## The resolution, decided

Three parts. A and B are decided here (ladder step 4: the tree's own precedents, `_ltr_sum` and GO-16's
recorder). C overwrites ratified text and goes to Jordan with two options.

### A. One accumulation rule (step 4: CR-01's fix, promoted)

New leaf `engine/dice_engine/fmath.py`:

```
def ltr_sum(xs) -> float     # ((0 + x0) + x1) + …; each `+` one IEEE-754 binary64 addition
```

`modules/combat/weapon_physics.py::_ltr_sum` is deleted and its callers import this one (a second copy
would be a second owner). Every `sum(...)` on the game path whose operands can be float calls it: the
ten sites in item 3, and `seam/wrappers/sigma.py:438`. Integer sums (`resolve.py:1170`,
`effects_economy.py:97`, `carriers.py:648`, the weight sums in `world_q.py`) are left alone; the rule is
"a float sum goes through `ltr_sum`", stated once in `fmath.py`'s docstring.

### B. One owner per transcendental, and a recorded log (step 4: GO-16's shape, reused)

`fmath.py` also exposes `log`, `exp`, `tanh`, `erf`, `sin`, `cos`, `atan2`, `hypot`, `powf` (`x ** y` for
a float exponent), each a one-line call to `math`. The 9 season and combat sites and the 44 mass-battle
sites call these instead of `math.*`. `sqrt` stays on `math`: IEEE-754 requires it correctly rounded.

A harness-installed recorder (never installed on the engine path, exactly as GO-16's) appends per call
`(function, operand bits, result bits)`. `tools/export_oracle_draws.py` writes that stream beside the
uniforms for every pinned run. The port's parity job:

- compares its own library's result with the recorded bits **at each call**, and reports a mismatch as a
  named site and operand, which is the thing a bare hash divergence cannot say; and
- in replay mode uses the recorded bits, so that one library difference does not cascade and the hash
  goes on testing the port's logic.

This is what the build file's "slice 3's float pin" was reaching for. **Slice 3 is struck as a name**;
the `fmath` stream is the float pin, and it rides slices 1 and 2 and the module-scene pins.

Edit, `…-v10-09-build-B10-20.md:177` — old: "`betavariate` and the chooser's Gumbel draw reach the port as
recorded values; the chooser's `math.log` over them is slice 3's float pin (CR-01's precedent)." New:
"Every non-`sqrt` transcendental the oracle calls goes through `engine/dice_engine/fmath.py`; the pinned
runs record each call's operand and result bits in `oracle_draws.json`, and the port's replay compares
and substitutes them (CR-01's precedent, generalised)."

GO-08's `primitives` block gains: `ltr_sum` vectors (three orderings of one list that differ under
compensated summation) and, per `fmath` function, the first N recorded calls as vectors.

### C. Step 13's "integer domain" (ratified text; §11 of the audit)

The decision here is the reading to propose, not the ruling. Two defensible options:

- **C1, integer state.** The hash folds no float. `Person.pursuits` and `Person.stance` values become
  fixed-point integers on a declared scale (the precedent is `Fixtures condition_scale = 1000`), the
  encoder refuses a float, and step 13's sentence is true as written. Transient arithmetic stays float
  behind A and B. Cost: design-first; the argue and determine effects that move `pursuits` quantise, so
  every realm hash moves once and some choices change at the margin.
- **C2, declared float state.** Step 13's sentence is amended to "…prints the Python oracle's hash",
  with the float contract (A, B and "hashed floats are produced only by `+ - * /`, `sqrt` and `fmath`")
  named as the condition. Cost: an edit to ratified Layer 1; no behaviour change.

They differ as games in one respect: under C1 a run is reproducible from seed and acts on any machine
the game ships on, which is what makes replay-based saves and shared seeds safe; under C2 it is
reproducible only where the math library agrees, so saves must be state snapshots. This proposal
recommends **C2 now and C1 only if replay-saves or shared seeds are wanted**, because A and B give the
port everything parity needs without moving the game.

## The gate (execution artifacts)

1. `PYTHONHASHSEED=0` realm hash at seeds 0–2, one season, under CPython 3.11 and 3.13: equal to each
   other and, on 3.11, equal to the value before the edit.
2. With the recorder installed, the count of recorded `fmath` calls equals the count from a shim on
   `math`'s nine functions over the same run (the completeness test GO-16 already specifies for draws).
3. `grep -rnE "math\.(log|exp|tanh|erf|sin|cos|atan2|hypot)\(" engine/season engine/dice_engine modules`
   (tests and `fmath.py` excluded) prints nothing.

## The falsifier

A float `sum()` left on the decision path: plant a list whose compensated and left-to-right sums differ
in the last bit at one such site and the 3.11 and 3.13 hashes of gate 1 separate. A `math.tanh` left in
a module: gate 2's counts differ.

## NERS reading (§0.06; E last)

- **N.** Cut it and a port's divergence is a hash that differs, with 58,000 lines to search. It holds
  vertically (oracle to port) and laterally (combat's accumulation rule and the season's become one).
- **R.** Completeness at the extreme: the knife-edge case is exactly where the mechanism fails today.
- **S.** *Calculations consistent in methodology*: two accumulation conventions for one operation is the
  defect §0.06 names, even though each is correct on its own interpreter.
- **E.** One leaf file and a rule a reader can hold in a sentence. It adds an import to about sixty call
  sites and removes a private helper.

## Cost class

A and B: small build (one leaf, about sixty mechanical call-site edits, one exporter stream). C1:
design-first. C2: edit.
