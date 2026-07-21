"""Tests for the canonical-identifier tag-normalizer (tools/tag_normalizer.py) — the
Reconciliation Program §3 keystone: the ONE utility every prose-consuming tool calls to
strip/resolve ``[[id]]`` tags, so a tag reads identically everywhere (CLAUDE.md §8).

Pinned against an EXISTING names_index entry (attr.body.strength -> "Strength") so these do
not depend on the conv.* seed added in the same slice.
"""
import importlib.util
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_SCRIPT = os.path.join(_ROOT, 'tools', 'tag_normalizer.py')


def _load():
    spec = importlib.util.spec_from_file_location('tag_normalizer', _SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


tn = _load()


def test_reuses_the_real_names_reader():
    # §8: resolve_id must go through tools/names.py, not a private parse.
    import names
    assert tn.names is names
    assert tn.resolve_id('attr.body.strength') == names.canonical('attr.body.strength') == 'Strength'


def test_find_tags_bare_override_and_none():
    assert tn.find_tags('no tags here') == []
    (t,) = tn.find_tags('the [[attr.body.strength]] check')
    assert t.id == 'attr.body.strength' and t.override is None
    (t2,) = tn.find_tags('call it [[attr.mind.will|Grit]] today')
    assert t2.id == 'attr.mind.will' and t2.override == 'Grit'
    assert len(tn.find_tags('[[a.b]] and [[c.d]] and [[e.f]]')) == 3


def test_render_resolves_known_and_preserves_inflection():
    # bare known id -> canonical display; adjacent inflection text untouched (the [[id]]'s form)
    assert tn.render("raise [[attr.body.strength]]'s die") == "raise Strength's die"
    # override wins even when the id is unknown
    assert tn.render('the [[zzz.nope|Fancy Name]] axis') == 'the Fancy Name axis'


def test_render_unknown_policies():
    txt = 'the [[zzz.unknown_id]] axis'
    assert tn.render(txt, unknown='keep') == 'the [[zzz.unknown_id]] axis'      # default: surfaced
    assert tn.render(txt, unknown='humanize') == 'the unknown id axis'          # tail humanized
    assert tn.render(txt, unknown='raw') == 'the zzz.unknown_id axis'


def test_strip_resolves_known_keeps_unknown_raw():
    # a scanner sees human text for known ids, and an unresolved id stays visible (not laundered)
    s = tn.strip('[[attr.body.strength]] vs [[zzz.bogus]]')
    assert s == 'Strength vs [[zzz.bogus]]'


def test_unknown_tags_and_has_tags():
    assert tn.has_tags('x [[a.b]] y') is True
    assert tn.has_tags('no brackets') is False
    assert tn.unknown_tags('[[attr.body.strength]] and [[zzz.bogus]] and [[qqq.also]]') == [
        'qqq.also', 'zzz.bogus']   # sorted, known one excluded


def test_stray_open_brackets_is_the_collision_lint():
    # a well-formed tag is NOT stray (every `[[` that appears opens a valid tag)
    assert tn.stray_open_brackets('clean [[attr.body.strength]] tag') == []
    assert tn.is_collision_free('clean [[attr.body.strength]] tag') is True
    # a bare `[[` that never closes as a tag IS stray — the migration precondition surface
    assert tn.stray_open_brackets('a raw [[ bracket that never closes') != []
    assert tn.is_collision_free('a raw [[ bracket that never closes') is False
