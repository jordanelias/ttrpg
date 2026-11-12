# SC — pessimist audit: NERS, premise and emergent narrative, of the social contest and proceedings

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `modules/social_contest/`, `systems/social_contest/`, the contest seam (`engine/season/seam/`),
the arrangements and venues, the proceedings verbs (`petition`, `carry`, `open_case`, `convene`, `speak`,
`determine`), the evidence-and-argument pipeline with fieldwork (`audits/19_LACUNA_investigation_to_proceedings.md`),
the obstacle as the task's difficulty plus all modifiers, and five premise sentences of a contest. The
SC lane's audits (`05_SC_audit.md`, `05_SC_audit_addendum_B.md`, `13_SC_contest_interrogation.md`) and
the LACUNA lane (`19_…`) are cited, not redone. Everything measured here is new work unless a lane is
named. All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_SC/`.

Short names: `es/` = `engine/season/`; `K/` = `systems/social_contest/sim/contest/` (the kernel the
loop does not run).

**PARTIAL FILE — written early and appended (PESSIMIST_BRIEF: "write early and append"). Sections
below this line are filled as the runs complete; a section that reads `[PENDING]` was not reached.**

## 0. Verdict

**None of the five premise sentences of a contest holds as run: the social contest is one honest draw
whose outcome reads almost nothing of the people, the case or the room, and whose results are written
where nobody who matters can read them.** Each sentence was executed on the smallest world that exhibits
it, with controls:

- *A petitioner with a good case before a friendly bench usually wins.* The verdict (`determine`) dealt
  the same 105 Failure / 33 Partial / 12 Success over the same 150 seeded acts in all six cells of
  {hostile, neutral, friendly bench} × {no case, four firsthand proofs}; exact odds 0.74 / 0.19 / 0.07 /
  0.00 in every cell; the control (the judge's pool) moves it. The speech that does read the room is
  not ordered either (a good case changes nothing before a hostile bench; good + friendly = good alone =
  friendly alone), and it writes nothing. When the petitioner "wins", the accused owes a term of service
  to the judge's seat, the petitioner receives nothing, and the convict may end it himself in one act.
- *A lie is caught more often by someone who knows the truth.* The roll is the same against a knower and
  an ignorant hearer (0.74 Failure), the same for a master liar and a novice, and easier than telling an
  expert the truth (0.74 against 0.90). Nothing is ever "caught": a failed lie leaves no trace of a lie.
  A knower marks the liar's record down in 12 of 13 landed lies and an honest teller's in 13 of 16
  landed truths, because a Partial telling garbles by the same rule a lie falsifies by. And one season
  later the knower holds the truth in the reader that gates his acts (32 of 32) and the lie in the
  reader that fills his sheet and his mouth (31 of 32).
- *A hearing ends.* It ends by exhaustion only. A bench may ask again at once and without limit (eight
  askings bind the party 0.90 of the time); a failure clears nobody; a lapsed matter is re-opened in the
  same fold; the one defence that works is to walk out of the bench's ground.
- *A verdict changes standing.* After a determination, every person alive holds a claim about the judge
  and none about the convicted (0 of 4 witnesses, the convict included); everyone's regard for the
  convicted is unchanged; everyone's regard for the judge rises, the convict's too. After a *failed*
  determination every person alive holds the accused's name.
- *An NPC argues against an NPC and one of them is moved.* Somebody is moved in 20 of 300 arguments
  (0.07). What is argued, the hearer's commitment to the contrary, his zeal and his regard for the arguer
  change nothing; the arguer is never moved; two hundred repetitions convert the hearer at no cost.

The steelman is owed and holds where it was attacked: the seam is correct and stayed correct under three
new attacks (order of the fold, interleaved acts, replay: §1.6); firsthand knowledge is never overturned
by hearsay in the weighed reader, even from a teller the hearer loves and has always found right (§2.2).
The single largest obstacle is upstream of every proposal on file: **the draw is the only thing in a
contest that varies, and its band is read by nothing but the Event's own name** (four of seven contested
social rows write `[]` in every band, and a fifth, `arrest`, never executes). The SC lane's proposals give the draw inputs; this lane's finding
is that the *outputs* are equally absent, and that three of them are wrong rather than missing (§3,
F-PES-SC-02, -03, -06).

**On the standing rule** (*we do not do deterministic*): the contest itself always draws. What does not
draw, in this scope: what a hearer believes once a telling lands (a fixed function of whether he holds
the cell firsthand), whether a bench that failed may ask again (always), whether a lapsed matter may be
re-opened (always), whether a convict may discharge an imposed service (always), and whether a petition
is docketed (always). And the draw that exists is, for a bench that persists, a timer and not a
decision (§2.3).

## 1. NERS — cut tests, executed

Method: `skills/ners/SKILL.md` §1's cut test; definitions `CLAUDE.md` §0.06; for the draw,
`skills/resolution-diagnostic/SKILL.md` as evidence. A cut is *free* when nothing but the cut thing's
own Event names differs. All on `harness/probes.py::tiny_world` (a test fixture, not canon) through the
real fold and, where memory matters, the real season with WITNESS.

### 1.1 Cut `speak` (and with it the room: `reception`, `proofs`, the mirror, route erosion) — FREE

`n2_cuts.py` (i). One docketed matter; arm A, nobody speaks for three seasons; arm B, the speaker speaks
once a season. Compared: every live tenure, the docket, every person's pursuits and stance, the records,
the propositions, the bench's `reception` of the speaker, the judge's `regard` for him, and the exact
odds of the next `determine`.

| | arm A (no speech) | arm B (three speeches, all `matter.turned`) |
|---|---|---|
| world state changed | no | **no** |
| bench's deed claims about the speaker | none | **none** (the judge stands in another rung and witnesses nothing) |
| reception of the speaker | 0.00 | 0.00 |
| judge's regard for the speaker | 0.00 | 0.00 |
| `determine` odds after | 0.74 / 0.19 / 0.07 / 0.00 | the same |

The four bands of `speak` emit four kinds (`matter.carried / advanced / held / turned`); the alignment
table gives all four the same valence (0.16 for a holder of `honour`; printed in the run), so a reader of
deeds cannot tell a triumph from a rout. With F-SC-05 (b)'s grep (no reader of the four kinds) this
closes the cut from both sides: **the roll on `speak`, and therefore everything SC-02 `22a` built to
move it, is necessary to nothing that changes the world.** What dies with the cut: four Event names.

False N-line: *"the room reads you"* (`es/queries/world_q.py:766`). It does, and then nothing reads the
room. The steelman (the room is a channel waiting for a consumer; `05_SC_playable_hearing_B.md` gives
speech a write) is accepted as a plan and fails as a present N-line.

### 1.2 Cut the Proposition from `argue` — FREE

`p5_argue.py` (b). The same seeded act id argued on three Propositions (the arguer's own; one about
deposing the King; **the hearer's own contrary one**): the first moving draw is the same draw (i = 4) and
leaves the hearer at the same pursuits (`wealth` 1.0 → 0.9, `honour` 0.2 → 0.28) in all three. The
Proposition is an eligibility token. In the realm (seed 1, seasons 2–3) every argued Proposition read
`(OUGHT, <a person, a settlement or a record id>, predicate '', value None)`: there is nothing in it to
read. False N-line: *"an argument is about something"*.

### 1.3 Cut the draw from `determine` — NOT free, but what dies is a delay

`p3_hearing_ends.py` (a). `k` determinations of one matter in one fold, shipped pool 2 against Ob 2,
200 forks per `k`:

| k | party bound | 1 − 0.74^k |
|---|---|---|
| 1 | 0.26 | 0.26 |
| 2 | 0.48 | 0.45 |
| 4 | 0.70 | 0.70 |
| 8 | 0.90 | 0.91 |
| 16 | 0.99 | 0.99 |

A Failure writes nothing (`matter.undetermined`; tenures and docket unchanged, run (b)), so the same
judge asks again with a fresh draw. Cutting the draw would remove the wait and the band on
`Tenure.degree` (one reader, which filters to `commit` edges: F-SC-05 (c)). Under the standing rule the
draw is not to be cut; the finding is that it is not yet a *decision*: nothing a draw can do here is
final for the accused except conviction. `05_SC_acquittal.md` (SC-P6, as amended by G-55) makes Failure
terminal; this run is its falsifier's "before" reading.

### 1.4 Cut `docket_lapse` — not free; it is the only ending most matters have

`p3_hearing_ends.py` (c). A matter nobody touches: docketed at tick 1, `matter.lapsed` at tick 6, the
item removed; the persons standing at the party's place hold `(party, matter.lapsed)` firsthand and the
judge, in another rung, holds nothing of it. Then `open_case` on the same party in the same fold:
`case.opened`, a second case file, the clock restarted. `carry` of the same petition after a lapse:
`petition.carried`. So the lapse is the docket's garbage collector, and nothing it collects stays
collected. N-line narrowed: *"a hearing ends"* holds from one direction (the docket's size) and from no
other (the accused, the accuser, the bench, the record).

### 1.5 The draw, on the five properties (evidence for the cut tests above)

`n1_favour_two_ladders.py`; exact odds through `modules/social_contest/roll.py::obstacle` and
`sigma_leverage.record_odds`.

- **P-ii (uniform leverage) and S (*calculations consistent in methodology*): what the speaker brings
  rides two ladders.** `effort` enters as named levels through `advantage_sources` →
  `levels_to_net_sigma` → `net_boost`, a μ-shift; `proofs` and a favourable `reception` enter as a
  subtraction from the obstacle, clamped at `OB_MIN` and clipped by the ceiling
  (`roll.py:142-143`). The second is the form `ED-884` retired (*"the engine applied advantage as an Ob
  reduction … violating canon P-232"*, ledger row read), kept alive by a clamp; `rosters.yaml:
  advantage_sources`' own note says a later source — *"a held finding"* among its examples — is *"never
  an Ob reduction"*. Measured consequence, pool 2:

  | proofs held (firsthand, unmirrored) | 0 | 1 | 2 | 4 | 8 |
  |---|---|---|---|---|---|
  | as shipped, nobody opposes — P(Failure) | 0.74 | 0.66 | 0.58 | 0.42 | 0.42 |
  | as shipped, hostile bench or opponent's score 8 | 0.90 | 0.90 | 0.90 | **0.90** | 0.74 |
  | as named levels (`minor` each), nobody opposes | 0.74 | 0.65 | 0.57 | 0.42 | 0.27 |
  | as named levels, hostile bench or score 8 | 0.90 | 0.85 | 0.80 | 0.69 | 0.54 |

  The shipped form has a dead zone (four proofs before a hostile bench: nothing) followed by a cliff, and
  saturates at the floor; the levelled form reproduces the shipped numbers where the shipped form is not
  clipped (0.74 / 0.66 / 0.58 / 0.42 against 0.74 / 0.65 / 0.57 / 0.42) and is monotone everywhere else.
  Control: `effort` 0 / 1 / 2 before the same hostile bench gives 0.90 / 0.80 / 0.69. **So pressing
  harder twice beats four firsthand proofs (0.69 against 0.90).** `05_SC_obstacle_difficulty_and_modifiers_B.md`
  moves the favourable half after the ceiling (fixing the clip) and keeps it an Ob subtraction floored at
  `OB_MIN` (keeping the saturation, and the second ladder). Proposal A; §5 item 1.
- **P-iv (graded, recoverable):** the four bands exist on every contested row; on four of seven they
  select only the Event's name (`tell`, `lie`, `speak`, `interrogate` write `[]` in every band), and a
  fifth, `arrest`, never executes. Graded in form, binary or nil in effect.
- **P-i (legible odds):** holds. `sigma.odds_of` returns the dealt odds for the true input and matched
  the empirical bands in every cell run here.
- **P-iii, P-v:** no finding beyond `13_SC_contest_interrogation.md` §4 (saturation at the cap, cited).

### 1.6 The other direction: mechanisms attacked for the first time that held

- **The seam's per-act draw** (`n2_cuts.py` (ii)): twelve speeches folded forward, reversed, and with
  five other contested acts interleaved give each act the same band; replay is identical. Steelman 1 of
  the SC audit survives a new attack.
- **Firsthand over hearsay** (`p2b_lie_extremes.py` (1)): a knowing hearer keeps the truth in the weighed
  reader when the liar is a teller he regards at +25 and has found right eight times (the told claim's
  weight reaches 1.0, a tie with firsthand, and the firsthand claim still wins on confidence). The
  attack failed; the defence is real — and §2.2 shows it defends one reader of two.
- **`odds_of` against the fold**: the exact odds matched the empirical shares within sampling error in
  every table below.

### 1.7 NERS readings (E last, as a ratio)

- **N.** From all six directions the social contest is necessary to one thing today: `argue` at Success
  moves a hearer's pursuits. `determine` is necessary to the docket's turnover and to one edge with one
  reader. `speak`, `tell`'s contest, `lie`, `interrogate`, the room and the arrangement rows fail the cut
  top-down (no ending depends on them), bottom-up (nothing reads their bands), laterally (no sibling
  subsystem consumes them: GAME audit §1.2's SC row), and vertically (no scale transition).
- **R.** The no-player half: contests do fire with nobody watching (SC audit §1). Completeness fails at
  the extremes: a bench of one that is the party (refused, then lapse); a matter that is a place (never
  determinable); a hearer with no pursuits (a Success is emitted as `argument.refused`); an arguer with
  no pursuits (a win pulls the hearer's values toward nothing: `wealth` 1.0 → 0.9, `honour` 0.2 → 0.18).
  Customisation: a master and a novice have one distribution on `lie`, `arrest`, `determine` and
  `interrogate` (13_SC §1.2, re-run for `lie` in §2.2).
- **S.** Three "two ladders for one quantity" defects: advantage (§1.5); belief (two readers of one
  ledger, §2.2); falsehood and noise (a lie and a Partial garble are one rule, §2.2). *Pauses correctly*:
  nothing pauses; `host` is accepted and unused (F-SC-07, cited).
- **E, as a ratio.** The apparatus is large (the room, nine arrangement rows of thirteen keys, the
  docket, six band-keyed rows, two ledger readers, a record, a refraction) and what a player can intuit
  from a choice is: *more dice in `argue` or `copying` helps, effort helps, nothing else does*. Overhead
  high, legibility of consequence near nil; the ratio is poor and improves only by giving the bands
  readers, not by removing the draw.

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the five sentences are the orchestrator's; the
boundary is the social-contest provider, its seam, and the proceedings verbs). **Contamination
declared:** the ordinary account O below was written after reading the SC lane's audits (which
describe the code) and `modules/social_contest/roll.py`, and before opening the seam, the effects, the
queries or the verb rows. No blind predictor was available to this lane (no `Agent` tool). O is
therefore written strictly from the words of each sentence; where a prediction leans on what a prior
audit said, the run decides, not the reading.

### 2.0 The ordinary account (O), written before the code was opened

**P1 — "A petitioner with a good case before a friendly bench usually wins."**

| # | link | O: what a player expects (a run could contradict it) |
|---|---|---|
| P1.1 | a petitioner petitions | anyone with a grievance may; the petition names what is asked and of whom; a trace exists |
| P1.2 | the petition comes before a bench | within about a season it is heard by a definite set of sitters; a petition nobody hears is visibly unheard |
| P1.3 | "a good case" | quality is a property of what the petitioner holds and cites (proofs, witnesses, the truth of the matter); ordered: more and better support, better odds; no support is worse than some |
| P1.4 | "a friendly bench" | the sitters' regard for the petitioner moves his odds; ordered: friendly > neutral > hostile; each sitter counts |
| P1.5 | "usually" | P(win) with a good case and a friendly bench is well above one half and below one; the 2×2 is ordered: good+friendly > good+hostile, bad+friendly > bad+hostile |
| P1.6 | "wins" | what he asked for is granted and the grant changes something he can point to; losing is a visible dismissal, not silence |
| P1.7 | bounds | a bench of one; no bench (no hearing, and he can tell); the petitioner sitting on his own bench is refused or recused |

**P2 — "A lie is caught more often by someone who knows the truth."**

| # | link | O |
|---|---|---|
| P2.1 | a liar says a falsehood to a hearer | the liar holds otherwise than he says; one act, with author, hearer and content |
| P2.2 | the hearer believes or catches it | two visibly different outcomes; a draw decides |
| P2.3 | "someone who knows the truth" | a hearer who holds the contradicting fact firsthand catches the lie materially more often than one who holds nothing; ordered: firsthand > hearsay > nothing |
| P2.4 | caught | the hearer does not take up the falsehood, knows he was lied to, thinks less of the liar, and can say so to others |
| P2.5 | not caught | the hearer now holds the falsehood and can act on it or pass it on |
| P2.6 | "more often" | never always, never never: a knowing hearer is sometimes fooled (he doubts himself), an ignorant one sometimes suspicious |
| P2.7 | neighbours and bounds | a skilled liar is caught less than a clumsy one; telling the truth to one who knows it is not "caught"; a lie about the hearer himself is the knowing case |

**P3 — "A hearing ends."**

| # | link | O |
|---|---|---|
| P3.1 | a hearing begins | a matter is put before sitters at a time and place |
| P3.2 | it is heard | the parties (or their advocates) speak, and what is said is part of the hearing |
| P3.3 | it is decided | the bench reaches a decision in bounded time: a season or two, not indefinitely |
| P3.4 | it ends | one of several named terminal states (granted, dismissed, convicted, acquitted); each is visible and distinguishable; ended-by-lapse is not the same word as ended-by-verdict |
| P3.5 | it stays ended | the same matter is not asked again of the same bench without something new (an appeal, new evidence) |
| P3.6 | bounds | the accused dies or leaves; the judge dies; no quorum; a hundred matters on one docket; each is an ending or a visible suspension, never a silent forever |

**P4 — "A verdict changes standing."**

| # | link | O |
|---|---|---|
| P4.1 | a verdict exists, about a person | it names who, by whom, on what matter, how firmly |
| P4.2 | "standing" | the person's position among others: what he may do (bound, detained, banned, owing), how he is regarded, what he holds |
| P4.3 | changes — against him | a conviction lowers it: a restriction others enforce or regard others hold |
| P4.4 | changes — for him | an acquittal clears him, and costs the accuser something |
| P4.5 | others learn and act on it | people who hear of the verdict treat him differently in at least one act they then take |
| P4.6 | proportion | a firmer verdict changes more than a narrow one |
| P4.7 | reversal | a pardon, a release or an appeal undoes it, visibly |

**P5 — "An NPC argues against an NPC and one of them is moved."**

| # | link | O |
|---|---|---|
| P5.1 | two NPCs who differ on something are together | the argument has a subject they hold differently |
| P5.2 | one argues, with no player | the decision layer offers it and someone takes it |
| P5.3 | the other resists | with his own skill and his own commitment to his position; a zealot is harder than a waverer |
| P5.4 | "one of them is moved" | either the hearer (the arguer prevails) or the arguer (he is answered and gives ground): in every decided argument somebody's position changes, and it is recorded whose and to what |
| P5.5 | being moved matters | the moved person later does something he would not otherwise have done |
| P5.6 | the reason is readable | the record says on what ground he was moved |
| P5.7 | bounds | arguing the same point again and again does not grind anyone down for free; arguing with oneself is refused |

The notes' account (N) is not rebuilt here: the SC lane's audit §1 and §5 and 13_SC §1 are that account,
read in aggregate, and are cited per link. Verdict words are the skill's (FOLLOWS, DEPARTS, INVERTED,
INERT, ASSERTED, UNREACHED, AMBIGUOUS); depth is EXECUTES unless a row says FORMS or FIRES.

### 2.1 P1 — the petitioner. *Holds to "comes before a bench", then breaks at "a good case" and never recovers.*

`p1_petitioner.py 150`. The speaker petitions about the party, addressed to the Duke; carries it;
speaks; the Duke determines. Bench: the Duke, given one pursuit so that he judges at all. *Friendly* /
*hostile*: three firsthand deed claims about the speaker of the kind the Duke leans on hardest, each way.
*Good case*: four firsthand deed claims about the party that the party does not mirror.

| bench / case | reception | proofs | `speak` Ob | `speak` odds F / P / S / O | `determine` Ob | `determine` odds | determined, 150 seeded acts |
|---|---|---|---|---|---|---|---|
| hostile / none | −4.02 | 0 | 2.842 | 0.90 / 0.08 / 0.02 / 0.00 | 2.0 | 0.74 / 0.19 / 0.07 / 0.00 | 45 (33 Partial, 12 Success) |
| hostile / good | −4.02 | 4 | 2.842 | 0.90 / 0.08 / 0.02 / 0.00 | 2.0 | the same | the same 45 |
| neutral / none | 0 | 0 | 2.0 | 0.74 / 0.19 / 0.07 / 0.00 | 2.0 | the same | the same 45 |
| neutral / good | 0 | 4 | 1.0 | 0.42 / 0.32 / 0.25 / 0.01 | 2.0 | the same | the same 45 |
| friendly / none | +2.79 | 0 | 1.0 | 0.42 / 0.32 / 0.25 / 0.01 | 2.0 | the same | the same 45 |
| friendly / good | +2.79 | 4 | 1.0 | 0.42 / 0.32 / 0.25 / 0.01 | 2.0 | the same | the same 45 |

Control: the neutral / none cell at `pool_default` 30 deals `determine` 0.01 / 0.01 / 0.03 / 0.96; the
instrument sees a verdict move when something that reaches it moves.

| # | link | O | C (run) | verdict · cause |
|---|---|---|---|---|
| P1.1 | petitions | anyone, with a trace | `petition.filed`, a Record `{terms, to, from}` | FOLLOWS |
| P1.2 | comes before a bench | heard within a season | `carry` dockets it; the bench is whoever holds a `determine` remit over the party's place | FOLLOWS at EXECUTES. FIRES: `speak` refused 23 of 25, SC audit §1 |
| P1.3 | a good case | ordered: more support, better odds | four proofs: 0.74 → 0.42 before a neutral bench; **0.90 → 0.90 before a hostile one**; 0.42 → 0.42 before a friendly one. Reaches `speak` only | DEPARTS · EDGE (ceiling, floor) and COMPOSITION (the wrong roll) |
| P1.4 | a friendly bench | ordered | hostile 0.90, neutral 0.74, friendly 0.42 on `speak`: ordered. On the verdict: nothing | FOLLOWS for the speech; INERT for the verdict |
| P1.5 | usually | 2×2 ordered, best cell well above one half | best cell: the *speech* fails 0.42; the *verdict* binds 0.26 in every cell | DEPARTS · BEHAVIOUR |
| P1.6 | wins | what he asked for is granted | the party owes an `oblige` to **the judge's seat** (term 4 ticks) and joins its establishment; the petitioner's holdings are unchanged; the petition Record keeps its stages; the docket keeps a husk `{matter: None, petition: rec}` | DEPARTS · COMPOSITION |
| P1.7 | bounds | no bench is visible; own bench refused | a petition naming the judge, addressed to the judge, is filed, carried and docketed; he cannot determine it; it lapses. A petition about a *place* is docketed, can be spoken to (a `speak` rolls), and `determine` refuses it on `exists:Person = 0` | DEPARTS · EDGE |

Play-back: *A clerk petitions the Duke against his neighbour, brings four things he saw the neighbour do,
and speaks before a Duke who thinks well of him. None of that reaches the Duke's decision, which fails
three times in four whoever asks. When it succeeds the neighbour is sworn to the Duke's household for a
year, and may walk out of that service the same day; the clerk has his petition back.*

Three sentences in that paragraph are surprises the premise did not warn of: only an accusation can be
granted; the grant is the judge's; the convict can discharge it.

### 2.2 P2 — the lie. *Does not hold; two links are INVERTED.*

`p2_lie.py 60`, `p2b_lie_extremes.py`, `p2c_two_readers.py`. The liar holds `(Hh, stores:grain) = 8`
firsthand. Hearers: KNOWS (holds 8 firsthand), HEARSAY (holds 8 told by a third person), NOTHING. Each
trial is one real season: the offered candidate, the shipped roll, WITNESS. Control verb: `tell`.

**The roll.** Exact odds (`sigma.odds_of`), liar or teller against the knowing hearer:

| who holds what | `lie` F / P / S / O | `tell` F / P / S / O |
|---|---|---|
| nobody holds a score | 0.74 / 0.19 / 0.07 / 0.00 | 0.74 / 0.19 / 0.07 / 0.00 |
| the speaker holds `copying` 8 | **0.74** / 0.19 / 0.07 / 0.00 | 0.23 / 0.16 / 0.34 / 0.28 |
| the hearer holds `copying` 8 | **0.74** / 0.19 / 0.07 / 0.00 | 0.90 / 0.08 / 0.02 / 0.00 |
| the hearer holds Attunement 7 | 0.74 / 0.19 / 0.07 / 0.00 | the same |

The hearer's knowledge is not an operand at all: over 400 seeded acts per hearer through the fold
(`p2e_roll_check.py`) a lie fails 0.745 against the knower and 0.740 against the hearer who holds
nothing; exact 0.74 for both. (The 60-season cells below read 47 and 54 Failures; that is sampling,
which the 400-act check was run to settle.) 13_SC §4 cell 1 reports that `lie` cannot be opposed; what the rows above add is the
comparison: a practised speaker is three times as likely to be heard *when he tells the truth* and no
likelier when he lies, and a practised listener is harder to tell the truth to (0.90) than to lie to
(0.74). INVERTED on P2.7's "a skilled liar is caught less".

**What lands, and what the hearer then holds** (landed tellings only; tick 0, so every claim is equally old):

| hearer | verb | landed | weighed belief wrong | told-copy values seen | `record(hearer, speaker)` after |
|---|---|---|---|---|---|
| KNOWS | lie (said 12) | 13 | 0 | 7, 9, 10, 11, 12, 13, 16 | 0.5 ×12, 1.0 ×1 |
| KNOWS | tell (said 8) | 16 | 0 | 5, 6, 7, 9, 10, 11, 12 | **0.5 ×13**, 1.0 ×3 |
| NOTHING | lie | 6 | 6 | 7, 9, 13, 16 | 1.0 |
| NOTHING | tell | 16 | **14** | 4, 5, 6, 8, 9, 11, 12 | 1.0 |

- *Belief is not drawn.* A hearer who holds the cell firsthand keeps it 29 of 29; one who holds nothing
  takes whatever landed 22 of 22. P2.6 (*never always, never never*) fails in both directions. The
  standing rule's line (a thing that could go either way) is crossed: whether a man who saw the granary
  is shaken by a confident lie is exactly such a thing.
- *An honest teller cannot be told from a liar.* At Partial — 0.73 of all landings at the default pair
  (`band_odds(2, 2.0)`: 0.19 of 0.26) — the hearer's copy is garbled by `person_q.drifted`, the same
  function, at the same band (`told_drift_band` 0.5), that makes the liar's number
  (`test_cr27_lie.py::test_the_liars_number_and_the_channels_lossy_copy_are_one_rule` pins this as
  intended). So a knower's `record` of an honest teller falls to 0.5 in 13 of 16 landings, and of a liar
  in 12 of 13. And the honest teller can never *gain* with a knower: a clean (Success) telling of what
  the hearer already holds is suppressed by the exact-triple guard (`loop/witness.py:958`), so it forms
  no agreeing pair. To a hearer who knows, an honest man's record only falls.
- *To a hearer who knows nothing, telling the truth leaves him wrong 14 times in 16.* The channel's
  garble is larger in effect than the lie: a truthful Partial hands over 4 to 12 for a true 8.
- *"Caught" has no owner.* No Event kind, claim or regard term says a lie was told or detected
  (`test_cr27_lie.py` asserts there is no `lie.*` kind). A failed lie (`news.untold`) leaves every person
  present holding `(Hh, news.untold, True)`; `record` 1.00 and regard 0.0 for all (`p2b` (2)). The hearer's
  regard for a detected liar is unchanged in every cell (0.0 → 0.0); only `record` moves, and `record`
  is read by one function (`teller_weight`).

**One season later: two readers of one ledger** (`p2c_two_readers.py`; the hearer's firsthand claim is
one tick older than the telling):

| hearer | verb | landed | weighed reader holds the truth | plain reader holds the truth |
|---|---|---|---|---|
| KNOWS | lie | 32 | 32 | **1** |
| KNOWS | tell | 27 | 27 | **4** |
| HEARSAY | lie | 31 | 3 | 3 |
| HEARSAY | tell | 30 | 6 | 6 |

`LedgerReader` with a `weigh` ranks by support, then recency; without one, by recency alone
(`es/queries/person_q.py:1057-1081`). The weighed reader has one caller, `epistemic.belief_contradicts`
(`es/epistemic.py:133`: *may I form this act*). The plain reader is what a person **says**
(`person_q.said_of`, `:1195`), what his **sheet shows** (`decision/sheet.py::chronicle`, `:199`),
and whether he thinks a goal's **stage is passed** (`world_q.py:2936`, whose own docstring marks the
missing `weigh` `[ASSUMPTION … B3.1]`). So an eyewitness who is lied to a season later is not stopped
from acting on the truth, and reports, displays and plans on the lie. FIRES: seed 1, season 3,
`cohort_set_s_035` lied to `p_npc_052` about its grain (said 113, holds 40): afterwards the hearer's
weighed belief is 40 and his plain belief 113 (`realm_s1_k4.txt`, season 3, section A).

| # | link | O | C (run) | verdict · cause |
|---|---|---|---|---|
| P2.1 | a liar says a falsehood | one act with a content | FOLLOWS; the false value is one whole drift step from the truth (8 → 12) | FOLLOWS |
| P2.2 | believed or caught | two outcomes, drawn | three outcomes: nothing heard (0.74), heard garbled (0.19), heard as said (0.07); none is "caught" | DEPARTS · WORD (`news.untold` is not a catch) |
| P2.3 | a knower catches it more often | ordered by knowledge | the roll: identical. The belief: never fooled (weighed) and nearly always fooled (plain), at once | **INVERTED · COMPOSITION** (two readers) |
| P2.4 | caught | the hearer knows, thinks less, can say so | `record` 0.5; regard unchanged; nothing sayable; the honest are marked at 13 of 16 | DEPARTS · BEHAVIOUR |
| P2.5 | not caught | the hearer holds the falsehood | FOLLOWS for a hearer who holds nothing (6 of 6) | FOLLOWS |
| P2.6 | more often, not always | a draw | fixed by whether the cell is held firsthand | DEPARTS · the standing rule |
| P2.7 | a skilled liar; a truth is not "caught" | skill helps the liar; truth is safe | skill unread for `lie`; truth to an expert fails 0.90; truth garbled marks the teller | **INVERTED** |

Attack that failed (the steelman holds): no combination of regard (+25) and record (eight confirmations)
makes the weighed reader prefer the lie to a firsthand claim (`p2b` (1): the told claim's weight reaches
1.0 and the firsthand claim still wins).

### 2.3 P3 — the hearing. *Begins and is heard; "is decided", "ends" and "stays ended" do not hold.*

`p3_hearing_ends.py`.

| # | link | O | C (run) | verdict · cause |
|---|---|---|---|---|
| P3.1 | begins | a matter before sitters | `open_case` or `carry`; a case file; a docket item | FOLLOWS |
| P3.2 | is heard | what is said is part of it | `speak` rolls and writes nothing; three speeches leave no state and no claim in the bench (§1.1) | INERT |
| P3.3 | is decided in bounded time | a season or two | per asking 0.26; a persistent bench binds 0.90 by the eighth asking, in one fold if it likes; FIRES: about one asking a season realm-wide (SC audit §1) | DEPARTS · BEHAVIOUR |
| P3.4 | ends, in one of several named states | granted, dismissed, convicted, acquitted | one state by act (bound), one by clock (`matter.lapsed`). No dismissal: Failure leaves the docket and every tenure unchanged | DEPARTS (known: H-162 (c); SC-P6) |
| P3.5 | stays ended | not asked again without something new | after a lapse `open_case` succeeds at once (a second case file) and the same petition is carried again; after a Failure the judge asks again | DEPARTS · BEHAVIOUR |
| P3.6 | bounds | each an ending or a visible suspension | the party walks out of the duchy (three `travel.moved`): `determine.refused` on `bench:off_duke = False`, then lapse. The judge is the party: `case.opened`, `determine.refused`, lapse. A matter that is a place: lapse | DEPARTS · EDGE |

A failed determination, through a real season (run (b)): tenures unchanged, docket unchanged, and every
person alive, the King in another rung included, gains `(party, matter.undetermined)`; regard for the
party unchanged (the kind's valence is authored 0). Compare §2.4: a *successful* one names the judge only.

Play-back: *The Duke opens a case against a clerk. Nobody says anything that matters. Each time the Duke
turns to it he probably fails to decide, and may turn to it again at once. If he never does, the case
evaporates after five seasons and he may open it again that day. The clerk's one sure way out is to
leave the duchy.* The last sentence is a story the premise did not promise and the engine does produce
(§4).

### 2.4 P4 — the verdict. *The verdict exists and restricts; "standing", "others learn" and "for him" do not hold; one link is INVERTED.*

`p4_verdict.py`. Two real seasons (open, then determine) with WITNESS, the judge forced strong so the
verdict lands (Overwhelming in all three arms), against a control in which the case is opened and never
determined. Every person given the same two pursuits so that every person judges deeds.

| what | control | verdict (`oblige`, the computed case) | verdict (`detain` row) | verdict (`ban` row) |
|---|---|---|---|---|
| disposal edge | none | `oblige` party → judge's seat, term to tick 5 | `detain`, no term | `ban`, no term |
| witnesses' new claims naming the **party** (4 persons, the convict included) | 0 | **0** | **0** | **0** |
| each witness's new claims naming the **judge** | 0 | three (`matter.determined`, `pursuit.moved`, `seen`), plus two on the edge's own id; all told (the public channel) | the same | the same |
| regard for the party, each witness | 0.0 | **0.0 → 0.0** | 0.0 → 0.0 | 0.0 → 0.0 |
| regard for the judge, each witness, **the convict included** | 0.0 | **0.0 → +0.18** | +0.18 | +0.18 |
| the party's `move` | moved | moved | **blocked** | moved |
| the party's `oblige` to that seat | taken | refused | taken | refused |
| the party's `release` of the edge | refused (none) | **`tenure.closed`** | refused | refused |
| the party offered `release` (FORMS, a question naming the seat) | — | yes | yes (and it will be refused) | yes (and it will be refused) |

| # | link | O | C (run) | verdict · cause |
|---|---|---|---|---|
| P4.1 | a verdict about a person | names who, by whom, how firmly | the edge carries party, seat and band; the Event's claims carry the judge and the edge's id (`world_q.py:5414-5422` says so of its own DOCKET arm) | DEPARTS · BEHAVIOUR |
| P4.2 | standing | what he may do, how he is regarded | what he may do: `detain` stops travel, `ban` and a live `oblige` stop a second oath to that seat. How he is regarded: untouched | half FOLLOWS |
| P4.3 | against him | lowers it | no person's regard for the convicted moves; no claim names him | INERT |
| P4.4 | for him | an acquittal clears him and costs the accuser | no acquittal exists; a failed determination publishes the accused's name to everyone and costs the accuser nothing | **INVERTED** (publicity) |
| P4.5 | others learn and act | treat him differently | they learn that the judge determined *something*; FIRES, seed 1 season 2: 254 `claim.deposited`, one `challenge.refused` and one `proposition.uttered` cite the verdict; 0 persons hold a claim of it naming the party | INERT |
| P4.6 | proportion | firmer, more | `Tenure.degree` has one reader, for `commit` edges (F-SC-05 (c), cited; not re-run) | INERT `[cited]` |
| P4.7 | reversal | pardon, release, appeal | an imposed `oblige` is closed by the convict's own `release`, free, the same season (C-1's ruled price, `effects_information.py:531-535`); `detain` / `ban` only by `pardon` | DEPARTS · DELIBERATE without a safeguard (§5 item 7) |

Why the judge gains regard: a `matter.determined` deed is attributed to its doer and valued by each
holder's own pursuits against the alignment of `determine` (+0.32 for a holder of `honour`). The sign
would differ for another temperament; the *subject* would not. The convict's regard for the man who
bound him moves exactly as a bystander's does.

### 2.5 P5 — the argument. *Forms and executes; "resists" reads one number; "one of them is moved" holds 0.07 of the time.*

`p5_argue.py 300`. Arguer `{honour: 1.0}`, hearer `{wealth: 1.0, honour: 0.2}`, shipped fixtures.

| outcome, 300 seeded arguments | share | who changed (pursuits, stance or conviction) |
|---|---|---|
| `argument.lost` @ Failure | 226 (0.75) | nobody |
| `argument.won` @ Partial | 54 (0.18) | **nobody** |
| `argument.won` + `pursuit.moved` @ Success | 20 (0.07) | the hearer: `wealth` 1.0 → 0.9, `honour` 0.2 → 0.28 |

Exact odds by what the hearer brings: baseline 0.74 / 0.19 / 0.07 / 0.00; a live `commit` to the contrary
Proposition, the same; pursuit weight ×5, the same; stance toward the arguer −25 or +25, the same.
Controls: the hearer holds `argue` 6 → 0.90 / 0.08 / 0.02 / 0.00; the arguer holds it → 0.33 / 0.20 /
0.33 / 0.14; both → 0.53 / 0.19 / 0.22 / 0.06.

Grinding, one fold, nothing else acting: 10 arguments → one move; 50 → `wealth` 0.656, `honour` 0.475;
**200 → `wealth` 0.185, `honour` 0.852**. The arguer's state is unchanged and the hearer's regard for
him is 0.00 → 0.00 throughout.

| # | link | O | C (run) | verdict · cause |
|---|---|---|---|---|
| P5.1 | they differ on something | a subject held differently | any uttered Proposition serves, the hearer's own included; the move is the same (§1.2) | DEPARTS · BEHAVIOUR |
| P5.2 | one argues, no player | forms and fires | FIRES (SC audit §1: 41 executed in six seasons at seed 0) | FOLLOWS |
| P5.3 | the other resists | skill and commitment | skill (`argue` / Presence) only | half FOLLOWS; commitment INERT |
| P5.4 | one of them is moved | in every decided argument, somebody | 0.07; never the arguer; `argument.won` at Partial moves nobody | DEPARTS · BEHAVIOUR and WORD |
| P5.5 | being moved matters | a later act differs | not run here `[UNVERIFIED]`: CHAR's reading is 2 of 83 persons' pursuits changed in three seasons (GAME audit §1.1) | — |
| P5.6 | the reason is readable | on what ground | the Event carries the band; the Proposition is an empty token in the realm (§1.2) | ASSERTED |
| P5.7 | bounds | no free grinding; self refused | self refused. Grinding is free and converts. A hearer with no pursuits, or one who already agrees: a Success is emitted as **`argument.refused` with degree Success** (13 and 19 of 200). An arguer with no pursuits who wins pulls the hearer toward nothing (`wealth` 1.0 → 0.9, `honour` 0.2 → 0.18) | DEPARTS · EDGE |

Play-back: *A man of honour argues a point with a man of money. Three times in four nothing happens;
one time in five he "wins" and nothing happens; one time in fourteen the other man becomes a tenth more
like him, whatever the point was, and however firmly the other held the opposite. If he says it two
hundred times the other man is his.*

FIRES (seed 1, four seasons, `realm_s1_k4.txt`): 27 arguments rolled, 21 lost, 6 "won" at Partial, 16
more refused because the hearer was elsewhere; **0 persons moved.** The SC lane's six-season log at the
same seed reads the same way (every `argument.won` is `@Partial`); at seed 0 it reads 3 moved of 41.

## 3. Emergent narrative — what stories the social contest can tell, and which it tells

Instruments: `realm_sc.py 1 4` (the populated realm, seed 1, four seasons, the shipped chooser, no
player; per-matter timelines, every landed telling with the hearer's two readings, every argument,
every verdict and what cites it) and `e1_reasons.py 1 1` (one season: for every proceedings act, the
kinds in its `causes[]` and what the actor holds about the person he acts on). One seed read in detail
is an instance; the cross-seed counts (seeds 0 and 1, six seasons each) are the SC lane's (`05_SC_audit.md`
§1) and agree in shape. Control for the instrument: it does see a verdict, a landed lie and a death when
they occur (two, four and one in this run).

### 3.1 The stories the code can produce at all (enumerated from the rows and effects, not the documents)

| story atom | beginning | escalation | reversal | cost | ending | a record a narrator could read |
|---|---|---|---|---|---|---|
| an accusation | `petition` + `carry`, or `open_case` | `speak` (no effect) | none: no acquittal, no counter-claim | none to the accuser | the accused bound (`oblige` / `detain` / `ban`), or the clock (`matter.lapsed`) | the judge's deed and an edge id; never the accused's name (§2.4) |
| a sentence served | `matter.determined` | — | self-`release` (oblige), `pardon` (detain, ban) | none to release | `tenure.closed`, or the term matures | `tenure.closed` on an edge id |
| flight | a docketed party walks out of the bench's ground | — | he may walk back | none | lapse | three `travel.moved`; nothing links them to the case |
| a persuasion | `argue` | repetition | none (the arguer never moves) | none | the hearer's pursuits drift toward the arguer's | `pursuit.moved`; not on what ground |
| a deception | `lie` | the hearer may pass on something (a deed claim, usually: `said_of` picks the newest) | a later sighting restores the truth in the weighed reader | none, if unheard or half-heard; `record` 0.5 with a hearer who knew | none | no kind says a lie was told |
| an arrest and questioning | `arrest` → `interrogate` | — | `pardon` | — | `confession.*` (four names, no write) | never fires (SC audit §1) |

Stories that **cannot** happen, each because no row, band or reader carries it: an acquittal; an appeal
or a reversal; a sentence proportioned to the offence or to the vote; a witness called or a document
entered and answered; a perjury exposed; a judge recused, bribed or challenged for bias; an accuser who
pays for a false charge; a petition for anything but a person's binding (relief, land, a pardon for
another, a levy lowered); a remedy that goes to the wronged party; a reputation made or ruined by a
trial; a split bench; a negotiation settled by anything but two unilateral acts; an argument about a
particular thing; a liar unmasked in public; a village that hides its grain (a numeric lie is always
upward, proposal E).

Stories that **can** happen and that nobody designed (the curious half): *flight* — a man docketed
before a bench leaves its ground and the case dies; *the mutual petition* — two persons each file
against the other in one season (`p_npc_089` and `p_npc_090`, season 3); *the court that tries its own*
— office-holders with the `determine` remit open cases on one another (`p_npc_004` on 037, 038 and 040;
`p_npc_038` on 041 and 034) and one of them tries to determine another's case and is refused; *the man
talked round* would exist with proposal D.

### 3.2 What the realm told, seed 1, four seasons

| | season 1 | 2 | 3 | 4 | total |
|---|---|---|---|---|---|
| petitions filed | 14 | 5 | 12 | 13 | 44 |
| petitions carried / carriage refused | 2 / 1 | 1 / 5 | 0 / 19 | 0 / 7 | **3 / 32** |
| cases opened / refused | 8 / 1 | 2 / 2 | 1 / 4 | 2 / 6 | 13 / 13 |
| speeches unheard (no docketed matter) | 9 | 15 | 10 | 5 | 39 |
| speeches heard: turned (Failure) / held / advanced (Success) | 5 / 0 / 0 | 4 / 0 / 1 | 3 / 0 / 1 | 2 / 0 / 2 | 14 / 0 / 4 |
| determinations: refused / undetermined / determined | 1 / 0 / 0 | 2 / 0 / 1 | 1 / 0 / 0 | 0 / 0 / 1 | 4 / 0 / **2** |
| `release.refused` / `pardon.refused` | 6 / 0 | 9 / 1 | 10 / 5 | 7 / 3 | 32 / 9 |
| tellings: refused (hearer elsewhere) / unheard / landed | 33 / 9 / 1 | 19 / 6 / 3 | 19 / 6 / 3 | 19 / 5 / 4 | 90 / 26 / 11 |
| …of the landed, deposited anything new in the hearer | 0 | 0 | 1 | 1 | **2** |
| lies: refused / unheard / landed | 10 / 3 / 0 | 19 / 3 / 1 | 10 / 2 / 1 | 26 / 5 / 2 | 65 / 13 / 4 |
| arguments: refused / lost / "won" at Partial / moved somebody | 0 / 0 / 0 / 0 | 1 / 8 / 3 / 0 | 6 / 6 / 2 / 0 | 9 / 7 / 1 / 0 | 16 / 21 / 6 / **0** |
| docket: items / with a matter / naming an arrangement | 10 / 10 / 0 | 16 / 12 / 0 | 21 / 13 / 0 | 25 / 14 / 0 | |

Read as stories:

- **Beginnings are plentiful and nearly all are the same beginning.** 44 petitions and 13 cases in
  four seasons. In every one of the 14 petitions of season 1 the person the petition is *about*
  (`terms`) is the person it is *addressed to* (`to`): the chooser forms `petition(subject = X, to = X)`.
  `carry` dockets `terms` as the matter, so a petition to a lord puts the lord on the docket as the
  accused. `p_npc_020` drew fourteen petitions in four seasons and was bound in season 4.
- **The reason for a prosecution is not readable.** Of the 24 petition and case acts of season 1
  (14 petitions, 10 `open_case`; `e1_reasons_s1.txt`): 11 of 14 petitions have no act among their
  causes (a standing question); the opener holds no deed claim at all about the person he proceeds
  against in 8 of 24; his regard for that person is zero or positive in 22 of 24 (`p_npc_089` petitions
  about a man he regards at +12.5). Two of the eight opened cases are a person opening a case on
  **himself** (`p_npc_020`, `p_npc_074`), and a third such attempt is refused (`p_npc_004`). One
  beginning does read as a reason: `p_npc_021` opens the case against `p_npc_004` with his own refused
  `covenant` among its causes.
- **Escalation is repetition.** `p_npc_033` speaks to `p_npc_020`'s matter in each of four seasons and
  fails each time. `p_npc_041` speaks to `p_npc_038`'s matter in seasons 2, 3 and 4 and *succeeds* each
  time (`matter.advanced`); the matter is where it was. `p_npc_075` carries one petition in season 1
  and is refused carrying it seven more times. `p_npc_032` tries to pardon `p_npc_020` three times in
  season 3 (refused: there is nothing to pardon) and sentences him in season 4.
- **Reversal: none observed, none possible.** No acquittal, no closed disposal, no answered speech.
- **Cost: none observed.** No accuser, speaker, arguer or liar lost anything he could point to. The one
  loss in the run is `p_npc_013`'s: he twice spoke to `p_npc_041`'s matter (seasons 2 and 3, both
  Failure) and in season 3 is the actor of a `tenure.closed` at degree `Felled` whose subject is
  `p_npc_041` (the GAME audit §1.1 identifies this person's death in a `capture` at this seed); the log
  does not link the hearing to the seizure `[UNVERIFIED causal link]`.
- **Endings.** Two verdicts in four seasons, both Partial, both an `oblige` to the judge's seat. In
  both, a new case against the same party is opened in the same season (`p_npc_004` by the judge who
  had just bound him; `p_npc_020` by himself). What cites the verdict: 254 and 251 `claim.deposited`,
  one `challenge.refused`, one `proposition.uttered`, three `tell.refused`. No person holds a claim of
  either verdict that names the convicted. Every other matter is waiting for the clock.
- **Retelling.** Of 11 tellings that landed, 9 told the hearer what he already held firsthand and
  deposited nothing; the two that carried news were a settlement's people saying that a date had come
  due. Of 4 lies that landed, three said that a place or a person "exists: 2" for a held 1 and one
  inflated a settlement's grain; in all three that deposited, the hearer's two readers now disagree
  (§2.2). A narrator reading the log can say *who filed against whom and that a judge determined
  something*; he cannot say who was convicted, of what, on what ground, or what it cost anyone.

**The shape of the tail.** Thirty-two persons were the matter of some proceedings act (classified from
the run's own timelines). By signature: petitioned and never carried, 13; docketed (opened or carried)
and never spoken to or decided, 10; spoken to and undecided, 2; determined, 2 (both re-opened at once);
named only in refused acts, 5. Within a signature no two differ in anything but the count of
repetitions. The SC lane's six-season logs add the only other ending: at season 6 eight
matters lapse at each seed. Across seeds and seasons it is one hearing: *filed; talked at; forgotten or,
rarely, bound to the judge.*

**What a player's choice would change.** `effort` on a speech (the only operand inside a contest,
F-SC-07) changes a band that is read by nothing. Choosing whom to petition changes who is docketed.
Choosing to walk away ends the case. Nothing else in this scope responds to a choice.

**Extremes.** No bench (the party outside every seat's ground): refused, then lapse. A bench of one
who is the party: opened, refused, lapse. One person alone: `argue` and `tell` to oneself are refused.
A hundred matters: not run `[UNVERIFIED]`; the docket's turnover at this seed is two determinations in
four seasons against sixteen docketed, so a hundred matters is the same story with a longer wait.

## 4. Findings, ranked worst first

Severity words are `AUDIT_BRIEF.md`'s. "Falsifier" is the run that would have shown the claim wrong, with
its control. Requirement ids are `dossiers/00_NINE.md`'s.

**F-PES-SC-01 · degrades narrative (R-07, R-08) · INVERTED · One ledger, two beliefs: an eyewitness
acts on the truth and says, shows and plans by the lie.** §2.2. `LedgerReader` with a `weigh` has one
caller (`epistemic.belief_contradicts`); without one it serves `said_of`, the sheet's `chronicle` and
the goal-stage reader. One season after a firsthand sighting, a landed lie leaves the weighed reader
true 32 of 32 and the plain reader true 1 of 32; an honest garbled telling, 27 of 27 against 4 of 27.
Each reader is wrong at its own extreme: the plain one believes whoever spoke last; the weighed one
keeps a nine-season-old sighting at confidence 5 against thirty independent tellers (`p2d`). Falsifier:
`p2c_two_readers.py` with equal columns — not observed; control: at tick 0 (equal ages) the readers
agree, 29 of 29. FIRES: three of three deposited lies at seed 1. Fix: proposal B.

**F-PES-SC-02 · degrades narrative (R-07, R-08, R-09) · INVERTED · An honest teller is marked a liar
almost as often as a liar is, and to a hearer who knows, his record can only fall.** §2.2. `record`
0.5 after 13 of 16 landed truths and 12 of 13 landed lies; the Partial garble and the lie are one
function at one band; a clean truth to a knower forms no agreeing pair. Falsifier: any landed truthful
telling with `record` < 1.0 — present, 13 of 16; control: a hearer who holds nothing keeps `record`
1.0 in 22 of 22. Fix: proposal E.

**F-PES-SC-03 · degrades narrative (R-01, R-02, R-07) · INVERTED · A verdict is remembered as
something the judge did; the convicted is named only when nothing was decided.** §2.4, §2.3. Zero
claims naming the party after a determination, in every witness and in all three disposal kinds;
regard for the convicted unmoved; regard for the judge up for everyone, the convict included; after a
failed determination every person alive holds the accused's name. Falsifier: one witness holding a
claim naming the party after a verdict — none, in three arms and in the realm's two verdicts; control:
the case opened and never determined deposits nothing. Fix: proposal C.

**F-PES-SC-04 · degrades narrative (R-06, R-09) · What the speaker brings rides two ladders, and the
one evidence rides is the form `ED-884` retired.** §1.5. Four firsthand proofs before a hostile bench
or a strong opponent: 0.90 → 0.90; two slots of effort: 0.90 → 0.69. Falsifier: a cell where a proof
leaves the odds unchanged — present in four of six premise cells; control: the same proofs as named
levels are monotone in every cell and reproduce the shipped numbers where the shipped form is
unclipped. Fix: proposal A.

**F-PES-SC-05 · blocks a requirement (R-02, R-05; touches R-09) · The verdict reads nothing of the
hearing.** §2.1. Six cells, one distribution, the same 45 of 150 seeded acts; control: the judge's
pool moves it. The SC lane states this from reading and from realm counts (F-SC-01, F-SC-05, F-SC-13);
this is its execution with controls. Fix: the proposals on file — `05_SC_obstacle_difficulty_and_modifiers_B.md`
(inputs to `determine`), `05_SC_evidence_and_rebuttal_B.md` with `19_LACUNA_admission_rides_the_citing_draw.md`
(what was said and entered), `05_SC_acquittal.md` (a losing band) — with proposal A's amendment to the
first. No new proposal here.

**F-PES-SC-06 · degrades narrative (R-06, R-07, R-09) · An argument moves somebody 0.07 of the time,
never the arguer; what is argued and how firmly the hearer holds the contrary are unread; repetition is
free and converts.** §2.5, §1.2. Falsifier: an argument at Failure or Partial after which anyone's
pursuits differ — none in 280; control: `argue` 6 on either side moves the odds. FIRES: 0 moved of 27
(seed 1, four seasons). Fix: proposal D; the Proposition's content is FA's and CORE's formation.

**F-PES-SC-07 · blocks a requirement (R-02, R-04) · A hearing ends by exhaustion only.** §2.3, §1.3,
§1.4. A bench may ask again at once (k = 8 binds 0.90); a lapsed matter is re-opened in the same fold
and the same petition re-carried; in the realm both verdicts were followed by a fresh case on the same
party in the same season. Known in part (H-162 (c), F-SC-05 (a)); the `k` curve, the lapse-and-reopen
loop and the realm's re-opened verdicts are new. Falsifier: an `open_case` refused because the matter
was lately decided or lapsed — not observed. Fix: `05_SC_acquittal.md` as amended by G-55 makes Failure
terminal; §5 item 4 adds the one clause it lacks.

**F-PES-SC-08 · degrades narrative (R-02, R-04) · The only petition that can be granted is an
accusation, the grant goes to the judge, and in computed play the accused is the person petitioned.**
§2.1, §3.2. A petition about a place is docketed, spoken to and undeterminable; a granted one binds the
party to the judge's seat; the petitioner holds nothing new; 14 of 14 computed petitions name their
addressee as their matter; two of eight opened cases are self-cases. Falsifier: a computed petition
with `terms` ≠ `to` — none in 14. Fix: §5 items 5 and 6 (formation is CORE's; the remedy is a Jordan
call).

**F-PES-SC-09 · degrades narrative · The room (reception, proofs, the mirror, route erosion) is
necessary to nothing that changes the world.** §1.1. Three speeches leave no state, no claim in the
bench and the same verdict odds; the four band kinds carry one valence. Falsifier: any state or regard
that differs between the arms — none. Fix: `05_SC_playable_hearing_B.md` (speech writes case-file
stages) with `19_LACUNA_admission_rides_the_citing_draw.md`; until one lands the machinery's N-line is
unearned.

**F-PES-SC-10 · degrades narrative (R-06, R-09) · The lie's roll reads neither party, is easier than an
honest telling to a practised listener, and its content is a fixed function.** §2.2. `lie` 0.74 for
every pair; `tell` to a hearer with `copying` 8 fails 0.90; a speaker with `copying` 8 is heard 0.77 of
the time honest and 0.26 lying; a numeric lie is always the held value plus half. 13_SC §4 cell 1 has
the missing opposition; the comparison with `tell` and the fixed direction are new. Fix:
`05_SC_capability_surface.md` and `05_SC_hearing_capabilities.md` (the rows, G-53); proposal E edit 2
(the direction). Residual, decided in §5 item 3: a cooperative telling should not be opposed by the
hearer's skill at the same vocation.

**F-PES-SC-11 · degrades narrative (R-01, R-07) · Proceedings begin without a readable reason.** §3.2.
11 of 14 petitions with no act among their causes; no held deed about the target in 8 of 24; regard
zero or positive in 22 of 24. Fix: not SC's. `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`
and CORE's formation own it; listed for them.

**F-PES-SC-12 · hygiene · Words that do not mean what they say.** `argument.won` at Partial (nobody
moved); `argument.refused` with degree Success (a won argument over an agreeing hearer); `matter.carried
/ advanced / held / turned` (four words, one meaning to every reader); `news.untold` for a failed lie;
`release` offered to a man under `detain` or `ban` (formed, then refused: 32 `release.refused` in four
seasons at seed 1 `[the 32 are not all this case: UNVERIFIED split]`). Fix: proposal D renames the
first; the rest ride the proposals that give those bands readers.

## 5. Resolutions decided, and what is Jordan's

Each chosen by the five-step ladder (`CLAUDE.md` §0), in order; the step is named.

| # | inconsistency, gap or unclear passage | decided resolution | ladder step | carried by |
|---|---|---|---|---|
| 1 | proofs and favour enter as an Ob reduction; `effort` as a μ-shift; SC-B keeps the reduction after the ceiling | what stands against the act is an obstacle term; what the actor brings is a named level | 1 (`ED-884`, `ED-934`; `advantage_sources`' law) | proposal A |
| 2 | two comparators for one person's belief; the weighed one ignores confidence | one comparator, every reader, weight × decayed confidence | 5, and 3 for the stage reader (its own revert line) | proposal B |
| 3 | `tell` is opposed by the hearer's own `copying` / Focus, so a practised listener is harder to inform (0.90) than to deceive (0.74) | a telling the hearer does not resist is unopposed: `tell`'s opposition is read only where the hearer holds a negative stance toward the teller; otherwise the task's difficulty stands alone. Until SC-B's `difficulty` column lands: `_opposition_of` returns `None` for `tell` | 5 (the word: a hearer's skill at reproduction is not resistance to being told) | a one-line amendment to `05_SC_obstacle_difficulty_and_modifiers_B.md`'s `opposition` row; no file of its own |
| 4 | after a lapse or (with SC-P6) a dismissal, the same matter is re-opened at once by the same bench | `open_case` and `carry` decline a matter whose case file or petition carries a `lapsed` or `dismissed` stage written within `docket_lapse` seasons, unless the act cites an item not on that file (`19_LACUNA_verdict_ladder_and_reversal.md`'s re-opening rule); MATTER writes the `lapsed` stage when it lapses an item | 4 (LACUNA's rule; `Record.stages` is the existing carrier) | an edit to `05_SC_acquittal.md` and to `loop/matter.py`'s lapse pass; listed for the SC lane |
| 5 | every computed petition names its addressee as its matter | formation: `petition`'s `to` is drawn from the seats whose bench sits over the subject's place (`judging_set`), never the subject | 5 | CORE (`decision/options.py` operand formation); listed |
| 6 | a judge may open a case on himself and can never determine it | `open_case` declines `subject == actor` (the fold's `counterparty` clause already exists for rows naming a second party; the row gains `counterparty: subject`) | 4 (`petition`'s two-sided rule, `ED-IN-0210`) | a one-cell edit to `verb_table.yaml`'s `open_case` row; listed for the SC lane |
| 7 | a verdict's claims name the judge and an edge id | restraints and imposed edges are read as their two ends; the two kinds join the paired kinds | 4, 3 | proposal C |
| 8 | Failure and Partial of `argue` move nobody; Partial is called "won" | Failure moves the arguer; Partial is `argument.held` | 3 (H-221's stated intent), 4 | proposal D |
| 9 | the garble and the lie are one rule, so `record` cannot separate them | a hearer who knows hears true; a lie has two directions | 5 | proposal E |
| 10 | LACUNA's table says an `oblige` is released *"by the obligee"*; the code's releaser is the convicted party | the same person: `establishment_of` calls the bound party the obligee; no conflict, the word is confusing | 3 (the code) | none |

**For Jordan** (survived the ladder; two defensible options that make different games):

1. **Is a favourable modifier part of the obstacle?** The clarification of 2026-11-12 (*the obstacle is
   the task's difficulty plus all modifiers*, relayed, not ledgered) against `ED-884` / `ED-934`
   (advantage is never an Ob reduction). *Option A* (SC-B as written): evidence and favour make the
   task easier, floored at `OB_MIN`; a small pool's room has three states. *Option B* (proposal A):
   they make the speaker stronger, bounded by the soft cap; every proof counts at every pool. B is
   decided here at ladder step 1; it is listed because the newer statement is Jordan's own.
2. **May a convicted man discharge his own sentence?** C-1's ruled price (`effects_information.py:531-535`:
   *"a convict can discharge his own penance"*) is executed: one `release`, free, the same season.
   `detain` and `ban` are not self-releasable. *Option A* (as ruled): a sentence of service is a penance
   the convict may walk away from; trials bind only by custody or ban. *Option B*: an imposed `oblige`
   (`Tenure.imposed`) is closed by the bench (`pardon`) or its term, as its two siblings are. Not
   resolved here: it would overwrite a ruled item.
3. **Who is a verdict for?** Today the disposal is the party's obligation to the judge's seat. *Option
   A*: keep (the court is the injured party; the petitioner's satisfaction is not modelled). *Option
   B*: where the docket item names a petition, the disposal's object is the petitioner (or the seat he
   names), so winning a case is something a person can want. B changes what C-1 ruled about the edge's
   object (*"ON THE SEAT EXERCISED"*); not resolved here.

## 6. False N-lines, failed premises, stories — the lists

**False N-lines found** (a thing the design treats as necessary whose cut is free, executed):
(1) *the room reads you* — `speak`'s roll, reception, proofs, the mirror, route erosion (§1.1);
(2) *an argument is about something* — the Proposition operand of `argue` (§1.2);
(3) *the verdict is a draw that could go either way* — for a bench that persists it is a wait (§1.3);
(4) *a hearing ends* — true of the docket's length only (§1.4);
(5) *a record separates liars from honest tellers* — it measures the channel's noise (§2.2);
(6) *the band of a contest is data* — on four of seven contested social rows it selects only a name,
and a fifth never executes (§1.5).

**N-lines attacked that held:** the per-act draw (order, interleaving, replay); firsthand over hearsay
in the weighed reader; `odds_of` against the fold; `argue` at Success (cut it and no person's pursuits
are moved by another person at all).

**Premises that failed:** all five, at these links — P1.3 (a good case), P1.5 (usually), P1.6 (wins);
P2.3 and P2.7 (INVERTED), P2.4, P2.6; P3.3, P3.4, P3.5; P4.1, P4.3, P4.4 (INVERTED), P4.5; P5.1, P5.4.
**Links that follow:** P1.1, P1.2, P1.4 (for the speech), P2.1, P2.5, P3.1, P4.2 (the restriction),
P5.2, P5.3 (skill).

## 7. Evidence log

All under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_SC/`;
`PYTHONHASHSEED=0`; no tracked file written; no `pytest` run. `lib.py` is the shared fixture helper
(`probes.tiny_world`, world seed 1).

