# Valoria — Master Workplan v8, part 2: THE NINE — how each core tenet gets built

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). Same status and held-back list as `valoria_master_workplan_v8.md`; this part carries no decision of its own.
## Reads after `workplans/valoria_master_workplan_v8.md`. One section per row of `engine/season/requirements.yaml`.
## Grade under `CLAUDE.md` §0.2: `paper`. A row of THE NINE moves only on its own `measured:` block, which `python -m engine.season.harness.register --requirements` validates. Nothing here moves a row.

**How each section is built.** Statement (verbatim, Jordan 2026-09-05) · status and the measured reading,
refreshed from this session's instruments where they disagree with the row's `measured:` text · what
moves it (positions, with batch) · what it needs that no position owned before this plan · the design
questions the tree does not answer (stated, never answered here — `CLAUDE.md` §0, scripting drift) ·
**`met`, stated as an instrument outcome**. Where the row's own `measure:` command can no longer
discriminate, that is said, and the replacement instrument is named as a record edit owed (not made
here).

**Instrument readings used below (all 2026-10-01 unless dated).** `register --requirements` [RAN] ·
`m1_acceptance --summary` [RAN] · `corpus_run`, 143 cases, seed 0 [RAN by the orchestrator, HEAD
`0671283`; no engine change since] · `aperture 4 0`, the populated realm, 4 seasons, 2,815 acts, control
hash EQUAL [RAN by the orchestrator, same tree].

**Summary — where each row stands and what closes it.**

| row | status | the gap, in one line | closes with | Jordan-gated? |
|---|---|---|---|---|
| R-01 | not_met | the channel is present (R3 46/46 · 96/97) but no corpus reconvergence rate exists since the corpus grew | `11-fix` → `11`; then the telling workplan's T4–T5 (§0.6), `14`, `17` move it | no — measurement first |
| R-02 | not_met | same instrument as R-01; its own `measure:` is U6's | `11-fix` → `11` | no |
| R-03 | met | keep it met; its `measured:` ends 2026-09-11 | `21`-rest refresh | no |
| R-04 | partial | seats without rungs (H-163 limit 1); governance verbs refused for want of an `office` operand (H-94); `mc_v18` still runs a faction scale the loop does not join; two scales have no spec | `13d-iii`, `28-iii`, J-3, J-11 | partly (J-3 office operand; J-11 scale specs) |
| R-05 | not_met | 16 of 44 rows execute; 10 have no predicate/effect | `14`, `R05-THREAD`, `13d-iii`, `22`, `ED-FI-0009`, `20-iv`; J-1, J-2, J-3, J-4 | partly |
| R-06 | partial | no `ambitions(p)` read; the cast is one shared OUGHT in the corpus; convictions are correlated | `17`, `13`-rest; J-1 (cells) | reason 2 yes (J-1) |
| R-07 | partial | no `stance` writer that a witnessed event reaches | the telling workplan (T3a; G1, regard at read — §0.6), `20-iv`, `24g` | no — the telling path is ratified; G1 waits on its own M0b trigger |
| R-08 | partial | inclination does not break ties (alignment table sparse) | the cells commit (J-1), then H3/H9 | yes (J-1) |
| R-09 | partial | the roll varies by seed, not by person (`capability` near-empty; `lev` 0); inquiries ungraded | `13`-rest, `17`, `8`, `ED-FI-0009`, `22` | corpus-wide `capability` needs J-13 |

**Read with this, before any section:** THE NINE cannot all be met by building what this plan lists.
These depend on Jordan's content or rulings (`_part5` §J): R-05 to `met` (J-1 + J-2 + J-3), R-06 reason 2
and R-08 (J-1), R-04's realm governance verbs (J-3) and its scale roster (J-11), R-09 corpus-wide (J-13).
That is stated, not hidden. Everything that can be
built without him is in Batches 1–3.

---

## R-01 — "decisions must propagate"  · `not_met`

