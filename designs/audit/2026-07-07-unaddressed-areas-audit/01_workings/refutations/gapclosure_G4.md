# Gap-closure G4 — misc doc verifications

_Archived verbatim from the agent's final message (2026-07-07)._

# G4 Gap-Closure Report — Unaddressed-Areas Audit

## 1. C-INJ primary-source gap: does `valoria_authoritative_graph_v1.md` §2 match scale_transitions §12.4?

**Verdict: MATCHES — no material addition or alteration.** §12.4 is a faithful, compressed restatement of the graph's top-down table, and explicitly cites it as its source.

Evidence:
- `designs/architecture/scale_transitions_v30.md:332`: "eight cross-band down-seams / fifteen type-edges... `domain_actions -> {npc_behavior, piety_track, settlement_economy}`, `faction_politics -> npc_behavior`, `peninsular_strain -> {npc_behavior, settlement_economy, settlement_layer}`, `scenario_authoring -> settlement_layer`. ... Reference: `designs/audit/2026-06-11-orchestration/valoria_authoritative_graph_v1.md` §2."
- `designs/audit/2026-06-11-orchestration/valoria_authoritative_graph_v1.md:37-47`: the 8-row seam table sums to exactly 15 type-edges across the same 4 families (domain_actions ×3 targets, faction_politics ×1, peninsular_strain ×3 targets, scenario_authoring ×1) — an exact match, family-for-family and count-for-count.
- The graph's ruling J-1 offered two options (`:48`, "(a) declare engine-mediated delivery canonical + A6-exempt... or (b) author a §3 down-rule"); scale_transitions §12.2 (`:321`) resolved with option (a) verbatim ("Engine-mediated Key delivery is therefore the sole canonical cross-scale delivery channel... A bespoke top-down delivery channel is not to be authored"). Consistent, not contradictory.
- One item in the graph (`:35`, "19 = raw assessor count incl. near-lateral seam 9 `scene_slate→piety_track`") is *not* repeated in §12.4 — but the graph itself already excludes seam 9 from its own canonical 8/15 count (labels it "near-lateral," bracketed separately), so the omission is consistent, not a material drop.

## 2. C-INJ Godot gap: `miraculous_event` / `scenario_authoring` in `designs/godot/`

**Verdict: CONFIRMED empty.** `grep -r "miraculous_event|scenario_authoring" designs/godot/` returns zero matches. The near-certainly-empty assumption holds.

## 3. C-REACH indirection gap: dynamic dispatch in `sim/`

**Verdict: does NOT undermine the ISLAND verdicts.** Full grep of `sim/` for `getattr(`, `importlib`, `globals()[`, `__import__`:
- `importlib`: 0 hits. `globals()[`: 0 hits. `__import__`: 0 hits.
- `getattr(`: 98 hits, all in production `sim/*.py` files (`sim/personal/combat.py`, `sim/thread/*.py`, `sim/provincial/*.py`, `sim/territory/infrastructure.py`, `sim/personal/contest/*.py`, etc.).

Disposition, hit by hit (grouped): the overwhelming majority (96/98) are `getattr(obj, 'field_name', default)` — plain attribute-with-fallback reads on data objects (actor stats, faction fields, world containers) inside already-reached production modules. This is data access, not call routing; it cannot create a hidden caller edge to an otherwise-unreached module. **Not ordering-relevant.**

The 2 exceptions that fetch-and-call are both in one test file, not production code:
- `sim/tests/test_sigma_leverage_parity.py:83`: `getattr(SL, fn_name)(*args, **kwargs)` — dispatches by name into `sim/autoload/sigma_leverage.py`.
- `sim/tests/test_sigma_leverage_parity.py:88`: `getattr(_m1, fn_name)(*args, **kwargs)` — dispatches into the external numpy reference `m1_dice_sigma_core`.

