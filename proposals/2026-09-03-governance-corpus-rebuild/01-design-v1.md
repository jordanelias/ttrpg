# Valoria — The Governance Corpus, Rebuilt

**A conceptual design pass over 33 documents (810,408 bytes · ~115,000 words), read as the
specification for a videogame with no GM.**

---

## What this is

Thirty-three design documents were read in full, sorted into sets, flattened, decomposed into
primitives, derivatives, pipelines and throughlines, compared, and rebuilt from the bottom up into a
single state graph and an architecture.

**This is a design document, not an audit.** Where the corpus said one thing twice, it has been
unified. Where it said two incompatible things, a decision has been taken and recorded in one line
(§ Reconciliations) rather than argued at length. Where it was silent, a choice has been made and
marked as a choice. The corpus's own defect registers — and it contains two large ones — have been
mined for their content and then set aside; they are the previous pass's work, not this one's.

The posture throughout is that **every mechanic in this corpus was there for a reason**, and that the
reason survives even where the mechanism is replaced. Most of what follows is not new design. It is
the design that is already in these documents, stated once instead of three times.

## Sources

The thirty-three uploaded documents, and nothing else. Where a document cites something that is not in
the upload, that citation is treated as unresolvable and the rule is reconstructed from what the
corpus itself says about it — which, for the two most load-bearing absences (the victory document and
the geography data), proved sufficient.

## Method

| stage | what it did |
|---|---|
| **Read** | All 33 documents in full, twice, by two independent readers with different questions. |
| **Sort** | Two independent groupings — one by reading (14 sets, membership criteria stated, multi-membership expected), one measured (tf-idf cosine over domain vocabulary). Compared in § The sets. |
| **Flatten** | Per set: duplicate statements collapsed to one, contradictions surfaced as decisions, gaps named. |
| **Decompose** | Per set: primitives (irreducible stored state, with owner and write path), derivatives (with the composition rule as an expression), pipelines (as state machines with evaluable predicates), throughlines (invariants). |
| **Compare** | Set against set; reading against measurement; each reader against the other. |
| **Rebuild** | State graphs bottom-up per set, then unified into one tick and one composition order. |
| **Design** | The architecture the unified graph implies, and the boundary between mechanism and content. |

Formulas, thresholds and band edges are reproduced **verbatim** wherever they are quoted, including
their original glyphs. Where this document states a number the corpus does not, it says so.

## The annexes

This document is the argument. Three annexes carry the exhaustive working, and each stands alone:

- **Annex A — Decomposition.** All 33 documents sorted into fourteen overlapping sets with stated
  membership criteria, each set flattened, then decomposed into **318 primitives, 293 derivatives,
  129 pipelines and 18 throughlines**, alongside 79 indexed contradictions, 37 specification holes
  where a human referee is required, and 196 set-local gaps. Formulas verbatim; contradictions
  preserved and marked rather than reconciled — this annex is what Part III's decisions were taken
  against.
- **Annex B — State graphs and the executable model.** The corpus rebuilt as twelve sets of typed
  state — 113 primitives, 153 derivatives, 57 pipelines, 24 core types — each set with a graph
  diagram, single-writer primitives, derivatives as expressions and pipelines with machine-evaluable
  predicates; then the twelve-phase tick, the scale-composition rules, the conservation properties,
  and the full code shape with worked examples. **◆** marks each of the 105 decisions the corpus did
  not make. Its §3.3 is the shortest useful summary of the whole exercise: twenty-two places where
  the corpus's graphs were fighting, and the resolution taken for each.
- **Annex C — Gaps and numbers.** Thirty entries naming, for each non-executable rule, the *specific
  missing decision* — the design agenda Annex B answers; plus 362 verbatim numeric constants,
  thresholds and formulas, preserved because a paraphrase destroys them.

## The shortest version

The corpus is one idea implemented three times at three scales, plus a resolution kernel and a
cross-scale propagation mechanism that it invented late and never connected to the rest.

- **The idea:** authority is never held, only accepted; it is contested from above by a tier issuing
  demands and from below by a constituency withholding consent; acceptance aggregates upward and
  reverts downward. Settlement, province and peninsula are three instances of this, built
  independently, sharing no primitive.
- **The kernel:** a deterministic-plus-stochastic resolver producing a four-degree outcome, with
  dice retained where variance is healthy and abolished where it was corroding irreversible
  decisions. Already ratified in the corpus; migration roughly a third complete.
- **The propagation:** Domain Echo — a degree-derived, scope-gated, clamped magnitude applied at a
  single commit phase, in which no subsystem names another. Already correct; already absorbed a whole
  new scale without amendment.

Build the acceptance primitive once, the pressure primitive once, and the pipeline primitive once;
give every quantity exactly one owner; and the thirteen subsystems become five mechanisms and a great
deal of authored content.

---

# Part I — The design

## One idea, implemented three times

Read across all thirty-three documents, the corpus is not thirteen mechanics. It is **one mechanic,
built independently at three scales, by three different hands, with no shared primitive.**

The idea is this: **authority is never held, only accepted — and it is contested from above and
below at the same time.** Every scale in Valoria has a tier above it issuing demands and a
constituency below it withholding consent, and the thing that mediates them is a quantity of
acceptance that flows *up* as legitimacy and reverts *down* as pressure to conform.

The corpus states this three times without noticing it is the same statement:

| scale | the tier above | the constituency below | the acceptance quantity | the pressure quantity |
|---|---|---|---|---|
| **Settlement** | the Provincial Authority's **Directive** — comply, bargain, or defy | **Local Actors and Needs** — petitions, famine, charters, grudges | **L / PS** (Legitimacy, Popular Support), 0–7 each, per settlement | **Π**, 0–10, the deck's draw rate |
| **Province** | the duchy and the parliamentary map | its **1–3 settlements**, which may be held by rivals | **Accord** = `floor(mean settlement Order)` | **fragmentation checks**, fired per Accounting on misalignment |
| **Peninsula** | nothing — this is the top | the **provinces and the institutions** (Parliament, Church, Ministry, Guilds) | **Mandate** = size-weighted saturating aggregate of settlement L/PS | **CI · IP · MS · PI · Strain** — five clocks |

The corpus even names the pattern once, at `conflict_architecture_proposal.md` › The Three Scales:

> "Control flows **upward** (win settlements → hold provinces → control the peninsula). Pressure
> flows **downward** (peninsula events → province consequences → settlement disruption). This
> bidirectional flow makes the game self-sustaining — structural misalignment at any scale propagates
> to the others."

That sentence is the whole design. Everything difficult in the corpus follows from the fact that it
was then built three separate times.

## What the triplication cost

Because acceptance was implemented three times, it acquired three incompatible shapes:

- **L/PS** are per-settlement, 0–7, with an explicit mean-reverting feedback from Mandate and a
  weighted saturating aggregation `Mandate = clamp(round(7·T/(T+K)), 0, 7)`, `K = 6`, over
  `W_s = base(Type) + Prosperity_s + FacilityTier_s`. It is the most carefully specified quantity in
  the corpus.
- **Accord** is `floor(mean settlement Order)` — but **Order is a different stat from L/PS**, defined
  as "civil compliance" rather than political acceptance, and it is the only one of the three that
  aggregates by a plain mean with no weighting, no saturation and no feedback.
- **Mandate** is derived from L/PS at one place and written *directly* at others (parliamentary
  transfer and mass seizure set control without touching settlement Order), so the aggregate and its
  inputs can disagree with no rule to reconcile them.

Three implementations of one idea also produced three *pressure* models: a well-formed homeostat at
settlement scale (Π, with anti-stall and anti-runaway both explicit), a bare per-Accounting die roll
at province scale (the fragmentation check), and five uncoordinated global counters at peninsula
scale, one of which (MS) is a shared-loss condition and the rest of which are not.

**The redesign is therefore not thirteen redesigns. It is one: build the acceptance primitive once
and the pressure primitive once, parameterised by scale, and let the three tiers be three
instantiations rather than three systems.**

## The three ideas worth keeping exactly as they are

Most of the corpus's mechanics are replaceable. Three are not, and any rebuild should preserve them
in substance:

**1. The two-stroke churn** (`governance_play_redesign_v1.md` › Part 4). Each season the world moves
on the player and the player moves on the world, and *each stroke writes the preconditions of the
other*. The guarantee is stated sharply — the world always acts (the Directive is mandatory and the
deck always draws at least one card), and the player always acts (every verb emits a world-delta).
This is what makes the game a loop rather than a state display, and it generalises to every scale.

**2. Method choice as the site of politics** (`governance_play_redesign_v1.md` › §1.3). The eight
governance verbs are deliberately *not* orthogonal stat pumps: `Develop` must choose Treasury,
Guild charter or Corvée; `Fortify` must choose Garrison, Militia or Walls; `Keep Order` must choose
Consent, Force or Clergy. Each choice raises the same number and hands power to a different faction.
**The tradeoff is not "which stat" but "whom do you owe".** That is the single best mechanical idea in
the corpus and it is stated in one document, at one scale. It should be the shape of every action in
the game.

**3. The world remembers, in a typed ledger** (`governance_play_redesign_v1.md` › §1.6). Precedent,
Grudge, Debt, Reputation — four tag families that persist, bias future rolls, gate event cards, and
**survive succession**. This is the mechanism by which player choices become world state rather than
score. It wants to be a general primitive, not a settlement-local one.

## The one idea the corpus keeps reaching for and never lands

**Autonomous NPC pursuit.** `governance_play_redesign_v1.md` § 3.2 states it exactly right — every
significant NPC carries an `ambition` (goal, method, timeline, progress) and a `trajectory` (what they
do when thwarted), and **advances it every Accounting whether or not the player engages**:

> "The player who ignores the ambitious Magistrate doesn't get a frozen NPC — they get a Magistrate
> who, three seasons later, has the votes to challenge them."

The same idea appears, unconnected, as the faction priority trees, as the insurgency pipeline's
four-stage promotion, as the RM's Stage 1→5 emergence, as graduated Löwenritter autonomy, and as the
succession contest. **These are all the same mechanism at different grains**: an entity with a goal, a
rate of progress, a set of triggers that promote it to a new state, and a set of conditions that
reverse it. The corpus builds it five times and shares nothing between them.

