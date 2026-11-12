# 19 — LACUNA: from investigation to proceedings, as one pipeline

## Status: REFERENCE (a precedent-and-design lane; resolves nothing at runtime; its edits are proposals `proposals/19_LACUNA_*.md`)

## Read at: 61fee8d (working tree)

Direction (Jordan, 2026-11-12): *"consider how LACUNA handles investigations/solving cases and how that
intersects with fieldwork and proceedings."* Bound by `AUDIT_BRIEF.md` (the detective and noir precedent;
the standing rule "we do not do deterministic"; Authority granted; the playable-standalone requirement) and
`CLAUDE.md`.

**Correction to the request's citation.** The request names Lacuna as "Datajack, 2022". The tree and the
sources read say otherwise: *Lacuna – A Sci-Fi Noir Adventure* is by **DigiTales Interactive**, published by
**Assemble Entertainment**, PC **2021-05-20**, consoles December 2021 (`research/game_precedent_suite/tutorials/T19_tactics_narrative.md:229`,
V3 there from the Steam API; corroborated this session by search snippets [S]). *DataJack* is an unrelated
isometric stealth game (Epic Banana Games) [S, search snippets only]. Everything below is about the DigiTales game.

---

## 0. Verdict

**Valoria already holds most of the carriers a Lacuna-style case needs, and lacks the one act that makes
Lacuna a detective game: a conclusion the investigator commits to, bound to its support, that the world
answers later.** Lacuna's whole design turns on its Case Sheet: a narrow, single-shot, unverified
commitment (*"many channels out, few channels back in"*, Colbus) whose correctness is never announced and
whose consequences cascade into later cases. Valoria has the wide channels (WITNESS deposits, the six
inquiry rows, the told channel, `record`'s teller pairing, the case file, the docket, `determine`'s graded
draw); `reconstruct` writes nothing (`engine/season/verb_table.yaml`, `reconstruct.writes: []`), so the
narrow channel back in does not exist. The second gap is that the two halves are not yet one pipeline: the
FI lane's evidence interface and the SC lane's hearing disagree on whether entering evidence is a draw, and
neither carries a conclusion from the field into the room. Lacuna's resolution is authored (a hidden
answer key, one railroad per wrong answer); Valoria's must be a draw at every stage that could go either
way, and the world must do the answering that Lacuna's writers do. That is achievable on existing owners
with four proposals: admission rides the citing act's draw (the FI/SC conflict decided), the conclusion
becomes a committed assertion, the verdict becomes a five-result ladder with a reversal route, and the
case carries forward through ledgers, `record` and the chronicle. **The single largest obstacle** is
upstream of all of it: a killing's hand does not travel by testimony (`08_FI_06`), so until that lands a
homicide case can be concluded and tried only by an eyewitness.

---

## 1. Lacuna, sourced

Source tiers: **[P]** primary, page read this session (developer devlog); **[V]** page read this session
(review); **[T19]** read in the tree's own tutorial, which itself marks its tiers (V3 = a page it fetched);
**[S]** search snippet only; **[M]** memory, not relied on. Fan wikis: none reachable (T19 found no
Wikipedia article and no fan wiki; this session did not find one either). No repository, user or project
detail was sent to any external service; only game search terms.

Primary sources read:
- Julian Colbus (CEO, DigiTales), *"Detective Game Design: Puzzles vs. Story (Lacuna Devlog)"*,
  Game Developer, 2020-09-28 [P].
- Julian Colbus, *"Detective game design problems"*, DigiTales blog 2020-11-07, reprinted on Game World
  Observer 2020-11-08 [P]. (The two overlap; the second is the fuller argument.)
- *Lacuna review*, jumpdashroll.com [V].
- T19 §LA (`T19_tactics_narrative.md:228-298`), built on jumpdashroll, a-to-jconnections and a gamepretty
  achievement guide [T19, V3 there].

### 1.1 How a case is opened and structured

| fact | tier |
|---|---|
| The player is always Neil Conrad, an agent of the CDI; no build or class. | [T19 V3 store] |
| A case is issued as a **Case Sheet** sent to the phone; "cases can be solved at any time after the Case Sheet is issued, so the player cannot know when exactly they possess enough information". | [P GWO] |
| Cases nest: "each act has an overarching case"; a correctly solved small case "may produce a piece of evidence relevant to the act's overarching case"; some cases span several levels and later ones need testimony and news from earlier levels. | [P GD; P GWO] |
| Structure per level: gather, conclude, submit; "a well-designed puzzle provides all the information, then moves the entire solution process solely into the player's head". | [P GWO] |
| A level ends when the Sheet is submitted: submission "ends the level and starts the next one". | [P GD] |

