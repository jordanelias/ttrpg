"""`harness.loops` -- THE DERIVED CYCLE CHECK (`H-106`; `H-25` folded in): declared loops vs derived.

Plan position IN-24 (`BOUND-LOOPS`). `ID-16`'s loop representation has two halves and this module
reads both and compares them:

  (a) DECLARED -- the `kind: LOOP` rows of `engine/season/hole_register.yaml`, each with its `sign:`
      (`+` amplifying, `-` damping; `harness/register.py` owns `LOOP_KIND`/`LOOP_SIGNS`) and its
      `default:` cell, which on a LOOP row is what bounds the loop (`register.normalised_default`).
  (b) DERIVED -- the cycle set recomputed from what is WRITTEN against every TYPED READER, then
      signed. `derive_cycles` is a pure function over plain `Process` data so a test can plant on it.
  (c) BOUNDS -- for each LOOP row, the largest value of each looped quantity over caller-supplied
      seeded seasons, beside a caller-supplied numeric bound; a value above its bound fails.

THE GRAPH (`derive_cycles`). Nodes are QUANTITIES: the `write_matrix.yaml` cells (`Kind.field`, the
keys `data/matrix.py::MATRIX` loads) plus one more, `Event` -- the log every act and step emits into,
which is what WITNESS fans out. A `Process` reads some quantities and writes others, each with a
polarity: `+` (more of the read thing means more of this process; the write adds), `-` (the write
removes), `?` (not typed -- the instrument does not know). A process that reads `q` and writes `r`
is a link `q -> r` whose sign is the product of the two polarities, `?` absorbing. A CYCLE is an
elementary cycle of that quantity graph, signed by the product of its links (`+` amplifying, `-`
damping, `?` unsigned); parallel links of different signs give one cycle per resulting sign.

THE PROCESSES, AND WHERE EACH EDGE COMES FROM (`build_processes`):
  * EVERY VERB of `data/verbs.py::VERB_TABLE` is a RESOLVE process. It reads `Act[].returned` (`+`:
    a verb resolves only an act DELIBERATE returned) and the cells its `requires_typed:` cell asks
    for -- the `requires` grammar (`data/requires.py`), walked through `AllOf`, each leaf's predicate
    stem mapped to cells by `STEM_READS`. It writes its `writes:` cells (and every `writes_by_degree`
    band's) at polarity `?` -- THE GRAMMAR TYPES WHICH CELL A VERB WRITES AND NOT WHICH WAY -- and
    `Event` at `+` when its row declares any emission.
  * THE STEP READERS `H-106` NAMES -- the question sources, the witness channel predicates and the
    eviction comparator -- plus WITNESS's fan-out over the log and MATTER's claim decay, which
    `H-103` and `H-112` are about. Their reads are not typed anywhere in the tree, so they are
    declared here in `QUESTION_SOURCE_READS`, `CHANNEL_READS` and `STEP_READS`. Each is tied to an
    owner and REFUSES on drift: a question source the roster carries with no entry here,
    a stem in `REQUIRES_STEMS` with none, a step write to a matrix cell whose row does not list that
    step, or a cited code site whose anchor text is gone.

[ASSUMPTION, stated where it is used] `Event` is ONE quantity. WITNESS reads every Event in the
code's TOPOLOGY, while `World.write` buffers only MATTER's emissions for the fan -- that one-line cut
is `H-112`'s declared BOUND, not an absent edge, exactly as `H-102`'s fixtures flatten an amplifying
topology. The derivation sees topology; part (c) is where a bound is read.

THE DECLARED SIDE'S CYCLE KEYS. A LOOP row is prose; nothing in it is a cycle the derivation can
compare against. `DECLARED_CYCLES` maps each row id to the quantity cycle(s) the row describes; the
row's SIGN is read from the register, never restated here. A LOOP row with no entry here, or an entry
naming a row that is not a LOOP row, is reported as a mismatch, so the table cannot drift silently.
[ASSUMPTION: the correspondence is this module's reading of each row's `hole:`; the honest home is a
typed column on the row, which `register.py` admits only as `sign` today.]

THE COMPARISON (`compare`) is over AMPLIFIERS: every derived `+` cycle must be some `+` LOOP row's,
and every `+` row's cycles must be derived at `+`. Damping cycles are compared and printed beside it
(`G13` asks a bound only of `+`, and the register says its damping enumeration is not complete).
Unsigned cycles are printed with their count: each could be an undeclared amplifier, and the grammar
cannot say which. Blind spots -- verbs whose `requires` is untyped, steps whose reads are not
declared -- are printed too; a cycle through them is invisible to this check.

PART (c) (`check_bounds`, pure). [ASSUMPTION: the looped quantity of a LOOP row is EACH quantity on
its declared cycles that has a reader in `QUANTITY_READERS`, read at the end of every season and
maximised over seasons and seeds.] No LOOP row's `default:` carries a number, so every bound is
caller-supplied (`--bound ROW:QUANTITY=VALUE`): a reading with no bound prints UNCHECKED, never a
pass. An amplifier with no LOOP row has no bound to read and is not observed here -- part (b) is what
names it. Every numeric argument is required of the caller and none has a default
(`tools/ci_sim_fabrication_check.py` scope).

Entry point: `python -m engine.season.harness.loops` prints (a) and (b);
`... --base-seed S --n N --seasons K [--cap C] [--bound H-NNN:Kind.field=V ...]` adds (c).
Exit 1 when amplifiers differ or a bound fails; 0 otherwise.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from itertools import product

from ..data import files
from ..data.rosters import QUESTION_SOURCES, WITNESS_CHANNELS
from . import register as R

#: The log, as a quantity. Not a `write_matrix.yaml` cell: every write that emits lands here.
EVENT = "Event"
#: The quantity DELIBERATE writes and every verb reads (`write_matrix.yaml`'s `(Act[], returned)`).
ACTS = "Act[].returned"
SIGNS = ("+", "-", "?")
_TENURE = (("Tenure.since", "?"), ("Tenure.until", "?"))

#: What each `requires` predicate stem reads, as `write_matrix` cells. The owner of the dispatch is
#: `queries/world_q.py::WorldReader.read`; this is its transcription, closed against
#: `data/requires.py::REQUIRES_STEMS` at build time. `exists` is resolved per kind by `_exists_reads`.
STEM_READS = {
    "stores":       (("Rung.stores", "+"),),
    "condition":    (("Site.condition", "+"),),
    "floor":        (),                                   # `band_floors`, a fixture: written by none
    "quorum":       (),                                   # `bench_quorum`, a fixture
    "contain.path": _TENURE,
    "held_by":      (("Tenure.since", "+"), ("Tenure.until", "-")),
    "present_at":   _TENURE,
    "with":         _TENURE,
    "claim.held":   (("Person.claim_ledger", "+"),),
    "rank":         (("Rung.exists", "?"),),
    "purview":      (("Office.exists", "?"),) + _TENURE,
    "bench":        (("Office.exists", "?"),) + _TENURE,
    "bench.size":   _TENURE,
    "exists":       None,
}

#: What each `rosters.yaml: question_sources` member reads (`queries/world_q.py::questions_for`).
QUESTION_SOURCE_READS = {
    "claim_landed": (("Person.claim_ledger", "+"),) + _TENURE,   # the landing, filtered by reach
    "need":         _TENURE + (("Proposition.exists", "?"),),    # a live `commit` to an OUGHT
}

#: What the witness channel predicates read, as ONE reader: the union over every `_ch_<name>` in
#: `epistemic.py` (presence, `knot`, `hold` and `oblige` tenures; `chronicle` reads who is alive).
#: Not keyed per channel -- that would restate `rosters.yaml: witness_channels`, which
#: `test_jordan_no_definition_is_hardcoded_in_a_body` refuses -- so a channel added there with a new
#: read is NOT caught here; it is listed among the blind spots.
CHANNEL_READS = _TENURE + (("Person.exists", "?"),)


@dataclass(frozen=True)
class Process:
    """One reader-writer. `reads`/`writes` are `((quantity, sign), ...)`; `step` is the
    `write_matrix.yaml` step code a write must be listed under (`""` for none to check)."""
    name: str
    reads: tuple
    writes: tuple
    source: str = ""
    step: str = ""


#: The step readers, each with the code site its reads were read off and an anchor that must still
#: be there. `writes` to a matrix cell are checked against that cell's `steps:`.
STEP_READS = (
    Process("WITNESS: fan-out over the log", ((EVENT, "+"),),
            (("Person.claim_ledger", "+"), (EVENT, "+")),
            "loop/driver.py::SeasonDriver.season -- `self.witness(` over every round's Events; "
            "the deposit emits `claim.deposited` (write_matrix `(Person, claim_ledger)`)", "WIT"),
    Process("WITNESS: eviction comparator", (("Person.claim_ledger", "+"),),
            (("Person.claim_ledger", "-"),),
            "loop/witness.py::witness -- `evict_over_cap`; emits nothing", "WIT"),
    Process("MATTER: claim decay", (("Claim.confidence", "+"),),
            (("Claim.confidence", "-"), (EVENT, "+")),
            "loop/matter.py::matter -- `claim_decay`; emits `claim.decayed`", "MAT"),
)
_ANCHORS = {
    "WITNESS: fan-out over the log": ("loop/driver.py", "self.witness("),
    "WITNESS: eviction comparator": ("loop/witness.py", "evict_over_cap"),
    "MATTER: claim decay": ("loop/matter.py", "claim_decay"),
    "DELIBERATE": ("queries/world_q.py", "def questions_for"),
    "WITNESS: channel": ("epistemic.py", "CHANNEL_PREDICATES"),
}

#: Each LOOP row's cycle(s), as canonical quantity tuples (see `canonical`). The SIGN is the row's.
DECLARED_CYCLES = {
    # claim lands -> question -> act -> Event -> witnessed -> claim; and the `own_ledger` reader
    # (`tell`, `reconstruct`, `survey`) on the same ledger, which `H-106` names as part of it.
    "H-102": ((ACTS, EVENT, "Person.claim_ledger"), (EVENT, "Person.claim_ledger")),
    "H-103": (("Claim.confidence",),),
    "H-104": (("Person.claim_ledger",),),
    "H-112": ((EVENT,),),
}


# ---------------------------------------------------------------------------------------------
# THE DERIVATION. Pure over `Process` data.
# ---------------------------------------------------------------------------------------------

def _mul(a: str, b: str) -> str:
    if "?" in (a, b):
        return "?"
    return "+" if a == b else "-"


def canonical(cycle) -> tuple:
    """Rotate a node cycle so its least quantity leads; direction is kept."""
    c = tuple(cycle)
    i = c.index(min(c))
    return c[i:] + c[:i]


def links(processes) -> dict:
    """`{(src, dst): {sign: sorted process names}}` over every read x write of every process."""
    out: dict = {}
    for p in processes:
        for q, rs in p.reads:
            for r, ws in p.writes:
                for s in (rs, ws):
                    if s not in SIGNS:
                        raise ValueError(f"{p.name}: polarity {s!r} is not one of {SIGNS}")
                out.setdefault((q, r), {}).setdefault(_mul(rs, ws), set()).add(p.name)
    return {k: {s: sorted(v) for s, v in d.items()} for k, d in out.items()}


def _simple_cycles(adj: dict) -> list:
    """Every elementary cycle, each once, led by its least node (DFS over larger nodes only)."""
    nodes = sorted(adj)
    rank = {n: i for i, n in enumerate(nodes)}
    found = []
    for s in nodes:
        stack = [(s, iter(sorted(adj.get(s, ()))))]
        path, on = [s], {s}
        while stack:
            node, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                stack.pop()
                on.discard(path.pop())
                continue
            if nxt == s:
                found.append(tuple(path))
            elif nxt not in on and rank.get(nxt, -1) > rank[s]:
                path.append(nxt)
                on.add(nxt)
                stack.append((nxt, iter(sorted(adj.get(nxt, ())))))
    return found


def derive_cycles(processes) -> list:
    """`[{"key": canonical quantity tuple, "sign": "+"|"-"|"?", "via": ((processes per hop), ...)}]`,
    one entry per (cycle, resulting sign), sorted."""
    L = links(processes)
    adj: dict = {}
    for (q, r) in L:
        adj.setdefault(q, set()).add(r)
        adj.setdefault(r, set())
    out = []
    for cyc in _simple_cycles(adj):
        hops = [L[(cyc[i], cyc[(i + 1) % len(cyc)])] for i in range(len(cyc))]
        signs = set()
        for choice in product(*(sorted(h) for h in hops)):
            s = "+"
            for x in choice:
                s = _mul(s, x)
            signs.add(s)
        via = tuple(tuple(sorted({n for names in h.values() for n in names})) for h in hops)
        for s in sorted(signs):
            out.append({"key": canonical(cyc), "sign": s, "via": via})
    return sorted(out, key=lambda c: (len(c["key"]), c["key"], c["sign"]))


def compare(derived: list, loop_rows: dict, declared: dict) -> dict:
    """Derived cycles against the LOOP rows. `loop_rows` is `{row id: sign}`; `declared` is
    `{row id: (cycle tuple, ...)}`. Returns, per sign class (`+`, `-`), the undeclared (derived, no
    row) and underived (row, not derived at its sign) keys, plus `unmapped` rows (a LOOP row with no
    cycle key), `stale` keys (a key naming no LOOP row) and `equal` -- the amplifier verdict."""
    unmapped = sorted(r for r in loop_rows if not declared.get(r))
    stale = sorted(r for r in declared if r not in loop_rows)
    by_sign = {}
    for sign in ("+", "-"):
        got = {c["key"] for c in derived if c["sign"] == sign}
        want = {canonical(k): r for r, ks in declared.items() if loop_rows.get(r) == sign
                for k in ks}
        by_sign[sign] = {
            "derived": sorted(got), "declared": sorted(want.items()),
            "undeclared": sorted(got - set(want)),
            "underived": sorted((k, r) for k, r in want.items() if k not in got)}
    amp = by_sign["+"]
    equal = (not amp["undeclared"] and not amp["underived"]
             and not [r for r in unmapped if loop_rows[r] == "+"] and not stale)
    return {"by_sign": by_sign, "unmapped": unmapped, "stale": stale, "equal": equal,
            "unsigned": [c for c in derived if c["sign"] == "?"]}


# ---------------------------------------------------------------------------------------------
# PART (c). Pure over the readings and the caller's bounds.
# ---------------------------------------------------------------------------------------------

def check_bounds(rows: dict, observed: dict, bounds: dict) -> dict:
    """`rows` is `{row id: (quantity, ...)}`; `observed` is `{quantity: largest value | None}`;
    `bounds` is `{(row id, quantity): number}`. Each line reads FAIL (observed > bound), PASS,
    UNCHECKED (no bound supplied) or NOT OBSERVED (no reading). A bound naming a quantity that is not
    on that row's cycles refuses: it would be a bound on nothing."""
    for (r, q) in bounds:
        if q not in rows.get(r, ()):
            raise ValueError(f"bound {r}:{q} names no looped quantity of {r} "
                             f"(its quantities: {list(rows.get(r, ()))})")
    lines = []
    for r in sorted(rows):
        for q in rows[r]:
            v, b = observed.get(q), bounds.get((r, q))
            verdict = ("NOT OBSERVED" if v is None else "UNCHECKED" if b is None
                       else "FAIL" if v > b else "PASS")
            lines.append({"row": r, "quantity": q, "observed": v, "bound": b, "verdict": verdict})
    return {"lines": lines, "failed": any(x["verdict"] == "FAIL" for x in lines),
            "checked": sum(x["verdict"] in ("PASS", "FAIL") for x in lines)}


