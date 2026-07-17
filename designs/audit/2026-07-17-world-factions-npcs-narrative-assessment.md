# Valoria — A Narrative Compendium of World, Factions & NPCs

**Status: ANALYSIS / ASSESSMENT — not a design doc, not canon.**
This is a qualitative reading of work already performed across the repository (fresh *and* deprecated).
It ratifies nothing, supersedes nothing, and touches no ledger, `CURRENT.md` row, or module contract.
Its purpose is threefold: to assess the **narrative quality** of Valoria's world, factions, and NPCs;
to name the **precedents and influences** that shaped them; and to lay a **platform** from which unique
features, actions, and mechanisms can be designed — by translating the setting's qualitative texture
into quantitative game form.

- **Date:** 2026-07-17
- **Scope:** world · factions · NPCs · emergent narrative · precedents & influences · the texture→mechanism bridge
- **Method:** a twelve-agent parallel deep-read of the narrative surface — canon foundations
  (`canon/`), the Solmund mythology (`systems/world/solmund_*`), geography & calamity (`systems/world/`,
  `systems/settlements/`), the faction corpus (`designs/provincial/`, `designs/factions/`), the NPC corpus
  (`systems/npcs/`, `references/npc_registry.yaml`), the arcs (`arcs/`), the historical-precedent program
  (`research/`), and the deprecated archives (`deprecated/`) — synthesized into this single document.
- **A source map is appended** at the end (what was read).

---

## The thesis

Valoria's narrative identity resolves to one disciplined idea, stated almost as a motto in
`designs/provincial/victory_v30.md`:

> **"Two simultaneous contests: who governs the peninsula AND whether it survives."**

Everything is downstream of that sentence. One contest is **political** — five-plus factions maneuvering
for legitimate rule of a fifteen-territory peninsula. The other is **ontological** — a wounded
metaphysical substrate ("Mending Stability") that mass violence corrodes independent of who wins any
battle. *You can win the war and lose the world.* The setting is a **post-secession recovery story** (35
years out from imperial occupation) engineered to be structurally hostile to the conquest fantasy it
superficially resembles, and its signature story is a **tragedy of structurally-correct actors**: not
villainy, but the compounding of individually reasonable decisions into a disaster nobody chose.

Three qualities make the corpus unusual for a game setting:

1. **The cosmology is load-bearing, not decorative.** The world runs on a rigorous
   phenomenological metaphysics (rendering, threads, the Ein Sof) that is enforced as *mechanical
   constraint*, not flavor — down to a banned-vocabulary list an audit script could check.
2. **The factions are a philosophy survey welded to real state-formation history.** Each carries a named
   ethical framework (Aristotelian virtue, Kantian deontology, consequentialism, Rawlsian justice…) and a
   named historical template (Hanseatic League, Avignon papacy, Jarl confederacy…), and both are threaded
   into the mechanics.
3. **The corpus is already reaching for the quantitative bridge this compendium serves.** Its NPC engine
   turns "what argument would change this person's mind" into a playable contest with permanent memory;
   its factions' ethical philosophies were *deliberately demoted from mechanics to pure narrative tags
   "for prose-writer continuity"*; its research program extracts **~230 explicit "=> Valoria design hook"
   lines** from real governance history. The bridge is half-built. Part VI maps the rest.

---

## Currency caveat (read before mining any specific number)

This assessment is deliberately altitude-agnostic about ratification status — but the platform it feeds
must not mistake vivid provisional material for settled canon. The load-bearing caveats:

- **The Solmund mythology docs are mostly DRAFT/PROVISIONAL.** Only `narrative_voice_canon_v30.md` is
  CANONICAL, and it descends from a different lineage. The richest cosmology in the repo currently has
  **no `CURRENT.md` row at all** — it is invisible to the repo's own currency index.
- **The `arcs/` corpus is hand-authored *illustrative sample* content** (~13 structural shapes dressed as
  138 arc instances), explicitly superseded as the *generative model* by the ratified **Churn Engine v2**
  (`designs/audit/2026-07-05-emergent-narrative-engine/`). Treat the arcs as a tone/quality bar and a
  verified library of interaction patterns — **not** as literal content to quantify.
- **Two "why factions act" models coexist unreconciled** — the named-ethical-framework labels in
  `faction_politics_v30.md` vs. the PP-686 Mission/Cascade/Public-Expectation/Legitimacy model in
  `faction_behavior_v30.md`, which explicitly retires the labels. `CURRENT.md` does not flag the tension.
- **Varfell's "Path B" victory is struck by GD-1** (peninsula-only victory), though its Warden Recognition
  relationship track survives in the cross-cutting clock registry (`clock_registry_v30.md`) — and is itself
  flagged "DRIFTED" (a naming collision) in a later coherence audit.
- **The settlement/territory scale is mid-refactor** (the 2026-07-13 "B12" ruling introduces a new
  Territory→Province tier not yet fully executed).
- **A metaphysics-vs-"no-GM" seam is unresolved** in the source itself (see Part I §1). Several scenarios
  still route a decision to "GM discretion" in a game whose premise is that there is no GM.

Where a section leans on provisional or superseded material, it says so. Resolve any number crossing into
the engine via `CURRENT.md` → the prose head → the cited `PP-`/`ED-` per CLAUDE.md §5, never from this
compendium directly.

**On quotation (added after an adversarial fidelity pass):** passages in quotation marks are drawn from the
cited source, and the large majority verify verbatim — but the review found a minority had been lightly
compressed, stitched across sentences, or reworded while kept inside quote marks. Every such instance the
pass surfaced has been corrected; still, treat any single-sentence quotation here as *close to* the source
and re-verify exact wording against the head before citing it onward as verbatim canon language.

---
---

# PART I — THE WORLD

## 1. The philosophical spine (the design DNA)

Beneath the map and the politics sits a compact, rigorous metaphysics in `canon/00_philosophical_foundations.md`,
condensed into loadable rules (`_rules.md`) and a binding constraint table `canon/02_canon_constraints.md`
(**P-01 through P-15**, each row carrying a citation, a mechanical implication, and an explicit
violation test). This is the deepest layer of Valoria's identity, and its worldview is a specific,
unusual synthesis: **phenomenological idealism about experience + hard physicalism about consequence +
anti-moralism about monstrosity + tragic (not conspiratorial) causation + trauma-as-dignity.**

The load-bearing principles, in plain terms:

- **P-01 Inseparability.** A "thread" has three aspects — temporal, epistemic (intelligibility), and
  actualized — and *"to move one is, necessarily and inescapably, to move all."* No clean, single-axis
  operation is ever possible. This is the axiom the whole mechanical system obeys: every act on the world
  resolves with automatic co-movement across all three axes, with no discretion to skip one.
- **P-03 Rendering is consciousness-performed.** Reality's substrate is threads; experience is the
  *rendering* of those threads by consciousness — *"the way the world is given to consciousness… what minds
  do, not an external mechanism."* Information asymmetry between the thread-sensitive and everyone else is
  therefore *the* core mechanic, not an overlay.
- **P-02 / P-04 Monstrosity is ontological, not moral.** Monstrous things are grounded positively in a
  *surfeit of being* from the **Ein Sof** (the Kabbalistic "without end," adopted as infinite positive
  being, not a void) and the Lacanian Real — never in evil, sin, or moral negativity. There is no
  alignment system by construction; a monster is *"a rendering failure,"* not a villain.
- **P-07 The Calamity is rendered-side.** The catastrophe that made the world was engineering failure, not
  divine wrath: *"The ground does not 'respond' or 'fight back.' The fabric strains and tears."* This is a
  deliberate genre choice — a reactor breach, not a curse.
- **P-08 The epistemological barrier is inaccessibility, not suppression.** Non-sensitives can recite facts
  about the deep world but cannot comprehend them — *"like reading the notation of a symphony without ever
  having heard music."* No amount of study crosses the gap.
- **P-10 Coherence.** The integrity of a being's continuous self-rendering — *"not spiritual strength, not
  moral standing, not willpower"* — and, strikingly, **intersubjectively verifiable but not
  introspectable**: *"the apperceptive self-presentation that is failing is the same one that would be
  required to perceive the failure."*
- **P-15 Three-layer being-persistence** (from the self-rendering amendment). You persist via (1) Ein Sof
  spooling, (2) unconscious self-rendering, (3) deliberate threadwork; the **Leap** briefly suspends layer
  2 (hence its vulnerability window). At Coherence 0 the outcome forks by Thread Sensitivity into four
  qualitatively different fates — *Ontological Freefall* (30–49), *Relational Persistence* held together
  only by one's Knots to others (50–69), *Structural Reconstitution* (70–89), and *Full Reconstitution and
  Reality Strain* (90–100), where a single being's continued existence strains the substrate the way the
  whole Einhir network once did.

Some of the finest writing in the repo lives here, in §4.3's reframing of trauma as **constitutive
finitude** rather than damage. Confrontation with what exceeds the rendering produces a signature
*"structurally indistinguishable from clinical trauma"* — and the text insists this is not failure:

> *"A cup pouring the ocean: the cup has not failed. The cup holds what cups hold. The water that does not
> fit does not fail to enter because the cup was defective… What is not cup-shaped and cup-sized does not
> become contained by failing-differently; it does not become contained at all."*

This single image should govern the *tone* of any interface around Coherence damage or "sanity" feedback:
dignifying, not punitive. It is the clearest statement of the setting's moral posture — the world is
tragic, but its people are never pathologized.

Two further pieces of the spine matter for design. First, the **operation taxonomy**: threadwork is
**Restorative** (substrate-aligned, *zero inherent Coherence cost — structurally, not as a balance
choice*), **Manipulative** (cost ∝ scale × deviation), or **Destructive** (catastrophic). Second, the
**scale-invariance** claim: a single Coherence-0 practitioner straining the substrate and the
civilization-scale Einhir Catastrophe are, in the foundations' words, *"identical in mechanism… reduced in
scale"* — *"The physics is the same."* One
formula spans the individual quest and the world's history — and any sufficiently powerful, sufficiently
broken NPC is a walking proto-Calamity, a built-in emergent-quest generator the canon implies rather than
invents.

**The unresolved seam — and it is the single highest-value open question in the corpus.** P-03 says only
minds render, and its own text glosses the implication in tabletop terms: *"GM is the rendering engine."*
But Valoria's premise is that **there is no GM — the engine resolves everything.** An engine is not a
mind. The foundations never reconcile whether the Godot engine is now claimed to "render" (which the
metaphysics as written would forbid) or whether the **player's** consciousness is the renderer and the
engine merely computes the substrate facts presented to it. Every downstream "GM discretion" escape hatch
(the Consecration Crisis; several NPC arcs) inherits this seam. It is not a flaw to paper over — it is a
genuine design fork the platform must choose deliberately.

Distinct from the metaphysical constraints (P-01–P-15, immutable) is a separate, mutable, project-owner
track — **GD-1/GD-2/GD-3** — which encodes producer directives: one universal victory condition
(Peninsular Sovereignty), deterministic mandatory-action precedence, and the Revolt→Insurgency→Faction
pipeline. Do not conflate these with the philosophical DNA; they are Jordan-ratified and Jordan-changeable.

## 2. Solmund: the mythology and the founding error

The setting's sacred center is **Solmund** — a *"threadcut being of the third mode"* who *"emerged through
the Gaps opened by the Einhir Catastrophe — a fully configured being from the unintelligible ground,
organised and self-aware."* He was not born and did not develop; he arrived *whole*, and chose to render
himself stable enough that human consciousness could perceive him as a person. The docs are emphatic,
almost liturgically so, that his motive is categorically unknowable: *"He chose. We cannot know why."*
This is not a lore gap awaiting fill — it is asserted as **the boundary of rendering encountered at its
deepest point.** Unknowability is the theology's foundation stone.

He ministered roughly seven perceivable years (of twelve total), moving through the Crown heartland and
north — deliberately *away* from the devastated Southernmost where surviving practitioners were
concentrated — and then **dissolved** at Year 0 of the calendar (which counts "AG," *After [Solmund's]
dissolution*): not death, but *"the threadcut being releasing its hold on actualization and returning to
the unintelligible ground from which it emerged."*

The mythology's genius is that **it is a founding-error machine.** The Church of Solmund was *catalyzed,
not designed* (canon draws the comparison directly to Jesus/Paul and the Buddha/Vinaya). Because Solmund's
witnesses were overwhelmingly non-practitioners — people who *"saw a man… who could do impossible things"*
— the scripture they built is **phenomenologically accurate but categorically miscast**: true reports,
wrong framework. And the orthodoxy that resulted doesn't merely fail to teach the truth; it
*cognitively forecloses* the very perceptual capacities needed to develop Thread Sensitivity at all. This
is the **Perceptual Prophylaxis**: *"the most devout adherents are the most thoroughly immunised — not
through active suppression of a faculty they possess, but through formation into a perceptual orientation
that makes the faculty's developmental preconditions unavailable."* Solmund's story is, at root, **a true
miracle producing a truth-proof institution** — and the Church is *"reliving its founding error"* in the
game's present tense every time a new Miraculous Event is captured and mis-interpreted (the throughline
the docs name "The Solmund Repetition").

Three of the mythology's structural moves are worth singling out as design-grade:

- **Inverted heresy.** In the Two Witness Traditions, it is the *accurate* accounts that got suppressed,
  *"because accuracy reveals the mechanism, and the mechanism reveals that the Church's cosmology is a
  rendering applied to something the rendering cannot contain."* Truth is the crime.
- **The Triple Interpretation** — philosophy converted directly into faction conflict. A Miraculous Event
  is read three internally-consistent, mutually-incompatible ways: the Church sees grace returning;
  Hafenmark/Baralta sees divine communion rewarding action; the Restoration/Varfell sees Einhir heritage
  vindicated. *"Each interpretation is internally consistent. None requires falsehood. Each requires
  ignoring one piece of evidence the others supply."* This is a three-faction gameplay lever with no seams
  showing.
