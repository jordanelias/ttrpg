# 18 · FINDINGS — the gameplay audit, the figure adjudication, and what they agree on

## Status: **PROPOSED (2026-09-06). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Inputs: three independent passes, none of which saw the others.
## `relay/E_FABLE_OPPORTUNITY_AUDIT.md` · `relay/F_FABLE_FIGURE_BANDS.md` · `relay/G_EMERGENCE_PRECEDENT.md`

---

> # THE VERDICT, FIRST
>
> **Not a game today, and the reason is four lines of code rather than anything in the design.**
>
> `reception` — the one hidden, load-bearing term the entire anti-solver argument rests on, *"composed
> from the hearers' own claims about the speaker"* — **reads a set the world cannot populate.**
>
> - A witnessed act that names a subject deposits **no claim naming the actor** (`shape.py:4203-4205`).
>   A hearer's ledger never records **who spoke**.
> - Every deposit is identical: `(predicate = event kind, value = True, source = firsthand,
>   confidence = 100)` (`shape.py:6336`).
> - `told_by` is rostered and **never minted** (`rosters.yaml:119` vs `shape.py:6327`). Hearsay does
>   not exist.
> - Default fan-out is **`total`** (`shape.py:1798`). Everyone knows everything, equally, instantly.
>
> **So `AX-2` hides nothing, because there is nothing to hide.** The arrangement is printed, the rung
> is public, the proofs are yours, and the one term that was supposed to make the sum uncomputable is
> **zero everywhere**. A player would sit down and take the flowchart's line.
>
> ⭐ **In the auditor's words: *the ledger cannot hold a reading of a person.*** Every mechanism in
> this document — the weight of a witness, pressing a fear, threatening a secret, the bench that
> remembers you folded — is a reader of that one missing row.

---

# PART A · WHAT RAN

| pass | model | what it was answerable for |
|---|---|---|
| **E · the opportunity audit** | `fable`, read-only | the game system and the twelve variants against Jordan's principles — degrees of success, fail forward, subversion, evidence and witnesses, playing the people, the character model, and emergent narrative |
| **F · the figure adjudication** | `fable`, read-only | success and failure for **each of the 27 figures**, derived from its own constraint set, into the four bands |
| **G · emergence precedent** | `sonnet` | what actually stores story in CK2/3, Dwarf Fortress, RimWorld, Nemesis, Caves of Qud, King of Dragon Pass, Pentiment — and the memory question specifically |

**Tiering per `CLAUDE.md` §10, and it was Jordan's call twice over:** `fable` is licensed for read-only
audit and planning, **never for authorship** — so both fable passes produce findings and this document
writes them up. The precedent survey is pattern recognition over public material, which is
sonnet-tier; running it at `fable` would have cost 5× for no judgment.

---

# PART B · ⭐ THE CONVERGENCE — three passes, one finding

**None of the three saw the others. They arrive at the same place from three directions, and that is
the strongest result this exercise produced.**

| pass | what it found |
|---|---|
| **the corpus** (F) | **Recurring shape #1, in 15 of 27 figures: *failure is the move read as a signal ABOUT THE MOVER.*** *"the presumption is itself the evidence against you"* · *"signals that you do not think the document sufficient"* · *"signals evasion"* · *"a concession not announced"* · *"a long defence reads as anxiety"* |
| **the precedent** (G) | **Ranked mechanism #1: typed, persistent relationship records — `(A,B) → {type, magnitude, source_event, expiry}` — never a scalar.** And **#2, called *"the single most load-bearing mechanism, and the one purely-cosmetic reputation systems miss"*: memory that gates ELIGIBILITY, not just flavour** |
| **the code** (E) | **That record cannot be written.** No deposit names an actor; every claim is firsthand at confidence 100; `told_by` is never minted; fan-out is total |

> ### **THE CORPUS SAYS THE OUTCOME OF A MOVE IS A READING ABOUT THE PERSON WHO MADE IT.**
> ### **THE PRECEDENT SAYS THE LOAD-BEARING MECHANISM IS A TYPED RECORD OF WHAT ONE PERSON HOLDS ABOUT ANOTHER.**
> ### **THE CODE CANNOT WRITE THAT RECORD.**
>
> That is the whole diagnosis. Everything below is either a consequence of it or a thing that becomes
> possible once it is fixed — and **the fix is three deposit rules and one field**, not a redesign.

**A second convergence, on the ladder's tuning.** The corpus's shape #2, in 13 figures: **overshoot,
not deficiency.** *"the perception is available and does not govern the action"* — elaborating past
the proof, answering more than asked, doing it twice, too fast, visible effort, invective where wit
would serve. **A Failure in this game is almost never *you did not see it*; it is *you saw it and
pressed*.** Which means Failure should sit **just past Success**, not far below it: the actor who
overshot was close. That is Jordan's fail-forward principle arriving from the source material rather
than from doctrine.

**A third, and it solves a problem the design had parked.** The corpus's shape #4, in 7 figures:
**terminal = being seen at it.** *"the DISCOVERED lie — not the lie"* · *"visible effort once seen"* ·
*"it need only be visible that you know"* · *"as legible as a plain statement"*. **Costly faults are
EFFECT faults; terminal faults are EXPOSURE faults.** ⭐ **So Failure's severity is a function of
visibility — and `Claim.visibility` already exists on the schema.** That grades Failure three ways
without a second ladder, without a coefficient, and without `stakes_grade`, which was already this
directory's most likely deletion.

