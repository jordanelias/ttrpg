# CHAPTER 3 — One Resolver, Four Scales, One Scalar

*Verified at HEAD `571ae14`. Every locator in this chapter was opened and read by its author; the
count of spot-checks and the list of claims that did **not** survive are in §10. Three findings here
correct reports this run produced, including the orchestrator's own headline; those corrections are
marked and argued, not absorbed.*

---

## The claim

**Valoria's resolution substrate is correct and well-owned at the top, and starved at the bottom.**

`degree_from_net` (`engine/autoload/dice_engine.py:104-157`) is the healthiest thing in this
repository: one owner for every scale, a margin ladder ruled by Jordan on 2026-08-14, a guard test
that fails when a second ladder appears, and a docstring honest enough to flag its own unexecuted
half in capital letters. It is not the problem. It is being handed two operands, and **neither
operand responds to the thing it is supposed to respond to**:

| operand | what it should track | what it actually does | locator |
|---|---|---|---|
| `net` | the target number the caller declared | ignores it — the face rule is a constant pinned to TN 7 | `dice_engine.py:53-61`, `:82` |
| `ob` | the entity you are facing (Jordan, 2026-08-14: *"their corresponding score/2 plus whatever specific modifiers exist"*) | six private derivations in six modules, three of them mutually contradictory, none owned by the resolver, all quantised to integer | §3 below |

`margin = net − ob` is computed correctly from two values that are, respectively, difficulty-blind
and unowned. That is the chapter's first half.

The second half is the same defect one level up. **Every cross-scale crossing that executes carries a
single scalar and no person**, and at three separate seams that scalar is the same field, `Faction.Mil`.
A personal-combat actor is derived from one rounded integer; the result of the fight echoes back as a
dictionary in which the winner is named twice and the loser is not named at all. The failure is not
in the resolver. **It is in the payload the resolver is handed.**

---

## 1. What is actually right, stated first — because it is the standard the rest is judged against

The degree ladder is the strongest evidence in the tree for Chapter 1's "substrate built" half, and it
sets the bar the rest of this chapter measures against.

`degree_from_net` bands `margin = net − ob` at 0 / 1 / 3 (`dice_engine.py:150-157`). It is single-owned
in the strong sense: `tests/valoria/test_degree_ladder_single_owner.py` enrols five implementations
and asserts they **collapse to one behavioural class over the integer and quarter-step domains**, and
it pairs that roster with a source sweep (`test_no_new_hand_rolled_ladder`) precisely because a roster
is a claim about the tree rather than a measurement of it — the file says so, and says so because an
earlier census missed a ninth ladder sitting in the owner's own package. Two divergences are **declared
HOLDs with measured reasons** and are asserted to *still diverge*, so a hold that quietly stops being
necessary fails the test rather than outliving its reason.

That is what a well-owned primitive looks like, and it is worth naming the specific disciplines,
because the rest of the chapter is a catalogue of their absence:

- the owner's docstring flags its own unexecuted half (`:118-123`) rather than asserting it as done;
- it names the retracted pre-ruling bands in `engine/engine_params/params_tables.yaml` and says
  explicitly *"where it disagrees with code, the code wins"* (`:130-137`) — CLAUDE.md §0.05 written
  into the function a reader consults;
- it states the behaviour change it caused, in the commit that caused it (`:145-148`).

**NERS — `dice_engine.degree_from_net`**

```
ENGINE: engine/autoload/dice_engine.degree_from_net    INSTANCE: A (core ladder)
VERDICT: COMPLIANT, with one unregistered divergence outside the owner

N: PASS — no redundant draw; the function contains no draw at all. It is the classifier over a
         draw's output, which is the correct place for a single owner.
R: PASS — monotone in margin, no clamp inversion, fractional-safe on both operands. The Partial
         band is a whole-success-wide WINDOW rather than the point `margin == 0`, which is the
         only reading that survives fractional obstacles (`:124-128`).
S: PASS except one site — the mass-battle strategic adapter classifies a finished battle by
         SURVIVOR RATIO (`massbattle.py:46-48`: 0.75 / 0.25 / 0.50 thresholds), and says of itself
         "These are NOT the canonical degree ladder ... reconciling the two is open MB-lane work."
         An honestly self-disclosed divergence is still a divergence, and it is the only one of the
         three not enrolled in the guard.
E: PASS — "3 or more is always overwhelming" is a rule a player can hold in their head.

REMEDIATION:
  LOW  S → enrol `systems/mass_battle/sim/massbattle.py`'s survivor-ratio map in
           `test_degree_ladder_single_owner.py` as a THIRD declared HOLD with its measured reason,
           or migrate it. Do not leave it as the one divergence the guard cannot see.
```

**This is T-10 and it currently passes.** Everything below is what happens to a good ladder when
nobody owns its inputs.

---

## 2. The first operand: `net` ignores TN

### 2.1 The defect, verified

```python
def _die_result(face: int) -> int:          # dice_engine.py:53 — takes ONLY the face
    if face == 1:   return -1
    elif face <= 6: return 0
    elif face <= 9: return 1
    else:           return 2

def roll_pool(pool_size, tn=7, ob=None, rng=None) -> RollResult:      # :75
    rolls = [rng.randint(1, 10) for _ in range(effective_pool)]       # :81
    net = sum(_die_result(face) for face in rolls)                    # :82  <- tn absent
    return RollResult(pool_size=..., tn=tn, ...)                      # :84  <- tn RECORDED
```

`tn` is accepted, recorded on the result, and never used. And I checked the other end of that write:
**`RollResult.tn` has zero readers anywhere in `engine/`, `systems/` or `tests/`.** The parameter is
written to a field nothing reads, by a function that never saw it. That is CLAUDE.md §0.1 point 1's
named hazard — read/write asymmetry — in its purest available form, and it explains why nothing caught
it: every test that asserts "the result records the TN it was given" passes, and every test written at
the TN-7 default passes.

Twelve lines below, the continuous twin **does** honour TN
(`:98`, `mu, sigma = _CONTINUOUS_PARAMS.get(tn, ...)`), and its docstring asserts the two engines are
*"statistically equivalent to discrete"* (`:91`).

### 2.2 The measurement

The hardcoded face rule's per-die moments, computed: **EV = 0.400, sd = 0.800.** That is *exactly* the
TN-7 row of `_CONTINUOUS_PARAMS` (`:70`). So `roll_pool` is not vaguely ignoring TN — **it is pinned to
TN 7**, and the asserted equivalence between Valoria's two resolvers holds at exactly one point.

Ran at n = 200,000 per cell, seeded:

| pool | continuous @ TN 6 | continuous @ TN 7 | continuous @ TN 8 | `roll_pool` observed, **any** tn |
|---:|---:|---:|---:|---:|
| 4D | 2.000 | 1.600 | 1.200 | **1.6009** |
| 6D | 3.000 | 2.400 | 1.800 | **2.3991** |
| 10D | 5.000 | 4.000 | 3.000 | **3.9950** |

