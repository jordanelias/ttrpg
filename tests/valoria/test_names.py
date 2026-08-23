"""
Unit tests for the centralized names index and its readers.

Covers:
  * tools/names.py — the single loader/resolver (canonical/aliases/legacy/all_legacy/key_for),
    including fault-tolerant loading (missing file -> {} rather than raising).
  * tools/ci_naming_check.py — the hard gate now reads its forbidden names FROM the index
    (block-tier), and still flags the deprecated proper noun while honoring path exclusions.
  * tools/ci_naming_check.py --warn — the report-only drift lint flags warn-tier legacy names and
    names the canonical replacement.
"""
import os
import sys
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import names  # noqa: E402
import ci_naming_check  # noqa: E402


def _write_index(tmp_path):
    p = tmp_path / "names_index.yaml"
    p.write_text(textwrap.dedent("""
        version: 1
        entries:
          world.example:
            canonical: Canon
            aliases: [AliasOne, AliasTwo]
            legacy: [OldName]
            category: proper_noun
            enforce: block
          mech.thing:
            canonical: New Thing
            aliases: []
            legacy: [Stale Thing]
            category: mechanic
            enforce: warn
    """), encoding="utf-8")
    return str(p)


# ── names.py loader ──────────────────────────────────────────────────────────

def test_canonical_aliases_legacy(tmp_path):
    idx = _write_index(tmp_path)
    assert names.canonical("world.example", path=idx) == "Canon"
    assert names.aliases("world.example", path=idx) == ["AliasOne", "AliasTwo"]
    assert names.legacy("world.example", path=idx) == ["OldName"]
    assert names.canonical("does.not.exist", path=idx) is None


def test_all_legacy_filters_by_enforce(tmp_path):
    idx = _write_index(tmp_path)
    block = names.all_legacy(path=idx, enforce="block")
    assert block == [("OldName", "Canon", "world.example", "block")]
    warn = names.all_legacy(path=idx, enforce="warn")
    assert warn == [("Stale Thing", "New Thing", "mech.thing", "warn")]
    assert len(names.all_legacy(path=idx)) == 2


def test_key_for_resolves_canonical_and_alias(tmp_path):
    idx = _write_index(tmp_path)
    assert names.key_for("Canon", path=idx) == "world.example"
    assert names.key_for("AliasTwo", path=idx) == "world.example"
    assert names.key_for("Nope", path=idx) is None


def test_load_missing_file_never_raises():
    assert names.load(path="/no/such/names_index.yaml") == {}
    assert names.all_legacy(path="/no/such/names_index.yaml") == []


# ── ci_naming_check reads forbidden names from the real index ────────────────

def test_naming_gate_loads_block_tier_from_index():
    # The repo's names_index.yaml must yield at least the proper-noun invariant.
    assert ci_naming_check.FORBIDDEN, "no block-tier names loaded from names_index.yaml"
    legacy_names = [leg for (leg, _c, _k, _t) in names.all_legacy(enforce="block")]
    assert any(n.lower() == "galbados" for n in legacy_names)


def test_naming_gate_flags_deprecated_in_prose():
    hits = ci_naming_check.scan_text("designs/x.md", "The Galbados heresy spread")
    assert hits and "Galbados" in hits[0]


def test_naming_gate_respects_exclusions():
    # The index itself names the token by design; it must be exempt.
    assert ci_naming_check.scan_text("references/names_index.yaml", "Galbados") == []
    assert ci_naming_check.scan_text("designs/x.md", "Solmund is canonical") == []


# ── drift lint (warn-tier) — merged into ci_naming_check 2026-08-23 (S6/D2) ──

def test_drift_lint_flags_warn_legacy_with_canonical(tmp_path):
    idx = _write_index(tmp_path)
    matchers = []
    import re
    for leg, canon, key, _tier in names.all_legacy(path=idx, enforce="warn"):
        matchers.append((re.compile(r"\b" + re.escape(leg) + r"\b"), leg, canon, key))
    hits = ci_naming_check.scan_text_warn("designs/x.md", "We still track Stale Thing here", matchers)
    assert hits == [("Stale Thing", "New Thing", "We still track Stale Thing here")]


def test_drift_lint_against_real_index_clean_text():
    # A canonical mechanic name must not be flagged.
    assert ci_naming_check.scan_text_warn("designs/x.md", "Church Influence rises") == []


# ── D2: the merge must keep the two tiers apart (S6, 2026-08-23) ─────────────
#
# `ci_names_check.py` was folded into `ci_naming_check.py --warn`. The hazard of merging a
# report-only lint into a BLOCKING gate is that the tiers bleed: a warn-tier name starts blocking
# merges, or the block tier goes quiet. These pin the separation from the index side.

def test_the_two_tiers_do_not_bleed_into_each_other():
    """A warn-tier name must not be caught by the blocking scan, and vice versa."""
    warn_names = [leg for (leg, _c, _k, _t) in names.all_legacy(enforce="warn")]
    block_names = [leg for (leg, _c, _k, _t) in names.all_legacy(enforce="block")]
    assert warn_names and block_names, "one tier is empty — this test would pass vacuously"

    for leg in warn_names:
        assert ci_naming_check.scan_text("designs/x.md", f"we still say {leg} here") == [], (
            f'warn-tier name {leg!r} is being caught by the BLOCKING scan — a report-only '
            f'drift term would now fail the build')
    for leg in block_names:
        assert ci_naming_check.scan_text("designs/x.md", f"we still say {leg} here"), (
            f'block-tier name {leg!r} is no longer caught by the blocking scan')
        assert ci_naming_check.scan_text_warn("designs/x.md", f"we still say {leg} here") == [], (
            f'block-tier name {leg!r} leaked into the warn tier, which is report-only — the '
            f'invariant would stop blocking anything')


