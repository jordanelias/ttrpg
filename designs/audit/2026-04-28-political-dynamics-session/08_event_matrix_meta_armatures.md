<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: Event Impact Matrix and Multi-Scale Meta-Armatures -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# Event Context, Meta-Armatures, and Domain Action Integration

These three questions resolve into one architectural addition: the Event Impact Matrix as shared compute, with armatures operating at three scales (NPC, settlement, faction) and Domain Actions serving as the primary expression of political dynamics in the strategic layer.

---

## §1 The Event Impact Matrix

### 1.1 Concept

Currently, when a treaty fires, the armature receives "treaty_signed" as input plus a tagged dimension profile. The NPC interprets through their Conviction frame. But the *treaty itself* contains structured information that every NPC interpreting it could use: who gained what, who lost what, who was symbolically empowered, who was symbolically marginalized, what scale the consequences run at.

Currently each NPC computes this implicitly from their own perspective. With ~35 NPCs interpreting the same event, that's 35× redundant computation of facts that don't depend on the interpreter.

**The fix:** compute the event's impact structure once when the event fires; attach the structure to the event record; let every armature read the relevant rows.

### 1.2 Structure

When any event fires, the engine computes an Event Impact Matrix:

```
EventImpact:
  event_id
  event_type (treaty, promotion, Domain Action result, scar, death, etc.)
  source_actor (who caused it)
  
  material_effects[]:           # who gains/loses what tangibly
    actor_id
    type: {resource, position, capacity, territory}
    direction: {gain, loss, neutral}
    magnitude: 1-3
  
  symbolic_effects[]:           # who is empowered/marginalized symbolically
    actor_id (or faction_id)
    conviction_resonance: {aligned, neutral, contradicted}
    institutional_resonance: {empowered, neutral, threatened}
  
  relational_effects[]:         # how the event shifts existing relationships
    actor_pair: (actor_a, actor_b)
    direction: {convergent, divergent, asymmetric}
  
  scale_signature[]:            # what scales the consequences run at
    {personal, settlement, faction, peninsula}
  
  time_horizon: {immediate, near (1-3 seasons), far (4+ seasons)}
  
  visibility:                   # who can observe the event
    public: bool
    semi_public_observers[]: actor_ids
    private_observers[]: actor_ids
```

### 1.3 Computation cost

