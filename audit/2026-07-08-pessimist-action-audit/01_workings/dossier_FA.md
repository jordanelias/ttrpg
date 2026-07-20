# FA Lane — Faction / Domain Actions
## Pessimist Subtractive NERS Dossier (Sonnet reconcile pass, read-only)

**Charter:** `designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md`. **Criteria:** `references/throughlines_meta.md` N §0, Ω §1, Q §5, Failure Lexicon §7. **Cardinal rule applied throughout:** every verdict below judges the action *as if built exactly as specified* — stub/unwired/doc:null/sim-superseded status is captured only as `build_state_note` routing metadata, never as verdict evidence.

---

## Reconciliation intro — three vocabularies, one menu

The charter names three unreconciled FA-lane player-action vocabularies. Reading all three plus the actual prose menus they claim to summarize:

1. **`module_contracts.yaml:59-63` `da.*` Key types** (consumed by `faction_state`, `npc_behavior`): `da.antinomian_action`, `da.covert_betrayal`, `da.diplomatic_alliance`, `da.economic_intervention`, `da.public_governance`. This is an **outcome-classification schema**, not a player-facing menu — five buckets a resolved Domain Action's *consequence* is supposed to fall into. `domain_actions` itself is `doc: null` (module_contracts.yaml:479-491) — no doc anywhere defines which concrete verb maps to which bucket. Prior-audit finding **C-FA-12** (`01_workings/cluster_C-FA.md:114`) already names this triple-vocabulary defect; this dossier extends it to a full subtractive disposition.
2. **`sim/provincial/faction_action.py`** — NOT a player menu at all. `faction_take_action()` is the **NPC/AI stochastic selector** (30% faction-unique / 35% Conquest / 20% Muster / 15% Govern, `M7_ASSUMPTION_SIX`) that picks one action per season for autonomous factions. It happens to implement 3 of the general-purpose verbs (Conquest, Muster, Govern) plus a Crown/Church-only faction-unique dispatch. The file is self-flagged `PRE-LPS-1 / PORT-BLOCKING (ED-FA-0004)` — a superseded 5-stat oracle. That is build-state; it is **not evidence against the design merit of Conquest/Muster/Govern**, which are prose-canonical regardless of what the current oracle implements.
3. **The actual player-facing prose menu** is not confined to `faction_layer_v30.md §7` (which is a *turn-sequence placement reference*, not the verb catalog — Phase 4 Priority 3 there lists "Consul, Muster, Govern, Trade, Fortify" only). The real catalog is spread across `params/bg/core.md` **Standard Action Ob Reference** (Muster, March, Govern, Trade, Diplomacy-vs-NPC, Diplomacy-between-players, Formal Crown Treaty, Thread Operation, Investigate/Intel, Spy, Survey, Parliamentary Manoeuvre, Community Organising/Weaving, Dynastic Proclamation, Cultural Reclamation, Martial Governance, Fortify), `faction_layer_v30.md §3` (Treaty 3-phase), `§5.4` (10 named Parliamentary Actions), `§5.5` (Rebuttal), `§2.5` (Resistance Check), `§1.5` (Reconstitute, Claim Masterless), and `params/bg/faction_actions.md` (≈20 named per-faction unique cards, PP-428–442 + later additions).

**Reconciliation verdict on the vocabularies themselves:** vocabulary (2) is not a menu (it is NPC AI selection code) and drops out of the player-menu reconciliation entirely — it is context, not a competing catalog. Vocabularies (1) and (3) *are* a genuine duplicate-authority pair: (3) is the real, detailed, mechanically-specified catalog; (1) is an unmapped 5-bucket abstraction layer sitting on top of it with no crosswalk. That pairing is itself judged as **Action 0** below, since collapsing it is the direct resolution of C-FA-12.

The player-available verb set below is organized as 17 reconciled action-objects (some are named clusters of near-identical prose entries, collapsed only where the underlying decision is provably identical — never for build-state reasons).

---

## Action 0 — `da.*` Key contract taxonomy (the abstraction layer itself)

