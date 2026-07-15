# Adversarial refutation — Jordan-veto (C2) + scripting-drift (C5) axes

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0069]
_Trying to BREAK "The Arc-Vector Engine with a Subordinate Director." Working tree only.
Cites charter + grounding + source docs; [UNGROUNDED] tags my own extrapolation._

Verdict: **SOUND-WITH-FIXES**. No absolute veto is breached (C1 clean — all offline bake;
C2 clean at the lexical level). But two real seams (convergence-effect fabrication; a
pre-empted Jordan fork) and three narrower items must be closed before a drafter proceeds.

---

## What survives the attack (I could NOT break these)

- **C1 (no runtime LLM):** the whole render path is offline-bake + deterministic splice
  (synthesis §6; `02_prose_render_stack (c)` NLG §8). Clean.
- **8 COLLISIONs as *data* is holonic-legitimate.** Transcribing `arc_register_events §VI`
  A–J into typed `convergence` vectors puts the named-entity references (ARC-S07, ARC-T04,
  Klapp, Olafsson…) in DATA, not code. Holonic doctrine §2 (L52) forbids code special-casing,
  not authored data that names entities. The compile step keeps the resolver general.
- **"Proto-currency" is not a NEW currency.** Standing/Obligation (synthesis §5 factionless
  ladder) are existing tracks; charter Q2 (L68) explicitly names "Standing/Obligation as
  proto-faction currency." C5 "no new progression currency" holds — progression IS the
  vectors' I/O (synthesis §1; charter Q3 L99 "one ledger").
- **Tie-graph casting keys on data fields** (position/Standing/Duty/Conviction/Bonds/Knots —
  synthesis §5), all charter-specified (Q2 L58). Position-differentiated CHANNELS are
  charter-mandated, not a hidden hardcode.
- **Convergence-triggered cut scenes are not a fresh doc-12 violation in principle.** doc-12
  §1.2 already ALLOWS "Cross-faction Key clustering → Contest acknowledgement" as a Tier-2
  trigger. The detector generalizes an already-sanctioned punctuation trigger; the veto was
  against *labels/resolutions* (doc-12 §0, §5 "REPLACE §4.2 arc detector surfacing in HUD"),
  which the C2 lint blocks.

---

## FINDING 1 (MAJOR, drift/fabrication) — the convergence-EFFECT seam

`arc_register_events §VI` (L25) states the defining property of a Convergence Marker: the
combined pressure is **"not predictable from the constituent vectors without the marker."**
Concretely COLLISION-C carries authored deltas (`RS +8, IP +2, TC +2 in a single season`,
L39) that are NOT derivable from ARC-S07 + ARC-T04 alone.

The synthesis runs TWO detectors (§3): (1) the 8 hand-authored conjunctions, which carry those
authored `pressure_effects[]`; (2) a **general cosine-similarity backbone** generalizing
articulation §3.1 trigger-9 from faction-pairs to arc-vector pairs. A general detector can
*detect* arbitrary arc-pair correlation but by §VI's own logic **cannot derive** the
"not-predictable-from-constituents" combined effect — that quantity exists ONLY where an author
wrote it.

The synthesis never states what a cosine-detected convergence OUTSIDE the 8 *applies*. Two bad
readings a drafter could take:
- Wire the general detector to synthesize a combined pressure_effect → the engine **fabricates
  unauthored deltas** (CLAUDE.md §5 "do not synthesize a value the ledger does not back"; §7
  the anti-fabrication gate is leaky). This is textbook holonic scripting drift by the back
  door: an outcome that cannot emerge from local rules gets manufactured.
- Apply nothing → then the only mechanically-real convergences are a **hardcoded whitelist of
  8**, and the vaunted "generality" is detection/render-theater. The brief's own worry ("does
  the tie-graph casting quietly hardcode?") lands here: the mechanically-consequential
  convergence set IS hardcoded at 8.

REQUIRED_FIX: state explicitly that cosine-detected convergences outside the register-authored
set are **RENDER/CHRONICLE-ONLY (zero `pressure_effects`)**; mechanical combined-pressure exists
ONLY for register-authored `convergence` vectors. Add conformance rule: any `convergence`
vector with non-empty `pressure_effects[]` must trace each delta to a register line (extend the
predicate-field-resolves lint, synthesis §10 rule 1). This preserves generality-of-*detection*
(Q3) while forbidding fabrication-of-*effect*.

---

## FINDING 2 (MAJOR, Jordan-veto/governance) — a charter-reserved fork silently resolved

Charter substrate contract (L148) lists the `mechanical.scene_entered` ownership conflict
(scene_slate vs game_director) explicitly as **"[OPEN — Jordan]"**. Synthesis §5 relabels it
**"scene_entered ownership — RESOLVED (this lane's job, not a fork)"** and demotes scene_slate,
citing `module_contracts.yaml:392-395` (scene_timer already consumes from game_director).

