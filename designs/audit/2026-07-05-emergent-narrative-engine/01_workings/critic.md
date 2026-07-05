# Completeness Critic — full working notes

## Status: PROPOSED (critic lane, 2026-07-05 · Lane IN)
_Role: completeness critic for the whole emergent-narrative-engine design effort, against the
charter. Read in full: `00_engine_charter.md`; the five `spec_sections/s{1..5}`; grounding
`01/02/03`; the three verification verdicts (contract-coherence, trace-accounting,
register-roundtrip). Verifier-caught defects (rule-numbering collisions, `chronicle`-not-a-module,
Himmensendt, `resolves_via:dice_pool` mis-scope, COLLISION-C delta aliasing, ledger_cause schema,
Domain-Echo loose usage, Torben 8-vs-3 start) are CONTEXT, not my findings — I do not re-report
them. My lens is charter-completeness: weakest Q, thinnest C, least-convincing capstone, unused
grounding, missing [OPEN — Jordan] flags._

---

## 1. Which of the four questions is weakest-answered → **Q2 (world affects player)**

Q1/Q3/Q4 are each substantively delivered and densely grounded. Q2 is the weakest on three
concrete, charter-anchored counts:

1. **The social-ladder table omits the charter-required per-rung "surfaces" column.**
   Charter Q2 L69-70: the ladder "individual → family → settlement → territory → faction → world:
   **each rung names its arc carrier, surfaces, casting ties**." The s1 §Q2.4 table has columns
   `Rung | Arc carrier | Casting tie | Transport up/down` — the **surface** dimension is dropped
   for every rung. Q4 has a surface map but it is not keyed per social rung. Actionable: add a
   `surface(s)` column to §Q2.4 (e.g. family→Tier-1 Bond register + Knot/Bond scene; settlement→
   governance events; world→chronicle + clock-band cut scenes).

2. **The factionless-on-ramp acceptance test is asserted "by construction," never demonstrated.**
   Charter Q2 makes it an explicit acceptance test: "a factionless PC gets playable seasons."
   s1 §Q2.3.c gives a ladder diagram and says "Acceptance test met by construction." But the ONE
   worked trace (S5) uses **Ser Halden, a Crown-household agent with `Duty(Halden,Crown)`** — a
   fully factioned PC. No factionless season is traced anywhere. The single acceptance test Jordan
   named for Q2 is structural-assertion-only. Actionable: add a short factionless mini-trace
   (Conviction/location-edge casting → settlement arc → Standing/Obligation proto-currency),
   showing 1 playable season with zero faction edges — otherwise the acceptance test is unmet.

3. **Two Q2 sub-requirements are one-line or ungrounded.** "Territory temperaments get their chance
   to earn a why" (charter Q2 L72) is a single closing sentence in §Q2.4. T-30 information-asymmetry
   (charter Q2 L66) is carried `[UNGROUNDED — T-30 named in charter, not re-verified]` (§Q2.3.b,
   fork 4). Honest, but thin relative to the rest of the effort.

Runner-up: Q4 is heavily hedged (ERA unbuilt, low-thousands bake, per-NPC voice uncertified) but
those hedges are honest and structural; Q4's *required content* is all present. Q2 has the most
charter-required items that are gestured rather than delivered.

---

## 2. Which C1-C7 has the thinnest treatment → **C6 (P-14, thread beats must render)**

C1 (offline realizer), C2 (lint on all lifecycle/salience + fragments), C3 (books venues), C4
(closes ED-IN-0003/0004), C5 (one store, 2-new-types flagged), C7 (offer-not-outcome +
director-subtract-only + foreclosure-via-edge + demotion-exempt) are all richly treated — C7 is the
most treated of the set.

**C6 is the thinnest.** The four ED-681 Rendering-Crisis beats (Withdrawal / Knot Anchoring / Place
Anchoring / The Choice, `threadwork_v30 §3.7`) "must render" — a HARD P-14 constraint. The whole
discharge is: s3 Deliverable 1 + s4 edge **E11** ("thread system → 4 ED-681 beats → articulation,
DECLARED-NOT-TRIGGERED, Stage-0 adds trigger"). That is a trigger-table line item. There is:
- **no worked render** of any of the four beats (no fragment cell, no coherence/certainty band, no
  focalizer example — unlike ARC-S07 which gets a full Q4.6.1 worked example);
- **no thread arc anywhere in the effort** — Q3 taxonomy/lifecycle examples are all faction/clock
  (ARC-S07, ARC-S20, COLLISION-C); the arc corpus's 8 thread vectors (ARC-S04/05/15/32-34, T07/T18,
  grounding 01a) are untouched; the capstone trace (S5) is a faction/succession arc exercising zero
  threadwork;
- **no confirmation** that each of the four beats maps to a distinct fragment + that low-Coherence
  Rendering-Crisis (Coherence 0) — the very band these beats live in — has authored fragments.

