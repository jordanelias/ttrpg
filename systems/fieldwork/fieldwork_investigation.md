# VALORIA — FIELDWORK SYSTEM v1.1 — §4 Investigation
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: TTRPG / Hybrid / Board Game / Godot

## §4 INVESTIGATION

### §4.1 Evidence Track

Investigation is a structured process of assembling knowledge. Each investigation has an **Evidence Track** — a progress clock that fills as the investigator gathers pieces.

**Evidence Track range:** 0 to threshold.

| Investigation scope | Threshold | Examples |
|-------------------|-----------|---------|
| Simple question | 3 | "Who stole the seal?" "Where is the hidden passage?" |
| Complex question | 5 | "What is the Church hiding in Himmelenger?" "What happened at the Einhir site?" |
| Structural question | 8 | "How does the Calamity mechanism work?" "What is the Restoration's true plan?" |

The GM sets the threshold at investigation opening. The threshold is not known to the player (unless the investigation is institutional — Church Heresy Investigations have published procedure lengths per social_contest_v30.md §7).

**Evidence Track progress is persistent across scenes and sessions.** An investigation begun in one session can be continued in the next. Evidence does not decay (knowledge, once assembled, remains assembled). However, the world may change around the evidence — a witness may be killed, a document may be destroyed, a site may be altered by Thread operations.

**One track per investigation, regardless of territory.** An investigation into "What is the Restoration's true plan?" might require evidence from T6, T13, and T15. The Evidence Track is unified — progress from any territory contributes to the same track. Exposure, however, is tracked per territory. Investigating in T6 then moving to T13 accumulates Exposure independently in each.

**Depth-limited resolution:** When the Evidence Track reaches its threshold, the investigation resolves at the deepest depth the investigator has accessed. Progress above the threshold has no additional effect. If the answer lies at Depth 4 but the investigator conducted only Depth 1-3 actions, they receive a partial answer — everything the evidence supports up to the depth accessed. The GM communicates this clearly: "You have assembled a complete picture of everything that is available at your level of perception. There is more, but it is beyond your current reach." Investigation can be reopened at greater depth if the character later acquires the perception prerequisites (gains TS, builds Disposition with a key informant, gains institutional access).

**Resolved investigation produces a Finding.** The Finding's reliability equals its strongest constituent evidence tag. A Finding can be cited in a Contest as a complete argument — the orator references a coherent body of evidence, not individual clues. A Finding containing only Thread-verified evidence is admissible only to TS ≥ 30 audiences (and remains Inert Knowledge for non-sensitives). A Finding containing Documentary or Verified evidence alongside Thread-verified evidence uses the non-Thread tag for admissibility (the Thread-verified components are treated as supporting context, not the evidentiary foundation).

### §4.2 Investigation Actions

Each investigation action represents one scene of focused inquiry. A character can perform 1–2 investigation actions per scene. Each action is a roll.

| Action | Primary Attribute | What it does | Depth access |
|--------|-------------------|-------------|-------------|
| Examine | Cognition | Study physical evidence, architecture, documents, objects | Up to Hidden (2); Buried (3) if TS ≥ 10 |
| Interview | Attunement | Question a witness, informant, or subject | Up to Hidden (2); Buried (3) at Disposition +3 |
| Research | Recall | Consult archives, oral histories, institutional records, Einhir documents | Up to Hidden (2); Buried (3) at institutional access |
| Surveil | Cognition | Observe a location, person, or faction operation over extended time | Up to Hidden (2). +2 Exposure (conspicuous activity). |
| Thread-Read | Attunement | Perceive Thread-level configurations via perceptive Leap (§4.5) | Depth 3–5. TS ≥ 30 required. Co-movement fires (P-01). +1 Exposure. |
| Reconstruct | Recall | Assemble existing evidence into a coherent picture. No new information gathered — this action synthesises. | Any depth already reached. Ob = (threshold − current progress), min 1. On success: reveals what the assembled evidence implies. |

**Evidence progress by degree:**

| Degree | Progress | Exposure | Additional |
|--------|----------|----------|------------|
| Failure | +0 | +2 | GM may offer a misleading clue (false lead). The investigator does not know whether the clue is genuine. |
| Partial | +1 | +1 | One incomplete detail. Enough to know something is there; not enough to know what. |
| Success | +2 | +0 | One reliable detail. Actionable information. |
| Overwhelming | +3 | −1 (elegant work) | Reliable detail + one bonus revelation from an adjacent line of inquiry. +1 Momentum. |

### §4.3 Evidence Quality and the Epistemological Barrier

Evidence gathered through fieldwork has a **reliability tag:**

| Source | Tag | Can be used as... |
|--------|-----|-------------------|
| Examine (physical) | Verified | Court evidence, Contest corroboration, Domain Action justification |
| Interview (witness) | Testimonial | Contest argument (Memory genre); −1 reliability if witness hostile to presenter |
| Research (archival) | Documentary | Court evidence, Contest corroboration (+2D Recall bonus per Contest §4 Step 3) |
| Surveil | Observational | Intelligence (faction action), Contest argument; Exposure cost makes it expensive |
| Thread-Read | Thread-verified | Actionable only by TS ≥ 30 characters. Inert Knowledge for non-sensitives. Cannot be presented in Church Tribunal as evidence (heretical methodology — this is an institutional restriction, not an epistemic one; the evidence is real but the Church rejects Thread-based methodology). |
| Rumour (social) | Unverified | Not admissible. Directional only — suggests where to investigate, not what happened. |
| Reconstruct | Derived | As strong as weakest constituent evidence. Cannot exceed source reliability. |

