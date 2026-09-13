# HANDOFF_SC — CLOSED WORK

**Lane:** `SC` — social contest. **Split out of `HANDOFF_SC.md` on 2026-09-13 (`ED-IN-0221`),
on Jordan's instruction:** *"why don't you just hive off all closed IN work into its own document"* …
*"tbh it's applicable to all handoffs"*.

## What this file is, and what it is NOT

**It is the closed narrative of this lane, moved VERBATIM and in original order.** Nothing was
rewritten, summarised or deleted — the split is proved lossless: the line multiset of this file
plus `HANDOFF_SC.md` equals the original file's, exactly.

**It is NOT a continuity surface. Do not orient from it and do not add to it.** New work goes in
`HANDOFF_SC.md`; this file only ever receives units that file has finished with.

## The predicate that moved a unit here, stated so you can re-run it

A unit moved **only if it carried none of** `needs_jordan` · `[OPEN]`/`STILL OPEN` ·
`HELD`/`SUSPENDED`/`PARKED`/`DEFERRED`/`⏸` · `BLOCKED` · `TODO` · `awaits`/`awaiting`.

⚠ **THE CUT IS AT THE FINEST GRANULARITY THE DOCUMENT ITSELF LABELS, and that is the whole reason
this was safe to do mechanically.** Section-level disposition markers in this corpus are known to
lie — a prior attempt (step `6c`) was refused for exactly that reason: *"12 of 17 sections marked
`[DONE]`/`[RULED]`/`EXECUTED` carry open, held or `needs_jordan` items inside them."* That finding
is about SECTION headings. The `Pending`, `Decisions` and `Next actions` logs label every **entry**
(`[OPEN]`, `[LANDED]`, `[DONE]`, `✅`), so those three split per entry and the rest per section.
No marker was trusted: the predicate reads the unit's **body**, never its title.

⚠ **`do not` / `never` was deliberately NOT used as a signal.** Sampled across this corpus it is
~75% narrative (*"a Date with no `due_at` is never due"*), and the genuine standing orders are
meaningless without the referent the surrounding paragraph supplies — extracting them as a list
would reproduce the `evacuate` failure `CLAUDE.md` §4 records. Units carrying imperative language
are instead **flagged on the index in `HANDOFF_SC.md`**, so a standing order is one file-open
away rather than buried.

---

## ⚠ CURRENT — 2026-09-07 · the proceedings subsystem was STRESS-TESTED
### *(read the section below this one first — it says what the subsystem IS; this one says what happened when somebody tried to run it)*

**`proposals/2026-09-05-proceedings-subsystem/20_STRESS_TESTS.md`** — 38 tests executed against the
tracer at `proposals/2026-09-01-season-loop-tests/tracer/shape.py`, harness at
`stress/stress_proceedings.py`, machine-readable run at `stress/results.json`. **ED-SC-0036.**
**Nothing was ratified and no design file was edited.** Reproduce: `python3 stress/stress_proceedings.py`.

**⚠ Read the second number, not the first.** 35 findings, **of which 20 restate a row this
directory already registers** — the gap register, `13_ADVERSARIAL.md` and `17_PLAYABILITY.md` are
unusually complete, and every finding carries an *already registered?* line saying which it is.
**Fifteen are new.**

### The four things that PASS, because a report of only holes has not checked anything

`speak` folds and emits for a person holding no seat · the appeal depth cap returns a typed
`ContestError` · ⭐ **a seeded proceeding replays identically** (21 Events, 18 claims, twice) ·
⭐ **permuting who attends does not move the outcome** — `05_PROCEDURE.md`'s own permutation
criterion, run for the first time.

### The five new results that survived an adversarial pass

| | |
|---|---|
| ⭐ **`F-14`** | **`disposes:` names a write and has no writer.** `determine` grades a Tenure and cannot open one; the draft row that would have opened it was corrected away. **`11_NERS.md`'s diagonal PASS rests on that write verbatim** |
| ⭐ **`F-38`** | **the count table at `00_DERIVATION.md` §B.1 — which `README.md` calls *the whole argument* — is stale in three of five rows.** The fields cell names `Proposition.rung` and says §B.2 *admits* what §B.2 retracts; the verbs cell says *4 new* where two other files say ZERO; the carriers cell lists `Seat`, which is not a carrier |
| ⭐ **`F-37`** | **five gaps are in the gap register nowhere** — `P-22 · P-23 · P-24 · P-28 · P-29` — each written as *Registered `P-nn`* at its own site. `P-24` is the one `14_THE_WORLD_IN_THE_ROOM.md` calls the sharpest thing its hardest question surfaced |
| ⭐ **`F-28`** | **the ladder rung is a fold over emitted `matter.*` Events and no emission can name a rung.** The zero-new-fields result rests on a fold with no operand |
| ⭐ **`F-33`** | **under the fan-out arm in force there is no such thing as being absent.** The subject who never travelled holds the same claims as the bench member who sat through it, so *a player can be condemned and not know it* is a claim about a sweep arm |

⭐ **And one CORRECTION to this lane's own headline diagnosis (`F-32`)**: *no deposit names the
actor* is false — one does, `(speaker, speech.made, 100, firsthand)`. **The defect is that
deposit's CONTENT**: the only claim about a speaker is that he spoke, which is the one shape the
question machinery cannot read. **`19_PLAN.md` step 2 is aimed one step to the left of the hole.**

### The shape, which matters more than the count