- **The refusal to resolve Solmund morally** — stated as an explicit authorial commitment: *"The reveal of
  Solmund's non-human nature does not resolve into 'he was bad all along.' This refusal of narrative
  resolution is the framework's stance."* It forecloses the cheapest possible ending and commits the
  setting to living with an unresolved center.

## 3. The sacred idiolect — vocabulary, seam-texts, and artifacts

Few settings give you their *language of belief* this precisely. The Solmund corpus stratifies its whole
vocabulary by orthodoxy (`solmund_master_document.md` §16):

- **Orthodox:** *the Weaving* (creation), *the Loom* (the world), *Thread*, *Pattern* (divine order),
  *the Wound* (the Southernmost), *Solmund's Hand* (providence), *the Unravelling* (sin), *Certainty*
  (faith), *the Rendering* (Solmund's gift to consciousness).
- **Suppressed / heterodox:** *the Ground* (the Ein Sof by another name), *Spooling*, *the Waterline* (the
  boundary of the intelligible), *the Oscillation*, *the Dark*, *the Excess*, *the Leap*.
- **Forbidden (heresy-investigation risk):** saying *"Ein Sof"* by its own name, using *"Einhir"* as a
  theological term, and *"Ungrund"* — the groundless ground, *"maximum heresy."*

That third tier is a genuinely sharp move: **naming the setting's own real metaphysics aloud is a crime
inside the setting.** A character who says "Ein Sof" instead of "the Ground" has committed a legible,
trackable act of heresy — a qualitative fact with an obvious mechanical hook.

The standout invented artifact-form is the **Seam Text** — a passage of ordinary orthodox scripture where
the witness-testimony breaks through the theological overlay, legible only above Thread Sensitivity 30.
The worked example is one of the strongest passages of prose in the corpus:

> *"And Solmund came to the village where the well had gone dry… the water returned. Not as rain returns —
> from above, falling. The water returned from below. It rose as if the ground remembered holding water and
> held it again. And the village elder said: 'He did not command the water. The water was already there. He
> only —' and the elder could not finish, because the word he needed was not a word any of us possessed."*

Crucially it is a **comprehension gate, not a visibility gate** — a high-TS reader sees the identical
words; they simply cohere with lived experience they now possess. Nothing is hidden; everything is
misunderstood by design. (This is a near-cousin of the epistemic mechanic in *Return of the Obra Dinn* and
*Outer Wilds* — content unlocked by the player's own accumulated understanding, not by new data.)

The **artifact taxonomy** (`solmund_artifacts_v30.md`) names a whole material culture: the *Weavings of
Solmund* (scripture), the *Hours of the Loom* (liturgy — morning is new thread, evening is the day woven
into fabric), *Graduation Texts* (school pieces that build rigorous architecture then confess its
insufficiency — *"dangerous students: the ones whose final section is too convincing"*), *Einhir Fragments*
(scraps in folk songs and craft gestures), the *Restoration Memorial* (bare lists of names, no argument),
and the rarest, the **Halt Text**: *"argument proceeding to failure, marking failure, stopping. Silence IS
conclusion."* This is worldbuilding-through-form, and it is unusually generative — each artifact type is
already a content template.

## 4. The narrative voice — how the world sounds

Valoria has two voice canons at different altitudes. `solmund_voice_v30.md` is the *in-world* register
bible: it keys prose style to a character's **Certainty** score, assigning named real-world authors as
tonal registers (a rare case of a voice bible precise enough to drive procedural or LLM-assisted
generation):

| Certainty | Register (named authors) | Feel |
|---|---|---|
| 1–2 | Böhme; plain speech | rejection / indifference |
| 3 | R.S. Thomas; early Levertov | faith as habit without conviction |
| 4 | Di Cicco; folk/vernacular | faith as lived cultural architecture, unexamined |
| 5 | Hopkins; Ficino; Eliot | intellectual/sensory commitment — "the world is evidence" |
| 6+ *with TS 30+* | John of the Cross; Teresa of Ávila | doctrine true but insufficient — paradoxically closest to heresy |

Register even flips grammatically on doctrinal position: **orthodox texts run first-person-plural or
second-person** (*"we who stand in the light"*) — the theology is communal — while **heterodox texts break
into the first-person singular; "the break from 'we' into 'I' is the first sign of theological dissent."**
That is a stunning, tiny, quantifiable tell: dissent detectable at the level of grammatical person.

The one genuinely CANONICAL voice doc, `narrative_voice_canon_v30.md`, governs the game's chronicle layer
and reads like a style constitution. Its most useful content is its **negative space** — "What the Voice
Does NOT Do": never use system terms inside an in-world POV; never announce themes (*"Themes emerge from
event and image"*); never pity characters (*"It accompanies them"*); never resolve into a single ground
truth (*"The voice tolerates aporia"*); never *"perform its own secrets"* (hidden abilities are discovered
through *accumulated discrepancy across scenes*, never by the prose winking); and — the most elegant
single instruction in the corpus — never render a Coherence-0 entity as broken *or* transcendent, but as
**"the competent monstrous"** via **"observing-around"**: describe the effects, never the interiority, so
that *"the gap between the observation's precision and the being's resistance IS the rendering."* That is
a complete, reusable solution to writing the incomprehensible without cheapening it.

## 5. The land — a peninsula wedged between an empire and a wound

Valoria is *"a peninsula defined by what it is attached to and cut off from"* (`geography_v30.md`): a
north–south strip barred from the Empire of Altonia by an impassable east–west mountain range to the
north, narrowing southward to terminate at **the Southernmost** — the epicenter of the Einhir Catastrophe.
The body politic is squeezed between two things it cannot control: a hostile empire above and an
unspeakable wound below.

The land is regionally coded onto explicit real-world analogues, and geography *authors political
temperament* rather than merely decorating it:

- **Hafenmark (NW Highlands) — "Swiss in character."** Landlocked, mineral-rich, glacial lakes, no coastal
  escape; *"concentrated Altonian oversight… produced a cultural emphasis on institutional order,
  procedural compliance, and constitutional governance."* Colonial claustrophobia is given as the *cause*
  of Hafenmark's proceduralism.
- **Varfell (Western Fjords) — "Norwegian in character."** Deep fjords, isolated sea-linked communities,
  commercially cut off from the east coast because there is no route around the south.
- **Crown heartland (Eastern Lowlands) — "Italian in character."** A major river through Valorsplatz to the
  eastern sea; fertile floodplain, accessible coast — the breadbasket-and-capital axis.
- **The Southernmost** — no cities, only Einhir ruins and hazard-zones; the Calamity epicenter.

The load-bearing thesis of the map is that **nationhood here is military necessity, not sentiment**:
*"Neither half of the peninsula is defensible alone against Altonia. The peninsula is one country because
geography demands it."* Several individual features do real dramatic work:

- **Himmelenger, the accidental kingmaker.** The Church's cathedral city sits at the most-connected node on
  the board *specifically because* Altonia placed it *"on the mountain ridge between the passes where it
  can be monitored"* — a colonial containment cage that became the political crossroads. The map's own open
  items flag it bluntly: *"Himmelenger (Church) at 5 connections is kingmaker territory."* The irony is
  baked into the geometry, not the lore.
- **The Maritime Forgetting.** There is no reliable sea route around the southern tip, so *"Varfell
  perceives this as Crown/Schoenland trade conspiracy — the rational explanation (Calamity blocks the
  route) is literally unrememberable without Thread Sensitivity."* An entire faction's grudge is
  *canonically wrong and permanently uncorrectable*, because the true explanation is metaphysically
  inaccessible. Geography generates a structurally unresolvable political grievance.
- **Church strength and Restoration strength are complementary gradients** radiating from opposite anchors
  (Himmelenger in the north-central ridge; the wound in the south). Every territory sits somewhere on the
  interpolation between orthodoxy and the suppressed old culture.

## 6. The calamity and the Forgetting — the world's mood

The **Einhir Catastrophe** (~12 years before the calendar's zero) was a mass working gone wrong: a
peninsula-spanning practitioner network attempted a foundational-scale correction, and *"at the moment of
maximum actualization pressure, the configuration inverts,"* releasing every accumulated thread at once,
tearing Gaps of unprecedented scale, birthing Solmund, and collapsing the civilization. Per P-07 this is
*engineering failure, not divine punishment* — closer to a reactor breach than a curse. Its three
surviving zone-types are each a distinct mode of failure, described with real economy:

- **Locked zones** — *"Threads frozen at the exact moment of catastrophe. Cities stand intact. Bodies are
  undecayed. The Einhir moment is preserved in amber."* (A Pripyat-frozen-in-time image.)
- **Oscillating zones** — *"Threads cycling without rest… Continuous Gap formation. The most dangerous
  zone-type."*
- **Snapped zones** — *"Threads wound to maximum potential. Objects crumble on contact."*

The calamity's signature — and one of the most distinctive ideas in this slice of the corpus — is **the
Forgetting**: the Southernmost's danger *cannot be rendered* by those without Thread Sensitivity, because
*"the threads encoding the nature and scale of the danger are too close to the unintelligible ground to
hold stable in consciousness — so they are simply not retained. This is not a psychological defence or a
failure of courage."* And the mechanic built on it is a beautiful inversion of the trauma-testimony trope:

> A **Testimony Ob penalty** applies to non-practitioners citing Southernmost knowledge — *and it
> decreases with exposure depth*, so those who have spent more time in the wound are *more* credible,
> *"because the Forgetting mechanism leaves emotional weight even when it strips content, and that weight
> reads as conviction."*

The world's mood is unusual for the genre. It is not the dread of imminent apocalypse; it is **the low,
generational ache of an old catastrophe that a whole society has structurally organized itself around
managing rather than solving** — closer to a civilization built around a permanent exclusion zone than a
ticking bomb. The hard-numbers backbone (`ms_trajectory_v1.md`) tracks **Mending Stability climbing from
5 at the Catastrophe to 72 ("Strained") at game start**, over 257 years, front-loaded (most recovery in
the first 50 years, driven by Solmund himself and the earliest Warden survivors) — a wound healing on a
geological clock, never closed within a campaign, and prose-constrained by P-07 to describe recovery
without ever saying the world "heals itself." The radiation *"creeps inward from the periphery… The Seat
is the last to feel the Catastrophe's reach"* — so any campaign-scale decline tells its story
geographically (border settlements slide first) before it tells it politically.

## 7. The canonical timeline — a colonial inheritance

The history (`canon/03_canonical_timeline.md`) is a tight, cited chronology, and its dramatic engine is
**colonial inheritance and its blowback**:

- **Pre-Collapse:** the Einhir civilization runs the Southernmost site-network stabilizing the world's
  ontical base; later Altonian administration imposes three provinces whose boundaries *"do not correspond
  to any recoverable pre-Calamity political geography"* — the seed of the modern duchies.
- **The Deterioration → the Catastrophe** (~12 years pre-0): the network fails; blame settles on the
  southern practitioners who ran it, *"surviving Altonian colonial rule and formalising into the
  post-independence caste system."*
- **Solmund** (~5 AG–0 AG) → **Church Formation** (0–200 AG), catalyst-to-institution over two centuries.
- **Altonian colonial period & Church containment** (~50–200 AG): Altonia grants the Church its walled
  city-state in exchange for quiescence — *explicitly modeled on the British Raj's management of
  Hinduism/Islam* — producing, over 200 protected years, *"the most institutionally mature organisation on
  the peninsula."* Modern Church strategy is this logic in reverse: **"The cage became a school."**
- **The Secession Wars & Settlement** (~195–200 AG): a northern-led coalition defeats Altonia; the first
  Almqvist wins the throne *purely through wartime deeds* (no bloodline survived Altonia's record
  destruction) and is Church-consecrated — *"the Carolingian model. Pepin received papal legitimation."*
  The **caste system** is *"the structural consequence of the south's exclusion from the war coalition's
  leadership,"* reinforced by both political convenience and genuine post-Catastrophe fear.
- **Game era** (200–245 AG): the first Almqvist dies in ~218 AG in a hunting accident *"widely suspected
  assassination, perpetrator deliberately undefined"* (a live succession-legitimacy mystery, editorial item
  E-01). His son **Almud** ascends unproven, spends his reign *"proving the presumption warranted."*
  **Game start is 245 AG:** MS 72 ("Strained"), Church Influence 22, Institutional Pressure (IP) 20
  ("Dormant").

## 8. Assessment — the world

**Standouts.** The world's narrative quality is high and, more importantly, *coherent*: a single tragic
thesis (govern-or-survive) is expressed at every altitude, from the cup/ocean image of individual trauma
to the peninsula-is-one-country-because-geography-demands-it logic of the map. Four elements are
genuinely original rather than genre-standard: the **Forgetting** (and its credibility-inversion
mechanic); the **Perceptual Prophylaxis** (a religion that immunizes its faithful against perceiving the
truth); the **Seam Text** (comprehension-gated, not visibility-gated, revelation); and the
**scale-invariant** treatment of the Calamity as a *renewable* hazard rather than a one-off. The voice
canon's "competent monstrous / observing-around" instruction and the Certainty→author register table are
the two most directly usable pieces of craft in the corpus. The Kabbalistic and phenomenological
substrate (Ein Sof, tsimtsum, Husserlian rendering) is deployed with unusual rigor for a game.

**Gaps and live faults.** (1) **The no-GM seam** (Part I §1) is the highest-value unresolved question and
sits unaddressed in the source itself. (2) **Currency is a real problem for a platform doc**: the richest
mythology (the Solmund corpus) is DRAFT/PROVISIONAL with no `CURRENT.md` row, and carries at least one
citable internal contradiction (the master doc still uses two Kabbalistic source-registers, ibn Gabirol
and Abulafia, that the voice-canon split says Jordan *rejected* on 2026-04-25). (3) **Terminology drift**
persists (an infill co-file still uses the retired "Rendering Stability" where its skeleton says "Mending
Stability"; the P-07 constraint text still says "TT"). (4) **The setting's own central endgame ritual is a
placeholder** — the canonical method for stabilizing the wound is referred to throughout as
`[NAME-PENDING]`. (5) **Altonia and Schoenland are pressure-systems, not casts** — richly instrumented as
invasion clocks, but nearly devoid of the named-character texture lavished on the peninsula. These are the
predictable unevennesses of a deep in-progress corpus, not conceptual failures; none undermines the
world's identity, and each is a concrete, bounded authoring target.

---
---

# PART II — THE FACTIONS

## 1. The shape of the political contest

The strategic layer is a **post-colonial recovery narrative wearing a grand-strategy skin**, and its most
important design decision is that it is *structurally hostile to conquest*. The peninsula is 35 years out
from independence, with living memory of the occupation, and — per `peninsular_strain_v30.md` —
*"military conquest across the peninsula recreates the Altonian pattern of domination; the population
resists it."* Territory taken by force starts at **Accord 1 (Resistant)** and contributes *nothing* to
victory until it is governed into consent: *"The cost is in the holding, not the conquest."*

Two rulings shape the whole contest. First, **there is exactly one way to win** (GD-1): **Peninsular
Sovereignty** — hold all fifteen territories at Accord ≥ 2, Turmoil ≤ 6, for two consecutive Accountings.
Every faction-specific "victory" that used to exist is explicitly demoted to *"a description of each
faction's asymmetric approach to territorial acquisition"* — and, in the victory doc's separate phrasing,
"not an alternate endpoint." The single win
condition means **the only way to win is to govern well enough that the whole peninsula consents.**
Second, **equal win probability across factions is a stated axiom** (BALANCE-001): no faction's identity —
theocracy, monarchy, mercantile duchy, insurgency — is intrinsically favored by the ruleset. Asymmetry is
in the *approach*, never the odds.

And — a mark of real maturity — **failure states are not endings.** *"No shared loss. No fade to black.
Every crisis becomes a new chapter."* Mending Stability hitting zero triggers the **Rupture Scene** (the
player must publicly declare their Belief, cite one action that expressed it, and say whether they would
do it again) and continues into a **Post-Calamity Era**; maxed invasion pressure opens a reversible
three-phase **Occupation Era**; total faction collapse opens an **Anarchy Era**. The only true terminal is
a *second* Calamity, requiring ten straight seasons of total failure. There is a quietly moving argument
buried in the design: *"A player who has been building Knots and Mending for 20 seasons is now the most
powerful actor — not from a power boost, but because the institutions that dwarfed them have collapsed."*
Patient, unglamorous work outlasts institutions.

## 2. The dramatis personae of power

Canon fixes the **starting faction count at four** (the 2026-07-13 ED-IN-0047 ruling): the Crown, the
Church, Hafenmark, and Varfell — with an explicitly *intentional* emergent-faction space (the Restoration
Movement, Löwenritter-style splinters, and an "Altonia-usurper" archetype). The full political ecology:

**The Valorian Crown (Almqvist dynasty) — the deed-monarchy.** *"Legitimacy is the continuously
demonstrated act of governing well, not divine right or pure heredity."* The founding Almqvist earned the
throne in war; every successor must *re-earn* it each season. Ethical framework: **Virtue** (public,
visible, honorable action is rewarded; covert action is penalized). Its institutional voice is exact:
*"The realm is what we hold together against all who would take it. / Authority that is not earned this
season is not authority next season."* The design's sharpest observation about the Crown is that it is
*"the campaign's central locus of structural tension"* — it starts with the **highest** Mandate and Wealth
yet is **structurally the most fragile**, because *every* other actor holds a live grievance against it
simultaneously (Altonia, Schoenland, Restoration infiltration, the Church's sovereignty claim, Hafenmark's
rivalry, Varfell's ambition, and its own army's coup track). *"The fragility is structural, not
stat-based."*

**The Church of Solmund — the theocracy.** *"The institutional rendering of Solmund's revelation."* Led by
**Confessor Arne Himlensendt** through a **Four-Cardinal structure** — Fortitude/Military (Jarnstal,
Templars), Justice/Judicial (Olafsson, Inquisitors), Prudence/Economic (Tormann), Temperance/Knowledge
(Klapp) — from the sovereign city-state of **Himmelenger**, *"analogous to the historical Vatican."*
Ethical framework: **Faith**. The corpus's single best character-sentence belongs to its leader:
*"Himlensendt is sincerely devout, not cynical: his faith is the load-bearing wall of the entire post-war
settlement, and that is exactly what makes him the most dangerous person on the peninsula."* The Church is
the strongest *substrate-suppressor* in the setting — it actively renders Thread perception as
heresy-or-illusion — and its whole political arc runs on Church Influence (CI), whose one-shot endgame gamble
(Mass Seizure at CI 100) is modeled by a genuinely elegant restraint-breaking curve, `P(declare) =
((CI−60)/40)^3.3`, that goes from 1% at CI 70 to *forced* at CI 100.

**Hafenmark — the constitutional / mercantile duchy (Hanseatic).** A parliamentary commercial duchy where
*"rank advancement is formal confirmation by legislative vote"* and a Burgher is physically inscribed on a
*"Roll of Burghers… in the Gransol Parliamentary Archive."* Led by **Duchess Inge Baralta**, whose
**Sovereign Authority Doctrine** asserts her rule derives directly from divine grant *"superseding Church
jurisdiction"* — an explicitly Henry-VIII-coded supremacy claim. Ethical framework: **Categorical
Imperative** ("rules that must apply universally… follow procedure even when it costs you"). *"Baralta IS
the institution,"* which is both her structural strength (Leadership Deviation Ob 1, the lowest of any
leader) and, as Part III shows, her deepest vulnerability.

**Varfell — the Jarl Confederacy (Old-Einhir / Norse).** A confederation where **Duke Magnus Vaynard, "the
White Wolf,"** is *"first among the Jarls,"* not a monarch, ruling from **Sigurdshelm**. Its legitimacy
logic is explicitly *"the Varangian Guard's role in Byzantine acclamation politics — the Assembly creates
the legitimacy it affirms."* Ethical framework: **Utility-driven Pragmatism**, given the most vivid
doctrine note in the corpus: *"cunning in service of pride — Vaynard presses every available advantage but
refuses anything publicly seen as cowardly. Acceptable register: classical battlefield stratagem (Hannibal
at Trasimene, Belisarius reading Persians, Mongol envelopment, oblique order, calculated retreat).
Unacceptable register: assassination, civilian targeting, breaking parley, sneak-thievery."* Varfell's Intel
advantage expresses as *"Talleyrand-style diplomatic intelligence, not espionage."* Vaynard secretly keeps
a Thread-artifact hoard — **the Private Collection** — and carries dormant Thread Sensitivity that climbs
with use.

**The Guilds — the economic bloc.** A rotating **Guildmaster Council** (Comptroller Annika Feldhaus),
ethical framework **Moral Relativism**: *"powerful as an economic bloc and weak as a political actor. They
cannot project unified political will."* Pointedly, the Guilds *benefit economically* from caste
suppression and are only selectively caste-open.

**The Restoration Movement ("The People's Revolution") — the reformist emergent.** *"No formal leader — a
movement,"* later crystallizing on **Yrsa Vossen + Aldric Hann**. Ethical framework: **Equity Social
Contract** — Rawlsian, *"evaluated by whether they would be chosen from behind a veil of ignorance."* Its
partial-sheet is thematically loaded: *"No Mandate (rejects the legitimacy of the system that confers
Mandate). No Military. No Wealth (operates through informal economies)."* Its founding pathways are
modeled explicitly on **Bolshevik 1917** (concentrated) vs. **1848** (distributed). Its deepest secret is
that its caste-justice folk culture is, mechanically, *surviving pre-Catastrophe Thread technique it does
not recognize as such* — a "substrate-heritage reclaimer, unknowingly," facing an eventual forced choice:
**Embrace / Denial / Schism**.

