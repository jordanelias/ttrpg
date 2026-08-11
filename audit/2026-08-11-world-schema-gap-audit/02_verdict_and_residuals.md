# World-Schema Gap Audit — verdict, held decisions, and what this run did not cover

## Status: REFERENCE — observations against the tree. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0153 · **Base:** `63d4d0c`
Method: [`00_orchestration_plan.md`](00_orchestration_plan.md) · Register: [`01_gap_register.md`](01_gap_register.md) (4 parts)

**Run:** 17 agents · 0 errors · 0 empty returns · `stop_reason: completed` · not degraded ·
61 disputes recorded, **0 left unadjudicated** · 75 raw findings → 50 register rows.

---

## 1. Ladder verdict

The schema cannot express the ratified entity ladder, and it breaks at two identifiable seams.
Vertically, scale_hierarchy_v1 is Jordan-ratified at Country > Duchy > Province > Territory > Settlement while the substrate enum (engine/substrate/keys.py:65) is exactly four values — personal, settlement, territory, peninsula — with no national, duchy or country member; 'provincial' appears in module_contracts rows and in zero of 55 key entries; the B12 Territory tier collapses back into the same 17 T-codes it was meant to sit beneath; and at least five parallel scale vocabularies now coexist under a held fork (G-21, G-22, G-43).
Horizontally it breaks hardest at the faction rung: four independent lanes across three method-disjoint passes found that no key type announces a faction coming into or going out of existence at any tier, the one production path claiming to implement emergence sets a boolean and returns, faction_state's owned-state block is three rows against its own canon doc's nine-plus authored and derived fields, and 'which factions exist' is a four-entry Python literal (G-01, G-02).
Below that, whole relations the world model asserts — treaty, Casus Belli, NPC relational edges, subnational footholds, settlement-to-province membership — are stored as untyped dicts because the bucket taxonomy has no shape for a per-counterparty relation, and eight of the fixes are structurally ungoverned today because §10 forbids new key types without a rendering-dispositions file that does not exist (G-17, G-24).
On individuation the answer is worse and simpler: the schema mostly cannot distinguish two instances of anything it does carry.
Every per-province authoring field the geography file supplies — spiritual_weight, proximity_calamity, starting_pros — has zero code readers; territory temperament's only implementation is a zero-importer orphan; institutional_culture, the single scalar meant to individuate faction behaviour, is read by no Python and authors the same value for three of six factions; and the genuinely faction-unique behaviours in code are dispatched by faction.name string equality while a capability map that would do it as data sits unread in mechanics_index.yaml (G-03, G-16, G-48, G-49).
What remains is a world of near-identical instances plus a handful of hardcoded singletons — T9's templar written as tid == 'T9', Church's CI seizure, Crown's automatic Casus Belli, four static factions — so a second campaign would differ from the first essentially by RNG seed.

---

## 2. The defect this run found in its own instrument

**Recorded first, because it conditions how every number in the register should be read, and
because the prediction it falsifies is one this unit made in writing before the run.**

`00_orchestration_plan.md` §6 stated the rediscovery limit as: *"two lanes that reach one gap
through different files will not group, so the rediscovery count is a floor, never a ceiling. It
under-reports corroboration; it cannot over-report it."*

**That was wrong in a way that matters.** The instrument did not under-report. It reported
**nothing**: 75 raw findings produced 75 groups, and every single `rediscovery` value in the
returned ranking is `1`. The corroboration signal — the entire justification for running three
method-disjoint passes rather than one — was absent from the data handed to the synthesis stage,
which reconstructed it by hand from lane labels and claim wording.

**Root cause**, in the single owner `tools/wf_harness.js`: `hSameFinding` gates on
`hFirstFile(a) === hFirstFile(b)` before it compares content words at all, and `hFirstFile` returns
the *first* file-shaped token in a finding's `evidence` string. Two lanes describing the same gap
from different directions almost never lead with the same citation, so the file-equality
precondition zeroed the comparison before the fuzzy matcher ran.

