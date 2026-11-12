# Implementation brief A — computed play reaches combat; no dead ends; the opposed obstacle is never a flat 2

## Status: WORK ORDER (Jordan's direction of 2026-11-12; not canon; resolves nothing until built and verified)

Jordan, verbatim: *"yeah implement the approach for PC. computed play must reach. we never want dead ends.
social contest ob always 2 is so wrong."* This brief is the first of two implementation lanes. Lane B
(the per-phase approach, the duel-round entry and the loadout cost) follows on top of this lane's merged
result, because both re-pin the same goldens.

## The three charges, as testable statements

1. **Computed play reaches personal combat.** In the shipped realm (`build_realm`), a played-out season
   forms, issues, accepts and fights duels (and captures) through the real chooser with no hand-built act.
   Baseline (`audits/03_PC_audit.md` F-PC-01, `aperture 2 s`, `PYTHONHASHSEED=0`): seed 0 `challenge`
   84/84 refused, `accept` 27/27 refused, zero combat calls; seed 1 two captures.
2. **No dead ends.** A mechanism that can be offered must be able to complete. An act the fold must
   refuse for a reason the chooser could have read is a dead end: it is not offered (formation reads the
   same facts the fold does, person-side only, AX-2). A roster, row or chain whose first link nothing can
   fire is a dead end: find the first broken link and repair it at its owner. 76% of resolved acts were
   refusals at baseline (`audits/02_CHAR_audit.md` F-CHAR-05).
3. **The social-contest obstacle is never a flat 2.** An opposed contest against a person is opposed by
   that person's own score (`audits/05_SC_audit.md` F-SC-03; `audits/10_DICE_audit.md` F-DICE-01/03:
   564 of 568 realm rolls are the same pool-2 roll; 83 of 83 persons hold no attribute at build, so the
   opposition falls to `obstacle_default` 2.0, which is worth a score of 4).

## Sources to read first (in this order)

`CLAUDE.md` (all of it binds you); `proposals/2026-11-12-subsystem-audit-suite/proposals/`:
`03_PC_duel_chain_reach.md` (formation: `challenge` classed `Person`, dispute declined person-side,
`accept` on a challenge Record), `10_DICE_one_score_two_roles.md` (a person opposes with the score he
rolls; the stand-in serves non-persons only), `05_SC_opposed_obstacle_parity.md` (HELD BACK, Option A/B on
`score/2`: **you do not change the ruled `score/2`**; see below), `03_PC_person_inputs_content.md`
(persons carry the content combat reads), `02_CHAR_offer_what_can_be_done.md`,
`02_CHAR_capability_uses_table.md`; and the audits' §3 for PC, SC, DICE, CHAR, CORE (F-PC-01/02,
F-SC-03, F-DICE-01..03, F-CHAR-05, F-CORE-20).

## What the ruling allows

The ruled form (Jordan, 2026-08-14, `dice_engine.degree_from_net` docstring): an opposed obstacle is
*"their corresponding score/2 plus whatever specific modifiers exist for them in that instance"*. Keep
it. The defect Jordan names is that the realm never reaches that form: persons hold no score, so the
flat `obstacle_default` 2.0 applies. The repair is therefore (a) a person's opposing score is the score he
rolls (`10_DICE_one_score_two_roles.md`), and (b) persons in the shipped realm hold scores
(attributes seated: `build_realm(cast_attributes=...)` ships OFF today by design as a control; flip the
shipped default, and give unauthored persons a data-driven default bundle, not a module constant). If
you find the ruled `score/2` itself is what Jordan calls wrong, do NOT change it: stop and say so in
your receipt; `05_SC_opposed_obstacle_parity.md` carries the two options for him.

## Ordered steps (one commit each; message `[simulation] ...`, subject <= 72 chars; no PP/ED cited unless real)

1. **Reach: formation.** `03_PC_duel_chain_reach.md`'s three edits (verb_table `challenge` Person class;
   `violence_contexts` dispute; `opening_set` Record-kind rule), plus the same repair wherever the same
   dead-end shape appears in the verbs a duel needs (`comply`, `capture`, `interrogate`, `fight`): list
   them from the refusal counts of `aperture 2 s`, fix the ones whose first link cannot fire.
2. **Reach: the duel actually fires.** After step 1, measure again. If the realm still forms no
   duel, find the next broken link (a dispute that no one holds because deeds are not judged; a
   `fight` that forms only on a held party; terms that nobody can name) and repair it at its owner, one
   link per commit, until a seeded realm produces `challenge.issued` -> `accept` -> a fought scene ->
   a typed outcome that other subsystems read (`duel.yielded`, a wound, a capture, a death naming a seat).
   Do not hand-build an act to pass; do not special-case a person (scripting drift).
3. **Persons hold scores.** Seat attributes in the shipped realm and give unauthored persons a
   data-driven default (owner: the existing registry the DICE capability map names, `rosters.yaml`
   `verb_capability` / `vocation_attribute`; do not invent a second system). Declare it a mover of the
   shipped realm.
4. **One score, two roles.** `seam/wrappers/sigma.py::_opposition_of` and `modules/social_contest/roll.py::obstacle`
   per `10_DICE_one_score_two_roles.md`: a person's opposition is the score he rolls; `obstacle_default`
   applies to a non-person subject only; add the four rolled verbs the proposal names to
   `verb_capability`. The control arm must reproduce today's bytes.
5. **Declared movers, honestly.** Every pin that moves is re-recorded in the same commit that moves it,
   and the commit body says plainly that it is a re-record and why (CLAUDE.md §7: nothing verifies a
   re-pin was intended). Use `python tools/tests_for_diff.py` to find the suites; run each touched file
   once (CLAUDE.md §0.4). Do NOT run the full suite: the orchestrator runs it once at the close.

## Gates (execution artifacts, quoted in the final receipt and the commit bodies)

- `aperture 2 s` for s = 0, 1, 2 before and after: `challenge`/`accept` refusals by last-read reason,
  `fight` formed, deaths and captures. The refusal reasons `exists:Person`, `dispute=False` and
  `exists:challenge` must be 0 at formation.
- A seeded planted-dispute run (the falsifier in `03_PC_duel_chain_reach.md`): the chain fires through the
  real chooser, and the same run with the edits reverted does not.
- Realm rolls: the distribution of (pool, obstacle) over a four-season, three-seed run: more than one
  distinct obstacle, and obstacle correlates with the opponent's held score (a table, with the control).
- Determinism: same seed, same hash, twice; `PYTHONHASHSEED=0`.

## Limits

Work in your isolated worktree on its own branch; commit there (the orchestrator merges). Edit no
file under `proposals/2026-11-12-subsystem-audit-suite/` (other lanes are writing there). No new guard,
no new standing document, no new tree (CLAUDE.md §0.1 pt 5). `.designs/` and `.audit/` may be read, never
cited as the reason a behaviour is correct, never read by code. Layer 1 binds how code is written
(`architecture/meta/04_CODE_ARCHITECTURE.md`; check with the `layer-conformance` skill's Lens B before
you finish). Canadian English in prose. If a step turns out to need a ruling Jordan has not given, stop
that step, finish the others, and say what is blocked.

## Receipt (<= 250 words)

Branch and commit list; the before/after gate numbers; every re-recorded pin and why; what you could
not do and what is blocked; anything the orchestrator must decide.
