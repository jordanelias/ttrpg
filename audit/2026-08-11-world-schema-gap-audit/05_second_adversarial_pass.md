# Second adversarial pass — checking what the first pass never checked

## Status: REFERENCE — verification of already-filed claims. **Ratifies nothing.**

**Date:** 2026-08-11 · **Lane:** IN · **ED:** ED-IN-0157 · **Base:** `c26a22c` (post-merge)

The first review pass checked what the register *asserted*. It did not check the register's
**residuals** — the list in `02` §4 of what the run never did. Those residuals were themselves
unverified claims. This pass tests them.

Two read-only `valoria-critic` agents plus two measurements only a Bash-capable session could run.
Every overturn below was **re-verified by hand** before being recorded here.

---

## 1. `existing_tracking` — 22 "none found" rows checked, 2 overturned, 3 softened

Residual `02` §4 item 5 confessed the field was unreliable and never re-checked it. It is now checked.

| row | verdict | what actually tracks it |
|---|---|---|
| **G-19** | **OVERTURN** | `registers/supersession_register.yaml:227-230` registers PP-632's Knot tier-cost model (`Loose/Medium/Close`) as superseded by **ED-912**, 2026-06-28 — verified by hand. The row's own *Evidence* field even quotes `knots_v30.md:58` saying *"Supersession logged in canon/supersession_register.yaml"*. **The row contained the pointer its tracking field denied.** |
| **G-36** | **OVERTURN** (as worded) | `audit/2026-08-10-subsystem-atlas-verification/code_strategic.md:111-114` independently measures `.subnational` as left at dataclass default with no writer. The row's grep scope was ledgers + index files — precisely the scope residual §4 item 5 said was too narrow. |
| **G-25** | **SOFTEN** | `tools/observability/INCOMPLETENESS.md:336` carries *"Church Attention Pool — in 19 docs, unregistered (IN)"* — **the same file, same format, two lines from** the `Casus Belli` entry at `:334` that the audit **did** harvest into G-06. Verified by hand. The audit read the file and took one entry, not the other. |
| **G-44** | **SOFTEN** | `settlements_flow_skeleton_v1.md:142` already files the referential-integrity half. |
| **G-13** | **SOFTEN** | ED-SC-0030 and `characters_flow_skeleton_v1.md:149` both track the 13-vs-9 conviction-shape seam. |

**17 of 22 upheld**, the strongest being **G-37** (`controller_subordinate` occurs at exactly one
non-audit location repo-wide) and **G-18** (the parser defect, mechanism verified end to end).

### 1.1 The sharpening on G-19 is worth more than the overturn

`supersession_register.yaml:238-240`'s `files_to_recheck` lists only `fieldwork_v30.md` and
`engine/params/fieldwork.md`. **`key_type_registry_v30.md` is absent from it.** That omission is the
*nameable mechanism* by which a struck enum survived in `meta.knot_formed`'s payload and propagated
into the generated `key_types.json` export. "Nobody filed it" was the weaker claim; "the recheck list
that would have caught it omits the registry" is the finding.

---

## 2. The reverse error — rows citing a real ID whose content does not support them

**Worse than "none found", because a citation looks verified.** Four found; all re-verified by hand.

**G-49 cites a line that says the opposite.** It cites
`audit/2026-07-13-multi-agent-audit/_workings_joined.md:978` as tracking for *"read by zero lines of
Python"*. Read in full, that line says `institutional_culture` *"is narrow (single-consumer: feeds
only α_institution) **but is consumed, not orphaned**"* — it appears under the orphaned-mechanics
heading **in order to exclude the field from it**.

⚠ But the disagreement **sharpens G-49 rather than weakening it**: that audit's "consumed" is
design-level (it feeds α_institution in the formula), while this session measured **zero Python
readers**. Design-consumed and code-unread is exactly the gap G-49 describes. The citation is
reversed *as tracking*; the underlying finding is stronger, not weaker.

