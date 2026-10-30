# Part 2 verdicts — C (argument and persuasion), E (negotiation), F (faction, patronage), M (persons as inputs)

## Status: **REFERENCE (2026-10-29).** Verdicts of fit; continues `2026-10-29-debate-fit-adjudication.md`, whose status, method and limits apply here. Judgments, not tasks.

Adjudicator: Opus, terminal pass. Tree read: `C:\Github\ttrpg-parliament`. Judgments of fit, not tasks.

## 0. The filter every cluster here passes through

A mechanism matters here only if it can **change a vote or an acceptance about a subject**, made by persons from their own inputs. I opened the four places that decide that:

- **`argue`** (`person_q.py:638-658`, `effects_information.py:555-581`): on a win each held pursuit moves toward **the arguer's own weight**; the Proposition must exist (`verb_table.yaml:136-144`) and is **never read**. Arguing for and against a motion is the same act.
- **The roll** (`roll.py:63-125`): `leverage` is 0; `argue` has no capability row and 1 of 430 persons holds any capability (`rosters.yaml:1223-1233`). **Everyone argues at pool 2.**
- **The chooser** (`choose.py:130-151`): verb-only pursuit term + regard of the subject + an inert `urgency`. Every `commit` scores alike; nobody holds regard of a fresh Proposition. **No risk term, no horizon term.**
- **`speak`** writes nothing (H-63); `reception`/`proofs` do not enter the `a proposition` prize.

So, today, **no mechanism in this group can change a vote about a subject.** They sort into five classes by the channel they would ride once content reaches it:

| class | channel | reaches a vote? |
|---|---|---|
| **logos** | `argue` → `Person.pursuits` (AX-3: argument moves what is held right) | only if `argue` pulls along the motion's predicate verb and `commit` reads it (the proposal's builds 1-2) |
| **ethos** | deed claims → `regard` → `stance_term`; `reception` → obstacle | yes, for acts whose subject is a person; for a motion only if `commit` reads the sponsor's standing |
| **truth** | `tell`/WITNESS → claims | only where the motion is a HOLDS matter about a person (forensic); AX-3 forbids evidence moving an OUGHT |
| **odds** | obstacle or pool terms (genre aptness, register, latitude, stasis aptness) | never by itself: it scales the chance that some other channel fires |
| **craft** | arrangement, ornament, delivery of an utterance | never: the engine has no utterance content to arrange |

That table is the main finding; each verdict below is a placement on it.

---

## 1. Clusters and verdicts

### C1 · Two tracks: evidence moves what is true, argument and consequence move what is right — **ALREADY-HELD**
Entries: CD-055, PR-005, CL-074 (ladder as AX-3 made procedural), CL-075, CD-029, PR-084 (part).
- **NERS.** N holds in every direction tried: cut it and evidence could "prove" a policy. Top-down (axiom → verb rows), bottom-up (`argue` writes pursuits, `tell` deposits claims), lateral (`determine` consequence-moves the judge, `person_q.py:615`). R-complete hole: the consequence Failure arm is unbuilt (H-221). S: one `DEGREE_STEP` ladder moves both pursuit writers. E: one axiom carries a whole verb split.
- **No-player story:** a judge drifts toward what his rulings were (CODED). **Persons:** the same evidence leaves two persons holding different "right". **Fails a player:** proof brought to a policy debate does nothing, unexplained — a legibility cost. **Evidence:** RATIFIED (opened) + CODED.

### C2 · Logos on the motion: an argument that moves the hearer toward the content argued — **FITS-IF-ADAPTED**
Entries: CD-028, CD-101, OP-035, CL-001 (logos), CL-011, CL-042, CL-047.
Adaptation: the won `argue` pulls along the motion's predicate verb (`pursuit_lean`), not the arguer's whole profile.
- **NERS.** As coded, N fails laterally: the pull is identical whatever is argued — a "become like me" charm verb labelled argument. Adapted, N holds in all six directions: AX-3 routes rightness through `pursuits`, and `argue` is that field's only person-to-person writer. S: `pursuit_lean` already owns the dot for the scar test, the consequence move and the chooser (`person_q.py:599-612`). R at the extreme: a predicate verb with a zero alignment row moves nothing (an honest dead motion). E: one reader swapped for another.
- **No-player story:** adapted, two dukes arguing a cession pull a third toward or away from `give`-shaped acts generally, so he later yields a ford nobody asked about — spill as churn. CODED (profile pull) / NOTCODED (content pull). **Persons:** only held keys move, so the hearer's shape survives. **Fails a player:** today arbitrary — arguing against a motion can move the hearer toward it. **Evidence:** CODED, opened; direction marked `[ASSUMPTION]` in the code.

