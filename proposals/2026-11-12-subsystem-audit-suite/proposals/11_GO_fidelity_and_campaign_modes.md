# GO — one mode, three fidelities, one campaign frame: what the mode documents become in code

Reconciled: 2026-11-12, U5d closure — folded **A-49**, **A-48**, **A-1** and **A-53**. §4 built E1 (the truth is never shown) "because it needs nothing"; A-49 rules E2 on top of it: after a line ends and no continuation is taken, the client may show the developer's chain (`harness/chronicle.py`'s reading of the log); never in play, and never when a continuation would carry the truth to the next seat. Step added to §4: one host-side reading, gated on the line's end and on no continuation. §3's display cap stays the client's constant; triage of the question list is player gameplay (A-48). A world that fails its checks is replaced by the next seed by default, with play-it behind a setting (A-53), stated in the campaign frame.

## Status: PROPOSED

Carries `audits/11_GO_audit_addendum_B.md` §B3.4, §B3.5, §B3.7 and resolutions R56, R60–R65. Lane: GO
states; IN owns `harness/play_surface.py`, `decision/sheet.py` and `data/fixtures.py`; each module
lane owns its decider. Reads for intent only, and makes nothing load, the quarantined
`campaign_modes_v30.md`, `auto_manual_resolution_duality_v1.md` (ED-SC-0013), `cogload_moderate_target.md`,
`companion_app_design_note.md`, `campaign_architecture_v30.md` Part 7 and `videogame_mode_spec.md`.
Depends on `11_GO_player_surface_contract_B.md` (SURF-B) for the readings it names.

## What it changes in `engine/season/` at runtime

