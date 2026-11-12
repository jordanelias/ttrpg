# GO — the float contract: one accumulation rule, one owner for each transcendental, and parity vectors (no recorded log)

Reconciled: 2026-11-12, U5d closure — folded **A-29** (declared floats now). Part C's proposed reading is the ruled one: Layer 1 step 13 is amended to name the float contract (APPLIED 2026-11-12, A-97, node `L1-A29`; `04:1131`), integer state stays possible later, and the audit's §11 survivor is closed. Parts A and B land as written. Consequence recorded for the save: a save is a state snapshot (`U5d_GO_owed_edits.md` §1).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U3_CONFLICT_LEDGER.md` C3-L3 (**no float recorder**: Part B's harness recorder, the `oracle_draws.json` stream of transcendental results and the port's replay of recorded bits are removed; parity is shown by `fmath` vectors at a stated tolerance, the same instrument that replaced the draw log; gate 2 and the build-file edit rewritten; Part A stands; the U5d head's "Parts A and B land as written" is superseded for Part B's recorder), `R1_READ.md` §2 row A-29 (Part C is the ruled reading C2: the "recommended C2 now, C1 later" discussion is removed; the Layer 1 step-13 text is owed, `OWED_TO_UNIFICATION.md` §A, not applied), A-30 (no recorder of any kind); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`). R1's placement question (a non-dice `fmath` leaf under `engine/dice_engine/`) was not decided by U1 and is left as written.

