# Lane dossier — WR (World / Scene Slate umbrella)

**Audit:** `designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md` (Pessimist
Subtractive NERS over player-available actions) · **Agent tier:** Sonnet · **Read-only.**

## Reconciliation intro

WR is explicitly *not* a standalone verb-menu lane (`00_charter.md` §1): it is the **umbrella
surfacing mechanism** by which every other lane's opportunities reach the player. The player-action
home is `designs/architecture/player_agency_v30.md` §4 "Scene Slate" — Status: **CANONICAL**,
approved 2026-04-17, editorial batch acceptance — extended per the charter's "extend as needed"
license with the concrete trigger table it draws on (`designs/architecture/scale_transitions_v30.md`
§4.3.2 mandatory / §4.3.3 optional / §4.4 "Where Were You" retrospective), because §4's Steps 1–2 are
generation *rules* whose content is *defined* in scale_transitions, not in player_agency itself.

**Dispersed work reconciled for this dossier:**
- `player_agency_v30.md` §4 (7-step generation algorithm + Witness Mode + cross-step pruning, ED-745/
  746/747/761/674/750/766) — the mechanical spec.
- `scale_transitions_v30.md` §4.3.2/§4.3.3/§4.4 — the concrete trigger conditions Steps 1–2 consume.
- `references/module_contracts.yaml` `scene_slate` entry (L351-375) — registry says "home doc
  unlocated [GAP]," citing only `key_substrate_v30 §8.5` and `settlement_layer_v30 §4.1`, **omitting
  player_agency_v30 entirely** even though CURRENT.md's own priority order and this audit's charter
  both point to player_agency §4 as the actual head. This is a registry-drift finding, not a
  subtractive one — noted for the record, not scored against any action below.
- `CURRENT.md` — **has no row for player_agency/Scene Slate at all**, despite the doc's own
  self-description as the ED-545 fix and the connective tissue for every other subsystem's Zoom-In. A
  currency-index gap, same caveat as above.
- `canon/mechanics_index.yaml` `scene_slate_service` → `sim/autoload/scene_slate.py` — build-state
  only (a 26-line FIFO priority queue stub; the 7-step generator + cross-step pruning + Witness Mode
  are all unbuilt). **Not a verdict input** per the cardinal rule — captured only as
  `build_state_note`.
- `designs/audit/2026-07-05-edge-playability-audit/01_workings/cluster_C_top_down.md` (E1–E15) and
  `cluster_I_mode_bridge.md` (E6, ep-21) — prior-audit reconciliation of the eight mandatory rows,
  the five optional rows, and the Witness Mode valve. Findings there are calibrated KNOWN-TRACKED
  below where directly reused; this dossier's contribution is the *subtractive* framing those audits
  didn't attempt (they graded playability, not whether the mechanism earns its keep).
- `sim/world/{miraculous_event,insurgency_pipeline,restoration_movement,npe}.py` — confirmed
  environmental/autonomous-agent generators (Ω-c compliant background processes), **not player
  verbs**. They feed content into Slate Steps 2/2b/6/7 (NPC population, insurgency emergence,
  RM PT decay) but the player never directly operates them, so they are out of this dossier's unit
  of analysis (§1 "the verbs the player takes") and are not separately judged.
- Convictions (§2) and Duties (§3) are the *steering inputs* to Steps 3–4 but are themselves
  chargen/authoring systems, not scene-verbs, and are not explicitly named in any of the eight
  lane rows in the charter's §1 table. Flagged here rather than silently absorbed: they are
  candidate orphan territory for a future audit pass, not adjudicated by this dossier.

**Unit of analysis.** The Scene Slate is one umbrella *selection* verb (attend vs. let pass, under a
scarce scene-action budget) instantiated over seven differently-sourced generation Steps, plus a
distinct two-part fallback verb (Witness Mode) for mandatory-overflow. Per the charter's granularity,
each Step is judged separately for whether its *content category* earns a dedicated place in the
Slate — because N's "Duplicate coverage" and "Abstractable" failure modes apply at the Step level,
not only at the umbrella-verb level.

---

## Action 1 — Scene Slate Attendance / Personal-Phase Triage (the umbrella verb)

**Design intent:** let the player spend a genuinely scarce resource (3–5 scene actions/season)
against a genuinely larger set of generated opportunities (4–9/season), so that *choosing what to
attend to* — not executing a fixed quest list — is itself the primary personal-layer decision.

