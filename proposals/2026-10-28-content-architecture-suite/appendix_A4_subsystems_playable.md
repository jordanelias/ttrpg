# A4 — Q6: what each subsystem needs to be legible and playable

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Appendix A4 of the suite, an analyst report copied from the session's `analysis/` into the suite at 07:10:35Z. Source: the session's own record of the analysis file written at 06:12:17Z and patched in place (14,198 bytes), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---

**VERDICT (Q6): No subsystem is playable today. The loop runs 83 persons with no seat for a human, and every subsystem fails on the same three things: no seat, no odds before a choice, no account afterwards. One shared play surface fixes most of it.**

Verdicts by section:
1. Principle: the player is the decision procedure of one seated Person. The rule is **parity**: the player chooses what that person's NPC chooser would choose, and nothing more.
2. Cards: only the season loop and social/proceedings have a running verb set worth a menu; the other 8 have no consequence behind the menu, or no menu.
3. Session shape: a season is at most 5 decisions. The first hour is choosing a person, then about 4 seasons. A campaign is one person's line; the client ends it.
4. Top gap: no seat. Cheapest fix: a text client on `dispatching_chooser`, before any Godot work.
5. Taxonomy: player-available, delegable, engine-only, all computed from `verb_table.yaml`, never listed.

State reconciled (verified at source, HEAD tree):
- **Seat unbuilt.** `dispatching_chooser` (`engine/season/harness/play_surface.py:41-54`) has callers only in `tests/test_play_surface_dispatch.py` and `tests/test_combat_trace_returned.py`. v10 renamed IN-46 to REM-31 and IN-47 to REM-30 (`workplans/valoria_master_workplan_v10.md:114`). Both are in batch B10-10 (`_part3.md:200`).
- **Verb table.** 56 rows (`grep -c`). 51 are resolvable (`aperture 2 0`). The errata's 53/47 (D14 G3) was measured at an older HEAD and is superseded.
- **Empty menu fails silently.** An empty candidate set returns `[]` (`decision/choose.py:435-436, :481`).
- **Godot:** `Main.tscn` is one bare `Node`; the client is wired to `KeyStore` [RETIRED] (D13 C-2). **UI v4** jumps Part 9 → 21 (`valoria_ui_ux_v4.md:1504, :1779`). `videogame_mode_spec.md`: 0 hits for controls, tutorial, new game.
- **Superseded:** the UI's clocks chrome (GEN/RS/TC/IP), mandatory Zoom on Stability ≤2, faction Hand/Domain Echo, Duty-from-leader [RETIRED] (ambient tracks and faction turns; no faction turn, S1:343). "Each Wound −1D" (v4.1 §7.1) [RETIRED] by ED-PC-0005.

## 1. The principle — what "legible and playable" means here

**VERDICT:** The player is a person among persons. Legibility therefore means showing what that one person holds, plus the arithmetic of the act they are about to take. It does not mean a narrator's view of the world.

- **Who the player is.** The player is the decision procedure of exactly one seated `Person`: *"for a player character the player IS the decision procedure"* (`architecture/meta/04_CODE_ARCHITECTURE.md:853`). It is not a faction and not a GM. Faction scale is reached by holding seats; scale is carried by the Rung a seat sits on (S1:247, :256).
- **What the player chooses.** Each round, the player makes the same choice the NPC chooser makes: one scene of 1-3 acts (verb, subject, operands), within budget (`deliberate.py:167-170`). A played fight (REM-31) adds intents at six moments: measure, reopen, commit, mode, counter and contact (D9b §2.1).
- **What the engine chooses.** Everything else, by the NPCs' own code: questions, the other 82 persons, release order, dice, degree, MATTER, WITNESS, CENSUS, and the three closed bout moments.
- **What the player is owed.**
  - (a) The person's own claims, rendered as belief: subject, value, source, teller and confidence (03 S-3).
  - (b) The band odds of the act (CP-T01-03 `odds_of`, B10-08).
  - (c) Why an option is absent.
  - (d) What came back: new claims, plus `explain(p, v)` (04:867).

> **THE RULE (recommended): PARITY.** A seated person's menu, budget, admission and resolution are byte-identical to what `make_chooser` would face for that person. A callback that returns `auto`'s pick must reproduce the run's `content_hash`. Presentation (the whole question list, odds, reasons) may be richer; the option set may not.
> The falsifier already exists in the plan: REM-31's exit, *"PLAYABLE-with-scripted-choices-equal-to-the-chooser's end at one `content_hash`"* (`_part3.md:201`).

## 2. Subsystem cards