def row_quantities(declared: dict) -> dict:
    """`{row id: quantities on its declared cycles, first-seen order}`."""
    return {r: tuple(dict.fromkeys(q for k in ks for q in k)) for r, ks in declared.items()}


def _ledger_max(w):
    return max((len(p.ledger) for p in w.persons.values()), default=None)


def _confidence_max(w):
    return max((c.confidence for p in w.persons.values() for c in p.ledger), default=None)


#: `quantity -> reader(world, season summary, events logged this season)`, read after each season.
QUANTITY_READERS = {
    "Person.claim_ledger": lambda w, summary, n_logged: _ledger_max(w),
    "Claim.confidence":    lambda w, summary, n_logged: _confidence_max(w),
    EVENT:                 lambda w, summary, n_logged: n_logged,
    ACTS:                  lambda w, summary, n_logged: summary.get("acts"),
}


def observe(quantities, seeds, seasons: int, cap=None) -> dict:
    """`{quantity: largest per-season reading over seeds x seasons}` for each quantity with a reader;
    a quantity with none reads `None`. The composition is `harness/storybar.py::drive`'s, repeated
    because a reading is taken after EVERY season and `drive` exposes no per-season hook."""
    from ..decision import make_chooser
    from ..loop.driver import SeasonDriver, resolvable_verbs
    from ..state.ids import H, draw_factory
    from . import probes as P
    from .populated import build_realm

    best = {q: None for q in quantities}
    for seed in seeds:
        w = build_realm(seed, cap)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        for _ in range(seasons):
            before = len(w.log)
            summary = d.season(ch, question=None, subsistence=P.SUBSIST,
                               contest_max_depth=w.fixtures.get("contest_max_depth"))
            for q in quantities:
                read = QUANTITY_READERS.get(q)
                v = None if read is None else read(w, summary, len(w.log) - before)
                if v is not None and (best[q] is None or v > best[q]):
                    best[q] = v
    return best