| # | command | what it is | outcome (where used) |
|---|---|---|---|
| 1 | `p1_petitioner.py 150` → `p1_petitioner.txt` | 3 benches × 2 cases; exact odds and 150 seeded acts per cell through the fold; control pool 30 | §2.1 |
| 2 | `p2_lie.py 60` → `p2_lie.txt` | lie and tell to three kinds of hearer, 60 real seasons per cell; exact odds by capability | §2.2 |
| 3 | `p2b_lie_extremes.py` → `.txt` | a loved, long-right liar against a knower; what a failed lie leaves | §2.2, §1.6 |
| 4 | `p2c_two_readers.py` → `.txt` | the same after one empty season; the two readers; the callers of each (grep) | §2.2, F-01 |
| 5 | `p2d_stale_sighting.py` → `.txt` | a stale sighting against n fresh tellers, direct reads | F-01, proposal B |
| 6 | `p3_hearing_ends.py` → `.txt` | k determinations in one fold (200 forks each); a failed determination through a season; the lapse; re-opening; bounds | §2.3, §1.3, §1.4 |
| 7 | `p4_verdict.py` → `.txt` | verdict against control, three disposal kinds, real seasons with WITNESS; what the party can do after | §2.4 |
| 8 | `p5_argue.py 300` → `.txt` | 300 seeded arguments; three Propositions; exact odds by what the hearer brings; grinding; bounds | §2.5, §1.2 |
| 9 | `n1_favour_two_ladders.py` → `.txt` | proofs as shipped and as named levels, exact | §1.5, proposal A |
| 10 | `n2_cuts.py` → `.txt` | the `speak` cut; the seam's per-act draw | §1.1, §1.6 |
| 11 | `d_projection.py` → `.txt` | proposal D's rule projected with the shipped `argued_pursuits` (not the engine) | proposal D |
| 12 | `realm_sc.py 1 4` → `realm_s1_k4.txt` | the populated realm, seed 1, four seasons (39, 93, 148, 233 s under load); content hash `25d23448…` | §3, FIRES rows |
| 13 | `e1_reasons.py 1 1` → `e1_reasons_s1.txt` | one realm season: causes and holdings behind each proceedings act; petition terms; proposition shapes | §3.2, §1.2 |
| 14 | `p2e_roll_check.py` → `.txt` | 400 seeded `lie` and `tell` acts per hearer through the fold, against the exact odds | §2.2 (the roll is one distribution) |

Not run: a second realm seed in detail (machine load 27 to 44 throughout; the SC lane's six-season logs
at seeds 0 and 1 are cited for the cross-seed shape); a realm before-and-after for any proposal (each
names it as its gate); `harness/storybar.py`, `chronicle.py`, `arc.py`, `strife.py` on this scope
`[SKIPPED: time; the per-matter timeline in run 12 was written instead]`; the kernel `K/` (not reached
by the loop; the SC addendum's §B3 stands). `[UNVERIFIED]` marks in the text are the complete list of
claims not checked by a run or an opened line.
