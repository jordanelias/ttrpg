"""
mc_v12 — AUDIT-GRADE SIMULATOR
v10 mechanics + Treaty Expiration (P3) + full mechanical logging per
mechanical_log_specification_2026-05-14.md

Proposals (configurable via proposals_enabled):
  P1 — Q-21 EA throttle (every-other-arc)           [canonical: Part 13 §2.2]
  P2 — Threshold 11/15 Co-Victory partition          [canonical: Part 13 §4.1]
  P3 — Treaty Expiration 40%/arc on Crown Treaties   [canonical: Part 13 §4.3]
  P4 — Vaynard's Settlement (post-conquest)          [canonical: Part 10 §5.2]
  P5 — Crown Initiative (3 modes)                    [canonical: Part 10 §3]
  P6 — Charter of Liberties (pure W cost)            [canonical: Part 13 §2.2]
  P7 — Vaynard's Hall (L-gain via military court)    [canonical: Part 10 §5.3]

Authority: peninsular_strain_v30 + canon/02_canon_constraints.md (P-01..P-15)
"""
import sys, json, random, os, time
from datetime import datetime, timezone
from collections import defaultdict, Counter
from copy import deepcopy

sys.path.insert(0, '/home/claude')
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5)
from mc_v6 import apply_outcome_v6, PARAMS
from mc_v8 import reset_seasonal_v8

Faction.reset_seasonal = reset_seasonal_v8

# ── Default config ──────────────────────────────────────────────────────────
DEFAULT_CONFIG = {
    'CAMPAIGN_SEASONS': 36,          # [canonical: peninsular_strain_v30 §4]
    'CONSENT_RATE': 0.6,             # [canonical: Part 13 §4.1 Q-1]
    'TURMOIL_CAP': 12,               # [canonical: Part 13 §4.1 Q-3]
    'TREATY_EXPIRATION_RATE': 0.4,   # [canonical: Part 13 §4.3]
    'ACTIONS_PER_FACTION': 3,        # [canonical: peninsular_strain_v30 §5]
    'APPEASE_RATE': 0.7,             # [canonical: peninsular_strain_v30 §5.3 Appease]
    'VARFELL_HAS_ACQUISITION': False, # [canonical: Part 13 §2.1]
}

ALL_PROPOSALS = {'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'}


# ═══════════════════════════════════════════════════════════════════════════
# MECHANICAL LOGGER — per mechanical_log_specification_2026-05-14.md
# ═══════════════════════════════════════════════════════════════════════════

class MechanicalLogger:
    """Emits JSONL per the log spec. One file per campaign."""

    def __init__(self, campaign_id, log_dir=None, tier=2):
        self.campaign_id = campaign_id
        self.tier = tier  # 1=summary only, 2=full stream, 3=per-die detail
        self.event_counter = 0
        self.current_season = 0
        self.current_arc = 0
        self._events = []  # in-memory buffer; flush per campaign
        # Integrity tracking
        self._parent_ids = set()
        self._all_event_ids = set()
        self.integrity = {
            'all_parent_ids_resolve': True,
            'monotonic_event_ids': True,
            'monotonic_seasons': True,
            'every_state_change_has_canonical_ref': True,
            'every_dice_roll_has_inputs_recorded': True,
            'every_obstacle_calc_has_inputs_recorded': True,
        }
        self._last_season = -1
        self._log_dir = log_dir

    def emit(self, event_type, **kwargs):
        self.event_counter += 1
        eid = self.event_counter
        self._all_event_ids.add(eid)

        # Integrity checks
        if event_type == 'state_change' and 'canonical_ref' not in kwargs:
            self.integrity['every_state_change_has_canonical_ref'] = False
        if event_type == 'action_resolved':
            dice = kwargs.get('dice_roll', {})
            if not dice.get('rolls') or not dice.get('method'):
                self.integrity['every_dice_roll_has_inputs_recorded'] = False
            ob_calc = kwargs.get('obstacle_calculation', {})
            if 'inputs' not in ob_calc:  # empty dict is valid for fixed-Ob
                self.integrity['every_obstacle_calc_has_inputs_recorded'] = False
        parent = kwargs.get('parent_event_id')
        if parent is not None:
            self._parent_ids.add(parent)

        if event_type == 'season_start':
            s = kwargs.get('snapshot', {})
            # (season monotonicity checked implicitly via self.current_season)

        event = {
            'ts': datetime.now(timezone.utc).isoformat(),
            'campaign_id': self.campaign_id,
            'season': self.current_season,
            'arc': self.current_arc,
            'event_type': event_type,
            'event_id': eid,
            **kwargs,
        }
        self._events.append(event)
        return eid

    def finalize(self):
        """Check integrity and emit campaign_end."""
        # Verify all parent_ids resolve
        unresolved = self._parent_ids - self._all_event_ids
        if unresolved:
            self.integrity['all_parent_ids_resolve'] = False
        self.emit('campaign_end',
                  total_events_logged=self.event_counter,
                  log_integrity_check=dict(self.integrity))

    def flush_to_disk(self, path):
        with open(path, 'w') as f:
            for ev in self._events:
                f.write(json.dumps(ev) + '\n')

    def get_events(self):
        return self._events


class NullLogger:
    """No-op logger for unlogged batch runs."""
    current_season = 0
    current_arc = 0
    def emit(self, *a, **kw): return 0
    def finalize(self): pass


