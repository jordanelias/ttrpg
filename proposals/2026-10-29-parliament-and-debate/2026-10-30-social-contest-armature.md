# Social contest: the armature, and one scale for its influences

## Status: PROPOSED (reference; resolves nothing)

Producer's draft for one adversarial pass. Reads, in order: `2026-10-30-social-contest-primitives-and-kinds.md`
(**PK**; its `R-1..R-41` and `S-1..S-8` are cited by number and outrank everything here),
`...-reconciliation-and-distillation.md` (**RD**), `...-code-audit.md` (**CA**), `...-how-contests-occur.md` (**HO**),
`...-unification-plan.md` (**UP**), and the code and research cited at their lines. Every engine figure below was
computed by me with `engine/dice_engine/sigma_leverage.py::p_success` at this checkout. Canadian spelling.

---

## A. The armature on one page

**A contest is a venue row, a matter and a sequence of acts. Each act is one draw. Draws move what persons hold;
persons decide by their own act; the row says whose decision counts and who learns it.** Nothing else is structure.

1. **The row** (`engine/season/arrangements.yaml`; R-12, R-15) names the **authority** the venue's force comes from
   (the parties, the polity, the church; R-34), the **decider** (the target, the parties, a bench of that authority's
   office-holders, or a count), the **acts it admits** out of the one verb table and speech-kind roster (R-33), the
   **weights** it gives seats and titles (R-31, R-38), its **reach**, and its **appeal route** to another authority
   (R-35). A kind of contest is a row; no row is a branch.

