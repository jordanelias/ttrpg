---
atom_id: threadwork_master__03__iii-what-the-player-should-feel
source_file: threadwork_master.md
source_section: "III. What the player should feel"
section_index: 3
total_sections: 12
line_count: 196
char_count: 19623
source_sha256: 66219286b90b6f9d
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## III. What the player should feel

The player should feel that they are encountering a world that is thicker than they had thought, that has an order beneath its surface they can partially perceive but never fully understand, that responds to action in ways shaped by skill and shaped by something that exceeds skill. They should feel that operations on this world have weight before they have cost — that the act of *touching* something at substrate depth changes both the toucher and the touched in ways neither can fully account for. They should feel, by the end of the campaign if they have travelled far enough, that what they have learned to do is itself a kind of intimacy with what cannot be described.

Fourteen specific phenomena, each paired with the engine state that produces it. The engine state is invisible to the player most of the time. The phenomenon is what they receive.

### III.A The world is whispering, all the time

**Felt:** Texture of places. Weather. How NPCs lean toward or away from each other. Some places feel taut. The practitioner's body responds to where it enters. None of this is named in numbers; it is the world's quality.

**Engine:** Per-territory fray field (sparse map of locations to magnitudes). Knot graph across configurations. Recent operation activity per region. NPC dialogue procedurally tinted. Weather and ambient audio shifted by accumulated fray. No numerical surface; qualitative heat-map at TS ≥ 30.

**Why it matters:** This is the foundation. Players learn the substrate's manifestation through felt engagement before any tooltip explains anything. When a high-TS NPC eventually says *this place is fraying*, the player already knows.

### III.B Every act has weight before it has cost

**Felt:** Approaching threadwork, the practitioner stands at the edge of a place where the world will be different on the other side. Interface slows. Music thins. Breathing audible. The thing they are about to touch becomes visible in a way it wasn't a moment before.

**Engine:** Pre-Leap interface treatment. Pool versus TN computed; three-axis Ob shown. Cost tooltip: expected fray range, expected knot feedback magnitude, expected Coherence risk, expected Causal Disjunction increment, qualitative pre-roll perception of substrate condition.

**Why it matters:** The player understands what they are doing in their gut before any roll resolves. Numbers come after the gut.

### III.C Skill controls aim, not consequence

**Felt:** A high-skill practitioner reliably hits what they aim at. The substrate's response is unpredictable for everyone. Master Mending in pristine substrate feels safe; master Mending in heavily-frayed substrate feels uncertain in the same way a beginner's would.

**Engine — the two-roll architecture (A1):**
- **Roll 1 (visible, public):** Pool [(Spirit×2) + History + TPS] versus TN. Successes − Ob = S. Determines whether operation lands as intended.
- **Roll 2 (visible to player; modifier hidden):** 2d6 − hidden_substrate_modifier. Modifier derived from local fray density, knot graph density, recent activity. Player sees their roll; not the modifier.
- **Pre-roll qualitative perception** (refinement from textile audit): the practitioner's body senses substrate condition before rolling — "the substrate feels taut here," "the ground feels unwilling," "compliance nearby" — gated by TS depth. The number stays hidden; the felt-tone does not. Skilled practitioners are not blind to substrate; they cannot predict its response.

**Verification:** Master Mending Object scope produces 73% Compliant in pristine substrate, 28% in moderately frayed, 0% in catastrophically frayed. Same skill; different substrate; different distribution. Skill controls intent-coupling frequency (whether op succeeds). Substrate variability stays substrate-side.

**Information rule:** Diagnose-Thread returns qualitative substrate descriptors only ("heavily frayed," "Lock active nearby"). Never numerical hidden_modifier. Otherwise A1 opacity is defeated.

### III.D The substrate's response is *the thing that happened*

**Felt:** Dice resolve. The player sees a configuration snap into held-state with a sound they hear in their chest. Light thickens. Someone three rooms away forgets why they walked into the kitchen. A child cries.

**Engine — Substrate Response Table (Appendix A — to be specified):**
- 18 rows, indexed by 2d6 − hidden_modifier outcome.
- Each row: three-axis pattern, tier values, fictional manifestation template, MS delta, knot feedback magnitude, CD delta, FD delta, Certainty modifier.
- All canonical co-movement effects produced per op (P-01).
- At least 30% Wild-band rows produce **surfeit-of-being** outcomes (canon A7) — configurations exceeding their stable form, "too present" rather than "less present." Monstrous incursions appear here.
- Fictional manifestations rendered in the world: animation, sound, NPC reactions, environmental change. Optional "what just happened" panel for numerical detail; closed by default.

