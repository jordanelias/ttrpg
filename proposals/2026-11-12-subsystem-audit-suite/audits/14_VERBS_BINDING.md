# VERBS — BINDING family: build-out of the twelve `binding_decision` verbs

## Status: REFERENCE (a verb build-out audit under `VERBS_BRIEF.md`; resolves nothing at runtime)

## Read at: 84d2a02 (working tree)

Family: the twelve rows of `engine/season/verb_table.yaml` whose `stratum:` is `binding_decision`:
`confer`, `convene`, `determine`, `dispatch`, `establish`, `issue`, `marshal`, `surrender`, `pardon`,
`release`, `revoke`, `succeed`. They are the governance verbs: who sits where, who is ordered, what a room
decides, who is let go. The FA lane's audit, addendum and proposals and the SC lane's proposals bind this
file; they are cited by path and not redone. The exact edits are in
`proposals/14_VERBS_BINDING_*.md`, one per batch of the landing order (§ "Landing order" at the end).

Every reading names its command, seed and season count. `[UNVERIFIED]` marks what was not checked.
`[FA]` marks a figure taken from the FA lane's run of the same instrument on the same tree
(`scratchpad/runs/FA/aperture_2_0.txt`), which this lane read at the line and did not re-run at that seed;
this lane's own reading is `aperture 2 1` (seed 1, two seasons), in
`scratchpad/runs/VERBS_BINDING/aperture_2_1.txt`.

## 0. Verdict for the family

**Two of the twelve work in computed play in the sense the premise requires; three execute and write
nothing a later decision reads; four form and are never chosen or are always refused; three are never
formed at all.** The mechanisms are sound almost everywhere (each effect returns a `Change` through the
write gate, each precondition asks the gate's own predicate, no entity is special-cased). What fails is
reach: the acts that redistribute power are not chosen, and the acts that are chosen bind nobody.

| verb | state (seed 0, 2 seasons, realm; `[FA]`) | verdict |
|---|---|---|
| `convene` | formed 12, attempted 12, executed 12 | **executes; consequence thin** (a date; summons nobody) |
| `dispatch` | formed 26, attempted 12, executed 12 | **executes but writes nothing** |
| `issue` | formed 18, attempted 26, executed 19, refused 7 on `authority` | **executes; binds nobody** |
| `establish` | formed 6, attempted 8, executed 1, refused 7 (no reason recorded) | **forms, mostly refused** |
| `determine` | formed 8, attempted 2, executed 0, refused 2 on `docket` | **forms but is refused** |
| `release` | formed 83, attempted 15, executed 0, refused 15 (no reason recorded) | **forms but is refused** |
| `confer` | formed 5, attempted 0 | **formed, never chosen** |
| `revoke` | formed 5, attempted 0; a computed act is refused at clause 1 by construction | **formed, unexecutable** |
| `pardon` | formed 8, attempted 0 (spine: 3 attempted, 3 refused) | **formed on no restraint** |
| `marshal` | eligible 26, formed 0 | **unreachable** |
| `surrender` | eligible 26, formed 0 | **unreachable** |
| `succeed` | eligible 83, formed 0 | **unreachable at this horizon** |

The per-verb sections follow in table order of the verb table. Each has the nine parts the brief orders.
