"""examples.py -- the worked examples and discriminating runs for the esoteric-concepts proposal, generated from the LIVE
combat module.

PROPOSED, NOT WIRED. Nothing under modules/, engine/ or systems/ is edited, and nothing is added to the engine's tables in
this process either: every technique used here is a LIVE ability (`ability_primitives.ABILITIES`), every number is computed
by the engine's own functions, and the one configuration overlay used (Part 7.3, the drains set to 0) is passed through
`modules.combat.fight.fight`'s own `cfg` argument, the workbench overlay the entry already takes (`fight.py:147-149`).

    python -I proposals/2026-11-20-pc-esoteric-concepts-to-levers/examples.py > proposals/2026-11-20-pc-esoteric-concepts-to-levers/07_worked_examples.md
    python -I proposals/2026-11-20-pc-esoteric-concepts-to-levers/examples.py --check     # this script's own falsifiers

WHAT IS TYPED (not computed): the build choices (weapon, armour, attributes, levels), the seed key and the prose. Every
figure in a table is a return value of `modules.combat`.

STUB DRAWS. Three discriminators call a pure engine function that takes a draw (`counter_select`, `read_contest`,
`commit_depth`). They are handed a stub whose `random()` returns a fixed number, so the function returns its decision for
that number; the probability is recovered by bisection on the number (`_prob_of`). The function's own formula is never
re-typed here.
"""
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, REPO)

from modules.combat import combat_systems as S                # noqa: E402
from modules.combat import tradition as TR                    # noqa: E402
from modules.combat import fight as FIGHT                     # noqa: E402
from modules.combat import wrapper as W                       # noqa: E402
from modules.combat import vocabulary as V                    # noqa: E402
from modules.combat import ability_primitives as AP           # noqa: E402
from modules.combat.combatant import Combatant                # noqa: E402
from modules.combat.config import CFG                         # noqa: E402
from engine.dice_engine import draw                           # noqa: E402
from engine.season.queries.inputs import PersonalCombatInput  # noqa: E402

SEED_KEY = 'pc_esoteric_examples'
N = 600            # paired seeds per arm; the 95% half-width of a win share near 50% is about 4 points at this n


# ── helpers ──────────────────────────────────────────────────────────────────────────────────────────────────────────
class _Fixed:
    """A stub draw: `random()` returns `u`; `below(k)` returns 0; `beta(a, b)` returns 0.5."""
    def __init__(self, u):
        self.u = u

    def random(self):
        return self.u

    def below(self, k):
        return 0

    def beta(self, a, b):
        return 0.5


def _prob_of(decide):
    """P(decide(stub) is True) for a decision of the form `rng.random() < p`, by bisection on the stub's number."""
    lo, hi = 0.0, 1.0
    if decide(_Fixed(1.0 - 1e-12)):
        return 1.0
    if not decide(_Fixed(0.0)):
        return 0.0
    for _ in range(50):
        mid = (lo + hi) / 2
        if decide(_Fixed(mid)):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _live(c):
    """Live state as the wrapper sets it at a fight's start (`wrapper._init_live`)."""
    W._init_live(c, CFG)
    return c


def _record(a, b, cfg_overlay=None):
    """A PersonalCombatInput for two builds (dicts with weapon, armour, tradition, techniques, disp, attrs)."""
    return PersonalCombatInput(
        claimants=('A', 'B'), ends=(a.get('end', 4), b.get('end', 4)), wound_quantities=('felled', 'wounds'),
        kits=((a['weapon'], a['armour']), (b['weapon'], b['armour'])), scores=(3, 3),
        attributes=(a.get('attrs', {}), b.get('attrs', {})),
        traditions=(a['tradition'], b['tradition']), techniques=(dict(a.get('tech', {})), dict(b.get('tech', {}))),
        axes=({}, {}), dispositions=(a.get('disp', 4), b.get('disp', 4)))


def _fights(a, b, n=N, cfg=None, tag=''):
    """Run n keyed fights; yield each trace. The same seeds for every arm (paired)."""
    for s in range(n):
        out = FIGHT.fight(_record(a, b), draw.seeded(draw.H2(SEED_KEY + tag, s)), cfg=cfg)
        yield out.trace


def _pct(x):
    return f"{100 * x:.1f}%"


