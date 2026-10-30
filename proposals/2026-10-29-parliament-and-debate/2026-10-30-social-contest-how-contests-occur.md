# How a social contest occurs, and what the armature is

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

Answers four questions: is it the Aristotelian triad; is it Cicero; is it contemporary persuasion; what is the
armature or basis. It uses the model in `2026-10-30-social-contest-reconciliation-and-distillation.md` (items 1 to 13)
and Jordan's rulings R-1 to R-41 (`2026-10-30-social-contest-primitives-and-kinds.md` §1). Where a point is mine and
not a ruling or a source's, it says so. The persuasion mechanisms themselves (Aristotle's topoi and emotions, Cicero's
officia and parts of an oration, Cialdini) are now sourced in
`research/social_contest_procedures/03_persuasion_mechanisms.md` (Aristotle, Cicero and Quintilian read in full
text; the psychology from abstracts and secondary summaries only, so weaker).

## 1. The answer

**None of the three is the armature. The armature is one structure that every kind of contest runs through; the
theories explain why an act lands, which is to say what feeds the two sides of one draw.**

The armature has four parts, and each is a ruling or a model item, not a theory:

1. **A venue-limited action surface** (R-33). One verb table and one speech-kind roster serve every contest; the
   venue row decides which acts are open, to whom, in what order, with which proofs, and who may act for whom.