# ---------------------------------------------------------------------------------------------
# ASSEMBLY FROM THE OWNERS.
# ---------------------------------------------------------------------------------------------

def _leaves(req):
    for c in getattr(req, "clauses", None) or ():
        yield from _leaves(c)
    if getattr(req, "clauses", None) is None:
        yield req


def _exists_reads(kind: str, cells) -> tuple:
    """`exists:<kind>`, per `WorldReader.read`'s branches: an edge kind, a record kind, the docket,
    or one of `World`'s collections -- here, that kind's `exists` cell."""
    from ..queries.world_q import DOCKET_KIND, RECORD_KINDS, TENURE_KINDS
    if kind in TENURE_KINDS:
        return (("Tenure.since", "+"), ("Tenure.until", "-"))
    if kind in RECORD_KINDS:
        return (("Record.exists", "+"),)
    if kind == DOCKET_KIND:
        return (("DocketItem.matter", "+"),)
    if f"{kind}.exists" in cells:
        return ((f"{kind}.exists", "+"),)
    raise SystemExit(f"loops: `exists:{kind}` maps to no write_matrix cell; extend `_exists_reads`")


def build_processes() -> tuple:
    """`(processes, blind_spots)` from the owners: `VERB_TABLE`, `MATRIX`, `REQUIRES_STEMS`, the two
    rosters, and the step readers above. Refuses on any drift named in the module docstring."""
    from ..data.matrix import MATRIX, _STEP_OF
    from ..data.requires import REQUIRES_STEMS
    from ..data.verbs import NO_PRECONDITION, VERB_TABLE

    cells = {f"{k}.{f}": row for (k, f), row in MATRIX.items()}
    known = set(cells) | {EVENT}
    if set(STEM_READS) != set(REQUIRES_STEMS):
        raise SystemExit(f"loops: STEM_READS {sorted(STEM_READS)} != REQUIRES_STEMS "
                         f"{sorted(REQUIRES_STEMS)}; a stem with no read map is invisible")
    if set(QUESTION_SOURCES) != set(QUESTION_SOURCE_READS):
        raise SystemExit(f"loops: question_sources {sorted(QUESTION_SOURCES)} != read map "
                         f"{sorted(QUESTION_SOURCE_READS)}")
    root = files.HOLE_REGISTER_YAML.parent
    for name, (rel, anchor) in _ANCHORS.items():
        if anchor not in (root / rel).read_text():
            raise SystemExit(f"loops: {name}'s site {rel} no longer carries {anchor!r}; "
                             "re-read the step and re-declare its reads")

    procs, untyped = [], []
    for verb, row in sorted(VERB_TABLE.items()):
        reads = [(ACTS, "+")]
        if row.requires_typed is not None:
            for leaf in _leaves(row.requires_typed.requirement):
                for stem in leaf.stems():
                    reads += (_exists_reads(leaf.kind, cells) if stem == "exists"
                              else STEM_READS[stem])
        elif str(row.requires).strip() not in NO_PRECONDITION:
            untyped.append(verb)
        wr = list(row.writes) + [c for band in (row.writes_by_degree or {}).values() for c in band]
        writes = [(c, "?") for c in dict.fromkeys(wr)]
        emits = list(row.emits) + list(_flat(row.emits_on_refusal))
        if emits:
            writes.append((EVENT, "+"))
        procs.append(Process(f"RESOLVE:{verb}", tuple(dict.fromkeys(reads)), tuple(writes),
                             "verb_table.yaml", "RES"))
    ledger_w = (("Person.claim_ledger", "+"),)
    procs.append(Process("DELIBERATE: question sources",
                         tuple(dict.fromkeys(x for s in QUESTION_SOURCES
                                             for x in QUESTION_SOURCE_READS[s])),
                         ((ACTS, "+"),), "queries/world_q.py::questions_for", "DEL"))
    procs.append(Process("WITNESS: channel predicates", CHANNEL_READS, ledger_w,
                         "epistemic.py::CHANNEL_PREDICATES", "WIT"))
    procs.extend(STEP_READS)

    for p in procs:
        for q, _ in p.reads + p.writes:
            if q not in known:
                raise SystemExit(f"loops: {p.name} names {q!r}, not a write_matrix cell")
        for q, _ in p.writes:
            if q != EVENT and p.step and p.step not in {k for k, v in _STEP_OF.items()
                                                        if _matrix_has(cells[q], v)}:
                raise SystemExit(f"loops: {p.name} writes {q} at {p.step}, and the write_matrix "
                                 f"row lists {sorted(s.value for s in cells[q].steps)}")
    writing_steps = {s.value for row in MATRIX.values() for s in row.steps}
    declared = {"RESOLVE", "DELIBERATE", "WITNESS", "MATTER"}
    blind = {"untyped_requires": untyped,
             "undeclared_step_reads": sorted(writing_steps - declared)
             + ["MATTER (every pass but claim decay)", "DELIBERATE (all but its question sources)",
                f"WITNESS channels as one union, not per channel ({len(WITNESS_CHANNELS)} rostered)"]}
    return tuple(procs), blind


