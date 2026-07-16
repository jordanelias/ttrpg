#!/usr/bin/env python3
"""
valoria_rename.py — the "change once" executor for centralized definition names.

A definition's name lives in exactly one place: references/names_index.yaml. To
rename it everywhere, run this tool. It rewrites every word-boundary occurrence of
the old name across the design corpus AND the registries (including names_index.yaml
itself and the descriptor/proper-noun mirrors that ci_names_consistency.py checks),
so a single command keeps the index, the mirrors, and the prose in lockstep.

    # by index key (reads the current canonical as the "from"):
    python tools/valoria_rename.py --key attr.mind.acuity --to Insight --apply

    # or by literal old name:
    python tools/valoria_rename.py --from Acuity --to Insight        # dry-run (default)
    python tools/valoria_rename.py --from Acuity --to Insight --apply

DRY-RUN IS THE DEFAULT: without --apply it prints every line that would change and
writes nothing. Matching is CASE-SENSITIVE by default (display names are
capitalized; this avoids corrupting lowercase dotted keys like `attr.mind.acuity`);
pass --ignore-case to widen.

SCOPE: walks designs/ params/ references/ canon/ for text files, skipping history
and test fixtures (archives/, deprecated/, tests/, designs/audit/, the editorial
ledger, prose-writer fixtures) so the past is never rewritten. Reads the current
name from the index via tools/names.py — no rule re-implemented here.
"""
import argparse
import os
import re
import sys

try:
    import names
except ImportError:  # allow running from repo root
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import names

# Directories whose text we sweep. references/ + canon/ are included so the index
# and the mirror registries are updated by the same pass.
SCOPE_DIRS = ('designs', 'params', 'references', 'canon')
EXTS = ('.md', '.yaml', '.yml', '.jsonl', '.txt')

# History / fixtures we must never rewrite (distinct from the naming gate's EXCLUDE,
# which also shields registries — here we WANT to update the registries).
SKIP = (
    'tests/',
    'archives/',
    'deprecated/',
    'designs/audit/',
    'registers/editorial_ledger',
    'skills/prose-writer/',
)


def _skip(path):
    p = path.replace('\\', '/')
    return any(s in p for s in SKIP)


def iter_files():
    for d in SCOPE_DIRS:
        if not os.path.isdir(d):
            continue
        for root, _dirs, files in os.walk(d):
            for fn in files:
                rel = os.path.join(root, fn).replace('\\', '/')
                if rel.endswith(EXTS) and not _skip(rel):
                    yield rel


def plan_changes(old, new, ignore_case=False):
    """Return {path: [(lineno, old_line, new_line), ...]} for every affected file."""
    pat = re.compile(r'\b' + re.escape(old) + r'\b', re.IGNORECASE if ignore_case else 0)
    changes = {}
    for path in iter_files():
        try:
            with open(path, encoding='utf-8') as f:
                lines = f.readlines()
        except (OSError, UnicodeDecodeError):
            continue
        edited = []
        for i, line in enumerate(lines, 1):
            new_line = pat.sub(new, line)
            if new_line != line:
                edited.append((i, line.rstrip('\n'), new_line.rstrip('\n')))
        if edited:
            changes[path] = edited
    return changes


def apply_changes(old, new, ignore_case=False):
    pat = re.compile(r'\b' + re.escape(old) + r'\b', re.IGNORECASE if ignore_case else 0)
    touched = 0
    for path in iter_files():
        try:
            with open(path, encoding='utf-8') as f:
                text = f.read()
        except (OSError, UnicodeDecodeError):
            continue
        new_text = pat.sub(new, text)
        if new_text != text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            touched += 1
    return touched


def main(argv):
    ap = argparse.ArgumentParser(description="Rename a definition everywhere from one edit.")
    ap.add_argument('--from', dest='old', help="literal current name to replace")
    ap.add_argument('--to', dest='new', required=True, help="new canonical name")
    ap.add_argument('--key', help="names_index key; reads its current canonical as --from")
    ap.add_argument('--apply', action='store_true', help="write changes (default: dry-run)")
    ap.add_argument('--ignore-case', action='store_true', help="case-insensitive match")
    args = ap.parse_args(argv)

    old = args.old
    if args.key:
        canon = names.canonical(args.key)
        if not canon:
            print(f"ERROR: key '{args.key}' not found in references/names_index.yaml.")
            return 2
        if old and old != canon:
            print(f"ERROR: --from '{old}' != current canonical '{canon}' for {args.key}.")
            return 2
        old = canon
    if not old:
        print("ERROR: provide --from <name> or --key <index-key>.")
        return 2
    if old == args.new:
        print("ERROR: --from and --to are identical; nothing to do.")
        return 2

    key = args.key or names.key_for(old)
    if not key:
        print(f"NOTE: '{old}' is not a known names_index canonical/alias — sweeping text only "
              f"(the index will not gain an entry). Add it to references/names_index.yaml to track it.")

    changes = plan_changes(old, args.new, args.ignore_case)
    total = sum(len(v) for v in changes.values())
    if not changes:
        print(f'No occurrences of "{old}" found in scope.')
        return 0

    verb = "Rewrote" if args.apply else "Would rewrite"
    print(f'{verb} "{old}" -> "{args.new}"  ({total} line(s) across {len(changes)} file(s))'
          + (f'  [index key: {key}]' if key else ''))
    for path in sorted(changes):
        print(f"\n  {path}")
        for lineno, old_line, new_line in changes[path][:50]:
            print(f"    {lineno}: - {old_line.strip()[:110]}")
            print(f"    {lineno}: + {new_line.strip()[:110]}")
        extra = len(changes[path]) - 50
        if extra > 0:
            print(f"    ... (+{extra} more line(s))")

    if args.apply:
        touched = apply_changes(old, args.new, args.ignore_case)
        print(f"\nApplied. {touched} file(s) written. "
              f"Run `python tools/ci_names_consistency.py` and review `git diff` before committing.")
    else:
        print("\nDry-run only (no files changed). Re-run with --apply to write.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
