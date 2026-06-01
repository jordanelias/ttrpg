"""Tests for resumable_runner.run_resumable — the resumable MC batch runner.

Covers all directions that matter for resumability:
  - basic completion + aggregation
  - resume across calls == uninterrupted run (determinism guarantee)
  - hard-kill survival: flushed seeds persist; the in-flight seed re-runs on resume
  - idempotent 'done' (no re-run)
  - stale checkpoint (changed n) restarts instead of resuming wrong
  - budget forces clean 'in_progress' and forward progress

Hermetic: each test uses its own tempdir scratch. No network, no Valoria deps.
"""
import os
import sys
import random
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/claude")  # fallback for ad-hoc container runs
sys.path.insert(0, os.path.join(_HERE, "..", "..", "skills", "valoria-orchestrator", "scripts"))  # repo (authoritative)
import resumable_runner  # noqa: E402


def _sd():
    return tempfile.mkdtemp(prefix="simrun_test_")


def test_basic_completion_and_summary():
    sd = _sd()
    out = resumable_runner.run_resumable(
        "basic", 10, run_one=lambda s: {"seed": s, "v": s * s},
        reduce_fn=lambda rs: sum(r["v"] for r in rs),
        scratch_dir=sd, verbose=False)
    assert out["status"] == "done"
    assert out["completed"] == 10 and out["total"] == 10
    assert [r["seed"] for r in out["results"]] == list(range(10))  # seed order preserved
    assert out["summary"] == sum(s * s for s in range(10)) == 285


def test_resume_equals_uninterrupted():
    sd = _sd()
    run_one = lambda s: {"seed": s, "r": random.Random(s).random()}
    full = resumable_runner.run_resumable("eq_full", 20, run_one, scratch_dir=sd, verbose=False)
    # Now run the same sweep in maximally-fragmented calls (1 seed per call).
    calls = 0
    while True:
        calls += 1
        out = resumable_runner.run_resumable("eq_resume", 20, run_one,
                                       scratch_dir=sd, max_seconds=0, verbose=False)
        if out["status"] == "done":
            break
        assert out["status"] == "in_progress"
        assert calls < 100, "resume loop did not converge (forward progress broken)"
    assert out["results"] == full["results"], "resumed run diverged from uninterrupted run"
    assert calls >= 20, "expected fragmented resume to take many calls"


def test_hard_kill_survival():
    sd = _sd()
    good = lambda s: {"seed": s, "v": s * 10}

    def crashing(s):
        if s == 5:
            raise RuntimeError("simulated wall-clock kill mid-seed")
        return good(s)

    # First invocation crashes at seed 5 (seeds 0-4 flushed because checkpoint_every=1).
    crashed = False
    try:
        resumable_runner.run_resumable("kill", 10, crashing, checkpoint_every=1,
                                 scratch_dir=sd, verbose=False)
    except RuntimeError:
        crashed = True
    assert crashed, "expected the crash to propagate"

    st = resumable_runner.status("kill", scratch_dir=sd)
    assert st is not None and st["completed"] == 5, f"flushed work lost: {st}"

    # Resume with a non-crashing run_one — must finish and reproduce a clean full run.
    out = resumable_runner.run_resumable("kill", 10, good, checkpoint_every=1,
                                   scratch_dir=sd, verbose=False)
    assert out["status"] == "done" and out["completed"] == 10
    assert out["results"] == [good(s) for s in range(10)], "resume produced wrong/duplicated results"


def test_idempotent_done():
    sd = _sd()
    seen = []
    run_one = lambda s: (seen.append(s) or {"seed": s})
    resumable_runner.run_resumable("idem", 5, run_one, scratch_dir=sd, verbose=False)
    assert seen == [0, 1, 2, 3, 4]
    seen.clear()
    out = resumable_runner.run_resumable("idem", 5, run_one, scratch_dir=sd, verbose=False)
    assert out["status"] == "done"
    assert seen == [], "re-calling a completed job must NOT re-run seeds"


def test_stale_checkpoint_restarts():
    sd = _sd()
    seen = []
    run_one = lambda s: (seen.append(s) or {"seed": s})
    resumable_runner.run_resumable("stale", 5, run_one, scratch_dir=sd, verbose=False)
    assert seen == [0, 1, 2, 3, 4]
    seen.clear()
    # Same job_id, different n -> different fingerprint -> must restart, not resume from 5.
    out = resumable_runner.run_resumable("stale", 8, run_one, scratch_dir=sd, verbose=False)
    assert out["status"] == "done" and out["completed"] == 8
    assert seen == [0, 1, 2, 3, 4, 5, 6, 7], "stale checkpoint was wrongly resumed"


def test_status_and_clear():
    sd = _sd()
    run_one = lambda s: {"seed": s}
    out = resumable_runner.run_resumable("sc", 10, run_one, max_seconds=0,
                                   scratch_dir=sd, verbose=False)
    assert out["status"] == "in_progress" and 0 < out["completed"] < 10
    st = resumable_runner.status("sc", scratch_dir=sd)
    assert st["status"] == "in_progress"
    assert resumable_runner.clear("sc", scratch_dir=sd) is True
    assert resumable_runner.status("sc", scratch_dir=sd) is None


def test_input_guards():
    sd = _sd()
    for bad in ["", "has space", "has/slash", 'has"quote']:
        try:
            resumable_runner.run_resumable(bad, 1, lambda s: {}, scratch_dir=sd, verbose=False)
            raise AssertionError(f"expected ValueError for job_id={bad!r}")
        except ValueError:
            pass


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\nALL {len(tests)} PASS")
