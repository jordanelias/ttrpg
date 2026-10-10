# Valoria — Master Workplan v9, part 2: THE NINE — how each core tenet gets built

## Status: part of v9 — see valoria_master_workplan_v9.md
## Reads after `workplans/valoria_master_workplan_v9.md` (§1 milestones, §3 state index, §4 crosswalk); graph and batches are `_part3` §A/§B. One section per row of `engine/season/requirements.yaml`; this part carries no decision of its own.
## Grade under `CLAUDE.md` §0.2: `paper`. A row of THE NINE moves only on its own `measured:` block, which `python -m engine.season.harness.register --requirements` validates. Nothing here moves a row.

**How each section is built.** Statement (verbatim, Jordan 2026-09-05) · status and the measured reading,
refreshed from the instruments read below where they disagree with the row's `measured:` text · what
moves it (positions, with batch) · what it needs that no position owned before this plan · the design
questions the tree does not answer (stated, never answered here — `CLAUDE.md` §0, scripting drift) ·
**`met`, stated as an instrument outcome**. Where the row's own `measure:` command can no longer
discriminate, that is said, and the replacement instrument is named as a record edit owed (not made
here).

**Instrument readings.** Read for v9, 2026-10-06, HEAD `8b57336`: `python -m engine.season.harness.register --requirements` exit 0 — met 2 (R-02 R-03), partial 5 (R-04 R-06 R-07 R-08 R-09), not_met 2 (R-01 R-05); `python tools/m1_acceptance.py --summary` exit 0 — `NOT MET`, one row failing (row 3, THE NINE 2/9, DOC-DERIVED).
**Every other figure here is carried and is not present tense.** Where a row's own `measured:` block holds a 2026-10-02 reading, the figure is re-keyed to it and reads "read 2026-10-02 from `engine/season/requirements.yaml:<line>`" (each paragraph names its tree); a figure with no such paragraph reads "read at v8, <date>" (HEAD `0671283`) **unless it carries its own date.** `14`, `13d-iii` and `17` landed after v8's 2026-10-01 readings (`COUNTERPARTY_CLAUSE`, `resolve_anchor`, `world_q.ambitions` are absent at `0671283`, present at HEAD), so a per-verb figure still labelled "read at v8" that they move is stale: re-run the row's `measure:` before quoting one. Not re-run for v9: `corpus_run`, `aperture`, `wd_collect.py`. Positions read `alias (v9 handle)`; a landed position has no handle. The two record edits v8 called owed (`21`-rest: R-01's stale opening, R-03's `measured:` refresh) are done: R-01 opens "46/46 NPC and 96/97 ARC" (`requirements.yaml:197-199`), R-03 holds a 2026-10-02 re-run (`:576-593`), read 2026-10-06.

**Summary — the critical path to each row, the batch each position lands in (`_part3` §B) and the earliest batch after which the row can read `met`; status and `measure:` re-read 2026-10-06 from `engine/season/requirements.yaml` (`register --requirements` exit 0, the counts above).** `_part3` §A(1) cites this table.

