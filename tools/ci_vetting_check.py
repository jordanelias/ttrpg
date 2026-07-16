#!/usr/bin/env python3
"""
ci_vetting_check.py — framework vetting gate (PP-674), CI port.

Ports valoria_hooks.vetting_gate (the "Hook 3b" framework vetting gate) into a
standalone, network-free CI validator that reads the working tree.

The enforced rule (canonical framework, ref references/throughlines_meta.md §8):
  * Parse PP-(\\d+) entries from registers/patch_register_active.yaml.
  * Entries with id < PP-674 are GRANDFATHERED (pre-framework) — skipped.
  * For any entry with id >= 674:
      - If it carries `class: C|D|E` (anywhere in the entry body) or
        `pre-framework: true`, it is EXEMPT.
      - Otherwise it must carry a `vetting:` block. A missing block is a
        violation (the framework defaults to requiring vetting for all
        PP-674+ entries unless explicitly exempted).
      - Inside the vetting block, the `class` field must be present and one of
        A-E. Class C/D/E need only the `class` field. Class A/B must carry the
        full required key set: class / necessity / omega / mu / m_ratings / q.

The ONLY behavioural change from the original valoria_hooks.vetting_gate is the
I/O surface: the original received an in-memory `additions` list from the old
GitHub-API commit harness and fired only when that list touched the patch
register. This version reads registers/patch_register_active.yaml from the working
tree on disk and validates it on EVERY run (a CI job should always validate the
current register, not just when it was touched). The regex-based, PyYAML-free
parsing approach of the original is preserved verbatim.

Usage (from the repo root):
    python tools/ci_vetting_check.py

Exit code 0 = clean (or file absent → SKIP), 1 = violations found.
"""
import os
import re
import sys

# ── Framework constants (mirrored from valoria_hooks.py) ──────────────────────
VETTING_REQUIRED_KEYS = ('class', 'necessity', 'omega', 'mu', 'm_ratings', 'q')
VETTING_CLASS_VALUES = ('A', 'B', 'C', 'D', 'E')
VETTING_ENFORCED_FROM_PP = 674

REGISTER_PATH = 'registers/patch_register_active.yaml'


def _extract_vetting_block(body: str):
    """
    Return the text nested under a `vetting:` key inside one PP entry body, or
    None if the entry has no vetting block.

    The block runs from the line after `vetting:` up to (but not including) the
    next line that is a SIBLING key — a `key:`-style line indented the same as,
    or less than, the `vetting:` line itself — or end-of-body. Deeper-indented
    lines (the vetting block's own nested keys: class/necessity/omega/mu/
    m_ratings/q and any sub-trees like m_ratings or t_touches) are retained.

    This replaces the original valoria_hooks pattern
    `\\n\\s+vetting:\\s*\\n(.*?)(?=\\n\\s+\\w+:|\\Z)`, whose non-greedy capture
    halted at the first nested key and so captured an empty block when fed a
    whole file rather than a trailing diff fragment.
    """
    m = re.search(r'\n([ \t]*)vetting:[ \t]*\n', body)
    if not m:
        return None
    vetting_indent = len(m.group(1))
    rest = body[m.end():]
    lines = rest.split('\n')
    kept = []
    for line in lines:
        stripped = line.lstrip(' \t')
        if stripped:  # non-blank line
            indent = len(line) - len(stripped)
            # A sibling/parent key at <= vetting indent terminates the block.
            if indent <= vetting_indent and re.match(r'[\w-]+:', stripped):
                break
        kept.append(line)
    return '\n'.join(kept)


