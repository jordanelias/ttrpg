# Social contest: equivalences, conflicts, and a distillation

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

Reads `2026-10-30-social-contest-primitives-and-kinds.md` (cited as **PK**, with its `R-n` and `S-n` ruling
numbers and its §numbers). Method: CLAUDE.md §0's five-step ladder for every conflict (superseded; irrelevant;
answered by a design document; answered by precedent; answered by what the architecture needs), applied in that order
and led by Jordan's rulings; `skills/ners`' meta-rule for the distillation (a remedy that adds a system has failed;
the target is deletions that leave the vocabulary shorter). Every proposal is an edit to an artifact that exists. The
mappings in §1 are my reading of PK; the "stale" and "retracted" statuses are the extractions' reports and were not
re-opened.

---

## 1. Equivalences and duplications

Each row is one thing under several names. "Owner" is the one that survives under the rulings; "fold" is what
becomes a synonym or is deleted.

| # | the one thing | names in the corpus | owner (and the ruling that picks it) | fold |
|---|---|---|---|---|
| E1 | **the resolver** | v30 exchange algebra; kernel `Bout` with Persuasion Track; live one-draw; proceedings "serial acts, one draw each" | one draw per act, pool against obstacle, `degree_from_net` (R-5, R-6, R-22). The live code and the proceedings design are already the same engine | v30 algebra (prose, no engine, quarantined); kernel track and bands |
| E2 | **the ladders** | stasis (4, kernel 6); "issue ladder"; "charge ladder" (6 rungs); Aristotle *Rhet.* III.15 descent; Lausberg fallback; frank-speech gate; 15-step recoverability table | two objects, both ordered rungs in data: a **ground** ladder (what the question is) and a **concession** ladder (how much is admitted). The audit already found "three ladders, same shape" | the shared name "issue ladder" for two things; kernel's six-ground version |
| E3 | **genre** | genre; tense; matter mood (HOLDS / OUGHT / neither); function of the stasis ground; Memory/Projection (kernel) | **matter mood** is the one axis; genre is its derived word (`00_DERIVATION`, PK §3). Forensic = HOLDS, deliberative = OUGHT, epideictic = neither | genre as a field; kernel's two-genre compression |
| E4 | **burden** | burden token; win-condition; biased track start; halved resistance | one: who must make their act succeed for the matter to move. The audit named "three encodings of one thing" | track start 6; "halved resistance" |
| E5 | **standing** | kernel 0-10 per contest; upstream 0-100 per (actor, body); A1-A4; Face; Reputation; Disposition; "impression"; attribution (CIP-12); armature | a **Query over stances and the ledger**, never a stored number (S-7). Three "second currencies" were never reconciled; none needs to exist | both numbers; Face, Rattled, Doubt Marker; the three currencies |
| E6 | **the audience** | five fragments: dead resistance, Room, Pressure.public, crowd-as-Panel, unconsumed faction boost; floor; reception; bench | three **derived** sets (parties, bench, floor) from edges (R-12, R-20) and one **reception** term read from the ledger (ED-SC-0040, option B) | the five fragments; adjudicator "types" |
| E7 | **a plural decision** | panel ballot; jury vote; `VoteAtClose`; Mandate-weighted faction vote; coalition vote; live-commit tally (CR-34); licence by count; Althing cascade | **one count over `commit` edges against a threshold, as a Query** (R-18 aggregates are Queries; R-29 licence) | five tallies and three ballots |
| E8 | **the move roster** | kernel moves (claim, present proof, question, rebut, shift, support, advance, hard); speech kinds (6, 10, 12 or 15); Nyāya forms; study's 27 figures; `persuade` | one **data roster of speech kinds** with aptness per row (R-16). `hard` is byte-identical to `advance` after its gate (audit F9) | kernel move enum; `hard` |
| E9 | **recoverability of failure** | `stakes_grade`; Terminal Doubt; Fig. 11/21; S7 failure classes; failure severity by observer set; 15-step table | derived from what the disposal writes (oblige, detain, ban) and who learns it (R-21); the key `stakes_grade` is already scheduled for deletion | four of the five names |
| E10 | **evidence** | kernel dossier with hidden weights; `proofs` key; `Record` with `forgery_quality`; claims with `confidence` | claims in the ledger carrying confidence, and Records for the documentary kind (S-5); `proofs` is what was told in the room | the dossier object |
| E11 | **the same proceeding, many names** | kernel: formal/grand contest, royal audience, church tribunal, guild arbitration, casual dispute, private negotiation, personal appeal. Library: court, disputation, assembly, appeal, fused arbiter, deliberative body, scholastic disputation, public oration, inquisition hearing, excommunication court, imperial petition, secret council, memorial remonstrance. Arrangements: the eight seeded rows | the arrangement rows. `church_tribunal` ≈ `tribunal` ≈ `inquisition_hearing` ≈ `excommunication_*`; `guild_arbitration` ≈ `arbitration`; `assembly` ≈ `parliamentary_debate`; `deliberative_body` ≈ `council_of_state`; `private_negotiation` ≈ `negotiation`; `royal_audience` ≈ `audience / embassy`. The kernel's own 8 differ from each other in four things only (exchange count, verdict rule, judge profile, tribunal start) (#530 kinds report) | kernel presets (5 with no campaign caller) and the 13 library venues |
| E12 | **the debate** | live `argue` and `speak`; kernel bout; unbuilt nested run; "public debate" | the proceedings run. R-26 asks for the result at the seam, not a particular resolver | the kernel bout |
| E13 | **a parliament** | board-game vote with sanction ladder; kernel faction adapter; live Mandate-pool bridge; interim King-and-Regent bench; the council count | licence by count at four rungs (R-26, R-29), with the King-and-Regent bench as one seat's row | the first three |
| E14 | **a tribunal** | a contest proceeding; a single-roll excommunication action; a price-cap or charter-review instrument | one word per thing: the proceeding keeps "tribunal" | the other two get their own names |
| E15 | **a sitting** | `convene` Date; docket slot; "Hold Court" (five jobs); reasons to convene A to L | a `Date` that forms a docket slot, filled by `open_case` | "Hold Court" |
| E16 | **seat conferral** | confer / determine / succeed; appointed / elected / annex | the closed set ED-IN-0256 | the three-verb set |
| E17 | **record** | `Record{status, citableAs}` in two upstream documents; `LedgerTag`; case file; docket item | the existing engine `Record` and `DocketItem` | the upstream duplicates |
| E18 | **verb renames** | `persuade` = `argue`; `lodge` = `carry`; `declare` = `utter`; `vote` = `commit` count | R-06 of verbs-11: `utter` stays; its own override withdraws `declare` | `persuade`, `lodge`, `declare`, `vote` as proposals |

