"""`harness.soak` — THE MULTI-SEASON RUN ON THE POPULATED REALM (Jordan's original ask).

A SOAK run drives the unmodified season loop for many consecutive seasons on ONE World and ONE
SeasonDriver, and records what only duration exposes: an uncaught exception, memory or wall-clock
growth, and churn that degenerates. It pins nothing and is wired into no gate
(`harness/aperture.py`'s own disclaimer, `:48`, repeated here because it applies unchanged). It
decides nothing either -- true of this harness too, but that clause is added here, not quoted from
aperture.py, which does not carry it. It grades exactly TWO things, both over a finished run's
per-season series (`grade_cost`, `grade_mix`, below): that the cost of a season stays flat, and
that the mix of acts settles into a stable, non-collapsed shape.

Entry point: `python -m engine.season.harness.soak --seed S --arm ARM --batches B
--seasons-per-batch N --season-wall-ceiling SECONDS --out DIR [--cost-growth-ceiling X]
[--mix-drift-ceiling X] [--mix-top-share-ceiling X]`. Every argument is caller-supplied and none
has a default — this module sits under `engine/`, inside the blocking scope of
`tools/ci_sim_fabrication_check.py`, and an uncited literal default here is exactly the uncited
mechanical value that gate exists to refuse. The first five are required. A grade's ceilings are
optional ONLY in the sense that omitting them omits the grade: the run still prints that grade's
measured readings and reports it `UNGRADED`, naming the missing flag, rather than inventing a
threshold. A `FAIL` makes the exit status 1.

WHAT THIS IS NOT. It is not a second `populated.run` — that owner is untouched, imported and
reused for its construction (`build_realm`, `make_chooser`, `SeasonDriver`, `resolvable_verbs`,
`H`, `draw_factory`). This module only keeps ONE driver alive across many seasons, where every
existing caller builds a fresh one, and records what crosses its path along the way. It is not a
second `corpus_run`/`run_cases`: those still own PLAYABLE/DEGRADED/BLOCKED and R1/R3/R4/R5; the two
grades here are about duration alone and read only the rows this harness itself wrote.

WHERE THE OUTPUT GOES, AND WHY NOT `engine/season/runs/`. That tree is `harness/report.py`'s
alone (`data/files.py`'s own header: *"`runs/` is written by `harness/report.py` alone"*), and the
package derives every path it owns in `data/files.py`. A soak run's logs are large, run-scoped and
regenerable from `(HEAD, seed, arm, PYTHONHASHSEED, argv)`, so `--out` is a required argument and
must resolve OUTSIDE the repository (`C.8`) — checked against `data/files.REPO_ROOT`, the one
anchor the package already has.

WHAT IS FIX-WORTHY AND WHAT IS NOT (`C.6`). This harness wraps ONLY the `SeasonDriver.season(...)`
call. A `gaps.InstrumentDefect` means the call was malformed -- either the harness called the
engine wrong, OR the engine's own internal invariants raised it directly (e.g.
`loop/resolve.py`'s staged-delta/contiguous-Events checks, `state/gate.py`'s `NoToken`) -- the
whole run stops either way; the fix may be in this file OR in the engine, and the recorded
traceback/frame decide which. A `gaps.ShapeGap` (the design's own gap taxonomy) means the design is
reporting an unruled hole -- the WORLD stops, `end_reason: design_gap_escape`, and nothing is
filled in to make it go away (scripting drift, off the register). Anything else is a genuine code
defect and is fix-worthy at the raising site, in its own commit, never inside this harness.

ARCS ARE OUT OF SCOPE BY DECISION (`ED-IN-0225`, Jordan 2026-09-13: *"Maybe we just ignore the arcs
now"*). This module seats and reads the NPC lane only, exactly as `populated.build_realm` already
does, and mints no carrier, field, Event kind, write-matrix row, roster or register row for an arc,
a story, a thread or a plot. Nothing here is named for one either.
"""

from __future__ import annotations

