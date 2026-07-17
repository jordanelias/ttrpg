# Valoria — A Speculative Companion to the Narrative Compendium (rev. after adversarial review)

**Status: SPECULATIVE ANALYSIS — proposals, extensions, and suggestions. Not canon, not ratified design.**
This is the companion to `2026-07-17-world-factions-npcs-narrative-assessment.md`. Where the assessment
*reads* the corpus, this document *extends* it: it fills the gaps the assessment named, proposes new
mechanisms, and grounds each in **real historical precedent — real actors, real politics — *alongside* the
acclaimed literary and narrative lenses**, using both rather than either alone. It ratifies nothing and touches no ledger, `CURRENT.md` row, or
module contract.

**This is a revised version.** An earlier draft leaned on literary lenses as the primary grounding; an
adversarial fidelity + cliché + historical-grounding review found that this inverted the corpus's own
discipline (its NPC anchors run ~15:1 real-historical to fictional, with the one fictional exception —
von Lohengramm — explicitly flagged as an outlier) and, three times, reached *past* a real precedent
already sitting in the paragraph being quoted. This revision corrects that — but the fix is *both/and*, not a
replacement: **every proposal now pairs a real precedent — drawn first from the repo's own `research/` corpus
and ratified canon — with its literary lens, each doing its own work.** The failure was relying *only* on the
literary (and, in three cases, reaching past a real anchor already in the paragraph); the correction is to
*add* the history the corpus demands, not to strip the literary that gives a mechanic its form and resonance.
The review's conceptual findings (a
Collision-class that flattened an asymmetric injustice into a symmetric tragedy; three proposals that
checked the wrong constraint; a stance mechanic that left out the very people it was about) are addressed
inline and summarized in Part IV.

