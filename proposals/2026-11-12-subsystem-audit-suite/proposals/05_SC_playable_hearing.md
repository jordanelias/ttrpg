# SC-P3 — the hearing as a played scene: one fixture, one callback, the season's own code path

## Status: PROPOSED

Source: `audits/05_SC_audit.md` F-SC-01, F-SC-05, F-SC-07 and §9; the standing requirement (each
subsystem playable alone, conformant, integrated). Composes on plan items already written
(CP-T05-01, CP-T05-02 (i), CR-62, CR-63) and schedules none of them anew.

## What it changes in `engine/season/` at runtime

Shipped realm runs: nothing until its two loop edits land (items 2 and 3 below), each a declared
mover. It adds one fixture builder and one harness entry point, and it makes the choice a `speak`
carries (which proofs, which plea) an operand the roll reads. The social contest stays ONE module
entry (`social_contest.roll`, typed input, `Margin` out, no state).

## The problem (evidence)

- **No decision inside a social contest.** `seam/wrappers/sigma.py::resolve` accepts `host` and does
  not use it (`:459-460`); personal combat is the only provider with a PLAYABLE mode
  (`queries/inputs.py::PlayHost`, `modules/combat/wrapper.py::TURN_CHOICES`). A `speak` is one act,
  one draw, and it spends its whole proof inventory (`world_q.proofs`' named limit: *"one `speak` is
  one act, so it spends its whole inventory"*).
- **The only played social contest is the kernel's** (`systems/social_contest/sim/contest/
  agon_harness.py`), which the loop does not run and SC-P2 retires. A standalone game on code the
  season never executes is the two-code-paths failure the standing requirement names.
- **A hearing does not end.** `python -m engine.season.harness.aperture 2 0` (PYTHONHASHSEED=0):
  `determine` attempted 2, executed 0; `matter.determined` is in the never-emitted list; `speak`
  attempted 25, refused 23 as `speech.unheard`, executed 2, both `Failure`. A three-season
  `build_realm(0)` probe: 7 cases opened, 3 `determine.refused`, 0 determined, the docket 8 → 14 → 18.
- **A speech does not reach the verdict.** `matter.carried`, `matter.advanced`, `matter.held` and
  `matter.turned` have no reader under `engine/season/` outside harness comments (grep at `601e715`);
  all four bands of `speak` write `[]`.

## The resolution, decided

**The standalone social contest is the season loop on a one-matter fixture, with a player callback
on `harness/play_surface.py::dispatching_chooser`.** No nested bout engine, no second resolver, no
suspension inside a provider: the season already ticks scene by scene (R-03), a scene already holds
up to `interactions_per_scene` acts, and each `speak` is already one exchange. What a hearing lacks
is a choice per exchange, a consequence per exchange, and an end. Each is an edit to an existing
owner.

Ladder: step 3 (R-03's built scene clock and A-25's module contract answer "where does the loop
live"); step 4 (precedent: the personal-combat PLAYABLE mode needed suspension because a duel's turns
are not season acts; a hearing's turns are — `speak`, `tell`, `give`, `determine` are rows).

## Exact edits, by owner

1. **Fixture (new function, existing file):** `engine/season/harness/governance_spine.py::
   build_hearing(seed)` — the spine realm plus: one convened sitting at a settlement (`convene`'s
   Date, fired), one person docketed under a NAMED arrangement row (`legal_trial`), a bench of three
   seated judges, an accuser holding two attributed deeds of the accused, the accused holding one of
   the accuser. Every element is built by the same builders `build()` uses; nothing is hand-planted on
   `w.docket` except through `_eff_open_case`'s own payload keys.
2. **The choice (`speak`'s operands; CR-62 and CR-63's rows carry the build):**
   `engine/season/verb_table.yaml` `speak` gains two optional operands read off the payload:
   `proofs: [claim id, …]` (the subset the speaker spends; absent = all, today's behaviour, the
   control) and `plea: <speech_kinds id>` (absent = none). `seam/wrappers/sigma.py::contest_input`
   passes the chosen subset to `world_q.proofs` (a `held=` filter over the actor's own ledger — own
   ledger, F8-clean). The plea enters as CR-62 decides it: THROUGH THE OBSTACLE (a `plea_step`
   operand on `queries/inputs.py::SocialContestInput`, composed in `modules/social_contest/roll.py::
   obstacle`, the single obstacle owner), never as a band rewritten outside `degree_from_net` (CR-62's
   critic: a grade cap beside the ladder is two methods for one quantity). `arrangements.yaml:
   speech_kinds` then supplies the closed set of plea ids and nothing else: its `reachable_bands`
   key is deleted in CR-62's commit unless CR-62's dominance test adopts the cap, and the roster is
   deleted whole if CR-62 lands without reading it (audit §6, G-06).
   **The chooser forms the variants, as it forms `effort` (one interface for player and NPC).**
   `decision/choose.py::settle_efforts` already turns a contested candidate into ordinary
   Candidates that differ in one operand. The proofs subset and the plea are offered the same way
   (owner: CHAR's file; SC's requirement is only that the variants are Candidates, so an NPC's
   temperament picks among them by the same score a player's callback sees). A choice only a player
   can make would be a second code path.
3. **The consequence — speech is entered on the case file.** The plan's carrier is CP-T05-02 (i):
   `queries/world_q.py::hearing(w, matter, venue)`, read from what the bench holds, re-specified on
   SC-02's commit route so it does not breach F8. DECIDED here as the better carrier (ladder step 5),
   and offered to that position rather than beside it: a `speak` that grades `Success` or better
   appends one stage to the matter's case file (`Record.stages`: `(tick, <band's kind>, act id)`),
   and `hearing` is a count over that Record's stages, signed by whose act it was. Three things
   follow from the one write. (i) F8 is not in question: a Record is a World store, and the case file
   is the proceeding's own record, not a judge's memory. (ii) `speak` now WRITES in two bands, so
   `decision/choose.py::_writing_bands` holds for it and the chooser prices its believed chance and
   offers `effort` on it with no edit to decision code — today both skip `speak` because it writes
   nothing (`choose.py:154-162`; `corpus_run`: *"BANDS THAT DIFFER … speak False"*). (iii) The
   hearing's record can be forged, burned or seized like any Record (CR-61's premise), which is a
   story. Needs CR-61 (the docket item names its case file). CP-T05-02 (i)'s arithmetic (Failure and
   Partial count 0; `DEGREE_STEP`) is kept unchanged; only its source moves.
