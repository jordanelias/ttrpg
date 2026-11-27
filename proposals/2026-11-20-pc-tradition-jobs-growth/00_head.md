# Personal combat: traditions as jobs, the tradition board, and how a fighter grows

## Status: PROPOSED — design reference, nothing built. Lane PC. No ID allocated. No file outside this directory is edited. **Merging this directory ratifies NOTHING** — the default that a merge ratifies PROPOSED content (ED-1094) is held back for every part; see "Held back" below.

---

## Verdict

**Make a tradition a shared curriculum that each person walks by their own path. Hold what a fighter brings to one fight on a small "tradition board" whose capacity grows with fight experience, not with strength. Let named sets of techniques open doors the engine already has, never add power.** Most of it composes on the host side into the numbers the combat module already takes. **The edits it would make to `modules/combat/`, all of them:**

| # | edit | needed for | required or optional |
|---|---|---|---|
| M-1 | a `gate` input family: four members, one read at each existing `if` (`wrapper.py:325`, which must also be split in two; `contact.py:27-36`; `combat_systems.py:857`) | sets that open doors (D-3, D-4) | required if sets are to do more than board rules |
| M-2 | R-1: one `fight_start` emit of the non-neutral input numbers (`wrapper.py:585-586`) | a player seeing why (Part 5) | optional, recommended; asked for by B18.02's own falsifier |
| M-3 | R-2: a comparison and an emit at each instrumented lever and gate site | a player seeing which technique decided an event | optional, recommended second |
| M-4 | the generics opened to every person: an edit to `ability_primitives.py` **only if made before B18.02**; after B18.02 the gate is host-side data | D-8 | optional |
| M-5 | a record field carrying a second tradition (`known_traditions`), **only if** cross-training must reach a fight before B18.02 lands | cross-training (Part 5 §5.1) | optional; B18.02 makes it unnecessary |
| — | familiarity taking a number per party instead of a tradition name (`combat_systems.py:936,938,990,1002`) | B18.02's "never the name of a … tradition" | **not this proposal's edit**: B18.02 or PC-21 owns it (Part 5 §5.3) |

Six legible character sheets, generated from the live engine by `sheets.py`, show the design on real figures, and they turned up three facts the plan should know: a practised board is worth about 10–21 points of win rate in a mirror (not "near zero"; the two cross-trained sheets, at +10.8 and +20.8, measure their primary school only); the counter's reach saturates at a level set by temperament (level 3 for a neutral fighter, so levels 4–8 do nothing there; level 2 for a cautious one, 5 for the most aggressive); and a second school's techniques cannot reach a fight through today's input record.

## The recommendation, ranked

| rank | proposal | part | one line |
|---|---|---|---|
| 1 | **J-D: shared curriculum, personal path** | 1 | a tradition is a curriculum in short lines; each person has a path through it (authored for notables, generated from the lifepath for everyone else); a primary tradition fixed by history; a second one after a threshold; at most one personal set |
| 2 | **B-1: the board** | 2 | five columns by phase of the bout, slots by growth stage, an attention budget read from Concentration, a fixed foundation, three saved boards; first increment B-2 (everything learned is on) |
| 3 | **sets that open gates** | 3 | 3–4 named techniques, visible, at most three per tradition, effect = one opened gate or one board rule, never magnitude |
| 4 | **G-1: taught depth, fought breadth** | 4 | technique levels only from a teacher who knows more (or a school, a story event, self-study to level 2); fighting and sparring raise attention through Concentration (PC-22), never a technique |
| 5 | **C-1: one `Person` field at a time** | 5 | first increment: `Person.tradition`, filled once at build; it fills the record's `traditions` and the fixed foundation at level 1. Input to PC-21, which owns the carrier |
| 6 | **R-1 then R-2: the record shows the technique** | 5 | the fight's first event lists the non-neutral numbers; then an event wherever a technique decided a yes-or-no draw (exact: the draw against the probability with and without it) |

