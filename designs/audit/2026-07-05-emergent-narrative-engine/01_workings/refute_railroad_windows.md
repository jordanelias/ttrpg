# Refutation lane — C7 RAILROAD adversarial audit

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Role: try to BREAK the synthesized Arc-Vector Engine on C7. Working tree only; every claim cites
file §section or is tagged [UNGROUNDED]. Charter C7 =
`00_engine_charter.md:40-41` + Q1 anti-railroad proof `:54` + Q2 history-modes `:75-79`._

---

## What C7 actually demands (four testable sub-properties)

From `00_engine_charter.md:40-41` (C7) + `:54` (Q1 proof) + `:75-79` (Q2 modes):
1. **Windows real** — "a different choice at EACH engagement window measurably changes trajectory"
   (`:54`). Note **EACH**, not once.
2. **No over-orchestration** — director may not shape trajectory toward a predetermined dramatic
   shape.
3. **Pricing preferred over gating** (`:41`, `:76`) — "Obligations price betrayal, don't wall it."
4. **Non-participation autonomous, no rubber-banding** — "unattended arcs proceed autonomously…
   ignoring a summons is remembered, never a pause" (`:52`, charter Q1 `:50-54`).
5. **Foreclosure via arc events only, never silent, surfaced in chronicle** (`:41`, `:77-78`).

I test the synthesis (`synthesis.md`) against each. The spine (Architecture B) is not the problem;
**C7 is asserted at the charter/capstone level but not ENFORCED by the six-rule conformance suite
(`synthesis.md:260-270`).** Every finding below is a missing enforcement or a grounding error, not
a reason to reject the spine → verdict SOUND-WITH-FIXES.

---

## Finding 1 (BLOCKER-adjacent → MAJOR) — windows proven ONCE, guaranteed NEVER

Charter `:54` requires trajectory-divergence at **EACH** window. The synthesis delivers exactly one
existence proof: capstone #3 "one player-shaped branch (participated outcome changes the arc's next
stage)" (`00_engine_charter.md:157`) and the watching/participating invariant, which only guarantees
a window is *offered/participable* (`synthesis.md:126-128`), NOT that participation *changes the
successor state*. The conformance suite (`synthesis.md:260-270`) has NO rule checking that a window's
distinct participated outcomes map to distinct `lifecycle.state` successors. An arc FSM where the
win-branch and lose-branch both transition to the same next state is an **illusory choice = textbook
railroad**, and nothing catches it. This is the single most load-bearing C7 property and it is
unenforced.
**FIX:** add conformance rule *engagement-window-divergence* — for every `activity_mode ∈
{edge_triggered_retryable, convergence}` vector with the player in `payload.participating_actors`, the
compiled FSM must expose ≥2 participated-outcome classes mapping to ≥2 distinct next `lifecycle.state`
values (or a distinct `pressure_effects` set); windows whose outcomes all collapse to one successor
are flagged illusory-choice at compile.

## Finding 2 (MAJOR) — foreclosure can fire silently via passive threshold-crossing

C7 `:41,:77-78`: foreclosure "via arc events only… surfaced afterward in chronicle… never silent."
Two breaks:
(a) `arc_vector.activity_mode` includes `clock_escalation` / `level_triggered` (`synthesis.md:58-59`),
and `pressure_effects` apply ±2/season deltas to clocks/stats (`:64`). A passive ARC-P clock (e.g.
ARC-S07 Loyalty ≤2 → "Crown Mandate −2 cumulative", `01_arc_corpus.md:41-42`) can drive a stat across
a foreclosure threshold with **no arc event** — foreclosure by accumulation, violating "arc events
only." Nothing distinguishes event-foreclosure from threshold-foreclosure.
(b) The synthesis leans on **total-accounting** (`synthesis.md:238-240`, §10 rule 3) to satisfy
"never silent." But total-accounting is engine-internal: a foreclosure `CONSUMED-INTO-STATE`
satisfies it while **never rendering to chronicle**. C7's "surfaced afterward in chronicle" is a
PLAYER-FACING guarantee; total-accounting's "discard-with-reason" is not surfacing. The two are
conflated.
**FIX:** (i) conformance rule — `stakes_tags:[foreclosure]` transitions may originate only from
`activity_mode ∈ {edge_triggered_once, edge_triggered_retryable, convergence}`, never
`clock_escalation`/`level_triggered`; a clock crossing that would foreclose must instead raise an
edge-triggered arc event that then forecloses. (ii) mandatory-render rule — every foreclosure
transition MUST emit a Tier-3 chronicle beat (positive surfacing check, distinct from rule 3's
discard logging).

## Finding 3 (MAJOR) — "pricing preferred over gating" is an unenforced authoring tag

