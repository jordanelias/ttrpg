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
    """The one deliberate asymmetry in the merge.

    An empty BLOCK tier is a broken index — a gate that cannot match anything must never report
    clean — so `main` returns 1 on it. An empty WARN tier is the legitimate end state (every entry
    triaged and promoted), so the drift lint returns 0. Merging the two files made it easy to
    "tidy" that difference away; this is what would notice.
    """
    import inspect
    src = inspect.getsource(ci_naming_check.main)
    assert "if not FORBIDDEN:" in src, "the block tier's empty-matcher fail-safe is gone"
    warn_src = inspect.getsource(ci_naming_check._main_warn)
    assert "return 0" in warn_src.split("if not matchers:")[1][:200], (
        "the warn tier no longer treats an empty tier as clean")


def test_the_hook_still_gets_strings_from_the_block_scan():
    """`tools/hook_naming_guard.py` slices each hit as a string (`h[:120]`). The merge introduced
    a richer (legacy, canonical, line) shape for the warn tier; widening the block tier's return
    to match would have broken the edit-time hook silently — it would print tuple reprs."""
    hits = ci_naming_check.scan_text("designs/x.md", "The Galbados heresy spread")
    assert hits and isinstance(hits[0], str), f"block-tier scan returned {type(hits[0])}, not str"
