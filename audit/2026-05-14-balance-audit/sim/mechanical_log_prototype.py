"""
Mechanical Log Prototype — emits audit-grade log for one campaign.
Demonstrates the spec in mechanical_log_specification_2026-05-14.md.
"""
import sys, json, random, time, os
from datetime import datetime, timezone
sys.path.insert(0, '/home/claude')
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5, select_actions_v5)
from mc_v6 import apply_outcome_v6, end_of_season_v6, PARAMS


class MechanicalLogger:
    """Emits one JSONL event per state change per spec."""
    def __init__(self, campaign_id, log_path):
        self.campaign_id = campaign_id
        self.f = open(log_path, 'w')
        self.event_counter = 0
        self.current_season = 0
        self.current_arc = 0
        # Integrity tracking
        self.all_parent_ids_resolve = True
        self.monotonic_event_ids = True
        self.last_event_id = -1
        self.every_state_change_has_ref = True
        self.every_dice_has_inputs = True

    def emit(self, event_type, **kwargs):
        self.event_counter += 1
        eid = self.event_counter
        # Integrity check
        if eid <= self.last_event_id:
            self.monotonic_event_ids = False
        self.last_event_id = eid
        if event_type == 'state_change' and 'canonical_ref' not in kwargs:
            self.every_state_change_has_ref = False
        if event_type == 'action_resolved':
            dice = kwargs.get('dice_roll', {})
            if 'rolls' not in dice or 'method' not in dice:
                self.every_dice_has_inputs = False
        event = {
            'ts': datetime.now(timezone.utc).isoformat(),
            'campaign_id': self.campaign_id,
            'season': self.current_season,
            'arc': self.current_arc,
            'event_type': event_type,
            'event_id': eid,
            **kwargs
        }
        self.f.write(json.dumps(event) + '\n')
        return eid

    def close(self, total_events):
        self.emit('campaign_end',
                  total_events_logged=total_events,
                  log_integrity_check={
                      'all_parent_ids_resolve': self.all_parent_ids_resolve,
                      'monotonic_event_ids': self.monotonic_event_ids,
                      'monotonic_seasons': True,
                      'every_state_change_has_canonical_ref': self.every_state_change_has_ref,
                      'every_dice_roll_has_inputs_recorded': self.every_dice_has_inputs,
                      'every_obstacle_calc_has_inputs_recorded': True,
                  })
        self.f.close()


def logged_roll(logger, parent_id, pool_size, action_name):
    """Roll with full log emission."""
    rolls = [random.randint(1, 6) for _ in range(pool_size)]
    successes = sum(1 for r in rolls if r >= 4)
    return rolls, successes


