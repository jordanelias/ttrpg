# F6 RULED BY JORDAN — the world is in FLUX, and its trajectory is a function of tending
# Verbatim: "The world is neither dying nor misunderstood -- rather, it is in a state of flux. If the
# world is not tended to by anyone, it will die. If it is tended to by everyone, it will thrive. What
# people think is the best way to tend to the world, though, and their ambitions within that world are
# the regions that drive conflict."

## This is a THIRD answer. Neither branch offered it.
The fork as filed was *a real trajectory the player must arrest* versus *a fact everyone reports
wrongly.* Both are **fixed**: one fixes the world's direction, the other fixes it at zero and puts the
variance in the reporting. **Jordan's answer makes the direction an OUTPUT** — the sum of what people
do about it. That is strictly better than either branch and it is why the fork survived five audits
undissolved: the missing option was not a parameter, it was a **sign**.

---

## CONSEQUENCE 1 — THE ARCHITECTURE AS WRITTEN CANNOT SAY THIS. `wear` is required.

`01_ARCHITECTURE.md:1111` — *"The slow fuses are **act-only**: `condition(site) = clamp(condition + Σ
this season's resolved deltas, 0, 1)`"* — and `:1113`, *"**A site that decays with nobody touching it
must be a matter event.**"*

> **Under act-only, an untended site does not die. It FREEZES.** `Σ acts = 0` leaves condition exactly
> where it was, forever. *"If the world is not tended to by anyone, it will die"* is **unwritable**.

⚠ **This reopens #343's D-1, and D-1 was right about the thing it actually caught.** Round 1 added
`season_factor` — a multiplier centred on 1.0 — to a `[0,1]` accumulator. That is a units error, and it
would have made **weather permanent** by routing an impermanent quantity into a persistent one
(`13:70-71` assigns permanence to `base(H)` and impermanence to `season_factor`). Deleting *that limb*
was correct. **Concluding that the accumulator must therefore be act-only was too strong**, and §15.19
recorded the cost honestly at the time: *"A fuse that is act-only cannot model a site that decays with
nobody touching it."* Jordan has now ruled that cost unacceptable, because untended decay **is** the
world model.

> **THE CORRECTED FORM. One term, dimensionally clean, and weather stays where D-1 put it.**
> ```
> condition(site) ← clamp( condition(site) + Σ (this season's resolved deltas) − wear(kind(site)), 0, 1 )
> ```
> `wear` is **a per-site-kind constant in the same units as `condition`** — a fraction of full condition
> per season. It is not weather, not a multiplier, and not a roll. `season_factor` and `(3+d10)/8.5`
> remain exactly where D-1 put them, inside `yield`. **The units error is not reintroduced; only the
> sign is.**

**It is an authored per-season constant, and that must be said out loud.** `SUP:1345` congratulated the
design on having *"no hidden per-season constant anywhere in the fuse."* Jordan's ruling **requires
one**. The honest position is that it is now *justified rather than hidden* — it is the world's
entropy, it is the quantity the whole political layer exists to argue about, and it belongs in the
centralized parameter table where code reads it (`CLAUDE.md` §0.05), one row per site kind.

### Why this is exactly Jordan's sentence, mechanically
| tending | arithmetic | outcome |
|---|---|---|
| **nobody** | `Σ acts = 0`, condition falls by `wear` each season | crosses a band floor · verbs leave · **the world dies, and no person did it** |
| **everyone** | `Σ restoration ≥ wear` | condition holds or climbs · **it thrives** |
| **some** | the *distribution* of tending decides **which sites** live | **that is the game** |

### And it converts D-2 into the load-bearing scarcity of the whole design
Under act-only, restoration was pure gain and neglect was free. **Under `wear`, maintenance is a
permanent tax and neglect has a price.** So the question *"how many person-seasons does this harbour
cost to keep open"* becomes a real, computable political quantity — and every one of those
person-seasons is drawn from the one-act-per-person budget `D2_PROPOSAL.md` proposes. **The act economy
stops being a bookkeeping fork and becomes the thing factions actually fight over.** The two rulings
converge; neither was written with the other in view.

---

## CONSEQUENCE 2 — CONFLICT'S TWO SOURCES. One is already shipped; one has no carrier.

*"What people think is the best way to tend to the world, and their ambitions within that world, are
the regions that drive conflict."*

**(a) Competing tending-doctrines need NO new object.** A doctrine is a Proposition of mood **`OUGHT`**
scoped to a site or a class of sites — *"the seam must be worked now"* against *"the seam must be
rested"*. `SUP:1519-1523` makes `when` a mandatory interval, so two such propositions with intersecting
scope and incompatible values **collide automatically**, and §10.1's mechanism already forms a faction
out of the people whose practice used the verb. **Shipped, and it is the design at its best.**

**(b) AMBITION has no carrier anywhere.** Verified: `ambition` and `goal` each occur **zero** times
across all 3,780 lines of the v2 suite. The scope runner flagged goals and ambitions as missing; Jordan
has now made them load-bearing on conflict itself.

> **THE ANSWER, and it adds no object.** An **ambition is an unsatisfied `commit` Tenure whose object is
> an `OUGHT` Proposition about the holder's own future** — *"I will hold the praefecture"*, *"my house
> will hold Grauwald"*.
>
> It inherits everything from primitives that already exist: it is **disputable** (others may hold
> claims about what you want), **concealable** (a commitment may be secret), **betrayable** (degree → 0
> is abandonment), **inheritable** (rows pass at reduced magnitude on succession), and — decisively —
> **it already drives `choose` with no new wiring**, because *commitment — a proposition you hold,
> unsatisfied* is one of the four needs (`SUP:187-190`) and reads the **view**.

So a man's ambition makes him hungry in exactly the way a shortfall does, and both arrive at `choose`
through the machinery already specified.

---

## THE NET COST OF THE RULING: one constant, zero objects.
`wear(kind)` in the centralized parameter table, one row per site kind — and one paragraph naming
ambition as a shape the primitives already make. **Nothing else in the v2 architecture changes**, which
is the strongest available evidence that its primitive set is the right one: a ruling that reverses the
world's whole trajectory model costs it a single number.

## What must be re-checked, and honestly
- **§14 row 12** — *a scheduled recovery tick on standing.* `wear` is a scheduled tick, so the row must
  be re-walked. It should clear: the row governs **standing**, a social quantity, and `wear` moves
  **matter**. §10.6 condition 1 licenses exactly this — *"the quantity crossed is matter or bodies,
  never a social quantity."* **But it must be walked, not glossed.**
- **§13.2's licensed decider-free channels.** `wear` is a non-act change to the world, so it must sit
  inside channel 1 (metabolism and nature) or be named a fifth. It is nature — a harbour silts, a road
  washes out — and channel 1 already carries *"crops yield, wounds close or fester, bodies age."*
  **Entropy belongs with metabolism, and this is the ruling that makes the channel's name honest.**
- **The balance question nothing here can settle:** the ratio of `wear` to a restoration act's effect
  sets the world's whole difficulty curve, and no number in this design has been measured.
