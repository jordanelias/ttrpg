# VERBS · PHYSICAL · D — `thread_read`: a graded diagnosis now, a priced working later

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) Stage 1 is the inquiries' form on the one roster `graded_tasks` (not `graded_routes`); stage 2 writes `Person.coherence` on every band, Failure included, so it is a contest row bound to the threadwork provider it re-points to (residue §1, shape (b)). (2) **A-5, A-7**: one sampler; the pool rule on the reader's score; Thread Sensitivity stays the one gate A-11 keeps. (3) **A-40** (the Thread is ground: one site a territory, no new entity kind) unblocks the Site half this file leaves waiting on a substrate; planning it is WR's (U5d's family). (4) **A-43** (zero coherence: a person no longer legible to others): what a `thread_read` of such a person shows is CHAR's and WR's to plan with that ruling; this file's stage 1 deposits a sensitivity reading and nothing about his reasons.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.4, 7b.5): stage 1 is an inquiry on `graded_tasks` (18-A renames the roster once; the `graded_routes` rename is withdrawn, D-U1-11i); stage 2 is a contest row (`contests: "a task"`) bound to the threadwork provider, blocked on its carriers (no writer of `Person.coherence` exists in the suite, `unified/U3_DEPENDENCY_ORDER.md` §6.3); `observes:` is flat with the band in `finding_terms` (C-24); A-81, A-30, U3 batch B35 and edge cut row 85, R4 7b.0 block. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "graded route" → "task route" (glossary *task*).

## Status: PROPOSED

Lands in batch: B35 (`unified/U3_DEPENDENCY_ORDER.md` §3.1); `17_CENSUS_REST_2_wiring` W3 lands with it (U3 §4.1 row 85). Stage 2 does not land in B35: it waits on a writer of `Person.coherence` (CP-T07-02, H-47; no carrier in the suite) and on `09_WR_B_threadwork_session_and_practitioner.md`'s module entry.
Depends on: `08_FI_03_playable-inquiry.md` §2 (B11: the `observes:` column); `09_WR_threadwork_module.md` (B03); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 2 (B07).
Lane: WR. Tier (R4 7b.0 (1)): stage 1 `sonnet`, effort `medium`; stage 2 `sonnet` producer with one `opus` read of WR's gate. Test file: `engine/season/tests/test_vm_phy_d_thread_read.py` (the audit's §9.7 test and the draw assertion as two functions).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the reader's trained score (A-6); talent as levels (A-7); a wound a level against the roll (A-8); Thread Sensitivity stays the one gate A-11 keeps. The draw takes `H(w.world_seed, w.tick, <actor id>, "thread_read.task")` (A-30). **A-81:** stage 2 writes `Person.coherence` at every band; stage 1's `finding.none` leaves the reader his own claim once the inquiries' `undeposited_kinds` edit lands (FI's; `14_VERBS_MATERIAL_E_knowledge.md`'s A-81 note).

Batches P-D1 and P-D2 of `audits/14_VERBS_PHYSICAL.md` §10.3. Carries that file's §9 and §0.6. Stage 1
lands after FI-03 §2's `observes:` column. Stage 2 lands after `09_WR_threadwork_module.md` and
CP-T07-02 (the Coherence carrier, H-47). Reference only (CLAUDE.md §0.05). Authored by Opus completing
a Fable lane cut off by the usage limit (2026-11-12).

## What it changes in `engine/season/` at runtime

- **Stage 1.** `thread_read` forms on a person and resolves by a draw (it is ungraded today: a
  deterministic success for anyone past the sensitivity gate). A success deposits whether the subject
  is Thread-sensitive and, on the better bands, how much.
- **Stage 2.** The draw's obstacle is the working's Three-Axis Ob, and every read, failed or not, costs
  the reader Coherence.

Declared movers: the realm pins in which the 4 sensitive persons formed `thread_read`.

## The problem (evidence)

`aperture 2 0`: formed 4, attempted 3, executed 3, each depositing only "a finding was made" (ungraded,
so `find_trail` keys nothing). Corpus: never attempted, listed as *EMITS AND WRITES NOTHING*. The row's
own note names its missing read, depth and cost.

