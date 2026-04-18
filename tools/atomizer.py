"""
atomizer.py — Splitting engine for Valoria file atomization.

Pure data transformation: given content + rule, returns new file set.
No GitHub I/O. Deterministic: same input → same output.
"""

import re
import yaml


def atomize(path: str, content: str, rule: dict) -> dict[str, str]:
    """
    Split content per rule['split_strategy']. Returns {new_path: new_content}.
    Original path may be included (as index or reduced form) or absent.
    """
    strategy = rule.get('split_strategy')
    if not strategy:
        raise RuntimeError(
            f"[ATOMIZER] No split_strategy in rule for {path}. "
            f"Cannot atomize without a strategy."
        )

    if strategy == 'by_level_2_heading':
        return split_by_heading(
            content,
            cap_tokens=rule.get('split_cap_per_file', 5000),
            target_pattern=rule.get('target_pattern', path.replace('.md', '_{slug}.md')),
        )
    elif strategy == 'by_vector_category':
        return split_by_category(
            content,
            categories=rule.get('categories', []),
            target_pattern=rule.get('target_pattern', path.replace('.md', '_{category}.md')),
        )
    elif strategy == 'canonical_vs_superseded':
        return split_at_marker(
            content,
            marker=rule.get('superseded_marker', 'SUPERSEDED'),
            target_before=path,
            target_after=rule.get('superseded_target', path.replace('.md', '_superseded.md')),
        )
    elif strategy == 'tables_vs_log':
        return split_at_marker(
            content,
            marker=rule.get('log_split_marker', 'BROKEN DEPENDENCIES'),
            target_before=path,
            target_after=rule.get('log_target', path.replace('.md', '_log.md')),
        )
    elif strategy == 'custom_map':
        split_map_path = rule.get('split_map')
        if not split_map_path:
            raise RuntimeError(f"[ATOMIZER] custom_map strategy but no split_map in rule for {path}")
        # Caller must provide split_map content in rule['_split_map_content']
        split_map_content = rule.get('_split_map_content')
        if not split_map_content:
            raise RuntimeError(
                f"[ATOMIZER] custom_map strategy requires rule['_split_map_content'] "
                f"to be populated before calling atomize(). Fetch {split_map_path} first."
            )
        return split_by_map(content, split_map_content)
    elif strategy == 'chunk_by_quarter':
        return chunk_by_quarter(
            content,
            pattern=rule.get('chunk_pattern', path.replace('.md', '_{year}_q{quarter}.md')),
        )
    else:
        raise RuntimeError(f"[ATOMIZER] Unknown split_strategy: {strategy}")


def archive_by_status(
    active_content: str,
    active_path: str,
    archive_content_by_range: dict[str, str],
    rule: dict,
) -> dict[str, str]:
    """
    Move entries matching rule['auto_archive_status'] from active to archive chunks.
    Returns updated {path: content} for all affected files.
    """
    archive_statuses = set(rule.get('auto_archive_status', []))
    chunk_by = rule.get('archive_chunk_by', 'pp_range')
    chunk_max = rule.get('archive_chunk_max', 10000)
    pattern = rule.get('archive_target_pattern', '')

    try:
        data = yaml.safe_load(active_content)
    except Exception as e:
        raise RuntimeError(f"[ATOMIZER] Cannot parse active YAML at {active_path}: {e}")

    if not isinstance(data, dict):
        return {active_path: active_content}

    # Separate active vs archivable entries
    keep = {}
    archive = {}
    for key, val in data.items():
        if isinstance(val, dict) and str(val.get('status', '')) in archive_statuses:
            archive[key] = val
        else:
            keep[key] = val

    if not archive:
        return {}  # nothing to archive

    # Build result
    result = {}

    # Updated active file
    if keep:
        result[active_path] = yaml.dump(keep, default_flow_style=False, allow_unicode=True, sort_keys=False)
    else:
        result[active_path] = "# Empty — all entries archived\n"

    # Merge archived entries into existing archive chunks
    if chunk_by == 'pp_range':
        archive_additions = _chunk_entries(archive, chunk_max, pattern, r'PP-(\d+)')
    elif chunk_by == 'ed_range':
        archive_additions = _chunk_entries(archive, chunk_max, pattern, r'ED-(\d+)')
    else:
        # Fallback: single archive file
        archive_additions = {
            pattern.format(range='all'):
            yaml.dump(archive, default_flow_style=False, allow_unicode=True, sort_keys=False)
        }

    # Merge with existing archive content
    for arch_path, new_content in archive_additions.items():
        existing = archive_content_by_range.get(arch_path, '')
        if existing:
            try:
                existing_data = yaml.safe_load(existing) or {}
            except Exception:
                existing_data = {}
            new_data = yaml.safe_load(new_content) or {}
            existing_data.update(new_data)
            result[arch_path] = yaml.dump(
                existing_data, default_flow_style=False,
                allow_unicode=True, sort_keys=False
            )
        else:
            result[arch_path] = new_content

    return result


