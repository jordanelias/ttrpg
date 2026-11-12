# GO — disposition of the player-facing design references: what survives as a test, what is dead, and two owner edits

## Status: PROPOSED

Carries `audits/11_GO_audit_addendum_B.md` F-GO-13, F-GO-14, F-GO-20, F-GO-21 and resolutions R48,
R49, R58, R59, R66–R71, R75. Lane: GO. It adds no file, guard or corpus, edits nothing under
`.designs/` or `.audit/` (both stay quarantined and unloaded), and extends, without replacing,
`11_GO_pointer_and_stale_text_resolutions.md` (TEXT).

## What it changes in `engine/season/` at runtime

Nothing. Two sentences change at their owners under `godot/`.

## The problem, with evidence

A porter looking for "what the player sees" finds three bodies of text and no code:

1. **The UI design set** (`.designs/systems/ui/reference/`, ten files, 433 KB). The newest document,
   v4.1, is by its own Status line a supplement to v4 and defers to v4 for content in at least
   eleven places; the v4 file in the tree stops at Part 9 and resumes at "§20.3 … continued"
   (`valoria_ui_ux_v4.md:1713-1714`), so Parts 10–19 and §20.1–§20.2 (the integrated loop, faction,
   settlement, character and party management, Parliament, the Inquisition hearing, treaty, the
   clock column, the cutscene system and two feel layers) are in no file. v4.1's own audit lists 69
   findings, twenty blocking, including two HUD tracks ("CD", "Taint") the threadwork design had
   already deleted; the thirteen-stage repair plan ran one stage. The whole set renders objects the
   season loop does not have: seven phases, a faction stat vector, card hands, four global clocks, a
   ten-step exchange with a Conviction track.
2. **`godot/godot_architecture_specification.md`** (998 lines, STALE REFERENCE by its Status line,
   which nevertheless says "The GOVERNING spec for the port is `godot/godot_conversion_strategy_v1.md`").
   Read against Layer 1 §C.12 it contradicts three of the five rejections and two type rulings
   (addendum §B5).
3. **The cross-cutting documents** under `.designs/systems/_architecture/reference/`. `engine_atlas_v1.md`
   anchors every claim to a driver that is gone (`engine/mc_v18.py` does not exist;
   `references/ENGINE_ATLAS.md` does not exist). `throughlines_complete.md` T-30 makes the gap
   between what the player sees and what the character knows "the gameplay" ("Church sees miracle;
   player sees Mending"), which is the opposite of the UI set's Oath II test 3 and of ratified §C.11.

## The resolution, decided

**None of the three is reconstructed, repaired or re-pointed. The oracle's typed readings
(`11_GO_player_surface_contract_B.md`) are the specification of the player surface; a new interface
design is a proposal written against those readings when a client exists.** Ladder: step 2 for the
missing and dead text (its subject, the board-game season, was retired; `CLAUDE.md` §0.05 keeps the
documents as reference and licenses no deletion); step 3 for each conflict (§C.11 and §C.12 are
ratified and decide it).

### What survives, as tests of the contract (intent read, nothing loaded)

| from | rule | how the contract meets it |
|---|---|---|
| UI v4/v4.1 Oath II, test 1 | no control for a capability the character lacks: absent, not greyed | `opening_set` forms only what the person may attempt; a `WithheldRow` exists only for an own-state conjunct |
| Oath II, test 3 | nothing the character's perception cannot render | every person-side reading takes no `World`; `receipt` withholds a value he does not hold |
| Oath I | the world stays present at every zoom | the `Situation` is the same record inside and outside a suspended scene; a scene adds a turn view and removes nothing |
| Oath III | a change is shown before it is labelled | a presentation is triggered by an `AccountRow` or `ReceiptRow`, so it can only be about something he has perceived |
| v4 §1.3 / v4.1 §1.2 | no save inside a resolution | the save boundary is the season (MODES §4) |
| v4 §4.3.1, the contest walkthrough §0 | the player sees the numbers before he commits | he sees his **believed** odds (`OfferRow.odds`) and his own operands; a resolver-side operand (the bench's regard, the opponent's score) only as far as he holds a claim about it. The walkthrough's stronger rule ("every number the resolver uses") is refused by §C.11 |
| v4.1 max audit, Part 0 | an inventory of playable moments, each asked: what is seen, what may be declared, what is learned | reused as the per-subsystem table of addendum §B3 |
| cogload target | one named choice where two binary ones were | a module's exported choice set carries `name` and `text` (MODES §3) |
| narrative-engine design v1 (`.audit/2026-07-05-…`) | "why-you is always a citable edge"; no arc label ever surfaces; a ceiling on what is surfaced, never a floor | `OfferRow.occasion` and `AskedRow.claim` are the citable edge; no reading carries an arc; the cap is the client's and removes nothing |

### What is dead, and is not to be built from

The seven-phase state machine and its timings; the Scene Slate as a generator (the loop's
`questions_for` is what produces occasions); the faction hand panel, Domain Action flow, Domain Echo
table and Framework Drift strip (a faction is a resolved view and does not act); the four global
clocks as stored tracks (a stored aggregate is ruled out, PART D); the Conviction track and the
ten-step exchange; the hex grids' stated sizes; the 22 mandatory cutscene triggers (not in the tree);
T-30's player-side omniscience; the single campaign-wide generator ("all rolls … draw from the same
sequence", `valoria_ui_ux_v4.md:2392-2400`).

## Exact edits, by owner

1. `godot/godot_architecture_specification.md:5-8` (its Status line) — old: "retained for its
   pipeline/procedure structure, not its numbers. The GOVERNING spec for the port is
   `godot/godot_conversion_strategy_v1.md`." New: "retained for its extraction procedure (Part Seven)
   only. The ratified Godot mapping is `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12, which this
   document contradicts at three points: one autoload holding all state (rejection 1), container
   signals as the consequence stream (rejection 3), and one seeded generator for the campaign
   (rejection 4). `godot/godot_conversion_strategy_v1.md` is PROPOSED, intent only."
2. `godot/README.md:13-14` — TEXT item 3's replacement sentence gains one clause, applied as one
   edit: "… Do not implement from it; its autoload, signal and generator designs are each rejected
   by name in `04` §C.12."
3. `CURRENT.md` — **no `ui` row is added.** `ui` has no code, no contract and no head; a row would
   point at quarantine, which `CLAUDE.md` §1 forbids.
4. `registers/handoffs/HANDOFF_GO.md`, Standing orders — one row: "The player surface is specified
   by the oracle's readings (`decision/sheet.py`, `harness/play_surface.py`); the UI design set and
   the stale architecture specification are intent only."

## The gate (execution artifacts)

`python tools/currency_consistency_check.py` and `python tools/freshness_gate.py` clean after items
1–2 and 4. `git diff --stat -- .designs .audit` empty.

## The falsifier

A port artifact, test or tool that opens a path under `.designs/systems/ui/` or names a v4 section
as its source: `grep -rn "valoria_ui_ux" tools engine modules tests` prints nothing today (run:
addendum §B7 E-B6) and must still.

## NERS reading (§0.06; E last)

Reference text, so N and E apply. **N:** cut any of the three bodies and the game behaves the same;
each stays because §0.05 keeps design documents, and the two edited sentences are the ones a porter
would act on wrongly. **E:** one sentence at each of two owners tells a porter which document binds.

## Cost class

Edit.
