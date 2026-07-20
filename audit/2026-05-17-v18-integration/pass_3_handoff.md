# VALORIA — Pass 3 Review Handoff

## Status: HANDOFF — authored 2026-05-17 by prior-chat Claude

## Scope: Anchored brief for fresh-chat Claude to execute Pass 3 (triple-pass review verdict) over Pass 2 work. The 11 Pass 2 commits + 23 editorial-ledger entries + 8 placeholder-registry entries are the review surface. This doc gives the verdict criteria, commit log with scope per commit, cross-edit composition pairs to verify, forward-flag trackers, and self-bias warnings. Pass 3 deliverable is the verdict commit; this doc supplies what Pass 3 reviewer needs without re-deriving from chat history.

---

## Bootstrap (run first in new chat)

```python
python3 - <<'BOOTSTRAP'
import os, sys, time, urllib.request, json, base64
PAT = open('/mnt/project/VALORIA_PAT').read().strip()
os.environ['GITHUB_PAT'] = PAT
open('/home/claude/.valoria_pat', 'w').write(PAT)
REPO = 'jordanelias/ttrpg'
SCRIPTS = [
    ('skills/valoria-orchestrator/scripts/github_ops.py', '/home/claude/github_ops.py'),
    ('skills/valoria-orchestrator/scripts/valoria_hooks.py', '/home/claude/valoria_hooks.py'),
]
for src, dst in SCRIPTS:
    if os.path.exists(dst) and (time.time() - os.path.getmtime(dst)) < 3600:
        continue
    req = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/contents/{src}?ref=main',
        headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'})
    with urllib.request.urlopen(req) as r:
        open(dst, 'w').write(base64.b64decode(json.loads(r.read())['content']).decode())
sys.path.insert(0, '/home/claude')
import github_ops as g, valoria_hooks as h
token = h.assert_bootstrap(); h.context_gate()
g.print_status_block(token)
BOOTSTRAP
```

Task: `audit` scope. Run `h.task_gate('audit')` after bootstrap.

---

## Pass 3 Verdict Criteria (per `<triple_pass_review>`)

Pass 3 verifies:

1. **Catalog completeness** — every Pass 1 catalog item is addressed OR deferred-with-reason
2. **No new contradictions** — no Pass 2 edit introduced a contradiction with prior canon
3. **Edits compose** — Pass 2 commits do not interact destructively (specific pairs in §4 below)
4. **Deliverable serves ask** — Pass 2 fulfills the original integration goal (mechanics integrated into modular sim armature; canon-grounded; surfacing rather than hiding contamination)
5. **Forward-flag completeness** — all surfaced forward-flags are in `canon/editorial_ledger.yaml` + `canon/placeholder_names.yaml` (count: 23 ED + 8 placeholder = 31 trackable items)

Verdict format: `[PASS-3: <APPROVE|APPROVE-WITH-FOLLOW-UP|REJECT> — <N catalog items remain, M new issues found, next action>]`

---

## Pass 2 Commit Log (the review surface)

| # | Commit | Pass | Scope | Files touched |
|---|---|---|---|---|
| 1 | `fe367105` | 2b | GD-1/2/3 canonized in `canon/02_canon_constraints.md §B` | 1 |
| 2 | `eaabf455` | 2c | HR-1 strike propagation: faction-specific victories struck across 4 design docs + canonical_sources struck entry | 5 |
| 3 | `80b4eb7e` | 2l | `sim/` armature scaffold — 72 modules across 8 subpackages, all stubs with NotImplementedError; CONVENTIONS.md + README.md | 75 |
| 4 | `d493944f` | 2j | `canon/mechanics_index.yaml` v1 (86 mechanics, 59 unique sim_modules, schema v1, 36k chars) + `tools/mechanics_index_gen.py` validator | 2 |
| 5 | `2420a193` | 2n | `designs/provincial/mass_battle_integration_v30.md` (29k) — v22-rich-port plan, 10-step migration sequence | 2 |
| 6 | `98417ac9` | 2g | `designs/personal/knots_v30.md` (23k) — unified Knot mechanic from 9 canon fragments. Surfaces TIER-DRIFT-001 + COMPOSURE-DRIFT-001 + TRUNC-DRIFT-001 | 3 |
| 7 | `3985cea0` | 2h | Royal Progress iter (`part10` §3.2 Ob formula = `max(2, floor((sum_max - sum_current)/2))`, ED-840 closed); `parliamentary_transfer_v30.md` (12.3k); `treaty_expiration_v30.md` (10.4k) | 5 |
| 8 | `6d6373c9` | 2i | `designs/world/insurgency_pipeline_v30.md` (22k) — GD-3 4-stage layered model | 3 |
| 9 | `1116d98d` | 2m | `designs/audit/2026-05-17-v18-integration/integration_plan_v18.md` (32k) — 12-phase build roadmap | 2 |
| 10 | `c65c6b1a` | Option A | `canon/placeholder_names.yaml` (8 entries) + `placeholder_names_gate` hook + `tests/hooks/test_placeholder_names_gate.py` + 2 sim module renames (`vaynards_hall` → `varfell_mandate_action`; `einhir_revival` → `varfell_territorial_acquisition`) | 9 |
| 11 | `ced90429` | 2k | 23 ED entries (ED-841..ED-863) appended; ED-788 + ED-840 archived to `editorial_ledger_archive_788_840.yaml` | 2 |

