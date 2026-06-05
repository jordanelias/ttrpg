# Mass-Battle Breakthrough Investigation — Resolution-vs-History Validation
**2026-06-05 · Stream B (active-work-index-2026-06-04) · scope: `mass_battle` continuous-scale unit-duel resolution**

> `[SELF-AUTHORED — bias risk]` This validates an engine that the same session was actively modifying; the bias-correcting finding (the wedge's frontal loss is historically *correct*, not a defect) is the result of an adversarial steelman of the breakthrough premise, not a defence of prior work.

## Verdict
The pristine engine's emergent duel outcomes already correspond to historical precedent across the archetypal matchups, and the casualty signature matches the historical pattern. The "breakthrough" target that drove this investigation — a wedge winning a **frontal** grind against a solid line — was **misframed**: historically the wedge wins by penetrating a gap to the rear/command (Gaugamela), not by grinding a solid line (Goldsworthy: deep-narrow risks outflanking). **No engine change is warranted.** The package is unchanged at battery digest `7655743e5a91b238`.

## Method
Continuous-scale duels, `PER_CELL=1`; parameterised formations (shape · troops · concentration · stance · discipline · command · speed · troop_type · instructions); unscripted resolution via `run_battle`, `max_turns=180`; N=18 × both side-orderings (36 trials/matchup). Recorded: intended-winner rate + surviving-HP fraction of winner vs loser over decisive trials.

## Results
| matchup | intended-win | winner hp% | loser hp% | decisive |
|---|---|---|---|---|
| Wedge vs solid Line (frontal) | 33% | 84 | 50 | 36/36 |
| deepColumn vs thinLine | 50% | 87 | 63 | 36/36 |
| command-dominates | 100% | 93 | 52 | 36/36 |
| ShieldWall vs Wedge | 97% | 94 | 46 | 36/36 |
| cavalry vs braced infantry | 0% | 93 | 45 | 36/36 |

## Validation against precedent
- **Win-direction** matches on every clear matchup: the wedge loses the frontal grind (Goldsworthy 10.1177/096834459700400101; Arrian on Gaugamela — the Companion wedge went *through a gap* straight at Darius, whose flight collapsed the army); command dominates; the braced shield wall stops the wedge; braced disciplined infantry stops cavalry (Waterloo squares).
- **Casualty asymmetry** matches Sabin (10.2307/300198): the victor retains far more (84–94%) than the loser (45–63%), every trial decisive, losers routing well before annihilation — the victory is the enemy's break, not mutual attrition.
- **deepColumn = 50% (contestable):** the column trades depth-cohesion/endurance (the stamina chain — deeper drains slower, fights better longer) against a narrower frontage the wider line can threaten, exactly Goldsworthy's deep-narrow-outflanking caution applied to the column. Leuctra's *decisive* deep-column win required tactical setup (oblique order, refused flank, local massing) absent from a naked head-on. 50% is defensible. If a head-on depth edge is wanted, the lever is the **existing** depth-endurance parameters (`PC_DEPTH_ROTATE`, `PC_STAM_SIGMA`) — a calibration, not a new coupling. *[historical-interpretation call — deferred to Jordan]*

## Finding — NULL on the breakthrough quest
The radial-concentration exchange-sigma channel prototyped this session, and the prior session's breakthrough attempts, solved a non-problem: the existing primitives already emit the historical outcome. Diagnosis: `_lanchester_strength` is frontage-only — **correct**, since Goldsworthy is explicit that rear ranks "cannot have inflicted any significant damage upon the enemy"; depth's historical role is cohesion / endurance / sustainment, not lethality. The wedge's narrow frontage means it bleeds against a wider line, which *is* the historically-correct outcome for a frontal assault. The prototype was reverted; the package is pristine.

## Capability bound (what this licenses claiming)
The engine resolves parameterised custom formations **emergently** — the winner and casualties fall out of the primitives interacting (frontage→attrition, depth→endurance, casualties→morale→rout, bracing→shock-resistance, command) with no scripted result — and the emergence is historically correct at the **qualitative / relational level** (win-direction + casualty asymmetry) for the dynamics tested (depth↔frontage, bracing, command, cavalry↔infantry), at the **unit-duel scale**. Not established: accuracy across the full formation space; quantitative reproduction of named battles (losers retain ~45–63%, not Sabin's <5%); decisive formation wins that depend on tactical context (oblique order, gaps, flanking-in-play) rather than formation shape alone; battle-scale multi-unit emergence.

## Reproduce
`PER_CELL=1 PYTHONHASHSEED=0 PYTHONPATH=<mass_battle sim root> python3 observe.py 18`

```python
"""Observe pristine-engine emergence on the historical matchups vs precedent.
Per duel: intended-winner rate (both side-orderings) + mean surviving-HP fraction of
winner vs loser over decisive battles. Requires PER_CELL=1. N from argv[1] (default 20)."""
import os, sys, random
assert os.environ.get('PER_CELL') == '1', "run with PER_CELL=1"
import mass_battle.orchestration as O
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20

def mk(shape, troops, conc, fac, **kw):
    ad = -1 if fac == 'A' else 1
    sr = O.SIDE_A_START_ROW if fac == 'A' else O.SIDE_B_START_ROW
    su = O.Subunit(shape=shape, troop_type=kw.get('troop_type', 'infantry'), tier=3,
                   starting_position=(sr, kw.get('anchor', 8)), advance_dir=ad,
                   unit_type=kw.get('unit_type', 'melee'), instructions=kw.get('instructions', ()),
                   troops=troops, concentration=conc)
    return O.Unit(name=fac, faction=fac, power=kw.get('power', 4), command=kw.get('command', 4),
                  discipline=kw.get('discipline', 5), discipline_start=kw.get('discipline', 5),
                  morale=kw.get('morale', 6), morale_start=kw.get('morale', 6),
                  subunits=[su], dr=1, stance=kw.get('stance', 'balanced'),
                  speed=kw.get('speed', 'Standard'))

DUELS = [
    ('Wedge>Line',            ('Arrowhead', 4000, 120, {}), ('Line', 4000, 120, {})),
    ('deepColumn>thinLine',   ('Column', 4000, 120, {}),    ('Line', 4000, 120, {})),
    ('command-dominates',     ('Line', 2000, 120, {'command': 7}), ('Line', 6000, 120, {'command': 2})),
    ('ShieldWall>Wedge',      ('Line', 4000, 120, {'stance': 'hold', 'discipline': 7, 'instructions': ('brace', 'hold')}),
                              ('Arrowhead', 4000, 120, {})),
    ('cav-vs-BRACED',         ('Arrowhead', 4000, 120, {'troop_type': 'cavalry', 'speed': 'Fast'}),
                              ('Line', 4000, 120, {'stance': 'hold', 'discipline': 8, 'instructions': ('brace', 'hold')})),
]

def frac(u):
    return (u.hp / u.hp_max) if getattr(u, 'hp_max', 0) else 0.0

for name, win, lose in DUELS:
    iw = dec = 0; wf, lf = [], []
    for ordering in (1, 2):
        for s in range(N):
            random.seed(s + 7000 + ordering * 100000)
            if ordering == 1:
                ua = mk(*win[:3], 'A', **win[3]); ub = mk(*lose[:3], 'B', **lose[3]); want = 'A'
            else:
                ua = mk(*lose[:3], 'A', **lose[3]); ub = mk(*win[:3], 'B', **win[3]); want = 'B'
            res = O.run_battle(ua, ub, max_turns=180).get('winner')
            if res in ('A', 'B'):
                dec += 1
                winner, loser = (ua, ub) if res == 'A' else (ub, ua)
                wf.append(frac(winner)); lf.append(frac(loser)); iw += (res == want)
    tot = 2 * N
    print(f"{name:22} {iw:2d}/{tot}  win {100*sum(wf)/len(wf):.0f}%  lose {100*sum(lf)/len(lf):.0f}%  (dec {dec}/{tot})")
```

## Citations
- Goldsworthy, A. K. (1997). *The Othismos, Myths and Heresies of the Greek Phalanx.* War in History 4(1). [10.1177/096834459700400101](https://doi.org/10.1177/096834459700400101)
- Sabin, P. (2000). *The Face of Roman Battle.* Journal of Roman Studies 90, 1–17. [10.2307/300198](https://doi.org/10.2307/300198)
- Arrian, *Anabasis Alexandri* III (Gaugamela) — primary source.
- Engine (pristine, battery digest `7655743e5a91b238`): `orchestration.py` (`_lanchester_strength`, `morale_check_phase`), `percell.py` (`update_stamina`, `_stamina_sigma`), `resolution.py` (`_morale_sigma`).
- `designs/provincial/mass_battle_v30.md` §A.4 — canonical morale triggers (unchanged by this work).