def _f(x, d=3):
    return f"{x:.{d}f}"


# ── Part 7.1: stillness — temperament against the counter lever ─────────────────────────────────────────────────────
def stillness_arms():
    base = dict(weapon='arming', armour='light', tradition='italian')
    arms = [('temper 4 (neutral; control)', dict(base, disp=4)),
            ('temper 3', dict(base, disp=3)),
            ('temper 2', dict(base, disp=2)),
            ('temper 1 (most still)', dict(base, disp=1)),
            ('temper 4 + mezzo_tempo L1', dict(base, disp=4, tech={'mezzo_tempo': 1})),
            ('temper 4 + mezzo_tempo L2', dict(base, disp=4, tech={'mezzo_tempo': 2})),
            ('temper 4 + mezzo_tempo L3', dict(base, disp=4, tech={'mezzo_tempo': 3}))]
    opponents = [('opponent temper 4', dict(base, disp=4)),
                 ('opponent temper 7 (presses)', dict(base, disp=7)),
                 ('opponent temper 1 (also waits)', dict(base, disp=1))]
    return arms, opponents


def counter_reach(build):
    """P(the counter is reached for), from the live `counter_select`, for this build as defender."""
    c = _live(Combatant('A', weapon=build['weapon'], armor=build['armour'], tradition=build['tradition'],
                        equipped=dict(build.get('tech', {})), disp=build.get('disp', 4)))
    return _prob_of(lambda r: S.counter_select(c, CFG, r, TR))


def room_rows():
    """The swing room in a closed exchange and the commit window it leaves (live `range_utilization`, `_commit_range_factor`)."""
    rows = []
    for gap in (0.0, 0.3, 1.0, 3.0):
        room = S.range_utilization(None, gap, CFG)
        rows.append((gap, room, 2.0 + 3.0 * S._commit_range_factor(room, CFG)))
    return rows


def stillness_measure(a, b, n=N, cfg=None):
    deep = (cfg or CFG)['DEEP_COMMIT']
    wins = a_commits = a_deep = opened = a_attacks = a_punished = 0
    sig = []
    for trace in _fights(a, b, n, cfg=cfg, tag='/still'):
        last_commit = None
        for e in trace:
            k = e['kind']
            if k == 'commit':
                last_commit = e
                if e['aggressor'] == 'A':
                    a_commits += 1
                    a_deep += e['commit'] >= deep
            elif k == 'read' and last_commit is not None:
                if e['defender'] == 'A' and last_commit['commit'] >= deep and e['read_win']:
                    opened += 1          # the gate at wrapper.py:325 is open for A this exchange
            elif k == 'roll' and e['aggressor'] == 'A':
                sig.append(e['net_sigma'])
            elif k == 'outcome' and e['aggressor'] == 'A':
                a_attacks += 1
                a_punished += bool(e['riposte'])
            elif k == 'fight_result':
                wins += e.get('winner') == 'A'
    return dict(win=wins / n, deep=a_deep / max(1, a_commits), opened=opened / n,
                punished=a_punished / max(1, a_attacks), sigma=sum(sig) / max(1, len(sig)))


