"""
Tests for the correctness-critical, pure-logic gates in valoria_hooks (+ the
handoff schema validator in github_ops).

Added 2026-05-31 as Lane B item 7.2 (hook test coverage). Before this, tests/hooks/
held only test_placeholder_names_gate.py against ~29 hook functions — the halting,
correctness-critical gates had no regression net. This file covers the gates that
are unit-testable without network (they take synthetic `additions`/strings and
raise on violation):

  - commit_message_gate     (commit format regex)
  - forbidden_token_gate    ("Solmund, never Galbados")
  - assert_unique_ids       (ID-collision guard — the ED-762 class)
  - jsonl_ledger_gate       (editorial_ledger.jsonl integrity)
  - sim_fabrication_check   (uncited mechanical constants in sim files)
  - _validate_handoff_schema (handoff dict schema; github_ops)

Network-dependent gates (safe_commit, task_gate, assert_bootstrap, context_gate)
are not covered here — they need fetch/commit mocking and are tracked separately.

Convention matches tests/hooks/test_placeholder_names_gate.py: sys.path.insert
'/home/claude' + import the module under test; pytest.raises for halts.
"""

import sys
import pytest

sys.path.insert(0, '/home/claude')
import valoria_hooks  # noqa: E402
import github_ops      # noqa: E402


# ─────────────────────────────────────────────────────────────────────────────
# commit_message_gate
# ─────────────────────────────────────────────────────────────────────────────

def test_commit_message_valid_scope_passes():
    valoria_hooks.commit_message_gate("[infrastructure] add hook tests for correctness gates")


def test_commit_message_fix_scope_passes():
    valoria_hooks.commit_message_gate("[fix] correct the freshness sync edge case")


def test_commit_message_no_scope_halts():
    with pytest.raises(RuntimeError, match="Bad commit message"):
        valoria_hooks.commit_message_gate("add some stuff without a scope tag")


def test_commit_message_unknown_scope_halts():
    with pytest.raises(RuntimeError, match="Bad commit message"):
        valoria_hooks.commit_message_gate("[bogus] a description of adequate length")


def test_commit_message_too_short_halts():
    # COMMIT_FORMAT requires >=10 chars after the scope tag.
    with pytest.raises(RuntimeError, match="Bad commit message"):
        valoria_hooks.commit_message_gate("[fix] short")


# ─────────────────────────────────────────────────────────────────────────────
# forbidden_token_gate  ("Solmund, never Galbados")
# ─────────────────────────────────────────────────────────────────────────────

def test_forbidden_token_absent_passes():
    # Rule (a): no forbidden token at all.
    valoria_hooks.forbidden_token_gate([('designs/world/x.md', 'Solveig rules the north.')])


def test_forbidden_token_with_canonical_name_passes():
    # Rule (b): canonical name (Solmund) co-located.
    valoria_hooks.forbidden_token_gate(
        [('designs/world/x.md', 'Note: the name was Galbados, now canonically Solmund.')]
    )


def test_forbidden_token_exception_phrase_nearby_passes():
    # Rule (c): "never" within 30 chars of the occurrence, and NO canonical name
    # present (so this isolates the exception-window path, not rule (b)).
    valoria_hooks.forbidden_token_gate(
        [('designs/world/x.md', 'The estate was never called Galbados.')]
    )


def test_forbidden_token_bare_halts():
    # Bare "Galbados", no Solmund, no "never" nearby -> halt.
    with pytest.raises(RuntimeError, match="forbidden_token_gate"):
        valoria_hooks.forbidden_token_gate([('designs/world/x.md', 'The lord Galbados marched south.')])


def test_forbidden_token_case_insensitive_halts():
    with pytest.raises(RuntimeError, match="forbidden_token_gate"):
        valoria_hooks.forbidden_token_gate([('designs/world/x.md', 'the GALBADOS estate')])


def test_forbidden_token_exempt_prefix_passes():
    # deprecated/archives/ is an exempt prefix even with a bare forbidden token.
    valoria_hooks.forbidden_token_gate([('deprecated/archives/old/x.md', 'historical: Galbados')])


# ─────────────────────────────────────────────────────────────────────────────
# assert_unique_ids  (ID-collision guard)
# ─────────────────────────────────────────────────────────────────────────────

def test_unique_ids_jsonl_unique_passes():
    content = '{"id": "ED-901"}\n{"id": "ED-902"}\n'
    valoria_hooks.assert_unique_ids([('canon/editorial_ledger.jsonl', content)])


def test_unique_ids_jsonl_duplicate_halts():
    content = '{"id": "ED-901"}\n{"id": "ED-901"}\n'
    with pytest.raises(RuntimeError, match="duplicate ID"):
        valoria_hooks.assert_unique_ids([('canon/editorial_ledger.jsonl', content)])


def test_unique_ids_patch_register_unique_passes():
    content = "- id: PP-761\n  status: open\n- id: PP-762\n  status: open\n"
    valoria_hooks.assert_unique_ids([('canon/patch_register_active.yaml', content)])


def test_unique_ids_patch_register_duplicate_halts():
    content = "- id: PP-761\n  status: open\n- id: PP-761\n  status: open\n"
    with pytest.raises(RuntimeError, match="duplicate ID"):
        valoria_hooks.assert_unique_ids([('canon/patch_register_active.yaml', content)])


