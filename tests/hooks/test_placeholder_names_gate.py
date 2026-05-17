"""
Tests for valoria_hooks.placeholder_names_gate.

Added 2026-05-17 as part of Pass 2 follow-up (Option A: generic-name unblocking
of faction-specific mechanic implementation, with hook-enforced rename deadline).
"""

import os
import tempfile

import pytest


def _setup_registry(tmp_path, registry_yaml):
    """Write a test placeholder_names.yaml in a temp canon/ dir + chdir."""
    canon_dir = tmp_path / "canon"
    canon_dir.mkdir(exist_ok=True)
    (canon_dir / "placeholder_names.yaml").write_text(registry_yaml)
    return tmp_path


def test_placeholder_pending_does_not_halt(tmp_path, monkeypatch):
    """A placeholder with deadline_status: pending must not block commits."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    _setup_registry(tmp_path, """
schema_version: 1
placeholders:
  - id: TEST-1
    placeholder_name: test_pending
    deadline_status: pending
""")
    monkeypatch.chdir(tmp_path)
    # Should not raise
    valoria_hooks.placeholder_names_gate([
        ('sim/test_pending.py', 'references test_pending'),
    ])


def test_placeholder_expired_halts(tmp_path, monkeypatch):
    """A placeholder with deadline_status: expired must halt with RuntimeError."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    _setup_registry(tmp_path, """
schema_version: 1
placeholders:
  - id: TEST-2
    placeholder_name: test_expired
    canonical_name_pending: test_canonical
    deadline_status: expired
""")
    monkeypatch.chdir(tmp_path)
    with pytest.raises(RuntimeError, match="placeholder_names_gate"):
        valoria_hooks.placeholder_names_gate([
            ('sim/test_expired.py', 'references test_expired'),
        ])


def test_placeholder_expired_absent_does_not_halt(tmp_path, monkeypatch):
    """An expired placeholder not in commit content must not halt."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    _setup_registry(tmp_path, """
schema_version: 1
placeholders:
  - id: TEST-3
    placeholder_name: test_expired
    deadline_status: expired
""")
    monkeypatch.chdir(tmp_path)
    # Different module; placeholder not present
    valoria_hooks.placeholder_names_gate([
        ('sim/unrelated_module.py', 'no placeholder here'),
    ])


def test_placeholder_resolved_does_not_halt(tmp_path, monkeypatch):
    """A placeholder marked resolved must not halt even if name still appears."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    _setup_registry(tmp_path, """
schema_version: 1
placeholders:
  - id: TEST-4
    placeholder_name: test_resolved
    deadline_status: resolved
""")
    monkeypatch.chdir(tmp_path)
    # Same-commit migration: placeholder reference still in code as transition
    valoria_hooks.placeholder_names_gate([
        ('sim/test_resolved.py', 'references test_resolved as transition'),
    ])


def test_registry_update_in_same_commit(tmp_path, monkeypatch):
    """When commit includes a registry update flipping status, the new
    registry is used (not the disk version)."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    # Disk version: expired
    _setup_registry(tmp_path, """
schema_version: 1
placeholders:
  - id: TEST-5
    placeholder_name: test_flipping
    deadline_status: expired
""")
    monkeypatch.chdir(tmp_path)

    # Commit-version: resolved (Jordan transitioning)
    new_registry = """
schema_version: 1
placeholders:
  - id: TEST-5
    placeholder_name: test_flipping
    deadline_status: resolved
"""
    # Should NOT halt: commit version takes precedence
    valoria_hooks.placeholder_names_gate([
        ('canon/placeholder_names.yaml', new_registry),
        ('sim/test_flipping.py', 'references test_flipping'),
    ])


def test_no_registry_file_skips_silently(tmp_path, monkeypatch):
    """If registry file doesn't exist, hook does not halt (bootstrap-safe)."""
    import sys
    sys.path.insert(0, '/home/claude')
    import valoria_hooks

    # No canon/ dir, no registry
    monkeypatch.chdir(tmp_path)
    # Should not raise
    valoria_hooks.placeholder_names_gate([
        ('sim/test_module.py', 'any content'),
    ])
