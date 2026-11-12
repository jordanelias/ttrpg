# GO — the draw is a function of its key: no generator, no recorder, no replay

Reconciled: 2026-11-12, U5d closure — folded **A-30**: Jordan chose option A (the draw is a function of its key). The "one question to Jordan" is closed; the Layer 1 row is rewritten by the ruling (text owed, not applied). With A-5 the sampler the key feeds is the one bell-curve sampler. No step changes.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (A-30: the Status line no longer says
"returned to Jordan"), §1 (AMBIGUOUS against `04` PART D 35's "no counter": the index `n` is part of the key, so a d10
pool drawing six or more uniforms draws each under its own key `(H(…), n)` and A-30's "one draw per key" holds — stated
once at the owner, `11_GO_one_draw_owner.md`'s `Draw` docstring (U6 R-C) — and the row is rewritten by A-30, text owed in
`OWED_TO_UNIFICATION.md` §A; `04` is not edited), §7/§7b (tests, order, tier); U3 B06, C3-Y10 (co-lands with
`11_GO_one_draw_owner.md`: this file's key function is that file's `Draw.u` body), C3-D3 (the keyed draw, B06, before the
task draw, B07), C3-L3 (no float recorder either: parity by `fmath` vectors); STAGES.md (the v11 workplan rows move to the
v12 plan). Changed: Status, the edits table's workplan row, the gate's test names.

Reconciled: 2026-11-12, U6 repair lane R-C (`unified/U6_VERDICT_AND_REPAIRS.md` finding 5, A-30): "the per-key index `n` inside one key" reworded above to "the index `n` is part of the key", pointing to the one statement at `11_GO_one_draw_owner.md`. The drafted Layer 1 row text in the edits table ("an index `n` within one key") is owed Layer 1 text and R-A's (finding 3); not edited here.

## Status: PROPOSED (A-30 taken: option A; the Layer 1 RNG row text is owed to Jordan's amendment, not applied)

Lands in batch: **B06** (IN/GO; one re-pin of every seeded result, shared with `11_GO_one_draw_owner.md`). Depends on:
`11_GO_one_draw_owner.md` (B06, the `Draw` type and its single constructor; one commit pair, one re-pin). Every later
draw site in the suite (B07 onward) is written against this owner.

Carries F-PES-GO-02 of `audits/16_PESSIMIST_GO.md` (§1.1). Lanes GO, IN (PC, MB and DICE touch their
draw sites). Read at `826b747`. Reference only (`CLAUDE.md` §0.05); not ratified by being written.
**It composes with, and narrows, `11_GO_one_draw_owner.md`:** that proposal's `Draw` type and single
constructor stand; this one changes what is underneath `u()` and deletes what that change makes
unnecessary.

## What it changes in `engine/season/` at runtime

Every uniform the loop or a module draws is computed from the draw's own key by the hash the engine
already owns, instead of by a `random.Random` seeded from that key. **Every seeded content hash and
golden moves once** (a declared re-pin, the same one `11_GO_one_draw_owner.md` already declares for
the nine non-uniform sites; the two land as one). Distributions are unchanged: a uniform on
`[0, 1)` at 53 bits either way. No act, eligibility, odds or write changes.

## The problem, with evidence

`draw_factory` (`engine/season/state/ids.py:87-90`) builds `random.Random(int(H(seed, tick, subject,
purpose), 16))` per call. `H`'s contract is "`purpose` must be unique per DRAW" (`:18`). So each
generator is, by contract, asked once.

Measured (`runs/PES_GO/probe.py census 0 1`; counting shims that override no generator method; the
build excluded; control: hash `5ab73af282d0779646c38839fbab85d8`, equal to the plain run). One computed
season, seed 0:

| | count |
|---|---|
| generators built | 18,702 |
| drew exactly once, `.random()` | 18,651 (99.73%) |
| drew six or more (a d10 pool) | 48 |
| drew nothing | 3 |
| method calls: `random` / `randint` / `randrange` / `getrandbits` | 18,652 / 96 / 96 / 159 |
| `blake2b` calls in the same season | 50,975 |

