# 16 · PESSIMIST · CORE — the record holds what changed: receipts carry the value the gate saw, and interior writes reach the log

## Status: PROPOSED

Carries F-PES-CORE-02 and F-PES-CORE-03 of `audits/16_PESSIMIST_CORE.md` (§1.4, §1.6). Reference only
(CLAUDE.md §0.05). Two edits at one owner (`state/world.py::World.write`) and two call sites.

## What it changes in `engine/season/` at runtime (first)

1. A `Receipt` minted for a `Change` whose subject names `fields` carries, in `delta`, the before and
   after encodings the gate already read to decide the write was not a no-op. Today `delta` is `None` on
   every receipt.
2. The scar write and the conviction-crisis write emit the Event kinds `write_matrix.yaml` already
   declares on their rows (`scar.taken`, `conviction.moved`), through the gate, once per causing act,
   carrying the receipts of the persons written. The Events go to the log by the gate's own append and
   are **not** in the list RESOLVE returns, so they join no WITNESS fan-out and deposit no claim.

Every content hash moves once (`content_hash` folds `delta`, and the log gains Events). No act is
chosen, admitted, resolved or witnessed differently.

## The problem (evidence; `build_realm(0)`, two seasons, hash `bacd687f…`)

- **36,586 of 36,586 receipts in the log carry `delta=None`.** The only two `gate.mint` calls
  (`state/world.py:1442`, `:1494`) pass none. `Receipt.delta`, `.spec` and `.mode` (always `"set"`) are
  declared fields with a constant in them; `content_hash` folds the constant (`world.py:1716`); nothing
  else reads a receipt's `delta` (the one `.delta` reader, `loop/effects_economy.py:89`, reads the Act's
  own declared changes). The log therefore says `stores.changed` at a granary and not whether it rose or
  fell, `body.changed` and not which way, `pursuit.moved` and not toward what.
- The gate holds the value at the moment it mints: `was = [… self.state_of(s) for s in
  change.subjects]` before `change.apply()` (`world.py:1399`), and `self.state_of(s) != b` after
  (`:1427`). For a subject naming `fields`, `state_of` is *"those attributes' canonical encodings: a
  snapshot"* (`world.py:745-747`). It compares the two and discards both.
- **3,914 of the 40,494 receipts the gate minted are in no Event**, and all are `Person.scar` writes
  (`loop/resolve.py:687-690`, whose return value is dropped). Of the 5,663 state changes that are not
  ledger bookkeeping, 69% are absent from the record. `_conviction_crisis` (`resolve.py:729-732`), the
  only writer that can fold or destroy a conviction, is built the same way. The stated reason
  (`resolve.py:637-640`): attaching the receipts to the act's Event *"would deposit claims about every
  scarred observer at WITNESS — a propagation change H3 does not license"*.
- `write_matrix.yaml:246,269` declare `emits: conviction.moved` and `emits: scar.taken` on those rows;
  neither kind is emitted in three seasons.

## The resolution, decided

The stated objection to recording the interior writes is an objection to **witnessing** them, and the
tree already separates the two: an Event the gate emits during a step is appended to the log directly
(`world.py:1476`) and is witnessed only if the step returns it (CALENDAR and MATTER return a log slice;
RESOLVE returns the fold's own list, `resolve.py:1200`). `claim.deposited` is the standing precedent for
an interior write that is logged and fans out to nobody. So: log them, fan them out to nobody.

For values: fill the field that exists, from what the gate already read. No second read, no new carrier.

Not chosen: deleting `delta`, `spec` and `mode` (the E-only cut). It is free today and it forecloses the
retelling; fill, do not amputate.

## Exact edits, by owner

1. **`engine/season/state/world.py::World.write`**, the `Change` branch:
   - `:1426-1427` keep the pair instead of the subject:
     `moved = [(s, b, a) for s, b in zip(change.subjects, was) for a in (… self.state_of(s) …,) if … a != b]`
     (edge subjects keep their tenure-diff test; their `delta` stays `None`: the Tenure is its own record).
   - `:1442` `self.gate.mint(s.id, "set", driver, fieldname, _delta(s, b, a))`, where `_delta` returns
     `(b, a)` when `s` names `fields`, and `None` for a whole-entity digest subject. For that case set
     `mode` honestly instead: `"create"` when `b == (False,)`, `"delete"` when `a == (False,)`, else
     `"set"`.
   - The closure branch (`apply=`, `:1394-1395`) is untouched: it has no observed value, which is H-145
     (F-CORE-11) and stays that row's.
2. **`engine/season/loop/resolve.py::_scar_witnesses`** (`:687`): add `emits="scar.taken"`,
   `subject=a.actor`, `causes=[a.id]` to the existing `w.write`, with each `Subject.entity(…,
   earns="scar.taken")` (`state/gate.py:1741`) so the gate's `extra` path (`world.py:1481-1492`) puts the
   per-person receipts on one Event. **`_conviction_crisis`** (`:729`): the same with `conviction.moved`. If the gate's
   single-kind `emits` path would mint a second, redundant receipt on `subject`, emit through `extra`
   alone; the implementer picks the form that yields exactly one Event per write carrying exactly the
   minted receipts. Delete the two docstring paragraphs that say nothing is emitted.
3. **`engine/season/tests/`**: the goldens re-pin once. No new test file; the existing receipt test
   (`G1a`) gains the planted case below.

## Gate (an execution artifact, §0.2)

| reading (`build_realm(0)`, two seasons) | today | passes when |
|---|---|---|
| receipts minted by the gate and carried by no Event (`p34.py`'s count) | 3,914 | 0 |
| `scar.taken` Events / `Person.scar` write calls | 0 / 315 per season | equal |
| claims deposited per season | 12,115; 10,607 | unchanged (the new Events fan out to nobody) |
| receipts on a fields-naming `Change` with `delta is None` | all | none |
| acts, per-act outcomes, every state component of `pes.proj` | — | identical to today's (only the log and the hash move) |
| a planted `Change` raising one cohort's `body` 940 → 1000 | receipt says `body` | receipt's `delta` decodes to `(940, 1000)` |

## Falsifier

Deposits per season change. Then a gate-emitted Event in RESOLVE does reach WITNESS by a path this
proposal did not see, the stated objection was right, and edit 2 is withdrawn (edit 1 stands alone).

## NERS reading (E last)

- **N.** Cut it and a narrator, a chronicle, a player's season summary and a port's replay test all
  re-read the present world to say what an old Event did. Top-down (premise: *recorded and retellable*),
  bottom-up (the gate has the value in hand), lateral (the matrix rows already declare the two kinds),
  vertical (Layer 1, `04 §C.2`: *"before = get(); store._set(); after = get()"* is the receipt's own
  recipe). Diagonal and horizontal: not tried.
- **R.** The interior is where a person's story turns (a conviction folding under repeated witness). It
  happens with no player and today leaves no trace; after this it is findable.
- **S.** One methodology for "what did this write do" (the receipt), where today a reader has the
  receipt for *which cell* and a state diff for *how much*.
- **E.** Two fields filled and two `emits=` arguments, against a log that cannot answer "by how much".

## Cost class

Small build. One deliberate golden re-record across `engine/season/tests` and `engine/tests` wherever a
content hash is pinned: say so plainly (CLAUDE.md §7). Log growth: about 315 Events a season on the
realm against 13,000.