The owner's own comment predicts this outcome for the *exact* key and builds `hSameFinding` as the
remedy: *"An exact key splits them into singletons and silently zeroes out the entire corroboration
signal, which is worse than not computing it: the output still has a `rediscovery` column, it just
always reads 1."* The remedy inherited the defect it was written to cure, because it kept the
same-file precondition. This is the §0.1 point-5 signature exactly — code that was correct for the
shape it was written against, and silently wrong for a shape that arrived later.

**Not fixed here, deliberately.** `tools/wf_harness.js` is the single owner of a prelude copied into
every workflow script, its behaviour is pinned by `tests/valoria/test_wf_harness.py` (mutation-verified,
13/13 mutants killed), and changing the grouping rule needs its own expected-delta test rather than a
drop-in edit. Filed as an IN-lane item. **The guard is the deliverable, not the patch:** any fix must
ship with a test that fails when a two-lane rediscovery collapses to two singletons, or the pattern
recurs invisibly — which is what happened here.

**Consequence for the register:** the `×` column is a **synthesis reconstruction, not a measurement**.
Rows at ×3 and ×4 reflect a judgment that lanes converged, formed by reading their claims. Treat the
counts as an ordering hint with a named provenance, not as an independent corroboration signal.

---

## 3. Decisions held for Jordan

**None of these is ruled by this audit, and merging its PR does not ratify any of them.** Each needs
a design call that an observation pass has no standing to make.

1. G-17 (blocks 8 propose_key rows): who authors references/rendering_dispositions.yaml, and whether the existing 55-type backlog is dispositioned before or alongside new appends. §10's precondition is RATIFIED (ED-IN-0026) and the file does not exist (verified by directory listing). Note the correction to ED-IN-0153's own wording: A15 enforces report-only first and flips to blocking once the file exists and the backlog is zero, so appends are ungoverned rather than mechanically refused.

2. G-21 / G-43: whether the B12 Territory tier enters the scales enum, and how five parallel scale vocabularies reconcile. HELD at ED-IN-0103 §6 fork 1, whose text bars any unification 'here or anywhere else'. This audit contributes two new measurements and proposes nothing: 'provincial' is 0-of-55 in the key registry, and :1084 declares a 'territorial' singleton no other entry uses, so the signature vocabulary is not internally closed — that is upstream of any request to add a value to it.

3. G-22: whether faction tier (local/provincial/national) is a FIELD on the existing faction_state contract or a module per tier. Recommendation on the record is tier-as-field, since §5.1's own point is that tiers are the same kind of entity differing only in population held — but the call is Jordan's, and the field can land independently of the frozen scales enum and should be split so it is not blocked behind a held ruling.

4. G-42: which of the 8 consumerless key types are legitimately terminal (ED-IN-0151 item c). env.crisis and mechanical.season_change declare wildcard consumers ('[all]', '[all subscribing systems]'), which is a join defect, not an absent declaration — fold both lanes' findings into that fork as one line.

5. G-05: Renown's owner — does player_agency_v30 get a contract module row, and is descriptor_registry's not_descriptors.tracks block (7 members: Piety, Disposition, Renown, Standing, Persuasion, Coherence, Warden Recognition) swept as a block? Two lanes proposed contradictory homes and a third proposed promoting Renown alone, which special-cases one member of a uniform block.

6. G-38: whether a singleton starting world is an intentional design ruling. If world-variant selection is intended, it composes on valoria_geography_v30.yaml plus ED-IN-0011's already-ratified template-pack format, not a new world_config.* key family.

7. G-24: whether governance_type_registry_v1 §4.2's Field/Gauge primitive lands, and whether the bucket taxonomy (owned by derived_stats_v30, not the adjudicator skill) gains a relational shape. Six findings here (G-03, G-05, G-13, G-23, G-25, and the derived half of G-02) are VECTOR-shaped; filing six per-quantity state rows before this fork resolves risks six divergent shapes for one primitive.

8. G-35: Deniability Debt currency. vocab_source.yaml:593-601, deprecated_terms_registry.yaml:74-77 and glossary.md:285 all mark it DEPRECATED with functions redistributed to the settlement broker and Niflhel-as-faction struck per ED-764, while faction_politics_v30.md:424 says 'retained' and ED-633 closes it CANON. Must be ruled before any schema row, or the row canonises a struck mechanic.