**The Löwenritter — the military order (the Crown's arm, pre-coup).** *"Not an independent political
faction — an institutional instrument of the Crown… loyalty is to the Crown as an institution, not to any
specific monarch."* Grand Master **Ehrenwall**; five arms including the covert **Riskbreakers** (whose
hidden Conviction is *Valoria the concept*). Its central drama is a **Graduated Autonomy track**
(Loyal → Restless → Autonomous → Split) — a slow-motion coup against the very Crown it serves, and the
design frames it not as treason but as *"the system working as designed"*: the deed-logic's own
enforcement mechanism.

**Infrastructure and spoilers.** The **Ministry of the Peninsula** (Registrar Lennart Haelgrund;
Administrative Proceduralism) is *"infrastructure, not a faction,"* guarding the **Deep Archives** —
*"pre-Catastrophe records containing inconsistencies… a Thread artifact."* **Niflhel**, a four-armed
shadow network (Dockworkers / Reckoners / Burned / Quiet), was **dissolved** and its function redistributed
to settlement-layer brokers — a deliberate anti-personification choice that leaves genuinely evocative
underworld texture orphaned (see §8). **Schoenland**, a neutral island trade republic, is the classic
mercantile spoiler: *"pro-war (arms sales), anti-conquest (benefits from feuding, not resolution)."*
**Altonia** looms as pressure rather than cast.

## 3. The caste substrate — identity with teeth

Beneath every faction runs the peninsula's **caste system**, framed explicitly as **Altonian colonial
residue, not indigenous**: unstigmatized Northern and Central Einhir vs. **Southern Einhir** (concentrated
near the wound — higher baseline Thread Sensitivity, lower Church penetration, *"structurally excluded
from the post-war settlement"*). This is the most mechanically serious "identity has consequences" design
in the corpus — it is not flavor, it is threaded through *every* rank ladder, the Renown track, and a
dedicated Conviction-crisis arc. Southern Einhir characters carry +1 Ob on most Initiation Duties,
per-NPC Disposition-floor penalties (Himlensendt starts at −1, the Inquisitor-Cardinal at −2), **halved
public Renown** in Northern/Central territories, and a mandatory **Conviction Reformation arc** if they
publicly cross caste lines. But the design gives the stigmatized the *narrow* paths to power the
"legitimate" institutions foreclose: the **Riskbreakers, Niflhel, and the Wardens of the Thread**
reverse-privilege them, because outsider status is *"a covert asset"* — and the Wardens are *"effectively
the resistance infrastructure for the caste system's victims."* Crucially, `franchise_v30.md` gives caste
*territorial* teeth: a per-territory **parliamentary weight (0–5)** means Southern-Einhir territories'
*"delegations are taken less seriously"* — the demographic *"the post-war settlement was built to
marginalize"* — turning Vaynard's motive to break the caste system into a concrete strategic objective. It
is, structurally, a mechanized **rotten-borough** apportionment.

## 4. The rank ladders — institutions you climb

Every primary faction runs an eight-position **Standing 0–7** ladder, specified across the same eight
dimensions the docs call **"the Skyrim Eight"** (Title, Initiation Gate, Access, Obligations, Hall Tier,
Livery, Mentor, Demotion) — an explicit, repeated citation of *The Elder Scrolls V*'s guild questlines.
Standing 0 is pre-initiation (*Petitioner, Stranger, Catechumen*), and each faction's Standing-0→1
**Initiation Duty** is a founding-myth-flavored first scene: Crown *"Carry the King's Word,"* Hafenmark
*"File the Petition,"* Varfell *"Answer the Muster,"* Church *"Witness the Solmund Codex."* The four
ladders speak four different institutional languages:

- **Crown:** Petitioner → Retainer → Crown Agent → Banneret → Crown Lieutenant → Seneschal → Inner Prince →
  Regent-Designate. Standing 3 grants **the Banner** — a physical faction-token (+1D Intimidate / −1D
  Subterfuge while displayed).
- **Hafenmark:** Petitioner → Advocate → Burgher → Alderman → Parliamentarian → Parliamentary Chair →
  Chancellor → Speaker-Regent. Rank above Burgher is *"a matter of public record."*
- **Varfell:** Stranger → Huscarl → Thane → Lendmann → Senior Lendmann/Hersir → Jarl → Senior Jarl →
  High Thane/Jarl-Regent. Rank is worn as escalating **torcs** — the Jarl's Crown *"a heavy gold torc
  marked with province symbol."*
- **Church:** Catechumen → Lay Confessor → Deacon → Canon → Bishop's Delegate → Prelate → Cardinal →
  Confessor-Presumptive, under Cardinal-arm color-coded vestments (red Fortitude, blue Justice, gold
  Prudence, green Temperance).

Layered on top are seven **sub-office ladders**, modeled explicitly on *"the Knight Templar historical
model — the military order reports to its own Grand Master… not to the secular king"*: the Löwenritter
Knight ladder, the covert **Riskbreaker** ladder (with its own private reputation economy — **Shadow
Renown** and **Deniability Debt**, whose Debt-7 cap forces demotion), the Inquisitor and Templar ladders
(capping at Cardinal), the Guild ladder (collective by design — Standing 6 "Grand Guildmaster" is marked
*extraordinary and normally omitted*), the four parallel informal Niflhel "Standings," and the **Warden of
the Thread** ladder — *the only ladder hard-gated by a numeric stat (Thread Sensitivity) rather than
politics.* The design intent is crystallized in one line: *"Crown rewards Virtue visibility; Hafenmark
rewards procedural correctness; Varfell rewards demonstrated results; Church rewards doctrinal coherence.
The same rank position thus carries different privileges and different costs in each."*

## 5. The faction-as-character model

Valoria encodes a faction's *personality* with real structural seriousness — and here the corpus carries
its most consequential internal fault: **two competing "why factions act" models coexist unreconciled.**

- **Model 1 (embedded throughout the ladder prose):** each faction has a named **ethical framework** —
  Crown = Virtue, Hafenmark = Categorical Imperative, Varfell = Utility, Church = Faith, Guilds = Moral
  Relativism, Restoration = Equity/Rawls, Ministry = Administrative Proceduralism — that sets Domain-Action
  Ob modifiers (aligned −1 Ob, contradictory +1 to +2). This is a near-complete survey of Western
  normative ethics mapped onto political factions.
- **Model 2 (`faction_behavior_v30.md`, PP-686):** explicitly *"eliminates philosophical-tradition
  vocabulary"* and replaces it with four interacting components — **Mission** (an authored telos with
  aligned/contradicted action categories), **Cascade** (leadership Convictions propagating down a
  supervisor graph, `effective = α·personal + (1−α)·supervisor`, with a per-institution *culture* scalar:
  Hafenmark −0.2 "rigid," Restoration +0.1 "permissive"), **Public Expectation** (six role templates, each
  a weighted vector over a 13-Conviction taxonomy; **Cascade Fidelity** = cosine similarity between what a
  faction *is* and what its role *claims* — a literal "is this faction being what it says it is" number),
  and **Legitimacy + Popular Support** (now per-settlement 0–7, aggregated into the headline **Mandate**).