**G-44/G-45 cite an anchor that does not exist.** They cite OI-37 at
`registers/handoffs/HANDOFF_SE.md:127-134`. Measured: **`HANDOFF_SE.md` contains zero occurrences of
"OI-37"** (`grep -c` → `0`). The mis-attribution is inherited verbatim from a stale code comment at
`systems/overview/sim/accounting.py:35`. **The audit propagated a code comment's citation without
opening the file it cited** — on the very module where it separately *did* catch a stale citation.

**G-17/G-20 cite a line anchor into a JSONL ledger.** They cite ED-IN-0153 at
`editorial_ledger_in.jsonl:57`; it was at `:54` then and is at **`:50` now**, because this session
archived settled entries. **A line anchor into an append-and-archive ledger is structurally unstable**
— cite the id, never the line.

**G-35 rests on two IDs that are themselves unresolved.** ED-632/ED-633 both carry
`"_migration_flag": "ID-CONFLICT: multiple distinct descriptions — Jordan resolve"` — the same defect
class the audit elevated to a held decision for ED-686, sitting on the two IDs G-35 uses to assert the
mechanic is "closed as CANON".

**And one self-contradiction:** **G-50** dispositions `not_a_gap` the exact claim ED-IN-0153 — the
audit's own instrument entry — asserts as measured fact (identity recorded twice at two grains with no
bridge). It overturns its own ED without recording that it is doing so.

**The register's strongest layer, by contrast:** every flow-skeleton and code anchor opened matched
verbatim. The failures cluster entirely in **ledger/handoff line anchors** and in one reversed prose read.

---

## 3. "Unread, not clean" — the residual is right in direction and wrong in detail

