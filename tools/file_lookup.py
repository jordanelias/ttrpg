"""
file_lookup.py — Deterministic file and concept lookup for Valoria sessions.
Loaded at bootstrap. Import as `f`.

Usage in bash_tool blocks:
    import sys; sys.path.insert(0, '/home/claude')
    import file_lookup as f

    # What files cover "caste stuff"?
    f.lookup('caste')           # alias or concept name match, returns [paths]
    f.lookup('character histories')

    # Search by keyword across headings/filenames
    f.search('lifepath origin')     # FTS5 match

    # Filtered queries
    f.find(domain='world', status='active')
    f.find(variant='normal', domain='canon')
    f.find(pair_id='character_histories_v30')   # all files in a pair

    # Inspect a concept
    f.concept('character_histories')  # {name, domain, aliases, files}

    # All active concepts
    f.concepts()                  # [(name, domain, alias_count, file_count)]

    # Entity lookup (characters, territories, factions)
    f.entity('Aldric')            # fuzzy alias match → canonical + source
    f.entities(category='character')

    # DB health
    f.status()                    # {active, deprecated, archived, concepts, regen_date}
"""

import sqlite3, os
from pathlib import Path

DB_PATH = Path('/home/claude/valoria.db')


def _conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise RuntimeError(
            '[file_lookup] valoria.db not found at /home/claude/valoria.db\n'
            'Bootstrap must build it before file_lookup can be used.\n'
            'Run the bootstrap block or call build_db() to initialise.'
        )
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys=ON')
    return conn


# ── Core lookup ───────────────────────────────────────────────────────────────

def lookup(query: str, status: str = 'active') -> list[str]:
    """
    Resolve a natural-language query to a list of file paths.

    Priority:
      1. Exact alias match (case-insensitive)  → concept → files
      2. Exact concept name match              → files
      3. FTS5 keyword match on headings/filename

    Returns [] if nothing matches.
    """
    query = query.strip()
    conn  = _conn()

    # 1. Alias → concept → files
    row = conn.execute(
        'SELECT concept_id FROM aliases WHERE alias = ? COLLATE NOCASE',
        (query,)
    ).fetchone()
    if row:
        return _files_for_concept(conn, row['concept_id'], status)

    # 2. Concept name → files
    row = conn.execute(
        'SELECT id FROM concepts WHERE name = ? COLLATE NOCASE',
        (query,)
    ).fetchone()
    if row:
        return _files_for_concept(conn, row['id'], status)

    # 3. FTS5
    try:
        rows = conn.execute(
            'SELECT path FROM files_fts WHERE files_fts MATCH ? '
            'AND path IN (SELECT path FROM files WHERE status = ?) '
            'ORDER BY rank',
            (query, status)
        ).fetchall()
        return [r['path'] for r in rows]
    except sqlite3.OperationalError:
        # FTS table may not yet exist (fresh DB before first regen)
        return []


def _files_for_concept(conn, concept_id: int, status: str) -> list[str]:
    rows = conn.execute(
        'SELECT f.path FROM files f '
        'JOIN concept_files cf ON cf.path = f.path '
        'WHERE cf.concept_id = ? AND f.status = ? '
        'ORDER BY f.variant, f.path',
        (concept_id, status)
    ).fetchall()
    return [r['path'] for r in rows]


# ── Search ────────────────────────────────────────────────────────────────────

def search(query: str, status: str = 'active', limit: int = 20) -> list[str]:
    """FTS5 keyword search across filenames and headings."""
    conn = _conn()
    try:
        rows = conn.execute(
            'SELECT path FROM files_fts WHERE files_fts MATCH ? '
            'AND path IN (SELECT path FROM files WHERE status = ?) '
            'ORDER BY rank LIMIT ?',
            (query, status, limit)
        ).fetchall()
        return [r['path'] for r in rows]
    except sqlite3.OperationalError as e:
        raise RuntimeError(f'[file_lookup.search] FTS error: {e}')


# ── Filtered queries ──────────────────────────────────────────────────────────

def find(domain: str = None, variant: str = None,
         status: str = 'active', pair_id: str = None) -> list[str]:
    """Return paths matching all supplied filters."""
    conn   = _conn()
    clause = ['status = ?']
    params = [status]
    if domain:
        clause.append('domain = ?')
        params.append(domain)
    if variant:
        clause.append('variant = ?')
        params.append(variant)
    if pair_id:
        clause.append('pair_id = ?')
        params.append(pair_id)
    sql  = 'SELECT path FROM files WHERE ' + ' AND '.join(clause) + ' ORDER BY path'
    rows = conn.execute(sql, params).fetchall()
    return [r['path'] for r in rows]


