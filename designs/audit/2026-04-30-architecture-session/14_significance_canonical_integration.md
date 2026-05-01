# Significance Function — Canonical Knot/Belief/Inspiration Integration

**Subject:** Refinement of significance function (`2026-04-30_significance_function_omniscient_voice.md`).
**Trigger:** Two corrections from Jordan I should have caught before drafting:
  (1) **Player participation is itself the significance signal** — they were called to a scene; the scene happened. Their throughline is visible in what scenes they completed.
  (2) **Knots, Beliefs, Inspirations are existing canonical mechanics** with established mechanical weight. The significance function reads from them, doesn't invent parallels.
**Method:** Searched repo before drafting. Citations to canonical sources inline.
**Date:** 2026-04-30
**Status:** Refinement; integrates into PP-688 spec.

---

## §0 What I Missed

In `2026-04-30_significance_function_omniscient_voice.md` I built a "protagonist significance" track using generic measures (observer set membership, Disposition magnitude, faction involvement). I should have read from canonical mechanics that already encode "what matters to this player-character":

- **Knots** (`designs/scene/fieldwork_socializing.md` §5.6; PP-632) — relational bonds the player has *invested in*; gated by significant gameplay thresholds; rupture is mechanically severe (5 Composure damage)
- **Beliefs** (`references/glossary.md` L151; fieldwork_socializing §5.5) — player-authored convictions that drive Momentum and Character Points; Belief-aligned/challenging/betraying are the canonical moral-political-engagement axis
- **Inspirations** (glossary L152; `params/core.md` L128) — named foci granting bonus dice when engaged; Resolve = Spirit caps total Inspiration value

These are not metaphors I should invent — they are the **player's authored statement of what they care about**, already weighted by mechanical effect. Significance scoring should consume them directly.

Plus the deeper point I missed: **the player only experiences scenes they played**. Participation isn't a significance modifier; it's the very definition of what the player's throughline contains.

---

## §1 The Scene-Completion Principle

A scene the player completed = a scene that exists in the player's narrative throughline.

This is mechanical, not interpretive:

- The player chose (or was called to) a scene
- The scene resolved with their participation
- Keys emitted during the scene have the player as observer (always) and often as source_actor or target
- The scene's existence in the player's experience is non-negotiable — they were *there*

This means **player_significance for any Key emitted in a player-completed scene starts at a high baseline**. Not because the player is privileged narratively but because their attention-budget was spent on this moment. The substrate should reflect that investment.

```python
def scene_completion_baseline(key, player):
    """Minimum significance for any Key in a scene the player participated in."""
    if key.scene_id and player.scenes_completed.contains(key.scene_id):
        return 0.5   # baseline floor
    return 0
```

This is a floor, not a ceiling — Keys *outside* scenes the player played still get significance scored normally; Keys *inside* are guaranteed at least 0.5 player_significance regardless of other factors.

**The player's throughline is the ordered sequence of scenes they completed**, plus the Keys those scenes emitted, plus the chain of consequences propagating from those Keys. The chronicle reads this ordering naturally.

---

## §2 Canonical Mechanics → Significance Inputs

### §2.1 Knots (relational weight)

Knots are *earned*. Formation requires Disposition+5, TS≥30 (one party), capacity in Knot Pool, and a successful Connect roll vs Spirit pool TN 7 Ob 2 (`fieldwork_socializing.md` §5.6). A Close Knot costs 5 Pool points. **A player who has formed a Close Knot has invested significant gameplay effort.** That investment is the substrate's signal of relational stakes.

Significance contributions from Knots:

| Knot involvement | Effect on significance |
|---|---|
| Key targets a Knot-bonded NPC of the player | +0.20 to player_significance baseline |
| Key.source_actor is a Knot-bonded NPC | +0.15 to player_significance |
| Knot tier modifier | Close: full weight; Medium: 0.6×; Loose: 0.3× |
| **Knot formation Key** | **automatic high-significance event** (universal_sig += 0.25 floor; player_sig += 0.5 floor) |
| **Knot rupture Key** | **automatic very-high-significance event** (universal_sig += 0.35 floor; player_sig += 0.7 floor) |
| Knot-partner appears in cut scene | counts as cumulative narrative weight bump for that NPC |

