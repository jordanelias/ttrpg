# Significance Function and Omniscient Voice

**Subject:** Refinement to the three-tier articulation model (`2026-04-30_three_tier_articulation_reframe.md`).
**Trigger:** Two corrections from Jordan:
  (1) The architecture is **present-moment play + year-end omniscient retrospective.** Lock this in as the canonical framing.
  (2) Prior doc named "actors" but didn't mechanize **what makes someone prominent**. The Bill Clinton affair vs neighborhood affair distinction is real and load-bearing.
**Date:** 2026-04-30
**Status:** Refinement; integrates into PP-688 spec.

---

## §0 The Locked Framing

> *Play happens in the present moment, with all the ambiguity and partial information of being inside an unfolding event. The year-end Accounting is an omniscient retrospective — a chronicler's voice articulating what happened, with knowledge the protagonist couldn't have had at the time.*

This is the canonical framing for the articulation layer. Two voices:

| Voice | When | Epistemic frame |
|---|---|---|
| **Present-moment voice** | Tier 1 (default UI) and Tier 2 (trigger cut scenes) | Protagonist's POV; only what *they* could observe; ambiguity preserved |
| **Omniscient retrospective voice** | Tier 3 (year-end chronicle cut scene) | Chronicler's POV; sees inside all factions; attributes motives the protagonist couldn't know; frames events with consequences known |

The omniscience is a **feature**, not a slip. Real chronicles are written after the fact with information unavailable to participants at the time. Compagni knew Dante's 1302 exile was significant only because he wrote in hindsight. Villani similarly. The Tier 3 chronicle should have this property: it knows what mattered, it knows what was hidden at the time, it knows whose actions caused which outcomes.

This is also period-correct narrative practice. *Cronache* are deliberately retrospective and deliberately omniscient.

---

## §1 The Significance Function

Not every Key warrants a cut scene; not every event makes the chronicle. The factors you named — *prominence, stakes, public expectation/judgment, public awareness* — together form a **significance function** that the engine computes per Key.

### §1.1 The four factors

| Factor | What it captures | Substrate fields used |
|---|---|---|
| **Prominence** | Who is involved; their position; cumulative narrative weight | `source_actor.standing`, `target.standing`, faction role, leader status, prior cut-scene appearances |
| **Stakes / extent** | How much is changed; magnitude of consequence | `impact_vector` magnitude, `stat_deltas` magnitude, `permanence`, `scale_signature`, downstream L/PS delta |
| **Public expectation / judgment** | How the action lands against role-expectation; the moral/political weight | Cascade Fidelity divergence, Mission alignment/contradiction, Self-Other orientation of source, Public Expectation strictness modulation |
| **Public awareness** | How widely the event is known; how observable it is | `visibility` field (public/semi-public/private), observer set size, downstream Key references back to this Key |

### §1.2 Significance score formula

For each Key, compute:

```
significance(key) = 
    w_p × prominence(key)
  + w_s × stakes(key)
  + w_e × expectation_weight(key)
  + w_a × awareness(key)
```

Each component scaled to [0, 1]:

```python
prominence(key) = clamp(
    0.5 * normalize(max(source_actor.standing, max(t.standing for t in targets)) / 7)
  + 0.3 * (1.0 if source_actor.is_faction_leader else 0.5 if source_actor.standing >= 5 else 0.2)
  + 0.2 * cumulative_appearance_weight(actor)
  , 0, 1)

stakes(key) = clamp(
    0.4 * vector_magnitude(impact_vector) / max_impact
  + 0.3 * permanence_score(key.permanence)   # transient=0, persistent=0.6, indelible=1.0
  + 0.2 * scale_score(key.scale_signature)   # personal=0.25, settlement=0.5, territory=0.75, peninsula=1.0
  + 0.1 * num_affected_factions / total_factions
  , 0, 1)

expectation_weight(key) = clamp(
    0.5 * abs(cascade_fidelity_divergence_caused)   # how strongly does this challenge role expectation
  + 0.3 * mission_alignment_magnitude               # ±1 → 1, 0 → 0
  + 0.2 * abs(self_other_orientation_of_source - 0)  # self-serving or self-sacrificing both register as significant
  , 0, 1)

awareness(key) = clamp(
    1.0 if key.visibility.public else
    0.6 if len(key.visibility.semi_public) >= 5 else
    0.4 if len(key.visibility.semi_public) >= 2 else
    0.2 if len(key.visibility.private) >= 2 else
    0.0
  , 0, 1)
```

