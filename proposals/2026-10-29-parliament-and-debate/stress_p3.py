"""Stress harness for PROPOSAL 3, "Authority first" (social contest). Reads the tree, writes only the
log. Every event is ONE FLUSHED, FSYNCED JSON LINE (PR #530's convention). Run from the repo root:

  python proposals/2026-10-29-parliament-and-debate/stress_p3.py --log OUT.jsonl --sections A C B ...

Sections (each independent; each ends in `section_end`; an exception inside one is logged as `error`
with a full traceback and the next section runs):
  A  legitimacy index L on build_realm 0..2 (claims 'church L .78 at T9 ...', 'commit share zero in 14 of 16')
  B  case-opening from a church seat in T1 / T4 (purview reads Office.rung, not scope_rung)
  C  authority.by_faction recomputed from offices.yaml (19 / 7 / 5)
  D  bench filtered by authority vs the gate's may_determine (a model in which they disagree)
  E  forum contest, `defy` and silence dominance (payoff model on real roll probabilities)
  F  custody as a warrant; the appeal and the pardon on a real world
  G  how often a Crown seat-holder is a party to a matter (real seasons)
  H  C1 deletions in a scratch worktree (separate script path: --worktree)
  S1 S2 S3 S4 S5 S6 S7  the brief's eight dimensions (S8 is H)
No chosen horizon: a run stops on the first of a crash, a quiet result, or --budget-s.
"""
import argparse, datetime, json, math, os, random, subprocess, sys, time, traceback, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
os.environ.setdefault('PYTHONHASHSEED', '0')


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


class Log:
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'a', encoding='utf-8', buffering=1)
        self.counts = collections.Counter()

    def w(self, kind, **kw):
        self.counts[kind] += 1
        self.f.write(json.dumps({'t': utc(), 'kind': kind, **kw}, default=str) + '\n')
        self.f.flush()
        os.fsync(self.f.fileno())


LOG = None


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(c - h, 4), round(c + h, 4))


def git(*a):
    try:
        return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as e:
        return f'unavailable: {e}'


def guarded(fn):
    def run(*a, **k):
        LOG.w('section_start', section=fn.__name__)
        t0 = time.time()
        try:
            fn(*a, **k)
        except Exception as e:
            LOG.w('error', section=fn.__name__, type=type(e).__name__, msg=str(e)[:500],
                  traceback=traceback.format_exc())
        LOG.w('section_end', section=fn.__name__, wall_s=round(time.time() - t0, 1))
    run.__name__ = fn.__name__
    return run


# ---------------------------------------------------------------------------------------------
# shared world helpers (REAL engine pieces)
# ---------------------------------------------------------------------------------------------
def real():
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q
    from engine.season.data.rosters import faction_prop_id, FACTION_BY_PROP
    return build_realm, world_q, faction_prop_id, FACTION_BY_PROP


FACTIONS = ["Crown", "Hafenmark", "Varfell", "Church of Solmund"]


def territory_of(w, world_q, rung):
    for a in world_q.ancestry(w, rung):
        r = w.rungs.get(a)
        if r is not None and r.kind == "territory":
            return a
    return None


# ---------------------------------------------------------------------------------------------
# A -- legitimacy L
# ---------------------------------------------------------------------------------------------
CLAIMED_CHURCH = {"terr_T9": .78, "terr_T8": .59, "terr_T14": .57, "terr_T1": .53, "terr_T3": .45, "terr_T4": .38, "terr_T2": .37}
CLAIMED_CROWN = {"terr_T9": .77, "terr_T14": .75, "terr_T1": .74, "terr_T3": .70, "terr_T2": .68, "terr_T5": .67, "terr_T4": .57}


def clamp01(x):
    return max(0.0, min(1.0, x))


def L_from(mean_op, opinion_full=1.0):
    return clamp01(0.5 + mean_op / (2 * opinion_full))


def legitimacy_table(w, world_q, faction_prop_id, opinion_full=1.0, weighted=False, level="territory"):
    """{faction: {rung: (n_residents, mean_opinion, L)}} using the proposal's formula verbatim."""
    res = world_q.residence_of(w)
    op = {}
    for f in FACTIONS:
        prop = faction_prop_id(f)
        op[f] = {pid: world_q.opinion_of(w, p, prop) for pid, p in w.persons.items()}
    out = {f: {} for f in FACTIONS}
    groups = collections.defaultdict(list)
    for pid, r in res.items():
        if pid not in w.persons:
            continue
        for a in world_q.ancestry(w, r):
            rr = w.rungs.get(a)
            if rr is not None and rr.kind == level:
                groups[a].append(pid)
    for rung, pids in groups.items():
        for f in FACTIONS:
            if weighted:
                tw = sum(w.persons[p].weight for p in pids)
                m = sum(op[f][p] * w.persons[p].weight for p in pids) / tw
            else:
                m = sum(op[f][p] for p in pids) / len(pids)
            out[f][rung] = (len(pids), m, L_from(m, opinion_full))
    return out, op