# ── Concept inspection ────────────────────────────────────────────────────────

def concept(name: str) -> dict | None:
    """Return full concept dict: {name, domain, notes, aliases, files}."""
    conn = _conn()
    row  = conn.execute(
        'SELECT id, name, domain, notes FROM concepts '
        'WHERE name = ? COLLATE NOCASE', (name,)
    ).fetchone()
    if not row:
        return None
    aliases = [r['alias'] for r in conn.execute(
        'SELECT alias FROM aliases WHERE concept_id = ? ORDER BY alias',
        (row['id'],)
    ).fetchall()]
    files = _files_for_concept(conn, row['id'], status='active')
    return {'name': row['name'], 'domain': row['domain'],
            'notes': row['notes'], 'aliases': aliases, 'files': files}


def concepts(domain: str = None) -> list[tuple]:
    """List all concepts: [(name, domain, alias_count, file_count)]."""
    conn   = _conn()
    clause = 'WHERE c.domain = ?' if domain else ''
    params = [domain] if domain else []
    rows   = conn.execute(f'''
        SELECT c.name, c.domain,
               COUNT(DISTINCT a.id)  AS alias_count,
               COUNT(DISTINCT cf.path) AS file_count
        FROM concepts c
        LEFT JOIN aliases      a  ON a.concept_id  = c.id
        LEFT JOIN concept_files cf ON cf.concept_id = c.id
        {clause}
        GROUP BY c.id
        ORDER BY c.domain, c.name
    ''', params).fetchall()
    return [(r['name'], r['domain'], r['alias_count'], r['file_count'])
            for r in rows]


# ── Entity lookup ─────────────────────────────────────────────────────────────

def entity(query: str) -> dict | None:
    """
    Look up an entity by canonical name or alias (case-insensitive substring).
    Returns {canonical, category, role, location, source, aliases} or None.
    """
    conn = _conn()
    # Try alias first
    row = conn.execute(
        'SELECT e.* FROM entities e '
        'JOIN entity_aliases ea ON ea.entity_id = e.id '
        'WHERE ea.alias LIKE ? COLLATE NOCASE LIMIT 1',
        (f'%{query}%',)
    ).fetchone()
    if not row:
        row = conn.execute(
            'SELECT * FROM entities WHERE canonical LIKE ? COLLATE NOCASE LIMIT 1',
            (f'%{query}%',)
        ).fetchone()
    if not row:
        return None
    aliases = [r['alias'] for r in conn.execute(
        'SELECT alias FROM entity_aliases WHERE entity_id = ? ORDER BY alias',
        (row['id'],)
    ).fetchall()]
    return {k: row[k] for k in ('canonical','category','role','location','source')} | \
           {'aliases': aliases}


def entities(category: str = None) -> list[dict]:
    """List entities, optionally filtered by category."""
    conn   = _conn()
    clause = 'WHERE category = ?' if category else ''
    params = [category] if category else []
    rows   = conn.execute(
        f'SELECT canonical, category, role, source FROM entities {clause} '
        f'ORDER BY canonical', params
    ).fetchall()
    return [dict(r) for r in rows]


# ── Status ────────────────────────────────────────────────────────────────────

def status() -> dict:
    """Return DB health summary for Status Block."""
    conn = _conn()
    def count(q, *p): return conn.execute(q, p).fetchone()[0]
    meta = dict(conn.execute('SELECT key, value FROM meta').fetchall())
    return {
        'active':      count("SELECT COUNT(*) FROM files WHERE status='active'"),
        'deprecated':  count("SELECT COUNT(*) FROM files WHERE status='deprecated'"),
        'archived':    count("SELECT COUNT(*) FROM files WHERE status='archived'"),
        'concepts':    count('SELECT COUNT(*) FROM concepts'),
        'entities':    count('SELECT COUNT(*) FROM entities'),
        'regen_date':  meta.get('generated', 'never'),
        'db_path':     str(DB_PATH),
    }


def summary_line() -> str:
    """One-line Status Block insert."""
    s = status()
    return (f"File index: {s['active']} active | {s['concepts']} concepts | "
            f"{s['entities']} entities | regen {s['regen_date'][:10] or 'never'}")


# ── DB bootstrap helper ───────────────────────────────────────────────────────

def build_db(sql_text: str) -> None:
    """
    Build /home/claude/valoria.db from a SQL dump string.
    Called at bootstrap after fetching references/valoria_index.sql.
    Safe to re-run (idempotent via INSERT OR REPLACE / OR IGNORE).
    """
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript(sql_text)
    conn.commit()
    conn.close()
