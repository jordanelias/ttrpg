"""The game trees hold code, not prose (ED-IN-0229, Jordan 2026-09-16).

This is the falsifier CLAUDE.md §0.1 pt 3 requires for the quarantine gate:
put a markdown file back into `systems/` and this test fails.

It also pins the two things a later session is most likely to erode without
noticing — the exemption list, and the fact that `.designs/` is hidden. The
leading dot IS the mechanism: ripgrep (and therefore the agent search tools
built on it) and Python's `glob.glob` skip dot-directories by default, which is
what stops a sweep of `systems/` from ingesting superseded design docs. Rename
the tree to something visible and the quarantine silently stops working while
every other check here still passes.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from tools import ci_design_prose_quarantine as gate  # noqa: E402


def test_no_markdown_in_the_game_trees():
    bad = gate.offenders()
    assert bad == [], (
        f"{len(bad)} markdown file(s) in a game tree. Design prose belongs in "
        f"proposals/ (new) or .designs/ (superseded), never in systems/ or "
        f"engine/ outside engine/season/. Offenders: {bad[:10]}"
    )


def test_the_gate_exits_nonzero_when_it_finds_prose(tmp_path, monkeypatch):
    """The check must FAIL, not warn — a warning is how the tree refilled."""
    monkeypatch.setattr(gate, '_tracked_md',
                        lambda staged=False: ['systems/combat/some_design_doc.md'])
    assert gate.offenders() == ['systems/combat/some_design_doc.md']


def test_engine_season_is_exempt():
    monkeypatched = ['engine/season/runs/DECISIONS.md', 'engine/mc_v18_walkthrough.md']
    kept = [p for p in monkeypatched if not p.startswith(gate.EXEMPT)]
    assert kept == ['engine/mc_v18_walkthrough.md'], (
        "engine/season/ is exempt by ruling; the rest of engine/ is not."
    )


def test_the_archive_is_hidden():
    """A visible archive defeats the whole mechanism."""
    assert gate.ARCHIVE.startswith('.'), (
        "The archive tree must be dot-prefixed. Ripgrep and glob.glob skip "
        "hidden directories by default; that skip is the quarantine."
    )
    assert (REPO / '.designs').is_dir(), "the .designs/ archive is missing"


def test_archived_documents_announce_themselves():
    """If a session DOES open one, it must read it as non-canon."""
    docs = sorted((REPO / '.designs').rglob('*.md'))
    assert len(docs) >= 230, f"expected the full archive, found {len(docs)}"
    missing = [
        str(d.relative_to(REPO)) for d in docs
        if not d.read_text(encoding='utf-8').startswith('<!-- ARCHIVED-NOT-CANON -->')
    ]
    assert missing == [], (
        f"{len(missing)} archived document(s) carry no ARCHIVED-NOT-CANON banner: "
        f"{missing[:5]}"
    )


def test_archived_paths_still_resolve():
    """Severing the pointers must not strand the citations in the ledgers."""
    from tools import pathres
    r = pathres.resolve('systems/mass_battle/reference/mass_battle_v30.md')
    assert r.status == 'ALIASED', f"expected ALIASED, got {r}"
    assert '.designs/' in str(r), f"should resolve into the archive, got {r}"


def test_the_cli_is_green_on_this_tree():
    proc = subprocess.run(
        [sys.executable, str(REPO / 'tools' / 'ci_design_prose_quarantine.py')],
        capture_output=True, text=True, cwd=REPO,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