@guarded
def sec_A():
    build_realm, world_q, faction_prop_id, FACTION_BY_PROP = real()
    LOG.w('plan', section='A', what='rebuild L per territory on build_realm seeds 0-2, 4 factions; compare to the proposal figures; sweep opinion_full; weighted vs unweighted; settlement-level n')
    LOG.w('claim', where='P3 3.3 "Measured at opinion_full = 1, seed 0, season 0"',
          quote='church L is T9 .78, T8 .59, T14 .57, T1 .53, T3 .45, T4 .38, T2 .37; Crown L is T9 .77, T14 .75, T1 .74, T3 .70, T2 .68, T5 .67, T4 .57. Territories peopled only by cohorts read .50. 166 opinion_of calls took 0.04 s')
    LOG.w('claim', where='P3 3.3 fallback', quote='the Church has 7 committed members, 6 in T9 and 1 in T1, so commit-share piety is 0 in 14 of 16 territories')
    for seed in (0, 1, 2):
        t0 = time.time()
        w = build_realm(seed)
        tb = time.time() - t0
        t1 = time.time()
        tab, op = legitimacy_table(w, world_q, faction_prop_id)
        tq = time.time() - t1
        ncalls = len(w.persons) * len(FACTIONS)
        LOG.w('batch', section='A', seed=seed, persons=len(w.persons), residents=len(world_q.residence_of(w)),
              territories_with_residents=len(tab['Crown']), territories_total=sum(1 for r in w.rungs.values() if r.kind == 'territory'),
              opinion_of_calls=ncalls, opinion_secs=round(tq, 3), build_secs=round(tb, 2),
              note='proposal: 166 calls (2 factions x 83) in 0.04 s; here 4 factions')
        for f in FACTIONS:
            rows = {t.replace('terr_', ''): {'n': v[0], 'mean_op': round(v[1], 4), 'L': round(v[2], 3)} for t, v in sorted(tab[f].items())}
            Ls = sorted(v[2] for v in tab[f].values())
            at_half = sum(1 for v in tab[f].values() if abs(v[2] - .5) < 1e-12)
            lo, hi = wilson(at_half, len(Ls))
            LOG.w('result', section='A', seed=seed, faction=f, n_territories=len(Ls), L_min=round(Ls[0], 3),
                  L_median=round(Ls[len(Ls)//2], 3), L_max=round(Ls[-1], 3),
                  share_exactly_half=round(at_half / len(Ls), 3), share_exactly_half_n=at_half, wilson95=[lo, hi],
                  share_below_half=sum(1 for x in Ls if x < .5 - 1e-12), per_territory=rows)
        if seed == 0:
            for f, claimed in (("Church of Solmund", CLAIMED_CHURCH), ("Crown", CLAIMED_CROWN)):
                for t, c in claimed.items():
                    got = tab[f].get(t)
                    g = None if got is None else round(got[2], 3)
                    ok = g is not None and abs(g - c) <= 0.0051
                    if ok:
                        LOG.w('result', section='A', check='claimed_figure', faction=f, territory=t, claimed=c, reproduced=g,
                              n_residents=got[0], verdict='HELD (within .005)')
                    else:
                        LOG.w('fail', section='A', check='claimed_figure', faction=f, territory=t, claimed=c, reproduced=g,
                              n_residents=None if got is None else got[0], diff=None if g is None else round(g - c, 4),
                              proposal_said=f'{f} L at {t} = {c}')
            # claimed ordering: is it complete? which territories did the proposal omit and what do they read
            for f, claimed in (("Church of Solmund", CLAIMED_CHURCH), ("Crown", CLAIMED_CROWN)):
                omitted = {t: round(v[2], 3) for t, v in tab[f].items() if t not in claimed and abs(v[2] - .5) > 1e-12}
                LOG.w('result', section='A', check='omitted_non_half_territories', faction=f, omitted=omitted,
                      note='territories the proposal did not list that read other than .50')
            # cohort-only .50 claim
            res = world_q.residence_of(w)
            cohort_only = []
            for t in tab['Crown']:
                pids = [p for p, r in res.items() if t in world_q.ancestry(w, r)]
                if all(w.persons[p].weight > 1 for p in pids):
                    cohort_only.append((t, len(pids), [round(tab[f][t][2], 3) for f in FACTIONS]))
            LOG.w('result', section='A', check='cohort_only_territories', territories=cohort_only,
                  verdict='HELD' if cohort_only and all(all(abs(x - .5) < 1e-9 for x in r[2]) for r in cohort_only) else 'BROKE')
            # all-zero-opinion territories vs cohort-only: are .50 territories exactly the ones with zero opinion?
            zero = [t for t in tab['Crown'] if all(abs(tab[f][t][1]) < 1e-12 for f in FACTIONS)]
            LOG.w('result', section='A', check='zero_opinion_territories', n=len(zero), territories=zero,
                  note='territories where every faction reads mean opinion exactly 0 (L = .50)')
            # territories with no residents at all (L undefined)
            allterr = [k for k, r in w.rungs.items() if r.kind == 'territory']
            empty = [t for t in allterr if t not in tab['Crown']]
            LOG.w('fail' if empty else 'null', section='A', check='territory_with_no_residents',
                  territories=empty, proposal_said='L(f, v) = clamp(0.5 + mean_{p resident under v} ...) with no case for an empty set',
                  consequence='mean of an empty set is 0/0: the formula is undefined; a naive implementation raises ZeroDivisionError')
        # commit-share fallback
        res = world_q.residence_of(w)
        church = faction_prop_id("Church of Solmund")
        by_t = collections.Counter()
        for t in w.tenures:
            if t.kind == "commit" and t.live and t.object == church and t.subject in w.persons:
                r = res.get(t.subject)
                by_t[territory_of(w, world_q, r) if r else None] += 1
        n_commit = sum(by_t.values())
        terrs = [k for k, r in w.rungs.items() if r.kind == 'territory']
        zero_t = [t for t in terrs if by_t.get(t, 0) == 0]
        populated = list(tab['Crown'])
        zero_p = [t for t in populated if by_t.get(t, 0) == 0]
        LOG.w('result', section='A', check='church_commit_share', seed=seed, church_commits=n_commit, by_territory=dict(by_t),
              territories_total=len(terrs), zero_of_all=len(zero_t), territories_populated=len(populated), zero_of_populated=len(zero_p),
              proposal='7 committed, 6 in T9 and 1 in T1, zero in 14 of 16',
              verdict=('HELD' if (seed == 0 and n_commit == 7 and by_t.get('terr_T9') == 6 and by_t.get('terr_T1') == 1) else ('n/a seed' if seed else 'BROKE')))
        # sweeps (one-at-a-time) on the church and crown
        for of in (0.5, 1.0, 2.0, 3.0):
            tabx, _ = legitimacy_table(w, world_q, faction_prop_id, opinion_full=of)
            LOG.w('result', section='A', check='opinion_full_sweep', seed=seed, opinion_full=of,
                  church_L={t.replace('terr_', ''): round(v[2], 3) for t, v in sorted(tabx['Church of Solmund'].items()) if v[0] >= 3},
                  church_L_range=[round(min(v[2] for v in tabx['Church of Solmund'].values()), 3), round(max(v[2] for v in tabx['Church of Solmund'].values()), 3)])
        tabw, _ = legitimacy_table(w, world_q, faction_prop_id, weighted=True)
        dif = {f: max(abs(tabw[f][t][2] - tab[f][t][2]) for t in tab[f]) for f in FACTIONS}
        LOG.w('result', section='A', check='weighted_vs_unweighted_mean', seed=seed, max_abs_L_diff_by_faction={k: round(v, 3) for k, v in dif.items()},
              note='cohorts are Persons at weight 2; the proposal says "mean over residents" and its script used the unweighted mean; weighting by Person.weight moves L by this much')
        # venue level: where cases actually happen is a settlement/hearth, not a territory
        sett, _ = legitimacy_table(w, world_q, faction_prop_id, level='settlement')
        ns = [v[0] for v in sett['Crown'].values()]
        nsett = sum(1 for r in w.rungs.values() if r.kind == 'settlement')
        LOG.w('result', section='A', check='residents_per_settlement', seed=seed, settlements_total=nsett, settlements_with_residents=len(ns),
              n_residents_min=min(ns), n_residents_median=sorted(ns)[len(ns)//2], n_residents_max=max(ns),
              settlements_with_le2_residents=sum(1 for x in ns if x <= 2),
              share_le2=round(sum(1 for x in ns if x <= 2) / len(ns), 3), wilson95=wilson(sum(1 for x in ns if x <= 2), len(ns)),
              church_L_spread_at_settlement=[round(min(v[2] for v in sett['Church of Solmund'].values()), 3), round(max(v[2] for v in sett['Church of Solmund'].values()), 3)],
              note='P3 5.1: heard_at: party = the matter place; judging_set takes a venue. L at that venue is over very few residents')
        # where is a person's *home* (the place_of a matter that is a person)? kind distribution
        from engine.season.state.containment import home_of
        ho = home_of(w)
        kinds = collections.Counter(w.rungs[r].kind for p, r in ho.items() if p in w.persons and r in w.rungs)
        LOG.w('result', section='A', check='home_rung_kind_of_persons', seed=seed, kinds=dict(kinds),
              note='the venue a case about a person is heard at is place_of(person); L(f,v) is meant for a territory')
    LOG.w('summary_section', section='A')


# ---------------------------------------------------------------------------------------------
# C -- authority grouping
# ---------------------------------------------------------------------------------------------
BY_FACTION = {"Crown": "polity", "Hafenmark": "polity", "Varfell": "polity", "Church of Solmund": "church"}


@guarded
def sec_C():
    import yaml
    from engine.season.data.rosters import office_faction
    build_realm, world_q, faction_prop_id, FACTION_BY_PROP = real()
    d = yaml.safe_load(open(os.path.join(ROOT, 'engine/season/offices.yaml')))
    seats = d['seats']
    LOG.w('plan', section='C', what='recompute authority.by_faction over offices.yaml seats via office_faction(body, faction); compare 19/7/5 and the sub-counts; cross-check against build_realm worlds; determine holders and scope')
    LOG.w('claim', where='P3 3.1 table', quote='polity 19: Crown 11 (incl. Inner Circle 2, Ministries 1), Hafenmark 4, Varfell 4; church 7: Holy See 1, four Cardinals, Senior Inquisitor, Archbishop\'s Representative; parties only 5: Guild 1, Lions\' Table 1, Riskbreakers 2, Restoration 1')
    rows = []
    for s in seats:
        f = office_faction(s.get('body'), s.get('faction'))
        rows.append((s['id'], s['post'], s.get('body'), f))
    cnt_f = collections.Counter(r[3] for r in rows)
    auth = collections.Counter(BY_FACTION.get(r[3], 'parties') for r in rows)
    LOG.w('result', section='C', check='counts', n_seats=len(seats), by_faction=dict(cnt_f), by_authority=dict(auth))
    exp = {'polity': 19, 'church': 7, 'parties': 5}
    for a, c in exp.items():
        (LOG.w('result', section='C', check='authority_count', authority=a, claimed=c, got=auth.get(a, 0), verdict='HELD')
         if auth.get(a, 0) == c else
         LOG.w('fail', section='C', check='authority_count', authority=a, claimed=c, got=auth.get(a, 0), proposal_said=f'{a} {c}'))
    expf = {'Crown': 11, 'Hafenmark': 4, 'Varfell': 4, 'Church of Solmund': 7}
    for f, c in expf.items():
        (LOG.w('result', section='C', check='faction_count', faction=f, claimed=c, got=cnt_f.get(f, 0), verdict='HELD')
         if cnt_f.get(f, 0) == c else LOG.w('fail', section='C', check='faction_count', faction=f, claimed=c, got=cnt_f.get(f, 0)))
    crown = [r for r in rows if r[3] == 'Crown']
    LOG.w('result', section='C', check='crown_sub_bodies', bodies=dict(collections.Counter(r[2] for r in crown)),
          claimed='Inner Circle 2, Ministries 1', parties_only_posts=[(r[1], r[3]) for r in rows if BY_FACTION.get(r[3]) is None])
    # foreign seats
    fs = d.get('foreign_seats') or []
    LOG.w('result', section='C', check='foreign_seats', n=len(fs), sample=[(x.get('id'), x.get('post'), x.get('faction'), x.get('body')) for x in fs][:6],
          note='not counted in the 31 by the proposal')
    # realm builds
    for seed in (0, 1, 2):
        w = build_realm(seed)
        offs = {oid: o for oid, o in w.offices.items()}
        auth_w = collections.Counter(BY_FACTION.get(o.faction, 'parties') for o in offs.values())
        det = []
        for t in w.tenures:
            if t.kind == 'hold' and t.live and 'determine' in t.granted_acts and t.object in offs:
                o = offs[t.object]
                det.append((o.post, o.faction, BY_FACTION.get(o.faction, 'parties'), o.rung, o.scope_rung, t.subject))
        LOG.w('result', section='C', check='realm_offices', seed=seed, n_offices=len(offs), by_authority=dict(auth_w),
              extra_vs_yaml=sorted(set(offs) - {s['id'] for s in seats}), determine_holders=det)
        if seed == 0:
            church_det = [x for x in det if x[2] == 'church']
            LOG.w('result', section='C', check='church_determine_scope', church_det=church_det,
                  claimed='Confessor, Cardinal of Justice, Senior Inquisitor: all scoped at T9',
                  verdict='HELD' if len(church_det) == 3 and all(x[4] == 'terr_T9' for x in church_det) else 'BROKE')
            poldet = [x[0] for x in det if x[2] == 'polity']
            LOG.w('result', section='C', check='polity_determine', polity_det=poldet,
                  claimed='King, Queen (realm scope); Senior Jarl, Skald-Chief (Varfell)',
                  hafenmark_has_determine=any(x[1] == 'Hafenmark' for x in det), claimed_hafenmark_none=True)
            other = [x for x in det if x[2] == 'parties']
            LOG.w('result', section='C', check='parties_only_determine', seats=other,
                  claimed='none authored; the unauthored 32nd seat (off_npc_084, a guild leader) holds it with scope_rung None')
    LOG.w('summary_section', section='C')



# ---------------------------------------------------------------------------------------------
# shared: a fold on a REAL world
# ---------------------------------------------------------------------------------------------
class Fold:
    def __init__(self, seed=0, fixtures=None):
        from engine.season.harness.populated import build_realm
        from engine.season.loop.driver import SeasonDriver, mint_token
        from engine.season.data.matrix import WriteClass
        self.mint_token, self.WriteClass = mint_token, WriteClass
        self.w = build_realm(seed)
        if fixtures:
            for k, v in fixtures.items():
                self.w.fixtures = self.w.fixtures.sweep(k, v)
        self.d = SeasonDriver(self.w)

    def __call__(self, *acts):
        out = self.d.resolve(self.mint_token(self.w, self.WriteClass.ACTS), list(acts),
                             contest_max_depth=self.w.fixtures.get("contest_max_depth"))
        self.w.log.extend(out)
        return out

    def holder(self, post_substr=None, oid=None):
        for o_id, o in self.w.offices.items():
            if (oid and o_id == oid) or (post_substr and o.post.startswith(post_substr)):
                for t in self.w.tenures:
                    if t.kind == 'hold' and t.live and t.object == o_id:
                        return o_id, t.subject
        return None, None

    def people_in(self, terr, exclude=()):
        from engine.season.queries import world_q
        from engine.season.state.containment import home_of
        ho = home_of(self.w)
        out = []
        for p, r in ho.items():
            if p in self.w.persons and p not in exclude and territory_of(self.w, world_q, r) == terr:
                out.append(p)
        return sorted(out)


def act(i, actor, verb, via, **payload):
    from engine.season.state.carriers import Act
    return Act(id=i, actor=actor, verb=verb, via=via, payload=payload)


@guarded
def sec_B():
    LOG.w('plan', section='B', what='open_case from each church seat holder (and the King, as control) on real build_realm(0) against every resident of T1, T4, T9; then the same with Q1 emulated (church determining seats re-anchored to the realm)')
    LOG.w('claim', where='P3 3.4 pt 2 / worked example A (1)', quote='Q1 asks to give the church\'s three determining seats a realm `scope:` anchor in offices.yaml while their `rung` stays T9: the church may then judge anywhere and execute only where its own arm reaches ... (1) Forum gate: church row, church seat. Today it fails (scope T9); under Q1 it passes.')
    LOG.w('claim', where='comparison 4 (assessors)', quote='Case-opening reads purview from Office.rung (T9 for church seats), not scope_rung, so its scenarios 2 and 3 and its worked example A break before Q1 can help')
    from engine.season.queries import world_q
    from engine.season.state import gate
    variants = {'as_built': None, 'Q1_scope_only': 'scope', 'Q1_scope_and_rung': 'both'}
    for vname, mode in variants.items():
        f = Fold(0)
        w = f.w
        realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
        seats = {}
        for lab, post in (('Senior Inquisitor', 'Senior Inquisitor'), ('Confessor', 'Confessor'), ('Cardinal Justice', 'Cardinal Justice'), ('King', 'King'), ('Archbishop Rep', "Archbishop's Rep")):
            seats[lab] = f.holder(post)
        if mode:
            for lab in ('Senior Inquisitor', 'Confessor', 'Cardinal Justice'):
                o = w.offices[seats[lab][0]]
                try:
                    o.scope_rung = realm
                    if mode == 'both':
                        o.rung = realm
                except Exception as e:
                    LOG.w('blocked', section='B', variant=vname, why=f'cannot patch Office: {type(e).__name__}: {e}')
        for lab, (oid, pid) in seats.items():
            if oid is None:
                LOG.w('blocked', section='B', seat=lab, why='no holder found'); continue
            for T in ('terr_T9', 'terr_T1', 'terr_T4'):
                targets = f.people_in(T, exclude=(pid,))
                opened = unauth = other = 0
                kinds = collections.Counter()
                for i, tgt in enumerate(targets):
                    out = f(act(f'b_{vname}_{lab}_{T}_{i}', pid, 'open_case', oid, subject=tgt))
                    k = [e.kind for e in out]
                    kinds.update(k)
                    opened += 'case.opened' in k
                    unauth += 'case.unauthorized' in k
                    other += not ('case.opened' in k or 'case.unauthorized' in k)
                n = len(targets)
                # the bench for the same territory under judging_set (scope_rung) and purview (rung)
                bench = world_q.judging_set(w, T)
                reaches = gate.purview_reaches(w, w.offices[oid], T)
                LOG.w('trial', section='B', variant=vname, seat=lab, holder=pid, territory=T, n=n, opened=opened,
                      opened_wilson95=wilson(opened, n), unauthorized=unauth, other=other, event_kinds=dict(kinds),
                      purview_reaches_territory=reaches, sits_over_territory=gate.sits_over(w, w.offices[oid], T),
                      in_judging_set=pid in bench, office_rung=w.offices[oid].rung, office_scope_rung=w.offices[oid].scope_rung)
        # verdicts (computed from the trial lines above, restated)
    LOG.w('result', section='B', note='see trial lines: verdicts are assigned in the report from them', falsifier='a church seat re-anchored to the realm on scope_rung alone would show opened > 0 in T1/T4; if it did, the assessors were wrong')


@guarded
def sec_B2():
    """B again, with a FRESH world per (variant, seat): the first B run shared one world per variant, so a case
    opened by an earlier seat docketed its targets and the later seats' `case.refused` was the docket's, not the seat's."""
    LOG.w('fail', section='B', what='my first B harness shared one world per variant across seats: the Confessor, Cardinal Justice and King rows at T9 (and every row of the Q1_scope_and_rung variant after the first seat) read `case.refused` because the Senior Inquisitor had already docketed those targets (`effects_information.py:341`). Order-confounded; B2 is the corrected attempt, one fresh world per (variant, seat). The B lines are kept, not deleted.')
    from engine.season.queries import world_q
    from engine.season.state import gate
    for vname, mode in {'as_built': None, 'Q1_scope_only': 'scope', 'Q1_scope_and_rung': 'both'}.items():
        for lab, post in (('Senior Inquisitor', 'Senior Inquisitor'), ('Confessor', 'Confessor'), ('Cardinal Justice', 'Cardinal Justice'), ('King', 'King')):
            f = Fold(0)
            w = f.w
            realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
            oid, pid = f.holder(post)
            if mode and lab != 'King':
                w.offices[oid].scope_rung = realm
                if mode == 'both':
                    w.offices[oid].rung = realm
            for T in ('terr_T9', 'terr_T1', 'terr_T4'):
                targets = f.people_in(T, exclude=(pid,))
                kinds = collections.Counter()
                opened = 0
                for i, tgt in enumerate(targets):
                    out = f(act(f'b2_{vname}_{lab}_{T}_{i}', pid, 'open_case', oid, subject=tgt))
                    kinds.update(e.kind for e in out)
                    opened += any(e.kind == 'case.opened' for e in out)
                n = len(targets)
                LOG.w('trial', section='B2', variant=vname, seat=lab, holder=pid, territory=T, n=n, opened=opened,
                      opened_wilson95=wilson(opened, n), event_kinds=dict(kinds),
                      purview_reaches=gate.purview_reaches(w, w.offices[oid], T), sits_over=gate.sits_over(w, w.offices[oid], T),
                      office_rung=w.offices[oid].rung, office_scope_rung=w.offices[oid].scope_rung)
    LOG.w('result', section='B2', falsifier='scope-only re-anchoring would show opened > 0 at T1/T4 if open_case read scope_rung; control: King opens at T1/T4 and the seat at T9 opens')


ARGS = None
ACT_VERBS = ('open_case', 'petition', 'carry', 'determine', 'arrest', 'pardon', 'release', 'evade / defy', 'comply', 'convene',
             'commit', 'argue', 'tell', 'dispatch', 'revoke', 'confer', 'issue')


def _royal_set(w):
    out = set()
    for t in w.tenures:
        if t.kind == 'hold' and t.live:
            o = w.offices.get(t.object)
            if o is not None and o.faction == 'Crown' and o.rung is not None and w.rungs.get(o.rung) is not None and w.rungs[o.rung].kind == 'realm':
                out.add(t.subject)
    return out


def _tee_resolve(d, sink):
    orig = d.resolve

    def resolve(token, acts, *a, **kw):
        out = orig(token, acts, *a, **kw)
        sink.append((list(acts), list(out)))
        return out
    d.resolve = resolve


@guarded
def sec_G():
    """Real seasons with the shipped chooser: what is attempted and executed for the verbs P3 builds on, and how often a
    royal person (a live holder of a realm-rung Crown seat) is a party to a matter. Stops on first of crash, a season with
    no new event, or --budget-s. One seed per process (ARGS.seed)."""
    from engine.season.harness.populated import build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P
    seed = ARGS.seed
    LOG.w('plan', section='G', seed=seed, what='tick build_realm(seed) with the shipped chooser; tee every resolve() call; per season count attempted acts and emitted kinds for open_case/petition/carry/determine/arrest/pardon/evade-defy; royal involvement per matter')
    LOG.w('claim', where='P3 7 weakest 1 / 9.2', quote='`determine` rolled 0 times and `arrest` was attempted 0 times (PROBE §3)')
    LOG.w('claim', where='P3 3.6 / 8 Q3', quote='R-34: "if a royal person is involved" ... P3\'s default is a party who holds a realm-rung Crown seat')
    w = build_realm(seed)
    d = SeasonDriver(w)
    sink = []
    _tee_resolve(d, sink)
    mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
    royal0 = _royal_set(w)
    LOG.w('result', section='G', seed=seed, royal_persons=sorted(royal0), n_persons=len(w.persons))
    t0 = time.time()
    deadline = t0 + ARGS.budget_s
    tot_att, tot_ev = collections.Counter(), collections.Counter()
    matters = []        # (season, verb, subject, actor, to, royal_subject, royal_actor, royal_to)
    s = 0
    stop = None
    prev = len(w.log)
    while True:
        if time.time() >= deadline:
            stop = 'budget'; break
        if ARGS.max_seasons and s >= ARGS.max_seasons:
            stop = 'ceiling'; break
        sink.clear()
        ts = time.time()
        d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
        secs = time.time() - ts
        royal = _royal_set(w) | royal0
        att, ev = collections.Counter(), collections.Counter()
        acts_by_id = {}
        for acts, out in sink:
            for a in acts:
                acts_by_id[a.id] = a
                att[a.verb] += 1
            for e in out:
                ev[e.kind] += 1
        for acts, out in sink:
            for e in out:
                if e.kind in ('case.opened', 'petition.filed', 'petition.carried', 'matter.determined', 'arrest.made', 'arrest.resisted'):
                    for c in e.causes:
                        a = acts_by_id.get(c)
                        if a is None:
                            continue
                        pl = a.payload if isinstance(a.payload, dict) else {}
                        subj, to = pl.get('subject'), pl.get('to')
                        matters.append((s, e.kind, subj, a.actor, to, subj in royal, a.actor in royal, to in royal, a.via))
        tot_att.update(att); tot_ev.update(ev)
        watched = {k: att.get(k, 0) for k in ACT_VERBS if att.get(k, 0)}
        LOG.w('batch', section='G', seed=seed, season=s + 1, wall_s=round(secs, 2), events_new=len(w.log) - prev,
              attempted=watched, emitted={k: v for k, v in ev.items() if any(x in k for x in ('case', 'petition', 'matter', 'determine', 'arrest', 'detention', 'ban', 'pardon', 'compliance', 'carried'))},
              docket=len(w.docket), docket_empty=sum(1 for x in w.docket if x.get('matter') is None),
              docket_named_arrangement=sum(1 for x in w.docket if x.get('arrangement')))
        if len(w.log) == prev:
            stop = 'quiet'; s += 1; break
        prev = len(w.log)
        s += 1
    n_m = len(matters)
    kinds = collections.Counter(m[1] for m in matters)
    rs = sum(1 for m in matters if m[5]); ra = sum(1 for m in matters if m[6]); rt = sum(1 for m in matters if m[7])
    anyr = sum(1 for m in matters if m[5] or m[6] or m[7])
    LOG.w('result', section='G', seed=seed, seasons=s, stop=stop, wall_s=round(time.time() - t0, 1), attempted_total=dict(tot_att),
          emitted_watch={k: v for k, v in tot_ev.items() if any(x in k for x in ('case', 'petition', 'matter', 'determine', 'arrest', 'detention', 'ban', 'pardon', 'compliance', 'carried'))},
          executed_matter_events=n_m, by_kind=dict(kinds),
          royal_is_matter_subject=rs, royal_is_actor=ra, royal_is_addressee=rt, any_royal=anyr,
          any_royal_rate=round(anyr / n_m, 4) if n_m else None, any_royal_wilson95=wilson(anyr, n_m),
          arrest_attempted=tot_att.get('arrest', 0), evade_defy_attempted=tot_att.get('evade / defy', 0), determine_attempted=tot_att.get('determine', 0),
          determine_executed=tot_ev.get('matter.determined', 0) + tot_ev.get('matter.undetermined', 0))
    LOG.w('result', section='G', seed=seed, matters_sample=matters[:60])
    LOG.w('summary_section', section='G', seed=seed, stop=stop)


ROW_AUTH = {'inquisition_hearing': 'church', 'excommunication_deliberation': 'church', 'tribunal': 'polity', 'legal_trial': 'polity',
            'arbitration': 'parties', 'interrogation': 'polity', 'parliamentary_debate': 'polity', 'council_of_state': 'polity'}


def seat_authority(w, seat_id):
    o = w.offices.get(seat_id)
    return BY_FACTION.get(o.faction, 'parties') if o is not None else None


class Patch:
    """Install MODEL versions of judging_set / may_determine at every binding site (module-global lookups), restore on exit."""
    def __init__(self, bench_filter=False, gate_filter=False, gate_reads_docket=True):
        self.bf, self.gf, self.grd = bench_filter, gate_filter, gate_reads_docket
        self.gate_calls = collections.Counter()

    def __enter__(self):
        import engine.season.state.gate as G
        import engine.season.queries.world_q as WQ
        import engine.season.loop.effects_information as EI
        self.mods = (G, WQ, EI)
        self.orig_md, self.orig_js = G.may_determine, WQ.judging_set
        me = self

        def row_auth(w, party):
            rows = WQ.docketed_under(w, party) if party else set()
            rows = {r for r in rows if r}
            return ROW_AUTH.get(next(iter(rows))) if rows else None

        def md(w, actor, via, party):
            ok = me.orig_md(w, actor, via, party)
            if not ok or not me.gf:
                return ok
            ra = row_auth(w, party)
            me.gate_calls['row_visible' if ra else 'row_not_visible'] += 1
            return ok if ra is None else (seat_authority(w, via) == ra)

        def js(w, venue, matter=None):
            base = me.orig_js(w, venue, matter)
            if not me.bf or matter is None:
                return base
            ra = row_auth(w, matter)
            if ra is None:
                return base
            seats = []
            for t in w.tenures:
                if t.kind == 'hold' and t.live and 'determine' in t.granted_acts and t.subject in base and seat_authority(w, t.object) == ra:
                    o = w.offices.get(t.object)
                    if o is not None and G.sits_over(w, o, venue):
                        seats.append(t.subject)
            return seats
        G.may_determine = md; EI.may_determine = md; WQ.may_determine = md; WQ.judging_set = js
        return self

    def __exit__(self, *a):
        G, WQ, EI = self.mods
        G.may_determine = self.orig_md; EI.may_determine = self.orig_md; WQ.may_determine = self.orig_md; WQ.judging_set = self.orig_js


@guarded
def sec_D():
    LOG.w('plan', section='D', what='MODEL of P3 3.4(1): authority-filtered bench vs the gate\'s may_determine. Arms: M0 live; M1 bench filtered only (the proposal as the assessors read it); M2 gate filtered only; M3 both, the gate reading the docketed row. Real fold, real realm, hand-built open_case under inquisition_hearing (church) with a King determine; quorum swept')
    LOG.w('claim', where='P3 3.4 pt 1 + 5 ("state/gate.py ... may_determine reads the row\'s authority")', quote='judging_set(w, venue, authority, assessors) lists seat-holders whose authority_of is the row\'s authority or one of its assessors ... may_determine reads the row\'s authority')
    LOG.w('claim', where='comparison 4', quote='judging_set and the gate\'s may_determine must be one test. Filtering only the bench lets the gate admit a judge the bench excludes (gate.py:735-737,251-254)')
    from engine.season.queries import world_q
    arms = {'M0_live': dict(), 'M1_bench_only': dict(bench_filter=True), 'M2_gate_only': dict(gate_filter=True), 'M3_both': dict(bench_filter=True, gate_filter=True)}
    for quorum in (1, 3, 4):
        for arm, kw in arms.items():
            for judge_lab, judge_post in (('King', 'King'), ('Confessor', 'Confessor')):
                with Patch(**kw) as P:
                    f = Fold(0, fixtures={'pool_default': 30, 'bench_quorum': quorum})
                    w = f.w
                    soid, spid = f.holder('Senior Inquisitor')
                    joid, jpid = f.holder(judge_post)
                    tgt = [p for p in f.people_in('terr_T9', exclude=(spid, jpid))][0]
                    o = f(act('d_open', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
                    venue = world_q.place_of(w, tgt)
                    bench_ids = world_q.judging_set(w, venue, tgt)
                    size_read = len(set(bench_ids))
                    gate_ok = P.orig_md(w, jpid, joid, tgt)
                    md_now = __import__('engine.season.state.gate', fromlist=['x']).may_determine(w, jpid, joid, tgt)
                    out = f(act('d_det', jpid, 'determine', joid, subject=tgt))
                    kinds = [e.kind for e in out]
                    LOG.w('trial', section='D', arm=arm, quorum=quorum, judge=judge_lab, judge_seat_authority=seat_authority(w, joid),
                          row='inquisition_hearing(church)', open_kinds=[e.kind for e in o], bench_size_read=size_read,
                          judge_in_bench=jpid in bench_ids, gate_unfiltered_admits=gate_ok, gate_arm_admits=md_now,
                          determine_events=kinds, executed=any(k.startswith('matter.') for k in kinds),
                          gate_calls=dict(P.gate_calls), n=1,
                          note='deterministic world; pool_default 30 so a success is near-certain; n=1 per cell by construction')
    LOG.w('result', section='D', falsifier='if filtering the bench alone kept the King off a church row the M1 King cell would read executed=False; the control is M0 (live), and M3 shows whether a both-sides filter is even implementable (gate_calls row_visible vs row_not_visible)')


def p_meets(ob, pool, sigma=0.0):
    from engine.dice_engine.sigma_leverage import p_success
    return p_success(ob, pool, sigma)


@guarded
def sec_E():
    """PAYOFF MODELS on real roll probabilities (sigma_leverage.p_success). MODEL of P3's mechanism, not code."""
    import itertools
    from engine.dice_engine.sigma_leverage import roll_net, net_boost
    LOG.w('plan', section='E', what='(E0) reproduce worked-example-A arithmetic; (E1) accused: appear vs defy, with and without a chooser that serves warrants; (E2) forum contest normal form; (E3) forum shopping by L; MC cross-check of the closed form against the live integer roll')
    LOG.w('claim', where='P3 4 worked example A (3)', quote="the inquisitor's weight 2 enters his dice at x .37 (0.74D) where in T9 it would be x .78 (1.56D); at the 5D reference that 0.82D is worth about 7 points of \"meets\" (ARM D.1: +1 die moves .390 to .480)")
    LOG.w('claim', where='P3 3.5', quote='a defiant party\'s custody disposal is always a warrant ... The draw is not changed by defiance.')
    LOG.w('claim', where='comparison 7 (assessors)', quote='`defy` leaves the draw unchanged and a warrant\'s cost decays toward zero because `arrest` was attempted 0 times')
    # E0
    ref = p_meets(2.5, 5)
    plus1 = p_meets(2.5, 6)
    LOG.w('result', section='E', check='ARM_D1_reference', p_5D_vs_Ob2_5=round(ref, 4), p_6D=round(plus1, 4), claimed=[0.390, 0.480],
          verdict='HELD' if abs(ref - .390) < .002 and abs(plus1 - .480) < .002 else 'BROKE')
    for b in (2, 5, 12, 30):
        for ob in (2.0, 2.5, b / 2.0):
            lo = p_meets(ob, b + 2 * 0.37); hi = p_meets(ob, b + 2 * 0.78); ctl = p_meets(ob, b + 2 * 1.0); none = p_meets(ob, b)
            LOG.w('result', section='E', check='worked_example_A_delta', pool=b, ob=ob, p_T2_L37=round(lo, 4), p_T9_L78=round(hi, 4), delta_pts=round(100 * (hi - lo), 2),
                  p_L1_control=round(ctl, 4), p_weight_off=round(none, 4), claimed_delta_pts_at_5D=7 if b == 5 else None)
    # MC cross-check of the closed form vs the live (integer-pool) roll: this model uses fractional pools that the live roll rounds
    rng = random.Random(1)
    for pool in (2, 5, 12):
        n = 20000
        k = sum(1 for _ in range(n) if roll_net(pool, rng=rng) + net_boost(0.0, pool) >= 2.0)
        LOG.w('trial', section='E', check='closed_form_vs_live_integer_roll', pool=pool, ob=2.0, n=n, successes=k, rate=round(k / n, 4), wilson95=wilson(k, n),
              closed_form=round(p_meets(2.0, pool), 4), note='discrete live roll vs continuous closed form; differences here are the armature\'s continuous-pool change, not P3\'s')
    # E1: accused chooses appear / defy. cost = P(sentence) * [executes]. executes(appear)=1; executes(defy)=q_serve * p_arrest (warrant branch)
    rows = []
    for b, L, q in itertools.product((2, 5, 12), (0.37, 0.78, 1.0), (0.0, 0.25, 0.5, 1.0)):
        ps = p_meets(2.0, b + 2 * L)                  # church seat's determine pool = base + weight 2 x L; Ob 2 = unopposed default
        parrest = p_meets(2.0, b)                     # polity dispatch-holder's arrest: base pool, Ob 2
        cost_appear = ps
        cost_defy = ps * q * parrest
        dom = 'defy_strictly_dominates' if cost_defy < cost_appear - 1e-12 else ('weakly' if cost_defy <= cost_appear else 'appear_dominates')
        rows.append((b, L, q, round(ps, 4), round(parrest, 4), round(cost_appear, 4), round(cost_defy, 4), dom))
        LOG.w('result', section='E', check='accused_appear_vs_defy', pool=b, L=L, q_warrant_served=q, p_sentence=round(ps, 4), p_arrest=round(parrest, 4),
              cost_appear=round(cost_appear, 4), cost_defy=round(cost_defy, 4), verdict=dom)
    n_strict = sum(1 for r in rows if r[-1] == 'defy_strictly_dominates')
    LOG.w('result', section='E', check='defy_dominance_summary', cells=len(rows), defy_strictly_dominates=n_strict, wilson95=wilson(n_strict, len(rows)),
          cells_where_defy_not_better=[r for r in rows if r[-1] != 'defy_strictly_dominates'],
          reading='defy costs nothing in the draw (P3 3.5); the only cost is the warrant executing. With a defiance penalty absent, defy is weakly dominant at every q; strictly at every q < 1 x p_arrest^-1')
    # a penalty that would restore the choice: how large must a contempt cost be?
    for b, L in itertools.product((2, 5, 12), (0.37, 0.78)):
        ps = p_meets(2.0, b + 2 * L); parrest = p_meets(2.0, b)
        for q in (0.0, 1.0):
            gap = ps - ps * q * parrest
            LOG.w('result', section='E', check='contempt_cost_needed_for_indifference', pool=b, L=L, q=q, contempt_in_custody_units=round(gap, 4))
    # E2: forum contest as a normal form game. Strategies per authority: C_own, C_other, S (silent). forum fixed only if both name the same forum.
    strat = ('C_own', 'C_other', 'S')
    forum_of = {('P', 'C_own'): 'P', ('P', 'C_other'): 'C', ('C', 'C_own'): 'C', ('C', 'C_other'): 'P'}
    payoff = {'own': 1.0, 'impasse': 0.0, 'other': -1.0}      # value of the matter being heard in own / nowhere / other authority's forum
    def outcome(sP, sC):
        fP = forum_of.get(('P', sP)); fC = forum_of.get(('C', sC))
        return fP if (fP and fC and fP == fC) else None
    def pay(who, sP, sC):
        f = outcome(sP, sC)
        return payoff['impasse'] if f is None else (payoff['own'] if f == who else payoff['other'])
    table = {(a, b): (pay('P', a, b), pay('C', a, b)) for a in strat for b in strat}
    def dominated(player):
        res = []
        for x in strat:
            for y in strat:
                if x == y:
                    continue
                if player == 'P':
                    ge = all(table[(y, c)][0] >= table[(x, c)][0] for c in strat); gt = any(table[(y, c)][0] > table[(x, c)][0] for c in strat)
                else:
                    ge = all(table[(r, y)][1] >= table[(r, x)][1] for r in strat); gt = any(table[(r, y)][1] > table[(r, x)][1] for r in strat)
                if ge:
                    res.append((x, 'weakly' if not gt else 'strictly', 'dominated by', y))
        return res
    LOG.w('result', section='E', check='forum_contest_normal_form', payoffs=payoff, table={f'{a}|{b}': v for (a, b), v in table.items()},
          P_dominated=dominated('P'), C_dominated=dominated('C'),
          pure_nash=[(a, b) for a in strat for b in strat if all(table[(x, b)][0] <= table[(a, b)][0] for x in strat) and all(table[(a, y)][1] <= table[(a, b)][1] for y in strat)],
          reading='mutual forum: committing to the other\'s forum is dominated by silence; silence is weakly dominated by committing to your own; (C_own, C_own) is an impasse. Impasse is the equilibrium in every non-royal matter')
    # E3: with a royal party the polity bench decides: authority-shopping. Which forum a rational opener picks = argmax of weight x L x pool effect
    for terr, Lc, Lp in (('T9', .774, .766), ('T1', .53, .74), ('T2', .367, .68), ('T4', .379, .57), ('T14', .569, .743)):
        for b in (2, 5, 12):
            pc = p_meets(2.0, b + 2 * Lc); pp = p_meets(2.0, b + 3 * Lp)
            LOG.w('result', section='E', check='forum_shopping_argmax', territory=terr, pool=b, p_church_row=round(pc, 4), p_polity_row_w3=round(pp, 4),
                  best_forum_for_accuser='polity' if pp > pc else 'church', margin_pts=round(100 * abs(pp - pc), 2))
    LOG.w('summary_section', section='E')


def ev_kinds(out):
    return [e.kind for e in out]


@guarded
def sec_F():
    """Custody, warrants, defy, appeal and pardon, tried on real build_realm(0) worlds with hand-built acts through the real fold."""
    from engine.season.queries import world_q
    from engine.season.state.carriers import Claim, Tenure
    LOG.w('plan', section='F', what='F1 church determine with a detain row at T9 and at T1 (Q1 scope-only): does custody open with no arm? F2 church-issued warrant -> give -> King arrest. F3 pardon by a crown seat on a church ban. F4 re-open after a ban (the wedge). F5 evade/defy on the open_case case file (the "summons")')
    LOG.w('claim', where='P3 3.5', quote='A disposal that needs custody (detain) executes directly only where the determining seat\'s purview reaches the party ... Otherwise _disposal opens a warrant ... the edge opens only when some dispatch holder whose purview reaches the party performs arrest')
    LOG.w('claim', where='P3 3.5', quote='open_case\'s Record is the summons; evade / defy ... gains its reader: a defiant party\'s custody disposal is always a warrant')
    LOG.w('claim', where='P3 3.7', quote='This needs a new closure basis: pardon closes only edges whose object is the exercised seat (effects_governance.py:327-352), so a crown seat cannot today end a church ban. ... a re-opening under the same authority is refused with a named reason instead of wedging as it does today')
    # F1
    for variant in ('as_built_T9', 'Q1_scope_only_T1'):
        f = Fold(0, fixtures={'pool_default': 30})
        w = f.w
        realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
        coid, copid = f.holder('Confessor')
        koid, kpid = f.holder('King')
        T = 'terr_T9' if variant.endswith('T9') else 'terr_T1'
        if variant.startswith('Q1'):
            w.offices[coid].scope_rung = realm
        tgt = f.people_in(T, exclude=(copid, kpid))[0]
        # docket by the King for T1 (the church cannot open there); by the Confessor at T9
        opener = (coid, copid) if T == 'terr_T9' else (koid, kpid)
        o = f(act('f1_open', opener[1], 'open_case', opener[0], subject=tgt, arrangement='legal_trial'))
        d = f(act('f1_det', copid, 'determine', coid, subject=tgt))
        edges = [(t.kind, t.object, t.degree) for t in w.tenures if t.subject == tgt and t.kind in ('detain', 'ban') and t.live]
        from engine.season.state.gate import purview_reaches
        LOG.w('trial', section='F', test='F1_church_custody', variant=variant, open=ev_kinds(o), determine=ev_kinds(d), edges=edges,
              church_purview_reaches_party=purview_reaches(w, w.offices[coid], world_q.place_of(w, tgt)), n=1,
              reading='a detain edge on the CHURCH seat opened directly with no arrest/warrant step' if any(e[0] == 'detain' for e in edges) else 'no custody opened')
    # F2: warrant chain at T1 under Q1 scope-only, Confessor issues, hand-plants hold for the King, King arrests
    f = Fold(0, fixtures={'pool_default': 30})
    w = f.w
    realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
    coid, copid = f.holder('Confessor'); koid, kpid = f.holder('King')
    w.offices[coid].scope_rung = realm
    tgt = f.people_in('terr_T1', exclude=(copid, kpid))[0]
    w.persons[copid].ledger.append(Claim("c_knows_t", copid, tgt, "exists:Person", 1, 0, "firsthand", 100, "own"))
    w.persons[copid].ledger.append(Claim("c_knows_k", copid, kpid, "exists:Person", 1, 0, "firsthand", 100, "own"))
    out = f(act('f2_issue', copid, 'issue', coid, subject=tgt, to=kpid))
    LOG.w('trial', section='F', test='F2_issue_warrant', events=ev_kinds(out), n=1)
    recs = [rid for rid, r in w.records.items() if r.kind == 'dispensation']
    LOG.w('result', section='F', test='F2_records', dispensations=recs)
    if not recs:
        LOG.w('blocked', section='F', test='F2', why='church issue of a warrant produced no dispensation Record (see F2_issue_warrant events); first blocker is the issue precondition at the fold', path='verb_table.yaml issue row')
    else:
        rid = recs[0]
        g = f(act('f2_give', copid, 'give', coid, subject=rid, to=kpid))
        LOG.w('trial', section='F', test='F2_give_to_King', events=ev_kinds(g), n=1,
              note='give requires the receiver to be WITH the giver (relation `with`); Confessor lives at T9, the King elsewhere')
        if not any(t.kind == 'hold' and t.live and t.subject == kpid and t.object == rid for t in w.tenures):
            w.tenures.append(Tenure(f"plant_{rid}", kpid, rid, "hold", since=w.tick)) if False else w.add_tenure(Tenure(f"plant_{rid}", kpid, rid, "hold", since=w.tick))
            LOG.w('unverified', section='F', test='F2', what='the King\'s hold on the church warrant was hand-planted (give was refused: not co-located); the arrest step below is real but the delivery step is not exercised')
        ar = f(act('f2_arrest', kpid, 'arrest', koid, subject=tgt))
        edges = [(t.kind, t.object) for t in w.tenures if t.subject == tgt and t.kind == 'detain' and t.live]
        LOG.w('trial', section='F', test='F2_King_arrest', events=ev_kinds(ar), edges=edges, n=1,
              reading='custody edge opened on the issuing CHURCH seat by a polity hand' if edges else 'no custody edge')
    # F3 pardon: church ban at T9, then King pardon
    f = Fold(0, fixtures={'pool_default': 30})
    w = f.w
    soid, spid = f.holder('Senior Inquisitor'); koid, kpid = f.holder('King')
    tgt = f.people_in('terr_T9', exclude=(spid, kpid))[0]
    o = f(act('f3_open', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
    d = f(act('f3_det', spid, 'determine', soid, subject=tgt))
    ban = [(t.object, t.degree) for t in w.tenures if t.subject == tgt and t.kind == 'ban' and t.live]
    p1 = f(act('f3_pardon_king', kpid, 'pardon', koid, subject=tgt))
    still = [(t.object) for t in w.tenures if t.subject == tgt and t.kind == 'ban' and t.live]
    p2 = f(act('f3_pardon_inq', spid, 'pardon', soid, subject=tgt))
    gone = [(t.object) for t in w.tenures if t.subject == tgt and t.kind == 'ban' and t.live]
    LOG.w('trial', section='F', test='F3_pardon', open=ev_kinds(o), determine=ev_kinds(d), ban_edges=ban, king_pardon=ev_kinds(p1), ban_after_king=still,
          inquisitor_pardon=ev_kinds(p2), ban_after_inquisitor=gone, n=1,
          reading='a crown seat cannot close a church ban (pardon.refused, edge stays); the issuing seat can' if still and not gone else 'unexpected')
    # F4 wedge: re-open after the ban
    o2 = f(act('f4_reopen', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
    d2 = f(act('f4_det2', spid, 'determine', soid, subject=tgt))
    stuck = [x for x in w.docket if x.get('matter') == tgt]
    d3 = f(act('f4_det3', spid, 'determine', soid, subject=tgt))
    o3 = f(act('f4_reopen2', kpid, 'open_case', koid, subject=tgt, arrangement='tribunal'))
    LOG.w('trial', section='F', test='F4_reopen_wedge', reopen=ev_kinds(o2), determine_again=ev_kinds(d2), determine_third=ev_kinds(d3), docket_items_for_party=len(stuck),
          second_authority_open_on_docketed=ev_kinds(o3), n=1,
          reading='baseline today: re-open executes, determine declines, item stays docketed (the wedge P3 promises to refuse); a second authority\'s open_case on the docketed matter is refused at effects_information.py:341')
    # F5 evade / defy on the case file
    f = Fold(0)
    w = f.w
    soid, spid = f.holder('Senior Inquisitor')
    tgt = f.people_in('terr_T9', exclude=(spid,))[0]
    before = set(w.records)
    o = f(act('f5_open', spid, 'open_case', soid, subject=tgt))
    new = [r for r in w.records if r not in before]
    kinds = [(r, w.records[r].kind) for r in new]
    holders = {r: [t.subject for t in w.tenures if t.kind == 'hold' and t.live and t.object == r] for r in new}
    dfy = f(act('f5_defy', tgt, 'evade / defy', None, subject=new[0])) if new else []
    LOG.w('trial', section='F', test='F5_defy_on_case_file', open=ev_kinds(o), new_records=kinds, holders=holders, party_is_holder=any(tgt in v for v in holders.values()),
          defy_events=ev_kinds(dfy), n=1,
          reading='the case file is a kind-text Record held by the opener, not the party; evade/defy forms only on a held dispensation (writ) and its precondition reads `existence kind dispensation`')
    LOG.w('summary_section', section='F')


@guarded
def sec_F2():
    """F again, correcting two of my own first-attempt flaws: (1) F4 pardoned the ban in F3 first, so the 're-open' succeeded and did
    not reproduce the wedge, and the 'second authority' opened on a matter no longer docketed; (2) F2's issue was refused and I did not
    ask why. Here: F4b wedge with a LIVE ban; F4c two authorities on one docketed matter; F2b who could receive a church warrant."""
    LOG.w('fail', section='F', what='F4 as first written is not the wedge test: F3 had pardoned the ban, so the re-open and second determine both executed (determine_again = matter.determined) and the docket was empty when the second authority tried to open. F2 stopped at issue.unauthorized without finding the reason. F2 section (below) corrects both; the F lines are kept.')
    from engine.season.queries import world_q
    from engine.season.state.gate import purview_reaches
    # F4b wedge with a live ban
    f = Fold(0, fixtures={'pool_default': 30})
    w = f.w
    soid, spid = f.holder('Senior Inquisitor'); koid, kpid = f.holder('King')
    tgt = f.people_in('terr_T9', exclude=(spid, kpid))[0]
    o1 = f(act('w_open1', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
    d1 = f(act('w_det1', spid, 'determine', soid, subject=tgt))
    o2 = f(act('w_open2', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
    d2 = f(act('w_det2', spid, 'determine', soid, subject=tgt))
    d3 = f(act('w_det3', spid, 'determine', soid, subject=tgt))
    items = [x for x in w.docket if x.get('matter') == tgt]
    LOG.w('trial', section='F2', test='F4b_wedge_live_ban', open1=ev_kinds(o1), det1=ev_kinds(d1), reopen_same_authority=ev_kinds(o2), det2=ev_kinds(d2), det3=ev_kinds(d3),
          docket_items_for_party_after=len(items), n=1,
          reading='WEDGE REPRODUCED: the same-authority re-open executes, determine declines, the item stays docketed' if ev_kinds(o2) == ['case.opened'] and 'determine.refused' in ev_kinds(d2) and items else 'wedge not reproduced')
    # F4c two authorities, one docketed matter
    f = Fold(0)
    w = f.w
    soid, spid = f.holder('Senior Inquisitor'); koid, kpid = f.holder('King')
    tgt = f.people_in('terr_T9', exclude=(spid, kpid))[0]
    a = f(act('c_open_church', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
    b = f(act('c_open_crown', kpid, 'open_case', koid, subject=tgt, arrangement='tribunal'))
    items = [(x.get('arrangement'), x.get('matter')) for x in w.docket if x.get('matter') == tgt]
    LOG.w('trial', section='F2', test='F4c_two_authorities_one_matter', church_open=ev_kinds(a), crown_open=ev_kinds(b), docket_for_party=items, n=1,
          reading='second open refused (effects_information.py:341): there is no forum contest in the code, the second authority just gets case.refused; P3 3.6 needs a new branch here')
    # F2b who could receive a church warrant: polity dispatch-holders and where they live, versus church seats' purview
    f = Fold(0)
    w = f.w
    from engine.season.state.containment import home_of
    ho = home_of(w)
    coid, copid = f.holder('Confessor')
    rows = []
    for t in w.tenures:
        if t.kind == 'hold' and t.live and 'dispatch' in t.granted_acts:
            o = w.offices.get(t.object)
            if o is None:
                continue
            home = ho.get(t.subject)
            rows.append(dict(post=o.post, faction=o.faction, authority=BY_FACTION.get(o.faction, 'parties'), seat_rung=o.rung, home=home,
                             church_confessor_purview_reaches_home=purview_reaches(w, w.offices[coid], home)))
    reach = [r for r in rows if r['authority'] == 'polity' and r['church_confessor_purview_reaches_home']]
    LOG.w('result', section='F2', test='F2b_church_warrant_executors', dispatch_holders=len(rows), polity_dispatch_holders=sum(1 for r in rows if r['authority'] == 'polity'),
          polity_dispatch_holders_the_confessor_may_issue_to=len(reach), detail=rows,
          reading='`issue` needs the issuing seat\'s purview to reach the executor (verb_table issue row): a church seat anchored at T9 can address a warrant only to executors who live inside T9')
    # F2c: chain with Q1_scope_and_rung (church rung = realm) so issue passes; give hand-planted if refused
    from engine.season.state.carriers import Claim
    f = Fold(0, fixtures={'pool_default': 30})
    w = f.w
    realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
    coid, copid = f.holder('Confessor'); koid, kpid = f.holder('King')
    w.offices[coid].scope_rung = realm; w.offices[coid].rung = realm
    tgt = f.people_in('terr_T1', exclude=(copid, kpid))[0]
    for who in (tgt, kpid):
        w.persons[copid].ledger.append(Claim(f"c_knows_{who}", copid, who, "exists:Person", 1, 0, "firsthand", 100, "own"))
    out = f(act('f2c_issue', copid, 'issue', coid, subject=tgt, to=kpid))
    recs = [rid for rid, r in w.records.items() if r.kind == 'dispensation']
    LOG.w('trial', section='F2', test='F2c_issue_with_church_rung_realm', events=ev_kinds(out), dispensations=recs, n=1)
    if recs:
        g = f(act('f2c_give', copid, 'give', coid, subject=recs[0], to=kpid))
        LOG.w('trial', section='F2', test='F2c_give', events=ev_kinds(g), n=1)
        if not any(t.kind == 'hold' and t.live and t.subject == kpid and t.object == recs[0] for t in w.tenures):
            from engine.season.state.carriers import Tenure
            w.add_tenure(Tenure(f"plant_{recs[0]}", kpid, recs[0], "hold", since=w.tick))
            LOG.w('unverified', section='F2', test='F2c', what='King\'s hold on the church warrant hand-planted because give was refused (not co-located); delivery step not exercised')
        ar = f(act('f2c_arrest', kpid, 'arrest', koid, subject=tgt))
        edges = [(t.kind, t.object) for t in w.tenures if t.subject == tgt and t.kind == 'detain' and t.live]
        LOG.w('trial', section='F2', test='F2c_King_arrest', events=ev_kinds(ar), edges=edges, n=1)
    LOG.w('summary_section', section='F2')


@guarded
def sec_S1():
    """Extremes. MODEL (closed form on real p_success) for pool/L/weight/ob; REAL fold for matters-per-party, unknown row, vacancy."""
    import itertools
    from engine.dice_engine.sigma_leverage import p_success
    LOG.w('plan', section='S1', what='pool x L x weight x opinion_full extremes incl NaN/negative/huge; clamp01 behaviour; opinion_full 0; bench of n majority; 1..50 matters per party (real fold); unknown row; missing authority; seat with no holder')
    nan = float('nan')
    # clamp01 with NaN
    LOG.w('result', section='S1', check='clamp01_nan', clamp01_nan=clamp01(nan), clamp01_neg=clamp01(-5), clamp01_big=clamp01(1e9), clamp01_inf=clamp01(float('inf')), clamp01_ninf=clamp01(float('-inf')),
          reading='min(1.0, nan) returns 1.0 in Python: a NaN mean opinion becomes L = 1.0, the MOST favourable value, silently' if clamp01(nan) == 1.0 else 'NaN passes through')
    for of in (0.0, -1.0, 1e-9, 1e9):
        try:
            v = L_from(1.0, of)
            LOG.w('result', section='S1', check='opinion_full_extreme', opinion_full=of, L_at_mean_opinion_plus1=v,
                  reading='negative opinion_full inverts the sign (a friendly territory reads hostile)' if of < 0 else None)
        except Exception as e:
            LOG.w('fail', section='S1', check='opinion_full_extreme', opinion_full=of, type=type(e).__name__, msg=str(e),
                  proposal_said='opinion_full is a sweep [ASSUMPTION; medium; revert 1.0]; no range stated')
    # pool x L x weight grid
    bad = 0; tot = 0; nonfinite = []
    for pool, L, w_, ob in itertools.product((0, 1, 2, 5, 12, 30, -1, nan), (0.0, 0.5, 1.0, nan, -1.0, 2.0), (0, 2, 3, 1e6, -2.0, nan), (0.5, 2.0, 6.0)):
        tot += 1
        try:
            v = p_success(ob, pool + w_ * L)
            if not (v == v) or not (0.0 <= v <= 1.0):
                nonfinite.append((pool, L, w_, ob, v)); bad += 1
        except Exception as e:
            nonfinite.append((pool, L, w_, ob, f'{type(e).__name__}: {e}')); bad += 1
    LOG.w('batch', section='S1', check='pool_L_weight_ob_grid', n=tot, nonfinite_or_raised=bad, wilson95=wilson(bad, tot), sample=nonfinite[:12],
          falsifier='a finite, in-range probability for every cell; any NaN or exception is a failure of the composed operand w x L',
          reading='the operand pool + w*L is unguarded for NaN / negative weight / negative L: NaN poisons p_success; a negative sum is floored to 1D by p_success only')
    for pool in (0, 1, 5, 12, 30):
        row = {f'L={L}': round(p_success(2.5, pool + 2 * L), 4) for L in (0.0, 0.37, 0.78, 1.0)}
        LOG.w('result', section='S1', check='pool_by_L_weight2', pool=pool, ob=2.5, p=row, spread_pts_L0_to_L1=round(100 * (row['L=1.0'] - row['L=0.0']), 2))
    # bench of n: majority of independent member rolls (MODEL: independent identical judges, majority rule, tie = no determination)
    from math import comb
    p1 = p_success(2.0, 5 + 2 * 0.55)
    for n in (1, 2, 7, 21):
        need = n // 2 + 1
        pm = sum(comb(n, k) * p1 ** k * (1 - p1) ** (n - k) for k in range(need, n + 1))
        tie = comb(n, n // 2) * p1 ** (n // 2) * (1 - p1) ** (n // 2) if n % 2 == 0 else 0.0
        LOG.w('result', section='S1', check='bench_size_majority', n_members=n, p_member=round(p1, 4), p_majority=round(pm, 4), p_exact_tie=round(tie, 4),
              note='MODEL: R-30 quorum share 0.5, independent identical judges; real benches are 3 to 5 distinct persons (S5)')
    # matters per party on the REAL fold
    f = Fold(0)
    soid, spid = f.holder('Senior Inquisitor')
    tgt = f.people_in('terr_T9', exclude=(spid,))[0]
    opened = refused = 0
    for i in range(50):
        out = f(act(f's1_m{i}', spid, 'open_case', soid, subject=tgt, record=f'case_{i}'))
        k = ev_kinds(out)
        opened += 'case.opened' in k; refused += 'case.refused' in k
    LOG.w('trial', section='S1', check='matters_per_party_50', n=50, opened=opened, refused=refused, wilson95_opened=wilson(opened, 50),
          reading='R-11 (many matters about one party) is unreachable: one docket item per party; P3 does not change this (the forum contest only adds a second AUTHORITY, not a second matter)')
    # unknown row
    out = f(act('s1_unknown', spid, 'open_case', soid, subject=f.people_in('terr_T9', exclude=(spid, tgt))[0], arrangement='no_such_row'))
    LOG.w('trial', section='S1', check='unknown_row', events=ev_kinds(out), n=1)
    # unknown/missing authority: an office whose faction is not in the map
    from engine.season.data.rosters import office_faction
    unmapped = sorted({o.faction for o in f.w.offices.values() if o.faction not in BY_FACTION})
    LOG.w('result', section='S1', check='missing_authority', factions_not_in_by_faction=unmapped,
          reading='P3 3.1: not listed => no bench, members contest as parties. Consequence for row `arbitration` (disposal: bench): authority `parties` has an empty bench by construction', 
          offices_with_no_faction=[oid for oid, o in f.w.offices.items() if not o.faction])
    # seat with no holder
    koid, kpid = f.holder('King')
    for t in f.w.tenures:
        if t.kind == 'hold' and t.live and t.object == koid:
            t.until = f.w.tick
    from engine.season.queries import world_q
    LOG.w('result', section='S1', check='seat_with_no_holder', king_seat_vacated=True, judging_set_T1_size=len(set(world_q.judging_set(f.w, 'terr_T1'))),
          is_royal_model=bool(_royal_set(f.w)), royal_after_vacancy=sorted(_royal_set(f.w)),
          reading='with the King\'s seat vacant is_royal(w, p) over live holds reads one fewer royal person; a vacant realm seat is not a royal person')
    LOG.w('summary_section', section='S1')


@guarded
def sec_S2():
    """Distributions and one-at-a-time sensitivity (MODEL on real p_success). The armature's claim: the sigma channel dominates at high pools."""
    from engine.dice_engine.sigma_leverage import p_success, net_boost
    LOG.w('plan', section='S2', what='one-at-a-time sensitivity of P(meets) around pool b, Ob 2.5, weight 2, L .55: L (0..1), weight (0..3), opinion_full, +-1 die, +-1 Ob, +-1 sigma; and the armature claim that sigma dominates at high pools')
    LOG.w('claim', where='ARM D.1 (shared base)', quote='sigma ... is a z-shift: it is worth the same probability to a novice and a master, while a die or an Ob point matters less as the pool grows')
    for b in (1, 2, 5, 12, 30):
        base = p_success(2.5, b + 2 * 0.55)
        eff = {
            'L 0->1 (weight 2)': p_success(2.5, b + 2 * 1.0) - p_success(2.5, b + 2 * 0.0),
            'weight 0->3 (L .55)': p_success(2.5, b + 3 * .55) - p_success(2.5, b),
            'T9 vs T2 church L (.78 vs .37)': p_success(2.5, b + 2 * .78) - p_success(2.5, b + 2 * .37),
            '+1 die': p_success(2.5, b + 1 + 1.1) - base,
            '-1 die': p_success(2.5, max(1, b - 1) + 1.1) - base,
            '+1 Ob': p_success(3.5, b + 1.1) - base,
            '-1 Ob': p_success(1.5, b + 1.1) - base,
            '+1 sigma': p_success(2.5, b + 1.1, 1.0) - base,
            '-1 sigma': p_success(2.5, b + 1.1, -1.0) - base,
            'opinion_full 1->3 at L(T9)': p_success(2.5, b + 2 * L_from(.549, 3.0)) - p_success(2.5, b + 2 * L_from(.549, 1.0)),
        }
        LOG.w('result', section='S2', check='tornado', pool=b, base_p=round(base, 4), delta_pts={k: round(100 * v, 2) for k, v in eff.items()},
              largest=max(eff, key=lambda k: abs(eff[k])), note='MODEL; p_success is the continuous closed form')
    for b in (2, 5, 12, 30):
        d_sig = p_success(2.5, b, 1.0) - p_success(2.5, b, 0.0)
        d_L = p_success(2.5, b + 2 * .78) - p_success(2.5, b + 2 * .37)
        d_die = p_success(2.5, b + 1) - p_success(2.5, b)
        LOG.w('result', section='S2', check='sigma_vs_dice_at_pool', pool=b, d_plus1sigma_pts=round(100 * d_sig, 2), d_L_T9_vs_T2_pts=round(100 * d_L, 2), d_plus1die_pts=round(100 * d_die, 2),
              ratio_sigma_to_L=round(d_sig / d_L, 2) if d_L else None)
    # kinds: the roll-level probability of each kind's deciding act at three pools (choice-level parts are NOT rollable)
    for b in (2, 5, 12):
        kinds = {
            'K3a royal tribunal (King w3, L .74 at T1)': p_success(2.0, b + 3 * .74),
            'K3a Hafenmark: bench is King+Queen only': p_success(2.0, b + 3 * .74),
            'K3b heresy, church seat w2 at T9 (L .78)': p_success(2.0, b + 2 * .78),
            'K3b heresy, church seat w2 at T2 (L .37)': p_success(2.0, b + 2 * .37),
            'K4 petition, bench of one (no weight)': p_success(2.0, b),
            'K1 dyadic influence vs equal (Ob b/2)': p_success(b / 2, b),
        }
        LOG.w('result', section='S2', check='kind_roll_probabilities', pool=b, p={k: round(v, 4) for k, v in kinds.items()},
              unverified='K2 negotiation (both commit), K5 panel count and K6 parliament count are choices and counts, not draws; K7 display is stance movement: none of these has a roll-level probability to report here')
    LOG.w('unverified', section='S2', what='the eight kinds end to end over many seeds: no kind runs from a computed case today (computed open_case names no row, G logs), so a seeded distribution of a whole kind would be a distribution of my model, not of the code')
    LOG.w('summary_section', section='S2')


@guarded
def sec_S5():
    """Real data: benches by authority and territory, who can open a case, what is empty; forum-contest reach."""
    build_realm, world_q, faction_prop_id, FACTION_BY_PROP = real()
    from engine.season.state import gate
    from engine.season.state.containment import home_of
    f = Fold(0)
    w = f.w
    LOG.w('plan', section='S5', what='per person (n=83): bench at his home under the live rule, P3 authority filter (polity / church), and with Q1 scope anchor; who has purview to open a case; where a forum contest (two authorities able to open on one matter) can exist')
    ho = home_of(w)
    realm = [rid for rid, r in w.rungs.items() if r.kind == 'realm'][0]
    def bench(venue, auth, scope_church_realm=False):
        out = set()
        for t in w.tenures:
            if t.kind == 'hold' and t.live and 'determine' in t.granted_acts:
                o = w.offices.get(t.object)
                if o is None:
                    continue
                sr = realm if (scope_church_realm and BY_FACTION.get(o.faction) == 'church') else o.scope_rung
                if sr is None or sr not in world_q.ancestry(w, venue):
                    continue
                if auth is None or BY_FACTION.get(o.faction, 'parties') == auth:
                    out.add(t.subject)
        return out
    n = 0; stats = collections.Counter(); sizes = collections.defaultdict(list); forum = 0
    for pid, home in sorted(ho.items()):
        if pid not in w.persons:
            continue
        n += 1
        live = bench(home, None); pol = bench(home, 'polity'); ch = bench(home, 'church'); chq = bench(home, 'church', True); par = bench(home, 'parties')
        sizes['live'].append(len(live)); sizes['polity'].append(len(pol)); sizes['church'].append(len(ch)); sizes['church_Q1'].append(len(chq)); sizes['parties'].append(len(par))
        stats['church_bench_empty'] += not ch; stats['church_Q1_bench_empty'] += not chq; stats['polity_bench_empty'] += not pol; stats['parties_bench_empty'] += not par
        stats['church_bench_has_king_in_live'] += any(w.offices[t.object].faction == 'Crown' for t in w.tenures if t.kind == 'hold' and t.live and t.subject in live and 'determine' in t.granted_acts and t.object in w.offices)
        # open_case purview (Office.rung) for church determining seats
        ch_open = any(gate.purview_reaches(w, w.offices[t.object], home) for t in w.tenures if t.kind == 'hold' and t.live and 'determine' in t.granted_acts and t.object in w.offices and BY_FACTION.get(w.offices[t.object].faction) == 'church')
        pol_open = any(gate.purview_reaches(w, w.offices[t.object], home) for t in w.tenures if t.kind == 'hold' and t.live and 'determine' in t.granted_acts and t.object in w.offices and BY_FACTION.get(w.offices[t.object].faction) == 'polity')
        stats['church_can_open'] += ch_open; stats['polity_can_open'] += pol_open; stats['both_can_open_forum_possible'] += (ch_open and pol_open)
    for k in ('church_bench_empty', 'church_Q1_bench_empty', 'polity_bench_empty', 'parties_bench_empty', 'church_bench_has_king_in_live', 'church_can_open', 'polity_can_open', 'both_can_open_forum_possible'):
        LOG.w('result', section='S5', metric=k, k=stats[k], n=n, rate=round(stats[k] / n, 4), wilson95=wilson(stats[k], n))
    for k, v in sizes.items():
        LOG.w('result', section='S5', metric='bench_size_distribution', bench=k, min=min(v), median=sorted(v)[len(v) // 2], max=max(v), histogram=dict(sorted(collections.Counter(v).items())), n=len(v))
    # by territory
    byt = collections.defaultdict(lambda: collections.Counter())
    for pid, home in ho.items():
        if pid in w.persons:
            T = territory_of(w, world_q, home)
            byt[T]['n'] += 1; byt[T]['church_bench'] = len(bench(home, 'church')); byt[T]['polity_bench'] = len(bench(home, 'polity'))
    LOG.w('result', section='S5', metric='by_territory', rows={t.replace('terr_', ''): dict(v) for t, v in sorted(byt.items())})
    hm = [oid for oid, o in w.offices.items() if o.faction == 'Hafenmark']
    LOG.w('result', section='S5', metric='hafenmark_seats', seats=hm, holders_with_determine=[t.object for t in w.tenures if t.kind == 'hold' and t.live and t.object in hm and 'determine' in t.granted_acts],
          claimed='Hafenmark has no seat that determines, so polity proceedings there are heard only by the King and Queen')
    LOG.w('summary_section', section='S5')


@guarded
def sec_S6():
    """Failure injection on a real realm through the real fold."""
    from engine.season.queries import world_q
    LOG.w('plan', section='S6', what='kill the judge mid-proceeding; revoke the seat; vacate the bench; burn the case file; party with no capability; compare to what P3 says should happen')
    LOG.w('claim', where='P3 9.1 R', quote='an empty bench, an impasse forum and an unexecuted warrant all leave the matter on the docket, never a refusal (R-16, R-17)')
    def setup(**fx):
        f = Fold(0, fixtures={'pool_default': 30, **fx})
        soid, spid = f.holder('Senior Inquisitor')
        tgt = f.people_in('terr_T9', exclude=(spid,))[0]
        o = f(act('s6_open', spid, 'open_case', soid, subject=tgt, arrangement='inquisition_hearing'))
        return f, soid, spid, tgt, o
    # 1 kill the judge
    f, soid, spid, tgt, o = setup()
    from engine.season.loop.driver import mint_token as _mt
    from engine.season.data.matrix import WriteClass as _WC
    f.w.write("exists", _mt(f.w, _WC.ACTS), lambda: f.w.remove_person(spid), record_kind="Person", fieldname="exists", driver="Event",
              emits="person.died", subject=spid, causes=[__import__("engine.season.state.ids", fromlist=["ROOT"]).ROOT])
    others = [(oid, pid) for oid, pid in (f.holder('Confessor'), f.holder('Cardinal Justice'))]
    d = f(act('s6_det_confessor', others[0][1], 'determine', others[0][0], subject=tgt))
    d2 = f(act('s6_det_dead', spid, 'determine', soid, subject=tgt))
    LOG.w('trial', section='S6', test='kill_judge_mid_proceeding', open=ev_kinds(o), docket_still_has_party=any(x.get('matter') == tgt for x in f.w.docket),
          other_church_judge_determine=ev_kinds(d), dead_judge_determine=ev_kinds(d2), n=1,
          reading='the docket item survives the opener\'s death and another seat can determine it (no orphan), the dead actor\'s act is refused or raises')
    # 2 revoke the seat of the would-be judge
    f, soid, spid, tgt, o = setup()
    for t in f.w.tenures:
        if t.kind == 'hold' and t.live and t.object == soid:
            t.until = f.w.tick
    d = f(act('s6_det_revoked', spid, 'determine', soid, subject=tgt))
    LOG.w('trial', section='S6', test='revoke_seat', determine=ev_kinds(d), docket_kept=any(x.get('matter') == tgt for x in f.w.docket), n=1)
    # 3 vacate the bench: every church determine seat vacated, King determines
    f, soid, spid, tgt, o = setup(bench_quorum=1)
    for t in f.w.tenures:
        if t.kind == 'hold' and t.live and 'determine' in t.granted_acts and f.w.offices.get(t.object) and BY_FACTION.get(f.w.offices[t.object].faction) == 'church':
            t.until = f.w.tick
    koid, kpid = f.holder('King')
    bench_now = world_q.judging_set(f.w, world_q.place_of(f.w, tgt), tgt)
    d = f(act('s6_det_king', kpid, 'determine', koid, subject=tgt))
    LOG.w('trial', section='S6', test='vacate_church_bench_then_King_determines_church_row', live_bench=bench_now, determine=ev_kinds(d), n=1,
          reading='live code: the King still determines a church-row matter (the bench is not filtered by row in the code)')
    # 4 burn the case file
    f, soid, spid, tgt, o = setup()
    rec = [r for r in f.w.records if r.startswith('rec:s6_open')]
    ds = f(act('s6_destroy', spid, 'destroy_record', None, subject=rec[0])) if rec else []
    d = f(act('s6_det_after_burn', spid, 'determine', soid, subject=tgt))
    LOG.w('trial', section='S6', test='burn_case_file', record=rec, destroy=ev_kinds(ds), determine_after=ev_kinds(d), n=1,
          reading='if determine still executes after the case file is destroyed, the case file is not load-bearing (P3 relies on the docket item, not the Record)')
    # 5 vacate everything: no holder anywhere for determine
    f, soid, spid, tgt, o = setup()
    for t in f.w.tenures:
        if t.kind == 'hold' and t.live and 'determine' in t.granted_acts:
            t.until = f.w.tick
    d = f(act('s6_det_nobody', spid, 'determine', soid, subject=tgt))
    LOG.w('trial', section='S6', test='empty_bench_everywhere', bench=world_q.judging_set(f.w, world_q.place_of(f.w, tgt), tgt), determine=ev_kinds(d), docket_kept=any(x.get('matter') == tgt for x in f.w.docket), n=1,
          reading='determine.refused is emitted (a refusal Event); the matter stays docketed (R-16/R-17 hold on the docket half; "never a refusal" is false: a refusal Event is emitted)')
    # 6 party with no capability: realm authors none
    LOG.w('result', section='S6', test='party_with_no_capability', note='no capability is authored for any person (shared dead core 6), so every party rolls at the default pool; there is no capability-less state distinct from the default to inject', verdict='NULL (nothing to inject)')
    LOG.w('summary_section', section='S6')


@guarded
def sec_S7():
    """Determinism and cost."""
    from engine.season.harness.populated import build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P
    import hashlib
    LOG.w('plan', section='S7', what='same seed twice: build hash, then 2 seasons: event-kind stream hash and content hash; cost of the L index vs tenure count; large realm')
    hashes = []
    for rep in (1, 2):
        w = build_realm(0)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        t0 = time.time()
        for _ in range(2):
            d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
        el = time.time() - t0
        stream = hashlib.sha256('\n'.join(f'{e.id}|{e.kind}|{e.degree}' for e in w.log).encode()).hexdigest()
        hashes.append((stream, w.content_hash(), len(w.log)))
        LOG.w('trial', section='S7', rep=rep, seasons=2, wall_s=round(el, 1), events=len(w.log), stream_sha=stream[:16], content_hash=w.content_hash())
    same = hashes[0] == hashes[1]
    LOG.w('result' if same else 'fail', section='S7', check='same_seed_twice_identical', identical=same, n_reps=2, seasons=2)
    # L-index cost vs tenure inflation
    build_realm_, world_q, faction_prop_id, _ = real()
    w = build_realm_(0)
    from engine.season.state.carriers import Tenure
    for mult in (1, 10, 50):
        w2 = build_realm_(0)
        base = list(w2.tenures)
        for i in range(mult - 1):
            for t in base:
                w2.tenures.append(Tenure(f'dead_{i}_{t.id}', t.subject, t.object, t.kind, since=0, until=0))
        t0 = time.time(); legitimacy_table(w2, world_q, faction_prop_id); dt = time.time() - t0
        LOG.w('result', section='S7', check='L_index_cost_vs_tenures', tenures=len(w2.tenures), persons=len(w2.persons), secs=round(dt, 3),
              note='dead tenures only inflate the scan; members() and deed_doers are O(tenures) per opinion_of call')
    LOG.w('skipped', section='S7', what='large realm', why='build_realm seats every authored case: 83 persons is the maximum (cap only reduces; foreign=True adds 2 offices). No larger world exists to build; scale is extrapolated from the tenure-inflation line above, not run')
    LOG.w('summary_section', section='S7')


@guarded
def sec_S1b():
    """Correction of two of my own first S1 readings."""
    from engine.dice_engine.sigma_leverage import p_success
    nan = float('nan')
    a = p_success(2.5, nan); b = p_success(nan, 5); c = p_success(2.5, 5 + 2 * nan)
    LOG.w('fail', section='S1', what='my S1 grid note said a NaN operand "poisons p_success". The grid found 0 non-finite cells in 864, so that reading was wrong for NaN in the POOL position: max(1.0, nan) is 1.0, so a NaN pool is silently the 1D floor.',
          p_success_ob2_5_pool_nan=a, p_success_ob_nan_pool5=b, p_success_pool5_plus_2xnan=c,
          consequence='NaN in w x L becomes a 1D pool (a quiet, unflagged value); NaN in the obstacle is NaN; clamp01(NaN) is 1.0 (the most favourable L)')
    LOG.w('fail', section='S1', what='my S1 first-attempt S6 call `remove_person` outside a write window raised InstrumentDefect (AX-4); S6 was rerun through World.write (see S6 lines after this one)')


@guarded
def sec_S7b():
    """The L-index cost vs tenure count, rerun: the first S7 attempt appended to the read-only `w.tenures` view (InstrumentDefect)."""
    LOG.w('fail', section='S7', what='first S7 cost probe did `w.tenures.append(...)`; w.tenures is a read-only view (S15.1) and raised InstrumentDefect after the determinism half had run. Rerun through w.add_tenure.')
    build_realm_, world_q, faction_prop_id, _ = real()
    from engine.season.state.carriers import Tenure
    for mult in (1, 10, 50):
        w2 = build_realm_(0)
        base = list(w2.tenures)
        for i in range(mult - 1):
            for t in base:
                w2.add_tenure(Tenure(f'dead_{i}_{t.id}', t.subject, t.object, t.kind, since=0, until=0))
        t0 = time.time(); legitimacy_table(w2, world_q, faction_prop_id); dt = time.time() - t0
        LOG.w('result', section='S7', check='L_index_cost_vs_tenures', tenures=len(w2.tenures), persons=len(w2.persons), secs=round(dt, 3),
              note='dead tenures inflate the scan; members() and deed_doers are O(tenures) per opinion_of call, 4 factions x 83 persons per index build')
    LOG.w('skipped', section='S7', what='large realm', why='build_realm seats every authored case: 83 persons is the maximum (cap only reduces; foreign=True adds 2 offices). No larger world exists to build; scale is extrapolated from the tenure-inflation line, not run')


H_KERNEL_FILES = ['engine/tests/test_contest_kernel.py', 'engine/tests/test_sigma_leverage_parity.py', 'engine/season/tests/test_social_contest_module.py',
                  'tests/valoria/test_import_cycle_game_state_npe.py', 'tests/valoria/test_engine_does_not_import_systems.py', 'tests/valoria/test_band_extension_seam.py',
                  'tests/valoria/test_tn7_always.py', 'tests/valoria/test_balance_oracle_arms.py', 'tests/valoria/test_structure_audit.py',
                  'tests/valoria/test_degree_ladder_single_owner.py']
H_KEY_FILES = ['engine/season/tests/test_arrangements.py', 'engine/season/tests/test_u7_remit.py', 'engine/season/tests/test_stress_proceedings_rehost.py']
H_JS_FILES = ['engine/season/tests/test_u7_remit.py', 'engine/season/tests/test_sc02_reception.py', 'engine/season/tests/test_stress_proceedings_rehost.py']
H_CONTRACT_FILES = ['tests/valoria/test_modules_reachable_closure.py', 'tests/valoria/test_wiring_validation.py', 'tests/valoria/test_stubwire.py',
                    'tests/valoria/test_coverage_matrix_threshold.py', 'tests/valoria/test_flow_skeletons.py']
H_EXT_FILES = ['engine/season/tests/test_u7_remit.py', 'engine/season/tests/test_sc01_speak.py']


def _run_files(wt, files, phase, timeout=420):
    """Run each test file in the worktree WITHOUT -x, so the per-file counts are whole (the brief suggests -x; that hides how many break)."""
    import re
    for fpath in files:
        if not os.path.exists(os.path.join(wt, fpath)):
            LOG.w('blocked', section='H', phase=phase, file=fpath, why='file does not exist in the worktree')
            continue
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, '-m', 'pytest', fpath, '-q', '-p', 'no:cacheprovider', '--no-header'], cwd=wt,
                               capture_output=True, text=True, timeout=timeout, env={**os.environ, 'PYTHONHASHSEED': '0'})
            out = (r.stdout + r.stderr)
            tail = out.strip().splitlines()[-1:]
            m = {k: int(v) for v, k in re.findall(r'(\d+) (passed|failed|error|errors|skipped)', ' '.join(tail))}
            failed = [l[:150] for l in out.splitlines() if l.startswith('FAILED') or l.startswith('ERROR')][:6]
            LOG.w('trial', section='H', phase=phase, file=fpath, rc=r.returncode, counts=m, wall_s=round(time.time() - t0, 1), failed_nodes=failed, n=1,
                  last_line=(tail[0][:200] if tail else ''))
        except subprocess.TimeoutExpired:
            LOG.w('fail', section='H', phase=phase, file=fpath, why=f'timeout {timeout}s')


@guarded
def sec_H():
    import re, shutil
    wt = os.environ.get('P3_WORKTREE')
    if not wt or not os.path.isdir(wt):
        LOG.w('blocked', section='H', why='P3_WORKTREE not set to an existing git worktree')
        return
    LOG.w('plan', section='H', worktree=wt, what='baseline the touched test files in a scratch worktree of HEAD, then apply P3 C1 in 5 cumulative steps (kernel dir; four arrangement keys; judging_set matter param; module_contracts kernel row; contest() extension param), running only the files each step can reach')
    LOG.w('claim', where='P3 6 C1', quote='deletions (5) | the suite, fewer files | green; one FORK: row per deletion')
    LOG.w('claim', where='comparison 4', quote="Deleting the kernel breaks a test none of them claims: engine/tests/test_sigma_leverage_parity.py:52 imports the kernel's degree_extension ... the four keys appear 44 times across three test files; test_arrangements.py:31-34 pins exactly eight rows.")
    if os.environ.get('P3_RELAUNCH'):
        LOG.w('fail', section='H', what='first H launch ran the baseline with test_engine_does_not_import_systems.py (a slow subprocess-import test, 3+ CPU minutes, listed three times across the phase sets) and engine/season/tests/test_season_shape.py (5+ CPU minutes; it only MENTIONS the kernel path in a comment at :15021). Killed after 4 baseline files; relaunched with the slow file kept once (kernel phase) and test_season_shape dropped for test_u7_remit / test_sc01_speak (which exercise contest() through the fold). The worktree was still unmodified when killed.')
    all_files = list(dict.fromkeys(H_KERNEL_FILES + H_KEY_FILES + H_JS_FILES + H_CONTRACT_FILES + H_EXT_FILES))
    _run_files(wt, all_files, 'baseline_control', timeout=int(os.environ.get('P3_TO', '420')))
    ph = os.environ.get('P3_PHASES', '1,2,3,4,5').split(',')

    def sub(path, old, new):
        fp = os.path.join(wt, path)
        t = open(fp).read()
        if old not in t:
            LOG.w('blocked', section='H', path=path, why='edit anchor not found: ' + repr(old[:70]))
            return False
        open(fp, 'w').write(t.replace(old, new, 1))
        return True
    if '1' in ph:
        d = os.path.join(wt, 'systems/social_contest/sim/contest')
        n_files = sum(len(fs) for _, _, fs in os.walk(d))
        shutil.rmtree(d)
        LOG.w('result', section='H', phase='1_delete_kernel', deleted_files=n_files, claimed='18 files')
        _run_files(wt, H_KERNEL_FILES, '1_delete_kernel')
    if '2' in ph:
        y = os.path.join(wt, 'engine/season/arrangements.yaml')
        out = []
        removed = 0
        for ln in open(y).read().splitlines(True):
            if re.match(r'^\s+(bench_basis|appeal_basis|venue_min_rank|records_dissent):', ln):
                removed += 1
                continue
            out.append(ln)
        open(y, 'w').write(''.join(out))
        LOG.w('result', section='H', phase='2_delete_keys', yaml_key_lines_removed=removed)
        A = 'engine/season/data/arrangements.py'
        sub(A, '"id", "disposal", "bench_basis", "floor", "records_dissent", "venue_min_rank",\n    "term_required", "appeal_basis", "interposed",', '"id", "disposal", "floor",\n    "term_required", "interposed",')
        sub(A, '    bench_basis = need("bench_basis")\n    if bench_basis != "none":\n        _refuse_not_in(name, "bench_basis", bench_basis, REMIT_ACTS, "`none` or a `remit_acts` member")\n', '')
        sub(A, '    records_dissent = need("records_dissent")\n    if not isinstance(records_dissent, bool):\n        raise SystemExit(f"arrangements.yaml: {name!r} has `records_dissent: {records_dissent!r}`, "\n                         "not `true`/`false`.")\n    venue_min_rank = need("venue_min_rank")\n    _refuse_not_in(name, "venue_min_rank", venue_min_rank, RUNG_KINDS, "a `rung_kinds` member",\n                   repr_fn=list)\n', '')
        sub(A, '    appeal_basis = need("appeal_basis")\n    if appeal_basis != "none":\n        _refuse_not_in(name, "appeal_basis", appeal_basis, REMIT_ACTS, "`none` or a `remit_acts` member")\n', '')
        sub(A, '"id": name, "disposal": disposal, "bench_basis": bench_basis,\n        "floor": floor_form, "floor_basis": floor_basis, "records_dissent": records_dissent,\n        "venue_min_rank": venue_min_rank, "term_required": term_required,\n        "appeal_basis": appeal_basis, "interposed":', '"id": name, "disposal": disposal,\n        "floor": floor_form, "floor_basis": floor_basis, "term_required": term_required,\n        "interposed":')
        r = subprocess.run([sys.executable, '-c', 'from engine.season.data.arrangements import ARRANGEMENTS; print(len(ARRANGEMENTS))'], cwd=wt, capture_output=True, text=True)
        LOG.w('result', section='H', phase='2_delete_keys', loader_import_rc=r.returncode, loader_out=(r.stdout + r.stderr)[-300:])
        _run_files(wt, H_KEY_FILES, '2_delete_keys')
    if '3' in ph:
        W = 'engine/season/queries/world_q.py'
        ok1 = sub(W, 'def judging_set(w: World, venue: str, matter: Optional[str] = None) -> list[str]:', 'def judging_set(w: World, venue: str) -> list[str]:')
        ok2 = sub(W, 'len(set(judging_set(w, venue, subject)))', 'len(set(judging_set(w, venue)))')
        LOG.w('result', section='H', phase='3_judging_set_param', edits_applied=[ok1, ok2])
        _run_files(wt, H_JS_FILES, '3_judging_set_param')
    if '4' in ph:
        y = os.path.join(wt, 'references/module_contracts.yaml')
        t = open(y).read()
        i = t.find('  - module: social_contest\n')
        j = t.find('\n  - module:', i + 5)
        LOG.w('result', section='H', phase='4_contract_row', row_found=i >= 0, block_lines=(t[i:j].count('\n') if i >= 0 else None), claimed='module_contracts.yaml:448-470 (23 lines)')
        if i >= 0:
            open(y, 'w').write(t[:i] + t[j + 1:])
        _run_files(wt, H_CONTRACT_FILES, '4_contract_row')
    if '5' in ph:
        ok = sub('engine/season/seam/contest.py', '            extension: Optional[Callable[[str], bool]] = None,\n', '')
        LOG.w('result', section='H', phase='5_contest_extension', edit_applied=ok)
        _run_files(wt, H_EXT_FILES, '5_contest_extension', timeout=600)
    LOG.w('summary_section', section='H')


@guarded
def sec_G2():
    """Derived from the three season logs (no new run): royal involvement by matter KIND. The G result logged only the first 60 matter events per seed
    (matters_sample), so seeds 0 and 1 are TRUNCATED there (77 and 66 executed) and are reported on that prefix; seed 2 (57) is whole."""
    d = os.path.dirname(os.path.abspath(__file__))
    tot = collections.Counter(); roy = collections.Counter()
    for sd in (0, 1, 2):
        path = os.path.join(d, f'2026-10-30-stress-log-p3-authority-seasons-s{sd}.jsonl')
        for l in open(path):
            x = json.loads(l)
            if x['kind'] == 'result' and 'matters_sample' in x:
                ms = x['matters_sample']
                full = None
                for l2 in open(path):
                    y = json.loads(l2)
                    if y['kind'] == 'result' and 'executed_matter_events' in y:
                        full = y['executed_matter_events']
                for m in ms:
                    kind = m[1]; royal_any = bool(m[5] or m[6] or m[7])
                    tot[(sd, kind)] += 1; roy[(sd, kind)] += royal_any
                    roy[(sd, kind, 'subject')] += bool(m[5]); roy[(sd, kind, 'actor')] += bool(m[6])
                LOG.w('result', section='G2', seed=sd, sample_n=len(ms), executed_total=full, truncated=(full or 0) > len(ms),
                      by_kind={k[1]: [roy[k], tot[k]] for k in tot if k[0] == sd})
    for kind in ('case.opened', 'petition.carried', 'petition.filed'):
        k = sum(roy[(s_, kind)] for s_ in (0, 1, 2)); n = sum(tot[(s_, kind)] for s_ in (0, 1, 2))
        ks = sum(roy[(s_, kind, 'subject')] for s_ in (0, 1, 2)); ka = sum(roy[(s_, kind, 'actor')] for s_ in (0, 1, 2))
        LOG.w('result', section='G2', matter_kind=kind, royal_subject_only=ks, royal_subject_wilson95=wilson(ks, n), royal_actor_only=ka, royal_party_any=k, n=n, rate=round(k / n, 4) if n else None, wilson95=wilson(k, n),
              note='royal = live holder of a realm-rung Crown seat (4 persons of 83) as matter subject, actor, or addressee; for computed petitions subject == addressee (H-94), so those two are one count')
    base = 4 / 83
    LOG.w('result', section='G2', control='royal persons are 4 of 83 persons (5%): chance share of a random person-matter is', rate=round(base, 4), wilson95=wilson(4, 83))


@guarded
def sec_S4():
    """Throughput: acts needed per route, and P(disposal within k seasons). MODEL: a Markov chain over stages, one tick per season; scene budget 5.
    Stage probabilities are PARAMETERS (the chooser forming the act), swept; the roll probabilities are real p_success. The measured arm uses the G-run rates."""
    from engine.dice_engine.sigma_leverage import p_success
    LOG.w('plan', section='S4', what='acts per route vs scene budget 5; MC of stage chains with p_stage in {.05,.2,.5}, q_serve in {0,.25,1}; horizons 1,2,4,8,16 seasons; a conservative one-stage-per-season arm and a chained arm (up to 5 rounds per season)')
    routes = {
        'A polity tribunal in purview': ['open_case', 'determine'],
        'B church custody outside T9/T1 (warrant)': ['open_case', 'determine', 'arrest'],
        'C B + appeal to another authority': ['open_case', 'determine', 'arrest', 'petition', 'carry', 'determine(appellate)', 'pardon(closure)'],
        'D forum contest (two authorities) then A': ['open_case', 'open_case(second, refused today)', 'commit', 'commit', 'determine(forum)', 'determine'],
    }
    for r, st in routes.items():
        LOG.w('result', section='S4', check='acts_needed', route=r, acts=len(st), stages=st, scene_budget=5, actors_min={'A': 1, 'B': 2, 'C': 3, 'D': 4}[r[0]],
              fits_one_person_budget=len(st) <= 5, note='acts are spread over several persons; each person has its own budget of 5 scenes a season, so the binding limit is how many seasons the DEPENDENCY chain takes, not the budget')
    rng = random.Random(7)
    p_roll_det = p_success(2.0, 5 + 2 * 0.55)
    p_roll_arrest = p_success(2.0, 5)
    N = 6000
    for route in ('A', 'B', 'C'):
        for pst in (0.05, 0.2, 0.5):
            for q in (0.0, 0.25, 1.0):
                if route == 'A' and q != 0.0:
                    continue
                for chained in (False, True):
                    stage_p = {'A': [pst, pst * p_roll_det], 'B': [pst, pst * p_roll_det, q * pst * p_roll_arrest],
                               'C': [pst, pst * p_roll_det, q * pst * p_roll_arrest, pst, pst, pst * p_roll_det, pst]}[route]
                    done_by = {k: 0 for k in (1, 2, 4, 8, 16)}
                    for _ in range(N):
                        i = 0; t_done = None
                        for season in range(1, 17):
                            rounds = 5 if chained else 1
                            for _r in range(rounds):
                                if i < len(stage_p) and rng.random() < stage_p[i]:
                                    i += 1
                            if i >= len(stage_p):
                                t_done = season; break
                        for k in done_by:
                            if t_done is not None and t_done <= k:
                                done_by[k] += 1
                    LOG.w('trial', section='S4', route=route, p_stage=pst, q_serve=q, chained_in_season=chained, n=N,
                          p_disposed_within={str(k): [round(v / N, 4), wilson(v, N)] for k, v in done_by.items()}, p_stall_after_16=round(1 - done_by[16] / N, 4),
                          falsifier='with q_serve = 0 route B/C must read 0 disposals at every horizon (the warrant never executes); if it does not, the model leaks')
    # measured arm from the three season logs
    det_att = det_exec = 0
    d = os.path.dirname(os.path.abspath(__file__))
    for sd in (0, 1, 2):
        for l in open(os.path.join(d, f'2026-10-30-stress-log-p3-authority-seasons-s{sd}.jsonl')):
            x = json.loads(l)
            if x['kind'] == 'result' and 'determine_attempted' in x:
                det_att += x['determine_attempted']; det_exec += x['determine_executed']
    LOG.w('result', section='S4', check='measured_determine_execution_rate', attempted=det_att, executed=det_exec, rate=round(det_exec / det_att, 4), wilson95=wilson(det_exec, det_att),
          note='real seasons, shipped chooser, 3 seeds x 8 seasons: executed counts matter.determined + matter.undetermined')
    LOG.w('summary_section', section='S4')


@guarded
def sec_notes():
    LOG.w('fail', section='E', what='my E dominance labels: in `forum_contest_normal_form` I tagged a dominance "strictly" when the dominating strategy was >= everywhere and > somewhere. That is WEAK dominance in the textbook sense. Read every "strictly" in P_dominated / C_dominated as weakly dominated (>= in every column, > in at least one). The defy rows (`accused_appear_vs_defy`) are strict in the textbook sense (cost_defy < cost_appear in every cell).')
    LOG.w('fail', section='S6', what='my `kill_judge_mid_proceeding` trial logged `docket_still_has_party` AFTER the second church judge had already determined the matter, so False there means "determined", not "lost". The evidence the item survived the opener\'s death is that the other church seat\'s determine returned matter.determined.')
    LOG.w('fail', section='G', what='my first G run (all three seeds) crashed on the first season: the resolve() tee did not forward the driver\'s third positional argument. Fixed and rerun; the first-attempt errors are the first lines of each seasons log.')
    LOG.w('fail', section='G', what='my G run stopped on --budget-s (540 s), not on a crash or a quiet world, at 8 seasons per seed; wall_s of each season grew with the docket; three seeds ran concurrently with other work, so absolute times are inflated (ratios within a run are the safer reading).')


@guarded
def sec_skips():
    for what, why in [
        ('S3: denial in a staged plea', 'a Proposal-2 mechanism (stage list, plea act); Proposal 3 has no plea stage, so there is no option set to enumerate'),
        ('S3: "pick the apt speech kind" as a lookup', 'speech kinds and aptness price belong to the shared armature (ARM B2), which Proposal 3 does not change (P3 3.3: "the armature\'s draw, unchanged"); nothing P3-specific to test'),
        ('S3: expected payoff at 2D/5D/12D for every actor option', 'done for the three option sets P3 adds (accused appear/defy, forum commit/silent, forum shopping) in section E; options inherited unchanged from the armature are not enumerated'),
        ('S6: seize the case file', '`seize` needs a held warrant Record naming the Record and a seat granted seize; the case file is a kind-text Record whose `seize` path is not reachable from P3; burn was run instead (S6 burn_case_file)'),
        ('S6: second case on a docketed matter, two authorities open one matter', 'run in section F2 (F4c): case.refused for the second opener; the real code has no forum branch'),
        ('S2: each worked example and each of the eight kinds over many seeds (seeded end to end)', 'no kind reaches a computed proceeding with a row today (computed open_case names none: G logs docket_named_arrangement = 0), and P3\'s forum, warrant-branch and appeal closure are unbuilt, so a seeded run would only be my model; roll-level probabilities were reported instead (S2 kind_roll_probabilities)'),
        ('S8: running the full suite or CI jobs', 'forbidden by the brief; only the files each C1 step can reach were run'),
        ('worked example A (4): Partial "leaves a docket matter (R-17)"', 'run indirectly: the live determine opens the edge on Partial (writes Tenure.since for Partial) so Partial does not leave a docket matter in the live code; not re-derived here'),
    ]:
        LOG.w('skipped', section='misc', what=what, why=why)


@guarded
def sec_Q1hash():
    build_realm, world_q, faction_prop_id, FACTION_BY_PROP = real()
    LOG.w('claim', where='P3 9.3 Goldens', quote='Q1 would move every build_realm digest (three seats\' scope_rung change); that is a declared move')
    w = build_realm(0)
    h0 = w.content_hash()
    realm = [r for r, x in w.rungs.items() if x.kind == 'realm'][0]
    n = 0
    for post in ('Senior Inquisitor', 'Confessor', 'Cardinal Justice'):
        for o in w.offices.values():
            if o.post == post:
                o.scope_rung = realm; n += 1
    h1 = w.content_hash()
    LOG.w('result', section='Q1hash', seats_patched=n, hash_before=h0, hash_after=h1, moved=h0 != h1, verdict='HELD' if h0 != h1 else 'BROKE',
          falsifier='an unchanged hash after patching scope_rung would show scope_rung is outside the content hash')


@guarded
def sec_H2():
    wt = os.environ.get('P3_WORKTREE')
    LOG.w('fail', section='H', what='my phase 4 ran only the contract-reading tests, so it MISSED that deleting the module_contracts `social_contest` row breaks the fold: the phase 5 files (u7_remit 54 of 65, sc01_speak 9 of 13 failed) read `contest_subsystems maps \'a matter\' to \'social_contest\', which is in no module contract`. The failures that phase 5 logged are phase 4\'s, not the `extension` parameter\'s. H2 restores the row and reruns phase 5\'s files to attribute them (falsifier: if they stay red the parameter is the cause).')
    n = subprocess.run(['git', 'ls-files', 'systems/social_contest/sim/contest'], cwd=ROOT, capture_output=True, text=True).stdout.split()
    LOG.w('fail', section='H', what='claim: the kernel is "18 files" (P3 5, CA B-1)', tracked_files_in_directory=len(n),
          note='git ls-files finds 16 tracked files in systems/social_contest/sim/contest/; my phase-1 count of 31 included the __pycache__ files the baseline pytest runs created in the worktree, so it is not evidence either way')
    r = subprocess.run(['git', 'checkout', '--', 'references/module_contracts.yaml'], cwd=wt, capture_output=True, text=True)
    LOG.w('result', section='H', phase='5b_restore_contract_row', rc=r.returncode, out=(r.stdout + r.stderr)[-200:])
    _run_files(wt, H_EXT_FILES, '5b_extension_alone_contract_row_restored')
    # and the contract row alone: delete it on a fresh baseline? -> restore, then delete only the row and run the same two files
    y = os.path.join(wt, 'references/module_contracts.yaml')
    t = open(y).read(); i = t.find('  - module: social_contest\n'); j = t.find('\n  - module:', i + 5)
    open(y, 'w').write(t[:i] + t[j + 1:])
    _run_files(wt, H_EXT_FILES, '4b_contract_row_deleted_alone_on_top_of_1to3_and_5')
    subprocess.run(['git', 'checkout', '--', 'references/module_contracts.yaml'], cwd=wt, capture_output=True, text=True)
    LOG.w('summary_section', section='H2')


@guarded
def sec_H3():
    """Occurrence counts for the four row keys (assessors: '44 times across three test files') in the main tree, and the C1 tally."""
    out = subprocess.run(['grep', '-rEn', 'bench_basis|appeal_basis|venue_min_rank|records_dissent', '--include=*.py', 'engine', 'tests'], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
    byf = collections.Counter(l.split(':')[0] for l in out)
    tests = {f: n for f, n in byf.items() if '/tests/' in f or f.startswith('tests/')}
    LOG.w('result', section='H', check='four_row_keys_occurrences', total=len(out), by_file=dict(byf), in_test_files=tests,
          claimed='44 times across three test files (comparison section 4)',
          verdict='BROKE: 30 literal occurrences in ONE test file (test_arrangements.py); a second test file (test_stress_proceedings_rehost.py) fails on the key COUNT, not the names; 57 occurrences in all of engine/ and tests/ (loader 17, probes 3, comments 7)')
    LOG.w('result', section='H', check='C1_tally', baseline_red_files=0, files_run_distinct=24,
          red_files=['test_contest_kernel', 'test_sigma_leverage_parity (collection error)', 'test_import_cycle_game_state_npe', 'test_engine_does_not_import_systems', 'test_band_extension_seam',
                     'test_structure_audit', 'test_degree_ladder_single_owner', 'test_arrangements', 'test_stress_proceedings_rehost', 'test_u7_remit', 'test_flow_skeletons', 'test_sc01_speak'],
          red_file_count=12, step_attribution={'1_kernel': 7, '2_keys': 2, '3_judging_set_param': 2, '4_contract_row': 3, '5_extension_param': 0},
          note='step 4 row appears red in 3 files (flow_skeletons, u7_remit, sc01_speak); step 3 in 2 (u7_remit, stress_proceedings_rehost); counts are per step, files can recur')


@guarded
def sec_verdicts():
    """Claim-level BROKE verdicts that earlier sections logged only as `result` lines, restated as `fail` lines so the roll-call is complete. Evidence is in the cited sections."""
    F = [
        ('claim 8', 'Q1 (church `scope:` anchor, `rung` stays T9) lets the church judge anywhere and open a heresy case in T1/T4', 'B2: open_case by Senior Inquisitor / Confessor / Cardinal Justice opened 0/19 (T1) and 0/4 (T4) with scope_rung alone (case.unauthorized); 19/19 and 4/4 only when rung also moved'),
        ('claim 10', 'judging_set filtered by authority and may_determine "reads the row\'s authority" (one test)', 'D: M1 (bench only) the King leaves the bench but determines a church-row matter at quorum 1 and 3; M2 (gate reads the docketed row) the gate logs row_not_visible once per determine (docket cleared in the same write), so its write-time answer is the unfiltered rule; quorum counts 5 where 3 can act'),
        ('claim 14', 'a church custody outside T9 "goes to a polity seat at realm scope" by warrant', 'F, F2: the Confessor\'s issue to the King is issue.unauthorized (issuer purview must reach the executor; 1 of 16 polity dispatch holders is inside it); give refused (not co-located); the chain runs only when the church seat\'s rung is the realm'),
        ('claim 15', '`open_case`\'s Record is the summons and `evade / defy` gains its reader', 'F5: case file is kind text, held by the opener; evade/defy on it is compliance.impossible. G: 160 attempts, 0 executed (no compliance.withheld)'),
        ('claim 16', 'defy has no cost in the draw, and the arm decides (a warrant) -- as a design', 'E: defy strictly cheaper than appear in 36/36 cells; at q=0 (the measured chooser) it removes the whole sentence'),
        ('claim 17', '`arrest` was attempted 0 times', 'G seed 0: 4 attempts, 4 arrest.refused (seeds 1, 2: 0)'),
        ('claim 18', '`determine` rolled 0 times', 'G: 65 attempts over 24 seasons, 3 executed (all matter.undetermined)'),
        ('claim 28', 'hostility lowers L ("polity legitimacy and piety are one calculation")', 'A: no polity faction reads below 0.50 in any of 16 territories; only the church does (3 of 16)'),
        ('claim 27', 'C1 deletions: "green; fewer files"', 'worktree: 12 of 24 test files red after the cumulative C1 steps (0 red at baseline); see S8'),
        ('assessor claim', '"the four keys appear 44 times across three test files"', 'H3: 30 literal occurrences in one test file; 57 in engine/ and tests/ together'),
        ('audit claim B-12', 'the module_contracts `social_contest` row (:448-470) is stale', 'H, 4b: deleting it fails 54/65 of test_u7_remit and 9/13 of test_sc01_speak (`contest_subsystems` maps \'a matter\' to \'social_contest\'); the row is load-bearing for the live contest dispatch, only its sim_module path is stale'),
        ('audit claim B-1', 'the kernel is 18 files', 'H: git ls-files finds 16 tracked files in the directory'),
    ]
    for tag, claim, ev in F:
        LOG.w('fail', section='verdicts', ledger=tag, claim=claim, evidence=ev)
    LOG.w('null', section='verdicts', ledger='claim 22', examined='the forum branch, warrant branch, appellate closure basis, expulsion rule and evade/defy reader are not in the tree (grep of loop/ and state/ for each name finds none), so only the controls could run',
          what='UNTESTABLE as built')


@guarded
def sec_A2():
    build_realm, world_q, faction_prop_id, FACTION_BY_PROP = real()
    tabs = []
    for seed in (0, 1, 2):
        w = build_realm(seed)
        tab, op = legitimacy_table(w, world_q, faction_prop_id)
        tabs.append({f: {t: round(v[2], 9) for t, v in tab[f].items()} for f in FACTIONS})
        LOG.w('result', section='A2', seed=seed, content_hash=w.content_hash(), world_seed=w.world_seed)
    same = tabs[0] == tabs[1] == tabs[2]
    LOG.w('null' if same else 'result', section='A2', check='L_tables_equal_across_seeds', identical=same,
          examined='legitimacy_table() for seeds 0,1,2 compared entry by entry to 9 dp',
          consequence='build_realm seeds differ in content_hash but not in any resident opinion: the three seeds are one sample of L, not three (n=1 world)')


# ---------------------------------------------------------------------------------------------
def main():
    global LOG
    ap = argparse.ArgumentParser()
    ap.add_argument('--log', required=True)
    ap.add_argument('--sections', nargs='+', required=True)
    ap.add_argument('--budget-s', type=float, default=1500)
    ap.add_argument('--label', default='authority')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--max-seasons', type=int, default=0)
    args = ap.parse_args()
    global ARGS
    ARGS = args
    LOG = Log(args.log)
    LOG.w('manifest', head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'), python=sys.version.split()[0],
          pythonhashseed=os.environ.get('PYTHONHASHSEED'), argv=sys.argv, started_utc=utc(), label=args.label,
          worktree=os.environ.get('P3_WORKTREE'), budget_s=args.budget_s,
          stop_rule='first of: crash (logged `error`, next section runs), quiet result, or --budget-s; no chosen horizon or n')
    t0 = time.time()
    for s in args.sections:
        if time.time() - t0 > args.budget_s:
            LOG.w('skipped', section=s, why='wall-clock budget reached')
            continue
        fn = globals().get('sec_' + s)
        if fn is None:
            LOG.w('blocked', section=s, why='no such section in this harness version')
            continue
        fn()
    LOG.w('summary', wall_s=round(time.time() - t0, 1), counts=dict(LOG.counts), stopped_by='all requested sections ended or budget')


if __name__ == '__main__':
    main()
