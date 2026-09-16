"""The naming chain's falsifier: `names_index.yaml` -> `export_names.py` -> `names.json` -> the leaf.

⚠ THIS FILE EXISTS BECAUSE AN ADVERSARIAL PASS FOUND THE CHAIN UNTESTED. The chain landed with five
mutations run by hand and reported in a commit message, which §0.1 pt 3 does not accept: a result
claim carries the test that would have shown it wrong. Worse, `engine/substrate/names.py`'s
`canonical_for()` had ZERO callers, so its three refusals were dead paths -- the module's whole
argument is that it raises instead of guessing, and nothing exercised a single raise.

Each test below plants a defect and asserts the refusal. Deleting a refusal reds this file.
"""
from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from engine.substrate import names as N  # noqa: E402


# ---------------------------------------------------------------------------
# THE LEAF'S REFUSALS. `canonical_for` raises rather than guessing; these are those raises.
# ---------------------------------------------------------------------------

def test_an_ambiguous_display_string_raises_instead_of_picking_one():
    """Three strings are claimed by two entries each. Resolving one would return whichever row the
    exporter met first, which is an answer with no basis -- so it refuses and names the claimants.

    ⚠ `Legitimacy` IS IN THIS LIST BECAUSE IT WAS MISSING. Jordan ruled on 2026-08-23 that it is a
    base faction stat; `descriptor_registry.yaml` gained `fac.legitimacy` and `names_index.yaml` did
    not, and `ci_names_consistency.py` only checks index -> registry. With no row, the collision was
    invisible and the leaf RESOLVED `Legitimacy` to the settlement stat. Found by an antagonist
    pass, fixed at the owner."""
    assert set(N.AMBIGUOUS) == {"Order", "Stability", "Legitimacy"}, (
        f"the ambiguous set changed: {sorted(N.AMBIGUOUS)}. A new entry means two rows started "
        "claiming one display string; a missing one means a row was removed or merged")
    for name, claimants in N.AMBIGUOUS.items():
        with pytest.raises(ValueError) as e:
            N.canonical_for(name)
        assert all(c in str(e.value) for c in claimants), (
            f"the refusal for {name!r} must name both claimants so the caller can pass a key")


def test_a_legacy_tag_raises_and_names_its_replacement():
    """A legacy tag is carried so a rename can be FINISHED, not so it keeps resolving. Resolving one
    silently is how a rename never lands -- the gate that exists for exactly this is
    `ci_naming_check.py`, and the leaf agrees with it rather than routing around."""
    assert N.LEGACY, "no legacy tags at all would make this test vacuous"
    tag, replacement = next(iter(N.LEGACY.items()))
    with pytest.raises(ValueError) as e:
        N.canonical_for(tag)
    assert replacement in str(e.value)


def test_an_unknown_name_raises_rather_than_passing_through():
    """The polarity `descriptors.resolve_conviction` uses, for its stated reason: a silent
    pass-through makes a wrong name indistinguishable from a right one at every later site."""
    with pytest.raises(ValueError) as e:
        N.canonical_for("NotAName")
    assert "names_index.yaml" in str(e.value), "the refusal must name the owner to edit"


def test_an_alias_and_a_key_and_a_canonical_all_resolve():
    """The three shapes that SHOULD resolve, so the refusals above are not passing vacuously."""
    assert N.canonical_for("Church") == "Church of Solmund"          # alias
    assert N.canonical_for("Church of Solmund") == "Church of Solmund"  # already canonical
    assert N.canonical_for("fac.influence") == "Influence"           # key
    assert N.canonical_for("RM") == "Restoration Movement"           # alias added 2026-09-16


def test_the_faction_roster_is_eight_and_the_season_loop_derives_it():
    """`rosters.yaml: factions` carries `from_names: faction` and no `values:`, so these are the
    same object rather than two lists that agree today. Schoenland is the eighth: its row is filed
    with the PLACES and lacked `token_class: faction` until 2026-09-16, so the alias map saw seven
    while the season roster carried eight."""
    from engine.season.data.rosters import FACTIONS
    assert set(N.FACTIONS) == set(FACTIONS), "the derived roster and the leaf disagree"
    assert len(N.FACTIONS) == 8
    assert "Schoenland" in N.FACTIONS and "Church of Solmund" in N.FACTIONS


