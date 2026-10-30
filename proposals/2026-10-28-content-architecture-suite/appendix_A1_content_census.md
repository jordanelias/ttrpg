# Appendix A1: content census (analyst report)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Appendix A1 of the suite, an analyst report copied from the session's `analysis/` into the suite at 07:10:35Z. Source: the session's own record of the analysis file written at 06:09:33Z (14,161 bytes) plus the three-lens note prepended by the sweep at 07:28:11Z (14,549 bytes), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---
> **Note (three-lens review):** (1) the refusal figures quoted here are withdrawn (see 07a); (2) "an unseated person has 45 of 56 eligible, none seat-gated" (E3) is superseded by part 04 §1: 41 rows every person has, plus the seat's own; (3) "appointing starts at a duchy seat" is false: which orders a seat offers depends on its remit list (the Confessor holds `confer` and `revoke`).

# A1 — Q1: world / character / narrative content in the game as coded

Repo HEAD be24c71 (B10-02 closed). Counts re-measured this session (`build_realm(0)`, YAML loads, greps); digest-only items are marked.

## VERDICTS (head)

| Layer | Verdict | One line |
|---|---|---|
| 1 CARRIERS | **partial** | Strong for persons, offices, tenures, information; absent for kit, troops, events, bonds, text, arcs. |
| 2 CONTENT | **thin** | A real cast, map and org chart; nothing that makes two seeds feel different; no events, no stories. |
| 3 PLAYER SURFACE | **none** | One test-only callback seam. No client, no wire format. The Godot repo is bare shells on a retired substrate. |
| 4 NARRATIVE TEXT | **none in the game; adequate as an out-of-game voice spec** | One instrument prints `n. season s \| actor verb \| emitted kinds`. The prose-writer skill and Rendstad are authored text wired to nothing. |

**Does workplan v10 contain a path to a playable slice? No.** It reaches a clean, ported simulator. "Vertical slice", "playable slice" and "first playable" return zero hits across `workplans/`, the v10 proposal folder, `CURRENT.md`, `HANDOFF.md`. It schedules no client, no un-HELD text layer, and no content authoring (section 6).

---

## 1. CARRIERS — partial

**EXISTS (BUILT, measured).** `build_realm(0)`: 83 persons (46 named, 37 cohorts), 32 offices, 412 rungs, 322 sites, 683 tenures, 67 Propositions, 0 Records. Verb table 56 rows / 58 names; 51 resolvable, 5 not (`construe`, `evade/defy`, `exchange`, `succeed`, `tie/knot`); 40 `@effect_for` registrations. Person: `id, name, weight, capability, stance, pursuits, ledger, body, born, scar`, plus `tenures`, `travel_leg` (`state/carriers.py:655`). CALENDAR fires `World.dates` when `due_at` arrives (`loop/calendar.py:39`); only `convene` writes them (`loop/effects_governance.py:413`).

**MISSING, ranked.**
1. `Person.capability` is empty on 83 of 83 (measured): every pool is the default 2. No attribute carrier (CR-20), heritage (CR-30), coherence or TS on `Person`.
2. No event carrier: no deck, card, omen, incident (0 hits in `engine/`, `modules/`). `season_factor_draw` ships `()` (`data/fixtures.py:469`).
3. No text-bearing record kind (NM-W4 UNBUILT). `Event` is a state-change row (`carriers.py:232`).
4. No kit, tradition or troop carrier; no subfaction; `tie`/`knot` declined (H-182); no companion mechanic (0 hits).
5. No arc or stage carrier, by ruling (ED-603/604/605). CL-THRUST stages are scheduled as data, HELD.
6. No births: closed cast of 46 (ED-WR-0011). AX-5 (`architecture/meta/01_AXIOMS.md:164`) lists three self-moves only: MATTER, bodies, fading memory.

**Scheduled (a):** CR-20/30/33 (B10-10), CL-EVENTS (B10-05, B10-18), IN-32 (B10-15), CP-T10-06 kin edges (B10-18). Troops HELD on M3.

---

## 2. CONTENT — thin

