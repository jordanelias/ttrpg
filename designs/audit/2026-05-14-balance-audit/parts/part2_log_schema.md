# Granular Log Schema — Design Decisions, Sims, Audits
## Date: 2026-05-13 · Session: log-schema-design · Status: PROPOSED · Part 2/5
## Authority: this proposal. Ratification requires Jordan + commit to canon.
## Companion: `references/throughline_registry.md`, `canon/patch_register_active.yaml`, `canon/editorial_ledger_summary.yaml`

---

## §1 Purpose

Define a structured log format that gives every design decision, sim run, audit outcome,
and balance change a uniform audit trail with **mandatory canonical-source linkage**,
**throughline tags**, and **NERS-axis tags**. Forward-only. No retroactive backfill of
prior work.

This is the missing layer between high-level decision documents (canon, design docs,
session logs) and per-commit history (git log + PP registers). The current ecosystem
has:

- **Canon docs** — what is true now (`canon/`, `designs/`, `params/`)
- **Patch register** — what changed and why (`canon/patch_register_active.yaml`)
- **Editorial ledger** — open issues + resolved (`canon/editorial_ledger_summary.yaml`)
- **Session log** — what happened this session (`session_log_current.md`)
- **Propagation map** — what cross-doc updates remain (`references/propagation_map.md`)
- **PP / ED registers** — change IDs

Missing: a **per-event** structured record with mechanically-checkable fields. The
patch register tracks *changes-to-canon*; this schema tracks *events-that-led-to-change*
(sims, audits, observations, balance probes) plus the change itself. Most sim runs don't
produce a PP. Most audit findings don't get a canon change immediately. Without a log
layer, these accumulate as unstructured findings in long markdown docs (like the 2 prior
sims this session — 1923 lines + 852 lines) where individual findings are hard to:

- Query ("what P1 findings touch Hafenmark's Diplomat Card?")
- Cross-reference ("which throughlines does this affect?")
- Re-verify ("was this finding confirmed in a later sim?")
- Promote to canon ("which findings became PPs?")

The schema below addresses these.

---

## §2 Design Constraints

**Mechanically usable.** Hooks can grep, parse, and validate. No hand-prose-only fields.

**Mandatory canonical linkage.** Every event references at least one canonical source by
path. No floating findings.

**Throughline-tagged.** Every event references at least one T-ID or N-ID from
`throughline_registry.md`. Untagged = `[ORPHAN]` flag = design debt per the registry's
canonical purpose statement.

**NERS-axis tagged.** Every event tagged with N/E/R/S axes it implicates. Audits
explicitly score per-axis; observations may flag axes touched.

**PP/ED linkage where applicable.** When an event motivates or resolves a PP/ED, the
linkage is explicit and bidirectional (the PP register entry should back-reference the
log event).

**Compact.** Each event ~10–30 lines YAML. Long-form discussion lives in the referenced
audit/sim/session doc; the log captures the *atomic* record.

**Append-only.** Events are never edited after commit. Corrections require a new event
with `supersedes:` field; the prior event remains for audit-trail integrity.

**Schema-versioned.** `schema_version` field on every event. Schema changes are
themselves events.

---

## §3 Event Types

Five event types cover the work observed across two sims this session:

| Type | Purpose | Cardinality |
|------|---------|-------------|
| `SIM` | A sim run (Mode A/B/C/D/E/F/G per skill v30) | One per sim |
| `FIND` | An individual finding (observation, with severity) | Many per SIM |
| `TWEAK` | A proposed mechanical change (probability-tested) | Many per SIM, especially Mode B |
| `AUDIT` | An audit application (NERS, throughline, bloat, etc.) | One per audit pass |
| `DECISION` | A Jordan-authored or sim-derived design decision | One per decision |

Each type uses the same envelope (§4) and adds type-specific body fields (§5).

---

## §4 Common Envelope

Every event has these fields:

