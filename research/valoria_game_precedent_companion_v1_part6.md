# Game Precedent Companion — Part 6: The Precedent Games, Decomposed in Valoria's Own Slices

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: Part 5 (the matrix). **This part is what makes the matrix flattenable against Valoria.**

**Reading order:** [Part 1](valoria_game_precedent_companion_v1.md) → [Part 2](valoria_game_precedent_companion_v1_part2.md) → [Part 3 · Critique](valoria_game_precedent_companion_v1_part3.md) → [Part 4 · Reconcile & Unify](valoria_game_precedent_companion_v1_part4.md) → [Part 5 · Matrix](valoria_game_precedent_companion_v1_part5.md) → [Part 6 · Decomposition](valoria_game_precedent_companion_v1_part6.md)

Part 5 puts the games side by side. **That is an index, not a decomposition** — and an index cannot be
flattened against Valoria, because Valoria's flatten is written in a specific vocabulary and the
matrix is written in prose.

So this part decomposes each surveyed mechanism **into the integration master's own slices**, with the
resolution shape annotated, so that a row from a precedent game and a row from Valoria's flatten sit
in the same schema and can be compared cell for cell.

### The vocabulary, restated so the rows are readable

| slice | stores state? | the question it answers |
|---|---|---|
| **primitive** | yes | where does this live between turns? |
| **derivative** | no — computed | what happens when its inputs move? |
| **formula** | n/a — the expression | is this arithmetic the same everywhere it appears? |
| **mechanic** | one resolution event | what does the player do, once? |
| **process** | several mechanics in order, usually on a clock | what happens whether or not anyone acts? |

| shape | meaning |
|---|---|
| **U** | Unopposed — a pool or value against a fixed or state-derived obstacle |
| **SO** | Statically opposed — the obstacle derives from a target's state; the target does not roll |
| **DO** | Dynamically opposed — both sides roll; one wins |
| **BI** | Bilateral — both sides roll **and both outcomes bind** |
| **GATE** | Deterministic — a threshold comparison, **no roll at all** |

`GATE` is added here and is not in the master's set. **That addition is itself a finding** — see §13.7.

---

## §13.1 Victoria 3 — law enactment, decomposed

| slice | the thing | detail |
|---|---|---|
| **primitive** | Interest Group | holds **clout**; is either in government or in opposition |
| **primitive** | Movement | holds **participation %**, which rises and falls |
| **primitive** | Legitimacy | 0–100 |
| **primitive** | Enactment | a **stage index** and a **setback count** — the state that makes a law a process rather than an event |
| **derivative** | government clout | Σ clout of governing IGs |
| **derivative** | Legitimacy | from governing clout, plus vote share where elections exist |
| **formula** | success contribution | Σ clout of supporting governing IGs + Σ support of active supporting movements |
| **formula** | stall contribution | Σ from all non-marginalized opposing IGs and movements |
| **formula** | ruler stance | ±5% per step of difference |
| **formula** | duration | 100 days base × class multiplier (×2 governing-principle, ×1.5 power-distribution) × legitimacy modifier (−25% above 90, +50% at 25–49) |
| **formula** | failure | **3 setbacks → fail, 2-year lockout** |
| **mechanic** | the per-stage resolution | **shape SO** — the obstacle derives from the opposition's state and the opposition does not roll |
| **process** | enactment | stages in sequence, each carrying the mechanic |
| **process** | counter-mobilisation | attempting the law raises participation in opposing movements — **half immediately, the rest bleeding in weekly**; above a threshold, revolution *`[UNVERIFIED against current patch]`* |

**The shape discussion, and it is the point.** This is `SO` **with a feedback term on the obstacle**.
Ordinary `SO` derives an obstacle from a target's *current* state. Victoria 3 derives it from a state
**that your attempt itself moves** — so the obstacle you face at stage 3 is partly a consequence of
having attempted stages 1 and 2.

