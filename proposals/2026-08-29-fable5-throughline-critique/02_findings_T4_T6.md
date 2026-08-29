# 02 — Findings: T4 no one is omniscient · T5 upward aggregation · T6 downward ripple

## Status: FILED (2026-08-29) — analysis. Reads: [`00_INDEX.md`](00_INDEX.md)
## Severities: BLOCKER (throughline unreachable as designed) · DEFECT · GAP · NIT.

---

# T4 — No one is omniscient

**Verdict: PARTIAL.** The player-facing half is genuinely structural and survives attack; the NPC half
is absent — in the suite **and in shipped code**.

## T4 steelman

The presentation layer never narrates. **E-2 is a registry field, not prose** — a state row without a
`disclosure:` block fails the contract check (`01 part2:253-256`) — and the rule is asymmetric on
purpose: publish every input, band never number, never the trigger. Knowability is a **gate composed
before ranking, never traded against salience** (`10:364-366`), enforced by five checkable witness
channels; mandatory rows bypass ranking but not the gate. A P-08-barred situation arrives **thinner,
not suppressed** — inaccessibility, not suppression, which is canon's own falsifier wording. The one
ruled exception runs the other way in full daylight: caste exclusion is published with institution,
post kind, caste and unmet predicate, because concealing the injustice would be worse than revealing
the mechanism (`04:269-277`). Misperception is representable; and the filter is honest by construction
— shaded candidates resolve bit-identically on per-candidate substreams (`10 part2:55-96`), so the
engine cannot secretly favour what it showed you. **This is the strongest anti-narrator architecture in
the tree.**

## T4 findings

1. **[BLOCKER] Every NPC decision function reads world state directly; none reads the actor's Holdings
   — the player is the only epistemically limited actor in the design.** Five functions traced by
   reading: `appeal` reads ethos, holder convictions, `signal(s, world)` and `custody_bias`
   (`05:304-315`); `preference` reads a conviction dot product, `qualification_margin`,
   `disposition_value` and Leverage/Debt tags (`04:390-394`); `accepts` mirrors it (`04:332-344`); bloc
   formation reads holders' *true* conviction distances and the *true* edge graph (`06:300-309`);
   `09`'s advance terms are predicates over *world* state (`09:196-211`), so an NPC's project advances
   on truth, not on what its owner knows. Meanwhile `01 §3.4` binds *"every selection function"* to
   carry the capped Holding bias, and `01 §4.3` promises *"a holder's convictions **and beliefs** rank
   the remit's contents"* — but the only consumers of `Holding` are the Slate renderer and the
   belief-revision transitions. **NPCs cannot be deceived, misinformed, or surprised.**
   *Authors would dispute*, citing ED-IN-0201's *"same option set with the same information"* — but that
   defence concedes T4 rather than answering it: "same information" is implemented as **total**
   information for NPCs while the player gets bands and hidden triggers, so the asymmetry runs opposite
   to the throughline. — **structural**

   > **Upgraded on request, by reading rather than matching.** Contract blocks in `04`, `05` (both
   > parts), `06` (both parts), `09` (both parts) and `12 §5` were opened: `04`'s formulas enumerate
   > their tag terms **by kind** (`Leverage or Debt`, `Debt or Grudge`), so a `Holding` cannot enter
   > through the generic slot — the kinds are closed at the call site. Two self-corrections resulted:
   > (a) the `tag existence` term kind **could** legally express a belief-reading advance term, since
   > `Holding` is a tag kind — no declared kind does, so the claim is *"expressible, unwired"*, not
   > *"impossible"*; (b) `02 §6` **is** a real NPC-side Holding consumer, but it governs what an NPC
   > *believes*, never what an NPC *does*. Final wording: **no action-selection function in the suite
   > takes a belief as input.**
   >
   > **What the original grep would have missed, stated so the negative is honest:** lowercase
   > `holding/holdings` in prose; the synonym family the suite itself uses (`belief`, `creed`,
   > `credence`, `confidence`, `prop_id`, `stance`); a generically-named term inside a weighted sum (a
   > `signal_weight` row named e.g. `perceived_weak_neighbour` carries belief with zero token overlap);
   > an accessor wrapper on the `disposition_value` pattern, which the suite already uses to hide
   > storage class; a string-resolved call through `composition.require("npc_memory")`; future registry
   > rows, since advance terms are data rather than prose; and the engine's own spelling,
   > `Belief`/`position` in `beliefs.py`, which matches `Holding` nowhere.
   >
   > **Engine side, checked because no other critic covered it.** `systems/characters/sim/beliefs.py`
   > is real, not a stub: per-actor `Belief` rows with `position ∈ strong/wavering/revised` (`:49-58`),
   > entry points `add_belief` (`:121`), `revise_belief` (`:140`), `social_success` (`:189`). It is
   > **live with zero importers**, reached by string through composition role
   > `snapshot_state.beliefs → systems.characters.sim.beliefs:Belief` (`module_contracts.yaml:142-143`)
   > — but the roles that reach it are **storage/snapshot, not decision**. Its only decision-bearing
   > effect today is +1 Momentum on a belief-aligned social win (`:210-219`). And the shipped NPC
   > strategic chooser, `faction_action.py:208-273`, re-weights four buckets from signals that
   > dereference `world.territories`/`world.factions` truth directly. **The omniscient-NPC shape is not
   > merely proposed; it is current shipped behaviour.** *Located, not verified:* whether
   > `contest_legacy_stub.py:29-32`'s belief→Momentum channel is invoked by any live path.

