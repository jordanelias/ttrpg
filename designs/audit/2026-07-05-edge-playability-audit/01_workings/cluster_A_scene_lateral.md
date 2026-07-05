# Cluster A dossier — scene-scale lateral seams (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md`. Verbatim below._

---

# Scene-Scale Lateral Seams — Playability Audit

**Scope:** combat ↔ social contest ↔ fieldwork/investigation ↔ threadwork. Currency resolved via `CURRENT.md`: combat head = `designs/scene/combat_engine_v1/` (not `combat_v30.md`, which is PARTIALLY SUPERSEDED but still the source for §10 thread-in-combat history); social contest head = `designs/scene/social_contest_v30.md` (rebuild in flight); fieldwork has **no `CURRENT.md` row at all** — `designs/scene/fieldwork_v30.md` is the de facto head by file structure only, an orphaned-from-index currency gap worth flagging on its own.

### E1 · Fieldwork → Combat (exposure/ambush, F-TRANS-01)
1. **MOMENT:** Investigation scene ends abruptly; player is dropped into a combat scene with the ambusher already advantaged.
2. **DECISION:** None at the seam itself — the player made the decisions earlier (how much Exposure to risk); the transition itself auto-fires.
3. **FEEDBACK:** Weak. `scale_transitions_v30.md` §3.9 says "Exposure converts to ambusher Initiative advantage," but combat_engine_v1's actual initiative mechanic (`wrapper.py` `overcommit_exposure`) has no field that ingests fieldwork Exposure at all — the bridge doc specifies an input the current combat resolver has no consumer for. Player cannot trace "I was Watched" → "I lost the first exchange" mechanically, only narratively.
4. **LATENCY:** Immediate (interrupt), dramatically appropriate.
5. **FRICTION:** Full mode switch, investigation scene truncated mid-action ("current fieldwork action resolves... Combat then begins," `fieldwork_v30.md` §2.3). Reasonable — ambush should interrupt.
6. **RECIPROCITY:** Yes, E2 exists.
7. **VERDICT:** PLAYS-ROUGH (declared handoff exists but the concrete numeric hook is unwired in the current engine) · P2 · UNDETERMINED (no evidence either resolver was told to consume the other; looks like drift, not choice).

### E2 · Combat → Fieldwork (battle-site investigation, F-TRANS-09/12)
1. **MOMENT:** Combat ends; player immediately gets an investigation scene at the same site with an Exposure penalty already applied (+1/+2/+3 by loudness, `fieldwork_v30.md` §2.3).
2. **DECISION:** Yes — Exposure tier is a real cost the player feels when choosing how loud to fight.
3. **FEEDBACK:** Good — the +1/+2/+3 tiering is explicit and legible, and the causal chain (loud fight → higher starting Exposure) is one sentence.
4. **LATENCY:** Immediate, appropriate.
5. **FRICTION:** Low — "Combat ends; fieldwork resumes as a new scene," no bookkeeping burden beyond the Exposure add.
6. **RECIPROCITY:** Yes (E1).
7. **VERDICT:** PLAYS-WELL · P3 · DELIBERATE (`fieldwork_v30.md` §2.3, cited procedure).

### E3 · Fieldwork → Contest (Evidence as Appeal)
1. **MOMENT:** Player cites a completed Finding at Contest setup; pool gets +1D/Finding, cap +2D (`social_contest_v30.md` §9.1/F-TRANS-10/11).
2. **DECISION:** Real and legible — investing scenes in fieldwork pays off tangibly in the political arena.
3. **FEEDBACK:** Strong — dice bonus is visible on the roll, Evidence not consumed so the player can see the resource persist.
4. **LATENCY:** Immediate (declared at setup).
5. **FRICTION:** Low — one declaration, no re-litigating the investigation.
6. **RECIPROCITY:** Yes (E4).
7. **VERDICT:** PLAYS-WELL · P3 · DELIBERATE.

