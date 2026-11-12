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

**The information layer is the realm's busiest engine and it informs nobody: of the five premise
sentences of knowing, one holds in part and four break, and cutting every information verb from the
chooser makes the world more eventful, not less.** In the shipped realm at seed 0 over three seasons,
with no player, 73.7% of the acts anyone carries out are information verbs (`create_record` 350,
`utter` 199, `research` 128, `reconstruct` 117, `surveil` 80, `forge` 52, `interview` 37, `conceal` 34)
and 93.9% of the 74,510 Events are ledger bookkeeping (`claim.deposited`, `claim.decayed`). What that
activity carries: ten tellings land; no rumour passes a second mouth, and on a hand-driven chain none
can, because the second teller says only that he was told (§2.1); the false beliefs the first FI audit
counted as formed by telling are seven people holding that one man exists twice; 52 papers are forged
and none leaves its forger's hand; no inquiry finds anything; every death in the arms run here (six,
at two seeds) is known as a death only to the six or seven people in the room. With every information verb removed
from the chooser (the cut `nofi`, same world, same seed, against a draw-seed control), persons march
53 times instead of 29, move 94 times instead of 21, issue 65 writs instead of 29, carry `determine`
through three times instead of never, fight once, and two men die (§1.1): the information verbs as the chooser
forms them are a false N-line, and they are spending the scenes the rest of the game needs. The parts
that hold are worth keeping and are stated as such: for a quantity a requirement names, a person does
act on what he believes and is corrected by being refused (§2.5 reading 1); the per-holder ledger and
the witness barrier are honest; the far channels are what make any act form at a distance (§1.1,
`presence`: no marches at all without them).

**The single largest obstacle** is that knowledge in this engine is a pointer and not a content: a
claim raises a question about its subject, and nothing but a dozen requirement cells reads what the
claim says. So "the King is dead" and "the King is well" produce the same candidates (§2.5), a paper
known to be false is read as true (§2.3), a deed leaves nothing a later look can read (§2.4), and what
people choose to tell one another is whichever claim is newest, most often that someone exists
(§2.1). The noir precedent the lane is built on (evidence that must be found, read, contradicted and
cited) needs content that binds; three proposals below are the smallest edits that give it some.

**On the standing rule** (*we do not do deterministic*): in this scope the draws are `research`,
`surveil`, `examine` (unformed), `tell` and `lie`. Fixed functions of state that could go either way
in the fiction, each observed here: every person present at a deed notices it and knows the hand
(§2.3, §2.4); `forge` writes at one quality; `interview` and `reconstruct` "find" 40 times in 40;
`sabotage` takes a harbour from 900 to 0 in one act; a `Partial` find forbids the hand for ever by rule
(§2.2); a `Success` telling is a perfect copy at any depth (§2.1); the realm learns of a vacated seat
at once and whole. `audits/18_DETERMINISM_SWEEP.md` C-02, C-05 and C-15 own the first, second and
fourth; the rest are listed in §4 for that lane.

*(Section order below is the order the work was done in, so that a partial file was usable
throughout: §2.0 holds the ordinary-meaning predictions, written before any FI note or code was
opened; §1 and §3 follow §2 in the file.)*

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

## 1. NERS: cut tests, executed