import argparse
import json
import os
import resource
import statistics
import subprocess
import sys
import time
import traceback
from collections import Counter, defaultdict
from pathlib import Path

# Four of these five mirror lines `harness/populated.py` already imports for this exact
# composition; the fifth (`build_realm`/`census`) is imported FROM `populated.py` itself, which
# obviously does not import from itself.
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.ids import H, draw_factory
from . import probes as P
from .populated import build_realm, census
# `corpus_run.attribute` is the ONE owner of execution attribution -- `[(act, made, refused)]`,
# reused rather than re-derived from `emits`/`emits_on_refusal` a second time (CLAUDE.md §8,
# §0.06 S: "one rule and cannot drift into two ladders for one quantity"). `harness/aperture.py`
# is the existing second caller this module becomes the third of.
from .corpus_run import attribute
from ..state.carriers import subject_of
from ..gaps import ShapeGap, InstrumentDefect
from ..trace_log import TRACE
from ..data import files

ARMS = ("first", "all")


# ---------------------------------------------------------------------------------------------
# PRE-FLIGHT REFUSALS. Each raises with a clear message; none is wrapped, because a pre-flight
# refusal is not a season crash -- it means the harness was invoked wrong, before any world
# exists to end.
# ---------------------------------------------------------------------------------------------

def _require_pinned_hashseed() -> str:
    """`C.3`: cross-process determinism (the falsifier's check 6) depends on every process in a
    comparison pinning the SAME value, and a process that pins NONE is silently non-reproducible.
    Refuse rather than fall back to whatever the interpreter happened to start with."""
    v = os.environ.get("PYTHONHASHSEED")
    if v is None or not v.isdigit():
        raise RuntimeError(
            "PYTHONHASHSEED must be set to a decimal string before running the soak harness "
            f"(got {v!r}). Cross-process determinism is meaningless without a pinned value.")
    return v


def _require_out_dir(raw: str) -> Path:
    """`C.8`: `engine/season/runs/` is `harness/report.py`'s alone and the package derives every
    path it owns in `data/files.py`; a soak run's logs are neither. Refuse any `--out` that
    resolves inside the repository, checked against the package's own anchor rather than a new
    one (CLAUDE.md §8)."""
    out_dir = Path(raw).expanduser().resolve()
    repo_root = Path(files.REPO_ROOT).resolve()
    if out_dir == repo_root or repo_root in out_dir.parents:
        raise RuntimeError(
            f"--out must resolve OUTSIDE the repository root ({repo_root}); got {out_dir}. "
            "engine/season/runs/ belongs to harness/report.py alone, and CLAUDE.md forbids a "
            "new top-level tree for run output (C.8).")
    return out_dir


def _require_clean_engine() -> str:
    """Every run must be attributable to a commit. `git status --porcelain -- engine/` non-empty
    means the code this run exercises is not what `git rev-parse HEAD` names, so refuse rather
    than record a HEAD that does not describe what actually ran. Returns HEAD once confirmed."""
    repo_root = str(files.REPO_ROOT)
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "engine/"],
                           cwd=repo_root, capture_output=True, text=True, check=True).stdout
    if dirty.strip():
        raise RuntimeError(
            "engine/ is dirty; the soak harness refuses to start so every run stays "
            f"attributable to a commit:\n{dirty}")
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo_root,
                          capture_output=True, text=True, check=True).stdout.strip()


# ---------------------------------------------------------------------------------------------
# ROW BUILDERS. Pure functions over what `season()` and `attribute()` already hand back --
# nothing here re-derives a fact a reader already owns.
# ---------------------------------------------------------------------------------------------

def _occasion_row(d, a) -> dict | None:
    sc = d.scenes.get(a.scene) if a.scene else None
    q = getattr(sc, "occasion", None) if sc is not None else None
    if q is None:
        return None
    return {"id": q.id, "source": q.source, "referents": q.referents, "about": q.about}