| residual claim | verdict |
|---|---|
| lenses `world history` and `threadwork` produced no finding | **half OVERTURNED** — `world history` appears in G-14's own lens line. `threadwork` upholds. |
| no finding from **victory** beyond Altonia | **OVERTURN** — G-34 files against victory's own state block; G-27 reads its four gates. |
| no finding from **npcs** beyond the relational graph | **OVERTURN** — G-39 is against the `npc_memory` contract; G-29 proposes a key `npc_behavior` emits. |
| no finding from **fieldwork** | **SOFTEN** — G-19's subject is `meta.knot_formed`, whose emitter is `fieldwork_knots`. True of *lane labels*, false of *subject matter*. |
| nobody opened `ENGINE_ATLAS.md` / `key_echo_armature_v1.md` §3 | **OVERTURN at unit level** — both are cited accurately (G-17 quotes §3's 12-row table precisely). True of the *producer lanes* only. |
| nobody opened `PROPOSALS.md` / `DECISIONS.md` | **UPHELD** |
| combat · social_contest · threadwork · articulation · UI | **UPHELD — genuinely unread** |

⚠ **One error this pass found in `04`:** §8 says *"`ENGINE_ATLAS.md` and the flow skeletons cover
[direct imports]"*. **ENGINE_ATLAS has no import map** — its sections are coverage, subsystem atlas,
declared-vs-executed, authored-coverage, attribution and nomenclature. Corrected in place.

### 3.1 Seven unfiled gaps in the "unread" surfaces — observations, not filings

The residual said *unread, not clean*. That was the right call: reading them found seven gaps of the
register's own classes. **None is filed here** — several straddle lane boundaries, and the G-33
precedent (`module_contracts.yaml:566-572` reserving MB's rows to the MB lane) says that is not IN's
call.

- **N-1 · combat.** `scene.combat_resolved`/`_felled`/`_hit` declare `emitting_systems:
  [personal_combat]`, but the sole constructor is `engine/cross_scale/echo_transport.py:416`, and
  **`echo_transport` has no row among the 27 contracts** while the key registry names it an emitting
  system elsewhere. The declaration names the **wrong owner** — admissible under `00` §1, and the same
  shape as G-45.
- **N-3 · threadwork.** `World.threadcut_beings` and `World.comovement_deck` are real, serialized,
  restored per campaign, and the threadwork contract's own comment **explicitly disclaims them**.
  This is `World.treaties`/G-07 exactly, one subsystem over, in a lens called unread.
- **N-4 · Composure.** Keyed as `composure_damage` in `meta.knot_ruptured`'s payload and noted
  *"gameplay-load-bearing"*, yet registered only as a bare name in `descriptor_registry.yaml:186`'s
  21-member `not_descriptors.derived_values` block, with **zero occurrences in `module_contracts.yaml`**.
  ⚠ **This exposes a scoping defect in held decision 5**, which asks whether the 7-member
  `not_descriptors.tracks` block is swept **and never mentions the structurally identical 21-member
  block on the line above**. Ruling on one block and not the other special-cases a block — the same
  objection G-05 raises to promoting Renown alone.
- **N-5 · articulation.** The contract declares its wildcard consume with an inline claim of *"31
  explicit per-type subscriptions"*; the code subscribes **13**. G-42 filed the registry-side wildcard;
  the contract-side one is unfiled.
- **N-6 · victory.** The fallback winner-decision is inline procedural code in `engine/mc_v18.py:276-286`
  and appears in no contract — so in every campaign not decided by GD-1, **the game's outcome is
  computed by a formula no contract owns**.
- **N-2 · fieldwork** (two state rows implemented in a sibling module with no contract row) and
  **N-7 · UI** (no contract row and no `CURRENT.md` row at all) complete the set.

**Sizing, with the instrument named:** `ENGINE_ATLAS.md`'s generated per-subsystem traced-gap counts
for the eight "unread" subsystems total **71 already-traced gaps**. Not all are schema-class; this
sizes the unread surface rather than claiming 71 schema gaps.

---

## 4. PP provenance — residual `02` §4 item 3, now measured

The residual said no cited PP number was provenance-verified. Measured:

- The audit cites **11 distinct PP numbers**. **6 resolve** to a register entry (2 in
  `patch_register_active.yaml`, 4 in `patch_register_index.md`). **5 do not**: PP-687, PP-510, PP-519,
  PP-723, PP-688.
- **The 5 are evacuation casualties, not fabrications.** Each is heavily cited across the live tree —
  PP-687 in 29 files, PP-688 in 17, PP-723 in 11 — so their entries went to fork ref `c451bcb`.
- **Nothing catches either case:** `tools/validate_ed_citations.py` has **no PP handling at all**.

The residual pointed at CLAUDE.md's *"433 of 452"* as if the audit's citations were probably
unresolvable. **More than half resolve.** The residual was right to flag the risk and overstated it.

That check then found a larger defect, filed separately as **ED-IN-0156**: CLAUDE.md asserts **13
countable figures and none is guarded**, and three of three re-measured are wrong or scope-ambiguous —
including `433 of 452` itself, which reproduces only against the 6-entry active register and is
**328/466 (70%, not 96%)** once `patch_register_index.md`'s 196 entries are counted.

---

## 5. What this pass did not check

- **It ran nothing against the engine.** The residual *"no finding was verified by execution"* stands
  **unaddressed**: I began the campaign-execution check to verify `04` §3.2's emit ledger empirically
  and did not complete it. Every emit/reachability claim remains static analysis.
- Both critics ran read-only (`Read, Grep, Glob`) and neither could execute a test, a validator, or a
  campaign; every "zero hits" in §1–§3 is a grep.
- 8 of 15 `§7 Traced gaps` sections and ~140 of 146 `audit/**` files remain unread.
- Anchors were checked against **today's tree, not base `63c26a22c`** — which is how the G-17/G-20 line
  anchor was found to have moved, but also means anchor drift cannot be fully excluded elsewhere.
- **No third pass has been run.** Two passes found 14 and then ~12 defects respectively. That
  sequence is not evidence of convergence.
