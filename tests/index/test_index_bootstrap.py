"""Offline smoke test for the SQL-index enshrinement.

Loads the committed references/valoria_index.sql, asserts it round-trips via the
fixed loader (open_db) and that the query interface resolves. The HEAD-rebuild +
coverage-validation path (index_bootstrap.load_index rebuild=True) needs network
and is exercised at bootstrap, not here.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# scripts: repo layout (../../skills/...) first, then a flat container dir
for _c in (os.path.join(_HERE, '..', '..', 'skills', 'valoria-orchestrator', 'scripts'),
           '/home/claude'):
    if os.path.isdir(_c):
        sys.path.insert(0, os.path.abspath(_c))
        break
# index sql: repo layout (../../references/...) first, then container copies
INDEX_SQL = next((p for p in (
    os.path.join(_HERE, '..', '..', 'references', 'valoria_index.sql'),
    '/home/claude/valoria_index.sql',
    '/mnt/user-data/outputs/valoria_index.sql') if os.path.exists(p)), None)

import index_bootstrap as ix
import regenerate_file_index as R


def test_committed_dump_round_trips(tmp_path):
    sql = open(INDEX_SQL).read()
    conn = R.open_db(str(tmp_path / 't.db'), sql)        # F2 fix: loads w/o raising
    assert conn.execute("SELECT COUNT(*) FROM concepts").fetchone()[0] > 0
    assert conn.execute("SELECT COUNT(*) FROM concept_files").fetchone()[0] > 0
    assert conn.execute("SELECT COUNT(*) FROM aliases").fetchone()[0] > 0
    conn.close()
    # NB: concept_files.path -> files(path) FK is dangling until `files` is rebuilt
    # at bootstrap; FK integrity is asserted there by index_bootstrap.validate().


def test_query_interface(tmp_path):
    sql = open(INDEX_SQL).read()
    conn = R.open_db(str(tmp_path / 't.db'), sql)
    assert any('threadwork_v30.md' in p for p in ix.concept_files(conn, 'threadwork'))
    assert ix.which_concepts(conn, 'params/threadwork.md')
    assert 'threadwork' in ix.search(conn, 'thread')
    conn.close()