Nothing in the automated run. One reader gains a field (`CreationRow.holdings`). One rule is stated
for every module decider (no decider means the person's own policy). The rest decides what is **not**
built: no mode enumeration, no second resolution formula, no tolerance number, no difficulty code
path, no display cap in the engine.

## The problem, with evidence

The design set describes play under five different switches, and the code has one mechanism that
answers all of them without a switch.

| the design set says | where | what the code has |
|---|---|---|
| three campaign modes (tabletop, board game, hybrid), each with its own resolution branch per subsystem ("Mass combat: … Disposition table, single roll per battle" in board-game mode) | `campaign_modes_v30.md` §12.5 | one season loop; one field engine; no board-game roll (`grep -rn "Disposition table" engine modules` → 0) |
| three fidelities of one event: played, witnessed, auto; "auto = the kernel run headless, played = the same kernel run interactively" (RULED); a calibration tolerance left open as fork C | `auto_manual_resolution_duality_v1.md` §3, §8 | `PlayHost.persons` is a party test at one provider (`seam/wrappers/combat.py`); a fight either of whose claimants the host plays is played, every other is automated; "Nothing records the mode" (`queries/inputs.py:189`) |
| a Scene Slate of specific events, budgeted at 3–5 scene actions, from which the player picks what to attend | `player_agency` §4 as quoted in the doctrine §1 | `View.questions` in `attention_key` order and `scene_budget = 5` (`data/fixtures.py:228`, ruled); the person's own acts are what he attends |
| difficulty as a budget (5 / 4 / 3 scene actions) | `valoria_ui_ux_v4_1.md` §1.3 | one fixture, `scene_budget` |
| complexity tiers per system (a Core tier and a Full tier) and a companion application that holds the tracking | `cogload_moderate_target.md` META-1; `companion_app_design_note.md` | the engine holds all tracking; there is nothing for a tier to switch off |
| a campaign that ends by victory, shared loss, or the player choosing to stop ("Conclude this story", a portrait) | `campaign_architecture_v30.md` Part 7 (its own Part 8 lists the mode specification as not yet updated for it) | death, then `carry_on` over `world_q.continuations` (`harness/play_surface.py:61-95`); the B10-20 build file warns `victory: true` is not the game's end (first audit §9) |

Measured for the cognitive-load target (seed 0, one season, `p_npc_001`, a reading at one seed): the
sheet showed 22, 32, 33, 32 and 38 candidates at five deliberations against a design ceiling of 5–8
visible options per decision (`valoria_ui_ux_v4.md` §5.2), 12 visible Slate entries (`v4_1` §2.5) and
a per-system load score of 8.0 or less.

## The resolution, decided

### 1. One mode (ladder step 1)

The three campaign modes are superseded by the season loop: their per-mode rule branches describe a
tabletop and a board game the engine does not run. **The port has no mode enumeration and the oracle
gains none.** What the documents called a mode is, in code, who chooses for a person: the shipped
chooser, or a callback (`dispatching_chooser`). An empty `overrides` mapping is the automated realm
and is the control.

### 2. Fidelity is derived from where the person stands, never selected from a list of formulas (steps 3, 5)

| fidelity | when | what the player gets (SURF-B) |
|---|---|---|
| **played** | his person is a party to a suspended scene and the host supplies a decider | the turn view, the choice, the `trace` between turns, then the `receipt` |
| **watched** (the doctrine's "witnessed") | his person is present and not a party, or is a party and the player declines to decide | the `account` rows WITNESS deposits firsthand; for a field, MB's per-phase Observations; no choice |
| **auto** | his person is absent | whatever is later told to him, with its teller and remove, or nothing |

No fidelity has its own formula, so none can be chosen for a better expected outcome: that is fork A
of ED-SC-0013 as ruled, and the code already has that shape. **Fork C (the calibration tolerance)
needs no number.** Two clauses replace it:

- *Equal on matched decisions.* A played scene whose decider returns what the automated call would
  have chosen reproduces the automated outcome and draw log. This is a pin (GATE §3), not a
  distribution test.
- *No decider means the person's own policy.* A scene with no decider asks the per-person decider
  the chooser supplies (PC §4 for the duel; MB's standing orders for a side nobody plays), never a
  module constant. Today `decide=None` in `modules/combat/fight.py` is "the engine's own
  engage-every-turn loop", which is a constant; it is the same for an NPC and for a player who
  declines, so nothing is forked now, and the clause binds the decider that replaces it. A player
  who lets a scene resolve then gets what an NPC with his sheet would get. What a skilled player
  gains by deciding is the game, not an exploit: his decisions are inputs.

The doctrine's "debt" (the automated parliamentary vote was a generic seasonal roll, not the
resolution of a specific slate event) is closed by supersession: that resolver is gone
(`git ls-files | grep parliamentary_vote` prints nothing), and a motion is now a docketed matter
persons act on.

### 3. The cognitive-load target becomes four oracle duties and one client constant (steps 4, 5)

The target's own principle is "every player decision should be meaningful and non-obvious", and its
method is to move tracking and arithmetic out of working memory. The engine already holds all
tracking, which is what the companion-application note asked for. What remains is the size and
legibility of each decision:

- **The oracle owes order and grouping, never a cut.** `Offer.rows` in rank order, each row's
  `occasion` (which question it answers, or none), its `terms` and `odds`, and the `withheld` rows.
  With these a client can show the rows that answer the question first and fold the standing menu
  behind one control, without holding a rule about which verbs matter.
- **The display cap is the client's constant.** Precedent: `harness/military_menu.py::SHOWN = 12`,
  annotated "display length only, no game meaning". A cap in `Fixtures` would be game data that
  moves no game. The cap never removes a row from the reading: a pick may name any index.
- **One choice where the design proved two were one.** The target's SC-3 (four named argument
  styles in place of two binary choices) and the UI audit's F-11 are the same finding. The rule is
  general: a module's closed choice set is exported with a `name` and one line of `text` per member
  (SURF-B §6 rule 2), so the client shows a named move and never a matrix.
- **The measure is the transcript.** `play_surface`'s transcript prints rows per deliberation and
  rows per occasion. A scenario whose first deliberation shows no occasioned row has nothing in
  front of the player, whatever the size of the menu.
- **Difficulty is a fixtures overlay chosen at world build**, data and not a code path: a client
  passes a `Fixtures` with `scene_budget` swept. The Core and Full tiers are not built; no rule
  exists for a tier to hide, and hiding an offered row would breach the first duty.

### 4. The campaign frame (steps 3, 4)

- **Begin.** `creation_sheet` then `seat`: the player picks a person the builder seated (IN-47 C1,
  as ruled). `CreationRow` gains `holdings` (his live Tenures, through `OwnStateReader`), because a
  seat's place in the world is the first thing a player must weigh and the row shows none of it. At
  seed 0, one season, 318 of 749 acts (42.5%) were matched in another person's ledger, 60 of 83
  persons had at least one act so matched, and `p_npc_001` had none of fifteen: seats differ in how
  much of the world can answer them, and the sheet should not hide it.
- **Continue.** `carry_on`, as built.
- **Save.** Between seasons only. The UI set ("no saves mid-resolution"), the stale Godot
  specification ("Save between seasons only") and the first audit's R44 (a snapshot at a barrier
  boundary) say the same thing; it is decided, and the snapshot format is R44's.