C6 is P-14 and its four named beats are, per grounding 02(d), "the exemplar of authored beats with
mechanical triggers." Discharging that with one E11 row, no worked render, is the thinnest
constraint treatment. Actionable: add a worked render (or a thread mini-trace) exercising each of
the four beats at its Coherence band, confirming a fragment cell + focalizer per beat.

---

## 3. Which capstone requirement is least convincing → **Capstone #1 (major arc … convergence …)**

Capstone #1: "seed → slate scene → **convergence** → resolution → chronicle echo, ≥3 rungs." The
trace hits the shape (4 rungs, S5.2 close) — but the **convergence** it demonstrates is the weakest
possible form, and this is not a verifier-caught defect:

- The traced spine's only convergence is the **cosine-detected ARC-S07↔ARC-S20 correlation**
  (S5 Beat 3.2(ii)), which by the effort's own R5/R9/CR-2 rule is **RENDER/CHRONICLE-ONLY with zero
  `pressure_effects[]`** — it changes nothing mechanical.
- The register-authored marker wired to ARC-S07, **COLLISION-C**, is **DISCARDED** (S5 Beat 3.2(i))
  because its constituent ARC-T04 is a dangling ID (fork 2).
- s2 §Q3.10 step 5 states ARC-S07 "still feeds COLLISION-B/F cleanly" — but **neither
  COLLISION-B nor COLLISION-F is ever fired** in the trace.

So the engine's **headline capability** — an effect-bearing convergence applying authored combined
pressure — is exercised **nowhere** in the worked deliverable. This is exactly the F-2 / ED-IN-0003
gap the whole effort exists to close (Convergence Markers with no applier). The capstone that is
supposed to prove "converged into a story that matters" demonstrates only a correlation that
explicitly does not matter mechanically. Least convincing.

Actionable: trace **COLLISION-B or COLLISION-F** firing end-to-end with its authored deltas (the
spec says they feed cleanly, so no new fork is needed), or add a second short mini-trace of any
register-authored COLLISION applying combined pressure. Right now every convergence in the capstone
is zero-effect.

Secondary least-convincing (noted, not lead): **#10** ("compiled end-to-end") rests on two open
forks (Coup Counter remap O-2, ARC-T04 strike O-3) plus the unbuilt `lifecycle.state` field, so it
is really "compiles-with-one-new-field + two forks resolved"; **#11** anti-oatmeal is honestly
red-by-default until ERA is built (the sketch meets the literal "sketch" bar, but the prose-level
charter requirement is unverified).

---

## 4. Which grounding sources went unused (all cited in grounding, absent from the sections)

- **ED-609 (open — Torben Beliefs/Conviction emergence)** — grounding 01(d) + 03(b). The capstone
  arc IS the Torben arc; ED-609 is the open editorial *specifically* about Torben Conviction
  emergence. s2/s5 build the entire ARC-S07 compile and never cite or reconcile ED-609. The
  neighbouring ARC-T02 (Almud Belief) is used; the on-point Torben ED is not. Actionable: cite
  ED-609 in the ARC-S07 compile and state whether the compile closes it, depends on it, or leaves
  it open.

- **doc-10 §8.5 NOT-list carried incompletely** — grounding 03(a) lists four items the charter says
  "stand": no single-character heroic arcs · no authored mystery/reveal arcs · no designed dramatic
  timing · no failure-of-the-world model. s2 §Q3.7 CANNOT list carries "no designed dramatic timing"
  and adds "no three-act guarantee," but **omits three of the four**: single-character heroic,
  authored mystery/reveal, failure-of-the-world. Charter Q3 L104-105 requires the CAN/CANNOT list
  and says the NOT-list stands. Actionable: add the three missing items to §Q3.7 CANNOT.

- **The arc-generator hard rule "no single player decision caused this"** — grounding 01(c),
  `skills/valoria-arc-generator/SKILL.md`. Unused, and in **latent tension with capstone #3**
  ("player-shaped branch changes the arc's next stage") and the anti-railroad divergence rule
  (CR-3/R7/R10). The sections assert a participated outcome flips the FSM branch; the arc-generator's
  own authoring doctrine says no single player decision causes an arc. Never reconciled. Actionable:
  state the reconciliation (the player *selects among emergent branches / accelerates-or-defers*,
  does not *author* the arc; the ±2/season cap and multi-vector causation still hold).

- **valoria_ui_ux_v4_1.md §9.7 "UI corruption ladder per Coherence band"** — grounding 02(c), a
  *third* state→presentation spec ("structural analogue"). Unused in Q4 UI-ceilings / coherence
  rendering (s3 Q4.8). Actionable: cite it as the UI-side companion to the coherence-tier render
  table (Q4.6.2), or note why it is out of scope.

- **ED-1009 (open — multi-emitter attribution: `scene.dialogue`/`belief_revised`)** — grounding
  03(b). s4 re-owns the *sibling* `mechanical.scene_entered` multi-emitter conflict and gives it a
  loud fork (S4.8), but s4 also has `scene_slate` emitting `scene.dialogue` and `articulation`
  consuming `belief_revised` — the exact pair ED-1009 flags — with no reference to ED-1009.
  Actionable: reference ED-1009 and state whether the substrate work touches or defers it.