```yaml
event_id: "EVT-{YYYY-MM-DD}-{nnn}"   # sequential per day
schema_version: "1.0"
type: "SIM | FIND | TWEAK | AUDIT | DECISION"
created_at: "2026-05-13T15:42:00Z"     # ISO 8601
session: "faction-cards-stress | log-schema-design | ..."   # free text, but referenced in session_log
session_token: "a8bba7a181d9610e"      # h.assert_bootstrap() token at time of event
author: "simulator | jordan | hook | ..."
authority: "simulator-under-jordan | jordan-direct | external-audit"

# Canonical linkage — MANDATORY, at least 1 entry
canon_refs:
  - path: "designs/provincial/faction_behavior_v30.md"
    sha: "c4b6000bcc99c991f155aaf39226346ba8077a15"   # SHA at time of read; for drift detection
    section: "§3.7"                                    # optional, narrows scope
  - path: "params/bg/core.md"
    sha: "a714282b4f2404f724e5b870fc186bd78e12184d"

# Throughline linkage — MANDATORY, at least 1 entry OR explicit [ORPHAN] flag
throughlines:
  primary: ["T6", "T15a"]      # T-IDs from throughline_registry; primary = strongly implicated
  secondary: ["N2"]            # implicated but not central
  orphan: false                # true if no throughline applies → design debt flag

# NERS-axis tags — MANDATORY, at least 1 axis flagged
ners:
  axes_touched: ["necessary", "robust"]   # subset of [necessary, elegant, robust, smooth]
  directions: ["lateral", "horizontal"]   # subset of [top-down, bottom-up, vertical, diagonal, lateral, horizontal]

# Optional cross-references
pp_refs: ["PP-686-v2"]              # PPs implicated, motivating, or resolving
ed_refs: ["ED-787"]                 # EDs implicated, motivating, or resolving
supersedes: null                    # event_id this event corrects; null if novel
links: []                           # other event_ids for context

body:
  # type-specific; see §5
```

**Field-level validation rules (hook-enforced):**

- `event_id` uniqueness within day, monotonic counter
- `session_token` must match an active bootstrap from session log archives
- `canon_refs` must be non-empty; each `path` must exist in `canonical_sources.yaml`
- `canon_refs.sha` validated against current canonical SHA on commit — drift triggers warning
- `throughlines.primary + secondary + (1 if orphan else 0)` must be ≥ 1
- `ners.axes_touched` non-empty; valid values `[necessary, elegant, robust, smooth]`
- `ners.directions` valid values `[top-down, bottom-up, vertical, diagonal, lateral, horizontal]`
- `pp_refs / ed_refs` must exist in `patch_register_active.yaml` or `editorial_ledger`
- `supersedes` must reference an existing event_id if set

---

## §5 Type-Specific Body Schemas

### §5.1 `SIM` body

```yaml
body:
  sim_mode: "A | B | C | D | E | F | G"   # per skill v30
  scope: "faction-cards-stress | balance-proposals | combat-X | ..."
  systems_under_test: ["faction_layer", "victory", "ci_political"]   # keys from canonical_sources.yaml
  starting_state_hash: "sha256:..."        # hash of starting state JSON; reproducibility
  seasons_run: 6                            # for Mode C; null otherwise
  probability_engine: "exact-binomial-convolution"  # or "monte-carlo:N=10000"
  engine_validation:
    validated_against: "tests/sim/sim_factions_stress_2026_04_13.md"
    discrepancy: "within MC noise"
  outcome_summary: "{N} findings; {N} P1; {N} P2; {N} P3"
  output_doc: "/path/to/sim_output.md"      # the long-form doc
  finds: ["EVT-2026-05-13-007", ...]       # event_ids of FIND events generated
  tweaks: ["EVT-2026-05-13-040", ...]      # event_ids of TWEAK events generated
```

### §5.2 `FIND` body

```yaml
body:
  finding_id: "A-02-F1"                    # within the sim's local namespace
  severity: "P1 | P2 | P3"
  category: "ceiling | cliff | degenerate | regression | ambiguity | gap | cascade | working-as-intended | other"
  statement: "Excommunication Ob = target Leader L → dominant-faction-self-reinforces"
  mechanical_detail: "vs Crown L=5: 8.3% Succ+"
  affects_factions: ["Church", "Valorsmark"]
  affects_mechanics: ["Excommunication"]
  source_sim: "EVT-2026-05-13-002"          # back-ref to SIM event
  confirms_prior:                            # if this is a regression confirmation
    - event_id: "EVT-2026-04-13-014"
      finding_id: "F06"
    - event_id: "EVT-2026-04-09-007"
      finding_id: "A-01-F1"
  resolution_proposed: null | "EVT-2026-05-13-040"   # TWEAK event_id if accompanied
  resolution_committed: null | "PP-NNN"     # if a PP later addresses it
  status: "open | proposed-fix | resolved | superseded"
```