Unified, it is one pipeline primitive — *entity, goal, progress rate, promotion predicate, demotion
predicate, terminal states* — and every one of those five becomes data rather than code.

## The concrete case for single ownership: Accord has two write paths, and one erases the other

`Accord` is the province-scale acceptance quantity. The corpus defines it as a **pure derivation**:

> "**Accord derivation (REVISED):** Province Accord is now the floor of the average Order across all
> settlements … a province with settlements at Order 4, 2, and 1 → province Accord =
> `floor((4+2+1)/3) = floor(2.33) = 2`." — `settlement_layer_v30 (1).md:61` › §1.3
> "Order = civil compliance, **feeds province Accord via `floor(mean settlement Order)`**" — `:156` › §1.8
> "Province Accord **recalculates via floor-average derivation**" — `settlement_adjacency_v30.md:110`

And then **nine files still write Accord directly**, with no reference to settlement Order at all:

| write | source |
|---|---|
| "Attacker conquest: territory **Accord → 1**. Defender territory: **Accord −1**." | `strategic_layer_v30.md:175` (PP-647) |
| "Seized territories start at **Accord 1** (military-equivalent) or **Accord 2** (if PT ≥ 3)." | `campaign_architecture_v30.md` › §1.3 |
| "Success \| **Accord +1** in target territory (max 3)" · "Overwhelming \| Both: **Accord +1** AND Mandate +1" | `ci_political_v30.md:227–228` |
| "All factions: **Accord −1** in one non-capital territory" · "**Accord −1** in ALL non-capital territories" | `ci_political_v30.md:251–252`, `core (1).md:147–148` (Strain bands) |
| "Govern Success in any territory = **Accord +1**. Govern OW in capital = Mandate +1 AND Accord +1" | `ci_political_v30.md:402` |
| "Garrison required (≥ 1 unit) or **Accord → 0** at Accounting" | `core (1).md:112` |
| "Varfell **Accord −1** in T4" | `early_game_ignition_analysis.md:129` |

**At the next Accounting the derivation recomputes from settlement Order and discards every one of
those writes.** A conquest that sets Accord to 1, a Strain band that docks it, a successful Govern
that raises it — all overwritten by `floor(mean Order)` the moment the cascade runs.

**And the corpus already saw this, and already wrote the fix.** The same line that defines the
derivation ends:

> "Existing Accord change rules (peninsular_strain §2.3–2.4) **now operate by modifying settlement
> Order values, which cascade upward**." — `settlement_layer_v30 (1).md:61`

`settlement_adjacency_v30.md:110` states it again for the conquest case: "**Accord drop: now applies
to the settlement's Order (Order −1), not the province's Accord.**"

So the rule below is not this document's invention — **it is the corpus's own, stated at the line
that defines the derivation.** What never happened is the propagation: nine files still carry direct
Accord writes, including `phases.md` step 4c, inside the very Accounting sequence this design adopts.
That is the whole defect, and it is a smaller and more tractable one than "nobody reconciled this".

This is not a bookkeeping slip. It is what happens when a quantity is *derived* in one document,
*stored* in nine others, and the correcting instruction is issued once in a subordinate clause. It is
the single clearest argument for the rule the rebuilt architecture should enforce above all others:

> **Every quantity has exactly one owner and exactly one write path. If it is derived, nothing writes
> it; the things that would have written it write its inputs instead.**

Applied here — and this is the corpus's instruction, promoted from a clause to a rule: conquest does
not set Accord, it sets the **Order** of the settlements it took (and their controller). Strain does
not dock Accord — it docks **Order** in the affected settlements. A successful Govern raises
**Order**. Accord then falls out, and the conquest, the strain and the governance are all still
visible in it, because they moved the thing it is made of.

**One range defect comes with the adoption and must be fixed in the same move.** `tracks.md:105`
declares "**Accord (Per-Territory, 0–3)**" with a band table that stops at 3, while settlement Order
runs 0–5 — so `floor(mean Order)` can return 4 or 5, outside Accord's declared range and off the end
of its own band table. Either Accord widens to 0–5 and gains two bands, or the derivation is scaled.

**Widen it — and a live rule already assumes it is wide.** `insurgency_pipeline_v30.md:162` gates
promotion to a full faction on "**Accord ≥ 4** averaged across held territories (population
acceptance)", a threshold that on a 0–3 scale can never be met. So the corpus contains both a stated
range of 0–3 and a promotion gate that requires 4, and the derivation from settlement Order can
produce exactly the values that gate needs. Three facts point the same way; the range is the thing
that is wrong.

The same test applied across the corpus retires several quantities outright: **Mandate** is already
declared a pure aggregate of settlement L/PS, so nothing may write Mandate either — the mission
outcomes and parliamentary results that currently adjust it should adjust the settlement L/PS they
are supposed to represent.

## The corpus already invented its own resolution kernel — and it is the right one

`stats_1_7_scale (1).md` › **Domain Action Resolution (deterministic+stochastic) — CANONICAL
(ED-874, ratified 2026-05-31)** is the most architecturally significant thing in the corpus, and it
is *under*-referenced rather than unreferenced: three section-level citations, from two documents —
`ci_political_v30.md:221` and `:234` ("See `stats_1_7_scale.md` §Domain Action Resolution
(ED-865/874)") and `faction_succession_split_v30.md:54` ("via the deterministic+stochastic resolver").
Three pointers, for a ruling that changes how every faction check in the game is decided.

```
margin  M = acting_stat − difficulty
    difficulty = the contested target's relevant stat   (contested actions)
               | a fixed action-difficulty rating       (non-contested)
    legacy mapping:  an action previously "vs Ob O"  →  difficulty D = max(1, (O−1)·2)

P_success(M)       = clamp(0.50 + 0.10·M, 0.05, 0.90)
P_overwhelming(M)  = clamp(0.50 + 0.10·M − 0.35, 0, 0.55)
P_atleast_partial  = clamp(0.50 + 0.10·M + 0.20, P_success, 0.97)

draw r ~ U[0,1)   (lower is better)
    r < P_overwhelming                 → Overwhelming
    P_overwhelming ≤ r < P_success     → Success
    P_success      ≤ r < P_partial     → Partial
    r ≥ P_partial                      → Failure
```

Parameters, ratified: **BASE 0.50** ("an even contest is fair"), **SLOPE 0.10** — "leverage is +10% per
stat-point of margin, **constant across the whole 1–7 range**" — **FLOOR 0.05** ("punching-up is hard
but never impossible — fixes the ~1% wall"), **CAP 0.90** ("overmatch reliable but never certain").
Live leverage zone `M ∈ [−4, +4]`.

**Three things make this the spine rather than one mechanic among many.**

**1. It states its own reason, and the reason is a real defect.** "The bare-stat d10 pool gave neither
legible odds nor uniform leverage at the small pools faction stats produce (1–7), making *noise*
decisive on pivotal, irreversible outcomes where structure should be." A d10 pool's leverage falls as
`1/√N`; a coup decided by a pool of 3 is a coin-flip wearing a simulation. The fix is not a bigger
pool — it is to stop rolling pools for structural questions.

**2. It fixes the output type and leaves it fixed.** Verbatim:

> "**Output is unchanged.** The resolver emits the same four-degree ladder
> (Failure/Partial/Success/Overwhelming) the dice system did, so Domain Echo (`scale_transitions_v30`
> §5: Success +1, Overwhelming +2, cap ±2) and all cost tables are untouched — **only the resolution
> *method* changes.**"

This is the whole of good architecture in one sentence. **`Degree` is the currency.** Every subsystem
produces one and every consequence consumes one, so the method that produced it is private.

**3. It draws an explicit scope boundary instead of universalising.**

> "**Scope boundary.** This method governs **bare-stat faction checks only.** Healthy dice systems —
> personal combat, social contest (pools 5–18D), aggregated mass battle — **remain dice** … replacing
> them would add complexity without fixing a defect."

### This is what makes the scales complementary rather than redundant

The brief for any rebuild is that each scale should do work the others cannot. The resolver supplies
the criterion, and it is about **variance**, not about subject matter:

| scale | pool size | what noise does there | resolution |
|---|---|---|---|
| **Personal** — combat, social contest | 5–18 dice | noise is *texture*: it makes a duel or an argument feel alive, and no single roll is irreversible | **dice** |
| **Tactical** — mass battle | aggregated | noise averages out across many subunits; the aggregate is already structure-decisive | **dice** |
| **Structural** — faction Domain Actions, seizures, votes, successions | 1–7 stat points | noise is *corrosive*: it decides irreversible, pivotal outcomes that should follow from position | **d+σ resolver** |

Same four-degree output at every scale; three different generators chosen by how much variance the
decision can bear. That is complementarity earned from a principle rather than asserted.

**What the rebuild must finish.** The migration is partial and the corpus says so: Assert, Suppress,
Reconstitute, Parliamentary Rebuttal, Treaty positioning and ratification, the Accounting Stability
Check, and four Unique Actions have migrated, each with its named degree-hooks preserved. Roughly
thirty other actions have not, and one is explicitly stranded — "*Hafenmark Sovereign Authority
Doctrine — bare Mandate vs Ob 4 — is the same class but was not in the ratified four; pending
decision.*" The legacy mapping `D = max(1, (O−1)·2)` makes finishing it mechanical rather than a
redesign: every surviving "vs Ob O" converts by formula.

## The second pillar: Domain Echo is already the right propagation mechanism

The corpus's cross-scale coupling is called **Domain Echo**. Its home document
(`scale_transitions_v30` §5/§7) is not in the upload, but its contract is fully recoverable from the
six documents that cite it, and it is the mechanism the architecture needs:

| property | source |
|---|---|
| **Magnitude comes from the degree, not from the action.** "Success +1, Overwhelming +2, **cap ±2**" | `stats_1_7_scale (1).md:86` |
| **It is gated by "Sufficient Scope"** — not every outcome propagates | `faction_behavior_v30.md:433`; `player_agency_v30 (3).md:100, 214` |
| **It batches; it does not apply inline.** "Domain Echo from personal scene \| **Batch to Cascade** (applied in Cascade step 1)"; the Cascade's step 1 is "**Domain Echoes from Personal phase scenes**" | `strategic_layer_v30.md:667, 719` |
| **It is the only translation path between scales.** "Domain Echo handles **TTRPG → faction layer translation**"; personal outcomes "reach faction stats **via the Domain Echo path** when they meet Sufficient Scope" | `ci_political_v30.md:429`; `faction_behavior_v30.md:433` |
| **It chains through however many scales exist.** "Governor → Province → National **as Domain Echo chain**" — the settlement layer inserted a new scale level and the mechanism absorbed it without change | `settlement_layer_v30 (1).md:710, 773` |

That last row is the proof that the abstraction is sound: a whole new scale was added to the game and
the propagation mechanism needed no amendment.

**Three primitives, and the architecture follows from them.** Put beside the resolver, the corpus has
already converged — without noticing — on the spine a clean implementation needs:

```
Degree   ::= Failure | Partial | Success | Overwhelming
             the single output type of every resolution, at every scale,
             from whichever generator that scale's variance requires

Echo     ::= { magnitude: from Degree (+1 / +2, clamped ±2),
               scope:     Sufficient-Scope predicate,
               target:    a SCALE, never a named subsystem }
             the single propagation type between scales

Cascade  ::= the one phase where echoes commit
             nothing crosses a scale except by batching here
```

**No subsystem names another.** A settlement action emits an Echo at province scale; it does not know
what a province is made of. A faction Domain Action emits an Echo at peninsula scale; it does not know
which clocks exist. Adding a scale — as the settlement layer did — means adding a link to the chain,
not editing the emitters.

**And it gives the commit-timing rule the corpus otherwise left to a referee.** `strategic_layer_v30`
§9.3 leaves inline-versus-batched application to "a Game Master call"; but the Domain Echo path has
already decided it — **everything batches to Cascade**. The referee clause is not a missing rule, it
is a *contradiction of a rule the corpus already has*. Deleting it costs nothing and makes the season
deterministic.

## The tick already exists, and its shape is right

`phases.md` gives the season loop in full: a three-layer resolution model, a seven-tier action
priority within the action phase, a thirteen-step Accounting, and a ten-step Year-End every fourth
season.

**The bottom-up layer order is the good bone.** `phases.md` › Three-Scale Resolution Model:

> "Each season resolves in three layers, **bottom-up**:
> 1. **Settlement layer** (resolves first) … Settlement Order and Prosperity update …
> 2. **Province layer** (resolves second). Fragmentation checks **using updated settlement data**.
>    Accord recalculates from settlement Order floor-average …
> 3. **Peninsula layer** (resolves third). RS/CI/IP/PI/Strain clocks update from province-level
>    events … Victory condition check against updated PV totals.
>
> Control flows upward: settlement infrastructure → province Accord/PV → peninsula victory.
> Pressure flows downward: peninsula events → province consequences → settlement disruption."

This is exactly the composition order a derived-quantity architecture requires: **write the leaves,
then recompute upward, then evaluate the global conditions.** Given the single-ownership rule, it is
also *sufficient* — Accord and Mandate fall out of step 1's writes without anyone needing to set them.

**The action phase's ordering is a real priority, not an accident.** Seven tiers — Intel/Covert first
("Executes first; **shapes information before other actions**"), then Military, Domain, Social,
Thread, Special/Unique, Project — with "Within tier: descending Stability order." That first line is
a genuine design commitment: *information resolves before the actions that would use it*, so a season
cannot be won by acting on knowledge you gain in the same season.

Its tie-break is the one gap. `phases.md` says only "Ties: simultaneous"; `strategic_layer_v30` ›
I-07 catches that this is undefined for three or more and supplies PATCH P-18 — "Three or more
factions tied on Stability: resolve in **alphabetical faction order** (consistent, arbitrary, no
player advantage)". Adopt P-18; the corpus already fixed this and the fix never propagated back into
`phases.md`.

### Two structural tells in the Accounting sequence

Both are symptoms of the same thing — **an ordinal-keyed list being used as an identity**.

**1. A dead step, preserved for its number.** `phases.md` › Phase 5, step 11, verbatim:

> "11. [DISSOLVED — Hollow Victory totals no longer tracked. **Step retained for numbering
> continuity.**]"

