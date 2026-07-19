# Pessimist Subtractive NERS Audit — Lane Dossier: MB (Mass Battle)

**Status:** WORKINGS (Sonnet reconcile pass) · read-only · feeds the inverted critic + Fable verdict/synthesis
**Charter:** `designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md` — CARDINAL RULE: judge as-if-built, never by build state.
**Criteria bound:** `references/throughlines_meta.md` — N §0, Ω(a-d) §1, Q(robust/smooth/elegant) §5, Failure Lexicon §7. No new criteria invented.
**Player-action homes read:** `designs/provincial/mass_battle_v30.md` §A.4-A.14 (Part A, TTRPG), Part B (Board Game + tactic cards), Part D (World Bridge / aftermath), Part E (battle consequences); `sim/provincial/massbattle.py`, `sim/provincial/tactic_cards.py`, `sim/provincial/units.py`; `references/module_contracts.yaml` (mass_battle module entry); prior-audit cross-checks: `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_mass_battle.md`, `designs/audit/2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md` (Mass battle / settlement table), editorial ledger `ED-908/909/1088/1090`.

---

## Reconciliation intro

Mass Battle's player-facing declarations live almost entirely inside the §A.7 Battle Turn Structure (seven phases: Strategy Declaration → Volley → Manoeuvre → Offensive Thread → Engagement → Cascade → Reform) plus §A.8 Tactics, with a Board-Game-mode compression in Part B and a mandatory personal-scale bridge in Part D. Three dispersed strands had to be reconciled before any action could be judged:

