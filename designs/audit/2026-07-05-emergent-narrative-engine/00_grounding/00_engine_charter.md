# Emergent Narrative Engine — Design Charter (read this first)

## Status: PROPOSED (design-effort charter — Jordan-vetoable)
## Date: 2026-07-05 · Lane: IN (cross-cutting; touches articulation/arcs/scene cluster) · Branch: `claude/ners-audit-fable5-9cpfdz`

## Premise

The ratified 2026-07-04 NERS audit proved the corpus computes more emergence than it can show
(F-2: 8 Convergence Markers with no detector/applier — now ED-IN-0003; F-4: renderer trigger
gaps — now ED-IN-0004; S-1: transport seams). **There is no GM.** The engine must do what a GM
does: notice that independent mechanical vectors have converged into a story, decide it matters,
call the player into it, and tell it in prose whose register tracks the character's Coherence
and the beholder's Certainty. Deliverable: a PROPOSED design spec + module contract for THIS
game — Godot, deterministic, authored-templates-only, riding the existing Key substrate and
Domain Echo transport, sourced from the simulated-arc corpus.

## The four key considerations (Jordan's — the spec's master sections; every architecture answers all four)

> **Q1. How does the player affect the world?**
> **Q2. How does the world affect the player?**
> **Q3. How do we make events legible as a narrative?**
> **Q4. How do we make these narratives present for the player?**

## Hard constraints (C1–C7 — violating any is a rejected architecture)

- **C1** Authored templates only; offline prose-writer bake; deterministic runtime — NO runtime
  LLM (`videogame_mode_spec.md §0` + Jordan 2026-07-05).
- **C2** No narratological surfacing — detection is internal; the player sees diegetic scenes,
  chronicle, texture — never arc labels or "Rising Action" (Jordan's 2026-04-30 doc-12 veto is
  standing).
- **C3** Key-native I/O on existing transport (Keys, Domain Echo, clocks); no parallel event
  system; the engine **books venues, never owns resolution** — scenes resolve through the
  ordinary subsystem engines (contest/combat/thread/fieldwork/mass-battle/settlement).
- **C4** Closes ED-IN-0003 (convergence detector/applier) + ED-IN-0004 (articulation trigger
  completion) by construction.
- **C5** Holonic guardrails (`holonic_container_doctrine_v1`) — no entity special-casing (arcs
  compile from register DATA), no genericization either; **no new progression currency**.