**Why it matters:** The player can play the campaign without ever opening the numerical panel. The mechanism produces the manifestation; the manifestation is what the player receives.

### III.E Damage takes specific forms

**Felt:** A configuration that has been Pulled is left loose and trembling, recoverable. A configuration that has been Torn has unresolved threads that the substrate cannot work with cleanly. A configuration that has been Dissolved leaves persistent absence the substrate continues to reach for. A region operated on too heavily and too long *felts* — the substrate's structure has fundamentally changed and cannot return to what it was.

**Engine — damage-form taxonomy (refinement from textile audit):**

| Damage form | Substrate manifestation | Repair |
|---|---|---|
| Active fraying | Disjunct between is and is-becoming at site | Mending (TS-gated perception) |
| Lock-radiation | Strain spreading from locked configuration through its loops and knots | Mending of surrounding substrate; Lock release |
| Imposed-Binding fray | Disjunct concentrated at bound site, continuous while held | Binding release only |
| Pull-residue | Loosened configuration awaiting re-resolution | Configuration completing alternative; Mending |
| Tear | Open wound with unresolved threads | Mending if caught early; persistent fray otherwise |
| Snag | Pulled-but-not-failed structural strain | Mending; or further pull = run |
| Run | Failure propagating along loop-grammar of self-coherent configuration | Catch with Mending before further propagation |
| Felting | Substrate-state irreversibly altered by sustained operation | None — replacement only (heroic intervention, external substrate) |
| Persistent residue | Substrate continuing to render absence at Dissolution site | Long elapsed time; heroic Mending at scale |
| Dissolution wake | Substrate disturbance radiating from removal site | Multi-practitioner coordinated Mending |

**Cross-link:** Configurations with self-coherent loop-grammar (canonical persons, institutions with deep procedural memory) fail through running. Configurations with foundationally-embedded warp-weft structure (territories, social fabrics, embedded relationships) fail through tearing. Mixed configurations can fail either way. The repair operation is specific to damage form.

### III.F Locks fray neighbours; bindings fray themselves

**Felt:** The locked thing holds. The cook three rooms over is the one paying for the practitioner's choice. The bound thing manifests visible wrongness at the bound site itself; bystanders react.

**Engine:**
- **Lock-radiation** (S1, refined): `fray_radiated_per_season = 0.5 × (loop_density + active_knot_count) × (1 + lock_seasons / 8)`. Loop_density measures the locked configuration's internal self-referential structural depth — for a person, depth × duration of self-identity practices; for an institution, count of internal procedures and roles. Locks fray *both* through the configuration's external bonds AND its internal coherence, because both are straining when redirection happens.
- **Imposed Binding fray** at site, continuous while held. Cannot be Mended without releasing.
- **Restoration paths:** Mending of Lock-frays repairs surroundings without releasing the lock (concealed-lock + maintained-mending pattern viable, expensive). Binding-frays cannot be mended; they are the binding's continuous cost.

**Why it matters:** This is the most counter-intuitive ontological claim of the system. Most players will assume the Lock is the thing that costs. The realisation that *what surrounds the Lock* is what costs — that the cook three rooms over is the one paying — is one of the system's deepest experiential teachings.

### III.G Mending is attention, not work

**Felt:** The practitioner kneels. Watches. Follows what the substrate is already trying to do. Interface slower. Music does not swell. Hands hover, do not close. Dice rolled with held breath between them.

**Engine:**
- Mending uses Compliant band only on substrate-response. Maximum Tier 2. No Wild outcomes possible on successful Mending.
- Restorative-tag knot propagation: zero Coherence cost (canon Amendment 3), zero feedback toward practitioner.
- Fray closure proportional to S and Tier. Mending REDUCES Causal Disjunction in territory.
- **Mending bounded by perception:** practitioner cannot mend frays they cannot perceive. TS-gated. Low-TS Menders close visible damage; deeper damage remains.

**Why it matters:** The canonical "fixed pipes but not roof" pattern emerges naturally. A confident TS 30 Mender closes Object/Personal damage while Relational/Field/Structural damage builds invisibly. When their TS rises through Confrontation, they perceive what they missed. *This is the Mender's Burden story arc, mechanically.*

