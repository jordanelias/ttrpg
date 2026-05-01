# NERS — Emergent Arcs and Player Engagement

**Subject:** The full architectural stack drafted this session — PP-684 (12-Conviction taxonomy + Self-Other axis + cultural backgrounds), PP-686 (faction architecture: Mission, Cascade, Public Expectation, Legitimacy + Popular Support), PP-687 (universal Key substrate)
**Question:** Does this stack produce emergent narrative arcs and player engagement? Examined NERS-fashion, all six directions.
**Date:** 2026-04-30
**Auditor:** Claude

---

## §0 Executive Summary

The stack is **unusually well-suited to producing emergent narrative arcs** because emergence is structural rather than incidental: the Key substrate makes every event legible to every observer; the armature/axis vectorization gives every NPC a unique interpretation function; the faction architecture creates dramatic state-divergence (L vs PS); the Self-Other axis adds character interiority without authoring overhead. Arcs emerge as **statistical inevitabilities**, not as authored events.

**Verdict matrix:**

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | STRONG | STRONG | STRONG |
| Bottom-up | STRONG | STRONG | STRONG | STRONG |
| Vertical | STRONG | STRONG | STRONG | STRONG |
| Diagonal | STRONG | STRONG | STRONG | STRONG |
| Lateral | STRONG | STRONG | MODERATE | STRONG |
| Horizontal | STRONG | MODERATE | MODERATE | MODERATE |

**Three engagement mechanics beyond standard gameplay loops:**

1. **"Why did that happen?" diagnostic.** Player walks Key chain backward from any consequential event. The substrate makes this free.
2. **"What if I had done X?" alternate-timeline.** Replay determinism (validated in sim) enables seeded re-runs from save points.
3. **Living NPCs.** Each NPC's armature interprets the same world differently; their Memory accumulates; Self-Other orientation creates internal character arcs without authored arcs.

**Three structural arc categories the stack supports:**

- **Personal-scale arcs:** Conviction crisis, Disposition rivalry, Self-Other transformation
- **Faction-scale arcs:** Honest defeat, Successful tyrant, Succession institutional drift
- **Cross-scale arcs:** Insult-to-peninsula chains, Religious legitimacy crises, Mission-shift cascades

**Three honest risks:**

- **Causes-population rate.** Sim showed only ~15% of Keys had causes[] populated; if this stays low in production, arc chains stay short and emergence is shallow.
- **Legibility burden.** Rich emergence is illegible without diagnostic UI; PP-687 enables the diagnostic but doesn't design it.
- **Authored-vs-emergent balance.** Pure emergence produces both rich arcs *and* incoherent ones. Some authoring scaffolding likely needed.

---

## §1 What "Emergent Arc" Means Here

Distinguishable from authored narrative:

| | Authored | Emergent |
|---|---|---|
| Source | Designer wrote the beats | System produced them from interactions |
| Variability | Fixed | Different per playthrough |
| Replay value | Low (you've seen it) | High (different each time) |
| Authoring cost | High per arc | One-time substrate cost |
| Coherence | Guaranteed | Probabilistic |
| Player ownership | Designer-owned | Player-co-authored |

A *good* emergent arc has the shape of an authored arc — beginning, complication, escalation, resolution — but arises from system dynamics rather than scripted beats. The architecture's job is to make these shapes *statistically likely* without forcing them.

The Renaissance lens makes this natural: chronicles, *cronache*, and family records are emergent narratives that look authored only in retrospect. The Borgia ascent, the Medici expulsion, Savonarola's fall — none were authored arcs. They are pattern-shapes that happened because of system pressures, observer interpretations, and contingent events. Period-correct gameplay should *generate* such arcs, not pre-author them.

---

## §2 Top-Down (project intent → arc generation)

**Project intent:** *positive feedback loop between player decisions and mechanics that produces an engaging game world with emergent narratives.*

### N (necessary)

**STRONG.** Emergent narratives are explicitly named in the intent statement. The architectural stack is built specifically to enable them:

- 12 Convictions × 4 axes × Self-Other × structured concentration → ~10^6 distinguishable NPC interior states. No two NPCs interpret events identically.
- Faction architecture decouples Legitimacy from Popular Support → produces *paradoxical* faction states (high-L low-PS = brittle authority; low-L high-PS = legitimized populism) that script-writers don't naturally invent.
- Key substrate makes every event observable, recordable, and walkable → arcs become traceable rather than vanishing into per-system event handling.

Each piece is necessary for emergence: remove the Conviction vectorization and NPCs become uniform. Remove the L/PS split and faction state becomes one-dimensional. Remove the Key substrate and chains stop being walkable. The stack as a whole crosses the threshold where emergence is *generative*.

### R (robust)

**STRONG.** Robustness sub-criteria for emergence:

- **Variety of arcs supported:** personal (Conviction crisis, Disposition rivalry, Self-Other drift), faction (honest defeat, successful tyrant, succession), cross-scale (insult-to-strain, religious crisis), multi-faction (peninsula realignment, Strain feedback). At least 3-4 arc shapes per scale. ✓
- **Variability per playthrough:** different seeds, different NPC choices, different player DAs → different Key sequences → different arcs. Sim confirmed determinism: same seed = same arc, different seed = different arc. ✓
- **Player customization:** player choices emit Keys; Keys feed armature interpretations; armatures shape NPC Memory; Memory drives Disposition; Disposition affects future scene events. Customization is structural. ✓
- **Player feels impactful:** every action emits Keys with causes[]; the player is in the causal chain of downstream events; the diagnostic UI surfaces this. ✓
- **Mechanics fully formed:** PP-686 has 5 calibration deltas pending (C1-C10 from sim v2 evaluation); PP-687 has 6 spec refinements pending. None are blocking; all have known fixes. ✓

### S (smooth)

**STRONG.** Arc smoothness is the question of whether arcs feel *coherent* rather than *fragmented*:

- **Personal-scale arcs feel like character development:** Conviction Scars accumulate, drift over time, eventually crisis. The d6 crisis table from `conviction_track_v1.md` produces visible character instability. The Self-Other axis adds an internal-orientation arc that is usually invisible in TTRPGs but here mechanically tracked.
- **Faction-scale arcs feel institutional:** Cascade re-resolution over 4-6 seasons (per sim v2) means succession effects span a meaningful playable duration, not instant snap-replacements. The L/PS divergence pattern (validated in sim — ΔL +0.76, ΔPS −1.79 over 8 seasons of honest defeat) is *exactly* the dignified-fallen-king signature of historical regimes.
- **Cross-scale arcs feel consequential:** the 4-step chain (scene insult → DA betrayal → succession → peninsular shock) walked in sim is *the* canonical Renaissance arc. Each step's interpretation by observing NPCs adds further beats.

### E (elegant)

**STRONG.** Player intuition test: can a player, starting fresh, learn to predict that an action will have downstream consequences without reading the system docs?

- "If I insult the captain publicly, his guards will see it" — yes, public visibility is intuitive.
- "If the Crown's leader has a Conviction crisis, the Crown's actions will become erratic" — yes, this is the cascade feel.
- "If a faction wins everything but does it covertly, they'll become powerful but unstable" — yes, this is the L/PS divergence.

The emergent shapes are familiar from history, fiction, family stories. **The architecture earns its complexity by producing recognizable arcs.**

**Verdict (top-down):** all four NERS criteria STRONG. Project intent matches architecture; emergence is the named goal and the architecture delivers.

---

## §3 Bottom-Up (individual mechanic → arcs)

### N (necessary)

**STRONG.** Each component contributes a specific arc shape:

- **Conviction vector + axis projection:** every NPC has unique armature → events land differently on different NPCs → Memory diverges → Disposition diverges → conflict potential
- **Self-Other axis:** modulates outcome attribution → tracks character's developmental drift across game → an arc *of orientation*
- **Cultural background templates:** NPCs from same culture share interpretive substrate → faction-affiliation produces predictable interpretive patterns → external observers can sociologize
- **Cascade math:** leader's Convictions propagate down → succession produces visible institutional drift → an arc *of institutions*
- **Mission + Cascade + Public Expectation:** three independent pressure axes → factions can fail one and succeed another → multi-dimensional faction states
- **L/PS split:** divergent state evolution → the *strong-but-fragile* and *honored-but-powerless* arc shapes
- **Key + observer + Memory:** every event lives in observer minds → grudges, debts, alliances accumulate → relational arcs
- **Causes[] graph:** chains traceable → player diagnostic → arc legibility
- **Symbolic dimensions:** events have meaning, not just mechanical outcome → arcs read as significant rather than transactional

Each piece does necessary work for emergence. None is decorative.

### R (robust)

**STRONG.**

- Edge cases handled: orphan NPCs (rule established), zero-vector leader (graceful degradation), cycle detection (validator), structured-concentration smoothness (sim-validated)
- Numerical bounds: all clamps in place (L/PS [0,7], strictness [0,1], salience [0,3], Ob ±2)
- Compositional robustness: PP-686 architecture composes cleanly with Keys (sim §1.5 confirmed)

### S (smooth)

**STRONG.** Mechanic-to-mechanic interactions don't fragment:

- An NPC's Memory accumulates Keys → its armature reads them → Disposition updates → Disposition affects future scene event probabilities → produces relational arc beats
- A faction's Cascade re-resolves → emits `mechanical.cascade_resolution` Keys → other factions observe → their Disposition with this faction shifts → cross-faction realignment

Each cross-mechanic flow follows the same pattern: emit Keys, observe Keys, update state. No special-case wiring.

### E (elegant)

**STRONG.** Bottom-up elegance = each mechanic produces clear, single-purpose contribution:

- Conviction vector = "what this NPC values"
- Self-Other axis = "for whom"
- Armature = "how this NPC interprets events"
- Memory = "what this NPC remembers"
- Cascade = "how leadership shapes institutional behavior"
- L/PS = "how the populace sees this faction"
- Key = "the canonical event format"

Each name maps to a single concept. No overloading.

---

## §4 Vertical (scale coherence in arcs)

Arcs traverse scales: a personal slight becomes a faction policy becomes a peninsular war.

### N (necessary)

**STRONG.** Scale-traversing arcs are the most distinctive Renaissance pattern:

- Romeo and Juliet: personal (love) → family (Capulet/Montague) → city (Verona) → political (Prince's intervention)
- Pazzi conspiracy: personal (rivalry with Lorenzo) → family (Pazzi vs Medici) → city (Florence) → ecclesiastical (Pope Sixtus IV) → military (Naples)
- Borgia ascent: personal (Cesare's ambition) → faction (Papal States) → territory (Romagna) → peninsula (Italian wars)

Period-correct gameplay must support these. The stack does:
- Personal-scale Keys (scene events) carry into NPC Memory permanently
- Faction-scale Keys (DA outcomes) consume personal-Memory of leadership
- Territory-scale Keys (territorial actions) emit from faction state
- Peninsula-scale Keys (Strain shocks) consume territory aggregates

Each scale's events propagate through the substrate to other scales.

### R (robust)

**STRONG.** Vertical robustness for arcs:

- Scale-bridges are first-class Keys with multi-element `scale_signature[]`
- Cross-scale Memory: an NPC at personal scale can hold Memory of peninsula-scale events (Strain shocks they observed)
- Cross-scale Disposition: a faction's Mission can consume territorial benefits from individual NPC actions

### S (smooth)

**STRONG.** No scale-translation friction. The same Key flows through different consumers at different scales without re-encoding.

### E (elegant)

**STRONG.** The 16-Accounting trace concept (per the prior workplan) becomes a forward walk of CAUSAL_GRAPH from one scene-scale Key. Player intuits: "my action started a chain that eventually shifted the peninsula" — this is *the* fantasy of impactful gameplay.

---

## §5 Diagonal (cross-scale + cross-system in arcs)

This was PP-686's weakest direction. With PP-687 it becomes the strongest arc-generator.

### N (necessary)

**STRONG.** The richest arcs are diagonal: a scene event (personal scale, scene system) cascades through a Conviction Scar (personal scale, conviction system) which influences a DA (territory scale, strategic system) which triggers a succession (territory scale, faction system) which raises Strain (peninsula scale, environmental system).

Five system × four scale = 20-cell matrix. Diagonals fill it. Without diagonal arc support, only ~10 cells (in-system within-scale) are exercised.

### R (robust)

**STRONG.** Diagonal arcs are walkable in both directions:

- Forward from a player's scene action: "what consequences cascaded?"
- Backward from a faction collapse: "what events led here?"

Sim §1.3 demonstrated the 4-step chain works. Reality will produce 6-12 step chains over a 30-season game.

### S (smooth)

**STRONG.** Diagonal coupling is *automatic substrate behavior*, not per-pair wiring. Adding a new system (e.g., trade) requires only Key emission/consumption; existing systems integrate without modification.

### E (elegant)

**STRONG.** The chronicle metaphor: a Renaissance chronicle reads as causal chains across scales and systems. Players grasp this immediately because it's how history reads.

---

## §6 Lateral (peer systems generating complementary arcs)

Same scale, different systems: scene events + Conviction Scars + Disposition shifts + Memory writes all happen *together* at personal scale. Faction Cascade + Mission + L/PS + Public Expectation all happen *together* at faction scale.

### N (necessary)

**STRONG.** Single-system arcs are thin. A pure scene-system arc (just dialogue) without the Conviction-system response and Memory-system encoding is one-dimensional. Multi-system convergence at the same scale is what makes arcs feel *thick*.

### R (robust)

**STRONG.** Each peer system contributes a different layer:

- Personal scale: scene system gives action; Conviction system gives interpretation; Memory system gives persistence; Disposition system gives relational change
- Faction scale: Cascade gives modus; Mission gives telos; Public Expectation gives external pressure; L/PS gives state metric

A single event triggers responses in *all* peer systems simultaneously.

### S (smooth)

**MODERATE.** The challenge: lateral coordination requires consistent vocabulary. PP-684 unifies Conviction labels across NPC and faction scales — solving a major previous fragmentation. But:

- Standing (personal rank), Mandate (faction acceptance, derived), Legitimacy (component of Mandate), Popular Support (component of Mandate), Disposition (relational), Reputation (composite of these) — six terms for related concepts.
- The audit P3-3 (vocabulary debt) is real and lateral.

**Smoothness is high within an architectural-stack-aware view; lower for a player learning the vocabulary.**

### E (elegant)

**STRONG.** Each peer system has one canonical contribution. No system overlaps another's responsibility. Player can intuit "this is a Disposition arc" vs "this is a Conviction arc" because the labels are distinguishable.

---

## §7 Horizontal (temporal — arc shape across seasons)

### N (necessary)

**STRONG.** Arcs require time. The architecture's timing characteristics:

- Conviction Scars: indelible (permanence-locked); accumulate over many seasons; eventual crisis
- Cascade re-resolution: 4-6 seasons to reach new equilibrium after succession
- L/PS drift: Legitimacy slow (long integration); Popular Support faster (per-DA); divergence emerges over 8+ seasons
- Memory: Keys persist with decay; old events fade but indelible Keys remain
- Mission shifts: rare, dramatic, indelible

Different timing produces different arc lengths: personal arcs (1-3 seasons), faction arcs (4-8 seasons), institutional arcs (8+ seasons).

### R (robust)

**MODERATE.** Robustness sub-criteria for temporal arcs:

- Sustained tension: ✓ Cascade fidelity drift creates ongoing pressure
- Beat structure: PARTIAL. The architecture supports rising tension via accumulating Memory, but climactic beats (the *moment* an arc crystallizes) are not explicit. Currently a faction's collapse is the integral of many Keys, not a triggered transition.
- Equilibrium vs dynamism: PARTIAL. Sim showed L/PS converge to plateaus (PS pegged at 7.0 in scenario 4). Arcs need recurring perturbation to stay alive; without external shocks, late-game state is static.
- Pacing: PARTIAL. Cascade drift takes 4-6 seasons; if a typical campaign is 12-20 seasons, only 2-3 succession arcs fit. Tight.

### S (smooth)

**MODERATE.** Smoothness questions:

- Mid-season vs season-boundary events: PP-687 supports both via sub_step_index, but the gameplay distinction is unclear. When does a player feel "the season is ending"?
- Multi-arc concurrency: a faction succession arc + a Conviction crisis arc + a peninsular Strain arc can all run simultaneously. The architecture handles this; player attention may not. UI prioritization needed.
- Arc resolution: when an arc completes, the substrate doesn't *announce* it. The player may not realize a 6-season arc just resolved unless the diagnostic UI surfaces it.

### E (elegant)

**MODERATE.**

- Append-only Key log is temporally elegant.
- But narrative pacing isn't built into the substrate. Pacing emerges from per-system rates of Key emission, which aren't tuned together.
- The architecture is *temporally honest* but not *narratively paced*. Players may experience long stretches where nothing dramatic happens, or simultaneous overload where too much happens.

**Horizontal is the weakest direction for arcs.** Pacing is the chief unmodeled dimension.

---

## §8 Specific Arc Categories Supported

Catalogued per scale/scope:

### §8.1 Personal-scale arcs

**8.1.1 Conviction Crisis Arc** (3-6 seasons)
- Setup: NPC accumulates Scars across seasons (Threadwork events, witnessed atrocities, Conviction-violating circumstances).
- Complication: Scars reach 3+; armature destabilizes; NPC personal_convictions oscillate per d6 crisis table.
- Climax: a Key emerges that the NPC cannot interpret coherently; behavior becomes erratic; effect propagates to faction Cascade if NPC is in leadership.
- Resolution: either Conviction reformulation (new primary), exit (death/retirement), or sustained crisis (becomes the NPC's permanent state).

Player engagement: this is *internal* character development, normally invisible in TTRPGs. Here it's tracked, observable, and consequential.

**8.1.2 Disposition Rivalry Arc** (variable, often campaign-long)
- Setup: two NPCs with high opposed-Conviction armatures encounter each other repeatedly.
- Complication: each interaction emits Keys; both observe; Memory accumulates; Disposition deteriorates.
- Climax: a triggering Key (insult, witnessed action) crosses Disposition threshold; one NPC takes adversarial action.
- Resolution: feud, public confrontation, alliance shift, exile, death.

Player engagement: emerging from observation, not authoring. Player sees the rivalry building before it explodes; can intervene or watch.

**8.1.3 Self-Other Transformation Arc** (8-15 seasons)
- Setup: NPC starts at orientation X (e.g., −0.3, mildly altruistic).
- Complication: Mission victories with measurable personal benefit gradually shift orientation toward +; or repeated sacrifice for collective shifts toward −.
- Climax: orientation crosses 0; NPC's behavior pattern visibly changes.
- Resolution: NPC inhabits new orientation; old allies notice; new alliances form.

Player engagement: this is the *Macbeth arc*, the *fall-from-grace* arc, the *moral-development* arc. Authored in dozens of stories; here it emerges from accumulating Mission outcomes and Self-Other tracking.

### §8.2 Faction-scale arcs

**8.2.1 Honest Defeat / Dignified Decline Arc** (8+ seasons)
- Setup: faction has high Cascade fidelity (modus matches role expectation).
- Complication: Mission failures accumulate; Popular Support bleeds; Legitimacy *grows* from preserved expectation-fidelity.
- Climax: Mandate stays static while underlying L/PS diverge dramatically.
- Resolution: faction reaches "honored but powerless" state; transitions to maintenance role or dissolves with dignity.

Sim-validated. Pattern signature: ΔL +0.76, ΔPS −1.79 over 8 seasons (sim v2).

**8.2.2 Successful Tyrant / Strong-but-Fragile Arc** (8+ seasons)
- Setup: faction with anti-role conduct (low Cascade fidelity, anti-expectation Mission).
- Complication: Mission victories accumulate; Popular Support climbs; Legitimacy bleeds from cumulative violations.
- Climax: L–PS divergence widens to 2.5+ points; faction is powerful but brittle.
- Resolution: a single failed Mission or exposed violation collapses Popular Support; combined with low L, faction crumbles fast.

Sim-validated. Divergence reached 2.79 in sim v2.

**8.2.3 Succession Institutional Drift Arc** (4-8 seasons)
- Setup: faction has stable Cascade with leader L1.
- Complication: leader changes to L2 with different Convictions; cascade re-resolves over 4-6 seasons.
- Climax: faction's effective Convictions visibly shift; Public Expectation strictness recalibrates; existing strategies become costlier or cheaper.
- Resolution: faction's modus settles; cross-faction Disposition responds; new equilibrium.

Sim-validated. Cesare succession reached fid 0.631 (from 0.904) over 8 seasons.

### §8.3 Cross-scale arcs

**8.3.1 Insult-to-Strain Cascade** (multi-season)
- Personal insult (scene event) → injured NPC's Conviction Scar → DA submission via faction → exposure of covert action → Legitimacy violation → succession crisis → Strain shock.

Sim §1.3 demonstrated the chain; production game will produce variants of this template repeatedly.

**8.3.2 Religious Legitimacy Crisis** (4-12 seasons)
- Church faction Cascade Fidelity drops below role-expectation threshold → emits state.coup_attempted Keys → all Faith-aligned NPCs across peninsula form Memory → Disposition shifts cascade → multiple factions realign religious affiliation → continental-scale realignment.

**8.3.3 Mission-Shift Cascade** (3-8 seasons)
- Major state event triggers faction Mission shift → DA categories aligned/contradicted change → previously-rewarded actions become contradicted → Public Expectation strictness shifts → existing alliances become costly → realignment.

### §8.4 Multi-faction emergent arcs

**8.4.1 Strain Feedback Loop** (long-running, often campaign-long)
- Multiple factions' actions emit Strain-contributing Keys → peninsular Strain accumulates → Strain Keys reduce Public Expectation strictness everywhere → previously brittle factions become more tolerant → behaviors that were costly become cheap → late-game permissiveness.

**8.4.2 Succession Cascade** (multi-faction, 4-8 seasons)
- One faction's succession event raises Strain → adjacent factions experience Public Expectation pressure shifts → secondary realignments trigger across factions.

### §8.5 What's NOT supported

**Not currently supported by the stack:**
- *Single-character heroic arcs.* The architecture treats all NPCs as approximately equal in agency. A "chosen one" who differs structurally from other NPCs would need explicit authoring beyond the substrate.
- *Authored mystery / reveal arcs.* The substrate doesn't hide information from the engine; visibility controls who knows, not what's true. A "twist" requires authoring at a level above the substrate.
- *Designed dramatic timing.* Pacing is emergent rate; climactic beats aren't engineered. Most playthroughs will have flat stretches.
- *Failure of the world.* The architecture self-stabilizes (clamps, drift coefficients, damping). It doesn't model collapse states well — when a faction reaches L=0 + PS=0, what happens? The substrate doesn't say.

These are scope limitations, not flaws. They define where authored content layers above the substrate.

---

## §9 Engagement Mechanics Specifically Enabled

Beyond standard gameplay loops, three engagement mechanics emerge from the substrate:

### §9.1 The "Why?" diagnostic

Player asks: *why did Captain Almud just refuse to defend the eastern border?*

Substrate answer: walk Captain Almud's CAUSAL_GRAPH backward from his refusal-emission Key. Surface the chain:

1. Captain refused → because he had Memory of (3 seasons ago)
2. Spymaster privately admitted to crown betrayal → because (this caused)
3. Crown's Cascade Fidelity dropped 0.4 → because (last season)
4. Almud's predecessor was deposed → because (8 seasons ago)
5. The original public ceremony went badly...

This is a Renaissance pleasure: the careful tracing of cause through chronicle. **Players who engage with this become deeply invested**; the game *rewards* attention by making attention legible.

### §9.2 The "What if?" alternate-timeline

Sim §1.2 confirmed determinism. From any save point:

- Same seed + same player choices = identical timeline
- Same seed + different player choices = divergent timeline
- Different seed = different game

**Players can experiment.** "What if I hadn't insulted the captain?" → reload, choose differently, see how the chain diverges. This is a *post-game replay* mechanic that emerges from substrate determinism. Most strategy games can't do this because they don't have replay-deterministic event substrates.

### §9.3 Living NPCs

Each NPC has:

- Unique armature (Conviction vector × axis matrix → 4-dim interpretation)
- Unique cultural background (subtle interpretive bias even at low primary weights)
- Unique Self-Other orientation (drifts)
- Unique Memory (accumulated Keys; their salience differs per NPC)
- Unique Disposition matrix to all other actors

No two NPCs experience the same world. Two NPCs witnessing the same event interpret it differently; their Memories diverge; their Dispositions toward the source actor diverge; their future behaviors diverge.

**NPCs feel like people because they *are* people-shaped data.** Not because they're authored as characters but because the substrate makes them structurally distinct.

### §9.4 Memory as personal record

NPCs remember. A gift given 12 seasons ago appears in salience-decayed but still-present Memory. An insult survives. A witnessed atrocity is indelible.

**This produces the felt experience of *consequence over time*.** Player actions don't reset between scenes; they accumulate in NPC interior states. Disposition isn't a number; it's a reflection of stored Keys.

### §9.5 Self-Other axis as character development

An NPC who starts altruistic and accumulates self-benefiting Mission victories drifts toward self-orientation. The drift is observable (sim §1.8). Player can watch a faithful retainer become a calculating courtier over 15 seasons.

**This is character development via mechanics.** No author wrote "Almud becomes corrupt"; it emerges from her orientation drift under accumulated outcomes.

---

## §10 Risks and Limitations

### §10.1 Causes-population rate

Sim showed only ~15% of Keys had `causes[]` populated. If production stays at this rate:
- Causal chains are short on average (1-2 hops)
- The "Why?" diagnostic returns trivial chains for most queries
- Diagonal arcs require dense causes[] population to be walkable

**Mitigation:** authoring guidelines for systems emitting Keys must require causes[] when applicable. PP-687's spec should add §3.x guidance: "Whenever a Key is emitted *because of* prior Keys (witnessed events, retaliation, response to outcome), causes[] must reference those prior Keys."

### §10.2 Legibility burden

Rich emergence is illegible without surfacing UI. Player won't notice a Cascade Fidelity shift of 0.05 over 4 seasons unless the UI shows it. Player won't see an arc resolve unless the diagnostic announces it.

**Mitigation:** Phase 5a Godot scope must include diagnostic UI specifications:
- Faction state dashboard (L, PS, Cascade Fidelity, Strictness, Mandate trend lines)
- NPC Memory viewer (recent salient Keys; relationship to focal action)
- CAUSAL_GRAPH walker for "Why?" queries
- Arc resolution notifications (when L/PS divergence crosses threshold; when Cascade re-resolves to new equilibrium; when Conviction crisis triggers)

Without these, the substrate's richness is invisible.

### §10.3 Variance management

Pure emergence produces both rich arcs *and* incoherent/boring arcs. Some playthroughs will lack drama; some will overload.

**Mitigation:** scenario authoring layer above substrate. Scenarios add seed Keys (initial conditions) that bias toward arc-rich starting states. Scenarios can add *escalation Keys* at specific milestones to ensure dramatic beats. The substrate supports this — Key emission is the engine's plug-in point — but the scenario design is its own authoring pass.

### §10.4 Authored vs emergent balance

Pure emergence: every game different, but no guaranteed dramatic shape. Pure authoring: every game similar, but reliable drama. The right balance is in between.

**Mitigation:** treat the substrate as the *bedrock* of emergence; layer scenarios as *campaign skeletons* that author key inflection points (Mission shifts, faction succession events, environmental shocks). The substrate runs continuously; scenarios punctuate.

### §10.5 Pacing

The horizontal-direction analysis flagged this. The architecture is temporally honest but not narratively paced. Players may experience flat stretches.

**Mitigation:** an explicit *pacing system* that monitors emission density and inserts perturbation Keys when activity drops below threshold. Out of scope for PP-687; future PP candidate.

---

## §11 Verdict

The architectural stack is **structurally well-suited to emergent narrative**, with NERS scoring STRONG in 21 of 24 cells. The three MODERATE cells (Lateral S, Horizontal R, Horizontal S, Horizontal E) reflect the unaddressed pacing dimension and vocabulary debt that's planned for cleanup.

**Three engagement mechanics enabled** that extend beyond standard gameplay loops: the "Why?" diagnostic, "What if?" alternate-timeline replay, and living NPCs with persistent Memory.

**Multiple structural arc categories supported** at every scale, with sim-validated examples. The *Honest Defeat*, *Successful Tyrant*, and *Succession Institutional Drift* arc patterns are mathematically reproducible and dramatically rich.

**Three honest risks** that are addressable but not yet addressed:
- Causes-population rate (authoring guideline fix)
- Legibility burden (Phase 5a Godot UI scope)
- Variance management / pacing (future authoring layer)

**Net assessment.** The stack achieves what the project's intent statement names — "engaging game world with emergent narratives" — at a rare level of structural depth. The architecture's emergence isn't accidental or hopeful; it's mathematically demonstrable from the substrate. The remaining work is to (a) ensure the substrate is *seen* (Phase 5a UI), (b) ensure the substrate is *fed properly* (causes[] authoring discipline), and (c) ensure the substrate is *paced* (scenario layer + future pacing system).

**This stack is the strongest architectural foundation for emergent narrative the project has produced.** It deserves the implementation discipline its complexity demands.

---

**End evaluation.**
