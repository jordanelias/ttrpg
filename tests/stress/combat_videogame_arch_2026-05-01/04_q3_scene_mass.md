# Combat Stress Test — Chunk 5/7
## Q3 — How does the scene↔mass battle interface work?

**Brief:** The spatial-substrate decision in Chunk 4 (S7-hybrid) and time-shape decision in Chunk 3 (T2+T4) both have implications for how scene combat connects to mass battle. Canon already has `mass_battle_v30 §B.5 Hybrid Handoff` and `Part D Mass Combat World Bridge` — both define interfaces, but neither was written assuming videogame-medium continuous scale traversal. This question stress-tests how the two scales connect when both share the same canonical substrate primitives.

**Method:** NERS-all-directions per interface candidate. Eight cross-scale interaction patterns. Each evaluated for whether it preserves canonical mass + scene mechanics, what it costs, and what it unlocks.

---

## Existing canonical baseline

`mass_battle_v30 §B.5` defines a Hybrid Handoff — when a hero engages a key target, the engagement zooms into scene combat, resolves at scene scale, and returns the result to the mass layer. This was authored for a board-game/TTRPG hybrid. **In a videogame, it can be more.**

`mass_battle_v30 Part D` defines post-battle world bridges — battlefield as fieldwork site, named officers as personal-scale NPCs, player morale effects across both layers.

The question is not whether to preserve these — they are canonical and survive — but **what additional cross-scale interfaces the videogame medium enables** that the original board-game-hybrid framing could not host.

---

## Interface candidates

| ID | Pattern | Description |
|---|---|---|
| **I1** | Pause-and-zoom (canonical Hybrid Handoff) | Mass battle pauses; hero engagement opens scene-scale combat; result returns to mass layer |
| **I2** | Continuous-zoom (camera-driven) | Camera zooms from army-scale view to character-scale view without modal break; both scales active simultaneously |
| **I3** | Hero-as-unit (mass-only) | Hero is a unit-scale actor with hero stats; never zooms; mass scale handles everything |
| **I4** | Hero-detached (parallel scenes) | Hero acts at scene scale on a sub-region; mass continues at unit scale; results merge at end of round |
| **I5** | Commander view (RTS-like) | Player commands units in real-time at mass scale; no scene zoom; hero is just a command modifier |
| **I6** | Strategic→tactical→personal (3 modes) | Three explicit modes (mass / unit / personal) with player-controlled mode switch |
| **I7** | Battle-as-fieldwork (post-battle only) | Mass battle resolves abstractly (no zoom); hero is a fieldwork actor on the battlefield site afterward |
| **I8** | Embedded scenes (scripted moments) | Mass battle plays out automatically; player only enters scene scale at scripted narrative beats |

---

### I1 — Pause-and-zoom (canonical Hybrid Handoff)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ⚠ | ⚠ | Modal interruption breaks immersion every zoom; legible but stuttering |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Canonical — both scales' math stays untouched, handoff is the only new logic |
| Vertical | ✓ | ✓ | ✓ | ⚠ | Vertical movement IS the interface — but it's mode-switch, not zoom; vertical traversal has cost |
| Diagonal | ✓ | ✓ | ⚠ | ⚠ | Threadwork crossing scales (§A.10) requires careful re-injection at each handoff — paperwork |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other lateral systems untouched |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | Repeated handoffs across a campaign feel rote — the pause is felt every time |

**Verdict:** Safe baseline. Lowest implementation cost. Highest immersion tax.

---

### I2 — Continuous-zoom (camera-driven)