And what that does to the ladder, which is the number that matters. Pool 6D against Ob 2, TN 8,
100,000 trials each path:

| band | discrete `roll_pool(6, tn=8, ob=2)` | continuous `degree_from_net(sample(6, tn=8), 2)` | gap |
|---|---:|---:|---:|
| Failure | 32.9% | 54.1% | **−21.2 pp** |
| Partial | 20.2% | 19.3% | +0.9 pp |
| Success | 32.8% | 22.0% | +10.8 pp |
| Overwhelming | 14.1% | 4.7% | **3.0× overstated** |

Two resolvers documented as equivalent disagree by 21 percentage points on whether the action failed.
Any mechanic that resolves discretely at one scale and continuously at another silently changes its
odds when it crosses — and that is precisely the personal↔faction seam, where `combat_engine_v1` uses
the **continuous** path (`core.py:56`, `SL.roll_net_continuous`) and the faction resolvers use the
**discrete** one.

### 2.3 Three corrections to how this defect has been reported

**(a) The count is 19, not 28.** `L0e_dice_engine_tn_defect.md` says "28 production call sites pass
`tn`". Parsing every `roll_pool(` occurrence under `engine/` and `systems/` gives 33 in production
code — but **14 of them are not calls to `dice_engine` at all.** `systems/mass_battle/sim/` defines its
own `roll_pool` at `resolution.py:36-42`, and `orchestration.py:167` pulls it in by
`from systems.mass_battle.sim.resolution import *`. Verifying imports at each of the remaining sites:
**19 production call sites reach `dice_engine.roll_pool`.** The THROUGHLINE_MAP's figure of 19 is
correct; L0e's 28 conflates two functions with the same name.

**(b) The mass-battle roller is the fix, already written, already executing.** This is the single most
useful thing I found, and it comes out of that same correction:

```python
def roll_pool(n, tn=7):                      # systems/mass_battle/sim/resolution.py:36
    ...
    if f == 1:         net -= 1
    elif tn <= f <= 9: net += 1              # <- consumes tn
    elif f == 10:      net += 2
```

Its moments at tn ∈ {6, 7, 8} are **0.500 / 0.400 / 0.300** with sd **0.8062 / 0.8000 / 0.7810** —
bit-exact against `_CONTINUOUS_PARAMS`, all three rows, mean and sigma. `_CONTINUOUS_PARAMS` is not an
independent calibration; **it is the moment table of the TN-parameterised discrete rule, and it has
been sitting in `dice_engine.py` the whole time as a fossil of the rule the discrete engine was
supposed to have.** The repair is not a design question. It is lifting four lines from a sibling module
that already got it right.

**(c) The goldens will NOT move, and L0e's honest-cost statement is wrong in the safe direction.**
L0e says "Expect goldens to move; that is the honest cost and it must be stated, not absorbed." I
checked, two ways.

*Analytically:* at `tn = 7` the parameterised rule and the current rule return the same value for every
face 1–10 — I enumerated all ten — and consume the same number of RNG draws. Bit-identical.

*By execution:* I applied the parameterised rule in memory (no repo file touched) and ran both seeded
campaign goldens. `engine/tests/test_mc_v18_regression.py` (n=2, seed 0) → **5 passed in 71.54s**.
`engine/tests/test_f7_smoke_oracle.py` (n=8, seed 42) → **6 passed**, matching its unpatched baseline
run exactly. The live win-share pin `GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0,
'Hafenmark': 0.0, 'Varfell': 12.5}` (`test_f7_smoke_oracle.py:267`, regenerated 2026-08-24 for the
mass-battle engine swap) is unmoved, as are `GOLDEN_WINNERS = {'Crown': 5, 'Church': 2, 'Varfell': 1}`,
`GOLDEN_BATTLES_MEAN = 35.1` and `GOLDEN_SCENES_RESOLVED = 975` (`:267-270`).

⚠ **A caution about that citation, because I nearly propagated the wrong number and the run's
orchestrator did.** `{Crown: 37.5, Church: 12.5, Hafenmark: 12.5, Varfell: 37.5}` appears twice in
that file — at `:16` and `:74` — and is a **superseded 2026-07-29 pin preserved in a comment block
labelled "OLD (pre-OI-04, pre-transfer-motion) values, preserved for the before/after record."** It is
not the live constant. The file's own history explains exactly how that trap forms (`:262-266`):

> "BOTH 'PREVIOUS' BLOCKS IN THIS FILE WERE WRONG UNTIL 2026-08-23, IN A WAY NO TEST CAN SEE. Each
> re-record copied the LIVE values into the PREVIOUS line instead of reading the superseded ones ...
> A golden test pins the LIVE constants; nothing pins the prose, so **a fabricated history stays green
> forever and the next re-recorder reasons from it.** ... Rule: a PREVIOUS line is read out of
> `git show <ref>:<file>`, never copied from the constant you are about to overwrite."

That rule should be lifted out of this one file and applied wherever the tree records superseded
values, which is everywhere §0.1 point 4 asks for a published delta. It is the golden-file instance of
the general defect this chapter is about: **an unguarded prose channel adjacent to a guarded code
channel, where the prose is what the next reader reasons from.**

⚠ **And a limit on what my own green run proves.** The same 2026-08-24 regeneration note states, of
these exact pins: *"THIS IS NOT A BALANCE MEASUREMENT: n=2/seed-0 and n=8/seed-42 cannot distinguish a
balance change from noise (`test_f7_smoke_oracle.py:8` demands an n≥100 oracle that still does not
exist). It is a reproducibility pin."* So "the goldens did not move" is a **reproducibility** result,
not a balance result. Here that is exactly the claim I need — the analytic argument carries the
correctness and the run is only its control — but it would **not** suffice for R-4 below, which
changes values on the campaign path. It is also the same argument this chapter makes about TN:
**a pin that cannot vary the thing it measures cannot observe a change in it.** n=8 cannot see
balance; a flat face rule cannot see difficulty.

Why it is safe: **every campaign-path call site resolves `tn` to 7.** I resolved all nine named TN
constants — `BG_VOTE_TN`, `ARGUE_POOL_TN`, `PARL_TRANSFER_TN`, `TRIBUNAL_TN`, `KNOT_FORMATION_TN` and
three `_TN` — and all nine are `7`. The sites that pass a *variable* TN are the three threadwork
modules and one deprecated combat adapter, and **threadwork does not execute on the campaign path**:
`mc_v18.py:192` and `:204-217` stubwire it deliberately rather than fabricate personal-scale actors.

That last fact is the diagnosis, not the reprieve. The declared difficulty tiers that would expose the
defect are `TN_BINDING = 8`, `TN_POP = 8`, `TN_POP_BINDING = 9` (`operations.py:47-50`), routed into
`_resolve_operation(..., TN_BINDING, ...)` at `:303` and `:312` for Locking and Dissolution. Threadwork
declares that binding a thread is harder than weaving one, and **that declaration is void**: Lock,
Dissolve and Weave all resolve on identical odds. The whole difficulty axis of the game has never been
exercised, because the only subsystems that use it are the ones that do not run.