**Depends on:** nothing unlanded for Part A. *(U6 R-A: the edge runs the other way — `11_GO_one_draw_owner.md`'s leaf `draw.py` imports `fmath` for `Draw.normal`/`beta`, so this file's Part A lands first in B06.)*
Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A29`, `unified/work/L1_PROPAGATION.md`): Part C's Layer 1 text is APPLIED at PART E step 13 (`04:1131`, the line moved from `:1130` by PART D row 52); the "owed" wording of the head, the problem (item 6), Part C and the cost class is rewritten to the applied state. The statement that `04:903` and D-29 hold without a further amendment is unchanged and still true (`04:903` reads "Fixed point for `condition`, `stores`, `margin`").

**Lands in batch:** B06 (`B06-keyed-draw`, IN/GO), Part A first, then `11_GO_one_draw_owner.md` with `16_PESSIMIST_GO_keyed_draw_no_recorder.md`, then `U5d_GO_owed_edits.md` (`U3_DEPENDENCY_ORDER.md` §1.2). Gate 2's export round-trip is read in B41 (§1.3).

## Status: PROPOSED

Carries audit finding F-GO-02 and F-GO-12 (`audits/11_GO_audit.md`). Lane: GO, IN (PC and MB route
call sites). One part of it touches ratified Layer 1 text and is therefore also in the audit's §11.

## What it changes in `engine/season/` at runtime

Nothing a seeded run can observe on CPython 3.11, where builtin `sum()` already accumulates left to
right: every hash is EQUAL. On 3.12 and later, float sums on the decision path stop depending on the
interpreter's compensated summation. The transcendental functions keep their values; they gain one
owner, and the port checks its own against them by exported vectors (no recorder, C3-L3).

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
   Python oracle's hash in the integer domain" (`architecture/meta/04_CODE_ARCHITECTURE.md:1130` as read
   when this was written; AMENDED 2026-11-12, A-97, node `L1-A29`, and now at `:1131` because PART D gained row
   52 above it: it reads "prints the Python oracle's hash, under the float contract"); the
   build file says "Slice 1 is **not integer-domain**" (`:175`).

## The resolution, decided

Three parts. A and B are decided here (ladder step 4: the tree's own precedent `_ltr_sum`; and the
port-gate file's replacement of the draw log by vectors, C3-L3). C is ruled by A-29 (C2).

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

### B. One owner per transcendental, and parity vectors (C3-L3)

`fmath.py` also exposes `log`, `exp`, `tanh`, `erf`, `sin`, `cos`, `atan2`, `hypot`, `powf` (`x ** y` for
a float exponent), each a one-line call to `math`. The 9 season and combat sites and the 44 mass-battle
sites call these instead of `math.*`. `sqrt` stays on `math`: IEEE-754 requires it correctly rounded.

*(Reconciled, W3-1, C3-L3: the first text's harness recorder of `(function, operand bits, result bits)`,
its `tools/export_oracle_draws.py` stream and the port's replay of recorded bits are removed; A-30 retires
recorders and one parity instrument serves draws and floats alike.)* **Parity is shown by `fmath` vectors:**
for each `fmath` function, a set of inputs covering the operand ranges its call sites reach, with the
oracle's outputs, exported once and read by the port's test at a stated tolerance (bit-equal for `ltr_sum`
and the IEEE-754-exact operations; a stated ulp bound for the transcendentals). A mismatch names the function
and the input, which a bare hash divergence cannot. **Slice 3 is struck as a name**; the `fmath` vectors are
the float pin, and they ride slices 1 and 2 and the module-scene pins.

Edit, `…-v10-09-build-B10-20.md:177` — old: "`betavariate` and the chooser's Gumbel draw reach the port as
recorded values; the chooser's `math.log` over them is slice 3's float pin (CR-01's precedent)." New:
"Every non-`sqrt` transcendental the oracle calls goes through `engine/dice_engine/fmath.py`; parity is shown
by `fmath` vectors (inputs and expected outputs at the stated tolerance), exported once and read by the port's
test; no stream is recorded (A-30, C3-L3). Draws reach the port by the keyed hash, not as recorded values."

GO-08's `primitives` block gains: `ltr_sum` vectors (three orderings of one list that differ under
compensated summation) and, per `fmath` function, its vector set as above.

### C. Step 13's "integer domain": declared float state (ruled, A-29)

*(Reconciled, W3-1: the two-option discussion is removed; A-29 ruled C2.)* Step 13's sentence is amended to
"…prints the Python oracle's hash", with the float contract (A, B, and "hashed floats are produced only by
`+ - * /`, `sqrt` and `fmath`") named as the condition. The amendment is APPLIED (2026-11-12, A-97, node
`L1-A29`): PART E step 13, `04:1131`, reads as above and names `engine/dice_engine/fmath.py` as unbuilt at the
amendment, its builder being Part A of this file. Integer state stays possible later. A
consequence: a run is reproducible only where the math library agrees, so a save is a state snapshot
(`U5d_GO_owed_edits.md` §1). A margin graded by the ladder is quantised at the seam
(`U5a_DICE_owed_edits.md` §1 row 1, C3-L1), so `04:903` and D-29 hold without a further amendment.

## The gate (execution artifacts)

1. `PYTHONHASHSEED=0` realm hash at seeds 0–2, one season, under CPython 3.11 and 3.13: equal to each
   other and, on 3.11, equal to the value before the edit.
2. *(W3-1, C3-L3:)* a Python re-run of every vector through `fmath` reproduces its expected output bit for bit
   (`engine/tests/test_fmath.py::test_every_vector_reproduces_bit_for_bit`, the vectors held in the test); a planted
   change of one function's body fails it. *(U6 R-A:)* the exported vectors' round-trip (the exporter that carries
   GO-08's `primitives` block, `tools/export_oracle_pins.py --check`) is read in B41, which builds that exporter; no
   exporter exists by B06 (`U3_DEPENDENCY_ORDER.md` §1.3).
3. `grep -rnE "math\.(log|exp|tanh|erf|sin|cos|atan2|hypot)\(" engine/season engine/dice_engine modules`
   (tests and `fmath.py` excluded) prints nothing.

## The falsifier

A float `sum()` left on the decision path: plant a list whose compensated and left-to-right sums differ
in the last bit at one such site and the 3.11 and 3.13 hashes of gate 1 separate. A `math.tanh` left in
a module: gate 3's grep prints it.

## NERS reading (§0.06; E last)

- **N.** Cut it and a port's divergence is a hash that differs, with 58,000 lines to search. It holds
  vertically (oracle to port) and laterally (combat's accumulation rule and the season's become one).
- **R.** Completeness at the extreme: the knife-edge case is exactly where the mechanism fails today.
- **S.** *Calculations consistent in methodology*: two accumulation conventions for one operation is the
  defect §0.06 names, even though each is correct on its own interpreter.
- **E.** One leaf file and a rule a reader can hold in a sentence. It adds an import to about sixty call
  sites and removes a private helper.

## Cost class

A and B: small build (one leaf, about sixty mechanical call-site edits, one vector block in the exporter).
C: edit (Layer 1 text APPLIED, `04:1131`, A-97; nothing left to build).

**Tests and lands (W3-1).** New `engine/tests/test_fmath.py`: `test_ltr_sum_is_left_to_right_on_three_orderings`,
`test_every_vector_reproduces_bit_for_bit`; gate 3's grep as `tests/valoria/test_fmath_one_owner.py::test_no_math_transcendental_outside_fmath`.
Lands: an IN-lane implementation session under `/methodology-execute` with GO, PC and MB review; the call-site
edits `haiku`-assisted, the leaf and vectors `sonnet`.