## 2. Conflicts, and how each reconciles

Ordered by whether a ruling decides it. "Step" is the ladder step that answers it.

### 2.1 Decided by a ruling (no question for Jordan)

| # | conflict | decided by | reconciliation |
|---|---|---|---|
| C1 | kernel track and bands against one ladder | R-5, R-6 (step 3) | one ladder. The track, its bands (`A_total` … `B_total`, `committee`) and `narrative.summarize`'s band labels die with the kernel. #530 found the track's decisiveness accidental (verdict bands are fixed gap sizes against a gain that varies about 5×), so the loss is free |
| C2 | tribunal asymmetry (84:16 from the start of 6; "halved resistance" never plumbed) against obstacle = defender's score ÷ 2 | R-5 (step 3) | the obstacle is derived from the defender; the start is deleted. The tribunal's tilt, if wanted, is a `proofs` or `order` value on its row, not a number |
| C3 | stored `Standing` / Face against derived aggregates | S-7 (step 3) | derived. Resolves E5 |
| C4 | aptness refused (older text in `03_PARAMETERS`, `06_RESOLUTION`) against priced | R-16 (step 1: superseded) | priced. The older text is stale |
| C5 | latitude in the pool *and* the obstacle (older text) against pool only | R-18 (step 1) | pool only; obstacle keeps four room terms. The count "five terms" is the older text |
| C6 | public debate as a twelfth game against a degenerate case | R-21 (step 1) | degenerate case (`14` is later than `07`). Eleven games plus one |
| C7 | "appeals should not be a thing" (R-2) against the `appeal` row | R-35, Jordan 2026-10-30 (step 3: a direct clarification) | R-2 barred contesting a rendered outcome **immediately** ("let the decision ride"); an **appeal to an authority is wanted**. Both hold: (a) a rendered outcome cannot be re-docketed before the same bench at once; (b) `appeal_basis` names the *other* authority (R-34: e.g. church to crown, a lower rung to a higher) to which a petition may be carried, and the first outcome stands until that authority disposes. So `appeal` is a **route** (a petition to another authority, bounded by the depth cap that already runs), not a retry and not a game of its own. `appeal_basis: none` is correct where no other authority exists (guild arbitration, a sovereign) |
| C8 | kernel: adopt, retire, or "evaluated, not deleted" | R-14, a direct quote (step 3) | retire. SC-05 records the "adopt" lean as indirect ("a lean, not a ruling"), and a direct quote outweighs an inferred lean. Only the *timing* is open, and the plan already treats it as a scheduling call (A1-58). `CURRENT.md`'s Social-contest row still lists the kernel as a head; that row is the artifact to edit |
| C9 | "everything in a scene binds" against one-tick trials (D-8, P-14) | R-11 (step 3) | the ruling wins. A trial that finishes in one tick still binds, since its disposal writes a Tenure. The "re-examination" ED-SC-0038 owes is one row stating this; no escalation |
| C10 | auto-resolve and played as two fidelities of one conflict | R-24 supersedes R-4 (step 1) | non-player contests take the module's automated path; the container is for the player's. The `E[auto] ≈ E[played]` residual died with its subject (ED-SC-0011 closure) |
| C11 | genre kept (CR4, CR5 depend on it) against genre dead (audit 04) | E3 and C8 (step 2: irrelevant) | CR4 and CR5 are kernel-era; with the kernel retired they have no consumer |
| C12 | `Standing` shown as a band (COMP S6) against never show a band (PS 15) | S-7 with §C.11's explanation contract (step 3) | show the character's own holdings and their arithmetic, never the engine's roll internals (obstacle, margin, band). The player sees an estimate, never the true aggregate |
| C13 | Layer 1 `04` §B.2:250 against `reception` and `proofs` reading other persons' ledgers | CLAUDE.md §0.05: a spec is not edited to fit code (step 3) | already taken as option B (re-source from commits). Correct the stale line in `HANDOFF_SC.md` that still calls it Jordan's |
| C14 | `"a matter"` new (08) against already in `rosters.yaml` | the code (step 3) | the code governs; 08's Part B premise is stale. Same for the dispatch (`contest.py:243` deleted the hard-coded branch) |
| C15 | arrangement keys 13, 14 or 15; games 12, 11+1 or 13; speech kinds 6, 10, 12 or 15; obstacle terms 4 or 5 | the loader and `roll.py` (step 3) | the counts are what `data/arrangements.py` and `obstacle()` load: 13 keys, 6 speech kinds, 4 room terms. Delete the others from the prose |
| C16 | church-tribunal share 84.2, 84.5, 84.7% | irrelevant (step 2) | three commits, one retired kernel |
| C17 | warrant × attack matrix: authored, retracted as fabricated, replaced by schemes conditional on an unrun sweep | the retraction (step 1) | retracted. Undermine / rebut / undercut survive as three speech kinds in the roster (E8); the schemes wait on a sweep that is not scheduled and nothing depends on them |