Method: `skills/ners/SKILL.md`; definitions `CLAUDE.md` §0.06. Instrument A, with the cuts **run**:
`fi_arms.py SEED SEASONS ARM` builds `populated.build_realm(seed)`, applies one cut, runs the shipped
chooser, and writes the world's state projection (the GAME lane's `pes.proj`), the per-verb census
and the ledgers. Instrument B (`resolution-diagnostic`'s questions) was put to the one draw this
scope owns outright, `research`, in §2.2 (pool sweep, quality sweep, mirror at quality 0). All arms
below: seed 0, three seasons, `PYTHONHASHSEED=0`. **Control for every cut: `draw1`**, the shipped
world and fixtures with only the chooser's draw seed changed, which is what a cut must exceed to be a
reading and not a butterfly.

### 1.1 The arms

| | `ship` | `draw1` (control) | `notell` | `noc4` | `presence` | `nofi` |
|---|---|---|---|---|---|---|
| the cut | none | none (draw seed 1) | `tell`, `lie` removed from the chooser | clause 4 off (`belief_contradicts` → False) | `fan_out_mode: presence_only` (four far channels off) | all fourteen information verbs removed from the chooser |
| Events | 74,510 | 64,236 | 81,066 | 61,827 | 42,640 | 98,225 |
| of them ledger bookkeeping | 93.9% | 92.8% | 94.2% | 93.0% | 89.4% | 96.4% |
| claims held at the end | 35,351 | 29,710 | 39,375 | 29,532 | 19,710 | 45,902 |
| `told_by` claims / with a teller | 14,272 / 20 | 8,641 / 9 | 16,631 / 0 | 9,127 / 10 | 15 / 15 | 28,741 / 0 |
| acts attempted / carried out | 2,630 / 1,394 | 2,636 / 1,465 | 2,699 / 1,501 | 2,494 / 1,041 | 2,616 / 1,441 | 1,881 / 456 |
| carried out, information verbs | 1,027 (73.7%) | 1,133 (77.3%) | 1,131 (75.3%) | 783 (75.2%) | 1,165 (80.8%) | 0 |
| carried out, everything else | 367 | 332 | 370 | 258 | 276 | **456** |
| `march` | 29 | 14 | 27 | 13 | **0** | **53** |
| `move` carried out | 21 | 32 | 27 | 14 | 39 | **94** |
| `migrate` attempted / carried out | 116 / 16 | 74 / 8 | 122 / 16 | 118 / 6 | **0 / 0** | 224 / 24 |
| `issue` carried out | 29 | 17 | 37 | 19 | 32 | **65** |
| `petition` | 28 | 26 | 34 | 26 | 27 | **53** |
| `convene` | 17 | 11 | 16 | 11 | **3** | **34** |
| `dispatch` | 14 | 7 | 17 | 10 | 14 | 29 |
| `oblige` attempted / carried out | 111 / 42 | 92 / 39 | **0 / 0** | **0 / 0** | **0 / 0** | 9 / 9 |
| `capture` carried out | 0 | 2 | 1 | 0 | 5 | 5 |
| `determine` carried through | 0 | 0 | 0 | 0 | 0 | **3** |
| `fight` | 0 | 0 | 0 | 0 | 0 | **1** |
| `challenge` attempted (all refused but one) | 118 | 140 | 135 | **302** | 123 | 86 |
| persons dead | 0 | 1 | 0 | 0 | 1 | **2** |
| fields lost / unopposed | 1 / 3 | 0 / 5 | 0 / 4 | 0 / 2 | 0 / 0 | **3 / 9** |
| seats changed against `ship` | — | 1 | 0 | 0 | 2 | 1 |
| realm stores total | 4,070 grain | same | same | same | same | **3,960 grain** (and ore, salt, timber lower) |
| site conditions | — | same | same | same | same | same |

Seed 1, two seasons, `presence` against `ship`: `march` and `migrate` are attempted 0 times
under the cut (the zeroes replicate); the `ship` figures at that seed are in §8, run 14.

### 1.2 The N-lines, attacked

**N-1 · `tell` and `lie` — "cut them and nothing a person knows can reach another by a person's
act."** Walked: the cut `notell` removes all 20 chained claims. Everything else is inside the
control's spread: acts carried out 1,501 (control 1,465, `ship` 1,394), no seat, no death, stores and
sites the same, the same 52 forgeries. The one row outside it is `oblige` (111 attempted in `ship`, 92
in the control, 0 here); it is also 0 under `noc4` and `presence`, 1 under `nochron`, and 0 in `ship`
itself at seed 1, so it is one seed-0 chain that any perturbation breaks, not a reading on `tell`
`[UNVERIFIED: the chain]`. **FALSE N-LINE as the game runs** (disqualifier 2, no producer: the possibility "a rumour
reaches a third person" has no producer, §2.1; what the 20 claims carry is §2.1's table). N holds for
the design object once `said_of` can pass content on; today the cut is free.

**N-2 · the information verbs as the chooser forms them — "cut them and persons cannot learn, record,
conclude, conceal or deceive."** Walked: under `nofi` nobody researches, records, utters, forges,
conceals or tells. What the realm then does: 456 other acts carried out against 367 (control 332);
marches 53 against 29 (control 14); moves 94 against 21 (32); writs 65 against 29 (17); petitions 53
against 28 (26); sittings convened 34 against 17 (11); three `determine` carried through against none;
the one `fight` any arm formed; two deaths; three fields lost; the realm's stores lower for the first
time in any arm. Every one of those is outside the control. **FALSE N-LINE, and worse than free: the
cut is a gain.** The possibilities the verbs were to provide (a finding acted on, a forgery believed,
a record read by another) do not occur with them present (§3.2: 16 non-information acts in three
seasons answer an information Event), and their formation takes three quarters of the scenes. What
dies with the cut, honestly counted: the 16 answers; `commit` (95 → 0) and `argue` (68 attempted, 17
carried out → 0), both of which need a proposition someone has uttered. That is the narrowed
N-line: **`utter` is necessary to `commit` and `argue`; the other thirteen verbs, as formed, are
not necessary to anything that happens.** `[One seed with a control; a second seed was not run under
this cut: the machine was loaded. The direction is far outside the control on eleven rows.]`

*N-2 decomposed* (two narrower cuts, same seed and seasons; run 15). Which verbs hold the scenes:

| acts carried out | `ship` | `draw1` | `nod3`: `interview`, `reconstruct`, `thread_read` cut | `noinq`: all six inquiry rows cut | `nofi` |
|---|---|---|---|---|---|
| all | 1,394 | 1,465 | 1,410 | 1,228 | 456 |
| `create_record` + `utter` | 549 | 613 | 625 | 625 | 0 |
| `commit` (a promise to an uttered proposition) | 95 | 95 | 135 | 180 | 0 |
| the six inquiry rows | 365 | 397 | 247 | 0 | 0 |
| everything else but `commit` | 272 | 237 | 285 | 300 | **456** |
| `march` | 29 | 14 | 39 | 43 | 53 |
| resolved by a draw | 209 | 247 | 255 | **56** | 33 |
| an information Event answered by a non-information act | 16 | 23 | 14 | 10 | 0 |

Two readings. (i) Cutting the three inquiry rows that have no product (`nod3`) loses nothing
measurable (14 answers against 16, every state component inside the control) and frees nothing
either: the 157 scenes go to more records, utterances and research. A free cut. (ii) The scenes are
held by **`create_record` and `utter`**: about 550 to 625 acts in every arm that has them, persons
writing down what they have just seen and stating propositions, with `commit` following. The gain
under `nofi` appears only when those go. And the inquiry rows are where the realm's dice are: with
them cut, acts resolved by a draw fall from 209 to 56 (the GAME lane's census read the same from the
other side: most draws are `research`, which finds nothing).

**N-3 · clause 4 (`belief_contradicts`) — "cut it and a person's own ledger can refuse him nothing."**
Walked: `noc4`. Acts carried out fall from 1,394 to 1,041 (control 1,465); `challenge` attempts rise
from 118 to 302, `accept` 45 to 83, `comply` 47 to 91, `construe` 10 to 29, every one refused. Seats,
deaths, sites the same. **N HOLDS, NARROWED**: clause 4 does not make persons act wrongly on false
beliefs (the first FI audit: the world agreed with the decline in 460 of 461); it stops them spending
a quarter of their acts on what their own ledger already says is impossible. Restated: *cut it and
persons are a quarter less effective*, an economy, not a source of story. (The cut also silenced the
function's second caller, a witness's reading of another's act; `oblige`'s zero may belong there.)

**N-4 · the four far channels — "cut them and knowledge stops at the room."** Walked: `presence`.
Claims held fall by 44%; `told_by` from 14,272 to 15. `march` 29 → 0, `migrate` 116 → 0, `oblige`
111 → 0, `convene` 17 → 3, at seed 0, and `march` and `migrate` 0 again at seed 1. Seats, sites and
stores inside the control. **N HOLDS, NARROWED, and not in the direction its design claims.** What
dies is not asymmetry of knowledge (the cut *increases* it); what dies is every act that forms at a
distance. The far channels, in the realm, are the broadcast that makes a person far from a thing act
on it. That is also a warning for a scheduled edit: B10-14's CR-29 deletes `chronicle` with a
replacement `reach` channel, and the first FI audit's R-06 asks for it first; §1.3 reads that cut
alone.

**N-5 · the lossy copy and the liar's inflation, on non-quantities.** Walked in §2.1: nothing reads
`exists:Person = 2`. **FALSE N-LINE** (disqualifier 2: no reader). On quantities: N holds (cut it and
a rumoured store is always exact).

**N-6 · forgery quality** (`default_forgery_quality`, CR-94's future Coordination read). Walked in
§2.2: 0 → 1 moves the default examiner's failure from 68% to 91%; 1 → 3 moves nothing at pool 2 and
17 points at pool 4. **N HOLDS, NARROWED**: above 1 the dial is dead for every examiner at the
default pool, by the per-pool ceiling.

**N-7 · the per-holder ledger and the witness barrier.** Attacked from the `presence` arm (do persons
still hold different things when the broadcast is cut: yes, 19,710 claims, all firsthand but 15) and
from §2.5's counterfactual pairs (does a belief change an act: yes, for a quantity, at 10 of 12
seeds). **N HOLDS** in every direction tried. Residual: its content is read by clause 4 alone.

### 1.3 The `chronicle` channel cut alone (CR-29's paired deletion, with no replacement)

`nochron` arm: `epistemic.CHANNEL_PREDICATES["chronicle"]` forced `False`, everything else shipped;
seed 0, three seasons.

| | `ship` | `draw1` (control) | `nochron` | `presence` |
|---|---|---|---|---|
| Events | 74,510 | 64,236 | 44,301 | 42,640 |
| claims held | 35,351 | 29,710 | 21,018 | 19,710 |
| `told_by` claims | 14,272 | 8,641 | 36 | 15 |
| `march` | 29 | 14 | **4** | 0 |
| `migrate` attempted / carried out | 116 / 16 | 74 / 8 | **17** / 10 | 0 / 0 |
| `oblige` attempted | 111 | 92 | 1 | 0 |
| `convene` | 17 | 11 | 19 | 3 |
| acts carried out | 1,394 | 1,465 | 1,509 | 1,441 |
| seats, deaths, sites, stores total | — | 1 seat, 1 death | same as `ship` | 2 seats, 1 death |

Reading. `chronicle` alone mints all but 36 of the realm's `told_by` claims (the channel's own
docstring arm says the same of one season at an earlier tree; this is three seasons at HEAD), and with
it gone the realm all but stops marching (4, against 29 and a control of 14) and stops trying to
migrate (17 attempts against 116 and 74). `convene` is untouched, so its fall under `presence` belongs
to `document_key` or `post_remit`. **For CR-29:** the replacement `reach` roster has to carry the
kinds that `march` and `migrate` candidates form on, or the paired deletion removes the only army
movement the realm has. The first FI audit's R-06 (CR-29 first) stands, with this as its gate: `march`
and `migrate` attempts under the new channel inside the `draw1` spread of today's. And for the 40% of
the log that goes with it: the broadcast is also the performance cost (F-FI-05, cited).

### 1.4 R, S and E

**R-COMPLETE** fails at four written branches that are empty: a `Partial` find (§2.2), a telling's
second hop (§2.1), a doubted paper (§2.3), a deed with no witness (§2.4). **R-WORLD**: the seats this
scope owns (the teller, the forger, the investigator, the concealer) resolve the same way every
season and throw 16 hooks in three seasons that anyone outside the scope answers: dead seats, not
portraits. **R-CHOICE** at the investigator's seat, intent *"learn whose hand"*: `research` again
after a `Failure` (gain: another 1.3% chance; cost: a scene) against `research` after a `Partial`
(gain: nothing, by rule; cost: a scene): the second row is dominated to extinction, and the player
cannot see which row he is on unless he reads the roster. At the forger's seat, intent *"be taken
for the head"*: `forge` then `give` (the only route) forms `give` 25 times and carries it out once.
**R-VARIETY**: one inquiry skill, one forgery, one lie, one thing to tell.

**S, calculations consistent in methodology.** Three defects, each two ways of saying one thing:
(i) a death is `(X, person.died, True)` to a witness and `(X, exists:Person, 0)` to a requirement,
and only the second is read (§2.5); (ii) how much of a deed a band shows is graded for a finder
(`finding_terms`) and not for a hearer of the same deed at the same band (§2.1); (iii) `finding.made`
means "found" from three rows and "was admitted" from three (H-318, cited). **S-DOWN** (an
opportunity reaching a party with no post, published, distorted in transit, picked up by his own
perception): the design's carrier is the telling, and it fails at the second mouth; what does reach
the postless is `chronicle`, which is addressed to everyone, undistorted: a pass on "published", a
fail on "distorts", and scheduled for deletion. **Pauses correctly**: untested; nothing in this scope
is a multi-step scene.

**E, last, as a ratio.** Against what N and R found (one story that runs: a stale store corrected by
refusal; and acts at a distance formed from a broadcast), the overhead is 94% of the log, three
quarters of the acts and fourteen verbs. E-LEGIBILITY: a player cannot intuit that examining a ruin
teaches that it exists, that a better look forbids the answer, or that telling passes on the fact of
telling. **The ratio is poor, and the repair is mostly deletion of formation, not of mechanism**:
§5, item 1.

```
NERS PASS: FI (fieldwork, investigation, epistemics, information, witness)     INSTRUMENTS: A+B

MUST BE STATED AS A LIMIT
  - a rumour spreads                      — one hop by construction (§2.1)                    [C5, §3 dq 2]
  - a forged paper is believed, then not  — never leaves the hand; doubt has no carrier (§2.3) [C1]
  - a crime leaves traces                 — witnesses of the instant only (§2.4)               [C1, C2]
  - non-omniscience holds                 — not for who exists or where (§2.5), nor for seats (F-FI-01) [C3]
  - investigation is built out            — as formed, a cut that improves the game (§1.2 N-2) [§3]
MAY BE CLAIMED, HAVING SURVIVED
  - a person acts on a believed quantity and is corrected by refusal — attacked by the silent-edit
    control and the refusal probe; holds (§2.5 reading 1)
  - two persons hold different things      — attacked by the presence arm; holds
  - skill orders an inquiry's result       — pool sweep monotone; mirror at quality 0 exact (§2.2)

| axis / test | verdict | what would overturn it |
|---|---|---|
| N (six directions) | FINDINGS: N-1, N-2, N-5 false; N-3, N-4, N-6 narrowed; N-7 holds | a second seed in which `nofi` reads inside its control |
| E-OVERHEAD | FINDINGS | the 16 answers of §3.2 shown to carry a story |
| E-LEGIBILITY | FINDINGS | a player predicting §2.2's lockout or §2.1's second hop from the verbs' names |
| R-COMPLETE | FINDINGS (four empty branches) | any of the four producing a claim |
| R-VARIETY | FINDINGS | two persons with one ledger telling, forging or examining differently |
| R-WORLD | FINDINGS (dead seats) | an information Event answered by a non-information act more than 16 times in three seasons |
| R-CHOICE | FINDINGS at the investigator's seat (dominated to extinction); upper bound elsewhere | — |
| S-UP | N-A (no docket at this scale; the petition route is SC's) | — |
| S-DOWN | FAIL | a two-hop chain in a seeded run |
| S coverage · pause · methodology | FINDINGS (three two-vocabulary defects) | — |
| the design's own falsifier (§8 of the skill): "nothing reaches belief unmediated" (AX-7) | HITS, one family: the question loop's world reads (seats, vacancies, existence, place) | — |
| self-audit (§9) | 9a: §2.2's correction of addendum B's C-3 was carried into §1.2 N-6 and proposal B's header; §2.5's CHOOSE reading was withdrawn where it had no power. 9b: proposals A, B, C add one derived set, one reader and four roster rows, no store, no guard | an independent reviewer would re-run `nofi` at seeds 1 and 2 |

GRADE: runs — the probe scripts and realm arms of §8
```

## 3. Emergent narrative: what stories this scope produces with nobody playing

Instruments. The tree's story instruments (`harness/storybar.py`, `chronicle.py`, `arc.py`,
`strife.py`, `aperture.py`) were not re-run here: the WR and GAME lanes own those readings
(`audits/09_WR_audit.md`, `16_PESSIMIST_GAME.md` §1.2), and a story bar counts chains by depth, which
for this scope is persons recording that a granary filled. The instrument used is this lane's
extension of the GAME lane's ancestry reading (`pes.seam_edges`) restricted to information Events,
plus the ledgers and the per-verb census of the §1 arms: it asks what an information Event *causes
someone else to do*, and what the ledgers hold at the end.

