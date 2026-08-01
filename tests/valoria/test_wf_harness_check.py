"""The dispute-shape gate must FAIL on the defect it was written to catch (ED-IN-0087 residual).

`tests/valoria/test_wf_harness.py` proves the harness behaves; this proves the GATE bites. The two
are not interchangeable, and the reason is the whole point of this module:

The harness's own behavioural suite passed 13/13 for the entire period during which five of eight
production scripts called `run.dispute()` with four keys the harness does not read. It could not
have failed — it exercises the harness with CORRECT keys, so it verified the contract while every
caller violated it. That is CLAUDE.md §0.1 point 2 exactly: an assertion that cannot observe the
failure it excludes is not a weak test, it is an absent one.

So every test here PLANTS a defect and asserts the gate reports it. A gate that has never been
observed to fail is indistinguishable from one that cannot.
"""
import importlib.util
import os
import shutil

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CHECKER = os.path.join(ROOT, 'tools', 'ci_wf_harness_check.py')
DONOR = os.path.join(ROOT, '.claude', 'wf_wave4_central.js')


def _load():
    spec = importlib.util.spec_from_file_location('ci_wf_harness_check', CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture()
def sandbox(tmp_path, monkeypatch):
    """A one-script tree the gate can be pointed at, so plants never touch the real .claude/."""
    mod = _load()
    dst = tmp_path / 'wf_sandbox.js'
    shutil.copy(DONOR, dst)
    monkeypatch.setattr(mod, 'WF_GLOB', str(tmp_path / 'wf_*.js'))
    monkeypatch.setattr(mod, 'ROOT', str(tmp_path))
    return mod, dst


def _keys_of(mod, src):
    return [keys for _, keys in mod._dispute_calls(src)]


# ─────────────────────────────────────────────────────────────── the contract is DERIVED, not typed

def test_the_legal_key_set_comes_from_the_owner_and_is_not_empty():
    """Hardcoding these keys would re-create the two-copies-drifting bug the gate exists to close."""
    mod = _load()
    legal, required = mod._dispute_contract()
    assert 'finding_id' in legal and 'layer_disputed' in legal and 'positions' in legal
    assert required == {'finding_id'}
    # the four keys that actually shipped, none of which the owner reads
    assert not ({'layer', 'target', 'detail', 'severity'} & legal)


def test_an_owner_without_run_dispute_fails_loudly_instead_of_passing_vacuously(tmp_path, monkeypatch):
    """A gate whose contract silently empties is the 'clean over nothing' defect class itself."""
    mod = _load()
    fake = tmp_path / 'wf_harness.js'
    fake.write_text("// no dispute here\n", encoding='utf-8')
    monkeypatch.setattr(mod, 'OWNER', str(fake))
    with pytest.raises(SystemExit):
        mod._dispute_contract()


# ─────────────────────────────────────────────────────────────────────── planted defects must fire

def test_the_exact_shape_that_shipped_is_rejected(sandbox):
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    planted = src.replace(
        "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))",
        "run.dispute({ layer: 'evidence', target: v.target, detail: v.evidence, severity: v.severity })")
    assert planted != src, "the donor no longer contains the call this test plants over"
    dst.write_text(planted, encoding='utf-8')
    assert mod.check() == 1, "the gate accepted the exact shape that shipped and ran live"


def test_an_unread_key_is_rejected_even_when_finding_id_is_present(sandbox):
    """ISOLATES the unknown-key branch, and only this test does.

    Mutation-checked: with the unknown-key check deleted, the whole module still passed 10/10,
    because the shape that actually shipped ALSO omits finding_id — so the test above was green on
    the required-key branch while the branch it named went unexercised. Keeping finding_id here is
    the entire point; drop it and this test stops testing what its name says.
    """
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    dst.write_text(src.replace(
        "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))",
        "run.dispute({ finding_id: v.target, detail: v.evidence, severity: v.severity })"),
        encoding='utf-8')
    assert mod.check() == 1, "an unread key passed the gate while finding_id was present"


def test_omitting_finding_id_alone_is_rejected(sandbox):
    """The subtle half: every key legal, but the record can never receive a ruling."""
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    dst.write_text(src.replace(
        "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))",
        "run.dispute({ layer_disputed: 'evidence', root_cause: 'stale-canon', positions: [] })"),
        encoding='utf-8')
    assert mod.check() == 1


def test_a_correct_hand_rolled_record_is_accepted(sandbox):
    """Both directions. A gate that rejects the correct form too is not a gate, it is a ban."""
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    dst.write_text(src.replace(
        "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))",
        "run.dispute({ finding_id: v.target, layer_disputed: 'evidence', "
        "root_cause: 'stale-canon', positions: [{ by: 'critic', holds: v.evidence }] })"),
        encoding='utf-8')
    assert mod.check() == 0


def test_the_live_tree_passes(sandbox):
    """The donor is copied unmodified: if this fails, a real script is broken right now."""
    mod, _ = sandbox
    assert mod.check() == 0


# ────────────────────────────────────────────────────────── parsing, where a false positive hides

def test_a_dispute_written_in_a_COMMENT_is_not_read_as_a_call(sandbox):
    """The harness documents this call in prose. Scanning prose as code made the gate flag the
    documentation of the defect it catches — which is how a gate earns being ignored."""
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    dst.write_text(
        src + "\n// counter-example: run.dispute({ layer: 'evidence', target: 'x' }) is WRONG\n",
        encoding='utf-8')
    assert mod.check() == 0


def test_nested_objects_and_braces_in_strings_do_not_leak_into_the_key_set():
    """`positions` holds objects whose string values contain braces. A regex-shaped parser reads
    their inner keys as top-level ones and invents violations that cannot be fixed."""
    mod = _load()
    src = ("run.dispute({ finding_id: 'a', positions: [{ by: 'critic', holds: 'see {layer: x}' }], "
           "root_cause: 'stale-canon' })")
    assert _keys_of(mod, src) == [['finding_id', 'positions', 'root_cause']]


def test_a_record_built_by_the_owner_is_not_second_guessed():
    """run.dispute(hVerdictDispute(...)) has no literal to check — the owner built it."""
    mod = _load()
    assert _keys_of(mod, "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))") == []


# ───────────────────────────────────────────────────── the --fix path must not corrupt its own view

def test_fix_reports_no_phantom_violations_when_the_resynced_block_changes_length(sandbox):
    """REGRESSION. After a re-sync the block's length changes, and the end offset was not
    recomputed — so every later check read a half-blanked harness as script code. It surfaced as
    violations inside the harness itself, on the one run (`--fix`) least likely to be re-verified.
    """
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    i, j = src.find(mod.BEGIN), src.find(mod.END)
    assert i >= 0 and j >= 0
    # a SHORTER stale block, so the re-sync must grow it — the direction that broke the offsets
    stale = mod.BEGIN + "\n// stale copy\n" + mod.END
    dst.write_text(src[:i] + stale + src[j + len(mod.END):], encoding='utf-8')

    assert mod.check(fix=True) == 0, "--fix reported violations it then could not reproduce"
    assert mod.check() == 0, "the re-synced file does not pass a plain check"


def test_a_quoted_key_is_not_invisible(sandbox):
    """ADVERSARIAL REVIEW FINDING — a false PASS in the guard's own failure mode.

    A quote character is consumed by the scanner's string branch before the key branch can see it,
    so `{ finding_id: x, 'layer': 'evidence' }` parsed to ['finding_id'] alone: the unknown key
    vanished, finding_id was present, and the call PASSED — while at run time `'layer'` is unread
    and layer_disputed silently defaults. Reachable by ordinary JSON habit.
    """
    mod, dst = sandbox
    src = dst.read_text(encoding='utf-8')
    dst.write_text(src.replace(
        "run.dispute(hVerdictDispute(v, 'critic:w4', v.target))",
        "run.dispute({ finding_id: v.target, 'layer': 'evidence' })"), encoding='utf-8')
    assert mod.check() == 1, 'a quoted unknown key passed the gate'


def test_quoted_and_bare_keys_are_both_collected():
    mod = _load()
    src = "run.dispute({ finding_id: 'a', 'layer_disputed': 'evidence' })"
    assert _keys_of(mod, src) == [['finding_id', 'layer_disputed']]


def test_a_comment_inside_the_owners_dispute_body_cannot_widen_the_contract(tmp_path, monkeypatch):
    """LATENT WIDENING CHANNEL. The legal key set is regex-derived from the owner's run.dispute
    body; without stripping comments first, `// rec.layer was retired` would make `layer` — the
    exact key that shipped broken — legal repo-wide, with no test failing."""
    mod = _load()
    fake = tmp_path / 'wf_harness.js'
    fake.write_text(
        "run.dispute = function (rec) {\n"
        "  // rec.layer was retired in v0\n"
        "  const d = { finding_id: String(rec && rec.finding_id) }\n"
        "}\n", encoding='utf-8')
    monkeypatch.setattr(mod, 'OWNER', str(fake))
    legal, _ = mod._dispute_contract()
    assert 'layer' not in legal, 'a comment inside the owner widened the legal key set'
    assert 'finding_id' in legal