---

# PART C · WHY IT IS NOT A GAME YET, STATED PRECISELY

**The four decisions are real** — go, descend, spend, say — and the descent is a genuinely good
irreversible-commitment object. **What is missing is a second player.** An NPC bench's `choose`
scores `convictions × alignment + stance_toward(subject)` (`shape.py:3494-3516`) and consults
**neither what it has been told nor what it wants.**

| field on `Person` | readers | verdict |
|---|---|---|
| `convictions` | 1 — ⭐ inside **`choose`** | live, and well placed |
| `stance` | 1 — `stance_toward()` | live |
| `ledger` (memory) | `belief_contradicts` filters candidates | live since `W-A`, and fed only undifferentiated claims |
| `tenures` | everywhere | live — and this is the `(A,B)` typed record the precedent ranks #1 |
| **`beliefs`** | **0** | ⛔ dead, and already scheduled for deletion |
| **`marks`** | **0** | ⛔ dead — ⭐ **and it is the precedent's #4 mechanism sitting unused** (identity-embedded memory: a scar, a byname, so every future encounter re-surfaces it at zero query cost). Keep it, conditionally, as the home of a person-predicate |

⭐ **AND THE PRECEDENT NAMES THE EXACT FAILURE THIS DESIGN IS WALKING INTO.** RimWorld is the one
surveyed system where memory surfaces **only ambiently** — thoughts feed mood and never gate an
action — and it is the one where players report memories that clearly should matter quietly expiring.
**`reception` is RimWorld's mood.** Claims sum into an obstacle term and that is all they do.

> **The precedent's answer, which is the answer to `P-42`:** *"the single mechanism that reliably
> prevents a retained memory from sitting inert is **coupling the read to a specific
> decision-evaluation point** — never a generic ambient scan."* CK surfaces a hook **in the scheme
> panel**. Nemesis **actively re-queues** the orc who beat you.
>
> **So `P-42` was the right question with the wrong remedy.** The fix is not raising the 200-claim
> cap. It is giving a claim somewhere decision-shaped to be read — which is the eligibility gap in
> the next paragraph.

**Nothing in Valoria makes a NEW ACT AVAILABLE because of what you know about someone.** CK3's hook
unlocks blackmail; a Dwarf Fortress grudge unlocks sabotage. Here, knowing a man's weakness changes a
number and opens no door. **That is the eligibility gap, and it is where fears, secrets and wants all
land.**

---

# PART D · THE EIGHT SHAPES — the corpus's own design law

**From the adjudication of all 27 figures. These are not opinions about the design; they are what the
source material does, counted.** They should govern the ladder wherever the design and the corpus
disagree.

| # | shape | in | what it binds |
|---|---|---|---|
| **1** | ⭐ **Failure is the move read as a signal ABOUT THE MOVER** | **15 figures** | the adverse write is **what the move was taken to mean about the speaker** — never a penalty applied to him |
| **2** | ⭐ **Overshoot, not deficiency** | **13 figures** | Failure sits **just past Success**. The actor who overshot was close. This is fail-forward, sourced |
| **3** | **The band is what the room takes the move as, and the room chooses** | `PERCEPTION`, 155 atoms, 26 of 27 | *"the hearer will choose the reading that costs him least."* **Nothing in the corpus refuses a move; the room reads it** |
| **4** | ⭐ **Terminal = being seen at it** | 7 figures | *the DISCOVERED lie, not the lie.* Costly = **effect** faults; terminal = **exposure** faults. **Severity is a function of `Claim.visibility`, which exists** |
| **5** | **Reception is a function of standing, not of the act** | 3 figures | the same move gets a different band from a different position — and the corpus says this is stronger than a modifier: **it can flip the band's sign** |
| **6** | **The descent** | 3 figures | *"descended only when forced, and each descent concedes something the room can see."* In all three the Partial is **the rung itself becoming the question** |
| **7** | **Relocation and proxy are the corpus's fail-forward** | 6 figures | every costly Failure has a named next move — the sponsor sought, the room changed, the proxy disavowed, the stock filled later. **The corpus supplies "still playing" unprompted in every case but one** |
| **8** | ⚠ **The inverted bands** | 5 figures | **five places the corpus's ladder and the design's disagree.** See below — this is the sharpest section of the adjudication |

## D.1 · The five inversions, because they are where the single ladder breaks

1. **The bottom rung produces the top band.** *Hand the error back to the audience* is the most
   conceding method and **the only one that can turn the room against the accuser rather than merely
   away from him.** Same shape for the joke under attack: highest return and highest variance in the
   corpus.
2. ⭐ **Overwhelming writes NO CREDIT to the actor.** Before a superior, the top outcome is that the
   ruler **adopts the correction as his own** — and the more visibly the counsellor is credited, the
   closer he is to the fatal fault. **The `speak` row writes `Person.stance` on Overwhelming. In the
   audience genre that write belongs to the SOVEREIGN's stance, or the ladder rewards exactly what
   the corpus says is fatal there.**
3. ⭐ **The matter's Overwhelming is the close's Failure.** *"Winning, and being repaid later"* —
   carrying the matter and losing the relationship. **A single `speak` contest cannot express this.**
   Either the close is its own contest, or `matter.carried` must be able to co-emit an adverse
   relationship write.