Knot rupture is the most narratively severe non-mortality event the substrate produces. The 5-Composure-damage cost (per `fieldwork_editorial.md` SIM-DEBT-SOC-03) is gameplay-load-bearing; it is *also* narrative-load-bearing. A ruptured Knot warrants a chronicle named-event regardless of other factors.

The Mitsein framing is important: Knots are the substrate's representation of *being-with*. Their engagement, formation, and rupture are categorically narrative events.

### §2.2 Beliefs (moral-political engagement)

Beliefs are player-authored. They are the player's declaration of *what their character is about*. The fieldwork_socializing §5.5 already encodes engagement gradients:

| Belief engagement | fieldwork canonical effect | Significance contribution |
|---|---|---|
| Belief-aligned action (success) | +1 Momentum (cap 4), counts as Belief achievement | player_sig += 0.20; expectation_weight bump |
| Belief-challenging action (success) | No Momentum; GM marks Belief revision opportunity | player_sig += 0.30 (challenge is more narratively significant than alignment) |
| Belief-betraying action | Certainty pressure resolves at session end | player_sig += 0.40; this is a very high-significance moment |
| **Belief revision (when triggered)** | **character-development beat** | universal_sig += 0.20 floor; player_sig += 0.6 floor; **chronicle named-event** |

**Belief revision is a canonical character-development arc beat.** The substrate already tracks "potential Belief revision opportunity" markers (per §5.5). When revision actually fires, it is the player's character changing — the Self-Other-axis-style *internal* arc but at the level of authored conviction. Belief revision events deserve cut scenes and chronicle prominence by default.

This also resolves an imprecision in the prior significance function: I had Self-Other orientation magnitude as the "Public expectation/judgment" input. Belief engagement is the more specific, canonical signal — Self-Other orientation is *one* facet; Belief alignment is *the player's stated facet*. The two coexist; Belief alignment is the more reliable in significance scoring because it's authored.

### §2.3 Inspirations (thematic engagement)

Inspirations grant bonus dice when engaged in relevant scenes. They are *thematic markers* — the player's statement of what their character is about *aesthetically* or *focally*, distinct from the moral-political compass of Beliefs.

| Inspiration engagement | Significance contribution |
|---|---|
| Scene engages an Inspiration (bonus dice received) | player_sig += 0.10 |
| Multiple Inspirations engaged in same scene | player_sig += 0.05 per additional |
| Inspiration-engaged scene resolution at high degree | player_sig += 0.05 (success at thematic point) |

Inspirations contribute less than Knots and Beliefs because they're *modifiers*, not *commitments*. A scene with engaged Inspiration is thematically resonant for the character but not necessarily a turning point. The contribution is real but bounded.

---

## §3 Revised player_significance formula

The earlier draft said:

```python
protagonist_significance(key, protagonist) = clamp(
    0.4 * is_in_observer_set(key, protagonist)
  + 0.2 * disposition_magnitude_to_actors(...)
  + 0.2 * is_protagonist_faction_involved(...)
  + 0.2 * cumulative_memory_overlap(...)
, 0, 1)
```

Generic substrate measures. It works but doesn't read from authored player commitments.

Revised:

```python
def player_significance(key, player):
    base = scene_completion_baseline(key, player)   # floor, see §1
    
    knot_bonus = compute_knot_involvement_bonus(key, player)
    belief_bonus = compute_belief_engagement_bonus(key, player)
    inspiration_bonus = compute_inspiration_bonus(key, player)
    
    # Generic substrate measures (still relevant; lower weight now)
    generic = (
        0.15 * is_in_observer_set(key, player)
      + 0.10 * disposition_magnitude_to_actors(player, key)
      + 0.10 * is_player_faction_involved(key, player)
      + 0.05 * cumulative_memory_overlap(key, player)
    )
    
    return clamp(base + knot_bonus + belief_bonus + inspiration_bonus + generic, 0, 1)
```

