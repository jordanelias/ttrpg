# Lens: playability_legibility — working notes

Lane of the 2026-07-04 qualitative NERS audit. North Star: emergent-narrative player
experience, rich meaningful choices, "from the screen" dramatic-legibility bar. Working tree
only; commit context ~cb227cf. Method: walk one hypothetical season across scales, apply the
three dramatic-legibility questions per juncture, count trackers, check immersion precedent,
and ask which subsystems have any player-interaction model at all.

## KEY REFRAME OF THE BRIEF (verified)

The brief says the contest walkthrough is "the one existing UI-model precedent." Verified more
precisely: it is the only *current-era* one. A large **CANONICAL** player-facing spec exists —
`designs/ui/valoria_ui_ux_v4_1.md` ("every interface surface the player encounters", status
CANONICAL, dated **2026-04-16**) — but:
- It predates the ENTIRE current generation: d+σ resolution, `combat_engine_v1`, the contest
  rebuild, the mass-battle re-architecture, the Key substrate / propagation spec. Its stated
  dependency is "all 19 v30 canonical design documents" + a `combat_v30` Wound patch — i.e. the
  superseded combat head.
- It is **absent from `CURRENT.md`** entirely (`grep` for `designs/ui`/`ui_ux`/`player_agency`/
  `scene_slate` in CURRENT.md → no rows). So the currency index does not point at it, and a
  session establishing currency the prescribed way never finds it.
- Its own repair workplan `designs/ui/valoria_ui_ux_v4_2_workplan.md` (69 findings, **20 P1**)
  targets a replacement `valoria_ui_ux_v4_2.md` that **was never created** (dir listing: only the
  workplan exists). Last substantive git touch of v4.1 = 2026-06-28 bulk workplan commit, not
  content.

Net: the North Star's "answer it from the screen" bar has **no maintained home**. The only
current-era player-interaction artifact is `player_interaction_walkthrough_v1.md` — itself DRAFT,
covering **one** subsystem (Agôn contest), and explicitly scoped to the "one game that is fully
built." Every other scale's player-facing surface is either stranded in the stale v4.1 or unwritten.

## CONTAMINATION: non-canon trackers in the Godot-facing UI reference

v4.1 §9.7/§9.8/§10.2/§11.3 still specify **Taint** (a separate 0–6 track) and a **CD track** as
player-facing. Canon STRUCK both: `designs/threadwork/threadwork_v30.md:653` "No separate Taint
track", :984, :990 ("'Taint' → Cut — Coherence degradation, All references"). The repair items
(v4.2 workplan F-15/F-16, "active contamination of the Godot reference") were never executed, and
the ED numbers the workplan proposed to register them under — ED-638/639/641 — are **already
occupied by unrelated ledger entries** (Varfell Skald-Chief; Cardinal name; Warden Conviction).
So a Godot developer building the character sheet from the canonical UI reference renders two
trackers that do not exist. KNOWN-UNTRACKED (documented only in an unexecuted workplan; no live
ED). Direction bottom-up.

## TRACKER COUNT / COGNITIVE LOAD (one season, all scales)

Distinct named trackers the player must hold, gathered from the docs I read:

Personal/scene: Coherence (10→0), Seasonal Fatigue, Face (Cha×3 ceiling), Concentration (5–35),
Persuasion Track (0–10), Doubt Marker, Wounds/Health, Momentum, Resources (0–5), TS, Certainty,
Evidence Track, Exposure / Church Attention Pool, per-NPC Disposition, Conviction strain (×3
Convictions). Player-progression: Standing (0–7), Renown (0–10), scene-action budget (3–5).
Strategic: Mandate (0–7), Stability, Accord (province), Turmoil, CI clock, MS/RS world track, IP
clock, per-settlement Prosperity/Order/Defense, Treasury/Military, settlement L/PS.

