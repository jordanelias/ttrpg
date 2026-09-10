# THREADWORK — PRACTICAL APPLICATIONS BY SUBSYSTEM
## Status: PROPOSED
## Date: 2026-09-10
## Lane: WR · ED-WR-0010
## Part 1 of 2 — `threadwork_applications_part2.md` continues at §6.

**What this is.** What threadwork *does* in each subsystem, as usable design material: what a
practitioner can attempt, what it costs, what it leaves behind for someone else to find, and what
each subsystem has to carry as a result. Carried across from the *Valoria Unreality Suite* of
2026-09-06 — its sector work, its four adversarial domains and their worked examples, its
political catalogue and its videogame systems — re-priced against the live philosophy in
`canon/philosophy/` and re-pointed at the subsystems this repository actually has.

**What it is not.** Metaphysics. The philosophy is settled and lives in `canon/philosophy/`; this
document cites it only where a ruling constrains a mechanic, and never re-argues it. §1 is the
whole of what you need before reading any application.

**Where the numbers stand.** Scale bands, reach thresholds and detection tiers are the v30
design's, unchanged. Absolute Coherence figures are **deliberately absent**: the suite priced
everything against a 10→0 depleting track, and the rulings replaced that quantity, so its
arithmetic does not transfer. Costs below are given as **bands** — free / one step / two steps,
plus per-season where a shape is held — which is what actually survives and what the tables were
really encoding.

---

## 1. The four rules every application below prices against

### 1.1 Direction decides whether there is a cost at all

Not scale, and not the verb. The same Weaving is one thing on a configuration already oriented
toward the woven shape and another on one that is not.

| direction | the working | what it costs the practitioner | what it leaves |
|---|---|---|---|
| **restorative** | the result is where the configuration was already going; once made, it needs no holding | **negative — it moves them toward their own equilibrium** | minimum temporal accrual, no residue to find, no propagation |
| **manipulative** | the result is off the attractor; it stands only while held, and the holding is theirs | one to two steps by scale, **plus a step per season held** | a held configuration readable at reach 30; propagation through knots in all three dimensions |
| **destructive** | a configuration standing in harmony with others is removed or unmade | one to two steps, **and the damage is not confined to the target** | orphaned configurations downstream that decay faster than grounded ones |

**Two consequences that reshape every catalogue in the suite.** Restorative work is not merely
free — a career of it is how a practitioner *recovers*, which changes what a Warden's life looks
like from the inside. And **destroying is not free**: the suite could not settle whether
accelerating a decay was "aligned", and the answer is that it is the third category, which a
binary aligned/opposed model had no room for. Harm costs. *(Carve-out: a configuration standing
in harmony with **nothing** — a corpse, a structure past holding, a crop already lost — has no
harmony to sever, so unmaking it is borne by no one.)*

### 1.2 Reading is free; working is dear

Diagnosis is perception at reach, not contact. It is not an operation, it moves nothing, and it
costs nothing.

**This is the single most consequential fact for institutional design in the setting**, and it
inverts the ordinary prestige gradient everywhere it lands: prognosis outranks operation. A
medical order's seniors are prognosticians and its juniors operate. A guild's mastery is reading
which batch was going where you want it; operative skill is journeyman work. A general who reads
and does not work wins cheaply and leaves nothing to find.

**And alignment is a fact about the substrate, not about the practitioner's belief.** Someone who
commissions what they assume is restorative and is wrong pays the manipulative rate, and nothing
informs them beforehand except the read. Tendency-reading is not a convenience; it is the
difference between free power and a spent house.

### 1.3 The detection ladder, and the one thing no reach returns

Thresholds are `operations.DEPTH_TS_MINIMUM`'s — the same four that gate what a practitioner can
operate on gate what they can see.

| reach | detects | blind to |
|---|---|---|
| **30–49** | Object and Personal-scale workings; wrapping; *that* a pull occurred | relational lattices; anything Structural; the content of anything |
| **50–69** | relational knots, live and dissolved; pull type and approximate date; induced vs spontaneous development | Structural workings; the reach of whoever performed one |
| **70–89** | Structural workings; Gaps; a Coherence-0 being distinguished from a threadcut one | — |
| **90+** | all of the above at any scale | — |

**No reach at any level returns the content of a pulled configuration**, because the content is
not present to be read. So: **operations are provable; their contents are not.** Every
investigative, legal and diplomatic application below is shaped by that one sentence.

