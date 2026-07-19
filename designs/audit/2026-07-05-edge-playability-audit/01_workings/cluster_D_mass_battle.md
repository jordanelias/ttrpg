# Cluster D dossier — mass-battle seams (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md`. Fable reclassification: CF2 (War-scale −2/op vs cap −1/op Coherence
contradiction) is NOT NEW — it is **ED-1010** (open, P1, ledger entry names the §A.10 War-row
contradiction explicitly). Carried in the report as KNOWN-TRACKED with the seam-level playability
impact this dossier adds. Verbatim below._

---

# Mass-Battle Seams — Playability Audit

Currency: `CURRENT.md` L25 confirms mass battle head = `designs/provincial/mass_battle_v30.md` + `mass_battle_integration_v30.md`. Cross-scale procedures live in `designs/architecture/scale_transitions_v30.md` §3.6–§3.9, §4, §11 (settlement scale in `designs/territory/settlement_adjacency_v30.md`).

### E1 · Thread → Mass
1. **MOMENT** Casting into a live battle — Leap declared publicly Phase 1, fired Phase 4 (rear-safe) or Phase 5 (front-conditional). `mass_battle_v30.md` §A.7 PP-101.
2. **DECISION** Real: rear/Reserve = guaranteed cast, front-line = conditional on no declared Phase-5 attacker; scale-tiered Coherence cost (`scale_transitions_v30.md` §3.6, `mass_battle_v30.md` §A.10 table).
3. **FEEDBACK** Weak. Effects "recorded but NOT applied until Phase 6 Step 1" simultaneous with Volley + Engagement (§A.7) — casualties land as one merged pool; no per-source attribution back to the practitioner's specific op.
4. **LATENCY** 2-phase delay (declare→resolve→apply); deliberate (simultaneous-damage rule, PP-505/ED-354).
5. **FRICTION** Coherence auto-depletes with no roll/UI hook described beyond the derived stat readout.
6. **RECIPROCITY** Partial — "Combat-type operations… Counter = contested roll" (§A.10); support ops face none.
7. **VERDICT** PLAYS-ROUGH · P2 · intent split: simultaneous-damage batching is DELIBERATE; opaque per-op attribution and the Coherence-cost contradiction (= ED-1010, KNOWN-TRACKED) are NOT-INTENDED.