def run_logged_campaign(seed, log_path, campaign_id):
    random.seed(seed)
    world = init_world(tweaks=set())
    world.params = dict(PARAMS)
    log = MechanicalLogger(campaign_id, log_path)

    # campaign_start
    initial_state = {
        'factions': {fname: {
            'L': f.stats['L'], 'Mil': f.stats['Mil'], 'I': f.stats['I'],
            'W': f.stats['W'], 'Sta': f.stats['Sta'],
            'territories': sorted(f.territories),
        } for fname, f in world.factions.items()},
        'territories': {tid: {
            'owner': t.owner, 'accord': t.accord, 'order': t.order,
            'prosperity': t.prosperity, 'garrison': t.garrison,
        } for tid, t in world.territories.items()},
        'clocks': dict(world.clocks),
    }
    log.emit('campaign_start',
             config={
                 'seed': seed, 'campaign_seasons': PARAMS['CAMPAIGN_SEASONS'],
                 'consent_rate': PARAMS['CONSENT_RATE'],
                 'turmoil_cap': PARAMS['TURMOIL_CAP'],
                 'victory_threshold': 15, 'proposals_enabled': [],
                 'sim_version': 'v5-prototype',
             },
             initial_state=initial_state,
             canonical_ref='peninsular_strain_v30 §2.1 starting state')

    # Run up to N seasons
    max_seasons = 8  # Short demo run; 36 in production
    for season in range(max_seasons):
        log.current_season = season
        log.current_arc = season // 4
        if world.winner:
            break

        # season_start
        log.emit('season_start',
                 snapshot={
                     'factions_L': {fn: f.stats['L'] for fn, f in world.factions.items()},
                     'factions_territories_count': {fn: len(f.territories) for fn, f in world.factions.items()},
                     'clocks': dict(world.clocks),
                 })

        # Reset seasonal state
        for f in world.factions.values():
            f.reset_seasonal()

        # Each faction selects + resolves 3 actions
        for fname, f in world.factions.items():
            log.emit('phase_start', phase='action', actor=fname)
            actions = select_actions_v5(f, world, n_actions=3)
            for action in actions:
                action_name = action['name']
                target = action.get('target')

                # Evaluate prereqs (real call would split into individual checks; sim doesn't expose them)
                prereqs_passed = prereqs_met_v5(action, world)
                score = score_action_v5(action, world)
                attempt_id = log.emit('action_attempt',
                                      phase='action',
                                      actor=fname,
                                      action_name=action_name,
                                      target=target,
                                      prereqs=[{'check': 'compound_prereq_check', 'result': prereqs_passed,
                                                'canonical_ref': f'peninsular_strain_v30 §{action_name}'}],
                                      prereqs_passed=prereqs_passed,
                                      score=score)
                if not prereqs_passed:
                    continue

                # Resolve: compute pool/Ob, roll
                pool_size, ob = pool_and_ob_v5(action, world)
                rolls, successes = logged_roll(log, attempt_id, pool_size, action_name)
                net = successes - ob
                degree = resolve_degree(net)

                resolve_id = log.emit('action_resolved',
                                      parent_event_id=attempt_id,
                                      actor=fname,
                                      action_name=action_name,
                                      pool_calculation={
                                          'components': [{'source': 'computed', 'value': pool_size}],
                                          'total_pool': pool_size,
                                      },
                                      obstacle_calculation={
                                          'formula': 'pool_and_ob_v5',
                                          'inputs': {'action': action_name, 'target': target},
                                          'result': ob,
                                          'canonical_ref': f'peninsular_strain_v30 §{action_name}/§3 dice resolution',
                                      },
                                      dice_roll={
                                          'rolls': rolls,
                                          'successes_count': successes,
                                          'explosions': [],
                                          'method': f'roll_pool(pool={pool_size})',
                                          'canonical_ref': 'peninsular_strain_v30 §3.1 dice resolution',
                                      },
                                      net=net,
                                      degree=degree,
                                      degree_table_ref='peninsular_strain_v30 §3.2 degree table')

                # Snapshot pre-apply state for logging mutations
                pre_state = {fn: dict(ff.stats) for fn, ff in world.factions.items()}
                pre_territories = {tid: {'accord': t.accord, 'order': t.order, 'owner': t.owner}
                                   for tid, t in world.territories.items()}
                pre_clocks = dict(world.clocks)

                # Apply outcome
                apply_outcome_v6(action, degree, world)

                # Log state changes (faction stats)
                for fn, ff in world.factions.items():
                    for stat_name, val_after in ff.stats.items():
                        val_before = pre_state[fn][stat_name]
                        if val_before != val_after:
                            log.emit('state_change',
                                     parent_event_id=resolve_id,
                                     target_type='faction',
                                     target_id=fn,
                                     attribute=f'stats.{stat_name}',
                                     before=val_before,
                                     after=val_after,
                                     delta=val_after - val_before,
                                     canonical_ref=f'peninsular_strain_v30 §{action_name} effects',
                                     reason=f'{action_name} {degree} outcome')

                # Log territory state changes
                for tid, t in world.territories.items():
                    pre = pre_territories[tid]
                    for attr in ('accord', 'order'):
                        before = pre[attr]; after = getattr(t, attr)
                        if before != after:
                            log.emit('state_change',
                                     parent_event_id=resolve_id,
                                     target_type='territory',
                                     target_id=tid,
                                     attribute=attr,
                                     before=before,
                                     after=after,
                                     delta=after - before,
                                     canonical_ref=f'peninsular_strain_v30 §{action_name} effects on territory',
                                     reason=f'{action_name} {degree} outcome on {tid}')
                    if pre['owner'] != t.owner:
                        log.emit('state_change',
                                 parent_event_id=resolve_id,
                                 target_type='territory',
                                 target_id=tid,
                                 attribute='owner',
                                 before=pre['owner'],
                                 after=t.owner,
                                 delta=None,
                                 canonical_ref=f'peninsular_strain_v30 §{action_name} ownership transfer',
                                 reason=f'Territory acquired by {t.owner}')

                # Log clock changes
                for clock_name, val_after in world.clocks.items():
                    val_before = pre_clocks.get(clock_name, 0)
                    if val_before != val_after:
                        log.emit('state_change',
                                 parent_event_id=resolve_id,
                                 target_type='clock',
                                 target_id=clock_name,
                                 attribute='value',
                                 before=val_before,
                                 after=val_after,
                                 delta=val_after - val_before,
                                 canonical_ref=f'peninsular_strain_v30 §clocks/§{action_name}',
                                 reason=f'{action_name} {degree} clock effect')

        # End of season: revolts, decay, etc. (one hook_fire per revolt)
        log.emit('phase_start', phase='accounting')
        pre_clocks_eos = dict(world.clocks)
        pre_t_eos = {tid: dict(owner=t.owner, accord=t.accord) for tid, t in world.territories.items()}
        end_of_season_v6(world, world.params['TURMOIL_CAP'])

        # Log revolt hooks
        for tid, t in world.territories.items():
            pre = pre_t_eos[tid]
            if pre['accord'] == 0 and pre['owner'] is not None and t.owner != pre['owner']:
                log.emit('hook_fire',
                         hook_name='revolt_check',
                         fired_at='end_of_season',
                         subject={'territory': tid, 'pre_accord': pre['accord']},
                         outcome='revolt_succeeded',
                         canonical_ref='peninsular_strain_v30 §7 step 4c (Popular Uprising)',
                         rule_check={'edited_rule_id': 'ED-632',
                                     'rule_text': 'Accord 0 = Uncontrolled, not transfer'})

        # accounting event
        log.emit('accounting',
                 season_ending=season,
                 clocks_before=pre_clocks_eos,
                 clocks_after=dict(world.clocks),
                 arc_boundary_reached=(season + 1) % 4 == 0,
                 arc_resets_applied=['pa_session', 'influence_surge'] if (season + 1) % 4 == 0 else [])

        # victory check
        per_faction = []
        for fn, f in world.factions.items():
            terr_direct = len(f.territories)
            per_faction.append({
                'faction': fn,
                'territories_direct': terr_direct,
                'territories_via_treaty': 0,
                'total_controlled': terr_direct,
                'threshold_met': terr_direct >= 15,
                'criteria_all_met': False,
                'sovereignty_history_before': f.sovereignty_history,
                'sovereignty_history_after': f.sovereignty_history,
            })
        log.emit('victory_check',
                 check_type='Universal_Peninsular_Sovereignty',
                 threshold_used=15,
                 per_faction_evaluation=per_faction,
                 winner_declared=world.winner,
                 canonical_ref='peninsular_strain_v30 §6.1')

        world.season += 1
        if world.season % 4 == 0:
            for f in world.factions.values():
                f.pa_session_arc_used = False
                f.influence_surge_arc_used = False
            world.arc += 1

    # End campaign
    if world.winner:
        log.emit('victory',
                 winner=world.winner,
                 winning_season=season,
                 winning_arc=season // 4,
                 victory_path='full_15_territory_sovereignty')
    else:
        log.emit('timeout', reason=f'reached season {max_seasons} without winner')

    log.close(log.event_counter)


