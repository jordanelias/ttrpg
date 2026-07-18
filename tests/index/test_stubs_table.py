"""Hermetic test for the curated `stubs` table + its concept link.

Asserts: stub rows survive a dump round-trip (curated preservation, the
Defect-2 class), stub_summary / stubs_by_status read correctly, and
stub_status joins a stub to its concept via canon_source -> concept_files
-> concepts. Fully mocked — no network, no real repo.
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
import index_bootstrap as ix       # noqa: E402
from pathlib import Path           # noqa: E402

FIXTURE = """-- valoria_index.sql
-- fixture header (stripped)
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS files (
  path TEXT PRIMARY KEY, directory TEXT, filename TEXT, status TEXT,
  variant TEXT, pair_id TEXT, domain TEXT, sha TEXT, headings TEXT);
CREATE TABLE IF NOT EXISTS concepts (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS aliases (alias TEXT, concept_id INTEGER);
CREATE TABLE IF NOT EXISTS concept_files (concept_id INTEGER, path TEXT);
CREATE TABLE IF NOT EXISTS stubs (
  module TEXT PRIMARY KEY, layer TEXT, tier INTEGER, status TEXT,
  canon_source TEXT, blocked_on TEXT);
INSERT OR REPLACE INTO concepts (id, name) VALUES ('1', 'threadwork');
INSERT OR REPLACE INTO concepts (id, name) VALUES ('2', 'combat');
INSERT OR REPLACE INTO concept_files (concept_id, path) VALUES ('1', 'designs/threadwork/threadwork_v30.md');
INSERT OR REPLACE INTO concept_files (concept_id, path) VALUES ('2', 'designs/scene/combat_v30.md');
INSERT OR REPLACE INTO stubs (module, layer, tier, status, canon_source, blocked_on) VALUES ('sim/thread/coherence.py', 'thread', 0, 'verified', 'designs/threadwork/threadwork_v30.md', NULL);
INSERT OR REPLACE INTO stubs (module, layer, tier, status, canon_source, blocked_on) VALUES ('sim/personal/combat.py', 'personal', 1, 'partial', 'designs/scene/combat_v30.md', NULL);
INSERT OR REPLACE INTO stubs (module, layer, tier, status, canon_source, blocked_on) VALUES ('systems/factions/sim/charter_liberties.py', 'provincial', 0, 'canon_gated', NULL, 'Pass 2e Hafenmark');
"""


def _schema_only(dump):
    L = dump.splitlines()
    s = next(i for i, l in enumerate(L) if l.lstrip().upper().startswith('CREATE'))
    return '\n'.join(l for l in L[s:] if not l.lstrip().upper().startswith('INSERT'))


def test_stub_summary_by_status_and_link(tmp_path):
    conn = R.open_db(Path(str(tmp_path / 's.db')), FIXTURE)
    assert ix.stub_summary(conn) == {'canon_gated': 1, 'partial': 1, 'verified': 1}
    assert ix.stubs_by_status(conn, 'canon_gated') == ['systems/factions/sim/charter_liberties.py']
    # concept-join: threadwork -> coherence stub (via canon_source -> concept_files)
    assert ix.stub_status(conn, 'threadwork') == [('sim/thread/coherence.py', 'verified', 0, None)]
    assert ix.stub_status(conn, 'combat') == [('sim/personal/combat.py', 'partial', 1, None)]
    # a concept with no stub link returns empty, not an error
    assert ix.stub_status(conn, 'nonexistent') == []


def test_stubs_survive_dump_roundtrip(tmp_path):
    conn = R.open_db(Path(str(tmp_path / 's.db')), FIXTURE)
    before = conn.execute("SELECT COUNT(*) FROM stubs").fetchone()[0]
    out = str(tmp_path / 'o.sql')
    R.SCHEMA_SQL = _schema_only(FIXTURE)
    R.dump_to_sql(conn, out)
    dumped = open(out).read()
    conn2 = R.open_db(Path(str(tmp_path / 'r.db')), dumped)
    after = conn2.execute("SELECT COUNT(*) FROM stubs").fetchone()[0]
    assert after == before == 3, f"stubs lost on round-trip: {before} -> {after}"
    assert 'CREATE TABLE IF NOT EXISTS stubs' in dumped
    assert dumped.count('INSERT OR REPLACE INTO stubs') == 3


if __name__ == '__main__':
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        test_stub_summary_by_status_and_link(Path(d))
    with tempfile.TemporaryDirectory() as d:
        test_stubs_survive_dump_roundtrip(Path(d))
    print("PASS: stub_summary / stubs_by_status / stub_status concept-link + dump round-trip preservation")
