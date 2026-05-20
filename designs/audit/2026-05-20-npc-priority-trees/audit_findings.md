# NPC Priority Trees — Contamination Audit (2026-05-20)

**Target:** `params/bg/npc_priority_trees.md`
**Flagged by:** Jordan 2026-05-17 ("priority-stack contamination")
**Status of consumer:** `sim/autoload/npc_ai.py` is a NotImplementedError stub. Audit is pre-implementation; findings prevent contaminated content from being authored into code.

---

## §1 — Structural defects (deduplication landing this commit)

**D-1. Every tree is duplicated.** Trees appear at L26–116 and again at L119–228. The two blocks are byte-identical except for trailing whitespace. The duplicate `### Priority Tree Template (7 levels)` at L15 / L119 is the seam.

**Resolution:** delete the second block (L118–229). Retain `## PP-NPC-01` through `## PP-NPC-04` (L231–253). No design judgment needed.

---

## §2 — Stale references (need decision)

Each item below references a mechanic or condition that may have been STRUCK or SUPERSEDED by canon Jordan has ratified since this file was last touched. The header SUPERSEDED 2026-04-19 banner covers Cultural Reformation and VTM, but several other mechanics weren't covered.

### S-1. Church P3: `CI < 75 AND Church L ≥ 4 → Assert (CI +1)`. Post-CI 75: P3 → Territorial Seizure.

CI no longer freezes at 75 per `ci_political_v30.md` §0 ("CI ceiling | 75 (freeze + seizure) | 100 (no freeze)"). The "75" threshold is stale. Per `ci_political_v30.md` §2.2, CI 100 triggers Theocracy Unification Attempt (one-shot Mass Seizure). CI 60 makes Mass Seizure available probabilistically per `victory_v30 §3.2 PP-534` formula `P = ((CI−60)/40)^3.3`.

Either:
- (a) replace "75" with "60" and "Territorial Seizure" with "Mass Seizure (probabilistic per CI; one-shot)";
- (b) replace "75" with "100" (Theocracy Unification trigger) and explicitly model the 60-100 range with seizure probability;
- (c) rewrite P3 entirely as a milestone-driven escalation matching the four CI milestones in `ci_political_v30 §2.1` (40 / 55 / 65 / 80 / 100).

**Decision required.** I recommend (c) — the canon now distinguishes five Church-Assertive levels; reducing them to a binary loses canon-fidelity. But (a) is cheapest.

### S-2. Crown P3: "Royal Decree" mechanic.

`crown_initiative.py` exists in the codebase (13 KB module) but I have not verified what `Royal Decree` resolves to canonically. The Crown tree references "Royal Decree" as an action without canonical sourcing in the priority-trees doc. PP-NPC-01 (L231) adds an L ≤ 2 gate but doesn't define the action itself.

**Possible canon paths:**
- `designs/provincial/crown_initiative_v30.md` (if it exists)
- `params/bg/factions.md` Crown faction-unique action table
- Cross-reference from `complete_systems_reference.md` Part 7

**Decision required.** Confirm canonical source for "Royal Decree" before npc_ai authors it.

### S-3. Löwenritter "Autonomy" track.

References to Löwenritter Autonomy = Restless appear in Crown P2 (L42) and Löwenritter P2 (L86). PP-NPC-02 (L236) refines the advancement trigger to require both CI ≥ 40 AND active Church Assertion that season. ED-781 migrated "Coup Counter increment" → "Löwenritter Autonomy advance to Restless".

**Concern:** is the Löwenritter Autonomy track still canonical? It's not in the current `canonical_sources.yaml` index that I pulled earlier (Löwenritter coup mechanics are referenced in P3 patches but the track itself may have been struck during the 2026-04-30 architecture session).

**Decision required.** Confirm whether Löwenritter Autonomy survives in current canon. If struck, both Crown P2 and Löwenritter P2 need rewriting.

### S-4. Crown P2 trigger: `PI ≥ 8`.

`PI` (presumably Imperial Pressure per Altonian Theocracy mechanics) — Altonian Theocracy is on the list of STRUCK victory conditions per GD-1 (canon/02_canon_constraints.md §B). If Altonian Theocracy is fully struck, IP-related triggers in Crown P2 may also need to go.

But — IP advancement is also tied to Accord-based territory-count thresholds per `peninsular_strain_v30 §3.2` (referenced in `ci_political_v30 §4.4`). So IP itself may survive even if Altonian Theocracy as victory path doesn't.

