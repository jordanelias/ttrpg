#!/usr/bin/env python3
"""tests/hooks/test_context_gate_factor.py — confirms W0.1: context_gate applies
_TOKENIZER_FACTOR (~1.35) to the char-based fetch estimate so it no longer
undercounts (finding 4C.1/K5). 40,000 chars -> 10,000 raw -> int(10,000*1.35)=13,500."""
import sys, io, contextlib
sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap
def main():
    g, h, _, _ = quick_bootstrap()
    import valoria_hooks as v
    assert getattr(v,'_TOKENIZER_FACTOR',None) and abs(v._TOKENIZER_FACTOR-1.35)<1e-9
    g._session_fetches = {'probe':'a'*40000}
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): v.context_gate()
    out=buf.getvalue()
    assert '13,500' in out, f"expected calibrated 13,500: {out!r}"
    assert '63,500' in out, f"expected total 63,500: {out!r}"
    print("PASS: context_gate applies tokenizer factor (10,000 raw -> 13,500 calibrated)")
if __name__=='__main__': main()