≈ 27–30 named trackers, before per-NPC and per-settlement multiplicity. The 2026-05-08 immersion
meta-audit sets the corpus's own ceilings: **3–4 per-decision consultations for personal scenes,
"7 at ceiling" for strategic** (§3 "Am I pulled out by mechanics?", §5 finding 2). The realized
surface is far above that, and only contest (walkthrough) and, partially, combat carry any
presentation-layer translation. The immersion audit's core charge — mechanical vocabulary
("Piety Track Scars", "Cascade Fidelity", "Resonant Style primary+secondary", "Self-Other
orientation scalar") leaking to the player — is unaddressed, and the layer meant to fix it (v4.1's
"what the player sees" translations) is the stale/off-index doc above. New scope vs the immersion
audit: the cross-scale *count*, and that the mitigating layer is stranded.

## DRAMATIC-LEGIBILITY WALK (three Qs from the screen, per juncture)

- **Strategic decision (faction):** PARTIAL. Mission/Doctrine text answers "what does each actor
  want"; "whose position is at risk" is scattered across 5 Stability Triggers with no single
  surfaced threshold line (faction dossier; faction_canon Part B). Autonomous-world hole:
  faction_layer §5.8 hands NPC votes to a human GM in a no-GM engine.
- **Domain action (settlement governance):** WEAK. Ratified loop is a single stat-pump verb-pick;
  only "what happens if no one acts" is cleanly answerable (Prosperity 0→famine, Order 0→revolt).
  Local Actors carry one Conviction but **no ambition/goal field**, so "what does each actor want"
  is unanswerable at the governor tier (settlement dossier; governance_play_redesign, unratified).
- **Social contest:** PASS — for Agôn only. The walkthrough's §0 principle ("every number the
  resolver uses is a number the player can see before committing") makes all three answerable, and
  hidden values (opponent Face, adjudicator convictions) degrade to a *consequence class* (Appraise
  hint / debuff icon), which is the correct legibility discipline. But 3 of 4 games raise
  NotImplementedError, so the test literally cannot be run for Negotiation/Inquiry/Consensus.
- **Combat:** FAIL. player_agency §4.4 routes a scene into combat as "the player's choice" of
  system, but per the personal_combat dossier the engagement loop exposes **no per-exchange
  player-decision parameter**, and Health/Wounds carry no goal/intent/political stake and no
  season-clock hook. The one current-era scale with neither an interaction model NOR threadwork
  (ED-911, open P1). All three Qs fail from the combat screen.
- **Thread op:** PARTIAL and rich. Decision space is genuinely non-dominant/multi-axis, but a
  player cannot state in one sentence *which world track is failing* because the MS vs RS naming
  split is live across canonical docs (threadwork_v30 §5 = MS; params/threadwork.md = RS; sweep
  ED-731/772 never reached params). A legibility tax on the richest decision space.
- **Season close:** UNEVEN. The "Where Were You?" retrospective (scale_transitions §4) plus the
  articulation chronicle are the designed surfacing, but articulation is silent on
  Thread/Calamity, self-contradictory on battle-conclusion coverage, blind to victory-era
  transitions (ED-1006), and has a starvation path (a Bonded NPC whose Keys never match a trigger
  is never rendered). So "what happened / whose position moved" is exactly weakest at the moment
  designed to answer it.

## SUBSYSTEMS WITH NO PLAYER-INTERACTION MODEL

Contest: yes (walkthrough, DRAFT). Combat: none (autonomous). Domain/settlement governance:
none current (unratified redesign). Faction strategic: only stale v4.1. Thread op: none current.
Mass battle: none current. Season close/articulation: none current. Implication: the contest
walkthrough is a *template* that has been applied once; the GM-removal mandate it exists to
satisfy ("the engine PRESENTS what a GM used to narrate") is unmet for ~6 of 7 scales, and there
is no live index entry commissioning the rest. This is the single biggest playability gap.

## POSITIVE PATTERNS TO PRESERVE

- The contest walkthrough's "resolved value = visible value" + "hidden value → consequence class"
  is the right, reusable legibility contract; §4 already pre-specifies divergent shapes for the
  other three games so they don't converge onto one UI.
- v4.1's *method* (capability-gated Thread UI, Standing/Renown-gated clock panels, per-Part "what
  the player sees") is sound salvage material — the problem is currency, not thinking.
