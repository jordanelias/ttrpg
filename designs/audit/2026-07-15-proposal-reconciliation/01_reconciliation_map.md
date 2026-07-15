# 01 — Reconciliation Map (Nature-B: the governance / cross-scale cluster)

## Status: REFERENCE (analysis-only; Class-A self-exempting — no canon flipped by this file). Anchors ED-IN-0068; the unified head it recommends is `governance_cluster_reconciliation_v1.md` (ED-IN-0069, filed for ratification).

The 13 remaining awaiting-ratification docs after the Nature-A/D bookkeeping are read here **against each
other**, applying the adjudication rule: **recency wins by default; explicit supersession beats a recency
debate; depth offsets recency only when the older doc is dramatically deeper on the specific point and the
newer is a thin note/umbrella; un-resolvable forks are HELD for Jordan.**

---

## §0 · The headline: this is TWO axes, not one cluster

A naive "reconcile all the 2026-07-11→14 governance docs into one head" is wrong. The 13 fall on **two
different axes** and must not be merged:

| Axis | Docs | What it is | Already anchored by |
|---|---|---|---|
| **B-gov — governance-PLAY design** | ripple_substrate, grounded_event_card_deck, compendium (00_index/42/43/44/45/event_cards), reeval_jp_se, **governance_type_registry** (07-13, index), **lps_wiring** (07-14, SE buildable) | The FLAG/VECTOR governance types, action-verbs, directives, institutions, long-fuse stats, L/PS wiring, event decks — the *mechanics of governing* | nothing yet — **this is what needs a unified head** |
| **B-obs — observatory / tooling remediation** | `remediation_plan_v1` (ED-IN-0066), `2026-07-14-holistic-unification/unification_v1` (ED-IN-0065) | The vector-audit scripts, pointer-debt, module-grounding, wiring closure — *tooling and repo structure*, not governance-play content | **ED-IN-0064/0065/0066** (already filed; D1–D16 docket held for Jordan) |

The two share vocabulary ("governance," "cross-scale") but not subject matter. **B-obs needs no
reconciliation here** — it is a coherent, already-anchored program with its own held docket; this pass only
records that it is a separate axis and points to it. All reconciliation below is **B-gov**.