C7 `:41,:76`: pricing *preferred* over gating. In the synthesis `stakes_tags` is a bare per-vector
enum `gating | pricing | foreclosure | pattern_response` (`synthesis.md:67`) carried through compile
untouched. Neither the compiler nor the six conformance rules (`synthesis.md:260-270`) prefer pricing
or flag gating overuse. A corpus authored entirely with `gating` tags passes every gate — the
*preference* is a guideline, not an engine property. Capstone #6 (`00_engine_charter.md:159`) only
proves one-of-each exists, which does not establish a preference.
**FIX:** compile-time report of the gating:pricing ratio + a rule that any `stakes_tags:[gating]`
vector must carry a `gaps[]`/justification note stating why pricing is infeasible for that option, so
gating is the *audited exception* the charter's "preferred" language intends.

## Finding 4 (MAJOR) — watching/participating invariant risks rubber-banding

Q4 invariant "every major arc keeps ≥1 open intervention point until converging"
(`00_engine_charter.md:120-121`) + synthesis "a major arc cannot be all-watched before converging"
(`synthesis.md:126-128`) collide with Q1 "ignoring a summons is remembered, never a pause; unattended
arcs proceed autonomously" (`00_engine_charter.md:50-54`). The synthesis never specifies the
*enforcement mechanism*. If the director enforces the invariant by holding an arc at pre-converging
until the player finally participates — or by re-injecting a summons that would otherwise have lapsed
— that IS a pause / the world waiting for the player = **rubber-banding = railroad**, directly
contradicting Q1.
**FIX:** specify the invariant as OFFER-not-outcome: the arc's FSM/clock advances on schedule
regardless of participation; the invariant is satisfied by an intervention point *having been
offered* (a fired summons or a slate candidate emitted), NOT by participation having occurred. An
all-ignored major arc still converges on time and passes. The CI check (rule 6) must count
*offered* windows, never *taken* windows.

## Finding 5 (MAJOR) — the director "owns the tension curve" graduates a DEFERRED, contentless spec

Charter Q4 `:128-129` and synthesis §3/§4 say the director "graduates articulation §7 D11" and "owns
the tension curve" (`synthesis.md:36,118-119`). But `articulation_layer_v30.md §7` (L302-304)
**explicitly DEFERS pacing**: "Pacing… is deferred to a future PP. The articulation layer as
specified does not enforce pacing; cut scenes fire whenever triggers match." §10 D11 = "Deferred per
§7" (`articulation_layer_v30.md:355`). There is **no tension-curve mechanism to graduate** — the
phrase is [UNGROUNDED] beyond the charter's own aspiration. Worse for C7: a director that shapes
*when* beats fire to hit a rising-action target IS over-orchestration; "owning a tension curve" is
the definition of the thing C7 forbids (and edges C2). The C2-non-surfacing argument
(`synthesis.md:134-138`) answers surfacing, not the *behavior*.
**FIX:** drop "tension curve" ownership. Redefine the director as a stateless budget CEILING only:
cap N cut scenes/season, demote overflow to texture, and NEVER promote/insert/re-time a beat to hit a
dramatic target. If any curve-shaping is retained, add a C7 rule: the director may only SUBTRACT
(ration/demote), never INSERT or advance a beat's timing.

## Finding 6 (MAJOR) — salience demotion can railroad AWAY from player-pursued arcs

The director rations the 3-5 envelope and demotes arcs to Tier-1 texture (`synthesis.md:122-131`).
detect-THEN-schedule protects *detection* from starvation (`synthesis.md:23-25`) but **nothing
protects player-agency-in-scheduling**: no rule states that an arc the player is actively pursuing
(player in `participating_actors` with a participated outcome in `causes[]`) is exempt from demotion.
If the budget fills with director-selected arcs and demotes the arc the player is chasing to rumor,
that is a soft railroad steering attention away from the player's chosen thread — a C7 failure the
"CEILING not floor" framing (`synthesis.md:124`) does not address (a ceiling still chooses *which*
arcs occupy the slots).
**FIX:** salience-economy rule — any arc with a player participated-outcome in its `causes[]` within
the last K seasons is demotion-exempt (or floored at foreground priority) until it resolves/converges;
demotion may only touch player-untouched arcs.

---

## What survives (the spine is C7-sound where it commits structurally)

- **Non-participation autonomy is structurally real** where the FSM is concerned: L1 steps lifecycle
  FSMs "with zero player Keys" (`synthesis.md:34`, Q1 `:50-52`). That mechanism, taken alone, is the
  correct anti-pause design — the risk (Finding 4) is only in how the *invariant* is enforced on top
  of it.
- **detect-THEN-schedule** genuinely prevents the C-architecture failure of scheduling starving
  detection (`synthesis.md:23-25`). Good.
- **Arcs-as-DATA** makes windows *inspectable* — Finding 1's fix is only possible BECAUSE vectors are
  typed data (`synthesis.md:190-192`); the spine enables the check it currently lacks.

## Net

C7 is not violated by the architecture's *shape*; it is under-ENFORCED. Five of the six sub-properties
have no conformance rule, one rests on a deferred/contentless spec, and one ("never silent") is
conflated with an engine-internal invariant. All fixes are additive conformance rules or a
scoping-down of the director — none requires abandoning Architecture B. **Verdict: SOUND-WITH-FIXES.**