Neither `sigma_leverage.py` nor `m1_dice_sigma_core` appears in the C-REACH ISLAND/ORGAN/STUB matrix, and both are test-only call sites (no bearing on production reachability). One more introspective (non-calling) use: `sim/personal/contest/_kernel_tests.py:483`: `_inspect.getsource(getattr(_modes_mod, _fn))` — fetches source text for a test assertion, never invokes it.

**Conclusion for C-REACH's own "honest gap" (`cluster_C-REACH.md:93`, "did not grep for getattr/importlib/globals()[ repo-wide to formally rule it out"): now formally ruled out.** No dynamic dispatch in `sim/` hides a production caller of any ISLAND-verdicted module (contest kernel, personal combat, threadwork, settlement layer, parliamentary_vote, Varfell/Hafenmark political actions, articulation, npc_ai).

## 4. C-MBSE ED-IN-0014 citation gap: "registry §10 already flags two of the three"

**Verdict: NOT stale/fabricated — mis-located, not miscited.** `key_type_registry_v30.md §10` (`:1026-1043`, "Extension Process") is indeed generic boilerplate, as `cluster_C-MBSE.md:111,158` already found ("could not corroborate"). But the "`[registry §10 candidate]`" annotation is a real, recurring tag used elsewhere — in `references/module_contracts.yaml`'s `gap_notes` fields — and it demonstrably flags **exactly two of ED-IN-0014's three targets**:
- `ci_political`: `references/module_contracts.yaml:641` — "ZERO Key integration in a CANONICAL doc... CI=100 Theocracy Unification Attempt (§2.2) is unkeyed **[registry §10 candidate]**." Cross-referenced in `designs/audit/2026-06-10-godot-conversion-strategy/godot_conversion_strategy_v1.md:64` and `designs/audit/2026-06-11-orchestration/valoria_authoritative_map_v1.md:71`.
- victory era/occupation transitions: `references/module_contracts.yaml:679` — "world-state era transitions... are UNKEYED... **[registry §10 candidate]**." Cross-referenced in `godot_conversion_strategy_v1.md:65`, `dossier_articulation.md:39-43` ("tracked — ED-1006... registry SS10 candidates"), and `canon/editorial_ledger.jsonl:392` (ED-1006: "4 unkeyed CANONICAL/DESIGN systems (territorial_piety, ci_political, victory era transitions, npc Procedure C projects) as registry SS10 candidates").
- `settlement_layer` (Order/L-PS drift, revolt, undefended auto-capture): **not** found tagged `[registry §10 candidate]` anywhere in `module_contracts.yaml` or elsewhere in the corpus — consistent with being the one-of-three left unflagged.

So "two of the three" is accurate; ED-IN-0014's citation just means "registry §10" loosely (candidate-for-§10-extension, tagged in `module_contracts.yaml`), not literally the registry doc's own §10 section. Recommend the fork docket note the citation should point at `module_contracts.yaml:641,679` (+ ED-1006), not `key_type_registry_v30.md §10`.

## 5. Registry YAML-validity census

Ran `yaml.safe_load` (Python, read-only) against every ` ```yaml ` fenced block in `designs/architecture/key_type_registry_v30.md`. Found **49** total fenced blocks (block 1 is the §1 generic "Type Format" template, not a per-type entry; blocks 2–49 = the **48 per-type entries** the task refers to).

**Result: exactly 1 failure — `scene.gossip` — all other 47 per-type blocks (+ the template) parse cleanly.**

- **FAIL**: `### scene.gossip`, lines 968–985. `yaml.safe_load` raises `ScannerError: mapping values are not allowed here` at line 979: `default_visibility: semi_public_observers=propagation_observers (initial: principals only)` — the unquoted scalar contains an embedded `: ` sequence (`initial: principals`) that YAML parses as a nested mapping key. This is the known case cited in the task and matches ED-1006's note ("registry scene.gossip yaml block malformed", `canon/editorial_ledger.jsonl:392`).
- All other 47 entries (`scene.dialogue` through `state.concern_resolved`) parse successfully under strict `safe_load`.

