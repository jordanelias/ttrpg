# Fit adjudication — debate, persuasion, negotiation, assemblies and their effect on the world

## Status: **REFERENCE (2026-10-29).** Judgments of fit about material that exists or is proposed. It allocates no `ED`/`PP`, moves no head, and is not a plan: a verdict here says whether a mechanism *fits* the game's purposes, never that someone should build it. Authority of the evidence behind each verdict is stated in the verdicts themselves; a verdict that rests only on tier-3 research says so.

**What this is.** The 757-entry corpus (`2026-10-29-debate-corpus-by-theme.md`, `_part2`, `_part3`) was judged by three Opus adjudicators, one per theme group, against the four NERS criteria (`CLAUDE.md` §0.06, method in `skills/ners/SKILL.md`) and against emergent narrative (the churn principle: every decision must generate churn that seeds narrative with no player present). Each cluster of mechanisms received one of six verdicts — `FITS`, `FITS-IF-ADAPTED`, `PARTIAL`, `MISFIT`, `ALREADY-HELD`, `HELD-FOR-REASON` — and each adjudicator re-opened between eight and nine of its riskiest claims in the tree. The three verdict files follow this reconciliation (`_part2` and `_part3` of this document). The pass ran once and its verdicts were not themselves re-audited (`CLAUDE.md` §0).

---

## 1. Five facts decide most of the verdicts

All three adjudicators reached these independently and opened the code for each.

