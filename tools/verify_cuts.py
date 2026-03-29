"""
verify_cuts.py — Scan compiled output for cut mechanics.
Returns findings for any cut mechanic reference found.
"""

import re

CUT_MECHANICS = {
    "Maxims": [
        r"\bMaxim\b",
        r"Maxim Award",
        r"Maxim CP",
        r"Maxim Points",
    ],
    "Push": [
        r"\bPush\b(?! back)(?! notification)(?! forward)(?! through)(?!ing)",
    ],
    "Thread Harvest": [
        r"Thread Harvest",
        r"Harvest.*Thread",
        r"harvesting supply chain",
    ],
    "Virtues & Vices": [
        r"Virtues?\s*(and|&)\s*Vices?",
        r"Vice\s*(and|&)\s*Virtue",
        r"\bVirtue Ethics\b",
    ],
    "Southernmost Harvesting": [
        r"Southernmost harvest",
        r"harvesting.*Southernmost",
    ],
}


def verify_cuts(file_content: str, filename: str) -> list:
    """
    Returns list of {line_number, line_text, matched_text, cut_mechanic, filename}
    for any cut mechanic reference found.
    """
    findings = []
    lines = file_content.split("\n")
    for i, line in enumerate(lines):
        for mechanic, patterns in CUT_MECHANICS.items():
            for pattern in patterns:
                m = re.search(pattern, line)
                if m:
                    findings.append({
                        "filename": filename,
                        "line_number": i + 1,
                        "line_text": line.strip(),
                        "matched_text": m.group(0),
                        "cut_mechanic": mechanic,
                    })
    return findings


def scan_files(file_contents: dict) -> list:
    """Scan multiple files. Returns all findings."""
    all_findings = []
    for path, content in file_contents.items():
        all_findings.extend(verify_cuts(content, path))
    return all_findings


def format_report(findings: list) -> str:
    if not findings:
        return "verify_cuts: PASS — zero cut mechanic references found."
    lines = [f"verify_cuts: FAIL — {len(findings)} finding(s):\n"]
    for f in findings:
        lines.append(
            f"  [{f['cut_mechanic']}] {f['filename']}:{f['line_number']} — "
            f"matched '{f['matched_text']}'\n    {f['line_text'][:120]}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    test = {
        "stage1.md": "Characters gain Maxim Awards for good play. Push actions cost 1 Momentum.",
        "stage2.md": "Beliefs replace Virtues and Vices entirely. No V&V system.",
        "stage3.md": "Thread operations require no harvesting. Clean content here.",
    }
    findings = scan_files(test)
    print(format_report(findings))