**As-if-built contribution:** this is the connective tissue the charter itself names it as. It
operationalizes P-03 (consciousness-performed rendering — the player's perceptual horizon *is* the
available-scene set) and is the stated structural fix for ED-545 ("only 5 Zoom-In triggers" — §7.4,
§8: "the Scene Slate IS the Zoom-In trigger system"). Every other lane's actions (combat, contest,
fieldwork, thread ops, governance) reach the player *through* this verb — cut this and every other
lane's action set loses its entry point into play.

- **N:** passes cleanly. Models a real, load-bearing Renaissance-leadership dynamic — an operative
  or councilor always has more claims on their attention than time to answer them (the design's own
  cited precedent, Pathologic 2's 12-day triage, §1.5). Not abstractable: no existing mechanic
  produces "more opportunities than actions, chosen against real consequence for the unchosen."
- **Ω-a/c (cross-scale, autonomous continuation):** passes. §4.5's per-source consequence table
  (NPC arc resolves via AI/Conviction; territory crisis resolves via faction Govern roll; Duty fails
  at −1 Standing; etc.) is precise and differentiated — the world visibly continues without the
  player, satisfying Ω-c directly, and routes across every scale (personal→faction→territory),
  satisfying Ω-a.
- **Ω-d (pays what it buys):** passes. Duty-vs-Conviction tension (§3.5) is a genuine, undamped
  trade-off — there is no dominant "always pick X" strategy because the highest-priority tiers
  (mandatory, crisis) are exactly the ones with the steepest unpursued-cost, and lower tiers trade
  certain-but-small payoff against opportunity cost of a scarce action.
- **Q-elegant:** passes. Core rule restates in one breath ("more opportunities than actions each
  season; unpursued ones resolve without you, per a named consequence"). Second-order consequence is
  predictable from the §4.5 table without extra rule-reading. External dependency (the cross-step
  pruning algorithm, §4.3, ED-747) is fully enumerated, not a hidden "except when."

**Caveat carried forward (not verdict-changing):** ep-21 (prior edge-playability audit) notes no
stated ceiling on simultaneous mandatory-count, so a pathological season could degrade *every*
discretionary slot to Witness Mode repeatedly. That is a parameter-tuning gap in the trigger
*generation* (scale_transitions §4.3.2), not a flaw in the selection verb itself — routed to the
additive plan, UNDETERMINED intent gate, not scored here.

**Verdict: KEEP.** Criterion: Ω-a/Ω-c cross-scale + autonomous-continuation dominance; Q-elegant.

---

## Action 2 — Step 1: Mandatory Crisis Attendance (incl. internal-priority override)

**Design intent:** force engagement with the handful of conditions serious enough that declining
outright isn't offered (revolt-at-0-Accord, Heresy target, mass battle in player's territory, leader
removal, +4 more via the internal-ordering list) — while still letting the player choose *which*
mandatory crisis to personally attend when several co-fire, via explicit-declaration override.

**As-if-built contribution:** this is Μ-α (pressure as engagement driver) made concrete and the
actual site of the Pathologic-style triage the design cites. Reconciling against the prior
edge-playability dossier (E1–E9): six of eight rows (Settlement Revolt, Heresy, Mass Battle,
Stability Crisis, Companion departure-branch, Recognition-granted) are genuinely well-specced with
real branching decisions and traceable feedback; two rows are markedly thinner (Knot Partner in
Crisis — E6, "no Ob/roll/subsystem cited anywhere in the corpus"; Faction Leader Removal below
Standing 5 — E3, "may intervene" left unspecified) and one has a dangling citation (Recognition
Event's withheld-branch "debt scene per §1," which cites a non-existent file — E8). None of these
are subtractive-worthy on their own terms: **as-if-built**, each of the eight rows models a real,
distinct Renaissance-leadership crisis (a coup, a heresy trial, a siege, an institutional collapse,
a relational rupture, a promotion contested by rivals) — none is Fantasy imposition, duplicate, or
edge-case. The thinness is a build/authoring gap (the mechanic behind two rows hasn't been written
yet, and one citation is stale), which is exactly what the cardinal rule says is not a verdict input.

- **N:** passes for all eight rows as designed.
- **Ω-a/c:** passes — mandatory-crisis-forces-Zoom-In is definitionally cross-scale (faction/
  territory-level state crossing into a forced personal scene) and Ω-c-compliant by construction.
- **Q-robust dramatic legibility:** passes for six rows; the two thin rows (E6, low-Standing E3) fail
  the "what happens if no one acts" one-sentence test *only because the resolution procedure hasn't
  been authored*, not because the category is void of stakes — Knot-crisis's *stakes* are legible
  (P-12 substrate-inseparability), only its *procedure* is missing.

**Verdict: KEEP** (category-level, all 8 rows + the override). The E6/E3-low-Standing/E8 findings are
real but are authoring-completeness gaps, correctly routed to the additive resolution plan — not
reopened here since they were already NEW findings in the prior edge-playability audit (severity P2,
intent NOT-INTENDED), not double-counted as fresh WR findings.

Criterion: N (real, distinct crisis dynamics) + Ω-c (forced, autonomous-consequential).

---

## Action 3 — Step 2: Crisis Events (Priority 1, presented-optional)

**Design intent:** surface five conditions (nearby low-Accord territory, NPC Scar crisis, Knot arc
trigger, global-clock band crossing, NPC conviction-conflict) as *optional* scenes the player may
decline, unlike Step 1's forced rows.

**As-if-built contribution:** each row names a real cross-scale condition (territorial decay
radius, relational-strain threshold, clock-band politics, NPC-faction conviction conflict) that, if
built with a resolvable procedure, would give the player early-warning agency before a condition
escalates into a Step-1 mandatory. This is Μ-δ (cross-scale consequence) operating at the
*optional* tier specifically — giving the player a chance to intervene before pressure becomes
forced. The prior edge-playability audit (E10) found all five rows mechanically thin ("no Ob, no
pool, no subsystem pointer... reads as flavor menu"), but per the cardinal rule that is a
spec-incompleteness finding about the underlying `scale_transitions_v30.md` §4.3.3 rows, not a
verdict on whether the *category* (early-optional-crisis-signal) belongs in the Slate. As-if-built
with a resolvable procedure per row (which several sibling systems in other lanes already supply —
e.g., Govern/Fieldwork/Thread-op actions are the obvious consuming mechanics), this passes N (real,
distinct escalation-prevention dynamic, not covered by Step 1's forced-crisis rows) and Ω-a
(explicitly cross-scale by construction).

**Verdict: KEEP.** The thinness (E10, already NEW/P3/UNDETERMINED in the prior audit) is an
authoring-completeness matter for the additive plan, not reopened as a fresh WR finding here.

Criterion: N (distinct early-warning dynamic, not duplicate of Step 1's forced crises).

---

## Action 4 — Step 2b: Thread-State Scenes (ED-674)

**Design intent:** surface the single highest-priority Thread-substrate condition in the player's
current territory (Critical MS, threshold-crossing, active Gap, active Lock, WC advance), capped at
one per Slate.

**As-if-built contribution:** this is Μ-γ (substrate ontology) made a first-class Slate citizen with
real discipline — the "max 1 per Slate, highest priority fires" rule (§4.2 Step 2b) is a genuinely
elegant scarcity device that prevents the Thread layer from crowding out every other Step, while
still guaranteeing the substrate is never invisible when it matters. This is precisely the kind of
rule the sibling qualitative audit's Thread-silence refutation credits as "the sanctioned cross-scale
pattern" (cited in the prior edge-playability dossier's P-14 closing note) — Thread events proper
*do* reach the player through this row.

- **N:** passes — Gap/Lock/WC/MS-band are exactly the load-bearing substrate mechanics this game's
  central ontology requires a presentation surface for.
- **Ω-a:** passes strongly — this row *is* the substrate-to-personal-scale bridge.
- **Q-elegant:** passes — "one Thread-State scene max, highest-priority wins" is a one-sentence rule
  with a fully predictable second-order consequence (no double-counting, no thread-fatigue from
  Slate-side stacking).

**Verdict: KEEP.**

Criterion: Μ-γ/Ω-a substrate-to-personal bridge; Q-elegant scarcity discipline.

---

## Action 5 — Step 3: Duty-Aligned Scenes

**Design intent:** translate the season's single assigned faction Duty (Investigate/Diplomacy/
Governance/Protection/Reconnaissance/Subversion/Thread Operation/Escort) into 1–2 concrete scene
opportunities in the relevant territory/NPC.

**As-if-built contribution:** this is the mechanism that answers §8's own stated problem — "why does
investigation/diplomacy/etc. matter this season" — by grounding an abstract faction-AI priority
output in a concrete personal-scale scene. It is Ω-a by definition (a faction-scale need generating
a personal-scale opportunity) and Ω-b-adjacent (repeated Duty pursuit is how Standing, and
eventually stature, changes the player's relationship to the faction layer — a personal
transformation with institutional stakes). Duplicate-coverage check: does this overlap with Step 1
(Mandatory) or Step 2 (Crisis)? No — those are triggered by *world state* independent of the
player's assigned Duty; Step 3 is triggered by the *player's own faction assignment*, a genuinely
distinct source with no other Step covering it.

**Verdict: KEEP.**

Criterion: Ω-a (faction-need → personal-scene translation) with no duplicate source.

---

## Action 6 — Step 4: Conviction-Aligned Scenes (incl. the ~25-keyword + role-reference validator)

**Design intent:** scan the player's self-authored Convictions for NPC/faction/territory/system-
keyword/role matches and surface intersecting scenes (max 3), so player-invented goals (the "forge a
secret alliance no AI priority stack would generate" case, §2.4) get scenes without needing to be
pre-scripted.

**As-if-built contribution:** this is the mechanism's strongest case for Disco Elysium-style
player-authored meaning (§1.3) reaching the engine mechanically rather than staying purely narrative
— a genuinely novel capability (no other Step lets the *player's own prose* steer generation). It
passes N (models a real "a leader's stated ambitions shape what opportunities find them" dynamic) and
Ω-a (personal authorship → concrete cross-system scene).

**Q-elegant concern (the reason for the verdict below):** the core Step-4 rule restates cleanly in
one sentence ("your Convictions are scanned for name/faction/territory/keyword/role matches; matches
generate scenes"). But the validator layered on top (ED-746, extended per ED-766) — strong-match /
weak-match / no-match, with a **capitalization-as-semantic-disambiguation heuristic** ("order" vs.
"Order," "crown" vs. "Crown") — asks the player to encode intent through a punctuation-adjacent
signal that is not restatable in the same breath as the core rule, and whose second-order consequence
(a lowercase "the crown on his head" silently never firing Step 4, with only a chargen-time
non-blocking suggestion as the tell) is not predictable without a second read of §4.2 Step 4's
validator-behavior table. This is a genuine Q-elegant fail on the *disambiguation mechanism*
specifically, not on Step 4's core scan-and-match rule.

**Verdict: REFINE.** Keep Step 4 itself (KEEP-grade on N/Ω); simplify the validator to a single
explicit yes/no confirmation dialog at Conviction-write time ("Did you mean the political entity
Crown? Y/N") rather than a silent capitalization convention the player must already know to apply.

Criterion: Q-elegant (second-order consequence not predictable without re-reading the validator
table).

---

## Action 7 — Step 5: NPC Outreach / Demand Scenes

**Design intent:** when a high-Disposition NPC has an actionable priority-tree hit, or a
hostile-authority NPC targets the player's faction, generate an outreach/demand scene; declining a
demand costs Disposition −1 and +1 Exposure.

**As-if-built contribution:** this operationalizes the §2.1 vocabulary-unification claim directly —
"an NPC's argument can target a player's Conviction... this symmetry means the world affects the
player the same way the player affects the world." Step 5 is the concrete instance: NPCs act on the
player via the same Disposition/priority-tree machinery the player uses on them. It is
Ω-c-compliant (autonomous NPC priority firing generates the scene, not player action) and carries a
real, priced cost for declining (Ω-d: ignoring a demand isn't free). Duplicate-coverage check against
Step 6's "NPC arrival": Step 5 is gated on Disposition thresholds and an NPC's own priority-tree
firing — a substantially more rigorous, causally-grounded trigger than Step 6's ungated generic NPC
arrival (see Action 8 below, where this asymmetry is exactly the finding).

**Verdict: KEEP.**

Criterion: Ω-c (autonomous NPC-driven scene) + Ω-d (priced decline).

---

## Action 8 — Step 6: Territorial Scenes

**Design intent:** generate 1–2 scenes per season from the player's current territory: NPC arrival,
trade/economic event, Thread phenomenon (gated on local MS ≤ 60), military movement.

**As-if-built contribution — where this fails the pessimist bar:** two of Step 6's four sub-rules are
**duplicate coverage** of sibling Steps that already do the same job with more rigor:
- "Thread phenomenon (if MS ≤ 60 in this territory's Calamity band)" duplicates Step 2b's
  Thread-State Scene, which already covers the identical local-MS-band condition with a stricter
  trigger (Critical/threshold-crossing/Gap/Lock/WC) *and* an explicit max-1-per-Slate discipline
  Step 6 does not share — so even as-if-built, Step 6's Thread-phenomenon sub-row either (a) never
  fires because Step 2b's stricter, higher-priority row already claimed the "one Thread scene" slot,
  making it dead weight, or (b) fires as a second, undisciplined Thread scene in the same Slate,
  contradicting Step 2b's own "max 1" rule. Neither outcome is acceptable by design.
- "NPC arrival" duplicates Step 5's NPC Outreach with strictly less rigor: Step 5 requires Disposition
  ≥ ±2 *and* an NPC priority-tree firing; Step 6's "NPC arrival" cites no comparable gate at all — it
  is the same content category (an NPC shows up and something happens) minus the causal grounding
  that makes Step 5 pass Ω-c cleanly. A generic, ungated NPC-arrival row sitting alongside a
  rigorously-gated NPC-outreach row is the textbook N failure mode "duplicate coverage": two
  mechanics modeling the same dynamic, one strictly weaker.

The remaining two sub-rules ("trade/economic event," "military movement") are the genuinely novel
content in this Step — ambient political/economic texture distinct from anything Steps 1–5 cover —
and would pass N/Ω on their own if isolated.

**Verdict: MERGE.** Fold the Thread-phenomenon sub-rule into Step 2b (it is already the more rigorous
home) and the NPC-arrival sub-rule into Step 5 (same reasoning), leaving Step 6 a slimmer
"Territorial Texture" generator carrying only trade/economic events and military movement — no lost
decision, since the folded content was either dead-weight or a strictly-dominated duplicate of an
existing, better-specified row.

Criterion: N — duplicate coverage (Thread-phenomenon vs. Step 2b; NPC-arrival vs. Step 5).

**Retires/shrinks:** shrinks the Step-6 generation-branch surface named in the resolution plan's
`C-INJ-7/8/9` row ("zoom rows name queueing call sites... the §25 witness row," lane WR/IN) by two
sub-branches once wiring begins — one fewer redundant branch to author, wire, and Godot-port.

---

## Action 9 — Step 7: Ambient Scenes

**Design intent:** generate exactly one "unstructured encounter offering low-stakes information or
minor relationship opportunity" per Slate, lowest priority (5) of all seven Steps.

**As-if-built contribution — where this fails the pessimist bar:** §4.5's own consequence table is
explicit and unambiguous: unpursued Ambient scenes produce **"No consequence. The world moved on."**
Read the same table for *pursued* Ambient scenes and the design offers nothing more — "low-stakes
information or minor relationship opportunity" is the entire content spec, with no Ob, no pool, no
named subsystem, and (per its own priority ranking) explicitly the least-important content in the
entire Slate. Judged as-if-built at maximum fidelity to its own one-line spec, this is the cleanest
textbook case of the Failure Lexicon's **Flavor-only** entry (fails Ω, Μ-γ, М-3: "adds no decision
the player weighs") anywhere in this lane. It is not Fantasy imposition (N is fine — ambient color is
a legitimate genre expectation) and it is not dominant (there's nothing to dominate) — it simply
costs a fully-documented, independently-numbered generation Step (its own §4.2 paragraph, its own row
in the §4.3 cross-step pruning table, its own row in the §4.5 consequence table) to produce a
mechanic that, by its own text, changes nothing and risks nothing. That is design cost paid for zero
decision-weight — the opposite of Ω-d's "pays what it buys," inverted: here the *design* pays a
documentation/wiring cost that the *mechanic* does not buy back in player decision-weight.

The one legitimate function Ambient serves — never presenting a suspiciously-sparse or "dead" Slate
in a quiet season — is real UX value, but does not require a dedicated, independently-specified,
independently-prioritized generation Step to deliver.

**Verdict: DISTILL.** Retain the backfill *effect* (never surface an emptier Slate than the
difficulty band's floor) as a fallback clause on Step 6 (Territorial Texture, post-Action-8 merge)
rather than a standalone Step with its own priority tier, pruning row, and consequence-table entry.

Criterion: Failure Lexicon "Flavor-only" (Ω/Μ-γ/М-3) — adds no decision the player weighs.

**Retires/shrinks:** folds into the same `C-INJ-7/8/9` generation-branch wiring surface — one fewer
independent Step to author/wire/port beyond the Action-8 merge.

---

## Action 10 — Witness Mode: Free Read/Appraise

**Design intent (ED-745, revised ED-761):** when mandatory-scene count exceeds the scene-action
budget, the player attends what they can and the rest resolve in Witness Mode; each Witnessed scene
grants one free (but rollable, Ob 1) Read/Appraise — success gives reliable surface information,
failure gives unreliable perception.

**As-if-built contribution:** this is a genuinely well-built consolation mechanic, already vetted
favorably by the prior edge-playability audit (E9: "one of the better-specced fallback systems in
the cluster... PLAYS-WELL as a degraded-but-legible fallback"). It passes N (models the real dynamic
of a leader triaging crises still getting *partial, fallible* intelligence on what they couldn't
personally attend, rather than either full omniscience or total blackout), Ω-c (the underlying scene
still resolves via NPC AI regardless of the roll — the roll changes only the player's *information*,
not the outcome, correctly preserving "world continues without you"), and Q-elegant (one-sentence
restatement: "free Ob-1 Read/Appraise; fail = unreliable info" — fully predictable).

**Verdict: KEEP.**

Criterion: Q-robust/Q-elegant fallback with a real pass/fail stake (unreliable vs. reliable info),
Ω-c-preserving.

---

## Action 11 — Witness Mode: Narrative Input Sentence

**Design intent (ED-745):** per Witnessed scene, the player also gets "one narrative input
opportunity at scene resolution (one sentence, GM may incorporate or reject; videogame: pre-scripted
dialogue branch tagged to player Conviction)."

**As-if-built contribution — where this fails the pessimist bar:** this repo's own foundational
invariant is **"There is no GM — the engine resolves everything"** (CLAUDE.md header). The mechanic
as written is defined in terms of a GM's discretionary judgment call ("may incorporate or reject")
and only gestures at a videogame translation in a parenthetical, which collapses the mechanic into
something categorically different: a **menu pick among pre-authored dialogue branches tagged to a
Conviction** — not an "input," a selection. Judged as-if-built at that videogame-faithful
translation: the scene's mechanical resolution has *already* proceeded via NPC AI (§4.2 Step 1 point
2, third bullet: "as if the player had declined to engage") *before* this sentence is offered, so the
branch-pick cannot itself change any world-state outcome — it is decorative flavor color layered on
an already-resolved scene. This is the Failure Lexicon's **Flavor-only** entry a second time in this
lane (adds no decision the player weighs, since the underlying resolution is fixed before the pick is
offered), compounded by a structural mismatch: the design's own tabletop origin ("GM may incorporate
or reject") was never actually re-derived for the stated no-GM engine invariant, it was merely
annotated with a parenthetical workaround.

**Verdict: DISTILL.** Fold the narrative-color beat into Action 10's roll outcome directly (e.g., a
Read/Appraise success additionally unlocks one flavor-tagged dialogue line at the next scene
involving that NPC) rather than carrying it as a second, independently-specified Witness Mode
sub-mechanic that requires its own GM-less translation the corpus never actually performed.

Criterion: Failure Lexicon "Flavor-only" (Ω fail — no decision weight, resolution already fixed) +
structural mismatch with the no-GM engine invariant.

**Retires/shrinks:** removes the open task (implied by `C-INJ-7/8/9`'s "the §25 witness row") of
inventing a GM-less equivalent for open-ended narrative input from scratch — the merged form (Action
10 + flavor unlock) needs no such invention.

---

## Lane summary

Judged as-if-built, the Scene Slate umbrella (Action 1) and five of its seven generation Steps
(1, 2, 2b, 3, 5) plus one Witness Mode sub-action (10) are the strongest, most load-bearing meta-
mechanism this audit is likely to find anywhere in the corpus: it is the literal connective tissue
turning every other lane's action set into a coherent seasonal choice, it is explicitly cited as the
structural fix for a named editorial gap (ED-545), and its cross-step pruning (ED-747) and
Witness-Mode fallback (ED-745/761) are genuinely elegant scarcity devices. The pessimist pass earns
its keep on the two lowest-priority generation Steps and one Witness Mode sub-action: Step 6
(Territorial) duplicates two more-rigorous sibling Steps and should MERGE its Thread/NPC-arrival
content into them; Step 7 (Ambient) is a textbook Flavor-only Step that should DISTILL into a Step-6
backfill clause rather than its own numbered priority tier; and Witness Mode's narrative-input
sentence is a tabletop-GM mechanic never actually re-derived for this engine's stated no-GM
invariant, and should DISTILL into the Free Read/Appraise roll's outcome. Step 4's keyword-match
validator is sound in intent but fails Q-elegant on its capitalization-based disambiguation
mechanism and should REFINE to an explicit confirmation prompt. None of the eleven actions rate a
flat CUT — even the subtractive verdicts preserve the underlying decision or UX effect, just at a
cheaper, less-duplicative, better-legible cost.