| # | fact | where verified | what it does to the verdicts |
|---|---|---|---|
| 1 | **No mechanism for persuasion can change a vote *about a subject* today.** `argue` pulls the hearer toward the arguer's *whole* pursuit profile and never reads the Proposition, so arguing for and against a motion is the same act. The voter's `commit` score has three terms (pursuit, stance, urgency) and the pursuit term reads only the verb, so every motion scores alike. Everyone argues at pool 2 and 1 of 430 persons holds any capability | `person_q.py:638-658`; `effects_information.py:555-581`; `decision/choose.py:130-151`; `roll.py:63-125`; `rosters.yaml:1223-1233` | Every opinion mechanism in themes C, E, F waits on one missing reader. All three adjudicators say it must stay `pursuit_lean` over the motion's predicate verb: a per-motion lookup would be scripting drift |
| 2 | **Delivery does not form.** Every route from a carried motion to a changed world (CR-36, CR-37, a resolution used as a warrant, a writ, a covenant) hands its document over by `give`, and a computed `give` of anything but a few Records does not form: 0 Rung cessions in 143 worlds | H-229, `hole_register.yaml:4802`; `verb_table.yaml:571` | Binding, transfer and negotiation are all expressible in shape and hand-built in practice |
| 3 | **Persons do not differ in risk or horizon.** The chooser has no risk term and no horizon term, and `Person` has no carrier for either, though Jordan ruled that persons differ in both. Theme M being thin is therefore a finding, not a gathering gap | `choose.py:130-151`; NL-032, NL-033 | Blocks BATNA, anchoring, impasse and the cheap-talk/costly-binding split; every person currently bargains with the same nerve and foresight |
| 4 | **A motion cannot end, and silence is free.** A below-quorum `determine` is a precondition refusal retried every round for ever; a Failure leaves the matter docketed; nothing lapses. And a ruler who ignores a held resolution *does nothing*, so nothing is witnessed | `verb_table.yaml:389,391`; `deliberate.py:332-340`; Part 3 §0 point 4 | A witnessed lapse and a *refusal that is itself an act* (the writ machinery's `defy`, which emits `compliance.withheld`) are what the binding verdicts hang on |
| 5 | **Most of the procedural data is paper.** Of 13 arrangement keys only `disposes` has a runtime reader; a computed `open_case` names no arrangement (H-80), so every per-row rule — including CR-34's tally — has realm reach 0 in computed play | grep of `engine/season/**/*.py`; `part4.md:352-357` | The eight arrangement rows give a good shape and almost no behaviour |

---

## 2. What fits

**Best shapes (verdict `FITS` or `ALREADY-HELD`, in the adjudicators' fit order):**
- **A council is ONE seat whose members join by their own `oblige`** (Part 1 B3). The only cluster that holds from all six NERS directions; zero new objects; membership is a person's decision, so abstaining is a political act with no player.
- **A vote is a count of live `commit`s, declared by a later act** (D2, ED-SC-0034, CR-34). Persons act, nothing is stored, reversing one's vote is `release` and a witnessed vow-break. Held back only by facts 1, 2 and 5.
- **Witnessed claims as institutional memory** (J3). No concession-penalty field is needed: everyone present deposits that you conceded, and ledgers already differ (3 differing pairs against 0).
- **Petition and `carry`** (A2): the only coded route by which a person with no seat reaches a bench. **Writ and compliance** (G2): `issue`, `comply`, `evade/defy` — promulgation and enforcement as two persons' acts. **Oaths** are `oblige`/`commit`/`release` (G10). **`seize` on a held warrant** is exactly "a person acting through a seat, holding a document" (H2). **Elections are `determine`** (D3). **Two tracks** (C1): evidence moves what is true, argument and consequence move what is right (AX-3). **The ABOUT-the-world test** (G5): a disposal must write something somebody can lose.
- **The substrate for drama exists** (K1): non-total fan-out, attribution, `told_by`, reception read from ledgers, pressure crossings, conviction moved by consequence.

**Fit if adapted** (the idea is right, the source form is not):
- *Logos on the motion* (C2): a won `argue` pulls along the motion's predicate verb — the one carrier by which argument can change a vote.
- *Failed or unlicensed moves cost witnessed standing* (C8): today a failed `argue` writes `[]`, so maximum pressure every turn dominates. The cost is an Event witnessed by those present and read later through `regard`.
- *Social proof and the first defector* (C11, D6): a voter's `commit` reads the witnessed commits of fellow members he regards. Today nothing reads others' commits, so there is no snowball.
- *BATNA as the chooser's own competing options* (E2): no reservation-value field; a person accepts when committing outscores his best other candidate act.
- *Bribery as regard* (F3): a bribe is a `give` whose deed raises the recipient's regard, reaching his vote only through a sponsor-standing term in `commit`. No bribe verb.
- *Offers as dated, authored utterances; the treaty is the Proposition both hold a live `commit` to* (E1).
- *Veto as a seat-holder's witnessed act* leaving the resolution held and unexecutable (D7); *attendance as a costed move to the venue* (B4); *agenda control as the holder choosing to carry, hold or let lapse* (A6); *a motion needs a real claim on a real owner plus a trigger of another kind* (A5); *reception re-sourced from commits so the fold reads only the actor's ledger* (J1, ED-SC-0040 option B); *a witnessed lapse* (B5, I1).
- *Binding strength*: **negative concurrence plus a witnessed held record**, not obligation (Part 3 §0). Every clause of H-90 and of canon (`canon/03_canonical_timeline.md:88`, which names the no-confidence motion as the enforcement) is a denial of unilateral power, none a grant of command to the assembly; every historical enforcement form gathered put the positive force in a person's hands.

---

## 3. What does not fit

`MISFIT`, with the constraint each breaks: **faction-stat parliaments and faction-actor voting** (Mandate-weighted tallies, Church Influence counted as votes, a faction that rolls — a faction never acts, and a vote as a stored aggregate is a field); **the archived sanction ladder and motion catalogue** (stat deltas, durations as clocks, AX-5); **the legacy kernel's trackers, armature, style cards and win conditions** (a second conviction store beside `pursuits`; returns a winner, not a margin; reads a faculty); **defeat by named fault** — the Nyaya list needs a semantic judge no person can be, and a second non-die ending; **composition and delivery craft** (the five canons, progymnasmata, *ars dictaminis*) — the engine has no utterance content to arrange; **sortition** — a lot is an outcome with no actor; **player-as-government meters** (political capital, bloc approval); **stored diplomatic rights** (casus-belli tokens, quota compacts) and **parliamentary transfer in its source form** (a faction's Influence against a faction's Legitimacy, the body writing the transfer).

`PARTIAL`: **Venice's councils and the Reichstag colleges** fit at the realm rung only, as several council seats whose resolutions one executor must hold (Venice's ducal co-signature is CR-36's two-seat clause; the Reichstag's three-college recess is three resolutions). **Stasis and proofs** fit forensic matters with a person party, not deliberation: an OUGHT motion has no issue ladder. Appeal and release fit the tenure layer, not proceedings.

`HELD-FOR-REASON`: **speaking order by rank** (nothing records order inside a season); **anchoring, logrolling, scaled compromise** (need content-weighing and per-matter outcomes); **envoys and ceremony** (nothing can carry a covenant); **charters, privileges and prescription** (no privilege carrier, and every hold is minted `since 0`, so age is unreadable); **quo warranto** (`determine` cannot dispose a `hold`, H-217); **risk and horizon** (CR-17).

**Land and asset transfer.** The adjudicators sorted the historical forms by one rule: a form is expressible when it reduces to one person's act whose precondition reads a Record that person holds. Cession, appointment, nomination-and-confirmation, dismissal, confiscation by writ, conquest and deposition by no-confidence are expressible (most hand-built today). Sale or purchase of a title (the gate refuses to move a seat as property), quo warranto, charters of privileges and prescription are not.

---

## 4. The classical and historical material, as judged

- **Plato contributes nothing mechanical, and that is right.** The corpus holds one paragraph on the *Gorgias* and *Phaedrus*, one *Phaedrus* contrast with the Guiguzi, and reading-list titles; the *Republic* is never discussed; canon's Plato is Neoplatonic metaphysics. The *Phaedrus*'s "know the kinds of soul" is the read-of-the-room stat that AX-2 (no privileged access) refuses. Isocrates, Abelard and Boethius are essentially absent; Aquinas appears only as a virtue-source in the pursuit cells.
- **Aristotle, Cicero, Quintilian and Hermagoras are well covered, and only two channels of them can move a vote.** Logos (argument on the motion's content) and ethos (standing in the hearers' eyes, via `regard`). Stasis and proofs reach a vote only in trials; genre, aptness and decorum only change odds; composition craft is decorative.
- **Rome:** convening and framing as office powers (*ius agendi*, *relatio*) are held in `convene`/the docket; speech by rank is held-for-reason; *senatus auctoritas* (a motion carried but vetoed, citable and without force) is exactly a held, unexecuted `resolution`.
- **Venice:** the Collegio setting the Senate's agenda is the A6 shape (agenda power is a holder's choice to carry, hold or let lapse); the ducal co-signature is the two-seat clause; sortition is a misfit. **Reichstag:** the colleges fit at the realm rung. **Han *tingyi*** (counsel without binding) already is the T3a shape. **Ming drafting** (the clerk who frames the decision) is power without a power stat.
- **Not in the corpus:** the Polish Sejm and *liberum veto* are names only (the liberum veto therefore *cannot be judged*); Magna Carta has one mention; Machiavelli and Guicciardini are cited without mechanisms; the "renaissance deliberation and the classical inheritance" file that an interface report describes is not in the tree.