**Design intent:** classify every resolved Domain Action's outcome into one of 5 buckets so downstream consumers (`faction_state`, `npc_behavior`) can react generically without knowing every concrete verb.
**As-if-built contribution:** if fully authored (a doc, a resolver, a crosswalk), this would let `faction_state`/`npc_behavior` subscribe to *categories* of Domain Action instead of ~35 concrete verbs — a real architectural economy.
**Criterion:** N — Duplicate coverage; Q-elegant.
Even fully built, this creates **two parallel catalogs of the same design space** with no declared mapping: the detailed Standard Action / Parliamentary / faction-unique tables (vocabulary 3) and the 5-bucket `da.*` taxonomy (vocabulary 1). A design that cannot state "Treaty Ratification is `da.diplomatic_alliance`, Outlawry is `da.antinomian_action`, Excommunication is `da.public_governance` or `da.antinomian_action`?" in one uncontested read fails Q-elegant's "core rule restatable after one reading" — not because it's unbuilt, but because as specified *even complete*, the bucket boundaries are underdetermined (is Spy `da.covert_betrayal`? Is Suppress `da.economic_intervention` or `da.public_governance`?). That ambiguity would persist even with full authorship; it is a design gap, not a wiring gap.
**Verdict: REFINE → MERGE.** Fold the 5-way tag as an explicit column on the existing Standard Action / Parliamentary / faction-unique tables (one tag per named verb, ratified once) rather than standing up `domain_actions` as an independent module requiring its own design doc. This directly retires the C-FA-12 defect and the `domain_actions doc:null` closure shrinks from "author a new system" to "add one column + a short crosswalk note."
**Intent gate:** UNDETERMINED — cannot tell from the corpus whether a full crosswalk was intended and simply never written (a NOT-INTENDED gap, which would route to the additive plan) or whether the two-catalog split was itself the design (in which case it is this audit's subtractive call). Flagging both readings; recommend Jordan rule which was meant.
**Severity:** P2. **Calibration:** KNOWN-TRACKED (C-FA-12).
**Retires downstream:** `domain_actions` module-contract closure (one of CLAUDE.md §6's 10 `doc:null` modules) — converts it from new-system authorship to a crosswalk-table task.

---

## Action 1 — Govern (Consul Inward)

**Design intent:** direct domestic administration of an owned territory — raise Accord/Prosperity.
**As-if-built contribution:** the base positive-administration lever; every territory eventually needs it or drifts toward Revolt (Turmoil §2.4 Accord decline). Feeds settlement-layer Prosperity, which feeds Wealth and Trade Network Investment (PP-178) — genuine cross-scale reach.
**Criterion:** N pass (real, load-bearing Renaissance administrative dynamic — a prince who never governs loses the countryside). Ω-a pass (territory Accord change ripples into settlement/social layer). Ω-d pass: costs a full action slot in a season where Muster/Trade/Diplomacy are also competing for the same slot, and Failure has a real cost (`faction.adjust('Sta', -5)` in the oracle mirrors a real Domain Action pool-vs-Ob roll with a stated failure branch). Q-elegant pass: "roll Influence vs Ob, success raises Accord in a controlled territory" restates cleanly in one sentence.
**Verdict: KEEP.**
**Direction:** top-down. **Severity:** P3. **Calibration:** NEW.

---

## Action 2 — Trade (Consul Outward)

**Design intent:** mercantile Wealth generation, tied to Prosperity/geography.
**As-if-built contribution:** the Wealth-side counterpart to Govern; feeds Muster's re-muster gate (§5.7 FSS-LOOP-2) and Trade Network Investment.
**Criterion:** N pass (commercial statecraft — Hafenmark/Guilds identity is explicitly built on this). Ω-d pass: opportunity-cost against Govern/Muster in the same season; +1D bonus at IP≥30/T2 is a situational modifier, not a hidden free-cost buff.
**Note (not a verdict input):** `settlement_layer_v30.md` carries a 5× internal contradiction on the Treasury formula (Prosperity×50 at line 47 vs ×10 at line 169 — prior finding C-FA-2). This is a spec-consistency bug, not a design-intent flaw; it doesn't change what Trade is *for*.
**Verdict: KEEP.**
**Direction:** top-down. **Severity:** P3. **Calibration:** NEW.

---

## Action 3 — Muster (Legionary Inward)

**Design intent:** raise Military via recruitment/mercenary hire.
**As-if-built contribution:** the sole Military-growth lever; gates Conquest (`Mil < 3.0 → invalid`) and battle power.
**Criterion:** Ω-d is the live question. As specified in the *design* (not the sim oracle): Military is capped at 7 (stat ceiling), Wealth=0 disables Muster entirely and inflicts an ongoing Military bleed (§5.7), and an ungoverned territory decays toward Revolt while its faction is spending slots on Muster instead of Govern. That is a real, stated tradeoff web — the design does NOT specify Muster as free of opportunity cost. **As-if-built, this passes Ω-d.** The undamped Mil→Conquest snowball documented in prior finding C-FA-5 is specifically an **oracle defect** (the sim's `_try_muster`/`_try_conquest` don't enforce the Accord-decay or Wealth-gate consequences that the *design* stipulates) — that is build-state, correctly out of scope for this verdict, and is already tracked (C-FA-5) for the additive plan.
**Verdict: KEEP**, with an explicit dependency flagged: the design's non-dominance claim for Muster is contingent on Accord-decay-under-neglect and the Wealth-gate actually being wired together with it — if the additive plan builds Muster without also building those two dampers, Muster becomes dominant *in practice* even though the *design* is not.
**Direction:** forwards (projecting the loop). **Severity:** P2. **Calibration:** KNOWN-TRACKED (C-FA-5 supplies the mechanism evidence; this dossier confirms the design itself is not at fault).

---

## Action 4 — March / Conquest (Legionary Outward, contested = mass battle)

**Design intent:** the strategic decision to attack an adjacent territory; resolution is handed to the MB-lane mass-battle engine.
**As-if-built contribution:** the core territorial-expansion verb — dynastic/military expansion is maximally load-bearing Renaissance material.
**Criterion:** N pass. Ω-a pass strongly: triggers occupation, officer capture, Trigger-1 Stability changes, Accord reset — a single declare-march decision cascades through Stability, Turmoil, and the MB engine, consequences the player can trace but not fully script in advance. Ω-d: the design gates it on Military≥3, exposes the attacker to Trigger-5 officer-loss/Stability costs on Failure, and the defender gets home-field structure (Fort level raises Ob) — a real, costed decision, not a no-brainer march.
**Cross-lane note:** this is the FA-owned *declaration*; the MB lane owns *resolution*. That is intentional layering (strategic decision → tactical resolution), not duplicate coverage — flagging only so the MB-lane dossier doesn't re-litigate the same verb as a competing "MB player action."
**Verdict: KEEP.**
**Direction:** diagonal (cross-scale into MB). **Severity:** P3. **Calibration:** NEW.

---

## Action 5 — Fortify

**Design intent:** raise a territory's Fort level, a defensive investment.
**As-if-built contribution:** the design's only stated counter-lever to Conquest/March — without it, offense has no cost-side friction beyond Military itself.
**Criterion:** N pass (fortification investment is a hallmark early-modern political-military dynamic — trace italienne, garrison economics). Ω-d pass: a real offense/defense allocation tradeoff (a slot spent on Fortify is a slot not spent expanding).
**Verdict: KEEP.**
**Direction:** top-down. **Severity:** P3. **Calibration:** NEW.

---

## Action 6 — Survey

**Design intent:** frontier reconnaissance revealing one undiscovered POI (Resource/Secret/Remnant/Anomaly), Ob keyed to Proximity Rating (distance-decay).
**As-if-built contribution:** a one-time discovery payoff distinct in shape from ongoing administration (Govern/Trade) — ties into `fieldwork_design_v1.md §8.1`.
**Criterion:** N — the Remnant/Anomaly payoff categories are Thread-substrate flavor, which is the setting's own grounding (Μ-γ substrate ontology), not an ungrounded genre import; this is not Fantasy imposition. Distinctness check against Investigate/Intel (Action 7): Survey targets *unclaimed frontier* territory for one-time discovery; Investigate/Intel targets *rival factions* for ongoing intelligence. Different object, different payoff shape, different Ob formula — not duplicate coverage.
**Verdict: KEEP.**
**Direction:** lateral (checked against Action 7 for duplication). **Severity:** P3. **Calibration:** NEW.

---

## Action 7 — Investigate/Intel + Spy (Tribune)

**Design intent:** reveal a rival faction's hidden stats/intent (Investigate/Intel), or specifically its Intel stat (Spy).
**As-if-built contribution:** informs every other decision in the same season — a real "information as a resource" lever, historically grounded (ambassadorial intelligence-gathering was central Renaissance statecraft: Venetian *relazioni*, resident ambassadors).
**Criterion:** N pass. Ω-d / Q-robust concern: pure information-reveal actions produce **no visible world-state change** by themselves (Q-robust's second bullet literally requires "visible, traceable world-state change from player action") — they only change what the player knows. Spy's table entry lists no stated Failure consequence at all (unlike Survey's fully-specified failure branch), which as *specified* (not merely unbuilt) leaves the action's downside undefined — a genuine Q-smooth gap ("external dependencies... 'except when X' flagged and justified" is not satisfied when Failure is simply absent from the table).
**Cross-lane flag:** "Investigate/Intel" targeting rival factions at the strategic scale risks overlapping the FI lane's Observe/Surveil verbs if those are ever generalized past personal-scale targets — noting for cross-lane synthesis, not resolving here.
**Verdict: KEEP**, with a REFINE sub-note: Spy needs an explicit Failure branch (even a mild one — e.g. "target gains +1D on next Intel-directed action against you") before it can be judged as satisfying Ω-d's "pays what it buys" without relying on Survey's better-specified sibling as a template.
**Direction:** lateral. **Severity:** P2. **Calibration:** NEW.

---

## Action 8 — Diplomacy between players (informal, no roll)

**Design intent:** free-form negotiation at the table between players, no mechanical resolution.
**As-if-built contribution:** none distinct from what Treaty's own Phase 2 already provides.
**Criterion:** N — Duplicate coverage. `params/bg/core.md`'s Standard Action table lists "Diplomacy between players | Negotiated | Not a roll" as its own catalog row, while `faction_layer_v30.md §3.3` Phase 2 (Concession declaration) is independently described as "player negotiation at the table; no roll." These are the same beat — free-form inter-player deal-making with zero mechanical resolution — catalogued twice, once as a generic Standard Action and once as a named phase inside Treaty initiation. As-if-built (i.e., even with both fully specified), a player cannot point to a decision available under one heading that isn't already available under the other.
**Verdict: DISTILL → MERGE into Treaty §3.3 Phase 2.** Retire "Diplomacy between players" as an independent Standard Action Ob Reference row; it is Treaty's Concession-declaration step wearing a second name.
**Intent gate:** UNDETERMINED (could be intentional generality — informal diplomacy usable even absent an active Treaty negotiation — but nothing in either doc describes a distinct use-case for it outside Treaty-adjacent context).
**Direction:** backwards (traced from the duplicate-listing symptom). **Severity:** P3. **Calibration:** NEW.
**Retires downstream:** removes one row from the Standard Action Ob Reference table (`params/bg/core.md`) and its associated balance/port burden; the actual mechanic remains fully covered by Treaty §3.3.

---

## Action 9 — Treaty (3-phase: Positioning / Concession / Ratification) + Formal Crown Treaty

**Design intent:** the core diplomatic-alliance mechanic — multi-phase negotiation with a resolver-backed Positioning roll, free-form Concession, and a resolver-backed Ratification vote; Crown gets an exclusive victory-adjacent variant (PP-512–514/523).
**As-if-built contribution:** this is the strongest-designed action family in the lane. Cross-scale reach is explicit and bidirectional: Domain Echo carries Treaty outcomes into personal-scale scenes (Hybrid mode, `scale_transitions_v30.md §3.4`), and a stalled negotiation can Zoom In to a Grand Debate whose personal-scale outcome feeds back as a Ratification modifier — a genuine two-way Ω-a bridge, rare in this lane.
**Criterion:** N pass strongly (treaty-making as power-structure-decisive diplomacy, explicitly the design's own rationale for the ED-865/874 resolver migration — "early-modern treaty-making is power-structure-decisive; chance is a tail"). Ω-d pass: breach costs Mandate −2/Stability −1 to the breaching party and grants all co-signatories Casus Belli; consent gates (Mandate≥3 ∧ Stability≤3 for NPC consent) prevent free hegemony-by-treaty. Q-elegant: the 3-phase structure (position → concede → ratify) restates in one sentence and composes cleanly with the vote mechanics already used by Parliament.
**Verdict: KEEP.** Formal Crown Treaty is a legitimate distinct sub-case (different actor-eligibility and victory-adjacency per GD-1/§3.1 of victory_v30), not a duplicate of the general Treaty track.
**Direction:** top-down. **Severity:** P3. **Calibration:** NEW.

---

## Action 10 — Parliamentary Motion, punitive cluster (Censure / Embargo / Blockade / Combined Embargo+Blockade / Outlawry)

**Design intent:** collective institutional coercion against a target faction, vote-gated, scaling from a one-time reputational ping (Censure) to permanent outlawing (Outlawry).
**As-if-built contribution:** models a real and load-bearing Renaissance/early-modern dynamic — parliamentary censure, trade embargo, attainder/outlawry are all historically attested tools of factional coercion short of war.
**Criterion:** N pass on the *dynamic*. But Abstractable on the *implementation as five separately-named cards*: every entry in `faction_layer_v30.md §5.4` shares the identical underlying decision structure — propose (min stat threshold) → vote (majority or supermajority) → apply a Stability/Wealth/Mandate penalty → renew-or-lapse. The five rows differ **only in magnitude, duration, and vote threshold**, never in the *kind* of decision the proposing player makes. Combined Embargo+Blockade is explicit textual evidence for this: it is defined as literally "both together," i.e. the design itself treats these as composable severity dials, not five independent mechanics. Judged as-if-built with all five fully realized, a player choosing among them is choosing a magnitude slider, not five qualitatively different moves — this is the Abstractable/Edge-case N failure mode applied to redundant *authoring surface*, not to the underlying dynamic (which is real and should survive in a leaner form).
**Verdict: DISTILL.** Collapse to one parameterized "Parliamentary Sanction" action with a chosen severity tier (Mild=Censure-equivalent … Total=Outlawry-equivalent), cost/threshold/duration scaling with tier. No player decision is lost (the choice of *how hard* to hit a target is preserved as a tier selection); the authoring, balancing, and eventual porting burden of five discrete named rules is removed.
**Direction:** lateral (cross-comparison within the cluster). **Severity:** P2. **Calibration:** NEW.
**Retires downstream:** collapses 5 rows of `faction_layer_v30.md §5.4` (plus their share of the Rebuttal ladder's per-target-type branching, §5.5) into 1 parameterized action — shrinks the Parliamentary-actions authoring/balance/port surface by ~4 entries.

---

## Action 11 — Parliamentary Motion, constructive/enabling cluster (Subsidy / War Authorisation / Treaty Ratification / Recognition Challenge / Succession Endorsement)

**Design intent:** collective-vote levers that *enable* or *legitimize* rather than punish — funding an ally, sanctioning a war, binding a treaty, contesting a rival's territorial legitimacy, endorsing a dynastic heir.
**As-if-built contribution:** unlike Action 10's cluster, each of these models a distinct Renaissance-era political lever with a genuinely different object (patronage; casus belli sanction; treaty legitimation; disputed sovereignty/recognition; dynastic succession legitimation) — not a magnitude variant of a shared template.
**Criterion:** N pass across the cluster. One weak point: **Recognition Challenge** (−1 TCV from victory calculation, *no territory change*) is a comparatively thin, purely-numerical effect with no other stated world-state hook (no Accord shift, no diplomatic-isolation consequence) — bordering on Abstractable, since "lower a rival's victory-count without touching anything else in the world" is a thinner decision than its four siblings.
**Verdict: KEEP** for the cluster; **REFINE** (P3 sub-flag) on Recognition Challenge specifically — give it a stated secondary world-state consequence (e.g., tie to Accord or diplomatic-isolation effects) so it isn't purely a number-shift.
**Direction:** lateral. **Severity:** P3. **Calibration:** NEW.

---

## Action 12 — Rebuttal

**Design intent:** the targeted faction's counter to a Censure/Outlawry vote — a resolver roll that can negate or halve the penalty, with an Overwhelming result actively punishing the proposer.
**As-if-built contribution:** this is the design's own non-dominance safeguard for Action 10's punitive cluster — without it, Censure/Outlawry would be a free, uncounterable strike. Its existence is direct evidence the design *does* respect Ω-d for that cluster; the DISTILL verdict on Action 10 is about authoring redundancy, not about this check-and-balance being unnecessary.
**Criterion:** N pass (targets defending against political attack, universal factional-politics dynamic). Ω-d pass explicitly (symmetric costs, proposer can be punished on Overwhelming).
**Verdict: KEEP.**
**Direction:** diagonal (feeds back into Action 10's verdict). **Severity:** P3. **Calibration:** NEW.

---

## Action 13 — Resistance Check

**Design intent:** once per Accounting, an occupied faction may attempt a free (no action-slot) pushback roll against its occupier.
**As-if-built contribution:** models occupied-population/partisan resistance — a real and historically loaded dynamic (occupied territories resisting foreign rule).
**Criterion:** N pass. Ω-d/Q-smooth: being a *free* action (doesn't compete for the occupied faction's own action economy) is a deliberate and correct design choice — an occupied faction is already disadvantaged; charging it a scarce slot to resist would double-punish the victim rather than model resistance as a distinct pressure on the occupier.
**Verdict: KEEP.**
**Direction:** top-down. **Severity:** P3. **Calibration:** NEW.

---

## Action 14 — Reconstitute (collapsed faction re-emergence)

**Design intent:** any faction reduced to collapse may attempt to re-emerge over 3 consecutive seasons via an Influence Domain Action; on success the faction returns diminished, and **the player becomes its new leader**.
**As-if-built contribution:** the strongest single hit on Ω-b (personal-scale transformation) in the entire FA lane — this is a strategic-scale mechanic whose payoff is explicitly a personal-scale identity change (you become the leader of the re-emerged faction), alongside the more usual Ω-a cross-scale reach (territory-holding prerequisite, frozen-attribute halving).
**Criterion:** N pass strongly (restored dynasties/houses returning from collapse — Reconquista-adjacent, restored-monarchy dynamics are deeply Renaissance-era load-bearing). Ω-a and Ω-b both pass explicitly. Ω-d pass: 3-consecutive-season commitment with a territory-holding prerequisite is a real, sustained cost, not a free respawn.
**Verdict: KEEP.**
**Direction:** diagonal. **Severity:** P3. **Calibration:** NEW.

---

## Action 15 — Claim Masterless units

**Design intent:** during a Political Vacuum aftermath, any faction may attempt to claim ownerless garrison units via a Military Ob 2 Domain Action; Failure disbands them.
**As-if-built contribution:** models condottieri/mercenary-garrison defection during a power vacuum — a real, specific early-modern dynamic (mercenary companies switching allegiance when their paymaster falls).
**Criterion:** N pass on the dynamic. Abstractable on the authoring level: the decision this action asks of the player — "spend a Military-gated action to seize a territory" — is not distinguishable from ordinary Conquest/March except in target-eligibility (Masterless vs. enemy-held) and a different Ob/failure branch (disband vs. Stability/officer cost). As-if-built, a player weighing "attack this Masterless territory" vs. "attack this enemy territory" is making the *same* strategic call (spend Military, take a territory, accept a specific failure risk); the mechanic doesn't add a decision beyond Conquest's own target-selection.
**Verdict: DISTILL.** Fold into Action 4 (Conquest/March) as a target-type variant (Masterless targets use Ob 2 / disband-on-failure instead of the standard battle-engine path) rather than a separately-named §1.5 rule.
**Direction:** lateral (compared directly against Action 4). **Severity:** P3. **Calibration:** NEW.
**Retires downstream:** removes one dedicated rule from the collapse-aftermath authoring surface (`faction_layer_v30.md §1.5`); the decision content survives inside Conquest's target-selection.

---

## Action 16 — Faction-unique special actions (cluster: Crown Royal Decree/Charter/Thread Liaison/Diplomatic Outreach; Church Piety Spread/Active Inquisition/Cardinal Focus/Ecclesiastical Appointment/Excommunication/Council of Solmund/Absolution/Church Seizure/Assert-Suppress; Hafenmark Parliamentary Manoeuvre/Challenge/Session/Dynastic Proclamation/Diplomat Card/Counter-Intelligence Postures; Varfell Cultural Reclamation/Revelation Tokens/Counter-Narrative; Löwenritter Martial Governance; Restoration Community Organising/Weaving)

**Design intent:** per-faction asymmetric identity — each of the six factions gets a distinct toolkit expressing its own historical archetype (Church wields excommunication/inquisition, Crown wields decree/charter, Hafenmark wields commercial-parliamentary leverage, Varfell wields military-cultural conquest, Löwenritter wields martial law, Restoration wields grassroots organizing).
**As-if-built contribution:** this is the strongest N-grounded material in the lane — asymmetric faction identity built from genuinely distinct, historically-attested Renaissance/early-modern political forms (papal excommunication was real; royal charters were real; guild/commercial parliamentary maneuvering was real; communal/contado organizing was real). This is exactly what the setting's own P-01..P-14 foundations call for: factions that are mechanically different, not reskins of each other.
**Criterion:** N pass strongly across the cluster (as design, not as sim). Ω-d spot-check on the highest-leverage member: Excommunication is gated on the Church's own Legitimacy (`EXCOMM_PREREQ_L_LIGHT`) — the Church spends its *own* political capital to strike a rival, a real designed tradeoff, not hidden-cost dominance.
**Build-state note (routing only, not a verdict input):** prior finding C-FA-4 documents that the *sim's AI selector* (`faction_action.py`) currently wires unique-action dispatch for Crown and Church only — Hafenmark and Varfell's turns silently fall through to Conquest. This reads, at first glance, like a design asymmetry problem. It is not: the prose catalog (`params/bg/faction_actions.md`) defines full unique-action rosters for Hafenmark (Parliamentary Manoeuvre/Challenge/Session, Dynastic Proclamation, Diplomat Card, Counter-Intelligence Postures) and Varfell (Cultural Reclamation, Revelation Tokens, Counter-Narrative) that are simply unimplemented in the AI selector. This is precisely the trap the charter's cardinal rule warns against — an unwired NPC-selector gap is being misread as a design gap. It is correctly C-FA-4's territory (additive plan), not this audit's.
**Notable precedent within the cluster:** Cultural *Reformation* (Varfell) was already struck by Jordan (2026-04-19, CR-STRIKE) for a design reason — "incompatible with Vaynard's identity" / fantasy-imposition-adjacent framing — and replaced with Cultural *Reclamation* (Influence-based, non-military, explicitly not a control-transfer or victory path). That is this exact audit method already exercised informally by design authority; it validates the pessimist-subtractive approach as consistent with how Jordan already prunes this lane.
**Verdict: KEEP** the design principle and the vast majority of named cards as N-grounded and Ω-d-plausible. **Honest gap:** the ~20 individual PP-numbered cards were not each independently re-vetted line-by-line in this pass (only headers + a handful of full reads); a full per-card N/Ω/Q sweep of this cluster is recommended as targeted follow-up, not fabricated here.
**Direction:** bottom-up (from the wiring-asymmetry symptom back to the prose catalog). **Severity:** P2 (flagging the misread risk, not a design defect). **Calibration:** KNOWN-TRACKED (C-FA-4 for the wiring half; the Cultural Reformation strike is a KNOWN precedent).

---

## Action 17 — "Thread Operation" listed as an FA-scale Standard Action (Pontifex/Weaver)

**Design intent (as filed):** a Standard-Action-table row letting a faction's Pontifex/Weaver card spend a Domain Action slot on a Thread operation.
**As-if-built contribution:** none distinct from the Threadwork lane's own `attempt_*` operations (Leap/Weaving/Pulling/Locking/Dissolution/Mending, `sim/thread/operations.py`, `threadwork_v30.md §2`) — this row in `params/bg/core.md` is the *same mechanic*, filed a second time under the FA Standard Action table because Thread operations happen to be biddable via a Domain-Action card slot.
**Criterion:** N — Duplicate/scale-break. Failure Lexicon: "Scale break" fails Μ-δ/М-5 — a mechanic re-catalogued under a second scale's action menu without being a genuinely different operation invites exactly this failure mode, not because the underlying Thread mechanic is bad (that is TW lane's call, not FA's) but because FA re-listing it as its own action risks double-authoring/double-balancing/double-porting the same rule.
**Verdict: PRUNE** (from the FA menu specifically — a filing correction, not a judgment on Thread operations' merit, which belongs to the TW lane dossier).
**Intent gate:** DELIBERATE (the game legitimately lets a Pontifex/Weaver card spend its slot on a Thread op; that's a real cross-scale eligibility rule) but the FA-lane **cataloging** of it as a first-class FA action is what should be pruned — cross-reference TW lane instead of re-listing.
**Direction:** diagonal (cross-lane). **Severity:** P3. **Calibration:** NEW.
**Retires downstream:** none within FA's own scope-reduction ledger (no FA mechanic is removed); avoids double-adjudication of one mechanic across two lane dossiers — flag for the cross-lane synthesis stage to single-source to TW.

---

## Honest gaps in this pass

- The ~20 individual per-faction unique-action PP-cards in `params/bg/faction_actions.md` were read by section header, not each fully re-vetted line-by-line (Action 16's honest gap, repeated here for visibility).
- `faction_politics_v30.md` Parts 3–9 (rank-ladder/caste/succession detail beyond Part 1) were not read in this pass; if any of those parts define additional player-facing verbs (e.g. explicit succession-contest actions), they are not captured in this menu and should be checked before this dossier is treated as exhaustive.
- No sim was run (read-only per charter); all Ω-d/N judgments on Muster/Conquest are argued from the *design* text, cross-checked against but not validated by executing `mc_v18`.
- This dossier does not attempt to adjudicate the `da.*` bucket assignment itself (which concrete verb goes in which of the 5 buckets) — Action 0's REFINE verdict says that mapping needs to be authored, not what it should say.

---

## Lane summary

Judged as-if-built, the FA lane's core general-purpose verbs (Govern, Trade, Muster, March/Conquest, Fortify, Survey, Treaty, Reconstitute, Resistance Check, Rebuttal, and the constructive Parliamentary cluster) are genuinely N-grounded, cross-scale, and non-dominant by design — this is a well-built lane at the center, including a standout (Reconstitute) that hits both Ω-a and Ω-b at once, and the faction-unique cluster is the strongest N-grounded material in the whole audit, with the apparent Crown/Church-only asymmetry correctly diagnosed as a sim-wiring misread rather than a design flaw. The lane's real subtractive yield is authoring-surface redundancy, not dynamic-level failure: the punitive Parliamentary cluster's five named cards collapse to one severity-dialed action, Claim Masterless collapses into Conquest, Diplomacy-between-players collapses into Treaty's own Concession phase, the mis-filed Thread Operation row should be single-sourced to the TW lane, and the da.* Key taxonomy needs to be merged onto the existing prose tables rather than stand as a second, unmapped catalog — together these retire roughly seven authoring/balance/port line-items without cutting a single real player decision, which is the correct pessimist outcome for a lane whose central dynamics already earn their place.