| row | status | positions on the path — `alias (v9 handle)`, batch | `measure:` (cites: `engine/season/requirements.yaml`) | earliest `met` |
|---|---|---|---|---|
| R-01 | met (B-I, `93b45b9a`; `engine/season/requirements.yaml` R-01) | `11` re-take after IN-08 as the control (B-G, `0f998f64`) → IN-11 (`2a2ed152`) and IN-50 (`5fa6ac16`) landed, `11` re-taken at B-I → #453 step 1 (IN-10: new cross-person edges; B-I, gated: H-203) → step 8 (IN-13: B-M, `11` re-take); H-116 named first if a re-take reads ≥ 96 % | `corpus_run` R3 rows + control (`:376`); `wd_collect.py` < 96 % at `2x3` (`:504`) | met at B-I; re-checked at each re-take |
| R-02 | met | keep met; the `11` re-takes at B-G (control), B-I, B-M, and B-N only if a reconvergence input moved (`_part3` O.2 E15) | `wd_collect.py` (`:504`) | met; re-checked at each re-take |
| R-03 | met | keep met; `-k test_u2_` green through IN-29 (H-110; landed `4a2e4494`) and PC-06 S-1 (landed in B-E, `ac9724fc`) | `headless` + `-k test_u2_` (`:594`) | met; holds |
| R-04 | partial | #453 step 1 (IN-10: `confer`/`establish`/`revoke` via; B-I) · IN-40 revised (vassalage as an `oblige` edge; B-J) · FA-01 mechanism (a faction head acts through a seat; B-J) · IN-49 (`levy`, after IN-10's second operand channel; B-K) · `22` (SC-01: `determine` in the realm; B-N); conjunct (3): an owner per `scales:` row (R-04's table) — IN-46 (SM-6) and IN-47 (the character sheet) are designs that landed at B-C, with no build batch | `aperture 4 0` (`:684`) | not before IN-46's and IN-47's builds have a batch and every `scales:` row has an owner — R-04, hence M1, cannot read `met` until then |
| R-05 | not_met | every verb row it counts, each with its batch, in R-05's table below: B-G · B-I · B-K · B-M · B-N · B-O · B-Q · B-R (with IN-51: `succeed`'s reader, #453 R-5) · B-S; pins re-recorded per step | `corpus_run` `WHERE THE <n> GO` (`:830`); `aperture 4 0` for seat-gated verbs | after B-S and B-R both merged — only if every owner's EXIT recorded ≥ 1 execution, and unless `carry` stops at a Layer 1 amendment (R-05) |
| R-06 | partial | cells commit (IN-08: B-G, `0f998f64`; RANKING under G-1's reading; the doctrine-pair measurement recorded) → H7's standing pair test, H3/H9 (IN-08's chain: B-H, `c13144b9`) → IN-11 (`release` ends an ambition; landed `2a2ed152`) → `13`-rest (IN-38: B-V) | RANKING DISCRIMINATION (`:977`) + H7's pair test + `conviction_spread`'s `within_60deg` | B-V |
| R-07 | partial | telling G1 (IN-18: landed at B-E, `ac9724fc`, live; its realm reader runs: control 0 of 11449 pairs differing, shipped 3270) → `24g` (SE-01: landed `d12c8db9`) → IN-13 (a fought field: B-M) | `:1030` + G1's falsifier + the realm reader | B-M |
| R-08 | partial | cells commit (IN-08: B-G, `0f998f64`, under G-1's reading) → H3/H9 (B-H, `c13144b9`); its `blocks:` W26 → SC-01 (B-N), H-62 → its owners | RANKING + tie ordering (`:1075`) | B-N (the `blocks:` W26; the `met` conjuncts are readable from B-G) |
| R-09 | partial | the selector fixed at B-C (IN-43, landed) → `22` (SC-01: `speak` graded; B-N) → `ED-FI-0009` (FI-01: three inquiries graded, three waiting; B-O) → #453 step 9 (IN-12: `train`, J-13 (iii); B-Q) → `13`-rest (IN-38: `capability` per cast; B-V) | `-k test_we_only_a_verb_that_declares_contests_can_be_graded_today` + `headless` (the `measure:`; the selector became that node id at B-C) | none under v9: measured 2026-10-06, the `headless` world seats no `capability` on any of its three persons, and no position changes that; the by-person conjunct waits on J-13's remainder (`_part5` §J.2) — R-09, hence M1 |

**M1, M2 and W30.** M1's row 3 passes only when all nine rows read `met` (`tools/m1_acceptance.py:320`, `met == len(rows)`), so R-04's conjunct (3) and R-09's by-person conjunct bound M1 exactly as they bound their rows. `corpus_run`'s `ARC ENDS` prints `NOT-COMPUTABLE` naming `W23 (contest results) + W26 (binding decisions) + W30 (the predicates)` (`engine/season/harness/corpus_run.py:676-680`); no row's `met` reads it, and no v9 position makes it computable; M2's bar instrument, STORY-BAR, landed at B-C (IN-19: `harness/storybar.py`) (`workplans/valoria_master_workplan_v9.md` §1, M2).

**What only Jordan can still supply on a row's path:** J-13's remainder, the SOURCE of `capability` beyond the interim (`_part5` §J.2) — R-09's by-person conjunct, hence M1, stays `partial` until it is ruled (J-13 (iii) is the adopted interim, RS-21 item 10; R-09 carries the measurement). One more can come to wait on him: `carry`, on R-05's path, stops and becomes his if its fourth gate `Subject` shape would amend ratified Layer 1 (`_part5` IN-45). Nothing else on a row's path waits on a ruling. **Answered as the plan's recommendation, each [medium; Jordan to correct], revert "Jordan states the other option" (RS-21; `_part5` §J):** H-111 (SKIP at WITNESS: FI-01's deposit half, B-O; the graded inquiries, R-09), `13`-rest (IN-38, B-V: R-06, R-09), #457 D6 (IN-27, B-U), D4 (IN-36 and FA-01's content, B-V), D2 (IN-34, B-F), J-18 (MB-07 landed at B-D2, `b31d2c31`, shipped OFF; the flip is MB-07r), J-20/J-21 (PC-07, landed, `9054df80`), J-13 (iii) (IN-12 step 9, B-Q), and **#453 R-5 (IN-51, B-R), which is ON R-05's critical path**: `succeed` sits in R-05's "no predicate/effect" class, and its one reader, transmission at death, is unbuilt (`engine/season/verb_table.yaml:839`, `decline_note`). H-101 is answered by G-4 (IN-40 revised: no stored parent) [medium; Jordan to correct]; SM-6 has a design owner (IN-46) and needs no ruling. **Still held, on no row's `met` as this part states it:** J-9 (M3 only), J-14, SM-1, the CAST-POPULACE spread construal (SE-04 (c)), `decision_policy_v1.md`'s fork, `godot_conversion_strategy_v1.md`, `2026-09-03-governance-corpus-rebuild/`, A-24 (i), H-89 and H-56's nested half [UNVERIFIED: not traced to a row here], and the ask-then rows (J-15, J-16, J-17, J-19, J-8 per post, SM-15 timing, and the CELL-VALUE AND COSINE PASS, which attaches to R-06's third conjunct without blocking it). J-1 and J-5 are answered (below).

**Read with this, before any section:** THE NINE cannot all be met by building what this plan lists — R-04's conjunct (3) waits on build batches for IN-46 and IN-47, which only their design review can create, R-09's by-person conjunct waits on a ruled `capability` source, and R-05's earliest `met` holds only if every owner's EXIT observed its verbs executing. Both are stated in their sections, not hidden. J-2 is ruled by Jordan (2026-09-18) and J-3 is answered at ladder step 4 (`_part5` §A; J-3 at [medium], with its revert path); J-8 is partly answered [medium] (R-04 below); J-4's interim is H-156's option (b), shipped, and the gaps close by build (IN-11 landed `2a2ed152`; IN-10 in B-I; IN-28 and IN-45 in B-K) [medium]; J-10 closes with J-2 at IN-09 [medium]. What can be built is scheduled in `_part3` §B; B-Z holds only what still waits (the J-9 chain, SC-05/SC-06 as asked, SE-04 (c), the ask-then rows). R-05 turns on IN-45 (B-K) for `forge`, `carry`, `work` and `migrate`: its per-verb STATE builds all four and leaves none at LEAVE (`_part5`), and R-05's `met` cannot read met while any of them stays refused or without an effect.

**Ruled by Jordan, 2026-10-06 (J-1 and J-5 answered; recorded as ruled, nothing added).** On the two drafts `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` and `candidate_affiliation_content.md` — *"so for candidate_*, let's just fold them in to build unless we can find any reason why not to?"* — they are folded into the build as the source of the cells (the 105 projection cells, the alignment re-cell, the doctrine pair, the affiliation roster, the ten `incompatible:` cells, the intensity scale, the verb × affiliation table C4, G-Q6). Folding in also accepts what the drafts ask Jordan to accept: the sign convention (`candidate_pursuit_cells.md` §0.1: negative = the first-named pole), G-Q5 = neither (keep gate-then-score; no `Person.precedence`), the 55 REASONED cells as placed, G-Q6 as the affiliation file recommends. Two build conditions, neither a blocker: the alignment extension to `build`, `found`, `give`, `march`, `migrate`, `survey` (the draft does not cell them; derived from each verb row, graded `reasoned`, each cell showing its reasoning) lands inside IN-08's atomic cells commit, and the doctrine-pair test is pinned at the draft's weights with its margin recorded. **Pursuit names:** `faith` → `doctrine` (*"you can change "faith" to "doctrine""*; the word `faith` in prose or the affiliations is not renamed) and `warden` → `stewardship` (*"sure, stewardship works for warden"*, RULED; the in-world Warden offices, faction, `p_warden` fixtures and `populated.py`'s title rule are unchanged; the five `conviction: Warden` rows of `references/npc_registry.yaml` are converted in the cells commit). Jordan expects the `doctrine` row's cell values to change when he works the cells and cosines (*"when we get to cell values and cosines for the axes*poles stuff, doctrine will change"*): the row lands PROVISIONAL, the doctrine-pair margin is not a blocker, and that pass is a non-blocking ask-then attached to IN-08 (`_part5` §J; IN-08 landed, `c13144b9`), not a rank. IN-08 built as B-G (the atomic cells commit, closed `0f998f64`) and B-H (its serial chain, closed `c13144b9`), ahead of the telling tail in B-E (closed `ac9724fc`); no "J-1" gate remains in this part.

---

## R-01 — "decisions must propagate"  · `met` (since B-I: `engine/season/requirements.yaml` R-01)

**Measured.** `corpus_run` [read 2026-10-02 from `requirements.yaml:197-199`, tree `444a00e1`]: `check R3: 46 of 46 pass` (NPC), `96 of 97` (ARC); planted control
`R3 False -> True` ("the detector works"). The row's `measured:` block opens with those figures; the "22/30 NPC and 34/59 ARC"
it read until then was the 2026-09-10 reading over the 89-case live set (`:199`). **R3 is presence
of the channel, not the behaviour the row asks about.** The behaviour — does a decision change what
follows — is the corpus-scale reconvergence rate. ⚠ **Superseded in part (v8's reading, 2026-10-01):** v8 carried "no rate exists since the corpus grew 89 → 143"
(`wd_collect.py` failed its own `probed` assertion at the first fixture point, `{'none': 21717, 'actor': 21954, 'total': 21897}`); `11-fix` repaired it and `11` re-took the rate (R-02 below).
Both conjuncts of `met` read true at B-I on one tree (`engine/season/requirements.yaml` R-01, the paragraph that sets the status): the failing case NPC-090 flipped at IN-11 (`2a2ed152`), not at IN-50; IN-50 (`5fa6ac16`) landed as the rule that a refused act cites its occasion.
**Realm context, not this row's `measure:`** (read 2026-09-30 from `requirements.yaml:286-294`, tree `c8cc408`, `build_realm(0)`, 4 seasons): 188
cross-actor edges, 77% of act-events with no act antecedent, longest chain 7 across 5 actors; 19 of 46
NPCs in no edge, 10 of them officeholders acting through verbs that never execute in the realm (H-156,
H-163). No committed instrument prints those edge figures.

**What moves it.**

| position — `alias (v9 handle)` | what it changes for R-01 | batch |
|---|---|---|
| `11` (no handle; P-4 passed first, at B-C) | re-produces the number the rows' status rests on: at B-G's close as the control for B-I, then at B-I's and B-M's closes, and at B-N's only if a step moved a reconvergence input (`_part3` O.2 E15) | B-G (taken, `0f998f64`), B-I (taken, `requirements.yaml` R-01), B-M (B-N conditional) |
| IN-50 — landed (`5fa6ac16`) | every refusal in `loop/resolve.py` carries the act's occasion ids; NPC-090 had already flipped at IN-11, so it no longer discriminates the rule (its falsifier test does) | landed (`5fa6ac16`) |
| telling T4–T5 — landed (#449); G1/G2 (IN-18, landed `ac9724fc`) | `tell` names its hearer, contests against them and dedups by origin, so a telling is a cross-person edge to a known person; the regard `score` reads arrived with G1/G2 | landed (`ac9724fc`) |
| IN-10, IN-13 (#453 steps 1, 8); IN-11 (step 2) — landed (`2a2ed152`) | new cross-person edges: `confer`/`establish`/`revoke` formable off a held Record (gated: H-203); `utter` mints the hold `commit` reads (landed); the realm fights a field | B-I, B-M |
| `14` — landed; `exchange` (IN-33) | counterparty verbs (`give`, `oblige`, `exchange`) are cross-person edges by construction (v8 read `give`/`oblige` forming 0 in the realm — re-run `aperture 4 0`); `exchange` still has no effect, and IN-33's EXIT observes it executing; `oblige` becomes formable at IN-10's sub-step | B-I |
| `13d-iii` — landed | the 10 isolated officeholders' governance acts start executing (H-163); the 2026-09-30 count (`requirements.yaml:294`) predates it | landed |
| `17` (landed) + `13`-rest (IN-38; RS-21 item 2 [medium; Jordan to correct]: overlays scaled on the NPC lane only, on the per-case observable) | distinct OUGHTs per case → distinct Q4 questions → more distinct first acts to propagate | B-V |
| J-4 (H-156) — interim: option (b), shipped [medium] | always-refused candidates take 34% of realm scene slots (v8); no decline mechanism is built (declining `commit`'s always-formed Candidate would move R-01/R-02 — H-156 read `release` crowded to 0 of 239 attempts, `hole_register.yaml:3518`); gaps close by build (IN-11 landed `2a2ed152`; IN-10 in B-I; IN-28, IN-45 in B-K); revert path `_part5` §A | — |

**No position owned until now:** none (IN-50 landed, `5fa6ac16`). The instrument repair (`11-fix`) landed 2026-10-01. **H-116** (the consequence→decision
edge is severed by a type mismatch — `belief_contradicts` narrows only on `PERSON_PREDICATES`) and
**H-111** (does a refusal propagate as news?) are in the row's `blocks:`; neither is a position — both are holes, not work (H-116 fires only at ≥ 96 %, read 77 % at v8; H-111 is answered as the plan's recommendation, RS-21 item 1 [medium; Jordan to correct]: SKIP at WITNESS, built by FI-01 in B-O).
H-116 is `measured`; whether widening `PERSON_PREDICATES` is a fix or a design call is not
settled by the tree → carried as the post-measurement step of `11` (`_part3` O.2 E15: the re-takes at B-I's and B-M's closes): **if `11`'s number is ≥ 96%,
the first closed channel to name is H-116's**, because it is the registered reason a deposited
consequence cannot narrow a later candidate set.

**`blocks:` (`requirements.yaml:377`), traced id by id.** `W-F` — **spent**: it is "Interior consequence: outcome → `Person.stance` (`H-62`)" (`proposals/2026-09-04-degree-sweep/EXECUTION_PLAN.md:87`), superseded by A-12 and the telling workplan's G1 (`_part5` §A; IN-18): regard is computed at read and `tell` writes no stance; the cross-person half R-01 needs is IN-10's and IN-13's (IN-11's landed, `2a2ed152`). `H-111` — FI-01's deposit half (B-O; RS-21 item 1). `H-116` — no handle: named first if a `11` re-take reads ≥ 96 % (§11's FALSIFIER). The record edit that re-points every spent id in THE NINE's `blocks:` lists to its successor or removes it landed at B-C (IN-43): each list names v9 handles, the spent ids in a comment line.

**Design questions the tree does not answer.** (i) Whether R-01's `met` should also require a realm
reading (the isolated-officeholder set) — the row's `measure:` runs the corpus only. Answered here at
ladder step 5 (architecture): **no** — the row is measured where its `measure:` says; the realm is
context, and building an edge instrument is warranted only if a falsifier needs it. (ii) H-111 (should a failed attempt be news?) is answered as the plan's recommendation (RS-21 item 1, [medium; Jordan to correct]; revert: Jordan states the other option): SKIP at WITNESS except keyed kinds a verb declares (`news.untold` stays), so a refused inquiry deposits nothing; FI-01 builds it in B-O. It was FI-01's question and the graded inquiries', never R-01's gate; it stays a registered hole here until FI-01 closes it.

**`met` =** `corpus_run` prints `check R3: n of n pass` on both lanes with the planted control
`False -> True`, **and** `wd_collect.py` (repaired at `11-fix`) prints reconvergence **< 96 % at `2x3`** with
the `none ≥ default` control printed and the completeness assertion covering all 143 cases. Both in one
`measured:` paragraph, same tree.

⚠ **Annotation — the `met` above is verbatim:** the status reads `met` at B-I by it, both conjuncts on one tree (`engine/season/requirements.yaml` R-01); B-M's `11` re-take is the first after every position on the path has landed, and is read against B-I's.

---

## R-02 — "decisions affect subsequent decisions"  · `met`

**Measured (`11-fix` + `11`; read from `engine/season/requirements.yaml:324` and `:489-500`).** At `2x3` over 143 cases a decision's deposit changes a later decision: reconvergence is
none 77.13 % · actor 43.03 % · total 38.47 % (run (i), v8's 2026-10-01 reading) and none 77.22 % · actor 42.59 % · total 38.58 % (run (ii), 2026-10-02, tree `8b03e518`, across `14`, `13d-iii`, `17-cast`), against a 96 % bar, with the `none ≥ actor` control printed and every arm covering all 143 cases
(`runs/WD_LOG.txt`, tracked). `requirements.yaml`'s dated paragraphs label each figure as committed log, derived cells (untracked) or scratch,
and its comparator and plant controls are described there. The `11` re-take re-checks it at the closes `_part3` O.2 E15 names.

**What moves it.** Exactly what moves R-01's behavioural half: the `11` re-take (no handle) measures it; telling T3a–T5 (landed, #449),
`14`, `17`, `13d-iii` (landed) changed what it measures, IN-11 did (`2a2ed152`), and IN-10 (B-I) and IN-13 (B-M) will; IN-08's re-scored chooser (B-G) may too, which is why B-G's close takes the control re-take. The channel a decision reaches a later decision through
is a ledger claim read by §F1 clause 4 (`belief_contradicts`), which reached five predicates after
ED-FI-0009; H-116's type mismatch is the registered limit on it.

**No position owned until now:** none. (`11-fix` landed; R-02's `measure:` comment was re-pointed off the retired plan.)

**`blocks:` (`requirements.yaml:505`), traced.** `W-F` — spent (R-01's trace: superseded by A-12 / IN-18 G1). `H-111` — FI-01's deposit half (B-O; RS-21 item 1 [medium; Jordan to correct]). Neither is on R-02's `met`; IN-43's re-point (landed at B-C) covered this list.

**Design question the tree does not answer.** Whether the `probed` divergence across deposit modes is
a defect in the instrument or a property of the loop. The row's own diagnosis (a deposit under
`actor`/`total` raises a new Q2 question in a later round that `none` never raises — R-03's channel
working) points to **property**, and `11-fix` took that reading: report `probed` per arm, compute the
rate per arm, stop asserting equality. **Attack at `11-fix`:** if `probed` differs between two runs of
the SAME arm, it is a determinism defect, not a property — then stop, register, and do not compute a
rate.

**`met` =** `python proposals/2026-09-04-degree-sweep/wd_collect.py`, after `wd_chunk.py` ×4 slices ×3
arms ×3 fixture points over all 143 cases, prints reconvergence **< 96 % at `2x3`**, with `none ≥
default` printed. ≥ 96 % ⇒ the row stays `not_met` and the commit names which channel is closed.

---

## R-03 — "seasons must tick scene-by-scene, so what occurs after one scene can impact the next scene"  · `met`

**Measured.** Met 2026-09-11 by U2, on an execution:
`test_u2_a_deposit_in_one_round_changes_a_later_rounds_candidate_set_in_the_same_season`. The control is
the `scene_budget = 1` arm. The `measured:` block also holds a fresh re-run of the row's own `measure:` (read 2026-10-02 from `requirements.yaml:576-593`, tree `444a00e1`: `headless --case NPC-088 --seasons 2 --seed 0` exit 0, `-k test_u2_` `5 passed`); the corpus grew 89 → 143
and the verb table 32 → 44 since the 2026-09-11 reading.

**What keeps it met.** Nothing builds on it; every position that touches the rounds loop
(`loop/driver.py`, `loop/deliberate.py` — IN-29 (landed `4a2e4494`) edits `driver.py` and PC-06 S-1 (landed in B-E, `ac9724fc`, `harness/play_surface.py`) calls it, `_part3` §C; IN-27 (B-U) adds an ending step to it) must keep `pytest engine/season/tests -q -k test_u2_` green, read at each of those batches' exits.
The `measured:` refresh v8 owed is done (the 2026-10-02 re-run above); a later one is one re-run of the row's own `measure:` command,
dated, changing nothing else.

**`blocks:` (`requirements.yaml:595`), traced.** `W17` — **spent**: the scene container LANDED (`requirements.yaml:517`); removed from this row's list at B-C (IN-43's re-point, landed).

**`met` (holds) =** `python -m pytest engine/season/tests -q -k test_u2_` passes, and
`python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` runs.

---

## R-04 — "strategic and management actions must be possible, ie decisions at differing scales"  · `partial`

**Measured.** The row's `measure:` line names `aperture 4 0` (`requirements.yaml:684`, read 2026-10-06); `corpus_run` prints no `unrepresentable scales:`
line at all since `20-ii` (all 143 cases run at four rung kinds, `:627`). The row stays `partial` on its own two
stated reasons:
1. **Seat-based acts do not execute.** `aperture 4 0` [read 2026-10-02 from `requirements.yaml:670-675`, tree `23bea9da`, realm, seed 0, 4 seasons, att/ex]: `levy` 23 attempted, 0 executed,
   refused 19 `levy.refused` + 4 `levy.unauthorized` (v8 read H-163 limit 1 — seats without a rung — as the cause; `13d-iii` has since anchored 29 of 30 seats, `:485`, and the conjunct a `levy` refusal now fails on is not read, `:677-679`).
   `open_case` 28/7, `issue` 30/6, `determine` 20/1, `convene` 12/2, `dispatch` 86/16. `confer` 70/0,
   `establish` 19/0, `revoke` 15/0 — a different cause: no computed act names an office (H-94, v8's reading).
2. **No Domain-Action mechanism, and no `Faction`-as-actor.** The row's reason as it reads now
   (`requirements.yaml:645-655`): its first half, `engine/mc_v18.py` running a faction scale the loop did
   not join, ended when `28-iii` deleted it (PR #450); what it still says is *"no Domain-Action mechanism
   exists in `engine/season/`, and no `Faction`-as-actor either (by design, not by omission: a faction
   never acts)"*, and no instrument counts it (`:680-681`). ⚠ **The `Faction`-as-actor half is Layer 1,
   not a gap:** `04_CODE_ARCHITECTURE.md` (RATIFIED) gives `Faction` a resolved view (`faction_q.resolve`)
   with **"no verbs"** and *"NEVER … `Act.actor` · a `contest` claimant"* — a faction acts as its members
   acting through seats (`Act.via`) (`_part5` §A, A-4). **The Domain-Action half is answered by the
   architecture, not by a mechanism of its own** [medium; Jordan to correct; revert: Jordan states the
   other option, a Domain-Action mechanism]: #453 §10.2 maps every entry of
   `references/action_vocabulary.yaml` onto a seat-holder's act or members' acts counted by a Query, and
   no entry needs a faction to act (FA-03, `_part7`, which is why `ED-FA-0002`'s `domain_actions` home
   document is cut; the contract row still reads `doc: null`, `references/module_contracts.yaml:576-579`).
   A domain action is therefore a seated person's verb `via` the seat — built by IN-10, IN-12's steps,
   IN-28, IN-45 and IN-49 — and what reads it is conjunct (1)'s `via` lines and the settlement row's
   `in_loop` flip in the table below.

**`march` — two readings disagree [UNVERIFIED].** The row's own `measured:` block (`engine/season/requirements.yaml:675`) carries the realm aperture line `march` **16/16** (att/ex; "its `both` column is a two-Event convention, so not a split"), from the orchestrator's run on tree `23bea9da` (2026-10-02; not re-run there); R-07's own paragraph (`:1022`, 2026-10-01) and the scales table below read 11 declared, 11 refused at ENCOUNTER (H-149's target-kind check). Neither was re-run for v9 (`aperture 4 0` takes about 25 minutes). R-07's third conjunct and IN-13 turn on which holds; the instrument is `aperture 4 0` itself.

**The seven scales of `requirements.yaml` `scales:` (`:70-189`; Jordan's roster, the settlement row added on his 2026-09-05 correction), read against the tree.** R-04 is measured
against this roster (the file says so); this is the strategic half of "decisions at differing scales". Conjunct (3) reads each row's `in_loop:` field, quoted below as it stands (re-read 2026-10-06), so each row needs the position whose EXIT supplies the execution artifact and whose close owes the record edit that flips the field [medium; Jordan to correct; revert: Jordan states the other option]. **Conjunct (3) is unmet until every row has such an owner; two rows have none today.**

| scale | `in_loop:` today | what expresses it in `engine/season` | the position that flips it (batch) | contributors · named residue |
|---|---|---|---|---|
| character creation / development / chronicling | `false` (`:74`) | `Person` carries the fields; nothing creates or develops a person | **none — named residue:** IN-47's build has no batch (its design, the character-sheet management space, landed at B-C) | `13`-rest (IN-38; B-V) + `17` (landed: a cast per case); `24g` P3 individuation (SE-01; landed `d12c8db9`); `train` (IN-12 step 9; B-Q). **No spec in code for creation or development** → IN-47's design (J-11 answered in part, A-25) |
| grand strategy politics | `false` (`:86`) | `faction_q` reads; seat acts `via` offices at realm/duchy rungs | FA-01 mechanism (B-J): a faction head's act executes `via` its seat in `aperture 4 0` | `13d-iii` (landed); IN-10 (B-I: the `office` operand, J-3 answered (ii)); IN-40 revised (B-J); IN-36 and FA-01's content (B-V) |
| social contests / debates | `"seam unbuilt"` (`:102`) | `tell` graded through σ-leverage; proceedings (`speak`, `determine`) not yet graded | SC-01 (B-N): THE BAR — two seeded proceedings resolved through the proceedings provider, twice byte-identical | `22a` → `23` → `22b` (SC-02; B-P); `2-ii` (SC-05: asked at B-N, held in B-Z) |
| mass battles / strategy warfare | `"seam built; reached via a constructed Question … AND, measured, via natural computed play in build_realm(0)/populated.run …; not yet reached naturally in corpus_run's separate 143-case NPC/ARC corpus"` (`:117-119`) | `march` → `seam/wrappers/mass_battle.py`; realm: 11 declared, 11 refused at ENCOUNTER, 0 fought (read 2026-10-01 from `requirements.yaml:1022`; [UNVERIFIED] — the `march` note) | IN-13 (B-M): the realm fights ≥ 1 field | `20-iv` (PR #450), `20-v` (PR #451) landed; ENCOUNTER's refusal is H-149's target-kind check (P-5). **Named residue:** the corpus half — why `corpus_run`'s 143 cases never give `march` a referent (H-175) — has no position that moves it; P-6 read it at B-C (IN-39, landed; H-175's `cite:`) |
| personal combat / grid-based map combat with units | `"duel only, via combat_seam.py"` (`:145`) | `fight` → `combat_seam` | **none — named residue:** IN-46's build has no batch (its design, the grid mode's suspension at ENCOUNTER's barrier, SM-6, landed at B-C) | `8` (landed), `9` (PC-01, landed, `9054df80`). **Grid-based unit combat does not exist anywhere in the tree** (`requirements.yaml` says so) → SM-5 CONFIRMED by Jordan's words (the grid version and the duel version are two modes of one engine; see the annotation below the `met`) |
| settlement management / city building / domain actions | `false` (`:158`) | `found`/`build`/`work`/`restore` (24e), cohorts (24f), `migrate` (19c) — realm: only `restore` executes (19) | IN-07 (= SE-02; B-T): the settlements module re-plugged, read after `found`, `build`, `work`, `migrate` and `levy` execute in B-K | IN-45 (`work` channel first, then `migrate`: H-165, H-168), IN-28 (`found`, `build`: H-166) and IN-49 (`levy`) (B-K); `24h` P5 (IN-30; B-U); SE-04 (a)(b) (B-T); J-4 (H-156) — interim option (b), shipped. The Domain-Action half: reason (2) above |
| investigations / detective / interactive fiction | `false` (`:173`) | six inquiry rows; degrees Failure/none only — "UNGRADEABLE" (the row's note) | FI-01 (B-O): three graded — `research`, `examine`, `surveil`'s place case | **Named residue:** three wait — `interview` (a prompt, not graded by design), `reconstruct` (a value space nothing supplies), `thread_read` (PC-06 K-3's operand, B-S) — and `surveil`'s Person case; FI-03 (B-S). Ruled: the loop is the mechanism; investigation is not made a contest |

**What moves it.**

| position — `alias (v9 handle)` | what it changes | batch |
|---|---|---|
| `13d-iii` — landed | every seat gets a rung anchor (`populated.resolve_anchor`) → `levy`/`issue`/`open_case` pass `authority`; `determine`'s bench resolves; the 2026-10-02 run above (`:670-675`) is after it and `levy` still executes 0 | landed |
| `28-iii` (+ `29b`) — landed (PR #450) | `mc_v18` and its faction scale are gone; "not joined" stopped being true by deletion | landed |
| `20-iv` — landed (PR #450) | a garrisoned defender changes a field's outcome (a constructed test); the realm still fights no field — ENCOUNTER's refusal is H-149's target-kind check (P-5), not a garrison/defender gap | landed |
| `20-v` — landed (PR #451) | H-150's walls bonus is a swept Fixtures value (`field_walls_dr`, sweep 3 / 0 / 1), so its `assumption` grade carries a sweep; no `arms.py` arm sweeps it, and one run through the realm would be a fake control (H-149) | landed |
| `22` (SC-01) | `determine` reaches a decision in the realm (THE BAR) | B-N |
| IN-10 (#453 step 1; J-3 answered (ii)) | `confer`/`establish`/`revoke` become formable from computed play, off a held writ/commission Record; sub-steps: `oblige` formable from a held Record's `terms` (#453 `:524`), and `confer` + `Tenure.term` (regency: a termed seat-hold opens and matures) | B-I |
| IN-49 (`levy`; H-163 limit 3) | a question source whose referent is a full larder in purview, so `levy` — conjunct (1)'s first-named verb, 23 attempted and 0 executed in the realm (2026-10-02) — has something to levy; it needs IN-10's second operand channel, which #453 names as the gate on `levy`'s limit 3 (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:546-547`), and it edits the always-refused pin, so it lands with the refused verbs [medium; Jordan to correct] | B-K |
| IN-40, revised (H-101; G-4 [medium; Jordan to correct]; revert: Jordan prefers a stored parent) | no stored `superior:`; "under" is derived — rung containment within a faction ("rung above of same faction", descendants only: RS-9) plus a seat-holder's own `oblige` to another seat for cross-faction subordination (#453 §7.2's vassalage), read by an oblige-edge clause in `purview_reaches`; the Ehrenwall Split in a seeded season | B-J |
| FA-01 mechanism; FA-01 content with IN-36 | a faction head's act carries `Act.via` its seat (the mechanism); one foreign faction with two seats and the Schoenland trade-demand clause (the content, RS-21 item 4 [medium; Jordan to correct]) | B-J; B-V |
| IN-46, IN-47 (designs) | the two `scales:` rows that want a spec before anything can be built (conjunct (3)): the grid mode's suspension (SM-6; the row reads `duel only`) and the character-sheet management space (`in_loop: false`); design only — each needs a build position, which only its design review can schedule | designs landed at B-C; reviews B-L (IN-46), B-H (IN-47, `c13144b9`); build: none |
| J-8 — partly answered [medium] | Jordan rejected deleting `dispatch` (2026-09-18) and said of the remit "for testing purposes for now, just build out a generic remit": the delete arm is out, `dispatch` stays in the generic remit (`rosters.yaml: remit_default`), and IN-12 steps 5, 5a, 8, 11 build on it; per-post naming is deferred until posts are authored (ask-then; revert: Jordan names the posts) | — |

**No position owned until now:** `13d-iii` (H-163 limit 1 — the row's own named cause; landed); the H-175
measurement (why `corpus_run`'s 143 cases never give `march` a referent while the realm does) — read at B-C
(IN-39's P-6, landed; H-175's `cite:` holds the reading), a read, not a build; `levy`'s referent (H-163 limit 3, `hole_register.yaml:3612`) — IN-49 (`_part5`; B-K); the two specs conjunct (3) waits on — IN-46 (SM-6) and IN-47 (`_part4`; designs landed at B-C).

**Design questions the tree does not answer.** The spec of two of the seven scales — grid-based unit combat (SM-6: its suspension at ENCOUNTER's barrier) and character creation/development/chronicling — has no mechanism in code (the only grid references are quarantined UI documents, reference only). Both are design positions now, IN-46 and IN-47, and neither needs a Jordan ruling: SM-5 is CONFIRMED by his words (below) and J-11 is answered in part (A-25: both scales are in scope — grid combat as the `combat` container's playable mode, character creation as the character-sheet management space). **J-3 is answered**
(ladder step 4 (ii) [medium]: IN-10); **J-8 is partly answered** (the row above).
**R-04, hence M1, cannot read `met` under v9 until a build batch exists for both IN-46 and IN-47** — their designs landed at B-C, and their build positions are scheduled only by the review of those designs (`_part3` §B.0 places them then); until that review, no batch builds either scale, and those two `scales:` rows are the ones with no owner in the table above.

**`met` =** (1) `python -m engine.season.harness.aperture 4 0` shows every seat-gated remit verb
(`levy`, `issue`, `open_case`, `determine`, `convene`, `dispatch`, and — after J-3 — `confer`,
`establish`, `revoke`) executing ≥ 1 with `Act.via` set; (2) `engine/mc_v18.py` absent (true since PR #450) and
`test_faction_q.py` green; (3) every `scales:` row in `requirements.yaml` reads `in_loop` with an
execution artifact named. ⚠ **Record edit owed** (`21`-rest, after `13d-iii`): R-04's `measure:` must
name the instrument that reads reasons (1)–(2) — `aperture 4 0`'s per-verb lines — since
`corpus_run`'s line no longer discriminates. Conjunct (3) cannot be met until J-11.

⚠ **Annotation — the `met` above is verbatim:** J-3 is answered (IN-10); the record edit it names is done (`requirements.yaml:684`'s `measure:` names `aperture 4 0`'s per-verb lines, read 2026-10-06); conjunct (3) is unchanged, and SM-5 is now CONFIRMED by Jordan's own words (RS-6; `proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md:8-11`): *"I want there to be a grid map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my personal combat engine resolving there for a round — and then a duel version where you actually decide at each step/beat"* — so grid combat is a **mode** of one combat engine with no second resolver, not an `[ASSUMPTION]`; the spec is still owed — SM-6, the suspension design, is IN-46's (landed at B-C), and the character-sheet space is IN-47's (landed at B-C) — and conjunct (3) waits on both builds having a batch and on every other row's owner in the scales table (J-11's residual). Conjunct (1)'s nine verbs and their batches: `confer`, `establish`, `revoke` B-I (IN-10); `levy` B-K (IN-49); `determine` B-N (SC-01); `issue` (30/6 with `Act.via`), `open_case` (28/7), `convene` (12/2), `dispatch` (86/16) already execute in the realm (`requirements.yaml:670-675`, 2026-10-02; `via` read for `issue` only, `:828`). Conjunct (1) is first readable after B-N.

**`blocks:` (`requirements.yaml:685`), traced.** `W10` — **spent**: declared routing for the 143 cases (`architecture/PLAN.md:1064`) carries a LANDED note (`architecture/PLAN.md:1315`). `W13` — the ARC re-authoring lane (`architecture/PLAN.md:1171`): no v9 handle, and none of R-04's three conjuncts reads it (they read `aperture 4 0`, `test_faction_q.py` and the `scales:` rows) — removed from this row's list at B-C (IN-43's re-point, landed).

---

## R-05 — "all verbs must be built out, and doing so requires planning out all the different scales of play required in a season"  · `not_met`

**Measured.** `corpus_run` [read 2026-10-02 from `engine/season/requirements.yaml:813-820`, tree `23bea9da`]: `WHERE THE 44 GO: 10 have no predicate/effect · 10 foldable but never
even attempted · 7 attempted and always refused · 17 executed`; `dispatch` moved from always-refused to never-attempted, `give` joined the executed set (v8's 2026-10-01 reading was 8 / 16). The second clause ("planning out all
the different scales") is answered by Jordan's `scales:` roster (R-04's table above). Re-read at B-I: 21 of 45 executed (`engine/season/requirements.yaml` R-05, the B-I paragraph); IN-09's and IN-10's verb families are still at 0 (H-203).

**Every verb row R-05 counts that does not yet execute, the rows positions add, the position that owns each, and the batch that moves it.** This is the R-05 build plan. The table holds 44 rows at HEAD (`len(VERB_TABLE)` via `engine.season.data.verbs._load_verb_table()`, re-run 2026-10-06; no `challenge` or `accept` row, only the comment at `verb_table.yaml:448`). Every owner's EXIT is "executes ≥ 1 in computed play (`aperture 4 0` or `corpus_run`)" for its verbs, beside any `w.log` observation, and every step that adds, cuts or moves a verb re-records the pins. **An EXIT that records 0 does not invent a position** [medium; Jordan to correct]: the verb is named as a residue in that batch's HANDOFF line, R-05 stays unmet, and the next batch whose exit re-reads `WHERE THE <n> GO` reads it again.

| verb(s) | corpus class (2026-10-02) | realm (`aperture 4 0`, att/ex — read 2026-10-02 from `requirements.yaml:670-677` unless marked) | why it does not execute | owner | batch |
|---|---|---|---|---|---|
| `challenge`, `accept` (rows IN-08 adds) | — | — | the `duel` is `challenge` → `accept` (resting on a short reply, RS-18: tagged [medium; Jordan to correct]); they arrive with the cells commit's verb split. `kill` and `wound` are not verbs: the split of `fight` is closed (Jordan, 2026-09-27, `engine/season/verb_table.yaml:442-448`: *"a character can only attempt to kill or wound, never choose the outcome directly"*; the same day, event ea741a6c-7194-4564-9f6c-cce425b2fa3b: *"Kill/wound is the output from a duel/personal combat having been called"*; and 2026-10-03, #453 §13.9, adopted) | IN-08 adds exactly these two rows (44 → 46); its EXIT: each executes ≥ 1 in `aperture 4 0` or `corpus_run` at B-H's exit (executed, `c13144b9`) — #453 answered the duel without a new verb (K-23, a challenge as `petition` + `fight`, `proposals/2026-10-03-verb-coverage-and-gap-fill.md:242-244`), which IN-08 strikes, so no other position makes the pair execute and the realm's chooser is their occasion; a row that records 0 is a named residue, re-read at B-I's exit | landed (`0f998f64`; read at B-H, `c13144b9`) |
| `comply`, `evade / defy` | no predicate/effect | never attempted | the Dispensation operand (H-94); H-44, "the NINE Dispensation term types enumerated nowhere" (`hole_register.yaml:500`) | `19b` (IN-09) ← J-2 answered (A); IN-09's EXIT observes each executing. If `evade / defy` splits when built (#453 K-24), `<n>` moves by one and both rows count | B-I |
| `construe` | no predicate/effect | never attempted | WITNESS-side in #453 (`:504`); built as an act by IN-09 so the row can execute | IN-09 — counted as stated below the table | B-I |
| `confer`, `establish`, `revoke` | foldable, never attempted | 70/0 · 19/0 · 15/0 | no computed act names an office (H-94, v8's reading) | IN-10 (J-3 answered (ii)); its sub-step `confer` + `Tenure.term` (regency) | B-I |
| `oblige` | foldable, never attempted | formed 0 (read at v8, 2026-10-01; re-run) | needs a seat referent; `14` (landed) gave each slot its own operand | IN-10's sub-step: formable from a held Record's `terms` (#453 `:524`, type clause 1), EXIT `oblige` executes ≥ 1; IN-18 G5 and IN-40's oblige-edge clause wait on it | B-I |
| `commit` | always refused | 0/154 (read at v8, 2026-10-01) | its own operand gap; crowds `release` (H-156) | IN-11 (#453 step 2) — landed (`2a2ed152`): `commit` executes and left the always-refused pin; H-156's interim is option (b), shipped | landed (`2a2ed152`) |
| `exchange` | no predicate/effect | never attempted | the counterparty's side of a trade (H-58, H-94) | IN-33 — its EXIT observes `exchange` executing, not merely forming | B-I |
| `repudiate` | no predicate/effect | never attempted | unbuilt (W31(a)) | cut (#453 R-3(b); IN-11, landed `2a2ed152`): the row left the table | landed (`2a2ed152`) |
| `forge`, `carry` | no predicate/effect | never attempted | `forge`: `14` declined its effect (H-169 (2), `verb_table.yaml:315`); `carry`: writes a docket item, has no effect (H-63, `verb_table.yaml:121`) | IN-45: `forge` with its sheet consumer first (H-169 limit 5); `carry` needs a fourth gate `Subject` shape, which may amend ratified Layer 1 — then it stops and is Jordan's | B-K |
| `work`, `migrate` | always refused | 183/0 · 137/0 | `work`: no computed act declares a works (H-165 limits 2–3); `migrate`: capacity/travel refusals (H-168) | IN-45: the `work` channel first, then `migrate` | B-K |
| `found`, `build` | always refused | 70/0 · 65/0 | no computed act declares a works (H-165 limits 2–3) | IN-28 (H-166), after IN-45's `work` channel lifts the cause (the channel first) | B-K |
| `levy` | always refused | 23 attempted, 0 executed (4 `levy.unauthorized`) | the conjunct it fails on is not read (`:677-679`); H-163 limit 3: the levied rung is "usually no rung or an empty larder" (`hole_register.yaml:3612`) | IN-49: a question source whose referent is a full larder in purview (design, then build), after IN-10's second operand channel, which #453 names as limit 3's gate (`:546-547`) | B-K |
| `survey` | always refused | 165/10 | referent | executes in the realm (the aperture clause of `met`); IN-12's sub-step `survey` + Rung with the sheet consumer (H-169 limit 6, #453 `:2074`) | B-K |
| `seize` (row IN-12 step 6 adds); `march` | — ; foldable, never attempted | — ; 16/16 (`:675`) against "declared 11, refused at ENCOUNTER 11" (`:1022`, 2026-10-01) [UNVERIFIED — R-04's `march` note] | `march`: corpus: no referent (H-175); realm: ENCOUNTER refusal — read at P-5: H-149's target-kind check refuses all 11 | IN-12 step 6 (`seize` over a warrant Record), IN-13 (the arrival; widens `seize` to Rung); P-6 read H-175 at B-C (IN-39, landed) (`20-iv` landed without changing H-149's check) | B-M |
| `determine` | foldable, never attempted | 20/1 | referent coincidence + quorum (H-163 limits 2–4, H-161) | `13d-iii` (landed: bench), `22` steps 11–12 (SC-01); contested: SC-03b (B-O) | B-N |
| `open_case`, `convene` | foldable, never attempted | 28/7 · 12/2 | few corpus seats; a fired slot no act fills | execute in the realm (the aperture clause); `open_case`'s docket item: SC-03a (#453 step 2b; B-J); the fired-slot → `convene` step and H-163 limit 2's question source: SC-01 | B-N |
| `dispatch` | foldable, never attempted (moved from always-refused) | 86/16 | rare in the corpus; seats | executes in the realm (the aperture clause); `13d-iii`, `17` (landed); J-8 partly answered [medium]: `dispatch` stays in the generic remit, per-post naming deferred | — (executes) |
| `examine`, `interview`, `research`, `surveil`, `reconstruct` | executed | — | graded Failure/none only (R-09) — R-05's `met` line does not read grading | FI-01: three graded (`research`, `examine`, `surveil`'s place case); three wait — `interview` (a prompt, not graded by design), `reconstruct` (a value space nothing supplies), `thread_read` (PC-06 K-3, B-S) — and `surveil`'s Person case waits; its deposit half built as SKIP at WITNESS (RS-21 item 1 [medium; Jordan to correct]) | B-O |
| `destroy_record` | foldable, never attempted | never attempted | `eligibility: hold:<record>` + presence — unformable for everyone | IN-26 (A-13; the held shape decided there); its EXIT observes `destroy_record` executing | B-Q |
| `covenant`, `conceal`, `forgive`; `sabotage`, `tend`, `argue`, `train` (rows IN-12 steps 7, 10, 13 and 9 add) | — | — | — | IN-12 steps 7, 10, 13; step 9 under J-13 (iii) (RS-21 item 10 [medium; Jordan to correct]): `train` writes `Person.capability` only where a case names a vocation — of the corpus, NPC-088's case text names the one vocation `verb_capability` covers (`copying`, `engine/season/cases/exercises/NPC-088.yaml:20-22`) and NPC-002's names one it does not (`NPC-002.yaml:15-16`; grep 2026-10-06), so `train` may form in one case or none. `forgive` needs a negative stance row toward its referent: the build-time loyalty seed gives one below indifference (`engine/season/data/cast.py:328-342`) and `_eff_march`'s losing-side write gives one once the realm fights a field (B-M) [UNVERIFIED: whether either is a referent `forgive` can name; `_part5` IN-12 step 13 states it]. Either verb at 0 on B-Q's exit is a named residue | B-Q |
| `arrest`, `pardon`, `interrogate`, `raze` (rows IN-12 steps 5, 11 add); `give` | — ; `give` executed (one corpus world; refused in 63, H-84) | — ; `give` formed 0 (read at v8, 2026-10-01; re-run) | — | IN-12 steps 5, 5a, 11; IN-12's sub-step `give` + Rung (cession, #453 `:2072`), after the arrival | B-R |
| `succeed` | no predicate/effect | never attempted | its one reader, transmission at death, is unbuilt (`verb_table.yaml:839`, `decline_note`); no heir operand | IN-51 (#453 R-5 (b), RS-21 item 9 [medium; Jordan to correct]): `inheritance` as a fourth conferral basis read by CENSUS at `person.died`, after IN-12; its EXIT observes `succeed` executing at a death | B-R |
| `tie / knot`, `thread_read` | no predicate/effect | never attempted | `tie / knot`: the missing partner operand, and `knot` is `29f`'s knots work (`requirements.yaml:821-826`, H-182); `thread_read`: Thread Sensitivity has no operand in the closed eight (H-85) | `tie / knot`: IN-32 (= FI-05); `thread_read`: `R05-THREAD` (answered A-7), the typed operand PC-06 K-3 (both after IN-06's build) | B-S |

**How R-05 counts `construe`.** `WHERE THE <n> GO` prints `len(VERB_TABLE)` (`requirements.yaml:830`), so it counts `construe`; #453 `:504` reads it as WITNESS-side, not an act — the content deposit already reads per holder — which would leave the row in "no predicate/effect" for good, since a row nobody can attempt never executes. **The plan's reading [medium; Jordan to correct]:** IN-09 builds `construe` as an act whose one effect is the construer's own reading of a writ they hold, the per-holder deposit #453 places at WITNESS reached by choice (`_part5` IN-09), because Jordan kept it as a verb (J-2) and R-05's `met` is instrument-defined. R-05's `met` line is this part's own — `requirements.yaml` carries no `met` text — so no record edit is owed. Revert: Jordan states `construe` is witness-side only; this part's R-05 `met` then counts the row by its witness observable (two holders of one writ holding different `content:dispensation` values, #453 `:504`), or the row is cut.

**No position owned until now:** `R05-THREAD`; the `found`/`build`/`work` works channel (H-165 limit
2); `destroy_record`'s formability — all three placed at `14` (landed) as decisions taken at ladder step 4 or 5, or declined with the reason recorded; what remains is re-keyed in the table. `levy`'s referent (IN-49), `succeed`'s reader (IN-51) and `oblige`'s formability (IN-10's sub-step) had no owner before v9, and no owner's EXIT observed its verbs executing.
**IN-45 (`_part5`, B-K) carries four verbs R-05's `met` needs at zero** — `forge`, `carry`, `work`, `migrate` — and its per-verb STATE builds all four, none at LEAVE.

**Earliest R-05 `met`: after B-S and B-R both merged** (`_part3` §B: B-R, then B-S) — **conditional** [medium; Jordan to correct]: only if every owner's EXIT above recorded ≥ 1 execution in computed play (`aperture 4 0` or `corpus_run`), and unless `carry` stops at its fourth gate `Subject` shape because that shape would amend ratified Layer 1 (then it is Jordan's). A verb whose EXIT recorded 0 stays a named residue in its batch's HANDOFF line, R-05 stays unmet, and no position is invented to fix it. `succeed` (IN-51, B-R) and `tie / knot` and `thread_read` (B-S) are the last to move, so #453 R-5 is on this row's critical path.

**`blocks:` (`requirements.yaml:831`), traced.** `W10-core` — no v9 handle: it authors the core `exercises:` rows for the NPC lane (`architecture/PLAN.md:1729-1735`; 72 files under `engine/season/cases/exercises/`, counted 2026-10-06) and gates `corpus_run`'s `R2` check (`harness/corpus_run.py:677`), not R-05's `WHERE THE <n> GO` — removed from this row's list at B-C (IN-43's re-point, landed). `H-65` (typed `requires:` cells per verb, `assumption`) — the per-verb owners above; each typed row is its progress. `H-94` (the person-side operand vocabulary) — IN-10 (the `office` operand off a held Record), IN-09 (the Dispensation operand), IN-45 (`migrate`'s destination channel), IN-33 (the counterparty's side).

**Design question the tree does not answer.** Whether "built out" means *executes in computed play*
(DONE-realm) or *a dedicated test executes it* (DONE-test). R-05's `measure:` is `corpus_run`'s executed
set, and U7's own acceptance said **"≥ 1 world — in the corpus, not merely in a hand-built `Act`"** — so
the tree already answers it (ladder step 4, U7's precedent): **computed play**. This plan adopts that.

**`met` =** `corpus_run`'s `WHERE THE <n> GO` line reads `0 have no predicate/effect · 0 foldable but
never even attempted · 0 attempted and always refused`, **or** every verb in the latter two classes is
shown executing ≥ 1 in `aperture 4 0` (seat-gated verbs the corpus does not seat), with the verb named.
After J-1 the table holds `kill`/`wound`/`challenge`/`accept`; `<n>` moves and the line must still read
zeros. ⚠ **Annotation — the `met` above is unchanged:** after IN-08 the table holds `challenge` and `accept` only — `kill` and `wound` are not verbs (the row above), so IN-08 moves `<n>` by two, not four (44 → 46); IN-11's cut of `repudiate` (`2a2ed152`, 46 → 45) and the twelve rows IN-12's steps add move it again, and the line must still read zeros — with `construe` counted as "How R-05 counts `construe`" above states. It needs `forge`, `carry`, `work` and `migrate` out of the first and third classes, and IN-45 (`_part5`, B-K) is the only position that does it, per verb.

---

## R-06 — "characters must be robustly built with goals, ambitions, convictions, moral values, etc"  · `partial`

**Measured.** `corpus_run` [read 2026-09-30 from `requirements.yaml:872-876`, U10]: `RANKING DISCRIMINATION 15..21 of 31 candidates carry a nonzero
conviction score; the rest TIE and the tie is broken BY THE DRAW`. Two stated reasons the row is not
`met`: (1) `ambitions(p)` does not exist ([SETTLED at v8: `grep -rn "def ambitions" engine/season` found
nothing; **at HEAD it finds `queries/world_q.py:1309`** — `17` landed, so what remains of (1) is the cast) and the corpus cast is one shared OUGHT; (2) the convictions are correlated — nine of thirteen
within 60° of the mean vector (U3) — so people differ from their own alternatives more than from each
other. Realm (read 2026-09-30 from `requirements.yaml:881-887`, tree `c8cc408`): 46 distinct ambitions; 44 of 46 still live after 4 seasons, none laid down;
the OUGHT has no condition under which it comes true (closed at ladder step 3: an OUGHT is an uttered,
immutable Belief; it ends by `release`, `repudiate`, or death — `repudiate` is cut at IN-11, `2a2ed152`, #453 R-3(b)).

**What moves it.**

| position — `alias (v9 handle)` | what it changes | batch |
|---|---|---|
| `17` — landed | `ambitions` — a person-side READ over live `commit`→OUGHT Tenures (built in `queries/person_q.py`, now `queries/world_q.py:1309`); `build_at` seats the `cast:` | landed |
| cells commit (IN-08; J-1 answered) | the fifteen pursuits (`faith` is `doctrine`, `warden` is `stewardship`) × seven axes, from the two folded drafts; re-cells alignment over every verb on the table (44 rows at HEAD, `len(VERB_TABLE)`, read 2026-10-06; 46 with the two rows it adds; the six the draft lacks are celled inside the atomic commit; `tell`, `thread_read` and `restore` form its declared `uncelled:` set, each with its reason, G-1) — the only thing that moves reason (2); the doctrine-pair measurement and `conviction_spread`'s `within_60deg` recorded | landed (`0f998f64`) |
| H7, `12` / `12e` (IN-08's serial chain, after the cells commit) | the doctrine-pair test as a standing test (H7), scar rebuild (H3), crisis threshold (H13) | landed (`c13144b9`) |
| IN-11 (#453 step 2) — landed | `release` earns `commitment.ended` — the voluntary ender of an ambition; `repudiate` is cut (#453 R-3(b)), replacing v8's `14` row | landed (`2a2ed152`) |
| `13`-rest (IN-38; RS-21 item 2 [medium; Jordan to correct]; revert: Jordan states the other option) | 41 NPC + 97 ARC `cast:` overlays: distinct OUGHTs and `capability` per case — stopped at its pilot by Jordan's 2026-10-01 rule; scaled on the NPC lane only, on the per-case observable (distinct executed sets per case against its no-overlay arm) | B-V |

**No position owned until now:** nothing new — reason (1) was `17`'s (landed; its cast half is IN-38's), reason (2) is IN-08's (J-1 answered 2026-10-06). `ED-IN-0214` (whether to re-centre the correlated matrix, "Jordan's", `requirements.yaml:869-871`) is superseded by the 15×7 fold and closed in `_part5` §A.

**`blocks:` (`requirements.yaml:978`), traced.** `W27` (the cast comes from the case, `architecture/PLAN.md:1583`) — `17` (landed: `build_at` seats a `cast:`) and IN-38 (B-V). `H-62` (no verb writes a `Person` interior field; `absent`) — re-scoped, not closed, to IN-08, IN-18 and IN-12 step 9 (`_part6`'s SE standing table).

**Design question the tree does not answer.** Whether an OUGHT can be satisfied (the row's own
"WHAT WOULD OVERTURN THIS PARAGRAPH"). The tree closes it at step 3 (no condition exists); this plan does
not re-open it. A ruling otherwise would be new design and would be Jordan's to start.

**`met` =** `corpus_run`'s `RANKING DISCRIMINATION` line shows a nonzero conviction score on every
candidate a person is offered (no tie broken by the draw when the person has a reason), **and**
`python -m pytest engine/season/tests -q -k 'ambitions or cast'` passes with `DISTINCT EXECUTED SETS`
above the pre-cast arm, **and** the J-1 conviction-spread falsifier (`conviction_spread.py`, Jordan's
faith pair far apart, no more than a declared share of pursuits within 60° of the mean) passes. The
third conjunct is Jordan-gated.

⚠ **Annotation — the `met` above is verbatim:** its "faith pair" is the doctrine pair (the pursuit is renamed `doctrine`), and "Jordan-gated" no longer holds: J-1 is answered, the third conjunct's result is recorded, not gated (the `doctrine` row is PROVISIONAL), and Jordan's CELL-VALUE AND COSINE PASS follows as a non-blocking ask-then (`_part5` §J; IN-08 landed, `c13144b9`). **The third conjunct has two instruments, not one:** `conviction_spread.py` computes each pursuit's cosine against the MEAN vector only (`engine/season/harness/conviction_spread.py:154-159`; `within_60deg`, `:193`), so it reads the "declared share within 60° of the mean" half and cannot see a pair; the pair half is H7's doctrine-pair test (`_part5` IN-08) — B-G recorded the pair measurement (`0f998f64`), and B-H built the standing test (`c13144b9`). The draft's own flag stands as information: `within_60deg` 4 of 15. **Its first conjunct is read under G-1 [medium; Jordan to correct]:** "every candidate a person is offered" counts only candidates whose verb has at least one celled axis — `tell` stays uncelled by design (the folded draft gives it "no cell on any axis", `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md:999`, `:1377`; telling is driven by regard — the telling workplan's G1 — not by pursuit), so a `tell` candidate's zero is not a tie the person has a reason to break. The `met` line is this part's own — `requirements.yaml` carries no `met` text for R-06 (its row holds `statement`, `status`, `measured`, `measure`, `blocks`, `:833-978`) — so what IN-08 owes is (i) `corpus_run`'s RANKING line counting only candidates whose verb has at least one celled axis, printing that numerator and denominator, and (ii) a `measured:` note in R-06 recording the reading; the `measure:` command is untouched. Revert: Jordan states the other option (cell `tell`). The second conjunct moves with IN-38 (B-V), so B-V is the row's earliest `met`.

---

## R-07 — "characters must have memories and feelings and attitudes and relationships, and they must only have imperfect knowledge"  · `partial`

**Measured.** Imperfect knowledge holds structurally (`choose` takes no `World`; `View` capped;
`LedgerReader` own-ledger only) — row's `measure:`
`pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'`. Memory holds
(the ledger; a death is witnessed and occasioned two later acts in the realm run). **Feelings,
attitudes, relationships — `Person.stance` — have two writers, neither reachable by a witnessed event:**
`harness/populated.py`'s build-time loyalty seed, and `loop/effects_combat.py::_eff_march`'s M4
losing-side write, reached by nothing in the realm run because no field was fought. Position `10`'s
`tell`→stance write was built and reverted (H-79: every write target breaks `claim_subjects`); `10` is retired and never reused.

**What moves it.**

| position — `alias (v9 handle)` | what it changes | batch |
|---|---|---|
| telling T3a, T6 — landed (#449); G1, G2 (IN-18, landed `ac9724fc`) | **regard computed at read** — `stored stance + judged deeds + told valence` (G1), the teller's relation in the weighed reader (T3a) and a teller's `record` (T6). No stance write by `tell`. G1's `deed:` keys are authored on IN-08's 15×7 axes (B-G and B-H landed first, `0f998f64`, `c13144b9`, because G1 reads the alignment axes IN-08 re-cells) | landed (`ac9724fc`) |
| `24g` (SE-01, landed `d12c8db9`; J-6 answered: fixture, control 0) | the bodies clock: deaths with a cause, P3 individuation at CENSUS | B-F |
| `20-iv` — landed (PR #450) | the morale source and the walls are on the battle path, but the realm still fights no field (H-149's target-kind check refuses all 11 marches — [UNVERIFIED], R-04's `march` note), so `_eff_march`'s existing M4 stance write is still unreached in the realm | landed |
| IN-13 (#453 step 8) | the realm fights a field, so `_eff_march`'s M4 stance write is reached (conjunct 3) | B-M |

CARRY-INTERIOR's falsifier (#457 `:161`, "after a lost field or famine, stance rows change for witnesses") and #445 P-1 are re-expressed as regard-at-read and homed at IN-18 G1 and IN-13 (`_part5` IN-08 states the move) [UNVERIFIED: #457 `:161` not re-opened here].

**⚠ Withdrawn, with the reason.** v8 first re-scoped `10` to a stored stance write on a resolved
`fight`'s subject. The telling workplan's ruling (carried at IN-18) computes regard at read and counts a judged deed there
(G1), so a stored deed write would be a second route to the same fact — an S defect (§0.06). The stored
half of regard keeps exactly its two writers: the build-time loyalty seed and `march`'s M4 write.

**`met` =** the row's `measure:` passes, **and** after two seasons of `populated.build_realm(0)`, two
hearers who hold different claims about one C — or the same claim from tellers they regard differently —
read different `regard(p, C)` (asserted `>= 1` such pair, so a world where nothing was told fails),
**and** `_eff_march`'s stance write is reached by a fought field (`20-iv` landed; the realm still fights none — H-149's target-kind check refuses all 11 marches). The instrument for the first
conjunct is the telling workplan's G1 falsifier; the row flips on its own `measured:` paragraph quoting
both.

⚠ **Annotation — the `met` above is verbatim:** the 11 refused marches are read 2026-10-01 from `requirements.yaml:1022` [UNVERIFIED — R-04's `march` note]. **The regard conjunct's instrument is not G1's falsifier alone:** that falsifier is a constructed two-hearer fixture, the conjunct reads `populated.build_realm(0)` after two seasons. **The realm reader** [medium; Jordan to correct; revert: Jordan states the other option]: a two-season `build_realm(0)` run that reads `regard(p, C)` for every pair of hearers holding a claim about one C and asserts ≥ 1 differing pair whose difference comes from a claim or a teller's regard, not from stored stance alone, beside the same run at G1's control arm (judged and told halves at 0), which must show no such pair. **The branch taken at B-E (`ac9724fc`):** M0b read 36.4 % at `declared` on IN-18's base (`a467126a`), so G1 landed in B-E with no `deed:` cell, shipped live (`judged_gain` and `told_valence_gain` 0.5, H-192, H-193); the realm reader is `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`, which printed control 0 of 11449 pairs differing, shipped arm 3270 of 11449 (run at `ac9724fc`; R-07's `measured:` records it). The stance-write conjunct reads at B-M (IN-13), so B-M is the earliest `met`.

**`blocks:` (`requirements.yaml:1031`), traced.** `W-F` — spent (R-01's trace: superseded by A-12 / IN-18 G1; the stored half of regard keeps its two writers, above). `W27` — `17` (landed) and IN-38 (B-V); not on R-07's `met`.

---

## R-08 — "decisions must not be omniscient and perfectly rational — characters may not make the optimal decision based upon their epistemic knowledge and personal inclinations"  · `partial`

**Measured.** Non-omniscience holds (R-07). *A person declines the optimum*: built (U4,
`softmax(score / choice_temperature)` via Gumbel; falsifier
`test_u4_the_choice_is_sampling_and_the_argmax_is_its_zero_temperature_control`). *Inclination breaks a
tie*: **not built** — the alignment table is sparse, so ties are broken by the draw (`corpus_run`
RANKING line, as R-06). `needs_jordan: false` on the row is correct: what remains is build work (IN-08; J-1 is
answered), not a question about R-08 itself.

**What moves it.** The cells commit (IN-08, B-G): `alignment` re-celled over 46 verbs × 7 axes — the 44 rows at HEAD plus `challenge` and `accept`, less the declared `uncelled:` set (`tell`, `thread_read`, `restore`), each with its reason — makes most
candidates carry a nonzero score, so the person's inclination — not the draw — orders them. Then H3
(scar) and H9 (B-H, landed `c13144b9`). **Of the row's named gap — inclination cannot break a tie while the alignment table is sparse (`requirements.yaml:1053-1056`) — nothing but IN-08 moves it** (`_part3` §B), and this plan does not
pretend otherwise. (Telling T3a, T6 (landed) makes what a person believes depend on whom they
trust, and G1/G2 (IN-18, landed at B-E, `ac9724fc`) put regard into `score`; contributors, not the row's named gap.)

**`blocks:` (`requirements.yaml:1076`) and the row's own open work, traced.** The disposition names what remains as "BUILD WORK: W26 and `H-62`" (`:1087`). `W26` (the sitting decides: `determine` gains a predicate and an effect, `architecture/PLAN.md:1571`) → SC-01 (B-N; THE BAR). `H-62` → re-scoped to IN-08, IN-18 and IN-12 step 9 (`_part6`'s SE standing table). Neither is a conjunct of the `met` below, which is readable from B-G; the earliest `met` is read as B-N because the row lists W26, and IN-43's re-point (landed at B-C) moved W26 to SC-01 (R-08's `blocks:` comment).

**`met` =** `corpus_run`'s RANKING line shows, for each sampled person, that every tie among offered
candidates is between candidates with equal *nonzero* score (the draw breaks only true indifference),
and the U4 test stays green. Reads after J-1.

⚠ **Annotation — the `met` above is verbatim:** it reads after IN-08 (J-1 is answered; landed, `0f998f64`, `c13144b9`), under G-1 [medium; Jordan to correct]: the offered candidates it reads are those whose verb has at least one celled axis — a `tell` candidate (uncelled by design, R-06's annotation) carries no inclination, so its tie is not one the person has a reason to break. The `met` line is this part's own — `requirements.yaml` carries no `met` text for R-08 (its row holds `statement`, `status`, `measured`, `measure`, `blocks`, `needs_jordan`, `disposition`, `:1033-1087`) — so what IN-08 owes is the same pair as R-06's: `corpus_run`'s RANKING line counting only celled-verb candidates with its numerator and denominator printed, and a `measured:` note in R-08 recording the reading; the `measure:` command is untouched. Revert: Jordan states the other option (cell `tell`).

---

## R-09 — "chains of events within a scene are probabilistic, not deterministic"  · `partial`

**Measured.** A roll exists and reaches the game: `tell` → σ-leverage provider (`net = roll_net(pool)
+ net_boost(lev, pool)`), graded. `corpus_run` [read at v8, 2026-10-01] `DEGREES RESOLVED {'Failure': 145, 'Felled': 10,
'Partial': 26, 'Success': 8, 'Untouched': 9, 'Wounded': 14}` — two graded chains (`tell`, `fight`), no
inquiry graded. Why `partial`: the roll varies by SEED, not by PERSON. ⚠ The row's text "`Person.capability`
is empty on every corpus person" is **stale since position `13`** (one `capability` value authored,
the 2026-09-28 plan §8.7, `FORK:0671283`) — the row already carries the correction (`engine/season/requirements.yaml:1124`, `:1162`); the substance (near-uniform pools) still holds. `lev`
is 0.0 with no producer, by design (a fabricated leverage is a number nobody chose).

**What moves it.**

| position — `alias (v9 handle)` | what it changes | batch |
|---|---|---|
| `13`-rest (IN-38; RS-21 item 2 [medium; Jordan to correct]) | `capability` authored per cast member, only where a magnitude has a source → `_pool_of` varies by person there | B-V |
| #453 step 9 (IN-12: `train`, with `sabotage`, `tend`, `argue`; J-13 (iii) adopted, RS-21 item 10 [medium; Jordan to correct]; revert: Jordan states the other option) | the writer: `train` writes `Person.capability` only where a case names a vocation, and `pool_default` stands wherever none does → `_pool_of` varies by person only there. #453 step 9 also deletes `Person.pursuits`' declaration while IN-08 keeps that field live; the conflict is read at B-Q against the live field [UNVERIFIED until then] | B-Q |
| `17`, `8` — landed | `17` seats the cast the overlays author; `8` made the wound-count band edge data (H-98(b); the edge is authored in `rosters.yaml: combat_band_edges`; H-184 is the row split from H-98 at `8`'s close, `engine/season/hole_register.yaml:4127`, `:4133`, `:4137`) | landed |
| `22` (SC-01) | `speak` graded (`contests: a matter`) — a third graded chain | B-N |
| `ED-FI-0009` (FI-01) | a degree producer per inquiry shape — `research` first, then `examine` and `surveil`'s place case; `interview` is a prompt, `reconstruct` and `thread_read` wait (`_part6` FI-01) — a fourth graded chain once `research` lands (its deposit half built as SKIP at WITNESS, RS-21 item 1) | B-O |

**No position owned until now:** none. **The by-person conjunct, measured 2026-10-06 on its own instrument:** `python -m engine.season.harness.headless --seasons 2 --seed 0 --log` (exit 0, content hash `293067ea0b02f3219043de3a6947c740`) runs the harness's own three-person world — Carin, the bailiff and the warden, built by hand in `engine/season/harness/headless.py:52-133`, not from NPC-088's `cast:` — and sets no `capability` on any of them (the field defaults empty, `engine/season/state/carriers.py:565`; `build_world` assigns none), so all three draw `pool_default`; across the two seasons the log holds one `news.told` and one `kill.refused`. **0 of 3 persons differ in pool: the conjunct reads false.** The one corpus person with a `capability` (`p_a`, `{copying: 3}`, NPC-088's `cast:` overlay, `requirements.yaml:77-79`) is seated by `corpus_run`'s `build_at`, which this instrument does not run. No v9 position changes the headless world's capabilities: IN-38 authors corpus casts (B-V), and `train` (B-Q) writes `capability` only where a case names a vocation. **So R-09, hence M1 (`tools/m1_acceptance.py:320`), cannot read `met` under v9 until the remainder of J-13 — the SOURCE of `capability` beyond the interim — is ruled** (`_part5` §J.2; J-13 (iii) stays the [medium] interim). That ruling also has to say whether the source reaches this hand-built world or the `measure:` moves to a world that seats a cast; the second would be a record edit owed by the position the ruling names.

**`blocks:` (`requirements.yaml:1174`), traced.** `W23` (the contest branch reaches the engine, `architecture/PLAN.md:1504`) — **spent in substance**: `fight` resolves two parties through the combat seam and is graded (`DEGREES RESOLVED` carries `Felled`/`Wounded`/`Untouched`, above), though `corpus_run`'s `NOT_COMPUTABLE` text still names it for `A2` (`harness/corpus_run.py:678`) — marked spent in substance at B-C (IN-43's re-point, landed). `H-98` — its margin producer (a) and wound-count edge (b) closed at `8`; the fourth band stays open and is not invented (`hole_register.yaml:1353`; `_part4`'s register table holds it), and PC-01 (landed, `9054df80`) added a Margin, no fourth band; not on R-09's `met`.

**Design questions the tree does not answer.** (i) **`capability`'s scale and source** — H-126/H-127
are `assumption`; the one authored value (`NPC-088`'s `3`) was a named judgment call, not canon. `13`-rest
authors a `capability` only where a magnitude has a source; the scale is **J-13** (`_part5` §J): `rosters.yaml: verb_capability`'s values are only `copying` (`tell`, `speak`), while `references/npc_registry.yaml`'s `stats:` is absent or `null` on 45 of its 46 rows (29 carry the key, 28 of them `null`; counted 2026-10-06) and its one block holds attribute keys (`cognition focus endurance social`, one a prose range) — the vocabularies are disjoint, so any attribute → capability map is a number nobody chose. **J-13 (iii) is adopted as the plan's recommendation** (RS-21 item 10, [medium; Jordan to correct]; revert: Jordan states the other option): `pool_default` wherever a case names no vocation, as the interim; (i) fails as written. Jordan's constraints on any answer (2026-09-06, session S7; context, not an answer): *"the big question for me is what determines the actor's pool, and whether that pool changes based upon the kind of proceeding"*; *"pool only it is, but ensure you don't go so far as to deprive player of a chance at winning"*; *"It's a derived score that is used for the subsystem for a character, but it is not a character attribute in and of itself"* — so latitude enters through pool only, social figures are derived and not stored attributes, and the player keeps a real chance. So IN-12 step 9 (`train`) builds in B-Q, writing `capability` only where a case names a vocation, and R-09
varies by person only in those cases until a source is ruled; `13`-rest's breadth is IN-38's (B-V). (ii) Where `lev`
(σ-leverage) comes from for a person. The
row records it as deliberately zero. Nothing in code specifies a producer; this plan schedules none and
names it as an open design input to `22` step 15 (SC-01, B-N: the obstacle ceiling and `sigma_leverage` sweep),
which is the first position whose falsifier reads leverage.

**`met` =** `python -m pytest engine/season/tests -q -k test_we_only_a_verb_that_declares_contests_can_be_graded_today` passes, **and**
`python -m engine.season.harness.headless --seasons 2 --seed 0` shows two persons with different
`capability` resolving the same contested verb at different pools, **and** `corpus_run`'s `DEGREES
RESOLVED` line is non-empty for at least one non-combat verb besides `tell` (an inquiry or `speak`).
**Selector defect, fixed at B-C** (IN-43, landed): the old `-k 'we_only_a_verb or u1_'` selected 1 of 846 tests and `u1_` alone none (read 2026-10-06); the `measure:` now names the node id it ran.

---

## §11 · the R-01/R-02 acceptance command (v8 position `11`, U6 — DONE 2026-10-02; the command is kept here because `engine/season/requirements.yaml` cites it)

Carried verbatim from `workplans/valoria_master_workplan_v8_part4.md:24-45` (retired at its `FORK:` ref); three cite edits only (`main §0.6`, `_part6` §H.3, the telling workplan's T4). The adoption patch re-points `requirements.yaml:322`, `:405` and `:504` to this section.

**Both runs landed (PR #451).** At `2x3`, over 143 cases, reconvergence reads none 77.13 % · actor 43.03 % · total 38.47 % (baseline, `c2ee345a`) and none 77.22 % · actor 42.59 % · total 38.58 % (re-take, `8b03e518`, across `14`, `13d-iii` and `17-cast`): no arm moved by half a point, against a 96 % bar, so R-02 is `met` and R-01 stays `not_met` (`engine/season/requirements.yaml`, whose dated paragraphs label each figure; `proposals/2026-09-04-degree-sweep/runs/WD_LOG.txt` is the committed record, the 36 cells are untracked and rebuilt by the commands below). The instrument's run-to-run noise is not measured. Re-run it only when a build changes what a fork can reach.
**Acceptance — verbatim** (carried from U6; slices re-derived for 143):

```
cd proposals/2026-09-04-degree-sweep
for m in none actor total; do for s in default narrow 2x3; do \
  for r in "0 36" "36 72" "72 108" "108 143"; do python wd_chunk.py $m $s $r; done; done; done
python wd_collect.py
cd - && python -m engine.season.harness.corpus_run
```

**Acceptance point is `2x3`, not the shipped default** (U6's own correction: the acceptance is
cell-dependent). **Declare the prior before running:** `2x3` has read **100.00 %, zero divergences**
and never below the bar. **OBSERVABLE:** reconvergence **< 96 % at `2x3`**, cells committed under
`runs/`. **FALSIFIER:** ≥ 96 % ⇒ both rows stay `not_met` and the commit names which channel is still
closed — **H-116 first** (`belief_contradicts` narrows only on `PERSON_PREDICATES`, so a deposited
consequence about a non-person cannot narrow a later candidate set). Do not re-pin. **Control:** the
`none ≥ default` arm is the only control this instrument yields; say so. `fan_out_mode` is R-07's
fixture, not this one's. **Not here any more:** `test_n3`'s floors and the reverted build-order item 4 (`budget()` counting
`granted_acts`) belong to the telling workplan's T4 (`FORK:` ref; absorbed), which re-pins the floors and closes that question
(item 4's re-land is IN-14); re-land item 4 only after T4, against T4's floors. **R:** R-01, R-02 — on the printed number only. **Records:** both rows' `measured:` paragraphs
cite the run and its tree; R-02's `measure:` comment re-pointed off the retired plan (`_part8` §H.3).
