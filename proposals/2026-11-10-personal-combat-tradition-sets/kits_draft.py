"""kits_draft.py — DRAFT tradition kits for the personal-combat module. PROPOSED, NOT WIRED, Jordan-vetoable.

This file is the single authored head of the ability entries in 00_tradition_sets.md (the .md carries the
reasoning and the tables; every number lives only here). Nothing imports it except check_kits.py. Entries use
the live `ability_primitives.ABILITIES` schema (tradition, grade, lever, op, value, desc) so a kit can be merged
with `ABILITIES.update(...)`; the extra keys (`point`, `lever_status`, `term`, `mech`, `src`) are ignored by
`ability_factor` / `ability_bonus`, which read only tradition / lever / op / value.

GRADES (ability_armature §1.5 source tiers, unchanged): S1 primary / critically edited, S2 peer-reviewed or
well-attested secondary, S2/S3 partly reliable. A claim's grade is no better than its best source.

VERIFICATION CODES, per ability, for the TERM (is the technique named in a source?) and the MECHANISM (does the
source say what the ability does?):
  V = read this session (2026-11-10) in the page or search result named in SOURCES (modern translation or secondary
      where SOURCES says so; none is a facsimile read).
  C = carried: graded by the repo's ability_armature / tradition_decomposition, NOT re-read this session.
  U = unverified recollection. An ability with mech == 'U' is a candidate: it must clear an S1/S2 read before it
      is merged (ability_armature §1.4: no technique, no ability).

VALUES are all [SIM-CALIBRATE]. Placement rule: multiplicative amplifiers at level 1 sit in 1.15-1.60, the range
the authored abilities already occupy (atajo 1.18, staerke_schwaeche 1.20, mezzo_tempo 1.40, zwerchhau 1.40,
shinogi 1.60); additive at 0.10-0.25 (true_times 0.25, indes 0.15). The numbers are starting points for the
PCA §6.2 texture band (|win-rate shift| <= 2pp, >= 15% of fights differ, 3-10% flip), not claims.
"""

# ── Levers ────────────────────────────────────────────────────────────────────────────────────────────
# LIVE: consumed today (tests/valoria/test_combat_tradition_levers.py `live` set).
LEVERS_LIVE = frozenset({
    'measure', 'tempo', 'visual', 'tactile', 'precommit', 'leverage', 'balance',
    'counter_success', 'counter_select', 'anti_overcommit',
    'spine_press', 'edge_grab', 'edge_read', 'choke_control', 'facing_regime',
})

# NEW: no consumer yet. Each is ONE `ability_factor(c, <lever>)` call at a function that already computes the
# right quantity. `form` is the sign-safe composition (PCA §5.1 rule 5; combat_systems.lever_log_edge): a
# multiplicative lever may scale its owner's own non-negative quantity, or enter a signed sigma as K*log(factor);
# it may never ratio-multiply a signed difference. `K` names the config.py constant the build must add
# (Class-C, [SIM-CALIBRATE]). At factor 1.0 every form is exactly neutral (log 1 == 0.0; *1.0; weights all 1.0).
LEVERS_NEW = {
    'close': dict(
        site='combat_systems.close_rate', point='approach.close',
        form='own-side product: cr *= ability_factor(shorter, "close") (cr is a non-negative rate)', K=None),
    'stophit': dict(
        site='combat_systems.stophit_sigma', point='approach.close',
        form='signed sigma: + STOPHIT_LEVER_K * log(ability_factor(longer, "stophit"))', K='STOPHIT_LEVER_K'),
    'disengage': dict(
        site='combat_systems.disengage_clean_p', point='disengage.withdraw',
        form='logistic argument is a signed difference: logistic(diff/2 + DISENGAGE_LEVER_K * log(f_withdrawer))',
        K='DISENGAGE_LEVER_K'),
    'pursuit': dict(
        site='combat_systems.pursuit_sigma', point='disengage.withdraw',
        form='signed sigma: + PURSUIT_LEVER_K * log(ability_factor(pursuer, "pursuit"))', K='PURSUIT_LEVER_K'),
    'guard_prior_parry': dict(
        site='combat_systems.read_contest (lost-read branch)', point='exchange.mode',
        form='weights w_m = ability_factor(defender, "guard_prior_<m>"); all 1.0 -> keep modes[rng.randrange(3)] '
             '(RNG-neutral); else one rng.random() weighted draw. mode_sigma still resolves with the weapon cap.',
        K=None),
    'guard_prior_dodge': dict(
        site='combat_systems.read_contest (lost-read branch)', point='exchange.mode', form='as guard_prior_parry', K=None),
    'guard_prior_wind': dict(
        site='combat_systems.read_contest (lost-read branch)', point='exchange.mode', form='as guard_prior_parry', K=None),
    'grapple_control': dict(
        site='contact.grab_sigma', point='contact.axis',
        form='signed sigma: + GRAB_CONTROL_K * log(ability_factor(actor, "grapple_control"))', K='GRAB_CONTROL_K'),
}

