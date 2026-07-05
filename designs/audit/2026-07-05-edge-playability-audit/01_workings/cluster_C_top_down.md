# Cluster C dossier — top-down transport (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md`. Fable corrections: (a) the "debt scene per §1" citation is dangling at
the FILE level — `faction_politics_expanded_v1.md` does not exist anywhere in the tree (the agent
checked only `faction_politics_v30.md` §1); (b) articulation trigger #3 fires `state.succession`
only for `succession_mode in [contested, emergency, imposed]` — routine succession does NOT fire
Tier 2, narrowing this dossier's E3/E14 "unconditionally" wording. Verbatim below._

---

### E1 · Strategic Settlement Revolt → Personal Scene
1. MOMENT: Player is in/near an Order-0 settlement; revolt scene forced (`scale_transitions_v30.md` §4.3.2 row 1).
2. DECISION: Real menu — support garrison / negotiate / investigate / flee.
3. FEEDBACK: Traceable — player is told it's *this* settlement, cause is Order=0, which is legible from §2.8 environmental-legibility cues (`peninsular_strain_v30.md` §2.8, L198-213) building up to it.
4. LATENCY: Fires at Accounting-detected Order 0, presented next Personal Phase — appropriate.
5. FRICTION: Dedup rule (ED-750) collapses same-settlement/same-season settlement_layer events into this one entry, but nothing in the Slate presentation spec (`player_agency_v30.md` §4.2b, L293-295: name/location/one-sentence/tag/priority) tells the player a second event was folded in — the merge is invisible.
6. RECIPROCITY: Good — 4 distinct resolution paths, each using an existing subsystem.
7. VERDICT: PLAYS-WELL (dedup legibility aside) · P3 · DELIBERATE (ED-750 cites explicit rationale).

### E2 · Heresy Investigation Target → Personal Scene
1. MOMENT: Player is investigation subject; Inquisitor arrives.
2. DECISION: Resist / comply / redirect via asymmetric social contest (`scale_transitions_v30.md` §4.3.2 row 2, L132).
3. FEEDBACK: Direct — the confrontation is the scene itself.
4. LATENCY: Immediate on becoming target; appropriate for interrogation pressure.
5. FRICTION: None specific beyond the generic social-contest §7 asymmetric-rules dependency (not audited here).
6. RECIPROCITY: Present — three real branches.
7. VERDICT: PLAYS-WELL · P3 · DELIBERATE.

