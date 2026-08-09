"""Guards for the generated glossary (ED-IN-0150).

Three of these pin defects the tool SHIPPED WITH and had to be fixed during the build. They are
here because each was silent — the tool ran green, printed a confident count, and was wrong:

  1. `descriptor_registry` read the wrong field names and contributed ZERO terms while still being
     advertised as one of five sources.
  2. `glossary.md`'s parser required >=4 columns and captured 31 of ~130 rows, because the file
     mixes 3-, 4- and 7-column tables.
  3. MIN_TERM_LEN=3 silently refused MS, CI, IP, PI, TS, CP, TD, RS, DD — the repo's nine most-used
     abbreviations, two of which (`TS`, `CI`) glossary.md's own usage rules name explicitly.

All three share one shape: a reader that quietly covers a fraction of its source. That is the same
class as a gate reporting clean over nothing, which this repo found three times in one week.
"""
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'references' / 'glossary'
sys.path.insert(0, str(ROOT / 'tools' / 'observability'))
import build_glossary as bg  # noqa: E402


@pytest.fixture(scope='module')
def payload():
    p = OUT / 'glossary.json'
    if not p.exists():
        pytest.skip('glossary not generated')
    return json.loads(p.read_text())


def test_every_declared_source_contributes_terms():
    """DEFECT 1. A source that reads nothing must fail loudly, not pad the source list."""
    sources = {
        'names_index': bg._from_names_index(),
        'glossary.md': bg._from_glossary_md(),
        'identifier_census': bg._from_identifier_census(),
        'mechanics_index': bg._from_mechanics_index(),
        'descriptor_registry': bg._from_descriptor_registry(),
    }
    dead = sorted(n for n, v in sources.items() if not v)
    assert not dead, (
        f'declared source(s) contributed zero terms: {dead}. Either the registry moved or the '
        'reader is looking at the wrong fields — do not ship a source that reads nothing.'
    )
    # and the guard itself must fire, not just the condition hold
    with pytest.raises(SystemExit):
        bg._assert_every_source_contributes({'fake_source': 0})


def test_the_glossary_md_parser_reads_three_column_tables():
    """DEFECT 2. The file mixes column counts; a >=4-column parser reads a quarter of it."""
    terms = bg._from_glossary_md()
    # `Mandate` lives in a 3-column table (Full Term | Abbr used in tables | Description)
    assert 'Mandate' in terms, '3-column glossary rows are not being parsed'
    assert terms['Mandate'].get('definition'), 'parsed the term but dropped its definition'
    assert len(terms) > 60, (
        f'only {len(terms)} terms parsed from glossary.md — the parser has narrowed again; '
        'it read 31 of ~130 rows before the column-count fix'
    )


def test_the_core_abbreviations_are_not_refused(payload):
    """DEFECT 3. MS/CI/TS/RS are load-bearing project vocabulary, not noise."""
    refused = {r['term'] for r in payload['refused']}
    for abbr in ('MS', 'CI', 'TS', 'RS'):
        assert abbr not in refused, f'{abbr} refused — see MIN_TERM_LEN'
        assert abbr in payload['terms'], f'{abbr} missing from the glossary entirely'


def test_two_char_lowercase_terms_are_still_refused():
    """The floor was lowered to 2 for UPPERCASE only. Lowercase 2-char terms match unsafely."""
    kept, refused = bg.collect_terms()
    bad = [t for t in kept if len(t) == 2 and not t.isupper()]
    assert not bad, f'unsafe 2-char lowercase terms admitted: {bad}'


def test_matching_is_word_boundary_and_case_sensitive():
    """The Mode-C hazard: substring matching turns common nouns into universal hits."""
    hits = bg.scan_locations({'CI': {}, 'Mind': {}})
    # 'CI' must not be matching inside 'specific'/'decision'; if it were, it would be near-universal
    assert hits['CI'], 'CI matched nothing at all — the scan is broken'
    total_md = sum(1 for r in bg.SCAN_ROOTS for _ in (ROOT / r).rglob('*.md')
                   if (ROOT / r).exists())
    assert len(hits['CI']) < total_md * 0.5, (
        'CI matches more than half the corpus — matching has become substring-based, which is the '
        'defect that made the vector audit report 97.5% of edges as notional'
    )


def test_broad_terms_are_flagged_not_hidden(payload):
    """Breadth is reported. A term in 144 files is a fact about the term, not something to bury."""
    flagged = [t for t, e in payload['terms'].items() if e.get('ambiguous')]
    assert flagged, 'nothing flagged broad — the ambiguity signal has gone inert'
    for t in flagged:
        assert payload['terms'][t]['file_count'] > payload['ambiguity_floor']


def test_every_located_term_carries_its_locations(payload):
    """The master's promise is 'all locations'. An empty location map breaks it."""
    for term, e in payload['terms'].items():
        if e['file_count']:
            assert e['locations'], f'{term} claims {e["file_count"]} files but lists none'
            assert len(e['locations']) == e['file_count'], f'{term} file_count disagrees with locations'


def test_committed_output_matches_a_fresh_build():
    """The artifact is generated; a stale commit is a lie about the corpus."""
    files, fresh = bg.build()
    for name, body in files.items():
        p = OUT / name
        assert p.exists(), f'{name} missing — re-run tools/observability/build_glossary.py'
        assert p.read_text() == body, f'{name} is stale — re-run the generator'
    assert (OUT / 'glossary.json').exists()
    committed = json.loads((OUT / 'glossary.json').read_text())
    assert committed['counts'] == fresh['counts'], 'glossary.json is stale'


def test_no_js_bundle_is_emitted():
    """Dropped deliberately (Jordan, 2026-08-08): it duplicated glossary.json byte-for-byte and
    nothing in dashboard/ loads any *_data.js bundle. Re-adding one needs a reader first."""
    assert not (OUT / 'glossary_data.js').exists(), (
        'a JS bundle reappeared. It duplicates glossary.json exactly; add a consumer before '
        'adding the file back.'
    )


def test_substring_prefilter_matches_regex_only():
    """The scan pre-rejects with `term not in text` before running the \\b-anchored regex.

    That is a pure speed optimisation (~160s -> ~10s) and MUST NOT change results: `in` cannot
    produce a false negative for a word-boundary pattern built from the same literal. Verified
    against a regex-only scan over a real slice of the corpus rather than asserted.
    """
    import re as _re
    terms = ['Mandate', 'CI', 'Stamina', 'Coherence', 'Threadwork']
    patterns = {t: _re.compile(r'\b' + _re.escape(t) + r'\b') for t in terms}

    files = sorted((ROOT / 'systems').rglob('*.md'))[:60]
    assert files, 'no corpus slice to check against'

    regex_only, prefiltered = {}, {}
    for p in files:
        text = p.read_text(errors='ignore')
        rel = p.relative_to(ROOT).as_posix()
        for t, rx in patterns.items():
            n = len(rx.findall(text))
            if n:
                regex_only.setdefault(t, {})[rel] = n
            if t in text:
                m = len(rx.findall(text))
                if m:
                    prefiltered.setdefault(t, {})[rel] = m
    assert regex_only == prefiltered, (
        'the substring pre-filter changed the result set — it must be a speed optimisation only'
    )