### §5.3 `TWEAK` body

```yaml
body:
  tweak_id: "T-01a"                          # local namespace within proposal set
  faction: "Valorsmark | Church | Hafenmark | Varfell | RM | Lowenritter | cross-faction"
  mechanism_target: "PP-433"                 # the PP being modified
  current_canon: "Each Charter: Crown L vs Ob = floor(P/2)+1"
  proposed_change: "Each additional active Charter beyond first: +1 Ob"
  probability_comparison:
    current: {pool: 5, ob: 1, p_succ_plus: 79.8}
    proposed: {pool: 5, ob: 3, p_succ_plus: 38.0}   # for 2nd Charter
  fixes:                                     # FIND event_ids this addresses
    - "EVT-2026-05-13-019"   # A-07-F1 Charter loop
    - "EVT-2026-05-13-027"   # D-02-03-F1
  priority: "P1 | P2 | P3"
  status: "proposed | playtest-pending | ratified | rejected"
  ratification: null | "PP-NNN"              # PP that ratifies the tweak
```

### §5.4 `AUDIT` body

```yaml
body:
  audit_type: "NERS | throughline | meta-throughline | bloat | propagation | other"
  scope: "what-was-audited"
  subjects: ["EVT-2026-05-13-040", "EVT-2026-05-13-041", ...]   # tweaks, sims, or docs audited
  
  # Per-axis verdicts (for NERS audits)
  ners_verdicts:
    necessary: "pass | fail | conditional"
    elegant: "pass | fail | conditional"
    robust: "pass | fail | conditional"
    smooth: "pass | fail | conditional"
    notes:
      necessary: "tweak T-01a addresses a P1 regression; necessary."
      ...
  
  # Per-direction verdicts (for NERS audits)
  directional_verdicts:
    top-down: "pass | fail | conditional"
    bottom-up: "..."
    vertical: "..."
    diagonal: "..."
    lateral: "..."
    horizontal: "..."
  
  # For throughline audits
  throughline_verdicts:
    - tweak_id: "T-01a"
      primary_throughlines: ["T9", "N2"]
      coverage: "pass"   # every tweak must touch ≥ 1 throughline
      conflict_with: []  # if tweak contradicts a throughline
      notes: "T-01a strengthens N2 sovereignty-by-governance by preventing prosperity loop dominance"
  
  meta_throughline_verdicts:                    # against throughlines_meta vetting protocol
    necessity_check: "pass"     # §0 N
    intent_check: "pass"        # §1 Ω
    mode_consistency: "pass"    # §2 Μ
    quality_check: "pass"       # §5 Q
    failure_mode: null          # §7 if any
  
  output_doc: "/path/to/audit_output.md"
  overall_verdict: "pass | fail | conditional | conditional-with-revisions"
```

### §5.5 `DECISION` body

```yaml
body:
  decision_id: "D-2026-05-13-01"
  decision_text: "4 player factions at game start; 25% ±5pp win-rate target"
  motivation: "balance-equality framing per Jordan 2026-05-13"
  affects:                                   # what changes
    canon_paths: ["designs/provincial/faction_state_authoring_v30.md"]
    eds_opened: ["ED-NEW-Crown-Valorsmark-rename"]
    pps_motivated: []
  invalidates:                               # event_ids that no longer apply
    - "EVT-2026-05-13-013"   # Guilds-finding
  status: "draft | ratified | implemented | reversed"
  author: "jordan"
```

---

## §6 Hook Integration

The schema is enforceable by extending `valoria_hooks.py`. Three new functions:

### §6.1 `h.log_event(event_dict)`

```python
def log_event(event: dict) -> str:
    """
    Validate, hash, and append an event to the running log.
    Returns event_id. Raises RuntimeError on validation failure.
    
    Validation steps:
    1. schema_version match
    2. type valid + body schema matches type
    3. canon_refs non-empty + each path in canonical_sources.yaml
    4. canon_refs SHA freshness check (warn if drift)
    5. throughlines non-empty OR orphan=true
    6. ners.axes_touched non-empty + valid values
    7. session_token matches current session bootstrap
    8. event_id uniqueness within day
    """
```

