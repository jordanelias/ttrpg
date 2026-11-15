"""The season's registries are exported to `engine/engine_params/season_registries.json`, with a
blocking round trip (GO-09, B03g.01).

`tools/export_season_registries.py` parses every YAML a loader under `engine/season/data/` opens, with
the loader's own parser (`rosters.load_yaml`, which refuses a duplicate key), and writes the parsed
documents losslessly. These tests are the falsifiers (CLAUDE.md §0.1 pt 3): each one can observe the
failure it excludes.

* a key deleted from the JSON reds `--check`;
* a row added to `verb_table.yaml` without a re-export reds it;
* CONTROL: the loader run over the JSON's document equals the loader run over the YAML, for every
  exported file, and the loop asserts that it ran (`checked >= 7`).
"""
import copy
import json
import os
import sys
import tempfile
from pathlib import Path

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)

import export_season_registries as esr  # noqa: E402
from engine.season.data.rosters import load_yaml  # noqa: E402

VERB_TABLE = 'engine/season/verb_table.yaml'


def _artifact():
    return json.loads(Path(esr.OUT).read_text(encoding='utf-8'))


def _delete_one_key(node):
    """Delete the first mapping key found, depth first; return True once one is gone."""
    if isinstance(node, dict):
        for k in list(node):
            if isinstance(node[k], (dict, list)) and _delete_one_key(node[k]):
                return True
        if node:
            del node[next(iter(node))]
            return True
    elif isinstance(node, list):
        for item in node:
            if _delete_one_key(item):
                return True
    return False


def test_season_registries_current():
    assert esr.main(['--check']) == 0


def test_a_deleted_key_reds_the_check(tmp_path):
    art = _artifact()
    assert _delete_one_key(art['files'][VERB_TABLE]), 'nothing to delete: the control cannot observe'
    mutated = tmp_path / 'season_registries.json'
    mutated.write_text(json.dumps(art, indent=2, sort_keys=False) + '\n', encoding='utf-8')
    assert esr.main(['--check'], out=str(mutated)) == 1
    # the control: the same logic over the untouched artifact is green, so the red was the deletion
    intact = tmp_path / 'intact.json'
    intact.write_text(json.dumps(_artifact(), indent=2, sort_keys=False) + '\n', encoding='utf-8')
    assert esr.main(['--check'], out=str(intact)) == 0


def test_a_registry_row_added_without_a_reexport_reds_the_check(tmp_path):
    import yaml
    text = (Path(ROOT) / VERB_TABLE).read_text(encoding='utf-8')
    doc = load_yaml(text)
    assert isinstance(doc['verbs'], list) and doc['verbs'], 'verb_table.yaml carries no verbs to copy'
    # one verb row appended to `verbs:`, as an author adding one would, and no re-export
    grown = copy.deepcopy(doc)
    row = copy.deepcopy(grown['verbs'][0])
    row['verb'] = 'zz_a_verb_nobody_exported'
    grown['verbs'].append(row)
    copy_path = tmp_path / 'verb_table.yaml'
    copy_path.write_text(yaml.safe_dump(grown, sort_keys=False), encoding='utf-8')
    assert load_yaml(copy_path.read_text(encoding='utf-8')) == grown, 'the dump lost more than the appended row'
    assert load_yaml(copy_path.read_text(encoding='utf-8')) != doc, 'the appended row changed nothing: blind'
    assert esr.main(['--check'], overrides={VERB_TABLE: copy_path}) == 1
    # the control: the tool pointed at an unmodified copy of the same file is green
    clean = tmp_path / 'clean_verb_table.yaml'
    clean.write_text(text, encoding='utf-8')
    assert esr.main(['--check'], overrides={VERB_TABLE: clean}) == 0


def test_the_loader_over_the_json_equals_the_loader_over_the_yaml():
    art = _artifact()
    checked = 0
    for rel, parsed in art['files'].items():
        text = (Path(ROOT) / rel).read_text(encoding='utf-8')
        assert load_yaml(text) == parsed, f'{rel}: the loader over the YAML differs from the artifact'
        checked += 1
    assert checked >= 7, f'only {checked} file(s) compared: the control asserted too little'
    assert checked == len(art['files'])


def test_sources_names_every_registry_a_data_loader_reads():
    """`SOURCES` is a hand list; a loader under `engine/season/data/` that reads a further `files.*_YAML`
    would leave it out of the artifact the port reads. The set the loaders read is derived from their text."""
    import re
    read = set()
    for f in sorted((Path(ROOT) / 'engine' / 'season' / 'data').glob('*.py')):
        if f.name != 'files.py':
            read |= set(re.findall(r'\b([A-Z][A-Z_]*_YAML)\.read_text', f.read_text(encoding='utf-8')))
    assert len(read) >= 7, f'only {len(read)} registry read(s) found: the derivation went blind'
    assert read == set(esr.SOURCES), (sorted(read - set(esr.SOURCES)), sorted(set(esr.SOURCES) - read))


def test_a_value_json_would_coerce_is_refused_naming_the_file(tmp_path):
    # a date key and an integer key are what an author adding a YAML entry could write by accident
    for body, what in (("verbs:\n  - verb: x\n    2026-01-01: y\n", 'a date key'),
                       ("verbs:\n  - verb: x\n    1: y\n", 'an integer key')):
        bad = tmp_path / 'verb_table.yaml'
        bad.write_text(body, encoding='utf-8')
        try:
            esr.build(overrides={VERB_TABLE: bad})
        except ValueError as exc:
            assert VERB_TABLE in str(exc), f'{what}: refused, but not naming the file'
        else:
            raise AssertionError(f'{what} was exported instead of refused')