The evidence is real and the default is probably right — but the charter's OWN classification
is `[OPEN — Jordan]`, and the synthesis overrides that classification while asserting "not a
fork." Per CLAUDE.md §2 ED-1094, a hard design call must be **loud, not silent** — "never bundle
a hard design call into a routine-work PR and rely on an unprompted follow-up to ratify it."
Converting a charter-flagged Jordan decision into a lane-resolved non-fork is exactly the
failure mode ED-1094 closes, even though the synthesis gestures at merge-ratification.

REQUIRED_FIX: restore scene_entered ownership as an explicit entry in §11's fork list (default =
game_director single-source, citing the scene_timer evidence as the RECOMMENDED resolution), OR
flag it prominently as a *held-back* hard call in the PR body. Do not carry it as "RESOLVED"
when the charter says [OPEN — Jordan].

---

## FINDING 3 (MAJOR, C2-veto reconciliation) — the director's tension curve vs the standing NOT-list

Charter Q3 (L104-105): "State what plot shapes this CAN and CANNOT produce (**doc-10 §8.5
NOT-list stands**)." That NOT-list includes **"no designed dramatic timing"** (`03_prior_art (a)`
doc-10). Yet the director (synthesis §4; charter Q4 L128-129) OWNS a **"tension curve"** and
**"impulsion cadence"** and schedules forced-choice M-6 turns.

C2 is satisfied *lexically* — the tension curve "NEVER surfaces" (§4) and the literal-string
lint blocks labels. But doc-12's actual veto (§0) targeted the engine **knowing/imposing
dramatic structure in real time**, not merely *displaying* a label. A scheduler that rations
beats against an internal tension curve is using a real-time narratological model — the very
thing doc-12 rejected in framing, even if never shown. The synthesis asserts "CEILING not a
floor" (C7) but never reconciles the tension curve with the standing "no designed dramatic
timing" NOT-list.

REQUIRED_FIX: add an explicit reconciliation clause: the director may only RATION which
already-emerged beats *surface* (a surfacing budget, per C7 ceiling); it must NEVER manufacture,
reorder, delay, or time-compress the underlying events to shape a curve. State that "tension
curve" governs articulation cadence, not event timing — and that event timing remains fully
emergent, preserving doc-10 §8.5. Without this clause the director reads as re-importing
designed dramatic timing under an internal-only fig leaf.

---

## FINDING 4 (MINOR, C2 lint scope) — literal-string lint under-guarantees C2

The C2 guarantee rests on a **literal-string lint** (synthesis §10 rule 4) over
lifecycle/salience state + baked fragments. Lexical linting cannot catch STRUCTURAL/timing
narratological tells: if a Tier-2 cut scene fires *only* at `meta.convergence_detected`, the
player learns over repeated plays that "a cut scene = a story just converged" — the timing
itself becomes a legible arc signal with zero forbidden strings. doc-12 §1.2 already requires
Tier-2 to be indistinguishable *punctuation*, not convergence-announcement.

REQUIRED_FIX: note that the lint bounds only LEXICAL surfacing; add a design constraint that
convergence-triggered cut scenes be framing- and frequency-indistinguishable from ordinary
Tier-2 trigger scenes (doc-12 §1.2), so timing is not a de-facto arc label.

---

## FINDING 5 (MINOR, currency axis) — engine-owned narrative-weight scalars are ungated only by assumption

"Actor narrative weight" (charter-owned, L139) + the salience/`unarticulated_weight`
accumulators (synthesis §3-4, from articulation §3.2/§3.3) are engine-owned scalars that govern
casting priority. They are NOT new player currencies — so C5 holds — but the synthesis never
states they are BOTH non-surfacing AND non-gating. If any ever gates/prices/forecloses a player
option, it becomes a hidden progression meter — the P-04 "no hidden morality meter" analogue
(charter Q1 L53).

REQUIRED_FIX: add invariant — narrative-weight/salience accumulators schedule surfacing ONLY;
they never gate/price/foreclose a player option and never surface as a tracker. Extend the
gate-cites-ledger_cause rule (§10) to forbid a narrative-weight/salience field from ever being a
gate's cited cause.

---

## FINDING 6 (MINOR, drift/casting hardcode) — leader-casting inherits named-NPC branch maps

The leader path (synthesis §5) subscribes to `npc_behavior_v30 §5` concern/project Keys, whose
§5.2 is **"named-NPC branch maps A–F"** (`01_arc_corpus (d)`). This is acceptable as an existing
canonical T-23 specialization the store READS — but the synthesis must guarantee the CASTING
RESOLVER code itself contains no named-entity branch (all named-ness stays in the npc_behavior
data bucket).

REQUIRED_FIX: add a single-rule conformance check on the casting resolver (assert no
`if actor == <name>` / no named literal), mirroring `tools/ci_module_shape_check.py` (holonic
doctrine §2 conformance row). Confirms the "ONE tie-graph rule" claim (charter Q2 L58) is code-
general.

---

## Net

No absolute veto breach. The architecture's C2 posture is defensible at the letter (labels never
surface; detection internal) and C5 holds (no new currency; arcs compile from data). The
breakable surfaces are (1) the convergence-effect fabrication seam and (2) the pre-empted Jordan
fork — both MAJOR, both closable by a drafter with the fixes above. SOUND-WITH-FIXES.
