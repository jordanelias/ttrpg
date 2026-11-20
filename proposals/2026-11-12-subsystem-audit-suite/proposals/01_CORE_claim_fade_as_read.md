# CORE 01 — the fading of memory as a read, not a logged write

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — Option A is confirmed by the decision register (D-48, taken A by the ladder; reversible on Jordan's word). `16_PESSIMIST_CORE_a_refusal_is_remembered.md` and `U5a_DICE_owed_edits.md` §4 read present confidence through this file's one function.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row CORE 01 (AMBIGUOUS), §7, §7b-2, §7b-T; `unified/U3_DEPENDENCY_ORDER.md` node B09, §6.2). Layer 1 rewrite (`04` §B.13 invariant 7: the log accepts only a kind an emission column declares; `04` §A.2: MATTER's may-read column does not list ledgers): the `claim.forgotten` Event is **deleted** (ladder step 5: no requirement cites a fade, this file's own N paragraph), so MATTER stops walking ledgers and emits nothing for memory; a reader that wants the moment a claim fell to zero calls `present_confidence` at two ticks. The reader list's `[UNVERIFIED]` is settled by a grep at this tree (sites listed in edit 2); the scratch probe becomes named tests; lands-it and tier added.

**Lands in batch:** B09. **Depends on:** `01_CORE_tests_one_golden_owner.md` (B02; one pin file for the re-pin); `U5a_DICE_owed_edits.md` §4 and `16_PESSIMIST_CORE_a_refusal_is_remembered.md` read through this file's function (same batch, after it).

## Status: PROPOSED

Source: `audits/01_CORE_audit.md` F-CORE-01, resolution 1, §11. Not ratified by being written.

## What changes in `engine/season/` at runtime

MATTER stops writing `Claim.confidence` once per live claim per season and stops emitting
`claim.decayed`. A claim's present confidence is computed where it is read. The Event log holds no Event
for fading. `World.content_hash()` moves (a declared
mover): fewer Events, and `Claim.confidence` holds the deposited value.

## The problem, with evidence

`loop/matter.py:471-501` walks every person's ledger and, for each claim with confidence above zero,
calls `World.write(... record_kind="Claim", fieldname="confidence", emits="claim.decayed")`.

Run: headless world (three persons), seed 0, eight seasons, tree `601e715`, `PYTHONHASHSEED=0`
(`probe_growth.py`, audit §12).

| season | acts | new log entries | of which `claim.decayed` |
|---|---|---|---|
| 0 | 16 | 86 | 0 |
| 3 | 26 | 481 | 276 |
| 7 | 22 | 1,164 | 938 |

After eight seasons: 182 acts, 4,621 Events. `content_hash()` walks the whole log each season
(`state/world.py:1709-1725`) and took 0.63 s of a 2.65 s profiled season. `harness/corpus_run.py:72`
clamps every case at six seasons and names the flood as the reason; five corpus cases ask for 8 to 16.

## Resolution (decided)

Fading is a function of a claim's deposited confidence and its age.

## Edits, by owner

1. **`engine/season/state/ledgers.py`** (the owner of the eviction comparator; the confidence reader
   joins it). New function, the single owner of the rule:

   ```python
   def present_confidence(confidence: int, when: int, tick: int, decay: int) -> int:
       """A claim's confidence at `tick`: what was deposited, less `decay` per season elapsed."""
       return max(0, confidence - decay * max(0, tick - when))
   ```

   `[ASSUMPTION; medium]` This reproduces today's schedule exactly for a claim that has a deposit
   Event and has faded once per season since. Today a claim with no deposit Event is skipped
   (`matter.py:482-485`) and so never fades; under this edit it fades. That difference is intended and
   is the one behavioural change beyond the log.