def _act_row(seed: int, arm: str, batch: int, season: int, tick: int, a, new_ev: list, d,
            kind_of: dict, attr_by_id: dict) -> dict:
    made, refused = attr_by_id.get(a.id, ((), ()))
    payload = a.payload if isinstance(a.payload, dict) else {}
    operands = {k: v for k, v in payload.items() if k != "subject"}
    events = [{"id": e.id, "kind": e.kind, "degree": e.degree, "causes": list(e.causes)}
              for e in new_ev if d.act_of.get(e.id) is a]
    # `occasioned_by`: the FIRST act-Event's own `causes`, minus the act's own id -- the fold
    # already stamped its answer there (`[a.id] + self._occasion_ids(w, a)`, `loop/resolve.py`),
    # so this reads it rather than re-deriving it through `world_q.occasioned_by`, which would be
    # a second route to one fact and a full reverse log scan per call (CLAUDE.md §8).
    first_ev = next((e for e in new_ev if d.act_of.get(e.id) is a), None)
    occasioned_by = []
    if first_ev is not None:
        for cid in first_ev.causes:
            if cid == a.id:
                continue
            ant = d.act_of.get(cid)
            occasioned_by.append({
                "event_id": cid, "kind": kind_of.get(cid),
                "antecedent_act": ant.id if ant is not None else None,
                "antecedent_actor": ant.actor if ant is not None else None,
            })
    return {
        "seed": seed, "arm": arm, "batch": batch, "season": season, "tick": tick,
        "act_id": a.id, "actor": a.actor, "verb": a.verb, "subject": subject_of(a),
        "operands": operands, "via": a.via, "stratum": a.stratum, "scene": a.scene,
        "occasion": _occasion_row(d, a), "made": list(made), "refused": list(refused),
        "events": events, "occasioned_by": occasioned_by,
    }


def _canary_h156(new_acts: list, attr_by_id: dict) -> dict:
    """`H-156`, Jordan's live choice: an always-refused verb is logged, never acted on -- so this
    is a canary, not a test, and nothing here touches `resolvable_verbs()` or a verb's formation."""
    per_verb: dict = defaultdict(lambda: {"attempted": 0, "executed": 0, "refused": 0})
    for a in new_acts:
        made, no = attr_by_id.get(a.id, ((), ()))
        row = per_verb[a.verb]
        row["attempted"] += 1
        if made:
            row["executed"] += 1
        if no:
            row["refused"] += 1
    always_refused = sorted(v for v, r in per_verb.items()
                            if r["attempted"] > 0 and r["executed"] == 0)
    always_refused_acts = sum(per_verb[v]["attempted"] for v in always_refused)
    return {"per_verb": {v: dict(r) for v, r in per_verb.items()},
            "always_refused": always_refused,
            "always_refused_share": (always_refused_acts / len(new_acts)) if new_acts else 0.0}


def _tenure_row(t) -> tuple:
    return (t.id, t.kind, t.object)


def _claim_row(c) -> dict:
    return {"id": c.id, "holder": c.holder, "subject": c.subject, "predicate": c.predicate,
            "value": c.value, "when": c.when, "source": c.source, "confidence": c.confidence,
            "visibility": c.visibility, "round": c.round, "teller": c.teller,
            "chain": list(c.chain)}


def _person_row(p) -> dict:
    ledger = list(p.ledger)
    return {
        "id": p.id, "name": p.name, "weight": p.weight, "is_cohort": p.is_cohort,
        "body": p.body, "travel_leg": list(p.travel_leg), "stance": list(p.stance),
        "pursuits": dict(p.pursuits),
        "tenures": [_tenure_row(t) for t in p.tenures if t.live],
        "ledger_len": len(ledger),
        "ledger_by_source": dict(Counter(c.source for c in ledger)),
        "ledger_by_predicate_stem": dict(Counter(str(c.predicate).partition(":")[0]
                                                 for c in ledger)),
        "ledger": [_claim_row(c) for c in ledger],
    }


# ---------------------------------------------------------------------------------------------
# EXCEPTION / GAP RECORDING (`C.6`). One file, one shape, a `type` field distinguishing the three
# ways a season can end abnormally.
# ---------------------------------------------------------------------------------------------