### §6.2 `h.assert_event_canon_freshness(event_id)`

```python
def assert_event_canon_freshness(event_id: str):
    """
    Re-check that all canon_refs SHAs in the event still match current canonical SHA.
    Used to detect when a finding may have been silently invalidated by canon change.
    Raises warning (not error) — auditor reviews and decides.
    """
```

### §6.3 `h.find_orphan_mechanics()`

```python
def find_orphan_mechanics() -> list:
    """
    Scan log + throughline_registry. Return mechanics referenced in FIND/TWEAK events
    that don't have throughline coverage. Per registry purpose: 'Orphan mechanics
    are design debt.' Run as part of weekly audit.
    """
```

---

## §7 Storage

**Format:** JSONL (one event per line, append-only) for machine-parsing, with parallel
YAML view for human readability.

**Path:** `logs/events/{YYYY}/{MM}/events.jsonl` for the machine view.  
**Companion:** `logs/events/{YYYY}/{MM}/events.md` rebuilt from JSONL on each commit;
human-readable summary.

**Indexing:** `logs/events/event_index.yaml` updated on each commit:

```yaml
by_date:
  2026-05-13: ["EVT-2026-05-13-001", "EVT-2026-05-13-002", ...]
by_faction:
  Valorsmark: ["EVT-2026-05-13-003", ...]
  Church: [...]
by_throughline:
  T9: ["EVT-2026-05-13-014", ...]
  N2: [...]
by_severity:
  P1: [...]
  P2: [...]
by_status:
  open: [...]
  resolved: [...]
```

Index regenerated by hook on each commit. Stale index = hook warning.

---

## §8 Example Events (Reconstructed from This Session)

For illustration only — per §1, no retroactive backfill of prior work. These show the
format for future events.

### §8.1 SIM event

```yaml
event_id: "EVT-2026-05-13-001"
schema_version: "1.0"
type: "SIM"
created_at: "2026-05-13T13:53:38Z"
session: "faction-cards-stress"
session_token: "a8bba7a181d9610e"
author: "simulator"
authority: "simulator-under-jordan"

canon_refs:
  - path: "params/bg/core.md"
    sha: "a714282b4f2404f724e5b870fc186bd78e12184d"
  - path: "params/bg/faction_actions.md"
    sha: "TBD"
  - path: "params/factions/stats_1_7_scale.md"
    sha: "e4c0912ca4540d63c369b081ebafcc7bfff86867"
  - path: "designs/provincial/faction_behavior_v30.md"
    sha: "c4b6000bcc99c991f155aaf39226346ba8077a15"
    section: "§3.7"

throughlines:
  primary: ["T7", "T9", "T12"]
  secondary: ["N1", "N2", "N6"]
  orphan: false

ners:
  axes_touched: ["necessary", "robust", "smooth"]
  directions: ["lateral", "horizontal", "diagonal"]

pp_refs: ["PP-686-v2", "PP-664", "PP-441-COR", "PP-431-COR"]
ed_refs: ["ED-787", "ED-322", "ED-172"]

body:
  sim_mode: "A+C+D"
  scope: "faction-cards-stress"
  systems_under_test: ["faction_layer", "ci_political", "victory"]
  probability_engine: "exact-binomial-convolution"
  engine_validation:
    validated_against: "tests/sim/sim_factions_stress_2026_04_13.md"
    discrepancy: "within MC noise (engine 11.9% vs prior MC 14% on SIM-FAC-01)"
  outcome_summary: "85 findings: 19 P1, 31 P2, 35 P3; 9 gap-register entries; 2 confirmed regressions"
  output_doc: "/mnt/user-data/outputs/sim_faction_cards_stress_2026-05-13.md"
```

### §8.2 FIND event