def part_7_1(n):
    arms, opponents = stillness_arms()
    out = ["## 7.1 Stillness (CP-06, CP-07, JP-05): temperament against the counter lever", "",
           "**Source passages.** Huang Zongxi, *Epitaph for Wang Zhengnan* (1669): \"有所謂內家者，以靜制動，犯者應手即仆\" "
           "(\"there is what is called the internal school, which uses stillness to control movement; whoever attacks it "
           "falls at the touch of the hand\") [PERIOD-TEXT; V: zh.wikisource 王征南墓誌銘; the sheet's gloss]. The Push-Hands "
           "Song couplet: \"彼不動，己不動；彼微動，己先動\" [LATER-CLASSIC; V: zh.wikisource 太極拳經]. Munenori: \"you obtain "
           "the victory by having your opponent make the first move\", and the cost, \"if you do not think your opponent will "
           "attack, you will be set upon quickly and severely\" [PERIOD-TEXT; V: WILSON].",
           "",
           "**The two nearest engine quantities.** (a) the fighter's temperament, `disp` (`combat_systems.py:171-174`), which "
           "skews his own commitment shallow (`:989-994`), raises his reach for the counter by `1 − 0.5·lean` (`:1029`) and "
           "drifts his Vor down every beat (`wrapper.py:165`); (b) a technique on the `counter_select` lever (live: "
           "`mezzo_tempo`, ×1.4 per level, `ability_primitives.py:36-37`), which raises only the reach.",
           "",
           "**The observation that separates them.** The tradition's stillness has two halves: *not breaking one's own posture* "
           "and *answering the one who breaks his*. Only (a) moves the first half, which shows as fewer of the still fighter's "
           "own commits being deep and fewer of his own attacks being punished by a riposte; (b) leaves both untouched. Both "
           "need the opponent to break posture: against an opponent who also waits, the door at `wrapper.py:325` (a won read "
           "against a deep commit) opens less often for either.",
           "",
           f"Builds: both fighters Italian, arming sword, light armour, every attribute at its default; {n} keyed fights per "
           "cell, the same seeds in every cell. *Reach for the counter* is the live `counter_select` probability for A as "
           "defender. *Door open* is the mean number per fight of exchanges in which B committed deep and A won the read. "
           "*Own deep* is the share of A's commits at or above `DEEP_COMMIT`. *Punished* is the share of A's attacks answered "
           "by a riposte. *A's σ* is the mean net sigma of A's rolls (the cost: shallow attacks carry less).", ""]
    for oname, ob in opponents:
        out += [f"**Against {oname}.**", "",
                "| A's build | reach for the counter | door open / fight | own deep | punished | A's σ | A wins |",
                "|---|---|---|---|---|---|---|"]
        for aname, ab in arms:
            m = stillness_measure(ab, ob, n)
            out.append(f"| {aname} | {_pct(counter_reach(ab))} | {_f(m['opened'], 2)} | {_pct(m['deep'])} | "
                       f"{_pct(m['punished'])} | {_f(m['sigma'])} | {_pct(m['win'])} |")
        out.append("")
    out += ["**Why the door so rarely opens: the swing room in a closed exchange.** The commit is drawn over `[2, 2 + 3·f]`, "
            "where `f` is `_commit_range_factor` of the room (`combat_systems.py:403-411`, `:993-994`), and the room in a "
            "closed exchange is `range_utilization` of a measure gap the close has already shrunk to `CLOSE_GAP_REF` or less "
            "(`:391-401`; `wrapper.py:169`, `:255-257`). Live values:", "",
            "| measure gap | room | highest commit the window allows (`DEEP_COMMIT` is "
            f"{CFG['DEEP_COMMIT']}) |", "|---|---|---|"]
    for gap, room, top in room_rows():
        out.append(f"| {gap} | {_f(room)} | {_f(top)} |")
    opened_world = dict(CFG, DEEP_COMMIT=3.0)
    out += ["",
            "**The same question in a world where the door can open.** Both fighters, `DEEP_COMMIT` set to 3.0 through the "
            "overlay argument (it also moves the other sites that read it: the displace-and-step-inside branch, "
            "`wrapper.py:387`, the over-committed closer's reopen moment, `:401`, and the centre of the Indes scale, "
            "`combat_systems.py:1023`). It approximates what workplan v12 B15.04 would do (the deep tier at the window's "
            "upper third, not built on this branch) and, for everyone, what the jobs set's `counter_shallow` gate would do "
            "for a set's holder; it is not a proposal to change the constant.", "",
            "| opponent | A's build | door open / fight | own deep | punished | A's σ | A wins |",
            "|---|---|---|---|---|---|---|"]
    picks = [arms[0], arms[3], arms[6]]
    for oname, ob in opponents:
        for aname, ab in picks:
            m = stillness_measure(ab, ob, n, cfg=opened_world)
            out.append(f"| {oname} | {aname} | {_f(m['opened'], 2)} | {_pct(m['deep'])} | {_pct(m['punished'])} | "
                       f"{_f(m['sigma'])} | {_pct(m['win'])} |")
    out.append("")
    return out


# ── Part 7.2: yielding — does the engine's feel grow with the opponent's force? ─────────────────────────────────────
def bind_p(a, b):
    return S.bind_dominance_p(S.bind_sigma(a, b, CFG, TR))