2. **[BLOCKER] `information` — the one gauge about not knowing — has two declared owners, no scale, no
   knower, and three inert guards.** `05 part2:168-181` deposits *"on the target"*; `01:527` declares
   owner **faction**; `05 part2:718` asks `01` to declare it `(target, 0–5)`. With no scale, `H_MIN`,
   the fixed-point falsifier and the commensurability gate are all inert (`01:540-544`). Structurally
   worse: a knower-less gauge on the target means faction A's inquiry raises the band that unlocks
   `requires_information` rows for **B, C and the player** — knowledge stored as a property of the thing
   known. The suite's own argument kills this shape: *"a person gauge needs a key, which is an edge with
   the naming hidden"* (`01 part2:118-121`, for `allegiance`). Information is exactly as dyadic and got
   no key. — **structural**
3. **[DEFECT] `signal(s, world)` is an unenumerated open read in the suite's most-executed decision
   function.** The schema is `signal_weight: {<world signal>: <weight>}` with no closed list
   (`05 part2:33-34`); examples include reading a distant neighbour's weakness with no witness,
   disclosure class, or scale constraint. `09 §3.1` closes its own term list *"because an open one is
   where a predicate grammar becomes a scripting language"* — `appeal`'s signals are the same object
   left open, and they are precisely where NPC omniscience is implemented. — **omission**
4. **[DEFECT] `tie_proximity_bp` collides with covert state under "publish every input."** It is derived
   from the shortest path in the **full** edge graph (`10:445-449`) and `sl.rank` publishes score
   components. Either the published proximity component exposes a path through an edge the player cannot
   know (covert Niflhel patronage; a secret `allegiance`), or the component is withheld and E-2 is
   breached. No edge-level covertness mechanism exists anywhere in the suite. — **structural, unresolved seam**
5. **[GAP] The player's information limit is one open ruling away from being pure rendering.** P-A makes
   shaded candidates resolve bit-identically; the only designed cost of ignorance is played-fidelity
   branch selection, and O-10.3 records that under a strict-parity ruling *"§6.5's premium becomes zero"*.
   In that world, ignorance costs nothing anywhere except `information`-gated option sets — broken per
   finding 2. — **structural dependency, already ledgered (ED-SC-0024/0026)**
6. **[GAP] "Arrives thinner" has no mechanism, and its falsifier tests the opposite.** `10:406-409` says
   a P-08-barred candidate *is cast* with the Thread-level payload absent — but the candidate row has no
   payload field and no thinning operation, and claim 7's test asserts no Thread-constituted candidate is
   cast at all. **The test forbids the designed behaviour.** — **wording + omission**
