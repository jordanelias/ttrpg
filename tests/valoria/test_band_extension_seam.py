"""The ladder's extension seam, probed with extensions that are NOT the contest's (ED-SC-0032).

WHY THIS EXISTS. `dice_engine.BandExtension` is the seam Jordan's 2026-08-15 ruling asked for:
*"if a system does require any modification or extension, then the wrapper needs to inject the
engine in such a manner that it can be modified cleanly."* The commit that built it claimed the
demote-only constraint was STRUCTURAL — an extension can express no band change but Overwhelming
-> Success — and an adversarial pass pointed out that the claim was asserted with a sample size
of ONE: every `degree_from_net` call site in the tree passed the contest's own extension, and
nothing anywhere probed the seam with a third-party or hostile one. A structural claim tested
only by its author's cooperative implementation is not tested.

So these extensions are deliberately BADLY BEHAVED. They try to promote, to move the Partial
window, to lie about their return type, to raise, and to mutate the owner's own tables. What the
seam guarantees, and what it does not, is measured rather than asserted.

CLAUDE.md §0.1 pt 5 admits this guard: the artifact is the ladder's contract, which is
load-bearing on the game (it decides every resolution in six subsystems) and on a Jordan ruling
(the seam IS the ruling's execution). It is not a test of a checker.

⚠ WHAT THIS FILE PROVES IS NARROWER THAN "SANDBOX", and says so: an extension confining itself to
its contract cannot express any band change but 3 -> 2. An extension reaching OUTSIDE the seam —
mutating `DEGREE_ORDINAL`, rebinding `degree_from_net` — can do more, and
`test_the_seam_is_not_a_sandbox` pins that honestly rather than letting the stronger reading
stand unchallenged.
"""
from __future__ import annotations

import pytest

from engine.autoload import dice_engine as DE
from engine.autoload.dice_engine import BandExtension, Degree, degree_from_net


# The four bands over a domain wide enough to include every boundary the ladder has.
DOMAIN = [(n / 4, o / 2) for n in range(-12, 61) for o in range(0, 13)]


class _AlwaysVeto(BandExtension):
    name = "probe:always-veto"

    def may_overwhelm(self, net, ob, **context):
        return False


class _NeverVeto(BandExtension):
    """The BASE class unmodified — its default must be permissive, or an extension that declares
    nothing would silently suppress every Overwhelming in its subsystem."""

    name = "probe:never-veto"


class _WantsToPromote(BandExtension):
    """Tries every way a bool-returning hook could be abused to raise a band."""

    name = "probe:wants-to-promote"

    def may_overwhelm(self, net, ob, **context):
        return "OVERWHELMING"          # truthy non-bool


class _LiesAboutItsType(BandExtension):
    """Returns an object whose truthiness flips per call — a hook cannot be trusted to be pure."""

    name = "probe:unstable"

    def __init__(self):
        self.calls = 0

    def may_overwhelm(self, net, ob, **context):
        self.calls += 1
        return self.calls % 2 == 0


class _Raises(BandExtension):
    name = "probe:raises"

    def may_overwhelm(self, net, ob, **context):
        raise RuntimeError("extension exploded")


def _unextended(net, ob):
    return degree_from_net(net, ob)


# ── What the seam GUARANTEES ──────────────────────────────────────────────────────────

@pytest.mark.parametrize("ext", [_AlwaysVeto(), _NeverVeto(), _WantsToPromote(), _LiesAboutItsType()])
def test_no_extension_can_express_any_band_change_but_overwhelming_to_success(ext):
    """THE FALSIFIER for the seam's central claim, run on extensions built to break it."""
    moved = 0
    for net, ob in DOMAIN:
        base = _unextended(net, ob)
        got = degree_from_net(net, ob, extension=ext)
        if got is base:
            continue
        moved += 1
        assert (base, got) == (Degree.OVERWHELMING, Degree.SUCCESS), (
            f"{ext.name} moved net={net} ob={ob} from {base.value} to {got.value} — the seam "
            "permits exactly one transition and this is not it"
        )
    assert len(DOMAIN) > 800, "the probe domain collapsed"
    if ext.name in ("probe:always-veto", "probe:unstable"):
        assert moved > 0, f"{ext.name} never fired — this parametrisation is vacuous"


