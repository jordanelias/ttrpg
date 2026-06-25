"""
Unit tests for tools/ci_vetting_check.py — the pure PP-674 framework vetting
gate core (`check_register`).

These tests exercise only the network-free, importable core function. They do
not touch disk, git, or the network.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_vetting_check  # noqa: E402


# ── Fixtures: minimal patch-register fragments ────────────────────────────────

# (a) Class A, id >= 674, NO vetting block → must be a violation.
CLASS_A_MISSING_VETTING = """\
patches:
- id: PP-700
  date: 2026-05-10
  severity: P1
  class: A
  description: Class A entry with no vetting block.
  status: applied
"""

# (b) Class A, id >= 674, COMPLETE vetting block → no violation.
CLASS_A_COMPLETE_VETTING = """\
patches:
- id: PP-701
  date: 2026-05-10
  severity: P1
  description: Class A entry with a full vetting block.
  status: applied
  vetting:
    class: A
    necessity: pass
    omega: pass
    mu: []
    m_ratings:
      M-1: +
      M-2: o
    q: pass
"""

# (c) class: C, id >= 674 → exempt (light validation, only `class` needed).
CLASS_C_EXEMPT = """\
patches:
- id: PP-702
  date: 2026-05-10
  severity: P3
  class: C
  description: Class C entry — exempt from full vetting.
  status: applied
"""

# (d) id < 674, no vetting → grandfathered (pre-framework), no violation.
PRE_FRAMEWORK_GRANDFATHERED = """\
patches:
- id: PP-500
  date: 2026-04-01
  severity: P2
  description: Old entry predating the framework, no vetting block.
  status: applied
"""

# (e) Class B, id >= 674, missing exactly one required key (omega) → a violation
#     that names `omega`.
CLASS_B_MISSING_OMEGA = """\
patches:
- id: PP-703
  date: 2026-05-10
  severity: P2
  description: Class B entry missing the omega key.
  status: applied
  vetting:
    class: B
    necessity: pass
    mu: []
    m_ratings:
      M-1: +
    q: pass
"""


# ── Tests ─────────────────────────────────────────────────────────────────────

def test_a_class_a_missing_vetting_block_is_violation():
    errors = ci_vetting_check.check_register(CLASS_A_MISSING_VETTING)
    assert errors, "Class A PP-700 with no vetting block should produce a violation"
    assert any('PP-700' in e for e in errors)
    assert any('vetting' in e for e in errors)


def test_b_class_a_complete_vetting_block_is_clean():
    errors = ci_vetting_check.check_register(CLASS_A_COMPLETE_VETTING)
    assert errors == [], f"Complete Class A vetting block should be clean, got: {errors}"


def test_c_class_c_entry_is_exempt():
    errors = ci_vetting_check.check_register(CLASS_C_EXEMPT)
    assert errors == [], f"Class C entry should be exempt, got: {errors}"


def test_d_pre_pp674_entry_is_grandfathered():
    errors = ci_vetting_check.check_register(PRE_FRAMEWORK_GRANDFATHERED)
    assert errors == [], f"PP-500 (< 674) should be grandfathered, got: {errors}"


def test_e_class_b_missing_omega_names_the_key():
    errors = ci_vetting_check.check_register(CLASS_B_MISSING_OMEGA)
    assert errors, "Class B PP-703 missing omega should produce a violation"
    assert any('omega' in e for e in errors), \
        f"violation should name the missing key 'omega', got: {errors}"
    assert any('PP-703' in e for e in errors)


if __name__ == '__main__':
    # Allow running without pytest: execute each test and report.
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as exc:
                failures += 1
                print(f"FAIL {name}: {exc}")
    print(f"\n{'-' * 40}\n{failures} failure(s)")
    sys.exit(1 if failures else 0)