### 2.2 Needing the architecture's judgment (step 5), taken here

| # | conflict | the call | revert |
|---|---|---|---|
| C18 | `ground` ladder: four grounds (04) against `consequence` and `feasibility` as start grounds (00) | four. Deliberative argument does not run on stasis (Heath; the proceedings design gives OUGHT matters no ladder), so consequence and feasibility belong to OUGHT motions as strain queries, not to a ladder | none needed; nothing reads the extra grounds |
| C19 | forum shopping added (00) against already foreclosed by canon (04) | foreclosed. Which bench hears a matter follows from `bench_basis` and `venue_min_rank`; a forum challenge (*translatio*) is a speech kind at the issue rung, not a chooser | restore if a ruling opens it |
| C20 | the armature hidden-vector merged into `Adjudicator.character` (04 K3) against "do not abandon" (04:332) | merge into the judge's convictions. The proceedings design already derives the bench from persons and gives them the thirteen conviction axes (H-46) | none |
| C21 | "Stage 4 four games" (`HANDOFF_SC`, `CURRENT.md`) against the CIP programme | the plan. `HANDOFF_SC.md` and `CURRENT.md` name the live plan; the CIP programme was a proposal | none |
| C22 | the position of the two held parliament calls (RH-1, RH-3) | keep held. Both are Layer-1 hunks; not an architecture choice to take | n/a |

