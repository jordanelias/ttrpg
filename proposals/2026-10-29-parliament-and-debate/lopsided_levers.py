"""Second half of the lopsidedness inquiry (companion to lopsided_mechanism.py).

  N  narrative   feed real track-proceeding results to narrative.summarize, which was written and tested
                 for winners 'a'/'b' while the track proceedings return 'A_decisive', 'committee', ...
  L  levers      the weak side (faculty 1) against faculty 4 in the track proceedings, given in turn the
                 levers the kernel has and the int-only sides of the stress test never used: evidence on
                 the live ground, a raised starting standing, institutional pressure toward it.

Same rule as the other probes: no chosen count; each cell samples until its slice of --budget-s ends and
logs n; every cell is one flushed JSONL line.
"""
import argparse, dataclasses, os, random, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lopsided_mechanism import cell, side, Log, git, sc, ROOT  # noqa: E402
from systems.social_contest.sim.contest import narrative as NAR  # noqa: E402
from systems.social_contest.sim.contest.contract import Pressure  # noqa: E402


def narrative_cell(log, proc, fa, fb, seconds, pa='logos', pb='logos'):
    rnd = random.Random(hash(('N', proc, fa, fb)) & 0xffffffff)
    shapes = Counter()           # (band, shape)
    names = Counter()            # what render() calls the winner, per band
    samples = {}
    n = 0
    end = time.time() + seconds
    while time.time() < end:
        for _ in range(20):
            random.seed(rnd.randrange(2 ** 31))
            c = sc.build_contest(fa, fb, venue=proc)
            (band, why), bout = sc.resolve_contest(c, policy_a=pa, policy_b=pb, record=True)
            ch = NAR.summarize(bout.log, band, why)
            shapes[(band, ch.shape)] += 1
            if band not in samples:
                samples[band] = ch.render()
            n += 1
    log.w('cell', cell='N_narrative', proceeding=proc, faculty_A=fa, faculty_B=fb, n=n,
          shapes={f'{b}|{s}': v for (b, s), v in sorted(shapes.items())}, sample_render=samples)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--budget-s', type=float, required=True)
    ap.add_argument('--log', required=True)
    args = ap.parse_args()
    log = Log(args.log)
    log.w('manifest', head=git('rev-parse', 'HEAD'), dirty=git('status', '--porcelain'), argv=sys.argv,
          note='levers + narrative probe; kernel is evaluated, not adopted (SC-05)')
    tracks = ['formal_contest', 'royal_audience', 'church_tribunal']
    start_ground = {'formal_contest': 'quality', 'royal_audience': 'quality', 'church_tribunal': 'fact'}
    n_cells = len(tracks) * (2 + 7)
    per = args.budget_s / n_cells
    log.w('plan', cells=n_cells, per_cell_s=round(per, 2))

    for p in tracks:
        g = start_ground[p]
        # N: narrative layer on equal and unequal sides
        narrative_cell(log, p, 4, 4, per)
        narrative_cell(log, p, 1, 4, per)
        # L: levers for the weak side (A, faculty 1) against faculty 4, both logos unless noted
        cell(log, 'L_lever', per, p, 1, 4, tag='none (bare skill)')
        cell(log, 'L_lever', per, p, {'faculty': 1, 'standing_start': 8.0}, 4, tag='A standing_start=8')
        cell(log, 'L_lever', per, p, {'faculty': 1, 'evidence': [(g, 3.0)]}, 4, pa='advocate', tag='A 1 evidence w=3')
        cell(log, 'L_lever', per, p, {'faculty': 1, 'evidence': [(g, 3.0), (g, 3.0)]}, 4, pa='advocate', tag='A 2 evidence w=3')
        cell(log, 'L_lever', per, p, {'faculty': 1, 'evidence': [(g, 1.0)]}, 4, pa='advocate', tag='A 1 evidence w=1')
        pr = Pressure(toward='a', institutional=1.0, public=0.0)
        cell(log, 'L_lever', per, p, 1, 4, mutate=lambda v, pr=pr: dataclasses.replace(v, pressure=pr),
             tag='institutional pressure toward A =1.0')
        cell(log, 'L_lever', per, p, {'faculty': 1, 'evidence': [(g, 3.0)], 'standing_start': 8.0}, 4,
             pa='advocate', mutate=lambda v, pr=pr: dataclasses.replace(v, pressure=pr),
             tag='evidence + standing 8 + pressure')
    log.w('done', cells=n_cells)


if __name__ == '__main__':
    main()