**The epistemological barrier (P-08) governs evidence transmission:**
Thread-verified evidence cannot transfer its full epistemic content to non-sensitive receivers. A sensitive investigator who perceives a Thread scar's configuration can *describe* it to a non-sensitive colleague, but the colleague receives Inert Knowledge — they can recite the description but cannot act on it with Thread-level precision. In mechanical terms: Thread-verified evidence contributes to the Evidence Track for non-sensitive investigators at half value (round down, minimum 0).

**Investigative asymmetry, both directions:** Sensitive characters access deeper layers but generate more Exposure and produce institutionally inadmissible evidence. Non-sensitive characters are capped at Depth 2 without social mediation but generate lower Exposure at Depth 3+ POIs (+0 vs +1) and produce universally admissible evidence. The optimal investigation team contains both.

### §4.4 Desperate Trail (Fail Forward)

Trails never go cold — they become more dangerous. After 3 consecutive failed investigation actions (net successes ≤ 0) targeting the same investigation, the investigation enters **Desperate Trail** state. The Evidence Track remains open, but conditions escalate:

- **TN shifts to 8** (Desperate) for all subsequent actions on this investigation. The easy approaches are exhausted; what remains demands risk.
- **Exposure doubles** on failed rolls (+2 base becomes +4; +1 becomes +2). The character is now pressing into places and asking questions that attract serious attention.
- **The GM introduces a complication** — a new obstacle that is itself consequential. The witness who could help is under Church surveillance. The archive is guarded by someone with their own agenda. The site is inside a territory that just changed hands. The complication is not a wall; it is a new situation that must be navigated, producing its own story.
- **Evidence progress on Partial improves to +2** (from +1). The desperation itself produces insight — every remaining action that lands, lands harder, because the investigator is now operating at the edge of what is accessible.

Desperate Trail clears when: (a) any single action produces a Success or Overwhelming result (the breakthrough resets conditions — TN returns to 7, Exposure normalises); or (b) the season changes (new circumstances, new access, fresh start).

**Desperate Trail persists through Compromised.** If doubled Exposure triggers Compromised (scene ends, must leave territory or go to ground), the Desperate Trail state does not clear — going to ground is not a breakthrough. The character emerges from ground still on Desperate Trail. Leaving the territory resets Exposure but does not clear Desperate Trail (the investigation is still desperate). Only a successful roll on this investigation, or a new season, resets conditions.

**Design principle:** Investigation failures should never produce "nothing happens." A failed Examine reveals that the evidence has been tampered with (who tampered with it?). A failed Interview means the informant was frightened by something (what frightened them?). A failed Research discovers the relevant archive section has been removed (by whom?). Every failure is a clue about the forces working against the investigation.

### §4.5 Thread-Read as Perceptive Leap

Thread-Read is a **perceptive Leap** — the practitioner enters active Thread contact (per threadwork_redesign_v25.md Leap procedure) to perceive Thread-level configurations rather than to manipulate them.

**Procedure:**
1. Declare Thread-Read. Requires TS ≥ 30. The practitioner must not be in melee with a declared attacker.
2. **Leap.** Follow standard Leap procedure: full-round action (Priority 5 in combat time; one scene action in fieldwork time). Vulnerability window applies — the practitioner is in Thread contact and exposed.
3. **Perception.** Roll Attunement × 2 + History bonus, TN 7, Ob per Depth. Add Thread Pool Score (TS ÷ 10, round down) as bonus dice.
4. **Co-movement fires (P-01).** Thread-Read is a genuine Thread operation. Three-dimensional auto-effects apply per threadwork_redesign_v25.md §3.2: temporal auto-effect (Calamity Drift + History Resonance), epistemic auto-effect (Truth modifier, investigation/testimony consequences), actualized auto-effect (d6 consequence table).
5. **Coherence cost.** Per scale table (stage11 §11.1): Object/Personal scale = 0 auto-cost; Relational+ scale = −1 Coherence.
6. **Evidence progress.** Apply degree result per §4.2 table.

**Thread-Read is the only fieldwork action that produces co-movement.** All other fieldwork actions (Examine, Interview, Research, Surveil, Reconstruct, social actions) are rendering-level activities that do not enter Thread contact and do not trigger P-01.

### §4.6 Contested Investigation

When two parties are investigating the same question (or one party is investigating while another is concealing), the investigation becomes **contested.**

**Concealment Pool:** The concealing party rolls (Cognition × 2) + relevant History, TN 7. Their net successes set a **Concealment Ob** that the investigator must exceed in addition to the base Ob.

This resolves per action, not per investigation. Each investigation action faces: base Ob (from Depth) + Concealment Ob (from opponent's concealment roll for that scene). The concealing party must actively maintain concealment — each scene they are not present to conceal, the Concealment Ob is 0.

**Church Heresy Investigation** is a specific institutional form of contested investigation. The Church's Concealment Ob equivalent is its investigatory bonus (+1D Investigate, +2 Ob for targets in Church territory with Inquisitor). See social_contest_v30.md §7 and params_board_game.md §Church Attention Pool for the BG-scale version.

---