**A dissolved knot stays readable indefinitely.** Relational offences therefore have no practical
limitation period, which is a real and unusual feature of this setting's law.

### 1.4 The practitioner is the asset that degrades, and cannot see it

Coherence is a distance from the human equilibrium, not a store. Two quantities matter and they
have different remedies: **present displacement**, which returns with time and rest — but only in
surroundings that are themselves in harmony — and a **resting point**, which no amount of rest
moves and which only deliberate restorative threadwork aimed at that configuration brings back.

Three consequences the applications lean on constantly:

- **A single observation dates a practitioner's load, not their history.** The band someone comes
  to rest in is their floor. **The community's instrument is not the worst state a practitioner has
  been seen in, but the best state they have been seen in lately.**
- **A veteran presents as further gone under identical load and is no more fragile.**
- **They cannot judge it themselves.** The faculty that would register the degradation is the
  faculty degrading, so others see it first — which is why every social application below attacks
  a practitioner through what observers perceive, never through cross-examining their self-report.

⚠ **One code note, and it is the only one in this document.** `systems/threadwork/sim/coherence.py`
implements the superseded quantity — a single clamped integer, 10→0, freely recovered, reset at
zero. Every cost band below assumes the model above, so the module needs the two quantities, the
environment condition on recovery, the direction gate and a resilience term before any of this
prices correctly. That is a code change, not a design question.

---

## 2. `systems/combat` — personal combat

The domain where the constraints bite hardest, because the Leap needs a window the fight will not
give.

### 2.1 Threadwork is a prepared action, never a combat action

The Leap suspends self-rendering for its duration; during it the practitioner's agency arrives
mediated and their balance runs on a clock detached from their stance. **That is a very long time
in a fight.**

> **Worked case — the duellist who tried.** Two swordsmen, one an adept intending to close a cut
> on his own forearm: restorative, free, a wound the body was closing anyway. He Leaps. His
> opponent does not wait. The wound closes and he has taken two more, and the reconstitution is
> forced by the second of them. **What it bought:** a closed forearm, a permanent set he will
> never see directly, and a duel he lost.

**Doctrine:** an adept works before the fight, or in a lull with allies screening, or not at all.

### 2.2 The Leap window is the assassination window, and the counter is free

> **Worked case — the standing order.** A house instructs its guard: *if a man's hands stop
> looking like hands, or he begins moving as though his balance belongs to someone else, put him
> down and do not wait to be told.*
> **What it costs:** nothing. No adept required, no detection problem.

This is the cheapest counter-threadwork capability that exists, and it is why every application in
§4 and §6 treats threadwork as a strategic instrument prepared off-site rather than a tactical one.

### 2.3 Fighting a drifting practitioner — a difficulty ladder that is canon-derived

| band | what the opponent experiences |
|---|---|
| **Dissonant** | His parry arrives before your cut. Not foresight — his responses track the position behind the movement. **Feinting fails.** |
| **Fragmented** | You cannot judge distance to him. His shadow does not match his posture; his presence occupies more space than his body; he flickers between fully in the scene and partly elsewhere. Two witnesses afterward describe the fight differently — in what they *saw* |
| **Fractured** | Measurement is impossible. Weight distribution wrong, light interacting at a register that produces unease, the exchange itself skipping and looping. Bystanders cannot say how long it lasted |
| **past the band** | Not a duel. §2.5 |

> **The teachable counter.** A guard captain feints high and cuts low; the parry is already low
> before the feint completes. He abandons feinting, attacks simply, and wounds the man.
> **Why:** the advantage is against *intent*, and a committed simple attack has little intent to
> read ahead of. **Deception is what the drift defeats; directness is what beats the drift.**

### 2.4 What is restorative, manipulative and destructive in a fight

| application | direction | cost |
|---|---|---|
| Closing your own wound the body was closing | restorative | free, and it moves you toward your own equilibrium |
| Accelerating an opponent's fatigue | destructive | one step |
| Accelerating an existing wound toward its outcome | destructive | one step — **unless already mortal in course**, then it severs no harmony and is free |
| Failing an opponent's blade | destructive | one step, unless the steel is already past holding |
| Holding your own wound closed that was not closing | manipulative | one step, plus per season |

