# Workplan v12 — questions for Jordan

## Status: WORK FILE (questions the v12 lanes leave to Jordan after the five checks; resolves nothing at runtime; deleted when v12 is adopted)

Same form as `unified/DECISIONS_FOR_JORDAN.md`: what the game does today, one question, the options and how
each plays, a recommendation, and what the plan assumes until you answer. Only questions that every
earlier check failed to settle are here: superseded, irrelevant, settled by a design document, settled by
precedent, settled by what the code clearly needs. Each was raised by a body-part author and passed through
the patch lane (`PATCH_LOG.md`, `H2_DECISIONS.md`). Questions those checks did settle are listed at the end.

---

### J-01 · A rung's population envelope: remove it from the architecture, or give it a reader · SE, Layer 1 · ANSWERED

**ANSWERED 2026-11-12 (Jordan: *"J-01 A"*; `unified/DECISIONS_ANSWERED.md` A-115).** Removed. Layer 1 node
`L1-A115` is applied (`ED-IN-0361`: `04` §B.3's `Rung` tuple and DELETED line, §A.2's `loop/census` row, §C.7,
F.19; pointers in `holonic_ARCHITECTURE.md`, `01_AXIOMS.md`, `ARCHITECTURE_V2.md`). B12b.18 is now a BUILD deletion
(`workplan_v12_part24.md`): the field, its write-matrix row, the probe that writes it, the tests that name it;
a hash MOVER(encoding), re-pinned at B12b.99. It left the head's held-back list. The text below is the
question as it was asked.

**The situation.** Every settlement rung (a town, a village and so on) carries a stored number, its
population envelope. It is written into the architecture's definition of a rung (`04` §B.3) and listed in
the census section, but nothing in the game reads it. Population growth and loss work through each
person's own weight, not through the envelope. Nothing in the suite gives the envelope a job.

**The question.** Drop the envelope from the architecture, or keep it and have a later design give it a
reader?

**Option A: remove it.** You amend `04` §B.3 and the census row in §A.2, and one commit deletes the field.
If the field is part of the world's fingerprint, the commit also re-pins once. Play does not change, since
nothing reads the field. The world carries one fewer number that looks meaningful and means nothing.
**Option B: keep it, and owe it a reader.** The field stays and the plan holds a "carrier owed" row for the
settlements lane. When that lane designs one, the envelope could cap growth or set the scale of a famine.
Until then it is a stored number that disagrees with the people actually living there.

**Recommendation.** A. The population rules already work through each person's weight, which is the one
owner. A second count of the same people is a second ladder for one quantity, and it drifts. If the
settlements lane later wants a cap, it can derive one from the persons, the way the census already does.

**What the plan assumes until you answer.** B: the field is kept, nothing edits it, and item B12b.18 is
BLOCKED and on the held-back list.

**Blocks.** B12b.18 (the half of H-171 it limits).

**Sources.** `workplan_v12_part24.md` B12b.18; `proposals/U5d_SE_owed_edits.md` §3 ("Owed to Jordan (Layer 1
text, not applied)"); `H2_NOTES.md` (A24).

---

### J-02 · How a lord learns what a town's granary holds, so that he can requisition it · SE, FA · ANSWERED

