# Threadwork × Character-Facing Systems — Cross-System Mapping — 2026-06-11
**Frame (Jordan's design assertion, this session):** threadwork is not a self-contained system but *the playable extension of the game's metaphysics* — per Foundations A1 every rendered thing is thread-configuration, so threadwork **must be applicable to every character-facing system**. This document treats that as a requirement, not a question: where applicability is present I map it; where absent, the absence is a **gap against requirement**, not a design option. Five relations analyzed per system: **maps-onto** (canonical hooks), **alters** (state threadwork writes that the system reads), **impacts** (state the system writes that threadwork reads), **inflects** (visibility/perception recontextualization), **modulates** (response machinery the system runs because thread happened).

**Shared spine (applies in every system, cite once):** wound −1D to all Thread pools (derived_stats §4.1, PP-716); TS visibility table (v30 §2.3, consumed verbatim by combat §10.2 / social §9.4b / investigation ED-680); co-movement fires on all three axes per operation (P-01/P-14); Coherence costs per §3.2 + per-op cap (RD-2 record caveat); Momentum unusable on Thread rolls (params/core); witnesses with engaged Convictions take Scars (npc_behavior §3.4 via combat §10.3 / social §9.4b).

[READ: combat_v30 §10/§10.2/§10.3; social_contest_v30 §9.4/§9.4b; mass_battle_v30 §A.7/§A.10; investigation_systems_v30 Case Board Thread Layer; threadwork_v30 §2.3 Thread-Read block, §2.5; ED-911 verbatim; ED-050 resolution note]

---

## §1 Scene Combat

**Maps-onto.** combat_v30 §10 gives the action-economy slotting: Leap is a **full-round action (Priority 5)**, barred while engaged in melee with an opponent who has declared an attack this round (infill l.38–39); during the Leap round the practitioner commits **all pool to Defence** and still faces ~60% hit probability (§10.1) — "real tactical cost," the document's own words. Only reactive defence (Parry / Dodge Backwards) is available. Two named Weave applications exist in the combat context: W-24 Coherent Strike (range-protected only; ED-046 carries the open design question of whether its Object-scale free-cost is intended) and W-33 Rally the Broken (CP ≥ 3 units only, P-31 note).

**Alters.** Killing a named NPC fires Knot rupture + Conviction Scars on witnesses (§10.3, Death Cascade §13.3); a witnessed Dissolution costs RS *and* Scars all engaged-Conviction witnesses, and drives companion departure for Faith/Order/Equity companions (companion_specification §6.1). Combat is where threadwork's social-metaphysical price is paid in front of an audience.

**Impacts.** Wounds degrade every Thread pool through the floor (true floor 1D, diagnostic Phase 1a) — combat is the principal source of degraded-pool thread play. Health 0 bars the Leap outright (eligibility, v30 §2.3).

**Inflects.** §10.2: every wound and death is *also* a substrate event for TS-30+ observers (thread disruption at the wound site; configuration ceasing to cohere) — feeding fieldwork evidence and Confrontation Development (A10).

**Modulates.** Adjudicator-response machinery does not run here (combat is not a formal proceeding), but faction visibility does (ED-677 extension).

**Gap against requirement — the headline.** **ED-911 (open P1, Jordan):** combat_engine_v1 (ED-900/904) is the ratified canonical resolver and handles strictly 1v1 melee; §10 lives **only on the superseded resolution layer**. So the metaphysics' combat expression currently has *interface rules without a resolver*: nothing canonical says when a mid-combat **operation** (as opposed to the Leap) resolves relative to the engine's structure, what targeting a combatant's configuration means mechanically, or how contact persists across engine rounds. Secondary record defects: §10's pointer to `designs/ttrpg/threadwork_v30.md` is a dead path (N11 family); W-24's cost question (ED-046) is still open.

**Anchored design shapes (Jordan-vetoable; analysis only — the active-work-index combat stream owns execution):**
- *(a) Two-resolver seam* (= ED-911 option a): declare §10 RETAINED-canonical on the combat_v30 chassis; thread ops in combat resolve as threadwork rolls slotted at Priority 5, combat continues around them. Bottom-up anchor: infill l.38–39 + §10.1 already define exactly this seam for the Leap; extending it to operations is one paragraph (operation = full-round action, same defence commitment, fatigue per round per ED-694). Top-down anchor: Burning Wheel's Sorcery-inside-Fight and Ars Magica's combat magic both run a slower-cadence subsystem inside the martial round structure — acclaimed precedent for a deliberate tempo mismatch (thread is *slow* in a fight; that is the Einhir cost made tactical).
- *(b) Engine extension* (= ED-911 option b): add a thread action class to combat_engine_v1. Costlier; buys one resolver. The A.10 *combat-type operations* row ("resolve Phase 4, no Defence allocation unless embedded Threadweaver present; counter = contested roll") shows the mass-battle layer already chose a seam-style answer — consistency favors (a).

---

## §2 Social Contest

**Maps-onto.** §9.4: a practitioner may initiate a Thread operation **between exchanges**; effects apply before the next exchange's Read step. Genre/orientation dice are fixed at setup — Thread cannot rewire the contest's frame mid-stream (an explicit anti-dominance valve). PP-351: a Thread operation on a temporal axis opposing the contest's primary orientation imposes **TN 8 on both orators' next Read roll** — temporal contradiction degrades the whole epistemic field, regardless of whom the practitioner supports.

**Alters.** Operation effects (a Woven reputation, a Pulled memory made vivid) enter the contest as changed ground truth before the next Read; Coherence social bands (−1D/−2D, PP-234) price prior thread ambition directly into Argue pools.

**Impacts.** Composure is the shared currency: opposing-op Knot strain pays in Composure (v30 §2.6 tables); Knot partners absorb Composure damage (knots §5) — social standing and thread strain drain one pool.

**Inflects.** Visibility gate (§9.4b): the adjudicator must *perceive* the use (TS bands; concealment = Cognition roll per §2.3).

**Modulates.** §9.4b (ED-667) is the most complete response machinery in the game: Certainty-indexed adjudicator table — C5 voids the proceeding and fires the PP-182 Heresy pathway; C4 imposes +1 Ob procedural suspicion; C3 Scar-checks the adjudicator's own Conviction; C2–0 may quietly convert the technique into +1 Evidence. Scope-limited to formal proceedings — informal argument is unadjudicated by rule.

**Gap against requirement.** None structural — this is the model integration. Two refinements rather than gaps: (i) §9.4 governs ops *between* exchanges; an op attempted *during* an exchange is undefined (presumably impossible — contact windows are scenes-within-scenes — but unstated); (ii) opposing-ops (§2.6) vs a contest's *other orator who is also a practitioner* would let thread duels piggyback on contests — the §2.6 mutual-cost design suppresses it (T7), but no text joins the two procedures. Both are P3 statement gaps, Claude-draftable.

---

## §3 Mass Battle

**Maps-onto.** The deepest mechanical integration of the four. ED-050 (resolved Option D, 2026-04-02): **offensive Thread has its own phase** between Manoeuvre and Engagement; damage defers to Cascade Phase 6 step 1, simultaneous with Engagement damage (§A.7 header). §A.10 supplies the battle-scale operating table: scale mapping (Skirmish→Personal TS30 Ob2 cost 0; Company→Object TS30 Ob1 cost 0; Battle/Campaign→Territorial TS50 Ob4 −1/op; War→Structural TS70 Ob5 −2/op), Diagnosis at Phase 1 (public declaration), Leap at Phase 4/5 by position (PP-101), combat-type ops at Phase 4 with contested-roll counters, command cost (a Threadweaving general forfeits the turn's tactical action), battle-scale co-movement (d3-turn command effects; actual = 1 Wound), collective ops via Reserve helpers, and four edge rules (Devout general EDGE-01 — cannot use *or counter* thread; Severed general EDGE-02; First-Leap-in-battle EDGE-03; Gaps register on the territory card EDGE-05).

**Alters.** Battle-created Gaps land on the territory card with standard MS drift (EDGE-05) — battles permanently scar the substrate map. PP-501's worked example: a practitioner operating all 7 turns ends at Coherence 3.

**Impacts.** Reserve status gates collective participation; unit CP gates W-33; Devout leadership *denies* the entire layer (Conviction as thread-counterplay — elegant: belief is armor).

**Inflects.** Thread intent is declared **publicly** at Phase 1 — at army scale, thread is doctrine, not secret.

**Modulates.** Enemy counters are contested rolls (P2-09); EDGE-01 makes general-selection a thread-strategic choice.

**Gaps against requirement.** Applicability is *present*; the defects are record-class and already filed: (i) the A.10 table runs on the dead taxonomy (N2's reach); (ii) A.10 asserts the per-op cap, cites it to a section that lacks it, and its own War row (−2/op) contradicts the four-witness total-cap reading — **RD-2's outlier cell**; (iii) coordination boundary: the mass-battle canon docket (LA-8, J-9) owns these edits — this analysis feeds it, does not execute.

---

## §4 Exploration / Investigation

**Maps-onto.** Thread-Read is canonically *both* a Thread operation and a fieldwork investigation action — "the only fieldwork action that constitutes a Thread operation and fires co-movement" (v30 §2.3 cross-reference block). Standard Leap procedure; TS ≥ 30; Evidence Track advances when consequences reveal investigation-relevant information (TW-05; fieldwork §2.3/§4.5). Knot-mediated **remote** Thread-Read (TS 30+, +1 strain/use, params PP-632) extends investigation across distance through relationships.

**Alters.** ED-680 Case Board Thread Layer: TS ≥ 30 toggles dual-depth evidence nodes (rendered + substrate); linking rendered evidence to substrate evidence of the same event = the constitutive insight, **+1 Evidence (max 1/investigation)**. Below TS 30, substrate evidence renders only as "something is wrong here."

**Impacts.** Investigation Depth gates Thread-Read's payout: Evidence advances only on **Depth ≥ 4 questions** (P1-16 — stated rationale: prevents Thread-Read trivializing mundane investigation). TW-10: Thread-Read and FR operations are mutually exclusive within a single fieldwork action.

**Inflects.** Combat §10.2 perception is itself investigative input (fieldwork §2.4): wounds and deaths are readable substrate events.

**Modulates.** C2–0 adjudicators converting witnessed technique into Evidence (§9.4b last row) quietly couples social proceedings back into investigations.

**Gaps against requirement.** Applicability strong; defects are record-class: the Thread-Read **stat line** sits inside the fieldwork P1 canonical-line split (master workplan LA-1 — conversion-blocking, already docketed); v30 cites `fieldwork_v30.md` / `fieldwork_investigation.md` while the canonical-sources registry resolves investigation to `investigation_systems_v30.md` (citation drift, N11 family). One genuine content gap: **exploration-as-traversal** (overland movement, hazard, discovery outside investigation framing) has no thread hooks beyond Gap encounters — if exploration is a character-facing system in its own right, Thread-sensing during travel (passive sensing already costs 2 fatigue/round, ED-694 — the price exists; the procedure doesn't) is the missing paragraph. P2, Jordan-vetoable shape: passive sensing as a travel-mode toggle feeding the §10.2-style perception bands.

---

## §5 Verdict against the applicability-everywhere requirement

| System | Applicability today | Blocking item | Class |
|---|---|---|---|
| Social contest | **Full** — model integration (ops slot, response machinery, anti-dominance valves) | — (two P3 statement gaps) | clean |
| Mass battle | **Full mechanically**, defective record | A.10 taxonomy + cap cell (RD-2; LA-8/J-9 docket) | record |
| Investigation | **Full**, defective record + one content seam | LA-1 stat split; exploration-traversal paragraph | record + P2 content |
| Scene combat | **Interface only — no resolver** | **ED-911** (Jordan decision a/b) | structural |

The metaphysics' claim ("applicable to every character-facing system") is **already the system's trajectory** — three of four integrations are substantively complete, and the visibility table + Scar machinery give every system the same perceptual spine. The single structural breach is combat's resolver (ED-911), and the seam-style answer (option a) is the one the rest of the canon already uses. No new P1s are minted by this analysis: every blocking item maps to an existing docket entry (ED-911, RD-2→N8/N2, LA-1, LA-8/J-9).

[CONFIDENCE: high on mappings (all five relations cited to live canon text read this session); medium on the exploration-traversal gap call — it depends on whether Jordan treats traversal as a distinct character-facing system or as investigation's outdoor face.]
