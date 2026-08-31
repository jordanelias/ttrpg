# THROUGHLINES OF THE 2026-08-31 SESSION — Fable-5 identification brief, v2
# ⚠ SUPERSEDES the v1 brief entirely. V1 named nine throughlines about the REVIEW METHOD. Jordan:
# "Throughlines should be about the design and code." The method observations are demoted to a single
# closing section; the twelve below are about the GAME and its CODE SHAPE.
# Nothing in this session executed. Every claim is an argument about text.

## D1 · EXISTENCE AND TENURE WERE THE TWO REGISTERS THE DESIGN COULD NOT TOUCH
The design could change the STATE of everything and could barely change **which things exist or who
holds them.** The proof is a five-item list — the only operations in 2,017 lines that change existence
or tenure are death, de-individuation, claim eviction, individuation, and holdings-on-death. **All five
are decider-free; four are subtractive.** In a design whose thesis is that every active decision is a
character's, no character could add or remove an object from the world.
**Consequences that all traced to this one gap:** no birth · no character generation · no caused
advancement · nothing creates a Site, Container or Office · no faction can be founded · no tenure
relation over sites or nodes · `holdings` is dead state no act reads.

## D2 · THE DESIGN HAD ONE EDGE PRIMITIVE AND SPELLED IT THREE TIMES
`Holding := (person, office, since, conferrer)`, the commitment edge `commit(person, faction, Δdegree)`,
and the hearth's succession pointer are one shape — and §4.2 already filed two of them in the same table
cell. Generalised to `Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?)` over
seven kinds, **with `confer`/`revoke` already in `remit.acts`**, four previously-unreachable operations
fall out with no new verb: appointment and dismissal, enfeoffment and confiscation, annexation and
secession, and the loss limb of every one.
⚠ **`until?` is what makes a REVOKED tenure a fact people can argue about.** Without it the record
carrying every disputable political fact could not be a claim subject — the design's thesis did not
reach the object the politics is made of.

## D3 · POWER IS A QUERY, NEVER A FIELD — and this is the design's deepest commitment
Nothing stores control. A faction is a proposition plus the `commit` edges pointing at it; leadership is
`leaders(observer, faction, rung)`; sovereignty is a reachability query; scale is derived and gates
nothing. **Deposition therefore needs no verb at all — it is the query returning someone else** when
members commit away or backing collapses.
⚠ **The query must take an OBSERVER.** Typed without one it is a read of the true profile, which nobody
may perform — the same rule that forbids reading a faction's real membership.

## D4 · THE PARTITION — the subject of a state change decides its driver
> **Peninsular human society** — polities, institutions, offices, organizations, occupations, religion,
> settlements, marriage — **is changed only by a character's choice. Every other subject** — weather,
> the non-peninsular, the metaphysical substrate — **is changed by an event acting on the world.**
It replaced an enumeration of four licensed channels **that had no membership test**, which is why that
list was wrong three ways at once: matter events licensed with nothing generating one, `wear`
unwritable, a 58-card deck with no home. **It also makes no-fallback true instead of approximately
true: if no person acts, no SOCIAL thing occurs.**
**Its first test reclassified four-fifths of a shipped deck in one pass** — 21 of 26 impact types are
social and therefore forbidden to an event; of nine full card records, zero are events.
**The extension — creation and deletion are state changes — moves `mint`/`efface` off `Act` onto
`StateChange`, so events create and destroy within their half.** A landslide exposes a seam.
**The worked case that proves it does real work:** a plague may kill bodies but may not efface a
settlement, so the village empties and **still legally exists until an office strikes it from the roll.**

## D5 · THE WORLD'S TRAJECTORY IS AN OUTPUT, NOT A CONSTANT
Neither dying nor misunderstood: **in flux.** `condition ← clamp(condition + Σ tending − wear, 0, 1)`.
Untended it falls to a band floor and verbs leave — **the world dies and no person did it.** Tended by
enough people it holds or climbs. **The fork's missing option was a SIGN, not a parameter**, which is
why five audits could not dissolve it.
**And it converts the act economy into the load-bearing scarcity of the whole game:** under an act-only
fuse restoration was pure gain and neglect was free; under `wear`, maintenance is a permanent tax, so
*how many person-seasons does this harbour cost to keep open* becomes a real contested quantity.

