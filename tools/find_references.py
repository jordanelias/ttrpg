"""
find_references.py — Search all files for exact occurrences of a value.
Used to verify affects list completeness for editorial decisions and patches.
"""


def find_all_occurrences(value: str, file_contents: dict) -> dict:
    """
    Search all files for exact occurrences of value.
    Returns {path: [line_numbers]} for files that contain value.
    """
    results = {}
    for path, content in file_contents.items():
        lines = content.split("\n")
        hits = [i + 1 for i, line in enumerate(lines) if value in line]
        if hits:
            results[path] = hits
    return results


def find_with_context(value: str, file_contents: dict, context_lines: int = 2) -> dict:
    """
    Returns {path: [{line, context}]} with surrounding context lines.
    """
    results = {}
    for path, content in file_contents.items():
        lines = content.split("\n")
        hits = []
        for i, line in enumerate(lines):
            if value in line:
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                hits.append({
                    "line": i + 1,
                    "context": "\n".join(lines[start:end]),
                })
        if hits:
            results[path] = hits
    return results


def verify_affects_list(value: str, declared_affects: list,
                         file_contents: dict) -> dict:
    """
    Compare declared affects list against actual occurrences.
    Returns {
        'declared_and_found': [...],
        'declared_not_found': [...],   # declared but value not present
        'found_not_declared': [...],   # has value but not in affects list
    }
    """
    actual = set(find_all_occurrences(value, file_contents).keys())
    declared = set(declared_affects)
    return {
        "declared_and_found": sorted(actual & declared),
        "declared_not_found": sorted(declared - actual),
        "found_not_declared": sorted(actual - declared),
    }


if __name__ == "__main__":
    test_files = {
        "stage1.md": "TC threshold is 60. Seizure at TC 60.",
        "stage2.md": "TC 60 triggers event. See also TC 60 in faction rules.",
        "stage3.md": "No TC references here.",
        "stage4.md": "TC 60 appears here but was not declared.",
    }
    result = verify_affects_list(
        "TC 60",
        declared_affects=["stage1.md", "stage2.md"],
        file_contents=test_files,
    )
    print("Declared and found:", result["declared_and_found"])
    print("Declared not found:", result["declared_not_found"])
    print("Found not declared:", result["found_not_declared"])