def check_register(content: str) -> list:
    """
    Pure, network-free core: validate patch-register text against the PP-674
    framework vetting gate.

    Args:
        content: the full text of registers/patch_register_active.yaml.

    Returns:
        A list of human-readable violation strings. An empty list means the
        register is clean (every PP-674+ Class A/B entry carries a complete
        vetting block; everything else is exempt or grandfathered).

    This is the function the unit tests exercise; it has no side effects and
    performs no I/O. The parsing follows valoria_hooks.vetting_gate (same
    entry-splitting regex, same exemption rules, same required-key set); the
    only deviation is an indentation-aware vetting-block extractor (see
    _extract_vetting_block) that correctly captures whole-file blocks — the
    original's extractor only worked on the trailing diff-fragment the old
    GitHub-API harness fed it.
    """
    # Parse PP entries — simple YAML-ish extraction (the full yaml module might
    # not be available in every environment; use the same regex style other
    # hooks use).
    entries = re.findall(
        r'-\s+id:\s+PP-(\d+)\s*\n(.*?)(?=\n-\s+id:\s+PP-\d+|\Z)',
        content, re.DOTALL
    )
    errors = []
    for pp_num_str, body in entries:
        pp_num = int(pp_num_str)
        if pp_num < VETTING_ENFORCED_FROM_PP:
            continue  # grandfathered
        # Does this entry have a vetting block? Capture everything nested under
        # `vetting:` — i.e. up to the next SIBLING key (a `key:` at the same or
        # shallower indentation as `vetting:` itself), or end-of-body.
        #
        # NOTE vs. the original valoria_hooks.vetting_gate: the original used the
        # pattern `(.*?)(?=\n\s+\w+:|\Z)`, whose non-greedy capture stops at the
        # FIRST nested key (`class:`), capturing almost nothing. That latent bug
        # never surfaced in the old harness because it only saw freshly-ADDED
        # diff lines (where the vetting block was the trailing text, terminated
        # by \Z). Reading the whole file on disk — the mandated I/O change —
        # exposes it: every real vetting block is followed by a sibling key or
        # the next entry. Preserving the original's *rule* (capture the vetting
        # block, then require its keys) therefore requires this indentation-aware
        # terminator so the block is captured in full.
        vetting_block = _extract_vetting_block(body)
        if vetting_block is None:
            # Missing — is this a Class A/B? We do not know for certain without
            # a class marker. Default: require vetting block for all entries
            # >= PP-674 unless the body explicitly carries "class: C|D|E" or
            # "pre-framework: true".
            if re.search(r'class:\s*[CDE]\b', body) or 'pre-framework: true' in body:
                continue
            errors.append(
                f"PP-{pp_num_str}: no `vetting:` block. Required for "
                f"Class A/B patches (PP-{VETTING_ENFORCED_FROM_PP}+). "
                f"Add class + vetting per references/throughlines_meta.md §8, "
                f"or mark `class: E` / `pre-framework: true` if grandfathered."
            )
            continue
        # Parse class
        class_match = re.search(r'class:\s*([A-E])\b', vetting_block)
        if not class_match:
            errors.append(
                f"PP-{pp_num_str}: vetting.class missing or invalid. "
                f"Must be one of {VETTING_CLASS_VALUES}."
            )
            continue
        cls = class_match.group(1)
        if cls in ('C', 'D', 'E'):
            # Light validation — only need class
            continue
        # Class A/B — require full set
        for key in VETTING_REQUIRED_KEYS:
            if re.search(rf'\b{key}:', vetting_block) is None:
                errors.append(
                    f"PP-{pp_num_str} (Class {cls}): vetting.{key} missing. "
                    f"Required keys for Class A/B: {VETTING_REQUIRED_KEYS}."
                )
    return errors


def main() -> int:
    """
    Read registers/patch_register_active.yaml from the working tree (relative to the
    current working directory, expected to be the repo root), validate it, and
    report. Returns a process exit code: 0 = clean / file absent, 1 = violations.
    """
    if not os.path.exists(REGISTER_PATH):
        print(f"SKIP {REGISTER_PATH}: not present in working tree — nothing to validate.")
        return 0

    try:
        with open(REGISTER_PATH, encoding='utf-8', errors='strict') as f:
            content = f.read()
    except UnicodeDecodeError as e:
        print(f"FAIL {REGISTER_PATH}: encoding error — {e}")
        return 1

    errors = check_register(content)

    if errors:
        print(f"[VETTING GATE FAILED] {len(errors)} violation(s) in {REGISTER_PATH}:\n")
        for i, e in enumerate(errors):
            print(f"  [{i + 1}] {e}")
        print(
            "\nFramework: references/throughlines_meta.md\n"
            f"Required for Class A/B patches (PP-{VETTING_ENFORCED_FROM_PP}+). "
            "Fix before merging."
        )
        return 1

    n_entries = len(re.findall(r'-\s+id:\s+PP-\d+', content))
    print(f"OK {REGISTER_PATH}: vetting gate passed — {n_entries} PP entries scanned.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
