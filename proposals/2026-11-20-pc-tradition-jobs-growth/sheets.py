"""sheets.py -- legible character sheets for the tradition-board proposal, generated from the LIVE combat module.

PROPOSED, NOT WIRED. Nothing under modules/, engine/ or systems/ is edited. Run from anywhere:

    python -I proposals/2026-11-20-pc-tradition-jobs-growth/sheets.py                > 08_character_sheets.md
    python -I proposals/2026-11-20-pc-tradition-jobs-growth/sheets.py --curriculum   # the worked curricula, sets, counts
    python -I proposals/2026-11-20-pc-tradition-jobs-growth/sheets.py --check        # this script's own falsifiers

WHAT IS COMPUTED BY THE ENGINE (never typed here): every figure under "What the engine derives", every technique's
factor or bonus, every weapon fact, every familiarity, and the measured fights. They come from `modules.combat`
imported through its PACKAGE path (`from modules.combat import ...`), exactly as the host imports it.

WHAT IS PROPOSAL DATA (this file is its worked-example home; it is NOT the owner a build would read): the curricula,
columns, costs, slots, the attention rule, sets, gates, growth stages, and the values of NEW techniques. Each such
number is marked [ASSUMPTION; low]. DRAFT technique values are read from the earlier draft
(`proposals/2026-11-10-personal-combat-tradition-sets/kits_draft.py`, plain data), never restated.

THE ONE IN-PROCESS STEP: `load_drafts()` adds the DRAFT and NEW techniques to this process's copy of
`ability_primitives.ABILITIES` and `TRADITION_KIT`, so the engine's own `ability_factor` / `ability_bonus` and its
tradition gate compute their figures. Nothing is written to disk; a fresh process sees the live tree unchanged.
A technique whose lever has no engine site yet ("NOT BUILT") gets a factor the engine never reads, and the sheet
says so.
"""
import importlib.util
import os
import re
import sys

sys.dont_write_bytecode = True   # write nothing beside the files this script imports (no __pycache__ in other dirs)
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, REPO)   # `python -I` drops the script dir and cwd; the package is reached from the repo root

from modules.combat import ability_primitives as AP          # noqa: E402  the live atoms and the gate
from modules.combat import traditions as TR                  # noqa: E402  roster and familiarity
from modules.combat import combat_systems as S               # noqa: E402  reflex, lean, afforded heads, half-sword
from modules.combat import weapon_physics as WP              # noqa: E402  spine, edge lines, defence affinities
from modules.combat import fight as FIGHT                    # noqa: E402  the module entry
from modules.combat import contact as CT                     # noqa: E402  the grab gate
from modules.combat import attributes as SPEC                # noqa: E402  the attribute defaults
from modules.combat.combatant import Combatant, WEAPONS      # noqa: E402
from modules.combat.config import CFG                        # noqa: E402
from engine.dice_engine import draw                          # noqa: E402  the keyed draw the host passes
from engine.season.queries.inputs import PersonalCombatInput # noqa: E402  the module's typed input

_spec = importlib.util.spec_from_file_location(
    'kits_draft', os.path.join(REPO, 'proposals', '2026-11-10-personal-combat-tradition-sets', 'kits_draft.py'))
KD = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(KD)

# ── Proposal data ──────────────────────────────────────────────────────────────────────────────────────────────
LIVE_LEVERS = frozenset(KD.LEVERS_LIVE)                      # TYPED, not computed: the draft's list of the fifteen read
                                                             # sites, each checked by grep in Part 2 §2.3.1's table

COLUMN_OF_LEVER = {                                          # Part 2 §2.3.1: a technique's column follows its lever
    'measure': 'Distance', 'balance': 'Distance', 'facing_regime': 'Distance',
    'close': 'Distance', 'stophit': 'Distance', 'disengage': 'Distance', 'pursuit': 'Distance',
    'visual': 'Reading', 'precommit': 'Reading',
    'tempo': 'Attack', 'anti_overcommit': 'Attack', 'edge_read': 'Attack', 'choke_control': 'Attack', 'handling': 'Attack',
    'leverage': 'Bind and grapple', 'tactile': 'Bind and grapple', 'spine_press': 'Bind and grapple',
    'edge_grab': 'Bind and grapple', 'grapple_control': 'Bind and grapple',
    'counter_select': 'Defence and counter', 'counter_success': 'Defence and counter',
    'guard_prior_parry': 'Defence and counter', 'guard_prior_dodge': 'Defence and counter',
    'guard_prior_wind': 'Defence and counter',
}
COLUMNS = ('Distance', 'Reading', 'Attack', 'Bind and grapple', 'Defence and counter')

LEVER_SHORT = {   # the same fifteen live levers, in two or three plain words, for the one-line summary
    'measure': 'distance contest', 'leverage': 'bind odds', 'tactile': 'feel in the bind', 'spine_press': 'blade-back pressure',
    'edge_grab': 'cut taken grabbing a blade', 'visual': 'reading the body', 'precommit': 'reading early',
    'tempo': 'initiative', 'balance': 'footing', 'counter_select': 'reach for a counter',
    'counter_success': 'counter landing', 'anti_overcommit': 'over-commitment', 'edge_read': 'hidden return',
    'choke_control': 'pole telegraph', 'facing_regime': 'facing',
}
HEAD_PLAIN = {'cut_thrust': 'cut and thrust', 'cut': 'cut', 'point': 'thrust', 'blunt': 'blunt blow',
              'straight_cut': 'cut', 'curved_cut': 'curved cut'}