### E2 · Mass → Personal (General Duel)
1. **MOMENT** General leaves the tent for single combat — hero-moment framing.
2. **DECISION** Enter (both sides' Command suspends — PP-232/§A.5) vs. decline; genuinely symmetric stakes.
3. **FEEDBACK** Good — wounds, Command-Ob penalties, Stage-1/2 incapacitation are all named, legible states.
4. **LATENCY** 1 exchange/battle-turn, max 5 — can span 5 full 7-phase turns; Stage-2 fires only the *following* turn's Phase 5.
5. **FRICTION** No forcing mechanism exists — a duel requires bilateral consent (PP-506); §3.7's own infill is header-only, empty of any trigger/AI-consent text.
6. **RECIPROCITY** Fully symmetric by design.
7. **VERDICT** PLAYS-ROUGH (mechanically sound, but reachability is unspecced) · P3 · DELIBERATE core (ED-898/PP-506 safeguarded — the "decapitation" line is a *confirmed refutation*, not re-litigated here) with a NOT-INTENDED gap in the enemy-consent trigger.

### E3 · Scene → Mass
1. **MOMENT** A won social/investigation/combat scene should feel like "I set up the battlefield."
2. **DECISION** Spend a pre-battle scene action to farm a buff.
3. **FEEDBACK** I verified directly: `mass_battle_v30.md`'s Phase 1/2/7 text contains **no reference** to §3.8's Command/Volley/Reform bonuses, and `references/module_contracts.yaml` L454 lists mass_battle `consumes: []` — no incoming-Key contract at all. The bonus exists only in `scale_transitions_v30.md` §3.8.
4. **LATENCY** "1 turn duration" — narrow, must be spent immediately.
5. **FRICTION** "Modifier to most relevant unit" has no deterministic selector for a GM-less engine.
6. **RECIPROCITY** None — one-directional.
7. **VERDICT** PLAYS-ROUGH · P3 · DELIBERATE single-source architecture (matches §3.6's identical pattern; a prior audit pass REFUTED calling this "unconsumed," ranking it P3/duplicate-of-ED-151) but the state-carry mechanism and "most relevant unit" selector remain genuinely unwritten — see CF1.

### E4 · Mass → Faction
1. **MOMENT** Ledger consequences land: Military −1/unit destroyed, Discipline −15/−30, MS −1/−2, Accord set/erosion (`mass_battle_v30.md` Part E, §A.13).
2. **DECISION** None — deliberately automatic, "cannot be mitigated by the battle's outcome" (Part E header).
3. **FEEDBACK** Numbers land on named, checkable stats, and §D.1 anchors an aftermath scene to the specific settlement — but that scene's three choices (tend wounded/survey/address) surface local Order/Prosperity, not the Military/MS/Discipline deltas that already fired.
4. **LATENCY** Immediate for MS/Accord; deferred to Accounting for IP/Strain (§E.2) — clean split.
5. **FRICTION** Confirmed calibration item (F-4): `articulation_layer_v30.md` §3.1's 10-trigger Tier-2 list omits `scene.battle_concluded` despite being a registry-declared consumer, and §6.4 falsely claims it "already triggers Tier 2" (prior audit: CONFIRMED, NOT-INTENDED, P2). Net effect at this seam: a decisive battle gets the mechanical D.1 aftermath scene but no dedicated narrative-significance cut scene beyond it — only the annual Tier-3 chronicle.
6. **RECIPROCITY** N/A (accounting, not exchange).
7. **VERDICT** PLAYS-ROUGH · P2 · NOT-INTENDED (per standing confirmed finding, cited not relitigated).

### E5 · Mass ↔ Settlement
1. **MOMENT** Choosing where/how to fight — assault, siege, or bypass a named settlement node with edge-type terrain (river/mountain/coastal) and settlement-type modifiers (Fort Level, Seat +1 Discipline, Port naval reinforcement, Cathedral Casus Belli, Mine Prosperity) — `settlement_adjacency_v30.md` §2.2.
2. **DECISION** Genuinely spatial and strategic; good tradeoff density.
3. **FEEDBACK** Strong — consequences scoped to the settlement's own Order/Prosperity (§2.3), rendered as a graph overlay + battle scene at the destination node (§4).
4. **LATENCY** Siege ticks Order −1/season until surrender — clearly telegraphed.
5. **FRICTION** Low; §5 Open Items flags unlimited edge-traversal capacity as untested balance debt, not a legibility problem yet.
6. **RECIPROCITY** Good — defender invests in Fort Level/garrison symmetrically.
7. **VERDICT** PLAYS-WELL · P3 (siege-turtle residual, CF7) · DELIBERATE.

### E6 · Fieldwork ↔ Mass
1. **MOMENT** History interrupts an investigation — a battle erupts nearby.
2. **DECISION** None for the player — suspension is unconditional (`scale_transitions_v30.md` §3.9 table).
3. **FEEDBACK** Evidence Track state freezes (numbers preserved) but the scene resumes as "1 new fieldwork scene (≠ continuation of suspended scene)."
4. **LATENCY** Instant suspend; resumption timing post-battle is unspecified in seasons.
5. **FRICTION** The player's narrative momentum is discarded even though the Evidence *number* survives — a real "why did my investigation reset" feel, unexplained by any cited rationale.
6. **RECIPROCITY** None — no player lever to shield an active investigation from an incoming battle.
7. **VERDICT** PLAYS-ROUGH · P3 · UNDETERMINED (CF3).

### E7 · Mandatory Zoom "Mass Battle at Settlement"
1. **MOMENT** The player is caught in a battle they didn't choose — high-stakes forced participation.
2. **DECISION** Participate (command/personal combat) vs. escape (Endurance Ob 2, failure = wound) — real binary, real cost.
3. **FEEDBACK** Clear pass/fail; participation drops into the well-specified apparatus above.
4. **LATENCY** Immediate, Priority 0.
5. **FRICTION** Low; minor cross-reference note: §4.3.2's header says mandatory scenes "consume 1 scene action each" while §D.1's *aftermath* scene explicitly does not — these are different scenes (trigger vs. aftermath), not a contradiction, but worth a documentation cross-link.
6. **RECIPROCITY** N/A (world-imposed).
7. **VERDICT** PLAYS-WELL · P3 · DELIBERATE.

### E8 · Contested Figure §11
1. **MOMENT** A duel wound on a Contested Figure should ripple into the strategic layer.
2. **DECISION** Incentivizes "target the CF" in personal combat — but targeting mechanics aren't specified here.
3. **FEEDBACK** Weak — the entire live spec is one bullet: "CF wound during personal combat → +1 Ob to commander's BG tactic rolls for remainder of current battle" (`scale_transitions_v30.md` §11, verified full section, L295–299). No in-fiction notification (contrast §D.2's officer-capture string), no definition of what qualifies a "Contested Figure," no symmetry statement.
4. **LATENCY** Battle-scoped, clear duration.
5. **FRICTION** Player must track an abstract Ob modifier with no rendering hook.
6. **RECIPROCITY** Cannot confirm from text — under-specified.
7. **VERDICT** UNDETERMINED / PLAYS-ROUGH (severe spec thinness, not a design failure I can fully characterize) · P3 · UNDETERMINED.

### E9 · Zoom In/Out during battle
1. **MOMENT** A personal scene (duel, key NPC beat) opens mid-battle without losing the war's thread.
2. **DECISION** System-timed, not player-timed: legal entry points only after Phase 1/3/6-Step-1; mid-phase triggers defer to the next legal point (PP-250).
3. **FEEDBACK** Clean — "Phase 6 continuation… using the updated state from the personal scene" (§4.2); ghost-unit state eliminated (ED-057).
4. **LATENCY** Bounded, but a Phase-5 trigger deferring to after Phase 6 Step 1 can feel like an odd narrative seam (interrupt lands after the fact, not in the dramatic moment).
5. **FRICTION** "Zoom In does not pause the BG clock" (deliberate, PP-109, anti-manipulation) — but no text addresses how simultaneity is *rendered* to the player (battle "happening around you" during a personal scene).
6. **RECIPROCITY** N/A.
7. **VERDICT** PLAYS-WELL mechanically, immersion-rendering gap unaddressed · P3 · DELIBERATE (mechanism) / UNDETERMINED (rendering).

### E10 · Aftermath / named officers / scene generation
1. **MOMENT** Mandatory, free Aftermath scene at the battle settlement — three choice points (tend wounded / survey damage / address population), each with distinct checks and payoffs (§D.1).
2. **DECISION** Real breadth — Endurance/Attunement, Cognition, or Charisma, each producing different consequences (Size recovery, hidden-consequence reveal, Order shift).
3. **FEEDBACK** Strong — named officer NPCs, Disposition shifts keyed to the player's actual command choices, and a legible 1d20-vs-total-Size-loss incapacitation formula with a worked example and an explicit in-fiction notification string (§D.2).
4. **LATENCY** Immediate; officer fate resolved once per battle, not per event — avoids grind.
5. **FRICTION** Low; the absent-player branch ("Where Were You?") covers the non-participation case gracefully.
6. **RECIPROCITY** Good — a persistent named-NPC relationship responds to strategic decisions across battles.
7. **VERDICT** PLAYS-WELL — the best-integrated seam in this cluster · P2 shadow (shares E4's articulation-trigger gap: the mechanical aftermath fires, but no Tier-2 narrative-significance marker does) · NOT-INTENDED for that shadow.

---

## Candidate findings

**CF1 — Scene→Mass bonus has no execution hook in the engine doc (reframed, not new).** `mass_battle_v30.md` §A.7 never applies the §3.8 Command/Volley/Reform bonuses in its own Phase 1/2/7 text, and `module_contracts.yaml` L454 declares mass_battle `consumes: []`. A prior audit pass (`refute_scene-mass-bonus-unconsumed.md`) REFUTED calling this a Q-smooth defect, arguing single-source architecture (mirrors §3.6) and citing ED-151 as the tracked provisional item. I concur with that verdict but flag the concrete player-chair failure it leaves open: nothing in either doc specifies *where the pending bonus is stored* between scene-end and the next battle's Phase 1, nor who resolves "most relevant unit" deterministically — for a GM-less engine that's an implementation cliff, not just a calibration value. Severity P3, duplicate_of ED-151, intent DELIBERATE architecture / NOT-INTENDED residual.

**CF2 — Thread §A.10 Coherence-cost table contradicts its own cap text.** [Fable reclassification: = ED-1010, KNOWN-TRACKED, open P1 in the ledger; the ledger entry names this exact §A.10 War-row contradiction. The seam-level impact stands: a practitioner-general at War scale cannot predict whether a cast costs 1 or 2 Coherence — a direct cost-prediction failure at the Thread→Mass seam.] (`mass_battle_v30.md` §A.10, L524–535.)

**CF3 — Fieldwork→Mass "resume as NEW scene" discards narrative continuity (NEW, P3).** `scale_transitions_v30.md` §3.9 (F-TRANS-06/12): mass battle suspends fieldwork, Evidence Track *numbers* freeze, but the scene resumes as "1 new fieldwork scene (≠ continuation)." No cited rationale addresses the player-facing cost of this reset framing. Severity P3, intent UNDETERMINED.

**CF4 — Mass→Faction/Articulation missing battle_concluded Tier-2 trigger (KNOWN, cite only).** Per the CONFIRMED prior finding (`articulation-battle-concluded-trigger-gap`): `articulation_layer_v30.md` §3.1's 10-trigger list omits `scene.battle_concluded`/`scene.investigation_resolved` despite both being registry-declared consumers, and §6.4 wrongly asserts the trigger already exists. Downstream impact at this cluster: E4 and E10 both fire clean, well-specified mechanical consequences and aftermath scenes, but the corpus's own narrative-significance layer never marks a decisive battle as a flagged dramatic beat — only the annual Tier-3 chronicle captures it. Severity P2, NOT-INTENDED (standing verdict, not relitigated).

**CF5 — General Duel §3.7 infill is empty; enemy-consent/trigger UX unspecified (reframed).** Per the CONFIRMED-then-REFUTED prior finding (`massbattle-general-duel-decap`), the "decapitation exploit" does not exist (bilateral consent required, symmetric Command suspension, capture is a real downside). What survives as residual: `scale_transitions_v30_infill.md` L24 shows §3.7's infill is a bare header with zero elaboration — no text anywhere specifies how a duel is offered/accepted or what an NPC general's decision rule is. Severity P3, intent DELIBERATE core / NOT-INTENDED gap (spec, not exploit).

**CF6 — Contested Figure §11 is two sentences total (NEW, P3).** Full canonical text verified at `scale_transitions_v30.md` §11 (L295–299): one bullet, no definition of what makes a figure "Contested," no symmetry statement, no rendering/notification spec (contrasting with §D.2's explicit capture-notification string). Severity P3, intent UNDETERMINED — too thin to characterize confidently either way.

**CF7 — Siege-turtle: Walls + Shield Wall + idle-clock waiver (corroborating existing hunt note, not yet formally adjudicated).** `mass_battle_v30.md` §A.9 (Walls: +3 DR, no flanking) × §A.6 (Shield Wall +2D Def, blanket per PP-500) × §A.7 Phase 7 terrain exception (no idle-Morale penalty for a defender "behind Walls with no available advance") combine so a besieged defender's decision tree collapses to "hold," with no morale cost for doing so. This is corroborated in-corpus by `designs/audit/2026-07-04-ners-qualitative-audit/01_workings/hunts/hunt_massbattle_minmax.md` Line 4, not yet run through this audit's confirm/refute pipeline. Attacker-side counters (Artillery, Campaign Supply attrition) exist, so it is dominant-but-counterable, not Ω-collapsing. Severity P3 with N-caveat (historically grounded), intent UNDETERMINED.

## Threadwork note (P-14 at these seams)

P-14 requires every mode to express Thread's three-dimensional co-movement — no mode may let a Thread operation fire without it. Mass battle is unusually well-served here structurally: §A.10 authors a dedicated Co-movement table *for this scale specifically* (Temporal: general loses Phase 5 action d3 turns; Epistemic: Command −1 d3 turns; Actual: general takes 1 wound) — better than most seams, which lean on generic Domain Echo. The concrete threat to P-14's *felt* weight at this cluster is the ED-1010 contradiction: if a practitioner-general cannot predict whether a War-scale op costs −1 or −2 Coherence, the co-movement consequence becomes statistically unpredictable rather than legibly costed, which erodes the "coherence-as-visible-price" half of co-movement even though the mechanism itself is present. Secondarily, E6's Fieldwork→Mass suspension doesn't address what happens to an *in-flight* Thread-Read declared during an investigation scene that a mass battle interrupts — whether that partial co-movement consequence still fires is unaddressed, a narrow but real P-14 edge case worth a follow-up ED rather than a full audit line here.