### E4 · Contest → Fieldwork (Appraise → Evidence; Disposition shift)
1. **MOMENT:** After a Contest, an Appraise success silently adds +1 Evidence progress (Testimonial tag); adjudicator Disposition auto-shifts ±1 (`fieldwork_v30.md` §2.3 "Contest → Fieldwork").
2. **DECISION:** None — this fires automatically, no player choice at the seam.
3. **FEEDBACK:** Weak/absent. "This is automatic — no additional fieldwork action required" (fieldwork_v30.md §2.3) means the player likely never notices their Evidence Track ticked from a Contest side-effect; there is no cited rendering path (no "the game tells you the Track advanced" line).
4. **LATENCY:** Immediate, but silent.
5. **FRICTION:** None (which is itself the problem — too invisible to register as a consequence).
6. **RECIPROCITY:** Yes (E3), but the return direction is mechanically thinner (auto vs. player-declared).
7. **VERDICT:** PLAYS-ROUGH · P3 · UNDETERMINED (plausibly deliberate low-friction design, but no confirming intent statement, and no feedback path is specified at all).

### E5 · Fieldwork → Thread (Thread-Read as perceptive Leap)
1. **MOMENT:** Player declares Thread-Read mid-investigation; full Leap procedure fires (Contact, Thread Fatigue, co-movement on three axes) before the Evidence roll resolves.
2. **DECISION:** Meaningful — TS≥30 gate, +1 time unit cost, +1 Exposure, and genuine co-movement risk (`threadwork_v30.md` §2.3, `fieldwork_investigation.md` §4.5) make this a real risk/reward call, not a free upgrade.
3. **FEEDBACK:** Good — Evidence progress by degree is explicit, and Thread-Read is flagged as "the only fieldwork action that constitutes a Thread operation and fires co-movement" (fieldwork_investigation.md §4.5), so the player can trace cause→effect (I Leapt → co-movement happened → I got +2/+3 evidence and paid Coherence/Exposure).
4. **LATENCY:** Immediate.
5. **FRICTION:** Moderate but earned — one scene-action, one extra time unit.
6. **RECIPROCITY:** N/A (this is the vertical handoff, not lateral); qualifies as PLAYS-WELL.
7. **VERDICT:** PLAYS-WELL · P3 · DELIBERATE.

### E6 · Personal → Thread (Leap, Contact/Fatigue) — general chair experience
1. **MOMENT:** Any Leap (fieldwork, combat-history, social) suspends the character's rendering; Thread Fatigue counts up (threshold Spirit×5) instead of the old round-based Contact Duration (`threadwork_v30.md` §2.3, ED-694).
2. **DECISION:** Real — practitioners must budget fatigue across multiple operations in one Contact window (Focus sets max ops, not duration).
3. **FEEDBACK:** Clear numeric track, explicit degree table (Overwhelming/Success/Partial/Failure) with legible consequences.
4. **LATENCY:** Immediate.
5. **FRICTION:** Appropriate — this is meant to feel costly (rendering-suspension is metaphysically dangerous per P-08).
6. **RECIPROCITY:** Return-to-Personal is automatic at Contact end (§3.1 handoff) — clean.
7. **VERDICT:** PLAYS-WELL where it applies (fieldwork, social) · P3 · DELIBERATE. — but see E7: this experience is **unavailable in combat**, which is the actual chair-impact worth flagging.

### E7 · Threadwork ↔ Personal Combat (ED-911 — assess impact only)
1. **MOMENT:** Nothing happens — a player who wants to Leap mid-fight has no button to press. `combat_engine_v1` (the ratified resolver) has zero Thread interface; the only Leap-in-combat procedure that ever existed lived in the now-superseded `combat_v30.md` §10.1 ("Practitioner commits all pool to Defence during Leap. ~60% hit probability... Real tactical cost").
2. **DECISION:** None available — the decision "do I risk a Leap while someone is trying to kill me" existed in combat_v30 and does not exist in the current engine.
3. **FEEDBACK:** N/A — nothing to trace, because nothing can fire.
4. **LATENCY:** N/A.
5. **FRICTION:** The friction is total exclusion, not overhead — a whole class of scene (practitioner forced to choose between fighting and Leaping mid-melee) is simply unplayable in the ratified engine.
6. **RECIPROCITY:** N/A.
7. **VERDICT:** MISSING · P1 · NOT-INTENDED (ED-911, status `open`, explicitly logs "thread-in-combat... exist ONLY in the superseded resolution layer with no engine counterpart," `canon/editorial_ledger.jsonl` ED-911, and ED-1029 D9 confirms it is scoped-but-unbuilt). **Chair impact beyond the known defect:** any scene where a Thread-sensitive PC is ambushed (E1) or where a fight breaks out mid-investigation cannot let that PC use their signature capability at all — the character's core verb is silently absent exactly where narrative tension would most reward it (a fight against a mundane threat while trying to decide whether to burn Coherence on a Leap). Ranged and >1v1 combat are equally absent (same ED), compounding the gap for any scene that isn't a clean 1v1 melee.