### C3 · Ethos as standing held by the hearers (reception), not as a tracker — **ALREADY-HELD**
Entries: CD-032, CL-081, CL-100, CL-070, PR-059 (ethos is not a field), PR-075, PR-077 (standing), CL-047 (forum corruptibility).
- **NERS.** N holds top-down and laterally: two benches of one arrangement play differently because different people sit (PR-075) — what keeps a proceeding unsolvable. **Two defects:** (1) it reads others' ledgers inside the fold (Layer 1 F8); option B, re-source from commits, is ruled and unbuilt (CD-054, OP-100); (2) it enters only `speak`'s prize and `speak` writes nothing, so **reception today moves no vote and no state**. S: one obstacle owner; under ceiling 2 a hostile room cannot raise a defaulted obstacle (H-213).
- **No-player story:** a rumour makes a harder room nobody knows is harder. **Persons:** differentiates by what each hearer holds. **Fails a player:** inert now; later legible only as fiction, by design. **Evidence:** CODED (`world_q.py:581`) vs a RATIFIED constraint (F8).

### C4 · Proofs: evidence as inventory, the mirror test, graded proof — **PARTIAL** (forensic matters only)
Entries: CD-033, CL-080, CL-082, PR-015, CL-046, CL-079, OP-064, PR-084, OP-025, CL-101, CL-061.
- **NERS.** Aristotle's atechnic/entechnic split is already `Claim` vs `Act` (CL-046 carried). The mirror test is coded but **0 on every computed pair** (WITNESS gives an actor his own deed, H-216) and reads the opponent's ledger (F8). Graded proof from `Claim.source` (OP-064) needs no store; forgery is already `forgery_quality` (`roll.py:96-106`). By C1, N holds only on the truth track: for a parliament, narrowed to motions naming a person party and turning on a deed.
- **No-player story:** at tribunal scale, record custody becomes power (OP-064). **Persons:** witnesses chosen by stance, not truth (PR-084). **Fails a player:** one `speak` spends every proof, so hoard-or-spend does not exist (CD-033). **Evidence:** CODED + INTENT; proof-ranking inversion is RESEARCH (UNVERIFIED figure).

### C5 · The forensic ladder: stasis and Aristotle's six concession responses (with `speak`) — **PARTIAL** (forensic matters with a person party; not deliberation)
Entries: CL-004, CL-005, CL-006, CL-007, CL-008, CL-074, CL-076, CL-091, CL-092, CD-085, OP-002, CL-106, OP-062, CD-011, CL-077, PR-094, OP-036, PR-048, PR-049, PR-096, PR-080, PR-010, CD-012, CD-013.
- **NERS.** N holds top-down at a trial: which ground the fight is on decides which carrier moves (conjecture → claims, quality → pursuits), C1 made procedural. It fails for deliberation: an OUGHT motion has no issue ladder (proposal §8; CL-008 retracts the deliberative "final headings"). **Tree:** `ladder_rungs` holds Aristotle III.15's six responses, labelled "the forensic issue ladder"; stasis itself has no carrier (CL-076); `SPEECH_KINDS` has no production reader (opened: loader and tests only); the nested run is unbuilt; `speak` writes nothing. The kernel's upward-only ladder with a +1D genre match is a flat bonus (NERS §3, disqualifier 5). The fit form is OP-062/CL-075: the rung you stand on is what you conceded; descent is irrevocable and the cost is a witnessed claim, not a penalty field.
- **No-player story:** a witnessed concession travels and is cited seasons later. NOTCODED. **Persons:** neutral. **Fails a player:** inert today. **Evidence:** CODED data with no reader; INTENT; four stases web-verified, Hermagoras's own formulation UNVERIFIED.

