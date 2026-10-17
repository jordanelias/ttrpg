# Valoria — Master Workplan v9, part 3: orchestration — dependency graph · batches · file-collision matrix · live ordering edges · file census · run discipline · pre-flight remainder

## Status: part of v9 — see valoria_master_workplan_v9.md
## Reads after `workplans/valoria_master_workplan_v9_part2.md`. Owns THE ORDER: the dependency graph (§A), the batches (§B: membership rules §B.0, batch table §B.1, handoff cards §B.2), the file-collision matrix (§C), the live ordering edges carried from v8 (§O.2), the file census (§O.3), the run discipline (§O.4) and the pre-flight remainder (§P). Each position's entry (WHAT, EXIT, FALSIFIER) lives once, in its home part (`_part4`…`_part7`); this part names handles only.
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol (`CLAUDE.md` §0.1 pt 3).

**Read every EXIT and FALSIFIER below under `valoria_master_workplan_v9.md` §0.5 (RULED 2026-10-13):** a verb position's "executes ≥ 1 in `aperture 4 0`" (or "in computed play") and "0 times → not built" are superseded by THE STOPPING RULE's relaxed exit — BUILT on a hand-built-world falsifier, the realm count recorded when a propagation reading runs, not required — and `aperture 4 0` runs only as TEST HORIZON allows.

---

## A. DEPENDENCY GRAPH

Kinds: D = data · F = file-collision (serial) · I = instrument · J = Jordan-gate · R = ordering-by-ruling (v8 O.2 edges, A-25,
main file §0.6). Handles are the state index's (main file §3); a v8 number is an ALIAS. Adjudicated read-only on 2026-10-06 at
HEAD `8b57336`; an edge's evidence is the file its reason names — re-open it before relying on the edge.

**An F edge is a SET, not an order — §B GOVERNS ORDER.** An F row names positions that must never be in flight at once on the
files it lists; it does not say which lands first. The verb-chain row below is the set that edits `verb_table.yaml`,
`rosters.yaml` and the count pins; §B lands it on the serial spine as B-G (IN-08's cells commit, closed `0f998f64`) → B-H (IN-08's chain, closed `c13144b9`) →
B-I (closed: `9d93cfab`) → B-J (closed: `42c5588c`; SC-03a, IN-40, FA-01's mechanism and IN-31's design landed; IN-48 left for B-JR) → B-K (closed: `c8d1db3a`)
→ B-M (closed: `be02666e`; IN-12 step 6 `5ea1bb47`, IN-13 `2e19aee8`) → B-N (closed: `cf69ceed`; SC-01) → B-O (SC-08 `59ca2055`, SC-03b `d855576b`, FI-01 `6d94d9d3` landed; FI-02 STOPPED at its own stop condition, `_part6`) → B-P (SC-02: `22b` writes in
`_eff_determine`) → B-Q (IN-12 steps 7, 9, 10, 13 → IN-26 → IN-31's build) → B-R (IN-12 steps 5, 5a, 11 → `give` + Rung →
IN-61) → B-S (IN-32 → PC-06 K-3 → FI-03), with B-Y (IN-59, PC-10b; placed by RS-28) beside B-S and merging before B-T (§B, §C.2). B-F (closed: `53807be4`) edited other files and ran beside
B-I (§C.2). No data edge ordered IN-12's steps against SC-01 (§A(3)): step 6 landed before it and the
rest land after it by batch order alone. Other editors of the same files (§C.1: the pins — most rows) are
serialised against the set by batch boundaries, and inside a batch by §C.2. **This part holds the
only copy of the batch table (§B)**; every other part points here.