A step exists solely so that step 12 can still be called step 12. Four of the thirteen steps have
already had to grow letters — seven of them, 4b, 4c, 4d, 4e, 8b, 9b, 10b — because new work had to be
inserted between numbers. **The phase sequence wants to be a named, ordered list of phase handlers**, where
inserting a phase is adding an entry and removing one is deleting it. Then nothing is retained for
continuity, because nothing was ever keyed to a position.

**2. The dissolved mechanic is still running at Year-End.** Phase 5 step 11 says Hollow Victory is
dissolved and no longer tracked. `phases.md` › Year-End Accounting, step 6, in the same file:

> "6. **Hollow Victory totals announced publicly.**"

A quantity that is not tracked is announced annually. This is the ordinal-keying defect again from
the other side: the Year-End list is a *separate* numbered sequence, so a dissolution applied to one
list never reached the other.

**3. And the retired loss framing is wired into the victory check itself.** Phase 5 step 12:

> "12. Victory condition check. … Co-victory pairings checked simultaneously (§4). **Shared loss
> conditions checked first (§5).**"

`campaign_architecture_v30.md:5` declares "All '**shared loss**' framing" superseded. The tick still
evaluates it, and evaluates it *first*.

### The idealized tick

Keep the bones, drop the ordinals:

```
PH-1  ACT        — resolve declared actions in tier order
                   (Intel → Military → Domain → Social → Thread → Unique → Project;
                    within tier by descending Stability, then alphabetical)
                   → produces Degrees; writes nothing but intents and Echoes

PH-2  COMMIT     — apply every pending write to its OWNER, leaves first
                   (settlement Order/Prosperity/Defense, L/PS, ledger tags)

PH-3  DERIVE     — recompute every derived quantity bottom-up
                   (settlement → province Accord/PV → faction Mandate/Treasury)
                   nothing else may write these

PH-4  ECHO       — apply batched Domain Echoes at their target scale, clamped ±2

PH-5  CLOCKS     — advance CI · IP · PI · MS · Strain from the season's events, apply caps
                   (±5 CI/season all sources, ±3 from Domain Actions, ±2 per faction stat)

PH-6  PRESSURE   — recompute Π per settlement; draw 1 + ⌊Π/3⌋ cards; advance NPC ambitions

PH-7  THRESHOLD  — fire band crossings, emergence checks, promotions and demotions

PH-8  RESOLVE    — victory and terminal conditions

PH-9  ADVANCE    — season marker; every 4th season, the annual sub-tick
```

Each phase names what it reads and what it may write, and **no phase may write a quantity another
phase derives**. That single constraint is what turns the corpus's thirteen steps plus seven letters
into nine phases that can absorb new mechanics without renumbering anything.

## Five pipelines that are one pipeline

The corpus builds the same state machine five times, at five grains, sharing nothing. Laid side by
side the identity is unmistakable — every one is *an entity with a goal, a rate of progress, a
promotion predicate, a demotion predicate, and terminal states*.

| | **Löwenritter autonomy** | **Insurgency pipeline** | **NPC ambition** | **Succession contest** | **RM emergence** |
|---|---|---|---|---|---|
| **grain** | a sub-faction | a territory cluster | a person | a faction | a movement |
| **states** | Loyal → Restless → Autonomous → **Split** | world-decay → Latent → Insurgency → **Promoted Faction** | progress 0…5 → **acts** | Stage 1 *who leads* → Stage 2 *whether it splits* | Stage 2 → … → **Stage 5** |
| **advance** | Crown Stability ≤ 3 · no military action 4+ seasons · Crown loses a province · Ehrenwall Disposition < 0 | `RM_PT_DECAY_CHANCE 0.35`, growth per arc; 2+ contiguous Uncontrolled territories sustained 2 seasons | "+1 each Accounting **unless the player or another actor intervened**" | leader eliminated → contest opens next Accounting | Order = 0 AND PT ≤ 1 AND Disposition ≥ +3 |
| **promote when** | a threshold on the trigger set | trigger predicates per GD-3 (a)–(e) | `progress` hits threshold → emits an Ambition card | gap `G` ≥ 3 unified / = 2 fractious / ≤ 1 split | once per province per 4 seasons |
| **demote / reverse** | "**reversible at stages 1–3**"; raise Stability above 3, conduct a military action, improve Disposition | "suppression mechanics return stages 3-4 to lower-stage states; **cannot fully erase stage 1**" | "if ambition blocked → shifts method (lawful → factional → violent/covert)" | re-merge on Mandate 3+ and treaty | dissolution → "non-existence", not back to Latent |
| **terminal** | Split — "**only stage 4 is irreversible** without reconquest" | Promoted Faction — eligible to win | the NPC acts | two factions, or one | a faction |

Five tables, five vocabularies, five code paths. One shape.

**Unified, it is a single primitive and every instance becomes data:**

```
Pipeline {
  subject      : EntityRef            # settlement · faction · person · territory-cluster
  states       : [State]              # ordered; the last are terminal
  advance      : Rate                 # per tick, conditioned
  promote      : Predicate → State    # evaluable, no referee
  demote       : Predicate → State    # the corpus is unusually good at specifying these
  irreversible : {State}              # Split; Promoted Faction; the NPC having acted
  on_enter     : [Effect]             # emits Echoes; never writes another scale directly
}
```

Two properties the corpus earned and a naïve unification would lose:

**Asymmetric reversibility.** Every one of these machines is reversible early and irreversible late,
and each says so in its own words — "reversible at stages 1–3", "cannot fully erase stage 1",
"no second attempt", "not back to Latent". That asymmetry is the corpus's most consistent design
instinct and it must be a first-class field, not an accident of how each was coded.

