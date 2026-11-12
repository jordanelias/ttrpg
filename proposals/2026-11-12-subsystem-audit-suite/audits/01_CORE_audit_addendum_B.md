# CORE — adversarial steelman audit · addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 785bc62 (working tree)

Addendum to `01_CORE_audit.md` (read at `601e715`). It covers what that audit declared skipped —
`loop/predicates.py`, `seam/wrappers/mass_battle.py` and the rest of `seam/wrappers/`, the `data/` loaders,
the `harness/` instruments it did not open, `registers/handoffs/HANDOFF_IN.md` and
`architecture/meta/04_CODE_ARCHITECTURE.md` — and adds the two sections the brief's later amendments ask
for that the audit does not carry: a Layer-1 conformance reading (§4 here) and the capability authoring
surface (§5 here, the brief's §14). The first audit is not edited; where this reading contradicts it, the
correction is in §3.

Finding numbers continue from the audit's last (F-CORE-11): F-CORE-12 onward.

## 1. What was read

Read in full, with comments and docstrings (line counts from `wc -l`):

| file | lines | note |
|---|---|---|
| `architecture/meta/04_CODE_ARCHITECTURE.md` | 1,657 | all of Parts A–G |
| `registers/handoffs/HANDOFF_IN.md` | 32 | Open and Standing orders |
| `loop/predicates.py` | 711 | nine registered predicates |
| `seam/wrappers/mass_battle.py` | 515 | |
| `seam/wrappers/__init__.py`, `pool.py` | 47, 100 | `pool.py` re-read in full for §5 |

| `data/cast.py`, `goals.py`, `pursuits.py`, `affiliations.py`, `arrangements.py`, `geography.py`, `__init__.py` | 545, 580, 171, 213, 287, 63, 62 | the lazy and import-time loaders |
| `data/rosters.py` | 1,590 | every roster binding, the capability maps (`VERB_CAPABILITY`, `VOCATION_ATTRIBUTE`, `VOCATION_OPPOSED_BY`, `LIFEPATH_TEMPLATES`) |
| `data/fixtures.py` | 1,169 | `Fixtures`, the matter tables, `DEFAULT_FIXTURES` |

<!-- APPEND-1 -->

## Working notes (kept while reading; folded into §2–§5 below)

- `loop/predicates.py`: nine predicates registered (`confer, convene, dispatch, establish, interrogate,
  oblige, release, revoke, succeed`); the module docstring says seven/five, the tail comment enumerates
  eight including the retired `give` and omits `succeed`, `interrogate`. Four raise `TypeError` on a
  list-valued operand (`dispatch`, `convene`, `revoke`, `oblige`) where five refuse; `_admits` calls
  `bool(pred(w, a))` with no catch (`loop/resolve.py:285`). Probe: `probe_predicates.txt`.
  REM-14's trace clause is written by five (`_refuse`) and not by `confer` (6 bare `return False`),
  `establish` (9), `oblige` (4), `succeed` (2).
- No predicate reads a capability; `04` §B.7 / D-33 refuses `capability` as an eligibility kind.
- `seam/wrappers/pool.py::faculty` is the one pool reader: `VERB_CAPABILITY[verb]` → `Person.capability[key]`,
  `VOCATION_ATTRIBUTE[key]` → `Person.attributes[attr]`, max of the two, else `pool_default`; plus
  `POOL_ADDENDS` (practice). Opposition: `VOCATION_OPPOSED_BY`.
- `data/cast.py`: the authored character row is `references/npc_registry.yaml` — `stats:` → attributes,
  `lifepath:` → capability keys at `pool_default`, `ts:` → thread sensitivity, `heritage:`, `convictions:`
  (pursuits), `affiliations:`; attribute roster and bounds in `engine/substrate/descriptors.py`.
- `data/fixtures.py`: `budget_office_bonus=1` ships; `04` §A.3 row 15 refuses an office bonus (tracked:
  IN-14, HANDOFF_IN "Build-order item 4 REVERTED"). `pool_default`'s comment (*"exactly one writer … which
  ZEROES it"*) is stale against `pool.py` and `cast.capability_of`.

