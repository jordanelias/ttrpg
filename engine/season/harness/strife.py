"""`harness.strife` -- WHICH OF THE STUDY'S 40 STRIFE MOVES THE SEASON LOOP CAN REACH, AND WHICH IT DID.

An INSTRUMENT, like `harness/aperture.py`: it reads the Event log and writes nothing, so it moves no
hash. The vocabulary is `strife_moves.yaml` (loaded by `harness/strife_data.py`), a reading of the study
"Mechanics of Strife to c. 1600". Each code is graded on separate things, because one number would
hide which owner closed it:

    route      STATIC. A verb the loop can resolve (`resolvable_verbs()`) whose row `emits:` a kind the
               code names. No route means a CONDITION OF POSSIBILITY IS MISSING (a verb, an effect, a
               seat, a switch): it is a build item, and the observed arm cannot be read for that code
    observed   DYNAMIC. Events in the log of a populated realm run through `populated.run`, pooled
               over the seeds given. A 0 is a finding about default play, never proof of absence
    act-level  an Event matched by a SIGNATURE: the Event's kind AND the verb of the act that caused it
               AND, for a march, the side of the marching faction. Side is read against the factions
               that govern the rung marched on, nearest first: the attacker is the authority (A) when
               it is the nearest governor or a governor above it, a challenger (R) when it governs
               nothing up that chain, and an outside power (O) when it is a foreign faction. An Event matching no signature is not guessed at

A code with a signature is graded on signature matches alone. A code with a `dark` switch and no
signature is DARK: its kinds are shared with other codes (`march.declared` is also an ordinary march),
so a kind count cannot show the switch has been thrown. A code whose row says it needs side, office
or context and has no signature is KIND-ONLY: the count is an UPPER BOUND. A code with no kind is GAP.

NOT HERE, AND WHY. The study's 16 links and its leave-and-rejoin profile need STRANDS (master design
§4 linking), which are batch S3's. Computing them over the raw log would link unrelated strife.

    python -m engine.season.harness.strife <seasons> <seed> [seed ...]
"""
from __future__ import annotations

import sys
from collections import Counter
from typing import Callable, NamedTuple, Optional

from ..data.rosters import DETAIN_KIND
from ..data.verbs import VERB_TABLE
from ..loop.driver import resolvable_verbs
from ..queries.world_q import faction_holding, faction_of, hold_force
from ..state.attribution import causing_act
from ..state.containment import ancestry
from . import populated
from .strife_data import FOREIGN, MOVES, SIGNATURES


class Readers(NamedTuple):
    """What a signature needs to know about an Event, as functions, so a planted test can stand in
    for a World. `cause_verb` is the verb of the act that caused the Event, or `None` when no act did.
    `attacker_side` is `A`, `R` or `O` (a foreign faction) for a march and `None` otherwise or when it cannot be told.
    `victim_held` is true when the person the Event reports dead held a live `detain` tenure at its tick."""
    cause_verb: Callable
    attacker_side: Callable
    victim_held: Callable = staticmethod(lambda e: False)


def governors(w, rung: Optional[str]) -> list:
    """Factions governing `rung`, nearest first and without repeats: the faction of the live `hold`
    on each rung from `rung` up to the root (`ancestry` includes `rung` itself)."""
    out: list = []
    for cur in ancestry(w, rung) if rung is not None else ():
        t = hold_force(w, cur)
        f = faction_holding(w, t.subject) if t is not None else None
        if f is not None and f not in out:
            out.append(f)
    return out


def side_against(attacker: Optional[str], gov: list, foreign=()) -> Optional[str]:
    """`O` if `attacker` is a foreign faction; else `A` if it is the nearest governor or a governor above
    it, `R` if it governs nothing in `gov`, `None` when there is no governor or no attacker to compare."""
    if attacker is None:
        return None
    if attacker in foreign:
        return "O"
    if not gov:
        return None
    return "A" if attacker in gov else "R"


def readers_for(w) -> Readers:
    def cause_verb(e):
        a = causing_act(w, e)
        return a.verb if a is not None else None

    def attacker_side(e):
        a = causing_act(w, e)
        if a is None or a.verb != "march":
            return None
        rung = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
        return side_against(faction_of(w, a.actor), governors(w, rung), FOREIGN)

    def victim_held(e):
        victims = {c.subject for c in e.changes if c.field == "exists"}
        return any(t.kind == DETAIN_KIND and t.subject in victims and t.since <= e.emitted_at
                   and (t.until is None or t.until >= e.emitted_at) for t in w.tenures)

    return Readers(cause_verb, attacker_side, victim_held)


def classify(e, rd: Readers, signatures=SIGNATURES) -> list:
    """The codes `e` matches, as `(code, side)`; `side` is the march's `A`/`R` or `None`."""
    out = []
    verb = side = None
    seen = False
    for g in signatures:
        if g["kind"] != e.kind:
            continue
        if not seen:
            verb, side, seen = rd.cause_verb(e), rd.attacker_side(e), True
        cv = g.get("cause_verb")
        if cv == "none" and verb is not None:
            continue
        if cv not in (None, "none") and verb != cv:
            continue
        if "attacker" in g and side != g["attacker"]:
            continue
        if "victim_held" in g and bool(rd.victim_held(e)) != g["victim_held"]:
            continue
        out.append((g["code"], side))
    return out


