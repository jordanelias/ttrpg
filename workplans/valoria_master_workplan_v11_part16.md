# Valoria master workplan v11 — carried entries and new positions, part 3: the strife positions (T04 · lane IN)
## Status: PROPOSED, ratified on merge (ED-1094, ED-IN-0312).
## Lane: IN (cross-cutting).
## Grade under `CLAUDE.md` §0.2: `paper`. IDs allocated: none (ED-IN-0312 is the head's).

## 1. How to read

Format as `-04` §1: `### <handle> — <title> (<lane>) · BATCH <…> · STATE <…> · R <rows>`, then WHAT, LANDED ALREADY, REMAINING UNBUILT, GATE (with NEEDS), EXIT and FALSIFIER, HASH MOVERS, HOLES AND LEDGER IDS, ASKS ATTACHED, RE-BASE, BUILDER and SOURCE. Each strife entry adds four lines: **FILES** (what the position edits), **VERB CLUSTER** (whether it joins P13's serialisation), **LAYER 1** (the `04`/`01` row it touches, opened at the row, and whether it needs a hunk) and **N-LINE** (rule V1's form, restated at the batch's re-base). HASH MOVERS names, for a mover, the pre-change `build_realm(0)` reading it takes (P14: the previous item's recorded after-reading, not a fresh run).

**The home.** Every entry's design home is `strife-00` (the batch it names in §8) and, for CR-75 to CR-77, `strife-01`. Those files are PROPOSED and held back in full; the entry here is the plan's spec, and where it departs from the home it says so and why. `strife-00`'s assumptions A1 to A12 are carried by the entries that rely on them, each `[ASSUMPTION; medium; Jordan to correct]` with the revert `strife-00` §10 states; `strife-00`'s R1 to R18 are Jordan's rulings of 2026-11-04 and `strife-01` §6's five calls are the orchestrator's, taken on narrative grounds at Jordan's instruction. No other ruling is asserted.

**Positions, by batch.** B11-S2: CR-71. B10-11: CR-72. B10-18: CR-73. B10-18b: CR-74. B11-S3: CR-75, CR-76, CR-77. B11-S4: CR-78. B11-S5: CR-79. B11-S6: CR-80. CR-70 is a retired handle (the story-telling fold dropped it, ED-IN-0311) and is not reused (P4).

**What is not a position, so nobody re-files it.** S1 and S1r are built (`60d13a7`, `79419b7`). `strife-00` §8 S2's lane for the foreign nations' natural-play frequency (H-233) is answered by S1r's readings (side O marches 12, 3, 4 and 6 at seeds 0 to 3, four seasons; `strife-00` §7's table row "unmeasured here" predates them); what remains is a value, `[OPEN — Jordan tuning]`, as `-03` B10-18 and the head record for the march frequency. The bodies lane (DR, DN) is a reading at B10-18's close after CP-T10-05 (`-03` B10-18's exit), because `age_step` and `illness_rate` ship 0.0 and their values are Jordan's (P11). `strife-00` §0's `queries/situation_q.py` is not built: CR-76 and CR-77 place both readings in `queries/world_q.py` (CR-76, LAYER 1).

## 2. The positions

