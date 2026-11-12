# VERBS · PHYSICAL · C — looking: `examine`, `surveil`

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) `examine` and `surveil` keep the inquiries' own form (task rows that write nothing; residue §1): the roster is `graded_tasks`, and `surveil`'s Failure kinds `finding.none` and `watcher.seen` are both members of its `emits_on_refusal` clause `draw`. (2) **A-5, A-7**: the draw is the one sampler; the pool is the one pool rule on the watcher's `inquiry` score. (3) The per-sighting admission draw at `surveil_watch_rate[band]` stands: a success is watchfulness, not omniscience (D-44 and D-45: an error has an author; this channel shows less, never something false). (4) A-32 and A-33 (who learns of a change of office; a death) are untouched: a watcher learns what is done where he watches.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the roster C2 left "[name the roster at landing]" is named at the tree: `engine/season/rosters.yaml: witness_channels` (`:409`, ordered by precedence, with a `claim_source:` per channel) loaded as `data/rosters.py::WITNESS_CHANNELS`, each channel's predicate a function `epistemic._ch_<name>` found by derived name into `CHANNEL_PREDICATES` (`epistemic.py:690-700`), dispatched by `epistemic.observers_for` (`:794`), not `loop/witness.py` (this corrects `unified/work/R4_READ.md` 7b.5, which said the roster does not exist); the admission draw is keyed (A-30; `04` PART D 35) and gets a pinned golden (R4 §1.4, the F-PC-08(b) precedent); `surveil_watch_rate` ships `[ASSUMPTION]` values with a sweep and a control (R4 7b.5); the stale "pools `[2]`" evidence is marked pre-A-5/A-6; A-81, U3 batch B26, R4 7b.0 block.

## Status: PROPOSED