def test_a_truthy_non_bool_cannot_promote():
    """`_WantsToPromote` returns a truthy string. `not "OVERWHELMING"` is False, so it permits —
    it cannot make a Success into an Overwhelming, which is the abuse it is named for."""
    ext = _WantsToPromote()
    assert degree_from_net(2, 2, extension=ext) is Degree.PARTIAL      # margin 0 — met, not exceeded
    assert degree_from_net(4, 2, extension=ext) is Degree.SUCCESS      # margin 2
    assert degree_from_net(5, 2, extension=ext) is Degree.OVERWHELMING # margin 3, and it PERMITS
    assert degree_from_net(1, 2, extension=ext) is Degree.FAILURE      # margin -1


def test_the_lower_bands_never_consult_the_extension_at_all():
    """A raising extension proves the branch is unreachable below the top band.

    Stronger than checking the returned band: if the ladder consulted it anywhere else, these
    calls would raise rather than return.
    """
    ext = _Raises()
    assert degree_from_net(-1, 2, extension=ext) is Degree.FAILURE
    assert degree_from_net(2, 2, extension=ext) is Degree.PARTIAL
    assert degree_from_net(3.5, 2, extension=ext) is Degree.SUCCESS
    with pytest.raises(RuntimeError, match="extension exploded"):
        degree_from_net(5, 2, extension=ext)


def test_an_undeclared_context_key_is_refused_not_swallowed():
    """The silent-no-op hole: `**context` used to accept anything, and an extension defaulting
    its parameter turned a misspelled key into a band change with no error."""
    from systems.social_contest.sim.contest.degree_extension import CONTEST_DEGREE_EXTENSION as C

    assert degree_from_net(6, 2, extension=C, pool=20) is Degree.SUCCESS
    with pytest.raises(TypeError, match="does not declare context key"):
        degree_from_net(6, 2, extension=C, poool=20)


def test_an_extension_declaring_nothing_accepts_nothing():
    """Strict by default: a new extension that forgets to declare fails loudly on first call
    rather than abstaining forever."""
    assert _AlwaysVeto().context_keys == ()
    with pytest.raises(TypeError, match="does not declare context key"):
        degree_from_net(6, 2, extension=_AlwaysVeto(), pool=8)


def test_no_extension_means_the_unmodified_ladder():
    for net, ob in DOMAIN:
        assert degree_from_net(net, ob, extension=None) is _unextended(net, ob)


# ── What the seam does NOT guarantee, pinned so the stronger reading cannot stand ──────

def test_the_seam_is_not_a_sandbox():
    """An extension reaching OUTSIDE its contract can do more, and that is stated, not hidden.

    The honest claim is "an extension confined to its contract cannot express any band change but
    3 -> 2", and the difference matters: a reader who takes "structural" to mean "sandboxed" will
    trust an untrusted extension. This test documents the escape by exercising it — and restores
    the table afterwards, because leaving it mutated would poison every later test in the worker.
    """
    original = dict(DE.DEGREE_ORDINAL)

    class _Hostile(BandExtension):
        name = "probe:hostile"

        def may_overwhelm(self, net, ob, **context):
            DE.DEGREE_ORDINAL[Degree.SUCCESS] = 3     # reaches around the seam entirely
            return False

    try:
        assert degree_from_net(5, 2, extension=_Hostile()) is Degree.SUCCESS
        assert DE.DEGREE_ORDINAL[Degree.SUCCESS] == 3, (
            "the hostile extension failed to mutate the owner's table — if the engine has since "
            "made DEGREE_ORDINAL immutable, that is a real strengthening and this test should be "
            "rewritten to assert it, not deleted"
        )
    finally:
        DE.DEGREE_ORDINAL.clear()
        DE.DEGREE_ORDINAL.update(original)

    assert DE.DEGREE_ORDINAL == original