**Decision required.** Does IP still drive Crown threat-priority, or is the P2 IP-trigger stale?

### S-5. Varfell P5: "Warden Recognition" + T15 march.

VTM was STRUCK in the 2026-04-19 banner at the top of the file. The parenthetical "(PP-664: VTM gating struck with VTM track.)" acknowledges this. But "Warden Recognition" itself — distinct from VTM — is referenced as still operative.

If WR is still canonical, P5 is fine. If WR was also struck along with VTM, this entry needs removal.

**Decision required.** Confirm Warden Recognition survives as Varfell-distinct advancement track. (Note: this connects to the Pass 2d Varfell contamination audit Jordan also flagged.)

### S-6. Church P5: "Temperance declaration if Cardinal active".

Cardinal mechanic isn't defined in any canon I've pulled this session. Possibly part of the Church faction-unique action set, possibly a stale reference. Same uncertainty as Royal Decree (S-2).

**Decision required.** Confirm Cardinal mechanic source.

### S-7. Crown P4: hardcoded "T2 Kronmark / T4" tactical rule.

> "If T2 Kronmark is ungarrisoned AND any Varfell unit is active in T4: deploy minimum garrison to T2..."

This is a *tactical* rule (specific territory pair) baked into the priority tree. Two issues:
- It hardcodes geography into AI policy — fragile against any future map changes (although the 17-territory canon is stable).
- It assumes Crown has a unique "breadbasket protection" rule against Varfell that no other faction has against any other faction. Asymmetric AI rules need explicit canon backing.

**Decision required.** Confirm this rule has canonical justification (e.g., a Jordan design note), or recommend striking it as over-specification.

### S-8. RM Priority Tree P2 condition: `PT ≤ 1 in 3+ territories`.

Per ED-743 (struck 2026-04-29) the old battle-occurrence → IP trigger was struck; IP now advances from Accord-based territory-count thresholds. The RM emergence trigger per GD-3 is `2+ contiguous territories at Uncontrolled status, sustained 2 consecutive seasons`. RM's *priority tree* condition `PT ≤ 1 in 3+ territories` is post-founding, so it's distinct from emergence — but I haven't seen canon defining post-founding RM behavior since GD-3 was added.

**Decision required.** Does post-founding RM still operate on PT-low triggers, or has GD-3 (extra-parliamentary status + invasion rights) shifted this?

---

## §3 — Architectural concerns (would-fix-without-input if you confirm)

### A-1. The priority-tree format mixes resolution into conditions.

Most rows have `Condition | Action`. Some — e.g., Church P3 — embed sequencing: "Assert (CI +1). Piety DA if Assert used." That's two actions in one cell. npc_ai will need to either run them as a micro-sequence or pick one. Either way, the canon should disambiguate.

**Recommendation:** When npc_ai is authored, treat semicolon-separated action lists as "first action; second action if first succeeded". Otherwise flag for canon revision.

### A-2. No explicit GD-2 mandatory-action interaction.

GD-2 (canon/02_canon_constraints.md §B) requires mandatory-actions pass *before* stochastic candidate generation. The priority trees here are *the* stochastic candidate generator. The mandatory-vs-priority precedence isn't documented in this file.

**Recommendation:** Add a header note clarifying that priority trees fire *after* GD-2 mandatory-action allocation (Muster at Accord ≤ 3 ungarrisoned; Govern at Accord ≤ 2 garrisoned). Any priority slot consumed by a mandatory action becomes a Pass for the priority tree.

### A-3. PP-NPC-04 Varfell Collection cooldown conflicts with §8.5 once-per-season limit if state flag isn't initialised.

PP-NPC-04 specifies that "P2 fires only if Private Collection not yet used this season. Mark Collection as used. Flag resets at Accounting." But the flag's initial state isn't specified — at S1 turn 1, has Collection been used or not? Default to False is the obvious read, but explicit canon helps.

**Recommendation:** Add to PP-NPC-04: "Initial state at world creation: Collection unused (flag = False)."

---

## §4 — Recommended commit shape

I can land this audit's structural findings in a single low-risk commit *without your input* if you authorize:

1. **D-1 dedup** — delete L118–229 (the duplicate block).
2. **A-2 GD-2 precedence note** — add a small section header clarifying mandatory-action precedence.
3. **A-3 PP-NPC-04 initial state** — add one sentence.

The S-* items (§2) require your judgment because they touch canon-policy decisions, not code mechanics. Same for A-1.

If you want me to commit just the dedup now and leave S-* / A-* for an input doc, say so.
