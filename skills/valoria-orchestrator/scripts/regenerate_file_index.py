#!/usr/bin/env python3
"""
regenerate_file_index.py — Build/update references/valoria_index.sql from repo state.

Usage (in-session, PAT already in env):
    python3 regenerate_file_index.py [--dry-run] [--full]

    --dry-run : print what would change, don't write
    --full    : ignore stored SHAs, re-fetch all files (use after schema changes)

Writes:
    references/valoria_index.sql  — committed text dump (diffable)
    /home/claude/valoria.db       — runtime binary (never committed)

Incremental: compares git blob SHAs against DB. Only fetches changed/new files.
Full regen from scratch takes ~20-30 GraphQL batches for 350 active files.
Incremental on a session where 3 files changed: 1 tree call + 1 batch.

Dependencies: stdlib only (sqlite3, urllib.request, json, base64, re, yaml).
PyYAML is required (already installed in container via valoria_hooks.py).
"""

import os, sys, re, json, sqlite3, base64, urllib.request, yaml, argparse
from datetime import datetime, timezone
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

REPO        = 'jordanelias/ttrpg'
SCHEMA_PATH = Path(__file__).parent.parent / 'schema.sql'  # relative; caller overrides
DB_PATH     = Path('/home/claude/valoria.db')
SQL_OUT     = 'references/valoria_index.sql'   # path in repo to write
SCHEMA_SQL  = None   # populated by load_schema()

PAT_FILE    = '/home/claude/.valoria_pat'

# Directories whose files are always 'deprecated' or 'archived' status
STATUS_OVERRIDE = {
    'deprecated': 'deprecated',
    'archives':   'archived',
}

# Directory → domain mapping (first match wins)
DOMAIN_MAP = [
    ('designs/world',         'world'),
    ('designs/territory',     'territory'),
    ('designs/scene',         'scene'),
    ('designs/provincial',    'provincial'),
    ('designs/arcs',          'arcs'),
    ('designs/npcs',          'npcs'),
    ('designs/threadwork',    'threadwork'),
    ('designs/ui',            'ui'),
    ('designs/audit',         'audit'),
    ('designs/architecture',  'architecture'),
    ('designs/',              'designs'),   # catch-all for designs subfolders
    ('canon/',                'canon'),
    ('references/',           'references'),
    ('skills/',               'skills'),
    ('tools/',                'tools'),
    ('params/',               'params'),
    ('tests/',                'tests'),
    ('session_logs/',         'sessions'),
    ('archives/',             'sessions'),
]

# Extensions to index (skip binaries)
INDEXED_EXTENSIONS = {'.md', '.yaml', '.yml', '.py', '.sql', '.toml', '.json', '.txt'}

# Skip these directories entirely (binary/generated/irrelevant)
SKIP_DIR_PREFIXES = ('.github',)


# ── GitHub helpers ────────────────────────────────────────────────────────────

def get_pat() -> str:
    pat = os.environ.get('GITHUB_PAT', '')
    if not pat and os.path.exists(PAT_FILE):
        pat = open(PAT_FILE).read().strip()
    if not pat:
        raise RuntimeError('GITHUB_PAT not set and .valoria_pat not found.')
    return pat