def _bind_pair(tech_a, str_b, weapon='longsword'):
    a = _live(Combatant('A', weapon=weapon, armor='light', tradition='german', equipped=dict(tech_a)))
    b = _live(Combatant('B', weapon=weapon, armor='light', tradition='german', strength=str_b))
    return a, b


def part_7_2(n):
    from math import log
    lg = lambda p: log(p / (1 - p))
    out = ["## 7.2 Yielding (CP-04, CP-05, EU-07): the engine's feel is a constant, not a conversion of force", "",
           "**Source passages.** Taijiquan Lun: \"人剛我柔謂之走\" (\"when the other is hard and I am soft, this is called "
           "yielding\"); \"察「四兩撥千斤」之句，顯非力勝\" (\"examine the saying 'four ounces deflect a thousand pounds': "
           "clearly it is not victory by strength\") [LATER-CLASSIC; V: zh.wikisource 太極拳經; the sheet's gloss]. Ringeck on "
           "*Fühlen*: \"notice — right in the moment when the blades make contact — whether he has bound hard or soft\" "
           "[PERIOD-TEXT; V: Ringeck page], and the windings keyed on it, doubling against the strong, mutating against the "
           "soft [HEMA sheet §3, Pseudo-Danzig].",
           "",
           "**The two nearest engine quantities.** (a) the `tactile` lever, which multiplies each side's own read in the bind "
           "(`combat_systems.py:936-940`; live generic `blade_feel_refined`, ×1.5 per level, German); (b) the `leverage` "
           "lever, a log-odds shift on the same contest (`:934`; live `staerke_schwaeche`, ×1.2 per level, German).",
           "",
           "**The observation that separates them, and tests the claim.** The tradition's claim is that the yielder's edge "
           "comes *from* the opponent's force: it should grow as he presses harder. In the engine, the opponent's force in the "
           "bind is his Strength (`BIND_STR_K`, `:941`) and his lever arm. Sweep the opponent's Strength and read A's "
           "probability of dominating one bind iteration, `bind_dominance_p(bind_sigma(A, B))` (`:1303-1305`), A the "
           "aggressor, both German, both with a longsword.",
           "",
           "| A's technique | B's Strength 4 | 5 | 6 | 7 | A's gain over no technique, in log-odds, at Strength 4 / 7 |",
           "|---|---|---|---|---|---|"]
    rows = [('none', {}), ('blade_feel_refined L1', {'blade_feel_refined': 1}),
            ('blade_feel_refined L3', {'blade_feel_refined': 3}), ('staerke_schwaeche L1', {'staerke_schwaeche': 1}),
            ('staerke_schwaeche L3', {'staerke_schwaeche': 3})]
    base = {s: bind_p(*_bind_pair({}, s)) for s in (4, 5, 6, 7)}
    for name, tech in rows:
        ps = {s: bind_p(*_bind_pair(tech, s)) for s in (4, 5, 6, 7)}
        g4, g7 = lg(ps[4]) - lg(base[4]), lg(ps[7]) - lg(base[7])
        out.append(f"| {name} | {_pct(ps[4])} | {_pct(ps[5])} | {_pct(ps[6])} | {_pct(ps[7])} | "
                   f"{_f(g4)} / {_f(g7)} |")
    out += ["",
            "**In whole fights.** The same question asked of the result: a weak fighter (Strength 3) against a strong one "
            "(Strength 6), and an even pair (4 against 4), each with and without `blade_feel_refined` at level 3 on A; "
            f"longswords, light armour, German, {n} keyed fights per cell. *Binds* is the mean number of bind entries per "
            "fight (`outcome` events with `bind` true).", "",
            "| pairing | A wins, no technique | A wins, feel L3 | gain | binds / fight |", "|---|---|---|---|---|"]
    for label, sa, sb in (('even (4 v 4)', 4, 4), ('weak v strong (3 v 6)', 3, 6)):
        a0 = dict(weapon='longsword', armour='light', tradition='german', attrs={'attr.body.strength': sa})
        b0 = dict(weapon='longsword', armour='light', tradition='german', attrs={'attr.body.strength': sb})
        a1 = dict(a0, tech={'blade_feel_refined': 3})
        w0 = w1 = binds = 0
        for t0, t1 in zip(_fights(a0, b0, n, tag='/yield'), _fights(a1, b0, n, tag='/yield')):
            w0 += any(e['kind'] == 'fight_result' and e.get('winner') == 'A' for e in t0)
            w1 += any(e['kind'] == 'fight_result' and e.get('winner') == 'A' for e in t1)
            binds += sum(1 for e in t0 if e['kind'] == 'outcome' and e['bind'])
        out.append(f"| {label} | {_pct(w0 / n)} | {_pct(w1 / n)} | {100 * (w1 - w0) / n:+.1f} pts | {binds / n:.2f} |")
    out.append("")
    return out


