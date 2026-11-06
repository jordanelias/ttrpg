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

THE STRANDS BLOCK (CR-76, behind `--strands`; off, the report is byte-identical to the one before it). It reads
`world_q.flows_in` with this module's code-level terminal test (`terminal_for`: a kind with signatures is
terminal when a matched code is, any other kind when every code it maps to is), and prints strands per rung,
the eras and the opening kinds open beneath the last, conclusions, per strand whether an incompatible pair
spans its parties (A5), the opening-to-terminal route check (`opening_routes`), and each strand's code
sequence's adjacent pairs against a shuffled-order control. A reading, never a bar (V2).
NOT HERE, AND WHY: the study's 16 links themselves. No file in the tree lists them (only the study artifact
does), so the block prints the observed pairs against the control and names the 16 as not transcribed.

    python -m engine.season.harness.strife <seasons> <seed> [seed ...] [--strands]
"""
from __future__ import annotations

import sys
from collections import Counter
from typing import Callable, NamedTuple

from ..data.rosters import BAN_KIND, DETAIN_KIND
from ..data.verbs import VERB_TABLE
from ..loop.driver import resolvable_verbs
from ..queries import world_q
from ..state.attribution import causing_act
from . import populated
from .strife_data import MOVES, SIGNATURES


class Readers(NamedTuple):
    """What a signature needs to know about an Event, as functions, so a planted test can stand in
    for a World. `cause_verb` is the verb of the act that caused the Event, or `None` when no act did.
    `attacker_side` is `A`, `R` or `O` (a foreign faction) for a march and `None` otherwise or when it cannot be told.
    `victim_held` is true when the person the Event reports dead held a live `detain` tenure at its tick."""
    cause_verb: Callable
    attacker_side: Callable
    victim_held: Callable = staticmethod(lambda e: False)


def readers_for(w) -> Readers:
    def cause_verb(e):
        a = causing_act(w, e)
        return a.verb if a is not None else None

    def attacker_side(e):
        return world_q.march_side(w, causing_act(w, e))     # the side read's one owner (CR-76)

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


def opening_kinds() -> tuple:
    """The kinds a strand can open on in the world reading: `world_q.OPENING_KINDS`, their one list."""
    return world_q.OPENING_KINDS


def opening_producers(kind: str, resolvable=None) -> list:
    """Resolvable verbs whose row emits `kind`; for a death, only `world_q.OPENING_DEATH_VERBS` (the opener is a
    death by those)."""
    ok = resolvable_verbs() if resolvable is None else resolvable
    verbs = sorted(v for v in ok if v in VERB_TABLE and kind in VERB_TABLE[v].emits)
    if kind == world_q.OPENING_DEATH_KIND:
        verbs = [v for v in verbs if v in world_q.OPENING_DEATH_VERBS]
    return verbs


def opening_routes(rows, resolvable=None) -> dict:
    """THE ROUTE CHECK (`strife-00` §7, "a conclusion from every opening"; CR-76): for each opening kind and each
    terminal code, `(opening verbs, terminal verbs)` -- the resolvable verbs that produce the opening, and `route`'s
    verbs for the code. A pair with either side empty has NO ACT ROUTE: a defect in the loop, reported by name
    (`routeless_pairs`), never a state the design accepts. STATIC, AND ONLY THAT: whether a terminal verb can take a
    referent the opening touched (so the two moves would link) is not read; a pair here is the product of the two
    static facts."""
    ok = resolvable_verbs() if resolvable is None else resolvable      # asked of the fold once, not once per pair
    term = terminal_codes(rows)
    ends = {r["code"]: [v for v, _ in route(r, ok)] for r in rows if r["code"] in term}
    opening = {k: opening_producers(k, ok) for k in opening_kinds()}
    return {(k, c): (opening[k], ends[c]) for k in opening for c in sorted(ends)}


def routeless_pairs(routes: dict) -> list:
    """The `(opening kind, terminal code)` pairs of an `opening_routes` table with no act route, sorted."""
    return sorted(p for p, (o, t) in routes.items() if not o or not t)


_TERMINAL = terminal_codes(MOVES)
_KIND_CODES = {}
for _r in MOVES:
    for _k in _r["kinds"]:
        _KIND_CODES.setdefault(_k, set()).add(_r["code"])
del _r, _k
_SIG_KINDS = frozenset(g["kind"] for g in SIGNATURES)


def move_codes(e, rd: Readers) -> list:
    """A move's codes as the world reading knows them: its signature matches when its kind has signatures, else every
    code its kind maps to (one code only when the kind is unambiguous)."""
    if e.kind in _SIG_KINDS:
        return sorted({c for c, _ in classify(e, rd)})
    return sorted(_KIND_CODES.get(e.kind, ()))


def terminal_for(w) -> Callable:
    """`world_q.flows_in`'s terminal test at CODE level, `terminal(e, a)` with `a` the causing act `flows_in`
    already resolved: a kind with signatures is terminal when a code it matches is terminal (`terminal_codes`:
    `ends` above 0 and `terminal` not false), read through `a`'s verb and march side; any other kind when every
    code it maps to is (`world_q.CONCLUDING_KINDS`)."""
    held = readers_for(w).victim_held

    def terminal(e, a) -> bool:
        if e.kind in _SIG_KINDS:
            rd = Readers(lambda _: a.verb if a is not None else None, lambda _: world_q.march_side(w, a), held)
            return any(c in _TERMINAL for c, _ in classify(e, rd))
        return e.kind in world_q.CONCLUDING_KINDS
    return terminal


def _single_code_runs(seq) -> list:
    """`seq` (one strand's moves, each a list of its codes) split into RUNS of consecutive moves with exactly one code
    each, as code sequences: a move with no code or several breaks the run, so two codes either side of it are
    never read as adjacent."""
    runs, cur = [], []
    for codes in seq:
        if len(codes) == 1:
            cur.append(codes[0])
        else:
            runs.append(cur)
            cur = []
    runs.append(cur)
    return [r for r in runs if len(r) > 1]


def pair_profile(seqs, shuffles: int = 200, seed: int = 0) -> list:
    """Adjacent code pairs over each strand's moves (`seqs`: per strand, each move's list of codes), paired only
    within a run of single-code moves (`_single_code_runs`), against a SHUFFLED-ORDER CONTROL (each run's order
    permuted `shuffles` times with a seeded `random.Random`): `[(pair, observed, control mean), ...]`, most observed
    first. A pair above its control is one the order produces, not the mix of codes."""
    import random
    rng = random.Random(seed)
    obs, ctl = Counter(), Counter()
    for s in (run for seq in seqs for run in _single_code_runs(seq)):
        obs.update(zip(s, s[1:]))
        for _ in range(shuffles):
            t = list(s)
            rng.shuffle(t)
            ctl.update(zip(t, t[1:]))
    return [(p, n, ctl[p] / shuffles) for p, n in sorted(obs.items(), key=lambda kv: (-kv[1], kv[0]))]


def strands_block(w, seed: int, resolvable=None) -> list:
    """The shipped-realm reading of CR-76 for one world. Prints; writes nothing; a reading, never a bar (V2)."""
    rd = readers_for(w)
    fl = world_q.flows_in(w, terminal_for(w))
    log_ix = {e.id: e for e in w.log}
    codes = {m.event: move_codes(log_ix[m.event], rd) for s in fl.strands for m in s.moves}
    done = {s.id: world_q.concluded(w, s) for s in fl.strands}
    out = [f"STRANDS (seed {seed}): {len(fl.strands)} strands, {len(fl.eras)} era(s)"]
    by_kind = Counter((w.rungs[s.rung].kind if s.rung in w.rungs else None) for s in fl.strands)
    out.append("  per rung kind: " + ", ".join(f"{k} {n}" for k, n in sorted(by_kind.items(), key=str)))
    out.append(f"  concluded {sum(done.values())} of {len(fl.strands)}")
    for era in fl.eras:
        inside = set(era.strands)
        cats = sorted({s.moves[0].kind for s in fl.strands if s.id in inside})
        out.append(f"  era {era.id}: {len(era.moves)} moves, {len(era.strands)} strands, "
                   f"{'concluded' if era.concluded else 'OPEN'}; opening kinds beneath: {', '.join(cats) or 'none'}")
    for s in fl.strands:
        kind = w.rungs[s.rung].kind if s.rung in w.rungs else None
        seq = "-".join("/".join(codes[m.event]) or "?" for m in s.moves)
        out.append(f"    {s.id[:12]:<12} {str(kind):<10} {s.rung or '-':<20} moves {len(s.moves):>3} "
                   f"opening {s.moves[0].kind:<18} {'concluded' if done[s.id] else 'open':<9} "
                   f"incompatible-span {world_q.incompatible_span(w, s)}  {seq[:60]}")
    arms = Counter(r[0] for s in fl.strands for r in world_q.open_referents(w, s.parties, s.referents))
    out.append("  open referents over the strands, by arm (an arm at 0 is vacuous in this world): "
               + ", ".join(f"{k} {arms[k]}" for k in (DETAIN_KIND, BAN_KIND, "at_war", "docketed")))
    slots, grouped = world_q.presented(w, fl)
    out.append(f"  presented: {sum(len(v) for v in slots.values())} in {len(slots)} rung(s); grouped {len(grouped)}")
    prof = pair_profile([[codes[m.event] for m in s.moves] for s in fl.strands])
    out.append("  adjacent code pairs in strands, observed against the shuffled-order control (top 10):")
    for p, n, c in prof[:10]:
        out.append(f"    {p[0]}->{p[1]}  observed {n:>3}  control {c:6.2f}")
    if not prof:
        out.append("    none (no strand holds two adjacent moves with one code each)")
    out.append("  the study's 16 links: NOT TRANSCRIBED (no file in the tree lists them); leave-and-rejoin unread")
    routes = opening_routes(MOVES, resolvable)
    bare = routeless_pairs(routes)
    out.append(f"  route check: {len(bare)} of {len(routes)} (opening kind, terminal code) "
               f"pairs have no act route")
    for k, c in bare:
        out.append(f"    NO ROUTE  {k:<20} -> {c}")
    return out


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


def measure(seasons: int, seeds: tuple, strands: bool = False) -> dict:
    """Run each seed through the owner (`populated.run`), classify its log, and pool the counts. `strands` adds the
    CR-76 reading per seed (`strands_block`); off, nothing about the report changes."""
    seen, act, residue = Counter(), Counter(), Counter()
    block: list = []
    for s in seeds:
        w = populated.build_realm(s)
        populated.run(seasons, s, w=w)
        rd = readers_for(w)
        for e in w.log:
            count_event(e, rd, seen, act, residue)
        if strands:
            block += strands_block(w, s)
    sig_codes = {g["code"] for g in SIGNATURES}
    rows = []
    for r in MOVES:
        st, n = grade(r, seen, act, r["code"] in sig_codes)
        rows.append((r, st, n, route(r)))
    m = {"seasons": seasons, "seeds": tuple(seeds), "seen": seen, "act": act, "residue": residue, "rows": rows}
    if strands:
        m["strands"] = block
    return m


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
    rows = [r for r, _, _, _ in m["rows"]]
    term, bare = terminal_codes(rows), routeless_terminals(rows)
    out.append("")
    out.append(f"Terminal codes with no static route ({len(bare)} of {len(term)}): " + (", ".join(bare) or "none"))
    out.append("")
    out.append("Residue: Events of a kind some signature names that matched NO signature, by (kind, cause verb, side):")
    res = m.get("residue", Counter())
    for (kind, verb, side), n in sorted(res.items(), key=lambda kv: (-kv[1], str(kv[0]))):
        out.append(f"  {n:>5}  {kind:<16} cause={verb}  side={side}")
    if not res:
        out.append("  none")
    if "strands" in m:
        out.append("")
        out.extend(m["strands"])
    return "\n".join(out)


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    strands = "--strands" in a
    a = [x for x in a if x != "--strands"]
    if len(a) < 2:
        print("usage: python -m engine.season.harness.strife <seasons> <seed> [seed ...] [--strands]")
        return 2
    seasons, seeds = int(a[0]), tuple(int(x) for x in a[1:])
    print(report(measure(seasons, seeds, strands)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