### 2.3 What survives all five steps (for Jordan)

Two items survived the ladder; Jordan has since answered both. **The ceiling** (M-7, corrected below): above the default (R-37). **R-31 against Layer 1 §A.3**, below it: office licenses and weighs (R-31), on both roll and obstacle (R-38). What remains for him is a measurement choice (M-7's scope) and the Layer-1 wording.

**M-7. [CORRECTION: this section first called the remedy open; it is not.]** R-8 (2026-08-27) accepted "if you
don't have enough dice you don't have enough dice"; R-18 (2026-09-06) asked "don't deprive player of a chance at
winning". M-7 was run and failed at the 1D floor. The code already chose a remedy: an **obstacle ceiling** (`H-213`,
swept; shipped value 2; `modules/social_contest/roll.py` docstring, "Contradiction 3 of the proceedings
reconciliation, resolved"), explicitly "NOT a pool floor". The ladder answers the choice (step 3, a design
document and the code), so it is not a question for Jordan. What survives is narrower and was found by the code audit:
the ceiling's value equals the default obstacle (2), so for any opposition over 4 the obstacle is the same 2 as no
opposition at all, and a hostile room cannot raise a defaulted obstacle. R-5 asks for "score ÷ 2 plus modifiers"; at
ceiling 2 the score term and the room's hostile half do no work in live play (see the code audit, finding B-11).

**ANSWERED (R-37, Jordan 2026-10-30): "Ceiling should sit above the default so opposition can bite."** The value is
not stated (`H-213`: "No ruling states the value"; its sweep is 1, 2, 3, and `None` is the uncapped arm). The cost is
measured, not guessed. `sigma_leverage.p_success` (I ran it) for pool × obstacle:

| pool | Ob 2 | Ob 3 | Ob 4 | Ob 5 | Ob 6 |
|---|---|---|---|---|---|
| 1D | .0228 | .0006 | .0000 | .0000 | .0000 |
| 2D | .1444 | .0259 | .0023 | .0001 | .0000 |
| 3D | .2819 | .0970 | .0217 | .0030 | .0003 |
| 4D | .4013 | .1908 | .0668 | .0168 | .0030 |
| 5D | .5000 | .2881 | .1318 | .0468 | .0127 |