**Valoria has no obstacle anywhere that responds to being attempted.** Every `SO` site in the tree
(Excommunication's `Ob = round(accused.L)`, Parliamentary Transfer's `Ob = holder.L + 2`, Coronation's
`Ob = floor(church.L/2)+1`) reads a stat the attempt does not touch. That is not a missing feature; it
is a **missing shape**, and it is the one the survey rates most highly.

**And a sub-mechanic worth separating out:** the three-setback counter is a *primitive*, not a formula.
It is what lets a process fail **without** any single stage failing — a thing no Valoria mechanic can
currently express, because every Valoria resolution terminates in one roll.

---

## §13.2 Burning Wheel — *Duel of Wits*, decomposed

| slice | the thing | detail |
|---|---|---|
| **primitive** | Statement of Purpose | the declared stake, fixed **before** any dice |
| **primitive** | Body of Argument | Will + successes from a register-appropriate skill (Oratory / Rhetoric / Persuasion / Interrogation) |
| **primitive** | the scripted volley | three manoeuvres, **committed in secret**, revealed simultaneously |
| **formula** | BoA | `Will + successes` |
| **formula** | compromise | **scaled to how much of the winner's own BoA was destroyed** |
| **mechanic** | the exchange | **shape BI** |
| **sub-mechanic** | manoeuvre selection | seven verbs: Point, Dismiss (attack); Avoid, Obfuscate, Rebuttal (defend); Feint, Incite (special) |
| **process** | the duel | volleys until one BoA reaches zero |

**The shape discussion.** `DO` and `BI` differ by exactly one rule. Strip the compromise and this is
`DO` — both roll, one wins, the loser gets nothing. **The compromise rule is what makes it
bilateral**, because it forces the winner's outcome to be a function of the loser's performance.

That is the cheapest possible route to `BI`, and it generalises: *any* `DO` mechanic becomes `BI` by
scaling the victor's payoff to what winning cost. The survey rates this **"the most valuable single
loan"** and it is one rule, not a subsystem.

**The failure, in slice terms.** The manoeuvre set collapsed because the seven verbs differ only in
**formula** (how much they subtract) and not in **primitive** (what they change about the argument's
state). Players found the two with the best formula and stopped. So the constraint is precisely
stated: *a manoeuvre must alter a primitive, not just apply a formula.*

**A second, separable sub-mechanic:** simultaneous secret scripting is not part of the resolution at
all — it is a **commitment layer above it**. It converts a sequence of checks into a prediction game
without touching the arithmetic. Valoria has no commitment layer anywhere.

---

## §13.3 CK3 — levies and men-at-arms, decomposed

| slice | the thing | detail |
|---|---|---|
| **primitive** | levy pool | per holding, regenerating; **costs zero gold to raise or hold** |
| **primitive** | MAA regiment | a typed, individuated standing unit with a stationing location |
| **primitive** | vassal contract | negotiable terms — and the special roles trade **one kind of extraction for another**: Scutage (+50% tax, −75% levy), March (−50% tax, +20% levy/garrison), Palatinate (−20% tax *and* levy, prestige to both) |
| **derivative** | available levy | from contract %, control, and opinion |
| **formula** | MAA maintenance | carried **even while unraised**; **roughly triples once fielded** |
| **mechanic** | raise levies | **shape GATE** — a deterministic draw-down against political and temporal conditions |
| **mechanic** | recruit MAA | **shape GATE** — gold and prestige thresholds |
| **process** | muster travel time | the temporal rationing that makes levies non-instant |
| **primitive** | anti-micromanagement caps | **one "tyrannical" contract change outstanding at a time**; escalating opinion costs (−15 then −25 for successive increases against +5 then +10 for decreases); a per-vassal frequency cap |

**The shape discussion, and this is the sharpest finding in Part 6.**

> **The genre gates where Valoria rolls.**