Model 2 is the more sophisticated system; Model 1 carries all the named-NPC detail; neither has been
rewritten to match the other, and `CURRENT.md` does not flag the tension. (The cleanest proof of the split:
the *same* ethical-framework table is struck and marked SUPERSEDED — PP-686/ED-784 — in
`engine/params/factions/stats_1_7_scale.md`, yet stands unmarked in `faction_politics_v30.md`'s live ladder
prose.) **Notably, the surviving
disposition of Model 1 is the single cleanest instance of this compendium's whole thesis in action:** the
ethical-framework labels were formally retired as mechanics but *deliberately kept alive "as descriptive
disposition tags for prose-writer continuity"* — a mechanic demoted to pure texture, on purpose,
decoupled from math. That is the qualitative↔quantitative boundary being managed consciously.

Two further layers give factions personality without over-quantizing it. The **Nine Political Axes**
(Sovereignty, Knowledge, Legitimacy, Cultural identity, Economic control, Military authority, Information,
External threat, Ontological) are *deliberately not tracked numerically* — the corpus reserves them for "war
justification (casus belli), Domain Echo content framing, faction-foil structural analysis," with named poles
and a primary opposition each (Axis 1: Crown authority vs. Church authority;
the Ontological axis: whether the world is what it appears to be). And each faction carries a
**Substrate-Posture** — its stance toward the Thread cosmology: the Church actively suppresses; Hafenmark is
an *"unmediated sovereigntist" (Protestant position)*; the Löwenritter are a *"substrate-agnostic protector"
(Praetorian position)*; the Restoration is a *"substrate-heritage reclaimer, unknowingly."* This means the
grand-strategy layer and the setting's central mystery are the *same axis viewed from different altitudes* —
a genuinely elegant unification.

## 6. Internal politics, succession, and the opposition matrix

Faction politics is dense and historically literate. **Demotion** is banded (default −1 rank; severe 2–3;
total = Dismissal to Standing −1 with a permanent *Dishonored* flag) and jumps straight to its destination.
**Succession** is a deliberately two-stage machine (`faction_succession_split_v30.md`) that separates the
*contingent* from the *structural*: Stage 1 rolls **who leads**; Stage 2 computes a *deterministic* strength
gap G that decides **whether the realm fragments** — *"near-equal claimants partition the realm (Carolingian
divisio, the Diadochi, contested Ottoman successions), a clearly dominant claimant consolidates it."* The
worked "Vaynard Falls" example runs three claimants (the blood heir Maret Uln, a Tribune Captain with an
institutional claim, an RM-backed candidate) through the full asset-division arithmetic — a civil war
costed to the settlement.

The campaign's central human drama is the **Ruler Diamond** (`npc_foils_v30_infill.md`), the richest
cross-faction artifact in the corpus (detailed in Part III). As an *opposition matrix* it works like this:
four rulers occupy structurally incompatible positions on the post-war settlement — **Almud** the custodian
with ethical doubt, **Lenneth** who would use Crown authority to *revive* Einhir heritage, **Baralta** who
would *restructure* the settlement with the caste preserved and strengthened, and **Vaynard** who would
*demolish* it entirely. The pairings carry real texture: on Almud↔Baralta, *"An uncertain custodian might
eventually decide. A certain claimant has already decided."* On Baralta↔Vaynard, *"They are not debating
governance philosophy. They are fighting over whether Vaynard's people deserve to exist as a distinct
cultural group… But they might need each other… The instability IS the drama."* Three triangles compound it
(Succession, Einhir — *"no two can ally without excluding the third"* — and Consecration).

## 7. The strategic drama — texture rendered as world-state

The strategic layer's specific concepts are unusually good at being *felt*, not just tracked:

- **Accord (0–3 per territory)** — population consent to the current ruler — comes with an explicit
  "environmental legibility" table meant to be narrated, not stat-flashed: *"3 (Aligned): Markets are busy…
  banners fly without graffiti… 0 (Revolt): A barricade blocks the main road… armed civilians watch from
  rooftops. The market has moved to an unofficial location the patrol cannot reach."* The changeover is
  narrated at human scale: *"the baker who used to greet you by name now serves you in silence."*
- **Turmoil (0–10, global)** — war-weariness in five named bands (Peace / Tension / Fracture / Crisis /
  Collapse), with a self-aware fix (ED-743) that taxes *failure to consolidate* rather than the act of
  battle, because *"Pax stabilizes after conquest."* Treaty-binding is *"the Roman Pax expressed
  mechanically."*
- **Fractional province ownership** — a split province becomes *"Greater Gransol"* (the Seat) and
  *"Eastern Gransol"* (the fragment, compass-named), with Consolidation above 75% and Secession below.