**Total commits: 11. Total files touched: ~108 (some files touched by multiple commits).**

---

## Cross-Edit Composition Pairs (§3 verdict criterion)

These pairs are the most likely interaction surfaces. Pass 3 must verify each pair composes:

| Pair | What to verify |
|---|---|
| 2b GD-1 × 2c HR-1 strike | GD-1's "sole peninsular_sovereignty victory path" matches HR-1's struck faction-specific victories. No leaked faction-victory references in `victory_v30.md`, `conviction_track_v30.md`, `complete_systems_reference.md` Part 7, `varfell_path_b_v30.md`, `canonical_sources.yaml`. |
| 2b GD-1 × 2i insurgency §7.1 | Promoted Factions (extra-parliamentary OR parliamentary) CAN win via peninsular_sovereignty per §7.1 cross-binding. GD-1 has no faction-status-gate. |
| 2b GD-2 × 2h Royal Progress iter | Royal Progress is `[Crown only]` action; GD-2 mandatory-threat-response triggers do not interfere with Royal Progress eligibility. |
| 2b GD-3 × 2h parliamentary_transfer §1.3 × 2i §4.3/§5.3 | Non-parliamentary + extra-parliamentary status blocks compose. Parliamentary Vote eligibility gate consistent across `social_contest §10`, `parliamentary_transfer §1.3`, `insurgency_pipeline §4.3/§5.3`. |
| 2c HR-1 strike × 2g knots | knots_v30 does not depend on struck faction-victory paths. Independent. |
| 2g knots × 2c HR-1 × Pass 2i RM | Latent RM doesn't gain territory; aligns with GD-1 (only formal-faction peninsular control wins). |
| 2j mechanics_index × 2l armature × 2m integration plan | All 72 sim modules in armature have entries in mechanics_index; integration plan §1.* tables match armature module list. |
| 2j mechanics_index × Option A renames | mechanics_index entry keys + sim_module paths reflect `varfell_mandate_action` / `varfell_territorial_acquisition` (not old names). |
| 2m integration plan §7.2 × Option A | §7.2 RESOLVED-via-placeholder status accurately reflects 8 entries in `placeholder_names.yaml`. |
| 2h treaty × 2h parliamentary_transfer | Treaty violation CB sources Parliamentary Transfer per `parliamentary_transfer §3` consistent with `treaty_expiration §3`. |
| 2n mass_battle_integration × 2l sim armature | `sim/provincial/massbattle.py` armature stub matches the 10-step migration plan §4 spec. |
| Pass 2k ED entries × source passes | Every forward-flag in source-pass docs has matching ED entry. Counts: 3+3+3+7+4+3 = 23, matches Pass 2k batch. |
| Pass 2k archive × architecture spec | `editorial_ledger_archive_788_840.yaml` follows `_<NNN>_<NNN>.yaml` naming convention per architecture spec §reference_files_pattern. |

---

## Forward-Flag Trackers

**`canon/editorial_ledger.yaml`** (27 active entries):
- 4 prior-open (ED-811, ED-813, ED-822, ED-823) — pre-Pass 2 work, not in scope
- 23 Pass 2 (ED-841..ED-863) — all `status: open`, `jordan_decision: pending`

**`canon/editorial_ledger_archive_788_840.yaml`** (2 archived):
- ED-788 (deferred 2026-05-09), ED-840 (closed 2026-05-17 Pass 2h)

**`canon/placeholder_names.yaml`** (8 entries):
- All `deadline_status: pending`. Hook `placeholder_names_gate` enforces lifecycle. Renamed modules (VARFELL-MANDATE-ACTION-001, VARFELL-TERRITORIAL-ACQUISITION-001) + 6 content-audit-pending entries.

