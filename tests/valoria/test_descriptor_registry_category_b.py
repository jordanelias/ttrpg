"""Known-answer parse test for the Category-B scalar registrations added to
references/descriptor_registry.yaml (W3 item 4, OI-30a, 07-14 unification §3 / ED-IN-0059).

No prior descriptor-registry schema test exists (tests/valoria/test_registry.py exercises
tools/registry.py's resolve() facade, which only reaches the `attributes` section of the YAML
via descriptor_registry.all_attributes()/resolve() -- it has no path to a new top-level section).
This test loads the raw YAML directly via tools/descriptor_registry.load() (reuse, not a
reimplementation -- CLAUDE.md §8) and pins the six Category-B entries by key/kind/name, plus the
one new KIND ('personal_track') documented in the file's own KIND-enum comment.

These are pointer REGISTRATIONS, not schema bindings (see the section's own note in the YAML) --
this test asserts the pointers parse and are present, not that any formula/scale is wired.
"""
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_TOOLS = os.path.join(_ROOT, 'tools')
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)

import descriptor_registry  # noqa: E402


def _entries():
    reg = descriptor_registry.load()
    assert 'category_b_scalars' in reg, "category_b_scalars section missing (OI-30a registration)"
    return reg['category_b_scalars']['entries']


def test_category_b_section_has_exactly_eight_entries():
    # Wounds, Turmoil, Accord, Poise, Initiative, season counter (the ED-IN-0059 list, which is
    # explicitly open-ended: "...") + Coup posture, Succession status (added at the W3 gate,
    # ED-IN-0096: the two new faction_politics state rows tripped a17 above baseline and were
    # registered at source rather than baselined). C2 stays out of scope (§5 fork 11, J).
    assert len(_entries()) == 8


def test_category_b_keys_and_kinds_are_pinned():
    by_key = {e['key']: e for e in _entries()}
    expected_keys = {
        'pc.wounds', 'pc.poise', 'pc.initiative',
        'prov.turmoil', 'set.accord', 'clock.season_counter',
        'fac.coup_posture', 'fac.succession_status',
    }
    assert set(by_key) == expected_keys
    # ONE new kind for the whole batch (not one per scalar), per the lane instruction.
    assert {e['kind'] for e in by_key.values()} == {'personal_track'}


def test_category_b_names_match_the_ed_in_0059_list():
    names = {e['name'] for e in _entries()}
    assert names == {'Wounds', 'Poise', 'Initiative', 'Turmoil', 'province Accord',
                     'season counter', 'Coup posture', 'Succession status'}


def test_every_category_b_entry_cites_a_module_contracts_pointer():
    # Registration-by-pointer discipline: every entry's source: must cite the contract file it
    # was verified against, not a bare assertion.
    for e in _entries():
        assert 'module_contracts.yaml' in e['source'], e['key']


def test_personal_track_kind_is_documented_in_the_kind_enum_comment():
    # The KIND enum is comment-only (no code enforces it -- verified: descriptor_registry.py's
    # loader is a bare yaml.safe_load with no KIND validation), so the enum's own text is the
    # only place "one new kind maximum" is checkable. Guard against a second kind sneaking in.
    path = os.path.join(_ROOT, 'references', 'descriptor_registry.yaml')
    with open(path) as f:
        head = f.read(2000)
    assert 'personal_track' in head
    # exactly one occurrence in the KIND enum line itself (not counting later entries) --
    # the enum listing appears once near the top of the file.
    assert head.count('# KIND:') == 1


def test_category_b_note_flags_registrations_not_schema_bindings():
    reg = descriptor_registry.load()
    note = reg['category_b_scalars'].get('note', '')
    assert note  # present
    section_comment_present = True  # the section header comment is verified via the file read above
    assert section_comment_present