7. **[DEFECT] `exposure` re-coins a canon term with different semantics** (**X-4**). T4's angle: canon
   keys *who has noticed you* per territory; the suite's scalar makes being-known ownerless — the dual of
   finding 2. — **structural**
8. **[NIT — soften, already disclosed] `forecast_mass` is unproduced, but the vacuity is half the
   *depth* layer, not half the render layer.** Membership, truncation, responses and the derived
   `imminence` band all function; one multiplicand of `depth_score` is constant. The document says so
   accurately at `10:490-493` and `10 part2:462-468`. Escalating this would manufacture a finding the
   text already owns.

---

# T5 — Granular actions, demands and choices radiate and aggregate upwards

**Verdict: PARTIAL.** The elite chain genuinely composes; the popular half is statically unreachable,
and the filtering half is done by the player-attention system, not the political ladder.

## T5 steelman

Architectural, not additive. AU-1 forces every upward read to be a derivation, so aggregation cannot
drift from its constituents. `06 §4.2` makes scale a **parameter**: `footing(faction, node)` is one
function summed over a node's subtree, adopting canon's calibrated, saturating `T/(T+K)` verbatim.
**Saturation *is* principled filtering** — `W_s` weighting plus diminishing returns means the Nth
hamlet's demand legitimately vanishes at territory grain — and `RELATION_SHARE_MAX` guarantees
individual feeling biases but never substitutes. Composition upward is demonstrated end to end for
officers: a passed-over candidate's Grudge feeds cohesion deposits, grudged officers connect into a bloc
over PP-724's edge graph, the bloc's pull against ethos gates schism, and schism charters a faction whose
ethos is the frozen practice of the dissenters — **individual grievance coalescing into institutional
rupture with zero special-casing.** `09 §6.4`'s auto-declaring `rising` extends this below the
post-holding class; `12 §5.2` carries the same discipline to the peninsula rung.

## T5 findings

1. **[BLOCKER] The mass actor cannot fire** (**X-3**). `rising`'s `required: true` term
   `tag(place, Precedent, key=legitimating.*)` (`09:612`) has no producer in the 18 files. `08`'s Defy
   deposits *"a Precedent tag on the place"* but declares no key; `11` appends Precedents but never this
   one. The suite's own standard condemns this exactly — v2's `found_settlement` gated on a module that
   could never exist, *"a row that cannot bind looks like coverage"* (`09:528-536`) — and **the static
   falsifier built for that defect checks modules and post kinds named in gates, not tag-key patterns in
   advance terms, so it structurally cannot catch this one.** Resentment → revolt is dead at the first
   hop. — **structural**
2. **[DEFECT] Individual resentment does not aggregate below the post-holding class.** `rising`'s terms
   read only place-owned state; the closed term grammar has **no quantifier over persons** — no term can
   say *"N residents hold Grudges"*. Person-owned Grudges deposit into no place gauge;
   `acceptance.legitimacy` has one depositor by the document's own admission; residents are a derived set
   whose stake is routed to two scalars plus Local Actors, of which most places seed exactly one
   (`03:104`). The coalescing path exists for officers and does not exist for populations — the rung the
   throughline's "individual resentment" names. — **omission (structural in effect)**
3. **[DEFECT] The filtering half is done by the attention system, not the political ladder.** The Slate
   filters what reaches the *player*; no tier-level analogue exists. **There is no upward demand object
   at all** — `08`'s up-stroke is retired into `05` rows, directives run downward only, and NPC attention
   is the unstructured `signal(s, world)` term. A settlement-scale demand is never *dropped* at territory
   scale because it can never be *raised* — filtering by nonexistence. The cost: the only expressible form
   of *"this town demands a new governor"* is a completed insurrection, since `rising`'s fire is
   `post_revoke` — **nothing between silence and revolt.** — **structural**