---

## 5. Emergent narrative: where the drama comes from with no player

**Strongest, and mostly already coded or one step from it:** a petition that is buried and noticed (A2/A3); a concession witnessed and cited seasons later (C5, J3); a lord who browbeats a council and is quietly marked by those who heard him (C8); a carried-but-unexecuted resolution and a deposed king who keeps his duchy and so lives on as a rival (G1, H5); a member who must decide whether to join a council at all, and whether to leave his duchy unguarded to attend (B3, B4); a hostage whose captor breaks faith (E4); votes that follow favours with no sale ever recorded (F3).

**Dead today:** the throne empties at tick 0 in every seed and never refills (OP-109) — a contested succession is the drama that should follow and nothing produces it; only 4 of 72 determinations walk back to a fired date and most determinations are Failure at pool 2 against obstacle 2; 11 tellings in two seasons; no ending is reachable (H-176). No entry in the corpus measures a sitting in computed play. The literature's requirement that memory gate a *decision* (not a mood) is met for regard and **failed for motions**, because the voter cannot see what a motion says.

**The repo's choices on the literature's open question** (steer or not): `choose` sees no `World`, thresholds only raise questions, and arcs may not be scripted — so drama-manager and rubber-banding designs misfit (K5), while an occasion ladder of existing questions meets the "enough events outside the characters' control" requirement without a director (K4).

---

## 6. Corrections to the corpus

The adjudicators found these gatherer entries stale or wrong. They are corrected here, not in the corpus files, which record what each source says.