- **Parliamentary transfer** — the same dice mechanism carrying four different *political stories*:
  Adversarial, Consensual, Punishment, and Appeasement (the last grants extra Accord *"because the transfer
  is meant to defuse, not subjugate"*).
- **Treaty expiration** — a self-critical balance patch (a punishing 90% lapse rate) that admits its own
  narrative cost outright and holds the line anyway, anchoring itself to Roman *foedera* renewed at each
  coronation.

## 8. Worked scenarios — the design showing its hand

Two set-pieces show the faction design at full quality. **The Baralta Crown Claim** turns a succession
into a formal contest and centers on the **Consecration Crisis**: if Hafenmark wins the Crown, the outcome
hinges entirely on Church Stability at that exact moment — at Stability ≥ 4 Himlensendt *refuses* to
consecrate (Baralta rules unblessed, the Church's influence spikes as its overreach becomes visible); at
Stability ≤ 3 he consecrates *under duress* (the Church is functionally subordinated for the rest of the
game). The design names its own central tension: *"needing the Church weak enough to force consecration but
not wanting CI to spike in the interim — is good design. It creates a multi-season strategic calculation,"*
with a further irony that Baralta-aligned players who weaken the Church to enable her claim are in tension
with their own interests. Its playtested pacing verdict — early claim is a trap, **Season 8–10 is Baralta's
optimal window**, late claim is a gamble — is genuine dramaturgical R&D.

**Varfell's "Path B" (Southernmost Dominion)** is the cautionary case: a richly-developed conquest-and-lore
victory path, now **struck outright by GD-1** (peninsula-only victory). It survives only as
supersession-trail evidence — but its underlying **Warden Recognition (0–4)** relationship track *survives* in
the cross-cutting clock registry (`clock_registry_v30.md`), not the faction ladders, and is itself flagged
"DRIFTED" (a naming collision) in a later coherence audit. A platform author needs to hold both truths: the
*victory frame is dead*
but the *relationship texture is live*.

## 9. Assessment — the factions

**Standouts.** The factions are the corpus's strongest domain, and their quality is *systemic*: the
philosophy-survey-welded-to-history construction gives each faction a legible worldview and a legible
historical grain simultaneously, and the caste substrate makes structural injustice a real mechanical
presence rather than set dressing. The best individual pieces are the **Consecration Crisis** (a genuine
multi-season strategic-and-moral knot), the **Franchise** system (caste turned from flavor into national
math), the **Accord environmental-legibility table** (world-state you read off the streets), the
**Substrate-Posture** unification (grand strategy and the central mystery as one axis), and the sheer
density of explicit historical grounding written into rules text (Pax Romana, Roman *foedera*, the
Varangian Guard, the Knight Templar model, Julius II vs. the Council of Pisa). The **failure-as-new-chapter**
architecture is unusually humane and unusually replayable.

**Gaps and live faults.** (1) **Two unreconciled faction-personality models** (§5) — the single most
important faction-lane debt, because "how a faction's personality is encoded" has no settled answer right
now, only a well-annotated one. (2) **Uneven finish across the founding factions**: `faction_canon_v30.md`
only carries full consolidated sheets for the Crown and the Church; Hafenmark, Varfell, the Restoration,
and the Löwenritter never got the pass, and correspondingly read flatter (no first-person "Institutional
Beliefs," no Arc Trajectories). (3) **Naming seams** — the Restoration's leadership (an earlier proposed
elder vs. the current Vossen/Hann) and the Church's Justice-Cardinal (two candidate names) are
unreconciled. (4) **Orphaned texture**: Niflhel's four-armed underworld is preserved only as legacy content
"to preserve numbering," its institutional voice handed to a single NPC. (5) **A GM-discretion escape hatch
in a no-GM game**: the Consecration Crisis routes its most interesting branch to *"GM discretion.
Himlensendt's personal faith state determines the outcome… No mechanical formula can capture this"* — a
precise, load-bearing piece of texture with, as yet, no engine-legible translation. (6) **~90% of the
richest recent research (the 44-item comparative-governance batch) is unlanded** — a live hazard (do not
present it as current architecture) and simultaneously the richest unused vein in the corpus (see Part V).

---
---

# PART III — THE NPCs

## 1. The design thesis — sincere virtue as exploitable weakness

The NPC roster runs on one formal constraint, stated as a design principle in `npc_roster_v30_infill.md`:

> *"Every named NPC except Edeyja carries a structural compromise: a conflict between personal ethics and
> faction loyalty, an exposure to Thread Sensitivity they cannot control, a behavioral flaw in their
> decision-making, or a position that makes them a spoiler target… Each NPC has a Behavioral AI Profile
> governing their autonomous decisions. The profile includes a named flaw that produces suboptimal play
> and creates consequences the players can exploit or mitigate."*

This is the roster's engine and its signature. Nearly every character is *a competent, sincere person
whose virtue is mechanically convertible into an exploitable weakness*. It is, deliberately, a corpus with
no moustache-twirling villains: the Church's suppression machinery is staffed by sincere believers, the
usurper has a coherent constitutional theory, and the revolutionary is simply *right* about the stakes.
The moral-framework tags across the roster are a real taxonomy of ethical positions — Deontological,
Rawlsian, Utilitarian, Procedural, Meritocratic, Protective-consequentialist, *oikonomia*, Stewardship —
not a good/evil axis. The result reads closer to *Malazan*'s empathy-for-every-faction or Le Guin's
anthropological even-handedness than to epic-fantasy heroics.

## 2. The dramatis personae

**Edeyja — Warden-Chief of the Southernmost.** The gold-standard character, and the *only* NPC exempted
from the compromise formula (that exemption is her dramatic function). Thread Sensitivity 75–80 (highest
living), Coherence 9; built as a mind, not a courtier. Her wound is literal and visible: she survived a
Gap that damaged her chest and shoulder, saving herself by Threadworking on her own body, leaving a scar
that *"renders unusually — texture, color, or apparent depth wrong."* She leads the last of a dying warden
lineage, and her tragedy is exact: *"functionally omnipotent within her domain and functionally powerless
outside it"* — she can perceive every faction's wars as trace damage to the substrate she maintains, but
cannot make anyone who matters understand what she protects, because the Forgetting means *"she is
maintaining a building whose occupants don't know the building exists."* Her flaw *is* her virtue at its
limit: *"Edeyja's 'flaw' is that she is correct and the world is dying anyway."* She is the fixed point the
others arc relative to: *"The question is never 'will Edeyja change?' It is 'will the world change enough
to make her job possible, or will she fail despite being the best?'"* The GM-voice summary is perfect: *"She is not hostile. She is occupied. These
are different things."*

**The Ruler Diamond.** Four incompatible visions of the post-war settlement, worked as a full opposition
lattice:

- **King Almud Almqvist** (Crown, TS 0). Second-generation deed-monarch, 27 years on the throne, competent
  patient restraint (anchor: Manuel I Komnenos, *"playing six boards at once"*). His wound is a private,
  unresolved doubt about the caste system *"he administers but does not feel,"* and his blind spot is
  precisely engineered — the foil doc notes his uncertainty "is itself a decision," that *"Lenneth sees this.
  Almud does not,"* because to him uncertainty is "the absence of a decision, not the presence of one." His administrative virtue *is* the
  caste system's chief protection.
- **Queen Lenneth Almqvist** (Crown, reformist; anchor Catherine the Great). Archivist who would make the
  dynasty *"the family that reunited the Valnese people."* Her frustration with Almud is exact: *"not that
  he disagrees — it is that he has not decided. She could argue against disagreement. She cannot argue
  against uncertainty."*
- **Duchess Inge Baralta** (Hafenmark, TS 0). The most extensively worked antagonist-pole, granted her own
  doctrinal document (`baralta_v30.md`). Triple anchor: Isabella I of Castile (patient claim-building) +
  Henry VIII (sovereign supremacy) + Theodora (*"she would ride the institution into the ground before
  admitting it was wrong"*). Her ambition is flat and unhedged — *"Baralta wants the Crown. This is active
  ambition, not contingency"* — and fearless because eschatological: *"she believes her work will be
  recognised in the afterlife… she has no need for dynastic continuity."* Her theology is a genuine
  in-world innovation — she accepts Solmund's divinity but *"questions the Church's exclusive claim to
  mediate"* — and her vulnerability is structural: *"Hafenmark without Baralta is a personality cult that
  discovers it was always a personality cult."*
- **Duke Magnus Vaynard** (Varfell). The one character the design most wants read as *sympathetic in a
  dangerous register* — anchor **Reinhard von Lohengramm** (*Legend of the Galactic Heroes*), the corpus's
  single deliberate pop-fiction template. Southern-Einhir heritage, Thread Sensitivity from environmental
  exposure. Desire: expel the Church and all Altonian cultural residue, restore Einhir heritage. Wound:
  *"The Forgetting is his political prison"* — he alone understands the existential danger, but the memory
  barrier means *"the most important argument for his entire worldview dissolves in the minds of anyone who
  cannot already perceive Thread reality."* He is *"the only faction leader who understands the existential
  crisis the peninsula faces,"* forced into secrecy and tradecraft rather than open persuasion.

**The Church hierarchy.** **Confessor Arne Himlensendt** — *"the most dangerous person on the peninsula
and does not know it"* — whose sincere faith is *"the load-bearing wall of the entire post-war
settlement,"* and whose pastoral compassion is self-undermining because outreach *"would deepen the
essentialist framework's penetration into exactly the communities where Thread Sensitivity survives. His
compassion and his suppression are the same act."* Beneath him, the four Cardinals are unevenly finished:
**Aldric Tormann** (Prudence; anchor Suger of Saint-Denis) is *"an excellent administrator solving the
wrong problem with perfect efficiency"* — his tithe-maximizing funds excellent charity while alienating
parishes into Restoration recruitment pools (*"The resentment is not in his ledger"*); the others (Klapp,
Olafsson, Jarnstal) are one evocative sentence each — Jarnstal's *"The Soldier Who Outgrew His Chain of
Command"* being a strong premise with no delivered content. Sharpest of all is **Sæmund Haelgrund**, the
field Inquisitor with Thread Sensitivity 12 *who does not know it* — anchor Bellarmine-after-Galileo —
*"the setting's most dangerous epistemological experiment"* and the source of *"the single highest-impact
personal scene in the roster"*: a TS-30+ player can Diagnose him, at which point *"the Inquisitor discovers
that he IS the thing he investigates."*

**The Löwenritter.** **Grandmaster Ehrenwall**, given one of the corpus's sharpest reframes: *"She is not a
potential traitor contemplating treason against a divinely ordained king. She is a military professional
calculating whether the current office-holder is still performing the deeds that justify the office."* Her
Coup Counter is *"the deed-logic's enforcement mechanism,"* and she would transfer loyalty to
Baralta without experiencing it as betrayal. **Halvar Brandt** (anchor Aetius, "the Last Roman") held a
mountain pass for three days twelve years ago and lost his command — *"militarily invaluable, politically
illiterate,"* his arc resolving on a question the setting may never answer (*was he right about
Altonia?*). **Sigrid Torsvald**, a covert Riskbreaker with Thread Sensitivity 35 gained by *accident*
cataloguing the Queen's archive — *"undercover from her own institution,"* her cover *"now less true than
her reality."*

**The operational tier** is where the roster's "sincere competence, fatal flaw" machine runs at full
density: **Maret Uln** (Vaynard's operative, anchor Richard Sorge) — *"a conscience operating inside a
competence structure that demands its suppression"*; **Yrsa Vossen** (RM leader, anchor Rosa Luxemburg) —
*"leading a cultural restoration movement while experiencing the cultural erasure her movement opposes,"*
*"playing the ethics correctly and losing the game"*; **Annika Feldhaus** (Guilds, anchor Jacques Cœur),
unknowingly laundering Thread-touched goods; **Peder Almstedt** (Ministry, anchor Byzantine *logothetes*)
— *"not a person who happens to work in bureaucracy… bureaucracy that happens to be a person"*; **Gerik
Strand** (Crown Lord Steward, anchor William Marshal), *"the most psychologically legible NPC in the
roster,"* whose flattery vulnerability is flagged as *"the most gameable mechanic in the roster"*; **Dalla
Virke** (broker, anchor Medici branch managers) — *"the trust IS the competitive advantage"*; **Doux
Alexios Laskaris** (Altonia, anchor Demetrios Palaiologos, ethic *oikonomia*), *"betraying the empire in
slow motion… through attachment"*; **Rikard Solberg** (Schoenland, anchor Xenophon's *Anabasis*), the
homesick functionary who is the peninsula's accidental peacemaker — *"He does not know he is doing this."*
Beyond the Diamond, one standout death: **Warden Orm** (anchor: the Chernobyl liquidators), whose Arc C
walks him to the worst Gap to perform continuous Mending until his Coherence gives out — *"a narrative
death, not a combat death"* that permanently seals a Catastrophic Gap.

## 3. Archetypes and moral range

The compromise formula yields a recognizable, reusable set of archetypes: **the double agent whose
divided loyalty is genuine, not performed** (Uln, Torsvald, Laskaris — effective *because* of the sympathy
that compromises them); **the visible martyr-in-waiting** (Vossen, and Lenneth in an institutional
register); **the system given a face** (Almstedt = procedure, Ehrenwall = the deed-ledger, Himlensendt =
sincere faith as load-bearing wall — none a schemer, all dangerous *because* they aren't); **the insecure
overperformer** (Strand); **the competent-but-uncommitted custodian** (Almud); **the merit-claimant
outside the bloodline** (Baralta); **the righteous revolutionary** (Vaynard); **the unwitting-threat true
believer** (Himlensendt, Haelgrund); **the profiteer blind to what they sell** (Feldhaus, Virke); and **the
last master of a dying order** (Edeyja, the sole exception).

The **moral range is real but formally uniform** — thirteen iterations of the same dramaturgical machine
(compromise → named flaw → numeric consequence). This is a *strength* for a game (systematic, reusable) and
a *limitation* for prose variety (there is no purely cynical operator, no purely evil antagonist). Worth
naming as a positive: the **gender range is wide and unstereotyped** — the sharpest political operators
(Baralta, Ehrenwall, Vossen, Lenneth) and most competent operational actors (Torsvald, Feldhaus, Virke,
Edeyja) are women in warden-master, guildmaster, broker, covert-operative, and grandmaster roles.

## 4. The foil architecture

`npc_foils_v30_infill.md` is the richest single artifact in the corpus for cross-faction drama. The
**Ruler Diamond** is worked across four axes (relationship to the settlement, to the caste question, to the
Church, to the basis of authority), then *every* pairing and perspective is drawn out: **six pairings**
(each with an objective analysis *and* each ruler's subjective, distorting view of the other three — twelve
asymmetric readings), and **four triangles** (Succession, Einhir, Consecration, Competence). The material
earns its keep because the subjective readings are load-bearing: Almud reads Vaynard as *"a governance
input,"* which is *exactly the reduction Vaynard's own analysis names as the insult* — *"The revolutionary
whose people were excluded from the founding settlement is, to the settlement's custodian, a management
challenge. The reduction itself is the insult."* The single sharpest pairing is Baralta↔Vaynard, framed as
categorical imperative vs. consequentialism — the caste axis, per the foil doc, *"makes the opposition
existential, not just philosophical"* — yet even
here an unstable operational coalition is conceivable if the Crown weakens enough: *"The instability IS the
drama."*

One more foil device is worth naming because it is *not* built on opposed conviction: **Feldhaus/Virke** are
structural mirrors — a legitimate guildmaster and a criminal broker unknowingly complicit in the *same*
Thread-tainted supply chain, each able to destroy the other by accident. The analyses doc calls it *"the
most mechanically consequential NPC relationship in the roster."*

## 5. The behavior model — where character becomes system

The NPC engine (`npc_behavior_v30.md`, `character_canon_v30.md`) is the model case for this whole
compendium: it is the clearest place the corpus turns a *personality* into resolvable *data*. Its atomic
unit is the **Stance Triangle** — three genuinely different questions about a character:

- **Conviction** — what they *want* to do (a weighted vector over **13 canonical Convictions**: Faith,
  Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue,
  Honor — each a period (mostly Latin) ethical dimension; 1–3 primaries at 0.6–0.8 plus a distributed cultural
  background template, projected through a fixed 13×4 matrix onto a `hierarchical/sacred/instrumental/
  traditional` armature).
- **Ethical Framework** — what they are *rewarded* for doing (faction-inherited; an Ob modifier).
- **Resonant Style** — what can *move* them (Evidence / Consequence / Authority / Solidarity).

Orthogonal to Conviction is a **Self-Other orientation** scalar `[−1, +1]` — *who benefits*, not *what is
valued* — that **drifts from accumulated outcomes** (κ ≈ 0.03/season). This is the cleanest single piece of
the bridge: it turns *"this character is becoming corrupt"* from a writer's decision into an emergent read
of play, using the corpus's own case of *"Cesare Borgia and a public-spirited republican magistrate"* (same Conviction, opposite
Self-Other) as its illustrating case — the Macbeth arc as an equation.

An NPC *decides* via a literal four-step procedure (Institutional Filter → Conviction Filter → a Scar-count
Decision Fork → Resonant-Style Interaction), and non-named NPCs get *only* the first step — a hard binary
between psychologically-modeled characters and faceless institutional actors. The strongest system in the
slice is the **Resonant Style → Belief → Scar loop**: to change an NPC's mind, a player must *discover* the
argument-shape that bypasses their defenses, *declare* it, match genre and style, and textually engage a
*known Belief* — and on a decisive win, the old Belief becomes a **Scar**, *"recorded permanently, cannot
be re-invoked,"* with the new belief written to *"incorporate the failure."* Persuasion has permanent
narrative memory; guessing wrong against a Church NPC in public *raises Church Stability*. This is
persuasion-by-argument-shape, not persuasion-by-flat-skill-check — the load-bearing novelty of the whole
NPC layer.

The **relational graph** (`npc_relational_graph_v30.md`, provisional) extends the same grammar to NPC↔NPC
ties: six edge types (Sworn-bond, Liege-vassal, Kinship, Patronage, Rivalry, Feud), each with a directional
scale, a named Renaissance precedent, and a coupling to a specific Resonant Style. Its most evocative rule
is that **feud auto-transmits along kinship on death** — *"the load-bearing mechanic for ROTK-style
emergent multigenerational narrative."* **Companions** (a named NPC at Disposition ≥ +3, max 2) get
departure scenes keyed to their *specific* Conviction red lines — a Faith/Order/Equity companion leaves,
no appeal, if you Dissolve a living being in their presence — so "loyalty" is a set of breakable values per
companion, not one universal approval meter.

A final, unusual detail closes the loop in the *other* direction: **voice is deliberately not stored
per-NPC.** *"The synthesis is the voice, not a per-NPC overlay"* — diction is generated at runtime from the
combination of Convictions + Coherence + TS + Spirit, so a numeric Spirit band maps directly onto a named
literary register (Spirit 6–7 at low Coherence reads as *"Beckett continuation — the will grips, the
decision recurs"*; Spirit 1–3 as *"Lispector dissolution — the name recedes, the feet replace the self"*).
That is quantitative→qualitative running the *other* way, on purpose.

## 6. Character histories and naming

A load-bearing correction first: `character_histories_v30.md` is **not** NPC backstory — it is a
Burning-Wheel/SaGa-style **lifepath character-creation system for PCs** (Origin → Formation → Vocation →
Catalyst, each granting skills, Certainty modifiers, and a **Knot** answering three questions: *what does
this person want from you, what does the relationship cost, what happens if it breaks*). It is a formalized
backstory compiler, and its "Lost Someone" catalyst even ships an anti-fridge *ghost-sheet* rule so the
dead keep influencing play. The actual named-character depth lives in `references/npc_registry.yaml` (**46
named entries**, 35 canonical + 11 thin/proposed) and the dedicated docs.

The **naming and etymology** are a strong, consistent *emergent* pattern — there is no naming style-guide
anywhere in the repo, which is itself a gap worth formalizing. The peninsula's personal names are
overwhelmingly **Old Norse / Scandinavian** (Yrsa, from *Hrólfs saga*; Orm, "serpent"; Njal; Vidar; Björn;
Sigrid) and its surnames and placenames **German/Germanic** (Ehrenwall "honor-wall," Kreutz "cross,"
Kronmark, Grauwald "grey forest," Himmelenger, the *-helm/-stad/-mark* compounds). The single sharpest
onomastic choice is **Sæmund** Haelgrund — echoing *Sæmundr fróði*, the legendary Icelandic priest credited
with compiling the *Poetic Edda* — for a Church Inquisitor who is institutionally orthodox while
unknowingly carrying the "old," suppressed perception. **Altonia** is coded *sharply* differently, in
**Byzantine/Greek**: Doux Alexios *Laskaris*, Zoe *Palaiologina*, Stephanos *Doukas* deploy three real
imperial dynasty names, with real Byzantine offices (*Katepano*, *Kommerkiarios*) as titles. The god-name
**Solmund** fits the Germanic register precisely — "Sol" (sun) + the Old Germanic name-element "-mund"
(protection/hand, as in Sigmund, Rosamund). It is also the corpus's single **hard-blocked** naming gate:
an earlier working name for the figure was retired and is now the *only* `enforce: block` entry among ~60
proper nouns (the rest are warn-tier), CI-enforced by `tools/ci_naming_check.py` — though, tellingly, the
rationale for the original retirement predates the current documentation layer and was not preserved.
In-world, the Church's *"forced conversion of naming conventions"* is itself framed as an instrument of
colonial violence — naming is diegetically a site of suppression, not just a design-layer curiosity.

The historical-figure-as-template method is remarkably systematic — every major NPC carries an explicit
"Inspiration" anchor (Manuel I Komnenos, Catherine the Great, Isabella/Henry VIII/Theodora, Bellarmine,
Rosa Luxemburg, Richard Sorge, Christine Granville, William Marshal, Aetius, Suger of Saint-Denis, Jacques
Cœur, the Chernobyl liquidators, and the one fictional outlier, von Lohengramm). Part V treats this method
in full.

## 7. Assessment — the NPCs

**Standouts.** **Edeyja** is the clear high-water mark — the only character with a physical signature, an
authored Coherence value, and a dramatic function *built out of* her exemption from the roster's own rule.
**Baralta** is the richest antagonist-pole, uniquely granted a doctrinal document that develops a genuinely
novel in-world theology. **Haelgrund** and the **Feldhaus/Virke** mirror are the two cleverest
narrative-mechanical fusions (an inquisitor who is the thing he hunts; two economic actors wired into the
same latent scandal). **Gerik Strand** is the most immediately runnable (his flattery vulnerability is a
named −1 Ob key). And the **behavior model** — Stance Triangle, Resonant-Style/Belief/Scar loop, outcome-
driven Self-Other drift, Conviction-specific companion red lines — is the strongest "personality is
gameplay" system in the whole corpus and the model this compendium's Part VI generalizes from.

**Gaps and live faults.** (1) **A texture cliff inside the roster**: the Ruler Diamond and the operational
tier are richly drawn, but three Cardinals (Klapp, Olafsson, Jarnstal) and both royal heirs (Torben,
Elske) are one structural sentence each, and ~11 proposed entries are visibly template-generated. (2)
**Stats are almost universally deferred** — every registry entry but Edeyja carries `stats: null [GAP]`,
and Spirit is unauthored for nearly the whole roster (defaulting to an `[ASSUMPTION]` 4). (3) **Three
incompatible Conviction taxonomies (7 / 9 / 13-value) are still live in canon** with acknowledged per-NPC
value conflicts — the quantitative substrate the whole behavior model depends on has not fully converged.
(4) **The relational graph is fully specified but empty** (`relational_edges_v30.yaml` does not exist), and
its most dramatic sub-mechanic (Defection Cascade) is admittedly unvalidated. (5) **A citable
cross-document contradiction on a load-bearing number**: Almud's Thread Sensitivity is stated as **0**
throughout the analyses and foils but as **28** in `character_canon_v30.md`'s Knot-strain table — worth
resolving before any system reads it. Haelgrund carries two of the same kind: his historical anchor is
**Bellarmine** in the roster/analyses but **"Savonarola"** in `npc_registry.yaml`, and his Thread Sensitivity
reads **12** in the analyses versus **15** (`# per Jordan`) in the registry. (6) The intended single canonical character sheet
(`character_canon_v30.md` Part B) *does not yet exist* — the texture is still scattered exactly the way the
consolidation doc complains about.

---
---

# PART IV — THE STORIES THE WORLD TELLS

## 1. The characteristic Valoria story

Across the arc corpus (`arcs/`), one pattern recurs so consistently that it deserves to be called the
setting's dramatic signature: **the compounding of individually correct decisions into a disaster nobody
chose.** The characteristic Valoria story is *not villainy* — it is closer to Greek tragedy or a
systems-thinking parable, in which sincere, competent, structurally-constrained actors produce a
catastrophe none of them intended and none of them can unilaterally stop. The corpus's own scoring rubric
rewards exactly this (it explicitly *penalizes* "political intrigue that could exist in any setting," even
when well-executed), and the strongest arcs pass it cleanly:

- **"The Unworked Clause"** — King Almud's *genuine, unresolved* ethical doubt about the caste system runs
  in parallel with Confessor Himlensendt's *unimpeachable* pastoral Church-growth. *"He is not
  rationalising. He is correct about the costs."* Two good-faith actors' restraint creates the vacuum the
  Restoration Movement drifts into.
- **"The Quiet Fracture"** — called *"the most thematically essential arc in the game"* — in which Church
  Weaving accelerates world-decay *while appearing to help*: **"The world is not breaking. That is the
  problem."** Existential dread produced by the *absence* of visible crisis.
- **"The Army That Stayed"** — *"the best demonstration of mechanical emergence in the entire portfolio"* —
  where a **9% probability event** (two failed Discipline checks in a mass battle) spirals into a
  multi-season political occupation crisis: *"The players are watching a political crisis caused by a 9%
  probability event."*
- **"The Chained Ships"** — the Church redistributes looted southern-Einhir cultural artifacts to the
  faithful as charity; over four invisible seasons they turn out to be Thread-active and are poisoning the
  world's substrate. Four separate NPC flaws (Virke's network-protection, Feldhaus's profit-maximizing, a
  Cardinal's optimizing, Haelgrund's proceduralism) interlock into a catastrophe none of them designed —
  *"the caste system's cultural erasure made material."*
- **"The Sinigaglia Dinner"** — a mutual-assured-destruction standoff producing *"the most psychologically
  tense arc in the portfolio,"* its title a direct citation of Cesare Borgia's 1502 massacre at Senigallia.
- **"The Practitioner Who Stopped"** — *"this game's signature move"* — a mystery of *absence*, in which a
  Truthseeker halts Thread practice out of self-preservation and becomes a question rather than an event.

The endgame table states the thesis plainly. When none of its nine stabilizing conditions hold, *"the
Einhir Catastrophe repeats. Not literally… but the political and metaphysical conditions that produced the
original collapse are recreated: practitioners acting ambitiously on a damaged substrate, factions
prioritising leverage over repair, and a world-scale rupture that no single actor caused and no single
actor can stop."*

## 2. The throughline model — pressures, not plots

The word "throughline" is a false friend in this repo (it names two unrelated design-audit artifacts). What
actually functions as a *campaign-spanning narrative thread* lives in the arc register under a different
name: **Vectors.** A Vector is *"a sustained pressure with a source, a direction, and conditions that
modulate its strength. Vectors do not specify outcomes or resolution paths — they state what is pushing,
toward what, and what changes the rate."* The seven **Clock Vectors** (Church accumulation, world-substrate
decay, the Löwenritter Coup Counter that *"never decrements,"* the Thread-acknowledgment axis, NPC faction
drift, invasion pressure, public instability) are the true throughlines — always-on, never resolved, only
managed. Where they collide, **Convergence Markers** (Collisions A–J) name the emergent crises — *"named
not for dramatic effect, but because the combined pressure is not predictable from the constituent vectors
without the marker."*

This is the register's real design philosophy, and it is a genuinely mature one: **the register authors
directional pressure, not plot.** *"Story events emerge from the intersection of active vectors; the GM
does not execute arcs, they run pressures and observe what they produce."* The register even polices itself
against narrativizing — its "What Was Cut and Why" section removes entries that were *"scripts, not
pressures."* The dissolution of Niflhel with *no replacement villain faction* (crime redistributed to
*"whichever local network is dominant, not a meta-faction"*) is the same instinct: refuse personification,
keep the drama structural.

## 3. The crucial caveat — what the arcs actually are

This is the single most important framing fact for anyone building on the arc corpus. **Nearly the entire
`arcs/` corpus is hand-authored *illustrative sample* content, not runtime-generated output.** The ratified
successor design — the **Churn Engine v2** (`designs/audit/2026-07-05-emergent-narrative-engine/`, newer and
more authoritative than almost everything in `arcs/`) — diagnoses its own predecessor bluntly: the
register's ~138 arcs *"are narrative text applied to sample trajectories through state graphs, collapsing
to ~13 structural shapes… v1 treated the samples as the content."* Its sharpest self-criticism — *"pruning
IS authorship"* — names the real gap: the Convergence Markers are *"8 authored conjunctions as the entire
convergence surface"* rather than discovered by simulation, and *"'what happens if no one acts' was
authored, not computed."*

The practical consequence for this compendium: **treat the arcs as a tone/quality bar and a verified
library of vector-interaction patterns — never as literal content to quantify.** The mechanical scaffolding
around each arc (thresholds, dice pools, Ob values, Priority Trees) *is* procedural and real; the
*"Narrative"* prose is hand-written illustration. Re-verify any specific probability or Ob against the
current `engine/params/*.md` tables before trusting it — several arc batches predate the current generation
and visibly drift in quality over their own development (Batch 01 reads like short fiction; the later
"resolved" batches read like an engineering changelog correcting the earlier prose against confirmed
mechanics).

## 4. Assessment — the narrative layer

**Standouts.** Assessed purely as drama, the strongest material genuinely earns it — *"The world is not
breaking. That is the problem,"* the Inquisitor turning his own institution's evidentiary procedure against
itself, Warden Orm's restrained self-sacrifice, the now-struck assassination mystery whose revelation is
*"not 'nobody did it' [but] 'everyone has spent 27 years building political structures around the
assumption that someone did, and those structures are now load-bearing.'"* The **Vector/pressure-ledger**
architecture is a mature, reusable model that keeps emergence structural rather than scripted, and the
scoring rubric's insistence on setting-specific *thematic* weight (over generic intrigue) is a real quality
discipline. The best arcs are novelistically complete.

**Gaps.** The corpus's own audit flags **missing arc *types*** — no mass-combat arc, no arc *from inside*
Thread practice, no Southernmost/Warden arc, no Torben-primary arc — and **NPC coverage gaps** (Edeyja,
"the moral anchor of the setting," is *invisible in the arc portfolio*). A meaningful fraction of the
material is **dead narrative infrastructure still physically present** (struck arcs retained with
strikethrough banners) — good hygiene, but a trap for anyone skimming. And the **quality-drift over
development time** means the arcs are an inconsistent stylistic template. Above all: the currency caveat in
§3 is not optional context — it is the difference between using this material correctly and building on a
foundation the corpus itself has already deprecated.

---
---

# PART V — PRECEDENTS & INFLUENCES

Valoria is unusually *forthcoming* about its sources. A dedicated `research/` program documents its
historical grounding with academic apparatus, and nearly every major NPC and faction carries an explicit
named "Inspiration" or "Historical anchor." This part separates **explicit** influences (named in the
corpus) from **inferred** ones (this reading's attribution of a resemblance the docs do not claim), because
the platform should know which is which.

## 1. The documented precedent program (explicit, and rigorous)

The `research/` corpus is the influences goldmine and the strongest evidence that Valoria's grounding is
*structural*, not cosmetic. Its method is consistent: **real case → abstracted structural mechanism →
explicit mapping to a named Valoria system → audit for over-fit or fabrication.** Highlights by theme:

**Theocracy / governance (`precedents_analysis.md`).** The Church of Solmund is grounded in the
**Papal States** (governance-vacuum filling), **Calvin's Geneva** (theocracy-by-invitation — the "Geneva
trap": you invite the Church because it governs better, then cannot remove it), **Iran 1979** (pre-positioned
religious network activated on state collapse — the model for the CI-100 Mass Seizure), **Tibet** (spiritual
legitimacy + external military enforcement), and the **HRE prince-bishoprics** (theocracy as political
arrangement).

**Invasion during instability.** The Altonian threat is grounded in the **Mongol/Khwarezmian** and
**Ottoman/Byzantine** patterns (invasion timed to internal division; the invited-ally-who-stays), **Charles
VIII's 1494 invasion of Italy** (rivalry prevents coalition), and **Soviet Afghanistan** (occupation
generates its own resistance — the model for the Occupation Era).

