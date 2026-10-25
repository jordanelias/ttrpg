"""P7 -- do the committed story instruments count refusals as story? Runs harness/storybar.py::drive
(the owner's own composition), reads storybar.read + chronicle.deepest_chain, and classifies every act
by the DRIVER's definition (loop/driver.py:489-505): refused if any of its Events is a row
`emits_on_refusal` kind. Reports: deepest-chain length and its refused acts; the share of refused acts
among all acts with depth >= 2; and the cross-person share recomputed with refused antecedents removed
(a 'refusal null' storybar does not have).

  PYTHONHASHSEED=0 python3 probes/p7_chain_refusals.py SEASONS SEED [SEED ...]
"""
import sys
from collections import defaultdict

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.harness import storybar as SB
from engine.season.harness import chronicle as CH
from engine.season.data.verbs import VERB_TABLE

seasons = int(sys.argv[1])
tot = defaultdict(int)
for seed in [int(s) for s in sys.argv[2:]]:
    w, d, bounds = SB.drive(seed, seasons, "off", None)
    res = SB.read(w.log, d.act_of, bounds)
    rows = res["acts"]
    refused = set()
    verb = {}
    for e in w.log:
        a = d.act_of.get(e.id)
        if a is None:
            continue
        verb[a.id] = a.verb
        if e.kind in (VERB_TABLE[a.verb].emits_on_refusal or ()):
            refused.add(a.id)
    chain = CH.deepest_chain(rows)
    ch_ref = [a for a in chain if a in refused]
    deep = [a for a, r in rows.items() if r["depth"] >= 2]
    deep_ref = [a for a in deep if a in refused]
    cross_any = sum(1 for r in rows.values() if r["cross"])
    cross_exec = sum(1 for a, r in rows.items()
                     if a not in refused and any(b not in refused for b in r["cross"]))
    exec_n = sum(1 for a in rows if a not in refused)
    print(f"seed={seed} acts={len(rows)} refused={len(refused & set(rows))} chain_len={len(chain)} "
          f"chain_refused={len(ch_ref)} chain_verbs={[verb.get(a) + ('*' if a in refused else '') for a in chain]} "
          f"depth>=2 acts={len(deep)} of_which_refused={len(deep_ref)} "
          f"cross_share_all={cross_any}/{len(rows)} cross_share_exec_on_exec={cross_exec}/{exec_n} "
          f"hash={w.content_hash()[:12]}", flush=True)
    for k, v in (("chain", len(chain)), ("chain_ref", len(ch_ref)), ("deep", len(deep)),
                 ("deep_ref", len(deep_ref)), ("acts", len(rows)), ("cross_any", cross_any),
                 ("cross_exec", cross_exec), ("exec", exec_n)):
        tot[k] += v
print("TOTAL", dict(tot))