Default weights `w_p = w_s = w_e = w_a = 0.25`. Tunable per scenario.

### §1.3 Worked examples

| Event | Prom | Stakes | Expect | Aware | Total |
|---|---|---|---|---|---|
| **Bar brawl, 2 commoners, witnessed by 4 patrons** | 0.20 (s=2 each) | 0.15 (transient, personal scale) | 0.05 | 0.40 (semi-public 4) | **0.20** |
| **Neighborhood affair, 2 mid-standing NPCs, semi-public** | 0.35 (s=4 each) | 0.40 (persistent, personal+settlement) | 0.55 (Cascade-level if leadership; Self-Other tilt high) | 0.40 | **0.43** |
| **Faction leader's affair exposed publicly** | 0.85 (leader, faction-prominent) | 0.70 (persistent, multi-scale L/PS impact) | 0.85 (high Cascade Fidelity divergence; Public Expectation breach) | 1.00 (public) | **0.85** |
| **Bar brawl, but one combatant is the Crown Captain** | 0.65 (s=4 + leader-adjacent) | 0.30 (still mostly transient but Cascade-relevant) | 0.50 (sovereign role expects dignity) | 0.40 | **0.46** |
| **Treaty signed between two faction leaders** | 0.90 | 0.80 (indelible, peninsula-scale) | 0.40 (Mission-aligned, expected role action) | 1.00 | **0.78** |
| **Peninsula-scale strain shock from harvest failure** | 0.30 (no actor) | 0.95 (peninsula scale, persistent, multi-faction) | 0.30 | 1.00 | **0.64** |
| **Conviction Scar acquired by Crown Captain after witnessing atrocity** | 0.70 | 0.65 (indelible, personal-cascade-relevant) | 0.60 | 0.40 | **0.59** |

These match intuition. The bar brawl is low-significance; the same brawl with a Crown Captain involved is medium-high; an exposed leader affair is very high. **The same event-type can have very different significance depending on the prominence of who's involved** — exactly the Clinton-vs-neighborhood distinction.

### §1.4 Two scoring tracks: universal vs protagonist

The above is **universal significance** — would this matter to anyone observing?

A second score, **protagonist significance**, weights by relevance to the player's character:

```python
protagonist_significance(key, protagonist) = clamp(
    0.4 * is_in_observer_set(key, protagonist)   # 1 if protagonist observed
  + 0.2 * disposition_magnitude_to_actors(protagonist, key.source_actor + key.targets)
  + 0.2 * is_protagonist_faction_involved(key, protagonist)
  + 0.2 * cumulative_memory_overlap(key, protagonist)  # do they have prior Memory of these actors
  , 0, 1)
```

A neighborhood affair involving the protagonist's neighbors scores low universally (~0.3) but can score high protagonist-locally (~0.7) — and *that* is when it deserves a cut scene for the player. Conversely, a peninsula-distant treaty between two unfamiliar factions scores high universally (~0.78) but low protagonist-locally (~0.2) — and gets a passing mention rather than a cut scene.

### §1.5 What significance gates

| Tier | Gate | Threshold |
|---|---|---|
| **Tier 2 trigger cut scene fires** | `max(universal_sig, protagonist_sig × 1.2) >= 0.55` | tunable |
| **Tier 3 chronicle inclusion (named event)** | `universal_sig >= 0.50` OR `protagonist_sig >= 0.65` | tunable |
| **Tier 3 chronicle prominent placement** | `universal_sig >= 0.70` OR `protagonist_sig >= 0.80` | tunable |
| **Cumulative-prominence weight bump** | Repeat appearance in 3+ prior cut scenes adds 0.15 to prominence permanently | for tracked actors |

