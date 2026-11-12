# CORE 01 — the fading of memory as a read, not a logged write

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — Option A is confirmed by the decision register (D-48, taken A by the ladder; reversible on Jordan's word). `16_PESSIMIST_CORE_a_refusal_is_remembered.md` and `U5a_DICE_owed_edits.md` §4 read present confidence through this file's one function.

## Status: PROPOSED

Source: `audits/01_CORE_audit.md` F-CORE-01, resolution 1, §11. Not ratified by being written.

## What changes in `engine/season/` at runtime

MATTER stops writing `Claim.confidence` once per live claim per season and stops emitting
`claim.decayed`. A claim's present confidence is computed where it is read. The Event log holds one
Event when a claim's confidence reaches zero, and none before. `World.content_hash()` moves (a declared
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
   is constructed with both. `[UNVERIFIED: the full reader list; `loop/witness.py` and
   `decision/options.py` were not opened.]`
3. **`engine/season/loop/matter.py:471-501`**: replace the per-claim write with one pass that finds
   claims whose `present_confidence` reached zero *this* tick and emits one `claim.forgotten` Event per
   such claim, `causes=[the deposit Event]`, no state write (the pattern `_crossings` already uses,
   `matter.py:126-129`: a crossing emits, a level does not).
4. **`engine/season/write_matrix.yaml`**, row `(Claim, confidence)`: remove `MAT` from `steps:` and
   `claim.decayed` from `emits:`; add `claim.forgotten` to the crossing kinds' owner
   (`rosters.yaml: fold_kinds` or the row MATTER's crossings already declare `[UNVERIFIED which]`).
5. **`engine/season/requirements.yaml`**, **`harness/corpus_run.py:72`**: raise `MAX_SEASONS` to the
   corpus maximum (16) once the gate below reads flat.

## Gate (execution artifact)

`probe_growth.py 8` at seeds 0, 1, 2: new log entries per season within ±20 % of season 1's from
season 1 onward; no `claim.decayed` in the log; two runs at one seed give one hash. The seeded goldens
re-pin, said plainly in the commit.

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
- **E (last, against the above).** One function replaces a write, a matrix step and an Event kind.

## Cost class

Small build; hash mover; Layer-1-descended row touched — listed in the audit's §11 with the
alternative (one aggregated `ledger.faded` Event per person per season).