```yaml
event_id: "EVT-2026-05-13-019"
schema_version: "1.0"
type: "FIND"
created_at: "2026-05-13T13:55:00Z"
session: "faction-cards-stress"
session_token: "a8bba7a181d9610e"
author: "simulator"

canon_refs:
  - path: "params/bg/faction_actions.md"
    section: "Crown — Royal Charter"
  - path: "designs/provincial/peninsular_strain_v30.md"

throughlines:
  primary: ["T9"]        # Church Infrastructure Pipeline (Charter weaponized against Seizure)
  secondary: ["N2"]      # Sovereignty Is Governance, Not Conquest
  orphan: false

ners:
  axes_touched: ["robust"]
  directions: ["horizontal"]   # temporal — multi-season Charter loop

pp_refs: ["PP-433"]

body:
  finding_id: "A-07-F1"
  severity: "P1"
  category: "stacking"
  statement: "Crown Charter is a territory-stat modifier; self-reinforcing positive loop for Crown wealth accumulation"
  mechanical_detail: "Crown 5D vs Ob 1 (Charter+capital floor) = 79.8% Success+ indefinitely"
  affects_factions: ["Valorsmark"]
  affects_mechanics: ["Royal Charter", "Govern", "Trade"]
  source_sim: "EVT-2026-05-13-001"
  confirms_prior: []
  resolution_proposed: "EVT-2026-05-13-101"   # T-01a tweak
  status: "open"
```

### §8.3 TWEAK event

```yaml
event_id: "EVT-2026-05-13-101"
schema_version: "1.0"
type: "TWEAK"
created_at: "2026-05-13T15:14:00Z"
session: "balance-proposals"
session_token: "d55778f18ce240aa"
author: "simulator"

canon_refs:
  - path: "params/bg/faction_actions.md"

throughlines:
  primary: ["T9", "N2"]
  secondary: []
  orphan: false

ners:
  axes_touched: ["robust", "elegant"]
  directions: ["horizontal"]

pp_refs: ["PP-433"]

body:
  tweak_id: "T-01a"
  faction: "Valorsmark"
  mechanism_target: "PP-433"
  current_canon: "Each Charter: Valorsmark L vs Ob = floor(territory P/2)+1"
  proposed_change: "Each additional active Charter beyond the first imposes +1 Ob on subsequent Charter plays by Valorsmark that season"
  probability_comparison:
    current_2nd_charter: {pool: 5, ob: 2, p_succ_plus: 60.0}
    proposed_2nd_charter: {pool: 5, ob: 3, p_succ_plus: 38.0}
    current_3rd_charter: {pool: 5, ob: 2, p_succ_plus: 60.0}
    proposed_3rd_charter: {pool: 5, ob: 4, p_succ_plus: 19.8}
  fixes:
    - "EVT-2026-05-13-019"   # A-07-F1
    - "EVT-2026-05-13-027"   # D-02-03-F1
  priority: "P1"
  status: "proposed"
  ratification: null
```

### §8.4 AUDIT event

```yaml
event_id: "EVT-2026-05-13-200"
schema_version: "1.0"
type: "AUDIT"
created_at: "2026-05-13T16:00:00Z"
session: "ners-and-throughline-audit"
session_token: "TBD"
author: "simulator"

canon_refs:
  - path: "references/throughlines_meta.md"
  - path: "designs/audit/2026-04-30-architecture-session/01_week_audit_NERS.md"

throughlines:
  primary: ["T9"]
  secondary: []
  orphan: false

ners:
  axes_touched: ["necessary", "elegant", "robust", "smooth"]
  directions: ["top-down", "bottom-up", "vertical", "diagonal", "lateral", "horizontal"]

pp_refs: ["PP-674"]

body:
  audit_type: "NERS+throughline"
  scope: "Part 4/5 audit of corrected balance proposals"
  subjects: ["EVT-2026-05-13-101", "EVT-2026-05-13-102", ...]
  
  ners_verdicts:
    necessary: "pass"
    elegant: "pass"
    robust: "conditional"
    smooth: "pass"
    notes:
      necessary: "tweak set addresses 10 P1 findings; necessary"
      elegant: "all tweaks are minimal Ob-modifier or scope-restriction edits"
      robust: "diminishing returns mechanic adds strategic depth; conditional on UI making the penalty visible"
      smooth: "tweaks integrate with existing PP-431-COR / PP-189 / PP-686 v2 cleanly"
  
  directional_verdicts:
    top-down: "pass"
    bottom-up: "pass"
    vertical: "conditional"   # see notes
    diagonal: "pass"
    lateral: "pass"
    horizontal: "pass"
  
  throughline_verdicts:
    - tweak_id: "T-01a"
      primary_throughlines: ["T9", "N2"]
      coverage: "pass"
      conflict_with: []
      notes: "T-01a strengthens N2 sovereignty-by-governance"
  
  meta_throughline_verdicts:
    necessity_check: "pass"
    intent_check: "pass"
    mode_consistency: "pass"
    quality_check: "pass"
    failure_mode: null
  
  output_doc: "/mnt/user-data/outputs/audit_2026-05-13.md"
  overall_verdict: "conditional-with-revisions"
```