def _flat(cell):
    if isinstance(cell, dict):
        return [k for v in cell.values() for k in v]
    return list(cell or ())


def _matrix_has(row, step_value: str) -> bool:
    return any(s.value == step_value for s in row.steps)


def loop_rows(reg: dict) -> dict:
    """`{row id: row}` for every `kind: LOOP` row of the register."""
    return {r["id"]: r for r in reg["rows"] if str(r.get("kind") or "") == R.LOOP_KIND}


# ---------------------------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------------------------

def _key(k) -> str:
    return " -> ".join(k) + f" -> {k[0]}"


def _bound_arg(s: str) -> tuple:
    try:
        lhs, val = s.rsplit("=", 1)
        row, q = lhs.split(":", 1)
        return (row, q), float(val)
    except ValueError:
        raise argparse.ArgumentTypeError(f"--bound wants ROW:QUANTITY=NUMBER, got {s!r}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base-seed", type=int)
    ap.add_argument("--n", type=int, help="seeded realms")
    ap.add_argument("--seasons", type=int)
    ap.add_argument("--cap", type=int, default=None,
                    help="build_realm's cast cap; omitted = build_realm's own None")
    ap.add_argument("--bound", type=_bound_arg, action="append", default=[],
                    help="ROW:QUANTITY=NUMBER, repeatable; no bound has a default")
    ap.add_argument("--all-unsigned", action="store_true", help="print every unsigned cycle")
    a = ap.parse_args(argv)
    run_c = (a.base_seed, a.n, a.seasons)
    if any(x is not None for x in run_c) and not all(x is not None for x in run_c):
        ap.error("part (c) needs all of --base-seed, --n and --seasons")

    rows = loop_rows(R.load())
    signs = {r: row.get("sign") for r, row in rows.items()}
    procs, blind = build_processes()
    derived = derive_cycles(procs)
    res = compare(derived, signs, DECLARED_CYCLES)

    print(f"(a) DECLARED: {len(rows)} LOOP rows in {files.HOLE_REGISTER_YAML.name}")
    for r, row in rows.items():
        keys = DECLARED_CYCLES.get(r, ())
        print(f"  {r} sign={row.get('sign')} cycles={[_key(k) for k in keys] or 'NONE MAPPED'}")
    print(f"(b) DERIVED: {len(procs)} processes, {len(derived)} cycles "
          f"(+ {sum(c['sign'] == '+' for c in derived)}, - {sum(c['sign'] == '-' for c in derived)}"
          f", ? {len(res['unsigned'])})")
    for sign, name in (("+", "AMPLIFYING"), ("-", "DAMPING")):
        b = res["by_sign"][sign]
        print(f"  {name} derived: {[_key(k) for k in b['derived']]}")
        print(f"  {name} declared: {[f'{r}: {_key(k)}' for k, r in b['declared']]}")
        print(f"  {name} undeclared (derived, no LOOP row): {[_key(k) for k in b['undeclared']]}")
        print(f"  {name} underived (LOOP row, not derived): "
              f"{[f'{r}: {_key(k)}' for k, r in b['underived']]}")
    if res["unmapped"] or res["stale"]:
        print(f"  LOOP rows with no cycle key: {res['unmapped']}; keys naming no LOOP row: "
              f"{res['stale']}")
    us = res["unsigned"]
    cells = sorted({q for c in us for q in c["key"]} - {EVENT, ACTS, "Person.claim_ledger"})
    print(f"  UNSIGNED: {len(us)} cycles the grammar cannot sign (a verb's write has no polarity); "
          f"each could be an undeclared amplifier. State cells on them: {cells}")
    for c in (us if a.all_unsigned else ()):
        print(f"    {_key(c['key'])}  via {[list(v) for v in c['via']]}")
    print(f"  BLIND: verbs with an untyped `requires` (their reads are invisible): "
          f"{blind['untyped_requires']}")
    print(f"  BLIND: steps whose reads are not declared here: {blind['undeclared_step_reads']}")
    print(f"  AMPLIFIERS: derived {'==' if res['equal'] else '!='} declared")

    rq = row_quantities({r: DECLARED_CYCLES.get(r, ()) for r in rows})
    bounds = dict(a.bound)
    if not all(x is not None for x in run_c):
        print("(c) BOUNDS: not run -- no seeds supplied (--base-seed/--n/--seasons); nothing "
              "observed, nothing passed")
        if bounds:
            ap.error("--bound given without seeds to observe")
        return 0 if res["equal"] else 1
    seeds = list(range(a.base_seed, a.base_seed + a.n))
    observed = observe(sorted({q for qs in rq.values() for q in qs}), seeds, a.seasons, a.cap)
    out = check_bounds(rq, observed, bounds)
    print(f"(c) BOUNDS: seeds={seeds[0]}..{seeds[-1]} seasons={a.seasons} cap={a.cap}")
    for x in out["lines"]:
        dflt = " ".join(str(rows[x["row"]].get("default") or "").split())
        print(f"  {x['row']} {x['quantity']}: observed={x['observed']} bound={x['bound']} "
              f"{x['verdict']}  | declared: {dflt[:90]}{'...' if len(dflt) > 90 else ''}")
    print(f"  {out['checked']} of {len(out['lines'])} readings checked against a bound; an "
          "amplifier with no LOOP row is not observed here -- part (b) names it")
    return 0 if res["equal"] and not out["failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
