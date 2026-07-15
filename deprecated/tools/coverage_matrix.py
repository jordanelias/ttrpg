"""
coverage_matrix.py — Coverage matrix management for Valoria simulation tracking.
Manages the 7-dimension test coverage matrix.
"""

import re
from datetime import date


def add_test(matrix: str, test: dict) -> str:
    """
    Add a test record to the coverage matrix markdown table.
    test dict keys: test_id, mechanics, mode, temporal, tracks, factions,
                    npcs, archetypes, status, findings
    Returns updated matrix string.
    """
    row = (
        f"| {test.get('test_id', '')} "
        f"| {test.get('mechanics', '')} "
        f"| {test.get('mode', '')} "
        f"| {test.get('temporal', '')} "
        f"| {test.get('tracks', '')} "
        f"| {test.get('factions', '')} "
        f"| {test.get('npcs', '')} "
        f"| {test.get('archetypes', '')} "
        f"| {test.get('status', 'Complete')} "
        f"| {test.get('findings', '')} |"
    )
    # Append before the last line if matrix ends with content, else append
    if matrix.strip():
        return matrix.rstrip() + "\n" + row + "\n"
    return row + "\n"


def coverage_report(matrix: str) -> dict:
    """
    Parse coverage matrix and return summary stats.
    Returns {total, by_mechanic, by_mode, by_faction, by_npc, gaps}
    """
    rows = []
    for line in matrix.split("\n"):
        line = line.strip()
        if line.startswith("|") and not line.startswith("| Test ID") and "---" not in line:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 9:
                rows.append(cells)

    total = len(rows)
    by_mode = {}
    by_mechanic = {}
    by_faction = {}
    by_npc = {}

    for row in rows:
        # mode is index 2
        if len(row) > 2:
            mode = row[2]
            by_mode[mode] = by_mode.get(mode, 0) + 1
        # mechanics index 1
        if len(row) > 1:
            for m in row[1].split(","):
                m = m.strip()
                if m:
                    by_mechanic[m] = by_mechanic.get(m, 0) + 1
        # factions index 5
        if len(row) > 5:
            for f in row[5].split(","):
                f = f.strip()
                if f:
                    by_faction[f] = by_faction.get(f, 0) + 1
        # npcs index 6
        if len(row) > 6:
            for n in row[6].split(","):
                n = n.strip()
                if n and n != "—":
                    by_npc[n] = by_npc.get(n, 0) + 1

    return {
        "total": total,
        "by_mode": by_mode,
        "by_mechanic": by_mechanic,
        "by_faction": by_faction,
        "by_npc": by_npc,
    }


def check_gate(matrix: str, requirements: dict) -> tuple:
    """
    Check if coverage meets gate requirements.
    requirements: {
        'min_mechanics_tested': int,
        'modes_required': [str],
        'factions_required': [str],
        'npcs_required': [str],
    }
    Returns (passed: bool, unmet: list[str])
    """
    report = coverage_report(matrix)
    unmet = []

    min_mech = requirements.get("min_mechanics_tested", 0)
    if len(report["by_mechanic"]) < min_mech:
        unmet.append(
            f"Mechanics tested: {len(report['by_mechanic'])} / {min_mech} required"
        )

    for mode in requirements.get("modes_required", []):
        if mode not in report["by_mode"]:
            unmet.append(f"Mode not covered: {mode}")

    for faction in requirements.get("factions_required", []):
        if faction not in report["by_faction"]:
            unmet.append(f"Faction not covered: {faction}")

    for npc in requirements.get("npcs_required", []):
        if npc not in report["by_npc"]:
            unmet.append(f"NPC not covered: {npc}")

    return (len(unmet) == 0, unmet)


if __name__ == "__main__":
    sample = """| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| T-001 | M-001 | TTRPG | PRES | TT | Crown | Almud | Practitioner | Complete | — |
| T-002 | M-002,M-003 | BG | FUT | TC,IP | Church | — | Devout | Complete | P2: clock drift |
"""
    report = coverage_report(sample)
    print("Total tests:", report["total"])
    print("By mode:", report["by_mode"])
    passed, unmet = check_gate(sample, {"modes_required": ["TTRPG", "BG", "HYB"]})
    print("Gate passed:", passed)
    print("Unmet:", unmet)
