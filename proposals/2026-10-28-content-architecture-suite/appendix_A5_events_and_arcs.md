# A5 — Events, freestanding storylines, the 55 arcs

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Appendix A5 of the suite, an analyst report copied from the session's `analysis/` into the suite at 07:10:35Z. Source: the session's own record of the analysis file written at 06:17:35Z and patched in place (13,988 bytes), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---

## Verdicts
- **Q7:** There is no event deck in code, and none should be built as a deck. "Event" means three objects. Goldenfurt's card template survives once Π, effects and tags are cut. Events attach to persons, seats and places, never to a faction or a season.
- **Directive:** Yes, lawfully. A **scenario row** is world-gen data read once by `build_realm`. It opens mid-game only through a bound person's own act, admitted by a T-b band. Every later beat is a person's choice or a staged Record maturing. Cost: one amended B10-19 line and about 36 authored rows.
- **Q8:** 49 of 55 arcs survive as stories in design. 1 runs in code. The plan as written makes about 17 reachable. Four additions take that to about 40, and a world-substrate object adds 7 more.

Known state, corrected:
- `engine/season/tensions.yaml` **does not exist**. The six cards are unbuilt CL-EVENTS commits (3)-(4) in B10-18 (`workplans/valoria_master_workplan_v10_part4.md:526-527`).
- CL-THRUST B0.1 is **BUILT** (`engine/season/harness/arc.py:123`). `_part4:529`'s "Built so far: nothing" is stale.
- The Tensions deck is **6 cards, draw 1**: the archive's cut table supersedes 8-10 draw 2 (`.designs/systems/_architecture/reference/conflict_architecture_proposal.md:154`).

## 1. EVENTS
**VERDICT:** No deck or card carrier exists. [NULL: `EVT-|EventDeck|deck|tension` over `engine/season`, `modules` — only threadwork co-movement and mass-battle tactic cards.] The plan does not adopt one.

| meaning | lawful form | status |
|---|---|---|
| **World forcing**: MATTER, BODIES, fading (AX-5, `architecture/meta/01_AXIOMS.md:164`) | actorless Event; a crossing "EMITS AND WRITES NOTHING" (`engine/season/loop/matter.py:80`) | BUILT; the weather factor is a constant 1.0 (`queries/world_q.py:945`); per-territory weather is CL-EVENTS (1)-(2) |
| **Person-driven**: every act | Event with `causes[]` (`state/carriers.py:258`) | BUILT; this is the bulk |
| **Authored situation** | rows placed at build, then left to persons | `goals.yaml` BUILT (38 rows); Tensions planned; scenarios (§2) proposed |

**Refused, and it stays refused:**
- A per-season emitter (`proposals/2026-10-13-narration-mechanisms.md:181-212`: Records exist only at RES/ACTS; T-c).
- Π draws, Directives and place-held tags (`_part4:525`: T-a, T-h, T-i, AX-2).

**Goldenfurt fields** (`.designs/.../goldenfurt_slice/reference/event_deck.md:30`):
- `id`/`family`: KEEP, as a tag only.
- `triggers`: SPLIT into a build-time eligibility query plus a person-side band on the opener's own ledger (AX-2).
- `weight`: KEEP the base for the build draw; CUT Π [RETIRED].
- `cooldown`/`excludes`: KEEP as draw-without-replacement at build, plus the gate refusing a duplicate live Record.
- `npc_refs`: become role slots on seats.
- `the_ask`: KEEP as the question to a named person.
- `pressure_if_ignored`: CUT; abstention is witnessable, consequences are others' acts.
- `responses`: KEEP the existing verbs; CUT the authored effects and Ledger tags. `seeds` becomes a later row's eligibility, reading the Record an act minted.
- Directive generator: CUT [RETIRED].

**Attach points:** a person (goal row, body) · a seat (whoever holds it) · a place (Rung stores, `Site.condition`, territory factor) · the world at build (Tensions draw, `foreign` switch). Never a faction (T-h: via its seats); never a season (no clock emits).

**Missing, ranked:** (1) a scenario registry; (2) per-territory weather; (3) the Tensions receiver (planned, shipped off); (4) card-by-card intake of the 58 proposed cards (`proposals/grounded_event_card_deck_v1.md`) and Goldenfurt's 28.