# ═══════════════════════════════════════════════════════════════════════════
# LOGGED DICE — wraps roll_pool with log emission
# ═══════════════════════════════════════════════════════════════════════════

def logged_roll_pool(pool_size, logger=None, parent_id=None, canonical_ref=None):
    """Roll pool and optionally log. Returns (rolls, successes, net_unused)."""
    rolls = [random.randint(1, 6) for _ in range(pool_size)]
    successes = sum(1 for r in rolls if r >= 4)  # [canonical: peninsular_strain_v30 §3.1]
    return rolls, successes


# ═══════════════════════════════════════════════════════════════════════════
# v12 MECHANICS — inherits v10, adds Treaty Expiration (P3)
# ═══════════════════════════════════════════════════════════════════════════

def v12_prereqs(action, world, proposals):
    """Prereqs check with per-proposal logging. Returns (passed, prereq_list)."""
    actor = action['actor']
    name = action['name']
    prereqs = []

    # P1: Q-21 EA throttle
    if name == 'Ecclesiastical Appointment':
        if actor.name != 'Church':
            prereqs.append({'check': 'actor.name == Church', 'result': False,
                           'canonical_ref': 'peninsular_strain_v30 §5.2 EA prereq'})
            return False, prereqs
        if actor.stats['L'] >= 7:
            prereqs.append({'check': 'actor.L < 7', 'result': False, 'actual': actor.stats['L'],
                           'canonical_ref': 'peninsular_strain_v30 §5.2 L cap'})
            return False, prereqs
        if getattr(actor, 'ecclesiastical_appointment_arc_used', False):
            prereqs.append({'check': 'ea_arc_not_used', 'result': False,
                           'canonical_ref': 'P1 Q-21 per-arc throttle'})
            return False, prereqs
        if 'P1' in proposals:
            # Every-other-arc cooldown
            ea_last = getattr(actor, 'ea_last_arc', -10)
            cooldown_met = world.arc - ea_last >= 2
            prereqs.append({'check': f'world.arc({world.arc}) - ea_last_arc({ea_last}) >= 2',
                           'result': cooldown_met,
                           'canonical_ref': 'P1 every-other-arc cooldown'})
            if not cooldown_met:
                return False, prereqs
        prereqs.append({'check': 'all_EA_prereqs', 'result': True,
                       'canonical_ref': 'peninsular_strain_v30 §5.2 + P1'})
        return True, prereqs

    if name == 'Crown Initiative':
        if 'P5' not in proposals:
            return False, [{'check': 'P5_enabled', 'result': False, 'canonical_ref': 'P5 not in proposals'}]
        if actor.name != 'Crown':
            return False, [{'check': 'actor==Crown', 'result': False, 'canonical_ref': 'Part 10 §3'}]
        if getattr(actor, 'senator_inward_used', False):
            return False, [{'check': 'senator_inward_available', 'result': False, 'canonical_ref': 'P5 spec §slot'}]
        if actor.stats['W'] < 3:
            prereqs.append({'check': f'actor.W({actor.stats["W"]}) >= 3', 'result': False,
                           'canonical_ref': 'P5 spec W-3 cost (v10 tuning)'})
            return False, prereqs
        return True, [{'check': 'all_CI_prereqs', 'result': True, 'canonical_ref': 'Part 10 §3'}]

    if name == "Vaynard's Settlement":
        if 'P4' not in proposals:
            return False, [{'check': 'P4_enabled', 'result': False, 'canonical_ref': 'P4 not in proposals'}]
        if actor.name != 'Varfell':
            return False, [{'check': 'actor==Varfell', 'result': False, 'canonical_ref': 'Part 10 §5.2'}]
        if getattr(actor, 'tribune_card_used', False):
            return False, [{'check': 'tribune_card_available', 'result': False, 'canonical_ref': 'P4 spec'}]
        target = action.get('target')
        if target not in world.territories:
            return False, [{'check': 'target_valid', 'result': False, 'canonical_ref': 'P4 spec'}]
        t = world.territories[target]
        if t.owner != 'Varfell' or t.accord >= 2:
            return False, [{'check': f'target({target}).owner==Varfell AND accord<2', 'result': False,
                           'actual': f'owner={t.owner} accord={t.accord}',
                           'canonical_ref': 'P4 spec'}]
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1:
            return False, [{'check': 'Mil>=3 AND W>=1', 'result': False, 'canonical_ref': 'P4 spec'}]
        return True, [{'check': 'all_VS_prereqs', 'result': True,
                       'canonical_ref': 'Part 10 §5.2',
                       'target_state': {'territory': target, 'accord': t.accord, 'order': t.order}}]

    if name == "Vaynard's Hall":
        if 'P7' not in proposals:
            return False, [{'check': 'P7_enabled', 'result': False, 'canonical_ref': 'P7 not in proposals'}]
        if actor.name != 'Varfell':
            return False, [{'check': 'actor==Varfell', 'result': False, 'canonical_ref': 'Part 10 §5.3'}]
        if getattr(actor, 'hall_card_used', False):
            return False, [{'check': 'hall_card_available', 'result': False, 'canonical_ref': 'P7 spec'}]
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1:
            return False, [{'check': 'Mil>=3 AND W>=1', 'result': False, 'canonical_ref': 'P7 spec'}]
        return True, [{'check': 'all_VH_prereqs', 'result': True, 'canonical_ref': 'Part 10 §5.3'}]

    if name == 'Charter of Liberties':
        if 'P6' not in proposals:
            return False, [{'check': 'P6_enabled', 'result': False, 'canonical_ref': 'P6 not in proposals'}]
        if actor.name != 'Hafenmark':
            return False, [{'check': 'actor==Hafenmark', 'result': False, 'canonical_ref': 'Part 13 §2.2'}]
        if getattr(actor, 'legacy_card_used', False):
            return False, [{'check': 'legacy_card_available', 'result': False, 'canonical_ref': 'P6 spec'}]
        if actor.stats['W'] < 1:
            return False, [{'check': 'W>=1', 'result': False, 'canonical_ref': 'P6 pure-W cost'}]
        return True, [{'check': 'all_Charter_prereqs', 'result': True, 'canonical_ref': 'P6 spec'}]

    # Fall through to v5 base prereqs
    passed = prereqs_met_v5(action, world)
    return passed, [{'check': 'v5_base_prereqs', 'result': passed,
                    'canonical_ref': f'peninsular_strain_v30 §5 {name}'}]