def _innermost_season_frame(exc: BaseException) -> str | None:
    tb = traceback.extract_tb(exc.__traceback__)
    frames = [fr for fr in tb if "engine/season/" in fr.filename.replace(os.sep, "/")]
    if not frames:
        return None
    fr = frames[-1]
    return f"{fr.filename}:{fr.lineno}"


def _append_jsonl(path: Path, row: dict) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, default=str) + "\n")
        f.flush()


def _record_escape(exceptions_path: Path, escape_type: str, seed: int, arm: str, batch: int,
                   season: int, tick: int, round_: int, detail: dict) -> None:
    _append_jsonl(exceptions_path, {
        "type": escape_type, "seed": seed, "arm": arm, "batch": batch, "season": season,
        "tick": tick, "round": round_, **detail,
    })


# ---------------------------------------------------------------------------------------------
# ONE WORLD, MANY SEASONS.
# ---------------------------------------------------------------------------------------------

def _run_world(args: argparse.Namespace, head: str, world_dir: Path, argv: list) -> str:
    seed, arm = args.seed, args.arm

    # -- THE COMPOSITION, EXACTLY `populated.run`'s (`C.1`) -----------------------------------
    # NOT a call to `populated.run`, because that owner builds a NEW `SeasonDriver` every call
    # (`.resolved`/`.scenes`/`.act_of` would reset every batch, and R3 depends on them crossing
    # seasons). One driver, kept alive across every batch; `season()` resets its own
    # season-local state on its own.
    w = build_realm(seed)                                                  # cap=None: the full realm
    w.fixtures = w.fixtures.sweep("question_aggregation_rule", arm)        # BEFORE the chooser
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))

    pre_census = census(w)
    world_meta = {
        "git_head": head, "argv": list(argv), "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED"),
        "python_version": sys.version, "seed": seed, "arm": arm,
        "batches": args.batches, "seasons_per_batch": args.seasons_per_batch,
        "season_wall_ceiling": args.season_wall_ceiling, "out": str(world_dir),
        "fixtures": {k: w.fixtures.get(k) for k in
                     ("question_aggregation_rule", "scene_budget", "observation_deposit_mode",
                      "fan_out_mode", "field_casualty_model", "contest_max_depth")},
        "census_before": pre_census,
        # `resolved_len` is `None`, not `0`, before any season has run: a run killed before
        # season 0 completes must not read as "zero acts happened", which would be a real
        # (if degenerate) result rather than the absence of one.
        "start_time": time.time(), "end_time": None, "resolved_len": None, "end_reason": None,
    }
    world_json = world_dir / "WORLD.json"
    world_json.write_text(json.dumps(world_meta, indent=2, default=str))

    # `C.4`, applied to the BUILD too: `build_realm`/`census`/`SeasonDriver.__init__` all write
    # `TRACE` rows before the first season ever runs. Clearing here (not just after each season)
    # keeps season 0's `trace_counts`/`gaps_by_kind` about season 0 alone.
    TRACE.rows.clear()
    TRACE.gaps.clear()

    acts_path = world_dir / "acts.jsonl"
    seasons_path = world_dir / "seasons.jsonl"
    exceptions_path = world_dir / "EXCEPTIONS.jsonl"

    kind_of: dict = {}
    season_hashes: list = []
    end_reason = "completed"
    stopped = False

    for b in range(args.batches):
        # ⚠ NO `if stopped: break` HERE (methodology-close Phase 1, 2026-09-30): `stopped` can only
        # become True inside the inner season loop below, and every site that sets it also
        # unconditionally `break`s the outer loop right there (see the unconditional `if stopped:
        # break` after the inner loop) -- so control can never return to the top of this loop with
        # `stopped` already True. A check here was dead code; removed rather than kept for
        # symmetry.
        for s in range(args.seasons_per_batch):
            n_log0 = len(w.log)
            n_res0 = len(d.resolved)
            alive0 = set(w.persons)
            stance0 = {pid: tuple(p.stance) for pid, p in w.persons.items()}
            tick_before = w.tick
            t0 = time.time()

            # `C.6`: the harness wraps ONLY this call. It catches, records, ends this world.
            # Never continues past an exception, never retries, never adds a `try` inside the
            # engine itself.
            try:
                season_out = d.season(ch, question=None, subsistence=P.SUBSIST,
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))
            except InstrumentDefect as exc:
                # `InstrumentDefect` is NOT a `ShapeGap` (`gaps.py`) and is caught first -- but it
                # is not always THIS file's bug: the engine raises it directly from its own
                # internal invariants too (`loop/resolve.py`'s staged-delta/contiguous-Events
                # checks, `state/gate.py`'s `NoToken`). Record the same traceback/frame/hashes a
                # crash gets, so a reader can tell which it was without re-running.
                _record_escape(exceptions_path, "instrument_defect", seed, arm, b, s, w.tick,
                              d.round, {"exception_class": type(exc).__name__,
                                       "message": str(exc),
                                       "traceback": traceback.format_exc(),
                                       "frame": _innermost_season_frame(exc),
                                       "season_hashes": list(season_hashes)})
                end_reason, stopped = "instrument_defect", True
                break
            except ShapeGap as exc:
                _record_escape(exceptions_path, "design_gap_escape", seed, arm, b, s, w.tick,
                              d.round, {"exception_class": type(exc).__name__,
                                       "kind": exc.kind, "what": exc.what, "where": exc.where,
                                       "needs": exc.needs, "law": exc.law,
                                       "traceback": traceback.format_exc(),
                                       "frame": _innermost_season_frame(exc),
                                       "season_hashes": list(season_hashes)})
                end_reason, stopped = "design_gap_escape", True
                break
            except Exception as exc:                                     # noqa: BLE001 -- C.6.1
                _record_escape(exceptions_path, "crash", seed, arm, b, s, w.tick, d.round, {
                    "exception_class": type(exc).__name__, "message": str(exc),
                    "traceback": traceback.format_exc(),
                    "frame": _innermost_season_frame(exc),
                    "season_hashes": list(season_hashes),
                })
                end_reason, stopped = "crash", True
                break

            wall_s = time.time() - t0
            new_ev = list(w.log[n_log0:])
            new_acts = d.resolved[n_res0:]
            for e in new_ev:
                kind_of[e.id] = e.kind

            # `attribute(w, d, w.tick)` is the whole history every time (it is the design's
            # single owner of execution attribution, and it takes the world and driver, not a
            # slice); restricted to THIS season's acts by id lookup below, as `C.1`/`C.5` direct.
            attr_by_id = {act.id: (made, no) for act, made, no in attribute(w, d, w.tick)}

            for a in new_acts:
                _append_jsonl(acts_path, _act_row(seed, arm, b, s, tick_before, a, new_ev, d,
                                                  kind_of, attr_by_id))

            persons_removed = sorted(alive0 - set(w.persons))
            stance_moved = [(pid, len(stance0.get(pid, ())), len(p.stance))
                            for pid, p in w.persons.items()
                            if pid in stance0 and tuple(p.stance) != stance0[pid]]
            event_kinds = Counter(e.kind for e in new_ev)
            gaps_by_kind = Counter((g["kind"], g["expected"]) for g in TRACE.gaps)
            season_row = {
                "seed": seed, "arm": arm, "batch": b, "season": s,
                "tick_before": tick_before, "tick_after": w.tick, "wall_s": wall_s,
                "acts": season_out["acts"], "events": season_out["events"],
                "rounds": season_out["rounds"], "deposits": season_out["deposits"],
                "hash": season_out["hash"],
                "log_len": len(w.log), "acts_store_len": len(w.acts),
                "resolved_len": len(d.resolved),
                "persons_alive": len(w.persons), "persons_removed": persons_removed,
                "event_kinds": dict(event_kinds),
                "canary_h112": event_kinds.get("claim.deposited", 0),
                "canary_h156": _canary_h156(new_acts, attr_by_id),
                "trace_counts": TRACE.counts(),
                "gaps_by_kind": [{"kind": k, "expected": exp, "count": n}
                                for (k, exp), n in gaps_by_kind.items()],
                "stance_moved": stance_moved,
                # [JUSTIFIED: KB -> MB, a unit conversion of `ru_maxrss` and not a game value]
                "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024,
            }
            _append_jsonl(seasons_path, season_row)
            # ⚠ `batch` CARRIED HERE TOO, NOT JUST `season`. Every other row in this file keys on
            # (batch, season) because `season` alone repeats across batches (0..seasons_per_batch-1
            # each time) -- a `season_hashes` entry keyed on `season` alone would collide across
            # batches for batch >= 1. Found by the WD-REBASE^ soak critic pass, 2026-09-30.
            season_hashes.append({"batch": b, "season": s, "hash": season_out["hash"]})

            # `C.4`: clear AFTER this season's records are built, never before, and never a
            # reassignment -- `.clear()` only, so no caller holding a reference to `TRACE.rows`
            # sees it silently replaced.
            TRACE.rows.clear()
            TRACE.gaps.clear()

            if wall_s > args.season_wall_ceiling:
                end_reason, stopped = "wall_ceiling", True
                break
            if not w.persons:
                end_reason, stopped = "extinct", True
                break

        # `C.5(c)`: at each batch end (including a batch cut short by a stop above), one row
        # per surviving person.
        persons_path = world_dir / f"persons_b{b}.jsonl"
        for pid in sorted(w.persons):
            _append_jsonl(persons_path, _person_row(w.persons[pid]))

        if stopped:
            break

    world_meta["end_time"] = time.time()
    world_meta["resolved_len"] = len(d.resolved)
    world_meta["end_reason"] = end_reason
    world_json.write_text(json.dumps(world_meta, indent=2, default=str))
    return end_reason


