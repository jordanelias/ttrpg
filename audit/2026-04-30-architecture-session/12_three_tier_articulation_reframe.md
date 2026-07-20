# Three-Tier Narrative Articulation

**Subject:** Reframe of how the Key substrate produces narrative experience for the player. Replaces the real-time arc-detection approach in `2026-04-30_story_vs_happenings_analysis.md` §4.
**Trigger:** Jordan's observation that real-life narrative coherence emerges through (a) identifiable triggers, (b) named figures, (c) visible contestation — and is mostly *retrospective*, not in-the-moment.
**Date:** 2026-04-30
**Status:** Reframe; supersedes prior arc-detection recommendation.

---

## §0 The Reframe

My prior recommendation (continuous arc detection + real-time pattern surfacing) was wrong in the way you identified: it papered over the real ambiguity of being inside an unfolding event. Real life doesn't tell you "you are now in the Rising Action of a Tragic Arc." Real life is muddy. *And yet* some events do read as coherent at the time — wars, scandals, protests — because of three signals:

1. **Identifiable trigger** (a specific event that started it)
2. **Notable figures** (named actors visibly involved)
3. **Visible contestation** (powers in conflict, or a power under threat)

These signals are *narrower* than full arc shape. They're detectable in real-time because they're concrete: a triggering Key exists, source/target actors are named, faction state divergence is measurable. **The substrate already produces all three.**

Story coherence then arrives in two waves:
- **In-the-moment:** triggers + actors + contest visible; *labels and resolutions absent*; player navigates ambiguity.
- **Retrospective:** at temporal boundaries (year-end accounting), the engine articulates what happened with hindsight. Arcs get named. Causal chains become legible. Story shape emerges.

This matches how the Renaissance actually narrativized its own events. *Cronache* are annual; *ricordanze* are seasonal/annual; papal *registra* organize by year. Coherent stories are constructed at temporal review boundaries from the chronicle of events. Period-correct gameplay should mirror this.

The proposed mechanism: **three-tier articulation**, plus **cut scenes as the punctuation form**.

---

## §1 The Three Tiers

### §1.1 Tier 1 — Continuous mud (default state)

The player experiences events as they happen. UI surfaces:
- **Protagonist frame:** the player's character is the lens; their Memory drives the default feed; their Disposition with NPCs/factions is the default relational view
- **Recent Keys:** what's happened recently from their observer set
- **Faction state at-a-glance:** L, PS, Mandate for entangled factions; numbers move, but no arc labels
- **No pattern claims, no resolution labels.** This is the muddy-present.

The player navigates this ambiguity. Some events feel significant; others don't. The player can't yet know which were inflection points. This is *correct*. Lived experience is muddy.

The substrate does not invent clarity that wouldn't exist.

### §1.2 Tier 2 — Trigger punctuation (event-driven cut scenes)

When specific Key types fire that match real-life "this reads as significant" patterns, the engine punctuates with a brief cut scene. The cut scene names the trigger, identifies actors, and gestures at contest — *without* labeling an arc or projecting resolution.

Triggering Key conditions (initial set):

| Trigger | Cut scene shape | Renaissance equivalent |
|---|---|---|
| `state.scar_acquired` (high salience to protagonist) | Brief moment showing the witnessing or the act | Personal traumatic event in chronicle |
| `state.coup_attempted`, `state.succession`, `mechanical.mission_shift` | Council scene; named figures; immediate aftermath | Court intrigue moment in cronache |
| `da.covert_betrayal` with `exposed: true` | Public revelation; reaction shots | Public scandal moment |
| `env.peninsular_strain_shock` with delta ≥ 1 | Environmental beat (city in unrest, omen, news) | Crisis bulletin moment |
| `meta.knot_formed` / `meta.knot_ruptured` | Recognition or breaking | Bond-forming or breaking moment |
| Cross-faction Key clustering (5+ Keys involving same two factions in 1-2 seasons) | Contest acknowledgement | "Tensions rose between the Houses..." |
| `scene.battle_concluded` | Battle aftermath | Battle chronicle entry |

Cut scene content is *generated* from the Key payload + brief prose template. The engine doesn't author the scenes; it composes them from facts available in the Key:

```
Trigger: da.covert_betrayal (exposed=true)
Source: Captain Almud
Target: Crown faction
Causes: K0001 (scene.insult)

Cut scene composition:
  Title: "The Betrayal Revealed"
  Prose: "Word reaches the Crown that Captain Almud — once trusted —
          has been working against its interests. The chamber falls silent.
          [Crown leader] looks toward the door."
  Visible state: Crown.legitimacy -= 0.6 visible animation
```

