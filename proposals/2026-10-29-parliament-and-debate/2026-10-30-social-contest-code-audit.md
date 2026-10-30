# Social contest: the code against the model

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

A comparative audit of the code. The baseline is the model in `2026-10-30-social-contest-reconciliation-and-distillation.md`
§3.1 and §3.1a (items 1 to 13, built from Jordan's rulings, including R-31 to R-34 of 2026-10-30) and the kinds in
`2026-10-30-social-contest-primitives-and-kinds.md`. Three readers took the code only (documents were used to find code,
never as evidence of behaviour, CLAUDE.md §0.05): the live roll and verbs; the procedural data layer; the kernel and
everything tied to it. They ran small tests and a season probe. I opened `sigma.py:112-131`, `roll.py` and `offices.yaml`
myself; everything else is a reader's report with its path:line. One pass; its findings are not themselves audited.

---

## 1. How it functions today

**The live subsystem is one short roll, called through a three-hop lookup, fed constants.**

- **Path.** `resolve._contest` → `seam/contest.py::contest` → `sigma.resolve` → `modules/social_contest/roll.py::roll` →
  `degree_of` → `dice_engine.degree_from_net`. The three prize rows and the three graded-inquiry rows all name the same
  provider and entry: one roll with six names. The roll proper is about 25 lines; the builder in `sigma.py` about 35; the rest of the 692 lines in those files is explanatory text (about 74% of `roll.py` and `sigma.py` is docstring).
- **Inputs on every logged roll** (3 seeds, 2 seasons): `pool=2`, `opposition=None`, `leverage=0.0`, `ob=2.0`. Exceptions: 3 `speak` rolls with a small reception term (ob 1.62 to 1.98) and a few inquiry rolls with a forgery term.
- **Pool.** `_pool_of` reads only `Person.capability[VERB_CAPABILITY[verb]]` and falls back to `pool_default` (2). `VERB_CAPABILITY` has two rows (`tell`, `speak`, both `copying`). In `build_realm(0)` 0 of 83 persons carry any capability. The result is cast `int(...)` (`sigma.py:131`, read by me).
- **Obstacle.** `opposition/2`, or the default 2; minus `reception_gain·reception + proof_step·proofs`; plus `forgery_quality`; then capped by `obstacle_ceiling` (shipped value 2, `H-213`) (`roll.py:103-117`, read by me).
- **Control (run, 20,000 draws).** At 2D against Ob 2: Failure .744, Partial .187, Success .070, Overwhelming 0. Leverage of 0.25, 0.5, 0.99 and 1.0 returns a distribution identical to 0.0; only 1.5 moves it. The roll is the discrete d10 path with an integer pool and an integer obstacle, so the continuous engine is not on this path.

**Which contests execute** (seeds 0 to 2, 2 seasons each, ~14 s a season; reader's run):

| verb | prize | executes? |
|---|---|---|
| `tell` | a standing | yes, every seed: 3 to 13 `news.told` per run |
| `speak` | a matter | refused as `speech.unheard` 13 to 34 times per run; rolled 0 to 4 times; writes `[]` at every band |
| `argue` | a proposition | rolled once across the six runs |
| `determine` | a proposition | never emitted `matter.determined` in the probe (the #530 report found it once on one seed) |
| `arrest` | a standing | never |
| `open_case`, `petition`, `carry`, `convene`, `utter`, `commit` | uncontested | run |

**The procedural layer is loaded and almost entirely unread.**

- `arrangements.yaml` holds 8 rows × 13 keys, all 8 `disposal: bench` with `bench_basis: determine`; none is `mutual`, `none` or `declared`, none has a `quorum`. **Twelve of the thirteen keys have no non-test reader.** Only `disposes` is read (`effects_information.py:336,521`; `state/gate.py:257`).
- A computed `open_case` never names an arrangement, so computed docket items carry `arrangement: None` and fall to `oblige`. The rows matter only to hand-built acts and tests.
- Six speech kinds are loaded (`genres`, `min_rank`, `reachable_bands`); no reader; there is no aptness pricing in `engine/season`.
- Bench: derived (`judging_set`, `world_q.py:3687`); quorum is the number of distinct seat-holders against the fixture `bench_quorum=1` (`data/fixtures.py:961`), not the row's `quorum`.
- Propagation: `matter.determined` goes to everyone through `_ch_chronicle` (`epistemic.py:649`), with no news-speed term.

**The kernel is a separate system the game never reaches.** Importing the live path loads no `systems.social_contest*` module (`sys.modules` probe). Its only non-test caller is `degree_extension.py`, and that is called by three tests. It returns a winner side; the live module returns a `Margin`. Its kernel self-test returns `(True, [])` and `_kernel_tests` reports 389 passed; the pytest wrapper only pins that count.

## 2. Against the model

| # | model item | status | what decides it |
|---|---|---|---|
| 1 | one engine: one draw per act, `degree_from_net`, four bands, Partial writes a docket matter | PARTIAL | one draw and one ladder: yes. Partial writes no docket matter anywhere; `speak` writes `[]` at all four bands |
| 2 | one host, many data rows | PARTIAL | host and rows load; 12 of 13 keys unread; computed play never names a row |
| 3 | parties, bench, floor derived, plus `disposal` | PARTIAL | bench derived; parties are only claimants; no floor query |
| 4 | one count over `commit` edges licensing the owner's act | ABSENT | `commit` edges read only as membership; `commit_count_guard` is called only by probes; CR-34 exists only in kernel `faction.py` |
| 5 | one matter axis (mood) | ABSENT | `Proposition.mood` is a free string nothing reads |
| 6 | one speech roster, aptness priced | PARTIAL | the data exists (6 rows); no reader, no pricing |
| 7 | reception from the ledger, no stored credibility number | PARTIAL / CONTRADICTED | `reception` and `proofs` feed the roll for `a matter` only; the kernel stores a `Standing` number, which S-7 refuses |
| 8 | one disposal vocabulary | PRESENT, thin | `oblige`, `detain`, `ban`; the two `Record`-disposing rows are refused at `open_case` (a test asserts it) |
| 9 | propagation at news speed, a reaction exists | PARTIAL | witness channels exist; no news-speed term; nothing enforces a reaction |
| 10 | **capability from attribute × title × office × faction by venue (R-31)** | ABSENT | no attribute field; title and office act only through bench membership; faction is not read; nothing varies by venue |
| 11 | **sigma-leveraged engine, continuous, with named modifier sources (R-32)** | PARTIAL / CONTRADICTED | integer pool cast; leverage hard-coded 0.0 with no producer; no producer for worldly state or argument content; audience and evidence are subtracted from the obstacle |
| 12 | **one action surface, limited by contest type (R-33)** | ABSENT as a limit | one global 56-verb table, limited only by per-verb eligibility and preconditions; the keys that would limit by contest type are unread; speech kinds are not actions |
| 13 | **authority and its adjudicators (R-34), weighted by local legitimacy (R-36)** | ABSENT | no concept of authority; `bench_basis` unread; no precedence between bodies; no `mutual` row. The nearest parts: `person_q.legitimacy(p, holder, window)` (`queries/person_q.py:452`) is a per-person, per-holder Query over stance and deeds; by grep nothing in `loop/`, `decision/`, `state/` or `seam/` calls it (readers: `harness/storybar.py:281` and tests). There is **no piety Query** and no aggregate over a territory's persons; the engine forbids a Rung to own one (`state/carriers.py:1103`) |
| | structures: dyadic / mutual / bench / count | PRESENT (thin) / ABSENT / PARTIAL (one judge) / ABSENT | |

**What exists that the new rulings can stand on.**

- *Offices tie to an authority already, in two spellings.* `offices.yaml` carries 31 seats, each with a `body` or a `faction`: `Crown` (8), `Holy See`, `Cardinal of Justice` (2), `Church of Solmund`, the Inner Council, Jarl Council, and others. That is the data R-34 needs (adjudicators are holders of offices relevant to the authority); the contest path reads none of it beyond `judging_set`'s scope test. `remit_acts` has six members (`confer`, `convene`, `determine`, `dispatch`, `issue`, `revoke`) and no speech act; `speak`, `tell` and `argue` are `own`-eligible, so no office licenses speech.
- *Where an office-and-venue weight (R-31) would enter.* Three points (reader's trace): `contest_input`'s pool (`sigma.py:186`); the leverage constant (`sigma.py:191`); a new operand on `SocialContestInput` composed in `roll.obstacle`. The seat exercised (`Act.via`) is available at `resolve.py` but is not passed to `contest()` or `sigma.resolve`. The loader's refusal of a `capability` eligibility kind (`data/verbs.py:865-877`) governs verb gating only, so a venue-keyed weight would not trigger it.
- *Capability for R-31 will be thin.* The roster's attribute set is in flux (ten ruled, nine shipped); no attribute field reaches the contest.

## 3. Where it is overly complex

Ranked by lines removable with no observed function lost. Each row shows its evidence; caller counts are the readers'.

| # | where | evidence | size |
|---|---|---|---|
| B-1 | **the kernel**, `systems/social_contest/sim/contest/` | no caller in the game; 18 files, 500,205 bytes, 6,693 lines (my count); `agon_harness.py` (522), `faction.py` (154) and `narrative.py` (170) are imported by nothing | the largest unit |
| B-2 | 12 unread arrangement keys and the `_load_arrangement` that validates them | zero non-test readers; computed play never names a row | ~60 lines of loader, 277 lines of YAML |
| B-3 | speech-kinds roster and loader | zero readers outside `data/arrangements.py:252` | ~25 lines Python, ~45 YAML |
| B-4 | the capability read (`_capability`, `_pool_of`, `_opposition_of`) | returns the constant 2 and `None` for every logged roll | ~25 lines |
| B-5 | `leverage` | no producer anywhere; every roll `0.0`; a boost below 1 is inert at an integer obstacle | one input, one call |
| B-6 | `ladder.degree_ladder` fallback ("engine unavailable") | `data.rosters` imports the dice engine at top level, so the fallback cannot be reached | ~30 lines |
| B-7 | `contest()`'s `extension` parameter | never read in the body; the sole live caller does not pass it | 1 line |
| B-8 | `contest_subsystem()` | one caller (`contest.py:235`) | a wrapper |
| B-9 | S27.4 refusal evaluated at two sites (`sigma.py:273`, `loop/resolve.py:1006`) and the opposition read at two (`sigma._opposition_of`, `roll.obstacle`) | second owners of one rule each | acknowledged in the docstrings |
| B-10 | `quorum` and `bench_basis` each stated twice (row key and fixture or constant); `arrangements_without_a_disposal_opener()` has callers only in tests; `judging_set`'s `matter` parameter is unused | readers' greps | small |
| B-11 | **the knot: `obstacle_ceiling = pool_default = refusal_multiple = 2`** | with the ceiling at 2, `opposition=6` composes to 2.0 (uncapped 3.0); a hostile room cannot raise a defaulted obstacle; the S27.4 refusal can fire only for pool below 1 | where the cut costs function |
| B-12 | two identities for the module in `references/module_contracts.yaml` (live `composition_roles` at `:52`; a legacy row at `:448-470` describing the kernel, "reached live only via `emergency_council`", a name that appears in no `.py`) | | stale |
| B-13 | `BandExtension` (`dice_engine.py:95`) | the live path never passes `extension`; only the kernel and one seam test use it | noted for the port |

**Where the complexity is.** The executable live path is small; the weight is in three places: an unread data layer (B-2, B-3), a kernel no game path reaches (B-1), and explanation text. The retirement claim in `HANDOFF_SC.md` is wrong in every term: "47 files, 1.2 MB, 20+ inbound sites" is **18 tracked files, 500 KB, and 9 files that break or need repointing** (six tests, `sim_params.json` (31 rows), `value_pointer_links.json` (5 rows), and the `sim_module:` pointer in `module_contracts.yaml`); 154 files mention the path, of which 123 are design or ledger documents. One of the six tests, `test_import_cycle_game_state_npe.py`, asserts exactly three import cycles and breaks on removal.

## 4. Where it is lacking

Ordered by what the rulings require, not by effort.

1. **Capability (R-31).** Nothing varies by person: every logged roll is pool 2. No attribute, title, office or faction reaches the roll. *Decides:* a producer in `_pool_of` and a venue-keyed row.
2. **Continuous dice and obstacle (R-32).** The pool is an `int`; the obstacle is an integer in every live roll; the fractional engine exists in `engine.dice_engine.sigma_leverage` but this path does not carry it. Leverage has no producer.
3. **Modifier sources (R-32).** Producers exist for capability (thin), evidence and audience (`speak` only), and forgery quality (inquiries). None exists for worldly state or for argument content (`argue` is content-blind: the proposition is never read).
4. **Action surface limited by contest type (R-33).** The limit is absent; the global table is the surface.
5. **Authority and adjudicator basis (R-34), and its weight by local legitimacy (R-36).** No representation, and no territorial Query to scale it by (only the per-person `legitimacy`, unread by the contest path). Negotiation has no row; the crown-over-church modulation has no place to live.
6. **Count (item 4).** No licence by count; `determine` is one judge's single draw.
7. **Partial writes the docket (R-17).** `speak` writes nothing at any band; Partial opens a disposal in `determine` but forms no docket matter.
8. **Reasons to convene.** Sittings are empty; computed `open_case` is addressed to the subject themselves (reader's report; `reasons-to-convene.md`).
9. **Appeal to an authority (R-35).** `appeal_basis` is an unread key (B-2); the only appeal code that runs is the depth cap on nested contests (`ContestError`). There is no route that takes a rendered outcome to another authority, and nothing bars an immediate retry before the same bench: a second `open_case` on the same matter is the observable to test.
10. **Mutual and count structures** do not execute at all; bench structure runs through one judge that never fired in the probe.

## 5. What this leaves open

1. **The ceiling's value: direction answered (R-37), value not.** Jordan: the ceiling sits above the default so opposition can bite. The sweep arm is 3; at 3, M-7 fails for a 1D party (0.0006) and passes at 2D (0.0259). Confirm whether M-7 is re-scoped to the default pool (reconciliation §2.3).
2. **Layer 1 §A.3's wording** now that R-31 says office carries weight. A narrow wording is suggested in the reconciliation §2.3; the amendment is Jordan's.
3. **R-34's mechanism.** He stated the outcome (royal authority modulates or undermines religious authority when a royal person is involved), not the means: the crown joins the bench, may revoke, or raises the church bench's obstacle. Each lands in a different place in §2 item 13 and in the code (`judging_set`, `revoke`, `roll.obstacle`).
4. **Where an office-keyed weight enters: answered (R-38): both the roll and the obstacle.** The audit's three entry points (pool at `sigma.py:186`; the leverage constant at `sigma.py:191`; a new `SocialContestInput` operand composed in `roll.obstacle`) are all needed, the obstacle one for the defender's side.

## 6. Port cost

A port carries the dice and obstacle math (about 25 lines), a record builder over `World`, typed refusals (GDScript has no exceptions), the bench, reception and proofs Queries, the gate predicate, the disposal edge literals, `CALENDAR` with its docket slots, the five witness channels, and the verb rows with their effect bodies. The arrangement YAML is behaviourally observable only through `disposes`. The kernel needs no port if retired.

## 7. Limits

The probe is one chooser over three seeds and two seasons, not a distribution; counts are what ran, not rates. The full suite was not run. Unverified by the readers: the readers of `confidence.broken`, `grade()`'s fan-in beyond the one inquiry route, and whether `rosters.yaml:2586` and `module_contracts.yaml:451` are existence-checked. I did not re-open the readers' other path:line cites. `[CONFIDENCE: medium]` on §2's PARTIAL/ABSENT grading boundary (a reasonable reader could grade items 1, 3 and 9 one step either way); the evidence for each grade is in its row.