4. **The player seam (new function, existing file):** `engine/season/harness/headless.py` gains
   `--play <person id>` and `--world hearing`: it builds item 1's world, wraps the shipped chooser in
   `dispatching_chooser(auto, {pid: callback})`, and the callback prints the person's `View` (his
   own claims about the other party, the docketed matter, his candidates with `View.odds`'s believed
   chance where he can say) and reads a choice from stdin; EOF or `--auto` returns `auto`'s pick. It
   prints, per round, the Events his person witnessed with SC-P1's `ending` for his OWN acts only.
5. **The end:** the run stops at `matter.determined` (stakes: the disposal Tenure's kind and
   `degree`, printed with what it binds), at `matter.lapsed` (CR-55's lapse), or at `--seasons`.

No file under `modules/social_contest/` gains state; `roll.py` reads two more fields of the frozen
record.

## The five things a player needs, and where each comes from

| need | source after this proposal |
|---|---|
| scenario seed | `governance_spine.build_hearing(seed)` |
| choice surface | `speak` {subject, proofs subset, plea, effort}; `tell`/`lie`/`give` to the bench; `evade / defy`; for a judge, `determine` or wait |
| outcome legibility | SC-P1's `Event.ending` on his own acts; the band's kind for others' |
| stakes | the arrangement row's `disposes:` kind and the edge's `degree`; `hearing_step` on the verdict |
| end condition | `matter.determined`, `matter.lapsed`, or the season bound |

## Gate (execution artifact)

`PYTHONHASHSEED=0 python -m engine.season.harness.headless --world hearing --seed 0 --seasons 4
--auto` twice: identical content hash, and the log holds a `matter.determined` whose `causes` reach
the sitting's `date.fired`. Then the same with `--play` and a scripted stdin choosing a different
proofs subset at the first `speak`: the hash differs and the determining draw's `ending` shows a
different obstacle. A control arm with `proofs` absent reproduces the `--auto` hash.

## Falsifier

If the scripted player's different proofs subset leaves the verdict's obstacle unchanged, the choice
is not load-bearing (the mirror is still total, H-216, or `hearing_step` is not read) and the scene
does not play: the gate is red, and the residue is named at H-216, not patched here. If `--auto` on
the fixture never reaches `matter.determined` in 4 seasons at seeds 0–2, F-SC-01's cause is in
formation and not in the fixture (cross-lane: CORE's chooser).

## NERS reading

- **N**: top-down a hearing is the game's most distinctive scene; bottom-up every act it needs is a
  row; lateral it matches how the season already plays a scene; diagonal (person to realm) the
  disposal Tenure is read by governance. Cut it and SC has no played form after SC-P2.
- **R**: strategy (which proof to hold back, when to concede), variety (plea kinds), impact (a
  graded disposal), and the no-player half is unchanged: the same acts form for NPCs.
- **S**: no second clock, no nested resolver; the hearing pauses the realm exactly as any scene does
  (it is a scene). One roll owner, one obstacle owner.
- **E**: two operands, one record field, one fixture and one flag, against a playable subsystem.

## Cost class

Small build (items 1, 4, 5) on top of two plan builds (items 2, 3) that are already scheduled.