### E8 · Threadwork ↔ Social Contest
1. **MOMENT:** A practitioner in active Thread contact adds `floor(TS÷30)` bonus dice to Argue (§9.3); a practitioner may fire a Thread operation *between* exchanges (§9.4); an adjudicator with Certainty-indexed reactions (C5 corrupts/suspends the whole proceeding, C3 just deepens internal conflict) responds visibly (§9.4b, ED-667).
2. **DECISION:** Strong — declaring Weaving mid-contest is a visible, risky move (Church may file Heresy Investigation on observation) with a real payoff curve.
3. **FEEDBACK:** Excellent and unusually explicit for this corpus — the Certainty-band table (§9.4b) gives a legible, differentiated NPC reaction the player can predict and exploit.
4. **LATENCY:** Immediate, in-exchange.
5. **FRICTION:** Low-moderate (a declare-before-rolling flag, a post-exchange Coherence check).
6. **RECIPROCITY:** Two-way and substantive (Thread → Contest via bonus dice/operations; Contest events → Thread via the visibility/Coherence checks).
7. **VERDICT:** PLAYS-WELL · P3 · DELIBERATE — **this is the healthiest seam in the cluster** and stands in sharp contrast to E7's combat gap; the same design attention that produced §9.3/§9.4/§9.4b was never extended to combat.

### E9 · Combat ↔ Social Contest
1. **MOMENT (Contest→Combat, §9.6):** "Violence in the contest chamber = immediate forfeit. Violent party auto-loses" (`social_contest_v30_infill.md` §9.6, ED-897). No combat scene is actually triggered — violence is adjudicated as an instant abstract penalty, not a scene-type switch.
2. **DECISION:** None at the seam — a player who "goes violent" in a Contest does not get to fight; they get an auto-loss.
3. **FEEDBACK:** Clear as written, but surprising in play: a player expecting a dramatic combat break-out gets a rules-lawyered forfeit instead.
4. **LATENCY:** Immediate.
5. **FRICTION:** Deliberately minimal (no scene switch at all).
6. **RECIPROCITY (Combat→Contest):** No canonical procedure found for surrender/parley opening a Contest mid-fight — the only related text is a Domain Echo line noting "Player defeats faction officer (incapacitation **or surrender**)" (`combat_v30.md` §Domain Echo table) with no procedure for how a surrender offer is adjudicated, negotiated, or refused.
7. **VERDICT:** Contest→Combat direction is INERT (specified as an instant penalty with no player-perceivable combat experience) · P2 · DELIBERATE (explicit rule, if a narrow one). Combat→Contest (surrender/parley) direction is MISSING · P2 · UNDETERMINED (no citation either way — plausible this was never designed rather than deliberately excluded).

