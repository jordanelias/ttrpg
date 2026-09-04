"""ARM 3 -- THE DEPTH-3 DEGREE TREE. At each decision point, four degrees; three deep.

HOW THE DEGREE IS SUPPLIED, AND WHY IT IS NOT A SECOND RESOLVER
---------------------------------------------------------------
`_fold` hardcodes `_degree_for_writes = None` (shape.py:4447) because H-98 has not ruled the
bands. The sweep therefore FORCES the argument into the shape's own two readers -- `writes_at`
and `emits_at` -- and then calls the REAL `_fold`. Nothing is re-implemented (§8): the selection
rule stays in `writes_at`, the gate stays in `_apply_write`, the emission stays in `_fold`. The
ONLY thing the sweep contributes is the value of one parameter, which is what "the degree is
exogenous" means and is the whole basis of this instrument's honesty.

A FALSIFIER FOR THAT CLAIM, RUN IN 3d: forcing degree=None must reproduce today's behaviour
exactly. If it does not, the harness is perturbing something else and every number here is void.
"""
from __future__ import annotations
import copy, itertools
import sweep_core as K
from sweep_core import S, C, R, KW, LADDER_C, LADDER_D, Log

_REAL_W = S.VerbRow.writes_at
_REAL_E = S.VerbRow.emits_at


class force_degree:
    """Context manager: every CONTESTED verb row reads `deg`; uncontested rows are untouched."""
    def __init__(self, deg): self.deg = deg
    def __enter__(self):
        d = self.deg
        def w(self_row, degree, _d=d, _r=_REAL_W):
            return _r(self_row, _d if self_row.writes_by_degree else degree)
        def e(self_row, degree, _d=d, _r=_REAL_E):
            return _r(self_row, _d if self_row.emits_by_degree else degree)
        S.VerbRow.writes_at, S.VerbRow.emits_at = w, e
        return self
    def __exit__(self, *a):
        S.VerbRow.writes_at, S.VerbRow.emits_at = _REAL_W, _REAL_E
        return False


def world_fingerprint(w) -> str:
    """⚠ THE LEAF IDENTITY, AND `content_hash` CANNOT BE IT — THIS ARM ONCE USED IT AND THE
    RESULT WAS AN ARTIFACT. `_fold` (shape.py:4390-4515) contains NO `w.log.append`; the five
    append sites are :1985, :3973, :4010, :4173 and :4852, and the last is inside `season()`,
    which `fold_one` never calls. So `w.log` is EMPTY and unchanged across every fold here, and
    `content_hash` — which iterates `self.log` only (arm 4a) — is a CONSTANT. The published
    "distinct leaf worlds per case: {1: 89}" was therefore entailed by the harness, not measured:
    this arm was committing in its own leaf metric the exact defect it discovers in arm 4a.
    Found by the adversarial pass. `moved` was false for every node including the ones that
    delete a person, for the same reason."""
    import hashlib
    h = hashlib.blake2b(digest_size=16)
    for pid, pr in sorted(w.persons.items()):
        h.update(f"P|{pid}|{getattr(pr,'body',None)}|{getattr(pr,'exists',None)}".encode())
    for t in sorted(getattr(w, "tenures", []) or [],
                    key=lambda t: (str(t.kind), str(t.subject), str(t.object))):
        h.update(f"T|{t.kind}|{t.subject}|{t.object}|{t.until}".encode())
    h.update(f"L|{len(w.log)}".encode())
    return h.hexdigest()


def snap(w) -> dict:
    """The observable state a degree could move. Read-only; mints nothing."""
    return dict(hash=world_fingerprint(w), log_hash=w.content_hash(), log=len(w.log),
                bodies={p: getattr(pr, "body", None) for p, pr in sorted(w.persons.items())},
                exists={p: getattr(pr, "exists", None) for p, pr in sorted(w.persons.items())})


def fold_one(w, d, deg, aid: str, actor: str, target: str) -> dict:
    """ONE decision point: fold one contested act at one injected degree. Returns the node."""
    act = S.Act(id=aid, actor=actor, verb=KW, payload={"subject": target})
    # ⚠ THE STEP MUST BE RESOLVE, AND THE FIRST DRAFT OF THIS HARNESS DID NOT SET IT.
    # `_fold` runs inside RESOLVE in a real season; called bare, `w.step` is unset and the write
    # gate refuses `(Person, body)` with `[FORBIDDEN] ... written during -`. That refusal is the
    # HARNESS's defect, not a property of the design, and reporting it as a finding would have
    # been this sweep's own confounded measurement (§0.1 pt 1: attack the SETUP, not only the
    # statistics). Recorded rather than silently corrected.
    w.step = S.Step.RESOLVE
    before = snap(w)
    try:
        with force_degree(deg):
            evs = d._fold(w, act)
        after = snap(w)
        return dict(degree=deg, verdict="ADMITTED",
                    events=[e.kind for e in evs], n_events=len(evs),
                    before=before, after=after,
                    moved=before["hash"] != after["hash"],
                    # ⚠ `.get`, NOT `[...]`. The first draft indexed `after["bodies"][k]` and a
                    # `Felled`/`Wounded` fold DELETES the person, so the harness raised
                    # `KeyError: 'p_b'` and reported it as a REFUSAL by the design. It was the
                    # harness reading its own output wrong -- the second confounded setup this
                    # sweep caught in itself. A deleted person reads `<deleted>`, which is the
                    # observation that matters here.
                    survived=sorted(after["bodies"]),
                    died=sorted(set(before["bodies"]) - set(after["bodies"])),
                    body_delta={k: (before["bodies"][k], after["bodies"].get(k, "<deleted>"))
                                for k in before["bodies"]
                                if before["bodies"][k] != after["bodies"].get(k, "<deleted>")})
    except BaseException as ex:
        base = "Exception" if isinstance(ex, Exception) else "BaseException-ONLY"
        return dict(degree=deg, verdict="REFUSED", exc=type(ex).__name__, base=base,
                    detail=str(ex)[:160], events=[], n_events=0,
                    before=before, after=snap(w), moved=False, body_delta={},
                    survived=[], died=[])


def tree(case, ladder, depth: int, log: Log, seed: int = 0) -> dict:
    """Enumerate EVERY path of `ladder`^`depth`. One world per path, forked by deepcopy."""
    paths, leaves = [], {}
    reached_depth = 0
    for combo in itertools.product(ladder, repeat=depth):
        w = C.build_at(case, seed)
        d = S.SeasonDriver(w)
        nodes, alive = [], True
        for i, deg in enumerate(combo):
            if not alive:
                nodes.append(dict(degree=deg, verdict="UNREACHABLE",
                                  why="a prefix node refused; this node is never evaluated"))
                continue
            n = fold_one(w, d, deg, f"kw{i}", "p_a", "p_b")
            nodes.append(n)
            if n["verdict"] == "REFUSED":
                alive = False
            else:
                reached_depth = max(reached_depth, i + 1)
        leaf = snap(w)["hash"] if alive else None   # world fingerprint, not content_hash
        paths.append(dict(path=list(combo), nodes=nodes, alive=alive, leaf=leaf))
        if leaf:
            leaves.setdefault(leaf, []).append(list(combo))
    n_alive = sum(1 for p in paths if p["alive"])
    return dict(case=case["id"], ladder=list(ladder), depth=depth,
                n_paths=len(paths), n_alive=n_alive,
                n_unreachable=len(paths) - n_alive,
                reached_depth=reached_depth,
                distinct_leaves=len(leaves),
                leaves={k: v for k, v in leaves.items()}, paths=paths)
