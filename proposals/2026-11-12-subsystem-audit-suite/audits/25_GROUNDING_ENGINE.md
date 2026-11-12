# 25 · Grounding: the suite's claims about the engine, settled at the line

## Status: REFERENCE (a grounding pass over documents that already exist; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `870c661` at the start, `62dbc8b` by the first probe (working tree, 2026-11-12). The code under every claim is the same at every SHA the suite cites (see §0).

Jordan, 2026-11-12: *"All ungrounded information should have info available on repository."* *"Do not
guess."* This file takes the suite's statements about the engine that their own authors marked as not
checked (`[UNVERIFIED]`, `[ASSUMPTION]`, "not opened", "by search only", "inferred", "cited second-hand"),
and the figures several proposals depend on, and settles each by opening the code or data at the cited
place, or by a short read-only probe.

**Statuses.** `VERIFIED` (the opened path:line is given). `VERIFIED-CORRECTED` (true in substance; a
line number, count or wording was wrong and is corrected in the suite text). `REFUTED` (what is true is
given with the opened path:line, and the suite text is corrected). `UNRESOLVABLE` (what would settle it is
named; the suite's mark stays).

**Method.** Each row was settled by `Read`/`grep` of the cited file at the cited line at the SHA above.
Where a behaviour is claimed, a probe was run with `PYTHONHASHSEED=0` at one seed per probe (seed 0;
seed 2 for the King's death, which is a claim about that seed); outputs are under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/GROUND_ENGINE/`
(called `runs/GROUND_ENGINE/` below). No pytest was run and no long aperture run. Other lanes' saved run
outputs (`runs/<LANE>/`) are cited as *their* evidence and say so; a figure this lane did not reproduce is
marked "as recorded, not re-run".

**What this file does not do.** It does not grade a design, and it does not re-audit a fix. A claim about
history, a game precedent or research is another grounding lane's subject and is not listed.

**Edits made to other suite files** are listed in §8; each edited file carries a `Grounded:` line at its
head. No finding of another lane was deleted.

## 0. Which tree the suite's claims are about

The suite's documents name fifteen or more read SHAs (`54e6661`, `601e715`, `84d2a02`, `6cbc712`, `870c661`
and others). **They are one code tree.** `git diff --name-only d015c93^ HEAD` (the commit before the suite's
first, to `62dbc8b`), filtered to paths outside `proposals/2026-11-12-subsystem-audit-suite/`, prints
nothing: every commit in that range touches the suite directory only. So a line number in `engine/`,
`modules/`, `references/`, `architecture/`, `registers/` or `tools/` cited by any suite document at any of
those SHAs is the line at HEAD, and a difference between two lanes' figures is a difference of seed,
season count or definition, never of code. (The locked worktree at
`.claude/worktrees/agent-a737f996de1fa4752` is another tree and was not read.)

A claim "measured at `51d7b05`" (2026-10-22) or any other commit before `d015c93` is a claim about another
tree. The clone is shallow (`.git/shallow` holds two boundary commits; 176 commits reachable), so those
are not reproducible here and are marked as recorded.

## 1. The figures the closure and unification lanes rely on

Probes: `runs/GROUND_ENGINE/g1_realm.py` (build facts, the verb table, then one season at seed 0, the
shipped chooser, the body of `populated.run`; 6 s for the season), `g2_king_probe.py 2 4` (the HAPPENINGS
lane's probe copied and re-run: seed 2, four seasons, 104 s), `g3_small.py` (build-time facts). That the
runs happened: `g1` logged 13,379 Events and 821 acts and reproduced the content hash two other lanes
recorded for that world (`5ab73af2…`); `g2` reproduced `b4bae063…`.

| # | claim | where in the suite | status | evidence (opened or run by this lane) |
|---|---|---|---|---|
| L-01 | the realm at `build_realm(0)` is 83 persons: 46 cast and 37 cohorts | `15_INSTITUTIONS_BYZANTINE.md:811`, `16_PESSIMIST_FA.md:295`, `:339`, `17_CENSUS_REST.md:253`, many | VERIFIED | `g1`: `persons` 83; 46 ids `p_npc_*` at weight 1, 37 ids `cohort_set_s*` at weight > 1 |
| L-02 | 34 seats: 18 `appointed`, 8 `elected`, 1 `inheritance`, 7 with no conferral | `15_INSTITUTIONS_VENICE.md:508`, `16_PESSIMIST_FA.md:29`, `:310` | VERIFIED | `g1`: `offices` 34; `conferral` counts 18 / 8 / 1 / 7 `None`. 33 persons hold the 34 seats (the King holds `off_king` and `off_duke_valorsmark`) |
| L-03 | 414 rungs | `15_INSTITUTIONS_BYZANTINE.md:811`, `07_SE_audit.md:357` | VERIFIED | `g1`: 414 = realm 1, duchy 3, territory 18, settlement 38, community 60, hearth 211, person 83 |
| L-04 | "37 of 37 settlements carry the site signature `(garrison, harbour, seam)`" | `21_PROCEDURAL_GENERATION.md:188` | VERIFIED-CORRECTED | `g3`: 322 Sites = 37 `harbour`, 37 `seam`, 37 `garrison`, 211 `dwelling`; 37 settlement rungs carry exactly that signature. The build holds a **38th** settlement rung, `set_alt_1` under `terr_ALT` (the foreign faction's place, `populated.py:1163-1179`, `foreign=True` shipped), with no Site. "37 settlements" is the realm's count; "38 settlement rungs" is the world's |
| L-05 | 698 tenures, 70 Propositions, 2 Records (both `works`) at build | `16_PESSIMIST_FA.md:145`, `15_INSTITUTIONS_BYZANTINE.md:811` | VERIFIED | `g1`: 370 on persons + 328 unowned = 698; live by kind on persons: `contain` 83, `reside` 83, `commit` 148, `hold` 52, `oblige` 4; `propositions` 70; `records` 2, kind `works` |
| L-06 | `capability` is empty for all but two cast; `attributes` empty for everyone | `12_ARCS_adjudication.md:301`, `01_CORE_audit_addendum_B.md:338`, `10_DICE_audit.md:142` | VERIFIED | `g1`: non-empty `capability` on `p_npc_004` and `p_npc_088`, each `{inquiry: 2}`; `attributes` non-empty on 0 of 83 |
| L-07 | "one of 46 cast rows authors `stats:`"; `ts` 10, `lifepath` 5, `heritage` 4; 34 lifepaths, 13 holding a key, only `argue` and `inquiry` | `01_CORE_audit_addendum_B.md:338`, `:774`; `02_CHAR_audit.md:924` | VERIFIED, with a reading | `references/npc_registry.yaml` parsed: 46 `characters`; `stats` 1, `ts` 10, `lifepath` 5, `heritage` 4. `rosters.yaml:3627-3661` (`tables: lifepath_templates: cells`): 34 rows, 13 with a non-empty `holds:` (`inquiry` 7, `argue` 6). **Five cast rows carry a lifepath; two of the five gain a key** (NPC-004 `3-CH5` and NPC-088 `3-CF4`, both `inquiry`; `3-VA1` and `3-LO3` hold `[]`). "to 5 of 46 cast rows" means *authored on* five, not *granted to* five |
| L-08 | `cast_attributes=False` ships (`populated.py:1016`) | `01_CORE_audit_addendum_B.md:338`, `10_DICE_audit.md:142`, `02_CHAR_audit.md:156`, `05_SC_audit.md:192`, `13_SC_contest_interrogation.md:175` | VERIFIED | `engine/season/harness/populated.py:1014-1016` (signature); `:1019` (docstring: reads each cast row's `stats:` into `Person.attributes`); `:1355` (`if cast_attributes:`). `inspect.signature` in `g1`: `cast_attributes` False, `guards` False, `foreign` True |
| L-09 | `faculty` is the one pool reader, at `engine/season/seam/wrappers/pool.py:78-100`; the base is `:94-100` | `01_CORE_audit_addendum_B.md:432`, `03_PC_audit.md:44`, `10_DICE_audit.md:141`, `:807`, and 40 other citations | VERIFIED | `pool.py:78` `def faculty(w, p, verb) -> int`; `:94-100`: held attribute, else the larger of attribute and held key, else the held key, else `pool_default`; plus `POOL_ADDENDS` (`:38`, practice registered at `:51`). Other line cites opened and right: `:18` `_capability`, `:41` `register_pool_addend`, `:54` `_held_attribute`, `:60` `_authored_attribute`, `:68-75` `_opposing_attribute`, `:79-80` (*"Rank supplies dice and gates nothing"*, citing `03 §A.2`) |
| L-10 | "`seam/wrappers/sigma.py::faculty`" | `04_MB_audit.md:1120`, `06_FA_audit.md:833`, `14_VERBS_PHYSICAL.md:813`, `14_VERBS_MILITARY.md:135`, `proposals/06_FA_office_capabilities.md:20` | VERIFIED-CORRECTED (five files edited) | the owner is `pool.py:78`. `sigma.py:105` imports it (`from .pool import … faculty …  # noqa: F401 (moved: see pool.py)`) so `sigma.faculty` resolves, as a re-export. `rosters.yaml:1417`, `:1424`, `:1509`, `:1566` still spell the old path (the census lane lists the hole register's copies as stale labels, `17_CENSUS_REST.md:211`) |
| L-11 | `obstacle_default` is 2, the stand-in where the subject has no score; `pool_default` 2; `obstacle_ceiling` 2 with `ceiling_per_pool` | `13_SC_contest_interrogation.md:82`, `:143`; `14_VERBS_SOCIAL1.md:234`; `16_PESSIMIST_GAME.md:181`; `01_CORE_audit_addendum_B.md:433` | VERIFIED | `engine/season/data/fixtures.py:449` `pool_default=2`, `:451` `obstacle_default=2`, `:454` `obstacle_ceiling=2`, `:460` `ceiling_per_pool=True`; `modules/social_contest/roll.py:141`: `ob = float(inp.opposition) / 2.0 if inp.opposition is not None else float(inp.obstacle_default)`. `g1` read the same four off the built world's fixtures |
| L-12 | 67 verb rows; 11 contested; 3 graded inquiries; so 53 take the uncontested fold | `18_DETERMINISM_SWEEP.md:28`, `:134`; `01_CORE_audit_addendum_B.md:774` | VERIFIED | `g1`: `VERB_TABLE` 67 rows; `contests` non-empty on `accept`, `argue`, `arrest`, `capture`, `determine`, `fight`, `interrogate`, `lie`, `march`, `speak`, `tell`; `rosters.yaml:1407` `graded_inquiries` = `research`, `examine`, `surveil` (`g3`). 67 − 11 − 3 = 53. `resolvable_verbs()` is 66 (`tie / knot` is the one out) |
| L-13 | "9 with a capability row; four vocations"; "five contested verbs name no capability key" | `01_CORE_audit_addendum_B.md:338`, `:774` | VERIFIED | `rosters.yaml: verb_capability` (`g3`): `tell`, `speak` → `copying`; `argue` → `argue`; `research`, `examine`, `surveil` → `inquiry`; `fight`, `accept`, `capture` → `arms`. Contested and absent from it: `arrest`, `determine`, `interrogate`, `lie`, `march` |
| L-14 | which verbs execute: realm seed 0, three seasons: 30 execute, 18 are attempted and always refused; corpus: 23 execute, 13 only refused, 30 never attempted, 1 with no predicate or effect; union 33 of 67 | `17_CENSUS_REST.md:317-322`, `:451-452`; `11_GO_audit.md:757` | VERIFIED for the realm from the saved output, and at one season by this lane; corpus as recorded, not re-run | the census lane's `census_rest/aperture_3_0.txt` lines 91-157 re-counted: 67 rows, 48 attempted, 30 with `ex > 0`, 18 with `ex 0`. `g1` (seed 0, **one** season): 42 verbs attempted, 26 execute, 16 refused only (`accept`, `build`, `capture`, `challenge`, `comply`, `construe`, `covenant`, `determine`, `establish`, `evade / defy`, `exchange`, `found`, `raze`, `release`, `sabotage`, `train`). The corpus run takes eight minutes (`runs/CORE/corpus_run.time`) and was not repeated; its saved line 31 reads "1 have no predicate/effect · 30 foldable but never even attempted" |
| L-15 | "92 % of success events were decided with no draw" (1,995 of 2,159; 385 Events carried a degree; 3,826 resolved acts; seeds 0 one season, 1 and 2 two seasons) | `18_DETERMINISM_SWEEP.md:30`, `:40`, `:131` | VERIFIED at seed 0; the pooled figure reproduces to within 45 events from the lane's saved files | `g1`, seed 0, one season: Events of an act whose kind is a success kind of its row: 454; with a degree 33 (`march` 12, `research` 9, `tell` 4, `argue` 4, `lie` 2, `speak` 1, `surveil` 1); without 421 = **92.7 %**. Events with any degree: 61, equal to `runs/DET/realm_s0.json` (`drawn_events` 61, `resolved` 749, same hash). Summing the three saved files: `resolved` 749 + 1,519 + 1,558 = 3,826 ✓; `drawn_events` 61 + 181 + 143 = 385 ✓; success-kind Events 454 + 840 + 910 = **2,204**, against the sweep's 2,159. The 45-event difference is a definition this lane could not recover (the sweep's script was not saved); the share is 92 % either way |
| L-16 | the refusal rate: "42 % of acts are refused" | `16_PESSIMIST_GO.md:34`, `:384`; "four in ten" `02_CHAR_audit.md:27`, `:295`; `22_HAPPENINGS.md:205`; `17_CENSUS_REST.md:452` | VERIFIED as a range; **four definitions are in use** | `g1`, seed 0, one season, the act store (821 acts): 377 acts carry a refusal-kind Event (45.9 %); 46 of those also carry a success kind and 28 are graded losses (a lost draw, `corpus_run.graded_loss`); **refused and nothing else: 331 = 40.3 %**. The suite's four figures: (a) GO pessimist, *every Event of the act is a refusal kind*, 2,151 of 5,116, three seeds two seasons: 42.0 % (not re-run; this lane's 40.3 % is the same definition at one seed, one season). (b) CHAR, `.refused` Events over **resolved** acts, 656 of 1,529. (c) HAPPENINGS, 322 refusal Events on 749 acts: the 749 is the folded set (`SeasonDriver.resolved`), not the 821 attempted. (d) census, 1,440 of 2,630 at seed 0 over three seasons (54.8 %): *acts carrying a refusal kind*, which includes 116 graded losses and 187 acts that also executed; refused-only there is 1,253 = 47.6 %. The rate rises with seasons |
| L-17 | "2,630 attempts, 1,377 executed, 1,440 refused" against "2,630 acts, 1,190 executed" for the same world | `17_CENSUS_REST.md:452` against `16_PESSIMIST_WR.md:68`, `:636` | VERIFIED: both are columns of one line | `census_rest/aperture_3_0.txt:158`: `TOTAL att 2630 ex 1377 ref 1440 att-ref 1190 both 187 graded 116`. 1,377 is acts with a success-kind Event; 1,190 is acts with no refusal-kind Event; they differ by the 187 acts in both columns. Neither figure is wrong; a document quoting "executed" should say which |
| L-18 | the King (`p_npc_020`, Almud Almqvist) is alive after the first season at seed 0; at seed 2 he dies in the fourth season, felled in the Spymaster's `capture`; the Cardinal of Prudence dies as captor in the second | `22_HAPPENINGS.md:17-36`, `:62-66`, `:99-109` | VERIFIED by re-run | `g1`: seed 0, one season, `king_alive` true, 0 deaths, hash `5ab73af282d0779646c38839fbab85d8`. `g2` (`g2_king_2.out`): seed 2; King alive after seasons 0, 1, 2; dead in season index 3; `person.died` at log index 111,995, degree `Felled`, act `capture` by `p_npc_033` via `off_spymaster`; `p_npc_013` dies at index 26,672 in season index 1 capturing `p_npc_004`; seats held 34 → 31; hash `b4bae063f33476988db678b5aae62a28`. Every figure equals the HAPPENINGS lane's `king_2.out` |
| L-19 | "the King dies at tick 0 in every seed" | `digests/DG_proposalsB4.md:100`, `:114`, `:258` (a digest of the 2026-10-22 tutorials) | REFUTED at HEAD (already so marked by `22_HAPPENINGS.md` §0) | L-18. The digest's line is a measurement at `51d7b05`, which this clone cannot reach |
| L-20 | `capture` is not gated by a context of violence | `22_HAPPENINGS.md:29`, `:113-116`; `proposals/22_HAPPENINGS_C_…md:31` | VERIFIED | `engine/season/rosters.yaml:2772-2773`: `violence_contexts: values: fight: [war, crime, duel, defence]`, one line; its note at `:2765-2767`: *"the coercion rows (`arrest`, `detain`, `capture`, `interrogate`, `seize`, `raze`, `march`) keep their own gates"*. Reader: `decision/options.py:216-224`. `capture`'s own gate: `verb_table.yaml:868` `eligibility: ["remit:dispatch"]`, `:872` `requires:` *"the subject is a living individual, present where the actor is"*; fought to the yield, `rosters.yaml:1019` `capture: yield` |
| L-21 | "v11 CR-87 gated `fight` and `accept`" | `22_HAPPENINGS.md:27-28` | VERIFIED-CORRECTED (text edited) | CR-87's roster gates `fight` alone (L-20). `accept` forms only on a held `challenge` Record addressed to the actor, which is v10 PC-10b's cell (`verb_table.yaml:956-958`, `:961-972`); what CR-87 gave `accept` is its terms, `blood` (`rosters.yaml:1000-1002`, `:1030`) |
| L-22 | nobody named can die of age or illness: `age_step = 0.0`, `illness_rate = 0.0` (`data/fixtures.py:690-691`); everyone is zero seasons old | `22_HAPPENINGS.md:144` | VERIFIED | `fixtures.py:690-691`; `g1`: `born` is 0 for 83 of 83; `state/carriers.py:776` (`born` defaults to `-age_at_build`) |
| L-23 | THE NINE: met 3, partial 5, not met 1 (R-05) | `17_CENSUS_REST.md:312` | VERIFIED | `python -m engine.season.harness.register --requirements`, run by this lane: `met 3 · not_met 1 · partial 5`; R-05 `not_met`. (The row is doc-derived by its own statement, CLAUDE.md §0.2) |
| L-24 | 586 `raise` statements in non-test `engine/season` | `01_CORE_audit_addendum_B.md:365` | VERIFIED | `grep -rE '^\s*raise ' engine/season --include=*.py`, less `/tests/`: 586. `04:986-987` records 167 on 2026-09-05, by `grep -c '^\s*raise ' engine/season/*.py` "and siblings". Whether those two file sets are the same cannot be read here (the shallow clone does not reach the tree of 2026-09-05), so the "about 3.5-fold" growth is UNRESOLVABLE as a ratio; the count 586 stands |


## 2. The Layer 1 passages the suite quotes

Each row was opened at the line. `holonic` is `architecture/holonic_ARCHITECTURE.md`; `04` is
`architecture/meta/04_CODE_ARCHITECTURE.md`; `03` is `architecture/meta/03_VERBS_AND_LOOPS.md`.

| # | passage, as the suite quotes it | where in the suite | status | opened |
|---|---|---|---|---|
| A-01 | §27.2: *"No second resolver. No auto-resolve formula. No fast path."* and *"THIS IS THE REFUSAL WITH NEITHER A MECHANISM NOR A CHEAP TEST. It is enforced by a person noticing."* | `04_MB_audit_addendum_B.md:112`, `:699`; `03_PC_audit_addendum_B.md:235`; `unified/DECISIONS_FOR_JORDAN.md:178` | VERIFIED | `holonic:984` (heading), `:986`, `:988-990`. "No second resolver" is also among the seam's four leaks at `holonic:1392` |
| A-02 | §29: CENSUS is *"DEMAND-DRIVEN ONLY. Nothing generates without a demand, and no clock generates anything."* | `07_SE_audit_addendum_B.md:339-340` | VERIFIED | `holonic:1023` (heading), `:1028` |
| A-03 | §25's table: *"bodies, ageing, natural death"* is *"one of the three licensed clocks"*; *"envelope weight — births and deaths"*; §10.3: written at MATTER, reconciled at CENSUS | `07_SE_audit_addendum_B.md:341-343` | VERIFIED | `holonic:850` (heading), `:860`, `:866`; `holonic:401-405` (*"The envelope is written at MATTER and reconciled at CENSUS"*) |
| A-04 | §39.3: the depth cap has no default; *"a nested instance is an instance"* is *"not a bound"*; exceeding it is a typed error | `03_PC_audit_addendum_B.md:274`; `unified/DECISIONS_FOR_JORDAN.md:256` | VERIFIED | `holonic:1396-1402` |
| A-05 | §44.3: a wrapper never holds state, decides, resolves or drives a clock; *"a wrapper that computes an outcome **is** the second resolver"* | `03_PC_audit_addendum_B.md:127`, `:237`, `:327`; `05_SC_audit_addendum_B.md:213` | VERIFIED | `holonic:1679-1686`; the quoted sentence is `:1685` |
| A-06 | `04` §A.2: MATTER reads *"Sites, bodies, larders, ttl/term"* (`:174`); CENSUS owns `weight` and `envelope` (`:179`); the provider adapters own *"nothing, ever"* and return a `Margin` | `07_SE_audit.md:393-394`, `:622`; `01_CORE_audit_addendum_B.md:357`; `17_CENSUS_REST.md:293` | VERIFIED | `04:127` (heading), `:174`, `:179`, `:182`. `04:122` is T-k, *"one resolver, one ladder"* (`03_PC_audit_addendum_B.md:51` cites `:116-122`) |
| A-07 | `04` §C.4 (ruled 2026-09-03): *"The degree is READ OFF THE SUBSYSTEM, never mapped onto it by the table"* | `01_CORE_audit_addendum_B.md:337`, `:379-381` | VERIFIED | `04:659` (heading), `:712-713`; the "no second resolver" row, graded CONVENTION, is `04:761` |
| A-08 | `04` §C.5: *"the subsystem returns a `Margin`; a subsystem returning a winner has not met the contract"*; D-24; §C.5.1: *"units = PersonId[] at weight — one type. There is NO unit class, at any scale"* | `01_CORE_audit_addendum_B.md:337`, `:357`, `:379`; `04_MB_audit_addendum_B.md:113`, `:741`; `04_MB_audit.md:625`, `:1248` | VERIFIED | `04:771` (heading), `:786`; D-24 is row 24 at `04:1050`; `04:793` (§C.5.1), `:802`; the grid-squad row `03_PC_audit_addendum_B.md:396` cites is `04:811` |
| A-09 | *"`04:237` forbids social aggregates on a Rung"* | `13_SC_contest_interrogation.md:331`; `14_VERBS_PHYSICAL.md` (three places); `proposals/14_VERBS_PHYSICAL_C_looking.md:44` | VERIFIED-CORRECTED (three files edited) | the rule is `04:260`, in §B.3 `Rung` (`04:255`): *"NEVER: any social aggregate — no norms, unrest, legitimacy, reputation, discipline"*. `04:237` is a line of §B.2's `Person` block. The stale number is the tree's own: `engine/season/verb_table.yaml:1747` cites `04:237`, and the suite copied it. The tree was not edited |
| A-10 | `04` §C.12: ratified; the RNG row, *"a seeded `RandomNumberGenerator` threaded like `World`"*; rejection 5's Result shape is *"PROPOSED, not ruled"*; 167 raises measured 2026-09-05 | `11_GO_audit.md:48`, `:425`; `16_PESSIMIST_GO.md:93`, `:645`; `01_CORE_audit_addendum_B.md:365` | VERIFIED | `04:906` (heading; the section runs to `:1017`), `:927`, `:986-987`, `:1004` |
| A-11 | "§C.4": fidelity, *"They agree exactly, because they are the same slice"* | `04_MB_audit_addendum_B.md:700`; `03_PC_audit_addendum_B.md:239`; `AUDIT_BRIEF.md:77`; `unified/DECISIONS_ANSWERED.md:7` | VERIFIED, with a note for the unification lane | `03:146` (heading, *"Fidelity — the same slice, rendered at different depths"*), `:153`. **Two documents have a §C.4.** The fidelity rule Jordan's ruling 1 leaves unchanged is `03` §C.4; `04` §C.4 is the one fold (A-07). The brief and the decisions record write "§C.4" without the document; the audits that quote it give the path. Not edited (the brief records rulings); a reader who opens `04` §C.4 looking for the fidelity rule will not find it |
| A-12 | *"Rank supplies dice and gates nothing"*, `03 §A.2` | `03_PC_audit.md:673` | VERIFIED as the code's citation | `seam/wrappers/pool.py:79-80` quotes it and names `03 §A.2`; `03` itself was not opened at that section |

## 3. Marks settled at the line

`G-nn` is the tag written into the suite text at the mark (`[GROUNDED, 25 G-nn: …]`). "Fallback" means
the proposal had already said what it would do if its first reading was wrong; where that reading was
wrong the mark now says so and the fallback is the edit.

| # | the claim, as marked | where | status | evidence |
|---|---|---|---|---|
| G-01 | a graded-route row can carry writes keyed by degree ("each converted row gains `writes_by_degree`", "the existing columns"; "the fold runs an effect per band for a graded-route row") | `proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md` steps 2, 4; `14_VERBS_MILITARY.md` S1; relied on by every VERBS band map | **REFUTED at the loader, VERIFIED at the fold** | `engine/season/data/verbs.py:848-851`: a degree-keyed `writes:` with no `contests:` is refused at import; `:872-876`: a routed row with a non-empty `writes:` is refused (*"A graded verb keys its emissions by Degree and writes nothing"*). The fold itself is ready: `loop/resolve.py:897`, `:450`, `:967`. Both refusals were observed on a planted scratch copy (`g6_loader_plant.out`, §7). No converted row loads until those two refusals are edited; the determinism proposal now carries the edit |
| G-02 | "whether an `any:` combinator exists in `data/requires.py`" | `proposals/14_VERBS_MATERIAL_D_paper.md` | REFUTED (fallback) | `data/requires.py:1021-1030`; requirement classes `:292-558` (`Existence`, `ScalarThreshold`, `ContainPath`, `Relation`, `OwnLedger`, `Basis`, `AllOf`) |
| G-03 | "a row may list two [referent] classes" | same, the `seize` row | REFUTED (fallback) | `data/verbs.py:245`, `:668`, `:693` |
| G-04 | "whether a typed conjunct can be waived by a payload key without a new form" | `proposals/14_VERBS_MILITARY_C_the_muster.md`, `…_D_the_order_of_battle.md` | REFUTED (fallback) | `data/requires.py:1027-1030` |
| G-05 | "whether a keyed refusal may name a clause, `stores`, that is the effect's decline" | `proposals/14_VERBS_MATERIAL_C_works.md` | REFUTED (fallback) | `data/verbs.py:945-967` |
| G-06 | "that `World.write` accepts a `spec=` for a MATTER write" | `proposals/16_PESSIMIST_SE_B_…md` | REFUTED (fallback) | `state/world.py:1138-1148`, `:1442`, `:1494`; `state/gate.py:1905-1906`; `state/carriers.py:197-205` |
| G-07 | "that `born` is hashed" | `proposals/22_HAPPENINGS_A_…md` | VERIFIED | probe `g3_small.py`: two `build_realm(0)` worlds differing in one `born` differ in `content_hash()` |
| G-08 | `mortal_terms` in `queries/world_q.py` may import `party_end` from `seam/wrappers/combat.py`, else sit beside `body_band_penalty` in `decision/budget.py` | same | **REFUTED, both homes** | `queries/world_q.py:16-17`; `seam/wrappers/combat.py:86`, `:92`, `:143`; `seam/wrappers/pool.py:15`; `decision/budget.py:71` |
| G-09 | `state/gate.py:782` (`may_claim`): "the claimant holds *the* title" | `proposals/22_HAPPENINGS_B_…md` | VERIFIED | `state/gate.py:770-786` |
| G-10 | ED-FI-0002 "lives in the archive ledger" | `08_FI_audit.md` §5; `proposals/08_FI_04_small-edits.md:78` | VERIFIED | `registers/editorial_ledger_fi_archive.jsonl` |
| G-11 | H-234 is "flagged for Jordan" by `needs_jordan` on ED-IN-0298 | `08_FI_audit.md` R-18 | REFUTED | the last `ED-IN-0298` row, `registers/editorial_ledger_in.jsonl`, 2026-10-26: `status: partial`, `needs_jordan: false`, answered by ED-IN-0300 |
| G-12 | `auto_manual_resolution_duality_v1.md` is "Doctrine RULED 2026-07-08", ED-SC-0013 | `proposals/03_PC_duel_round_and_approach.md` | VERIFIED-CORRECTED | `registers/editorial_ledger_sc_archive.jsonl`: one row, `status: resolved`, describing the doctrine as "(PROPOSED) — drafted 2026-07-08 at Jordan's request" |
| G-13 | "`rosters.yaml: unrest_kinds`" | `proposals/14_VERBS_MATERIAL_B_stores.md` | REFUTED (name corrected) | `queries/person_q.py:517`; `data/rosters.py:1001` |
| G-14 | standing orders "fire and are obeyed with certainty once their trigger is met" | `14_VERBS_MILITARY.md` §0 | VERIFIED | `modules/mass_battle/core/contact.py:66-128` |
| G-15 | "`claim.decayed` deposits nothing a person acts on" (`undeposited_kinds` not opened) | `01_CORE_audit.md` §5 | VERIFIED-CORRECTED (the route) | `rosters.yaml: undeposited_kinds` = `[finding.none]`; `epistemic.py:756-766` |
| G-16 | "no row needs [`hold:<kind>`] today" | `01_CORE_audit.md` H-75 | VERIFIED-CORRECTED | `verb_table.yaml:340`, `:659`, `:2062`; `loop/resolve.py:139-141` |
| G-17 | "`train` raises a key a person already holds" | `05_SC_audit.md` §14 | VERIFIED | `loop/effects_combat.py:794-816` |
| G-18 | "that `held_by` is a predicate `LedgerReader` already reads" | `proposals/07_SE_kernel_repairs.md` | VERIFIED | `data/requires.py:851-855`, `:888-889`, `:901`; `queries/person_q.py:1002-1016` |
| G-19 | "that `release` admits one's own commit today" | `16_PESSIMIST_CHAR.md` | VERIFIED | `data/rosters.py:526`, `:538`; `loop/predicates.py:431-447` |
| G-20 | "whether `_seize_rung` rolls today" | `proposals/09_WR_B_draws_not_thresholds.md` | VERIFIED (it does not) | `loop/effects_information.py:1038-1075`; L-12 |
| G-21 | `epistemic.py:379`, "witnessing a forging closes its trail" (cited second-hand) | `19_LACUNA_investigation_to_proceedings.md` §2 | VERIFIED-CORRECTED | `epistemic.py:376-377` (the rule), `:379-383` (reachable only through a plant) |
| G-22 | "the lasting mark falls at the deepest gate crossed" (`effects_combat.py:394-424`, not opened) | `16_PESSIMIST_PC.md` | VERIFIED | `loop/effects_combat.py:394-424` (`:418`, `:421-423`); `data/fixtures.py:723` |
| G-23 | a cohort's `tend` "is not caused, in the log, by the fall it answers" | `16_PESSIMIST_SE.md` §3 | VERIFIED | probe `g4_behaviour.py`, seed 0, one season: 37 `body.tended`, 37 self-tending, each with `causes` = its own act |
| G-24 | the `(Person, weight)` matrix row's `steps:` | `proposals/07_SE_population_census.md` | VERIFIED | `write_matrix.yaml:300-306` (`steps: [CEN]`); the regrowth proposal's cite of the same lines is right |
| G-25 | "`write_matrix.yaml` admits `determine` on `(Record, stages)` without a row edit" | `proposals/05_SC_acquittal.md` | VERIFIED | the matrix row parsed (`steps: [RES]`, `class: ACTS`, no verb column); `determine`'s row parsed |
| G-26 | "the exact stem names of the `hold`, `capability` and `dispute` conjuncts" | `proposals/02_CHAR_offer_what_can_be_done.md` | VERIFIED-CORRECTED | `data/requires.py:809`, `:851-855`, `:888-889`; `verb_table.yaml:34`; `loop/effects_combat.py:812-814` |
| G-27 | "that `CHOICE_RANGES` accepts a numeric range" | `proposals/07_SE_arc_needs.md` | VERIFIED-CORRECTED | `data/verbs.py:1698-1700`, `:1708`; `modules/mass_battle/massbattle.py:226` |
| G-28 | "that every reader of `SUCCESSIONS` asks it in place" | `proposals/06_FA_playable_scenario.md` | VERIFIED, with its condition | `state/gate.py:54`, `:743`, `:782`; `decision/options.py:34`, `:240`; `loop/effects_governance.py:16`, `:164`; `engine/season/tests/test_in61_succession.py:161` |
| G-29 | "the pair order of `cache.tenure_index(w).knots`" | `proposals/08_FI_08_knots-season-form.md` | VERIFIED | `queries/cache.py:95` |
| G-30 | the test at `test_season_shape.py:4729-4731` | `proposals/17_CENSUS_REST_1_deletions.md` | VERIFIED | `engine/season/tests/test_season_shape.py:4724` |
| G-31 | "whether `enemies_heard` stamps cohort persons as `Enemy`" | `14_VERBS_PHYSICAL.md` §2 | VERIFIED (no cohort test; none stamped at build) | `queries/world_q.py:3677-3711`; probe `g4`: `faction_holding` is `None` for 37 of 37 cohorts and set for 43 of 46 cast, which also verifies `16_PESSIMIST_FA.md:339` |
| G-32 | "the captive's `detain` edge is read by `world_q.mustered` through `restrained`" | `14_VERBS_PHYSICAL.md` §2 | **REFUTED** as a description of today | `queries/world_q.py:2132-2149`, `:2027-2038`, `:1766` |
| G-33 | "whether [the `challenge.issued`] witness claim names the Record id" | `14_VERBS_PHYSICAL.md` §5 | VERIFIED in part; the rest left marked | `loop/effects_information.py:205-231`, `:308-334` |
| G-34 | "`_fall` must be a draw, and if it is a fixed fraction it is a finding" | `14_VERBS_PHYSICAL.md` §6 | VERIFIED (a fixed fraction) | `loop/effects_economy.py:141-158` |
| G-35 | "whether `comply` and `evade / defy` carry alignment cells" | `06_FA_audit.md` §15 (d) | VERIFIED (they do) | `rosters.yaml: tables: alignment: cells`, parsed: both verbs under each of 7 axes; neither under `pursuit_projection` |

## 4. Line citations opened and found as cited (no text changed)

`engine/season/` is the root unless a path says otherwise.

| # | the suite's citation | where | opened |
|---|---|---|---|
| V-01 | mass battle "returns `attacker_wins` and `winner=`" (`mass_battle.py:457-459`) | `01_CORE_audit_addendum_B.md:337` | `seam/wrappers/mass_battle.py:457-459` |
| V-02 | personal combat's entry returns a dict (`combat.py:398-401`) | `01_CORE_audit.md:301` | `seam/wrappers/combat.py:398-401` (`got["result"]`, `got["trace"]`, `got["wound_state"]`) |
| V-03 | `Rung.envelope` is "the ratified-but-unwritten field" (`world_q.py:1803-1807`); the matrix row | `17_CENSUS_REST.md:293` | `queries/world_q.py:1803-1807`; `write_matrix.yaml` `(Rung, envelope)`: `steps: [MAT, CEN]`, emits `envelope.changed` |
| V-04 | `body_hazard` at `world_q.py:1248` | `22_HAPPENINGS.md:144` | `queries/world_q.py:1248` |
| V-05 | a commander who left the faction cannot command (`effects_army.py:40-42`) | `04_MB_audit.md:1065` | `loop/effects_army.py:40-42` |
| V-06 | "THE BODIES CLOCK" at `loop/matter.py:713` | `07_SE_audit_addendum_B.md:343` | `loop/matter.py:713` |
| V-07 | a matured term closes its edge, emitting `tenure.closed` (`matter.py:428-435`) | `09_WR_audit.md:733` | `loop/matter.py:428-435`. It closes **every** live Tenure whose term matured, of any kind; that the 27 season-5 closures are `oblige` terms is still U-03 |
| V-08 | `choose` cannot reach world state through its `View`, by type (`carriers.py:504-509`) | `01_CORE_audit.md:178` | `state/carriers.py:504-509` |
| V-09 | `DevelopmentSheet` (`decision/sheet.py:115-163`) | `01_CORE_audit_addendum_B.md:336` | `decision/sheet.py:115` (the class and its docstring; the body was not read to `:163`) |
| V-10 | who may strip a seat: the rung directly above (`gate.py:485`, `:604-606`) | `16_PESSIMIST_FA.md:353` | `state/gate.py:485-486`, `:604-606` |
| V-11 | the silent default at `manifest/registry.py:180` | `11_GO_audit.md:396` | `manifest/registry.py:178-180` |
| V-12 | a kit is one weapon and one armour (`world_q.py:3484-3509`) | `03_PC_audit.md:582` | `queries/world_q.py:3484-3487` |
| V-13 | `violence_contexts` read at `decision/options.py:216-224` | `22_HAPPENINGS.md:97` | `decision/options.py:216-224`; the closed reader set `VIOLENCE_CONTEXT_READERS` is in the same file (`:434-509`), which settles `proposals/03_PC_duel_chain_reach.md:62`'s mark on its location |
| V-14 | ED-IN-0337's record lists "the Spymaster against the King" among 13 fights | `22_HAPPENINGS.md:95-96` | `registers/editorial_ledger_in.jsonl`, row `ED-IN-0337` (2026-11-05, ratified) |
| V-15 | ED-FA-0001 is one archived row, 2026-07-05, ratified | `06_FA_audit_addendum_B.md:88` | `registers/editorial_ledger_fa_archive.jsonl` |
| V-16 | the two degree ladders differ "at 6 of 10,000 tenth-step cells"; the guard sweeps only exactly representable values (`test_degree_ladder_single_owner.py:302-309`) | `10_DICE_audit.md:121`, `:279`; `04_MB_audit_addendum_B.md:145` | reproduced (`g5_ladders.out`): `dice_engine.degree_label` against `modules/mass_battle/resolution.py:104` `compute_degree`, 6 of 10,000 with `i*0.1`; **18 of 10,000 with `i/10`**. The count depends on how the tenth is formed; that the two disagree does not. `tests/valoria/test_degree_ladder_single_owner.py:302-309` |
| V-17 | `knowledge_kinds` is a roster nothing reads (`rosters.yaml:1763-1777`) | `17_CENSUS_REST.md:158`; `12_ARCS_adjudication.md:375` | `rosters.yaml:1763`; values `[mundane, thread_substrate]`. "Nothing reads it" is the census lane's grep, not repeated |
| V-18 | `rung_kinds` (not opened) | `proposals/03_PC_person_inputs_content.md:67` | `rosters.yaml: rung_kinds` = `person, hearth, community, settlement, territory, province, duchy, realm` |
| V-19 | `(Tenure, term)` for a `comply` writer; `utter`'s pair for a Proposition | `proposals/14_VERBS_SOCIAL1_B_…md:95`; `proposals/14_VERBS_MATERIAL_E_knowledge.md:124` | `write_matrix.yaml`: `(Tenure, term)` `steps: [RES]`, emits `term.renewed` (the pair exists; `comply`'s row writes `[]` today and must list it); `(Proposition, exists)` `steps: [RES]`, emits `proposition.uttered`, and `utter` writes `Proposition.exists` |
| V-20 | `present_at` is a requirement stem | `proposals/14_VERBS_MATERIAL_E_knowledge.md:61` | `data/requires.py:852` (a member of `REQUIRES_STEMS`; the rest of that mark was not read) |
| V-21 | `harness/chronicle.py` has a `--chains` reading | `proposals/01_CORE_requirements_reading_record.md:56-57` | `harness/chronicle.py:50-64`; whether it exposes the count that proposal wants was not checked |


## 5. Left marked: what this lane could not settle, and what would

Line numbers in §5 are those of the inventory, taken at `870c661`
(`runs/GROUND_ENGINE/inventory_raw.txt`); a file this lane edited has since gained two or three lines at
its head. None of these marks was changed. Nothing here is a queue: each row says what observation
would settle the mark, for whoever next relies on the claim.

| # | the marks | why not settled here | what would settle it |
|---|---|---|---|
| U-01 | **a cause that was not traced in a run**: `02_CHAR_audit.md:306` (which conjunct fails per refused verb); `03_PC_audit.md:143` (which `violence_contexts` reader admitted a fight); `07_SE_audit.md:299`, `16_PESSIMIST_SE.md:642`, `14_VERBS_MATERIAL.md:383` (why `restore` stopped executing since `24f`); `08_FI_audit.md:291`, `:395`, `08_FI_audit_addendum_B.md:139` (unsplit counts; the seven unattributed death claims); `09_WR_audit.md:264` (the one death's causing act); `16_PESSIMIST_WR.md:103`, `:540`; `16_PESSIMIST_SC.md:586`, `:708`; `16_PESSIMIST_PC.md:457`; `16_PESSIMIST_CORE.md:162`; `20_NARRATIVE_CHURN.md:287`; `16_PESSIMIST_FI.md:503` | each needs the specific run re-made with a per-act reading; none is a line to open | the lane's own probe with `aperture`'s `DECIDING READ PER REFUSAL` block or `Event.causes` walked one level, at the seed it names. `24f` is before the clone's boundary, so "what changed since" needs `git fetch --unshallow` |
| U-02 | **a behaviour over more seasons, seeds or a scale this lane was told not to run**: `01_CORE_audit.md:175` (R-04, `aperture 4 0`, run stopped); `:264` (hot-path timing on the realm); `04_MB_audit.md:580`, `:601`; `04_MB_audit_addendum_B.md:225`, `:261`, `:456`; `10_DICE_audit_addendum_B.md:257`; `16_PESSIMIST_DICE.md:655`; `16_PESSIMIST_SC.md:494`, `:613`; `16_PESSIMIST_FA.md:299`, `:328`; `16_PESSIMIST_PC.md:516`, `:721`; `16_PESSIMIST_WR.md:394`, `:502`; `16_PESSIMIST_FI.md:154`; `09_WR_audit_addendum_B.md:800`; `17_CENSUS_C1B.md:87`; `proposals/09_WR_B_weather_with_memory_and_the_year.md:159`; `proposals/02_CHAR_choice_alignment.md:87` | no long aperture run; one seed | the run each mark names. For R-04 the CORE lane's `runs/CORE/aperture_4_0.txt` exists and was not read to its end by this lane |
| U-03 | **"the 27 season-5 closures are matured `oblige` terms"**: `09_WR_audit.md:579`, `:733`; `09_WR_audit_addendum_B.md:95-96`, `:327-330`; `16_PESSIMIST_WR.md:417` | the mechanism is verified (V-07) and it is not `oblige`-specific; which Tenure kinds closed is a six-season reading | at seed 0, six seasons: for each `tenure.closed` Event of season 5 with a `matured_term`, the kind of the Tenure it names |
| U-04 | **a test's behaviour**: `01_CORE_audit.md:178` (R-07's three tests); `16_PESSIMIST_SE.md:456`, `:756` (`test_term_upkeep.py`, `test_in12_raze.py`, read from docstrings); `04_MB_audit_addendum_B.md:802` (`test_flow_skeletons.py`); `proposals/01_CORE_tests_delete_what_cannot_fail.md:105`; `proposals/01_CORE_requirements_reading_record.md:70` | this lane was told to run no pytest | the one test file, run once (CLAUDE.md §0.4 cl.2) |
| U-05 | **WITNESS's deposit rules, not opened**: `proposals/19_LACUNA_questioning_has_an_approach_and_a_cost.md:27`; `proposals/05_SC_contest_record_on_event.md:87`; `proposals/16_PESSIMIST_SE_A_…md:125`; `proposals/20_NARRATIVE_C_who_holds_what.md:71`; `proposals/20_NARRATIVE_B_what_he_was_owed.md:98`; `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md:88`, `:145`, `:149`; `proposals/14_VERBS_MILITARY_C_the_muster.md:87`; `proposals/14_VERBS_MATERIAL_A_mending.md:141`; `proposals/14_VERBS_MATERIAL_D_paper.md:160`; `proposals/01_CORE_claim_fade_as_read.md:55-56`, `:63`; `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md:65`; `proposals/16_PESSIMIST_FI_D_…md:90`; `14_VERBS_PHYSICAL.md` §5 (the residue of G-33); `14_VERBS_SOCIAL1.md:341`, `:519` | `loop/witness.py` and `epistemic.py::observers_for` were opened only at the lines named in §3. One probe was tried for the first of these and is inconclusive: at seed 0, of five `interview` Events on a living person, the interviewee holds no claim whose predicate is an interview kind, but the probe matched claims by tick and not by source Event (`g4_behaviour.out` (b)) | read `loop/witness.py:537-700` (the fan and the deposit loop) and `epistemic.py:794` on, once, for all of them: they are one function's behaviour asked sixteen ways |
| U-06 | **a loader, gate or matrix shape the proposal hopes for, not opened**: `proposals/06_FA_seat_terms_by_body_B.md:83`; `proposals/14_VERBS_SOCIAL1_B_…md:53`, `:80`, `:88`; `proposals/14_VERBS_SOCIAL1_D_…md:38`, `:114`; `proposals/14_VERBS_SOCIAL1_A_formation.md:71`, `:93`; `proposals/14_VERBS_SOCIAL1_C_…md:39`, `:60`; `proposals/14_VERBS_SOCIAL2_A_…md:50`; `proposals/14_VERBS_MILITARY_A_movement.md:104`; `proposals/14_VERBS_MILITARY_B_train.md:84`; `proposals/16_PESSIMIST_CHAR_A_…md:101`; `proposals/16_PESSIMIST_CHAR_C_…md:93`; `proposals/16_PESSIMIST_FA_B_…md:89`; `proposals/16_PESSIMIST_FA_C_under_the_seat.md:60`; `proposals/16_PESSIMIST_FA_A_…md:79`, `:115`; `proposals/02_CHAR_scar_cap_and_regard_unit.md:83`; `proposals/02_CHAR_capability_uses_table.md:104`; `proposals/01_CORE_predicates_name_their_clause.md:55`; `proposals/01_CORE_case_setup_and_beats.md:64`; `proposals/08_FI_06_testimony-names-a-hand.md:86`; `proposals/06_FA_war_lives_in_seats_B.md:98`; `proposals/06_FA_remit_grant_by_row.md:74-75`; `proposals/06_FA_office_capabilities.md:73`; `proposals/22_HAPPENINGS_C_…md:86`; `proposals/22_HAPPENINGS_D_…md:82`, `:102`; `proposals/07_SE_campaign_supply_and_muster.md:85`; `proposals/07_SE_capability_rate_B.md:46`, `:80`; `proposals/04_MB_campaign_party_economy.md:74`; `proposals/03_PC_loadout_and_carry.md:8-10`; `proposals/12_ARCS_cited_evidence.md:52`; `proposals/12_ARCS_substrate_as_ground.md:44`; `proposals/12_ARCS_arcs_as_staged_goals.md:42`; `proposals/19_LACUNA_verdict_ladder_and_reversal.md:83`; `proposals/19_LACUNA_conclusion_is_a_committed_assertion.md:78`; `proposals/17_CENSUS_REST_3_corrections.md:94`; `proposals/17_CENSUS_REST_2_wiring.md:188`; `06_FA_audit.md:278`, `:855`; `07_SE_audit.md:466`; `11_GO_audit.md:608`; `12_ARCS_adjudication.md:365`, `:414`, `:467`, `:468`; `16_PESSIMIST_CHAR.md:416`; `16_PESSIMIST_PC.md:474`; `16_PESSIMIST_GAME.md:102`, `:577`; `17_CENSUS_C1A.md:341`, `:365`; `17_CENSUS_REST.md:293` (its bracket), `:411`; `04_MB_audit.md:757`, `:788`, `:1047`, `:1239`; `05_SC_audit.md:299`, `:469`, `:652`; `02_CHAR_audit.md:385`, `:409`, `:888`; `10_DICE_audit.md:508` (the DICE addendum reports it verified; not re-opened here) | time. Each is one line or one function to open; this lane opened the ones several proposals stand on and stopped | open the named function or row. Every one of these proposals states its fallback, so none is blocked; a lane that lands one opens the line first |
| U-07 | **a proposal's own new conjunct**: `proposals/22_HAPPENINGS_C_…md:20` ("no person at `build_realm(0)` holds both conjuncts") | the conjuncts (`enmity`: wants dead **and** is hostile) are the proposal's, not yet code; there is nothing to read | the proposal's gate, once the reader exists |
| U-08 | **the institutions family's engine marks**: 55 `[UNVERIFIED]` lines under `audits/15_INSTITUTIONS_*.md` and `proposals/15_INSTITUTIONS_*.md`, about a dozen of them naming code | not reached. Their realm facts are verified (L-01, L-02, L-05) | as U-06 |
| U-09 | the "about 3.5-fold" growth of raises (`01_CORE_audit_addendum_B.md:365`) | L-24: the 2026-09-05 file set is before the clone's boundary | `git fetch --unshallow`, then the same grep at the commit `04:986` was written |

## 6. Inventory and coverage

`grep -rnEi` for the fourteen marker phrases over `audits/`, `proposals/`, `unified/` at `870c661`: **658
lines in 208 files**. By kind: 128 lines are in the institutions family (U-08, plus history and precedent,
another lane's); 158 quote the tree's own `[ASSUMPTION; …]` tags, which are the code's declared
assumptions and not a claim a suite author failed to check; 112 are coverage statements ("not opened",
`[SKIPPED: …]`) about documents; **260 are `[UNVERIFIED]` marks outside the institutions family**.

| | count |
|---|---|
| load-bearing figures checked (§1) | 24: 19 verified, 4 verified with a correction (L-04, L-10, L-21, and L-16's four definitions), 1 refuted at HEAD (L-19, already known) |
| Layer 1 passages checked (§2) | 12: 11 as quoted, 1 line corrected (A-09) |
| marks settled at the line (§3) | 35: 19 verified (G-33 in part), 6 verified with a correction, 10 refuted (five of them a proposal's hoped-for shape, whose stated fallback now applies) |
| line citations opened as cited (§4) | 21 |
| **total checked** | **92: 70 verified, 11 verified with a correction, 11 refuted** |
| marks left, grouped (§5) | 9 groups. 37 `GROUNDED` tags were written into the suite; `grep -c UNVERIFIED` outside the institutions family and this file now reads 225 lines, about a dozen of which are this lane's own `Grounded:` head lines naming the marks they settled |
| suite files edited | 35 (§8) |

**What this lane did not do.** It did not open `loop/witness.py` beyond four lines, so every claim about
what WITNESS deposits is U-05. It did not open `holonic` §43 or §45–§47, which two audits name as the
ground of their module-conformance claim (`05_SC_audit.md:652` still marks it; `07_SE_audit_addendum_B.md`
C-4 says it opened them). It ran no test. It re-ran one other lane's long probe (the King) and none of
the others; a figure in §1 "as recorded" is that lane's saved output re-counted, not a new run. It read
no document under `.designs/`, `research/` or `registers/` except the five ledger rows named.

## 7. Falsifiers (CLAUDE.md §0.1 pt 3)

- *The realm facts (L-01 to L-06).* Falsifier: `g1_realm.py` printing another count. Control that the
  probe reads the world other lanes read: its one-season hash equals the hash recorded independently
  by the determinism and the happenings lanes.
- *The King (L-18).* Falsifier: `king alive True` after season index 3 at seed 2. It printed `False`,
  and the hash equals the first run's.
- *92 % (L-15).* Falsifier: a success-kind Event of an uncontested verb carrying a degree. Zero of 421.
  Control: every verb with a `contests:` or a route that resolved shows Events with a degree (61, the
  number the determinism lane's file holds).
- *The loader refuses a routed row that writes (G-01).* Observed, on a scratch copy of
  `verb_table.yaml` with `files.VERB_TABLE_YAML` pointed at it (`g6_loader_plant.py`; the tracked file
  was read and never written). Control, the file unchanged: loads, 67 rows. `research` given a flat
  `writes: ["Record.stages"]`: `SystemExit`, *"has a `graded_inquiries` route and a FLAT `emits:` or a
  non-empty `writes:`"*. `research` given a degree-keyed `writes:`: `SystemExit`, *"has a degree-keyed
  `writes:` and no `contests:`. Nothing resolves a degree for it"*. Falsifier: either plant loading. Neither did.
- *`mustered` does not read `restrained` (G-32).* Read at `:2132-2149`, not run. Falsifier: a hand-built
  world with a detained faction member under a rung; `mustered` omits him.
- *An absence claimed by grep* (no `any:`, no `spec=`, no waiver; G-02, G-04, G-06): each is the body of
  one function read whole, not a search of the tree.

## 8. Edits made to other suite files

Each file carries a `Grounded:` line at its head naming the rows. No finding, resolution row or
proposal edit was deleted; where a mark was refuted the original claim is still legible inside the
bracket that corrects it.

| file | what changed |
|---|---|
| `proposals/18_DETERMINISM_task_draw_for_uncontested_verbs.md` | step 2 gains the two loader refusals to edit (G-01); step 3's reader path (L-10) |
| `audits/14_VERBS_MILITARY.md` | S1's two marks settled (G-01, G-14); reader path (L-10) |
| `audits/14_VERBS_PHYSICAL.md` | four marks settled (G-31 to G-34), one of them against the text; reader path (L-10); `04:237` → `04:260` three times (A-09) |
| `audits/22_HAPPENINGS.md` | §0 item 2: which gate CR-87 added (L-21) |
| `audits/04_MB_audit.md`, `audits/06_FA_audit.md`, `proposals/06_FA_office_capabilities.md` | reader path (L-10); FA also G-35 |
| `audits/08_FI_audit.md` | G-10; R-18's "flagged for Jordan" struck (G-11) |
| `audits/01_CORE_audit.md` | G-15, G-16 |
| `audits/05_SC_audit.md`, `audits/16_PESSIMIST_CHAR.md`, `audits/16_PESSIMIST_PC.md`, `audits/16_PESSIMIST_SE.md`, `audits/19_LACUNA_investigation_to_proceedings.md` | one mark each: G-17, G-19, G-22, G-23, G-21 |
| `audits/21_PROCEDURAL_GENERATION.md` | the 38th settlement rung (L-04) |
| `audits/13_SC_contest_interrogation.md`, `proposals/14_VERBS_PHYSICAL_C_looking.md` | `04:237` → `04:260` (A-09) |
| `proposals/14_VERBS_MATERIAL_D_paper.md` | G-02, G-03 |
| `proposals/14_VERBS_MILITARY_C_the_muster.md`, `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | G-04 |
| `proposals/14_VERBS_MATERIAL_C_works.md`, `proposals/14_VERBS_MATERIAL_B_stores.md` | G-05; G-13 |
| `proposals/16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` | G-06 |
| `proposals/22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`, `proposals/22_HAPPENINGS_B_the_throne_is_never_stranded.md` | G-07, G-08; G-09 |
| `proposals/03_PC_duel_round_and_approach.md` | G-12 |
| `proposals/07_SE_kernel_repairs.md`, `proposals/07_SE_population_census.md`, `proposals/07_SE_arc_needs.md` | G-18; G-24; G-27 |
| `proposals/05_SC_acquittal.md`, `proposals/02_CHAR_offer_what_can_be_done.md`, `proposals/06_FA_playable_scenario.md`, `proposals/08_FI_08_knots-season-form.md`, `proposals/17_CENSUS_REST_1_deletions.md`, `proposals/09_WR_B_draws_not_thresholds.md` | one mark each: G-25, G-26, G-28, G-29, G-30, G-20 |

**For the orchestrator, not edited by this lane.** (1) `AUDIT_BRIEF.md:77` and
`unified/DECISIONS_ANSWERED.md:7` write "§C.4" for the fidelity rule without naming `03` (A-11). (2)
The tree's own stale pointers, outside this lane's write scope: `engine/season/verb_table.yaml:1747`
cites `04:237` for a rule now at `04:260`; `engine/season/rosters.yaml:1417`, `:1424`, `:1509`, `:1566`
and `loop/effects_combat.py`'s `_eff_train` docstring spell `seam/wrappers/sigma.py::faculty` for a
function that lives in `pool.py`. (3) G-01 and G-08 change what two proposals must edit; the
unification lanes' conformance and order tables, if already written, were written before them.