**Movements → government.** The Restoration Movement is grounded in **Bolshevik 1917**, the **Indian
independence movement** (constructive-program legitimacy), **Solidarity**, the **ANC**, the **CCP** (Yan'an
base-area governance), and — named as the parallel the doc draws "most directly" — the **Zapatistas**
(anti-hierarchical, alternative-not-capture governance). Its two founding pathways are modeled — in the
mechanics doc `victory_v30.md`, not this research file — on Bolshevik 1917 (concentrated) vs. the 1848
revolutions (distributed).

**Cultural revival / post-colonial governance.** Grounded in the **Irish (Gaelic League)**, **Hebrew/Zionist**
(the most successful revival→state transition), post-colonial **India** (inheriting the colonial
administrative state), the **Baltic Singing Revolution**, and the **Māori Renaissance** (revival *within* the
state). Valoria's novel twist: because of the Forgetting, RM's revival is necessarily *partial* — it can
reconstruct the political shell of Einhir governance but not its Thread foundation.

**Governance at depth (`research/governance/`, the methodological gold standard).** An 8-civilization ×
3-theme corpus (Ottoman, Rome, Carolingian, HRE, Renaissance Italy, Venice, Han/Three-Kingdoms, Shogunate
Japan) built by a Sonnet-researcher / Opus-verifier pipeline with the verifier's factual corrections
preserved inline. It yields **~230 explicit "=> Valoria design hook" lines** (an exact count runs 228–230
depending on whether the manifest's prose mentions are included; `CURRENT.md` hedges it "~228") and three
reusable primitives:
**standing = a claim on a debasable currency, never a bare scalar** (rank as a display aggregate over
office/honor/access/kinship axes); the **collision-of-stresses (two-signal) event primitive** (a bare
grievance fizzles; only a material threshold *plus* an independent interpretive trigger, arriving together,
detonates — flagship case the **Ōnin War**); and **mode-as-mask-vs-substance** (a polity can display one
governance mode while running another — Cao Cao's "Han" edicts, the Medici informal principate). Its most
telling discipline: a standing design-lead ruling that **"Mandate of Heaven appears as history only, never a
Valoria mechanic,"** enforced across all ~230 hooks and verifier-checked civilization by civilization — the corpus
repeatedly had the on-the-nose fantasy answer available (a cosmic-mandate legitimacy meter) and *deliberately
declined it*, doing the harder work of finding ideologically-inert equivalents. **Max Weber's** tripartite
legitimacy typology (named in the warfare-precedent research, `precedents_warfare.md`) and **Polybius's**
*anacyclosis* (in the governance corpus) are named as organizing frameworks.

**Warfare (`precedents_warfare.md`, `research/pre_firearms_formations/`).** The mass-battle layer is
validated against named battles and historians — Cannae, Trasimene, Hastings, Leuctra, Leuthen; du Picq,
Lanchester, Goldsworthy, Sabin — with a 29-throughline synthesis. The single most consequential finding, per
a Jordan correction: **"threadwork is Valoria's firearm-analog,"** recontextualizing the historical
firearm-transition window (Cerignola 1503, Chaldiran 1514) as the canonical model for the setting's central
narrative hinge — a technology that renders an entire prior doctrine obsolete once a *system* to use it
exists.

**Rhetoric (`rhetoric_oratory_contest_research.md`).** The social-contest layer is grounded in **Ciceronian
stasis theory** (conjectural/definitional/qualitative/translative — the last = jurisdiction = the
Parliamentary "Stay"), the five classical canons, and — unusually — the **Nyāya-sūtra**'s three-mode debate
theory with its 22 *nigrahasthāna* "points of defeat" (grounding the contest's self-gating), plus a whole
proposed petition subsystem drawn from Arabic chancery *inshāʾ* and the medieval *ars dictaminis*
five-part letter (*supplique* vs. *remontrance*).

## 2. The literary, mythological, and philosophical lineage (explicit)

The Solmund cosmology and the canon foundations wear their sources openly:

- **Kabbalah, centrally and by name.** *Ein Sof* is used verbatim for the infinite unmanifest ground;
  *tsimtsum* (contraction) models the rendered world as a region of finitude within infinite being; and
  Lurianic *shevirah/tikkun* (shattering/repair) is explicitly framed as the Restoration Movement's own
  theological self-understanding.
- **Phenomenology and existentialism.** **Husserl** (retention/protention, apperception — used verbatim),
  **Heidegger** (the ontical/ontological distinction, thrownness), **Kierkegaard** (repetition, and *the
  Leap*, mechanized directly as a game term), **Lacan** (the Real, grounding monstrosity structurally),
  **Whitehead/Bergson** (process philosophy), **Wittgenstein** (*Tractatus* 7, "whereof one cannot speak"),
  **Levinas** (the Face, applied specifically to the Einhir dead), and **Derrida** (aporia).
- **The poets, as tonal registers** (the Certainty table): Böhme, R.S. Thomas, Di Cicco, Hopkins, Ficino,
  Eliot, John of the Cross, Teresa of Ávila — and, for the post-catastrophe Einhir voice, **Paul Celan** and
  **Edmond Jabès** (post-Holocaust Jewish poetics of double-speech and absence). The prose-writer's own
  Beckett-vs-Lispector spectrum keys diction to the Spirit stat.
- **The historical-figure-as-structural-template method** — the corpus's most distinctive *authorial*
  technique. Every major NPC is assigned a named parallel: Manuel I Komnenos (Almud), Catherine the Great
  (Lenneth), Isabella I of Castile + Henry VIII + Theodora (Baralta), Bellarmine (Haelgrund), Rosa Luxemburg
  (Vossen), Richard Sorge (Uln), Christine Granville (Torsvald), William Marshal (Strand), Aetius (Brandt),
  Suger of Saint-Denis (Tormann), Jacques Cœur (Feldhaus), the Byzantine *logothetes* (Almstedt), Demetrios
  Palaiologos (Laskaris), Xenophon's *Anabasis* (Solberg), the Chernobyl liquidators (Orm), and the single
  deliberate pop-fiction outlier, **Reinhard von Lohengramm** (Vaynard), reserved for the character the
  design most wants read as sympathetic-but-dangerous. The palette is overwhelmingly Byzantine and
  late-medieval/early-modern European, and the technique gives writers fast, legible tonal shorthand — worth
  formalizing as a deliberate discipline.

## 3. The onomastic and cultural register (mostly inferred)

There is no naming style-guide in the repo, but the pattern is unmistakable and does real thematic work: a
**Norse/Germanic** peninsula (personal names from the sagas, placenames from Holy-Roman/Hanseatic compound
German) set against a **Byzantine/Greek** empire (Altonia), with the invented god-name Solmund sitting
squarely in the Germanic register. The explicit in-doc coding ("Swiss character" Hafenmark, "Norwegian
character" Varfell, "Italian character" Crown heartland) reinforces a general **early-modern European
state-formation** frame, and the Northern/Central/Southern Einhir caste reads as a deliberately-designed
**settler-colonial internal-stratification** analogue (framed in-doc as Altonian colonial residue, with the
Altonian occupation itself anchored explicitly to the **British Raj**).

## 4. The inferred ludic ancestry (game-design lineage)

The corpus names some of its game precedents outright — **Skyrim** (rank-ladder "Skyrim Eight"), **Crusader
Kings** and **KOEI Romance of the Three Kingdoms** (court/officer/succession simulation, cited by name),
**Mount & Blade** (player-presence-affects-morale), **Terra Mystica / Gaia Project**, **Root** (the RM as
the asymmetric "Vagabond"), **Here I Stand / Virgin Queen** (*"Valoria's closest precedent in structure"*),
and **Twilight Imperium** (cited for narrative completeness for every player — "Hollow Victory" is Valoria's
own mechanic, not TI4's). Beyond the named set, the structural resemblances are
strong and worth recording as inferred lineage:

- **Blades in the Dark** — the entire Vector/Clock apparatus (segmented pressures filled by triggering
  conditions, never a single roll; the Coup Counter that "never decrements") and the "clocks track pressure,
  not plot" philosophy are BitD to the letter; the **"Ob"** difficulty notation is **Burning Wheel**.
- **Dwarf Fortress** (legends-style emergence) and **RimWorld / Left 4 Dead** (an AI storyteller/director
  escalating pressure off aggregate world-state via banded thresholds) — the register's refusal to
  pre-script outcomes and its tolerance for absurd disproportion (a 9% roll becoming an occupation crisis)
  are squarely in this lineage.
- **Disco Elysium** — the Certainty/TS-gated internal register-switching, and the immersive-sim "each NPC is
  a lock with a specific key" design (Strand's flattery, Haelgrund's Diagnosis) — persuasion as skill-gated
  discovery rather than a flat check.
- **Return of the Obra Dinn / Outer Wilds** — the Seam Text's comprehension-gated (not visibility-gated)
  revelation is the same epistemic mechanic: content unlocked by the player's own accumulated understanding.
- **Total War** and the **Paradox grand-strategy** family (EU/CK) — the formation/facing mass-battle model
  and the seasonal domain-action/estate-friction loop; the corpus's own research self-describes Valoria as
  resembling *"a Skyrim-guild-style rank ladder plus an EU4/CK3-style estate-friction governance loop."*
- **Roadside Picnic / S.T.A.L.K.E.R. / Annihilation** — the Southernmost's whole apparatus (a bordered
  hazard-zone around a catastrophe site, multi-season phased expeditions, things that "shift" near the
  wound, a containment-not-conquest institution) is close kin to the Zone genre, and the Forgetting's
  testimony-degradation is very near *Annihilation*'s core conceit.
- **Legend of the Galactic Heroes** (Vaynard, explicit), **Gnostic Christianity** (the esoteric/exoteric
  witness split, inferred), **Dune**'s Missionaria Protectiva (the Perceptual Prophylaxis as its *emergent*
  cousin, inferred), and **His Dark Materials** (a Church suppressing perception of an imperceptible
  substrate — which Valoria pointedly declines to resolve by unmasking its god, inferred).

## 5. The intellectual signature

Taken together, the influences describe a coherent authorial program with four hallmarks: **structural, not
cosmetic** grounding (real case → mechanism → mapping → audit); **adversarial verification** where the
stakes are highest (the governance corpus's second-agent fact-checking; the rhetoric corpus's source-tiering
and self-correction); a **standing veto on the cheapest fantasy shortcut** (the Mandate-of-Heaven ban); and
a repeated **willingness to cut historically-faithful proposals that fail the game's own narrative-value
bar** (two precedent-analysis proposals were dropped as "invisible cap → player frustration" and "zero
narrative moments"). The civilizational palette is late-antique/medieval/early-modern Old-World
state-formation, with a genuine non-European rhetorical spine (Arabic *balāgha*, Chinese *zonghengjia*,
Sanskrit Nyāya) and a 20th-century decolonial case-study layer for the movements material — chosen, per the
manifest, precisely because they *isolate variables the dominant European tradition fuses*. This is a
setting built by people reaching for comparative-politics scholarship and continental philosophy as
scaffolding, not for genre trivia — and it is the single strongest asset the platform inherits.

---
---

# PART VI — FROM TEXTURE TO MECHANISM

This is the payoff volume. The preceding parts assessed the narrative quality of Valoria's world,
factions, and NPCs; this one turns that assessment into a **platform for design** — a method for
translating qualitative texture into quantitative form, the principles that keep the texture intact through
the translation, a catalogue of concrete opportunities, and a prioritized build order. The good news the
whole compendium has been building toward: **Valoria has already built the bridge in several places.** The
task is less to invent the method than to name it, extract it, and apply it consistently.

## 1. The method — three moves that recur across every built bridge

Every place the corpus successfully turns character or world *texture* into resolvable *state* uses one of
three moves. Naming them makes them reusable.

**Move A — Texture as a vector (a quality becomes a position in a small named space).** The clearest case is
the NPC **Conviction vector**: "she is a legalist" becomes a weighted 13-dimensional vector projected onto a
four-axis armature (`hierarchical/sacred/instrumental/traditional`), which anything downstream can
dot-product against. The faction **Public-Expectation** role templates do the same at faction scale, and
**Cascade Fidelity** (cosine similarity between what a faction *is* and what its role *claims*) is a whole
qualitative judgment — "is this institution being true to itself" — rendered as one number in `[−1, +1]`.
The move generalizes: any recurring qualitative descriptor (a place's mood, a faction's posture, a
territory's temperament) can be a low-dimensional vector with named axes rather than a prose adjective.

**Move B — Texture as a gated threshold (a quality becomes a band that changes what is *possible*).** The
corpus's best mechanics are threshold systems where a numeric track crosses named bands and *forecloses or
unlocks* actions rather than merely adding modifiers: **Accord** (0–3) changes what a territory *is*
(busy markets vs. barricades); **Coherence** (0–10) crossing bands changes which Thread actions are *legal*
and forks into four different fates at zero; **Certainty** selects the *prose register* a character speaks
in; **Thread Sensitivity 30** gates *comprehension* of the Seam Text. The signature of the best of these is
the **two-stat intersection fork** — Coherence-0 outcome forked by TS, the Consecration Crisis forked by
Church Stability *at the moment of claim* — where the drama comes from *which* threshold you cross *when*.

**Move C — Texture as an ability tag → cost/effect formula (a quality becomes a rule the resolver reads).**
The **operation taxonomy** (Restorative = zero Coherence cost / Manipulative = scale×deviation / Destructive
= catastrophic) is a quality ("what kind of act is this against the substrate's grain") rendered as a tag
each action carries and the resolver prices. The **ethical-framework Ob modifier** is the same move: "this
act aligns with the faction's philosophy" becomes −1 Ob. The **Resonant Style** is Move C at the level of
persuasion: "what argument-shape moves this person" becomes a declared tag that must be matched for a
mechanical bonus.

Almost every proposal in §3 below is one of these three moves applied to texture that is currently pure
prose.

## 2. Design principles for keeping texture intact through mechanization

The corpus has learned — sometimes painfully — a set of rules for *not* flattening narrative into a
spreadsheet. These are its own lessons, extracted; treat them as the platform's constitution.

1. **Keep some things qualitative on purpose, and say so.** The **Nine Political Axes** are *deliberately
   un-tracked* — the corpus reserves them for "war justification, Domain Echo content framing, faction-foil
   structural analysis." The **ethical-framework labels** were
   *deliberately retained as prose-only tags* after their mechanical role was retired. Not every quality
   should become a number; the skill is choosing which stays prose, and *documenting the choice* so a later
   pass does not "helpfully" quantify it.
2. **Protect irreversible, pivotal acts from dice noise.** A recurring design instinct (the σ-leverage
   audits, the two-stage succession split): a near-irreversible outcome — Excommunication, a Royal Decree, a
   realm fragmenting — should be *structure-decisive with a stochastic tail*, not a coin flip. Separate the
   *contingent* roll (who wins) from the *structural* determination (whether it fragments), so variance
   colors the outcome without owning it.
3. **Make the number legible as texture, not just a stat.** Accord ships an *environmental-legibility table*
   (what the streets look like at each value) precisely so the number is *felt*. A track the player reads
   only in a UI panel has failed this test; a track they read off the baker's silence has passed it.
4. **Let identity have teeth, symmetrically.** The caste system is the model: it is not a debuff bolted on,
   it is threaded through *every* ladder, the Renown track, *and* a set of compensating advantages (the
   Wardens, the Riskbreakers reverse-privilege the stigmatized). Structural injustice modeled as *only* a
   penalty reads as designer cruelty; modeled as a penalty *with* the narrow paths it forces open, it reads
   as a world.
5. **Naming/identity accuracy is a precondition for mechanization, not an afterthought.** The
   `placeholder_names` gate literally *blocks a mechanic from shipping under its real name* until a
   "contamination audit" confirms its qualitative identity is right (a Varfell action was struck for a
   "mead-hall" framing that contradicted the ruler's ratified conqueror identity). Encode the texture
   *before* the numbers, and let the texture veto the numbers.
6. **Prefer emergence from accumulated outcomes over authored beats.** The Self-Other drift (the "Macbeth
   arc as an equation") and the Vector/pressure-ledger both make character and story *emerge from play*
   rather than firing on scripted triggers. When a quality can be a *drift* off outcomes rather than a
   scripted flip, make it a drift.
7. **Failure is a chapter, not a screen.** The Rupture/Occupation/Anarchy Eras are the humane, replayable
   default: a lost track opens new play rather than ending it. Any new "loss" mechanism should ask what
   *era* it opens, not what screen it shows.

## 3. A catalogue of translation opportunities, by domain

These are concrete, texture-grounded openings where qualitative material in the corpus is *already
reaching* for quantitative form. Each names the texture, the move (A/B/C from §1), and a candidate
mechanism. None is a ratified proposal — they are a menu for the design pass.

### World & cosmology

- **Heresy of naming (Move C).** The tripartite vocabulary already makes *saying the wrong word* an act of
  dissent (orthodox "the Ground" vs. forbidden "Ein Sof"/"Ungrund"). Candidate: a lightweight **Lexical
  Exposure** tag on dialogue/appeal actions — using suppressed or forbidden vocabulary in public raises a
  Heresy-Investigation signal and shifts the speaker's Certainty register; using it *privately* with a
  high-trust NPC is a bonding beat. Texture that is currently a glossary tier becomes a spoken-risk economy.
- **The grammatical tell of dissent (Move A/C).** "The break from 'we' into 'I' is the first sign of
  theological dissent." Candidate: the prose-generation layer already keys register to Certainty; add a
  *person* axis (plural/orthodox ↔ singular/heterodox) so that generated NPC speech *shows* a drifting
  Certainty before any stat is revealed — the voice performs the number.
- **The Forgetting as a testimony economy (Move B, already half-built).** The Testimony-Ob-penalty-that-
  *decreases*-with-exposure-depth is one of the best mechanics in the corpus. Extend it into a full
  **Credibility-from-Proximity** system for Southernmost knowledge: what a character can *convince* others
  of about the wound is a function of how deep they have been, independent of what is true — a permanent,
  structurally-unresolvable information asymmetry that drives Vaynard's whole tragic bind.
- **The Seam Text as discoverable content (Move B, specified but not built).** Comprehension-gated scripture
  is a ready open-world content slot (a "Remnant" POI): the *same* text renders as devotion below TS 30 and
  as witness-account above it. This is a cheap, high-texture way to make Thread Sensitivity *feel* like a
  different way of reading the world rather than a bigger number.
- **The wound as a renewable hazard (Move C, licensed by canon).** The scale-invariance claim ("one
  Coherence-0 NPC and the whole Catastrophe run the same mechanism at different scale and duration) means the platform
  can generate **proto-Calamity quests** procedurally: any sufficiently powerful, sufficiently broken NPC is
  a walking Gap-in-waiting; containing them before they tear a new Locked Zone is a quest template the canon
  *implies*. This is among the most generative unbuilt hooks in the world layer.

### Factions & politics

- **Substrate-Posture as the mystery's strategic face (Move A).** Each faction's stance toward the Thread
  cosmology is already a named posture (suppressor / sovereigntist / agnostic-protector / heritage-reclaimer).
  Because the grand-strategy axis and the central mystery are the *same axis*, a single **Revelation Pressure**
  track (how close the setting's occult truth is to going public) can drive *both* a faction's political
  behavior and its metaphysical arc — the Triple Interpretation becoming the branch table when it fires.
- **Franchise / caste as national math (Move A/B, built).** The parliamentary-weight-by-territory system
  already turns caste stigma into national voice. The design opportunity is to make *breaking* it a
  first-class strategic objective with its own track — Vaynard's motive rendered as a **Caste-Reform** clock
  that other factions can advance, resist, or co-opt, with the Franchise numbers as its scoreboard.
- **Two-signal crisis events (Move C, from the research corpus).** The collision-of-stresses primitive
  (material threshold + independent interpretive trigger, both required) is *the* reusable event grammar the
  governance research hands over, ready-cited to the Ōnin War. Any settlement-shaking event should require
  *both* signals so that a bare grievance fizzles — this alone would give the strategic layer a principled
  answer to "what makes a crisis actually detonate."
- **Standing as a debasable composite (Move A, from the research corpus).** The research's headline finding
  — standing is *never* a bare scalar — argues for the 0–7 rank number becoming a **display aggregate** over
  tracked sub-currencies (office, honor, access, kinship-proximity), so that a character can be
  "disgraced-but-titled" (the Byzantine Office/Dignity split) rather than simply demoted. This is the
  richest single item in the ~90%-unlanded comparative-governance vein.
- **Mode mask vs. substance (Move C).** Let a territory *display* one governance mode while *running*
  another (the Medici principate, Cao Cao's "Han"), with the Legitimacy gate reading the *displayed* mode —
  a deliberately exploitable gap that rewards sophisticated play and models real political hypocrisy.
- **The Consecration Crisis's un-translated branch (open seam → opportunity).** Its "GM discretion"
  escape hatch (Himlensendt's personal faith state) is precisely the kind of texture the platform must learn
  to encode: candidate is a hidden **Faith-State** track on Himlensendt (advanced by whether he has undergone
  his "Originary Lock" encounter) that the engine reads in place of the GM — converting a load-bearing prose
  judgment into a legible, discoverable state.

### NPCs & relationships

- **Generalize the Stance Triangle to every actor (Move A, built for named NPCs).** The Conviction /
  Ethical-Framework / Resonant-Style triple is the model case; the opportunity is to make even
  *lightly-drawn* NPCs run a compressed version (the roster already does this via one-line "Behavioral AI"
  flaws with a named cost) so the ~35-NPC "Active" cap can extend gracefully without every NPC needing a full
  sheet.
- **The Resonant-Style/Belief/Scar loop as the universal persuasion spine (Move C, built).** This is the
  strongest "personality is gameplay" system in the corpus and should be the *default* model for every
  social contest: discover the argument-shape, match it, engage a known Belief, and permanently Scar the old
  one on a decisive win. It is exactly the qualitative-texture-with-permanent-consequence the whole project
  is chasing. Priority: author the Beliefs (currently sparse) so the loop has fuel.
- **Self-Other drift as the corruption/redemption engine (Move C, built, underused).** The outcome-driven
  ego/altruism scalar already exists; wiring more actions to feed it would let Macbeth and redemption arcs
  *emerge* from twenty seasons of play rather than being authored — the single cleanest instance of "texture
  from accumulated outcomes."
- **Conviction-keyed companion red lines (Move C, built).** "A Faith companion leaves, no appeal, if you
  Dissolve a living being" is the model for making *every* companion's loyalty a set of specific breakable
  values rather than one approval meter. Generalize the departure table across the roster.
- **Feud-transmits-on-death and the empty relational graph (Move C, specified but unpopulated).** The
  ROTK-style multigenerational feud mechanic exists on paper but the graph has *zero authored edges*.
  Authoring the Ruler-Diamond edges (and the Feldhaus/Virke mirror) is a small, high-leverage task that turns
  a specified system into a live one.

### Narrative & emergence

- **Vector-pressure ledger as the generative spine (built as a model, not as a generator).** The Churn
  Engine v2 already names the work: make the Convergence Markers *computed* from vector intersection rather
  than authored, and make "what happens if no one acts" a *forward-simulation query* rather than a written
  paragraph. The arcs corpus is the verified pattern library that tells the generator what *good* output
  looks like.
- **Tag the NPC "flaw" vocabulary and the arc-scoring rubric (Move A).** The closed set of flaws (IDEALIST,
  PROCEDURALIST, OVERPERFORMER…) and the five-axis arc-quality rubric (Emergence / Table-experience /
  Grounding / NPC-fidelity / Thematic-coherence) are currently applied by hand; both are ready to become
  numeric inputs to an automated *promotion/pruning* decision — which the Churn Engine explicitly names as
  its central unsolved problem ("pruning IS authorship").

## 4. Prioritized recommendations — where to build first

If the platform can only pursue a handful of these, this is the order the assessment recommends, chosen for
leverage (how much texture it unlocks) over effort:

1. **Resolve the two faction-personality models** (Model 1 labels vs. PP-686). Everything in the faction and
   NPC layers reads *through* this fork; it is the highest-leverage debt and blocks clean quantification of
   faction behavior.
2. **Author the empty substrate the built systems are starving for** — the relational-graph edges, the NPC
   Beliefs (fuel for the Resonant-Style loop), and the deferred stat blocks. These convert *specified*
   systems into *live* ones at low authoring cost and high dramatic return.
3. **Adopt the Resonant-Style/Belief/Scar loop as the canonical social-contest spine** and the Stance
   Triangle as the canonical NPC model — they are the corpus's strongest bridges and the template Part VI's
   method is drawn from.
4. **Build the two-signal crisis-event grammar** from the governance research — it is fully cited, gives the
   strategic layer a principled detonation rule, and is the readiest of the ~230 hooks.
5. **Make Thread Sensitivity a way of *reading the world*** — ship the Seam Text as comprehension-gated
   content and the Forgetting as a credibility economy — so the setting's central perceptual gift *feels*
   qualitatively different rather than being a larger number.
6. **Resolve the no-GM seam deliberately** (see §5) before it forces itself, because every "GM discretion"
   escape hatch in the scenarios is an IOU written against it.

## 5. The open seams the platform must resolve

Three faults are not gaps to fill but *choices to make*, and the platform should make them consciously
rather than inherit them by default:

- **The no-GM metaphysical seam.** P-03 says only minds render; the game has no GM and an engine is not a
  mind. Decide, explicitly, whether the **engine renders** (revising the metaphysics) or the **player's
  consciousness renders and the engine computes the substrate** (preserving it). Every "GM discretion"
  branch — the Consecration Crisis, several NPC arcs — is downstream of this and cannot be encoded until it
  is settled.
- **The unreconciled models.** Two faction-personality systems and three Conviction taxonomies coexist in
  live canon. The platform cannot quantify what the canon has not yet decided; pick one of each, and retire
  the others to the supersession trail.
- **The finish-line problem.** A great deal of the richest material is *provisional or superseded* — the
  Solmund cosmology (DRAFT, no `CURRENT.md` row), the arcs (illustrative samples), Varfell's Path B (struck),
  ~90% of the comparative-governance research (unlanded). The texture is a strong platform; the *ratification
  state* is the bottleneck. The most valuable non-creative act available is a currency pass that promotes the
  best of this material to canonical heads so the quantitative work has settled ground to stand on.

---

## Appendix — Source map (what was read)

This compendium synthesizes a twelve-agent parallel deep-read of the following surfaces (all paths under
`/home/user/ttrpg/`):

- **Canon foundations:** `canon/00_philosophical_foundations.md` (+`_rules`), `canon/01_foundations_amendment_self_rendering.md`, `canon/02_canon_constraints.md`, `canon/02_foundations_amendment_leap_mechanism.md`, `canon/03_canonical_timeline.md`.
- **The world / Solmund:** `systems/world/solmund_master_document.md`, `solmund_philosophy_v30.md`, `solmund_v30.md`, `solmund_voice_v30.md`, `solmund_artifacts_v30.md`, `narrative_voice_canon_v30.md`, `worldbuilding_v30*.md`, `geography_v30*.md`, `calamity_radiation_v30*.md`, `southernmost_v30*.md`, `insurgency_pipeline_v30.md`, `ms_trajectory_v1.md`, `worldbuilding_canon_audit_v30*.md`; `systems/settlements/territory_temperaments_v30.md`, `valoria_geography_v30.yaml`, `valoria_political_hierarchy_v30.md`.
- **The factions:** `designs/provincial/faction_canon_v30.md`, `faction_layer_v30*.md`, `faction_state_authoring_v30.md`, `faction_politics_v30*.md`, `faction_behavior_v30.md`, `faction_succession_split_v30*.md`, `political_dynamics_keys_migration_v30.md`, `ci_political_v30*.md`, `baralta_crown_claim_v30*.md`, `varfell_path_b_v30*.md`, `strategic_layer_v30*.md`, `military_layer_v30*.md`, `mass_battle_v30*.md`, `mass_battle_integration_v30.md`, `victory_v30*.md`, `peninsular_strain_v30*.md`, `franchise_v30.md`, `fractional_province_ownership_v30*.md`, `treaty_expiration_v30.md`, `parliamentary_transfer_v30.md`, `factions_personal_v30*.md`; `designs/factions/faction_systems_overview_v30.md`.
- **The NPCs:** `systems/npcs/npc_roster_v30*.md`, `character_canon_v30.md`, `npc_character_analyses_v30*.md`, `npc_foils_v30*.md`, `npc_behavior_v30*.md`, `npc_behavior_system_v1*.md`, `npc_relational_graph_v30.md`, `companion_specification_v30.md`, `baralta_v30.md`, `edeyja_npc.md`, `character_histories_v30*.md`; `references/npc_registry.yaml`, `names_index.yaml`, `glossary.md`, `registers/placeholder_names.yaml`; `designs/personal/conviction_taxonomy_v30.md`, `conviction_axis_matrix_v30.md`.
- **The arcs:** `arcs/arc_expansion_v30.md`, `emergent_arcs_experimental.md`, `emergent_campaign_arcs.md`, `emergent_scenarios.md`, `narrative_scenario_chains.md`, `throughline_resolutions_v30.md`, `arcs/registers/*.md`, `arcs/simulated/arc_narrative_analysis.md` (+ sampled batches); context: `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md`.
- **Precedents:** `research/historical/precedents_analysis.md`, `precedents_warfare.md`; `research/governance/*.md`; `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md`; `research/pre_firearms_formations/*.md`.
- **Deprecated (mined for recovered texture):** `deprecated/archives/audit/2026-06-09-faction-comprehensive/`, `2026-06-22-faction-action-audit/`, `2026-06-09-faction-stat-architecture-review/`, `2026-05-20-npc-priority-trees/`; `deprecated/archives/session/`, `deprecated/archives/session_handoff_2026_04_20.md`, `deprecated/archives/audit/2026-06-11-canon-flatten/canon_flatten_examination.md`.

*End of compendium.*





