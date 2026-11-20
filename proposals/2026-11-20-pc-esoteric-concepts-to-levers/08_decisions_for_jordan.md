# Part 8 — Decisions for Jordan

## Status: PROPOSED. Reference only. Each candidate was put through CLAUDE.md §0's answer order — superseded, irrelevant, answered by a design document, answered by precedent, answered by what the architecture plainly needs — before it was allowed here. **One survives.** Everything else is answered in §8.2, with the successor or precedent named.

## 8.1 Escalated

### D-1. Should a fight remember, within one engagement, what each fighter has done? (N-1)

**The question.** Seven rows from five clusters — Musashi's feint that makes the enemy "show his long sword" and his rule never to try a thing a third time, boredom passed on, Dugu's formlessness, the maiden's lull, *malícia*'s misdirection, Kumango's three warnings, the Māori point-feint into the butt-end blow — need one exchange to depend on an earlier one. Today none does: the feint is dissolved into commit depth and legibility (`wrapper.py:298-301`) and every exchange forgets the last.

**Why it survives the answer order.** (1) Not superseded: no workplan item or ruling builds within-fight memory (a search of `workplans/`, `proposals/` and `registers/` finds only the agency proposal's mention of a "within-fight threat-memory (dynamic A), if that is ever built", §3 I3). (2) Not irrelevant: the subject is live. (3) No design document decides it. (4) The nearest precedent cuts against a *feint manoeuvre* (WS-5 removed the old feint machinery and its streak bugs), not against memory, which is a different object. (5) The architecture does not settle it: both options are clean. The two lead to materially different games — one in which deception, pattern and the lure are learnable and the read is a contest across a whole engagement, and one in which those traditions keep their names and none of their effect.

**Options.**

| option | what it is | what it costs | what it buys |
|---|---|---|---|
| **A (recommended)** | one per-engagement record held by `wrapper.engagement` (which already owns `ready` and the per-beat state): the last few commits and modes of each fighter; read by `read_contest` for the defender's expectation and by `commit_depth`; zero at an engagement's start | new state in the orchestrator (within a fight only: a registered module still keeps nothing between calls); a hash mover for every fight; one export row per constant it introduces; a falsifier that an all-neutral record is byte-identical to today | the largest family in Part 6 (seven rows); the agency proposal's I3 habit-exploit, which needs the same record; a technique column (*Reading*) with things in it that are not a flat factor on the read |
| B | no memory; the traditions of F3 stay flavour | nothing | nothing; the board's *Reading* column holds only factors on `visual` and `precommit` |

**Recommendation: A, owned by the PC lane, scheduled after workplan v12 B15.04 and B16** (both reshape the commit and the read it would feed, so building first would pin numbers they move). This proposal does not design the record.

## 8.2 Answered without escalation

| candidate | answered by (step of the order) | the answer |
|---|---|---|
| The deep-commit door is nearly shut in the close (Part 7 §7.1; Part 2 §2.4) | **superseded by the plan** (step 1): workplan v12 B15.04, "the deep tier follows the window it is drawn in" (`…_part18.md:153-175`) | B15.04 owns it and states the same finding; this run is corroboration. Consequence for the jobs set: once B15.04 lands, the `counter_shallow` gate (M-1) opens a door that is no longer shut for everyone, so sets that open it (S-IT-1, S-JP-1, S-ZH-1) buy less than Part 7 §7.1's shut-door figures suggest |
| Fury's price; the still pole's payoff; agency proposal D3/Q2 (Part 5 §5.4-5.5) | **the plan** (step 1): B16.08's conserved transfer, coefficient owed to D2-1 (`…_part23.md:221-223`; `…_part44.md:150`) | no second mechanism (a read term would be a second owner of one fact). The four sources that name fury's price are **evidence for D2-1**: they support a non-zero coefficient |
| Concentration that acts on a fresh body (N-8; Part 7 §7.3) | **a design owner** (step 3): "PC-22 retires this key [`LAPSE_K`] into one Concentration function" (`config.py:119`) | evidence for PC-22's function: it must act on a fresh body, or the top rung of nearly every ladder in Part 4 does nothing in the bout |
| The yield in the bind (N-5) | **precedent** (step 4): the jobs set's deferred `branch` relation, "two levers keyed by state, deferred with PC-08" (jobs set Part 3 §3.3 rule 6) | PC-08 owns it; Part 7 §7.2 is its evidence (no factor can produce the claimed shape) |
| A "hold" choice for the never-strike-first schools (N-14) | **a design owner** (step 3): B16's round-choice cells ship empty for content (`…_part23.md:44`) | a candidate member for that content, not a mechanism |
| Should *kiri-otoshi* stay on `guard_prior_parry`? (JP-15) | **architecture** (step 5) | no: a guard prior acts on a *lost* read, and the Ittō-ryū's cut is made on a won read during the opponent's cut — the counter route. The jobs set's Part 3 table should re-file it (flagged here; that file is not edited) |
| Do concepts that land on an attribute, temperament or Concentration become board entries? | **precedent** (step 4): the jobs set keeps a standing tendency as the `disp` number, not an entry (Part 2 §2.2), and PC-22 makes composure a fought growth | no. Stillness and fury are temperament; *mushin*-as-composure, courage and the unstopped mind are Concentration; lightness and the tiger are Agility |
| What does a vow reach in the engine? (Part 5 §5.3; AF-05) | **architecture** (step 5) | only the narrowing: the decider and the terms host-side, and, when M-1 is built, the `withdraw_band` member admitting values below today's (one more value of an existing member). The reward is the season's |
| Charms, invulnerability, possession, divine infusion | **design documents** (step 3): agency proposal §5 Class A; canon P-07, P-08, P-13 (`canon/philosophy/10_constraints.md`) | never a combat handle; no carrier is invented |
| May the MODERN-SYNCRETIC and POPULAR-MYTH rows (*qinggong*, Dugu, *ki-ken-tai-icchi*, *shu-ha-ri*, *malícia*) feed content? | **a pending owner** (step 4): the jobs set's D-6, "how far this session's relaxation of the source-tier rule reaches" | D-6 decides; every such row here is labelled with its grade |
| Content for Destreza's circle on `facing_regime` (EU-15) | **superseded by a ruling** (step 1): "facing_regime stays bare (geometry, not this position; Jordan 2026-11-01)" (`ability_primitives.py:82-83`) | none proposed |
| A growth stage that itself opens a gate (Part 4 §4.3) | **architecture** (step 5) | not recommended: it duplicates what a set does |
| Silver's true time read two ways (EU-08) | **architecture** (step 5) | no decision until a technique reads one of them; a smoothness note for the PC lane |