**No arrangement row is blocked on a parameter of its own** — all twelve stop on needs shared
across the catalogue. That is the closure claim holding in the only direction currently testable,
and it is why twelve rows have not yet bought anything. **Of sixteen steps in one worked trial
(`PART D`), the five that are supplied are all things the tree owned before this design existed.**
And **the clerk — somebody putting the matter on the docket — is in none of `12_BUILD_ORDER.md`'s
twelve steps**, which leaves its own step 9 BAR (*one seeded proceeding, zero authored acts*)
unreachable by its own plan for want of one act that costs nothing.

### What the suite got wrong, since it is the record that makes the rest readable

Two structurally independent read-only critics attacked the output without seeing its reasoning.
They **killed two findings** (the `convene` `scale:` key is live at `verb_table.yaml:138`, not gone;
`disposal_reach` does NOT need a sixth channel — `_ch_post_remit` and `_ch_chronicle` already carry
`body` and `<rung kind>`), **overturned a third as stale** (P-15 is closed by `ED-SC-0034`; the
gap-register row is what is stale), **voided one execution** (a docket test ran one season against
a date due at tick 1 and measured its own off-by-one), and **corrected four counts** — including
`runnable = []`, which was an identity that could not have come out otherwise. All applied in place;
`PART F` is the record.

## ⚠ 2026-09-07, LATER — THE REVIEW, AND PHASE 0 EXECUTED

**`21_RECONCILIATION.md`** — a read-only Fable 5.1 pass over the stress report's PARTS A–F against
`04_CODE_ARCHITECTURE.md` and R1–R8, **with every decision-changing citation re-verified by hand**.
Twelve conflicts ruled, **zero escalations**, a five-phase plan. **PHASE 0 is executed** and its
falsifiers are green: `ST-06 · ST-12 · ST-13 · ST-23 · ST-27 · ST-37 · ST-38` all return RAN.

### ⛔ Four of the stress report's results did not survive, and the next actions below are retracted

| was | is |
|---|---|
| ~~*`F-14` is the one that needs a design answer*~~ | ⛔ **answered before it was written.** `19_PLAN.md` step 15: *the declaring act is the determination … the declaration writes the disposal.* The finding is real and its grade was wrong — `04_VERBS.md` §B.2 had been corrected **away** from the plan. **Now fixed in the row**: `determine` writes `Tenure.since` + `Tenure.degree`, degree-keyed |
| ~~*`F-32` re-aims `19_PLAN.md` step 2*~~ | ⛔ **withdrawn — this lane's original diagnosis was right.** `claim_subjects` **replaces** the actor with the act's referents when the act names a subject and writes nothing; `ST-32` ran a `speak` with no payload, so the actor survived by the default branch rather than by the rule. **I refuted a claim by running the case it was not about.** `R8.1`'s struct supersedes step 2's mechanism |
| ~~*`ST-34` could not run the deprivation floor*~~ | ⛔ **withdrawn.** `p_success` is at `engine/autoload/sigma_leverage.py:246`; the suite searched `dice_engine` only. **`M-7` and `M-8` are runnable today** |
| ~~*`F-05`: the docket never names a matter, so a clerk is mandatory*~~ | **re-cut sharper.** `exists:DocketItem` returns `UNKNOWN` — `docket` is a state *sequence* and the reader looks for a *collection* — so **the design's `speak` cannot form at all.** The fix is a reader branch plus `open_case` gaining the write |

⚠ **Three "what executes today" claims are also corrected**: `ST-09` ran the **pre-design** `speak`
row; `ST-35` replays a season rather than a seam draw; `ST-36` permutes deliberation order rather
than attendance, against an Event multiset rather than the hash.

### What PHASE 0 changed, all of it documentation

`10_LOOPS_AND_GAPS.md` (five orphan rows filed; `P-08`/`P-15`/`P-29`/`P-33` closed with citations) ·
`00_DERIVATION.md` §B.1 (three stale cells) · `03_PARAMETERS.md` (header; the inverted `vacant`
claim) · `08_SEAM.md` §D.1 (four wrong emission kinds, and which column fires when) ·
`04_VERBS.md` (`determine`'s row per C-1; the `basis` operand; `path` → `contain_path`; the five
investigation rows onto the one ladder; the stance owner named on all three bands) ·
`12_BUILD_ORDER.md` (the docketing step, which was in none of the twelve) · `19_PLAN.md` step 22
(the field is the doctrine's, not the plan's).

**Six stress-test instruments were rebuilt in the same pass**, because they were substring searches
that could not observe their own fix — a falsifier that cannot fire green is not one.

---

# ⭐ THE HANDOFF — where the proceedings work stands, and what to do next

**Written at session close 2026-09-07, PR #376 merged. Read this before anything else in this file;
everything below it is history.**

## The state in one paragraph

**The proceedings subsystem is PROPOSED, held back in full, and does not run.** Nothing in PR #376
changed that — it touched **zero lines under `engine/` or `systems/`**. What it did was measure the
design against the executable tracer (38 tests), reconcile the results against
`04_CODE_ARCHITECTURE.md` and R1–R8 (twelve conflicts ruled, zero escalations), and execute the
corrections that carried no design decision. **The design is now accurate about itself in about
fifteen places where it was not.** The game is where it was.

## What is DONE and needs nobody