Where:

```python
def compute_knot_involvement_bonus(key, player):
    bonus = 0
    actors = [key.source_actor] + [t.actor_id for t in key.targets]
    for actor in actors:
        knot = player.knots.get(actor)
        if knot:
            tier_weight = {"Close": 1.0, "Medium": 0.6, "Loose": 0.3}[knot.tier]
            bonus += 0.20 * tier_weight if actor in [t.actor_id for t in key.targets] else 0.15 * tier_weight
    if key.type == "meta.knot_formed" and key.payload.get("participants").contains(player.id):
        bonus += 0.50
    if key.type == "meta.knot_ruptured" and key.payload.get("knot_id") in player.knots:
        bonus += 0.70
    return bonus

def compute_belief_engagement_bonus(key, player):
    bonus = 0
    engagement = key.payload.get("belief_engagement_for", {}).get(player.id)
    if engagement == "aligned":      bonus += 0.20
    elif engagement == "challenging": bonus += 0.30
    elif engagement == "betraying":   bonus += 0.40
    if key.type == "state.belief_revised" and key.payload.get("npc_id") == player.id:
        bonus += 0.60
    return bonus

def compute_inspiration_bonus(key, player):
    engaged = key.payload.get("inspirations_engaged_for", {}).get(player.id, [])
    if not engaged: return 0
    return min(0.20, 0.10 + 0.05 * (len(engaged) - 1))
```

These functions read from canonical mechanics already present in the substrate (Knots, Beliefs, Inspirations are tracked on each character; engagement state is recorded on Keys per scene resolution).

---

## §4 What the Substrate Needs to Carry

For the above to work, scene-resolution Keys need three additional payload fields recording the canonical engagement state:

| Field | Purpose | Source |
|---|---|---|
| `belief_engagement_for: {actor_id: aligned/challenging/betraying}` | Per fieldwork_socializing §5.5 outcome categorization | Scene resolution computes from Belief vs action vector |
| `inspirations_engaged_for: {actor_id: [inspiration_names]}` | Which Inspirations gave bonus dice | Already tracked at scene resolution per derived_stats_v30 |
| `knot_partners_present: [actor_ids]` | Which of the source_actor's Knot partners are in the scene | Computed at scene initialization |

These extend the existing scene-event Key payload schema (`scene.dialogue`, `scene.contest_resolved`, etc.) without modifying the universal Key schema. PP-687's per-type registry handles this — these become required-payload fields for scene-event subtypes.

Plus three new Key types to add to the registry:

| Key type | When emitted | Notes |
|---|---|---|
| `meta.knot_formed` | Successful Knot Formation roll per §5.6 | Permanence: indelible. Public visibility unless private formation. |
| `meta.knot_ruptured` | Knot rupture event (mechanism per ED-773 lifecycle) | Permanence: indelible. 5-Composure-damage payload. |
| `state.belief_revised` | Player Belief revision per fieldwork_socializing §5.5 marker | Permanence: indelible. Records old + new Belief. |

These are Class B extensions to the Key registry per PP-687 §4.3.

---

## §5 Why This Is Better Than What I Had

The prior draft's significance function used generic substrate measures. They worked, but they treated all NPCs and all events as roughly equivalent until weighted. **The canonical mechanics already do the weighting** — they're authored statements of what matters to this character.

A Knot-bonded captain is *not* an arbitrary NPC the player has high Disposition with — they are an NPC the player invested ~5 Pool points and a successful Connect roll into. The substrate should treat that investment as weighted-in, not re-derive it from generic Disposition magnitude.

A Belief-challenging social action is *not* an arbitrary event the player observed — it is a moment the player's authored conviction is being tested. The substrate should treat that as weighted-in via the Belief engagement state, not re-derive it from Conviction-axis projection alone.

