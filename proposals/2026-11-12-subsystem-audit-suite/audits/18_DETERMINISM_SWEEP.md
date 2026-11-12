# 18 — Determinism sweep: the suite and the code against "we do not do deterministic"

## Status: REFERENCE — a terminal sweep (CLAUDE.md §0, the RULED exception). Corrections land as edits in finished lanes' files and as proposals `proposals/18_DETERMINISM_*.md`; nothing here resolves anything at runtime.

Rule swept against: `AUDIT_BRIEF.md` "Standing rule (Jordan, 2026-11-12, emphatic)". The test applied to
every hit: *could this go either way for the people in the fiction?* If yes, and the text or the code
decides it from state alone, it is a finding. **Not findings:** seeded replay; arithmetic bookkeeping
(stores conserved, a clock's tick, an id, the aggregation of weights such as noisy-OR); eligibility
(may this act be attempted at all); and a person's choice that is itself sampled (the chooser's
`softmax(score / choice_temperature)` in `decision/choose.py::_sample_order` is a draw whose odds his
interior sets — so a choice taken by that sampler is compliant, and one taken by a top-score pick is not).

Read at the working tree of 2026-11-12, `PYTHONHASHSEED=0`. Fan-out: none (0 agents; one reader held the
suite and the code paths, and no judgment node here is one a second reader would see differently enough
to pay for).

## Verdict

**The documents are mostly conformant already; the code is not.** Of the suite's finished lanes, ten
passages made a consequential outcome a fixed function of state (D-01 to D-10). All ten are corrected in
place, each file carrying a `Reconciled:` line at its head. Nine further passages in running lanes are
listed for those lanes (§3) and were not edited. The running VERBS, SC-interrogation (13), WR addendum,
LACUNA (19) and INSTITUTIONS lanes are already writing draws for most verbs; they are the owners of the
per-verb band maps, and this file does not write a second copy of any of them.