### E3 · Faction Leader Removal → Personal Scene + Succession
1. MOMENT: Leader assassinated/overthrown/incapacitated; player witnesses or learns directly (`scale_transitions_v30.md` §4.3.2 row 3, L133).
2. DECISION: If Standing ≥5, real: accept/decline/contest leadership per `player_agency_v30.md` §5.2 (L376-386) — offered, contested (SUC-01–03), or seized via challenge. Below Standing 5, player is a spectator to canonical-NPC succession.
3. FEEDBACK: `state.succession`/`state.coup_attempted` are consumed by `faction_state` and `npc_behavior` (`module_contracts.yaml` L78,81,130,133) and trigger a Tier-2 cut scene (`articulation_layer_v30.md` §3.1 triggers #2/#3) — cause→effect is traceable. [Fable correction: #3 is conditional on succession_mode; see header.]
4. LATENCY: Immediate, matches dramatic weight of a leadership crisis.
5. FRICTION: Below Standing 5 the "may intervene" language (row 3) is unspecified — no procedure for *how* a low-Standing PC intervenes, unlike §5.2's Standing 5+ paths.
6. RECIPROCITY: Strong at Standing ≥4 (offer/contest/seize); weak/undefined below Standing 5.
7. VERDICT: PLAYS-WELL at high Standing, PLAYS-ROUGH at low Standing · P2 · UNDETERMINED (no citation resolves the low-Standing "may intervene" mechanic).

### E4 · Mass Battle at Settlement → Personal Scene
1. MOMENT: Player caught in a battle at their location (`scale_transitions_v30.md` §4.3.2 row 4, L134).
2. DECISION: Fight (command or personal combat) or flee (Endurance Ob 2).
3. FEEDBACK: Failure state explicit (1 wound); clear causal chain.
4. LATENCY: Appropriate — battle timing is externally forced, matching genre expectation of being swept up in war.
5. FRICTION: None beyond generic mass-battle/personal-combat handoff (§3.7, out of this cluster's scope).
6. RECIPROCITY: Binary but legitimate (participate vs. risk-checked escape).
7. VERDICT: PLAYS-WELL · P3 · DELIBERATE.

### E5 · Companion Arc Trigger → Personal Scene
1. MOMENT: Companion's arc branch condition fires; transformation scene with player present (`scale_transitions_v30.md` §4.3.2 row 5, L135; `companion_specification_v30.md` §7.1, L185-189).
2. DECISION: Player "may influence" arc resolution — for departures specifically, this is concrete (appeal roll, counter-offer, Tend-the-Wounded Ob 3 — `companion_specification_v30.md` §6.1-6.2, L152-176). For non-departure arc branches, no analogous procedure is cited.
3. FEEDBACK: Departure branch is traceable (explicit success/fail states). Non-departure "transformation scene" content is unspecified.
4. LATENCY: Immediate, appropriate.
5. FRICTION: Two-tier spec quality — departure well-built, generic "arc branch" thin.
6. RECIPROCITY: Strong for departures, weak/UNDETERMINED elsewhere.
7. VERDICT: PLAYS-WELL (departure) / PLAYS-ROUGH (other branches) · P2 · DELIBERATE for departures (explicit table), UNDETERMINED for the rest.

### E6 · Knot Partner in Crisis → Personal Scene
1. MOMENT: Knotted NPC hits Scar ≥3; crisis transmits via the relational thread (`scale_transitions_v30.md` §4.3.2 row 6, L136).
2. DECISION: "Seek out the NPC or experience the crisis at distance" — no Ob, roll, or subsystem named for either branch.
3. FEEDBACK: Thematically justified by P-12 (Knot-substrate inseparability, also invoked in `npc_behavior_v30.md` §5.0b, L518-528 for a *different* mechanic — Transformation Knot Strain — which at least has a numeric table); this row has no comparable numeric hook.
4. LATENCY: Immediate — appropriate.
5. FRICTION: Thinnest-specced of the eight mandatory rows — no resolution procedure exists anywhere else in the corpus (grep of `fieldwork_socializing.md`/threadwork docs returns nothing for this trigger).
6. RECIPROCITY: Nominal only ("may seek out... or experience at distance" is not a real choice — both are the same non-mechanical narration).
7. VERDICT: PLAYS-ROUGH (borders INERT — a mandatory, unskippable scene with no resolution mechanic) · P2 · NOT-INTENDED (no ED citation grounds it; contrasts with the well-built companion-departure sibling row).

### E7 · Stability Crisis → Personal Scene
1. MOMENT: Faction Stability ≤2 or drops ≥2 at Accounting (`scale_transitions_v30.md` §4.3.2 row 7, L137).
2. DECISION: Real — intervene (Govern Ob 2 → +1 Stability queued) or assess (Fieldwork Evidence +2).
3. FEEDBACK: Direct, with explicit Domain Echo routing (§5).
4. LATENCY: Appropriate, Accounting-boundary triggered.
5. FRICTION: Hysteresis (ED-749: re-arms only after Stab≥3 held 2 Accountings) is not surfaced in Slate presentation (`player_agency_v30.md` §4.2b) — player has no way to know why a *second* Stability dip in the same season/next didn't re-fire the mandatory scene; reads as a missed crisis, not a designed cooldown.
6. RECIPROCITY: Good (two real interventions).
7. VERDICT: PLAYS-WELL mechanically / PLAYS-ROUGH on legibility of the hysteresis · P3 · DELIBERATE (hysteresis is cited/intentional) but its **presentation** is NOT-INTENDED-covered (nothing authors a UI tell for it).

### E8 · Rank Advancement Recognition Event → Personal Scene
1. MOMENT: Standing crosses threshold; ceremony scene (`scale_transitions_v30.md` §4.3.2 row 8, L138). Per-rank detail (insignia, obligations, revocation conditions) is genuinely rich (`faction_politics_v30.md` L111-115, e.g. Banneret/Prince/Regent-Designate rows).
2. DECISION: Passive (receive rank) unless withheld.
3. FEEDBACK: Strong when granted (concrete tokens/obligations).
4. LATENCY: Appropriate.
5. FRICTION: The withheld branch — "creating a debt scene per §1" — cites a mechanic that does not exist: `faction_politics_v30.md` §1 contains no "debt scene" concept (grep confirms only unrelated "debt" hits, L539/1091/1111). The fallback path is a dangling citation. [Fable: worse — the cited FILE `faction_politics_expanded_v1.md` no longer exists; 57 citations corpus-wide still point at it.]
6. RECIPROCITY: Full for the happy path; MISSING for the withheld path.
7. VERDICT: PLAYS-WELL (granted) / MISSING (withheld) · P2 · NOT-INTENDED (phantom cross-reference, not a flagged exception).

### E9 · Scene-Budget Contention → Witness Mode (cross-cutting tail rule)
1. MOMENT: Mandatory-scene count exceeds scene-action budget (`scale_transitions_v30.md` §4.3.2 tail, L140; specified in `player_agency_v30.md` §4.2 Step 1, L207-218, ED-745/761).
2. DECISION: Player chooses which to attend personally; the rest resolve in Witness Mode with a **real** consolation mechanic: one free (but rollable, Ob 1) Read/Appraise, one narrative-input sentence, resolution via NPC AI.
3. FEEDBACK: Traceable — the player explicitly learns the surface event, with unreliable info on Appraise failure.
4. LATENCY: Same-season resolution (not deferred to retrospective).
5. FRICTION: Low — this is one of the better-specced fallback systems in the cluster (revised twice per stress-test ED-761).
6. RECIPROCITY: Deliberately reduced (that's the point — "present but overwhelmed"), but not zero.
7. VERDICT: PLAYS-WELL as a degraded-but-legible fallback · P3 · DELIBERATE.

### E10 · World-State (Optional) Triggers → Personal Scene (5 rows, §4.3.3)
1. MOMENT: Clock Band Transition / NPC Conviction Crisis / Treaty / Territory Control Change / Warden Emergency (`scale_transitions_v30.md` §4.3.3, L142-152).
2. DECISION: Player may decline entirely (Priority 1, optional).
3. FEEDBACK: Cause is named per row, but resolution mechanics are unspecified prose ("the player may contribute Thread operations, investigate the cause, or support logistics" — no Ob, no pool, no subsystem pointer), contrasting with the mandatory rows' concrete Ob values.
4. LATENCY: Appropriate (optional, so player controls timing by attendance choice).
5. FRICTION: Mechanical thinness across all 5 rows — none cite a resolvable procedure the way E1-E4 do.
6. RECIPROCITY: Nominal (options are named but not adjudicated).
7. VERDICT: PLAYS-ROUGH (reads as flavor menu, not gameplay) · P3 · UNDETERMINED.

### E11 · "Where Were You?" Retrospective (§4.4)
1. MOMENT: Free narrative scene the season after a major world event the player missed (`scale_transitions_v30.md` §4.4, L154-169).
2. DECISION: No decision over the event itself (explicitly cannot change outcome); the real choice is the *response*.
3. FEEDBACK: Context-keyed shape (companion/Knot/Disposition/none) is well-differentiated, including reliability tagging for the ambient-source case (Unverified per fieldwork §4.3).
4. LATENCY: One-season delay by design — appropriate for "hearing about it after the fact."
5. FRICTION: Low — response paths (new Conviction, new Scene Slate entry, new Duty) are concretely named and match Step 4's Conviction-scan re-validation (`player_agency_v30.md` §4.2 Step 4, L252-273).
6. RECIPROCITY: Real, but deferred by a full season and mediated (never direct action on the event).
7. VERDICT: PLAYS-WELL as a legibility/consolation device · P3 · DELIBERATE.

### E12 · Zoom-In Scene Opportunity (§4.1) — BG Degree → Scene Ob
1. MOMENT: BG Domain Action degree sets personal-scene Ob modifier (`scale_transitions_v30.md` §4.1, L105-108; mirrored at §3.9 for Survey→Fieldwork Offset, L91).
2. DECISION: Indirect — player doesn't choose the modifier, only reacts to a harder/easier scene.
3. FEEDBACK: The rule itself is legible in spec, but nothing in the Slate presentation (§4.2b) or scene framing surfaces *why* a given scene's Ob shifted — no "the campaign is going well, this will be easier" tell is specified for the player-facing UI.
4. LATENCY: Immediate application — fine.
5. FRICTION: Silent modifier — a player who fails a scene with no visible reason it was Ob+1 cannot trace it to last season's Board failure.
6. RECIPROCITY: One-directional (BG→personal only, per this row).
7. VERDICT: PLAYS-ROUGH (mechanically sound, feedback-poor) · P3 · UNDETERMINED (no citation for a Ob-source tell in UI).

### E13 · da.* Keys → Personal Experience (enemy espionage/heresy/economic action against player's faction)
1. MOMENT: Enemy runs `da.covert_betrayal`/`da.antinomian_action`/`da.economic_intervention` (`module_contracts.yaml` L59-63, 111-113, 615).
2. DECISION: None available to the player at personal scale.
3. FEEDBACK: Only path to the player is a Tier-2 cut scene, and only for `da.covert_betrayal` **when `exposed==true`** (`articulation_layer_v30.md` §3.1 trigger #5) — a 5-15s *non-interactive* vignette (§1, §3.2). Unexposed betrayals, and all `antinomian_action`/`economic_intervention` instances, produce no player-perceptible signal at all; `settlement_economy`, the nominal consumer of `da.economic_intervention`, is a documented phantom module with no doc/state/logic (`module_contracts.yaml` L609-623).
4. LATENCY: N/A — no personal-scale delivery exists to have a latency.
5. FRICTION: High — the player cannot detect, investigate, or retaliate against a rival faction's covert action even when it targets them directly.
6. RECIPROCITY: MISSING — one-way, passive, no counter-espionage or defensive scene path exists anywhere in scale_transitions §4.3.2/§4.3.3.
7. VERDICT: DEGENERATE-RISK / MISSING (an entire genre beat — faction espionage against you — has no interactive surface) · P1 · NOT-INTENDED (no ED/doctrine flags this as an intentional omission; §12.2/§12.3 authoring discipline exists precisely to close such gaps and hasn't been applied here).

### E14 · Succession/Coup → Player (state.succession / state.coup_attempted)
See E3 for the Zoom-In mechanics. Key-delivery side: both types are declared consumed by `faction_state` and `npc_behavior` (`module_contracts.yaml` L78/81/130/133) and fire an articulation Tier-2 cut scene (`articulation_layer_v30.md` §3.1 triggers #2/#3 — #3 conditional on non-routine succession_mode) giving succession/coup better top-down legibility than E13's da.* events. VERDICT: PLAYS-WELL at the delivery layer; the residual gap is E3's low-Standing "may intervene" thinness · P2 · DELIBERATE for delivery, UNDETERMINED for the low-Standing intervention procedure.

### E15 · env.disaster / env.crisis / env.peninsular_strain_shock → Player Experience
1. MOMENT: Environmental/crisis Keys from `peninsular_strain` (`module_contracts.yaml` L500-504).
2. DECISION: None directly — these are accounting-tier stat deltas (Turmoil, faction stats via §3.4.2 temperament drift, `faction_behavior_v30.md` L268-271).
3. FEEDBACK: Only `env.peninsular_strain_shock` at `severity in [severe, crisis]` reaches the player, as a non-interactive Tier-2 cut scene (`articulation_layer_v30.md` §3.1 trigger #8) or, less immediately, a line in the annual Tier-3 chronicle. **`env.disaster` and `env.crisis` are not in the 10-trigger list at all** — they reach articulation only indirectly if they happen to also produce a co-firing `peninsular_strain_shock`, otherwise they are a pure stat delta with zero surfaced experience.
4. LATENCY: Cut scene is immediate; chronicle is annual (a season+ delay) — for `env.disaster`/`env.crisis` specifically, there may be no scene at all, ever.
5. FRICTION: The mandatory-trigger table (§4.3.2) and optional table (§4.3.3 "Clock Band Transition") do not name `env.disaster`/`env.crisis` as Zoom-In conditions either — they fall through every net except the Tier-2/Tier-3 articulation layer, and only conditionally.
6. RECIPROCITY: MISSING — no personal-scale response mechanic (compare to Warden Emergency in §4.3.3, which at least offers "contribute Thread operations, investigate, support logistics").
7. VERDICT: DEGENERATE-RISK — "a disaster is (at best) a stat delta with an occasional cut scene, never an interactive moment" · P1 · NOT-INTENDED (contradicts the design intent implicit in §2.8's "should be experienceable, not just trackable," which was written for Accord/Order specifically but the same principle is absent for disaster/crisis).

## Known down-seams (§12.4) — what the player misses today

Per calibration, not re-reporting the mechanism gap itself — only the concrete scene-level absence at each:

- **`domain_actions → {npc_behavior, piety_track, settlement_economy}`:** an enemy (or even friendly) faction's Governance/Betrayal/Antinomian/Diplomacy/Economic Domain Action never names which NPC(s) or settlement it touches. Player-visible effect: no companion or Knotted NPC ever reacts, gains/loses a Conviction Scar, or comments on a faction's domain-level action — Standing/Renown-adjacent NPCs are silent about world-shaping political events even when those events are thematically about their faction.
- **`faction_politics → npc_behavior`:** a coup or contested succession (E14) fires the Tier-2 cut scene, but no specific NPC's Disposition, dialogue, or arc state visibly shifts *because of* that specific event — the cut scene is a spectacle with no personal-relationship consequence trail.
- **`peninsular_strain → {npc_behavior, settlement_economy, settlement_layer}`:** a peninsula-wide disaster/shock never manifests as "this specific settlement's Prosperity/Order/Defense changed" — even though `settlement_layer` is nominally a consumer (`module_contracts.yaml` L543-544), without populated `targets[]` no individual settlement updates, so a player standing in the disaster zone sees the same generic Accord-tier flavor text (§2.8) as anywhere else, not a place-specific consequence.
- **`scenario_authoring → settlement_layer`:** hand-authored scripted events (miraculous events, scenario-injected disasters) have no settlement-level landing point either — an author who writes "the harbor town burns" has no mechanism to make that settlement's stats reflect it.

## Candidate findings

1. **[NEW] Enemy da.* covert actions against the player's own faction are functionally invisible and unactionable** (E13). Defect: `da.covert_betrayal`/`antinomian_action`/`economic_intervention` reach the player only via a passive, conditional (exposed==true), non-interactive cut scene, or not at all. Player-chair scenario: the player's faction loses Legitimacy from a rival's covert betrayal three seasons running; the player has no way to notice, investigate, or intercept it — it simply shows up as a faction-sheet number drop. Citations: `references/module_contracts.yaml` L59-63,110-116,609-623; `designs/architecture/key_type_registry_v30.md` §da.covert_betrayal/antinomian_action; `designs/articulation/articulation_layer_v30.md` §3.1 trigger #5. Severity P1. Intent gate: NOT-INTENDED.
2. **[NEW] Disaster/crisis events are a stat delta, rarely a scene** (E15). `env.disaster`/`env.crisis` are absent from both the articulation Tier-2 trigger list and the scale_transitions §4.3.2/§4.3.3 trigger tables; only `env.peninsular_strain_shock` at severe/crisis reaches the player, and only as a non-interactive vignette. Player-chair scenario: a settlement the player has invested in is hit by `env.disaster`; Prosperity drops; the player learns only by checking a menu, never through play. Citations: `designs/articulation/articulation_layer_v30.md` §3.1 (10 triggers, no env.disaster/env.crisis entry); `designs/provincial/peninsular_strain_v30.md` §2.8, §4.3. Severity P1. Intent gate: NOT-INTENDED.
3. **[NEW] "Knot Partner in Crisis" is the thinnest of the 8 mandatory rows — mandatory but mechanically empty** (E6). No Ob, roll, or resolution procedure exists anywhere in the corpus for this trigger, unlike its sibling rows. Player-chair scenario: a mandatory, un-skippable scene fires, consuming a scene action, and resolves as pure narration with no player agency distinguishable from doing nothing. Citations: `designs/architecture/scale_transitions_v30.md` §4.3.2 row 6 (L136); absence confirmed by grep of `designs/scene/fieldwork_socializing.md` and `designs/threadwork/`. Severity P2. Intent gate: NOT-INTENDED.
4. **[NEW] Dangling "debt scene" citation on Recognition-Event withholding** (E8). `scale_transitions_v30.md` §4.3.2 row 8 (L138) references "a debt scene per §1" for withheld recognition, but no such mechanic exists (and the cited file `faction_politics_expanded_v1.md` no longer exists — Fable verification). Player-chair scenario: inner-circle conditions withhold the player's promotion ceremony; the game has nothing to resolve into. Severity P2. Intent gate: NOT-INTENDED (phantom cross-reference, not a flagged deferral).
5. **[REFRAMED, sharpens known §12.4] Hysteresis/dedup rules (ED-749 Stability re-arm, ED-750 settlement-event dedup) are mechanically sound but have zero UI legibility.** Slate-entry presentation spec (`player_agency_v30.md` §4.2b) has no field for "this was suppressed/merged, and why." Player-chair scenario: Stability crashes again next season but the mandatory crisis scene doesn't re-fire (correctly, per hysteresis) — the player reads this as a bug, not a design choice, because nothing tells them the re-arm condition. Severity P3. Intent gate: DELIBERATE (mechanic) / NOT-INTENDED (presentation).
6. **[NEW] Zoom-In Ob modifier (§4.1) is a silent difficulty tax with no player-facing tell.** Citations: `designs/architecture/scale_transitions_v30.md` §4.1 (L105-108), §3.9 (L91); no presentation hook in `player_agency_v30.md` §4.2b. Severity P3. Intent gate: UNDETERMINED.
7. **[REFRAMED] World-state optional triggers (§4.3.3, all 5 rows) are flavor menus, not gameplay** — no row names an Ob, pool, or resolvable procedure, unlike the mandatory-trigger table. Severity P3. Intent gate: UNDETERMINED.

## Threadwork note (P-14 at these seams)

P-14 (three-dimensional co-movement on every Thread operation, in every mode) is the constraint most directly tested by E6 and E15. The Knot-crisis row (E6) *invokes* P-12/relational-thread perception rhetorically but supplies no operation, roll, or Coherence/co-movement hook — it name-drops the doctrine without executing it, which is weaker than the sibling `npc_behavior_v30.md` §5.0b Transformation Knot Strain table (L518-528), which *does* operationalize Knot-substrate inseparability numerically. E15's disaster gap is adjacent but not identical: peninsula-scale Thread/Calamity shocks (MS band, `env.peninsular_strain_shock`) do reach the player via the Tier-2 trigger #8 and are explicitly the "sanctioned cross-scale pattern" per the sibling qualitative audit's refutation of a thread-silence claim (`designs/audit/2026-07-04-ners-qualitative-audit/01_workings/refutations/refute_thread-absent-from-faction-engine-math.md`) — so the P-14 substrate obligation is met for *Thread* events proper. What's missing is narrower: `env.disaster`/`env.crisis` are non-Thread environmental Keys that never reach articulation at all, so this is a top-down-transport/legibility gap (§4-8 of this report), not a P-14 co-movement violation — worth keeping the two failure modes distinct so a fix to one doesn't get credited against the other.