| Content | Count (measured) | Note |
|---|---|---|
| Named cast + 37 cohorts (no pursuits) | 46 (35 canonical, 11 proposed) | `references/npc_registry.yaml`; 36 carry a non-empty `arc_trajectory` |
| Offices | 31 authored + 1 derived = 32; 2 foreign seats shipped off | derived split from D3e |
| Factions | 10 in roster, one the placeholder `faction x` | a view over `commit` tenures; no entity |
| Provinces / settlements / terrain | 17 / 37 / 20 | 74 `description:` strings; 31 POIs counted, unnamed |
| Goals | 38 | 24 `orientation` (mint no Proposition); 14 object-bearing |
| Buildings / arrangements | 42 / 8 | `venues.yaml` "Not canon" |
| Pursuit vectors | 46 persons | weights `[ASSUMPTION]`; cohorts 0 |
| Endings | 2 | H-176: none shown reachable (`hole_register.yaml:3972`) |
| Attribute values | 1 of 46 cast rows | and its keys do not match the 9-attribute roster |

`register --requirements`: met 3, partial 5, not_met 1 (R-05). [run this session]

**Stale parallel set (D13, spot-checked).** `valoria-game` has 22 character `.tres`, 15 trigger `.tres`, 8 factions, 17 territories, 36 settlements (37 in the engine); no GDScript reads any engine export; the 13 `trajectory_script_path` targets do not exist; 9 of 17 trajectory evaluators are `pass`. Scaffolding, not a content source.

**Designed, not built (archived):** 20 named NPC arcs across 5 NPCs (two bodies empty); 55 numbered arcs; Tensions cards (6 or 8, sources disagree); miraculous event and insurgency pipeline (never fired). `narrative_engine_design_v2_churn.md` (still listed at `CURRENT.md:35`) is built on the [RETIRED] Key substrate.

**MISSING, ranked.**
1. Anything that varies by seed beyond dice: events, weather, Tensions, SE-06 temperaments.
2. Attribute and capability values for the 46; heritage; lifepath key map.
3. Referent-bearing goals: no seat-attached goal binds anyone (G-09); thrust axes B, H, I, J have no rows (G-26).
4. Named POIs; relational edges (spec has no code).
5. Authored storylines. The 50 `ARC-NN` records in `cases/` are a test corpus; the chain files are fenced and do not parse as YAML.


---

## 3. PLAYER SURFACE — none

**EXISTS.** `harness/play_surface.py::dispatching_chooser` hands named persons to a callback; exercised only by tests. The callback sees `(Person, View of last 12 claims, Sensation, budget, auto)`; DELIBERATE refuses over-budget or foreign-actor returns. `fight` returns its trace (`seam/wrappers/combat.py:252`).

**Godot repo (verified):** 8 `.tscn`, each one bare node; `scenes/ui/*` empty; `assets/` and `dialogue/` only `.gitkeep`; KeyStore autoload live [RETIRED]; HEAD 6b0df3d (2026-08-19); declares 4.3, README says 4.6; its 289 tests are excluded from CI.

**Designed (archived):** UI v4.1, Scene Slate (3-5 actions/season), Zoom In/Out, played/witnessed/auto resolution. None is code (Slate, Zoom, Domain Echo: 0 hits). The "22 mandatory triggers" and 7-scene walkthrough are cited and not found.

**MISSING, ranked:** (1) a client showing the person's ledger and taking an Act; (2) a serialised season; (3) player-side odds (CP-T01-03 (a), PROPOSED); (4) human character creation (REM-30, scheduled); (5) save/load, menu, onboarding; (6) art, audio, chrome.

---

## 4. NARRATIVE TEXT — none in game

**EXISTS.**
- In game: `harness/chronicle.py::render` (:115) prints the deepest cross-person chain as `<n>. season <s> | <actor> <verb> | emitted <kinds> | answers <m>`. Observer only, wired to no gate. 55 of 66 deepest-chain acts are refusals (G-27).
- Out of game: **prose-writer skill** (SKILL.md 219 lines, 19 reference files; five coherence tiers 10-8 / 7-5 / 4-3 / 2 / 1 plus external-focalization tier 0; 12-author weight tables by TS band; the 10-8 table is `[ASSUMPTION]`). **Rendstad**: 7 scenes, 192 lines (T7; Church assessor vs Hafenmark sub-prefect over a folk practitioner; coherence 9, 7, chronicle, 4, 7, 7, 10). No ending, no machine-readable slots (D15).

