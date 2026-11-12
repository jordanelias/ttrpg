# WR — pessimist audit: NERS, premise and emergent narrative, of the world, its clocks and the narrative engine

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: world, threadwork, clocks, travel, survival, weather, strife and the narrative engine (`loop/encounter.py`,
`loop/calendar.py`, `loop/matter.py`, `queries/world_q.py`, `harness/strife.py`, `storybar.py`, `chronicle.py`,
`arc.py`, `ENDINGS_CLASSIFIED.yaml`), the coupling of eras, regimes and strife to allegiance, duty, obligation,
pursuit and conviction, and the five premise sentences of the world. The WR lane's audit and addendum
(`09_WR_audit.md`, `09_WR_audit_addendum_B.md`), the narrative-churn audit (`20_NARRATIVE_CHURN.md`) and the
game-level pessimist audit (`16_PESSIMIST_GAME.md`) are **cited, not redone**; every number below is new work
of this lane unless a lane is named. All runs: `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_WR/`.

## 0. Verdict

*(Being written; the sections below are appended as each probe finishes. If this line is still here the lane was
interrupted: read §12 for what ran.)*

## 2. Premise audit — the five sentences of the world, by execution

Method (`skills/premise-check/SKILL.md`): the ordinary meaning first, written before the code was opened;
the notes' account second; then the smallest world that exhibits the premise, with a control. PROXY marks a
hand-set state (a builder's write before any season); everything else is the shipped chooser or no chooser.

### 2.1 "The world changes whether or not anyone acts"

**Ordinary meaning.** Left alone, the world is not the same place a year later: seasons turn, harvests
differ, people age, sicken and die, things decay unevenly, and what happens in one valley differs from the
next. A strategy player expects a world that drifts and surprises, so that waiting is itself a risk.

**The notes' account.** MATTER is "the three motions" (matter wears, memory decays, bodies fall) plus
terms maturing; the weather draw, ageing and illness, and the lattice coupling are built and ship at their
controls (`data/fixtures.py:535, 690-691, 700`; WR F-WR-04, cited).

**The run (P1).** `build_realm(0, cap=0)` (the realm's 322 Sites and 37 cohorts, no named person), a
chooser that returns no act, shipped fixtures, 41 seasons (`p1_s0_k125_shipped.txt`; stopped at 41, the
machine was loaded). Control for the instrument: the lattice arm and the planted-source arm below move the
same columns.

| season | harbour, seam (each of 37) | band crossings | realm yield (grain) | grain in store | grain eaten | cohorts, body |
|---|---|---|---|---|---|---|
| 0 | 990 | 0 | 1,480 | 1,480 | 0 (larders empty at build) | 37, all 1000 → 940 |
| 1 | 980 | 0 | 1,443 | 2,775 | 148 | 37, all 940 |
| 20 | 790 | **37 of 37 harbours, the same season** | 1,184 | 24,716 | 148 | 37, all 940 |
| 30 | 690 | **37 of 37 seams, the same season** | 1,036 | 34,114 | 148 | 37, all 940 |
| 40 | 590 | 0 | 888 | 42,032 | 148 | 37, all 940 |

What the world does when nobody acts, in full: two of four Site kinds lose exactly 10 of 1000 a season;
the other 248 Sites are written with a wear of zero (WR F-WR-21, cited); every one of the 37 settlements is
the same settlement, so every band edge in the realm is crossed by all 37 in one season; yield falls one
per cent of its base a season; 37 cohorts eat 148 grain a season against 1,443 produced (SE measured the
ratio at build, `07_SE_audit.md:116`; this run shows it never closes: at season 40 the realm holds 284
seasons of grain and has eaten no ore, salt or timber at all, 60,310 ore in store and rising); no body
moves after season 0; nobody dies; no Date fires. The season costs about 9,900 Events at steady state, of
which 322 are the wear writes (248 of them zero) and the rest are claims deposited and decayed about
those writes. By arithmetic on the measured rate (not run): the last band edges fall at seasons 90 and 95,
every producing Site reaches 0 at season 100, and the stores then feed the cohorts for roughly another
400 seasons before the first body falls.

Seed control: `p1_s3_k8` was not run (load); the claim "the same for every seed" is by reading:
no draw is taken anywhere in MATTER at shipped fixtures (`matter.py:726` skipped, `world_q.py:1194`
returns the constant), and the build's Sites do not depend on the seed `[UNVERIFIED by run]`.

**Compare.** Ordinary understanding: a world that drifts and surprises. The notes: three licensed
clocks. The running code: a linear ramp, identical in every place, with no draw, whose first visible
event is at season 20 (five years in) and whose only consequence for anyone is a yield change smaller
than the surplus by a factor of ten. **The premise fails at shipped values.** "Changes" is true of 74
integers; it is false of anything a person in the fiction, or a player, could notice or be harmed by.
*Genre:* a strategy player would be surprised that waiting costs nothing and that every province has the
same weather, the same decay and the same granary. *Names:* `condition.worn` is emitted 322 times a
season; 74 are changes.

**F-PES-WR-03** carries this (§3).

### 2.2 "A calamity builds and breaks"

**Ordinary meaning.** Something gathers (strain, a front, a count of bad signs), people can see it
coming and argue about it, it reaches a point where it breaks, the breaking is an event with a before and
an after, and what people did beforehand changes where and how badly it breaks.

**The notes' account.** `loop/matter.py::_lattice_strain`: "THE CALAMITY RE-EXPRESSED AS A COUPLING RULE
… a worn place drags the fabric beside it down, and that fabric the next ring out, one border a season …
BOUNDED BY MENDING — persons' `restore` acts". The docstring states what is not built: "the SOURCE. No
act yet strains the lattice at Askeheim … on `build_realm` a non-zero weight couples ordinary wear … not a
Calamity (H-236)". The Rupture has no ending row (WR F-WR-20, R-26, cited).

**Three runs.**

*(a) Shipped (coupling 0).* No calamity exists: §2.1's table is the whole of it.

*(b) Coupling 250, no source, nobody acting, 26 seasons* (`p1_s0_k60_lattice.txt`). The coupling does one
thing: the 248 wear-0 Sites (dwellings, garrisons) follow the 74 wearing ones down, 40 behind
(season 20: dwelling and garrison 830, harbour and seam 790; season 25: 780 and 740). Yield, stores,
bodies, crossings: identical to (a) to the unit. There is no front, because there is no gradient: every
territory holds the same Sites at the same condition. *The Calamity switched on, in the world as built,
is a second uniform ramp.*

*(c) Coupling 250, the missing source planted (PROXY: one dwelling in `terr_T1` set to 0 before season
0), nobody acting, 14 seasons* (`p3_s0_k14_c250.txt`).

| season | ring 0 (source territory, 32 Sites) | ring 1 (76) | ring 2 (57) | ring 3 (119) | ring 4 (38) | realm yield, all kinds |
|---|---|---|---|---|---|---|
| 0 | 725 | 748 | 998 | 998 | 997 | 4,810 |
| 3 | 303 | 311 | 722 | 932 | 978 | 3,510 |
| 7 | 92 | 93 | 335 | 635 | 837 | 2,173 |
| 13 | 15 | 14 | 62 | 212 | 432 | 719 |

It **builds**, and as the docstring says: a ring a season, geometric (each Site loses a quarter of its gap
to the weakest neighbour), so one ruined cottage takes the realm's yield from 4,810 to 719 in fourteen
seasons. It does **not break**: in fourteen seasons there is no death, no body falls (every cohort still
940; the stores of §2.1 carry them), no Event marks a rupture, `endings_reached` is `[]`, and the 96 band
crossings are each "a witnessable Event; produce no outcome". The decay has no floor but zero, no
reversal, and no moment. *And nothing a person does can be shown to bound it:* `restore`, the one verb the
docstring names as the bound, was attempted 0 times in three seasons at seeds 0, 1 and 2 of the shipped
realm (GAME X1's verb census, re-read here; this lane's P2 arms below).

**Compare.** Ordinary: gathers, is seen, breaks, is changed by what people did. Notes: honest that the
source is unbuilt. Code: at shipped values nothing; switched on, a uniform ramp; with a hand-planted
source, an exponential that never arrives anywhere. **The premise fails in both halves at shipped
values, and in the second half ("breaks") in every arm.** *Intent:* a designer reading "the Calamity"
would not recognise it in a rule under which the world's defining catastrophe is started by whichever
cottage is worst. *Standing rule:* the pull is exact arithmetic (WR F-WR-24, cited).

**F-PES-WR-02** carries this (§3).