def route(row: dict, resolvable=None) -> list:
    """Static routes for a row: `(verb, kinds)` for each verb the loop can resolve whose row emits a
    kind the code names. Empty means a condition of possibility is missing."""
    ok = resolvable_verbs() if resolvable is None else resolvable
    out = []
    for v in row["verbs"]:
        if v in ok:
            ks = sorted(set(VERB_TABLE[v].emits) & set(row["kinds"]))
            if ks:
                out.append((v, ks))
    return out


def grade(row: dict, seen: Counter, act: Counter, has_sig: bool) -> tuple:
    """`(status, count)` for one row. See the module docstring for the five cases."""
    if has_sig:
        n = sum(v for (c, _), v in act.items() if c == row["code"])
        return ("OBSERVED" if n else "UNOBSERVED"), n
    if not row["kinds"]:
        return "GAP", 0
    if row.get("dark"):
        return "DARK", 0
    n = sum(seen[k] for k in row["kinds"])
    if row.get("needs"):
        return "KIND-ONLY", n
    return ("OBSERVED" if n else "UNOBSERVED"), n


def terminal_codes(rows) -> frozenset:
    """Codes a case can END on: `ends > 0` and `terminal` not false (XP is the study's mark of later linked trouble)."""
    return frozenset(r["code"] for r in rows if r.get("ends", 0) > 0 and r.get("terminal", True))


def routeless_terminals(rows, resolvable=None) -> list:
    """Terminal codes with no static route, in file order. Master section 7 wants a conclusion route per terminal
    code; until strands exist (S3) the check is per terminal code, not per opening-to-conclusion pair."""
    term = terminal_codes(rows)
    return [r["code"] for r in rows if r["code"] in term and not route(r, resolvable)]


def count_event(e, rd: Readers, seen: Counter, act: Counter, residue: Counter, signatures=SIGNATURES) -> None:
    """Count one Event once: `seen` by kind; `act` by each signature it matches; and, when its kind is named by
    some signature but it matched none, `residue` by `(kind, cause_verb, side)`. The signatures for one kind are
    mutually exclusive, so an Event lands in `act` or `residue`, never both (a test holds that)."""
    seen[e.kind] += 1
    hits = classify(e, rd, signatures)
    for hit in hits:
        act[hit] += 1
    if not hits and any(g["kind"] == e.kind for g in signatures):
        residue[(e.kind, rd.cause_verb(e), rd.attacker_side(e))] += 1


def measure(seasons: int, seeds: tuple) -> dict:
    """Run each seed through the owner (`populated.run`), classify its log, and pool the counts."""
    seen, act, residue = Counter(), Counter(), Counter()
    for s in seeds:
        w = populated.build_realm(s)
        populated.run(seasons, s, w=w)
        rd = readers_for(w)
        for e in w.log:
            count_event(e, rd, seen, act, residue)
    sig_codes = {g["code"] for g in SIGNATURES}
    rows = []
    for r in MOVES:
        st, n = grade(r, seen, act, r["code"] in sig_codes)
        rows.append((r, st, n, route(r)))
    return {"seasons": seasons, "seeds": tuple(seeds), "seen": seen, "act": act, "residue": residue, "rows": rows}


def report(m: dict) -> str:
    out = [f"strife moves: {len(m['rows'])} codes, {m['seasons']} seasons, seeds {list(m['seeds'])}", ""]
    tally = Counter(st for _, st, _, _ in m["rows"])
    out.append("  ".join(f"{k} {tally[k]}" for k in ("OBSERVED", "UNOBSERVED", "KIND-ONLY", "DARK", "GAP")))
    out.append("")
    out.append(f"{'code':<4} {'move':<24} {'status':<11} {'n':>6}  {'A':>4} {'R':>4}  {'ends':>4}  route")
    for r, st, n, rt in m["rows"]:
        a = m["act"].get((r["code"], "A"), 0)
        rr = m["act"].get((r["code"], "R"), 0)
        rtxt = ", ".join(v for v, _ in rt) if rt else "NONE"
        ends = r.get("ends", 0) if r.get("terminal", True) else 0
        out.append(f"{r['code']:<4} {r['name']:<24} {st:<11} {n:>6}  {a:>4} {rr:>4}  {ends:>4}  {rtxt}")
    out.append("")
    out.append("No verb route (a condition of possibility is missing):")
    for r, st, n, rt in m["rows"]:
        if not rt:
            why = r.get("gap") or r.get("dark") or "kinds come from matter or the gate, not a verb"
            out.append(f"  {r['code']:<3} {r['name']:<22} {why}")
    term = terminal_codes(r for r, _, _, _ in m["rows"])
    bare = [r["code"] for r, _, _, rt in m["rows"] if r["code"] in term and not rt]
    out.append("")
    out.append(f"Terminal codes with no static route ({len(bare)} of {len(term)}): " + (", ".join(bare) or "none"))
    out.append("")
    out.append("Residue: Events of a kind some signature names that matched NO signature, by (kind, cause verb, side):")
    res = m.get("residue", Counter())
    for (kind, verb, side), n in sorted(res.items(), key=lambda kv: (-kv[1], str(kv[0]))):
        out.append(f"  {n:>5}  {kind:<16} cause={verb}  side={side}")
    if not res:
        out.append("  none")
    return "\n".join(out)


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if len(a) < 2:
        print("usage: python -m engine.season.harness.strife <seasons> <seed> [seed ...]")
        return 2
    seasons, seeds = int(a[0]), tuple(int(x) for x in a[1:])
    print(report(measure(seasons, seeds)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
