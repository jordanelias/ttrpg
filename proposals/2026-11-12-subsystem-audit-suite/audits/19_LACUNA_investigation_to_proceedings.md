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