def chunk_archive(
    archive_path: str,
    archive_content: str,
    rule: dict,
) -> dict[str, str]:
    """
    Split an over-threshold archive into chunks per rule['archive_chunk_max'].
    Returns {chunk_path: chunk_content, index_path: index_content}.
    """
    chunk_max = rule.get('archive_chunk_max', 10000)
    pattern = rule.get('archive_target_pattern', rule.get('chunk_pattern', ''))
    id_pattern = r'(PP-\d+|ED-\d+)'

    try:
        data = yaml.safe_load(archive_content)
    except Exception:
        return {archive_path: archive_content}

    if not isinstance(data, dict):
        return {archive_path: archive_content}

    # Sort entries by ID number
    entries = []
    for key, val in data.items():
        m = re.search(r'\d+', str(key))
        num = int(m.group()) if m else 0
        entries.append((key, val, num))
    entries.sort(key=lambda x: x[2])

    # Greedy pack into chunks
    chunks = {}
    current_chunk = {}
    current_tokens = 0
    chunk_start = entries[0][2] if entries else 0

    for key, val, num in entries:
        entry_yaml = yaml.dump({key: val}, default_flow_style=False, allow_unicode=True)
        entry_tokens = len(entry_yaml) // 4
        if current_tokens + entry_tokens > chunk_max and current_chunk:
            chunk_end = list(current_chunk.keys())[-1]
            # Extract range numbers
            s = re.search(r'\d+', str(list(current_chunk.keys())[0]))
            e = re.search(r'\d+', str(chunk_end))
            range_str = f"{s.group().zfill(3)}_{e.group().zfill(3)}" if s and e else "misc"
            chunk_path = pattern.format(range=range_str)
            chunks[chunk_path] = yaml.dump(
                current_chunk, default_flow_style=False,
                allow_unicode=True, sort_keys=False
            )
            current_chunk = {}
            current_tokens = 0

        current_chunk[key] = val
        current_tokens += entry_tokens

    # Final chunk
    if current_chunk:
        s = re.search(r'\d+', str(list(current_chunk.keys())[0]))
        e = re.search(r'\d+', str(list(current_chunk.keys())[-1]))
        range_str = f"{s.group().zfill(3)}_{e.group().zfill(3)}" if s and e else "misc"
        chunk_path = pattern.format(range=range_str)
        chunks[chunk_path] = yaml.dump(
            current_chunk, default_flow_style=False,
            allow_unicode=True, sort_keys=False
        )

    return chunks


# ── Strategy implementations ─────────────────────────────────────────────────

def split_by_heading(content: str, cap_tokens: int,
                     target_pattern: str) -> dict[str, str]:
    """Split by level-2 headings, greedy-packing to cap_tokens per file."""
    sections = _parse_level2_sections(content)
    if not sections:
        return {}

    result = {}
    current_sections = []
    current_tokens = 0

    for heading, body in sections:
        section_text = f"## {heading}\n\n{body}\n"
        section_tokens = len(section_text) // 4

        if current_tokens + section_tokens > cap_tokens and current_sections:
            slug = _slugify(current_sections[0][0])
            path = target_pattern.format(slug=slug)
            result[path] = _join_sections(current_sections)
            current_sections = []
            current_tokens = 0

        current_sections.append((heading, body))
        current_tokens += section_tokens

    if current_sections:
        slug = _slugify(current_sections[0][0])
        path = target_pattern.format(slug=slug)
        result[path] = _join_sections(current_sections)

    return result


