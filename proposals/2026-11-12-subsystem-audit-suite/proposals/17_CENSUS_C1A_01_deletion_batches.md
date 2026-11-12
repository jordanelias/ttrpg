# Census C1A · 01 — deletion batches for the season loop's core packages

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-15) — D2 stands. Its premise that no proposal names the projection is corrected: `09_WR_B_chronicle_that_tells.md` (R-32), `09_WR_B_threadwork_session_and_practitioner.md`, `19_LACUNA_verdict_ladder_and_reversal.md` and `02_CHAR_voices_and_the_room.md` did; each now carries a `Reconciled:` line re-pointing it at `account` or at its own helper, so the deletion still leaves no reader behind. Order unchanged: after `11_GO_player_surface_contract_B.md`.

## Status: PROPOSED

Author: census lane C1A. Audit: `audits/17_CENSUS_C1A.md` (findings F-C1A-01, F-C1A-06; rows in its §3
and §4). Read at b805fad.

## What it changes in `engine/season/` at runtime

Nothing. Every name below is called by no step, effect, predicate, query, module, harness instrument or
tool. No seeded run moves; no golden is re-recorded. What changes is what a reader is told exists: a
client read, a taxonomy class, a registry report and two query twins stop standing as if something used
them.

## The problem

A top-level name that only a test calls (or nothing calls) passes every gate and describes a capability
the game does not have. The audit's upward search found, in this partition, the names below. Each was
read at its site and grepped across `engine/`, `modules/`, `systems/`, `tools/` and `tests/`.

## The batches, ordered by risk (lowest first)

Each batch is one commit. Line numbers are at b805fad. A deleted **file** needs its `FORK:` row in
`references/restructure_ledger.md`; a deleted symbol inside a surviving file does not (the path still
resolves), and its record is the commit.

### D1 · names nothing calls (no test edit beyond one assertion)

| file | delete | also |
|---|---|---|
| `engine/season/gaps.py` | `class Ineligible` (`:87-107`) | nothing imports it; refusal by ineligibility is the Event kind `FOLD_INELIGIBLE` (`loop/resolve.py:88, :220`) |
| `engine/season/data/cast.py` | `def name_of` (`:118-126`) | `engine/season/tests/test_cr30_heritage.py:131`: replace the assertion with `assert (cast.row("NPC-020")["first_name"], cast.row("NPC-020")["last_name"]) == ("Almud", "Almqvist") and (cast.row("NPC-052")["first_name"], cast.row("NPC-052")["last_name"]) == ("Magnus", "Vaynard")` |
| `engine/season/data/cast.py` | `def defects` (`:408-423`) | its paren check moves into the loader (proposal 02, W3), landed in the same commit |
| `engine/season/data/files.py` | `SEAM_DIR` (`:246`), the comment block `:247-250`, `COMBAT_SEAM_PY` (`:251`) | `engine/season/seam/__init__.py:26`: correction in proposal 02 (C1) |
| `engine/season/state/world.py` | `_FIRST, _SECOND = _itemgetter(0), _itemgetter(1)` (`:166`) | drop `itemgetter as _itemgetter` from the import at `:40-41` (no other use) |

Why `name_of` is dead and not a missing wire: a person's displayed name is `Person.name`, built from the
case row's `name:` (`harness/populated.py:1315`); at `build_realm(0)` all 83 persons are named without this
function. `name_of` formats a second source (`first_name`, `last_name`) that no display reads.

Cut test: what dies is one assertion's spelling. Gate: `python -c "import engine.season.gaps,
engine.season.data.cast, engine.season.data.files, engine.season.state.world"` exits 0, and
`python -m pytest engine/season/tests/test_cr30_heritage.py -q` is green. Falsifier:
`grep -rn "Ineligible\b\|cast\.name_of\|cast\.defects\|COMBAT_SEAM_PY\|SEAM_DIR\|_FIRST\b\|_SECOND\b" engine modules systems tools tests --include=*.py`
returns a use outside the deleted lines.

### D2 · the person projection (one test file dies)

| file | delete |
|---|---|
| `engine/season/queries/world_q.py` | the section header `:4359-4362`, `_person_or_refuse` (`:4364-4371`), `witnessed` (`:4374-4406`), `PersonProjection` (`:4410-4431`), `projection` (`:4434-4441`); then `import copy` (`:32`) if `grep -n "copy\." engine/season/queries/world_q.py` is empty (it was, outside `:4440-4441`) |
| `engine/season/tests/test_person_projection.py` | the file (115 lines, 5 tests, all on the deleted names) |