**ANSWERED 2026-11-12 (Jordan: *"J-02 A typically but B can be selected"*; `unified/DECISIONS_ANSWERED.md`
A-116).** A report up the chain is the typical rule; reach down the residence ladder can be selected per seat.
Built in Batch B12c (`workplan_v12_part28_cont.md`): B12c.30 the seat-row key `larder_reach: report | residence`
(default `report`) and its loader refusal; B12c.32 the offer aimed at the stock the lord was told of; B12c.33
the `residence` reach; B12c.34 the flip (CR-23's stock report every season, the believed read on), whose gate
is an issuing seat offered a larder in the built realm at seed 0, two seasons, against the 766-of-766 reading
as the control; B12c.35 a design item for the report as the seat-holder's own word (a shaded or withheld
report). B10.79 is a POINTER to them; B33.30 is HELD on B12c.34. Assumptions recorded (B12c's UNDECIDED (8)):
`[ASSUMPTION: "each lap" read as each season, the report riding MATTER, which runs once a season; a per-lap
report is the seat-holder's own act, B12c.35]`; `[ASSUMPTION: "the seat above" read as every seat whose
purview reaches the settlement, \`governors_of\`]`; `[ASSUMPTION: the key sits on the seat row, \`offices.yaml\`,
not an \`arrangements.yaml\` row]`; `[ASSUMPTION: no shipped seat is set to \`residence\`; which seats are is
authored content]`; all reversible. The text below is the question as it was asked.

**The situation.** A seat-holder may `requisition` stores, but in played seasons he never does. The query
that lists the larders he may draw on returned nothing in every call measured, 766 of 766: a settlement's
larder is not within reach of the seats that grant `issue`. So everything downstream (who complies, the
tax edict, the refill of a garrison's upkeep, unrest when a town is stripped) has been tested only on
hand-built worlds.

**The question.** What gives an issuing seat a claim on a settlement's larder: a report up the seat's
chain, or reach down the ladder of places he resides over?

**Option A: a report up the chain.** Each lap, the settlement's seat sends its stock to the seat above it as
news. A lord knows what a granary held when he was last told, and can be lied to or kept uninformed. The
requisition is aimed at what he believes is there. A town can hide grain, and a stale report can send men
to an empty store.
**Option B: reach down the residence ladder.** The lord's purview extends to the larders of the places
under the place he holds. He can requisition from any of them, and what he finds is what is there. It is
simpler, and the fiscal game becomes one of reach and consent, not one of information.

**Recommendation.** A. The rest of the game holds that people act on what they hold, not on the world
(imperfect knowledge is structural). A report is one more deposit on a channel the engine already has, and
the stale or false report is the drama an administrative game wants. B would make the granary the one
quantity a lord sees perfectly. If A proves too slow at two seasons, B's reach can be added later as the
admission rule, with A's report still shaping what he aims at.

**What the plan assumes until you answer.** Neither. B12c.30, B10.79 and B33.30 (the tax edict) stay
BLOCKED. `requisition` counts toward the requirement only through hand-built worlds, and B12c's close
quotes the computed count (0) as the standing reading.

**Blocks.** B12c.30, B10.79, B33.30. Also, through them, CP-T08-06's compliance reader, CP-T08-07's
collection and CP-T08-08's refill, which are credited on hand-built worlds only.

**Sources.** `workplan_v12_part28.md` B12c.30; `master/eval/E5.md` Block C12 (AM-E-21: "which lift to build
… is a design choice with different information games"); the intake `:326`; `H2_NOTES.md` (A28, A38).

---

### J-03 · Is giving something up a sure act, or a drawn one? · FA, SC (verb `release`)

(Raised by repair lane R2d as its J-1, from check lane K8's finding 4, `checks/R2d_APPLIED.md`; folded here by lane H3. It re-opens the `release` row of the "settled" table below: HD-27's move turned out not to be mechanical.)

**The situation.** A person can give up a holding of his own — step down from a seat (a king abdicating), end an oath, let a tie lapse — with one verb, `release`. Today it always succeeds when he chooses it, and no one opposes it. The plan's rule for every act that changes the world (from the task-draw proposal) puts each such act in one of three classes: a contest (someone opposes it), a task (drawn against how hard the job is), or bookkeeping (it only records, and may never touch a seat). `release` fits none cleanly: it can close a seat, which bookkeeping is forbidden to do, and nobody opposes it, so it is no contest. The plan parks it on a list of acts "owed a class", where it resolves as today.

**The question.** Should stepping down (and ending any holding of one's own) stay certain, or be drawn?

**Option A — certain (a bookkeeping act that may close one's own seat).** Abdication and oath-breaking happen exactly when chosen; the drama is in the choice and its consequences, never in failing to let go. Cost: the bookkeeping rule gains one exception (an act may close a seat *its own actor holds*), written at the loader.
**Option B — drawn (a task).** Letting go can go badly: a Partial abdication that leaves the seat contested, a Failure that leaves him bound. More texture, but a man can fail to resign, which reads oddly, and every `release` in the realm moves the seeded readings.
**Option C — leave it owed.** `release` stays on the "owed a class" list indefinitely and resolves as today; the three-class rule carries a standing exception.

**Recommendation.** A: it matches what the act is (ending one's own commitment), keeps the "no deterministic outcome" rule intact where there is an outcome to draw (the succession that follows is already drawn), and the exception is narrow and checkable.

**What the plan assumes until you answer.** C: `release` stays in `contest_owed`, resolved as today (B32.26 step 5 carries this as an `[ASSUMPTION]`).

**Blocks.** Nothing executes differently until answered; the close of the `contest_owed` roster (H2's HD-27) waits on it.

**Sources.** `workplan_v12_part34_cont.md` B32.26 step 5; `workplan_v12_part34.md` UNDECIDED (9); `H2_DECISIONS.md` HD-27; `workplan_v12_part2_cont2.md` §11 C-22; `workplan_v12_part10_cont2.md` B07.01 (the three classes and the bookkeeping refusal); `engine/season/verb_table.yaml:1335` (`release`); `checks/CHK_K8.md` finding 4; `checks/R2d_APPLIED.md` J-1.

---

### J-04 · Items longer than the plan's 6 KB cap: does the cap give way, or do the items split? · the plan's form (no game effect)

(Folded by lane H3 from the repair lanes' notes to the orchestrator: `checks/R2a_APPLIED.md` K2 #11, `R2b_APPLIED.md` K4 F11, `R2c_APPLIED.md` K5 F6 and K6 F7, `R2d_APPLIED.md` K7 F-17. One row for all of them.)

**The situation.** This changes nothing the game does; it is how the plan is written. The plan's work order budgets each item at about 4 KB and caps it at 6 KB (`V12_STRUCTURE_part4.md` E-12), and the same order says an item over the cap "copies only the exact edit text (files, symbols, schema, test body) and cites the rest", while `V12_STRUCTURE.md` §5.4 says an item carries the edit text a cold agent needs to execute it. The four repair lanes cut every quotation, rationale and history paragraph they found to a citation. What is left over the cap is edit text: **160 items over 6,144 bytes** (184 over 6,000; 40 over 8 KB), counted by script over every part (`sizes.py`, part 2 appendix): 35 in parts 3 to 11, 28 in 12 to 20, 26 in 21 to 28, 70 in 29 to 43, 1 in 44. The largest are B02.38 (25 KB: the requirement file's conjunct table, copied), B38.20 (13 KB), B35.10 (12 KB), B27.01 (11 KB). Two the lanes named: B16.09 (about 7.4 KB, the consult/view/chooser and the withdrawal, which its source says land as "one commit", U3 §1 item 16) and B21c.01 (about 7.2 KB, over by the 1.6 KB `ladders:` block of 66 names it copies).

**The question.** For an item whose text over 6 KB is all edit text, does the 6 KB cap give way to §5.4, or does the item split?

**Option A — the cap gives way.** An item carries its whole edit text however long; the cap stays a budget for prose, not for edit text. Nothing is renumbered; a producer reads a longer item; one commit stays one commit (B16.09).
**Option B — the items split.** Every item over 6 KB becomes two or more positions by a seam in its edit (for B16.09, consult/view/chooser apart from the withdrawal). Up to about 160 new positions (about +64 h by the plan's per-position estimate), new handles in the parts that cite the old ones, and some splits cut a change its source says lands whole.
**Option C — cut further.** Trim copied edit text to citations so each item fits. The producer then re-reads the sources the item was written to spare it, which is what §5.4 forbids.

**Recommendation.** A. The cap was set to stop prose sprawl, and the lanes' cuts did that; what remains is the text a commit applies. Splitting buys a size figure at the cost of handles, hours and, for B16.09, the one-commit rule its source sets.

**What the plan assumes until you answer.** A: the over-cap items stand as the repair lanes left them.

**Blocks.** Nothing; the plan executes either way.

**Sources.** `V12_STRUCTURE_part4.md` E-12; `V12_STRUCTURE.md` §5.4; `checks/R2a_APPLIED.md` (K2 #11), `R2b_APPLIED.md` (K4 F11), `R2c_APPLIED.md` (K5 F6, K6 F7), `R2d_APPLIED.md` (K7 F-17); `workplan_v12_part23.md` B16.09; `workplan_v12_part25.md` B21c.01; part 2 appendix `sizes.py`.

---

### J-05 · Set the repository to allow merge commits for v12's batch PRs · the plan's run (no game effect)

(Raised by repair lane V1 from the Fable verdict's defect 2, `V12_VERDICT.md`.)

**The situation.** Each v12 batch has its own branch and PR (`workplan_v12.md` §7 point 7). A later batch's gate on an earlier one is met only if the earlier batch's closing commit is an ancestor of the current head (§1's table, the gate row). The `methodology-execute` skill says GitHub squash-merges each batch's PR (its BATCH BOUNDARY item 2). A squash (or a rebase-and-merge) puts a new commit on `main` in place of the batch's own, so the next batch's gate reads unmet and the run stops at B01. Which merge methods the repository allows was not checked (no GitHub call was made).

**The question.** Will you set the repository to allow merge commits, so v12's batch PRs merge that way?

**Option A — allow merge commits.** Each batch PR merges by merge commit; its commits, the closing one included, land on `main` as they are; every gate reads as written. `main`'s history keeps each batch's item commits (one per item) rather than one squash.
**Option B — keep squash only.** Batches run one after another on one branch under the driver (`tools/methodology_drive.py`), merged to `main` at points you choose; the steps that open several batches at once (S4, S6, S8, S9, S12 to S19) lose their parallel sessions.
**Option C — keep squash and rewrite each gate at merge.** The coordinator rewrites `@<closing sha>` to the squash's SHA after each merge. One more edit per batch, and the gate no longer names the commit the close read.

**Recommendation.** A: it is the only option under which the plan runs as written, in parallel where §7 allows.

**What the plan assumes until you answer.** Merge commits where the repository allows them; otherwise the driver on one branch (`workplan_v12.md` §7 point 7, `[ASSUMPTION: merge setting of the repository — unverified]`; the difference from the skill, §2.1 (e)).

**Blocks.** Every parallel step's merges; nothing in B00 to B03, which run one at a time.

**Sources.** `workplan_v12.md` §1, §2.1 (e), §7 point 7; `.claude/skills/methodology-execute/SKILL.md`, BATCH OPEN item 3 and BATCH BOUNDARY item 2; `V12_VERDICT.md` defect 2.

---

### J-06 · Batches over about 60 positions are one close each: split them, or keep them whole? · the plan's form (no game effect)

(Raised by repair lane V1 from the Fable verdict's question 8; the plan's forms make a batch one close (RULED 2026-11-06, the skill), and the verdict's question is about size, not a defect, so nothing is re-cut here.)

**The situation.** Six batches hold about 60 positions or more, each one close (one review fan, one full suite, one re-pin): B98 (87 positions, 38 behaviour movers, 39.3 h), B10 (67, 10 movers, 29.3 h), B03 (65, 2 movers, 28.5 h), B38 (65, 13 movers, 28.5 h), B11 (58, 31 movers, 25.7 h), B21 (57, 35 movers, 25.3 h) (part 2's batch table). A larger close carries more risk of a red found late and is harder to resume.

**The question.** Keep each as one close, or split at its first forward cut?

**Option A — keep them whole.** One close each, as written.
**Option B — split on request, at the first forward cut.** A cut is valid where no row before it gates on a row after it. Verified for B10 only: B10.01 to B10.50 | B10.54 onward, after B10.51 to B10.53 land first (the first half's rows gate on nothing in the second half but those three, `workplan_v12_part12.md`'s position table; `V12_VERDICT.md` question 8). B98 can be cut at any position (each flip gates only on the previous flip's reading). The cuts for B03, B38, B11 and B21 are **unverified**.

**Recommendation.** A until a close of one of them runs long; then B for that batch, at its verified cut.

**What the plan assumes until you answer.** A: each is one close; no batch is re-cut.

**Blocks.** Nothing.

**Sources.** `workplan_v12_part2.md` (the batch table); `workplan_v12.md` §5 ("What shortens the path"); `V12_VERDICT.md` question 8.

---

### J-07 · Two Layer 1 rewordings with no amendment node: give each a node, or say the word · Layer 1

(Raised by repair lane V1 from the Fable verdict's question 7.)

**The situation.** Two items edit `architecture/meta/04_CODE_ARCHITECTURE.md` with no `L1-A*` node in `unified/U3_LAYER1_AMENDMENTS.md`. **B03.71** re-words the `succeed` designation nodes to the title route the code takes, on the assumption that your ruling RS-27 (*"the heir still has to claim their throne"*) owes that wording; CLAUDE.md §0.05 says a spec edited to match its implementation checks nothing, and A-97 says Layer 1 follows a ruling, never the code. **B41.03** step 4 adds a paragraph to §C.12 (a refusal and a defect as two typed shapes, GO-10). ED-IN-0300 lets an agent land unmarked architecture text openly in a PR; its ratified row names the positions whose holds it lifted (CR-29 among them, which covers B11.04's §C.6 row), and names neither A1-81 nor GO-10.

**The question.** For each: apply it as a Layer 1 amendment (a node, or your word in the PR), or leave `04` as it stands?

**Option A — amend.** B03.71 lands its re-wording and B41.03 its paragraph, each cited to your answer.
**Option B — leave.** `04` keeps its text; B03.71 is retired with a note; B41.03's code (the typed refusal) lands without the paragraph, so the code holds a rule Layer 1 does not state.

**Recommendation.** A for both: RS-27 does make the heir a claimant, and GO-10's shapes are what the port is built against; but each is a Layer 1 text, so it is yours.

**What the plan assumes until you answer.** Neither lands: B03.71 is HELD, and B41.03's step 4 is HELD while its steps 1 to 3 proceed (`workplan_v12_part5.md` B03.71; `workplan_v12_part29.md` B41.03).

**Blocks.** B03.71; B41.03 step 4.

**Sources.** `workplan_v12_part5.md` B03.71; `workplan_v12_part29.md` B41.03; `registers/editorial_ledger_in.jsonl` (ED-IN-0300, the superseding row); `workplan_v12_part2_cont2.md` (the Layer 1 table); `V12_VERDICT.md` question 7.

---

### J-08 · A-80's C8 thresholds: how much must a held world still move? · WR (the census), A-80

(Raised by repair lane E from the Stage E antagonist's finding 2, `checks/E_REPAIR.md`.)

**The situation.** Your ruling A-80 says entrenchment must still move the world. The plan checks it with clause C8 of the cascade census: a run in which every contested draw goes to the holder (the "entrenched" arm), set beside a free run at the same seeds. C8 now fails the batch (B38 does not close) when fewer than three of ten kinds of story (the six ways of turning to another means, blame, refugees or a riot, the side thinning, a petition's intensified stage) appear at two seeds or more of five, or when people in the entrenched run act less than half as often per season as in the free run. The two numbers, three of ten and a half, come from the proposal and were marked for you to correct; nothing measured sets them.

**The question.** Keep three of ten and a half, or set other values?

**Option A — keep them.** A held world must show at least three different kinds of response, and lose no more than half its activity. Loose enough that a two-season run can pass; a world where only one or two kinds of response ever appear fails.
**Option B — other values.** Tighter (say five of ten, or two thirds) asks more variety and activity of a held world and risks failing a two-season run on noise; looser lets a nearly still world pass.

**Recommendation.** A for v12's two-season gates, re-read at B99's long run, where a tighter value can be set against eight seasons of data.

**What the plan assumes until you answer.** A: three of ten and a half, each marked `[ASSUMPTION; Jordan to correct]` at the gate.

**Blocks.** Nothing; B38 closes or stops on these values.

**Sources.** `workplan_v12_part41.md` B38.71 (step 6, C8; GATE); `workplan_v12_part40.md` B38.13 GATE 3 (row 7, the related flagged rate "`the rate is a seed`"); `proposals/30_WR_E_cascade_chains_and_the_census.md` §4 C8; `unified/DECISIONS_ANSWERED.md` A-80.

---

**Settled by the checks and not asked** (each with what settled it, in `H2_DECISIONS.md`):

| raised as a question for you | settled as | by |
|---|---|---|
| the guild leader's seat (`off_npc_084`) has no rung, so the stored `scale:` column cannot be cut (B03.69) | B03.69 stays BLOCKED (owner: you, for the seat's rung or scope, or A1-46's revert); the column is not cut in v12's run, and the position goes to the held table at B03's expunge with that trigger (`workplan_v12_part5.md` B03.69) | the item's own text; HD-24's "drafted as seed content" was not carried into the item (corrected by repair lane V1, `V12_VERDICT.md` defect 4) |
| `release` is listed as owed a contest, and nobody gives it one | its shape file gives it no contest, so B32 reclassifies it | precedent: a row's shape is owned by its shape file (HD-27). **Re-opened as J-03**: check lane K8 found the move is not mechanical (the bookkeeping class may not touch a seat) |
| readings that need more than two seasons (the scar flip, the Church Influence bands, claim fade) | they go to the final long re-take (B99) | your ruling A-114 (HD-26) |
| `knot` has no written effect, but the thread batch must build it out | a design item comes first, inside the batch | precedent: E-14 and D-18 (HD-25); written by lane H3 as B35.30 |
| the two Layer 1 rows edited by B11.04 and B41.03 | ED-IN-0300 covers unmarked architecture text stated in the PR; a (RULED) row stops the item | ED-IN-0300, ratified (HD-22) |

---

**Added 2026-11-13 by the verb pass (`proposals/2026-11-13-verb-governing-attributes.md`; items B05.24, B05.25, BA1.13, B28.34, B28.35)**

| id | question | what the plan assumes meanwhile |
|---|---|---|
| J-09 | Does resisting arrest turn on standing (a brute office function) or on the body (an efficacy roll on `attr.body.*`)? | the body: efficacy-relevant, because the person arrested can plainly succeed or fail by ability |
| J-10 | Do acts on one's own state (`commit`, `forgive`, `give`, `challenge`, `covenant`) roll? B05.25's loader refuses a draw on a brute row; B07's task class (`open_case`, `destroy_record`, `issue`) and B28.02, .05, .06, .08, .09 draw today, so J-10 must be answered before those batches land | they stay efficacy-relevant (they roll) and are NOT marked brute; the loader's refusal applies to rows marked brute only |

---

**Added 2026-11-14 by the social-contest redesign (stage 3; `proposals/2026-11-14-social-contest-redesign_part5.md` §F.7; Batch B24p-sc-proceeding).** These are the two questions the redesign's five-step ladder could not settle: each overwrites the letter of a ratified ruling, which CLAUDE.md §0 reserves to you. Everything else the redesign left open was closed by the ladder and is marked where it is decided (RD §B.5, §D.1, §D.2, §A.5, §C.6, §A.2); the values that are content and yours to correct are marked `[ASSUMPTION; Jordan to correct]` in the items.

### J-SC-1 · What are the dice of an argument: Reason, or Presence? · SC (Batch B24p-sc-proceeding, B24p.07) · ANSWERED

**ANSWERED 2026-11-14 (Jordan: *"argument dice is Presence and/or Reason depending upon content of argument and
venue"*; `proposals/2026-11-14-social-contest-jordan-rulings.md` R11; `unified/DECISIONS_ANSWERED.md` A-127).**
Neither option as written: a blend. The dice of a speech are a weighted mean of the speaker's Reason and Presence,
rounded to the nearest tenth; the weight on Reason is the speech's content class (`rosters.yaml: content_classes`,
named by each ground and by `divert`: evidentiary, logical, procedural, appeal, emotional) plus the proceeding type's
`reason_bias` (a court leans to Reason, a crowd to Presence, private talk neither), clamped to `[0, 1]`; Presence
takes the rest. Presence keeps its own role besides (the share heard and delivery, R1). ED-IN-0350's letter
(*"argue main component is presence"*) is superseded by these words. The plan now does this at B24p.01 (the content
classes and their loader check), B24p.03 (`reason_bias` on every type row and its check), B24p.04 (the `speech_blend`
register row), B24p.07 (`_blend`, `weighted_tenth`, and each role's falsifier in two arms plus the slope test by venue
and content), B24p.13 (the builder fills the weights), B24p.16 (the ledger row records the amendment), B24p.18 and
B24p.23 (the shipped weights, `[ASSUMPTION; Jordan to correct]`, and the per-type slope bounds). RD §B.2 (a) holds the
rule and both weight tables. The text below is kept as the question was put.

**The situation.** When someone argues, the number of dice he rolls comes from one attribute (plus his rank in the skill). Two rulings read differently. ED-IN-0350 (ratified 2026-11-05) says `argue`'s pool attribute is Presence (charisma). Your ruling of 2026-11-14 (R1) says Reason is *"constructing the argument/speech, making it logical and reasonable and evidentiary"* and charisma is *"the ability to be listened to and be compelling with your delivery"*. The redesign gives every one of the six attributes its own mechanism, so the speech needs one of the two as its dice and the other as something else.

**The question.** Is the dice of an argument Reason (the case) or Presence (the speaker)?

**Option A — Reason is the dice (what the plan builds).** The better case rolls the more dice. Presence is the share of the speech that is heard (a quiet room hears little of a poor speaker, a crowd hears the loud) and the leverage of delivery, and it is the larger slope in an open room. Play: a bench is won by the better case, a crowd by the better speaker; a learned, graceless man has a home ground (the bench), a charming fool has another (the crowd).
**Option B — Presence is the dice.** The better speaker rolls the more dice everywhere; Reason is leverage (the proofs the room can use and the account of the other side). Play: the better speaker has the wider swing in every room, and a learned, graceless speaker has no home ground.

**Recommendation.** A: it is what R1 says in its own words (Reason *constructs* the argument, charisma is *delivery*), it keeps the six attributes' operands separate (the redesign's test that no two roles share an operand), and ED-IN-0350's sentence is kept in the sense it still has (Presence matters most where a crowd listens). B is one cell to switch to (which attribute `_speech_input` passes to `pool_of`) and the role readings of B24p.23 are then re-taken.

**What the plan assumes until you answer.** A: B24p.07 builds Reason as the dice; the one cell is named in its INSTRUCTION step 3.

**Blocks.** Nothing executes differently until B24p.07 lands; a B answer after that is one cell and a re-read of B24p.23's curves (and B98.87).

**Sources.** `proposals/2026-11-14-social-contest-redesign.md` §B.2, §B.4; `_part5.md` §F.7; `proposals/2026-11-14-social-contest-jordan-rulings.md` R1; ED-IN-0350; `master/workplan_v12/workplan_v12_part22_b24p.md` B24p.07.

---

### J-SC-2 · Does the wrong kind of argument cost, or only fail to help? · SC (Batch B24p-sc-proceeding, B24p.08)

**The situation.** An argument can appeal to evidence, to consequence, to authority or to solidarity, and each hearer is moved most by one of them. Attunement is *"identifying what kind of argumentation/speech is most effective for audience adjudicator opponent"* (R1): it lets a speaker find the ground that moves this hearer. The tree's armature (v30, ratified at Gate C, ED-1062) says a misaligned style *"simply forgoes the boost"*: choosing the wrong ground gains nothing, but costs nothing.

**The question.** When a speaker argues on his target's worst ground, does it cost him, or does it only fail to help?

**Option A — it costs (what the plan builds).** The target's worst ground subtracts a level (`misfit_level` `moderate`): reading people matters because misreading them hurts. Play: in the redesign's scratch probe Attunement's slope is about twice what it is under B; a bold speaker who cannot read a room loses rooms.
**Option B — it never costs (`misfit_level` `None`).** The best ground adds; the worst adds nothing. Play: the worst a poor reader does is argue plainly.

**Recommendation.** A: R1 gives Attunement the work of knowing what *rattles* the opponent and what is most effective, which is an edge only if error can lose something; under B Attunement is a bonus a plain speaker simply does not collect. The scratch figure (about twice) is the redesign's own probe on its own formulas, not repository code: the reading on the built module is B24p.21 and B24p.23's.

**What the plan assumes until you answer.** A: `misfit_level` ships at `moderate` at B24p.23 (it is `None` at control until then) `[ASSUMPTION; Jordan to correct]`.

**Blocks.** Nothing until B24p.23 sets the shipped values; a B answer is one setting (`None`) and a re-read.

**Sources.** `proposals/2026-11-14-social-contest-redesign.md` §B.3; `_part5.md` §F.7; `proposals/2026-11-14-social-contest-jordan-rulings.md` R1; v30 `:154-188` (reference only; ED-1062); `master/workplan_v12/workplan_v12_part22_b24p.md` B24p.04, B24p.08, B24p.23.