### 3.1 The stories this scope can produce, enumerated from the code, and what computed play did

Columns: EXECUTES = a hand-built act produces the link (§2); FIRES = it occurred in the shipped realm
(seed 0, three seasons; seed 1, two seasons; the `draw1` control where it adds a case).

| # | story | EXECUTES | FIRES | verdict |
|---|---|---|---|---|
| 1 | *He went to the granary on what he believed and found it otherwise.* A stale or false quantity, acted on, refused, corrected. | yes (§2.5) | yes: 117 firsthand cells false at the end; `transfer` 70 attempted, 2 carried out, each refusal teaching the cell | **the one story that runs.** It is small, private and ends in one step |
| 2 | *Word came that the seat was empty.* Realm-wide knowledge of a vacated seat. | yes | yes, by broadcast, at once, to everyone | runs, with no teller, no delay and no error |
| 3 | *A man was introduced.* A telling that a person exists makes the hearer know of him. | yes | yes: 3 of the 7 tellings that landed in two seasons | runs; it is most of what is said |
| 4 | *The report was wrong by the time it arrived.* A garbled quantity at second hand, acted on. | one hop | 1 told quantity in two seasons (grain 86 for 74, itself a lie); acted on: not observed | possible at one hop; not observed |
| 5 | *The rumour ran ahead of the truth.* Two or more hops. | **no** (§2.1) | 0 chains over one hop in every arm (20, 9, 10, 15, 5, 13 chained claims, all one hop) | **cannot happen** |
| 6 | *The liar was caught.* | privately (`record`, a number per hearer) | no Event, no claim, no act (F-FI-04, cited) | cannot be told as a story |
| 7 | *The forged grant was believed.* | yes (§2.3) | 0 of 52, 53, 52, 40, 57, 51, 34, 37 forgeries (eight arms) left their forger's hand | **does not happen** |
| 8 | *The forgery was exposed.* | the find, yes; the disbelief, no (§2.3) | 0 found deposits (first FI audit, three seeds) | the first half cannot begin; the second has no carrier |
| 9 | *Nobody saw it done, and it was found out.* An unwitnessed deed uncovered later. | **no** (§2.4) | — | **cannot happen** |
| 10 | *They say the steward killed him.* A killing reported at second hand, with a name. | no (F-FI-11, cited) | six deaths across the arms; each held as a death by the six or seven persons present, by nobody else, and told to nobody | **cannot happen**; and in the runs no death is even reported without a name |
| 11 | *He looked and found the hand.* | yes at `Success` (§2.2) | `research` 128 acts and `surveil` 80 at seed 0: nothing to find | does not happen |
| 12 | *He kept looking and never could.* The `Partial` lockout. | yes (§2.2) | unreached (nothing to find) | would be the commonest ending of any inquiry: 85% at the default pool |
| 13 | *He hid who he was.* `conceal`. | the cover is minted | 34 covers at seed 0; those present see the hand anyway (H-324); no inquiry can find a cover | an act with no consequence |
| 14 | *He acted on a dead man's standing.* News not having reached him. | **inverted** (§2.5: the engine removes the dead from his options) | — | **cannot happen** |
| 15 | *The wrong man was accused.* | no conclusion can be stated (F-FI-03, cited) | — | cannot happen |