| | |
|---|---|
| the stress suite | `proposals/2026-09-05-proceedings-subsystem/20_STRESS_TESTS.md` — **a closed record, not a work queue.** Reproduce: `python3 stress/stress_proceedings.py` |
| the reconciliation and the plan | `21_RECONCILIATION.md` — **this is the file a next session reads.** PART C rules the conflicts; PART D is the ordered plan; PART E is what must not be done |
| PHASE 0 | executed. Ten edits, falsifiers green (`ST-06 · ST-12 · ST-13 · ST-23 · ST-27 · ST-37 · ST-38`) |

## ⭐ WHAT TO DO NEXT, in order, and the first one is the only one that matters

> ### ✅ **UPDATE 2026-09-07 (PR #379, `ED-IN-0202`) — action 1's PREDICATE HALF IS DONE, and it reaches further than this handoff said.**
>
> `_ch_document_key` now tests the subjects in `changes[]` instead of `e.subject`, so **`R5`'s
> bureaucratic channel fires on acts.** Two falsifiers, both mutation-checked (green repaired, **red**
> on the pre-repair predicate); seeded hashes identical on all three fan-out arms, because the live
> arm is `total`, under which channels are never consulted.
>
> ⚠ **The claim below that the channel *fires for nobody but the author* is FALSE of the mechanism.**
> It is true only of Carin's world, which holds no rung. `_eff_transfer` subjects its `StateChange`s
> to the RUNGS, so a person holding the destination witnesses `transfer.made` without acting —
> executed, and pinned by `test_r8_4_document_key_reaches_a_non_author_through_a_store`. **`H-84`
> blocks the RECORD route only**, and nothing was invented to get round it.
>
> **So action 2 (fan-out off `total`) is now unblocked** — C-3's ordering constraint is satisfied for
> the store route. The Record route stays blocked on `H-84`, whose owner is *Part E — the verb that
> would do it*, and which forbids in terms inventing a `give_record` to make a case pass.
>
> ⚠ **And one consequence that is `PHASE 1` step 3's, not step 2's:** a `document_key`-only witness
> now learns WHO ACTED, because `observers_for` discards which channel admitted a person and
> `claim_subjects` under the default `both` rule starts from the actor. `R8.5` cites a ratified line
> pointing the other way. That asymmetry was vacuous while the channel was dead; it is reachable now.


**1 · `R8.4`'s `document_key` repair — `IN` lane, and it is the first step that moves the game.**
`shape.py`'s `document_key` channel tests `t.object == e.subject` while every fold Event sets
`subject = actor` and no `hold` Tenure takes a person as object, **so the channel cannot fire on any
act at all.** Repair: test the changed record in `changes[]`. ⚠ **It must land BEFORE the fan-out
flip** or `M-6` measures a starved propagation chain rather than a narrowed one
(`21_RECONCILIATION.md` C-3). Everything about absence, secrecy, hearsay and `R5`'s bureaucratic
fact is behind it.

**2 · ✅ DONE 2026-09-07 — fan-out off `total`** (`19_PLAN.md` step 1, `ED-IN-0205`, `IN` lane).
`engine/season/data/fixtures.py` ships `all_five`; `total` stays as `H-33`'s control arm and the
channel list is untouched. **Forced by `R7`** — `total` is the echo model Jordan refused, arriving
at the deposit layer.

- **The artifact.** Two persons' witness deposits differ after two seasons and are **identical under
  `total`** — the control sits inside the same test. Deposits 649 → 60; ledgers `[200,200,200]`
  (pinned at the cap) → `[0,28,32]`. **Control: 122 probes, ZERO verdict changes** (63 PASS / 59
  GAP before and after); the run artifacts re-baselined and the deltas are in the commit.
- ⛔ **`M-6` cannot fail as specified and is not reported as passed.** `_r3_propagates` walks
  `Event.causes[]` and never reads a ledger, so the corpus tallies are identical across all three
  arms **both co-located and dispersed to distinct rungs**. What is claimed is links 1 and 2:
  questions raised hold at 5/9/10 under `all_five` and fall to 5/8/8 under `presence_only`, which
  is the measured reason for the arm.