**DECISION:** the decks remain a content quarry. Their gate requires retired Key types (`_part4:525`).

## 2. FREESTANDING STORYLINES
**VERDICT:** No rule needs to bend. The narration proposal already names the lawful shape: *"one authored occasion placing an object, after which the later beats are the engine's own motions on it (`Record.stages` → `term.matured`) or persons' responses"* (`narration-mechanisms.md:196`). Staged Records, `oblige`, `date.scheduled` and `case.opened` are "Already exist; lawful" (:209).

Why needed: the synthesis finds "**no convergence check**" and that a blocked core "stops it from terminating" (`proposals/2026-08-30-arc-reachability/04_SYNTHESIS.md:105`, `:146`); 19 of 50 arcs want a crossing to **summon** a named person (`proposals/2026-08-31-shape-tracer/02_TEST_B_ARCS.md` §2). Emergence alone supplies neither.

**Template**: `engine/season/scenarios.yaml`, one loader, read once at build. Precedents: Tensions commit (3) and narration W8 Rung 2.
| field | content · rule |
|---|---|
| `id` `family` `source` | tag and quoted origin |
| `eligible` | a build-time query over the world; a failing row is not drawn |
| `places` | persons (cast or lifepath), goal rows through `data/goals.py::parse`, a claim seeded in one ledger. Ids are prefixed `scn_<id>_`; no new World field |
| `opener` | a **seat** (office-rooted, so it rebinds through tenure) — AX-1 |
| `opens_on` | a band on the opener's **own ledger**, via the CL-THRUST B3.2 referent into his `need` question. T-b: it changes the choice and is not `fires_at` |
| `opening_act` | an existing verb plus a Record kind with `stages`. The **act** declares the term, so T-c is satisfied |
| `roles` | the opener's chosen referent, or the holder of a seat over the place. Never a random bind |
| `beats` | the question each role receives (a document, a summons, a hearing at `term.matured`). The menu is the whole verb table, with no whitelist |
| `outcomes` | **none authored**: only degrees of `determine`/`argue`/`fight`, or `covenant`/`migrate`/`conceal` |
| non-repetition | ≤1 row per family per world at build; the gate refuses a second live Record of the same kind and subject; a re-open is the opener's own act. No stored aggregate (T-a) |

**Worked instance: Rendstad** (`skills/prose-writer/references/rendstad-arc.md`, `rendstad-scenes-6-7.md`):
- *eligible:* a non-Church-held Hafenmark settlement with a folk practitioner.
- *places:* Ilse; the foreman, holding a firsthand claim and a goal to tell the Church.
- *opener:* the Doctrinal Compliance seat. *opens_on:* that claim is in the opener's ledger.
- *act:* `open_case`, Record `assessment` [notice → hearing], term declared by the act.
- Beats:
  - B1, Kalder (the hold seat): comply, `evade/defy` (Precedent 41), or `petition` Baralta's seat.
  - B2, Baralta: `issue` a counter-writ, `covenant`, or nothing.
  - B3, Vael or anyone present: `interview`, `tell`, `conceal`.
  - B4, Ilse, only if a claim reaches her: `conceal`, `migrate`, or appear.
  - B5, at the hearing the judge `determine`s (DECIDER), or Church and Hafenmark `argue` (ROLL).
