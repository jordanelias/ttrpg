# Social contest: the primitives, and the kinds of contest they compose

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

Companion to `2026-10-30-social-contest-kinds-of-contest.md` (#530), which describes what the *code* does. This
document sorts what the whole corpus says a contest is made of. It is a reading, not a plan (CLAUDE.md §0.05): it
dies with the documents it sorts. Read from the working tree at `7f77ea7`.

**Method.** Thirteen readers each took one slice in full (the pre-proceedings designs; the 2026-08-06 three-lens
audit and its five source studies; the proceedings subsystem, 00 to 21 with atoms and relay; the 2026-10-29
debate corpus of 757 entries and the parliament design; the rhetoric research and `SC_social_contest.md`; the
institutional research on Venice, councils and tribunals; the verb lexicon, system description, completion
proposal and the live code). Two more collected Jordan's rulings with their dates and context. Their extractions
(about 55,000 words) are not committed. Dates below are those the source text gives; the checkout is shallow, so
`git log` could not date anything before 2026-10-16.

**Order of precedence used throughout.** Jordan's rulings first, oldest first, because they fix what is not
open. Code second (§0.05). Proposals third. Research last, as a supplier of mechanisms.

---

## 1. Jordan's rulings, in the order they were made

Only rulings that constrain what a contest is made of, or how it is performed. `R-n` is cited in later sections.
"Governs" is the collectors' reading of whether a later row supersedes. Agent rulings and `[ASSUMPTION]` takes are
excluded; they are listed in §1.3.

| # | date | ruling | where it was made | governs? |
|---|---|---|---|---|
| R-1 | 2026-06-02 | An undecided outcome "is a legitimate and interesting outcome" | `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:403` | yes |
| R-2 | 2026-07-01 | Panel votes weighted by standing; "appeals should not be a thing -- let the decision ride"; Terminal Doubt is terminal everywhere; the Guilds boost comes from the venue ("GM picks" was a no-GM defect) | ED-1057, ED-1059..1061 | narrowed: kernel retiring; **in tension with R-14** (the successor lists *appeal* among twelve games; no row reconciles them) |
| R-3 | 2026-07-05 | "Ratify all" for the audit's findings and sequencing; forks without a stated default stay open | ED-SC-0001..0005 | superseded in the particulars (closed 2026-09-11 to 2026-10-26) |
| R-4 | 2026-07-08 | Auto-resolve and play-it-out are one conflict at two fidelities; "specific events on a slate", not a generic per-season roll | ED-SC-0013 | narrowed by R-24 |
| R-5 | 2026-08-14 | `degree_from_net` is "THE degree ladder. Single owner for every scale"; an opposed obstacle is "their corresponding score/2 plus whatever specific modifiers exist for them in that instance" | `modules/social_contest/roll.py` docstring; `04_VERBS.md:87` | **yes** |
| R-6 | 2026-08-15 | "systems should not need different degree bands. it should be consistent in application"; if one needs an extension, "the wrapper needs to inject the engine" cleanly | ED-SC-0031, ED-SC-0032 | **yes** (`BandExtension`) |
| R-7 | 2026-08-18 | "We can script narrative hooks and sequences so long as we don't script entire arcs" | `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:616` | yes |
| R-8 | 2026-08-27 | "Stop arbitrary fiat capping"; "if you don't have enough dice you don't have enough dice" (a pool-2 contest cannot reach Overwhelming; settled, not to be re-raised) | ED-SC-0032; ED-PC-0057 | **yes** |
| R-9 | 2026-09-02 | Titles: realm = king/queen, duchy = duke/duchess, province = count/countess, territory = lord. "there is a Parliament, so there is no monopoly of power in the ruler"; a duke may revoke office within his purview | `engine/season/hole_register.yaml:1126` (H-90) | yes |
| R-10 | 2026-09-03 | Kill and wound degrees are *read* from scene combat, not mapped from the winner | `02_THE_SOCKET.md:116` | yes, generalised: a verb reads the degree from the scene |
| R-11 | 2026-09-04 (recorded 09-26) | "many different lines of adjudication requiring verdict so you can win on one thing but partially lose three items and lose completely on five"; and "negotiated agreement bind in scene ... everything that occurs within a scene should bind or else it's as if time doesn't exist within a season" | ED-SC-0038 | **yes**, all twelve rows; the per-matter half is built (H-213); re-examination of P-14/D-8 is owed and unrecorded |
| R-12 | 2026-09-05 | "The subsystem is a game structure ... hosts the parameters, logic, processes, mechanics, actions, roles, venues ... and then the games within it ... are **just defined parameters**" | `README.md:18`; `00_DERIVATION.md:12` | **yes** (reaffirmed by ED-SC-0033/0034) |
| R-13 | 2026-09-05 | The proceedings proposal "will not refer to any previous work concerning social contests" | `README.md:102`; HANDOFF_SC standing order | scope ban for the proceedings *build*; ED-SC-0038 had to relay two rulings the ban hid |
| R-14 | 2026-09-06 | "this subsystem obviously owns all social contests"; "orphaned social contest code: retire it" | ED-SC-0033 | yes in direction; **execution held** (`systems/social_contest/sim/` still on disk; timing is SM-15) |
| R-15 | 2026-09-06 | "whatever works best for the subsystem is what goes, so long as it can receive input and give output to seasons" | `19_PLAN.md:69` | yes; zero-new-primitives is a tiebreak only |
| R-16 | 2026-09-06 | Aptness **priced, not refused**: a character may "choose the 'wrong' action and roll against a higher obstacle but still succeed", or choose right and "still fail" | `04_VERBS.md:252` | **yes** |
| R-17 | 2026-09-06 | Partial must bring something forward: it writes a docket matter and the docket grows | `04_VERBS.md:131` | yes |
| R-18 | 2026-09-06 | "why can't we have aggregates in a subsystem?"; "of course we accept those shapes" (multilateral tally, debate score); "pool only it is" (latitude enters the pool, not the obstacle); "ensure you don't go so far as to deprive player of a chance at winning"; "a brilliant speaker to be rewarded" | ED-SC-0034 | **yes** (M-7 deprivation floor was run and **failed** at the 1D floor; the remedy shipped as an obstacle ceiling, `H-213`, value 2: see the code audit) |
| R-19 | 2026-09-06 | "fears are leverage that you can press"; "cornered man breaks toward the feared thing"; "pressure is the gap"; "second-person lever stays refused" (no creditor verb, no `call_in`, no hook) | ED-SC-0035 | **yes** |
| R-20 | 2026-09-06 | "so what if the argument doesn't come out of a closed room? ... if you're playing the head of a major faction like Baralta, you're going to be in those closed rooms"; "characters will be enacting the system as participants, audience, adjudicators" | `10_LOOPS_AND_GAPS.md:99`; `03_PARAMETERS.md:394` | yes: a role is a relation to an occasion, never a field |
| R-21 | 2026-09-06 | "This subsystem and its games must be ABOUT the world and enacted by characters OF the world." Three tests for every row: what in the world changes, why is each person in the room, who learns it happened. "the decisions made therein still get announced to the world as the parliament's decision, which means state change and propagation" | `14_THE_WORLD_IN_THE_ROOM.md:238-357` | **yes**, "binds every row" |
| R-22 | 2026-09-09 | "we have the sigma leverage d10 resolver in engine to use" (interim provider) | ED-SC-0037 | yes; the obstacle's ownership is *not* closed by it |
| R-23 | 2026-09-17 | The act is inviolate, reception is not: "the player must have the sanctity of their choices/actions/decisions preserved ... the worldly churn is in how those contents are received and acted upon by others" (AX-7) | ED-IN-0234, ED-IN-0244 | **yes** |
| R-24 | 2026-10-03 | Social contests "occur within their own Godot container ... season loop determines calling of container through its verbs"; non-player contests "routed through an automated resolution in the module that does not call forward a playable scene"; the module must "exist on its own" | ED-IN-0285 (11, 13, 14) | **yes** |
| R-25 | 2026-10-06 | Proceedings design **ratified as intent only** (merge ratifies, ED-1094); only `README.md`, `04_VERBS.md`, `21_RECONCILIATION.md` carry the flipped Status | ED-SC-0039 | yes: "nothing exists in `engine/season/` until SC-01 is built" |
| R-26 | 2026-10-29 | The ask: debate between characters on worldly topics; the result must change the world at the seam, "even if it is just a change in opinions"; a parliament at kingdom, duchy, province and territory rungs | `2026-10-29-parliament-and-debate.md:6` | yes |
| R-27 | 2026-10-29 | "a rung has never been a place in my understanding": where a decision occurs is a hierarchical position | `reasons-to-convene.md:22` | yes |
| R-28 | 2026-10-29 | Persons "differ in risk appetite as well as in short- vs medium- vs long-term views"; short = this or next season, medium = three to four, long = five or more | ED-IN-0304 | yes that they differ; the source is deferred to CR-17 |
| R-29 | 2026-10-29 | He "ruled for the licence": a counted vote licenses or blocks the owner's own act; no declaring verb, no stored tally; consent, not command | `resolution-design.md:27,178` | yes |
| R-30 | 2026-10-30 | "resolve for me for now": the held parliament calls taken provisionally, each with a revert (no chair; quorum share 0.5; ladder stays as location; titles stand); then #527 merged by Jordan | `resolution-design.md:182`; P15 | provisional; RH-1, RH-3 and the appetite/horizon hunk held |
| R-31 | 2026-10-30 | "Ensure that character capabilities within subsystem stem from a combination of character attribute, title, office, and faction as according to venue and contest type." | this session | **yes, newest.** Clarified 2026-10-30: office licenses acts **and** carries weight, venue-keyed ("a King ... in a royal tribunal"). Narrows `06_RESOLUTION` B.0's refusals of a per-proceeding skill and an office bonus; **contradicts Layer 1 `03` §A.3** (amendment held; §1.2) |
| R-32 | 2026-10-30 | "Ensure that there is a sigma-leveraged engine with continuous dice and obstacles, and ensure that there are modifiers according to the capabilities above as well as worldly state, evidence, argument, audience and so forth." | this session | yes; restates R-5, R-6, R-22 and adds the modifier sources |
| R-33 | 2026-10-30 | "Ensure that there is a logical action surface that is used by all social contest types with the actionable possibilities limited by those social contest types, ie provide a consistent armature or subsystem engine." | this session | yes; restates R-12 and adds the limit by contest type |
| R-34 | 2026-10-30 | "There are different kinds of 'authority' for contest types: negotiation's authority is held between the contestants negotiating with the imbalance coming from differential rung positions and circumstantial leverage; a royal tribunal or parliamentary proceeding has a royal/imperial/political authority as vested by the nation itself; a religious tribunal or heresy charge has its authority come from a religious basis, but it may be modulated/undermined by royal authority if a royal person is involved. Adjudicators, consequently, will be actors whose offices are relevant to that given authority." | this session | yes, newest; fixes the source of a venue's authority and who may adjudicate (see §2.1, `bench_basis`) |
| R-35 | 2026-10-30 | "My writing about 'appeals' is about contesting the outcome of a social contest immediately after it has been rendered; an appeal to an authority, however, is something that I do want to be possible in this engine." | this session | yes, newest. **Clarifies R-2:** no immediate re-contest of a rendered outcome; an appeal to an authority is wanted |
| R-36 | 2026-10-30 | "The legitimacy of the authority, which is related to a territory in terms of political legitimacy and religious piety, then, can impact the weight/impact of the authority for a social contest. For example, a territory that places little weight in the words of Church of Solmund may not have a heresy proceeding that occurs in those lands be biased in favour of Church because the authority vested into the church is weak there" | this session | yes, newest; scales an authority's weight (R-34) by its standing in the venue's territory |
| R-37 | 2026-10-30 | "Ceiling should sit above the default so opposition can bite" | this session | yes, newest; answers the question left by `H-213` ("No ruling states the value"). **Meets R-18's M-7 check**, which fails above 2 at the 1D floor (measured: 0.0006 at Ob 3) |
| R-38 | 2026-10-30 | "office weight can affect both roll and obstacle" | this session | yes, newest; answers where an office-keyed weight enters (R-31) |
| R-39 | 2026-10-30 | "a 1D party is effectively useless and destined to lose. it's like asking a murderer who says 'i love to murder and i murdered that guy' to defend himself in a court room." | this session | yes, newest; **narrows R-18** ("don't deprive player of a chance at winning"): a 1D party facing strong opposition is *meant* to lose, so M-7's 1D-floor check is not a requirement |

### 1.0 The 2026-09-06 rulings file

`references/design_rulings_2026-09-06.md` quotes eight further rulings verbatim from the same day as R-14 to R-21.
They are about the world model, not the contest, but each constrains what a contest may write or leave behind. The
file marks itself reference (§0.05); where it and the code disagree, the code governs.

| # | ruling (verbatim) | what it fixes for a contest |
|---|---|---|
| S-1 | "war supersedes the character, typically, but if the casus belli is purely based upon the character running it, then the inheritors ... will have justification in negotiating its end." | an ending is *standing in a negotiation*, not an automatic exit; the end stays contestable |
| S-2 | "you have license to do whatever makes for the best game architecture. your only constraints are making this as dynamic and capable and flexible and emergent and persistent as possible." | the five terminal criteria; every earlier refusal is instrumental and must be argued against them |
| S-3 | "propagation across scales and domain echoes and rippling all directions in a probabilistic world driven by character interiorities and compromised by external incidents and events and pressures." | a contest is one link in a loop: act, state through the gate, witnessed claims, later decisions, changed interiors |
| S-4 | "world must churn" | pressure that changes nobody's decision is scenery; do not answer with a clock |
| S-5 | "not every fact of the world or record of event lives in memory — much of it is documented and borne bureaucratically." | a ruling's record is an object that can be moved, copied, forged, seized, burned (diegetic persistence) |
| S-6 | "the domain echo means that something that happens at one scale ... is recorded as a factual event" | a contest's result is a *fact* others read, not a magnitude pushed at them |
| S-7 | "yeah this is better" (news-speed, not instant echo) | **no magnitude carrier at any scale**; legitimacy, standing and morale are derived from stances and learned at the speed of news, so a ruler can be wrong about their own standing |
| S-8 | "I don't know the description of the person who did x"; "someone looking like y did x"; "I saw this person doing y, but I don't know what y is"; "I don't know why they were doing y" | testimony is a per-witness claim whose identity, act and motive are each independently absent, partial or wrong |

The file's own closing line is a ruling-grade sentence about this subsystem: "**propagation without reaction is a
chronicle, not a game.**"

### 1.1 What the sequence evinces (my reading, labelled as such)

1. **A contest is a host plus data rows.** Every difference between games lives in the row, never in a branch (R-12, R-15, R-25).
2. **One ladder, one resolver, one obstacle owner; no private bands, no fiat caps; a disclosed cost is accepted** rather than patched (R-5, R-6, R-8, R-22).
3. **The game must be winnable and a specialist must be rewarded.** The wrong choice may win, the right one may lose, nothing is refused outright (R-16, R-18). He accepts "not enough dice" (R-8) and rejects "no chance at winning" (R-18); the M-7 failure sat exactly on that boundary, and the code answered it with an obstacle ceiling (corrected from "remedy open").
4. **Stakes are things someone in the world can lose, and the world is told.** No internal scores as stakes; many matters per contest; results bind in the season; opinion change counts (R-11, R-21, R-26).
5. **Consent, not command; no declaring verb, no stored tally** (R-18, R-29).
6. **Coercion happens inside the target's own decision.** Fears are reusable leverage; a presser may not write into another person (R-19, R-23).
7. **No dead band and no forced result.** Partial moves the docket; an undecided hearing is acceptable play (R-1, R-17).
8. **Authored hooks, not authored arcs; persons differ in nerve and foresight** (R-7, R-28).
9. **A result is a fact that others read at the speed of news, never a number pushed at them** (S-3, S-6, S-7); a reaction must exist for a propagated fact to matter (S-3, S-4); testimony is partial by construction (S-8); the five terminal criteria outrank any earlier refusal (S-2).
10. **Process.** Ratify as intent and let code decide (R-25). Retire dead code, but hold execution when deletion breaks gates (R-14). Delegate gates, expect reversibility (R-30). Surface forks one at a time (R-3).

### 1.2 Tensions among the rulings, and questions only he can answer

- **Appeal: resolved by R-35.** R-2 (2026-07-01) barred contesting an outcome immediately after it is rendered; Jordan has since said an appeal *to an authority* is wanted. They do not conflict: no retry before the same bench, an appeal route to another authority (R-34).
- **Adopt or retire the kernel.** R-14 says retire. SC-05 records Jordan's *indirect* lean as "adopt" (from an event id, "a lean, not a ruling"). Only the timing (SM-15) is his; the plan treats it as a scheduling call (A1-58).
- **R-11(2)** ("everything in a scene binds") reopens D-8 (one-tick trials) and the outer-act degree. No row records the re-examination.
- **R-13 against this document.** The scope ban binds the proceedings *build*. This is a survey and the request named the prior work, so I read it; ED-SC-0038 is the precedent for relaying rulings the ban hid.
- **R-31 against Layer 1: answered, "both" (Jordan, 2026-10-30).** "A King has more actions that are available in some contests (e.g. a royal tribunal), and their actions also carry more weight in those contests." Office therefore licenses acts *and* carries weight, venue-keyed; the Layer-1 wording below is contradicted and its amendment is held (see the reconciliation §2.3). The trail follows. `architecture/meta/03_VERBS_AND_LOOPS.md` §A.3 reads "A seat adds no verb and no modifier", and `04_CODE_ARCHITECTURE.md:351` makes it STRUCTURAL ("no bonus field; no modifier column; `eligibility_kinds` has no `capability` member and the loader raises on one"). `06_RESOLUTION` B.0 refused an office bonus on that ground. R-31 names *office* as a source of capability. Two readings: (a) office licenses which acts a holder may take and who may be heard (its `remit_acts`, today's behaviour), while attribute, title and faction supply the numbers; consistent with §A.3. (b) office carries a numeric modifier; this requires amending a ratified Layer-1 row, which is held for his separate sign-off (RH-1, RH-3). I take (a) here `[ASSUMPTION: R-31 means the capability to act, not an office bonus; basis: it is the reading under which R-31 and §A.3 agree]`. The question is §2.3 of the companion reconciliation document.
- **Open on him:** D-6 (the "whoever touches it is killed" fault has no fail-forward move); D-7 (does a detailed denial beat a brief one; does displayed anger extract concessions); J-C-6 (may a person lie); J-13 (what sets a pool); the source of risk appetite and horizon; the held hunks of #527. `HANDOFF_SC.md` still calls ED-SC-0040 Jordan's; its last row is closed by an agent assumption (option B), so that line is stale.

### 1.3 Not rulings, though they read like them

ED-SC-0003/0005/0015 closures (read-only agent passes); ED-SC-0040 (agent assumption, revert if he authorises option A); verbs-11 R-06..R-24 and "audit ruling C1" (orchestrator reconciliations); `P-27` (1/√pool "accepted by ruling", no quote attached); every `[ASSUMPTION; medium; Jordan to correct]` tag in CR-34..CR-39.

---

## 2. The primitives, flattened

Every source below names these things differently; this is the common set. `●` marks a primitive that a ruling in §1 fixes. Status: **LIVE** (code the season loop reaches), **KERNEL** (`systems/social_contest/sim/contest/`, evaluated, not adopted), **INTENT** (proceedings design, ratified as intent), **PROPOSED**, **RESEARCH**.

### 2.1 Who is in the room

| primitive | what it is | sources and names | status |
|---|---|---|---|
| party | a person with something at stake in the matter | sides A/B (kernel); claimants; petitioner; accused; "parties" derived from edges | LIVE / KERNEL / INTENT ● R-20 |
| bench (judge, adjudicator) | who may dispose of the matter; the set is *derived* from `determine` seats whose scope contains the venue (`Query.judging_set`) | adjudicator ×4 types; panel; inquisitor; podestà; lord; sovereign | LIVE (read only for `a matter`) ● R-20 |
| floor | who may speak; `open`, `closed`, or `admitted:<basis>` | crowd; assembly; senate; "Room" | INTENT; no runtime reader |
| audience | those who witness and form a reception | the room; gallery; jury of opinion | LIVE as `reception` term ● R-23 |
| advocate, proxy, intercessor | speaks for a party; absorbs defeat but not the principal's lie | logographer; patronus; proctor; envoy | INTENT (interposition, six kinds) |
| witness, informer | supplies claims; name may be withheld. **Identity, act and motive are separate claims, each possibly absent (S-8)** | `WITNESS` deposit; Inquisition informers; Bocche di Leone | LIVE (`tell`); the three-term observation is INTENT; withheld names RESEARCH |
| chair, presiding officer | frames the question, orders the speaking | magistrate (*relatio*); lawspeaker; Speaker | not ruled; "no chair" provisional (R-30) |
| role | **never a field**: a relation to an occasion, fixed by which edges a person holds | party/advocate/audience from `commit` edges | INTENT ● R-20 |
| absent subject | declined / could not / was not admitted / did not know | `P-33` | INTENT |

### 2.2 What is contested

| primitive | what it is | sources and names | status |
|---|---|---|---|
| matter | the thing before the room; carries a **mood**: HOLDS (a past fact), OUGHT (a future act), or neither | docket item; case; motion; question | LIVE (`DocketItem`) / INTENT |
| proposition, claim | a statement that persons hold, with a source chain | `Claim`, `Proposition`; warrant; thesis | LIVE |
| prize | what the roll wins: `a standing`, `a matter`, `a proposition` | `rosters.yaml` prizes | LIVE ● R-22 |
| stakes | what the world loses: oblige, detain, ban; a seat; a Record; a standing; territory | `disposes`; tenure kinds; sanction ladder | LIVE (3 kinds) ● R-21 |
| stakes grade | terminal / costly / free (recoverability) | `stakes_grade` (scheduled for deletion) | INTENT |
| issue ground (stasis) | the *kind of question*: fact → definition → quality → jurisdiction; kernel adds consequence, feasibility | Hermagoras; Cicero *De Inv.* 1.10-19; issue ladder | KERNEL (6) / INTENT (4) |
| many matters | one contest, a vector of verdicts | "win on one, partly lose three, lose five" | INTENT ● R-11 |

### 2.3 What a person brings

| primitive | what it is | sources and names | status |
|---|---|---|---|
| standing | rank and credit, indexed to a body: A1 ascribed, A2 accumulated, A3 performed, A4 staged, by route (prestige or dominance). **Derived from stances, never pushed (S-7)** | Standing; Face; precedence | LIVE (a prize) / KERNEL (0-10 per contest, a stored number, which S-7 refuses) |
| pool | dice brought: `brought + conduct × latitude`, floored at 1D, fractional | σ-leverage d10 | LIVE ● R-18, R-22 |
| latitude | room the person has to act; low, intermediate, high; **enters the pool only** | rank-derived | INTENT ● R-18 |
| obstacle | defender's score ÷ 2 plus four room terms, floored at 1 | `obstacle()` | LIVE ● R-5 |
| proof, evidence | claims that carry weight, with age, remove, mirror and kind axes | dossier; `proofs`; hidden evidence array | KERNEL / INTENT |
| burden token | who must prove: accuser, respondent, lower standing, none | `gate(burden)` | RESEARCH / KERNEL |
| capacity | nine learnable skills (calibrate reception, classify the institution, elicit, discriminate evidence, control display, calibrate rank, reframe, remember, time) | study Fig. 12/22 | RESEARCH |
| conviction, ambition, fear, secret | what a person holds; **fears are reusable leverage, secrets are spent** | `Person.convictions`; pursuits | LIVE / INTENT ● R-19 |
| temperament | risk appetite; horizon (short, medium, long) | ED-IN-0304 | open ● R-28 |

### 2.4 What a person can do (move classes)

These are the corpus's verbs, kernel moves, Nyāya terms and figures sorted into classes. No new verbs are proposed.

| class | members as named in the sources | status |
|---|---|---|
| **frame** | convene (a Date); open a case; petition; carry/lodge; propose a motion; relatio; charge (*libellus*) | LIVE (`convene`, `open_case`, `petition`, `carry`) |
| **assert** | tell; utter; claim; commit to a proposition | LIVE (`tell`, `utter`, `commit`) |
| **support** | present proof; testify; support; construe; amplify | KERNEL / INTENT |
| **attack** | rebut; undercut; undermine; refute; object; impugn; shift; *chala*, *jati* | KERNEL / INTENT |
| **probe** | question; interview; interrogate; surveil; examine | LIVE (inquiries) / INTENT |
| **argue** | argue (moves a hearer's pursuits); persuade | LIVE (`argue`) |
| **concede, descend** | concede; pre-empt; recapitulate; step down the issue ladder; the six-rung descent (deny the act → deny the law applies → admit and justify) | INTENT |
| **escalate, translate** | appeal; forum challenge (*translatio*); remonstrance; *lettre de jussion* | INTENT / RESEARCH |
| **bind** | commit; covenant; oath; give; the *kishomon* self-curse | LIVE |
| **withhold** | abstain; silence (priced only where a lawful act was available); veto; *intercessio* | INTENT |
| **display** | praise, blame; supplicate; ceremony; precedence | RESEARCH / KERNEL |
| **assess covertly** | *liang-quan*, *chuai-qing* (weigh power, estimate disposition); *bai-he* (open/close) | RESEARCH |
| **side-channel** | logroll; bribe; whip; intercede | PROPOSED; no verb exists |
| **enforce** | arrest; seize; issue; comply, evade, defy | LIVE |

Of these, five verbs carry a social prize in code: `tell`, `argue`, `speak`, `determine`, `arrest`. `petition`, `carry`, `convene`, `open_case`, `utter` and `commit` are uncontested. `persuade`, `lodge`, `declare`, `lie`, `vote` and `interrogate` are **not** rows (R13 ran the verb table).

### 2.5 Persuasion modes (why a move lands)

| mode | content | source | status |
|---|---|---|---|
| ethos / pathos / logos | speaker's projected character; audience's emotional state; the argument | Aristotle *Rhet.* I; kernel appeals | KERNEL; **ruled out as fields** (ethos and bias are not fields; `06_RESOLUTION.md`) |
| three genres | deliberative (future, advantageous), forensic (past, just), epideictic (present, honourable) | Aristotle *Rhet.* I.3 | INTENT (derived from matter mood) |
| topoi and the enthymeme | reusable argument seats; the rhetorical syllogism | Aristotle | thin: one line each in the repo |
| central and peripheral routes | elaboration likelihood | Petty and Cacioppo | RESEARCH |
| story model | jurors judge by coverage, coherence, uniqueness | Pennington and Hastie | RESEARCH |
| levers | reciprocity, commitment, authority, scarcity; reactance; inoculation | Cialdini; Brehm; McGuire | RESEARCH |
| anchoring and logroll | first offer sets the range; trade across issues | Galinsky and Mussweiler; Raiffa | RESEARCH |
| desire and fear | *yang-yan* (persuade by wants), *yin-yan* (by fears); target believes the decision his own | *Guiguzi*; *Han Feizi* | RESEARCH |
| aptness | fit of speech to genre and rung | study | INTENT ● R-16 priced, not refused |
| reception | what the room takes the move as; a function of standing; can flip a band's sign | study; eight shapes | LIVE as terms ● R-23 |

### 2.6 How a contest runs (procedure and resolution)

| primitive | what it is | status |
|---|---|---|
| venue, arrangement | a data row with 13 keys: `disposal` {bench, mutual, none}, `bench_basis`, `floor`, `records_dissent`, `venue_min_rank`, `term_required`, `appeal_basis`, `interposed`, `order`, `proofs`, `disposes`, `disposal_reach`, `quorum` | 8 rows loaded; **only `disposes` is read at runtime** ● R-12 |
| speaking order | free, rank, alternating, scripted, written-only | INTENT; no reader |
| act | one move by one attendee, one draw | LIVE |
| exchange count | 1 to 5 alternations | KERNEL only |
| sitting | a Date that fires and forms an empty docket slot | LIVE (rare) |
| one draw | pool against obstacle gives a margin; `degree_from_net` gives Overwhelming / Success / Partial / Failure | LIVE ● R-5, R-6 |
| persuasion track | a 0-10 gap moved by each argument; bands A_total … B_total | KERNEL only |
| verdict rules | exchange majority; jury vote weighted by discipline; ProofBar; ThresholdRace; GraceThreshold; count at close | KERNEL |
| consensus cascade | consensus, then lot, then majority | Althing (RESEARCH) |
| licence by count | a count licenses or blocks the owner's own act | INTENT ● R-29 |
| clock | enactment clock; term; sitting due-date | PROPOSED |
| information rule | who learns what: `WITNESS` deposits to all present; sealed room; withheld witness names | LIVE / INTENT ● R-21 |

### 2.7 What follows

| primitive | what it is | status |
|---|---|---|
| disposal | oblige, detain, ban; a Record; a licence; a seat conferred or revoked | LIVE (3 kinds) |
| disposal reach | who learns the ruling: room, body, or a rung | INTENT ● R-21 |
| fail-forward | Partial writes a docket matter; every band leaves the proceeding somewhere different | LIVE ● R-17 |
| record | a durable object that later contests may cite, and that can be moved, copied, forged, seized, burned (S-5) | PROPOSED (kernel leaves only stat deltas) |
| opinion drift | members' pursuits move; counts as world impact | PROPOSED ● R-26 |
| appeal basis | which authority a rendered outcome may be taken to, never back to the same bench at once (R-35) | INTENT; unread |
| enforcement | promulgation is not enforcement; compliance, evasion, defiance | LIVE (verbs); delivery by `give` does not form |

---

## 3. The kinds of contest

The proceedings design derives every game from three sets (parties, bench, floor) plus one declared key,
`disposal`, with values `bench`, `mutual`, `none` (`00_DERIVATION.md:45-83`). That is the structural axis of the one design Jordan ratified (as intent), so the kinds below are cut along it; the
kernel and the live module do not use it. The remaining axes (question tense, burden, proof regime,
order, ladder) set the *procedure within* a kind.

| axis | values found in the corpus |
|---|---|
| who decides (`disposal`) | nobody but the target (dyadic); the parties jointly (`mutual`); one third party (`bench` of one); a panel by ballot; a floor of members by count; an audience with no formal power |
| tense and mood of the question | past, HOLDS (forensic); future, OUGHT (deliberative); present, neither (epideictic) |
| burden | accuser; respondent; lower standing; none |
| proof regime | witness count; confession; probe of a hidden array; ordeal (refused, §1); acclamation |
| order | alternating; rank; scripted; free; written only |
| symmetry | two equal sides; or the institution is one side and the other's resistance is halved |
| forum | fixed; or itself contested (composition, jurisdiction) |

### 3.1 The eight kinds

**K1. Dyadic influence** (no decider; the other person is the target).
*Instances:* rumour, testimony, confession, warning; arguing a point to one hearer; counsel to a ruler; frank speech to a
superior; covert persuasion (*Guiguzi*); personal appeal.
*Performed:* assert or argue → one draw against the hearer's obstacle (score ÷ 2 plus room terms) → the hearer's claims or pursuits move.
*Status:* `tell` is the only contest that runs on every seed; `argue` is wired but formed 0 of 83 persons at seeds 0 to 2 (figure from the #530 report, not re-measured by me); content-blind (the proposition is never read).
*Rulings:* R-5, R-19, R-23.
*Research supplies:* the target types (counterpart, audience, superior, peer under distrust); desire and fear; the licence conditions for frank speech (goodwill, private, unrepeated, no visible advantage); the six-rung descent when answering a prejudicial attack (Aristotle *Rhet.* III.15, by the study's reconstruction).

**K2. Negotiation** (`disposal: mutual`; no bench; burden none).
*Instances:* private negotiation; envoy negotiation; audience or embassy; treaty; transfer between two characters; Kautilya's *sama / dana / bheda / danda*; Duel of Wits.
*Performed:* approach → mandate (an envoy's latitude: plenipotentiary, limited brief, message-bearer) → anchor and counter-anchor → exchange → pressure → impasse or close → bind (`commit`, then `give`).
*Status:* kernel has a private_negotiation proceeding; the negotiation *game* is a stub; the proceedings row is unseeded; **a negotiation cannot complete in computed play** (H-229).
*Rulings:* R-11 (agreement binds in scene; many matters), R-18 (five-party settlements accepted), R-19.
*Research supplies:* a hearing with the burden token removed (source 01); anchoring, logroll and reactance (source 04); supplication binds the stronger party; the oath form escalates as trust falls (*kishomon*).

**K3. Adjudication** (`disposal: bench`; a third party rules on a past matter about a person).
Subkinds differ only in the keys named.

| subkind | burden | proof | order | note |
|---|---|---|---|---|
| accusatorial trial (`legal_trial`, formal contest) | accuser | witnesses; *litis contestatio* fixes the issue | alternating | Roman *quaestio*, canonical *ordo iudiciarius*: *libellus*, issue joined, proofs graded (two witnesses = full proof; confession "queen of proofs") |
| inquisitorial hearing (`tribunal`, `interrogation`, `inquisition_hearing`) | respondent | hidden dossier probed; witness names withheld | inquisitor proposes | Gui *Practica* (1323), Eymerich (1376); abjuration the usual outcome; the accused's resistance is halved to compensate for the tilt |
| political tribunal | lower standing | informers; secrecy | scripted | Council of Ten, State Inquisitors (1539), Foscarini 1622: no public trial, no cross-examination; posthumous exoneration |
| arbitration (`arbitration`, `guild_arbitration`) | neutral | party submissions | alternating, then a ballot | panel of jurors weighted by discipline |
| excommunication (`excommunication_deliberation`) | institutional | canonical | bench | a cross-ladder demotion; Cadaver Synod |
| appeal | the appellant | the record | written | `appeal_basis` names the other authority it may be carried to (R-35) |
| audit, inspection | none | the books | outside auditor | *residencia*, *visita*, Carolingian *missi*, Venetian *sindici* |

The burden and order cells for arbitration, excommunication, appeal, audit and the political tribunal's order are my
inference from the sources' general pattern, not a source's statement; the others are sourced.

*Performed:* convene (a sitting) → frame (open case, docket item) → issue gate (stasis, a four-rung ladder) → burden → acts (speak, tell, produce proof, question) → `determine` by the bench → disposal → disclosure by `disposal_reach` → appeal if the row has one.
*Status:* `determine` runs rarely and only on one measured seed; `speak` writes nothing; a computed `open_case` never names an arrangement, so every computed determination opens an `oblige`; the kernel's `church_tribunal` favours seat A at 84.2% to 84.7% (three documents, three figures) from its track start of 6 alone.
*Rulings:* R-2 (appeal), R-10 (degrees read from the scene), R-11, R-14, R-16, R-18, R-21.

**K4. Petition and supplication** (a bench of one who is unbound; grace, not right).
*Instances:* royal audience; English Ancient Petitions (more than 17,000, complaint against request; common against private); French *supplique*; memorial; the sovereign's grace.
*Performed:* petition (a Record) → `carry` into a docket slot → the addressee `determine`s or lets it lapse. There are no deny or withdraw verbs.
*Status:* verbs built; computed petitions are addressed to the subject themselves; the kernel's `royal_audience` runs three exchanges with the institution as the opponent.
*Research supplies:* the register is indexed to the petitioner's rank (*insha'*, *ars dictaminis*: *salutatio*, *captatio benevolentiae*, *narratio*, *petitio*, *conclusio*); intercessor and patron decide success; the Parlements' *remontrance* ladder (*remontrance*, *jussion*, *remontrances itteratives*, *lit de justice*): contest an edict before registering it.
*Rulings:* R-1 (lapse is acceptable), R-17.

**K5. Panel and jury** (`disposal`: a ballot by a small body).
*Instances:* Athenian *dikasteria* (timed by water clock, no professional judges); Roman *quaestiones*; guild arbitration; Venetian *Quarantia*; trial jury.
*Performed:* speeches → each member votes, weighted → majority or threshold.
*Status:* KERNEL only (jury vote weighted by discipline; Panel closure ED-1057/1059).
*Research supplies:* who sits is the larger contest (Roman *album iudicum* fought for about fifty years while the statute never changed); group dynamics (faction size, first ballot, normative against informational pressure).
*Rulings:* R-2 (weighted by standing).

**K6. Deliberation by count** (a floor of members who are also parties; consent, not command).
*Instances:* parliament at four rungs; council of state; Roman Senate (*relatio*, *sententiae* by rank, *discessio*); Althing and *thing*; synod; conclave; Venetian Great Council and the 1268 doge election (nine alternating lot and election stages); Florentine *balìa*.
*Performed:* convene for a **reason** (a docketed matter; a vacant seat; a shortage; a war) → frame the motion → floor speaks in order → commits are counted → the count **licenses or blocks the owner's own act** → the member's opinions drift.
*Status:* PROPOSED. Two `disposes: Record` rows exist (`parliamentary_debate`, `council_of_state`), but `determine` refuses any arrangement that disposes a Record, so they decide nothing. No chair, speaker, minutes, vote, veto or filibuster verb exists. The only live parliament-like thing is the interim King-and-Regent bench.
*Rulings:* R-9, R-18 (tally accepted), R-26, R-27, R-29, R-30.
*Research supplies:* speaking order is a function of standing; the Althing's consensus, lot, majority cascade; the Senate's *intercessio*; the 3-mark fines for procedural failure.

**K7. Display** (an audience with no formal power whose reception sets standing).
*Instances:* coronation, eulogy, public oration, sermon, praise and blame, the staged audience.
*Performed:* an act before the room → reception → a standing delta. Epideictic, per Aristotle: "nothing is at issue".
*Status:* the proceedings design **demotes public debate to a degenerate case** (eleven games plus one); `disposes: standing` is forbidden (R-21).
*Rulings:* R-21 (a standing is not a stake that someone can lose in the world; no internal scores).

**K8. Contests over the contest** (the forum, the jurisdiction, the enforcement).
*Instances:* who sits (composition fights; Florentine *ammonizione*, disqualification without trial); *translatio* (forum challenge); an emergency organ re-classifying ordinary business as security (Venice 1582); nomination and confirmation; deposition by no-confidence; election; succession; writ and compliance; arrest and seizure.
*Performed:* these are the same moves as K3 or K6 aimed at a seat or a jurisdiction instead of a matter; election is `determine`, not `confer` (AX E.3).
*Status:* verbs `confer`, `revoke`, `succeed`, `arrest`, `seize`, `issue`, `comply` exist; election and deposition are RATIFIED unbuilt; nothing contests jurisdiction.
*Rulings:* R-9 (a duke may revoke within purview), R-14.

### 3.2 Where the live subsystem actually sits

The season loop reaches **K1 only, plus a thin edge of K3** (`speak`, `determine`, `arrest`, `open_case`). Every other kind is data, kernel, or intent. That is the plain answer to "what is it building from": the code executes one roll; the ratified design is a host with twelve data rows; the kernel is a third system with a different resolver that nothing in the game calls.

### 3.3 The twelve proceedings rows against the eight kinds

Eight rows are seeded; five are not. `public debate` is demoted to a degenerate case, which leaves eleven.

| row | seeded? | kind |
|---|---|---|
| arbitration | yes | K3 |
| legal_trial | yes | K3 |
| tribunal | yes | K3 |
| interrogation | yes | K3 |
| inquisition_hearing | yes | K3 |
| excommunication_deliberation | yes | K3 (K6 if read as a synod) |
| parliamentary_debate | yes | K6 |
| council_of_state | yes | K6 |
| negotiation | no | K2 |
| negotiation through envoys | no | K2 |
| audience / embassy | no | K4 (K2 if between rulers) |
| appeal | no | a route from K3 or K4 to another authority (R-35) |
| public debate | no | K7 (degenerate) |
| examination | authored to test closure | K3 |

---

## 4. How each kind performs the same stages

Every kind is a pass through the same stages; the kinds differ in the value each stage takes. The first line gives the
ruled engine that all kinds share: one draw per act, pool against obstacle, `degree_from_net` to four bands,
Partial writes a docket matter (R-5, R-6, R-17, R-22).

| stage | K1 dyadic | K2 negotiation | K3 adjudication | K4 petition | K5 panel | K6 deliberation | K7 display | K8 forum / enforce |
|---|---|---|---|---|---|---|---|---|
| **convene** | co-presence | an approach, a Date | sitting on a Date | a petition Record | sitting | a reason A to L (matter, vacancy, shortage, war) | an occasion | a vacancy, a writ, a challenge |
| **frame** | the topic | agenda: existence, valuation, authority | charge; issue joined | grievance or request | as K3 | motion (OUGHT) | none | the seat or order |
| **gate** | none | mandate | issue ladder (fact, definition, quality, jurisdiction) | none | as K3 | procedural motions first | none | jurisdiction |
| **burden** | target | none | per subkind (§3.1) | petitioner | per subkind | mover | none | challenger |
| **acts** | tell, argue | offer, counter, press, concede | speak, produce proof, question, impugn | supplicate, intercede | speeches | speak in rank order, commit | oration, praise or blame | the K3 or K6 acts |
| **decide** | the draw | agree or impasse (`mutual`) | `determine` by the bench | the addressee | weighted ballot | count | reception | `determine` or the holder's act |
| **dispose** | claims or pursuits move | `commit`, `give` | oblige, detain, ban; a Record | grant, deny or lapse | as K3 | licence or block of the owner's act | a standing delta (forbidden as a stake) | tenure, seat, seizure |
| **reach** | those present | the parties and their principals | `disposal_reach`: room, body, rung | the petitioner | as K3 | the body, then the world | the room | the realm |
| **after** | none | bond, reputation | appeal basis; record | precedent | none | opinion drift; lapse event | none | compliance, evasion, defiance |

---

## 5. What the historical and theoretical material contributes, by primitive

Contributions are listed against the primitive each supplies (§2), not by author. Items marked ◇ are named in the
repo's own research with the repo's own caveat that the primary text was not read.

| primitive supplied | contribution | source |
|---|---|---|
| issue ground | four stases: conjectural (*an sit*), definitional (*quid sit*), qualitative (*quale sit*), translative (jurisdiction). Hermagoras excluded legal-textual questions (Heath 1994, read directly per the doc); the thirteen *status* of Hermogenes are a school-declamation inflation. Stasis is a *forensic* doctrine; deliberative argument runs on *topoi* | Cicero *De Inv.* 1.10-19; Quintilian 3.5-6, 7.2; Heath |
| descent | status as a fallback ladder: deny the act, deny the law applies, admit and justify | Lausberg |
| persuasion modes | ethos, pathos, logos; three genres by tense; the enthymeme | Aristotle *Rhetoric* ◇ |
| move: concede | six responses to a prejudicial attack, ordered by what each concedes | Aristotle *Rhet.* III.15, as reconstructed by the study ◇ |
| process | five canons (*inventio*, *dispositio*, *elocutio*, *memoria*, *pronuntiatio*); six oration parts; three styles | Cicero; Quintilian (source 04) |
| burden, proof | *libellus*, *litis contestatio*, graded proofs; confession as "queen of proofs" | Tancred, *ordo iudiciarius* (c. 1216) |
| information rule | informers' names withheld (16 of 48 at Délicieux 1319; Hus 1414); the five-part inquisitor's manual; abjuration | Bernard Gui; Eymerich (via Hill 2019) ◇ |
| institution | Council of Ten: tribunal of 1310, permanent 1355 (1334 in a verifier note; the files disagree); State Inquisitors 1539; *Avogadori* (legality guardians); *Quarantia*; the *promissione* oath rewritten each accession; no separation of powers, the overlap is the mechanic | Venetian research |
| selection | the 1268 doge election: alternating lot and ballot over nine stages (30, 9, 40, 12, 25, 9, 45, 11, 41 electors; 25 of 41 to carry) | governance research |
| scope creep | an emergency organ reclassifies ordinary business as security (Venice 1582) | conflicts research |
| order | *relatio*, *sententiae* in rank order, *discessio*; *intercessio* | Roman Senate |
| cascade | consensus, then lot by quarter, then majority; weapon-clash assent; 3-mark fines for procedural failure | Althing; *Grágás* |
| forum composition | the jury roll fought over for decades while the law stood | Roman *quaestiones* |
| petition | complaint against favour; the register indexed to rank; the escalation ladder | English Ancient Petitions; *supplique*, *remontrance* |
| debate types | *vāda* (truth-aimed), *jalpa* (victory-aimed), *vitaṇḍā* (refutation only); 22 *nigrahasthāna* (defeat conditions) adjudicated against a checklist; pre-debate triage of opponent standing and assembly | Nyāya; *Caraka-saṃhitā* ◇ |
| covert persuasion | assess before acting; the hidden "reverse scale" that ends the encounter; being seen to divine the target's mind is lethal | *Guiguzi*; *Han Feizi*, *Shuinan* ◇ |
| diplomacy | envoys typed by latitude; four *upāya*; six *ṣāḍguṇya*; seating and precedence negotiated before speech | Kautilya; Liudprand |
| audit | outside auditor in mixed pairs; end-of-tenure judicial review; unannounced inspection | Carolingian *missi*; Castilian *residencia*, *visita* |
| influence | central and peripheral routes; story model; reactance; inoculation; anchoring; first-ballot effects | Petty and Cacioppo; Pennington and Hastie; Brehm; McGuire; Devine |
| game warnings | spend-resources-to-influence-rolls is "a lot less fun than fighting" (Griftlands); the Duel of Wits collapses to Point and Dismiss; Dogs in the Vineyard's flaw is "Give" immediately when losing | designers' statements |

---

## 6. Gaps, conflicts and what could not be verified

**Ranked, worst first.**

1. **Three resolvers share one name.** The v30 exchange algebra (prose, no engine), the kernel `Bout` with its Persuasion Track, and the live one-draw margin. They overlap only at the track's band thresholds. The proceedings design adds a fourth shape (serial acts, one draw each) that nothing executes.
2. **The vocabulary of "kind" is used at four levels:** venue or proceeding (eight in the kernel, eight arrangement rows, twelve designed games), game type (agon, consensus, negotiation, inquiry), verb, and genre. Counts disagree: arrangement keys 13, 14 or 15; games twelve, eleven plus one, or thirteen; speech kinds six, ten, twelve or fifteen; obstacle terms four or five.
3. **Most of the research sits where nothing reads it.** The v30 design, the audit and its sources are in `.designs/` and `.audit/`, which the repo rules quarantine; the stasis ladder, armature and Appraise are reachable only through the kernel.
4. **Venice and the Inquisition are covered at the level of offices and outcomes, not trials.** The only stage-by-stage Venetian procedure in the corpus is the 1268 election. The Inquisition appears as withheld witness names, a manual's five parts and abjuration. Compurgation, ordeal (except Savonarola's trial by fire), canon-law procedure and burden of proof have no hits in the institutional research.
5. **Cicero and Quintilian are thin.** The repo carries stasis, the five canons, six oration parts and three styles; it does not reproduce Cicero's *officia oratoris* (*docere*, *delectare*, *movere*) or Quintilian's *vir bonus* as a mechanism. Aristotle's *topoi* get one line and no list.
6. **Influence psychology is named, not reproduced.** Cialdini-type levers appear only in audit source 04; the SC research file names a dozen studies without their mechanisms. The study verified ten entries directly; the rest are `[UNVERIFIED]`. It also contradicts the classical corpus on denial detail, displayed anger and indirection (D-7 is open).
7. **A pointer that leads nowhere.** `research/fa_se_historical_precedent_research_v1.md:75-77` cites a "13-family catalog of pre-1600 decision procedures" (ostracism, Venetian lot-ballot, conclave, *liberum veto*, …) from a 2026-06-28 research set. No file location is given and no file was found.
8. **Figures that disagree.** The church tribunal's seat-A share is 84.5%, 84.2% and 84.7% in three PR #530 documents (measured at different commits). The progymnasmata number is 14 and 12 inside one file. The King-dies-at-tick-0 claim has three bases and none reproduces.
9. **Stale text.** `references/module_contracts.yaml` still says the kernel is "reached live only via `emergency_council`". The completion proposal's "nothing here executes" header is stale; one of its five items has landed in part. The proceedings docs' `shape.py:NNNN` citations cannot sit in the only tracked `shape.py` (534 lines).

**Not checked by me.** Every line cite into `engine/season/` and every measured rate is a reader's report. Two readers executed code (the verb-table and arrangement import; the kernel self-test, which returned `(True, [])`) and one opened four of the report's claims. I ran nothing myself. `[CONFIDENCE: medium]` on §3.3 (the mapping of rows to kinds is mine) and on §1.1 (my reading of preferences; the rows in §1 are sourced).

**Not examined.** The 2026-10-30 JSONL stress logs and the `.py` probes (figures taken from the three PR #530 reports); `_kernel_tests.py`. `references/design_rulings_2026-09-06.md` I read in full myself (§1.0), but its `shape.py` and `engine/season/` line cites predate the merge of those trees and were not re-opened.