### 1.2 How evidence and testimony are gathered

| fact | tier |
|---|---|
| "Many channels out, few channels back in": clues arrive through dialogue, objects, environments, the news and e-mails with attachments; early cases use only investigable clues and witness testimony. | [P GWO] |
| An investigation menu highlights interactables (searching is "not a particularly interesting type of challenge"); an optional Highlight Mode outlines objects and people with new information and shows when none remain. | [P GD] |
| **Redundant clues**: an important clue can be reached two ways. | [P GD; P GWO] |
| Clues are padded with "fluff, world-building, or even red herrings". | [P GWO] |
| **Dialogue is single-play**: "each dialog can only be played a single time"; dialogues branch and do not loop back to a hub; some open only after the player finds something (a witness gives a key after a cupboard is examined). | [P GD] |
| Replies are timed (a few seconds). The devlogs do not mention timers; a review caption does ("limited time to make decisions"). | [V caption; T19 V3] |
| Clues can be **lost for good** by a wrong dialogue choice or search order. | [T19 V3 a-to-jconnections] |
| Everything learned is logged automatically on the phone (clues, conversations, news, e-mail). | [T19 V3; V] |
| Tone toward witnesses (agreeable or aggressive) is tracked across the run as a counter with achievements; whether it changes the plot is not established. | [T19 V3 gamepretty; effect `?`] |

### 1.3 How the player assembles a theory

| fact | tier |
|---|---|
| The Sheet is a **cloze text** ("The shot was fired from ____"), answered from drop-down options. | [P GD; S reviews] |
| "The Case Sheet does not ask how they arrived at the conclusion": the answer only, never the reasoning. | [P GD] |
| The answer space is widened to defeat guessing: "256 (4x4x4x4) or even more possible answers"; the first case has four options, accepted as guessable because early. | [P GD; P GWO] |
| There is **no connecting board**: the phone log holds the clues; the reasoning is in the player's head. | [P GWO "into the player's head"; absence of a board in every source read, so an absence, not proven] |

### 1.4 How the player commits, and why a wrong conclusion costs

| fact | tier |
|---|---|
| Submission is **single-shot and irreversible**: "no takebacks"; auto-save only, overwriting the slot after each level; three slots; on PC since 2026 a chapter select. | [P GD; P GWO; T19 V3 Steam news] |
| The game does **not** block a wrong submission (blocking "allows brute-forcing"), has no Game Over ("break the immersion"), and builds no dead-end levels (cost, pacing). | [P GWO] |
| The player is **not told** whether the answer was right ("isn't told (right away)"). | [P GD] |
| A wrong answer is a **soft redirect**: in the sniper case the player boards a train, an anonymous tip sends him to the right building; the squad later finds the wrong building a dead end; a colleague (Gary) comments on the mistake next level. | [P GD; P GWO] |
| The game gives no "X will remember this" notice and does not disclose which decisions matter. | [P GD] |

### 1.5 How consequences run forward

| fact | tier |
|---|---|
| **Cascade**: "every incorrectly solved case makes it more likely (or even inevitable) that the player will fail the bigger ongoing case"; failing Act One's case can make information unobtainable in Act Two and close one of the two best endings. | [P GWO] |
| The developer names the cost: the player may find this unfair or not see why a later puzzle is unsolvable. | [P GWO] |
| News articles at kiosks and later conversations refer back to choices. | [V; T19 V3] |
| Arrests, letting a suspect go, and lying are stored consequences; the epilogue reads standing with the CDI, standing with one character (Zora), and the data decision: 2 x 2 x 2 = 8 endings. | [T19 V3 gamepretty; S for "8"] |

### 1.6 Authored versus systemic, and what Lacuna does not do

- **Authored:** the truth of every case, the answer key, every consequence, every redirect, the eight
  epilogues. The "world answers later" is writers' branching. **Systemic:** the log, the save, a tone
  counter, the bookkeeping of which Sheets were right [P; T19].
