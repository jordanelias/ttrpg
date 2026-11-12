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

### 2.1 P2 "A rumour spreads and distorts": does not hold; it breaks at the second teller (EXECUTES), and what distorts is only a number

**Verdict.** The premise holds for one hop and then breaks by construction, at EXECUTES depth, before
any question of whether the chooser forms the act. `08_FI_audit.md` F-FI-02 and H-272 measured the
absence in computed play (0 two-hop chains); this section shows it on a hand-driven chain, where every
teller is made to tell, so the absence is the mechanism's and not the chooser's.

**Run** (`p2_chain.py`; `probes.tiny_world`, shipped fixtures, seven added persons each in his own
hearth; teller walks to the next hearer by `move`, then `tell` through the real fold with the degree
forced, the tree's own `_tell` recipe; `said` is what `person_q.said_of` returns for the teller, as
`opening_set` would copy it):

| hop | what the teller says (`said_of`) | what the hearer then holds on the topic |
|---|---|---|
| 1 | `(S, stores:grain, 40)` | `(S, stores:grain, 40)` `told_by`, one hop; and his own `(S, news.told, True)` |
| 2 | **`(S, news.told, True)`**: "there was a telling about S" | only his own `(S, news.told, True)`: the told copy is the triple he already holds, so the exact-triple guard drops it |
| 3..6 | the same | the same |

Identical for a deed (`(p_king, person.died, True)`), at `Success` and at `Partial`. The second man in
any chain passes on the fact that he was told, and the third man receives nothing. **A rumour in this
engine has a maximum length of one telling.** The other `said_slant` arm (`valence`) gave the same
table for these persons, who carry no convictions (`p2_chain_valence.py`); a teller whose convictions
give the deed a nonzero valence was not tested `[UNVERIFIED]`, and `valence` does not ship.