**Measured.** `corpus_run` [RAN]: `check R3: 46 of 46 pass` (NPC), `96 of 97` (ARC); planted control
`R3 False -> True` ("the detector works"). ⚠ **The row's `measured:` block still opens with "R3 passes
22/30 NPC and 34/59 ARC"** — the 2026-09-10 reading over the 89-case live set; its own 2026-09-30
paragraph carries the 143-case figures. The stale opening is a `21`-rest record edit. **R3 is presence
of the channel, not the behaviour the row asks about.** The behaviour — does a decision change what
follows — is the corpus-scale reconvergence rate, and **no rate exists since the corpus grew 89 → 143**:
`wd_collect.py` fails its own `probed`-must-not-depend-on-`observation_deposit_mode` assertion at the
first fixture point (`{'none': 21717, 'actor': 21954, 'total': 21897}`), so it never reaches `2x3`. The
last corpus figure (~4% later-decision divergence; 100% reconvergence at `2x3`) predates the growth.
**Realm context, not this row's `measure:`** (2026-09-30, `build_realm(0)`, 4 seasons): 188
cross-actor edges, 77% of act-events with no act antecedent, longest chain 7 across 5 actors; 19 of 46
NPCs in no edge, 10 of them officeholders acting through verbs that never execute in the realm (H-156,
H-163). No committed instrument prints those edge figures.

**What moves it.**

| position | what it changes for R-01 | batch |
|---|---|---|
| `11-fix` → `11` | produces the number the row's status rests on | 2 |
| the telling workplan's T4–T5 (§0.6) | `tell` names its hearer, contests against them and dedups by origin, so a telling is a cross-person edge to a known person; the regard `score` reads arrives with G1/G2 | carved out |
| `14` | counterparty verbs (`give`, `oblige`, `exchange`) are cross-person edges by construction; today `give`/`oblige` form 0 in the realm | 2 |
| `13d-iii` | the 10 isolated officeholders' governance acts start executing (H-163) | 2 |
| `17` + `13`-rest | distinct OUGHTs per case → distinct Q4 questions → more distinct first acts to propagate | 2 |
| J-4 (H-156) | always-refused candidates take 34% of realm scene slots; a ruling returns them to verbs that execute | 4 |

**No position owned until now:** the instrument repair (`11-fix`). **H-116** (the consequence→decision
edge is severed by a type mismatch — `belief_contradicts` narrows only on `PERSON_PREDICATES`) and
**H-111** (a refusal propagates as news, unruled) are in the row's `blocks:`; neither is in any
position. H-116 is `measured`; whether widening `PERSON_PREDICATES` is a fix or a design call is not
settled by the tree → carried as `_part4` §`11`'s post-measurement step: **if `11`'s number is ≥ 96%,
the first closed channel to name is H-116's**, because it is the registered reason a deposited
consequence cannot narrow a later candidate set.

**Design questions the tree does not answer.** (i) Whether R-01's `met` should also require a realm
reading (the isolated-officeholder set) — the row's `measure:` runs the corpus only. Answered here at
ladder step 5 (architecture): **no** — the row is measured where its `measure:` says; the realm is
context, and building an edge instrument is warranted only if a falsifier needs it. (ii) H-111 is a
real design choice (should a failed attempt be news?) — not escalated, because nothing in Batches 1–3
depends on it; it stays a registered hole.

**`met` =** `corpus_run` prints `check R3: n of n pass` on both lanes with the planted control
`False -> True`, **and** `wd_collect.py` (after `11-fix`) prints reconvergence **< 96 % at `2x3`** with
the `none ≥ default` control printed and the completeness assertion covering all 143 cases. Both in one
`measured:` paragraph, same tree.

---

## R-02 — "decisions affect subsequent decisions"  · `not_met`

**Measured.** No corpus-scale figure since 89 → 143 (the same break as R-01). The row's `~4%` is the
last number on file and "provably stale". The pinned NPC-088 2-slot slice moved 0/16 → 14/18 forks
diverging after ED-FI-0009 (2026-09-10) — a slice, not the corpus.

