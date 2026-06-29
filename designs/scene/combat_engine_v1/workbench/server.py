"""Combat Workbench backend (WS-6) — a tiny stdlib HTTP server. No external deps, no build step.

Run:  python designs/scene/combat_engine_v1/workbench/server.py   then open http://localhost:8765

Endpoints (all JSON except GET /):
  GET  /                -> the single-page app (static/index.html)
  GET  /api/params      -> the class-aware tuning surface (Class A read-only / B / C editable / M method)
  POST /api/trace       -> {scenario, overrides, seed} -> one traced fight: {result, narration, events}
                           each branch-node event carries `dist` (alternate branches + odds) for the explorer
  POST /api/montecarlo  -> {scenario, overrides, trials, seed} -> win-rate +/- Wilson CI, position-swapped
  POST /api/promote     -> {overrides} -> a reviewable Class-C patch + ledger stub (writes nothing)
  POST /api/save_preset -> {name, overrides} -> persists a named scratch overlay
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import numpy as np
import wrapper
from combatant import Combatant
import presets, probabilities as P, narrate
from trace import run_traced_fight

_STATIC = os.path.join(os.path.dirname(__file__), 'static')
_FIGHTER_FIELDS = ('strength', 'agi', 'end', 'cog', 'att', 'spirit', 'focus', 'history', 'disp')


def _make_fighter(spec, default_label):
    kw = {f: int(spec.get(f, 4 if f in ('strength', 'agi', 'end') else 3)) for f in _FIGHTER_FIELDS}
    kw['disp'] = int(spec.get('disp', 4))
    return Combatant(spec.get('label', default_label),
                     weapon=spec.get('weapon', 'arming'), armor=spec.get('armor', 'light'),
                     tradition=spec.get('tradition', 'none'), **kw)


def _wilson(w, n, z=1.96):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = w / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = (z * (p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (round(p, 4), round(max(0.0, c - h), 4), round(min(1.0, c + h), 4))


def do_trace(req):
    cfg = presets.effective_cfg(req.get('overrides'))
    seed = int(req.get('seed', 0))
    A = _make_fighter(req['scenario']['A'], 'A')
    B = _make_fighter(req['scenario']['B'], 'B')
    result, events = run_traced_fight(A, B, cfg=cfg, seed=seed)
    for e in events:                      # attach the alternate-branch distribution to each node
        d = P.node_distribution(e)
        if d is not None:
            e['dist'] = d
    return {'result': result, 'narration': narrate.render(events, seed=seed), 'events': events,
            'winner': (A.label if result == 1 else B.label if result == -1 else None)}


def do_montecarlo(req):
    cfg = presets.effective_cfg(req.get('overrides'))
    trials = int(req.get('trials', 1000))
    seed = int(req.get('seed', 0))
    specA, specB = req['scenario']['A'], req['scenario']['B']
    rng = np.random.default_rng(seed)
    a_wins = decided = draws = 0
    half = trials // 2
    for i in range(trials):
        swap = i >= half                  # position-swap to cancel first-mover; A's win-rate is symmetric
        X = _make_fighter(specB if swap else specA, 'A')
        Y = _make_fighter(specA if swap else specB, 'B')
        r = wrapper.fight(X, Y, cfg, rng)
        if swap:
            r = -r
        if r == 1:
            a_wins += 1; decided += 1
        elif r == -1:
            decided += 1
        else:
            draws += 1
    p, lo, hi = _wilson(a_wins, decided)
    mirror = abs(round(50 * (1 - abs(2 * (a_wins / decided - 0.5))) if decided else 0, 1))  # inform/diagnostic
    return {'trials': trials, 'decided': decided, 'draws': draws,
            'A_winrate': p, 'ci_lo': lo, 'ci_hi': hi,
            'A_label': specA.get('label', 'A'), 'B_label': specB.get('label', 'B')}


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
                return self._send(200, f.read(), 'text/html; charset=utf-8')
        if self.path == '/api/params':
            return self._send(200, presets.param_surface())
        return self._send(404, {'error': 'not found'})

    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0))
        try:
            req = json.loads(self.rfile.read(n) or b'{}')
        except Exception as e:
            return self._send(400, {'error': f'bad json: {e}'})
        try:
            if self.path == '/api/trace':
                return self._send(200, do_trace(req))
            if self.path == '/api/montecarlo':
                return self._send(200, do_montecarlo(req))
            if self.path == '/api/promote':
                return self._send(200, presets.promote_diff(req.get('overrides', {})))
            if self.path == '/api/save_preset':
                path = presets.save_scratch(req['name'], req.get('overrides', {}))
                return self._send(200, {'saved': os.path.basename(path)})
        except Exception as e:
            return self._send(500, {'error': f'{type(e).__name__}: {e}'})
        return self._send(404, {'error': 'not found'})


def main(port=8765):
    srv = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    print(f"Combat Workbench -> http://localhost:{port}  (Ctrl-C to stop)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8765)
