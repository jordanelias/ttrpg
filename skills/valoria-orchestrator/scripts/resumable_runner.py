"""resumable_runner — resumable batch runner for Valoria Monte-Carlo seed sweeps.

WHY
---
Long seed sweeps overrun a single bash_tool wall-clock and the block is killed,
forfeiting all work (e.g. mc_v17 runs N=1000 campaigns). This runner checkpoints
per-seed results to local scratch and resumes, so a kill loses at most the seeds
since the last flush, and the caller drives the sweep across multiple blocks.

This is the *work-resumability* primitive that `h.write_checkpoint` is NOT:
write_checkpoint stores session-progress metadata to GitHub at the 60/75% context
bands; this stores partial batch results to local disk against the wall clock.

MODEL (matches tests/sim/v17-integration/mc_v17.py `run_batch`)
---------------------------------------------------------------
    for i in range(n): r = run_campaign(seed=i)   # run_campaign: rng = random.Random(seed)
    summary = reduce(results)
Each seed is independent and deterministic (per-seed RNG), so resuming at seed k
and continuing reproduces an uninterrupted run exactly. A hard kill mid-seed loses
only the seeds since the last flush; those are re-run identically on resume.

USAGE — replace a `for i in range(n)` batch loop:
    from resumable_runner import run_resumable
    out = run_resumable('v17_n1000', 1000,
                        run_one=lambda s: run_campaign(seed=s),
                        reduce_fn=summarize,        # results -> summary dict
                        checkpoint_every=25,        # flush cadence
                        max_seconds=240)            # soft per-CALL wall-clock budget
    if out['status'] == 'done':
        summary = out['summary']
    # else status == 'in_progress' -> call again (same args) in the NEXT bash block; it resumes.

SCOPE (MVP): independent, deterministic-per-seed trials — the Valoria MC shape.
NOT for stateful sequential sims that carry RNG/state across trials; those need
RNG-state serialization, deliberately out of scope. run_one(seed) must return a
JSON-serializable value.
"""
import json
import os
import time
import hashlib
import tempfile

DEFAULT_SCRATCH = '/home/claude/.valoria_sim_ckpt'


def _ckpt_path(scratch_dir, job_id):
    return os.path.join(scratch_dir, job_id + '.json')


def _fingerprint(job_id, n, extra):
    h = hashlib.sha256()
    h.update(repr((job_id, n, extra)).encode())
    return h.hexdigest()[:16]


def _atomic_write(path, obj):
    d = os.path.dirname(path)
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, suffix='.tmp')
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(obj, f)
        os.replace(tmp, path)            # atomic on POSIX
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass


def _load_ckpt(path, fp):
    try:
        with open(path) as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    if data.get('fingerprint') != fp:
        return None                      # stale (n / params changed) -> restart
    return data


def _ret(data, path, reduce_fn, done):
    out = {
        'status': 'done' if done else 'in_progress',
        'completed': data['completed'],
        'total': data['total'],
        'job_id': data['job_id'],
        'ckpt': path,
    }
    if done:
        out['results'] = data['results']
        out['summary'] = reduce_fn(data['results']) if reduce_fn else None
    return out


def run_resumable(job_id, n, run_one, reduce_fn=None, checkpoint_every=25,
                  max_seconds=None, scratch_dir=DEFAULT_SCRATCH,
                  fingerprint_extra=None, verbose=True):
    """Run run_one(seed) for seed in 0..n-1, checkpointing to scratch_dir/<job_id>.json.

    Returns a dict: status ('done'|'in_progress'), completed, total, job_id, ckpt;
    plus results + summary when done. Re-call with the same args to resume; identical
    args after 'done' return the cached result without re-running.

    checkpoint_every : flush to disk every K completed seeds (lower = less lost work
                       on a hard kill, more I/O). Set 1 for very expensive seeds.
    max_seconds      : soft wall-clock budget for THIS call; set well under the
                       bash_tool limit so the runner returns 'in_progress' cleanly
                       before a kill. None = run to completion.
    """
    if not isinstance(job_id, str) or not job_id or any(c in job_id for c in '/\\ \t"\''):
        raise ValueError("job_id must be a non-empty string with no whitespace/path separators/quotes")
    if n < 0:
        raise ValueError("n must be >= 0")
    if checkpoint_every < 1:
        raise ValueError("checkpoint_every must be >= 1")

    fp = _fingerprint(job_id, n, fingerprint_extra)
    path = _ckpt_path(scratch_dir, job_id)
    data = _load_ckpt(path, fp)
    if data is None:
        data = {'job_id': job_id, 'total': n, 'fingerprint': fp,
                'completed': 0, 'results': [], 'status': 'in_progress'}

    if data['completed'] >= n:           # already complete (cached)
        data['status'] = 'done'
        if verbose:
            print(f"[resumable_runner] {job_id}: already complete ({n}/{n}) — cached")
        return _ret(data, path, reduce_fn, done=True)

    results = data['results']
    t0 = time.time()
    flushed = data['completed']
    for seed in range(data['completed'], n):
        r = run_one(seed)                # deterministic per seed; a crash here loses only
        results.append(r)                # seeds since the last flush (re-run on resume)
        data['completed'] = seed + 1
        if (data['completed'] - flushed) >= checkpoint_every:
            _atomic_write(path, data)
            flushed = data['completed']
        if max_seconds is not None and (time.time() - t0) >= max_seconds and data['completed'] < n:
            data['status'] = 'in_progress'
            _atomic_write(path, data)
            if verbose:
                print(f"[resumable_runner] {job_id}: budget hit — {data['completed']}/{n} done, "
                      f"checkpointed; re-call (same args) to resume")
            return _ret(data, path, reduce_fn, done=False)

    data['status'] = 'done'
    _atomic_write(path, data)
    if verbose:
        print(f"[resumable_runner] {job_id}: complete {n}/{n} ({time.time() - t0:.1f}s this call)")
    return _ret(data, path, reduce_fn, done=True)


def status(job_id, scratch_dir=DEFAULT_SCRATCH):
    """Inspect progress without running. Returns dict or None if no checkpoint."""
    try:
        with open(_ckpt_path(scratch_dir, job_id)) as f:
            d = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return {'job_id': job_id, 'completed': d.get('completed'),
            'total': d.get('total'), 'status': d.get('status'),
            'ckpt': _ckpt_path(scratch_dir, job_id)}


def clear(job_id, scratch_dir=DEFAULT_SCRATCH):
    """Delete a job's checkpoint (start fresh next run). Returns True if removed."""
    try:
        os.remove(_ckpt_path(scratch_dir, job_id))
        return True
    except FileNotFoundError:
        return False