LEVER_PLAIN = {   # what the engine multiplies (or adds to), in plain words; NOT BUILT = no engine site reads it yet
    'measure': "his odds in the contest of distance (weaker against plate)",
    'leverage': "his odds of winning a bind",
    'tactile': "how well he feels the opponent's pressure in a bind",
    'spine_press': "the pressure of his blade's back in a bind (single-edged blades only)",
    'edge_grab': "the cut he takes seizing a live blade (below 1 = less)",
    'visual': "how well he reads the opponent's whole body",
    'precommit': "how early he reads an attack",
    'tempo': "his hold on the initiative and his reach for a counter",
    'balance': "his footing in the distance contest and in pursuit",
    'counter_select': "how readily he reaches for a counter",
    'counter_success': "the chance his counter lands (added)",
    'anti_overcommit': "how exposed a deep attack leaves him (subtracted)",
    'edge_read': "how hard his return cut is to read (double or false edge only)",
    'choke_control': "how much he telegraphs gathering a long pole (below 1 = less)",
    'facing_regime': "how far he turns to his weapon's preferred facing",
    'pursuit': "his strike on a retreating opponent -- NOT BUILT",
    'close': "how fast he closes the distance -- NOT BUILT",
    'disengage': "a clean break from a bind -- NOT BUILT",
    'stophit': "his stop-hit on an opponent closing in -- NOT BUILT",
    'guard_prior_parry': "his habitual parry when surprised -- NOT BUILT",
    'grapple_control': "how much of a grapple goes his way -- NOT BUILT",
    'handling': "how well he handles a demanding weapon -- NOT BUILT",
}

# Techniques invented in this proposal (Part 3 §3.4, code NEW / NEW·NL). Values [ASSUMPTION; low; Jordan to correct],
# placed inside the range the live and draft techniques occupy.
NEW_ABILITIES = {
    'gardant':       dict(tradition='english',  lever='guard_prior_parry', op='*', value=1.40),
    'lan_na':        dict(tradition='chinese',  lever='leverage',          op='*', value=1.15),
    'zha':           dict(tradition='chinese',  lever='counter_success',   op='+', value=0.10),
    'zhan':          dict(tradition='chinese',  lever='tactile',           op='*', value=1.15),
    'flow':          dict(tradition='filipino', lever='tempo',             op='*', value=1.10),
    'live_hand':     dict(tradition='filipino', lever='tactile',           op='*', value=1.15),
    'triangle_step': dict(tradition='filipino', lever='balance',           op='*', value=1.10),
}

PLAIN = {   # name on the sheet, and what it does in plain words
    'staerke_schwaeche': ("Strong and weak (Stärke-Schwäche)", "knows where his blade is strong and the other's weak in a bind"),
    'indes':             ("In the same instant (Indes)", "feels the bind and answers in the same moment, so his counters land more often"),
    'zwerchhau':         ("The crosswise cut (Zwerchhau)", "meets a blow from above with a cut that strikes in the same move"),
    'ringen_am_schwert': ("Wrestling at the sword (Ringen am Schwert)", "seizes the opponent's blade at the strong without cutting his hand"),
    'fuehlen':           ("Feeling (Fühlen)", "feels the opponent's pressure through the crossed blades"),
    'nachreisen':        ("Travelling after (Nachreisen)", "follows a retreating opponent and strikes into the gap"),
    'misura':            ("Measure (misura)", "holds the right distance to strike and not be struck"),
    'mezzo_tempo':       ("Half-time (mezzo tempo)", "strikes into the opponent's attack in half a beat"),
    'contratempo':       ("Counter-time (contratempo)", "strikes as the opponent arrives at close distance"),
    'volta':             ("The turn (volta)", "turns the body off the line as he closes"),
    'cavazione':         ("Slipping the blade (cavazione)", "slips round the opponent's blade to refuse the bind"),
    'abrazare':          ("Wrestling (abrazare)", "once hands are on, more of the grapple goes his way"),
    'atajo':             ("Occupying the line (atajo)", "lays his blade on the opponent's line and holds it"),
    'circulo':           ("The circle (círculo)", "holds the geometry of distance around the opponent"),
    'compas':            ("The geometric step (compás)", "steps by angles that keep him balanced at his distance"),
    'true_times':        ("True times", "commits only as far as he can recover"),
    'four_governors':    ("The four governors", "judges the incoming attacker's time and distance"),
    'gardant':           ("The guardant fight", "when surprised, falls back on a high guarded parry"),
    'shinogi':           ("The ridge (shinogi)", "presses with the ridge and back of a single-edged blade"),
    'metsuke':           ("The gaze (metsuke)", "watches the whole opponent, not the blade"),
    'sen_no_sen':        ("Seizing the intent (sen no sen)", "reads the attack as the intent forms, before the blade moves"),
    'kiriotoshi':        ("Cutting down (kiriotoshi)", "answers a cut with a cut that beats it down"),
    'zanshin':           ("Remaining mind (zanshin)", "stays alert after the cut and keeps the initiative"),
    'lan_na':            ("Block and seize (lan, na)", "circles the spear-head to deflect and control the line"),
    'zha':               ("The thrust (zha)", "thrusts straight out of the circling parry"),
    'zhan':              ("Sticking (zhan)", "sticks to the opponent's blade and feels where it goes"),
    'flow':              ("Flow", "strikes continuously without resetting"),
    'live_hand':         ("The live hand", "his second hand checks and feels the opponent's weapon arm"),
    'triangle_step':     ("The triangle step", "angled footwork that keeps a stable base"),
}

STATUS = {}   # filled by load_drafts(): LIVE / DRAFT / DRAFT-NL / NEW / NEW-NL