2. **Every reader of `Claim.confidence`** routes through it (§0.1 pt 1: grep the field's readers and
   its assignments). Known sites: `state/ledgers.py::eviction_key`'s caller, `queries/person_q.py`
   (`LedgerReader._best`, `:1057`), `loop/deliberate.py:547` (the inputs fingerprint),
   `seam/wrappers/sigma.py:290`. The reader needs `tick` and the fixture `claim_decay`; `LedgerReader`
   is constructed with both. Settled by `grep -rn "\.confidence\b" --include=*.py engine/season` (non-test,
   non-harness) at this tree, the code reads besides: `queries/person_q.py:1072`, `:1078`, `:1201`, `:1273`;
   `queries/world_q.py:848` (`reception`); `loop/witness.py:260`, `:988`; `decision/options.py:1706`;
   `decision/questions.py:107`; `state/ledgers.py` (two sites). The `decision/` readers read through the
   ledger reader the person is handed (constructed with `tick` and `claim_decay`), never `World`; the
   executing session re-runs the grep before the edit and routes every site found.
3. **`engine/season/loop/matter.py:471-501`**: the per-claim write is deleted and nothing replaces it:
   MATTER stops walking ledgers (its may-read column does not list them, `04` §A.2). No Event marks a
   claim reaching zero: "it reached zero" is a function of `present_confidence`, and a reader that wants
   the moment calls it at two ticks. If an Event is later wanted, it is added as a `(Claim, exists)`-style
   matrix row written at WITNESS/CENSUS when eviction removes the claim, so invariant 7 derives the kind;
   it is not built here.
4. **`engine/season/write_matrix.yaml`**, row `(Claim, confidence)`: remove `MAT` from `steps:` and
   `claim.decayed` from `emits:`. No new kind.
5. **`engine/season/requirements.yaml`**, **`harness/corpus_run.py:72`**: raise `MAX_SEASONS` to the
   corpus maximum (16) once the gate below reads flat.

## Gate (execution artifact)

`probe_growth.py` (a scratch script, not in the repository) is restated as new tests in
`engine/season/tests/test_claim_fade_as_read.py`: `test_present_confidence_matches_the_schedule_of_the_old_write`
(a hand-built ledger, ticks 0 to 7, `==` against the old write's values for a claim with a deposit Event);
`test_no_claim_decayed_in_an_eight_season_log` (headless, seeds 0, 1, 2, eight seasons); and
`test_log_growth_per_season_is_flat` (new log entries per season within ±20 % of season 1's from season 1
onward). Two runs at one seed give one hash. The seeded goldens re-pin, said plainly in the commit.

## Falsifier

A person's choices change. Control: run the present tree and the edited tree at seed 0 for four seasons
with `claim_decay` swept to 0 (no fading in either); the act multiset must be identical. With fading on,
the act multisets must also be identical for every claim that had a deposit Event; a difference is the
proposal read wrong, except where assumption 1 names it.

## NERS reading

- **N.** The fade is needed (R-07: memory that weakens). The Event per fade is removable without
  worsening play from each direction tried: top-down, no requirement cites a fade; bottom-up, no
  verb's `requires` reads `claim.decayed`; lateral, the sibling clocks (wear, yield) emit one Event per
  Site, not per datum.
- **R.** Completeness improves: the mechanism stops breaking at its extreme (long campaigns).
  The no-player half is unchanged; forgetting entirely still leaves a record.
- **S.** "Calculations consistent in methodology": a band crossing emits and a level does not is
  already the rule for Sites and bodies; this applies it to memory.
- **E (last, against the above).** One function replaces a write, a matrix step and an Event kind, and adds
  none.

## Cost class

Small build; hash mover; Layer-1-descended row touched — listed in the audit's §11 with the
alternative (one aggregated `ledger.faded` Event per person per season), not taken.

**Lands it and tier.** The B09 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B09's
`methodology-close` with its terminal `opus` critique once. **Hash movers.** Every world (fewer Events;
`Claim.confidence` holds the deposited value), re-pinned once in `_realm_goldens.py`, said plainly.
