"""
Unit tests for tools/handoff_atomize.py — the handoff skeleton/infill/archive contract
(ED-IN-0086, Jordan ruling 2026-07-28).

What these pin, and why each one is the falsifier for a specific claim (§0.1 point 3):

  • The STATUS TAG is authoritative over prose. The whole point of the tag is that prose
    inference was wrong — five lanes carry LIVE items whose text matches RESOLVED_SKIP and
    are counted as settled by the SessionStart banner. If prose could still override a tag,
    the convention would buy nothing.
  • A tag that can lie is no better than the prose it replaced, so [DONE]-with-residue and
    [PART]-without-a-named-residual must be reported.
  • Archive naming: exactly one open-ended document, everything else a closed range. If two
    files claimed `_open`, appends would be ambiguous.
  • The 10,000-token cap actually binds.
"""
import datetime
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import handoff_atomize as H  # noqa: E402

CUTOFF = datetime.date(2026, 6, 28)


def test_status_tag_parses_all_three_states_and_tolerates_bold():
    assert H.status_tag("- [OPEN] a thing")[0] == 'OPEN'
    assert H.status_tag("- [PART] a thing — residual: x")[0] == 'PART'
    kind, when = H.status_tag("- [DONE 2026-07-26] a thing")
    assert (kind, when) == ('DONE', datetime.date(2026, 7, 26))
    # `- **[OPEN] …**` is how a human writes it; a convention that only matched unbolded
    # text would be bypassed by ordinary formatting.
    assert H.status_tag("- **[OPEN] a thing**")[0] == 'OPEN'
    assert H.status_tag("- an untagged legacy bullet") is None


def test_tag_beats_prose_in_both_directions():
    # The exact defect the convention exists to kill: prose says settled, tag says open.
    open_but_reads_closed = "- [OPEN] ED-IN-0029 — PARTIALLY RATIFIED 2026-07-08, RESOLVED in part"
    assert H.classify(open_but_reads_closed, CUTOFF) == ('live', True)
    # And the converse — prose gives no closer, tag says done.
    done_but_reads_open = "- [DONE 2026-07-26] groundwork filed 2026-07-26"
    assert H.classify(done_but_reads_open, CUTOFF) == ('closed', True)


def test_untagged_bullets_still_classify_by_prose_and_are_reported():
    assert H.classify("- Thing DELIVERED 2026-07-04", CUTOFF) == ('closed', False)
    assert H.classify("- Thing PARTIALLY RATIFIED 2026-07-08", CUTOFF) == ('live', False)
    problems = H.tag_problems("XX", ["- untagged one", "- untagged two"])
    assert any("carry no [OPEN|PART|DONE] tag" in p for p in problems)


def test_lying_tags_are_reported():
    assert any("still describes residual" in p for p in
               H.tag_problems("XX", ["- [DONE 2026-07-01] shipped\n  but the sweep is STAGED"]))
    assert any("does not name its residual" in p for p in
               H.tag_problems("XX", ["- [PART] half of it shipped"]))
    # A well-formed PART is silent.
    assert not [p for p in H.tag_problems("XX", ["- [PART] shipped — residual: the sweep"])
                if 'residual' in p and 'not name' in p]


def test_stale_items_age_out_on_last_activity_not_first():
    # MIN would misdate an old item carrying recent follow-on notes.
    revived = "- [OPEN] filed 2026-05-01, follow-on note 2026-07-20"
    assert H.classify(revived, CUTOFF)[0] == 'live'
    assert H.classify("- [OPEN] filed 2026-05-01", CUTOFF)[0] == 'stale'


def test_archive_names_carry_a_range_with_exactly_one_open_document():
    items = [(f"- [DONE] item {i}\n\n" + ("filler " * 900), datetime.date(2026, 5, i + 1))
             for i in range(8)]
    docs = H.paginate_archive(items, "# head", "HANDOFF_XX_archive", "XX")
    names = [n for n, _ in docs]
    assert sum(n.endswith('_open.md') for n in names) == 1, names
    assert any('_index.md' in n for n in names)
    ranges = [n for n in names if not n.endswith(('_open.md', '_index.md'))]
    assert ranges, "expected at least one closed range document"
    for n in ranges:                       # e.g. HANDOFF_XX_archive_2026-05-01_2026-05-04.md
        assert n.count('2026-') == 2, n


def test_documents_respect_the_ten_thousand_token_cap():
    items = [(f"- [DONE] item {i}\n\n" + ("filler " * 900), datetime.date(2026, 5, i + 1))
             for i in range(8)]
    for name, content in H.paginate_archive(items, "# head", "HANDOFF_XX_archive", "XX"):
        if name.endswith('_index.md'):
            continue
        assert H.tokens(content) <= H.MAX_TOKENS, (name, H.tokens(content))


def test_archive_index_lists_every_item_exactly_once():
    items = [(f"- [DONE] item {i}", datetime.date(2026, 5, i + 1)) for i in range(5)]
    docs = dict(H.paginate_archive(items, "# head", "HANDOFF_XX_archive", "XX"))
    index = docs["HANDOFF_XX_archive_index.md"]
    for i in range(5):
        assert f"item {i}" in index, i


def test_tokens_counts_characters_not_bytes():
    # A byte count overstates unicode-heavy files, and every cap in this repo is chars//4.
    assert H.tokens("✅" * 4) == 1


# ── executive-summary drift (ED-IN-0088) ─────────────────────────────────────────────

def test_summary_drift_catches_a_stale_count_and_a_stale_date():
    """The summary is AUTHORED, not generated — deliberately. The cost of that choice is that it
    decays undetectably: items close, new ones land, and the paragraph a reader trusts most quietly
    stops describing the file under it. So it carries two recomputable facts and this reports when
    either diverges — human judgement kept, decay made observable."""
    live = ["- [OPEN] a thing 2026-07-28", "- [OPEN] another thing"]
    stale = H.summary_drift('XX', 'Lane holds 3 live items as of 2026-07-01.', live, {})
    assert any('says 3 live item(s); the file has 2' in p for p in stale)
    assert any('predates its own contents' in p for p in stale)


def test_summary_drift_is_silent_when_the_summary_is_accurate():
    """Both directions: a guard that always fires is noise, and noise is what gets ignored."""
    live = ["- [OPEN] a thing 2026-07-28", "- [OPEN] another thing"]
    assert H.summary_drift('XX', 'Lane holds 2 live items as of 2026-07-28.', live, {}) == []


def test_summary_with_no_checkable_fact_is_reported_as_uncheckable():
    """A summary asserting nothing recomputable cannot drift — because it never said anything. That
    is the failure mode this guard exists for, so silence would be the wrong answer."""
    problems = H.summary_drift('XX', 'Lane is in reasonable shape.', ["- [OPEN] a thing"], {})
    assert any('states no live-item count' in p for p in problems)


def test_the_drift_guard_is_actually_WIRED_into_the_atomizer():
    """Guards the wiring, not just the function. A checker nobody calls is dead data — the exact
    defect class this session spent its time removing, and a mutation deleting the call site
    survived every assertion above until this test existed."""
    import inspect
    src = inspect.getsource(H)
    assert 'problems.extend(summary_drift(' in src, (
        "summary_drift() is defined but never called — the executive summary can drift silently "
        "again, which is the whole thing it was added to prevent.")