9. G-08: whether state.standing_change is Class-A superseded (payload edit) or given a Class-B sibling type. §10 makes the payload edit the MORE expensive path, inverting what two lanes assumed. Related: ladder_id must resolve against a ladder registry, not a frozen proper-noun enum — 'niflhel' is a value Jordan struck as a faction on 2026-05-09, and the real arity is (npc × ladder × arm), not the 8-value enum proposed.

10. G-11: ratify or strike franchise_v30 (Status: DRAFT) before any schema allocation. The lane proposal to wire Franchise into three keys' consuming_systems is rejected outright — ED-IN-0096 deliberately emptied exactly those lists after finding they created false consumers.

11. G-32: the BALANCE-005 contradiction. registers/editorial_ledger_archive.jsonl:477 is status resolved, 2026-04-13, 'The dependency is narrative pressure, not mechanical', while ED-SE-0009 reopens it as a mechanical rule and HANDOFF_SE.md:61 works it as open. A resolved archive ruling is live on two surfaces.

12. G-31 / G-45: whether a settlement id is a legal actor_id in the substrate's targets[] array. This decides whether da.public_governance needs a target_settlement_id at all, and it is the question two lanes answered wrongly by reading optional_payload_fields instead of key_substrate_v30.md:45-53.

13. G-33: the mass_battle single-writer boundary. module_contracts.yaml:566-572 reserves MB's rows to the MB lane, stating 'the join lane does not touch MB's rows even to add a field' (OI-54, ED-IN-0097 W4). The military-unit and garrison findings cannot be filed by this audit; they are the MB lane's to dispose.

14. G-19: whether meta.knot_formed's struck tier enum (Loose|Medium|Close, superseded by ED-912's Distant/Close and already propagated into the generated key_types.json export) is corrected now — a Class A supersession — and whether the additive relation_kind field ships in the same supersession rather than a second one.

15. G-10 / G-12 doc-status contradictions, recorded not resolved: fractional_province_ownership_v30.md declares PROVISIONAL at :1, CANONICAL at :3, PROVISIONAL at :5; march_layer_v30.md declares CANONICAL at :5 and PROVISIONAL at :7 with an unmet §11 promotion gate at :191-195. Two independent instances make this a doc-header pattern worth a sweep, not two one-offs.

16. G-28: the ED-686 citation defect as an IN-lane provenance item separate from the schema gap. A CANONICAL doc cites an ED that validate_ed_citations.py passes (the ID exists) while it resolves to unrelated closed content about Co-Movement card calibration, with the real subject surviving only in a _migration_alt field — a live instance of the leaky anti-fabrication gate CLAUDE.md §0 names.

17. Out of scope but blocking a citation this audit had to read around: CLAUDE.md §§4-7 were deleted 2026-08-05 with disposition HELD (ED-IN-0147), and module_contracts.yaml's engine_clock gap_note still cites 'the temporal-spine gap CLAUDE.md §6 names'. Recorded as an IN-lane citation-rot item, not ruled on.

---

## 4. What this run did not cover, and what it got wrong

Stated plainly so a reader can tell a clean surface from an unread one. The synthesis stage authored
these against its own output.

1. LANE COVERAGE IS PARTIAL AND UNEVEN. Twelve lanes reported (A1-A4, B1-B5, C1-C3). The lens pass is described as 19 domain lenses but only about 14 are visible in the findings. Lenses named in lane titles that produced NO finding: world history and threadwork. Treat those as unread, not clean.

2. WHOLE SUBSYSTEMS PRODUCED NOTHING. No finding in this register comes from combat (PC lane), social_contest (SC lane), fieldwork/investigation, threadwork, articulation/UI, npcs beyond the relational graph, or victory beyond the Altonia residual. Given that the faction and settlement rungs — the ones that WERE swept — yielded ~50 gaps, the absence of findings from six subsystems is a coverage fact about this run, not evidence those surfaces are clean.