Cut scenes are short (5-15 seconds Godot scene time). They punctuate without claiming closure. The player still doesn't know what this *means* for the campaign — only that something concrete just happened that warrants attention.

**This is the trigger + named figures + contest signal made visible.** Not arc labeling; punctuation of significance.

### §1.3 Tier 3 — Year-end articulation (retrospective chronicle + cut scene)

At year-end (4 seasons), the engine performs **chronicle generation** and presents it as a longer reflective cut scene.

Process:

1. **Gather** all Keys emitted during the year, filtered to those observable by the protagonist *or* affecting factions the protagonist is entangled with.
2. **Identify the most causally-connected chains** within the year (and reaching back to prior years where causes[] points there). These are the "stories" of the year — sequences of Keys densely linked by cause-and-consequence.
3. **Identify state-divergence events** — moments where faction L/PS shifted significantly, where succession occurred, where Mission shifted. These are the *named-events* of the year.
4. **Compose chronicle prose** from the gathered events, using period-correct templates:

```
"In the third year of the [scenario_period], the [protagonist_faction] 
 faced [state_divergence_summary]. The year began with [first_significant_key], 
 which led to [chain_climax]. By winter, [year_end_state]..."
```

5. **Present as cut scene** with appropriate visual framing (period-correct illumination, parchment, named portraits of involved figures). Player watches; engine shows the chain visually as it narrates.

Crucially: **the engine narrates events; the player names patterns.** The chronicle says "the Crown lost three border engagements; their captain defected; popular support eroded by harvest" — not "this was the Crown's Tragic Decline arc." Player does the labeling. Engine provides the chronicle.

This matches how *cronache* actually read. Compagni doesn't tell us "this is the Tragic Fall of Florentine Liberty"; he tells us what happened, and we name the pattern.

The retrospective cut scene is the major articulation moment. **The year-end is when story shape becomes legible.**

---

## §2 What Each Tier Solves

| Tier | What it solves | What it preserves |
|---|---|---|
| 1 (mud) | Player experiences ambiguity authentically | Substrate's emergent character; player agency in interpreting |
| 2 (trigger) | Significant events feel significant; named actors identifiable; contest visible | Real-time honesty (no spoiler-labels; no premature closure) |
| 3 (year-end) | Story shape becomes legible with hindsight | Player owns the meaning; engine provides chronicle, not story |

The combination addresses your observation directly:
- *Real life is also a smattering of happenings* — Tier 1 honors this
- *Some occurrences present as coherent (war, scandal, protest)* — Tier 2 captures this
- *Identifiable trigger, prominent figures, contestation* — Tier 2 detection signals are exactly these three
- *Stories emerge after the fact; we can't have the future* — Tier 3 articulates retrospectively, not prospectively
- *Cut scenes as throughline articulation* — both Tier 2 and Tier 3 are cut-scene mechanics

---

## §3 Cut Scenes as the Architectural Form

You named cut scenes as the punctuation form. They serve two distinct functions in this model:

### §3.1 Trigger cut scenes (Tier 2)

- **Length:** 5-15 seconds
- **Frame:** present tense
- **Content:** what just happened, who's involved, immediate reaction
- **Composition:** generated from Key payload + prose template
- **Purpose:** punctuate significance without claiming closure
- **Frequency:** ~2-4 per season, depending on emission density and trigger thresholds

These are the moments where the substrate's mud thickens momentarily into a visible event. They feel like *news bulletins* in the Renaissance sense — heralds arriving, public proclamations, witnessed acts.

### §3.2 Retrospective cut scenes (Tier 3)

- **Length:** 30-90 seconds
- **Frame:** past tense, reflective
- **Content:** the year's significant chains; named events; state changes; visible figures
- **Composition:** generated by chronicle assembly from year's Keys
- **Purpose:** articulate what happened with hindsight; let story shape emerge
- **Frequency:** once per year (4 seasons)

These are the moments where the chronicle is *read aloud*. They feel like *manuscripts being copied* in a scriptorium — a year's events composed into prose, illuminated with portraits of those involved, intoned by a narrator.

### §3.3 Optional: Player-triggered cut scenes

The player can request a retrospective at any moment ("show me the chronicle so far") and receive a chronicle through the most recent Accounting boundary. This is the *Why?* diagnostic in narrative form — instead of a bare causal chain walk, the player gets prose articulation.

This is optional but powerful. It means players can *stop and look* at their accumulating story whenever they want, even mid-year, without forcing the engine to articulate continuously.

