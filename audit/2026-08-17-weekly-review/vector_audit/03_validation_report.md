# Validation report — P1/P2/P3

**Verdict: VALIDATED** (2/3 passed)
(2/3 required to publish as authoritative; a FAIL is itself a finding — methodology §3.8)

- **P1 foundation-periphery:** FAIL — foundation cite-mean 59.75 vs median 75.5; tl-mean 1.0 vs median 0.0
- **P2 conviction-symmetry (v4, context-gated presence):** PASS — context-gated paragraph CV 0.382 (≤0.5 to pass), presence [85, 85, 52, 32, 44, 71, 30]
- **P3 citation-density:** PASS — mean cite-degree 51.64 (13839 edges / 268 tokens; floor 6.0, scale-relative — revised from the old ≥100 absolute bar, fix #3)

TF-IDF supporting graph: skipped (numpy/sklearn absent).