- **Lacuna does not:** let the player gather evidence by a draw (examining is certain once highlighted);
  ask for reasoning or support with the answer; show a board of connections; hold a court, a hearing,
  a cross-examination or a sentence (T19: *"arrests and the choice to hand over or leak; no courts or
  sentencing system found"*); let any non-player investigate, accuse or be tried; let a wrong conclusion
  stand — the railroad sends the player to the authored truth; let a wrong answer be *partly* right in a
  graded way (a field is right or wrong; the Sheet's fields are graded per field only in the story's
  branching) [P; T19; absences are mine].

### 1.7 The tree's claims about Lacuna, re-checked

| tree claim | where | verdict |
|---|---|---|
| "consequence-tested submission: accepted whether or not right, the world answers later" | VCD:789; REPO_MENTIONS §3 | **CONFIRMED** by the developer [P]. Refinement: the world answers in two ways the tree has not recorded, a soft redirect toward the truth and a cascade into the parent case. |
| `petition`/`determine` CARRY "submission regardless of correctness" | VCD:789 | **CONTRADICTED**, as `D_T06.md:57` already says: they accept a judgment, but nothing commits a *conclusion* bound to support. |
| "structured hypothesis slots (Sheets)" ≈ a claim's `(subject, predicate, value)` | VCD:783 | **HOLDS in shape**: a Sheet field is a cell; a Sheet is several cells committed together. |
| "Lacuna-style spatial attention", "temporal drift" | `.designs/systems/fieldwork/reference/investigation_systems_v30.md:209` | **NOT SUPPORTED** (T19:298; `D_T06.md:60`; nothing in the devlogs). The design document's Lacuna label is a misattribution; the nearest real thing is the dialogue timer. |
| "approach choice, calm or aggressive" | VCD:776 | **PARTLY**: tracked as a counter; its effect on play is not established. |
| "irreversibility" | VCD:791 | **CONFIRMED** [P]: no takebacks is the studio's stated first principle. |

---

## 2. What transfers, and what does not

Steelman first (the case for Lacuna as a model), then the attack, then what survives.

**Steelman.** Lacuna solved the detective genre's central problem (a puzzle blocks the story) by making
the conclusion a single-shot commitment the story absorbs either way, and made that commitment matter by
letting wrong answers cascade. That is exactly Valoria's need: a no-GM engine cannot block on a puzzle, a
wrong conclusion must be playable, and the consequence must arrive later from the world.

**Attack.** (a) Lacuna's correctness is an answer key; Valoria has ruled no verifier (2026-08-18 Q5, kept by
`08_FI_05_B` §7 and `05_SC_evidence_and_rebuttal_B`). (b) Lacuna's redirect is authored railroading
toward the truth; Valoria has no author and must not script (CLAUDE.md §0, scripting drift). (c) Lacuna's
gathering is certain; Valoria's inquiries are graded draws (`graded_inquiries`, `rosters.yaml:1407`).
(d) Lacuna has no court. (e) Lacuna has one investigator; Valoria's one-chooser rule makes every person a
possible investigator, accused and judge.

**What survives (the transferable structure):**