| from → to | kind | reason |
|---|---|---|
| B-A (adoption merged; the IN-01 fix, `7b619328`, rides the same branch) → everything | I | `All Gates Green` on `main` is B-A's exit; a red `main` hides every later regression |
| every position that adds, changes or deletes a dataclass field, or moves an outcome → the realm and corpus hashes | I | `content_hash` folds `repr()` of every dataclass (`engine/season/state/world.py:175-176`) across `_STATE_COLLECTIONS` (`:1267`) and the docket (`_STATE_SEQUENCES`, `:1272`), so a new, changed or deleted field moves the hash by SCHEMA alone. Declared, never discovered, each field at ONE commit: by schema — SC-03a's docket items gaining arrangement and petition (landed `c2f855d2`), IN-34's `Person` birth-tick field (B-F), SC-02's `22a`/`22b` field deletions (B-P); by outcome — FI-01's skip arm (landed `6d94d9d3`), and every verb batch's newly executing rows (the hidden pin `engine/season/tests/test_build_realm_determinism.py:113-118` asks for `march.declared` or `march.refused` in seed 0 season 1). IN-08's movers landed at B-G (`0f998f64`) and B-H (`c13144b9`: H3's scar counts by outcome — the field kept its name; H10's `Person.conviction` by schema; 6f none at the shipped arm); B-I's (IN-53, IN-10's sub-steps, IN-09's `comply`) at `9d93cfab`. IN-40 added no field (G-4; landed `3f320093`). §B.1 names each batch's movers |
| IN-05 (landed `5422ed1e`) → GO-05 | D, satisfied | the manifest resource lists `modules/**` (SM-13) |
| IN-09's `comply` (landed `128299db`) → J-10 close | D, satisfied (`_part5` §A, J-10 [medium]) | `19b` types `comply`'s cell (`engine/season/verb_table.yaml:139`); nothing reads it earlier |
| {IN-09, IN-12; IN-08, IN-33, IN-45 (its EDITS, `_part5`); IN-26, IN-31, IN-32 (their EDITS: `effects_information`, `verb_table`, `verb_table`); SC-02 (`22b`'s write in `_eff_determine`, `loop/effects_information.py:229`); IN-61, IN-59, PC-10b (their EDITS: `verb_table`, `rosters` + pins)} | F — a set; order is §B's spine | `verb_table.yaml`, `rosters.yaml`, `effects_*.py`, the count pins (`engine/season/tests/`: `test_governance_build.py:817`, `test_season_shape.py:2246, :13032`, the executed / always-refused pins `test_season_shape.py:7547`/`:7633` and again `:9505`/`:9567`, `test_u7_own.py:42`) — never two in flight at once |
| IN-10 (landed `fae9e623`) → IN-12 steps 5/5a/7, IN-33 | D | `record_sourced_operands` delivers the addressee and the classed-stamp subjects only; Person (warrant) and Proposition (covenant) terms have no route (H-94; step 6 landed over a warrant Record, `5ea1bb47`) |
| SC-03a (landed `c2f855d2`) → IN-12 step 5 | D, satisfied | `arrest` writes `detain`; `interrogate` reads the docketed petition |
| IN-10 sub-step (b) (`confer` + `Tenure.term`, #453 `:2071`, `:1382`; landed `905b7a21`), IN-11 (landed `2a2ed152`) → IN-48 | D, satisfied | IN-48 builds H-108's delegation half (acts exercised by someone who does not hold the seat; Jordan 2026-09-03 "Regency and puppet rulers must be possible. / Same with delegation"); regency is a termed seat-hold (`Tenure.term`, `state/carriers.py:100`), whose opening and maturing IN-10's sub-step (b) observes. H-108's row was re-scoped to "delegation without a hold" at B-C (IN-43, landed); IN-48 owns that half |
| SC-01 (B-N closed `cf69ceed`) → SC-08 (landed `59ca2055`) → SC-03b (landed `d855576b`) → SC-02 | D, satisfied through SC-03b | provider at step 15 (landed `f982f4c2`); `arrangements.py` has its production readers (`state/gate.py`, `loop/effects_information.py`); `determine` contested = the provider graded |
| SC-01 (B-N closed `cf69ceed`) → FI-01 (landed `6d94d9d3`) | F+D, satisfied | both edit `effects_information.py`, `seam/ladder.py`; the non-prize routing column designed once |
| FI-01 (landed `6d94d9d3`) → FI-02 → FI-03 | D | the second role in `_ROLE_ROSTERS` (`engine/season/manifest/registry.py:26`) is the container FI-03 hosts |
| J-8's per-post list → nothing on the graph (ask-then) | — (was J) | J-8 PARTLY ANSWERED [medium] (RS-8: Jordan 09-18, `03eeb811-3355-4264-bc4b-567c9ca0c1ec`, rejecting the delete; "just build out a generic remit", `e07b7146-7c34-4f61-b32b-4c16dbe0a434`): the delete arm is out; `dispatch` stays in the generic remit; per-post naming is deferred by Jordan until posts are authored. IN-12 steps 5, 5a, 11 build on `remit_default`; step 8's `muster` remit half (IN-13, landed `2e19aee8`) does. Revert: Jordan names the posts |
| IN-28 (landed `32024e27`) → IN-12 step 11 | R, satisfied | "after H-166's own order" (#453 §10.4); `raze` is H-166 limit 3's closer |
| IN-13 (landed `2e19aee8`) → R-07 conjunct 3, `20-v`'s control, J-19 | I | a fought field reaches `_eff_march`'s stance write; the arrival is built and the realm fights 0 fields at B-M's close (`be02666e`), so the dependants read a field only on hand-built worlds (the chooser's referents: H-175, H-149) |
| IN-13 (landed `2e19aee8`) → `give` + Rung; IN-13 → IN-36 | D, satisfied | `give` + Rung (cession, #453 `:2072`, an IN-12 sub-step in B-R) is built beside seizure under occupation (it reads `rung.seized` / `record.seized`) [ASSUMPTION: #453 `:2072` itself names no data edge — the widening is a cell edit over the gate's existing `handover`]; IN-36's falsifier is a foreign `march` reaching the seam (`_part5` IN-36 DEPS) |
| IN-12 (every step) → IN-61 | R | #453 §10.4's "later" row (`:2472`), R-5 (b), lands after IN-12. RS-21 item 9 adopted `inheritance` as a fourth conferral basis; RS-27 (2026-10-14, *"designated heir is not a verb but a status or title. the heir still has to claim their throne"*) re-specifies it: the heir is the holder of the throne's registered heir seat, and `inheritance` is a gate basis admitting that holder's own `succeed` claim on a vacant throne — not a CENSUS fill at `person.died` (IN-51's reading, retired). It gives `succeed` an act (the `verb_table.yaml` `succeed` row's `decline_note`: a carrier nobody reads, ID-13) [ASSUMPTION; medium; Jordan to correct]; revert: Jordan states (a), or another carrier (RS-29 ratified the title; IN-61's carrier reverts) |
| IN-53 (landed `5652e846`), IN-10 (c) (landed `905b7a21`) → IN-61 | D, satisfied | the writ delivery and the vacancy machinery IN-61 builds beside; the heir learns of a vacant throne through `seats_named` (a claim naming it), not through `vacancies`, which does not stamp an `inheritance` throne — and `may_fill` refuses `inheritance`, so neither the Widow Regent nor any seat can `confer` it (`_part5` IN-61 (1), (3), (4)) |
| ED-IN-0292 (2) (pending; about `vacancies`) → IN-61 | J | its answer is re-read at IN-61's design step; IN-61's occasion route (4) does not edit `vacancies` |
| SC-04's `succession` row (B-P) → IN-61 | D | the tribunal route over a VACANT throne; SC-03a's determination basis refuses to close a `hold`, so the row awards, never unseats (`_part6` SC-04) |
| IN-58 (landed stance-only `3bf936ee`), H-209 → IN-12 step 5's EXIT | I; D | the RS-23 conjunct — a petition against a killer from a hearer whose regard moved — reads IN-58's grievance at B-R, and needs a dead victim's death claim to reach the hearer's question set (`hole_register.yaml` H-209: IN-72, landed `2f0c0227`, scores a paired claim that reaches it and does not widen `reach`; `_part5` IN-12 step 5's two blockers) |
| IN-40 → IN-58's sworn-to half, IN-60, IN-59 | D | the sworn-to edge (IN-40's `oblige` reader, B-J) is IN-58's sworn-to half (not built: shipped off at `3bf936ee` until the edge is readable person-side), IN-60's "sworn", and IN-59 (b)'s sworn limb |
| IN-36's guard content (B-V) → IN-60 → IN-59 | D | `guard_weight` reads the guard cohorts B-V authors at the principal's home and the throne/duchy `obligees:` (every `offices.yaml` row reads `obligees: []` today); IN-59's audience half reads `guard_weight` |
| PC-10a → PC-10b | D | the module's stop rule under non-lethal terms lands before the season passes terms and reads `result["surrender"]`; PC-10a is B-Y's chain head |
| W2's arm (the narration proposal's candidate typing) → IN-59 | I | the access gate adds a second refusal class to acts already about a third kind-mismatched; W2's arm is measured first — an instrument edge, not a Jordan item, not a v9 position |
| FA-04 (landed `2f0c0227`) ∥ IN-36 (B-V) | F | `offices.yaml` `off_king` `obligees:`; IN-36 merges after and re-runs its "off, byte-identical" arm on the merged tree (§C.2) |
| FA-04 (landed `2f0c0227`) → IN-60 (B-Y) | I | `guard_weight` counts the sworn Grand Master wherever she stands at the King's rung |
| IN-66, IN-68 (landed `2f0c0227`) → IN-36's Altonia row (B-V) | D | the goal rides the carrier; the loader refuses it until the faction exists |
| IN-67, IN-69 (landed `2f0c0227`) → IN-70 (B-R) → IN-12 step 5's RS-23 conjunct | D | opinion of a faction reaches choice as referents |
| SE-06 → SE-04 (c) | D | the vector half answered (if SE-06 is answered yes); the spread stays held |
| IN-62's `--arms` reading → ED-IN-0296 (WRITTEN at B-X's close, `2f0c0227`, `needs_jordan`) | I | the H-54/H-194 question (and SE-06's) is asked with the measurement (`_part5` §J.2; `requirements.yaml` R-06) |
| IN-37 → IN-27 → IN-30 | D | M2's chain; IN-27 builds on RS-21 item 3 (#457 D6: the ending vocabulary is a Query over holds and seats the season reports, never an actor), IN-30 on items 3 and 4 [medium; Jordan to correct]. FA-01's content is NOT a data edge into IN-30 (IN-30's entry says so), so B-U does not wait on B-V |
| IN-36 → FA-01 content (with the Schoenland trade-demand clause) | D | RS-21 item 4 (#457 D4: one foreign faction, two seats, in `references/npc_registry.yaml`) [medium; Jordan to correct]. The churn engine "external trade demands by Schoenland" had no driver, so FA-01's content carries a demand formed from a foreign seat (G-6). ONE copy, in FA-01 (`_part7`); IN-36 points at it. Its carrier is `exchange` (IN-33: reverted at B-I, `cdc03f67`, restorable under main file §0.5; it lands before B-V) [ASSUMPTION; medium; Jordan to correct — revert: a `covenant` reader, B-Q] |
| IN-46, IN-47 designs (landed at B-C; IN-46 re-read at B-L, `e77794a2`, IN-47 reviewed at B-H, `c13144b9`) → their builds → R-04 conjunct (3) | D | IN-46 is SM-6's design (the grid mode's suspension at ENCOUNTER's barrier); IN-47 the character-sheet management space (creation, development, chronicling). Neither design has a build batch; R-04, hence M1, cannot read `met` until both builds are batched and every other `scales:` row has its owner (§A(4)) |
| IN-18 G6 (landed `66bf51f9`) → SC-02 `22a` | D | G6 landed at B-I and is dormant in play: its break path is not reached (`engine/season/hole_register.yaml` H-204; the swept chance is H-197). `22a` (B-P) re-greps the readers of `Claim.visibility` (`state/carriers.py`) and decides keep or delete then |
| SC-02 `22b` step 24 → IN-12 step 9; IN-45 `forge` (landed `c435a5ec`) → SC-02 `22b` | F; D | `22b` step 24 adds a degree-keyed write in `_eff_determine` (`loop/effects_information.py:229`) whose target is `(Person, pursuits)` — `Person.conviction` is IN-08's H10 affiliations, not this — and step 9's `argue` is that field's other first producer; `write_matrix.yaml`'s `unproduced:` line for `(Person, pursuits)` (`:186-193`) has ONE owner at a time, in landing order: step 24 (B-P) first, step 9 (B-Q) amends it. So B-P lands before B-Q. The `forgery_quality` writer and reader (`19_PLAN.md` step 25, H-210) are SC-02 `22b`'s (B-P), re-added at B-K's close because `forge` landed without the writer [medium; Jordan to correct] |
| the `11` re-take | R (E15) | O.2 E15 is the one statement of when it runs |
| IN-35 after IN-21 (landed `3544d568`), SE-01 (landed `d12c8db9`) and IN-34 (landed `44fdb4df`) | F | `loop/matter.py` |
| IN-06 → WR-01's reach, IN-32, PC-06 K-3; IN-07 (design) → IN-07's build (= SE-02), SE-04 | D | designs name the carriers. IN-06's design (landed at B-C) is REVIEWED again now that IN-08 has landed (`c13144b9`): it names carriers IN-08 created |
| IN-06 (built) → IN-35 | D | the Calamity's strain needs thread operations as a carrier (#457 `:136`, H-85, `33`); #457 `:200` orders FORCE-HAZARD after the threadwork re-plug and its ruling — after IN-06's BUILD, not its design. The class gate (#457 D1) is ANSWERED [medium] (RS-12, ladder step 3/4: `canon/philosophy/RULINGS.md:126-136` D-3 "Ruled: tensile", with P-07 and Jordan's 2026-10-04 item (6) — a CONSEQUENCE of held configurations failing, not a matter motion; baseline sign: unmanaged, it worsens outward with increasing intensity; revert: Jordan says the ongoing expansion is ambient matter motion) |
| IN-08 → every verb row ADDED or RE-SPECIFIED after it (IN-12's steps, IN-61's `succeed`, IN-32, PC-06 K-3); IN-08 → IN-09, IN-10 (landed `fae9e623`), IN-33 | D; F | IN-08 re-axes the alignment table 4 → 7; every verb row added after it is celled on the new axes (RS-1(a)), which binds IN-12's steps and the other verb-adding positions. The six-verb extension (`build`, `found`, `give`, `march`, `migrate`, `survey`) lands INSIDE the atomic cells commit: cells on the new axes are refused until the roster swap. NOT a density rule: `_check_sparse_table` (`data/verbs.py:900`; its checks `:917-933`) refuses only an unrostered key and an all-zero table, and sparse is lawful (`:956-957`, an unlisted pair reads `default_cell`), so IN-08's falsifier reads "every table verb has a cell on each axis, or is listed in a declared `uncelled:` set (`tell`, `thread_read`, `restore`) with its reason" (G-1). IN-09, IN-10 and IN-33 type EXISTING rows: their edge is F only — B-G closed (`0f998f64`), so the cells are authored once |
| IN-08 → IN-12 step 9 | D [UNVERIFIED until B-Q] | step 9 deletes `Person.pursuits`' declaration (#453 `:2468`) while IN-08 re-cells `Person.pursuits`; the two are read against each other at B-Q, after the live field exists |
| GO-01 (J-9) → GO-05, PC-05(1) | J | no version asserted first |

### A(1) Critical path to THE NINE

`measure:` line numbers are `engine/season/requirements.yaml`'s, re-opened 2026-10-06 (each is its row's `measure:` line).

One line per row; the full path, verb by verb and with each row's `blocks:` traced, is `_part2`'s section for that row,
which governs where the two differ.

| row | path (batch) | `measure:` | earliest `met` |
|---|---|---|---|
| R-01 | met at B-I (`93b45b9a`; `engine/season/requirements.yaml` R-01, the paragraph that sets the status) → IN-10's sub-steps (landed `905b7a21`) → B-X (three `11` re-takes, taken; O.2 E15) → IN-13 (landed `2e19aee8`; B-M closed `be02666e`; `11` re-take per O.2 E15, read against B-X's close re-take); H-116 named first if ≥ 96 % | `corpus_run` R3 rows + control; `wd_collect.py` < 96 % at `2x3` (`requirements.yaml:376, :504`) | met; re-checked at each re-take (E15) |
| R-02 | met; `11` re-taken at B-G, B-I, B-W (taken after IN-57 and at its close, `3bf936ee`; `engine/season/requirements.yaml` R-01), B-X (taken, `2f0c0227`), B-M (closed `be02666e`), B-N (closed `cf69ceed`; taken, `engine/season/requirements.yaml` R-01's) per O.2 E15 | `:504` | stays met |
| R-03 | met; `-k test_u2_` green through IN-29 (landed `4a2e4494`) and PC-06 S-1 (landed in B-E, `ac9724fc`) | `:594` | holds |
| R-04 | IN-10 `confer`/`establish`/`revoke` via (`confer` landed through IN-53, `5652e846`; `establish`, `revoke` on IN-10's enabler, landed `fae9e623`) · FA-01 heads act via their seats (B-J), IN-40 revised (landed `3f320093`) · IN-49 `levy`, conjunct (1)'s named verb (built at B-K, `c8d1db3a`; it executes 0 times in the realm and the corpus, so conjunct (1) is unmet) · SC-01 `determine` in the realm (B-N, closed `cf69ceed`: the fired-slot chain to `determine` closes on hand-built worlds only; in the realm `convene` is refused at its referent, H-163) · `remit_default` (J-8's per-post list ask-then, RS-8 [medium]) · conjunct (3): all SEVEN `scales:` rows `in_loop` — `_part2` R-04 names each row's owner or a named residue; IN-46 and IN-47 own two of them; their designs landed at B-C and neither has a build batch | `aperture 4 0` (`:684`); the seven `scales:` rows (`:70-189`) | not before every `scales:` row has an owner and IN-46's and IN-47's builds are batched (§A(4)) |
| R-05 | `challenge`/`accept` (B-G rows, `0f998f64`; executed at B-H's exit, `c13144b9`) · `comply`, `confer`, `oblige` (landed at B-I, `9d93cfab`) · `evade / defy`, `construe`, `exchange` (restorable, main file §0.5; unbatched) · `establish`, `revoke` (IN-10's enabler, landed `fae9e623`) · `forge`, `carry`, `migrate`, `survey` + Rung, `levy`, `found`/`build` (built at B-K, `c8d1db3a`: `carry`, `levy`, `found`/`build` execute 0 times in the realm; `forge` and `survey` execute there and stay in the corpus's always-refused set) · `work` (IN-45, stopped: ED-IN-0297) · `seize`, `march` (B-M, closed `be02666e`: `seize` forms person-side only where a held dispensation names the Record or rung, so it is never attempted in the corpus or the seed-0 realm — a named residue under main file §0.5's relaxed exit rule, pinned in `test_season_shape.py`'s never-attempted set; the `march` arrival executes only on hand-built worlds) · `open_case` → `convene`, `speak`, `determine` (B-N, closed `cf69ceed`: every corpus `speak` is refused `speech.unheard`, and `convene` is refused at its referent in the realm, H-163; `engine/season/requirements.yaml` R-05's B-N reading) · three inquiries graded — `research`, `examine`, `surveil`'s place case — three waiting (B-O) · `covenant`, `train` et al., `conceal`, `forgive`, `destroy_record` (B-Q) · `arrest`/`pardon`/`interrogate`, `raze`, `give` + Rung, `succeed` (IN-61: the heir's claim, RS-27) (B-R) · `tie / knot`, `thread_read` (B-S) · `fight`, `challenge`, `accept` re-read after IN-59's `with` and PC-10b's held-challenge binding (B-Y: each may fall to 0 executions, declared); `kill`/`wound` are not verbs (RS-5); pins re-recorded per step | `corpus_run` `WHERE THE <n> GO` (`:830`; the classes at `:813-822`) | CONDITIONAL: after B-R, B-S AND B-Y all merged (B-Y can regress `fight`, `challenge`, `accept`), only if every row's EXIT observed ≥ 1 execution in computed play (`aperture 4 0` or `corpus_run`), and not while ED-IN-0297 (`work`'s producer, IN-45) is unanswered. A row whose EXIT recorded 0 stays a named residue in its batch's HANDOFF line and R-05 stays unmet; no position is invented to fix it. `succeed` sits in the no-predicate/effect class until IN-61 |
| R-06 | IN-08 (B-G, `0f998f64`: the doctrine-pair cosine measured and recorded; RANKING under G-1's reading; H7's standing pair test, H3/H9: B-H, `c13144b9`) → IN-11 `release` ends an ambition (landed `2a2ed152`) → B-X (closed `2f0c0227`: `requirements.yaml` R-06's EXIT READING) → IN-38 (B-V, RS-21 item 2) | RANKING DISCRIMINATION (`:977`) + spread falsifier | B-V |
| R-07 | IN-18 G1, landed live at B-E (`ac9724fc`) with its two-season `build_realm(0)` realm reader (control 0 of 11449 pairs differing, shipped 3270) → SE-01 (B-F, landed `d12c8db9`) → IN-13 (landed `2e19aee8`; B-M closed `be02666e`): conjunct 3 (a fought field) UNMET at B-M's close, the realm fights 0 fields — residue H-175/H-149 (the chooser's referents, outside IN-13); no position is invented to fix it (main file §0.5) | `:1030` + G1's falsifier + `_eff_march`'s stance write reached | not before the chooser's referents (H-175, H-149) reach a field |
| R-08 | IN-08 (B-G, `0f998f64`, G-1's reading: only candidates whose verb has ≥ 1 celled axis count; H3/H9: B-H, `c13144b9`) → W26 → SC-01 (B-N, closed `cf69ceed`); H-62 → its owners (`_part2` traces both) | `:1075` | the `met` conjuncts are readable from B-G; the `blocks:` W26 reaches a sitting that decides on hand-built worlds only at B-N's close (`cf69ceed`; in the realm, H-163) |
| R-09 | the `u1_` selector fixed at B-C (IN-43, landed) → SC-01 `speak` graded (landed `947747e0`; B-N closed `cf69ceed`) → FI-01's inquiries (landed `6d94d9d3`) → `train` (B-Q, J-13 (iii): `pool_default` wherever a case names no vocation, RS-21 item 10) → IN-38 (B-V) | `:1173` | partial on the by-person pool until the source of `capability` beyond the interim is ruled (`_part5` §J.2); `_part2` R-09 measures today's reading |

### A(2) M2 and M3

**M2:** the STORY-BAR instrument (IN-19, landed at B-C: `harness/storybar.py`) → SC-01 step 16, THE BAR (landed `801f733e`, a test on seeds picked from a sweep; B-N closed `cf69ceed`) → IN-37 → IN-27 → IN-30 (B-U; IN-27 and IN-30 on RS-21 items 3 and 4
[medium; Jordan to correct]). **M3:** Gate-0's first step and the strategy-document edit landed at B-C (IN-42 = GO-02, GO-03) · GO-01 (J-9) → GO-05 (its IN-05 gate met: B-L closed, `fc4f3ba9`)
→ PC-05 (1), all B-Z.

### A(3) Cycles and false dependencies

| finding | verdict |
|---|---|
| anything need J-10 before IN-09? | No. IN-10 reads a held dispensation's `terms` (Record field, exists); IN-12 step 7 `covenant` mints a Record (K-54), not `comply`'s cell; `24h` P7 retired only on IN-09's typed form. `verb_table.yaml:139` read by nothing on the graph before IN-09 [UNVERIFIED beyond grep of `comply` consumers in `decision/`, `loop/`] |
| SC-03 BLK:SC-01 whole (the first adjudication pass) | **Partly false.** Split **SC-03a** (landed `c2f855d2`; step 2b docket names arrangement/petition; step 3 `detain`/`ban` + readers + widened `determination` basis — needs IN-10/IN-11, `gate.py`) into the verb chain; **SC-03b** (step 4 `determine` contested; landed `d855576b`) after SC-01 |
| missing F: IN-35 after IN-21 `3544d568` / SE-01 `d12c8db9` (`matter.py`) | serialised in §B |
| no cycle | the verb chain is a line; `covenant` ← `commit` ← `utter` hold is a chain |
| the verb-chain row read as an order | **Not an order.** It is the F set above; §B's spine orders it. IN-12 step 6 landed before SC-01 (B-M closed `be02666e` before B-N, closed `cf69ceed`) and steps 7, 9, 10, 13, 5, 5a, 11 after it (B-Q, B-R) by batch order alone: no data edge ties any step to SC-01 |
| B-P parallel with B-Q | **False.** SC-02's `22b` step 24 writes in `_eff_determine` (`loop/effects_information.py:229`), which B-Q's steps also edit, and both claim `write_matrix.yaml`'s `unproduced:` line for `(Person, pursuits)`; B-P lands before B-Q (the `22b` row above) |
| IN-14 → IN-57 (landed `3bf936ee`) | **None.** IN-57's tier key reads ambitions, tenures, purview and valence, never the budget; IN-14 is MEASURED, NOT LANDED and is not among B-J's members (`_part4` IN-14; `_part8` §N names the batch reading that disagrees), so no edge is written |
| IN-35 behind IN-06's design | **Too early.** It needs IN-06's BUILD (#457 `:136`, `:200`), so it sits in B-S, after IN-06's build |
| IN-08 heads the verb batches because "a loader raising on partial landing needs every table verb celled" | **False reason.** The loader accepts a sparse table (`data/verbs.py:956-957`); "partial landing" is the atomic roster swap, not density. The real edge runs to the verb-ADDING positions only (§A, the IN-08 row); IN-08's place before IN-09…IN-33 is a file choice (cells authored once) |
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

- **#453 R-5 → IN-61 (B-R).** `succeed` sits in R-05's "no predicate/effect" class (`requirements.yaml:813-822`;
  the `verb_table.yaml` `succeed` row's `decline_note`: a carrier nobody reads), so R-5 is ON R-05's path, not "on no row's path".
  Item 9 adopts (b): `inheritance` as a fourth conferral basis, after IN-12; RS-27 (2026-10-14) re-specifies it as a gate
  basis admitting the heir-title holder's own `succeed` claim on a vacant throne, not a CENSUS fill (IN-51, retired). Jordan's 2026-10-04 "(9) royal succession crises" is the churn engine
  it drives. R-05's earliest `met` is after B-S and B-R both merged, on the conditions §A(1) states.
- **H-111 → FI-01's deposit half (landed `6d94d9d3`)**, built as SKIP at WITNESS except keyed kinds a verb declares (item 1).
- **J-13 → IN-12 step 9 (B-Q)**, (iii) as the interim: `pool_default` wherever a case names no vocation; `train` writes
  `Person.capability` only where a case names one; R-09's by-person pool stays partial until a source is ruled (item 10).
- **`13`-rest → IN-38 (B-V)**: scale the overlays on the NPC lane only, on the per-case observable (item 2).

**Answered, off the critical path** (RS-21, same tag and revert): #457 D6 → IN-27, IN-30 (B-U; item 3); #457 D4 → IN-36,
FA-01's content and the Schoenland trade-demand clause (B-V; item 4, G-6); #457 D2 → IN-34 (B-F, landed `44fdb4df`; item 5, with its
birth-tick hash note); J-18 (A) → MB-07 (landed, `b31d2c31`, shipped OFF; the flip is MB-07r; item 6); J-20 (B) and J-21 (A) → PC-07 (landed, `9054df80`; items 7 and 8).

**Still held, ON a path to THE NINE:** J-13's remainder — the source of `capability` beyond the interim (iii) — is the item
R-09's by-person conjunct, hence M1, waits on (`_part5` §J.2). And ED-IN-0297 (`needs_jordan`: where a works comes from in
computed play — `work`'s producer, `_part5` IN-45), on R-05's path.

**Still held, off every path to THE NINE** (RS-21's STILL HELD list; ranks and evidence are `_part5` §J's): J-9 (the Godot
version and the tenth attribute name — M3 only: GO-01 → GO-05 → PC-05 (1), B-Z), J-14, SM-1 (SC-06, asked at B-N), the
CAST-POPULACE spread construal (SE-04 (c), B-Z), `decision_policy_v1.md`'s fork, `godot_conversion_strategy_v1.md`,
`2026-09-03-governance-corpus-rebuild/`, A-24 (i), H-89, H-56's nested half.

**Ask-then, blocking nothing** (B-Z's ask rows): J-8's per-post list (RS-8 [medium]); J-15, J-19 (J-16, J-17 and IN-14's repair shape are delegated-ruled 2026-10-12, `_part5` §J.2); SM-15's timing
(SC-05, asked at B-N); the CELL-VALUE AND COSINE PASS, attached to IN-08 and following its landing (`c13144b9`) — Jordan revises cell values (at
least the `doctrine` row) against the cosine instruments (the doctrine pair, `conviction_spread`, the correlation table of
`candidate_pursuit_cells.md` §5.3); RS-3 amended; the decision-surface defaults H-54 / H-194 and SE-06's cohort question, asked together
at B-X's close `2f0c0227` with IN-62's `--arms` grid (ED-IN-0296, written, `needs_jordan`; `_part5` §J.2's ask-then rows).

**Decided by logic and precedent** (Jordan 2026-10-06: "apply all critic fixes, author fixes for all gaps without my rulings
based on logical and precedent, then re-batch"; each [medium; Jordan to correct], revert: Jordan states the other option):
G-1 `tell` stays uncelled by design, and R-06/R-08 count only candidates whose verb has at least one celled axis.
`requirements.yaml` carries no `met` wording for R-06 or R-08 (their keys are `statement`, `status`, `measured`, `measure`,
`blocks`, `disposition`, `needs_jordan`; the `met` lines are `_part2`'s own), so the record edit IN-08 owes is (i)
`corpus_run`'s RANKING line counting only those candidates, its numerator and denominator printed, and (ii) a `measured:`
note in R-06 and R-08 recording the reading; G-2 H-52 closed "assumption stands" at B-C (IN-43, landed); G-3 `refusal_axis` (H-146) is
not armed; G-4 IN-40 revised (landed `3f320093`; no stored parent); G-5 IN-46 … IN-50; G-6 the Schoenland trade demand rides FA-01's
content; G-7 every other gap the same instruction covers.

**Left the held list** (Jordan 2026-10-06 unless dated): J-1 and J-5 ANSWERED (RS-1: the two `candidate_*` drafts folded
into the build; IN-08 landed at B-G and B-H, `0f998f64`, `c13144b9`); J-8 PARTLY ANSWERED [medium] (RS-8); #457 D1 ANSWERED [medium] (RS-12); SM-5
CONFIRMED by Jordan's words (RS-6); H-101 ANSWERED [medium; Jordan to correct] (RS-19, ladder step 4/5 on Jordan's typed
requirements of 2026-09-02, events `b2133a54-992d-4505-82fc-3b9bb2b703eb`, `d111dc52-31a9-4903-b0a8-d3b3fa897324`,
`5959df57-b1e8-43b9-9478-34a7c26bac17`, `41eb0216-3f37-4004-877f-28dc5379d782`, `8980df9f-2b11-430c-bff8-901eaca46721`, and
2026-09-03, `95b03164-d4a1-4216-92a6-1b52bc74f1e0`, `40966503-d8a0-43b1-be74-3ad5fa55aa33`: a faction can be under a larger
faction and offices nest), read under G-4 against RS-9's words (purview reaches "Descendants only"; who is above is the
"rung above of same faction"; "factions can be of any scale") and #453 §7.2 (vassalage as the seat-holder's own `oblige`):
derived containment plus the oblige-edge clause, no stored `superior:` — IN-40 built it (landed `3f320093`). Revert: Jordan prefers a stored
parent.

## B. BATCHES

One batch = one session's working context = one PR; batches are FILE CLUSTERS with the membership rules of §B.0; a late
position is slotted by its EDITS (R1–R9). `{…}` = a parallel worktree lane merging after the chain (§C.2). Serial spine:
B-A → B-D (closed: `9054df80`, `b31d2c31`, `0a690b30`) → B-G (closed: `0f998f64`) → B-H (closed: `c13144b9`) → B-E (closed: `ac9724fc`) → B-F (closed: `53807be4`) → B-L (closed: `fc4f3ba9`) → B-I (closed: `9d93cfab`) → B-J (closed) → B-W (closed: `3bf936ee`) → B-X (closed: `2f0c0227`) → B-K (closed: `c8d1db3a`) → B-M (closed: `be02666e`) → B-N (closed: `cf69ceed`) → B-O → B-P → B-Q → B-R → B-S →
B-T; B-U beside B-P and B-Q (opens after B-N, closed `cf69ceed`; merges before B-R); B-V after B-M (closed) in parallel (merges before B-S); B-Y beside B-S (opens when B-R and B-V are merged; merges before B-T); B-Z as
ruled. [medium; Jordan to correct — B-P before B-Q and these gates; revert: Jordan states the other option.]
**B-I is CLOSED** (closing code commit `9d93cfab`, PR #472). What it left open is in the entries: `_part5` IN-09 (`evade / defy`, `construe`) and IN-33; `_part4` IN-18 (G5's trigger); IN-10 (the enabler) landed at B-K (`fae9e623`).
**B-F is CLOSED** (`53807be4`): IN-21 (`3544d568`), SE-01 (`d12c8db9`), IN-34 (`44fdb4df`, shipped dark, with H-206's holder half, `d47077d5`) and IN-22's live arm (a test in `engine/season/tests/test_in22_shortfall_reach.py`, run in `scarce.governed`; H-160 limit (3) ruled a balance number, 2026-10-12) landed. **B-L is CLOSED** (`fc4f3ba9`). **B-J is CLOSED** (`42c5588c`; merged `092fc453`, #476): SC-03a (`c2f855d2`) and IN-40 (`3f320093`) landed; FA-01's mechanism needed no data edit (all six authored heads were already seated; `engine/season/tests/test_fa01_head_seats.py`); IN-31's design landed (`proposals/2026-10-14-in31-revocation-cost-provenance.md`, PROPOSED; its build is B-Q). **IN-48 left B-J as B-JR**: its `delegate` tenure kind was built and REVERTED because it contradicts ratified Layer 1 (`_part5` IN-48 STATE). B-JR gates nothing: B-W follows B-J, not B-JR, B-X behind B-W (RS-30) and B-K behind B-X [ASSUMPTION; medium; Jordan to correct; revert: IN-48 returns to B-J's row and B-W waits for it]. B-JR is unscheduled and edits `state/gate.py`, so it serialises with any batch that does (R7). **B-W is CLOSED** (merged `3bf936ee`, #477; pre-squash `6a9caf85..2856e00e`): IN-54, IN-55 and IN-56 (hash unchanged), IN-57 (hash moved, declared) and IN-58 (stance-only; hash equal at the shipped fixtures) landed; IN-57 and IN-58 stay in `_part5`, narrowed, for what B-X, B-K and B-R read, and IN-58's sworn-to half is not built. **B-X is CLOSED** (`2f0c0227`): IN-62 (the instrument), IN-63, IN-64 (the cast), IN-71 (the doctrine coupling; as first built it zeroed `doctrine` for a conviction-less person, repaired at the close), IN-65 (the scar measured, no floor), FA-04, IN-66 .. IN-68 (the goals carrier, referents, seeding; seeding applies `influences` since FA-05), IN-69 (salience; `data/pursuits.py::pursuit_cosine`), IN-72 (the paired-claim scorer; it does not unblock RS-23's petition conjunct: H-209), FA-05, FA-06 (35 goal rows, the completeness refusal) landed. Its EXIT does not hold on leg (3) (`requirements.yaml` R-06); ED-IN-0296 asks Jordan; the `11` re-take on the fixed tree equals B-W's close (R-01). **B-K is CLOSED** (`c8d1db3a`, PR #483): IN-10 (the held-Record channel), IN-45's `forge` with its sheet consumer, `survey` + Rung, IN-45's `carry` and `migrate`, IN-49 (`levy`) and IN-28 (+ SE-03's MW-5) landed; IN-45's `work` stopped (ED-IN-0297, `needs_jordan`); `forgery_quality` returned to SC-02 `22b` step 25 (B-P, H-210); the closer of H-166 limit 3 is `raze` (IN-12 step 11, B-R). **B-M is CLOSED** (`be02666e`): IN-12 step 6 (`5ea1bb47`, `seize` over a warrant Record) and IN-13 (`2e19aee8`, the arrival; `seize` widened to Rung holds) landed; the realm still fights 0 fields (R-07 conjunct 3 unmet, H-175/H-149); hash unchanged; B-JR, B-N follow. **B-N is CLOSED** (`cf69ceed`): SC-01 steps 12 (`speak`, a typed contested cell whose band writes are empty: H-63), 14 (the obstacle ceiling, H-213), 13+15 (the `social_contest` provider; the kernel evaluated and not adopted; `chronicle` kept: H-214), the fired-slot step (H-163) and step 16 (THE BAR, as a test on seeds picked from a sweep) landed; step 11's vote-quorum conjunct was measured and NOT built, it waits on J-4 (H-161); `DEGREES RESOLVED` gaining `a proposition` is unmet and belongs to SC-03b (B-O); the `11` re-take moved `actor` -1.83 pp and `total` -2.06 pp, all of it step 12 (`engine/season/requirements.yaml` R-01); hash: `build_realm(0)` unchanged, the 1- and 2-season readings moved at step 12; B-O next.

- **Continuity** is the batch's HANDOFF line (§B.2) and git; the session is cleared at the clear point its card names.
- **Boundary:** when a batch closes, its finished positions are deleted from the plan in one net-deleting commit (`CLAUDE.md` §2: the commit is their record) and the run stops for a cleared window before the next batch opens (`methodology-execute`'s BATCH BOUNDARY).
- **Full suite:** once per batch, at its close, and only where the pins make a per-file run blind (`CLAUDE.md` §0.4 pt 1);
  B-A runs none locally (records; CI is the gate). Each position's own EXIT and FALSIFIER are in its entry
  (`_part4`…`_part7`); the exit instrument here is what proves the batch.
- **Hashes:** every batch's exit cell names its movers, with the pre-change `build_realm(0)` reading taken on its base
  commit (§A's hash row); a parallel lane re-runs its hash control on the merged tree (§C.2).
- **Where the cuts fall:** where the hub set changes (B-G/B-H interior files vs B-I verb files; B-J gate files; B-K refused
  verbs; B-N the provider; B-O graded; B-Q/B-R either side of IN-13's arrival, landed `2e19aee8`), merged where it is identical (SC-08
  in B-O, IN-26/IN-31 in B-Q, IN-61 in B-R, IN-23 in B-U, MB-04/MB-07 in B-D, WR-01..03 in B-D3). B-F is the
  `matter.py`/`fixtures.py`/`census.py` hub with no verb row; B-U and B-V hold the positions RS-21 made buildable whose files
  are driver/harness (B-U) and cast content (B-V).

### B.0 Membership rules

R1 — EDITS name `verb_table.yaml`, a count/set pin, or any `loop/effects_*.py` → cluster V; the batch is the earliest V batch whose entry gate covers the position's D edges (B-I closed at `9d93cfab`; B-J needs IN-10's sub-steps and IN-11 (landed, `905b7a21`, `2a2ed152`) or `gate.py`; B-K closed at `c8d1db3a`: a late refused-verb lift takes the V batch its D edges name; B-N closed at `cf69ceed`: a late proceedings-core position takes the V batch its D edges name; B-O needs SC-01's provider (landed `f982f4c2`); B-Q/B-R need IN-13 (landed `2e19aee8`); B-S needs IN-06).
R2 — EDITS in `decision/options.py`, `loop/witness.py`, `queries/person_q.py`, `decision/choose.py` and no verb row → B-E if gate-free, else the V batch its D edges name. B-E closed at `ac9724fc`: a late position R2 would have put there takes the V batch its D edges name.
R3 — EDITS in `loop/matter.py`, `loop/census.py`, `data/fixtures.py` season/body terms, a larder/store reader in `world_q` → B-S/B-T if it needs IN-06/IN-07 (B-F closed at `53807be4`).
R4 — EDITS in `module_contracts.yaml`/`composition.json`/`manifest/`/`seam/wrappers/`/`loop/driver.py` → B-S/B-T (a re-plug, or a late move/split: B-L closed at `fc4f3ba9`), B-U (an ending step).
R5 — EDITS only under `harness/`, a record file, a ledger, `proposals/`, `godot/*.md`, or `cases/` → a lane in the next batch to open, merging last (C.2).
R6 — EDITS only under `systems/<name>/` → that lane's B-D batch (pre-move); a `modules/<name>/` edit → the batch its D edges name (B-L closed at `fc4f3ba9`).
R7 — EDITS in `state/gate.py` or `state/carriers.py` with `offices.yaml`/`populated.py` → B-J (gate) or B-V (cast).
R8 — a still-held item stays in B-Z until ruled, then slots by R1–R7 into the next unopened batch of its cluster, else runs as its own sub-batch.
R9 — no file overlap, no gate → its own lane in the first batch whose entry gate covers its D edges; merges last.

Where two rules fit, R1 outranks the others: a position that re-records a count or set pin is in the verb cluster whatever
else it edits.

**B-W, B-X and B-Y are placed outside R1–R9 (RS-28; B-X by RS-30, below; B-X closed `2f0c0227`).** The basis is DIRECT for B-W's slot (*"immediately after batch j"*) and for
"after B-J" (*"ensure all folds occur after batch j"*); B-Y's slot after B-R and B-V is the plan's [ASSUMPTION; medium;
Jordan to correct], as is each batch's internal order. **B-J's card's `next B-K` reads `next B-W` (RS-28)**; the card itself
is unchanged. B-Y sits after B-R,
because IN-59 and PC-10b edit `verb_table.yaml`/`rosters.yaml` with B-S (R2's file overlap, serialised at merge, §C.2) and
IN-60's input is B-V's content. Every position the 2026-10-14 fold adds or changes lands after B-J (RS-28: *"ensure all folds
occur after batch j"*). Revert (B-Y only): place B-Y after B-T.
**B-X was placed outside R1–R9 by the user (RS-30)** — DIRECT, 2026-10-14: *"we will be finishing our original session batch then doing this next one"* — after B-W's close and before B-K, and is CLOSED (`2f0c0227`).

Slotted by these rules: K-36 `interview`-as-prompt and FI-01's per-verb inquiry
shapes → B-O inside FI-01;
`give` + Rung → B-R (after IN-13's arrival, landed `2e19aee8`); the occupation-subsistence MATTER reader, if
built, → B-T by R3 (its hole row is H-212, `absent`); IN-48 → B-JR (R7); IN-61 → B-R's tail (R1, "after IN-12"; IN-51 is deleted, and IN-61 takes its slot); IN-46 re-read at B-L (`e77794a2`), IN-47 reviewed at B-H (`c13144b9`),
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
| **B-JR REGENCY (IN-48 redesigned)** (unscheduled; left B-J, `42c5588c`) | IN-48, design-first on Layer 1's route: `establish` a second seat over the domain, `confer` it, IN-10's `Tenure.term` (`01_AXIOMS.md` §E.2.2, `04:351`); MEASURE what ends a regency early; a new `revocation` basis is data in Layer 1's shape; a new `tenure_kinds` member is NOT licensed (Jordan's, `_part5` IN-48 STATE) | `state/gate.py` (`REVOCATION_RULES`, `may_fill`, `seat_hold`), `offices.yaml`, `harness/populated.py`, pins | IN-10 (a), (b) and IN-11 landed (`905b7a21`, `2a2ed152`); IN-40 landed (`3f320093`) | B-J merged (`092fc453`) | the design's own falsifier per `_part5` IN-48; the held `delegate` design's findings that apply (`proposals/2026-10-14-in48-delegation-carrier.md` §9). **Hash: movers** declared by the design; pre-change read on the base commit | 1 | not measured |
| **B-O PROCEEDINGS GRADED** | FI-02 (SC-08 `59ca2055`, SC-03b `d855576b` and FI-01 `6d94d9d3` landed; FI-02 STOPPED: no fieldwork provider exists, `_part6`) | `loop/effects_information.py`, `loop/witness.py:380`, `seam/ladder.py`, `verb_table.yaml`, `write_matrix.yaml:344`, `data/verbs.py:589-604`, `rosters.yaml` (routing column, `verb_capability`), `manifest/registry.py:26`, `module_contracts.yaml`, `composition.json`, `test_u7_remit.py`, pins (`:2188`, `:12962`) | FI-01 (landed `6d94d9d3`) → FI-02 (D, satisfied) | B-N closed (`cf69ceed`) | (`data.arrangements` loaded in a headless run and `Tenure.degree` set on a contested `determine`: landed, `test_arrangements.py`, `test_u7_remit.py`) (FI-01 landed `6d94d9d3`: three inquiries graded, skip at WITNESS, `engine/season/tests/test_fi01_graded_inquiries.py`) `test_season_providers_are_registered` asserts the new role; pins re-recorded. **Hash: movers** FI-01's, declared and re-pinned at `6d94d9d3` (`test_season_weather.py`); FI-02 moves none | none | ⚠ 205/120 — the clear point after SC-03b has passed |
| **B-P PROCEEDINGS TAIL** | SC-02 (`22a` → `23` → `22b`: `22a` re-greps the readers of `Claim.visibility` and decides keep or delete — IN-18's G6 landed `66bf51f9` and is dormant in play, H-204; `22b` step 24's degree-keyed write targets `(Person, pursuits)` and owns `write_matrix.yaml`'s `unproduced:` line for it until B-Q; step 25 is re-added at B-K's close: the `forgery_quality` writer and reader, H-210); {SC-04 (+ the `succession` arrangement row, `disposes: hold`, that IN-61's tribunal route reads; RS-27)} | `data/` loaders and ids, `data/files.py::effects_modules()`, `queries/faction_q.py:88`, effects modules per `19_PLAN.md` steps (`_eff_determine`, `loop/effects_information.py:229`, for step 24), `write_matrix.yaml:186-193`, `state/carriers.py:283` (`Claim.visibility`); `arrangements.yaml`, `test_arrangements.py`, `test_stress_proceedings_rehost.py` | SC-03b (landed `d855576b`) → SC-02 (D, satisfied); SC-03a (landed `c2f855d2`) → SC-04 (rows, D, satisfied); IN-18 G6 (landed `66bf51f9`) → `22a` (D) | B-O merged; **parallel with B-U only** (loaders/ids vs driver/harness); lands BEFORE B-Q (step 24 shares `_eff_determine` and the `(Person, pursuits)` row with B-Q) | one planted violation per loader invariant → `SystemExit` naming its row; `SeatId` as `Act.actor` refused; SC-04's not-ported list shrinks by exactly the re-hosted cases. **Hash: movers** `22a`/`22b`'s field deletions by schema — the corpus hash moves; `23`'s wrappers leave `content_hash` unchanged; pre-change read on the base commit | 1 | 130/95 |
| **B-Q VERBS II** | IN-12 steps 7 (`covenant`), 9 (`train` et al. under J-13 (iii)'s interim, RS-21 item 10: writes `capability` only where a case names a vocation; its deletion of `Person.pursuits`' declaration re-read against IN-08's live field [UNVERIFIED]; it amends `write_matrix.yaml`'s `unproduced:` line after `22b`), 10 (`conceal`), 13 (`forgive`); IN-26 (`destroy_record` executes ≥ 1); IN-31 build | `verb_table.yaml`, `rosters.yaml`, `decision/options.py`, `loop/witness.py` (`anchor_of`, `_ch_witness_key`), `loop/effects_information.py`, `loop/effects_governance.py`, `loop/matter.py` (IN-26), `state/carriers.py` (`Person.capability`), `write_matrix.yaml`, the host input builder's `_pool_of`, `harness/corpus_run.py:875`, pins | IN-10 → 7 (D, landed `fae9e623`: a Proposition term has no route, H-94; IN-11 landed `2a2ed152`); IN-25 → 13 (D, landed `ac9724fc`); FI-01 (landed `6d94d9d3`) ↔ IN-26 (F; SC-01's half satisfied, B-N closed `cf69ceed`); SC-03a (landed `c2f855d2`) → IN-31 (D, satisfied); `22b` step 24 → step 9 (F) | B-O merged (FI-01's `effects_information`/`witness`); B-P merged (`_eff_determine`, `write_matrix.yaml`) | per step (`_part5` IN-12 table), each step executing ≥ 1 in `aperture 4 0` or `corpus_run` beside its `w.log` observation: an addressee's `commit` to a covenant; an Event anchors on a `cover` id; `forgive` leaves `stance_toward == 0`; `Person.pursuits` moves under `train`, `_pool_of` varies where a vocation is named; records/season flatten and `destroy_record` executes ≥ 1; `revoke` has > 1 outcome across provenances; a step at 0 is a named residue; pins re-recorded. **Hash: movers** every newly executing verb and `Person.capability`'s writes, by outcome; pre-change read on the base commit | none | ⚠ 175/105 — clear after step 10 |
| **B-R VERBS III + SUCCESSION** | IN-12 steps 5 (`arrest`, `pardon`, `interrogate`; + the RS-23 EXIT conjunct, a petition against a killer), 5a (the charge; the petition route, RS-23), 11 (`raze`); `give` + Rung; IN-61 (succession, RS-27: the heir is the holder of the throne's registered heir seat, linked by a `successions` registry in `rosters.yaml`; `inheritance` joins `conferral_bases` as the gate basis admitting that holder's own `succeed` claim on a vacant throne; RS-21 item 9 re-specified; EDITS per `_part5` IN-61) | `verb_table.yaml` (`give`'s cell; the `succeed` row), `rosters.yaml` (`conferral_bases`, `successions`), `offices.yaml` (`off_king`, `off_heir` `conferral:`), `loop/effects_information.py`, `loop/effects_governance.py`, `state/gate.py`, `loop/effects_founding.py` (`raze`), pins | SC-03a (landed `c2f855d2`), IN-10 (landed `fae9e623`; a Person term has no route, H-94) → 5/5a (D); IN-58 → step 5's RS-23 conjunct (I, landed `3bf936ee`); IN-72 → step 5's RS-23 conjunct (D, B-X); IN-28 (landed `32024e27`), IN-13 (landed `2e19aee8`) → 11 (D/R, satisfied: `raze` copies `_seize_rung`'s inlined occupation read, `holder_faction_of` + `mustered`; H-151's recorded residues — holder-vs-occupier, two armies unopposed, `travel.ended` rooting at [ROOT] — are in the H-151 cite); IN-13 → `give` + Rung (D, satisfied); IN-12 all → IN-61 (R, "after IN-12"); SC-04's `succession` row → IN-61 (D, B-P) | B-P, B-Q and B-U merged; B-K closed (`c8d1db3a`; IN-28); B-M closed (`be02666e`; IN-13 `2e19aee8`: a `march` arrival and `seize` over a Rung hold, read as OCCUPATION = `world_q.mustered(...)` at a settlement whose `holder_faction_of` differs from the mustered faction) | `aperture 1 0` `arrest` ex > 0; `move` refused in custody; `detention.ended`, `confession.made`; a hand-built charge and a witness's `commit`; `w.rungs` shrinks on `raze`; a rung `hold` changes hands by `give`; a death followed by the heir-title holder's `succeed` claim opening the throne's hold (IN-61); a petition against a killer docketed, or named as residue (step 5's RS-23 conjunct); each step executing ≥ 1 in `aperture 4 0` or `corpus_run`, a step at 0 named as residue; pins re-recorded; **R-05's earliest `met` is read here only together with B-S and B-Y, on §A(1)'s conditions**. **Hash: movers** every newly executing verb, by outcome; pre-change read on the base commit | none | 150/95 |
| **B-Y ACCESS, SECURITY, DUEL TERMS** (after B-R/B-V: the plan's placement under RS-28's "after B-J" [ASSUMPTION; medium; Jordan to correct; revert: after B-T]) | PC-10a (the chain head, PC lane: the stop rule in `modules/combat/wrapper.py::fight`) → IN-60 (`guard_weight`) → W2's arm measured (an instrument edge) → IN-59 (a) (the attack conjunct) → IN-59 (b) (the `audience` stem on `move` and `migrate`, on B-V's guard content) → PC-10b (the `challenge` Record and `challenge_terms`; `accept` bound to a held challenge Record; `duel.yielded`) | `verb_table.yaml` (`fight`, `accept`, `challenge`, `move`, `migrate`), `rosters.yaml` (`record_kinds`, `challenge_terms`, the `stakes` key), `data/requires.py` (the `audience` stem), `queries/world_q.py` (`guard_weight`; `WorldReader.read` for `audience`; `writs_held`), `modules/combat/wrapper.py`, `modules/combat/fight.py`, `seam/wrappers/combat.py`, `loop/effects_combat.py`, `loop/effects_information.py`, pins | PC-10a → PC-10b (D); IN-60 → IN-59 (D); IN-40 → IN-60, IN-59 (D, B-J); B-V's guard content → IN-60's reading, IN-59 (b) (D); W2's arm → IN-59 (I); IN-59 (a) ↔ PC-10b (F: the `challenge`/`accept` rows) | B-R merged; B-V merged (IN-60's content). **Beside B-S** (both edit `verb_table.yaml`/`rosters.yaml`: serialised at merge, §C.2); merges before B-T; B-S's gate does not gain B-Y | `guard_weight` read by IN-59 and stored nowhere; a cross-settlement `fight` refused and the co-located pair executing; a guarded court refusing a stranger and admitting a writ-holder, a sworn man and the seat's purview; a `blood` challenge yielding with `surrender` set and no `person.died`; an `accept` with no held challenge refused; R-05's `fight`, `challenge` and `accept` rows re-read (each may fall to 0 executions in computed play, declared; R-05's earliest `met` is read only after this batch); the executed / always-refused pins re-recorded; `register --requirements` exit 0. **Hash: movers** IN-59's refusals and PC-10b's terms wherever a challenge forms, by outcome; IN-60 alone none; pre-change read on the base commit | none (PC-10a is the chain head, not a lane) | ⚠ 210/130 [estimate: `wc -c` ÷ 4, read 2026-10-14 — `rosters.yaml` 207k and `verb_table.yaml` 169k whole / by row working, `data/requires.py` 56k, `state/gate.py` 85k, `queries/world_q.py` 140k, `modules/combat/wrapper.py` 52k, `modules/combat/fight.py` 4k, `seam/wrappers/combat.py` 16k, `loop/effects_combat.py` 18k, `loop/effects_information.py` 42k; pins by site] — clear after IN-59 |
| **B-U STORY + ENDINGS (M2 tail)** | IN-37 → IN-27 (#457 D6, RS-21 item 3: a Query over holds and seats the season reports; a `driver.py` ending step) → IN-30 (a loop-side caller of `uncontrolled`, `faction_holding`); {IN-23} | `loop/driver.py`, `queries/world_q.py` (`uncontrolled` `:1192`, `faction_holding` `:1129`), `queries/` (new Queries), `harness/` (render, STORY-BAR reader) | SC-01 step 16 → IN-37 (D, satisfied: landed `801f733e`; IN-19's reader landed at B-C); IN-37 → IN-27 → IN-30 (D) | B-N closed (`cf69ceed`); **beside B-P and B-Q** (driver/`world_q`/harness vs their files; `world_q` is shared with SC-08, landed `59ca2055`); merges before B-R and B-T | a render a reader can follow (writes nothing to `World`); an ending reached by choices only (a threshold-fired ending with no person's act among its antecedents fails); `uncontrolled(` has a caller in `loop/` or `decision/` executing in a seeded season; IN-23's Query read by a person's windowed estimate, no stored value. **Hash: movers** IN-27's ending step and IN-30's caller, by outcome; pre-change read on the base commit | 1 | 110/80 |
| **B-V CAST** | {IN-36 (one foreign faction, two seats, #457 D4, RS-21 item 4; + IN-60's guard content — guard cohorts at the principal's home and the throne and duchy `obligees:`, RS-26, carried in IN-36's entry, not FA-01's [ASSUMPTION; medium; Jordan to correct]) → FA-01 content with the Schoenland trade-demand clause — ONE copy, in FA-01 (`_part7`); IN-36 points at it; carrier `exchange` (IN-33: reverted at B-I, `cdc03f67`, restorable under main file §0.5; it lands before B-V) [ASSUMPTION; medium; Jordan to correct — revert: a `covenant` reader, B-Q]} {IN-38 (NPC-lane overlays on the per-case observable, RS-21 item 2)} | `harness/populated.py`, `rosters.yaml`, `references/npc_registry.yaml`, `offices.yaml` (+ `obligees:`, IN-60's content), `cohorts.yaml` (guard cohorts); `cases/exercises/*.yaml` (disjoint) | IN-13 → IN-36 (D, satisfied: landed `2e19aee8`); IN-36 → FA-01 content (D) | B-M closed (`be02666e`; IN-13 `2e19aee8`); **parallel with B-O…B-R** (merges after them on `rosters.yaml`); merges before B-S | a foreign `march` reaches the seam through the real chooser; each foreign faction is in `data/rosters.py::FACTION_BY_PROP`, or a `march` on its town reads as unheld (`holder_faction_of` None: arrival without a fight) and its seat holders can never `seize`; off, byte-identical; a demand forms from a foreign seat; IN-60's content: the throne and duchy `obligees:` non-empty and a guard cohort seated at the principal's home (the King's home, a duke's home; read by IN-60 at B-Y); IN-38: per-case executed-set change against the no-overlay arm, seed named; R-06/R-09 re-measured. **Hash: movers** the foreign faction's persons and seats (new `World` entries) and IN-38's overlays (per-case corpus hashes); the "off" arm byte-identical; pre-change read on the base commit | 2 | 95/70 |
| **B-S RE-PLUG I (threadwork, knots, ties)** | IN-06 build (design re-reviewed after B-G: it names carriers IN-08 creates) → IN-35 (coupling rule; `+` LOOP row) → IN-32 (`_eff_tie`) → PC-06 K-3 (`thread_read` operand) → FI-03 (design, then build); WR-01's `engine/season/` reach | `module_contracts.yaml`, `composition.json`, `systems/threadwork/sim/*` (store-shed, reach), `systems/fieldwork/sim/knots.py`, `systems/characters/sim/conviction.py`, `modules/` (each re-plugged closure's move, SM-7), `loop/matter.py:36-82`, `loop/effects_information.py`, `verb_table.yaml`, `state/carriers.py`, `rosters.yaml`, `manifest/registry.py` (FI-03's role row), `hole_register.yaml` rows, pins | IN-06 → IN-35, IN-32, K-3, FI-03 (D); IN-35 after IN-21 `3544d568` / SE-01 `d12c8db9` (F), and ↔ IN-34 (F: `loop/matter.py`); IN-17 → IN-32 (D, landed `ac9724fc`); FI-02 → FI-03 (D) | B-R merged (verb files); B-V merged (`rosters.yaml`); B-F closed (`53807be4`); B-D3 merged (threadwork in-module halves); IN-06's design reviewed after IN-08 | a plugged row's deletion refuses (fresh subprocess); one seed twice = one hash; unmanaged arm: lattice condition falls outward, managed arm stabilises, weight 0 = today; `aperture 1 0` `tie / knot` offered and executed > 0 with a reader; `thread_read` leaves the no-predicate set; FI-03's trail-only response; pins re-recorded; **R-05 `met` first readable after this AND B-Y (with B-R), on §A(1)'s conditions**. **Hash: movers** the Calamity coupling's non-zero arm and `tie / knot`, `thread_read` executing, by outcome; weight 0 = today's hash; pre-change read on the base commit | none | 145/95 |
| **B-T RE-PLUG II (settlements module)** | IN-07 build (= SE-02) → SE-04 (a) H-170 arms, (b) H-171 `Rung.envelope`; (c) stays HELD (the spread construal); the occupation-subsistence MATTER reader, if built (`engine/season/hole_register.yaml` H-212, `absent`: its owner, slotted here by R3 when a position takes it); {IN-52 (the levy-to-field feed, shipped OFF behind `field_provisioning`, the flip ON delegated-ruled and its own declared-mover commit at the tail, `_part5` §J.2; tail lane after IN-07's extractions)} | `queries/world_q.py`, `loop/matter.py` (extractions to `step_call`/`query`), `modules/settlements/`, `module_contracts.yaml`, `composition.json`, `cohorts.yaml`, `loop/census.py`, `harness/populated.py::seat_cohorts`, `state/carriers.py` (`Rung.envelope`); IN-52: `seam/wrappers/mass_battle.py`, `loop/effects_combat.py`, `verb_table.yaml` (`march`), `modules/mass_battle/` | IN-07 → SE-04 (D); IN-08 → SE-04 (D, landed); IN-07's extractions → IN-52 (D) | B-S merged (`matter.py`, `carriers.py` serial); B-U merged (`queries/world_q.py`); B-Y merged (`verb_table.yaml`, `queries/world_q.py`; RS-28); IN-07's design reviewed | per extraction: host body gone (`rg`), both hashes unchanged, composition-row deletion refuses; H-170's two arms executed on `build_realm(0)`; `envelope` has a writer or is deleted; IN-52 with `field_provisioning` off: both hashes equal the base. **Hash: movers** none per extraction, none from IN-52 shipped off (the flip ON is its own declared mover, re-pinning the realm hashes); SE-04's arms declared; pre-change read on the base commit | none | 140/90 |
| **B-Z HELD / LEAVE** (not a batch; slots by R8) | J-9: GO-01 → GO-05 → PC-05 (1) (one question: 4.6?); SC-05 (SM-15 timing), SC-06 (SM-1) — both asked at B-N's close (`cf69ceed`); SC-07 (each item builds when a carrier exists [ASSUMPTION; medium; Jordan to correct]); SE-04 (c); IN-44 (Layer 0/1, Jordan's files); GO-06 (another repository); MB-08, PC-08, FA-03, FA-07 (LEAVE); the ask-then rows J-15, J-19, J-8 per post (J-16, J-17 and IN-14's repair shape are delegated-ruled 2026-10-12, `_part5` §J.2), the CELL-VALUE AND COSINE PASS (IN-08 landed, `c13144b9`), H-54 / H-194 and SE-06 (both asked at B-X's close, ED-IN-0296; SE-06 is also §J.2 row 4's). IN-46's and IN-47's builds are NOT here: they are unscheduled, not held (§A(4)) | — | — | the ruling AND the member's own BLK | per entry; one-value items `/code-review` + `/simplify` | — | — |

**Placement notes** (so that this table, the state index and the entries agree; each rests on the §A row it names):

- **IN-08 binds only the verb-ADDING positions**: IN-12's steps, IN-61 (re-celling `succeed`), IN-32, PC-06 K-3. It precedes IN-09, IN-10
  and IN-33 by file (cells authored once), not by data. PC-01 landed at `9054df80`, before B-G, so E5's "never interleaved"
  holds. `challenge`/`accept` were added in B-G (`0f998f64`) and executed at B-H's exit (`c13144b9`).
- **IN-08 before IN-18's G1/G2 and IN-25**: B-G (`0f998f64`) → B-H (`c13144b9`) → B-E (`ac9724fc`), all landed. IN-18's G5 waits
  on its trigger, `oblige` having landed at B-I (`905b7a21`).
- **B-P lands before B-Q; B-U runs beside them** [medium; Jordan to correct]: SC-02's `22b` step 24 and B-Q's steps share
  `_eff_determine` and the `(Person, pursuits)` row; B-U's driver/harness files are disjoint from both.
- **Hash movers are declared in every batch's exit cell** (§A's hash row), each field at one commit.
- **IN-12 step 9 is in B-Q** under J-13 (iii)'s interim (RS-21 item 10); its deletion of `Person.pursuits`' declaration is
  read there against IN-08's live field.
- **Held in B-Z, no build of their own:** SC-07 (each item builds when a carrier exists, `_part6`'s assumption); SC-05 (`2-ii`; the
  kernel measured at SC-01 step 15, `f982f4c2`, and not adopted; SM-15's timing) and SC-06 (SM-1), ASKED at B-N's close (`cf69ceed`).
- **IN-35** builds in B-S after IN-06's build (§A, `IN-06 (built) → IN-35`); **IN-37** opens B-U (M2: SC-01 step 16 landed `801f733e`).
- **LEAVE and Jordan's files** sit in B-Z: MB-08, PC-08, FA-03 (LEAVE), GO-06 (needs a `valoria-game` checkout), IN-44
  (Layer 0/1, Jordan's: `_part8`).
- **IN-51 is deleted; IN-61 stays in B-R (R1)**, in IN-51's slot at the tail: it re-specifies `succeed` and re-records
  `DECLINED` (RS-27).
- **B-W and B-Y by ruling (RS-28, §B.0):** B-W (closed `3bf936ee`) landed its hash-neutral half (IN-54 → IN-55 → IN-56) before its
  declared mover (IN-57), so B-O and B-Q, which edit `epistemic.py`/`loop/witness.py`, build on the indexes; B-Y
  opens when B-R and B-V are merged, runs beside B-S and merges before B-T. B-S's gate does NOT gain B-Y; R-05's earliest
  `met` is read only after B-R, B-S and B-Y (B-Y can regress three of its rows, `_part2` R-05).

### B.2 Handoff cards

READ-FIRST = files and entries only (plus `CLAUDE.md`, always). The exit line is the one line left in
`registers/handoffs/HANDOFF_<LANE>.md` (template: `B-<id> <name> MERGED <sha>: <members>; pins re-recorded <sites>; hash
<unchanged|moved old→new, declared>; next B-<id>, READ-FIRST below`). Clear = when the session's context is cleared.

| batch | READ-FIRST | lane file · exit line | clear point |
|---|---|---|---|
| B-A | `_part8` §K; `references/restructure_ledger.md` (tail); the branch carries `7b619328` (the CI fix, built) | IN: `B-A ADOPT MERGED <sha>: v9 is the one plan; main green; next B-B/B-C/B-D` | after `All Gates Green` |
| B-JR | `_part5` IN-48 (STATE and §9 of its design); `proposals/2026-10-14-in48-delegation-carrier.md` §9; `architecture/meta/01_AXIOMS.md:1440-1580`, `04_CODE_ARCHITECTURE.md:340-380`; `gate.py` (`seat_hold`, `may_fill`, `REVOCATION_RULES`); `hole_register.yaml` H-108 (`:1571`) | IN: `B-JR MERGED <sha>: <regency route built or a needs_jordan row>; H-108 <grade>; pins re-recorded <sites>; hash <unchanged|moved old→new, declared>; next: the spine's next open batch` | after the design |
| B-O | `_part6` FI-02; `queries/cache.py::tenure_index` and `epistemic.py::changes_only_held_claims` (IN-54, IN-55, landed `3bf936ee`: `witness.py` and the channel predicates read the Tenure index and the fan skip); #453 `:561-564, :2462, :3341-3344`; `write_matrix.yaml:62-69, :340-344`; `witness.py:380`; `data/verbs.py:585-606`; `registry.py:22-26, :208-226`; `test_season_shape.py:2188, :12962` | FI: `B-O MERGED <sha>: arrangements loaded in production; determine contested writes Tenure.degree; three inquiries graded (research, examine, surveil's place case), three waiting; skip at WITNESS; second role <name>; hash moved <old→new>; next B-P (B-U may open beside it)` | after FI-02 |
| B-P | `_part6` SC-02, SC-04; `hole_register.yaml` H-197, H-204 (G6, landed `66bf51f9`); `19_PLAN.md:511-716`; `21_RECONCILIATION.md:582-594`; `faction_q.py:88`; `data/files.py:117-121`; `effects_information.py:229` (`_eff_determine`); `write_matrix.yaml:186-193`; `carriers.py:283` (`Claim.visibility`); `test_stress_proceedings_rehost.py:1-30, :111-131`; `test_arrangements.py:93` | SC: `B-P MERGED <sha>: 22a (visibility <kept: G6 landed or deleted>), 23 (invariants <list>), 22b (step 24 → (Person, pursuits); step 25: the `forgery_quality` writer and reader); arrangements <n> rows; re-hosted <cases>; hash moved <old→new>; next B-Q` | after `23` |
| B-Q | `_part5` IN-12 rows 7, 9, 10, 13; IN-26, IN-31; `queries/cache.py::tenure_index` and `epistemic.py::changes_only_held_claims` (IN-54, IN-55, landed `3bf936ee`: step 10's `anchor_of` / `_ch_witness_key` edit sits on the Tenure index and the fan skip); #453 `:2468, :2480-2481, :3286-3287`; `witness.py` `anchor_of`/`_ch_witness_key`; `corpus_run.py:875`; `write_matrix.yaml:186-193`; `hole_register.yaml:3518` (H-156), `:845`, `:1925` (H-100); `_part5` §J's RS-21 item 10 | IN: `B-Q MERGED <sha>: covenant, train (capability where a vocation is named), conceal, forgive executing <n each, or residue named>; destroy_record executes; revoke provenances; Person.pursuits declaration <reading>; pins <sets>; hash moved <old→new>; next B-R` | after step 10 |
| B-R | `_part5` IN-12 rows 5, 5a, 11, IN-61, IN-58 (the grievance step 5's RS-23 conjunct reads), H-209 (its attention blocker), IN-70; `_part6` SC-04 (the `succession` row); #453 `:2072, :2472, :2511, :3233-3251, :3291`; `rosters.yaml` `conferral_bases`, `revocation_bases`, `tenure_kinds`; `offices.yaml` `off_king`, `off_widow_regent`, `off_heir`; `state/gate.py::has_conferral_basis`, `may_fill`; `world_q.py` `vacancies`, `seats_named`; `test_governance_build.py` (the conferral-basis tests); `verb_table.yaml` `give`'s cell, the `succeed` row; `_part5` §J's RS-21 item 9; `_part8` §M RS-23, RS-27, RS-29 | IN: `B-R MERGED <sha>: arrest/pardon/interrogate, charge (+ petition route), raze, give+Rung, succession (the heir's succeed claim executes; inheritance basis); petition against a killer <docketed or residue>; pins <sets>; R-05 classes <counts>, residues <list>; hash moved <old→new>; next B-S (B-Y opens once B-V is merged)` | after 5a |
| B-Y | `_part5` IN-59, IN-60, IN-36 (the guard-content note); `_part7` PC-10; `_part8` §M RS-25, RS-26, RS-28; `modules/combat/wrapper.py` `fight`, `Yield`, the wound-tracker re-initialisation; `seam/wrappers/combat.py::surrender_of`; `seam/ladder.py` (H-98's note); `verb_table.yaml` `give` (`with`), `fight`, `challenge`, `accept`, `move`, `migrate`; `data/requires.py` (`REQUIRES_STEMS`, `WORLD_ONLY_STEMS`, the basis clause's `check`); `queries/world_q.py::WorldReader`; `loop/resolve.py`, `decision/options.py` (the `presence:` declines — read, not edited); `queries/world_q.py` `presence`, `reach`; `rosters.yaml` `record_kinds`; `offices.yaml` `obligees:`; the W2 arm's reading | IN: `B-Y MERGED <sha>: guard_weight; access gate (with + audience); duel terms + yield (PC-10a <sha>); pins <sets>; hash moved <old→new>; next B-T` · PC: `PC-10a MERGED <sha>: non-lethal stop rule in fight (blood, yield); Yield unchanged; next PC-10b in B-Y` | after IN-59 |
| B-U | `_part5` IN-37, IN-27, IN-30, IN-23; #457 `:163-169, :175, :186, :190`; `driver.py` `season()`; `world_q.py:1192` (`uncontrolled`), `:1129` (`faction_holding`); `populated.py:1304`; `hole_register.yaml:3872` (H-176), `:4153` (H-186) | IN: `B-U MERGED <sha>: render; ending Query <name>; uncontrolled caller; legitimacy/stability Queries; M2 <reading>; hash moved <old→new>; next B-R once B-P and B-Q merge` | after IN-27 |
| B-V | `_part5` IN-36, IN-38; `_part7` FA-01 (the one copy of the trade-demand clause); `_part5` §J's RS-21 items 2 and 4, G-6; `offices.yaml:158-526`; `npc_registry.yaml`; `populated.py` cast overlay; `cases/exercises/` index | FA: `B-V MERGED <sha>: foreign faction <name>, two seats; demand clause via <exchange or covenant reader>; IN-38 <n> cases, per-case set change <reading>; R-06 <reading>; hash moved <old→new>` | after IN-36 |
| B-S | `_part4` IN-06 (+ `proposals/2026-10-07-unplugged-systems-replug.md`; reconcile the entry gate first, IN-06's finding (1)); `_part5` IN-35, IN-32; `_part7` PC-06 K-3; `_part6` FI-03; #457 `:123-143, :174`; `matter.py:36-82`; `hole_register.yaml:4034` (H-182), H-85, H-47; `knots.py:155-156`; `conviction.py:82` | WR: `B-S MERGED <sha>: threadwork/knots/conviction plugged; Calamity coupling (weight 0 = today); tie executes; thread_read typed; FI-03 <design or built>; R-05 <met or the residues left>; hash moved <old→new>` | after IN-35 |
| B-T | `_part4` IN-07 and IN-52 (+ `proposals/2026-10-07-settlements-computation-modules.md`); `_part6` SE-04; `effects_governance.py:308-347`; `cohorts.yaml`; `hole_register.yaml:3700-3725`; `world_q.py:498, :559-572` | SE: `B-T MERGED <sha>: settlements module extractions <list>; H-170 arms <readings>; envelope <writer or deleted>; hashes unchanged per extraction; SE-04(c) HELD` | after IN-07 |
| B-Z | `_part5` §J (the still-held list, its ranks and the ask-then rows); the member's own entry and its BLK; the batch its ruling slots it into (§B.0 R8) | the member's lane: `B-Z <item> RULED <date>: <the ruling, verbatim>; slotted to B-<id> by R<n>; next <that batch's card>` — or, for an ask-then row, `ASKED <date> at B-<id>: <answer or "no answer">` | per sub-batch: after its slotted batch's exit |

## C. FILE-COLLISION MATRIX

### C.1 By position (× = edits)

Serialisation points: `verb_table.yaml` (IN-09 IN-12 IN-31 IN-32 IN-33 IN-45 FI-01 PC-06 K-3 IN-61 IN-59 PC-10b), `rosters.yaml`, `decision/options.py`, `loop/matter.py`,
`loop/driver.py`, `seam/wrappers/*`, `state/gate.py` (IN-12, IN-61; IN-48 assumed), the count and set pins (`test_season_shape.py`, and `test_governance_build.py:817`, which is not a shape pin). Paths are under `engine/season/` unless named; "shape
pins" = `engine/season/tests/test_season_shape.py`'s count and set pins.

| position | edits |
|---|---|
| IN-09 | verb_table, effects_information, shape pins |
| IN-12 | verb_table, rosters, options.py, witness.py, effects_information/governance/combat/founding+economy, gate.py, shape pins |
| IN-14 | shape pins (decision/budget) |
| IN-18 (G5) | G5's site (re-derived by grep at its build, `_part4` IN-18 EDITS), shape pins |
| IN-35 (after IN-21 `3544d568`, SE-01 `d12c8db9`) | matter.py, world_q, shape pins |
| IN-26 | effects_information, matter.py |
| IN-27 † | driver.py (an ending step; `SeasonDriver.season` has none) |
| IN-30 † | a loop-side caller of `uncontrolled`; world_q (`faction_holding`) |
| IN-31 † | verb_table (`revoke`'s `writes`), effects_governance |
| IN-32 † | verb_table, effects_information (`_eff_tie`) |
| IN-36 † | harness/populated.py, rosters, `references/npc_registry.yaml` |
| IN-38 † | `engine/season/cases/exercises/*.yaml` (and the pins its observable re-reads, O.3) |
| IN-48 | assumed in `_part5`'s entry [UNVERIFIED]: gate.py (`seat_hold`/`via`), choose.py, resolve.py |
| IN-59 † | verb_table (`fight`, `accept`, `challenge`: `with`; `move`, `migrate`: `audience`), requires.py (`audience` in `REQUIRES_STEMS` and `WORLD_ONLY_STEMS`), world_q (`WorldReader.read`), shape pins |
| IN-60 † | world_q (`guard_weight`); its content is IN-36's (offices.yaml `obligees:`, cohorts.yaml) |
| IN-61 † | rosters (`conferral_bases`, `successions`), offices.yaml (`off_king`, `off_heir` `conferral:`), gate.py (`has_conferral_basis`; `may_fill` refusing `inheritance`; the `inheritance` rule), verb_table (`succeed`), shape pins (`DECLINED`), `test_governance_build.py`'s conferral-basis pins |
| IN-70 † | world_q, person_q [assumed] |
| SE-06 † (if answered) | cohorts.yaml (`temperaments:`), harness/populated.py (`seat_cohorts`), the SE ledger, pins |
| PC-10 † | PC-10a: `modules/combat/wrapper.py`, `modules/combat/fight.py`, combat tests (PC lane; the season chain may read, never edit); PC-10b: verb_table (`challenge`, `accept`), rosters (`record_kinds`, `challenge_terms`), seam/wrappers/combat.py, effects_combat, effects_information, shape pins |
| SC-02 † | `data/` loaders and ids, `data/files.py`, `queries/faction_q.py`, effects modules per `19_PLAN.md` (`_eff_determine` for `22b` step 24), `write_matrix.yaml` (the `(Person, pursuits)` `unproduced:` line), `state/carriers.py` (`22a`: `Claim.visibility`, kept or deleted at `22a`; IN-18's G6 landed `66bf51f9`, dormant, H-204) |
| FI-01 | verb_table, witness.py, effects_information, seam/ladder, shape pins |
| IN-52 † | seam/wrappers/mass_battle, effects_combat (`_eff_march`), verb_table (`march`), `modules/mass_battle/`, a `field_provisioning` fixture |
| FA-01 † | offices.yaml, harness/populated.py, `references/npc_registry.yaml` (content) |
| IN-33 † | verb_table, rosters |
| IN-37 † | harness/ (a reader; nothing else in `engine/season/`) |
| IN-45 (`work`) | verb_table, rosters, options.py, shape pins (its `_part5` EDITS, re-read when ED-IN-0297 is answered) |

† added from the entry's own EDITS field (`_part4`, `_part5`, `_part7`), read 2026-10-06 (IN-59..IN-61 and PC-10: 2026-10-14; IN-62..IN-72, FA-04..FA-06, SE-06: 2026-10-15). Every other row is the adjudicated matrix; the IN-18 and IN-22 rows were narrowed at B-E's close (`ac9724fc`) to what remains, and the IN-18 row again at B-I's (G6 landed, `66bf51f9`).

### C.2 Collisions inside a batch — the merge rule

**A `{…}` lane that edits a file its batch's serial chain also edits builds in its own worktree and MERGES after the chain;
two lanes sharing a file merge one after the other. After each such merge, RE-RUN THAT LANE'S EXIT AND FALSIFIER on the
merged tree — hash controls included, not only the pins.** A hash or pin taken on a tree the other side had not reached is
no control. The same rule binds two BATCHES run in parallel on the spine: the later to merge is the lane. The pairs this binds
hardest: B-V against whichever of B-O…B-R is open (`rosters.yaml`). O.2's preamble is the rule (`isolation: worktree` defers an edge
to the merge; it never removes it). Derived from §C.1:

| batch(es) | shared file | serial chain (first to merge) | lane(s) — merge after, then re-run their exit |
|---|---|---|---|
| every | `requirements.yaml`, `hole_register.yaml` | every position's forward sweep | every lane (O.2 E13) |
| B-P → B-Q | `loop/effects_information.py` (`_eff_determine`), `write_matrix.yaml:186-193` | SC-02's `22b` (B-P) | B-Q's steps — serial by B-Q's entry gate; step 9 amends the `(Person, pursuits)` `unproduced:` line `22b` step 24 set |
| B-P ∥ B-U; B-Q ∥ B-U | none (loaders/ids and verb effects vs driver/`world_q`/harness) | — | B-U merges before B-R; B-T's gate waits on it for `queries/world_q.py` |
| B-O…B-R ∥ B-V | `rosters.yaml`, `offices.yaml` (IN-61's `conferral:` edits at B-R; IN-60's `obligees:` content at B-V) | the open one of B-O, B-P, B-Q, B-R | B-V (IN-36 → FA-01 content; IN-38): merges after it and re-runs its "off, byte-identical" arm; B-S waits for B-V |
| B-Q | `loop/effects_information.py`, `loop/witness.py` | IN-12 steps 7, 9, 10, 13 → IN-26 → IN-31's build — all in the chain | none |
| B-X (closed `2f0c0227`) → B-V | `offices.yaml` (FA-04's `off_king` `obligees:`; IN-64's two Riskbreakers rows), `cohorts.yaml` (SE-06's `temperaments:`, if built; B-V's guard cohorts), `references/npc_registry.yaml` (IN-64's cast; IN-36's foreign persons), `harness/populated.py` (IN-68's seeding; IN-36's cast), `rosters.yaml` (IN-66's rosters; IN-36's) | B-X, closed (`2f0c0227`) | B-V (IN-36 → FA-01 content; IN-38): merges after, re-runs its exit and hash controls on the merged tree; SE-06's temperament rule, if built, is re-read for IN-60's guard cohorts |
| B-S ∥ B-Y | `verb_table.yaml`, `rosters.yaml`, the pins | the open one of B-S's chain | B-Y (PC-10a → IN-60 → IN-59 → PC-10b): merges after it, re-runs its exit and hash controls on the merged tree; merges before B-T |
| B-Y | `modules/combat/` (PC lane) vs the season files | PC-10a — the CHAIN HEAD, not a `{}` lane: the module edit lands first and PC-10b reads it | none; PC-10a's exit line is HANDOFF_PC's |

---

## O. ORCHESTRATION — carried from v8 `_part3` (O.1 is replaced by §B)

### O.2 Hard serial edges (live ones only)

Carried from the retired 2026-09-18 plan (§3.9) and 2026-09-28 plan (§3.5), both at `FORK:0671283`; edges both of whose ends
are finished are spent and omitted (v8 `_part6` §H listed them; not carried — read it at v8's `FORK:` ref). `isolation:
worktree` defers an edge to the merge; it never removes it. v9 also omits an edge whose earlier end has landed, since the
order then holds by construction (main file §0.6: E14 and E16 spent); each omitted edge is in the second table, with its reason.

| # | edge | why | origin |
|---|---|---|---|
| E15 | **THE ONE STATEMENT of the `11` re-take; every other mention points here.** It ran at the close of B-G (the CONTROL, `0f998f64`: IN-08's re-scoring, so B-I's reading can be separated from it), ran at B-I's partial close (`engine/season/requirements.yaml` R-01: IN-11's edges, not IN-10's, H-203), runs again when B-I's remainder lands (IN-10 adds cross-person edges), and at the close of B-M (`be02666e`; IN-13 arrives; its reading, when taken, is `engine/season/requirements.yaml` R-01's); **twice inside B-W: after IN-57 and before IN-58 merges, and again at B-W's close after IN-58 (both taken, `3bf936ee`: `engine/season/requirements.yaml` R-01's B-W RE-TAKES)** (IN-57's attention key moves the question order, and IN-58 changes `regard`, which `teller_weight` and choice read, `person_q.py` ~124-137 — both reconvergence inputs; two declared movers in one batch cannot be separated by one re-take taken at its close); **three times inside B-X (RS-30; all taken, `requirements.yaml` R-01 -- the reading that counts is the one on the fixed tree, equal to B-W's close): after IN-65** (the cast — IN-64's data with its two seat rows, IN-71's doctrine coupling and IN-65's floor if built — one input change, the cast's content and the readers of its intensities; control: B-W's close re-take), **after IN-69 and IN-72, before FA-05 merges** (IN-69 and IN-72 move the question order as IN-57 does; FA-04's one Tenure rides it), **and at B-X's close after FA-06** (FA-05's and FA-06's goal rows); if R-01 falls below its bar at any of them, main file §0.5's stopping rule applies to the last mover before it; SE-06, if built after its ask-then, takes its own re-take; and B-M's comparison reads against B-X's close re-take [ASSUMPTION; medium; Jordan to correct]; at B-N's close (closed `cf69ceed`; taken, `engine/season/requirements.yaml` R-01's); never across B-E (IN-16 … IN-18, IN-15, IN-25; closed `ac9724fc`). P-4 ran before the first, at B-C (IN-39, landed: `probed` equal across two runs) | B-E moves the claim channel `11` measures; a number taken across it has no control. B-I and B-M add the cross-person edges R-01 counts (§A(1)); without B-G's control, B-I's re-take cannot tell IN-10/IN-11's edges from IN-08's re-scored chooser | the telling carve-out, absorbed (main file §0.6); keyed to v9's batches (§B) |
| E13 | every position → its own forward sweep's `requirements.yaml` / `hole_register.yaml` edits | the shared record files; never edited from two worktrees at once | main file §0.4 |

**Omitted** (landing evidence: v8 `_part3` O.1 row 2, at v8's `FORK:` ref; `git log` #449–#456):

| # | v8 edge | why omitted |
|---|---|---|
| E4 | `22` (SC-01) → `2-ii` (SC-05) | `22` landed (B-N, closed `cf69ceed`; the prize rows repointed at `f982f4c2`): `2-ii` follows the repoint by construction |
| E5, its `8` half | the cells commit ↔ `8` | `8` landed (v8's Batch B, PR #451) |
| E5, its `9` half | the cells commit (IN-08) ↔ `9` (PC-01) | `9` landed (PC-01, B-D1, `9054df80`), before the cells commit |
| E7 | `8` → `ED-FI-0009` | `8` landed; FI-01's `seam/ladder.py` serialisation is §A's SC-01 → FI-01 (F+D) |
| E8 | `8` → `ED-FI-0009` → `14` → `17` → `13d-iii` | every end but `ED-FI-0009` landed (v8's Batches B, C); FI-01 is in §A's verb-chain set |
| E9 | `14` → `24h` P6 | both ends closed: `14` landed (v8's Batch C); `24h` P6 retired, superseded by IN-11 (#453 R-3; landed `2a2ed152`) |
| E10 | `11-fix` → `11` → `21`-rest | all three landed; the next `11` re-take is E15's |
| E11 | `13d-iii` → `22` steps 11–12 | `13d-iii` landed (v8's Batch C): `determine`'s bench has its scope-rung test (`sits_over`, not `purview_reaches`; §A(3)) |
| E14 | telling T4 → `14` | both landed (PR #449; v8's Batch C) |
| E16 | telling T6 → the AX-7 wiring | both landed: T6 (PR #449), the wiring (IN-15, B-E, `ac9724fc`) |
| E17 | `30` → `31a` → `22` (SC-01); `31a` → `31b` → `31c` | `31a`, `31b`, `31c` landed (IN-03 … IN-05; B-L, `fc4f3ba9`): `22` follows `31a` by construction |
| E18 | `31a`–`31c` (IN-03 … IN-05) ↔ every editor of a file O.3 or §C.1 lists with an `SM` position | `31a`–`31c` landed (B-L, `fc4f3ba9`) |

### O.3 File census — open positions × shared files

§C.1 is the per-position matrix and governs where the two differ; this is v8's per-file census, carried for the files and
consequences §C.1 does not state. Edits to the carried rows: a closed editor is removed (main file §3 lists only open
positions); a row left with no open editor is omitted (listed below); each v8 alias carries its v9 handle. `30` has landed (`5097e49`;
`rosters.yaml` `modules:`; `R04_PENDING_SUBSYSTEMS` derived at
`tests/valoria/test_engine_does_not_import_systems.py`), its close at `4a2e4494`.

| file | edited by | consequence |
|---|---|---|
| `engine/season/verb_table.yaml` | `ED-FI-0009` (FI-01), `19b` (IN-09) | serial in the IN/SC chains (§A's verb-chain set) |
| `engine/season/seam/ladder.py` | `ED-FI-0009` (FI-01), `2-ii` (SC-05: veto `extension=`) | `2-ii` is HELD (SC-05) |
| `engine/season/loop/effects_information.py` | `ED-FI-0009` (FI-01) | serial |
| `engine/season/cases/exercises/*.yaml` | `13`-rest (IN-38) | parallel authoring |
| `engine/season/tests/test_season_shape.py` | `13`-rest (IN-38) | every pin re-taken serially (§A's verb-chain set; §C.2) |
| `references/module_contracts.yaml` | `2-ii` (SC-05) | — |
| `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` | every forward sweep; `11` | E13 |
| `references/restructure_ledger.md` | `2-ii` (SC-05) | — |
| `.github/workflows/valoria-ci.yml` | `2-ii` (SC-05: the job folds) | — |
| `tests/valoria/test_engine_does_not_import_systems.py` | `2-ii` (SC-05) | E4 |

**Omitted rows and paragraph** (every editor closed, or the carve-out the row served is absorbed):

| v8 row | v8 editors | why omitted |
|---|---|---|
| `rosters.yaml` | `22` (SC-01: prize rows, `chronicle`) | landed (B-N, closed `cf69ceed`); `chronicle`'s deletion is held, `engine/season/hole_register.yaml` H-214 |
| `loop/effects_governance.py` | `14` | landed (v8's Batch C) |
| `loop/effects_combat.py` | the cells commit (IN-08) | landed (B-G, `0f998f64`) |
| `queries/person_q.py` | telling G1 (IN-18) | landed (B-E, `ac9724fc`), after IN-08 (`0f998f64`, `c13144b9`) |
| `decision/options.py` | telling T1, T3a, T4; then `14` | all landed; v9's editors are §C.1's |
| `queries/world_q.py` | telling T4 (`with`) | landed; v9's editors are §C.1's |
| `harness/populated.py`; `offices.yaml` | `13d-iii` | landed (v8's Batch C) |
| `harness/corpus_run.py` | `17` | landed (v8's Batch C); IN-43's print landed at B-C |
| `engine/engine_params/composition.json`, `engine/season/manifest/`, `engine/season/data/files.py`, `engine/season/loop/driver.py`, `tools/ci_common.py`, `tools/export_sim_params.py` | `31a`–`31c` (IN-03 … IN-05) | landed (B-L, `fc4f3ba9`) |
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
- **Working-session cost (RS-24, RS-28; added 2026-10-14)** [ASSUMPTION; medium; Jordan to correct]: B-W's hash-neutral
  half (IN-54 … IN-56, landed `3bf936ee`) makes every later batch's seeded probes and `aperture 4 0` readings cheaper to run, because the fan-out
  and emission scans it removes are what a season costs; it changes no answer, so no later reading is re-taken for it. Read
  `test_season_shape.py` and `hole_register.yaml` by site only (grep the assertion or the row id), never whole. Run the `11`
  re-take once per declared hash mover that moves a reconvergence input (O.2 E15), never per step. Revert: the cadence
  before this bullet.

---

## P. PRE-FLIGHT — remainder

**Read at B-C (IN-39, landed; the readings are in its commit body):**

| # | command | what it decided |
|---|---|---|
| P-4 | `cd proposals/2026-09-04-degree-sweep && python wd_chunk.py none default 0 36 && python wd_chunk.py none default 0 36` (same cell twice) | `11-fix`'s determinism attack: PASSED at B-C — equal, `probed` 5514 in both runs; no determinism defect |
| P-6 | for one `corpus_run` case, list the `questions_for` referents offered to a seated person, and compare with `build_realm(0)` (H-175) | READ at B-C; the reading is H-175's `cite:` in `engine/season/hole_register.yaml` — a measurement for R-04's table, not a build |

P-4 has run before `11` is first re-taken, which is B-G's control (§A(1) R-01; when: O.2 E15). Not carried: the settled pre-flight rows S-1…S-10 (not #445's S-1) and the
consumed P-1…P-3, P-5, P-7, P-8 — v8 `_part3` §P, at v8's `FORK:` ref.