**What moves it.** Exactly what moves R-01's behavioural half: `11-fix` → `11` measures it; the telling workplan's
T3a–T5 (§0.6), `14`, `17`, `13d-iii` change what it measures. The channel a decision reaches a later decision through
is a ledger claim read by §F1 clause 4 (`belief_contradicts`), which reached five predicates after
ED-FI-0009; H-116's type mismatch is the registered limit on it.

**No position owned until now:** `11-fix`. ⚠ **A record edit owed:** R-02's `measure:` comment cites
`workplans/2026-09-09-r-execution-plan.md:1445-1451`, a retired file. The command itself is right; the
comment must name this plan's `_part4` §`11` instead (`register --requirements` must still exit 0).
Listed in `_part6` §H.3.

**Design question the tree does not answer.** Whether the `probed` divergence across deposit modes is
a defect in the instrument or a property of the loop. The row's own diagnosis (a deposit under
`actor`/`total` raises a new Q2 question in a later round that `none` never raises — R-03's channel
working) points to **property**, and `11-fix` takes that reading: report `probed` per arm, compute the
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
the `scene_budget = 1` arm. ⚠ The `measured:` block ends at 2026-09-11; the corpus has grown 89 → 143
and the verb table 32 → 44 since.

**What keeps it met.** Nothing builds on it; every position that touches the rounds loop
(`loop/driver.py`, `loop/deliberate.py`) must keep `pytest engine/season/tests -q -k test_u2_` green.
**`21`-rest** refreshes the `measured:` block with one re-run of the row's own `measure:` command,
dated, and changes nothing else.

**`met` (holds) =** `python -m pytest engine/season/tests -q -k test_u2_` passes, and
`python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` runs.

---

## R-04 — "strategic and management actions must be possible, ie decisions at differing scales"  · `partial`

**Measured.** The row's `measure:` line is **spent**: `corpus_run` prints no `unrepresentable scales:`
line at all since `20-ii` (all 143 cases run at four rung kinds). The row stays `partial` on its own two
stated reasons, which its `measure:` command cannot see:
1. **Seat-based acts do not execute.** `aperture 4 0` [RAN]: `levy` attempted 20, executed 0,
   `levy.unauthorized` 19 — H-163 limit 1, *16 of `build_realm`'s 19 seats carry no rung*, so the
   holder's purview is empty. `open_case` 2/45, `issue` 1/10, `determine` 0/45. `confer` 0/213,
   `establish` 0/74, `revoke` 0/45 — a different cause: no computed act names an office (H-94).
2. **The faction scale.** `engine/mc_v18.py` runs one and the loop does not join it. ⚠ **Half of this
   reason is answered by Layer 1, not by building:** `04_CODE_ARCHITECTURE.md` (RATIFIED) gives
   `Faction` a resolved view (`faction_q.resolve`) with **"no verbs"** and *"NEVER … `Act.actor` · a
   `contest` claimant"* — a faction acts as its members acting through seats (`Act.via`). So
   "no `Faction`-as-actor" is the architecture, not a gap (`_part5` §A, A-4). The other half — `mc_v18`
   still running a parallel faction scale — dies at `28-iii`.

**The six scales Jordan ruled (`requirements.yaml` `scales:`), read against the tree.** R-04 is measured
against this roster (the file says so); this is the strategic half of "decisions at differing scales".