---

## Self-Authored Bias Warning

Pass 3 reviews Pass 2, which prior-chat Claude authored. Per `<triple_pass_review>` self-authored corollary: bias toward under-finding issues and under-finding drift. Pass 3 reviewer MUST actively search for what prior-chat Claude was incentivized to miss:

1. **Pattern-matched plausibility instead of primitive reads.** Did Pass 2g/h/i derive claims that "sound right" without re-reading the actual canon source?
2. **Self-rationalization on PROVISIONAL flags.** Are forward-flags genuine derivations, or are they hedge-fields for claims prior Claude was uncertain about?
3. **Compositional drift undetected.** Pass 2c strike-propagation may have left fragments. Pass 2g knots may reference fields that no longer exist after strikes.
4. **Citation accuracy in Pass 2k.** Did each ED entry's `affected_docs` list actually contain the referenced section, or was it inferred?
5. **integration_plan_v18.md self-validation.** Pass 2m claims "Pass 2 content-complete" — does the claim hold against the catalog, or is it self-attestation?

**Procedural anchor:** for every claim Pass 3 considers ratifying, descend to the primitive (the actual canon file, the actual sim module, the actual ED entry text). Plan-altitude review without primitive descent reproduces prior-chat Claude's likely failure modes.

---

## Recommended Pass 3 Procedure

**Phase 1 — Read all 11 Pass 2 commit deliverables in full.**
- The 5 new design docs: `knots_v30`, `parliamentary_transfer_v30`, `treaty_expiration_v30`, `insurgency_pipeline_v30`, `mass_battle_integration_v30`
- The 1 audit doc: `integration_plan_v18.md`
- The 3 canon registries: `mechanics_index.yaml`, `placeholder_names.yaml`, `editorial_ledger.yaml`
- The 1 amended canon: `canon/02_canon_constraints.md §B`
- The 4 strike-propagation docs: `conviction_track_v30`, `varfell_path_b_v30`, `victory_v30`, `complete_systems_reference.md` Part 7
- The hook + test: `valoria_hooks.py` `placeholder_names_gate`, `test_placeholder_names_gate.py`
- The 2 renamed sim modules: `varfell_mandate_action.py`, `varfell_territorial_acquisition.py`
- `sim/CONVENTIONS.md`, `sim/README.md` for armature orientation
- (Skip 70 sim stub files; all uniform NotImplementedError per CONVENTIONS)

Use `g.read_files_graphql(paths, force_full=True)`. Token cost: substantial. Plan for ~250-350k context for the read.

**Phase 2 — Walk the 13 composition pairs in §4 above.** For each, verify the claim. Log `[VERIFIED: <pair>]` or `[ISSUE: <pair> — <description>]`.

**Phase 3 — Walk the 23 Pass 2k entries against their source docs.** For each ED: open `editorial_ledger.yaml`, find the entry, open the `affected_docs` first path, search for the forward_flag_id text. Verify the entry accurately reflects the source flag.

**Phase 4 — Walk the 8 placeholder entries against the 2 renamed module files + 6 retained-name module stubs.** Verify path + content alignment.

**Phase 5 — Emit verdict.** Format per Pass 3 criterion in §3 above. Land verdict commit at `designs/audit/2026-05-17-v18-integration/pass_3_verdict.md` with:
- Verdict line (APPROVE / APPROVE-WITH-FOLLOW-UP / REJECT)
- List of `[VERIFIED]` items
- List of `[ISSUE]` items with severity + recommended resolution
- If APPROVE-WITH-FOLLOW-UP: explicit follow-up commits required + their scope
- If REJECT: explicit rollback recommendations

**Tool budget guidance:** ~60-80 tool calls expected for Phase 1-2; ~30-50 for Phase 3-4; ~5-10 for Phase 5. Total ~95-140 tool calls. Plan for `<long_deliverable_protocol>` multi-turn split — Pass 3 will not fit in one turn.

---

## Status Declaration

[STATUS: HANDOFF READY — authored 2026-05-17 by prior-chat Claude. Pass 3 reviewer is fresh-chat Claude on the same Valoria project. Bootstrap + verdict criteria + commit log + composition pairs + forward-flag trackers + bias warning + recommended procedure all encoded. Self-bias caveat: this handoff is itself self-authored content; bias risk applies to the handoff structure as much as the content it summarizes.]
