# 10 — The Resolution Surface

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: cross-cutting · Composes on: `01_substrate.md` (binding, unmodified)
## Method: derived, not adapted. No prior dice engine, obstacle rule, or degree ladder constrains it.

**What this document owns.** The substrate fixed three signatures and refused a fourth possibility outright: `choose(person, view) -> act`, `resolve(act, world) -> event`, `witness(person, event) -> claim`. Nothing here adds a fourth function. This document specifies **what `resolve` does at the instant an act's outcome is uncertain** — the one place in the whole design where a random number is drawn. Two functions live here, and every other document in the suite calls them rather than inventing their own: `roll(pool) -> successes` and `obstacle(context) -> target`. If a mass-battle document, a social-contest document, or a field-investigation document ever computes a probability without routing through these two, this document has failed at its one job.

**Why a resolver has to exist at all, stated plainly.** A tabletop GM does five things nobody wrote down as rules: sets a difficulty on the spot, decides when a tie is dramatic instead of null, decides whether the mismatch in front of them is worth a full scene or a single line, decides what a middling result *means*, and quietly nudges an outcome when the dice would otherwise wreck the story. There is no GM. Every one of those five jobs is either mechanized below or explicitly abolished (the fifth — narrative nudging — is abolished outright: the resolver never sees the story, only the pool and the obstacle, by the same discipline that keeps `resolve` from taking an agent argument).

---

## 1. The core roll

### 1.1 The die and why it is shaped this way

Every attempt rolls **N ten-sided dice.** A die showing 1–6 scores nothing. A die showing 7, 8 or 9 scores **one success**. A die showing 10 scores **two successes.**

Per-die: P(0) = 0.6, P(1) = 0.3, P(2) = 0.1. Mean = 0.5 successes/die, variance = 0.45, σ ≈ 0.671.

**Why a pool, not a target-number-plus-modifier system (d20+mod vs. DC, 2d6+mod vs. a fixed number).** A DC system requires someone, at the table, to *decide* a difficulty out of judgment. That someone is the GM this game does not have. A dice pool sidesteps the decision entirely: both the actor's side and the opposing side are expressed in the *same unit* — small integers already sitting on the person/object schema (§2) — so a target number can be *computed*, never *assigned*. That is the entire reason this document reaches for a pool shape rather than any other: it is the only shape where "how hard is this" is arithmetic over things that already exist in the world, not an authored number.

**Why the double-success 10, rather than the classical flat threshold.** Doubling the top face keeps the mean at exactly `Pool ÷ 2` — a number a player computes in their head — while still giving the distribution a right tail fat enough that the top degree band (§3) is reachable at *every* realistic pool size, not just large ones (verified below). This is the design erring, on purpose, toward **legibility over depth**. The corpus records that no shipped game in this domain found a formula-legible system critics also called deep. Given that choice, this design takes legible: the resolver is the one surface in the whole game that must never be foggy, because everything sitting on top of it — belief, rumour, motivated reasoning, an epistemic barrier that is *inaccessible* by canon (P-08) — is foggy by design. If the dice were also illegible, the player would have no fixed ground to read the deliberate fog from. Depth here comes from the obstacle derivation (§2) and the manoeuvre layer (§5), not from opacity in the roll itself.

### 1.2 Pool assembly (what I own, given Capability)

Document 02 supplies **Capability**: a set of Practices, each paired to a relevant Attribute. This document owns the arithmetic that turns that into a die count:

```
Pool(person, practice) = Attribute[relevant](person) + Practice[practice](person)
```