The plan's answer to "the port will not implement Mersenne Twister" is GO-16: a recorder on the
factory, `tools/export_oracle_draws.py`, `engine/engine_params/oracle_draws.json`, a completeness
test, a digest in GO-08, and a replay harness in the port. The prior GO lane found what that costs:
replay proves the port on the recorded runs only, those runs enter the combat engine for 0, 2 and 4
fights and fight one field (F-GO-01), and the port's own samplers never run in a parity test
(F-GO-03). All of it follows from keeping a generator the oracle uses as a hash.

## The resolution, decided

Ladder step 5, on step 4's precedent: `H` is "an OWNED, VERSIONED mix — never a language built-in"
(`ids.py:17`); the same argument, applied to the draw.

```
# engine/dice_engine/draw.py  (the file 11_GO_one_draw_owner.md adds; this is its body)
class Draw:
    key: str                    # the 16-hex H(seed, tick, subject, purpose)
    n: int = 0                  # draws taken from this key
    def u(self) -> float:
        # the n-th uniform of this key: the first is the key itself, later ones re-mix it with n
        word = int(self.key, 16) if self.n == 0 else int(H2(self.key, self.n), 16)
        self.n += 1
        return (word >> 11) / 9007199254740992.0        # 53 high bits / 2**53
    # random(), below(), die(), pick(), normal(), beta(): as 11_GO_one_draw_owner.md, each a function of u()

def H2(key_hex: str, n: int) -> str     # draw.py (the leaf; ids.py imports it): blake2b(f"v1d|{key_hex}|{n}", digest_size=8)
def seeded(key_hex: str) -> Draw        # the one constructor
```

`draw_factory` returns `seeded(H(world_seed, tick_of(), subject_id, purpose))`. The two generators
built outside it (`seam/wrappers/combat.py:395`, `:397`) and the unseeded fallbacks
`11_GO_one_draw_owner.md` lists go through the same constructor, as that proposal says.