**Progress that does not wait for the player.** "The player who ignores the ambitious Magistrate
doesn't get a frozen NPC — they get a Magistrate who, three seasons later, has the votes to challenge
them." The advance rate ticks in `PH-6` regardless of engagement; player action changes the rate or
trips a demotion predicate, it does not gate the clock. This is the whole of "the world moves whether
or not you do", and it costs one field.

**What this buys.** Graduated Löwenritter autonomy stops being a bespoke four-row table in a proposal
document and becomes five rows of data. So does the insurgency ladder, the succession contest, the RM
ascent, and every NPC ambition in every settlement. Adding a sixth — a guild going independent, a
cardinal building a faction, a governor's own emergence, all of which the corpus gestures at — is
authoring, not engineering.

And the corpus already noticed. `faction_succession_split_v30.md` describes itself as a "**Universal
Succession Contest Framework**" *generalized from the Baralta spec* — one instance promoted to a
framework. That promotion, applied four more times, is the whole refactor.

## Where the line between data and code falls

The corpus is, by volume, overwhelmingly *content* written in the grammar of *code*. Sorting it
correctly is most of the implementation.

**Code — mechanism, small, and it should stop growing.** Six things:

1. **The resolver.** `d+σ` for structural checks; dice pools for personal and tactical scale. Two
   generators, one `Degree` output.
2. **The tick.** Nine ordered phases, each declaring what it reads and what it may write.
3. **The composition rules.** How settlement state aggregates to province and province to faction —
   `floor(mean Order)`, `Σ Prosperity`, the size-weighted saturating `Mandate = clamp(round(7·T/(T+K)), 0, 7)`.
4. **The pipeline runner.** One state machine interpreter, above.
5. **The echo bus.** Degree → magnitude → target scale → clamp → apply at Cascade.
6. **The ledger.** Typed durable tags with time-to-live, written by effects, read by predicates.

**Data — everything else, and there is a great deal of it.** The whole of `geography.md`'s territory
table; every rank ladder and initiation gate in `faction_politics_v30`; the four Church infrastructure
axes and their obstacle modifiers; the temperament table; every clock's bands and thresholds; the
Tensions Deck; every event card; every NPC dossier; every governance verb with its method choices;
each of the five pipelines above expressed as states, predicates and rates.

**The test that sorts them:** *would adding another one of these require a programmer?* Another
province, another rank, another card, another verb, another ambition, another clock band — all should
be authoring. Another *scale*, another *resolution method*, another *kind of durable consequence* —
those are the six.

### The corpus's own strongest evidence for this line

`governance_play_redesign_v1.md` § 2.2 already writes an event card as data, and the schema is very
nearly right as it stands:

```yaml
card:
  id: EVT-Sxxx
  family: Petition | Friction | Opportunity | Crisis | Intrigue | Ambition | Thread
  triggers:                       # state predicates — ALL must hold
    - settlement.Order <= 2
    - settlement.has_subnational(RM)
  weight: base + Π-scaling + tag-modifiers
  cooldown: 2
  excludes: [EVT-Syyy]
  the_ask: { summary: "…", pressure_if_ignored: +2 }
  responses:
    - verb: Hold Court (rule for) -> Magistrate.Disp +1, Garrison.Disp -1,
                                     Precedent: "conscription-exempts-only-sons", Π -2
    - ignore                      -> Π +2, Grudge(Magistrate), Reputation -> "Weak"
  follow_on:
    - on Grudge(Magistrate): unlock EVT-S140 "Magistrate backs a rival"
```

Predicates in a small evaluable language, weights, cooldowns, exclusions, typed consequences, and
chaining — authored, not compiled. And the document says exactly what this replaces: it is "the
canonical home for the §4.3 settlement events, **generalized from 8 hard-coded rows into an open,
stateful … card set**."

**That sentence is the refactor, stated by the corpus about itself.** Eight hard-coded rows became a
schema. The same move applied to the four Church infrastructure axes, the seventeen province rows,
the seven rank ladders, the five pipelines and the five clocks is the entire difference between a
codebase that grows with the design and one that grows with the content.

