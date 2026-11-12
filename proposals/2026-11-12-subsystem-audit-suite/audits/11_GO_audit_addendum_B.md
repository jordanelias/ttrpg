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

Numbered in the order found; the severity is on each, and §B6.1 ranks them. "The UI set" means the ten files under
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

**Falsifier.** A second copy anywhere in the working tree, hidden trees included: `grep -rIl` for
"THE CUTSCENE SYSTEM", "PART 19 — ", "PART 15 — PARLIAMENT" over `*.md` (run; §B7 E-B2). Outcome: the
only hit is this file.

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

### F-GO-15 · blocks the standing requirement · the player surface has no shared vocabulary, and six lanes have each proposed their own

**Claim.** "Each subsystem a playable game, on one code path, integrated" needs one answer to *what a
player is shown*. The suite's own proposals give six: SE `sheet(w) -> dict` (`07_SE_valley_scenario.md`
§4); FA "a digest" (`06_FA_playable_scenario.md`); MB `FieldOutcome.report` of `PhaseSummary` plus a
`FieldPhaseView` (`04_MB_playable_field_scenario.md` B, D); PC `DuelRoundOutcome.trace` plus
`CombatTurnView` (`03_PC_duel_round_and_approach.md` §2, §4); SC a tuple on `Event.ending`
(`05_SC_contest_record_on_event.md`); FI "one scenario summary line" (`08_FI_03_playable-inquiry.md`
§5). The two surfaces already built disagree about what a surface may read: `decision/sheet.py` is
under the AX-2 path scan and takes no `World`; `harness/military_menu.py::menu(w, actor)` takes it
(`:87`).

**Evidence.** The files cited, each opened at the lines given. **Falsifier.** A shared record type
two of those proposals both name for a consequence: `grep -ln "ReceiptRow\|AccountRow\|AftermathRow"
proposals/*.md` in the suite finds only GO's files (§B7 E-B6).

**Touches.** R-04, and the standing requirement's "one code path". **Consequence.** Each lane's
design is sound alone; together they are six dialects (`CLAUDE.md` §10, shape divergence), a port
re-implements six, and a player learns six. SE's and FA's summaries also read world truth
(`world_q.hunger`), which is right for a developer's instrument and wrong as the steward's own view.
**Minimal fix.** One protocol: five readings and one scene pair (SURF-B), and one transcript runner
every scenario prints through (SURF-B §8). R50, R74.

### F-GO-16 · degrades narrative · a person cannot read what his own act came to

**Claim.** The oracle shows what may be done and, in the ledger, what has been learned. It has no
reading of *what this act of mine did*, and the ledger does not reliably carry it.

**Evidence** (E-B3, E-B4: seed 0, one season, hash `5ab73af2…` equal to the plain run). `p_npc_001`
resolved 15 acts; each caused one Event directly. Two `research` acts ended `finding.none`,
`degree=Failure`: his ledger holds **0** claims of that kind. `sabotage.refused` and
`compliance.impossible` did deposit. Ten of the 15 Events carry `observed` (the fold's reads, for
example `Observation(subject='set_s_001', predicate='stores:grain', value=40)` elsewhere in the log);
none carries `ending`, which has no production reader (`state/carriers.py:303`). Of his 119 claims,
0 hold an Event id or an act id as `id`, `subject` or `value`. Pairing by `(kind, subject)` fails
for 8 of the 15 (a `record.created` claim's subject is the new Record, not the act's subject).

**Falsifier.** A claim in the actor's ledger for each of his 15 acts' Event kinds on the act's
subject: run; 7 of 15. **Touches.** R-02 (consequence) as the player meets it; R-06.
**Consequence.** A player who researches and fails is shown nothing. A port would reach into the log
for it, which is world truth through the back door. **Minimal fix.** `receipt`, host-side, own acts
only, depth one, values withheld unless held (SURF-B §3). R51, R72, R73. `finding.none` leaving no
claim is cross-listed to FI as a question (is "I found nothing" a belief?), not changed here.

### F-GO-17 · CORRECTS SURF §3 · `AftermathRow.own_act` cannot be computed

SURF §3 read `own_act` as "the act id of his that the claim's chain names" and grouped claims "by
whether `Claim.chain` or `Claim.doer` names one of his own act ids (both fields exist on `Claim`)".
Both fields exist; neither holds an act id. `chain` is the tellers, origin first
(`state/carriers.py:358-371`: "WHO PASSED THIS CLAIM ON"); `doer` is "the holder's own id when the
claim records HIS OWN act, else `None`" (`:372-381`). E-B4: 0 of 119 claim ids are act ids.
**Resolution (R52).** `account` partitions by what the fields do say (`own = doer == holder`; told,
with teller, origin and hops already derived on `Claim`); the pairing of an act to its outcome is
`receipt`'s, through the driver's `act_of`. No carrier field is added: an act id on `Claim` would be
a second amendment to ratified `04` §B.9 (the first was `doer`, ED-IN-0294), and the host-side
reader makes it unnecessary.