CK, Shogun 2 and Medieval II all resolve recruitment as a **deterministic gate**: you meet the
conditions or you do not. **Valoria's `_try_muster` is a roll** — `pool = Mil + floor(W/2)` against
`Ob 1`, shape `U`. So Valoria applies its resolution kernel to a question every surveyed franchise
answers without dice.

That is a real divergence and it is not obviously wrong — but it should be *chosen* rather than
inherited. Rolling makes recruitment a risk; gating makes it a budget. **Valoria has the risk and,
because Wealth has no income, none of the budget** — which is the worst of both: an uncertain
outcome on a resource with no scarcity.

**The anti-micromanagement caps deserve their own row** because they are a primitive Paradox built
*as a guardrail rather than as content* — trusting players to self-regulate was the rejected option.
Nothing in Valoria's design has that character.

---

## §13.4 Jagged Alliance 2 — morale and loyalty, decomposed

| slice | the thing | detail |
|---|---|---|
| **primitive** | per-merc morale | the aggregate the player sees moving |
| **primitive** | pairwise opinion | a **±25 matrix** over every merc pair |
| **primitive** | town loyalty | per sector |
| **primitive** | tolerance clock | **hidden** — the actual defection trigger |
| **derivative** | effective morale | from the five-layer stack |
| **formula** | idleness | after three days without offensive action, dock merc morale **and** town loyalty |
| **formula** | recruitment consent cost | town loyalty **per unit purchased** — 0.1 regular, **0.15 veteran** — charged **globally**, not to the receiving sector |
| **formula** | channel pricing | train militia ≈ $75/head vs buy regulars ≈ $440/head, at **2× daily upkeep** |
| **mechanic** | defection | **shape GATE against a hidden threshold** — not a roll the player ever sees |
| **view** | the v1.13 audit tool | itemises **every pairwise opinion by source**. Changes no mechanic |

**The shape discussion.** The defection mechanic is a `GATE`. It is not a contest, not a roll, and it
never surfaces odds. Everything the player experiences as *drama* comes from the **primitives being
legible while the gate is not.**

**And the last row is not a slice the master's taxonomy has.** The v1.13 audit tool altered no
primitive, no formula and no mechanic — and it is the single most-cited fix in the personnel research,
because it converted a resented system into a legible one. See §13.7.

---

## §13.5 Kremlin and John Company — the shared contested object

| slice | the thing | detail |
|---|---|---|
| **primitive** *(Kremlin)* | politician | position in a pyramid, **age**; owned by **nobody** |
| **primitive** *(Kremlin)* | influence | held **per player, per politician** |
| **mechanic** *(Kremlin)* | influence placement | **shape DO** — players contest control of an object neither holds |
| **process** *(Kremlin)* | ageing and death | the pacing clock, requiring no design attention |
| **primitive** *(John Company)* | office | held by one player, with powers that are **complementary rather than sufficient** |
| **mechanic** *(John Company)* | a venture | **requires several offices held by different players to cooperate** |
| **process** *(John Company)* | the Parliament phase | can change the game's own rules |

**The shape discussion.** Both games are built on a primitive Valoria does not have anywhere: **an
entity that is contested rather than owned.** Every Valoria entity has a single owner field —
`Territory.owner`, `Settlement.governor_id`, `Faction.territories`. There is no object over which two
factions hold competing partial claims.

This is the structural reason the roster research's `custodian_id` versus `holder_id` proposal reads
as novel inside Valoria and reads as ordinary outside it: **the genre solved shared control decades
ago, in board games, by not making ownership a scalar field.**

---

## §13.6 Total War — autoresolve, decomposed, and why it cannot be fixed by tuning

| slice | the played path | the auto path |
|---|---|---|
| **primitive** | unit positions, facing, morale, fatigue, terrain | army composition summary |
| **derivative** | line of sight, flanking, cohesion | strength ratio |
| **mechanic** | real-time engagement | a scalar comparison |
| **process** | the battle, over minutes | **a formula, evaluated once** |

**The shape discussion, and it is the cleanest structural statement in this document.**

