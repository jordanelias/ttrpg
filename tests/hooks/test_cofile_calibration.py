#!/usr/bin/env python3
"""
tests/hooks/test_cofile_calibration.py

Confirms the W0.8 calibration of the design-doc co-file gate in pre_commit_gate:
  - Editing an EXISTING (already-registered) design doc without canonical_sources
    in the commit -> non-blocking advisory (commit proceeds).
  - Adding a NEW design doc without canonical_sources -> hard error (registration).

Integration-style: real bootstrap + real task_gate + real canon content, so
editorial/size checks pass and only the co-file path-existence logic is exercised.
Run: python3 tests/hooks/test_cofile_calibration.py
"""
import sys, io, contextlib
sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap

def main():
    g, h, _, _ = quick_bootstrap()
    h.task_gate('infrastructure')
    existing = 'designs/architecture/key_substrate_v30.md'
    newpath  = 'designs/architecture/zzz_cofile_probe_v30.md'
    content = g.read_files_graphql([existing]).get(existing, '') or "<!-- version: vTEST -->\n# probe\n"

    def run(adds):
        buf = io.StringIO(); err = None
        with contextlib.redirect_stdout(buf):
            try:
                h.pre_commit_gate(adds, [])
            except Exception as e:
                err = str(e)
        return buf.getvalue(), err

    out_edit, err_edit = run([(existing, content)])
    out_new,  err_new  = run([(newpath, content)])

    assert 'CO-FILE advisory' in out_edit, "existing-doc edit should print advisory"
    assert not (err_edit and 'CO-FILE: NEW' in err_edit), "existing-doc edit must not be co-file-blocked"
    assert err_new and 'CO-FILE: NEW design docs' in err_new, "new design doc must hard-error on registration"
    print("PASS: co-file calibration (existing->advisory, new->hard error)")

if __name__ == '__main__':
    main()
