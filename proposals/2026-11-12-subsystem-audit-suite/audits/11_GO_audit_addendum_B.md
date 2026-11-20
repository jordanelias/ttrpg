# GO — adversarial steelman audit, addendum B: the player-facing layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

Grounded: 2026-11-12 by `audits/24_GROUNDING_GAMES.md` (GM-07; GC-3) — §B3.4's "Football Manager (three renderings of one match engine)" is sourced only as a viewing ladder; that a skipped and a played match are one simulation is not established. The section's rule (one decider, the person's own policy) is unchanged.

## Read at: 13a82e4 (working tree; the first GO lane read at ad07a9a; `git diff --stat 13a82e4 2d909d9` outside this suite's directory is empty)

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
duel, holds the first in fragments no reading assembles, and types the third and fourth for nothing
a client could read: at seed 0 a seated person's two failed inquiries left no trace in his own
ledger. Meanwhile six lanes of this suite have each proposed a different shape for what their
subsystem shows a player. Until one set of readings exists, every UI document in the tree specifies
pixels over data that is not there, and a port would have to invent the data, which is the second
owner the first audit warned against. Three proposals carry the repair (one supersedes the first
lane's contract), thirty-one resolutions are decided, two of the first lane's are corrected, and one
question (whether a campaign's end may show what the character never knew) is returned to Jordan.

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
executed (v4.1's Status line is the workplan's item 1.1 text, with a pointer to the workplan added) and stage 2 not: §9.8 "CD
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
(`world_q.hunger`; `digest(w, since)` over `w.log`), which is right for a developer's instrument and
wrong as the steward's or the duke's own view.
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
38 candidates with budgets 5, 5, 4, 3, 2: 157 rows in a season. Twenty-one verbs were offered five
times across the five sheets (`forge`, `sabotage`, `conceal`, `challenge`, `exchange`, `surveil`,
`speak`, …) and `train` twenty times; five verbs appeared once (`petition`, `tend`, `lie`, `commit`,
`argue`). The question changed each time (`need`, then four `claim_landed`, each `about` a different
claim) and the view carried up to 12 separate questions. `Candidate.why` was deleted because nothing read it
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

## B3. The player-surface design reading

The measuring stick is four things a player must be able to do in every subsystem: **(a)** see a
situation, **(b)** be offered choices (the verb aperture), **(c)** see consequences, **(d)** read
the reasons behind what persons and the world did. The design set is read for what it asks; the
code and the probes for what exists. A design document is cited for intent only.

### B3.1 What the design set asks, in twelve intents, and where each stands

| # | the design set asks | source (intent) | in the loop as built |
|---|---|---|---|
| 1 | the surface shows only what the character can perceive and use; a control he cannot use is absent, not greyed | UI Oath II and its three tests; v4.1 §2.1 | **built, by type.** The `View` is claim ids and one query; `opening_set` forms only what he may attempt; reaching past the `View` raises |
| 2 | the world's demands arrive as a short ranked list of specific occasions, more than can be attended; choosing is the play | the Scene Slate; ED-SC-0013 §1 | **built, unnamed.** `View.questions` in `attention_key` order and `scene_budget = 5`; no reading presents them (SURF-B `AskedRow`) |
| 3 | every option shows its pool, obstacle, cost and projected band before commit | v4 §4.3.1 | **partly.** The candidate; `View.odds` (believed); no terms, cost or odds on the sheet |
| 4 | an option out of reach is shown with what it needs, unless it is beyond his perception | v4 §5.3; max audit F-7 (seven gate kinds) | **absent.** A declined candidate is discarded; `harness/interactions.py` names it as the first thing its log cannot show |
| 5 | after a roll, what decided it: the pool as assembled, the margin against the resistance, the named interaction | v4 §6.3.1, §7.6; the contest walkthrough, step 3 | **partly, and not for the player.** The duel returns a `trace` list; the contest's `Margin(net, ob)` stops at the seam; `Event.observed` holds the fold's reads |
| 6 | consequences enumerated and traceable, at once and at the season's close ("What did I just do?") | v4 §7.9 (five panels), §21.3 (the accounting scroll) | **absent for his own acts** (F-GO-16); `chronicle` shows the ledger as a present state |
| 7 | another person's reason is visible as the frame he speaks from, and a counterpart can predict him | v4 §5.5; cases NPC-073, NPC-090, NSC-04 | **only as far as he holds claims.** No reading groups what he holds about one person's deeds and commitments |
| 8 | evidence on a persistent board, each item with source and reliability; an argument cites held items | v4 §4.5–§4.6; max audit F-6 | **the carrier is built** (`Claim.source`, `chain`, `confidence`; `LedgerReader` support over origins); no board reading; `proofs` spends the whole ledger and cites nothing |
| 9 | one engine at three fidelities | ED-SC-0013 (ruled) | **built in shape** at one provider; two of the three fidelities have no reading |
| 10 | information is dark, then perceived, then named, earned by engagement | `integration_proposal_v30.md` Part 4 | **dark and held are built**; "perceived but unnamed" is presentation over an `AccountRow` |
| 11 | what happened elsewhere reaches the player through his nearest connection, tagged for reliability | max audit F-44 | **built.** A told claim carries its teller, origin and hops. 77 of the seated person's 119 claims were `told_by`, every one through a channel with no speaking actor (`chain` empty), so this run exercised only the anonymous form |
| 12 | a change is felt before it is labelled; the moments that matter are staged | Oath III | **a trigger rule only** (SURF-B §7); staging is the client's |

Seven of twelve are built or partly built in the engine and reach no client; the absences are 4, 6
and the readings of 5, 7 and 8.

### B3.2 What a seated person is shown today, measured

Seed 0, one season, `p_npc_001` seated with `take_ranked`; hash equal to the plain run (E-B3, E-B4).

| | reading |
|---|---|
| (a) situation | 5 deliberations; question sources `need` ×1, `claim_landed` ×4; the view held 0 then 12 claim ids and 1 to 12 separate questions; no place, holdings or company on the sheet |
| (b) offer | 22 / 32 / 33 / 32 / 38 candidates; 33 distinct verbs of 66 resolvable; a `Candidate` is `verb`, `subject`, `operands`; `View.odds` is a function the sheet does not call |
| (c) consequence | 15 acts, 15 direct Events (4 `record.created`, 3 `finding.made`, 2 `finding.none`, 2 `compliance.impossible`, one each of `petition.filed`, `sabotage.refused`, `proposition.uttered`, `commitment.made`); 2 with a degree, 10 with `observed`, 0 with `ending`; 119 claims deposited (42 firsthand, 77 `told_by`), 40 with `doer` set |
| (d) reasons | 30 new claims about other persons (14 `dispensation.issued`, 7 `order.given`, 4 `date.scheduled`, 2 `pursuit.moved`); none says why |
| the world's share | 13,379 Events in the season; 119 deposits to him, 0.9% by count |
| the world's notice | realm-wide, 318 of 749 acts (42.5%) are matched by kind and subject in another person's ledger, and 60 of 83 persons had an act so matched; of his 15, none (E-B5) |

The last row is one seed and one matcher; it shows a range, not a rate. It bears on creation: a seat
the world cannot answer is a poor first game, and the creation sheet shows nothing of it (MODES §4).

### B3.3 Per subsystem: what the oracle must export, and what exists

"Export" means a typed reading or a typed field on a module's input or outcome, built in the oracle
and re-implemented or rendered by the port; never a rule in `game/`.

| subsystem | (a) situation | (b) choices | (c) consequences | (d) reasons |
|---|---|---|---|---|
| **the person's season** | *needs* `Situation`: asked rows, holdings, budget. *Exists:* the sheet's own-field copies, `View.questions` | *needs* `Offer` with terms, odds, occasion, withheld. *Exists:* ranked candidates | *needs* `receipt`, `account`. *Exists:* `chronicle` | *needs* `account` rows with source and teller; `explain`. *Exists:* `Claim` fields |
| **duel, and a duel round on a grid** | *needs* a turn view with what a fighter can see (PC §4). *Exists:* `CombatTurnView(turn, claimants, wound_state)` | *needs* the approach per round, exported with names. *Exists:* `TURN_CHOICES = (engage, withdraw)`, the duel terms `yield / blood / death` | *needs* the round's typed trace and `Event.ending` read by `receipt`. *Exists:* an untyped `trace` list on the entry's return; `ending` stamped, unread | *needs* the decisive beat (PC's typed outcome) and the opponent's approach as seen. *Exists:* nothing typed |
| **field** | *needs* his army as he holds it and, in battle, his own side per phase (MB's `FieldPhaseView`). *Exists:* `MilitaryMenu` (host-side); `MassBattleInput` (resolver-side) | *needs* orders before and at phase boundaries. *Exists:* six army commands with bounds, `FieldOrder(role, retreat_at)`, `battle_orders.json`; no choice during | *needs* a per-phase report on the typed outcome. *Exists:* `degree`, two size shares, `_person_report` (who broke first, survivors) | *needs* the report's terms (flanked, parts broken) as Observations a bystander can carry. *Exists:* four advisories before battle |
| **contest** (hearing, petition, debate) | *needs* the matter, the bench as he knows it, his own case (`dossier`). *Exists:* the docket question; `SocialContestInput` is resolver-side | *needs* `speak` with what he cites, plea and effort; `tell`, `lie`, `give`, `evade / defy` (SC). *Exists:* the verbs in the offer; `proofs` uncited | *needs* the roll on the act's Event (SC-P1) read by `receipt`. *Exists:* `Margin(net, ob)`, dropped | *needs* the room and leverage terms (SC-P1's `room`, `leverage`) for his own act only. *Exists:* composed inside the module |
| **inquiry** | *needs* what he holds about the subject (`dossier`); **never** the trail (`TrailItem` is the host's projection of deeds he did not witness) | *needs* the inquiry verbs and, at the end, a conclusion to state (FI-03). *Exists:* six inquiry verbs in the offer | *needs* the finding's terms, and "nothing found". *Exists:* `Findings(found)`; `finding.none` reaches no ledger | *needs* source, origin and contradiction per item. *Exists:* on `Claim`; no reading |
| **governance** | *needs* the vacancies, writs and dockets stamped on his question. *Exists:* `Question.classes` | *needs* nothing new. *Exists:* `confer`, `succeed`, `commit`, `comply`, `construe`, `evade / defy` form on the classes | *needs* `receipt`. *Exists:* refusal kinds with `observed` | *needs* who ordered, who refused, as held. *Exists:* `order.given`, `dispensation.issued` claims |
| **settlement** | *needs* the shortfall and store claims he holds; a steward's holdings. *Exists:* hunger is a Query nobody is shown; claims of `condition.worn` and the like | *needs* nothing new. *Exists:* `build`, `found`, `tend`, `transfer`, `requisition` | *needs* `receipt`; `account` with `prior` for a store he holds claims about. *Exists:* the claims | *needs* an unattributed fall to say so. *Exists:* §C.11's rule, unbuilt |

### B3.4 Auto-resolve and manual play

The ruled doctrine (ED-SC-0013) is one engine at two ends and a thin middle; its referents are
Football Manager (three renderings of one match engine) and Total War (per battle, fight or
resolve). `[CORRECTED 2026-11-12, audits/24_GROUNDING_GAMES.md GC-3: what is sourced for Football Manager is a
ladder of ways to watch one match (research/game_precedent_suite/dispositions/D_T04.md row 57); that its
instant result runs the same simulation is not established (D_T04 row 58;
grounding/football_manager_instant_result.md). Total War's own auto-resolve is a second calculation
(tables/R6 F5), so neither referent demonstrates one engine at two ends; the doctrine is a ruling.]` The code has the doctrine's shape and none of its presentation. It also has something the
doctrine did not anticipate: **fidelity is epistemic already.** A party decides (if hosted), a
bystander receives firsthand `seen` deposits, an absent person receives a telling at some remove or
nothing. So "witnessed" needs no mechanism and the played/auto pair needs one rule the first audit
did not state: with no decider, the scene is decided by the person's own policy, never a module
constant, so that declining to play costs and gains nothing an NPC of the same sheet would not
have (MODES §2, R61, R62). The doctrine's open fork C then needs no number. Football Manager's
other half, the post-match explanation, is the `trace` and the `receipt`: the same record, shown
between turns to one who plays and after the fact to one who does not.

### B3.5 The cognitive-load target

`cogload_moderate_target.md` scores each system's load and brings every one to 8.0 or less, chiefly
by moving state and arithmetic onto cards and mats; its companion note concludes that the tracking
layer should be software. In the video game that is already true, so the target's residue is the
decision itself, and its stated principle is the test: "every player decision should be meaningful
and non-obvious". Three things follow. First, the offer as shown (22 to 38 rows) fails the test not
by having too many verbs but by not distinguishing the five that answer the question from the
standing thirty (F-GO-19). Second, where the design found that two choices were one (four named
argument styles for genre × orientation), the rule generalizes: a module's choice set is exported
with a name and a line of text, and the client shows a named move. Third, the lossy cuts the target
considered (flat costs, auto-corroboration, a "Core tier" hiding advanced actions) are not needed
and should not be built: nothing in the engine is expensive for a player to track, and hiding a row
he could take breaks intent 1 from the other side. MODES §3 decides this.

### B3.6 The three surfaces the brief names

**The duel, and a duel round inside grid combat.** *Asked:* each fighter equipped, an approach per
phase, each exchange visible; on a grid, the player picks an approach and the engine runs one round.
*Exists:* one suspension seam with a typed view and a two-member choice set; a per-turn trace the
module returns and nothing reads. *For the surface:* the round as the unit (PC §2) is what makes
both modes one path, because a grid turn then asks for exactly one `DuelRoundOutcome` and shows its
`trace`; the view must carry what a fighter can see (PC §4); the choice set must be exported. The
quarantined UI's version (a pool split slider declared blind by initiative) describes a retired
resolver and is not a target.

**The managed battle.** *Asked* (Football Manager, Total War, Ogre Battle, Unicorn Overlord,
Bannerlord): compose and instruct before; watch; intervene; resolve automatically and consistently;
read afterwards why it went as it did. *Exists:* the composing and instructing half is further on
than the first audit recorded: `MilitaryMenu` gives legal recruitment by cohort and troop type with
bounds, subformations, roles, stances, targets, a retreat threshold and four advisories ("under N it
routs at the first check", "levy will not close to contact"), and `army_presets` fields an unplayed
faction through the same commands. *Missing:* anything during the battle and any explanation after.
*For the surface:* MB's phase decider and three phase summaries are the smallest faithful form; the
summaries must be on the typed outcome so that the played, watched and absent player read the same
battle at three removes. The 2026-07-29 visualization audit (re-read in full; lesser weight) is the
one record of a battle rendered tick by tick: formations sheared at 30–45°, attrition was 7–15% where
the historical battles lost most of an army, and cells interpenetrated until an exclusion pass
halved it at a cost of 19% of the casualties. Those are MB's to re-verify; for GO they say that a
per-tick view is where a field's defects become visible to a player, which is an argument for
watching at the phase, not the tick, until MB has re-measured them.

**Evidence-and-argument contests and the case board.** *Asked* (the detective precedents; v4 §4.6;
max audit F-6, F-7, F-11): a persistent board of held items with source and reliability; an
argument that cites items; a contradiction that answers; one named choice per exchange. *Exists:*
the strongest carrier in the tree for it. A claim already knows who told it and through whom, a
reader already counts support over distinct origins and prices a teller caught out, and a forged
Record already has a quality an inquiry rolls against. *Missing:* the reading (`dossier`), the
citation (FI-05's `cites`), and the roll shown to its maker (SC-P1 with `receipt`). SC's decision
that a hearing is loop-played is right for the surface as well: the board and the offer are the
same two readings inside and outside the room, so "zooming in" to a hearing changes the fixture and
not the interface. The UI set's Reconstruct rule ("the conclusion is WRONG; you will not know") has
its lawful form in FI-03: a wrong conclusion follows from a wrong ledger, and no band is hidden.

### B3.7 Campaign modes

`campaign_modes_v30.md` is a rule-branching table for a tabletop game, a board game and their hybrid;
`campaign_architecture_v30.md` adds the Church's four settlement axes, a three-phase invasion, the
revelation curve, and an ending by portrait and lineage. None of the per-mode branches exists in
code and none should: MODES §1 decides one mode. What the two documents hold that a campaign still
needs is a frame: how it begins (a seat is chosen), continues (the line carries on, built), is saved
(between seasons; three documents agree) and ends (extinction, or the player concludes and reads
the chronicle). The world-content parts (axes, invasion phases, the revelation curve by band) are
WR's and FA's content, and reach a player only as claims.

### B3.8 What the provided arcs and characters ask of the surface

The 143 cases were loaded through `harness/run_cases.load_cases` (972 needs). 243 needs name a
player or use the vocabulary of seeing (81 name a player in the need or its reason; the first audit
counted 53 on the need alone), and 46 of 281 knowledge rows name a player. Read in full and classed
by hand; the classes are about legibility, which no other lane owns.

| what the cases require | cases (examples) | carried by | today |
|---|---|---|---|
| a quantity hidden **from its own holder**, visible to a trained third party | ARC-02, ARC-05, ARC-26, ARC-35, ARC-39, NPC-004, NPC-007 | the holder's readings show nothing; the observer's `account` holds the claim | representable (per-holder ledgers); the surface must not have a sheet field that leaks it |
| one entity rendered as nothing to one observer and in full to another, in one scene | SCN-10, ARC-16, ARC-27, ARC-30, ARC-48, ARC-54 | readings are per seated person by construction | built in shape |
| a hidden thing surfaced only by a specific investigative act or a holder's choice to tell | ARC-07, ARC-12, ARC-18, ARC-36, ARC-47, ARC-50 | `receipt` of the inquiry; a told `AccountRow` | the channel is built; no reading |
| disclosure as a real choice (tell him, tell his institution, withhold) | ARC-02, ARC-12, ARC-15, ARC-41, ARC-47, NPC-033, NPC-039 | `Offer` rows for `tell` and its kin on a held claim | `tell` forms; whether the three destinations form is CHAR's and FI's |
| an accumulated change attributed to the actor whose behaviour caused it, or marked untraceable | ARC-R16, SCN-02, EMG-C3 | `AccountRow.unattributed`; never an Event walk | absent |
| a counterpart's bias predictable from his disposition | NPC-073, NPC-090, NSC-04, NPC-030, NPC-089 | claims he holds about that person's commitments and past deeds, grouped (`dossier` on a person) | claims exist; no grouping |
| a value followed across periods, or read as one summary on return | ARC-46, ARC-R16, ARC-R19 | `AccountRow.prior`; `account(p, since)` over several seasons | absent |
| a cost the chooser is not warned of | ARC-14, EMG-X5, EMG-C2, ARC-R19 | `odds` and `terms` are his beliefs, so an unknown cost is simply not in them | built in shape: the surface never promises completeness |
| noticing an absence | ARC-09, ARC-06 | no carrier (the first audit's finding stands; IN's) | absent |

Two consequences for the contract. The corpus asks for ignorance as often as for knowledge ("players
must NOT automatically know"), which is the strongest argument in the tree for person-side
readings over any status display. And the needs that ask for a *summary* ask for it as something
read at an accounting, late, which is `account` over a longer `since`, not a live meter.

## B4. The player-surface contract, refined

The decision-ready text is SURF-B. What it changes in the first lane's contract, and why the full
set warrants each change:

| SURF | SURF-B | warranted by |
|---|---|---|
| §1 `OfferRow(candidate, pursuit, stance, odds, cost)` | `OfferRow(candidate, occasion, terms, odds, cost)` in an `Offer` that also carries `withheld` rows | F-GO-19; design intents 3 and 4; CHAR's two proposals, which own the hook and the decline |
| — | `Situation` with `asked` rows and `holdings` | intent 2 (the Slate is `View.questions`); B3.2 (a) |
| §2 `explain` | unchanged | `04` §C.11 |
| §3 `aftermath(p, since)` with `own_act` | `account(p, since)` with `own`, `prior`, `unattributed`; and `receipt`, host-side, for his own acts | F-GO-16, F-GO-17; intents 5 and 6; the case classes of B3.8 |
| — | `dossier(p, subject)` | intent 8; the brief's case board; FI-05 |
| §4 scars and crises emit | unchanged | — |
| §5 `OFFER-CONTAINS` | unchanged | — |
| §6 every scene through one typed decider | two kinds of play; five rules for the scene pair; no decider means the person's policy; the outcome carries `trace` | F-GO-18; SC's decision; ED-SC-0013 |
| — | a presentation is triggered by an `AccountRow` or `ReceiptRow`, never a log Event | Oath III against §C.12 rejection 3 |
| — | one transcript runner for every lane's scenario | F-GO-15 |

The split between oracle and runtime that the first audit drew (§5) gains one row and loses none:

| what | crosses as | owner here | state |
|---|---|---|---|
| **The surface's readings** — `Situation`, `Offer`, `account`, `dossier`, `explain` (person-side); `receipt` (host-side); each module's turn view, choice set and `trace` | **re-implemented** as person-side functions in the port's core and one host reader; **rendered** by `game/`, which computes none and holds no legal-choice list | `decision/sheet.py`, `queries/person_q.py`, `harness/play_surface.py`, each module | the sheet and one turn view built; the rest designed |

`harness/play_surface.py` is the seam and lives under `harness/` (the first audit's §9 noted it).
With `receipt` and the transcript it becomes the host half of the surface in fact; whether it moves
out of `harness/` is IN's call when a client exists, and nothing here depends on its path.

## B5. The Godot architecture specification, read against Layer 1 §C.12

`godot/godot_architecture_specification.md` (2026-04-11, 998 lines, read to the end). Its Status line
calls it STALE and "retained for its pipeline/procedure structure". Read part by part:

| part | says | against §C.12 and the code | verdict |
|---|---|---|---|
| 1.2–1.3, 3.1 | "One autoload. The Meta-Container … holds all persistent state"; all mutation through `Meta.receive_consequence()` (`:41`, `:233-305`) | **rejection 1**: `World` is not an autoload; D-2 and D-46 depend on it being unreachable by name | conflict; dead |
| 3.1 | a `Tracker` registry keyed `scope:owner:id` holding world clocks, faction stats and territory tracks, with a seasonal ±2 cap at one choke point (`:241-293`) | PART D: a Query is a function, never a stored aggregate; a faction is a Query return (§B.6.1); the stat vector was deleted | conflict; dead. The idea that survives is its last clause: one choke point for every mutation, which is the write gate |
| 3.3a | containers emit `consequence_reported`, `scene_completed`, `zoom_in_requested`, `scene_escalated`; the Conflict Container routes consequences by signal (`:380-450`) | **rejection 3**: the log is not signals; a signal carries no cause and no receipt | conflict as the state channel. As a `game/`-side notification after an append it is what rejection 3 permits |
| 3.3a | a zoom stack, outer scene suspended and dimmed, maximum depth three (`:455-481`) | the driver's one suspension (`loop/driver.py`), `contest_max_depth`, a typed refusal at the cap (§C.8–§C.10) | agrees in shape; the oracle owns the depth and the port only renders the nesting |
| 3.3a | "Containers do not know about each other" (`:45`) | a registered module takes a typed input and returns a typed outcome, reached by composition row | agrees |
| 3.3b | every modifier "sourced and traceable" (`PoolModifier.source`, `reason`) (`:489-501`) | §C.11's derivation; `OfferRow.terms`; SC-P1's `room` and `leverage` | agrees in intent; the nearest thing in the stale documents to the reason trail the contract types |
| 3.3b | five resolution modes; d10 pools, target number 7, exploding tens; a second non-exploding dice variant for the board game (`:505-523`) | one degree ladder read from `engine/dice_engine`; no second variant | conflict; dead (`CLAUDE.md` §6: pre-`d+σ`) |
| 3.4 | consequences are immediate or deferred; a cascade display that "is not a processing step", reading a visual queue (`:309-340`, `:559-561`) | barriers between steps; a presentation reads `account` and `receipt` | the second half agrees: display never processes. The first half is the retired phase model |
| 3.4 | "Domain Echo scope recognition … must implement this programmatically" (`:549-557`) | no GM; a faction is a view, so there is no echo to recognise | superseded |
| 3.5 | the Game Director awaits the player's slate choices, runs conflicts, then a strategic phase, then accounting (`:575-616`) | the seven-step season; the player is a `choose` callback inside DELIBERATE | conflict; dead |
| 4 | create a character or play a named one; "Both paths produce a `CharacterData` … treated identically" (`:633-637`) | `creation_sheet` and `seat` (C1); one agent type | agrees with the ruled half (pick a seated person); creating one is CENSUS's, unbuilt |
| 5 | "Save between seasons only" (`:652-667`) | R44; MODES §4 | agrees |
| 6 | installs an engine version and add-ons (`:673-698`) | ED-GO-0002 owns the version | not asserted here; superseded by the ledger row |
| 7 | the extraction procedure: values from parameter files, procedures from design documents, worksheets per document (`:702-794`) | `CLAUDE.md` §5: never take a number for the port out of prose; values cross behind an exporter | conflict in source (it extracts from prose); its distinction between a formula, a procedure and a trigger condition is sound vocabulary |
| 8–12 | phases, a daily workflow, verification by worked examples, a timeline | the port gate (B10-20); parity by content hash over replayed draws | superseded |

**What is binding for the port:** Layer 1 §C.8–§C.12 and PART E step 13 (ratified, ED-IN-0204);
`CLAUDE.md` §5 and §6; ED-1050; ED-GO-0002 for the version; the B10-20 card for the gate. **What is
not:** every `godot/` document but the README's pointer line; the conversion strategy (PROPOSED);
the UI set. **Stale inside the binding text:** the two §C.12 passages the first audit named (TEXT
items 4–6); nothing further was found on this reading. One sentence of §C.12 gains weight from the
player surface: rejection 3's "emit one per appended Event after the append, for the view layer to
consume" is correct for a developer's view and too broad for a player's, which is why SURF-B §7
narrows the trigger to the seated person's two readings. That is a rule for `game/`, stated in a
proposal; it does not edit §C.12.

## B6. Proposals, resolutions, and what returns to Jordan

### B6.1 The findings ranked, and the proposals that carry them

| rank | finding | severity | proposal |
|---|---|---|---|
| 1 | F-GO-15 no shared surface vocabulary; six lane dialects | blocks the standing requirement | SURF-B |
| 2 | F-GO-16 a person cannot read what his own act came to | degrades narrative (R-02 as met by a player) | SURF-B §3 |
| 3 | F-GO-19 the offer is flat and three to five times the legible size | degrades narrative | SURF-B §2; MODES §3 |
| 4 | F-GO-18 two kinds of play; two choice surfaces missed (**corrects** F-GO-08, R20) | correction | SURF-B §6 |
| 5 | F-GO-21 two opposite answers to what the player knows | degrades narrative | REF; §B6.3 |
| 6 | F-GO-17 `own_act` not computable (**corrects** SURF §3) | correction | SURF-B §4 |
| 7 | F-GO-13 the UI set's content half is not in the tree | degrades narrative | REF |
| 8 | F-GO-20 the stale Godot specification against §C.12 | hygiene | REF |
| 9 | F-GO-14 dead tracks in the newest UI document; a repair plan that stopped | hygiene | REF |

Three proposals written: `proposals/11_GO_player_surface_contract_B.md` (supersedes
`11_GO_player_surface_contract.md`), `proposals/11_GO_fidelity_and_campaign_modes.md`,
`proposals/11_GO_design_reference_disposition.md`. The first audit's §8 changes in one place: its
step 8 ("the offer's terms, `aftermath`, `OFFER-CONTAINS`") becomes, in order, CHAR's `watch` hook
and own-state decline → `Offer` and `Situation` → `receipt` and the transcript → `account` →
`OFFER-CONTAINS`; `dossier` follows FI-05. None is a port-gate member and none waits on the freeze.

### B6.2 Every inconsistency, gap and unclear passage found on this reading, decided

Ladder steps as in the first audit: 1 superseded · 2 irrelevant · 3 answered by a design document
or ruling · 4 precedent · 5 what makes sense for the architecture.

| # | kind | what | resolution | step | carried by |
|---|---|---|---|---|---|
| R48 | gap | v4 Parts 10–19 and §20.1–§20.2, to which v4.1 defers, are in no file | not reconstructed; the oracle's readings are the specification | 2, 5 | REF |
| R49 | unclear | the v4.2 workplan's standing (one stage of thirteen run) | a retired plan in quarantine; not a queue | 2 | REF |
| R50 | inconsistency | six lane shapes for what the player sees | one protocol: five readings and one scene pair | 4, 5 | SURF-B |
| R51 | gap | the outcome of a person's own act has no reading | `receipt`, host-side, own acts, depth one | 4, 5 | SURF-B §3 |
| R52 | inconsistency | SURF's `own_act` reads act ids from fields that hold person ids | `account` uses what the fields say; pairing is `receipt`'s; no carrier field | 3 | SURF-B §4 |
| R53 | inconsistency | "every scene through a typed decider" against SC's loop-played hearing | two kinds of play, named per subsystem | 3, 4 | SURF-B §6 |
| R54 | gap | the military menu is an unlisted surface that reads `World` | stays as ruled; named the pattern for payload-carrying verbs | 3 | SURF-B §2 |
| R55 | gap | nothing ties a candidate to the question it answers; declines are invisible | `OfferRow.occasion`; `Offer.withheld` for own-state conjuncts only | 4, 5 | SURF-B §2 |
| R56 | unclear | where a display cap lives | the client's constant; never a fixture; never removes a row | 4 | MODES §3 |
| R57 | inconsistency | CHAR's `DevelopmentSheet.terms` and SURF's two floats are one datum under two names | one field, `terms`, from the `watch` hook | 5 | SURF-B §2 |
| R58 | inconsistency | T-30 and the "Reported layer" against Oath II test 3 and §C.11 | §C.11 governs in play | 3 | REF |
| R59 | inconsistency | "every number the resolver uses is visible before commit" (contest walkthrough) against AX-2 | believed odds and his own operands; resolver-side operands only as held | 3 | REF |
| R60 | inconsistency | three campaign modes with per-mode rules against one loop | superseded; no mode enumeration | 1 | MODES §1 |
| R61 | unclear | ED-SC-0013 fork C, the calibration tolerance | no number: equal on matched decisions (a pin); no decider is the person's own policy | 3, 5 | MODES §2 |
| R62 | gap | the "witnessed" fidelity (refines R46) | presence: firsthand `account` rows, and the scene's `trace` or report where a module returns one | 5 | MODES §2 |
| R63 | unclear | difficulty as 5 / 4 / 3 actions; Core and Full complexity tiers | a `Fixtures` overlay on `scene_budget` at world build; tiers not built | 5, 2 | MODES §3 |
| R64 | gap | creation shows nothing of a seat's place in the world | `CreationRow.holdings` | 5 | MODES §4 |
| R65 | gap | how a campaign ends for a client | extinction (built) or the player concludes; the chronicle and account read then; no victory screen | 3 | MODES §4 |
| R66 | inconsistency | the specification's single autoload | §C.12 rejection 1 | 3 | REF |
| R67 | inconsistency | container signals and a 50-signal bus as the state channel | §C.12 rejection 3; signals after the append, at `game/` only | 3 | REF |
| R68 | inconsistency | one seeded generator, "all rolls … from the same sequence" (v4 §24.11; spec Part 3) | keyed draws, threaded; a single sequence makes an outcome depend on call order | 3 | REF |
| R69 | inconsistency | d10 pools and a board-game dice variant | the one degree ladder | 1 | REF |
| R70 | inconsistency | a registry of stored faction and clock trackers | no stored aggregate; the write gate is the one choke point | 1 | REF |
| R71 | unclear | the specification's Status line names the strategy as governing | the line names §C.12 | 3 | REF edit 1 |
| R72 | gap | `finding.none` reaches no ledger, so a failed inquiry shows its maker nothing | the receipt shows it; whether "nothing found" is a belief is FI's | 5 | SURF-B §3 |
| R73 | unclear | may an actor always learn the band of his own act | yes; a row that must hide it declares `receipt: none`; no row does today | 5 | SURF-B §3 |
| R74 | inconsistency | lanes' scenario summaries read `World` and are offered as the player's view | instruments; every scenario prints through the transcript | 4 | SURF-B §8 |
| R75 | gap | `engine_atlas_v1.md` anchors to a driver that no longer exists | no action; not cited | 2 | REF |
| R76 | unclear | the UI's "locked by Conviction, override costs a scar" has no carrier | not a lock: an ordinary row with a negative stance term; the cost is the fold's | 3, 5 | SURF-B §2 |
| R77 | gap | the Scene Slate has no generator in code | it is `View.questions` in attention order with the scene budget; no second generator | 1 | SURF-B §1 |
| R78 | gap | what triggers a staged presentation | an `AccountRow` or `ReceiptRow` of the seated person, never a log Event | 3 | SURF-B §7 |

Thirty-one resolutions (R48–R78). R52 and R53 correct the first lane's R17 and R20; R62 refines its
R46.

### B6.3 Survivors for Jordan

One, and it is not the first audit's.

**May the end of a campaign show the player what his person never knew?** In play the answer is
ruled: no (§C.11). At the end it is open. The quarantined ending design asks for a "World Footprint
(counterfactual impact)" and "The World They Leave"; T-30 makes the gap between the two views the
point of the game; and the oracle already has the instrument (`harness/chronicle.py` renders the
deepest causal chain "OUTSIDE the simulation"). Ladder: not superseded (the ending design was never
built or struck); not irrelevant; §C.11 rests on "anything shown before they declare is shown inside
a decision", and after a line is extinct or concluded nothing is declared, so the ruling is silent;
no precedent in the tree; and the architecture serves either.

- **E1, the truth is never shown.** The portrait is `chronicle` and `account`: what he believed,
  false beliefs included. The world stays a place of permanent partial knowledge, and a second
  campaign in the same world can still be surprised by it.
- **E2, the truth is shown at the end.** After a line ends (and only when no continuation is taken,
  or the truth would reach the next seat's decisions), the client may show the chain a developer
  sees. The player learns which beliefs were false and whose hand was behind an unattributed fall.
  That is the detective genre's closing reveal, and it makes each campaign a case that resolves.

They differ as games in whether mystery is permanent or deferred. MODES §4 builds E1 because it
needs nothing; E2 is one host-side reading at one moment and can be added without touching E1.

## B7. Evidence log and reading record

### B7.1 Commands and probes

All seeded runs: `populated.build_realm(0)`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`. Scripts
and outputs: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/GO_B/`.
No `pytest`, no long `aperture` run.

| id | command or probe | seed · seasons | outcome |
|---|---|---|---|
| E-B1 | `grep -n "^# PART" valoria_ui_ux_v4.md`; the v4 index's heading table | — | Parts 0–9 and 21–25; "§20.3 … continued" at `:1714`; the index (generated 2026-04-18) lists the same |
| E-B2 | `grep -rIl` over `*.md`, hidden trees included, for "THE CUTSCENE SYSTEM", "PART 19 — ", "PART 15 — PARLIAMENT"; `ls` for a v4.2 document; `ls engine/mc_v18.py references/ENGINE_ATLAS.md`; `grep -rn render_protagonist_lens --include=*.py` | — | only this file matches; no `valoria_ui_ux_v4_2.md`; both atlas referents absent; no `render_protagonist_lens` |
| E-B2c | `case_extract.py` through `harness/run_cases.load_cases` | — | 143 cases, 972 needs; 81 name a player (need or reason), 185 use seeing vocabulary, 243 either; 281 knowledge rows, 46 naming a player. A regex count of the legibility classes is in the script's output and is a floor; the table in §B3.8 is by hand |
| E-B3 | `surface_probe.py 0 1 p_npc_001` (seated with `take_ranked`; `military_menu.menu` for all 83 at build) | 0 · 1 | hash `5ab73af282d0779646c38839fbab85d8` (equal to the first audit's plain run), 13,379 Events, 749 acts. Menu: 43 serve a faction, 43 may mint an army, 0 command one. Five sheets: sources `need`, `claim_landed` ×4; candidates 22/32/33/32/38; budgets 5/5/4/3/2; 33 distinct verbs of 66 resolvable; `View.odds` a function. 15 acts, 15 direct Events, 2 with degree, 10 with `observed`, 0 with `ending`. 119 claims deposited: 42 firsthand, 77 `told_by`, 40 with `doer`, 0 with a chain; 0 claim fields equal to an Event id |
| E-B4 | `surface_probe2.py` (plain run; each of his acts against his ledger) | 0 · 1 | same hash. `finding.none` (Failure) ×2: 0 claims of that kind held. `sabotage.refused`: 1. By `(kind, act subject)`: 7 of 15 matched. 0 claim ids are act ids. `observed` example `Observation(subject='set_s_001', predicate='stores:grain', value=40)`. Claims by round: 28/19/26/27/19 |
| E-B5 | `surface_probe3.py` (every act against every other ledger, by kind and subject, anchor or actor) | 0 · 1 | same hash. 318 of 749 acts matched in another person's ledger (42.5%); 60 of 83 persons with an act so matched; `p_npc_001` 0 of 15, `p_npc_033` 6 of 6; 1,215 `Seen.who` claims naming 35 persons. One seed, one matcher |
| E-B6 | `grep -ln "ReceiptRow\|AccountRow\|AftermathRow" proposals/*.md` (the suite); `grep -rn valoria_ui_ux tools engine modules tests`; `grep -rn "Disposition table" engine modules --include=*.py`; `git ls-files \| grep parliamentary_vote` | — | GO's files only; 0; 0; nothing |
| E-B7 | `git status --short`, `git diff HEAD --stat` on this lane's four files, at the end | — | this lane wrote four files and edited no other. It did not commit: the suite's own sweep commit `2d909d9` (02:56 UTC) had already taken them in, and a later edit to this row leaves this file modified against it. Other lanes' files were changing in the same tree throughout. One early append to this file was made with a shell heredoc before the lane switched to the edit tool; the text it wrote is the F-GO-13 and F-GO-14 entries as they stand |

### B7.2 What was read, and what was not

**Read in full.** The brief; `CLAUDE.md`; the first GO audit and its dossier; SURF, GATE and TEXT.
The UI set: `valoria_ui_ux_v4_1.md`, `valoria_ui_ux_v4.md` (to its end; what the file holds),
`valoria_ui_ux_v4_1_max_audit.md`, `valoria_ui_ux_v4_2_workplan.md`, the derived-settlement
supplement. Cross-cutting: `auto_manual_resolution_duality_v1.md`, `cogload_moderate_target.md`,
`campaign_modes_v30.md` and its infill, `campaign_architecture_v30.md`, `companion_app_design_note.md`,
`complete_systems_reference.md`, `subsystem_flow_skeletons_v1.md`, `engine_atlas_v1.md`,
`integration_proposal_v30.md`, `throughlines_complete.md`. `godot/godot_architecture_specification.md`.
`04_CODE_ARCHITECTURE.md` `:845-1017` and `:1106-1146`. Code: `decision/sheet.py`,
`harness/play_surface.py`, `harness/military_menu.py`, `queries/inputs.py`,
`state/carriers.py:240-614`, `modules/combat/fight.py:55-117`. `.audit/`:
`2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md`,
`2026-07-29-scenario-visualization/00_findings.md` (the remainder the first lane had not read),
`2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md`. `chain/CASE_BRIEF.md`.

**Read in part.**
`[PARTIAL: the case bodies — 243 of 972 needs and 46 of 281 knowledge rows in full, chosen by the matcher in case_extract.py; the head of one file read raw; the narrative fields (one_line, temporal, ends_when, who_acts) were not read case by case]`.
`[PARTIAL: the twelve sibling proposals that define a playable surface — headings and the interface sections of each, not the whole]`.
`[PARTIAL: harness/interactions.py :1-94; the heads of storybar, report, chronicle, aperture, exercises, obligee_report, heir_hears, army_presets; modules/mass_battle/massbattle.py :440-520; modules/combat/wrapper.py :553-597]`.
`[PARTIAL: the four UI index files and the campaign_architecture, cogload and integration_proposal index files — generated heading tables; the v4 index's table was read for F-GO-13, the others opened at their heads]`.

**Not read.**
`[SKIPPED: .audit/ beyond the three files above — about 7 MB in 32 other entries, among them the emergent-narrative-engine v2 and its 800 KB of workings, the NERS qualitative audit, the social-contest three-lens audit and the combat customization state; a directory listing and file sizes only. Nothing from them is cited]`.
`[SKIPPED: the other .designs/systems/_architecture documents not named in the charge — player_agency_v30 (cited here only as quoted by the documents that were read), scale_transitions_v30, hybrid_gaps_v30, conflict_architecture_proposal, early_game_ignition_analysis, propagation_spec_v1, the key and governance registries, derived_stats_v30, decision_policy_v1, and the rest; about 700 KB]`.
`[SKIPPED: the float-contract and one-draw-owner proposals — outside the player-facing charge; known from the first audit's §3 and §6]`.
`[SKIPPED: jordanelias/valoria-game — another repository, not attached]`.
The reason for each skip is the reading budget of one lane; the player-agency document is the one
whose absence most limits §B3.1, and its rows there rest on quotation at second hand.

