# Chapter 5 — What We Should Not Do

*Every other chapter in this analysis proposes. This one constrains. Its claim is that each
mechanism Chapters 1–4 recommend has a shipped precedent that failed while holding it, that those
failures cluster into five reusable shapes, and that Valoria is already standing inside four of
them — so the deliverable is a set of named guards bound to named modules, not a warning.*

**Verification note.** I spot-checked 20 Valoria locators myself at HEAD `571ae14` by opening the
files rather than copying a lane's citation; they are listed in §10, including the two that did not
check out — **both claims in this run's own governing brief**, written up in §9 rather than quietly
corrected. Precedent claims are carried at the dossiers' own confidence, with `[UNVERIFIED]` and
community-derived marks preserved rather than laundered. Nothing here is run-verified by me: I
executed no test suite, so every "EXECUTED"/"INERT" verdict is a code read (D-14 applies to me as
much as to anyone). The one experimental result I rely on is Chapter 1's, credited as such.

---

## 1. The frame: legibility and depth are different axes, and every title in the corpus bought one at the other's cost

P1's genre-wide verdict is this chapter's frame and should be quoted rather than paraphrased:
*"no shipped game in this domain has found a formula-legible system that critics also called deep,
nor a deep system that critics also called clear"* — every one of seven titles drew one of those two
complaints from its own playerbase (P1 §C). CK3 pays for shown percentages with additively confusing
modifier stacks; Victoria 3 pays for a stated Legitimacy formula with "deep as a puddle"; EU4's
estates have real depth of intent and are tuned below the threshold of mattering; Imperator had real
interaction depth and a down-direction that read as a bug.

Valoria's ambition — legible odds on a strategic layer with stochastic resolution — is therefore
**not a solved pattern imported from a mature genre; it is that genre's own open problem.** The
consequence binds every chapter here: treat each mechanism Chapters 1–4 recommend as a partial
answer *with its failure mode attached*, never as a proven solution borrowed wholesale.

**The five shapes, and where Valoria stands in each.** (**A**) *The direction that cannot run* —
untunable down-pressure, or a threshold never reached; rows 1–2, and T-07. **Valoria is inside it.**
(**B**) *The extreme the model never meets* — apparatus decorative once the sides part, a band that
vanishes with competence, leverage that dominates at small N and evaporates at large; rows 5, 6, 9.
**Inside it.** (**C**) *Two answers to one question* — a second resolver for one event; row 8.
**Half inside**: one event class already carries a second, self-disclosed degree semantics. (**D**)
*The substrate mistaken for the game* — tracking without expression, variety measured on unperceived
axes, apophenia counted as a mechanism; rows 4, 7, 10. **Inside it.** (**E**) *The bypassed causal
chain* — an outcome acquired without the history that justifies it; row 3. **Not yet inside it, and
the guard is cheap while the ledger still has no writer.**

---

## 2. The guard table

Ten documented precedent failures, each converted into a guard on a named Valoria module, plus one
domestic failure this run discovered in itself. A failure that does not become a guard is an
anecdote; a guard that cannot name its module is a wish.