Both scales are simultaneously active. Camera position determines what the player sees and interacts with. At max-zoom-out: army units; at max-zoom-in: individual characters. Mass-scale and scene-scale resolve **on the same time-shape** (T2+T4 IP gauge from Chunk 3) — both tick on the same clock. Intermediate zoom levels show units as composed of visible individual fighters.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ✓ | Modern videogame paradigm (Total War: Three Kingdoms hero duels mid-battle); high implementation cost; deeply immersive |
| Bottom-up | ✓ | ⚠ | ✓ | ✓ | Requires both scales' math to run continuously — but if T2+T4 unifies time-shape, they tick on the same clock natively |
| Vertical | ✓ | ✓ | ✓ | ✓ | **Vertical scale traversal is literally a zoom** — granularity is camera-driven, not mode-driven; canonical scales are reaffirmed by the UI |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork at any scale runs on the same clock; cross-scale fire (§A.10 §10.3) becomes natural |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems unchanged |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Player learns one camera language; pacing feels organic across campaign |

**Verdict:** **Highest-fit interface if the engineering is feasible.** All directions clean. Mass-battle rework cost is the question — but recall from Chunk 4 that S7-hybrid keeps mass-battle substrate canonical (zones unchanged), so the rework is in *time-shape* (Chunk 3 already recommended unification) and *render layer* (intermediate zoom levels). Substrate stays canonical.

**Implementation cost:** High. Two scales' simulations running concurrently; intermediate zoom levels need to render units composed of individuals. Mitigation: **at intermediate zoom, units render as schematic icons; at full-zoom-in, individuals render**. The simulation is unit-scale by default and *spawns individuals only when zoomed past a threshold*. This is the Total War: Three Kingdoms / Mount & Blade Bannerlord pattern — proven, expensive, achievable.

---

### I3 — Hero-as-unit

Hero is treated as a unit-scale actor in mass battle. Has unit stats (Size 1, high Power, high Discipline). Never zooms in. All canonical scene mechanics (Combat Pool, Wound Interval, Stamina, weapon TN, Stunt) collapse into unit-scale resolution.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ⚠ | Loses personal-scale player connection during mass battles — heroes feel like generals, not protagonists |
| Bottom-up | ✗ | ⚠ | ✗ | ✗ | **Canonical scene math is discarded** during mass battles — Combat Pool, Feint, Stunt all dormant; canonical Hero-Unit-Bond §11 PP-179 broken |
| Vertical | ⚠ | ✓ | ⚠ | ✓ | No scale traversal — but that means no scale traversal *at all* during mass battle |
| Diagonal | ✗ | ⚠ | ⚠ | ✗ | Threadwork at personal scale (canonical Practitioner Leap §10.1) cannot fire mid-battle — narrative tension dies |
| Lateral | ✓ | ✓ | ⚠ | ⚠ | Other lateral systems unaffected |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Heroes feel disconnected from mass-battle narrative beats |

**Verdict:** **Reject.** Canonical scene mechanics are abandoned during mass battle. Loses the protagonist-in-history feel.

---

### I4 — Hero-detached (parallel scenes)

Hero acts at scene scale on a sub-region of the battlefield (a flank, a hill, a breakthrough). Mass scale continues at unit scale concurrently. Results merge at the end of each round — hero outcomes affect adjacent units (kill enemy officer → unit Discipline penalty), unit outcomes affect hero (unit routs nearby → hero exposed to flanking).

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ✓ | Hero feels heroic; battle continues realistically; videogame-medium-native |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Both scales' canonical math run independently; merger is per-round bookkeeping |
| Vertical | ✓ | ✓ | ✓ | ✓ | Scales coexist explicitly — the interface IS the scale split |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork at hero scene affects mass via §A.10 cross-scale fire — canonical |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems unaffected |
| Horizontal | ✓ | ✓ | ✓ | ⚠ | Risk: every battle becomes "find the breakthrough where the hero matters" — pattern fatigue without scene variety |

**Verdict:** **Strong second-best.** Engineering simpler than I2 (no continuous zoom — distinct scenes resolved in parallel). Preserves both scales' canonical mechanics. Per-round merger logic is the only net-new spec.

---

### I5 — Commander view (RTS-like)