| Lacuna element | survives? | Valoria form |
|---|---|---|
| Many channels out, few back in | **yes, as structure** | Wide: WITNESS's deposits, six inquiry rows, the told channel, the found deposit. Narrow: one committed conclusion per case question (§3, stage 4). |
| The Sheet: a cloze of cells, answer without reasoning | **yes, changed** | A conclusion is an uttered `Proposition` (a cell) the investigator `commit`s to. Valoria **adds** what Lacuna omits: the support is bound to it (`cites`), because in Valoria the support is what a bench will weigh. |
| Single-shot, irreversible submission | **yes** | `Proposition` is immutable (`loop/effects_information.py::_eff_utter` docstring, §14); a `commit` can be `release`d, but the release is itself an Event others witness (`commitment.ended`), so a retraction is a deed with a cost, not an undo. |
| Not told whether right | **yes, already true** | Nothing person-side reads the Event log as truth; `record` pairs held items only (`decision/options.py:1727-1767`). |
| Wide answer space against guessing | **yes, already true** | The value space is the persons the ledger names (`person_q.deed_doers`, `:302`), which can be empty, one, several, or wrong. |
| Wrong answer cascades into the parent case | **yes, systemic** | A wrongly disposed accused leaves the true doer free to act again; the convicted man's kin and he hold the determination as a deed; the parent matter (a faction's grievance, a strand) reads the outcome. No authored cascade: the free doer's next deed is the cascade. |
| Soft redirect toward truth | **no (null, kept)** | Valoria lets a wrong conclusion stand. What can correct it is another person's firsthand contradiction reaching the concluder (FI_03 §4, the caught-liar question) — a draw-driven, not authored, redirect, and it may never come. |
| Colleague comments on the mistake | **yes** | A colleague who holds a contradicting firsthand cell and `tell`s it; `record` re-grades the concluder in that hearer (§4.4). |
| Single-play dialogue, clues lost by order | **partly** | Order already matters (`engine/season/epistemic.py:379` `[as cited by D_T06; not opened]`, witnessing a forging closes its trail; `D_T06.md:55`). Single-play becomes a cost, not a lock: questioning someone tells him he is being asked about (proposal 4). |
| Tone (agreeable / aggressive) | **yes, as odds** | An `approach` payload key on `interview` and `interrogate` that moves the obstacle and the subject's `regard` (VCD row 9; proposal 4). |
| Standing with the institution at the end | **yes, systemic** | A bench's or investigator's later `reception` and `record` move by what the room and the realm come to hold. |
| Authored truth and endings | **no** | The truth is the Event log; no ending table (ERRATA G17, `D_T06.md:61`). |
| Certain gathering | **no** | Every inquiry is a graded draw. |

**Null, honestly marked.** No shipped detective game read here (Lacuna, and the T06/T19 set: Obra Dinn,
Shadows of Doubt, L.A. Noire, Ace Attorney, Pentiment) lets a non-player investigate, conclude wrongly,
accuse and be judged by the same surface the player uses, and none resolves a verdict by a draw from the
case. Ace Attorney's court is authored and scored per present (T19:171-190); Pentiment's accusation has no
canonical culprit but is authored (R5:52, per THROUGHLINES P26). Valoria's pipeline below has no
precedent as a whole; its parts each have one.

---

## 3. The pipeline, one path from crime to chronicle

Six stages. Every person runs it through the same Candidates and the same fold; a player differs only in
who chooses (`harness/play_surface.py::dispatching_chooser`). Draws are named with their pool and obstacle
owners; "choice" means a chooser's decision (sampled for an NPC; the determinism sweep classes that as
drawn, `audits/18_DETERMINISM_SWEEP.md:8-9`); "eligibility" is the brief's carve-out; "bookkeeping" is
arithmetic by definition.