4. **[DEFECT] Q-5's local-disjointness claim is checkable only per document** (**X-7**). The falsifier is
   scoped to *"no module in this document"* and carves out `fm.posture`'s deposit — itself the D.6 overlap
   shape. Cross-document flows are outside the check entirely: `fm.fisc` lifts `residual(place)` into
   treasury, `05` spends it on musters whose campaigns deposit back into the place gauges that next
   boundary's residual and `W_s` read. And `01 part2 §9.2`'s obligation that every herald declare *which
   channel carries the magnitude* has **no field** in the `00 §7` schema — `emits:` carries only
   `{type, terminal}`. **An undeclarable declaration is a discipline, not a mechanism.** — **structural**
5. **[DEFECT — the finding the authors would dispute] `Precedent` is three objects in one kind:**
   institutional memory, machine trigger, and the suite's *de facto* cross-document transport —
   `founding_claim`, `failure_mark.*`, `legitimating.*`, `rising.suppressed`, lapse residues. The `key`
   field does type-system duty and **no registry owns the key vocabulary**. The authors would call this
   the disclosed J-N-compliant pattern (*"the gate reads state left behind"*); the dispute fails on
   consequences — two documents already coordinate a key string by prose with no check, and an unowned key
   namespace is precisely how finding 1 shipped. — **structural**
6. **[GAP] There is no community rung, and canon has one** (**X-8**). `settlement_layer_v30.md:171`:
   Restoration *"operates at the **community** level via Presence markers"*. The suite flattens community
   into institutional presence gauges and strata (claims on yield); the bloc is elite-only by construction.
   **T5's ladder starts one rung above where the throughline does.** — **omission** → escalated to **J-2**
7. **[GAP] The suppression-backfire ratchet hangs on a check that does not exist.** `09 §6.4` concedes
   re-arming is reached only by a successor kind and *"puts real weight on the successor-graph acyclicity
   check §13.1 records as not existing"*. Disclosed honestly — but it gates the only composition path the
   mass actor has, stacking under finding 1: an unreachable kind chained to an unguarded cycle. — **omission (admitted)**
8. **[NIT] "rising" now has two suite meanings** — the project kind and a gauge band label
   (`11:570`). `00 §7.1`'s rename rule binds and was not applied. — **wording**
9. **[NIT] The three reused project key types are registered `[personal]` scale, `emitting_systems:
   [npc_behavior]`.** A place-owned settlement-scale rising emitting through personal-scale, NPC-only types
   is unaddressed. — **omission**
