# Inverted Critic Pass — Lane FI (Field Investigation)

Independent Sonnet critic, read-only. Method: steelman every condemned action against the charter's
N/Ω/Q criteria, judged strictly as-if-built (CLAUDE.md/charter cardinal rule). Two actions in this
dossier carry subtractive verdicts: **Interview (MERGE)** and **Dialogue Lattice (REFINE)**. Both are
attempted below. The six KEEP verdicts were spot-checked against source text (fieldwork_v30.md §4.2
tag table, lines 315-320) rather than re-steelmanned in full, per charter instruction.

---

## 1. Interview (fieldwork_v30 single-roll object) — verdict MERGE

**Steelman attempt:** Is there an honest case the bare-roll Interview object survives as-is, i.e. that
the "duplicate coverage" diagnosis is wrong or that the merge direction assumed in the dossier
(retire Interview, canonize the Lattice) is backwards?

- The dossier's own upstream evidence (`designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/
  cluster_C-FI.md`, "Adjudication options" section) shows this is a **genuinely live three-way fork**,
  not a settled direction: Option A keeps `fieldwork_v30`'s single-roll Interview and retires the
  Lattice entirely; Option B ports the Lattice into fieldwork and rewrites Interview; Option C keeps
  both as separate status tiers (fieldwork canonical-for-play, Lattice PROPOSED/aspirational). Two of
  the three live options do **not** end with "retire the bare-roll spec, canonize the Lattice" — the
  dossier's `retires_downstream` field asserts that outcome as if it were already decided when the
  sibling audit explicitly frames it as open.
- Structural case for Interview surviving: it shares an identical Ob/degree/Exposure spine with
  Examine/Research/Surveil (all KEEP in this same dossier, precisely because that spine composes
  cleanly — Q-smooth). Losing Interview to the Lattice would make the fourth Fieldwork investigation
  action structurally unlike its three siblings, trading a uniform, cheap-to-reason-about mechanic for
  one this same dossier's Dialogue Lattice entry (below) flags as failing one-read legibility. On a
  pure Q-smooth/Q-elegant reading, Interview is the *more* composable, not the redundant, object.
- Steelman fails on the actual textual evidence, though: `investigation_systems_v30.md:425`'s own
  Cross-System Integration Table asserts Interview "now routes through Dialogue Lattice + Response
  Matrix **instead of** single Charisma roll" — an explicit, unambiguous supersession claim in the
  corpus's own words, not an inference the dossier constructed. That forecloses a "two-tier, both
  coexist by design" reading (minor NPCs get quick rolls, major NPCs get the Lattice) — nothing in
  either document authors that split; the claim is total replacement, and it's asserted by the
  challenger document, not disputed by the incumbent. The single-roll Interview and the Lattice
  utterance system are two different mechanical answers to one player verb ("question the NPC"),
  and the corpus itself says only one was meant to remain.

**Verdict on the verdict:** The core diagnosis — duplicate coverage of one player verb by two
irreconcilable, contradictory specs — survives the steelman intact regardless of which document wins.
MERGE (i.e., "these two must resolve to one," as opposed to "coexist as parallel systems") is the
correct verdict shape. What the steelman **does** correct is the `retires_downstream` field's
implicit direction: it should not assert "retire the bare-roll spec, canonize the Lattice" as if that
were the dossier's own finding — that specific direction is one of three options still open at
`ED-IN-0016`'s pending CURRENT.md row, and Option A (keep Interview, retire/demote the Lattice) is at
least as textually defensible given Interview's cleaner composition with its three KEEP siblings.
Recommend the field be reworded to name the *collapse*, not presuppose the *winner*: "collapses
`ED-921` + the fieldwork-row half of `ED-IN-0016`/EP-8 from an open two-document contradiction to a
single Jordan-ruled direction (Option A/B/C per `cluster_C-FI.md`) — this dossier does not adjudicate
which."

**No build-state leakage found** — the MERGE verdict rests entirely on the `investigation_systems_v30.md:425`
supersession sentence and the still-open adjudication options, never on either module's `NotImplementedError`
stub state. Compliant with the cardinal rule.

---

## 2. Dialogue Lattice utterance-selection — verdict REFINE

**Steelman attempt:** Is the five-filter Response Matrix chain actually a Q-elegant failure, or is the
dossier over-penalizing legitimate "complexity grounded in the subject matter" (charter §2, N)?

- Real steelman case: Renaissance-era political/religious persuasion genuinely depends on simultaneous,
  independent axes — what the listener knows, what they believe, how they feel about the speaker, what
  they'd trade, and their ethical ceiling. A single-axis NPC-response model would be the *actual*
  N-failure here (Fantasy imposition via flattening). Five filters is arguably the minimum decomposition
  that doesn't collapse a real multi-causal social dynamic into one die roll — this cuts toward KEEP,
  not REFINE.
- Direct read of the source (`designs/scene/investigation_systems_v30.md:314-370`, SYSTEM 4) confirms
  each individual filter (Information / Conviction / Disposition / Compromise / Ethical Framework) is
  independently simple — a lookup table or threshold check. The steelman for "restatable after one
  reading" would need the *composed* pipeline to reduce to something like "the NPC responds according
  to what they can understand, believe, are disposed to, and will trade" — a fair one-sentence gloss of
  intent. If the player only ever experiences the *outcome* (the NPC's reply), the internal filter
  order is engine substrate, not a rule the player must track — comparable to a dice-pool engine whose
  internal math the player doesn't recompute by hand.
- Steelman fails on inspection of the actual branching, though: each filter doesn't just compute a
  value, it can independently **pass / modify / block / escalate** the *outcome type itself* (Filter 3's
  Disposition table alone has five distinct response-character bands, one of which is a hard Block that
  the dossier's sibling C-FI-2 finding shows directly contradicts fieldwork's own "Any Disposition
  always attemptable" rule). That is a materially different legibility problem than "the player doesn't
  need to see the math" — a *designer* extending or auditing this system (and eventually a player
  reading "why did that response happen") cannot restate in one sentence which of five simultaneous
  gate/filter interactions produced a given outcome, because each filter's branch can override or
  redirect the ones before it. This is exactly the corpus's own C-FI-2 finding surfacing as a Q-elegant
  symptom: the chain is complex enough that its own author-adjacent audit missed an internal
  contradiction between two of its rungs.
- The REFINE verdict is also the *correct severity of subtraction*, not just "any subtractive tag will
  do": the Certainty Gate (character-ontological-state-gated dialogue) is a real, load-bearing,
  hard-to-replicate-elsewhere Ω-b mechanic, and the outcome routing into Evidence Track/Case
  Board/Conviction Wounds is real Ω-a cross-scale consequence — nothing here is flavor-only or
  dominant-strategy, which is what would earn CUT/DISTILL/PRUNE instead. The prescribed remedy
  ("simplify the design," per charter §3's Q-elegant-fail row) is proportionate: collapse or expose the
  five-filter chain to a compact, player-legible readout (e.g., a visible "why this response" summary)
  without discarding the underlying model.

**Verdict on the verdict:** REFINE survives the steelman. The N/Ω case for keeping the *underlying
model* is genuinely strong (this is not an over-designed flourish), but the composed five-filter
chain's failure to be one-read-legible is independently confirmed by the corpus's own internal
contradiction (C-FI-2) between Filter 3 and fieldwork's Information Gates — that is direct evidence of
a legibility failure, not just the critic's assertion. REFINE (not CUT/DISTILL/PRUNE) correctly
distinguishes "the model is sound, the presentation/composition needs simplifying" from "the model
itself shouldn't exist."

**No build-state leakage found** — REFINE is argued entirely from the five-filter chain's specified
branching logic and the C-FI-2 cross-document contradiction it produces, never from the module's
`NotImplementedError`/`doc:null` status. Compliant with the cardinal rule.

---

## 3. Spot-check of KEEP verdicts (not fully re-steelmanned, per charter)

Checked against `fieldwork_v30.md` §4.2 evidence-tag table (lines 315-320) directly rather than taking
the dossier's characterization on faith:

- **Examine → Verified** ("Court evidence, Contest corroboration, Domain Action justification"),
  **Research → Documentary** ("+2D Recall bonus... Court evidence, Contest corroboration"),
  **Surveil → Observational** ("Intelligence (faction action)... Exposure cost makes it expensive"),
  **Thread-Read → Thread-verified** ("Inert Knowledge for non-sensitives... Cannot be presented in
  Church Tribunal — heretical methodology") — all four tags carry textually distinct, independently
  citable downstream consequences in the source table itself. This is real evidence against the
  duplicate-coverage attack these KEEPs were defending against, not the dossier restating its own
  claim. Confirmed, not over-generous.
- **Reconstruct** — the "Combined Findings" rule (+1D per additional Finding, max +2D) and the
  Failure/plausible-but-wrong mechanic are both present in the source text as described; the KEEP is
  well-grounded.
- No KEEP verdict in this lane's dossier cites build state as supporting evidence; each `build_state_note`
  is explicitly marked "not a verdict input," consistent with the cardinal rule.

---

## 4. Cardinal-rule compliance sweep (all 8 actions)

Re-checked every `verdict`/`one_line`/`retires_downstream` field in the dossier for build-state
language leaking into the justification itself (as opposed to the quarantined `build_state_note`
field, which is allowed to discuss stub/wiring status). **No violations found** — every subtractive
and KEEP verdict in this lane's dossier is argued from prose-spec content (tag tables, gate/filter
definitions, cross-document contradictions), never from `NotImplementedError` counts or
`module_contracts.yaml doc:null` entries. The one correction issued above (Interview's
`retires_downstream` direction) is a precision fix on an adjudication-direction overreach, not a
cardinal-rule violation.