### C6 · Genre as which carrier a proceeding moves; aptness priced, not refused — **FITS-IF-ADAPTED**
Entries: CL-002, CL-078, PR-027, PR-050, PR-051, CL-014, OP-003, OP-097, OP-031, CL-013, CL-031, PR-045, PR-074, PR-038, CL-048 (three styles).
Adaptation: genre is a Query over the bench's remit naming the live track (forensic → claims, deliberative → pursuits, epideictic → standing only); a mismatch costs one obstacle term. No style cards, no +1D, no 12×12 coefficient table.
- **NERS.** Aristotle's three genres line up with the engine's three carriers, so genre names which write an act makes rather than adding a mechanism. That is high E, and N holds vertically and laterally. The kernel's genre-match die and the faction style boosts (OP-003) are false N-lines (a flat bonus; a faction acting). Epideictic as "`speak` with no bench" (PR-074) fits: it deposits claims and disposes nothing. Aptness on its own is odds-class and changes no vote. The `genres` roster is loaded and nothing derives genre (CL-078).
- **No-player story:** a man who praises the Crown at a feast changes who will hear him at the next trial. **Fails a player:** gamey if aptness reads as the one right answer; PR-051's "the wrong move can still land" is the defence. **Evidence:** CODED rosters with no reader, INTENT, CLASSICAL.

