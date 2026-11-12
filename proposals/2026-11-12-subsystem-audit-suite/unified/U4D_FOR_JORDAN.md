# Your words that fail the ordinary-English test: four questions

## Status: REFERENCE (a decision register for the U4d glossary lane; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: U4d (glossary reconciliation and the ordinary-English word test, `STAGES.md` "Terms mean what ordinary English says").

**What this is.** The word test asks two things of every term: does a reader who has never seen this repository,
given the word in its sentence, land on the meaning we intend; and is the word used that way outside the
repository. Where one of your own ruled words fails, or where an agent has narrowed or redirected it, no agent
renames it: it is listed here with a plain alternative and what a rename would cost. The form follows
`DECISIONS_FOR_JORDAN.md`. Answering none of them is safe: the suite keeps your word as it stands.

**ANSWERED 2026-11-12 (A-94): J-U4d-01 regime stands; J-U4d-02 subformation stands as Jordan's word and is settled in the mass-battle lexicon (A-95); J-U4d-04 rung stands; J-U4d-03 prowess/aptitude open.**

**How to answer.** One line will do: *"keep all four"*, or *"J-U4d-01 take B"*, and so on.

---

### J-U4d-01 · "Regime": a government, or a camp of shared opinion?

**What it means today.** Your A-82 and A-83 define a regime as a cluster of persons and bodies who share, to
some extent, opinions on caste, religion, politics, Altonia and militarism, with a core and a fringe, and who
feel an unsaid pressure to act alike. The suite builds it under that name (`rosters.yaml: regime_cores`,
proposed; `30_WR_B`, `30_WR_G`, `31_WR_A`).

**Why it is listed.** In ordinary English a regime is a government or a system of rule ("the old regime"). A
reader given "Varfell's regime" lands on "whoever governs Varfell", not "the camp of people who think as
Varfell's core does". Your A-86 uses the word in that ordinary sense ("the ruling regime is part of 'who
rules'"), so the one word carries two meanings in your own rulings.

**The question.** Should the game's word for a camp of shared opinion stay "regime"?

**Option A: keep "regime".** No change. The glossary defines it and the suite keeps A-86's "ruling regime"
as the one place it also means the government.
**Option B: "camp"** (or "persuasion"). The ordinary word for people who share a position. A-82's "factions of
opinion" is the player-facing phrase either way. Cost: about 70 suite documents use the word; the tree has no
code name yet (`regime_cores` is proposed, not landed), so no seeded result moves.

**Recommendation.** B, because the proposed roster has not landed and the rename is free in code now; A if you
want the political flavour of the word.

**What the suite assumes meanwhile.** A: "regime" as A-82 defines it.

**Sources.** `DECISIONS_ANSWERED.md` A-82, A-83, A-86; `U1_GLOSSARY.md` *regime*.

---

### J-U4d-02 · "Subformation": a group of units, or one unit?

**What it means today.** Three meanings meet in one word. Your A-59: *"each unit within subformation will have
its own martial prowess ... impacted by subformation with tactics"*, a grouping that holds units. The tree's
code: the army Record's key `subformations` and the class `orderofbattle.Subformation` are each **one unit**
(A-2: a unit is a row). An older design surface: a unit's cell arrangement. The suite's vocabulary decision
(`U1_OWNERS_AND_VOCABULARY.md` D-U1-11o) kept the code's meaning, called a unit's arrangement its
**formation**, and called your grouping a **formation post group** (front, rear, left, right, reserve), so the
suite's prose no longer uses your word for what you meant by it.

**Why it is listed.** Ordinary military English agrees with you: a subformation is a formation inside a larger
one. It is the tree's code name that fails the test (it names a single unit). An agent redirected your word,
which this lane may not do.

**The question.** Is a subformation a group of units inside the army (your A-59 reading)?

