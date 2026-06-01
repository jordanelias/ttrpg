"""Valoria SQL-index bootstrap: load + validate + query the governing file index.

Enshrines references/valoria_index.sql as the single interface for "what files
does system X comprise" and "what system does file Y belong to". Called from the
PI bootstrap script immediately after quick_bootstrap():

    import index_bootstrap as ix
    conn, report = ix.load_index(g)          # rebuild files from HEAD, load curated, validate
    ix.print_index_summary(report)
    # thereafter, route reads through the manifest:
    for path in ix.concept_files(conn, 'threadwork'):
        ...

Drift model:
  - `files` (machine table) is rebuilt from HEAD every session via run_fast's
    SHA-diff tree walk, so it cannot drift from the actual repo tree.
  - curated tables (concepts / concept_files / aliases) load from the committed
    dump; validate() surfaces drift LOUDLY (manifest paths pointing at deleted/
    renamed files; active design docs registered to no concept) and HALTS on FK
    corruption — or on any drift when strict=True.
"""
import os
import sqlite3
import json
import base64
import urllib.request

DB_PATH = '/home/claude/valoria.db'
REPO = 'jordanelias/ttrpg'
INDEX_PATH = 'references/valoria_index.sql'


def _fetch_committed_sql(pat, repo=REPO, path=INDEX_PATH):
    req = urllib.request.Request(
        f'https://api.github.com/repos/{repo}/contents/{path}?ref=main',
        headers={'Authorization': f'token {pat}',
                 'Accept': 'application/vnd.github.v3+json'})
    with urllib.request.urlopen(req) as r:
        return base64.b64decode(json.loads(r.read())['content']).decode()


CACHE_PATH = '/home/claude/.index_cache.json'


def load_index(g=None, sql_text=None, rebuild=True, strict=False,
               db_path=DB_PATH, ttl=600):
    """Load the committed index, rebuild `files` from HEAD, validate.

    Returns (conn, report). `g` is accepted for call-site symmetry with
    quick_bootstrap but is not required; the PAT is read from disk.

    Cost discipline: within `ttl` seconds and with the DB already present, the
    HEAD rebuild and the dump fetch are skipped entirely (zero API calls) — so
    per-subprocess bootstrap does not exhaust the GraphQL/REST rate budget
    (the cc052aa failure mode). `safe_commit` must clear CACHE_PATH on any
    file-tree-changing commit to force the next bootstrap to rebuild.
    """
    import time
    import json as _json
    import regenerate_file_index as R
    R.DB_PATH = db_path
    if rebuild and os.path.exists(db_path) and os.path.exists(CACHE_PATH):
        try:
            c = _json.load(open(CACHE_PATH))
            if time.time() - c.get('ts', 0) < ttl:
                conn = sqlite3.connect(db_path)
                conn.isolation_level = None
                return conn, validate(conn, strict=strict)   # cache hit: zero API
        except Exception:
            pass
    if sql_text is None:
        pat = open('/home/claude/.valoria_pat').read().strip()
        sql_text = _fetch_committed_sql(pat)
    for f in (db_path, db_path + '-wal', db_path + '-shm'):
        if os.path.exists(f):
            os.remove(f)
    if rebuild:
        # open_db (fixed loader) applies schema + curated rows; run_fast adds `files`
        R.run_fast(schema_sql=sql_text)
        conn = sqlite3.connect(db_path)
        conn.isolation_level = None
    else:
        conn = R.open_db(db_path, sql_text)
    report = validate(conn, strict=strict)
    try:
        _json.dump({'ts': time.time()}, open(CACHE_PATH, 'w'))
    except Exception:
        pass
    return conn, report


