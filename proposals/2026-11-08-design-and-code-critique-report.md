# Design and code critique: categorized findings, adversarial results, suggestions

## Status: FILED — reference, not canon (CLAUDE.md §0.05). A one-round review record (CLAUDE.md §0): its suggestions are proposals, and none enters the plan or a ledger until Jordan so rules. If this file were deleted the game would behave identically.
## Date: 2026-11-08 · Lane: IN (cross-cutting) · Written against `f94043d`
## What changes in `engine/season/`: nothing.
## Filed because: Jordan asked for the report to be committed (2026-11-08). CLAUDE.md §0 otherwise bars a standing review record with a suggestion queue; this is one file, in `proposals/`, with no directory, and the rulings it led to are in `registers/editorial_ledger_in.jsonl` ED-IN-0353 to 0357.


## 0. Summary, method and the rulings recorded

1. **Five rulings are now in the ledger** (ED-IN-0353 to 0357; `next_free` is 358). They close the four design ambiguities the critique called for and settle the Queen's intent.
2. **The canon timeline's Schoenland text was corrected** (section and the 238 AG row), because the ruling contradicts it directly.
3. **The Queen's code change was not made.** Remit is a snapshot taken at seating, so a grant contingent on another seat's vacancy is not a data edit. ED-IN-0357 records the three options and recommends one; it needs a go.
4. **Grades**: the rulings tighten the design (fewer contradictions) but build nothing, so the grades did not move.

Net: the critique's structure held; about nine institutional and interaction claims were wrong or stale and about ten overstated; the design is denser than first read, and the runtime lags it in specific places.

## 1. Rulings recorded

