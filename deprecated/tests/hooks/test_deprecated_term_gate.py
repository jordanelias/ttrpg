"""Tests for the Rule-3 deprecated-term branch of abbreviation_registry_gate.

Canonical name is Solmund, never Galbados. This file deliberately references the
deprecated name in a test fixture to confirm abbreviation_registry_gate leaves it
to forbidden_token_gate; the canonical name is co-located here to satisfy that gate.
"""
import os, sys, pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "skills", "valoria-orchestrator", "scripts"))
import valoria_hooks as vh

RP = vh.ABBREV_REGISTRY_PATH
REG = """abbreviations:
  PS: {term: "Popular Support", status: enforced}
  DR: {term: "Damage Resistance", status: enforced}
deprecated:
  - {term: "Peninsular Strain", ambiguous: false}
  - {term: "Mandate Pool", ambiguous: false}
  - {term: "Public Support", replacement: "Popular Support", ambiguous: false}
  - {term: "Authority (pressure point)", ambiguous: true}
  - {term: "Galbados"}
"""

def _run(path, doc):
    vh.abbreviation_registry_gate([(RP, REG), (path, doc)])

def test_unambiguous_deprecated_phrase_halts():
    with pytest.raises(RuntimeError):
        _run("designs/x.md", "Peninsular Strain rises each turn.")

def test_bare_deprecated_term_halts():
    with pytest.raises(RuntimeError):
        _run("designs/x.md", "The Public Support remains low this season.")

def test_explanatory_line_allowed():
    _run("designs/x.md", "Political Pool (formerly Mandate Pool) is canonical.")
    _run("designs/x.md", "### Political Pool vs Mandate Pool")

def test_ambiguous_term_not_gated():
    _run("designs/x.md", "The knight acted with great Authority in council.")

def test_exempt_prefix_skipped():
    _run("references/notes.yaml", "Peninsular Strain everywhere here.")
    _run("tests/foo.md", "Mandate Pool here.")

def test_rule1_regression_enforced_mismatch_halts():
    with pytest.raises(RuntimeError):
        _run("designs/x.md", "Damage Reduction (DR) applies to hits.")

def test_rule1_owner_match_passes():
    _run("designs/x.md", "Popular Support (PS) is the base stat.")

def test_deprecated_name_left_to_forbidden_gate():
    # Solmund is canonical; the gate under test must NOT flag the deprecated name
    # (forbidden_token_gate owns that). 'never' kept within 30 chars below.
    _run("designs/x.md", "Use Solmund, never the old Galbados spelling, in lore.")