def validate(conn, strict=False):
    dangling = [p for (p,) in conn.execute(
        "SELECT DISTINCT cf.path FROM concept_files cf "
        "LEFT JOIN files f ON f.path = cf.path WHERE f.path IS NULL")]
    uncovered = [p for (p,) in conn.execute(
        "SELECT path FROM files WHERE variant='normal' AND status='active' "
        "AND path NOT IN (SELECT path FROM concept_files) "
        "AND filename NOT LIKE '%\\_v0.md' ESCAPE '\\' "
        "AND filename NOT LIKE '%draft%'")]
    # malformed-dump check: a concept_files row pointing at a missing concept_id.
    # (concept_files.path -> files(path) "violations" are the `dangling` set above and
    #  are drift, not corruption — they warn, they do not halt.)
    orphan_cf = conn.execute(
        "SELECT COUNT(*) FROM concept_files cf "
        "LEFT JOIN concepts c ON c.id = cf.concept_id WHERE c.id IS NULL").fetchone()[0]
    report = {
        'concepts': conn.execute("SELECT COUNT(*) FROM concepts").fetchone()[0],
        'concept_files': conn.execute("SELECT COUNT(*) FROM concept_files").fetchone()[0],
        'files_active': conn.execute(
            "SELECT COUNT(*) FROM files WHERE status='active'").fetchone()[0],
        'dangling': dangling,
        'uncovered': uncovered,
        'orphan_concept_files': orphan_cf,
    }
    if orphan_cf:
        raise RuntimeError(
            f"[INDEX] {orphan_cf} concept_files row(s) reference a missing "
            f"concept_id — the dump is malformed")
    if strict and (dangling or uncovered):
        raise RuntimeError(
            f"[INDEX] drift under strict mode: {len(dangling)} dangling path(s), "
            f"{len(uncovered)} unregistered active design doc(s)")
    return report


def print_index_summary(report):
    print(f"[INDEX] {report['concepts']} concepts / {report['concept_files']} "
          f"concept_files / {report['files_active']} active files")
    if report['dangling']:
        print(f"[INDEX DRIFT] {len(report['dangling'])} manifest path(s) point at "
              f"missing files (rename/delete not propagated):")
        for p in report['dangling'][:10]:
            print(f"    - {p}")
    if report['uncovered']:
        print(f"[INDEX DRIFT] {len(report['uncovered'])} active design doc(s) "
              f"registered to no concept:")
        for p in report['uncovered'][:10]:
            print(f"    - {p}")
    if not report['dangling'] and not report['uncovered']:
        print("[INDEX] coverage clean — every active design doc maps to a concept.")


def concept_files(conn, name):
    """Canonical file set for a system/concept (the governing read list)."""
    return [p for (p,) in conn.execute(
        "SELECT cf.path FROM concept_files cf JOIN concepts c ON c.id = cf.concept_id "
        "WHERE c.name = ? ORDER BY cf.path", (name,))]


def which_concepts(conn, path):
    """Reverse lookup: which concept(s) a file belongs to."""
    return [n for (n,) in conn.execute(
        "SELECT c.name FROM concept_files cf JOIN concepts c ON c.id = cf.concept_id "
        "WHERE cf.path = ? ORDER BY c.name", (path,))]


def search(conn, term):
    """Concepts whose name or alias matches term (alias-aware lookup)."""
    rows = conn.execute(
        "SELECT DISTINCT c.name FROM concepts c "
        "LEFT JOIN aliases a ON a.concept_id = c.id "
        "WHERE c.name LIKE ? OR a.alias LIKE ? ORDER BY c.name",
        (f'%{term}%', f'%{term}%')).fetchall()
    return [r[0] for r in rows]


def stub_status(conn, system):
    """Implementation status of the sim modules backing a concept/system.

    Joins the curated `stubs` table to the concept graph via
    canon_source -> concept_files -> concepts. Returns rows of
    (module, status, tier, blocked_on) for the named concept.
    """
    return conn.execute(
        "SELECT s.module, s.status, s.tier, s.blocked_on FROM stubs s "
        "JOIN concept_files cf ON cf.path = s.canon_source "
        "JOIN concepts c ON c.id = cf.concept_id "
        "WHERE c.name = ? ORDER BY s.module", (system,)).fetchall()


def stubs_by_status(conn, status):
    """All sim modules in a given implementation status.

    status in {'verified','partial','stub','canon_gated'}.
    """
    return [m for (m,) in conn.execute(
        "SELECT module FROM stubs WHERE status = ? ORDER BY module", (status,))]


def stub_summary(conn):
    """{status: count} across all tracked sim stub modules."""
    return dict(conn.execute(
        "SELECT status, COUNT(*) FROM stubs GROUP BY status ORDER BY status").fetchall())
