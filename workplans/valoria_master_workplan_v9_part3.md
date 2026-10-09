# Valoria — Master Workplan v9, part 3: orchestration — dependency graph · batches · file-collision matrix · live ordering edges · file census · run discipline · pre-flight remainder

## Status: part of v9 — see valoria_master_workplan_v9.md
## Reads after `workplans/valoria_master_workplan_v9_part2.md`. Owns THE ORDER: the dependency graph (§A), the batches (§B: membership rules §B.0, batch table §B.1, handoff cards §B.2), the file-collision matrix (§C), the live ordering edges carried from v8 (§O.2), the file census (§O.3), the run discipline (§O.4) and the pre-flight remainder (§P). Each position's entry (WHAT, EXIT, FALSIFIER) lives once, in its home part (`_part4`…`_part7`); this part names handles only.
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol (`CLAUDE.md` §0.1 pt 3).

---

## A. DEPENDENCY GRAPH

Kinds: D = data · F = file-collision (serial) · I = instrument · J = Jordan-gate · R = ordering-by-ruling (v8 O.2 edges, A-25,
main file §0.6). Handles are the state index's (main file §3); a v8 number is an ALIAS. Adjudicated read-only on 2026-10-06 at
HEAD `8b57336`; an edge's evidence is the file its reason names — re-open it before relying on the edge.

