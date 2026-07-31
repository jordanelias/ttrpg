# Audit-family critique — which families are load-bearing, and what the staleness metric actually measures

**Date:** 2026-07-30 · **Lane:** IN · **ED:** ED-IN-0099 · **Status:** FILED — findings, with three
recommendations held for Jordan
**Trigger:** the SessionStart banner reports six families stale (vector-audit 240 files, decisions-digest
76, proposals-register 54, apparatus-registry 29, graph-lexicon 12, mechanics-index 9). Filed as P8 during
the W4 gate as *"needs Jordan's call on which are load-bearing"*; this is the evidence for that call.

**Everything below was measured against the working tree, not inferred from the code's own comments.**
Where a claim came from reading rather than running, it says so.

---

## §0 — The finding, in one paragraph

The vector audit **is** the thing that identifies what is missing, and nothing else in the repo computes
it. Its findings are also **near-stationary**: over 8 days and 240 files of in-scope churn they moved
**3 rows out of 178**, in the improving direction. Both facts are true at once, and the staleness
metric conflates them. A freshness warning on a stationary backlog measures the wrong axis — it says
*"re-run a script"* when the real message is *"178 structural gaps have gone unworked."* The number that
should reach the banner is the **backlog**, not the **drift**.

---

## §1 — Two axes, not one

The original P8 framing scored families on a single "load-bearing" axis and got the answer wrong, because
two independent questions were being asked at once:

| axis | question | what it tells you |
|---|---|---|
| **Content value** | if this artifact vanished, what capability is lost? | whether to keep the family |
| **Staleness informativeness** | does "N files changed" predict that the artifact's content has changed? | whether to keep the *warning* |

They are uncorrelated here. `vector-audit` is **highest** on content value and **lowest** on staleness
informativeness. Scoring it on one number produced "LOW", which was wrong in the way that mattered.

---

## §2 — Per-family findings

Executable consumers were separated from prose citations by grepping for actual read patterns and then
**reading each hit** — a plain filename grep produced 8 apparent consumers for artifacts that turned out
to have one or none.

### 2.1 vector-audit — `tools/observability/audit_findings.json`

- **Generator:** `skills/valoria-vector-audit/scripts/vector_audit.py --emit-findings` (~70s).
- **Executable consumer:** exactly one — `tools/observability/build_incompleteness.py:507`
  (`scan_audit_structural`), with a `schema_version: 2` handshake that degrades **loudly** on mismatch.
- **Content:** 7 diagnostic modes, 178 rows at measurement time. Representative and specific:
  - `implied_missing` (35) — system pairs sharing ≥2 meta-links with no direct connection, e.g.
    `Campaign Architecture ↔ Faction Layer`, `Clocks ↔ Faction Layer`, `CI Political ↔ Clocks`. Each row
    names both docs.
  - `isolates` (7) — tokens declared **canonical** in a registry with `doc: null` and degree 0:
    `Active Inquisition`, `Counter-Intelligence`, `NPC Relational Graph`.
  - `notional` (100), `cascade_sinks` (15), `sparse_context` (15), `vocab_debt` (3),
    `throughline_orphans` (0).
- **The staleness caveat:** both production paths — `.github/workflows/dashboard.yml:83` and
  `audit-refresh.yml:83` — **regenerate the feed immediately before consuming it**. The committed copy is
  never the version those pipelines use. It matters only when `build_incompleteness.py` is run standalone.
- **VERDICT: content value HIGH — the unique capability in this list. Staleness informativeness LOW.**

### 2.2 decisions-digest — `tools/observability/decisions.json`