def split_by_category(content: str, categories: list,
                      target_pattern: str) -> dict[str, str]:
    """Split by named categories matching level-1/2 headings."""
    lines = content.splitlines()
    result = {}

    for cat in categories:
        cat_name = cat.get('name', 'misc')
        matches = cat.get('matches', [])
        cat_lines = []

        for match_text in matches:
            # Find the heading line
            for i, line in enumerate(lines):
                heading_match = re.match(r'^(#{1,2})\s+(.+)', line)
                if heading_match and match_text in heading_match.group(2):
                    # Collect until next same-or-higher level heading
                    level = len(heading_match.group(1))
                    end = len(lines)
                    for j in range(i + 1, len(lines)):
                        next_match = re.match(r'^(#{1,2})\s+', lines[j])
                        if next_match and len(next_match.group(1)) <= level:
                            end = j
                            break
                    cat_lines.extend(lines[i:end])
                    cat_lines.append("")
                    break

        if cat_lines:
            path = target_pattern.format(category=cat_name)
            result[path] = "\n".join(cat_lines).strip() + "\n"

    return result


def split_at_marker(content: str, marker: str,
                    target_before: str, target_after: str) -> dict[str, str]:
    """Split content at a marker line."""
    lines = content.splitlines()
    marker_line = None

    for i, line in enumerate(lines):
        if marker in line:
            marker_line = i
            break

    if marker_line is None:
        # No marker found — return original unchanged
        return {target_before: content}

    before = "\n".join(lines[:marker_line]).rstrip() + "\n"
    after = "\n".join(lines[marker_line:]).rstrip() + "\n"

    return {
        target_before: before,
        target_after: after,
    }


def split_by_map(content: str, split_map_content: str) -> dict[str, str]:
    """Split by custom heading → target mapping."""
    try:
        split_map = yaml.safe_load(split_map_content)
    except Exception as e:
        raise RuntimeError(f"[ATOMIZER] Cannot parse split map: {e}")

    index_file = split_map.get('index_file', '')
    domain_files = split_map.get('domain_files', [])

    lines = content.splitlines()
    heading_ranges = _build_heading_ranges(lines)

    result = {}
    claimed_lines = set()

    for domain in domain_files:
        target = domain.get('target', '')
        headings = domain.get('headings', [])
        domain_lines = []

        for heading_text in headings:
            for h_text, (start, end) in heading_ranges.items():
                if heading_text.strip() == h_text.strip():
                    domain_lines.extend(lines[start:end])
                    domain_lines.append("")
                    for li in range(start, end):
                        claimed_lines.add(li)
                    break

        if domain_lines:
            result[target] = "\n".join(domain_lines).strip() + "\n"

    # Collect orphan lines (not claimed by any domain file)
    orphan_lines = []
    for i, line in enumerate(lines):
        if i not in claimed_lines and line.strip():
            # Skip the top-level title heading
            if re.match(r'^#\s+', line):
                continue
            orphan_lines.append(line)

    if orphan_lines:
        # Include orphans in a misc file
        misc_path = index_file.replace('.md', '_misc.md') if index_file else 'misc.md'
        result[misc_path] = "\n".join(orphan_lines).strip() + "\n"

    return result


def chunk_by_quarter(content: str, pattern: str) -> dict[str, str]:
    """Split session archive by quarter based on dates found in content."""
    # Find session boundaries (--- separator)
    sessions = re.split(r'\n---\n', content)
    quarters = {}

    for session in sessions:
        if not session.strip():
            continue
        # Extract date
        date_match = re.search(r'session_close:\s*(\d{4})-(\d{2})', session)
        if date_match:
            year = date_match.group(1)
            month = int(date_match.group(2))
            quarter = (month - 1) // 3 + 1
        else:
            year = "unknown"
            quarter = 0
        key = (year, quarter)
        if key not in quarters:
            quarters[key] = []
        quarters[key].append(session.strip())

    result = {}
    for (year, quarter), session_list in sorted(quarters.items()):
        path = pattern.format(year=year, quarter=quarter)
        result[path] = "\n\n---\n\n".join(session_list) + "\n"

    return result