## Exact edits, by owner

### Stage 1

| file (owner) | edit |
|---|---|
| `engine/season/verb_table.yaml`, row `thread_read` | add `referent_class: Person`. `requires_typed` becomes `all:` of today's `scalar_threshold` and `{form: relation, of: subject, relation: with}` (world-only). Add `counterparty: subject`, so the fold refuses a self-read (the reading of one's own sensitivity is already one's own state). `emits:` becomes degree-keyed `{Overwhelming: [finding.made], Success: [finding.made], Partial: [finding.made], Failure: [finding.none]}` (the inquiry form, which a route row may key, `data/verbs.py:868-876`). `observes:` (FI-03 §2's column, **flat**, C-24): `[{form: scalar_threshold, of: subject, scalar: thread_sensitivity, threshold_predicate: "thread_sensitivity.gate", comparator: ">="}, {read: band, of: subject, scalar: thread_sensitivity}]` as non-gating reads; which band deposits which is `finding_terms`' (Partial and better: "sensitive / not", firsthand; Success and better add the subject's sensitivity band, `band_floors`' reading of the same scalar). Update `requires_typed_note` and `writes_note` to cite this file. |
| `engine/season/rosters.yaml: graded_tasks` (18-A's one rename of `graded_inquiries`; the `graded_routes` rename is withdrawn, D-U1-11i) | add `thread_read` on the same provider and role as `examine`. |
| `engine/season/data/requires.py` | none, if the `observes:` loader accepts `of: subject` on `scalar_threshold`. Otherwise `OWN_STATE_STEMS`' `thread_sensitivity` must be admitted as a world read of another person on the observation path only `[verify at landing; if a new stem is needed it is a declared grammar change and is named in the commit]`. |

### Stage 2 (waits on WR)

| file | edit |
|---|---|
| `rosters.yaml: graded_tasks` | `thread_read` leaves the route roster: a row that writes on every band is a contest row (VRES §1 shape (b)), so it declares `contests: "a task"` with the prize's roll re-pointed to the threadwork module's `read` entry (`09_WR_threadwork_module.md` edits 1-3; `thread_operations` gains `read` if WR has not named it) `[ASSUMPTION: the `a task` prize row names `social_contest.roll`; a second prize row, or a per-verb module entry, is WR's to propose — basis: VRES §2 "a prize row exists for each distinct pair of (who hears, when it is fought)"]`. `manifest/registry.py::check_contest_prizes` refuses an unregistered pair. |
| `verb_table.yaml`, row `thread_read` | `contests: "a task"`; `writes:` `{Overwhelming: [Person.coherence], Success: [Person.coherence], Partial: [Person.coherence], Failure: [Person.coherence]}` (a failed read still frays). Emits gain `coherence.changed` (an existing never-emitted kind) on every band. `observes:` gains the subject's live `knot`/`tie` edges and his Coherence band (T07's definition). |
| `engine/season/loop/effects_*` (WR's choice of module) | `_eff_thread_read` writes the displacement the module's outcome returned, through CP-T07-02's carrier. The size is the module's draw, not a constant. |

## Gate (execution artifacts)

Stage 1: the audit's §9.7 test, plus a draw assertion: at the shipped pool, seeds 0-29 produce both
Success and Failure for one reader-subject pair. Stage 2: WR's gate, plus an executed read that lowers
the reader's resting point by the module's returned displacement at every band.

## Falsifier

Drop the `observes:` cell (a Success deposits only `finding.made`). Leave the row out of the graded
route (every attempt deposits the same flat finding, so the draw is absent). Stage 2: a read that
leaves `Person.coherence` unmoved at Failure.

## NERS reading

- **N.** It is the only loop verb of the threadwork arcs (M-PERC: 26 cases). Audit §9.9.
- **R.** A hidden capacity becomes discoverable, and later a priced and condemned act.
- **S.** The same task route and observation deposit as every inquiry. Stage 2 becomes a contest row
  on the one prize roster, its roll the threadwork module's.
- **E (last).** Stage 1 is data edits only. Stage 2 is one prize binding and one write.

## Cost class

Stage 1: edit. Stage 2: a small build on WR's module.
