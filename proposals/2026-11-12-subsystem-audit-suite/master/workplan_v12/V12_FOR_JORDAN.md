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

**Settled by the checks and not asked** (each with what settled it, in `H2_DECISIONS.md`):

| raised as a question for you | settled as | by |
|---|---|---|
| the guild leader's seat (`off_npc_084`) has no rung, so the stored `scale:` column cannot be cut (B03.69) | the plan drafts the seat's scope as seed content for your correction | precedent: D-19, content is drafted for your correction rather than waited on (HD-24) |
| `release` is listed as owed a contest, and nobody gives it one | its shape file gives it no contest, so B32 reclassifies it | precedent: a row's shape is owned by its shape file (HD-27) |
| readings that need more than two seasons (the scar flip, the Church Influence bands, claim fade) | they go to the final long re-take (B99) | your ruling A-114 (HD-26) |
| `knot` has no written effect, but the thread batch must build it out | a design item comes first, inside the batch | precedent: E-14 and D-18 (HD-25) |
| the two Layer 1 rows edited by B11.04 and B41.03 | ED-IN-0300 covers unmarked architecture text stated in the PR; a (RULED) row stops the item | ED-IN-0300, ratified (HD-22) |