| entry | defect |
|---|---|
| HP-079 / `by_lane/SC` "carry is a no-op" | stale: `_eff_carry` is built (`effects_information.py:355-386`) |
| HP-080 "closed by withdraw or deny" | states the ruling, not the code: no such verb rows exist |
| CL-044 "no petition subsystem" | superseded by CL-099 (a `petition` Record kind and `carry` exist) |
| CD-038 "non-compliance is weak" | wrong: `evade / defy` exists, graded `ruled`, emits `compliance.withheld`; only `construe` is `absent` |
| CD-040 `seize` | incomplete: the Record half needs a held dispensation naming the Record (a seat can license itself by one `issue`); the Rung half licenses on occupation and muster |
| CD-044 "`opinion_of` feeds decisions" | narrowed: it is consumed only as the `< 0` gate on grudge referents (`world_q.py:2471-2473`) |
| PR-059, PR-071 "convictions are ethical weights" | stale: `conviction` is religious-affiliation intensity 0-5 (ED-IN-0251); the ethical weights are `pursuits` |
| PR-001, PR-093, PR-019, PR-052, PR-104, HP-108 | predate code that now exists (the 13-key loader, 8 of 12 games, `judging_set`, SC-03b's contested `determine`, the judge's consequence-moved pursuits) |
| the mirror test "unreached" (SC lane synthesis) | stale: `proofs()` is coded (`world_q.py:641`) — though it is 0 on every computed pair and reads the opponent's ledger |
| `repudiate` (several sources) | cut at IN-11; `release` absorbed it (`verb_table.yaml:1062`) |
| theme J "15-23 entries" | a gathering artifact: 125 entries carry J as a secondary tag. The real gap is narrower: the proceeding-level record (minutes, division, defeat, precedent) has no code, and the adjudication judges that it should stay a gap in *store* form — the record is distributed through witnessed acts |

---

## 7. What this means for the 2026-10-29 parliament proposal

The proposal (`2026-10-29-parliament-and-debate.md`) was written before this adjudication. The adjudication confirms its core (one council seat with members by `oblige`; a motion whose subject is the person it concerns; assembly mints a resolution, the owning seat executes; concurrence over obligation) and its blocker register, and finds two points where the proposal was wrong or too weak, **both corrected in the same commit**:

1. **T2's silence defect.** The proposal let a ruler's non-execution of a resolution cost him "opinion and legitimacy" computed on read. A non-act emits nothing, so nothing is there to read: silence dominates. The record only bites if the owner's answer is an *act* — the writ machinery's `defy` is one. The proposal's §6 now says so.
2. **The first defector.** The proposal marked it "absent". The adjudication finds it *fits if adapted*: a voter's `commit` reading the witnessed commits of fellow members he regards, with no influence rounds and no track. The proposal's §8 row now says so.

It also finds, without changing the proposal, three clusters the proposal does not mention and which sit next to its §5: failed moves costing witnessed standing (C8), bribery as regard (F3), and BATNA as the chooser's own competing options (E2).

---

## 8. Limits of this adjudication

- **Tier-3 evidence.** `research/` cannot settle design (`research/00_INDEX.md`), and the Guiguzi material is graded T2 "a paraphrase of a paraphrase". Verdicts that rest on research alone — social proof, the first defector, the Avogadori, enfeoffment as a renewing bond — are flagged as such in the verdicts.
- **No sitting has been measured in computed play.** Whether a member's `commit` forms on a sitting question, whether anyone off the realm rung hears a realm-venue `date.fired`, and whether `convene` is in the King's grant are all unverified. The adjudications judge fit, which does not require running the engine; they cannot say how a played sitting feels.
- **Reading depth.** The gatherers did not open every file (named in the corpus header); the adjudicators read every entry in their parts but only a sample of sources. Relay passes A-F and most of the 591-row atom table enter only through the proceedings design's own adjudications.
- **The corpus is uneven by theme** (Argument 147, Emergent narrative 121, Convening/procedure 97; Persons 18, Faction 28, Record 23, Agenda 42). Part of that is the repo's coverage, part the gathering's sorting; the verdicts say which where they can.
- **One pass.** Per `CLAUDE.md` §0 the adjudication was not itself audited and its findings seeded no second fan-out.

---

# The three verdict files follow

Part 1 (themes A, B, D, J; L as constraint) is `2026-10-29-debate-fit-adjudication_part2.md`, Part 2 (C, E, F, M) is `_part3.md`, and Part 3 (G, H, I, K) is `_part4.md`.