## D6 · BELIEF AND TRUTH ARE TWO FUNCTIONS THAT WERE SHARING ONE NAME
`choose` takes no `World`, yet a person must know their options, and the option set reads hidden world
state. The resolution is a split, not a new primitive:
> **`verbs(site, rung)`** is **world truth**, read only by `resolve`. **`opening_set(person, view)`** is
> **belief**, computed inside `choose` from the person's own ledger.
**So a person may attempt a verb the world has already removed, and discover the harbour silted.**
Better fiction than a menu that greys out, and the design already argued for it — *"the people who
notice first are the ones whose practice used that verb."*

## D7 · THE EPISTEMIC LAYER WAS ALREADY RIGHT, AND ITS PROBLEM WAS NEVER MECHANISM
#342 shipped the claim, a **closed fourteen-form predicate vocabulary**, view assembly under a budget,
salience with a defined `relevance(c,q)`, corroboration that fails closed, concealment, **and six
investigation acts with pools, products and costs**. What it lacked was **enough happening to disagree
about** — and every enlargement this session kept is a fact factory feeding it.
⚠ **This session twice claimed parts of that layer did not exist. Both claims were false.** The layer's
own owner-document was never read.

## D8 · ENFORCEMENT BY OMISSION DEGRADES TO ENFORCEMENT BY CONVENTION IN THE TARGET LANGUAGE
*`choose` has no `World`* and *a consensus broadcast is a type error* are guarantees in prose and
**unenforceable in GDScript** — no module system, no visibility modifiers, autoloads global to every
script, and the port's own skeleton already reaching `GameState` from inside a resolver module.
> **What survives is nearly as strong and must be stated as the weaker true thing:** put **no live world
> state behind any global name**, and give **every resolver-side query an explicit `World` first
> parameter**, so calling one from `choose` fails at the call site for want of an argument. Enforcement
> by omission goes from 3 signatures to 23 — *unreachable-by-name*, not *unwritable*.

## D9 · ONE ACT PER PERSON, AT EVERY RUNG, AND THE ESTABLISHMENT CARRIES THROUGHPUT
The word *act* was doing two jobs — **personal attention**, identically scarce for a Duke and a fisher,
and **institutional throughput**, which scales with the people an office employs. The design already
moved the *pool* for an act-by-remit onto the establishment and left the *act* on the holder.
**A Duke takes one act — `dispatch` — and thirty-five named people each spend their own deciding what to
do about it.** Same allowance, incomparable reach. **And the cohort exploit prices itself:** individuate
to farm acts and you have created eleven people with ledgers, stances toward you, and the standing
option to refuse.

## D10 · COHORTS MUST ACT, OR THE POLITICS GOES ELITE-ONLY BY CONSTRUCTION
A cohort is **persons at coarse fidelity — one type, not two** — and it commits one act per season like
any person. ⚠ **Replacing it with a demographic envelope makes population MATTER, and matter does not
act**, so everyone outside a handful of notability triggers stops deciding, and every derived faction
becomes elite by construction — including the dynamically generated replacements for collapsed royal
ones. **The envelope is the inflow reservoir for minting and nothing more.**

## D11 · A NAME MUST BE CHECKED AGAINST THE TARGET ENGINE AND THE LOCAL CORPUS, NOT ONE OR THE OTHER
`Node` collides with Godot's scene-tree base class. `Container`, chosen *to fix that*, collides with
Godot's `Control`-derived UI base — **and collides worse**, because `Node` fails loudly while
`Container` shadows. `Derived` collides with this repository's own glossary, where it means **stored**
values — the opposite. Settled: **`Rung`** and **`Query`**, both already in the design's own prose.

## D12 · IDS, NOT POINTERS — and the reason is one the design did not know it had
Objects reference each other by id. **Godot has no cycle collector, and the design documents reference
cycles as normal, so a `RefCounted` cycle is a permanent leak.** The design is right for a reason it
never states, and **the first Godot-fluent reviewer will suggest exactly the edit that breaks it.**
Ids also mint from the determinism substream `(world_seed, tick, subject_id, purpose)`, which gives
unique order-independent ids **with no shared allocator** — the thing that would otherwise break the
per-person maps' parallelism.

---

## CLOSING SECTION, NOT A THROUGHLINE — how these were arrived at, and why to distrust them
Kept to one section deliberately. Every audit in this session checked **derivative documents against
each other** and none swept the corpus: **108 of 123 proposal documents over 200 lines are cited
nowhere**, four mechanisms were reinvented that already shipped, and **every false claim the session
produced was an absence claim** — *"there is no X"* — because that is the only error a derivative-facing
audit can make. Both discoveries were Jordan's, not any audit's. **So D1–D12 are claims about the
documents that were read, and the read set is a minority of the corpus.**