# ---------------------------------------------------------------------------------------------
# THE GRADES. Pure functions over plain data (a list of per-season costs; a list of per-season
# `{verb: count}` mixes) so a test can plant on them. Every ceiling is an ARGUMENT: nothing here
# invents a threshold, and the only literals are structural (halving, the empty case).
#
# Both grades compare blocks of seasons taken from the END of the series, never one season against
# another, because a single season is noise (a wall-clock reading, one realm's draw). Blocks are
# built by halving only: `half = n // 2` for the cost grade, `block = half // 2` for the mix grade.
# ---------------------------------------------------------------------------------------------

def grade_cost(costs: list, growth_ceiling: float) -> dict:
    """Flat cost per season: the median cost of the LATER half of the run over the median cost of
    the EARLIER half is at most `growth_ceiling`. Medians, not means, so one stalled season does
    not read as growth. A cost that grew 13 s -> 169 s (the proposal's own observation) puts the
    later median far above the earlier one; a cost that rose and then plateaued inside the first
    half still passes, because the grade asks whether cost is STILL growing, not whether it ever
    did. `UNGRADED` below two seasons per half: a median of one season is the season itself."""
    n = len(costs)
    half = n // 2
    if half < 2:
        return {"grade": "UNGRADED", "why": f"{n} season(s); a half needs at least two",
                "seasons": n}
    early = statistics.median(costs[:half])
    late = statistics.median(costs[n - half:])
    # an earlier median of zero: any later cost at all is unbounded growth, none is flat
    ratio = (late / early) if early > 0 else (float("inf") if late > 0 else 1.0)
    return {"grade": "PASS" if ratio <= growth_ceiling else "FAIL", "seasons": n,
            "early_median": early, "late_median": late, "ratio": ratio,
            "growth_ceiling": growth_ceiling}