# ── Sources ───────────────────────────────────────────────────────────────────────────────────────────
# `read` says what was actually read. None of these is a facsimile; every V is a modern translation, a wiki
# page or a search result, and is as weak as that.
SOURCES = {
    'LIECH': dict(ref="Liechtenauer, Zettel (long sword verses 17-48), Wiktenauer (Chidester / Tobler translations)",
                  url='https://wiktenauer.com/wiki/Johannes_Liechtenauer',
                  read="page text to ~char 100000: Vor/Nach v.17, Indes v.18, Schwach/Stark v.18, five strikes v.21-23, "
                       "Nachreisen v.24 ('pursue, run down, and set the blow'), Durchwechseln v.25, Winden v.26, "
                       "Zornhau v.27-31. NOT seen: Fuhlen as a term; Absetzen as a term (the idea at v.28)."),
    'RINGECK': dict(ref="Dresden C 487 gloss, Rawlings 2003 translation, via a search result (excerpt only)",
                    url='https://www.wiktenauer.com/wiki/Sigmund_ain_Ringeck/David_Rawlings_LS_2003',
                    read="snippet only: displacement 'simultaneously' (Indes) then strike the nearest opening from "
                         "the bind. Not read: Fuhlen / weich-hart, Zwerchhau as counter to Oberhau."),
    'LECK': dict(ref="Lecckuchner, Kunst des Messerfechtens, Cod.Pal.germ. 430 (1478) and Cgm 582 (1482)",
                 url='https://wiktenauer.com/wiki/Kunst_des_Messerfechtens_(CGM_582)',
                 read="search result: two manuscripts, 1478 draft and 1482 illustrated; system rests on Liechtenauer. "
                      "Techniques not read."),
    'FIORE': dict(ref="Fiore dei Liberi, Fior di Battaglia / Flos Duellatorum (c.1409), Wiktenauer",
                  url='https://wiktenauer.com/wiki/Fiore_dei_Liberi',
                  read="page text to ~char 100000: Abrazare (8 attributes), Daga, one-hand sword, two-hand sword in "
                       "zogho largo / stretto, spada en arme (half-sword), azza, lancia, mounted. Not read: the "
                       "animals, contrario sequences."),
    'FIORE_VOLTE': dict(ref="Fiore, Getty f.22r: volta stabile / meza volta / tutta volta; Windsor 2024 (secondary)",
                        url='https://guywindsor.net/2024/03/fiore-dei-liberi-footwork-revisited/',
                        read="search result: the three turns are named; Windsor says Fiore gives no precise "
                             "definitions and readings vary. Footwork meaning is an interpretation, not a fact."),
    'FIORE39R': dict(ref="Fiore, Getty f.39r (Posta Mezza Porta di Ferro): step off line and beat the point",
                     url='research/by_lane/PC_personal_combat.md section 1.2',
                     read="CARRIED: the repo's R9 fact file quotes it and grades it 'Fiore's own claim, not "
                          "independently verified'; the engine already implements the step and beat "
                          "(FACING_VOID_K, approach_displace)."),
    'CAPO': dict(ref="Capoferro, Gran Simulacro (1610), Wiktenauer",
                 url='https://wiktenauer.com/wiki/Ridolfo_Capoferro',
                 read="page text to ~char 100000, chapters 1-9: misura, larga / stretta, tempo defined; "
                      "'cavationi and contracavationi' named (criticised as vanities); 'many strike each other in "
                      "contra tempo'. NOT read: cavazione defined, chapter 10 on guards."),
    'SILVER': dict(ref="Silver, Paradoxes of Defence (1599), Wiktenauer",
                   url='https://wiktenauer.com/wiki/George_Silver',
                   read="page text to ~char 100000: four governors named but not defined; true fight = hand before "
                        "foot; 'whosoever wins or gains the place in true pace, space and time has the advantage'; "
                        "guardant fight named; short staff over long staves. NOT read: the governors' list, grounds."),
    'DESTREZA': dict(ref="Carranza (1582) / Pacheco de Narvaez (1600); repo ability_armature section 5 (S2/S3)",
                     url='https://wiktenauer.com/wiki/Jeronimo_Sanchez_de_Carranza',
                     read="CARRIED. The Wiktenauer Carranza page (partial, garbled translation) does NOT define "
                          "circulo, compas, atajo, angulos or perfil; it names cut / reverse / thrust only."),
    'KORYU': dict(ref="koryu sen / maai / zanshin / kiriotoshi; repo ability_armature section 5 (S2, budo-gaku / J-STAGE)",
                  url='https://koryu.com/books/lifegivingsword/',
                  read="CARRIED. A search for the three sen terms in Yagyu Munenori's Heiho Kadensho and Musashi's "
                       "Gorin no Sho found NO passage. Check Wilson (2003) or Guo (2022) before merging."),
}