3. PROVENANCE WAS NOT VERIFIED FOR ANY CITED PP NUMBER. Findings cite PP-666, PP-724, PP-687, PP-726, PP-632, PP-684/685, PP-688, PP-510/519, PP-674 and others as authority. CLAUDE.md §0 records that 433 of 452 distinct PP-NNN numbers cited in live surfaces resolve to no register on main since the 2026-08-05 evacuation, and validate_ed_citations.py is scoped to ED only. I verified ED citations by hand where a verdict turned on them (ED-686's ID-CONFLICT, ED-711, ED-632/633, ED-898, ED-IN-0096, ED-IN-0026) and did NOT verify a single PP number. Every PP-backed claim in this register inherits that unverified status.

4. SURFACES NOBODY OPENED, per the critics' own disclosure plus my checks: references/ENGINE_ATLAS.md; tools/observability/PROPOSALS.md and DECISIONS.md (I read only INCOMPLETENESS.md, which immediately falsified two 'none found' claims); systems/_architecture/key_echo_armature_v1.md §3, the corpus's canonical route for proposing registry deltas, against which no proposal here is shaped; and the per-subsystem flow-skeleton §7 traced-gap tables for world, factions, victory and settlements, which between them already carried at least nine gaps that lanes reported as untracked. One critic also declined to open key_substrate_v30.md, propagation_spec_v1.md, KEY_INDEX.md and CONTRACT_INDEX.md, and read descriptor_registry.yaml only at :92-149.

5. THE 'EXISTING TRACKING' FIELD IS SYSTEMATICALLY UNRELIABLE IN THE INPUT. Roughly a dozen findings asserted 'none found' after grepping registers/editorial_ledger*.jsonl ONLY. This corpus also files findings in surviving audit units (audit/2026-07-13-multi-agent-audit, audit/2026-08-08-world-churn-audit), in per-subsystem flow-skeleton §7 tables, in tools/observability/INCOMPLETENESS.md, and in module_contracts.yaml's own gap_notes. I corrected every instance I could check; I did not re-check every 'none found' in the set, so some remaining novelty claims in this register may still be overstated.

6. NO FINDING WAS VERIFIED BY EXECUTION. Every 'zero production callers', 'unreachable in a fresh campaign' and 'orphan' claim rests on grep plus the flow-skeleton documents' own instrumented measurements, which I read but did not re-run. I ran no campaign, no pytest suite, and no seeded simulation. The one executable defect I assert as a bug (G-18, the registry flow-list parse failure) was verified by reading the parser, the apply_defaults call and the two affected registry lines — the failure mode is traced, not observed.

7. RANK ORDERING IS COARSE BELOW ABOUT G-14. Rediscovery counts are honest where lanes genuinely converged (G-01 at 4; G-02, G-03, G-04, G-05 at 3), but the input labelled ALL findings 'rediscovery 1', so every merge is my reconstruction from lane labels and claim content rather than a recorded fact. The critics independently flagged the same accounting error and put the true distinct-gap count near 13-14 for the clusters they saw. Single-lane rows are ordered by ladder-blocking and by the scripting-drift rule, which is a judgment call; two readers could reasonably reorder G-25 through G-50.

8. THREE CLAIMS WERE OVERTURNED AND DO NOT ENTER AS FILED. (1) 'No field anywhere lets a faction declare a unique action as data' — false; registers/mechanics_index.yaml:939-966 is exactly that map, verified verbatim, and the lane grepped only two files. Re-entered as G-16, a routing defect against an existing primitive. (2) 'Settlement.subnational is the real, built mechanism for cross-scale claiming' — false; the identifier occurs three times in registry.py, all serialization, with no write site. Its underlying schema gap re-entered as G-36. (3) The Altonia claim's load-bearing citation (victory_v30.md:468 gating on 'Altonian diplomacy') is fabricated — grep confirms the string does not occur in that file, and the term names an existing Church-side track that one registry lists as Struck. Re-entered as G-14 at the residual only. A fourth, the NPC dual-grain residence claim, enters as G-50 with disposition not_a_gap because its premise (generate_npc is production-populated) is contradicted by an xfail-pinned measurement.

9. TWO PROPOSALS IN THE INPUT WOULD HAVE CAUSED DAMAGE IF EXECUTED AND ARE FLAGGED RATHER THAN SILENTLY DROPPED: the templar fix (a spiritual_weight threshold would site the station in Askeheim, an uncontrolled settlement-less calamity epicentre, because the stated 'T9 is highest of all 17' is false — T15 is 5, verified by full census), and the Franchise fix (wiring three keys' consuming_systems, the exact defect ED-IN-0096 reversed). Several others proposed 'provincial' as a default_scale_signature value, which invariant 7 would reject at runtime, or a 'ledger' bucket absent from the four-value enum. I stripped these; a reader should assume similar defects survive in the proposals for which I had no critic verdict.

10. ONE STRUCTURAL LESSON THE REGISTER ENCODES BUT SHOULD STATE PLAINLY: two lanes independently reasoned from a key's optional_payload_fields table to 'this key cannot carry a multi-target fan-out', when the substrate's targets[] array (key_substrate_v30.md:45-53) is precisely that channel and the cited resolver already populates it. Any future sweep of this schema must read key_substrate_v30.md before concluding a key type lacks a capability, and must read mechanics_index.yaml and INCOMPLETENESS.md before asserting that a field or a tracking item does not exist.

---

## 5. Lane coverage

| lane | findings | surfaces reported clean |
|---|---|---|
| A1 — the character rung and every binding out of it | 7 | 4 |
| A2 — Settlement, Settlement Faction, Settlement Governance | 5 | 5 |
| A3 — Territory/Province, Provincial Factions + Governance | 5 | 5 |
| A4 — national factions, national governance, cross-scale spine | 7 | 3 |
| B1-interior-life | 7 | 4 |
| B2-social-order | 7 | 6 |
| B3-material-and-martial | 5 | 4 |
| B4-governance-and-relations (LENS-FIRST SWEEP: politics · geopolitics  | 9 | 5 |
| B5-dynamics (events · threadwork · churn seam), World-Schema Gap Audit | 8 | 6 |
| C1 — What makes a character unique and consequential (Lane C: Individu | 3 | 6 |
| C2 — What makes a faction unique and consequential, at every tier | 6 | 5 |
| C3 — settlements/territory/world individuation (schema-vs-world-model  | 6 | 6 |

A high `clean` count next to a low finding count is the honest signal this audit wanted: it means the
lane checked things and found them adequately keyed and contracted. `clean` is not the same as
unread — `coverage` notes in the run's return value record what each lane did and did not reach.

---

## 6. What the critics found that the producers missed

The read-only `valoria-critic` pass returned 43 items the producer lanes never reached. The most
load-bearing are folded into the register; these are recorded because they are corrections to
*method*, not to individual claims:

- **Every `propose_key` row is gated by a precondition none of the producers mentioned** — §10's
  ratified `rendering_dispositions.yaml` requirement. Registered as **G-17**.
- **The substrate already carries the channel two lanes asserted was missing.** `key_substrate_v30.md`
  §45-53 defines `targets[]` with per-target `impact_vector` and `stat_delta`; two lanes reasoned
  from a key's `optional_payload_fields` table to *"this key cannot express a multi-target fan-out"*
  without opening the substrate spec. **Any future claim that a key cannot express an arity must
  cite the substrate, not the type entry.**
- **`ledger` is not a bucket.** The bucket vocabulary is exactly `{derived_value, track, clock, pool}`
  across all 39 state rows. Two proposals invented a `ledger` bucket — new enum vocabulary presented
  as though it existed. Folded into **G-24**, which asks whether the taxonomy gains a relational shape.
- **Every key-type proposal carries an unstated regeneration obligation:**
  `engine/engine_params/key_types.json` is GENERATED from the registry via `tools/export_key_types.py`.
- **`references/npc_registry.yaml` is the character-identity surface nobody opened** — it declares
  itself *"Canonical source of truth for ALL named characters"* with an enforcement rule. Registered
  as **G-20**, and it materially changes the character-identity finding.
