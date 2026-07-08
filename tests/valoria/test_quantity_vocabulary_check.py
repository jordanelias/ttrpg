"""Tests for tools/quantity_registry.py + tools/ci_quantity_vocabulary_check.py
— the A17 stat-vocabulary closure checker (extension §3.1, ED-IN-0029; the
mechanical rows OPT-AV-4/16 this tool executes, not the doc's still-open
design-naming forks).

Fixture-based: builds a small descriptor_registry.yaml + names_index.yaml on
disk (tmp_path) so tests never depend on the live corpus's current backlog
(which is expected to change as the registry gains entries), styled like
tests/contracts/test_contract_adjudicator.py.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import quantity_registry  # noqa: E402
from ci_quantity_vocabulary_check import check, scan_module_contracts, scan_sim_literals  # noqa: E402

DESCRIPTOR_FIXTURE = """
attributes:
  scale: "1-7"
  default: 1
  body:
    - {key: attr.body.strength, name: Strength, aliases: []}
  mind: []
  social: []
aggregates:
  entries: []
faction_stats:
  entries:
    - {key: fac.wealth, name: Wealth}
by_reference: []
not_descriptors:
  derived_values: [Health]
  tracks: [Piety]
  clocks: []
  pools: []
"""

NAMES_INDEX_FIXTURE = """
entries:
  clock.church_influence:
    canonical: Church Influence
    aliases: []
    legacy: ["Theocracy Counter"]
"""


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return str(p)


# -- quantity_registry --------------------------------------------------------

def test_resolves_direct_registry_key_name(tmp_path):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    matched, key = quantity_registry.resolve("Strength", d, n)
    assert matched == "Strength" and key == "attr.body.strength"


def test_resolves_names_index_canonical(tmp_path):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    matched, key = quantity_registry.resolve("Church Influence", d, n)
    assert matched == "Church Influence" and key == "clock.church_influence"


def test_resolves_not_descriptors_name_with_no_key(tmp_path):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    matched, key = quantity_registry.resolve("Health", d, n)
    assert matched == "Health" and key is None


def test_resolves_via_parenthetical_and_suffix_normalization(tmp_path):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    # "Piety Track" -> strip " Track" suffix -> "Piety" (a not_descriptors track)
    assert quantity_registry.resolves("Piety Track", d, n)
    # "CV (Piety)" -> parenthetical content "Piety" resolves
    assert quantity_registry.resolves("CV (Piety)", d, n)


def test_unresolvable_name_returns_none(tmp_path):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    matched, key = quantity_registry.resolve("TotallyMadeUpStat", d, n)
    assert matched is None and key is None


# -- ci_quantity_vocabulary_check ---------------------------------------------

def test_scan_module_contracts_splits_bundled_names():
    contracts = {
        "modules": [{
            "module": "m1",
            "state": [{"name": "Prosperity / Defense / Order", "bucket": "track"}],
            "derivations": [{"output": "Health", "inputs": ["Strength", "Endurance"],
                              "formula": "f(x)"}],
        }]
    }
    found = list(scan_module_contracts(contracts))
    state_hits = [f for f in found if f[0] == "state"]
    assert len(state_hits) == 3  # Prosperity, Defense, Order
    assert {c for _, _, _, c in state_hits} == {"Prosperity", "Defense", "Order"}


def test_scan_sim_literals_finds_literal_string_keys(tmp_path):
    sim_dir = tmp_path / "sim"
    sim_dir.mkdir()
    (sim_dir / "example.py").write_text(
        'x = Target(actor_id="a", role="subject", '
        'stat_deltas={"Strength": 1, "MadeUp": 2})\n',
        encoding="utf-8",
    )
    hits = list(scan_sim_literals(str(sim_dir)))
    names = {h[3] for h in hits}
    assert names == {"Strength", "MadeUp"}


def test_scan_sim_literals_skips_variable_keys(tmp_path):
    sim_dir = tmp_path / "sim"
    sim_dir.mkdir()
    (sim_dir / "example.py").write_text(
        "x = Target(stat_deltas={er.affected_stat: er.delta})\n", encoding="utf-8"
    )
    assert list(scan_sim_literals(str(sim_dir))) == []


def test_check_reports_unresolved_and_resolved_counts(tmp_path, monkeypatch):
    d = _write(tmp_path, "descriptor_registry.yaml", DESCRIPTOR_FIXTURE)
    n = _write(tmp_path, "names_index.yaml", NAMES_INDEX_FIXTURE)
    # Point quantity_registry at the fixture files for this test only.
    monkeypatch.setattr(quantity_registry, "DESCRIPTOR_PATH", d)
    monkeypatch.setattr(quantity_registry, "NAMES_INDEX_PATH", n)
    monkeypatch.setattr(quantity_registry, "_cache", None)

    sim_dir = tmp_path / "sim"
    sim_dir.mkdir()
    (sim_dir / "example.py").write_text(
        'stat_deltas={"Strength": 1, "Unregistered": 2}\n', encoding="utf-8"
    )
    contracts = {
        "modules": [{
            "module": "m1",
            "state": [{"name": "Wealth", "bucket": "track"},
                      {"name": "NotInRegistry", "bucket": "track"}],
            "derivations": [],
        }]
    }
    resolved, findings = check(contracts, str(sim_dir))
    assert resolved == 2  # Strength, Wealth
    unresolved_ids = {f["identifier"] for f in findings}
    assert unresolved_ids == {"Unregistered", "NotInRegistry"}
    monkeypatch.setattr(quantity_registry, "_cache", None)