# ── Phase slots (phase4_5_plan_v1 section 4b: Approach, Reading, Commit, Defence, Bind, Counter; Feint is dissolved into
# Commit). An injection point belongs to one slot, so `slot` is derived from `point`, never authored twice. 'Contact' and
# 'Separation' are NOT among the seven (Phase 5, the contact pole); they are named here so no ability is slotless.
SLOT_OF_POINT = {
    'beat.head': 'Approach', 'approach.close': 'Approach', 'reopen.measure': 'Separation',
    'disengage.withdraw': 'Separation', 'exchange.commit': 'Commit', 'exchange.read': 'Reading',
    'exchange.mode': 'Defence', 'exchange.roll': 'Commit', 'exchange.counter': 'Counter',
    'riposte.counter': 'Counter', 'exchange.bind_entry': 'Bind', 'burst.continuation': 'Commit',
    'contact.axis': 'Contact',
}


# ── The kits ──────────────────────────────────────────────────────────────────────────────────────────
# `lever_status`: 'live' merges today; 'new' needs LEVERS_NEW[lever] built first. `existing=True` marks the eight
# abilities already in ability_primitives.ABILITIES (restated so one file shows the whole kit; the checker asserts
# they match the live entry, so a drifted copy fails).
def _a(tradition, grade, lever, op, value, point, term, mech, src, desc, existing=False, also=()):
    return dict(tradition=tradition, grade=grade, lever=lever, op=op, value=value, desc=desc, point=point,
                also=tuple(also), term=term, mech=mech, src=src, existing=existing,
                lever_status='live' if lever in LEVERS_LIVE else 'new')