This is computed *once per event*. For most events, the affected actor list is small (5-15 NPCs). Material effects use existing stat deltas (already computed for the event's mechanical resolution). Symbolic resonance uses pre-built Conviction × Event-type alignment tables. Relational effects are derived from existing Disposition + RP data.

Per event compute: ~50-100 simple lookups. Negligible. The cost is paid once and consumed by every NPC armature interpreting the event, which is a net reduction from the current implicit-per-NPC computation.

### 1.4 What this enables for NPC armatures

Currently armature input is the event's dimension profile. With the Impact Matrix, armatures receive **specifically what the event did to whom**. The Concern an NPC generates can now reference concrete structure:

- *Without Matrix:* "Why did Almud sign the treaty?" → resolution via Conviction-weighted seeking-tags + general Memory
- *With Matrix:* "Why did Almud sign the treaty *that gave Varfell intelligence-sharing access while symbolically threatening Church doctrinal authority and divergently shifting the Crown-Hafenmark relationship*?" → resolution can target specific Memory entries about each component effect

Concerns become more specific. NPC reasoning becomes more legible. Player intelligence operations targeting "what NPC X believes about the treaty" can return structured information rather than vague summary.

### 1.5 Authoring overhead

The Impact Matrix is computed by the engine from existing data + a small alignment table:

- **Conviction × Event-type symbolic resonance table:** 7 Convictions × ~30 event types = 210 entries (each entry is one of: aligned, neutral, contradicted). Authorable in a single afternoon.
- **Material effect extraction:** read from event's existing mechanical resolution (Domain Action outcomes, treaty terms, etc.) — no new authoring.
- **Relational effect derivation:** computed from event participants and existing Disposition data — no new authoring.

Net new authoring: 210 alignment entries. Not 210 templates — single-cell ratings.

---

## §2 Meta-Armatures: Settlements and Factions

### 2.1 Why scale them

If only NPCs have armatures, then factions and settlements are passive aggregations. But factions and settlements *interpret* events at their own scale:

- The Crown court collectively interprets the Hafenmark amendment as either "constitutional overreach" or "legitimate parliamentary action" depending on the dominant Conviction in its inner circle and its institutional posture.
- A Crown-controlled settlement near the Varfell border collectively interprets a cultural exchange differently than a Crown-controlled settlement deep in the heartland.

These collective interpretations drive Domain Action proposals, Settlement Signal content, and faction-level reactions. They need explicit specification.

### 2.2 Settlement Meta-Armature

A settlement's interpretive frame is computed at Accounting from:

```
SettlementMetaArmature:
  governor_armature_weight: 0.4
    (the governor's Conviction frame dominates settlement-level interpretation)
  
  passive_npc_aggregate_weight: 0.3
    (lite-armatures of named Passive NPCs, weighted by their local Disposition with population)
  
  institutional_character_weight: 0.2
    (settlement type produces baseline interpretive bias:
     Cathedral → Faith bias; Market → Reason/Autonomy bias;
     Fortress → Order/Continuity bias; Outpost → Autonomy bias)
  
  population_disposition_weight: 0.1
    (statistical mean Disposition with controlling faction
     produces baseline acceptance/resistance bias)
```

When an event affects the settlement (e.g., a Domain Action targeting it, an external faction's diplomatic move), the Settlement Meta-Armature interprets the event and produces a settlement-level reaction:

- One Concern at the settlement level (becomes a Settlement Signal Concern propagating to controlling faction)
- One Mood at the settlement level (Steady/Anxious/Resolved/Confident — affects local NPC behaviors and future event interpretations)
- One Project shift if applicable (settlement may begin pursuing a community-level goal: defensive preparation, economic consolidation, religious revival)

This is computed once per affected settlement per event. Settlements without Active governors use the Passive NPC aggregate as primary, with institutional character as tiebreaker.

**Critical property:** if the governor's Conviction differs from the institutional character's bias, the settlement experiences Framework Tension (existing P-8 mechanism). The Meta-Armature makes this tension *interpretively visible*: the same event produces different settlement-level reactions depending on which weight dominates.

### 2.3 Faction Meta-Armature

A faction's interpretive frame is the inner-circle aggregate plus institutional inertia:

```
FactionMetaArmature:
  inner_circle_aggregate:
    weighted average of inner-circle Active NPC armatures
    weights by Standing (Standing 7: 1.0, Standing 6: 0.7, Standing 5: 0.5, Standing 4: 0.3)
    leader's armature weighted at 1.5× of their Standing weight
  
  institutional_inertia:
    bias toward maintaining existing Faction-level Concerns and Projects
    strength: 0.3 (significant but not dominant)
    declines as inner-circle Conviction Scars accumulate
    (a court with many Scarred NPCs has weakened institutional inertia)
  
  ethical_framework_anchor:
    fixed bias toward the faction's Ethical Framework
    strength: 0.2
    represents the faction's formal doctrine, distinct from inner-circle preferences
```

When a faction-level event fires, the Faction Meta-Armature interprets:
- Faction-level Concerns generate (separate from individual NPC Concerns; these are institutional-scale: "Is our diplomatic strategy still viable?")
- Faction-level Projects shift (institutional agendas)
- Domain Action proposals emerge (see §3)

**Key insight:** the leader's individual armature carries 1.5× weight but does not dominate. A Reformer-arc Almud (Conviction shifted to Reason) does not single-handedly shift Crown's institutional interpretation — the institutional inertia + Faith-aligned Confessor + Order-aligned Marshal still pull the Faction Meta-Armature toward Crown's traditional framework. This produces the historically realistic dynamic where reformer rulers find their courts resisting their personal transformations.

**Verifiable design property:** if the player joins the inner circle and reaches Standing 5+, their armature becomes part of the Faction Meta-Armature. The player's Conviction now influences the faction's institutional interpretation. This makes Standing advancement meaningful at the institutional level — the player isn't just gaining personal authority, they're becoming part of how the faction *sees* the world.

### 2.4 Computational additions

- Settlement Meta-Armature: 36 settlements × per-event interpretation (only when affected). Most events affect 0-3 settlements. ~3 computations per event × ~5 events per season = ~15 settlement-meta computations per Accounting. Negligible.
- Faction Meta-Armature: 7 factions × per-event interpretation. ~5 events per season × 7 factions = ~35 computations per Accounting. Each computation is a weighted average over ~6 inner-circle armatures. Cheap.

---

## §3 Domain Actions in the Armature System

Domain Actions are the most important political events in Valoria. They need explicit integration with armatures, both as event-sources and as outputs of inner political dynamics.

### 3.1 Domain Actions as event-sources

Every Domain Action that resolves (success, partial, failure) generates an Event Impact Matrix per §1. The Matrix entries:

- **Material effects:** the Domain Action's mechanical outcome (stat changes, territorial shifts, resource transfers). Already computed for existing systems.
- **Symbolic effects:** mapped from action type to Conviction resonance (e.g., Crown Royal Decree → Order resonance: aligned for Order-aligned NPCs, contradicted for Autonomy-aligned NPCs).
- **Relational effects:** Domain Actions that target specific other factions create rivalry/alliance shifts. Already partially modeled in faction stat changes.
- **Visibility:** Domain Actions are typically public unless covert (Niflhel-broker-style). Visible Domain Actions produce widespread interpretation; covert ones generate intelligence opportunities.

NPCs whose armatures interpret the Domain Action generate Concerns, Memories, and Opinion shifts. **Every Domain Action is a political event with consequences beyond its mechanical effect.**

### 3.2 Domain Actions as outputs of armature dynamics

This is the more important direction: Domain Actions don't just *get interpreted*, they *get proposed* by NPCs whose armatures and Projects make them want to.

**Proposal generation mechanism:**

At each Accounting, before the faction's AI priority tree selects Domain Actions, each inner-circle Active NPC evaluates:
1. Does my current Project benefit from a specific Domain Action?
2. Does my current high-salience Concern push for a specific Domain Action?
3. Does my Mood (Confident, Vindicated, Humiliated) favor specific Domain Action types?

Each NPC may propose up to one Domain Action per season. Proposals are evaluated by the faction's AI priority tree alongside automatic priority-driven actions.

**Example:** Marshal Ehrenwall, Project "train Torben to be a war-leader," season where Torben needs hands-on command experience. Ehrenwall proposes Crown Domain Action: "Send Torben to lead the eastern border patrol." This is a faction-level Domain Action with a specific NPC sponsor. Other inner-circle NPCs evaluate per their own armatures:

- Confessor (Faith, Anxious Mood from treaty): interprets through institutional-stability lens. "Is sending the heir to the border imprudent during these unstable times?" Generates obstruction (+1 Ob to the Domain Action).
- Cardinal Klapp (Reason, Confident Mood): interprets as developmental opportunity. Supports.
- Spymaster Kolbrun (Autonomy, Steady): interprets through risk lens. "Acceptable if the patrol is well-secured." Conditional support.

The faction's Domain Action proceeds with modifiers: +1 Ob from Confessor obstruction, +0 from Klapp's support (his Standing too low to provide bonus), +0 from Kolbrun's neutrality. Net effect: harder to succeed than if the inner-circle were unified.

### 3.3 Cross-armature Domain Action competition

When two NPCs propose conflicting Domain Actions in the same season, the faction's AI priority tree selects based on:
- Standing weight of each proposer (higher Standing = more weight)
- Alignment with faction's current top-priority Concern (if any)
- Faction Meta-Armature interpretation of which proposal best serves the faction's Conviction frame

The losing proposer's Project advancement stalls this season. The winner gets their Domain Action attempt. This produces realistic court dynamics where personal political success is partly about getting the prince to do what advances *your* Project rather than your rival's.

**Player intersection:** A player at Standing 3+ can also propose Domain Actions through this mechanism (existing system: Counselor rank can suggest Domain Actions, Lieutenant can issue sub-commands). The armature system makes the player's proposals subject to the same inner-circle competition. The player who wants their Domain Action to succeed must build Disposition with inner-circle NPCs whose armatures will support it — or whose Projects align with theirs.

### 3.4 Failed Domain Actions feed armature

A failed Domain Action generates Event Impact Matrix entries:
- Material effects: stat losses (existing PP-403)
- Symbolic effects: the proposing faction is symbolically weakened in the action's domain
- Relational effects: depends on what failed and why

NPCs interpret per armatures. Proposing NPC's Concerns generate ("Why did this fail? Was it sabotage? Bad timing? Wrong approach?"). Opposing NPCs may have Vindicated Mood. The Domain Action's failure becomes ammunition in subsequent court politics.

**The Confessor whose obstruction added the +1 Ob that pushed the Marshal's Domain Action from success to partial:** he gains Memory of his own effective opposition. His Opinion of the Marshal updates. His next Domain Action proposal is less likely to be supported by the Marshal in turn. The faction develops chains of grudges through this mechanism.

---

## §4 Synthesis: How These Three Pieces Work Together

The Event Impact Matrix, meta-armatures at three scales, and Domain Action integration form a coherent architecture:

1. **Event fires** (Domain Action resolution, treaty signing, NPC death, etc.). Engine computes Event Impact Matrix once.

2. **Three scales of interpretation read the Matrix:**
   - Individual NPC armatures generate Concerns, Memories, Opinion shifts
   - Affected Settlement Meta-Armatures generate settlement-level reactions
   - Affected Faction Meta-Armatures generate faction-level Concerns/Projects

3. **Interpretations drive subsequent proposals:**
   - NPCs propose Domain Actions advancing their Projects or addressing their Concerns
   - Settlements generate Settlement Signals propagating to controlling factions
   - Factions develop institutional Concerns that shape their AI priority trees

4. **Inner-circle competition resolves proposed Domain Actions:**
   - Multiple proposals evaluated per Faction Meta-Armature
   - Winning proposal proceeds (with armature-induced Ob modifiers from supporters/opposers)
   - Losing proposers face stalled Projects and accumulated grievances

5. **Domain Action resolves**, generating new Event Impact Matrix. Cycle continues.

**This is the political loop.** Events produce interpretations; interpretations drive proposals; proposals compete; outcomes produce new events. The player participates in this loop at multiple scales simultaneously: their personal social engagements (which build Disposition with inner-circle NPCs), their Standing-based proposal authority (which lets them inject Domain Actions into the competition), their settlement governance (which affects Settlement Meta-Armatures), their long-term faction trajectory (which can shift the Faction Meta-Armature if they reach Standing 5+).

---

## §5 Computational Honesty

Per-Accounting cost estimate (revised):

| Operation | Count | Per-op cost |
|---|---|---|
| Event Impact Matrix computation | ~5 events | ~100 lookups each |
| NPC armature interpretation (35 Active) | per affected event | ~50 lookups |
| Settlement Meta-Armature interpretation | ~3-5 settlements per event | weighted average |
| Faction Meta-Armature interpretation | ~7 factions per event | weighted average |
| Domain Action proposal generation | up to 1 per Active NPC | ~30 lookups |
| Inner-circle competition resolution | per proposal pair | comparison |

This is honest about what computation is required but does not commit to ms estimates. Profile in implementation.

The architectural addition (Event Impact Matrix as shared compute) actually *reduces* total computation versus per-NPC implicit computation. The meta-armatures add ~10% overhead. The Domain Action proposal generation adds modest new work but replaces the existing AI priority tree's blind selection with armature-informed selection.

**Net assessment:** more work than the previous specification, but the work scales linearly with NPC count and event count — both of which are bounded.

---

## §6 New Authoring Obligations

In addition to existing armature authoring (~370 entries):

| New item | Count | Notes |
|---|---|---|
| Conviction × Event-type symbolic resonance table | 210 | Single-cell ratings (aligned/neutral/contradicted) |
| Settlement institutional character bias | 6 | One bias profile per settlement type |
| Faction ethical framework anchor weights | 7 | Already exists in Conviction system; just formalize |
| Domain Action sponsor mapping | ~30 | Which inner-circle NPC roles can propose which Domain Action types per faction |

Total new authoring: ~250 entries, mostly single-cell ratings.

**Combined total authoring (armature + this addition):** ~620 entries. Still less than the 630 templates the original library would have required, with much greater behavioral capacity.

---

## §7 Verdict

Three answers to three questions:

**Yes, cheaply compute event context as input matrix.** The Event Impact Matrix is computed once per event from existing data + small alignment table. Cost is negligible; it actually reduces total computation by replacing redundant per-NPC implicit computation with shared structured data. NPC armatures consume the matrix as enriched input, producing more specific Concerns and more legible reasoning.

**Yes, factions and settlements have meta-armatures.** Settlement Meta-Armature is a weighted aggregate of governor armature + Passive NPC armatures + institutional character + population baseline. Faction Meta-Armature is weighted aggregate of inner-circle armatures (Standing-weighted, leader-amplified) + institutional inertia + ethical framework anchor. Both interpret events at their scale and produce scale-appropriate outputs (Settlement Signals; faction Concerns and Projects).

**Domain Actions are the primary expression of political dynamics in the strategic layer.** They are both event-sources (interpreted by armatures across scales) and outputs of armature-driven NPC and faction Projects. Inner-circle NPCs propose Domain Actions advancing their Projects; competing proposals are resolved by Faction Meta-Armature; Ob modifiers from inner-circle support/opposition determine whether the action succeeds. This is how the personal-scale armature dynamics become strategic-scale consequences.

The three additions integrate cleanly with the existing armature system, add modest authoring (250 entries), reduce per-event redundant computation, and complete the architecture for political dynamics across all three Valoria scales.