### III.H Accumulation haunts the practitioner's own past

**Felt:** Recent past becomes unreliable. Witnesses report things that don't match what the practitioner remembers. Old wounds ache for no reason. A conversation last week is now denied by the other party. The light in the practitioner's home looks slightly different than it should.

**Engine — Causal Disjunction (R1, restoring threadwork_v30 cut):**
- CD as separate stat track on practitioner sheet.
- `CD_delta_per_op = Past_axis_tier × scale_multiplier + History_Resonance_check`. Always ≥ 1 per op (canon P-11: no zero-CD ops).
- Mending REDUCES CD: −1 to −2 per successful Mending in territory.
- Thresholds: Low (1–4) narrative discomfort; Medium (5–9) unreliable memory effects; High (10–14) significant memory failures; Catastrophic (15+) memory cannot be trusted.

**Plus parallel Forward Disjunction (FD — surfaced in textile audit):**
- Tracks future-axis temporal disjunction from operations that pre-actualise future configurations.
- Accumulates from manipulative-tag operations whose Future-axis tier is significant.
- Thresholds: as CD but inverted — sense of fated outcomes, premature lock-in, future foreclosure.
- The Foundational-scale Manipulative Catastrophe (canon/02 Amendment 4) was extreme FD — over-actualised future inverting catastrophically.
- Mending reduces FD when restoring configurations the practitioner had over-actualised.

**Surfaced to player:**
- Subtle dialogue inconsistencies from NPCs who knew the practitioner.
- Quest log entries diverging from how the practitioner remembers.
- At higher CD/FD: practitioner's own journal entries become unreliable. Time skips in conversation. Some days the practitioner finds outcomes they don't remember choosing.

### III.I Knots are felt through other people's responses

**Felt:** Months after the practitioner Locked the noble's loyalty, a bartender in another city hesitates when they enter. Not because the bartender knows. Because something has changed in *how the practitioner is rendered to others*, and the bartender responds to wrongness they can't articulate.

**Engine:**
- Knot graph per canon/02 Amendment 6. Every Leap forms knots tagged restorative/manipulative/destructive.
- Knot-profile data structure (R6): operation_type, target, formation_context (session, scale, co_practitioners), formation_date.
- Outward-facing alteration: per canon/01 Amendment 1, the practitioner's outward facing of layer 2 is altered by accumulated manipulative/destructive knot weight.
- NPC response: NPCs respond to the practitioner's outward facing without commentary. No moralism. No score.

**Why it matters:** Moral weight enters without moralism. The world reads accumulated state through everyone the practitioner meets. The Church misreads this and condemns; the substrate does not. The player learns the difference.

### III.J Mass scenes alter the substrate

**Felt:** A battle is won or lost. The territory afterward is different — not just owned by a different faction. The land has been written into. People speak slightly past each other for years. Crops grow oddly in the valley where the lattice collapsed. A bird that was once common is missing.

**Engine — R2 (with explicit canon-compromise flag):**
- Generic-NPC threadwork tracked as aggregate per faction × scope per round.
- Single substrate-response rolled per faction-scope-batch — full three-axis result. *This satisfies P-14 in spirit by producing co-movement; it is acknowledged as a tractability compromise rather than canon-strict.*
- Aggregate outcome applies to all generic NPCs of that faction × scope.
- Knot feedback for generic-NPCs is abstracted — no named knot graphs but faction-knot-density carries the magnitude.
- Named NPCs and player characters retain full per-op resolution.

**Note:** This is the closest the system can get to P-14 compliance at mass-scale without making mass scenes computationally intractable. Editorial flag: Jordan should bless or revise.

### III.K Multi-practitioner contests punish all participants

**Felt:** Three practitioners contest a configuration. The substrate refuses everyone. All three feel feedback through their own knots. The substrate has not chosen sides; it has *withdrawn from being touched*.

**Engine — A4:**
- One substrate-response roll for the contested op (substrate is unitary).
- Worst S among contested practitioners drives the modifier.
- Each practitioner's knot feedback runs independently per canon/02 magnitudes.
- Cascade walks each practitioner's knot graph separately.
- Lattice collapse (3+ practitioners with 2+ opposing intentionalities): all practitioners receive feedback as if they had performed the operation *opposed to* their intent.