### C7 · Defeat by named fault (Nyaya *nigrahasthana*, DefeatCatalogue, F1-F12 force-close) — **MISFIT**
Entries: CL-022, CL-023, CL-094, CD-087, CL-096, OP-063, OP-061, OP-070, CL-105.
- It needs per-exchange state (the unbuilt nested run) and a semantic judge of "evasion", "quibble" or "off the live issue" that no person can evaluate from what he holds (NERS C3: it would be an omniscient oracle). It is a second, non-die ending beside the one σ roll, which fails S's methodology test, and a checklist ending is solvable. The one fault with a carrier is self-contradiction: arguing a Proposition incompatible with one's own live commit (GV-082's incompatibility test). It belongs in C8 as a witnessed cost, not as a close. *Vada*, *jalpa* and *vitanda* as modes are arrangement rows, which `arrangements.yaml` already is. **Persons:** flattened (a fault is the same for everyone). **Evidence:** the kernel is coded but not adopted; the count of 22 comes via Vidyabhusana, not the primary text.

### C8 · Overshoot priced through witnesses (CR5 self-backfire, self-gating, reactance, the frank-speech licence, tempting moves, fail-forward bands) — **FITS-IF-ADAPTED**
Entries: CD-086, CL-093, CL-025, CL-084, PR-066, PR-028, PR-086, CL-053, OP-008, PR-080, PR-049, CL-066.
Adaptation: the cost of a failed or unlicensed move is an Event witnessed by those present, read later through `regard`. No Face tracker, no Doubt Marker, no −2.
- **NERS.** Today `argue`'s Failure writes `[]`, and a failed argument costs nothing (proposal §7). Maximum pressure every turn therefore dominates, which is CL-053's own warning and an R-CHOICE failure at every playable seat. Every carrier already exists (witnessed acts deposit claims; `regard` reads deeds), so N holds bottom-up and laterally at the cost of one emit. PR-066 is the correct E-legibility reading: *"a player who sees −2 has been told the answer"*. The kernel's licence rule (`opp < my − 1.0`) is scripted; drop it.
- **No-player story:** a lord who browbeats the council is quietly marked by those who heard him, and his next petition meets a harder bench. Strong R-world. The cost is NOTCODED; the carriers are CODED. **Persons:** varies with who witnessed and what each values. **Evidence:** INTENT plus a kernel coded but not adopted. Van Kleef is RESEARCH; Brehm is UNVERIFIED.

### C9 · Reading the hearer by acting on him (Guiguzi, Han Feizi, Plato's *Phaedrus*, elicitation, the explanation contract) — **ALREADY-HELD**
Entries: PR-004, CL-083, CL-019, CL-020, CL-021, CL-063, CL-064, CL-066, CL-043, PR-067, PR-065, PR-056, PR-011, PR-054, CL-009, CL-088.
- Held by AX-2 (no privileged access) and by `choose` receiving a PersonInterior and no World, plus `interview`. N holds, because this is why a sitting cannot be solved. Gaps: the investigation acts share one row writing `[]` (PR-054), and six of the study's fifteen steps are cleared by no verb (PR-056). The dyadic/public split (CL-043, CL-063) is already the `argue`/`speak` split.
- **Plato:** the corpus holds one paragraph (CL-009), one *Phaedrus* contrast (CL-083) and reading-list titles (CL-088); canon's Plato is Neoplatonic metaphysics (CL-108). Nothing mechanical comes from Plato, and that is right: the *Phaedrus*'s "know the kinds of soul" is the read-of-the-room stat AX-2 refuses. **Evidence:** RATIFIED axiom. The Guiguzi material is TIER-FLOOR T2 and may not be cited as grounded.

### C10 · The kernel's judge armature, appraise bands, style cards and in-bout trackers — **MISFIT**
Entries: CD-088, CD-089, CD-090, CD-094, OP-005, OP-006, OP-007, OP-098, OP-055, OP-088, OP-093, CL-095, HP-084.
- The four-axis armature is a second conviction store beside `Person.pursuits` (NERS §3, disqualifier 1), and only pursuits can be moved by argument. Face, Reserve, Room and the Persuasion Track are contest-local meters the design refuses (PR-105). The kernel returns winners, takes no rng and reads a faculty (opened: `roll.py:16-37`), and Layer 1 C.5 refuses a winner. OP-088 shows its stacks decided contests at setup. The one idea worth keeping, that a partial reveal keeps the choice a bet (OP-098), is already carried by AX-2. **Evidence:** coded but not adopted; retirement RULED (CD-052, PR-108).

### C11 · Social proof and consistency: other people's commitments as an input (Cialdini, ELM, attribution) — **FITS-IF-ADAPTED**
Entries: CL-051, CL-049, CL-065, CL-071, CD-036; across themes CL-056, OP-030 (D).
Adaptation: keep only social proof and consistency. A voter's `commit` reads the witnessed commits of those he regards (claims he holds), and a repudiation costs reception (F1). Drop ELM's decaying peripheral change and the attribution flag.
- `score_terms` reads no other member's commit: no snowball, no first defector (proposal §8; CL-056); a council is independent draws. Social proof is the cheapest person-input cascade with no player present (strong R-world). ELM decay contradicts AX-3 (*"nothing moves either on a clock"*); the attribution flag is a store with no producer. **Evidence:** RESEARCH only — rests on tier 3.

### C12 · Composition and delivery craft (the five canons, the six parts, progymnasmata, *ars dictaminis*, *balagha*, the story model, *procatalepsis*, inoculation, logographers, the sophists) — **MISFIT**
Entries: CL-003, CL-010, CL-012, CL-016, CL-017, CL-029, CL-048, CL-052, CL-053, CL-058, CL-085, CL-087, HP-094.
- Decorative. Each acts on an utterance's arrangement or wording, and the engine has no utterance content: a Proposition is subject, predicate and value, and moves are menu choices (CL-061). The story model needs a judge of a narrative's coherence that no person can be. Klei's finding (CL-058) warns against rebuilding them as resource sinks. Rank-indexed salutation survives only as "standing settled before speech" (E5).

### C13 · Lies and concealment — **FITS**
Entries: CD-065, PR-029, OP-103, CL-086, CL-061.
- A lie is a `tell` of a false value (CR-27, planned). Discovery is any ordinary investigation; silence is not an act. There is no deception subsystem and no truth meter. N holds laterally: without lies a hostile witness and an honest but mistaken one could not be indistinguishable (PR-084), and the ethos channel would have nothing to punish. **No-player story:** a lie found seasons later is a deed every hearer re-reads. NOTCODED. **Persons:** whether to conceal turns on whether the party is needed again (CL-086), which is horizon (M3). **Evidence:** RATIFIED plan position.

### E1 · Offers as dated utterances; the treaty is the Proposition both parties commit to (`covenant`) — **FITS-IF-ADAPTED**
Entries: CD-037, HP-077, OP-046, PR-069, PR-033, CD-105, OP-068, OP-102, CD-077, OP-040, GV-095, OP-059, OP-044, OP-039.
Adaptation: acceptance weighs the offer's content (C2's `commit` reader), and delivery is bound to the terms (a `give` that can form).
- Opened `verb_table.yaml:292-317`. `covenant` is seat-only and mints a dispensation held by its maker. The counterparty learns the terms only when handed it by `give`, which computed play cannot form (H-229), and its readers are deferred. N holds in every direction: immutable dated offers leave a record a third party can produce, the best no-GM negotiation shape in the corpus, and it needs no new store. Today a 40-grain and a 25-grain offer score alike. **No-player story:** a rejected offer, still on record, embarrasses its author when a rival produces it. NOTCODED end to end. **Evidence:** CODED (`covenant`) plus INTENT.