### E10 · `investigation_systems_v30.md` edges (GAP-1, never previously audited)
This doc (NPE / Investigation Interface / Dialogue Lattice / Response Resolution Matrix) is marked `## Status: CANONICAL — approved 2026-04-17` and its own Cross-System Integration table claims: "Interview action now routes through Dialogue Lattice + Response Matrix instead of single Charisma roll" and "Surveil gains spatial context in scene graph."
1. **MOMENT:** As authored, a rich Disco-Elysium-style gated-utterance conversation with a five-filter NPC response chain.
2. **DECISION:** As authored, very high (seven gate types, visible-locked vs hidden utterances).
3. **FEEDBACK:** As authored, strong (Case Board, Thread Layer toggle). **But none of this is consumed anywhere the player actually plays.** `fieldwork_v30.md` §4.2 and its co-file `fieldwork_investigation.md` §4.2 — the actual live Interview/Examine/Research/Surveil actions — are still exactly the pre-proposal single-roll design ("Interview | Attunement | Question a witness... | Up to Hidden(2)"), with zero Gate/Lattice/Genome reference. `sim/personal/investigation.py` confirms this at the implementation layer: `resolve_npe_response`, `evaluate_dialogue_lattice`, and `apply_response_matrix` are all `NotImplementedError` stubs ("Pass 2l armature stub"), while the sibling `sim/world/npe.py` (System 1 only) is actually implemented.
4. **LATENCY:** N/A — the system as a player-facing thing doesn't fire at all; only its NPE-generation half exists in the sim layer.
5. **FRICTION:** N/A.
6. **RECIPROCITY:** N/A.
7. **VERDICT:** INERT — a "CANONICAL" doc whose four systems are 1-of-4 implemented (NPE only) and 0-of-4 wired into the consuming fieldwork mechanics document · **P1** · NOT-INTENDED as a permanent state (the doc's own integration table asserts the wiring exists; that assertion is false against the current fieldwork head — this is a declared-but-unconsumed defect in the same family as the `scene.combat_resolved` gap flagged in the calibration notes, just larger in scope: an entire four-system conversational layer that play never actually touches). Edges this orphans: Dialogue Lattice↔Contest escalation (claimed, never built), NPE-generated minor NPCs↔Scene Slate Priority 4/5 (claimed integration, unverified against player_agency), Case Board Thread Layer↔fieldwork Thread-Read (claimed +1 insight bonus, no hook in fieldwork_investigation.md §4).

## Candidate findings

1. **investigation_systems_v30.md is canonical-in-name only for 3 of its 4 systems.** Player-chair failure: a player attempting Interview expecting Dialogue Lattice gates gets one Attunement roll, exactly as if the proposal had never been written. Citations: `designs/scene/investigation_systems_v30.md` (Cross-System Integration Table), `designs/scene/fieldwork_v30.md` §2.3/§4.2, `designs/scene/fieldwork_investigation.md` §4.2, `sim/personal/investigation.py` (all three entry points `NotImplementedError`). Severity P1. Intent gate NOT-INTENDED (the doc's own table asserts wiring that the consuming doc contradicts).
2. **F-TRANS-01's ambush-Initiative bonus has no receiving field in combat_engine_v1.** Player-chair failure: an ambusher who built high Exposure risk gets no mechanically traceable payoff in the current combat resolver (only `overcommit_exposure`, an unrelated in-fight geometry term, exists in `wrapper.py`). Citations: `designs/architecture/scale_transitions_v30.md` §3.9 F-TRANS-01; `designs/scene/combat_engine_v1/wrapper.py:188-193`. Severity P2. Intent gate UNDETERMINED.
3. **Contest §9.6 "Chamber Violence" forecloses the Combat↔Contest seam rather than opening it, and Combat→Contest (surrender/parley) has no procedure at all.** Player-chair failure: a player who threatens violence in a negotiation never fights — they auto-lose — and a player who wants to negotiate a surrender mid-battle has no rule to invoke. Citations: `designs/scene/social_contest_v30_infill.md` §9.6; `designs/scene/combat_v30.md` §Domain Echo table ("incapacitation or surrender," no procedure). Severity P2. Intent gate: forfeit rule DELIBERATE (explicit), surrender-into-contest MISSING/UNDETERMINED.
4. **Contest→Fieldwork Evidence/Disposition update (§2.3) is fully automatic with no cited feedback mechanism** — likely to be mechanically real but experientially invisible. Citation: `designs/scene/fieldwork_v30.md` §2.3. Severity P3. Intent gate UNDETERMINED.
5. **Fieldwork itself has no `CURRENT.md` row**, unlike every other subsystem audited here — a currency-index gap, not a mechanical one, but it means an agent (or Jordan) resolving "what's the fieldwork head" has to infer it from file structure rather than the authoritative index. Citation: `CURRENT.md` (absence). Severity P3. Intent gate UNDETERMINED.

## Threadwork note (P-14 at these seams)

**Present and well-realized:** Fieldwork↔Thread (E5/E6) and Contest↔Thread (E8) both give Thread a first-class, mechanically distinct channel with real risk/reward and legible NPC-facing consequences (`fieldwork_investigation.md` §4.5; `social_contest_v30.md` §9.3/§9.4/§9.4b).

**Absent and deliberate:** Combat↔Thread is the single explicitly-logged exception — ED-911 (open, P1) states plainly that the ratified engine dropped thread-in-combat from `combat_v30.md` §10 and treats this as an unresolved gap, not silence. That is deliberate-acknowledgment of an absence, not a P-14 violation by omission — but it is the one seam in this cluster where P-14's "every mode expresses inseparability" claim is currently false in the shipped resolver, and it is the single node from which E1 (fieldwork ambush) and E9 (Combat↔Contest reciprocity) both inherit their P1/P2 severity, since neither can route a Thread-sensitive PC's signature verb through the fight that either edge produces.