def _tv_distance(p: dict, q: dict) -> float:
    """Total-variation distance between two `{verb: count}` mixes read as shares (0 = identical
    shape, 1 = disjoint). An empty mix against a non-empty one is maximally distant."""
    tp, tq = sum(p.values()), sum(q.values())
    if tp == 0 and tq == 0:
        return 0.0
    if tp == 0 or tq == 0:
        return 1.0
    return 0.5 * sum(abs(p.get(v, 0) / tp - q.get(v, 0) / tq) for v in set(p) | set(q))


def grade_mix(mixes: list, drift_ceiling: float, top_share_ceiling: float) -> dict:
    """Convergence of the act mix ("season 40 resembles season 30"): the pooled mix of the last
    block of seasons against the block before it (the final two quarters of the run) must

      * DRIFT by at most `drift_ceiling` (total-variation distance; the mix has settled), and
      * not be COLLAPSED: no single verb's share of the last block may exceed `top_share_ceiling`.

    The second condition is not decoration. A mix that has collapsed onto one act drifts by
    exactly zero, so a drift test alone passes the worst case; convergence here means settling
    into a SHAPE, not merely holding still. An empty last block fails (a run that stopped acting
    has not converged on anything). `UNGRADED` below four seasons (a block needs one season)."""
    n = len(mixes)
    block = (n // 2) // 2
    if block < 1:
        return {"grade": "UNGRADED", "why": f"{n} season(s); two blocks need at least four",
                "seasons": n}
    prev, last = Counter(), Counter()
    for m in mixes[n - 2 * block:n - block]:
        prev.update(m)
    for m in mixes[n - block:]:
        last.update(m)
    total = sum(last.values())
    top_verb, top_n = (last.most_common(1)[0] if total else (None, 0))
    top_share = (top_n / total) if total else 1.0
    drift = _tv_distance(prev, last)
    reasons = []
    if total == 0:
        reasons.append("no acts in the last block")
    if drift > drift_ceiling:
        reasons.append(f"drift {drift:.3f} over {drift_ceiling}")
    if total and top_share > top_share_ceiling:
        reasons.append(f"collapsed onto {top_verb!r}: share {top_share:.3f} over "
                       f"{top_share_ceiling}")
    return {"grade": "FAIL" if reasons else "PASS", "seasons": n, "block": block,
            "drift": drift, "drift_ceiling": drift_ceiling, "top_verb": top_verb,
            "top_share": top_share, "top_share_ceiling": top_share_ceiling,
            "distinct_verbs_last": len(last), "reasons": reasons}


def load_series(world_dir: Path) -> tuple:
    """`(costs, mixes)` for a finished world: one entry per completed season, in run order, read
    from the `seasons.jsonl` and `acts.jsonl` this harness wrote (so the grades apply to a prior
    run's directory as well as to a fresh one)."""
    seasons_path = world_dir / "seasons.jsonl"
    seasons = ([json.loads(line) for line in
                seasons_path.read_text(encoding="utf-8").splitlines() if line]
               if seasons_path.exists() else [])         # a run killed in season 0 wrote none
    mix_by: dict = defaultdict(Counter)
    acts_path = world_dir / "acts.jsonl"
    if acts_path.exists():
        for line in acts_path.read_text(encoding="utf-8").splitlines():
            if line:
                r = json.loads(line)
                mix_by[(r["batch"], r["season"])][r["verb"]] += 1
    costs = [s["wall_s"] for s in seasons]
    mixes = [dict(mix_by.get((s["batch"], s["season"]), {})) for s in seasons]
    return costs, mixes


def grade_run(world_dir: Path, args: argparse.Namespace) -> tuple:
    """Print the per-season cost and act-mix readings and the two grades for `world_dir`; return
    `(cost_grade, mix_grade, lines)`. A grade whose ceiling flag was not supplied is `UNGRADED`
    and names the flag, and still prints what it measured."""
    costs, mixes = load_series(world_dir)
    lines = []
    for i, (c, m) in enumerate(zip(costs, mixes)):
        tot = sum(m.values())
        top = max(m.items(), key=lambda kv: kv[1]) if m else (None, 0)
        lines.append(f"  season {i}: wall_s={c:.3f} acts={tot} distinct_verbs={len(m)} "
                     f"top_verb={top[0]} top_share={(top[1] / tot) if tot else 0.0:.3f}")

    if args.cost_growth_ceiling is None:
        cost = {"grade": "UNGRADED", "why": "--cost-growth-ceiling not supplied"}
    else:
        cost = grade_cost(costs, args.cost_growth_ceiling)
    missing = [f for f, v in (("--mix-drift-ceiling", args.mix_drift_ceiling),
                              ("--mix-top-share-ceiling", args.mix_top_share_ceiling))
               if v is None]
    if missing:
        mix = {"grade": "UNGRADED", "why": f"{', '.join(missing)} not supplied"}
    else:
        mix = grade_mix(mixes, args.mix_drift_ceiling, args.mix_top_share_ceiling)
    lines.append(f"soak grade cost: {_fmt_grade(cost)}")
    lines.append(f"soak grade act-mix convergence: {_fmt_grade(mix)}")
    return cost, mix, lines


def _fmt_grade(g: dict) -> str:
    return g["grade"] + "".join(f" {k}={v:.3f}" if isinstance(v, float) else f" {k}={v}"
                                for k, v in g.items() if k != "grade")


# ---------------------------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------------------------

def _parse_args(argv) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--arm", choices=ARMS, required=True)
    ap.add_argument("--batches", type=int, required=True)
    ap.add_argument("--seasons-per-batch", type=int, required=True)
    ap.add_argument("--season-wall-ceiling", type=float, required=True,
                    help="seconds; a completed season over this stops the world cleanly "
                         "(end_reason: wall_ceiling) -- a harness parameter, not an engine "
                         "fixture")
    ap.add_argument("--out", type=str, required=True,
                    help="must resolve OUTSIDE the repository root")
    # The grades' ceilings. No defaults (a default is an invented value): omitting one omits its
    # grade, which then reads UNGRADED.
    ap.add_argument("--cost-growth-ceiling", type=float, default=None,
                    help="grade_cost: largest allowed (later-half median season wall time) / "
                         "(earlier-half median); omitted = cost UNGRADED")
    ap.add_argument("--mix-drift-ceiling", type=float, default=None,
                    help="grade_mix: largest allowed total-variation distance between the last "
                         "two blocks' act-verb mixes; omitted = mix UNGRADED")
    ap.add_argument("--mix-top-share-ceiling", type=float, default=None,
                    help="grade_mix: largest allowed share of the last block held by one verb "
                         "(a single-act mix fails); omitted = mix UNGRADED")
    return ap.parse_args(argv)


def _require_fresh_world_dir(world_dir: Path) -> None:
    """`C.8`/`C.6.1` step 3: every `*.jsonl` here is opened in APPEND mode and `WORLD.json` is
    overwritten, never the reverse, so re-running into a world directory that already holds rows
    silently mixes two runs' data with no run id to tell them apart afterward -- exactly the
    "restart from season 0" path `C.6` calls for after an `instrument_defect`. Refuse rather than
    silently append. A caller that means to restart removes or renames the old directory first."""
    if world_dir.exists() and any(world_dir.iterdir()):
        raise RuntimeError(
            f"{world_dir} already exists and is non-empty. Every output file here is appended "
            "to, never truncated, so re-running into it would silently mix two runs' rows with "
            "no run id to separate them. Move it aside or delete it first, then re-run.")


def main(argv=None) -> int:
    used_argv = list(argv) if argv is not None else list(sys.argv[1:])
    args = _parse_args(argv)

    _require_pinned_hashseed()
    out_dir = _require_out_dir(args.out)
    head = _require_clean_engine()

    world_dir = out_dir / f"seed{args.seed}_{args.arm}"
    _require_fresh_world_dir(world_dir)
    world_dir.mkdir(parents=True, exist_ok=True)

    end_reason = _run_world(args, head, world_dir, used_argv)
    print(f"soak seed={args.seed} arm={args.arm} batches={args.batches} "
          f"seasons_per_batch={args.seasons_per_batch} end_reason={end_reason} out={world_dir}")
    cost, mix, lines = grade_run(world_dir, args)
    print("\n".join(lines))
    return 1 if "FAIL" in (cost["grade"], mix["grade"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