2. **One draw per act** (R-5, R-6, R-22, R-32). What the actor brings (a total over capability, argument, evidence,
   leverage, standing, normally 5D or more, R-40) against what stands against them (the opponent's score ÷ 2, the
   room, proofs held against, an office's weight; R-38), through the single degree ladder.
3. **A decider that converts acts into a disposal** (R-12, R-34): the target, the parties, a bench, or a count, on
   the authority the venue gets its force from (the parties, the polity, the church), scaled by that authority's
   legitimacy in the territory (R-36).
4. **A world that learns it** (R-21, S-3, S-7): the result is a fact, witnessed, read at the speed of news, bearing a
   reaction. The outcome rides; an appeal goes to another authority, never back to the same bench (R-35).

The flowchart (`2026-10-30-social-contest-proceeding-flowchart.svg`, beside this file) is this armature drawn in ten steps.

## 2. What each theory explains, and where it lands in the draw

The test for each is the same: *which input to which side of the draw does it supply, or which row key does it set?*

### 2.1 Aristotle

| in Aristotle | what it explains | lands in | status |
|---|---|---|---|
| **ethos** (the speaker's projected character) | why a hearer credits the speaker | the pool, through capability (presence or charisma, R-41; title; office; faction) and **standing**, derived from stances (S-7); the **authority's legitimacy** where the speaker speaks for an office (R-36) | **ruled not a field** (`06_RESOLUTION`: ethos and bias are not fields); read off the ledger |
| **pathos** (the audience's emotional state) | why the same speech moves one room and not another | the obstacle, through **reception** (the room's stance toward the speaker) and **leverage** (what a person fears is pressed *inside their own decision*, R-19); never a stored mood | reception LIVE for `a matter` only; leverage has no producer |
| **logos** (the argument, by enthymeme and example) | why a case is convincing on its merits | the pool, through **argument** and **evidence** a party holds; against a party, through **proofs held against** (the obstacle) | evidence and audience feed `speak` only; argument content is read by nothing |
| **three genres** (forensic, deliberative, epideictic) | what kind of question the room decides | **matter mood** (HOLDS, OUGHT, neither) × the structure: forensic = a bench rules a past matter; deliberative = a count licenses a future act; epideictic = an audience, no bench | derived, not a field (reconciliation E3); nothing reads mood today |
| **topoi** | where an argument comes from | the speech-kind roster's `apt_genre` and `apt_rung`: aptness priced, not refused (R-16) | the roster loads; unread |
| **the emotions** (Rhet. II.2-11) | what to know to move a person: the state of mind, toward whom, on what grounds | Aristotle's rule (II.1): to arouse an emotion one must know **the audience's state, a named target, and a fact the audience believes about that target**; if any is missing, aptness is zero. The same three are what a stance row holds | sourced in file 03; no code |

### 2.2 Cicero and Quintilian

| in Cicero or Quintilian | what it explains | lands in | status |
|---|---|---|---|
| **stasis** (conjecture, definition, quality, jurisdiction) | which question the dispute turns on | the **issue ladder** on a forensic matter (four rungs); it governs HOLDS matters only, since deliberative argument does not run on stasis (Heath) | INTENT; kernel holds a six-rung version |
| **docere, delectare, movere** | the three jobs of a speech: inform, win goodwill, move | *docere* deposits claims (the evidence channel); *delectare* raises reception (the audience term); *movere* is the **effect**, a pursuit that moves, not an input | sourced in file 03: the pairing differs by work (*Orator* 69: prove, please, sway; *De Oratore* II.115: prove, win favour, rouse feelings), and each of the three styles serves one duty (*Orator* 69-70) |
| **partes orationis** (exordium, narratio, partitio, confirmatio, refutatio, peroratio) | the order a case is made in | the **`order` key** and the speech kinds: exordium = frame and win reception; narratio = `tell`; partitio = the issue gate; confirmatio and refutatio = support and attack; peroratio = recapitulate or concede | the keys and kinds load; unread |
| **the five canons** (inventio, dispositio, elocutio, memoria, pronuntiatio) | the process of a speech | invention = choosing the claim; arrangement = `order`; memory = the ledger and Records; delivery = presence | audit source 04 only |
| **vir bonus** (Quintilian) | the good man speaking well | standing as moral character, which self-gates (a discovered lie is terminal, the study's "being seen at it") | RESEARCH |

### 2.3 Contemporary persuasion

| in the research | what it explains | lands in | status |
|---|---|---|---|
| **central and peripheral routes** (Petty and Cacioppo) | the same speech persuades by argument for a motivated hearer and by cues for a distracted one | central = argument and evidence in the pool; peripheral = standing, charisma and numbers, also the pool, but reaching the hearer through reception; **which route** is set by the bench and floor (an expert judge against a crowd) | RESEARCH |
| **story model** (Pennington and Hastie) | jurors judge by the coherence of a story, not by items | **coherence with claims the room already holds**: evidence is weighed against the ledger, not tallied | RESEARCH |
| **reciprocity, commitment, social proof, authority, liking, scarcity, unity** (Cialdini) | levers on compliance | reciprocity = an `oblige` owed; commitment = a `commit` edge (a stated position binds); social proof = the audience's stances; authority = **office weight** (R-31, R-38); liking and unity = charisma and faction; scarcity = circumstantial leverage | sourced in file 03 **with its evidence record, which is weak**: door-in-the-face behavioural compliance r = .052, not significant; the hotel-towel result partly replicated; descriptive norms can boomerang; for unity, no replication found. Treat as heuristics for what feeds pool and reception, not as mechanisms with known size |
| **reactance, inoculation** | pressure backfires; forewarning protects | a failure band reads as "a signal about the mover"; a pre-empt speech kind | study figures; no code |
| **anchoring, logrolling** | first offers set the range; trading across issues | negotiation: an offer sets the obstacle; many matters per contest (R-11) | RESEARCH |
| **BATNA and ZOPA** (Fisher and Ury, Raiffa) | what a party can walk away to | **leverage** (circumstantial, worldly state), the imbalance R-34 names for negotiation | named once in the repo; "not designed" |
| **commitment stores** (Hamblin; Walton and Krabbe) | what a party is held to having said | `commit` edges and claims in the ledger | RESEARCH |

### 2.4 Other genres and traditions

| tradition | what it contributes | lands in |
|---|---|---|
| **Nyāya: vāda, jalpa, vitaṇḍā** | three aims of debate: truth, victory by any device, refutation only; defeat by a named condition | what the row counts as winning and which speech kinds it permits (`proofs`, the roster) |
| **Guiguzi and Han Feizi** | assess before acting; the hidden "reverse scale"; success is the target believing the decision his own | a **probe act** before an act; attribution as the scored outcome |
| **Kautilya** | envoys typed by latitude; sama, dana, bheda, danda | negotiation's `mandate` and the four ways a party moves another |
| **Ars dictaminis and the Arabic chancery** | a register indexed to rank | the `floor` and `interposed` keys; rank-gated speech |
| **Roman Senate; Althing** | speaking order by standing; consensus, then lot, then majority | the `order` key; the count structure's rule |
| **Ordo iudiciarius; Gui; the Council of Ten** | a graded hierarchy of proof; withheld witnesses; secret process | the `proofs` key and what is secret (`disposal_reach`) |
| **Supplication, remontrance, the oath** | a petition that binds the stronger party; an escalation ladder; an oath that escalates as trust falls | the petition kind and `appeal_basis`; ceremony as an interposition |

## 3. How a contest occurs, in order

The ten steps of the flowchart, with the theory each draws on:

1. A **reason to convene** (a charge, a petition, a vacancy, an offer). The world supplies it; nothing is scripted (R-7, R-26).
2. **Frame**: the matter goes on the docket with a mood (HOLDS or OUGHT). Cicero's *constitutio*: what is the question?
3. **Authority**: the parties, the polity or the church decide whose force the venue carries, and so who sits (R-34), scaled by local legitimacy or piety (R-36).
4. **The venue row** limits the action surface: floor, order, proofs, who may act for whom (R-33).
5. **Acts**: an attendee takes an open act. This is where Aristotle, Cicero and the modern literature all work: they say what the speaker brings and what the room resists.
6. **One draw** against the obstacle gives a margin; the one ladder gives a band; Partial leaves the matter on the docket (R-17).
7. **Decision**: by the target, the parties, a bench or a count (R-12, R-29).
8. **Disposal**: a Tenure disposal, a Record, a licence, a seat.
9. **Record and reach**: witnessed, spread at the speed of news, opinions drift (R-21, S-7).
10. **The outcome rides**; an appeal goes to another authority (R-35); compliance or defiance follows.

## 4. What is ruled, what is the repo's, and what is mine

- **Ruled** (Jordan): the single ladder and one draw (R-5, R-6, R-22); the action surface limited by contest type (R-33); the three authorities and their modulation (R-34, R-36); the pool as a total of 5D or more (R-40); that ethos and bias are not fields (`06_RESOLUTION`) and that coercion happens inside the target's decision (R-19).
- **The repo's** (research, unratified): the classical and contemporary mechanisms in §2, as named in the audit sources and the rhetoric research.
- **Mine:** every "lands in" cell. They are a mapping from each theory's mechanism to the draw's inputs and the row's keys, built from the model; none is a ruling. `[CONFIDENCE: medium]`: a reader could place *delectare* in the pool (charisma) rather than in reception, or the story model in the obstacle rather than the pool; the row says which I chose and why.
