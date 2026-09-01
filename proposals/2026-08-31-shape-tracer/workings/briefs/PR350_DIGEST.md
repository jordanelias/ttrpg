# PR #350 — THE IDEAL UNIFIED CODE SHAPE: orientation digest

Merged as commit `647fbdf` on 2026-08-31. Lives at
`/home/user/ttrpg/proposals/2026-08-31-unified-code-shape/` — 17 numbered documents plus
`ADVERSARIAL.md`, `TRACE_REGISTER.md`, `MANIFEST.md`, `dossier.txt`. 10,619 lines, additive only.
**Status: PROPOSED, HELD BACK IN FULL. Nothing ratified on merge. Nothing in it executes.**

This digest is ORIENTATION, not authority. Verify every claim against the file before relying on it.

## SCOPE, AS THE SUITE ITSELF DECLARES IT
In scope: the **season loop**, **world churn**, **emergent narrative**, and **persons/the player** as
the throughline. Explicitly out of scope as systems: personal combat, social contest, mass battle —
they appear only at `09_THE_SEAM.md`, four pages, specifying attachment and nothing internal.

## THE ARCHITECTURE
```
Person · Rung · Office · Site        four carriers — identity-bearing, MUTABLE
Proposition                          fifth identity-bearing record — IMMUTABLE
Tenure                               THE one edge · seven kinds · cardinality on the schema
StateChange := (subject, mode, driver)   mode ∈ create|alter|destroy   driver ∈ Act|Event
Query                                never stored, always recomputed

Claim       what a person holds TRUE    — moved by EVIDENCE, at WITNESS
Conviction  the moral AXES (13, closed) ┐
Belief      what a person holds RIGHT   ├ moved by ARGUMENT and CONSEQUENCE, at RESOLVE
Duty        what a person OWES          ┘  — an `oblige` Tenure; no new record

choose  : (Person, View, Sensation) -> Act     NO World, ever
resolve : (Act[], World)            -> Event[] NO Person
witness : (Person, Event)           -> Claim[] per person; a collection is not spellable

CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS
  nested in the running tick: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY
Write classes: CALENDAR · MATTER · ACTS · INTERIOR (a class is not a phase)
```

### THE FOUR LAWS
1. **The person is the only actor.** No faction verb, no settlement speaker, no clock that acts. A
   cohort is a Person at `weight > 1`. "No leader, no faction action" (Jordan) — a campaign with no
   people performs zero faction actions.
2. **Nobody is omniscient, and the signatures are how** — by what they OMIT. `View` is a distinct type
   from `World`, **built not filtered**; absence produces absence, never a widened interval
   (ignorance, not uncertainty). In GDScript the guarantee degrades from *unwritable* to
   *unreachable-by-name*, and the suite says so.
3. **Every aggregate is a function, never a field.** Nobody owns an aggregate. No stored unrest,
   legitimacy, reputation, cohesion, norm, density, footprint, presence, mandate. R-1: a rung may
   compute an aggregate over descendants on demand, may not receive a pushed one, may not store one.
   R-2: a rung writes only its own state. One concession: a Query MAY be cached at a barrier,
   read-only until the next, discarded there.
4. **Every state change is partitioned by its subject**, and the membership test is a static schema
   column `social: bool` keyed on `(record-kind, field)` — ASYMMETRIC: `social:true` ⇒ act-driven
   only; `social:false` ⇒ either driver. Worked case: a plague may empty a village and may not
   destroy it; only an office strikes it from the roll.

### GOVERNANCE / FACTION / SETTLEMENT SPECIFICS
- **The Faction row is DELETED from the ownership table.** A faction IS a `Proposition` (mood `OUGHT`)
  plus its `commit` edges. Membership = `commit`; leadership/presence/density/footprint = Queries;
  identity = the immutable Proposition; institutional memory = Records at a Rung. A faction collapses
  when people leave, with no dissolution mechanism. Scale is DERIVED as a presence/density/footprint
  profile — never a `tier`, `level` or `scale` field.
- **A Proposition of mood `OUGHT` is an uttered Belief** — so a faction is somebody's morals, said out
  loud, that other people signed. Enables the hypocrite and the founder-discredited-movement.
- **Rung ladder, eight kinds:** `person, hearth, community, settlement, territory, province, duchy,
  realm`. `hearth` is the code-side name for Jordan's `family`. Both `province` and `duchy` retained.
- **Office** := `(id, post, rung?, remit, conferral, revocation, establishment[], dates[], upkeep)`.
  `rung?` optional (office-cluster case: dicastery, chivalric order, trans-settlement guild).
  `remit.acts[]` from a closed five: `issue · determine · confer/revoke · dispatch · convene`.
  **An office adds NO verb** — it makes ordinary acts eligible and substitutes the pool source.
  Who holds it is a `hold` Tenure owned by the holder, never a field on the Office.
- **Site** := `(id, rung, kind, condition, drawers[])`. `condition` is PRIMARY state, fixed-point on
  `COND_SCALE`. Base case: a Rung with no Sites has UNDEFINED condition and the verb gate does not run.
- **Deposition** is `leaders()` returning somebody else next season — no deposition subsystem.
- **`annex`/`secede` are deleted from the vocabulary** — covered by `confer` on `hold`.
- **Migration cost, priced:** the running tree ships a faction stat-bag (six stored floats + standing,
  territories, per-arc flags) written at **31 non-test sites, 30 of which bypass the event log**.
  Path is build-beside → flag-gate → golden-control → cut over. Not a base to refactor.