**VERDICT:** Every card needs the same three readouts (the row's band writes, its odds, its result as claims); they differ only in what is behind the menu.

Key: **B** = row built and runs in loop · **T** = tests only · **D** = designed (CP/REM positions, v10) · **M** = missing. Precedent tags cite digests; others are [FROM MEMORY].

| subsystem | player verbs | rhythm | must be shown | precedent | biggest gap |
|---|---|---|---|---|---|
| **Resolution / dice** | none: engine-only | one roll per contested act, at RESOLVE | pool, Ob, F/P/S/O odds, dice faces, band; refusal reason | Disco exact odds (D6a R4:31); XCOM hit chance; BG3 Karmic Dice rejected (D_T01:21) | no surface shows a chance, and `p_success` is 10-17 points wrong at small pools (R-F11). Fix: `band_odds` (B10-08) |
| **Season / persons** | B: 51 resolvable rows. D: View on any listed question (CP-T02-07) | 5 rounds, 1 released scene each; budget `5 + holds − body − legs` (`budget.py:57-61`) | the whole question list, not top-1 (`first`, fixtures.py:481); budget/rounds left; why a verb is absent | CK3 alerts strip (D_T02 KD7); Old World orders pool (OW2) | no seat (REM-30/31, B10-10); an empty menu is silent |
| **Personal combat** | B: `fight`, `accept`. T: `tend`, Yield. `challenge` writes nothing. D: `capture`, guards (IN-59), duel terms. M: flee | auto (one act), grid, or duel at ENCOUNTER (REM-31) | matchup odds (CP-T03-05); risk to self; wound band; trace as narration | JA2 auto/enter/retreat box (D7b T14:22); Battle Brothers harm kept | the attacker never takes a band: a fight is risk-free (CP-T03-00, B10-09) |
| **Mass battle** | B: `march` (only refusals run). D: `marshal`, `besiege`, `surrender`, retreat, `field_estimate`; raising a force on Ask A. M: decide at contact | declare at RESOLVE → field at ENCOUNTER → 18 engine ticks | `field_estimate`; side as persons at weight; walls; why it was won | Dominions orders set before battle (T17); FoG2 odds from 1000 samples (D04:L32); squad v5 RULED as a layer | 0 fields fought at seeds 0-2; the army is whoever lives at home (`sides.py:115`) |
| **Social / Proceedings** | B: `tell`, `utter`, `petition`, `open_case`, `convene`, `speak`, `determine`, `commit`. T: `carry`, `argue`. D: `interrogate`, `persuade`, `vote` (J-4) | file → docket date → hearing → verdict, across seasons | the docket (matter, date, bench); proofs held; what the character holds of the room — *"a room whose mind they cannot see"* (07_THE_GAME:13) | Griftlands hand; Suzerain visible increments (D7b T11:126) | the verdict reads nothing: pool 2 vs Ob 2 for every party (VT:384). Fix: CP-T05-01/-02 |
| **Fieldwork** | B: `research`, `surveil`, `interview`, `reconstruct`, `survey`, `forge`, `conceal`, `create_record`. `examine` formed, all refused. D: `shadow`, `bribe`, a charge with a price | an act per lead; claims at WITNESS | journal of belief; *"is there more to find"* (FW-C O5) | Obra Dinn; Shadows of Doubt payouts (R5:L33); L.A. Noire completeness | `finding.none` goes to nobody, the actor included (FW-C:21): failure teaches nothing |
| **Threadwork** | B: `thread_read` row (writes `[]`, never formed). D: `weave`, `lock`, `mend`, `ward`, `knot` (CP-T07) | Leap → working → charge → rest | Coherence felt before the breach (CP-T07-07); exposure | Darkest Dungeon II stress fork; Sunless Sea Terror bands (D6b §5) | the oracle is not called by the loop: a practitioner's first season is empty (TW-T:87-88) |
| **Settlements / economy** | B: `confer`, `revoke`, `issue`, `requisition`, `transfer`, `release`. T: `work`/`restore` (no natural Site), `found`/`build`. D: levy edict (CP-T08-07), `craft`, `exchange` (REM-2B) | MATTER yield/draw once per season | stores and hunger per place (REM-50); what this seat's remit allows | Manor Lords approval tiers; Frostpunk Hope/Discontent; Patrician supply diamonds (D6b) | the spine never binds: yield has no labour term and `body_step` 0 means hunger hurts no body (08 G1, G3). Governing has no felt cost |
| **Factions / war** | B: `covenant`, `commit`, `release`, `seize`, `give`, `oblige`. `dispatch` writes nothing. D: `declare`, `conspire`, `recruit`, `defect`, `pledge` | edges open and lapse at MATTER | who stands with whom; wars and treaties as committed Propositions; vacant seats and claims | CK3 factions, casus belli and succession; Pax Pamir (09 §0) | no succession: IN-61 stopped on H-230, and 7 seats can never refill (R-F1). The realm cannot survive its ruler |
| **World / NPC life** | B: `move`, `forgive`. T: `migrate`, `tend`, `train`. D: route-priced travel (CP-T10-01), `marry`, kin, estates. `explore` parked (P-2) | a leg costs 1 budget until MATTER | map with route cost; body bands; ties; the year (CP-T10-03) | Sims 4 neighbourhood stories (D6b) | distance is free: every destination is one leg, and the map has no reader (WT-C A) |

## 3. Session shape (proposed; minutes are [ASSUMPTION: 1-2 min per decision])

- **First hour.**
  - Pick one of 4-6 curated named persons from the 46. The cast is closed (ED-WR-0011), and REM-30 makes creation *"a cast entry the world-gen builder seats"*. Precedent: CK3 or Suzerain, not a free build.
  - Read the person's one sheet (09 §2) and their opening question, which is a `need` from their own ambition (S3:212).
  - Then play about 4 seasons. Seat-holders die by `fight` early (aperture seed 0: 3 deaths, 2 seat-holders). The first big choice is therefore a vacancy, which needs IN-61.
  - Directive 8: draw one authored opening **Tension** per game as world-gen content (a Date, seeded claims, a filed petition). It writes occasions, never outcomes; precedent: the build-time OUGHTs (`populated.py:560`). It answers the *"sit and wait"* equilibrium (early_game_ignition §1).
- **A season (about 10 min).**
  - Read the CALENDAR/MATTER notices.
  - Make up to 5 decisions. Each shows the question list, the menu cards and their odds.
  - A played fight may suspend the loop at ENCOUNTER.
  - The season report is the person's new claims, plus `explain`.
- **A campaign.**
  - It runs 30-50 seasons (v4:166) and is one person's line. On death, the client re-binds to an heir or sworn tie (CP-T02-06).
  - It ends when the line is extinct, the player retires, or `endings_reached` returns a row. **The client ends it; the engine halts nothing** (`rosters.yaml` endings).

## 4. Top 8 gaps, ranked, with the cheapest fix

1. **No seat.** Fix: a stdin/HTTP text client over `dispatching_chooser` for one person, like `agon_harness`. The parity test already exists, and no Godot is needed.
2. **No odds at the point of choice.** Fix: `band_odds` and `odds_of`, display-only and hash-equal (B10-08).
3. **The menu names verbs, not consequences** (S1 §6 #1). Fix: render each candidate's row (`requires`, `writes` by degree, `emits_on_refusal`) as its card. The data is already in `verb_table.yaml`.
4. **Only the top question is seen** (`first`). Fix: hand the callback the full `questions[p.id]` list, and CP-T02-07.
5. **Silent nothing.** An empty menu returns `[]`; `finding.none` reaches nobody. Fix: a read-only drop-reason trace in `opening_set` (*"nothing to do here, because…"*); deposit `finding.none` to the actor.
6. **No stake or end.** Endings are never reached and seats are never refilled. Fix: the client-side end conditions above, plus CP-T02-01/-02 → IN-61.
7. **Acts cost the actor nothing** (a free fight, a free broken promise, H-205). Fix: CP-T03-00 first.
8. **No season account.** There is no wire format for a season (01 §1.2), and `chronicle` sits outside the loop. Fix: the ledger delta since the last deliberation is the log. Do not build a second journal.

## 5. Verb menu taxonomy

| class | membership rule (computed from `verb_table.yaml`, never listed) | today |
|---|---|---|
| **Player-available** | the seated person's `opening_set` forms it: eligibility (`own`/`remit`/`hold`/`presence`) ∧ in `resolvable_verbs()` ∧ not withheld | identical to the NPC set: 41/56 eligible unseated, 56/56 for the King (aperture) |
| **Delegable** | the player causes another person's act through a `binding_decision` edge (`dispatch`, `issue`, `confer`, `oblige`). The delegate's own chooser picks, and the result returns as claims. This also covers fidelity delegation (an auto-resolved fight) | `dispatch` writes nothing yet (09 G8) |
| **Engine-only** | has no chooser: moves inside a resolver (parry, rally: "scene moves", verbs-03 S-1), MATTER/CALENDAR/CENSUS motions, and outcomes (kill, wound, endure: ED-IN-0288) | — |

The rule: **no verb exists only for the player** (the analogue of `verb_table.yaml:34`). A lexicon name enters a menu only when it gets a row: of 128 names, 52 have one.

## 6. Decisions taken (each with its reason)

- **Parity** is the binding play rule: answered by architecture (04:853), and the plan's exit tests it.
- **Text client before Godot:** the Godot repo is a scaffold on retired substrate; CLAUDE.md §6 blocks the port.
- **The Slate is the built `questions_for` list, shown whole;** the ARCH Slate's clock-band steps are [RETIRED].
- **Fights use three fidelities on one resolver,** auto by default; the player plays only their own person's fights. Reason: ED-SC-0013 RULED; duel mode keeps 3 closed moments (05 §4.2).
- **Start from the cast,** not a free build. **The client owns campaign end.** Reasons: ED-WR-0011; REM-30; the endings row halts nothing.

## 7. Escalations (2)

- **E1. True odds or held arithmetic?** AX-7 says *"No state is hidden from the player"* (`01_AXIOMS.md:301`). 04 says the engine owes *"the ARITHMETIC of what the character already holds, and nothing else"* (`04:858`). v10 took true odds (CP-T01-03 mode (a)). I recommend v10's reading: show true band odds, and narrow 04's clause to world facts (who did what, where), not roll arithmetic.
- **E2. Does the player command a battle after contact** (K-MB-4, J-C-31)? Live command is Total War; plan-before is Dominions. Recommend plan-before plus a general's duel zoom (squad v5 §6.6): one resolver, seat-only control.