`FORK:` row (the sha is the last commit touching the test file; in this clone
`git log -1 --format=%h -- engine/season/tests/test_person_projection.py` gives `60d13a7`, and the clone
is shallow, so run `git fetch --unshallow` and re-read it before writing the row):

```
| `engine/season/tests/test_person_projection.py` | `FORK:<sha8>` | FORKED (<date>, census C1A D2: the five tests of `world_q.projection` / `witnessed` / `PersonProjection`, v9 PC-06 S-2/L-1, a per-person client read that no harness, tool or plan called; the player's reading is the ledger-only `account` and the host-side `receipt` of the player surface contract; `<sha8>` is the last commit touching it, so the text there is the file) |
```

Why dead and not a missing wire: the proposal the suite accepted for the player's reading,
`11_GO_player_surface_contract_B.md` §3-§4, reads the person's own ledger (`account`) and walks forward
from his own act (`receipt`). `PersonProjection` hands a client copies of whole Events selected by
witness, and its docstring (`world_q.py:4384-4388`) leaves open whether an inferred Event belongs there.
Wiring it would add a second owner of "what a client reads for one person".

**Order:** after GO-B is accepted. If GO-B is rejected, hold D2: the projection is then the only typed
client read in the tree.

Also correct, in the same commit: `09_WR_B_threadwork_session_and_practitioner.md:170, :214` and
`09_WR_B_chronicle_that_tells.md:29-32` describe `PersonProjection` as a present reader; the unification
lane should point them at `account`.

Gate: `python -c "import engine.season.queries.world_q"` exits 0 and a seeded one-season `content_hash`
at seed 0 equals the hash before the commit. No shape test or registry enumerates the deleted names
(`grep` over `tests/test_season_shape.py`, `tests/valoria/`, `write_matrix.yaml`, `rosters.yaml`: none). Falsifier: `grep -rn "PersonProjection\|world_q\.projection\|world_q\.witnessed\|import.*\bprojection\b" engine modules tools --include=*.py`
finds a call.

### D3 · two test-only twins of a live pair (one test file re-pointed)

| file | delete | re-point |
|---|---|---|
| `engine/season/queries/person_q.py` | `violated_pursuits` (`:637-654`), `violated_affiliations` (`:657-670`) | `engine/season/tests/test_h11_affiliation_scar.py` (8 uses): `violated_pursuits(p, v)` becomes `broken_by(p, (elements_violated_by(v)[0], frozenset()))` and `violated_affiliations(p, v)` becomes `broken_by(p, (frozenset(), elements_violated_by(v)[1]))` (each half of the live pair, exactly); where the test wants both, `broken_by(p, elements_violated_by(v))` whole |

Keep `_pursuits_violated_by` (`:673`) and `_affiliations_violated_by` (`:746`): `elements_violated_by`
(`:754`) calls them and `loop/resolve.py::_scar_witnesses` calls that. Move the two deleted docstrings'
statement of the rule (which elements an act violates, and why by sign) onto `elements_violated_by`, which
today defers to them (`:755-756`); also reword `broken_by`'s docstring (`:771-773`), which defines itself
by the deleted names.

Cut test: the tests then exercise the path the loop runs, where today they exercise a twin of it. Gate:
`python -m pytest engine/season/tests/test_h11_affiliation_scar.py -q`. Falsifier: a seeded season's scar
counts differ before and after (they cannot: `resolve.py` never called the deleted names).

### Not in these batches

- `faction_q.superiors` and the standalone `holdings`: `06_FA_hygiene.md:39` already deletes them.
- `world_q.footprint`, `density`, `sovereign_fraction`, `provinces_of`: no caller, and **not deleted**,
  because `architecture/holonic_ARCHITECTURE.md:597-598` names three of them and the fourth implements a
  ratified ruling. See the audit's §6.
- `seam/wrappers/combat.load_error`, `files.loop_source`, `files.decision_modules`, `rosters.MODULES`,
  `options.operands_for` and the `*_without_*` report functions: read by tests that are themselves the
  check; false positives.

## NERS reading

N: each name can be removed without worsening play, by construction (nothing plays through it); the one
with a claim to necessity, the projection, is replaced by a reading with a narrower leak. R: nothing a
player or a world does is lost; completeness improves by one open contract question retired with its
subject. S: one fewer player-view dialect, one fewer ladder for "which elements an act violates".
E, last and as a ratio: about 190 lines of code and 115 of test leave, against no function lost.

## Cost class

Edit. Three commits, each with the one test file it touches.
