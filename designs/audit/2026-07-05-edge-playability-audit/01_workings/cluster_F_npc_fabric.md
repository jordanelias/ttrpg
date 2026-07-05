# Cluster F dossier — NPC / personal fabric (verbatim agent output)

_Sonnet evidence agent, 2026-07-05. Headline claims Fable-verified against the working tree —
see `verification_log.md` (private_observers hard-coding confirmed at 6 sites incl. the
visibility_default lines; npc_behavior §6.1/§6.1b confirmed literally empty; "No appeal roll —
the act is unambiguous" confirmed verbatim, ED-666). Verbatim below._

---

# Playability Audit — NPC / Personal Fabric Cluster

Currency: per `CURRENT.md`, NPC behaviour head = `designs/npcs/npc_behavior_v30.md`; Social contest head = `designs/scene/social_contest_v30.md` (contest_rebuild in flight, not yet superseding); doc-12 migration = `designs/provincial/political_dynamics_keys_migration_v30.md`. Piety Track promoted out of npc_behavior into `designs/personal/conviction_track_v1.md` (PP-681). All read at working-tree state.

### E1 · Social contest ↔ npc_behavior (2-cycle)
1. **Moment:** player wins/loses a persuasion contest against a named NPC in-scene (`social_contest_v30.md` §2 Step4 Persuasion Track ≥7/≤3).
2. **Decision:** Style/Genre/RS-targeting locked at setup (§6.2/§6.4.1).
3. **Feedback:** the scene's own stakes resolve immediately (§2 Step6), but the NPC's durable behavioral echo runs through Procedure D, which emits `state.opinion_revised` only at a threshold (`|Δaffect|≥0.5`) and only "1/Accounting" (`references/module_contracts.yaml:442` damper note; `political_dynamics_keys_migration_v30.md` §5.2).
4. **Latency:** up to one season between a decisive in-scene win and any visible shift in the NPC's ongoing behavior/priority tree.
5. **Friction:** none added by the player; the delay is systemic.
6. **Reciprocity:** the NPC's opinion-of-player updates on the same batch cadence — no immediate readback either direction.
7. **Verdict:** PLAYS-ROUGH · P1 · UNDETERMINED (dampers "unconfirmed [OPEN—Jordan]," `module_contracts.yaml:153`). A single dramatic persuasion beat gets its stakes resolved now but its relational truth ("does this NPC actually treat me differently") deferred a season — right for slow court intrigue, wrong as the *only* channel for an in-scene win.

### E2 · NPC ambient fabric → player (Procedure E)
1. **Moment:** off-screen inner-circle interactions/gossip, computed each Accounting.
2. **Decision:** none — player is not a participant.
3. **Feedback:** `scene.interaction` and `scene.gossip` Keys are emitted with an explicit visibility override, `private_observers: [npc_a.id, npc_b.id]` (`political_dynamics_keys_migration_v30.md` §6.1 line 358, §6.3). Per the substrate's observer resolution (`key_substrate_v30.md:231-253`) and the player-facing "Why?" diagnostic ("chain filtered to player's observable subset... whose visibility includes the player," line 381), this structurally excludes the player unless the player literally *is* one of the two NPCs.
4. **Latency:** N/A — never surfaces, not merely delayed.
5. **Friction:** n/a (invisible).
6. **Reciprocity:** none.
7. **Verdict:** MISSING · P1 · NOT-INTENDED. Nothing marks player-invisibility as deliberate; `§6.3`'s own comment that gossip's "observer set expands per propagation" implies an intended path to reach the player that is never specified.

### E3 · npc_memory → player legibility
1. **Moment:** the promised "the world remembers me" beat — via Read/Converse (`fieldwork_v30.md` §5.2) or Contest Appraise ("Overwhelming: one Belief revealed," `npc_behavior_v30.md` §3.1).
2. **Decision:** revelation, not choice; informs future RS targeting.
3. **Feedback:** the concrete hook, `npc_behavior_v30.md` §6.1 "Appraise Revelation" (lines 679-681) and §6.1b (683-685), are **empty section headers**. `npc_memory` itself carries `doc: null` in `module_contracts.yaml:179`, gap-noted "home doc unlocated... standalone spec [GAP]" (line 192). The one specified videogame surface is a *momentary* Scar-flicker on the NPC portrait that "does not persist... the player must remember" (`social_contest_v30.md:350`) — memory held by the player, not cited back by the NPC.
4. **Latency:** n/a — mechanism doesn't exist to surface.
5. **Friction:** high — no persistent in-fiction marker, no specified dialogue path for an NPC citing a past event.
6. **Reciprocity:** none specified.
7. **Verdict:** INERT bordering MISSING · P1 · NOT-INTENDED. `npc_memory` consumes Keys silently (`module_contracts.yaml:182-186`) with its sole player-facing hook left as an unwritten stub.

### E4 · piety_track — scar acquisition on player strategic verbs
1. **Moment:** player performs `da.antinomian_action`/`da.covert_betrayal` or a witnessed Thread op (`conviction_track_v1.md` §3 matrix).
2. **Decision:** the act is chosen for tactical/faction reasons; Scarring is a side effect, not a declared stake.
3. **Feedback:** §3's Thread-Event×Conviction matrix and Certainty scaling are engine-side tables, not a player-facing pre-warning; the player's own Conviction check (ED-664, §3) is *post-hoc* ("failure: Scar 1 effect for one season"). Scars=2 (RS exposed) and Scars≥3 (crisis, d6 table) are numeric thresholds (§2) with no authored crisis-scene shape here — Companion departure (§6.1 of `companion_specification_v30.md`) is the only dramatized crisis surface in the cluster.
4. **Latency:** Scar accrual is scene-immediate (1/season cap); the crisis roll fires "per major X-engaging decision" thereafter — open-ended.
5. **Friction:** none for NPCs (engine-run); reasonable Spirit roll for the player.
6. **Reciprocity:** none — Scars are indelible (`module_contracts.yaml:216`).
7. **Verdict:** PLAYS-ROUGH · P1 · NOT-INTENDED. No in-fiction preview that a specific antinomian act is about to Scar a Knotted/companion NPC's Conviction — compounds directly into E7's un-telegraphed companion departure.

### E5 · state.scar_acquired → faction_state + npc_behavior (crisis reaches player)
1. **Moment:** NPC hits 3+ Scars on a Conviction → `state.scar_acquired` emits, consumed by both `faction_state` (`module_contracts.yaml:79`) and `npc_behavior` (line 131).
2. **Decision:** if the NPC is Knotted to the player, `scale_transitions_v30.md` §4.3.2 "Knot Partner in Crisis" fires a **mandatory** Zoom-In; player may seek the NPC or perceive at distance.
3. **Feedback:** well-specified for the Knot-gated path; for a merely-liked NPC (Disposition ≥+1, no Knot) the same crisis is only a *declinable* Priority-1 scene (§4.3.3); below Disposition +1 there is no listed trigger at all.
4. **Latency:** tight for the mandatory path (Priority 0).
5. **Friction:** requires having specifically formed a Knot (Bonds≥5 gate, `knots_v30.md` §3.1).
6. **Reciprocity:** the same Key cascades to faction Mandate/Stability regardless of whether the player ever sees the personal beat — a faction-shaking consequence can land silently.
7. **Verdict:** PLAYS-WELL (Knot path) / MISSING (non-Knot majority) · P2/P1 · DELIBERATE (Knot trigger) / UNDETERMINED (non-Knot gap).

### E6 · Knots (form → strain → decay/break)
1. **Moment:** Disposition reaches +5 → Formation roll (`knots_v30.md` §3.2).
2. **Decision:** invest toward +5, then opt into the roll; later, spend strain on 5 use-sites (§4).
3. **Feedback:** formation/rupture are cut-scene triggers (`articulation` §10.2, "Trigger #6/#7") and Tier-1 UI shows Knot status (§10.1) — genuinely good. But the strain gauge itself (the −5..+5 axis governing Break) has **no cited UI meter** in §10 — only Coherence-band "sense of wrongness" (§8.1), which is diegetic, not numeric.
4. **Latency:** strain accrues per-use but decay/Break resolve only at Accounting (`module_contracts.yaml:322-325`).
5. **Friction:** Bonds≥5 is a chargen-time gate (§3.4) closing off Wager, Composure-buffer, remote Thread-Read, counsel-extraction, corroboration-bonus, and the E5/§4.4 distance-perception payoff for the campaign's duration to any Bonds 1-4 build — with no flag of this cost at character creation in this doc.
6. **Reciprocity:** the richest-specified sub-mechanic (§4-§7 use/strain/break/opposing-ops tables).
7. **Verdict:** PLAYS-WELL (formation/rupture) / PLAYS-ROUGH (strain legibility + Bonds gate) · P1 · DELIBERATE (Bonds gate, ED-780) / UNDETERMINED (whether permanent exclusion for low-Bonds builds was intended).

### E7 · Companion arcs
1. **Moment:** Disposition ≥+3 → Companionship Scene, explicit "moment of truth" (`companion_specification_v30.md` §2.2).
2. **Decision:** accept/decline; direct in combat or let AI run (§4.1); several departure triggers (§6.1) are player-uncontrollable in the moment.
3. **Feedback:** the cluster's richest surface — persistent stats, scene bonuses (§7.2), Sufficient Scope +1 modifier (`scale_transitions_v30.md` §7), mandatory Arc-Trigger scenes with the player present (§4.3.2).
4. **Latency:** immediate/mandatory (Priority 0) — best in the cluster.
5. **Friction:** max 2 active Companions (§1.3); Thread-violation departure fires "no appeal roll — the act is unambiguous" (§6.1) — same blind spot as E4.
6. **Reciprocity:** Companion Conviction shapes their combat AI (§4.1), retrospective narration (§4.4 of `scale_transitions_v30.md`), and departure risk.
7. **Verdict:** PLAYS-WELL overall / DEGENERATE-RISK at the Thread-violation seam · P2 overall, P1 at that seam · DELIBERATE (hard consequence intended) / UNDETERMINED (no pre-act warning surface found anywhere in threadwork/combat UI for a companion-conviction conflict).

### E8 · Disposition track
1. **Moment:** continuous, touched by nearly every social/fieldwork/contest action.
2. **Decision:** player chooses social actions/gifts to shift it.
3. **Feedback:** `fieldwork_v30.md` §10.4 gives Disposition an explicit UI meter (segmented bar, −5..+5, on NPC portrait) — the strongest legibility artifact found in the cluster.
4. **Latency:** scene-immediate shifts (§5.2 table); but its highest-stakes payoffs — Knot strain decay at ≥+3 (`knots_v30.md` §5), Sufficient Scope Domain Echo at +4/+5 (`scale_transitions_v30.md` §7 item 6) — resolve at Accounting.
5. **Friction:** low.
6. **Reciprocity:** explicitly asymmetric per-NPC (`knots_v30.md` §1).
7. **Verdict:** PLAYS-WELL as one currency, one meter · P2 · DELIBERATE (ED-912 consolidated it from a fragmented Bonds-capped model precisely to fix this) — residual fragmentation is not in the number but in the *different secondary gates* (Bonds, companion slots, faction office) each payoff hides behind, invisible from the meter itself.

### E9 · state.belief_revised dual attribution
1–2. **Moment/Decision:** an NPC revises a Belief via decisive Contest (`npc_behavior_v30.md` §3.2) or Knot-mediated Solidarity RS (`fieldwork_knots`).
3. **Feedback:** `module_contracts.yaml:129/306` shows the SAME type emitted by both `npc_behavior` and `fieldwork_knots`, flagged "[OPEN—Jordan]." Player-facing exposure (via Appraise) likely survives a double-emission, but the "Why?" backward-walk diagnostic (`key_substrate_v30.md:381`) risks an incoherent or duplicated causal chain when a player asks "why does this NPC now believe X."
4-6. n/a to the conflict itself.
7. **Verdict:** PLAYS-ROUGH at the diagnostic surface only · P3 · UNDETERMINED (explicitly open).

---

## Candidate findings

1. **[NEW] Ambient fabric is structurally player-invisible by explicit visibility override, not by omission.** `political_dynamics_keys_migration_v30.md` §6.1/§6.3 hard-codes `private_observers: [npc_a, npc_b]` on `scene.interaction`/`scene.gossip`. Player-chair failure: a player stands in a tavern, two courtiers visibly gossip about them per the fiction, but the engine's own Key never enters the player's observable set — there is no representable "overheard gossip" or "changed greeting" event, even though `npc_behavior_v30.md` §8.11 explicitly frames Outreach as "the world's actors do not wait to be approached." Severity P1, NOT-INTENDED.

2. **[NEW] Belief/Scar revelation's player-facing hook is an unwritten stub, not a gap in a peripheral doc.** `npc_behavior_v30.md` §6.1/§6.1b "Appraise Revelation" are empty headers; `npc_memory` has `doc: null`. Player-chair failure: a player who wins a Contest at Overwhelming and is told "one Belief revealed" gets nothing, because the section that would specify *which* Belief, in what form, is blank. Severity P1, NOT-INTENDED.

3. **[Reframed from calibration note] The npc↔contest 2-cycle damper isn't just "unconfirmed" — it conflates two different payoffs.** The scene's own stakes resolve immediately; only the NPC's *durable* behavioral shift is batched. This distinction isn't drawn anywhere in canon, so a design/build risk exists that the engine either (a) never gives immediate stakes resolution outside the Persuasion Track number, leaving every persuasion feel inert until season-end, or (b) conflates the two and makes even trivial in-scene concessions wait for Accounting. Severity P1, UNDETERMINED.

4. **[NEW] Strategic-verb Scar acquisition and companion Thread-violation departure share one un-telegraphed trigger, compounding across two systems.** A player performing Dissolution/Lock/covert-betrayal gets no pre-act warning (conviction_track_v1.md §3 is engine-facing) before it both Scars a Knotted NPC's Conviction (E4) and, if a companion with Faith/Order/Equity is present, ends that companion relationship with "no appeal roll" (`companion_specification_v30.md` §6.1). Player-chair failure: the first indication a companion's Conviction forbids an act is the departure scene itself. Severity P1, NOT-INTENDED (departure-without-appeal is deliberate; the absence of any preview is not flagged as a deliberate design cost anywhere found).

5. **[NEW] Knot payoffs (crisis-at-distance, "Where Were You?" companion framing, strain legibility) are gated behind a chargen-time attribute (Bonds≥5) with no UI warning of the gate's scope.** `knots_v30.md` §3.4 lists six major systems closed to a Bonds 1-4 character for the whole campaign, and the strain gauge itself has no exposed meter (§10). Severity P2, DELIBERATE gate / UNDETERMINED scope-awareness cost.

## Threadwork note (P-14 at these seams)

P-14 requires that Board/VG modes never omit the three-dimensional co-movement of a Thread operation — the analogous discipline at this cluster's seams is the **Knot-substrate inseparability rule** (`npc_behavior_v30.md` §5.0b, citing A12/canon P-12): a transforming NPC's Thread-shift exerts strain on everyone Knotted to them, scaled by TS band. This is honored where it's wired — knot strain propagation table (§5.0b), opposing-Thread-ops strain (`knots_v30.md` §7), Coherence-band strain (§8.1) — but the propagation stops exactly where E2/E3/E6 stop: a Knot-partner's crisis reaches the player only through the Knot itself (E5's mandatory trigger), never through the wider ambient fabric (E2's private-observer scoping) or a legible memory surface (E3's empty stub). The P-14 analog here is not violated in its narrow Thread-op sense, but the *design intent behind P-14* — that consequence must be inseparable and visible, never a silent side-channel — is exactly what E2 and E3 break: consequence propagates through the Key substrate (mechanically inseparable) but is authored to be invisible to the one observer (the player) the whole cluster exists to serve.