> **Worked case — the confirmation, and the domain's darkest fact.** A soldier takes a wound
> through the lung and is tending toward death over some hours. An adept accelerates it; he dies
> in under a minute. The body presents as hours dead within the minute — cooled, settled, the
> lividity of a man down since dawn. The men who saw him fall cannot agree when he fell.
> **A field diagnostician can establish the death was accelerated and can never establish whether
> it was mercy or execution — intent is content, and no reach returns content.**

### 2.5 Fighting what cannot be fought

**A threadcut being.** Coherence does not apply. Wounds cost it sustained thread work rather than
an ordinary penalty, it does not tire in the human way, and it cannot be worn down.

> **Worked case — the champion and the mob.** A champion lands seventeen clean hits over four
> minutes. Each costs the being work to maintain against; none *accumulates*, because there is no
> body accumulating. The champion tires. The being does not. He dies.
> Forty militia with poles then confront it. No individual blow matters. What matters is that the
> being must spend continuous work against **forty simultaneous demands**, and being configured is
> itself the work — performed moment to moment, at undiminished cost, forever, because only
> spooling yields the depth that makes a configuration progressively cheaper to be. It cannot
> sustain the rate. Its rendering fails.
> **A mob beats a threadcut being where a champion cannot.** Distributed, continuous, simultaneous
> damage exceeds a finite maintenance rate; concentrated skilled damage does not. This inverts
> every ordinary assumption about heroic combat.

⚠ **Never Past-Pull one.** It has no spooled past to be pulled toward, so the operation finds no
purchase and leaves a **Gap** at the site — a structural opening through which incursions begin
arriving within the day. Attacking it with threadwork makes the ground worse and does not remove
the being.

**A being past the band, at high reach.** Not a combat proposition. Every moment of its existence
is an operation and its vicinity is under strain, so the engagement generates incursions in the
fight's own location. Cordon and survey; do not clear.

### 2.6 Equipment, and why held gear is absurd

**Work the material before it becomes the thing; never the thing after it is assembled.** Seasoned
stave, cured leather, tempered steel — all restorative, all free, all leaving nothing to find.

> **Worked case — the held blade at judicial combat.** A champion's sword has been held at edge
> for nine years: never sharpened, never dulled. **Cost:** a step at initiation and a step per
> season, for nine years — more than several practitioners' entire working lives. In practice a
> *house*, not a person, has been paying for a sword.
> **Detection:** immediate, at reach 30. The handle's wear and the blade's absence of history
> disagree, and the assay officer reads it in seconds. **Ruling:** barred.

### 2.7 Two knotted fighters, and a fight in a high-tension district

> **The knotted pair.** Two guards knotted, fighting as a pair against three. Their opponents
> cannot reliably attend to one without the other entering the attention; attacks aimed at one
> arrive as though aimed at a position between them. **They are not faster and not stronger —
> they are harder to individuate, and individuation is what a swordsman does first.**
> **The cost:** they co-date, so their accounts of any fight are identical in a way a board of
> inquiry reads as collusion. Over years each becomes describable only in terms of the other. And
> if one dies the knot severs by event — the survivor loses part of what held him in
> configuration, permanently. Sworn pairs and bodyguard orders are where this appears.

> **The skirmish at the margin.** Two patrols engage within a kilometre of a Locked Zone margin
> loosened eleven days earlier and re-tightening. At minute four it re-tightens across ground both
> patrols occupy. Every survivor carries the confrontation signature — residue without referential
> content, fragmentary perception that will not compose into recall, somatic trace. **Neither side
> can give an account of who won**, and both companies' after-action reports are fragmentary in
> the same way and both honest. **There is no treatment**; what exists is framing.

---

## 3. `systems/social_contest` — proceedings, negotiation, trial

### 3.1 What threadwork cannot do here, and the characteristic error

**It cannot persuade.** There is no operation that produces assent. Memory can be pulled, but
pulling is displacement rather than replacement: it leaves an orphan and a detectable cut face.
Nothing supports weaving a belief into a person.

> **Worked case — the pulled objection.** An envoy has one standing objection to a treaty: his
> brother died in the last war under the other party's banner. An adept pulls the memory of the
> death. **Cost:** one step, manipulative.
> **Result:** he no longer raises the objection. He also stops writing to his sister-in-law,
> without deciding to, and the correspondence lapses within a season. He can recite that he opposed
> the treaty last month and cannot construct why; asked to reconstruct his reasoning he produces
> sequences that do not join. He reports a presence in his study — no figure, no voice, complete
> certainty with nothing attached to it.
> **Detection:** reach 30 finds the absence in one session; reach 50 dates it to within a month.
> **What it bought:** one vote, and a diplomatic incident the moment the other side surveys him —
> which they will, because §3.2 makes pre-negotiation survey routine.