4. **Overwhelming is structurally absent for counsel.** Under all four settlements of the
   candour/protection axis, *"none of the four escapes it"* — the best available is Success on one
   axis paid for on the other. **For counsel, the top band does not exist.**
5. **Two speech kinds have a fixed native band regardless of the roll.** *Impugn the accuser's
   motive* is **Partial by construction** — it *"does not answer the charge"* — and *object* at the
   procedural rung is Overwhelming (dismissal) or Failure (*"signals evasion"*) with Partial as
   referral, and **has no Success at all.** ⭐ **If the speech-kind roster carries aptness by genre
   and rung, it should also carry WHICH BANDS A KIND CAN REACH.**

## D.2 · The Partial, scored honestly

**The `Partial` correction landed this morning — a held matter grows the docket — and the adjudication
tested it against all 27.**

- **Twelve figures yield a Partial in their own words.** The strongest four: the *Guiguzi* loop
  (*"if the reply does not fit, the opposite is said and one listens again"* — literally a machine
  that emits Partials until it emits a Success); relocation (*"where the room is lost, the room is
  changed"*); interposition (defeat absorbed, and **the concession only the principal can make** goes
  on the docket); and *impugn* (the charge stands unanswered, the accuser's motive becomes a
  counter-charge).
- **Six were reached for** and should not be cited as corpus warrant.
- **Three figures are honestly two- or three-band**, and one — the register matrix — is nearly
  binary: heard-as-virtue or heard-as-vice, with Overwhelming and Success indistinguishable.
- **Six yield no bands at all** and are apparatus about the study rather than about a move.

⭐ **The docket-grows mechanic is corpus-warranted in twelve of twenty-seven figures, which is a
stronger result than it needed.**

---

# PART E · THE OPPORTUNITY REGISTER — sixteen, ranked

**Costs in the design's own units. `A` marks the character-model items.** Three of the first six are
deposit rules that cost a roster member or a line, and everything else stands on them.

