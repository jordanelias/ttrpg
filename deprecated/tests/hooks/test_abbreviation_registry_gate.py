"""Tests for valoria_hooks.abbreviation_registry_gate (Level-4 acronym one-owner gate).

Added 2026-06-04. The gate enforces references/name_collision_database.yaml's
"one abbreviation, one owner" rule on definitional "Name (ACR)" patterns.
"""
import os, sys
import pytest

_SCRIPTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                        "skills", "valoria-orchestrator", "scripts"))
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

import valoria_hooks as vh
G  = vh.abbreviation_registry_gate
RP = vh.ABBREV_REGISTRY_PATH

REGISTRY = """abbreviations:
  CI: {term: "Church Influence", status: enforced}
  CR: {term: "Church Influence", status: recorded}
deprecated:
  - "Theocracy Counter (TC)"
"""

def _run(doc_path, doc, registry=REGISTRY):
    # registry supplied via the commit's additions (gate prefers commit version)
    return G([(RP, registry), (doc_path, doc)])

def test_enforced_owner_violation_halts():
    with pytest.raises(RuntimeError):
        _run("designs/x.md", "Crown Index (CI) climbs each season.")

def test_co_location_escapes():
    # owner term present in file -> rename/meta doc, allowed
    _run("designs/x.md", "Church Influence (CI) and the legacy Crown Index (CI).")

def test_recorded_status_soft_warns_not_halts():
    _run("designs/x.md", "Some Other Term (CR) appears.")

def test_deprecated_abbreviation_halts():
    with pytest.raises(RuntimeError):
        _run("designs/x.md", "The old Theocracy Counter (TC) value.")

def test_unregistered_soft_warns_not_halts():
    _run("designs/x.md", "A Brand New Thing (NTX) here.")

def test_exempt_prefix_skipped():
    _run("tests/fixtures.md", "Crown Index (CI) used as a fixture.")

def test_bare_acronym_does_not_fire():
    # no definitional parenthetical -> no halt, no concern
    _run("designs/x.md", "CI rose to 60 and IP fell this season.")

def test_missing_registry_is_bootstrap_safe():
    # no registry in additions and none on disk at RP -> silent skip, no raise
    cwd = os.getcwd()
    try:
        os.chdir("/tmp")
        G([("designs/x.md", "Crown Index (CI).")])
    finally:
        os.chdir(cwd)
