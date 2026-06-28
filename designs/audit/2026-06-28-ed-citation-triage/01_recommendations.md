# ED-citation triage — recommended dispositions (advisory)

_Generated 2026-06-28. A first pass over the items in `00_triage.md`, grounded in the citing
contexts (3 parallel investigators read the source docs + ledger). **Advisory only — Jordan
decides.** No ledger entry is created or flipped by this file. "Recorded at" means a decision is
already documented somewhere, so the action would be grounded, not fabricated._

## Headline finding

**~75% of the 292 NONEXISTENT citations are "ledger lag," not errors.** They are decisions already
made and applied in design-doc editorial tables (with dates + rationale) that were never migrated
into `canon/editorial_ledger.jsonl`. The largest source tables:
`designs/provincial/faction_politics_v30.md` (register block), `designs/scene/fieldwork_editorial.md`,
`designs/arcs/arc_expansion_v30.md`, `designs/provincial/baralta_crown_claim_v30.md`. The cleanest
fix is a **bulk migration** of these tables into the JSONL using their recorded statuses/dates —
no editorial creativity, low retcon risk.

Disposition vocabulary: **register** (file a ledger entry; suggested status in parens) ·
**fix-citation** (wrong/phantom ID) · **strike** (cut/abandoned) · **resolve** (recorded decision
exists; flip status) · **reword** (open ED over-claimed in the citing doc) · **decide** (needs Jordan).

---

## A. OPEN_AS_BASIS (16 EDs) — most have recorded decisions → flip-eligible

| ED | ledger status | recommended | where the decision is recorded | conf |
|---|---|---|---|---|
| ED-912 | open | **resolve** | `fieldwork_v30.md:467` "ED-912/ED-841 — Jordan ruling 2026-06-23 (rev 2026-06-28)"; applied across 7+ docs | high |
| ED-864 | open | **resolve** | ledger `jordan_decision: ratified 2026-05-17`; `designs/audit/2026-05-17-scene-combat-contest/decisions.md` | high |
| ED-295 | provisional | **resolve** | `params/contest.md` §P1 "Resolved 2026-05-17 (audit ED-864)" | high |
| ED-869 | open | **resolve (Crown-Mil) / split** | `stats_1_7_scale.md:19` "prior value 4 struck per ED-869 / Jordan 2026-05-31"; Löwenritter split-state still open | high |
| ED-644 | open | **resolve** | vocabulary audit 2026-05-08; `censured_vocabulary.yaml` authority ED-644; equivalence note in `conviction_track_v30 §1` | high |
| ED-738 | provisional | **resolve** | `editorial_ein_sof_gradient_2026_04_21.md`; adopted across throughline meta layer | high |
| ED-618 | provisional | **resolve** | applied in `npc_behavior_v30 §2.8` (emergence window); consistent across 3+ docs | high |
| ED-670 | provisional | **resolve** | `thread_horizontal_integration_spec.md:287-289` "Applied … Close → resolved" | high |
| ED-643 | open | **resolve** | Solmund naming fix applied (`conviction_track_v30` line 16); narrow cleanup, complete | high |
| ED-545 | provisional | **resolve** | `valoria_ui_ux_v4.md` "Resolves: ED-545"; ledger note "substantially resolved by §4.3.2/4.4" | high |
| ED-542 | open | **resolve** | cited as live CANONICAL ruleset in `mass_battle_v30 §E`; no superseding record; propagation deferred not blocked | med |
| ED-620 | open | **strike** | `victory_v30.md:684` header "[SUPERSEDED-BY: GD-1]" (2026-05-17); GD-1 in `canon/02_canon_constraints.md` | high |
| ED-631 | open | **decide / reword** | genuinely open (Heresy proceeding timing); citing docs treat derived rule as canonical w/o flag | med |
| ED-649 | open | **decide** | roster gap ("2 Prelates need naming"); close-as-tracked or keep open | med |
| ED-893 | open | **decide** | citation↔ledger scope mismatch (PP-614 adoption vs Arc-E wager tolerance); reconcile first | low |
| ED-1042 | open | **decide** | citation↔ledger mismatch (heading de-dup applied vs wound-model drift still open); split/clarify | low |

**Flip-eligible now (recorded): 11** (ED-912, 864, 295, 869, 644, 738, 618, 670, 643, 545, 542).
**Strike: 1** (ED-620). **Need your call: 4** (ED-631, 649, 893, 1042).

---

## B. NONEXISTENT (292 citations / 94 EDs) — grouped by batch

### B1. Register as RESOLVED — decision recorded in-doc, just un-migrated (ledger lag)

