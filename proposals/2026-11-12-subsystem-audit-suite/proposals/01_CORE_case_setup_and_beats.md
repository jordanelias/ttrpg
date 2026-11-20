# CORE 02 — a case builds its own world and states its beats

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row CORE 02 (CONFORMS), §2 row (A-44, A-50, A-51 via the ARCS file), §7, §7b-T; `unified/U3_DEPENDENCY_ORDER.md` node B39). This file is extended and in two places overruled by `12_ARCS_case_on_the_realm.md` (base `realm` for cast cases; a setup is a delta on the realm, which is now a generated cast with a five-year prologue, A-44, A-50, A-51): `who:` resolves by registry case id (`p_npc_088`), never by name; **`knows:` is struck** (the loader refuses a new Claim construction site, `corpus_run.py:384-387`; what a person knows at the start is prehistory folded through RESOLVE and WITNESS); the beat matcher's `actor_of` read is lawful for a harness observer and is said at the site; `harness/arc.py` exists (verified: `_reach`, `shuffled_causes`); named tests, lands-it and tier.

**Lands in batch:** B39, with and before `12_ARCS_case_on_the_realm.md`. **Depends on:** `21_PROCEDURAL_C_prologue_and_case_seeds.md` (B39).

## Status: PROPOSED

Source: `audits/01_CORE_audit.md` F-CORE-02, F-CORE-04, F-CORE-05; resolutions 2, 3, 4; §13.

## What changes in `engine/season/` at runtime

Nothing in the loop. The harness changes: `harness/corpus_run.py::build_at` reads a typed `setup:` block
from a case's overlay file and builds that case's world; a beat matcher reads a typed `beats:` list and
reports, per case, which beats occurred in a seeded run. The game behaves identically; what can be
*said* about it changes.

## The problem, with evidence

- `build_at` (`harness/corpus_run.py:467-662`) builds one template for all 143 cases: a rung chain from
  `scale`, a Site per yielding kind, persons `p_a…`, seeded pursuits, a ring of `OUGHT`s. Corpus run,
  seed 0, tree `601e715`: `RUNS-UNDECLARED 103 · SPAN-UNAUTHORED 40`; `R2`, `A2`, `A3` `NOT-COMPUTABLE`.
- `python -m engine.season.harness.exercises`: 35 of 292 NPC need-rows bound (32 of 122 core); 0 of
  611 ARC rows.
- 86 cases state their span as prose and run two seasons (`corpus_run.py:73`); 16 name a player and
  are run with the automated chooser only (`corpus_run.py:953`).
- Persons are seated with no `capability` unless an overlay supplies one (`corpus_run.py:537-540`); one
  case does. Result in the same run: 1,552 of 2,152 graded outcomes `Failure`; `told_by` 64 of 93,760
  claims.

## Resolution (decided)

Two typed blocks in the existing overlay file `engine/season/cases/exercises/<CASE>.yaml` (the owner
that already carries `cast:`, `scale:` and `office:`). The case files under `cases/` stay as the
shape-neutral specification (`CASE_BRIEF.md`); the overlay is where a case meets the shape.

```yaml
setup:
  span_seasons: 6            # integer; `ongoing: true` beside it where the source says so
  base: realm                # `realm` (cast cases) or `template` (12_ARCS_case_on_the_realm.md)
  cast:                      # extends the existing `cast:` keys (corpus_run.CAST_KEYS); on `realm`, a delta only
    - who: p_npc_088         # registry case id, never a name match
      capability: {copying: 3}
      pursuits: {stability: 0.9, community: 0.3}     # pursuit_axes keys; refused off-roster
      office: {post: ..., conferral: ...}            # as today
      holds: [rec_einhir]                            # ids declared under `records:`
  prehistory: [{actor: p_npc_088, verb: ..., subject: ...}]   # folded through RESOLVE and WITNESS; no `knows:` key
  records: [{id: rec_einhir, kind: ..., subject_matter: {...}}] # checked by Record.__post_init__
  dates:   [{id: d_assize, venue: <rung>, due_at: 2, holder: <cast who>}]
  player:  {who: <cast who>, policy: echo | first_offered | <named policy>}
beats:
  - id: b1
    kind: record.created            # an Event kind on the derived roster
    actor: p_npc_088                # optional; the seated person by registry case id
    subject: rec_einhir             # optional
    after: null                     # optional beat id that must precede
    caused_by: null                 # optional beat id reachable through causes[]
    terminal: false                 # true = the case's `ends_when`
    needs: [<need_sha>, ...]        # the season_requires rows this beat stands for
  off_arm: {withhold: "cast[0].holds"}   # one setup element whose removal must remove b1
```