Lands in batch: B26 (`unified/U3_DEPENDENCY_ORDER.md` §3.1). C1's stamp and trail halves may land before FI-03 §2's `observes:` column; the `observes:` halves wait on it.
Depends on: `08_FI_03_playable-inquiry.md` §2 and `08_FI_04_small-edits.md` (B11); `14_VERBS_MATERIAL_A_mending.md` (B12: `sabotage` emits `site.damaged`, so `_check_covert_kinds` accepts it); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` item 2 (B07: `graded_tasks`).
Lane: FI. Tier (R4 7b.0 (1)): C1 `sonnet`, effort `medium` (data and a stamp); C2's channel `sonnet` producer, effort `high`, with one `opus` read of the admission sweep. Test file: `engine/season/tests/test_vm_phy_c_looking.py` (one function per gate; the admission draw's pinned golden is one of them).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the watcher's trained `inquiry` score (A-6); talent as levels (A-7); a wound a level against the roll (A-8). Draws: the inquiry's own `H(w.world_seed, w.tick, <actor id>, "<verb>.task")`; the channel's admission `H(w.world_seed, w.tick, <event id>, "surveil.watch")` per (watcher, Event) (A-30). **A-81:** `surveil`'s Failure emits `watcher.seen`, a deed deposited to those present; `examine`'s `finding.none` leaves the actor his own claim once `undeposited_kinds` is amended for inquiries (`14_VERBS_MATERIAL_E_knowledge.md`'s A-81 note; FI's edit).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (A-09) — one Layer 1 line corrected in the proposed note text: the rule is `04:260` (§B.3 `Rung`, "NEVER: any social aggregate"), not `:237`.

Batch P-C of `audits/14_VERBS_PHYSICAL.md` §10.3 (the first to land). Carries that file's §7, §8 and
§0.6. Adopts `08_FI_03_playable-inquiry.md` §2's `observes:` rows for these two verbs and does not
redesign them. Reference only (CLAUDE.md §0.05). Authored by Opus completing a Fable lane cut off by
the usage limit (2026-11-12).

## What it changes in `engine/season/` at runtime

1. The Sites at a person's own place reach his question, so `examine` (and the other Site-classed rows)
   forms where he stands (C1).
2. A sabotage leaves a findable trail. An `examine` that succeeds names the saboteur (C1).
3. `surveil` forms only on the place where the person stands (C2).
4. A successful `surveil` makes the watcher an observer, by a draw per Event, of what is done at the
   place for the rest of the season. A failed one is seen (C2).

Declared movers: every realm pin (`examine` 0 to some formations, `surveil` formations narrowed, Site
rows such as `restore` and `sabotage` gain formations at the actor's place: H-163's shared-class cost).

## The problem (evidence)

`aperture 2 0`: `examine` formed 1, attempted 0. `surveil` attempted 44, 6 `finding.made`, each
teaching nothing (`covert_kinds` = `[record.forged]`, which never writes a Rung or Site). 22 refusals on
`present_at` and `exists:Rung`. Pools `[2]` for everyone (the whole-dice reading before A-5 and A-6; under
the one pool rule an untrained watcher rolls `pool_default` plus the base).

## Exact edits, by owner

### C1 — `examine`

| file (owner) | edit |
|---|---|
| `engine/season/queries/world_q.py` | stamp term `sites_here(w, p)`: Sites whose `rung` equals `place_of(w, p.id)`, sorted. Stamped in `_stamped` under `Site`. |
| `engine/season/rosters.yaml: covert_kinds` | `values: ["record.forged", "site.damaged"]`. Note: *"`site.damaged` (14_VERBS_PHYSICAL_C): a sabotage is a deed done TO a Site, which `examine` (a Site inquiry) can uncover through `trail_of`'s written side. [ASSUMPTION; medium; revert: drop the value]."* `_check_covert_kinds` accepts it (`sabotage` emits it). |
| `engine/season/verb_table.yaml`, row `examine` | `observes:` per FI-03 §2 (the Site's `condition`; the `stores` of its rung). `referent_class_note`: append *"14_VERBS_PHYSICAL_C: `sites_here` stamps the Sites where he stands, so the row forms; REM-22's 'never attempted' closes."* |

### C2 — `surveil`

| file | edit |
|---|---|
| `queries/world_q.py` | stamp term `place_here(w, p)`: `(place_of(w, p.id),)` or `()`, stamped under `Rung`. |
| `rosters.yaml` | new roster `own_presence_declines` (`own_hold_declines`' shape): `values: [surveil]`. Read in `decision/options.py::opening_set` beside `OWN_HOLD_DECLINES`: keep `r` only if `r` is the object of one of `p`'s own live `contain` Tenures. Own state, no World. |
| `verb_table.yaml`, row `surveil` | `referent_class: Rung`. `emits:` `Failure: ["finding.none", "watcher.seen"]`. `emits_note`: *"`watcher.seen` (14_VERBS_PHYSICAL_C C2): the Exposure half of canon carried as a deed anchored on the watcher and witnessed by those present (no aggregate on a Rung, 04:260)."* `observes:` per FI-03 §2. |
| `rosters.yaml: witness_channels` (T, `:409`) | `values` gains `surveil`, placed **second**, after `co_located` and before `witness_key` (the list is ordered by precedence, strongest first; a watcher who is also in the room is credited to `co_located`); `claim_source:` gains `surveil: firsthand` (he saw it himself); one note sentence naming this file and the revert (drop the value). The channel admits observer `q` to an Event `e` when `e`'s place is the subject Rung of a `finding.made` Event of verb `surveil` by `q` in the same season, or lies under that Rung (`causing_act` to read the verb and subject, resolver-side; no new state). Admission is a keyed draw at `surveil_watch_rate[band]` (fixture, swept). The terms shown are `finding_terms[band]` (one mask). |
| `engine/season/epistemic.py` | one function `_ch_surveil(w, e, pid) -> bool`, found by derived name into `CHANNEL_PREDICATES` (`:696-700`; a channel with no function raises at import); `observers_for` (`:794`) dispatches it from the roster with no verb literal. *(W3-4a: the earlier `loop/witness.py::observers_for` is corrected; the dispatcher is `epistemic.observers_for`.)* The draw is `H(w.world_seed, w.tick, e.id, f"surveil.watch:{pid}")` through the one draw owner (A-30), with a pinned golden in the test (`04` PART D 35: a new draw must not move unrelated goldens) |
| `data/fixtures.py` | `surveil_watch_rate: {Overwhelming: 1.0, Success: 0.5, Partial: 0.25}`, `[ASSUMPTION: not decidable from the repository — basis: R4 7b.5; swept {0.25, 0.5, 1.0}, control 1.0 at every band (the band alone admits)]`, NUMBER row in `hole_register.yaml`. |

### Order of landing

C1 (stamp, covert kind, `observes:`). Then C2 (stamp, decline, channel, `watcher.seen`). The
`observes:` halves wait on FI-03 §2's column. The stamp and trail halves do not.

## Gate (execution artifacts)

Audit §7.7 and §8.7. `aperture 2 0` and `2 1` before and after: `examine` attempted above 0; `surveil`
refusals on `present_at` and `exists:Rung` at 0; a `finding.made` from `surveil` deposits at least one
claim other than "a finding was made" where any deed happened at the place.

## Falsifier

Remove `sites_here` (examine formations return to 0). Ship `covert_kinds` unchanged (a Success finds
no saboteur). Remove the `surveil` channel (a Success sees nothing). Set `surveil_watch_rate` to 1.0 in
the probe and observe that every Event is seen: the control that the draw, not the band alone, admits.

## NERS reading

- **N.** These are the only inquiries into the physical present and past. Audit §7.9 and §8.9.
- **R.** Concealment gets a counter, and watching gets a risk.
- **S.** The existing trail, mask and witness machinery. One more channel and one more covert kind.
- **E (last).** Three stamps or declines, one roster value, one channel and one kind. Very high.

## Cost class

Edit plus a small build (one witness channel). Declared re-records.