### §8.5 DECISION event

```yaml
event_id: "EVT-2026-05-13-300"
schema_version: "1.0"
type: "DECISION"
created_at: "2026-05-13T15:30:00Z"
session: "errata-and-corrections"
session_token: "3f66c99fe5775c5a"
author: "jordan"
authority: "jordan-direct"

canon_refs:
  - path: "designs/provincial/faction_state_authoring_v30.md"
    sha: "TBD"

throughlines:
  primary: ["N6"]   # Institutions Are Characters
  secondary: ["T15a", "T15b", "T15c"]
  orphan: false

ners:
  axes_touched: ["necessary"]
  directions: ["top-down"]

body:
  decision_id: "D-2026-05-13-01"
  decision_text: "4 player factions at game start: Valorsmark (Crown), Church, Hafenmark, Varfell. RM + Löwenritter background/NPC. Win-rate target 25% ±5pp per player faction."
  motivation: "Game-design decision; balance-equality framing"
  affects:
    canon_paths: ["designs/provincial/faction_state_authoring_v30.md"]
    eds_opened: ["ED-NEW-Crown-Valorsmark-rename"]
    pps_motivated: []
  invalidates:
    - "EVT-2026-05-13-013"   # any Guilds-as-player findings
  status: "ratified"
  author: "jordan"
```

---

## §9 Migration Path

**Stage 0 (pre-adoption):** This proposal sits in `/tests/sim/` or `proposed/` until
ratified.

**Stage 1 (schema ratification):** Jordan reviews, suggests edits, ratifies.
Schema becomes canonical; commit to `references/log_schema_v1.md` (or wherever).

**Stage 2 (hook integration):** `valoria_hooks.py` gains `log_event`,
`assert_event_canon_freshness`, `find_orphan_mechanics`. Test suite added.

**Stage 3 (storage init):** `logs/events/` directory initialized; empty JSONL files.
First DECISION event = schema ratification itself.

**Stage 4 (forward use):** All new sims, audits, tweaks, decisions go through
`log_event`. Long-form output docs (the actual sim/audit markdown) reference
event_ids and link back.

**Stage 5 (~6 months):** Review of orphan-mechanics flag; review of canon-freshness
drift warnings; refactor as needed.

**No backfill of prior work.** The 114 findings across this session's two sims
remain in their long-form docs. If a future event references them, it cites the doc
path and finding ID (e.g., `sim_faction_cards_stress_2026-05-13.md#A-02-F1`) — the
event itself is novel, citing prior work as motivation.

---

## §10 Open Items

- **Schema field for "playtest evidence":** TWEAK events may want a `playtest_runs:`
  field once tweaks reach prototyping. Defer to v1.1.
- **Confidence metric:** events from sim/audit may want `[CONFIDENCE: high|medium|low]`
  field. Currently lives in body free-text; could promote to envelope.
- **Multi-session events:** an audit spanning multiple sessions needs a `session: []`
  array rather than single string. Defer to v1.1 if encountered.
- **Cross-repo events:** when `valoria-game` (Godot implementation) commits affect the
  log, the schema may need `repo:` field. Defer to v1.1.
- **Auto-tagging:** an LLM tagger could propose throughline tags from event text. Risky
  for canonical-linkage accuracy. Defer; manual or explicit.

---

## §11 Sign-off Required

This schema is **PROPOSED**. To proceed to Stage 1 (ratification):
1. Jordan reviews §§3–8 and §6 (hook integration).
2. Adjusts field set, valid values, or storage path.
3. Confirms `references/log_schema_v1.md` (or alternative path) as canonical destination.
4. A DECISION event records the ratification (manually written; first event in the system).

Once ratified, this proposal itself becomes the schema's documentation — the long-form
spec — and the JSONL/YAML log layer begins.

---

*Session: log-schema-design · 2026-05-13 · Part 2/5 · Author: simulator under Jordan*
