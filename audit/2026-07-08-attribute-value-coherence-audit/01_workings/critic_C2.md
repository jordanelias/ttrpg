# Critic pass — C2 (Derived values)

Antagonist relay over `dossier_C2.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C2-F1 | **soften** (P1→P2) | Verified real and NEW (ED-FA-0004, editorial_ledger.jsonl:359, covers only sim/ + two design-doc headers, not params/ prose). But the canonical definition is not ambiguous where it matters: CURRENT.md:39 routes settlement/territory to settlement_layer_v30.md (correct formula), and no engine/typed-export path reads params/factions_personal.md or params/bg/* (CLAUDE.md §5). Textbook "stale carrier surface" = P2 under the rubric's own wording. |
| C2-F2 | **soften** (P1→P2) | Verified: params/core.md:158 still (End+6)×(MW+1) vs derived_stats_v30.md §4.1 + combatant.py (ED-1021). But the same cell's Notes column says "See derived_stats_v30.md §4.1 as authoritative" — a reader is routed correctly. Stale carrier, not undecidable definition; P2 for consistency with F1. |
| C2-F3 | **sharpen** (P1 stands, worse than claimed) | Both lines inside the SAME §7 (header combat_v30.md:281): :298 (not :301) states the ED-PC-0005 fractional-Ob reversal; :307's Hybrid paragraph still asserts the superseded −1D. Crucially, ED-PC-0005's ledger entry (editorial_ledger.jsonl:377) claims "combat_v30.md §7/§10... rewritten" — falsified by :307 sitting unfixed inside the §7 it claims to have rewritten. The "resolved" status is partially false. |
| C2-F4 | **uphold** | Word-for-word: derived_stats_v30.md:382 "Not canonicalized"; module_contracts.yaml:558,575-600 gates the same three derived values live (g_dv0, writable:false); settlement_layer_v30.md §1.3 presents them as settled citing a nonexistent source; ledger grep 0 hits. Ratification-status gap, P2 right. |
| C2-F5 | **uphold** | Direct read: params/core.md:154-165 table has no Concentration row despite §5.2 + params/contest.md:140 defining it on equal footing with Composure (present). |
| C2-F6 | **uphold** | registry:107 derived_values has no Face entry despite Face being formula-distinct (Face_max=Cha×3; Face_current=round(Standing/10×Face_max), params/contest.md:137,144). ED-SC-0011 (only same-day SC ED) is scene_dispatch routing — not already tracked. |
| C2-F7 | **uphold** | "derived_stats_v1 §4" cited verbatim; no such file; real §4 is personal combat, settlement values live at §9. Double-wrong citation. |
| C2-F8 | **uphold** | key_substrate_v30.md stat_deltas schema is bare `<stat_name>: <delta>` free text; no registry cross-check anywhere in the doc. Correctly scoped cluster-wide. |
| C2-F9 | **uphold** | params/core.md:162 is the Thread Fatigue row; no Concentration row exists — the census's F-SIM-01 "Charisma×3 third formula" citation is wrong; Concentration coherent everywhere it appears. |
| C2-F10 | **uphold** | Spot-checked params/contest.md:133-151 and name_collision_database.yaml:463 — accurate, correctly not re-litigated. |
| C2-U1 | **uphold** | Pure propagation of a Jordan-ratified formula (LPS-2e, 2026-05-30); correctly fed to FA (ED-FA-0004 adjacency). |
| C2-U2 | **soften** (process nit) | Substance compliant (propagation of ED-1021), but "a fresh ED citing ED-826 recurrence" ignores the mandatory lane-tagged format — this is PC-lane (ED-PC-00xx). |
| C2-U3 | **soften** (lane feed under-scoped) | Defers the value to ED-PC-0006 correctly, but the Hybrid paragraph targets mass-battle Command checks (MB territory) and mass_battle_v30.md:313-314 carries its own older variant (see M1) — must also feed an MB-lane ED. |
| C2-U4 | **uphold** | Fork correctly docketed with a default; tagged SE feed. |
| C2-U5 | **uphold** | Registry bookkeeping, W2.8/W3 scope. |
| C2-U6 | **uphold** | Pure propagation of an uncontested formula. |

## Missed findings

**C2-M1 · P2 · stale · NEW** — `designs/provincial/mass_battle_v30.md:313-314` carries a THIRD,
even-older wound-Command-penalty formulation ("Wounds from personal combat add +1 Ob to Command
tactic execution rolls") predating the whole PP-716/ED-1041/ED-PC-0005 lineage and citing none of
it. Unlike params/fieldwork.md:225 (explicitly subsumes its prior +1 Ob into ED-PC-0005) and
params/mass_combat.md:434-435 (current fractional-Ob text), this design-doc carrier was never
swept: ED-PC-0005's ledger entry (editorial_ledger.jsonl:377) scopes the mirror sweep to
"params/core.md/fieldwork.md/mass_combat.md" only — a real gap between the params/ sweep and the
design-doc layer. Sits beside C2-F3 as a third stale carrier of the same mechanic.

## Conformance note

No invented criteria; all findings map onto the given KIND taxonomy and cite armature/registry
surfaces. No fork silently ruled (C2-U4 and the shape of U2/U3 defer to Jordan/ED-PC-0006, rule e).
Lane scoping mostly respected; C2-U3 under-feeds MB (corrected in the docket). No
build-state-as-verdict instances. Two severities were inflated: C2-F1/F2 labeled
"stale-carrier-with-reachable-canon" as P1 when the rubric places that at P2 — both softened.
C2-F3's P1 holds and is worse than filed: the ledger resolution it rests on is partially false.