### 3.2 The survey is the capability

| a survey establishes | a survey never establishes |
|---|---|
| whether they are knotted, and roughly to what — a person, a place, an institution | who the knot is to |
| whether a knot they once held was dissolved (readable **indefinitely**) | what it was for |
| whether anything was pulled from them, of what type, roughly when | what the pulled thing was |
| whether their instruments carry a held configuration | whether the instrument's contents are true |
| — | what they want, what they will accept, what they were told |

> **Worked case — the pre-negotiation survey.** Two houses meet over a river toll. One
> diagnostician surveys the opposing envoy in the anteroom and reads a live relational knot and a
> dissolved one of the same scale, roughly nine years old. Nothing pulled; the credentials clean.
> **Inference:** the envoy currently answers to someone other than the party he represents, and
> has done this before. Not proof, and not content — **a shape**, and enough to restructure the
> offer so that any term he accepts eagerly is treated as a term his other principal wants.
> **Cost:** nothing, and the survey itself leaves nothing to detect.

### 3.3 The one free working, and its opposed twin

Relations can be tending somewhere, and accelerating a convergence already underway is
restorative.

> **The alliance that was coming.** Two minor houses have been converging for two years — shared
> markets, a marriage under discussion, aligned grievances. An adept reads the tendency and weaves
> the alliance. **Cost: free**, and it moves the adept toward their own equilibrium.
> The treaty exists with the depth of an arrangement two years in negotiation, witnessed and
> sealed. Neither house can now say who first proposed it, and they disagree by about four months
> on when talks opened. A rival's diagnostician can establish the alliance was **accelerated** and
> cannot establish that it was fabricated — **because it was not.**
> **What it bought:** eighteen months. That is the whole benefit and it is substantial.

> **The alliance that was not coming.** Same working between two houses with no convergence.
> **Cost:** two steps, manipulative, plus the hold. Both archives agree on the treaty in detail
> and **neither family agrees with its own archive** — retainers on both sides recall years of
> hostility the documents no longer record. The disagreement is not between the houses; it is
> between each house and its own paper. The two cannot agree which of them ceded what, and the
> dispute matures into a casus belli within three seasons.
> **What it bought:** a season of cooperation and a war.

### 3.4 The trial: operations are provable, contents are not

> **The contested will.** A claimant produces a will dated eleven years back. Reach 30 reads a
> **held configuration** on the parchment — the document is being maintained at a state it was not
> going to reach on its own.
> **What that proves:** an operation was performed on this instrument. **Not** forgery — a genuine
> will kept from decay by a loyal steward reads identically to a fabricated one aged into
> plausibility. **What the court can do:** shift the burden. The offence is *unlawful working on a
> legal instrument*, defined by the act; the claimant must account for the working, not for the
> contents. **What no reach adds:** whether the words are the testator's.

> **The honest contradiction.** Two witnesses to a killing give irreconcilable accounts and both
> pass every ordinary test of candour.
> **Ordinary reading:** one is lying. **Correct reading:** a pull altered the fact and left both
> retentions standing. The *shape* of the disagreement is the signature — agreement on inventory,
> disagreement on sequence. Reach 50 finds a cut face in the relational weave, dated to within a
> fortnight.
> **Finding:** the court records both accounts, adjudicates neither, and proceeds against whoever
> performed the operation rather than against either witness.
> **What the subsystem must carry:** a court here **cannot use *one of you is lying* as its default
> frame**, and needs a distinct category of proceeding for the operated-upon case. That is not a
> refinement of evidence law; it is a different foundation for it.

**And the inverse is the setting's most important countermeasure.** A pull changes the record and
**preserves the witness's retention**, so sworn testimony from retained experience is evidence
*against* a documentary record. This inverts the evidentiary hierarchy a literate society would
otherwise develop, and it is why a threadworking polity keeps large bodies of sworn witnesses and
re-swears them on a cadence rather than trusting its archives.

### 3.5 Practitioner testimony is structurally hedged