# ── Part 7.3: the stopping mind — Concentration against the read lever ──────────────────────────────────────────────
def mind_measure(a, b, n=N, cfg=None, tag='/mind'):
    before, after, wins = [], [], 0
    for trace in _fights(a, b, n, cfg=cfg, tag=tag):
        hit = False
        for e in trace:
            if e['kind'] == 'wound' and e['victim'] == 'A':
                hit = True
            elif e['kind'] == 'read' and e['defender'] == 'A':
                (after if hit else before).append(e['p_read_win'])
            elif e['kind'] == 'fight_result':
                wins += e.get('winner') == 'A'
    mb = sum(before) / max(1, len(before))
    ma = sum(after) / max(1, len(after))
    return dict(before=mb, after=ma, gap=ma - mb, nb=len(before), na=len(after), win=wins / n)


def part_7_3(n):
    base = dict(weapon='arming', armour='heavy', tradition='german')
    drain_off = dict(CFG, CONC_DRAIN_HIT=0.0, CONC_DRAIN_LOSS=0.0)
    arms = [('control (no technique, default Focus)', base, None),
            ('`keen_eye_basic` L2 (visual ×1.21)', dict(base, tech={'keen_eye_basic': 2}), None),
            ('`keen_eye_basic` L4 (visual ×1.46)', dict(base, tech={'keen_eye_basic': 4}), None),
            ('Focus 5 (Concentration 21 against 15)', dict(base, attrs={'attr.mind.focus': 5}), None),
            ('both fighters: the drains on a hit and on a lost riposte set to 0', base, drain_off)]
    out = ["## 7.3 The stopping mind (JP-01, JP-03, CP-12): Concentration against the read lever", "",
           "**Source passages.** Takuan, *Fudōchi shinmyōroku*: \"the moment your attention is drawn to the slashing blade of "
           "your opponent, you rush to meet his attack at that place, with the result that your mind becomes attached there "
           "to your opponent's blade, so that you lose your free functioning and can be slain\"; and *fudōchi*, \"Confronting "
           "the ten different opponents, your mind responds ten different times, but if you never attach your mind to any one "
           "of the attackers, … your free functioning will never waver\" [PERIOD-TEXT; V: HASKEL pp.33-35].",
           "",
           "**The two nearest engine quantities.** (a) Concentration: drained by a hit taken (`wrapper.py:411`, `:217`, "
           "`:249`, `:437`) and a lost riposte (`:445`), read back into the defender's read through `mental_fatigue` "
           "(`combat_systems.py:1285-1289`, `:1004`) and into his response through `consistency` (`:1281-1283`, `:340`); "
           "(b) the read levers, `visual` (`:1004`, `:1011`; live generic `keen_eye_basic`, ×1.1 per level, German).",
           "",
           "**The observation that separates them.** Takuan's failure is caused by the blow that captured the mind: it is "
           "worse *after* being struck than before. So read the engine's own probability that the defender wins the read "
           "(`p_read_win`, emitted by `read_contest`, `wrapper.py:310-311`) for A as defender, before A has taken a wound and "
           "after. A read lever should lift both; a Concentration effect should close the gap between them.",
           "",
           f"Builds: both German, arming sword, heavy armour (longer fights, so more reads after a wound), attributes at "
           f"default unless named; {n} keyed fights per arm. The last arm changes the configuration for both fighters through "
           "`fight.fight`'s overlay argument; it is a world in which no blow drains the mind, not a technique.", "",
           "| arm | A's p(read) before a wound | after | gap | reads before / after |",
           "|---|---|---|---|---|"]
    for name, a, cfg in arms:
        m = mind_measure(a, base, n, cfg=cfg)
        out.append(f"| {name} | {_pct(m['before'])} | {_pct(m['after'])} | {100 * m['gap']:+.2f} pts | "
                   f"{m['nb']} / {m['na']} |")
    out += ["",
            "**The magnitude chain, from the live functions.** A default fighter (Focus 3, Spirit 3: Concentration 15) after "
            "k hits taken, each draining `CONC_DRAIN_HIT` "
            f"({CFG['CONC_DRAIN_HIT']}): the response term `LAPSE_K·consistency` added inside `mode_sigma` (`:340`), and the "
            "factor on the defender's read, `1 − MENTAL_FAT_READ_K·mental_fatigue` (`:1004`), at a stamina fatigue of 0.5. "
            "For scale, one level of `keen_eye_basic` multiplies the read by 1.1.", "",
            "| hits taken | Concentration | LAPSE term on the response (σ) | read factor at fatigue 0.5 |", "|---|---|---|---|"]
    for k in range(0, 8, 2):
        c = _live(Combatant('A', weapon='arming', armor='heavy', tradition='german'))
        c.conc = max(0.0, c.conc_max - k * CFG['CONC_DRAIN_HIT'])
        lapse = CFG['LAPSE_K'] * S.consistency(c, CFG)
        rf = 1 - CFG['MENTAL_FAT_READ_K'] * S.mental_fatigue(c, 0.5, CFG)
        out.append(f"| {k} | {c.conc:g} | {lapse:+.4f} | {rf:.4f} |")
    out.append("")
    return out