**Why it matters:** Canon A13 (collective operations produce emergent consequences none intended) made mechanical at correct weight.

### III.L The substrate is finite-buffer, not negative-sum

**Felt:** The peninsula is sliding. Not because the substrate is decaying on its own — the substrate alone, untouched, would relax. Because autonomous NPC operations are running ahead of the substrate's relaxation rate. The buffer is exceeded. Damage accumulates.

**Engine — A5 (reframed from textile audit):**
- Substrate has finite buffer per region per season for absorbing operations without persistent damage.
- Decay function: `decay_rate = 0.25 × (1 − fray_density / 100)`. Pristine substrate heals fast; frayed substrate barely heals at all.
- Under typical autonomous-NPC density, peninsular MS drifts toward 25–30 over 100 seasons of non-intervention. *This is not inherent decay; it is operations exceeding buffer.*
- MS = 0 = **felted state** (refined from textile audit): substrate fundamentally altered by sustained operation, irreversible to original form.

**Reframing matters:** The substrate is not running down on its own. The world is operating on it faster than it can rest. Player intervention is what holds the line. Peninsular crisis is the baseline players resist, but the cause is operational, not ontological.

### III.M MS=0 is felting (refined from textile audit)

**Felt:** A territory at total fabric collapse is not "very damaged but recoverable." It has *changed kind*. The original configuration cannot be restored. What remains is a different substrate-state, capable of supporting new configurations of new kinds, but the original is gone forever.

**Engine — G3 revised:**
- At fray density = 100, substrate has felted. Single-practitioner Mending cannot recover original configuration.
- Heroic intervention can establish *new* substrate-relations on top of the felted region (new configurations, new patterns).
- Recovery is not restoration; it is replacement with acceptance that the original is lost.
- Per canon: this is the canonical Calamity-zone state. Locked zones are felted substrate. They permit no Mending of what was; they permit only working with what now is.

**Why it matters:** This is canonically aligned with how Calamity-zones currently function. Names the felting explicitly so the mechanic does not promise recovery the substrate cannot deliver.

### III.N Perception, once gained, cannot be relinquished

**Felt:** The first time the practitioner sees a thread is the most beautiful frame in the game. It arrives earned, through a Confrontation they did not engineer. After that moment, they cannot stop seeing what they have seen. Some choices they used to be able to make are no longer visible to them as choices.

**Engine:**
- **Thread Sensitivity (TS) gates depth of constitutive-grammar perception** (refined from textile audit). Different TS levels see different *depths of how configurations are constituted*, not different quantities of substrate.
- **TS develops through Confrontation only** (R3, canon A10 + C3). Triggers: witnessing Coherence-failure events at Tier 3+; encountering threadcut beings or Gap manifestations; witnessing Wild substrate-response in own or knotted operations; surviving Coherence checks by margin ≤ 1; encountering Calamity sites. Routine successful operations do not advance TS.
- **Skilled regulation** is distinct from perceptual depth (textile audit gap surfaced). Bodily competence with operations — felt regulation of tension, accumulated familiarity with substrate-conditions — accumulates through practice and is captured in the TPS component of pool. Distinct stat from TS.
- **Perceptual Transformation (PT)** — separate, irreversible track (R4, canon A11 + C4). Rises with Confrontation; can rise without TS gain. Mechanical effect: at higher PT, certain choice options become *invisible* to the player character — not forbidden but no longer perceived as choices.
- **PT and TS are orthogonal**, not coupled. A practitioner can have high TS with low PT (Mender path) or moderate TS with high PT (fanatic path). Different combinations produce different beings.

**Surfaced to player:**
- First Confrontation: singular moment, designed for, not engineered. Visual/audio/animation unique. Designed to be unforgettable.
- Subsequent Confrontations: still shaped, still costly.
- After Confrontation: persistent change in how the world is rendered. Some interface options remove themselves over time as PT rises. The player notices what is gone, sometimes; sometimes only realises afterward.

**The deepest recognition (apophatic mode 3):** at PT 10, the practitioner recognises that *every prior framework they used to understand threadwork — including their own current operational understanding — was rendered, not real*. They stand in some relation to substrate they cannot articulate even to themselves. This is the canonical one-way gate at maximum depth. It is the campaign's most precious offering and its deepest cost.

---