**An F edge is a SET, not an order — §B GOVERNS ORDER.** An F row names positions that must never be in flight at once on the
files it lists; it does not say which lands first. The verb-chain row below is the set that edits `verb_table.yaml`,
`rosters.yaml` and the count pins; §B lands it on the serial spine as B-G (IN-08's cells commit, closed `0f998f64`) → B-H (IN-08's chain) →
B-I (IN-09 → IN-10 → IN-11 → IN-33; IN-18's G5) → B-J (SC-03a → IN-40 → IN-48) → B-K (IN-45, `survey` + Rung, IN-49,
IN-28) → B-M (IN-12 step 6 → IN-13) → B-N (SC-01) → B-O (SC-08 → SC-03b → FI-01 → FI-02) → B-P (SC-02: `22b` writes in
`_eff_determine`) → B-Q (IN-12 steps 7, 9, 10, 13 → IN-26 → IN-31's build) → B-R (IN-12 steps 5, 5a, 11 → `give` + Rung →
IN-51) → B-S (IN-32 → PC-06 K-3 → FI-03). B-F (IN-21 → SE-01 → IN-22's live arm → IN-34) edits other files and runs beside
B-I, merging after it (§C.2). No data edge orders IN-12's steps against SC-01 (§A(3)): step 6 lands before it and the
rest after it by batch order alone. SC-01's step 11 (rest) needs `commit`, which is IN-11's (`IN-11 → SC-01 step 11`,
below). Other editors of the same files (§C.1: `rosters.yaml` — IN-03, IN-16/IN-18, IN-28; the pins — most rows) are
serialised against the set by batch boundaries, and inside a batch by §C.2. **This part holds the
only copy of the batch table (§B)**; every other part points here.

| from → to | kind | reason |
|---|---|---|
| B-A (adoption merged; the IN-01 fix, `7b619328`, rides the same branch) → everything | I | `All Gates Green` on `main` is B-A's exit; a red `main` hides every later regression |
| every position that adds, changes or deletes a dataclass field, or moves an outcome → the realm and corpus hashes | I | `content_hash` folds `repr()` of every dataclass (`engine/season/state/world.py:175-176`) across `_STATE_COLLECTIONS` (`:1267`) and the docket (`_STATE_SEQUENCES`, `:1272`), so a new, changed or deleted field moves the hash by SCHEMA alone. Declared, never discovered, each field at ONE commit: by schema — `Person.scar` re-shaped at IN-08's H3 (B-H; `state/carriers.py:602`), `Person.conviction` added at IN-08's H10 (B-H), SC-03a's docket items gaining arrangement and petition (B-J), IN-34's `Person` birth-tick field (B-F), SC-02's `22a`/`22b` field deletions (B-P); by outcome — IN-08's re-celled scores (B-G) and re-scored chooser (6f, B-H; the hidden pin `engine/season/tests/test_build_realm_determinism.py:113-118` asks for `march.declared` or `march.refused` in seed 0 season 1), IN-10's `confer` + term sub-step (B-I; `Tenure.term` already exists, `state/carriers.py:100`, so no schema move), FI-01's skip arm (B-O: the one told-channel candidate the corpus reaches at `Partial` is `ARC-13` seed 0's `finding.none` claim, `loop/witness.py:113-118`), and every verb batch's newly executing rows. IN-40 adds no field (G-4). §B.1 names each batch's movers |
| IN-03 → IN-04 → IN-05 | R (E17) | each SM stage waits on the previous stage's falsifiers OBSERVED (`_part4`, the §SM specs); `30` landed at `5097e49`, its falsifiers observed at B-B's close (`4a2e4494`) |
| IN-03 → SC-01 | R (E17/A-25) | `22` builds the social-contest container's provider on `31a`'s typed input record |
| IN-03 → PC-06 S-2; IN-04 → PC-06 M-1 | D | projection/trace ride the typed input/output records |
| IN-05 → IN-13, MB-03, MB-05r | F | both edit `seam/wrappers/mass_battle.py` / `massbattle.py`, which `31c` splits and moves |
| MB-01/02/04/05/06/07 → IN-05 | F (lane edits FIRST), satisfied | `31c` moves the reachable closure of `mass_battle/sim/`; the MB lane's edits to it are landed at `b31d2c31`; the PC lane edits to the closure `31b` moves (PC-01..04, PC-07) are satisfied, landed at `9054df80` |
| IN-05 → GO-05 | D | the manifest resource lists `modules/**` (SM-13) |
| IN-09 → J-10 close | D (`_part5` §A, J-10 [medium]) | `19b` types `comply`'s cell (`engine/season/verb_table.yaml:139`); nothing reads it earlier |
| {IN-09, IN-10, IN-11, SC-03a, IN-12, SC-01, SC-03b, FI-01; IN-08, IN-13, IN-33, IN-40 (§C.1), IN-45 (its EDITS, `_part5`); IN-26, IN-28, IN-31, IN-32 (their EDITS: `effects_information`, `rosters` + pins, `verb_table`, `verb_table`); SC-02 (`22b`'s write in `_eff_determine`, `loop/effects_information.py:229`); IN-49 and IN-51 [ASSUMPTION: their assumed EDITS, `_part5`]} | F — a set; order is §B's spine | `verb_table.yaml`, `rosters.yaml`, `effects_*.py`, the count pins (`engine/season/tests/`: `test_governance_build.py:817`, `test_season_shape.py:2246, :13032`, the executed / always-refused pins `test_season_shape.py:7547`/`:7633` and again `:9505`/`:9567`, `test_u7_own.py:42`) — never two in flight at once |
| IN-10 → IN-12 steps 5/5a/7, IN-33 | D | `record_sourced_operands` answers `subject` from a held Record (#453 §10.1) |
| IN-11 → SC-01 step 11 (rest) | D | `commit` must execute for C-7's vote-quorum conjunct (`_part6` SC-01, step 11 (rest)); the bench-size conjunct already ships (`bench.size >= quorum`, `bench_quorum` 1: H-161, `engine/season/hole_register.yaml:3589`; `data/requires.py:700`) |
| IN-12 step 6 → IN-13 | D | `seize`'s Rung half lands with the arrival that licenses it, so step 6 (`seize`, the `seizure` basis over a Record) lands first and IN-13 widens it (#453 `:2465`, `:2481`); step 6's prerequisites IN-10 (B-I) and SC-03a (B-J) land first |
| SC-03a → IN-12 step 5 | D | `arrest` writes `detain`; `interrogate` reads the docketed petition |
| IN-10 sub-step (a) (`oblige` formable from a held Record's `terms`, #453 `:524`, type clause 1), IN-11 → IN-40; IN-10 (a) → IN-18 G5 | D | IN-40 is REVISED (G-4) [medium; Jordan to correct]: NO stored `superior:` field. "Under" is (i) rung containment within a faction — Jordan 09-17/18 (RS-9): purview reaches "Descendants only"; who is above is the "rung above of same faction"; "factions can be of any scale" — plus (ii) a seat-holder's own `oblige` to another seat for cross-faction subordination (#453 §7.2's vassalage, `:1389-1391`, `:2076`: "a seat-holder's own `oblige` to another seat … is read by `purview_reaches` as subordination (H-101)"), read by an added oblige-edge clause in `purview_reaches` (`engine/season/state/gate.py:253`). So IN-40 needs `oblige` formable in computed play (IN-10's sub-step (a)) and IN-11, NOT `confer` mutating a pointer. IN-18's G5 also waits on `oblige` executing, so G5 is built in B-I after `oblige` forms (IN-18's BATCH reads "B-E · B-I"). Revert: Jordan prefers a stored parent |
| IN-40's oblige-edge clause vs "purview reaches descendants only" | — (a reading, not an edge) | `purview_reaches` "DOES NOT ASK DIRECTION UPWARD … Upward reach is petition, never purview" (`gate.py:283-284`). The clause keeps that: reach runs from the seat sworn TO, along the swearer's own `oblige`, down to the swearer's seat and its descendants — never from a vassal up. The clause never asks upward, so the two agree |
| SC-03a ↔ IN-40 | F | both edit `state/gate.py`, at different functions: SC-03a widens `tenure_write_basis`'s `determination` clause (`gate.py:744-750`, documented at `:610-619`) and `may_determine` (`:448-501`) and edits the readers #453 step 3 names (`_eff_move`/`_eff_migrate`, `loop/effects_migration.py:22`, `:93`; `sides_of`, `loop/sides.py:37`; `_req_oblige`, `loop/predicates.py:351`; `_eff_confer`, `loop/effects_governance.py:27`) plus the `warrant` basis IN-12 step 6 reads (none exists in `gate.py` today); IN-40 adds the oblige-edge clause to `purview_reaches` (`:253`). The file-level edge stands; IN-40 no longer edits `rosters.yaml`'s `factions` roster, `state/carriers.py` or `offices.yaml` (G-4) |
| IN-10 sub-step (b) (`confer` + `Tenure.term`, #453 `:2071`, `:1382`), IN-11 → IN-48 | D | IN-48 builds H-108's delegation half (acts exercised by someone who does not hold the seat; Jordan 2026-09-03 "Regency and puppet rulers must be possible. / Same with delegation"); regency is a termed seat-hold (`Tenure.term`, `state/carriers.py:100`), whose opening and maturing IN-10's sub-step (b) observes. H-108's row was re-scoped to "delegation without a hold" at B-C (IN-43, landed); IN-48 owns that half |
| SC-01 → SC-08 → SC-03b → SC-02 | D | provider at step 15; `arrangements.py` reader is `22`'s (SC-08, `_part6`); `determine` contested = the provider graded |
| SC-01 → FI-01 | F+D | both edit `effects_information.py`, `seam/ladder.py`; the non-prize routing column designed once |
| FI-01 → FI-02 → FI-03 | D | the second role in `_ROLE_ROSTERS` (`engine/season/manifest/registry.py:26`) is the container FI-03 hosts |
| FI-01's graded half → its deposit half (the last step of FI-01, B-O) | — (was J: H-111) | H-111 ANSWERED [medium; Jordan to correct] (RS-21 item 1): SKIP at WITNESS except keyed kinds a verb declares — a refused inquiry deposits nothing, no `finding.none` deposit, `news.untold` stays (T4). FI-01 is one position. Revert: Jordan states the other option |
| IN-29 (landed `4a2e4494`) → SC-01's fired-slot step | D | `open_case` filling a fired slot → `convene` (`convene`'s dates fire VACANT in every computed world, `loop/effects_information.py:199-201`; `_eff_open_case`'s item at `:220`) and H-163 limit 2's question source (a docketed matter for the persons on its bench) are the second half of #453 pass-1 step 4 (`:553-554`: "CALENDAR events reach WITNESS and `open_case` fills a fired slot → `convene` → `determine`"), whose first half IN-29 landed (`4a2e4494`); SC-01's THE BAR consumes the step; it shares `_eff_open_case` with SC-03a (B-J), which lands first |
| J-8's per-post list → nothing on the graph (ask-then) | — (was J) | J-8 PARTLY ANSWERED [medium] (RS-8: Jordan 09-18, `03eeb811-3355-4264-bc4b-567c9ca0c1ec`, rejecting the delete; "just build out a generic remit", `e07b7146-7c34-4f61-b32b-4c16dbe0a434`): the delete arm is out; `dispatch` stays in the generic remit; per-post naming is deferred by Jordan until posts are authored. IN-12 steps 5, 5a, 11 and step 8's `muster` remit half (IN-13) build on `remit_default`. Revert: Jordan names the posts |
| IN-28 → IN-12 step 11 | R | "after H-166's own order" (#453 §10.4) |
| IN-45's `work` channel → IN-28 | R | `found`/`build` never execute in the shipped worlds for a cause the works channel lifts (H-165; #453 pass-1 step 5, "The J-4 works channel → `found`, `build`, `work`"), while IN-28 prices, holds and ends what they make (H-166). Channel first, then IN-28, both in B-K, so IN-28's EXIT can observe `found`/`build` executing ≥ 1 in computed play; SE-03 rides IN-28 |
| IN-13 → R-07 conjunct 3, `20-v`'s control, J-19 | I | a fought field reaches `_eff_march`'s stance write |
| IN-13 → `give` + Rung; IN-13 → IN-36 | D | `give` + Rung (cession, #453 `:2072`, an IN-12 sub-step in B-R) lands after the arrival so cession is built beside seizure under occupation [ASSUMPTION: #453 `:2072` itself names no data edge — the widening is a cell edit over the gate's existing `handover`]; IN-36's falsifier is a foreign `march` reaching the seam (`_part5` IN-36 DEPS) |
| IN-13 → the occupation-subsistence hole row | — (inside IN-13) | IN-13 creates occupation, so it writes the deferred hole #453 recommends (`:2473`, `:2109`) and carries #453 R-6/R-7 (`:3253-3258`; R-7: a routed army does not arrive); a MATTER-side reader, if the row calls for one, slots by §B.0 R3 (B-T) |
| IN-12 (every step) → IN-51 | R | #453 §10.4's "later" row (`:2472`): R-5 (b) — `inheritance` as a fourth conferral basis read by CENSUS at `person.died`, dispatching to a rule table whose first rule is the designated heir — lands after IN-12; it gives `succeed` its reader (`verb_table.yaml:839` `decline_note`: a carrier nobody reads, ID-13). RS-21 item 9 [medium; Jordan to correct]; revert: Jordan states the other option |
| IN-37 → IN-27 → IN-30 | D | M2's chain; IN-27 builds on RS-21 item 3 (#457 D6: the ending vocabulary is a Query over holds and seats the season reports, never an actor), IN-30 on items 3 and 4 [medium; Jordan to correct]. FA-01's content is NOT a data edge into IN-30 (IN-30's entry says so), so B-U does not wait on B-V |
| IN-36 → FA-01 content (with the Schoenland trade-demand clause) | D | RS-21 item 4 (#457 D4: one foreign faction, two seats, in `references/npc_registry.yaml`) [medium; Jordan to correct]. The churn engine "external trade demands by Schoenland" had no driver, so FA-01's content carries a demand formed from a foreign seat (G-6). ONE copy, in FA-01 (`_part7`); IN-36 points at it. Its carrier is `exchange` (IN-33, B-I, landed before B-V) [ASSUMPTION; medium; Jordan to correct — revert: a `covenant` reader, B-Q] |
| IN-21, SE-01 → IN-34 | F | `loop/matter.py`; IN-34 builds on RS-21 item 5 (#457 D2: ageing and illness IN SCOPE, a hazard reader only, rates swept) [medium; Jordan to correct]. Its birth-tick field moves the hash by schema, so "age step 0 reproduces today" reads as equality of event kinds and counts, or a comparison against a re-recorded hash |
| IN-10 (the second operand channel) → IN-49 | D | `levy`'s cause is H-163 limit 3 ("THE LEVIED RUNG … usually no rung or an empty larder", the H-163 row at `engine/season/hole_register.yaml:3609`); IN-49 adds a question source whose referent is a full larder in purview. #453 pass-1 step 1 (`:545-546`) lists `levy` (limit 3) among the verbs IN-10's second operand channel gates, and IN-49 re-records the always-refused set pin (`engine/season/tests/test_season_shape.py:7633`, which lists `levy`), so §B.0 R1 places it in the verb cluster at B-K, after B-I — R1 outranks R3 for a position that edits a pin. [medium; Jordan to correct; revert: Jordan states the other option.] `levy` is R-04 conjunct (1)'s named verb and an R-05 verb |
| IN-46, IN-47 designs (landed at B-C; reviewed at B-L and B-H) → their builds → R-04 conjunct (3) | D | IN-46 is SM-6's design (the grid mode's suspension at ENCOUNTER's barrier); IN-47 the character-sheet management space (creation, development, chronicling). Neither design has a build batch; R-04, hence M1, cannot read `met` until both builds are batched and every other `scales:` row has its owner (§A(4)) |
| IN-16 → IN-17 → IN-18 | D | absent-row re-check and G-triggers read at T7 |
| IN-16/IN-18 ↔ IN-15 ↔ IN-10 ↔ IN-22 | F | `decision/options.py`, `queries/person_q.py`, `loop/witness.py` (a set: B-E lands before B-I) |
| IN-15, IN-18 → IN-22 reach half (B-E); IN-21 → SE-01 → IN-22 live arm (B-F) | F; D | the reach half (`containing_rung_of`, `decision/options.py:442`) edits B-E's files and closes in B-E; the live arm needs SE-01's bodies (IN-22's one data edge, `_part5`) and lands after the IN-21 → SE-01 steps with its own falsifier |
| IN-08 → IN-18 G1/G2, IN-25 | D | G1's judged regard is built on `align_kind` and the pursuit projection (`engine/season/data/verbs.py:1044-1061`), and G2 and IN-25 tune `score`; IN-08 re-axes the first (13×4 → 15×7) and rewrites the second (6f). So the cells and the chain land FIRST (B-G → B-H → B-E), and IN-18's `deed:` keys are authored on the 15×7 axes. The files IN-08 shares with the telling tail (`person_q`, `choose`, `rosters`, `fixtures`) are honoured in the same direction. [medium; Jordan to correct] — revert: Jordan states the other option, telling first with G1's `deed:` branch forbidden until IN-08 lands and IN-08's EXIT re-running G1, G2 and IN-25 |
| IN-18 G2 → IN-25 | D | the stance term's gain needs G2's polarity in `score` |
| IN-18 G6 ↔ SC-02 `22a` | D | G6 deposits private tellings with `Claim.visibility == (A, B)` (its trigger is met, so it builds in B-E); `22a` deletes `visibility` as inert (`state/carriers.py:283`). `22a` (B-P) re-greps the field's readers and KEEPS it if G6 landed |
| SC-02 `22b` step 24 → IN-12 step 9; IN-45 `forge` → SC-02 `22b` | F; D | `22b` step 24 adds a degree-keyed write in `_eff_determine` (`loop/effects_information.py:229`) whose target is `(Person, pursuits)` — `Person.conviction` is IN-08's H10 affiliations, not this — and step 9's `argue` is that field's other first producer; `write_matrix.yaml`'s `unproduced:` line for `(Person, pursuits)` (`:186-193`) has ONE owner at a time, in landing order: step 24 (B-P) first, step 9 (B-Q) amends it. So B-P lands before B-Q. The `forgery_quality` reader (`19_PLAN.md` step 25) is IN-45 `forge`'s (B-K), struck from `22b` [medium; Jordan to correct] |
| the `11` re-take | R (E15) | O.2 E15 is the one statement of when it runs |
| IN-21 ↔ SE-01 ↔ IN-35 | F | `loop/matter.py` |
| IN-06 → WR-01's reach, IN-32, PC-06 K-3; IN-07 (design) → IN-07's build (= SE-02), SE-04 | D | designs name the carriers. IN-06's design (landed at B-C) is REVIEWED again after IN-08 lands: it names carriers IN-08 creates |
| IN-06 (built) → IN-35 | D | the Calamity's strain needs thread operations as a carrier (#457 `:136`, H-85, `33`); #457 `:200` orders FORCE-HAZARD after the threadwork re-plug and its ruling — after IN-06's BUILD, not its design. The class gate (#457 D1) is ANSWERED [medium] (RS-12, ladder step 3/4: `canon/philosophy/RULINGS.md:126-136` D-3 "Ruled: tensile", with P-07 and Jordan's 2026-10-04 item (6) — a CONSEQUENCE of held configurations failing, not a matter motion; baseline sign: unmanaged, it worsens outward with increasing intensity; revert: Jordan says the ongoing expansion is ambient matter motion) |
| IN-08 → every verb row ADDED after it (IN-12's steps, IN-51, IN-32, PC-06 K-3); IN-08 → IN-09, IN-10, IN-11, IN-33 | D; F | IN-08 re-axes the alignment table 4 → 7; every verb row added after it is celled on the new axes (RS-1(a)), which binds IN-12's steps and the other verb-adding positions. The six-verb extension (`build`, `found`, `give`, `march`, `migrate`, `survey`) lands INSIDE the atomic cells commit: cells on the new axes are refused until the roster swap. NOT a density rule: `_check_sparse_table` (`data/verbs.py:900`; its checks `:917-933`) refuses only an unrostered key and an all-zero table, and sparse is lawful (`:956-957`, an unlisted pair reads `default_cell`), so IN-08's falsifier reads "every table verb has a cell on each axis, or is listed in a declared `uncelled:` set (`tell`, `thread_read`, `restore`) with its reason" (G-1). IN-09, IN-10, IN-11 and IN-33 type EXISTING rows (IN-11 deletes three cells): their edge is F only — B-G closed (`0f998f64`), so the cells are authored once |
| IN-08 chain: `12b`/`12c`/`12d` + H6 + H8 (B-G, closed `0f998f64`) → H7 → H3 = `12` → H9 → H10 → H11 → `12e` → 6f (B-H) | R | atomic cells commit, serial chain (`_part5`); E5 with PC-01 (the same `fight` row) is satisfied, PC-01 landed at `9054df80`. J-1 and J-5 are ANSWERED (RS-1, Jordan 2026-10-06: the two `candidate_*` drafts are folded into the build). IN-08 adds exactly two verb rows, `challenge` and `accept` (R-05 +2); each must execute ≥ 1 in `aperture 4 0` or `corpus_run` at B-H's exit — #453 `:242-244` answered the duel with no new verb (K-23), which IN-08 strikes, so no other position makes them execute and the realm's own chooser is the occasion; a row that records 0 is a named residue in B-H's HANDOFF line and B-I's exit re-reads it |
| IN-08 → IN-12 step 9 | D [UNVERIFIED until B-Q] | step 9 deletes `Person.pursuits`' declaration (#453 `:2468`) while IN-08 re-cells `Person.pursuits`; the two are read against each other at B-Q, after the live field exists |
| GO-01 → GO-05, PC-05(1) | D | the version is ruled (J-9, `ED-GO-0002`, 2026-10-09) and GO-01 records it where code reads it before GO-05 re-exports. GO-04's only gate, Gate-0's first step (IN-42 = GO-02), landed at B-C: GO-04 is not behind GO-05, and rides B-L's tail, reading the seams after the move |
| MB-07, MB-04 → IN-05 | F (lane edits FIRST), satisfied | each was built at its pre-move `systems/` paths in B-D2 and landed at `b31d2c31`. PC-07's edge to IN-04 is satisfied (RS-21 items 7 and 8, landed at `9054df80`). MB-07 built item 6 (J-18 (A)) [medium; Jordan to correct; revert: Jordan states the other option] and shipped it OFF; its flip is MB-07r (`_part7`), a declared mover |

### A(1) Critical path to THE NINE

`measure:` line numbers are `engine/season/requirements.yaml`'s, re-opened 2026-10-06 (each is its row's `measure:` line).

One line per row; the full path, verb by verb and with each row's `blocks:` traced, is `_part2`'s section for that row,
which governs where the two differ.

| row | path (batch) | `measure:` | earliest `met` |
|---|---|---|---|
| R-01 | `11` control (B-G) → IN-50 repairs ARC-23 (B-H; the failing-case print, the diagnosis and P-4 landed at B-C) → IN-10/IN-11 (B-I, `11` re-take) → IN-13 (B-M, `11` re-take); H-116 named first if ≥ 96 % | `corpus_run` R3 rows + control; `wd_collect.py` < 96 % at `2x3` (`requirements.yaml:376, :504`) | B-M (IN-50's repair is slotted to B-H, before it) |
| R-02 | met; `11` re-taken at B-G, B-I, B-M (B-N conditional) per O.2 E15 | `:504` | stays met |
| R-03 | met; `-k test_u2_` green through IN-29 (landed `4a2e4494`) and PC-06 S-1 (B-E) | `:594` | holds |
| R-04 | IN-10 `confer`/`establish`/`revoke` via (B-I) · FA-01 heads act via their seats, IN-40 revised (B-J) · IN-49 `levy`, conjunct (1)'s named verb (B-K) · SC-01 `determine` in the realm (B-N) · `remit_default` (J-8's per-post list ask-then, RS-8 [medium]) · conjunct (3): all SEVEN `scales:` rows `in_loop` — `_part2` R-04 names each row's owner or a named residue; IN-46 and IN-47 own two of them; their designs landed at B-C and neither has a build batch | `aperture 4 0` (`:684`); the seven `scales:` rows (`:70-189`) | not before every `scales:` row has an owner and IN-46's and IN-47's builds are batched (§A(4)) |
| R-05 | `challenge`/`accept` (B-G rows; executing at B-H's exit) · the `comply` and `confer` families, `oblige`, `commit`, `exchange` (B-I) · `forge`, `carry`, `work`, `migrate`, `survey` + Rung, `levy`, `found`/`build` (B-K) · `seize`, `march` (B-M) · `open_case` → `convene`, `speak`, `determine` (B-N) · three inquiries graded — `research`, `examine`, `surveil`'s place case — three waiting (B-O) · `covenant`, `train` et al., `conceal`, `forgive`, `destroy_record` (B-Q) · `arrest`/`pardon`/`interrogate`, `raze`, `give` + Rung, `succeed` (IN-51) (B-R) · `tie / knot`, `thread_read` (B-S); `kill`/`wound` are not verbs (RS-5); pins re-recorded per step | `corpus_run` `WHERE THE <n> GO` (`:830`; the classes at `:813-822`) | CONDITIONAL: after B-S and B-R both merged, only if every row's EXIT observed ≥ 1 execution in computed play (`aperture 4 0` or `corpus_run`), and unless `carry` stops at a fourth gate Subject shape (an amendment to ratified Layer 1, then Jordan's). A row whose EXIT recorded 0 stays a named residue in its batch's HANDOFF line and R-05 stays unmet; no position is invented to fix it. `succeed` sits in the no-predicate/effect class until IN-51 |
| R-06 | IN-08 (B-G: the doctrine-pair cosine measured and recorded; RANKING under G-1's reading) → H7's standing pair test, H3/H9 (B-H) → IN-11 `release` ends an ambition (B-I) → IN-38 (B-V, RS-21 item 2) | RANKING DISCRIMINATION (`:977`) + spread falsifier | B-V |
| R-07 | IN-18 G1, with the two-season `build_realm(0)` realm reader in IN-18's EXIT (B-E) → SE-01 (B-F) → IN-13 a fought field (B-M) | `:1030` + G1's falsifier + `_eff_march`'s stance write reached | B-M |
| R-08 | IN-08 (B-G, G-1's reading: only candidates whose verb has ≥ 1 celled axis count) → H3/H9 (B-H) → W26 → SC-01 (B-N); H-62 → its owners (`_part2` traces both) | `:1075` | B-N |
| R-09 | the `u1_` selector fixed at B-C (IN-43, landed) → SC-01 `speak` graded (B-N) → FI-01's inquiries (B-O) → `train` (B-Q, J-13 (iii): `pool_default` wherever a case names no vocation, RS-21 item 10) → IN-38 (B-V) | `:1173` | partial on the by-person pool until the source of `capability` beyond the interim is ruled (`_part5` §J.2); `_part2` R-09 measures today's reading |

### A(2) M2 and M3

**M2:** the STORY-BAR instrument (IN-19, landed at B-C: `harness/storybar.py`) → SC-01 step 16, THE BAR (B-N) → IN-37 → IN-27 → IN-30 (B-U; IN-27 and IN-30 on RS-21 items 3 and 4
[medium; Jordan to correct]). **M3:** Gate-0's first step and the strategy-document edit landed at B-C (IN-42 = GO-02, GO-03) · GO-01 → GO-05 (which also waits on IN-05)
→ PC-05 (1), all B-Z · GO-04, unblocked, in B-L's tail.

### A(3) Cycles and false dependencies

| finding | verdict |
|---|---|
| anything need J-10 before IN-09? | No. IN-10 reads a held dispensation's `terms` (Record field, exists); IN-12 step 7 `covenant` mints a Record (K-54), not `comply`'s cell; `24h` P7 retired only on IN-09's typed form. `verb_table.yaml:139` read by nothing on the graph before IN-09 [UNVERIFIED beyond grep of `comply` consumers in `decision/`, `loop/`] |
| IN-13 BLK:IN-10 (the first adjudication pass) | **False.** The arrival needs no operand channel; only `muster`'s remit conjunct needed J-8. Real gate: IN-05 (file). `muster`'s remit conjunct builds on `remit_default` (RS-8 [medium]) |
| SC-03 BLK:SC-01 whole (the first adjudication pass) | **Partly false.** Split **SC-03a** (step 2b docket names arrangement/petition; step 3 `detain`/`ban` + readers + widened `determination` basis — needs IN-10/IN-11, `gate.py`) into the verb chain; **SC-03b** (step 4 `determine` contested) after SC-01 |
| missing F: IN-16/IN-18 vs IN-10/IN-15/IN-22 (`options.py`); IN-21 vs SE-01 vs IN-35 (`matter.py`); PC/MB lane edits vs IN-04/05 (the MOVE) | serialised in §B |
| no cycle | the verb chain is a line; `covenant` ← `commit` ← `utter` hold is a chain |
| the verb-chain row read as an order | **Not an order.** It is the F set above; §B's spine orders it. IN-12 step 6 lands before SC-01 (B-M before B-N) and steps 7, 9, 10, 13, 5, 5a, 11 after it (B-Q, B-R) by batch order alone: no data edge ties any step to SC-01 |
| B-P parallel with B-Q | **False.** SC-02's `22b` step 24 writes in `_eff_determine` (`loop/effects_information.py:229`), which B-Q's steps also edit, and both claim `write_matrix.yaml`'s `unproduced:` line for `(Person, pursuits)`; B-P lands before B-Q (the `22b` row above) |
| IN-29 ↔ PC-06 S-1 (F, `loop/driver.py`) | **False — dropped.** S-1 lives in "a harness or client module; no engine change" (#445 `03_play_surface.md:75`); its entry calls `SeasonDriver.season(choose, …)` (`loop/driver.py:347`) and does not edit the driver |
| IN-35 behind IN-06's design | **Too early.** It needs IN-06's BUILD (#457 `:136`, `:200`), so it sits in B-S, after IN-06's build |
| IN-40 → SC-01 (D: "`determine`'s bench is a purview read", v8 E11's reason) | **False — deleted.** `determine`'s bench conjunct is `basis: bench` (`verb_table.yaml:220-229`) → `may_determine` → `sits_over`, which reads `scope_rung` through `ancestry` (`state/gate.py:425-501`) and is explicitly NOT `purview_reaches` (`gate.py:435-442`); E11 is spent (O.2's omitted table). IN-40 → SC-01 orders nothing |
| IN-08 heads the verb batches because "a loader raising on partial landing needs every table verb celled" | **False reason.** The loader accepts a sparse table (`data/verbs.py:956-957`); "partial landing" is the atomic roster swap, not density. The real edge runs to the verb-ADDING positions only (§A, the IN-08 row); IN-08's place before IN-09…IN-33 is a file choice (cells authored once) |
| IN-08 BLK on IN-16/IN-18/IN-25 (F) | **Reversed.** The data edge runs IN-08 → IN-18 G1/G2, IN-25; B-G and B-H land before B-E, and the shared files follow the same order |
| IN-22 BLK:IN-10 | **F, not D.** IN-10 shares `decision/options.py` with IN-22 (a set: B-E lands before B-I); IN-22's one data edge is SE-01, for the live arm; the reach half closes in B-E |
| IN-45 BLK:SC-01 or IN-13 | **False.** Its per-verb gates are IN-10 (`forge`, `work`, `migrate`), SC-03a (`carry`) and IN-22 (`migrate`, F) only (`_part5` IN-45 DEPS); it lands in B-K, ahead of both |
| IN-12 step 9 behind J-13 | **Answered (RS-21 item 10).** J-13 (iii) is adopted as the interim — `pool_default` wherever a case names no vocation — so step 9 builds in B-Q, beside steps 7, 10 and 13 |

### A(4) What is still held, and what stands on the critical path

**Not held, but M1 cannot be met without it:** R-04 conjunct (3) needs all SEVEN `scales:` rows
(`requirements.yaml:70-189`) `in_loop`; today four read `false` (character creation, grand strategy politics, settlement
management, investigations) and three read a partial string (social contests "seam unbuilt", mass battles "seam built",
personal combat "duel only"). `_part2` R-04 tables each row's owner — the position that flips it — or "none, a named
residue". Two of the owners are design positions: SM-6 (the grid mode's suspension at ENCOUNTER's barrier; SM-5 is confirmed
by Jordan's words, RS-6) is IN-46, and the character-sheet management space (creation, development, chronicling) is IN-47;
both designs landed at B-C and neither has a build batch. **R-04, hence M1, cannot read `met` under v9 until every `scales:` row has an
owner and a build batch exists for IN-46 and IN-47;** their review adds one by §B.0 R4/R7. No Jordan ruling is needed for
either design.

**On the critical path, answered** (RS-21, Jordan 2026-10-06: "adopt plan recommendations then"; each the plan's
recommendation, [medium; Jordan to correct]; revert for each: Jordan states the other option):

- **#453 R-5 → IN-51 (B-R).** `succeed` sits in R-05's "no predicate/effect" class (`requirements.yaml:813-822`;
  `verb_table.yaml:839`'s `decline_note`: a carrier nobody reads), so R-5 is ON R-05's path, not "on no row's path".
  Item 9 adopts (b): `inheritance` as a fourth conferral basis read by CENSUS at `person.died`, dispatching to a rule table
  whose first rule is the designated heir, after IN-12. Jordan's 2026-10-04 "(9) royal succession crises" is the churn engine
  it drives. R-05's earliest `met` is after B-S and B-R both merged, on the conditions §A(1) states.
- **H-111 → FI-01's deposit half (B-O)**, built as SKIP at WITNESS except keyed kinds a verb declares (item 1).
- **J-13 → IN-12 step 9 (B-Q)**, (iii) as the interim: `pool_default` wherever a case names no vocation; `train` writes
  `Person.capability` only where a case names one; R-09's by-person pool stays partial until a source is ruled (item 10).
- **`13`-rest → IN-38 (B-V)**: scale the overlays on the NPC lane only, on the per-case observable (item 2).

**Answered, off the critical path** (RS-21, same tag and revert): #457 D6 → IN-27, IN-30 (B-U; item 3); #457 D4 → IN-36,
FA-01's content and the Schoenland trade-demand clause (B-V; item 4, G-6); #457 D2 → IN-34 (B-F; item 5, with its
birth-tick hash note); J-18 (A) → MB-07 (landed, `b31d2c31`, shipped OFF; the flip is MB-07r; item 6); J-20 (B) and J-21 (A) → PC-07 (landed, `9054df80`; items 7 and 8).

**Still held, ON a path to THE NINE:** J-13's remainder — the source of `capability` beyond the interim (iii) — is the item
R-09's by-person conjunct, hence M1, waits on (`_part5` §J.2). And `carry` (IN-45, B-K), on R-05's path, stops and becomes
Jordan's if it needs a fourth gate Subject shape, since that amends ratified Layer 1.

**Still held, off every path to THE NINE** (RS-21's STILL HELD list; ranks and evidence are `_part5` §J's): the tenth attribute's name (D2; M3 only, B-Z; J-9, the Godot version, was ruled 2026-10-09: `ED-GO-0002`), J-14, SM-1 (SC-06, asked at B-N), the
CAST-POPULACE spread construal (SE-04 (c), B-Z), `decision_policy_v1.md`'s fork, `godot_conversion_strategy_v1.md`,
`2026-09-03-governance-corpus-rebuild/`, A-24 (i), H-89, H-56's nested half.

**Ask-then, blocking nothing** (B-Z's ask rows): J-8's per-post list (RS-8 [medium]); J-15, J-16, J-17, J-19; SM-15's timing
(SC-05, asked at B-N); the CELL-VALUE AND COSINE PASS, attached to IN-08 and following B-G (closed `0f998f64`) — Jordan revises cell values (at
least the `doctrine` row) against the cosine instruments (the doctrine pair, `conviction_spread`, the correlation table of
`candidate_pursuit_cells.md` §5.3); RS-3 amended.

**Decided by logic and precedent** (Jordan 2026-10-06: "apply all critic fixes, author fixes for all gaps without my rulings
based on logical and precedent, then re-batch"; each [medium; Jordan to correct], revert: Jordan states the other option):
G-1 `tell` stays uncelled by design, and R-06/R-08 count only candidates whose verb has at least one celled axis.
`requirements.yaml` carries no `met` wording for R-06 or R-08 (their keys are `statement`, `status`, `measured`, `measure`,
`blocks`, `disposition`, `needs_jordan`; the `met` lines are `_part2`'s own), so the record edit IN-08 owes is (i)
`corpus_run`'s RANKING line counting only those candidates, its numerator and denominator printed, and (ii) a `measured:`
note in R-06 and R-08 recording the reading; G-2 H-52 closed "assumption stands" at B-C (IN-43, landed); G-3 `refusal_axis` (H-146) is
not armed; G-4 IN-40 revised (§A, no stored parent); G-5 IN-46 … IN-50; G-6 the Schoenland trade demand rides FA-01's
content; G-7 every other gap the same instruction covers.

**Left the held list** (Jordan 2026-10-06 unless dated): J-1 and J-5 ANSWERED (RS-1: the two `candidate_*` drafts folded
into the build; IN-08 is B-G and B-H); J-8 PARTLY ANSWERED [medium] (RS-8); #457 D1 ANSWERED [medium] (RS-12); SM-5
CONFIRMED by Jordan's words (RS-6); H-101 ANSWERED [medium; Jordan to correct] (RS-19, ladder step 4/5 on Jordan's typed
requirements of 2026-09-02, events `b2133a54-992d-4505-82fc-3b9bb2b703eb`, `d111dc52-31a9-4903-b0a8-d3b3fa897324`,
`5959df57-b1e8-43b9-9478-34a7c26bac17`, `41eb0216-3f37-4004-877f-28dc5379d782`, `8980df9f-2b11-430c-bff8-901eaca46721`, and
2026-09-03, `95b03164-d4a1-4216-92a6-1b52bc74f1e0`, `40966503-d8a0-43b1-be74-3ad5fa55aa33`: a faction can be under a larger
faction and offices nest), read under G-4 against RS-9's words (purview reaches "Descendants only"; who is above is the
"rung above of same faction"; "factions can be of any scale") and #453 §7.2 (vassalage as the seat-holder's own `oblige`):
derived containment plus the oblige-edge clause, no stored `superior:` — IN-40 builds in B-J. Revert: Jordan prefers a stored
parent.

## B. BATCHES

One batch = one session's working context = one PR; batches are FILE CLUSTERS with the membership rules of §B.0; a late
position is slotted by its EDITS (R1–R9). `{…}` = a parallel worktree lane merging after the chain (§C.2). Serial spine:
B-A → B-D (closed: `9054df80`, `b31d2c31`, `0a690b30`) → B-G (closed: `0f998f64`) → B-H → B-E → {B-F ∥ B-I} → B-J → B-K → B-L → B-M → B-N → B-O → B-P → B-Q → B-R → B-S →
B-T; B-U beside B-P and B-Q (opens after B-N, merges before B-R); B-V after B-M in parallel (merges before B-S); B-Z as
ruled. [medium; Jordan to correct — B-P before B-Q and these gates; revert: Jordan states the other option.]

- **Continuity** is the batch's HANDOFF line (§B.2) and git; the session is cleared at the clear point its card names.
- **Boundary:** when a batch closes, its finished positions are deleted from the plan in one net-deleting commit (`CLAUDE.md` §2: the commit is their record) and the run stops for a cleared window before the next batch opens (`methodology-execute`'s BATCH BOUNDARY).
- **Full suite:** once per batch, at its close, and only where the pins make a per-file run blind (`CLAUDE.md` §0.4 pt 1);
  B-A runs none locally (records; CI is the gate). Each position's own EXIT and FALSIFIER are in its entry
  (`_part4`…`_part7`); the exit instrument here is what proves the batch.
- **Hashes:** every batch's exit cell names its movers, with the pre-change `build_realm(0)` reading taken on its base
  commit (§A's hash row); a parallel lane re-runs its hash control on the merged tree (§C.2).
- **The one licensed reordering:** B-L may run right after B-D instead of after B-K if Jordan wants MB-03 or PC-06 M-1/S-2
  sooner; every edge still holds (E17 orders only `30` → `31a` → `22`, and nothing in B-G…B-K reads a module). The spine
  places it later so THE NINE move first.
- **Where the cuts fall:** where the hub set changes (B-G/B-H interior files vs B-I verb files; B-J gate files; B-K refused
  verbs; B-N the provider; B-O graded; B-Q/B-R either side of IN-13's arrival), merged where it is identical (IN-33 in B-I,
  SC-08 in B-O, IN-26/IN-31 in B-Q, IN-51 in B-R, IN-23 in B-U, MB-04/MB-07 in B-D, WR-01..03 in B-D3). B-F is the
  `matter.py`/`fixtures.py`/`census.py` hub with no verb row; B-U and B-V hold the positions RS-21 made buildable whose files
  are driver/harness (B-U) and cast content (B-V).

### B.0 Membership rules

R1 — EDITS name `verb_table.yaml`, a count/set pin, or any `loop/effects_*.py` → cluster V; the batch is the earliest V batch whose entry gate covers the position's D edges (B-I needs only IN-08; B-J needs IN-10/IN-11 or `gate.py`; B-K is a refused-verb lift or a Rung widening with no IN-13 need; B-N needs IN-03/IN-11; B-O needs SC-01's provider; B-Q/B-R need IN-13; B-S needs IN-06).
R2 — EDITS in `decision/options.py`, `loop/witness.py`, `queries/person_q.py`, `decision/choose.py` and no verb row → B-E if gate-free, else the V batch its D edges name.
R3 — EDITS in `loop/matter.py`, `loop/census.py`, `data/fixtures.py` season/body terms, a larder/store reader in `world_q` → B-F (or B-S/B-T if it needs IN-06/IN-07).
R4 — EDITS in `module_contracts.yaml`/`composition.json`/`manifest/`/`seam/wrappers/`/`loop/driver.py` → B-L (a move/split), B-S/B-T (a re-plug), B-U (an ending step).
R5 — EDITS only under `harness/`, a record file, a ledger, `proposals/`, `godot/*.md`, or `cases/` → a lane in the next batch to open, merging last (C.2).
R6 — EDITS only under `systems/<name>/` → that lane's B-D batch (pre-move); a `modules/<name>/` edit that cannot precede the move → B-L's tail.
R7 — EDITS in `state/gate.py` or `state/carriers.py` with `offices.yaml`/`populated.py` → B-J (gate) or B-V (cast).
R8 — a still-held item stays in B-Z until ruled, then slots by R1–R7 into the next unopened batch of its cluster, else runs as its own sub-batch.
R9 — no file overlap, no gate → its own lane in the first batch whose entry gate covers its D edges; merges last.

Where two rules fit, R1 outranks the others: a position that re-records a count or set pin is in the verb cluster whatever
else it edits.

Slotted by these rules: `confer` + term and `oblige` formable → B-I (IN-10's sub-steps, R1); IN-18's G5 → B-I, after
`oblige` forms (R2, its D edge naming B-I); H-44 → B-I beside IN-09; K-36 `interview`-as-prompt and FI-01's per-verb inquiry
shapes → B-O inside FI-01; the fired-slot → `convene` step and H-163 limit 2's question source → B-N inside SC-01; `forge`'s
sheet consumer, the `forgery_quality` reader (`19_PLAN.md` step 25, struck from SC-02's `22b`) and `survey` + Rung → B-K;
`give` + Rung → B-R (after IN-13's arrival); the occupation-subsistence hole row → B-M with IN-13 (its MATTER reader, if
built, → B-T by R3); IN-48 → B-J (R7); IN-49 → B-K (R1 over R3: it re-records the always-refused set pin and needs IN-10's
operand channel); IN-50's repair (diagnosed at B-C) → B-H, whose files hold `loop/resolve.py`'s fold (R1 moves it to B-I if its
hash move re-records a count or set pin); IN-51 → B-R's tail (R1, "after IN-12"); IN-46/IN-47 → their reviews at B-L and B-H,
their builds unscheduled (§A(4)); IN-52 → B-T's tail (R9: no V batch follows its last D edge, IN-07's extractions).

### B.1 The batches

Code sites in this table and in §B.2 were read 2026-10-06 at `8b57336` for the re-batching; those not also cited in §A are
[UNVERIFIED] here — re-derive each by its symbol. Budget: **whole** = `CLAUDE.md` 14k + entries 0.4k each + every edited
file read in full; **working** = the same with `rosters.yaml`/`verb_table.yaml` read by row, pins by site,
`test_season_shape.py` (267k) and `hole_register.yaml` (154k) by site only, proposals via one Haiku extract (≤ 10k, O.4).
⚠ = above ~150k whole; the mitigation is the working-set discipline plus the named clear point.

| id · name | members (build order; `{}` = parallel worktree lane, merges after the chain) | shared files that justify it | intra-batch D/F edges | entry gate | exit instruments · declared re-records | lanes | budget whole/working |
|---|---|---|---|---|---|---|---|
| **B-A ADOPT** | the v9 adoption patch, on the branch that already carries the built CI fix (`7b619328`: `personal_combat` joins `RETIRED_CONTRACTS`; not a position) — its full edit set and each file's covering run are `_part8` §H.3 and §K (FORK rows, ledger rows, the `requirements.yaml`, `rosters.yaml`, handoff, lane_assignments and CURRENT re-points, the proposals' `## Status:` flips; the head regenerated from the entries) | `tests/valoria/test_flow_skeletons.py`; record files only | the adoption merge → everything (I) | Jordan has read `_part8` §K (c) and `_part5` §J | `pytest tests/valoria/test_flow_skeletons.py -q` 0 failed; the covering runs `_part8` §H.3 names (`valoria_local.py --staged`; `test_currency_consistency_check.py`, `test_tool_input_paths_resolve.py`, `test_ledger_hygiene.py`, `test_forked_status.py` after `git fetch --unshallow`); `python tools/pathres.py <each old path>` → FORKED; `grep -c '^## Status:' workplans/valoria_master_workplan_v9*.md` = 1 per file (`test_single_status_line.py` walks only `.designs/systems` and cannot see these files); `register --requirements` exit 0; `validate_ed_citations.py`; then `All Gates Green` on main. No hash, no pin; no full suite locally | none | 60/45 |
| **B-H INTERIOR CHAIN** | H7 (the standing doctrine-pair test — the pair instrument) → H3 (`Person.scar` `{element: count}`, `observers_for` at RESOLVE) → H9 (crisis reader, `Fixtures` arm) → H10 (affiliation roster, `incompatible`, `Person.conviction`, `confliction(p)`) → H11 → `12e` (H13) → 6f (`score` dotting; `beneficiary:`) → IN-50 (ARC-23's repair: the three direct-`Event` refusals routed through `_act_events`, occasion ids appended there; `_part4`); {IN-47 design review against the carriers} | `state/carriers.py`, `loop/resolve.py` (`:117`, the fold, and IN-50's refusal returns `:72-73`, `:746-747`, `:776-779` with `_act_events` `:874`), `queries/person_q.py`, `decision/choose.py`, `data/fixtures.py`, `rosters.yaml` (`affiliation_roster`), `write_matrix.yaml`, `harness/conviction_spread.py`, IN-50's falsifier test | H7 → H3 → H9 → H10 → H11 → 12e → 6f (R, `_part5`); H3 → IN-50 (F: `loop/resolve.py`) | B-G closed (`0f998f64`) | IN-50: `python -m engine.season.harness.corpus_run` ARC `check R3: 97 of 97 pass`, the planted control still flipping False → True, NPC `46 of 46`, no other case flipping; per step (`_part5` IN-08): scar counts differ by `fan_out_mode`; H9 fork divergence at `total`; two incompatible affiliations load, `confliction` non-zero; `aperture` after 6f; **`challenge` and `accept` each execute ≥ 1 in `aperture 4 0` or `corpus_run`** — a row at 0 is a named residue in the HANDOFF line and B-I's exit re-reads it; **hash: movers** `Person.scar` (H3) and `Person.conviction` (H10) by schema, 6f's re-scored chooser by outcome, IN-50's `World.content_hash` wherever an occasioned act is refused (`test_build_realm_determinism.py:113-118` re-checked); pre-change read on each step's base commit | 1 | 125/95 [not re-measured with IN-50] |
| **B-E TELLING / SCORE** | IN-16 → IN-17 → IN-18 (G1/G2 on the 15×7 basis, G1 with `deed:` cells authored here; step 2a; G3, G4, G6–G8 by trigger, G6's trigger met; G5 waits for B-I) → IN-15 → IN-25 → IN-22 reach half; {PC-06 S-1} | `decision/options.py`, `loop/witness.py`, `queries/person_q.py`, `queries/world_q.py`, `decision/choose.py`, `data/fixtures.py`, `rosters.yaml` (claim-kind row), pins (`test_season_shape.py:14741-14757`), `harness/scarce.py` | IN-16 → IN-17 → IN-18 (D); G2 → IN-25 (D); IN-18/IN-15 → IN-22 (F) | B-H merged (`person_q`/`choose`/`fixtures`; the `score` G2 and IN-25 tune is 6f's); **never re-take `11` across this batch (E15)** | `pytest engine/season/tests/test_told_by_channel.py --collect-only -k t7` lists ≥ 1 test (the file holds t1–t6 today, so `-k t7` selects nothing until IN-16 writes it), then `-k t7` green; G1's falsifier and the realm reader IN-18's EXIT carries (a two-season `build_realm(0)` run, ≥ 1 regard pair differing because of a claim, with a control arm); step 2a re-pin; `CLAIMS BY SOURCE` / `DISTINCT EXECUTED SETS` diffed; IN-25 sweep 0/1/3 (0 = today's hash); IN-22: a governor's `questions_for` holds the claim in `scarce.py`'s world; S-1 equal-hash test, `-k test_u2_` green (R-03). **Hash: movers** the telling channel (realm ×1/×3 declared); pre-change read on the base commit | 1 (S-1: no engine file) | ⚠ 165/100 |
| **B-F MATTER I** | IN-21 → SE-01 → IN-22 live arm → IN-34 (RS-21 item 5) | `loop/matter.py`, `data/fixtures.py` (`:399`, `:520`), `queries/world_q.py`, `loop/census.py`, `state/carriers.py` (birth tick), `decision/options.py` (IN-22 live), `test_territorial_subsistence.py` | IN-21 → SE-01 (F); SE-01 → IN-22 live (D); IN-21/SE-01 → IN-34 (F) | B-C closed (`harness/storybar.py`, IN-19's, is the control); B-E merged (`world_q`, `options.py`); **may run parallel with B-I** (merges after it; re-run its hash controls on the merged tree, C.2) | `season_factor` 1.0 = today's hash; drought leaves stores below control, `shortfall:` observed; SE-01 `body_step` arm, control 0 hash EQUAL, `person.demanded` → `person.individuated`; IN-22's live arm with its own falsifier; IN-34: age step 0 as event kinds/counts equality or against a re-recorded hash. **Hash: movers** IN-34's birth-tick field by schema; the drought and `body_step` arms off-control only; pre-change read on the base commit | none | 140/95 as measured with IN-49, now in B-K — clear after SE-01 |
| **B-I VERBS I** | IN-09 (+ H-44's schema rows: keep or close stated) → IN-10 (+ sub-steps `oblige` formable [type clause 1, #453 `:524`] and `confer` + `Tenure.term` [#453 `:2071`, `:1382`]) → IN-11 → IN-33; then IN-18's G5 (after `oblige` forms) | `verb_table.yaml`, `rosters.yaml`, `loop/effects_information.py`, `loop/effects_governance.py`, `decision/options.py`, `data/requires.py`, `data/verbs.py` (`act_key`), pins, `cases/chain/*.yaml` re-grade, `harness/headless.py:153` comment; G5's telling files | IN-09 → IN-10 → IN-11 (F); IN-10 → IN-33 (D); IN-10 → `oblige` → IN-40 (D) and → IN-18 G5 (D) | B-G closed (`0f998f64`; cells once; IN-11's `repudiate` cut deletes three cells); B-E merged (`options.py`) | `aperture 4 0`: `comply`, `evade / defy`, `construe` (how WITNESS-side `construe` counts is `_part2` R-05's), `confer` 70/0 → ≥ 1 with `via`, `establish`, `revoke`, `oblige`, `commit` (leaves `:7633`), `exchange` executes ≥ 1 (not "forms"); a termed seat-hold opens and matures; `test_u7_own.py:42` `DECLINED` shrinks; G5's falsifier per IN-18; `challenge`/`accept` re-read if B-H named either as residue; pins re-recorded; **`11` re-take (E15)**, read against B-G's control; R-04/R-05/R-06 re-measured. **Hash: movers** IN-10 (b)'s termed seat-holds and every newly executing verb, by outcome; pre-change read on the base commit | none | ⚠ 185/120 |
| **B-J GATE + DOCKET + VASSALAGE** | SC-03a → IN-40 (revised, G-4: derived containment + the oblige-edge clause in `purview_reaches`, never asking upward) → IN-48 (H-108's delegation half, design-first; assumed EDITS `state/gate.py` `seat_hold`/`via`, `decision/choose.py:434`, `loop/resolve.py:117`) → IN-31 design; {FA-01 mechanism} | `state/gate.py` (`:253`, `:448-501`), `rosters.yaml`, `loop/effects_information.py` (`_eff_open_case` `:184`, `_eff_determine` `:229`), `queries/world_q.py:329-341`, `data/rosters.py:453`, `arrangements.yaml`, `offices.yaml`, `harness/populated.py`, `test_u7_remit.py`, pins | SC-03a ↔ IN-40 (F: `gate.py`); IN-10/IN-11 → IN-40 (D); IN-10, IN-11 → IN-48 (D); SC-03a → IN-31 (D) | B-I merged; B-F merged (it merges after B-I and shares `queries/world_q.py` and the pins) | `test_u7_remit.py` + three #453 tests; the determination basis still refuses closing a `hold`; the Ehrenwall Split in a seeded season by an `oblige` lapsing or released, purview over a holding not in the superior's holdings refused; IN-48's falsifier per its entry; FA-01: `aperture 4 0` shows a head's act `via` its seat. **Hash: movers** SC-03a's docket items gaining `arrangement`/`petition` by schema; the new `oblige` reads by outcome; pre-change read on the base commit | 1 | ⚠ 190/115 |
| **B-K REFUSED VERBS + WORKS** | IN-45: `forge` (+ the sheet consumer, H-169 limit 5; + the `forgery_quality` reader, `19_PLAN.md` step 25) → `carry` (if it needs a fourth gate Subject shape, that amends ratified Layer 1: stop, register, and it is Jordan's) → `work` → `migrate`; `survey` + Rung; IN-49 (`levy`: a question source whose referent is a full larder in purview; assumed EDITS `decision/options.py`, `queries/world_q.py` stores/`upkeep_of`, pins); then IN-28 (+ SE-03's intent; pricing AFTER the works channel) | `verb_table.yaml`, `rosters.yaml` (`site_kinds`, operands `:1569`), `decision/options.py`, `queries/world_q.py` (IN-49), `state/gate.py:924`, `loop/effects_information.py`, `loop/effects_migration.py`, `loop/effects_founding.py`, `loop/effects_economy.py`, `loop/census.py`, `test_information_cluster.py:146, :204, :297`, `test_migrate_capacity.py`, pins (`:7633` lists `levy`) | per verb: `forge`/`work`/`migrate` ← IN-10 (D); `carry` ← SC-03a (D); `migrate` ↔ IN-22 (F, landed); IN-10 → IN-49 (D); the `work` channel → IN-28 (R) | B-J merged | each verb executes in computed play (`aperture 4 0` row ex > 0) and leaves `DECLINED`/`:7633`; a forgery read differently from a true sheet, and `forgery_quality` has a reader; a `survey` sheet on a Rung subject; `levy` executes ≥ 1 with `via`; a founded place paid for, held, endable, and `found`/`build` executing ≥ 1; MW-5/MW-11 written and run ([UNVERIFIED] red today); pins re-recorded. **Hash: movers** every lifted verb, by outcome; pre-change read on the base commit | none | ⚠ 185/115 before IN-49 [not re-measured] — clear after `carry` |
| **B-L MODULES** | IN-03 → IN-04 → IN-05; then {MB-03, MB-05r} {PC-06 M-1, S-2/L-1} {GO-04 (its one gate, IN-42, landed at B-C; it reads the seams after the move)} {IN-46 design re-read against the combat container} | `seam/wrappers/{sigma,combat,mass_battle}.py`, `seam/ladder.py`, `module_contracts.yaml`, `composition.json`, `manifest/`, `tools/ci_common.py`, `tools/ci_pp_frozen_check.py`, `tools/ci_module_shape_check.py`, `engine/substrate/pc_engine.py`, `tests/valoria/test_engine_does_not_import_systems.py`, `restructure_ledger.md` (MOVE rows), `test_season_shape.py:13113` (a `roll_net` producer-scan comment inside `test_we_only_a_verb_that_declares_contests_can_be_graded_today`, `:12962`, naming the moved file), the moved closures (not read: a Haiku reachability census) | IN-03 → IN-04 → IN-05 (R, E17); IN-05 → MB-03 (F); IN-03 → S-2, IN-04 → M-1 (D) | B-K merged (the spine; E18); B-B closed (`4a2e4494`; IN-02's falsifiers observed, E17); B-D1 closed (`9054df80`) and B-D2 closed (`b31d2c31`; lane edits before the move). Jordan may run it right after B-D instead (§B) | per stage: both hashes unchanged (re-read on the base commit — the declared mover is none); fresh-subprocess composition-row deletion refuses; `aperture 4 0` `tell` equal; `balance.py` runs; one seed twice in one process = one hash; SM-7's test; `export_composition --check`; `freshness_gate` | 4 | 130/100 |
| **B-M ARRIVAL** | IN-12 step 6 (`seize` over a warrant Record) → IN-13 (the arrival; + the occupation-subsistence hole row; carries #453 R-6/R-7) | `verb_table.yaml`, `loop/effects_combat.py` (`_eff_march`), `loop/sides.py`, `seam/wrappers/mass_battle.py` (host half, post-split), `state/gate.py`, `data/fixtures.py:558`, `test_march.py`, `hole_register.yaml` (H-149, H-151, the new row), pins | step 6 → IN-13 (D); IN-05 → IN-13 (F) | B-L merged; B-J merged (step 6 needs IN-10, SC-03a) | `test_march.py` (i)–(vii); `field.unopposed` + `army.arrived`; `seize` flips `holder_faction_of`; **the realm fights ≥ 1 field (R-07 conjunct 3)**; **`11` re-take (E15)**; pins re-recorded. **Hash: movers** `march`/`seize` outcomes (arrival, occupation); pre-change read on the base commit | none | 105/85 |
| **B-N PROCEEDINGS CORE** | SC-01 steps 11 (vote-quorum conjunct, H-161), 12 (`speak`), 14 (ceiling), 13 + 15 (one commit), 16 (THE BAR); + the fired-slot → `convene` step and H-163 limit 2's question source (`effects_information.py:199-220`, `options.py`; the IN-29 (landed `4a2e4494`) → SC-01 edge); attached asks SC-05 (SM-15 timing), SC-06 (SM-1), SC-07, J-16, J-17 | `verb_table.yaml`, `rosters.yaml` (prize rows `:1134`, `:1152`; `chronicle`), `loop/effects_information.py`, `loop/effects_shared.py`, `queries/world_q.py`, `epistemic.py`, `data/requires.py` (`cardinality`), the host input builder (ex-`sigma.py`), `seam/ladder.py`, `modules/social_contest/`, `module_contracts.yaml`, `composition.json`, `manifest/`, `decision/options.py`, pins; reads `systems/social_contest/sim/contest/` (122k: Haiku extract) | step order per `_part6`; 13 and 15 one commit; IN-11 → step 11 (D); IN-03 → step 15 (R) | B-M merged (verb files serial); B-L merged (IN-03); B-I merged (IN-11). **IN-40 → SC-01 is DELETED** (§A(3)) | planted `if arrangement.id == "tribunal"` reddens; M-7 clears Ob ≥ 4; THE BAR (two seeded proceedings twice byte-identical, `causes[]` to the raising date); `DEGREES RESOLVED` gains `a proposition`; `speak` executes; a `date.fired` claim reaches a docket item; `11` re-take only if a reconvergence input moved (E15). **Hash: movers** the provider's graded outcomes; pre-change read on the base commit | none | ⚠ 240/140 — the entry's own sub-batching (11/12/14 · 13+15 · 16), a clear point after each |
| **B-O PROCEEDINGS GRADED** | SC-08 → SC-03b → FI-01 (routing column; deposit half built as SKIP except keyed kinds, RS-21 item 1; per-verb shapes: `research` first, `examine`/`surveil`, `interview` as a prompt K-36, `reconstruct` waits on K-37) → FI-02 | `loop/effects_information.py`, `queries/world_q.py` (SC-08's import), `loop/witness.py:380`, `seam/ladder.py`, `verb_table.yaml`, `write_matrix.yaml:344`, `data/verbs.py:589-604`, `rosters.yaml` (routing column, `verb_capability`), `manifest/registry.py:26`, `module_contracts.yaml`, `composition.json`, `test_u7_remit.py`, pins (`:2188`, `:12962`) | SC-01 → SC-08 → SC-03b (D); SC-03b → FI-01 (F+D); FI-01 → FI-02 (D) | B-N merged | `data.arrangements` loaded in a headless run; `Tenure.degree` set on a contested `determine`; `DEGREES RESOLVED` non-empty for an inquiry — three graded (`research`, `examine`, `surveil`'s place case), three waiting; a refused inquiry deposits nothing (no `finding.none`), `news.untold` still deposits; one-roll-owner test green and sees a planted second resolver fail; `test_season_providers_are_registered` asserts the new role; pins re-recorded. **Hash: movers** FI-01's skip arm (`ARC-13` seed 0 holds a `finding.none` claim today, `loop/witness.py:113-118`) and the graded inquiries; pre-change read on the base commit | none | ⚠ 205/120 — clear after SC-03b |
| **B-P PROCEEDINGS TAIL** | SC-02 (`22a` → `23` → `22b`: `22a` re-greps the readers of `Claim.visibility` and KEEPS the field if IN-18's G6 landed; `22b` step 24's degree-keyed write targets `(Person, pursuits)` and owns `write_matrix.yaml`'s `unproduced:` line for it until B-Q; step 25 is struck — its `forgery_quality` reader is IN-45's, B-K); {SC-04} | `data/` loaders and ids, `data/files.py::effects_modules()`, `queries/faction_q.py:88`, effects modules per `19_PLAN.md` steps (`_eff_determine`, `loop/effects_information.py:229`, for step 24), `write_matrix.yaml:186-193`, `state/carriers.py:283` (`Claim.visibility`); `arrangements.yaml`, `test_arrangements.py`, `test_stress_proceedings_rehost.py` | SC-03b → SC-02 (D); SC-03a → SC-04 (rows); IN-18 G6 ↔ `22a` (D) | B-O merged; **parallel with B-U only** (loaders/ids vs driver/harness); lands BEFORE B-Q (step 24 shares `_eff_determine` and the `(Person, pursuits)` row with B-Q) | one planted violation per loader invariant → `SystemExit` naming its row; `SeatId` as `Act.actor` refused; SC-04's not-ported list shrinks by exactly the re-hosted cases. **Hash: movers** `22a`/`22b`'s field deletions by schema — the corpus hash moves; `23`'s wrappers leave `content_hash` unchanged; pre-change read on the base commit | 1 | 130/95 |
| **B-Q VERBS II** | IN-12 steps 7 (`covenant`), 9 (`train` et al. under J-13 (iii)'s interim, RS-21 item 10: writes `capability` only where a case names a vocation; its deletion of `Person.pursuits`' declaration re-read against IN-08's live field [UNVERIFIED]; it amends `write_matrix.yaml`'s `unproduced:` line after `22b`), 10 (`conceal`), 13 (`forgive`); IN-26 (`destroy_record` executes ≥ 1); IN-31 build | `verb_table.yaml`, `rosters.yaml`, `decision/options.py`, `loop/witness.py` (`anchor_of`, `_ch_witness_key`), `loop/effects_information.py`, `loop/effects_governance.py`, `loop/matter.py` (IN-26), `state/carriers.py` (`Person.capability`), `write_matrix.yaml`, the host input builder's `_pool_of`, `harness/corpus_run.py:875`, pins | IN-10/IN-11 → 7 (D); IN-25 → 13 (D); IN-15/IN-18 ↔ 10 (F); SC-01/FI-01 ↔ IN-26 (F); SC-03a → IN-31 (D); `22b` step 24 → step 9 (F) | B-O merged (FI-01's `effects_information`/`witness`); B-P merged (`_eff_determine`, `write_matrix.yaml`) | per step (`_part5` IN-12 table), each step executing ≥ 1 in `aperture 4 0` or `corpus_run` beside its `w.log` observation: an addressee's `commit` to a covenant; an Event anchors on a `cover` id; `forgive` leaves `stance_toward == 0`; `Person.pursuits` moves under `train`, `_pool_of` varies where a vocation is named; records/season flatten and `destroy_record` executes ≥ 1; `revoke` has > 1 outcome across provenances; a step at 0 is a named residue; pins re-recorded. **Hash: movers** every newly executing verb and `Person.capability`'s writes, by outcome; pre-change read on the base commit | none | ⚠ 175/105 — clear after step 10 |
| **B-R VERBS III + SUCCESSION** | IN-12 steps 5 (`arrest`, `pardon`, `interrogate`), 5a (the charge), 11 (`raze`); `give` + Rung; IN-51 (`inheritance` read by CENSUS at `person.died`, a rule table, `succeed`'s reader; RS-21 item 9; assumed EDITS `rosters.yaml:1737-1755` `conferral_bases`, `loop/census.py`, a `state/gate.py` basis, `verb_table.yaml` `succeed`, `effects_governance.py`, pins) | `verb_table.yaml` (`give`'s cell `:398`; `succeed` `:839`), `rosters.yaml`, `loop/effects_information.py`, `loop/effects_governance.py`, `state/gate.py`, `loop/effects_founding.py` (`raze`), `loop/census.py`, pins | SC-03a, IN-10 → 5/5a (D); IN-28, IN-13 → 11 (D/R); IN-13 → `give` + Rung (D); IN-12 all → IN-51 (R, "after IN-12") | B-P, B-Q and B-U merged; B-K merged (IN-28); B-M merged (IN-13) | `aperture 1 0` `arrest` ex > 0; `move` refused in custody; `detention.ended`, `confession.made`; a hand-built charge and a witness's `commit`; `w.rungs` shrinks on `raze`; a rung `hold` changes hands by `give`; `succeed` executes ≥ 1 at a death; each step executing ≥ 1 in `aperture 4 0` or `corpus_run`, a step at 0 named as residue; pins re-recorded; **R-05's earliest `met` is read here only together with B-S, on §A(1)'s conditions**. **Hash: movers** every newly executing verb, by outcome; pre-change read on the base commit | none | 150/95 |
| **B-U STORY + ENDINGS (M2 tail)** | IN-37 → IN-27 (#457 D6, RS-21 item 3: a Query over holds and seats the season reports; a `driver.py` ending step) → IN-30 (a loop-side caller of `uncontrolled`, `faction_holding`); {IN-23} | `loop/driver.py`, `queries/world_q.py` (`uncontrolled` `:1192`, `faction_holding` `:1129`), `queries/` (new Queries), `harness/` (render, STORY-BAR reader) | SC-01 step 16 → IN-37 (D; IN-19's reader landed at B-C); IN-37 → IN-27 → IN-30 (D) | B-N merged; **beside B-P and B-Q** (driver/`world_q`/harness vs their files; `world_q` is shared with SC-08 — B-O, already merged); merges before B-R and B-T | a render a reader can follow (writes nothing to `World`); an ending reached by choices only (a threshold-fired ending with no person's act among its antecedents fails); `uncontrolled(` has a caller in `loop/` or `decision/` executing in a seeded season; IN-23's Query read by a person's windowed estimate, no stored value. **Hash: movers** IN-27's ending step and IN-30's caller, by outcome; pre-change read on the base commit | 1 | 110/80 |
| **B-V CAST** | {IN-36 (one foreign faction, two seats, #457 D4, RS-21 item 4) → FA-01 content with the Schoenland trade-demand clause — ONE copy, in FA-01 (`_part7`); IN-36 points at it; carrier `exchange` (IN-33, landed in B-I) [ASSUMPTION; medium; Jordan to correct — revert: a `covenant` reader, B-Q]} {IN-38 (NPC-lane overlays on the per-case observable, RS-21 item 2)} | `harness/populated.py`, `rosters.yaml`, `references/npc_registry.yaml`, `offices.yaml`; `cases/exercises/*.yaml` (disjoint) | IN-13 → IN-36 (D); IN-36 → FA-01 content (D) | B-M merged (IN-13); **parallel with B-N…B-R** (merges after them on `rosters.yaml`); merges before B-S | a foreign `march` reaches the seam through the real chooser; off, byte-identical; a demand forms from a foreign seat; IN-38: per-case executed-set change against the no-overlay arm, seed named; R-06/R-09 re-measured. **Hash: movers** the foreign faction's persons and seats (new `World` entries) and IN-38's overlays (per-case corpus hashes); the "off" arm byte-identical; pre-change read on the base commit | 2 | 95/70 |
| **B-S RE-PLUG I (threadwork, knots, ties)** | IN-06 build (design re-reviewed after B-G: it names carriers IN-08 creates) → IN-35 (coupling rule; `+` LOOP row) → IN-32 (`_eff_tie`) → PC-06 K-3 (`thread_read` operand) → FI-03 (design, then build); WR-01's `engine/season/` reach | `module_contracts.yaml`, `composition.json`, `systems/threadwork/sim/*` (store-shed, reach), `systems/fieldwork/sim/knots.py`, `systems/characters/sim/conviction.py`, `modules/` (each re-plugged closure's move, SM-7), `loop/matter.py:36-82`, `loop/effects_information.py`, `verb_table.yaml`, `state/carriers.py`, `rosters.yaml`, `manifest/registry.py` (FI-03's role row), `hole_register.yaml` rows, pins | IN-06 → IN-35, IN-32, K-3, FI-03 (D); IN-21/SE-01 ↔ IN-35 (F); IN-17 → IN-32 (D); FI-02 → FI-03 (D) | B-R merged (verb files); B-V merged (`rosters.yaml`); B-F merged; B-D3 merged (threadwork in-module halves); IN-06's design reviewed after IN-08 | a plugged row's deletion refuses (fresh subprocess); one seed twice = one hash; unmanaged arm: lattice condition falls outward, managed arm stabilises, weight 0 = today; `aperture 1 0` `tie / knot` offered and executed > 0 with a reader; `thread_read` leaves the no-predicate set; FI-03's trail-only response; pins re-recorded; **R-05 `met` first readable here (with B-R), on §A(1)'s conditions**. **Hash: movers** the Calamity coupling's non-zero arm and `tie / knot`, `thread_read` executing, by outcome; weight 0 = today's hash; pre-change read on the base commit | none | 145/95 |
| **B-T RE-PLUG II (settlements module)** | IN-07 build (= SE-02) → SE-04 (a) H-170 arms, (b) H-171 `Rung.envelope`; (c) stays HELD (the spread construal); the occupation-subsistence MATTER reader if IN-13's hole row calls for one; {IN-52 (the levy-to-field feed, shipped OFF behind `field_provisioning`; tail lane after IN-07's extractions)} | `queries/world_q.py`, `loop/matter.py` (extractions to `step_call`/`query`), `modules/settlements/`, `module_contracts.yaml`, `composition.json`, `cohorts.yaml`, `loop/census.py`, `harness/populated.py::seat_cohorts`, `state/carriers.py` (`Rung.envelope`); IN-52: `seam/wrappers/mass_battle.py`, `loop/effects_combat.py`, `verb_table.yaml` (`march`), `modules/mass_battle/` | IN-07 → SE-04 (D); IN-08 → SE-04 (D, landed); IN-07's extractions → IN-52 (D) | B-S merged (`matter.py`, `carriers.py` serial); B-U merged (`queries/world_q.py`); IN-07's design reviewed | per extraction: host body gone (`rg`), both hashes unchanged, composition-row deletion refuses; H-170's two arms executed on `build_realm(0)`; `envelope` has a writer or is deleted; IN-52 with `field_provisioning` off: both hashes equal the base. **Hash: movers** none per extraction, none from IN-52 shipped off; SE-04's arms declared; pre-change read on the base commit | none | 140/90 |
| **B-Z HELD / LEAVE** (not a batch; slots by R8) | GO-01 → GO-05 → PC-05 (1) (J-9 ruled, `ED-GO-0002`; D2, the tenth attribute's name, still held); SC-05 (SM-15 timing), SC-06 (SM-1) — both asked at B-N; SE-04 (c); IN-44 (Layer 0/1, Jordan's files); GO-06 (another repository); MB-08, PC-08, FA-03 (LEAVE); the ask-then rows J-15, J-16, J-17, J-19, J-8 per post, IN-14's repair shape, the CELL-VALUE AND COSINE PASS (B-G closed, `0f998f64`). IN-46's and IN-47's builds are NOT here: they are unscheduled, not held (§A(4)) | — | — | the ruling AND the member's own BLK | per entry; one-value items `/code-review` + `/simplify` | — | — |

**Placement notes** (so that this table, the state index and the entries agree; each rests on the §A row it names):

- **IN-08 binds only the verb-ADDING positions**: IN-12's steps, IN-51, IN-32, PC-06 K-3. It precedes IN-09, IN-10, IN-11
  and IN-33 by file (cells authored once), not by data. PC-01 landed at `9054df80`, before B-G, so E5's "never interleaved"
  holds. `challenge`/`accept` were added in B-G (`0f998f64`) and are read executing at B-H's exit.
- **IN-08 before IN-18's G1/G2 and IN-25** [medium; Jordan to correct]: B-G → B-H → B-E. IN-18's G5 waits for `oblige` and
  is built in B-I.
- **IN-40 → SC-01 is deleted**; IN-40 is revised under G-4 and lands in B-J with SC-03a and IN-48 (one gate session).
- **IN-22 is split**: the reach half closes in B-E; the live arm lands in B-F after IN-21 → SE-01.
- **IN-49 is in B-K, not B-F** [medium; Jordan to correct]: it re-records the always-refused set pin and needs IN-10's
  operand channel, so R1 places it with the refused verbs.
- **B-P lands before B-Q; B-U runs beside them** [medium; Jordan to correct]: SC-02's `22b` step 24 and B-Q's steps share
  `_eff_determine` and the `(Person, pursuits)` row; B-U's driver/harness files are disjoint from both.
- **Hash movers are declared in every batch's exit cell** (§A's hash row), each field at one commit.
- **IN-12 step 9 is in B-Q** under J-13 (iii)'s interim (RS-21 item 10); its deletion of `Person.pursuits`' declaration is
  read there against IN-08's live field.
- **IN-28 is in B-K**, after IN-45's `work` channel (H-165); SE-03 rides it.
- **GO-04 is in B-L's tail**: its one gate (IN-42 = GO-02) landed at B-C; it is not behind GO-05.
- **Attached to B-N, no build of their own:** SC-07 (rides SC-01's batch, `_part6`'s assumption); SC-05 (`2-ii`; the
  measurement at SC-01 only, SM-15's timing) and SC-06 (SM-1) are ASKED at B-N and sit in B-Z.
- **IN-35** builds in B-S after IN-06's build (§A, `IN-06 (built) → IN-35`); **IN-37** opens B-U (M2: after SC-01 step 16).
- **LEAVE and Jordan's files** sit in B-Z: MB-08, PC-08, FA-03 (LEAVE), GO-06 (needs a `valoria-game` checkout), IN-44
  (Layer 0/1, Jordan's: `_part8`).

### B.2 Handoff cards

READ-FIRST = files and entries only (plus `CLAUDE.md`, always). The exit line is the one line left in
`registers/handoffs/HANDOFF_<LANE>.md` (template: `B-<id> <name> MERGED <sha>: <members>; pins re-recorded <sites>; hash
<unchanged|moved old→new, declared>; next B-<id>, READ-FIRST below`). Clear = when the session's context is cleared.

| batch | READ-FIRST | lane file · exit line | clear point |
|---|---|---|---|
| B-A | `_part8` §K; `references/restructure_ledger.md` (tail); the branch carries `7b619328` (the CI fix, built) | IN: `B-A ADOPT MERGED <sha>: v9 is the one plan; main green; next B-B/B-C/B-D` | after `All Gates Green` |
| B-H | `_part5` IN-08 "Then, in order"; `_part4` IN-50 and IN-47; `state/carriers.py:557, :602`; `loop/resolve.py` fold, `:72-73, :746-747, :776-779, :874`; `engine/season/requirements.yaml` R-01's `measured:` (the IN-50 paragraph); `harness/conviction_spread.py:12-13, :193, :209`; `data/fixtures.py:565-566` | IN: `B-H MERGED <sha>: H7..6f; doctrine-pair test standing; scar counts by fan_out_mode; confliction non-zero; challenge <n>, accept <n> executed (or residue named); IN-50 ARC R3 <n> of 97; hash moved <old→new> (Person.scar, Person.conviction, IN-50's refusals); next B-E` | after H10 |
| B-E | `_part4` IN-16, IN-17, IN-18 (+ its §5/§6 tables), IN-15; `_part5` IN-25, IN-22; `person_q.py:260-271`; `options.py:442`; `test_season_shape.py:14741-14757`; `test_told_by_channel.py:1026-1079`; `scarce.py` | IN: `B-E MERGED <sha>: T7; M0 figures <a,b,d>; G1 <landed or control>, G2, G3-G8 <status>; IN-15 formula <name>; IN-25 gain; IN-22 reach; S-1; realm x1/x3 hash <values>; next B-F ∥ B-I` | after IN-18 |
| B-F | `_part5` IN-21, IN-22 (live), IN-34; `_part6` SE-01; `matter.py:255-258, :296-312, :425-432, :489-490`; `fixtures.py:399, :520`; `hole_register.yaml` H-26 `:274`, H-125 `:911` | SE: `B-F MERGED <sha>: season_factor live, body_step arm <v>, IN-22 live, IN-34 (hash re-recorded <old→new>); next B-J` | after SE-01 |
| B-I | `_part5` IN-09, IN-10, IN-11, IN-33; `_part4` IN-18 (G5); #453 `:2309-2357, :2457-2458, :524, :2071, :3207-3219`; `verb_table.yaml:139-160`; `rosters.yaml:1562-1569`; `hole_register.yaml:498` (H-44), `:3583` (H-161); `test_u7_own.py:42`; the pins | IN: `B-I MERGED <sha>: comply/evade-defy/construe, confer+term, oblige, establish, revoke via; commit left :7633; exchange executes; G5 <landed or trigger not met>; H-44 <kept or closed>; 11 re-take <none/actor/total> vs B-G's control; R-04/R-05 <readings>; hash moved <old→new>; next B-J` | after IN-10 |
| B-J | `_part6` SC-03a; `_part5` IN-40 (revised), IN-48, IN-31; `_part7` FA-01; `gate.py:253-288, :425-501, :744-750, :924`; `world_q.py:327-342`; `data/rosters.py:448-453`; `hole_register.yaml:1961-2017` (H-101), H-108 (`:1571`); #453 `:1389-1391, :2076, :2460-2461, :3299-3300`; `offices.yaml:117` | SC: `B-J MERGED <sha>: docket names arrangement+petition; detain/ban; purview oblige-edge clause (Ehrenwall Split expressed); IN-48 design <commit>; FA-01 heads seated; hash moved <old→new>; next B-K` | after IN-40 |
| B-K | `_part5` IN-45 (its table), IN-49, IN-28; `_part6` SE-03; #453 `:545-546, :557, :2074, :3303-3305`; `19_PLAN.md:675-685` (the `forgery_quality` reader); `hole_register.yaml` H-169 `:3687`, H-63 `:728`, H-165 `:3635`, H-168 `:3674`, H-166 `:3648`, H-163 `:3609`; `verb_table.yaml:105, :121, :306, :315, :623, :1161`; `test_information_cluster.py:146, :204, :297` | IN: `B-K MERGED <sha>: forge(+consumer, forgery_quality read) carry work migrate execute; survey on a Rung; levy executes <n>; found/build priced and executing; pins :7633/:42 now <sets>; hash moved <old→new>; next B-L` | after `carry` |
| B-L | `_part4` §4.3 preamble + IN-03, IN-04, IN-05; `_part5` A-25; `_part7` MB-03, MB-05r, PC-06 (M-1, S-2), GO-04; `seam/wrappers/*.py`; `seam/ladder.py:92-116, :124-195`; `manifest/{registry,providers}.py`; `tools/ci_common.py` roots; `test_season_shape.py:13113` (a `roll_net` producer-scan comment inside the test at `:12962`); `test_engine_does_not_import_systems.py:223, :689` | IN: `B-L MERGED <sha>: modules/{social_contest,combat,mass_battle}; hashes unchanged; sim_params decision <kept out or taken>; MB-03, M-1, S-2, GO-04 landed; next B-M` | after each stage (three) |
| B-M | `_part5` IN-12 step 6 row, IN-13; #453 `:2465-2467, :2473, :3253-3258`; `test_march.py:78, :134-140, :196-239, :267-274`; `hole_register.yaml:3122` (H-149), `:3247-3298` (H-151); `loop/sides.py`; `effects_combat.py::_eff_march` | IN: `B-M MERGED <sha>: seize (Record); arrival: realm fights <n> fields; occupation hole H-<n>; 11 re-take <...>; R-07 conjunct 3 <reading>; hash moved <old→new>; next B-N (and B-V may open)` | after IN-13 |
| B-N | `_part6` SC-01 (carried block + v9 re-read), SC-05/06/07; `21_RECONCILIATION.md:565-594`; `04_VERBS.md` `speak`; `requires.py:700, :872-876`; `effects_information.py:184-243`; `epistemic.py` `chronicle`; `rosters.yaml:1028-1036, :1134, :1152`; `hole_register.yaml:3583-3600, :3609-3618`; a Haiku extract of `contest/wrapper.py:110, :200-255` | SC: `B-N MERGED <sha>: steps 11,12,14,13+15,16; provider <interim or kernel>; THE BAR green; fired slot → convene; DEGREES RESOLVED <...>; SC-05/SC-06 asked <answers>; hash moved <old→new>; 11 <re-taken or not needed: no input moved>; next B-O` | after step 14; after 13+15 |
| B-O | `_part6` SC-08, SC-03b, FI-01 (+ corrections), FI-02; #453 `:561-564, :2462, :3341-3344`; `write_matrix.yaml:62-69, :340-344`; `witness.py:380`; `data/verbs.py:585-606`; `registry.py:22-26, :208-226`; `test_season_shape.py:2188, :12962` | FI: `B-O MERGED <sha>: arrangements loaded in production; determine contested writes Tenure.degree; three inquiries graded (research, examine, surveil's place case), three waiting; skip at WITNESS; second role <name>; hash moved <old→new>; next B-P (B-U may open beside it)` | after SC-03b |
| B-P | `_part6` SC-02, SC-04; `_part4` IN-18 (G6); `19_PLAN.md:511-716`; `21_RECONCILIATION.md:582-594`; `faction_q.py:88`; `data/files.py:117-121`; `effects_information.py:229` (`_eff_determine`); `write_matrix.yaml:186-193`; `carriers.py:283` (`Claim.visibility`); `test_stress_proceedings_rehost.py:1-30, :111-131`; `test_arrangements.py:93` | SC: `B-P MERGED <sha>: 22a (visibility <kept: G6 landed or deleted>), 23 (invariants <list>), 22b (step 24 → (Person, pursuits); step 25 left to forge); arrangements <n> rows; re-hosted <cases>; hash moved <old→new>; next B-Q` | after `23` |
| B-Q | `_part5` IN-12 rows 7, 9, 10, 13; IN-26, IN-31; #453 `:2468, :2480-2481, :3286-3287`; `witness.py` `anchor_of`/`_ch_witness_key`; `corpus_run.py:875`; `write_matrix.yaml:186-193`; `hole_register.yaml:3518` (H-156), `:845`, `:1925` (H-100); `_part5` §J's RS-21 item 10 | IN: `B-Q MERGED <sha>: covenant, train (capability where a vocation is named), conceal, forgive executing <n each, or residue named>; destroy_record executes; revoke provenances; Person.pursuits declaration <reading>; pins <sets>; hash moved <old→new>; next B-R` | after step 10 |
| B-R | `_part5` IN-12 rows 5, 5a, 11, IN-51; #453 `:2072, :2472, :2511, :3233-3251, :3291`; `rosters.yaml:1737-1772`; `verb_table.yaml:398, :839`; `_part5` §J's RS-21 item 9 | IN: `B-R MERGED <sha>: arrest/pardon/interrogate, charge, raze, give+Rung, inheritance (succeed executes); pins <sets>; R-05 classes <counts>, residues <list>; hash moved <old→new>; next B-S` | after 5a |
| B-U | `_part5` IN-37, IN-27, IN-30, IN-23; #457 `:163-169, :175, :186, :190`; `driver.py` `season()`; `world_q.py:1192` (`uncontrolled`), `:1129` (`faction_holding`); `populated.py:1304`; `hole_register.yaml:3872` (H-176), `:4153` (H-186) | IN: `B-U MERGED <sha>: render; ending Query <name>; uncontrolled caller; legitimacy/stability Queries; M2 <reading>; hash moved <old→new>; next B-R once B-P and B-Q merge` | after IN-27 |
| B-V | `_part5` IN-36, IN-38; `_part7` FA-01 (the one copy of the trade-demand clause); `_part5` §J's RS-21 items 2 and 4, G-6; `offices.yaml:158-526`; `npc_registry.yaml`; `populated.py` cast overlay; `cases/exercises/` index | FA: `B-V MERGED <sha>: foreign faction <name>, two seats; demand clause via <exchange or covenant reader>; IN-38 <n> cases, per-case set change <reading>; R-06 <reading>; hash moved <old→new>` | after IN-36 |
| B-S | `_part4` IN-06 (+ `proposals/2026-10-07-unplugged-systems-replug.md`; reconcile the entry gate first, IN-06's finding (1)); `_part5` IN-35, IN-32; `_part7` PC-06 K-3; `_part6` FI-03; #457 `:123-143, :174`; `matter.py:36-82`; `hole_register.yaml:4034` (H-182), H-85, H-47; `knots.py:155-156`; `conviction.py:82` | WR: `B-S MERGED <sha>: threadwork/knots/conviction plugged; Calamity coupling (weight 0 = today); tie executes; thread_read typed; FI-03 <design or built>; R-05 <met or the residues left>; hash moved <old→new>` | after IN-35 |
| B-T | `_part4` IN-07 and IN-52 (+ `proposals/2026-10-07-settlements-computation-modules.md`); `_part6` SE-04; `effects_governance.py:308-347`; `cohorts.yaml`; `hole_register.yaml:3700-3725`; `world_q.py:498, :559-572` | SE: `B-T MERGED <sha>: settlements module extractions <list>; H-170 arms <readings>; envelope <writer or deleted>; hashes unchanged per extraction; SE-04(c) HELD` | after IN-07 |
| B-Z | `_part5` §J (the still-held list, its ranks and the ask-then rows); the member's own entry and its BLK; the batch its ruling slots it into (§B.0 R8) | the member's lane: `B-Z <item> RULED <date>: <the ruling, verbatim>; slotted to B-<id> by R<n>; next <that batch's card>` — or, for an ask-then row, `ASKED <date> at B-<id>: <answer or "no answer">` | per sub-batch: after its slotted batch's exit |

## C. FILE-COLLISION MATRIX

### C.1 By position (× = edits)

Serialisation points: `verb_table.yaml` (IN-08 IN-09 IN-11 IN-12 IN-13 IN-31 IN-32 IN-33 IN-45 SC-01 SC-03b FI-01 PC-06 K-3; IN-51 assumed — IN-10 edits `rosters.yaml`+`requires.py`+`options.py`, not `verb_table`; SC-03a edits `rosters.yaml`, not `verb_table`), `rosters.yaml`, `decision/options.py`, `loop/matter.py`,
`loop/driver.py`, `seam/wrappers/*`, `state/gate.py` (SC-03a, IN-40, IN-12, IN-13, IN-45 `carry`; IN-48, IN-51 assumed), the count and set pins (`test_season_shape.py`, and `test_governance_build.py:817`, which is not a shape pin). Paths are under `engine/season/` unless named; "shape
pins" = `engine/season/tests/test_season_shape.py`'s count and set pins.

| position | edits |
|---|---|
| IN-03 | rosters, seam/wrappers/sigma, module_contracts+composition.json, manifest/, shape pins |
| IN-04 | seam/wrappers/combat, seam/ladder, module_contracts+composition.json, shape pins, systems/combat move |
| IN-05 | seam/wrappers/mass_battle, module_contracts+composition.json, shape pins, systems/mass_battle move |
| IN-08 † | rosters, `references/descriptor_registry.yaml`, person_q, effects_combat, shape pins; verb_table (adds the `challenge` and `accept` rows — none exists, `verb_table.yaml:448` is a comment — so the count pins move 44 → 46, `engine/season/tests/test_governance_build.py:817` among them), `state/carriers.py` (H3 `Person.scar`, H10 `Person.conviction`), `data/verbs.py` (`_load_projection` `:937`, `_load_alignment` `:1002`), `data/fixtures.py` (H9's arm), `write_matrix.yaml` (`12b`), `engine/substrate/descriptors.py`, `data/pursuits.py`, `decision/choose.py` (6f), `loop/resolve.py` (H3), `harness/conviction_spread.py`, `harness/corpus_run.py` (G-1's RANKING line), `requirements.yaml` (G-1's two `measured:` notes); plus the pursuit renames (RS-2 `faith` → `doctrine`, RS-4 `warden` → `stewardship`) where the PURSUIT is meant: `references/npc_registry.yaml` (five `conviction: Warden` rows, `:39, :65, :89, :778, :809`, and six `conviction: Faith` rows, `:112, :375, :492, :591, :616, :639`), `rosters.yaml` (`Faith` at `:2015, :2018, :2078`), `engine/season/npcs.yaml`, `references/names_index.yaml`, `references/definitions/definitions.yaml` |
| IN-09 | verb_table, effects_information, shape pins |
| IN-40 † | `state/gate.py` (`purview_reaches`, `:253`: the oblige-edge clause), a `queries/world_q.py` reader of the swearer's `oblige`, tests — NOT rosters, `state/carriers.py` or offices.yaml (G-4) |
| IN-10 | rosters, options.py, requires.py, shape pins — not verb_table (the entry is right; the extraction that listed it was wrong); its sub-steps (`oblige` formable; `confer` + `Tenure.term`) add `loop/effects_governance.py` (`_eff_confer`) [ASSUMPTION: their EDITS are `_part5`'s] |
| IN-11 | verb_table, rosters, effects_information, effects_governance, shape pins |
| IN-12 | verb_table, rosters, options.py, witness.py, effects_information/governance/combat/founding+economy, gate.py, shape pins |
| IN-13 | verb_table, effects_combat, seam/wrappers/mass_battle, gate.py, shape pins, systems read |
| IN-14 | shape pins (decision/budget) |
| IN-15 | options.py, witness.py, shape pins |
| IN-16 / IN-18 | rosters, options.py, person_q, witness.py, world_q, shape pins |
| IN-21 / SE-01 / IN-35 | matter.py, world_q, shape pins |
| IN-22 | options.py, witness.py |
| IN-25 | decision/choose.py, fixtures.py |
| IN-26 | effects_information, matter.py |
| IN-27 † | driver.py (an ending step; `SeasonDriver.season` has none) |
| IN-28 | rosters (`site_kinds`), effects_founding/economy, census.py, shape pins |
| IN-30 † | a loop-side caller of `uncontrolled`; world_q (`faction_holding`) |
| IN-31 † | verb_table (`revoke`'s `writes`), effects_governance |
| IN-32 † | verb_table, effects_information (`_eff_tie`) |
| IN-34 † | matter.py; `state/carriers.py` (a `Person` birth-tick field: a hash mover by schema) |
| IN-36 † | harness/populated.py, rosters, `references/npc_registry.yaml` |
| IN-38 † | `engine/season/cases/exercises/*.yaml` (and the pins its observable re-reads, O.3) |
| IN-48 / IN-49 / IN-51 | assumed in `_part5`'s entries [UNVERIFIED]: IN-48 gate.py (`seat_hold`/`via`), choose.py, resolve.py; IN-49 options.py, world_q (stores), shape pins; IN-51 rosters (`conferral_bases`, `:1737`), census.py, gate.py (a basis), verb_table (`succeed`), effects_governance, shape pins |
| PC-06 S-1 ‡ | a harness or client module; no engine change (#445 `03_play_surface.md:75`) |
| SC-01 | verb_table, rosters, effects_information (+ the fired-slot → `convene` step in `_eff_open_case`), world_q, seam/wrappers, seam/ladder, requires.py, options.py (H-163 limit 2's question source), module_contracts+composition.json, manifest/, shape pins, systems read |
| SC-03a | rosters, effects_information (`_eff_open_case`), world_q, gate.py (`tenure_write_basis`'s `determination` clause and `may_determine`, `:448-501` — not `purview_reaches`), the readers #453 step 3 names: `loop/effects_migration.py` (`_eff_move`, `_eff_migrate`), `loop/sides.py` (`sides_of`), `loop/predicates.py` (`_req_oblige`), `loop/effects_governance.py` (`_eff_confer`), shape pins |
| SC-02 † | `data/` loaders and ids, `data/files.py`, `queries/faction_q.py`, effects modules per `19_PLAN.md` (`_eff_determine` for `22b` step 24), `write_matrix.yaml` (the `(Person, pursuits)` `unproduced:` line), `state/carriers.py` (`22a`: `Claim.visibility`, kept if IN-18's G6 landed) |
| SC-03b / FI-01 | verb_table, witness.py, effects_information, seam/ladder, shape pins |
| IN-50 † | `loop/resolve.py` (the three direct-`Event` refusal returns and `_act_events`), a falsifier test |
| IN-52 † | seam/wrappers/mass_battle, effects_combat (`_eff_march`), verb_table (`march`), `modules/mass_battle/`, a `field_provisioning` fixture |
| MB-03 †, MB-05r † | data/fixtures.py, seam/wrappers/mass_battle, `systems/mass_battle/sim/massbattle.py` (+ `terrain.py` for MB-05r) |
| FA-01 † | offices.yaml, harness/populated.py, `references/npc_registry.yaml` (content) |
| IN-33 † | verb_table, rosters |
| IN-37 † | harness/ (a reader; nothing else in `engine/season/`) |
| IN-45 | verb_table, rosters, options.py, `state/gate.py` (`carry`'s Subject shape, `:924`), effects_information, `loop/effects_migration.py`, shape pins (its `_part5` EDITS) |

† added from the entry's own EDITS field (`_part4`, `_part5`, `_part7`), read 2026-10-06; IN-08's rename files are the scope
of Jordan's 2026-10-06 renames (RS-2, RS-4; the role-template row `rosters.yaml:2016` and `pursuit_projection`'s `Warden`
row `:2128` — that table starts at `:2051`; five `conviction: Warden` and six `conviction: Faith` rows in `npc_registry.yaml`,
read 2026-10-06; a review greps case-blind, `grep -rniw faith`), never the in-world Warden offices, faction or fixtures.
‡ re-scoped 2026-10-06: PC-06 S-1 per its source. Every other row is the adjudicated matrix.

### C.2 Collisions inside a batch — the merge rule

**A `{…}` lane that edits a file its batch's serial chain also edits builds in its own worktree and MERGES after the chain;
two lanes sharing a file merge one after the other. After each such merge, RE-RUN THAT LANE'S EXIT AND FALSIFIER on the
merged tree — hash controls included, not only the pins.** A hash or pin taken on a tree the other side had not reached is
no control. The same rule binds two BATCHES run in parallel on the spine: the later to merge is the lane. The pairs this binds
hardest: B-F against B-I (`rosters.yaml`, the pins, and B-F's control hashes), B-V against whichever of B-N…B-R is open (`rosters.yaml`). O.2 E18 is the rule (`isolation: worktree` defers an edge
to the merge; it never removes it). Derived from §C.1:

| batch(es) | shared file | serial chain (first to merge) | lane(s) — merge after, then re-run their exit |
|---|---|---|---|
| every | `requirements.yaml`, `hole_register.yaml` | every position's forward sweep | every lane (O.2 E13) |
| B-E → B-F | `decision/options.py`, `queries/world_q.py` | IN-16/IN-18, IN-22's reach half (B-E) | IN-22's live arm (B-F) — serial by B-F's entry gate |
| B-F ∥ B-I | `rosters.yaml`, the pins, `decision/options.py` (IN-22's live arm vs IN-10) | B-I's chain | all of B-F: it merges after B-I and re-runs its control hashes (IN-21 at 1.0, SE-01 at 0, IN-34's re-recorded hash) on the merged tree; B-J waits for that merge (`queries/world_q.py`, the pins) |
| B-P → B-Q | `loop/effects_information.py` (`_eff_determine`), `write_matrix.yaml:186-193` | SC-02's `22b` (B-P) | B-Q's steps — serial by B-Q's entry gate; step 9 amends the `(Person, pursuits)` `unproduced:` line `22b` step 24 set |
| B-P ∥ B-U; B-Q ∥ B-U | none (loaders/ids and verb effects vs driver/`world_q`/harness) | — | B-U merges before B-R; B-T's gate waits on it for `queries/world_q.py` |
| B-J | `offices.yaml`, `harness/populated.py` | SC-03a → IN-40 → IN-48 | FA-01 mechanism; under G-4 IN-40 does not edit `offices.yaml`, so FA-01 shares no file with the chain and merges last by R9 |
| B-L | `seam/wrappers/mass_battle.py` (post-split) | IN-03 → IN-04 → IN-05 | {MB-03, MB-05r}; {PC-06 M-1, S-2/L-1}, {GO-04}, {IN-46's re-read}: distinct files |
| B-N…B-R ∥ B-V | `rosters.yaml` | the open one of B-N, B-O, B-P, B-Q, B-R | B-V (IN-36 → FA-01 content; IN-38): merges after it and re-runs its "off, byte-identical" arm; B-S waits for B-V |
| B-Q | `loop/effects_information.py`, `loop/witness.py` | IN-12 steps 7, 9, 10, 13 → IN-26 → IN-31's build — all in the chain | none |

---

## O. ORCHESTRATION — carried from v8 `_part3` (O.1 is replaced by §B)

### O.2 Hard serial edges (live ones only)

Carried from the retired 2026-09-18 plan (§3.9) and 2026-09-28 plan (§3.5), both at `FORK:0671283`; edges both of whose ends
are finished are spent and omitted (v8 `_part6` §H listed them; not carried — read it at v8's `FORK:` ref). `isolation:
worktree` defers an edge to the merge; it never removes it. v9 also omits an edge whose earlier end has landed, since the
order then holds by construction (main file §0.6: E14 and E16 spent); each omitted edge is in the second table, with its reason.

| # | edge | why | origin |
|---|---|---|---|
| E4 | `22` (SC-01) → `2-ii` (SC-05) | the prize-row repoint | 09-28 §3.5.4 |
| E15 | **THE ONE STATEMENT of the `11` re-take; every other mention points here.** It ran at the close of B-G (the CONTROL, `0f998f64`: IN-08's re-scoring, so B-I's reading can be separated from it), and runs at the close of B-I (IN-10/IN-11 add cross-person edges) and at the close of B-M (IN-13 arrives); at B-N's close only if an SC-01 step moves a reconvergence input; never across B-E (IN-16 … IN-18, IN-15, IN-25). P-4 ran before the first, at B-C (IN-39, landed: `probed` equal across two runs) | B-E moves the claim channel `11` measures; a number taken across it has no control. B-I and B-M add the cross-person edges R-01 counts (§A(1)); without B-G's control, B-I's re-take cannot tell IN-10/IN-11's edges from IN-08's re-scored chooser | the telling carve-out, absorbed (main file §0.6); keyed to v9's batches (§B) |
| E17 | `30` (landed `5097e49`) → `31a` (IN-03) → `22` (SC-01); `31a` → `31b` (IN-04) → `31c` (IN-05) | every path-keyed scan reads `modules/` before anything lands there (`35`, landed); `30`'s registrar and refusals precede the first module entry (`31a`); `22` builds on both (A-25). Each later `SM` stage waits on the previous stage's falsifiers observed | A-25 |
| E18 | `31a`–`31c` (IN-03 … IN-05) ↔ every position editing a file that O.3 or §C.1 lists with an `SM` position | `31a`–`31c` re-key the corpus pins in `test_season_shape.py`; two worktrees editing one collide. Serial, never interleaved. B-L is never in flight with any other editor of `rosters.yaml` or the pins (the spine runs it alone). | A-25 |
| E13 | every position → its own forward sweep's `requirements.yaml` / `hole_register.yaml` edits | the shared record files; never edited from two worktrees at once | main file §0.4 |

**Omitted** (landing evidence: v8 `_part3` O.1 row 2, at v8's `FORK:` ref; `git log` #449–#456):

| # | v8 edge | why omitted |
|---|---|---|
| E5, its `8` half | the cells commit ↔ `8` | `8` landed (v8's Batch B, PR #451) |
| E5, its `9` half | the cells commit (IN-08) ↔ `9` (PC-01) | `9` landed (PC-01, B-D1, `9054df80`), before the cells commit |
| E7 | `8` → `ED-FI-0009` | `8` landed; FI-01's `seam/ladder.py` serialisation is §A's SC-01 → FI-01 (F+D) |
| E8 | `8` → `ED-FI-0009` → `14` → `17` → `13d-iii` | every end but `ED-FI-0009` landed (v8's Batches B, C); FI-01 is in §A's verb-chain set |
| E9 | `14` → `24h` P6 | both ends closed: `14` landed (v8's Batch C); `24h` P6 retired, superseded by IN-11 (#453 R-3) |
| E10 | `11-fix` → `11` → `21`-rest | all three landed; the next `11` re-take is E15's |
| E11 | `13d-iii` → `22` steps 11–12 | `13d-iii` landed (v8's Batch C): `determine`'s bench has its scope-rung test (`sits_over`, not `purview_reaches`; §A(3)) |
| E14 | telling T4 → `14` | both landed (PR #449; v8's Batch C) |
| E16 | telling T6 → the AX-7 wiring | T6 landed (PR #449); IN-15's gate is met (main file §0.6) |

### O.3 File census — open positions × shared files

§C.1 is the per-position matrix and governs where the two differ; this is v8's per-file census, carried for the files and
consequences §C.1 does not state. Edits to the carried rows: a closed editor is removed (main file §3 lists only open
positions); a row left with no open editor is omitted (listed below); each v8 alias carries its v9 handle. `30` has landed (`5097e49`;
`rosters.yaml` `modules:`; `R04_PENDING_SUBSYSTEMS` derived at
`tests/valoria/test_engine_does_not_import_systems.py`), its close at `4a2e4494`.

| file | edited by | consequence |
|---|---|---|
| `engine/season/verb_table.yaml` | `ED-FI-0009` (FI-01), `22` (SC-01: `speak`, `determine`), `19b` (IN-09), cells commit (IN-08) | serial in the IN/SC chains (§A's verb-chain set) |
| `engine/season/rosters.yaml` | `22` (SC-01: prize rows, `chronicle`), cells commit (IN-08) | serial (E18) |
| `engine/season/seam/ladder.py` | `ED-FI-0009` (FI-01), `2-ii` (SC-05: veto `extension=`), `31b` (IN-04: the T-k docstring) | E18; `2-ii` is HELD (SC-05) |
| `engine/season/loop/effects_combat.py` | cells commit (IN-08) | E5 spent (PC-01 landed, `9054df80`); one open editor |
| `engine/season/loop/effects_information.py` | `ED-FI-0009` (FI-01), `22` (SC-01) | serial |
| `engine/season/queries/person_q.py` | cells commit (IN-08); then telling G1 (IN-18) | IN-08 first (B-G, B-H), the telling tail after (B-E): the data edge runs IN-08 → G1 (§A) |
| `engine/season/cases/exercises/*.yaml` | `13`-rest (IN-38) | parallel authoring |
| `engine/season/tests/test_season_shape.py` | `13`-rest (IN-38), `22` (SC-01), `31a`–`31c` (IN-03 … IN-05: corpus pins, wrapper imports, the prize-roster test) | every pin re-taken serially (E18) |
| `references/module_contracts.yaml` and `engine/engine_params/composition.json`, `engine/season/manifest/`, `engine/season/data/files.py`, `engine/season/loop/driver.py`, `tools/ci_common.py`, `tools/export_sim_params.py` | `31a`–`31c` (IN-03 … IN-05) (`2-ii` (SC-05) edits `module_contracts.yaml` too) | serial (E17, E18) |
| `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` | every forward sweep; `11` | E13 |
| `references/restructure_ledger.md` | `2-ii` (SC-05), `31b` (IN-04), `31c` (IN-05) (MOVE rows) | serial; appended rows conflict at the file end |
| `.github/workflows/valoria-ci.yml` | `2-ii` (SC-05: the job folds) | — |
| `tests/valoria/test_engine_does_not_import_systems.py` | `2-ii` (SC-05), `31b` (IN-04) | E4, E17 |

**Omitted rows and paragraph** (every editor closed, or the carve-out the row served is absorbed):

| v8 row | v8 editors | why omitted |
|---|---|---|
| `loop/effects_governance.py` | `14` | landed (v8's Batch C) |
| `decision/options.py` | telling T1, T3a, T4; then `14` | all landed; v9's editors are §C.1's |
| `queries/world_q.py` | telling T4 (`with`) | landed; v9's editors are §C.1's |
| `harness/populated.py`; `offices.yaml` | `13d-iii` | landed (v8's Batch C) |
| `harness/corpus_run.py` | `17` | landed (v8's Batch C); IN-43's print landed at B-C |
| `loop/witness.py`, `state/carriers.py`, `data/verbs.py`, `data/requires.py`, `loop/resolve.py`, `test_told_by_channel.py` | the telling workplan only | the carve-out is absorbed (main file §0.6); v9's editors are §C.1's |
| "Parallel lanes this census permits" | v8's Batch 2 `{WR: 27}`, `{MB/PC: LADDER-MBPC}`; v8's Batch 3 `{SE: 24h P5}`; FI `ED-FI-0009` serial against `14` | all landed or recorded (`_part5` A-23); v9's lanes are §B's `{…}` |

### O.4 The run discipline every batch uses

- **Driver:** `methodology-execute` (`CLAUDE.md` §9): `valoria-author` builds and commits each
  position cheaply; `methodology-close`'s pipeline (agonist/antagonist → `/code-review` → `/simplify`
  → `layer-conformance` → terminal Opus critique, the full pipeline at B-G and proportionate elsewhere) and the pytest
  suite run **once per batch** — the heavy batches (B-G, B-I, B-J, B-N, B-O) take `methodology-close` per sub-batch at the
  clear points §B.2 names, the suite still once. The per-step cadence (main file §0.4) runs inside each step, minus the suite and minus its `/code-review` and `/simplify` phases, which run at batch close (Jordan, 2026-10-06).
- **Share the reading** (`CLAUDE.md` §10): one Haiku `valoria-measure` extract per batch, from the
  batch's reading list, handed to every producer. Fire one producer, await its first token, then fan
  out.
- **Receipt (fixed, every producer):** `POSITION <handle> | COMMIT <sha> | FILES <paths> | RAN
  <commands, exit codes> | FALSIFIER <test::name → pass/fail> | HASH <unchanged | moved old→new,
  declared> | HOLES <H-ids touched> | NOT DONE <named remainders>`.
- **Commit shape:** `[scope] <≤72-char subject naming the handle>`; body cites `PP`/`ED`; scopes per
  `CLAUDE.md` §2. Ids from `references/id_reservations.yaml` `next_free` at allocation time, never
  max+1.
- **Tiers:** `haiku` extraction and measurement; `sonnet` bounded builds, deletions, re-hosts; `opus`
  judgment nodes (verify, critique, any effect body with a design choice). Per step: its entry (`_part4`…`_part7`).
- **Stopping rule:** main file §0.5. Revert and register; never widen.

---

## P. PRE-FLIGHT — remainder

**Read at B-C (IN-39, landed; the readings are in its commit body):**

| # | command | what it decided |
|---|---|---|
| P-4 | `cd proposals/2026-09-04-degree-sweep && python wd_chunk.py none default 0 36 && python wd_chunk.py none default 0 36` (same cell twice) | `11-fix`'s determinism attack: PASSED at B-C — equal, `probed` 5514 in both runs; no determinism defect |
| P-6 | for one `corpus_run` case, list the `questions_for` referents offered to a seated person, and compare with `build_realm(0)` (H-175) | READ at B-C; the reading is H-175's `cite:` in `engine/season/hole_register.yaml` — a measurement for R-04's table, not a build |

P-4 has run before `11` is first re-taken, which is B-G's control (§A(1) R-01; when: O.2 E15). Not carried: the settled pre-flight rows S-1…S-10 (not #445's S-1) and the
consumed P-1…P-3, P-5, P-7, P-8 — v8 `_part3` §P, at v8's `FORK:` ref.
