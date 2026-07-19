# Refutation lane — v2 CHURN engine on C2-VETO + C7-RAILROAD (+ Light-Function N/Ω/Q)

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Target: `narrative_engine_design_v2_churn.md`. Try to BREAK on C2 (no narratological surfacing,
doc-12 veto — `00_engine_charter.md:26-30`) + C7 (never railroads — `:40-41`, Q1 `:54`, Q2
`:75-79`). Working tree only; `[UNGROUNDED]` tags my extrapolation. v2's new attack surface vs
v1 = the FORECAST field (§3), the LIGHT FUNCTION (§4), NPC anticipatory behavior (§6). The prior
passes (`refute_veto_and_drift.md`, `refute_railroad_windows.md`) covered v1; I do not re-tread
their findings except where v2 makes them WORSE._

Verdict: **SOUND-WITH-FIXES at the letter of C2/C7; the Light Function organ FAILS the N/Ω/Q
gate on Ω(c)/Ω(d) + Q-smooth/elegant.** No absolute veto string breaches, but the
forecast→casting→NPC reflexive loop is an unadmitted Ω-autonomy corruption that should BLOCK the
M1 path until severed. Five findings; F2 is the deepest.

---

## F1 (MAJOR · C2) — forecast anticipation-render is a probability meter in a diegetic coat

**Claim.** §6's new render surfaces — "stakes-preview lines," "foreclosure warnings,"
"projected-next-beat + horizon band, rendered as anticipation," "foreclosure_countdown" (§3
output), "counsel/omens in Certainty-keyed voices" — leak the §3 probability field to the player
in prose. The doc's defense (§9.1: "numbers never surface") answers the wrong question.