Player commands units in real-time at mass scale. Hero is a unit modifier or commander-level buff. No scene zoom.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ⚠ | Off-tone for character-driven CRPG |
| Bottom-up | ✗ | ✓ | ✗ | ✗ | Canonical scene mechanics dormant during mass battle (same as I3) |
| Vertical | ⚠ | ✓ | ⚠ | ✗ | No scale traversal |
| Diagonal | ✗ | ✗ | ✗ | ✗ | Threadwork, Conviction, scene-scale Wound Interval — none fire during commander view |
| Lateral | ✓ | ✓ | ⚠ | ⚠ | Untouched |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Mass-battle pacing is fine; but mass battles feel disconnected from rest of game |

**Verdict:** **Reject.** Off-genre and breaks canonical scene-scale integration.

---

### I6 — Strategic / tactical / personal (3 explicit modes)

Three modes: **strategic** (army movement at territory scale, canonical campaign layer), **tactical** (mass battle at unit scale), **personal** (scene combat at hero scale). Player switches mode explicitly via UI button or auto-triggered by event.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ⚠ | ✓ | ⚠ | Three modes is two mode-switches per encounter — fatigue accumulates |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Canonical math at each scale survives intact |
| Vertical | ✓ | ⚠ | ✓ | ⚠ | Scale traversal is real but mode-gated — same as I1 problem at three levels |
| Diagonal | ✓ | ✓ | ⚠ | ⚠ | Threadwork crossing modes requires re-injection per mode-switch |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems unaffected |
| Horizontal | ⚠ | ⚠ | ⚠ | ⚠ | Three-mode UX is a known cost (Total War, Crusader Kings) — workable but adds learning friction |

**Verdict:** Workable but inelegant. Adds mode-switch tax compared to I2 (continuous-zoom). If I2 engineering is infeasible, I6 is the **explicit fallback**.

---

### I7 — Battle-as-fieldwork (post-battle only)

Mass battle resolves abstractly without player interaction (or with a strategic-only commit decision). Hero acts only post-battle as a fieldwork actor on the battlefield site. Canonical Part D World Bridge upgraded to be the entire interface.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ⚠ | Battles become cutscene-then-cleanup; loses visceral participation |
| Bottom-up | ⚠ | ✓ | ⚠ | ⚠ | Mass canonical math runs without player input; scene canonical math runs only post-battle |
| Vertical | ⚠ | ✓ | ⚠ | ⚠ | Scales coexist serially, not in parallel |
| Diagonal | ⚠ | ✓ | ⚠ | ⚠ | Mid-battle Threadwork cannot fire — kills canonical §A.10 dramatic moments |
| Lateral | ✓ | ✓ | ✓ | ✓ | Other systems unchanged |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Each battle is "watch outcome, walk the field" — narrative beats only post-hoc |

**Verdict:** **Reject as primary.** Useful as **fallback for off-screen battles** the player isn't directly involved in (a faction war elsewhere on the peninsula resolves abstractly; player visits the aftermath). Canonical Part D World Bridge already does this for that use case.

---

### I8 — Embedded scenes (scripted moments)

Mass battle plays out automatically. Player enters scene scale only at scripted moments — duel with enemy general, defend the standard, breach the gate. Pre-authored.

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✓ | ⚠ | ⚠ | Cinematic — but author-driven, low player agency |
| Bottom-up | ✓ | ✓ | ⚠ | ✓ | Both scales' canonical math used at scripted moments |
| Vertical | ⚠ | ✓ | ⚠ | ⚠ | Scale traversal happens — but only when scripted, not when player chooses |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Threadwork can fire at scripted moments cleanly |
| Lateral | ✓ | ✓ | ✓ | ✓ | Untouched |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Scripted beats over a campaign require authoring per battle — content cost scales linearly |

**Verdict:** Useful **layer atop I2 or I4** — battles can have scripted beats *and* free zoom. Not a primary on its own.

---

## Aggregate read on Q3