- ⚠ **One cost, recorded and not acted on.** At the shipped `observation_deposit_mode: actor`,
  `W-D`'s 16-fork slice diverges 2 at `total`, **0 at `all_five`**, 7 at `presence_only` —
  non-monotonic. Half the channel survives (widened fingerprint: 8 vs the control's 6). The arm is
  not re-chosen on 16 forks whose question order `H-54` says is decided by hash ordering 75% of the
  time. Both numbers are pinned in their own tests.
- ⚠ **And the flip retired a registered argument.** The ledger cap now evicts **nothing** in any arm
  (48/49/204 → 0/0/0), so `H-40`'s decay sweep is observable in every deposit arm and `H-122`'s
  first reason for defaulting to `actor` is gone. Its second — form 6 recording a holder-relative
  value in the wrong holder's ledger — is a correctness argument, untouched, and is why the default
  does not move. Recorded on the row.

### ⭐ DIAGNOSED — why the shipped arm shows zero, and why the arm is not chosen on it

A fork reaches a later decision by exactly **one** route: §F1 clause 4 (`shape.py:627`,
`belief_contradicts`) — a claim in the actor's own ledger contradicts a candidate's precondition,
so the candidate is dropped. Counting that population over the same 89 worlds
(`wd_extra.corpus_drops`), at `observation_deposit_mode: actor`:

| `fan_out_mode` | clause-4 drops | fork divergences |
|---|---|---|
| `total` | 37 | 62 of 1467 |
| **`all_five` (shipped)** | **0** | **0 of 1467** |
| `presence_only` | 114 | 229 of 1467 |

**The divergences track the drops exactly.** The zero is neither a property of the arm nor a defect
in the channels: at the shipped configuration **clause 4 never fires**, so a fork has nothing to
change. Beliefs still form there (22 false-when-recorded); they contradict nothing.

⭐ **And the reason is the finding.** Every clause-4 drop in the entire corpus, in every cell, is
the verb **`move`** refusing on a **`contain.path:<person>`** belief — *there is no road from here
to there*, formed by witnessing a `travel.blocked` and overturned by a later `travel.moved`.
Nothing else in the corpus fires clause 4 at all. So the metric measures **people being wrong**,
and a wider channel set does not suppress propagation — **it corrects the stale belief before it
can bite.** Better-informed people refuse fewer acts.

⚠ **So the arm is not chosen on this metric in either direction.** It is a monoculture: one verb,
one predicate, one stale-belief shape. Choosing an epistemic model to preserve `move`'s refusals
would tune the design's whole knowledge layer to protect a single worked instance. **The defect it
exposes is that §F1 clause 4 has exactly ONE reachable instance in the corpus** — a producer hole,
and the place the next work goes. The shipped arm stays `19_PLAN.md` step 1's, which is also the
only arm that produces a secret between two people in the same room.

**2b · ⚠ The Record route is still blocked on `H-84`,** whose owner is *Part E — the verb that would
do it*, and which forbids in terms inventing a `give_record` to make a case pass. The STORE route is
open and executed (PR #379). Nothing was invented.

**3 · ⛔ The obstacle needs a ceiling, and this is new.** `M-7` was run for the first time and
**fails**: at the 1D pool floor `p_success` is `0.2266 / 0.0228 / 0.0006` at Ob 1/2/3 and **0.0000
from Ob 4** — reaching effectively zero at a value `opposition_score / 2` produces alone against a
score of 6, before any room term. **And remedy (a) is refuted**: σ-leverage at the floor against
Ob 7 gives `0.0000` at net_σ 0, 1, 2 **and 3**, because a channel uniform in Δz cannot lift a
probability already at zero. **So `06_RESOLUTION.md` §B.3a's remedy (b) — a ceiling — or a higher
pool floor is what is left.** ⚠ Magnitudes are `MD-07`'s injected set; 1D is the pathological pool.

**4 · Then PHASE 2** — the six rosters and the arrangements loader, `judging_set`, `release`,
`convene`, the docketing step, `determine`'s row, the provider, and the BAR.

## What is genuinely open, and it is not much

- **Nothing needs Jordan.** All twelve conflicts closed on `CLAUDE.md` §0's five tests. The one that
  came closest is `C-7`'s quorum: a filtered-cardinality eighth form would be more expressive and is
  **refused by default**, with its trigger named — if a non-bench person's commitment counting toward
  quorum reads wrong in play, that is when it is earned, and it must be argued then.
- ⚠ **One `IN`-lane defect this design revealed and does not own.** The write gate's `F3` clause has
  four exceptions and a conferral-basis opener matches none — **so `confer`, a live `ruled` verb,
  would be refused by the gate as specified**, and `determine` opening a disposal needs the same
  clause. **Register it in `IN`; it is not this lane's to fix.**
- ⛔ **The retirement wave** — cross-lane, ruled 2026-09-06, still unexecuted. 47 files, 20+ inbound
  sites. Not this lane's PR.

## ⚠ Two method lessons this session paid for, worth more than any single finding

1. **Six falsifiers were substring searches and could not observe their own fix.** A correction that
   quotes a retracted claim while withdrawing it still read as the defect, so every one of them would
   have gone on failing after its target was corrected. **A test that cannot go green when the thing
   it names is fixed is not a falsifier** — `§0.1` point 2 from the other side.
2. **Three things written as *Registered* / *blocking* / *done* had never been exercised** — five
   orphan `P-` rows, `M-7`, and `12_BUILD_ORDER.md`'s missing docketing step, whose absence made its
   own step 9 BAR unreachable. **Writing the citation is not filing the row.** ⚠ And the M1 gate's
   own row 4 (`0/7`, self-declared DOC-DERIVED) is the same disease at the milestone scale.

---

- **Three-lens pessimistic NERS audit + upload delta FILED 2026-08-06 (ED-SC-0017..0022).**
  `audit/2026-08-06-social-contest-three-lens-audit/` (synthesis + working records). Three read-only
  Fable 5 lenses (primitives / mechanics / emergence) relayed agonist→antagonist per CLAUDE.md §10;
  every gating claim re-verified by the orchestrator against the working tree (verification log at
  synthesis §1). **Headline: the subsystem is three resolution models wearing one name**, and the
  canonical head's entire §4 loop has no engine while the kernel's actual loop has no canonical prose.
  - **P1 · ED-SC-0022 — bug batch, do first, no design authority needed.** F1: Stage 3 is unreachable
    in production (`build_contest` has no armature parameter → CR4/armature/CR5 fire only in tests).
    F6: the "one-season" Mandate −1 is **permanent** (no temporary-modifier facility exists in
    `season_manager.py`). Plus 6 more (F2–F5, F7, F8).
  - **P1 · ED-SC-0019 — no record spine, and it is a composition failure, not a gap.** The Record
    primitive already exists single-owner at `systems/settlements/sim/ledger.py:7-14` (`Precedent` /
    `Grudge` / `Debt` / `Reputation` / `Leverage`, durable across succession). Compose on it rather
    than emitting bespoke stat deltas. Sibling: M2 Scope — a contest win binds a whole faction with
    no authority check and no repudiation path.
  - **ED-SC-0017 closes ED-SC-0005 without a new number:** CR6 already ratifies a tanh soft-cap at
    `M_MAX = 1.5σ` and the kernel already enforces it — the doc's four flat pool dice violate the
    subsystem's own ratified substrate. Also: `params/contest.md` is cited 97× across the kernel and
    was evacuated 2026-08-05 (content safe in `engine/engine_params/params_tables.yaml`; citations
    dangling), and `CURRENT.md:151` cites an audit directory that no longer exists.
  - **ED-SC-0018:** ED-1062 fixed Memory's CR4 reachability and left Projection's identically broken —
    CONSEQUENCE/FEASIBILITY is no proceeding's start ground and the doc specifies no reframe action.
  - **⚠ TWO FORKS NEED JORDAN, held back explicitly per CLAUDE.md §2, not bundled:**
    **ED-SC-0020 (Fork A)** — adopt a burden-parameterized gate? We already have the burden family in
    disguise (ProofBar / GraceThreshold / TallyAtClose) and lack only stall semantics; adopting
    replaces four WinCondition classes + two biased track starts + the tracker tri-state with one
    Venue field. *Audit recommends ADOPT.* **ED-SC-0021 (Fork B)** — the armature is not an
    anti-collapse device (all four Styles produce identical state changes differing only in one
    upside-only scalar; the orientation bit is dominated contest-wide, and CR5's cost half is wired
    while the Doubt Marker upside is not). *Audit recommends warrant × attack — but the falsifier
    (AI-vs-AI best-response sweep) has NOT been run; do not ratify without it.*
  - **Cut docket: ~800 lines** off the live surface, of which ~50 are the only ones a player would
    have noticed (synthesis §4.3). Includes moving the banner-superseded
    `social_contest_system_v2.md` (+ index, 513 lines) out of the live subsystem folder.

- **Auto/Manual Resolution Duality doctrine RULED 2026-07-08 (ED-SC-0013 → resolved).**
  `designs/architecture/auto_manual_resolution_duality_v1.md`, reworked per Jordan's "specific events on a
  slate" steer to lead with the **Scene Slate as the spine** — already canon (`player_agency_v30 §4`:
  deterministic, priority-ranked, settlement-anchored, Conviction-biased SPECIFIC events; 3–5 scene-action
  budget; "opportunities not pursued resolve through NPC AI without player input" = the auto-resolve). Fidelity
  is a SPECTRUM (played / witnessed [Witness Mode] / auto); precedents FM/Total War/CK/XCOM/Disco Elysium.
  **Forks ruled (Jordan: resolve A/B/D, keep C):** A = one engine event-parameterized; B = the Slate's budget/
  priority/Conviction triage + Mandatory §4.3.2; D = Mandatory/opt-in/Witness — all RESOLVED (A by steer, B/D by
  existing canon). **C (calibration tolerance) is the one residual** — carried to ED-SC-0011's parity-harness
  acceptance gate. **Load-bearing constraint:** E[auto]≈E[played] (exploit-prevention). **Chief build implication
  (next, separate item):** event-parameterize the auto-resolver so it resolves SPECIFIC slate motions, not a
  generic per-season roll; then ED-SC-0011 (the zoom-in expansion) + the parity harness.

- **Social-contest staged rebuild (`claude/happy-shaw-da0f1d`, IN PROGRESS).** Agonist/antagonist gated rebuild
  of the contest engine: promote the stranded 62-test groundup engine (`designs/audit/2026-06-03-contest-groundup/`,
  actually **9 modules / 151 tests green**) onto the v30 surface + fold in CR1–CR7, build all four deliberative
  games (Agôn/Negotiation/Inquiry/Consensus), close J-36 seams, drive to settled canon (T-25 + sim-validation).
  Plan: `C:\Users\Jordan\.claude\plans\this-is-a-broader-nested-mountain.md`. Runs stage-by-stage via the Workflow
  tool (Opus agonist/antagonist/judge + Haiku scribe), Jordan ratifies each gate; cadence = auto-advance, interrupt
  only for design-authority forks.
  - **Stage 0 (Foundation) DONE + Gate 0 RATIFIED (2026-06-30).** Reconciliation contract + decisions:
    `designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md` (+ raw map + gate packet). Three ratified
    forks: **D0-1** appeal ethos/pathos/logos = build both multiplicative+additive behind a flag, decide by seeded
    A/B (player-win-rate vs venue-identity-spread); **D0-2** σ-leverage → new numpy-free `sim/autoload/sigma_leverage.py`
    sibling (retires the test-dir/numpy/sys.path-hack + the two-σ-kernels debt); **D0-3** TN6/7/8 divergence + Jordan's
    fractional-Ob idea → contest stays δσ TN7 (unaffected), open a substrate probe (reopens CR6 uniformity), non-blocking.
    Good news: `faction.py` already has BG-Vote/Succession/committee-band → Consensus mostly promote-existing.
    IDs reserved: `contest_rebuild` = ED 1055-1079 / PP 800-809.
  - **Stage 1a DONE + committed (d64e2ffe).** `sim/autoload/sigma_leverage.py` — numpy-free σ sibling, byte-identical
    to the oracle, 623 tests green; two-σ-kernels debt retired.
  - **Stage 1b DONE + committed.** 9-module kernel promoted to `sim/personal/contest/`, rewired onto the σ sibling
    (no third kernel); `degree` = clean carry-across (pool-aware integer degree added to sigma_leverage, distinct from
    `dice_engine.Degree` combat enum); old stub → `contest_legacy_stub.py`; 815 sim tests + both importers green.
  - **D0-3 RESOLVED → HYBRID** (present-as-Ob display over the δσ substrate; CR6 upheld, not reopened). Memo:
    `designs/audit/2026-06-30-contest-fractional-ob-probe/MEMO.md`; decision → ED-1055. Probe also surfaced a LIVE
    combat bug (`dice_engine.roll_pool` ignores `tn`; TN5/6/8 weapons rolled at TN7 rate) → spun out as a
    combat-lane task (`task_210994b7`, out of contest scope — see `registers/handoffs/HANDOFF_PC.md`).
  - **Stage 1c DONE + merged into main (PR #44, all CI green).** v30 re-skin (8 proceedings, Persuasion Track
    banding, 4 adjudicator types) + `build_contest`/`resolve_contest` wrapper + MECHANICS registry, mirroring
    `tests/sim/mass_battle/engine.py`. 888 tests green.
  - **Stage 1d / Gate A DONE — 3 forks ratified by Jordan (2026-07-01).** Propagated CR1 (wrapper, confirmed
    already-realized)/CR2 (σ-substrate, confirmed already-realized)/CR3 (three trackers: Concentration+Face+
    Persuasion, Composure retired — contest-scope only) into prose (`social_contest_v30.md` §4/§8 + co-files,
    `params/contest.md`) + code (`sim/personal/contest/` Face primitive) + ledger (ED-1055, ED-1056). Packet:
    `designs/audit/2026-07-01-contest-gate-a-packet/GATE_A_packet.md`. **Ratified:** (1) Face scale-binding =
    combo formula, not a straight rescale — `Face_max = Charisma×3` (ceiling, player-build-controlled) +
    `Face_current = round(Standing/10 × Face_max)` (position within ceiling, earned through play, Standing's
    kernel math/Readiness/leak feed untouched); (2) Composure retirement scoped to the contest tracker only
    (knots/combat/conviction untouched, confirmed); (3) provisional EDs use non-basis citation phrasing until
    ratified (standing policy). A small Sonnet-tier finalize pass is applying the resolved formula + 4 agreed
    nits (dead imports, ED-1056 recitation, prose wording, TRACKERS sourcing); that pass also caught the ratified
    Face formula shipped with zero test coverage and added 10 targeted kernel checks (boundary cases, midpoint
    round-half-to-even, non-mutation, live-tracking). **Committed (884cf89a).** 1041 sim+valoria + 244 kernel
    checks green. Push to `claude/happy-shaw-da0f1d` updates the open tracking PR ([ttrpg#44]) — Jordan merges,
    not this session.
  - **NEW standing requirement (decision 5, 2026-07-01): the player-interaction model is a concrete deliverable,
    not a late audit.** First-draft walkthrough seeded ahead of Stage 6 so every later stage designs toward it:
    `designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md` — setup screen,
    the exchange loop (Appraise / style-choice cards / roll-and-resolve / Face+Concentration bars), the
    resolution screen, and how Negotiation/Inquiry/Consensus should each look different from Agôn's track meter
    so Stage 4 doesn't converge them onto one UI. Stage 2 now owns authoring the Style/Venue flavor text; Stage 3
    now owns the Appraise-reveal boundary for `armature_position`; Stage 4 now owns each game's interaction
    shape; Stage 6 finalizes+ratifies the model this seeds. Plan file amended accordingly.
  - **Gate A committed (`884cf89a` mechanics + `98ecdf41` player-model), PR #44 all-green.**
  - **Stage 2 / Gate B (dictionaries) DONE + committed.** Built Venue×8 / Adjudicator×4 / Style×4 /
    InteractionType×4 typed dicts (`sim/personal/contest/dictionaries.py`, new module) + Style/Venue
    flavor text; closed ED-137 (Panel adjudicator). Packet:
    `designs/audit/2026-07-01-contest-gate-b-packet/` (pre-ratification snapshot + the authoritative
    `GATE_B_closeout_audit.md`). **Ratified and independently re-verified in actual code (not just ledger
    text):** Panel votes weighted-by-standing (ED-1057; reuses the existing `Adjudicator.discipline` field,
    NOT the contestant `Standing` name — no new state invented); Panel reachability = rebind Guild
    Arbitration's adjudicator → Panel (ED-1059; NO appeals — "let the decision ride"; roster stays 8);
    Terminal Doubt = terminal-value-everywhere, banded (PersuasionTrack) + tally (TallyAtClose) branches
    both specified (ED-1060); Guilds "GM picks" boost = context-derived from the venue's dominant
    ethos/pathos/logos via the existing `Appeal` machinery (ED-1061; literal "GM picks" text removed from
    both prose heads). ED-1055/1056/1058 flipped to `status: ratified` (a bookkeeping fix — they were left
    `provisional` only because two earlier finalize-workflow attempts were killed by infrastructure
    issues — API 401/529 errors and a background-task stop, unrelated to the work itself — before
    flipping their own metadata; the ratifications themselves happened earlier via Jordan's answers).
    1041 sim+valoria + 319 kernel tests green; freshness gate clean (5/5 fresh); no scope drift (grep
    confirmed knots/combat/conviction untouched, Composure retirement still contest-scoped).
  - **SOURCE-RESEARCH GROUNDING (found 2026-07-01 via files13.zip → already in repo, NOT orphaned).** The
    deliberation-critique source research
    `designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` (a 3-part
    Renaissance-deliberation / machination-games-lens / model-testing trilogy) is READ-AND-CITED-BUT-NOT-APPLIED:
    it shaped the plan's four-games / alea / consensus / commitment-store / armature *shape* via `critique.md`,
    but its rich detail (Dowlen small-pool weighted lottery; `liberum veto` as self-undermining equilibrium;
    Padgett robust action; Putnam two-level bargaining) is not yet in the code. Plan amended: Stage 3 (armature)
    and Stage 4 (four games) agonists must now READ the source-research trilogy directly, not just the critique
    distillation, so this commissioned scholarship actually reaches the implementation.
  - **Stage 3 / Gate C DONE + RATIFIED (2026-07-02, ED-1062)** — rhetoric grounding + adjudicator
    armature (CR4 stasis, CR5 self-gating, 4-axis Style×Conviction dot-product) landed; packets:
    `designs/audit/2026-07-01-contest-gate-c-packet/` + `2026-07-02-contest-gate-c-packet/`.
    *(This line corrects the previous "NEXT: Stage 3" — the handoff trailed the ratified state by one
    stage; flagged as a currency observation by the 2026-07-05 audit below.)*

- **ED-SC-0030 (2026-08-06) — KEYS, KNOTS, NPCs AND THE COMBAT MODEL.**
  `audit/2026-08-06-social-contest-three-lens-audit/07_keys_knots_npcs_and_the_combat_model.md`.
  Six read-only Fable lenses, Opus authorship. **Coverage finding against this unit's own work:**
  `00`–`06` never opened `systems/combat/combat_engine_v1/` — the repo's own reference
  implementation of "multiple tracks and balances", on the *same* σ-kernel — and no CIP addresses
  repetition or Knots. **NEW FINDING — the Standing dead zone:** `frac()` is `(v−5)/5` clamped, and
  both consumers read `frac`, so **Standing 0 and Standing 5 are identical in reception**; the cliff
  belongs there (`discredit_bar`), not in a re-founded `frac`. **Combat's rule made testable:** tracks
  may only multiply/gate process or terminate — no fixed-rate conversion into `adv`. That guard
  **lands first**. **OF-CAP is now rulable:** `cascade_depth_max = 3`, `emissions_per_tick_max = 64`.
  **Live latent break:** `drain_tick` has zero production callers; the first scheduling subscriber
  makes `next_tick` raise. **Knots:** `public_citation` rupture is *unfireable in principle* —
  `EvidenceItem` has no provenance, which gives W3 a second consumer. **Churn: insufficient** — the
  auto path repeats to campaign end; the repeat detector ships **xfail**. **Ten corrections to filed
  work, seven of them mine.** Nine forks, incl. the missing NPC lane.

- **ED-SC-0029 (2026-08-06) — PROPOSAL REWRITTEN (v2).**
  `proposals/social_contest_consolidation_integration_v1.md` (filename kept per CLAUDE.md §4 —
  renaming breaks ~a dozen ED citations; the header carries v2). Restructured around Jordan's eight
  requirements + seven world questions, which are now the **grading standard** (§1), each naming its
  owning CIP. Five new corrections C-8..C-12. **Four new proposals, three of them net removals:**
  CIP-13 (decorum operator — one graded owner absorbs `RhetoricalWeights` + the venue tense trio +
  CR4's +1D, deletes `Stasis.TENSE`, retires the `hard` verb), CIP-15 (per-venue rung vocabularies,
  translatio extracted, genre decomposed), CIP-7c (institutional party — and it **settles
  `split_standing`**, whose only in-bout consumer is the `hard` verb CIP-13 kills), CIP-14 (the
  audience as a party — the headline, with all four of its conditions stated). **CIP-2 strengthened,
  not shrunk:** warrant schemes carry their own critical questions, so there is no warrant × attack
  matrix to author at all — the C-5 retraction was solving a problem that stops existing. **CIP-12
  reframed** into the reconciliation of three unreconciled second currencies, with a proposed ruling:
  one currency, two holders. **Strict sequencing CIP-9b → CIP-12 → CIP-14** (unsound before the
  first, ambiguous before the second). **10 forks need Jordan**, including a new one: the programme
  has never been counted against `04`'s eleven-primitive irreducible set. ⚠ **File is 14,503 tokens
  against the 15,000 blocking cap — the next substantive addition must split into `_part2`.**

- **ED-SC-0028 (2026-08-06) — ADVERSARIAL AUDIT OF ED-SC-0027 + CORRECTIONS.**
  `audit/2026-08-06-social-contest-three-lens-audit/06_adversarial_audit_of_05.md`; `05` revised in place.
  Three read-only Fable critics found four broken claims. **CRITICAL:** `05`'s headline
  ("the contest is sealed off from the world in both directions") is FALSE at the scope written —
  `mc_v18.py:148-151` runs `parliamentary_bridge` every season (ECHO_TRANSPORT default ON),
  `_derive_vote` generates a topic from world pressure, and `parliamentary_vote.py:206-216` writes
  back. **`05`'s own falsifier named that exact test and was never run.** Surviving claim: the
  personal-scale Bout kernel is sealed. **THE INSTRUMENT WAS BROKEN:** the two-category test lost
  its "…that anything reads" rider and graded kills against the kernel-as-built while grading
  withdrawals against the architecture-as-proposed — a rescue licence, and it was used (the
  FactionBoost→disposition-matrix category error). Repaired with two riders. **The duality claim
  does not hold** without CIP-9b, an unratified amendment `05` never cited. **"No new primitive" is
  false** — `ledger_add` is single-valued by kind, and there is no holder dimension: one primitive,
  extended cross-lane, **needs SE**. Architecture reduced to 8 tracks / 8 edges / 2 config surfaces /
  1 ledger interface by `05`'s own rows-not-code rule. Warrant-vs-appeal downgraded to undecided;
  `00` Fork B's sweep condition reinstated. **18 forks open, all needing Jordan.**

- **ED-SC-0027 (2026-08-06) — TRACK ARCHITECTURE + STATE GRAPH, organised by Jordan's requirements.**
  `audit/2026-08-06-social-contest-three-lens-audit/05_track_architecture_and_state_graph.md`.
  Eight requirements (C1-C4 character: HOW one argues = rhetoric x temporal · WHAT · WHY · HOW
  effectively; P1-P4 type: WHAT KIND · WHO adjudicates · HOW adjudication occurs · HOW audience
  impacts), seven world-interface questions W1-W7, nine tracks, fifteen interaction edges.
  **Fourteen forks filed, ALL needing Jordan (§10).** Headlines:
  (a) **Decorum is the content-dynamic weighting operator** — both lenses converged on one object
  from opposite directions; generalise the EXISTING binary relevance gate (`Stasis.relevant` /
  `Dossier.available`) from {0,1} to graded and it absorbs `RhetoricalWeights` + the venue tense
  trio + CR4's +1D. A 1:1 venue→style table is *anti*-decorum.
  (b) **Temporal orientation becomes an orator CHOICE**, not a lookup from the rung; `Stasis.TENSE`
  is deleted, which dissolves the DEFINITION past-vs-present incoherence (ED-SC-0026 item a).
  (c) **The contest is sealed off from the world in both directions — MEASURED:** the entire
  world→contest interface is two integers (`scene_dispatch.py:298`), every `EvidenceItem` in the
  tree is a hand-authored literal, and `systems/fieldwork/sim/investigation.py` is all stubs.
  (d) **"Lose the case, win the room"** — verdict and reputation route through different profiles to
  different consumers. Supplies the foundational choice `04` found missing and satisfies the
  duality doctrine on its own terms.
  (e) **Six priors (3 objects x 2 holders)** read from the same `LedgerTag` ledger the contest
  writes — loop closed, no new primitive.
  (f) **TWO OF MY OWN VERDICTS CORRECTED:** `split_standing` (ascribed Rank vs earned Credit) is the
  institutional-party primitive, not excess; `FactionBoost`'s *table* is authoring data for the
  faction disposition row even though its *die* dies.
  (g) Genre is NOT rescued — both lenses rejected chosen-vs-terrain-genre divergence independently.

- **ED-SC-0006 + ED-SC-0007 DONE (2026-07-08)** — kernel routing, party-derivation bridge, the
  composed-keying echo mapping, the P3-lite Agôn harness, and Censure-tier parliamentary-vote
  wiring are all executed; see Decisions above.

- **JORDAN RULING NEEDED: ED-SC-0015** (Parliamentary total-victory Mandate stacking, −2 vs −1) —
  the one open design call this session's build could not resolve on its own authority.

- **`contest.py` fabrication-debt triage** — 19 uncited constants block the J-31 terminology
  propagation into code (also tracked at `decision_queue.md` item 16).

- **contest_rebuild Stage 1+ gates** — each stage ratified individually (Gate 0 ratified
  2026-06-30; ED 1055-1079 / PP 800-809 reserved; Gates A–C ratified through 2026-07-02; also
  tracked at `decision_queue.md` item 15).

---

## 2026-08-27 (later) — the seam landed, and the instrument it broke (ED-SC-0032)

**Read this before touching `tools/balance_oracle.py`.** ED-SC-0032 moved `degree` and
`OVERWHELM_SIGMA` out of `engine/autoload/sigma_leverage.py` and thereby **broke the balance
oracle's live arm**, which read both off the engine. `python3 tools/balance_oracle.py` raised
AttributeError. Nothing caught it, because nothing executes that file — it is deliberately not a
CI gate (240 campaigns, ~13 min), so it has no freshness relationship to the code it measures.
The instrument that produced ED-SC-0031's control was disabled by ED-SC-0031's own successor.

Repaired, and `tests/valoria/test_balance_oracle_arms.py` now constructs both arms and asserts
they band differently at `degree(3, 3)` — cheap, runs no campaigns, mutation-verified.
**The general lesson, which is not confined to this tool:** a deliberately-uncalled instrument
needs a cheap liveness test or it rots silently. If you add another one, add its arm test too.

### Still open in this lane

- **Nothing about the degree ladder.** All four rulings are executed or accepted; the RULINGS
  block at `tests/valoria/test_degree_ladder_single_owner.py` is the record.
- **The bridge's shut-out set** has taken three values under three unrelated mechanic changes
  (`{'Hafenmark'}` -> `set()` -> `{'Church'}`), which is evidence it tracks the seed, not the
  spine. Only ever measured at n=8/seed-42. Settling it needs the n>=100 arm. **FA/WR-lane.**
- **The seam has exactly one consumer.** `PoolDesaturation` is the only `BandExtension` in the
  tree. That is correct today — no other subsystem has asked for one — but it means the contract
  is proven by probes rather than by a second real user. If a second subsystem wants an
  extension, expect the "veto the top band only" power to be the thing under pressure, and widen
  it by ruling and ledger entry rather than by convenience.

---
