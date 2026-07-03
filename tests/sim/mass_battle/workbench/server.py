"""Mass-Battle Workbench backend — a tiny stdlib HTTP server. No external deps, no build step.
(Mirrors designs/scene/combat_engine_v1/workbench/server.py's pattern.)

Run:  python tests/sim/mass_battle/workbench/server.py   then open http://localhost:8766
      A bare run now visualizes the COORDINATE FIELD — FIELD_MOVEMENT/PC_NODE_COHESION default ON
      since the ED-1089 flip (Jordan-ratified 2026-07-02). To visualize the legacy integer-grid
      oracle instead: FIELD_MOVEMENT=0 PC_NODE_COHESION=0 python tests/sim/mass_battle/workbench/server.py

IMPORTANT — mode is fixed at process start. PER_CELL / FIELD_MOVEMENT / PC_NODE_COHESION are read
from os.environ once at import time and star-imported into every consumer module as INDEPENDENT
copies (Python's `from X import *` binds a value, not a live reference) — so there is no way to
switch modes for a single running server. To compare grid vs field, run two server instances (two
ports) with different env. GET /api/mode reports what THIS process is actually running.

Endpoints (all JSON except GET /):
  GET  /              -> the single-page app (static/index.html)
  GET  /api/mode      -> {per_cell, field_movement, pc_node_cohesion} — this process's fixed config
  GET  /api/presets   -> named scenario presets (mirrors gauge_mb.py's TESTS/CAV_TESTS matchups)
  GET  /api/roster-options -> {shapes, troop_types, roles_by_troop_type, subunit_cap, battlefield_size}
                         — [Stage E] the live registries (geometry.CELL_PATTERN_FN,
                         troop_types.TROOP_TYPE_STATS, roles_for per type, engine.SUBUNIT_CAP), so
                         the Army Configuration Mode UI never hardcodes a second copy of a shape/role
                         list that would drift out of sync with the engine (e.g. after a future LC-8-
                         style shape retirement).
  POST /api/trace     -> {a:{...build_unit spec...}, b:{...}, seed, kind, max_battle_turns}
                         -> one traced battle: {winner, events, a:{summary}, b:{summary}}
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # tests/sim
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from trace import run_traced_battle
from mass_battle import config as _cfg
from mass_battle.hierarchy import units as _units
from mass_battle import geometry as _geo
from mass_battle.troop_types import registry as _troop_registry
from mass_battle.engine import SUBUNIT_CAP

_STATIC = os.path.join(os.path.dirname(__file__), 'static')

# HTTP status codes — protocol constants, not sim-mechanical values.
HTTP_OK = 200            # [canonical: RFC 9110 §15.3.1]
HTTP_BAD_REQUEST = 400   # [canonical: RFC 9110 §15.5.1]
HTTP_NOT_FOUND = 404     # [canonical: RFC 9110 §15.5.5]
HTTP_SERVER_ERROR = 500  # [canonical: RFC 9110 §15.6.1]

DEFAULT_PORT = 8766  # arbitrary local dev port (scene-combat's workbench uses 8765; avoid collision if both run)

# Named presets mirroring gauge_mb.py's TESTS/CAV_TESTS (a convenience subset, not a re-export —
# gauge_mb.py is a sibling harness script, not a package module this workbench depends on).
#
# [LC-8, ED-909, Jordan-approved 2026-07-02: "correct, retire them. those are emergent outcomes."]
# 'Horseshoe'/'RefusedFlank' are retired as Subunit.shape values; H4/C4 below now build the real
# Unit-level 'Envelopment' composition (a held center + two wide-placed wings released into 'envelop'
# on a timer — trace._build_side's 'preset':'envelopment' dispatch, mirroring bat.py's/gauge_mb.py's
# own _envelop_army helper) instead of a single subunit stamped with a fixed Horseshoe cell pattern.
_R = _cfg.SIDE_A_START_ROW  # [canonical: config.py SIDE_A_START_ROW]
_ENVELOP_CENTER = [{'shape': 'Line', 'starting_position': (_R, 9)}]
_ENVELOP_WINGS = [{'shape': 'Line', 'starting_position': (_R, 3)}, {'shape': 'Line', 'starting_position': (_R, 15)}]
_ENVELOP_WINGS_CAV = [{'shape': 'Line', 'troop_type': 'cavalry', 'speed': 'Fast', 'starting_position': (_R, 3)},
                      {'shape': 'Line', 'troop_type': 'cavalry', 'speed': 'Fast', 'starting_position': (_R, 15)}]

# Side-B mirrors, for genuinely symmetric multi-subunit-vs-multi-subunit scenarios (both sides field
# 3 independently-tasked subunits at once, not just an attacker with a lone-subunit defender) — this
# is what actually exercises the Unit-level command layer (build_army/orders/escort) on both sides.
_RB = _cfg.SIDE_B_START_ROW  # [canonical: config.py SIDE_B_START_ROW]
_ENVELOP_CENTER_B = [{'shape': 'Line', 'starting_position': (_RB, 9)}]
_ENVELOP_WINGS_B = [{'shape': 'Line', 'starting_position': (_RB, 3)}, {'shape': 'Line', 'starting_position': (_RB, 15)}]
_REFUSED_STRONG = [{'shape': 'Line', 'starting_position': (_R, 5)}]
_REFUSED_REFUSED = [{'shape': 'Line', 'starting_position': (_R, 13)}]  # [canonical: sim_verification_ledger.json — CALIBRATED, workbench deployment spacing, not historically cited]

PRESETS = [
    {'id': 'H1', 'label': 'Line vs Line (mirror)', 'a': {'shape': 'Line'}, 'b': {'shape': 'Line'}},
    {'id': 'H4', 'label': 'Envelopment vs Arrowhead (Cannae)',
     'a': {'preset': 'envelopment', 'center': _ENVELOP_CENTER, 'wings': _ENVELOP_WINGS},
     'b': {'shape': 'Arrowhead'}},
    {'id': 'H7', 'label': 'GappedLine vs Line (manipular)', 'a': {'shape': 'GappedLine'}, 'b': {'shape': 'Line'}},
    {'id': 'C4', 'label': 'Cavalry envelop vs Line',
     'a': {'preset': 'envelopment', 'center': _ENVELOP_CENTER, 'wings': _ENVELOP_WINGS_CAV},
     'b': {'shape': 'Line'}},
    {'id': 'C2', 'label': 'Cavalry vs braced Line (repel)', 'a': {'shape': 'Arrowhead', 'troop_type': 'cavalry', 'speed': 'Fast'},
     'b': {'shape': 'Line', 'stance': 'hold', 'discipline': 8, 'instructions': ['brace']}},  # [canonical: mass_battle_gauge_grounding.md §3 — C2 braced repels; raw cav-a LOW]
    {'id': 'R1', 'label': 'Ranged vs Line (open field)', 'a': {'shape': 'Line', 'unit_type': 'ranged', 'stance': 'hold'}, 'b': {'shape': 'Line'}},
    {'id': 'M3', 'label': 'Envelopment vs Envelopment (symmetric, 3v3 subunits)',
     'a': {'preset': 'envelopment', 'center': _ENVELOP_CENTER, 'wings': _ENVELOP_WINGS},
     'b': {'preset': 'envelopment', 'center': _ENVELOP_CENTER_B, 'wings': _ENVELOP_WINGS_B}},
    {'id': 'OBL', 'label': 'RefusedFlank vs Envelopment (oblique order, 2v3 subunits)',
     'a': {'preset': 'refused_flank', 'strong': _REFUSED_STRONG, 'refused': _REFUSED_REFUSED},
     'b': {'preset': 'envelopment', 'center': _ENVELOP_CENTER_B, 'wings': _ENVELOP_WINGS_B}},
]


def do_trace(req):
    a = dict(req['a']); b = dict(req['b'])
    seed = int(req.get('seed', 0))
    kind = req.get('kind', 'multi')
    max_battle_turns = int(req.get('max_battle_turns', 8))  # [canonical: mass_battle_v30.md §A.7 — battle-turn cap]
    return run_traced_battle(a, b, seed=seed, kind=kind, max_battle_turns=max_battle_turns)


def do_mode():
    return {'per_cell': bool(_cfg.PER_CELL), 'pc_node_cohesion': bool(_cfg.PC_NODE_COHESION),
            'field_movement': bool(_units.FIELD_MOVEMENT),
            'battlefield_size': _cfg.BATTLEFIELD_SIZE}


# [Stage E] Troop types the Army Configuration Mode UI offers — the canonical §B.2 taxonomy
# (TROOP_TYPE_STATS) plus the two generic legacy types ('infantry'/'cavalry') every existing preset
# and gauge row already uses. Not just TROOP_TYPE_STATS.keys() alone: those two generics carry no
# stat preset (they inherit the Unit's own power/discipline/morale, exactly as build_unit's own
# troop_type='infantry' default does) but are real, load-bearing options a deployer should be able
# to pick — omitting them would make the UI strictly less capable than the API it drives.
_ROSTER_TROOP_TYPES = sorted(set(_troop_registry.TROOP_TYPE_STATS) | {'infantry', 'cavalry'})


def do_roster_options():
    return {
        'shapes': sorted(_geo.CELL_PATTERN_FN.keys()),
        'troop_types': _ROSTER_TROOP_TYPES,
        'roles_by_troop_type': {tt: _troop_registry.roles_for(tt) for tt in _ROSTER_TROOP_TYPES},
        'subunit_cap': SUBUNIT_CAP,
        'battlefield_size': _cfg.BATTLEFIELD_SIZE,
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype='application/json'):
        data = body if isinstance(body, bytes) else json.dumps(body).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            with open(os.path.join(_STATIC, 'index.html'), 'rb') as f:
                return self._send(HTTP_OK, f.read(), 'text/html; charset=utf-8')
        if self.path == '/api/mode':
            return self._send(HTTP_OK, do_mode())
        if self.path == '/api/presets':
            return self._send(HTTP_OK, PRESETS)
        if self.path == '/api/roster-options':
            return self._send(HTTP_OK, do_roster_options())
        return self._send(HTTP_NOT_FOUND, {'error': 'not found'})

    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0))
        try:
            req = json.loads(self.rfile.read(n) or b'{}')
        except Exception as e:
            return self._send(HTTP_BAD_REQUEST, {'error': f'bad json: {e}'})
        try:
            if self.path == '/api/trace':
                return self._send(HTTP_OK, do_trace(req))
        except Exception as e:
            return self._send(HTTP_SERVER_ERROR, {'error': f'{type(e).__name__}: {e}'})
        return self._send(HTTP_NOT_FOUND, {'error': 'not found'})


def main(port=DEFAULT_PORT):
    srv = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    m = do_mode()
    print(f"Mass-Battle Workbench -> http://localhost:{port}  (Ctrl-C to stop)")
    print(f"  mode: PER_CELL={m['per_cell']} FIELD_MOVEMENT={m['field_movement']} "
          f"PC_NODE_COHESION={m['pc_node_cohesion']}  battlefield={m['battlefield_size']}")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT)
