# Valoria — Cast & Culture Expansion (proposals)

**Status: SPECULATIVE ANALYSIS — proposals and suggestions. Not canon, not ratified design.**
A companion to the 2026-07-17 narrative compendium and its speculative companion. Three jobs: (A) consolidate
the **full existing cast** so every suggested NPC is in one place; (B) **suggest new NPCs in critical
under-served areas**; and (C) **intensify the cultural texture** of factions, provinces, and settlements. It
ratifies nothing and touches no ledger, `CURRENT.md` row, or module contract.

**Disciplines this document obeys:**
- **Grounding is both/and** — every suggestion leads with a real-actor / real-politics precedent (drawn first
  from the repo's own `research/` corpus and canon) *and* keeps a literary lens where it adds form or register.
- **Canon constraints hold** (P-01–P-15): the caste is Altonian colonial residue (never an innate trait);
  monstrosity is ontological, not moral; Solmund is never resolved; the Forgetting is metaphysical, not
  institutional.
- **Naming follows the corpus's onomastics** — saga-Norse personal names + Hanseatic-German placenames for the
  peninsula; imperial-Greek for Altonia; **never the CI-blocked deprecated name**. Every *new* proper noun here
  is a **proposal**, not a registry allocation: before any canonization it needs an `id_reservations.yaml`
  allocation and the `placeholder_names` "contamination audit" that confirms the name's identity is correct
  (the discipline that struck `vaynards_hall`). Names are checked against the 46 existing entries for collision.
- **Roster capacity is real** — `npc_behavior_v30` caps ~35 "Active" NPCs. These suggestions are deliberately
  targeted at gaps, not proliferation; most would enter as **Passive/Background** tier and be promoted only on
  recurrence.

---
---

# PART A — THE CONSOLIDATED CAST (all 46 suggested NPCs)

The full roster from `references/npc_registry.yaml` — **35 canonical + 11 proposed** — so every suggested NPC
is available in one view. (● = richly drawn; ◐ = sketched; ○ = one-line/template.)

## Founding factions & Crown

| # | Name | Faction | Role | Depth |
|---|---|---|---|---|
| 016 | **Almud Almqvist** | Crown | King (the *tertius gaudens* statesman) | ● |
| 019 | **Lenneth Almqvist** | Crown (royal) | Queen / Widow-Regent; reformist | ● |
| 018 | **Torben Almqvist** | Crown (royal) | Prince, heir apparent (the malleable heir) | ◐ |
| 017 | **Elske Almqvist** | Crown (royal) | Princess, married to Doux Laskaris | ◐ |
| 009 | **Gerik Strand** | Crown | Lord Steward (OVERPERFORMER; William Marshal) | ● |
| 008 | **Peder Almstedt** | Crown (Ministry) | Chief Parliamentary Clerk (the *logothetes*) | ● |
| 020 | **Kolbrun Thale** | Crown (Inner Circle) | Spymaster | ○ |
| 023 | **Wilhelm Voss** | Crown (Inner Circle) | Royal Marshal | ○ |
| 024 | **Annalie Reichard** | Crown (Inner Circle) | Lord Treasurer | ○ |
| 022 | **Theodor Kreutz** | Crown / Löwenritter | Royal Guard Captain, liaison | ○ |
| — | **Hedda Kronvald** *(proposed)* | Crown | Governor of Ehrenfeld (T14) | ○ |
| 028 | **Inge Baralta** | Hafenmark | Duchess (the no-lose claimant; Isabella+Henry VIII+Theodora) | ● |
| 026 | **Torvi Heljason** | Hafenmark (Council) | Legal Advisor to Baralta | ○ |
| 027 | **Olaf Geirson** | Hafenmark (Council) | Military Commander | ○ |
| — | **Uta Falkenrath** *(proposed)* | Hafenmark (Council) | Commune Representative (Banneret) | ○ |
| 029 | **Magnus Vaynard** | Varfell | Duke, "the White Wolf" (von Lohengramm) | ● |
| 001b | **Maret Uln** | Varfell | Practitioner / succession fallback (Richard Sorge) | ● |
| 030 | **Björn Holdar** | Varfell (Jarl Council) | Senior Jarl of the Western Highlands | ○ |
| 031 | **Ingrid Stenskald** | Varfell (Jarl Council) | Skald-Chief (law-speaker) | ◐ |
| — | **Njal Torberg** *(proposed)* | Varfell (Jarl Council) | Military Jarl | ○ |

## Church, Löwenritter, Guilds, Restoration, independents & Altonia

| # | Name | Faction | Role | Depth |
|---|---|---|---|---|
| 015 | **Arne Himlensendt** | Church | Confessor ("the most dangerous person on the peninsula"; Bellarmine-adjacent) | ● |
| 013 | **Aldric Tormann** | Church | Cardinal of Prudence (OPTIMISER; Suger of Saint-Denis) | ● |
| 038 | **Arnlod Olafsson** | Church | Cardinal Justice / Inquisition | ◐ |
| 039 | **Magnus Klapp** | Church | Cardinal Temperance (the scholar-heretic; Gerbert of Aurillac) | ◐ |
| 040 | **Osten Jarnstal** | Church | Cardinal Fortitude / Templars | ○ |
| 004 | **Sæmund Haelgrund** | Church | Field Inquisitor (secretly TS; Bellarmine-after-Galileo) | ● |
| 021 | **Gustav Linder** | Church (Crown agent) | Archbishop's Representative, dual-loyalty | ○ |
| 003 | **Lisbeth Ehrenwall** | Löwenritter | Grandmaster (the deed-ledger enforcer) | ● |
| 002 | **Sigrid Torsvald** | Löwenritter | Covert Riskbreaker, secretly TS (Christine Granville) | ● |
| 006 | **Halvar Brandt** | Löwenritter | Officer, Lions' Table (Aetius) | ● |
| — | **Vidar Haldorsen** *(proposed)* | Löwenritter | Riskbreaker (doctrine-following foil to Torsvald) | ○ |
| 007 | **Annika Feldhaus** | Guilds | Guilds Representative (Jacques Cœur) | ● |
| — | **Frieda Kessler** *(proposed)* | Guilds | Zunftmeisterin (Guildmaster Council) | ○ |
| — | **Nessa Grindvold** *(proposed)* | Guilds | Guild Advocate at Crown court | ○ |
| — | **Joren Bergvall** *(proposed)* | Guilds | Guild Surveyor (maps the maritime Forgetting boundary) | ○ |
| 001c | **Yrsa Vossen** | Restoration | RM leader (Rosa Luxemburg) | ● |
| 025 | **Aldric Hann** | Restoration | RM visible leadership (operational wing) | ◐ |
| — | **Uwe Askeland** *(proposed)* | Restoration | Buditel (hedge-school teacher) | ○ |
| — | **Carin Vedel** *(proposed)* | Restoration | Copyist of suppressed Einhir texts | ○ |
| 001 | **Edeyja** | Wardens (indep.) | Warden-Chief of the Southernmost (Hypatia; the fixed point) | ● |
| 041 | **Orm** | Wardens (indep.) | Second Senior Warden (Chernobyl liquidator) | ◐ |
| 010 | **Dalla Virke** | Indep. (Virke syndicate) | Syndicate Broker (Medici branch-manager) | ● |
| 011 | **Alexios Laskaris** | Altonia | Doux (frontier prince; Demetrios Palaiologos) | ● |
| — | **Zoe Palaiologina** *(proposed)* | Altonia | Katepano (frontier governor) | ○ |
| — | **Stephanos Doukas** *(proposed)* | Altonia | Kommerkiarios (trade prefect at the Schoenland interface) | ○ |
| 012 | **Rikard Solberg** | Schoenland (indep.) | Trade Factor (Xenophon's *Anabasis*) | ● |

**What the inventory shows about *where the gaps are*:** the peninsula's own institutions are well-cast (the
Ruler Diamond, the operational tier). The thin zones are exactly the setting's most dramatically loaded
edges — **Altonia** (three frontier-*interface* figures, but no face of the invasion and no emergent
usurper), **the Southern Einhir *community*** (RM leadership, but few of the caste's own people speaking for
themselves), **the settlements** (37 places, one named governor), **the Wardens** (a two-person dying order),
and **the underworld** (Virke alone, atop a dissolved four-arm network). Part B fills those.

---
---

# PART B — NEW NPCs IN CRITICAL AREAS

Each entry: proposed name (collision-checked, convention-compliant), role, the Conviction/flaw and dramatic
function, the real-precedent anchor (+ literary where it adds), and the gap it fills. All **PROPOSED** —
pending registry allocation + contamination audit.

## B.1 Altonia — the face of the threat, and the sanctioned usurper

Altonia is the existential pressure with no cast beyond its frontier interface. The compendium's rule holds
(**never a throne-room scene; the empire is a weather system with human faces at its edge**) — but the edge
needs more faces, and canon (ED-IN-0047) explicitly sanctions an **emergent "Altonia-usurper archetype."**

- **Strategos Nikephoros Bryennios** — commander of the Altonian *thema* massed beyond the northern passes;
  the human face of Institutional Pressure. *Anchor:* the real Byzantine border-*strategos* (the Bryennioi
  were a genuine frontier-magnate house that produced rebels and generals). Conviction: **Authority + Utility**;
  flaw: **CONTEMPT** — he regards the peninsula not as a nation but as a rebellious *thema* overdue for
  recovery, and his condescension (not malice) is what makes him dangerous (Coetzee's banal empire). Fills:
  the invasion has no face; IP milestones ("forces massing at the border") can now be *his* decisions.
- **Emmerich Kaltenbach, styled by Altonia *Doux of the Reclaimed Marches*** — the **emergent usurper**
  (ED-IN-0047). Peninsula-born, of a duchy-family that backed the losing side at secession and fled to the
  Altonian court; raised imperial, returning with the Empire's backing to "restore" the peninsula to the fold
  he believes its own factions are tearing apart. *Anchor:* the real *collaborationist-restorationist* pattern
  — émigré claimants returned under a foreign patron (the Jacobite pretenders under France; White émigrés; the
  Byzantine claimants who returned with Ottoman or Latin backing). Conviction: **Order + Precedent**; the
  tragedy: he may be *right* that the peninsula is destroying itself (the three-body ratchet made flesh), which
  is exactly why he is not a cartoon villain. Fills: the sanctioned emergent Altonia-usurper.
- **Metropolitan Anthimos Skleros** — a hierarch of the **Almaic Kyriakos** (Altonia's imperial religion, named
  but undefined in canon) attached to the frontier. *Anchor:* the Byzantine imperial-church model + the
  *basilikos logos* (Menander Rhetor's codified imperial-praise) — a confident state orthodoxy that
  *"quarantined rather than destroyed"* the Church of Solmund (as canon says the Raj managed Hinduism/Islam).
  His galling quality is condescension: to him the Church of Solmund is a tolerated provincial curiosity, and
  Solmund a local saint. Fills: the religious mirror that explains the Church of Solmund's own containment
  psychology.

## B.2 The Southern Einhir — the caste's own people, speaking for themselves

The Omelas-compass repair (companion §3.4) requires the marginalized to be *subjects*, not objects other
factions take stances toward. The RM has leaders; the *community* needs its own voices — and this is where the
orphaned `worldbuilding_v30 §8` proposal "Elder Solvei Kaldring" (geographically stranded on non-existent
place-names) should be cleanly resolved.

- **Elder Ragnfrid Aslaksdottir** — lawspeaker and memory-keeper of the Southern Einhir (Oastad/Grauwald), the
  community's own voice *distinct from the RM's political leadership*. She holds the old Einhir oral law and
  adjudicates the community's internal disputes; she is not a revolutionary but the reason there is a community
  left to revolt. *Anchor:* the Icelandic **lögsögumaðr** (law-speaker reciting law from memory at the
  Lögberg) + the real keepers of suppressed tradition (Korean/Baltic underground transmitters). Conviction:
  **Precedent + Community + Warden**; she embodies the **"endure and transmit"** stance the compass names.
  *Resolves the Kaldring seam:* propose Ragnfrid as the clean successor and formally strike the stranded
  Kaldring proposal.
- **Clerk Emil Nordholt (born Eyvind of Aschenbach)** — a Southern Einhir who took a northern name to serve in
  the Ministry, and lives the exposure-dread. *Anchor:* the **converso** (a sacramentally-orthodox subject
  targeted by descent) and the corpus's own **Sōshi-kaimei** naming-as-violence point — his assumed name *is*
  the wound. Conviction: **Order** (the mask) over **Identity** (the truth); flaw: **CONCEALMENT**, a survival
  mechanism like Torsvald's and Haelgrund's, but for caste. Fills: the compass's **"assimilate"** stance made a
  person; the caste's cost lived from inside an institution.
- **Aslaug the Weaver of Skogheim** — a village weaver whose craft-songs are dormant Einhir Thread-technique
  she does not know she is performing. *Anchor:* the real pattern of **suppressed technique surviving as
  folk-craft** (the Irish/Baltic cultural-revival craft traditions) — and canon's own claim that RM folk-
  practice *is* substrate-heritage its practitioners don't recognize (P-08: the barrier is metaphysical, so she
  *cannot* know). Fills: the RM's "substrate-heritage reclaimer, unknowingly" made concrete and human.

## B.3 The settlements — local notables (the deferred Stage 6b, given faces)

`territory_temperaments_v30 §5` explicitly defers settlement-level culture. These local figures give the most
dramatically-loaded settlements a face and double as Part C's cultural seeds.

- **Toll-Master Berthold Zöllner of Goldenfurt (T2)** — the Crown-appointed collector at the tolled river-ford
  whose "Guild toll dispute *is* the settlement's defining tension" (per the geography flavor). Caught between
  the Crown that appointed him and the Guilds that want the toll gone. *Anchor:* the real **staple-right /
  Stapelrecht** toll-town official (Rhine/Hanseatic river-toll politics). Fills: Goldenfurt's named tension.
- **Granary-Reeve Mathilde Speicher of Feldmark (T5)** — steward of the granary complex on which Hafenmark's
  food-dependency rests; a quiet fulcrum of the Crown–Hafenmark relationship (whoever she favors eats).
  *Anchor:* the real **annona / grain-officer** whose control of the store was political power (Roman
  *praefectus annonae*; medieval granary-reeves). Fills: the food-dependency anchor with a human lever.
- **Father Lorenz Aldenhoven of Stillhelm (T6)** — a Church parish priest at the southern gate to the wound,
  tending a frightened, "uneasy" population and half-perceiving what he tends beside. *Anchor:* the real
  **frontier/mission parish priest** and the corpus's own Church-pastoral-network model. Conviction: **Faith +
  Warden**; his quiet terror is that his flock's dread is *correct* and he can't say why (the Forgetting).
  Fills: the Church parish level and the lived texture of the Calamity-adjacent south.
- **Steiger Konrad Bergmann of Halvarshelm (T17)** — a mine-foreman (*Steiger*) over the iron and copper
  workings, the pivot between Guild labor and Hafenmark ownership. *Anchor:* the real **medieval/early-modern
  mining-guild culture** (the *Steiger*, the Bergmeister, the Saxon *Bergrecht*). Fills: the mining north's
  distinct labor culture and a Guild-labor face.
- **Roll-Keeper Griseldis Amtmann of Gransol (T8)** — keeper of the physical **Roll of Burghers** in the
  Gransol Parliamentary Archive (the corpus's own image), who literally inscribes a citizen's rank into
  existence. *Anchor:* the real **civic enrollment/matricola** officials (Venetian *Avogadori*, the guild
  matriculation registers). Fills: Hafenmark's civic-constitutional ritual with its gatekeeper.

## B.4 The Wardens & the underworld — depth for a dying order and an orphaned network

- **Torgny Havardsson, the Warden who left** — a Warden who could not stay at the wound and fled north,
  carrying the knowledge and the guilt; a living foil to Edeyja and Orm. *Anchor:* the real **liquidator/relief-
  worker who broke** (the Chernobyl personnel who could not continue) — the human cost of the maintenance no
  one else can perceive. Conviction: **Warden** in exile; his tragedy is that leaving did not free him. Fills:
  the two-person dying order's depth, and the compass's **"exit"** stance among the Wardens.
- **"Ash" (born Skarde), one of the Burned** — a settlement-layer intelligence broker of the dissolved
  Niflhel's "Burned" arm (those who lost everything and have nothing left to lose), rivaling and sometimes
  serving Dalla Virke. *Anchor:* the real **underworld information economy** (the Venetian *bocche di leone*
  informer culture; the early-modern *bravo*/fixer). Fills: the orphaned four-arm underworld beyond Virke — the
  "Burned" made a person.

**Roster-capacity note:** that is **eleven** proposals across five critical areas. Even added to the 46
existing, most enter at Passive/Background tier; the ones most likely to earn Active promotion are **Bryennios**
and **Kaltenbach** (they give the invasion agency), **Ragnfrid** (she anchors the caste's own voice), and
**Father Lorenz** (he is the south's face). The rest are settlement/scene texture.

---
---

# PART C — CULTURAL INTENSIFICATION

The cast tells you *who*; this tells you *where they stand and what they touch*. Three layers — factions
(institutional culture), provinces (regional character), settlements (the deferred Stage 6b, given local
texture) — each grounded both/and and canon-safe, each written so a Godot content-author could turn a
paragraph into a Domain-Echo string, a scene dressing, or a temperament rationale. **Nothing here rewrites
the temperament table or the geography YAML; it thickens the prose they gesture at.**

## C.1 Faction culture — the under-consolidated institutions

The compendium found the Crown, the Church, and the Ruler Diamond richly cultured and four institutions
under-drawn: **Hafenmark, Varfell, the Restoration Movement, the Löwenritter** — plus **Altonia**, whose
culture the invasion cast (B.1) now needs. Each below gets a **self-image, a rite, a material culture, a
law-custom, and the caste as *locally lived*** — the last because P-01/P-13 mean the caste is not a uniform
overlay but a thing each culture metabolizes differently.

### Hafenmark — the republic of the ledger
- **Self-image:** *liberty is commerce is law.* Baralta's duchy does not think of itself as ruled but as
  *chartered* — a constitutional merchant-republic whose freedom is written, sealed, and enforceable.
  *Anchor:* the **Hanseatic Kontor** and the **Venetian constitution** — the *Maggior Consiglio*, the
  *Avogadori de Comùn*, the 1297 *Serrata* that froze the patriciate into a closed register (Gransol's Roll
  of Burghers is that *Serrata* in miniature). Literary co-contributor: the mercantile fatalism of Mann's
  *Buddenbrooks* — a house that is a firm that is a bloodline. **Rite:** the annual **swearing of the Roll**
  — every burgher's rank re-read aloud and re-sealed (Griseldis Amtmann, B.3, presides). **Material culture:**
  the sealed ledger, the salt-measure, the guild-hall, the harbor-chain; wealth shown as *account* not
  ornament (a Hafenmark noble displays a clean book, not a jewel). **Law-custom:** contract is sacred and
  retroactive law is abomination — which is exactly the lever Vaynard uses against Baralta (he weaponizes
  *her own* proceduralism). **Caste, locally lived:** Hafenmark's is the coldest caste-culture — not hatred
  but *non-enrollment*. A Southern Einhir is not persecuted here; they simply cannot be entered on the Roll,
  and so cannot own, testify, or inherit. The cruelty is administrative, and therefore deniable — the
  Investiture-Controversy symmetry the companion §3.3 guards.

### Varfell — the long cold and the longer memory
- **Self-image:** *the old blood keeps the old truth.* Vaynard's fjord duchy is the peninsula's memory-culture
  — patient, genealogical, convinced the newcomers (Crown, Church, and above all Hafenmark's money) are a
  passing weather over a permanent people. *Anchor:* the **Norse–Icelandic þing** and **jarl-council**, the
  **skald as law-speaker** reciting descent and precedent from memory (Ingrid Stenskald, 031, *is* this
  office), the saga-culture where a grudge is a legal instrument that outlives its holder. Literary
  co-contributor: Le Guin's Gethen and Gethenian *shifgrethor* — prestige as a cold, indirect, wholly
  serious currency. **Rite:** the **reckoning of descent** at succession and at feud-settlement — a public
  recitation that *is* the title. **Material culture:** the fjord-hall, worked timber and dark iron, and
  Vaynard's **Private Collection** (S-031) — objects that are *arguments*, provenance as power. **Law-custom:**
  memory is admissible; the skald's recitation outranks a written charter, which is why Varfell distrusts
  Hafenmark's paper and Hafenmark distrusts Varfell's word. **Caste, locally lived:** Varfell holds the
  **Einhir heritage** (Grauwald T4) and is thus the most *ambivalent* caste-culture — the same genealogical
  pride that ranks men also remembers when the Einhir were *not* beneath them. The RM's deepest roots (Oastad
  T13) are here for that reason: Varfell is where the memory of the pre-caste order was never fully burned.

### The Restoration Movement — the counter-culture of the remembered order
- **Self-image:** *we are not rebels; we are the memory they tried to kill.* The RM is not a state but a
  diffuse transmission network — its "culture" is a **counter-culture** carried in copied texts, hedge-schools,
  and folk-craft. *Anchor:* the real **national-revival undergrounds** — the Polish *latający uniwersytet*
  (flying university), the Baltic **book-smugglers** (*knygnešiai*) who ran a banned alphabet past an empire,
  the Irish **hedge-school** and Gaelic-revival copyists. Literary co-contributor: the memorized-book people
  at the close of *Fahrenheit 451* — a culture that survives by *becoming* the text. **Rite:** the **passing
  of a copied page** — transmission as sacrament (Carin Vedel, the copyist; Uwe Askeland, the *buditel*
  hedge-teacher — both B.2/registry). **Material culture:** the palimpsest, the hidden lodge (Grauwald's Lodge,
  S-026), the craft-song that is dormant technique (Aslaug, B.2). **Law-custom:** no law but memory and the
  oath of transmission — its fragility is that a network cannot enforce, only entrust. **Caste, locally lived:**
  the RM *is* the caste's political voice, but the companion §3.4 repair holds — its members metabolize the
  caste four ways (endure/transmit via Ragnfrid, assimilate via Emil, reclaim-unknowing via Aslaug, revolt via
  Vossen), and the movement's real internal drama is the argument *between* those four stances.

### The Löwenritter — honor, accounted
- **Self-image:** *the deed is the man; the ledger does not lie.* A knightly order whose radical premise is
  **merit recorded over blood inherited** — and which is therefore both the peninsula's one anti-caste
  institution *and* its own severe hierarchy of accounted worth. *Anchor:* the **military orders** — Templar,
  Teutonic, Hospitaller — with their rule, their chapter, their treasury; crossed with the **deed-ledger**
  discipline of a muster-roll and the *ordo* of accounted service. Literary co-contributor: the grim
  accountancy of honor in Malory — worth as a thing that can be won, spent, and forfeited. **Rite:** the
  **Lions' Table** (canon) — the entry of a deed into the ledger, witnessed; Ehrenwall (003) is its keeper and
  its conscience. **Material culture:** the black-and-gold, the muster-roll, the plain refectory; conspicuously
  *un*-ornamented, because ornament is inherited and the order recognizes only the earned. **Law-custom:** the
  ledger is appealable only by deed, never by birth — a knight demoted for cowardice cannot buy the entry back.
  **Caste, locally lived:** the Löwenritter is the peninsula's proof that the caste is *contingent* — it
  admits and ranks the Southern Einhir on deeds — which is exactly why the Church and the Crown find it quietly
  dangerous, and why Sigrid Torsvald (002) can hide a Threadwork-Sensitive identity inside it: the order asks
  what you *did*, not what you *are*.

### Altonia — the confident metropole
- **Self-image:** *the peninsula is a lost province, not a nation.* Altonia does not hate Valoria; it
  *administers the memory of owning it.* Its culture is imperial condescension — orderly, literate, sincerely
  convinced of its own civilizing role. *Anchor:* **Byzantine imperial culture** — the *thema* frontier system
  (Bryennios's command, B.1), the *basilikos logos* (Menander Rhetor's codified imperial-praise oratory), the
  tax-roll and the silk diplomacy, and the **Almaic Kyriakos** state church (Metropolitan Anthimos, B.1) that
  *"quarantined rather than destroyed"* the provincial faith — the containment-not-conquest model the
  compendium draws from the Raj. Literary co-contributor: the patient, paperwork-borne dread of Coetzee's
  *Waiting for the Barbarians* — empire as a climate, not a villain. **Rite:** the **reception of a
  province's embassy** as a ritual of subordination — gifts up, recognition down. **Material culture:** the
  icon, the imperial silk, the sealed *chrysobull*; power shown as *legitimacy*, the aesthetic of the rightful.
  **Law-custom:** Valoria's secession is, in Altonian law, an ongoing *rebellion* — which is what makes
  Kaltenbach (B.1) a *restorer* in his own eyes, not an invader. **Caste, locally lived:** here is the
  root-truth the companion insists on — the caste is **Altonian colonial residue**. To Altonia the Einhir
  distinction is simply the correct order of a province it once ran; the peninsula inherited the empire's
  filing system and forgot it was the empire's.

## C.2 Province culture — the six regions

The 17 provinces cluster into six cultural regions. Each note grounds the temperament-table rationale
(§2 of `territory_temperaments_v30`) in lived regional character — the "why" behind the α/β weights, ready to
dress a Domain action or a settlement scene.

- **① The Eastern Lowlands (Crown core) — T1 Valorsplatz, T2 Kronmark, T5 Feldmark.** The peninsula's
  Italian-coded heartland: river-sea trade at the capital (T1 *pragmatic*), devout farmland behind it (T2/T5
  *traditional*). *Anchor:* the **Lombard/Tuscan** commune-and-*contado* pattern — a mercantile city ringed by
  a conservative grain-country that feeds and resents it. Culture: the Valoris-river artery as the Crown's
  lifeblood; the harvest calendar as the real clock of Kronmark and Feldmark; the granary (Feldmark, C.3) as
  the single most political building in the realm. The lowlands' self-image is *the center that holds* — which
  is precisely the burden Almud carries and the fiction the three-body ratchet erodes.
- **② The Northern Passes & the Ridge (the Altonian frontier) — T3 Lowenskyst, T10 Spartfell, T17 Halvarshelm,
  T9 Himmelenger.** The cold militarized north where the empire presses: two fortress-passes (T3 Crown, T10
  Hafenmark — *balanced*, garrison-plus-civilian), the mining highland (T17 — *balanced*, Guild labor), and the
  Cathedral ridge deliberately placed *between the passes* (T9 — *principled*, spiritual_weight 4). *Anchor:*
  the **military-march / Militärgrenze** frontier society — a border people whose culture is vigilance, and a
  **Church containment-placement** that reads like the Raj's cordon. Culture: the pass-watch as a way of life;
  the mining guilds' distinct labor-rite (Halvarshelm, C.3); the Cathedral's self-understanding as the *cork in
  the bottle* between Altonia and the wound. This is where Bryennios's massing (B.1) will be *felt* first.
- **③ The Hafenmark Highlands (the mercantile west) — T7 Rendstad, T8 Gransol.** Swiss-coded rocky highland:
  remote timber-valley (T7 *traditional*) and the constitutional capital on the west sea (T8 *pragmatic*,
  Baralta's court). *Anchor:* the **Swiss cantons** and the **Hanseatic west-sea** — a hard-country liberty
  that turned poverty of soil into wealth of trade and a fierce constitutionalism. Culture: the Roll of Burghers
  and the Parliament (Gransol, C.3) as civic religion; the timber-and-salt-and-iron economy; the highland
  self-image of *earned, chartered freedom* against both Crown and empire. The α/β *pragmatic* weight is
  Baralta's whole strategy made demographic.
- **④ The Varfell Fjords (the deep north-west) — T4 Grauwald, T11 Halvardshelm, T12 Sigurdshelm.** Norwegian-coded
  fjord country: Einhir-heritage highland timber (T4 *traditional*, RM roots), central fjords (T11
  *traditional*), and Vaynard's seat (T12 *balanced* — ducal court over traditional fjord folk). *Anchor:* the
  **Norwegian fjord-þing** society — dispersed, genealogical, saga-memoried, hard to rule from outside and
  slow to forget. Culture: the reckoning-of-descent (C.1); the fjord-hall and the skald; the **Einhir-heritage
  ambivalence** that makes this the RM's cradle. Its self-image is *permanence* — the cold that outlasts kings.
- **⑤ The Calamity South (the wound's edge) — T6 Stillhelm, T13 Oastad, T15 Askeheim.** The *outcomes-only*
  band (α 0.9): two Calamity-adjacent gate-provinces (T6 Crown, T13 Varfell/RM-stronghold) and the epicenter
  itself (T15, uncontrolled, spiritual_weight 5, the Forgetting zone). *Anchor:* real **disaster-frontier /
  exclusion-zone** societies — Chernobyl's *samosely*, sacrifice-zone communities who stay because leaving is
  its own death. Culture: the **Calamity-vigil** (Stillhelm, C.3) — a frightened folk-piety half-perceiving the
  Forgetting (Father Lorenz, B.3); the southern shrines (Oastad's, S-034); the outcomes-only ethic of people
  who have no headroom for conduct-scruple because survival is the only question. **Canon guard:** the
  Forgetting is metaphysical (P-13) — the south's dread is *correct and unspeakable*, never mere superstition.
- **⑥ The Sea-Edges (the foreigners) — T16 Schoenland.** The independent island republic (*pragmatic*), naval
  choke and Altonian-trade broker. *Anchor:* the **neutral entrepôt** — Ragusa/Dubrovnik, the island republic
  that survives between empires by being useful to all and loyal to none. Culture: the factor's cool
  calculus (Solberg, 012); the harbor as the whole polity; a self-image of *interested neutrality* that makes
  Schoenland the naval hinge the Altonian invasion route (IP 75+) must buy.

## C.3 Settlement culture — the deferred Stage 6b, curated

`territory_temperaments_v30 §5` defers settlement-level authoring to Stage 6b. This is not that authoring
(no α/β values, no ledger) — it is the **prose seedbed** for it: a curated set of the most dramatically-loaded
settlements, each with a local custom / material culture / rite that a content-author can lift. Each ties to a
Part B notable so cast and place arrive together.

- **Goldenfurt (S-006, Kronmark) — the toll-culture.** The tolled river-ford whose *"Guild toll dispute is the
  settlement's defining tension."* Custom: the **ford-reckoning** — goods weighed and taxed at the crossing,
  the toll-boards posted publicly. *Anchor:* the Rhine **Stapelrecht / staple-right** toll-towns. Notable:
  Toll-Master Berthold Zöllner (B.3), caught between the Crown that appoints him and the Guilds that want the
  toll gone. Material: the toll-chain, the weigh-house, the ledger of passage.
- **Feldmark (S-009, T5) — the harvest-rite and the granary.** The breadbasket granary that *is* Hafenmark's
  food-dependency. Custom: the **first-sheaf and the granary-count** — a harvest-home folk-rite layered over a
  coldly political store-audit (whoever the Granary-Reeve favors, eats). *Anchor:* the Roman *annona* and the
  medieval tithe-barn. Notable: Granary-Reeve Mathilde Speicher (B.3). Material: the tithe-barn, the sealed
  granary door, the measure.
- **Stillhelm (S-012, T6) — the Calamity-vigil.** *"Population uneasy,"* Calamity-adjacent. Custom: the
  **night-vigil at the southern gate** — a parish folk-piety of watching-against-the-dark that is half
  liturgy, half dread, and (P-13) *correct without knowing why*. *Anchor:* frontier rogation and plague-vigil
  processions. Notable: Father Lorenz Aldenhoven (B.3), tending a flock whose fear he cannot name. Material:
  the gate-lantern, the ward-marks, the un-rung bell.
- **Halvarshelm Town (S-023, T17) — the mining-guild culture.** *"Miner settlement. Guild labor presence."*
  Custom: the **shift-descent rite and the Steiger's roll** — the guild's initiation and the daily muster into
  the dark, a labor-culture distinct from farm and harbor. *Anchor:* the Saxon *Bergrecht* and the *Steiger* /
  Bergmeister mining-guild tradition (the real root of "Glück auf"). Notable: Steiger Konrad Bergmann (B.3),
  the pivot between Guild labor and Hafenmark ownership. Material: the lamp, the Bergrecht-book, the ore-token.
- **Gransol (S-018, T8) — the civic-constitutional ritual.** Hafenmark's capital, Baralta's court, the
  Parliament and the physical **Roll of Burghers**. Custom: the **swearing of the Roll** (C.1) — the annual
  re-reading that inscribes rank into being, and the Parliament floor where the three-body ratchet plays out
  (assessment: Baralta grandstands, Vaynard maneuvers the record, Almqvist subverts both with one command).
  *Anchor:* the Venetian *Serrata* and the guild *matricola*. Notable: Roll-Keeper Griseldis Amtmann (B.3),
  who *is* the gate. Material: the sealed Roll, the parliamentary mace, the archive.
- **The Einhir hamlets — Skogheim (S-027, Grauwald) & Yrnastead (S-030, Halvardshelm).** *"Norse-Einhir forest
  hamlet"* / *"Norse-Einhir hillside stead."* Custom: the **craft-song and the weaving-circle** — folk practice
  that (P-08) *is* dormant Thread-technique its practitioners cannot know they perform. *Anchor:* Baltic/Irish
  cultural-revival craft survival. Notable: Aslaug the Weaver of Skogheim (B.2); Elder Ragnfrid (B.2) holds the
  law for both. Material: the loom, the pattern that is a memory, the un-read knot.
- **Auerheim (S-002, Valorsplatz) — the Latinate market town.** *"Latinate riverside market town"* — the one
  explicitly Latin-coded settlement, a pocket of older imperial residue in the Crown capital's shadow. Custom:
  the **river-market fair** and a lingering Latinate rite-calendar older than the Crown. *Anchor:* the
  Lombard market-town under a newer sovereignty; a living trace of the Altonian imperial past inside the Crown's
  own province. Material: the Latin inscription weathered on the market-cross, the fair-charter.
- **Oastad (S-034, T13) & the southern shrines.** Southern fishing town, Calamity-adjacent, RM stronghold, with
  a **Shrine** sub-feature (PP-726). Custom: the **shore-shrine offering** — a syncretic Warden-adjacent
  folk-cult of tending-the-edge, where RM memory and Calamity-dread and old Einhir practice fuse. *Anchor:*
  fishing-village votive shrine culture on a dangerous coast. This is where the RM's roots and the Warden ethic
  and the caste's memory physically overlap — the densest single settlement for the setting's themes.

## C.4 Texture → mechanism (how this feeds the engine)

Consistent with the compendium's Part 6, every cultural note above is written to become **quantitative**
without being invented from nothing:
- **Faction culture → Domain-action flavor + foil structure.** A Hafenmark domain action reads in ledger-and-
  charter register; a Varfell one in descent-and-memory register; the *contrast* is the faction-foil structure
  the assessment names. The caste-lived-texture (C.1) is the content layer for belief/stance Keys, not a new rule.
- **Province culture → the α/β rationale, made legible.** C.2 is the human-readable "why" behind each
  temperament weight and the `peninsular_strain_shock` drift toward *outcomes-only* (§4) — a designer tuning a
  province can read the culture and know whether a number is faithful.
- **Settlement culture → Stage 6b seed + scene dressing.** C.3 gives Stage 6b its prose starting point (each
  entry is one settlement's custom/material/rite) and gives the scene layer its local color, tied to a named
  notable so a settlement scene has a face on arrival.

**None of this is canon.** Every proper noun coined here (rites, the notables of Part B) is a **proposal**
pending `id_reservations.yaml` allocation and the `placeholder_names` contamination audit; every cultural
claim is checked against P-01–P-15 and leads with a real precedent. The document ratifies nothing — it is a
platform to build unique features, actions, and mechanisms from, exactly as the compendium set out to be.

---

*End Cast & Culture Expansion. SPECULATIVE — proposals and suggestions, ratifying nothing.*
