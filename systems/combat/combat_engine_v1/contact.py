"""contact.py — L2 module for the post-opening grapple/contact resolution (D8/D9, I7b,
designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md).

Grab affinity derives from real primitives the schema actually supports — free-hand availability
(a dagger/unarmed-class weapon is already functionally at grapple range) and LEVERAGE
(systems.leverage, already grounded) + strength — NEVER a hook-hardware term. D9/JD-7 retracted the
pull-hook grab-hardware claim: no primitive in the schema separates a pull-hook from a bind-lug
(orient_deg interleaves guisarme/ji/guandao pulls against ranseur/spetum/bear_spear binds; `guard
type='lug'` appears on both), so a hand-authored `pull_capable`/`hook` boolean would be morally
identical to the `clinch` scalar D9 deletes — explicitly forbidden.

Callers (wrapper.py) own the `opening_created` flag: a real prior opening this beat (a bind, a
beaten-aside/slip-inside displace, or a deep-commit reopen moment) — never re-derived here."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
import math
import combat_systems as S

# ── contact axis (I7b) ──────────────────────────────────────────────────────────────────────────
def _short_reach_exempt(c, cfg):
    """Primitive-derived open-contact exemption (dagger/unarmed-class): a weapon short enough
    (head_len, METRES — U0/ED-PC-0002) offers no reach to lose by closing all the way to grapple range —
    GROUNDING: a physical threshold on the weapon's own head_len, never a name check. Clears the
    roster's dagger-class (dagger/rondel/stiletto/main_gauche/misericorde/cinquedea, head_len<=0.36)
    and excludes the next-shortest non-dagger record (paired_short / half-sworded 2H forms,
    head_len>=0.399) — [SIM-CALIBRATE] threshold."""
    return c.w['head_len'] <= cfg['GRAB_SHORT_REACH_M']


def grab_available(actor, opponent, opening_created, cfg):
    """The gate (D8/D9 acceptance 1): dagger/unarmed-class weapons need no opening — they are
    already at grapple range. Every other weapon-wielder needs a REAL prior opening THIS beat (bind
    / beaten-aside-or-slip-inside / deep-commit reopen — set by the caller's opening_created flag);
    a 2H weapon's own bind substitutes for a free hand (Ringen am Schwert — wrestling at the
    sword), a 1H weapon's off-hand is already free once that opening exists. No grapple path from
    open measure: this predicate is only ever consulted from the closed-exchange outcome tail."""
    if _short_reach_exempt(actor, cfg):
        return True
    return bool(opening_created)


def grab_sigma(actor, opponent, cfg):
    """Grab affinity: STRENGTH-dominant (a gross-motor grip/throw contest, unlike the blade-read
    bind_sigma mirrors) plus systems.leverage (control of the contact point) — NO hook-hardware
    term (D9/JD-7 retraction). +ve favours actor. Pure."""
    lev = S.leverage(actor, cfg) - S.leverage(opponent, cfg)
    strq = (actor.strength - opponent.strength) * cfg['GRAB_STR_K']
    edge = cfg['GRAB_EDGE_K'] * S.WP.grab_hazard(opponent.w) * (1.0 - actor.skill('grab'))   # U3/ED-PC-0018: seizing the opponent's LIVE edge bare-handed self-injures an unskilled/untimely grab -> lowers the actor's grab affinity; reads the GRABBED (opponent's) weapon hazard, mitigated by the actor's grab skill. K=0 until U9; 0 for an edgeless weapon.
    return strq + cfg['GRAB_LEV_K'] * lev - edge


# Branching grapple menu (Fiore's 2nd Remedy four-branch + a foot-pin/escape pair) — reachable
# across seeds; a flat escape chance first, then gsig-skewed weights over the rest. [SIM-CALIBRATE]
# weights. A single one-shot resolution — never loops, never mutates a caller's `beats` counter.
GRAB_OUTCOMES = ('disarm', 'throw', 'pin', 'control', 'foot_pin', 'escape')


def grab_outcome(gsig, rng, cfg):
    """Resolve one grapple attempt into a branch token. Pure aside from the rng draw; terminates in
    O(1) — does not re-enter any caller loop (in particular, never mutates the bind inner loop's
    `beats` counter, which lives entirely in wrapper.engagement and is never touched here)."""
    if rng.random() < cfg['GRAB_ESCAPE_P']:
        return 'escape'
    p = 1.0 / (1.0 + math.exp(-gsig))   # logistic squash of the dominance edge into [0,1]
    weights = (
        ('disarm',   0.15 + 0.25 * p),
        ('throw',    0.15 + 0.20 * p),
        ('pin',      0.15 + 0.15 * p),
        ('control',  0.35 - 0.25 * p),
        ('foot_pin', 0.10),
    )
    total = sum(w for _, w in weights)
    r = rng.random() * total
    acc = 0.0
    for name, w in weights:
        acc += w
        if r <= acc:
            return name
    return weights[-1][0]