| scale | in the loop today | what expresses it in `engine/season` | position | design gap |
|---|---|---|---|---|
| character creation / development / chronicling | **no** | `Person` carries the fields; nothing creates or develops a person | `13`-rest + `17` (a cast per case); `24g` P3 individuation | **no spec in code for creation or development** → J-11 |
| grand strategy politics | partial | `faction_q` reads; seat acts `via` offices at realm/duchy rungs | `13d-iii`, `28-iii`, `29b`; J-3 | the `office` operand (J-3) |
| social contests / debates | partial | `tell` graded through σ-leverage; proceedings (`speak`, `determine`) not yet graded | `22` → `22a` → `23` → `22b`; `2-ii` | none beyond `22`'s steps |
| mass battles / strategy warfare | seam built | `march` → `seam/wrappers/mass_battle.py`; realm: 11 declared, 11 refused at ENCOUNTER, 0 fought | `20-iv`; H-175 measurement | why ENCOUNTER refuses (pre-flight P-6) |
| personal combat / grid-based map combat with units | duel only | `fight` → `combat_seam` | `8`, `9` (J-7) | **grid-based unit combat does not exist anywhere in the tree** (`requirements.yaml` says so) → J-11 |
| settlement management / city building / domain actions | partial | `found`/`build`/`work`/`restore` (24e), cohorts (24f), `migrate` (19c) — realm: only `restore` executes (19) | `24h`, J-4 (H-156), H-165 limit 2 | a person-side works channel (H-165 limit 2) — `_part4` §`14` ride-along decision |
| investigations / detective / interactive fiction | partial | six inquiry rows; degrees Failure/none only | `ED-FI-0009` | none (ruled: the loop is the mechanism) |

**What moves it.**

| position | what it changes | batch |
|---|---|---|
| `13d-iii` | every seat gets a rung anchor → `levy`/`issue`/`open_case` pass `authority`; `determine`'s bench resolves | 2 |
| `28-iii` (+ `29b`) | `mc_v18` and its faction scale are gone; "not joined" stops being true by deletion | 1 |
| `20-iv` | a garrisoned defender changes a field's outcome; if ENCOUNTER's refusal is a garrison/defender gap, marches start being fought | 1 |
| `22` | `determine` reaches a decision in the realm (THE BAR) | 3 |
| J-3 | `confer`/`establish`/`revoke` become formable from computed play, or are withheld | 4 |

