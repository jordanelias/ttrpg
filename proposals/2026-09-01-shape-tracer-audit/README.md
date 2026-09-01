# Shape-tracer audit — PR #351, and the forward doctrine it produced

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 every document here is **REFERENCE, never mechanism.**

A read-only audit of PR #351 (merge `32bd13e`), an adversarial review of that audit, and the
resolution / configuration / testing doctrine derived from both. **No repository file was modified by
the audit itself**; artifacts touched during execution testing were restored and verified clean, and
the tree was confirmed byte-identical to `32bd13e` including ignored `__pycache__` residue.

| file | what it is |
|---|---|
| `00_AUDIT.md` | the audit of PR #351's shape tracer, corrected after adversarial review, with its evidence appendix |
| `01_FORWARD_DOCTRINE.md` | resolution (the four kinds), configuration (declare, don't route), testing (three tiers, anti-vacuity, controls) |

## Method

Five read-only Fable lanes over the tracer (`valoria-critic` — read-only **by agent definition**, no
Write/Edit/Bash, so independence is structural rather than declared), covering: primitives and
ownership; logic, flexibility and scalability; harness honesty; data and provenance; repository
integration. Then **three adversarial lanes attacking the audit itself** for factuality, inference
and methodology. Then re-verification by execution of every load-bearing claim.

Execution verification was done by the orchestrating session, since read-only critics structurally
cannot run anything. That division is also the audit's own biggest methodological weakness — the
headline finding was discoverable *only* by execution, so the five-lane fan-out bought breadth on
secondary surfaces while the decisive test ran single-threaded. Recorded in `00_AUDIT.md` §8.

**Findings the review overturned are struck rather than deleted**, so the correction record stays
legible. Four published claims did not survive: a fabrication charge (withdrawn in full), a
"CI reaches none of it" absolute, two precision figures the evidence did not support, and an
unsupportable superlative. The decisive control run the original audit failed to run was then
performed, and it made the verdict **more favourable** to PR #351, not less.

⚠ **No `ED` was allocated.** Under `CLAUDE.md` §0's amendment an adversarial pass may append at most
one ledger row, and only if it needs a human decision. The escalations this work identifies are named
in `01_FORWARD_DOCTRINE.md` §6 and are deliberately **not** filed here — filing is a separate act.
