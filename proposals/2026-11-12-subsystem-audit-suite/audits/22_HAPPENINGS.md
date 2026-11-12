# 22 · Happenings: do the things that happen in computed play make sense, and what repairs the ones that do not

## Status: AUDIT (a terminal pass; proposals in `proposals/22_HAPPENINGS_*.md`; not canon; resolves nothing at runtime, CLAUDE.md §0.05)

Jordan, 2026-11-12, on a digest line reading "the King dies at tick 0 in every seed, which empties seven
seats that can never be refilled": *"why would the King always die?? Anyway, I expect Fable to assess
whether these happenings actually make sense and seem reasonable, and then fix."*

Method (`PESSIMIST_BRIEF.md`): ordinary meaning first, then run. A happening is judged against what a
player of strategy and role-playing games, or a reader of the world, would expect from the words. Scratch
output: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/HAPPEN/`.

## 0. Verdict

**The King does not die at the first tick any more. The digest line is true of an old tree and false of
this one.** It was measured on 2026-10-22 at commit `51d7b05`; the digest (`digests/DG_proposalsB4.md:100`,
`:114`, `:258`) repeats it without a re-run. Re-run at HEAD (§1.1): at seed 0 the King, `p_npc_020` Almud
Almqvist, is alive after season 0, nobody in the realm dies, and all 34 seats are still held.

**Why he died then** (§1.2): at `51d7b05` a person formed `fight` or `accept` against **any living person
his question named**; the King is the person most questions name; a fight then ended with somebody felled in
most calls; and `accept` needed no challenge. So in the first season, at every seed, somebody near him
attacked him: at seed 0 `p_npc_006` wounded him and then **the Queen's `accept` killed him**; at seed 1 **the
Prince's `fight`** killed him; at seed 2 the Queen's `accept` again. No motive, no quarrel, no war. That was
a formation defect, and v11 CR-87 (`rosters.yaml: violence_contexts`, ED-IN-0337) closed it: violence now
needs a context (war, crime, duel, defence).

**What is true now is the opposite failure, and it is no more reasonable** (§1.3): at HEAD the King cannot
die of anything in shipped play. Age and illness hazards ship at 0, nobody starves but a cohort, `fight`
never forms, and every one of the 48 challenges issued at seed 0 in one season is refused. A realm where
the royal family murders the King in the first season is absurd; a realm where no named person can die is
inert. The repair (§1.5, proposal `22_HAPPENINGS_A_*`) makes a ruler's death what it is in the world: rare,
caused, graded, drawn, and followed by a succession that can go more than one way.

The rest of this file is the same test applied to everything else the suite has measured (§2), ranked by
how much of play each spoils, with the fix and who carries it.

