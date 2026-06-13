"""
tradition_gate.py -- ILLUSTRATIVE sketch of the tradition imposition-gate mechanism (design proposal;
companion to combat_tradition_state_graph_gates_2026-06-13.md). NOT wired into the engine, NOT balance-
validated -- it demonstrates that the §1 contest produces tradition-distinct, opponent-sensitive,
mirror-fair imposition odds from the REAL channel competences. Jordan-vetoable. No canon touched.

THE IDEA (replacing flat `channel_weight x sigma` tuning):
  Each tradition has a PREFERRED NODE in the bout state graph and a DEFINING CHANNEL it imposes with.
  At a transition, both fighters "pull" the exchange toward their own node using their defining channel;
  whoever wins the opposed, familiarity-bounded contest routes the exchange into THEIR node. The gate sets
  the TERMS (which node), not the OUTCOME (the node still has to be won) -- so the channel weights survive
  as the in-node competence, and the new layer is purely structural. The advantage is EARNED (win your
  characteristic contest) not asserted (a flat multiplier).

Grounding for the node/channel map: manual-vs-combat-v32-bridge.md + martial_traditions_synthesis.md
(see the proposal doc §2 for the per-row citations). The CONTENT is the corpus's; this is the mechanism.
"""
from math import exp
import sys
sys.path.insert(0, '/home/claude/combat_engine')
import tradition as TR

# preferred (node, defining channel) per tradition -- the corpus's preferred-fight, made structural.
PREFERRED = {
    'german':   ('bind',          'tactile'),    # Bind Fighter: drag it into the Krieg/Winden
    'italian':  ('counter',       'tempo'),       # Thrust Duelist: the stop-hit / single-time counter at measure
    'spanish':  ('measure_hold',  'measure'),     # Destreza: hold the circulo, deny the close (atajo)
    'japanese': ('counter',       'precommit'),   # koryu: seize at the commit (sen-no-sen) -> the counter
    'english':  ('counter',       'tempo'),       # Silver true-times: the clean counter, refuse over-commit
    'chinese':  ('burst',         'leverage'),    # fa jin: the explosive burst from reach
    'filipino': ('flow',          'tactile'),     # continuous-flow: sustain the exchange
    'none':     (None,            None),          # no tradition -> imposes nothing (neutral)
}

# sim-tunable (Class-C); set against the harness once wired. Lower = sharper imposition for a given edge.
IMPOSE_SCALE = 0.8


class _F:
    """minimal stand-in: a tradition + the stats `reading` needs (engine reading = (2cog+att)/3 +
    0.2*(history-3)); default stats isolate the channel/tradition effect."""
    def __init__(self, tradition, cog=3, att=3, history=3, equipped=()):
        self.tradition = tradition; self.cog = cog; self.att = att; self.history = history
        self.equipped = equipped


def _reading(c):
    return (2 * c.cog + c.att) / 3 + 0.2 * (c.history - 3)


def pull(c, opp):
    """How hard `c` pulls the exchange toward its preferred node: reading x defining-channel competence x
    how well c reads opp (familiarity). Returns (pull_magnitude, node)."""
    node, ch = PREFERRED.get(c.tradition, (None, None))
    if node is None:
        return 0.0, None
    return _reading(c) * TR.eff_cw(c, ch) * TR.familiarity(c.tradition, opp.tradition), node


def impose_probability(a, b):
    """P(a imposes a's node) in the opposed style-clash. Symmetric, logistic on the pull difference.
    Mirror -> 0.50; vs a styleless opponent -> high; cross-tradition -> a channel-strength contest."""
    pa, na = pull(a, b)
    pb, nb = pull(b, a)
    if na is None:
        return 0.0
    if nb is None:
        return 1.0 / (1.0 + exp(-(pa) / IMPOSE_SCALE))      # opponent imposes nothing
    return 1.0 / (1.0 + exp(-(pa - pb) / IMPOSE_SCALE))


def resolve_imposition(a, b, rng):
    """Route the transition: returns (imposer, node) or (None, None) if neither has a node. The wrapper
    would translate `node` into the matching transition (bind-entry / counter / reopen / burst-continue)."""
    pa, na = pull(a, b); pb, nb = pull(b, a)
    if na is None and nb is None:
        return None, None
    if rng.random() < impose_probability(a, b):
        return a, na
    return b, nb


# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    TRADS = ['german', 'italian', 'spanish', 'japanese', 'english', 'chinese', 'filipino', 'none']

    print("== preferred node + defining channel per tradition (the corpus's preferred-fight, made structural) ==")
    for t in TRADS:
        n, c = PREFERRED[t]
        print(f"  {t:9s} -> node={str(n):13s} via channel={c}")

    print("\n== mirror check: same tradition imposes symmetrically -> 0.50 (default fighters unaffected) ==")
    for t in TRADS:
        if PREFERRED[t][0] is None:
            continue
        p = impose_probability(_F(t), _F(t))
        print(f"  {t:9s} vs {t:9s}: P(impose) = {p:.3f}   {'OK' if abs(p-0.5)<1e-6 else 'MISMATCH'}")

    print("\n== illustrative matchups (the style clash; the node each would impose) ==")
    def show(ta, tb):
        a, b = _F(ta), _F(tb)
        p = impose_probability(a, b)
        na = PREFERRED[ta][0]; nb = PREFERRED[tb][0]
        clash = 'same node' if na == nb else f"clash: {na} vs {nb}"
        print(f"  {ta:9s} vs {tb:9s}: P({ta} imposes {str(na):12s}) = {p:.3f}   ({clash})")
    show('german', 'italian')      # Bind Fighter drags the duelist toward the bind; duelist pulls to the counter
    show('italian', 'german')      # the reverse view
    show('german', 'none')         # vs a styleless fighter: the tradition imposes its fight freely
    show('german', 'spanish')      # incompatible nodes (bind vs measure-hold) -- a real terms-of-engagement clash
    show('italian', 'english')     # compatible: both route to the counter node
    show('japanese', 'italian')    # both pull to the counter (sen-no-sen vs contratempo) -- compatible
    show('chinese', 'spanish')     # burst-from-reach vs hold-the-circulo -- the reach/measure clash
    show('filipino', 'german')     # flow vs bind: who sets the exchange's shape

    print("\nNOTE: P is opponent-sensitive (channel-strength contest), 0.50 on the mirror, and high vs a")
    print("styleless fighter -- the mechanism is well-defined and tradition-distinct. Routing the actual")
    print("path in full fights + tuning IMPOSE_SCALE/boosts is the build step (unvalidated here).")
