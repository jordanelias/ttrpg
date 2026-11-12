# GO — adversarial steelman audit, addendum B: the player-facing layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 13a82e4 (working tree; the first GO lane read at ad07a9a)

Continues `audits/11_GO_audit.md` (§0–§14, F-GO-01..12, R1–R47). Nothing there is repeated; where this
file corrects it, the correction is marked **CORRECTS**. Finding ids continue at F-GO-13, resolutions at
R48. Proposal short names: **SURF-B** = `proposals/11_GO_player_surface_contract_B.md` (supersedes
`11_GO_player_surface_contract.md`, called **SURF** below), **MODES** =
`proposals/11_GO_fidelity_and_campaign_modes.md`, **REF** =
`proposals/11_GO_design_reference_disposition.md`. The first lane's **GATE** and **TEXT** keep their
names.

## B0. Verdict

**The player-facing layer is designed twice and built once, and the two designs do not describe the
game that was built.** The UI design set (v4, v4.1, its audit and workplan) and the stale Godot
architecture specification both render a board game with a player attached: seven phases, a Scene
Slate of authored opportunities, four global clocks, faction stat vectors, card hands, a Conviction
track contest of ten steps. The season loop that runs has none of those objects; it has persons, a
ledger of claims per person, a ranked offer of verbs, and five module entries. What the loop does
have is the thing the design set wanted most and could only assert in prose: a surface that shows
only what the character can perceive (Oath II, test 3), because the `View` is claim ids and nothing
else. **The single largest obstacle** is therefore not a missing screen but a missing *reading
vocabulary*: of the four things a player must be able to do in every subsystem (see a situation, be
offered choices, see consequences, read reasons), the oracle types the second for the season and the
duel, and types the other three for nothing. Until those readings exist as person-side functions,
every UI document in the tree specifies pixels over data that is not there, and a port would have to
invent the data, which is the second owner the first audit warned against.

## B1. What was read

The full list, with what was not read, is §B7.2; it is written once, there. In short: the whole UI
design set (ten files); the nine cross-cutting documents the first lane named, with the ruled
auto/manual doctrine; `godot/godot_architecture_specification.md` to its end; Layer 1 §C.11, §C.12
and PART E; the player-surface code (`decision/sheet.py`, `harness/play_surface.py`,
`harness/military_menu.py`, `queries/inputs.py`, the `Event`, `Claim`, `View`, `Question` and
`Candidate` carriers, the combat and mass-battle entries); the 143 cases through the repository's
own loader (972 needs, 281 knowledge rows; 243 needs and 46 knowledge rows read in full, selected by
a stated matcher); four entries of `.audit/`; and the twelve sibling proposals that define a playable
surface. `.audit/` beyond those four (about 7 MB) was not read.

## B2. Corrections and new findings

Ranked worst first within the player-facing layer. "The UI set" means the ten files under
`.designs/systems/ui/reference/`; all are ARCHIVED-NOT-CANON and none is cited below as the reason a
behaviour is correct.

### F-GO-13 · degrades narrative · the UI set's content-level half is not in the tree

**Claim.** `valoria_ui_ux_v4_1.md` declares itself a "structural supplement to v4" and says "v4 remains
authoritative for content-level UI specification" (its Status line, `:14`). It defers to v4 by section
at least eleven times (`:476` §4.3 the action panel; `:533` §5.2; `:626` Parliament "See v4 §15"; `:703`
"See v4 §7.6–7.9"; `:719` "See v4 Part 8"; `:965` "Content unchanged from v4 Part 11"; `:1007` "per v4
§13.2"; `:1045`, `:1062` the seven-scene walkthrough "from v4 §10.2"; `:1094` "From v4 Part 19 — 22
mandatory triggers. Unchanged"; `:1102` "From v4 §19.3"; `:1409` "Content from v4 Part 24"). **The v4 file
in the tree has no Part 10 to Part 19 and no §20.1–§20.2**: it runs Part 0 to Part 9, then resumes at
"§20.3 … continued" (`valoria_ui_ux_v4.md:1713-1714`), then Parts 21–25.

**Evidence.** `grep -n "^# PART" valoria_ui_ux_v4.md` prints Parts 0–9 and 21–25 only. The generated
index (`valoria_ui_ux_v4_index.md`, dated 2026-04-18) lists the same headings, so the loss predates the
index: it is not a quarantine-move accident. Missing, therefore, from every file in the repository:
the integrated seven-scene loop walkthrough (the one passage v4.1 calls "the document's strongest
single Part"), national faction management, settlement management, character management (including
Conviction revision, "v4 §13.2"), party management, the Parliament interface, the Inquisition hearing,
treaty and Grand Debate, the clock column, the whole cutscene system with its 22 mandatory triggers, and
feel layers 1–2.

**Falsifier.** A second copy: `git grep -l "PART 19" -- . ':!.audit'` and a search of `.designs/` and
`.audit/` for "THE CUTSCENE SYSTEM" (run; §B7 E-B2). Outcome: no copy.

**Touches.** R-04 (strategic and management actions as the player meets them), R-06/R-07 (how a
character is shown). **Consequence.** The first audit's R45 ("the UI documents stay reference") stands,
but its premise was that the reference exists. For the management surfaces and the season's integrated
loop it does not; what a port would build from is a table of contents. **Minimal fix.** None to the
quarantined tree (it is not edited). The decided resolution is R48: the oracle-side readings of SURF-B
are the specification of the player surface, written against the season loop as built, and the missing
v4 parts are *not* reconstructed. REF records the disposition.

### F-GO-14 · hygiene · the newest UI document still carries two tracks its own audit ruled out, and its repair plan stopped after one stage

`valoria_ui_ux_v4_1_max_audit.md` (69 findings; 20 P1) found that v4.1 §9.8 displays a "CD" clock and
§9.7/§11.3 a "Taint" track that the threadwork design had already deleted (its F-15, F-16, F-55, F-58),
and `valoria_ui_ux_v4_2_workplan.md` sequenced thirteen stages to repair it. The tree shows stage 1
executed (v4.1's Status line is the workplan's item 1.1 text, word for word) and stage 2 not: §9.8 "CD
accumulation display" is at `valoria_ui_ux_v4_1.md:868-877`, "Taint" at `:864-866`, `:1001`, `:926`. No
`valoria_ui_ux_v4_2.md` exists. So the document the first audit's proposal quoted two rules from is, by
its own audit, 65–70% of a reference, with sixteen blocking findings open and a known-false HUD.
**Minimal fix.** None in the quarantined tree. R49: nothing binds; the workplan is a retired plan held
in quarantine and is not a queue (CLAUDE.md §0, the terminal-record test). The audit's *method* (an
inventory of 84 playable moments, each tested for what the player sees, may declare, and learns) is the
one transferable instrument and is reused in §B3.