> **The adept in the witness box.** A practitioner testifies that she performed a lawful
> restorative working on a granary.
> **What she can assert:** what she intended, what she did, at what scale.
> **What she cannot assert:** that she is currently reliable. The self-presentation that would be
> required to vouch for her perception is the one that fails first, so the honest answer available
> to her is that it was *as though* it were sound.
> **What the court has instead:** the observers. Two fellow practitioners describe her differently
> — not in opinion, in what they perceived — and their disagreement is the more probative evidence
> about her state.
> **Consequence for the subsystem:** advocacy attacks a practitioner-witness through the **outward
> facing**, never through cross-examination of self-report, because self-report on this point is
> structurally unavailable.

### 3.6 The drifting practitioner as an uncontrollable asset

> **The envoy who answers early.** A negotiator well into Dissonant, across a two-hour session,
> answers the concession the other party has not yet offered — not the words spoken, the position
> behind them. Three times. Twice he begins a reply a half-beat before the question ends. The
> opposing envoy experiences this as being read and adjusts by conceding what has already been
> answered.
> **The cost:** by the third occurrence the opposing party stops negotiating and starts recording.
> The session's outcome is favourable; its transcript becomes a heresy exhibit.
> **The rule: a drifting practitioner wins the room and loses the record.**

**Usability by band** — the table a house actually plans around:

| band | usable for | not usable for |
|---|---|---|
| **Stable** | anything, including public counsel | — |
| **Dissonant** | private survey, closed negotiation | any proceeding of record |
| **Fragmented** | working-site operations only | any room with a rival's diagnostician, or any witness who will later testify |
| **Fractured** | nothing political | — |

> **The retirement that came too late.** A house keeps its best diagnostician on the negotiating
> staff at Fragmented, because his reads are the best they have. Two members of the opposing
> delegation afterward describe him differently — in what they saw. He is knotted to his household:
> his daughter begins reporting a fractional lead in her perception of rooms, and his under-steward
> cannot hold it and leaves service. **The opposing house does not need to prove anything. It needs
> to seat him opposite a witness twice and let the record accumulate.**
> **The rule: rotate on exposure, not on the value of the reads.**

---

## 4. `systems/mass_battle` — command, terrain, and the theatre

### 4.1 The commander's instrument is prognosis, not operation

> **The line that was going to break.** A general holds a two-mile front. His prognostic staff
> survey his own formations at first light and read that the left-centre regiment is tending
> toward rout — not from casualties, which are light, but because the configuration is going
> there — while two regiments on the right are tending to hold well past what their strength
> suggests. **Cost: nothing. Enemy detection: none below reach 70, and the read leaves no trace.**
> He does not reinforce the left-centre. He withdraws it before contact and extends the right. The
> manoeuvre looks like a mistake to his own officers and to the enemy commander.
> **What it bought:** the battle. And note what he did *not* do — no operation, no cost, and
> nothing for a rival diagnostician to find afterward.

**This is the whole shape of competent command with threads.** The general who reads and does not
work wins cheaply and leaves no evidence.

### 4.2 Terrain preparation is the decisive use, and nobody can see it

Landscapes are already tending to produce crossings, channels and discontinuities, so accelerating
one is restorative and free — and invisible below reach 70.

- A ford that was going to form, formed the night before a river crossing.
- A track through country the army needs, faster than the enemy expects.
- Drainage that turns ground the enemy is counting on into ground they are not.
- Fire-breaks shaping where a burning countryside can and cannot spread.

> **The ford that was not there yesterday.** An army marches to a river expecting a two-day
> crossing. The enemy crossed in six hours the previous night at a ford its own scouts had
> reported impassable a week earlier. The general's staff, topping out below reach 70, **find
> nothing** — no held configuration, no cut face, no residue, because a restorative working on a
> crossing the river was tending to make leaves nothing at that reach. He concludes the scouts
> were wrong or the water dropped.
> **The staff requirement this generates:** an army campaigning against a thread-capable opponent
> needs at least one Structural-scale diagnostician, or it is fighting an enemy whose preparations
> it is constitutionally unable to perceive. Such practitioners cannot be trained to order, which
> makes them the binding constraint on strategic parity.

**A campaign decided by threadwork looks, to every participant and every later historian, like a
campaign decided by good roads.**

### 4.3 No command lattices, and no held formations

