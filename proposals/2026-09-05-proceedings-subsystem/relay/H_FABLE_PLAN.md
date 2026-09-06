> ## RELAY STAGE H · THE PLAN — `fable`, read-only, planning only
> ## Status: **PROPOSED (2026-09-06). NOTHING HERE RATIFIES ON MERGE.**
>
> Planned the work from *"fears"* to now against the design owner's comments across that span.
> `CLAUDE.md` §10 licenses `fable` for read-only audit, planning and guardrail work and **never for
> authorship**, so this is the plan; `19_PLAN.md` writes it up and verifies its load-bearing claims.
>
> **Two rulings arrived mid-plan and are folded in**: that this subsystem owns all social contests,
> and that the multilateral tally and the debate score are accepted shapes.
>
> ⭐ **It corrects the ordering it was given, twice, from the code** — the fan-out must narrow BEFORE
> attribution (at total the cap is already saturated, so measuring there measures the flood), and the
> ledger-cap debt is payable in Phase 1 because it is not a proceeding question at all.
>
> ⭐ **And it corrects `18_FINDINGS.md`**: the severity carrier that document proposed is an inert
> field with one occurrence in the whole module. Verified by hand before acting on it.

---

# PLAN · Improving the proceedings subsystem, from "fears" to now

**Path legend (all citations below use these short names; every path is absolute).**
- `shape.py` = `/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/shape.py`
- `headless.py`, `corpus_run.py`, `test_tracer_is_honest.py`, `combat_seam.py`, `register.py` = same directory as `shape.py`
- `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`, `hole_register.yaml` = `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/`
- `01_AXIOMS.md`, `04_CODE_ARCHITECTURE.md` = `/home/user/ttrpg/proposals/2026-09-03-meta-architecture/`
- `dice_engine.py`, `sigma_leverage.py` = `/home/user/ttrpg/engine/autoload/`
- `NN_*.md` and `relay/*` = `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/`

Both coordinator rulings are folded in: ownership is settled (manifest row and prize repoint are instructions 8–9; the two-owner hedge is gone from every step it touched), the multilateral disposal and the in-run debate score are accepted (instructions 15 and 14c), `records_dissent` is withdrawn from the cut list, every refusal in the directory is re-sorted in PART 6R, and `AX-1` holds throughout — the one mechanism adjacent to it is escalated in PART 7, not assumed.

---

## PART 1 · THE SHAPE OF THE WORK

This plan makes the ledger able to hold a reading of a person, then makes this subsystem the single owner of every social contest through the seam, then joins the two so the obstacle reads what the room holds — in that order, because the first is measurable today with the existing harness, the second is the ruling, and the third is where the flowchart becomes a game. It treats the design owner's four comments as the spec: aggregates inside a proceeding are free, the zero-primitive count is a tiebreak and never a reason to ship a worse mechanism, a fear is pressed and a secret is spent, and the seam (read-only projection, no write token, Events out, a Margin back) is the only hard boundary. It refuses to add a stat, a meter, a bias field, a stress scalar, a turn limit, a second ladder, a per-pair table, a `Proceeding` object, a hook-call verb, a second `if` in the seam, or anything that acts through another person. It cuts three arrangement keys, two dead carriers, one dead channel, and one inert field, and it names the six measurements that must run before anything is built on top of them. Every step ends in a run, a hash, or a red-then-green test, and a document with a status line counts for nothing.

---

## PART 2 · THE CRITICAL PATH

`18_FINDINGS.md` PART L orders the work O-1 → P-42 → (O-6 + fan-out) → O-3 → roster → O-2 → `Tenure.term` → O-7. `12_BUILD_ORDER.md:25` orders the seam 0 → 1 → 2 → 6 → 7 → 8 → 9. Neither ordering is inherited here; both were tested against what each step actually needs to *run*, and the result is two independent stems that join once.