**Option A: yes, your reading.** The suite says "subformation" for a group of units (what D-U1-11o calls a
formation post group), "unit" for a row, "formation" for a unit's cell arrangement. The code's `subformations`
key and `Subformation` class become `units` / `Unit` in a v12 batch. Cost: 9 code and data files; the army
Record's key is part of its content, so every seeded result with an army moves once
[ASSUMPTION: the army Record's keys enter `World.content_hash()`; not measured].
**Option B: keep D-U1-11o.** The suite never says "subformation" in prose; your grouping is a "formation post
group"; the code keeps its names.

**Recommendation.** A: it keeps your word in your sense and removes the one name that misleads.

**What the suite assumes meanwhile.** B (as decided by D-U1-11o), with the prose already using "unit" for a
row (U4d).

**Sources.** `DECISIONS_ANSWERED.md` A-2, A-59; `U1_OWNERS_AND_VOCABULARY.md` D-U1-11o;
`proposals/04_MB_cell_hierarchy_as_data.md`; `proposals/27_MB_B_unit_prowess_on_the_row.md`.

---

### J-U4d-03 · "Prowess" (and "aptitude"): a unit's quality only, or a person's too?

**What it means today.** The suite reserves **prowess** for a unit's quality of troops and equipment (your A-59)
and says **training** for a person (D-U1-11p); it reserves **aptitude** for a kind of capability that gives no
dice, and says **talent** for the governing attribute (D-U1-11q). Lane 29 read your A-71 (*"someone's
aptitude/prowess allowing them to defend better"*) as talent and training.

**Why it is listed.** Ordinary English uses "prowess" first of a person (skill at arms) and "aptitude" of a
person's natural ability. Your A-71 uses both of a person. The narrowing is an agent's, so it is put to you.

**The question.** May the suite use "prowess" for a person's fighting skill as well as a unit's quality?

**Option A: keep the narrowing.** Prowess is a unit's; a person has training (learned) and talent (inborn).
**Option B: prowess for both.** A person's prowess is his trained score in arms; a unit's is its troop and
equipment quality. Cost: no code (neither name is in the tree); prose in about 23 suite documents is read
again.

**Recommendation.** A: the suite's two words for a person (training, talent) are plainer and already carry A-7's
two numbers; "prowess" stays your word for a unit, as A-59 used it.

**What the suite assumes meanwhile.** A.

**Sources.** `DECISIONS_ANSWERED.md` A-7, A-59, A-71; `U1_OWNERS_AND_VOCABULARY.md` D-U1-11p, D-U1-11q;
`proposals/29_DICE_one_opposed_rule_form_and_tuning.md`.

---

### J-U4d-04 · "Rung" for a place

**What it means today.** Your ruling of 2026-10-28 (ED-IN-0302: *"rung = world side"*) made "rung" Layer 1's
word for a node of the realm: a territory, a settlement, a duchy, the realm, even a person's own place
(`state/carriers.py::Rung`, eight kinds, one type). Your A-64 also says *"rung of office"*, meaning a level of
seniority.

**Why it is listed.** In ordinary English a rung is a step of a ladder, and figuratively a level ("a rung of
office", which passes). Used for a place it fails: a reader given "the army marched into the rung" does not
land on "a territory".

**The question.** Should the code's name for a place in the realm stay `Rung`?

**Option A: keep `Rung`.** Prose says the kind ("territory", "settlement") or "place" where it can and gives
`Rung` in backticks once; "rung of office" keeps your A-64 sense.
**Option B: rename the type** (to `Place` or `Division`; `Holding` is taken).
Cost: a Layer 1 amendment (`04` §B.3 and the ED-IN-0302 vocabulary), about 217 tree files that mention a rung,
and every Event kind spelled `rung.*` (`rung.ceded`, `rung.abandoned`), which are logged, so every seeded result
moves once if the kinds are renamed too [ASSUMPTION: renaming the class alone moves no hash; not measured].

**Recommendation.** A: the cost is large, the word is only half wrong, and the suite's prose can carry the plain
word.

**What the suite assumes meanwhile.** A.

**Sources.** `registers/editorial_ledger_in.jsonl` ED-IN-0302; `architecture/meta/04_CODE_ARCHITECTURE.md`
§B.3; `DECISIONS_ANSWERED.md` A-64; `U1_GLOSSARY.md` *rung*.