**Control (PROXY, labelled).** `p2_proxy.py` forces each teller to pass on the content claim he was
told (what `08_FI_02`'s proposed slant would choose), to test the links downstream of the break. Twenty
world seeds, six hops, origin `(S, stores:grain, 40)`:

| arm | hop 1 | hop 2 | hop 3 | hop 4 | hop 5 | hop 6 |
|---|---|---|---|---|---|---|
| every telling `Success`: mean abs. error | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| every telling `Partial`: mean abs. error (fraction of 40) | 0.26 | 0.30 | 0.31 | 0.44 | 0.55 | 0.72 |
| every telling `Partial`: mean value held (true 40) | 39.2 | 41.1 | 41.8 | 45.2 | 48.0 | 49.2 |
| every telling `Partial`: min .. max | 22..58 | 12..70 | 10..72 | 13..86 | 8..120 | 10..122 |
| stored confidence, any arm | 100 | 100 | 100 | 100 | 100 | 100 |
| weight at read (`teller_weight`) | 0.5 | 0.25 | 0.125 | 0.062 | 0.031 | 0.016 |

Under the proxy the distortion link FOLLOWS for a number: error grows with hops (ordered, E4). Four
things do not make sense of the word "distorts", each observed in the same run:

1. **Only a number distorts.** `(p_king, person.died, True)` arrives verbatim at hop 6 through six
   `Partial` tellings. A deed, a name, a place, who did it: none can be garbled, swapped or inflated.
   "They say the King is dead" can never become "they say the King is dying" or "the Duke is dead".
   `loop/witness.py::_told_value` drifts an `int`/`float` and drops one addressee of a document's
   content; everything else is deposited "verbatim, honestly" (its own comment).
2. **A good telling is perfect.** At `Success` the copy is exact at any depth. Distortion is a
   property of one degree band, not of distance.
3. **The drift has an upward bias and two fixed points.** Mean 40 → 49 over six hops (the step is
   proportional and clamped above zero). `0` never drifts (*"the granary is empty"* is always passed
   on exactly) and no number can drift to `0` (a full granary can never be rumoured empty).
4. **Things that are not quantities drift as if they were.** Observation deposits include
   `(X, exists:Record, 1)` and `(X, exists:Person, 1)` (seen in `p4_detective.py`'s ledgers); the
   proxy chain garbles `exists:Person` `1` into `2`, then `1`, then `2`. `condition` (an ordinal)
   drifts by one each hop. `is_cell` and `_told_value` test only "is it a number".

**What is actually said in computed play** (`told_dump.py 0 2`: the shipped realm, seed 0, two
seasons, content hash `bacd687f…`, the same world as the first FI audit's two-season reading). The
whole of the realm's person-to-person traffic is twelve claims held with a teller on them:

| held by | claim | what was said | how it came to be false |
|---|---|---|---|
| 7 persons | `(p_npc_004, exists:Person, 2)` | `p_npc_040` told `(p_npc_004, exists:Person, 1)`, once to `p_npc_004` himself | a `Partial` telling drifted `1` to `2` |
| 1 | `(p_npc_089, exists:Person, 3)` | `p_npc_090` **lied** to `p_npc_089`: `(p_npc_089, exists:Person, 2)` | the lie moved `1` up a band; the `Partial` copy moved it again |
| 1 | `(p_npc_089, exists:Person, 1)` (the man lied to, about himself) | the same lie | the `Partial` copy drifted `2` back to `1` |
| 1 | `(set_s_003, stores:grain, 86)`, true value 74 | a cohort lied: 60 | lie, then drift |
| 1 | `(set_s_036, room:p_npc_013, False)`, true `True` | `p_npc_013` lied | the boolean negated |
| 1 | `(set_s_021, stores.changed, True)` | a true telling | — |

**The false beliefs the first FI audit counted as formed by telling (its §1a: "told 0 true / 7
false"; F-FI-04: "all 7 told cell claims at seed 0 are false") are seven people holding that one man
exists twice.** Of the seven tellings that landed in two seasons, three said that a person exists.
What the 70 tellings attempted in those two seasons chose to say, by `said_of`'s newest-claim rule
(and the liar's cell rule): `exists:Person` 36 times, `tell.refused` (*"my last telling was
refused"*) 9, `proposition.uttered` 3, `cover.assumed` 3, `record.created` 3, a bare sighting 3,
`room:<person>` 3, `train.refused` 2, `stores:grain` 2, `stores.changed` 2, and one each of
`issue.unauthorized`, `challenge.refused`, `yield.taken`, `term.matured`. An existence reading is the acquaintance marker (`known_person_operands`): a
hearer told it comes to know of the man, so the telling is an introduction and has a use. It is also
a number, so the lossy copy garbles it and the liar inflates it.

**Link table** (C = the run; N = the notes; scale: season loop; module scale n/a).

| # | O predicted | N says | C observed | verdict · cause |
|---|---|---|---|---|
| P2.1 a rumour | a thing said, with content, started by a person | a `Said` fixed at CHOOSE from `said_of`'s one pick | one claim, the teller's newest non-`seen` claim on the subject | FOLLOWS (EXECUTES) |
| P2.2 spreads | hop after hop | "the `tell` chain is the only transport" (`claim_subjects` comment); H-272: retelling passes on `news.told` | **one hop, then nothing** | **DEPARTS · BEHAVIOUR** (N = C: the notes know; O differs) |
| P2.3 by contact | along who meets whom | hearing by presence (H-323) | everyone co-located hears the first telling | FOLLOWS for hop 1; UNREACHED beyond |
| P2.4 distorts | content drifts with hops | lossy copy at `Partial` (r2 `02` §A.10) | PROXY only: numbers drift, deeds never, `Success` never | **DEPARTS · WORD and EDGE** (items 1–4) |
| P2.5 acted on | a hearer acts on it | Q2 raises a question on a landed claim | a `told_by` claim landing occasioned 31 of 821 acts at seed 0 (FI audit §1a) | FOLLOWS, thin |
| P2.6 ends | denied, corrected, dies | decay 5 a season; no denial verb | no act denies or corrects a rumour; a told claim keeps confidence 100 at every hop while firsthand claims decay | ASSERTED (denial); DEPARTS (a sixth-hand rumour is stored as certain) |
| P2.7 true and false alike | indistinguishable to the hearer | by construction | a lie's copy and a truth's copy have the same shape | FOLLOWS |

**Play-back.** *A steward tells a carter the granary holds forty measures. The carter walks to the
next village and tells the miller that the steward told him something about the granary. The miller
learns nothing. Nobody in the valley ever says what the steward said.*

**Requirement touched:** R-01 (propagation by speech), R-07. **Minimal fix at the owner:** the
exclusion in `said_of` (`08_FI_02`, and its narrow arm C-5 in addendum B) is necessary and, by the
proxy, not sufficient for the word "distorts": see `proposals/16_PESSIMIST_FI_A_what_a_rumour_can_garble.md`.

### 2.2 P4 "A detective who looks finds something or nothing": holds at EXECUTES for one look; the second look is where it breaks

**Run** (`p4_detective.py`; the tree's trail fixture shape; a sheet forged or surveyed (genuine) by a
stranger and handed to the investigator; `research` resolved 300 times per cell with distinct act ids,
RESOLVE only so no deposit changes the next draw; shipped fixtures, so `ceiling_per_pool` is on).

| sheet | pool | Failure | Partial | Success | Overwhelming | P(the hand is ever found), retrying until the first `Partial`-or-better |
|---|---|---|---|---|---|---|
| forged (quality 1, shipped) | 1 | 91.7% | 8.3% | 0.0% | 0.0% | 0.00 |
| forged | 2 (the default) | 91.0% | 7.7% | 1.3% | 0.0% | **0.15** |
| forged | 3 | 81.7% | 11.0% | 7.3% | 0.0% | 0.40 |
| forged | 4 | 70.3% | 14.0% | 14.3% | 1.3% | 0.53 |
| forged | 5 | 57.7% | 20.3% | 17.0% | 5.0% | 0.52 |
| forged | 7 | 39.3% | 19.3% | 29.7% | 11.7% | 0.68 |
| genuine (control) | 2 | 68.3% | 24.0% | 7.7% | 0.0% | n/a |
| genuine | 4 | 45.0% | 25.3% | 23.7% | 6.0% | n/a |
| genuine | 7 | 23.7% | 15.7% | 36.7% | 24.0% | n/a |

Monotone in the pool (E4 FOLLOWS), and the mirror reads correctly: quality 0 reproduces the genuine
row exactly (68.3 / 24.0 / 7.7 at pool 2). Three things depart.

1. **A better look is worse than a failed one (INVERTED at the second look).** A `Partial` lands the
   claim on the paper, withholds the hand, and closes that trail to the finder for good
   (`epistemic.holds_trail`; pinned by `test_a_partial_find_closes_the_same_trail_to_a_later_better_one`;
   H-314). A `Failure` leaves the trail open and costs a scene. So an investigator with the default
   pool who keeps looking learns whose hand it was in 15% of cases (measured; 1.3 / (1.3 + 7.7)) and is
   locked out in 85%; the best investigator the scale allows (pool 7) is locked out in a third. The
   first FI audit recorded the lockout; the rate is new, and it is the dominant outcome at every pool
   below 4. CP-T06-03 (scheduled) is the right edit; until it lands the premise's word "finds" means
   "may be forbidden from finding".
2. **Addendum B's correction C-3 is itself now false.** It records forgery quality as *"inert at the
   shipped fixtures … quality 0, 1 and 3 are identical in play"* and a quality-3 forgery as
   *refused*. Measured at HEAD: quality 0 → 1 moves `Failure` from 68.3% to 91.0% at pool 2; quality
   1 → 3 changes nothing at pool 2 (the per-pool ceiling binds) and moves `Failure` from 70.3% to 87.3%
   at pool 4; nothing is refused (300 of 300 resolve to `finding.made` or `finding.none`). The per-pool
   ceiling (CP-T01-06) landed after the register row C-3 quotes.
3. **"Nothing" is not a result he holds, and "something" is minted where nothing was found.** After
   one look the investigator's new claims are:

   | sheet | band | Event | new claims about the paper |
   |---|---|---|---|
   | genuine | Failure | `finding.none` | none |
   | genuine | Partial or Success | `finding.made` | `(paper, finding.made, True)`, `(paper, exists:Record, 1)` |
   | forged | Failure | `finding.none` | none |
   | forged | Partial | `finding.made` | the same two, plus `(paper, record.forged, True)` `inferred`, hand withheld |
   | forged | Success | `finding.made` | the same, plus `(forger, record.forged, True)` and the sighting naming him |

   A clean paper examined well and a forged paper examined badly both leave no claim that says
   anything about the paper's honesty. *"I examined it and it is sound"* cannot be held, told or
   cited; `finding.none` is deposited to nobody (`UNDEPOSITED_KINDS`), so *"I looked and found
   nothing"* cannot be held either; and `finding.made` is emitted for a genuine paper on which
   nothing was found (WORD; H-318 names the kind, this is the content half).

**Link table.**

| # | O | C | verdict · cause |
|---|---|---|---|
| P4.1 a detective (FORMS) | someone with a reason is offered the act | see §3 (computed play) | see §3 |
| P4.2 looks at a definite thing | place, person, thing, record | a Record (`research`), a Rung (`surveil`); `examine` forms on nothing (F-FI-12); no inquiry takes a person | DEPARTS · BEHAVIOUR (cited) |
| P4.3 finds something specific and true | who, what | at `Success`: the hand and the deed, true to the log | FOLLOWS (EXECUTES) |
| P4.4 or nothing, and holds that | a reportable null | nothing is held on `Failure`; a clean result is not a claim | DEPARTS · BEHAVIOUR |
| P4.5 by skill and by what is there | monotone; zero where nothing is | monotone; `finding.made` on a genuine paper | FOLLOWS; WORD |
| P4.6 usable | told, cited, a lead | a found deed raises a question on the doer (the tree's own test); telling it names no hand for paired kinds (F-FI-11) | FOLLOWS at EXECUTES, cited limits |
| P4.7 looking again | neither a free reroll nor futile by rule | `Failure`: a free reroll; `Partial`: futile by rule for ever | **INVERTED · BEHAVIOUR** |

**Play-back.** *The magistrate reads the grant nine times and sees nothing. The tenth time he sees it
is false, and from that day he can never see whose hand wrote it, however long he studies it. Had he
been slower, he might have.*

### 2.3 P3 "A forged letter is believed until someone who knows better sees it": holds to "is believed" (EXECUTES), then every later link is inert or asserted; INERT at FIRES

**Runs** (`p3_forgery.py`, `p3b_knows.py`; tiny world; the forger forges or, as the control, surveys
a sheet of a faction, and hands it on by `give`; candidates are `opening_set` over `questions_for`
for the receiver; realm counts from `fi_arms.py`, seed 0, three seasons).

| # | link | O | C observed | verdict · cause |
|---|---|---|---|---|
| P3.1 | forged, by an act with skill in it | could go well or badly | `forge` writes with certainty once admitted; quality is one fixture (`default_forgery_quality` 1) for every forger; realm: 113 attempted, 52 written, 61 refused by the `requires` cell | DEPARTS · BEHAVIOUR (no draw: the standing rule; the determinism sweep lists `forge`) |
| P3.1b | the making can be seen | maybe, by chance | everyone in the room holds `(paper, record.forged, True)` firsthand and a sighting naming the forger, with certainty. Realm: 12 of 52 forgeries were known forged, to up to 7 others, the instant they were made | DEPARTS · BEHAVIOUR (a forger cannot forge unseen in company, and every bystander recognises the act as forging; `18_DETERMINISM_notice_is_a_draw` is the owner) |
| P3.2 | a letter that purports an author | an author field that is false | a `faction_sheet` (proposition, members, holdings, seats, head) with the forger written in as `head`. There is no author, sender or seal on any Record | DEPARTS · WORD: `forge` forges a roll with oneself at its head, the same for every forger (F-FI-10) |
| P3.3 | is believed | the reader acts as if it were true | a holder's candidates take `to` from the sheet's `head`: 19 (a hearth member) and 28 (the Duke) candidates addressed to the forger, by `challenge`, `capture`, `determine`, `exchange`, `interview`, `move`, `pardon`, `raze`, `sabotage`, `speak`, `surveil`, `train`, `transfer`. Control (surveyed sheet, `head: None`): the same candidates with `to` bound to **the paper itself** | FOLLOWS at EXECUTES, with a COMPOSITION defect: being named head earns the forger a duke's `challenge` and `capture` as readily as his `exchange` |
| P3.3 | (FIRES) | forgeries reach readers | **0 of 52 forgeries ever left the forger's hand** (0 of 57 and 0 of 40 in the two cut arms); `give` 25 attempted, 1 executed | **INERT at FIRES** |
| P3.4 | someone who knows better | a definite set | nobody can. The content claim's subject is the paper, so no claim a person holds shares a cell with it, and nothing can contradict it. A man who **watched the forging** and is then handed the sheet is offered 116 candidates, 19 of them addressed to the forger off the sheet; with that knowledge deleted from his ledger (control): 116 and 19, the same candidates | **INERT** (knowledge of the forgery is read by nothing) |
| P3.5 | sees it; odds by what he knows | a draw, ordered by knowledge | a draw ordered by the reader's `inquiry` pool and the fixture quality (§2.2's table); knowledge of the faction, of the forger or of the true head plays no part | DEPARTS · BEHAVIOUR (skill, not knowledge) |
| P3.6 | until: then he disbelieves | the content is discounted | after his own `Success` find the holder holds `(paper, record.forged)` and `(forger, record.forged)`, **and the content claim unchanged at confidence 100, firsthand**; 21 of his candidates still read `to: the forger` off the sheet | **DEPARTS · BEHAVIOUR** (disbelief has no carrier) |
| P3.7 | a genuine letter is not called forged | control | a surveyed sheet has an empty trail; 0 `record.forged` claims in any band | FOLLOWS |

**Play-back.** *A stranger writes out the roll of the Duke's house with his own name at its head, in
front of two clerks who watch him do it. He keeps it in his coat for three years. In the one telling
where he hands it to a clerk who watched, the clerk weighs challenging him, questioning him and
trading with him as head of the house, exactly as he would had he not watched. The Duke, handed the
same roll, proves it false and goes on reading it as true.*

**What the precedent asks and the code lacks** (L.A. Noire, Ace Attorney, Obra Dinn: a document is
set against what the reader holds): a cell the paper and the reader's ledger share. The fix is at one
owner and is `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md`.

### 2.4 P5 "A crime leaves traces": does not hold; the only trace of a deed is the memory of those in the room at that instant

**Run** (`p5_crime.py`; tiny world, shipped fixtures; the killing is the real `fight` fold at a
forced `Felled`, the sabotage the real act; the visitor's inquiries are real acts, 40 act ids each).

*A killing with nobody else present* (the King, alone at the realm rung, by a stranger):

| who | holds, the instant after |
|---|---|
| the killer | `(King, person.died)`, the sighting naming himself |
| every other living person, anywhere | `(the King's seat, tenure.closed)` `told_by`, hand withheld: the `chronicle` channel |
| every other living person | **nothing about the King** |

Then: a visitor reaches the place one tick later and learns nothing (there is no body; a Person is
deleted). `surveil` of the place, 40 acts: 12 `finding.made`, nothing about the King. `interview` of
the killer, 40 acts: 40 `finding.made`, nothing. `reconstruct` on the King, 40 acts: 40
`finding.made`, and what he holds is `(King, finding.made, True)`. `trail_of` is empty for the place,
for the killer and for the victim. The visitor is still offered `tell` and `lie` candidates naming the
dead man. A duke two rungs away is offered `confer` on the King's seat. **Control** (two bystanders in
the room): both hold the death and the killer's name, with certainty.

*A sabotage with nobody else present* (a harbour, condition 900 → 0 in one act, with no draw): the
saboteur alone holds anything about the site. The Duke returns, a visitor arrives: neither holds
anything. The visitor's `examine` of the ruined harbour, 40 acts (hand-built: the chooser never forms
`examine`, F-FI-12): 15 `finding.made`, and he holds `(harbour, exists:Site, 1)` and
`(harbour, finding.made, True)`. **He has examined a ruin and does not hold that it is ruined.**

*The roster.* `rosters.yaml: covert_kinds` is `[record.forged]`. The verb rows emit 89 deed kinds;
thirteen are harm-shaped (`person.died`, `body.changed`, `person.captured`, `arrest.made`,
`site.damaged`, `rung.razed`, `record.seized`, `rung.seized`, `requisition.taken`,
`record.destroyed`, `cover.assumed`, `record.forged`, `arrest.resisted`). One of thirteen leaves a
trail, and it is the one whose trail the realm never reaches (§2.3).

| # | link | O | C | verdict · cause |
|---|---|---|---|---|
| P5.1 | a crime | an act with an author, a place, a time | yes: Events with `causes[]` to the act | FOLLOWS (in the log, which no person reads) |
| P5.2 | leaves | the act itself produces traces | only the WITNESS deposit of that tick | DEPARTS |
| P5.3 | traces of several kinds | witnesses, the changed thing, documents | witnesses only. The changed thing is not perceivable: a later visitor sees no body and no ruin; `examine` and `surveil` read nothing of state | **DEPARTS · BEHAVIOUR** |
| P5.4 | specific, pointing at the author | varying strength | certainty for those present (who is always shown); nothing for anyone else | DEPARTS (no gradation: the standing rule) |
| P5.5 | for a time; hidden at a cost | fading; concealment is an act | a witness's claim decays 5 a season; nothing else exists to fade or to hide. `conceal` re-anchors a deed for the far channels and those present still see the hand (H-324, cited) | ASSERTED |
| P5.6 | found by looking in the right place | the scene, or a witness | the scene yields nothing. A witness can be reached only if he volunteers a telling, and for a killing his telling names no hand (F-FI-11) | **INERT** |
| P5.7 | leading to the author before a body | the pipeline | no step of `19_LACUNA` §3's pipeline can start from an unwitnessed deed | UNREACHED |
| P5.8 | zero; planting | no crime, no trace; framing possible | no crime, no trace: FOLLOWS. Nothing can be planted: no act mints a false deed claim (H-198) | FOLLOWS; ASSERTED |

**The composition defect.** The realm learns at once, everywhere, that the King's seat is empty, and
no one but the killer can ever learn that the King is dead, where, or by whom. The succession can
proceed; the murder cannot be a story.

**Play-back.** *A stranger kills the King in an empty hall. By nightfall every village knows the
throne is vacant. Nobody finds a body, because there is none; nobody can ask what happened, because
no question about it can be formed; a magistrate who searches the hall for a year learns that the
hall exists.*

### 2.5 P1 "A person acts on what he has seen or been told, not on what is true": holds for a quantity a requirement names; does not hold for who exists, nor for what a claim says

**Runs** (`p1_belief.py`, `p1b_belief.py`; tiny world; one person at a hearth whose true grain is
8; counterfactual pairs, each differing in one thing; candidates are `opening_set` over
`questions_for`; then three seasons in which only he acts, shipped chooser, twelve world seeds).

| arm | what differs | candidates against the arm's control |
|---|---|---|
| `true` | he holds `(hearth, stores:grain, 8)` | +28 (a claim about the hearth raises a question on it) |
| `false-empty` | he holds `(hearth, stores:grain, 0)`; the hearth is full | the same +28 **less 12** (`exchange` 6, `transfer` 6): clause 4 declines on the false belief |
| `stale-full` | he holds 8; the world's hearth was emptied silently | identical to `true`: he forms the transfer on the stale belief |
| `silent-empty` | he holds nothing; the hearth emptied silently | identical to control: no leak |
| `dead-false` | he holds `(King, person.died, True)`; the King lives | **+28 candidates about the King**: `challenge`, `interview`, `tell` ×4, `lie` ×4, `move`, `speak`, `surveil`, `transfer`, `tie / knot`, … |
| `dead-silent` | the King is removed from the world silently; he holds nothing of it | **−28: every candidate about the King is gone** |

Three readings.

1. **For a quantity a `requires` cell names, the premise holds end to end, and this is the best
   thing in the subsystem.** The false belief declines the act; the stale belief forms it; the fold
   refuses it; the refusal's observation lands in his ledger (`(hearth, stores:grain, 0)`, firsthand,
   one tick later) and the transfer candidates fall from 7 to 0. In the three-season runs the
   `false-empty` arm's attempted acts differ from the `true` arm's at 10 of 12 seeds. (Steelman
   holds: attacked by the silent-empty control and by the refusal probe; it stands.)
2. **Whether a person exists is read from the truth, by subtraction** (INVERTED pair, rows 5 and 6).
   A man who believes the King dead is offered to challenge and interview him; a man who knows nothing
   stops being offered anything about the King the instant the King is deleted. The owner is
   `queries/world_q.py::questions_for`'s claim loop (clauses 1 and 2): a held claim raises a question
   only where its subject is in `reach(w, p)` or `place_of(w, subject)` is, and both are world reads,
   so a subject that no longer exists raises nothing. The first FI audit read clause 2 as harmless (its R-04: *"filters the person's
   own landed claims and adds no referent"*). It adds none and removes them on a fact he was never
   told, which is the same leak with the sign changed; F-FI-01's probes could not see it because they
   moved a seat, not a person.
3. **What a claim says is read by nothing but clause 4.** Any claim about X raises the same
   candidates about X (28 here for the hearth and for the King alike). `person.died` is not a cell a
   requirement reads (`individual`, `with` are world-only stems), so a belief that a man is dead
   cannot decline `challenge` on him, and no verb is offered *because* he is dead. News is a pointer
   to a subject; its content steers only the dozen store, condition and containment cells.

4. **Where another person is, is read from the truth too** (`p1d_where.py`). The King's containment
   is edited on the World to a second realm, with no Event and no WITNESS; the subject's ledger is
   identical before and after. Candidates naming the King: 38 → 10. The same claim loop: `place_of` is
   where the King is *now*. A man's options about a person he has heard of change when that person
   leaves the valley, though no one has told him.
5. **The engine's own word for "gone" is a different claim from the one a witness of a death
   receives** (`p1c_exists.py`). A requirement asks `kind: Person` of its subject and the ledger answers
   it from `(X, exists:Person, v)`. Planting `(King, exists:Person, 0)` declines `challenge`,
   `interview`, `train` and the cell lies about him (and leaves `tell`, `move`, `speak`, `surveil`,
   `transfer`, `tie / knot` formed, whose cells ask nothing of his being a person). A witness of a
   killing is given `(King, person.died, True)`, which declines nothing. Correction by refusal works
   here as it does for stores: a hand-built `challenge` on a silently deleted King is refused, the
   observation `(King, exists:Person, 0)` lands, and candidates naming him fall from 38 to 16; the same
   refusal through `interview` teaches nothing, because `finding.none` is deposited to nobody
   (CP-T06-04, scheduled, is that repair).

At CHOOSE the death arms have no power in this fixture: the control chose no act naming the King at
any of 12 seeds, so "0 of 12 differ" is not a reading. The FORMS rows above are.

**Link table.**

| # | O | C | verdict · cause |
|---|---|---|---|
| P1.1 truth and holdings are two things | yes | yes: `Person.ledger` against `World` | FOLLOWS |
| P1.2 seen | present, he holds it | by `co_located`, with certainty and in full (who, what) | FOLLOWS (no draw on noticing: cited) |
| P1.3 told | a telling names its teller | the told claim carries `chain`; but 14,252 of 14,272 `told_by` claims at seed 0, three seasons, have no teller (the broadcast; F-FI-05) | FOLLOWS at EXECUTES; DEPARTS at FIRES |
| P1.4 a holding may be false | stale, lied, forged, misheard | stale: yes (117 firsthand cells false of 1,651); lied or misheard: 17 of 18 told cells false; forged: never reaches a reader | FOLLOWS, thin |
| P1.5 he acts on it | choice reads holdings | for requirement cells: yes. For a claim's content otherwise: no (reading 3) | FOLLOWS, narrowed; DEPARTS · BEHAVIOUR |
| P1.6 not on what is true | truth alone changes nothing | stores: holds (`silent-empty`). Persons: fails (`dead-silent`). Seats, vacancies, aims: fails (F-FI-01, cited) | **DEPARTS · BEHAVIOUR**, three families |
| P1.7 correction | truth arrives, holding and act change | by refusal: yes, for the cell that refused | FOLLOWS |
| P1.8 holds nothing, does nothing | zero | a person with an empty ledger still has the world-stamped questions | DEPARTS (F-FI-01) |