**Stem A (the season loop's WITNESS/DELIBERATE barriers) and Stem B (the seam) do not depend on each other to execute.** Everything in Phase 1 runs through `headless.build_world` + `SeasonDriver.season` today with no proceeding in the world; everything in Phase 2 runs through `contest()` with an empty ledger. They meet at `reception` (O-2), which needs both a composed obstacle to enter and attributed, differentiated claims to read.

**Two corrections to the findings' order, both from the code:**

1. **Fan-out comes off `total` before O-1, not after.** O-1 doubles deposits per witnessed speech (`relay/E:44`), and the risk is ledger inflation at cap 200 (`shape.py:1772`). But at `total` the cap is *already saturated* — `test_tracer_is_honest.py:3084-3090` asserts the control arm's fullest ledger sits at exactly 200 — so measuring O-1's inflation at `total` measures the flood, not O-1. `presence_only` cuts deposits by more than 4× (`:3070-3074`). Narrow first, then attribute, then measure.
2. **P-42 is not a proceeding question.** The concession is the fiction; the mechanism is the eviction key `confidence × (when + 1)` (`shape.py:6443`). That key is measurable on any planted firsthand claim in the NPC-088 world, so the ledger-cap debt is paid in Phase 1, before a single proceeding exists — and the prediction is sharp enough to falsify (PART 5, M-1).

| phase | what it delivers | boundary argument | is it the game? |
|---|---|---|---|
| **1 · The ledger holds a reading of a person** (steps 1–7) | fan-out narrowed · attribution · `told_by` minted · the P-42 measurement · the want/fear term with habituation · the fear press traced to its terminus · the speech-kind roster | Runs on the existing harness with no seam. It is where the owner's central ask (the character model) lives, and it makes the *world* a story-generator (emergent mechanisms 1–4 of `18:410-419`) before any proceeding runs | **the world becomes a story instead of a log** |
| **2 · The subsystem owns the contest** (steps 8–16) | the manifest row and prize repoint · `judging_set` · the arrangements loader with the multilateral disposal · `release` and `convene` · the composed Ob and the licence `BandExtension` · `speak` and `determine` · `proceedings.run` with the in-run aggregates · the bar (step 9 of `12_BUILD_ORDER`) · `disposal_reach` in code | Nothing here needs Phase 1 to *run*; all of it needs Phase 1 to be a *game*. Doing Phase 1 first means the bar's first end-to-end proceeding is run against a world whose ledgers already differ, so the run is a game-shaped test rather than a flowchart test | **the structure exists and resolves** |
| **3 · The room reads you** (steps 17–21) | `reception` reads the bench's ledgers · the source ordinal and the mirror test on proofs · the product deposit closing P-05 · route erosion · Failure severity by observer set | The join. `reception` is the only hidden load-bearing term (`15_WHY_IT_IS_A_GAME.md:55-66`); it cannot exist before both stems | **THIS IS THE PHASE THAT MAKES IT A GAME** |
| **4 · Forty seasons stop looking like four** (steps 22–27) | `Tenure.term` (the one field) with the return day and DEFY · pressure crossings · conviction moved by consequence · the forged record examined · cross-season momentum priced · the dead-carrier deletions | Polish in the exact sense that the subsystem is a game without it — but without it every loop damps and season 40 resembles season 30 (`10_LOOPS_AND_GAPS.md:4-5`). `Tenure.term` touches the substrate (`write_matrix`, the gate), so it is sequenced after the game exists | polish that prevents convergence |

---

## PART 3 · THE INSTRUCTIONS

Conventions: **Cost** is in the audit's units (`relay/E:38`) — fields · verb rows · roster members · obstacle terms · score terms · magnitudes · Event kinds — plus grammar entries and arrangement keys where they apply. Every injected magnitude gets a `hole_register.yaml` row with `site:` and three `sweep:` points, or `python register.py --check` goes red on R2 (`register.py:28-31`). Every new sweep must be *executed* by a test in the shape of `test_tracer_is_honest.py:3965` (`test_w9_the_sweeps_the_register_declares_are_executed`), because declared-and-unrun sweeps are the laundering that test exists to stop.

### PHASE 1 · THE LEDGER HOLDS A READING OF A PERSON

**1. Take fan-out off `total`.**
- **Change:** `shape.py:1798` `fan_out_mode="total"` → `"all_five"`. `total` stays in the roster as `H-33`'s control arm (`hole_register.yaml:358-369`). Do **not** touch `witness_channels` in this step — it is a sweep's arm set.
- **Why here:** Every secret, lie and rumour is impossible while everyone holds everything (`18:313-316`). It is one fixture. And it is the precondition for measuring O-1's cost at all (PART 2, correction 1).
- **Artifact:** `test_w6_h33s_declared_sweep_runs_and_the_deposit_count_falls` (`test_tracer_is_honest.py:3058`) stays green with the arms re-labelled (`all_five` is now the default, `total` the control). Add one assertion: after two NPC-088 seasons, there exist two persons whose ledgers differ in at least one `(subject, predicate)` pair — *the first secret in the world*. `python corpus_run.py` re-baselines; the deltas are printed, not hidden.
- **Cost:** 0 of everything. A default flip with an existing sweep.
- **Breaks if wrong:** The propagation loop `H-102` (`hole_register.yaml:1345`) may starve — `tell` becomes the only transport and `tell` requires `own_ledger` (`verb_table.yaml:475-482`). If R3 (claim → question → act) drops to zero on the NPC lane, the narrowing is too tight and `presence_only`/`all_five` need `post_remit` and `document_key` to actually match someone.
- **Falsifier:** the two-ledgers-differ assertion is green at `total` (it cannot be — `total` fans identically) or red at `all_five`. Or: R3 on NPC-088 falls from 30/30 to 0.

**2. O-1 · A witnessed act that names a subject deposits the actor too.**
- **Change:** a fourth member of `rosters.yaml:250-303` `claim_subject_rules` — call it `named_and_actor` — under which `shape.py:4203-4205` (`out = [r for r in (refs or ()) if r]`) becomes `out = [e.subject] + [r for r in refs if r and r != e.subject]`. Make it the default at `shape.py:1841`; `both` stays as the arm whose measured reason for *replacing* is recorded at `rosters.yaml:294-299`. Under `T-d`/`H-107` the tracer's `Event.subject` is still the actor (`shape.py:2113`, `hole_register.yaml:1458`), so nothing new is read.
- **Why here:** Every mechanism in this plan is a reader of the row this writes (`18:28-30`). With step 1 done, its inflation is measurable.
- **Artifact:** extend `test_w9_the_sweeps_the_register_declares_are_executed` (`:3965-3980`): under `named_and_actor`, the bailiff's ledger holds a claim with `subject == p_carin` for a witnessed speech whose payload named a Record; under `both` it does not. The H-79 sweep now has four arms and all four run.
- **Cost:** 1 roster member. Deposits per witnessed speech double (`relay/E:44`).
- **Breaks if wrong:** the exact defect `rosters.yaml:294-299` measured — `H-40`'s decay sweep goes inert because the extra claims evict the decayed ones first. Step 3 exists to see it.
- **Falsifier:** `test_wb_h40s_decay_sweep_is_re_run_in_every_arm_and_goes_inert_at_total` (`test_tracer_is_honest.py:6735`) goes red in the `actor` observation arm under `named_and_actor` at `all_five`. If it does, the fix is the eviction key (step 3's finding), not reverting the rule.

**3. Measure P-42 with steps 1–2 on: does a witnessed act about a person survive the cap?**
- **Change:** no mechanism. One test, `test_p42_a_witnessed_act_about_a_person_survives_the_ledger_cap`, beside `:6735`. Build NPC-088 at seed 0 with `fan_out_mode=all_five`, `claim_subject_rule=named_and_actor`; run season 1; record the id of the bailiff's claim `(p_carin, speech.made, when=1)`; run seasons 2..12; report the first season it is absent; sweep `ledger_cap` {100, 200, 400} × `claim_decay_per_season` {0, 5, 20}. Print the 9-cell table in the test output.
- **Why here:** `18:511-512` — the inflation is a *measured* risk. And the prediction is sharp: the eviction key `c.confidence * (c.when + 1)` (`shape.py:6443`) is recency-dominated — a season-1 claim at confidence 100 has key 200, a season-10 claim at 100 has key 1100 — so **the cap forgets the oldest thing first regardless of what it is about**. That is exactly the wrong thing for a recurring cast pricing each other across seasons (`03_PARAMETERS.md:317-323`).
- **Artifact:** the printed table; the register row `P-42` in `10_LOOPS_AND_GAPS.md:100` moves from *open* to *measured* with the table's numbers, and `H-104` (`hole_register.yaml:1371`) gains the cite.
- **Cost:** 0.
- **Breaks if wrong:** nothing — it is a measurement. What it *decides* is whether step 3b runs.
- **Falsifier (of the prediction):** the claim survives 12 seasons at cap 200. Then the cap is not the problem and no eviction change is warranted. **If it evicts before season 4, do 3b.**
- **3b (conditional):** weight the eviction key by subject kind — `key = confidence × (when + 1) × (person_subject_weight if c.subject in w.persons else 1)` — one magnitude, injected and swept {1, 2, 4}, register row. This is the precedent's #4 mechanism (identity-embedded memory outlives event memory, `relay/G:120`) applied to eviction rather than to a field. **Not** a cap raise — `18:106-113` says why.

**4. O-6 · `told_by` is minted from the channel, and a telling carries the teller's confidence.**
- **Change:** three lines in the deposit. (a) `observers_for` (`shape.py:4430-4453`) returns `(pid, channel)` pairs rather than pids, `channel` being the first live predicate that admitted the person in a declared precedence `[co_located, witness_key, document_key, post_remit]` (a fifth entry on `rosters.yaml:382` `witness_channel_predicates`, `precedence:`). (b) `shape.py:6325-6327` sets `src` from a roster map `channel_source: {co_located: firsthand, witness_key: firsthand_via_knot, document_key: told_by, post_remit: told_by}` — and, for an Event whose kind is in a one-member roster `transport_kinds: [news.told]`, co-located hearers deposit `told_by` (they heard it told; they did not see the thing). (c) for a `news.told` Event, `conf` is the teller's own held confidence on the told subject (`max(c.confidence for c in teller.ledger if c.subject == subj)`), not `confidence_default` — which is what `14_THE_WORLD_IN_THE_ROOM.md:166` already claims happens.
- **Why here:** hearsay does not exist (`18:20-21`); `standing_of` reads `told_by` and never sees one (`shape.py:4011`); the source ordinal O-2 and O-10 weight by is never minted.
- **Artifact:** a test: Carin `tell`s the warden about the record; the warden's ledger holds `(record, news.told, source=told_by, confidence=Carin's)`; the bailiff, who witnessed the *speech* directly, holds `firsthand`. And `standing_of(p_carin)` returns something other than the maximum gap for the first time (`shape.py:4013-4014` returns `scale` when `paired == 0`).
- **Cost:** 0 fields · 2 roster members (`precedence`, `transport_kinds`) · 1 roster map (`channel_source`) · 1 signature change on `observers_for`.
- **Breaks if wrong:** if `post_remit` maps to `told_by`, an office-holder who *was in the room* is downgraded — precedence (a) prevents it; test both channels admitting one person.
- **Falsifier:** every deposit in a 3-season corpus run is still `firsthand` (grep the ledgers); or a `told_by` claim carries `confidence == 100` for a teller who held it at 60.

**5. O-3 · The unmet-want term, with the habituation clause inside it.**
- **Change:** one person-side term in `score` (`shape.py:3502-3506`). For each live `commit` Tenure whose object is an OUGHT Proposition (the same walk as Q4, `:3929-3937`), evaluate `(subject, predicate, value)` as a typed cell against `LedgerReader(p.ledger)` — the call `belief_contradicts` makes at `:3860-3861`. If the want is KNOWN-FALSE or UNKNOWN, boost candidates whose subject is the want's subject by `want_boost`. **Polarity:** a fear is `value=False` (`Proposition.value: Any`, `shape.py:2432`), satisfied by default, and boosts only when a claim lands making it KNOWN-FALSE — so a fear names the *precursor* (fear the case, not the sentence; `relay/E:364`). **Habituation:** `boost ÷ (1 + Σ c.confidence/100 for c in p.ledger if (c.subject, c.predicate) == (want.subject, landed.predicate) and c.when < landed.when)` — a count over the holder's own live rows discounted by their decayed confidence, no scalar stored (`relay/E:338, 346`).
- **Why here:** initiation — the one thing no character does today (`18:414-415`); the second press is refuted as identical without this clause (`relay/E:338`). It reads only person-side state, so `T-f` holds.
- **Artifact:** a test with two NPCs at seed 0, one committed to `OUGHT(hold(X)=True)` and one to `OUGHT(hold(X)=False)`, both witnessing the same `X` event: their ranked candidate lists differ in first position. A second test: press the same fear twice across seasons; the boost on press 2 is strictly less than press 1 (print both). **The sweep runs against `question_aggregation_rule="all"`** (`shape.py:4474-4500`; `rosters.yaml:217-231`), not `first`, or it measures the fixture (`18:507-510`).
- **Cost:** 1 score term · 1 magnitude (`want_boost`, swept three points, register row) · 0 fields · 0 verbs.
- **Breaks if wrong:** large enough to beat `date_due`, characters become monomaniacal; small enough not to, it is `urgency` again — a term that never moves a ranking (`shape.py:3449-3468`). **Both ends of the sweep must flip at least one verdict**, or the magnitude is inert (`04_CODE_ARCHITECTURE.md` G.4.5: a verdict that flips across the sweep is the finding).
- **Falsifier:** the two-NPC test produces identical rankings at every sweep point; or the press-2 boost equals press-1.

**6. The fear press, run to its terminus, with no new mechanism.**
- **Change:** none. One seeded 8-season test: A holds a claim on B's committed fear F (A witnessed the `commit`); A `speak`s/`utter`s F in B's hearing each season. Observe: press 1 → B's Q2 fires (`shape.py:3900-3903`, F ∈ `mine`), B's promoted candidates are about F's subject; press 2 → boost falls (step 5); press N → B's `repudiate` (`harm_borne: 0.8`, `rosters.yaml:934`) outscores the habituated boost, B repudiates the commit, F leaves `mine`, and press N+1 lands a claim and raises no question (`relay/E:343`). Print the season of repudiation. Then the symmetric test: A presses the wrong F (not in B's tenures) — no Q2, and with step 2 the room holds `(A, speech.made)` ×1 for nothing.
- **Why here:** it is the owner's correction (*"fears are leverage that you can press"*) executed rather than described, and it is the audit's model tested end to end. It also proves the terminus needs nothing new.
- **Artifact:** the printed press table (season · B's top candidate · boost value · Q2 fired?) and the repudiation season, at three `want_boost` points.
- **Cost:** 0.
- **Breaks if wrong:** if B never repudiates at any sweep point, the conviction baseline never crosses the boost and the lever is infinite — the precedent's "escalation with no terminus" (`relay/G:130`). Then the habituation denominator is too weak.
- **Falsifier:** press N+1 fires a Q2 after repudiation; or the wrong-F press fires one.

**7. Author the `speech_kinds` roster, with reachable bands.**
- **Change:** `rosters.yaml` gains `speech_kinds` — promised at `04_VERBS.md:211-216` and absent (`17_PLAYABILITY.md:1003`). Columns: `kind` · `apt_genre` (set over `{forensic, deliberative, epideictic}`) · `apt_rungs` (set over the ladder roster) · **`reachable_bands`** — the figure adjudication's finding that `impugn` is Partial by construction and `object` at the procedural rung has no Success (`relay/F:547-552`; `18:157-161`). Ten members: propose · concede · refute · define · construe · amplify · object · impugn · pre-empt · recapitulate. The two starred ones are not rostered (`withhold` is priced by step 14d; `elicit-in-room` is `interview`).
- **Why here:** needed regardless of anything else, it is data, and steps 12–14 read it.
- **Artifact:** the loader refuses an eleventh kind whose `reachable_bands` names a band outside `DEGREE_LABEL` (`dice_engine.py:39-44`); `recapitulate` carries a `warrant: thin` note per `relay/F:571`.
- **Cost:** 1 roster (with three typed columns — a schema addition, counted, per `17:805-806`).
- **Breaks if wrong:** `reachable_bands` is a per-kind cap on the ladder's output — it is *not* a second ladder (`T-k`) because it is applied as a demotion by the seam's one `BandExtension` (step 12), never by re-banding. If a session implements it as a lookup that *returns* a band, that is R-7.
- **Falsifier:** `impugn` ever resolves at `Success` or `Overwhelming` in any run.

### PHASE 2 · THE SUBSYSTEM OWNS THE CONTEST

**8. The manifest row lands, and the seam dispatches by row rather than by `if`.**
- **Change:** `shape.py:6740` `if _sub["module"] == "personal_combat": import combat_seam …` is replaced by a lookup on `w.manifest` (`shape.py:2633`, role → provider, resolved at boot via `boot()` at `:3039-3044`): `provider = PROVIDERS[w.manifest[("contest", _sub["module"])]]`, where `PROVIDERS` is populated from a `manifest.yaml` row `- role: contest / provider: proceedings / prize: "a matter"` (`08_SEAM.md:60-65`) plus the existing combat row. `personal_combat` keeps working through the same lookup. The `raise Unspecified` at `:6757-6771` survives for any prize no row routes.
- **Why here:** the ruling. And `08_SEAM.md:46-58` already argues why a second `if` violates `§C.5`, `02_HIERARCHIES §D.4` and `G.2.6`.
- **Artifact:** `boot(("contest",))` on a world whose manifest lacks the proceedings row fails **naming the row** (`NoProducer`, `:3041`); with the row present, `contest(w, rung, "a matter", …)` reaches `proceedings.run` and does not raise. Combat's byte-exact goldens are the control — they must not move.
- **Cost:** 0 verbs · 1 manifest row · 1 provider module (`proceedings.py`, beside `combat_seam.py`).
- **Breaks if wrong:** the manifest lookup by-passes `contest_subsystem()`'s `module_contracts.yaml` cross-read (`shape.py:6493-6520`) — keep that read for the `doc`/`sim_module` refusal text; only the dispatch changes.
- **Falsifier:** `grep -n 'module"\] ==' shape.py` returns any line inside `contest()`.

**9. The two `rosters.yaml:441-446` prize rows repoint here.**
- **Change:** `"a standing": "social_contest"` → `"proceedings"`; `"a proposition": "social_contest"` → `"proceedings"`; add `"a matter": "proceedings"`. `speak` declares `contests: "a matter"` (`04_VERBS.md:67`). The other two prizes are routed and, as today, claimed by no verb (`H-120`, `hole_register.yaml:2043`) — leave them routed; they are almost certainly "a matter" under `disposal: none` and `disposal: mutual` respectively, and collapsing three prizes to one is an engineering call for after the bar runs.
- **Why here:** ruling item 2; it is one line each, and it is now loud (`README.md:109-113`'s objection is answered by the ruling itself).
- **Artifact:** a seeded `contest(w, rung, "a proposition", …)` resolves through the seam without raising; `H-120`'s cite is updated with the run. `contest_subsystem("a standing")["module"] == "proceedings"`.
- **Cost:** 2 roster edits · 1 roster member.
- **Breaks if wrong:** whatever those rows previously reached is orphaned — **that disposition is Jordan's (PART 7, D-1) and the orphaned tree is not to be opened.**
- **Falsifier:** `contest_subsystem("a standing")` still returns `social_contest`; or `contest()` for either prize still raises the `:6757` refusal.

**10. `Query.judging_set(w, venue, matter)` — three parameters.**
- **Change:** `shape.py:3161-3163` (raises unconditionally) becomes the walk at `04_VERBS.md:318-321`: seats whose `remit_acts` contain `arrangement.bench_basis`, whose `scope_rung` contains the venue by the containment walk, with a live `hold`. The third parameter is stated as an extension of the live two-parameter signature (`04_VERBS.md:323-330`).
- **Why here:** `12_BUILD_ORDER.md:12` — buildable today; `H-32` (`hole_register.yaml:346-356`) has the default and the sweep (`remit+scope`, `remit only`, `scope only`).
- **Artifact:** a bench resolves over a planted seat roster; removing the seat's remit empties it; a purview walk one rung up still finds it; **the three-arm sweep runs**.
- **Cost:** 0 fields; the function is four lines and a walk.
- **Breaks if wrong:** a venue-only judging set makes two matters before one bench return one answer — the deleted `Rung.judging_set_rule` defect one level up (`04_VERBS.md:326-330`).
- **Falsifier:** two docketed matters at one venue with disjoint remit coverage return the same seat set.

**11. `arrangements.yaml` and its loader — with the multilateral disposal, and three keys fewer.**
- **Change:** the row at `03_PARAMETERS.md:435-468`, edited: **delete** `stakes_grade` (`P-09`, replaced by step 21), `verdict_reasons` (its only lawful mechanism is identical to `records_dissent`'s — which emissions of the bench reach `disposal_reach` — so one key carries both; fold its `given | withheld` into `records_dissent`'s scope), and `registers[]` (the roster does not exist, the 7→7 map is `P-39`'s forbidden lookup, and its idea folds into aptness — step 12). **Add** `disposal: declared` and a `quorum:` key (integer or fraction; data). **Keep** `records_dissent` — withdrawn from the cut list, because under `declared` it is the tally made visible: `true` scopes the members' `commitment.made` emissions to `disposal_reach`; `false` scopes only the declaration. Net: 15 − 3 + 1 = 13 keys.
- **Why here:** `12_BUILD_ORDER.md:13`; the ruling on multilateral; the cuts are cheapest before rows exist.
- **Artifact:** twelve rows load; a fourteenth key fails naming the row; the examination (`03:723-739`) loads with no code change; a row with `disposal: declared` and no `quorum` fails the load (loader invariant: `declared` requires `quorum`). Loader invariant 13 (`08_SEAM.md:144`) fires on a `room`-reach row whose disposal is not between the parties.
- **Cost:** −3 keys · +1 key · +1 `disposal` value.
- **Breaks if wrong:** if `records_dissent` is folded into `verdict_reasons` rather than the reverse, the key's name stops saying what it does. Keep the name that names the tally.
- **Falsifier:** the closure scan (`03:799-802`) finds an `arrangement.id ==` comparison anywhere in the provider.

**12. The composed obstacle, the injected magnitudes, and the licence veto as one `BandExtension` at the seam.**
- **Change:** (a) rule `P-29` as **A — latitude in the pool only** (`06_RESOLUTION.md:110`, the file's own recommendation, and `17:995` puts it first because the term count is wrong until it is ruled; it needs the owner's confirmation — PART 7, D-2 — but the build proceeds on A with B as a swept arm). The obstacle is then four room terms plus aptness: `base_Ob = opposition_score/2 ± reception ± rung ± aptness ± proofs_told`, floored at 1 (`06:227-242`; canon P-232). (b) the pool is `brought + conduct × latitude(game)`, fractional, floored at 1D, drawn once per interaction through `continuous_engine_sample` (`sigma_leverage.py` `roll_net_continuous`; never `roll_pool`, `06:296-298`). (c) `aptness` reads step 7's roster: genre mismatch and rung mismatch each add `APT_STEP`; the manner-misreading idea from `registers[]` folds in here as the same term. (d) **the licence veto** — Fig. 26's four conjuncts (`03:163-198`) — is one `BandExtension` subclass (`dice_engine.py:95-138`) injected by the provider's wrapper, whose `may_overwhelm` returns False when `licence_failures > 0` **or** when the speech kind's `reachable_bands` (step 7) excludes Overwhelming; it is demote-only by construction (`:292-300`). No four terms; one `licence` count (`17:620-629`). (e) `eff_ob()` is never resolved on (`06:299-303`).
- **Why here:** `12_BUILD_ORDER.md:11` step 0; the margin's band edges are ruled and pinned (`P-01` dissolved). **Single owner now** — with ownership settled, the obstacle composition has exactly one home and the de-saturation extension that lived elsewhere (`sigma_leverage.py:336-343`) is not this provider's; the extension the seam injects is this one.
- **Artifact:** a seeded margin produces the same band twice; a planted margin either side of each edge bands differently; a composed Ob never falls below 1; `licence_failures=1` on a margin ≥ 3 returns `Success`; `validate_context` (`dice_engine.py:120-137`) refuses an undeclared key. Register rows for `APT_STEP`, `RUNG_STEP`, `PROOF_STEP`, the source weights, the latitude multiplier — each with three swept points, each executed.
- **Cost:** 4 room terms + aptness · ~6 magnitudes · 1 `BandExtension` subclass · 0 fields.
- **Breaks if wrong:** every flat Ob term swings a weak speaker by `1/√pool` (`06:265-282`, `P-27`). The sweep at pools {1, 4, 9, 16} is PART 5 M-3, and it decides whether `reception` alone moves to the σ-channel.
- **Falsifier:** any code path in `proceedings.py` that returns a band; any Ob < 1 in any run; a `BandExtension` whose `may_overwhelm` ever returns True on a licence failure.

**13. `speak` and `determine` land as rows.**
- **Change:** `speak` per `04_VERBS.md:58-80` with one addition — **O-9**: the `Partial` write to `DocketItem.matter` takes the speech's own operand (the speaker names the subsidiary question), so a `Partial` is a `carry` the bench did not choose (`relay/E:106`). `determine` per `04_VERBS.md:288-300` **plus** `contests: "a matter"` — `17:288-291` finds it declares none and therefore writes a degree it cannot compute; with `contests:` the finding's `Tenure.degree` is a real band and gains its first reader (step 15's quorum). `P-25` (whose score the Ob is half of) is under a standing suspension (`06:212`); inject the default — the opposing party's score/2, the hearer's where unopposed — declare it, sweep it, and do not re-escalate.
- **Why here:** `12_BUILD_ORDER.md:17-18` steps 6–7.
- **Artifact:** a `speak` with no live occasion forms no Candidate; the four `writes`/`emits` key sets are equal (loader invariant 12); `Partial` emits `docket.formed` with the speaker's operand as the new item's matter; a bench member determines a heard matter; an unseated actor emits `determine.unseated`.
- **Cost:** 2 verb rows given bodies · 1 `contests:` on `determine`.
- **Breaks if wrong:** `Person.stance` on `Overwhelming` is the actor's own (`AX-4`); in the audience genre the corpus says the credit belongs to the sovereign (`18:145-149`) — a mechanism for that needs a write to another person's stance, which is R-10 and forbidden. So the sovereign's adoption is expressed by the *sovereign's* own later `commit` to the counsel's Proposition, not by a write. State that in the row's note and do not build a workaround.
- **Falsifier:** the `Partial` docket item carries `matter: None` (the CALENDAR shape, `shape.py:5378-5380`) instead of the speaker's operand.

**14. `proceedings.run` — the nested run, with its three in-run aggregates, all free.**
- **Change:** the provider at `08_SEAM.md:20-27` / `05_PROCEDURE.md:35-46`: order attendees from the arrangement row (`08 §C.1`); for each in that order, the person forms candidates from what they hold (no `World` — `T-f`), the act is folded through `SeasonDriver._fold(w, act, Resolution(degree, r))` with a degree the provider computed from **one draw** against the composed Ob (`06:340`); Events go to the same log; the run ends when nobody acts, the term matures (step 22), the ladder's foot is reached, or the depth cap returns a typed `Refusal`. **There is no turn limit** (`05:67-70`). The provider never calls `w.write`. It returns `{"status": "RESOLVED", "net": …, "ob": …, …}` for the *opening* speech, which is what `degree_of` reads (`shape.py:6678-6679`), and the fold bands it. Three aggregates, each a fold over this run's own emitted Events, owned by nobody, dying with the run — licensed outright by the owner (*"why can't we have aggregates in a subsystem?"*) and by `T-a`'s correction (*"say cannot be a field, never cannot be stored"*, `01_AXIOMS.md:279-282`):
  - **14a · the two-fold rung (O-5):** `own(party)` = lowest rung any of that party's own emissions named at any band; `forced(party)` = lowest rung an opponent's `Overwhelming` named. The obstacle reads `min(own, forced)`. This replaces the band-blind shared fold (`05:92-95`) and answers `18:515-517`'s worry — the comparison is intra-run, so it is not a tally in `T-a`'s sense.
  - **14b · proofs told so far** (already in `06:238`) — unchanged.
  - **14c · momentum (the debate score, accepted by ruling):** `momentum(party) = Σ over this run's `matter.*` emissions by that party: +2 carried · +1 advanced · 0 held · −1 turned`. It enters the obstacle as `± MOMENTUM_STEP × momentum` — one term, one magnitude. The player *in the room* can count the emissions (they witnessed them); the coefficient is hidden (R-18). Cross-season survival is step 26.
  - **14d · silence priced (O-11 / P9 rebuilt):** `PASS_STEP` added to an attendee's next obstacle only where the provider formed a non-empty lawful candidate set for them and they took none (`17:578-584`); carve-out from the arrangement row (`order: free` charges nothing) as data, never a membership test; falsified on `order: scripted`, which is buildable.
- **Why here:** it is the provider; everything above it is a parameter of it.
- **Artifact:** **THE BAR** (`12_BUILD_ORDER.md:20`): one seeded proceeding runs end to end with zero authored acts, twice, byte-identical including `World.content_hash()` (`shape.py:3025-3034`); `causes[]` walks from the determination back to the date that raised it. Plus: permute `order` and the outcome moves; permute anything else about the sub-steps and it does not (`08:95`). Plus: at depth == `max_depth` the return is a `ContestError`/`Refusal`, and in GDScript it must be reachable without a crash (`09_IMPOSSIBILITIES.md:21`).
- **Cost:** 1 provider module · 2 obstacle terms (momentum, pass) · 2 magnitudes (`MOMENTUM_STEP`, `PASS_STEP`) — **`PASS_STEP` swept jointly with `HELD_STEP`** (`17:951-958`; PART 5 M-4).
- **Breaks if wrong:** if the provider evaluates any precondition outside `_fold`, it is a second resolver (`§C.4`, CONVENTION); an AST scan of `proceedings.py` for `w.write(` and for `requires` evaluation is the guard. If `momentum` and the rung fold read the same emissions with the same sign, they double-count — sweep them jointly.
- **Falsifier:** the hash differs between two runs at one seed; or `grep -n "\.write(" proceedings.py` returns a hit; or a proceeding advances with no act taken.

**15. The multilateral disposal — the quorum is a Query read by a declaring act.**
- **Change:** the construction at `05_PROCEDURE.md:110-116`, built. Each bench member's finding is a **`commit`** (`own`, `verb_table.yaml:97-111`) to a disposition Proposition (P or ¬P) — their own edge, nobody else's. The declaring act is **`determine`** by a seat in `judging_set`, whose `requires_typed` gains a third conjunct: `{form: cardinality, of: subject, kind: commit, by: judging_set, at_least: quorum}` — counting live `commit` edges to the subject whose holder sits in the bench. This widens form 4's `needs:` (`rosters.yaml:810-818`) with `by` and `at_least`: **two grammar entries, counted as a design change and taken because it is what works best** (ruling 4). Form 4 has no typed cell today (`rosters.yaml:788-790`); this is its first. The declaration writes the disposal; `records_dissent` scopes the members' `commitment.made` emissions to `disposal_reach` (step 16). **No count is stored anywhere.** `P-15` closes.
- **Why here:** ruling; and it gives `Tenure.degree` (a writer and no reader, `08_SEAM.md:120`) and `records_dissent` their first readers in one step.
- **Artifact:** five seats; three `commit` to P; the presiding seat's `determine` succeeds; with two it emits `determine.no_quorum` (one Event kind, declared on the row); `records_dissent: true` fans three `commitment.made` to the realm, `false` fans only `matter.determined`. `grep` over `shape.py` and `proceedings.py` for any field named `count`, `tally`, `votes`, `quorum_reached` returns nothing.
- **Cost:** 2 grammar entries · 1 refusal Event kind · 0 fields · 0 verbs.
- **Breaks if wrong:** a member's `commit` to ¬P is a public dissent even under `records_dissent: false` if it is fanned by `floor` rather than by `disposal_reach` — the members' commits happen *in the room*, so the room sees them regardless (that is `P-41`'s ruling: the player is in the room). `records_dissent` governs what *leaves* the room. State this so nobody tries to hide a commit from a co-located witness.
- **Falsifier:** the declaring `determine` succeeds with fewer live bench `commit`s than `quorum`; or a stored count appears; or the tally changes a member's own `commit`.

**16. `disposal_reach` in code — landed in design, not in the tracer.**
- **Change:** `08_SEAM.md:153-166` — the disposal's existing emission (`tenure.opened`/`tenure.closed`/`case.opened`, and now `matter.determined` and the members' `commitment.made` under `records_dissent`) computes its witness set from `arrangement.disposal_reach` rather than from presence: `room` → the frozen attendee set; `body` → holders of a seat whose remit reaches the matter; `<rung kind>` → the containment walk from the venue up to that tier. Implemented as one more channel in `observers_for` (`shape.py:4430`) keyed on Event kind — the design says it adds no Event kind and no act.
- **Why here:** without it, the `chronicle` channel that "matches nobody" (`shape.py:4398-4407`) is the only public channel and it is dead; with it, **delete `chronicle` from `witness_channels`** (`rosters.yaml:110`) — its job is done by the reach — and re-label `H-33`'s `all_five` arm `all_four` with the sweep test's assertion at `test_tracer_is_honest.py:3078-3083` updated to the new arm name.
- **Artifact:** the same excommunication at `disposal_reach: room` vs `realm` deposits into 4 vs 40 ledgers; the argument's `matter.*` emissions deposit identically in both (they scope by `floor`).
- **Cost:** 1 channel predicate · −1 dead channel.
- **Breaks if wrong:** a `room`-reach negotiation whose `oblige` leaks to the realm — invariant 13 catches the row; the test catches the code.
- **Falsifier:** any `matter.*` Event's deposit count changes with `disposal_reach`.

### PHASE 3 · THE ROOM READS YOU

**17. O-2 · `reception` is composed from the bench's ledgers and convictions, resolver-side.**
- **Change:** `reception(w, speaker, bench, matter) -> float`, `World` first (`P-30`), living beside the other resolver-side Queries and **never importable from decision code** (`T-f`). For each seat's holder: claims with `c.subject == speaker`, each weighted by `SOURCE_WEIGHT[c.source]` (an ordinal of remove over `rosters.yaml:119` — `firsthand > firsthand_via_knot > told_by > inferred`, injected, swept) × `c.confidence/100`, with valence from `Σ_axis holder.convictions[axis] × alignment(verb_of(c.predicate), axis)` — `verb_of` being the emits-column lookup `_ch_post_remit` already does (`shape.py:4382-4386`). Sum over the bench; `RECEPTION_STEP` scales it into the obstacle. **The valence source is the swept choice**: arm 1 reuses `alignment` (`rosters.yaml:877-938`), which conflates "what this hearer prefers to *do*" with "how this hearer *regards* someone who did it"; arm 2 is a dedicated `regard` roster keyed on Event kind. The sweep decides, and the conflation is recorded rather than glossed.
- **Why here:** the join. It is the only hidden term (`15:55-66`), and with steps 1–4 there is finally something for it to read.
- **Artifact:** two benches of identical seats and identical convictions, differing only in one member's ledger (one `told_by` claim that the speaker `destroy_record`ed), produce different bands for the same seeded draw. A `told_by` claim moves the Ob strictly less than the same claim `firsthand`. An AST test that `reception` takes `World` first and that no module under the decision side imports it (`P-30`'s scan).
- **Cost:** 1 obstacle term (already ruled) · 2 magnitudes · 1 optional roster (arm 2).
- **Breaks if wrong:** `1/√pool` — the weak speaker's room becomes a lottery. PART 5 M-3 is the check and its remedy is moving `reception` alone to the σ-channel via `levels_to_net_sigma` (`06:278-282`).
- **Falsifier:** a bench's Ob is invariant under any change to its members' ledgers; or `reception` is reachable from `choose`.