# ── Internal helpers ──────────────────────────────────────────────────────────

def _parse_level2_sections(content: str) -> list[tuple[str, str]]:
    """Parse content into list of (heading_text, body) for level-2 headings."""
    lines = content.splitlines()
    sections = []
    current_heading = None
    current_body = []

    for line in lines:
        m = re.match(r'^##\s+(.+)', line)
        if m:
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_body).strip()))
            current_heading = m.group(1).strip()
            current_body = []
        elif current_heading is not None:
            current_body.append(line)

    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_body).strip()))

    return sections


def _build_heading_ranges(lines: list[str]) -> dict[str, tuple[int, int]]:
    """Build heading_text → (start_line, end_line) mapping for all headings."""
    headings = []
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            headings.append({
                'line': i,
                'level': len(m.group(1)),
                'text': m.group(2).strip(),
            })

    ranges = {}
    for idx, h in enumerate(headings):
        start = h['line']
        end = len(lines)
        for j in range(idx + 1, len(headings)):
            if headings[j]['level'] <= h['level']:
                end = headings[j]['line']
                break
        ranges[h['text']] = (start, end)

    return ranges


def _slugify(text: str) -> str:
    """Convert heading text to filename-safe slug."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9]+', '_', slug)
    slug = slug.strip('_')
    return slug[:50]  # cap length


def _join_sections(sections: list[tuple[str, str]]) -> str:
    """Join heading+body pairs into a single markdown string."""
    parts = []
    for heading, body in sections:
        if body:
            parts.append(f"## {heading}\n\n{body}")
        else:
            parts.append(f"## {heading}")
    return "\n\n".join(parts) + "\n"


def _chunk_entries(entries: dict, chunk_max: int, pattern: str,
                   id_regex: str) -> dict[str, str]:
    """Greedy-pack YAML entries into chunks by ID range."""
    # Sort by ID number
    sorted_entries = []
    for key, val in entries.items():
        m = re.search(id_regex, str(key))
        num = int(m.group(1)) if m else 0
        sorted_entries.append((key, val, num))
    sorted_entries.sort(key=lambda x: x[2])

    chunks = {}
    current = {}
    current_tokens = 0

    for key, val, num in sorted_entries:
        entry_yaml = yaml.dump({key: val}, default_flow_style=False, allow_unicode=True)
        entry_tokens = len(entry_yaml) // 4

        if current_tokens + entry_tokens > chunk_max and current:
            s_num = list(current.keys())[0]
            e_num = list(current.keys())[-1]
            s = re.search(r'\d+', str(s_num))
            e = re.search(r'\d+', str(e_num))
            range_str = f"{s.group().zfill(3)}_{e.group().zfill(3)}" if s and e else "misc"
            chunk_path = pattern.format(range=range_str)
            chunks[chunk_path] = yaml.dump(
                current, default_flow_style=False,
                allow_unicode=True, sort_keys=False
            )
            current = {}
            current_tokens = 0

        current[key] = val
        current_tokens += entry_tokens

    if current:
        s = re.search(r'\d+', str(list(current.keys())[0]))
        e = re.search(r'\d+', str(list(current.keys())[-1]))
        range_str = f"{s.group().zfill(3)}_{e.group().zfill(3)}" if s and e else "misc"
        chunk_path = pattern.format(range=range_str)
        chunks[chunk_path] = yaml.dump(
            current, default_flow_style=False,
            allow_unicode=True, sort_keys=False
        )

    return chunks


# ── CLI test ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_content = """# Test Doc

## Section A

Content A here.

## Section B

Content B here with more text.

## Section C

Content C.

## SUPERSEDED SECTIONS

Old content here.
"""
    print("=== split_at_marker ===")
    result = split_at_marker(test_content, "SUPERSEDED", "before.md", "after.md")
    for p, c in result.items():
        print(f"  {p}: {len(c)} chars")

    print("\n=== split_by_heading (cap=100) ===")
    result = split_by_heading(test_content, 100, "test_{slug}.md")
    for p, c in result.items():
        print(f"  {p}:")
        print(f"    {c[:80]}...")