**No position owned until now:** `13d-iii` (H-163 limit 1 — the row's own named cause); the H-175
measurement (why `corpus_run`'s 143 cases never give `march` a referent while the realm does) — placed
as pre-flight P-6's sibling, a read, not a build.

**Design questions the tree does not answer** → `_part5` §J: **J-3** (the `office` operand),
**J-11** (two of Jordan's six scales — grid-based unit combat, and character creation/development —
have no mechanism spec in code; the only grid references are quarantined UI documents, reference
only). Until J-11 is answered, R-04 **cannot be `met` on the scale roster**, and this plan schedules no
build for either scale.

**`met` =** (1) `python -m engine.season.harness.aperture 4 0` shows every seat-gated remit verb
(`levy`, `issue`, `open_case`, `determine`, `convene`, `dispatch`, and — after J-3 — `confer`,
`establish`, `revoke`) executing ≥ 1 with `Act.via` set; (2) `engine/mc_v18.py` absent and
`test_faction_q.py` green; (3) every `scales:` row in `requirements.yaml` reads `in_loop` with an
execution artifact named. ⚠ **Record edit owed** (`21`-rest, after `13d-iii`): R-04's `measure:` must
name the instrument that reads reasons (1)–(2) — `aperture 4 0`'s per-verb lines — since
`corpus_run`'s line no longer discriminates. Conjunct (3) cannot be met until J-11.

---

## R-05 — "all verbs must be built out, and doing so requires planning out all the different scales of play required in a season"  · `not_met`

**Measured.** `corpus_run` [RAN]: `WHERE THE 44 GO: 10 have no predicate/effect · 10 foldable but never
even attempted · 8 attempted and always refused · 16 executed`. The second clause ("planning out all
the different scales") is answered by Jordan's `scales:` roster (R-04's table above).

**Every verb that does not execute, and the position that owns it.** This is the R-05 build plan.

| verb(s) | corpus class | realm (`aperture 4 0`) | why it does not execute | owner |
|---|---|---|---|---|
| `repudiate`, `succeed`, `tie / knot`, `forge`, `exchange`, `carry` | no predicate/effect | never attempted | unbuilt (W31(a)/(b)) | `14` |
| `comply`, `evade / defy`, `construe` | no predicate/effect | never attempted | ED-IN-0210's fork (one `comply` or two) | `19b` ← J-2 |
| `thread_read` | no predicate/effect | never attempted | Thread Sensitivity has no operand in the closed eight (H-85) | `R05-THREAD` (rides `14`; answered A-7) |
| `give`, `oblige` | foldable, never attempted | formed 0 | counterparty: untyped `give` gets `{}` from `operands_for`; `options.py` binds one referent to every slot | `14` (distinct operand per slot; counterparty in the fold) |
| `destroy_record` | foldable, never attempted | never attempted | `eligibility: hold:<record>` + presence — unformable for everyone | `14` (A-13) |
| `confer`, `establish`, `revoke` | foldable, never attempted | 0 of 213 / 74 / 45 | no computed act names an office (H-94) | J-3 |
| `determine` | foldable, never attempted | 0 of 45 | referent coincidence + quorum (H-163 limits 2–4, H-161) | `13d-iii` (bench), `22` steps 11–12 |
| `open_case`, `convene` | foldable, never attempted | 2/45 · 5/14 | rungless seats; few corpus seats | `13d-iii`, `17` (cast seats offices) |
| `march` | foldable, never attempted | declared 11, refused at ENCOUNTER 11 | corpus: no referent (H-175); realm: ENCOUNTER refusal (cause unread) | P-6 → `20-iv` |
| `levy` | always refused | 0/20 (`unauthorized` 19) | H-163 limit 1 | `13d-iii` |
| `dispatch`, `survey` | always refused (corpus) | 2/27 · 5/123 | rare; seats (dispatch) / referent (survey) | `13d-iii`, `17`; J-8 decides `dispatch`'s remit |
| `commit` | always refused | 0/154 | its own operand gap; crowds `release` (H-156) | J-4 |
| `found`, `build`, `work` | always refused | 0/70 · 0/60 · 0/144 | no computed act declares a works (H-165 limits 2–3) | `14` ride-along decision (H-165 limit 2) + J-4 |
| `migrate` | always refused | 0/131 | capacity/travel refusals (H-168) | J-4 (shares H-156's shape); re-measure after `13d-iii` |
| `kill`, `wound`, `challenge`, `accept` (rows not yet in the table) | — | — | the verb split rides the cells commit | J-1 |

**No position owned until now:** `R05-THREAD`; the `found`/`build`/`work` works channel (H-165 limit
2); `destroy_record`'s formability. All three are placed at `14` (`_part4`), each as a decision taken at
ladder step 4 or 5 with its precedent named, or declined with the reason recorded.

**Design question the tree does not answer.** Whether "built out" means *executes in computed play*
(DONE-realm) or *a dedicated test executes it* (DONE-test). R-05's `measure:` is `corpus_run`'s executed
set, and U7's own acceptance said **"≥ 1 world — in the corpus, not merely in a hand-built `Act`"** — so
the tree already answers it (ladder step 4, U7's precedent): **computed play**. This plan adopts that.

**`met` =** `corpus_run`'s `WHERE THE <n> GO` line reads `0 have no predicate/effect · 0 foldable but
never even attempted · 0 attempted and always refused`, **or** every verb in the latter two classes is
shown executing ≥ 1 in `aperture 4 0` (seat-gated verbs the corpus does not seat), with the verb named.
After J-1 the table holds `kill`/`wound`/`challenge`/`accept`; `<n>` moves and the line must still read
zeros.

---

## R-06 — "characters must be robustly built with goals, ambitions, convictions, moral values, etc"  · `partial`

**Measured.** `corpus_run` [RAN]: `RANKING DISCRIMINATION 15..21 of 31 candidates carry a nonzero
conviction score; the rest TIE and the tie is broken BY THE DRAW`. Two stated reasons the row is not
`met`: (1) `ambitions(p)` does not exist ([SETTLED: `grep -rn "def ambitions" engine/season` finds
nothing]) and the corpus cast is one shared OUGHT; (2) the convictions are correlated — nine of thirteen
within 60° of the mean vector (U3) — so people differ from their own alternatives more than from each
other. Realm (2026-09-30): 46 distinct ambitions; 44 of 46 still live after 4 seasons, none laid down;
the OUGHT has no condition under which it comes true (closed at ladder step 3: an OUGHT is an uttered,
immutable Belief; it ends by `release`, `repudiate`, or death).

**What moves it.**

| position | what it changes | batch |
|---|---|---|
| `17` | `queries/person_q.py::ambitions(p)` — a person-side READ over live `commit`→OUGHT Tenures; `build_at` seats the `cast:` | 2 |
| `13`-rest | 41 NPC + 97 ARC `cast:` overlays: distinct OUGHTs and `capability` per case | 2 |
| `14` | `repudiate` gets its effect: the second voluntary ender of an ambition | 2 |
| cells commit (J-1) | the fifteen pursuits × seven axes; re-cells alignment over 43 verbs — the only thing that moves reason (2) | 4 |
| `12` / `12e` (after J-1) | scar rebuild (H3), crisis threshold (H13) | 4 |

**No position owned until now:** nothing new — reason (1) is `17`'s, reason (2) is J-1's.

**Design question the tree does not answer.** Whether an OUGHT can be satisfied (the row's own
"WHAT WOULD OVERTURN THIS PARAGRAPH"). The tree closes it at step 3 (no condition exists); this plan does
not re-open it. A ruling otherwise would be new design and would be Jordan's to start.

**`met` =** `corpus_run`'s `RANKING DISCRIMINATION` line shows a nonzero conviction score on every
candidate a person is offered (no tie broken by the draw when the person has a reason), **and**
`python -m pytest engine/season/tests -q -k 'ambitions or cast'` passes with `DISTINCT EXECUTED SETS`
above the pre-cast arm, **and** the J-1 conviction-spread falsifier (`conviction_spread.py`, Jordan's
faith pair far apart, no more than a declared share of pursuits within 60° of the mean) passes. The
third conjunct is Jordan-gated.

---

## R-07 — "characters must have memories and feelings and attitudes and relationships, and they must only have imperfect knowledge"  · `partial`

**Measured.** Imperfect knowledge holds structurally (`choose` takes no `World`; `View` capped;
`LedgerReader` own-ledger only) — row's `measure:`
`pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'`. Memory holds
(the ledger; a death is witnessed and occasioned two later acts in the realm run). **Feelings,
attitudes, relationships — `Person.stance` — have two writers, neither reachable by a witnessed event:**
`harness/populated.py`'s build-time loyalty seed, and `loop/effects_combat.py::_eff_march`'s M4
losing-side write, reached by nothing in the realm run because no field was fought. Position `10`'s
`tell`→stance write was built and reverted (H-79: every write target breaks `claim_subjects`).

**What moves it.**

| position | what it changes | batch |
|---|---|---|
| the telling workplan (§0.6) | **regard computed at read** — `stored stance + judged deeds + told valence` (G1), the teller's relation in the weighed reader (T3a) and a teller's `record` (T6). No stance write by `tell` | carved out |
| `20-iv` | fields get fought → `_eff_march`'s existing M4 stance write is reached in the realm | 1 |
| `24g` (J-6) | the bodies clock: deaths with a cause, P3 individuation at CENSUS | 4 |

**⚠ Withdrawn, with the reason.** This plan first re-scoped `10` to a stored stance write on a resolved
`fight`'s subject. The ratified telling workplan computes regard at read and counts a judged deed there
(G1), so a stored deed write would be a second route to the same fact — an S defect (§0.06). The stored
half of regard keeps exactly its two writers: the build-time loyalty seed and `march`'s M4 write.

**`met` =** the row's `measure:` passes, **and** after two seasons of `populated.build_realm(0)`, two
hearers who hold different claims about one C — or the same claim from tellers they regard differently —
read different `regard(p, C)` (asserted `>= 1` such pair, so a world where nothing was told fails),
**and** `_eff_march`'s stance write is reached by a fought field (`20-iv`). The instrument for the first
conjunct is the telling workplan's G1 falsifier; the row flips on its own `measured:` paragraph quoting
both.

---

## R-08 — "decisions must not be omniscient and perfectly rational — characters may not make the optimal decision based upon their epistemic knowledge and personal inclinations"  · `partial`

**Measured.** Non-omniscience holds (R-07). *A person declines the optimum*: built (U4,
`softmax(score / choice_temperature)` via Gumbel; falsifier
`test_u4_the_choice_is_sampling_and_the_argmax_is_its_zero_temperature_control`). *Inclination breaks a
tie*: **not built** — the alignment table is sparse, so ties are broken by the draw (`corpus_run`
RANKING line, as R-06). `needs_jordan: false` on the row is correct: what remains is build work behind
J-1, not a question about R-08 itself.

**What moves it.** Only the cells commit (J-1): `alignment` re-celled over 43 verbs × 7 axes makes most
candidates carry a nonzero score, so the person's inclination — not the draw — orders them. Then H3
(scar) and H9 per `_part5` §B4. **Nothing buildable in Batches 1–3 moves R-08**, and this plan does not
pretend otherwise. (The telling workplan's weighed reader (T3a, T6) makes what a person believes depend on whom they
trust, and G1/G2 put regard into `score`; contributors, not the row's named gap.)

**`met` =** `corpus_run`'s RANKING line shows, for each sampled person, that every tie among offered
candidates is between candidates with equal *nonzero* score (the draw breaks only true indifference),
and the U4 test stays green. Reads after J-1.

---

## R-09 — "chains of events within a scene are probabilistic, not deterministic"  · `partial`

**Measured.** A roll exists and reaches the game: `tell` → σ-leverage provider (`net = roll_net(pool)
+ net_boost(lev, pool)`), graded. `corpus_run` [RAN] `DEGREES RESOLVED {'Failure': 145, 'Felled': 10,
'Partial': 26, 'Success': 8, 'Untouched': 9, 'Wounded': 14}` — two graded chains (`tell`, `fight`), no
inquiry graded. Why `partial`: the roll varies by SEED, not by PERSON. ⚠ The row's text "`Person.capability`
is empty on every corpus person" is **stale since position `13`** (one `capability` value authored,
2026-09-28 plan §8.7) — a `21`-rest record edit; the substance (near-uniform pools) still holds. `lev`
is 0.0 with no producer, by design (a fabricated leverage is a number nobody chose).

**What moves it.**

| position | what it changes | batch |
|---|---|---|
| `13`-rest | `capability` authored per cast member → `_pool_of` varies by person | 2 |
| `17` | seats the cast those overlays author | 2 |
| `8` | the wound-count band edge becomes data (H-98(b)) — band provenance, no new chain | 2 |
| `ED-FI-0009` | a degree producer for the six inquiries — a third graded chain | 2 |
| `22` | `speak` graded (`contests: a matter`) — a fourth | 3 |

**No position owned until now:** none.

**Design questions the tree does not answer.** (i) **`capability`'s scale and source** — H-126/H-127
are `assumption`; the one authored value (`NPC-088`'s `3`) was a named judgment call, not canon. `13`-rest
authors a `capability` only where a magnitude has a source; the scale is **J-13**, and without it R-09
varies by person only in the few cases whose text names a covered vocation. (ii) Where `lev`
(σ-leverage) comes from for a person. The
row records it as deliberately zero. Nothing in code specifies a producer; this plan schedules none and
names it as an open design input to `22` step 15 (the obstacle ceiling and `sigma_leverage` sweep),
which is the first position whose falsifier reads leverage.

**`met` =** `python -m pytest engine/season/tests -q -k 'we_only_a_verb or u1_'` passes, **and**
`python -m engine.season.harness.headless --seasons 2 --seed 0` shows two persons with different
`capability` resolving the same contested verb at different pools, **and** `corpus_run`'s `DEGREES
RESOLVED` line is non-empty for at least one non-combat verb besides `tell` (an inquiry or `speak`).