# ---------------------------------------------------------------------------
# THE EXPORTER'S REFUSALS, each planted in a tmp copy of the authored index.
# ---------------------------------------------------------------------------

def _run_exporter_on(tmp_path: Path, doctor) -> subprocess.CompletedProcess:
    """Copy `names_index.yaml`, let `doctor` corrupt the text, and run the exporter against it.

    The exporter reads a module-level `SRC`, so the copy is injected by importing it and rebinding
    that constant in a subprocess -- which also keeps the real artifact untouched whatever happens.
    """
    src = (REPO / "references" / "names_index.yaml").read_text(encoding="utf-8")
    bad = tmp_path / "names_index.yaml"
    bad.write_text(doctor(src), encoding="utf-8")
    code = (
        f"import sys; sys.path.insert(0, {str(REPO / 'tools')!r});"
        f"import export_names as E; E.SRC = {str(bad)!r};"
        "import json; print(json.dumps(E.build())[:40])"
    )
    return subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=REPO)


def test_the_exporter_refuses_an_alias_that_resolves_to_two_canonicals(tmp_path):
    """The coin-flip case: one string, two answers, and whichever table you reach first wins."""
    def doctor(s):
        return s.replace(
            '  fac.wealth:     {canonical: Wealth,    aliases: []',
            '  fac.wealth:     {canonical: Wealth,    aliases: ["Church"]')
    r = _run_exporter_on(tmp_path, doctor)
    assert r.returncode != 0, f"exporter accepted a two-canonical alias: {r.stdout}"
    assert "resolves to BOTH" in (r.stdout + r.stderr)


def test_the_exporter_refuses_an_alias_that_shadows_a_canonical(tmp_path):
    """The `Influence` shape (ED-IN-0057), which is why this refusal exists: `Influence` was an
    alias of Charisma AND the canonical name of `fac.influence`, and the attribute won because it
    was checked first. Restoring that alias must now red the gate."""
    def doctor(s):
        return s.replace(
            "  attr.social.charisma:  {canonical: Charisma,   aliases: [Presence]",
            "  attr.social.charisma:  {canonical: Charisma,   aliases: [Presence, Influence]")
    r = _run_exporter_on(tmp_path, doctor)
    assert r.returncode != 0, f"exporter accepted a canonical-shadowing alias: {r.stdout}"
    assert "canonical name of" in (r.stdout + r.stderr)


def test_the_exporter_refuses_a_legacy_tag_that_is_also_a_live_alias(tmp_path):
    def doctor(s):
        return s.replace(
            '  fac.wealth:     {canonical: Wealth,    aliases: [], legacy: []',
            '  fac.wealth:     {canonical: Wealth,    aliases: ["Coin"], legacy: ["Coin"]')
    r = _run_exporter_on(tmp_path, doctor)
    assert r.returncode != 0, f"exporter accepted a legacy-and-alias tag: {r.stdout}"
    assert "BOTH legacy and alias" in (r.stdout + r.stderr)


def test_the_exporter_refuses_a_legacy_tag_that_shadows_a_canonical(tmp_path):
    """The fourth member of the family, found by an antagonist pass rather than by use. The leaf
    tests LEGACY before CANONICAL, so this would refuse a perfectly live name as deprecated."""
    def doctor(s):
        return s.replace(
            '  fac.wealth:     {canonical: Wealth,    aliases: [], legacy: []',
            '  fac.wealth:     {canonical: Wealth,    aliases: [], legacy: ["Military"]')
    r = _run_exporter_on(tmp_path, doctor)
    assert r.returncode != 0, f"exporter accepted a canonical-shadowing legacy tag: {r.stdout}"
    assert "canonical name" in (r.stdout + r.stderr)


def test_the_shipped_artifact_matches_the_authored_index():
    """`--check`'s round trip, asserted here too so a stale artifact fails the unit suite and not
    only the CI step -- the artifact is read at IMPORT by the leaf, so staleness is a wrong value at
    runtime rather than a drifted document."""
    r = subprocess.run([sys.executable, "tools/export_names.py", "--check"],
                       capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, f"names.json is stale — run tools/export_names.py\n{r.stdout}{r.stderr}"