Feeds `DECISIONS.md` + `decisions_data.js` → the dashboard's "needs your decision" inbox. Refreshed by the
weekly cron. **Value MEDIUM** (it is Jordan's inbox), **staleness MEDIUM** — a mid-week warning is
ordinary drift, not neglect.

### 2.3 proposals-register — `tools/observability/proposals.json`

Same shape, plus a **live test coupling**: `tests/valoria/test_build_proposals.py` pins the proposals-doc
count, so adding anything to `proposals/` reddens a test until the assert is bumped. **Value MEDIUM,
staleness MEDIUM.** (This is why the present document lives in `audit/`, which is not pinned.)

### 2.4 apparatus-registry — `references/apparatus_registry.yaml`

Read by `build_incompleteness.py`. **`tools/review_core.py` does NOT read it** — the apparent hit is a
comment (`review_core.py:52`, "All are existing CLIs (has_cli in …)"). Its orphan flags fed W4's OI-15/16
**retirement decisions**, so stale evidence here has consequences; W4 mitigated by re-running the ED-1082
greps independently. **Value MEDIUM-LOW, staleness MEDIUM** — and a regen is already owed at W5.

### 2.5 graph-lexicon — `graph.json` + `lexicon.json`

- `graph.json` is read at `vector_audit.py:1653` to enrich a **name vocabulary**, guarded by
  `if g else []` — it degrades to empty.
- **`tools/ci_naming_check.py` does NOT consume `lexicon.json`.** It appears in that tool's **skip-list**
  (`ci_naming_check.py:70`) because generated glossaries carry deprecated aliases as data. It is an
  exclusion, not an input — the opposite of the load-bearing reading a filename grep suggests.
- **STALE DOCSTRING FOUND.** `vector_audit.py:1215-1222` states its key-graph is pinned as a subset of
  `build_graph`'s `graph.json` by a CI drift guard. **That coupling no longer exists**: the guard was
  rewritten as `test_key_graph_matches_an_independent_rederivation_from_contracts`, whose own docstring
  says it "depended on graph.json being co-fresh with module_contracts… **no graph.json dependency**".
  The comment still advertises the removed dependency. *(Fix not applied here — see §5.)*
- **Value LOW, staleness LOW.**

### 2.6 mechanics-index — `registers/mechanics_index.yaml`

The odd one out, and the most actionable. **It has no generator.** It is hand-authored, so drift is
genuine editorial debt that no script can clear. It is read by `structure_audit.py`, cited by
`vector_audit.py`, its 88 `sim_module:` rows were the leverage for W4's OI-54 contract↔code join, and
`mechanics_index_gen.py --strict` validates its schema in CI on every push (a *different* concern —
schema validity, not content currency). **Value HIGH, staleness HIGH** — the smallest number on the
banner and the only one where the number means what it appears to mean.

### 2.7 npc-audit — `audit/lane-a/2026-06-22-npc-comprehensive-audit.md`

Currently fresh, so absent from the banner. Structurally different from all six above: the artifact is an
**authored document**, not a generated file. "Stale" here means *a human must re-audit*, which shares no
remedy with "re-run a script" while sharing the warning vocabulary.

---

## §3 — Three defects in the metric itself

**D1 — it measures the wrong event.** Drift is computed from the artifact's **last git commit**
(`_family_base`), not its last regeneration. A regeneration that produces identical content commits
nothing, so drift accumulates forever and the family reports "stale" while being provably current.
*Tested:* regeneration currently **does** change content (decisions 228→225 items, proposals 252→259,
apparatus/decisions/proposals ≈674 insertions / 462 deletions), so D1 is not firing today — but the
failure mode is live and silent when it does.

**D2 — the weekly cron is nominally weekly, actually 1-in-3.** Exactly **one** scheduled refresh has ever
landed: `4029870`, PR #244, 2026-07-27 — the only commit in history matching the bot's own message
`"Scheduled decisions-digest + proposals + apparatus refresh"`. The workflow has existed since ~07-11
(Mondays 07-13, 07-20, 07-27). `vector-audit` and `graph-lexicon` last moved on **07-22** and were not
updated by the 07-27 run. Their artifacts are otherwise updated *incidentally*, by sessions doing
unrelated work. No `audit-refresh/*` branch is pending on the remote.

**D3 — scope over-breadth manufactures the headline numbers.** `vector-audit`'s scope is
`systems/ engine/ canon/ arcs/ audit/ references/` + the patch register — most of the repo. Any session
trips it. "240 in-scope files changed" is not 240 changes that would move the artifact; measured against
the actual delta, 240 files of churn produced **3 changed rows**. The maintainers already know this
failure mode — the code carries a prior correction removing `godot/` and `proposals/` for exactly this
reason — so this is the same defect recurring at a larger scope, not a new one.

---

## §4 — Which families are part of the vectorization review

Asked directly, because the shared refresh workflow implies a coherence that does not exist. Only three of
the six touch `skills/valoria-vector-audit/`:

| family | relation to the vector audit |
|---|---|
| **vector-audit** | **IS its output** — `--emit-findings` writes the feed the Incompleteness Ledger reads |
| **graph-lexicon** | **soft input** — `graph.json` supplies known names at `vector_audit.py:1653`, degrades to empty |
| **mechanics-index** | **cited input** to both `vector_audit.py` and `structure_audit.py` |

**`decisions-digest`, `proposals-register` and `apparatus-registry` are not part of it at all.** They are
the *governance* observatory — a separate pipeline that merely shares `audit-refresh.yml`. Presenting all
six under one banner heading is the reason the block reads as undifferentiated noise.

---

## §5 — Recommendations (HELD for Jordan — none executed)

1. **Invert what vector-audit reports.** Replace `"stale: N in-scope files changed"` with the backlog:
   `"35 implied-missing · 7 isolates · 100 notional — unchanged in 8 days"`. The queue not moving is the
   signal; the file's age is not. **Do not demote the family** — an earlier draft of this analysis
   recommended demoting it to info, and that was wrong for the reason §1 gives.
2. **Promote mechanics-index.** Only family where no script can fix the drift.
3. **Fix D1** by stamping a `_generated_at` into each artifact and measuring drift from that.
4. **Suppress the three cron-managed families between Mondays**, or print "next scheduled refresh: Monday"
   so mid-week drift reads as expected rather than as rot.
5. **Reclassify npc-audit** as an authored document — different remedy, should not share the vocabulary.
6. **Investigate D2** — a 1-in-3 landing rate is the difference between a working automation and a
   decorative one.
7. **Fix the stale docstring** at `vector_audit.py:1215-1222` (§2.5). Left unfixed here deliberately: it is
   a `skills/valoria-vector-audit/` file and this document is a read-only critique.

---

## §6 — Limits of this critique

- **`notional` (100) is untriaged.** It is the largest bucket and this analysis did not determine whether
  those rows are genuine debt or deliberate placeholders. The claim "178 open structural gaps" should be
  read as "**42 sharp** (35 implied-missing + 7 isolates) **+ 136 needing triage**", not 178 actionable.
- **Single-run measurement.** The 178→175 delta is one regeneration at one commit. It shows the findings
  are stationary *over this window*; it is not a claim about long-run behaviour.
- **Consumer analysis is static.** Readers were found by grep-then-read. A dynamic import or a
  `getattr`-built path would be missed — the same blind spot CLAUDE.md §0.1 #5 notes for grep-based sweeps.
- **Three of this analysis's own starting hypotheses were wrong** and were corrected by checking:
  `ci_naming_check` consuming `lexicon.json` (it excludes it), `review_core` reading
  `apparatus_registry.yaml` (comment only), and a `graph.json`-pinned CI drift guard (removed). Recorded
  because the same filename-grep shortcut that produced them is available to the next reader.

---

## §7 — Reproduce

```bash
# the backlog + the stationarity claim (~70s)
python3 skills/valoria-vector-audit/scripts/vector_audit.py --repo-root . \
    --emit-findings /tmp/af_fresh.json
python3 -c "import json;d=json.load(open('/tmp/af_fresh.json'));print({k:len(v) for k,v in d.items() if isinstance(v,list)})"
# ...then diff against the committed tools/observability/audit_findings.json

# D1 — does regeneration actually change content?
python3 tools/observability/build_decisions.py && git diff --stat tools/observability/decisions.json

# D2 — has any scheduled refresh ever landed?
git log --all --oneline --grep="Scheduled decisions-digest"

# the family table itself
python3 tools/audit_staleness.py
```