> The played path is a **process**. The auto path is a **formula**. They are different slices, and
> **two different slices cannot be calibrated to agree** — only their outputs can be made to agree
> *on average*, which is exactly what twenty years of complaints say is insufficient.

That reframes the null. Total War's failure is not that its autoresolve is badly tuned; it is that a
formula was asked to stand in for a process, so it is **systematically** wrong for any battle whose
outcome turned on a dimension the formula does not carry. Both dominant complaints —
*"too punishing"* and *"doesn't credit my army's quality"* — are that single fact seen from two sides.

**Football Manager avoids it by keeping the slice constant:** three fidelities of *one engine* means
instant-result is the **same process** run headless, not a formula approximating it.

**Valoria's parliamentary bridge is currently the Total War shape**, and the fix is a slice change
rather than a tuning change: make the auto path resolve **the same specific slate event** the played
path would, through the same kernel.

---

## §13.7 The slice the taxonomy is missing

Three separate rows above did not fit the master's five slices, and they are not marginal:

- **JA2 v1.13's audit tool** — changed no mechanic, and is the most-cited fix in the personnel research.
- **Shogun 2's visible band over a hidden precise value** — the presentation form that makes a hidden
  threshold feel principled rather than arbitrary.
- **Victoria 3's shown percentage** — the reason its enactment stages are playable rather than dead
  time. The survey states it directly: *"if the running probability is hidden, the intermediate stages
  are dead time."*

None is a primitive, derivative, formula, mechanic or process. Each is a **view**: a rule about what
the player is shown of state that already exists.

**Valoria's slice taxonomy has no cell for this, and that is why U-1 — the Disclosure Contract — had
nowhere to live in Part 4 except as a "DOC" item.** It is not documentation. It is a class of design
object the corpus keeps rediscovering, that costs no mechanics, and that the survey's own evidence
says decides whether a system is loved or resented.

**Proposed sixth slice: `view`.** Stores no state, computes nothing, resolves nothing — governs what
of an existing primitive is disclosed, at what granularity. Its addition would let U-1 be *specified*
rather than merely asserted, and would give the eleven writers of Proposal 1 somewhere to declare
their disclosure alongside their arithmetic.

---

## §13.8 The shape census, across everything surveyed

| shape | where it appears in the precedent | where it appears in Valoria |
|---|---|---|
| **GATE** | **Dominant.** CK levies and MAA, Shogun 2's building chains, JA2's defection, EU4's Loyalty-vs-Influence revocation, RoTK's order floors, TK's class gating | Rare — a few flag checks; **not used for recruitment, which the genre gates** |
| **U** | RoTK's domestic commands (a stat-scaled effect, no contest) | **Dominant** — five of seven obstacle-bearing production rolls |
| **SO** | Victoria 3's enactment (**with a feedback term on the obstacle**) | Three sites, all reading a stat the attempt does not move |
| **DO** | Kremlin's influence contest; most board-game bidding | The Persuasion Track; the emergency council — **whose two sides derive from the same faction** |
| **BI** | **Burning Wheel alone**, and only because of the compromise rule | The catalogue's Negotiate Quota and a handful of designed-only rows |
| **view** | JA2 v1.13, Shogun 2 bands, Victoria 3's shown odds | **No representation, and no slice to hold it** |

**Four readings.**

1. **The genre gates far more than Valoria does.** Where a franchise wants a *budget decision*, it uses
   a threshold; Valoria reaches for the kernel. That is a defensible choice made by default rather
   than deliberately, and it is most visible at Muster.
2. **`SO` with a feedback term is the shape Valoria is missing**, and it is the one the survey rates
   highest — a measure that makes its own opposition.
3. **`BI` is one rule away from `DO`**, and that rule is Burning Wheel's compromise. Valoria's contest
   resolver could acquire the shape for the price of scaling a payoff.
4. **`view` has no home**, which is why the cheapest and highest-value import in the whole companion
   currently has to be filed as documentation.