> **The knotted corps.** An army knots its commander to four corps commanders. Orders arrive
> without couriers; each corps commander knows where the general's attention is in the way one
> knows one's own arm.
> **The failure mode:** each becomes partly renderable only through the general — their own staffs
> report that speaking to them is like addressing the army rather than the man. The five co-date,
> so their after-action reports agree in a way a board of inquiry reads as collusion. Drift
> propagates through every knot in all three dimensions, so the general's adept's accumulation
> reaches four corps and their staffs. And a corps commander killed is a knot severed **mid-battle**:
> the general loses part of what held him in configuration, with no remedy.
> **Verdict: recommend against.** A lattice is a structure that degrades exactly when it is needed
> and damages its members when they disagree — which is what men under bombardment do. Force
> distributes by topology rather than by sum, and a practitioner whose contact closes mid-working
> loosens what they held.

> **The regiment that did not break.** A regiment is tending to rout; its brigade's adept weaves
> its Discipline. **Manipulative, two steps, plus a step per season — indefinitely.**
> It holds, and continues past the point where casualties should have ended it. Its men stop
> taking the field's ordinary marks: fatigue that does not accumulate, wounds that do not slow them
> at the rate the wounds warrant. The regiment becomes hard to give orders to — runners report the
> men answer the *intent* of an order rather than its words, which works well and cannot be relied
> on. Neighbouring regiments will not billet beside them. Its own account of the action does not
> compose; company officers give sequences that do not join, and all of them are honest.
> **Released, it routs** — the configurations resume what they were tending toward. Maintained, it
> is a permanent liability.
> **Verdict:** buys one battle and creates a regiment nobody can billet, disband, or send home.

### 4.4 The knotted garrison commander, from the commander's side

> **The order that cannot be countermanded.** A colonel is knotted to a fortress. **Two steps.**
> **What the house gained:** damage to the territory registers on him materially, and — the
> militarily useful direction — his continued function stabilizes the holding.
> **What the house cannot now do: move him.** He does not leave, because he stops forming the
> intention. Removed to a distance, his configuration begins failing within days and recovers on
> return. When the strategic situation changes and the fortress should be abandoned, the house must
> choose between the fortress and the officer — **and the choice was made two years earlier by an
> adept solving a different problem.**
> **If the fortress falls,** the knot severs by event. He survives, reads to observers as occupying
> slightly more space than his body, and is apperceived differently by different observers. He is
> unemployable as an officer and there is no remedy.
> **Command rule: knotting is a permanent commitment made under temporary conditions.** Reserve it
> for holdings the house intends never to trade.

### 4.5 The sea gets less, and it matters

Water and weather are not available: rivers do not tend to move, rainfall patterns do not tend to
change, coastlines do not tend to relocate. **Naval command derives materially less from threadwork
than land command.** What remains is almost entirely diagnostic or pre-assembly.

| application | direction | cost |
|---|---|---|
| Seasoning timber, curing cordage, tarring | restorative | free — fleet maintenance is the best-suited industry in the setting |
| Reading where a shoal is tending, where a channel is silting | diagnostic | free — navigation as prognosis |
| Reading which of your hulls is tending to fail | diagnostic | free, and it decides which ships sail |
| Accelerating a hull repair the timber was going to take | restorative | free, **in port only** — a Leap at sea is §2.1's problem |
| Holding a hull sound that is not | manipulative | a step, plus per season, and crews will not serve on her twice |
| Weather, current, wind | — | **not available** |

> **The fleet that sailed and the fleet that did not.** An admiral has nineteen ships and orders to
> force a strait in eleven days. His adept surveys the fleet over three days at no cost, and reads
> that four hulls are tending toward failure within the season — two of them ships his captains
> rate sound — while two his carpenters have condemned are tending to hold. He sails with
> seventeen, including both condemned ships, and leaves two sound-rated hulls in port. His captains
> regard the decision as inexplicable. **He loses none. The two left behind open their seams at the
> mooring within six weeks.**

**And the sea keeps no boundaries**, which is the one place the externalities are lighter: no
tenure records to fall out of agreement, no families holding incompatible accounts of who ceded
what, no sowing calendar to decohere. A fleet is also naturally lattice-free — ships are dispersed
and contact windows unreliable at distance. **A polity whose thread practice concentrates in its
navy is running the least dangerous version of the technology available to it.**

### 4.6 Theatre tension is a line item