| Candidate | All-directions verdict | Recommendation |
|---|---|---|
| **I2 continuous-zoom** | All 6 directions ✓ or ⚠ once; no ✗ | **Primary if engineering feasible** |
| **I4 hero-detached parallel** | All 6 directions ✓ except minor horizontal pattern-fatigue risk | **Primary if I2 infeasible; fallback otherwise** |
| I1 pause-and-zoom (canonical) | Safe but immersion-tax | Safety net; canonical baseline |
| I6 three explicit modes | Workable, inelegant | Explicit-mode fallback |
| I8 embedded scenes | Layer, not primary | Combine with I2/I4 |
| I7 battle-as-fieldwork | Off-screen battles only | Limited use case |
| I3 hero-as-unit | Breaks scene canon | Reject |
| I5 commander view | Off-genre | Reject |

**Composite recommendation:** **I2 + I8** — continuous-zoom as the base interface, with scripted I8 beats authored at narrative climaxes. **I4 as fallback** if I2 engineering scope balloons. **I1 as safety net** that the engine can always degrade to.

The three-tier fallback is itself a design feature: ship I1 first (lowest cost, canonical-faithful), upgrade routes to I4 (parallel scenes, medium cost), reach I2 (continuous zoom, highest cost) over development. Each tier is a complete game.

---

## Specific cross-scale mechanics — how each interface handles them

### Threadwork crossing scales (canonical mass §A.10)

| Interface | Threadwork at scene level → mass | Threadwork at mass level → scene |
|---|---|---|
| I1 pause-and-zoom | Hero Leap inside scene; on un-zoom, mass effects (terror) apply per §A.10 | Mass-scale Practitioner channels affect hero via canonical Knot rupture / Conviction Scar bleed |
| **I2 continuous-zoom** | Hero Leap visible at any zoom; effects apply on same clock; no transition | Mass channels affect hero immediately; same clock |
| I4 hero-detached | Hero Leap at scene scale fires §A.10 effects on adjacent units at end of round | Mass channels arrive in hero's parallel scene at end of round |
| I3/I5 (hero-as-unit/commander) | Cannot fire personal-scale Leap — canonical mechanic dormant | N/A — no scene scale |
| I6 three-mode | Mode-gated; same as I1 with extra layer |
| I7 post-battle | Threadwork in battle is engine-resolved without player input |

I2 is uniquely smooth on Threadwork.

### Hero death in mass battle

| Interface | Hero death handling |
|---|---|
| I1 | Scene-scale Wound cascade fires inside zoomed scene; canonical §13.3 Death Cascade on un-zoom |
| **I2** | Wound cascade at any zoom; Death Cascade fires immediately on same clock |
| I4 | Scene scale handles Wounds; mass scale informed at end of round |
| I3/I5 | Hero "dies" by unit being eliminated — loses scene-scale Wound nuance, Death Cascade reduced |
| I7 | Hero cannot die mid-battle (no scene presence) — kills tension |

I3, I5, I7 all weaken the canonical Death Cascade. I1, I2, I4 preserve it.

### Rout / pursuit (canonical mass §A.12)

| Interface | Rout handling |
|---|---|
| I1/I2/I4 | Routing units flow across battlefield; hero can pursue at scene scale (cinematic chase) |
| I3/I5/I7 | Rout resolves at unit/abstract scale; hero participates only as unit modifier |

Pursuit-as-scene is a major narrative beat. I1/I2/I4 enable it.

### Officer assassination (canonical mass §D.2)

| Interface | Officer assassination |
|---|---|
| I1 | Detect officer → zoom into scene → kill → un-zoom → unit Discipline drops |
| **I2** | Mark officer at any zoom → close in → kill → unit responds in real time |
| I4 | Hero scene targets officer; on success, end-of-round merger applies Discipline drop |
| I3/I5 | Officer is just a unit stat; no narrative scene |

I2 maximizes the drama; I4 preserves it cleanly; I3/I5 lose it.

---

## Implications for canonical mass_battle_v30