- **Date:** 2026-07-17 · **Companion to:** the narrative compendium of the same date.
- **Governing constraint (the user's, and the right one):** extend curiously, fill gaps, propose — grounded
  in **precedent by real actors and real politics**, and *without* falling into cliché or pattern-matching.

## Currency inheritance (this companion depends on provisional ground)

The companion builds directly on material the assessment flagged as unsettled, and repeats the flags here so
a reader of *this* document alone is not misled:

- The Solmund cosmology it extends (the Forgetting, the Perceptual Prophylaxis, Certainty) is **DRAFT with no
  `CURRENT.md` row.**
- Several proposals build on the **~90%-unlanded comparative-governance research** (`research/governance/`,
  the two-signal primitive, the standing-as-currency finding).
- Load-bearing characters carry live contradictions (Almud's Thread Sensitivity reads **0** in the foils/
  analyses and **28** in `character_canon_v30.md`; the faction-personality model is split two ways).
- Varfell's "Path B" is **struck by GD-1**; the arcs are **illustrative samples superseded by Churn Engine v2.**

The consequence for Part IV's "free vs. needs-Jordan" split: a proposal is *not* free merely because it
doesn't touch load-bearing canon — it is also not free if the canon it *does* touch is itself unsettled.
That second test is applied below.

---
---

# PART I — THE GENERATIVE DISCIPLINE

Two rules govern everything that follows. The first is a positive commitment (lead with real history); the
second is a filter (the setting's refusals). Neither is a generator — the selection of *which* proposal to
make is a matter of judgment and taste, and this document does not pretend otherwise. What the two rules
guarantee is that whatever is proposed is *grounded* and *not a cliché*, not that it was mechanically
derived.

## 1. The primacy of real precedent

Valoria's defining strength — the thing that makes it more than a competent fantasy setting — is that it
grounds mechanics in **real historical cases, real political actors, and documented institutions**, then
adversarially fact-checks them, and bans the single most tempting ahistorical shortcut (the "Mandate of
Heaven," ruled "history only, never a Valoria mechanic"). Its NPCs are anchored to Manuel I Komnenos,
Catherine the Great, Isabella of Castile, Bellarmine, Rosa Luxemburg, Richard Sorge, William Marshal, Suger
of Saint-Denis, the Chernobyl liquidators. Its factions are anchored to the Hanseatic League, the Avignon
papacy, the Varangian Guard, the Investiture Contest, the British Raj.

The discipline for this companion follows directly: **before reaching for a novelist or a philosopher, find
the real actor and the real politics — first in the repo's own `research/` corpus, which was built for
exactly this and is mostly unused, then in the wider historical record.** The real precedent must be
*present* — its absence was the earlier draft's failure — but the literary lens is a genuine *co-contributor*,
not a decoration: the history supplies the mechanism, the actors, and the proof it can happen; the literary
lens supplies the *form*, the *register*, the *moral framing*, and the *question* that makes a mechanic
resonate. Use both. The corpus's own research self-audit states the principle this companion now obeys: *"the
methodology was the right work to do first. Without it, design proposals would have been built on ungrounded
intuition."* (`research/pre_firearms_formations/16_historical_vs_gamedesign_audit.md`.)

Where the earlier draft's literary lens turned out to be *replacing* a real anchor the corpus had already
established, this revision restores the real anchor *and keeps the literary lens working beside it*. In three
cases the history was in the same paragraph the draft was quoting, and had simply been ignored:

- **Altonia** already carries the ratified anchor *"Historical parallel: British India… the British managed
  religious institutions by granting them defined jurisdictional space"* (`canon/03_canonical_timeline.md`)
  — the draft rebuilt it from Coetzee.
- **The Crown–Church axis** already carries the ratified anchor *"Investiture Contest as Crown-Church axis
  precedent"* (`faction_canon_v30.md`) — the draft reached for Hegel's *Antigone*.
- **Doux Laskaris** already carries the anchor *"Demetrios Palaiologos surrendered Morea… partly because
  continued resistance would have destroyed the province and everyone in it, including his family"*
  (`npc_character_analyses_v30_infill.md`) — the draft reached for a Coetzee character one sentence away.

## 2. Valoria by negation — a filter, not a generator

The fastest way to write a cliché into Valoria is to ask "what would a good fantasy setting do here?" The
corpus has already refused almost every load-bearing fantasy convention, and those refusals make a useful
*filter*: any proposed addition should be run against them, and one that requires a refused convention is
almost certainly a cliché. (This is a check ideas must *pass* — not a machine that *produces* them; the
earlier draft overclaimed it as generative and "excavated," which the review correctly flagged.)

| The convention Valoria refuses | Where the refusal lives |
|---|---|
| The chosen one / prophecy | Solmund's motive is "genuinely unknowable"; no prophesied heir |
| The Dark Lord / the villain unmasked | "does not resolve into 'he was bad all along'"; every antagonist is sincere |
| Ancient evil sealed away | the Calamity is "a rendered-side mechanism… the fabric strains and tears" |
| Restore the rightful bloodline | deed-monarchy: "authority not earned this season is not authority next season" |
| Magic as power fantasy | threadwork costs Coherence; the Leap is "an epoché and a leap of faith" |
| The rebels who are simply right | the Restoration is "playing the ethics correctly and losing the game" |
| Grimdark nihilism | "No shared loss… Every crisis becomes a new chapter"; trauma is "constitutive finitude" |
| The exotic other-culture as flavor | the caste is "Altonian colonial residue," with numeric teeth |

Two refusals from the review must be added to the filter as explicit tests, because the earlier draft
tripped both:

- **Do not dignify an unjust position as a co-equal tragic good.** The caste's exclusion of the Southern
  Einhir is *not* an "ethical substance" symmetric with the case for their equality; canon frames Vaynard as
  "the only person who understands why the caste must end for the peninsula to survive." A mechanic that
  renders that as a 50/50 tragic dilemma has imported the cliché of false balance. (This repairs Part III's
  Collision class — see §III.3.)
- **Do not build a stance mechanic about a marginalized people that gives every faction a position except
  that people.** Real subordinated populations had documented strategies of their own; a compass of elite
  stances toward them, with no seat for their own agency, reproduces the "marginalized as object" cliché the
  caste's own design refuses. (This repairs the Omelas compass — see §III.4.)

---
---

# PART II — FILLING THE GAPS, REGROUNDED

Each gap the assessment named, filled with a proposal that leads with real actors and real politics.

## 2.1 Altonia and Schoenland — the empire known by its indifference

The gap: both are richly-instrumented *pressure systems* with almost no cast; the temptation is to give
Altonia a scheming emperor and a throne-room. Refuse it — but ground the refusal in the corpus's own
ratified anchor, not a novel.

- **Rule Altonia through one embedded face — the real model is the British Raj's District Collector.**
  `research/historical/precedents_analysis.md` already names the mechanism: a single resident
  magistrate-administrator holding revenue, judicial, and police authority per district, with no visible
  viceroy present across most of the territory. Lord Cromer's "Veiled Protectorate" in Egypt (1883–1907) —
  ruling through advisers inside a nominally sovereign Khedival government, never needing a throne-room
  because there was deliberately none — is the tightest real match for the design instinct "no scene ever
  takes place in the Altonian capital." **Doux Alexios Laskaris is this District Collector**, and his
  betrayal-through-attachment is already canon-anchored to **Demetrios Palaiologos's 1460 surrender of the
  Morea** (surrender-as-protection of his own family and province) — the real precedent the draft reached
  past. Use it.
- **The caste is Altonian residue the free duchies now maintain themselves — the real mechanism is
  cost-of-dismantling, not conscience.** `precedents_analysis.md` states it: post-independence India
  *"inherited the colonial administrative state… and modified rather than replaced it… dismantling it would
  have created chaos."* That is a documented, unsentimental answer to "why does a formerly-colonized people
  keep running the colonizer's own stratification" — sharper than any magistrate's private guilt, because it
  is structural, not psychological. Jim Crow (a stratification self-perpetuated for a century after the
  occupying Reconstruction authority withdrew) and the British-Indian census's hardening of caste categories
  (Nicholas Dirks, *Castes of Mind*) are the two closest "maintained without occupiers" comparanda.
- **The Almaic Kyriakos** — Altonia's dominant religion, named but undefined in canon — should be the mirror
  that *explains the Church of Solmund's own containment psychology*: a secure imperial orthodoxy that
  quarantined rather than destroyed the Church (as canon says the Raj managed Hinduism/Islam), whose galling
  quality is condescension, not malice.
- **Schoenland** is the corpus's one honest cynic — an island trade republic that "profits from tension,
  including caste tensions." Its real register is the mercantile neutral (Genoa, Ragusa, the arms-dealer
  city-state); lean into making it *charming* rather than menacing, with its homesick factor Solberg
  (anchored to Xenophon's Ten Thousand, already in canon) the human tell inside the cynicism.

*Cliché avoided:* the evil empire, the rival dark religion. *Grounding:* British Raj / District Collector,
post-colonial India, Cromer's Egypt, Demetrios Palaiologos — the last three already in the repo.

## 2.2 The three thin Cardinals — completing a real-anchor slot the corpus already has

The assessment flagged Klapp, Olafsson, and Jarnstal as one sentence each. The corpus's own convention
(every major NPC gets a named *historical* Inspiration) is the template to complete — not a parallel
literary-anchor convention.

- **Cardinal Arnlod Olafsson (Justice / Inquisition)** — "The Compromised Enforcer," whose heresy hunts fall
  disproportionately on the south. His grounding is *already cited* in canon: the Church is anchored to
  *"the Spanish Inquisition's pattern of using procedural law to enforce doctrinal categories on populations
  who didn't fit them"* (`faction_canon_v30.md`). The exact real mechanism is the **limpieza de sangre
  (blood-purity) statutes** (from the 1449 Toledo Sentencia-Estatuto onward) and the persecution of
  **conversos** — sacramentally orthodox Catholics targeted by *descent* regardless of sincere faith — which
  is precisely the Southern Einhir's position (legally within Church jurisdiction, hunted by ancestry).
  Olafsson enforces a doctrine he half-knows is really about blood. *(Caution, per the corpus's own
  adversarial discipline: cite the limpieza-de-sangre **system** and the well-attested presence of conversos
  within the Inquisition's own ranks, not the contested claim about Torquemada's personal ancestry.)*
- **Cardinal Magnus Klapp (Temperance / Knowledge)** — the scholar-archivist, anchor **Gerbert of Aurillac /
  Pope Sylvester II** (the churchman whose learning outran his peers so far that legend made him a sorcerer).
  Crucially, Klapp must be *differentiated from Haelgrund*, who is the same "sincere official whose competence
  delivers the forbidden truth" shape one Cardinal-seat over. The distinction is sharp and worth designing to:
  **Haelgrund's threat is perceptual** (he *senses* practitioners without knowing his own Thread Sensitivity —
  a field-inquisition danger), while **Klapp's is documentary** (he could *prove*, from the archive he curates,
  that the Church edited its own scripture — a scholarly danger). Perceptual vs. textual: two real routes to
  the same heresy, deliberately paired.
- **Cardinal Osten Jarnstal (Fortitude / Templars)** — "The Soldier Who Outgrew His Chain of Command." The
  draft called him "a pure Praetorian" and left the adjective unanchored; the real event is one file away:
  **the Praetorian Guard's murder of Pertinax and auction of the empire to Didius Julianus (193 AD)** after
  he tried to enforce discipline and cut their pay (`research/governance/conflicts_power_struggles.md`).
  Wallenstein — the Habsburg generalissimo assassinated in 1634 once his personal army's loyalty to *him*
  outweighed its loyalty to the throne — is the secondary color. Jarnstal is the substrate-*agnostic* soldier
  inside the substrate-*suppressing* institution, and in a Consecration Crisis his swords are a *factor the
  engine could weigh*, not a decree (see the seam note in §III).

## 2.3 The royal heirs — real hollow-crown and hostage-heir precedent

The assessment: Torben is "the most malleable named NPC… his Stance Triangle is largely blank"
(`npc_behavior_v30_infill.md` — this is the *corpus's* line, not the assessment's), and Elske is "almost
entirely defined by succession mechanics." Both gaps have precise real anchors.

- **Torben — the hollow crown, anchored to Henry VI of England.** Crowned an infant in 1422, dominated for
  decades by rival protector-dukes and then his queen, a real king around whose emptiness the Wars of the
  Roses were fought — which ties directly to the Crown's *own already-established* Wars-of-the-Roses anchor.
  The repo's research offers a darker escalation: the **Later Han child emperors** — Emperor Zhi, enthroned
  at seven and **murdered by his regent for calling him "a domineering general" to his face** (146 CE);
  Emperor Xian, held as a legitimating instrument by successive warlords for life — and **Toyotomi Hideyori**,
  the heir Hideyoshi trusted so little he chartered a five-elder council around the boy. Torben's interior
  fact is that he *knows* he is being shaped; the drama is whether any of his sculptors — his father included
  — ever treats him as a person rather than an instrument.
- **Elske — the hostage-heir who belongs to neither side.** The repo already has the structurally-identical
  institution: **sankin-kōtai** (1635–1862), under which daimyo heirs and wives resided permanently in Edo as
  de facto hostages — "a class of elite family members who structurally belonged to neither the home domain
  nor fully to the shogunal court" (`research/governance/governance_modes.md`). For the marriage-diplomacy
  mechanism specifically, Byzantine-coded Altonia suggests **Irene of Montferrat** (empress-consort of
  Andronikos II, who after 1303 set up her own independent court and finances at Thessalonica and fought her
  husband over her sons' succession) — a real foreign-born consort who "would not act as anyone's instrument"
  — or the Han **heqin** treaty-marriage system if a cleaner instrument fits. Her arc is the peninsula's one
  genuinely tender thread, and its danger is that tenderness is the one force the strategic layer cannot model.

## 2.4 The empty relational graph — author the edges, the corpus already wrote them as prose

The graph is fully specified and holds *zero* edges. The Ruler-Diamond edges are already written as prose in
the foils doc and need only to be *typed* — a real dynastic-politics exercise, not invention:

- Almud ↔ Lenneth: **Kinship** (marriage) + a latent **Rivalry** of method. *Design question raised, not a
  free authoring task:* the graph's own rule makes sworn-bond + rivalry mutually exclusive — does that
  exclusion cover Kinship + Rivalry, or does a real marriage where custody and reform coexist require the
  composition rule to be extended? Flag it (see Part IV), don't silently author past it.
- Baralta ↔ Vaynard: **Feud** at strength 2 (ideological), wired to suppress Solidarity per the graph's rule.
- Almud ↔ Ehrenwall: **Liege-vassal**, decaying — the Coup Counter *is* this edge's strain accruing.
- Feldhaus ↔ Virke: the **shared-vulnerability mirror** — a Patronage-adjacent tie with a hidden shared-strain
  channel (the Thread-tainted supply chain), so either's exposure damages both.
- Haelgrund ↔ Olafsson: **Liege-vassal** with a buried reversal (if Haelgrund's Thread Sensitivity surfaces,
  the vassal becomes the thing the liege hunts).

## 2.5 The missing arc types — build the battle arc on real battles

The arc corpus never tells certain kinds of story. The mass-battle-from-inside arc is the sharpest gap, and
the repo's pre-firearms research is a dense inventory of exactly the phenomenon — a battle decided by the
soldiers, not the general's plan — in *real, already-verified* engagements:

- **Hastings (1066)** — the feigned retreat worked because the Saxon shield-wall broke discipline to pursue,
  not because Harold ordered it. **Crécy (1346)** — French knights charged through their own crossbowmen for
  personal prestige, overriding the plan at the individual level. **Agincourt (1415)** — French nobles charged
  independently seeking glory, with no coordinated command at all. **Grandson (1476)** — the Burgundian line
  lost "without significant fighting because it believes itself to be losing," the purest morale-cascade on
  record. **Bannockburn (1314)** and **Ankara (1402)** add a subordinate detachment and a mid-battle defection
  deciding a campaign no plan controlled.
- The political (non-battle) version of "no one caused it" is the **Roman Third-Century Crisis** (explicitly
  grounded in the research as *endogenous, army-loyalty fission, never legitimacy draining from above*) and
  the **Venetian *barnaboti* collapse** ("decline by currency-debasement of standing itself, not by conquest
  of an intact hierarchy").

The other missing types — an arc *from inside* Thread practice (the interior of the Leap), a Warden arc about
*staying* rather than entering, a Torben arc — are authored to existing rules; the Warden one is where §III.1's
Attention economy does its work.

## 2.6 An Edeyja arc that does not break her — the decision is taken *from* her

The assessment calls Edeyja the biggest coverage gap *because* she is the fixed point everyone else arcs
relative to. The earlier draft's fix — giving her a yieldable decision about whether to let the Forgetting
thin — was correctly caught as breaking her: a character who can face a campaign-altering fork *is* a
variable, however it's dressed. The repair: **the decision about the Forgetting is made by others, about the
thing she guards, and she cannot control it.** Her arc is the *temptation to be understood* — the Buried
Giant fork (§III.5) is contested by the factions and the Wardens around her, and its resolution would either
end her solitude (the world finally able to see what she protects) or confirm it forever — but she is not the
decider. Her fixedness is that she keeps maintaining regardless of the ruling. That is a gravity well around a
constant, not an arc that moves it.

## 2.7 The naming logic — real colonial name-policy, real reclamations

Codify the two rules the corpus already follows (saga-Norse personal names + Hanseatic-German placenames for
the peninsula; imperial-Greek for Altonia) — and ground the one diegetic fact that makes naming *matter* in
real history the repo already cites: **Japan's *Sōshi-kaimei* (1939–1945), the forced adoption of Japanese
names in occupied Korea**, named in `precedents_analysis.md` as part of the occupation's cultural erasure. The
reclaiming half — that taking back an old Einhir name is a political act — is grounded in real
decolonization-era reclamations (Léopoldville→Kinshasa, Salisbury→Harare, Bombay→Mumbai). Naming is a site of
the caste conflict, not flavor.

---
---

# PART III — NEW MECHANISMS, REGROUNDED AND CANON-CHECKED

Each proposal below leads with real precedent, states the canon constraints it must clear (the earlier draft
checked only P-07/agency and missed P-08, the rule that the epistemic barrier is *metaphysical, not
institutional*), names the cliché it routes around, and flags whether it is **free** or **needs Jordan**.

## 3.1 The Attention economy — a designed "watch-only" office, not a mystic's virtue

**The idea.** A mode of *witnessing* orthogonal to the action economy: reading the world at depth reveals
Seam Texts, diagnoses a drifting practitioner's orphaned configurations, and perceives what acting would
destroy — the Warden's true discipline, and the one thing Edeyja does that no faction leader can.

**Real grounding (leads).** The corpus *already* anchors the Warden role to the **Chernobyl liquidators** —
the ~600,000 conscripted people who contained the 1986 disaster, maintaining a failing substrate others
could not perceive, at the cost of their own bodies, with no combat verb available (`edeyja_npc.md`'s
companion analysis anchors Warden Orm exactly here). Extend that anchor to the whole Warden institution.
For the *institutional* mechanism — how a "watch-only" office is *designed* — the model is the **Han Regional
Inspectors (*Cishi*, 106 BCE)**: thirteen roving overseers whose entire function was audit-by-observation and
who were *deliberately kept junior in rank* (600-*shi*, below the governors they watched) so they could not
accumulate independent executive standing (`research/governance/governance_modes.md`). The **Roman Censor's
*regimen morum*** (an office of watching, enrolling, certifying, with no command attached) and **augural
*obnuntiatio*** (an augur could *halt* a magistrate's action by announcing an unfavorable reading, never
executing anything — Bibulus used it against Caesar in 59 BCE) are the two closest "perception nullifies
action without touching it" precedents.

**Literary lens (what it adds).** Simone Weil's *attention* and *décréation* supply what the institutional
history cannot: the *ethics and phenomenology* of a mode that gives precisely because it does not grasp — the
reason a "watch-only" office is a spiritual discipline, not merely an audit function. The Cishi and the
liquidators tell you how to *build* it; Weil tells you why it *matters*, and how it should *feel*.

**Canon check.** P-01 is satisfied (attention *alters nothing*, so co-movement has nothing to move). **The
real risk is P-08 / Foundations §10.1** (thread-perception requires repeated confrontation; study alone
cannot cross the barrier). So Attention must **reveal depth proportional to the character's existing Thread
Sensitivity** — it is not a zero-cost route to thread-level perception for a TS-0 scholar (which would be a
P-08 workaround); a low-TS observer reads a Seam Text as devotion still, and gains only what their sensitivity
already licenses. This preserves "the scholar gets a seat" honestly: the scholar's seat is *interpretation and
diagnosis at their own TS*, not free enlightenment.

**Cost.** The earlier framing ("turns not spent acting") priced Attention at *zero* for its target archetype
— a scholar wasn't going to spend the turn fighting anyway. Give it a real cost for everyone: an Attending
character forgoes a **concealment** they can't take back (deep observation is *noticed* — the Cishi were
resented precisely because everyone knew they were watching), and sustained Attention near the wound carries
the Warden's own hazard exposure. *Needs Jordan* (a new resource and mode of play).

## 3.2 Belief as a rendering force — the political readout is real, the metaphysics is Borges

**The idea.** A territory's orthodox belief-density thickens the rendered orthodox surface: where belief is
dense, Seam Texts read as pure devotion and the deep world is buried; where it thins, the Ground shows
through. This unifies Church Influence, the Perceptual Prophylaxis, and the map's complementary
Church/Restoration gradients.

**Real grounding (the *political* half).** The metaphysical claim — belief altering what is legible — is by
design fictional, and Borges's "Tlön, Uqbar, Orbis Tertius" is the one place in this document a literary lens
does *irreplaceable* work (no real precedent grounds "collective belief edits ontology"). But the political
*manifestation* the proposal actually cares about — why orthodox territories behave differently, why the
Church's saints are its "densest fog" — has tight real grounding the corpus already holds: the **mask-vs-
substance** primitive (Cao Cao's Xu court issuing "Han" edicts everyone performs as real —
`governance_modes.md`); **Roman *damnatio memoriae*** and **Doge Marino Faliero's blanked-out portrait in the
Sala del Maggior Consiglio** ("still there today") as permanent visible erasures doing ongoing political work
(`political_hierarchy_standing.md`); the **"myth of Venice"** finding that legitimacy was maintained partly by
*archival suppression of contentious politics*; and, since Altonia/the Church are Byzantine-coded, the
**Byzantine *basilikos logos* tradition** (Menander Rhetor's codified imperial-praise template, Agapetus's
*Ekthesis* to Justinian) — a real rhetorical technology whose point was *performing/constituting* legitimacy,
not describing it.

**Canon check.** P-07 is cleared (nothing is attributed to the Ein Sof; the force is entirely rendered-side —
the aggregate of minds performing the world, which P-03 licenses). **But the earlier "canon-clean" claim was
false**: making Thread-Sensitivity *development* a function of Church Influence (a political stat)
re-institutionalizes a barrier P-08 insists is *not* institutional. So the belief-density field may govern
*legibility* (how the surface reads, a rendered-side effect) but must **not** be the gate on whether a
character can *develop* TS — that stays confrontation-driven per §10.1. *The TS-development coupling is a real
P-08 tension and needs Jordan;* the legibility effect alone is the safer version.

## 3.3 The Collision event class — grounded in the Investiture Controversy, and guarded against false balance

**The idea.** An event grammar distinct from a conflict: where a conflict has a winner, a Collision *withholds
the clean outcome* — two positions, each genuinely defensible within its own order, resolved only by wounding
one.

**Real grounding (leads, and fixes the flaw).** The earlier draft used Hegel's *Antigone* and — fatally — its
headline example was **Baralta ↔ Vaynard**, which canon makes *asymmetric* (Vaynard understands "why the
caste must end for the peninsula to survive"). Rendering an oppressed people's *existence* as a 50/50 tragic
dilemma is exactly the false-balance cliché the setting refuses. The repair is to ground the class in the real
case the corpus *already* names for the Crown-Church axis: the **Investiture Controversy (1075/76–1122)**,
which `conflicts_power_struggles.md` independently flags as the paradigm two-signal collision —
*"resolved by partition (Concordat of Worms 1122), not victory."* Two authorities, each structurally correct
within its own order (royal administrative necessity vs. Gregorian sacramental integrity), and *neither gets
what it originally claimed* — the office is split (spiritual investiture to the Church, temporal to the
Emperor). That is the literal template for "withholds the clean outcome," and it is genuinely *symmetric*, as
the class requires.

Two resolution-*shapes* come from more real cases: the **Nanboku-chō schism (1336–1392)** — two
simultaneously-legitimate emperors for 56 years, "resolved" by an alternating-succession promise the Ashikaga
then broke (*the resolution is itself the second wound*); and the **Palatinate electorate dispute (1623/1648)**
— resolved not by reversing the stripped title but by *creating an eighth electorate*, diluting both claimants.

**The guard (required).** The Collision class must carry an explicit restriction: **it may only be applied
where both positions are genuinely defensible within their own order.** Where one side is substantively
correct — the caste's existence, the Southern Einhir's claim to exist as a people — the situation is *not* a
Collision; it is an **asymmetric injustice**, whose drama is the different and harder one of a just cause that
pays a terrible price or loses (the tragedy of *Antigone* read from Antigone's side, or of the Stellinga
revolt below). Baralta ↔ Vaynard stays that asymmetric case, with the caste's injustice intact. Applying the
"no right answer" mechanic to it is a design error the class is built to prevent.

**Literary lens (what it adds).** Hegel's reading of *Antigone* — two ethical substances, each right within
its own order — supplies the *conceptual clarity* the historical cases only illustrate: it names precisely
*why* a true collision has no clean outcome, and, read from Antigone's own side, it is also the frame for the
*asymmetric* injustice (the just cause that pays a terrible price). The Investiture Controversy is the
mechanism; *Antigone* is the idea it enacts, and the reason the guard against false balance matters. *Needs
Jordan* (a new event grammar).

## 3.4 The Omelas compass — with the Southern Einhir's own documented stances

**The idea.** The peninsula's settlement rests on the Southern Einhir's exclusion; every embedded actor holds
a standing posture toward that fact, which gates which actions read as coherent and drifts under outcomes.

**Real grounding (leads).** Canon already states the mechanism without a fable: the caste is *"the structural
consequence of the south's exclusion from the war coalition's leadership"* (`canon/03_canonical_timeline.md`)
— a real, common pattern (a marginal co-belligerent excluded from a founding settlement). The **Ottoman
*devshirme*/*kul* system** is the tightest real "the order runs on this population's marked status" case: the
Janissaries and much of the administrative elite were levied Christian boys, converted and *legally severed
from kin and inheritance* — their subordination *was* what made them trustworthy to the state
(`political_hierarchy_standing.md`). **Sparta's Helots** are the closest real "openly-admitted subsidized
order" (an entire citizen class built on a subject population, with institutionalized terror — the
*krypteia*). And **Jim Crow** and the **British-Indian census caste** are the "maintained without occupiers"
cases from §2.1.

**The repair — give the marginalized their own stances.** The earlier draft's four poles (Uphold/Reform/
Refuse/Walk-Away) were *all elites*; the mechanic about the Southern Einhir left them out. Real subordinated
peoples had documented strategies, and the compass must include them as *subjects*: the **Stellinga revolt
(Saxony, 842–843)** — subordinated freedmen who rose to reclaim pre-conquest status *the moment elite
coercive unity fractured* during the Carolingian civil war (not spontaneous virtue — a real trigger condition,
and precisely how the Restoration Movement should activate: exploiting the Almud/Baralta/Vaynard/Church
fracture); the **converso** strategy of assimilation-within (outward conformity, private persistence); the
Messenian-revolt "Refuse from within"; and the Korean-underground "endure and transmit" (cultural persistence
through occupation). So the compass is two-sided: elite postures *toward* the subsidy (devshirme's beneficiaries)
**and** the subordinated population's own postures — *assimilate, persist, revolt (on the Stellinga trigger),
or exit* — the "bitter agency of the unseen" the assessment's Ellison reading (below) insists on.

**Vocabulary fix.** Do not call the political version a "subsidy" — Le Guin's term names a *magically
necessary* causal link, and using it smuggles the metaphysical framing into the political mechanic. Call it
**the founding exclusion** (or "the settlement's bargain"). Reserve any "subsidy" language for the explicitly
metaphysical version, which contradicts the Warden-driven Mending trajectory and *needs Jordan* — the political
compass itself is free to build.

**Literary lens (what it adds).** Le Guin's "Omelas" supplies the *moral architecture* the mechanisms need:
the specific ethical weight of *knowing* the cost and choosing anyway, and the fourth stance — walking away —
that a devshirme-or-Helot analysis alone would never surface. The history proves such orders exist and
endure; "Omelas" is what makes *a stance toward one* a moral act rather than a bookkeeping entry.

## 3.5 The Buried Giant fork — a legislated non-remembering pact, not a liftable mist

**The idea.** As Warden work and Thread revelation advance, the peninsula approaches a threshold where the
factions must contest whether to force the Forgetting to *thin* — a genuine campaign-scale Collision (§3.3),
not a quest.

**Real grounding (leads, and fixes a canon-precision problem).** The earlier draft used Ishiguro's *Buried
Giant* — a supernatural *mist* over people who once knew — which is a *loose fit for canon*: P-13/P-08 make
the Forgetting an *individually-developmental epistemic finitude* ("evidence is available; the capacity to
render it as knowledge is not"), not an externally-imposed veil. The real precedent fits both better: the
**Athenian Amnesty of 403 BCE**, after the Thirty Tyrants — citizens swore *μὴ μνησικακεῖν* ("not to recall
past wrongs"), a *legislated, bounded, exception-carrying* non-prosecution pact (Andocides, *On the
Mysteries*; Aristotle, *Ath. Pol.* 39–40). Because it is a **political-legal** mechanism, not a supernatural
one, it is compatible with P-13: the "thinning" is not a lifting of the metaphysical barrier but a *political*
decision to reopen records, testimony, and prosecution about the Catastrophe's blame, the caste's origin, and
the assassination — things non-sensitives *can* hold as propositional history even if they cannot render the
Southernmost's danger. **Spain's *Pacto de Olvido* (1977) and its contested reopening (2007/2022)** is the
living "no clean answer, still argued today" case — a negotiated non-remembering that bought stability, later
reopened by a generation asking whether the mercy was a wound.

**The stakes stay both-sided:** reopen it, and the Restoration's grievance becomes undeniable *and*
combustible; leave it, and the peace holds atop a bargain no one will name. Neither is the good ending. *Needs
Jordan* (makes the Forgetting a decision; implicates the un-named endgame ritual — the biggest single narrative
call the setting has deferred).

**Literary lens (what it adds).** Ishiguro's *Buried Giant* supplies the *question* that makes the fork more
than a policy choice — *is forgetting a wound or a mercy?* — and the mood of a whole society quietly
organized around a shared not-remembering. The Athenian Amnesty is the legal mechanism; Ishiguro is the ache
that makes a table hesitate before either answer.

## 3.6 The archive and the Testament — real accountability instruments

**The Deep Archives** ("pre-Catastrophe records containing inconsistencies… a Thread artifact") are named and
unused. Ground them as instruments of *contested memory*, using both a form and a politics: the Nabokov
*Pale Fire* structure (a fixed text whose meaning lives in the gloss the player's growing knowledge writes)
supplies the *form* — how a document can betray itself on re-reading — while the real register of *why* an
archive is a battlefield is **archival suppression as political technology** (the "myth of Venice" /
*damnatio memoriae* material from §3.2). The Deep Archives are where the Buried Giant fork (§3.5) is
*researched*.

**The Testament** — a first-person artifact a dying leader or Warden leaves, carrying their Belief forward —
works best as *both* a moving personal document and an audited instrument. Robinson's *Gilead* supplies the
*register* the design should keep — grace, the dying first-person voice, a testament written to a successor —
while the **Doge's *Promissione Ducale*** and the ***Inquisitori sopra il Doge defunto*** (`governance_modes.md`)
supply the *teeth* the register alone lacks: the Doge's oath was re-drafted and lengthened at *every*
accession by a standing magistracy closing off the previous Doge's abuses, and a posthumous audit could
*fine his estate before his heirs inherited*. A Testament that is *both* Gilead-tender *and* reckoned against
after death — formally audited by a successor institution — is richer than either alone.
**Hideyoshi's 1598 deathbed charter of the Go-Tairō** is the
secondary case (a testamentary instrument establishing the governance meant to carry a dead ruler's intent
forward). *Free* (additive artifact + a real accountability mechanic).

## 3.7 The reader as renderer — the one place the literary lens is primary, honestly

**The idea.** For the no-GM seam (P-03 says only minds render; the engine is not a mind): the *player's*
consciousness renders; the engine computes the substrate and presents it, addressed in the second person
(which the voice canon's "you who enter this house" register is already half-built for).

**Honest grounding.** This is the one proposal where a real-political precedent would be a *strained* fit —
it is an engine-epistemology question, not a politics question — so **Calvino's *If on a winter's night a
traveler* stays primary**, and this document says so plainly rather than manufacturing a historical costume.
If a real-world angle is wanted, the closest is legal epistemology's real shift from **trial by ordeal/combat**
(an external mechanism renders the outcome) to **trial by jury** (a body of doubting peers becomes the
renderer of fact) — a documented case of an institution moving "who makes reality legible" from an external
mechanism to a body of witnesses. Keep it secondary.

**The cost the draft ignored.** If *only* the player renders, engine-computed NPCs would, by P-03's own logic,
have no experience when unobserved — an implicit solipsism in tension with the NPC design's insistence on
*sincere, interior* antagonists (Almud's private doubt, Himlensendt's private faith). The resolution must
therefore hold that **NPC consciousness is itself modeled as rendering** (the engine computes their rendering
too, off-screen), not that the player is the sole renderer. Weigh this cost explicitly; do not claim
"canon-preserving" without it. *Needs Jordan* (an engine-architecture fork, as the assessment argues).

## 3.8 The drama of the unsaid (Chekhov) — naming an existing discipline

A small, honest note rather than a new mechanism: the corpus *already* has "boring by design" characters and
a voice canon that "never performs its own secrets." Chekhov is the *name* for that existing discipline
(subtext over escalation — the Belief a character does *not* voice, the deviation they *decline*), not a new
rule. The design suggestion is only to *trust* it: let a pivotal scene be quiet. *Free* (it's already policy).

## 3.9 The three-body ratchet — designing so all three always win (and Almud's impossible choice)

**The idea.** Design the three principals so that *every* political exchange leaves all of them ahead — and
therefore settles nothing. If Baralta, Vaynard, and Almud each wield moves that win *whatever* the opponent
does, no contest is ever resolved; the stakes only ratchet, season over season, until the whole board is
wound tighter than any single actor intended. **The escalation *is* the point:** it is what keeps the
strategic layer relentless and its tension from ever plateauing. This is a structural engine, not a scene.

**The corpus already holds the seed.** Baralta's *"Penitent's Gambit"* is a fully-worked no-lose move: a
Parliamentary motion *"phrased so precisely that Cardinal Justice must either accept it (establishing that
Church authority requires Parliamentary authorisation) or reject it (proving the Church considers itself
above Parliament). Either way, Hafenmark wins the argument"* (`arcs/simulated/arcs_10_18.md`). Vaynard's
equivalent works through *"Tribune intel"* and his hidden Collection — winning by controlling the
documentation and the framing rather than the vote. And a faction-identity canon review already names the
third: *"Almud = best player at the table playing defense on all fronts — weaponizes the Einhir question,
redirects threats into each other, wins late by absorbing wreckage"*
(`deprecated/archives/session/session_log_archive_part_7.md`).

**Real grounding (leads).** The shape is a named piece of political sociology: **Georg Simmel's *tertius
gaudens*** — the third who rejoices, profiting from the other two's conflict, and its active form
*divide et impera*. That is Almud exactly: he does not defeat Baralta or Vaynard, he *turns them on each
other* and banks the wreckage. His own anchor, **Manuel I Komnenos** ("six simultaneous threats through
strategic patience"), and **Bismarck holding the balance** (the honest broker who kept rivals in tension so
his own power profited) are the real statesmen of precisely this craft. The no-lose forced dilemma has a
historical archetype the corpus's own arc already invokes: **Canossa (1077)**, where Gregory VII (by
absolving a penitent king) and Henry IV (by forcing the priest to absolve him) *both* walked away claiming
victory from the same act. And the escalation the mechanic produces is the real **"war of increments"** of a
multipolar balance — the security-dilemma ratchet in which each crisis is settled in a way that leaves every
party more dangerously positioned than before (the pre-1914 concert; the Warring States; the Italian-Wars
balance Machiavelli anatomizes).

**Literary lens (what it adds).** Tragic **peripeteia** — the reversal in which the very act that looks like
a triumph is the seed of the fall — supplies the register the engine needs: the player must *feel* that each
"win" tightens a noose none of the three can see, so the ratchet reads as mounting dread rather than
stalemate. And the figure of the **impossible-choice statesman** — the ruler whose greatness is measured by
loss *averted*, never victory *won* — is what makes Almud playable as a person rather than a chess engine:
he is assailed from every direction at once, and canon should never hand him a *right* answer, only a *best*
one. That constraint is his character.

**The design.** (1) Give each principal a signature *no-lose forced dilemma* — Baralta's exists; author
Vaynard's documentation-trap and Almud's redirect-and-absorb. (2) Make the moving quantity the *stakes*
themselves: every exchange increments a peninsula-scale pressure (Turmoil, the "war of increments") even as
each actor wins *locally*, so the board escalates while no contest resolves. (3) Author Almud explicitly as
*tertius gaudens*: his win condition is not to prevail but to be *still standing, and still choosing*, when
the other two have spent themselves — and every choice he is offered is best-not-right, a selection of which
fire to let burn. This is the engine that makes the campaign's tension monotone-increasing, and it pairs
directly with the Collision class (§3.3): a Collision is what fires when the ratchet finally forces a stake
no one can win their way out of. *Needs Jordan* (a structural commitment on how the political layer
escalates, and a character-design ruling that Almud never gets a right choice).

---
---

# PART IV — THE DISCIPLINE OF REFUSAL

## 4.1 The cliché test (revised — two questions added the earlier draft failed)

Before any addition — from this document or later — run it through these questions. Each is drawn from a
refusal the corpus has made. The last two are *new*, added because the earlier draft applied the first five
carefully and then failed on exactly the risks it hadn't written a test for.

1. **Does it require a villain?** If it only works because someone is *evil* rather than sincere, it
   contradicts the foundational stance.
2. **Does it resolve the mystery?** If it explains Solmund, the Ein Sof, or the wound, it violates the ruled
   refusal-of-resolution.
3. **Does it reward power without cost?** Every strong act must cost the actor or the world.
4. **Does it make a good ending?** If a fork has a *right* answer, it is a false dilemma, not a Collision.
5. **Does it treat the marginalized as a device?** They are subjects (including the bitter agency of the
   unseen), not people to be rescued, corrupted, or made to seethe.
6. **(NEW) Does it dignify an unjust position as a co-equal tragic good?** False balance is its own cliché.
   The caste's exclusion is not an "ethical substance" symmetric with the case for equality; a mechanic that
   renders it 50/50 has smuggled in the false-balance failure. (This is the test the Collision class failed
   and now carries a guard against — §3.3.)
7. **(NEW) Does a mechanic *about* a marginalized people give them a seat in it?** A compass of elite stances
   *toward* the Southern Einhir, with no position for their own documented agency, reproduces the
   marginalized-as-object cliché even while claiming to oppose it. (This is the test the Omelas compass failed
   and now passes via the Stellinga/converso stances — §3.4.)

And one meta-test, from the historical-grounding review: **is the real precedent already in the paragraph you
are quoting?** Three of the earlier draft's proposals reached past a ratified canon anchor (British India,
the Investiture Contest, Demetrios Palaiologos) for a more citable novel. Check the source you are already
citing before importing a lens.

## 4.2 What is free, and what needs Jordan (with the settled-canon test)

The earlier draft's split was found self-contradictory (it filed items as "free" that were built on
needs-Jordan mechanics). This version applies two tests, not one: a proposal is free only if it *both* (a)
adds no new mechanic/touches no load-bearing canon, *and* (b) the canon it touches is *settled* (not DRAFT
Solmund cosmology, not the ~90%-unlanded governance research).

**Free — texture/authoring on settled ground:**
- Altonia/Schoenland regrounding (§2.1) — texture within existing pressure systems; all anchors ratified.
- The three Cardinal characterizations (§2.2) — completing the corpus's own real-anchor slots.
- The royal-heir characterizations (§2.3) — authored to existing rules.
- The relational-graph edges (§2.4) — **except** Almud↔Lenneth's Kinship+Rivalry composite, which raises a
  live composition-rule question (does the sworn-bond/rivalry exclusion cover it?) and is therefore a *design
  question*, not free authoring.
- The missing arc *types* (§2.5) and the naming-logic codification (§2.7) — to existing rules.
- The Testament's accountability mechanic (§3.6) and the Chekhovian subtext discipline (§3.8) — additive/
  already-policy.

**Needs Jordan — new mechanic, engine fork, or unsettled ground:**
- **The Attention economy (§3.1)** — new resource + mode of play, and its P-08-safe design (reveal
  proportional to TS) is a real constraint call.
- **Belief-as-rendering-force (§3.2)** — the legibility field is a new mechanism; the *TS-development
  coupling* is a genuine P-08 tension; and it extends the DRAFT Solmund cosmology (unsettled ground).
- **The Collision event class (§3.3)** — a new event grammar, and the guard against false balance is itself a
  design commitment.
- **The Omelas compass** (§3.4) — the *political* two-sided compass is free to build; the *metaphysically
  literal* "subsidy" version contradicts the Mending trajectory and needs a ruling.
- **The Buried Giant fork (§3.5)** — makes the Forgetting (DRAFT P-13 territory) a decision and implicates the
  un-named endgame ritual; the single largest deferred narrative call.
- **The reader-as-renderer resolution (§3.7)** — an engine-architecture fork with a real philosophical cost
  (NPC rendering) to weigh.
- **The three-body ratchet (§3.9)** — a structural commitment on how the political layer escalates (every
  principal wields no-lose moves, so stakes ratchet and never resolve), plus a character ruling that Almud
  never gets a *right* choice, only a best one.
- **The Edeyja arc (§2.6)** — free to *sketch* her stance, but its payoff is *gated on the §3.5 ruling* and so
  cannot be finalized independently.

## 4.3 On the literary lenses — what each one adds (honest accounting)

The proposals use *both* real precedent and literary lens, because they do *different* work. The real
precedent supplies the mechanism, the actors, and the proof that such a thing can happen and endure; the
literary lens supplies the form, the register, the moral framing, and the question that makes the mechanic
*resonate* at the table. Neither alone is enough — the earlier draft's error was using *only* the literary;
the correction is to add the history beside it, not to strip the literary out. What each contributes:

- **A few lenses do work no real precedent can** — **Borges** (belief-edits-ontology has no real analogue by
  design — §3.2's metaphysical half) and **Calvino** (the reader-as-renderer is an epistemology question, not
  a politics one — §3.7). Here the literary lens genuinely *leads*.
- **The rest pair a real mechanism with a literary framing, both load-bearing**: the Investiture Controversy
  supplies the Collision mechanism and *Antigone* supplies the idea it enacts; the Cishi and the liquidators
  supply the Attention office and Weil supplies its ethics; the Athenian Amnesty supplies the Buried Giant
  pact and Ishiguro supplies its unanswerable question; devshirme and the Stellinga revolt supply the Omelas
  compass and Le Guin supplies its moral weight; the British Raj supplies Altonia's mechanism and Coetzee
  supplies the magistrate's interiority; the Promissione Ducale supplies the Testament's teeth and Robinson
  supplies its voice. In each pair, remove *either* and the proposal is poorer.
- **Two lenses the corpus already uses** — a fidelity note, not a demotion: **Ishiguro** and **Borges** are
  *both already named* in the canonical voice doc (`narrative_voice_canon_v30.md`) as two of its twelve style
  authors (for grammatical register), and Borges recurs in the ratified Churn Engine v2 grounding. This
  companion's use of them for *theme/mechanism* is an **extension of an existing influence** — a *stronger*
  footing than the earlier draft's "not yet used," made honestly.

---

## APPENDIX — THE PRECEDENT LEDGER (real precedent + literary lens, both load-bearing)

The reground in one table. **Each proposal draws on both:** a real precedent for the *mechanism*, and a
literary lens for the *form, register, question, or moral framing*. Real precedents from the repo's own
corpus are marked ⟢; the rest are the wider historical record.

| Proposal | Real precedent (the mechanism) | Literary lens (what it adds) | Status |
|---|---|---|---|
| Altonia through one face (§2.1) | ⟢ British Raj / District Collector; ⟢ post-colonial India retained-state; ⟢ Demetrios Palaiologos; Cromer's Veiled Protectorate | Coetzee (the magistrate's interiority; "never show the capital") | free |
| Cardinal Olafsson (§2.2) | ⟢ Spanish-Inquisition anchor → limpieza de sangre / converso persecution | — | free |
| Cardinal Klapp (§2.2) | Gerbert of Aurillac; differentiated from Haelgrund (documentary vs. perceptual) | Nabokov (the self-betraying text — the form, §3.6) | free |
| Cardinal Jarnstal (§2.2) | ⟢ Praetorian Guard / Didius Julianus (193 AD); Wallenstein | — | free |
| Torben (§2.3) | Henry VI; ⟢ Han child-emperors (Zhi, Xian); ⟢ Toyotomi Hideyori | — | free |
| Elske (§2.3) | ⟢ sankin-kōtai; Irene of Montferrat; ⟢ Han heqin | — | free |
| Mass-battle arc (§2.5) | ⟢ Hastings/Crécy/Agincourt/Grandson/Bannockburn/Ankara; ⟢ Third-Century Crisis; ⟢ barnaboti | Tolstoy (history as the integral of small wills — the frame) | free |
| Naming as contest (§2.7) | ⟢ Sōshi-kaimei (Korea 1939–45); decolonization reclamations | — | free |
| Attention economy (§3.1) | ⟢ Chernobyl liquidators; ⟢ Han Cishi; Roman Censor/*obnuntiatio* | Weil (the ethics & feel of attention) | needs Jordan |
| Belief-as-rendering (§3.2) | ⟢ mask-vs-substance (Cao Cao); ⟢ damnatio memoriae / Faliero; ⟢ basilikos logos | **Borges (primary — metaphysical half, irreplaceable)** | needs Jordan |
| Collision class (§3.3) | ⟢ Investiture Controversy → Concordat of Worms; ⟢ Nanboku-chō; ⟢ Palatinate electorate | Hegel/*Antigone* (the idea the mechanism enacts) | needs Jordan |
| Omelas compass (§3.4) | ⟢ excluded-from-coalition (canon); ⟢ devshirme; ⟢ Stellinga revolt; Sparta Helots; Jim Crow | Le Guin (the moral weight of knowing the cost) | political free / metaphysical needs Jordan |
| Buried Giant fork (§3.5) | Athenian Amnesty (403 BCE); Pacto de Olvido (1977/2007/2022) | Ishiguro (the question: wound or mercy?) | needs Jordan |
| Testament (§3.6) | ⟢ Promissione Ducale + posthumous audit; ⟢ Hideyoshi's Go-Tairō charter | Robinson (the dying first-person voice; grace) | free |
| Ellison / non-perception | Jim Crow testimony-discounting (cross-refs §3.4) | Ellison (the phenomenology of invisibility) | free |
| Reader-as-renderer (§3.7) | trial-by-ordeal → trial-by-jury (secondary) | **Calvino (primary — epistemology, honest)** | needs Jordan |
| Three-body ratchet (§3.9) | ⟢ tertius gaudens (Simmel); Manuel I Komnenos; Bismarck's balance; Canossa 1077; the "war of increments" | tragic peripeteia; the impossible-choice statesman | needs Jordan |

*Closing word on method.* The corpus's own research self-audit is the standard this revision now meets:
*"the methodology was the right work to do first. Without it, design proposals would have been built on
ungrounded intuition."* The earlier draft's failure was not using famous books — it was letting a famous book
do a job a real actor and a real politics was already doing, in the same paragraph, better. Precedent as
structure, drawn first from the history the corpus already researched, and never as costume.

*This is a companion for thinking with, not a plan of record. Pursue the free items freely; raise the
needs-Jordan ones as the design calls they are.*

*End of companion (revised after adversarial review).*