### F-GO-18 · CORRECTS F-GO-08 and R20 · play is of two kinds, and two choice surfaces were missed

**Claim.** F-GO-08 said "PLAYABLE exists at one seam" and R20 that every scene is hosted "only
through a typed decider". That is true of suspension and false of play.

**Evidence.** (i) *Loop-played subsystems.* The seated person's offer at seed 0 held 33 distinct
verbs of the 66 resolvable, among them `speak`, `argue`, `petition`, `tell`, `lie`, `give`
(contest); `research`, `surveil`, `interview`, `reconstruct`, `thread_read`, `survey` (inquiry);
`commit`, `comply`, `construe`, `evade / defy` (governance); `build`, `found`, `tend`, `transfer`
(settlement) (E-B3). SC decided that a hearing is "the season loop on a one-matter fixture, with a
player callback on `dispatching_chooser`. No nested bout engine … no suspension inside a provider"
(`05_SC_playable_hearing.md` §"The resolution"), because a hearing's turns are verb rows and a
duel's are not. (ii) *The military menu.* `harness/military_menu.py` (ED-IN-0306 phase 5b; "Jordan
ruled the menu an engine-side Python API") gives the commander of a faction's army the legal army
commands with bounds, the module's vocabulary and advisories, and builds the acts
(`recruit`, `form_unit`, `assign_troops`, `order_unit`, `disband_unit`, `discharge_troops`). At
build, seed 0: 43 of 83 persons may mint their faction's army; none commands one (E-B3).
`harness/army_presets.py` gives an unplayed faction an army through the same fold.

**What stands of F-GO-08.** Suspension exists at one seam (the duel). The field has a choice surface
before the battle (the menu, and `FieldOrder(role, retreat_at)`) and none during it; the contest and
the inquiry need none. **Resolution (R53, R54).** SURF-B §6 types both kinds and says which
subsystem uses which.

### F-GO-19 · degrades narrative · the offer is three to five times the size the design set calls legible, and nothing in it says which rows are about the matter in hand

**Evidence** (E-B3; one person, one seed, a reading). Five deliberations showed 22, 32, 33, 32 and
38 candidates with budgets 5, 5, 4, 3, 2: 157 rows in a season. Twenty-three verbs appeared on all
five sheets (`forge`, `sabotage`, `conceal`, `challenge`, `exchange`, `surveil`, …; `train` four
times a sheet); five verbs appeared once (`petition`, `tend`, `lie`, `commit`, `argue`). The
question changed each time (`need`, then four `claim_landed`, each `about` a different claim) and
the view carried 7 to 12 separate questions. `Candidate.why` was deleted because nothing read it
(`carriers.py:591-595`). The design intent: 5–8 options a decision (`valoria_ui_ux_v4.md` §5.2), 12
visible Slate entries (`v4_1` §2.5), a load score of 8.0 or less with "every player decision …
meaningful and non-obvious" (`cogload_moderate_target.md`).

**Falsifier.** A field on `Candidate`, `DevelopmentSheet` or `View` that ties a candidate to one of
the questions: read the three classes; none. **Touches.** R-05 (verbs) and R-04 as the player meets
them. **Consequence.** The aperture is wide, which is the engine's strength, and unreadable as
shown, which makes the wide aperture feel like no situation at all. **Minimal fix.** `OfferRow.occasion`
and `Offer.withheld`; order and grouping are the oracle's, the cap the client's (SURF-B §2, MODES
§3). R55, R56.

### F-GO-20 · hygiene · the Godot architecture specification contradicts Layer 1 at five points and names the wrong governing document

Detail and the full table are §B5. In one line: one autoload holding all state against rejection 1;
container signals as the consequence stream against rejection 3; one seeded generator for the
campaign against rejection 4; a tracker registry of stored faction and clock values against PART D's
ban on stored aggregates; d10 pools with a target number against the one degree ladder. Its Status
line says the governing document is the conversion strategy; the ratified mapping is §C.12.
**Minimal fix.** REF edits 1–2. R66–R71.

### F-GO-21 · degrades narrative · the design set holds two opposite answers to "what does the player know", and three lanes' scenario summaries follow the wrong one

`throughlines_complete.md` T-30: "Player POV (full-framework access) → Character POV
(framework-blind) … The gap between player and character knowledge IS the gameplay."
`integration_proposal_v30.md` Part 7 gives the player a "Reported layer" (a faction intelligence
feed) beside the "Witnessed" one. Against them: UI Oath II test 3; the case corpus (46 of 281
knowledge rows name a player, and their recurring form is "players must NOT automatically know …
surfacing it requires a specific investigative action", "only by watching her behavior across
sessions, not via any status readout", "discovered retroactively, not tracked live"); and ratified
§C.11 ("A split on who is looking breaches the axiom"). The code follows §C.11: reaching past the
`View` raises. **Resolution (R58, R59).** §C.11 governs; nothing in play shows the player more than
his person holds; a lane's `sheet(w)` is a developer's instrument. What survives T-30 is one
question about the end of a campaign, returned to Jordan in §B6.3.