Variants ranked below each winner, with the reason each loses, are in their parts: Part 1 (shared ladder; Bravely-Default job-swap; Triangle-Strategy bespoke line alone), Part 2 (all-on; Troubleshooter's three budgets; a power budget, which dies under the fiat audit), Part 4 (a technique-point currency; growth by use, which dies under the 2026-11-07 ruling; fixed at creation).

## Words used in every part (each defined once, here)

| word | means | why this word |
|---|---|---|
| **tradition** | a school of fighting (German, Italian, Spanish, English, Japanese, Chinese, Filipino, or `none`). In the engine a name on the fighter (`modules/combat/combatant.py:106`) | the repo's own word; "job" is used only when comparing with other games |
| **technique** | one learnable, named thing a tradition teaches (in code an *ability*, `modules/combat/ability_primitives.py:29`), with a **level** from 0 (no effect) to 8 (`:151`) | plain; the code's word is kept in code references |
| **lever** | a place in the engine's bout where a technique acts (fifteen live today) | the code's own word; it never appears on a character sheet |
| **curriculum** | a tradition's techniques, in short lines, with what must come before what | ordinary teaching word |
| **path** | one person's route through one or more curricula: what they learned, in what order, from whom | Triangle Strategy's per-character line, as an ordering rather than a wall |
| **tradition board** (short: **board**) | what a fighter brings into one fight out of everything they know | **not "loadout"**, which in this repo means the weapons and armour carried (workplan v12 B18.06 glossary). Both layers sit on one fighter and are named apart |
| **attention** | the board's budget: how much a fighter can hold in mind in a bout, read from Concentration | plain; it says what it limits |
| **set** | 3–4 named techniques that, held together, open one door none opens alone | Troubleshooter's "Mastery Set", in plain words |
| **gate** | an existing "if" in the engine that a set may widen (four proposed) | plain |

## What is in each part

| part | file | holds |
|---|---|---|
| 1 | `01_tradition_as_job.md` | what the engine does with a tradition today (verified); four job variants compared on the same axes; the recommendation J-D |
| 2 | `02_tradition_board.md` | the two layers (loadout and board); the three kinds of entry (modifier, access, board rule) reconciled with the older access/bias/tendency words; columns tested against FFT's and Troubleshooter's slots; fixed foundation; the budget; saved boards; one technique per lever |
| 3 | `03_gates_sets_mixing.md` | the gate-and-enable map (what is rigid engine fact, what is free data); the four proposed gates; tradition categories against the engine; the set rule; techniques and sets for all seven traditions, each labelled source-inspired or invented; the generics; mixing rules |
| 4 | `04_acquisition_and_growth.md` | three growths with one writer each; what raises a technique level and at what cost; how it differs from the Concentration growth of the 2026-11-07 rulings; growth precedents adjudicated; two findings from the sheets |
| 5 | `05_carrier_and_record.md` | carrier options and the smallest first increment; the cross-training door finding; how the record would show a technique at work |
| 6 | `06_troubleshooter_study.md` | Troubleshooter: Abandoned Children in detail: its systems as tagged facts, what players and reviewers said, and a 27-row transfer table |
| 7 | `07_precedent_adjudication.md` | Troubleshooter, Triangle Strategy, Tactics Ogre, Bravely Default, FFT, Fire Emblem: Three Houses, Divinity: Original Sin 2, D&D 5e, Pathfinder 2e, FF5, GURPS and SaGa on gating, enabling, reward, sets and mixing; what Valoria takes and rejects |
| 8 | `08_character_sheets.md`, generated by `sheets.py` | six sheets: German (practised), Italian (novice), Japanese (veteran), Spanish cross-trained in Italian, a bespoke-path notable (Italian with German lessons), and a fighter with no school. Every engine figure is computed in the run, except what is typed and says so: the list of fifteen live levers (taken from the earlier draft, each checked by grep in Part 2) and the plain-language descriptions |
| 9 | `09_decisions_for_jordan.md` | eight ranked decisions, each with the recommended option and the cost of the others; the questions answered without escalation |

**Regenerate and check:** `python -I proposals/2026-11-20-pc-tradition-jobs-growth/sheets.py > proposals/2026-11-20-pc-tradition-jobs-growth/08_character_sheets.md` (about 15 seconds; 400 seeds per sheet); `sheets.py --check` (its own falsifiers: every curriculum entry matches the live registry's tradition, an untaught technique is exactly inert, an empty board fights byte-identically to no board over 20 seeds, every build is within its budget); `sheets.py --curriculum` (the curricula as data). `sheets.py` imports `modules.combat` through its package path and edits nothing on disk; the draft and invented techniques are added to its own process's copy of the ability table so the engine's functions compute their figures.

## Decisions for Jordan (titles; detail in Part 9)

1. D-1 The job model: shared curriculum with a personal path.
2. D-2 The board's budget: slots plus attention from Concentration.
3. D-3 Sets: gate-or-board-rule effects only, visible, three per tradition.
4. D-4 The gate input family (M-1; with M-2 to M-5 the full list of module edits is in the Verdict); grid predicates only over states the engine computes.
5. D-5 What a board is judged by: the 2-point band for one technique at level 1, the fiat audit plus a per-stage ceiling for a board.
6. D-6 How far this session's relaxation of the source-tier rule reaches; invented period terms ship under plain names until checked (ED-PC-0026).
7. D-7 May a teacher's level gate `train`?
8. D-8 The 21 generics become open to every person.

## Held back (nothing here is ratified by merging)

Every proposal and every number in this directory needs Jordan's separate sign-off. Specifically: the job model; the board, its columns, budget, costs and slot counts; the sets and the four gates; the teacher rule for `train`; the generics' status; the scope of the source-tier relaxation; every technique, set, curriculum and value marked NEW, INV, RECALL or `[ASSUMPTION; low]` (content is Jordan's, plan rule P11); and the six persons on the sheets, who are illustrations.

## Reading status (stated so a reader can weigh the claims)

**Read in full:** the brief and its eleven addenda; the four research sheets (Troubleshooter characters, combat and reception; Triangle Strategy; Tactics Ogre and Bravely Default); the user's board screenshot sheet; `modules/combat/ability_primitives.py`, `traditions.py`, `tradition.py`, `fight.py`, `attributes.py`, `combatant.py`; the earlier draft `00_tradition_sets.md` and `kits_draft.py`; the agency proposal §1–§11 and §21.

**Read in part:** `guide_2037290423.md` §4–§7 (all of the sections the brief named); `guide_1349483727_images.md` (method, the first three boards, Tables 1–3); `fandom_wiki.md` §1.1–1.2, §3–§4; `fandom_masteries.md` (by grep); `precedents_other.md` (FFT §1.1–1.7 and all four GATES/ENABLES blocks); `discussions_builds.md` (by grep for praise, complaint and role identity); `wrapper.py:535-637` and the gate sites; `combat_systems.py` at every lever site and gate cited; `capabilities.py:1-80`; `inputs.py` (the combat input record); `carriers.py` (the `Person` fields); `effects_combat.py` (`_eff_train`, `_grown`); hole rows H-97, H-264, H-265, H-349, H-350; workplan v12 B15.13, B15.14, the PC-21/PC-22/PC-08 rows; the B18 batch (scratchpad copy); the person-inputs proposal (Part D, NERS); the 2026-10-24 progression adjudication §2.2, §3, §4.1–4.5 (not §4.6–§5).

**Not read:** `guides_masteries.md`, `combat_skill_interlocks.md` and `guide_1971619284.md` beyond their heading lists; `fandom_wiki.md`'s set transcription and character appendices; the agency proposal §12–§20 and §22; the August 2026 stats-and-progression proposal (`2026-08-15-…`; the brief asked for a skim; not done); the archived `ability_armature.md`, `tradition_decomposition_v1.md` and `phase4_5_plan_v1.md` (their content is used only as quoted by the earlier draft and the agency proposal); `.audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md` (quoted via the earlier draft); `03_PC_loadout_and_carry.md` and `03_PC_typed_outcome_one_door.md` beyond what the B18 batch copies; the B16 batch; the rest of `combat_systems.py`, `wrapper.py`, `core.py`, `contact.py`.

**Not verified:** the season hash for any step (no season was run); whether any pinned artifact hashes the fight trace (R-1, R-2); that the closed-measure state is in scope at the grab call (`grab_close`); that each sigma site holds the net it banded (R-2); the experience term of Concentration (PC-22, unbuilt).