# ── discriminating runs for rows outside the worked examples ────────────────────────────────────────────────────────
def discriminators():
    out = ["## 7.4 Discriminating runs for three more rows", ""]
    # CM-04 qinggong: Agility against the balance lever
    def pair(agi=4, tech=None):
        d = _live(Combatant('D', weapon='arming', armor='light', tradition='spanish', agi=agi, equipped=dict(tech or {})))
        a = _live(Combatant('X', weapon='arming', armor='light', tradition='spanish'))
        return a, d
    rows = [('control', pair()), ('Agility 5', pair(agi=5)), ('`footing_refined` L2 (balance ×2.25)',
                                                               pair(tech={'footing_refined': 2}))]
    out += ["**CM-04, 輕功 lightness.** The dodge (`mode_sigma`, `combat_systems.py:309-341`, at commit 3 and a won read), "
            "the defender's reach-and-footwork term against an equal attacker (`reach_sigma`, `:778-792`; positive lowers "
            "the attacker's net), and the closing rate as the shorter fighter (`close_rate`, `:1220-1227`). Spanish "
            "fighters, arming swords.", "",
            "| defender | dodge σ | reach_sigma (footwork) | close_rate |", "|---|---|---|---|"]
    for name, (a, d) in rows:
        er = {a: S.reach_base(a, CFG), d: S.reach_base(d, CFG)}
        dodge = S.mode_sigma(V.DEF_DODGE, a, d, 3.0, True, 0.0, CFG)
        rs = S.reach_sigma(a, d, er, 0.0, 0.0, CFG, TR)
        cr = S.close_rate(d, 0.0, 0.0, 1.0, CFG)
        out.append(f"| {name} | {_f(dodge, 4)} | {_f(rs, 4)} | {_f(cr, 4)} |")
    out.append("")
    # CM-07 Dugu: the formless fighter is the most legible
    out += ["**CM-07, 無招勝有招 no move beats move.** A German defender reads attackers of four traditions: the live "
            "`read_contest` (`combat_systems.py:997-1017`) returns the probability he wins the read (`p_read`), and the live "
            "`commit_depth` (`:980-995`) returns the Beta parameters of the attacker's commitment against him (equal "
            "parameters: no wariness). Arming swords, every attribute at default, commit 3.5.", "",
            "| attacker's tradition | familiarity (`traditions.py:40-48`) | defender's p(read) | attacker's Beta (a, b) |",
            "|---|---|---|---|"]
    for trad in ('none', 'german', 'italian', 'japanese'):
        att = _live(Combatant('X', weapon='arming', armor='light', tradition=trad))
        dfn = _live(Combatant('D', weapon='arming', armor='light', tradition='german'))
        rc = S.read_contest(att, dfn, 3.5, S.consistency(att, CFG), 0.0, 0.0, CFG, _Fixed(0.0), TR)
        _, ba, bb, _ = S.commit_depth(att, dfn, CFG, _Fixed(0.5), TR)
        out.append(f"| {trad} | {TR.familiarity('german', trad):.2f} | {_pct(rc['p_read'])} | ({_f(ba)}, {_f(bb)}) |")
    out.append("")
    # JP-06 hyoshi: one's own tempo factor lowers the opponent's readiness
    out += ["**JP-06, 無拍子 out of rhythm.** The anticipation factor on each fighter's readiness (`tempo_pressure`, "
            "`combat_systems.py:1173-1198`) at equal Vor, A with `timing_refined` (×1.5 per level, Italian), B without.", "",
            "| A's level | A's tempo_pressure | B's tempo_pressure |", "|---|---|---|"]
    for lvl in (0, 1, 2, 3):
        a = _live(Combatant('A', weapon='arming', armor='light', tradition='italian', equipped={'timing_refined': lvl}))
        b = _live(Combatant('B', weapon='arming', armor='light', tradition='italian'))
        out.append(f"| {lvl} | {_f(S.tempo_pressure(a, b, CFG, TR), 4)} | {_f(S.tempo_pressure(b, a, CFG, TR), 4)} |")
    out.append("")
    return out