**In the code, the structural fact is one line of `engine/season/loop/resolve.py`.** An act whose verb row
carries no `contests:` and no `graded_inquiries` route takes `_fold` with `resolution=None`, and every
effect on that path applies on eligibility alone. That is 53 of the 67 verb rows. Measured on the realm
(`build_realm`, seeds 0 one season, 1 and 2 two seasons; 3,826 resolved acts): **385 events carried a
degree, and 1,995 of the 2,159 success events (92 %) were decided with no draw.** Removing the pure
bookkeeping (`create_record`, `utter`, `commit`, `convene`, `dispatch`, `oblige`, filing a `petition`,
`give`, `transfer` between one's own rungs), **727 consequential outcomes in five realm seasons were fixed
functions of state** (findings made, wounds healed whole, forgeries and covers of one fixed quality, writs
binding, journeys arriving, cases docketed, stores taken). Ranked by the play it decides, the top five:

1. **C-02 — who learns of a deed** (`epistemic.observers_for`, `loop/witness.py`): every person a channel
   admits deposits the claim, with certainty. Every belief in the game starts here (84,443
   `claim.deposited` over seeds 0–4, two seasons, the hole register's HR-9 control). Proposal:
   `18_DETERMINISM_notice_is_a_draw.md`.
2. **C-01 — the uncontested fold** (`resolve.py::_fold`, `resolution=None`): 53 rows, 92 % of success
   events. Proposal: `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (the one route, the loader's
   refusal, the class of every row; per-verb bands owed to the VERBS lanes where they state them).
3. **C-03 — inquiry that always finds** (`reconstruct` 244 findings of 251, `survey` 32, `interview` 18,
   `thread_read` 5): knowledge-making without resistance. Same proposal as C-01 (graded route).
4. **C-06/C-13 — violence with one outcome**: a plain `fight` kills 200 of 200 (F-PC-04); at season
   scale a heavy fighter never loses to a light one (0 deaths in 1,000, `03_PC_audit.md:332`) because the
   `UPSET_FLOOR` flip moves `result` and the fold reads the trackers; a defended field is lost by the
   attacker 60 of 60 (F-MB-01). Low frequency, highest stakes (deaths, territory). Proposals:
   `14_VERBS_PHYSICAL_A` A3 (mortal draw, adopted by `03_PC_exits_withdrawal_recovery.md` Part B),
   `04_MB_headcount_grade_and_scale.md` gate 2, and `18_DETERMINISM_no_certain_matchup.md` (new).
5. **C-07 — the binding acts and rival claims**: `issue` (49 dispensations), `release`, and, the moment
   they are admitted, `confer`, `revoke`, `succeed`, `pardon`, `establish`, `seize` — each takes effect
   with certainty; and when two acts in one RESOLVE want the same seat, store or Record, the canonical
   order (a content hash) decides who wins, with no contest. Per-verb draws: `14_VERBS_BINDING_*`; the
   rivalry: `18_DETERMINISM_rival_acts_in_one_fold.md` (new).

Counts: **documents — 19 deterministic resolutions found (10 corrected in finished lanes, 9 owed to running
lanes); code — 15 sites found (C-01 to C-15), 4 new proposals; 0 corrected in code (no lane edits code).**

## 1. Documents — finished lanes, corrected in place

| id | file : line (as found) | the claim | why it is deterministic | corrected design (in the file now) |
|---|---|---|---|---|
| D-01 | `proposals/05_SC_evidence_and_rebuttal_B.md:52-61, 79-93` (+ `05_SC_evidence_and_rebuttal.md` edit 5; `08_FI_05_evidence-interface_B.md` E-6; `audits/05_SC_audit_addendum_B.md:305, 473, 489`) | "entering and striking are deterministic"; the heavier item stands, the lighter is struck; a forgery finding strikes every item of its origin | an answer's success could go either way in the room; weight alone decided it (G-65) | filing is bookkeeping; standing against an answer is the **answering act's draw**: pool = the answerer's `speak` pool; obstacle = `answer_ob` (proposed 2) `+ proof_step × (w_answered − w_answer)` (impeachment: `− finding confidence`) + the room's modifiers; Failure stands · Partial both halved · Success struck · Overwhelming struck + origin-wide strike/fault. One rule shared by SC `_B` and FI E-6; admission deferred to `19_LACUNA` |
| D-02 | `05_SC_playable_hearing_B.md:104` (move table); `05_SC_hearing_capabilities.md:60`; `05_SC_audit_addendum_B.md:299` | `answer`: "none (no draw): the lighter of the pair is struck" | same as D-01, in the room | `answer` is a rolled move with a capability (by rung, as `argue`); bands as D-01 |
| D-03 | `05_SC_playable_hearing_B.md:115-117`; `05_SC_audit_addendum_B.md:314-318` | fault `silence`: "the rung is conceded"; faults are "deterministic conditions" | a bench may still find for a silent party; a rule ended the rung | `silence` = two levels against that side on the closing draw; faults move odds, never the verdict; `forgery_found` only on an Overwhelming answer |
| D-04 | `03_PC_exits_withdrawal_recovery.md` Part B | "a plain `fight` is to the death" left open as Jordan's | a felling is death with certainty (200 of 200) | decided by the standing rule (ladder step 1): the death is `14_VERBS_PHYSICAL_A` A3's mortal-wound draw, adopted (not restated); terms follow context |
| D-05 | `03_PC_exits_withdrawal_recovery.md` Part C | `tend` restores a fraction of headroom, certain | whether a wound mends could go either way | `tend` through the one task draw: pool = tender's `healing` (or `pool_default`), obstacle = `tend_ob` (1) + the patient's marks; Failure none · Partial half the fraction · Success the fraction · Overwhelming to ceiling |
| D-06 | `05_SC_playable_hearing_B.md` "Who decides"; `05_SC_negotiation_scene.md` "How each side chooses" | the NPC decider "draws nothing"; consent decided by the decider's valuation | a top-score pick makes a person's consent a fixed function of the board | the decider samples through `_sample_order` on a keyed stream from the host; consent stays a choice, and the choice is a draw |
| D-07 | `06_FA_levy_through_the_seat_B.md` | the levy decides who may raise; silent on turnout | a levy that raises the asked amount is certain | note: turnout is `recruit`'s graded draw (`14_VERBS_MILITARY` §3); this file is eligibility only |
| D-08 | `06_FA_playable_scenario.md:40` | "the heir's `succeed`"; set-up acts at tick 0 assumed to take | succession and the set-up acts certain | `succeed` is a draw (`14_VERBS_BINDING_C`); a failed set-up act is reported as the opening situation, never forced or seed-picked |
| D-09 | `06_FA_audit_addendum_B.md:300-305` | "a sole heir the apparatus accepts inherits"; "whether the realm splits, by the deterministic gap" | inheritance and schism by rule | the heir's claim, the election's ballots and any split are draws (BINDING_C; 13's ballot row) |
| D-10 | `07_SE_audit_addendum_B.md:156` | "Governing acts do not roll … the right one to keep" | every settlement verb certain on eligibility | overruled (ladder step 1): every settlement verb that could go either way rolls through the task route; only own-rung bookkeeping is exempt |

Checked and conformant (no edit): `06_FA_decree_binds.md` (suspicion's threshold raises a question the
chooser samples; the recall is `revoke`, a draw once BINDING_C lands); `08_FI_08_knots-season-form.md`
(a strain threshold raises a question, not an outcome); `03_PC_duel_round_and_approach_B.md` §5 (approach
sampled); `05_SC_acquittal.md` (a draw at 0.26); `05_SC_hearing_capabilities.md` `insight_bench_threshold`
(what a seat sees, not an outcome); `08_FI_02_rumour-that-travels.md` edit 3 (which held claim a teller
says is picked by a tier order — content selection inside an act that itself rolls; borderline, left).

## 2. Code — every place a consequential outcome is decided without a draw

Evidence run: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/det_probe.py`
(`build_realm(seed)`, the shipped chooser over `resolvable_verbs()`, counts per verb of resolved acts,
success kinds and events with a degree), outputs `…/scratchpad/runs/DET/realm_s0.json` (hash
`5ab73af2…`, matching the FI audit's seed-0 one-season hash), `realm_s1_2season.json`,
`realm_s2_2season.json`; verb classes from `…/runs/DET/verbs.txt`. Ranked by play decided.

| id | site | what is decided without a draw | play decided (3 seeds, 5 seasons) | corrected design | proposal |
|---|---|---|---|---|---|
| C-02 | `epistemic.py:794-834::observers_for`; `loop/witness.py` deposit | whether a present person notices a deed | every deposit (84,443 / HR-9) | a **notice draw** per admitted witness of a deed whose kind is covert or concealed, or whose channel is not co-presence; overt public acts to the co-present stay certain (they are the act's publicity, an eligibility of channel) | `18_DETERMINISM_notice_is_a_draw.md` |
| C-01 | `loop/resolve.py:1079-1111` → `_fold(…, resolution=None)` | every effect of 53 rows, on eligibility | 1,995 of 2,159 success events | every writing row declares `resolution:` ∈ {`contest`, `task`, `bookkeeping`}; `task` goes through `seam.grade` (the graded route `research` already takes); the verb loader refuses a writing row with none, and refuses `bookkeeping` on a row that writes another person's body, tenure, capability or stores | `18_DETERMINISM_task_draw_for_uncontested_verbs.md` |
| C-03 | `verb_table.yaml` rows `reconstruct`, `interview`, `thread_read`, `survey` (flat `finding.made`; `_eff_survey`) | a finding is made, or a sheet drawn up true, with certainty | 299 | `task` (C-01): pool `inquiry`/`copying`; bands Failure none · Partial finding at half confidence / withheld hand · Success finding · Overwhelming finding + a second read; `interview` per `13_SC_draw_for_unrolled_contests.md` (opposed) | C-01's; band rows owed to `14_VERBS_MATERIAL`, 13 |
| C-04 | `loop/effects_combat.py:767-790::_eff_tend` | a body restored to its ceiling | 118 | D-05 | `03_PC_exits_withdrawal_recovery.md` Part C (edited) |
| C-05 | `effects_information.py:843::_eff_forge` (`default_forgery_quality`, a constant); `_eff_conceal` | every forgery of one quality; every cover perfect | 90 + 72 | `task`: the forger's `copying` against `forge_ob`; the band sets `forgery_quality` (Partial low, Overwhelming high), which the examining draw already reads as obstacle; `conceal`'s band sets the cover's quality, which `surveil`/notice read | C-01's; owed to `14_VERBS_MATERIAL` / `SOCIAL1` |
| C-07 | `effects_governance.py` `_eff_confer`, `_eff_revoke`, `_eff_succeed` (`:146-182`, "the first valid claim wins"), `_eff_release`, `_eff_pardon`, `_eff_establish`; `effects_information.py` `_eff_issue` | an appointment takes, a man is stripped, an heir reigns, a writ binds | `issue` 49, `release` 4; the rest refused today, certain when admitted | per-verb draws: `14_VERBS_BINDING_A/B/C`, `14_VERBS_SOCIAL1_B` (obedience) | owed (running) |
| C-08 | `effects_information.py:1000-1085::_eff_seize`, `_seize_rung` ("asks nothing of the defenders"); `effects_governance.py:511::_eff_requisition` | a Record or a town taken; stores taken | 6 + 6 (seize refused 6 today) | `seize` against the holder: `contest` (`a standing`); `requisition`: `task`, the rung's people's resistance as obstacle, the band the share of `amount` taken | C-01's; bands owed to `14_VERBS_MATERIAL` |
| C-09 | `effects_migration.py::_eff_move`, `_eff_migrate` | a journey arrives | 45 + 13 | `task`: the road's hazard (`travel.blocked`'s predicate becomes an obstacle term where it is not an eligibility); Partial arrives a step short, Failure turned back | C-01's; owed to `14_VERBS_PHYSICAL` |
| C-10 | `effects_information.py` `_eff_open_case`, `_eff_carry` | a matter docketed | 23 + 8 | `13_SC_draw_for_unrolled_contests.md` (docketing row) | owed (running) |
| C-11 | `loop/resolve.py:51::_canonical_order` + scarcity refusals (`_eff_requisition` docstring: "the second finds it short"; `_eff_succeed`: "the first valid claim wins") | which of two rival acts in one RESOLVE gets the seat, store or Record | unmeasured (a rivalry count is the proposal's first gate) | an opposed draw between the rivals sets their fold order; graded (Overwhelming all, Partial split or disputed) | `18_DETERMINISM_rival_acts_in_one_fold.md` |
| C-13 | `modules/combat/wrapper.py:618-624` (`UPSET_FLOOR` flips `result`; the season fold reads the trackers, F-PC-06) | at season scale a heavy fighter never loses to a light one | every mismatched `fight` | the upset becomes diegetic: a critical opening drawn inside the exchange through `core.resolve`, so the trackers record it and the fold sees it | `18_DETERMINISM_no_certain_matchup.md` |
| C-06 | `modules/mass_battle/massbattle.py::_weighted_unit`; `resolve_field` | a defended field is lost by the attacker 60 of 60 | 18 marches, every opposed field | `04_MB_headcount_grade_and_scale.md` (one scale owner); its gate 2 (the verdict varies by seed) is the acceptance, kept | `04_MB_headcount_grade_and_scale.md` |
| C-12 | `modules/combat` default terms + `seam/wrappers/combat.py` | a felling is a death | 200 of 200 (F-PC-04) | D-04 | `14_VERBS_PHYSICAL_A` A3 |
| C-14 | `queries/world_q.py:737::declared_votes` as a hard conjunct (`verb_table.yaml:390`) | a verdict by count of commits | `excommunication_deliberation` only | each ballot drawn (13's ballot row) | owed (13) |
| C-15 | `effects_combat.py:794::_eff_train`; `effects_army.py::_eff_recruit`; `effects_economy.py` `_eff_work`, `_eff_restore`, `_eff_sabotage`; `effects_founding.py` `_eff_build`, `_eff_found`, `_eff_raze` | a capability raised by one; men raised as asked; a site worked, mended, damaged, built, founded, razed | refused today (train 177, sabotage 87, raze 40 attempts), certain when admitted | `task` (C-01) with bands per verb lane | C-01's; owed to `14_VERBS_MATERIAL`, `MILITARY`, `PHYSICAL` |

Not findings in code (checked): the chooser (sampled, `choice_temperature` 0.05); `loop/matter.py:730`
body hazard (drawn); `world_q.subsistence_draw` (drawn); `witness.py:136` confiding (drawn);
`seam/ladder.py` and `degree_from_net` (the roller); `modules/fieldwork/find.py` (draws nothing because
the roll that decided it is upstream — compliant where the upstream verb rolls, which C-03 fixes for the
flat ones); `determine` (draws; its no-spread odds are 13's tables, not a determinism finding).

## 3. Owed to running lanes (not edited; nothing sent)

| to | file : place | finding | what the correction must satisfy |
|---|---|---|---|
| 13 (SC interrogation) | `proposals/13_SC_draw_for_unrolled_contests.md` negotiation row | `covenant` acceptance by a contest roll, while SC-B2 (finished, D-06) makes consent the counterparty's **sampled** choice: two rules for one outcome (an S defect) | pick one in one place. This sweep's reading: consent is the sampled choice in both paths, and 13's roll is the persuasion (`argue`'s told deposit) that moves his valuation. Either is non-deterministic; two is not allowed |
| 13 | `audits/13_SC_contest_interrogation.md` §4 cell 9 | lists the ballot as "a verdict by count"; the shipped site is a hard conjunct on `determine` (C-14) | confirm the ballot row replaces the `vote` conjunct, not adds a draw beside it |
| 14 VERBS (all) | every verb section | band maps for C-03, C-05, C-07–C-10, C-15 | each band map lands as a `writes_by_degree` row on the route C-01 makes mandatory; the class (`contest`/`task`/`bookkeeping`) is declared on the row |
| 14 VERBS MATERIAL | `tend` | D-05 already corrects `tend` in PC's file | supersede or adopt D-05 explicitly, so there is one `tend` rule |
| 14 VERBS SOCIAL2 | `audits/14_VERBS_SOCIAL2.md:211` | `petition`: "no roll: a filing is a fiat" | conformant as filing; confirm the addressee's response is the drawn act |
| 19 LACUNA | `19_LACUNA_admission_rides_the_citing_draw.md` | admission to the case file: FI E-2 (at the citing band) vs SC `_B` (filing draw-free) | decide once; both files now defer to it |
| WR addendum | `09_WR_strand_conclusion.md`, `09_WR_world_motion.md` (first lane), `09_WR_audit.md` R-26 | endings and a strand's conclusion "reached when a count crosses"; wear a fixed amount | `09_WR_B_draws_not_thresholds.md` is writing this; confirm it reaches the first lane's two proposals |
| INSTITUTIONS | `15_INSTITUTIONS_VENICE.md:709-714` | lists deterministic text in other lanes | cross-check against §1 here so no finding is listed twice with two corrections |
| PESSIMIST | `16_PESSIMIST_GAME.md:37` | "ten verbs succeed every time they are admitted with no roll" | its count and §2's should agree on one definition of "draw" (events with a degree) |

## 4. Gate for this sweep's own claims (run, not asserted)

- *"92 % of success events carry no degree"*: the probe above, three seeds; control — `research`,
  `surveil`, `tell`, `lie`, `argue`, `speak`, `march`, `capture`, `determine` (the routed rows) all show
  `drawn = resolved` or more, so the instrument sees a degree where one exists.
- *"53 of 67 rows take the uncontested fold"*: `…/runs/DET/verbs.txt` (contests empty and no graded
  route; 11 contested, 3 graded). Falsifier: a row with neither whose success events carry a degree in
  the probe — none. Control check run: for the routed rows, events with a degree ≥ resolved acts at
  every seed (e.g. seed 1: `research` 95/95, `surveil` 23/23, `march` 5 acts / 11 graded events).