Sustained manipulative work raises substrate tension in the province, tension produces incursions,
incursions drop Accord, and low Accord forces the local faction into mandatory response —
consuming action slots before anything else is scheduled. **Both armies bear this, along with
everyone living there.**

> **The province taken and the province held.** A general takes three territories in a season with
> heavy manipulative work: two held supply configurations, one Structural past-pull, one held
> regiment. Season 1: three territories, and the campaign is judged brilliant.
> Season 2: tension in the pulled province crosses threshold. An incursion arrives, deteriorates
> within hours having killed nine people, and drops Accord — forcing a mandatory governing action
> before the general's own plans are considered.
> Season 3: the held regiment costs again. The senior adept is withdrawn. The two held supply
> configurations must be released or paid for, and releasing them means the garrisons starve on the
> schedule the substrate originally set.
> **Net: three territories taken, and the action economy for holding them spent on consequences the
> campaign generated.**

**War-fighting with threads manufactures monsters in the theatre**, and those conditions outlast
the campaign. **Threadwork is very good at taking a territory and structurally hostile to holding
fifteen.**

### 4.7 Doctrine for a competent threadworking army

1. **Terrain first, and almost only.** Free, decisive, invisible.
2. **Medical second.** Accelerating recovery in the wounded who were going to recover is the
   largest sustained return, and it moves the adept toward their own equilibrium rather than away.
3. **Diagnostic corps over operative corps**, several to one. The enemy's ceiling determines what
   you can do invisibly.
4. **No battlefield lattices. Do not hold formations.**
5. **Adepts off the line**, workings prepared in advance and off-site.
6. **Structural past-pull reserved for the war-deciding case, once**, accepting detection and
   archival damage.
7. **Do not fight what a cordon handles.**
8. **Budget theatre tension** as an operational cost borne by whoever holds the province after.

---

## 5. `systems/fieldwork` — investigation and forensics

The domain the content rule shapes most sharply, and the one where thread practice and ordinary
detection are useless apart and formidable together.

### 5.1 Two disciplines, and neither closes a case alone

| a thread-investigator establishes | a thread-investigator never establishes |
|---|---|
| that an operation occurred | what it contained |
| at what scale | what was said or intended |
| roughly when | motive |
| roughly what reach performed it (at 70+) | identity |
| that a knot exists, and its scale | who the knot is to |
| that a configuration is orphaned | what its cause was |
| that an instrument is held | whether its contents are true |

**Thread forensics establishes the *shape* of a crime; ordinary investigation establishes its
content.** A service employing adepts without detectives, or detectives without adepts, is working
with half a method.

### 5.2 Orphan signatures are legible to anyone — the bridge between the two

This is why a non-sensitive investigator is not helpless, and it is the suite's best single piece
of applied design.

> **The appointment nobody obeys.** A magistrate's clerk notices that requisitions for the harbour
> office are being signed by a deputy, and have been for two months, though the harbourmaster is
> present daily and in good health. **No adept is involved in this observation.**
> Referred to a diagnostician: an orphaned configuration at Personal scale, decaying at roughly
> twice the ordinary rate, and upstream a cut face in the relational weave dated to within a
> fortnight of the appointment. **Known:** the appointment's cause was pulled. **Never known:** what
> the reason was. **How the case actually closes:** ordinarily — the clerk finds who benefited from
> the appointment being uncontestable, and the diagnostic finding supplies the warrant.

**Teach conventional investigators the shapes.** Authority that fails to register. A habit whose
cause is missing. An institution routing around a functioning part. These are orphan signatures and
they are legible without any reach at all.

### 5.3 The honest contradiction, run forward as technique

> **The two accounts.** Two witnesses to a fire give incompatible accounts. Both are candid,
> neither benefits, and their accounts **agree on inventory and disagree on sequence**.
> **Ordinary conclusion:** memory is unreliable, discard both. **Correct conclusion:** that
> specific disagreement shape is a pull signature. Directed diagnostic at reach 50: a cut face,
> dated within the fortnight.
> **The rule: honest irreconcilable witnesses are a lead, not a dead end.** An investigator who
> resolves contradictions by deciding which witness is mistaken has discarded the evidence.

### 5.4 Wrapping is a trace of presence, and it is not a fingerprint

Wrapping accumulates in rooms a practitioner uses repeatedly, until every entrant reports a
presence with no content. It establishes that someone spent time there, and roughly how much. **It
does not identify.**