The 1.2x weighting on protagonist_sig is intentional: events that matter to the player's character should crack the threshold even when they wouldn't be universally significant. The neighborhood affair gets a cut scene if it's *the player's* neighborhood affair.

---

## §2 Mechanizing "Prominence" (the gap I left)

The prior doc said "named figures" — that wasn't enough. Mechanically, prominence is composed of:

### §2.1 Static prominence (authored / inherent)

- **Standing** (1-7 scale already exists). Standing 7 = sovereign, archbishop, etc.; 1 = anonymous commoner. This is the baseline.
- **Faction role**. Leader of a faction = high prominence regardless of Standing. Generic captain = mid-tier. Anonymous clerk = low.
- **Title / office**. Some roles carry prominence beyond Standing (e.g., a low-Standing inquisitor in an ecclesiastical context).

This is the *structural* prominence. It changes only when characters change roles.

### §2.2 Dynamic prominence (substrate-tracked)

- **Cut-scene appearance count**. Each time a character appears in a Tier 2 cut scene, their cumulative narrative weight increases. By season 6, characters who have been triggered repeatedly become *familiar to the player* and trigger more readily.
- **Disposition density**. Characters with strong Disposition (positive or negative) to many other tracked characters become prominent through sociometric position.
- **Recent emission density**. Characters who have been source or target of many recent Keys are *currently active* in the campaign's attention — even if their structural prominence is moderate.

This is *narrative* prominence. It accumulates organically as the campaign runs.

### §2.3 Why both matter

A duke (high static prominence) who has been off-screen for 10 seasons (low dynamic prominence) is somewhat less narratively present than a captain (mid static) who has been at the center of every recent crisis (very high dynamic). The substrate should treat them comparably — not by lowering the duke but by raising the captain through accumulated narrative weight.

This produces the *narratively-elevated mid-tier character* — Almud the Crown Captain who, by the end of the campaign, has the cut-scene presence of a sovereign because she has been at the center of so many triggered events. **This is how protagonists are made narratively without being authored as protagonists.**

### §2.4 The protagonist-as-prominence boost

The player's character is automatically high-prominence regardless of Standing. This is a one-line override:

```python
prominence(key) += 0.3 if protagonist in (source_actor, targets) else 0
```

The protagonist is always narratively significant from their own viewpoint. This is what makes the player feel central without forcing the world to revolve around them mechanically.

---

## §3 Stakes — what was vague before, now explicit

I treated stakes loosely as "magnitude." More precisely, four sub-factors:

| Sub-factor | Captures |
|---|---|
| **Magnitude** | How big is the immediate impact (vector magnitude, stat_deltas) |
| **Permanence** | How long does it last (transient/persistent/indelible) |
| **Scale reach** | How far does it propagate (personal → peninsula) |
| **Multiplicity** | How many parties are affected |

A bar brawl is high-magnitude *immediately* but transient and personal-scale → low stakes. A treaty signing is moderate-magnitude immediately but indelible, peninsula-scale, multi-faction → high stakes. The four sub-factors prevent magnitude alone from over-weighting brief but flashy events.

---

## §4 Public Expectation / Judgment — the moral-political weight

This is where Convictions and faction architecture earn their keep narratively. An action's significance partly depends on **how it lands against expectation**:

- A sovereign acting virtuously (Cascade Fidelity matches role): low expectation_weight (this is what's expected; not noteworthy)
- A sovereign acting against role expectation (Cascade Fidelity diverges): high expectation_weight (this is news)
- A Mission-contradicted action: high expectation_weight (this is wrong relative to stated purpose)
- An action with extreme Self-Other orientation (very selfless or very self-aggrandizing): high expectation_weight (this reads as significant of character)

This is exactly the "Bill Clinton affair was a scandal because expectations were violated" dynamic. A monarch's mistress in 14th-century Europe was structurally tolerated; a married monarch in 21st-century context with hyper-active Public Expectation is a scandal. **The Convictions/Public Expectation system gives the substrate a moral-political compass that significance scoring reads from.**

---

## §5 Public Awareness — the spread

Significance is partly a function of how widely something is known:

- A private event between two NPCs: low awareness, even if high-stakes between them
- A semi-public event with witnesses: medium awareness
- A public event: high awareness
- An event referenced by subsequent Keys (re-referred to, gossiped about, brought up in council): rising awareness over time

The substrate already tracks visibility on emission. The "awareness rises through subsequent reference" pattern needs a small extension: **awareness can grow post-emission** if subsequent Keys reference this Key in their causes[]. A private betrayal becomes more known when subsequent public Keys cite it as cause.

```python
awareness(key, current_time) = base_awareness(key)
                              + 0.1 * count_subsequent_keys_with_key_as_cause(key, current_time)
                              [clamped at 1.0]
```

This produces the "the secret that became famous" pattern — high stakes initially private, then awareness grows through downstream references, eventually crossing significance threshold for cut scene or chronicle inclusion.

---

## §6 Worked Example: the Clinton vs Neighborhood Affair

To ground all this in your example:

**Bill Clinton affair (1998):**
- Prominence: 1.00 (head of state, leader of largest faction, established political prominence)
- Stakes: 0.80 (persistent, peninsula-scale L/PS impact, multi-faction realignment)
- Expectation weight: 0.95 (high Public Expectation strictness for sovereign role; major Cascade Fidelity divergence; high public-judgment temperament)
- Awareness: 1.00 (peninsula-public; subsequent Keys reference for years)
- **Significance: 0.94** → triggers cut scenes; chronicle prominently features.

**Neighborhood affair:**
- Prominence: 0.30-0.40 (mid-Standing locals; not faction leaders; low cumulative narrative weight)
- Stakes: 0.30-0.40 (persistent emotionally, but personal/settlement scale; low L/PS impact)
- Expectation weight: 0.30-0.50 (some Public Expectation involvement if devout community; low if pragmatic)
- Awareness: 0.40-0.60 (semi-public local; not peninsula)
- **Significance (universal): 0.32-0.48** → below cut scene threshold for general player, no chronicle prominence
- *But:* if protagonist is one of the participants, **protagonist_sig = 0.85+** → triggers cut scene for *that* player

**Same event-type (affair); different actors; different mechanical significance.** This is what your distinction was getting at, and the formula now produces it.

---

## §7 The Year-End Chronicle, with Significance Filtering

Tier 3 chronicle generation now reads from significance-scored Keys:

```python
def generate_year_chronicle(year, protagonist):
    candidates = []
    for key in keys_in_year(year):
        u_sig = universal_significance(key)
        p_sig = protagonist_significance(key, protagonist)
        causal_centrality = causal_graph_centrality(key)
        score = max(u_sig, p_sig * 1.2) + 0.2 * causal_centrality
        candidates.append((score, key))
    
    candidates.sort(reverse=True)
    
    # Top 8-15 candidates form the year's named events
    named_events = candidates[:12]
    
    # Plus state-divergence summaries (faction L/PS deltas, succession events)
    state_summaries = compute_year_state_changes(year, protagonist.faction)
    
    # Plus background trends (causal chains below threshold but interconnected)
    background_chains = identify_background_chains(year, threshold=0.4)
    
    return compose_chronicle_prose(named_events, state_summaries, background_chains)
```

The chronicle:

- Names the most significant events with prominence
- Notes state changes for the protagonist's faction and major peers
- Sketches background trends without naming them prominently
- Uses **omniscient voice**: attributes motives the protagonist couldn't have known; reveals private events that are now historically established; frames events with their consequences known

Sample updated chronicle (using Bill Clinton + Almud composite from earlier):

> **The Third Year**
>
> The year was overshadowed by the exposure of the Crown's Spymaster — though this would not become public until midsummer. From the spring, the eastern engagements proved indecisive, and Captain Almud, newly elevated, found the realm's resources thinner than her predecessor had reported.
>
> By summer the betrayal was uncovered: years of covert action against the Lowenritter, undertaken on the Spymaster's own initiative and concealed even from the throne. The revelation cost the Crown more than the campaign had — Public Support across three provinces eroded measurably, and the Cathedral's quiet support began to drift.
>
> Almud's response, both restrained and visible, preserved what Legitimacy could be saved. By harvest, a new disposition had settled: the Crown was diminished but dignified, the Lowenritter watchful, the Cathedral hedged. The Restoration's voice, long marginal, grew louder.
>
> Three captains carried Conviction Scars from the year's losses. The peninsula's strain rose with the early winter.

Notice the omniscience: the narrator knows the betrayal was on the Spymaster's "own initiative and concealed even from the throne" — information the protagonist (if not the Spymaster themselves) could not have had at the time. This is the chronicler's voice, articulating what the substrate's CAUSAL_GRAPH and Key visibility actually contain, but unavailable to participants in the moment.

---

## §8 What This Adds to PP-688

PP-688 (Articulation Layer) now has three named subsystems:

1. **Tier 1 protagonist UI lens** (no new mechanics; UI work)
2. **Tier 2 trigger detection** (significance function + cut scene composition)
3. **Tier 3 chronicle generation** (significance + causal centrality + omniscient voice prose templates)

Plus one new substrate-piece needed:

4. **Cumulative narrative weight tracking** — per-actor cut-scene appearance counter, contributing to dynamic prominence. Small addition to actor schema.

Plus one substrate extension:

5. **Awareness post-emission update** — when a Key is referenced as cause by a subsequent Key, the original Key's awareness score increases. Small addition to Key emission rule.

The significance function itself is ~50 lines of code; the trigger threshold and chronicle composition algorithms are similar size. **Mechanically light; conceptually load-bearing.**

---

## §9 What This Resolves

| Concern | Resolution |
|---|---|
| Prior doc said "named figures" without mechanizing prominence | §1.1, §2 mechanize prominence as static + dynamic |
| Bar brawl vs Gulf War distinction | §1.3 worked examples show formula produces correct disparity |
| Bill Clinton vs neighborhood affair | §6 worked example shows it explicitly |
| Stakes was vague | §3 sub-factors explicit |
| Public expectation/judgment was hand-waved | §4 maps to Cascade Fidelity, Mission alignment, Self-Other orientation |
| Public awareness was binary (visibility flag only) | §5 adds post-emission awareness growth |
| When to fire cut scene was unspecified | §1.5 thresholds gates each tier |
| Chronicle inclusion criteria undefined | §7 uses significance + causal centrality |
| Omniscient voice unspecified | §0 locks framing; §7 sample chronicle demonstrates |

---

## §10 The Architectural Result

The architecture now articulates story through:

- **Present-moment ambiguity** in Tier 1 (protagonist's epistemic frame)
- **Significance-gated punctuation** in Tier 2 (events that cross the threshold get cut scenes; below-threshold events stay as background)
- **Year-end omniscient chronicle** in Tier 3 (significance + causal centrality + chronicler's voice)

The significance function is composed from four substrate-derived measures (prominence, stakes, expectation weight, awareness) in two tracks (universal, protagonist-relative). It produces the Clinton-vs-neighborhood distinction mechanically.

The omniscient voice in Tier 3 is a feature, not a slip. It lets the chronicle reveal what was hidden, attribute motives the protagonist couldn't have known, and frame events with their consequences clear. This matches Renaissance chronicle practice exactly.

**Player experience:**
- Daily play: muddy, partial, ambiguous (correct)
- Significant moments: punctuated, present-tense, what-they-witnessed (correct for that scale)
- Year-end: panoramic, retrospective, attributed-and-explained (correct for chronicle form)

The throughline is articulated annually by an omniscient chronicler from the substrate's events. The player navigates the present; the chronicler speaks for the past.

---

**End refinement.**
