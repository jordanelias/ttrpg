# ARCS 01 — a case is a delta on the realm, with beats and three controls

Reconciled: 2026-11-12, U5d closure — folded **A-44**, **A-50** and **A-51**. A case is a delta on the realm; the realm is now a generated cast of about 94 persons plus kin under a cap (A-44) with some bounded starting state drawn (A-50), and it has run a five-year prologue before play (A-51; the year's length is read from the code: `queries/world_q.py::season_of_year` takes it as `len(season_factor_draw)`, which ships `()`, so no year is declared at the shipped fixtures and the swept arms declare four seasons; five years is five times the declared length, twenty seasons under a four-entry table, and the prologue needs a declared year, `21_PROCEDURAL_C_prologue_and_case_seeds.md` as reconciled). So: the delta is applied to the world **after** generation and before the prologue where it states a standing fact, and after the prologue where it states the opening situation; knowledge seeded "as prehistory through the fold" is seeded inside those five years, not as a single pre-tick pass. The three controls stand; each is read on a fixed generation seed so a beat's absence in the off-arm is not a difference of cast.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row ARCS-01 (CONFORMS), §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-10; `unified/U3_CONFLICT_LEDGER.md` C3-K11, C3-L13; `unified/U3_DEPENDENCY_ORDER.md` node B39, §4.1 rows 84, 86, 87). Changed: the year the five-year prologue is measured on is the one owner `rosters.yaml: seasons_of_year` (four seasons, ED-IN-0332; landed by `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 at the head of B12), not `len(season_factor_draw)` as the U5d line above reads it (D-U1-10, C3-K11); the beat matcher's use of `state/attribution.py::actor_of` (a resolver-side read) is stated as lawful for a harness observer; `harness/arc.py` is verified to exist with `_reach` (`:223`) and `shuffled_causes` (`:213`); the three items other lanes split into this batch are named; tests named; lands-it and tier. `01_CORE_case_setup_and_beats.md` now carries a `Reconciled:` line pointing here (the contradiction on `knows:` and `who:` is closed there).

**Lands in batch:** B39. **Depends on:** `21_PROCEDURAL_C_prologue_and_case_seeds.md` (B39, the prologue and its year), `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 (B12), `01_CORE_case_setup_and_beats.md` (B39, same batch, this file's base). **Takes into this batch:** `15_INSTITUTIONS_SYNTHESIS_B` prehistory, `15_INSTITUTIONS_COLONIAL_D` founders-as-prehistory, `17_CENSUS_C1B_02_wires` W-2 (U3 §4.1 rows 84, 86, 87).

## Status: PROPOSED

Source: `audits/12_ARCS_adjudication.md` §2.2, §5, §6 rows 9 and 16. Extends
`proposals/01_CORE_case_setup_and_beats.md`; where the two differ, this file says so.

## What changes in `engine/season/` at runtime

Nothing in the loop. Two harness modules change (`harness/corpus_run.py`, `harness/arc.py`) and the
overlay files under `cases/exercises/` gain two typed blocks. The game behaves identically.

## The problem, with evidence

- `corpus_run.build_at` (`:467-662`) builds a three-seat template for every case and reads no need
  (audit §2.2). The CORE proposal fixes this by extending the template's `cast:`.
- The provided characters are already built elsewhere: `populated.build_realm(0)` seats all 46 by name
  with offices, fifteen pursuit weights, commitments, seeded ledgers and authored Thread sensitivity
  (probe: 83 persons, 34 offices, hash `600d8b271474…`). Re-authoring them per case in the overlay would
  create a second copy of the cast, free to disagree with `references/npc_registry.yaml` and `npcs.yaml`.
- CORE's `knows:` key is refused by the loader today as a new Claim construction site
  (`corpus_run.py:384-387`).

## Resolution (decided)

1. **Base.** A case names its base: `base: realm` (the default for every case whose people are cast
   members: all 46 NPC cases and the arcs that name them) or `base: template` (the SCN rule chains and
   anything with anonymous actors). One builder per base; no third.
2. **Setup is a delta, not a cast.** `setup:` lists only what the case needs that the base lacks:
   `who:` entries resolve to the realm's person by registry case id (`p_npc_088`), never by name match;
   `records:`, `dates:`, `offices:` as in CORE 02; `span_seasons` an integer.
3. **What a person knows at the start is prehistory.** `setup.prehistory:` is an ordered list of acts
   (`{actor, verb, subject}`) folded through the real RESOLVE and WITNESS before tick 0 with the case's
   seed; the claims that result are deposited by the engine. No `knows:` key. A prehistory act the fold
   refuses fails the build, naming the refusal.
4. **Beats** as CORE 02, plus three forms the cases need: `absent: true` (the beat must not occur: a
   secret kept, a hold maintained); `any_of: [...]` (one of several person-chosen branches); `window:
   {from, to}` in seasons. A beat may match on the answered question's source where the reason trail
   exposes it.
5. **Three controls, all required for a pass.** (a) off-arm: one setup element withheld, the beat
   absent; (b) cast shuffle: creeds permuted between seated persons, an actor-keyed beat fails in the
   majority of permutations; (c) null: the matcher run over `arc.shuffled_causes(log, seed)` finds no
   `caused_by` beat.

## Edits, by owner

- `harness/corpus_run.py`: `build_case(case, seed)` dispatches on `base`; `build_at` stays the template
  builder unchanged (hash EQUAL for unauthored cases); the realm arm calls `build_realm(seed)` then applies
  the delta with the constructors `build_at` already uses (`_seat_office`, `add_tenure`), validated at
  load as `_check_cast` validates a cast today.
- `harness/arc.py` (exists, 400 lines; `_reach` `:223`, `shuffled_causes` `:213`): `match_beats(w, d, beats)
  -> list` (pure read; reuses `_reach` for `caused_by`). It reads `state/attribution.py::actor_of` (`:73`), a
  resolver-side read; that is lawful because a harness is an observer outside the simulation, not a
  person-side reader (`04` §B.9: no person-side Query reaches the act store), and is said in its docstring.
- `cases/exercises/NPC-088.yaml` first; then by §5's stages.

## Gate (execution artifact)

NPC-088 on the realm, seeds 0, 1, 2: `record.created` by `p_npc_088` and `term.matured` matched; the
off-arm (her copying capability and workshop Record withheld) matches neither; the null matches no causal
beat; unauthored cases hash as before. Named tests (new, `engine/season/tests/test_case_on_the_realm.py`):
`test_npc088_beats_match_on_the_realm`, `test_npc088_off_arm_matches_neither`,
`test_the_null_matches_no_caused_by_beat`, `test_unauthored_cases_hash_as_before`,
`test_a_setup_key_outside_the_closed_set_is_refused`, `test_a_prehistory_act_that_writes_a_terminal_beat_is_refused`.
**INCOMPLETE, not decidable here:** the per-case `prehistory` lists and `beats` are content each lane authors
from its §13 table.

## Falsifier

A setup that contains an outcome. The loader refuses any `setup` key outside the closed set and any
prehistory act whose verb's row writes the field a beat names as its terminal: a case may not pre-write
its own ending. If a beat matches in the off-arm the case reads `BEATS-UNCONTROLLED`.

## NERS reading

An instrument; read on what it lets be judged. **N**: the cast is single-owned; a case can no longer
drift from the registry. **R**: it tests the half of R with no player in it on the world the game
actually builds. **S**: prehistory uses the engine's own fold, so a case's opening state is reachable by
play by construction. **E (last)**: one key (`base`) and one list (`prehistory`) more than CORE 02,
against a second cast avoided.

## Cost class

Small build, then data per case. Realm cases cost about two seconds to build and are slower per season
than the template; the corpus run's wall time rises with each authored case.

**Lands it and tier.** The B39 batch, a WR/IN `valoria-author` session on `sonnet` (`high`) for the builder
and matcher; case content per lane; closed by B39's `methodology-close` once. **Hash movers.** None for
unauthored cases (control).
