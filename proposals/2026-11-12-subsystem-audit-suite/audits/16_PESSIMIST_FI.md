# FI — pessimist audit: NERS, premise and emergent narrative, of fieldwork, investigation, epistemics, information and witness

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `engine/season/epistemic.py`, `engine/season/loop/effects_information.py`,
`engine/season/loop/witness.py`, `modules/fieldwork/`, the decision code that forms the information
verbs, the detective and noir precedent, the investigation-to-proceedings pipeline
(`audits/19_LACUNA_investigation_to_proceedings.md`), and the five premise sentences of knowing. The FI
audit (`08_FI_audit.md`), its addendum B, the FI proposals (`08_FI_01`..`08`), the LACUNA audit and its
four proposals, and the GAME pessimist audit (`16_PESSIMIST_GAME.md`) are cited, not redone. Everything
measured here is new work unless a lane is named. Runs: `PYTHONHASHSEED=0`; scripts and outputs in
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_FI/`.

## 0. Verdict

*(written last; see the end of this section once the runs are in. The section order below is the order
the work was done in, so that a partial file is still usable: §2.0 holds the ordinary-meaning
predictions, written before any FI note or code was opened.)*

## 2. Premise audit

### 2.0 The ordinary account (O), written before any FI note or code was read

Method: `skills/premise-check/SKILL.md` STEP 1 and STEP 2. Five premise sentences, as given in the
work order. Each is split into links; each link carries what a player who reads the words in their
dictionary sense, and who knows strategy and role-playing games, would expect. `[GENRE]` marks an
expectation the words do not themselves promise. These predictions were fixed at this point and are
not edited after the code was read; where a later section disagrees with one, the disagreement is the
finding.

**P1. "A person acts on what he has seen or been told, not on what is true."**

| # | link | O: what the words promise |
|---|---|---|
| P1.1 | there is a truth, and there is what a person holds, and they are two things | the world's state and a person's holdings are separately stored; a holding can differ from the state |
| P1.2 | he has *seen* | a person present where a thing happens comes to hold it; a person absent does not (E3: presence is a definite set) |
| P1.3 | he has *been told* | another person's act of telling gives him a holding that names its teller; without a telling, an absent person holds nothing of it |
| P1.4 | what he holds may be false | stale (the world moved on), lied, forged or misheard; the false holding is stored like a true one and he cannot tell them apart from inside |
| P1.5 | he *acts on* it | his choice of act reads his holdings and never the world's state; two persons in one world with different holdings choose differently; give him a false holding and he acts on the falsehood (E4: direction) |
| P1.6 | *not on what is true* | change the truth without anyone seeing or telling him and his behaviour does not change (the counterfactual control); nothing in the chooser or the eligibility gate leaks the truth to him |
| P1.7 | correction | when the truth does reach him (he sees, or is told by one he believes) the holding changes and so does the act; the record says which holding he acted on (E10) |
| P1.8 | bounds | a person who holds nothing about a matter does nothing about it; a hermit acts only on what he saw himself |

**P2. "A rumour spreads and distorts."**

| # | link | O |
|---|---|---|
| P2.1 | a rumour | a thing said about someone or something, with content, started by a person at a time |
| P2.2 | spreads | it passes person to person, each hop an act of one person telling another who is near him; over seasons the number of holders grows; it reaches persons who never met the originator (E3, E6) |
| P2.3 | by contact | it travels along who meets whom; a person cut off does not get it; a market town gets it sooner than a hermitage |
| P2.4 | distorts | what the n-th hearer holds is not what the first said: the content drifts, the certainty drops, the origin is lost; distortion grows with hops (E4: ordered) |
| P2.5 | acted on | a hearer may act on the distorted version (P1.5) |
| P2.6 | ends | it can be denied, corrected or die out; a rumour nobody repeats stops (E7) |
| P2.7 | zero | no rumour started, nobody holds it; a true report and a false one spread alike (the hearer cannot tell) |

**P3. "A forged letter is believed until someone who knows better sees it."**

| # | link | O |
|---|---|---|
| P3.1 | forged | a person makes a letter that purports an author who did not write it; the making is an act with skill in it, which could go well or badly, and it is itself a thing someone might witness |
| P3.2 | a letter | a thing that is held, given and shown; reading it requires having it or being shown it |
| P3.3 | is believed | a reader who does not know better takes it as the purported author's and holds its content as if that author had said it; he acts on it (P1.5) |
| P3.4 | someone who knows better | a definite set: the purported author; one who knows that hand or seal; one who saw the forging; one who holds a fact the letter contradicts (E3) |
| P3.5 | sees it | detection requires seeing the letter, not hearing of it; the better the forgery and the less the viewer knows, the less likely (a draw, by the standing rule; ordered: E4) |
| P3.6 | until | from then, that viewer disbelieves; the forgery is exposed to those he tells; what was done on the strength of it is not silently undone (E7), and the forger may be named if the letter can be traced to him |
| P3.7 | controls | a genuine letter shown to the same expert is not called forged (or rarely); a forgery shown only to the ignorant stays believed indefinitely |

**P4. "A detective who looks finds something or nothing."**

| # | link | O |
|---|---|---|
| P4.1 | a detective | a person with a reason to look: an office, a grievance, a commission, curiosity; the game forms the act for such a person (FORMS) |
| P4.2 | who looks | at a definite place, person, thing or record; looking takes time and may be noticed by its subject (E8, [GENRE]) |
| P4.3 | finds something | a specific finding about what is actually there: who, what, where; true to the world (it is a trace of a real thing), held by him with himself as its source |
| P4.4 | or nothing | he may find nothing because nothing is there, or because he missed it; he cannot tell which; "nothing" is a result he holds and can report |
| P4.5 | which, depends | on what is there and on his skill: a draw; a better detective finds more often; where nothing is there to find, nobody finds anything (E4: zero; a find where nothing exists is a defect) |
| P4.6 | the finding is usable | he can tell it, cite it before a body, and it can point to the next place to look (a lead) |
| P4.7 | looking again | a second look at the same thing is not a free reroll for certainty, nor is it futile by rule ([GENRE]) |

**P5. "A crime leaves traces."**

| # | link | O |
|---|---|---|
| P5.1 | a crime | an act with an author, a victim or object, a place and a time: a killing, a theft, a forgery, a sabotage, a concealment |
| P5.2 | leaves | the act itself produces the traces; nobody has to author them afterwards |
| P5.3 | traces | of several kinds: those who saw; the changed thing (a body, a gap in the store, a burnt mill); a document; what the culprit now holds |
| P5.4 | of that crime | a trace is specific: it connects to the act, and with varying strength to its author |
| P5.5 | for a time | traces fade (witnesses die or forget, a site is repaired); the culprit can remove or hide some, at a cost or a risk, and hiding is itself an act that can leave a trace (E6, E11) |
| P5.6 | found by looking in the right place | a looker at the scene, or questioning one who saw, can come to hold it; a looker elsewhere cannot (P4) |
| P5.7 | leading somewhere | traces can add up to naming the author before a body that can act on it (the pipeline of `19_LACUNA`) |
| P5.8 | zero and planting | no crime, no trace; a trace of a crime that did not happen exists only if someone planted it (framing), which is itself a crime with traces |