- *Endings:* `arrest`/`pardon`; dismissed; jurisdiction conceded; subject gone; or lapsed (`record.expired`), with re-opening the assessor's choice.
- Scenes 4-7 (Vael's TS, Edda, Tamar) are render-only. They need family G (§3) and NM-W5. Without them the row runs as a jurisdiction story.

**B10-19 amendment** (`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-19.md:95`):
- The row breaks none of: carrier, stage store, non-person outcome, forecast, lookahead, verb whitelist.
- **Replace** *"deal arcs per season (the deck is world-gen only)"* with: *"deal arcs or scenarios per season by any emitter: no loop step mints one; a scenario row is world-gen data read once by `build_realm`, opened mid-game only by a bound person's own act on a candidate a T-b band admitted."*
- **Add** to the loader's refusal list: `fires_at`, `outcome`, `deadline`, and any standing, stance or tenure write outside goal rows.
- **Extend** the arc rule: the NEVER arcs (9) and arcs 10/14/18 (`.../gm_ref/arc_narrative_analysis.md:346`, "reclassify as scenario triggers") become scenario rows, not ladders.

**How many:**
- Each world draws 6 (2 Tensions plus 4 openable). For two worlds to share fewer than one on average, 6²/P < 1, so **P ≥ 36** (about 9 families × 4). First slice: **8**, enough to read STORY-BAR on against off.
- **Runtime-generated: 0.** Variety comes from binding.
- The seed corpus is already about 60: 9 NEVER arcs, 10/14/18, SCN-01..15 (`engine/season/cases/ARC6.yaml`), NSC 2/6/8/9, Tensions 6, Goldenfurt 28, Rendstad.
- Precedent: King of Dragon Pass ships 544 authored events (D7b, T16:230).

## 3. THE 55 ARCS
**VERDICT:** The stories survive and the mechanisms do not. The exercise scored MECHANISM and STORY separately (`04_SYNTHESIS.md:8-20`).
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
- Plan as written: C, E and F plus most of A and part of I, **≈17**. This also needs B6.n's ladder content, which "has no builder" (B10-19:93).
- Plus the summons hook owned, TS on persons, `foreign` on, and scenario rows plus authored ladders (B, D, G, rest of I): **≈40**.
- Plus the substrate: **≈47**.
- [CONFIDENCE: low; family-table count, not traced.]

**Sample check, 8 arcs at source:**
- ENDINGS classes match for 01 THRESHOLD/forced, 05 NEVER, 06 ROLL, 20 THRESHOLD, 22 ROLL, 34 DECIDER/forced, 39 NEVER/forced (`engine/season/ENDINGS_CLASSIFIED.yaml:25-176`).
- Lane verdicts match for 05 LOST (`01_arcs_01_18.md:249`), 20 T (`02_arcs_19_40.md:103`, invasion arm blocked on the off-board actor), 39 T (:753, the sensitisation rule is lost), 34 RB (:557), and 52 NW (`03_arcs_41_55_and_emergent.md:306`).
- "50 of the 55 classified" is wrong: ENDINGS holds 48 ARC rows (1-18, 20-45, R16-R19) plus EMG-10/11. Arcs 46-55 are unclassified, so the arc rule cannot draw on them yet.
- `cases/exercises/ARC-*` are scale re-authoring records, not arcs.

## 4. HOW THE PIECES RELATE
| object | side | written by | read by | state |
|---|---|---|---|---|
| Arc register (55) and `cases/` | **outside the sim**: calibration and test corpus; "never runtime data" (B10-19:93) | the archive | `harness/arc.py`, `corpus_run.py` | data BUILT; arcs feed ladders (DECIDER/ROLL), scenarios (NEVER, 10/14/18) and Tensions |
| NPC arc maps (archived A/B/C; Vaynard A/B empty) | content only. Their state-machine triggers are [RETIRED] | Jordan | — | transcribe as goal rows and ladders |
| Goal rows and thrust ladders (`goal_stages`) | **person-side**: attention order; `current_stage` read from the person's own ledger | authored | the `need` question | 38 goal rows BUILT; ladders: schema planned (B10-05), content 0 |
| Tensions and scenario rows | **world-side at build**, then **person-side** opening and beats | authored | `build_realm`, the chooser | planned / proposed |
| World forcing | world-side, actorless, writes no outcome | the engine (AX-5) | persons, via claims | BUILT (control 1.0) |
| Chronicle, journal, coherence tiers | **render, outside the sim** | — | the reader | chronicle BUILT; journal and tiers DESIGN, no consumer |

## ESCALATIONS
1. **Build a world Thread substrate?** It turns "misunderstood" into "dying" and unlocks 7 arcs, including all four LOST. Recommendation: yes, as a MATTER condition on Thread sites (the `Site.condition` and `condition.band_crossed` precedent). No fourth motion.
2. **Tenth attribute = TS (J-T2).** It unlocks family G (12 arcs). Recommend TS (it has readers).
3. **Who authors scenarios and ladders?** B6.n is "Jordan's content, no builder". Recommendation: an author lane transcribes the roughly 60 seeds as `[ASSUMPTION]` rows, each with its own revert. Jordan vetoes rows rather than writing them.