Adopting **I2 (continuous-zoom)** with **T2+T4 unified time-shape** (Chunk 3) and **S7-hybrid spatial substrate** (Chunk 4) requires the following canonical updates to mass_battle_v30:

| Current canonical | Required change |
|---|---|
| `§A.7 Battle Turn Structure` — distinct phase model | **Unify with scene phase + IP gauge model.** Mass phases collapse into IP-driven unit acts on the same clock as scene actors. |
| `§B.5 Hybrid Handoff` — board-game-flavored zoom-in/out protocol | **Generalize to videogame-medium continuous zoom.** Handoff becomes camera-zoom event, not modal switch. |
| `Part B Board Game Mass Battle` | **Reframe as Tier-3 abstract resolution mode** for off-screen / non-participating battles (I7 use case) — still canonical, but not the default mode in videogame. |
| `Part D World Bridge §D.1` Post-battle scenes | **No change.** Already videogame-friendly. |

These changes are **substantial** but every change reduces complexity rather than adding it (mode unification, not mode addition). The board-game artifacts in Part B retain value as the abstract-resolution mode for off-screen wars.

---

## Implications for mass battle scope

The S7-hybrid spatial decision (Chunk 4) keeps mass-battle's canonical zones intact at large scale. The I2 interface decision keeps mass-battle's canonical math intact. **What changes is presentation, not mechanics.**

Specifically: mass battle in videogame is the same 6-step Cascade Phase (canonical §A.7), the same Power dice resolution, the same Discipline checks, the same §A.10 Threadwork — **rendered as continuous-time IP-gauge tactical battle on a zoomed-out version of the scene's spatial substrate**.

The three-mode TTRPG/Hybrid/Board-Game framing in canonical `mass_battle_v30` becomes:
- TTRPG mode → **deprecated** (no GM in videogame)
- Hybrid mode → **becomes the videogame default** (continuous zoom)
- Board Game mode → **retained** as abstract off-screen battle resolution

This is the kind of canon refactor the videogame medium permits and the move-away-from-zone-abstraction surfaces.

---

## Canon gaps surfaced (Q3)

1. **Continuous-zoom spec.** Canonical §B.5 defines a board-game-flavored handoff. A videogame continuous-zoom interface needs net-new spec (camera-driven scale, intermediate zoom rendering, simulation granularity rules).
2. **Unified IP gauge across scales.** Chunk 3's T2+T4 recommendation, applied across both scales, requires explicit canonical "IP gauge — same clock for unit and personal actors" rule.
3. **Hero-detached parallel scene merger logic.** I4 fallback requires per-round end-of-round merger spec (hero outcomes → adjacent unit modifiers, unit outcomes → hero exposure).
4. **Off-screen battle resolution mode.** Canonical Part B board-game resolution is the natural fit, but its trigger ("when does a battle resolve abstractly vs. with player participation") is not specified — needs a rule.
5. **Officer assassination ↔ scene scale.** Canonical §D.2 names officers as personal-scale NPCs but doesn't specify how a hero targets one mid-battle. I2 enables this; spec needed.
6. **Pursuit-as-scene.** Canonical §A.12 Rout and Pursuit is unit-scale; I1/I2/I4 enable scene-scale pursuit; spec needed for trigger and resolution.

---

## Godot implementation notes

- **I1 (canonical baseline):** lowest cost. Modal scene-switch. Existing Godot scene-tree pattern. Achievable in weeks.
- **I4 (parallel scenes):** medium cost. Two scene-trees ticking concurrently with end-of-round merger. Months.
- **I2 (continuous-zoom):** highest cost. Multi-resolution simulation, intermediate zoom rendering, individuals-spawn-at-threshold. Major engineering project. Quarters.

**Recommended ship path:** I1 in MVP → upgrade to I4 in v0.2 → reach I2 in v1.0. Each version is a complete game. The interface tier is a major shipping milestone.

End Chunk 5.