Attribute ranges 1–7 (the nine named in the setting — Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds — plus the ruled-but-unnamed tenth, which composes identically whatever it turns out to be, since this formula never inspects an attribute's name). Practice ranges 0–7, where 0 is "never trained" — an untrained attempt is always legal (T1: a person with no office, and no training, can still try), it is just a small pool. Realistic Pool therefore runs **1–14.**

### 1.3 The probability table

| Pool | Mean successes | σ |
|---|---|---|
| 3 | 1.5 | 1.16 |
| 4 | 2.0 | 1.34 |
| 6 | 3.0 | 1.64 |
| 8 | 4.0 | 1.90 |
| 10 | 5.0 | 2.12 |
| 12 | 6.0 | 2.32 |
| 14 | 7.0 | 2.51 |

Full distribution at Pool 8 (the "competent, ordinary adult" case), for legibility:

| Successes | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8+ |
|---|---|---|---|---|---|---|---|---|---|
| P | 1.7% | 6.7% | 14.0% | 19.6% | 20.4% | 16.7% | 11.0% | 5.9% | 4.0% |

**Closed loop.** `roll(pool)` — produced by `resolve` whenever an act's outcome is uncertain; carried as a plain integer (successes) inside the event `resolve` is about to construct; consumed immediately by `obstacle`'s margin calculation (§3) and nowhere else — it is never stored on the person.
**N-line.** Cut the pool roll and every uncertain act becomes deterministic — a person with the bigger Capability number always wins, always, which collapses the entire "even the skilled can fail, even the unskilled can succeed" texture the corpus and the setting both depend on (Greta's salt run only matters because it could have gone the other way).

---

## 2. The obstacle, with one owner

### 2.1 The derivation

Doc01's single structural fact — **there is exactly one kind of actor, a person** — is also the fact that decides how difficulty works. Something that isn't a person cannot *try harder*. It has one performance, fixed at the moment of the attempt. A person can. That single distinction is the whole of "one owner":

```
obstacle(context):
    if context.opponent is a person:
        return OPPOSED    # go to §4 — both sides roll, live
    R = resistance_pool(context)          # dice-equivalents of whatever resists
    if R <= 1:
        return 0          # uncontested — no roll, automatic Clean Success
    return round_half_up(R / 2)
```

`resistance_pool(context)` is *always* a dice-equivalent — a lock's fineness, a wall's sheerness, a cliff's grade, a document's forgery quality — expressed in the identical unit Capability is expressed in. This is the second half of "one owner": not just one function, but **one unit**, used for everything that ever resists an act, so nothing needs a bespoke difficulty currency invented per scene. A GM would have improvised a DC. This design instead asks "what, concretely, resists this, and how many dice would it roll if it were a person" — and if the honest answer is "it wouldn't roll at all, it just sits there," it gets the deterministic form above instead. **The obstacle formula is not a different idea from the roll — it is the roll's own expected value**, `E[roll(ResistancePool)]`, used deterministically because the resisting thing has no agency to vary.

**Rounding.** Half rounds up: R=5 → Obstacle 3. **Floor.** R≤1 skips the roll entirely — most of a headless world's background acts (a person eating breakfast, a scribe copying a routine letter) never reach a die, which matters when thousands of persons are ticking at once (T8). **Ceiling.** If Obstacle > 2×Pool (the actor's mathematically maximum possible successes — every die a 10), the attempt is not merely unlikely, it is *impossible*, and the resolver refuses to roll it at all. The act must change under a manoeuvre (§5) — reframe the pool source, seek aid, contest a different obstacle — or it does not happen. This is the discipline named in §4 for mismatched contests, applied here to the unopposed case: the engine does not spend a die roll pretending an impossible thing might happen.

### 2.2 Worked institutional case — the Masterpiece Examination

The examination committee is a **community's judging set** (doc01 §4). Its obstacle is never a stored "caste penalty" — doc01 explicitly refuses a faction-wide reputation scalar, and this resolver honours that refusal by construction: `resistance_pool` for an admission act is computed **on demand**, from the *individual* stances of the sitting masters toward the candidate's marks (heritage, guild grade), summed. A Southern Einhir candidate before a panel with three masters whose stance toward "Southern Einhir" runs cold contributes a *larger* resistance pool than the identical candidate before a panel that doesn't; nothing is stored, nothing is a caste number — it is masters, being asked, right now, what they think of this specific person. Change the masters (a schism, a retirement, a bribe) and the number changes with no edit anywhere.

---

## 3. Degrees of outcome

Margin = successes − Obstacle. Bands are derived from margin directly, in the same unit successes are already counted in — no rescaling needed, because Obstacle is already commensurate with successes by construction (§2):

| Margin | Band |
|---|---|
| ≤ −2 | **Disaster** |
| −1 | **Failure** |
| 0 | **Costed Success** |
| +1, +2 | **Clean Success** |
| ≥ +3 | **Overwhelming** |

**Costed Success is the deliberate middle band** — you meet the obstacle exactly, and something is given up for it (a complication attaches; Greta gets the salt through *and* a Knight files a claim). The brief's own warning applies here: a consequence gated to a middle band is fragile if that band is rarely reached. It is not, here:

| Pool vs Obstacle | Disaster | Failure | Costed | Clean | Overwhelming |
|---|---|---|---|---|---|
| 4 vs 2 (balanced) | 13.0% | 25.9% | 28.1% | 28.9% | 4.2% |
| 8 vs 4 (balanced) | 22.4% | 19.6% | 20.4% | 27.6% | 10.0% |
| 12 vs 6 (balanced) | 27.1% | 16.4% | 16.8% | 25.5% | 14.3% |
| 8 vs 2 (favoured) | 1.7% | 6.7% | 14.0% | 40.0% | 37.6% |
| 6 vs 5 (outmatched) | 64.2% | 18.0% | 10.6% | 6.6% | 0.6% |

Every band is reachable — non-trivially so — across the entire realistic range. Costed Success alone runs 14–28% in every row.

**The failure test, run properly.** A band that a system is tuned never to reach is indistinguishable from a band that does not exist (the EU4-estates refusal). Check the extreme, not the average: a master (Pool 14) attempting something almost trivial (Obstacle 2) still carries **0.08% Disaster** — genuinely reachable, not a special-cased floor, because it falls out of the *same* binomial that produces every other row, not a hand-authored exception. Push further, to Pool 20 vs Obstacle 3: Disaster is still 0.04%, never zero. The only way Disaster becomes *literally* impossible is the §2 ceiling case in reverse — when the attempt is trivial enough that the resolver never rolled at all (Obstacle ≤ 1). Below that line, the game has already decided nothing is at stake; above it, the failure state is always live, at whatever vanishing probability the pools actually produce, never a floor bolted on top of the math.

**Closed loop.** Band — produced by `resolve` immediately after `roll`; carried as one field on the `event`; consumed by whichever consequence table the act declared (§5's "escalate the stake" manoeuvre is precisely a player choosing which consequence table attaches to which band, before the roll).
**N-line.** Cut degree bands and every act becomes binary pass/fail — Costed Success (the injury of succeeding at a cost, the actual texture of Greta's salt run) becomes inexpressible, and Overwhelming (the thing that makes a master's mastery *feel* like something) collapses into ordinary success.

---

## 4. Opposed contests

### 4.1 Same function, live on both sides

An opposed contest is what `obstacle` returns `OPPOSED` for: **both sides call `roll`, live**, because both sides are persons and only persons vary their performance. Margin = successes_A − successes_B, banded exactly as in §3, read from A's perspective (B reads the mirror). This is not a second resolver — it is the identical `roll` function called twice instead of once, with the second call's *expected value* (§2's deterministic Obstacle) replaced by an actual draw because there is now someone on the other side capable of having a good day.

### 4.2 When it isn't close

| A vs B | A wins (Clean+Overwhelming) | B wins (A's Failure+Disaster) |
|---|---|---|
| 8 vs 8 | 42.6% | 42.6% |
| 10 vs 8 | 56.8% | 29.9% |
| 10 vs 6 | 71.1% | 17.5% |
| 12 vs 6 | 80.8% | 10.7% |
| 12 vs 4 | 90.8% | 4.2% |
| 14 vs 4 | 94.8% | 2.2% |

Past a gap of roughly **6** (on this design's 1–14 scale — nearly half the practical range), the underdog's win chance falls under ~11% and keeps collapsing. This is the corpus's warning realized exactly: at a large enough pool gap, the manoeuvre layer cannot manufacture chances the dice don't support. **The honest response is not to hide the mismatch behind a menu that pretends to matter — it is to publish it.** Before any die is drawn, the resolver exposes the same inputs a player would need to compute the table above (both pool sizes, the obstacle interpretation, nothing else) — the corpus's *view-slice* discipline, adopted whole: publish every input, publish the resulting band probabilities, never publish a hidden trigger point. A hamlet fisher can still *attempt* to out-argue a Cardinal on doctrine — T1 never revokes the right to try — but the game will not dress up a 3-vs-14 roll as a rich tactical scene.

The one manoeuvre that is never decorative at a large gap is the one that **changes which obstacle you're rolling against** (§5.2): the fisher doesn't win the doctrinal argument, he routes it — contests jurisdiction, or converts a private grievance into a backed petition (doc01 §5.1), which is not a dice contest at all. That is the correct shape of "what the system does when a contest is not close": it points the player at a *different primitive*, not a bigger number.

**Closed loop.** The opposed roll — produced by two simultaneous `roll` calls inside one `resolve`; carried as a signed margin; consumed by the band table for both participants, and by `witness` twice, independently, per doc01 §3.3 (a contest has two losers' and two winners' *accounts* of it, not one).
**N-line.** Cut opposed contests as their own case and every person-vs-person conflict must be laundered through a fake static obstacle for one side — which is a lie about who that side is (a person, who might have had a bad day) and destroys the case where the underdog *does* pull off the 17.5%.

---

## 5. What a player chooses

At the point of declaration — before `roll` is called — the acting person (player or, via `choose`, an NPC) may attach one or more of the following to the act. Each is checked against the refusal that a manoeuvre must **alter a primitive**, never apply a formula:

**5.1 Reframe the pool source.** Choose which Attribute+Practice pairing the attempt draws from (persuade through Charisma+Rhetoric, or through Strength+Intimidation). This changes *which number is your pool*, not a bonus added to it. Free, no resource cost — it is pure tactical reading of the situation, and it interacts with marks (a Southern Einhir target's stance toward Intimidation-from-a-Templar is not the same as their stance toward Rhetoric-from-a-neighbour).

**5.2 Contest the venue, not the fight.** Deny the act happened; deny the label; admit-and-justify; challenge the jurisdiction. Each redirects the attempt to a **different obstacle entirely** — a different judging set, a different rung, a different resistance pool — which is a change to which function inputs get used, not a modifier on the current ones. This is the manoeuvre that survives a large pool gap (§4.2).

**5.3 Escalate the stake.** Before rolling, commit to needing Clean Success or better; a Costed Success now counts as Failure. In exchange, the consequence table attached to Overwhelming is swapped for a larger, durable one. This changes the **consequence mapping**, a primitive, and is symmetric: the downside scales with the upside at declaration time, so there is no repeated-use dominance question — it is a single-instance bet, not a resource that accumulates advantage over sessions.

**5.4 Draw aid from a Knot.** A bonded partner contributes real dice, **sourced from their own relevant Attribute+Practice** — never a flat number (§6) — at a cost of +1 Strain to the Knot. **Dominance check, run honestly:** the gain here is flat per use (one small pool's worth of dice, once), while the cost compounds toward Rupture (+5 Strain). That is structurally the same shape the brief names as broken (decaying/flat gain against compounding cost) — *unless* the cost path is genuinely self-limiting, which it is: Rupture removes the option entirely (the Knot is gone, along with a Coherence hit and, for a Close Knot, a Conviction scar), so heavy repeated use does not stay profitable indefinitely, it **consumes the resource that made it possible.** Strain decays −1/season under sustained investment, so light, spaced use is sustainable; leaning on one Knot every scene is not. The fork is not broken because neither branch is free forever — one branch just runs out.

**Closed loop.** A manoeuvre declaration — produced by `choose` (player or NPC, identically); carried as fields on the `act` object doc01 already defines (pool_source, obstacle_target, stake_band, aid_from); consumed by `resolve` before it calls `roll`.
**N-line.** Cut manoeuvres and every roll becomes "declare intent, roll the default pool" — which satisfies R for nobody: there would be no choice left that changes anything about *how* the attempt is made, only whether it is made at all.

---

## 6. No flat modifiers from persons

**The arithmetic, derived fresh for this die, and this document owns the constant.** Per-die variance is 0.45, so σ(Pool) = √(0.45·Pool) ≈ 0.671·√Pool. **0.671 is the constant for this die**; docs 09 and 12 price flat shifts against it and cite here rather than deriving their own. A flat shift of X successes is therefore worth `X / (0.671·√Pool)` in standardized terms — **inversely proportional to √Pool.** A flat +2 that is a rounding error against a Pool-14 master is a third of a small Pool-4 apprentice's entire expected output. Applied to persons specifically: a leader who grants a flat bonus to whoever they're helping is worth *more* to whoever needs it least well, systematically, by construction — the exact backwards-from-intent failure the corpus names.

**What survives this rule, audited against every source of influence in this document:**

- **Aid (§5.4)** survives because it is *sourced* — an actual second small pool, generated by the helper's own Attribute+Practice and merged into the roll, not an arithmetic addition to the result. Its size still shrinks in *relative* importance as the recipient's own pool grows (a smuggler cousin's boat matters enormously to Greta's Pool-7 attempt and would be nearly invisible bolted onto a Pool-14 master smuggler's), which is the correct direction — the aid is genuinely worth what it is worth, not artificially inflated for the weak.
- **Marks (§2.2)** survive because they change *eligibility and obstacle composition* (which pool sources are open to you; how large the resistance pool a judging set produces is) — never a flat penalty subtracted from a roll's result.
- **A leader affecting a group** (relevant wherever this document's `roll`/`obstacle` pair is reused at settlement or faction scale) is **not owned here. Doc 09 §6 owns it, and this document defers to it in full.** An earlier draft of this bullet licensed a second form — `ΔPool_group = round(f × Pool_group_base)` with `f` set "by the leader's own rating" — and that form is **withdrawn**, for two reasons. It was a third leader formula in a suite that already had two, in a document whose own §9 says a second resolver anywhere means it has failed at its one job; and it required a *leader rating*, a stored personal scalar that doc 02 and doc 09 both refuse — doc 09 derives the leader's weight from `Φ(C)·share(P,C)`, which is composed out of the command graph, concord and supply rather than out of a number on the man. The live rule is doc 09 §6's: a leader (a) adds their practices to the collective's option set for the exchange, and (b) on the fraction `φ = Φ(C)·share(P,C)` of the collective's weight, that weight's roll draws the named attribute **from the leader instead of the collective's own mean**; the remaining `1−φ` rolls its own. No addend, and no third thing.

Nothing in this design's modifier vocabulary is a bare number added to a result. Every one of them is either a real, second, sourced pool, or a change to which pool or which obstacle applies.

---

## 7. Randomness, determinism, and replay

**Seeding.** Every attempt gets a substream keyed off its own identity, never a shared sequential draw counter: `substream = hash(world_seed, actor_id, act_type, target_id, tick, sequence)`. `roll(pool)` advances exactly `pool` steps within its own substream and nowhere else.

**Guaranteed invariants, and how each is checked:**

1. **Reproducibility.** Same `world_seed` + same act log, replayed → identical events. Checked by hashing the full event log across two runs from the same seed and asserting equality.
2. **Order-independence.** Two causally-unrelated attempts, resolved in either order (or in parallel, since substreams don't share state), produce the same per-attempt outcome. Checked by shuffling a batch's resolution order and diffing outcomes keyed by `attempt_id` — they must be bit-identical.
3. **Preview-transparency.** Computing the odds table a player sees before committing (§4.2's published inputs) reads `pool` and `obstacle` and evaluates the binomial *analytically* — it never calls `roll`. Checked by asserting the substream's position is unchanged after any preview query. This is what makes "showing the player a possibility" safe: looking at the odds cannot consume the die that later determines the outcome.
4. **Fidelity-invariance.** The identical `attempt_id`, given identical resolved inputs, produces the identical dice regardless of who declared the manoeuvre or whether the result is rendered. There is exactly one probability law, sampled by exactly one function — never a fast "auto formula" approximating a slow "played" process that can drift out of calibration on its own (the failure the corpus records twenty years of complaints about). Checked by resolving the same `attempt_id` once with a human-supplied manoeuvre and once with `choose`-supplied defaults, holding pool and obstacle equal, and confirming identical dice.

**Closed loop.** The substream — produced once per `attempt_id`, never reused; carried nowhere (recomputed from the id every time it's needed); consumed exactly once, inside `resolve`, by the `roll` call(s) that attempt authorizes.
**N-line.** Cut keyed substreams for a single shared draw stream and the engine loses order-independence outright — two field investigators auditing the same ledger in a different tick order would get different worlds, which breaks the headless-and-reproducible requirement this whole engine exists to satisfy.

---

## 8. The setting's own resolution content

### 8.1 Thread Sensitivity and the Thread Pool — **kept**

`Thread Pool = floor(TS / 10)`. This is a **second pool on the same person, drawn through the identical `roll` function** — not a second resolver. A Thread-act simply sources its dice from Thread Pool instead of Attribute+Practice; everything in §1–§4 applies unchanged.

**N-line.** Cut it and P-03's core mechanic — information asymmetry between sensitive and non-sensitive as *the* mechanic, not a modifier on it — has no resolver-legible cost. Without a distinct, TS-derived pool, a sensitive and a non-sensitive attempting the same Thread-adjacent act would be indistinguishable in the one place (the dice) where the game actually decides anything.
**Closed loop.** Produced from TS (itself set by doc02); carried as a person field; consumed by `roll` whenever an act's declared pool_source is Thread rather than Attribute+Practice.

### 8.3 Coherence bands — **kept, with the reachability check run**

Coherence counts down 10→0. Bands: 10 Whole (no penalty); 9–7 Dissonant (−1 die on Thread rolls); 6–4 Fragmented (−2 dice, some Thread ops closed); 3–1 Fractured (−3 dice, Composure halved); 0 Severed (Thread Pool locked to zero). Coherence is never itself rolled — it resizes the Thread Pool by a fraction/step per band, the same sourced-not-flat discipline as §6.

**Accrual:** every Thread attempt costs −1 drift (P-01: every op moves all three dimensions, nothing is free); a contested Thread op costs −2. **Mitigation:** a grounding act restores Coherence, capped at `min(2, ⌈Will/3⌉)` per season. **The test, run at the extremes:** a heavy user attempting three ordinary Thread ops a season accrues −3/season minimum against a *maximum* mitigation of +2/season even at high Will — net −1/season, reaching Severed in **ten seasons — two and a half years**, not the "roughly a decade" an earlier draft of this sentence claimed by silently reading seasons as years (this world runs four seasons to the year), and far faster (2–3 seasons) under contested-op-heavy play. The corrected figure makes the check *stronger*, not weaker: Severed is not a distant asymptote a career never reaches, it is inside the span of a single campaign for anyone who uses the Thread routinely. Severed is reachable, not an asymptote nobody hits — the failure state exists because the accrual rate genuinely outruns the best available maintenance under real pressure, not because a number was tuned to look scary and never fire.

**N-line.** Cut Coherence and Thread-sensitive play has no cost axis at all — a sensitive could act on the Southern layer arbitrarily with no accruing risk, deleting the central tension of playing one, and P-12's relational propagation-through-Knots has nothing to propagate.
**Closed loop.** Produced by Thread-attempt resolution (drift) and by grounding acts (recovery); carried on the person; consumed by every subsequent Thread-pool sizing and, per P-12, by Knot-strain propagation to bonded partners.

### 8.4 Composure — **kept, narrowly**

A per-scene resource depleted by the *margin of loss* in each losing exchange of an opposed social contest (§4); at 0, the person must concede or take a Disposition/Coherence hit. Resets between distinct contests — it is not a permanent stat, and deliberately not a compounding punishment carried across the whole game.

**N-line.** *(Corrected — the original claimed the exchange loop's work as Composure's own.)* It read *"cut it and every opposed social contest collapses to one roll with no attrition — a skilled arguer instantly demolishes anyone regardless of resolve, and there is no mechanical difference between a jab and a sustained interrogation."* The multi-exchange structure is **not** Composure's and survives the cut: doc 08 §8.3 owns the exchange loop — alternating `propose`/`counter`/`press`/`probe`/`withdraw` acts against a venue-set budget — and it has its own three terminal conditions, **a named fault** (F1–F5, close or strike), **a `withdraw`**, and **the budget lapsing**. Delete Composure and a jab is still one exchange while a sustained interrogation is a dozen, differing in faults armed, claims deposited and record rows written; nothing collapses to one roll. What actually dies is **attrition to concession**: the accumulated *margin of loss* making the person, rather than the clock or the record, the thing that gives way — and with it the "press on or disengage" fork, which is the R loss and is the whole of what this object is kept for.
**Closed loop.** Produced by losing margins inside §4's opposed-contest resolution; carried per-scene, non-persistent; consumed by the concede/break check at 0, and by Close-Knot strain-buffering (SETTING's own listed trigger) when a bonded partner spends *their* Composure to shield yours.

---

## 9. What is refused, under E-as-a-ratio

- **A second resolver of any kind — the strongest refusal in the corpus.** There is one `roll`, one `obstacle`. Thread acts, physical acts, social contests, and (should another document reuse this surface at settlement or faction scale) mass-action checks all draw from the same two functions with different pool sources. No combat-specific dice mechanic, no separate social-combat engine, no per-domain variant of the opposed contest.
- **Critical-hit tables.** Degree bands (§3) already produce a graduated, margin-derived "how good was this." A separate crit table would be a second, uncorrelated source of the same judgment, competing with margin for the same job.
- **Per-skill subsystems.** A Practice is a number that feeds a pool. No lockpicking minigame, no called-shot sub-resolver beyond the manoeuvre vocabulary in §5 — a manoeuvre is domain-blind by construction.
- **A confidence cap on the roll itself, or on how far a manoeuvre can move it.** Correction, per doc01 §3.2, is by collision, not by ceiling; the same principle that keeps belief uncapped keeps this resolver's outputs uncapped.
- **Exploding/open-ended dice.** A reroll-on-10 chain makes the number of draws per pool variable, which complicates the fixed substream-stepping (§7) an engine resolving thousands of AUTO attempts per world-tick depends on for O(1)-per-attempt cost. The double-success 10 gets the same reachable-top-band effect with a bounded, deterministic draw count.
- **A separate "auto-resolve formula."** Named explicitly in §7: there is one probability law, one function, sampled identically at every fidelity. Building a faster approximation for the strategic layer is exactly the twenty-year-unsolved defect the corpus documents.
- **Momentum — CUT, and this entry is a retraction, not a tidy-up.** Earlier drafts of this document kept Momentum twice: as manoeuvre §5.5 and as §8.2, where it was marked **kept**. Both are gone, and §8's numbering keeps the gap where §8.2 was so that a reader meeting the old text elsewhere can see it was removed rather than renamed. Three reasons, in ascending order of force. (i) Its N-line was false. It claimed to be "the only mechanical account of how the Restoration produces outcomes" and that without it "playing to your values becomes pure flavour text" — but a Conviction **is** a stance row (adjudication B-8), and stance rows already gate the willingness function, a negotiator's option set, concord, and view salience. Convictions keep full resolver consequence with Momentum deleted; nothing about playing to your values became flavour. (ii) Its residue was `+1 die` — a flat pool bonus, which is the one shape §6 of this very document refuses, and which doc 02's opening charter names as "the one shape that cannot produce a politics." A sourced-die defence does not rescue it: the die was sourced from an abstraction, not from a second person's Attribute+Practice. (iii) It was produced by "scene-level detection" and reset "per session" — and neither a scene nor a session exists at AUTO fidelity. That makes it a pool term available to a played person and unavailable to the identical person resolved headless, which is a direct breach of §7's fidelity-invariance guarantee, the guarantee this document exists to make. **Two independent auditors reached the cut separately**, without sight of each other's findings, which is the strongest signal this process produces. Nothing replaces it.

---

## 10. One attempt, three fidelities

Take doc01's own trace: Greta, Pool 7 (Agility 4 + Wayfinding/Stealth 3), against the Knight of the Peace on checkpoint duty, Pool 7 (Acuity 4 + Vigilance 3) — a person, so this is an opposed contest (§4), gap 0, well inside manoeuvre-rich territory.

**One `attempt_id`, one substream.** Say it yields Greta 5 successes, the Knight 4. Margin +1 → **Clean Success** for Greta.

- **Played.** The player controls Greta directly. They see both pools before committing, choose the pool-source reframe (§5.1 — run it through Agility+Stealth, or through Charisma+Bearing and talk her way past), watch the dice, see the margin and band resolve live.
- **Witnessed.** The player controls someone else nearby — a neighbour glimpsing the run. `choose` supplies Greta's manoeuvre declaration (her own reframe, decided by her own decision function, not a human at this table). The *identical* substream produces the *identical* dice. The player sees one line: "Greta slips past the checkpoint." No dice, no menu — but it is not a different formula, it is the same `resolve` call with the render truncated.
- **Auto.** This happens during a world-tick the player isn't present for at all — one petition among thousands the headless engine is resolving in bulk. `choose` again supplies Greta's declaration; `resolve` runs identically; nothing is displayed until, weeks later, its downstream event (the Knight's claim, her neighbours' claim, per doc01 §3.3) surfaces in someone's ledger.

All three are one `resolve` call. The only variable across them is **who supplied the manoeuvre** — a human or `choose` — **and whether the result is rendered.** The dice, the pool, the obstacle, and the bands never change shape. That is the whole answer to the corpus's hardest warning about this exact seam: there is no fast formula quietly approximating a slow process. There is one process, and fidelity is a camera, not a second engine.