An Inspiration-engaged scene is *not* an arbitrary scene the player participated in — it is a scene that thematically resonates with their character. The substrate should treat that resonance as weighted-in via the Inspiration engagement record, not re-derive it from generic scene-completion presence.

In each case: **the canonical mechanic is the authored signal of significance.** The function should read from it.

---

## §6 The Player as Always-Protagonist

Returning to your first point: *"if the player character is involved, then they were called to action to play out the scene. the player is always important in narrative because THEIR arcs and participation in other arcs is visible by what scenes the player completed."*

This is more correct than my prior framing. I had treated player_significance as "events that happen to be more relevant to the player." Better:

**The player_significance score is the *visible-to-the-player throughline filter.*** If they completed a scene, that scene is in their throughline by construction. The significance function determines:
- Which scenes get cut scenes (ones with significance ≥ Tier 2 threshold)
- Which Keys the chronicle prominently features (ones with significance ≥ Tier 3 prominent placement)
- Which background events still get summarized (significance below threshold but participated in)

The player's narrative throughline is *literally* the trace of their scene completions, with significance scoring deciding which moments crystallize into cut scenes vs which fade into background.

Universal significance still exists — it determines whether *peninsula-level* events warrant chronicle inclusion regardless of player participation. A war the player isn't directly in is universally significant; the chronicle reports it. But the player's *throughline* is the ordered set of scenes they played, weighted by Knots/Beliefs/Inspirations engaged within them.

This is a cleaner framing. The player isn't *more important* than other characters in the world — but their *experience* of the world is the trace of scenes-they-completed, and that's what the chronicle should reflect for them.

---

## §7 Worked Example (Revised)

A Knot-bonded captain (Almud, Close Knot with player) is publicly accused of treason. The accusation scene engages the player's Belief about loyalty. The player participates in the scene.

| Significance input | Value |
|---|---|
| Scene completion baseline (player participated) | 0.5 |
| Knot involvement (Close Knot, Almud is target) | +0.20 |
| Belief engagement (challenging — player's loyalty Belief tested) | +0.30 |
| Inspiration engagement (none assumed in this case) | 0 |
| Generic measures (faction involved, Disposition magnitude) | +0.20 |
| **Total player_significance** | **clamped at 1.0; threshold easily crossed** |

| | |
|---|---|
| Universal significance (Almud is Crown Captain, public accusation, Cascade impact) | ~0.75 |

Both tracks high. Tier 2 cut scene fires immediately; Tier 3 chronicle features prominently. The omniscient retrospective at year-end reveals attribution the player couldn't have known at the time.

Compare: **same accusation, same Almud, but no Knot, no Belief engagement, player wasn't in the scene.** Universal significance still ~0.75 (warrants chronicle mention); player significance ~0.20 (doesn't trigger cut scene; goes into chronicle as ambient context).

The function distinguishes correctly.

---

## §8 What's Replaced

Replaces in `2026-04-30_significance_function_omniscient_voice.md`:

- §1.4 protagonist_significance formula → §3 here (richer, reads canonical mechanics)
- Implicit "any-actor" treatment of named figures → §1 scene-completion principle (explicit player-attention model)
- Self-Other orientation as primary moral-political input → demoted to one-of-several; Belief engagement is the primary

Keeps:

- Universal significance formula (§1.2) — unchanged
- Two-track significance scoring (universal + player) — unchanged structure, refined inputs
- Tier gates and thresholds — unchanged
- Cumulative narrative weight tracking — unchanged
- Awareness post-emission update — unchanged

---

## §9 What Should Have Happened

I should have searched the repo before drafting the significance function. The Knot/Belief/Inspiration mechanics are well-established; pretending to invent equivalents was wasted effort and risked drift from canon. Reading first would have produced cleaner output the first time.

This refinement integrates them properly. PP-688 (Articulation Layer) spec should consume `fieldwork_socializing.md` §5.5-5.6, `params/core.md` Inspirations, and ED-773 Knot lifecycle as required reading.

---

**End refinement.**