1. **Formation taxonomy (prose vs. code divergence #1).** §A.6's dice-modifier stance table (Shield Wall, Wedge, Skirmish, Column, Feigned Retreat, Reserve) looks, on a naive read, like it collides with the engine's geometric `Subunit.shape` axis (Line, Arrowhead, GappedLine, Column — with Horseshoe/RefusedFlank retired to Unit-level `build_envelopment`/`build_refused_flank` presets). This is *not* an unreconciled duplicate: Jordan explicitly ruled it (ED-909, 2026-06-09; executed ED-1088, 2026-07-02) as two orthogonal axes — geometry (spatial shape) crossed with posture (dice stance) — with historical grounding (Cannae, Leuctra, Leuthen) cited for the Unit-level presets. The residual (a full shape×stance pairing table) is unfinished *prose documentation*, not an open design question, and is correctly out of scope for a build-state-blind verdict.
2. **Tactic-card contents (prose vs. code divergence #2).** §B.4's tactic-card system (4 shared cards + 8 faction-specific pairs + the Varfell Stratagem initiative-inversion) is confirmed canonical (PP-283). `sim/provincial/tactic_cards.py` ships a deliberately empty `FACTION_TACTIC_CARD_POOL_MODIFIERS` dict, blocked pending a 'contamination audit' (`integration_plan_v18` §1.4) into suspected prior over-authoring. This is pure build-state — the cardinal rule requires judging the ratified prose, not the stub.
3. **Prior-art cross-check.** The 2026-05-28 resolution-diagnostic verdict already found Mass Battle's core architecture N-PASS / Robust-PASS / Elegant-with-one-flag (MB5, no explicit Pool Floor — an architecture finding, not an action-menu finding, out of scope here). That verdict's only *action*-relevant residue is the Splitting-doctrine dominance data (PP-508/ED-358), which this dossier folds into the Concentration tactic finding below.

Twelve player-available-action objects follow, each carrying its own N/Ω/Q read and subtractive disposition. Muster (a Faction-lane action referenced only tangentially in §A.13/A.14) is deliberately excluded — it is FA lane's action to score, per the ED-`<LANE>` taxonomy and the resolution plan's own C-FA-5/8 routing.

---

## Actions

### 1. Sub-unit Assignment (Phase 1; TTRPG cap 3 / videogame cap 11, span-of-control = Command)
**Reconciled view:** §A.5 ties the sub-unit limit directly to Command (`clamp(round((2·Cha+Cog)/3),1,7)`); the TTRPG hard cap of 3 is a tabletop-bookkeeping simplification, the videogame cap of 11 (ED-1090, Jordan-ruled 2026-07-02) is the realized ceiling, with an explicitly flagged (not yet designed) future mechanism for fielding beyond 7 sub-units under a 1-7 Command clamp.
**As-if-built:** the foundational Phase-1 decision every other declaration (formation, split, tactic, reserve) hangs off. Directly encodes a general's real, historically load-bearing capacity limit to coordinate multiple simultaneously engaged bodies.
**Criterion:** N (real command-span dynamic, not fantasy) — Ω-d (Command directly rations how many bodies can usefully be split, a real cost on over-splitting via the Command-based pool math).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3.

### 2. Formation Declaration (Phase 1; dual-axis geometry + stance)
**Reconciled view:** see reconciliation-intro strand 1. Two Jordan-ruled orthogonal axes: geometric `Subunit.shape` (Line/Arrowhead/GappedLine/Column, governing contact/frontage/facing) crossed with A.6 dice-stance (Shield Wall/Wedge/Skirmish/Column/Feigned Retreat/Reserve, governing combat dice), with Envelopment/Refused Flank promoted to Unit-level emergent deployment presets sourced from Cannae/Leuctra/Leuthen.
**As-if-built:** a genuine two-layer historical-command choice — what shape your line takes (which determines who can be flanked/enveloped) and what stance it holds (which determines its dice). No formation is universally dominant (Wedge beats Line; Shield Wall beats Wedge but can't advance; Skirmish resists flanking but concedes to Heavy).
**Criterion:** N (five/six named historical formations, explicit rock-paper-scissors counter logic) — Q-elegant (ED-909's ruling makes the rule restatable — 'shape governs geometry, stance governs dice' — even though the full pairing table is still an unwritten residual).
**Verdict:** KEEP. **Intent gate:** DELIBERATE (Jordan-ruled, ED-909/908/1088). **Severity:** P3. **Calibration:** NEW (this audit's reconciliation of the apparent divergence). **Direction:** lateral.
**Build-state note (routing only):** the full shape×stance pairing table is still an ED-909 'FOLLOW-UP' residual in canon prose — a documentation-completion item, not a design flaw, and not a verdict input.

### 3. Offence/Defence Pool Split (Phase 1, secret, per sub-unit)
**Reconciled view:** each sub-unit secretly commits a fraction of its Effective Pool to Offence vs Defence (default equal, round down to Offence; PP-273 floors both sides at 1D), revealed simultaneously at Phase 5.
**As-if-built:** a distinct per-engagement hidden-information wager layered on top of Formation's persistent stance — Formation is 'how do I stand this whole battle,' the split is 'how hard do I press *this* engagement, this turn, without knowing the enemy's answer.' The default-equal fallback means a disengaged player isn't punished for not manually declaring, without making full declaration pointless (net-hits and critical thresholds reward correct reads).
**Criterion:** Q-robust (secret simultaneous declaration is a genuine distinct mini-game, not redundant with Formation) — Ω-d (full-Offence forfeits Defence and vice versa; no free lunch).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3.

### 4. Tactic Declaration (§A.8 menu, overall)
**Reconciled view:** six named maneuvers (Envelopment, Feigned Retreat, Ambush, Concentration, Refused Flank, Hammer & Anvil), each with an Ob cost and a named counter (Refused Flank counters Envelopment; Scouting counters Ambush; 'Flanks exposed' counters Concentration; 'Break Anvil first' counters Hammer & Anvil).
**As-if-built:** realizes textbook, sourced command doctrine (Cannae-style envelopment, Leuctra/Leuthen refused flank, ambush, mass-of-force concentration, combined-arms hammer-and-anvil) as discrete, always-counterable choices.
**Criterion:** N (all six are named, historically sourced maneuvers) — Ω-d (every entry has an explicit named counter, so none is unconditionally free).
**Verdict:** KEEP (menu as a whole). **Intent gate:** DELIBERATE. **Severity:** P2 (downgraded from P3 only because one menu entry, scored separately below, weakens the set's own Q-robust 'three viable approaches' claim). **Calibration:** KNOWN-TRACKED.

### 4a. Tactic: Concentration (§A.8) — isolated finding
**Reconciled view:** 'All sub-units on one target; max Fibonacci,' countered by 'Flanks exposed.' The corpus's own validated Splitting-doctrine simulation (PP-508, resolving ED-358 / superseding P2-14) is unambiguous: splitting dominates concentration by +9pp to +45pp win-rate depending on Command matchup, and the design itself names only two narrow conditions where concentration is not dominated — (1) the attacker heavily out-commands the defender (Cmd 4-5 vs Cmd 2-3) *and* concentration already approaches the win-rate ceiling anyway, or (2) terrain forces a single engagement (Narrow Pass) or the defender is at floor-Size relative to Command.
**As-if-built:** taken at face value, a player reading the §A.8 table sees six co-equal tactical choices. Concentration is not co-equal — it is a documented, quantified trap pick in the large majority of match-ups. This is real mass-of-force doctrine (Napoleonic 'mass at the decisive point' is a genuine historical dynamic), so it is not an N-fail — but as currently framed as a general-purpose menu entry, it fails the tactic-menu's own Q-robust bar ('three viable player approaches to any situation the mechanic governs') for most of the situations a player will actually face it in.
**Criterion:** Ω-d — a choice that looks viable on the menu but rarely rewards taking it is its own failure of 'every action pays what it buys' (here inverted: the action *costs* an Ob roll and a declaration slot for a payoff that is usually negative-EV relative to the alternative); Q-robust — undermines the three-viable-approaches bar outside the two enumerated windows.
**Verdict:** REFINE (simplify/reframe, not cut — the underlying doctrine and its two legitimate windows are real). **Intent gate:** DELIBERATE (design already knows this: ED-358 resolved narrowed the viability window; this is not a wiring gap). **Severity:** P2. **Calibration:** KNOWN-TRACKED (surfaced 2026-04-XX per ED-358/PP-508; re-surfaced here under the Ω-d/subtractive lens specifically). **Direction:** bottom-up.
**Retires downstream:** Stratum E gauge-triage (`C-MBSE-1/2/3`, resolution_plan_v1 §3 'Mass battle / settlement') — narrows: one fewer general-purpose tactic branch needs independent re-validation once Concentration is explicitly reframed as a terrain/mismatch-conditional counter-tactic rather than a general-purpose menu entry (recommended fix direction: retitle/re-scope the table entry with its own two-condition Ob gate, rather than a mechanical rebalance, since the underlying math is already validated and correct).

### 5. Thread Intent Declaration (declare Phase 1; Leap/operation resolve Phase 4 rear / Phase 5 embedded)
**Reconciled view:** practitioner-generals publicly declare offensive or support intent and a target (declaration = Diagnosis, per the substrate rule); Combat-type ops (Dissolution/Pulling/Locking) resolve Phase 4/5, support ops (Weaving/Mending/Rally) resolve Phase 6 after casualties are known. Costs Coherence automatically per operation and feeds the Substrate Saturation Counter.
**As-if-built:** this is Μ-γ (substrate ontology) made a mass-battle-scale verb, and the clearest Ω-a exemplar in the lane: a practitioner-general's battlefield Leap can create a Thread Gap that registers on the territory card and drifts faction Stability for seasons afterward — traceable, but not fully anticipable at declaration time (Coherence depletion, brittleness thresholds, Gap-Mending drift all compound downstream).
**Criterion:** Ω-a (textbook cross-scale, not-fully-anticipable consequence: battle-scale Thread op → territory Gap → Stability drift) — Ω-c (Discovery Events / Dissociation fire regardless of further player choice once triggered).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** diagonal.

### 6. Reserve Commitment (declare Phase 3; commits Phase 3 of next turn; engages that turn's Phase 5)
**Reconciled view:** a sub-unit in Reserve formation cannot engage the turn it is declared but commits automatically at Phase 3 of the following turn (PP-MB-04 closes the 'does it skip a turn' ambiguity) and is then available for that turn's Engagement, with a default equal Off/Def split for its first engagement (it had no Phase-1 declaration window that turn).
**As-if-built:** models real reserve doctrine — holding a decisive force back rather than committing everything at once — as a distinct WHEN-to-fight decision layered on, not identical to, the stance choice (Formation) of a committed sub-unit.
**Criterion:** N (reserve doctrine is a real, load-bearing pre-modern command dynamic) — Q-elegant (the full timing rule is one sentence and closes its own obvious ambiguity).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** forwards.

### 7. General Action at Phase 6 (Rally / Reinforce Discipline / Support Threadweave / Personal Combat / Stabilise incapacitated general — pick exactly one)
**Reconciled view:** the general's single Cascade-phase action, chosen after that turn's casualties are known (Phase 6 step 4, after Steps 1-3 apply damage and check Discipline/Morale).
**As-if-built:** a forced-scarcity triage decision with full information about the turn's cost — do you save the routing flank (Rally), shore up a cracking unit (Reinforce Discipline), commit your practitioner's Mending, personally duel the enemy general, or save an incapacitated ally general? Each choice forecloses the other four for that Cascade.
**Criterion:** Ω-d (hard one-action scarcity, mutually exclusive, real opportunity cost — no combination is available) — Q-robust (fires with visible, legible stakes: whose flank is at risk, what the general is choosing to sacrifice, is answerable in one sentence from game-state each Cascade).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** top-down.

### 8. Tactic Card Play (Board Game layer, §B.3/§B.4, incl. faction-specific cards + Varfell Stratagem)
**Reconciled view:** see reconciliation-intro strand 2. Ratified canon (PP-283): 4 shared cards + 8 faction-specific pairs, refreshing each season, mapped onto the disposition table with an additional named effect; Stratagem (PP-690) lets Varfell read the opponent's card and revise once before simultaneous reveal, framed as prestige battlefield-reading doctrine (Hannibal at Trasimene, Belisarius), not secrecy.
**As-if-built:** the deliberate compression of the full 7-phase TTRPG declaration set into one face-down card pick, for battles the player is not personally present at — exactly the Zoom-Out register the game needs so the player is never forced to hand-resolve every NPC-vs-NPC battle on the peninsula. The faction-specific cards double as asymmetric faction-identity levers (Royal Guard, Crusade Fervour, Mercenary Surge, Paid Off, Assassination, Iron Discipline, People's Courage), each grounded in that faction's stated doctrine, not generic re-skins.
**Criterion:** N (abstraction of a real dynamic — pre-battle disposition/planning — not fantasy) — Q-smooth (the mode boundary with the TTRPG layer is explicitly specified: §B.5 Hybrid Handoff routes PC-present battles to full TTRPG and PC-absent battles to cards, so the two layers never compete for the same decision — this is not duplicate coverage, it is mode selection).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** lateral.
**Build-state note (routing only):** `sim/provincial/tactic_cards.py` ships an intentionally empty `FACTION_TACTIC_CARD_POOL_MODIFIERS` dict, blocked on a 'contamination audit' (`integration_plan_v18` §1.4) into suspected prior Claude-overreach authoring. The prose is ratified canon (PP-283); per the cardinal rule this build state is not a verdict input.

### 9. Personal Presence / Zoom In-Out (§B.5 phase-lock protocol; §D.3 Player Morale Effect)
**Reconciled view:** the player may enter an otherwise BG-resolved battle at one of three legal phase-lock points (after Phase 1 / after Phase 3 / after Phase 6 Step 1 — PP-103/PP-250 defer any mid-phase trigger to the next legal point, eliminating ghost-unit states). While present, friendly units in the player's territory gain +1 Discipline; if the player takes 2+ wounds or is incapacitated, all friendly units take −1 Discipline immediately.
**As-if-built:** models the real 'does the leader risk himself on the field' dynamic (the doc's own 'Mount & Blade effect' framing) with a genuinely two-sided stake — presence helps morale, but the same presence that helps can, if the leader is hurt, hurt worse. The phase-lock discipline is careful, deliberate engine design specifically to prevent a known failure mode (ghost units), which is itself a real Q-smooth achievement rather than incidental plumbing.
**Criterion:** Ω-b (a personal-scale choice — go to the field or stay safe — with a genuine strategic-scale payoff/cost) — Ω-d (the bonus is capped at +1D and the downside is symmetric, so presence is not free upside).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** diagonal.
**Scope note:** broader Zoom In/Out mechanism ownership sits with the WR lane (Scene Slate); scored here only for the MB-specific timing rule (phase-lock points) and MB-specific consequence (§D.3 Discipline swing), to avoid double-scoring WR's action.

### 10. Pursuit / Recall (§A.12)
**Reconciled view:** Fast units may pursue a routing enemy unit, dealing Offence-successes-as-Size-loss with no enemy Defence roll each turn the pursuit continues, until the pursuing general recalls them (Command Ob 2) or the doc's own explicit warning fires: 'over-pursuing exposes flanks.'
**As-if-built:** models the historically real and historically dangerous decision to press a rout — devastating against a broken enemy, but genuinely risky: Recall is a failable Command check, so a general can lose control of victorious cavalry mid-battle (a real, recorded historical failure mode — armies that won the initial clash and then lost the battle to over-extended pursuit).
**Criterion:** N (pursuit-discipline is a load-bearing, well-attested historical dynamic) — Ω-d (the reward — free damage, no enemy Defence — is paired with a real, failable cost: flank exposure and a Command check that can fail).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** backwards.

### 11. Aftermath Choice (§D.1, Post-Battle Consequence Scene)
**Reconciled view:** after every mass battle, the present player picks exactly one of three beats — Tend the Wounded (Endurance/Attunement Ob2 → +1 Size to a surviving unit + officer Disposition +1), Survey the Damage (Cognition Ob1 → exact casualties/infrastructure damage + one hidden consequence), Address the Population (Charisma Ob2 → Settlement Order ±1 + Renown) — with the other two resolving via NPC AI; an absent player gets a substitute 'Where Were You?' retrospective instead. The beat is mandatory and costs no scene action.
**As-if-built:** despite a superficially parallel 'single skill check' shape across all three, each pays into a genuinely different resource — unit recovery, information/hidden-consequence discovery, and settlement-stat/reputation — so this is not a reskinned triple of the same decision. Because it is mandatory and free, it guarantees the personal-check-to-strategic-stat bridge fires on *every* battle rather than only when a player happens to opt in — this section is literally titled 'World Bridge' in the source doc, and the mechanism earns that name.
**Criterion:** Ω-a/Ω-b (explicit, mandatory personal-check → strategic-stat bridge) — Q-robust (three genuinely distinct payloads and stakes, not flavor-only; each one-sentence-answerable from game-state: whose recovery, what hidden fact, whose loyalty).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** KNOWN-TRACKED. **Direction:** backwards.
**Adjacent-lane note (not a finding):** 'Address the Population' sits near the SE lane's settlement-governance action (`settlement_layer_v30` §3.2); this dossier does not have visibility into that lane's full action set to make a confident cross-lane duplicate-coverage claim, so it is flagged here only as an awareness note for the SE dossier / synthesis pass, not scored as a finding in this lane.

### 12. Assign Officer as Governor (§D.2)
**Reconciled view:** after a battle, a named unit officer at Disposition ≥+2 may be assigned as governor of the battle settlement or any garrisoned settlement — a military-to-civil-administrator conversion (the doc's own 'ROTK post-conquest appointment' framing).
**As-if-built:** converts a personal relationship (officer Disposition, earned turn-by-turn through the player's battle-turn command choices — tactically sound orders, saving the unit, or conversely costing it Size ≥2 or being absent) directly into a strategic-layer asset (a settlement governor). This is as clean an Ω-a bridge as the lane has: battlefield conduct toward a named NPC becomes administrative capacity.
**Criterion:** Ω-a (personal Disposition, built via combat-command micro-decisions, converts directly into a strategic-layer appointment) — N (the veteran-officer-to-administrator pipeline is a real historical dynamic).
**Verdict:** KEEP. **Intent gate:** DELIBERATE. **Severity:** P3. **Calibration:** NEW (not separately surfaced as its own action in prior audits reviewed). **Direction:** diagonal.

---

## Summary table

| # | Action | Verdict | Severity | Criterion | Retires downstream |
|---|---|---|---|---|---|
| 1 | Sub-unit Assignment | KEEP | P3 | N / Ω-d | — |
| 2 | Formation Declaration | KEEP | P3 | N / Q-elegant | — |
| 3 | Offence/Defence Pool Split | KEEP | P3 | Q-robust / Ω-d | — |
| 4 | Tactic Declaration (menu) | KEEP | P2 | N / Ω-d | — |
| 4a | Tactic: Concentration | **REFINE** | P2 | Ω-d / Q-robust | Stratum E gauge-triage (C-MBSE-1/2/3) — narrows |
| 5 | Thread Intent Declaration | KEEP | P3 | Ω-a / Ω-c | — |
| 6 | Reserve Commitment | KEEP | P3 | N / Q-elegant | — |
| 7 | General Action (Phase 6) | KEEP | P3 | Ω-d / Q-robust | — |
| 8 | Tactic Card Play (BG) | KEEP | P3 | N / Q-smooth | — |
| 9 | Personal Presence / Zoom In-Out | KEEP | P3 | Ω-b / Ω-d | — |
| 10 | Pursuit / Recall | KEEP | P3 | N / Ω-d | — |
| 11 | Aftermath Choice | KEEP | P3 | Ω-a/b / Q-robust | — |
| 12 | Assign Officer as Governor | KEEP | P3 | Ω-a / N | — |

**Net:** 11 KEEP, 1 REFINE, 0 DISTILL/PRUNE/MERGE/CUT. The lane's player-action set earns its place under adversarial, as-if-built, pessimist scrutiny; the one flagged item (Concentration) is a scoping/reframing note on a single tactic-menu entry, not a structural problem with the lane.
