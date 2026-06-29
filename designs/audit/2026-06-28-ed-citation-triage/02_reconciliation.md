# ED-Citation Integrity — Full Reconciliation (2026-06-29)

_Closes the backlog surfaced in `00_triage.md` / `01_recommendations.md`. The validator gate
`ED Citation Integrity` went from **292 report-only violations → 0**, and is now **blocking** in CI._

## Why the violations existed (diagnosis)

`tools/validate_ed_citations.py` flags ED references in canonical docs that don't resolve to a real,
non-open ledger entry. Of the 292:

- **286 were `NONEXISTENT`** — citations to ED numbers never written to `canon/editorial_ledger.jsonl`
  (verified absent from active **and** archives). Root cause: **dual ledger-of-record drift** — design
  docs minted ED numbers and recorded decisions in their own inline `[EDITORIAL:]` tables, and the
  2026-05-28 YAML→JSONL migration harvested the standalone ledger YAMLs but not those inline tables.
- **6 were `OPEN_AS_BASIS`** — of which **2 were false positives** (a validator precedence bug; see below)
  and 4 were genuine (open EDs cited as canonical basis).

The mechanisms were **legitimate flags of a real provenance break**, not validator noise — except for
two genuine validator defects found and fixed here.

## What was done

### Track A — validator correctness (`tools/validate_ed_citations.py`)
Three defects fixed (all reduce false positives; none can mask a real violation):
1. **Active ledger now authoritative.** Archives were appended *after* the active JSONL, so a stale
   archived `ED-864: open` overwrote the active `struck` (→ false `OPEN_AS_BASIS`). Archives now load
   first, active last.
2. **No silent swallow + salvage.** 7 frozen archive YAMLs are malformed (split-fragment indentation);
   the loader used a bare `except: continue`, silently shrinking the "active + archives" universe to
   active-only. It now surfaces the failures (stderr) and **regex-salvages** their IDs (553 recovered,
   all redundant with active — so 0 effect on the count, but the universe is now honest).
3. **Basis detection scoped to the citation's own line.** A 90-char window bled across table-row
   boundaries, counting a neighbour row's `**RESOLVED.**` as if it qualified an open-ED citation
   (the ED-509 false positive). New regression tests cover precedence, salvage, and row-bleed.

### Track B — grounded ledger reconciliation (`canon/editorial_ledger.jsonl`)
**91 entries registered** for the 92 missing EDs (1 was a fix-citation, not a registration). Each
disposition was **verified against the citing doc's recorded decision** by per-batch subagents
(anti-fabrication: `resolved` only where a decision is actually recorded; otherwise open/provisional).

| Disposition | Count | Basis |
|---|---|---|
| `resolved` | 36 | decision recorded in-doc (e.g. fieldwork ED-496–506, companion ED-555/557/559/571, Cardinal arcs ED-591–594) |
| `provisional` | 12 | Claude-made defensible call awaiting review (e.g. NPC stat assignments ED-393/395–398, PP-284 combat rules ED-173/177/178) |
| `open` | 30 | genuine unanswered question raised inline (e.g. lifepath ED-379–382, arc-conditioner proposals ED-603–609) |
| `open` + `needs_jordan` | 13 | creative/design-intent only Jordan can set (NPC naming ED-595–602/610/634, ED-885 ratification) |

Every new entry carries `reconciled_2026_06_28` + a `source` (doc:line) for audit.

### Track C — citing-doc fixes (18 files)
- **ED-814 → ED-907** repointed (the self-declared phantom; 7 occurrences across
  `pc_formation_system.md` + `mass_battle_shape_echelon_revamp.md`).
- **Over-claims reworded** to honest `pending`/`proposed` qualifiers so open/provisional EDs are no
  longer cited as canonical basis (demotes `OPEN_AS_BASIS` → `OPEN_INFO`) — e.g. the uncorroborated
  "ED-591–609 approved" line, "characterization canonical per ED-393–401", "PT canonical per ED-644".
  No fabricated resolutions.

### Track D — gate flipped
`ed-citations` dropped `continue-on-error` and added to `ci-summary` needs → **blocking**.

## Findings worth flagging (for Jordan)
- **ID collisions** surfaced: ED-408–411 mean different things in `arcs_36_40.md` (resolved arc items,
  registered here) vs `baralta_crown_claim_v30.md` (crown-claim mechanics); ED-413/417/647 are similarly
  reused. The registered entries use the dated/decision-bearing meaning; the collided second uses are a
  latent cleanup item.
- **13 `needs_jordan` items** are now `open` in the ledger with a flag — NPC naming (Crown inner circle
  ED-634, Cardinal/Warden arcs ED-595–602), the Baralta successor (ED-610), and ED-885 (a never-written
  ratification ID whose real authority is plausibly ED-874 — confirm or repoint).
- The 7 malformed archive YAMLs are salvaged at runtime but not repaired; the validator prints a WARNING
  each run until the source YAML is fixed (low priority — content fully recovered).
