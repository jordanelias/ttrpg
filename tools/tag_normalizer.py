#!/usr/bin/env python3
"""
tag_normalizer.py — the ONE resolver/stripper for canonical-identifier tags in prose.

Reconciliation Program §3 (the vocabulary enabler). A canonical-identifier tag is an ID-form
reference to a named definition, written ``[[<id>]]`` (e.g. ``[[conv.faith]]``) or, for an
irregular surface form ONLY, ``[[<id>|<override display>]]``. The renderer resolves ``<id>`` to
its display string from ``references/names_index.yaml`` (via ``tools/names.py``) — the
"change once" guarantee: the display lives in ONE place, so a rename there propagates to every
tag site without embedding ``|Faith`` into thousands of tags (the denormalization
``valoria_rename`` exists to prevent).

WHY A SINGLE OWNER (§3 precondition — priced in BEFORE any tag enters the corpus): every
prose-consuming tool — the vector audit, the co-file checker, the naming lints, the size caps,
and the eventual gameplay text renderer — must strip/resolve tags the SAME way, or one tag
would read as literal ``[[conv.faith]]`` noise to one tool and "Faith" to another. This is that
one implementation (CLAUDE.md §8 "every rule lives once").

Guarantees:
  • ID-form tokens are EXCLUDED from prose matching (A6 / perf) — resolve to display first.
  • Collision-free: ``[[`` does not occur in the current corpus, so the tag syntax adds no
    ambiguity with existing prose (``stray_open_brackets`` is the migration precondition lint).
  • Deterministic, model-free, fault-tolerant: an unknown id never crashes; policy decides
    whether it passes through raw (default, so a typo is not silently laundered) or humanizes.

Import-only (no __main__): consumers ``import tag_normalizer as tags``.
"""
import os
import re
import sys

_TOOLS = os.path.dirname(os.path.abspath(__file__))
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)
import names  # noqa: E402  — the ONE names_index reader (§8)

# [[ id ]]  or  [[ id | override display ]].
#   id       : a dotted canonical key — starts alnum/_, then word chars, '.', '-'.
#   override : anything up to the closing ']]' (spaces/punctuation allowed), for irregulars.
# Inner whitespace is tolerated (``[[ conv.faith ]]``) so hand-authored tags are forgiving.
TAG_RE = re.compile(r'\[\[\s*([A-Za-z0-9_][\w.\-]*?)\s*(?:\|\s*([^\]]*?)\s*)?\]\]')


class Tag(tuple):
    """A parsed tag: ``(id, override, start, end)``. ``override`` is None for a bare ``[[id]]``."""
    __slots__ = ()

    def __new__(cls, id, override, start, end):
        return super().__new__(cls, (id, override, start, end))

    id = property(lambda s: s[0])
    override = property(lambda s: s[1])
    start = property(lambda s: s[2])
    end = property(lambda s: s[3])


def find_tags(text):
    """Every tag in ``text``, in source order, as ``Tag(id, override, start, end)``."""
    if not text or '[[' not in text:
        return []
    return [Tag(m.group(1), m.group(2), m.start(), m.end()) for m in TAG_RE.finditer(text)]


def resolve_id(tag_id):
    """The display string for a tag id, or None if the id is not in names_index.
    Reuses ``names.canonical`` (the ONE reader); never re-parses the index."""
    return names.canonical(tag_id)


def render(text, unknown='keep'):
    """Replace every ``[[id]]`` / ``[[id|override]]`` with its display string.

    Precedence: an explicit ``override`` wins (irregular surface form); else the names_index
    canonical display; else, for an UNKNOWN id, the ``unknown`` policy:
      * ``'keep'``     — leave the raw ``[[id]]`` (visible as unresolved; the default for
                         lints, so a typo'd id is not silently laundered into plausible prose).
      * ``'humanize'`` — the id's last dotted segment with ``_``/``-`` → spaces (best-effort
                         display for the gameplay renderer).
      * ``'raw'``      — the bare id, unbracketed.

    Non-tag text (including inflection adjacent to a tag, ``[[conv.faith]]'s``) is untouched.
    """
    if not text or '[[' not in text:
        return text

    def _sub(m):
        tid, ovr = m.group(1), m.group(2)
        if ovr:                                   # explicit override (irregular) wins
            return ovr
        disp = names.canonical(tid)
        if disp:
            return disp
        if unknown == 'humanize':
            return _humanize(tid)
        if unknown == 'raw':
            return tid
        return m.group(0)                         # 'keep' — surface the unresolved tag as-is

    return TAG_RE.sub(_sub, text)


def strip(text):
    """Prose as a scanner should see it: every tag resolved to its display string, unknown ids
    kept raw so they surface as defects rather than laundered. This is what the naming lints /
    co-file checker / size caps call before scanning, so a tag reads as its human text."""
    return render(text, unknown='keep')


def has_tags(text):
    """True if ``text`` contains at least one well-formed tag."""
    return bool(text) and '[[' in text and TAG_RE.search(text) is not None


def unknown_tags(text):
    """Sorted tag ids in ``text`` that names_index cannot resolve — the lint surface."""
    return sorted({t.id for t in find_tags(text) if names.canonical(t.id) is None})


def stray_open_brackets(text):
    """Positions of any ``[[`` in ``text`` that is NOT the start of a well-formed tag — the
    collision surface the migration must be clean of (§3: ``[[`` verified absent from prose).
    A doc with stray ``[[`` uses the sequence for something other than a tag; migrate with care."""
    if not text or '[[' not in text:
        return []
    tag_starts = {m.start() for m in TAG_RE.finditer(text)}
    return [m.start() for m in re.finditer(r'\[\[', text) if m.start() not in tag_starts]


def is_collision_free(text):
    """True if ``text`` has no stray ``[[`` (every ``[[`` that appears is a well-formed tag)."""
    return not stray_open_brackets(text)


def _humanize(tag_id):
    tail = tag_id.rsplit('.', 1)[-1]
    return re.sub(r'[_\-]', ' ', tail).strip()