## 6. C-VERIFY duplicate-ED corroboration: ED-IN-0012 / ED-IN-0013

Confirmed by direct scan of `canon/editorial_ledger.jsonl`. Both IDs appear **twice**, from two different audit sources landed in two different PRs:

| ID | Line | `source` field (quoted) |
|---|---|---|
| ED-IN-0012 (1st) | **597** | `"designs/audit/2026-07-05-fable5-social-contest-audit/fable5_social_contest_audit_v1.md SS3-SS4; references/throughlines_complete.md:121-200; designs/ui/valoria_ui_ux_v4_1.md:592-649"` |
| ED-IN-0013 (1st) | **598** | `"designs/audit/2026-07-05-fable5-social-contest-audit/fable5_social_contest_audit_v1.md SS2.5; designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md:6-19; sim/personal/contest/resolver.py:33-42"` |
| ED-IN-0012 (2nd) | **599** | `"designs/audit/2026-07-05-edge-playability-audit/edge_playability_audit_v1.md"` |
| ED-IN-0013 (2nd) | **600** | `"designs/audit/2026-07-05-edge-playability-audit/edge_playability_audit_v1.md"` |

The first pair (lines 597-598) is from the fable5-social-contest-audit (PR #80, "throughline citation refresh" / "rolling-engine re-verdict"); the second pair (lines 599-600) is from the edge-playability-audit (PR #81, "registry-by-rendering sweep" / "GM-token sweep") — genuinely distinct content colliding on the same ID via two separate ratify-all merges.

## 7. C-NPC "Cardinal Reichard" staleness gap

**Verdict: the naming finding is STILL LIVE — a genuine, unresolved cross-doc inconsistency, not stale.** `cluster_C-NPC.md:72` flagged this as "genuinely uncertain" since it wasn't found in `npc_behavior_v30.md`. Resolving that uncertainty:

- `references/npc_registry.yaml:547-569` (NPC-037) documents the **correction**: `first_name: Annalie`, `last_name: Reichard`, `faction: Crown (Inner Circle)` — "CORRECTED: was listed as Church/Cardinal — actually Crown Lord Treasurer per faction_canon" — with explicit note `:569`: `"Crown Lord Treasurer. Cardinal Reichard STRUCK."` and `status: canonical  # verified per faction_canon_v30 (ED-634 naming pending)`.
- `designs/npcs/npc_behavior_v30.md:360` (Status: CANONICAL) already carries the **corrected** name: `Lord Treasurer | Annalie Reichard`.
- But `designs/personal/conviction_migration_roster_v30.md:137` (Status: **CANONICAL**) still presents `#### Cardinal Reichard (per artifact 15 sample)` as a live "Senior cardinal archetype" for the Ecclesiastical/Cathedral faction — with no strike-through, correction note, or pointer to NPC-037/Annalie.
- `designs/npcs/npc_relational_graph_v30.md:473,475` (Status: PROVISIONAL) also still uses `Cardinal Reichard` twice in its geographic-strain distance table.
- `canon/editorial_ledger.jsonl:516` — ED-634 (status: **open**, needs_jordan: true) explicitly tracks "Crown inner-circle names (Voss, **Reichard**, Thale, Linder, Kreutz)... confirm names" — confirming the naming question is still open, not resolved.

**Conclusion:** two CANONICAL/PROVISIONAL docs (`conviction_migration_roster_v30.md`, `npc_relational_graph_v30.md`) still carry a name (`Cardinal Reichard`) that `npc_registry.yaml` has explicitly marked STRUCK and corrected to `Annalie Reichard` (Crown, not Church), and `npc_behavior_v30.md` already uses the corrected name — while the tracking ticket (ED-634) remains open. The orphan-audit's naming finding is confirmed still live, not stale.