10. **[NIT / in the suite's favour] The rung collapse is verified.** The brief named territory and
    province as separate rungs; O-5.6's collapse is correct against `settlement_layer_v30.md:151`, and the
    mechanism is rung-count-agnostic, so a later ruling costs one registry row. The producer's arithmetic
    citations held up everywhere checked. — **wording**

---

# T6 — Large actions ripple downwards in scale

**Verdict: PARTIAL.** Real and well-owned from faction policy to place gauges, and it reaches
post-holders and the player; for anyone holding no post the last hop is unfilled schema.

## T6 steelman

A lattice, not a pipe. The herald makes distribution **data**: one Key, N `targets[]` entries, each
carrying the deltas *that receiver* gets, with rule 2 reserving the felt magnitude to the receiver —
*"whether a fact scars a person depends on that person's convictions"*. `08`'s directive is an addressed
order a **named governor** answers, and every response deposits into that person's own
`standing`/`exposure` and tags them — **the policy literally lands on a man.** `07 §5` gives institutions
a material claim on a place's yield, so `act.contest_influence` has stakes a person can lose. Place
improvement creates person opportunity through form: prosperity feeds growth, growth sites a governor
post, vacancy demands a candidate or generates a person, and presence buys individuals *eligibility*.
`sm.business` closes the loop — a policy's residue becomes next season's business, scored by
`identity_touch`, cast into a scene where a person grieves. `09 §6.4` gives the governed a route to
unseat a governor. **Individuals are the joints of every hop.**

## T6 findings

1. **[BLOCKER] A person who holds no post cannot receive an opportunity through the only opportunity
   mechanism the suite has.** `am.declare` costs a point of the owner's **post** budget and requires a
   remit; auto-declare exists **only** for `entity_kind: place` — *"hysteresis: REQUIRED for
   entity_kind: place, **forbidden otherwise**"* (`09 part2:173-177`). This is byte-for-byte the
   registry-ghost structure `09 §6.4` prosecutes for place-bound kinds, left standing for
   `entity_kind: person`. The ~45–50 Local Actors and all residents are **structurally excluded** from
   "getting excited about opportunities." — **structural**
2. **[DEFECT] Even for post-holders, the opportunity channel is unexercised:** *"there are no rows"*
   (`09 part2:351`), so no `owner_binding: person` kind with a term reading a place's prosperity exists
   anywhere. T6's last clause is currently **unfalsifiable** — the schema admits it and nothing
   instantiates it. — **omission**
3. **[DEFECT] Treaty trace stops at the edge.** `12 §4`'s terms are `Debt` tags owned by the edge; no
   mechanism converts a tribute clause into a place deposit, and breach detection *"belongs to whichever
   module enforces that clause — 05, 06 or 08"* (`12:405-407`) — **three candidate owners, none
   assigned.** Missing hops: edge→place *and* place→person. — **structural**
4. **[DEFECT] Blockade trace stops at an unread tag.** `we.route_severed`'s only deposits are
   `Precedent key: "route_cut:<place>"`; the row admits it *"does not own route-cut storage"*. `07`'s
   yield formula carries no route term and `route_cut` appears nowhere in `07`. **A blockade does not
   reach even the place's economy** — it dies two hops above a person. By the suite's own W-6 standard, a
   subscription with no rule content is decoration. — **structural**
5. **[DEFECT] The Q-5 exception hides an unbounded loop, not a double-count** (**X-7**).
   `fm.posture` deposits into `acceptance.support` every season held; footing reads those same gauges;
   footing gates posture changes. §11.1's "one declared, named exception" answers *double-counting* — a
   cost is not a re-derivation — but the **posture→support→footing→posture-gate feedback loop appears in
   no row of the loop table.** — **structural**
6. **[DEFECT] The suite's "only measured loop bound" is a measurement of a different experiment.**
   `06 part2:310` marks footing↔acceptance MEASURED, citing canon's 30-season sim — which measured the
   **coupled** system including canon's stabilizing Mandate→L/PS drift that the suite **did not adopt**,
   and **excluding** `fm.posture`'s per-season deposit that the suite **adds**. Different arms;
   `CLAUDE.md` §0.1 point 4 binds in both directions. *Authors would dispute*: the exception is declared,
   the deposit is a bounded gauge flow, and `T/(T+K)` damps everything. **Reply:** a declared exception is
   not a bound, the drift they didn't adopt is part of *why* canon's sim converged, and a stability result
   does not transfer across a change in feedback structure. — **wording/structural**
7. **[GAP] Verified in the tree: `targets[]` is populated today only upward.** The schema and the
   one-Key-N-targets rule exist (`keys.py:88-94`); the only production populators are
   `echo_transport.py:330-331` (scene→settlement) and `:432-433` (scene→faction). **Zero down-stroke Keys
   populate targets** — consistent with the "eight declared down-seams that populate nothing". — **omission**
8. **[GAP] `residents` conceded — argued both ways, then ruled.** *For:* `07:459-462` is honest
   distillation; a second population accounting channel would be under-distillation; Local Actors are the
   population's named sample; `acceptance.*` is its aggregate mood. *Against:* the concession only works
   if the named sample can **act**, and per finding 1 it cannot — Local Actors have a Disposition field
   **nothing at place scale ever writes**, and the rising is owned by the *place*, contains no individuals,
   and fires a post-revocation. **Ruling: the one line at `07:459` is where T6 is conceded** — defensible
   only if finding 1 is fixed. — **structural** → contributes to **J-2**
9. **[NIT] `08 §5`'s row-1 gloss implies NPC initiative that does not exist:** the candidate's
   `responses` are filtered by *the player's* remit, so the "someone" is the player or a scene cast for
   them. The genuine AI-side person-hop is `appeal` reading each holder's convictions — real, but an
   **up**-stroke. — **wording**