### E2 · Reservation value and BATNA — **FITS-IF-ADAPTED**
Entries: CL-102, HP-071, CL-062, OP-029, OP-091, OP-028.
Adaptation: no reservation field. A person accepts when committing to the offer outscores his best other candidate act.
- The chooser already ranks every candidate, and the outside option is his opening set, so a stored reservation value is a false N-line (NERS §3, disqualifier 1). CL-062's *"alternatives are built off-table; the table only prices them"* is literally how the engine works once `commit` reads content: improve your alternatives elsewhere and every acceptance threshold moves. Red lines are a value no offer's alignment clears, not an announced list. **Evidence:** RESEARCH T1.

### E3 · Anchoring, logrolling and scaled compromise — **HELD-FOR-REASON**
Entries: CL-054, CL-055, HP-072, CD-051, OP-070.
- Two prerequisites are missing: content-weighing of offers (C2, E1), and per-matter outcomes within a bundle (CD-051 is ruled and unbuilt; the obstacle bounds one matter, `roll.py:79-82`). Anchoring as a bias would be a scripted adjustment with no person input; its informational half, that the first offer leaks preference, is already carried by the dated utterance. Scaled compromise's carrier (`Tenure.degree`) has no producer. **Evidence:** RESEARCH T0/T1.

### E4 · Binding: cheap talk by default, costly instruments as the exception — **FITS-IF-ADAPTED**
Entries: OP-069, HP-073, HP-068, HP-040, GV-072, HP-087, HP-090, HP-074.
Adaptation: a binding instrument is an existing tenure (a person detained, an `oblige`, a marriage commit) whose breach is a witnessed release priced by reception. No pledge store, no Stability cost, no casus-belli grant.
- The cheap-talk default is already how `commit` and `release` behave. N holds: a world where accords bind automatically has no diplomacy. **No-player story:** the hostage whose captor breaks faith. **Evidence:** PROPOSED plus GAME and RESEARCH.

### E5 · Envoys, interposition, audience and ceremony — **HELD-FOR-REASON**
Entries: PR-034, PR-043, CL-026, CL-098, HP-076, CL-015, CL-041, GV-096.
- The prerequisites are missing: a computed `give` (H-229), and a dispatch that can carry an instrument. `interposed` and `venue_min_rank` have no reader (HP-045). The idea fits: Kautilya's three envoy latitudes are how much of oneself one brings, PR-034 inverts the game with one key, and a pair of envoys carries a real collusion risk. But nothing can carry a covenant today.

### E6 · Escalation across instruments (Kautilya's four *upaya* and six measures, changing arena, negotiation → debate → appeal, collective boycott) — **ALREADY-HELD**
Entries: CL-027, CL-028, CL-060, OP-018, HP-047, HP-012, GV-018 (Grand Debate).
- Held as the verb set. Conciliation is `argue` and `covenant`; gift is `give`; division is `tell` and `conspire`; force is `fight` and `march`; war and alliance are Propositions (OP-059). Escalation is a person choosing a different act next season, with no mode switch and no zoom-in, so it passes "pauses correctly" by construction. It fits on one condition: escalation must not be free, which is DitV's flaw (CL-060). Its price is C8's witnessed cost.

### E7 · Stored diplomatic rights and the archived faction treaty machinery (casus-belli tokens, demand-redress windows, a three-phase treaty roll, faction bonuses, quota compacts) — **MISFIT**
Entries: GV-017, GV-018, GV-019, HP-048, HP-083, GV-105.
- Factions act, rolling Influence and Mandate. Faction-specific bonuses (the Church's Sacred Compact, the Guilds' ×1.5) are scripting drift. A casus-belli token is a stored world condition the tree has refused (GV-095). The surviving idea, a formal demand followed by defiance, is already two acts (`utter` an OUGHT, then `release`).