| # | stage | verbs (rows) | typed objects in / out | what is drawn | writes and who learns | state today |
|---|---|---|---|---|---|---|
| 1 | **open** — a crime, a claim or a petition becomes a case | in the field: none (the case is the goal `{deed_doers: …}`, `08_FI_07` §1); before a bench: `open_case` (seat with `remit:determine`, purview), `petition` + `carry` (anyone) | in: a held deed claim or a held petition; out: the goal (field), a case-file `Record` + `DocketItem` (proceedings) | nothing: opening is an eligibility-gated act (`open_case` has no contest; `petition` none) | `_eff_open_case` mints the case file and dockets the matter (`effects_information.py:367-446`); WITNESS tells those present | **built** (both rows run); the field case as a goal is `08_FI_07` §1 |
| 2 | **investigate** — evidence and testimony as typed objects held by persons | `examine`, `surveil`, `research`, `interview` (questioned person answers by his own `tell`/`lie`, CP-T06-05), `interrogate` (seat, detainee), `thread_read` | in: a Site / Rung / Record / Person; out: `Claim`s in the actor's ledger (firsthand, found, told), `Record`s on his `hold` | each inquiry is a graded draw (`graded_inquiries`); the answer to `interview` is the subject's own `tell`/`lie` draw; `interrogate` is a contest (`contests: a proposition`) | WITNESS deposits; `finding_terms` decides what of a covert trail a band shows; the subject learns he was questioned (proposal 4) | rows exist; products are `08_FI_03` §2 / `08_FI_07` §2; `examine` never forms (F-FI-12) |
| 3 | **theorise** — the board | none (a read) | in: the ledger; out: groups by cell, support over distinct origins, contradictions held, the suspects line | nothing (a rendering) | nothing | `08_FI_07` §3 (`play_surface.board`), harness only |
| 4 | **conclude** — commit to an assertion, support bound | `reconstruct` (product: an uttered `Proposition` HOLDS naming the doer), then `commit` to it | in: the goal's `deed_doers` value space, the held claims chosen as support; out: `Proposition` (immutable) + `hold` + `commit` edge; `Proposition.support` = the cited ids (proposal 2) | `reconstruct`'s graded draw sets what the conclusion can say (Failure: nothing; Partial: the deed without a hand; Success: the hand; Overwhelming: the hand and full confidence); **which** suspect, when the ledger names several, is the chooser's choice | `proposition.uttered`, `commitment.made` witnessed by those present; the conclusion is now a deed others can hold | `reconstruct.writes: []` today; `utter`/`commit` rows exist and run |
| 5 | **proceed** — the conclusion enters a hearing | `petition` (terms name the accused, from the held Proposition via `terms_sourced`) → `carry`, or `open_case`; `speak` with `cites` (party, accused, advocates); the answering `speak`; `determine` | in: the docketed matter, the case file, each side's held items; out: `filed`/`excluded` stages, `struck` stages, the disposal Tenure with its `degree` | **admission**: rides the citing `speak`'s own band (proposal 1); **answer**: the answering act's draw (`05_SC_evidence_and_rebuttal_B` rules 1-2); **verdict**: `determine`'s draw, obstacle moved by the standing items, the venue and the persons (`05_SC_obstacle_difficulty_and_modifiers_B`) | the case file's stages; every hearer holds the told copies (FI E-3); `matter.*` Events | `speak` writes `[]` at every band; `determine` runs (a draw at pool 2 vs ob 2: 0.74 / 0.19 / 0.07 / 0.00 Failure / Partial / Success / Overwhelming, as measured in `05_SC_acquittal.md`) |
| 6 | **carry forward** — reputation, grudges, precedent, record | none new: `record`, `reception`, `consequence_pursuits`, `deeds_judged`, the chronicle | in: the determination Event, the case file; out: claims of it in every witness; pursuit moves; a disposal edge | none at this stage: what follows is ordinary acts with their own draws (the freed doer's next deed; the convicted man's kin's `petition` or `challenge`; an appeal) | witnesses hold `matter.determined`/`matter.dismissed` as a deed; the case file persists, can be cited, forged, seized | partly built; the concluder is not yet paired by `record` (proposal 2); the chronicle cannot say what a case was about (`09_WR_B_chronicle_that_tells`) |

**The verdict ladder** (proposal 3), one draw, five results:

| result | how it arises | write | reversible by |
|---|---|---|---|
| **conviction** | `determine` at `Success` / `Overwhelming` | the disposal the arrangement names (`oblige` / `detain` / `ban`), `degree` = the band | appeal; `pardon` (detain, ban); `release` (oblige, by the obligee, C-1's ruled price) |
| **partial** | `determine` at `Partial` | the disposal at `degree: Partial` (the lesser sentence, which a degree reader scales) | as conviction |
| **acquittal** | `determine` at `Failure` | `matter.dismissed`, the docket cleared, a `dismissed` stage on the case file (SC-P6) | a new `open_case` on new evidence (the case file is reopenable) |
| **mistrial** | the sitting reaches no closing draw: a `bench` or `quorum` conjunct of `determine` refuses (eligibility), or every `for` item is struck origin-wide on an `Overwhelming` impeachment (`forgery_found`) before the close | a `voided` stage on the case file; the matter stays docketed | a new sitting (the standing court re-hears it) |
| **reversal** | an appeal: a petition whose `terms` name the disposal edge, carried to a bench at a higher rung, `determine` there at `Success`+ | closes the disposal (`Tenure.until`) and writes a `reversed` stage on the original case file | not reversible below the appellate rung |

---

## 4. The intersection, stage by stage: same, different, invented

### 4.1 Open

**Same as Lacuna:** a case is issued and may be closed at any time; the investigator cannot know when he
holds enough. **Different:** nobody issues it. In the field the case is a goal whose object is a
`deed_doers` question (`08_FI_07` §1; the form exists in `rosters.yaml: goal_object_kinds`); before a
bench it is a `DocketItem` with a case file. **Invented:** nothing. The decided rule (R-19-01, §6): a field
case and a docketed case are linked by the case file only when an `open_case` or `carry` docket it; a field
case needs no document.

### 4.2 Investigate

**Same:** many channels (place, paper, person, news-by-telling); redundant routes (three inquiry rows reach
one fact, `08_FI_07` steps 2-3); order can close a route. **Different:** each look is a draw; a `Failure`
teaches the reads but not the trail (`08_FI_07` §2(b)); the person questioned answers by his own act and
may lie. **Invented here (proposal 4):** questioning costs disclosure: the subject holds a `seen` claim that
he was questioned, by whom, about whom, so a guilty subject may flee, forge, or lie better, and an innocent
one tells others. This is the systemic counterpart of Lacuna's single-play dialogue (a lock in Lacuna, a
risk in Valoria), plus the tone choice as an `approach` key.

### 4.3 Theorise

**Same:** the reasoning is the player's; no machine grades it. **Different:** Valoria shows a board
(`08_FI_07` §3), because a non-player's reasoning must be legible afterwards (the brief's NPC charge (d)),
and because the board shows what clause 4 actually weighs. A connection is two claims on one subject, not a
stored link. **Invented:** nothing.