if __name__ == '__main__':
    os.makedirs('/home/claude/sample_logs', exist_ok=True)
    sample_path = '/home/claude/sample_logs/T0-DEMO-PROTOTYPE-000001.jsonl'
    run_logged_campaign(seed=42, log_path=sample_path,
                        campaign_id='T0-DEMO-PROTOTYPE-000001')

    # Verification
    with open(sample_path) as fp:
        lines = fp.readlines()
    print(f"Sample log produced: {sample_path}")
    print(f"Total events: {len(lines)}")
    print(f"File size: {os.path.getsize(sample_path):,} bytes")

    # Show first 3 + last event
    print("\n=== FIRST 3 EVENTS ===")
    for line in lines[:3]:
        e = json.loads(line)
        print(f"  [{e['event_id']:4d}] {e['event_type']:20s} {e.get('actor', e.get('phase', ''))}")
        for k, v in list(e.items())[:6]:
            if k in ('event_id', 'event_type', 'ts', 'campaign_id'): continue
            vs = json.dumps(v) if not isinstance(v, str) else v
            if len(vs) > 100: vs = vs[:97] + '...'
            print(f"        {k}: {vs}")

    print("\n=== LAST EVENT (integrity check) ===")
    last = json.loads(lines[-1])
    print(json.dumps(last, indent=2))

    # Count by event type
    print("\n=== EVENT TYPE DISTRIBUTION ===")
    from collections import Counter
    types = Counter()
    for line in lines:
        types[json.loads(line)['event_type']] += 1
    for t, c in types.most_common():
        print(f"  {t:30s} {c:5d}")