def test_an_empty_tier_means_different_things_and_the_code_says_so():
    """The one deliberate asymmetry in the merge, asserted on BEHAVIOUR.

    An empty BLOCK tier is a broken index — a gate that cannot match anything must never report
    clean — so `main` returns 1 on it. An empty WARN tier is the legitimate end state (every entry
    triaged and promoted), so the drift lint returns 0. But an UNREADABLE index also presents as an
    empty warn tier, and `names.all_legacy` returns {} for a missing PyYAML, an open failure, a
    parse failure and a non-dict root alike — so the warn tier must consult the block tier before
    it may call emptiness legitimate.

    ⚠ REWRITTEN after an adversarial pass. The first version asserted on SOURCE TEXT
    (`inspect.getsource(main)` contains "if not FORBIDDEN:"). That could not observe its own
    failure: flipping the fail-safe's `return 1` to `return 0` leaves the string in place and the
    blocking gate silently reports clean on an unreadable index — the exact defect it claimed to
    guard — while going red on a behaviour-preserving rename. §0.1 pt 2: an assertion that cannot
    observe the failure it excludes is not a weak test, it is an absent one.
    """
    real_matchers, real_forbidden = ci_naming_check.matchers_for, ci_naming_check.FORBIDDEN
    try:
        # (1) unreadable index — nothing loads at either tier. BOTH tiers must refuse.
        ci_naming_check.matchers_for = lambda tier: []
        ci_naming_check.FORBIDDEN = ()
        assert ci_naming_check.main([]) == 1, (
            "the BLOCK tier reported clean with no matchers loaded — a gate that cannot match "
            "anything must never pass")
        assert ci_naming_check._main_warn('staged') == 1, (
            "the WARN tier called an UNREADABLE index 'no warn-tier legacy names' — it cannot "
            "tell an unreadable index from a triaged-empty one")

        # (2) legitimate end state — the index loaded, the warn tier is genuinely empty.
        ci_naming_check.FORBIDDEN = real_forbidden
        ci_naming_check.matchers_for = (
            lambda tier: [] if tier == 'warn' else real_matchers('block'))
        assert ci_naming_check._main_warn('staged') == 0, (
            "an empty warn tier is the END STATE (all entries promoted to block) and must be "
            "clean, not an error")
    finally:
        ci_naming_check.matchers_for, ci_naming_check.FORBIDDEN = real_matchers, real_forbidden


def test_the_hook_still_gets_strings_from_the_block_scan():
    """`tools/hook_naming_guard.py` slices each hit as a string (`h[:120]`). The merge introduced
    a richer (legacy, canonical, line) shape for the warn tier; widening the block tier's return
    to match would have broken the edit-time hook silently — it would print tuple reprs."""
    hits = ci_naming_check.scan_text("designs/x.md", "The Galbados heresy spread")
    assert hits and isinstance(hits[0], str), f"block-tier scan returned {type(hits[0])}, not str"

    # ...and ONE HIT PER LINE, not one per matching pattern. `_scan` yields per-pattern because the
    # warn tier must name which term it found; the block tier's pre-merge `any()` yielded per-line.
    # Identical with one block-tier name, divergent with two — so this plants the second name rather
    # than waiting for someone to promote one (CLAUDE.md §0.1 pt 2: an assertion must be able to
    # observe the failure it excludes).
    import re as _re
    two = ci_naming_check.matchers_for('block') + [
        (_re.compile(r'\bPlantedLegacyName\b', _re.I), 'PlantedLegacyName', 'Canonical', 'k')]
    _orig = ci_naming_check.matchers_for
    ci_naming_check.matchers_for = lambda tier: two if tier == 'block' else _orig(tier)
    try:
        both = ci_naming_check.scan_text("designs/x.md", "Galbados and PlantedLegacyName")
    finally:
        ci_naming_check.matchers_for = _orig
    assert both == ["Galbados and PlantedLegacyName"], (
        f"one line matching two block-tier names produced {len(both)} hits, not 1 — the violation "
        f"count in `[NAMING VIOLATIONS: N]` now double-counts and the edit-time hook's five-hit "
        f"budget is spent on duplicates: {both}")


def test_the_audit_exclusion_is_ROOTED_not_a_substring():
    """`audit/` must exempt the audit corpus and NOT `skills/valoria-vector-audit/scripts/`.

    `is_excluded` is a substring test, so a bare `'audit/'` entry silently exempted every
    vector-audit script from this BLOCKING gate. That is the ED-IN-0133 unanchored-substring
    defect, and `tools/pathres.py`'s docstring uses this exact collision as its worked example —
    the lesson was written down in one tool while the other kept the bug.

    The second half is the part that makes this worth pinning: `tests/` must STAY a substring, or
    the 28 files under `engine/tests/` lose an exemption they legitimately have. A fix that rooted
    every bare entry would have passed the first assertion and broken those.
    """
    assert not ci_naming_check.is_excluded('skills/valoria-vector-audit/scripts/vector_audit.py')
    assert ci_naming_check.is_excluded('audit/2026-08-17-weekly-review/00_findings.md')
    assert ci_naming_check.is_excluded('engine/tests/test_f7_smoke_oracle.py')
    assert ci_naming_check.is_excluded('tests/valoria/test_names.py')