**Where diegetic becomes a meter — the line, concretely.** A character voicing uncertainty ("the
odds are not kind") is diegetic and C2-clean IN ISOLATION — doc-12 vetoed narratological
*structure* labels ("Rising Action"), not in-world opinion. The breach is STRUCTURAL, per
`refute_veto_and_drift.md:F4`: if the rendered anticipation is a **deterministic, monotone,
frequent** image of the computed P-band, the player inverts it over repeated play — the counsel
IS a quantized probability read-out with zero forbidden strings. v2 makes this first-class (§6
"Plots project forward ... horizon band ... rendered as anticipation"), where v1 left it
incidental.

**Evidence — §9.1's own worked example breaches its own claim.** Skeptic clerk (Cert-2): *"Miss
two more contacts and the heir is theirs by spring — the odds are not kind past that."* This
surfaces (i) the exact k-horizon ("two more contacts" = the `foreclosure_countdown` k-index),
(ii) the threshold outcome ("theirs by spring"), (iii) a comparative-probability claim ("odds
not kind past that" = the P-band ordering). A **countdown-in-prose is a number**; §9.1 asserts
"numbers never surface" one line after surfacing one. `foreclosure_countdown` and
`stake_horizon{P-band per k}` are being rendered near-verbatim. The Warden line ("not taut yet")
and Orthodox line ("two winters of silence") do the same softly — all three are monotone in the
same band.

**Line drawn.** C2-clean: counsel whose APPEARANCE is one-to-many w.r.t. the band (multiple bands
→ same register; a line is compatible with a RANGE of horizons; NPC-variance noises the
coupling), expressing DIRECTION/STAKE only. C2-breach: injective/monotone band→line coupling, or
any **quantized** horizon surfaced ("two more contacts," "by spring," a countdown).

**REQUIRED_FIX.** (a) Ban quantized-horizon surfacing: anticipation may express who/what-is-at-
stake and direction, never the k-count or P-band. Rewrite §9.1's Skeptic line. (b) Require
many-to-one band→render coupling (an entropy/de-quantization conformance check, the forecast
analogue of `refute_veto_and_drift.md:F4`'s "framing- and frequency-indistinguishable" rule) so
the line cannot be inverted to the meter. (c) `foreclosure_countdown` must never render as a
countdown; it schedules internal urgency only.

---

## F2 (BLOCKER-class · C7 + Ω-autonomy) — self-fulfilling forecast: the loop the "one-pass" bound does not touch

**Claim.** Forecast mass drives CASTING, NPCs act on the same forecast, then discovery "finds"
the convergence they helped cause. The engine manufactures the crises it predicts. The design
admits reflexivity but bounds the WRONG loop.

**Evidence.**
- §4 selection score = meaningfulness × **forecast mass** × imminence × inertia × scale-weight;
  §4 reflexivity: "lit → slate → **played** → changed trajectory." So forecast mass selects which
  futures get impelled onto the player (L4 CAST/IMPEL, §8).
- §6: "NPCs and factions acting on **position-scoped forecasts** (armies muster, prices move)."
- §3: convergence_candidates are "**discovery** over the ensemble"; the ensemble samples "through
  the LIVE code paths" incl. `faction_action.py` / (unstubbed) `npc_ai`. R-F1 (§7) makes forecast
  ≡ live code — which maximizes the self-fulfillment channel's efficiency while it guarantees
  honesty.
- Stated bounds (§4): "one-pass allocation per Accounting (no fixed-point iteration); NPC
  anticipatory behavior reads position-scoped forecasts, **not the light ledger**."

**Why the bounds miss.** "No fixed-point WITHIN an Accounting" ≠ no fixed-point ACROSS
Accountings. The loop closes on the game clock: Accounting t forecasts convergence C → forecast
mass lights C + NPCs act toward C → between t and t+1 real NPC Keys push state toward C →
Accounting t+1 forecasts C at HIGHER mass → lights harder, NPCs act harder → positive feedback
= rubber-banding toward the forecast, unbounded by a per-Accounting one-pass rule. And "reads
forecasts, not the light ledger" is a distinction without a difference: the light's selection
term IS the §3 forecast, so light-on-forecast and NPC-on-forecast read the **same signal** —
their correlation is exactly what closes the loop. Separating from the *ledger* does nothing.
§3's honesty bound ("field pressure under average play, never a promise") governs whether the
forecast is epistemically honest, NOT whether ACTING on it is causally self-fulfilling — a
forecast can be honest and still manufacture its own referent. The design conflates
forecast-honesty with forecast-neutrality.

**C7 tie-in.** `refute_railroad_windows.md:F1`'s illusory-choice is dynamically restored: even if
a window's outcomes diverge within one FSM step, the next Accounting re-lights the forecasted
convergence and NPCs re-drive it, herding divergent choices back to the predicted attractor.
Windows real once, un-real across the loop.

**REQUIRED_FIX.** (a) Sever forecast mass from the CASTING/slate-injection path — forecast may
weight retrospective SALIENCE/texture among already-fired beats, never select which futures are
impelled onto the player; casting keys on the tie-graph (charter Q2 ONE rule) + REALIZED state
only. (b) NPC anticipatory behavior reads only observable/realized state + in-character
expectation, never the engine's `stake_horizon`/`convergence_candidate` objects; make those
objects non-readable by any actor resolver (conformance: no `faction_action`/`npc_ai` path takes
a forecast object as input). (c) Cross-Accounting anti-self-fulfillment fixture (extends F7):
seed a forecast of C, suppress player participation, verify realized P(C) does NOT exceed the
forecast-BLIND control. If forecasting C raises P(C), the loop is live. F7's smoke oracle does
not cover this.

---

## F3 (MAJOR · C7/self-contradiction) — "strictly selective / never shape an outcome" is internally contradicted

**Claim.** §4 asserts the Light Function "can never inject content, **shape an outcome**,
accelerate a clock, or touch resolution ... Allocation-among-given IS the subtract-only
discipline." Two lines later the SAME section: reflexivity "lit → slate → played → **changed
trajectory**." A changed trajectory IS a shaped outcome. Both cannot hold.

**Every light path, checked for outcome-touch.**
1. **Slate injection — OUTCOME-TOUCHING.** The playable slate is scarce (§6: 3–5 scene actions).
   Choosing which beats occupy scarce playable slots determines which outcomes the player CAN
   affect; subtract-only demotion of a thread the player would have pursued removes a real
   intervention point (= `refute_railroad_windows.md:F6`, made worse because v2 keys injection on
   forecast mass — the engine slots the futures IT predicts, crowding the player's). "Attention-
   only" is FALSE when attention gates entry to the scarce agency surface.
2. **Texture render** — clean (prose cost O(attention), no outcome).
3. **Catch-up re-light (§4)** — clean ONLY IF re-light Keys are render-only; if a re-light
   "designed beat" emits pressure-bearing Keys, light state alters the Key log = outcome-touch
   (see F5).
4. **Projected beats / NPC anticipation** — the F2 channel; the largest outcome-touch.

**REQUIRED_FIX.** (a) Retract the unqualified "never shape an outcome"; restate: "never shapes
the RESOLUTION of a scene the player enters, never accelerates a clock, never emits a pressure-
bearing Key." (b) Because slate-injection IS outcome-relevant, bind it to C7: a thread with live
player intervention interest is slate-eligible regardless of forecast mass (import
`refute_railroad_windows.md:F6` exemption); forecast mass may not demote a player-pursued thread
out of the playable set. (c) catch-up re-light Keys are render-only, zero `pressure_effects`
(conformance) — so light provably cannot alter the Key log.

---

## F4 (MAJOR · Ω-autonomy) — NPC-on-forecast corrupts "autonomy earned in the shade"

**Claim.** §4: "shaded branches keep churning (autonomy is earned in the shade)." But §6 NPCs
act on the engine's forecast, and forecast samples NPC decisions via shared code. If the same
prediction nudges every NPC toward the predicted attractor — in foreground AND shade — the
world's autonomy is a hidden hand. The shade is steered by the same forecast that lights the
foreground; "discovered, not authored" (§9.1) becomes "caused by the forecast, then discovered."

**Evidence.** Charter C5/Ω-c requires an autonomous world; Q1 `:50-54` "unattended arcs proceed
autonomously." §3 computes the forecast BY simulating NPC/faction decisions (`faction_action.py`,
`npc_ai`); §6 then has NPCs ACT on that forecast; the next forecast re-simulates the moved state.
Oracle and actor are the same code reading each other — R-F1 ENABLES this rather than guarding
it. "Position-scoped" limits WHICH forecast an NPC sees, not WHETHER the engine's prediction
drives it.

**REQUIRED_FIX.** Same structural cut as F2(b): NPC expectation is a diegetic heuristic over
observable state + memory; the engine's forecast objects are actor-invisible. Conformance rule:
assert no actor resolver imports `stake_horizon`/`convergence_candidate`. This is the clean line
between "NPCs are prudent" (fine) and "NPCs are the engine's forecast-delivery mechanism" (Ω-c/d
fail).

---

## F5 (MAJOR→MINOR · P-08/trail/focalization) — shade catch-up narrates the unwitnessed with no focalizer

**Claim.** §4 catch-up example — *"while you were at war, Hafenmark changed"* — narrates shade
churn no accessible actor focalized. §1 says every projection has a FOCALIZER; the example names
none. It is omniscient, present-tense, second-person direct address = the "telling" the charter
Q4 reserves for RETROSPECT, used as a real-time "designed beat."

**Canon hazard.** Charter Q4 requires every foregrounded beat to leave a followable diegetic
trail (gossip/witness/document) and to render "AT a location, THROUGH a venue, or IN the
chronicle." A focalizer-less omniscient catch-up satisfies neither, and makes shade transparently
knowable — eroding P-08 (epistemological barrier = inaccessibility). The ONLY sanctioned
omniscient register is doc-13's "year-end omniscient retrospective" (chronicle) — a present-tense
"while you were at war" catch-up beat is outside it. `[UNGROUNDED: no explicit "no unwitnessed
narration" string in canon/ — grep empty; argued from Q4 trails + P-08 + doc-13.]`

**REQUIRED_FIX.** Shade catch-up MUST focalize through (i) the omniscient CHRONICLE register
(past tense, doc-13-sanctioned), or (ii) a diegetic carrier with a trail (returning agent,
gossip, document, witness present in the shade) — never focalizer-less present-tense omniscient
address. Rewrite the example. Conformance: a re-light catch-up beat must cite a focalizer
(`chronicle | witness_key | document_key`), enforcing Q4's venue rule on catch-up beats (the
easiest to render as placeless telling). Pair with F3(c) render-only Keys.

---

## N/Ω/Q gate — the LIGHT FUNCTION organ (§4)

Framework: `2026-07-04-ners-qualitative-audit/00_grounding/01_criteria_ners_lineage.md:30-46`.

- **N (Necessity, Jordan-owned) — PARTIAL, flag.** Selection-from-churn IS necessary (no GM;
  ~10³ Keys/season must be rationed) — the subtract-only CORE passes N. The **forecast-mass term
  in the selection score** is the N-suspect addition: forecast-driven SALIENCE models real
  counsel/advisement; forecast-driven CASTING is the engine playing oracle, not modeling
  Renaissance leadership — candidate "fantasy imposition." N-fail → flag to Jordan, never
  auto-reject.
- **Ω (Intent).** (a) cross-scale consequence — PASS (holonomy §1). (b) personal transformation
  — PASS (player-rooting/identity-touch). (c) **autonomous world — FAIL** (F2/F4 self-fulfilling
  loop). (d) **non-dominance — FAIL/AT-RISK** (forecast mass dominates casting + NPC behavior;
  cross-Accounting rubber-banding). **Ω is the axis the organ fails**, precisely where the
  forecast term reaches into casting.
- **Q (Quality, Claude-owned; Q-fail = iterate).**
  - Q-robust — PARTIAL: "what happens if no one acts" is now COMPUTED (good, §3); "three viable
    approaches" at risk under forecast-driven slate crowding (F3).
  - Q-smooth — **FAIL**: does not compose without entanglement; light reads forecast, NPC reads
    forecast, forecast reads NPC via shared code — a three-organ reflexive knot the one-pass bound
    doesn't sever.
  - Q-elegant — **FAIL**: the load-bearing second-order consequence (self-fulfilling forecast) is
    not predicted — it is actively DENIED by §4. A rule whose second-order behavior surprised the
    author fails Q-elegant by definition.

**Organ verdict: N-flag · Ω(c),(d)-FAIL · Q-smooth/elegant-FAIL → iterate before M1.** The
subtract-only + coherence-guarantee CORE (invariants i/ii/iii, the any-seed theorem §9.4) is
sound and survives. The failing element is narrow and excisable: **forecast-mass-in-casting** +
**NPC-on-forecast**. Strip both (F2/F3/F4 fixes) and the organ passes Ω and Q.

---

## Net

C2: SOUND-WITH-FIXES — defensible at the letter (no labels, no digits by intent), one real MAJOR
structural-tell seam (F1) the doc's own §9.1 example trips. C7: the window mechanics are not
broken in shape, but F2's cross-Accounting self-fulfilling loop dynamically re-railroads divergent
choices and is UNADMITTED — BLOCKER-class for the Ω-autonomy intent even though no C7 string is
breached. All five fixes are additive conformance rules + a scoping-down of the forecast term's
reach (casting/NPC), plus two example rewrites (§9.1 Skeptic, §4 Hafenmark). None requires
abandoning the churn architecture or the Light Function core.