CURRICULUM = {   # Part 3 §3.4. 'requires': {technique: {prerequisite: level}}
    'german':   dict(fixed=['staerke_schwaeche'],
                     lines=[['fuehlen', 'staerke_schwaeche', 'indes'], ['zwerchhau', 'nachreisen'], ['ringen_am_schwert']],
                     requires={'indes': {'fuehlen': 1}}),
    'italian':  dict(fixed=['misura'],
                     lines=[['misura', 'mezzo_tempo', 'contratempo'], ['volta'], ['cavazione'], ['abrazare']],
                     requires={'mezzo_tempo': {'misura': 1}, 'contratempo': {'misura': 1}}),
    'spanish':  dict(fixed=['atajo'], lines=[['circulo', 'compas', 'atajo']], requires={}),
    'english':  dict(fixed=['true_times'], lines=[['true_times', 'four_governors'], ['gardant']], requires={}),
    'japanese': dict(fixed=['shinogi'], lines=[['metsuke', 'sen_no_sen'], ['kiriotoshi'], ['zanshin']], requires={}),
    'chinese':  dict(fixed=['lan_na'], lines=[['lan_na', 'zha'], ['zhan']], requires={'zha': {'lan_na': 1}}),
    'filipino': dict(fixed=['flow'], lines=[['flow', 'live_hand'], ['triangle_step']], requires={'live_hand': {'flow': 1}}),
}

GATES = {   # Part 3 §3.1.1: each an existing `if` in the engine; closed = today
    'counter_shallow': "after a won read, he may counter even an attack that was not deeply committed",
    'steal_shallow':   "after a won read, he may take the initiative even from a shallow attack",
    'grab_close':      "at close distance he may grab without first making an opening",
    'withdraw_band':   "he tries a fighting withdrawal from a bind he is losing a little, not only badly",
}

SETS = [   # Part 3 §3.4; effect = ('gate', name) or ('slot', column)
    dict(id='S-DE-1', name="Feel, then answer in the same instant", members=['fuehlen', 'staerke_schwaeche', 'indes'], effect=('gate', 'steal_shallow')),
    dict(id='S-DE-2', name="Wrestling at the sword", members=['ringen_am_schwert', 'fuehlen', 'staerke_schwaeche'], effect=('gate', 'grab_close')),
    dict(id='S-IT-1', name="Counter-time at narrow measure", members=['misura', 'mezzo_tempo', 'contratempo'], effect=('gate', 'counter_shallow')),
    dict(id='S-IT-2', name="Refuse the bind", members=['misura', 'cavazione', 'volta'], effect=('gate', 'withdraw_band')),
    dict(id='S-ES-1', name="Occupy the line, then take the time", members=['circulo', 'compas', 'atajo'], effect=('gate', 'steal_shallow')),
    dict(id='S-EN-1', name="True fight", members=['true_times', 'four_governors', 'gardant'], effect=('slot', 'Defence and counter')),
    dict(id='S-JP-1', name="Cut down and through", members=['shinogi', 'kiriotoshi', 'sen_no_sen'], effect=('gate', 'counter_shallow')),
    dict(id='S-JP-2', name="Remaining mind", members=['metsuke', 'sen_no_sen', 'zanshin'], effect=('slot', 'Reading')),
    dict(id='S-ZH-1', name="Block, seize, thrust", members=['lan_na', 'zha', 'zhan'], effect=('gate', 'counter_shallow')),
    dict(id='S-PH-1', name="Live hand", members=['flow', 'live_hand', 'triangle_step'], effect=('gate', 'grab_close')),
]

SET_MIN_LEVEL = 3                 # [ASSUMPTION; low] Part 4 §4.2: a set opens only with every member at 3+
SLOTS_BY_STAGE = {'novice': 1, 'practised': 2, 'veteran': 3}   # [ASSUMPTION; low] per column
ATTENTION_DIVISOR = 3             # [ASSUMPTION; low] attention = floor(Concentration / 3)
CROSS_TRAIN_THRESHOLD = (3, 3)    # [ASSUMPTION; low] three techniques at level 3+ before a second tradition


def stage_of(levels):
    """novice / practised / veteran, derived from the levels (Part 4 §4.2) [ASSUMPTION; low]."""
    if sum(1 for v in levels.values() if v >= 6) >= 3:
        return 'veteran'
    if sum(1 for v in levels.values() if v >= 3) >= 3:
        return 'practised'
    return 'novice'


def cost_of(level):
    """Attention cost of a modifier: 1, or 0 once drilled to level 6+ (Part 2 §2.3.3) [ASSUMPTION; low]."""
    return 0 if level >= 6 else 1


def load_drafts():
    """Add DRAFT (from kits_draft.py) and NEW techniques to THIS PROCESS's copy of the live tables, so the engine's own
    functions compute their figures. Writes nothing to disk. Idempotent."""
    for name in AP.ABILITIES:
        STATUS.setdefault(name, 'LIVE')
    for trad, kit in KD.KITS.items():
        for name, a in kit['abilities'].items():
            if a['existing'] or name in AP.ABILITIES:
                continue
            AP.ABILITIES[name] = dict(tradition=trad, grade='DRAFT', lever=a['lever'], op=a['op'], value=a['value'], desc='')
            AP.TRADITION_KIT[trad].append(name)
            STATUS[name] = 'DRAFT' if a['lever'] in LIVE_LEVERS else 'DRAFT-NL'
    for name, a in NEW_ABILITIES.items():
        if name in AP.ABILITIES:
            continue
        AP.ABILITIES[name] = dict(grade='NEW', desc='', **a)
        AP.TRADITION_KIT[a['tradition']].append(name)
        STATUS[name] = 'NEW' if a['lever'] in LIVE_LEVERS else 'NEW-NL'


