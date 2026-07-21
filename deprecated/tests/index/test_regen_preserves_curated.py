"""Hermetic regression test for the regenerate_file_index entrypoint.

Guards the curated-data-loss defect: regenerating the file index must NOT wipe
the hand-curated tables (concepts / aliases / concept_files / meta). The
entrypoint seeds curated rows into a fresh DB before run() refreshes the machine
`files` table; because every CREATE is `IF NOT EXISTS`, run()'s own open_db is an
idempotent no-op and the curated rows survive into the committed dump.

Fully mocked — no network, no real repo. Run via pytest or directly.
"""
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))
for _p in (
    os.path.join(_here, '..', '..', 'skills', 'valoria-orchestrator', 'scripts'),
    '/home/claude',
):
    if os.path.isdir(_p) and _p not in sys.path:
        sys.path.insert(0, _p)

import regenerate_file_index as R  # noqa: E402
from pathlib import Path  # noqa: E402


# Compact, self-consistent fixture: schema (with a leading header block that must
# be stripped) + a known curated set. Columns match what run()/dump_to_sql touch.
FIXTURE = """-- valoria_index.sql
-- fixture header block — MUST be stripped on regen (no accretion)
-- \u2500\u2500 Schema \u2500\u2500
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS files (
  path TEXT PRIMARY KEY, directory TEXT, filename TEXT, status TEXT,
  variant TEXT, pair_id TEXT, domain TEXT, sha TEXT, headings TEXT);
CREATE TABLE IF NOT EXISTS concepts (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS aliases (alias TEXT, concept_id INTEGER);
CREATE TABLE IF NOT EXISTS concept_files (concept_id INTEGER, path TEXT);
-- meta
INSERT OR REPLACE INTO meta (key, value) VALUES ('version', '1');
INSERT OR REPLACE INTO meta (key, value) VALUES ('file_count', '0');
-- concepts
INSERT OR REPLACE INTO concepts (id, name) VALUES ('1', 'alpha');
INSERT OR REPLACE INTO concepts (id, name) VALUES ('2', 'beta');
INSERT OR REPLACE INTO concepts (id, name) VALUES ('3', 'gamma');
-- aliases
INSERT OR REPLACE INTO aliases (alias, concept_id) VALUES ('a', '1');
INSERT OR REPLACE INTO aliases (alias, concept_id) VALUES ('al', '1');
INSERT OR REPLACE INTO aliases (alias, concept_id) VALUES ('b', '2');
-- concept_files
INSERT OR REPLACE INTO concept_files (concept_id, path) VALUES ('1', 'designs/alpha_v30.md');
INSERT OR REPLACE INTO concept_files (concept_id, path) VALUES ('2', 'designs/beta_v30.md');
"""
EXPECT = {'concepts': 3, 'aliases': 3, 'concept_files': 2}


def _schema_only(dump: str) -> str:
    lines = dump.splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.lstrip().upper().startswith('CREATE')), 0)
    return '\n'.join(l for l in lines[start:]
                     if not l.lstrip().upper().startswith('INSERT'))


def _run_case(workdir):
    db = os.path.join(workdir, 'idx.db')
    reload_db = os.path.join(workdir, 'reload.db')
    out = os.path.join(workdir, 'out.sql')

    # Mock the network: a tiny tree, trivial file contents, empty proper-noun
    # registry (so import_entities is skipped — keeps the fixture schema minimal).
    R.fetch_tree = lambda pat: {
        'designs/alpha_v30.md': 's1',
        'designs/beta_v30.md': 's2',
        'designs/gamma_v30.md': 's3',
    }
    R.fetch_contents_batch = lambda paths, pat: {
        p: ('' if 'proper_noun' in p else '# Title\n## Section\n') for p in paths
    }
    R.get_pat = lambda: 'fake-pat'
    R.DB_PATH = db

    schema_only = _schema_only(FIXTURE)

    # Entrypoint step 1: seed curated into a fresh DB.
    conn = R.open_db(Path(db), FIXTURE)
    before = {t: conn.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in EXPECT}
    assert before == EXPECT, f"fixture seed wrong: {before}"
    conn.close()

    # Entrypoint step 2: regen — run() refreshes files; its open_db is idempotent.
    R.run(dry_run=False, full=True, schema_sql=schema_only, write_sql_to=out)

    dumped = open(out).read()
    # Reload the emitted dump and confirm curated rows survived a full round-trip.
    conn2 = R.open_db(Path(reload_db), dumped)
    after = {t: conn2.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in EXPECT}
    conn2.close()

    assert after == before, f"curated LOST on regen: {before} -> {after}"
    assert dumped.count('-- valoria_index.sql') == 1, "header accretion (>1 header block)"
    files_rows = sum(1 for l in dumped.splitlines()
                     if l.startswith('INSERT') and 'INTO files' in l)
    assert files_rows == 0, "machine `files` rows must not be committed to the dump"
    return before, after


def test_regen_preserves_curated(tmp_path):
    before, after = _run_case(str(tmp_path))
    assert after == before == EXPECT


if __name__ == '__main__':
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        b, a = _run_case(d)
    print(f"PASS: curated preserved across regen {b} -> {a}; no header accretion; "
          f"files excluded from dump")