| ED batch | citing source | recorded decision | conf |
|---|---|---|---|
| ED-393–401 | `arc_expansion_v30.md §1.4`, `npc_foils_v30.md` | "characterization canonical per ED-393–401" (2026-04-17 ruler/NPC foil suite) | high |
| ED-496–506 | `fieldwork_editorial.md`, `fieldwork_v30.md` | 11 fieldwork rules resolved via PP-630/631/632 (2026-04-13) + sim debt closures | high |
| ED-555/557/559/571 | `companion_specification_v30.md:2` | header "Resolves: ED-555/557/559/571" (companion spec doc, 2026-04-16) | high |
| ED-585/590 | `victory_v30.md:273` | "ED-585/590 resolved 2026-04-16: Accord ≥ 3 seizure condition" | high |
| ED-544/548 | `valoria_ui_ux_v4.md`, `valoria_ui_ux_v4_1.md` | P-03 rendering model + Wound-interval correction, ratified UI audit | high |
| ED-671/672 | `thread_horizontal_integration_spec.md:287-289` | "Applied (§3.4/§4.3 npc_behavior_v30) — Close → resolved" (2026-04-17) | high |
| ED-820 | `mass_battle_shape_echelon_revamp.md` | two-stage formation setup, decision recorded in revamp doc | high |
| ED-938/939 | `clock_registry_v30.md`, `derived_stats_v30.md` | docket J-31 ratified fixes (2026-06-04 / 2026-06-24) | high |
| ED-406–412 (most) | `baralta_crown_claim_v30.md:141-144`, `arcs_36_40.md` | succession/consecration mechanics "Decision made"; ED-412 resolved 2026-04-12 | high |

### B2. Register as OPEN/PROVISIONAL — genuine pending design questions

| ED batch | citing source | what it is | conf |
|---|---|---|---|
| ED-379–382 | `character_histories_v30.md` | lifepath design questions (Catalysts, equip slots, Coherence loss) | high |
| ED-173/174, ED-177/178 | `threadwork_superseded.md`, `combat_v30.md` | authored PROVISIONAL rules (cite PP-284) awaiting ratification | high |
| ED-507–509 | `fieldwork_v30.md` | POI authorship / NPC dispositions / Godot-deferred node validation | high |
| ED-510–514 | `propagation_log.md` | NPC recruitment/hooks/surrender/fail-forward, provisional, propagation pending | high |
| ED-567 | `arc_expansion_v30.md` | Longevity-roll generational conditioner **proposal** | high |
| ED-595–610 | `arc_expansion_v30.md:740-759` | named-NPC arc-profile expansion set, "requires user approval" | high |
| ED-634/639/646/647/649/653 | `faction_politics_v30.md` register | ministry/naming/recognition-ceremony items, P2/P3 flagged-for-review | high |
| ED-413–417 | `arcs_36_40.md` | arc timing/thread/battle/uprising questions awaiting confirmation | high |
| ED-538/546 | `complete_systems_reference.md` | compound stat mechanics flagged unvalidated pending sim | med |
| ED-402–405 | `canonical_sources_notes.md` | arc-register editorial batch, scope thin — review arc_register v8 | low |

### B3. Fix-citation / already-filed

| ED | action | detail | conf |
|---|---|---|---|
| ED-814 | **fix-citation → ED-907** | docs themselves flag "ED-814 is a phantom; should point to ED-907" (7 occurrences) | high |
| ED-591–594 | **register as struck** | superseded by ED-758 (arc consolidation 2026-04-24) | med |
| ED-972 | **verify** | not clearly located; confirm it's a real reference vs stale before acting | low |

---

## C. Suggested execution order (when you greenlight)

1. **Flip the 11 recorded OPEN_AS_BASIS** (§A) + **strike ED-620** — grounded, clears those violations now. I would verify each recorded decision against the cited source before flipping (not trust this table blindly).
2. **Bulk-migrate the B1 "resolved" batches** from their design-doc tables into the JSONL with recorded statuses/dates (via valoria-editorial-register Workflow B).
3. **Register the B2 open/provisional** items (status open/provisional, owner authority).
4. **fix-citation ED-814→ED-907**; handle ED-591–594 strike, ED-972 verify.
5. **Decide** the 4 genuine OPEN_AS_BASIS calls (ED-631/649/893/1042).
6. Re-run the validator (target 0), then drop `continue-on-error` on the `ed-citations` CI job.

Confidence note: B1/§A high-confidence rows are safe to act on after a quick source re-check; the
`low`/`med` rows want your eyes first. Nothing here mutates the ledger.