def lever_of(name):
    return AP.ABILITIES[name]['lever']


def column_of(name):
    return COLUMN_OF_LEVER[lever_of(name)]


def build_combatant(b, techniques, known=None):
    """A Combatant from a build dict, through the constructor `fight.py` uses. `known` sets `known_traditions`
    (the cross-training input `_invested` reads; it cannot cross today's PersonalCombatInput door)."""
    c = Combatant(b['id'], weapon=b['weapon'], armor=b['armour'], tradition=b['tradition'], equipped=dict(techniques),
                  skills=dict(b.get('axes', {})), disp=b['disp'], faculty=b['faculty'], **b['attributes'])
    if known is not None:
        c.known_traditions = tuple(known)
    return c


def compose_board(b, conc_max):
    """The host-side composer of Part 2 (B-1): fixed baseline outside the columns; each column filled with the
    highest-level techniques its slots and the attention budget allow (or the build's own saved board). Returns
    (on_board names, fixed names, slots per column, attention used, attention max, complete sets). Refuses an
    over-budget saved board by name, never trims it."""
    levels = b['techniques']
    stage = stage_of(levels)
    fixed = [t for t in CURRICULUM.get(b['tradition'], {}).get('fixed', []) if levels.get(t, 0) > 0]
    attention_max = int(conc_max // ATTENTION_DIVISOR)
    slots = {col: SLOTS_BY_STAGE[stage] for col in COLUMNS}
    candidates = sorted((t for t in levels if t not in fixed and levels[t] > 0), key=lambda t: (-levels[t], t))
    chosen = b.get('board')

    def sets_complete(names):
        held = set(names) | set(fixed)
        return [s for s in SETS + b.get('personal_sets', [])
                if all(m in held and levels.get(m, 0) >= SET_MIN_LEVEL for m in s['members'])]

    for _ in range(2):   # a slot granted by a set can admit one more entry; two passes reach the fixed point here
        board, used = [], 0
        if chosen is not None:
            board = list(chosen)
            used = sum(cost_of(levels[t]) for t in board)
            levers = [lever_of(t) for t in board + fixed]
            if len(set(levers)) != len(levers):
                raise ValueError(f"{b['id']}: saved board holds two techniques on one lever ({sorted(levers)})")
            for col in COLUMNS:
                n = sum(1 for t in board if column_of(t) == col)
                if n > slots[col]:
                    raise ValueError(f"{b['id']}: saved board puts {n} techniques in {col}, which has {slots[col]} slots")
            if used > attention_max:
                raise ValueError(f"{b['id']}: saved board costs {used} attention, budget {attention_max}")
        else:
            for t in candidates:
                col = column_of(t)
                if lever_of(t) in {lever_of(x) for x in board + fixed}:
                    continue   # one technique per lever on a board (Part 2 §2.3.3): stacking compounds
                if sum(1 for x in board if column_of(x) == col) < slots[col] and used + cost_of(levels[t]) <= attention_max:
                    board.append(t)
                    used += cost_of(levels[t])
        done = sets_complete(board)
        extra = {}
        for s in done:
            if s['effect'][0] == 'slot':
                extra[s['effect'][1]] = extra.get(s['effect'][1], 0) + 1
        new_slots = {col: SLOTS_BY_STAGE[stage] + extra.get(col, 0) for col in COLUMNS}
        if new_slots == slots:
            break
        slots = new_slots
    return board, fixed, slots, used, attention_max, done


def pronoun(text, b):
    """The sheets are written with he/his/him; a build with `pro='she'` is rewritten word by word."""
    if b.get('pro') != 'she':
        return text
    for a, c in (('He', 'She'), ('he', 'she'), ('His', 'Her'), ('his', 'her'), ('himself', 'herself'), ('him', 'her')):
        text = re.sub(rf'\b{a}\b', c, text)
    return text


def fmt(x):
    return f"{x:.3g}" if isinstance(x, float) else str(x)


def measure(b, techniques, known, n):
    """Paired fights against a MIRROR: the same person (weapon, armour, attributes, skill, school) with an empty board.
    Arm 1: the build WITH this board; arm 0 (the control): the build with an EMPTY board; same keyed seeds. Returns win shares,
    the share of fights whose event sequence differs, and the share whose winner differs. Set gates are not built,
    so set effects are not in it; a second tradition's techniques cannot cross today's door, so they are not in it."""
    if n <= 0:
        return None
    attrs = {spec.registry_key: b['attributes'][spec.key] for spec in __import__('modules.combat.attributes', fromlist=['SPEC']).SPEC
             if spec.registry_key and spec.key in b['attributes'] and spec.key != 'end'}

    def one(tech, seed):
        end = b['attributes'].get('end', 4)
        inp = PersonalCombatInput(   # the partner is the same person with an empty board: a mirror, so the control is ~50%
            claimants=(b['id'], 'mirror'), ends=(end, end), wound_quantities=('felled', 'wounds'),
            kits=((b['weapon'], b['armour']),) * 2, scores=(b['faculty'],) * 2, attributes=(attrs, attrs),
            traditions=(b['tradition'],) * 2, techniques=(tech, {}), axes=(dict(b.get('axes', {})),) * 2,
            dispositions=(b['disp'],) * 2)
        out = FIGHT.fight(inp, draw.seeded(draw.H2('pc_tradition_sheets', seed)))
        res = [e for e in out.trace if e.get('kind') == 'fight_result'][-1]
        return res.get('winner'), out.trace
    win_with = win_without = differ = flip = 0
    for s in range(n):
        w1, t1 = one(dict(techniques), s)
        w0, t0 = one({}, s)
        win_with += (w1 == b['id'])
        win_without += (w0 == b['id'])
        differ += (t1 != t0)
        flip += (w1 != w0)
    return dict(n=n, win_with=win_with / n, win_without=win_without / n, differ=differ / n, flip=flip / n)


def sheet(b, n_measure):
    lines = []
    levels = b['techniques']
    probe = build_combatant(b, {})
    board, fixed, slots, used, att_max, done = compose_board(b, probe.conc_max)
    on = {t: levels[t] for t in list(fixed) + board}
    known = [b['tradition']] + ([b['second']] if b.get('second') else [])
    c = build_combatant(b, on, known=known if b.get('second') else None)
    c_door = build_combatant(b, on)                        # what today's fight.py door delivers (one tradition name)
    w = WEAPONS[b['weapon']]
    stage = stage_of(levels)
    P = lines.append

    P(f"## {b['title']}")
    P("")
    P(f"**Who.** {b['who']}")
    P("")
    trad = b['tradition'] if b['tradition'] != 'none' else 'none (no school)'
    P(f"**Tradition (the job).** {trad.capitalize() if b['tradition'] != 'none' else trad}"
      + (f"; second tradition: {b['second'].capitalize()}" if b.get('second') else "")
      + f". **Growth stage:** {stage} (computed from the levels below) [ASSUMPTION; low: the stage rule is proposal data].")
    if b.get('path_note'):
        P("")
        P(f"**Path.** {b['path_note']}")
    P("")
    P("**What he carries (loadout).**")
    P("")
    wname = {'arming': 'arming sword'}.get(b['weapon'], b['weapon'])
    aname = {'none': 'none', 'light': 'light (padded)', 'medium': 'medium (mail)', 'heavy': 'heavy (plate)'}[b['armour']]
    P(f"- In hand: {wname} (engine record `{b['weapon']}`). Armour: {aname} (engine tier `{b['armour']}`).")
    if b.get('secondary'):
        P(f"- Also carried: {b['secondary']}. *A second weapon is planned (workplan v12 B18.08) and is not an engine input today.*")
    P("")
    d = SPEC.DEFAULT
    P(f"**Attributes and fighting skill** (the engine's default fighter has Strength {d['strength']}, Agility {d['agi']}, "
      f"Endurance {d['end']}, Perception {d['att']}, Spirit {d['spirit']}, Focus {d['focus']}, skill score {d['faculty']}).")
    P("")
    a = b['attributes']
    P("| Strength | Agility | Endurance | Perception | Spirit | Focus | Fighting skill score |")
    P("|---|---|---|---|---|---|---|")
    P(f"| {a['strength']} | {a['agi']} | {a['end']} | {a['att']} | {a['spirit']} | {a['focus']} | {b['faculty']} |")
    P("")
    axes = b.get('axes', {})
    if axes:
        P("**Trained defences and contact** (added to the engine's contest for each; 0 is untrained): "
          + ", ".join(f"{k} +{v}" for k, v in axes.items()) + ".")
    else:
        P("**Trained defences and contact:** none (0 in each).")
    P("")
    P(f"**Temperament.** Disposition {b['disp']} on 1 to 7; the engine's lean is {S.disp_lean(c):+.2f} "
      f"(positive = commits deeper and reaches less for counters, negative = the reverse).")
    P("")
    P("### Techniques he knows")
    P("")
    if not levels:
        P("None.")
    else:
        P("| technique | level | what it does | column | status | engine figure at this level (this fight) |")
        P("|---|---|---|---|---|---|")
        for t in sorted(levels, key=lambda x: (-levels[x], x)):
            nm, does = PLAIN[t]
            lever = lever_of(t)
            one = build_combatant(b, {t: levels[t]}, known=known if b.get('second') else None)
            if AP.ABILITIES[t]['op'] == '*':
                val = f"×{AP.ability_factor(one, lever):.3f} on {LEVER_PLAIN[lever]}"
            else:
                val = f"+{AP.ability_bonus(one, lever):.3f} to {LEVER_PLAIN[lever]}"
            where = "fixed (always on)" if t in fixed else ("on today's board" if t in board else "known, not brought")
            if lever not in LIVE_LEVERS:
                val += " (no engine site yet)"
            P(f"| {nm} | {levels[t]} | {does} | {column_of(t)} | {STATUS[t]}; {where} | {val} |")
    P("")
    P("### Today's board (proposal; not an engine figure)")
    P("")
    P(f"Attention: {used} of {att_max} [ASSUMPTION; low: attention = ⌊Concentration {fmt(probe.conc_max)} ÷ "
      f"{ATTENTION_DIVISOR}⌋; a technique costs 1, or 0 once drilled to level 6].")
    P("")
    P("| column | slots | brought |")
    P("|---|---|---|")
    for col in COLUMNS:
        here = [PLAIN[t][0] for t in board if column_of(t) == col]
        P(f"| {col} | {len(here)} of {slots[col]} | {', '.join(here) if here else '—'} |")
    P("")
    if fixed:
        P(f"Fixed foundation, outside the columns: {', '.join(PLAIN[t][0] for t in fixed)}.")
        P("")
    sets_here = [s for s in SETS + b.get('personal_sets', []) if any(m in levels for m in s['members'])]
    if sets_here:
        P("**Sets.**")
        P("")
        for s in sets_here:
            eff = (f"opens: {GATES[s['effect'][1]]}" if s['effect'][0] == 'gate'
                   else f"+1 slot in {s['effect'][1]}")
            if s in done:
                state = "COMPLETE"
            else:
                miss = [f"{PLAIN[m][0]} {levels.get(m, 0)}→{SET_MIN_LEVEL}" if levels.get(m, 0) < SET_MIN_LEVEL
                        else f"{PLAIN[m][0]} brought to the board" for m in s['members']
                        if levels.get(m, 0) < SET_MIN_LEVEL or (m not in board and m not in fixed)]
                state = "incomplete; needs " + "; ".join(miss)
            tag = " (personal set)" if s in b.get('personal_sets', []) else ""
            P(f"- *{s['name']}*{tag}: {' + '.join(PLAIN[m][0] for m in s['members'])} — {eff}. **{state}.** "
              f"*(Gates are proposed; none is built, so no set acts in today's engine.)*")
        P("")
    P("### Growth path")
    P("")
    for step in b['next']:
        P(f"- {step}")
    P("")
    P("### What the engine derives for him (computed by `modules.combat`, not typed)")
    P("")
    P("| figure | value | what it means |")
    P("|---|---|---|")
    P(f"| Health | {c.wt.health_full} | damage he can take before he falls |")
    P(f"| Wound interval | {c.wt.wi} | damage that makes one wound |")
    P(f"| Wounds before the last | {c.wt.max_wounds} | wounds he can carry before the next one fells him |")
    P(f"| Stamina | {fmt(c.stamina_max)} | his reserve for effort in a bout |")
    P(f"| Concentration | {fmt(c.conc_max)} | his reserve of focus in a bout ({fmt(CFG['CONC_FOCUS'])} × Focus + "
      f"{fmt(CFG['CONC_SPIRIT'])} × Spirit) |")
    P(f"| Reflex | {fmt(S.reflex(c, CFG))} | speed of his defensive response (Agility and Perception) |")
    P(f"| Reading | {fmt(S.reading(c, CFG))} | how well he reads an attack (Perception) |")
    heads = sorted({HEAD_PLAIN.get(h, h) for h in S.afforded_heads(w, CFG)})
    aff = WP.defense_affinities(w)
    P(f"| Weapon strikes with | {', '.join(heads)} | the striking modes his weapon allows |")
    P(f"| Can half-sword | {'yes' if S.affords_halfsword(w) else 'no'} | grip the blade to thrust into armour gaps |")
    P(f"| Can grab without an opening | {'yes' if CT.grab_available(c, c, False, CFG) else 'no'} | the engine's grab gate with no opening made |")
    P(f"| Blade back (single edge) | {fmt(WP.spine(w))} | 0 means the ridge technique (shinogi) does nothing |")
    P(f"| Edge lines (double or false edge) | {fmt(WP.edge_lines(w))} | 0 means hidden-return techniques do nothing |")
    P(f"| Defence suits the weapon | parry {fmt(aff['parry'])}, dodge {fmt(aff['dodge'])}, wind {fmt(aff['wind'])} | ceiling the weapon puts on each defence (higher is better) |")
    if b['tradition'] != 'none':
        fam = ", ".join(f"{t} {TR.familiarity(b['tradition'], t):.2f}" for t in TR.TRADITIONS if t != b['tradition'])
        P(f"| How well he reads other schools | {fam} | 1.00 = as well as his own |")
    else:
        vals = sorted({TR.familiarity('none', t) for t in TR.TRADITIONS} | {TR.familiarity(t, 'none') for t in TR.TRADITIONS})
        P(f"| How well he reads other schools | {', '.join(f'{v:.2f}' for v in vals)} against every school, both ways | "
          f"a fighter with no school has none to misread, and none to be misread by (`traditions.py:44-45`) |")
    P("")
    non_neutral = []
    for lever in sorted(LIVE_LEVERS):
        f, bon = AP.ability_factor(c, lever), AP.ability_bonus(c, lever)
        if f != 1.0:
            non_neutral.append(f"{LEVER_SHORT[lever]} ×{f:.3f}")
        if bon != 0.0:
            non_neutral.append(f"{LEVER_SHORT[lever]} +{bon:.3f}")
    P("**Everything his board changes in the engine, all at once:** "
      + ("; ".join(non_neutral) if non_neutral else "nothing (every lever at its neutral value)") + ".")
    if b.get('second'):
        door = [lv for lv in sorted(LIVE_LEVERS)
                if (AP.ability_factor(c, lv), AP.ability_bonus(c, lv)) != (AP.ability_factor(c_door, lv), AP.ability_bonus(c_door, lv))]
        P("")
        P(f"**Cross-training through today's door.** The fight's input carries one tradition name per fighter "
          f"(`fight.py:58-63`), so his {b['second'].capitalize()} techniques are refused by the engine's tradition gate and "
          f"act on nothing today. What differs between the two cases: {', '.join(LEVER_SHORT[x] for x in door) if door else 'nothing'}. "
          f"After B18.02 the host composes the numbers and the difference disappears.")
    P("")
    m = measure(b, on, known, n_measure)
    if m:
        P(f"**Measured** ({m['n']} seeds; his opponent is himself with an empty board, same weapon, armour, attributes and "
          f"school): he wins {m['win_with']:.1%} with this board and {m['win_without']:.1%} without it (the control, a pure "
          f"mirror); with the board the fight goes differently in {m['differ']:.1%} of seeds and the winner changes in "
          f"{m['flip']:.1%}. *A run, not a balance claim: one matchup, draft values [SIM-CALIBRATE]; set gates and a "
          f"second school's techniques are not in it (neither can reach today's engine).*")
        P("")
    if b.get('note'):
        P(f"*Note.* {b['note']}")
        P("")
    return pronoun("\n".join(lines), b)


# ── The builds (named persons, invented for illustration; every level and attribute is [ASSUMPTION; low]) ─────
BUILDS = [
    dict(id='konrad', pro='he', title="Sheet 1 — Konrad Rauch: German school, practised",
         who="A master-at-arms in a town garrison, forty, taught in the Liechtenauer line as a boy.",
         tradition='german', weapon='longsword', armour='medium', secondary="a dagger",
         attributes=dict(strength=5, agi=4, end=5, att=4, spirit=4, focus=4), faculty=4,
         axes={'bind': 0.5, 'parry': 0.3}, disp=5,
         techniques={'staerke_schwaeche': 4, 'fuehlen': 3, 'indes': 3, 'zwerchhau': 3, 'ringen_am_schwert': 1, 'nachreisen': 1},
         next=["Wrestling at the sword 1 → 3: two lessons from a teacher who holds it at 3 or more (1 `train` each at "
               "these levels). That completes *Wrestling at the sword*.",
               "Travelling after has no engine site yet (its lever, `pursuit`, is not built): training it changes nothing in a fight until it is.",
               "Ready to take a second school: he has three techniques at level 3 or more."]),
    dict(id='lucia', pro='she', title="Sheet 2 — Lucia Ferro: Italian school, novice",
         who="A merchant's daughter in her second year at a fencing hall.",
         tradition='italian', weapon='rapier', armour='none',
         attributes=dict(strength=3, agi=5, end=4, att=4, spirit=3, focus=3), faculty=3,
         axes={'dodge': 0.3}, disp=3,
         techniques={'misura': 1, 'mezzo_tempo': 1},
         next=["Measure 1 → 2 and Half-time 1 → 2: one lesson each at the hall.",
               "Counter-time (needs Measure at 1, which she has): taught at the hall when the master judges her ready.",
               "*Counter-time at narrow measure* needs all three at level 3: seven lessons away (2 + 2 + 3)."]),
    dict(id='hayato', pro='he', title="Sheet 3 — Mori Hayato: Japanese school, veteran",
         who="A retainer's sword instructor, fifty, who has taught for twenty years.",
         tradition='japanese', weapon='katana', armour='light',
         attributes=dict(strength=4, agi=5, end=4, att=5, spirit=5, focus=5), faculty=5,
         axes={'parry': 0.6, 'balance': 0.3}, disp=4,
         techniques={'shinogi': 7, 'metsuke': 6, 'sen_no_sen': 6, 'kiriotoshi': 6, 'zanshin': 4},
         next=["Remaining mind 4 → 6: four lessons, and there are few teachers left who hold it at 6.",
               "The ridge 7 → 8: three lessons from a teacher at 8, or none at all if no such teacher lives.",
               "Drilled techniques (level 6 and up) cost him no attention, so his board is limited by slots, not by attention."],
         note=f"With a double-edged tsurugi in hand his ridge technique would do nothing: the engine's blade-back figure "
              f"for a tsurugi is {fmt(WP.spine(WEAPONS['tsurugi']))}."),
    dict(id='margarethe', pro='she', title="Sheet 4 — Margarethe Vos: Spanish school, cross-trained in the Italian",
         who="A court fencer who learned the Spanish geometry at home and the Italian measure abroad.",
         tradition='spanish', second='italian', weapon='rapier', armour='light',
         attributes=dict(strength=3, agi=5, end=4, att=5, spirit=4, focus=4), faculty=4,
         axes={'parry': 0.4}, disp=4,
         techniques={'atajo': 4, 'circulo': 3, 'compas': 3, 'misura': 3, 'mezzo_tempo': 2},
         next=["Half-time 2 → 3: one lesson from an Italian teacher.",
               "Counter-time (Italian; needs Measure 1): with it at 3 she would complete *Counter-time at narrow measure* as well.",
               "A third school needs three Italian techniques at level 3 first [ASSUMPTION; low]."]),
    dict(id='ysolde', pro='she', title="Sheet 5 — Ysolde Marr: a bespoke path (Italian, with a German master's lessons)",
         who="The duke's fencing master, a named character. Her father taught her the Italian measure; an exiled "
             "German master taught her the crosswise cut and the bind.",
         path_note="Authored, in this order: Measure (her father) → Half-time → Counter-time → the crosswise cut and "
                   "Strong and weak (Ulrich, the exile). Every step is on the shared curricula, so anyone can walk the "
                   "same techniques; the order, the teachers and the personal set are hers.",
         tradition='italian', second='german', weapon='arming', armour='light', secondary="a dagger",
         attributes=dict(strength=4, agi=5, end=4, att=5, spirit=5, focus=5), faculty=5,
         axes={'parry': 0.5, 'bind': 0.3}, disp=4,
         techniques={'misura': 5, 'mezzo_tempo': 4, 'contratempo': 3, 'zwerchhau': 4, 'staerke_schwaeche': 3},
         personal_sets=[dict(id='P-YM', name="The exile's lesson", members=['misura', 'zwerchhau', 'staerke_schwaeche'],
                             effect=('gate', 'steal_shallow'))],
         board=['zwerchhau', 'contratempo', 'staerke_schwaeche'],
         note="Her saved board brings the crosswise cut rather than Half-time: both act on her reach for a counter, and a "
              "board holds one technique per lever, so she chooses which door to open today (her own set, not the "
              "Italian one).",
         next=["Strong and weak 3 → 4: one more lesson, but Ulrich is dead; the next German teacher is two weeks' travel away.",
               "Her personal set is filed under her name; any fighter who holds the same three techniques at 3 opens the same door."]),
    dict(id='odo', pro='he', title="Sheet 6 — Odo: no school",
         who="A carter who keeps an old arming sword under the seat.",
         tradition='none', weapon='arming', armour='none',
         attributes=dict(strength=5, agi=3, end=5, att=3, spirit=3, focus=3), faculty=2,
         axes={}, disp=5,
         techniques={},
         next=["Today: nothing to learn. A fighter with no school can be taught no technique (the engine's tradition gate "
               "admits none).",
               "Proposed (Part 3 §3.5, decision D-8): the plain drill techniques (the 21 generics) become open to anyone, "
               "so Odo could learn *keen eye* or *footing* from any teacher who has them."],
         note=None),
]


def curriculum_report():
    out = ["# Curricula, as data (proposal; values of DRAFT techniques from kits_draft.py, NEW ones [ASSUMPTION; low])", ""]
    for trad, cur in CURRICULUM.items():
        names = sorted({t for line in cur['lines'] for t in line} | set(cur['fixed']))
        sets = [s for s in SETS if any(m in names for m in s['members'])]
        out.append(f"## {trad} — {len(names)} techniques, {len(sets)} sets; fixed: {', '.join(cur['fixed'])}")
        out.append("")
        out.append("| technique | status | lever | column | op | value | requires |")
        out.append("|---|---|---|---|---|---|---|")
        for t in names:
            a = AP.ABILITIES[t]
            out.append(f"| {t} | {STATUS[t]} | {a['lever']} | {column_of(t)} | {a['op']} | {a['value']} | "
                       f"{cur['requires'].get(t, '')} |")
        for s in sets:
            out.append(f"\n- set {s['id']} *{s['name']}*: {' + '.join(s['members'])} → {s['effect'][0]} {s['effect'][1]}")
        out.append("")
    return "\n".join(out)


def check():
    """This script's falsifiers. Each must be able to fail."""
    checked = 0
    # 1. Every live technique named in the curricula matches the live registry's tradition (no drifted copy).
    for trad, cur in CURRICULUM.items():
        for t in {x for line in cur['lines'] for x in line} | set(cur['fixed']):
            assert t in AP.ABILITIES, f"{t} is in no table"
            assert AP.ABILITIES[t]['tradition'] == trad, f"{t}: filed under {trad}, registry says {AP.ABILITIES[t]['tradition']}"
            assert t in PLAIN, f"{t} has no plain description"
            checked += 1
    # 2. Every set member exists and every column is derivable.
    for s in SETS:
        for m in s['members']:
            assert column_of(m) in COLUMNS
            checked += 1
    # 3. An untaught technique is exactly inert (Odo equipping a generic): the engine's gate, not this script.
    odo = build_combatant(BUILDS[-1], {'keen_eye_basic': 3})
    assert AP.ability_factor(odo, 'visual') == 1.0
    checked += 1
    # 4. A German fighter with an empty board fights byte-identically to the same German fighter given no technique
    #    argument at all; and (the positive control, so the instrument can see a difference) the same fighter with
    #    one taught technique at level 4 changes at least one of the same 20 seeds.
    b = BUILDS[0]

    def run(tech, seed):
        kw = {} if tech is None else dict(techniques=(tech, None))
        inp = PersonalCombatInput(claimants=('x', 'y'), ends=(4, 4), wound_quantities=('felled',),
                                  kits=((b['weapon'], b['armour']), ('arming', 'light')), traditions=('german', None), **kw)
        return FIGHT.fight(inp, draw.seeded(draw.H2('pc_tradition_check', seed))).trace
    moved = 0
    for seed in range(20):
        t_none = run(None, seed)
        assert run({}, seed) == t_none, f"seed {seed}: an empty board changed the fight"
        moved += run({'staerke_schwaeche': 4}, seed) != t_none
        checked += 1
    assert moved >= 1, "positive control: a taught technique changed no fight, so check 4 could not fail"
    # 5. Every build composes within its own budget (the composer refuses, by name, otherwise).
    for bb in BUILDS:
        compose_board(bb, build_combatant(bb, {}).conc_max)
        checked += 1
    assert checked >= 40, checked
    return checked


def main(argv):
    load_drafts()
    if '--check' in argv:
        print(f"check: {check()} assertions held")
        return
    if '--curriculum' in argv:
        print(curriculum_report())
        return
    n = 400
    if '--measure' in argv:
        n = int(argv[argv.index('--measure') + 1])
    print("# Part 8 — Character sheets (GENERATED by `sheets.py`; do not edit by hand)")
    print("")
    print("## Status: PROPOSED. Generated by `python -I proposals/2026-11-20-pc-tradition-jobs-growth/sheets.py`. Every "
          "figure under *What the engine derives*, every technique's engine figure, and every *Measured* line is computed "
          "by the live `modules.combat` package in this run. Board, attention, stage, sets and growth path are proposal "
          "data, marked as such. The persons, their levels and attributes are invented for illustration "
          "[ASSUMPTION; low].")
    print("")
    print("**How to read a sheet.** A *tradition* is the fighter's school. A *technique* is something the school teaches, "
          "with a level from 1 (just learned) to 8 (mastered). The *board* is what the fighter brings to this fight. "
          "*Status* says whether the technique exists in the engine today (LIVE), comes from an earlier draft (DRAFT), or "
          "is invented in this proposal (NEW); *-NL* means the thing it acts on is not built yet, so it does nothing in a "
          "fight today. *Engine figure* is the multiplier (×) or addition (+) the engine applies at that level.")
    print("")
    for b in BUILDS:
        print(sheet(b, n))


if __name__ == '__main__':
    main(sys.argv[1:])