- **C6** P-14 — thread beats (ED-681's four Rendering-Crisis beats, `threadwork_v30 §3.7`)
  must render.
- **C7** Never railroads — engagement windows are real (seed-testable); pricing preferred over
  gating; foreclosure only via arc events, never silent.

## Q1 — Player affects world (required content)

Participation IS Key-emission (arc-tagged slate scene → resolved by ordinary engines → outcome
Keys enter the arc's causes[] chain); arc-vectors consume player-originated Keys as first-class
lifecycle inputs, transitions conditioned on participated outcomes. Reach scales with position
(Domain Echo aggregate-up; leader delegation = assigned beats returning as owned consequence;
member missions; factionless channels). **Non-participation is also an input** — unattended
arcs proceed autonomously (GD-3-style); ignoring a summons is remembered, never a pause. The
world keeps a ledger of you (Obligations, Standing, Scars, Beliefs, Knot strain, foreclosures,
chronicle) — ethics as pattern, not points (Convictions are the ethics ledger; npc_memory +
Standing + Cascade read accumulated behavior; P-04: no hidden morality meter). Anti-railroad
proof: a different choice at each engagement window measurably changes trajectory.

## Q2 — World affects player (required content)

**Casting**: ONE tie-graph rule (Duty/Conviction alignment, Bonds/Knots, lifepath/location,
Standing, position) drives every summons channel — arc-driven slate injection (riding
`player_agency_v30 §4`'s 7-priority algorithm), NPC Outreach/Demand (≤3/season), Mandatory
Crisis, witness-presence; same mechanism casts NPCs; casting explains *why you*, diegetically.
**Position determines native story**: leaders receive subordinate-originated beats (NPC
concern/project engine pointed upward — reports-as-scenes, requests-for-ruling, disputes;
politics Keys hunt the leader as target; anti-spreadsheet rule: named actors with wants, never
report rows); members receive duties-with-refusal-costs + missions under positional information
asymmetry (T-30 socially applied) + peer/rival standing arcs; **the factionless on-ramp** is a
ladder (Conviction/Duty vectors → settlement arcs → Standing/Obligation as proto-faction
currency → recruitment-as-arc → GD-3 build-your-own) — acceptance test: a factionless PC gets
playable seasons. **The social-scale ladder** individual → family → settlement → territory →
faction → world: each rung names its arc carrier, surfaces, casting ties; story traverses rungs
on the same aggregate-up/distribute-down transport as state; family is the thinnest rung (bind
to Bond/Knot clusters + character_histories or declare absent-deliberate — never silently
skip); territory temperaments get their chance to earn a why. **Impulsion**: pressure arrives
as choices with deadlines (diegetic clocks, forced-choice М-6 turns, refusal costs). **History
conditions the option space** in four modes: gating (TS/Certainty/Coherence/Mandate/clock
thresholds) · pricing (prefer over gating — Obligations price betrayal, don't wall it) ·
foreclosure (permanent closes — Almud's Arc A exemplar; via arc events only, surfaced
afterward in chronicle, budgeted to majors) · pattern-response (oath-breaker vs zealot get
different summons). Every gate cites its ledger cause.

## Q3 — Events legible as narrative (required content)

**Story vs context**: arc membership decides, not event type. **Meaningfulness test**
(orthogonal to §3.2 stakes-loudness): durability × tie-proximity × identity-touch — changes
who someone is (Belief/Conviction/Scar/Coherence), what someone owes (Obligation/Standing/
Knot), or what is possible (gate/foreclosure), for a tie-graph actor. **Emergence vs noise**:
the detector's discrimination — correlation tests (shared targets[], causes[] overlap, temporal
windows, same-direction pressure on a shared stake); noise explicitly backgrounded, never
silently dropped; false positives cost player trust. **Arc taxonomy**: major/medium/minor by
measurable properties (scale span, stakes weight, duration, vector count, protagonist
alignment); lifecycle states (seeded → active → escalating → converging → resolved/dormant/
abandoned) + accumulated weight + participating-actor set, persistent and queryable.
**Coherence as A narrative**: concurrency budget per tier; protagonist-frame braiding;
causes[] continuity (raising the ~15% population rate is load-bearing); chronicle callbacks.
**Salience economy**: foreground budget, promotion/demotion rules, background's dignity
(re-promotable; §3.3 accumulator generalized to arcs). **Recognizable-yet-dynamic NPCs**: slow
variables (Convictions core, Resonant Styles, voice register — arc-grade changes only) vs fast
variables (opinions, concerns, projects — every season); per-NPC lexicon overlays.
**One ledger**: progression IS narrative state (no new currency; NPCs progress through the
same arcs — co-protagonists). **PLOT** (under the doc-12 veto): *experienced forwards as
pressure and choices, recognized backwards as story* — setup = scenario_authoring
campaign-skeleton seed Keys (PP-690 realized) + arc seeding; escalation/turn = lifecycle
transitions + convergence detections (internal); resolution = punctuation rendered
diegetically; retrospect = chronicle + causes[] walk. State what plot shapes this CAN and
CANNOT produce (doc-10 §8.5 NOT-list stands).

## Q4 — Narratives present for the player (required content)

**Surface map**: Tier-1 ambient lens (never modal) · Tier-2 cut scenes (ONLY interruption
medium, 5-15s, rationed) · Tier-3 chronicle (retrospect, searchable) · **texture-between-
scenes** (the immersion-audit gap: rumor, overheard, documents) · the scene slate (where
narrative becomes play); route information classes per surface per Coherence/Certainty
register. **Venue matrix — NOT popups**: every subsystem hosts played scenes (contest 8
proceedings × 4 games; combat duels/General Duel; thread ops/anchoring/Rendering-Crisis beats;
fieldwork trails/case board; mass-battle pre/aftermath; settlement governance events; Knot/Bond
scenes; witness mode; travel flagged thinnest — ED-694 residue). Hard rule: every beat renders
AT a location, THROUGH a venue, or IN the chronicle — no modal dialog divorced from place;
venue-specific interaction shapes per the contest-walkthrough model (ED-IN-0005 policy).
**Watching vs participating**: cut scenes/chronicle/witness-mode (ED-761) are watching; slate
scenes + texture are participating; **every major arc keeps ≥1 open intervention point until
converging and routes through ≥1 playable scene**; spectator surfaces carry casting hooks.
**Trails**: every foregrounded beat leaves a followable diegetic trail (gossip, witnesses,
documents, Thread-Reads — the causes[] walk as in-world media); investigation is the natural
trail consumer. **Showing vs telling**: showing carries the present; telling reserved for
retrospect. **Prose realizer**: graduate the NLG proposal (template/slot schema; offline bake
per Key-type × Coherence/TS/Spirit band × Certainty register × focalizer; per-NPC overlays;
deterministic splice). **Beat budget & pacing**: per-tier season budgets inside
player_agency §4.3's 3-5 scene-action envelope; director layer (articulation §7 D11) owns the
tension curve. **Legibility acceptance criterion**: each surface answers ≥1 of the three
dramatic-legibility questions from the screen; all three answerable at every scale. UI
ceilings: 3-4 personal trackers; mechanical vocabulary never surfaces ("my Faith is shaken,"
not "Certainty −1"). **Anti-oatmeal**: (1) arcs instantiate from typed register vectors bound
to specific factions/NPCs/territories; (2) Expressive Range Analysis as a required bake gate;
(3) the arc_test_batch seed method as NARRATIVE regression — 5 seeds must yield chronicles
differing in named actors, stakes, outcomes.

## The substrate contract (cross-cutting — supports all four)

**States**: engine OWNS (arc-vector states, actor narrative weight, convergence windows,
texture budgets) vs READS (clocks, faction stats, NPC state) — holonic containment. **Keys
in**: subscription model; cadence tied to `propagation_spec_v1` ordering (ORD-3/ORD-4);
filtering ladder (trigger → significance → accumulate → discard); replay determinism (same Key
log → same narrative state, PP-687 §6 V4). **Keys out — TOTAL ACCOUNTING**: every Key touched
is RENDERED / ACCUMULATED / CONSUMED-INTO-STATE / EXPLICITLY DISCARDED with reason — nothing
silent; every emitted Key registered in `key_type_registry_v30` with ≥1 declared consumer whose
`consumes:` names it; `targets[]`/`causes[]` populated. **Edges**: declared-vs-implemented
table for the engine itself; resolves the `mechanical.scene_entered` ownership conflict
(scene_slate vs game_director, [OPEN — Jordan]); gives `game_director` and/or
`scenario_authoring` home docs. **All six directions** (up/down/lateral/diagonal/forwards/
backwards) each with ordering/determinism notes. **Conformance**: a CI-checkable rule per
invariant, each living once in `tools/`.

## Capstone requirements (the worked season trace must exhibit ALL of these)

1. One major arc: seed → slate scene → convergence → resolution → chronicle echo, traversing
   ≥3 social-ladder rungs. 2. One casting moment (why-you via tie-graph). 3. One player-shaped
   branch (participated outcome changes the arc's next stage). 4. One followed-only arc
   (spectator channels, no played scene). 5. One leader beat (subordinate-originated) + one
   member beat (duty-assigned). 6. One option gated / one priced / one foreclosed — each citing
   its ledger cause. 7. Every beat's venue labeled. 8. Meaningfulness test passing one beat and
   failing one context event. 9. Total accounting: zero unaccounted Keys. 10. ARC-S07 (Torben
   Loyalty Clock) compiled end-to-end (typed vector + template slots + trace). 11. Two-seed
   chronicle comparison sketch (must differ in named actors, stakes, outcomes). 12. Type-checks
   against `scale_transitions_v30` §5/§12.

## Method rules (all agents)

Working tree only; cite file §section or tag [UNGROUNDED]; the calibration list from
`designs/audit/2026-07-04-ners-qualitative-audit/00_grounding/00_audit_charter.md` still
applies (KNOWN items are not discoveries); numbers marked [OPEN — Jordan tuning] are
calibration, not structure; write full notes to your assigned notes file under this folder's
`01_workings/` and keep structured output concise.

## Companion grounding

- `01_arc_corpus.md` — the simulated-arc corpus, seed provenance, T-23 vs T-24 state.
- `02_prose_render_stack.md` — prose-writer layers, articulation runtime, the NLG proposal.
- `03_prior_art_and_module_homes.md` — prior questions (docs 10–13, immersion audit), the
  doc:null module cluster, today's scene-selection pipeline.