Renumbered after merging main: another session landed ED-IN-0352 (flow conditioning, #595), so these five are ED-IN-0353 to 0357.

| Id | Ruling (Jordan's words) | Supersedes | Still open |
|---|---|---|---|
| ED-IN-0353 | "One parliament." | The two-parliament conflation (Court Parliament at T1; Hafenmark's at Gransol) | Seat and membership: assumed Valorsplatz; membership derived from rung and service deed [ASSUMPTION, reverts stated] |
| ED-IN-0354 | "Transnational church." + option (a): the Holy See at Himmelenger (T9) | faction_politics_v30's "off-stage … GM-determined" concurrence | Church persons abroad; binding by oath, not rung containment [untested] |
| ED-IN-0355 | "15 territories." | ci_political_v30's "11 of 15" | Which 15: assumed T1–T14 and T17 [ASSUMPTION]; the victory selector counts Askeheim and needs reconciling |
| ED-IN-0356 | Schoenland is a neutral offshore trade nation that trades with both sides in war | Timeline's "spoiler … tension-stoking … GM-driven"; hierarchy document's "tributary" | Seats and goals; whether neutrality needs a cost of seizure; rosters note on naval passage |
| ED-IN-0357 | "Queen is widow regent or whatever" | The unconditional five grants (a normalization artefact) | Mechanism: three options, option 1 recommended; design-first, not in the plan |

Housekeeping forced by the 120,000-token ledger cap: three resolved, uncited rows (ED-IN-0268, ED-IN-0270, ED-IN-0272) moved to the archive, the cap's designed relief valve.

## 2. Corrections to the session critique (the first-pass claims the adversarial round overturned)

| # | Was | Now |
|---|---|---|
| 1 | 104 fight formations, 74 same-faction | **STALE.** CR-87 landed; `fight` formed 0 in my aperture run |
| 2 | 46% refused | 40.3% did not execute (331/821); 46 acts count as both |
| 3 | CI loop is an attractor with one brake | Several brakes (±5/season cap, seizure fails with no second attempt, exposure −3, duress −5, floored votes); CR-89 supersedes v30; loop not shown closed |
| 4 | Templars and Löwenritter are one Praetorian mechanism | **WRONG.** Jarnstal's arm refuses political deployment; the Split is built via FA-04/FA-07 |
| 5 | Few relief valves | **WRONG for the design** (penance, banishment, Grand Debate, appeal, recognition fork, Stay, appeasement transfers); runtime has `appeal_basis` and `pardon` closing a `ban` |
| 6 | No runtime counterpart to faction ethics | Transposed to person-level descriptor axes; the faction-level Ob modifier is a deviation |
| 7 | Cross-faction surface narrow | Also `oblige` vassalage and holdings revocation, but holdings revocation is inert at build |
| 8 | 31 seats, 16 unrevocable | A rungless guild-leader seat makes 34 in the realm; 25 of 31 authored seats strippable by nobody at build [critic-reported] |
| 9 | Parliament least built | Overstated: CR-36/37/38 planned; Guilds and the Restoration Movement are thinner |
| 10 | Research reach ≈ 0 | A runtime-file citation count is not reach; about 100 proposals cite `research/` [critic-reported] |
| 11 | Rule conflict (§0 vs research) | **Retracted** |
| 12 | Verifiers "non-discriminating" | Needs a control |
| 13 | "Managed decline" | A 45-year-old settlement on borrowed legitimacy, second-generation ruler, under ratcheting strain |
| 14 | Faction-as-view is distinctive | In degree, not kind |
| 15 | 203 positions in 20 | 186 in 19 at v11.md:130; falls as batches close; 160/15 unconfirmed |
| 16 | Player-facing F | F for this repository only |

## 3. Findings by category, classified (updated)

| Institution | Design intent | Code status | Class |
|---|---|---|---|
| Crown | Rebuttable deed-presumption; consecration | King by `inheritance`; Queen holds five grants unconditionally | Consecration PLANNED (CP-T09-09, inferred); Queen **RULED (ED-IN-0357), build open** |
| Church | Four Cardinals; transnational; Holy See at Himmelenger | Holy See body, elected Confessor, four Cardinals at T9; seats irrevocable | Placement **BUILT and now RULED** (ED-IN-0354); irrevocability DEVIATION BY RULING (2026-10-11); concurrence PLANNED (CR-37); Church abroad NOT BUILT |
| Löwenritter | Layered loyalty | Split built via oath; Grand Master irrevocable | BUILT / DEVIATION |
| Parliament and Hafenmark | One parliament | "Court Parliament" body still holds no seat; Duchess has no conferral route | **RULED** (ED-IN-0353); PLANNED (CR-36/38); seat/membership assumed |
| Varfell | Jarl Council; Skald-Chief endorses | Duke elected; three council seats | BUILT in part |
| Guilds | Autonomy against state and Church taxation | Comptroller plus `off_npc_084`; `settlement_economy` doc null | Thin; PLANNED |
| Restoration Movement | Insurgency pipeline | One Leader seat | PLANNED |
| Altonia | Military and treaty tracks; marriage and tutoring levers | Two foreign seats behind `foreign=True` | BUILT in part |
| Schoenland | Neutral offshore trade nation | Root rung T16, no seats, no leader | **RULED** (ED-IN-0356); seats NOT BUILT |
| Territories | 15 | Geography carries 17 | **RULED** (ED-IN-0355); which 15 assumed |
| Ministries, Rectorates, Praefectures, Imperial Court | Executive and judicial organs | Bodies without seats | UNEXPLAINED |

Defects the aperture run surfaced: `challenge` fails 43 of 48 on a wrong-collection subject so `accept` refuses 17 (`exists:challenge=0`); 103 of 821 attempts fail the kind check; 106 of 167 declared event kinds never emitted. ED-IN-0292 says no computed `accept` forms until a challenge is `give`n, yet 26 formed: ruled residue or drift is unresolved.

## 4. Lens results

**Originality.** Rare: per-person believed clocks, the regime credit factor, conclusion by terminal moves coded from 102 cases, a doctrine derived from its founder's ontology. Missed precedents: Skyrim, Dragon Age (recalled), Weber, Dune, Mage. Henry VIII and Catherine are authorial annotations. The earlier "delivered D" double-counted implementation.

**Emergent-narrative capability.** Design-side: gates D1–D3, F7 and H pass; F3 and F4 partial; no channel to the player; no dead-referent policy. The arc instrument counts seeds reaching marks, not whether routes differ (B4). Running loop: the story filter is still missing at the read.

**Fidelity.** Sharper referents (recalled): Bruce and Arbroath or Gustav Vasa for the Crown; Elizabeth I for Baralta; Innocent III for the ratchet; the Ottoman patriarchate for incubation; the Althing for Varfell. With the Holy See now at Himmelenger, Baralta's move is closer to Philip IV and Avignon than to Henry VIII.

**Political nuance.** Weber's types are encoded in the ladders; Franchise is a draft; gender, regency and hostage-kin politics were missed; the macro layer is epistemically situated.

**Institutional nuance.** Jurisdictional seams exist; whether the Church is national or transnational is now ruled; missed: succession split and consecration crisis, Church taxation, the insurgency pipeline.

## 5. Grades

| Dimension | Grade |
|---|---|
| Player-facing experience (this repo) | F |
| Scope realism | D− |
| Implementation | D |
| Game concept | C+ |
| World originality | C+ (intent B; delivered depends on implementation) |
| Design rigour | B |
| Overall | D+ (design B−, implementation D, delivered F) |

## 6. Suggestions, with status

1. ~~Settle the four ambiguities~~ **Done**: ED-IN-0353 to 0356.
2. **The Queen's regency** — ruled; build awaits a mechanism choice. Recommended option 1: Queen's seat `remit_acts: []` at build, plus a regency seat claimed through `succeed` with a "while `off_king` vacant" precondition (RS-27's pattern). Realm hash moves; pins re-recorded once per batch; `test_in61_succession`'s control re-read. **Needs your go.**
3. Fix the duel chain's front (`challenge` subject class); settle the ED-IN-0292 question first.
4. Seat or declare nominal the parliament and the Imperial Court, Rectorates and Praefectures; membership by derivation (ED-IN-0353).
5. Build the three-level read layer with perspective-bound chronicles.
6. Validate against held-out stylized facts (tune on three, hold three).
7. Trace the research route for the half-dozen convergent shapes in a commit message.
8. No second audit round.
9. **New from the rulings:** (a) reconcile the victory selector with 15 (it counts Askeheim); (b) give Schoenland seats and trade goals on the existing verbs; (c) model Church persons abroad by oath; (d) decide whether Askeheim healing raises the bar to 16.

Originality and concept (from the earlier expansion): the referent ledger (two or three referents per institution, one altered condition), three engines (capacity licensing; the war-finance triangle with Schoenland credit as an `oblige` tenure; one act, two readings by standing), and three signature patterns with control arms. Each is a design-first proposal needing a NERS pass and layer-conformance before any build.

## 7. Limits

- The aperture figures come from `python -m engine.season.harness.aperture 1 0` (one season, seed 0); the saved output was a session artefact and is not committed, so regenerate it with that command.
- Neither critic ran code; critic A could not read inside `research/` (hook-blocked); A3 (`wc`) unchecked; critic B did not open `aperture.txt`; its analogies are recalled.
- I re-opened corrections 1–7, 15, the Queen note, and the ledger/size/validator results; the 25-of-31 figure, the 160/15 count and the ~100 proposal citations are critic-reported.
- Validators run on this change: ED-citation integrity, register size, claim-provenance, freshness gate, naming, and the two test files that read touched paths (42 passed). The full suites were not run (CLAUDE.md §0.4: a ledger and canon-prose diff).
- `currency_consistency_check` reports `CURRENT.md`'s stamp (2026-11-04) as predating several heads; that drift predates this change and I did not re-reconcile `CURRENT.md`.