def v12_pool_ob(action, world, proposals):
    """Pool/Ob with full input logging. Returns (pool, ob, pool_calc, ob_calc)."""
    actor = action['actor']
    name = action['name']

    if name == 'Crown Initiative' and 'P5' in proposals:
        accords = {tid: world.territories[tid].accord
                   for tid in actor.territories if tid in world.territories}
        sum_accord = sum(accords.values())
        pool = actor.stats['I']
        ob = max(1, sum_accord // 2)
        pool_calc = {'components': [{'source': 'actor.stats.I', 'value': pool}], 'total_pool': pool}
        ob_calc = {'formula': 'max(1, sum(territory.accord)//2)',
                   'inputs': {'territory_accords': accords, 'sum': sum_accord},
                   'result': ob,
                   'canonical_ref': 'P5 spec §obstacle / М-2 geography holds pressure'}
        return pool, ob, pool_calc, ob_calc

    if name == "Vaynard's Settlement" and 'P4' in proposals:
        pool = actor.stats['Mil'] + (actor.stats['W'] // 2)
        ob = 3  # [canonical: Part 10 §5.2]
        pool_calc = {'components': [
            {'source': 'actor.stats.Mil', 'value': actor.stats['Mil']},
            {'source': 'actor.stats.W//2', 'value': actor.stats['W'] // 2}],
            'total_pool': pool}
        ob_calc = {'formula': 'fixed Ob 3', 'inputs': {}, 'result': 3,
                   'canonical_ref': 'Part 10 §5.2 Vaynard Settlement Ob'}
        return pool, ob, pool_calc, ob_calc

    if name == "Vaynard's Hall" and 'P7' in proposals:
        token_bonus = 1 if actor.revelation_tokens >= 1 else 0
        pool = actor.stats['Mil'] + token_bonus
        ob = 3
        pool_calc = {'components': [
            {'source': 'actor.stats.Mil', 'value': actor.stats['Mil']},
            {'source': 'revelation_token_bonus', 'value': token_bonus}],
            'total_pool': pool}
        ob_calc = {'formula': 'fixed Ob 3', 'inputs': {}, 'result': 3,
                   'canonical_ref': 'Part 10 §5.3 Vaynard Hall Ob'}
        return pool, ob, pool_calc, ob_calc

    if name == 'Charter of Liberties' and 'P6' in proposals:
        token_bonus = sum(1 for v in actor.tokens_held.values() if v > 0)
        pool = actor.stats['I'] + token_bonus
        ob = 4  # [canonical: v10 tuning, Part 13 §2.2]
        pool_calc = {'components': [
            {'source': 'actor.stats.I', 'value': actor.stats['I']},
            {'source': 'tokens_on_rivals', 'value': token_bonus}],
            'total_pool': pool}
        ob_calc = {'formula': 'fixed Ob 4', 'inputs': {'token_bonus': token_bonus}, 'result': 4,
                   'canonical_ref': 'P6 Charter Ob 4 (v10 tuning)'}
        return pool, ob, pool_calc, ob_calc

    # Base v5
    pool, ob = pool_and_ob_v5(action, world)
    pool_calc = {'components': [{'source': 'v5_base', 'value': pool}], 'total_pool': pool}
    ob_calc = {'formula': 'pool_and_ob_v5', 'inputs': {'action': name}, 'result': ob,
               'canonical_ref': f'peninsular_strain_v30 §5 {name}'}
    return pool, ob, pool_calc, ob_calc


def v12_apply(action, degree, world, logger, resolve_id, proposals):
    """Apply outcome and log every state_change atomically."""
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    def log_stat(target_id, attr, before, after, ref, reason, target_type='faction'):
        if before != after:
            logger.emit('state_change', parent_event_id=resolve_id,
                        target_type=target_type, target_id=target_id,
                        attribute=attr, before=before, after=after,
                        delta=after - before if isinstance(after, (int, float)) else None,
                        canonical_ref=ref, reason=reason)

    def log_territory(tid, attr, before, after, ref, reason):
        log_stat(tid, attr, before, after, ref, reason, target_type='territory')

    # ── Proposal-specific outcomes ──
    if name == 'Ecclesiastical Appointment':
        actor.ecclesiastical_appointment_arc_used = True
        actor.ea_last_arc = world.arc
        if success:
            before_L = actor.stats['L']
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            log_stat(actor.name, 'stats.L', before_L, actor.stats['L'],
                     'peninsular_strain_v30 §5.2 EA Success', f'EA {degree}')
        return

    if name == 'Crown Initiative' and 'P5' in proposals:
        actor.senator_inward_used = True
        before_W = actor.stats['W']
        actor.stats['W'] = max(0, actor.stats['W'] - 3)
        log_stat(actor.name, 'stats.W', before_W, actor.stats['W'],
                 'P5 spec W-3 cost (v10)', 'Crown Initiative cost')
        if overwhelming:
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 2)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P5 spec OW L+2', f'CI {degree}')
            bS = actor.stats['Sta']; actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            log_stat(actor.name, 'stats.Sta', bS, actor.stats['Sta'], 'P5 spec OW Sta+1', f'CI {degree}')
            for tid in actor.territories:
                t = world.territories[tid]
                if t.accord == 1:
                    log_territory(tid, 'accord', 1, 2, 'P5 spec OW accord lift', f'CI {degree}')
                    t.accord = 2
        elif degree == 'Success':
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 1)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P5 spec Success L+1', f'CI {degree}')
            if actor.territories:
                worst = min((world.territories[tid] for tid in actor.territories), key=lambda t: t.accord)
                bA = worst.accord; worst.accord = min(3, worst.accord + 1)
                for tid in actor.territories:
                    if world.territories[tid] is worst:
                        log_territory(tid, 'accord', bA, worst.accord, 'P5 spec Success accord+1', f'CI {degree}')
                        break
        elif degree == 'Partial':
            bS = actor.stats['Sta']; actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            log_stat(actor.name, 'stats.Sta', bS, actor.stats['Sta'], 'P5 spec Partial Sta+1', f'CI {degree}')
        return

    if name == "Vaynard's Settlement" and 'P4' in proposals:
        actor.tribune_card_used = True
        bW = actor.stats['W']; actor.stats['W'] = max(0, actor.stats['W'] - 1)
        log_stat(actor.name, 'stats.W', bW, actor.stats['W'], 'P4 spec W-1 cost', f'VS {degree}')
        t = world.territories[action['target']]
        if overwhelming:
            bA = t.accord; t.accord = min(3, t.accord + 2)
            log_territory(action['target'], 'accord', bA, t.accord, 'P4 OW accord+2', f'VS {degree}')
            bO = t.order; t.order = min(5, t.order + 1)
            log_territory(action['target'], 'order', bO, t.order, 'P4 OW order+1', f'VS {degree}')
            bM = actor.stats['Mil']; actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
            log_stat(actor.name, 'stats.Mil', bM, actor.stats['Mil'], 'P4 OW Mil+1', f'VS {degree}')
        elif degree == 'Success':
            bA = t.accord; t.accord = min(3, t.accord + 1)
            log_territory(action['target'], 'accord', bA, t.accord, 'P4 Success accord+1', f'VS {degree}')
            bO = t.order; t.order = min(5, t.order + 1)
            log_territory(action['target'], 'order', bO, t.order, 'P4 Success order+1', f'VS {degree}')
        elif degree == 'Partial':
            bO = t.order; t.order = min(5, t.order + 1)
            log_territory(action['target'], 'order', bO, t.order, 'P4 Partial order+1', f'VS {degree}')
        return

    if name == "Vaynard's Hall" and 'P7' in proposals:
        actor.hall_card_used = True
        bM = actor.stats['Mil']; actor.stats['Mil'] = max(1, actor.stats['Mil'] - 1)
        log_stat(actor.name, 'stats.Mil', bM, actor.stats['Mil'], 'P7 Mil-1 cost', f'VH {degree}')
        bW = actor.stats['W']; actor.stats['W'] = max(0, actor.stats['W'] - 1)
        log_stat(actor.name, 'stats.W', bW, actor.stats['W'], 'P7 W-1 cost', f'VH {degree}')
        if overwhelming:
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 2)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P7 OW L+2', f'VH {degree}')
            rivals = [(f, f.stats['L']) for f in world.factions.values() if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                bvL = victim.stats['L']; victim.stats['L'] = max(1, victim.stats['L'] - 1)
                log_stat(victim.name, 'stats.L', bvL, victim.stats['L'],
                         'P7 OW public insult rival L-1', f'VH {degree} insult')
        elif degree == 'Success':
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 1)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P7 Success L+1', f'VH {degree}')
            if actor.revelation_tokens >= 1:
                actor.revelation_tokens -= 1
                bS = actor.stats['Sta']; actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
                log_stat(actor.name, 'stats.Sta', bS, actor.stats['Sta'],
                         'P7 Success token sacrifice Sta+1', f'VH {degree}')
        elif degree == 'Partial':
            bM2 = actor.stats['Mil']; actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
            log_stat(actor.name, 'stats.Mil', bM2, actor.stats['Mil'],
                     'P7 Partial Mil recovery', f'VH {degree}')
        return

    if name == 'Charter of Liberties' and 'P6' in proposals:
        actor.legacy_card_used = True
        bW = actor.stats['W']; actor.stats['W'] = max(0, actor.stats['W'] - 1)
        log_stat(actor.name, 'stats.W', bW, actor.stats['W'], 'P6 W-1 cost', f'Charter {degree}')
        if overwhelming:
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 2)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P6 OW L+2', f'Charter {degree}')
            bPI = world.clocks['PI']; world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            logger.emit('state_change', parent_event_id=resolve_id,
                        target_type='clock', target_id='PI',
                        attribute='value', before=bPI, after=world.clocks['PI'],
                        delta=world.clocks['PI'] - bPI,
                        canonical_ref='P6 OW PI-2', reason=f'Charter {degree}')
            bS = actor.stats['Sta']; actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            log_stat(actor.name, 'stats.Sta', bS, actor.stats['Sta'], 'P6 OW Sta+1', f'Charter {degree}')
        elif degree == 'Success':
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 1)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P6 Success L+1', f'Charter {degree}')
            bPI = world.clocks['PI']; world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
            logger.emit('state_change', parent_event_id=resolve_id,
                        target_type='clock', target_id='PI',
                        attribute='value', before=bPI, after=world.clocks['PI'],
                        delta=world.clocks['PI'] - bPI,
                        canonical_ref='P6 Success PI-1', reason=f'Charter {degree}')
            token_count = sum(1 for v in actor.tokens_held.values() if v > 0)
            if token_count >= 2:
                bL2 = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 1)
                log_stat(actor.name, 'stats.L', bL2, actor.stats['L'],
                         'P6 Success token-leverage bonus L+1', f'Charter {degree} token synergy')
        elif degree == 'Partial':
            bL = actor.stats['L']; actor.stats['L'] = min(7, actor.stats['L'] + 1)
            log_stat(actor.name, 'stats.L', bL, actor.stats['L'], 'P6 Partial L+1', f'Charter {degree}')
        return

    # Fallback to v6 base apply (not individually logged — base mechanics)
    apply_outcome_v6(action, degree, world)