- **The ~850KB prior emergent-arc drafting in `tests/`** — grounding 03(e) item 4 / decision-queue
  25a: "a content asset for the bake, currently invisible." The bake-volume analysis (s3 Q4.6.5,
  low-thousands) counts `gm_ref` (~300KB) as *evidence craft is achievable* but never counts the
  ~850KB `tests/` asset as an existing input that could offset the authored-unit total. Actionable:
  fold it into the bake accounting (or explicitly exclude it with reason).

- **`module_11_provincial_authority.py`** — grounding 01(d): "the Governor→Province→National Echo
  chain, the literal canonical mechanism T-23 names." s1 grounds leader-delegation aggregate-up
  (§Q1.2) on `domain_echo.py` but not on this concrete Governor→Province→National implementation,
  which is the on-point evidence that leader→subordinate→Echo reach is already built. Minor but
  directly relevant to Q1's reach claim.

- (minor) `references/three-axis-test.md` (worked Spirit example) and the per-seed
  `arc_test_batch*_results.md` prose write-ups ("writing around randomized seeds," grounding 01a) —
  the existing seed-divergence evidence base for the 5-seed narrative regression — are not mined by
  s3/s5. Would strengthen the anti-oatmeal argument with real prior divergence data.

---

## 5. Which open forks are missing [OPEN — Jordan] flags

**PRIMARY — dropping the director's tension-curve ownership is presented as settled, not a fork.**
Charter Q4 L128-129 states plainly: "director layer (articulation §7 D11) **owns the tension
curve**." All five sections (s1 §Q2.5 reconciliation clause, s2 §Q3.7 director ruling, s3 Q4.7
director contract, s4 S4.10, s5 S5.7 sidebar) **DROP** tension-curve ownership and reduce the
director to subtract-only, presented as a "ruling" / "reconciliation" / settled structure, justified
via doc-10 §8.5. The justification is *good* — but reversing an explicit charter directive is
exactly the hard-call-bundled-into-routine-work failure CLAUDE.md §2 (ED-1094) exists to prevent,
and the charter's own method rules put design reversals to Jordan. This reversal is unanimous across
the effort and carries **no [OPEN — Jordan] flag anywhere** — it is asserted, not forked. Actionable:
carry "director tension-curve ownership DROPPED → subtract-only" as an explicit [OPEN — Jordan] with
the doc-10 §8.5 rationale as the recommended default, and flag it in the PR body as held-back.

**SECONDARY — the "cosine convergences carry zero effect, forever" ruling (CR-2/R5/R9)** forecloses
a whole class (general emergent convergence never bears mechanical pressure) as settled structure.
It is well-justified by anti-fabrication, but it is a *design* call about the ceiling of emergence
Jordan set out to maximize — borderline worth a soft flag rather than a silent ruling. (Lower
priority than the tension-curve item.)

**TERTIARY — the family-rung "Bind vs declare absent-deliberate" disposition** (§Q2.4) is a per-
campaign authoring choice presented with a recommended default and a conformance rule; probably does
not need a Jordan fork, but note it reads as settled where the charter treats family as the "thinnest
rung … handle explicitly."

Everything else contestable IS flagged: scene_entered (O-1), Coup Counter (O-2), ARC-T04 (O-3),
realizer RNG (O-4), temporal_window (O-5), bake/Certainty (O-6), Gate-0 (O-7), GM-judgment 15%
(O-8), Cert-0 row, K-window, two-new-types, lifecycle-field ownership. Fork discipline is otherwise
strong.

---

## 6. Minor interpretive note (not a headline)

Charter Q4 L120-121 requires every major arc to "keep ≥1 open intervention point until converging
**AND route through ≥1 playable scene**." The offer-not-outcome rule (s1 §Q1.3, s3 Q4.3, R6) counts
*offered* windows, so an all-ignored major arc routes through **zero played scenes** yet passes. The
spec reads "offered = routed-through-a-playable-scene." Defensible (and necessary to avoid the
rubber-band), but it is a real interpretive narrowing of the charter's second clause; worth one
explicit sentence acknowledging the clause is satisfied by *playability offered*, not *play taken*.

---

## Summary ranking (most to least load-bearing)
1. Missing [OPEN — Jordan] on dropping director tension-curve ownership (charter reversal, silent).
2. Capstone #1: no effect-bearing convergence anywhere in the trace (headline capability unexercised).
3. C6 thinnest: four ED-681 thread beats discharged as one trigger row, zero worked render, no thread arc in the effort.
4. Q2 weakest: factionless acceptance test untraced; ladder table missing the per-rung surfaces column.
5. Unused sources: ED-609 (on-point Torben ED), doc-10 §8.5 NOT-list (3 of 4 items dropped), arc-generator "no single decision" rule (tension with capstone #3), ED-1009, ui_ux §9.7, ~850KB tests/ bake asset.