### 3.2 What an information Event causes another person to do

`pes.seam_edges` over each arm's log: one edge per (answering act, antecedent Event) where the
antecedent is an information Event (`finding.*`, `news.*`, `tell.*`, `record.*`, `cover.*`,
`faction.surveyed`, `proposition.uttered`, `confession.*`) caused by another person's act and the
answering act was not refused.

| | `ship` s0, 3 seasons | `draw1` s0 | `ship` s1, 2 seasons |
|---|---|---|---|
| cross-person answers carried out, all antecedents | 513 | 472 | 309 |
| cross-person answers to an information Event, refused ones included | 157 | — | — |
| **an information Event answered by a non-information act** | **16** | 23 | 13 |

At seed 0 the sixteen are `finding.made → issue` 6, `tell.refused → issue` 3, `finding.made → move` 2,
and one each of `→ petition` (three antecedents), `→ open_case` (two). The commonest answers to an
information Event are more information: `finding.made → create_record` 9, `record.created →
create_record` 7, `proposition.uttered → utter` 5, `record.created → utter` 5,
`finding.made → reconstruct` 4. A finding leads to a record; a record leads to a record.

### 3.3 The tail: are all runs the same run

Yes, for this scope. Across `ship`, `draw1`, the three cuts that leave the information verbs in, and
seed 1: forgeries 52, 53, 52, 40, 57, 34 and none travels; chained claims 20, 9, 0, 10, 15, 5, all one
hop; rumours (distinct subject, predicate and origin) 7, 3, 0, 3, 3, 1, the widest held by 7 persons
(the room); found deposits 0; `interview` and `reconstruct` "find" every time. The runs differ in
which granary someone is wrong about.

