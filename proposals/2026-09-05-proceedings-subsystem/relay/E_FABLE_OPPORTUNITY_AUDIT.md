> ## RELAY STAGE E · THE OPPORTUNITY AUDIT — `fable`, read-only, informing only
> ## Status: **PROPOSED (2026-09-06). NOTHING HERE RATIFIES ON MERGE.**
>
> Audited the game system and the twelve variants against Jordan's stated principles — degrees of
> success, fail forward, subverting the proceeding, the weight of evidence and witnesses, and
> playing on what you know of other characters. `fable` is licensed for read-only audit and
> planning and **never for authorship** (`CLAUDE.md` §10), so this is findings; `18_FINDINGS.md`
> writes them up.
>
> ⭐ **Its headline is a code fact, not a design opinion: the ledger cannot hold a reading of a
> person.** No deposit names the actor; every claim is firsthand at full confidence; hearsay is
> never minted; fan-out is total. So `reception` — the one term the anti-solver argument rests on —
> reads a set the world cannot populate.
>
> ⚠ **This file contains TWO passes.** The first is the audit as briefed. The second, appended after
> Jordan corrected the coordinator (*"naming a fear once only is dumb. fears are leverage that you
> can press"*), revises O-4 and the fears subsection — and **refutes the coordinator on the
> diminishing return**, which needed a habituation clause the original model did not have.

---

I have everything I need; no further reads. Verified against the code before writing: the default fan-out is `total` (`shape.py:1798`, `:6256-6259`), so a closed floor is an unbuilt sweep arm; every WITNESS deposit is `(predicate=e.kind, value=True, source=firsthand, confidence=100, visibility="own")` (`shape.py:6327`, `:6336`, `:1787`); `told_by`/`inferred` are rostered (`rosters.yaml:119`) and never minted (only reader is `standing_of` at `shape.py:4011`); and a witnessed write-nothing act that names a subject deposits **no claim naming the actor** (`shape.py:4203-4205`; `rosters.yaml:272-274` says so in words). Those four facts drive most of what follows.

---

# PART 1 · THE VERDICT ON PLAYABILITY

**No — not today, and not "as designed" either, because the design's game-making claims sit on code that does the opposite.** The four decisions in `07_THE_GAME.md:23-29` (go · descend · spend · say) are real decisions with legible stakes, and the descent (`07:95-118`) is a genuinely good irreversible-commitment object. But every one of them resolves against an obstacle whose only hidden, load-bearing term — `reception`, "composed from the hearers' own claims about the speaker" (`06_RESOLUTION.md:231-235`, `15_WHY_IT_IS_A_GAME.md:57-66`) — reads a set that the world cannot populate. A hearer's ledger never records who spoke (`shape.py:4203-4205`); every claim it does hold is an event-kind at confidence 100 sourced `firsthand` (`shape.py:6336`); `told_by` is never minted (`rosters.yaml:119` vs `shape.py:6327`); and the seam raises for any prize but the body (`shape.py:6757-6771`, and `"a matter"` is not in `rosters.yaml:441-446`). So the player's "room whose mind they cannot see" (`07:13`) has no mind: `AX-2` hides nothing because there is nothing to hide, and `15` PART A's solver is intact — the arrangement is printed, the rung is public, the proofs are yours, and the one term that was supposed to make the sum uncomputable is zero everywhere. A person would sit down, take the flowchart's line, and be told afterwards through channels that also do not attribute (`07:218-228` promises "the attribution — you saw who did it"; the code drops it). That is not tense; it is opaque and then unexplained, which is the frustration `15:153-157` names and does not resolve.

**Taking the design as if built, it is closer, and the reason is that the study's structure survived into the schema.** The hoard/spend decision on proofs has genuinely opposite correct answers by elaboration (`07:120-138`); `Partial` now grows the docket (`04_VERBS.md:144-159`) so the middle band is off-axis; a genre-mismatched speech is priced not refused (`04:228-260`), so the wrong ground can be taken on purpose; and the tempo result — hearing and judgment cannot share a season because `binding_decision` resolves before `social` (`rosters.yaml:129`, `04:338-355`) — creates a whole season of reachable people between pressing and ruling, which is where the game actually is. What it lacks is a second player: an NPC bench whose `choose` (`shape.py:3494-3516`) scores `convictions × alignment + stance_toward(subject)` and consults neither what it has been told nor what it wants. Its "characters of the world" (`14_THE_WORLD_IN_THE_ROOM.md:239-254`) are slots with names until something a person knows about another person reaches an outcome.

**The single biggest thing standing between this and a game: the ledger cannot hold a reading of a person.** Not "reception is unbuilt" (that is downstream) — the deposit itself, `Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own")` at `shape.py:6336`, with `subj` set to what was named rather than who acted (`:4203-4205`), makes "what the bishop holds about you" unrepresentable anywhere in the world. Every mechanism in Parts 3, 4 and 5 below — the value of a witness, the weight of a proof, the threat, the pressure, the bench that remembers you folded — is a reader of that one missing row. Fix the deposit (opportunity O-1) and the rest becomes buildable; leave it and every term is decoration.

---

# PART 2 · THE OPPORTUNITY REGISTER

Ranked by how much play changes. Costs are counted in the design's own units: **fields · verb rows · roster members · obstacle terms · score terms · magnitudes · Event kinds**. Where a band column says "deposit-independent" it is because WITNESS fans out regardless of degree (`06:385-388`), which is correct and is stated rather than glossed. `A` = ambition/fear items, detailed in PART 4A and ranked here.

### O-1 · The room remembers who spoke — attribution in the deposit
- **Principle:** exploiting knowledge of other characters (prerequisite for all of it); fail-forward (a failure only "brings new obstacles" if the failure is *yours* in somebody's ledger).
- **Mechanism:** a fourth `claim_subject_rules` member (`rosters.yaml:250-303`) under which a write-nothing act that names a subject deposits **both** the named subject and the actor — today `both` replaces the actor when `refs` is non-empty (`shape.py:4203-4205`). Under `T-d`/`H-107` the tracer's `Event.subject` is still the actor (`shape.py:2113`, `rosters.yaml:291-292`), so nothing new is read; the rule stops discarding it.
- **Bands:** deposit-independent — but with attribution, `Failure`'s `matter.turned` (`04:76`) becomes "*Aldric* turned it", which is the first moment any band is *about a person* in anybody's memory.
- **Cost:** 1 roster member, 0 fields. Not free: it doubles deposits per witnessed speech, and `rosters.yaml:294-299` measured that doubling made `H-40`'s decay sweep unobservable under `ledger_cap=200` (`shape.py:1772`). So it forces the `P-42` measurement (`10_LOOPS_AND_GAPS.md:100`) to happen first.
- **Variant most changed:** legal trial (`floor: open`) — the open floor is only expensive if the concession is attributed.
- **The play:** you concede at conjecture so that the definition speech lands; the bishop who watched holds `(you, matter.held)`; three seasons later he sits on your appeal and the reception term reads it. Without O-1 he holds `(matter, matter.held)` and you are nobody.

### O-2 · The obstacle reads the hearers' ledgers — `reception`, and only as a resolver-side term
- **Principle:** subverting the proceeding (the sum becomes uncomputable for a reason inside the fiction, `15:72-77`).
- **Mechanism:** as `06:231-235`, composed over `Claim` rows whose `subject == speaker` in each bench member's ledger, weighted by `Claim.source` ordinal (`17_PLAYABILITY.md:288-299` adjudicated: source, not confidence) and by `Claim.when` (decay already exists, `shape.py:5458-5488`), plus `Person.convictions × alignment` for the matter's verb kind. `World` first in the signature (`10:88`, `P-30`).
- **Bands:** it moves the *obstacle*, so it moves the prior over all four; what it does *per band* is nothing — which is correct, and is why O-11 and O-14 must exist to give bands distinct jobs.
- **Cost:** 1 obstacle term (already ruled, `06:219-242`), 2 magnitudes (source weight, conviction weight), 0 fields. Depends on O-1 and on `told_by` being minted (O-6).
- **Variant most changed:** excommunication deliberation — a bench deciding about an absent person is *only* its ledgers.
- **The play:** you learn (by `interview`, at the price of being seen asking) that two of five bench members were told you are a forger; you send an advocate instead of going, because reception attaches to the *speaker* (`03_PARAMETERS.md:404-409`). The catch: an advocate cannot concede (`01_THE_STUDY.md:177`), so you have bought a room that will not descend.

### O-3 · The unmet-want term in `score` — ambition gets a direction, fear gets a precaution (A)
- **Principle:** emergent narrative (initiation); playing the people (a want is what a threat reads).
- **Mechanism:** Q4 `need` already turns a live `commit` to an OUGHT Proposition into a standing question every season (`shape.py:3929-3937`) — but only the Proposition's `subject` is read (`:3937`); `predicate`/`value` are read by nothing (grep: no `prop.predicate`/`prop.value` in `shape.py`). Add one person-side term to `score` (`shape.py:3502-3506`): evaluate the OUGHT's `(subject, predicate, value)` as a typed cell against `LedgerReader(p.ledger)` — the same call `belief_contradicts` makes at `:3860-3861` — and boost candidates about that subject when the want is KNOWN-FALSE or UNKNOWN. A fear is the same Proposition with `value=False`; it is satisfied by default and boosts only when the feared predicate lands.
- **Bands:** person-side, so band-free at the term; its consequences enter the run through whatever act it promotes.
- **Cost:** 1 score term, 1 magnitude (swept), 0 fields, 0 verbs, 0 rosters. **One real bound:** a want is expressible only in the seven `requires_forms` (`rosters.yaml:810-818`), so a person can want exactly what the precondition grammar can ask. That is narrower than "goals and ambitions" and it is said plainly in PART 4A.
- **Variant most changed:** council of state / parliament — deliberative bodies have no ladder (`03:643-649`), so what a member *wants* is the only thing that moves them.
- **The play:** the Count commits to OUGHT(hold(Count, the ford)); the levy debate is about the ford; his candidates about it outscore his convictions' caution, and he speaks first (`07:154`, the costly move). You knew that because you witnessed his `commit` last winter.

### O-4 · Naming the fear — coercion that happens inside the target (A)
- **Principle:** playing the people; subverting (the threat can fail, and fail publicly).
- **Mechanism:** already lawful and half-live. A `speak` whose subject is the Proposition id F that B holds a `commit` to deposits, under the default `both` rule, a claim with `subject == F` into every present ledger (`shape.py:4148-4205`); B's Q2 fires because F is in `mine` — the objects of B's live tenures (`shape.py:3883`, `:3900-3903`). B then forms candidates about F's subject. **What is missing is polarity:** with O-3, those candidates are precautionary; without it they are scored by convictions alone. **What makes it knowledge you had to acquire:** you can only name F if you hold a claim about it — you witnessed B's `commit`/`utter` or were `tell`-ed by someone who did, and `tell` refuses a teller with no claim (`verb_table.yaml:478-489`).
- **Bands (the speech is a `speak` and rolls):** O — `matter.carried`: the room takes your framing and B's Q2 fires; S — B's Q2 fires; P — the docket grows with your subsidiary question (O-9); F — `matter.turned` and your own stance written adversely (`04:72`); *and in every band* the room holds that *you* named it (O-1) and B may name the wrong fear back.
- **Cost:** 0 of everything beyond O-1 and O-3. **Misread:** if F is not in B's tenures, Q2 does not fire, nothing happens in B, and you are on record as having threatened someone with nothing.
- **Variant most changed:** interrogation — the questioner's whole craft is naming what the subject fears without a bench to persuade.
- **The play:** you utter "the Cardinal has opened a case on the Guildmaster" in the Guildmaster's hearing, because you saw him commit against exactly that last season; his own `choose` sends him to `petition`, which puts him in a room you control. The Cardinal, who was also present, now holds that you know about a case he thought was sealed.

### O-5 · `Overwhelming` forces the descent; a concession is per-actor
- **Principle:** degrees of success — the top band gets the one thing the others cannot do.
- **Mechanism:** the rung fold today is over *any* `matter.*` emission in the run and is band-blind (`05_PROCEDURE.md:85-95`; the honest version at `17:415-421`). Replace with two folds, both over emitted Events (which carry `subject`=actor at `shape.py:2113` and `degree` at `:2117`, assigned at `:5855`): (a) a party's *own* rung = lowest rung their own emissions named, at any band — you said it, you conceded it; (b) the *forced* rung = lowest rung named by an *opponent's* `Overwhelming`. The obstacle for your next speech reads `min(own, forced)`.
- **Bands:** O — the fact is established against the other side without their conceding ("descended only when forced", `01:244`); S — the matter advances, nobody is moved; P — the docket grows (O-9); F — `matter.turned`, your own stance written.
- **Cost:** 0 fields (a fold over live Events, owned by nobody, dies with the run — `00_DERIVATION.md:298-302`); 0 terms; replaces one fold with two.
- **Variant most changed:** legal trial — the only row where three parties (accuser, advocate, subject) all emit.
- **The play:** you refuse to descend and press at conjecture against a proven fact, gambling on a bad draw for them; they roll `Overwhelming` and the room now treats the fact as found. You are at definition without having said a word, and everyone knows you were pushed.

### O-6 · `told_by` is minted from the channel — hearsay becomes a different thing from presence
- **Principle:** evidence and witnesses; playing the people ("who told you, and how long ago", `14:160`).
- **Mechanism:** `witness()` builds `fan` as `(pid, e, mode)` (`shape.py:6268-6269`) and sets `src` only from the knot test (`:6325-6327`). Set `src` from the channel that admitted the observer: `co_located → firsthand`, `chronicle`/`document_key`/`post_remit` → `told_by`, which is what `14:166` claims already happens. Requires `fan_out_mode` off `total` (`shape.py:1798`); and `chronicle` matches nobody today (`shape.py:4390-4407`), so the `tell` verb is the only transport (`shape.py:4167-4169`) — a `tell` deposits `told_by` into its co-located hearers.
- **Bands:** deposit-independent.
- **Cost:** 0 fields, 0 rosters (`claim_sources` already carries all four, `rosters.yaml:119`), one deposit line. Unblocks `standing_of` (`shape.py:4011`), O-2's source ordinal, and pressure (O-8).
- **Variant most changed:** excommunication — a bench told at second hand about a person who did not come.
- **The play:** you cannot reach the bench, so you reach the archdeacon who dines with them; what lands in their ledgers is `told_by` at *his* confidence, and O-2 weights it below a firsthand — unless nobody firsthand is on the bench, in which case your rumour is the only evidence there is.

### O-7 · Conviction moves by consequence — `determine` writes the determiner's own convictions (closes `P-21`/`L-6`)
- **Principle:** emergent narrative over forty seasons; degrees (the band sets the magnitude of the movement).
- **Mechanism:** `(Person, convictions)` is a live `RES` row with `social: true`, "moved by argument and consequence, never by evidence", and no producer (`write_matrix.yaml:182-188`, `:58-64`). Give `determine` a `Degree`-keyed `writes` that includes `Person.convictions` on the *actor* (owner = actor, `AX-4` clean) — the shape `write_matrix.yaml:61-64` says an interior write must take. The axis moved is the one `alignment` weights for `determine` (`rosters.yaml:909`: `Precedent`), so nothing branches on a game.
- **Bands (of the finding, once `determine` has a `contests:` — `17:288-291` finds it declares none):** O — the determiner hardens on the axis; S — small movement; P — none, the matter is held; F — the determiner is *moved against* their own axis (the judge who ruled and regretted it).
- **Cost:** 1 degree-keyed write on an existing row, 1 magnitude, 0 fields. Sign of `L-6` is then measurable (`10:26`).
- **Variant most changed:** tribunal — a standing body that sits every season is the one whose members drift.
- **The play:** you steer a case to the bench whose Precedent-weight has been ground down by three lenient findings; the same arrangement, the same seats, a different obstacle, and nobody scripted it.

### O-8 · Pressure surfaces as a `Sensation.standing` band crossing (Q3), never as a stored number (A)
- **Principle:** pressures and stresses under the no-aggregates rule; fail-forward (a crossing changes what can be chosen, never what happens — `T-b`, `05:115-116`).
- **Mechanism:** `Sensation` is *exactly two scalars* and the second is `standing`, computed per season as the gap between `told_by` claims about self and own firsthand claims (`shape.py:2163-2207`, `:3993-4014`), stored nowhere. Q3's docstring says "a Sensation band change" but the code iterates site crossings only (`shape.py:3905-3927`). Add standing crossings to `w.crossings`, computed by recomputing `standing_of` over claims with `when < tick` versus all claims — no stored previous value. Referents of the question = the people whose `told_by` claims compose the gap. A crossing may admit/promote `repudiate`, `evade / defy`, `move` through the existing `alignment` table (`rosters.yaml:917-924`) — the person still chooses.
- **Bands:** person-side; the acts it promotes roll.
- **Cost:** 0 fields, 0 rosters, a Q3 reader; depends on O-6. **What it cannot express without a field:** an *overdue* obligation — `Tenure` has no `term` (`shape.py:2067-2086`, `P-04` at `10:59`). Contradictory commits (two live `commit`s to Propositions sharing subject+predicate, differing value) are computable today with no reader — one more crossing source, zero fields.
- **Variant most changed:** inquisition hearing — `term_required: false` is "authored indefiniteness" (`03:612-619`) only if the subject can feel it.
- **The play:** the bailiff has been told three things about himself by people he cannot name (`07:190-193`); his standing gap crosses a band; his season's first question is about *them*, and he forms `open_case` against the man he thinks said it — who did not.

### O-9 · `Partial` grows the docket with a matter *you* name
- **Principle:** degrees (landed 2026-09-06); fail-forward.
- **Mechanism:** the row writes `DocketItem.matter` and emits `docket.formed` (`04:69-76`, `write_matrix.yaml:119-125`) but nothing says *which* Proposition. Make it the speech's own operand — the speaker chooses the subsidiary question. CALENDAR dockets a fired date with `matter: None` (`shape.py:5378-5380`) and `carry` writes the matter (`verb_table.yaml:83-96`), so a `Partial` is a `carry` that the *bench* did not choose.
- **Bands:** this *is* the P band's job; O/S/F leave the docket alone.
- **Cost:** 0 (an operand on an existing act). One correction: `03:365-366` says a *vacant* fired date is docketed; `shape.py:5371-5380` dockets only a *held* one. The code wins, and it means a proceeding nobody holds a date for lapses with no docket — which is the right behaviour for "a hearing nobody attended".
- **Variant most changed:** parliamentary debate — the game of which-of-many-to-address becomes the game of what the house must take up next.
- **The play:** you press a matter you expect to be *held* so that the room is forced to docket your framing ("was the grant ever made?"); the bench's Q1 next season carries your matter in its referents (`shape.py:3885-3891`). Your opponent can catch you by pressing the same date to `Overwhelming` first and carrying the original.

### O-10 · A proof is weighed by its remove and by the mirror test
- **Principle:** evidence and witnesses. Detailed in PART 3.
- **Mechanism:** term 5 ("proofs told so far", `06:238`) reads each told claim's `source` ordinal `[firsthand, firsthand_via_knot, told_by, inferred]` (`17:295-297`) and discounts to zero any told claim for which the *opposing party* holds a claim with the same `(subject, predicate)` — the mirror test as a Query over two ledgers, resolver-side.
- **Bands:** the term moves the prior; a *told* proof is itself a `tell`, whose refusal `news.untold` is witnessed (`verb_table.yaml:485`).
- **Cost:** 0 new terms (term 5 reweighted), 1 magnitude. Depends on O-6 for `told_by` to exist.
- **Variant most changed:** "is it true that this occurred" at the conjecture rung (`14:97-106`).
- **The play:** your best proof is a confident witness; theirs is a record. You hoard yours because the mirror test says a probable sign they can run back moves nothing (`01:292-294`) — and spend it only once their record has been `examine`d for forgery (O-12).

### O-11 · Silence priced only where a lawful act was not taken (P9 rebuilt)
- **Principle:** subverting; the fifteen-step table's inhibition finding (`01:93-98`).
- **Mechanism:** as adjudicated at `17:578-584`: the provider's own loop iterates attendees (`05:40-44`), knows the candidate set it just formed, and adds `PASS_STEP` to the actor's obstacle only when a lawful act existed and none was taken; carved out by the arrangement row, falsified on `order: scripted`.
- **Bands:** raises the obstacle of your *next* speech; what that speech does per band is unchanged.
- **Cost:** 1 obstacle term, 1 magnitude, and `G.4`'s ratio to `HELD_STEP` must be swept jointly (`17:951-958`).
- **Variant most changed:** interrogation — the only row where *what not to say* is the whole game (`07:269-273`).
- **The play:** you are called and say nothing, twice, because the only lawful act was a `tell` that would spend your one proof; the third time the obstacle is high enough that the detailed denial (`07:150`) is tempting, and that is the study's fault exactly.

### O-12 · The forged record is a proof until it is examined
- **Principle:** evidence and witnesses; subverting (the "wrong" evidence can carry).
- **Mechanism:** `forge` writes `Record.forgery_quality` (`verb_table.yaml:229-237`, `shape.py:2418`) and nothing reads it. Let `examine` (the new row at `04:428-438`) contest `retention` *plus* `forgery_quality` when the subject is a Record: `Found` deposits a claim `(record, forged, True)`; `Nothing` leaves the forgery standing. Until then a `tell` from a forged record enters term 5 at the weight of a record.
- **Bands (of `examine`):** Found — the forgery is a claim in the examiner's ledger (and the forger's exposure is `TERMINAL`, `01:318-319`); Partial — a claim at lower confidence; Nothing — the record stands and you were witnessed examining (`04:437-438`).
- **Cost:** 1 obstacle term on an already-proposed row, 0 fields. `Record` has no holder (`shape.py:2412-2421`), so *who carries it* is `hold` Tenures only — `destroy_record` needs `hold:<record>` (`verb_table.yaml:158-167`).
- **Variant most changed:** appeal to authority (`order: written_only`, `proofs: [record]`) — a game played entirely on paper is a game played entirely on forgeries.
- **The play:** you forge the grant at quality 7; they must spend a scene and be seen examining it; if their draw fails, the forgery is a finding, and the appeal that could expose it is one somebody has to open.

### O-13 · The aptness term (landed) — with `speech_kinds` authored as data
- **Principle:** subverting (the right choice can fail, the wrong can land).
- **Mechanism:** `04:198-260`; the roster is promised at `04:211-216` and does not exist (`17:229-231`).
- **Bands:** the wrong ground rolls against a higher obstacle; F at the wrong ground writes your stance *and* the room witnessed the category error (`04:252-255`).
- **Cost:** 1 term, 2 magnitudes, 1 roster with two typed columns (`17:805-806` — a schema addition, counted).
- **Variant most changed:** the Demosthenes case — a trial played as an honour contest (`03:133`).
- **The play:** "you refuse the forensic frame and argue what should be done to a bench empowered only to find the fact — and the Cardinal of Prudence, who wants the ford more than the finding, hears you."

### O-14 · The advocate's four degrees of presence (P7 kept) and the summons with a return day
- **Principle:** fail-forward (absence is a course, not a negation); the three absences of `P-33` (`10:91`).
- **Mechanism:** GO / SEND (an advocate's `commit` to your disposition + `oblige` to you, `03:393`) / NEITHER, plus **DEFY** — `evade / defy` of a summons (`verb_table.yaml:202-214`), which is contumacy and in canon and common law *is* the finding. Requires the summons to be an `issue` with a return day → `Tenure.term` (`P-04`).
- **Bands:** the advocate's bands attach to the advocate; a discovered lie attaches to you regardless (`03:411-414`).
- **Cost:** 0 for the gradient; **1 field (`term`) for the return day**, and it is the field that also unblocks `surveil`, the inquisition's indefiniteness, and overdue pressure — the best-value field in the register.
- **Variant most changed:** excommunication deliberation — three kinds of absence, one row.
- **The play:** you defy the summons so that the bench must find contumacy rather than heresy; contumacy is `costly`, heresy is `terminal`, and the bishop who wanted heresy must now `open_case` again next season, where you have had a season to reach him.

### O-15 · `petition` is the route into any room; the clerk is a person with a stance
- **Principle:** playing the people; the D.6 rescue (`17:456-459`).
- **Mechanism:** `petition` has no dedup and no cap (`verb_table.yaml:377-387`); a petition reaches a docket only when somebody `carry`s it (`:83-96`), and that somebody scores it by `stance_toward(you)` (`shape.py:3437-3446`). Every docket has a gatekeeper who is a person.
- **Bands:** `carry` is uncontested; the *petition's* fate is the carrier's `choose`.
- **Cost:** 0.
- **Variant most changed:** audience/embassy — you cannot speak until you are on the docket, and the chamberlain decides.
- **The play:** you `tie / knot` the clerk in autumn so that your petition is carried in spring; the knot also makes you a `witness_key` observer of *his* acts (`shape.py:4361-4365`), which is how you learn he carried your rival's first.

### O-16 · Standing route as an erosion profile derived from the hearers' claims
- **Principle:** the study's one predictive cut (`01:203-216`); degrees (a single `Failure` collapses dominance).
- **Mechanism:** no `route` key. Resolver-side, partition the hearer's claims about the speaker by the *kind* of act they record: `kill / wound`, `revoke`, `levy`, `evade / defy` → dominance-sourced; `determine`, `create_record`, `tell`, `comply` → prestige-sourced. A `speak` with a person subject that rolls `Failure` against a dominance-standing speaker zeroes the dominance-sourced weight in reception for that hearer ("a single called bluff", `01:208`).
- **Bands:** O/S — nothing; P — nothing; **F — the bluff is called**: dominance-sourced weight collapses.
- **Cost:** 1 reception sub-term, 1 magnitude, 1 data mapping (verb → route) — a table keyed on the verb table, the `alignment` precedent (`rosters.yaml:877-906`).
- **Variant most changed:** public debate — the only prize is standing, and this is the only mechanism under which standing can *fall* in one act.
- **The play:** the Lord who governs by fear is challenged in the open by a nobody; the nobody rolls badly and is turned; but if he rolls well once, every ledger in the settlement discounts the Lord's every future room.

### O-17 · The licence veto as one `BandExtension`, once, at the seam
- As adjudicated (`17:620-629`): `dice_engine.BandExtension` is the injection seam (`dice_engine.py:95-138`), demote-only by construction (`:292-300`). One `licence` count of failed conjuncts. Cost: 1 magnitude (the cut, `17:817`). Principle: degrees — Fig. 26's four failures each name what the room heard instead (`03:168-179`), and the demotion is the only band-transition an extension may make.

---

# PART 3 · EVIDENCE AND WITNESSES

**What exists.** One obstacle term counting "proofs told so far in this run" (`06:238`); `tell` requiring the teller hold a claim on the subject (`verb_table.yaml:478-482`) and refusing with `news.untold`; `proofs[]` as an admissibility set on the arrangement (`03:457-458`); a `Record` with `forgery_quality` and no holder (`shape.py:2412-2421`); five investigation rows with typed preconditions and no deposit (`04:427-535`, `P-05`); and a study that says the confident witness is "a probable sign wearing a necessary sign's clothes" (`01:299-301`) and supplies the mirror test as its one operational result (`01:292-294`).

**What makes a proof heavy or light — four axes, all derivable from live rows, none stored:**

| axis | carrier | today | opportunity |
|---|---|---|---|
| **remove** | `Claim.source` ordinal `[firsthand, firsthand_via_knot, told_by, inferred]` (`rosters.yaml:119`) | all deposits `firsthand` (`shape.py:6327`); `inferred` never minted; `reconstruct` would mint it at "real confidence" (`04:465-475`) | O-6 + O-10. A told proof's weight is its remove, and `reconstruct`'s `Wrong` band emits identically to `Sound` — the purest `AX-2` proof in the game |
| **age** | `Claim.when` + decay (`shape.py:5458-5488`) | live | free; a stale proof is light because its confidence fell, and the eviction key `confidence × (when+1)` (`shape.py:6443`) forgets it first |
| **symmetry** | the mirror test — does the opponent hold a claim with the same `(subject, predicate)`? | not built | O-10: a Query over two ledgers, resolver-side. The player cannot run it (they cannot read the other ledger) — they *guess* it, which is `07:135-138`'s point |
| **kind** | `proofs[]` on the arrangement — `record, testimony, oath, ordeal, confession, sign` (`03:30`) | inert; `ordeal`/`confession` are this design's additions to Fig. 6 (`10:96`, `P-38`) | keep as admissibility only; the *weight* by kind is what `source` already carries (a record is `document_key`-sourced, testimony is `told_by`) — do not add a second table |

**Witnesses — who can be called, at what cost, and what their interests do:**
- A witness is not a role; it is a person present who `tell`s (`03:394`). Calling one is a summons (`issue` + their own `move`), which needs a return day → `P-04`. Until then a witness is whoever travelled.
- **A witness tells what they hold, at their own confidence, and it may be wrong.** That is already the whole mechanism: `AX-2` makes a hostile witness and an honest-but-mistaken one indistinguishable to the bench. Their *interests* enter through `choose`: whether they `tell` at all is scored by `stance_toward(subject)` and `self_preservation × alignment(tell)` — and `tell` is `suspicion: -0.5` in the alignment table (`rosters.yaml:929`), so a suspicious witness withholds. **What a player does with that:** you call the witness whose stance toward the *accused* is negative (learned by `interview`) and whose suspicion is low; you do not call the one who holds the truth but distrusts you.
- **A witness who holds nothing on the matter is refused with `news.untold`, witnessed** (`verb_table.yaml:485`). Calling the wrong witness is a public category error and costs the scene.
- **Cost of calling:** a scene of theirs (they must travel), and a scene of yours to reach them beforehand; under O-1 the room records *who called whom*.
- **What is underbuilt and cannot be finessed:** the *content* of a told claim. Every deposit is `predicate = e.kind, value = True` (`shape.py:6336`) — a witness can only "tell that a thing happened", never *what was in the granary*, until `observation_deposit_modes` (`rosters.yaml:305-337`, `H-122`) fans typed reads beyond the actor. That is `P-05` and it is the bar (`10:51`).

**Forged and destroyed records:** O-12. Add: `destroy_record` is `hold:<record> | presence` and its own eligibility declines on both (`verb_table.yaml:158-167`, `:72-74`), so *burning the record* cannot fire today — the design's "forgeable, burnable" (`03:118`) is half-true. A destroyed record leaves `record.destroyed` witnessed by whoever was co-located, which is how the arsonist is found.

**Oath and ordeal** (`03:30`): an ordeal is two games (`03:766`) — correct, and it is the one place a *physical* contest (`combat_seam`, live) feeds a proceeding: the wound state is a firsthand claim in every present ledger. Oath is an `oblige` to a HOLDS Proposition — breaking it is `repudiate`, witnessed; perjury is the discovered lie, `TERMINAL`. Both cost zero.

---

# PART 4 · PLAYING THE PEOPLE

What a player can *do* with knowledge of a specific person. Each row: the read (how you could know it), the act, the risk. Everything here assumes O-1 and O-6; without them the reads below are unobtainable, because nothing in any ledger names a person's disposition.

| the read | how you get it | the act | the risk |
|---|---|---|---|
| **their allegiance** — a live `commit` to a faction's Proposition | you witnessed the `commit` (co-located) or were `tell`-ed by someone who did | address them as a party, not a judge: `speak` with a subject their faction is committed against, so their own Q2 fires | their `commit` may have been `repudiate`d since; a claim about a dead edge is a stale belief nothing marks (`14:167`) |
| **their conviction weights** (`Person.convictions`, four axes, `rosters.yaml:171`) | never directly (`AX-2`); inferred from *what they were witnessed doing* — a person who `open_case`s often weights `suspicion` (`rosters.yaml:926`) | pick the speech kind whose `alignment` matches their weights; pick the *bench* by its members' histories | a weight moved by consequence (O-7) is invisible to you until they act again |
| **their want** — a `commit` to an OUGHT | you were present at the `utter`/`commit`, or a witness told you | O-4: name it. Or *offer* it: `utter` an OUGHT whose terms satisfy their want and `commit` first — a negotiation is exactly this (`14:76-95`) | naming a want they have `release`d is a public misread; offering it makes your own advantage *visible*, which fails Fig. 26's fourth conjunct (`03:173`) |
| **their fear** — a `commit` to an OUGHT with `value=False` | same channels; rarer, because `utter` is `self_preservation: -0.9` (`rosters.yaml:920`) — cautious people do not say what they fear | O-4 | the wrong fear named in a room is a witnessed threat with nothing behind it; under O-16 it is exactly the "called bluff" |
| **what they were told about you** | you cannot read it; you can `interview` them (their `SAID` row, which may be a lie, `04:385`) and they learn what you asked | correct it: `tell` them your own firsthand before the sitting — which is the "reaching the bench" the design calls corrupt and cannot distinguish from diligence (`17:294-299`) | `interview` is contested; `Misread` emits identically to `Read` (`04:446`); you may act on a read that was false |
| **their stance toward the subject** (`Person.stance` rows) | from their acts about that subject | choose your *advocate* from among those they hold a positive stance toward — reception attaches to the speaker | `Person.stance` is written by `speak`'s bands (`04:68-72`) — including yours; a stance you observed last season may have moved |
| **their office and its remit** | public (`Office.remit_acts`, `shape.py:2443`) | the procedural objection — press at rung `procedural` that this bench's remit does not reach the matter; "cheapest win, signals evasion" (`00:163`) | it descends nothing and concedes nothing, but the room reads evasion; under O-1 it is on your record |
| **who they are knotted to** (`tie / knot`) | a knot is stored once (`verb_table.yaml:507`) and witnessed at formation | tell the knotted person, who is a `witness_key` observer of the target's acts (`shape.py:4361-4365`) and vice versa | the knot runs both ways: what you tell the knotted person, the target's ledger can carry |

**The three things the design lets you do to a person that the code makes impossible today, said plainly:** (1) know that *they* said a thing — attribution is dropped (`shape.py:4203-4205`); (2) know it *from someone else* at a discount — `told_by` is never minted; (3) have any of it reach *their* next decision — `score` reads convictions and stance, not the ledger, except through clause 4's KNOWN-FALSE filter (`shape.py:3259-3265`), whose write side is unbuilt (`rosters.yaml:310-318`).

---

# PART 4A · THE CHARACTER MODEL — wants, fears, pressures, and the dead carriers

The owner's list against `Person` (`shape.py:2362-2394`): **memories** = `ledger` (real, but see the deposit defects above); **beliefs** = `beliefs[]`, **dead** — no reader anywhere in `shape.py`, and `write_matrix.yaml:52-53` schedules its deletion under #358 rev.2 ("a belief is a `commit` to an OUGHT"); **convictions** = `convictions{}`, read by `score` (`shape.py:3503`), written by nothing (`write_matrix.yaml:58-64`); **ethical stances** = `stance[]`, read by `stance_toward` (`:3437-3446`), written by no live verb; **allegiances/relationships** = `tenures[]` (`commit`, `oblige`, `hold`, `tie`, `knot`), live and read everywhere; **`marks[]`** — **dead**: declared at `:2367`, named as the predicate vocabulary standing needs (`rosters.yaml:195-204`), and read by nothing — `standing_of` (`:3993-4014`) pairs on predicate without consulting it. Two dead carriers; `ID-13` says delete or find a reader — `marks[]` is the natural home of the `person_predicates` a *reading of a person* would carry (heritage · grade · church_standing · office · residence), and O-1/O-2 are its reader if the deposit ever writes a person-predicate. Keep it, conditionally.

### Goals and ambitions
**Lawfully a `commit` to an OUGHT Proposition, needing no new field — and the code already reads it as a standing question** (`shape.py:3929-3937`; `rosters.yaml:173-193`: "Without Q4 an NPC with a standing ambition and a quiet season forms no candidates at all"). So the coordinator's diagnosis "nothing on a Person is forward-looking" is wrong by one carrier: a want lives on `tenures[]`, not on a field.

**What an NPC's `choose` does with it today:** forms candidates whose *subject* is the OUGHT's subject (`:3937`), across every eligible verb, ranked by `convictions × alignment + stance_toward(subject)` (`:3502-3506`). The want supplies a topic, not a direction: an NPC who wants to *hold* Vellenmark and one who wants to *burn* it form identical candidate sets, and both may pick `comply` because their convictions favour it. The OUGHT's `predicate` and `value` reach nothing.

**What breaks if you rely on it as-is:** (a) ambitions are direction-less (above); (b) a satisfied want never terminates — Q4 fires every season while the commit lives, and nothing `release`s it; that is tolerable (keeping what you won is a want) and avoids a termination mechanism; (c) *forming* a want is expensive by data — `utter` is `self_preservation: -0.9` and `commit` is `-1.0` (`rosters.yaml:918-919`), so cautious NPCs never acquire new ambitions; most wants will be authored at world-gen; (d) the `question_aggregation: first` fixture means a Date always beats a need (`rosters.yaml:217-231`), so a docketed person is never ambitious that season.

**The fix is O-3: one person-side score term.** Cost: 0 fields · 0 verbs · 0 rosters · 1 score term · 1 magnitude. **The genuine limit, stated rather than contorted:** a want must be a typed cell in the seven `requires_forms` with the eight closed operands (`rosters.yaml:768-818`) to be *evaluable* against the ledger. "Hold Vellenmark" is `existence` over a `hold`; "be Duke" is `existence` over a `hold` of an office; "be loved" is not expressible, and should not be pretended to be. If the owner wants wants the grammar cannot ask, that is an eighth form, which is a design change (`rosters.yaml:788-790`), and I would rather say so than fake it through `stance`.

### Fears — the coordinator's three claims, adjudicated
1. **"Pursued vs prevented; a fear never terminates."** Holds — but as a *polarity of one mechanism*, not a second class of act. A fear is `commit` to OUGHT(P, value=False). Its satisfied state is the default (nothing has happened), so under O-3 it boosts nothing until a claim lands that makes it KNOWN-FALSE. Precaution *before* the feared thing is the interesting half and it needs the fear to name the **precursor**: fear of excommunication that is precautionary is `OUGHT(case.opened(me) = False)`, not `OUGHT(excommunicated(me) = False)`. The alternative — a table from precursor to outcome — is pair-count growth (`04:266`) and is refused. So: **fears are fears of specific Events, and they never terminate because the commit never has to be released.** The "costly step to forestall something that was never coming" falls out when the precursor lands and the outcome never does — and nothing in the world has to produce it.
2. **"Specific, not scalar; same carrier as ambition."** Holds. `Proposition.value` is `Any` (`shape.py:2432`); `value=False` suffices; no new mood, and `mood` stays `OUGHT` so Q4 (`:3935`) already picks it up. Tested against `choose`: today a negative-value OUGHT is treated exactly like a positive one — a topic — so an NPC who fears X acts *about* X with no avoidance polarity. `stance_toward` with negative valence (`:3444-3445`) would *suppress* candidates about X, which is avoidance, not precaution. Only O-3 gives precaution. **Verdict: one carrier, zero fields, and neither works without O-3.**
3. **"Naming the fear is lawful leverage."** Holds architecturally and is *half-live today* (traced in O-4): a `speak`/`utter` about the feared Proposition deposits a claim with `subject == F` in the target's ledger under the default `both` rule, and Q2 fires because F is an object of the target's own live `commit` (`shape.py:3883`, `:3900-3903`). The coercion is the target's own `choose`. What is missing: (i) attribution — the target learns that F was named, not *by whom* (O-1); (ii) polarity — the target's candidates about F are scored by convictions, not by threat (O-3); (iii) the threat has no band unless it is a `speak` with `contests:` — `utter` is uncontested (`verb_table.yaml:531-539`), so "naming the wrong fear in front of a room is a witnessed act with a band" is true only for `speak`. **Where the coordinator is wrong:** "it costs the world nothing to produce" — it costs one attribution rule and one score term, and it costs the target a `commit` they must have made where you could see it. That last cost is the good part: you cannot threaten someone with a fear they never showed.

**Cost, both together:** 0 fields · 0 verbs · 0 rosters · 0 Event kinds · 1 score term (O-3) · 1 magnitude · 1 `claim_subject_rules` member (O-1). No new primitive is needed for either. The one *new primitive* this section would otherwise reach for — a "wants the grammar cannot ask" eighth form — is named and declined.

### Pressures and stresses
- **As a Query over live edges:** (a) *adverse claims about self* — `standing_of` **is** this Query and is designed as `Sensation`'s second scalar (`shape.py:2163-2207`); it reads `told_by`, which is never minted (O-6). (b) *contradictory commitments* — computable today over `tenures[]` and `propositions`; zero fields; no reader; add as a crossing source (O-8). (c) *overdue obligations* — **inexpressible without `Tenure.term`** (`P-04`, `10:59`). That is one field, it is the same field O-14 needs, and it is the one place in this audit where I say: add the field.
- **What makes it surface at a dramatic moment:** the Q3 `band_crossed` source (O-8), whose referents are the *people* whose claims compose the gap — so pressure surfaces as a question *about someone*, which is the difference between "his stress is 7" and "he has decided it was the archdeacon". A crossing changes what can be chosen (T-b); it never acts.
- **Breaking:** no scalar breaks. A crossing that admits `repudiate`/`evade / defy`/`move` by their `alignment` weights (`rosters.yaml:917-924`) is the person breaking — and it is their act, with their name on it. The forbidden shape (Blades' stress spent for outcomes) is refused because nothing is spent; the lawful shape is that a threshold changes the option set.
- **Cost:** 0 fields (a)(b) · 1 field (c) · 1 Q3 reader · 0 magnitudes beyond the band edges of `standing` (which `condition_scale` already supplies, `shape.py:4010`).

---

# PART 5 · EMERGENT NARRATIVE

**What the world does when nobody is watching, today:** dates fire; a held date is docketed with `matter: None` (`shape.py:5378-5380`); every NPC's questions arrive as `date_due` first (`rosters.yaml:193`, `:224-226`), so they attend to whatever is docketed; candidates form for every eligible verb about the docket's referents; `speak` (no precondition, writes nothing) is taken or not by convictions; WITNESS fans every event to everyone (`shape.py:1798`, `:6256-6259`); every ledger fills with `(what-was-named, kind, True, firsthand, 100)`; the cap evicts; confidence decays. Twelve NPCs for forty seasons produce a **log**: things happened, everyone knows them equally, nobody knows who did them, nobody wants anything but what the docket says, and nobody's convictions change. `07:368-373`'s "the world holds hearings when nobody is watching" is true and it holds them the way a clock holds time.

**What produces a story rather than a log:** a *difference between two people's ledgers* that a third person's act exploits, and a *want* that makes someone initiate. Neither exists. The minimum set, in order, with what exists honestly marked:

| # | mechanism | exists? | what it produces on its own |
|---|---|---|---|
| 1 | **the fan-out is not total** — `floor`/presence scoping live (`fan_out_mode` off `total`; H-33's `presence_only` arm) | swept arm, not default (`shape.py:1798`) | two ledgers can differ — the precondition of every secret, lie and rumour |
| 2 | **attribution** (O-1) | no | "Aldric said" — the precondition of grudges, alliances, and being caught |
| 3 | **`told_by` from transport** (O-6) | no | rumour distinct from presence — the precondition of being misled |
| 4 | **the unmet-want term** (O-3) | Q4 half exists | initiation: an NPC who *does something* in a quiet season for a reason of their own |
| 5 | **reception reads ledgers** (O-2) | no | the same room, different people, different outcome — R's "without player involvement" in one line |
| 6 | **conviction moves by consequence** (O-7) | no (`P-21`) | forty seasons look different from four: judges harden, benches drift, `L-6` gets a sign |
| 7 | **a summons with a return day** (`Tenure.term`, O-14) | no (`P-04`) | absence has three kinds; contumacy is a finding; clocks can be bribed |
| 8 | **pressure crossings** (O-8) | `standing_of` exists, reads nothing | the person who breaks, at somebody, on their own initiative |

Items 1-3 are deposit rules and cost nothing but a measured ledger-inflation risk. Items 4-6 are one term each. Item 7 is the one field. **Without 1-4 nothing below them can fire; with 1-4 alone, twelve NPCs already generate the study's first-order drama** — the wrong person blamed, the want pursued into the wrong room, the rumour believed by the bench — because the loop's `claim_landed → question → candidate → act → witness` chain (`14:127`, `L-3`) is live and merely fed with undifferentiated claims.

**Honestly, which of the eight do not exist:** 2, 3, 5, 6, 7, and 8's reader; 1 is a sweep arm; 4 is half-built (Q4 reads the subject). Six of eight. The design documents describe 2, 3 and 5 as though present (`07:222`, `14:166`, `06:231`); the code disagrees, and the code wins.

---

# PART 6 · THE TWELVE VARIANTS

| game | the play HERE that is nowhere else | stands on | finding |
|---|---|---|---|
| **negotiation** | the offer ladder — `utter` a complete OUGHT, refuse to `commit`, `utter` better terms; every rejected offer is authored and dated (`14:76-95`); row 6, fixing the concession before you are asked | `utter`, `commit`, `repudiate` — all live | ⚠ two-party only; multilateral is `P-15`, and it is a coverage bound on every conclave |
| **negotiation by envoys** | instructions and rope: the envoy cannot concede (`01:177`), so the game is *how much rope* — P7's gradient (`17:493-498`) | `commit` + `oblige`, live | the seizure ("the point") is flavour; the gradient is real |
| **arbitration** | the game before the game — who arbitrates is a prior mutual disposal (`commit`s to OUGHT("X arbitrates")); `appeal_basis: none` | `commit`; `open_case` terms via `Record.stages` (a fabricated default, `17:443-446`) | distinct, and buildable today |
| **legal trial** | the ladder in the open with an advocate: descend and be seen (needs O-1); the discovered lie no advocate absorbs (`03:411-414`) | O-1, O-5, `P-04` for the summons | the flagship, and the one most dependent on unbuilt deposits |
| **tribunal** | contest or accept: `office` interposed discounts the criticism (`03:583-588`); no appeal → `P-12` ratchet | `interposed: [office]` waiving Fig. 26 (`03:155-158`) | ⚠ the only distinct play is *not entering*; without O-7 (a bench that drifts) it is a trial with fewer keys |
| **interrogation** | what not to say — the subject's only lever is silence, which is not an act (`07:74`) | O-11 (silence priced) and a confession as a `tell`+`oblige` | ⚠ **no distinct play until O-11 exists**: today the subject either speaks or the turn evaporates; the questioner's play is O-4 |
| **inquisition hearing** | being made the subject *is* the loss; authored indefiniteness (`03:612-619`) reachable through the person who set it | `Tenure.term` (`P-04`) | ⚠ its whole distinctness is one unbuilt field; today it is an interrogation with a bench |
| **excommunication deliberation** | deciding about someone who is not there on claims you cannot check (`07:280-284`); three absences (`P-33`); the decree reaches the realm (`disposal_reach`) | O-2, O-6, O-14 | distinct, and the purest test of ledgers-as-evidence |
| **parliamentary debate** | no ladder, no proofs (`03:643-649`): which of many to address; `Partial` docketing your framing (O-9); losers on the record | O-3 (members' wants), `order: rank` (`P-08`, absent) | ⚠ `records_dissent` has no reader; `order: rank` needs the fold changed |
| **council of state** | the hidden profile: the one thing only you hold, and saying it breaks consensus (`07:292-297`) | ledgers differing (fan-out off `total`) | ⚠ **real only if item 1 of Part 5 lands**; today everyone holds everything, so there is no hidden profile |
| **audience / embassy** | the seating was the negotiation; lose the room and change the room — say nothing here and `tell` elsewhere (`07:299-304`) | O-6 (`told_by` transport), `order: scripted` | distinct *only* through transport; without `told_by` the Relatio reaches nobody at a discount |
| **appeal to authority** | nested; written-only so nobody is seen to yield; the depth cap is a declared term somebody can be reached about (`00:238-253`) | `contest_max_depth` (a fixture today, `shape.py:1803`, not an act's term) | ⚠ the cap is a fixture, not a term of the opening act — `T-n` unbuilt |
| **public debate** | degenerate (`14:321-340`): a `speak` that finds no bench; standing only | O-16 (route erosion) is the only thing that makes it worth a scene | ⚠ eleven games and a degenerate case; correctly demoted |

**Findings from the table:** three rows have no distinct play as the code stands (interrogation, inquisition, council), two more are distinct only through transport (audience, excommunication), and the trial's distinctness is attribution. The parameter rows are right; what separates them is almost entirely in deposit rules and one field.

---

# PART 7 · WHAT I WOULD CUT, AND WHERE I AM LEAST SURE

**Cut.**
- **`stakes_grade`** — `P-09`, the design's own next move (`10:70`); the stake is what `disposes` writes and whether it is closable.
- **`verdict_reasons`** — incoherent as a boolean on learning, because any bench member can `tell` (`17:727-732`); Fig. 13 needs a construction and this is not it.
- **`records_dissent`** — no reader anywhere; the council/parliament inversion (`03:657-662`) is produced by `floor` and by ledgers differing, not by this key. Delete until a quorum (`P-15`) gives it a job.
- **`register fit` as an obstacle term and `registers[]` as a key** — the roster does not exist (`17:748-750`), the 7→7 map is a lookup the design's own compliance row forbids (`P-39`), and as a "risk" it is a second draw against the one-stochastic-thing claim (`17:760-763`). Hold the *idea* (a manner invites a misreading) and fold it into aptness as one term, or drop it.
- **`route` as anything declared** — derive it (O-16) or leave it.
- **The word "chronicle" wherever the design leans on it** — the channel matches nobody (`shape.py:4398-4402`); `tell` is the only transport.
- **The claim at `03:365-366`** that a vacant fired date is docketed — the code does the opposite (`shape.py:5371-5380`); correct the sentence.
- **The claims at `07:222` and `14:166`** that co-located witnesses hold the attribution and that `chronicle` mints `told_by` — neither is true of the code; both are the O-1/O-6 backlog wearing the present tense.

**Least sure, handed forward.**
1. **O-3's magnitude.** A want-boost large enough to beat `date_due` under `question_aggregation: first` makes NPCs monomaniacal; small enough not to, and it is `urgency` again — a term that never moves a ranking (`shape.py:3449-3468`). The sweep must be against `question_aggregation: all`, not `first`, or it measures the fixture.
2. **O-1's ledger inflation.** Attribution doubles deposits per speech; `rosters.yaml:294-299` measured that a similar doubling made decay unobservable at cap 200. `P-42` must be run *with* attribution on before anything else is built on it.
3. **Fear-as-precursor puts the authoring burden on whoever writes the fear.** "Fear the case, not the sentence" is right and it means a badly authored fear (of the outcome) is inert until the outcome — which is a fear that never protects. I do not know whether world-gen can author precursors well.
4. **O-5's per-actor rung.** A fold over emitted Events keyed by actor is owned by nobody and dies with the run — but "min(own, forced)" is a *comparison across two people's emissions*, and I cannot rule out that it is a tally in the sense `T-a` refuses. If it is, the honest fallback is the band-blind shared fold with `Overwhelming` alone moving it.
5. **`Sensation.standing` is a GAP, not a reputation** (`shape.py:3998-4002`). Using it as the pressure scalar means "everyone reads you as you read yourself" is zero pressure — a hated man who knows he is hated feels nothing. That may be exactly right (the study's *inhibition* is about knowing and acting anyway) or it may be backwards. Not decided.
6. **Whether `speak` should be a contest at all today.** `"a matter"` is not in `rosters.yaml:441-446` and `contest()` raises on any prize the manifest does not route (`shape.py:6757-6771`). Everything above assumes the manifest row at `08_SEAM.md:60-65` lands; if Jordan routes `"a proposition"` to `social_contest` instead (`README.md:107-111`), the obstacle composition in `06` competes with `systems/social_contest/sim/contest/degree_extension.py`'s pool-aware de-saturation (`sigma_leverage.py:336-343`), and there would be two owners of one obstacle.
7. **The 1/√pool behaviour of every obstacle term** (`06:265-282`, `P-27`): all of O-2, O-10, O-11, O-13 add flat Ob shifts, so a weak speaker is swung by them far more than a strong one. That is defended as the fiction ("a duke who speaks badly is carried by his rank") and it may instead mean a bad speaker's room is a lottery. Nobody has swept it.

### Critical Files for Implementation
- `/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/shape.py` — the deposit (`:6319-6346`), `claim_subjects` (`:4133-4205`), `score` (`:3494-3516`), `questions_for` (`:3864-3959`), `standing_of` (`:3993-4014`), `witness()` channels (`:4340-4407`)
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/rosters.yaml` — `claim_subject_rules`, `observation_deposit_modes`, `witness_channel_predicates`, `contest_subsystems.prizes`, `alignment`
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/verb_table.yaml` — `speak`, `determine`, `tell`, `petition`, `forge`, `the six investigation acts`
- `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/04_VERBS.md` — the `speak` row and bands, the five investigation rows, `P-05`
- `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/06_RESOLUTION.md` — the obstacle composition and the `reception` term every opportunity above feeds

---

# ⭐ SECOND PASS — the fear model revised after Jordan's correction

Understood — the one-shot model is withdrawn. Below is the replacement for the fear material; it supersedes **O-4** in the register and the **Fears** subsection of PART 4A. I modelled the three presses against the actual deposit path rather than asserting them, and the result is: **confirmed for the cost to you, refuted for the diminishing return on him, and the inversion is real but lands somewhere you did not say.**

---

## O-4 (REVISED) · Pressing a fear — standing leverage with changing returns

**What a fear is, mechanically, and why it is not a secret.** A fear is a live `commit` Tenure to an OUGHT Proposition with `value=False` (`shape.py:2425-2434`, `:3929-3937`). It is a *tenure fact* — it persists until its owner `repudiate`s it — and naming it consumes nothing because nothing is written to it. A **secret** is a *distribution fact*: a claim held by few ledgers, which `tell` spreads and nothing can un-spread. Different carriers already; CK3's evict-on-use hook is the secret's shape and never the fear's. No design is needed to keep them apart.

**The press.** A `speak` (or `tell`, or `utter`) whose subject is the feared Proposition F. Traced through the deposit: under the default `claim_subject_rule="both"` (`shape.py:1841`), a write-nothing act naming a subject deposits `Claim(subject=F, predicate=e.kind, value=True, when=tick, source=firsthand, confidence=100)` into every present ledger (`:4203-4205`, `:6336`); B's Q2 fires next season because F is an object of B's own live tenure (`:3883`, `:3900-3903`); B forms candidates about F's subject. Each press is a new Event with a new claim id (`:6335`), so N presses across seasons leave N dated claims in every witness's ledger. **That count is reconstructible from live rows and no counter is stored — confirmed.**

**The three presses, against the code:**

| press | what the ledgers hold afterwards | what B's `choose` does | what it costs A |
|---|---|---|---|
| **1** | one `(F, kind, when)` per witness | Q2 fires; under O-3 the precautionary boost is full; B's promoted candidates about F's subject are where "he yields" comes from — *his* act, never forced | the first press can pass Fig. 26 conjunct 3 (*unrepeated*, `03_PARAMETERS.md:172`, form 4 cardinality at `:193`); if the other three hold it is received as counsel, not attack |
| **2** | two dated claims per witness; with **O-1**, also `(A, kind, when)` ×2 — "the kind of man who does this" | Q2 fires again. ⚠ **Refuted as written: the boost is identical to press 1.** Nothing in the deposit path discounts a second landed claim. Diminishing return on *him* needs a habituation clause in O-3: boost ÷ (1 + count of prior claims in B's *own* ledger with the same `(subject, predicate)`). A count over live rows, person-side, no scalar | conjunct 3 now fails → *characterization* ("said twice it is about the man"); the licence veto demotes (O-17) and/or the `licence` term raises the obstacle. **This half needs no O-1**: the veto is resolver-side and can count prior presses from the log and `act_of` (`shape.py:5360`). The *reception* half (O-2, what these hearers hold about A) does need O-1 |
| **3+** | many; the oldest are decaying (`:5458-5488`) and first to evict (`:6443`) | the habituated boost falls under B's conviction baseline; the verbs his weights favour take over — `harm_borne → kill / wound 0.9, repudiate 0.8`; `self_preservation → evade / defy 0.8, move 0.3`; `Precedent → open_case 0.8` (`rosters.yaml:908-938`). **A cornered man breaks in the direction of who he is, and A cannot read who he is** (`AX-2`) | every room these witnesses sit in reads A worse; the only ceiling is P-232's floor of 1 on the obstacle — there is none on the reception term, and `P-27`'s 1/√pool behaviour means a weak presser is swung hardest |

**The inversion, and where it actually lands.** B's drastic act is about **F's subject — the feared thing — not about A.** Q2 admits only claims whose subject is B or something B holds (`shape.py:3902`); A is neither unless B holds a `tie`/`knot`/`oblige` whose object is A. So the cornered man burns the record, flees the settlement, kills the witness, confesses to the lesser crime — *not* the presser, unless he was already bound to the presser. **Retaliation at A requires a live edge B→A, or a widening of Q2's second clause — a design change to §F1, counted as one.** I think landing on the feared thing is the better story and the study's picture; I flag the alternative rather than take it.

**The true terminus needs nothing.** `repudiate` is `harm_borne: 0.8` (`rosters.yaml:934`). A `harm_borne`-weighted man under repeated pressure `repudiate`s his own commit to F — *"let them excommunicate me"* — and F leaves `mine` (`:3883`). Every subsequent press lands a claim and raises no question. **The lever is spent by him, not by you**, at a moment his convictions chose and you could not see coming. That is the release valve, it is already in the table, and it is the property the precedent survey says badly-designed escalation lacks.

**Where a press decays, escalates, inverts — and on what read:**
- **decays** (return on him): on the count of prior identical claims in B's own ledger, *discounted by their decayed confidence* — so a press after many quiet seasons is nearly a first press again. Free, correct, and a loophole: *press, wait, press.* The loophole is bounded by the presser's own aging record in the hearers' ledgers, which decays at the same rate (same clock, `write_matrix.yaml:79-85`), so waiting out his habituation also waits out your infamy. That is symmetrical and I would leave it.
- **escalates** (cost to you): on (i) the log — prior charges by this actor on this subject, resolver-side, no O-1 needed; (ii) the hearers' ledgers — what they hold about A, needs O-1, read by O-2.
- **inverts**: where the habituated boost crosses B's conviction baseline for the drastic verbs. Not a threshold anyone sets; two curves cross, at a different press count for every man.

**Bands of a press (it is a `speak` and rolls):** O — `matter.carried`, the room takes your framing and B's Q2 fires; S — B's Q2 fires; P — the docket grows with a matter *you* name (O-9): you have made the room take up the thing he fears; F — `matter.turned` and your own stance written adversely, and (with O-1) the room holds that you tried and were turned — the first press that fails is the moment he learns you are pressing.

**Two ways it turns on you, both already in the table:** name the wrong F (F ∉ B's tenures → no Q2, and you are on record as threatening with nothing); name the right F too often (conjunct 3, reception, and the man breaking toward something you did not foresee).

**Cost of the revised model:** 0 fields · 0 verbs · 0 rosters · 0 Event kinds · 0 counters. The habituation clause lives inside O-3's one score term. O-1 for the reception half of the rising cost. "The ledger is already the mechanism" — **confirmed for the record and the cost; refuted for the diminishing return, which needs one reading of that record inside the target's own decision.**

**Hoarding and the reason to have learned it.** Both hold, with one code fact behind them: the NPC-side press is not opportunistic. An NPC can only form a Candidate about F's subject if it is a referent of a live question (`shape.py:3279`) — Q4 if the NPC's own want has the same subject (wants collide), Q2 if the NPC holds a `commit` to F itself (a shared fear, which is what a faction *is*). So NPCs press fears exactly when their interests touch them, which is when they should, and never as inventory.

**The eligibility answer.** Knowing a fear makes **no new verb available and no new eligibility kind** — every relevant verb is `own` (`verb_table.yaml:448-457`, `:475-489`, `:531-539`). What it makes available is a **subject**: `tell` with subject F is gated by `own_ledger` of F (`:478-482`) — you cannot tell what you do not hold; `speak`/`utter` about F are formable only if F is in a question's referents for an NPC, or in what the player holds. **The knowledge is the referent, and clause 3 of `opening_set` is the gate** (`shape.py:3234`). That is the whole answer, and it is cheaper than the question implied.

---

## PART 4A · Fears (REVISED) — replaces the three-claim adjudication

1. **Pursued vs prevented.** Holds, as a polarity of one carrier: OUGHT(P, `value=False`) is satisfied by default and boosts only when P's *precursor* lands — fears must name the precursor (fear the case, not the sentence), which is authoring, not mechanism. It never terminates unless its owner `repudiate`s it, which is the terminus above.
2. **Specific, same carrier.** Holds; `value=False`, no new mood, Q4 already reads it. Inert without O-3.
3. **Leverage inside the target.** Holds, *and is pressable*: each press is a new witnessed claim; the returns change on three reads (his ledger, the log, the hearers' ledgers); the terminus is his own `repudiate` or his own drastic act about the feared thing. Wrong in the original message on one point: retaliation at the presser is not reachable without a live edge or a Q2 widening.

**Unchanged from before:** ambitions and fears share one carrier; zero new primitives; the one bound is that a want or fear must be expressible in the seven `requires_forms` (`rosters.yaml:782-818`) to be evaluable, and an eighth form is a design change I name and decline.

### Critical Files for Implementation
- `/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/shape.py` — `questions_for` Q2/Q4 (`:3893-3937`), `score` (`:3494-3516`), `claim_subjects` (`:4133-4205`), the deposit (`:6319-6346`), decay (`:5458-5488`)
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/rosters.yaml` — `alignment` (`:877-938`), `claim_subject_rules` (`:250-303`), `claim_sources` (`:112-119`)
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/verb_table.yaml` — `speak`, `tell`, `utter`, `repudiate`
- `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md` — Fig. 26's four conjuncts and the *unrepeated* cardinality form (`:137-199`)
- `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/04_VERBS.md` — the `speak` row and its bands (`:58-80`)