**(d) The "entire Weapon TN Matrix" belongs to a deprecated module.** L0e and L1 cite the Weapon TN
Matrix among the affected sites. It is at `systems/combat/sim/combat.py:55-60`, in a file whose own
header (`:4-11`) reads *"[DEPRECATED 2026-06-23 — superseded by combat_engine_v1 ...] do NOT wire new
game code through this file."* The canonical personal-combat engine does not use it. The finding
survives without that site; citing it inflates the blast radius.

### 2.4 NERS

```
ENGINE: engine/autoload/dice_engine.roll_pool    INSTANCE: A (core resolver)
VERDICT: NON-COMPLIANT — the difficulty lever is accepted, recorded, and discarded

N: FAIL — 19 production sites pass a parameter with no effect, and the field it is stored on has
         ZERO readers tree-wide. A lever that does nothing is the purest N failure available.
R: FAIL (severity HIGH) — the discrete engine cannot express difficulty at all. "Leverage in-band
         across the whole range" is vacuously violated: response to TN is flat, so there is no
         leverage to be in band.
S: FAIL (severity HIGHEST) — two resolvers are canonically asserted equivalent (`:91`) and are
         equivalent at exactly one point. Measured divergence at 6D/Ob 2/TN 8: 21.2 pp on the
         Failure band, Overwhelming overstated 3.0x. `combat_engine_v1` resolves continuous and the
         faction layer resolves discrete, so this is a smoothness break sitting ON the game's most
         load-bearing seam.
E: FAIL — a player shown "TN 8" receives TN-7 odds. The displayed difficulty is not the difficulty.

REMEDIATION (worst-first):
  HIGH  S/R -> `dice_engine._die_result(face, tn)`, with the success threshold at `tn`. LIFT THE
              IMPLEMENTATION from `systems/mass_battle/sim/resolution.py:36-42`, which already does
              exactly this and whose moments reproduce _CONTINUOUS_PARAMS at 6/7/8 EXACTLY. Do not
              re-derive it. Then delete the duplicate and have mass battle import the owner.
  HIGH  N   -> falsifier FIRST (CLAUDE.md 0.1 pt 3): assert
              mean(roll_pool(n, tn)) ~= _CONTINUOUS_PARAMS[tn][0] * n for tn in {6,7,8} over a
              seeded batch. RUN TODAY: FAILS at 6 and 8, PASSES at 7 — the pass at 7 is the control
              proving the test can observe the defect (0.1 pt 2).
  LOW   E   -> the 28-site audit L0e recommends is NOT needed and should not be performed: all nine
              named TN constants resolve to 7, and the fix is bit-identical at 7. The audit surface
              is three threadwork modules whose declared TN 8/9 tiers are currently void.
COST: ~6 lines plus the falsifier. Seeded goldens DO NOT MOVE (proven by execution, S2.3 above).
```

---

## 3. The second operand: `ob` — and the correction that changes the recommendation

### 3.1 What the ruling says, and what the tree says about it

Jordan ruled on 2026-08-14: *"an obstacle rolled against a character or faction is their corresponding
score/2 plus whatever specific modifiers exist for them in that instance."* The resolver's own
docstring reports the state of that ruling at `dice_engine.py:120-123`:

> ⚠ THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the tree still passes a hand-set Ob.

`L0f_ruled_but_unexecuted.md` row **R2** carries the same sentence, and so does the guard test's own
docstring (`test_degree_ladder_single_owner.py:38-42`).

**It is false, and the tree already knows it is false.** `tests/valoria/test_faction_obstacle_conventions.py:10-13`,
added 2026-08-21:

> "the M1 board records that derivation as 'wired NOWHERE'. **Measured 2026-08-21, that is FALSE**: of
> the three sites that roll against a target faction's score, one already implements the ruling
> exactly, one implements it under a condition, and one contradicts it — each citing its own canon."

Verified at HEAD, opening every site myself:

| site | derivation | relation to the ruling |
|---|---|---|
| `crown_initiative.py:189-191` `coronation_renewal_ob` | `floor(church_l / 2) + 1` | **exactly the ruled shape** — score/2 plus a modifier |
| `tribunal.py:118` | `max(1.0, round(accused.L * 0.5))` | score/2 **conditionally** — only under formal grounds; `:120` uses `round(L)` otherwise |
| `parliamentary_transfer.py:325` | `int(world.factions[holder].L) + 2` | **contradicts it** — full score, not half, and its design doc states the number |
| `threadwork/opposing.py:80-85` | `max(1, opponent_tps // 2)` added to a hand-set `DEPTH_OB` | score/2 as the *modifier*, hand-set as the *base* — the ruling inverted |
| `council_solmund.py:31-33` | `floor(CI / 30) + 2` | derived from a world clock, no target — **out of scope** |
| `crown_initiative.py:46-58` `royal_progress_ob` | `max(2, floor((sum_max − sum_current) / 2))` | derived from own state, no target — **out of scope** |

So the honest statement is not *"implemented nowhere."* It is: **the derivation is implemented at
least four times against a target, in four private and mutually inconsistent forms, none of them owned
by the resolver, and all of them quantised to integer.** That is T-05 — *the obstacle has no owner* —
confirmed in its literal sense, and it is a materially different and more actionable finding than the
one three surfaces are currently carrying.

Two things follow that change what should be recommended.

**First, the disposition is SUSPENDED, not unexecuted.** Jordan suspended the reconciliation on
2026-08-21 rather than let a session reconcile three ratified numbers on its own authority, and the
pin test exists to stop drift while the question is held (`test_faction_obstacle_conventions.py:15-22`).
L0f's R2 recommends "perhaps thirty lines of code plus falsifiers." **That recommendation would
overwrite a Jordan hold.** The pin test names exactly the damage: applying score/2 to the tribunal's
*base* either compounds the formal-grounds halving to `L/4` or collapses the two-tier structure that
*is* the mechanic (`:47-54`), and applying it to parliamentary transfer overwrites
`parliamentary_transfer_v30.md:30`, which states the number in its own resolution table (`:70-76`).

**Second, the ruled shape has a working reference implementation.** `coronation_renewal_ob` is
`floor(score/2) + modifier`, executing, today, cited to `part10 §3.4`. When the hold lifts, the work is
not *design* — it is promoting an existing function to the owner and routing four sites through it.

### 3.2 The quantisation, which nobody has flagged and which is free to fix

Every one of those derivations throws away the fractional part. `round(accused.L * 0.5)`;
`floor(church_l / 2) + 1`; `opponent_tps // 2`; `max(1, round(f.L))` at
`scene_dispatch.py:139`. Meanwhile `degree_from_net` states in its own docstring that **both operands
may be fractional** and that only the windowed Partial band "survives contact with fractional
obstacles, where exact equality essentially never occurs" (`:117-128`), and the continuous engine has
always accepted a fractional pool (`:92`).