**Structural gap.** The skill selects voice by PC coherence, TS and Spirit. `Person` carries none (coherence waits on CP-T07-02, B10-15; attributes on CR-20, B10-10). Text written to the spec cannot yet be selected by engine state.

**MISSING, ranked:** (1) text-bearing record (NM-W4); (2) focalized journal (NM-W5, HELD on NM-W1); (3) fragment bake, scale lines (NM-W6/W7); (4) occasion ladder (NM-W8); (5) authored fragments per pattern. B10-19 "Builds nothing" (`-09-build-B10-19.md:56`). Milestone M2 is "carried by" it, as "a reading and not a pass condition".

---

## 5. WHAT BLOCKS A PLAYABLE GAME SOONEST

"Playable slice" here: one human plays one named person through N seasons, sees in words what that person knows, picks acts with legible odds, sees consequences and an end.

| # | Blocker | Kind | v10 status |
|---|---|---|---|
| 1 | Client over the `choose` seam + wire format | **c** | Unscheduled. "Nothing here proposes a player-facing client" (S4). |
| 2 | Refusal: 67% of resolved acts refuse; 16 of 48 attempted verbs never succeed | **a** | B10-04..08. Largest scheduled block; a player meets it on turn one. |
| 3 | Words for own knowledge and results | **a/c** | NM-W1/W5 HELD; fragments unscheduled |
| 4 | A playable person: attributes, capability | **a**+**b** | B10-10; values for the 46 are Jordan's |
| 5 | Odds at the point of choice | **a** | CP-T01-03 (B10-08); no surface (c) |
| 6 | Stakes: halting ending, loss state, time box | **a/c** | H-176; CP-T09-04 (B10-17); no loss state designed beyond GD-1 |
| 7 | Seed-varying world pressure | **a**/**b** | CL-EVENTS ships off; values Jordan's (M16) |
| 8 | Freestanding storylines | **c** | None. CL-THRUST HELD on content |
| 9 | Bonds, companions | **a**/**c** | IN-32 (B10-15); companion unscheduled |
| 10 | Menus, save/load, onboarding, art, audio | **c** | Unowned |

**(a) scheduled engine work:** the B10-04..18 spine and its carriers. **(b) Jordan's content** (head §7 item 6, `valoria_master_workplan_v10.md:129`; ED-649 "invent no content"): attribute values of 46; weather values; CL-THRUST ladders; heritage beyond two; ladder/seat map; lifepath key map; Tensions content; arms inventory. **(c) nobody provides:** client; text layer past HELD NM rows; fragments; freestanding storylines; loss state; companion mechanic; save/load, onboarding; art/audio owner; POI names; a rule for what ends a slice.

---

## 6. PATH TO A PLAYABLE SLICE IN v10: none

**Schedules toward it:** REM-31 (played fight suspends at ENCOUNTER; exit "PLAYABLE-with-scripted-choices equal to the chooser's end at one hash"), REM-30 (character-sheet space), CP-T01-03 (true odds "for the player's Act interface"), CP-T02-06, CL-EVENTS, B10-20 (exporters, pins, freeze).
**Does not:** any client; serialised season; un-HELD text layer; content authoring (by design); a halting ending; R-05 ("not in v10"). M3 Godot "begins at B10-20", after eighteen serial batches, in a repo that reads none of the engine.
**Plan's own grade:** "v10 cannot make all nine `met` by building what it lists" (head §3). Code report: "a deterministic, well-tested simulator of a lawful society, and it is not yet a game."

**Repair, one position: "B10-S", after B10-10, before B10-11.**