**18. O-10 · A proof is weighed by its remove and discounted by the mirror.**
- **Change:** the `proofs_told` term (14b) weights each told claim by `SOURCE_WEIGHT` and **discounts to zero** any told claim for which the opposing party holds a claim with the same `(subject, predicate)` — a Query over two ledgers, resolver-side (`relay/E:114`). The player cannot run the mirror (they cannot read the other ledger); they guess it, which is the hoard/spend decision (`18:349`).
- **Why here:** needs step 4's `told_by` and step 17's weights.
- **Artifact:** a `tell` of a claim the opponent also holds moves the Ob by exactly zero; a `tell` of one they do not moves it by `PROOF_STEP × SOURCE_WEIGHT[source]`.
- **Cost:** 0 new terms · 1 magnitude (already step 12's).
- **Falsifier:** the mirrored proof moves the Ob.

**19. Close P-05 · an investigation deposits its *product*, at a confidence keyed on its degree.**
- **Change:** the five rows at `04_VERBS.md:427-492` land in `verb_table.yaml` at `contested_physical`. `observation_deposit_mode="actor"` (`shape.py:1847`) already deposits what the *precondition* read — which for `interview` is co-location, not the disposition. So each row gains a `product:` column naming the predicate its finding deposits: `interview → stance:<subject>` (the subject's SAID row), `examine → retention:<record>`, `research → record:<subject>`, `reconstruct → inferred on the matter`, `surveil → present:<place>`. At WITNESS, the actor's deposit for the act's own Event carries `(subject, product_predicate, value)` at `conf = DEGREE_CONF[e.degree]` (Found/Read/Sound: high · Partial/Glimpsed: mid · Misread/Wrong: **the same as Read/Sound, with a wrong value** — `AX-2`, `04:474-475`). This is the write side of the person-predicate vocabulary (`rosters.yaml:195-204`).
- **Why here:** `15:78-99` — without it nobody has a reason to ask anybody anything; the obstacle it estimates now exists (step 17).
- **Artifact:** Carin `interview`s the bailiff about the record; her ledger gains `(p_bailiff, stance:record, ±)`; on `Misread` the sign is wrong and the confidence identical; the bailiff's ledger gains `(p_carin, said.given)` — he learned what she asked. `surveil` still refuses for want of a term until step 22.
- **Cost:** 5 verb rows · 1 column (`product:`, a schema addition, counted) · 1 magnitude table (`DEGREE_CONF`, swept).
- **Breaks if wrong:** a `Nothing`/`Misread` that deposits nothing would make absence legible — it must deposit at the same confidence with the wrong value or the empty read, never be silent about having asked.
- **Falsifier:** `Read` and `Misread` are distinguishable by anything in the actor's ledger other than the value.

**20. O-16 · Route erosion, derived from the hearers' claims.**
- **Change:** inside `reception`, partition each hearer's claims about the speaker by the verb kind they record — dominance-sourced (`kill / wound`, `revoke`, `levy`, `evade / defy`) vs prestige-sourced (`determine`, `create_record`, `tell`, `comply`) — a verb → route mapping in data (the `alignment` precedent). A `speak` with a person subject that resolves `Failure` against a dominance-standing speaker zeroes that hearer's dominance-sourced weight (the single called bluff, `relay/E:162`).
- **Why here:** it is the study's one predictive cut, and it needs step 17.
- **Artifact:** the Lord who governs by fear is challenged; the challenger's one `Failure` leaves the Lord's reception intact; the challenger's one `Success` collapses it in every witness's ledger.
- **Cost:** 1 sub-term · 1 magnitude · 1 data mapping.
- **Falsifier:** a called bluff leaves dominance weight unchanged.

**21. Failure's severity is the observer set, and `stakes_grade` is gone.**
- **Change:** the corpus's shape #4 — terminal = being seen at it (`relay/F:522`). `18:78-81` proposed `Claim.visibility` as the carrier; **that field is inert** — declared at `shape.py:2158`, written as the constant `"own"` at `:6336`, read nowhere (the only occurrence of the word in the file is the declaration). The honest carrier is the size of the observer set for the failing Event at WITNESS, minus the actor — a barrier-scoped aggregate, licensed (`01_AXIOMS.md:279-282`). A `Failure` witnessed by nobody but the actor writes `Person.stance` alone (costly); one witnessed by N others additionally deposits into N ledgers (that already happens — the *grading* is that the row's terminal writes, the `commit` severed, fire only when `observers > SEEN_FLOOR`). **Delete `Claim.visibility`** or give it a roster and a reader — it is `ID-13`'s dead carrier and this plan does not need it.
- **Why here:** replaces `stakes_grade` (cut in step 11) with the study's own rule at zero coefficients beyond one floor.
- **Artifact:** the same `Failure` in a `floor: closed` room with two attendees and a `floor: open` room with twelve writes the costly consequence in both and the terminal one only in the second.
- **Cost:** 1 magnitude (`SEEN_FLOOR`) · −1 inert field.
- **Falsifier:** a discovered lie in an empty room severs a `commit`.

### PHASE 4 · FORTY SEASONS STOP LOOKING LIKE FOUR

**22. `Tenure.term` — the one field.**
- **Change:** `shape.py:2067-2086` `Tenure` gains `term: Optional[Term] = None` with `Term(matures_at, declared_by: ActId, closer)` (`04_CODE_ARCHITECTURE.md:333-340`); `payload` is deleted (`write_matrix.yaml:52-53` already schedules the replacement; `payload` has no reader). MATTER matures a `term` citing `declared_by` as its cause (`§B.8` — one causation-bound seam, not a fourth clock). Then: `issue` of a summons declares a return day; `evade / defy` of it is contumacy and **is** the finding (O-14 DEFY); `surveil`'s interval types (`04:481-484`); an overdue `oblige` is a pressure source (step 23); the inquisition row's `term_required: false` is authored indefiniteness *the subject can feel* (`03:612-619`). `P-04` closes; `P-33`'s three absences become derivable — declined (a `compliance.withheld` Event exists), could not (no Event, not present), not admitted (`floor` refused) — no ruling needed.
- **Why here:** it is the best-value field in the register (`18:212-213`) and it touches the substrate (`write_matrix`, the gate's `T-n` path), so it comes after the game exists.
- **Artifact:** a summons matures with no act and closes citing the act that wound it; `evade / defy` on it emits and the bench's `determine` for contumacy is formable next season; a `surveil` row now loads with a typed cell; `Tenure` with a `term` and `payload` deleted passes `matrix_rows_without_a_field`.
- **Cost:** 1 field · −1 field.
- **Breaks if wrong:** routing maturation through CALENDAR makes a term un-endable when nobody acts — the ratchet `T-n` exists to forbid (`§B.8`).
- **Falsifier:** a term matures with `causes=[ROOT]`.

**23. O-8 · Pressure surfaces as a `standing` band crossing, about someone.**
- **Change:** Q3 (`shape.py:3905-3927`) reads only site crossings from `w.crossings` (`:5607`, site-keyed). Add person-keyed crossings: at MATTER, recompute `standing_of(p)` over claims with `when < tick` and over all claims; if the band (on `condition_scale`, `:4010`) differs, append `(p.id, "standing", before, after, ev.id)` and emit `standing.band_crossed` with `causes` = the deposits that composed the gap. Q3's referents are **the holders of the `told_by` claims that compose the gap** — so the question is about *the archdeacon*, not "stress 7" (`18:304-306`). Second source: two live `commit`s to Propositions sharing subject and predicate with different value — computable today, no reader. Third source: an `oblige` whose `term.matures_at < tick` (step 22). A crossing changes what can be chosen and never what happens (`T-b`).
- **Why here:** needs `told_by` (step 4) for the gap to be non-trivial and `term` (step 22) for the third source.
- **Artifact:** the bailiff is told three things about himself; his standing crosses; his first question next season names the tellers; he forms `open_case` against one of them (`suspicion → open_case 0.9`, `rosters.yaml:926`) — who may not have said it.
- **Cost:** 0 fields · 1 Q3 reader · 1 Event kind (`standing.band_crossed`, declared on the MATTER row).
- **Breaks if wrong:** `Sensation.standing` is a *gap*, so a hated man who knows he is hated feels nothing (`18:518-520`). Whether that polarity is right is PART 7, D-4; the mechanism is the same either way and the sweep arm for the other polarity is one line.
- **Falsifier:** a crossing produces an outcome (a write) rather than a question.

**24. O-7 · Conviction moves by consequence — `determine` writes the determiner's own convictions.**
- **Change:** `determine` (now with `contests:`, step 13) gains a degree-keyed write to `Person.convictions` on the **actor** (`write_matrix.yaml:182-188` — a live RES row with no producer; `AX-4` clean because owner = actor). The axis moved is the one `alignment` weights for `determine` (`Precedent`, `rosters.yaml:909`): Overwhelming hardens, Success moves a little, Partial none, Failure moves *against* the axis. Magnitude injected and swept. `P-21` closes; `L-6` gets a sign.
- **Why here:** `12_BUILD_ORDER.md:23` — not on the critical path and the most interesting row; needs 40 seasons to be seen (PART 5 M-5).
- **Artifact:** three lenient findings by one judge move his `Precedent` weight by a printed amount; the same arrangement on the same seats then produces a different obstacle for the same speaker; and **`test_r16_witness_never_touches_a_conviction`** stays green — the write is at RESOLVE by the actor's own act, never at WITNESS (`T-j`).
- **Cost:** 1 degree-keyed write on an existing row · 1 magnitude.
- **Breaks if wrong:** if the loop is positive, a judge hardens into a caricature; if negative, every bench converges (`10_LOOPS_AND_GAPS.md:26`). The 40-season run is the only way to know.
- **Falsifier:** a conviction moves at WITNESS; or `conviction.moved` is emitted with a cause that is a deposit rather than an act.

**25. O-12 · The forged record is a proof until examined.**
- **Change:** `examine` (step 19) contests `retention` plus `Record.forgery_quality` (`shape.py:2418`, written by `forge`, `verb_table.yaml:229-237`, read by nothing) when its subject is a Record; `Found` deposits `(record, forged, True)` to the examiner; `Nothing` leaves the forgery standing and the examiner witnessed examining. Until examined, a `tell` from a forged record enters the proofs term at a record's weight.
- **Why here:** needs step 19's product deposit.
- **Artifact:** a grant forged at quality 7 carries an appeal (`order: written_only`, `proofs: [record]`); an `examine` at `Found` makes the forger's exposure terminal by step 21's rule.
- **Cost:** 1 obstacle term on a proposed row.
- **Falsifier:** `forgery_quality` still has zero readers after this lands.

**26. Cross-season momentum — what the accepted debate score costs if it must survive the run.**
- **Change:** none by default. The in-run momentum (14c) dies with the run, and an adjourned hearing resumes at the ladder's top (`00_DERIVATION.md:303-306` names this cost). If the owner wants a debate's state to carry across seasons, the lawful carrier is a **`Record`** the presiding clerk writes (`create_record` with `subject_matter` = the run's final momentum and rung) — a document, carried, forgeable, burnable, and *claimable*, so what the record says about last season's debate is something a witness holds, not a truth. **Cost if wanted:** one clerk's scene per adjournment · one write on `Record.subject_matter` (an existing field; needs a `write_matrix` row) · the resumed proceeding's opener reads it as a proof, not as state.
- **Why here:** so the accepted shape has its cross-barrier form stated once, and so nobody builds a `Proceeding.momentum` field (R-1's sneak-in shape).
- **Artifact:** if built — a resumed hearing whose clerk's record was burned starts at the top; one whose record was forged starts where the forger says.
- **Falsifier:** any momentum value surviving a barrier outside a `Record`.

**27. Delete the dead carriers.**
- **Change:** `Person.beliefs` (`shape.py:2372` — zero readers, a `grep '\.beliefs'` returns nothing; scheduled at `write_matrix.yaml:52`). `Person.marks` (`:2367` — zero readers; it is a second home for the person's own firsthand self-claims, which `standing_of` already reads from `ledger`, `:4012`; the person-predicate vocabulary lives at `rosters.yaml:195-204` and step 19 is its writer). `Tenure.payload` (step 22). `Claim.visibility` (step 21). The `chronicle` channel (step 16). `urgency` stays — it is inert by construction and the code says the null result is the measurement (`shape.py:3449-3468`).
- **Artifact:** `matrix_rows_without_a_field` and the `ID-13` tests pass with four fewer fields; the corpus hash moves (deleting a field folds into `content_hash`, `:3010-3034`) and the move is recorded, not hidden.
- **Cost:** −4 fields · −1 channel.
- **Falsifier:** a reader appears for any of them in the diff that deletes it.

### The twelve variants, mapped to the step that gives each its distinct play

| variant | the distinct play (`18:447-461`) | lands at |
|---|---|---|
| negotiation | the offer ladder; `mutual` generalised to all parties | live today; step 11 |
| by envoys | rope | live |
| arbitration | the game before the game | step 10 |
| legal trial | descend and be seen | steps 2, 14a, 22 |
| tribunal | a bench that drifts | step 24 |
| interrogation | what not to say | step 14d |
| inquisition | indefiniteness the subject can feel | step 22 |
| excommunication | deciding about someone absent on claims you cannot check | steps 4, 16, 17, 22 |
| parliamentary debate | which of many to address; the vote; the losers on record | steps 5, 11, 15 |
| council of state | the hidden profile | step 1 |
| audience / embassy | say nothing here, tell it elsewhere | step 4 |
| appeal to authority | the cap is a term somebody set | step 22 |

Three rows had no distinct play as the code stood (`18:463-464`); each now has one step, and none of the three needed a new mechanism.

---

## PART 4 · THE CHARACTER MODEL, IN FULL

The owner's list, verbatim: *goals and ambitions, allegiances, memories, beliefs, convictions, ethical stances, pressures, stresses, relationships … fears.* Each row: what it is, where it lives, what reads it, what it costs, and which step makes it live. **The governing fact:** every one of these already has a carrier except pressure's third source; what was missing was not carriers but *readers* — the precedent's exact failure mode, memory that never surfaces (`relay/G:128, 155`).

| the thing | what it is, mechanically | where it lives | what reads it (after this plan) | cost / step |
|---|---|---|---|---|
| **memories** | claims: *who holds it, about whom, what, when, from what source, at what confidence* — `Claim(holder, subject, predicate, value, when, source, confidence)` (`shape.py:2148-2158`) | `Person.ledger`, the holder's own and nobody else's | Q2 (`:3893-3903`), `belief_contradicts` (`:3855-3861`), `standing_of` (`:3993-4014`), O-3's cell evaluation (step 5), `reception` (step 17), the mirror (step 18) | today every memory is `(what was named, event kind, True, firsthand, 100)` and forgets who acted. Steps 1–4 make it hold a reading of a person. Step 3 decides whether it forgets the right things |
| **goals and ambitions** | a live `commit` to an OUGHT Proposition (`Q4`, `:3929-3937`) — *"hold Vellenmark"* is `existence` over a `hold`; a want must be expressible in the seven `requires_forms` (`rosters.yaml:810-818`) to be evaluable | `Person.tenures`, kind `commit`, object an OUGHT | Q4 supplies the topic today and reads only `prop.subject`; **step 5 supplies the direction** | 1 score term · 1 magnitude. *"Be loved"* is not expressible and is not faked through stance — an eighth form is a design change, named and declined (PART 6) |
| **fears** | the same carrier with `value=False`; satisfied by default; boosts when the precursor lands; **pressable indefinitely because nothing is spent**; the returns change on three reads (his ledger, the log, the hearers' ledgers); the terminus is his own `repudiate` (`relay/E:329-343`) | `Person.tenures`, kind `commit`, object an OUGHT with `value=False` | step 5's term with the habituation clause; step 6 traces the press to its end; the licence veto's *unrepeated* conjunct (step 12) prices the presser; `reception` (step 17) prices him in every later room | 0 beyond steps 2 and 5. **What a fear makes available is a subject, not a verb** — you can only name what you hold (`relay/E:358`). The inversion lands on the feared thing, not the presser (PART 7, D-3) |
| **secrets** | **a distribution fact**: a claim few ledgers hold. Threatening to reveal is the same lever as pressing a fear (name the subject without telling it); revealing spends it (telling deposits it everywhere and nothing un-spreads it); a closed floor contains it while `disposal_reach` proclaims the ruling (`18:308-329`) | nowhere new — the *absence* of a claim from most ledgers | everything that reads ledgers; and it is impossible until step 1 | 0. Step 1 is the whole precondition; step 16 is the containment's second scope |
| **allegiances** | a live `commit` to a faction's Proposition (`T-h`: a faction is a Proposition plus the `commit` edges to it) | `Person.tenures` | Q2's `mine` set; step 15's quorum counts them; a `speak` on a subject the faction is committed against fires the member's own Q2 (`18:383`) | 0. Repudiation ends it; a claim about a dead edge is a stale belief nothing marks — that is `AX-2` working |
| **relationships** | edges: `oblige` (owes), `tie`/`knot` (bound; the knot is a witness channel both ways, `shape.py:4361-4365`), `hold` (of a seat, a record), `succeed` — the typed `(A,B) → {type, since, until}` record the precedent ranks first (`relay/G:117`) | `Person.tenures` | `person_side_eligible`, the channels, `release` (step 11) | 0 new kinds. **What is refused and stays refused:** a creditor's act on another's edge (R-10; PART 7, D-5) |
| **convictions** | weights over the closed moral axes — what a person holds **right**; four of thirteen (`rosters.yaml:171`; `H-46` stays open by ruling) | `Person.convictions` | `score` (`:3502-3504`) — the one live reader; `reception` (step 17) reads the *hearer's*; **step 24 gives it a producer** | 1 write · 1 magnitude. Never moved by evidence (`AX-3`, `T-j`); moved by the person's own determinations |
| **ethical stances** | posture toward a subject: `(referent, valence, weight)` rows | `Person.stance` (`:2368`), read by `stance_toward` (`:3437-3446`) | `score`; written by `speak`'s bands (`04:69-72`) — the actor's own, only | 0. `Failure` writes it adversely — that is the study's whole fault catalogue in one column |
| **beliefs** | ⛔ **not a field.** A belief is a `commit` to an OUGHT; the field has zero readers | `Person.beliefs` — deleted (step 27) | — | −1 field |
| **pressures** | **a Query, never a number**: the gap between what you are told about yourself and what you hold (`Sensation.standing`, `:3993-4014`, computed each season and stored nowhere); contradictory commitments; overdue obligations | nowhere — computed at `sense()` (`:4550-4562`), the one world-taking non-decision function | **step 23** adds standing crossings to Q3, with the *people who told* as referents | 0 fields for two sources · **the one field (`Tenure.term`, step 22) for the third** |
| **stresses** | the crossing, not a meter. A band on the gap changes what can be chosen — admits `repudiate`, `evade / defy`, `move`, `open_case` through their `alignment` weights (`rosters.yaml:917-926`) — and never produces an outcome (`T-b`) | nowhere | step 23 | 0. **The forbidden shape — a scalar spent for outcomes — is refused because nothing is spent** (`18:300-302`); it is also the RimWorld failure mode the precedent warns against |
| **ethos / what others take you to be** | ⛔ **not a field.** Claims in *other people's* ledgers whose subject is you, each of which may be wrong | their ledgers | `reception` (step 17); `standing_of` from your side | 0. Step 2 is what lets a ledger hold one |
| **bias** | ⛔ **not a field, and must never become one** (`06:22-33`, `09` row 10). The divergence between a ledger and the world plus the weights convictions put on the axes | nowhere | it changes the finding and nobody can read it | 0 |
| **marks / identity-embedded memory** | the precedent's #4 (`relay/G:120`) — a scar, a byname. Here it is a person's own firsthand self-claim (`ledger`, `subject == p.id`), which `standing_of` already pairs; the field `Person.marks` is a second home | `Person.marks` — deleted (step 27); the vocabulary stays at `rosters.yaml:195-204`; step 19 writes it; step 3b makes person-claims outlive event-claims in eviction | — | −1 field |
| **attributes / efficacy** | `Person.capability` — supplies dice at RESOLVE and gates nothing (`03:104-108`); two keys (`brought`, `conduct`), content by `ID-12` | `Person.capability` | the pool (step 12) | 0 |

**What the model refuses, so it stays a model of people and not of stats:** nine capacities as stats (`03 §B.2`), a per-proceeding skill (`06 §B.0`), an office bonus, a bias field, a stress scalar, a reputation number, a want the grammar cannot ask. Every one is refused on the same ground — it would be a value with two readers or a threshold that acts — and every one has a lawful cousin above.

---

## PART 5 · MEASUREMENT DEBTS

Each must run before the thing after it is built; each names the experiment and the number that would change a decision.

| # | debt | before building | the experiment | the number that decides |
|---|---|---|---|---|
| **M-1** | **the ledger cap** (`P-42`) | anything that reads a person-claim across seasons (steps 17, 20, 23) | step 3: seed 0, NPC-088, `all_five` + `named_and_actor`, seasons 1..12, `ledger_cap` {100, 200, 400} × `claim_decay_per_season` {0, 5, 20}; first season the season-1 person-claim is absent | evicts before season 4 → the key is recency-dominated → step 3b. Survives 12 → the cap is not the problem |
| **M-2** | **the want-term magnitude** | step 6 (the press) and everything that depends on NPC initiation | step 5's sweep at `question_aggregation_rule="all"`, three `want_boost` points, two-NPC world; count verdict flips per arm | zero flips at any arm → inert; flips at every arm → monomania at the top. The usable window is what the sweep prints |
| **M-3** | **the `1/√pool` swing** (`P-27`) | step 20 (route erosion) and any further obstacle term | step 12's five terms at pools {1, 4, 9, 16}, one term at a time, seeded; record band by pool | a rank advantage swings a pool-1 speaker's band more than a pool-16 speaker's **and** that reads wrong in play → move `reception` alone to the σ-channel (`06:278-282`). Only `reception`; the other four are properties of the room |
| **M-4** | **`PASS_STEP` vs `HELD_STEP`** (`17:951-958`) | shipping step 14d | joint sweep, 3×3, `order: scripted`; count runs where silence is chosen | `PASS_STEP ≥ HELD_STEP` → silence strictly dominated, the decision does not exist; `PASS_STEP` small → a shrug. The ratio, not either constant |
| **M-5** | **standing concentration over forty seasons** (`P-20`) and **`L-6`'s sign** | step 24's magnitude; any claim that the loops are bounded | `headless` 40 seasons, 12 persons, seeds {0, 1, 2}; Gini of `reception` across speakers per season; `Precedent` weight of each judge per season | standing Gini rising monotonically → `L-1` unbounded, and three of its four bounds are corpus properties not code (`10:28-36`). Judges converging → `L-6` negative; diverging → positive |
| **M-6** | **`presence_only` starvation** | making step 1's flip the shipped default rather than a swept arm | `corpus_run.py` at `total` vs `all_five`: R3 (claim → question → act) on the NPC lane and on ARC | R3 falls below 30/30 on NPC at `all_five` → `post_remit` and `document_key` are not matching anyone and the narrowing is too tight |

Rule for all six, from `CLAUDE.md` §0.1: a number without a control is not a measurement in either direction; each row above names its control arm (`total`, `first`, pool 16, the diagonal, seed 0, `total` respectively).

---

## PART 6 · WHAT NOT TO DO

### A · Do not build these, and why

| the attractive thing | why not |
|---|---|
| **a stress meter, a political-capital pool, a reputation number** | a per-person scalar with two readers (holder and resolver) that gates or is spent; `T-a`, R-9; and it is RimWorld's failure — memory into a number and nothing gates on it (`relay/G:128`). The crossing (step 23) is the lawful cousin |
| **a `bias` field, a displayed "the room is hostile"** | `AX-2`; `06:22-33`; it makes prejudice legible in a game whose epistemic layer exists to make it illegible |
| **nine capacity stats, a per-proceeding skill, an office bonus** | `03 §B.2`, `06 §B.0` — scripting drift with a schema's face; `capability` supplies dice and gates nothing |
| **a `Proceeding` object, a `Verdict` type, a `role` enum** | derivations, not omissions (`10 PART C`; `03 §C.2`) |
| **a hook-call verb (`call`), a creditor closing a debtor's `oblige`** | a non-owner Tenure write — `AX-4`, `T-m`, R-10. It is the second-person lever and it is PART 7, D-5, not a step |
| **widening Q2 so the cornered man retaliates at the presser** | not an `AX-1` breach (it reads B's own ledger) but a §F1 design change; the audit says the feared thing is the better story (`relay/E:341`). PART 7, D-3 |
| **an eighth `requires` form for "be loved"** | a new thing a precondition can ask (`rosters.yaml:788-790`); wants the grammar cannot ask are authored as stances or not at all |
| **raising the 200-claim cap as the P-42 remedy** | `18:106-113` — the fix is coupling the read to a decision point and (if M-1 says so) weighting eviction, not more slots |
| **a per-pair table** — speech kind × game, register × register | `§0.06`'s emergence rule; 144 numbers nobody measured (`04:266`) |
| **a second `if` in `contest()`, a subsystem-local `degree()`, a fifth band, a `Turned` band** | `08 §B`, `T-k`, R-7; the draft did the last one and it could not load (`04:82-89`) |
| **a turn limit, a round cap, "the hearing concludes after N"** | `AX-5`/`T-c`, `05:67-70` |
| **`reception` computed person-side, or shown to the player as a number** | `T-f`, `P-30`; R-18. Legible hand, illegible room |
| **a `catchment`, a `subject_absent` flag, a `cast:` on the row** | `03 §C.1.1`; presence is whoever travelled |
| **a `chronicle` channel that matches everyone** | `all_five` collapses into `total` and the sweep measures nothing (`rosters.yaml:395-402`) |
| **the other nine conviction axes** | `H-46` stays open by ruling (2026-09-02); nothing here branches on a member |
| **a `Thread-Read` row** | `P-19` — its obstacle is a rendering layer this directory has not derived |
| **restoring `stakes_grade`, `verdict_reasons`, `registers[]`** | step 11; each is a summary, a duplicate, or a lookup of a roster that does not exist |
| **opening `systems/social_contest/` or `proposals/2026-09-04-social-contest-branches/`** | the standing scope ban; and the disposition of that code is Jordan's (PART 7, D-1) |

### B · The cuts that pay

| cut | pays because |
|---|---|
| `stakes_grade` (step 11) | severity is whether the fault was *seen* — one floor instead of a three-valued summary |
| `verdict_reasons` (step 11) | its only lawful mechanism is `records_dissent`'s; one key |
| `registers[]` and the register-fit term (steps 11–12) | the roster never existed; the idea folds into aptness |
| `chronicle` (step 16) | matches nobody; `disposal_reach` does its job |
| `Person.beliefs`, `Person.marks`, `Tenure.payload`, `Claim.visibility` (step 27) | zero readers each; `ID-13` admits no third state |
| the `both` deposit rule as default (step 2) | it replaces the actor where it should join him |
| the shared band-blind rung fold (step 14a) | replaced by two folds that can see who conceded and who was pushed |
| "the chronicle mints hearsay", "co-located witnesses hold the attribution", "a vacant date is docketed" | already struck as backlog in the present tense (`18:479`); do not let them back in |

---

## PART 6R · THE REFUSALS, RE-SORTED UNDER THE SECOND RULING

The set is relay A §3.3 (R-1..R-21, `relay/A:348-374`), §3.4's named impossibilities (`:377-394`), the binary census walls (B-6, B-7, B-9, B-18, B-19; `:222-256`), `17_PLAYABILITY.md` PART F (`:886-908`), and `03_PARAMETERS.md` §F.2's three refused games. Sorted by what actually builds the wall.

**Genuinely forced — by the seam, by `AX-1`, or by an engine ruling. These hold.**

| refusal | forced by | note |
|---|---|---|
| R-2 a readable bias / disposition meter | `AX-2` | |
| R-3 a GM, a timer, a round cap, a fourth clock | `AX-1`, `AX-5`/`T-c` | |
| R-4 a view of the room inside a decision | `T-f` from `AX-2`; `P-30` | the boundary is one parameter list |
| R-5 Ob below 1; advantage as an Ob reduction | canon P-232; ED-884 | engine ruling, not this design's |
| R-6 a flat bonus not σ-scaled | the σ-engine's uniformity | advantage enters through `levels_to_net_sigma` |
| R-7 a second ladder, a fifth band, a promoted band | `T-k`; Jordan 2026-08-15; `BandExtension` demotes only | |
| R-9 eligibility by stat | `§A.2`; the loader raises on `capability` | |
| **R-10 a non-owner Tenure write** | **`AX-4`, `T-m`** | **the `AX-1` wall the coordinator flagged. Holds. The only mechanism adjacent to it is escalated (PART 7, D-5)** |
| R-11 an arrangement that declares a cast | `AX-1` | presence is travel |
| R-12 a disposal that writes only a Query | the about-the-world ruling (Jordan 2026-09-06); `T-a` | not provisional on ownership |
| R-13 an Event carrying a target or an actor | `T-d`, `T-e` | attribution is a per-witness claim (step 2) |
| R-15 a mutated Proposition | `frozen=True` (`shape.py:2425`) | terms are re-uttered |
| R-16 evidence moving a conviction | `AX-3`, `T-j` | step 24 moves it by *consequence* at RESOLVE |
| R-17 a `requires` operand outside the closed roster | load-time closure | step 15 widens form 4's `needs`, which is a *declared* grammar change, not an operand outside the roster |
| B-18 making someone a party | `AX-1` | party-hood is their own `commit` |
| B-19 the creditor verb | `T-m` | = R-10; `P-36` is a ruling |
| `03 §F.2` (1) a disposal with no author — lot, self-executing ordeal | `AX-1`, `T-b` | an ordeal is two games |
| `03 §F.2` (2) a shared transcript | `AX-2` | the largest refusal and the one that buys every mechanism the game has for politics |
| `03 §F.2` (3) a proceeding that advances because time passed | `AX-5`, `T-c` | recovered by `Tenure.term` (step 22) |
| CK3's hook spent by its holder (§3.4) | `T-m` | = R-10 |
| Disco Elysium's percentage (§3.4) | `AX-2` for the player, who controls a person | |
| R-19 a magnitude sourced to the study | `CLAUDE.md` §0.1 pt 4 | inject, declare, sweep |

**Provisional — justified on someone else owning the prize or on the over-applied aggregates reading, and now accepted.**

| refusal | what changed | where it lands |
|---|---|---|
| **R-1 a shared visible track / debate score / momentum / vote count** | the owner's *"why can't we have aggregates in a subsystem?"* and `T-a`'s own correction: a Query is the licensed form; a barrier cache cannot go stale. **In-run: accepted, free.** A *field* is still forbidden; a cross-barrier version costs a `Record` | steps 14a–c, 26 |
| **B-6 the multilateral disposal** | `05:110-116` supplies the `T-a`-compliant construction; the ruling accepts it | step 15 |
| Republic of Rome's counted vote (§3.4) | same construction — one declarer reads the Query. The relay called that "a different game"; it is the accepted one | step 15 |
| Sidereal Confluence's multilateral binding deal (§3.4) | `T-h`: a treaty is a Proposition plus N `commit` edges — a faction everyone joined. No `T-a` break; `mutual` reads as *all parties* | step 11 |
| R-20 zero new primitives | downgraded from constraint to tiebreak (brief, ruling 4) | steps 7, 15, 19, 22 each add a counted thing because it works best |
| B-7 `appeal_basis: none` as a wall | not forced (`17:895`); finality is derivable from the finding's degree and the declared cap | step 22 |
| B-9 `term_required: false` as "authored indefiniteness" | misfiled — a build blocker (`P-04`), not a virtue | step 22 |
| R-14 order from anything but declared data — the B-10 tension (a `Record` carrying the order) | narrowed: a Record the opener wrote *is* declared data (`T-n`); what stays refused is order from a capability or a body default | the provider reads the arrangement row; an opening act may *select* the row by its declared terms — noted, not built |
| the two-party bound on `disposal: mutual` (`P-15` coverage) | the multilateral ruling | step 11 |
| `records_dissent` on the cut list | it is the tally made visible; withdrawn | step 11 |

**Cut for being bad design, not for being unlawful.**

| refusal | why it stays refused even though nothing forces it |
|---|---|
| R-8 a per-pair rule table | the rule count grows with the pair count; scripting, not composing |
| nine capacity stats; a per-proceeding skill; an office bonus | models the half of the variance the study says is not there |
| a stress scalar spent for outcomes | RimWorld's failure; nothing is spent in this design |
| a `Proceeding` object | `00 §A.1` runs the carrier question over five candidates and none survives |
| `chronicle` as a channel | matches nobody; a public channel that matched everyone would collapse a sweep |
| `disposal: none` as a twelfth game | eleven games and a degenerate case (`14 §E.3`) |
| R-18 showing the obstacle | a UI rule (`15 PART E`), not a refusal; kept because a shown number is a solved line |

**Does "all social contests" widen the twelve?** No. Ownership of the *contest kind* is not a mandate to host every social interaction. `tell`, `utter`, `commit`, `petition`, `oblige`, `tie / knot` stay season-loop verbs with no `contests:` column; what routes to this provider is any verb that declares a prize the roster maps here — today `speak` (`"a matter"`), and the two repointed prizes when a verb claims them. The catalogue stays eleven games and one degenerate case, plus the examination, plus whatever a data row can express under the thirteen keys — and now including conclaves, votes and five-party settlements under `declared` and generalised `mutual`.

---

## PART 7 · JORDAN'S DECISIONS

Each survived the five tests (`04_CODE_ARCHITECTURE.md` G.4.5: superseded · irrelevant · answered by a design document · answered by precedent · answered by what makes sense for the architecture). Items that failed a test are closed in the instructions and listed at the end so the closure is visible. **Ownership is not here** — it is settled and its consequences are steps 8–9.

**D-1 · What happens to the code the repointed rows previously reached.** Repointing `rosters.yaml:441-446` orphans whatever `social_contest` was reachable through those two rows. Retire, migrate, or leave unreferenced is a separate disposition, described here only from the routing rows and from `H-120`'s cite (`hole_register.yaml:2043-2053`: *"connecting `a proposition` would reach social_contest's `agon` game, which is WIRED"*). **Blocks:** nothing in this plan — the rows repoint regardless. **Options:** (a) leave unreferenced with a `CURRENT.md` note that its rows are gone; (b) a retirement wave under the culling precedent; (c) a migration of anything in it this provider lacks — which this plan cannot assess without opening the tree, and will not. *Passed all five tests: it is a disposition over another lane's artifact.*

**D-2 · `P-29` — latitude in the pool only (A), or in both (B).** `06_RESOLUTION.md:108-132` records that the file implements B, says it implements C, and recommends A; `17:995` puts ruling it first because the base term count is wrong until then. Step 12 builds on A with B as a swept arm. **Blocks:** the term arithmetic in every magnitude row. **Options:** A — an interposed room is one where *who you are matters less*, four room terms (recommended, and the study's claim stated exactly); B — harder *and* flatter, double-counts. *Survives test 3 because the document recommends without ruling, and the 2026-09-06 ruling was for a third option the file does not implement.*

**D-3 · Where the cornered man's drastic act lands.** With step 5 the habituated man breaks in the direction of his convictions — toward the *feared thing* (burns the record, flees, confesses to the lesser crime), never toward the presser, unless a live edge B→A exists (`relay/E:341`). Retaliation at the presser needs Q2's second clause widened to admit claims whose *actor* is A when the claim's subject is in B's `mine`. That is person-side (B reads B's own ledger), so it is not an `AX-1` or `AX-2` breach — but it is a change to §F1 and it changes every NPC's question set. **Blocks:** nothing; the default ships without it. **Options:** keep the audit's picture (the better story, the study's picture, zero cost); or widen Q2 (one clause; every grudge becomes a question about a person, which is CK3's rival flag — and every NPC gets noisier). *Survives because the design documents take the first and the owner said fears are pressed; the direction of the break is content-shaped and his.*

**D-4 · The polarity of pressure.** `Sensation.standing` is a *gap*, not a reputation (`shape.py:3998-4002`): "everyone reads you as you read yourself" is zero pressure, so a hated man who knows he is hated feels nothing. That may be exactly right (the study's inhibition is about knowing and acting anyway) or backwards (`18:518-520`). Step 23's mechanism is identical under either; the arm is one line. **Blocks:** step 23's default arm. **Options:** the gap (a man is pressed by what he does not yet believe about himself); the adverse sum (a man is pressed by how badly he is thought of, whether or not he agrees). *Survives all five — it is a statement about what stress is in this fiction.*

**D-5 · The second-person lever — `P-36`, and the hook.** Forgiveness is inexpressible: `release` is `own`, so it is the obligor discharging himself; an obligee who forgives has no act (`10:94`). The same wall from the other end is CK3's hook — a creditor *calling* a debt (`relay/A:381-382`). Both are a non-owner write of a Tenure (R-10, `T-m`). **The wall holds in this plan.** What is expressible without breaching it: the creditor `tell`s that the debt exists (publicity), and a counter-`oblige` by the creditor (mercy as a new edge the creditor owns). **Blocks:** nothing built here; blocks the CK3 hook and forgiveness-as-clemency forever unless ruled. **Options:** leave `T-m` intact (a world of people; the lever is publicity and counter-promise, slow and political); amend `T-m` with an obligee-side closer for `oblige` only (one verb, one theorem amended — `G.1.2`: break a theorem and you have a contradiction unless it is re-derived). *Survives because it is the one place the design's own register says "a ruling" and the coordinator names it as the wall.*

**D-6 · The inverse-scale fault.** *"Whoever touches it is killed"* (`relay/F:557-559`) is the one terminal fault with no corpus-supplied next move, so it does not reconcile with fail-forward. **Options:** treat it as the one place the ladder's `Failure` is not the outcome (the outcome is removal from the world, outside this subsystem — a `kill / wound` contest the sovereign's own `choose` reaches); or soften the corpus. Handed forward unsoftened. **Blocks:** one row of the speech-kind roster's `reachable_bands` for `propose` before a superior.

**D-7 · Two corpus-vs-evidence branches in the speech-kind roster** (`relay/F:565-568`): whether a detailed denial outperforms a brief one; whether displayed anger extracts concessions (the evidence for the second is marked unverified by the study itself). Data authoring, per branch. **Blocks:** two rows of step 7's roster. Low stakes; can ship either way and sweep.

**D-8 · One-tick trials.** `P-14`: a hearing and its judgment cannot share a season because `binding_decision` resolves before `social` (`rosters.yaml:129`); the design banks it as a result it did not choose (`04:338-355`). *Passes test 4 (answered by precedent — the stratum roster)*, so it is **not** escalated as a decision — listed so the owner can veto: if one-tick trials are wanted, the row to argue about is `rosters.yaml: strata`, not this subsystem.

**Closed by the five tests, not escalated — recorded so the closures are visible:** `P-33` absence kinds (derivable after step 22 — test 5); the per-actor rung as a tally (the aggregates ruling — test 3); `P-12` the tribunal ratchet (the determiner's own `release` closes it — test 3, `04 §B.5`); `P-16` register position (moot after step 11 — test 2); `P-17` refuse vs demote (`03 §B.4`: always demote — test 3); `P-25` whose score (a standing suspension; inject and sweep — test 4); `H-46` the nine axes (ruled open — test 1); whether the three prizes collapse to one (engineering after the bar — test 5).

---

## PART 8 · WHERE THIS PLAN IS WEAKEST

1. **The outer act's degree is not specified anywhere in the design.** `speak` opens the contest and the seam returns one Margin (`08:21-27`), but a proceeding is six draws. Step 14 chooses *the opening speech's margin* as what the outer fold bands, with every inner act folded through `_fold` with a provider-computed `Resolution`. That is a choice this plan made; the design does not state it, and the alternative (the disposal's degree) is defensible. It must be stated on the row before the bar runs.

2. **`presence_only`/`all_five` as the shipped default is a corpus-wide change with one sweep behind it.** 89 baselines re-baseline (`shape.py:3946-3955`); M-6 is the only check that the propagation loop does not starve. If `post_remit` and `document_key` match nobody in the corpus worlds, `all_five` is `presence_only` and every NPC learns only what happens in front of them.

3. **The reception valence reuses `alignment`** (step 17, arm 1), which conflates *what I prefer to do* with *how I regard someone who did it*. Arm 2 is a second table. If the sweep does not separate them, the term is decoration wearing a person's name.

4. **The quorum cell widens the grammar** (step 15): form 4 has no typed cell today (`rosters.yaml:788-790`), and this plan gives it its first with two new `needs` entries. The loader's closure argument (an eighth form is a design change) is being spent on the one form nobody has exercised. If `by: judging_set` cannot be evaluated by `WorldReader` without the cell reaching a resolver-side Query, the fold is evaluating a Query inside a precondition, which is new.

5. **`18_FINDINGS.md`'s severity-by-`Claim.visibility` rests on an inert field.** The field is declared at `shape.py:2158`, written as the constant `"own"` at `:6336`, and read nowhere. Step 21 corrects the carrier to the observer set; the findings document should be corrected too, and this plan cannot edit it.

6. **The habituation loophole is assumed symmetric.** *Press, wait, press* decays his habituation and your infamy on one clock (`relay/E:346`). Under step 3b (person-subject weight on eviction), *your* record about *him* is a person-claim and outlives *his* record of the event — the clocks stop being symmetric. Step 3b and step 5 must be swept together, and this plan orders them apart.

7. **The multilateral disposal's dissent cannot be hidden from the room.** A member's `commit` to ¬P is witnessed by every co-located attendee regardless of `records_dissent` (step 15's note). The council-of-state row's "consensus discourages the disagreement from forming at all" (`03:657-662`) is therefore a *person-side* effect (a member who wants no record of dissent does not `commit` to ¬P), not a key's effect. The key governs what leaves; the room always sees. That is probably right and the row's prose says otherwise.

8. **`Claim.confidence` on a `told_by` deposit (step 4c) is the teller's *maximum* held confidence on the subject.** A teller holding two claims on one subject at 100 and 40 tells at 100. Whether the told thing is the 100 or the 40 is not distinguished — the deposit's predicate is `news.told`, not the told claim's predicate. That is the "content of a told claim does not exist" problem (`18:368-370`) and step 19's `product:` column is only the investigation half of it; `tell`'s product column is not planned here and probably should be.

9. **M-5 is a forty-season run nobody has done**, and `L-1`'s bounds are corpus properties (`10:28-36`). If standing concentrates, three of four bounds have no column to turn.

10. **The `alignment` reuse in `verb_of(claim.predicate)`** (steps 17, 20) depends on every Event kind being on exactly one verb's `emits` column. Two body literals remain (`act.ineligible`, `act.refused`; `shape.py:6181-6182`) and refusal kinds are shared across verbs; a claim whose predicate is a refusal kind maps to no single verb. Those claims get zero valence, silently.

---

### Critical Files for Implementation

- `/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/shape.py` — the deposit (`:6319-6346`), `claim_subjects` (`:4133-4207`), `observers_for` (`:4430-4453`), `score` (`:3494-3516`), `questions_for` (`:3864-3959`), `standing_of` (`:3993-4014`), `contest()` (`:6690-6771`), `Tenure`/`Person`/`Claim` (`:2067-2158`, `:2362-2394`)
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/rosters.yaml` — `claim_subject_rules` (`:250-303`), `claim_sources` (`:119`), `witness_channel_predicates` (`:382-411`), `contest_subsystems.prizes` (`:441-446`), `requires_forms` (`:768-818`), `alignment` (`:877-938`), the new `speech_kinds`
- `/home/user/ttrpg/proposals/2026-09-02-executable-architecture/verb_table.yaml` — `speak` (`:448-457`), `determine` (`:168-178`), `tell` (`:475-489`), `commit` (`:97-111`), the five investigation rows and `release` to be added
- `/home/user/ttrpg/proposals/2026-09-01-season-loop-tests/tracer/test_tracer_is_honest.py` — the artifact templates: the H-33 sweep (`:3058`), the H-40 inertness test (`:6735`), the register-sweep executor (`:3965`), the content hash (`:295`)
- `/home/user/ttrpg/proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md` — the arrangement row (`:435-468`) and the twelve rows (`:501-704`) that step 11 rewrites; with `04_VERBS.md` (`:58-80`, `:288-300`, `:427-492`) and `06_RESOLUTION.md` (`:227-242`) as the rows steps 12–13 land