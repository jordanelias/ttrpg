# Season-loop tests of PR #353's idealized code shape — 46 NPCs and every unique arc

## Status: **IN PROGRESS (2026-09-01). PROPOSED. HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Nothing here runs the game. This is an INSTRUMENT and its output, not an engine.

## Scope — the rule that decides what counts as evidence

**The only admissible source is the design chain PR #337 → now**, head =
`proposals/2026-09-01-holonic-architecture/ARCHITECTURE.md` (#353). No file under `engine/`, no
subsystem `sim/`, and no decision ratified before #337 is authority — not as support, not as
precedent, not as an incumbent to defer to. This is `ARCHITECTURE.md` §0.1's own rule, applied to
the thing measuring it.

The two case ROSTERS are the exception the same rule already carves out (§0.1 qualification 1): a
pre-#337 document may be the **subject** of a claim, never the **reason** one is correct.
`references/npc_registry.yaml` and `designs/arcs` at `v30-snapshot-2026-06-28` supply *who and what
to test*; they supply nothing about whether the shape is right.

| file | what it is |
|---|---|
| `tracer/shape.py` | **the instrument.** `ARCHITECTURE.md` implemented faithfully enough to EXECUTE — six steps, four barriers, the write matrix as a store-API parameter, the `Event` record §19 adds, the three-clause aggregation boundary, fixed point, the two topologies |
| `tracer/probes.py` | the probes. Each is a REAL EXECUTION that either completes or raises a typed `ShapeGap` |
| `tracer/run_cases.py` | the router and grader. Routes each case's `season_requires` rows onto probes |
| `tracer/test_tracer_is_honest.py` | **the instrument's own adversarial test.** 63 tests |
| `tracer/trace_log.py` | the tracing channel — every step, barrier, decision, write, act, event, claim and gap, in order |
| `cases/` | this session's completion of the case corpus (the in-chain corpus at #351 covers 27 of 46 NPCs and 51 of ~90 arcs) |
| `runs/` | `results.json` and `TRACE.txt` — the run |

## The instrument's own honesty

**Revision 1 was attacked by a read-only antagonist that never saw the producer's reasoning. THE
FIDELITY CLAIM DID NOT SURVIVE.** It found ten defects and **every one of them flattered the
shape**, which is the direction nobody notices. The three that would have changed the most:

- **The Partition was invented.** Revision 1 declared twelve `social:` rows. `ARCHITECTURE.md`
  states exactly **one** (§15.3) and declares two MISSING (§30.1). Two of the invented rows were
  the precise keys the in-chain instrument marks *deliberately absent* — adding them turns a real
  gap into a PASS.
- **`contest()` was the second resolver** — §27.2's highest-value refusal, broken inside the seam.
  It hardcoded an outcome band with no margin and named *the most recent unrelated event* as its
  cause, which is worse than `[ROOT]`: it produces a plausible, wrong arc graph **that walks**.
- **The act budget was an engine truncation**, silently discarding a person's acts beyond the
  budget. §26.3 is explicit that any such cap is *"an engine deciding a person's options"*, i.e. L1.

All ten are fixed, and **each is pinned by a regression test** so a recurrence is caught by a
machine rather than by luck. **Four revisions have now been attacked by three independent read-only antagonists and one anti-fabrication auditor, who between them found 10, 16, 16 and 14 defects.** Revisions 1 and 2 flattered the shape; revision 3's errors ran in BOTH directions, which is the more dangerous state because neither a favourable nor an unfavourable reading survives it. Every finding is fixed and pinned.

### The provenance column, which is the instrument's central honesty claim

§34 says overstating the enforcement column is the failure mode; §47 says a false claim of
enforcement is worse than none, because it stops the next reader from checking. Revision 1 had
eleven probes that **raised a gap by hand** and reported it as though the shape had refused. Every
probe now declares how its verdict was reached:

| `by=` | means |
|---|---|
| `construction` | **the shape itself raised.** The probe called a real signature and a gate, a law or a type stopped it. This is evidence |
| `no-signature` | there is nothing to call. The design supplies no function by which the thing could be attempted — which *is* the refusal, but is weaker evidence: **absence is not a guard** |
| `convention` | the shape permits it and only a reader stops it. §27.2 is the design's own example and says so out loud |
| `probe-model` | the probe supplies a model the design does not, to reach the question at all. Named so a reader can discount it |

## Two defects in the chain's own evidence base, recorded rather than fixed

The committed case corpus is the chain's evidence and this instrument **does not edit evidence**. It
works around both at load time and says so:

1. **Six of the seven in-chain case files are committed inside a markdown fence with an
   agent-transcript preamble** — they do not load with `yaml.safe_load`.
2. **`ARC3.yaml` is truncated at its head.** Its first record's `- id:` line was lost when
   committed, leaving an orphaned fragment of a third emergent case above `EMG-10`. Its rows are
   recovered under a synthetic id rather than dropped — dropping them would silently delete real
   `season_requires` needs.

## What is deliberately scoped out, declared rather than lost

`designs/arcs/arc_expansion_v30.md` holds arc *skeletons attached to named NPCs* rather than
standalone arcs. Its subject is covered by the NPC test, through each character's own
`arc_trajectory`. **A declared scoping is not a drop** (§54.3).

## What would make this done

**Under `CLAUDE.md` §0.2 a milestone is done when the behaviour EXECUTES.** The instrument executes;
**the game does not.** Nothing here is evidence that the season loop runs — only evidence about
where the specification cannot carry a case. §66's ten artifacts remain the done-conditions, and
five of them cannot be satisfied by writing.