### F1 · A faction is a view over persons' commits; allegiance follows opinion; defecting is free to do and costly to be seen doing — **FITS-IF-ADAPTED**
Entries: GV-032, GV-082, GV-083, OP-057, CD-044, GV-090, GV-100, OP-048, OP-060.
Adaptation: `opinion_of` gains a decision consumer (joining and leaving, and the party term in `commit`).
- Opened: `opinion_of` is consumed only as the `< 0` gate on grudge referents (`world_q.py:2471-2473`). CD-044's "feeds decisions" holds only in that narrow sense. The ratified "factions hold people" (GV-032) is persons-as-inputs exactly. `conspire` composes on a commit to an OUGHT and a contested invitation, with no new store. **No-player story:** defections that propagate because a superior heard of them. **Evidence:** RATIFIED plus CODED plus PROPOSED.

### F2 · Faction-actor voting (Mandate-weighted votes, Church Influence weight, fixed heuristic votes, card hands, ethic obstacle modifiers) — **MISFIT**
Entries: CD-091, CD-092, GV-013, GV-014, GV-016, GV-081, OP-084, OP-081.
- A faction never acts. "Guilds always vote no on Blockade" is scripting drift, and Church Influence counted as votes is a stored aggregate. OP-084's own critique applies: the old motion had a vote but no debate and left no causal trace. The kernel files run only in their own tests.

### F3 · Patronage, bribery and office as lever, through regard rather than transaction — **FITS-IF-ADAPTED**
Entries: CD-078, PR-106, HP-017, HP-037, HP-043, HP-100, CL-107, GV-038, CD-074, HP-088, HP-042, HP-018; across themes GV-070 (D).
Adaptation: a bribe is a `give` whose deed raises the recipient's regard for the giver. That regard reaches his vote only through a sponsor-standing term in `commit`. No bribe verb, and no debt to call in: the second-person lever stays refused (PR-106, RULED).
- `revoke` with a permanent ban is CODED (CD-074), so the patron's stick exists. Medici "robust action" (HP-100) emerges from regard held across factions, and the proposed Cross-Faction Reach stat is a false N-line. The *barnaboti* debasement is the same mechanism at scale. Today *"a give never reaches a commit, so votes cannot be bought"* (CD-078). **No-player story:** votes that follow money with no sale ever recorded. **Evidence:** CODED (`revoke`), RULED (the refusal), HISTORICAL (the rest).

### M1 · The character model: wants as commits to an OUGHT, fears as negated wants, conviction, stance, ledger — **ALREADY-HELD** (the carriers; the readers are missing)
Entries: CD-050, PR-071, PR-082, PR-083, PR-105, PR-107, PR-059, CL-104, OP-079, PR-072.
- Opened `carriers.py:656-708`: `Person` carries `capability`, `stance`, `pursuits` (the 15-pursuit roster, i.e. what he holds right), `ledger`, `scar`, `conviction` and `thread_sensitivity`. **Stale entries:** PR-059 and PR-071 treat the retired `convictions` field as ethical weights over closed axes. `conviction` is now religious-affiliation intensity, 0-5 (ED-IN-0251); the ethical weights are `pursuits`.
- What is missing is the readers. A want gives a topic but not a direction (PR-082: holding Vellenmark and burning it form identical candidates). Pressure is built but never fires in realm play (H-222). 35% of audited characters have no act that reaches their goal (OP-079). **For persuasion, every input a vote needs exists — what a person values, whom he regards, what he is committed to — and nothing reads them for a motion.**

### M2 · Persuasive capacity: a pool from capability, latitude in the pool only, capacities as requirements on steps — **FITS-IF-ADAPTED**
Entries: PR-026, PR-060, PR-061, PR-062, PR-012, CL-090, PR-064, CD-030, CD-031, PR-099, PR-063, PR-022.
Adaptation: an `argue` capability row and authored capability values. The design is sound (one stochastic draw; latitude in the pool, floored); the tree supplies nothing to it.
- Today every arguer rolls 2D against 2 (verified, `rosters.yaml:1223-1233`), so persuasive skill varies by seed, not by person. CL-090 (person effects are large but trait-opaque) argues against a nine-stat block, which the design already refuses.