**One ratified companion the B-gov cluster routes through (not in the 55 — it's ratified, so not PROPOSED):**
`designs/architecture/governance_consolidation_v1.md` (2026-07-12, **RATIFIED 2026-07-13, ED-IN-0046/0047**)
is the *decision-surface* the compendium's own `00_index.md` names as its companion ("read that for 'what to
decide'"). It already rules D1–D6 (incl. the Compact question, §2.1) and holds the 12-item PR#119 disposition
table. **Any governance synthesis must route through it or it re-litigates settled ground.** It pairs with the
`governance_type_registry` as the *taxonomic* index (§3).

---

## §1 · B-gov doc-role table (recency + depth)

| Doc | Date | Depth | Role | Uniquely owns | Disposition |
|---|---|---|---|---|---|
| `governance_type_registry_v1.md` | 07-13 | 298L | **INDEX HEAD** | The FLAG/VECTOR taxonomy; a deduplicated registry of every governance type across the scale hierarchy; §4's new Key+Field/Gauge architecture proposal | **Index head** — points to the deep sources; §4 is a HELD fork |
| `governance_ripple_substrate_v1.md` | 07-11 | 559L | **deep substrate** | The propagation/accumulation/dissipation ("ripple") model; §7 Treasury vector | **Deep-content source** under the index — depth offset: newer index cites it, doesn't re-derive it |
| `2026-07-12-governance-compendium/` (42/43/44/45 + event_cards + 00_index) | 07-12 | ~860L | **research corpus** | 109-verb action catalogue (42); directive types (43); standing institutions (44); hidden long-fuse stats (45); event-card integration | **Deep-content source** — a research menu NOT yet authored into canon heads; the index selects from it |
| `grounded_event_card_deck_v1.md` | 07-11 | 335L | event-deck spec | The grounded 13-card event-deck engine | **Deep-content source** — pairs with the compendium's `event_cards/00_integration_map`; the two are complementary (deck engine vs integration map), not rivals |
| `reeval/reeval_jp_se.md` | 07-12 | 82L | re-evaluation | The built-vs-proposed check that surfaced the Compact/Leverage divergence | **Superseded-by-ruling** on its headline finding (see §2.1); retained as the provenance of that catch |
| `lps_wiring_v1.md` (SE) | 07-14 | 227L | **buildable spec** | The Legitimacy/Popular-Support wiring — the concrete build of the registry's "consent/resistance VECTOR" (`type_registry §2.1`) | **SE-lane buildable head** — most recent, executable; the registry's L/PS row points here |

**Recency-vs-depth reading for B-gov:** the newest content doc (`type_registry`, 07-13) is explicitly an
*index* that "claims no new mechanical canon by itself" and grounds against the deeper 07-11/07-12 work — so
this is the **depth-offset case working as intended**: recency gives us the *organizing* head, but the deep
content stays owned by the older ripple_substrate + compendium. No recency-driven deletion of depth. `lps_wiring`
(07-14) is newer *and* the concrete build, so it wins its slot outright.

---

## §2 · Conflicts / overlaps (with verdicts)

### §2.1 · Compact vs Leverage as the "5th ledger family" — RESOLVED by later ruling
- **Claim A (compendium, 07-12 + ED-SE-0018/0019):** "Compact" is a new 5th ledger tag-family.
- **Claim B (built code):** `sim/territory/ledger.py:30` `TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}` — Leverage is the 5th; no Compact.
- **Ruling (ED-IN-0046 D3, RATIFIED 2026-07-13):** "Compact models as a recurring **Debt subtype**, not a 6th [or 5th] ledger family."
- **Verdict:** **RESOLVED by recency (rule 2).** ED-IN-0046 (07-13) post-dates and overrides the compendium's
  5th-family framing: Compact is a Debt subtype; Leverage is the built 5th family; **no conflict once D3 is
  applied.** The compendium's own §268 already anticipated this ("tag-family proliferation… a consolidation
  pass is warranted before all five ship"), and `governance_type_registry §2.4` already reflects D3.
- **Residual (not a fork, but broader than the cluster):** the pre-D3 "5th ledger family" framing survives in
  **`grounded_event_card_deck_v1` C.3, compendium Part 44 §44.2.7 / Part 45, AND
  `designs/territory/governance_play_redesign_v1.md` §1.3a/§1.6** — a *current head* whose Encabezamiento
  "Negotiate Quota" defines Compact as "a new fifth Ledger-of-Consequence tag family," the exact framing D3
  superseded. Propagating `Debt(key="compact:<quota>", ttl=term, recurs=True)` executes a *ratified* ruling
  (ED-IN-0046 D3), not a new design call — but because it re-models a mechanic in a current head, **recommend it
  run as ED-IN-0046 D3's own SE/IN propagation follow-up, not bundled into this reconciliation PR.** Tracked in
  the held-back list as a residual.

### §2.2 · Tag-family proliferation (Compact / Concession / Outlawed / Capital-Posture / Muster) — HELD
- The compendium (44 §268) proposes several new tag-families atop the base 5 and flags them as likely
  over-proliferated ("Muster/Compact may be collapsible; Concession/Capital-Posture overlap").
- **Verdict:** **HELD for Jordan.** ED-IN-0046 D3 set the *pattern* (collapse into existing families where
  possible — Compact→Debt), but the remaining candidates (Concession, Outlawed, Capital-Posture, Muster) have no
  ruling. This is a genuine taxonomy design call, not bookkeeping. → Held-back list.

### §2.3 · 109-verb action catalogue (42) vs the 8 canon governance verbs — no conflict, a menu
- `governance_play_redesign_v1 §1.3` has **8** governance verbs (Develop/Fortify/Keep Order/Hold Court/Sponsor/
  Treat/Levy/Investigate); Part 42 organizes its 109 research entries under exactly those 8 (verified). (The old
  4 stat-pumps Develop/Fortify/Pacify/Administer are the pre-redesign baseline it replaces.)
- **Verdict:** **No contradiction** — 42 is an unadopted *menu* to draw from, not a rival ruleset. The registry
  classifies these as FLAG/VECTOR; **which verbs get authored into the canon head is a HELD selection call** (Jordan
  picks the shortlist). → Held-back list (verb-selection).

### §2.4 · Directive types (43) & standing institutions (44) — floating research, not yet authored
- Grep confirms neither is authored into `faction_politics_v30.md` / `governance_play_redesign_v1.md` (only a
  generic "Directive" mention exists).
- **Verdict:** **No conflict; un-adopted.** These are research corpus the index points to; authoring them into a
  canon head is a HELD decision. Not superseded, not adopted. → Held-back list (author-or-drop).

### §2.5 · 45_hidden_longfuse_stats — open granularity ruling
- Its own status: "needs a granularity ruling."
- **Verdict:** **HELD for Jordan** — a genuine open design question (at what tier the long-fuse stats live). → Held-back list.

### §2.6 · type_registry §4 — Key + Field/Gauge dual substrate primitive — HELD (the one genuinely-new architecture fork)
- §4 argues the dominant "VECTOR-with-derived-FLAGS" shape needs **both** a Key (FLAG moment) and a new
  **Field/Gauge** primitive (VECTOR body), because "one substrate primitive cannot serve both halves well"
  (grounded on `key_echo_armature_v1 §1`).
- **Verdict:** **HELD for Jordan.** This is the cluster's one substantive new-canon proposal — it would add a
  primitive to the Key substrate. High-leverage, cross-cutting, explicitly unratified. → Held-back list (top item).

### §2.7 · Not a conflict: the two 07-14 unifications
- `remediation_plan_v1` (ED-IN-0066) and `holistic-unification/unification_v1` (ED-IN-0065) are **B-obs** (§0) —
  observatory/tooling, not governance-play. **They do not compete with the B-gov docs and must not be merged into
  the governance head.** Recorded here only to close the "reconcile all the 07-14 unification docs" trap.

---

## §3 · Recommended unified structure (→ `governance_cluster_reconciliation_v1.md`, ED-IN-0069, PROPOSED)

- **Index head:** `governance_type_registry_v1.md` (07-13) — the FLAG/VECTOR registry indexing the cluster.
- **Deep-content sources (kept, pointed-to, not superseded):** `governance_ripple_substrate_v1` (propagation
  substrate), the `2026-07-12-governance-compendium` corpus (42 verbs / 43 directives / 44 institutions / 45
  long-fuse), `grounded_event_card_deck_v1` + `event_cards/00_integration_map` (the event-deck pair).
- **Buildable SE head:** `lps_wiring_v1` — the L/PS VECTOR build the registry names.
- **Superseded-on-a-point:** `reeval_jp_se`'s Compact-5th-family finding (by ED-IN-0046 D3); retained as provenance.
- **Separate axis, pointer only:** `remediation_plan_v1` (ED-IN-0066) + `holistic-unification` (ED-IN-0065).

Nothing in B-gov is deleted; the reconciliation is **organizational** (one index head over kept deep sources) plus
**one recency supersession on a point** (Compact) plus a **held-back fork list**.

---

## §Held-back — decisions only Jordan can make (mirror this in the PR body)

**From B-gov:**
1. **type_registry §4 — add a Field/Gauge substrate primitive alongside Keys?** (the cluster's top new-canon fork, §2.6)
2. **Tag-family taxonomy** — ratify/collapse Concession / Outlawed / Capital-Posture / Muster (Compact already → Debt subtype) (§2.2)
3. **Governance verb selection** — which of the 109-verb catalogue (42) get authored into the canon head over the current 8 (§2.3)
4. **Directives (43) & standing institutions (44)** — author into `faction_politics_v30`/`governance_play_redesign` or shelve (§2.4). Note Part 44's tracked-stat institutions (Water Magistracy, Ever-Normal Granary) are **blocked on #5 first**.
5. **`45_hidden_longfuse_stats` granularity ruling** — its own framework recommends *track* RisingWaterLevel, *conditionally track* SiltLevel, *abstract* the other six; **StockLevel is blocked on a prior binary: adopt Ever-Normal Granary as a mechanic at all, yes/no** (§2.5).
6. **`governance_ripple_substrate` open rulings R-1/R-2/R-4** — R-1 (are the 5 §2 settlement levers in scope), R-2 (can an NPC event contest a player-held seat), R-4 (Π 7→8 event-deck band-cliff: hard threshold or softened band). (R-3 "Territory as connective tissue" is substantially answered by B12/`scale_hierarchy_v1`; residual = a one-sentence reconciliation of whether the new tier *behaves* as ripple-substrate connective tissue vs "a bigger settlement.")
7. **ED-SE-0045 (Treasury ×10 vs ×50)** — already a filed ED (2026-07-13 batch); flagged here because `lps_wiring §3.1` surfaces that both `ripple_substrate §7` and `type_registry §2.4` silently inherit `×10`. Cross-reference, not a new fork.

**From Nature C (`03_natureC_dispositions.md`):**
6. `character_canon_v30` PART A ratify / PART B scope (Q1)
7. `franchise_v30` — reconcile vs L/PS + scale-hierarchy first (recency/depth → governance is head; likely re-express as a derived view, not a new stat)
8. `solmund_master_document` — editorial read (likely ratify-as-is)

**From Nature D (`04_natureD_designs_proposals.md`):**
9. PC-4.4 success-stress (FA) — revive or drop
10. mechanics-integration-v3.1 (FA/SE, 31 items) — scoping triage vs the newer comparative-governance corpus
11. multiunit Path-B envelopment (MB) — greenlight the unbuilt spatial mechanism or not
12. PARTIAL residuals → file as lane handoff items: MB yield exits/calibration (#4), MB §A.6 dice-vs-geometry (#7), PC §7 concentration-error (#9)

**Non-fork residuals (safe, tracked under ED-IN-0068, not needing a Jordan pick):**
- Propagate the Compact=Debt-subtype annotation to `governance_play_redesign §1.3a/§1.6`, deck C.3, compendium 44/45
  (§2.1) — as ED-IN-0046 D3's own follow-up.
- **Broken path citation** `designs/architecture/governance_compendium_v1/` (does not exist) → real
  `designs/audit/2026-07-12-governance-compendium/`: **fixed** this pass in `42_action_verb_catalogue.md` (×2) and
  `event_cards/00_integration_map.md` (×1); **left in `tier3_proposal_status_closure.md` L28** because there the path
  is entangled with a false "the `reeval/` directory is empty" claim (the real `reeval/` holds `reeval_jp_se.md`) —
  needs a content-aware fix, flagged for a stale-citation sweep.
- **Event-card duplicate** GEO-04 ≡ XSCALE-08 ≡ HEV-BLOC-09 (Berlin Blockade) across the 3 event corpora — the
  merge is a mechanical de-dup (recommend target GEO-04), not a Jordan-blocking fork.
- Widen `build_proposals()` to catch **bold-inline `**Status:**`** (Nature-D systemic finding) — also affects
  `governance_play_redesign_v1.md`, which has no `## Status:` heading and is likewise dashboard-invisible.
