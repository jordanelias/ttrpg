"""
propagator.py — Valoria text propagation tool
Applies editorial decisions and patches across compiled stage files.
"""

import re


def propagate_exact(old: str, new: str, file_contents: dict) -> dict:
    """
    Exact string replacement across all files.
    Returns {path: (new_content, replacement_count)}
    """
    results = {}
    for path, content in file_contents.items():
        count = content.count(old)
        if count > 0:
            results[path] = (content.replace(old, new), count)
    return results


def propagate_contextual(old: str, new: str, context_required: str,
                          file_contents: dict) -> dict:
    """
    Replace old->new only where context_required appears within 100 chars.
    For ambiguous replacements where old value appears in multiple senses.
    Returns {path: (new_content, replacement_count)}
    """
    results = {}
    for path, content in file_contents.items():
        new_content = content
        count = 0
        # Find all occurrences of old
        idx = 0
        while True:
            pos = new_content.find(old, idx)
            if pos == -1:
                break
            # Check if context_required is within 100 chars
            window_start = max(0, pos - 100)
            window_end = min(len(new_content), pos + len(old) + 100)
            window = new_content[window_start:window_end]
            if context_required in window:
                new_content = new_content[:pos] + new + new_content[pos + len(old):]
                count += 1
                idx = pos + len(new)
            else:
                idx = pos + len(old)
        if count > 0:
            results[path] = (new_content, count)
    return results


def propagate_from_ledger(entry: dict, file_contents: dict) -> dict:
    """
    Read affects list from ledger entry. Apply contextual or exact replacement
    based on entry's 'replacement_type' field.
    Only processes files listed in entry's affects list.
    """
    affects_paths = {a["path"] for a in entry.get("affects", [])}
    relevant = {p: c for p, c in file_contents.items() if p in affects_paths}

    old = entry.get("old_value", "")
    new = entry.get("new_value", "")
    if not old or not new:
        return {}

    rtype = entry.get("replacement_type", "exact")
    if rtype == "contextual":
        context = entry.get("context_hint", "")
        return propagate_contextual(old, new, context, relevant)
    else:
        return propagate_exact(old, new, relevant)


if __name__ == "__main__":
    # Quick test
    test_files = {
        "stage1.md": "The TC threshold is 60. When TC reaches 60, seizure triggers.",
        "stage2.md": "TC 60 is the limit. Also TC 60 appears in faction rules.",
        "stage3.md": "No relevant content here.",
    }
    results = propagate_exact("TC 60", "TC 65", test_files)
    for path, (content, count) in results.items():
        print(f"{path}: {count} replacements")
        print(f"  -> {content[:80]}")