---

## §4 What the Substrate Already Provides (So This Is Cheap)

The three tiers don't require new substrate. Everything is already in PP-687:

| Tier requirement | Substrate piece |
|---|---|
| Tier 1 protagonist frame | Per-NPC Memory, Disposition matrix, observer set |
| Tier 2 trigger detection | Key types + Key emission events |
| Tier 2 named figures | Key.source_actor + Key.targets |
| Tier 2 contest visibility | Cross-faction Key clustering (queryable from CAUSAL_GRAPH or Key log) |
| Tier 3 chronicle assembly | Year's Keys + CAUSAL_GRAPH walks + state trajectories |
| Tier 3 named events | High-magnitude state-transition Keys |

**No new substrate.** What's needed:

1. **A Tier 2 trigger ruleset** — list of Key conditions + cut scene composition templates. Authored once; ~15-25 trigger types.
2. **A Tier 3 chronicle generator** — algorithm that selects significant chains and composes period-correct prose. Authored once; uses Key log queries.
3. **Cut scene rendering** — Godot Phase 5a scope; integrates with existing scene system.

Estimated effort: PP-688 (Tier 2 + Tier 3 spec) is medium; Phase 5a Godot work is the larger piece because of cut scene visuals.

---

## §5 What This Replaces in My Prior Recommendation

In `2026-04-30_story_vs_happenings_analysis.md` §4 I proposed:

| Prior proposal | Reframed |
|---|---|
| §4.1 Protagonist frame | **KEEP** — Tier 1 default lens. |
| §4.2 Arc detector running each season, surfacing in HUD | **REPLACE** — no continuous arc labeling. Tier 2 triggers fire instead, without arc names. Tier 3 chronicle articulates retrospectively. |
| §4.3 Arc resolution punctuation | **REPLACE** — Tier 2 trigger cut scenes punctuate *events*; Tier 3 articulates *years*. Arc *resolution* is identifiable in retrospect through chronicle reading, not announced as it happens. |
| §4.4 Probability deltas | **REVISE** — see §7 below. |

The earlier framing presupposed real-time arc-aware UI. The new framing accepts ambiguity in the present and uses temporal boundaries for articulation. It is closer to lived experience and to Renaissance documentary practice.

---

## §6 Probability Estimates Revised

| Configuration | Story experience frequency |
|---|---|
| Substrate alone | ~10-15% |
| + Tier 1 (protagonist frame as default lens) | ~25-30% |
| + Tier 2 (trigger cut scenes; no arc labels) | ~40-45% |
| + Tier 3 (year-end chronicle cut scenes) | ~70-75% |
| + scenario authoring (campaign skeletons) | ~80-85% |

The numbers are similar to my prior estimate, but the *quality* of the story experience changes:

- Prior approach: player gets continuous arc labels → game feels like a simulation dashboard with story tags
- New approach: player navigates mud, has triggered moments of significance, receives chronicled retrospectives → game feels like a *life lived*, not a story told to you

The latter is what you actually want. It's also more period-correct.

---

## §7 Year-End as the Anchor

Year-end accounting is the right granularity for retrospective articulation. Three reasons:

1. **Renaissance practice.** *Cronache* and *ricordanze* are typically annual. Annual review is the period's native temporal frame for narrative composition.

