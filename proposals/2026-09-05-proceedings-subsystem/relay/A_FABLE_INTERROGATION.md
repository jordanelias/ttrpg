> ## RELAY STAGE A · THE INTERROGATION — `fable`, read-only, informing only
> ## Status: **PROPOSED (2026-09-06). NOTHING HERE RATIFIES ON MERGE.**
>
> **This is the first of four stages preserved verbatim so the relay is checkable rather than
> asserted.** `17_PLAYABILITY.md` adjudicates; these four files are its evidence, and none of them
> is the deliverable.
>
> **What this stage was, and what it deliberately was not.** Jordan, 2026-09-06: *"fable 5.1 isn't
> supposed to be writing output as an agonist, only informing an agonist."* So this pass has **no
> positions and authors no mechanism.** It supplies the census of binaries, the precedent survey, the
> option surface, the refusals with the axiom that builds each wall, and — in §4.6 — the places it is
> least sure, handed forward rather than hidden. **The agonist (stage B) is a separate model that
> takes this as established and is answerable for every position it then takes.**
>
> ⚠ **Read §4.6 first if you are looking for the weak joints.** This pass names them itself, which
> is why the antagonist stages did not have to find them.

---

# FABLE PLAYABILITY — interrogation, precedent, and the option surface for `proposals/2026-09-05-proceedings-subsystem/`

**Fable 5.1, 2026-09-06 — read-only audit and planning, informing an agonist.** Per `CLAUDE.md` §10
(RULED 2026-07-28) this tier does not author artifacts. §1 and §2 below are the finding set and the
precedent verdicts; §3 is the **option surface and the refusals** an agonist needs and cannot get
without a guardrail pass — a list of levers and a list of walls, not a design. No number is supplied
anywhere; where a magnitude is needed the note says *inject, declare, sweep* (`ID-6`).

**Jordan's brief, verbatim:** *"interrogate the proposal as it stands … to make it function as a
structure for a playable videogame rather than be a mere flowchart, review acclaimed precedent games
… then present ways to convert this proposal into something playable where outcomes are not precluded
and conditioned solely upon constraints and binary choices, but gradients and creating then seizing
opportunities with other characters or the venue format."* The third clause is the agonist's; this
document supplies what it needs.

---

## 0 · Reading note — what was read, and four facts the antagonist should have

All seventeen files were read in full, `15_WHY_IT_IS_A_GAME.md` first; `13_ADVERSARIAL.md` was
written at 01:19, after this pass's first directory listing, and was read once it appeared. The
engine was read at `engine/autoload/sigma_leverage.py`, `engine/autoload/dice_engine.py` and
`skills/valoria-resolution-diagnostic/SKILL.md` §11. The executable chain was read at
`proposals/2026-09-02-executable-architecture/{verb_table,rosters,write_matrix}.yaml` and
`proposals/2026-09-01-season-loop-tests/tracer/shape.py` (dataclasses `:2067-2440`, witness predicates
`:4355-4380`). Axioms and theorems at `proposals/2026-09-03-meta-architecture/01_AXIOMS.md`.

1. **Three findings below were reached independently by `13_ADVERSARIAL.md` and are credited, not
   claimed.** Its #15 (`P-36`: `release` points the wrong way, *"FORGIVENESS IS CURRENTLY
   INEXPRESSIBLE"*) is this pass's `B-19`. Its #20 (`P-41`: descent is free in six closed-floor rows)
   is `B-20`, which this pass had missed. Its #17 corrects a genre label this pass had wrong
   (Demosthenes on the crown is a *deliberative* claim in a court, not epideictic) — corrected
   throughout. Independent rediscovery on disjoint charges is `§G.4.3`'s corroboration signature; the
   overlap raises the grade of those three rows.
2. **The seven-register roster and the twelve-kind speech roster exist in no data file at the commit.**
   `grep -n "registers\|speech_kinds"` over `rosters.yaml` returns nothing. `03_PARAMETERS.md:380` writes
   `registers: [ <subset of the seven> ]` and `04_VERBS.md:144-148` writes *"`rosters.yaml`: `speech_kinds`
   — a closed set in DATA"*. Both describe rosters not yet authored. Under `§0.05` they are reference.
   Two binaries below (`B-1`, `B-3`) are keyed on rosters that are not rows, so there is nothing to delete.
3. **`release` is the DEBTOR's verb.** `04_VERBS.md:451-452` — `requires: "a live Tenure of the named kind
   whose subject is the actor"`. `oblige`'s subject is the party who owes (`03_PARAMETERS.md:317`, the
   advocate holds *"an `oblige` to that person"*; `14:230` *"an `oblige` opened — a duty one of them now
   owes"*; `T-m`, *"a duty can always be forsworn"*). So §B.5's *"releasing something you could have held
   them to"* is a non-owner write under `AX-4`. The holder of a debt has no verb in either direction.
4. **`Event.subject` is set to the actor today** (`13_ADVERSARIAL.md:53`, #8; `01_AXIOMS.md` `T-d`:
   *"honoured in a field name and violated in mechanism"*). This matters for §3.2: an intra-run fold over
   emissions *can* attribute a descent at this commit, even though `T-d` says it should not be able to.
   A lever that depends on attribution is standing on a defect the chain intends to fix (`W24`).

---

# PART 0 · THE ENGINE CHECK — which gradients already exist, and which the design fails to read

The brief asks where a new gradient is needed and where the design merely fails to expose one it
has. Against `dice_engine.py` and `sigma_leverage.py`:

| the gradient | in the engine? | read by the design? | verdict |
|---|---|---|---|
| **effect — how well it landed** | ✅ `degree_from_net`, four bands on a continuous margin; whole-success-wide Partial; fractional `net` and `ob` (`dice_engine.py:227-301`) | ✅ `speak` keys `writes`/`emits` on the four | **exposed.** Blades' *effect* axis |
| **position — what failure costs** | ⚠ margin below zero is continuous; the ladder bands it as one `Failure` | ❌ `04:72` `Failure: ["Person.stance"]` at every margin and every rung. `03:35` says recoverability *"governs what a misstep WRITES"*; the row keys on band alone. And the ladder tuple's `track` column (`03:228-229`) *"is read by nothing"* (`13:55`, #10) | **carried by the study, dropped by the row.** Position is the rung |
| **advantage — a named level, uniform at every pool** | ✅ `LEVEL_SIGMA` minor/moderate/strong/major → `levels_to_net_sigma` → `net_boost`; `Δz = soft_cap(net_σ)` at every pool (`sigma_leverage.py:97-102, 190-203`) | ❌ `06:271` — *"available and not used by the five terms"* | **a whole channel unused** — the only lawful carrier for an edge that is *bought* rather than *composed* |
| **the veto** | ✅ `BandExtension.may_overwhelm` — declared, named, can only demote 3→2 (`dice_engine.py:95-138`) | ⚠ `08:42` carries a second `veto : bool` at the seam | **two homes for one demotion** (`T-k`) |
| **how much of yourself you bring** | ✅ fractional pool, floored at 1D on mean and variance (`sigma_leverage.py:275-279`) | ✅ `pool = brought + conduct × latitude` (`06:83-86`) | **exposed** — the Citizen Sleeper cousin (§2.3) |
| **confidence of a read** | ✅ `Claim.confidence: int` (`shape.py:2157`) on every claim | ❌ `interview` (`04:339-350`) writes `[]` at every band and says nothing about the deposited claim's confidence | **a field left at default** |
| **degree on a finding** | ✅ `Tenure.degree` (`shape.py:2086`), written by `determine`, read by nothing (`F.4`) | ❌ `00:275-319` withdrew the design's claim to read it | **a compromise gradient with no reader** |
| **Ob composition** | ✅ ruled 2026-09-06: five terms compose, floored at 1 (`06:210-225`) | ✅ | the channel every priced-not-precluded lever uses |

**Reading.** Two of seven gradients are exposed. **Four are carried and unread** — position-by-rung,
the σ-channel, `Claim.confidence`, `Tenure.degree`. *"Zero new fields"* is true; its cost is that the
design also declined to read four fields the tree already had.

⚠ **A contradiction between the diagnostic and the proposal.** SKILL.md §11.5 lists **P-i · Legible
odds** — failure is *"the player cannot read their chance; advantage surfaced only as an opaque roll
modifier rather than a named level"*. `15:140` rules *"NEVER SHOW THE PLAYER A NUMBER THEY COULD OPTIMISE
AGAINST"*. They reconcile only on a narrow reading — P-i wants **named levels of your own advantage**,
PART E forbids **the obstacle, the margin, a percentage** — and that reading is the Disco Elysium half
that survives (§2.3). If the antagonist reads P-i as *odds*, one document must yield.

---

# PART 1 · INTERROGATION — where outcomes are precluded, binary, or make the player a respondent

**The charge:** *outcomes are precluded and conditioned on constraints and binary choices.* Each row
quotes the file and line. A quoted `requires` that returns before the draw is a finding; a feeling is not.