The full sentence also shows exactly how much TL-1 work remains, and it should be quoted whole rather
than trimmed: the deck is "generalized from 8 hard-coded rows into an open, stateful,
**GM-/sim-authorable** card set", and § 5.3 asks for the "**GM-authorable vs sim-generated split**".
The schema is right and the authorship model still has a referee in it. In a no-GM engine the split
is not between GM-authored and sim-generated cards — it is between **authored** cards (content, in
the schema above) and **generated** ones (a template plus the settlement's current state). Both are
data; neither is a person at the table.

One correction to the schema, from the reconciliations: `responses` currently names verbs inline, and
the verb list is settlement-local. It should name **actions by id from the action catalogue**, so the
same card can be answered by a governance verb, a faction Domain Action or a personal scene depending
on who is looking at it — which is what a three-scale game needs and what a settlement-local verb list
cannot express.

## The throughlines — what must survive any rebuild

Throughlines are not mechanics; they are rules *about* mechanics. These are the ones the corpus holds
consistently enough to build on, with the documents that carry them.

**TL-1 · There is no referee. The engine resolves everything.**
The corpus violates this in ~36 places across 10 documents and *fixes* it in exactly one, which is
the pattern to copy — `player_agency_v30 (3).md:212`: "one sentence, GM may incorporate or reject;
**videogame: pre-scripted dialogue branch tagged to player Conviction**". Every referee clause gets
that treatment: name the predicate, or delete the branch.

**TL-2 · One victory condition for everyone (GD-1).**
"Per GD-1 the SOLE victory condition for all factions is Peninsular Sovereignty … **no
faction-specific or non-military victory path exists**" (`core (1).md:10`). Faction-flavoured tracks —
CI, RDT, Restoration presence, Warden stewardship — are *approaches* to it, never win triggers:
"faction-specific tracks in victory_v30 §3 are **approaches, not win triggers**"
(`faction_behavior_v30.md:94`). This is the constraint that keeps five asymmetric factions playing
one game, and it is worth more than any of the tracks it demotes.

**TL-3 · Nothing that emerges can bypass the game (GD-1 binding).**
"insurgencies and promoted factions produce **stat/territorial deltas only, never victory triggers**"
(`insurgency_pipeline_v30.md:7`), and symmetrically a promoted faction is *fully* eligible: "A
successful insurgency that grows to 11+ territory sustained 2 seasons **wins — including against the
parent faction it emerged from**" (`:278`). New entities enter the same game on the same terms.

**TL-4 · A faction cannot ignore a threat (GD-2).**
"**mandatory threat response**" — insurgency formation compels the parent faction to act, and
"Standard GD-2 mandatory action triggers apply if Accord drops below threshold in adjacent parent
territories" (`insurgency_pipeline_v30.md:284–286`). This is what stops NPC factions going passive
when the player is elsewhere, and it belongs in the AI's obligation layer rather than in each
subsystem.

**TL-5 · Control flows up; pressure flows down.**
`conflict_architecture_proposal.md` › The Three Scales, and `phases.md`'s bottom-up resolution order
implement it. The corollary the corpus states and does not always keep: **a scale may only read the
scale below and write the scale above** — via Echo.

**TL-6 · Everything is capped, and the caps are uniform.**
±5 CI per season from all sources, ±3 from Domain Actions (PP-504); ±2 per faction stat per season;
Mandate hard 0–7; Domain Echo clamped ±2; Prosperity, Order, Defense bounded. The corpus defends the
uniformity explicitly when tempted to make an exception — "counts against the ±5/season CI cap **like
any other territory. The cap is uniform. No T9 bypass.** … uniform mechanic preserves cap design
intent" (`ci_political_v30.md:378`), rejecting two alternatives that would have special-cased the
Church's keystone territory. **That instinct is the corpus at its best** and it is exactly the
anti-special-case rule an engine needs.

**TL-7 · Reversible early, irreversible late.**
Every pipeline says it in its own words. Asymmetric reversibility is the corpus's most consistent
structural instinct and belongs in the pipeline primitive as a field.

**TL-8 · Consequences persist and survive succession.**
Ledger tags "persist across the governor's tenure and **survive succession** (the next governor
inherits the settlement's memory)" (`governance_play_redesign_v1.md` § 1.6); the generational model
partitions every tracked value into PRESERVE / TRANSFORM / RESET / BREAK / TRANSFER
(`generational_transition_v30.md`). **State outlives the character.** That is what makes a campaign a
place rather than a save file.

**TL-9 · No scripting; the game is system-driven.**
"Emergent narrative comes from fragmentation checks, bishop appointments, and black market emergence —
**all system-driven, no scripting**" (`conflict_architecture_proposal.md:156`); "stature progression
as **emergent possibility, not scripted path**" (`player_agency_v30 (3).md:49`); "risen from nobody to
contender through accumulated deeds, **not scripted events**" (`settlement_layer_v30 (1).md:614`).
Three documents, one commitment. It is also the sharpest test to apply to any proposed mechanic: if
it names a specific faction, territory or outcome, it is scripting and the abstraction is wrong.

**TL-10 · The world acts whether or not the player does.**
The Directive is mandatory, the deck always draws, ambitions advance every Accounting, NPC priority
trees fire, GD-2 compels response. Five mechanisms, one commitment — and the one the whole
"two-stroke churn" rests on.

---

**Where the throughlines conflict, TL-6 and TL-9 win.** They are the two that protect the engine from
the design: uniform caps stop a mechanic from escaping its bounds, and no-scripting stops a mechanic
from being written for one entity. Every special case the corpus was tempted into — a keystone
territory bypassing the CI cap, a faction-specific victory path, a hand-authored settlement event
row — was correctly refused on one of those two grounds, and the refusals are on the record.

---

# Part II — The sets


Two groupings of the same 33 documents were built without sight of each other:

- **Read-based (14 sets).** A full reading of every document, grouping by *what a document specifies*.
  Membership criterion stated per set; a document may belong to many. Produced by the stage-A reader.
- **Measured (6 components + 16 singletons).** tf-idf cosine over each document's capitalised domain
  terms and acronyms, connected components at cosine ≥ 0.30. Produced mechanically, no reading.

The measured method answers "which documents *talk about* the same things"; the read method answers
"which documents *specify* the same things". Where they agree, the grouping is real. Where they
disagree, the disagreement is the finding.

## Agreement — five of six measured components map cleanly onto read sets

| measured component | maps to read set(s) | verdict |
|---|---|---|
| `faction_politics`, `institutions`, `player_agency`, `worldbuilding` | SET-10 Kingdom Institutions + SET-11 PC Agency/Standing/Rank | agree |
| `march_layer`, `settlement_adjacency`, `settlement_layer`, `valoria_political_hierarchy` | SET-05 Geography & Movement + SET-06 Settlement Layer | agree |
| `ci_political`, `core` | SET-04 Church Influence/Piety/Seizure + SET-01 Resolution Engine | agree |
| `conflict_architecture`, `early_game_ignition` | SET-12 Conflict Ignition & Campaign Arc | agree — and this pair is also the corpus's only mutual citation, one superseding the other |
| `stats_1_7_scale`, `strategic_layer` | SET-01 Resolution Engine & Action Economy | agree |

## Where the methods converge hardest — and what that converged-on thing is

The strongest pair in the whole corpus by vocabulary is `parliamentary_transfer` ↔ `treaty_expiration`
at **0.56**, with `insurgency_pipeline` attached at 0.39. The read method **agrees**: it makes
`treaty_expiration` and `parliamentary_transfer` the *two co-centres of gravity of SET-14* (Diplomacy,
Treaties, Pledges & Casus Belli), and places `insurgency_pipeline` elsewhere — in SET-09 (Succession,
Splits, Emergence & Collapse), which is where its subject belongs.

*(An earlier reading of this comparison claimed the two methods disagreed here — that the read method
split the three across three sets. It does not; SET-14 lists both as co-centres. The claim is
withdrawn.)*

**But the vocabulary is not binding them by subject, and that is the finding.** A treaty lapsing and a
province changing hands by parliamentary motion are different mechanics; what makes their term
vectors nearly identical is that they were written to a **shared template**. These three documents,
and only these three of the thirty-three:

- carry `## Status: CANONICAL — Pass 2h/2i authoring 2026-05-17`;
- declare an executable target — `## Sim module:` — naming `sim/world/insurgency_pipeline.py`,
  `sim/provincial/parliamentary_transfer.py`, `sim/provincial/treaty.py`;
- carry an N=1000 balance validation ("v12c balance-validated at N=1000");
- open with an explicit `## GD constraints:` block binding themselves to the canon constraints;
- state their triggers as evaluable predicates with named constants.

**The corpus contains one worked example of what a finished specification looks like in this project,
and it is three documents long.** The template is recoverable and it is the right template: subject,
binding constraints, provenance, an executable target, a validation, and predicates a machine can
evaluate.

**Consequence for the rebuilt sets.** The trio is not a set — it is a **standard**. The rebuilt
structure keeps the read method's subject-based sets and lifts the trio's document shape out as the
form every set's specification should take.

## What the measured method could not see

Sixteen documents are singletons at cosine ≥ 0.30, including `governance_play_redesign_v1` (nearest
neighbour `settlement_layer` at 0.24) and `campaign_architecture_v30` (nearest `player_agency` at
0.28). The read method places `governance_play_redesign_v1` firmly in SET-06 and SET-11, and
`campaign_architecture_v30` in **six** sets while being the centre of none.

Those two failures are the same failure: **vocabulary similarity cannot see a document that
introduces new terms** (the governance redesign brings Administration Points, Directives, the Π
homeostat, Ledger tags, NPC ambitions — none of which occur elsewhere), **or one that spans too many
subjects to have a centre** (campaign_architecture covers Church infrastructure, RM identity, MS and
Coherence, the revelation curve, IP phases, Warden paths and Portrait Retirement in seven parts).

The second is itself a design signal: a document that belongs to six sets and anchors none is not a
document, it is a **session transcript**. Its seven parts belong in seven places.

## The corpus's shape, measured

Three measurements that bear on which documents a rebuild should trust and which it should mine.

**Citation structure.** Counting a citation only where one document names another *as a file*
(`name.md`, or a `params/…` path), and excluding bare mentions of the ten stems that are also
ordinary words here (*core*, *parliament*, *geography*, *clocks*, *tracks*, *phases*, *institutions*,
*ministry*, *southernmost*, *ci_seizure*, whose in-degrees are therefore **lower bounds** — a
permissive matcher raises *parliament* and *core* to 13 each, *geography* and *tracks* to 9):

- **One hub.** `settlement_layer_v30` has in-degree **11**, more than half again the next
  (`conflict_architecture_proposal`, 7), cited by eleven of the other thirty-two. Everything about
  governance resolves through it, and it is where the acceptance model, the settlement registry and
  the aggregation to Mandate all live. **It is the right hub**, which is the useful part of the
  finding.
- **Fifteen documents are cited by no other** — including the largest (`strategic_layer_v30`, 55KB)
  and the newest (`governance_play_redesign_v1`).
- **Seven neither cite nor are cited**: `ci_seizure`, `clocks`, `geography`, `institutions`,
  `parliament`, `southernmost`, `strategic_layer_v30`. Six of those seven are the parameter stratum —
  the documents holding the raw numbers sit outside the corpus's own reference structure entirely.

**Provenance density.** The corpus carries **690 provenance citations** — 385 `PP-NNN` (115 distinct)
and 305 `ED-NNN` (159 distinct), 274 distinct identifiers. **None of their registers is in the
upload**, so within this corpus every one is unresolvable. Density is highest in exactly the isolated
parameter documents: `ci_seizure` 5.94 ids/KB, `parliament` 4.46, `march_layer_v30` 2.29,
`stats_1_7_scale` 2.20, `core` 2.16, `tracks` 2.15. **The documents with the most numbers have the
most provenance and the least resolvable provenance** — which is why the reconciliations decide by
design merit rather than by citation weight.

**File references.** 153 distinct cited paths, of which **24 resolve inside the upload and 129 do
not**. The four most load-bearing absences are cited by four or more documents each: `victory_v30.md`
(5), `valoria_geography_v30.yaml` (5), `canon/02_canon_constraints.md` (4) and
`references/canonical_sources.yaml` (4) — respectively the victory condition, the map and adjacency
data, the GD-1/2/3 constraints, and the currency index. Their content proved recoverable from what
the citing documents say *about* them, which is why this rebuild was possible from the upload alone;
but it means every reconstruction of those four is an inference, and marked as one.

**Status labels.** Twenty-two documents declare a status, in four syntaxes, using **eight distinct
labels** — CANON, CANONICAL, PROVISIONAL, PROPOSAL, WORKING DESIGN, DESIGN, ANALYSIS, VERIFIED — none
of which the corpus defines and none of which it orders. Eleven documents declare none, and ten of
those eleven are the parameter stratum. Four documents declare two statuses at once: three pair
"pending smoke-test **before** CANONICAL" with `## Status: CANONICAL` two lines later, and the
largest document in the corpus opens `## Status: CANONICAL` and closes "*this is a proposal
document*".

**The consequence for method, and it is the reason Part III exists.** When two documents conflict,
the corpus offers no way to adjudicate: not by status (undefined, unordered, sometimes doubled), not
by citation (the registers are absent), and not by recency (dates are inconsistent and supersessions
propagate partially). **So the collisions were decided on design merit, and each decision says which
it is.**

---

# Part III — Reconciliations

Not a defect list. Each row is a collision found in the corpus and **the decision taken**, so the
idealized model below has exactly one of everything. Where the corpus already implies an answer, the
decision follows it; where it does not, the decision is made on design grounds and marked *[chosen]*.

## Identity — one name per thing

| collision | decision |
|---|---|
| `Halvardshelm` (T11, Varfell, central fjords) vs `Halvarshelm` (T17, Hafenmark, northern mines) — two provinces one letter apart | **Rename T17 to `Nordhelm`.** Two primary keys at edit distance 1 is a defect regardless of which is "right". T11 keeps Halvardshelm; T17 becomes Nordhelm ("northern mines" is its stated character). *[chosen]* |
| `CV` (Conviction) vs `PT` (Piety Track) — the corpus rules them the same stat, defers the rename | **`PT` everywhere.** The corpus's own ruling, applied instead of deferred; 149 uses already use it against 30. `SW` (Spiritual Weight) stays distinct — it is a fixed weight on PT yield, not PT. |
| T15 `Southernmost` vs `Askeheim` | **`Askeheim` is the entity; `the Southernmost` is prose.** Follows the corpus's own recommendation in ED-645. |
| T1 lore-name "Varfell city" vs map-name `Valorsplatz` | **`Valorsplatz`.** The lore mapping predates the current geography and assigns T1 to the wrong duchy. |
| `Community Weaving` vs `Community Organizing` | **`Community Organizing`** — see the semantic decision below, which is the real question. |
| `faction_politics_expanded_v1` vs `faction_politics_v30` | **One document.** The rank ladder has one home. |
| `P-NN` meaning both a Philosophical Foundation and a mechanical patch | **`P-NN` = Philosophical Foundation only. Patches become `PATCH-NN`.** A warrant prefix that resolves two ways cannot be a warrant. |
| `territory` vs `province` for the 17 top-level nodes | **`province`.** 14 duchy provinces + Himmelenger + Askeheim + Schoenland = 17 nodes; `settlement` is the tier below. The `T1…T17` labels survive as display ids, not as a tier name. |

## Quantities — one range, one value

| collision | decision |
|---|---|
| Standing `0–7` vs `0–5` (four live carriers of the old cap, one of them a hard clamp) | **`0–7`.** The eight-position ladder is the specified one; the 0–5 cap is retired everywhere, including the standing-cap patch. |
| Prosperity `0–5` vs Valorsplatz at `6` | **`0–6`, with 6 reserved for the Kingdom capital.** The capital *should* out-rank every other settlement; widening the range is the cheaper truth than demoting the capital. Develop's `floor(P/2)+1` then yields Ob 4 there by design. *[chosen]* |
| Prosperity at province grain vs `Prosperity_s` at settlement grain | **Settlement is canonical; province Prosperity is `Σ` over members.** Matches the existing settlement→faction Treasury rollup. |
| CI ceiling `100, no freeze` vs `frozen at 75` | **`0–100`, no freeze.** The freeze is superseded; the CI-100 Mass Seizure Declaration depends on reaching 100. |
| Victory: "all 15" vs "11/15" vs "11+ of 15" vs "fractional PV total" | **11 of 15 controllable provinces, sustained 2 seasons, treaties counting; fractional holdings count as their PV share toward the 11.** Reconciles the count and the fractional-ownership rule instead of leaving them in different units. |
| The denominator `15`, never derived | **15 = 14 duchy provinces + Himmelenger.** Askeheim is uncontrollable, Schoenland is foreign. Stated, not assumed. |
| Settlement adjacency `49 edges / 36 settlements` vs `56 edges / 37` | **56 edges over 37 settlements**, and the derivation rule is restated: hub-spoke intra-province edges + one hub-to-hub edge per province adjacency + thread-witnessed specials, recomputed against the 37-node registry rather than asserted as a total. |
| Province count `17` vs `14` inside one document | **14 provinces; 17 map nodes.** Temperaments authored for Askeheim and Schoenland are dropped — neither has faction politics to have. |

## Semantics — one meaning per mechanic

| collision | decision |
|---|---|
| RM's signature action: "**NOT** a Thread operation, uses Charisma/Attunement, no MS change, no co-movement" vs "**is** a Thread operation, pool `(Spirit×2)+History+TPS`, co-movement canonical, MS ±" | **Split into two verbs, because these are two mechanics that were fighting over one name.** `Community Organizing` — RM's political action: social pool, builds Presence and consensus cells, reduces PT by cultural displacement, **no MS, no co-movement, no Thread gate**. `Thread Weaving` — the Thread operation: `(Spirit×2)+History+TPS`, TS gate, MS delta, co-movement draw. RM may *sponsor* Thread Weaving only after the revelation arc turns it, which is the story the corpus already tells. *[chosen — this is the corpus's sharpest collision and neither side is disposable]* |
| Simultaneous trigger ordering: "no strict mechanical priority" | **Deterministic order: scale (Settlement → Province → Peninsula), then phase, then a stable key.** An engine cannot have a dramatic-logic tiebreak. |
| Effect commit timing: "Game Master judges" inline vs batched | **All effects batch to Accounting** except those the acting scale itself reads back within the same resolution. Generalises the rule the corpus already wrote for military loss. |
| Shared loss retired in one document, running in five (two distinct conditions) | **Keep one: MS 0 = Rupture, universal loss.** The institutional-collapse "Threshold 10" check folds into faction collapse, which is a faction outcome, not a game end. |
| MS starts at 72 but "folklore" is the 100–80 band | **Rebase the visibility bands to the reachable range**: the campaign starts in the second band and the top band is the *restored* world, reachable only by sustained Mending. The starting state is "quiet anomalies", not "nothing". |
| ~36 human-referee decisions across 10 documents | **Each becomes an engine rule.** Where the corpus dual-specified once — "GM may incorporate or reject; *videogame: pre-scripted branch tagged to player Conviction*" — that is the pattern for all of them. |

## Two more, found while checking the decomposition

| collision | decision |
|---|---|
| **Mass Seizure obstacle stated two ways.** `ci_political_v30.md:87, 94, 415` — "Ob = **10 − PT − infrastructure** (floor 1)". `stats_1_7_scale (1).md:155, 203` — "Influence + floor(CI/15) vs **Ob = 7 − PT**", flagged "**AUTHORITATIVE** per faction_layer §2.7; supersedes the stale L-based formula". Different constant, and one drops the infrastructure term that four Church infrastructure axes exist to feed. | **`Ob = 10 − PT − Σ(infrastructure modifiers)`, floor 1; pool `Influence + ⌊CI/15⌋`.** Take the obstacle from `ci_political` and the pool from `stats`. The `7 − PT` form is the one to drop: it makes the Cathedral/Templar/Inquisitor/Governor axes — an entire subsystem with a stated −6 cap — do nothing, and a Church that has built four tiers of infrastructure in a settlement should find it easier to seize than one that has not. *[chosen]* |
| **"CI = 100 Mass Seizure Declaration" vs "Mass Seizure, one-shot from CI ≥ 60".** Read as two mechanics, they conflict: one is a mandatory event at a fixed threshold, the other a probabilistic one-shot available forty points earlier. | **They are one mechanic, and the corpus already says so.** `ci_political_v30.md:415` gives the declaration probability as `P = ((CI−60)/40)^3.3` — "1% at CI 70, 10% at CI 80, 39% at CI 90, **100% at CI 100**". The CI-100 "mandatory Zoom In scene" is simply the **P = 1 endpoint of the same curve**. Two documents described one curve from opposite ends. Keep the curve; the mandatory scene is what happens when it saturates. Nothing needs to change but the framing. |

## Sharpened by the second reader

The independent contradiction pass found several collisions to be wider than the first pass had them.
The decisions do not change; their scope does.

| collision, as widened | decision |
|---|---|
| **Victory is not stated three ways but eight.** Beyond "all 15" / "11 of 15" / "11+ of 15" / fractional PV, **five faction-specific win conditions survive in the corpus** — Church CI ≥ 65, a PI ≥ 4/5 condition, Path B, Intelligence Hegemony, and RM's Mending Stability ≥ 50 — each written as a win trigger, all of them under a throughline (GD-1) that says no such thing exists. | **GD-1 stands; all five become approaches.** Each is retained *as content* — a faction-flavoured route to territorial control — and stripped of its terminal clause. This is what the corpus itself already ruled ("faction-specific tracks … are *approaches*, not win triggers"); it simply never propagated. One win predicate, five flavours of pressure toward it. |
| **Church seizure has six obstacle formulas, not two** — `10 − PT − infra`, `7 − PT`, `max(0, 3 − PT)`, `Fort + 1`, a Military-vs-Military Ob 2, and a Mandate vs Ob 3/2 — across three triggers (CI 60 probabilistic, CI 100 deterministic, a CI 75/80 threshold). | **One trigger, one formula, as already decided**: the `((CI−60)/40)^3.3` curve with `Ob = 10 − PT − Σ(infrastructure)`, floor 1, pool `Influence + ⌊CI/15⌋`. The Military-vs-Military form is a *different mechanic* — the garrison battle that precedes seizure — and keeps its own resolution; it was being confused with the seizure roll because both were written as "the seizure". |
| **Two degree ladders and two target numbers.** Success bands are stated as "≥ 2×Ob and ≥ 3" in one place and "Ob + 1" in another; the die target is 7 in some documents and 8 in others. | **Two ladders is correct; two *outputs* is not.** The margin resolver produces its degree from probability bands and needs no net-success ladder at all; the pool resolver keeps **PP-179's `≥ 2×Ob AND ≥ 3` ladder at TN 7** — `core (1).md:73` is explicit that "ED-031 (Ob+1 surplus) is **SUPERSEDED** by PP-179 (2×Ob). PP-179 is canonical", with an Ob-10 exception (Overwhelming unavailable, Partial needs net ≥ 5). What must be single is the **output type** — both emit the same four-valued `Degree` — and the **advantage unit** that bridges them: `+1 point = +1 die = +1 M`, and `Ob ±1 = ∓2 difficulty`. That one conversion is what lets a modifier written for a dice rule apply to a margin rule without translation, and it is what makes the legacy mapping `D = max(1, (O−1)·2)` mechanical rather than a redesign. *(This corrects a call made earlier in this pass — "one ladder" — which would have forced the margin resolver into a net-success form it does not need.)* |
| **Three PV tables** with different totals (40 vs 33) and different Crown shares (16 / 14 / 12), under a victory condition scored in PV. | **PV is derived, never authored.** `PV(province) = Σ over member settlements of territory_value + unification bonus if wholly held`, computed from the settlement registry. The three tables were three snapshots of a derivation nobody had written down; write the derivation and the tables stop existing. |
| **Mandate is both a stored stat that rules decrement ("Mandate −1") and a derived saturating aggregate.** | Same defect and same decision as Accord: **derived quantities have no writers.** Every "Mandate −1" becomes a write to the settlement L/PS it was standing in for. |
| **Three incompatible territory numberings**, and the Ministry's engine keyed to **T13 (Oastad)** where its own description places it at the capital. | **One registry, ids stable, and the Ministry sits at T1 Valorsplatz** — its stated role is the civil service of the Kingdom and every other rule attaches it to the capital's Parliament and ministerial offices. *[chosen]* |
| **Struck mechanics that are still load-bearing** — the Coup Counter, VTM and Niflhel are each retired in one document and depended on by several others (an autonomy threshold, expedition and Path-B gates, a full rank ladder and settlement rules). | **Honour the strikes and re-home what depended on them.** Graduated Löwenritter Autonomy already replaces the Coup Counter and is strictly better. Niflhel's four functions already have systemic replacements (black markets, independent brokers, exploitation sites); its rank ladder becomes generic covert-standing. VTM's gates become Thread Sensitivity gates, which is what they were measuring. |

## Collapses — quantities the corpus kept under many names

The decompositions surfaced a class of collision the naming table above does not cover: not two names
for one thing, but **many names for one kind of thing**, each with its own rules. Each collapses to a
single primitive, and the collapse is pure gain — every rule written against any of the old names
still works, and the special cases stop.

| the corpus's names | collapses to |
|---|---|
| Presence markers · CP-tokens · AP-tokens · Guild Favour · Church Favour | **`s.presence[institution]`**, a bounded per-settlement value per institution. Church Prominence stays separate — it is a *comparison* of Church legitimacy against the controller's, not a stock. |
| Standing (a rank 0–7) · Standing tokens (a faction-pair credit) · Standing (public reputation, docked on treaty violation) · Warden's Accord | rank stays **`pc.standing`**; every relational sense becomes **`Regard`**, one directed ledger between parties. This is what makes the treaty pool's "Standing modifier" evaluable — the corpus never said which of the three it meant. |
| Turmoil · Public Instability | **one clock.** They advance on the same events and gate the same bands. |
| Thread Tension (TT) · Mending Stability (MS) | **`TT ≡ 100 − MS`.** One quantity, two readings; the corpus's formulas work unchanged under either. |
| Deed tokens · Hollow Victory totals · Milestone bonuses · faction-specific victory paths | **removed, with nothing lost.** Under one universal score every "path" is already a strategy toward the same eleven provinces; the tokens existed to make alternative wins countable, and there are no alternative wins. |
| Coup Counter | **Graduated Autonomy.** The counter's increments become the ladder's transition predicates — strictly more expressive, and already written. |
| Niflhel as a faction | **three derivations**: black markets from `Order ≤ 1 ∨ no governor`, independent brokers from prosperity and weak control, exploitation sites from proximity. Its rank ladder survives as generic covert standing for a player in the shadow economy. |
| VTM gates | **Thread Sensitivity gates.** That is what they were measuring. |
| **`IP`** — expanded as **Invasion Pressure** in `clocks.md:33`, `core (1).md:83`, `geography.md:19` and `settlement_layer_v30 (1).md:674`, and as **Institutional Pressure** in `baralta_crown_claim_v30 (1).md:171` and `worldbuilding_v30 (1).md:85` — both with the abbreviation attached | **two clocks, two names, and neither keeps `IP`.** *Invasion Pressure* becomes **`Altonian`** (it measures one foreign power's advance and nothing else); *Institutional Pressure* becomes **`Strain`**, which is what the rest of the corpus already calls the same quantity's bands. A two-letter key that resolves two ways across six documents is the acronym form of the `P-NN` defect, and the fix is the same: retire the ambiguous key rather than adjudicate it. *[chosen]* |
| the Cascade Depth Cap | **retired.** It existed to stop effects cascading without bound; *effects never fire effects within a phase*, so the depth is one by construction. A cap that a structural rule makes unreachable is a cap to delete. |

**The pattern in all nine.** Each name was coined where the mechanic was first needed, and the second
site coined another rather than reusing the first — the corpus's own §4.2 diagnosis of `CV`/`PT`,
generalised. The cost is not the vocabulary; it is that **each name accreted its own rules**, so a
modifier written for Guild Favour cannot touch Church Favour and a treaty clause about "Standing"
cannot be evaluated at all. Collapsing them is what turns roughly thirty special cases into nine
primitives with uniform rules.

---

# Part IV — The unified state graph


One page, bottom-up. Everything below a line is *owned* state; everything above it is *derived* and
has no writers. The arrows that cross scales are all Echoes, and they all commit in one phase.

```
                                    ┌───────────────────────────────────────┐
  PENINSULA                         │  VICTORY   11 of 15 provinces,        │
  (derived + clocks)                │            sustained 2 seasons        │
                                    └────────────────▲──────────────────────┘
                                                     │  reads only
   ┌──────────────┬──────────────┬──────────────┬────┴─────────┬──────────────┐
   │  CI  0–100   │  IP  0–100   │  MS  0–100   │  PI  0–20    │ STRAIN bands │
   │  Church      │  Altonian    │  world       │  parliament  │  Peace…      │
   │  influence   │  pressure    │  integrity   │  integrity   │  Collapse    │
   └──────▲───────┴──────▲───────┴──────▲───────┴──────▲───────┴──────▲───────┘
          │ ±5/season, ±3 from Domain Actions          │              │
          └──────────────┴──────────────┴──────────────┴──────────────┘
                                   ▲  clocks advance from the season's events (PH-5)
                                   │
  ═════════════════════════════════╪══════════ ECHO ═══════════════════════════
                                   │  degree → ±1/±2, clamped ±2, Sufficient Scope
  FACTION                          │
  (derived)          ┌─────────────┴──────────────┐        ┌──────────────────┐
                     │  MANDATE  0–7              │        │ TREASURY         │
                     │  clamp(round(7·T/(T+K)))   │        │ Σ settlement     │
                     │  K=6,  T = Σ W_s·(q_s/7)   │        │   Prosperity     │
                     │  q_s = 0.5·L_s + 0.5·PS_s  │        └────────▲─────────┘
                     │  W_s = base(Type)          │                 │
                     │       + Prosperity_s       │                 │
                     │       + FacilityTier_s     │                 │
                     └─────────────▲──────────────┘                 │
                                   │  no writers — nothing may set Mandate
  ═════════════════════════════════╪═══════════════════════════════════════════
  PROVINCE                         │
  (derived)      ┌─────────────────┴────────┐   ┌──────────────────────────┐
                 │  ACCORD                  │   │  PV                      │
                 │  floor(mean member Order)│   │  Σ territory_value        │
                 │                          │   │  + unification bonus      │
                 └─────────────▲────────────┘   │    if wholly held         │
                               │                └────────────▲─────────────┘
                               │  no writers — conquest and strain write Order
  ═════════════════════════════╪═══════════════════════════════════════════════
  SETTLEMENT                   │
  (OWNED — the only writable   │
   political state in the game) │
   ┌───────────────────────────┴───────────────────────────────────────────┐
   │  Order 0–5   Prosperity 0–6   Defense 0–5   L 0–7   PS 0–7            │
   │  FacilityTier 0–3    PT 0–5    SW 0–5 (fixed)    controller           │
   │  Ledger[ Precedent · Grudge · Debt · Reputation ]   (ttl, durable)    │
   │  Π 0–10        open_needs[]        active_directive                   │
   └───▲───────────▲───────────▲───────────▲───────────▲───────────▲───────┘
       │           │           │           │           │           │
  ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐
  │ verbs   │ │Directive│ │ conquest│ │ strain  │ │  cards  │ │ NPC     │
  │ 8, each │ │ comply/ │ │ writes  │ │ writes  │ │ resolve │ │ ambition│
  │ w/ method│ │ bargain/│ │ Order + │ │ Order   │ │ → Δstate│ │ acts    │
  │ choice  │ │ defy    │ │ controller│ │        │ │ + Ledger│ │         │
  └────▲────┘ └────▲────┘ └────▲────┘ └────▲────┘ └────▲────┘ └────▲────┘
       └───────────┴───────────┴───────────┴───────────┴───────────┘
                                   ▲
                       ┌───────────┴────────────┐
                       │   RESOLUTION KERNEL    │
                       │  d+σ  (structural)     │
                       │  dice (personal/mass)  │
                       │  ────────────────────  │
                       │  → Degree ∈ {F,P,S,OW} │
                       └────────────────────────┘
```

## What the picture asserts

**One writable tier.** Every political write in the game lands on a settlement. Conquest does not set
Accord — it sets the Order and controller of the settlements it took. Strain does not dock Accord — it
docks Order. A mission outcome does not adjust Mandate — it adjusts the L/PS of the settlements the
mission was about. Accord, PV, Mandate and Treasury then fall out, and the conquest, the strain and
the mission are all still visible in them, because they moved what those quantities are made of.

**Two derivation hops, both pure.** settlement → province (`floor(mean Order)`, `Σ territory_value`)
and settlement → faction (the saturating weighted aggregate, `Σ Prosperity`). Neither has a writer.
Recomputing them is idempotent, which is what makes save/replay trivial: persist the settlement tier
and the clocks, recompute everything else on load.

**One crossing.** Nothing reaches from one scale into another except an Echo: a magnitude derived from
a Degree, gated by Sufficient Scope, clamped to ±2, applied at a single phase. A settlement action
emits at province scale without knowing what a province is made of.

**One outcome type.** Every generator at every scale produces a `Degree`. The card that says
`Hold Court (rule for) -> Magistrate.Disp +1, … Π -2` and the seizure that says `OW → transfer + PT +1`
are consuming the same four-valued thing.

**The clocks are the only global state, and they only read.** CI, IP, MS, PI and Strain advance from
the season's events under uniform caps, and feed obstacles and thresholds back down as pressure. They
never write settlement state directly — they change the difficulty of things that do.

## The season, as the graph runs it

Twelve phases. Everything before PH-07 only *appends to an effect queue*; PH-07 is the single commit
for action effects; PH-08 onward are the Accounting phases, each committing its own effects through
the same routine. Every phase is deterministic given the snapshot and a seeded stream keyed
`(season, phase, key)`.

```
PH-01  OPEN          season flags (year_end, arc_boundary); reset budgets (AP, scene actions,
                     card cooling); read radiation rows into the snapshot
PH-02  WORLD STROKE  the settlement acts on the player: open Needs, recompute Π, issue the
                     Directive, advance NPC ambitions, draw 1 + ⌊Π/3⌋ cards
PH-03  ORDERS        every polity and PC declares — cards, duties, pledges, treaty dissolutions,
                     a Mass-Seizure declaration, a Policy
PH-04  PERSONAL      scenes resolve in pool mode; Domain Echoes queued
PH-05  SETTLEMENT    Directive response (comply / bargain / defy), AP verbs, card responses,
                     appointments, building upgrades — queued
PH-06  PROVINCE      declared actions in tier order: Intel → Military → Domain → Social → Thread
                     → Unique → Projects; within tier by descending Stability, then alphabetically
PH-07  COMMIT        the one commit for action effects, applied in (scale, path, key) order under
                     source-class sub-caps and the net ±2 faction clip
PH-08  DERIVE UP     recompute the derived snapshot — controller, Accord, PV shares, fractional
                     holdings, Mandate, aggregate L/PS, Prominence. No writes to primitives.
PH-09  PENINSULA     clocks advance in order Turmoil → CI → IP → PI → MS; band crossings,
                     milestones, peninsula cards
PH-10  PIPELINES     every state machine steps once, in registry order: fragmentation,
                     consolidation, autonomy, succession, splits, insurgency, emergence,
                     invasion phases, suspicion, ambitions acting
PH-11  SETTLE        Stability checks, cooldowns, L/PS feedback, settlement drift, Attention →
                     Inquisitors, Thread Debt ageing, CB expiry, ledger tag expiry, Π releases
PH-12  CHECK         eliminations, revolts, sustained counters, then rupture, then victory;
                     if year_end, the annual sub-tick; season += 1; state hash
```

Read the order against the picture and it is the graph evaluated bottom-up: the world moves, everyone
declares, the scales resolve upward, everything commits once, the derived tier recomputes, the globals
advance, the machines step, and only then does anyone ask who has won.

**The invariant that makes it work, stated once:** *no phase may write a quantity that a later phase
derives.* PH-02..06 write nothing but queued effects; PH-07 writes only owned settlement and polity
state; PH-08 writes only derived state and reads only owned; PH-09 writes only clocks. Every ordering
bug the corpus records — conquest overwritten at Accounting, Mandate decremented and then recomputed,
effects applied inline in one place and batched in another, a Cascade Depth Cap invented to stop
effects cascading — is a violation of that one line. The depth cap in particular becomes unnecessary:
**effects never fire effects within a phase**, so depth cannot run away and nothing needs capping.

---

# Part V — What is still genuinely open


Most of what looked like an open question in this corpus was not one — it was a decision nobody had
written down, and § Reconciliations writes them down. What follows is the short list that survives:
places where **two defensible options lead to materially different games**, so the choice is a design
call rather than a tidying-up.

**1 · Does the player govern a settlement, or a province?**
The governance redesign puts the player in one settlement with 2–5 Administration Points, eight
verbs, a Directive from above and Local Actors below — an intimate, high-resolution loop. The
Stature progression runs the same player up to "Hegemon … **multiple provinces** … competes with
Crown, Hafenmark, Varfell, Church for peninsular sovereignty". These are different games sharing a
character sheet. Either the AP loop scales up (and the intimacy dilutes), or governance stays
settlement-scale and the late game changes activity entirely (and the AP economy is early-game
content). **The corpus never chooses, and every downstream pacing question depends on it.**

**2 · Do fractional province holdings count toward victory, and how?**
Victory is a count — 11 of 15. Fractional province ownership scores in PV shares to one decimal. The
reconciliation converts shares into the count, but the conversion *is* the design: at one extreme a
faction wins by holding eleven whole provinces, at the other by accumulating eleven provinces' worth
of fragments across the map without ever consolidating one. The second is a materially different
game — sieges matter less, adjacency matters more, and the "unification bonus" that exists to reward
consolidation has to be re-tuned or it stops mattering.

**3 · Which fracturing model?**
Two are specified. One splits a contested province into **Greater / Lesser** by PV share with a
Consolidation action at ≥ 75%. The other splits it **geographically** — northern/southern,
eastern/western — and merges back automatically on common alignment. The first is a political
model, the second a territorial one; they produce different maps and different reconquest play.
Nothing chooses.

**4 · Is the Restoration Movement wrong about the world?**
The corpus's most interesting story premise: RM believes threadwork is folklore and rebuilds Einhir
governance as a *political* programme — and the governance nodes they are rebuilding turn out to be
Threadweaving sites. Three arcs are offered (Embrace, Denial, Schism) and the choice is left to
player influence. **Mechanically this decides whether RM's signature action stays social forever or
converts**, which is why the two-verb split in § Reconciliations is a scaffold rather than an answer.
The story question and the mechanical question are the same question.

**5 · What is the campaign's length, and therefore its clock rates?**
The corpus states the problem itself, and states it as unresolved rather than unnoticed —
`settlement_layer_v30 (1).md:668`: "**The existing clocks assume a 13–15 year game.** With settlements
adding governance granularity and the faction emergence pathway adding a bottom-up progression,
**games may last 20–30 years. Clocks must be recalibrated.**" A balance argument elsewhere in the same
document works from "30-year game = 120 seasons". So every threshold in the corpus is tuned to
13–15 years while the design has grown to 20–30, and the recalibration is named and not done.
This is open in the sense that matters: **fixing the target length first turns most of the remaining
balance questions into arithmetic**, and leaving it open means every clock rate, every "sustained N
seasons" trigger and every fuse window is tuned against an assumption the corpus has already
disowned.

**6 · Is Askeheim reachable?**
It is uncontrollable, holds zero settlements, is the epicentre of the calamity, and has a stated
healing path ("should the Calamity zone heal sufficiently, settlements may emerge there and the
territory may be assigned to a duchy"). If that path is live, the map has a sixteenth controllable
province that appears late and rewrites the victory arithmetic; if it is flavour, the Warden faction's
entire reason for existing is a subplot. **The corpus leaves it "a future-state contingent on
canonical healing events" — which is a decision deferred, not a decision made.**

---

Everything else that looked open has been closed by decision and recorded. These six are recorded
because closing them by fiat would be choosing the game rather than building it.

---

# Verification

**Quotation check.** Thirty-three quotations, chosen as the ones this document's arguments most
depend on, were re-opened against the corpus files and matched verbatim, including glyphs (`≥`, `·`,
`−`, `⌊⌋`, `×`, `Π`). All thirty-three verify. The set covers every load-bearing claim in Part I:
the three-scale statement and its resolution order; the Accord floor-mean derivation; the Mandate
saturating aggregate and its weight formula; all four lines of the `d+σ` resolver including the
legacy Ob mapping and the scope boundary; the Domain Echo magnitude and its batching; the tick's
dissolved step, its Hollow Victory contradiction and its shared-loss ordering; the AP formula, the Π
homeostat, ledger persistence and the NPC-ambition line; the no-scripting commitment; the
Löwenritter reversibility clause; the uniform-cap defence; all three victory formulations; the
dual-specification pattern; both Standing ranges; the "8 hard-coded rows" refactor sentence; the
"Universal Succession Contest Framework" self-description; and both GD-2/GD-3 bindings.

**Arithmetic check.** The counts stated in Part II were produced mechanically and are reproducible
from the corpus directory alone: 33 files, 810,408 bytes; the citation graph under both a strict
file-reference matcher and a permissive bare-stem matcher, with the strict figures reported as lower
bounds where the stem is an ordinary English word; 690 provenance citations over 274 distinct ids;
153 distinct cited file paths of which 24 resolve; the PT/CV and Southernmost/Askeheim usage splits;
the eight status labels and the eleven documents declaring none.

**Independent corroboration.** Two readers analysed this corpus without sight of each other's output
and without sight of this document. Where they converged — on the settlement layer as the hub, on the
implementation-ready trio sharing a template rather than a subject, on the derived-versus-stored
collision at both Accord and Mandate, on the victory condition having no single predicate — those
findings are rediscoveries rather than assertions, and are the ones this design leans on hardest.

**What is inferred rather than quoted.** Four documents the corpus depends on are not in the upload:
`victory_v30.md`, `valoria_geography_v30.yaml`, `canon/02_canon_constraints.md` and
`references/canonical_sources.yaml`. Every statement here about their content is reconstructed from
what the citing documents say about them, and is marked as reconstruction where it matters — chiefly
the GD-1/2/3 throughlines, the victory denominator, and the adjacency edge counts. The Domain Echo
contract is likewise assembled from seven citing documents rather than read from its home
(`scale_transitions_v30`), which is why its magnitude, gating, batching and chaining are each given
with the citation that establishes them.

**Adversarial pass, and what it overturned.** An independent antagonist — read-only, with no sight of
how this document was produced — re-opened roughly forty-five of its quotations against the corpus and
recomputed its counts. Every formula, parameter and cap reproduced, and the resolver section, the
Mandate derivation, the tick description, the pipeline table, the template trio and the throughline
quotations were all found clean. **Seven claims did not survive, and all seven have been corrected in
place rather than softened:**

1. **The Accord reconciliation is the corpus's, not this document's.** The line defining the
   derivation ends "Existing Accord change rules … now operate by modifying settlement Order values,
   which cascade upward", and `settlement_adjacency_v30.md:110` says it again for conquest. The
   original text claimed "nothing reconciles them". The defect is unpropagated instruction, not
   absent instruction — a smaller and more tractable finding, now stated that way.
2. **The resolver is under-cited, not uncited.** Three section-level citations exist
   (`ci_political_v30.md:221`, `:234`; `faction_succession_split_v30.md:54`). The claim that nothing
   points at it was false.
3. **Part II's "one disagreement" between the two set-groupings did not exist.** The read method makes
   `treaty_expiration` and `parliamentary_transfer` co-centres of the same set. The section is
   rewritten as a convergence; the template finding, which stands on its own evidence, survives.
4. **The Ob+1 degree band is explicitly superseded** — `core (1).md:73`: "ED-031 (Ob+1 surplus) is
   SUPERSEDED by PP-179 (2×Ob). PP-179 is canonical." The reconciliation had selected the retired
   ladder; it now selects PP-179.
5. **Batching overrides a live rule, not just a referee clause.** `clocks.md` › Cascade Depth Cap sets
   a third commit-timing rule with a dependent in `parliament.md`. The decision stands but is now
   marked *[chosen]* and argued against the rule it displaces.
6. **Campaign length is stated, and stated to be shifting** — "The existing clocks assume a 13–15 year
   game … games may last 20–30 years. Clocks must be recalibrated." Part V previously called the
   assumption unstated.
7. **Three counts were wrong**: Domain Echo is cited by six documents, not seven; the Accounting's
   lettered sub-steps are seven across four parent steps, not "nine of thirteen"; and the direct
   Accord writes span nine files, not "eight across five".

One further correction of the document's own making: a quotation of the event-card refactor had been
elided at "an open, stateful … card set", and the elided words were "**GM-/sim-authorable**" — exactly
the referee the design's first throughline says must go. The full sentence is now quoted, and the
authorship question it raises is answered rather than hidden.

**What the antagonist judged asserted rather than earned**, and which the reader should weigh
accordingly: that the corpus is "one idea implemented three times" is a reading, not a corpus
statement; and that the five pipelines "are one pipeline" is a synthesis the corpus nowhere makes,
though every cell of the comparison table verifies individually. Both are offered as design
arguments, and both are falsifiable against Annex A's decomposition.

**What it judged skipped.** Three items from the second reader's inventory that this design needs
settled and does not settle: the faction stat schema (5, 6 or 7 stats, with Crown both having and
lacking Intel); the battle→MS/IP/Turmoil clock strikes (struck in one document, live in the tick);
and the absence of any starting Prosperity/Defense/Order for any settlement, which the corpus marks
"DEFERRED … PROVISIONAL". Annex B supplies a seed-state generator for the third; the first two remain
open and are not in Part V because they are bookkeeping to settle, not designs to choose.
