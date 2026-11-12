# CORE — a governance refusal that never crashes and says which clause refused

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_B.md` F-CORE-14. Read at `785bc62`.

## What it changes in `engine/season/` at runtime

Step one: nothing in any computed season (no computed act carries a list operand; a trace row is not
world state). A hand-built or client-returned act with a malformed operand is refused with the row's
refusal kind instead of ending the season. Step two is a declared hash mover: a refused `confer`,
`establish`, `revoke` or `oblige` emits a kind that names its clause.

## The problem, with evidence

`loop/predicates.py` registers nine predicates. `probe_predicates.py` (this addendum's evidence log):

| predicate | bare `return False` | `_refuse(clause, …)` | list-valued operand |
|---|---|---|---|
| `confer` | 6 | 0 | refuses |
| `establish` | 9 | 0 | refuses |
| `oblige` | 4 | 0 | **raises `TypeError`** |
| `succeed` | 2 | 0 | refuses |
| `revoke` | 0 | 4 | **raises** |
| `interrogate` | 0 | 3 | refuses |
| `release` | 0 | 2 | refuses |
| `convene` | 0 | 2 | **raises** |
| `dispatch` | 0 | 1 | **raises** |

The fold calls `ok = bool(pred(w, a))` with no catch (`loop/resolve.py:285`), so a raise leaves the fold.
REM-14 added `_refuse` so that *"a predicate with several `return False` lines"* could say which; four
predicates, with twenty-one refusing branches between them, were not converted. Where the clause is
recorded it goes to `TRACE` (a process-global list) and never to the Event, because a keyed
`emits_on_refusal:` is admitted only on a typed cell (`data/verbs.py:972-976`: *"a predicate's conjuncts
live in `loop/`, which this loader may not import"*). The persons who hold seats therefore learn least
from a refusal: `confer.refused` is one kind for seven causes.

## The resolution

Three edits at the owners, in two steps. No guard.

## Step one (hash EQUAL)

### 1 · owner `engine/season/state/carriers.py::subject_of` — one referent read that cannot be unhashable

`subject_of` is documented as *"THE ONE READ"* and returns `d.get("subject") or ""`. It returns `""`
for any value that is not a `str`. Old: `return d.get("subject") or ""`. New:

```python
s = d.get("subject")
return s if isinstance(s, str) else ""
```

A sibling `operand_of(a, name) -> str` with the same rule serves `office`, `to`.
`[UNVERIFIED: that no computed act carries a non-string subject today. The predicates' own comments say
the case arises from hand-built acts; the gate's two hashes are what would show otherwise, and if either
moves the edit is confined to the four predicates and `subject_of` is left alone.]`

### 2 · owner `engine/season/loop/predicates.py` — every predicate reads through it

`_req_dispatch` (`:621-624`), `_req_convene` (`:662-673`) and `_req_revoke` (`:593-596`) read
`payload` directly; `_req_oblige` (`:514-515`) passes a possibly unhashable `seat` to `dict.get`. Each
reads `subject_of(a)` / `operand_of(a, "office")`. `_req_convene`'s carve-out (no subject admits) is
kept by testing the raw key's absence before the read. The three inline guards (*"a list … is
unhashable: refuse, never raise"*) at `:141-142, :152-153, :191-192` become the same call, so the rule
lives once.

### 3 · same owner — every refusing branch names its clause

The twenty-one bare `return False` in `confer`, `establish`, `oblige`, `succeed` become
`return _refuse("<clause>", "<ids>")`, each clause a short fixed phrase taken from the docstring's own
numbered list (`establish`: `office resolves`, `rung held`, `conferral basis`, `filler`, `re-founding`,
`may fill`, `reduction needs revocation`).

**Gate.** `probe_predicates.py` re-run: nine predicates, zero bare refusals, zero raises on the planted
list operand; `headless --case NPC-088 --seasons 2 --seed 0` prints `5405522c36b0399247f83fd9f6d29494`.
**Falsifier.** Any predicate still raising on `{"subject": ["a", "b"]}`; a changed headless hash.

## Step two (a declared hash mover; one commit per row)

### 4 · owner `engine/season/loop/predicates.py`, `data/verbs.py`, `verb_table.yaml` — the clause reaches the Event

A predicate may return `(ok, clause)` where `clause` is one of the names it declares:

```python
@requires_predicate("confer", clauses=("office", "basis", "conferee", "purview", "held", "displacement"))
def _req_confer(w, a) -> tuple[bool, Optional[str]]: ...
```

`_admits` builds `Verdict(UNKNOWN, (), failed=clause)` for a predicate row (it builds
`Verdict(UNKNOWN, ())` today) and already calls `row.refusal_for(verdict.failed)`. No `observed` reads
are attached, so WITNESS deposits nothing new from the read itself; what changes is the refusal *kind*.
The loader's rule *"a keyed row must be typed"* gains its second arm: a keyed predicate row is admitted
when its keys equal the clause names passed in by the driver (`precondition_evaluable(predicates)`
already receives the predicate table as a parameter for the same import-direction reason). A flat
predicate row is unchanged.

The rows that take it first, and the kinds they key: `confer`, `establish`, `revoke`, `oblige` — the
kinds are authored in `verb_table.yaml` by the FA lane (they are governance vocabulary); this proposal
supplies the channel.

**Gate.** A seeded season in which a `confer` is refused at the purview clause emits the purview kind and
not the cardinality kind, and the actor's ledger holds a claim keyed by it (so §F1 clause 4 can decline
the same act through the same seat next round). **Falsifier.** Two refusals for different clauses
emitting one kind on a keyed row.

## NERS reading

- **N.** From the actor's side a refusal he cannot read is one he repeats; from the fold's side the
  clause is already known and discarded; laterally the typed cells have carried it since plan position
  `19`. Holds in the three directions.
- **R.** Strategic play by seat-holders needs a refusal that teaches; completeness requires that a
  malformed act be refused, not fatal.
- **S.** *Calculations consistent in methodology*: predicate rows and typed rows report a failed
  clause the same way.
- **E (last).** Two functions and a decorator argument; twenty-one one-line edits.

## Cost class

Step one: edit. Step two: small build plus data authoring by the FA lane.