| Field | Value |
|---|---|
| Client | text-first Python over `dispatching_chooser`; no Godot |
| Person | one seated mid-rung holder (E3) |
| Screen 1 | "What I know": last 12 claims as tier-10-8 fragments, source and confidence kept |
| Screen 2 | `opening_set` candidates (5-9) with `odds_of` band odds |
| Screen 3 | act, degree, what was witnessed; refusals in plain words |
| Stop | PC's line ends (CP-T02-06 / IN-61) or season N (default 12) |
| Control | scripted-callback-equals-chooser hash test (REM-31 pattern) |

---

## 7. FREESTANDING STORYLINES (Jordan's directive)

**Finding: the architecture already permits them without bending the person rule.** AX-5 / T-c (`01_AXIOMS.md:164`, `:376`) forbid an *unwound* clock; they allow a clock "wound by a nameable act", and "a world-generation roster is not a clock and is lawful". A **fuse** wound at world generation by an authored row has handles (burn the Record, kill the holder). It needs no amendment and is not M16's refused "fourth motion", provided it writes only a *situation* (a dated Docket item, Record, Claim, Proposition), never standing or a seat. Persons write every outcome.

**Hooks present:** CALENDAR fires `World.dates`; CENSUS individuates a person a demand names; the Tensions receiver is already planned as "a world-generation draw"; NM-W8 offers "authored boot-time rows". Missing: the rows and a seed-indexed draw.

**StoryPattern row (menu for `engine/season/storypatterns.yaml`):**

| Field | Meaning |
|---|---|
| `id`, `scale` | hearth to realm |
| `roles` | slots bound by query to *existing* persons (office, faction, place); unbound = does not fire; cast stays 46 |
| `precondition` | query over rungs/sites (e.g. a Church and a Hafenmark seat both reach T7) |
| `fuse` | dated Docket/Record/Claim/Proposition writes at build |
| `question` | the OUGHT Proposition each role holder answers |
| `exits` | predicates over persons' acts only (closed set) |
| `fragments` | text slots by focalization and coherence tier |
| `draw` | weight; k of the pool drawn per seed, so seeds differ in *which* stories exist |

**Seed pool from existing authored matter:** Rendstad jurisdiction fuse; Disputed Succession; Feldmark Famine (the one Tensions card all sources share); Heresy at Himmelenger; Border Incident at Ehrenfeld; Guild Fracture. Three drawn of six gives 20 combinations before roles vary.

## 8. DECISIONS TAKEN

- Code arbitrates counts (83 / 46 / 67; D3e's 64 Propositions is stale).
- `valoria-game` is scaffolding: retired substrate, different register. The slice runs on the Python engine.
- Fuses are world-generation-wound, drawn per seed, roles bound to existing persons: the right option for AX-5 and the closed cast.
- A slice ends on the PC's line or a time box, using scheduled CP-T02-06.
- Text-first client precedes the port gate: sequencing, but it adds a position to a RATIFIED plan (E2).

## 9. ESCALATIONS (3)

- **E1. May agents draft `[ASSUMPTION]`-tagged content (attribute values, Tensions text, pattern fragments) for you to edit, despite "Content is not the plan's to author" and ED-649?** Otherwise blockers 4, 7, 8 wait on your authoring time and emergent range stays "unmeasurable, not zero". Recommend yes: drafts only, each with a stated revert, as the plan already does for Tensions.
- **E2. Do you add B10-S to ratified v10 ahead of the port gate?** Otherwise nothing a human can play exists before B10-20. Recommend yes, on the Python engine.
- **E3. Does the first playable person hold a seat or stand unseated?** Seated gives the strategic verbs (an unseated person has 45 of 56 eligible, none seat-gated; a ruler 56) and stakes; unseated is a personal-scale game without governance. Recommend seated at rung 1-2 (Lord Steward or a Cardinal), since the thesis is the join between scales.

[ASSUMPTION: six patterns give enough variety - basis: count of existing authored Tensions and arc material; untested]
[GAP: whether a boot-time Date can be written without an act's token - only `convene` writes `dates` today; read the build path before B10-S]
[CONFIDENCE: medium - plan parts 6 to 14 read via digests and part3 cards, not in full]