2. **Mechanical pacing.** A year (4 seasons) is long enough that arcs can have visible rising/falling action; short enough that articulation stays current. End-of-season is too frequent (most seasons won't have a clear shape); end-of-campaign is too infrequent (players need articulation along the way to stay engaged).

3. **Statistical reliability.** Sim shows ~360 Keys per year (60-120 per season × 4 seasons). That's enough material for chronicle assembly. Most years will have *something* to articulate even if the substrate produced an undramatic year.

**This makes Accounting events themselves carry articulation weight.** The end-of-year Accounting Key (`mechanical.accounting` with annual=true) becomes the trigger for chronicle generation and retrospective cut scene. Annual Accounting becomes the player's "checkpoint" not just mechanically but narratively.

---

## §8 What the Chronicle Looks Like (Sample)

To make this concrete — sample year-end chronicle generated from a hypothetical year's Keys (illustrative; actual templates would be more polished):

> **The Third Year**
> 
> The year began under the Crown's reformed Mission, declared the previous winter following the failed eastern campaign. Captain Almud, newly elevated to command, faced his first season tested by the spring engagements at the border, which proved indecisive but costly.
> 
> By summer, the Spymaster's covert action against the Lowenritter — long suspected by some at court — was uncovered. The exposure carried a heavy cost: the Crown's standing among the eastern provinces eroded measurably. Yet Almud's stewardship preserved what dignity remained. The Council convened in late autumn under conditions of strain, and a new season's Mission was set.
> 
> By harvest, three of the Crown's captains had taken Conviction Scars from the year's events. The Cathedral's posture toward the Crown softened, perhaps anticipating need; the Restoration's positions hardened. The peninsula's strain rose as winter approached.
> 
> Almud's leadership remains intact; the Crown's purpose, contested.

This is composed mechanically from:
- Mission shift Key (last winter)
- Succession Key (Almud)
- Spring battle Keys
- Covert betrayal Key with exposed=true
- L/PS trajectory data
- Cross-faction Disposition shifts
- Conviction Scar Keys
- Strain shock Key
- Year-end faction state

The *names* (Almud, Spymaster, Lowenritter, Cathedral, Restoration) come from Key payloads. The *prose templates* are authored once. The *selection of which events to include* is by causal-connectedness ranking. The *narrative voice* is period-stylized but mechanically generated.

**Player reads this. Player names the pattern: "ah, this was the year my Crown almost broke." The engine doesn't make the claim. The player does.**

---

## §9 Honest Limitations

Even with three-tier articulation, two limits persist:

1. **Some years won't have a strong shape.** The chronicle will read as "and then this happened, and also that, and also..." — the *and-then* failure mode. Mitigation: chronicle generator prefers to include causally-connected chains; isolated events are demoted to background. But truly arcless years remain possible. This is honest; not all years in real life have a story shape either.

2. **Player must engage to receive narrative.** A player who skips cut scenes or skims chronicles won't experience story. The architecture provides the mechanism; player attention is what realizes it. This is true for any narrative game; not unique to this architecture.

A third less-limiting note: the Tier 2 trigger ruleset is *authored*. Different trigger conditions produce different feels. Calibration during Stage 10 / Phase 5a will tune what counts as significant enough for a cut scene. This is design work, not architecture.

---

## §10 Updated Sequencing Recommendation

After PP-687 ratifies:

1. **PP-688 Articulation Layer (formerly Arc Detector)** — codifies Tiers 1-3.
   - §3.x trigger ruleset (~15-25 conditions, prose templates)
   - §3.x chronicle generator (selection algorithm + prose composition)
   - Both are Class A subsystems consuming the Key substrate.
   - Estimated effort: 2-3 sessions.

2. **PP-689 Scenario Authoring Layer (optional but powerful)** — campaign skeletons with seed Keys + inflection-point Keys. Raises arc-rich starting states.

3. **Phase 5a Godot scope addition: cut scene system.**
   - Scene rendering for trigger cut scenes (5-15 sec)
   - Scene rendering for chronicle cut scenes (30-90 sec) with parchment/illumination aesthetic
   - Player-triggered chronicle review

Phase 5a Godot estimate: increases by ~1-2 sessions for cut scene work, but produces the most player-facing impact of any single feature.

Drop the prior recommendation for "PP-689 Chronicle Generator" as a separate proposal — it's now part of PP-688 since chronicle generation and trigger detection share the same substrate query infrastructure and prose-template approach.

---

## §11 Verdict

The reframe is the right move. Prior approach treated narrative as a real-time labeling problem; new approach treats it as a *temporal articulation* problem.

**What changes:**
- Tier 1 preserves authentic ambiguity in lived experience
- Tier 2 punctuates significance through trigger-detection, not arc-labeling
- Tier 3 articulates story shape retrospectively at year-end via chronicle generation
- Cut scenes are the punctuation form for both Tier 2 (trigger) and Tier 3 (chronicle)

**What stays:**
- Substrate (PP-687) unchanged — provides everything needed
- Protagonist frame (UI default lens) still the right entry point
- Probability estimate of "story" experience: still ~70-85% with full implementation

**What's earned by the reframe:**
- Period-correct narrative practice (cronache tradition; annual articulation)
- Player owns meaning; engine provides chronicle (preserves agency)
- Cut scenes have authentic dramatic timing (triggered + retrospective, not continuous)
- Real-time experience matches lived experience (mud, with moments of clarity, with retrospective sense-making)

**Net assessment:** This is the right architecture for what you're trying to build. The throughline is *the chronicle, articulated annually, punctuated by triggered cut scenes, framed through the protagonist's eyes*. Player navigates ambiguity in the present and receives coherence in retrospect, exactly as in lived experience and exactly as Renaissance subjects experienced their own histories.

---

**End reframe.**