def gh_request(url: str, pat: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={'Authorization': f'token {pat}',
                 'Accept': 'application/vnd.github.v3+json'}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def fetch_tree(pat: str) -> dict[str, str]:
    """Return {path: sha} for all blobs in repo HEAD (recursive)."""
    data = gh_request(
        f'https://api.github.com/repos/{REPO}/git/trees/HEAD?recursive=1',
        pat
    )
    return {
        item['path']: item['sha']
        for item in data.get('tree', [])
        if item['type'] == 'blob'
    }


def fetch_contents_batch(paths: list[str], pat: str) -> dict[str, str]:
    """Fetch file contents via GraphQL, 20 paths per query."""
    if not paths:
        return {}
    # Try github_ops if available (already batches cleanly)
    try:
        sys.path.insert(0, '/home/claude')
        import github_ops as g
        return g.read_files_graphql(paths)
    except Exception:
        pass
    # Fallback: REST, one at a time (slow, last resort)
    results = {}
    for path in paths:
        try:
            data = gh_request(
                f'https://api.github.com/repos/{REPO}/contents/{path}?ref=main',
                pat
            )
            results[path] = base64.b64decode(data['content']).decode('utf-8', errors='replace')
        except Exception as e:
            print(f'  [WARN] Could not fetch {path}: {e}', file=sys.stderr)
    return results


# ── Classification ────────────────────────────────────────────────────────────

def classify(path: str) -> dict:
    """Derive status, variant, pair_id, domain from path alone."""
    parts   = path.split('/')
    fname   = parts[-1]
    dirpath = '/'.join(parts[:-1]) + ('/' if len(parts) > 1 else '')

    # Status
    status = STATUS_OVERRIDE.get(parts[0], 'active')

    # Domain
    domain = 'root'
    for prefix, d in DOMAIN_MAP:
        if path.startswith(prefix):
            domain = d
            break

    # Variant + pair_id
    ext = Path(fname).suffix.lower()
    if fname.endswith('_index.md'):
        variant = 'index'
        pair_id = re.sub(r'_index\.md$', '', fname)
    elif fname.endswith('_infill.md'):
        variant = 'infill'
        pair_id = re.sub(r'_infill\.md$', '', fname)
    elif re.match(r'.+_v\d+\.md$', fname):
        variant = 'normal'
        pair_id = re.sub(r'\.md$', '', fname)
    elif ext == '.py':
        variant = 'tool'
        pair_id = None
    elif ext in ('.yaml', '.yml', '.json', '.toml'):
        variant = 'data'
        pair_id = None
    elif ext == '.md':
        variant = 'other'
        pair_id = re.sub(r'\.md$', '', fname)
    else:
        variant = 'other'
        pair_id = None

    # Skills: SKILL.md files get skill variant
    if '/skills/' in path and fname == 'SKILL.md':
        variant = 'skill'

    # Tests
    if parts[0] == 'tests':
        variant = 'test'

    return {
        'directory': dirpath.rstrip('/'),
        'filename':  fname,
        'status':    status,
        'variant':   variant,
        'pair_id':   pair_id,
        'domain':    domain,
    }


# ── Content parsing ───────────────────────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter block. Returns {} if absent or unparseable."""
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def extract_headings(content: str, max_level: int = 3) -> str:
    """Return tab-separated H1..H{max_level} texts for FTS indexing."""
    headings = []
    for line in content.splitlines():
        m = re.match(r'^(#{1,%d})\s+(.+)' % max_level, line)
        if m:
            headings.append(m.group(2).strip())
    return '\t'.join(headings)


# ── DB helpers ────────────────────────────────────────────────────────────────

def _split_sql(sql: str):
    """Split SQL into statements, keeping CREATE TRIGGER ... END; bodies atomic."""
    import re as _re
    sql = _re.sub(r'^\s*--.*$', '', sql, flags=_re.M)
    out = []; i = 0; n = len(sql)
    while i < n:
        if _re.match(r'\s*CREATE\s+TRIGGER', sql[i:], _re.I):
            m = _re.search(r'\bEND\s*;', sql[i:], _re.I); j = i + m.end()
            out.append(sql[i:j].strip()); i = j
        else:
            k = sql.find(';', i)
            if k < 0:
                if sql[i:].strip():
                    out.append(sql[i:].strip())
                break
            out.append(sql[i:k + 1].strip()); i = k + 1
    return [s for s in out if s.strip()]


def open_db(db_path: Path, schema_sql: str) -> sqlite3.Connection:
    """Open or create DB, applying schema if fresh.

    Loads statement-by-statement in autocommit with FK off during creation.
    executescript() wraps the whole script in one implicit transaction; combined
    with the dump's embedded `PRAGMA foreign_keys=ON` and the FTS5 trigger /
    shadow-table creation, that trips a deferred FK check at the transaction
    boundary (the committed-dump round-trip bug). Per-statement autocommit with
    FK disabled during creation avoids it; FK is re-enabled afterward.
    """
    conn = sqlite3.connect(str(db_path))
    conn.isolation_level = None
    conn.execute('PRAGMA foreign_keys=OFF')
    conn.execute('PRAGMA journal_mode=WAL')
    for stmt in _split_sql(schema_sql):
        if stmt.upper().startswith('PRAGMA'):
            continue  # ignore embedded pragmas; FK governed externally
        conn.execute(stmt)
    conn.execute('PRAGMA foreign_keys=ON')
    return conn


def stored_shas(conn: sqlite3.Connection) -> dict[str, str]:
    """Return {path: sha} currently in DB."""
    return dict(conn.execute('SELECT path, sha FROM files').fetchall())


def upsert_file(conn: sqlite3.Connection, path: str, sha: str,
                meta: dict, headings: str) -> None:
    conn.execute('''
        INSERT INTO files (path, directory, filename, status, variant,
                           pair_id, domain, sha, headings)
        VALUES (:path, :directory, :filename, :status, :variant,
                :pair_id, :domain, :sha, :headings)
        ON CONFLICT(path) DO UPDATE SET
            directory = excluded.directory,
            filename  = excluded.filename,
            status    = excluded.status,
            variant   = excluded.variant,
            pair_id   = excluded.pair_id,
            domain    = excluded.domain,
            sha       = excluded.sha,
            headings  = excluded.headings
    ''', {**meta, 'path': path, 'sha': sha, 'headings': headings})


def delete_removed(conn: sqlite3.Connection, live_paths: set[str]) -> int:
    """Remove DB rows for paths no longer in repo."""
    stored = {r[0] for r in conn.execute('SELECT path FROM files')}
    gone   = stored - live_paths
    if gone:
        conn.executemany('DELETE FROM files WHERE path = ?', [(p,) for p in gone])
    return len(gone)


# ── Entity import (proper_noun_registry.yaml) ─────────────────────────────────

def import_entities(conn: sqlite3.Connection, registry_yaml: str) -> int:
    """Load proper_noun_registry.yaml into entities + entity_aliases tables."""
    try:
        registry = yaml.safe_load(registry_yaml) or {}
    except yaml.YAMLError as e:
        print(f'  [WARN] Could not parse proper_noun_registry.yaml: {e}', file=sys.stderr)
        return 0

    count = 0
    for category, entries in registry.items():
        if not isinstance(entries, dict):
            continue
        for key, data in entries.items():
            if not isinstance(data, dict):
                continue
            canonical = data.get('canonical', key)
            conn.execute('''
                INSERT INTO entities (key, canonical, category, role, location, source)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(key) DO UPDATE SET
                    canonical = excluded.canonical,
                    category  = excluded.category,
                    role      = excluded.role,
                    location  = excluded.location,
                    source    = excluded.source
            ''', (key, canonical, category,
                  data.get('role'), data.get('location'), data.get('source')))
            entity_id = conn.execute(
                'SELECT id FROM entities WHERE key = ?', (key,)
            ).fetchone()[0]

            # Clear existing aliases for this entity before re-inserting
            conn.execute('DELETE FROM entity_aliases WHERE entity_id = ?', (entity_id,))
            for alias in data.get('aliases', []):
                if alias:
                    try:
                        conn.execute(
                            'INSERT OR IGNORE INTO entity_aliases (entity_id, alias) VALUES (?, ?)',
                            (entity_id, alias)
                        )
                    except sqlite3.IntegrityError:
                        pass  # alias claimed by another entity — skip
            count += 1
    return count


# ── Dump to SQL ───────────────────────────────────────────────────────────────

def dump_to_sql(conn: sqlite3.Connection, out_path: str = None,
                include_generated: bool = False) -> str:
    """
    Produce a text .sql dump suitable for committing.

    By default (include_generated=False), emits only:
      - Schema (CREATE TABLE / INDEX / TRIGGER / VIRTUAL TABLE statements)
      - Curated data: concepts, aliases, concept_files, meta

    The files, entities, and entity_aliases tables are GENERATED at session
    start by run_fast() / run() and are never committed — they are always
    rebuilt from the live repo. Committing them would create large diffs on
    every regen.

    Pass include_generated=True only for debugging / inspection.
    Returns the SQL string (and writes to out_path if provided).
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = [
        '-- valoria_index.sql',
        '-- Schema + curated data for Valoria file index.',
        f'-- Last updated: {now}',
        '-- Generated tables (files, entities, entity_aliases) are rebuilt at',
        '-- session start by regenerate_file_index.py — never hand-edit those.',
        '-- Curated tables (concepts, aliases, concept_files) are safe to edit here.',
        '',
    ]

    if SCHEMA_SQL:
        lines.append('-- ── Schema ─────────────────────────────────────────────────────────────────')
        lines.append(SCHEMA_SQL)
        lines.append('')

    # Curated tables — always emit
    curated = ['meta', 'concepts', 'aliases', 'concept_files']
    # Generated tables — emit only when explicitly requested
    generated = ['files', 'entities', 'entity_aliases']

    tables = curated + (generated if include_generated else [])

    for table in tables:
        rows = conn.execute(f'SELECT * FROM {table}').fetchall()
        # PRAGMA table_info returns: (cid, name, type, notnull, dflt_value, pk)
        cols = [d[1] for d in conn.execute(f'PRAGMA table_info({table})').fetchall()]
        if not rows:
            if table in curated:
                lines.append(f'-- {table}: (empty — add curated entries here)')
            continue
        lines.append(f'-- {table}: {len(rows)} rows')
        col_list = ', '.join(cols)
        for row in rows:
            vals = ', '.join(
                'NULL' if v is None else f"'{str(v).replace(chr(39), chr(39)+chr(39))}'"
                for v in row
            )
            lines.append(f"INSERT OR REPLACE INTO {table} ({col_list}) VALUES ({vals});")
        lines.append('')

    result = '\n'.join(lines)
    if out_path:
        Path(out_path).write_text(result)
    return result


# ── Main ──────────────────────────────────────────────────────────────────────

def run(dry_run: bool = False, full: bool = False, schema_sql: str = '',
        write_sql_to: str = None) -> dict:
    """
    Returns summary dict: {added, updated, removed, entities, elapsed_s}
    """
    import time
    t0 = time.time()

    global SCHEMA_SQL
    SCHEMA_SQL = schema_sql

    pat = get_pat()

    # 1. Fetch tree
    print('Fetching git tree...')
    tree = fetch_tree(pat)
    live_paths = {
        p for p in tree
        if Path(p).suffix.lower() in INDEXED_EXTENSIONS
        and not any(p.startswith(s) for s in SKIP_DIR_PREFIXES)
    }
    print(f'  {len(live_paths)} indexable paths in repo')

    # 2. Open DB
    conn = open_db(DB_PATH, schema_sql)

    # 3. Identify changed/new paths
    if full:
        to_fetch = sorted(live_paths)
        print(f'  Full mode: fetching all {len(to_fetch)} files')
    else:
        existing = stored_shas(conn)
        to_fetch = sorted(
            p for p in live_paths
            if tree[p] != existing.get(p)
        )
        print(f'  Incremental: {len(to_fetch)} changed/new (of {len(live_paths)})')

    if not to_fetch and not dry_run:
        removed = delete_removed(conn, live_paths)
        conn.commit()
        print(f'  No content changes. {removed} paths removed.')
        return {'added': 0, 'updated': 0, 'removed': removed,
                'entities': 0, 'elapsed_s': round(time.time()-t0, 1)}

    if dry_run:
        print(f'  [DRY RUN] Would fetch {len(to_fetch)} files. Stopping.')
        return {'added': 0, 'updated': 0, 'removed': 0,
                'entities': 0, 'elapsed_s': round(time.time()-t0, 1)}

    # 4. Fetch content in batches
    print('Fetching file contents...')
    BATCH = 20
    contents: dict[str, str] = {}
    for i in range(0, len(to_fetch), BATCH):
        batch = to_fetch[i:i+BATCH]
        print(f'  batch {i//BATCH + 1}/{(len(to_fetch)-1)//BATCH + 1} ({len(batch)} files)')
        contents.update(fetch_contents_batch(batch, pat))

    # 5. Also fetch proper_noun_registry
    print('Fetching proper_noun_registry.yaml...')
    pnr_content = fetch_contents_batch(['references/proper_noun_registry.yaml'], pat)
    registry_yaml = pnr_content.get('references/proper_noun_registry.yaml', '')

    # 6. Upsert files
    print('Updating database...')
    added = updated = 0
    existing_paths = {r[0] for r in conn.execute('SELECT path FROM files')}
    for path, content in contents.items():
        meta     = classify(path)
        fm       = parse_frontmatter(content)
        # Frontmatter overrides derived values when present
        if 'status'  in fm: meta['status']  = fm['status']
        if 'variant' in fm: meta['variant'] = fm['variant']
        if 'pair_id' in fm: meta['pair_id'] = fm['pair_id']
        if 'domain'  in fm: meta['domain']  = fm['domain']
        headings = extract_headings(content)
        upsert_file(conn, path, tree[path], meta, headings)
        if path in existing_paths:
            updated += 1
        else:
            added += 1

    # 7. Remove stale paths
    removed = delete_removed(conn, live_paths)

    # 8. Import entities
    entity_count = 0
    if registry_yaml:
        entity_count = import_entities(conn, registry_yaml)
        print(f'  Imported {entity_count} entities')

    # 9. Update meta
    active_count = conn.execute(
        "SELECT COUNT(*) FROM files WHERE status='active'"
    ).fetchone()[0]
    conn.execute("UPDATE meta SET value=? WHERE key='generated'",
                 (datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),))
    conn.execute("UPDATE meta SET value=? WHERE key='file_count'",
                 (str(active_count),))
    conn.commit()

    print(f'  +{added} added, ~{updated} updated, -{removed} removed')
    print(f'  Active files: {active_count}')

    # 10. Dump SQL
    if write_sql_to:
        sql_dump = dump_to_sql(conn, write_sql_to)
        print(f'Writing {write_sql_to} ({len(sql_dump):,} chars)...')
        # This writes to local disk; caller can commit via safe_commit
        Path(write_sql_to).write_text(sql_dump)
        print('  Done.')

    elapsed = round(time.time() - t0, 1)
    print(f'Regeneration complete in {elapsed}s')
    return {'added': added, 'updated': updated, 'removed': removed,
            'entities': entity_count, 'elapsed_s': elapsed}


def run_fast(schema_sql: str = '') -> dict:
    """
    Fast bootstrap path: classify all files from git tree + path alone.

    No content fetches. 1 API call (tree). ~5 seconds.
    Populates: path, directory, filename, status, variant, pair_id, domain.
    Does NOT populate: sha (stored as None), headings (None), entities.
    FTS is not populated — f.search() won't work until run() or run_full() is called.
    f.find() and f.lookup() work immediately after run_fast().

    Designed to run at bootstrap before any task work begins.
    """
    import time
    t0 = time.time()

    pat = get_pat()
    conn = open_db(DB_PATH, schema_sql)

    print('run_fast: fetching git tree...')
    tree = fetch_tree(pat)
    live_paths = {
        p for p in tree
        if Path(p).suffix.lower() in INDEXED_EXTENSIONS
        and not any(p.startswith(s) for s in SKIP_DIR_PREFIXES)
    }
    print(f'  {len(live_paths)} indexable paths')

    # Upsert with path-derived metadata only (no content fetch)
    added = updated = 0
    existing = {r[0] for r in conn.execute('SELECT path FROM files')}
    for path in live_paths:
        meta = classify(path)
        conn.execute('''
            INSERT INTO files (path, directory, filename, status, variant,
                               pair_id, domain, sha, headings)
            VALUES (:path, :directory, :filename, :status, :variant,
                    :pair_id, :domain, NULL, NULL)
            ON CONFLICT(path) DO UPDATE SET
                directory = excluded.directory,
                filename  = excluded.filename,
                status    = excluded.status,
                variant   = excluded.variant,
                pair_id   = excluded.pair_id,
                domain    = excluded.domain
        ''', {**meta, 'path': path})
        if path in existing:
            updated += 1
        else:
            added += 1

    removed = delete_removed(conn, live_paths)

    active = conn.execute(
        "SELECT COUNT(*) FROM files WHERE status='active'"
    ).fetchone()[0]
    conn.execute("UPDATE meta SET value=? WHERE key='file_count'", (str(active),))
    conn.execute("UPDATE meta SET value=? WHERE key='generated'",
                 (datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),))
    conn.commit()

    elapsed = round(time.time() - t0, 1)
    print(f'  run_fast complete: +{added} added, ~{updated} updated, '
          f'-{removed} removed, {active} active ({elapsed}s)')
    return {'added': added, 'updated': updated, 'removed': removed,
            'active': active, 'elapsed_s': elapsed}



    parser = argparse.ArgumentParser(description='Regenerate Valoria file index')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print what would change without writing')
    parser.add_argument('--full', action='store_true',
                        help='Re-fetch all files (ignore stored SHAs)')
    parser.add_argument('--write-sql', metavar='PATH', default=None,
                        help='Write SQL dump to this local path')
    args = parser.parse_args()

    # Load schema
    schema_candidates = [
        Path(__file__).parent.parent / 'references' / 'valoria_index.sql',
        Path('/home/claude/schema.sql'),
    ]
    schema_sql = ''
    for sc in schema_candidates:
        if sc.exists():
            # Extract schema: drop any leading header/comment block (prevents
            # header accretion on repeated regen) and all INSERT data rows.
            raw = sc.read_text()
            _lines = raw.splitlines()
            _start = next((i for i, l in enumerate(_lines)
                           if l.lstrip().upper().startswith('CREATE')), 0)
            schema_lines = [l for l in _lines[_start:]
                            if not l.lstrip().upper().startswith('INSERT')]
            schema_sql = '\n'.join(schema_lines)
            break

    result = run(
        dry_run  = args.dry_run,
        full     = args.full,
        schema_sql = schema_sql,
        write_sql_to = args.write_sql,
    )
    print(json.dumps(result, indent=2))