KITS = {
    # ── German: Liechtenauer lineage, Lecckuchner Messer, armoured and unarmoured wrestling-at-the-sword ──
    'german': dict(
        teaches=['longsword', 'falchion', 'dagger', 'poleaxe'],
        candidates=['greatsword', 'flamberge'],   # Zweihander: recollection only, no source read
        skills=['bind', 'technique', 'grab'],
        abilities={
            'indes': _a('german', 'S1/S2', 'counter_success', '+', 0.15, 'riposte.counter', 'V', 'V', 'RINGECK',
                        "Indes — the displacement made in the same tempo, then the strike at the nearest opening "
                        "(existing).", existing=True),
            'staerke_schwaeche': _a('german', 'S1/S2', 'leverage', '*', 1.20, 'exchange.bind_entry', 'V', 'C', 'LIECH',
                        "Staerke-Schwaeche — seek the opponent's weak and strong (v.18) (existing).", existing=True),
            'zwerchhau': _a('german', 'S1/S2', 'counter_select', '*', 1.4, 'exchange.counter', 'V', 'C', 'LIECH',
                        "Zwerchhau — the crosswise cut that intercepts an Oberhau in one tempo (existing; its "
                        "interception function is carried from the repo, not read here).", existing=True),
            'ringen_am_schwert': _a('german', 'S1/S2', 'edge_grab', '*', 0.4, 'contact.axis', 'C', 'C', 'LIECH',
                        "Ringen am Schwert — seizing a live blade at the strong with less self-injury (existing).",
                        existing=True),
            'fuehlen': _a('german', 'S1/S2', 'tactile', '*', 1.20, 'exchange.bind_entry', 'C', 'C', 'RINGECK',
                        "Fuehlen — feeling the opponent's pressure through the crossed blades, soft or hard, to "
                        "choose wind or thrust. The term did not appear on the Wiktenauer verse page and the gloss "
                        "was not read; the repo grades it S1/S2. Reads the same bind_sigma tactile term and the "
                        "bind steal (tactile+leverage)/2 that Indes' steal already uses."),
            'nachreisen': _a('german', 'S1/S2', 'pursuit', '*', 1.25, 'disengage.withdraw', 'V', 'V', 'LIECH',
                        "Nachreisen — travelling after: 'pursue, run down, and set the blow' (v.24). Raises the "
                        "owner's chance that the strike on a withdrawing opponent lands in the gap."),
            'absetzen': _a('german', 'S1/S2', 'guard_prior_parry', '*', 1.5, 'exchange.mode', 'U', 'V', 'LIECH',
                        "Absetzen — setting off: taking the blow away while striking. The IDEA is in the Zornhau "
                        "verses (v.28 'take it away above'); the term itself did not appear on the page read, so "
                        "term=U. On a lost read the fighter falls back on the displacing parry, not a uniform guess."),
        }),
    # ── Italian: Fiore -> Bolognese -> rapier (Capoferro, Fabris) ──
    'italian': dict(
        teaches=['rapier', 'longsword', 'arming', 'dagger', 'main_gauche', 'cinquedea', 'poleaxe', 'spear'],
        candidates=['estoc'],
        skills=['dodge', 'technique', 'grab'],
        abilities={
            'mezzo_tempo': _a('italian', 'S2', 'counter_select', '*', 1.40, 'exchange.counter', 'C', 'C', 'CAPO',
                        "Mezzo tempo — the half-time counter (existing). Capoferro's tempo is 'the measure of the "
                        "stillness and of the motion' (V).", existing=True),
            'misura': _a('italian', 'S2', 'measure', '*', 1.15, 'exchange.roll', 'V', 'V', 'CAPO',
                        "Misura — 'a just distance from the point of my sword to the body of my adversary in which I "
                        "can strike him'; larga by lengthening the foot, stretta by advancing the body (existing).",
                        existing=True),
            'contratempo': _a('italian', 'S2', 'counter_success', '+', 0.12, 'riposte.counter', 'V', 'V', 'CAPO',
                        "Contratempo — the blow delivered as the opponent arrives at narrow measure: 'many strike "
                        "each other in contra tempo, having come at the same time to narrow measure'. Makes the "
                        "selected counter (mezzo_tempo) land more often; without it the selection is the high-variance "
                        "desperate move the engine already punishes."),
            'volta': _a('italian', 'S2', 'close', '*', 1.20, 'approach.close', 'V', 'C', 'FIORE_VOLTE',
                        "Volta — Fiore's three turns of the body (volta stabile, meza volta, tutta volta) and the "
                        "step off line that beats the point (f.39r). The engine models the step as FACING_VOID_K, "
                        "which moves close_rate by ~0.14%; this lever lets a trained fighter close faster by it. "
                        "Footwork meaning is an interpretation (Windsor 2024)."),
            'cavazione': _a('italian', 'S2', 'disengage', '*', 1.30, 'disengage.withdraw', 'V', 'C', 'CAPO',
                        "Cavazione — slipping the blade round the opponent's to refuse the contact. Named in "
                        "Capoferro (cavationi, contracavationi), definition not read. WEAKEST MAPPING IN THE SUITE: "
                        "cavazione changes the blade's line, the engine's `disengage` is a body withdrawal from a "
                        "lost bind. The repo's decomposition made this mapping (S2); it is the same kind of "
                        "category stretch ED-PC-0026 removed for winden and guardia. Hold it unless the effect "
                        "matches (leaves contact, re-presents the point at the owner's measure)."),
            'abrazare': _a('italian', 'S2', 'grapple_control', '*', 1.30, 'contact.axis', 'V', 'V', 'FIORE',
                        "Abrazare — Fiore's wrestling, the foundation of his art: strength, speed, knowledge of "
                        "superior holds, locks, throws, dislocations; 'taking of the sword' and the dagger "
                        "remedies follow from it. Biases the grab toward the trained fighter's control."),
        }),
    # ── Spanish: La Verdadera Destreza ──
    'spanish': dict(
        teaches=['rapier', 'main_gauche', 'dagger'],
        candidates=[],
        skills=['technique', 'balance'],
        abilities={
            'atajo': _a('spanish', 'S2/S3', 'leverage', '*', 1.18, 'exchange.bind_entry', 'C', 'C', 'DESTREZA',
                        "Atajo — occupying and interrupting the opponent's line by angulation (existing; "
                        "re-homed from measure to leverage at ED-PC-0026).", existing=True),
            'compas': _a('spanish', 'S2/S3', 'balance', '*', 1.08, 'exchange.roll', 'C', 'C', 'DESTREZA',
                        "Compas — the geometric steps that hold the fighter's measure. The balance lever feeds "
                        "reach_sigma's footwork term and pursuit_sigma."),
            'circulo': _a('spanish', 'S2/S3', 'measure', '*', 1.04, 'beat.head', 'C', 'C', 'DESTREZA',
                        "Circulo / angulos — the geometry of distance; holding it slows the decay of the held "
                        "initiative (init_hold_decay reads the measure lever)."),
        }),
    # ── English: Silver ──
    'english': dict(
        teaches=['arming', 'staff', 'dagger'],
        candidates=[],
        skills=['parry', 'technique'],
        abilities={
            'true_times': _a('english', 'S2', 'anti_overcommit', '+', 0.25, 'exchange.roll', 'V', 'V', 'SILVER',
                        "True times — a true fight is 'whatsoever is done with the hand before the foot' (existing).",
                        existing=True),
            'four_governors': _a('english', 'S2', 'stophit', '*', 1.20, 'approach.close', 'V', 'U', 'SILVER',
                        "The four governors — Silver says that without them 'it is impossible to fight safe' and that "
                        "'whosoever wins or gains the place in true pace, space and time has the advantage'. The "
                        "governors are named but were not listed in the text read, so the mechanism (judgement of the "
                        "incomer, mapped to the stop-hit) is U; the repo's own decomposition makes the same mapping."),
        }),
    # ── Japanese: koryu ──
    'japanese': dict(
        teaches=['katana', 'tachi', 'odachi', 'tsurugi', 'yari', 'kama_yari', 'naginata'],
        candidates=[],
        skills=['technique', 'parry'],
        abilities={
            'shinogi': _a('japanese', 'S2', 'spine_press', '*', 1.6, 'exchange.bind_entry', 'C', 'C', 'KORYU',
                        "Shinogi — pressing along the ridge and spine of a single-edged blade (existing).",
                        existing=True),
            'sen_no_sen': _a('japanese', 'S2', 'precommit', '*', 1.08, 'exchange.read', 'C', 'C', 'KORYU',
                        "Sen no sen — taking the initiative at the instant the opponent's intent forms, reading the "
                        "attack before the blade moves. RE-HOME of a name that was removed when its `seize` lever "
                        "died (ED-PC-0042): `precommit` has since gained a consumer (read_contest read_d). The sen "
                        "terms' meanings differ between authors and were not found in the texts searched."),
            'metsuke': _a('japanese', 'S2', 'visual', '*', 1.06, 'exchange.read', 'C', 'C', 'KORYU',
                        "Metsuke — the gaze: perceiving the opening (suki) without fixing on the blade. Feeds "
                        "read_contest, reopen_prob and disengage_clean_p through the visual lever.",
                        also=('reopen.measure', 'disengage.withdraw')),
            'kiriotoshi': _a('japanese', 'S2', 'guard_prior_parry', '*', 1.40, 'exchange.mode', 'C', 'C', 'KORYU',
                        "Kiriotoshi — the cut that beats the opponent's blade down and strikes as one act; the "
                        "habitual answer to a cut is the cutting parry."),
            'zanshin': _a('japanese', 'S2', 'tempo', '*', 1.08, 'exchange.roll', 'C', 'C', 'KORYU',
                        "Zanshin — continued awareness after the cut: the fighter does not lose the initiative by "
                        "striking (init_overcommit_loss divides by the tempo factor)."),
        }),
    # ── Chinese and Filipino: NOT AUTHORED (see 00_tradition_sets.md section 6) ──
    'chinese': dict(teaches=['guandao', 'podao', 'ji', 'changdao', 'nandao', 'jian', 'hook_sword', 'staff'],
                    candidates=[], skills=[], abilities={}),
    'filipino': dict(teaches=[], candidates=[], skills=[], abilities={}),
}