### 4.4 Conclude

**Same:** a narrow commitment; irreversible; not graded at submission; may be wrong. **Different:**
(a) the support is bound to the conclusion, because a bench will weigh it and a reader must see why
(Lacuna's cloze omits reasoning by design; Valoria's chronicle needs it); (b) the commitment is drawn twice
over: `reconstruct`'s band sets how much the conclusion can say, and the chooser picks among the suspects
the ledger names; (c) the world answers through `record`: a person who holds the concluder's Proposition
and later holds a firsthand cell that contradicts it re-grades the concluder exactly as he re-grades a teller.
**Invented (proposal 2):** `Proposition.support` (a tuple of claim and Record ids, cited at commit,
refused if unheld); `reconstruct`'s product; the concluder as a teller in `record` (CR-83's designated home).

### 4.5 Proceed

**Same as nothing in Lacuna** (no court). Ace Attorney's present-against-statement is the nearest (T19
§AA), and its shape — a held item set against a testimony and found inconsistent — is the SC lane's rule 2
(contradiction), with the decisive difference that the result is a draw, not a lock. **Different:** a
verdict is a draw with odds; the bench's members hear and keep the evidence (FI E-3). **Decided here
(proposal 1):** whether an offered item is entered on the record is a draw, read off the citing act's own
band. **Invented (proposal 3):** mistrial and reversal as named results.

### 4.6 Carry forward

**Same:** consequences arrive late, through what others say (Lacuna's news and Gary). **Different:** no
endings table; the cascade is the free doer's next deed, the convicted man's grudge, the bench's reputation,
the case file that can be cited, forged or burned. **Invented:** a case thread in the chronicle (proposal 3,
harness only): from the determination back through the case file's stages to the first deed claim, using
`09_WR_B_chronicle_that_tells`'s owners (`subject_of`, `anchor_of`).

---

## 5. The standing rule, applied to this pipeline

| point | could it go either way in the fiction? | decided |
|---|---|---|
| opening a case | no: an eligibility (the seat, the purview, a held petition) | bookkeeping + eligibility, no draw |
| an inquiry's yield | yes | graded draw (built) |
| a questioned person's answer | yes | his own `tell`/`lie` draw (CP-T06-05) |
| what a conclusion can say | yes | `reconstruct`'s graded draw |
| which suspect | yes, a judgment | the chooser's sampled choice; an NPC can pick the weaker-supported name |
| **whether an offered item is entered** | **yes: benches refuse exhibits** | **the citing `speak`'s band (proposal 1)**; this overturns the SC file's "filing is bookkeeping" |
| whether an item survives an answer | yes | the answering act's draw (SC `_B` rules 1-2, already reconciled) |
| the verdict | yes | `determine`'s draw; obstacle from the standing items, venue and persons |
| mistrial on a refused quorum | no: whether a sitting may decide at all | eligibility |
| an item's weight after corroboration | no: arithmetic over held items | bookkeeping (noisy-OR, ED-IN-0322) |
| whether a later contradiction re-grades the concluder | no: a reading over two held claims | bookkeeping (`record`); what anyone does about it is a later draw |