> **The room that was used.** A merchant is found dead, no marks, no obvious cause. His
> counting-room reads clean; the disused store adjoining it reads heavy wrapping.
> **Established:** a practitioner used that store repeatedly over a period, probably months. Not
> who. Not for what.
> **What it does for the investigation: it relocates it.** The store has a separate door onto a
> lane, a lease, a keyholder, and deliveries — all ordinary detection, none of which would have
> been examined without the read.

### 5.5 Interviewing someone who has been worked on

The barrier gives a testable protocol: **propositional retention survives; actionable capacity does
not.**

> **The smith who cannot smith.** A man is suspected of having had eleven years pulled from him. He
> denies it, and denies it honestly — he does not experience a gap, only an unexplained callus.
> **Wrong technique:** ask him about smithing. He names every tool, describes every process,
> answers at any level of detail. Propositionally he is a master.
> **Right technique:** put a hammer in his hand and ask him to draw out a taper. He cannot — and the
> diagnostic point is that **he does not know he cannot until he tries.**
> **What this establishes:** a gap between recitation and capacity, which is a pull's signature
> rather than deception's. **A liar's recitation and capacity fail together.**

### 5.6 The interrogator's own hazard, and it is unique to this setting

> **The witness ruined by questioning.** An investigator questions a witness about a place-name
> across four sessions, returning to it perhaps forty times. The name stops arriving as a word for
> her: she hesitates, then substitutes descriptions, then cannot produce it at all. Her account
> degrades and her confidence with it.
> **What happened:** ordinary satiation, produced by the investigator — in a setting where the same
> symptom is also a threadwork signature. **The compounding error:** a diagnostician later reads her
> difficulty as evidence of an operation. **It is not. The investigator manufactured the signature.**
> **Protocol requirement:** vary the referent, cap repetitions, and **record the count** — an
> interview log here must show how many times a term was put to a witness, because that number is
> exculpatory evidence about the witness's degraded recall.

### 5.7 Cold cases do not go cold, and the archive can be a crime scene

> **The knot that outlived everyone.** A succession is contested on the grounds that a marriage
> forty years earlier was arranged under an unlawful binding. Every party is dead. A diagnostic on
> the surviving daughter reads a **dissolved** relational knot in her mother's line, still legible.
> **Established:** a knot existed and was dissolved. Not who made it, not why, not whether the
> marriage was otherwise valid. **What it does:** makes the claim triable, forty years on, where no
> document and no witness survives.
> **Consequence: houses carry forensic liability across generations for operations nobody living
> performed.**

> **The register that was mended.** A land register carries a held configuration across four folios,
> readable at reach 30. **First inference:** fraud. **Correct inference:** the records office mended
> its own water-damaged register two years ago, in good faith, using its own adept.
> **What the investigator now cannot do:** distinguish lawful mending from fraudulent alteration on
> those folios, ever. The signature is identical.
> **The rule this enforces: an archive that works its own holdings has not damaged its records. It
> has destroyed their admissibility.**

### 5.8 Investigating an incursion — the file must not contain a motive

> **The evening that was organized.** A district reports that for one evening the snow fell in a
> pattern, the pattern meant something, and then it stopped.
> **Establishable:** that a transient event occurred; its duration and extent; the district's
> tension before and after; whether manipulative work was performed nearby in preceding seasons.
> **Never establishable:** why the surfeit took that form. No causal claim about the ground is
> supportable, and any account attributing responsiveness to it is wrong.
> **What must not happen: the file must not contain a motive. There is no entity to have had one.**
> The service needs a category of finding that records an occurrence with no agent, and its officers
> need training not to supply one.

### 5.9 Doctrine for an investigative service

1. **Pair every adept with a conventional investigator.** Neither closes a case.
2. **Teach the orphan signatures to non-sensitives.**
3. **Treat honest irreconcilable witnesses as a lead.**
4. **Test capacity, not recall,** on any subject suspected of a pull.
5. **Log repetitions** — the interview degrades the witness and manufactures the signature.
6. **Never work your own archive.**
7. **Retire on exposure, not on competence.** A drifted investigator is an impeachable witness, and
   a service's best are usually its most exposed.
8. **Record incursions without agents.**

---

**Continues at `threadwork_applications_part2.md` §6** — faction politics and domain actions, the
twelve civilian sectors and the institutions they require, the strategic layer, presentation and
UI, the prohibitions, and the record of what was carried across from the suite and what was not.