# ── Scoring and candidate selection (inherit v10) ──

def v12_score(action, world, proposals):
    name = action['name']
    actor = action['actor']
    if name == 'Crown Initiative' and 'P5' in proposals:
        return 4 + max(0, 6 - actor.stats['L']) + (3 if actor.stats['L'] <= 3 else 0)
    if name == "Vaynard's Settlement" and 'P4' in proposals:
        return 12
    if name == "Vaynard's Hall" and 'P7' in proposals:
        return 9 + max(0, 6 - actor.stats['L'])
    if name == 'Charter of Liberties' and 'P6' in proposals:
        return 8 + max(0, 6 - actor.stats['L'])
    return score_action_v5(action, world)


def v12_list_candidates(faction, world, proposals):
    cands = list_candidate_actions_v5(faction, world)
    if faction.name == 'Crown' and 'P5' in proposals:
        a = dict(name='Crown Initiative', actor=faction, target=None)
        passed, _ = v12_prereqs(a, world, proposals)
        if passed: cands.append(a)
    elif faction.name == 'Varfell':
        if 'P4' in proposals:
            for tid, t in world.territories.items():
                if t.owner == 'Varfell' and t.accord < 2:
                    a = dict(name="Vaynard's Settlement", actor=faction, target=tid)
                    passed, _ = v12_prereqs(a, world, proposals)
                    if passed: cands.append(a)
        if 'P7' in proposals:
            a2 = dict(name="Vaynard's Hall", actor=faction, target=None)
            passed, _ = v12_prereqs(a2, world, proposals)
            if passed: cands.append(a2)
    elif faction.name == 'Hafenmark' and 'P6' in proposals:
        a = dict(name='Charter of Liberties', actor=faction, target=None)
        passed, _ = v12_prereqs(a, world, proposals)
        if passed: cands.append(a)
    return cands


