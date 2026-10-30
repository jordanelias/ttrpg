# Fragments of the unrecovered parts (06, A1, A3, A5)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Fragments of the files that could not be recovered. Source: tool results in the transcript between 07:12:45 and 07:26:50 of 2026-10-28, listed under each heading. The files themselves were analyst reports copied from `analysis/A6_attribute_set_from_demand.md` and `analysis/A1..A5` into the suite at 07:10:35, and the transcript half in which the analysts wrote them is not in the pages the reconstruction could read. The suite was written in a session of 2026-10-28 that committed nothing. Where this text and the tree disagree, the tree wins.

---

This file is not a part of the suite. It is every line of the unrecovered files (part 06 and appendices A1 to A5) that the transcript's surviving tool results show, quoted verbatim with the line number the session's tool printed. Nothing between the quoted lines is known. Most of these were printed by grep or `sed` through `cut -c1-N`, so a long line may end early.

## Part 06 (`06_A6_attribute_demand.md`), from the grep at 07:12:45

- line 82: - **Smaller alternative: #505's six** (Body, Hand, Wit, Nerve, Presence, Sense; `proposals/2026-10-24-character-progression-adjudication.md:248`). Body folds STR and END, which combat reads separately, and collides with `Person.body`. Sense keeps the 29% dominance. Nerve is decision-side by #505's own §10.2.
- line 88: - **`faculty(p, verb)`** = `max(capability[k], attributes[vocation_attribute[k]])`, else `pool_default`, with `k = verb_capability[verb]` (CR-20). Attributes are the floor; #505's ceiling arm can compose on this later.

## Appendix A1 (`appendix/A1_content_census.md`)

From the grep at 07:13:21 (lines 14 and 162), and from `sed -n 160,164p` through `cut -c1-600` at 07:26:50 (lines 160 to 164):

- line 14: **Does workplan v10 contain a path to a playable slice? No.** It reaches a clean, ported simulator. "Vertical slice", "playable slice" and "first playable" return zero hits across `workplans/`, the v10 proposal folder, `CURRENT.md`, `HANDOFF.md`. It schedules no client, no un-HELD text layer, and no content authoring (section 6).
- line 162: - **E3. Does the first playable person hold a seat or stand unseated?** Seated gives the strategic verbs (an unseated person has 45 of 56 eligible, none seat-gated; a ruler 56) and stakes; unseated is a personal-scale game without governance. Recommend seated at rung 1-2 (Lord Steward or a Cardinal), since the thesis is the join between scales.

Lines 160 to 164, as printed at 07:26:50:

- **E1. May agents draft `[ASSUMPTION]`-tagged content (attribute values, Tensions text, pattern fragments) for you to edit, despite "Content is not the plan's to author" and ED-649?** Otherwise blockers 4, 7, 8 wait on your authoring time and emergent range stays "unmeasurable, not zero". Recommend yes: drafts only, each with a stated revert, as the plan already does for Tensions.
- **E2. Do you add B10-S to ratified v10 ahead of the port gate?** Otherwise nothing a human can play exists before B10-20. Recommend yes, on the Python engine.
- **E3. Does the first playable person hold a seat or stand unseated?** Seated gives the strategic verbs (an unseated person has 45 of 56 eligible, none seat-gated; a ruler 56) and stakes; unseated is a personal-scale game without governance. Recommend seated at rung 1-2 (Lord Steward or a Cardinal), since the thesis is the join between scales.

[ASSUMPTION: six patterns give enough variety - basis: count of existing authored Tensions and arc material; untested]

## Appendix A3 (`appendix/A3_faction_settlement.md`), from the greps at 07:13:10 and 07:26:08

- line 15: - **Creed.** An `OUGHT` whose subject is the authored leader, with value = the faction and scope = its role template (`POP:
- line 91: 5. Ground endowment: every place gets one harbour and one seam (CP-T08-02). 6. `work` cannot run on dwellings or garrisons (empty floors).
- line 149: - **D2. Retire `set.*`.** It is orphaned; follow the 29b precedent. The `GEO` stats become build seeds only.
- line 158: - **E1. Runtime founding of factions and settlements** (FA-G39 parked, Γ22 declined). Without it the cast is closed forever and the Restoration Movement cannot rise in play. Recommend: a faction is founded by `utter` OUGHT + `commit` (already a fold), with seats only through `establish`.

## Appendix A5 (`appendix/A5_events_and_arcs.md`), lines 90 to 110

From `sed -n 90,110p` through `cut -c1-700` at 07:24:42 (the output as printed, up to the `**Reachable:**` line the cut ended on):

- Recounted from the lane headings: **RB 31 · R 2 · T 16 · LOST 4 (5, 22, 27, 48) · NEVER-WORKED 2 (19, 52)**.
- In code, **1 of 50** traced arcs is PLAYABLE (ARC-06; `02_TEST_B_ARCS.md` §1).
- Every ambient track, CI/MS scalar, auto-firing threshold and GM call in the register is [RETIRED] (D12a §C, D12b §b).

| fam | arcs (primary need) | capability | plan provides? | build |
|---|---|---|---|---|
| G | 2 9 26 28 29 30 32 35 39 41 51 54 | TS and Coherence on persons; TS gains on anomalous claims; Discovery as a person's roll | **NO** (`_part12:272` J-T2: nine keys, pending slot; threadwork modules unloaded, `_part11:42`) | TS as the tenth attribute, plus its gain and cost readers |
| A | 6 10 13 18 19 21 31 49 52 | a standing venue decides (docket, debate, vote, tribunal) | PARTIAL (`determine` executes 3/43, `_part11:25`; CR-38 bench is design-first; D-5 councillor venue [UNVERIFIED]) | `determine` executing; a councillor venue |
| H | 5 22 27 33 42 43 48 | a world Thread substrate | **NO** (G-21, `_part11:42`) | Escalation 1 |
| B | 3 4 17 34 47 55 | a person's private estimate whose crossing **summons** someone | NO: B4.1 HELD, no owner (B10-19:90) | own B4.1 as the general summons hook.; **19** arcs need it (ENDINGS `forced_by_threshold: yes`) |
| I | 1 14 36 44 46 50 | mass opinion moved by witnessed acts | PARTIAL (`tests/test_in25_stance_gain.py`; conviction motion is a top-3 blocker) | measure, then repair |
| E | 8 12 15 16 37 | covert action and revelation | PARTIAL (`conceal`, `surveil`, the investigation verbs) | Feldhaus's undeliverable revelation (`04_SYNTHESIS.md` §7) |
| D | 20 25 38 45 | an off-board polity as persons | BUILT behind `foreign=False` (`harness/populated.py:724`), HELD | flip it; foreign seat goals (G-09) |
| C | 11 24 40 | succession and office-rooted conferral | YES (IN-61 in B10-09, CR-35 in B10-17) | — |
| F | 7 23 53 | battle and wounds carry over to the next season | PARTIAL (`march` has no `field.*` in the run) | test the field path |

**Ranked by arcs unlocked:** summons hook 19 (cross-cutting) · TS on persons 12 · venue decisions 9 · substrate 7 · opinion motion 6 · revelation 5 · foreign switch 4 · battle carry-over 3. Succession is covered.

**Dead:** **19** (pure phase ordering; its dilemma survives as the one-act rule, `04_SYNTHESIS.md` §7). **5, 22, 27, 48** are dead **unless** the substrate is built (an omission, not a refusal, §2). **52** survives only with a councillor venue. All others survive as stories.

**Reachable:**
