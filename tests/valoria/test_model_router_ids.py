"""Keep tools/model_router.html's tier->model-ID map in sync with CLAUDE.md §10.

ED-IN-0087 (finding: ED-IN-0085). Before this guard, `model_router.html` pinned `sonnet` to
`claude-sonnet-4-20250514` and `opus` to `claude-opus-4-6` — two generations stale — and nothing
noticed, because **nothing in the tree bound tier aliases to model IDs at all**. §10 described the
tiers in prose; the only concrete IDs lived in an unversioned HTML tool that no check read.

That is the §0.1 point-5 signature: the router was correct when written and rotted because the
roster moved. The fix is the standard shape — one owner (§10's table), every other surface derived
from it, and a guard that fails on divergence rather than trusting discipline.

This test deliberately parses the DOC as the source of truth and the TOOL as the mirror. If the
direction ever needs to flip, flip it here explicitly rather than letting the two drift.
"""
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CLAUDE_MD = os.path.join(ROOT, 'CLAUDE.md')
ROUTER = os.path.join(ROOT, 'tools', 'model_router.html')

# `| `haiku` | `claude-haiku-4-5` | 200K | ... |` — tier alias then model ID, both backticked.
_DOC_ROW = re.compile(r"^\|\s*`([a-z]+)`\s*\|\s*`(claude-[a-z0-9.\-]+)`\s*\|", re.M)
# `haiku: 'claude-haiku-4-5',`
_JS_ENTRY = re.compile(r"^\s*([a-z]+)\s*:\s*'(claude-[a-z0-9.\-]+)'\s*,?\s*$", re.M)


def _read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def doc_map():
    return dict(_DOC_ROW.findall(_read(CLAUDE_MD)))


def router_map():
    text = _read(ROUTER)
    block = re.search(r"const MODELS\s*=\s*\{(.*?)\}", text, re.S)
    assert block, "tools/model_router.html no longer defines `const MODELS = { ... }`"
    return dict(_JS_ENTRY.findall(block.group(1)))


def test_claude_md_declares_the_tier_to_id_binding():
    """§10 must actually contain the table — the whole point is that it is the single owner."""
    ids = doc_map()
    missing = [t for t in ('haiku', 'sonnet', 'opus', 'fable') if t not in ids]
    assert not missing, (
        f"CLAUDE.md §10's tier->model-ID table is missing {missing}. That table is the single owner "
        f"of the binding (ED-IN-0087); without it every other surface is guessing.")


def test_router_mirrors_the_doc_exactly():
    doc, router = doc_map(), router_map()
    shared = sorted(set(doc) & set(router))
    assert shared, "no overlapping tiers between CLAUDE.md §10 and model_router.html"
    drift = {t: (doc[t], router[t]) for t in shared if doc[t] != router[t]}
    assert not drift, (
        "tools/model_router.html has drifted from CLAUDE.md §10's tier->ID table "
        f"(tier: doc_id != router_id): {drift}. §10 is the owner — update the mirror.")


@pytest.mark.parametrize('tier', ['haiku', 'sonnet', 'opus'])
def test_router_covers_every_routable_tier(tier):
    """The router routes to haiku/sonnet/opus; a tier it can emit must have an ID."""
    assert tier in router_map(), (
        f"model_router.html can emit tier '{tier}' but defines no model ID for it")


def test_no_dated_snapshot_suffixes_outside_haiku():
    """Current-generation IDs are undated aliases; a date suffix is a stale-pin smell.

    Haiku 4.5 is the documented exception (`claude-haiku-4-5-20251001` is a real full ID), so it is
    allowed either way; the rest must not carry one.
    """
    offenders = {t: i for t, i in router_map().items()
                 if t != 'haiku' and re.search(r'-\d{8}$', i)}
    assert not offenders, (
        f"dated snapshot IDs pinned for {offenders} — current-generation models use undated "
        f"aliases, and a date suffix is how the previous two-generation drift went unnoticed.")
