# EVIDENCE — the working artifacts this session's claims rest on

## Status: **PROPOSED (2026-09-02). HELD BACK IN FULL.** Reference only; nothing here runs.

**Committed because the claims elsewhere in this directory are unverifiable without them.** These
were session scratch files; a scratchpad is not a durable location, and a finding whose evidence
lives only in a temporary directory is a finding the next reader must take on trust.

## `instrument_history/shape_rev1.py`

**Revision 1 of the tracer — the artifact the FIRST antagonist's ten findings are ABOUT.**

`tracer/shape.py` carries a retraction record naming ten defects *"and every one of them flattered
the shape"*. **That record is a claim about a file, and this is the file.** Without it a reader can
check that revision 4 does the right thing but cannot check that revision 1 did the wrong thing —
so the ten findings, and the whole argument built on them, would rest on assertion.

Verifiable directly against it: the twelve-row invented Partition (including `(Person, convictions)`
and `(Person, beliefs)`, the keys the in-chain instrument marks *deliberately absent*); `contest()`
computing a band with no margin and citing the most recent unrelated Event; `deliberate()`
truncating a person's act list; `sense()` returning a constant `standing`; the wear rate, `//60`
and `confidence=1` sitting in bodies.

⚠ **It is superseded and must not be read as the instrument.** `tracer/shape.py` is.

## `extraction_sources/`

**The source texts and build scripts for the 46 arc cases this session added**, taken from
`git show 6311caa8d132281a52033dea8159408d155137c9:designs/arcs/…` — the `v30-snapshot-2026-06-28`
ref Jordan identified as the arc corpus's home.

| file | what it is |
|---|---|
| `original.md`, `resolved.md` | `gm_ref/arcs_46_55{,_resolved}.md` → cases `ARC-46`…`ARC-55`. **The resolved file is the later, corrected version and several arcs are renamed or rebuilt in it**; the cases follow it |
| `emg_c.md`, `emg_x.md` | `emergent_campaign_arcs.md`, `emergent_arcs_experimental.md` → `EMG-C1`…`C4`, `EMG-X5`…`X8` |
| `nsc.md` | `narrative_scenario_chains.md` → `NSC-01`…`NSC-09`. **`NSC-01` is STRUCK at source (PP-675)** and was extracted in full anyway, because a struck arc still says what its author expected the engine to do |
| `emergent_scenarios.md` | the 15 scenarios + four cross-scenario feedback loops → `SCN-01`…`SCN-15`, `SCN-LOOP-A`…`D` |
| `build_arc6*.py`, `part*.json` | the staged build of `cases/ARC6.yaml` |

**Why these are committed rather than re-fetched:** the ref is reachable today, but §2's working-tree
rule and the chain's own experience with evacuated trees both say a claim should not depend on a
fetch. The id namespacing (`ARC-R16`…`R19` vs `ARC-16`…`18`) is only checkable against the sources.

> ⚠ **THE FINDING THESE SOURCES CARRY, and it is why the arc extension mattered:** the in-chain
> corpus covered **51 of ~97** unique arcs. Across the corpora it never touched, the ending
> distribution is markedly weaker on the axis L1 cuts along — and **three of the four cross-scenario
> feedback loops name no off-switch at all**, with the fourth's counter-action strippable by the
> loop's own downstream instability. That corroborates §40.1's termination debt **from the corpus
> side**, which no reading of the design could have produced.