The ladder was deliberately built to consume fractional obstacles. Every producer rounds. That is a
seam defect of exactly the kind CLAUDE.md §0.1 pt 5 calls a pattern — the code was correct when
written and stopped being correct when the ladder moved underneath it — and it is load-bearing on the
game, so it earns a guard under the amended predicate.

### 3.3 NERS

```
ENGINE: the obstacle-derivation surface (no owner; 4 target-derived sites + ~2 out-of-scope)
VERDICT: NON-COMPLIANT on S. Not a rolling engine in itself — the DERIVATION is arithmetic — so
         N/R/E are scored on the roll it feeds, and S is the real verdict.

N: PASS-with-caveat — no redundant draw is introduced by any derivation. The caveat is
         parliamentary_transfer's `L + 2`, which makes the obstacle scale at TWICE the ruled rate;
         that is a calibration disagreement, not a redundancy.
R: FAIL — quantisation. Four derivations produce integers for a ladder built to consume floats,
         so a 0.5-wide difference in a faction's score is invisible to the resolution it should
         decide. Combined with S2's flat TN, `margin = net - ob` is computed from a
         difficulty-blind numerator and a step-quantised denominator.
S: FAIL — this is the criterion the defect belongs to. Sibling engines disagree about what an
         obstacle IS: half the score, the full score, half-the-score-as-a-modifier-on-a-fixed-base,
         and a fixed constant (ABSOLUTION_OB = 3, KNOT_FORMATION_OB = 2, DECISIVE_OB = 3). Four
         conventions, four canons, one ruling.
E: FAIL — a player cannot learn one rule for "how hard is this." The rule is per-subsystem.

REMEDIATION (worst-first):
  BLOCKED  S -> reconciliation is SUSPENDED by Jordan (2026-08-21). Do not wire it. The correct
              session action is to REPLACE the false sentence at `dice_engine.py:120-123` with
              the measured classification, and strike R2 from L0f as mis-dispositioned.
  MED      R -> the quantisation is NOT suspended and is separable: it is a defect against
              `degree_from_net`'s own stated fractional contract, not against the score/2 ruling.
              Return floats from `coronation_renewal_ob` and `tribunal`'s effective_ob. Cost: this
              WILL move campaign goldens, because both sites are on the campaign path — unlike the
              TN fix. Requires a control run and an argued re-pin, per CLAUDE.md 7.
  WHEN UNBLOCKED -> promote `crown_initiative.coronation_renewal_ob` into `dice_engine` as
              `obstacle_from_score(score, *modifiers)`, and route the four target-derived sites
              through it. The reference implementation already exists; do not author a new one.
```

---

## 4. Why the two halves are one finding

`degree_from_net` is fed `net` and `ob`. `net` cannot express difficulty. `ob` is not derived from the
thing being faced. The function between them is exemplary and it is classifying the margin between two
constants.

This has a consequence for how the tree's own held decisions unblock, and it is worth stating because
it makes the ordering non-obvious. The combat engine's degree-ladder HOLD
(`test_degree_ladder_single_owner.py`, `HELD['systems/combat/combat_engine_v1/core.py']`) is explicitly
gated on the Ob derivation:

> "the ORDER is now settled and is the opposite of the obvious one: derive Ob from the defender FIRST
> (score/2 + that instance's modifiers), THEN the owner's ladder applies directly. ... **Delete this
> entry when the Ob derivation lands, not before.**"

with Jordan quoted directly: *"DECISIVE_OB for combat is stupid as hell and is dead because Ob should
be determined by your opponent more than anything."* And `combat_engine_v1/core.py:45` still reads
`DECISIVE_OB = 3` — a fixed constant, with the opposition carried in `net_sigma` instead
(`core.py:78-80`, `:99-104`). So the obstacle lever in personal combat is inert by construction: the
defender does not set the bar, they shift the roll.

**The obstacle derivation is the keystone.** It is the one change that unblocks two declared ladder
holds, satisfies a Jordan ruling, and makes difficulty relational at every scale at once. And it is
the one change currently suspended. That is worth putting in front of Jordan plainly: *the suspension
is blocking more than the faction lane.*

---

## 5. The same defect one level up: every seam carries one scalar

### 5.1 The measurement (T-06), re-verified

**IN, faction → personal.** `engine/cross_scale/combat_bridge.py:103-111`:

```python
history = max(1, round(f.Mil))
return _combatant_mod.Combatant(label=fid, history=history)
```

One rounded integer becomes an entire personal-combat actor. Every other `Combatant` field is a
constructor default — strength, agility, weapon, armour, tradition. The personal engine's whole
customisation surface is **constant at the seam**.

**OUT, personal → faction.** `engine/cross_scale/scene_dispatch.py:267-268`:

```python
ctx["echo"] = {"actor_faction": winner_fid, "target_faction": winner_fid,
               "most_relevant_stat": "Mil", "degree": echo_degree}
```

Actor and target are the same value. **The loser cannot be named.** The module says why, at `:250-260`:
attribution "is a named precondition of the DISPATCH_COMBAT_BRIDGE ON-flip," and rather than invent an
attacker/defender split it reuses the contest branch's degenerate self-echo shape verbatim. The
refusal is correct — CLAUDE.md §5's no-fabrication rule — and it is a refusal, which is the point.

Round trip: **`Mil` → a duel → `Mil`.**

**One scale up, same field.** `systems/mass_battle/sim/massbattle.py:71-90`,
`power = max(1, int(round(faction.Mil)))`, with `command=4, discipline=5, morale=5, tier=2,
starting_position=(8,12)` all inherited defaults, each carrying its own `[GAP: no canonical spec]`
comment. Three seams, one field, three times. Class (a) — shared state, and the state is nameable.

### 5.2 The one live personal→faction contest is a faction arguing with itself

`scene_dispatch.py:121-139`, `_emergency_council_parties`:

```python
return (max(1, round(f.L)), max(1, round(7.0 - f.Sta)))
```

Both sides derived from the **same faction's** aggregate stats — "the sitting leadership's case to stay
the course" versus "the crisis's own case for change" — and both played by identical default policies.
This is the run's answer to Jordan's third mandate question, and it is better than "no": the executing
tree **does** contain an intra-faction two-sided contest with a real resolver and a real stat
consequence, firing by default. What it does not contain is anybody on either side. Give the two sides
persistent identities and the divergent-interest mechanic exists that afternoon. (The person object is
Chapter 1's; the seam is mine.)

### 5.3 Matrix cells

| cell | mark | locator | what crosses |
|---|---|---|---|
| **P → U** | **BROKEN** | `zoom_in_out.py:119-120` | carriers fire — `pc_incapacitated` (bool, immediate, ED-159), `contested_figure_wounded` → **+0.15 Ob** to the commander's tactic rolls (ED-167) — but **no producer** queues a personal scene from a battle |
| **U → P** | **EMPTY** | `scale_transitions_v30.md:125-141` promises "Mass Battle at Settlement": participate or escape, Endurance Ob 2, failure = 1 wound | no resolver path exists; `scene_dispatch`'s combat branch is faction-shaped, not battle-shaped, and flag-OFF |
| **F → U** | **EXECUTED-lossy** | `massbattle.py:63-90` | `Mil` → `power`, everything else an inherited default |
| **U → F** | **EXECUTED** | `faction_action.py:433-528` | battle outcome → conquest / territory transfer. The healthiest crossing in the matrix, and it needs no person |
| **P → F** | **EXECUTED-degenerate** | `scene_dispatch.py:267-268` | winner twice, loser never; `most_relevant_stat: "Mil"` |

**The matrix's own shape is the argument.** The crossings that execute are exactly the ones that need
no person. Every crossing that needs a person is prose-only, flag-off, or dormant. A scalar is all you
can pass when no object exists at the far end.

And PART 3's constraint on the third cell binds hard here: **U → P must call into the personal engine,
never approximate it.** P5 §S2 is unambiguous — Total War is the only surveyed precedent with two
resolution paths for one event and the only one with a documented, two-decade-unsolved consistency
failure; Dominions and Mount & Blade achieve consistency by never building a second path, and P5 says
"don't build a second resolver at all" should be **the first option on the table, not a corner case.**
Valoria currently has one resolver per event. T-12 is the one throughline in the register that
*passes*, narrowly, and building U → P as an approximation would commit the failure deliberately.

### 5.4 NERS for the seam bridges

```
ENGINE: engine/cross_scale/combat_bridge.derive_parties   INSTANCE: B (adapter, flag-OFF)
VERDICT: NON-COMPLIANT on R — rank-1 channel

N: PASS — introduces no draw of its own; it constructs operands for an existing engine. It also
         RETURNS None on a derivation gap rather than fabricating (`:113-128`), which is the
         correct behaviour and should be preserved through any repair.
R: FAIL — one rounded int carries the entire aggregate world state into a resolver whose measured
         customisation levers span ~90pp of outcome. Leverage is not in-band; there is one band.
S: FAIL — asymmetric with its own return path (one int in, one int out) and unreachable: the flag
         is default-OFF (`mc_v18.py:78-88`) AND no `queue_scene("combat", ...)` call site exists,
         so it is dead twice over. P5 S1.3 names this exact state as the one option NO surveyed
         precedent defends: "never let the bridge's default state be 'off equals doesn't exist.'"
E: n/a — no player surface.

REMEDIATION:
  HIGH R -> the payload is the fix, not the resolver. Blocked on Chapter 1's person loader; until
           an object exists at the far end there is nothing richer to pass, and widening the
           tuple without it is shape-divergence for its own sake.
  MED  S -> resolve the flag to one of P5's two defensible states (single pass, or explicit
           crossing with a tested equivalence protocol). Do not ship a third.
```

⚠ **The loader is NOT golden-safe, and every recommendation in this chapter that depends on it
inherits that cost.** This run circulated a claim that loading persons at world-gen is "golden-safe by
construction," on the precedent of `populate_from_geography`. **Chapter 1's author refuted it by
controlled experiment**, and the refutation is load-bearing on my §8: the two guards
(`test_pipeline_reach.py:625-628`, `test_f7_smoke_oracle.py:335`) pin `generate_npc`'s **call
counter**, not `world.npcs`, so loading two NPCs directly left both guards green at
`npcs_generated = 0` **and moved seed-42's winner from Crown to Hafenmark**; the control arm with
`simulate_npc_actions` neutered reproduced baseline byte-exact, identifying the channel as
`npe.simulate_npc_actions` drawing `world.rng` at `systems/overview/sim/accounting.py:139`. Cite
Chapter 1 for the finding; I do not re-derive it.

Two consequences here. **First**, R-1's golden-neutrality does not generalise — it holds because the
TN fix is bit-identical at tn=7 and touches no RNG draw count, and that argument is *specific*, not a
template. **Second**, this is a live instance of the class §3.2 and §5.5 both describe: **a stochastic
term running unobserved over an empty container for months, behind a guard that appeared to cover it
and measured the wrong variable.** It is §0.1 point 1's read/write asymmetry with the polarity
reversed — the guard watched the write and the damage came through a read — and it is the same shape
as `RollResult.tn`, a field faithfully written and never read. A guard that observes the call rather
than the effect is §0.1 point 2's exact pattern, and this repository has now produced two of them in
the same substrate.

```
ENGINE: scene_dispatch's combat echo (`:261-268`)     INSTANCE: B
VERDICT: NON-COMPLIANT on S/E — the self-loop

N: PASS. R: FAIL — the degree is one of two labels ("Success" / "Partial") derived from a -1/0/1,
         so a graded personal outcome is quantised to a coin with a shoulder before it crosses.
S: FAIL — `actor_faction == target_faction`. The channel structurally cannot debit a loser, so
         personal→faction consequence is one-signed by construction. This is T-07's shape (the
         counter-force that never fires) arriving at a seam rather than a ladder.
E: FAIL — nothing legible: no player can read "who lost what" out of this echo, because it is
         not in it.

REMEDIATION:
  BLOCKED -> attribution is a named ON-flip precondition and the module is right to refuse to
           invent it. Chapter 1's loader unblocks it. Cite, do not duplicate.
```

```
ENGINE: `_emergency_council_parties` (`scene_dispatch.py:121-139`)   INSTANCE: A (default ON)
VERDICT: PARTIALLY COMPLIANT — correct machinery, degenerate operands

N: PASS — a real contest with a real resolver, fired by a real trigger.
R: FAIL — both operands quantised (`round(f.L)`, `round(7.0 - f.Sta)`) into a kernel whose pool
         floors at 5 regardless (ED-SC-0004), so faculty differences below the floor are invisible.
S: FAIL — the contest's output echoes onto the same faction it was derived from.
E: PARTIAL — the *shape* (leadership vs. the case for change) is legible and good.

REMEDIATION:
  LOW -> do NOT redesign this. It is the correct mechanism with the wrong operands, and the
        repair is the person loader (Ch1), not a new contest.
```

### 5.5 P5's honest verdict, which I am not going to paper over

P5 §S5: **no surveyed precedent has a tested, general solution** for keeping a personal actor's
contribution leverage-in-band from N = 1 to N = 1000+. Every mechanism found either does not scale the
effect with mass size (Dominions' commander anchor, Total War's lord aura — dominant at small N,
invisible at large) or makes the personal entity literally part of the mass sim with no distinct
channel (Mount & Blade — consistent, and personally irrelevant at scale). Shipping teams with large
budgets tried.

Valoria's officer/commander object sits exactly on that problem. So the honest report is: **this is
an open design problem, not an adaptation.** P5's own suggestion — scale the morale delta to a
*fraction* of the unit's own size/cohesion rather than a flat amount — is a hypothesis with no shipped
validation behind it, and it should be labelled as such rather than borrowed as a fix. The instrument
P5 *can* supply (§S2's equivalence protocol) verifies that two resolution paths agree; **it does not
verify that a personal contribution's relative weight stays sane across three orders of magnitude.**
That metric would have to be designed. Chapter 5 owns the general treatment of precedent failure;
what belongs here is the narrow claim: **do not present the seam repair as precedented, because it is
not.**

---

## 6. Precedent that does bind, and how

Two things from P3 attach to specific modules here.

**P3 S1.1 — Ironsworn's one-resolver-many-operands.** The same two challenge dice against a different
left-hand operand: a stat, or a progress track. It is the closest working analogue to Valoria's
four-scales-one-resolver ambition and the one place in the dossier where the reuse is *quantitatively*
clean. Valoria already has the shape — `degree_from_net` over `margin = net − ob` at every scale. What
Ironsworn has that Valoria lacks is that **its left-hand operand is always derived from the thing being
faced.** That is §3's ruling, restated as a precedent. The recommendation it licenses is narrow and
real: when the obstacle hold lifts, do not build per-scale obstacle rules — build
`obstacle_from_score(score, *modifiers)` and vary the *operand*, not the *formula*.

**P3 §S3 — a consequence menu driven by a continuous margin, with no hand-authored special cases.**
This is the single most constructive precedent for a GM-less design in the dossier, and Valoria is
better positioned than any system P3 surveys, because every precedent that gets consequence-selection
right (Ironsworn's 0/1/2 challenge-dice count, PbtA's 6−/7-9/10+) is really *a margin discretised into
bands* — and Valoria's margin is already continuous. Three rules, and the third is the one that
matters:

1. **Menu class by band, magnitude continuous within band.** A fixed "−2" regardless of how badly you
   missed is the naive-port mistake.
2. **Class selected structurally, not by taste**: if an open clock/track exists that this failure
   could feed, route the consequence there (Twist-class); if not, debuff the acting entity
   (Condition-class). That is a lookup on the sim graph, not a judgment.
3. Both require a margin that *moves*. **Which brings it back to §2**: a consequence menu keyed to a
   margin computed from a difficulty-blind numerator will produce the same consequence distribution at
   TN 6, 7 and 8. **The TN fix is a precondition for the consequence layer**, not an unrelated tidy-up.

**P3 §S2's three-way GM-less split**, applied to this chapter's surfaces:

- **(i) Works unchanged.** `degree_from_net` — a closed-form band read on a margin, needing no
  adjudication. Valoria's ladder is already in this category, which is the good news.
- **(ii) Needs a specified mechanical substitute.** Obstacle selection. In a GM'd game a human sets
  the Ob; Jordan's score/2 ruling *is* the mechanical substitute, and it is exactly P3's prescription
  for Mythic's Likelihood assignment: *"the Likelihood should be derived, not chosen — from a relevant
  faction/NPC disposition stat already tracked elsewhere in the sim, never from an ad hoc read."*
  Four hand-set constants (`ABSOLUTION_OB = 3`, `KNOT_FORMATION_OB = 2`, `GREAT_WORK_FINAL_OB = 4`,
  `DECISIVE_OB = 3`) are the ad hoc reads, frozen into code.
- **(iii) Genuinely requires a human, do not copy.** Duel of Wits' scripted-maneuver interpretation —
  and P3 notes Valoria sidesteps this **for free**, because a videogame UI makes maneuver choice a
  button rather than a natural-language classification problem. Worth recording as a place the
  GM-less constraint costs nothing.

---

## 7. Omega — closed

`skills/valoria-resolution-diagnostic/SKILL.md:250` and `:369` carry an `[UNVERIFIED]` flag on an
"omega" Class-A-new-system vetting framework whose spec was "not read this session," with the correct
caution *"do not assume it supersedes NERS."* I verified the resolution in the live tree.

**Ω is the tier-1 Intent gate of `references/throughlines_meta.md`** (`:45-55`), adopted via PP-672
(framework) and PP-674 (Necessity tier plus `valoria_hooks.vetting_gate` enforcement, `:16`). Four
clauses, verbatim from `:47`: (a) strategic-layer actions produce **cross-scale consequences the player
can trace but cannot fully anticipate**; (b) personal-layer moments **permanently transform** the
character; (c) autonomous agents continue generating consequential events **regardless of player
action**; (d) **no strategy produces dominance** — every action pays what it buys. A Class-A proposal
runs the full chain **N → Ω → Μ → М → Τ → Q** (`:185`) and must carry a `vetting:` block in the patch
register (`:200-220`). Authority is split: *"Jordan owns N, Ω, Μ ... Claude flags N/Ω concerns to
Jordan; never unilaterally rejects"* (`:14`).

**Verdict: Ω complements NERS; it does not supersede it.** The lineage document calls the throughlines
framework "a tiered supersession of NERS" *for qualitative vetting* — Q-robust/smooth/elegant subsume
the qualitative readings of R/S/E — but the mechanical rolling-engine N/R/S/E verdict remains the live
instrument for engines. The SKILL.md caution was correct and can now be replaced with the definition.

**And Ω is not decorative here — it scores this chapter's findings directly**, via its own failure
lexicon at `:155-175`:

| finding | Ω clause | lexicon term |
|---|---|---|
| P→F echoes onto the faction it came from; U→P empty | **Ω-a fail** — no traceable cross-scale consequence | *Personal-only* (`:172`) |
| `combat_bridge` passes `round(Mil)`; nothing persists from a fight | **Ω-b fail** — no permanent personal transformation | *Strategic-only* (`:171`) |
| TN accepted and discarded; four hand-set Ob constants | **Ω-d strain** — "every action pays what it buys" is unverifiable when the price lever is inert | *Cost-hidden* (`:167`) |

That is a useful result on its own: **the seam failures are Ω-a/Ω-b failures by the framework's own
anti-pattern table**, which means they are tier-1 — and per `:194`, an Ω failure is flagged to Jordan
and does not proceed. The two clauses Valoria's canon names as constitutive are exactly the two its
executing seams do not deliver.

---

## 8. Recommendations, worst-first, with honest cost

**R-1 — `engine/autoload/dice_engine._die_result` / `roll_pool`: make the discrete engine consume TN.**
Take the implementation from `systems/mass_battle/sim/resolution.py:36-42`. Land the falsifier first
(§9). **Cost: ~6 lines. Both seeded campaign goldens do not move** — proven analytically
(bit-identical at tn=7, all ten faces enumerated) and by execution against both pins, patched in
memory (`test_mc_v18_regression.py` 5 passed; `test_f7_smoke_oracle.py` 6 passed, matching its
unpatched baseline). The only behaviour that changes is threadwork's TN 8/9 tiers, which currently do
not run. **This is the highest value-to-risk change in the chapter and it should not wait for
anything.** Note precisely what the green run licenses, per §2.3's caution: it is a reproducibility
control on an analytic argument, not a balance measurement — n=8 cannot supply one, by that file's
own statement.

**R-2 — same commit or the next: delete the duplicate roller.** Once `dice_engine.roll_pool` honours
TN, `systems/mass_battle/sim/resolution.py:36` is a second implementation of the owner's primitive
with the same name — a live T-12 hazard and a grep trap. Have mass battle import the owner. **Cost:
this is the risky half.** Mass battle's roller is reached through `import *` at
`orchestration.py:167`, `VOLLEY_TN = 6` genuinely varies (`config.py:181`), and mass battle
deliberately maintains a no-`engine.*`-imports property that
`test_degree_ladder_single_owner.py:104-110` relies on. **Do R-1 alone first**; R-2 is a separate,
separately-argued commit, and it may correctly be refused.

**R-3 — `engine/autoload/dice_engine.py:120-123`: replace the false sentence.** "IMPLEMENTED NOWHERE —
every call site still passes a hand-set Ob" is refuted by four sites and by
`tests/valoria/test_faction_obstacle_conventions.py:10-13` in the same repository. Under §0.05 the
guard test is mechanism and the docstring is reference; reference that contradicts mechanism at the
function a reader consults to learn what an obstacle *is* is the exact failure that docstring's own
neighbouring paragraph apologises for. Replace it with the four-row classification and a pointer to
the pin test. **Cost: zero.** Also strike R2 from `L0f_ruled_but_unexecuted.md` — the disposition is
SUSPENDED, not unexecuted, and L0f's "thirty lines of code" recommendation would overwrite a Jordan
hold.

**R-4 — un-quantise the obstacle producers.** `crown_initiative.coronation_renewal_ob` and
`tribunal`'s `effective_ob` return integers to a ladder that documents itself as fractional-safe.
Returning floats is separable from the suspended score/2 reconciliation, because it is a defect
against `degree_from_net`'s own stated contract rather than against the ruling. **Cost: this one DOES
move campaign goldens** — both sites are on the campaign path, unlike the TN fix. It needs a control
run and an argued re-pin, and CLAUDE.md §7 flags the re-pin path as uncontrolled, so say so out loud
rather than performing it quietly. **And the re-pin cannot honestly be called neutral**: n=2 and n=8
cannot distinguish a balance change from noise (`test_f7_smoke_oracle.py:8` and the 2026-08-24
regeneration note), so a moved golden here has to be argued from the *mechanism* — "obstacles stopped
being step functions" — rather than from the new numbers, which carry no balance information either
way. When re-recording, read the PREVIOUS line out of `git show <ref>:<file>` (`:262-266`). Not free;
still cheap; genuinely reversible.

**R-5 — enrol the survivor-ratio map in the ladder guard.** `systems/mass_battle/sim/massbattle.py:46-48`
is the only degree divergence the guard cannot see. Add it as a third declared HOLD with its own
measured reason. **Cost: ~15 lines of test.** Earns its existence under §0.1 pt 5's amended predicate:
the artifact is load-bearing on the game.

**R-6 — when the obstacle hold lifts: promote, do not author.** `obstacle_from_score(score, *modifiers)`
in `dice_engine`, implemented as `crown_initiative.coronation_renewal_ob` already is, with the four
target-derived sites routed through it and `test_faction_obstacle_conventions.py` rewritten as the
record of the new convention — which is what that file says it is for (`:20-22`). **Cost: a Jordan
decision, then perhaps forty lines.** This is the keystone: it satisfies the ruling, unblocks both
declared ladder holds, kills `DECISIVE_OB`, and makes difficulty relational at every scale at once.

**R-7 — the U → P seam, when Chapter 1's loader lands: `mass_battle` calls into `combat_engine_v1`.**
Never a second approximation (P5 §S2.1). Gate it with the equivalence protocol: same engine, two entry
points; a **two-sample distribution test** (K-S on casualty-percentage, binomial CI on win rate) at
n ≥ 100 seeds per state across declared extremes — 1v1, 1000v1000, 100:1, zero-morale, max-fatigue —
checked into CI beside `test_mc_v18_regression.py`. **Cost: real, and there are two honest caveats,
not one.** *First* (§5.5): the protocol verifies *resolution* consistency and does **not** verify that
the personal contribution's relative weight stays sane from N=1 to N=1000. No precedent supplies that
metric; if Valoria wants it, it must be designed, and that is a genuine original contribution rather
than an adaptation. *Second*: this recommendation is gated on Chapter 1's loader, which is **not**
golden-safe — see §5.4 — so the seam work carries the loader's re-pin cost on top of its own, and the
two should not be bundled into one commit where a moved golden could be attributed to either.

**A note on n≥100, which R-7 needs and the tree does not have.** The K-S protocol P5 specifies is the
same instrument `test_f7_smoke_oracle.py:8` has been demanding since it was written — *"no balance
claim without an oracle + n ≥ 100"* — and which still does not exist. That is not a coincidence of
vocabulary: **it is one missing instrument with two customers.** The autoresolve-equivalence test and
the balance oracle are the same machinery (run N seeds, compare distributions, gate in CI) pointed at
different pairs of arms. Building it once serves R-7, retires the standing caveat on every golden
re-pin in this chapter, and is the only thing that would let anyone say whether the TN fix changed
the game rather than merely reproducing it. Chapter 4 arrives at the same instrument from the
expressive-range side; that convergence is worth Jordan's attention, because a tool three chapters
independently ask for is cheaper than three tools.

---

## 9. This chapter's falsifier, stated and run

> **If `tn` is consumed anywhere on the discrete path, or if any call site passes an
> opponent-derived Ob to `dice_engine`, this chapter's two headline defects are wrong.**

Run at HEAD `571ae14`:

| check | outcome |
|---|---|
| `_die_result` signature takes `tn`? | **No** — `dice_engine.py:53`, one parameter, `face`. Two call sites, both `:82`. |
| Any reader of `RollResult.tn`? | **No** — zero across `engine/`, `systems/`, `tests/`. |
| Does `mean(roll_pool(n, tn))` track `_CONTINUOUS_PARAMS[tn][0]*n`? | **FAILS at TN 6 and TN 8, PASSES at TN 7**, n = 200,000 seeded. The pass at 7 is the control (§0.1 pt 2). |
| Any opponent-derived Ob reaching `dice_engine`? | **YES — four sites**, and this half of the falsifier **fires**. `crown_initiative.py:189-191`, `tribunal.py:118`, `parliamentary_transfer.py:325`, `opposing.py:80-85`. |

**So half my falsifier fired, and the chapter is written around that rather than past it.** The
"obstacle is implemented nowhere" claim — carried by the resolver's docstring, by L0f R2, and by the
ladder guard's own docstring — is false, and §3 replaces it with the measured classification. What
survives, and is stronger: **the obstacle has no owner**, four conventions contradict each other, all
of them quantise, and the reconciliation is suspended rather than pending.

The TN half did not fire and is unqualified.

**Golden-neutrality artifacts for R-1**, since a claim about cost needs one, and a claim of *no*
change needs a baseline to be a claim at all (§0.1 pt 4 — a number without a control is not a
measurement). The parameterised face rule was applied in memory; **no repo file was written**.

| arm | test | result |
|---|---|---|
| baseline, unpatched | `engine/tests` (whole suite) | **2055 passed, 5 xfailed** in 562.85s |
| baseline, unpatched | `test_f7_smoke_oracle.py` (n=8, seed 42) | **6 passed** in 177.81s |
| **patched** | `test_mc_v18_regression.py` (n=2, seed 0) | **5 passed** in 71.54s |
| **patched** | `test_f7_smoke_oracle.py` (n=8, seed 42) | **6 passed** in 179.59s |

Both goldens hold under the patch, against a run baseline rather than against an assumption. And the
honest reading of that, stated once more because it is the discipline this chapter argues for: it
establishes **reproducibility**, not balance — `test_f7_smoke_oracle.py:8` says an n≥100 oracle is
what a balance claim would require, and it still does not exist.

---

## 10. Spot-checks, and what I did not cover

**Locators opened and read by me at HEAD `571ae14`: 27.** `dice_engine.py` (`:53-61`, `:68-72`,
`:75-84`, `:87-101`, `:104-157`) · `mass_battle/sim/resolution.py:36-42` ·
`threadwork/sim/operations.py:47-50, :145-157, :303, :312` · `threadwork/sim/opposing.py:80-85,
:127-140, :150-151` · `factions/sim/tribunal.py:108-140` · `factions/sim/crown_initiative.py:46-58,
:80-83, :189-191` · `factions/sim/parliamentary_transfer.py:325-327` ·
`factions/sim/council_solmund.py:30-33` · `factions/sim/absolution.py:33` · `fieldwork/sim/knots.py:59` ·
`cross_scale/combat_bridge.py:103-128` · `cross_scale/scene_dispatch.py:121-139, :250-268` ·
`cross_scale/zoom_in_out.py:110-130` · `mass_battle/sim/massbattle.py:37-90` ·
`combat/combat_engine_v1/core.py:45, :56, :60-104` · `combat/sim/combat.py:1-60, :195-225` ·
`social_contest/sim/contest/resolver.py:155, :286-289` · `mc_v18.py:192, :204-217` ·
`tests/valoria/test_degree_ladder_single_owner.py` (full) · `tests/valoria/test_faction_obstacle_conventions.py`
(full) · `references/throughlines_meta.md:14, :45-55, :155-175, :185, :194` ·
`skills/valoria-resolution-diagnostic/SKILL.md:250, :369`.

**Locators and claims that did NOT check out:**

1. **`engine/autoload/dice_engine.py:120-123`** — "THAT DERIVATION IS IMPLEMENTED NOWHERE — every call
   site in the tree still passes a hand-set Ob." **FALSE at HEAD.** Four target-derived sites, one of
   them (`coronation_renewal_ob`) exactly the ruled `floor(score/2) + modifier`. Refuted by a test in
   the same repo (`test_faction_obstacle_conventions.py:10-13`, "Measured 2026-08-21, that is FALSE").
   The same false sentence appears in `test_degree_ladder_single_owner.py:38-42` and in `L0f` R2.
2. **`L0f_ruled_but_unexecuted.md` R2 disposition** — filed as "ruled but unexecuted." The correct
   disposition is **SUSPENDED by Jordan, 2026-08-21**, with a pin test guarding against drift. Its
   recommendation ("thirty lines of code plus falsifiers") would overwrite a hold.
3. **`L0e_dice_engine_tn_defect.md`'s "28 production call sites"** — measured **19** reach
   `dice_engine.roll_pool`. 14 of the 33 production `roll_pool(` occurrences call
   `mass_battle/sim/resolution.py:36`, a *different* function with the same name that **does** consume
   `tn`. The THROUGHLINE_MAP's 19 is correct.
4. **L0e's "Expect goldens to move; that is the honest cost"** — wrong in the safe direction.
   Bit-identical at tn=7 and every campaign-path TN constant resolves to 7. Verified by execution.
5. **"including the entire Weapon TN Matrix"** (L0e/L1) — the matrix is at
   `systems/combat/sim/combat.py:55-60`, in a module marked DEPRECATED at `:4-11` and superseded by
   `combat_engine_v1`. The canonical engine does not use it.
6. **"27–30 probability gates"** (commission) — I measure **25** `.random() <` sites, all under
   `systems/`, none under `engine/`. The substantive point stands unchanged: **no resolution doctrine
   has ever mentioned them and NERS has never been run on them.** I did not run it either — see below.
7. **`combat_engine_v1/core.py:103`, `roll_net(pool, rng)`** — flagged by me as a possible positional
   mis-bind against `SL.roll_net(pool, tn, rng)`, which would have silenced the seed. **It checks out**:
   `core.py:56` defines a local two-argument shim that forwards `TN` explicitly. Recorded because a
   negative result on a plausible bug is worth as much as a positive one.

**What I did not cover.** The 25 probability gates get a named N-question and no verdict — a proper
NERS pass on them needs a doctrine to test against and none exists, which is itself the finding rather
than something I could close. Lanchester's trajectory-fit exponent (measured p ≈ 1.55–1.7 against a
≤1.4 target, honestly disclosed) I take from L3 and did not re-measure. The contest kernel's
input-starvation — `rebut` dead on all eight proceedings, CLASH/REINFORCE display-only, `faculty`
entering both the pool and the leverage term (`resolver.py:286-287`), `base_ob = 2.0` never overridden
(`:155`) — I verified the locators but did not measure the double-dip's magnitude; it deserves its own
pass. `roll_net_continuous` vs `roll_net` at fractional pools (they agree on mean and differ in shape;
the shipped falsifier tests only the mean) I confirmed as a live gap and did not quantify. Both
campaign goldens ran under the patch and both hold (§9), so R-1's cost claim has no outstanding
execution gap — but **I did not run the wider `tests/valoria` suite under the patch**, only `engine/`,
so a non-campaign assertion elsewhere in the tree that varies TN would not have been caught by me.
Given all nine named TN constants resolve to 7 that is unlikely, and it is still unverified rather
than excluded. Per this chapter's own standard, that is a stated gap, not a silent one.

**One correction to this run that I inherited rather than found**, recorded because §10 is where a
reader checks what to trust: the orchestrator's brief gave me a **stale** win-share golden — the
2026-07-29 pin preserved in a comment — as the live one. I cite the live constant at
`test_f7_smoke_oracle.py:267` and explain the trap at §2.3. The relevant methodological point is not
that a number was wrong; it is that **the wrong number came out of the one channel in that file which
nothing guards**, which is the same shape as every finding in this chapter.

Chapter 1 owns the person loader; Chapter 2 owns the officer ladder and the `Standing` homonym
correction; Chapter 4 owns VSG; Chapter 5 owns the precedent-failure catalogue. Where their material
touches mine — and it does, at every EMPTY cell in §5.3 — I have cited rather than re-derived.


---

## Adversarial pass

This chapter was attacked by a structurally read-only `valoria-critic` (Read/Grep/Glob only), which
opened 64 locators across this chapter and Chapter 4 — **55 exact (86%)**, this chapter scoring ~82%.
**Seven corrections apply to this chapter, two of which change a conclusion**, including a downgrade
of the `roll_pool` **S** severity from HIGHEST to HIGH-latent. They are recorded in
`09_adversarial_pass.md`, together with what survived the attack.