- **Measured dead state:** a settlement's `legitimacy` and `popular_support` are never read, never
  written; the peninsula's `Turmoil` clock is initialised once and never written again, read at one
  site where it makes a victory condition's stability term unconditionally true; a faction's `intel`
  is unreachable (no multiplier-table entry, a write raises).

### WORLD CHURN (05)
- Jordan's flux ruling: the world's trajectory is an **OUTPUT** — `sum(acts)` against `wear`.
  Nobody tends ⇒ it dies and no person did it. Everyone tends ⇒ it thrives. Some tend ⇒ the
  distribution decides which sites live, and that is the game. Cost: one constant, zero objects.
- `wear` per site kind, same units as `condition`, MATTER class; act deltas at RESOLVE; ONE clamp
  after both. **The `wear` : restoration ratio sets the entire difficulty curve and is UNMEASURED.**
- **The world-substrate hole** (found by three independent arc lanes) closes as a `Site` kind whose
  `condition` is the substrate quantity — zero new objects. Falsifier: wrong if the metaphysics needs
  one global scalar with no site identity.
- **Trigger purity:** an event row's trigger may read only `social:false` rows plus terrain and season,
  never a social quantity. The shipped event deck violated this — every card gated on a composite
  pressure quantity three of whose four summands are social.
- **Persistence is a Record with a `ttl`, never a scheduled future event** — the substrate has no
  cross-season transport. A three-season drought is three re-evaluations of a gate.
- **An off-board polity is an event source, not a simulation.** Agentive actorless rows are
  **specified and GATED** until a criterion exists that stops any actor being reclassified as weather.
- **Exactly three quantities are clock-driven: matter, bodies, and the confidence of a memory.**
  Standing, regard, grievance, cohesion, commitment move only when an act causes an event. A governor
  loses the town by being **forgotten** — claim confidence decays.
- Churn ledger: 14 rows, each with its N-line. The suite retracts its own earlier "there is no
  thirteenth" as under-enumerated (individuation and claim eviction were missed).

### EMERGENT NARRATIVE (06)
- **A story is a provenance chain read backwards.** `causes[]` on every Event. An arc is a projection,
  never a maintained structure. No arc object, no arc state machine, no arc registry, no quest object.
- Scored against a 55-arc corpus by three lanes: 40 REPRODUCED-BETTER, 2 REPRODUCED, 22 TRANSFORMED,
  10 LOST, 9 NEVER-WORKED. The suite CORRECTS its own draft: the ten LOST are **not one loss** — five
  die on the world-substrate hole (closed), two on an off-board actor (gated), one on a closure axis.
- **Ambition** = a Proposition (`OUGHT`) + `INTENDS` claims + progress **derived at read** over
  ordinary world terms. Therefore **obstruction needs no verb** — a stranger who takes your seat has
  obstructed you without knowing you exist. Published as bands, never numbers, never a forecast.
- **The Slate**: `gate THEN rank`, never summed. Cast gate = knowability via **five witness channels**
  (`post_remit · co_located · witness_key · document_key · chronicle`), no sixth. Rank = `cast_score`.
  `depth_score` governs render depth, NEVER entry. `forecast_mass` is CUT — no producer anywhere.
- **The funnel: ~190–200 candidates resolve per season, 6 reach the slate, 4 are acted on.** The player
  sees ~3% and acts on ~2%; 100% resolves. The surplus is the point.
- Candidate contract C-1..C-6: provenance required · witness required · realized-state terms only ·
  `resolver_ref` resolves at both fidelities · 3–5 responses from a declared option set · an emitter
  emits and never presents, ranks or checks budget.
- **No convergence check exists.** "The sharpest unmeasured claim in the suite" — nothing measures
  whether confrontations arrive at all. The suite deliberately proposes no instrument for it.
- 19-row narrative ledger of emergent opportunities, each two or three primitives meeting.

### THE PLAYER (07 / 01 §3)
- **There is no player model.** Same `choose`, same one-act budget, same no-World. The player's only
  advantage is deliberation time. Fidelity (`played`/`witnessed`/`auto`) is a **camera, never a
  formula** — identical resolver, rolls and seeds. A second resolution path is refused (the genre's
  twenty-year unsolved divergence).
- **A person holding no office can act, petition, investigate and receive an opportunity.** Office
  changes whether a decision BINDS others, never whether you may act. What an ordinary person holds
  that is scarce: a **channel**, a **custody**, a **gate**, or a **unique root** — and that
  correlation, not rank, predicts whether a season is worth playing.
- `opening_set` is CLAIM-derived, recomputed from need + capability + terms they hold a claim of.

### KNOWN OPEN / WEAK (the suite's own list — `02` §10, `15` §3)
1. the `wear` : restoration ratio (unmeasured) · 2. `leaders`' comparator · 3. where the channel store
lives (plausible past) · 4. the cohort's construal spread representation · 5. `World`'s record ·
6. the agentive/non-agentive split (gated) · 7. the testimony half of the salience floor ·
8. **`destroy` is NOT cleared against the refusal rows — the hole is inherited, not closed** ·
9. age-band boundaries, channel latency, `season_factor`'s distribution.
Escalated to Jordan (survived all five tests): which seats a campaign OFFERS at start · state
ownership and the autoload table · the save model · the engine version (4.3 vs ≥4.5).
Also: `12_TESTS.md` specifies four structural claims that have NEVER been run; `13_EXECUTION.md`
names the ordered build; `11_PARAMS.md` grades 11 of 25 parameter rows ASSUMPTION.