### M3 · Risk appetite and horizon as inputs to persuasion and bargaining — **HELD-FOR-REASON**
Entries: none in theme M. Adjacent: CL-020 (Han Fei's fear and desire registers), CL-086 (is the party needed again), PR-086 (anger works only against one who cannot afford impasse), OP-028 (a patience gate); across themes NL-032 and NL-033 (K).
- **The theme is thin, and that is the finding.** Jordan ruled that persons differ in risk and in short, medium and long horizon (NL-032, ED-IN-0304). The chooser has neither term (opened `choose.py:130-151`; NL-033) and `Person` has no carrier for either. Every bargaining mechanism in E leans on these two inputs: a BATNA is a risk judgment, anchoring and impasse are patience, cheap talk against costly binding is horizon, and Han Fei's fear register is risk. The prerequisite is CR-17 (believed odds weighting the alignment term). Until then E2, E3 and E4 can be expressed, but every person bargains with the same nerve and the same foresight.

---

## 2. Ranking by fit for purpose

1. **C1** — the filter that makes every verdict here decidable.
2. **C2** — the only carrier by which argument can change a vote.
3. **F3** — votes follow favours with no new verb and no player.
4. **C8** — every failed speech becomes churn.
5. **E1** — no-GM negotiation with a citable record.
6. **C11** — votes cascade; cheapest no-player drama.
7. **E2** — retires a store the engine already has.
8. **F1** — allegiance from inputs, not flags.
9. **C3** — held, inert until what it modulates writes.
10. **C13** — the truth track's adversary.
11. **M1** — carriers held, unread.
12. **C6** — names a split the engine already has.
13. **E6** — held.
14. **E4**. 15. **M2** — sound design, empty data. 16. **C9**. 17. **C4** — forensic only. 18. **C5** — forensic, unread.
19. **M3** — blocked, yet most consequential for E. 20. **E3**. 21. **E5** — blocked on `give`.
22. **C12** — decorative. 23. **C7** — an oracle and a second ending. 24. **C10** — a second conviction store. 25. **E7**, 26. **F2** — factions act.

## 3. The clusters that most affect the others

- **C2 (logos content) and the `commit` reader it implies.** Theme D's tally (CD-049, OP-101: the count of live commits) counts nothing meaningful until a commit reads content. E1, E2, E3 and F3 all wait on the same single reader. The collision: if the reader is built as a per-motion lookup it becomes scripting drift. It must stay `pursuit_lean` over the predicate verb.
- **C1 (AX-3).** It decides that forensic matters run through J (claims, record) and OUGHT matters through pursuits. That cuts C4, C5 and the stasis half of part 1's B down to tribunals, and it is why the proposal's parliament has no issue ladder.
- **C8 (witnessed cost).** It leans on J (reputation as ledgers) and K (churn). It collides with I if a failure cost turns into a walkout or a feud with no person behind it. It is also E6's price.
- **M3 (risk and horizon).** It leans on K's NL-032 and NL-033. It gates E2, E3 and E4 and D's abstention and first-defector dynamics (CL-056), and the PR-107 cornered-man break is a risk response with no risk input.
- **F3 (patronage).** It collides with part 1's GV-070 (a vote as the sign of regard for the proposer minus regard for the holder), which is the same ethos channel written as a faction tally. F3 is the person form of it. It also leans on H (transfers by `give`) and G (`oblige`).

## 4. Verification: what I opened, and whether the entry held

1. `person_q.py:638-658`, `effects_information.py:555-581` (CD-028, CD-101): **held**; Proposition never read.
2. `choose.py:54-151, 217-238` (CD-101, NL-033): **held**; three terms, no risk or horizon.
3. `arrangements.py` plus a grep for `SPEECH_KINDS` across `engine/` (CD-011, CL-077, PR-094): **held.** Only the loader and tests read it.
4. `verb_table.yaml:292-317` (CD-037, OP-046, CD-105): **held.** `covenant` is seat-only and one-shot, held only by its maker, its readers deferred and its delivery by `give`.
5. `world_q.py:2388, 2471-2473` (CD-044): **narrowed.** `opinion_of` is consumed only as a salience gate on grudge referents, not by any vote or join decision.
6. `carriers.py:656-708` (PR-059, PR-071): **stale.** `conviction` is religious-affiliation intensity, not a 13-axis ethical roster; the ethical weights are `pursuits`.
7. `roll.py:63-125` and `rosters.yaml:1223-1233` (CD-030, CD-031, PR-099): **held**, with an addition: `argue` has no capability row, and 1 of 430 persons carries any capability.
8. `01_AXIOMS.md:124-128` (CD-055): **held.** Fading is the one clock-driven motion, and it only removes.