| # | Precedent failure | Valoria module | The guard |
|---|---|---|---|
| 1 | **Imperator: Rome's launch Loyalty** — governors lost 20+ points on appointment alone and bled regardless of play; Paradox scrapped the whole action-currency four months later (P1 §7.3, [Steam](https://steamcommunity.com/app/859580/discussions/0/4698886342112948827/), [Medium](https://medium.com/@matthewjamesgannon1996/did-paradox-interactives-imperator-rome-fail-268b15e1da33)). *Lesson: test the down-direction against the **best-case** counter-investment, not the average* | Ch2's demotion path — G606 cumulative suspicion, `systems/factions/faction_politics_v30.md:129` §1.0d, and `Settlement.suspicion` (`systems/settlements/sim/registry.py:78`) | Before any suspicion or demotion writer lands: run the **maximum** available per-season mitigation against the maximum accrual and assert the net is recoverable. If the fastest possible remediation still nets negative, the mechanic is broken, not hard. Arithmetic; no campaign needed |
| 2 | **EU4 estates**, the canonical ignorable mechanic — legible, well-motivated, tuned so its failure state is rarely reached; players "hardly even bother" (P1 §4.3, [Steam](https://steamcommunity.com/app/236850/discussions/0/2575445196376922029/), [Paradox](https://forum.paradoxplaza.com/forum/threads/the-updated-estates-are-quite-boring.1440709/)). *Lesson: a mechanism engineered not to fire is indistinguishable from one that does not exist* | **T-07, which this chapter owns.** Live instance: `faction_politics_v30.md:129` §1.0d Performance Audit, measured to contribute ~nothing once G606 is live | Every internal-competition threshold ships with a **control arm** (§0.1 pt 4): a seeded run that never engages the mechanic, plus a stated reachability bar — X% of campaigns cross the threshold by season N. A mechanic that fires in 0% of the control's complement is deleted, not tuned |
| 3 | **Shadow of War's War Chests** — buying the *output* of an earned relationship corroded the system for non-payers too, by breaking the causal chain; Monolith removed the market ([GamesRadar](https://www.gamesradar.com/middle-earth-shadow-of-war-devs-admit-microtransactions-messed-with-the-core-premise-but-theyll-be-gone-soon/), P2 §4.3). *Lesson: no convenience path may produce a relational outcome the Key history does not justify* | `systems/settlements/sim/ledger.py:47-58` `ledger_add`; `LedgerTag` (`:35-44`) | The commit giving the ledger its **first production writer** must (a) validate `tag.kind ∈ TAG_KINDS` — today `ledger_add` validates nothing and an unrecognised kind appends silently — and (b) add a provenance field bound to the causing Key. Test: no reachable `LedgerTag` has empty provenance |
| 4 | **The Tale-Spin effect** — DF, Nemesis and Wildermyth hit it independently; the state space grows combinatorially while authored expression grows linearly ([Ryan, Mateas & Wardrip-Fruin](https://eis.ucsc.edu/papers/ryanEtAl_OpenDesignChallengesForInteractiveEmergentNarrative.pdf); P2 §1.3/§6/§11.3). *Lesson: tracking state well is not expressing it; all three teams converged on small tagged units recombined by matching* | The Key substrate as a whole; `ledger.py` `TAG_KINDS` | Budget expression as a first-class line item **in the same milestone** as the substrate. Acceptance bar for any "emergent narrative" claim: a **specific reachable state has a specific enumerated expression path** — not that the state is tracked |
| 5 | **Duel of Wits collapsing** to "the bigger number wins fast" at a 21-vs-11 Body of Argument; Burning Wheel bolted on Bloody Versus afterwards (P3 §3.3/§S4.1 — `[UNVERIFIED single actual-play account, commonly cited]`). *Lesson: a maneuver layer earns its complexity only while the sides are close* | `systems/social_contest/sim/contest/resolver.py`; any officer-contest Ch2 proposes | A pre-roll gap detector: past a declared pool ratio, **fast-path to a single opposed resolution**. Test: assert the staged path moves the outcome distribution by more than a stated tolerance in the band where it runs — if not, the apparatus is decorative there |
| 6 | **Blades' pool-size scaling silently erasing its own failure band** — P(fail) 50%→1.6% from N=1 to N=6, no floor, well inside a normal growth curve (P3 §1.4 derived, §S4.2). *Lesson: a resolver whose relative variance shrinks with competence degrades "risky" into "a formality"* | `engine/autoload/dice_engine.py:104-123` `degree_from_net` — **the single-owned margin ladder Ch3 rightly calls the healthiest thing in the tree** | **I ran this audit on Valoria; it fails, in a way the opponent-derived-Ob ruling does not cure (§4).** Guard: a checked-in test computing all four band probabilities across the practical pool range, failing if any band drops below a declared floor |
| 7 | **The oatmeal problem** ([Compton](https://galaxykate0.tumblr.com/post/139774965871/so-you-want-to-build-a-generator)) and **WFC's local-only homogenisation** ([Boris the Brave](https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/); P4 §6/§4.3/§S4). *Lesson: variety measured on axes humans do not perceive is not variety; local coherence implies nothing global* | Ch4's VSG / P15 verify step; `systems/settlements/sim/temperaments.py` | The expressive-range gate is necessary and **not sufficient** (§8.4). Guard on the gate: *a metric that is also a knob cannot be evidence* — which forbids plotting Π against Π. Plus Compton's budget rule: **not everyone can be a main character**; concentrate generative budget rather than spreading it across 46 officers |
| 8 | **Total War's autoresolve divergence** — two paths that are different algorithms, ~20 years unfixed, exploited in both directions (P5 §3.3). *Lesson: two paths for one event are two distributions, and players route through whichever favours them* | `systems/mass_battle/sim/massbattle.py:37-50` — the survivor-ratio degree map whose own comment says it is **NOT the canonical ladder** | Reconcile it into `degree_from_net` or **register the divergence explicitly**. If a fast path is ever built, ship P5 §S2's protocol: one resolver two entry points; a two-sample K-S test on outcome distributions at the declared extremes; CI-gated. **A failing instance is a design bug, not a known issue** |
| 9 | **Dominions' single-commander rout** — "the biggest army in the universe will rout if it is led by a single commander, and he is killed" (P5 §2.3 — `[UNVERIFIED — player-community consensus, not a developer statement]`), and its mirror, **Mount & Blade's player-irrelevance at scale** (§4.3). *Lesson: the two failure directions of one seam — flat leverage dominates small N and vanishes at large N* | `engine/cross_scale/zoom_in_out.py:138-153` — **both directions are live in the same 16 lines** (§3) | Any personal→unit effect must be **a fraction of the unit's own size or cohesion, never a flat amount**. Guard: a leverage-in-band test sweeping N across three orders of magnitude, asserting the personal contribution's share of outcome variance stays inside a declared band at both ends |
| 10 | **CK2's apophenia** — a real, delightful effect its own developer flagged as not-a-mechanism; Paradox was exploring "emergence detection" because waiting for coincidence is a limitation, not a strategy (P2 §8.2). *Lesson: substrate plus player pattern-seeking is not a designed output and cannot be budgeted* | Valoria's ablation-based emergence test, wherever it lands | The ablation must be **two-armed**: remove the story-recognition layer and measure whether perceived quality moves. If it does not, that layer is not earning its cost. If it does, it is essential and missing. Running only the with-layer arm is the failure |
| **+** | **DOMESTIC — not a precedent, and the sharpest instance in the set.** Both guards believed to hold the world empty pin `generate_npc`'s **call counter**, not the population: `engine/mc_v18.py:100` says so itself (*"F7 telemetry: `world.npc_counter` (generate_npc call-count proxy)"*, assigned `:307`), and `test_pipeline_reach.py:628`'s failure message reads *"world.npcs stayed empty"* while asserting on something else. *Lesson: **a guard's name is not evidence of what it guards — assert the effect, not the call**; and "X cannot move a golden" is a measurement, so it needs a control arm before it is banked* | `test_f7_smoke_oracle.py:335`, `test_pipeline_reach.py:628`, `mc_v18.py:100,307`; live channel `npe.py:353` `simulate_npc_actions`, called each season at `systems/overview/sim/accounting.py:139` | Re-point both guards at `world.npcs` itself. Then adopt the cheap general rule: **any assertion whose message names a state must assert on that state.** Chapter 1 ran the experiment: two NPCs written into `world.npcs` left both guards green at `npcs_generated == 0` **and moved seed-42's winner from Crown to Hafenmark**, with a neutered-`simulate_npc_actions` control arm reproducing baseline byte-exact |

---

## 3. Both directions of the seam failure are already in the tree, in the same function

P5 §S5's verdict: no shipped title makes a personal actor's contribution leverage-in-band from N=1
to N=1000+. Every surveyed mechanism is either **scale-blind** (flat — dominates a small mass,
evaporates in a large one: Dominions' commander anchor, Total War's lord aura) or **fully fused**
(one engine, consistent, personal actor irrelevant as N grows: Mount & Blade). Valoria has already
committed one of each, sixteen lines apart:

```
engine/cross_scale/zoom_in_out.py:138-142
    pc_incap = scene_outcomes.get('pc_incapacitated', False)   # boolean, applies immediately (ED-159)

engine/cross_scale/zoom_in_out.py:149
    wound_ob = 0.15 if scene_outcomes.get('contested_figure_wounded', False) else 0.0
```

`pc_incapacitated` applies immediately and consults the size of nothing — the Dominions shape: a
personal-scale count with leverage over an outcome of arbitrary scale. `contested_figure_wounded` is
a **flat +0.15 Ob**, and its own comment concedes it: *"Still a flat modifier keyed on the boolean
wounded flag, not a per-wound-cumulative counter… a true wound-counter model for the CF is future
work"* (`:143-148`). A fixed Ob shift against a distribution whose standard deviation grows as
`0.8·√N` has an effect on outcome probability decaying as `1/√N` — its influence **shrinks as the
battle grows**. That is the Mount & Blade direction, in arithmetic.

**NERS-R: fail, both poles.** Leverage is not in-band across the range in either carrier. This is
the same verdict P5 hands Dominions (§2.4) and Mount & Blade (§4.4), reached independently from
Valoria's own code.

Two things save this from being a live defect, and one is not reassuring. **Matrix cell P→U is
BROKEN, not executing** — the carriers fire and no production caller queues a personal scene from a
battle; I confirmed nothing outside `zoom_in_out.py` reads either field. And **being unreachable is
exactly why nobody has had to decide.** When Chapter 3's matrix cell 3 (UNIT→PERSONAL, `EMPTY`)
closes, these two carriers become the seam's semantics by default — inherited rather than chosen.
The guard must land **before** the producer.

P5's third structural warning binds here too, and Valoria currently violates it:
`DISPATCH_COMBAT_BRIDGE` is **default OFF** (`engine/mc_v18.py:78-80`), and P5 §S1.3 found *no
precedent defending* a bridge whose default state is "off equals doesn't exist" — every surveyed
game either has no seam to disable or ships an explicit, imperfect crossing. Ship one of those two.
A flag that silently returns to zero-state is the option with no precedent behind it.


---

## 4. The vanishing band — the audit Blades never ran, run on Valoria, with a result

P3 §S4.2 asks Valoria to *"verify its σ term has a floor that doesn't collapse to near-zero relative
variance as investment rises — the same audit Blades itself never ran."* I ran it against the live
ladder, treating `degree_from_net` (`engine/autoload/dice_engine.py:104`) and the canonical face
rule (`:52-60`, values −1/0/+1/+2 at p = 0.1/0.5/0.3/0.1) as arithmetic. Fixed obstacle, `Ob = 3`
(the combat engine's `DECISIVE_OB`):

| Pool N | P(Failure) | P(Partial) | P(Overwhelming) | CV of net |
|---|---|---|---|---|
| 2 | 0.930 | 0.060 | 0.000 | 1.41 |
| 4 | 0.721 | 0.161 | 0.009 | 1.00 |
| 6 | 0.530 | **0.188** | 0.059 | 0.82 |
| 10 | 0.280 | 0.148 | 0.272 | 0.63 |
| 16 | 0.109 | 0.073 | 0.606 | 0.50 |
| 20 | 0.059 | **0.043** | 0.756 | 0.45 |

That is Blades' curve with different arithmetic: failure collapses from 93% to 6%, and the *middle*
band peaks at N=6 and then falls to 4%. Ch3 correctly identifies the opponent-derived obstacle
ruling — *"their corresponding score/2 plus modifiers"*, ruled 2026-08-14, and unexecuted by
`degree_from_net`'s own admission (*"THAT DERIVATION IS IMPLEMENTED NOWHERE"*, `:113-116`) — as the
compensating term. **It compensates for half the problem.** Re-running with `Ob = 0.5·N`:

| Pool N | P(Failure) | P(Partial) | P(Overwhelming) |
|---|---|---|---|
| 2 | 0.420 | **0.320** | 0.010 |
| 6 | 0.530 | 0.188 | 0.059 |
| 12 | 0.606 | 0.128 | 0.092 |
| 20 | 0.666 | **0.093** | 0.105 |

Scaling the obstacle with the opponent fixes the *failure*-band collapse — it now drifts the other
way, which is its own calibration problem, since a literal "score/2" against a per-die mean of 0.40
makes symmetric contests fail more often as competence rises. But **the Partial band still collapses
monotonically, 0.320 → 0.093, because the ladder's Partial window is a fixed width of exactly one
success (`0 ≤ margin < 1`) laid over a distribution whose spread grows as √N.** No obstacle
derivation can cure that; only a band width that scales with the pool can.

**This is a NERS-R defect in the one throughline the run scores as passing.** T-10's single
ownership, its guard test and its ruled provenance are real and not in question — the defect is in
the *band arithmetic underneath* the ownership, and single-ownership is what makes it cheap to fix
in one place. The guard is table row 6: a checked-in test computing the four band probabilities
across the practical pool range, failing if any band drops below a declared floor. One test file, no
campaign run.

**Where the fix would itself be an over-correction (NERS-N inverse).** Do *not* answer this with a
compensating die, a second roll or a re-roll. The engine needs one band definition parameterised on
pool size, not more apparatus. Bolting structure onto an engine that does not need it fails N and E
at once — the SKILL's own canonical over-correction.

---

## 5. Do not build the second resolver

Dominions and Mount & Blade achieve perfect resolution-consistency *by never offering a second
path*; Total War is the only surveyed precedent with two paths, and the only one with a documented,
unsolved, two-decade consistency failure players exploit in both directions (P5 §3.3, §S1, §S2). P5
states the consequence plainly: **"don't build a second resolver at all" is the first option on the
table, not a corner case.**

Valoria currently has one resolver per event, which is why T-12 is the register's only entry that
*passes* — and it passes narrowly. The hole is verified and self-disclosed:

> `systems/mass_battle/sim/massbattle.py:37-50` — three survivor-ratio thresholds (0.75 / 0.25 /
> 0.50) mapping a finished battle to a degree, whose own comment reads *"These are NOT the canonical
> degree ladder… a bespoke post-hoc classification of a finished battle's survivor ratios, and
> reconciling the two is open MB-lane work."*

That is a second degree semantics for one event class, carried over verbatim through the 2026-08-24
port so the port would be single-variable — a good reason to exist on that commit, not a reason to
persist. It is Total War's divergence in miniature: the cheap classification maintained by a
different process than the canonical one. Reconcile it or register it; do not leave it
self-disclosed and unowned, because the self-disclosure is doing all the work of a guard and none of
the work of a fix.

The same warning binds Chapter 3's matrix cell 3 (UNIT→PERSONAL). The mass-battle resolver must
**call into** `combat_engine_v1` for flagged encounters, never maintain a cheaper approximation of
what personal combat would have produced. Building it the other way commits Total War's failure
deliberately, with full knowledge, which is a worse position than Creative Assembly was ever in.

---

## 6. T-07 — the counter-force that never fires

This chapter owns T-07: *the damping or reversing arm of a bidirectional mechanism exists in the
primitive and is never invoked.* Both P1 failures land here from opposite sides — Imperator shipped
a down-direction the player could not out-invest; EU4 shipped an up-and-down system whose thresholds
were never reached. **A ladder with an unreachable rung and one with an unstoppable slide are the
same defect measured from two ends: the mechanism does not run both ways in practice.**

The cleanest verified instance is Coherence, and the function's own docstring is the falsifier:

> `engine`-side owner `systems/threadwork/sim/coherence.py:138-142`:
> *"delta: signed int. Negative = reduction (operation, FR, residue, etc). **Positive = recovery
> (non-practice season, Anchoring Scene, Einhir).**"*

I enumerated every call site — `operations.py:194`, `opposing.py:228,231`, `collective.py:179`,
`knots.py:375`. **Every one passes zero or a negative.** `COHERENCE_COST_BY_SCALE`
(`operations.py:105-113`) holds only `0`, `-1`, `-2`; `RUPTURE_COHERENCE_LOSS` is `-1`
(`knots.py:95`). Even the explicitly *restorative* operation is restorative only in the sense of not
costing: `operations.py:189-192` exempts Mending from the blanket penalty so it *"costs 0 Coherence
at EVERY degree"* — zero, not positive. So the ceiling clamp at `coherence.py:153` is unreachable
dead code: practitioners start at 10 and the tree contains no path back up.

That is T-07 in one function — a signed primitive with only one sign's caller, a recovery vocabulary
that exists only in a docstring, and a clamp guarding a direction nothing takes. The same shape
recurs at the officer ladder (Ch2's count: ~88 up-gates and ~74 demotion cells authored, 0 up and 0
down executing) and at settlement Order.

**NERS.** Coherence is not a rolling engine — the delta application is a deterministic ledger, so
NERS does not apply and I do not manufacture a verdict. It routes to consistency, and bears on **R**
wherever it appears, because *graded recoverable output* is R's own wording.

**The guard.** Row 2's control arm is the general form; the specific form for a signed primitive is
cheap and mechanical: **a sign-coverage test.** For each function whose contract declares a signed
delta, assert a seeded campaign reaches at least one call site of each sign. It is the
field-assignment-sweep pattern (`tests/valoria/test_morale_write_sweep.py`'s `_CELL_OWNED` registry,
CLAUDE.md §0.1 pt 1) applied to sign rather than assignment, and it is load-bearing on the game under
§0.1's amended predicate — its subject is a mechanic the player experiences, not apparatus.

**Where a T-07 fix would be an over-correction.** Do not answer "the up direction never fires" by
adding a *scheduled* recovery tick. P2 §11.2 row 3 is explicit that promotion and demotion should be
caused by **specific Key events, never scheduled** — a timer that restores Coherence or Standing on a
cadence converts a consequence system into a treadmill, which is the Imperator failure with the sign
flipped.

---

## 7. The inverse-N docket: five places where adding apparatus would be the error

NERS' N cuts both ways and this chapter owns the second edge: *a fix that adds apparatus must
itself be necessary*, and migrating a healthy dice engine to deterministic-odds Mode B is the equal
and opposite failure. The five sites, named:

1. **Initiation duties and recognition contests** (the rung gates of `faction_politics_v30.md`
   §1.1–§1.4). Healthy d10 pool engines where a player weighs a real bet. Migrating them to Mode B
   is the diagnostic SKILL's own canonical over-correction. Leave them alone.
2. **`crown_initiative`'s graded bidirectional standing bands** (`systems/factions/sim/crown_initiative.py`,
   ±1/±2 at eight sites). This is a healthy stochastic engine on a genuinely bidirectional ledger —
   the one place in the faction layer where both signs execute. Its defect is elsewhere and specific:
   `Faction.standing` (`engine/autoload/game_state.py:129`) is an unclamped `int` written by direct
   `+=`/`-=` at ten sites, all of which **bypass `Faction.adjust()`**, the method that reads bounds
   from `references/descriptor_registry.yaml` (`game_state.py:188-195`). It is then read straight
   into a pool: `pool = int(crown.I) + crown.standing` (`crown_initiative.py:81`). Standing feeds the
   pool that writes standing, with no ceiling. Verified: `roll_pool` floors the pool at 1
   (`dice_engine.py:78`, `effective_pool = max(1, pool_size)`), so the *downward* runaway is
   accidentally caught and the *upward* one is not. **The fix is a `descriptors` clamp — an R fix,
   one line. It is not an S-failure and Mode B here would be N-fail.**
3. **The §7.2 Persuasion-Track succession bout.** A multi-exchange contest whose track *is* the
   legible-odds surface. Flattening it to a single deterministic-odds draw destroys the very
   legibility Mode B is adopted to provide — fails N and E simultaneously.
4. **Mass-battle resolution feeding conquest** (`systems/factions/sim/faction_action.py:433-528`).
   Already excluded from ED-874's scope for exactly this reason; the battle engine is the odds
   surface and a second deterministic layer above it would be a second resolver (§5).
5. **The deterministic entry/exit predicates of the yield state machine** (T-17's MB implementation).
   Adding a draw to a boundary predicate is the classic S-failure — dice on a deterministic ledger —
   pointing the wrong way.

Where Mode B *is* the remedy, and this chapter endorses it: `systems/factions/sim/treaty.py:42-46`
and `:135-142`. A flat `TREATY_LAPSE_RATE_DEFAULT = 0.90` per arc and a flat
`TREATY_CONSENT_RATE_DEFAULT = 0.28`, unconditioned on any state, rolled over a pure ledger of
active treaties — **S-fail and E-fail together.** I verified the fallback: `roll = rng.random() if
rng else 0.95`, compared `roll < lapse_rate`, so with no RNG a treaty can never lapse at any
canonical rate in the 0.90–0.95 band. The module has zero callers, which is the only reason this is
dormant rather than live.

---

## 8. Four things nobody wants in a proposal document

### 8.1 No precedent solves the cross-scale problem. This needs original design work, not adaptation.

P5 surveyed nine titles plus the naval-attrition literature and reports: *"No precedent in this
survey demonstrates a mechanism whose personal-scale contribution is provably leverage-in-band across
the full range from N=1 to N=1000+."* Every mechanism found is either scale-blind or fully fused. P5
adds the reading that matters: the Dominions and Mount & Blade failures are best read as evidence
that **well-funded teams tried and did not solve it**, not that nobody looked.

Valoria's officer object, if it is meant to genuinely bridge `combat_engine_v1` and `mass_battle`
rather than decorate one with the other's flavour, is attempting something with no worked precedent.
P5's equivalence protocol (§S2) verifies that *resolution* stays consistent; **nothing in the survey
tests whether the personal contribution's relative weight stays sane across three orders of magnitude
of mass size.** That metric must be designed from scratch. Say so plainly in any officer proposal
rather than implying the seam is an imported pattern.

### 8.2 There is no cheap general expression channel for interior state, and the Key substrate does not supply one.

Ryan, Mateas & Wardrip-Fruin name Challenge 2 *"perhaps the hardest challenge we present in this
paper"*: physics has graphics, so any reachable physical state is visible at zero marginal authoring
cost, and **no equivalent exists for mood, grudge, loyalty or ambition**. Every P2 mechanism that
"solves" it narrows scope rather than generalising — DF's templated flavour text over a facet band,
Nemesis's small closed trait vocabulary, Wildermyth's hand-written per-personality variants
(explicitly not procedural, by its developers' own account).

P2 asks one sentence be carried verbatim: **any Valoria plan that treats "we have the Key substrate"
as equivalent to "we have emergent narrative" is skipping exactly the step every precedent struggled
hardest with.** Tracking and expressing are different problems, and the field failed at the second.

### 8.3 Legibility and depth are different axes — every steal in Chapters 1–4 is a partial answer

Stated in §1; restated as a *hardest truth* rather than a framing device. Operationally: when
Chapter 2 borrows CK3's landless track, EU4's Loyalty-vs-Influence revocation gate or Shogun 2's
visible-band-over-hidden-value, each arrives with a documented failure attached (P1 §A's own
annotations) and the chapter must carry the attachment. **A borrowed mechanism whose failure mode is
not stated has not been researched, only cited.**

### 8.4 No general method certifies generated content is *good* — only that it is *varied*. Chapter 4's gate must not be oversold.

P4 §S5 is the field's own textbook, not an outside critique: Chapter 12 of Shaker/Smith/Yannakakis
says evaluation appropriateness for autonomous PCG *"remains largely unexplored"*, that ERA and
questionnaires are explicitly complementary and partial, and — fourteen years after Smith &
Whitehead — the follow-on literature ([*The Right Variety*, 2023](https://arxiv.org/pdf/2304.02366))
is still arguing about **which metrics to plot**. Compton's "interesting" and "characterful" are
named as real target properties with *no proposed measurement at all*.

So, by name: **Chapter 4's expressive-range gate catches collapse and pinning reliably, and cannot
certify that a non-collapsed generator produces settlements, factions or officers that feel
meaningful.** That residual closes by human design review and player testing, and by nothing in the
dossier. Ship the gate — it is the right instrument, and P4 §S4.3 shows the same protocol verifies
balance-loop health too, so it is one instrument rather than two — but state its ceiling in the same
paragraph. A gate presented as a quality certificate is worse than no gate: it stops the next reader
asking the question it cannot answer.

One sequencing point from the tree: the Π runaway everyone cites is currently **unreachable**,
because `Settlement.pressure: float = 4.0` (`systems/settlements/sim/registry.py:79`) has, as I
verified, exactly three references in the whole tree — its declaration, `to_dict` at `:122`, and
`from_dict` at `:147`. Zero readers, zero writers. **Write the boundedness test before the writer**;
P4 §S1 Step 6's zero-noise limit check is pure arithmetic and needs no kernel.


---

## 9. The worked example: this run made the error it is warning about, four times

A document arguing that Valoria's characteristic hazard is mistaking a shared *word* for a shared
*mechanism*, and a shared *name* for a shared *mechanism*, has an obligation to record that its own
authors did exactly that — four times, three of them caught by the adversarial stage and one by an
experiment. This is not self-flagellation. It is the strongest available evidence that the
independent stages earn their cost, and it is the most useful methodological content in the chapter.

**Error 1 — `Standing` (`L0g_RETRACTION_standing.md`).** The orchestrator claimed `ED-SC-0014`
ratified the officer ladder's scale to 0–10 and left it unexecuted, so `faction_politics_v30.md`'s
eight-rank ladder was written against a scale that does not exist. The ruling
(`references/id_reservations_history.md:73`) says the opposite: *"BG faction track 0-10; **scope-tag
the cross-scale homonym with the contest kernel**"* — a ruling that Standing is a homonym naming
different mechanisms, whose senses must be **tagged apart**. The evidence cited was
`contest/primitives.py:31-36`, which I opened: a per-bout ethos float with `build(deg)`/`strip(deg)`
at 0.8 per degree, reset each contest. It shares a word with a rank ladder and shares no state, no
invariant and no failure topology with it. **The orchestrator promoted a vocabulary collision to a
mechanism claim — the precise move the run's constitution forbids — and fired its own falsifier**,
since a different module (`Faction.standing`) does own a durable standing scale.

Three generalisable properties. **Only the independent reader caught it**: two lanes, an audit and
the orchestrator all touched `Standing`, and the one that found the error went to the class
definition instead of the comment naming a range — as did both of the document's earlier
corrections. **None of the three came from re-reading**, so more producer effort would have found
none of them; CLAUDE.md §10's relay is the only mechanism in the corpus with a measured hit rate on
this error class. **The refutation produced a better finding than the claim it destroyed** — §7's
item 2, `Faction.standing` unclamped and feeding the pool that writes it, did not exist as a finding
until the tidy claim was killed. And **the failure had a direction**: the orchestrator's own audit
names it — *when a fact could be read as supporting the tidy story, it was read that way* — which is
a bias, not carelessness, and predicts at least one surviving instance in these five chapters.

**Error 2 — over-generalisation (`L0c_counter_case.md`, PART 1 §1.2).** The first thesis grouped ten
unrelated absences into one pattern; the audit narrowed it to seven. A dropped constructor write is
not a missing caller, a ruled-but-unexecuted item is not an unwired one, and a property of authored
prose is not a state of the code. The narrowing **raised** the evidence class — from "grouped by
consequence", which the brief forbids, to "shared invariant by construction". The counter-case that
forced it must travel with the thesis: *"zero production callers" is the definition of
not-yet-wired, not a diagnosis.* What defeats it is not the list but three discriminators — the
one-directional emit/consume asymmetry (60 declared / 3 observed), the **guarded** absence
(`strict=True` xfail plus a golden asserting `npcs == 0`), and ratification-outrunning-execution as
a measured class. Assert the thesis without the first two and you assert the vacuous version.

**Error 3 — the brief's replacement number was itself stale, read out of a comment that exists to
record what the value used to be.** Constraint 6 binding all five chapters says: *"Do not propagate
the retracted ~87% degenerate win-share. The live golden is `{Crown: 37.5, Church: 12.5, Hafenmark:
12.5, Varfell: 37.5}`."* I checked before being told. At HEAD the executing constant is
`GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}`
(`engine/tests/test_f7_smoke_oracle.py:267`), regenerated 2026-08-24 at the mass-battle engine swap.
The quoted figure survives in exactly two places, both prose: the module docstring at `:16`, and a
comment block at `:74-78` whose own header reads *"OLD (pre-OI-04, pre-transfer-motion) values,
**preserved for the before/after record**."* So the instruction warning five writers against
propagating a retracted number handed them, in the same sentence, a superseded one — read out of an
annotation whose stated purpose is to say *this is not the current value*.

**What makes it worth the space is where it happened.** Forty lines below, at `:262-265`, the same
file carries the rule that would have prevented it, written by whoever paid for it last time:

> *"A golden test pins the LIVE constants; nothing pins the prose, so a fabricated history stays
> green forever and the next re-recorder reasons from it. Restored from git. Rule: a PREVIOUS line
> is read out of `git show <ref>:<file>`, never copied from the constant you are about to
> overwrite."*

Someone earned that rule and wrote it down at the point of use — exactly what CLAUDE.md §4 asks for
— and the next reader violated it anyway. **That is evidence that prose annotation is not sufficient
protection, in the one experiment where the annotation was placed as well as it could be.** The
generalisable claim: *a preserved historical value sitting beside a live one is a trap*, and the
guard that works is mechanical, not textual — the live constant should be the only copy reachable
without an explicit `git show`. For this run: `Varfell 87.5` remains retracted; `{37.5, 12.5, 12.5,
37.5}` is a superseded pin; the live one is `:267`, and any chapter quoting a win-share should quote
**the line the interpreter reads**.

**Error 4 — "golden-safe by construction" was asserted, and refuted by experiment.** The run's D7
position held that loading persons at world-gen could not move a seeded golden, on the strength of
`populate_from_geography`'s precedent. Chapter 1 tested it instead of believing it, and the claim is
false. I verified the mechanism by reading: **both guards pin a call counter, not a population.**
`engine/mc_v18.py:100` labels the field in its own comment — *"F7 telemetry: `world.npc_counter`
(generate_npc call-count proxy)"* — and assigns it at `:307`; `test_f7_smoke_oracle.py:335` and
`test_pipeline_reach.py:628` both read that field. The second is the sharpest artifact in the
corpus: its failure message reads *"world.npcs stayed empty (OI-05: generate_npc has zero
callers)"* while the assertion beside it examines `r.npcs_generated`. **The message names the state;
the assertion reads the counter.** Two NPCs written straight into `world.npcs` therefore leave both
guards green — and moved seed-42's winner from Crown to Hafenmark.

The channel is `systems/world/sim/npe.py:353` `simulate_npc_actions`, called unconditionally each
season at `systems/overview/sim/accounting.py:139`, pulling `world.rng` for a pairwise Volatility
check over every NPC pair in a territory. One precision to add to the report as it reached me: with
the store empty the inner loops never execute, so the function draws **zero** times today while
being *invoked* about 400 times per golden batch (50 seasons × 8 campaigns). It is not consuming
entropy; it is a live RNG consumer sitting one non-empty dict away from consuming it, and the golden
cannot see the difference.

Three lessons, different in kind from the first three. **This one could not have been caught by
reading** — reading is what produced the false belief, because the guards are named for what they do
not check; the control arm (neutering `simulate_npc_actions`, reproducing baseline byte-exact) is
what converts "the golden moved" into an attribution, CLAUDE.md §0.1 pt 4 vindicating itself on the
run's own work. **It retires a shortcut the whole run leaned on** — "golden-safe by construction" is
now available only for a manoeuvre *demonstrated* deterministic, and the demonstration must include
the downstream consumers of the state, not just the writer. And **it is §0.1 pt 2 in the wild**:
*an assertion must be able to observe the failure it excludes.* Both guards are unfalsifiable with
respect to the thing they are named for — not a weak test but an absent one, surviving because its
name was reassuring.

---

## 10. Falsifier, coverage, and what I did not cover

**My falsifier, per CLAUDE.md §0.1 pt 3.** *If any recommendation in Chapters 1–4 has no precedent
failure attached to it in this chapter, this chapter is incomplete.* Against the five commissions in
PART 4 I count **25 distinct recommendations**. Twenty-one carry an attached failure: the person
loader and golden re-pin (rows 3, 4, 10, and — decisively — the **+** row, domestic rather than
borrowed, which refutes the golden-safety premise the loader rested on); `hidden_allegiance`'s
constructor argument and `Key.causes`' honest writers (row 3); the officer object, demotion writers,
the `Faction.standing` clamp, the ledger's first writer, treaty Mode B, the §6.4 fate d10 and
bloc/patronage design (rows 1, 2, 3, 5, §7); TN consumption, the opponent-derived Ob, the third
degree map, contest-kernel starvation, the σ floor and the mass-battle call-in (rows 5, 6, 8, 9,
§§3–5); VSG execution, the expressive-range gate, the Π boundedness test, the event-deck cap and the
conviction matrix (rows 7, 10, §8.4).

**Four carry none, and I say so rather than manufacturing one.** (i) **ED-FA-0018**, the
examination-style credentialing pipeline for the flat Crown Administrative branch — no P1 title
ships a merit-examination office ladder, so the dossiers supply no failure to bind; Chapter 2's
genuine escalation candidate arrives unguarded. (ii) The **`T16` adjacency hole** — a one-line data
omission. (iii) The **`ledger_add` validation gap** as distinct from provenance — an ordinary defect
with no precedent behind it. (iv) The **`Key.causes` hashing convention** (T-14) — P2 and P4 both
assume stable content addressing and neither documents a failure of one. **Four of twenty-five** is
what this chapter's falsifier returns.

**Locators I checked myself at HEAD `571ae14`.** Twenty opened and read, all confirming what I say
of them: `game_state.py:109-137` + `:188-195` (Faction dataclass; `standing: int = 0` at `:129`;
the `adjust()` bounds path every `standing` write bypasses) · `contest/primitives.py:31-48` ·
`dice_engine.py:52-84` and `:104-123` · `massbattle.py:37-50` and `:63-90` · `registry.py:65-105`
(plus a grep confirming `pressure` has three references in the whole tree) · `ledger.py:25-58` ·
`treaty.py:42-46` and `:121-142` · `coherence.py:138-158` **plus all five call sites of
`apply_coherence_delta`, none of which passes a positive delta** · `zoom_in_out.py:105-160` ·
`scene_dispatch.py:118-139` · `npe.py:320-350` · `mc_v18.py:64-80` · `faction_layer_v30.md:599-614` ·
`faction_politics_v30.md:129` · `mc_v18.py:100,307` · `test_pipeline_reach.py:628` ·
`test_f7_smoke_oracle.py:16,74-78,262-267,335` · `accounting.py:130-143` · `npe.py:353-383`.

**Two did not check out, and both were the brief's own.** (i) The "live golden" win-share
`{37.5, 12.5, 12.5, 37.5}` is a superseded pin surviving in the module docstring at `:16` and in a
comment block at `:74-78` explicitly labelled *"OLD … preserved for the before/after record"*; the
executing constant is `{'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}` at
`test_f7_smoke_oracle.py:267` (§9, Error 3). (ii) "Golden-safe by construction" for a person loader
is false — both guards pin `world.npc_counter`, not `world.npcs` (§9, Error 4, and the **+** row of
the guard table).

**What I did not cover.** I ran no test suite and no campaign — every verdict above is a code read
(D-14), except Chapter 1's experiment, credited as theirs. I re-verified no precedent URL; P1–P5's
citations are carried at their own confidence with `[UNVERIFIED]` and community-derived marks
preserved (notably P5's Dominions assassination-meta claim, P3's Duel of Wits account and its whole
Blades failure corpus, P2's Nemesis depth critique). I did not open the archived 579-document
corpus, nor `jordanelias/valoria-game`, so nothing here bears on the five-of-seven junctures
reportedly implemented there. I did not run CLAUDE.md's five tests on ED-FA-0018 — Chapter 2 owns
that and must, before treating it as Jordan's.

I deliberately refused the tempting merge between this repository's measured apparatus loop
(CLAUDE.md §0.3 — closed, gain > 1) and the game's measured pathology (open circuits: readers
without writers, writers without readers). The topologies are opposite, docket item D-13 rejects the
merge, and the one parallel that survives scrutiny is narrow and belongs to T-07 — **a declared
counter-force with no executed path**, true alike of Coherence's recovery arm and of 191 "reduce"
commits that were a net +82,020 lines. That is a fact about authoring practice, reported explicitly
**below** the (a)/(b)/(c) bar for a mechanism throughline, and it is not a throughline. Finally, I
did not evaluate any Chapter 1–4 recommendation's *merits*; this chapter constrains proposals, it
does not judge them.