### 3.4 What a player's choice changes

At EXECUTES, a player seated on a person can do four things the chooser does not: hand a forged paper
on (`give`: the tree's own trail fixture), examine it repeatedly, sabotage a site that is a Site, and
kill in private. Each leads into §2's broken links: the paper is believed and cannot be disbelieved;
the look ends in the lockout 85 times in 100; the ruin and the body cannot be found by anyone. He
cannot choose what to say (F-FI-10), state a conclusion (F-FI-03), accuse on evidence (F-FI-09), or
learn anything by questioning (`interview`: 40 of 40 "found", nothing held).

### 3.5 The extremes

| extreme | observed |
|---|---|
| a rumour at six hops (proxy) | stored at confidence 100; a quantity of 40 arrives as anything from 10 to 122; a deed arrives exact |
| a quantity of 0 | never garbled, and never produced by garbling |
| the weakest examiner (pool 1) | `Success` 0 in 300 on a forged and on a genuine paper |
| the strongest (pool 7) | locked out of the hand by a `Partial` in a third of cases |
| forgery quality above 1 | no effect for an examiner at the default pool |
| one person acting alone in a world (§2.5's seasons) | runs; his tellings are refused (nobody is where he thinks) |
| the ledger over time | 12,351 → 22,958 → 35,351 claims over three seasons at seed 0; one `claim.decayed` Event per held claim per season (34,837 in three seasons, 46.8% of the log); the cap is 3,200 a person, so the log's bookkeeping share rises until then |
| every information verb removed | the realm does more (§1.2 N-2) |
| every far channel removed | the realm stops marching and migrating (§1.2 N-4) |

## 4. Findings, ranked worst first

Severity: *blocks* = blocks a requirement; *degrades* = degrades narrative; *hygiene*. Every falsifier
names its control. Proposal files are under `proposals/2026-11-12-subsystem-audit-suite/proposals/`.

| id | severity · requirement | finding | falsifier run · control | minimal fix at the owner |
|---|---|---|---|---|
| **F-PES-FI-01** | blocks R-05; degrades R-01, R-07 | **A deed leaves no trace but the memory of those present at that instant.** An unwitnessed killing or ruin is unknowable for ever; `examine` of a ruin teaches that the site exists; the realm learns a seat is empty and never that its holder died (§2.4) | `p5_crime.py` · the same killing with two bystanders (they hold it) | `16_PESSIMIST_FI_C` edits 1–3 (three roster rows; CP-T06-01's object list; the ending deposited as `exists:<Kind>` 0) |
| **F-PES-FI-02** | degrades R-01, R-07 | **A rumour is one telling long, by construction; and what is said is mostly that someone exists.** The second teller says "there was a telling". The first FI audit's seven told-false cells are `(p_npc_004, exists:Person, 2)` (§2.1) | `p2_chain.py`, `told_dump.py 0 2` · the proxy chain in which content is passed on (it travels and drifts) | `08_FI_02` (cited) **amended by** `16_PESSIMIST_FI_A` edit 5: as written its slant would prefer the realm's 577 existence readings to every deed |
| **F-PES-FI-03** | degrades R-05, R-08 | **A forged paper is believed by nobody in play (0 of 376 across eight arms left the forger's hand), and where one is put in a hand, knowing it false changes nothing.** A man who watched the forging is offered the same 19 acts off it; after a `Success` find the content stands at confidence 100 (§2.3) | `p3b_knows.py` · the same holder with the knowledge deleted (identical candidates); the surveyed sheet | `16_PESSIMIST_FI_B` edits 1–3 |
| **F-PES-FI-04** | blocks R-07, R-08 (with F-FI-01) | **Who exists and where they are is read from the truth.** A silently deleted or relocated person leaves the subject's candidates (−28; 38 → 10) with his ledger unchanged; a man who believes the King dead is offered to challenge him (§2.5) | `p1_belief.py`, `p1d_where.py` · the silent-edit arm for a store (no leak) | `16_PESSIMIST_FI_C` edit 4 (the question loop reads `present_persons` and the holder's own `exists` cell); the decision is ED-IN-0292's |
| **F-PES-FI-05** | degrades R-04, R-05 | **The information verbs, as the chooser forms them, crowd the game out.** They are 73.7% of acts carried out; with them cut the realm marches 53 times for 29, moves 94 for 21, determines 3 matters for 0, fights, and two die; with only `tell` and `lie` cut nothing changes (§1.2 N-1, N-2) | `fi_arms.py 0 3 nofi`, `notell`, `nod3`, `noinq` · `draw1` (the draw-seed control) | `16_PESSIMIST_FI_D`: the three product-less inquiry rows join `withheld_verbs` until their products land (a free cut, measured). The sink itself is `create_record` and `utter` (about 600 acts in three seasons): what a scene is spent on is the chooser's scoring, CHAR's and CORE's; named for the orchestrator, not authored here |
| **F-PES-FI-06** | degrades R-09 | **Distortion is a drift applied to anything stored as a number, and to nothing else.** Existence flags garble to 2 and 3; a deed never distorts; a `Success` copy is perfect at any depth; 0 is a fixed point; the mean drifts upward (40 → 49 in six hops) (§2.1) | `p2_proxy.py` · the all-`Success` arm (exact), the deed arm (exact) | `16_PESSIMIST_FI_A` edits 1–4; the drift's bias is `[OPEN — Jordan tuning]` |
| **F-PES-FI-07** | degrades R-05, R-09 | **A better look is worse than a failed one.** At the default pool the hand of a forgery is found in 15% of unlimited retries and forbidden for ever in 85%; at pool 7, a third. Addendum B's C-3 (quality "inert", quality 3 "refused") is false at HEAD (§2.2) | `p4_detective.py` · the genuine sheet; quality 0 reproduces it exactly | CP-T06-03 (scheduled; unchanged). The correction to C-3 is in proposal B's header |
| **F-PES-FI-08** | degrades R-06, R-08 | **A claim is a pointer: what it says is read by clause 4 alone.** Any claim about X raises the same candidates about X; `person.died` declines nothing while `exists:Person 0` does: two words for one fact (§2.5 readings 3 and 5) | `p1_belief.py` (`true` against `dead-false`: +28 each), `p1c_exists.py` · the false-empty store arm (content read) | `16_PESSIMIST_FI_C` edit 3 (one vocabulary for an ending). The general case (content shaping what is offered) is CHAR's question projection; named, not authored |
| **F-PES-FI-09** | degrades R-01 | **News of a death does not travel.** Six deaths in the arms; each held as a death by the 6 or 7 persons present and by no one else at the end of the run (up to three seasons) (§3.1 row 10) | `fi_arms.py` (`draw1`, `presence`, `nofi`, seed 1 `presence`) · `tenure.closed` for the same men is held by everyone | F-FI-11's fix (`08_FI_06`) plus `08_FI_02`; and CR-29's `reach` row for `person.died` if seat news stays realm-wide (first FI audit §11 item 1) |
| **F-PES-FI-10** | degrades R-01 (a warning on a scheduled edit) | **Cutting `chronicle` alone takes the realm's marches from 29 to 4 and its migration attempts from 116 to 17** (control 14 and 74) (§1.3) | `fi_arms.py 0 3 nochron` · `draw1` | CR-29's `reach` roster carries the kinds `march` and `migrate` form on; gate stated in §1.3 |
| **F-PES-FI-11** | degrades R-09 (the standing rule) | **Fixed outcomes that could go either way:** `interview` and `reconstruct` 40 of 40; a `Partial` forbids the hand by rule; a `Success` telling is exact; the vacated seat is known to all at once; (and, owned by `18_DETERMINISM_SWEEP` C-02, C-05, C-15: notice, forgery quality, sabotage 900 → 0) | §2.2, §2.4, `p2_proxy.py` · the graded rows beside them | CP-T06-03; CP-T06-05 (the questioned person answers by his own draw); `16_PESSIMIST_FI_A` edit 4; `18_DETERMINISM_*` |
| **F-PES-FI-12** | hygiene (performance) | **93.9% of the log is ledger bookkeeping**, half of it one decay Event per held claim per season, growing with the ledgers (§3.5) | `fi_arms.py` Event census · `presence` (89.4%) | none proposed: CR-29 removes the broadcast's share; whether decay needs an Event per claim is IN's (`04` §A.2's write rule) |
| **F-PES-FI-13** | hygiene | Candidates formed with a Record's id where a person is meant (`interview … to <paper>`, 12 and 16 on a sheet with no head); `transfer` from a hearth to itself; a man told that he himself exists | `p3_forgery.py`, `p1b_belief.py`, `told_dump.py` | `16_PESSIMIST_FI_B` edit 4; the others named for CHAR's operand bags |

**Corrections to cited lanes** (each re-run here): addendum B C-3 (forgery quality: §2.2); first FI
audit R-04 (clause 2 "adds no referent": it removes them on world truth, §2.5); first FI audit F-FI-04
and §1a (the told-false cells are existence readings, §2.1); `08_FI_02` edit 2 (its `cell` tier
prefers existence readings, proposal A edit 5).

## 5. Path, proposals and what is left for Jordan

**Ordered** (each with its gate in the proposal):

1. `16_PESSIMIST_FI_D_withhold_what_has_no_product.md`: three rows join `withheld_verbs`. A data
   edit and a free cut (157 acts in three seasons at seed 0 that teach nobody anything and "find" with
   certainty). It does not by itself release the world: the scenes go to records and utterances
   (§1.2, N-2 decomposed), and that sink is the chooser's.
2. `16_PESSIMIST_FI_A_what_a_rumour_can_garble.md` edits 1–3, then `08_FI_02` with A's edit 5.
3. `16_PESSIMIST_FI_C_what_a_deed_leaves_behind.md` edits 1–3 with B10-14's CP-T06-01, -02, -03, -04.
4. `16_PESSIMIST_FI_B_a_paper_is_about_something.md`.
5. `16_PESSIMIST_FI_C` edit 4 with `08_FI_01` (one change to the question loop, not two).
6. CR-29, gated by §1.3's reading.

**For Jordan** (survivors of the five-step ladder; each with two options that make different games):

- **S-PES-FI-1 · May a garbled deed name the wrong person?** Loss only (decided as the shipped arm) or
  substitution. In proposal A.
- **S-PES-FI-2 · How fast does a death travel compared with the seat it empties?** Today the seat is
  known everywhere at once and the death nowhere. *Option A, together:* the `reach` row that carries
  `tenure.closed` carries `person.died`; a realm that knows its King is dead the day he dies; fast,
  legible succession; a killer is the only unknown. *Option B, apart:* the seat by `reach`, the death
  by presence, trail and telling only; a realm that knows the throne is empty and argues for a season
  about why; pretenders, false reports of death (proposal A's lie), and an investigation that matters.
  The first FI audit's §11 item 1 asks the same of seats; this is its other half, and the two answers
  need not match.

Everything else in §4 is decided at ladder step 1, 3, 4 or 5 in the proposal that carries it.

## 6. The premises, the false N-lines and the stories, in one place

**Premises** (verdict by execution): P1 *holds for a quantity a requirement names; fails for who
exists, where they are, and what a claim says*. P2 *does not hold: one hop; only numbers distort*.
P3 *holds to "is believed" on a hand-built handover; inert in play; "until someone who knows better"
has no carrier*. P4 *holds for one look; inverted at the second*. P5 *does not hold*.

**False N-lines found:** `tell` and `lie` as the game runs (N-1); the information verbs as the
chooser forms them (N-2, a cut that is a gain); the lossy copy on non-quantities (N-5). **Narrowed:**
clause 4 (an economy, not a source of error); the far channels (they form acts at a distance; they do
not make knowledge asymmetric); forgery quality above 1. **Holds:** the per-holder ledger and witness
barrier; the quantity belief loop; skill ordering an inquiry.

**Stories that can happen:** a stale store corrected by refusal; a seat known empty; an
introduction; a wrong quantity at one remove. **Stories that cannot:** a rumour past one mouth; a
believed forgery in play; a forgery disbelieved; an unwitnessed crime found out; a death reported; a
liar exposed; acting on a dead man's standing; a wrong man accused.

## 7. The detective and noir precedent, read against these runs

The first FI audit's §16 and addendum B's §B3c judge which borrowings are understood and which only
named; the LACUNA lane states the pipeline. They are cited, not redone. What the runs add is where
each precedent's *first* requirement fails, which is earlier than those lanes place it:

| precedent | what its play rests on | where the engine stops, by run |
|---|---|---|
| Shadows of Doubt (procedural crime, a signature left at the scene, leads that chain) | a deed writes something a later visitor can read | §2.4: a killing and a ruin write nothing readable; one covert kind of thirteen |
| Return of the Obra Dinn (the scene reconstructed after the fact) | arriving later and working out what happened | §2.4: a visitor one tick later holds nothing; `examine` of a ruin teaches that it exists |
| L.A. Noire, Ace Attorney (a statement set against a held item) | the item and the statement share a subject, so one can contradict the other | §2.3: a paper's content is about the paper; nothing a person holds can contradict it |
| Lacuna (a committed conclusion the world answers later) | a wrong conclusion acted on | §2.5: a claim's content is read by clause 4 alone, so a wrong belief about a person changes nothing he does |
| Disco Elysium, Pentiment (a community that talks, and remembers what it heard) | talk with content, moving between people | §2.1: one hop; the content is that someone exists |
| The Case of the Golden Idol (a typed assertion a machine can grade) | — | nothing run here bears on it; F-FI-09 stands as cited |

The nulls the first audit marked stand (no shipped game makes NPC-to-NPC rumour the main carrier of
a strategic layer). One is added: **no run here could test a noir staple, the misleading clue**,
because nothing can be planted (P5.8) and a finding is never false (§2.2: a find is true to the log
or absent). The design's refusal of a false finding on `Failure` (K-37, ratified as intent) and the
absence of planting together mean that every clue in the game is true. Whether that is wanted is
proposal A's survivor in another form; it is not escalated twice.

## 8. Evidence log

All `PYTHONHASHSEED=0`. Scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_FI/`.
Tiny-world probes use `harness/probes.tiny_world` at the shipped `DEFAULT_FIXTURES` (a test fixture,
not canon: it shows EXECUTES and FORMS, never FIRES). Realm runs use `populated.build_realm(seed)`,
the shipped chooser and fixtures, through the GAME lane's `pes.py`.

| # | script | world · seed · seasons | outcome |
|---|---|---|---|
| 1 | `p2_chain.py 1` | tiny + 7 persons · world seed 1 | §2.1 first table; identical for cell and deed, `Success` and `Partial` |
| 2 | `p2_chain_valence.py 1` (control) | the same at `said_slant: valence` | the same table |
| 3 | `p2_proxy.py` (PROXY) | the same · world seeds 1–20 · 6 hops | §2.1 second table; deed, existence, ordinal, 1 and 0 arms at seed 1 |
| 4 | `told_dump.py 0 2` | realm · 0 · 2 | hash `bacd687f1470883b412be9638d0b0f88` (the first FI audit's run 8); 37,646 Events; §2.1 third table |
| 5 | `p4_detective.py 300` | tiny (the trail fixture's shape) · 300 act ids per cell | §2.2; RESOLVE only for the band tables; (b) through WITNESS |
| 6 | `p3_forgery.py` | tiny | §2.3: who holds what after a forging; candidates forged against surveyed |
| 7 | `p3b_knows.py` | tiny | §2.3: 116 / 19 with and without the knowledge; 28 → 21 after a `Success` find, content at 100 |
| 8 | `p5_crime.py` | tiny | §2.4; `fight` folded at a forced `Felled` with both parties' wound states (the tree's `_scar_helpers` shape) |
| 9 | `p1_belief.py` | tiny · world seed 1 · 3 seasons, one actor | §2.5 table |
| 10 | `p1b_belief.py` | tiny · world seeds 1–12 · 3 seasons | `false-empty` differs from `true` at 10 of 12; refusal teaches the cell (7 → 0 transfer candidates) |
| 11 | `p1c_exists.py`, `p1d_where.py` | tiny | §2.5 readings 4 and 5 |
| 12 | `fi_arms.py 0 1 ship` (smoke) | realm · 0 · 1 | hash `5ab73af2…`, 13,379 Events: the first FI audit's run 4 |
| 13 | `fi_arms.py 0 3 <arm>` | realm · 0 · 3 | `ship` `52ff67bc…` (equal to the GAME lane's `x1` shipped arm, so this instrument perturbs nothing); `draw1` `a162bf8b`; `notell` `a9b3283d`; `noc4` `d45d46f2`; `presence` `a0742623`; `nofi` `56741b4b`; `nochron` `7a08179a`. §1.1, §1.3, §3 |
| 14 | `fi_arms.py 1 2 ship`, `presence` | realm · 1 · 2 | `ship` `8aae8412`: `march` 5, `migrate` 41 attempted / 4, forgeries 34 (0 travel), chained 5 (one hop), 13 non-information answers. `presence` `a992acee`: `march` 0, `migrate` 0, two deaths (6 firsthand holders each) |
| 15 | `fi_arms.py 0 3 nod3`, `noinq` | realm · 0 · 3 | §1.2 "N-2 decomposed"; proposal D's measured arm is `nod3` |

Not run: `pytest` (by instruction); `aperture`, `strife`, `storybar`, `chronicle`, `arc`,
`corpus_run`, `register --requirements`, `m1_acceptance` (cited from the lanes that ran them). A
second and third seed for `nofi`, `notell`, `noc4` and `nochron` (machine load of 25 to 45 throughout;
each three-season arm took 2 to 11 minutes of wall time): those four cuts are one seed with a
draw-seed control, and are stated as such where they are used.

Read: `PESSIMIST_BRIEF.md`, `AUDIT_BRIEF.md`, `skills/ners/SKILL.md`, `skills/premise-check/SKILL.md`
in full; `08_FI_audit.md` in full; addendum B §B2; `19_LACUNA…` §0, §3–§11; `16_PESSIMIST_GAME.md`
§0–§1; `08_FI_02`; `engine/season/epistemic.py` lines 1–759 in full and the rest with docstrings
stripped; `loop/witness.py`, and the forge, conceal, give, seize, destroy and mint bodies of
`loop/effects_information.py`, with docstrings stripped; `queries/person_q.py::said_of`,
`lie_said_of`, `drifted`, `is_cell`, `known_persons`; `decision/options.py::record`, `teller_weight`,
`_content_answer`; `queries/world_q.py::questions_for` (code); the verb rows; the trail fixture.
**Not read** (`[SKIPPED]`): `skills/resolution-diagnostic/SKILL.md` (its questions were taken from
the ners skill's description of it: a pool sweep, a quality sweep and a mirror); `modules/fieldwork/find.py`
(34 lines; cited from the first audit); the rest of `effects_information.py`; `08_FI_01`, `03`–`08` and
the four `19_LACUNA_*` proposals beyond what the audits say of them; `18_DETERMINISM_SWEEP.md` beyond
the rows C-02, C-05, C-15; `.designs/`, `.audit/` and `research/` (cited through the first audit and
its addendum). The §14 capability and §13 arcs charges of `AUDIT_BRIEF.md` were not redone: the first
audit's sections stand, and nothing measured here changes a row of either.

One mishap, corrected: a mistyped redirect wrote four small error files into the repository root
(`p2_chain_s1.out`, `p2_proxy.out`, `p3_forgery.out`, `p4_detective.out`); they were removed at once.
`git status --short` at the end shows this lane's files only (plus other lanes' own).