- **End.** The line is extinct (built), or the player concludes. A conclusion writes nothing: it is
  `chronicle(p)` and the whole `account` read at that moment. No victory screen is derived from
  `requirements.yaml`. Whether an ending may show the player what his person never knew is the one
  question this addendum returns to Jordan (addendum §B6.3).
- **Standalone.** Each subsystem's playable game is its lane's scenario builder run through the
  same transcript runner and, in the port, the same five readings and scene pair. There is no
  separate "skirmish mode" code path: a scenario is a world.

## Exact edits, by owner

1. `engine/season/decision/sheet.py` — `CreationRow` gains `holdings: tuple`; `creation_sheet`
   fills it from each person through `OwnStateReader` (no `World`).
2. `engine/season/queries/inputs.py::PlayHost` docstring — add the clause "a scene with no decider is
   decided by the person's own policy" and name the present interim (the module default).
3. Each module's exporter — its closed choice set with `name` and `text` (`tools/export_battle_orders.py`
   has the roles; `tools/export_engine_params.py` gains combat's `TURN_CHOICES`/`APPROACHES`).
4. `registers/handoffs/HANDOFF_SC.md` — ED-SC-0013 fork C closed by the two clauses above, citing the
   module-scene pin as its instrument.
5. No edit under `.designs/`.

## The gate (execution artifacts)

1. `overrides = {}` reproduces the plain hash; a seated person with `take_ranked` does too (holds
   today at seed 0).
2. For each suspended scene with a decider: the played run whose decider returns the automated
   choice reproduces outcome and draw log (PC's and MB's own gate; listed here because fork C rests
   on it).
3. A `Fixtures` with `scene_budget` swept to 3 gives the seated person three scenes and moves the
   hash; nothing else in the engine reads a difficulty.
4. `creation_sheet` on a built realm shows a non-empty `holdings` for a seat holder and takes no
   `World` (the path scan).

## The falsifier

A second resolution formula reachable from the loop under any name. A decider default that differs
for a played person and an NPC of the same sheet. A row absent from `Offer.rows` because of a cap.

## NERS reading (§0.06; E last)

- **N.** Cut the derived fidelities and "auto-resolve" becomes a second engine to calibrate, the
  defect the doctrine was written against. Holds vertically (duel, field, speech: one rule) and
  diagonally (a scene entered from the season and a scene run alone).
- **R.** *Strategic thought* is choosing where to stand and what to attend with five scenes; the
  world's drama without the player reaches him at the remove the tellers leave it.
- **S.** *Pauses correctly* and *zooms across scales* are one statement here: suspension is the
  only pause, and it has one form. *Consistent methodology*: one budget, one cap rule.
- **E.** Scored against N and R: five switches in the documents become zero in the engine and one
  constant in the client. A player intuits the fidelity rule from where his person is.

## Cost class

§1, §2: a decision and two docstring edits. §3: edit (exports) on top of SURF-B. §4: edit. No build.
