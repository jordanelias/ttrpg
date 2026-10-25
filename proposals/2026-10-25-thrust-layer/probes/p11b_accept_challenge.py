"""P11b (supersedes P11: adds the TARGET of each prior challenge) -- A12(a) / NEEDS-RUN "accept deaths": was a `challenge.issued` act behind each `person.died` whose
cause is an `accept`? P4 never checked. For each death whose causing act is `accept`: the acceptor, the
subject (the claimed challenger), and
  issued_by_subject   a `challenge.issued` Event in the log BEFORE the death, whose act's actor is the subject
  issued_either       ... whose act's actor is either party
  ledger_claim        the acceptor's ledger holds a claim with predicate `challenge.issued` whose subject is the
                      `accept` subject or whose `about`/referent names it -- read off the ledger at death time
Also reports the total `challenge.issued` Events in each seed's log (the supply).
  PYTHONHASHSEED=0 python3 probes/p11_accept_challenge.py SEASONS SEED [SEED ...]
"""
import sys
from collections import Counter

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory
from engine.season.state.carriers import subject_of
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

seasons = int(sys.argv[1])
T = Counter()
for seed in [int(s) for s in sys.argv[2:]]:
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    snap = []          # (death event index, acceptor, subject, acceptor ledger snapshot)
    orig_res = d.resolve

    def resolve(tok, acts, cmd, _o=orig_res):
        # ledgers as they stand BEFORE this round's acts resolve: what the chooser could have read
        led = {a.actor: [(c.predicate, c.subject) for c in w.persons[a.actor].ledger]
               for a in acts if a.verb == "accept" and a.actor in w.persons}
        ev = _o(tok, acts, cmd)
        for a in acts:
            if a.verb == "accept" and a.actor in led:
                snap.append((a.id, a.actor, subject_of(a), led[a.actor]))
        return ev

    d.resolve = resolve
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    by_act = {s[0]: s for s in snap}
    log = list(w.log)
    issued = []
    for i, e in enumerate(log):
        if e.kind == "challenge.issued":
            a = d.act_of.get(e.id)
            issued.append((i, a.actor if a else None, subject_of(a) if a else None))
    T["challenge_issued_events"] += len(issued)
    n_acc_att = sum(1 for e in log if (d.act_of.get(e.id) is not None and d.act_of[e.id].verb == "accept"))
    for i, e in enumerate(log):
        if e.kind != "person.died":
            continue
        a = d.act_of.get(e.id)
        if a is None or a.verb != "accept":
            continue
        _, actor, subj, led = by_act.get(a.id, (None, a.actor, subject_of(a), []))
        prior = [x for x in issued if x[0] < i]
        by_subj = any(x[1] == subj for x in prior)
        either = any(x[1] in (actor, subj) for x in prior)
        aimed = [x for x in prior if (x[1] == subj and x[2] == actor)]
        aimed_any = [x for x in prior if ({x[1], x[2]} == {actor, subj})]
        lc = any(p == "challenge.issued" and (s == subj or s == actor) for p, s in led)
        lc_any = any(p == "challenge.issued" for p, s in led)
        print(f"seed={seed} death_log_idx={i} acceptor={actor} subject={subj} prior_challenge_events={len(prior)} "
              f"issued_by_subject={by_subj} issued_either={either} acceptor_ledger_claim_about_pair={lc} challenge_subject_to_acceptor={len(aimed)} challenge_either_direction={len(aimed_any)} prior_list={[(x[1], x[2]) for x in prior]} "
              f"acceptor_ledger_any_challenge_claim={lc_any}")
        T["accept_deaths"] += 1
        T["issued_by_subject"] += by_subj
        T["issued_either"] += either
        T["aimed_at_acceptor"] += bool(aimed)
        T["aimed_either_direction"] += bool(aimed_any)
        T["ledger_pair"] += lc
        T["ledger_any"] += lc_any
    print(f"seed={seed} log={len(log)} hash={w.content_hash()[:16]} challenge.issued_events={len(issued)}", flush=True)
print("TOTAL", dict(T))
