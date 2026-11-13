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

**Settled by the checks and not asked** (each with what settled it, in `H2_DECISIONS.md`):

| raised as a question for you | settled as | by |
|---|---|---|
| the guild leader's seat (`off_npc_084`) has no rung, so the stored `scale:` column cannot be cut (B03.69) | the plan drafts the seat's scope as seed content for your correction | precedent: D-19, content is drafted for your correction rather than waited on (HD-24) |
| `release` is listed as owed a contest, and nobody gives it one | its shape file gives it no contest, so B32 reclassifies it | precedent: a row's shape is owned by its shape file (HD-27). **Re-opened as J-03**: check lane K8 found the move is not mechanical (the bookkeeping class may not touch a seat) |
| readings that need more than two seasons (the scar flip, the Church Influence bands, claim fade) | they go to the final long re-take (B99) | your ruling A-114 (HD-26) |
| `knot` has no written effect, but the thread batch must build it out | a design item comes first, inside the batch | precedent: E-14 and D-18 (HD-25); written by lane H3 as B35.30 |
| the two Layer 1 rows edited by B11.04 and B41.03 | ED-IN-0300 covers unmarked architecture text stated in the PR; a (RULED) row stops the item | ED-IN-0300, ratified (HD-22) |