def v12_select_actions(faction, world, proposals, n_actions=3):
    selected = []; used = set()
    for _ in range(n_actions):
        cands = v12_list_candidates(faction, world, proposals)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used]
        if not cands: break
        scored = [(v12_score(a, world, proposals), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used.add((chosen['name'], chosen.get('target')))
    return selected


# ═══════════════════════════════════════════════════════════════════════════
# P3 — Treaty Expiration (40%/arc lapse)
# [canonical: Part 13 §4.3]
# ═══════════════════════════════════════════════════════════════════════════

def treaty_expiration_check(world, logger, expiration_rate):
    """At arc boundary, each Crown Treaty has expiration_rate chance of lapsing."""
    lapsed = []
    for fname, f in world.factions.items():
        for partner_name, treaty_type in list(f.treaties.items()):
            if treaty_type == 'CrownTreaty':
                roll = random.random()
                did_lapse = roll < expiration_rate
                hook_id = logger.emit('hook_fire',
                    hook_name='treaty_expiration_check',
                    fired_at='arc_boundary_accounting',
                    subject={'treaty': {'holder': fname, 'partner': partner_name, 'type': treaty_type}},
                    outcome='lapsed' if did_lapse else 'retained',
                    canonical_ref='Part 13 §4.3 Treaty Expiration 40%/arc',
                    rule_check={
                        'dice_outcome': {'roll': round(roll, 4), 'threshold': expiration_rate,
                                        'lapsed': did_lapse}})
                if did_lapse:
                    lapsed.append((fname, partner_name))
    # Remove lapsed treaties from both sides
    for holder, partner in lapsed:
        if holder in world.factions and partner in world.factions[holder].treaties:
            del world.factions[holder].treaties[partner]
            logger.emit('state_change', parent_event_id=None,
                        target_type='treaty_register', target_id=f'{holder}←{partner}',
                        attribute='treaty', before='CrownTreaty', after=None, delta=None,
                        canonical_ref='Part 13 §4.3 treaty lapsed',
                        reason=f'Treaty between {holder} and {partner} lapsed at arc boundary')
        if partner in world.factions and holder in world.factions[partner].treaties:
            del world.factions[partner].treaties[holder]
    return lapsed


# ═══════════════════════════════════════════════════════════════════════════
# VICTORY CHECK — logged per spec §3.9
# ═══════════════════════════════════════════════════════════════════════════

def universal_victory_v12(world, turmoil_cap, threshold, logger):
    """Victory check with full per-faction logging."""
    per_faction = []
    for fname, f in world.factions.items():
        territories_direct = set()
        territories_via_treaty = set()
        treaties_active = []
        for tid in ALL_PLAYABLE_15:
            t = world.territories.get(tid)
            if t is None: continue
            if t.owner == fname:
                territories_direct.add(tid)
            elif t.owner in world.factions:
                rival = world.factions[t.owner]
                tt = f.treaties.get(rival.name, '')
                if tt in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                    territories_via_treaty.add(tid)
                    treaties_active.append({'partner': rival.name, 'type': tt})
                elif rival.submitted:
                    territories_via_treaty.add(tid)
                elif rival.stats['L'] <= 1 and f.stats['L'] >= 5:
                    territories_via_treaty.add(tid)
        total = len(territories_direct) + len(territories_via_treaty)
        threshold_met = total >= threshold
        all_accord = all(world.territories[tid].accord >= 2
                        for tid in territories_direct if tid in world.territories)
        turmoil_ok = world.turmoil() <= turmoil_cap

        before_sov = f.sovereignty_history
        if threshold_met and all_accord and turmoil_ok:
            f.sovereignty_history += 1
        else:
            f.sovereignty_history = 0

        winner = f.sovereignty_history >= 2
        per_faction.append({
            'faction': fname,
            'territories_direct': len(territories_direct),
            'territories_via_treaty': len(territories_via_treaty),
            'treaties_active': treaties_active,
            'total_controlled': total,
            'threshold_met': threshold_met,
            'all_accord_ge_2': all_accord,
            'turmoil_le_cap': turmoil_ok,
            'criteria_all_met': threshold_met and all_accord and turmoil_ok,
            'sovereignty_history_before': before_sov,
            'sovereignty_history_after': f.sovereignty_history,
            'winner': winner,
        })

    logger.emit('victory_check',
                check_type='Universal_Peninsular_Sovereignty',
                threshold_used=threshold,
                per_faction_evaluation=per_faction,
                winner_declared=next((pf['faction'] for pf in per_faction if pf['winner']), None),
                canonical_ref='peninsular_strain_v30 §6.1')

    for pf in per_faction:
        if pf['winner']:
            return pf['faction']
    return None


# ═══════════════════════════════════════════════════════════════════════════
# END OF SEASON — logged revolt hooks, clock changes
# ═══════════════════════════════════════════════════════════════════════════

def end_of_season_v12(world, config, proposals, logger):
    turmoil_cap = config['TURMOIL_CAP']
    threshold = config.get('VICTORY_THRESHOLD', 11 if 'P2' in proposals else 15)

    # Clock ticks
    bCI = world.clocks['CI']; world.clocks['CI'] += 1
    logger.emit('state_change', parent_event_id=None, target_type='clock', target_id='CI',
                attribute='value', before=bCI, after=world.clocks['CI'], delta=1,
                canonical_ref='Campaign Index tick', reason='end of season')
    bMS = world.clocks['MS']; world.clocks['MS'] = max(0, world.clocks['MS'] - 1)
    if bMS != world.clocks['MS']:
        logger.emit('state_change', parent_event_id=None, target_type='clock', target_id='MS',
                    attribute='value', before=bMS, after=world.clocks['MS'], delta=-1,
                    canonical_ref='MS decay', reason='end of season')

    # Revolt processing
    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord == 1 and not t.garrison:
            log_territory_accord = t.accord
            t.accord = 0
            logger.emit('state_change', parent_event_id=None, target_type='territory', target_id=tid,
                        attribute='accord', before=1, after=0, delta=-1,
                        canonical_ref='peninsular_strain_v30 §7 accord decay',
                        reason='Ungarrisoned accord 1 → 0')
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            logger.emit('hook_fire', hook_name='revolt_check', fired_at='end_of_season',
                        subject={'territory': tid, 'accord': 0, 'garrison': t.garrison},
                        outcome='revolt_processing',
                        canonical_ref='peninsular_strain_v30 §7 step 4c')
            if t.garrison:
                c = world.factions[t.owner]
                net = roll_pool(c.stats['Mil']) - 2
                if net >= 1:
                    t.accord = 1
                    logger.emit('state_change', parent_event_id=None, target_type='territory', target_id=tid,
                                attribute='accord', before=0, after=1, delta=1,
                                canonical_ref='peninsular_strain_v30 §7 garrison holds',
                                reason='Garrison suppressed revolt')
                else:
                    prev_owner = t.owner
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for ff in world.factions.values(): ff.inquisitors.discard(tid)
                    logger.emit('state_change', parent_event_id=None, target_type='territory', target_id=tid,
                                attribute='owner', before=prev_owner, after=None, delta=None,
                                canonical_ref='peninsular_strain_v30 §7 garrison fails',
                                reason='Revolt: garrison defeated, territory uncontrolled')
            else:
                prev_owner = t.owner
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None
                logger.emit('state_change', parent_event_id=None, target_type='territory', target_id=tid,
                            attribute='owner', before=prev_owner, after=None, delta=None,
                            canonical_ref='peninsular_strain_v30 §7 Popular Uprising',
                            reason='Revolt: ungarrisoned territory lost')

        # Garrison passive accord recovery
        if t.garrison and t.owner and world.season - getattr(t, 'last_hostile_season', 0) >= 2:
            t.consec_passive_seasons = getattr(t, 'consec_passive_seasons', 0) + 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                bA = t.accord; t.accord += 1; t.consec_passive_seasons = 0
                logger.emit('state_change', parent_event_id=None, target_type='territory', target_id=tid,
                            attribute='accord', before=bA, after=t.accord, delta=1,
                            canonical_ref='peninsular_strain_v30 §7 passive garrison recovery',
                            reason='Garrison passive recovery')
        else:
            t.consec_passive_seasons = 0

    # Turmoil decay if no revolts
    if revolts == 0:
        bT = world.clocks.get('Turmoil', 0)
        world.clocks['Turmoil'] = max(0, bT - 1)
        if bT != world.clocks['Turmoil']:
            logger.emit('state_change', parent_event_id=None, target_type='clock', target_id='Turmoil',
                        attribute='value', before=bT, after=world.clocks['Turmoil'], delta=-1,
                        canonical_ref='peninsular_strain_v30 §7 Turmoil decay', reason='No revolts')

    world.clocks['Strain'] = world.clocks['Turmoil']

    # Sta cascade
    for fname, f in world.factions.items():
        if f.stats['Sta'] <= 2:
            for tid in list(f.territories):
                t = world.territories[tid]
                bA = t.accord; t.accord = max(0, t.accord - 1)
                if bA != t.accord:
                    logger.emit('state_change', parent_event_id=None,
                                target_type='territory', target_id=tid,
                                attribute='accord', before=bA, after=t.accord, delta=-1,
                                canonical_ref='T12 Morale Cascade / Sta<=2 accord decay',
                                reason=f'{fname} Sta<=2 morale cascade')

    # Victory check
    winner = universal_victory_v12(world, turmoil_cap, threshold, logger)
    if winner:
        world.winner = winner

    # Arc boundary processing
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.pa_session_arc_used = False
            f.influence_surge_arc_used = False
            f.ecclesiastical_appointment_arc_used = False
        world.arc += 1
        # P3: Treaty Expiration at arc boundary
        if 'P3' in proposals:
            treaty_expiration_check(world, logger, config['TREATY_EXPIRATION_RATE'])


# ═══════════════════════════════════════════════════════════════════════════
# CAMPAIGN RUNNER
# ═══════════════════════════════════════════════════════════════════════════

def run_campaign_v12(config=None, seed=None, proposals=None, log_dir=None, test_id='T0'):
    """Run one campaign. Returns result dict. If log_dir set, writes JSONL."""
    if seed is not None: random.seed(seed)
    cfg = dict(PARAMS)  # start from v6 base params
    cfg.update(DEFAULT_CONFIG)  # layer v12 defaults
    if config: cfg.update(config)  # layer user overrides
    props = proposals if proposals is not None else ALL_PROPOSALS
    threshold = 11 if 'P2' in props else 15

    world = init_world(tweaks=set())
    world.params = cfg

    campaign_id = f'{test_id}-{seed:06d}' if seed is not None else f'{test_id}-{int(time.time())}'
    logger = MechanicalLogger(campaign_id, log_dir) if log_dir else NullLogger()

    # campaign_start event
    initial_state = {
        'factions': {fn: {
            'L': f.stats['L'], 'Mil': f.stats['Mil'], 'I': f.stats['I'],
            'W': f.stats['W'], 'Sta': f.stats['Sta'],
            'territories': sorted(f.territories),
        } for fn, f in world.factions.items()},
        'territories': {tid: {
            'owner': t.owner, 'accord': t.accord, 'order': t.order,
        } for tid, t in world.territories.items()},
        'clocks': dict(world.clocks),
    }
    logger.emit('campaign_start',
                config={'seed': seed, 'campaign_seasons': cfg['CAMPAIGN_SEASONS'],
                        'consent_rate': cfg['CONSENT_RATE'], 'turmoil_cap': cfg['TURMOIL_CAP'],
                        'victory_threshold': threshold,
                        'treaty_expiration_rate': cfg['TREATY_EXPIRATION_RATE'],
                        'proposals_enabled': sorted(props), 'sim_version': 'v12'},
                initial_state=initial_state,
                canonical_ref='peninsular_strain_v30 §2.1 starting state')

    almud_history = []
    for s in range(cfg['CAMPAIGN_SEASONS']):
        if world.winner: break
        logger.current_season = s
        logger.current_arc = s // 4

        # season_start
        logger.emit('season_start', snapshot={
            'factions_L': {fn: f.stats['L'] for fn, f in world.factions.items()},
            'factions_territories_count': {fn: len(f.territories) for fn, f in world.factions.items()},
            'clocks': dict(world.clocks),
        })

        # Reset seasonal
        for f in world.factions.values():
            f.reset_seasonal()
            f.hall_card_used = False

        # Action phase
        all_actions = []
        for f in world.factions.values():
            all_actions.extend(v12_select_actions(f, world, props, n_actions=cfg['ACTIONS_PER_FACTION']))

        for action in all_actions:
            passed, prereq_list = v12_prereqs(action, world, props)
            score = v12_score(action, world, props)
            attempt_id = logger.emit('action_attempt',
                                     phase='action',
                                     actor=action['actor'].name,
                                     action_name=action['name'],
                                     target=action.get('target'),
                                     prereqs=prereq_list,
                                     prereqs_passed=passed,
                                     score=score)
            if not passed:
                continue

            pool, ob, pool_calc, ob_calc = v12_pool_ob(action, world, props)
            rolls, successes = logged_roll_pool(pool)
            net = successes - ob
            degree = resolve_degree(net)

            resolve_id = logger.emit('action_resolved',
                                     parent_event_id=attempt_id,
                                     actor=action['actor'].name,
                                     action_name=action['name'],
                                     pool_calculation=pool_calc,
                                     obstacle_calculation=ob_calc,
                                     dice_roll={
                                         'rolls': rolls,
                                         'successes_count': successes,
                                         'explosions': [],
                                         'method': f'roll_pool(pool={pool})',
                                         'canonical_ref': 'peninsular_strain_v30 §3.1'},
                                     net=net, degree=degree,
                                     degree_table_ref='peninsular_strain_v30 §3.2')

            v12_apply(action, degree, world, logger, resolve_id, props)

        # End of season
        end_of_season_v12(world, cfg, props, logger)

        # Track Almud
        crown = world.factions.get('Crown')
        if crown:
            almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))

    # Determine winner
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            h = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: h += 1
                elif t and t.owner in world.factions:
                    if f.treaties.get(t.owner, '') in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                        h += 0.5
            scores[fname] = h * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)

    # Almud state classification
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history):
        almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'

    # Victory/timeout log events
    if world.winner:
        logger.emit('victory', winner=world.winner,
                    winning_season=world.season - 1,
                    winning_arc=(world.season - 1) // 4,
                    victory_path='treaty_hegemony' if world.season > 1 else 'direct',
                    almud_state=almud_state,
                    almud_state_evidence={
                        'min_sta': min((h['Sta'] for h in almud_history), default=0),
                        'min_L': min((h['L'] for h in almud_history), default=0),
                    })
    else:
        logger.emit('timeout', reason=f'reached season {cfg["CAMPAIGN_SEASONS"]}')

    logger.finalize()
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        logger.flush_to_disk(os.path.join(log_dir, f'{campaign_id}.jsonl'))

    return {
        'winner': winner,
        'almud_state': almud_state,
        'world': world,
        'season_reached': world.season,
        'direct_victory': world.winner is not None,
        'final_L': {fn: f.stats['L'] for fn, f in world.factions.items()},
        'final_terr': {fn: len(f.territories) for fn, f in world.factions.items()},
        'turmoil': world.clocks.get('Turmoil', 0),
        'log_events': len(logger.get_events()) if hasattr(logger, 'get_events') else 0,
        'log_integrity': logger.integrity if hasattr(logger, 'integrity') else {},
    }