**What is then not built:** GO-16 whole (the recorder, `export_oracle_draws.py`,
`oracle_draws.json`, the completeness shim, the port's replay); in GO-08, "the digest of GO-16's
draw log" and the sentence "NO Mersenne Twister or `random`-method vectors (the port replays
recorded draws)". **What GO-08 gains instead:** a `draws` entry in its `primitives` block: twelve
`(key, n) → u` vectors (the IEEE-754 hex of `u`), including `n = 0`, `n = 1` and a key at or above
2^63, and the `die`/`normal`/`beta` vectors `11_GO_one_draw_owner.md` names. The integer contract
it already carries (64-bit unsigned `H` values against GDScript's signed integers) covers the shift.

**What the port then does:** computes the same `u` from the same key. Its parity job runs any seed
and season count and compares `content_hash`; the pinned slices become three fixed points of a check
that is no longer limited to them.

## Exact edits, by file and owner

| file | owner | edit |
|---|---|---|
| `engine/season/state/ids.py` | IN | `draw_factory` returns `seeded(...)`, importing `seeded` (and, where it needs it, `H2`) from `engine/dice_engine/draw.py`; `H` stays here, the id mint |
| `engine/dice_engine/draw.py` | DICE | `H2` (its one home: U6 R-A, `U3_CONFLICT_LEDGER.md` C3-R3) and `Draw.u` as above (the rest as `11_GO_one_draw_owner.md`) |
| the v12 cards for B10-20, GO-16 and GO-08 (not the v11 lines `workplans/valoria_master_workplan_v11_part3.md` B10-20 and `…_part5.md` GO-16, GO-08, which this session's content supersedes) | GO | GO-16 is not carried into v12 (the order line and the freeze row's "the draw log's digest" with it); GO-08's text as above; exit line 4 drops `export_oracle_draws --check` (a plan edit for the v12 author) |
| `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12 | **Jordan** (A-30 ruled the substance; the text is owed, `OWED_TO_UNIFICATION.md` §A, applied only by his amendment; no lane edits `04`) | the RNG row: "the draw (built) · a function of its key, `H(seed, tick, subject, purpose)`; an index `n` within one key; no generator object, nothing global · see rejection 4"; rejection 4's last two sentences ("not yet load-bearing, because no roll exists yet") replaced by the measured count |
| every seeded golden under `engine/season/tests/`, `engine/tests/` | IN | one re-record, said plainly in the commit (§7) |

## The gate (execution artifacts)

`probe.py census` was lane scratch, not in the repository. Committed, in the one test file of the draw owner,
`engine/tests/test_draw.py` (CI job `sim-regression`, CLAUDE.md §3; `engine/dice_engine/` has no tests directory; U6 R-A,
C3-R3: one file, shared with `11_GO_one_draw_owner.md`'s gate, never a second): `test_u_is_a_function_of_the_key`,
`test_n_zero_is_the_key_itself`, `test_n_one_remixes_with_h2`, `test_no_random_Random_in_runtime_code` (the scan as
`11_GO_one_draw_owner.md` gate 2 defines it, with its three named harness controls). Command:
`python -m pytest engine/tests/test_draw.py -q`. Readings:

1. A census run as above on the new tree: zero `random.Random` instances constructed in a computed
   season (the scan of `11_GO_one_draw_owner.md` gate 2 prints nothing outside its three named harness controls).
2. Same seed, same hash, twice, under `PYTHONHASHSEED` 0, 1, 2 (`m1_acceptance` row 2).
3. A two-sample check that the re-pin is a stream change and not a balance change: over seeds 0–9,
   two seasons, the per-verb act counts and the degree histogram of the new tree against the old lie
   within the seed-to-seed spread of the old (the control is the old tree's own spread). This is the
   instrument a re-record owes (`CLAUDE.md` §7); it is run once, at the re-pin.
4. In B06: `engine/tests/test_draw.py::test_samplers_match_their_vectors` reproduces the `(key, n) → u` vectors held in
   the test. The export round-trip (`tools/export_oracle_pins.py --check` passes with the `draws` vectors and reds when
   one is edited) is read in B41, where GO-08 builds that exporter (U6 R-A: the instrument does not exist by B06;
   `U3_DEPENDENCY_ORDER.md` §1.3).

## The falsifier

A draw site whose stream cannot be expressed as `u()` calls on a key (a sampler that consumes a
variable, state-dependent number of generator words in a way two languages could disagree on).
`11_GO_one_draw_owner.md` already fixes `normal` and `beta` to named algorithms over `u()`; if one
cannot be, this proposal fails for that site and it keeps a recorded vector set instead.

## Where "we do not do deterministic" stands

Untouched, and slightly better served: seeded replay is what the rule permits ("same seed, same
world"), and this makes it true across the oracle and the port, not only inside each.

## NERS reading (§0.06; E last)

- **N.** The cut test is the proposal: remove the generator and name what dies. A re-pin; the
  Mersenne Twister. Nothing a player or a requirement names. From the other directions: bottom-up,
  every draw site keeps its call; top-down, the gate loses a position and gains coverage; lateral,
  PC's and MB's samplers become testable in the port.
- **R.** Completeness at the extremes: parity at any seed, where the plan has it at three.
- **S.** One methodology for "a value derived from the clock and a purpose": ids, mints and draws are
  all `blake2b` over the same tuple. Today two of the three are.
- **E.** Fewer objects (no generator, no recorder, no log, no replay) for more of what N and R ask.

## Cost class

Small build plus one re-pin; deletes a BUILD position (GO-16) and part of another (GO-08). Tier: `opus` for gate 3's
two-sample check design (the judgment that the re-pin is a stream change, not a balance change), `sonnet`, effort
`high`, for the code. Hash movers declared: every seeded content hash and golden, once, shared with
`11_GO_one_draw_owner.md`. Lands it: B06, order `H2` and `Draw.u` → `draw_factory` returns `seeded` → the two outside
generators → the re-pin with gate 3.