def check():
    """Falsifiers for this script: (1) every technique named is LIVE and gated to the tradition it is used with; (2) an empty
    board fights byte-identically to no technique argument over 20 seeds; (3) the stub bisection recovers a known
    probability from the live counter_select (a neutral fighter's base reach) to 1e-9 of the value the engine's own pieces
    give; (4) the drain overlay changes something (it is not a no-op)."""
    checked = 0
    for name, trad in (('mezzo_tempo', 'italian'), ('blade_feel_refined', 'german'), ('staerke_schwaeche', 'german'),
                       ('keen_eye_basic', 'german'), ('footing_refined', 'spanish'), ('timing_refined', 'italian')):
        assert name in AP.ABILITIES and AP.ABILITIES[name]['tradition'] == trad, name
        checked += 1
    base = dict(weapon='arming', armour='light', tradition='german')
    for s in range(20):
        t0 = FIGHT.fight(_record(base, base), draw.seeded(draw.H2(SEED_KEY + '/check', s))).trace
        t1 = FIGHT.fight(_record(dict(base, tech={}), base), draw.seeded(draw.H2(SEED_KEY + '/check', s))).trace
        assert t0 == t1, s
        checked += 1
    c = _live(Combatant('A', weapon='arming', armor='light', tradition='italian'))
    p = _prob_of(lambda r: S.counter_select(c, CFG, r, TR))
    assert abs(p - CFG['COUNTER_SELECT_BASE']) < 1e-9, p      # neutral build: every factor is 1 (ability_primitives.py:196-207)
    checked += 1
    heavy = dict(weapon='arming', armour='heavy', tradition='german')
    m0 = mind_measure(heavy, heavy, 40, tag='/check')
    m1 = mind_measure(heavy, heavy, 40, cfg=dict(CFG, CONC_DRAIN_HIT=0.0, CONC_DRAIN_LOSS=0.0), tag='/check')
    assert (m0['after'], m0['na']) != (m1['after'], m1['na']), 'the drain overlay changed nothing'
    checked += 1
    assert checked >= 28, checked
    print(f"check: {checked} assertions held")


def main(argv):
    if '--check' in argv:
        check()
        return
    n = N
    lines = ["# Part 7 — Worked examples, generated from the live engine", "",
             "## Status: PROPOSED. Reference only. GENERATED by `examples.py` (`python -I proposals/2026-11-20-pc-esoteric-"
             "concepts-to-levers/examples.py > …/07_worked_examples.md`); edit the script, not this file. Every figure in a "
             "table is a return value of `modules.combat`, imported by its package path; the builds and the prose are typed. "
             "The reading of each table is in Part 7's commentary, `07_worked_examples_part2.md`.", ""]
    lines += part_7_1(n)
    lines += part_7_2(n)
    lines += part_7_3(n)
    lines += discriminators()
    print("\n".join(lines))


if __name__ == '__main__':
    main(sys.argv[1:])