### CR-71 — The strife funnel: why the routed codes stay unseen (IN) · BATCH B11-S2 · STATE MEASURE (a reading; edits no file under `engine/` except one hole row per unowned clause) · R — (an instrument reading)
- WHAT: for every code of `strife_moves.yaml` that has a static route (`harness/strife.py::route`) and reads 0 at every seed run (graded UNOBSERVED by signature, or KIND-ONLY with a count of 0), name the verb, the deepest funnel stage its acts reach (formed, attempted, admitted, executed: `harness/aperture.py`'s per-verb funnel) and the read that decided each refusal (REM-11's reasons, `aperture`'s "why each refusal refused" block), and the position of this plan that owns that read. `strife-00` §7: "the aperture funnel per verb first (which clause refuses it); change nothing before that." No reader is written: `aperture` owns the funnel and the reasons, `strife.py` the code-to-verb map, and this position joins their outputs in its commit body. A finding routes to its owner: a read owned by a position is written into that position's RE-BASE line (`-04`, `-04` part 2) as one sentence naming the read and this commit (expected owners, re-derived at entry: `evade / defy` CR-48; `arrest` and `pardon` CR-51; `covenant` CP-T09-03 and `determine` B10-18c; `succeed` IN-61; `establish` CR-25; the two field outcomes REM-32 and CP-T04-*; `release`, `commit`, `forgive` as the funnel finds them). A read no position owns is one row in `engine/season/hole_register.yaml` (P8: the gap was measured), not a new position. A default that keeps a code dark is named with the batch that owns its file; its flip is a position of that batch, written by a later fold, never built here.
- LANDED ALREADY: S1 and S1r (the signatures, the residue, `route`, `terminal_codes`, `routeless_terminals`); `aperture`'s funnel and reasons (REM-10, REM-11, REM-14; CR-14's pooled census).
- REMAINING UNBUILT: the reading; the RE-BASE sentences; any hole row.
- GATE: B10-09 merged (both closes). NEEDS: none. It runs beside B10-10 in its own worktree: it edits nothing B10-10 edits.
- EXIT and FALSIFIER: one line per code, `<code> <verb> <deepest stage> <deciding read> <owner | H-nnn>`, from `python -m engine.season.harness.aperture 2 --seeds 0 1 2` and `python -m engine.season.harness.strife 2 0 1 2` on one recorded sha (P10: two seasons is the horizon). FALSIFIER: a line naming an owner whose entry does not reach the named read is a routing error, found by opening the owner's entry at that read before the commit (`CLAUDE.md` §0.1 pt 3, "as `F` says at `:L`"). CONTROL: both instruments re-run on the same sha read identically, and the code-to-verb map printed equals `route`'s.
- HASH MOVERS: none (no code edit).
- HOLES AND LEDGER IDS: one row per unowned read, if any.
- ASKS ATTACHED: none.
- RE-BASE: re-derive the zero list on the base sha. `strife-00` §7's ten (RF, RG, CL, NG, WA, WR, DA, CA, AM, XN) come from #553's first-draft run, before side-aware grading. An unsaved run whose per-seed totals match the S1r receipt (shipped realm, four seasons) read RF, CL, NG, WR, CA, AM and XN at 0 at every seed 0 to 3, and RG, WA, DA and PU at 0 at some; XE and DN were UNOBSERVED at every seed and are not funnel codes here (XE is CR-72's; DN has no route, by design). These figures are the expected shape only, never quoted as the base.
- FILES: none under `engine/` but `engine/season/hole_register.yaml` (an unowned read); `-04` and `-04` part 2 RE-BASE lines.
- VERB CLUSTER: no.
- LAYER 1: none: harness readers resolve nothing and write nothing (`04` §A.2's `queries/` read discipline, which they keep).
- N-LINE: the funnel reading — cut it and the gameplay experience is worse, because the turns the study's cases most often take after a rising begins (a refusal, a claim, talks, a capture, an amnesty, a change of regime or border) stay unreachable with no named cause, and the positions built to reach them close on their own falsifiers with nobody having checked that they reach the read that refuses them.
- BUILDER: second tier.
- SOURCE: `strife-00` §7 (the declared-none row), §8 S2.

### CR-72 — Execution: does `fight` form against a held party? (IN/PC) · BATCH B10-11 (after CP-T03-09 and PC-10) · STATE MEASURE (a test) · R —
- WHAT: `strife-00` §9 defines an execution (XE) as a death caused by a lethal `fight` on a person who holds a live `detain` tenure at that tick, recognised by S1's signature (`victim_held: true`), with no new verb (A7). Its open item (i): whether `fight` forms against a held party at all (its access gate wants co-location, and the seam must say what a restrained party can do in a scene). One hand-built test answers it: a world in which the holder of a custody seat and a person held under that seat's `detain` tenure, written by CP-T03-09's opener (`capture`), are co-located. It asserts (b) and (c) always and records (a): (a) whether `fight` forms for the holder against the held party and is admitted by the fold; (b) a planted lethal `fight` death of the held party is classified XE by `harness/strife.py::classify`; (c) the same planted death of a free person is classified KL. Item (ii) (the sentence as a precondition) stays as `strife-00` leaves it, not proposed.
- If (a) does not form or is refused: the commit names the refusing read (formation or admission) and XE stays a named residue whose owner is the combat seam's restrained-party rule; no gate is widened and no `execute` row is added (A7's revert is Jordan's). No assertion that it does not form is written (it would be a guard on an absence, `CLAUDE.md` §0.1 pt 5); if it forms, the assertion that it forms is kept.
- LANDED ALREADY: S1's XE and KL signatures; `arrest` opens a `detain` to the issuing seat (`verb_table.yaml`, `arrest`); IN-12's `interrogate` (B10-09).
- REMAINING UNBUILT: the test.
- GATE: CP-T03-09 and PC-10 landed (this batch). NEEDS: CP-T03-09, PC-10.
- EXIT and FALSIFIER: the test file passes; MUTATION: flipping `victim_held` in the planted world swaps XE and KL (red). The finding on (a) is quoted in the batch's close commit beside the `interrogate` re-read the card already names.
- HASH MOVERS: none (a test).
- HOLES AND LEDGER IDS: the kill ruling (Jordan, 2026-09-02: "you can't just kill or wound", at `hole_register.yaml`, carried at `verb_table.yaml` beside `fight`), which is why the death must come through the combat seam.
- ASKS ATTACHED: none.
- RE-BASE: `classify`, `readers_for` and the `victim_held` reader by symbol; CP-T03-09's `detain` opener in `state/gate.py` as built.
- FILES: `engine/season/tests/test_strife_execution.py` (new).
- VERB CLUSTER: no.
- LAYER 1: `04` §B.8 (`Tenure`, the `detain` edge) and §C.5 (the contest seam: a death reaches only through it); no hunk.
- N-LINE: the held-party fight test — cut it and the gameplay experience is worse, because whether a captured leader can be put to death, the study's ending in five cases, cannot be known, so a capture (CP-T03-09) leads to no ending of its own and the plan cannot say whether XE is reachable or a residue.
- BUILDER: second tier.
- SOURCE: `strife-00` §8 S2 ("execution has no lane of its own … waits on CP-T03-09's `capture`"), §9.

### CR-73 — Natural shock (SH): a reading of the live weather draw (IN/WR) · BATCH B10-18 (directly after CL-EVENTS commit (2)) · STATE BUILD (harness; hash EQUAL) · R —
- WHAT: SH has no producer (`strife_moves.yaml` SH `gap:`: `season_factor_draw` ships `()`, the calamity bands are unbuilt). CL-EVENTS commit (2) ships the live draw `((0.5, 1.0, 2.0),)*4` per territory, keyed on (world seed, tick, territory rung id) since commit (1). No Event records a drawn factor, so the instrument reads the draw: SH counts one per territory and season whose drawn factor is below 1.0, recomputed after the run from the draw's own key through `queries/world_q.py::season_factor_of`, so nothing is recorded during the run and nothing is stored `[ASSUMPTION; medium; Jordan to correct; revert: SH stays GAP]`. No Event kind is added (CL-EVENTS (2) emits none, and this position may not add an emission). Whether a low draw binds hunger is CR-22's reading, not this one's.
- LANDED ALREADY: CL-EVENTS commit (1) (`df4ffc88`, the key); S1's instrument.
- REMAINING UNBUILT: the SH reading in `strife.py`; the SH row's `gap:` replaced by the reading's description; its test.
- GATE: CL-EVENTS commit (2) landed (this batch). NEEDS: CL-EVENTS. Not a dependency: CP-T10-02 (a calamity band is a second producer only if it lands as an Event; read at the close if it does).
- EXIT and FALSIFIER: at the live arm SH is above 0 at some seed of 0 to 2 (`strife 2 0 1 2`); at the control arm `()` SH reads 0; a planted world with one territory's draw below 1.0 for one season reads exactly one SH. CONTROL: `content_hash` and log length unchanged by the reading.
- HASH MOVERS: none (harness).
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none.
- RE-BASE: `season_factor_of`'s signature and key as commit (2) leaves them; the SH row.
- FILES: `engine/season/harness/strife.py`, `strife_moves.yaml` (the SH row), `strife_data.py` (only if the row needs a new key), `engine/season/tests/test_strife_instrument.py`.
- VERB CLUSTER: no.
- LAYER 1: none (a harness reader calling a `world_q` function).
- N-LINE: the SH reading — cut it and the gameplay experience is worse, because the subsistence category (the study's A: drought, flood, plague) cannot be seen to open in play, so the reachability report cannot say whether a famine strand can begin even once the weather is live.
- BUILDER: second tier.
- SOURCE: `strife-00` §7 (natural shock row), §8 S2.

### CR-74 — Religious sanction (CH): a signature on a restraint opened through a church seat (IN/FA) · BATCH B10-18b (directly after CR-51) · STATE BUILD (harness; hash EQUAL), or the missing carrier named · R —
- WHAT: CH has no kind (`strife_moves.yaml` CH `gap:`); `strife-00` §7: "a church seat issuing ban or detain tenures: data, and the seat". A CH signature reads an Event that opens a `detain` or `ban` (`arrest.made`, or the church-custody branch CR-51 builds if its measure names it) whose causing act's `via` seat belongs to a church, read from a property the seat's institution already carries in code. The re-base looks for that property in this order: IN-30's `faction_props` (B10-17), an `offices.yaml` field naming the institution's kind, a faction's creed. A signature keyed on a named faction is refused (scripting drift, `CLAUDE.md` §0; the `foreign_factions` list is Jordan's ruling R16 and is no precedent for a church list). If no such property exists, the commit names the missing carrier and CH stays GAP; no roster is authored (P11).
- LANDED ALREADY: S1's instrument; the church seats in `offices.yaml` (the Cardinal seats, the Senior Inquisitor, faction "Church of Solmund").
- REMAINING UNBUILT: the signature or the named finding; its test.
- GATE: CR-51 landed (this batch). NEEDS: CR-51, IN-30.
- EXIT and FALSIFIER: at the batch close CH above 0 at some seed (`strife 3 0 1 2`, P10's close horizon) or GAP with the carrier named; planted: a restraint opened through a church seat reads CH, the same restraint through a secular seat does not (it reads CA or PU by the existing rows). CONTROL: `content_hash` unchanged by the reading.
- HASH MOVERS: none (harness).
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none (a church seat's authority to sanction is content, P11).
- RE-BASE: CR-51's outcome (which restraint producer was built); the property search above.
- FILES: `engine/season/harness/strife.py`, `strife_moves.yaml` (the CH row and a signature), `engine/season/tests/test_strife_instrument.py`.
- VERB CLUSTER: no.
- LAYER 1: none.
- N-LINE: the CH signature — cut it and the gameplay experience is worse, because strife begun by the Church's own hand (the study's F and I categories, 15 cases) cannot be told from a secular arrest, so the report cannot say whether a religious strand can open in the realm at all.
- BUILDER: second tier.
- SOURCE: `strife-00` §7 (church sanction row), §8 S2; the church lane's deferral to CR-51 is the fold's placement (ED-IN-0312).

### CR-75 — The strife kind list: a `rosters.yaml` block the loader checks (IN) · BATCH B11-S3 (first) · STATE BUILD (data and loader; hash EQUAL) · R —
- WHAT: `strife-01` §5's block in `engine/season/rosters.yaml`, read through `data/rosters.py::roster_map` (so the loop reads a roster, never the harness's `[UNVERIFIED]` registry: `strife-01` §5, critic F7): `strife_kinds: {opens: [9 kinds], joins: [23 kinds], concludes: […]}`; every other kind is NEVER. Two loader refusals (`04` §B.13): a kind absent from `data/verbs.py::EVENT_KINDS`; a kind in both `opens` and `joins`. A third list, `concludes`, carries the kind-level terminal rule (`strife-01` §3 item 2, critic F1): a kind may conclude a strand only if every code it maps to in `strife_moves.yaml` is terminal; `dispensation.issued` (CO, IM, PC, XS) is checked against it. The rule has one owner: a test re-derives `concludes` from `strife_moves.yaml` and fails on drift (the chain's check, `CLAUDE.md` §0.05 cl. 3), and the same test refuses a kind the registry names in a move row that is in neither `opens` nor `joins` (a deliberate decision per kind, not a default). The loader never reads `strife_moves.yaml`. `concludes` is an addition to `strife-01` §5, needed because the loop may not read the harness's terminal flags `[ASSUMPTION; medium; Jordan to correct; revert: no concludes list; a person's flow concludes only by the open-referent test]`.
- LANDED ALREADY: `roster_map`; `EVENT_KINDS`; `strife_moves.yaml`'s `terminal` and `ends`.
- REMAINING UNBUILT: the block; the two loader refusals; the test.
- GATE: B10-18c merged (the spine). NEEDS: none in the graph (S1 built).
- EXIT and FALSIFIER: the loader refuses a planted kind outside `EVENT_KINDS` and a kind in both lists; the test refuses a registry kind in neither list and a `concludes` that differs from the rule's derivation (MUTATION: add IM's kind to `concludes` by hand, red). CONTROL: the shipped build loads and `content_hash` is unchanged (nothing in the loop reads the block yet).
- HASH MOVERS: none. If landed before the freeze, GO-09 exports the block with the other rosters; after it, a registry change re-exported with an `ED-GO-` row (head §4).
- HOLES AND LEDGER IDS: A3 (`strife-00` §10): `concludes` derives from `ends` counts transcribed `[UNVERIFIED]`; it carries that mark until A3's cross-check, and no step of the loop reads it before then (CR-78's flip is gated on A3).
- ASKS ATTACHED: `strife-01` §6 rulings 1 to 5, the orchestrator's, each reverting alone by moving one kind between lists or striking one content opener.
- RE-BASE: the counts in `strife-01` §2 (seeds 0 and 1, four seasons) re-taken on the base sha; `roster_map`'s signature by symbol.
- FILES: `engine/season/rosters.yaml`, `engine/season/data/rosters.py`, `engine/season/tests/test_strife_kinds.py` (new).
- VERB CLUSTER: no (`rosters.yaml` is not `verb_table.yaml`; any roster-size pin is re-recorded by symbol).
- LAYER 1: `04` §B.13 (the loader refuses a malformed closed set at load) and §C.5.1 (the roster contract, a statement); no hunk.
- N-LINE: the kind list — cut it and the gameplay experience is worse, because the person reading would count every `news.told`, `duty.taken` and `travel.moved` as strife (`duty.taken` 221 and 165, `duty.refused` 388 and 379 per run, `strife-01` §2), so strands would be ordinary life, the realm's one slot would hold noise, and no person could tell a rising from a season.
- BUILDER: second tier for the data; third for the terminal rule.
- SOURCE: `strife-01` §1, §2, §3, §5, §6 (its §6 cites "R7" for awareness not being required; the ruling is R9, `strife-00` §3); `strife-00` §8 S3.

### CR-76 — The world reading: strands, the era, conclusion, `commensurate` and the content openers (IN) · BATCH B11-S3 (after CR-75) · STATE BUILD (World-first queries with no consumer in the loop; hash EQUAL) · R R-04, R-07 (contributors)
- WHAT: in `queries/world_q.py`, World first, owning nothing:
  - `flows_in(w)`: moves are Events whose kind is in `strife_kinds.opens` or `joins`, plus the side-aware openers of `strife-01` §4 (a `march.declared` by side R or O; a death by a lethal `fight` or `accept`). Strands by `strife-00` §4's linking rule (a shared referent; parent or child one rung step apart; the same doer; never through the realm rung; never by who holds a rung) (A9), each read at the lowest rung covering its moves; the era as the realm's one scope (R4, R11); presentation capacity from `rung_kinds`' order, realm 1, duchy 2, then n+1 (A1); the slot ranking (A2). The side read moves here as its one owner (`governors`, `side_against` from `harness/strife.py`, which then imports them: `world_q` may not import the harness, and two copies of the side rule would be the defect `CLAUDE.md` §8 names).
  - `concluded(w, strand)`: a strand concludes on a `concludes` move when no open referent remains (no live `detain` or `ban` among its parties, no `at_war` between its parties, no docketed matter on its referents), reopens if a conflict move follows (rule (b)), never on its own opening move; the era concludes on a terminal move at the realm rung by the same test (A10).
  - `commensurate(w, a, b)` in {−1, 0, +1}: +1 when no pair across the two persons' held affiliations is `incompatible`, −1 when some pair is, 0 when either holds none or every pair is `null` (A4, A12). It reads the `incompatible` pairs from the one place `person_q.confliction` reads them; no second copy.
  - Content openers (`strife-01` §6 rulings 4 and 5): a second `succession.claimed` on one seat; a second `petition.filed` on one matter, read from the minted record's `Record.subject_matter` (an Event cannot say "same matter": 22 of 22 and 25 of 25 `petition.filed` Events carry distinct change subjects, `strife-01` §4). **Named gap: which term in a writ's `subject_matter` marks a burden.** The position reads `record_kinds` and names the key before coding the burden opener; if no key tells a burden from a grant, the opener is not built and rides CR-67 (B10-19: which taxes exist is its design and Jordan's content), a named residue.
  - The shipped-realm reading: a block behind its own flag in `harness/strife.py` (strands per rung, the era's open categories, conclusions, and per strand whether an incompatible pair spans its parties, A5), with the 16 links and the leave-and-rejoin profile against a shuffled-order control, the items `strife-00` §8 S1 moved here. Nothing in the loop reads it.
- No stored flow, state, phase or counter (T-a; ED-IN-0225; a derived reading is inside it, R15).
- LANDED ALREADY: `state/attribution.py::actor_of`; `rung_kinds`; `faction_q.at_war`; `world_q.writs_held` (which already reads `subject_matter`).
- REMAINING UNBUILT: the four functions; the side read's move; the reading block; the tests.
- GATE: CR-75. NEEDS: CR-75.
- EXIT and FALSIFIER: (`strife-00` §8 S3, the world half) two realm-wide events while an era is open read as one era; a terminal claim with the open-referent test met concludes the flow and frees the realm slot, the claim missing leaves it open; a person within the realm flow whose ledger holds none of its moves is listed as within; two petitions sharing a `subject_matter` open a strand and two with different ones do not; `commensurate` reads +1, −1 and 0 on planted pairs (one `null` pair, one person with no affiliation). CONTROL: `content_hash` and log length unchanged; the shipped-realm reading at `strife 3 0 1 2` (P10's close horizon), a reading, never a bar (V2).
- HASH MOVERS: none (no consumer). Base reading: B10-18c's close reading @sha.
- HOLES AND LEDGER IDS: ED-IN-0225 (no arc carrier); `strife-00` A1, A2, A4, A5, A9, A10.
- ASKS ATTACHED: the assumptions above, each with its revert (`strife-00` §10).
- RE-BASE: `questions_for`, `actor_of`, `at_war`, `confliction`'s pair source, `Record.subject_matter` and `record_kinds` by symbol; whether `at_war` is still `False` for every pair (if so, that arm of the open-referent test is vacuous, stated in the commit).
- FILES: `engine/season/queries/world_q.py`, `engine/season/harness/strife.py`, `engine/season/tests/test_strife_flows.py` (new).
- VERB CLUSTER: no.
- LAYER 1: `04` §A.2 (`queries/` enumerates `world_q`, `person_q`, `cache`, `faction_q`; a fifth module, `strife-00` §0's `situation_q.py`, would need an amendment, so none is created; `world_q` owns nothing and takes no token: kept); §B.9 (an `Event` has no actor: the reading reaches the actor only through `causes[]` into the act store, by `actor_of`, the route §B.9 names); §B.10–§B.12 (`world_q.<n>(w : World, ...)`). No hunk.
- N-LINE: the world reading — cut it and the gameplay experience is worse, because simultaneous crises cannot be read as one era nor a war be seen to end, so nobody can check that every opening can reach a conclusion (R1), and persons, offices and factions cannot be shown to stand within the events they live through (R9, R12).
- BUILDER: third tier (the linking rule is judgment, `strife-00` §8 S3).
- SOURCE: `strife-00` §4, §5, §8 S3; `strife-01` §4, §6.

### CR-77 — The person reading: `flows_known` and `concluded_known` (IN) · BATCH B11-S3 (after CR-76) · STATE BUILD (a World-first query over one ledger; no consumer in the loop; hash EQUAL) · R R-07 (contributor)
- WHAT: `flows_known(w, p)` in `queries/world_q.py`: moves are the claims in `p.ledger` whose kind is in `strife_kinds` (kind-level only: a claim carries its kind, subject and, on his own deeds, a `doer`, and no verb, degree or faction: `04` §B.9's `Claim`), linked by CR-76's rule over the claims' subjects and the containment tree. A person's strand opens only on an `opens` kind; a `joins` kind attaches through linking and may conclude it if it is in `concludes`. `concluded_known(w, p, strand)`: open until a `concludes` claim lands in his ledger with the open-referent test met as he holds it, so he may believe a war on after it ended (AX-7). No era object exists in his reading (`strife-00` §4).
- **Named gap: person-side attachment of a joining claim to a world-held strand** (`strife-01` §6 ruling 4). The position confirms by symbol whether the claim a `joins` kind deposits carries a referent that links to a content-opened strand (the seat id of a second claim; the record of a second petition). If it does not, the person learns of those flows only from an opening or terminal kind: a stated limit, never a widened list.
- LANDED ALREADY: the ledger; WITNESS's channels; `person_q.ledger_names`.
- REMAINING UNBUILT: the two functions; their tests.
- GATE: CR-76. NEEDS: CR-75, CR-76.
- EXIT and FALSIFIER: (`strife-00` §8 S3, the person half) a witness and a hearsay holder of the same events read different flows; an empty ledger reads none; a person within the realm flow whose ledger holds none of its moves reads no realm flow (CR-76 lists him as within); a person whose ledger lacks the terminal claim reads the strand open while `concluded` reads it closed. CONTROL: `content_hash` unchanged; the same seed read twice reads identically.
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: none beyond CR-75's and CR-76's.
- RE-BASE: the `Claim` fields and the ledger reader by symbol.
- FILES: `engine/season/queries/world_q.py`, `engine/season/tests/test_strife_flows.py`.
- VERB CLUSTER: no.
- LAYER 1: `04` §A.2 (`world_q`), §B.9 (`Claim`); `01` AX-7 (a character holds a reading of the world, never the world). No hunk.
- N-LINE: the person reading — cut it and the gameplay experience is worse, because a character could not hold a mistaken or partial account of the strife around him (the war he has not heard is over, the rising he knows only by report), so the stamp (CR-78) would have nothing lawful to read and every person would face the world's flows instead of his own.
- BUILDER: third tier.
- SOURCE: `strife-00` §4 (last paragraph), §5, §8 S3; `strife-01` §6 ruling 4.

### CR-78 — The stamp: a held flow's referents among a person's occasions (IN) · BATCH B11-S4 · STATE BUILD (commit (1): switch shipped off, hash EQUAL; commit (2): the flip on, a declared mover, only on its guards) · R R-02 (contributor)
- WHAT: `queries/world_q.py::questions_for` already stamps standing occasions as classed referents onto the person's first question after the sort, so they displace nothing (`_stamped`: vacancies, writs held, places named, larders in purview). One more term: for each flow `flows_known(w, p)` holds open, the rungs, persons and offices at stake, as referents of the existing closed classes (`Office`, `Record`, `Rung`, `Site`, `Proposition`, `Person`, `Detainee`); no `Flow` class. No chooser reads a flow's opening kind or last move; which verb forms on the stamped referent, and whether it is chosen, is the person's own (R10). Commit (1) adds a boolean in `data/fixtures.py` (a plain-word name chosen at build), shipped off. Commit (2) flips it on, `[ASSUMPTION; medium; Jordan to correct; revert: ship off]` (ladder step 5: R2's intent, and CR-17's precedent of shipping once the falsifier passes), only if all three hold: (i) the strife guard passes at three seasons over seeds 0-4 and again over 5-9 (CR-28's two sets), with the off arm reaching at least two distinct terminal codes over the seeds read (else the guard cannot observe concentration, `CLAUDE.md` §0.1 pt 2, and the flip waits on Jordan's call for a four-season reading, P10); (ii) HR-9 controls (2) and (4) (`-08`) hold against the off arm on both seed sets; (iii) A3 is cross-checked, because from this commit a loop step reads the `concludes` set. If any fails, commit (2) is not made (or is reverted, P8); the stamp stays built and off, a named residue.
- LANDED ALREADY: `_stamped` and its four terms; CR-28's term, if its re-take in B10-09 close two holds.
- REMAINING UNBUILT: the term, the switch, the tests; the flip.
- GATE: B11-S3 merged; B10-09 close two closed with CR-28's re-take passing HR-9 controls (4) and (2) on seeds 0-4 and 5-9. If CR-28 is reverted a third time, this position moves to B10-Z HELD with that finding (`-03` §0). NEEDS: CR-77, CR-10, CR-28.
- EXIT and FALSIFIER: planted, a person aware of a rising at his settlement finds that rung and its holder among his occasions with the switch on, and does not with it off (the stamp changes which verbs form for a person in a held flow, `strife-00` §8 S4); the strife guard and HR-9 (2) and (4), on against off, quoted in commit (2)'s body; MUTATION: stamp a referent of a class outside the closed set (refused). CONTROL: switch off reproduces the base hash at seeds 0-2.
- HASH MOVERS: commit (1) EQUAL, `content_hash` at `build_realm(0)` equal to B11-S3's close reading @sha. Commit (2) a declared MOVER: its pre-change `build_realm(0)` reading is commit (1)'s recorded after-reading (P14); seeds 1 and 2 read because it declares a mover (P10); every seeded golden it moves re-recorded, old to new in its body.
- HOLES AND LEDGER IDS: H-156 (the two earlier ledger-sourced stamps falsified on HR-9 (4)); A3.
- ASKS ATTACHED: the flip, taken, revert stated.
- RE-BASE: `questions_for` and `_stamped` by symbol (B10-18b edits the same `added =` expression); CR-28's landed term.
- FILES: `engine/season/queries/world_q.py`, `engine/season/data/fixtures.py`, `engine/season/tests/test_strife_flows.py`; at commit (2), the seeded goldens.
- VERB CLUSTER: no (no `verb_table.yaml`, pin of the verb count or set, or `loop/effects_*.py`); serial by its file and hash edges (head §4).
- LAYER 1: `04` §A.2 (`decision/` reads `Question[]`: the stamp arrives as Questions, so `decision/` reads nothing new and holds no World; `queries/world_q` owns nothing); `01` AX-2 (kept: the stamp is computed in `questions_for`, which already takes World and the person). No hunk.
- N-LINE: the stamp — cut it and the gameplay experience is worse, because a person who knows of a rising at his own settlement chooses exactly as if he did not, so flows condition nothing (R2) and strife becomes a chronicle the characters never act inside.
- BUILDER: third tier.
- SOURCE: `strife-00` §5 (the stamp), §6 (the guard), §8 S4.

### CR-79 — The credit term at WITNESS: one factor in the refraction of a told claim (IN) · BATCH B11-S5 · STATE BUILD (`regime_gain` shipped 0, hash EQUAL), after Lens B · R —
- WHAT: `strife-00` §5 (R14, A12): when WITNESS deposits a told claim, `decision/options.py::refracted_confidence` takes one more factor, `1 + regime_gain × c`, with `c = commensurate(w, hearer, teller)` (CR-76) computed at the WITNESS call site (`loop/witness.py::_refract`'s caller), where World is in scope, and passed in as a number, as `gain` is passed. Told claims only; firsthand claims are not graded by it. **Corrected against `strife-00` §5:** the factor and its clamp apply only when `regime_gain × c` is not 0, so at gain 0 (and wherever `c` is 0) the deposit is today's exactly, rounding included; the clamp's ceiling is the one `refracted_confidence` already respects. The owner's docstring says refraction "only ever LOWERS a confidence"; with `c` = +1 the factor raises, so the docstring is rewritten in the same commit, stating the departure from CAT-3's "graded when read" for this one factor (R14). `regime_gain` is one `data/fixtures.py` value, shipped 0.
- **Lens B first** (`layer-conformance`): (1) whether `04` §A.2's `loop/witness` row ("may read: this tick's log, presence cache, channel predicates, the act store") admits calling a `world_q` function for two persons' held affiliations; (2) whether `01` AX-7's divergence governors ("the channel it arrived on, the reader's competence, and their prior beliefs", ruled as all three together) admit a factor read from the teller's actual affiliations. Both inside: build as written. Either outside: take the variant inside Layer 1 (ladder step 5), `c` from the hearer's own affiliations against what his own ledger holds of the teller's (a prior belief) `[ASSUMPTION; medium; Jordan to correct; revert: the written form, with hunk H-L0-11]`, and write H-L0-11 into this entry: the one sentence Lens B names (the §A.2 cell, or AX-7's governors line), applied only on Jordan's word and only if no (RULED) mark sits at its anchor; it reverts alone.
- LANDED ALREADY: `refracted_confidence` (v9 IN-15) with `refraction_gain` 0.5 shipped; CR-19's `competence_gain` (B10-10).
- REMAINING UNBUILT: Lens B's verdict; the factor; the call-site read; the docstring; the tests.
- GATE: B11-S4 closed (the stamp measured first, `strife-00` §8 S5). NEEDS: CR-76, CR-78, CR-19.
- EXIT and FALSIFIER: (`strife-00` §8 S5, corrected) at fixed claims below the ceiling, a commensurate teller is credited more than an incommensurate one, and an unrelated teller (`c` = 0) exactly as at gain 0; the dissenter case (the hearer's own conviction, not his settlement's, sets the sign; Fable F9); a claim at the ceiling with `c` = +1 is not raised past it; the strife guard with the term on (a test arm at a non-zero gain, never shipped) against off. CONTROL: gain 0 reproduces the base hash at seeds 0-2.
- HASH MOVERS: EQUAL at gain 0; base reading B11-S4's close reading @sha. Any gain above 0 is a magnitude, `[OPEN — Jordan tuning]`, and a declared post-freeze mover.
- HOLES AND LEDGER IDS: H-181 (`rank` dormant, the standing of those who pronounce); H-200 (competence, CR-19).
- ASKS ATTACHED: A11, A12 taken; a gain above 0 is Jordan's value.
- RE-BASE: `refracted_confidence`'s signature and factors after CR-19; `_refract` and its caller by symbol; whether CR-29 (B10-14) moved the told channel.
- FILES: `engine/season/decision/options.py`, `engine/season/loop/witness.py`, `engine/season/data/fixtures.py`, `engine/season/tests/test_strife_credit.py` (new).
- VERB CLUSTER: no.
- LAYER 1: `04` §A.2 (`loop/witness` and `decision/`: `decision/` reads nothing new and `fx` stays flat), §C.6 (WITNESS mints per channel); `01` AX-7. H-L0-11 only on Lens B's finding.
- N-LINE: the credit term — cut it and the gameplay experience is worse, because a hearer credits a co-religionist's report and an enemy creed's alike, so what persons take as true does not depend on who tells them, and dissent and orthodoxy spread at one rate (`strife-00` §5: the regime has no hold on belief).
- BUILDER: third tier.
- SOURCE: `strife-00` §5 (grading what a person credits), §8 S5; the correction (clamp only when the factor is not 0; test below the ceiling; gain shipped 0) recorded with the fold (ED-IN-0312).

### CR-80 — The deck: world-build seeds per strife category (IN/WR) · BATCH B11-S6 (HELD on CL-OPEN's build) · STATE BUILD (rows; shipped off; hash EQUAL) when released · R —
- WHAT: `strife-00` §8 S6: world-build seeds per category (A to I) through the schema of CL-EVENTS commit (3) (goal rows or yield scales, drawn once at build), so that every category can open in a seeded world without anything firing in a season (R1, R2; T-c). Rows only: the schema, and any widening of it, are CL-EVENTS (3)'s and CL-OPEN's (the one owner of the widening, `-10` §3). Each row is read from the study's occasion column (`strife-00` §2) and carries `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`; the switch is the Tensions switch, shipped off.
- LANDED ALREADY: none (CL-EVENTS (3) and (4) are B10-18's).
- REMAINING UNBUILT: the rows; their test.
- GATE: CL-EVENTS commits (3) and (4) landed (B10-18); CL-OPEN's build landed (B10-19, HELD on M26). NEEDS: CL-EVENTS, CL-OPEN.
- EXIT and FALSIFIER: on the test arm (switch on), each category's opening kind appears at some seed in the strife reachability report; the loader refuses a row outside CL-EVENTS (3)'s schema. CONTROL: switch off reproduces the base hash. "It has no on-arm today": the on-arm flip is the Tensions flip already on B10-20's freeze row.
- HASH MOVERS: none (switch off). Released after B10-20 opens, a registry change re-exported through GO-09 with an `ED-GO-` row.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: the rows' content beyond `[ASSUMPTION]` rows is Jordan's (P11).
- RE-BASE: CL-EVENTS (3)'s schema and CL-OPEN's widening as built.
- FILES: `engine/season/tensions.yaml`, `engine/season/tests/test_tensions.py`.
- VERB CLUSTER: no.
- LAYER 1: none beyond CL-EVENTS (3)'s.
- N-LINE: the deck — cut it and the gameplay experience is worse, because categories whose occasion no default world holds (a subject people under a burden, a servile population, an unpaid army) can never open, so R1 holds only for the categories the cast happens to seed.
- BUILDER: second tier for rows.
- SOURCE: `strife-00` §8 S6.