2. **The draw** is the one σ-leveraged continuous roll (R-5, R-6, R-22, R-32). Each influence enters once, through
   one of three channels, by **whose fact it is**:
   - **dice**: what the actor holds (capability, its conduct half multiplied by latitude; title; his seat's weight in
     this venue times the authority's local legitimacy; faction backing where the row keys it; evidence held);
   - **obstacle**: what the other side holds, as **its score ÷ 2** (R-5), plus the act's or the document's own terms
     (aptness, R-16; forgery quality; the default where nobody resists);
   - **leverage** (σ, a μ-shift, soft-capped): what holds **between** actor and decider now (reception, argument fit,
     circumstantial leverage).

   The common scale is **the expected margin in net successes**, the unit `degree_from_net` grades:
   `E[m] = 0.4·N + 0.8·√N·softcap(s) − Ob`, spread `0.8·√N`. One Ob point is one net success, 2.5 dice of mean at
   every pool; one σ is `0.8·√N` Ob points. At the 5D reference (R-40) one die ≈ 0.25σ ≈ 0.4 Ob.

3. **The decider** acts by its own verb: the target's claims or pursuits move (dyadic); both parties `commit` or
   there is an impasse (mutual; R-1); a seat-holder of the row's authority chooses a disposition and `determine`
   grades it by a draw of its own (bench); members' `commit`s are counted and license or block the owner's own act
   (count; R-29). Advocates never write into a decider (R-19, R-23): their draws move what he holds, and **his own
   choice reads it**. Fears, wants and convictions act there, never as modifiers.

4. **The world learns it** (R-21, S-3, S-6, S-7): a Tenure edge, a Record or a licence, witnessed, spreading at the
   speed of news; Partial leaves a matter on the docket (R-17). The outcome rides; an appeal is a petition carried to
   the authority the row names, never a retry before the same bench (R-2, R-35).

**Off the scale** (§D.3): will; the licence to act (a gate); burden (a default, not a size); truth itself; an
authority's availability and enforcement (later acts); a discovered lie (a Record); and any effect whose size the
evidence does not support (a sweep with a control arm, inside the σ channel's shared cap).

**Today** (§F): one integer roll at 2D against Ob 2 for nearly everyone, leverage hard-coded 0, no row key changing
any outcome, and no channel from a speech to a determination.

---

## B. The adjudication ledger

The ladder is CLAUDE.md §0's: (1) superseded, (2) irrelevant, (3) answered by a design document, (4) answered by
precedent, (5) answered by what the architecture needs. Rulings lead, newest governing where two speak to one
thing. "Step" names the rung that decided it.

| # | idea or conflict | verdict | ground (step) | ruling or source |
|---|---|---|---|---|
| B1 | **UP §1: a new data roster of contest sources, each with a `side` declared once** | **CHANGE: keep the rule, reject the roster** | (a) it has two sides; the engine has three channels, and the roster omits σ, the one R-32 names. (b) Its own row list breaks its own rule twice: `standing` and `reception` are one fact (S-7); `capability.office` and `authority_weight` are one fact (R-36 scales the first). [CORRECTION after the critic: the first draft listed a third, `opposition_score` and `proofs_against`; in the plan `proofs_against` is the *actor's* proofs, which are evidence held (dice), so it is not the opponent's score. What moves is that the live code subtracts proofs from the obstacle and the actor's proofs belong in the actor's dice.] (c) The closed set of channels is already declared once, in code, by the fields of `SocialContestInput` (`queries/inputs.py:43-83`) and their composition in `roll.py:103-124`; a roster saying "side" beside that record is a second owner (§0.05 clause 3). (d) Its per-source `venue_key` duplicates the row (R-12). The remedy is field edits to the existing record, one producer per field in `sigma.py::contest_input`, and a weight column on the row (5). [CORRECTION after the critic: "three field edits" undercounts. At least: pool `int` to float (`inputs.py:79`, `sigma.py:131`); sigma producers; reception and proofs taken out of the obstacle; a new aptness field (none exists); `opposition` widened from one capability key to the full score; `roll_net` switched to the continuous roll (`roll.py:124`). And the record's fields are *operands*; which channel one reaches is set by the composition at `roll.py:103-105,124`, so "a fact enters once" remains a **discipline for the reader**, not a mechanism, unless a named observable catches a breach.] | R-5, R-12, R-32; S-7 |
| B2 | which channel a source enters | **by whose fact it is**: the actor's holding → dice; the other side's holding → its score ÷ 2; a relation between actor and decider → σ; the act's or the document's own property → an Ob term | R-5 fixes the second, R-18 and R-38 the first, R-16 the act's term; R-40 lists leverage among the roll's sources; the σ layer is the ruled μ-shift (ED-884, ED-934 per `sigma_leverage.py:169-177`). The rule is mine, built so each ruling is an instance (5) | R-5, R-16, R-18, R-38, R-40 |
| B3 | reception and standing: an obstacle term (`06_RESOLUTION` §C.1; live `roll.py:104-105`) or the roll | **roll, as σ, signed, net of the decider's regard for the opponent** | R-40 (newer than both) puts standing among what a party brings (1). σ, not dice, because the fact is signed and relational and σ is the signed, bounded channel; `levels_to_net_sigma` (`sigma_leverage.py:224`) is the aggressor-minus-defender precedent (4). Also corrects a unit defect: live `reception` is a *sum* over bench members and deeds (`world_q.py:673-680`), so it grows with bench size; it should be a mean (5) | R-40; revert: reception stays the live Ob term |
| B4 | evidence: subtracted from Ob as "unmirrored proofs" (live), leverage (file 03 §1.1), or pool | **dice, per party, gross** | R-40 names evidence as a pool source (1). With each party's proofs in its own score, the live subtraction of "unmirrored proofs" from the obstacle (`world_q.py:733`, `roll.py:105`) moves to the actor's dice. [CORRECTION after the critic: the first draft said R-5's ÷ 2 *neutralises* a mirrored proof by arithmetic. It does not: `x` dice add 0.4x net, and `x/2` more obstacle costs 0.5x, so a mirrored proof costs the actor 0.1x. The live "mirror" is also a different thing: the opponent holds a claim with the same subject and predicate, i.e. he knows the charge, not that he has an opposing proof. Whether to keep any netting is open, for a reason other than arithmetic (5)] | R-5, R-40 |
| B5 | a fear pressed: a σ term on the presser's roll, or the target's own decision | **the target's decision; no modifier** | ED-SC-0035: "you can name what he dreads and his own decision procedure does the rest"; the presser's act is a draw on whether the claim lands (3) | R-19, R-23 |
| B6 | the judge's own belief on the matter: σ on `determine`, or the judge's choice | **choice**: belief picks the disposition; the `determine` draw grades its degree against the party's resistance | R-10 (a verb reads the degree from the scene); one fact, one place (5) | R-10, R-29 |
| B7 | the ceiling: R-37 "above the default" against R-8 "stop arbitrary fiat capping" once R-39 withdrew the M-7 ground it was built for | **escalated (G1)** | [CORRECTION after the critic: R-37 is not the newest (R-38 to R-41 follow it), and R-39 does not remove R-37's stated reason, "so opposition can bite"; the M-7 link was a gloss. R-8 comes from band de-saturation (ED-SC-0032, ED-PC-0057), not an obstacle bound, so "R-8 forbids a fiat cap" matches on a word. The governing ruling is (a), R-37: a ceiling above the default. Option (b), deletion, would AMEND it, and must also state the S27.4 consequence: with no ceiling an obstacle above `obstacle_refusal_multiple` (2) × pool is refused outright (`sigma.py:240-241,273-275`), against R-16.] Two options remain, different games | R-8, R-37, R-39 |
| B8 | integer pool (`sigma.py:131`) and the discrete `roll_net` path (`roll.py:124`) against "continuous dice and obstacles" | **continuous**: `roll_net_continuous` (`sigma_leverage.py:299`); remove the cast | R-32 (1). Dies with it: CA's finding that leverage below 1 is inert at an integer obstacle | R-32 |
| B9 | office weight against Layer 1 §A.3 ("a seat adds no verb and no modifier"; STRUCTURAL at `04_CODE_ARCHITECTURE.md:351`) | **R-31 and R-38 decide the substance; the wording is held (G2)** | §0.05: a Layer-1 spec is not edited by an agent to fit; it is the owner's to amend | R-31, R-38 |
| B10 | title and seat for a ruler (`off_king` has `post: "King"` and the title King: one fact, two spellings, `offices.yaml:183`) | **one weight per holder per venue: the larger of the row's weight for his seat and for his title** | double count otherwise (5) `[ASSUMPTION; medium; revert: seat only]` | R-31 |
| B11 | latitude "rank-derived" (PK §2.3) against a Query over `interposed` (`06_RESOLUTION` §B.1, `03_PARAMETERS:70`) | **the Query over `interposed`, multiplying conduct only, floored** | the design document (3); rank-derived would double-count title. Pool only (R-18) | R-18; ED-SC-0034 (3) |
| B12 | presence or charisma as a source | **the conduct half of capability, so it is multiplied by latitude** | R-41 (1); a written petition discounts charisma, which is the study's claim | R-41 |
| B13 | "the rung" as an obstacle term ("what is being asked for", `06_RESOLUTION` §C.1) | **cut from the obstacle; the size of the ask acts in the decider's choice** | "NO BASE Ob BY SCALE" (Jordan, 2026-09-05, carried at `roll.py:71`) (1); a bigger ask costs the decider more, which his choice already weighs (5). The cut is free | Jordan 2026-09-05 |
| B14 | "register fit" (`06` §C.1) and aptness (R-16) | **one term, aptness** | same fact (3) | R-16 |
| B15 | reception composed from "the hearers' convictions on this matter's axes" (`06` §C.1) | **convictions go to choice only; reception is regard for the speaker** | the decider's choice already reads his convictions; counting them in reception too is a double count (5) | R-23 |
| B16 | ethos, pathos, logos as fields | **no fields** (`06_RESOLUTION`); each is split across channels in §D | already ruled out as fields (3) | `06_RESOLUTION` |
| B17 | authority: `bench_basis` names a remit act; offices name `body` *or* `faction` | **`bench_basis` names the authority (parties, polity, church); one spelling of the office-to-authority tie** | R-34 (1); `offices.yaml` already carries the tie (4) | R-34 |
| B18 | how royal authority "modulates or undermines" religious authority | **by acts and data that exist, no new mechanism**: a royal party brings his office weight where the church row weights crown seats; the crown holds the secular arm (`arrest`, `seize`) without which a church `detain` is not executed; the crown confers and revokes seats (R-9); the church row's `appeal_basis` names the crown | every sourced case acted through those four routes and changed no rule of evidence or sentence (`research/social_contest_procedures/02_inquisition_heresy_procedure.md` §3.5; `01_venice_procedure.md` §3.7) (4) | R-9, R-34, R-35 |
| B19 | R-36: local legitimacy on the verdict's weight, or on availability and enforcement (file 02 §3.5) | **both, in different channels**: weight × L in the draw (ruled); availability and enforcement through persons' own later acts (`comply`, `arrest`), no term | R-36 fixes the first (1); the research's finding needs no apparatus (5) | R-36 |
| B20 | a hostile territory: L floored at 0, or negative | **floored at 0**; hostility beyond indifference is the locals' reception of the officer, already σ | a negative weight would count the hostility twice (5) | R-36 |
| B21 | legitimacy as a territorial number | **a per-contest Query over persons in the venue's territory, dying with the run** | S-7; `state/carriers.py:1103` refuses a Rung any aggregate; ED-SC-0034 (1) licenses an in-run aggregate (3) | S-7 |
| B22 | R-2 "appeals should not be a thing" against an appeal row | **appeal is a route**: no retry before the same bench; a petition carried to `appeal_basis` | R-35 (1) | R-2, R-35 |
| B23 | kernel: adopt or retire | **retire**; timing SM-15 stays Jordan's and is not re-asked | R-14 (3) | R-14 |
| B24 | eight kinds against four structures (RD §3.2) | **four deciders** (target, parties, bench, count); K8 is a matter type | RD §3.2 (3) | R-12 |
| B25 | parliament as `mutual`, a bargain between crown and estates (file 04 §4) | **count**: the body's commits license or block the owner's own act; the owner's act is the second consent | R-29 (1) | R-29 |
| B26 | count weight: by standing (R-2, panels) or one per seat | **escalated (G3)** | R-2 is narrowed and predates R-29; materially different parliaments | R-2, R-29 |
| B27 | Cialdini's principles as magnitudes | **none sets a magnitude**: authority is office weight; liking, unity, social proof and commitment act only through reception; reciprocity and scarcity act in the target's choice | file 03 §3's records (door-in-the-face behavioural r = .052, not significant; towel effect partly unreplicated; unity unreplicated) (3); R-19 refuses a creditor's lever, so a debt cannot be called in | R-19 |
| B28 | D-7 (detailed denial; displayed anger) | **closed as two speech-kind aptness rows**, anger's sign set by the rank gap, both costing reception after | peer-reviewed findings in the proceedings study (`source/02-part-I-throughlines.md:146-206`), as HO §2.3a proposed (3) `[ASSUMPTION; medium; revert: D-7 open]` | none |
| B29 | J-13 "what sets a pool" | **superseded** | R-31, R-40, R-41 (1) | R-40 |
| B30 | R-24's two fidelities | **one armature**: the player chooses acts in the container; the automated path chooses by policy; the draw is identical | R-24 routes, it does not fork the rules; R-23 (3) | R-23, R-24 |
| B31 | one-tick trials against "everything in a scene binds" | **binds** | RD C9 (3) | R-11 |
| B32 | lot and acclamation (file 04 families 2, 4) | **not this engine's draw**: a lot is a rule for who sits, an acclamation a count without ballot; no row needs either yet | (2) for now; nothing reads them | none |
| B33 | the visible middle of a long debate (the track's gauge) | **cut is a cost, kept as one** | RD §3.3; an explanation-contract matter, not a mechanism | S-7, C12 |

---

## C. The primitive set and owners

Eleven primitives carry every ruling and every kind. Owner = the one place code reads the fact.

| primitive | carries | owner | state |
|---|---|---|---|
| **row** | authority, decider, admission, order, proof grades, interposition, weights, disposal, reach, appeal, threshold | `engine/season/arrangements.yaml`, loaded by `data/arrangements.py` | loads; one key read |
| **matter** | what is before the room, with mood (HOLDS, OUGHT, neither) and ground | `DocketItem`, `Proposition` | exists; `mood` unread |
| **act** | one verb plus, for speech, one speech kind | `verb_table.yaml`, `data/verbs.py`; speech kinds in the arrangements data | exists; kinds unread |
| **gate** | licence to act (remit, floor, rank) | `state/gate.py` | exists; row keys unread |
| **the record of one draw** | the three channels' operands | `SocialContestInput` (`queries/inputs.py:43`) | exists, short of σ producers |
| **producers** | one function per operand | `seam/wrappers/sigma.py::contest_input` | two of the needed ones |
| **the draw** | composition, μ-shift, ladder | `modules/social_contest/roll.py`; `engine/dice_engine/` (`degree_from_net`, `dice_engine.py:236`) | exists |
| **choice** | will: what a person does given what he holds | `engine/season/decision/` | exists; unlinked to `speak` |
| **count** | commits against a threshold, licensing the owner's act | a Query in `queries/world_q.py` | absent (`commit_count_guard` probe-only, PROBE §1) |
| **authority and legitimacy** | which seats sit; L per territory | `judging_set` (`world_q.py:566`); `person_q.legitimacy` (`:452`) | partial; L unread; no piety |
| **disposal and reach** | Tenure edges, Records, licences; who learns | `effects_information.py`, the witness channels | three kinds; no news speed |

Appeal is not a primitive: it is `petition` plus `carry` to the authority `appeal_basis` names.

**Cut, and what dies.** The kernel (dies: eight presets that differ in four accidental things, RD §3.3; free). UP's
roster (B1; dies: nothing, since its rule survives in the record). Latitude in the obstacle (dies: nothing; R-18).
The rung term (B13; free). The "unmirrored" netting (B4; free, R-5 does it). The discrete integer path (B8). The
`obstacle_ceiling` if G1 goes that way (dies: a bound on very strong opposition; provided instead by the σ channel,
which at its effective cap (1.5σ) still lifts a 5D party against Ob 6 from 1.3% to about 23%). `VERB_CAPABILITY`'s two-row map, replaced by the
brought and conduct keys `06_RESOLUTION` §B.1 already names. The word "kind". The arrangement keys: of the thirteen,
`venue_min_rank` folds into the admission gate, `records_dissent` into `disposal_reach`, `stakes_grade` and
`verdict_reasons` were already scheduled to go; `term_required` I do not cut, since Layer 1 §A.4 (every opener
declares its terms) may be what it carries and I have not found its intended reader.

---

## D. Commensurability

### D.1 The one scale

Every commensurable influence changes one of three numbers in one expression, and the expression is in the unit the
ladder grades (`dice_engine.py:236-248`: margin = net − Ob; Partial at 0, Success at 1, Overwhelming at 3):

```
E[margin] = 0.40·N  +  0.80·√N·softcap(s)  −  Ob          spread = 0.80·√N
            dice       leverage (μ-shift)      obstacle      softcap(s) = 1.5·tanh(s/1.5)
```

(`MU_PER_DIE` 0.40 and `SIGMA_PER_DIE` 0.80 at `dice_engine.py:181-182`; `M_MAX` 1.5 at `sigma_leverage.py:104`;
`net_boost` at `:190-203`.) Exchange rates follow without any choice of mine: **1 Ob = 1 net = 2.5 dice of mean, at
every pool**; **1σ = 0.8·√N Ob** (1.13 at 2D, 1.79 at 5D, 2.77 at 12D). Dice and Ob convert at a fixed rate; σ does
not, because it is a z-shift: it is worth the same probability to a novice and a master, while a die or an Ob point
matters less as the pool grows. That property is the reason each source is put where §B2 puts it.

**What a unit is worth at the reference** (my runs of `p_success`; "meets" is margin ≥ 0, i.e. Partial or better,
which is what `p_success` returns; "succeeds" is margin ≥ 1). Reference: 5D (R-40) against an equal 5D opponent, so
Ob = 2.5 by R-5.

| change from the reference | meets | succeeds | overwhelms |
|---|---|---|---|
| reference: 5D v Ob 2.5 | .390 | .201 | .025 |
| +1 die | .480 | .287 | .057 |
| +2.5 dice (one Ob's worth of mean) | .590 | .410 | .127 |
| +1 Ob | .201 | .081 | .006 |
| +0.25σ / +0.5σ / +1σ | .487 / .580 / .724 | .277 / .361 / .514 | .044 / .070 / .140 |
| +1.5σ (soft-capped to 1.14) | .806 | .619 | .208 |
| −0.5σ | .223 | .093 | .007 |
| 8D v an equal-skill 5D | .621 | .447 | .155 |
| 5D v an 8D | .132 | .047 | .003 |
| 5D v nobody (Ob default 2) | .500 | .288 | .047 |
| 10D v an equal 10D | .346 | .215 | .057 |

At the reference **one die ≈ 0.25σ ≈ 0.4 Ob**. Two consequences of the ruled arithmetic, stated rather than fixed:
R-5's ÷ 2 converts an opponent's dice at 0.5 Ob each while the engine credits 0.4 net each, so **equals favour the
side that does not act** (61% of acts against an equal fail at 5D, 65% at 10D; G4). And `obstacle_default` 2 is an
unopposed matter as hard as a 4D opponent.

### D.2 The table

Tiers: **RULED** (Jordan; R or S number), **SOURCED** (research, with the file), **ASSUMPTION** (mine). Where the
evidence cannot set a size, the size is a **sweep** parameter with a control arm at 0; nothing weakly evidenced is
given a magnitude.

| influence | channel | unit | conversion or bound | tier | today |
|---|---|---|---|---|---|
| capability, *brought* (preparation, evidence discrimination, memory) | dice | D | one capability point = 1D `[ASSUMPTION; low; revert: per-key scale]`; the attribute roster is in flux | source RULED (R-31, R-40); spread SOURCED as a **calibration target**, not a value: persons explain 25% (distributive), 46% (integrative) of negotiated outcomes (Elfenbein et al. 2008, `source/02-part-I-throughlines.md:15-23`) | only `copying`, for `tell`, `speak`; 0 of 83 persons carry it (CA §1) |
| capability, *conduct* (presence, charisma, reading, timing) | dice × latitude | D | latitude ∈ [floor, 1], a Query over `interposed`; floor swept | RULED (R-18, R-41); SOURCED: a constrained office keeps about 70% of the person-effect (Quigley et al. 2022, per ED-SC-0034) | absent |
| title (rank) | dice | D | the row's weight for the title; per holder the larger of title and seat (B10) | RULED (R-31, R-34: negotiation's rung differential); size sweep | absent |
| office weight, the holder's own seat in this venue | dice for its holder; reaches the other side only through that holder's score | D | `row.weights[seat] × L(authority, territory)` | RULED (R-31 clarified, R-36, R-38); ordering SOURCED: weight grows as constraints fall (Jones and Olken 2005; Quigley 2022, `source/02-part-I-throughlines.md:49-85`); size sweep | absent; `Act.via` not passed to the contest (CA §2) |
| faction backing | dice, where the row keys it | D | row column | RULED source (R-31); size ASSUMPTION, sweep | not read |
| evidence held | dice, per party, gross | D | weight by remove and age (as live), times the row's grade for that proof kind; live `proof_step` 0.25 Ob = 0.625 D of mean as a start (not value-identical: a die also widens the spread, so +2.5 dice gives P = .590 against .610 for −1 Ob) | RULED (R-32, R-40); grades SOURCED (*ordo iudiciarius*: two witnesses a full proof, confession the queen of proofs; PK §5) | subtracted from Ob, netted, `speak` only (`roll.py:104`) |
| opponent's score | Ob | Ob | `S_opp ÷ 2`, `S_opp` the opponent's own dice total from the rows above | RULED (R-5) | capability `copying` only |
| aptness (fit of the speech kind to genre, rung, ground; undeclared proofs) | Ob | Ob | a price per kind; where an emotion's three preconditions (state, target, a believed fact) are not all held, the maximum price; the act still rolls and may write (R-16: the wrong act can land) [CORRECTION after the critic: the first draft said it writes nothing, which is a refusal in effect] | RULED (R-16); SOURCED (Aristotle *Rhet.* II.1; *De Inv.* I.33, file 03 §1.2, §2.4); size sweep | roster loads, unread |
| forgery quality of a document examined | Ob (the document's score) | Ob | as live | live (`roll.py:106`) | live, inquiries only |
| no resisting person | Ob | Ob | `obstacle_default` 2 | live (`H-127`) | live |
| reception: the decider's regard for the actor, net of his regard for the opponent | σ | σ | mean over deciders; gain set so 5D reads as the live 1.0 Ob per unit (≈ 0.56σ per unit), swept | RULED source (R-32 "audience", R-40 "standing"); SOURCED weakly (Quintilian's *vir bonus*; ELM from abstracts, file 03 §4) | Ob term, a sum (B3) |
| argument fit: coherence of the proposition with what the decider already holds | σ | σ | sweep | RULED source (R-32 "argument"); SOURCED secondary (Pennington and Hastie: 78% against 31% guilty by story order, file 03 §4) | no producer; `argue` is content-blind (PROBE §2.1) |
| circumstantial leverage (what the actor can do to the matter's outcome outside the room) | σ | σ | sweep | RULED (R-34, R-40) | `leverage=0.0` (`sigma.py:191`) |
| anger, detailed denial, frank speech | aptness rows; a reception cost after | — | anger's sign by the rank gap | SOURCED peer-reviewed (Van Kleef et al. 2004, 2006; the correction literature; `throughlines.md:146-206`) | absent |
| practice | grows the capability rows across seasons | — | — | SOURCED (Antonakis et al. 2011, about .62) | unverified |

All σ sources sum before the soft cap, so together they are bounded at 1.5σ (effective 1.14 at s = 1.5). That
bound is the evidence discipline in the engine's own arithmetic: the weakly evidenced levers live in the one channel
whose total cannot exceed it, however their sweeps come out.

### D.3 What cannot be made commensurable, and where it goes instead

| not on the scale | why | treated as |
|---|---|---|
| **will**: fears, wants, convictions on the matter, risk appetite and horizon, the size of the ask, the walk-away option, a debt owed | it is the decider's own decision, not the act's landing (R-19, R-23, R-28) | the choice layer (`engine/season/decision/`), reading the claims and pursuits the draws moved. "The cornered man breaks toward the feared thing" lives here |
| licence to act | R-31's licence half is a permission | the gate: remit, floor, admission. Aptness is priced (R-16); licence is not aptness |
| burden | it names who must succeed, not by how much (RD E4) | the default disposition when no act lands; undecided is an outcome (R-1) |
| truth, worldly state as such | the world reaches a person only as claims (S-7, S-8) | evidence held, and circumstance as leverage. No truth bonus |
| an authority's availability, its enforcement, its speed | sourced as what local hostility actually changed (file 02 §3.5) | persons' later acts: `arrest`, `seize`, `comply`, `confer`, `revoke` |
| a lie or forgery discovered | a past act, not a present advantage | a Record (S-5) and the reception that follows |
| a secret | spent by telling (ED-SC-0035) | a distribution act |
| lot, ordeal, divination | no margin; ordeal refused | not this engine (B32) |
| threshold, quorum, mood, ground | structure | row keys; mood and ground act only through aptness |

### D.4 Double counting, checked

| pair | verdict |
|---|---|
| standing and reception | one fact, σ, once (B3) |
| office weight and "authority weight" | one fact; L is a multiplier on it, not a source (B19) |
| the opponent's proofs and "proofs against" | inside the opponent's score; the netting goes (B4) |
| presence, charisma, and capability | one: conduct (R-41) |
| Cialdini's "authority" and office weight | one: office weight |
| unity, liking, faction backing | backing is the actor's holding (dice); shared identity with the hearer is reception (σ); reception may not also read faction membership `[ASSUMPTION; medium]` |
| title and seat | one weight per holder per venue (B10) |
| latitude and title | latitude reads `interposed`, not rank (B11) |
| a fear on the roll and in the choice | choice only (B5) |
| the judge's belief on `determine` and in his choice | choice only (B6) |
| a decider's convictions in reception and in his choice | choice only (B15) |
| an office's weight on its holder's roll and on the other side's obstacle | never both for one act: the actor's office is on his roll; the opponent's is in the opponent's score (R-38 read per holder) |
| the gallery's regard | not an input unless the gallery decides; otherwise an output (its stances move) |

---

## E. The kinds as rows of the one structure

Every row has the same keys: authority · decider · admitted acts · weights · burden and proofs · reach · appeal.
Only the values below differ; everything else (the draw, the channels, the choice layer, disposal) is shared.

| kind | values that differ |
|---|---|
| **K1 dyadic persuasion** | authority: none · decider: the target, whose claims or pursuits the draw moves · admits `tell`, `argue`, frank speech, display kinds · weights: title only · burden: the actor · reach: those present · appeal: none |
| **K2 negotiation** | authority: between the parties (R-34) · decider: both parties `commit` to the same terms, else impasse (R-1) · admits offers (`utter`), `argue`, `commit`, `give`; an envoy by `interposed` · weights: title (the rung differential) and circumstantial leverage · burden: none · reach: parties and principals · binds in scene (R-11) |
| **K3 adjudication** (trial, inquisitorial hearing, political tribunal, arbitration, excommunication, audit) | authority: polity or church · decider: seat-holders of that authority over the venue; `determine` grades the degree · admits per `floor`, `order`, `proofs` · weights: the row's office table × L · burden: per subkind (accuser, respondent, lower standing) · reach: `disposal_reach` · appeal: another authority |
| **K4 petition** | authority: the addressee's · decider: a bench of one, by grace; lapse is an outcome (R-1) · admits `petition`, `carry`, intercession by `interposed` · burden: the petitioner · reach: the petitioner · appeal: none, or a higher rung |
| **K5 panel or jury** | as K3, bench of several; each member's `determine` is counted against the threshold |
| **K6 deliberation** (parliament at four rungs, council of state, synod) | authority: the polity at a rung (R-27) · decider: members' `commit` edges counted, licensing or blocking the owner's own act (R-29) · admits speaking in order and `commit` · weights: per G3 · burden: the mover · reach: the body, then the world; opinions drift (R-26) |
| **K7 display** | authority: none · decider: each hearer's reception moves · admits display kinds · no disposal; standing is never a stake (R-21) |
| **K8 contests over the contest** | a matter type: a seat, a jurisdiction or an order as the matter, under the K3 or K6 values; disposal by `confer`, `revoke`, `hold` |

A heresy proceeding and a royal tribunal with the same accused are then two rows differing in `authority`, their
weight tables and `appeal_basis`, and L is read for a different authority in the same territory (R-36).

---

## F. What executes today

From CA §1-§4 and PROBE.md (scratchpad, 2026-10-30, against this tree; one chooser, three seeds, two seasons:
counts, not rates).

| armature part | state |
|---|---|
| one draw, one ladder | **executes**, on the discrete integer path: pool 2 and Ob 2 for nearly every roll (F .744, P .187, S .070 at 2D v Ob 2, CA §1); the continuous engine is not on the path |
| dice channel | **paper**: `pool_default` for everyone; no attribute, title, office or faction reaches the roll |
| obstacle channel | **executes in part**: ÷ 2 over one capability key; reception and proofs subtracted for `speak` only; forgery for inquiries; ceiling 2 bounds everything at the default |
| σ channel | **paper**: the literal 0.0 (`sigma.py:191`) |
| the row | **loads, decides nothing**: only `disposes` is read; computed `open_case` names no row (`{None: 15}`); in the probe "no row key changes an outcome" across six rows (PROBE §2.3) |
| action surface limited by venue | **absent**: the global verb table; the speech-kind payload is ignored |
| decider: target | `tell` writes nothing at any band (PROBE §1, `verb_table.yaml:1334`); `argue` moves pursuits on Success and better, content-blind, formed once in six runs |
| decider: bench | **executes by hand only**: all six K3 rows open a case and determine; computed play rolled `determine` 0 times (refused at the docket and person conjuncts). **`speak` does not reach `determine`**: the same determination before and after three speeches drew the same (PROBE §2.3), which is the armature's central link missing. A failed judge leaves the matter for any other seat-holder to retry |
| decider: parties | **absent**: no negotiation row; `disposal: mutual` has no reader and runs as a one-judge bench (PROBE §2.2) |
| decider: count | **absent**: `commit` edges read only as membership |
| authority | **absent as a concept.** [CORRECTION after the critic: the first draft said no church bench can sit; that was wrong. `populated.build_realm` passes `scope_rung=rung` for every authored seat (`populated.py:1521-1523,1582-1583`; asserted by `test_governance_build.py:2391-2410`), so church seats sit. What is true: every church seat holding `determine` (Confessor, Cardinal of Justice, Senior Inquisitor) is anchored at T9 Himmelenger, so a church bench reaches only venues contained in T9; and `judging_set` has no authority filter, so the King and Queen (`determine` at realm scope) sit on every bench, church venues included (`world_q.py:636-642`; `offices.yaml:187,239,366-434`).] |
| legitimacy | **paper**: `person_q.legitimacy` exists, unread by the contest; no piety Query |
| disposal | `oblige`, `detain`, `ban` by hand; in computed play only `oblige`, from the self-service `oblige` verb; Record-disposing rows refused (`effects_information.py:334-337`) |
| reach | everyone, through `chronicle`; no news speed |
| appeal | **absent**: `appeal_basis` unread; a second bench's edge stacks and voids nothing; a re-opened matter wedges (PROBE §2.3) |
| Partial writes a docket matter | **absent** (R-17 unmet) |

Roughly: the draw and three disposals run; the channels, the row, the deciders other than one judge, authority,
reach and appeal are paper.

---

## G. What survives for Jordan

**G1. The ceiling.** R-39 withdrew the 1D M-7 check the ceiling was built for, and R-40 puts normal pools at 5D.
(a) **Keep a ceiling above the default** (the sweep's 3; this is R-37, the governing ruling): very strong opposition reads as a 6D opponent, a cap that bounds an input, not an outcome frequency. (b) **Delete it** (`None`, the existing control arm): a 5D party against Ob 6 meets 1.3% of the time,
about 23% with leverage at its effective cap of 1.5σ [CORRECTION: the first draft read s = 1.5 as the cap; `soft_cap` is `1.5·tanh(s/1.5)`, so s = 1.5 gives only 1.14σ and 1.5σ is the limit as s grows (`sigma_leverage.py:104,148,202-203`)]; R-18's chance at winning then comes from leverage the player assembles. Either
moves the goldens (§7). The producer recommended (b); the critic found its grounds wrong (above), so I do **not** carry that recommendation: (a) is the ruling and (b) is an amendment for Jordan.

**G2. The Layer-1 wording.** R-31 and R-38 require an office weight; `03` §A.3 and its STRUCTURAL row forbid one.
The narrow wording RD §2.3 suggested: "a seat adds no verb and no modifier **of itself**; a venue row may license an
office-keyed act set and weight." Accept that wording, or give another. Nothing of R-31's weight can be built before.

**G3. The count's weights.** (a) **One seat, one vote**: a parliament where rank buys speaking order and weight in
the draw but not votes. (b) **Weighted by the row's office weights** (R-2's "weighted by standing", read through the
one weight table): a parliament where great lords carry more of the count. Different games; R-2 is the only ruling
and predates R-29.

**G4. Equals and the status quo.** Under R-5's ÷ 2 at R-40's scale, an act against an equal fails 61% (5D) to 65%
(10D) of the time and succeeds 20%. (a) **Intended**: the world resists change, and Partial's docket matter (R-17)
carries the churn. (b) **Convert the opposed score at the engine's own rate** (× 0.4), so equals meet half the time.
(b) amends a ruling, so only he can choose it.

Untouched and still his: J-C-6 (may a person lie; it decides whether a party may knowingly hold false evidence),
SM-15 (the kernel's timing), the source of risk appetite and horizon (CR-17).

---

## H. Where I attack my own result

1. **The draw may be cosmetic for every decider but the target.** I put will in the choice layer and grade only
   the degree with `determine`. If the choice layer does not read what the advocates' draws moved, a brilliant
   speaker wins every draw and changes no verdict, and R-18's "a brilliant speaker to be rewarded" fails. The probe
   shows exactly that gap today (`speak` does not reach `determine`). Falsifier: a seeded test in which an `argue`
   Success on a judge flips his `determine` choice on the same matter, against a control in which it does not. If
   no reasonable choice rule passes it, the decider's belief must go back on the draw as σ (reverting B6).
2. **σ dominates at high pools.** Dice and Ob shrink as 1/√N; σ does not. At 12D the capped σ channel is worth up to
   4.16 Ob, about 10.4 dice of mean (corrected from 3.2 and 8), so reception, fit and circumstance, the three least evidenced sources, outweigh
   evidence and office for a master. That may be wrong. Falsifier: at 5D and 12D, the share of outcome variance by
   channel across seeded realms; if σ's share exceeds the dice share at 12D, reception moves to dice or the σ sweep
   is bounded lower.
3. **"Whose fact" is still a judgment per source.** Reception is the decider's fact about the actor; I call it a
   relation and put it on the actor's roll, which R-40 supports but the rule does not force. An office's weight
   could as well be read as a relation between its holder and the venue. If a critic can place a third source on
   two channels by the same rule, the rule does not decide, and per-source choices have returned under another name.
   I also read R-40's "5D" as the roll side's dice-equivalent (dice plus leverage), which is my reading, not his.

---

## I. The critic's pass and its reconciliation

One round, by a read-only critic that could not run code and recomputed the figures from the closed form
(`sigma_leverage.py:275-279`). Fifteen findings; the corrections are made in place above and marked
`[CORRECTION after the critic]`. The disposition of each:

| # | severity | finding | disposition |
|---|---|---|---|
| 1 | MATERIAL | the soft cap was read as 1.5σ at an input of 1.5; the effective value is 1.14σ there and the limit 1.5σ as s grows; nothing caps the raw sum | **accepted**; figures corrected: 5D against Ob 6 at the true cap is about **23%**, not 13%; at 12D the cap is worth **4.16 Ob (about 10.4 dice)**, not 3.2 Ob |
| 2 | NIT | the 2.5 dice per obstacle point rate holds for the mean only; probability differs (+2.5 dice .590 against −1 Ob .610) | **accepted**; "value-identical" withdrawn |
| 3 | MATERIAL | a mirrored proof is not neutralised by R-5's ÷ 2: 0.4x gained against 0.5x lost, so it costs the actor 0.1x; the live "mirror" is a same-claim read, not an opposing proof | **accepted**; B4 corrected; whether to keep any netting is open on other grounds |
| 4 | MATERIAL | `proofs_against` is the actor's evidence (dice), not the opponent's score | **accepted**; the third double-count is dropped |
| 5 | MATERIAL | the record's fields are operands, not channels; "three field edits" undercounts (six or more); the rule remains a discipline for a reader | **accepted**; stated as a discipline; edits counted |
| 6 | MATERIAL | the draft omits ED-SC-0040 and the 04 §B.2 F8 rule: reception as a mean over the bench's ledgers, argument fit, the opponent's evidence and a per-territory legitimacy are all cross-ledger reads at RESOLVE | **accepted as an open constraint** on B3, B4 and B21: each σ and score producer must be sourced from commits or edges, or carry ED-SC-0040 as unresolved. This is a Layer-1 tension, not a detail |
| 7 | MATERIAL | "no church bench can sit" is wrong: `build_realm` passes `scope_rung` for every authored seat. What is true: church `determine` seats are all anchored at T9, so a church bench reaches only T9 venues; and `judging_set` has no authority filter, so the King and Queen sit on every bench | **accepted; my own relay of it as verified was wrong** (I checked only that `offices.yaml` lacks the field, not that `build_realm` supplies it) |
| 8 | MATERIAL | B7/G1: flagged, but on wrong grounds (R-37 is not the newest; R-39 does not remove R-37's stated reason; R-8 is about band de-saturation; the draft's own "newest governing" rule favours R-37); option (b) omits the S27.4 refusal of an obstacle above 2 × pool | **accepted**; R-37 is the governing ruling, deletion would amend it, the producer's recommendation is not carried |
| 9 | MATERIAL | R-40 lists argument, evidence, leverage and standing as parts of the dice total; the draft moves three of four into σ and then reads "5D" as dice-equivalent, which depends on pool; the D.1 reference table uses pure dice with σ on top, contradicting H.3 | **accepted as open**: either those sources enter dice, or the 5D bar is defined at a stated pool and flagged as amending R-40. Jordan's reading is needed (question G5 below) |
| 10 | MATERIAL | an act that writes nothing at maximum price breaks R-16 | **accepted**; corrected |
| 11 | MATERIAL | circumstantial leverage ("what I can do to you outside the room") and a pressed fear are the same fact on two channels (σ and the decider's choice) | **accepted as open**: one placement per venue type, and how R-19 and R-34 divide it (question G6) |
| 12 | MATERIAL | the "choice exists, unlinked to `speak`" claim is soft: `choose` holds pursuit and stance only; no fear field; `determine` has no disposition operand; computed play never reaches `determine`; A.3 contradicts live `argue` (which writes the hearer's pursuits). Closing the link needs (a) a disposition operand on `determine`, (b) a matter-specific term in `choose` read from the judge's own interior, (c) computed play reaching `determine` | **accepted**: the central link is **not small**; (a) to (c) are its cost |
| 13 | NIT | reception as a mean: bench-size scaling fixed, but the per-deed sum stays unbounded (the σ cap bounds the effect) | accepted; noted |
| 14 | NIT | "standing is never a stake (R-21)" is the collector's gloss; a live `a standing` prize exists | accepted; cite PK §1.1 item 4 |
| 15 | observation | the Layer-1 amendment (G2) is outside the critic's lane | no change |

**What survived the attack** (the critic named the failed attack in each): the closed form `E[m] = 0.4N + 0.8√N·softcap(s) − Ob` with spread `0.8√N`, and the D.1 table (recomputed to three places); the 61% and 65% headline odds for acts against equals; the live ladder (no `BandExtension` on the live seam, `seam/ladder.py:250-251`); G4 (correctly leaves R-5's ÷ 2 to Jordan); R-38 read per holder; the count as a resolver-side Query (R-29, S-7, AX-2); the R-35 appeal route; the kernel deletion; and every citation the critic opened.

### Questions for Jordan, after the critique (replaces G1 to G4 and adds two)

- **G1. The ceiling.** R-37 stands as the ruling: a ceiling above the default. The sweep's 3 is the candidate; at 5D it is not binding. Deleting it would amend R-37 and make an obstacle above 2 × pool a refusal (S27.4), against R-16. *Which value, or do you want it deleted?*
- **G2. Layer 1 §A.3's wording** for office weight (R-31, R-38); nothing of that weight can be built before it.
- **G3. The count's weights:** one seat one vote, or weighted by the row's office weights.
- **G4. Equals:** keep R-5's ÷ 2 (an act against an equal fails 61% of the time at 5D), or convert the opponent's score at the engine's own rate (× 0.4) so equals meet half the time. This amends R-5.
- **G5. What R-40's "5D" counts.** Dice only (the sources named all enter dice) or dice plus σ at a stated pool. The critique shows the armature cannot hold both.
- **G6. Where circumstantial leverage sits** (σ or the decider's choice) for each venue type, given R-19 ("fears are leverage that you can press") and R-34 (circumstantial leverage is negotiation's imbalance).

`[CONFIDENCE: medium]` that fifteen findings from one round are the findings that matter; the critic read the cited surfaces and recomputed the arithmetic but could not run code, so the church-bench correction and the soft-cap figures are by reading and by closed form, not by execution.