## 1.1 · The binaries

| # | the binary, quoted | file:line | what it precludes |
|---|---|---|---|
| **B-1** ⭐ | *"What varies is whether the move is APT — and an inapt move is REFUSED, not discounted."* … genre: *"a mismatch fails `requires`"* | `04_VERBS.md:138-139, 157` | **refusing the frame.** The design's own §B.3 bend (`03:133`) says Demosthenes *"wins by refusing the forensic frame — he plays the second game"* (a deliberative claim in a court, per `13:67`); under this row his move fails `requires` and forms no Candidate. A refused act teaches nothing and costs a turn. **The proposal has already written the argument against itself**, about licence, four sections later — `03:159-161`: *"It is always a demotion … unlicensed frankness is not impossible, it is priced as an attack"* — and did not apply it to aptness |
| **B-2** | `veto : bool` — *"the ladder takes the minimum"*; the four conjuncts *"all four hold, or the speech is received as an attack"* | `08_SEAM.md:17, 42`; `03:166-173` | four separately-named failures collapse to one bit that demotes one band. Failing one conjunct and failing four are received identically |
| **B-3** | `registers: [restricted]` on six rows; *"`registers: [restricted]` means they do not choose their manner"* | `03:380, 487, 512, 517, 527, 584, 648` | a manner is in or out; Fig. 8's misreading map — which the design says is read *"at deposit time"* — never reaches the choice. And the roster does not exist in data (§0 note 2) |
| **B-4** | `proofs: []` — *"the future admits no witnesses; the fact is not in dispute"* | `03:558, 561-563`; `14:108-111` | at a deliberative body no `tell` counts. But `14:113-119` (`P-24`) shows the invasion debate contains a HOLDS sub-matter (*is the threat live*) — a record told there addresses a different Proposition, not nothing |
| **B-5** | *"GO? … SEND? an advocate goes. Lower latitude · you cannot concede in absentia … NEITHER?"* | `07_THE_GAME.md:50-55` | three discrete options; the advocate is a whole substitute or nothing; a letter, a sworn statement carried by a clerk, being spoken for by a debtor are not degrees. And `13:61` (#11, `P-33`): the design collapses *declined / could not / was not admitted* into one absence |
| **B-6** | `disposal: bench \| mutual \| none`; *"`disposal: mutual` is defined over TWO parties"* | `03:364`; `14:92-95` | who may dispose is fixed before the run; a conclave, a vote, a five-party peace are unrepresentable (`P-15`, regraded a coverage bound) |
| **B-7** | *"`appeal_basis: none` is what makes it arbitration"*; *"A player who wins the choice of arbiter has usually won"* | `03:479`; `07:256-257` | finality is a key, not a price |
| **B-8** | `verdict_reasons: given \| withheld` — *"the subject cannot even learn what moved it"* | `03:387, 520-521` | learning is one bit; Fig. 13's three columns collapse to it (`13:67`, #17); `interview` of a bench member afterwards is a live act the key silently overrides |
| **B-9** | *"`term_required: false` … is the whole horror of it, and it is one boolean"* | `03:530-531` | the proposal is proud of this. A term is a wound clock with a `closer` (`T-n`; `P-04` unbuilt); the horror is that the closer is *unreachable*, which is a distance |
| **B-10** | `order: free \| rank \| alternating \| scripted \| written_only` — *"the subject does not choose when to speak"* | `03:378, 516`; `05:18` | who speaks when is fixed at load. No point of order, no yielding, no motion. The venue is *"a row, not state"* (`00:119`); `13:63` (#13) notes `order` is an enum the provider *must switch on* |
| **B-11** | `Failure: ["Person.stance"]` at every margin below zero | `04:72, 124-129` | a near-miss and a rout are one event. ⚠ And **whose** stance is unstated; under `AX-4` a seam-fed fold can write only the actor's own |
| **B-12** | *"`Read` and `Misread` emit IDENTICALLY"*; the row writes `[]` at every band | `15:88`; `04:344-345` | correct by `AX-2`, but the deposited claim's `confidence` comes from nothing — the player gets a read with no feel of how sure their character is. The study's hazard is *confidence without accuracy*, a gradient on confidence, not its absence |
| **B-13** | `Partial: []` — *"the speech that moved nothing"* | `04:71, 116-122`; `06:273` | the middle band is the emptiest — the inversion of Apocalypse World, where 7–9 is the whole design |
| **B-14** | *"`rung(run) := the lowest rung any emitted matter.* Event in THIS run has named`"* — descent only, self only, one way | `00:298-302`; `05:76-86` | you cannot be *drawn* down by an opponent's Overwhelming; cannot step half a rung; cannot climb. A ratchet you turn yourself |
| **B-15** | `stakes_grade: terminal \| costly \| free` — *"the one most likely to be deleted"* | `03:388, 411` | a grade as a key |
| **B-16** | *"say nothing — not an act. It emits nothing, writes nothing"*; `withhold*` … *"is not an act at all"* | `07:74`; `04:149-151` | **silence when the order reaches you is free and invisible.** Liudprand *"said nothing at the time because of the pain in his heart"* — and recorded it, because the room saw it. The *Guiguzi* loop's *"listen again"* has no move |
| **B-17** | *"a per-genre resolver … refused, and the refusal emits"*; *"an `obstruct`-shaped rule for the floor … The second is refused by the fold"* | `00:327, 330` | two of the seven "deletions earned" are refusals. The floor is first-come; the genre is a gate |
| **B-18** | roles are *"membership in a set of edges"* — party by own `commit`, advocate by own `commit` + `oblige` | `03:312-320` | correct — and it means **you cannot make anyone a party.** Every route into the room is first-person; the design gives no second-person lever |
| **B-19** ⭐ | `release`: *"a live Tenure … whose subject is the actor"* | `04:451-452` (§0 note 3; `13:65` #15, `P-36`) | **the creditor has no verb.** A hook, a marker, a favour owed has a carrier (`oblige`) and no holder-side act, to call or to forgive. Row 14 (*leave a way down*) is not cleared |
| **B-20** ⭐ | *"the descent is FREE when nobody is watching … A closed room is a room where you can concede cheaply"* — and `floor: closed` on six rows, three of them `stakes_grade: terminal` | `07:115-118`; `03:424, 428-430, 432`; `13:70` #20 (`P-41`) | the concession's price is the witness count, and the floor key sets it to zero or not. *"The design's core tactical decision is cheapest exactly where the study grades the stakes TERMINAL"* — a gradient (how many saw it) collapsed by a key |

## 1.2 · The respondent finding — one shape shared by all twenty

The design's own loop is *"deciding what to spend and what to keep, in a room whose mind they cannot
see"* (`07:13`). The four decisions — be there · descend · spend a proof · say the thing (`07:23-29`) —
are each a response to a room that already exists. The arrangement is *"a row, not state"*; the bench
is a Query; the order is a parameter; the floor is who travelled. **Nothing in the four changes the
room.**

`14:290` then forbids *"a participant who is in the room by the arrangement's say-so."* Correct under
`AX-1` — and it cuts both ways: if the arrangement may not put people in the room, people get there
only by acts, and **the design supplies no act by which one person brings another.** `move`, `commit`,
`oblige` are all first-person. That is §3(b)'s gap, and it is not closable in the arrangement row; it is
closed by what one person can put in another's ledger before the day — which is `tell`/`interview` +
`P-05` + `H-72`, and all three are open.

⚠ **The honest precondition, before §3 lists levers:** every lever that runs through another
character's decision is blocked on the edge `14:182-186` measures — *belief → decision: SEVERED; over
4,800 claims, zero can fire.* §3.2 marks which levers are blocked so the antagonist need not find it.

---

# PART 2 · PRECEDENT — the mechanism each acclaimed game uses, and whether it survives the axioms

**Column key.** *Survives* tests against `AX-1` (only a person acts), `AX-2` (no privileged access),
`AX-3` (true ≠ right), `AX-4`/`T-a` (one owner; no stored aggregate), `T-f` (`choose` has no `World`),
`T-k` (one ladder), and the zero-new-primitive bar. *Cousin* is what an architecture-compatible form
would have to be — a verdict, not a design. *Cost* is against the count if the cousin were pulled.

## 2.1 · Tabletop / RPG

| game | the mechanism, extracted | survives? | the architecture-compatible cousin would have to be | cost |
|---|---|---|---|---|
| **Dogs in the Vineyard** | **raise / see / give**: dice pushed forward; to see a raise you match it; you may **give** at any point, keeping what you have; escalating the *arena* (talk → physical → guns) adds dice and adds **fallout** scaled to the arena reached. *Conceding is a first-class move with a price; escalation raises stakes and cost together* | ✅ mostly. Give = `repudiate`/descent (exists). Escalation = the nested contest at depth+1 under the caller's cap (`11:75` — *"the nesting is the pause"*). ❌ **the visible dice pile** is a shared track (`T-a`) | escalation as *which prize is now contested* — the same `seam.contest` one deeper, entered by an act; fallout as writes keyed on the rung reached | 0 |
| **Burning Wheel — Duel of Wits** | **Body of Argument** per side; scripted volleys (Point / Rebuttal / Dismiss / Avoid / Obfuscate / Incite / Feint) resolved by pair; **the winner compromises in proportion to the BoA they LOST**. *The anti-binary mechanism par excellence* | ⚠ BoA is a per-side track — refused as a field (`T-a`). The 7×7 volley table is a per-pair rule (`04:165`'s emergence rule). **The compromise rule survives whole** — it is a function of the margin, and the seam returns a margin | a reader for `Tenure.degree` on the finding — Success and Overwhelming producing different downstream state for the loser's `commit` and the appeal path | 0 — reads a field with a writer and no reader |
| **Blades in the Dark** | **position × effect** declared before the roll — position (controlled/risky/desperate) is *what failure costs*; effect is *what success buys*; traded against each other. **The devil's bargain**: a die *now* for a complication *later*, chosen. Stress spent to resist consequences | ✅ effect = the ladder. ⚠ position = a graded Failure write — the design has one. ✅ the bargain = a σ-level (`LEVEL_SIGMA`) bought with an `oblige` opened now — the unused channel is the exact carrier. ❌ stress as a meter — a field | position = the rung's `track` (unread, `13:55`); the bargain = `levels_to_net_sigma` paid with a Tenure the buyer opens | 0 |
| **Apocalypse World** | **7–9 is the whole design.** 10+ you get it; 7–9 *at a cost, or a lesser version, or the MC chooses*; 6− a hard move. The middle band is the richest | ⚠ the four bands exist; the middle's *content* is inverted (`B-13`). No MC — "the MC chooses" must become a derivation | Partial advances *and* costs, the cost derived from the run's own emissions (the `proofs told so far` fold, `06:221`, is the precedent for any intra-run gradient) | 0 |
| **Ars Magica — Certamen** | a duel of wills; the loser each round takes **fatigue**; ends on exhaustion or concession; the winner's margin sets what may be imposed | ✅ the scene budget is the fatigue; the descent is the concession; the margin is the return | already present at the season scale | 0 |
| **Pendragon** | **traits and passions act AGAINST the player** — rolled by the GM when a knight acts against his nature; a passion can seize him. *Who you are is scored, not narrated* | ⚠ no GM; `Person.convictions` (`shape.py:2368`) exists and `score()` already sums `convictions × alignment` for NPCs (`14:159`). For a PC it may not gate (`§A.2`); it may price | a term in the speaker's **own** Ob from the misalignment between the speech and their convictions — *visible effort once seen* is TERMINAL on the erosion list. Reads `PersonInterior`, lawful at `choose` and the resolver | 0 + one injected term |
| **Reign / ORE** | one roll, two axes: **width** (speed) and **height** (quality) | ⚠ the continuous engine returns one number; width has no carrier | width ≈ position in `order` — a public ruling before the roll. Not adoptable; recorded | — |
| **Microscope / Follow** | authorial: players *declare* history; no character viewpoint; consensus | ❌ **fails `AX-1` and `AX-2`** — a GM by committee | none. Named so it is not tried | — |
| **Blood on the Clocktower** | **information is the only currency**; nothing verifiable; every claim is a public act that commits its maker; play is contradicting earlier public claims; the Storyteller lies by rule; **death does not remove your voice** | ✅ **the design's posture already** — `AX-2` + `tell` + Read/Misread + *"a lie is `utter` of a false Proposition"* (`03:205`). What BotC has and the design has not read: **a public claim is immutable and authored** (`Proposition`, `frozen=True`, `shape.py:2425`), so contradiction with one's own spring offer is detectable by anyone holding both | `tell` whose subject is an *uttered Proposition* someone committed to in this run — the contradiction as the object. Needs `P-05` | 0 |
| **Sidereal Confluence** | real-time, simultaneous, **multilateral binding trades**; any deal any players agree to is enforced | ❌ multilateral mutual disposal is unrepresentable (`B-6`); real-time contradicts the ordered fold | a later act *declares* the matter carried — one person reads a Query and acts (`05:94-98`). That is Republic of Rome's cousin, not Sidereal's mechanism | **no cousin for the mechanism itself** (§3.4) |

## 2.2 · Board

| game | the mechanism, extracted | survives? | the cousin would have to be | cost |
|---|---|---|---|---|
| **Diplomacy** | **no randomness; simultaneous secret orders; the game is other minds.** Press unlimited and unenforceable; *support* lets one player's units act for another's plan; a stab is a promise unkept, and everyone remembers | ✅ **exactly the season scale.** DELIBERATE is simultaneous from a frozen world (`02:54-56`). Support = `commit` to another's disposition. A stab = `repudiate`, witnessed. Press = `tell` before the day. ❌ the nested run is *sequential*, so inside the room it is not Diplomacy | already present at the season scale; inside the room the order must become a resource (§3.2 venue levers) | 0 |
| **Republic of Rome** | the Senate with **a presiding magistrate who controls what is proposed and in what order**; any senator may **prosecute**; votes counted by influence; a shared enemy; offices with terms; *persuasion attempts* priced by loyalty and influence | ⚠ counted votes = `T-a`. ✅ the presiding magistrate = the seat whose `open_case` declares `Record.stages` (`T-n`). ✅ prosecution = `speak` with a person subject under Fig. 26. ✅ persuasion = `interview` + `oblige` | *who sets the docket* as a game before the game; *call the question* as a later act reading a Query (`05:94-98`) | 0 |
| **Pax Pamir (2e)** | **the market row prices cards by position**; **gifts** buy influence; loyalty changes priced by what is discarded; **dominance checks** the world runs; **patriots** act for a coalition they do not own | ✅ position-pricing = a gradient by order; gifts = `oblige`; loyalty change = `repudiate` + `commit`, witnessed. ❌ the dominance check as a world-initiated event is a fourth clock (`AX-5`) unless a `Date` winds it | position in `order` composed into Ob; the check as a `Date` somebody set | 0 + one injected term |
| **John Company** | **offices held by players in a company nobody owns**; failure in office costs the holder; patronage | ✅ seats + `T-o` + `AX-6` = `determine` `via` a seat, revocable, held against you (`07:320-334`) | present | 0 |
| **Twilight Struggle** | **the cost of holding a card**: playing the opponent's event for ops *fires it for them*; the headline is bid; timing is the game | ✅ a proof told deposits into *every* ledger including the opponent's (`06:368-372` — *"the deposit does not depend on the degree"*), so spending the card gives them its event — the mirror test is mechanical. ✅ the season between hearing and judgment (`04:244-249`, `P-14`) is the timing window | present; proofs *priced by what they hand the other side* rather than admitted-or-not | 0 |

## 2.3 · Videogame

| game | the mechanism, extracted | survives? | the cousin would have to be | cost |
|---|---|---|---|---|
| **Crusader Kings III** | **hooks** (a debt you may spend, weak or strong), **secrets** (a fact you hold that they do not know you hold; revealing is a move; blackmail converts a secret to a hook), **schemes** with progress and secrecy, **stress** from acting against traits | ⚠ secret = **every `Claim`** by construction (`shape.py:2149` — *"Lives in the HOLDER'S OWN ledger"*). Hook = `oblige`. Scheme progress = `Tenure.term` (`P-04`). Stress = Pendragon's cousin. ❌ **the holder-side act** — `T-m` makes closure the debtor's; the creditor has no verb (`B-19`). Blackmail is two acts by two people across two seasons | leverage as **publicity** — `tell` the room the debt exists (firsthand, attributed); mercy as a **counter-`oblige`** by the creditor. Both weaker and slower than a button | 0 — but the *feel* needs a verb (§3.4) |
| **King of Dragon Pass / Six Ages** | **advisors with biases who disagree**, each reading the situation through their nature; the player weights whose counsel to trust; **the clan ring**; the advisors are never the truth, only their read | ✅ **completely** — each advisor is a `Person` with `convictions`, a ledger, a stance; `interview` and they `tell` what they hold (`told_by`, at their confidence). The ring = the council row | the pre-day briefing loop. **Requires `P-05`** — today `interview` returns nothing usable | 0 |
| **Pentiment** | a trial where **the game never tells you the truth**; accuse on incomplete evidence under a time limit; the town remembers for decades; **you cannot investigate everything first** | ✅ `07:197-214` is Pentiment; the scene budget is the time limit; per-witness deposit is *the town remembers differently* | present | 0 |
| **Ace Attorney** | **press vs present**: press a statement (free; may reveal); **present evidence against a specific statement** — the contradiction is the object; a wrong present costs a fraction of a bar, never the case | ✅ press = `interview` in the room; present = `tell` whose subject is an uttered Proposition. ✅ the bar is a *priced* error — Ace Attorney does not refuse a wrong present, it charges | a proof apt in proportion to how directly it addresses a statement committed to in this run (`Claim.subject`, `Proposition.id`, and the run's emissions all exist) | 0 |
| ⚠ **Disco Elysium** — *the counter-example* | **shows the modifiers and the odds** ("+1: you noticed the boots; −2: he distrusts you; 63%"); white checks retry when the world changes, red once; **failure is content** | **why it works there:** single-player; the skills are *voices in the character's own head*, so the shown modifiers are `explain(p, v)` over `PersonInterior`, which `07:174-181` permits; the target is authored, static, the same on retry. **Why not here:** the odds include the hearers' hidden interiors (`15:55-85`), which move without the player's knowledge — a percentage is either stale or a leak (`AX-2`); a legible optimum against a static NPC is a solved proceeding (`15:10-27`) | **the half that survives:** the *sourced, named* modifiers from the player's own hand — *told by Aldric, three seasons ago, at his confidence* — as named levels, never summed, never a percentage. **Legible hand, illegible room.** That reconciles SKILL §11.5 P-i with `15` PART E | 0 |
| **Suzerain** | **political capital** as a spendable scalar; promises tracked; the constitution as an amendable document; every faction remembers | ⚠ capital = a meter (`T-a`); `Sensation.standing` is the computed cousin. ✅ promises = `oblige`; constitution = a `Record` | present at the carrier level | 0 |
| **Citizen Sleeper** | **dice rolled at the start of the day, ASSIGNED to slots by the player** — which action gets the 6 | ⚠ inside the run the draw is once-per-interaction, unassignable. ✅ **at the season scale exact**: ~5 scenes are the dice, occasions the slots; `pool = brought + conduct × latitude` means what you bring is the die you assign | present at the season scale; inside the run, *which proofs to spend here vs keep for the appeal* is the same allocation one level down | 0 |
| **Fallen London / Sunless** | **qualities as numbers that unlock storylets**; menaces accumulate and expel | ❌ eligibility-by-stat — refused by name (`§A.2`; `rosters.yaml:131-142`, *"`capability` IS NOT AND MUST NEVER BE A MEMBER"*). ✅ menaces = the erosion list | claims held as eligibility (form 6 `own_ledger`) — act on what you hold, never on a number | — |
| **Tyranny** | **verdicts every faction receives differently**; the Edicts — rulings authored before the game that shape the map | ✅ per-witness deposit (`07:222-228`); an Edict is `T-n`'s opener declaring terms | present; *the same finding is a different fact in each ledger* is the `AX-2` dividend already banked | 0 |
| **Wildermyth** | characters **transformed** by events; scars persist | ✅ `Person.marks` (`shape.py:2365`); a determination may write one | present at the carrier level | 0 |

## 2.4 · What the survey says as a whole — three verdicts

1. **The design already IS four of the acclaimed games — at the season scale.** Diplomacy, Pentiment,
   Blood on the Clocktower, Citizen Sleeper. None needed converting; they are what `AX-2` + the scene
   budget + per-witness deposit produce. **The proposal under-claims them** — `11:99` grades E's
   legibility half *"weaker by a lot"* without noticing that the four best-loved games in the survey
   have exactly that legibility profile.
2. **Inside the room, the design is none of them.** Every precedent that made the *exchange itself*
   playable — Duel of Wits, Dogs, Apocalypse World, Ace Attorney, Blades — has a gradient on the middle
   outcome, a graded cost of failure, a concession that is a move, and an error priced rather than
   refused. The proposal has a full ladder on effect and a binary on everything else.
3. **Every mechanism that does not survive is one shape: a shared visible track** — BoA, the Dogs pile,
   Rome's vote count, Sidereal's open table. `T-a` refuses each as a field, and the cousin is always
   the same — *a Query over live edges, read by a later act* — which is `05:94-98`'s own quorum shape,
   known and not built.

---

# PART 3 · OPTIONS AND CONSTRAINTS — what an agonist needs and cannot get without a guardrail pass

Not positions. **3.1** is the census with a yes/no an author cannot give; **3.2** is the surface of
levers the architecture already has and nobody has pulled; **3.3** is the walls, each with the axiom
that builds it; **3.4** is the named impossibilities.

## 3.1 · The binary census — is a gradient expressible in the LIVE schema?

*"Live schema"* means `shape.py` at commit `1b1e382` plus the rosters and verb table as they stand —
not the proposal's prose. The last column is a verdict on expressibility, not a recommendation.

| # | binary | file:line | current values | gradient expressible NOW? | with what, and the cost |
|---|---|---|---|---|---|
| **B-1** | aptness | `04:138-139, 157` | apt / refused (`requires` fails) | ✅ **YES** | Ob composition is ruled (`06:210-225`); the rung roster is ordered (`03:228-229`) so *distance* is an ordinal; genre is a set. A demotion emits an existing kind with roster content (Fig. 26's four readings, `03:168-173`, are content already). **Cost: one injected Ob term, one data roster of readings.** The `requires` conjunct on genre is *removed* |
| **B-2** | licence veto | `08:42`; `03:166-173` | `bool` | ✅ **YES** | four conjuncts → four Ob terms; the structural demotion is `BandExtension.may_overwhelm` (`dice_engine.py:109-111`), which the seam's bool duplicates. **Cost: up to four injected terms, one declared `BandExtension` subclass; the seam's `veto:bool` is deleted** |
| **B-3** | registers | `03:380` | `[restricted]` / `[all seven]` | ✅ **YES — by deletion** | `register fit` is already the fourth Ob term (`06:220`); the set is a second home (`ID-2`) for it, and the roster does not exist in data. **Cost: −1 key** |
| **B-4** | proofs | `03:381, 558` | `[...]` / `[]` | ✅ **YES** | the fifth Ob term (`06:221`) can weigh a proof *against the Proposition it addresses*; `Claim.subject` (`shape.py:2151`) and `Proposition.id` exist; HOLDS sub-matters inside an OUGHT matter are already the design's own reading (`14:113-119`). **Cost: −1 key, one weight family (injected).** ⚠ `P-24`: a claim about a future state has no producer — the HOLDS sub-matter must be *uttered* by someone |
| **B-5** | presence | `07:50-55` | there / advocate / absent | ⚠ **PARTLY** | four degrees compose from rostered verbs (`move`; `commit`+`oblige`; `create_record`+`carry`+`tell`; a debtor's `tell` at `told_by`). The Ob's `reception` must read *who is speaking*. **The advocate's licence to concede has a carrier — `Tenure.payload` (`shape.py:2087`, unread) — but attribution of a descent inside the run rests on `Event.subject`, which `T-d` says should not carry the actor and `W24` intends to remove** (§0 note 4). The cause of absence (`P-33`) needs `evade / defy` on a summons with a return day — `P-04` |
| **B-6** | disposal | `03:364` | bench / mutual / none | ⚠ **PARTLY** | *bench* and *mutual* are the two shapes `AX-1` permits (a seat disposes; both parties commit). *None* is a degenerate case (`14:263-282`). **A multilateral disposal is NOT expressible** — a tally is `T-a`; the lawful shape is a later act reading a Query (`05:94-98`), which is a *different* game (someone declares) rather than a gradient of this one |
| **B-7** | finality | `03:373, 479` | `appeal_basis: <remit> \| none` | ✅ **YES** | `Tenure.degree` on the finding is written (`determine`, `verb_table.yaml`) and unread; the appeal's `max_depth` is a term the opener declares (`00:246-253`). Finality can be a function of degree and of the declared cap. **Cost: 0 — a reader for a dead field; the key becomes derivable** |
| **B-8** | reasons | `03:387` | given / withheld | ✅ **YES** | reasons are claims bench members hold; `interview` a bench member (`04:339-350`) is a live act; the key can be a floor on what may be `tell`-ed, not a switch. **Requires `P-05`** for the interview to return anything |
| **B-9** | term | `03:372` | `true / false` | ❌ **NOT NOW** | `Tenure` has no `term` (`shape.py:2067-2091`); `P-04`. Once built, the gradient is *who is the closer and can they be reached*, which is `T-c`'s handles |
| **B-10** | order | `03:378` | five enum values | ⚠ **PARTLY** | `Record.stages: list[tuple]` (`shape.py:2422`) is written by `open_case` and read by nothing — it can carry the order as a *document*. ⚠ **But `08:88-91` amends the seam so the provider orders sub-steps only *"from a value it read in the arrangement row … not from the world"*** — a Record is world. **One of the two must move; that is a ruling, not an edit** |
| **B-11** | Failure's cost | `04:72` | one write | ✅ **YES** | the ladder tuple carries `track` per rung (`03:228-229`) and it is unread (`13:55`); the run's rung is a fold (`00:298-302`). The write at Failure can be derived from the rung's track. **Cost: 0 fields; the loader's `writes_at(degree)` must be able to see the run's rung — a fold read, not a column.** ⚠ Whose `Person.stance` is written must be settled first (the actor's, or the row breaches `AX-4`) |
| **B-12** | read confidence | `04:344-345` | `[]` at every band | ✅ **YES** | `Claim.confidence: int` (`shape.py:2157`) exists on the deposited claim; deposit mode `actor` (`rosters.yaml:305-345`, `H-122`) is the forced mode. Confidence from the actor's conduct pool and value from the draw makes *confidence ≠ accuracy* mechanical. **Requires `P-05`.** Cost: 0 |
| **B-13** | Partial | `04:71` | `[]` | ✅ **YES** | `matter.advanced` exists; a `partials so far in this run` fold is the same construction as `proofs told so far` (`06:221`). **Cost: one injected term** |
| **B-14** | the ladder | `00:298-302` | self-descent only | ✅ **YES** | an opponent's `matter.carried` names a rung; the fold already reads *"the lowest rung any emitted `matter.*` Event … has named"* — a carried rung is in that set. Whether it becomes the loser's *floor* is a rule over the same fold. **Cost: 0**. ⚠ needs `B-1` priced, or the loser's next speech at that rung is refused rather than expensive |
| **B-15** | stakes_grade | `03:388` | three values | ✅ **YES — by deletion** | the proposal's own `P-09`; derivable from `disposes` + the rung's track. **Cost: −1 key** |
| **B-16** | silence when called | `07:74`; `04:149-151` | not an act | ✅ **YES** | `withhold` is on the proposal's own speech roster (starred); emitting `matter.held` (an existing kind) under `order: rank/scripted` and nothing under `free` is one data row. **Cost: one speech kind in data; 0 Event kinds** |
| **B-17** | the floor is first-come | `00:327` | refused by the fold | ⚠ **PARTLY** | inside the run the order is the arrangement's (`08:83-95`), so first-come is already not the rule *inside* a proceeding; `T-g` governs the season fold. Nothing to convert unless `B-10` moves |
| **B-18** | making someone a party | `03:312-320` | their own `commit` only | ❌ **NOT NOW** | the only lever is what one puts in their ledger, and `14:182-186` measures the ledger→decision edge as severed (`H-72`). Expressible after `H-72`; **not before** |
| **B-19** | the creditor | `04:451-452` | no verb | ❌ **NOT AS A VERB** | `T-m` makes closure the subject's; a creditor act on another's Tenure is a non-owner write (`AX-4`; `HANDOFF_NEXT.md` 1a plans the gate). **What IS expressible:** `tell` that the debt exists (publicity), and a counter-`oblige` by the creditor (mercy). `13:65` (`P-36`) grades whether forgiveness *should* be expressible as a ruling |
| **B-20** | the concession's price | `07:115-118`; `03:424-435` | free (closed floor) / costly (open) | ✅ **YES** | the price is the witness set, computed at WITNESS from presence (`rosters.yaml:104-110`, five channels). `floor` is a key on *admission*, not on *who came* (`03:284-290`). The gradient is *how many, and who, and through which channel* — already computed. **What collapses it is the row setting `floor: closed` on the terminal games**; that is a data choice, not a schema limit. Cost: 0 |

**Census verdict.** Of twenty binaries, **thirteen are gradient-expressible in the live schema at zero
or negative schema cost** (four by deleting a key; four by reading an unread field; five by an injected
Ob term or a data row). **Four are partial** and each names the exact wall (`T-d`/`W24`, the seam
amendment's letter, `T-a` for multilateral, the season fold). **Three are not expressible now** — two
on `H-72` (`B-18`; and `B-8`/`B-12` on `P-05`, its write side) and one on `P-04` (`B-9`) — and **one is
not expressible as a verb at all** (`B-19`), by theorem.

## 3.2 · The opportunity surface — levers that exist and nobody has pulled

For *creating and then seizing openings with other characters or the venue format*. Each row is an
available lever, its carrier or verb at `file:line`, what it could hold or do, and its status. This is
inventory, not design.

### 3.2.1 · Carriers that could HOLD an opening

| carrier | where | what it could hold | who reads it today | status |
|---|---|---|---|---|
| **`Claim`** — private by construction | `shape.py:2148-2158`; `rosters.yaml` `claim_sources` | **every secret.** *"Lives in the HOLDER'S OWN ledger… Nobody else may read or write it."* A fact you hold about someone that they do not know you hold is the default state of every claim | `belief_contradicts` (severed, `H-72`); `standing_of` | the CK3 *secret*, for free. Its `visibility: str` field is unrostered |
| **`Claim.confidence`** | `shape.py:2157` | how sure the holder is — set by *nothing* on an `interview` deposit | `LedgerReader` resolves on `(when, confidence)`; eviction ranks on it | an unread gradient on every read; blocked on `P-05` for interview |
| **`Claim.source = told_by`** | `rosters.yaml` `claim_sources` | *who told you* — a claim planted by another person carries its planter | `explain` (specified, absent) | the briefing's receipt; a false read traceable to its source *by the holder alone* |
| **`oblige`** (Tenure kind) | `rosters.yaml:84-87`; `verb_table.yaml` `oblige` (`requires: "—"`, `eligibility: own`, `writes: Tenure.since`) | **the hook / the promise / the surety.** Subject = who owes, object = who is owed | `release` (the debtor's) | the persistent-opportunity carrier; **no creditor verb** (`B-19`) |
| **`Tenure.payload`** | `shape.py:2087` | the *terms* of an oblige or commit — what it is for, at which rung an advocate may concede, by when | **nothing** (`00:288`, objection 5 — *"equally unread"*) | a free field on every edge, waiting for a reader |
| **`Tenure.degree`** | `shape.py:2086`; written by `determine` | the *band* at which a finding was reached — the compromise scale | **nothing** (`F.4`) | `ID-13` is about to delete it; a reader saves it |
| **`Tenure.term`** | — | a wound clock with a `closer` — the scheme's progress, the summons' return day, the stay's length | — | **absent** (`P-04`); `T-n` specified, unbuilt |
| **`Record.stages`** | `shape.py:2422`; written by `open_case` | **the venue format as a document** — order, term, floor basis, `max_depth`, declared by the opener under `T-n`; carried (`carry`), forged (`forge`), burned (`destroy_record`) | **nothing** | see `B-10`'s wall (`08:88-91`) |
| **`Proposition`** (frozen) | `shape.py:2425-2435`; `utter` | **a commitment that cannot be edited** — every rejected offer, every denial, stays authored and dated (`14:80-91`: *"what he offered in the spring is a fact somebody can produce later"*) | `commit`'s `requires` (form 1) | the Ace Attorney *statement*; the BotC *public claim* |
| **`knot`** (Tenure kind) + `witness_key` channel | `rosters.yaml:84-87`; `shape.py:4361-4364` | a person tied by a live `knot` to the event's subject **hears what happens to them** — a standing information line to a person, across seasons | WITNESS | an unused *intelligence* carrier: knot the clerk and you learn when the record changes |
| **`Date` / `DocketItem`** | `shape.py:5363-5381` (CALENDAR); `convene` | the occasion itself — a date set the season before, firing whether or not anyone comes; a vacant date is already a mechanism | CALENDAR | the season-scale opening: convene, and see who travels |
| **`Person.marks`** | `shape.py:2365` | a scar a determination leaves — *heritage · grade · Church standing · office · residence* per `person_predicates` | `standing` pairs claims by predicate | the Wildermyth/Tyranny carrier |
| **the σ-channel** | `sigma_leverage.py:97-102, 224-234, 190-203` | a **named level of bought advantage** — minor/moderate/strong/major, uniform at every pool, boosting the roll and never touching Ob | `p_success`, `net_boost`; **no caller in this design** (`06:271`) | the devil's-bargain carrier: an edge *paid for* with a Tenure opened now |
| **`BandExtension`** | `dice_engine.py:95-138` | the one structural demotion a subsystem may declare — and the licence veto's lawful home | `degree_from_net` | the seam's `veto:bool` (`08:42`) is its duplicate |
| **the intra-run fold** | `00:298-302` (rung); `06:221` (proofs told so far) | **any per-run gradient** — a value derived from *this run's own emissions*, owned by nobody, dying with the run. The design uses it twice; the pattern generalises to *partials so far*, *rungs carried against X*, *conjuncts failed so far* | the provider | the lawful home for every intra-proceeding state that must not be a field. ⚠ attribution inside it rests on `Event.subject` (§0 note 4) |

### 3.2.2 · Verbs that could CREATE an opening (all live rows; none invented)

| verb | row | what it creates, in another person or the venue | when | status |
|---|---|---|---|---|
| **`tell`** | `requires: own_ledger` (form 6); deposits at WITNESS | a claim in *their* ledger, `told_by` you, at your confidence — **the briefing; the planted read; the public debt** (tell the room an `oblige` exists) | the season before, or in the room | live; the *effect* on their choice is blocked (`H-72`) |
| **`interview`** | `04:339-350`; `contests: "a disposition"` | **their `SAID` row** — and *they learn what you are asking* (the cost is itself a move: *asking about the bribe tells them you suspect the bribe*, `15:87`) | the season before, or in the room at the price of a turn | row exists; returns nothing usable (`P-05`) |
| **`utter`** | `writes: Proposition.exists` | **an immutable statement** — a terms-offer, a denial, an accusation — that others must commit to or refuse, and that can later be produced against its author | any time | live |
| **`commit`** to *another's* disposition | `requires: the Proposition exists` | **you become their advocate; they become a party** by your act plus their `oblige` — the one second-person route into the room the roster has, and it runs through *your* edge | before the day | live |
| **`oblige`** (yourself) | `requires: "—"` | **a promise** their scoring can read; **a counter-promise** that is mercy (`B-19`'s lawful forgiveness); **the price of a σ-level** (the bargain) | any time | live; the read side is `H-72` |
| **`petition`** | `requires: "—"`; *"no dedup, no cap"* | **a demand the seat must docket** — the route to a summons, an adjournment, a change of floor: petition the presiding seat | the season before | live; what a petition *obliges* the seat to do is unstated |
| **`issue` → `comply` / `evade / defy`** | `issue` writes `Dispensation.exists`; `comply`/`evade` require a claim of the terms in one's own ledger | **a summons, a writ, an exclusion from the floor** — and the summoned person's *refusal on the record* (`evade / defy`), which is `13:61`'s missing key for the cause of absence | a season | live; the operand (Dispensation) is outside the closed `requires` roster (`04:206`), so the fold refuses today |
| **`convene`** | corrected to an ordinal floor | **the occasion** — set a date, at a venue whose ordinal fixes who can realistically travel (`03:291-294`) | a season | live |
| **`open_case`** | `requires: "the act DECLARES the stages and their terms"`; writes `Record.stages` | **the venue format** — order, term, floor basis, cap — as a document the opener authored | a season | live; `Record.stages` unread |
| **`create_record` / `carry` / `forge` / `destroy_record`** | live | **a letter** (a Record whose `subject_matter` is your Proposition, borne by another); **a forged docket**; **a burned term** | a season | live |
| **`move`** — and *not* `move` | `requires: a contain path` | presence, and the free terminal choice not to be there | the day | live |
| **`repudiate`** / **`release`** | `requires: a live commit / Tenure whose subject is the actor` | **the stab; the forswearing** — each witnessed, each remembered | any time | live |

### 3.2.3 · `§F.24a` forms — which could let an act's `requires` name something SOMEBODY ELSE did

The seven-form grammar (as the proposal cites it, `03:186-198`; `04:193-194, 330, 354, 367`): 1
existence over an edge kind · 2 a computed scalar against a threshold · 3 a containment path · 4
cardinality · 5 a relation between actor and subject **over prior acts** · 6 own-ledger · 7 a basis
lookup. The closed operand roster is `(actor, subject, from, to, site, kind, amount, floor)` (`04:206`).

| form | what it can already say about another's act | example the proposal itself gives | limit |
|---|---|---|---|
| **1 — existence** | *a `commit` edge by the subject exists* — i.e. they have taken a position (a party exists; a Proposition has been committed to) | `commit`'s own cell; `private` = no third party `contain`ed at the venue (`03:192`) | can name the *subject's* edges only — the operand roster has no *third person* |
| **4 — cardinality** | *no prior live charge by this actor on this subject* — repetition (Fig. 26 conjunct 3) | `03:193` | counts the actor's own acts, or edges on the subject |
| **5 — relation over prior acts** | ⭐ *goodwill demonstrated first, in acts the hearer can point to*; *the actor holds no stake the disposal would move* | `03:191, 194` | **this is the form that lets a `requires` (or an Ob term) read what the OTHER person did before** — it is the only form that quantifies over prior acts between two named operands. It is the form a *"they committed at conjecture, so my proof is now apt"* term would use |
| **6 — own ledger** | *I hold a claim about the subject* — including one they `tell`-ed me, `told_by` them | `tell`, `reconstruct` | reads only the actor's own ledger, which is correct (`AX-2`) and is *how* another person's act reaches you: through what you were told |
| **7 — basis** | *my seat's basis reaches the subject* | `determine` | a seat's remit, not another's act |
| **2, 3** | a scalar; a path | `convene`'s ordinal; `move` | not about acts |

**Verdict for the agonist.** Form 5 is the lever. It already carries two of Fig. 26's four conjuncts,
and a term composed from *"the subject committed to Proposition X in this run"* is the same form over
the run's own emissions. **What the roster cannot say:** anything about a third person who is neither
actor nor subject — *"my ally has told the bench"* is not expressible as a `requires`; it reaches the
actor only as a claim (form 6), which is the correct epistemic shape and the reason `H-72` is
load-bearing.

### 3.2.4 · What the venue's own order and procedural rung already give for free

| lever | where | what it gives without a new rule |
|---|---|---|
| **the procedural rung** | `00:162-164`; `03:234` | *"is this bench competent"* — the cheapest win, spent early or not at all, *"signals evasion"*. **A point of order is already a rung** — the top one — and a speech there is a move on the venue rather than the matter |
| **`order`** — position as a public ruling | `05:18`; `04:483-489` | under `rank`, *when* you are called is your seat's ordinal — *"precedence is a public ruling delivered without a word"*. Speaking first carries the framing and *"opens into a house that has not settled"* (`07:154`); speaking later answers. **Position in order is already a datum every speech has**; it composes into nothing today |
| **the opener's terms** (`T-n`) | `00:215-221`; `03:479-481` | *who arbitrates, how many appeals, by when* are terms of the opening act — **"a game before the game"** the proposal names and does not play. The opener is a person; the terms are on a Record; both can be reached the season before |
| **the season interval** | `04:237-254` (`P-14`) | hearing and judgment cannot share a season — *"a whole season in which people can act: flee, bribe the bench, produce a document, reach the man who must renew the term, or die"*. **This is the largest opening in the design and it is unmarked as one** |
| **the vacant date** | `shape.py:5363-5381`; `07:332` | a convened proceeding nobody attends lapses; *not determining is not acting*. Absence is a move for a bench member as much as for a subject |
| **the serial fold** | `03:349` | *"the order is real because the fold is serial"* — each act resolves against the world its predecessors left. Inside the run, **what was said before you is in the log** and the fold can read it; the register-as-position question (`P-16`) is this lever unresolved |
| **the depth cap as a declared term** | `00:238-253` | *"the exhaustion of appeals is a game mechanic, not an engine limit"* — the cap is contestable because somebody declared it |
| **`floor: admitted:<basis>`** | `03:366` | admission is a *basis* — a Query over edges — so **who may be present is already something an act could change** by changing an edge the basis reads (confer a seat; sever a commit). No mid-run change is lawful; the season-before change is |
| **the presence cache and the five channels** | `rosters.yaml:104-110` | *how many saw the concession and through which channel* — the concession's actual price — is computed at every act. `B-20`'s collapse is the row's, not the loop's |

### 3.2.5 · Blocked levers — say it once

Every lever whose payoff is *another character choosing differently* — the briefing, the provoked
reply, the debtor who behaves because the creditor is in the room, the ally who speaks because they
were told — is **blocked on `H-72` / `H-116` / `F.24`** (`14:182-198`: belief → decision severed; 0
of 4,800 claims can fire). Every lever whose payoff is *an investigation the player can use* is
blocked on **`P-05`** (its write side, `H-122`). Every lever with a *clock* — the scheme, the summons'
return day, the adjournment — is blocked on **`P-04`**. The levers that are **not** blocked are the
ones inside the Ob composition, the ladder, the run fold, and the four unread fields — which is why
§4.3 names those first.

## 3.3 · The refusals — what a conversion MAY NOT do, and the axiom or theorem that forbids it

An agonist under pressure will reach for a track, a meter, or a table. Each row is the wall and its
builder.

| # | forbidden | forbidden by | the shape it takes when it sneaks in |
|---|---|---|---|
| **R-1** | **a shared visible track** — a Body of Argument, a debate score, a momentum bar, a dice pile, a vote count | `T-a` (from `AX-4`): an aggregate over many owners cannot be a field; `09` row 9 | *"a `Proceeding.progress` field"*; *"the matter's heat"*; a quorum stored as a count (`05:88-92`) |
| **R-2** | **a bias, disposition or reception meter anyone can read** | `AX-2`; `06:22-33`; `09` row 10 (*"absence is the weaker guard"*) | `Person.bias`; `bench.leaning`; a displayed *"the room is hostile"* |
| **R-3** | **a GM, narrator, or engine that decides** — a phase timer, a round cap, "debate is over after N turns", a proceeding that advances because time passed | `AX-1`; `AX-5`/`T-c` (a fourth clock); `05:67-70` (*"THERE IS NO TURN LIMIT AND THERE MUST NOT BE"*) | *"the hearing concludes automatically"*; *"the world escalates the matter"* |
| **R-4** | **a view of the room inside a decision** — any Query taking `World` reachable from `choose`; `explain` with a `World` | `T-f` (from `AX-2`); `P-30`; `07:184-188` | a `reception` helper that drifts person-side; a UI reading `eff_ob` |
| **R-5** | **advantage as an Ob reduction**; **Ob below 1** | F1 / ED-884; canon P-232 (*"no modifier may reduce Ob below 1"*); SKILL §11.2 | `Eff_Ob = base_Ob − eff_σ·σ_N`; resolving on `eff_ob()` (display only, `sigma_leverage.py:169-177`) |
| **R-6** | **a flat bonus to the roll** not σ-scaled | SKILL §11.2 (*"Δz = X/(0.8·√pool) ∝ 1/√pool — the exact non-uniformity this engine exists to kill"*) | `+2 dice for a good argument`. Advantage enters through `levels_to_net_sigma` → `net_boost` or it is a defect |
| **R-7** | **a second ladder, a fifth band, a moved band edge, a widened outcome** | `T-k`; Jordan 2026-08-15 (*"systems should not need different degree bands"*); `BandExtension` can only demote 3→2 (`dice_engine.py:89-94`); `08:42` (*"the ladder takes the minimum"*) | *"a `Turned` band"* (the draft did this, `04:82-89`); an extension that promotes; a subsystem-local `degree()` |
| **R-8** | **a per-pair rule table** — speech kind × game, register × register, volley × volley | `§0.06`'s emergence rule (*"the rule count must not grow with the pair count"*); `04:165` | Duel of Wits' 7×7; *"refute vs amplify"* lookup; 12 kinds × 12 games |
| **R-9** | **eligibility by stat** — a capacity, a standing, a skill gating an option | `§A.2` (*"`if skill < N: return []` … deletes the best thing about the option set"*); `rosters.yaml:131-142` (`capability` is never an eligibility kind, and the loader raises) | *"only a speaker of standing ≥ X may address the bench"*; Fallen London's storylet locks |
| **R-10** | **a non-owner write of a Tenure** — a creditor closing a debtor's `oblige`; an advocate's act binding the principal directly; a descent written onto the opener's edge | `AX-4`; `T-m`; `00:285` (objection 2); `HANDOFF_NEXT.md` 1a (the `subject == actor` gate) | `call_in(hook)`; *"the advocate's concession writes the principal's commit"*. The principal is bound only by an edge the principal opened |
| **R-11** | **an arrangement that declares a cast** — a row saying who is present, who is a party, who attends | `AX-1`; `03:284-290`; `14:290` | `cast: [...]`; `subject_absent: true`; a `catchment` |
| **R-12** | **a disposal that writes only a Query** — standing, reputation, "how they feel" | `14:288-289` (the *about-the-world* ruling); `T-a` | `disposes: standing` (the draft did this) |
| **R-13** | **an `Event` carrying a target or (by design) an actor** — *"call a witness"* as delivery; a summons that arrives | `T-d`, `T-e` (from `AX-2`, `AX-1`) | *"the summons is delivered to X"*. Delivery is WITNESS from presence; a writ reaches the summoned by their own channel |
| **R-14** | **an order of sub-steps from anything but declared data** | `08:88-91` (the seam amendment: *"not from the world, not from a capability, not from a default in a body"*); `P-18` | *"the loudest speaks first"*; an order from a capability. ⚠ **and, as written, an order read from a `Record`** — the live tension `B-10` names |
| **R-15** | **a mutated Proposition** — amended terms, a revised offer | `shape.py:2425` (`frozen=True`); `14:77-91` | *"edit the treaty"*. Terms are re-uttered; the old ones stay in the log |
| **R-16** | **evidence moving a conviction; WITNESS touching a belief** | `AX-3`; `T-j`; `09` row 11 | a `determine` whose `requires` reads the actor's ledger to move `convictions`; a guilt scalar both tracks push on (`00:188-194`) |
| **R-17** | **a `requires` operand outside `(actor, subject, from, to, site, kind, amount, floor)`** | `04:206` (*"a cell naming an operand outside this roster REFUSES AT LOAD"*) | `{of: via}`, `{of: creditor}`, `{of: ally}` — a third person cannot be named; they reach you as a claim |
| **R-18** | **a number the player can optimise against** — the obstacle, the margin, a band preview, a percentage | `15:140-147` (PART E); `07:174-181` | any UI summing the Ob terms. ⚠ **Named levels of the player's OWN advantage are permitted** (SKILL §11.5 P-i; `07:176-178`) — legible hand, illegible room |
| **R-19** | **a magnitude sourced to the study** | `01:334-353` (*"quote a probability as sourced"* / *"draw a decision tree with likelihoods"*); `CLAUDE.md` §0.1 pt 4 | every Ob term's size, every level's weight: **inject, declare, sweep three points** (`ID-6`) |
| **R-20** | **a new verb, carrier, field, edge kind or Event kind that does not make something UNNECESSARY** | `00:321-334`; `03_VERBS_AND_LOOPS.md` §F.1; `README.md`'s count | `elicit`, `charge` (both committed and retracted in this directory); `Proceeding`; `Verdict`; `role` |
| **R-21** | **a guard, a document, or a ledger row as the output of an adversarial pass** | `CLAUDE.md` §0 (AMENDED 2026-08-19); SKILL §12 | this note is the exception the coordinator asked for; it produces no row |

## 3.4 · Named impossibilities — mechanisms with NO architecture-compatible cousin, and what each would cost

A strained adaptation is worse than a named wall. These are the precedent mechanisms that do not
survive *and* whose cousin is a different mechanism rather than the same one in lawful dress.

| mechanism | why there is no cousin | what it would cost to have it |
|---|---|---|
| **CK3's hook, spent by its holder** | the carrier exists (`oblige`), the secret exists (`Claim`), but **the holder-side act is a non-owner write** (`T-m`, `AX-4`, `R-10`). *Publicity* and a *counter-promise* are a different, slower, political game — not a button | **one new verb** (`call`, eligibility over another's Tenure) — which `T-m` refuses by construction, so it costs an amendment to a theorem, not a row. `13:65` (`P-36`) grades *whether forgiveness should be expressible* as a genuine ruling; calling a debt is the same ruling from the other end |
| **Sidereal Confluence's multilateral binding deal** | `disposal: mutual` is two-party (`14:92-95`); a five-party settlement is a tally (`T-a`, `R-1`). *A later act declares it carried* is Republic of Rome's mechanism, in which one person decides — not a multilateral one | **either** break `T-a` for one case (a stored n-party commitment set — which is what a treaty roster would be, and `T-h` says a faction is exactly a Proposition plus `commit` edges, so *the carrier may already exist as a faction*: a treaty is a faction everyone joined). ⚠ That is a reading worth an agonist's attention and not a cousin this pass can certify |
| **Republic of Rome's counted vote** | a tally across holders (`R-1`). The cousin — a Query read by a later act — changes *who decides* (one declarer) and therefore is a different game | a `records_dissent`-style key cannot buy it. **It costs `T-a`**, and `05:88-103` says so |
| **Microscope / Follow — shared authorship** | no person in the fiction acts (`AX-1`); the author has privileged access (`AX-2`) | a different game (`G.1.2`: *"break an axiom and you have chosen a different game"*) |
| **Disco Elysium's percentage** | the Ob includes hidden interiors that move; a shown number is stale or a leak (`AX-2`, `R-18`) | `AX-2` for the player only — which `07:166-169` refuses because the player *controls a person*, so the leak is the character's |
| **Blades' stress meter; Suzerain's political capital; Fallen London's qualities** | a per-person scalar spent to buy outcomes is a field with two readers (the holder and the resolver) and it gates eligibility (`R-9`) | `Sensation.standing` is the computed cousin of *capital*; *stress* has none — a conviction-misalignment Ob term prices the act but does not accumulate |
| **Reign/ORE's width** | one draw, one number (`continuous_engine_sample`) | a second draw per interaction — `P-v` (bespoke draw) and `06:308-326`'s *"exactly one thing is stochastic"* |
| **Pax Pamir's dominance check** | a world-initiated periodic event is a fourth clock (`AX-5`) | a `Date` somebody sets — which is then not the world checking, it is a person convening. That is a cousin, listed here because the *feel* (the world decides) is the part that does not survive |
| **Duel of Wits' scripted volley table; Dogs' dice pile** | per-pair table (`R-8`); shared track (`R-1`) | the compromise rule and the give-move survive; the tables do not, and nothing replaces them — the *rhythm* of a scripted volley (three actions declared blind, then revealed) is Diplomacy's simultaneity, which the nested run does not have (`04:480`: *"nobody reacts to a same-season act"* is the season rule; inside the run the order is serial) |

---

# PART 4 · THE TWO AUDIT VERDICTS, THE THREE LEVERS, AND WHAT IS LEAST SURE

## 4.1 · The single most important binary — `B-1`, apt or refused

It is the proposal's own headline mechanism for weighting speech (*"by APTNESS not coefficients"*,
`04:131`). It fires **before the draw**, so no gradient downstream can reach it. It teaches nothing —
a refused Candidate emits `speech.unheard` and costs a turn. It forbids the study's own best example:
the design says Demosthenes *"wins by refusing the forensic frame"* (`03:133`) and then writes a row
under which his move does not form. And the proposal has **already written the argument against it,
about licence** — `03:159-161`, *"a refusal would delete the study's point … priced as an attack"* —
and did not apply it one file over. The three grounds given for refusal (`04:161-168`) each fail on
the proposal's own text: *weights grow with the pair count* — a distance on an ordered roster is one
rule; *the study forbids the numbers* — `ID-6` injects and sweeps, as the design does for its other
five terms; *a refusal emits and a weight does not* — a demotion emits too, which is exactly what
`03:175-179` says of Fig. 26. Every other binary in §1.1 is one the design *asserts*; `B-1` is one the
design *defends*, which is why it is first. **The line the agonist must hold:** `requires` answers
whether the act can be *formed* (is there an occasion); aptness answers how the room *takes* it. The
first is a refusal; the second is reception, which the design already says is an Ob term.

## 4.2 · The precedent mechanism that transfers best — Duel of Wits' compromise scaled to what the winner lost

Three reasons no other survivor shares. **(a)** Its carrier already exists in the tree with a writer
and no reader — `Tenure.degree`, written by `determine` (`verb_table.yaml`), graded *"a writer and no
reader"* (`F.4`), and about to be deleted under `ID-13`. Adoption is reading a field, not adding one.
`00:275-319` withdrew the design's claim to read it *for the rung*, on five grounds; none of the five
touches reading it for what `determine` already writes there. **(b)** It converts two binaries with
one reading — `B-7` (finality) and `B-14` (the one-way ladder) — because a finding at Success and one
at Overwhelming can lawfully leave the loser's `commit` in different states, and the appeal's cap is a
declared term. **(c)** Its whole reputation is its anti-binary property: a narrow win that must give
much back is *the* reason the mechanism is loved, so the design's E-legibility risk (`11:99`) is
answered by a game people already play for exactly this. Apocalypse World's 7–9 is its sibling and
transfers second — the middle band as the rich one — and its carrier is the intra-run fold the design
already uses twice. Neither adoption is designed here.

## 4.3 · The three levers an agonist should reach for first, and why

Chosen by *changes play* × *not blocked on another lane* — which rules out everything in §3.2.5.

1. **The Ob composition, for aptness and licence** (`B-1`, `B-2`). The ruling is in hand (2026-09-06:
   *"I'm fine with Ob being modified by things"*); the rung roster is ordered; Fig. 26's four readings
   are content; the structural demotion already exists as `BandExtension`. It lands at build steps 0
   and 6. It is the lever that turns the primary binary into a price, and it costs the count nothing
   but injected magnitudes and a data roster. ⚠ The wall to watch is `R-18` — every term added is a
   place a port could leak — and `15` PART F's *"not free to compute"* depends on the `reception` term
   keeping the sum non-stationary.
2. **The intra-run fold, for Partial and for position** (`B-13`, `B-11`, `B-14`). *"Proofs told so far in
   this run"* (`06:221`) and `rung(run)` (`00:298-302`) are the two existing instances; *partials so far*,
   *rungs carried against X*, and *the rung's `track`* (unread, `13:55`) are three more of the same
   construction. Owned by nobody, stored nowhere, dying with the run — the one place intra-proceeding
   state may live under `T-a`. ⚠ The wall is attribution: today `Event.subject` is the actor (§0 note
   4), which lets the fold say *whose*; `W24` intends to remove that. A lever standing on a defect
   should say so.
3. **The four unread fields** — `Tenure.degree` (`B-7`, the compromise), `Tenure.payload` (`B-5`, the
   advocate's licence; the hook's terms), `Claim.confidence` (`B-12`, the read's feel), `Record.stages`
   (`B-10`, the venue as a document). Each is an `ID-13` closure at zero schema cost. ⚠ Two walls:
   `Record.stages` as the order collides with the seam amendment's letter (`R-14`) and needs a ruling;
   `Claim.confidence` on an interview deposit needs `P-05`'s write side.

**What these three do not reach — stated so the agonist does not over-claim:** they make the room
*graded*; they do not make it *generative*. Every "create then seize" lever with another character in
it waits on `H-72`. The honest first act toward §3(b) is closing that edge, and it is not this
subsystem's lane.

## 4.4 · The mechanism most wanted and not adoptable — CK3's hook, spent by its holder

The carrier, the secret and the clock are all present or registered; the holder's *act* is a
non-owner write and `T-m` refuses it by construction (§3.4 row 1). The lawful cousin — make
forswearing expensive by making it seen; forgive by binding yourself — is, on this pass's reading, the
better and more political game, and a player who has played CK3 will feel its absence as *"my hook
does nothing."* `13:65` (`P-36`) has already graded the forgiveness half as a genuine ruling; the
calling half is the same ruling from the creditor's side. Second: Sidereal Confluence's multilateral
binding deal, refused at `B-6` — with the one reading worth an agonist's time being that `T-h` makes a
treaty everyone joined *a faction*, which may be a carrier rather than a cousin.

## 4.5 · The count — what pulling every lever in §3.2 would do to the proposal's zero

| | proposal | if every unblocked lever were pulled | delta |
|---|---|---|---|
| new carriers · edge kinds · verb names · fields · Event kinds | 0 · 0 · 0 · 0 · 9 | 0 · 0 · 0 · 0 · 9 | **0** — every demotion, withhold or compromise emits an existing kind |
| arrangement keys | 14 | 10–11 | −3 to −4 (`registers`, `proofs`-as-set, `stakes_grade`; `appeal_basis` derivable) |
| speech kinds (data; no roster in data yet) | 12 | 12 (`withhold` un-starred) | 0 |
| **Ob terms** | 5 | **up to 12** | **+7, all `assumption`-grade, injected, swept — the real cost, and it is an audit surface (`R-18`), not a schema** |
| `BandExtension` subclasses | 0 (+ a `veto:bool` at the seam) | 1 | +1; the seam's bool is deleted |
| fields given a reader | — | 4 (`ID-13` closures) | +4 |
| seam signature | carries `veto: bool` | does not | shorter |

**Net: the schema shrinks, the data grows by one roster of readings, the Ob composition grows by seven
hidden terms, four dead fields get readers. New primitives: zero.** The agonist should treat the
twelve-term Ob as the thing to attack — not for its size but for whether a patient player with many
seasons of data can make it stationary.

## 4.6 · Where this pass is least sure — handed over so the antagonist need not find it

1. **`B-1`'s pricing routes category errors toward standing** — and `14:263-282` demoted the public
   debate for being about standing only. A priced inapt move may resurrect the degenerate game as
   the destination of every mistake. This pass has no clean answer.
2. **Attribution inside the run** (`B-5`, `B-14`, lever 2) rests on `Event.subject` carrying the actor,
   which is `T-d` violated in mechanism and scheduled for repair (`W24`). Whether the resolver may
   walk `causes[] → Act.actor` instead — `T-f` permits resolver-side reads; `07:188` forbids it for
   `explain` only — is a reading, not a ruling.
3. **`Record.stages` as the venue format** collides with `08:88-91`'s letter (`R-14`). The amendment's
   *purpose* (no order from a body or a default) is honoured by a `T-n`-declared Record; its *letter*
   is not. One of them must move and this pass cannot say which.
4. **The σ-channel for bought advantage** may re-open the 2026-09-06 ruling that put the five terms in
   Ob composition (`06:143-160`). This pass reads the ruling as scoped to *room* terms and silent on
   *bought* advantage; the antagonist may read it wider.
5. **Whose `Person.stance` `speak` writes** (`B-11`) is unstated. If the hearers', every band is a
   non-owner write and the row breaches `AX-4` as written; every lever above assumes the actor's.
6. **`T-h` as the multilateral carrier** (§3.4 row 2; §4.4) — *a treaty everyone joined is a faction* — is
   a reading this pass noticed late and did not test against `T-h`'s own retraction (`01_AXIOMS.md`,
   *"a memberless faction leaves territory held by a banner nobody carries"*). It may be a carrier or a
   second debt.
7. **All of §3.2.5.** If the antagonist holds that a lever which cannot fire is prose, the whole
   "create then seize" surface reduces to: *closed until belief reaches decision*, and the three
   levers of §4.3 make the room graded but not yet generative. That is this pass's honest residue.