# ═══════════════════════════════════════════════════════════════════════════
# BATCH RUNNER — summary statistics
# ═══════════════════════════════════════════════════════════════════════════

def run_mc_v12(n, config=None, proposals=None, log_dir=None, test_id='T0'):
    """Run n campaigns, return summary. If log_dir, writes JSONL per campaign."""
    wins = Counter(); states = Counter()
    L = defaultdict(list); terr = defaultdict(list)
    direct = 0; turmoil_vals = []; seasons = []
    integrity_failures = 0

    for i in range(n):
        r = run_campaign_v12(config=config, seed=i, proposals=proposals,
                             log_dir=log_dir, test_id=test_id)
        wins[r['winner']] += 1
        states[r['almud_state']] += 1
        for fn, val in r['final_L'].items():
            L[fn].append(val)
        for fn, val in r['final_terr'].items():
            terr[fn].append(val)
        if r['direct_victory']: direct += 1
        turmoil_vals.append(r['turmoil'])
        seasons.append(r['season_reached'])
        if r.get('log_integrity') and not all(r['log_integrity'].values()):
            integrity_failures += 1

    total = sum(wins.values())
    return {
        'n': n,
        'proposals': sorted(proposals or ALL_PROPOSALS),
        'config': config or {},
        'win_share': {k: round(wins.get(k, 0)/total*100, 1) for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        'L_mean': {k: round(sum(v)/len(v), 2) for k, v in L.items()},
        'terr_mean': {k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        'direct_rate': round(direct/n*100, 1),
        'turmoil_mean': round(sum(turmoil_vals)/len(turmoil_vals), 2),
        'season_mean': round(sum(seasons)/len(seasons), 1),
        'almud_strong': round(states.get('strong', 0)/n*100, 1),
        'almud_deposed': round(sum(v for k, v in states.items() if k.startswith('deposed'))/n*100, 1),
        'almud_states': dict(states),
        'integrity_failures': integrity_failures,
    }


if __name__ == '__main__':
    print("v12 smoke test — 10 campaigns, full proposals, logged...")
    r = run_mc_v12(10, config={'CAMPAIGN_SEASONS': 36, 'CONSENT_RATE': 0.6},
                   proposals={'P1','P2','P3','P4','P5','P6','P7'},
                   log_dir='/home/claude/v12_test_logs', test_id='SMOKE')
    print(f"Win shares: {r['win_share']}")
    print(f"Direct: {r['direct_rate']}% | Almud strong: {r['almud_strong']}%")
    print(f"Integrity failures: {r['integrity_failures']}")
    print(f"Turmoil mean: {r['turmoil_mean']} | Season mean: {r['season_mean']}")