So a ceiling of 3 (the sweep's third arm) lets opposition bite but fails M-7 for a **1D** party (0.06% at Ob 3). The
default pool is 2D and R-31 gives persons more dice, so the 1D floor becomes the rare case that R-8 ("if you don't
have enough dice you don't have enough dice") already accepts. **R-39 (Jordan 2026-10-30) settles the scope:** "a 1D party is effectively useless and destined to lose. it's like
asking a murderer who says 'i love to murder and i murdered that guy' to defend himself in a court room." So the
1D-floor M-7 check is **withdrawn as a requirement**: R-18's "chance at winning" belongs to a party with dice to bring,
and a floor-pool party against strong opposition is correctly lost. The 2D default at Ob 3 (2.6%) is then a floor of
plausibility, not a protection. The murderer's case is also an argument about *evidence*, not only dice: what is
already established against a party (his own confession, a proof he cannot mirror) is item 11's evidence channel, and
should weigh with the pool, not be a separate rule. The ceiling's value (3 is the sweep arm) remains Jordan's.
Changing `obstacle_ceiling` moves the goldens and is a behaviour change to be re-recorded plainly (CLAUDE.md §7); it
has not been made.

**R-31 against Layer 1 §A.3: ANSWERED by Jordan, 2026-10-30: it is both.** "A King has more actions that are
available in some contests (e.g. a royal tribunal), and their actions also carry more weight in those contests." So
office licenses acts **and** carries weight, both keyed to the venue. That settles the ruling and leaves the
amendment: §A.3 ("A seat adds no verb and no modifier"), its STRUCTURAL row (`04_CODE_ARCHITECTURE.md:351`), the
axioms table row (`01_AXIOMS.md:1635`), `06_RESOLUTION` B.0's refusal and the loader's refusal of a `capability`
eligibility kind are all contradicted by it. Layer 1 is not edited by an agent to fit a ruling given in conversation
without his say-so on the wording, so the amendment is held as a hunk (the same status as RH-1 and RH-3).
*A narrow wording that keeps §A.3's concern* (that a seat which carries a modifier everywhere becomes a stat to be
optimised) *is to put the weight in the venue row, not on the office*: "a seat adds no verb and no modifier **of
itself**; a venue may license an office-keyed action set and weight". Then a King is weighty in a royal tribunal
because that row says so, which is also what R-12 asks (every difference lives in the row). This is my suggestion, not
a ruling.

The record of the original question, for the trail: R-31 (2026-10-30, newest) names *office* among the sources of capability.
`architecture/meta/03_VERBS_AND_LOOPS.md` §A.3 says "A seat adds no verb and no modifier"; `04_CODE_ARCHITECTURE.md:351`
makes it STRUCTURAL (no bonus field, no modifier column, the loader raises on a `capability` eligibility kind); and
`06_RESOLUTION` B.0 refused an office bonus on that ground. A newer ruling outranks the older proposal text, but a
spec that binds code is not edited to fit (CLAUDE.md §0.05), and the Layer-1 hunks are held for his sign-off. I took
the reading under which they agree, **office licenses which acts a holder may take and who is heard** (its
`remit_acts`, which the code already honours), **while attribute, title and faction supply the numbers**, and marked
it an assumption. The question: *does R-31 mean that, or does an office carry a numeric modifier, in which case §A.3
and its STRUCTURAL row are amended?* Everything in §3.1 items 10 to 12 holds under the first reading.

Questions that were already open and are untouched by this reconciliation: J-C-6 (may a person lie), D-7 (detailed
denial; displayed anger), the source of risk appetite and horizon.

---

## 3. Distillation

### 3.1 The model the rulings already imply

Read in order, the rulings fix nine things. Nothing else in the corpus is required.

1. **One engine.** An act is one draw: pool against an obstacle, `degree_from_net`, four bands. Partial writes a docket matter (R-5, R-6, R-17, R-22).
2. **One host, many rows.** A proceeding is an arrangement row; every difference between games lives in a key (R-12).
3. **Three derived sets.** Parties, bench and floor, from edges, plus one declared key: `disposal` ∈ {bench, mutual, none} (`00_DERIVATION`; R-20).
4. **One count.** Every plural decision is a count over `commit` edges against a threshold, as a Query, licensing or blocking the owner's own act (R-18, R-29).
5. **One matter axis.** The matter's mood (HOLDS, OUGHT, neither) derives genre, ladder and disposal (R-21, `14`).
6. **One speech roster.** A data roster of speech kinds with aptness priced per row (R-16).
7. **One reception.** The audience's reading of the speaker's ledger replaces every stored credibility number (S-7, ED-SC-0040).
8. **One disposal vocabulary.** The existing Tenure kinds, Record, licence, seat conferral; no new verb (R-18, R-29, R-21).
9. **One propagation rule.** A result is a fact, witnessed, read at the speed of news; a reaction must exist (S-3, S-6, S-7).

### 3.1a The three requirements of 2026-10-30 (R-31 to R-33), as model items

10. **Capability = attribute × title × office × faction, set by venue and contest type** (R-31). Attribute gives dice; title gives rank in the ladder and so standing; faction gives alignment and the audience's disposition; office gives **both** the licence to act (`remit_acts`, who is heard) **and weight**, each keyed to the venue ("a King ... in a royal tribunal", Jordan 2026-10-30). Where the weight enters (pool, leverage, obstacle) is item 11's per-source choice; **R-38 (Jordan 2026-10-30): the weight can affect both the roll and the obstacle.** The two sides are the actor's (a King's own roll carries his office) and the defender's circumstance (an office-holder is harder to move: the obstacle presented to whoever contests him), so item 11's per-source rule holds: an actor's advantage goes to the roll, a defender's circumstance to the obstacle. The resolution-diagnostic skill's objection (advantage is never an Ob reduction) is not breached, since the obstacle term here *raises* the defender's difficulty and is not applied as the actor's advantage. The weight is a venue-row value keyed by office, not a column on the office. The venue row decides which of these the contest reads, so a trial, a council and an embassy draw on different combinations of the same four sources. **Not** a per-proceeding skill (B.0's refusal stands: that branches on the game's name). Latitude stays pool-only (R-18). The attribute roster is in flux (ten ruled, nine shipped, the tenth unnamed); the reading must go through whatever the roster is.
11. **One sigma-leveraged engine, continuous in dice and obstacle, with named modifier sources** (R-32). Channels: **pool** (capability, item 10), **leverage** (a μ-shift on the roll), **obstacle** (the defender's score ÷ 2 plus room terms, R-5). Sources: capability; worldly state (what the matter's referent now is); evidence (`proofs`); argument (the proposition's content and its aptness, priced per R-16); audience (reception); forgery quality. Every source maps to exactly one channel, once. The repo's own resolution-diagnostic skill holds that advantage is a μ-shift and never an Ob reduction; R-5 and the 2026-09-06 direction ("I'm fine with Ob being modified by things") allow terms on the obstacle. The two are reconcilable only by deciding, per source, whether it is the defender's circumstance (obstacle) or the actor's advantage (leverage).
12. **One action surface, limited by contest type** (R-33). The same verb table and speech-kind roster serve every structure (dyadic, mutual, bench, count); the arrangement row decides which actions are *available* in it, through `floor` (who may act), `order` (when), `proofs` (what may be offered), `interposed` (who may act for whom), and the speech kinds' `apt_genre` / `apt_rung` / `reachable_bands`. This is the "consistent armature". It must not be confused with the kernel's `armature` (a hidden judge-conviction vector), which is a different object and dies with the kernel.

13. **Authority: where a venue's decision gets its force, and who may adjudicate** (R-34, Jordan 2026-10-30). Three bases, each with its own source of imbalance: **between the parties** (negotiation: no one sits above; the imbalance is the difference in rung position and the circumstantial leverage each holds); **the polity** (a royal tribunal or parliamentary proceeding: royal, imperial or political authority vested by the nation); **the church** (a religious tribunal or heresy charge: authority from a religious basis). Authorities are not independent: royal authority **modulates or undermines** religious authority when a royal person is involved. The adjudicator is an actor holding an office **relevant to that authority**. In the model this is the content of the row's `disposal` (`mutual` is the first basis; `bench` the other two) and of `bench_basis`, which today names a remit act and is unread; it needs to name the authority, so that the bench is the set of persons holding offices of that authority, scoped to the venue. The precedence between authorities (crown over church when a crown-holder is a party) is a row-level rule, not a branch. `offices.yaml` already ties each seat to a `body` or a `faction` (`Crown`; `Holy See`, `Cardinal of Justice`, `Church of Solmund`, …), so the tie exists in data in two spellings. `[ASSUMPTION; medium: the mechanism of "modulate or undermine" (the crown joins the bench, may revoke, or raises the church bench's obstacle) is not stated by Jordan; the outcome is.]` Historical support in the repo's research: Clarendon 1164, criminous clerks and benefit of clergy, interdicts (Innocent III; Venice 1606), the Council of Constance, the Cadaver Synod.

13a. **The authority's weight depends on its legitimacy in the venue's territory** (R-36, Jordan 2026-10-30). Political legitimacy for the crown, religious piety for the church, each *as held in the territory where the proceeding sits*. A territory that gives little weight to the Church of Solmund does not tilt a heresy proceeding toward the church; the authority's weight (item 10's office weight, and the tilt the kernel hard-coded as the tribunal's start) scales with the local standing of the authority. Two consequences for the model. (1) The standing is a **Query over the persons in the territory** (their stance toward the holder or the doctrine), never a stored territorial number: S-7 forbids a magnitude carrier, and the engine already refuses a Rung any social aggregate (`state/carriers.py:1103`, S10.1: "a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy"). (2) The same Query serves negotiation's two imbalances, but from the other side: rung position is rank (item 10, title) and circumstantial leverage is worldly state (item 11). `[ASSUMPTION; medium: weight × local legitimacy, with weight tending to zero, not below it; Jordan did not say whether a hostile territory tilts the proceeding *against* the church; revert: floor at zero is dropped]`.

11a. **The pool is a total over many sources, and a normal pool is 5D or more** (R-40 and R-41, Jordan 2026-10-30). What a party brings to a contest is the sum of its capability (item 10), its argument, its evidence, its leverage, its standing and so on (presence and charisma are not a separate source: Jordan, R-41, "that's capability", the attribute part of item 10); "it should be very difficult for a character to have less than 5D", and a total of 1D means "something has gone very wrong ... they probably deserve the outcome". This fixes the scale the rest is tuned against. It does not contradict R-38 or the obstacle terms: **what a party holds goes to its own pool; what stands against it (the opponent's score ÷ 2, a hostile room, proofs the opponent holds) goes to the obstacle**, which is item 11's per-source rule stated for both sides. At 5D the roll behaves as designed (`p_success` .50 at Ob 2, .29 at Ob 3, .13 at Ob 4, .05 at Ob 5, .01 at Ob 6), so a ceiling above the default lets difficulty differentiate among competent parties instead of among the doomed. The live default of 2D is a placeholder for a sum nothing yet builds (audit §4).

### 3.2 Eight kinds become four

PK §3.1 lists eight kinds. Under the model they reduce to four values of `disposal` and the *cardinality of the
bench*; the other four were never different structures.

| structural kind | `disposal` | folds in | what differs inside it |
|---|---|---|---|
| **dyadic** | none (the target is the hearer) | K1 influence; K7 display (the audience as hearer) | which claims or pursuits move; reception |
| **mutual** | mutual (the parties) | K2 negotiation | mandate; `commit` then `give` |
| **bench** | one third party | K3 adjudication; K4 petition (the bench is unbound, so the row says `appeal_basis: none`) | burden, proofs, order, appeal basis |
| **count** | a bench with more than one seat, by count | K5 panel and jury; K6 deliberation (bench = floor) | threshold, quorum, whether members are also parties |

K8 (contests over the forum, the jurisdiction, enforcement) is not a kind. It is a **matter type**: the same four
structures with a seat, a jurisdiction or an order as the matter instead of a person's conduct.

### 3.3 What is cut, and what dies

Graded as the NERS method grades a cut: for each, the possibility that would be lost, and whether something already
ruled in provides it.

| cut | what could be lost | already provided by | verdict |
|---|---|---|---|
| kernel `Bout`, track, bands, styles, interactions, armature, Pressure, Face, Doubt Marker, CR4, CR5, Appraise | the *feel* of eight differentiated proceedings | rows differing in `disposal`, `order`, `proofs`, `appeal_basis`; #530 showed the eight differ in four accidental things | **free** (R-14) |
| kernel faction adapter, outlawry .60, sanction ladder, coalition vote | faction-level parliamentary politics | licence by count at four rungs (R-26, R-29) | **free** once the rungs exist; until then they are the only thing that runs, so retire in the order the plan already gives |
| 13 library venues, 5 unused presets, 3 scaffold modes, stub games | variety of institutions | data rows, one per institution that has a source; research supplies them (§3.4) | **free** |
| v30 prose algebra | none (no engine) | n/a | **free**; already in `.designs/` |
| `genre`, `stakes_grade`, `registers`, `verdict_reasons` as fields or keys | none | derived (E3, E9); three already scheduled for deletion | **free** |
| the 45-primitive presentation, M1-M14, the upstream state graphs | a vocabulary | this file's nine-item model; the audit's own "do not adopt" tier | **free** (a presentation, not a mechanism) |
| proposed verbs `persuade`, `declare`, `lodge`, `vote`; sc05's CP-T05-01..03 and 05 | none yet | `argue`, `utter`, `carry`, `commit` count | **free** pending a draw they cannot make |
| numbers: 0-10 and 0-100 Standing | the player's sense of rank | a Query over stances (S-7) | **free** *only if* the Query exists; until then standing is the one place the cut costs something |
| the Persuasion Track as a visible gauge | a legible score during a debate | the character's own holdings (C12) | **costs**: the live roll shows no progress between acts. This is the one cut the corpus did not answer |

The last two rows are where the distillation could fail the NERS test. If the stance Query does not exist when the
numbers go, there is no standing at all; and if the track goes, a long debate has no visible middle. Both are
sequencing questions about when to cut, not about whether.

### 3.4 Unify the vocabulary

PK §6 found "kind of contest" used at four levels. Fix four words, and only two of them are code objects:

| word | meaning | a code object? |
|---|---|---|
| **verb** | what a person does (a row of the verb table) | yes |
| **row** (arrangement) | where and how it is done; 13 keys | yes |
| **matter** | what is before the room (a docket item with a mood) | yes |
| **structure** | dyadic / mutual / bench / count (§3.2) | no: a classification of rows by `disposal` and bench cardinality |

"Proceeding", "game", "venue" and "mode" then mean *row*; "genre" means the derived word for mood; "kind" is retired
in favour of *structure*.

### 3.5 Make the research a supplier of rows, not of mechanisms

Under R-12, every institution in the research becomes at most one row, and a row is filled from the sources' own
pattern: `disposal`, `bench_basis`, `floor`, `order`, `proofs`, `appeal_basis`, `interposed`, `disposal_reach`. Where
the sources give a stage-by-stage procedure (the 1268 election; the Roman *relatio / sententiae / discessio*; the
*ordo iudiciarius*; the Althing cascade), the stages are the row's `order` and `proofs`. Where they give only
offices and outcomes (most of the Venetian and Inquisition material), the row is thin and should say so, because the
research does not support more. The influence-psychology studies (central and peripheral routes, the story model,
reactance, anchoring) become **reception terms and speech-kind aptness**, not a second engine: they are the
justification for which kinds are apt before which audience, and the corpus has no mechanism for them.

### 3.6 Purify the documents

Four classes, and a document should be one:

| class | what it is | where it should live | present state |
|---|---|---|---|
| rulings | what is fixed | the ledgers, and `references/design_rulings_2026-09-06.md` for the verbatim ones | scattered across five ledgers and a dozen proposals; the SC ledger holds 5 rows because the real ones are in the archive |
| code | the mechanism | `modules/social_contest/`, `engine/season/` | one roll and five verbs |
| rows | the data | `engine/season/arrangements.yaml` | 8 rows, 13 keys, one key read |
| reference | everything else | `proposals/`, `.designs/`, `.audit/`, `research/` | about 500,000 words, many with inline retractions |

---

## 4. Edits that carry this out (each to an artifact that exists)

None adds an object, a store, a guard or a document.

1. **`CURRENT.md`, Social-contest row:** remove the kernel as a second head; name the proceedings successor and the live module. (C8)
2. **`registers/handoffs/HANDOFF_SC.md`:** correct the ED-SC-0040 line (closed by assumption, not Jordan's); name the one open question (§2.3). (C13)
3. **`references/module_contracts.yaml`:** correct the kernel row that says it is "reached live only via `emergency_council`". (R13)
4. **`proposals/2026-09-05-proceedings-subsystem/`, `03_PARAMETERS.md` and `06_RESOLUTION.md`:** delete the pre-R-16, pre-R-18 text (aptness refused; latitude in the obstacle); delete the 14- and 15-key counts and the "five terms". (C4, C5, C15)
5. **Same directory, `07_THE_GAME.md`:** the twelve-games statement, to eleven plus one. (C6)
6. **`registers/editorial_ledger_sc.jsonl`:** one row recording C7 (appeal is a route to another authority, R-35; no immediate re-contest, R-2) and C9 (one-tick trials bind), answering ED-SC-0038's owed re-examination. This is the one ledger row proposed, and it needs no ruling: both answers are already given.
7. **Kernel retirement:** no change to the plan's scheduling; once the kernel is removed, E11, C1 and C2 are moot.
8. **The stance Query behind standing (S-7)** and **a visible middle for a long debate (the last row of §3.3)** are the two things the cuts depend on; they are listed so the order of cutting is not chosen by accident.

## 5. What this does not do

It does not choose the ceiling's value (3 is the sweep arm; Jordan has said only "above the default"). It re-runs one measurement, the success-probability table in §2.3. It does not test whether the
four-structure reduction survives a NERS pass on the player half of R (is each structure playable at a seat a
player occupies?); PK §3.2 found that the season loop reaches only dyadic influence and a thin edge of adjudication,
so the player-facing half of the other three is untested by anything that executes.