### Edits, by owner

1. **`harness/corpus_run.py`**: `CAST_KEYS` gains `pursuits`, `holds` (not `knows`: struck, see the
   `Reconciled:` line); `build_case` dispatches on `base` (`12_ARCS_case_on_the_realm.md`); `build_at` builds
   from `setup:` when present and falls back to the template when absent (so the 135 un-authored cases run
   as today, hash EQUAL). `seasons_for` reads `setup.span_seasons`. Unknown keys are refused at load,
   as `_check_cast` does today.
2. **`harness/arc.py`** (the existing arc harness, 400 lines; verified: `_reach` `:223` walks causes,
   `shuffled_causes` `:213`, `read_arcs` `:335`): `match_beats(w, driver, beats) -> list[BeatResult]`, a pure
   read over `w.log` and `driver.act_of`: kind equality, actor through `state/attribution.py::actor_of`
   (`:73`; a resolver-side read, lawful for a harness observer, said in the docstring), subject through the
   Event's changes, `after` by log order, `caused_by` by `_reach`. No new Event kinds, no writes.
3. **`harness/corpus_run.py::run_case`**: runs the on-arm and, where `off_arm:` is stated, the off-arm;
   status vocabulary gains `BEATS n/m` and loses `RUNS-UNDECLARED` for authored cases. `R2` stops being
   `NOT-COMPUTABLE` for them.
4. **Player proxy**: when `setup.player` is present the runner passes
   `play_surface.dispatching_chooser(auto, {pid: policy})`. A policy picks among the candidates the
   engine offers (through `decision/sheet.py`'s development space); it names no outcome. `echo` is
   the control and must leave the hash equal to the automated run.
5. **Data**: author `setup:`/`beats:` for NPC-088 first, then the seven other cases with overlay rows
   (NPC-002, -005, -010, -012, -075, -086, -087); other lanes author theirs from their §13 tables.
   Integer spans for the 86 prose rows are a data edit in the overlay, with `ongoing: true`.

## Gate (execution artifact)

Per authored case, seeds 0, 1, 2: every non-optional beat matched in the on-arm; the off-arm's
withheld beat absent; two cases at the same scale hash differently at tick 0. Printed by `corpus_run`.
Named tests (new, `engine/season/tests/test_case_setup_and_beats.py`): `test_an_unauthored_case_hashes_as_before`;
`test_beats_match_on_arm_and_not_off_arm`; `test_echo_policy_leaves_the_hash_equal`;
`test_a_knows_key_is_refused_at_load`; `test_who_resolves_by_registry_id_only`.

## Falsifier

Scripting drift is the failure to watch for. The check: the beat matcher is given no ability to write
and the policy no ability to name an Act the engine did not form (`development_space` refuses an index
outside the offered set, per its docstring). If a case's beats match in the off-arm too, the beat is
not evidence of the setup and the case is reported `BEATS-UNCONTROLLED`, not passed. A second
falsifier: shuffle the cast's pursuits between persons; a beat keyed to an actor should fail to match
more often than not, or the beat was never about that person.

## NERS reading

This is an instrument, not a design object in play, so N, R and S are read on what it lets be judged.

- **N.** Without it no arc can be shown simulated; the standing corpus is otherwise unread by any run.
- **R.** It tests the half of R with no player in it (beats from persons' own acts) and, with the
  proxy, the half with one.
- **S.** One overlay file per case, the file that already exists; one builder; the beat grammar uses
  only fields Events already carry (kind, causes, changes), so it adds no second vocabulary.
- **E (last).** Two blocks and one matcher against 903 unread need-rows.

## Cost class

Small build in the harness, then data authoring per case (each lane's). No hash moves for un-authored
cases. No guard: nothing here runs in CI unless a later decision puts `corpus_run` there.

**Lands it and tier.** The B39 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B39's
`methodology-close` once; case data by each lane.