def test_unique_ids_non_ledger_path_ignored():
    # A non-ledger file with repeated ids is not this gate's concern.
    content = '{"id": "ED-901"}\n{"id": "ED-901"}\n'
    valoria_hooks.assert_unique_ids([('designs/world/notes.md', content)])


# ─────────────────────────────────────────────────────────────────────────────
# jsonl_ledger_gate  (editorial_ledger.jsonl integrity)
# ─────────────────────────────────────────────────────────────────────────────

JSONL = 'canon/editorial_ledger.jsonl'


def test_jsonl_complete_entry_passes():
    valoria_hooks.jsonl_ledger_gate(
        [(JSONL, '{"id": "ED-901", "status": "open", "description": "x"}\n')]
    )


def test_jsonl_missing_soft_fields_warns_not_halts():
    # id present (hard) but no status/description (soft) -> warning only, no raise.
    valoria_hooks.jsonl_ledger_gate([(JSONL, '{"id": "ED-901"}\n')])


def test_jsonl_missing_id_halts():
    with pytest.raises(RuntimeError, match="missing/empty id"):
        valoria_hooks.jsonl_ledger_gate([(JSONL, '{"status": "open", "description": "x"}\n')])


def test_jsonl_invalid_json_halts():
    with pytest.raises(RuntimeError, match="invalid JSON"):
        valoria_hooks.jsonl_ledger_gate([(JSONL, '{"id": "ED-901", broken\n')])


def test_jsonl_non_object_halts():
    with pytest.raises(RuntimeError, match="not a JSON object"):
        valoria_hooks.jsonl_ledger_gate([(JSONL, '"just a string"\n')])


def test_jsonl_non_standard_id_warns_not_halts():
    # id present but not ED-<int> -> warning, no raise.
    valoria_hooks.jsonl_ledger_gate([(JSONL, '{"id": "FOO-1", "status": "open", "description": "x"}\n')])


def test_jsonl_non_ledger_path_ignored():
    valoria_hooks.jsonl_ledger_gate([('canon/other.jsonl', 'not even json')])


# ─────────────────────────────────────────────────────────────────────────────
# sim_fabrication_check  (uncited mechanical constants)
# ─────────────────────────────────────────────────────────────────────────────

def test_sim_fab_non_sim_file_ignored():
    # Not a sim .py file -> no scan, no raise (even with a bare constant).
    valoria_hooks.sim_fabrication_check([('scripts/helper.py', 'rate = 4567\n')])


def test_sim_fab_cited_constant_passes():
    content = 'damage = 4567  # [canonical: designs/scene/combat_v30.md §3]\n'
    valoria_hooks.sim_fabrication_check([('tests/sim/test_x.py', content)])


def test_sim_fab_exempt_numbers_pass():
    # 0/1/2/10/100 are exempt; range() bound is structural.
    content = 'for i in range(10):\n    total = i + 1\n'
    valoria_hooks.sim_fabrication_check([('tests/sim/test_x.py', content)])


def test_sim_fab_uncited_constant_halts(monkeypatch):
    # Ensure no local sim_verification_ledger.json masks the value (determinism).
    monkeypatch.setattr(valoria_hooks.os.path, 'exists', lambda p: False)
    with pytest.raises(RuntimeError, match="sim_fabrication_check"):
        valoria_hooks.sim_fabrication_check([('tests/sim/test_x.py', 'damage_value = 4567\n')])


# ─────────────────────────────────────────────────────────────────────────────
# _validate_handoff_schema  (github_ops)
# ─────────────────────────────────────────────────────────────────────────────

def _valid_handoff():
    return {
        'id': 'test-handoff',
        'task': {'skill': 'valoria-orchestrator', 'description': 'd'},
        'context_files': [{'path': 'a.md', 'depth': 'full', 'reason': 'r'}],
        'working_state': {'next': ['do x']},
        'last_commit': 'abc123',
        'owns': ['references/**'],
    }


def test_handoff_schema_valid_returns_no_errors():
    assert github_ops._validate_handoff_schema(_valid_handoff()) == []


def test_handoff_schema_missing_top_level_fields():
    errs = github_ops._validate_handoff_schema({})
    assert any('Missing top-level fields' in e for e in errs)


def test_handoff_schema_empty_context_files():
    h = _valid_handoff(); h['context_files'] = []
    errs = github_ops._validate_handoff_schema(h)
    assert any('context_files' in e for e in errs)


def test_handoff_schema_bad_depth():
    h = _valid_handoff(); h['context_files'] = [{'path': 'a', 'depth': 'index', 'reason': 'r'}]
    errs = github_ops._validate_handoff_schema(h)
    assert any('depth' in e for e in errs)


def test_handoff_schema_empty_next():
    h = _valid_handoff(); h['working_state'] = {'next': []}
    errs = github_ops._validate_handoff_schema(h)
    assert any('next' in e for e in errs)


def test_handoff_schema_empty_owns():
    h = _valid_handoff(); h['owns'] = []
    errs = github_ops._validate_handoff_schema(h)
    assert any('owns' in e for e in errs)