| # | opportunity | principle | mechanism | cost | the play it creates |
|---|---|---|---|---|---|
| **O-1** | ⭐ **The room remembers WHO SPOKE** | prerequisite for all of it | a fourth `claim_subject_rule` under which a witnessed act deposits **both** the named subject and the actor. Today `both` *replaces* the actor when a subject is named | **1 roster member.** ⚠ Doubles deposits per speech; forces the `P-42` ledger measurement first | you concede at conjecture so the definition speech lands; the bishop who watched holds *(you, matter.held)*; three seasons later he sits on your appeal. **Without O-1 he holds `(matter, held)` and you are nobody** |
| **O-2** | **The obstacle reads the hearers' ledgers** — `reception`, resolver-side | subversion | claims whose subject is the speaker, weighted by `Claim.source` ordinal and by `when`, plus convictions × alignment | 1 term (already ruled) · 2 magnitudes. Needs O-1 and O-6 | you learn two of five bench members were told you are a forger, so you send an advocate — and buy a room **that cannot concede** |
| **O-3** | ⭐ **The unmet-want term** (A) | emergent narrative — initiation | Q4 already turns a `commit` to an OUGHT into a standing question, **but reads only the Proposition's `subject`**; `predicate`/`value` reach nothing. Evaluate the OUGHT as a typed cell against the holder's own ledger and boost candidates when it is unsatisfied | **1 score term · 1 magnitude · 0 fields** | the Count committed to holding the ford; the levy debate touches the ford; his candidates outscore his caution and he speaks first. **You knew because you witnessed the commit last winter** |
| **O-4** | ⭐ **Pressing a fear** (A) | playing the people | see PART F.2 — it is already half-live | 0 beyond O-1 and O-3 | you name what he dreads in open hearing; his own `choose` sends him where you want. **And you can be wrong** |
| **O-5** | **`Overwhelming` forces the descent** | degrees | two folds, both over live Events: your **own** rung (anything you emitted) and the **forced** rung (an opponent's Overwhelming). Obstacle reads the lower | **0 of everything** — replaces one fold with two | you refuse to descend and gamble; they roll Overwhelming; you are at definition without having spoken, and everyone saw you pushed |
| **O-6** | **`told_by` is minted from the channel** | evidence | set the claim's source from the channel that admitted the observer, which is what the design already claims happens | **0 fields, 0 rosters, one deposit line** | you cannot reach the bench, so you reach the archdeacon who dines with them — and your rumour is the only evidence there is |
| **O-7** | ⭐ **Conviction moves by consequence** — closes `P-21` | forty seasons | `(Person, convictions)` is a live row, *"moved by argument and consequence"*, **with no producer.** Give `determine` a degree-keyed write to the determiner's **own** convictions | 1 write on an existing row · 1 magnitude | you steer a case to the bench whose weight has been ground down by three lenient findings. **Nobody scripted it** |
| **O-8** | **Pressure as a band crossing** (A) | pressures | `Sensation.standing` already *is* the Query — the gap between what you are told about yourself and what you hold. Add standing crossings to the crossing set; a crossing changes what can be chosen, never what happens | 0 fields for two of three sources · **1 field for the third** | the bailiff's standing crosses; his season's first question is about the people who told; he opens a case against a man who said nothing |
| **O-9** | **`Partial` docket grows with a matter YOU name** | degrees | the write exists; nothing says *which* Proposition. Make it the speech's own operand | **0** | you press a matter you expect to be **held**, so the room must docket your framing. Your opponent catches you by carrying the original first |
| **O-10** | **A proof weighed by remove and by the mirror** | evidence | term 5 reads each told claim's `source` ordinal and **discounts to zero** any claim the opposing party can mirror | 0 new terms · 1 magnitude. Needs O-6 | you hoard your witness because a probable sign they can run back moves nothing — and spend it once their record has been examined |
| **O-11** | **Silence priced where a lawful act existed** | subversion | the provider knows the candidate set it just formed; charge only a *choice* not to act | 1 term · 1 magnitude, **swept jointly with the Partial step** | called twice, you say nothing because the only lawful act spends your one proof. The third time the detailed denial is tempting — **which is the study's fault exactly** |
| **O-12** | **The forged record is a proof until examined** | evidence | `forge` writes a forgery quality **that nothing reads**. Let `examine` contest it | 1 term on a proposed row | you forge the grant; they must spend a scene **and be seen examining it**; if their draw fails, the forgery is a finding |
| **O-13** | **The aptness term** (landed) | subversion | with the speech-kind roster authored as data — promised and absent | 1 term · 2 magnitudes · 1 roster | you refuse the forensic frame and argue what should be done — to a bench empowered only to find fact, one of whom wants the ford |
| **O-14** | **Four degrees of presence, and DEFY** | fail-forward | go · send an advocate · a letter · nothing — **plus defy a summons**, which in canon and common law *is* the finding | **1 field (`Tenure.term`)** — and it is the best-value field in the register | you defy so the bench must find contumacy rather than heresy. Costly, not terminal — and the bishop must open again next season, by which time you have reached him |
| **O-15** | **`petition` is the route into any room** | playing the people | no dedup, no cap; a petition reaches a docket only when somebody **carries** it, and that somebody scores it by their stance toward you | **0** | you knot the clerk in autumn so your petition is carried in spring — and the knot tells you he carried your rival's first |
| **O-16** | **Standing route as an erosion profile** | degrees | no key: partition a hearer's claims by the **kind of act** they record. A `Failure` against a dominance-standing speaker **zeroes** the dominance weight for that hearer | 1 sub-term · 1 magnitude · 1 data mapping | the Lord who governs by fear is challenged by a nobody. If the nobody rolls well **once**, every ledger in the settlement discounts the Lord's every future room |
| **O-17** | **The licence as one `BandExtension`, at the seam** | degrees | one count of failed conjuncts, demote-only by construction | 1 magnitude | Fig. 26's four failures each name **what the room heard instead** |

> ### **THE THREE THAT UNLOCK THE REST: O-1, O-6, and taking fan-out off `total`.**
> Between them: **one roster member, one deposit line, one sweep arm.** They cost nothing conceptual
> and every other opportunity is a reader of what they produce. **O-14's one field is the only new
> field in the register, and it also buys the return day, the inquisition's indefiniteness, and
> overdue pressure.**

---

# PART F · THE CHARACTER MODEL — wants, fears, pressures, secrets

> **Jordan, 2026-09-06:** *"Valoria characters are under defined right now but need to have goals and
> ambitions, allegiances, memories, beliefs, convictions, ethical stances, pressures, stresses,
> relationships, etc"* — and then *"fears."*

**Most of the list has a carrier already.** Memories are the ledger, and it is better than expected —
each claim carries *who holds it, about whom, what, when, from what source, at what confidence,
visible to whom.* Allegiances and relationships are the tenure edges. Convictions and stances are
separate fields, both read at decision time. **Two were missing and one was miscounted.**

## F.1 · Goals and ambitions — **there IS a carrier, and it is half-read**

⛔ **My diagnosis of "nothing forward-looking" was wrong by one carrier.** A want is a **`commit` to
an OUGHT Proposition**, it lives on the tenure edges rather than on a field, and the season loop
already turns it into a standing question every season — with a comment that says why: *"without this
an NPC with a standing ambition and a quiet season forms no candidates at all."*

⚠ **But it reads only the Proposition's SUBJECT.** The `predicate` and `value` reach nothing. **So a
want supplies a topic, not a direction:** an NPC who wants to *hold* Vellenmark and one who wants to
*burn* it form identical candidate sets, and both may pick `comply`.

**O-3 fixes it with one score term and no fields.** Three honest caveats, all handed forward:
- **A want must be expressible in the seven precondition forms to be evaluable.** *"Hold Vellenmark"*
  is; *"be loved"* is not, and should not be faked through stance. **An eighth form is a design
  change, named and declined.**
- **Acquiring a want is expensive by data** — uttering and committing are heavily weighted against
  self-preservation, so cautious characters never form new ambitions. **Most wants will be authored
  at world-gen.**
- A satisfied want never terminates, which is tolerable: keeping what you won is a want.

## F.2 · Fears — pressable leverage, and my one-shot model was wrong

> **Jordan:** *"naming a fear once only is dumb. fears are leverage that you can press."*

**A fear is the same carrier as a want with `value=False`** — no new mood, no new field, and Q4
already picks it up. **What separates it from a secret is carrier, not policy:** a fear is a *tenure
fact* that persists until its owner repudiates it; a **secret is a distribution fact** — a claim few
ledgers hold, which telling spreads and nothing can un-spread. **CK3's spend-on-use hook is the
secret's shape and was never the fear's.**

**The press, traced against the deposit path rather than asserted:**

| press | what it costs him | what it costs you |
|---|---|---|
| **1** | his own `choose` promotes candidates about the feared thing — **his act, never forced** | passes the *unrepeated* licence conjunct; received as counsel, not attack |
| **2** | ⚠ **REFUTED: the boost is identical.** Nothing in the deposit path discounts a second landed claim. Diminishing return needs a **habituation clause** inside O-3's term — a count of prior identical claims in his own ledger, person-side, no scalar stored | the conjunct fails → **characterization** (*"said twice it is about the man"*). The veto demotes and the obstacle rises |
| **3+** | the habituated boost falls **below his conviction baseline**, and the verbs his own weights favour take over. ⭐ **A cornered man breaks in the direction of who he is, and you cannot read who he is** | every room these witnesses sit in reads you worse, and there is no ceiling on the reception term |

⭐ **THE INVERSION LANDS SOMEWHERE I DID NOT SAY, AND THE AUDIT IS RIGHT.** The cornered man's drastic
act is about **the feared thing, not about you** — he burns the record, flees the settlement, kills
the witness, confesses to the lesser crime. **Retaliation against the presser requires a live edge
between them.** That is the better story and it is the study's picture; the alternative is a design
change, flagged rather than taken.

⭐ **AND THE TRUE TERMINUS NEEDS NOTHING NEW.** `repudiate` is weighted toward harm borne. A man under
repeated pressure **repudiates his own commitment to the feared thing** — *"let them excommunicate
me"* — and it leaves the set his questions read. **Every later press lands a claim and raises no
question. The lever is spent by HIM, not by you, at a moment his convictions chose and you could not
see coming.** That is the release valve the precedent survey says badly-designed escalation lacks,
and it was already in the table.

**One loophole, and it is symmetrical:** press, wait, press — his habituation decays. But **your
infamy decays on the same clock**, so waiting out his memory waits out your record too. Leave it.

## F.3 · ⭐ The eligibility answer, which is cheaper than the question implied

**Knowing a fear makes no new verb available and no new eligibility kind — every relevant verb is
already `own`. What it makes available is a SUBJECT.** You cannot tell what you do not hold; you
cannot speak about a Proposition you never witnessed. **The knowledge IS the referent**, and the
candidate-formation gate is where it enters.

That answers the gap in PART C without inventing a hook mechanic: the door that knowledge opens is
not a new verb, it is **a new thing you are able to be talking about.**

## F.4 · Pressures and stresses — a Query, not a number

| source | carrier | cost |
|---|---|---|
| **adverse claims about yourself** | ⭐ `Sensation.standing` **already is this Query** — the gap between what you are told about yourself and what you hold, computed per season, stored nowhere | 0 fields; needs O-6 |
| **contradictory commitments** | computable today over the tenure edges; **no reader** | 0 fields |
| **overdue obligations** | ⛔ **inexpressible.** A tenure has no term | **1 field** — the same one O-14 needs |

**Nothing breaks a scalar, because there is no scalar.** A band crossing changes *what can be chosen*
and never *what happens*; the person still acts, with their name on it. **The forbidden shape — a
stress meter spent for outcomes — is refused because nothing is spent.**

⭐ **And the surfacing is the good part:** a crossing's referents are **the people whose claims
compose the gap**, so pressure surfaces as a question *about someone*. That is the difference between
*"his stress is 7"* and *"he has decided it was the archdeacon."*

## F.5 · Secrets — and the containment Jordan named

> **Jordan:** *"secrets can be threatened for revealing, and they can be contained if closed doors
> technically"*

**A secret is a claim some ledgers hold and others do not.** That is the whole definition, and today
it is **impossible** — not unbuilt, impossible — because fan-out is total and everyone holds
everything. It is the emergence survey's **item 1**: *"the fan-out is not total — two ledgers can
differ — the precondition of every secret, lie and rumour."*

Once ledgers can differ, both properties fall out with no new machinery:

- **Threatening to reveal is the same lever as pressing a fear** — you name the subject without
  telling it, and the target's own decision procedure does the rest.
- **But the economics are opposite.** A fear is pressable indefinitely because the condition
  persists; **a secret is spent when you reveal it**, because telling deposits it into every hearer
  and destroys the asymmetry that was your leverage. **One-shot at the terminal move, pressable
  before it.**
- **Containment is now two scopes and both exist.** The floor restricts who was in the room;
  `disposal_reach` (landed this morning) proclaims the ruling regardless. **A sealed conclave
  produces a public decree while the secrets aired inside stay with whoever was standing there** —
  and it does nothing until fan-out stops being total.

## F.6 · The two dead carriers

`beliefs` has **zero readers** and is already scheduled for deletion — a belief is a commit to an
OUGHT. `marks` has **zero readers** and is ⭐ **exactly the precedent's #4 mechanism sitting unused**:
identity-embedded memory, where the consequence is written onto the person (a scar, a byname) so
every future encounter re-surfaces it at no query cost. **Keep it, conditionally, as the home of a
person-predicate — and delete it if O-1 lands without needing it.**

---

# PART G · EVIDENCE AND WITNESSES

**Four axes make a proof heavy or light. All four are derivable from live rows; none is stored.**

| axis | carrier | today | fix |
|---|---|---|---|
| **remove** | `Claim.source` — `firsthand · firsthand_via_knot · told_by · inferred` | ⛔ all deposits are `firsthand`; two of four values are **never minted** | O-6 + O-10 |
| **age** | `Claim.when` + decay | ✅ live | free — a stale proof is light because its confidence fell, and it is **evicted first** |
| **symmetry** | ⭐ **the mirror test** — does the opponent hold a claim with the same subject and predicate? | not built | O-10, resolver-side. ⭐ **The player cannot run it — they cannot read the other ledger. They GUESS it**, which is the hoard/spend decision |
| **kind** | the arrangement's admissible proof set | inert | keep as **admissibility only.** Weight by kind is already carried by `source`; a second table would be a second home |

**On witnesses.** A witness is not a role — it is a person present who tells. Their interests enter
through their own decision: whether they tell at all is scored by their stance toward the subject and
by a **suspicion weight that pushes against telling.** ⭐ **So the play is: call the witness whose
stance toward the accused is negative and whose suspicion is low — not the one who holds the truth
but distrusts you.**

Three properties that already work and cost nothing:

- **A witness who holds nothing on the matter is refused, and the refusal is witnessed.** Calling the
  wrong witness is a public category error that costs the scene.
- **A hostile witness and an honest-but-mistaken one are indistinguishable to the bench.** That is
  `AX-2` doing real work rather than being an obstacle to design around.
- **An ordeal is two games** — and it is the one place a physical contest feeds a proceeding, because
  the wound is a firsthand claim in every present ledger. **Oath is a commitment; breaking it is
  witnessed; perjury is the discovered lie, and terminal by shape #4.** Both cost zero.

⚠ **Two things that cannot be finessed.** The *content* of a told claim does not exist — every
deposit is *"a thing happened"*, never *what was in the granary* — so a witness cannot yet testify to
a fact, only to an event. And **`destroy_record` cannot fire**: burning a record requires holding it,
and nothing confers that hold. The design's *"forgeable, burnable"* is half true.

---

# PART H · PLAYING THE PEOPLE

**Each row: the read, how you could get it, the act, and the risk.** Everything here assumes O-1 and
O-6; without them **the reads are unobtainable**, because nothing in any ledger names a person's
disposition.

| the read | how you get it | the act | the risk |
|---|---|---|---|
| **their allegiance** | you witnessed the commitment, or were told by someone who did | address them as a party, not a judge — speak on a subject their faction is committed against, so **their own question fires** | the commitment may have been repudiated since; **a claim about a dead edge is a stale belief nothing marks** |
| **their convictions** | ⭐ **never directly.** Inferred from what they were witnessed doing — a man who opens cases often weights suspicion | pick the speech kind their weights favour; pick the **bench** by its members' histories | a conviction moved by consequence (O-7) is **invisible to you until they act again** |
| **their want** | you were present when they committed, or a witness told you | name it — or **offer** it, which is what a negotiation is | naming a want they have released is a public misread; **offering it makes your own advantage visible, which fails a licence conjunct** |
| **their fear** | same channels, but rarer — **cautious people do not say what they fear** | press it (PART F.2) | the wrong fear named is a threat with nothing behind it, and under O-16 it is exactly the **called bluff** |
| **what they were told about you** | ⛔ you cannot read it. You can **interview** them — and they learn what you asked | correct it: tell them your own firsthand **before the sitting** | ⭐ this is *"reaching the bench before the sitting"* — **which the design calls corrupt and cannot distinguish from diligence.** A live question, not a defect |
| **their stance toward the subject** | from their acts about it | choose your **advocate** from those they regard well — reception attaches to the speaker | stance is written by speech bands, **including yours**; last season's read may have moved |
| **their office and its remit** | public | the **procedural objection** — cheapest available win | it concedes nothing and **signals evasion**, and under O-1 it is on your record |
| **who they are knotted to** | a knot is witnessed at formation | tell the knotted person, who observes the target | ⭐ **the knot runs both ways** |

⚠ **Three things the design promises and the code makes impossible today:** knowing that **they** said
it (attribution is dropped), knowing it **from someone else at a discount** (`told_by` never minted),
and having any of it reach **their next decision** (the score reads convictions and stance, not the
ledger).

---

# PART I · EMERGENT NARRATIVE

**What the world does today, honestly:** dates fire, dockets form, candidates form for every eligible
verb, speech is taken or not by convictions, and **every event fans out to everyone equally.** Twelve
characters over forty seasons produce **a log**: things happened, everyone knows them identically,
nobody knows who did them, nobody wants anything the docket did not put there, and nobody's
convictions change.

> ### **WHAT MAKES A STORY RATHER THAN A LOG: a DIFFERENCE between two people's ledgers that a third
> person's act exploits, and a WANT that makes someone initiate. Neither exists.**

| # | mechanism | exists? | what it alone produces |
|---|---|---|---|
| **1** | **fan-out is not total** | ⚠ a sweep arm, not the default | two ledgers can differ — **the precondition of every secret, lie and rumour** |
| **2** | **attribution** (O-1) | ⛔ no | *"Aldric said"* — the precondition of grudges, alliances, and being caught |
| **3** | **`told_by` from transport** (O-6) | ⛔ no | rumour distinct from presence — the precondition of being misled |
| **4** | **the unmet-want term** (O-3) | ⚠ half — the question fires, the direction does not | ⭐ **initiation.** Somebody does something in a quiet season for a reason of their own |
| **5** | **reception reads ledgers** (O-2) | ⛔ no | the same room, different people, different outcome — **the R criterion in one line** |
| **6** | **conviction moves by consequence** (O-7) | ⛔ no | forty seasons look different from four: judges harden, benches drift |
| **7** | **a summons with a return day** (O-14) | ⛔ no | absence has three kinds; contumacy is a finding; clocks can be bribed |
| **8** | **pressure crossings** (O-8) | ⚠ the Query exists and reads nothing | the person who breaks, at somebody, on their own initiative |

**Six of eight do not exist. Items 1–4 cost one roster member, one deposit line, one sweep arm and one
score term** — and with those four alone, twelve characters already generate the study's first-order
drama: **the wrong person blamed, the want pursued into the wrong room, the rumour believed by the
bench.** The chain from claim to question to candidate to act to witness is live; it is merely fed
undifferentiated claims.

⚠ **The design documents describe items 2, 3 and 5 as though they were present. The code disagrees,
and the code wins.**

## I.1 · What the precedent survey says will go wrong

**Ranked failure modes from seven shipped systems, and where this design sits on each:**

| failure | this design |
|---|---|
| **undifferentiated NPCs** | ⚠ at risk — convictions and stance exist but are authored thin |
| **memory that never surfaces** | ⛔ **the live risk.** RimWorld's exact failure: memory feeds a number and gates nothing |
| **no causal chain between events** | ✅ avoided by construction — every event carries its causes |
| **escalation with no terminus** | ✅ avoided — see the fear's self-repudiation in F.2 |
| **legibility collapse at scale** | ⚠ unaddressed. Dwarf Fortress's known ceiling: past a certain world-age the linked graph reads as a database dump. **Nothing here curates** |
| **cosmetic memory** | ⛔ **currently true.** Stored, and fed to one obstacle term |

---

# PART J · THE TWELVE VARIANTS — what is the play HERE that is nowhere else

| game | the distinct play | stands on | |
|---|---|---|---|
| **negotiation** | ⭐ **the offer ladder** — utter a complete set of terms, refuse to commit, utter better ones. Every rejected offer is authored, frozen and dated. And the row-6 move: **fix the concession before you are asked** | live today | ✅ ⚠ two-party only; multilateral is a coverage bound on every conclave |
| **negotiation by envoys** | **instructions and rope** — the envoy cannot concede, so the game is *how much rope*, and the rope is a frozen Proposition he can be produced against | live | ✅ the gradient is real; the seizure is flavour |
| **arbitration** | ⭐ **the game before the game** — who arbitrates is a prior mutual disposal, and no appeal makes the choice final | live | ✅ buildable today |
| **legal trial** | **the ladder in the open with an advocate** — descend and be *seen*; and the discovered lie no advocate can absorb | O-1, O-5, the return day | ✅ the flagship, and the most dependent on unbuilt deposits |
| **tribunal** | contest or accept; office interposed **discounts** the criticism | — | ⚠ **its only distinct play is not entering.** Without O-7 it is a trial with fewer keys |
| **interrogation** | **what not to say** — the subject's only lever is silence | O-11 | ⚠ **no distinct play until O-11 exists.** Today the subject speaks or the turn evaporates |
| **inquisition hearing** | **being made the subject IS the loss**; authored indefiniteness reachable through the person who set it | the return-day field | ⚠ **its whole distinctness is one unbuilt field.** Today it is an interrogation with a bench |
| **excommunication** | ⭐ **deciding about someone who is not there, on claims you cannot check.** Three kinds of absence; the decree reaches the realm | O-2, O-6, O-14 | ✅ **the purest test of ledgers-as-evidence** |
| **parliamentary debate** | **which of many to address**, no ladder, no proofs — and `Partial` docketing your framing | O-3, and a speaking order that is unbuildable | ⚠ dissent has no reader |
| **council of state** | ⭐ **the hidden profile** — the one thing only you hold, and saying it breaks consensus | **fan-out off total** | ⚠ **real only if item 1 lands.** Today everyone holds everything, so there is no hidden profile |
| **audience / embassy** | **the seating was the negotiation**; lose the room and change the room — say nothing here and tell it elsewhere | O-6 | ⚠ distinct **only through transport** |
| **appeal to authority** | nested, written-only so nobody is seen to yield; **the depth cap is a term somebody set and can be reached about** | the cap is a fixture, not a term | ⚠ the opener-declares-terms rule is unbuilt |
| *(public debate)* | — | — | ⛔ correctly demoted: eleven games and a degenerate case |

> ### **THREE ROWS HAVE NO DISTINCT PLAY AS THE CODE STANDS** (interrogation, inquisition, council),
> **two more are distinct only through transport**, and the trial's distinctness is attribution.
> ⭐ **The parameter rows are right. What separates them is almost entirely in the deposit rules and
> one field.**

---

# PART K · WHAT TO CUT

| cut | why |
|---|---|
| **`stakes_grade`** | already this directory's most likely deletion. ⭐ **And shape #4 replaces it for free: severity is whether the fault was SEEN, and `Claim.visibility` exists** |
| **`verdict_reasons`** | incoherent as a switch on learning — any bench member can tell. Fig. 13 needs a construction and this is not it |
| **`records_dissent`** | **no reader anywhere.** The council/parliament inversion is produced by the floor and by ledgers differing |
| **`registers[]` and the register-fit term** | the roster does not exist; the map is a lookup the design's own compliance rule forbids; as a "risk" it is a second draw against the one-stochastic-thing claim. **Fold the idea into aptness as one term, or drop it** |
| **the word "chronicle" wherever the design leans on it** | ⛔ **the channel matches nobody.** Telling is the only transport |
| **three false present-tense claims** | that co-located witnesses hold the attribution; that the chronicle channel mints hearsay; that a vacant fired date is docketed. **All three are backlog wearing the present tense** |

---

# PART L · BUILD ORDER

**Nothing below is done until it runs. Ordered by what unblocks what.**

| # | do | why here |
|---|---|---|
| **1** | 🔨 **O-1 · attribution in the deposit** | ⭐ **everything is a reader of this.** One roster member |
| **2** | 📐 **Measure `P-42` WITH attribution on** | attribution doubles deposits, and a similar doubling once made decay unobservable at the 200 cap. **Measure before building on it** |
| **3** | 🔨 **O-6 · `told_by` from the channel**, and take fan-out off `total` | one deposit line and one arm. **Together with O-1 this is the whole precondition for secrets, rumour and hidden profiles** |
| **4** | 🔨 **O-3 · the unmet-want term**, with the habituation clause | ⭐ **initiation.** With 1–4 alone the world starts generating first-order drama |
| **5** | ✏ **Author the speech-kind roster** | promised, absent, needed regardless |
| **6** | 🔨 **O-2 · reception reads the ledgers** | the anti-solver term finally reads something |
| **7** | 🔨 **`Tenure.term`** — the one new field | the return day, the summons, contumacy, overdue pressure, the inquisition's indefiniteness |
| **8** | 🔨 **O-7 · conviction moves by consequence** | forty seasons stop looking like four |

**Items 1–4 are one roster member, one deposit line, one sweep arm and one score term.**

---

# PART M · WHAT NOBODY IS SURE ABOUT

**Handed forward rather than hidden. Seven from the audit, twelve from the adjudication; these are the
ones that would change a decision.**

1. ⭐ **The want-term's magnitude has no honest sweep yet.** Large enough to beat a docketed date and
   characters become monomaniacal; small enough not to, and it never moves a ranking. **And the sweep
   must run against a question-aggregation setting that is not the current fixture, or it measures
   the fixture.**
2. ⭐ **O-1's ledger inflation is a measured risk, not a theoretical one.** A comparable doubling
   already made a decay sweep unobservable. **This is why step 2 exists.**
3. **A badly authored fear is inert.** *Fear the case, not the sentence* is right, and it puts the
   burden on whoever authors the fear. **Nobody knows whether world-gen can author precursors well.**
4. **The per-actor rung may be a tally in the forbidden sense.** Comparing two people's emissions is
   close to a cross-holder aggregate. **The safe fallback is the shared fold with only Overwhelming
   moving it.**
5. ⚠ **`Sensation.standing` is a GAP, not a reputation** — so *"everyone reads you as you read
   yourself"* is **zero pressure**, and a hated man who knows he is hated feels nothing. **That may be
   exactly right (the study's inhibition is about knowing and acting anyway) or backwards. Undecided.**
6. ⭐ **Whether this subsystem owns the contest at all.** Its prize is not in the routing roster, and
   if the prize routes elsewhere instead, **two owners would compose one obstacle.** That is Jordan's
   call and it is the one question here that changes everything downstream.
7. **Every obstacle term added swings a weak speaker far more than a strong one.** Defended as
   fiction — *a duke who speaks badly is carried by his rank* — but it may instead mean a bad
   speaker's room is a lottery. **Nobody has swept it.**
8. ⛔ **One corpus fault does not reconcile with fail-forward.** Every other terminal fault has a
   corpus-supplied next move; the inverse-scale fault does not — *"whoever touches it is killed"*.
   **Either that is the one place the ladder's Failure is not the outcome, or the corpus is being
   softened. Handed forward unsoftened.**
9. **Two branches where the corpus and the modern evidence disagree**, both under attack: whether a
   detailed denial outperforms a brief one, and whether displayed anger extracts concessions.
   **The design must pick per branch, and the evidence for the second is marked unverified by the
   study itself.**
10. **Low latitude reshapes the band distribution in two directions at once** — more impasse **and**
    a bigger win when it lands. ⚠ **An obstacle term cannot express that.**
11. **Interposition hides bands rather than changing them.** Under a document *"the counsellor is not
    seen to be overruled, the sovereign not seen to be persuaded"* — which is exactly what the
    design's uniform fan-out prevents. **A design decision, not a derivation.**
12. **How legibly a band reaches the actor differs by genre** — announced with reasons, announced
    without, never announced. **The design emits uniformly and has no carrier for this.**

---

> ## THE ONE-LINE VERSION
>
> **The design is sound and the corpus supports it better than expected — twelve of twenty-seven
> figures supply a Partial in their own words, and the recurring shapes independently confirm both
> fail-forward and the docket-grows correction.**
>
> **What is missing is not design. It is that no deposit names an actor, no claim is ever second-hand,
> and everyone knows everything. Fix those three and sixteen opportunities become reachable; leave
> them and every term is decoration.**