# Held entries: written down so a later session does not rediscover and re-propose them blind.
HELD = {
    'perfil': dict(tradition='spanish', lever='facing_regime',
                   why="Destreza's profile stance is a body-facing concept, so the lever fits; but facing moves "
                       "close_rate by ~0.14% (PC_personal_combat.md item 9, config FACING_REGIME_K) so the ability "
                       "would be inert, and the term was not verified."),
    'gardant': dict(tradition='english', lever='guard_prior_parry',
                    why="Silver names the guardant fight as essential (V) but what it does mechanically was not "
                        "read; a lever cannot be chosen without that."),
}

NOT_HOOKED = {
    'exchange.commit': "commit_depth is owned by disposition (D3 unresolved, PCA section 9 P1); a tradition term here "
                       "would compose with an axis whose intended shape is undecided.",
    'burst.continuation': "burst length is a separation reason (clean_defence / burst_ceiling / collapse), not a "
                          "contest. A tradition that extends it is the retired imposition gate (ED-PC-0023); "
                          "tradition reaches it only through the tempo lever upstream.",
}


# ── Relations: how one ability sets up another, or changes behaviour around its lever ─────────────────
# The live record is flat: `_invested` checks tradition membership only and abilities on a lever multiply. These are
# the three relations the draft adds, each with the engine site that would have to honour it. NONE IS BUILT.
#   requires : ability can be invested only while every `needs` ability is invested to at least that level
#              (the access gate gains a second clause; phase4_5_plan section 4b's `prereq`).
#   widens   : with every `with_` ability invested, a named GATE admits a case it refuses today (agency proposal
#              Class B: an ability may change AVAILABILITY, never magnitude). It only ever ADDS cases, so an
#              empty kit stays byte-identical to today.
#   branch   : the follow-up the fighter takes depends on a state the lever already computes, instead of one
#              fixed weight. `selects` maps that state to the ability that then applies.
# RULES. Relations stay inside one tradition. Chain depth <= 3 (Fiore: 'few plays go past the third master', V,
# Wiktenauer Fiore page). A relation is authored only where a source states the dependency; the rest of each kit
# is left flat and is listed in RELATION_GAPS rather than invented.
RELATIONS = [
    dict(id='IT-1', kind='requires', tradition='italian', ability='mezzo_tempo', needs={'misura': 1.0},
         term='V', mech='V', src='CAPO',
         note="Capoferro ties the time available to the measure: wide measure takes a tempo and a half, fixed-foot narrow "
              "a whole tempo, the narrowest half a tempo. A half-time counter presupposes holding the measure it is "
              "taken in."),
    dict(id='IT-2', kind='requires', tradition='italian', ability='contratempo', needs={'misura': 1.0},
         term='V', mech='V', src='CAPO', note="As IT-1: the blow in counter-time is delivered 'at narrow measure'."),
    dict(id='IT-3', kind='widens', tradition='italian', ability='mezzo_tempo', with_={'misura': 1.0}, gate_class='B',
         gate="wrapper.engagement: `if read_win and commit>=cfg['DEEP_COMMIT']` before counter_select",
         effect="a won read at narrow measure admits a counter attempt without a deep commit; the existing success "
                "roll and the punishment of a miss are untouched",
         term='V', mech='U', src='CAPO',
         note="Capoferro's counter-time happens when both 'come at the same time to narrow measure'; he does not say the "
              "attacker must have committed deeply. The engine's DEEP_COMMIT gate is the repo's, not the treatise's. "
              "BUILD NOTE: in wrapper.engagement the Indes steal and counter_select share ONE `if` on that gate, so the "
              "block must be split or the widening also grants the steal."),
    dict(id='DE-1', kind='requires', tradition='german', ability='indes', needs={'fuehlen': 1.0},
         term='C', mech='C', src='RINGECK',
         note="The repo's decomposition pairs 'Fuhlen / Indes' (feel, then the decision in the same tempo). Not re-read."),
    dict(id='DE-2', kind='branch', tradition='german', ability='fuehlen',
         selects={'soft': 'absetzen', 'hard': 'staerke_schwaeche'},
         site="bind state already computed in bind_sigma (the sign of the tactile read against the opponent's pressure)",
         term='V', mech='U', src='LIECH',
         note="Zornhau, Wiktenauer v.27-31: it threatens the point; if the opponent reacts, take the blow off above; if "
              "the opponent is strong, wind and thrust. The follow-up depends on what the fighter feels. The mapping of "
              "soft/hard onto the engine's bind state is mine."),
]

RELATION_GAPS = {
    'spanish': "no relation stated in any source read (the Destreza terms were not found in the text read)",
    'english': "Silver's governors are named but not listed in the text read, so no dependency can be cited",
    'japanese': "the sen terms were not found in the texts searched; a sen -> zanshin dependency is plausible and unsourced",
}
