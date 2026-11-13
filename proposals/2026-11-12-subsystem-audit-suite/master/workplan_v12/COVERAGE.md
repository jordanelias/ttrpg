# Workplan v12 — coverage: does v12 carry every RESOLVED-BY finding and every v11 intake id?

## Status: WORK FILE (lane: coverage, one round; answers Jordan's two questions of 2026-11-12; resolves nothing at runtime, CLAUDE.md §0.05; deleted when v12 is adopted)

## Read at: the working tree of 2026-11-12 (branch `ccr-62958c70-0kjhsw`), with the body parts `workplan_v12_part3.md` .. `_part43_cont.md` as they stood at 23:30–23:50 (1,353 item handles indexed at the last run). A patch lane (`PATCH_LOG.md`, P-01 to P-34) was editing the same directory; every part this lane edited was re-read just before the edit.

**The two questions (Jordan, 2026-11-12).** (1) The master-findings lane "could not place 132 RESOLVED-BY rows in a batch", and 77 findings have no parseable severity: does that mean they are not part of the workplan and will not be built? (2) Does v12 fold in every non-superseded item of workplan v11?

**The rule this file checks** (`UNIFICATION_BRIEF.md`, closure): every finding has one disposition, and RESOLVED-BY means a proposal carries the exact edit and a gate. A RESOLVED-BY row is built only if a v12 item carries its proposal's edit; a v11 intake id is built only if a v12 item (or the head) carries its carry-forward block.

## The answers

**(1) No: the 132 rows were unplaced by the master-findings extract, not by the plan.** Opened one by one (Appendix B): 62 are carried by named v12 items, 1 is carried as content (a pike is a content row, `U5b:190`), and 69 owe no edit of their own (a "no edit" decision of the audit, a pointer to rows that are themselves carried, or a reference to a whole part of the closure table). None is uncarried. Their batch cells in `master/MASTER_FINDINGS_part3.md`..`_part6.md` now name the batch and items, or "none owed (a pointer)". **The 77 findings with no severity** (76 rows) were never outside the plan: every one already named a batch (72 RESOLVED-BY, 3 SUPERSEDED, 1 JORDAN since answered). Their severity was missing because 13 sit in a table whose severity is a column (`audits/16_PESSIMIST_FI.md:757`) and 5 rows under a table whose grade is stated once above it (`audits/14_VERBS_MILITARY.md:100`, "degrades narrative"): those 18 rows now carry B, D or H. The other 58 rows' audits grade by a different scheme ("Layer-1 conformance", "goldens", "design (NERS N)", "standing rule", …): they read "unrated in source" (Appendix D gives each audit line). Severity orders work; it does not decide whether it is built.

**(2) Yes, with the held items held on purpose.** The intake (`master/eval/V12_INTAKE.md` §5) is the list of v11 and gap-register items the evaluation settled as STILL-NEEDED or MISSING-DEP, that is, the non-superseded ones: 273 entries, 297 ids. Every id is placed (Appendix E): 22 are head rules carried by `workplan_v12.md` §3.A; 221 are carried by items (194 by build, design, content or reading items; 12 by pointers to a named item; 10 by BLOCKED items with an owner; 5 by HELD items with a trigger); 54 are the intake's own "held / LEAVE" entries, which are by rule not items (`V12_STRUCTURE_part2.md` §5.6) but rows of H2's held table. The 37 ids an earlier scan found absent verbatim are 3 head rules, 31 held entries (H2's table), and 3 entries carried under the authors' citation of the intake line (the two §2 FA entries, B21b.14–.15 and B21c.05, .09; P16 §3.4, B11F1.06).

**What the check found and fixed.** Three pieces of carrying proposals were in no item, though their batches were named: `U5a_tests_digest_additions` §G (H-172's test arm, "§G in B08"), `27_MB_A` item 27A-6 (the `command` skill row and the host builder `command_record`, which B22.21 and B22.26 depend on), and `U5b_PC_residue` §1 item 3 with the `READ_SCALE` fit ("the fit (item 3) with B15"). Each is now an item (§C: B08.06, B19.70, B15.15).

## Counts

| scope | rows / ids | COVERED | CONTENT-OWED | POINTER-ONLY | HELD-TABLE | SUPERSEDED | UNCARRIED |
|---|---|---|---|---|---|---|---|
| RESOLVED-BY rows, `U5a` | 377 | 356 | 0 | 20 | 1 | 0 | 0 |
| RESOLVED-BY rows, `U5b` | 276 | 272 | 1 | 2 | 0 | 1 | 0 |
| RESOLVED-BY rows, `U5c` | 309 | 295 | 1 | 13 | 0 | 0 | 0 |
| RESOLVED-BY rows, `U5d` | 425 | 376 | 0 | 49 | 0 | 0 | 0 |
| **all RESOLVED-BY rows** | **1,387** | **1,299** | **2** | **84** | **1** | **1** | **0** |
| of them, MF's 132 unplaced | 132 | 62 | 1 | 69 | 0 | 0 | 0 |
| v11 intake ids | 297 | 243 (22 head, 221 items) | — | — | 54 | — | 0 |
| instruction suite and codebase handles | 129 | 125 (114 items; 11 pointer rows whose targets are items) | — | 1 (IS-MB-B4) | 1 (IS-PC-B1, HD-33) | 1 (IS-MB-06) | 0; IS-A-13 is B99 (A44) |

**Percentages.** Of the 1,303 RESOLVED-BY rows that owe an edit (1,387 less the 84 that owe none), 1,301 are carried by a named item (99.8 %); the other two are held for B99 (`U5a:140`) and superseded (`U5b:325`). Of the 297 intake ids, 243 are carried (81.8 %) and 54 held by the intake's own rule (18.2 %). Of the 129 suite handles, 125 are carried.

**The rows and ids not carried by an item, each with its disposition.**

| row or id | what | disposition |
|---|---|---|
| `U5a:140` (ARC-44, EMG-C4, EMG-C3, EMG-X8, ARC-20) | `01_CORE_claim_fade_as_read` Edit 5: lift `MAX_SEASONS` to 16 once the gate reads flat over eight seasons | HELD for B99: `H2_DECISIONS.md` HD-26 ("B99, the longer re-take"; B98 lists it `BLOCKED (A-114: past two seasons)`); B09 says why it is not carried (part 11_cont, B09 UNDECIDED (1)) |
| `U5b:325` (CL-TROOP, MB-08, CR-52, CP-T04-04, CP-T04-10) | `U5b_MB_residue` §7: edits to v11 plan cards | SUPERSEDED: v12's adoption deletes the v11 files those edits target (part 11, B17 UNDECIDED (3)); CR-52 and the two CP-T04 ids are intake ids, placed in Appendix E (CP-T04-04 and CP-T04-10 held) |
| `U5b:190` (F-PC-20) | `03_PC_weapon_records_in_the_export` item 6: a pike | CONTENT-OWED: "Roster coverage is **not** built here. A pike is authorable today … and is content"; B14.12 lands the export; the matchup rows are A-113's (B19a, B19, B31) |
| `U5c:285` (R-31) | one skill for three inquiries | CONTENT-OWED: "no engine edit owed: authoring (two data rows on the capability surface U1 decides)"; the verb rows' skill values land with B04.03 (CORE Edit 8) |
| 54 intake ids under "held / LEAVE" | Appendix E, class HELD-TABLE | HELD for H2's held table (§7.9), each with the trigger its entry names |
| IS-PC-B1 | PB step 3d, the `measure` lean | HELD: `H2_DECISIONS.md` HD-33, "one held-table row each, with its owner lane" (PC) |
| IS-MB-06 | `prowess_of` arithmetic | SUPERSEDED by A-100 (MBA-04): struck in `master/instructions/IS_B1_PC_MB_DICE_part2.md:5` |
| IS-MB-B4 | two unread sites, read at landing | a reading owed to the landing sessions of B22 and B19 ("nothing; each proposal says which function"); B22.04 cites it |
| IS-A-13 | the longer re-take of the nine | B99 (part 44, lane A44, not yet written); `workplan_v12.md` §6 names it |

**Closing statement.** Every RESOLVED-BY finding of `U5a`..`U5d` (1,387 rows) is carried by a named v12 item (1,301, two of them as content), owes no edit of its own (84, each listed with its ground in Appendices B and C or matched by its "no edit" text), is held for B99 by `H2_DECISIONS.md` HD-26 (1 row), or is retired as superseded because the v11 cards it edits are deleted on adoption (1 row). Every one of the 297 v11 intake ids is carried by the head's §3.A (22), by an item (221; 15 of them BLOCKED or HELD with a named owner or trigger), or held for H2's held table by the intake's own "held / LEAVE" rule (54). This is true at the level this lane checked: a row is matched to the items that carry its proposal and, where the row names an edit or section, to an item whose source names it (§A.3 states what that does not see).

---

## A. The closure rows

**A.1 Method.** Appendix A's `closure` mode reads every table of `unified/U5_FINDINGS_CLOSURE_U5a.md`..`_U5d.md` whose header has a `disposition` column and takes each row whose disposition cell contains `RESOLVED-BY`: 1,387 rows, equal to the master-findings count (`master/MASTER_FINDINGS.md` §0). The carrier cell is split at `;` and each clause resolved to proposal files by (a) the file stem, (b) the closure tables' own abbreviation paragraphs (`**DECREE** = `06_FA_decree_binds.md``, `T1 = …`, `PES-A…D = 16_PESSIMIST_PC_A…D_*`), applied in reading order with single-letter names (`A`, `B`, `C`) dropped at each heading so they never leak into "Part B" or "Edits A–B" (the defect `MASTER_FINDINGS.md` §0 reports and fixed in its own extract), (c) the v12 parts' own short-name lines (`**SQUAD** `proposals/04_MB_squad_grid_of_named_characters.md``, shared by a part and its `_cont` files) and the authors' family aliases (BYZ_D, PAP_B, HAP_C, S1-C, CAP, MAP, UPR, UMR, HEAR_B, VEN-E, COL-F, PAP-G, BYZ-G), and (d) "same file", "as F-…", "§A row n" (U5a's owed-edits file), "U1 architecture §n" and a v11 id in the carrier. Each stem is mapped to the items whose heading, `SOURCE:` line or position-table source cell names it; where the clause names an edit, section, part, step or row (ranges expanded), the items whose source names the same token are preferred. The index finds an item for every one of the 300 proposals.

**A.2 Rows resolved by hand.** 55 rows (Appendix C): the 34 the script could not resolve, and rows whose section token matched no item, whose match was imprecise, or that were re-pointed after this lane added items (14 script matches whose section token matched no item were opened and left as the script mapped them). Each was opened in its closure table and its carrier's section, and the v12 parts were searched for the edit.

**A.3 What this check does not see.** A proposal-level match says an item carries the proposal; it does not prove that every edit of the proposal is in some item. A second check (Appendix A `lands`) read each proposal's own `**Lands in batch:**` line and asked whether every batch it names for its own pieces has an item of that proposal: of 18 flags, 15 named another proposal's batch as an ordering or were carried under another proposal's name (EXITS Part C by `14_VERBS_MATERIAL_A` §6, B12c.06; CHAR Part A's sheet `terms` by GO-B's `Offer`, B34.02; `11_GO_float_contract` gate 2 by B41.06; `U5a_CORE_owed_edits` §I by B03.65 with B21.72 and B34.04, P-29), and three were real gaps, now C-01 to C-03. A census of every numbered edit of all 300 proposals against the items was not run; a gap of the same kind can remain where neither the closure row nor the proposal's Lands line names the piece. Appendix B's handles for script-resolved rows are the proposal's items with the best section match and may include a neighbouring item of the same proposal.

## B. The v11 intake

Appendix A's `intake` mode parses the 273 `- **ids** · …` entries of `master/eval/V12_INTAKE.md` §5 (297 ids; the entry "§2 the arcs (55 numbers, 58 ar…" is one id that a comma splits) with the heading each sits under, and looks each id up in every item's heading, `SOURCE:` line and position row, verbatim or by the authors' citation of the entry's line (`the intake `:317``). The 22 head rules were checked against `workplan_v12.md` §3.A by hand (P1 to P12, P14 to P16, V1 to V4 each a row; "risk 2" is cited in V1's row, "risk 4" and "risk 6" are rows). The 54 held ids are exactly the intake's own count of held entries ("54 are held", `V12_INTAKE.md:7`). The 15 ids carried by BLOCKED or HELD items are listed with their owners in Appendix E (B03.69, B10.76, B10.79, B12c.30 BLOCKED; B11F2.10, B11F2.11, B21c.08, B12b.26 HELD); each pointer item (12 ids) was opened: it points at a named item (B02.35 → B02.13; B11F2.01 and B11F2.04 → the block's RULES line and the items that edit each file, e.g. B11F2.05; B21b.03 → B21b.02; B21b.09 → B21b.08; B21b.19, B21b.20 → B21b.18; B35.21 → B35.10, B35.20) or records the answer that closes it (B21.78: M38's marquis half "ANSWERED (step 3): canon stands"; B10.78: H-185 settled done in code, H-191 the BLOCKED B10.75). Not checked: whether each item's INSTRUCTION copies its entry's carry-forward block in full.

## C. Items added, and what is left for H2, A44 and the patch lane

| marker | item added | part | ground |
|---|---|---|---|
| C-01 | **B08.06** — the lap stamp earns its test arm or the arm goes (H-172), `U5a_tests_digest_additions` §G | `workplan_v12_part23.md` (position row and item, before B08.99) | closure row `U5a:840` names TDA §G; the proposal's head: "§G in B08 with `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`"; no item carried it |
| C-02 | **B19.70** — the `command` skill row, its three `field` use rows, and the one host builder of a `CommandRecord`, `27_MB_A` item 27A-6 | position row in `workplan_v12_part27.md` (after B19.65); item in `_part27_cont.md` (before B19.66) | `27_MB_A`'s head puts 27A-6 in B05; no B05 item carries it; its `field_input` edit needs B19.02's fields, so the dependency decides the batch (E-8); closes `U5b:437` with B19.02–.05, .55; B22.21 and B22.26 depend on it |
| C-03 | **B15.15** — the slope bound joins the lever table; `READ_SCALE` is fitted; the two wound values stated side by side, `U5b_PC_residue` §1 items 3, 5 | `workplan_v12_part18.md` (position row and item, before the Readings block) | the source: "the fit (item 3) with B15"; B14's DIALS line says `READ_SCALE` is "set by B15"; `U5b:223` names "the slope bound as the calibration rule" |

Retired with a stated ground: none beyond the table above (`U5b:325`, IS-MB-06).

**For H2 and A44 (this lane edits no other author's item or batch head).**
- B08: the position count is 7; B08.99's "B08.01 to B08.05" (its row and DEPENDS ON), the SERIAL EDGES line (B08.04 → B08.06 → B08.99) and EST want B08.06; the file census gains `engine/season/tests/test_season_shape.py` for B08.
- B15: B15.99's "B15.01 to B15.14" wants B15.15; B15's file census gains `systems/combat/combat_engine_v1/workbench/build_levers.py` and, if the fit moves the value, `modules/combat/config.py` and `engine/engine_params/combat_engine_v1.json`.
- B19: B19.99's "B19.01 to B19.69" wants B19.70; B19's file census gains `references/descriptor_registry.yaml`, `engine/season/rosters.yaml` (`tables.capability_uses`) and `engine/season/seam/wrappers/mass_battle.py`; `27_MB_A`'s Lands line ("27A-6 in … B05") is superseded by B19.70 for the plan's purpose.
- H2's held table: the 54 held intake ids (Appendix E) and IS-PC-B1 (HD-33).
- A44: B99 reads `claim_fade` edit 5 (HD-26) and is IS-A-13.
- The master findings' prose: `MASTER_FINDINGS.md` §0 ("the other 132 … printed with **—**") and `_part2.md:75` ("77 of the 439 rows … printed **—**") are now stale; this lane edited only the two columns its brief names.
- The patch lane: `U5a_tests_digest_additions` §D3 ("The revert goes in the commit that lands that draw": drop `revert_cp_t03_08` from `engine/season/tests/test_territorial_subsistence.py` in the commit of the `tend` draw, B12c.06) is in no item; its closure row (`U5a:875`) is SUPERSEDED, so it is outside the RESOLVED-BY rule, but it is one line of B12c.06.

## D. The instruction suite and the codebase items

Appendix A's `suite` mode: 129 handles (`IS-A-01`..`-13`, `IS-B2-…`, `IS-B3-…`, `IS-DICE-…`, `IS-MB-…`, `IS-PC-…`, with their `-Pn` pointer rows and `-Bn` blocked rows; CI-01..CI-11; MBA-01..MBA-09; PCR-1..PCR-4). 114 are named by an item (Appendix F; CI-01..CI-11, MBA-01..MBA-09 and PCR-1..PCR-4 all are). The eleven pointer rows name no item by their own handle because each points at a proposal whose items carry it: IS-DICE-P1 → B05.03; IS-DICE-P2 → B06.03, B06.04 (with CI-06, B03.67); IS-DICE-P3 → B05.01, B41.06; IS-DICE-P4 → B03.12; IS-DICE-P5 → B05.60; IS-MB-P1 → B05.08–B05.11 then B19.70 (C-02); IS-MB-P2 → B19.66 (27C-2, in B19's order); IS-MB-P6 → B05.03, B19.12; IS-PC-P1 → B30.03, B30.10; IS-PC-P4 → B18.02–B18.05; IS-PC-P5 → B13.01. The other four are in the table under "Counts".

## E. Severities

Appendix A's `grades` mode opened the defining line of each of the 77 finding ids in `audits/` and wrote the audit's grade into the `sev` cell where the audit states one (Appendix D). The suite's grades are B (blocks a requirement), D (degrades narrative), H (hygiene) (`AUDIT_BRIEF.md`; `MASTER_FINDINGS.md` §0). F-PES-FI-01 is graded "blocks R-05; degrades R-01, R-07" and is written B.

---

## Appendix A — the script

Run from `proposals/2026-11-12-subsystem-audit-suite/` (reads only; no pytest, no engine run): `python coverage_check.py index | closure | final | intake | suite | grades <file> | lands | show <stem> | find <regex>...`. Kept here, not committed elsewhere (scratch copy in the lane's scratchpad). `HAND` is the table of Appendix C.

```python
#!/usr/bin/env python3
"""Coverage check for workplan v12 (lane: coverage).  Run from the suite root
(proposals/2026-11-12-subsystem-audit-suite/).  Reads only; prints TSV.

  python coverage_check.py index     -> v12 item index summary
  python coverage_check.py closure   -> one line per RESOLVED-BY closure row
  python coverage_check.py intake    -> one line per V12_INTAKE id
  python coverage_check.py suite     -> IS_*, CI-, MBA-, PCR- items

Method (closure): every table of U5a..U5d whose header has a `disposition`
column; a row is RESOLVED-BY when that cell starts with the code.  The carrier
is the next cell.  Carrier names are resolved to proposal stems by (a) the stem
itself, (b) the closure file's own abbreviation paragraphs (`**X** = `file``),
applied in reading order so a later definition replaces an earlier one, and
(c) family aliases used by the v12 authors (BYZ_D, PAP_B, HAP_C, S1-C, ...).
A stem is mapped to every v12 item whose heading, SOURCE line or position-table
source cell names it (or an alias of it); a section/edit token next to the name
in the carrier ("edit 3", "§2", "Part B", "step 4") picks among those items.
"""
import glob, os, re, sys
from collections import defaultdict

ROOT = '.'
STEMS = sorted(f[:-3] for f in os.listdir('proposals') if f.endswith('.md'))
STEMSET = set(STEMS)
PARTS = sorted(glob.glob('master/workplan_v12/workplan_v12_part*.md'),
               key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', p)])
HANDLE = r'(?:B\d\d[a-z]?(?:F\d)?|BA1|B16[LM]|B98|B99)\.\d\d'

# ---------------------------------------------------------------- aliases
def pat_to_stems(target):
    """`06_FA_decree_binds.md`, `16_PESSIMIST_PC_A_*.md`, `…_B_x.md` (needs prefix)."""
    t = target.strip().strip('`').replace('.md', '')
    t = re.sub(r'^proposals/', '', t)
    rx = '^' + re.escape(t).replace(r'\*', '.*').replace('…', '.*') + '$'
    return [s for s in STEMS if re.match(rx, s)]

# family letters: prefix -> stem prefix (v12 authors' and closure families)
FAMILIES = {
    'BYZ': '15_INSTITUTIONS_BYZANTINE_', 'PAP': '15_INSTITUTIONS_PAPACY_',
    'COL': '15_INSTITUTIONS_COLONIAL_', 'VEN': '15_INSTITUTIONS_VENICE_',
    'SYN': '15_INSTITUTIONS_SYNTHESIS_', 'HAP': '22_HAPPENINGS_', 'HAPP': '22_HAPPENINGS_',
    'PROC': '21_PROCEDURAL_', 'STORY': '23_STORY_', 'NARR': '20_NARRATIVE_',
    'S1': '14_VERBS_SOCIAL1_', 'S2': '14_VERBS_SOCIAL2_', 'VB': '14_VERBS_BINDING_',
    'BIND': '14_VERBS_BINDING_', 'M': '14_VERBS_MATERIAL_', 'MAT': '14_VERBS_MATERIAL_',
    'MIL': '14_VERBS_MILITARY_', 'PHY': '14_VERBS_PHYSICAL_', 'PFI': '16_PESSIMIST_FI_',
    'PES-FA': '16_PESSIMIST_FA_', 'PES-SE': '16_PESSIMIST_SE_', 'PES-WR': '16_PESSIMIST_WR_',
    'SC': '16_PESSIMIST_SC_', 'PC': '16_PESSIMIST_PC_',
    'FA': '16_PESSIMIST_FA_', 'SE': '16_PESSIMIST_SE_', 'WR': '16_PESSIMIST_WR_',
    'FI': '16_PESSIMIST_FI_', 'GO': '16_PESSIMIST_GO_', 'MB': '16_PESSIMIST_MB_',
    'CHAR': '16_PESSIMIST_CHAR_', 'CORE': '16_PESSIMIST_CORE_', 'DICE': '16_PESSIMIST_DICE_',
}
# letter-suffixed proposals outside FAMILIES whose stems carry the letter (27_MB_A, 28_.., 30_WR_A ...)
def family(prefix, letter):
    p = FAMILIES.get(prefix)
    if not p:
        return []
    return [s for s in STEMS if s.startswith(p + letter + '_') or s == p + letter]

# global aliases (used in v12 item text). Closure aliases are added per file below.
GLOBAL = {
    'CAP': ['U5a_capability_home_and_two_inputs'], 'U1': [], 'MAP': ['10_DICE_capability_axiom_map'],
    'DEF': ['02_CHAR_capability_definitions'], 'TWO': ['10_DICE_one_score_two_roles'],
    'ADV': ['10_DICE_advantage_sources_for_the_arcs'], 'UPR': ['U5b_PC_rulings_in_the_fight'],
    'UMR': ['U5b_MB_rulings_in_the_field'], 'HEAR_B': ['05_SC_playable_hearing_B'],
    'EVID_B': ['05_SC_evidence_and_rebuttal_B'], 'KERN_B': ['05_SC_sc05_kernel_disposition_B'],
    'FI_05_B': ['08_FI_05_evidence-interface_B'], 'VRES': ['U5c_VERBS_residue_and_governance_owner'],
    'RES-V': ['U5b_VERBS_military_physical_residue'], 'OBS': ['U5c_SC_one_obstacle_form'],
    'FRES': ['U5c_FI_residue'], 'DOE': ['U5a_DICE_owed_edits'],
    'FI-05B': ['08_FI_05_evidence-interface_B'],
    'VEN-E': ['15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds'],
    'COL-F': ['15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds'],
    'PAP-G': ['15_INSTITUTIONS_PAPACY_grounding_mechanisms'],
    'BYZ-G': ['15_INSTITUTIONS_BYZANTINE_grounding_mechanisms'],
    'SQD': ['04_MB_squad_grid_of_named_characters'], 'SQUAD': ['04_MB_squad_grid_of_named_characters'],
}

def _resolve_target(tgt):
    tgt = tgt.replace('`', '').strip()
    if tgt.startswith('…'):
        return pat_to_stems('*' + tgt.lstrip('…'))
    return pat_to_stems(tgt)

ALIAS_DEF = re.compile(r'((?:\*\*[^*]+\*\*\s*,?\s*)+|(?<![\w`*-])[A-Z0-9][A-Za-z0-9-]{0,9}(?![\w-]))\s*=\s*'
                       r'(?:the proposals\s*)?((?:`[^`]+`(?:\s*,\s*|\s+and\s+)?)+)')

def parse_alias_paragraph(para, out):
    """Update `out` with the `**X** = `file`` / `X = `file`` pairs of one paragraph."""
    flat = para.replace('\n', ' ')
    for m in ALIAS_DEF.finditer(flat):
        names = re.findall(r'\*\*([^*]+)\*\*', m.group(1)) or [m.group(1).strip()]
        targets = re.findall(r'`([^`]+)`', m.group(2))
        pairs = list(zip(names, targets)) if (len(names) > 1 and len(targets) == len(names)) \
            else [(names[-1], targets[0])]
        for name, tgt in pairs:
            if '/' in name:                                   # PES-FA-A/B/C
                base, tail = name.split('-')[:-1], name.split('-')[-1]
                base = '-'.join(base) + '-'
                for L in tail.split('/'):
                    out[base + L] = _resolve_target(re.sub(r'A…[A-Z]', L, tgt))
                continue
            rng = re.match(r'^(.*?)([A-Z]|\d\d)…([A-Z]|\d\d)$', name)
            if rng:                                           # PES-A…D, FI-01…08
                base, lo, hi = rng.groups()
                letters = ([chr(c) for c in range(ord(lo), ord(hi) + 1)] if lo.isalpha()
                           else ['%02d' % i for i in range(int(lo), int(hi) + 1)])
                for L in letters:
                    t = re.sub(r'A…[A-Z]', L, tgt).replace('0n', L)
                    if t == tgt and t.rstrip('`').replace('.md', '').endswith('_*'):
                        t = t.replace('.md', '')[:-1] + L + '_*'     # `14_VERBS_SOCIAL1_*` -> _A_*
                    if '*' not in t and '…' not in t:
                        t = t.replace('.md', '') + '_*'
                    out[base + L] = _resolve_target(t)
                continue
            out[name] = _resolve_target(tgt)
    return out

# ---------------------------------------------------------------- v12 index
PART_ALIAS_RX = re.compile(r'(?:\*\*|`)([A-Za-z0-9_.\-]{1,16})(?:\*\*|`)\s*(?:is|=|:)?\s*`(?:proposals/)?([0-9A-Za-z_\-]+?)(?:\.md)?`')

def part_aliases(txt):
    out = {}
    for m in PART_ALIAS_RX.finditer(txt):
        name, tgt = m.groups()
        if tgt in STEMSET and name != tgt:
            out.setdefault(name, [tgt])
    return out

def v12_index():
    items = {}      # handle -> dict(file, batch, title, src, body, al)
    group_alias = defaultdict(dict)       # a part and its `_cont` files share their short names
    for p in PARTS:
        group_alias[re.sub(r'_cont\d*', '', p)].update(part_aliases(open(p).read()))
    for p in PARTS:
        txt = open(p).read()
        pal = group_alias[re.sub(r'_cont\d*', '', p)]
        batch = None
        cur = None
        for ln in txt.split('\n'):
            mb = re.match(r'^## Batch (\S+)', ln)
            if mb:
                batch = mb.group(1)
            mh = re.match(r'^### (' + HANDLE + r')\b(.*)$', ln)
            if mh:
                h = mh.group(1)
                it = items.setdefault(h, dict(file=[], batch=batch, title='', src='', body='', al={}))
                it['file'].append(os.path.basename(p))
                it['al'].update(pal)
                it['title'] = mh.group(2)
                it['src'] += ' ' + mh.group(2)
                cur = it
                continue
            mp = re.match(r'^\| (' + HANDLE + r') \|([^|]*)\|([^|]*)\|([^|]*)\|', ln)
            if mp:
                h = mp.group(1)
                it = items.setdefault(h, dict(file=[], batch=batch, title=mp.group(2), src='', body='', al={}))
                it['al'].update(pal)
                if os.path.basename(p) not in it['file']:
                    it['file'].append(os.path.basename(p))
                it['src'] += ' ' + mp.group(3)
                it.setdefault('state', mp.group(4).strip())
                continue
            if ln.startswith('### ') or ln.startswith('## '):
                cur = None
                continue
            if cur is not None:
                if ln.startswith('- SOURCE:'):
                    cur['src'] += ' ' + ln
                cur['body'] += ln + '\n'
    return items

TRUNC = re.compile(r'(?<![\w/])((?:\d\d|U5[a-d])_[A-Za-z0-9_\-]+)')

def truncated(text):
    """`16_PESSIMIST_SE_A` (a stem cut short) -> the stems it begins, if at most three."""
    out = set()
    for tok in TRUNC.findall(text):
        tok = tok.rstrip('_')
        if tok in STEMSET:
            continue
        hits = [s for s in STEMS if s.startswith(tok + '_')]
        if 0 < len(hits) <= 3:
            out.update(hits)
    return out

def cited_stems(text, aliases):
    found = truncated(text)
    for s in STEMS:
        if s in text:
            found.add(s)
    for a, st in aliases.items():
        if st and re.search(r'(?<![\w-])' + re.escape(a) + r'(?![\w-])', text):
            found.update(st)
    for m in re.finditer(r'(?<![\w-])([A-Z][A-Z0-9]{0,4}(?:-[A-Z]{2})?)[_-]([A-G])(?![\w-])', text):
        found.update(family(m.group(1), m.group(2)))
    return found

def build_stem_map(items, aliases):
    by_stem = defaultdict(list)
    for h, it in items.items():
        al = dict(aliases); al.update(it.get('al', {}))
        it['stems'] = cited_stems(it['src'], al)
        for s in it['stems']:
            by_stem[s].append(h)
    return by_stem

# ---------------------------------------------------------------- closure rows
def closure_rows():
    rows = []
    for f in 'abcd':
        path = f'unified/U5_FINDINGS_CLOSURE_U5{f}.md'
        lines = open(path).read().split('\n')
        aliases = dict(GLOBAL)
        para, dcol = [], None
        for i, ln in enumerate(lines, 1):
            if ln.startswith('#'):                     # single-letter names live in their section only
                for k in [k for k in aliases if len(k) == 1]:
                    del aliases[k]
            if not ln.startswith('|'):
                if ln.strip():
                    para.append(ln)
                    continue
                if para and '= `' in ' '.join(para):
                    parse_alias_paragraph('\n'.join(para), aliases)
                para, dcol = [], None
                continue
            if para and '= `' in ' '.join(para):
                parse_alias_paragraph('\n'.join(para), aliases)
            para = []
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            if i < len(lines) and re.match(r'^\|[-| :]+\|$', lines[i].strip()):
                dcol = next((k for k, c in enumerate(cells) if c.lower().startswith('disposition')), None)
                continue
            if dcol is None or re.match(r'^[-| :]+$', ln.strip()) or len(cells) <= dcol:
                continue
            if 'RESOLVED-BY' in cells[dcol]:
                rows.append(dict(file=f'U5{f}', line=i, id=cells[0], claim=cells[1] if dcol > 1 else '',
                                 disp=cells[dcol], carrier=cells[dcol + 1] if len(cells) > dcol + 1 else '',
                                 aliases=dict(aliases)))
    return rows

SECT = re.compile(r'(?:edits?|Edits?|items?|Items?|steps?|Steps?|rows?|Parts?|§|Cut|commits?|PG-|R-19-|stage)\s*'
                  r'((?:[0-9A-Z][0-9a-z.]*(?:\s*(?:–|-|to|…)\s*[0-9A-Z][0-9a-z.]*)?(?:\s*(?:,|and)\s*)?)+)')

def sect_tokens(text):
    """'edits 1–3, 5' -> {1,2,3,5}; 'Part B' -> {B}; '§2.4' -> {2.4, 2}."""
    out = set()
    for grp in SECT.findall(text):
        for piece in re.split(r'\s*(?:,|and)\s*', grp.strip()):
            m = re.match(r'^([0-9A-Z][0-9a-z.]*)\s*(?:–|-|to|…)\s*([0-9A-Z][0-9a-z.]*)$', piece)
            if m:
                a, b = m.groups()
                if a.isdigit() and b.isdigit() and int(b) - int(a) < 40:
                    out.update(str(i) for i in range(int(a), int(b) + 1))
                elif len(a) == 1 and len(b) == 1 and a.isalpha():
                    out.update(chr(c) for c in range(ord(a), ord(b) + 1))
                else:
                    out.update((a, b))
            elif piece:
                out.add(piece)
                out.add(piece.split('.')[0])
    return out

def refine(stem_items, frag, items):
    toks = sect_tokens(frag)
    if not toks:
        return stem_items, None
    best = [h for h in stem_items if toks & sect_tokens(items[h]['src'])]
    return (best, True) if best else (stem_items, False)

PLAN_ID = re.compile(r'(?<![\w-])(CR-\d+[a-z]?|CP-T\d\d-\d\d|H-\d+|IN-\d+|G-\d+|DEF-\d+|NM-W\d+|REM-\d+|CL-[A-Z]+|ER-[A-Z0-9]+|ARC-\d+|B10-\d+|IS-[A-Z0-9-]+-\d\d|CI-\d\d|MBA-\d\d|PCR-\d)\b')

def stems_in(clause, al):
    st = set(x for x in STEMS if x in clause) | truncated(clause)
    for pre in re.findall(r'(\d\d_[A-Za-z0-9_]+?)…', clause):
        st.update(x for x in STEMS if x.startswith(pre))
    for a, ss in al.items():
        if not ss:
            continue
        if len(a) == 1:      # `A`, `B`, `C`: never in "Part B", "Edits A–B", "§A", "Cut A", "Option B"
            rx = r'(?<!Part )(?<!Parts )(?<!Edit )(?<!Edits )(?<!edit )(?<!edits )(?<!Cut )(?<!Option )(?<!row )(?<![\w`§-])' + a + r'(?![\w–…-])'
        else:
            rx = r'(?<![\w`-])' + re.escape(a) + r'(?![\w-])'
        if re.search(rx, clause):
            st.update(ss)
    for m in re.finditer(r'(?<![\w-])([A-Z][A-Z0-9]{0,4})[_-]([A-G])(?![\w-])', clause):
        st.update(family(m.group(1), m.group(2)))
    return st

def classify_closure(rows, items, by_stem, plan_index):
    out, by_id, prev = [], {}, set()
    POINTER = re.compile(r'^\s*(none owed|no edit owed|no edit|nothing owed|none of its own|accepted|restated by the audit|'
                         r'made in the audit|the mechanism rows below|each by the row above|corrected in the addendum|'
                         r'the audit\'s own restatements|none owed beyond)', re.I)
    for r in rows:
        car = r['carrier']
        al = r['aliases']
        handles, how = [], ''
        if r['file'] != getattr(classify_closure, '_f', None):
            by_id, prev = {}, set()
            classify_closure._f = r['file']
        if POINTER.search(car):
            out.append((r, 'POINTER-ONLY', [], 'pointer-text'))
            for i_ in re.split(r'[ ,]+', r['id']):
                by_id.setdefault(i_, [])
            continue
        for clause in re.split(r';', car):
            m = re.match(r'\s*as ((?:F|R|C|H|M)-[A-Z0-9-]+)', clause)
            if m and m.group(1) in by_id:
                handles.extend(by_id[m.group(1)][:2]); how = how or 'as-row'
                continue
            st = stems_in(clause, al)
            if not st and re.match(r'\s*(same|the same file|same file)\b', clause):
                st = set(prev); how = how or 'same-file'
            if not st and r['file'] == 'U5a' and re.match(r'\s*§[A-H](\s|$)', clause):
                st = {'U5a_CORE_owed_edits'}; how = how or 'U5a-owed-section'
            for s_ in st:
                cand = by_stem.get(s_, [])
                if not cand:
                    continue
                best, refined = refine(cand, clause, items)
                handles.extend(best[:4] if refined else best[:1])
                how = how or {True: 'stem+section', None: 'stem', False: 'stem(section-unmatched)'}[refined]
            if st:
                prev = st
            for pid in PLAN_ID.findall(clause):
                for h in plan_index.get(pid, [])[:2]:
                    handles.append(h)
                    how = how or 'plan-id'
        if not handles:      # "U1 architecture §n": the U1 sections v12 cites as `U1 §n`
            for n in re.findall(r'U1 architecture §(\d+[a-z]?)', car):
                handles.extend(u1_index(items).get(n, [])[:2]); how = how or 'U1-section'
        if not handles:      # "F-CORE-02's and F-CORE-15's carriers": the named rows' items
            for fid in re.findall(r'((?:F|R|H|C|D)-[A-Z0-9-]*\d+)\'s', car) + re.findall(r'\bas (D-\d+)', car):
                handles.extend(by_id.get(fid, [])[:2]); how = how or 'as-row'
        if not handles and re.search(r'their workplan positions|^the plan\b', car):
            for pid in PLAN_ID.findall(r['id']):
                handles.extend(plan_index.get(pid, [])[:1]); how = how or 'plan-id(id cell)'
        handles = list(dict.fromkeys(handles))
        for i_ in re.split(r'[ ,]+', r['id']):
            by_id.setdefault(i_, handles)
        out.append((r, 'COVERED' if handles else 'UNRESOLVED', handles, how))
    return out

_U1 = {}
def u1_index(items):
    if not _U1:
        for h, it in items.items():
            for m in re.finditer(r'U1(?: architecture)? §(\d+[a-z]?)', it['src']):
                _U1.setdefault(m.group(1), []).append(h)
    return _U1

def plan_id_index(items):
    idx = defaultdict(list)
    for h, it in items.items():
        for pid in set(PLAN_ID.findall(it['src'])):
            idx[pid].append(h)
    return idx

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'closure'
    items = v12_index()
    glob_alias = dict(GLOBAL)
    by_stem = build_stem_map(items, glob_alias)
    if mode == 'index':
        print(len(items), 'items;', len(by_stem), 'stems cited;',
              'uncited stems:', sorted(set(STEMS) - set(by_stem)))
    elif mode == 'closure':
        rows = closure_rows()
        pidx = plan_id_index(items)
        res = classify_closure(rows, items, by_stem, pidx)
        for r, cls, hs, how in res:
            print('\t'.join([f"{r['file']}:{r['line']}", r['id'][:40], cls, ','.join(hs[:6]), how,
                             r['carrier'][:200]]))

def show(stem_or_alias, items, by_stem, n=400):
    """print every v12 item that cites a stem (hand check)."""
    st = [stem_or_alias] if stem_or_alias in STEMSET else GLOBAL.get(stem_or_alias, []) or \
        [s for s in STEMS if s.startswith(stem_or_alias)]
    for s in st:
        print('##', s)
        for h in by_stem.get(s, []):
            it = items[h]
            print('  ', h, it.get('state', ''), '|', it['src'][:n].replace('\n', ' '))

if __name__ == '__main__' and sys.argv[1:2] == ['show']:
    items = v12_index(); by_stem = build_stem_map(items, dict(GLOBAL))
    for a in sys.argv[2:]:
        show(a, items, by_stem)

if __name__ == '__main__' and sys.argv[1:2] == ['find']:
    # find <regex> ...: the items whose heading, SOURCE or body matches every regex
    items = v12_index()
    for h, it in items.items():
        txt = it['src'] + '\n' + it['body']
        if all(re.search(a, txt) for a in sys.argv[2:]):
            print(h, it.get('state', ''), it['file'][0], '|', it['title'][:150])

# ---------------------------------------------------------------- intake
def intake_entries():
    """Every `- **ids** · ...` line of V12_INTAKE.md §5, with its heading and line number."""
    out, lane, head = [], None, None
    lines = open('master/eval/V12_INTAKE.md').read().split('\n')
    for i, ln in enumerate(lines, 1):
        if i < 71:
            continue
        if ln.startswith('### Lane'):
            lane = ln.split()[2]
        elif re.match(r'^\*\*[^*]+\*\*\s*$', ln):
            head = ln.strip('*').strip()
        elif ln.startswith('- **'):
            name = re.match(r'^- \*\*([^*]+)\*\*', ln).group(1)
            ids = [p.strip() for p in re.split(r',\s*', name) if p.strip()]
            out.append(dict(line=i, lane=lane, head=head, name=name, ids=ids, text=ln))
    return out

def id_regex(i):
    core = re.sub(r'\s*\(.*$', '', i).strip()          # 'NM-W9 (b)' -> 'NM-W9'
    return core, r'(?<![\w-])' + re.escape(core) + r'(?![\w])'

if __name__ == '__main__' and sys.argv[1:2] == ['intake']:
    items = v12_index()
    head = open('master/workplan_v12/workplan_v12.md').read()
    allv12 = '\n'.join(open(p).read() for p in PARTS)
    for e in intake_entries():
        held = 'held' in (e['head'] or '').lower()
        headrule = 'head rules' in (e['head'] or '')
        cite = r'intake[^\n]{0,30}?`:%d`|`V12_INTAKE\.md:%d`|intake `?:%d\b' % (e['line'], e['line'], e['line'])
        for i in e['ids']:
            core, rx = id_regex(i)
            hs = [h for h, it in items.items() if re.search(rx, it['src']) or re.search(cite, it['src'])]
            hb = [h for h, it in items.items() if h not in hs and (re.search(rx, it['body']) or re.search(cite, it['body']))]
            inhead = bool(re.search(rx, head))
            anyv12 = bool(re.search(rx, allv12)) or bool(re.search(cite, allv12))
            cls = ('HEAD-RULE' if headrule else 'HELD-TABLE' if held else
                   'COVERED' if hs else 'MENTIONED' if (hb or anyv12) else 'ABSENT')
            print('\t'.join([str(e['line']), e['lane'] or '', (e['head'] or '')[:30], i, cls,
                             ','.join(hs[:5]), ','.join(hb[:4]), 'head' if inhead else '']))

# ---------------------------------------------------------------- instruction suite and codebase items
def suite_ids():
    ids = set()
    for p in glob.glob('master/instructions/IS_*.md'):
        for m in re.finditer(r'^(?:#+|\*\*|\| )[^|]{0,6}`?(IS-[A-Z0-9]+(?:-[A-Z]+)?-[A-Z0-9]+)', open(p).read(), re.M):
            ids.add(m.group(1))
    ids.discard('IS-B2-01')        # a stray citation, not an item heading (checked by hand)
    ids |= {'CI-%02d' % i for i in range(1, 12)} | {'MBA-%02d' % i for i in range(1, 10)} | {'PCR-%d' % i for i in range(1, 5)}
    return sorted(ids)

if __name__ == '__main__' and sys.argv[1:2] == ['suite']:
    items = v12_index()
    allv12 = '\n'.join(open(p).read() for p in PARTS + ['master/workplan_v12/workplan_v12.md'])
    for i in suite_ids():
        rx = r'(?<![\w-])' + re.escape(i) + r'(?![\w])'
        hs = [h for h, it in items.items() if re.search(rx, it['src'])]
        hb = [h for h, it in items.items() if h not in hs and re.search(rx, it['body'])]
        st = [items[h].get('state', '') or items[h]['title'].split('·')[-2].strip() for h in hs[:3]]
        print('\t'.join([i, 'COVERED' if hs else 'MENTIONED' if (hb or re.search(rx, allv12)) else 'ABSENT',
                         ','.join(hs[:6]), '; '.join(s[:30] for s in st), ','.join(hb[:3])]))

# ---------------------------------------------------------------- severity of the unrated F- rows
def grade_of(fid):
    """The audit's own grade for a finding id, read off its defining line; None if the audit states none."""
    base = re.match(r'(F-[A-Z0-9]+(?:-[A-Z]+)?-\d+)', fid)
    if not base:
        return None, None
    fid = base.group(1)
    rx = re.compile(r'^(?:#+ |\| |\*\*|- \*\*)\**' + re.escape(fid) + r'\b\**(.*)$')
    for p in sorted(glob.glob('audits/*.md')):
        lines = open(p).read().split('\n')
        for n, ln in enumerate(lines, 1):
            m = rx.match(ln)
            if not m:
                continue
            rest = m.group(1)
            cat = rest.split('|')[1] if ln.startswith('| ') else ' · '.join(rest.split(' · ')[:2])
            if ln.startswith('| ') and not re.search(r'block|degrad|hygiene', cat, re.I):
                # a table whose grade is stated once above it ("each a finding of the same kind (degrades ...)")
                k = n - 1
                while k > 0 and lines[k - 1].startswith('|'):
                    k -= 1
                above = ' '.join(lines[max(0, k - 3):k])
                g = re.search(r'\((degrades[^)]*|blocks[^)]*|hygiene[^)]*)\)\s*:?\s*$', above.strip())
                if g:
                    cat, n = g.group(1), k
            low = cat.lower()
            g = ''.join(c for c, w in (('B', 'block'), ('D', 'degrad'), ('H', 'hygiene')) if w in low)
            return (g or None), '%s:%d · %s' % (os.path.basename(p), n, cat.strip(' ·*|')[:90])
    return None, None

if __name__ == '__main__' and sys.argv[1:2] == ['grades']:
    for ln in open(sys.argv[2]):
        loc, fid = ln.split('\t')[:2]
        for one in re.findall(r'F-[A-Z0-9]+(?:-[A-Z]+)?-\d+', fid):
            g, where = grade_of(one)
            print('\t'.join([loc, fid[:40], one, g or 'unrated in source', where or 'no defining line in audits/']))

# ---------------------------------------------------------------- rows resolved by hand (each opened; see COVERAGE.md §A.2)
HAND = {
 'U5a:140': ('HELD-TABLE', [], 'claim_fade Edit 5 (lift MAX_SEASONS) needs an eight-season flat reading; B09 does not carry it (part 11_cont, B09 UNDECIDED (1)); A-114 holds runs past two seasons to B99; H2_DECISIONS HD-26: B98 lists it BLOCKED (A-114), B99 reads it'),
 'U5a:151': ('POINTER-ONLY', [], 'points at the rows above; the UNCLEAR rows close nothing'),
 'U5a:215': ('COVERED', ['B34.16'], 'CORE-SC Edit 5 (resolution 20)'),
 'U5a:284': ('COVERED', ['B05.02'], 'test_fractional_pool.py deleted with its subject (DOE §1; F-DICE-22)'),
 'U5a:309': ('POINTER-ONLY', [], 'as F-PES-CORE-01..07, each COVERED (B09.02, B09.10, B09.11, B02.13, B02.14, B08.02, B03.16)'),
 'U5a:395': ('POINTER-ONLY', [], 'each by the finding it restates (F-CHAR-04, -02, -09, -01; F-CORE-05), each COVERED'),
 'U5a:422': ('POINTER-ONLY', [], 'closed at U5a §2.7'),
 'U5a:441': ('POINTER-ONLY', [], 'RESOLVED-BY no edit (decided in the audit)'),
 'U5a:475': ('POINTER-ONLY', [], 'RESOLVED-BY no edit (decided in the audit)'),
 'U5a:477': ('POINTER-ONLY', [], '= F-CHAR-03, F-CHAR-17, F-CHAR-18 and the reason trail, each COVERED'),
 'U5a:491': ('COVERED', ['B10.30', 'B09.13'], 'goal lean (02_CHAR_goal_lean_on_its_own_question); reason trail (02_CHAR_reason_trail_and_small_edits Part A)'),
 'U5a:500': ('POINTER-ONLY', [], 'RESOLVED-BY no edit (decided in the audit)'),
 'U5a:569': ('POINTER-ONLY', [], 'RESOLVED-BY no edit'),
 'U5a:607': ('COVERED', ['B05.60'], 'ADV "The resolution" (Edits A-D)'),
 'U5a:620': ('POINTER-ONLY', [], 'ADV Edit E is "Not built; the door each waits at" (the proposal\'s own text)'),
 'U5a:621': ('COVERED', ['B05.60'], 'SCN-05: resolution 19 (ADV); SCN-02 named for SC (ED-SC-0038); ARC-23 SUPERSEDED by A-11'),
 'U5a:637': ('COVERED', ['B09.04'], 'DOE §4'),
 'U5a:661': ('POINTER-ONLY', [], 'corrected in place in SC and FI files; U5c rows close the design'),
 'U5a:662': ('COVERED', ['B15.10'], 'EXITS Part B superseded by 16_PESSIMIST_PC_A (U3 §4.1 row 55), which B15.10 lands'),
 'U5a:663': ('COVERED', ['B12c.06', 'B07.01'], 'EXITS Part C defers to MAT_A §6 (tend drawn, B12c.06) over 18-A\'s route (B07.01)'),
 'U5a:665': ('POINTER-ONLY', [], 'FA files as corrected (U5d rows); A-19, A-14'),
 'U5a:777': ('COVERED', ['B10.15'], 'CHAR_A item 4: the emitter with the Event'),
 'U5a:840': ('COVERED', ['B08.06', 'B03.16'], 'no_stored_plan is B03.16; TDA §G (H-172, "lands in B08 with SEQ") was in no item: added by this lane as B08.06 (Covered: C-01)'),
 'U5b:70':  ('COVERED', ['B15.10', 'B14.27'], 'EXITS Part B superseded by PC_A (B15.10); PHY_A A3 in B15'),
 'U5b:106': ('COVERED', ['B01.01'], 'P1 lands whole as lane A\'s e5d6ab9'),
 'U5b:128': ('COVERED', ['B12c.06', 'B07.01'], 'EXITS Part C: tend drawn (MAT_A §6)'),
 'U5b:154': ('COVERED', ['B12c.06'], 'EXITS Part C: tend drawn (MAT_A §6)'),
 'U5b:190': ('CONTENT-OWED', ['B14.12'], 'PX item 6 is "not built here": a pike is content (the stated matchup rows of A-113, B19a/B19/B31); B14.12 lands the export'),
 'U5b:259': ('COVERED', ['B15.10'], 'PHY_A A3 adopted with PC_A in B15'),
 'U5b:325': ('SUPERSEDED', [], 'RES-MB §7 edits v11 plan cards, deleted on adoption (B17 UNDECIDED (3)); CR-52 and CP-T04-04 are intake ids (§B)'),
 'U5b:437': ('COVERED', ['B19.02', 'B19.05', 'B19.55', 'B19.70'], '27-MB (A-59): 27_MB_A, the commander\'s record; 27A-6 added by this lane as B19.70 (C-02)'),
 'U5b:524': ('COVERED', ['B29.01', 'B22.29', 'B22.30', 'B23.10'], 'the world_q licence readers (warrants_for, field_defender, may_ruin)'),
 'U5b:559': ('COVERED', ['B12c.06'], 'EXITS Part C: tend drawn (MAT_A §6)'),
 'U5b:560': ('POINTER-ONLY', [], 'each case by the verb\'s own proposal; NPC-088 by A-16\'s carrier'),
 'U5b:223': ('COVERED', ['B14.17', 'B14.18', 'B15.15'], 'RES-PC §1: items 1-2 in B14; the slope bound and the fit (item 3) added by this lane as B15.15 (C-03)'),
 'U5b:208': ('COVERED', ['B18.02', 'B14.17', 'B14.18', 'B15.15'], 'P4 Part A (B18.02, with RES-PC §1 item 4); RES-PC §1 items 1-3 (B14.17, B14.18, B15.15)'),
 'U5c:380': ('COVERED', ['B36.07'], 'VERD R-19-09 (edit 6, the harness) is B36.07'),
 'U5c:285': ('CONTENT-OWED', ['B04.03'], 'two data rows on the skill surface; the verb rows\' skill values land with B04.03 (CORE Edit 8)'),
 'U5c:306': ('POINTER-ONLY', [], 'R-49 dropped as a referent'),
 'U5c:348': ('COVERED', ['B26.06'], 'PFI-D edits 1, 3 (the three product-less rows)'),
 'U5c:433': ('POINTER-ONLY', [], 'the rows above, each with its prize'),
 'U5c:490': ('COVERED', ['B12c.06'], 'MAT_A §6 owns the tend row'),
 'U5d:170': ('POINTER-ONLY', [], 'WAR-B edit 7 (a) answered no (an outcome Query)'),
 'U5d:350': ('POINTER-ONLY', [], 'as F-WR-07 (none of its own)'),
 'U5d:543': ('POINTER-ONLY', [], 'the audit\'s table; A-47 and A-15 carried by STAGED and HAPP-A items'),
 'U5d:568': ('COVERED', ['B07.01', 'B15.09', 'B11.65', 'B08.05'], 'the four 18_DETERMINISM carriers'),
 'U5d:708': ('POINTER-ONLY', [], 'U5d Part 2 (each row there carries its own item)'),
 'U5d:711': ('POINTER-ONLY', [], 'U5d Part 7'),
 'U5d:712': ('POINTER-ONLY', [], 'U5d Part 3'),
 'U5d:773': ('POINTER-ONLY', [], 'answered in the audit\'s table ("Not yours")'),
 'U5d:784': ('POINTER-ONLY', [], 'closed by the synthesis: no `purchase` form'),
 'U5d:789': ('POINTER-ONLY', [], 'as the PAPACY rows above; R-11 SUPERSEDED by A-17'),
 'U5d:792': ('COVERED', ['B32.19'], 'per-row patronage (PAP_B)'),
 'U5d:798': ('POINTER-ONLY', [], 'closed by the synthesis: no bar'),
 'U5d:817': ('POINTER-ONLY', [], 'the families\' Reconciled lines; the items carry the reconciled text'),
}

def final_closure():
    items = v12_index()
    by_stem = build_stem_map(items, dict(GLOBAL))
    res = classify_closure(closure_rows(), items, by_stem, plan_id_index(items))
    out = []
    for r, cls, hs, how in res:
        key = '%s:%d' % (r['file'], r['line'])
        if key in HAND:
            cls, hs, note = HAND[key]
            how = 'hand: ' + note
        out.append((key, r, cls, hs, how))
    return out, items

if __name__ == '__main__' and sys.argv[1:2] == ['final']:
    out, items = final_closure()
    for key, r, cls, hs, how in out:
        print('\t'.join([key, r['id'][:40], cls, ','.join(hs[:6]), how[:160]]))

# ---------------------------------------------------------------- second check: each proposal's own "Lands in batch:" line
def lands_lines():
    out = {}
    for s in STEMS:
        txt = open('proposals/%s.md' % s).read()
        m = re.search(r'\*\*Lands in batch:\*\*\s*(.*)', txt)
        if m:
            out[s] = m.group(1)
    return out

if __name__ == '__main__' and sys.argv[1:2] == ['lands']:
    items = v12_index(); by_stem = build_stem_map(items, dict(GLOBAL))
    for s, line in lands_lines().items():
        own = re.split(r'\*\*(?:Depends on|Serial edge|Read by|Handed)', line)[0]
        own = re.sub(r'~~.*?~~', '', own)                      # struck text
        named = set(re.findall(r'\bB\d\d[a-z]?(?:F\d)?\b|\bBA1\b', own))
        have = set(h.split('.')[0] for h in by_stem.get(s, []))
        have_short = set(re.sub(r'-.*', '', b) for b in have)
        miss = sorted(b for b in named if b not in have_short and not re.search(r'none|SUPERSEDED|superseded', line[:60]))
        if miss:
            print('\t'.join([s, ','.join(miss), ','.join(sorted(have_short)), line[:220]]))
```

## Appendix B — the 132 RESOLVED-BY rows the master-findings lane printed with no batch, each resolved

Generated by Appendix A (`final`), joined on the closure row `U5x:line` with the rows of `master/MASTER_FINDINGS_part3.md`..`_part6.md` whose disposition is RESOLVED-BY and whose batch cell read `—`. "hand" in the last column: the row was opened and resolved by this lane (Appendix C gives the ground).

| closure row | MF row | id | class | carried by | how |
|---|---|---|---|---|---|
| `U5a:84` | `part3.md:183` | H-10 | COVERED | B03.86 | plan-id |
| `U5a:93` | `part3.md:188` | H-145, H-220 | COVERED | B03.51, B03.52 | as-row |
| `U5a:95` | `part3.md:189` | IN-14, CR-98, CR-99, NM-W9 | COVERED | B03.86, B11F2.05, B11F2.06, B09.09 | plan-id(id cell) |
| `U5a:104` | `part3.md:191` | 3 | COVERED | B39.13, B39.14 | same-file |
| `U5a:105` | `part3.md:192` | 4 | COVERED | B39.11 | same-file |
| `U5a:136` | `part3.md:194` | all 143 · each `season_requires` need is checked b | COVERED | B39.11 | same-file |
| `U5a:142` | `part3.md:198` | 26 cases · `needs_deadline` | COVERED | B39.11 | same-file |
| `U5a:143` | `part3.md:199` | 91 cases · `ends_when` | COVERED | B39.11 | same-file |
| `U5a:151` | `part3.md:202` | needs wrongly stated: prose spans; `UNCLEAR:` rows | POINTER-ONLY | — | hand: points at the rows above; the UNCLEAR rows close nothing |
| `U5a:180` | `part3.md:203` | C6 | COVERED | B03.69, B03.51 | as-row |
| `U5a:197` | `part3.md:207` | §4.4 typed outcome on two of four providers | COVERED | B17.03, B14.01 | as-row |
| `U5a:205` | `part3.md:208` | §5 (d) five of eleven contested rolls name no capa | COVERED | B04.03, B04.19 | same-file |
| `U5a:208` | `part3.md:210` | §5 (d) traits, talents, flaws have no carrier | COVERED | B04.15, B04.18 | U1-section |
| `U5a:215` | `part3.md:215` | §7.1 the slate (design) against the per-person que | COVERED | B34.16 | hand: CORE-SC Edit 5 (resolution 20) |
| `U5a:224` | `part3.md:219` | §7.2 "the masters exist, the code does not read th | COVERED | B04.06, B04.08 | U1-section |
| `U5a:225` | `part3.md:220` | §7.2 near-identical instances (returning finding) | COVERED | B39.11, B39.13, B04.02 | as-row |
| `U5a:226` | `part3.md:221` | §7.2 J-1, J-5 (a playable season; choice surfaces) | COVERED | B34.19, B10.57, B24.03 | as-row |
| `U5a:227` | `part3.md:222` | §7.2 J-7 emergence made visible | COVERED | B10.05, B09.13, B09.01 | as-row |
| `U5a:243` | `part3.md:225` | 16 | COVERED | B04.14 | same-file |
| `U5a:249` | `part3.md:227` | 22 | COVERED | B34.19 | U5a-owed-section |
| `U5a:284` | `part3.md:228` | §4 `[not adjudicated]` `tests/valoria/test_fractio | COVERED | B05.02 | hand: test_fractional_pool.py deleted with its subject (DOE §1; F-DICE-22) |
| `U5a:303` | `part3.md:231` | F-PES-CORE-05 | COVERED | B02.14, B02.15 | same-file |
| `U5a:309` | `part3.md:232` | res. 1–6 | POINTER-ONLY | — | hand: as F-PES-CORE-01..07, each COVERED (B09.02, B09.10, B09.11, B02.13, B02.14, B08.02, B03.16) |
| `U5a:395` | `part3.md:375` | §5 NERS cuts (scar count; the realm-wide draw; `te | POINTER-ONLY | — | hand: each by the finding it restates (F-CHAR-04, -02, -09, -01; F-CORE-05), each COVERED |
| `U5a:417` | `part3.md:381` | H-330 | COVERED | B03.86 | plan-id |
| `U5a:420` | `part3.md:382` | H-347 | COVERED | B10.17 | stem |
| `U5a:422` | `part3.md:383` | the 38 rows read at the dossier excerpt only | POINTER-ONLY | — | hand: closed at U5a §2.7 |
| `U5a:423` | `part3.md:384` | CR-88, CR-89–91, CR-93, CR-92, CL-PERSON, CL-ATTR | COVERED | B10.30, B21b.13, B10.01, B24.41, B10.53 | plan-id(id cell) |
| `U5a:437` | `part3.md:385` | 17 | COVERED | B03.86 | plan-id |
| `U5a:439` | `part3.md:386` | 19–25 | COVERED | B03.52, B09.15 | same-file |
| `U5a:441` | `part3.md:387` | 27, 28, 30 | POINTER-ONLY | — | hand: RESOLVED-BY no edit (decided in the audit) |
| `U5a:444` | `part3.md:388` | §8 step 12 | COVERED | B21b.03, B27.18 | plan-id |
| `U5a:475` | `part3.md:308` | F-CHAR-22 | POINTER-ONLY | — | hand: RESOLVED-BY no edit (decided in the audit) |
| `U5a:477` | `part3.md:391` | B2.2 returning findings (six rows) | POINTER-ONLY | — | hand: = F-CHAR-03, F-CHAR-17, F-CHAR-18 and the reason trail, each COVERED |
| `U5a:491` | `part3.md:393` | H-233, H-343 | COVERED | B10.30, B09.13 | hand: goal lean (02_CHAR_goal_lean_on_its_own_question); reason trail (02_CHAR_reason_trail_and_small_edits Part A) |
| `U5a:492` | `part3.md:394` | H-273, H-282 | COVERED | B10.17 | stem |
| `U5a:500` | `part3.md:397` | rows 15, 16, 23 | POINTER-ONLY | — | hand: RESOLVED-BY no edit (decided in the audit) |
| `U5a:503` | `part3.md:398` | row 21 (the file for the capability definition: re | COVERED | B04.03, B04.04 | U1-section |
| `U5a:552` | `part5.md:490` | F-DICE-04 | COVERED | B04.03, B04.19 | U1-section |
| `U5a:569` | `part5.md:530` | C-2 | POINTER-ONLY | — | hand: RESOLVED-BY no edit |
| `U5a:595` | `part5.md:535` | H-312 | COVERED | B04.03, B04.19 | U1-section |
| `U5a:607` | `part5.md:539` | res. 19 (SCN-05 restated: a spend buys named level | COVERED | B05.60 | hand: ADV "The resolution" (Edits A-D) |
| `U5a:615` | `part5.md:543` | §13 ARC-22, NSC-04, NSC-07, SCN-01, ARC-10 (four g | COVERED | B04.24, B05.05 | U1-section |
| `U5a:621` | `part5.md:546` | §13 SCN-05, SCN-02, ARC-23 | COVERED | B05.60 | hand: SCN-05: resolution 19 (ADV); SCN-02 named for SC (ED-SC-0038); ARC-23 SUPERSEDED by A-11 |
| `U5a:623` | `part5.md:548` | §13 NPC-001, NPC-004, NPC-075, ARC-22 (competence  | COVERED | B04.09, BA1.01 | U1-section |
| `U5a:661` | `part6.md:312` | D-01, D-02, D-03 | POINTER-ONLY | — | hand: corrected in place in SC and FI files; U5c rows close the design |
| `U5a:663` | `part6.md:313` | D-05 | COVERED | B12c.06, B07.01 | hand: EXITS Part C defers to MAT_A §6 (tend drawn, B12c.06) over 18-A's route (B07.01) |
| `U5a:665` | `part6.md:314` | D-07, D-08, D-09 | POINTER-ONLY | — | hand: FA files as corrected (U5d rows); A-19, A-14 |
| `U5a:666` | `part6.md:315` | D-10 | COVERED | B07.01 | stem |
| `U5a:667` | `part6.md:316` | D-11 | COVERED | B15.09 | stem |
| `U5a:674` | `part6.md:317` | C-02 | COVERED | B11.65 | stem |
| `U5a:675` | `part6.md:318` | C-03, C-05, C-08, C-09, C-10, C-15 | COVERED | B07.01 | stem |
| `U5a:676` | `part6.md:319` | C-04 | COVERED | B07.01 | as-row |
| `U5a:679` | `part6.md:321` | C-11 | COVERED | B08.05 | stem |
| `U5a:681` | `part6.md:323` | C-13 | COVERED | B15.09 | stem |
| `U5a:690` | `part6.md:327` | every verb's band map lands on the route C-01 make | COVERED | B07.01 | stem |
| `U5a:723` | `part6.md:573` | §6 item 1 | COVERED | B03.65 | as-row |
| `U5a:746` | `part6.md:575` | X-1, X-2, X-3, X-4 | POINTER-ONLY | — | pointer-text |
| `U5a:747` | `part6.md:576` | X-4b, X-5 | POINTER-ONLY | — | pointer-text |
| `U5a:770` | `part6.md:581` | C6 16 code-less contract rows; 19 dead path string | POINTER-ONLY | — | pointer-text |
| `U5a:783` | `part6.md:586` | §5a `envelope.changed`; X-R3 | POINTER-ONLY | — | pointer-text |
| `U5a:790` | `part6.md:588` | §8 `witness_channel_predicates`; `venues.yaml` row | POINTER-ONLY | — | pointer-text |
| `U5a:834` | `part3.md:234` | F-TEST-07, harness probe loops (DG4) | POINTER-ONLY | — | pointer-text |
| `U5a:861` | `part3.md:244` | harness tests guard process artifacts (DG4) | POINTER-ONLY | — | pointer-text |
| `U5a:885` | `part3.md:254` | "not asserted in a played realm" notes (about twen | COVERED | B02.21, B02.22 | as-row |
| `U5a:890` | `part3.md:259` | `test_descriptors_runtime.py`: nothing catches a r | POINTER-ONLY | — | pointer-text |
| `U5b:89` | `part4.md:168` | §5 "no matchup is ever certain" | COVERED | B15.09 | stem |
| `U5b:196` | `part4.md:184` | §B4 row 3 | COVERED | B15.09 | stem |
| `U5b:437` | `part4.md:224` | U5a F-DICE-18 (C-7) | COVERED | B19.02, B19.05, B19.55, B19.70 | hand: 27-MB (A-59): 27_MB_A, the commander's record; 27A-6 added by this lane as B19.70 (C-02) |
| `U5b:524` | `part6.md:185` | §0.5 the family's one repair | COVERED | B29.01, B22.29, B22.30, B23.10 | hand: the world_q licence readers (warrants_for, field_defender, may_ruin) |
| `U5b:560` | `part6.md:191` | cases (item 8 of each section) | POINTER-ONLY | — | hand: each case by the verb's own proposal; NPC-088 by A-16's carrier |
| `U5c:110` | `part4.md:519` | §13 wrongly stated needs | POINTER-ONLY | — | pointer-text |
| `U5c:162` | `part4.md:520` | §B4.7 | COVERED | B27.02 | plan-id |
| `U5c:285` | `part5.md:120` | R-31 | CONTENT-OWED | B04.03 | hand: two data rows on the skill surface; the verb rows' skill values land with B04.03 (CORE Edit 8) |
| `U5c:306` | `part5.md:122` | C-7 | POINTER-ONLY | — | hand: R-49 dropped as a referent |
| `U5c:309` | `part5.md:123` | C-10 | POINTER-ONLY | — | pointer-text |
| `U5c:332` | `part5.md:124` | R-45 | POINTER-ONLY | — | pointer-text |
| `U5c:336` | `part5.md:125` | R-49 | POINTER-ONLY | — | pointer-text |
| `U5c:348` | `part5.md:126` | F-PES-FI-05 | COVERED | B26.06 | hand: PFI-D edits 1, 3 (the three product-less rows) |
| `U5c:373` | `part6.md:360` | C-6 / R-19-12 | POINTER-ONLY | — | pointer-text |
| `U5c:374` | `part6.md:361` | C-7 | POINTER-ONLY | — | pointer-text |
| `U5c:433` | `part6.md:192` | §0.6 | POINTER-ONLY | — | hand: the rows above, each with its prize |
| `U5c:500` | `part6.md:195` | named (2) | POINTER-ONLY | — | pointer-text |
| `U5d:78` | `part5.md:244` | H-133 | POINTER-ONLY | — | pointer-text |
| `U5d:96` | `part5.md:246` | FA-03, FA-07 | POINTER-ONLY | — | pointer-text |
| `U5d:149` | `part5.md:252` | C-1 | POINTER-ONLY | — | pointer-text |
| `U5d:152` | `part5.md:253` | C-4, C-5, C-8 | POINTER-ONLY | — | pointer-text |
| `U5d:168` | `part5.md:254` | R-30 | POINTER-ONLY | — | pointer-text |
| `U5d:171` | `part5.md:255` | R-33, R-34 | POINTER-ONLY | — | pointer-text |
| `U5d:174` | `part5.md:257` | §B8.2 (old findings re-verified; what transfers) | POINTER-ONLY | — | pointer-text |
| `U5d:190` | `part5.md:258` | F-PES-FA-11 | COVERED | B21.03, B21.16 | as-row |
| `U5d:191` | `part5.md:168` | F-PES-FA-12 | POINTER-ONLY | — | pointer-text |
| `U5d:227` | `part5.md:311` | F-SE-16 | POINTER-ONLY | — | pointer-text |
| `U5d:258` | `part5.md:355` | §13 NPC-083 (methods), ARC-44/ARC-01 (drift with n | POINTER-ONLY | — | pointer-text |
| `U5d:277` | `part5.md:357` | §2.3 (twelve `.audit/` findings re-verified) | POINTER-ONLY | — | pointer-text |
| `U5d:336` | `part5.md:388` | F-WR-07 | POINTER-ONLY | — | pointer-text |
| `U5d:348` | `part5.md:446` | H-238 | POINTER-ONLY | — | pointer-text |
| `U5d:350` | `part5.md:447` | H-274 | POINTER-ONLY | — | hand: as F-WR-07 (none of its own) |
| `U5d:356` | `part5.md:448` | R-10, R-17, R-19 | POINTER-ONLY | — | pointer-text |
| `U5d:394` | `part5.md:454` | R-24, R-33, R-35 | POINTER-ONLY | — | pointer-text |
| `U5d:398` | `part5.md:455` | R-36 | POINTER-ONLY | — | pointer-text |
| `U5d:416` | `part5.md:389` | F-PES-WR-08 | POINTER-ONLY | — | pointer-text |
| `U5d:421` | `part5.md:457` | §5, §6, §7 lists | POINTER-ONLY | — | pointer-text |
| `U5d:457` | `part5.md:618` | GO-06 | POINTER-ONLY | — | pointer-text |
| `U5d:466` | `part5.md:621` | R21, R36–R43, R47 | POINTER-ONLY | — | pointer-text |
| `U5d:472` | `part5.md:623` | §13 ARC-14, ARC-17 ("a single threshold stat", "a  | POINTER-ONLY | — | pointer-text |
| `U5d:508` | `part5.md:625` | F-PES-GO-11 | POINTER-ONLY | — | pointer-text |
| `U5d:525` | `part6.md:279` | §3 (the per-case table, 143 cases) | POINTER-ONLY | — | pointer-text |
| `U5d:542` | `part6.md:282` | §5 (staged sequence, stages 0–8) | POINTER-ONLY | — | pointer-text |
| `U5d:543` | `part6.md:283` | §5 scripting-drift table (ARC-14, -17, -11, NPC-01 | POINTER-ONLY | — | hand: the audit's table; A-47 and A-15 carried by STAGED and HAPP-A items |
| `U5d:545` | `part6.md:284` | §6 rows 2, 3, 4, 5, 10, 11, 13, 14, 15, 19, 20 | POINTER-ONLY | — | pointer-text |
| `U5d:548` | `part6.md:285` | §6 row 12 | COVERED | B33.09 | as-row |
| `U5d:568` | `part6.md:21` | F-PES-GAME-04 | COVERED | B07.01, B15.09, B11.65, B08.05 | hand: the four 18_DETERMINISM carriers |
| `U5d:586` | `part6.md:40` | §7.2 (the first ring; the game gate) | POINTER-ONLY | — | pointer-text |
| `U5d:612` | `part6.md:393` | R-N3 | POINTER-ONLY | — | pointer-text |
| `U5d:623` | `part6.md:395` | CR-76 to CR-80, CR-88, CR-91, CR-97, CR-100 to CR- | COVERED | B39.15, B10.30, B21b.13, B11F2.01, B11F2.07 | plan-id(id cell) |
| `U5d:685` | `part6.md:456` | §1 (the King's death, re-run and explained) | COVERED | B02.17, B12a.01 | plan-id |
| `U5d:708` | `part6.md:496` | M9 | POINTER-ONLY | — | hand: U5d Part 2 (each row there carries its own item) |
| `U5d:711` | `part6.md:497` | M16 | POINTER-ONLY | — | hand: U5d Part 7 |
| `U5d:712` | `part6.md:498` | M17 | POINTER-ONLY | — | hand: U5d Part 3 |
| `U5d:721` | `part6.md:500` | §6.3 (thirteen places intent meets Layer 1) | POINTER-ONLY | — | pointer-text |
| `U5d:727` | `part6.md:501` | R-09 | POINTER-ONLY | — | pointer-text |
| `U5d:728` | `part6.md:502` | R-10 | POINTER-ONLY | — | pointer-text |
| `U5d:773` | `part6.md:234` | §10 "closed here" (eight family items) | POINTER-ONLY | — | hand: answered in the audit's table ("Not yours") |
| `U5d:782` | `part6.md:236` | VENICE §17 (re-grounding: corrections; mechanisms  | COVERED | B40.14, B40.15, B40.16, B40.17 | stem+section |
| `U5d:784` | `part6.md:238` | COLONIAL §11 item 2 | POINTER-ONLY | — | hand: closed by the synthesis: no `purchase` form |
| `U5d:787` | `part6.md:240` | COLONIAL §16 (re-grounding: corrections; mechanism | COVERED | B40.07, B40.21, B40.22, B40.23 | stem+section |
| `U5d:789` | `part6.md:241` | PAPACY R-1 to R-17 | POINTER-ONLY | — | hand: as the PAPACY rows above; R-11 SUPERSEDED by A-17 |
| `U5d:792` | `part6.md:243` | PAPACY §13 item 3 | COVERED | B32.19 | hand: per-row patronage (PAP_B) |
| `U5d:794` | `part6.md:245` | PAPACY §15 (re-grounding) | COVERED | B40.26, B40.27 | stem+section |
| `U5d:798` | `part6.md:247` | BYZANTINE §14 item 4 | POINTER-ONLY | — | hand: closed by the synthesis: no bar |
| `U5d:817` | `part6.md:332` | §3: the institutions' deterministic text | POINTER-ONLY | — | hand: the families' Reconciled lines; the items carry the reconciled text |

## Appendix C — every row resolved by hand (opened; the ground stated)

| closure row | id | class | carried by | ground |
|---|---|---|---|---|
| `U5a:140` | ARC-44, EMG-C4, EMG-C3, EMG-X8, ARC-20 · long span | HELD-TABLE | — | claim_fade Edit 5 (lift MAX_SEASONS) needs an eight-season flat reading; B09 does not carry it (part 11_cont, B09 UNDECIDED (1)); A-114 holds runs past two seasons to B99; H2_DECISIONS HD-26: B98 lists it BLOCKED (A-114), B99 reads it |
| `U5a:151` | needs wrongly stated: prose spans; `UNCLEAR:` rows | POINTER-ONLY | — | points at the rows above; the UNCLEAR rows close nothing |
| `U5a:215` | §7.1 the slate (design) against the per-person que | COVERED | B34.16 | CORE-SC Edit 5 (resolution 20) |
| `U5a:284` | §4 `[not adjudicated]` `tests/valoria/test_fractio | COVERED | B05.02 | test_fractional_pool.py deleted with its subject (DOE §1; F-DICE-22) |
| `U5a:309` | res. 1–6 | POINTER-ONLY | — | as F-PES-CORE-01..07, each COVERED (B09.02, B09.10, B09.11, B02.13, B02.14, B08.02, B03.16) |
| `U5a:395` | §5 NERS cuts (scar count; the realm-wide draw; `te | POINTER-ONLY | — | each by the finding it restates (F-CHAR-04, -02, -09, -01; F-CORE-05), each COVERED |
| `U5a:422` | the 38 rows read at the dossier excerpt only | POINTER-ONLY | — | closed at U5a §2.7 |
| `U5a:441` | 27, 28, 30 | POINTER-ONLY | — | RESOLVED-BY no edit (decided in the audit) |
| `U5a:475` | F-CHAR-22 | POINTER-ONLY | — | RESOLVED-BY no edit (decided in the audit) |
| `U5a:477` | B2.2 returning findings (six rows) | POINTER-ONLY | — | = F-CHAR-03, F-CHAR-17, F-CHAR-18 and the reason trail, each COVERED |
| `U5a:491` | H-233, H-343 | COVERED | B10.30, B09.13 | goal lean (02_CHAR_goal_lean_on_its_own_question); reason trail (02_CHAR_reason_trail_and_small_edits Part A) |
| `U5a:500` | rows 15, 16, 23 | POINTER-ONLY | — | RESOLVED-BY no edit (decided in the audit) |
| `U5a:569` | C-2 | POINTER-ONLY | — | RESOLVED-BY no edit |
| `U5a:607` | res. 19 (SCN-05 restated: a spend buys named level | COVERED | B05.60 | ADV "The resolution" (Edits A-D) |
| `U5a:620` | §13 NPC-085, SCN-12, SCN-04/07/LOOP-C, SCN-13 | POINTER-ONLY | — | ADV Edit E is "Not built; the door each waits at" (the proposal's own text) |
| `U5a:621` | §13 SCN-05, SCN-02, ARC-23 | COVERED | B05.60 | SCN-05: resolution 19 (ADV); SCN-02 named for SC (ED-SC-0038); ARC-23 SUPERSEDED by A-11 |
| `U5a:637` | F-PES-DICE-05 | COVERED | B09.04 | DOE §4 |
| `U5a:661` | D-01, D-02, D-03 | POINTER-ONLY | — | corrected in place in SC and FI files; U5c rows close the design |
| `U5a:662` | D-04 | COVERED | B15.10 | EXITS Part B superseded by 16_PESSIMIST_PC_A (U3 §4.1 row 55), which B15.10 lands |
| `U5a:663` | D-05 | COVERED | B12c.06, B07.01 | EXITS Part C defers to MAT_A §6 (tend drawn, B12c.06) over 18-A's route (B07.01) |
| `U5a:665` | D-07, D-08, D-09 | POINTER-ONLY | — | FA files as corrected (U5d rows); A-19, A-14 |
| `U5a:777` | §5a `conviction.moved` | COVERED | B10.15 | CHAR_A item 4: the emitter with the Event |
| `U5a:840` | §3 R-03 (DG4) | COVERED | B08.06, B03.16 | no_stored_plan is B03.16; TDA §G (H-172, "lands in B08 with SEQ") was in no item: added by this lane as B08.06 (Covered: C-01) |
| `U5b:70` | F-PC-04 | COVERED | B15.10, B14.27 | EXITS Part B superseded by PC_A (B15.10); PHY_A A3 in B15 |
| `U5b:106` | H-240 | COVERED | B01.01 | P1 lands whole as lane A's e5d6ab9 |
| `U5b:128` | R-PC-14 | COVERED | B12c.06, B07.01 | EXITS Part C: tend drawn (MAT_A §6) |
| `U5b:154` | §13 SCN-03 (two recoveries) | COVERED | B12c.06 | EXITS Part C: tend drawn (MAT_A §6) |
| `U5b:190` | F-PC-20 | CONTENT-OWED | B14.12 | PX item 6 is "not built here": a pike is content (the stated matchup rows of A-113, B19a/B19/B31); B14.12 lands the export |
| `U5b:208` | R-PC-43 | COVERED | B18.02, B14.17, B14.18, B15.15 | P4 Part A (B18.02, with RES-PC §1 item 4); RES-PC §1 items 1-3 (B14.17, B14.18, B15.15) |
| `U5b:223` | F-PES-PC-08 | COVERED | B14.17, B14.18, B15.15 | RES-PC §1: items 1-2 in B14; the slope bound and the fit (item 3) added by this lane as B15.15 (C-03) |
| `U5b:259` | U5a sweep C-12 | COVERED | B15.10 | PHY_A A3 adopted with PC_A in B15 |
| `U5b:325` | CL-TROOP, MB-08, CR-52, CP-T04-04, CP-T04-10 | SUPERSEDED | — | RES-MB §7 edits v11 plan cards, deleted on adoption (B17 UNDECIDED (3)); CR-52 and CP-T04-04 are intake ids (§B) |
| `U5b:437` | U5a F-DICE-18 (C-7) | COVERED | B19.02, B19.05, B19.55, B19.70 | 27-MB (A-59): 27_MB_A, the commander's record; 27A-6 added by this lane as B19.70 (C-02) |
| `U5b:524` | §0.5 the family's one repair | COVERED | B29.01, B22.29, B22.30, B23.10 | the world_q licence readers (warrants_for, field_defender, may_ruin) |
| `U5b:559` | U5a "one `tend` rule" | COVERED | B12c.06 | EXITS Part C: tend drawn (MAT_A §6) |
| `U5b:560` | cases (item 8 of each section) | POINTER-ONLY | — | each case by the verb's own proposal; NPC-088 by A-16's carrier |
| `U5c:285` | R-31 | CONTENT-OWED | B04.03 | two data rows on the skill surface; the verb rows' skill values land with B04.03 (CORE Edit 8) |
| `U5c:306` | C-7 | POINTER-ONLY | — | R-49 dropped as a referent |
| `U5c:348` | F-PES-FI-05 | COVERED | B26.06 | PFI-D edits 1, 3 (the three product-less rows) |
| `U5c:380` | R-19-09 | COVERED | B36.07 | VERD R-19-09 (edit 6, the harness) is B36.07 |
| `U5c:433` | §0.6 | POINTER-ONLY | — | the rows above, each with its prize |
| `U5c:490` | `tend` | COVERED | B12c.06 | MAT_A §6 owns the tend row |
| `U5d:170` | R-32 | POINTER-ONLY | — | WAR-B edit 7 (a) answered no (an outcome Query) |
| `U5d:350` | H-274 | POINTER-ONLY | — | as F-WR-07 (none of its own) |
| `U5d:543` | §5 scripting-drift table (ARC-14, -17, -11, NPC-01 | POINTER-ONLY | — | the audit's table; A-47 and A-15 carried by STAGED and HAPP-A items |
| `U5d:568` | F-PES-GAME-04 | COVERED | B07.01, B15.09, B11.65, B08.05 | the four 18_DETERMINISM carriers |
| `U5d:708` | M9 | POINTER-ONLY | — | U5d Part 2 (each row there carries its own item) |
| `U5d:711` | M16 | POINTER-ONLY | — | U5d Part 7 |
| `U5d:712` | M17 | POINTER-ONLY | — | U5d Part 3 |
| `U5d:773` | §10 "closed here" (eight family items) | POINTER-ONLY | — | answered in the audit's table ("Not yours") |
| `U5d:784` | COLONIAL §11 item 2 | POINTER-ONLY | — | closed by the synthesis: no `purchase` form |
| `U5d:789` | PAPACY R-1 to R-17 | POINTER-ONLY | — | as the PAPACY rows above; R-11 SUPERSEDED by A-17 |
| `U5d:792` | PAPACY §13 item 3 | COVERED | B32.19 | per-row patronage (PAP_B) |
| `U5d:798` | BYZANTINE §14 item 4 | POINTER-ONLY | — | closed by the synthesis: no bar |
| `U5d:817` | §3: the institutions' deterministic text | POINTER-ONLY | — | the families' Reconciled lines; the items carry the reconciled text |

## Appendix D — severities filled in `master/MASTER_FINDINGS_part3.md`..`_part6.md`

The 76 rows whose `id` is an `F-` finding and whose severity cell read `—` (77 finding ids: two rows hold two ids). Each defining line was opened by Appendix A (`grades`); a grade is written only where the audit states one (B blocks, D degrades, H hygiene); every other row reads "unrated in source", and the audit's own category is given here.

| MF row | finding | severity written | the audit's defining line |
|---|---|---|---|
| `part3.md:57` | F-TEST-05 | unrated in source | 01_CORE_audit_addendum_C_tests.md:147 · R-07's named measure begins with a substring test, and the property it names is not the on |
| `part3.md:59` | F-CORE-16 | unrated in source | 01_CORE_audit_addendum_B.md:168 · Layer-1 conformance |
| `part3.md:61` | F-TEST-02 | unrated in source | 01_CORE_audit_addendum_C_tests.md:100 · goldens |
| `part3.md:62` | F-TEST-03 | unrated in source | 01_CORE_audit_addendum_C_tests.md:118 · goldens |
| `part3.md:63` | F-TEST-04 | unrated in source | 01_CORE_audit_addendum_C_tests.md:134 · tests of archived prose |
| `part3.md:64` | F-TEST-06 | unrated in source | 01_CORE_audit_addendum_C_tests.md:164 · the invariant sweep runs on a world with no office, and a test pins that |
| `part3.md:65` | F-TEST-07 | unrated in source | 01_CORE_audit_addendum_C_tests.md:173 · three loops that assert on whatever they are handed |
| `part3.md:66` | F-TEST-08 | unrated in source | 01_CORE_audit_addendum_C_tests.md:185 · the dice golden is 58 % rows the engine refuses or contradicts |
| `part3.md:67` | F-TEST-09 | unrated in source | 01_CORE_audit_addendum_C_tests.md:195 · eight tests assert a substring of source text and nothing else |
| `part3.md:68` | F-TEST-10 | unrated in source | 01_CORE_audit_addendum_C_tests.md:202 · a test that keeps a retired symbol importable; a standing non-strict `xfail` |
| `part3.md:69` | F-TEST-11 | unrated in source | 01_CORE_audit_addendum_C_tests.md:210 · thirteen skips on an absent combat engine |
| `part3.md:73` | F-TEST-02 | unrated in source | 01_CORE_audit_addendum_C_tests.md:100 · goldens |
| `part3.md:74` | F-TEST-02 | unrated in source | 01_CORE_audit_addendum_C_tests.md:100 · goldens |
| `part3.md:75` | F-TEST-03 | unrated in source | 01_CORE_audit_addendum_C_tests.md:118 · goldens |
| `part3.md:76` | F-TEST-04 | unrated in source | 01_CORE_audit_addendum_C_tests.md:134 · tests of archived prose |
| `part3.md:77` | F-TEST-05 | unrated in source | 01_CORE_audit_addendum_C_tests.md:147 · R-07's named measure begins with a substring test, and the property it names is not the on |
| `part3.md:77` | F-TEST-09 | unrated in source | 01_CORE_audit_addendum_C_tests.md:195 · eight tests assert a substring of source text and nothing else |
| `part3.md:78` | F-TEST-06 | unrated in source | 01_CORE_audit_addendum_C_tests.md:164 · the invariant sweep runs on a world with no office, and a test pins that |
| `part3.md:79` | F-TEST-07 | unrated in source | 01_CORE_audit_addendum_C_tests.md:173 · three loops that assert on whatever they are handed |
| `part3.md:80` | F-TEST-08 | unrated in source | 01_CORE_audit_addendum_C_tests.md:185 · the dice golden is 58 % rows the engine refuses or contradicts |
| `part3.md:81` | F-TEST-10 | unrated in source | 01_CORE_audit_addendum_C_tests.md:202 · a test that keeps a retired symbol importable; a standing non-strict `xfail` |
| `part3.md:82` | F-TEST-11 | unrated in source | 01_CORE_audit_addendum_C_tests.md:210 · thirteen skips on an absent combat engine |
| `part3.md:107` | F-CORE-17 | unrated in source | 01_CORE_audit_addendum_B.md:182 · Layer-1 conformance |
| `part3.md:108` | F-CORE-23 | unrated in source | 01_CORE_audit_addendum_B.md:298 · bears on the arcs charge |
| `part3.md:164` | F-PES-CORE-06 | unrated in source | 16_PESSIMIST_CORE.md:484 · touches R-03, R-09 |
| `part3.md:231` | F-PES-CORE-05 | unrated in source | 16_PESSIMIST_CORE.md:479 · touches R-01, R-02 |
| `part3.md:234` | F-TEST-07 | unrated in source | 01_CORE_audit_addendum_C_tests.md:173 · three loops that assert on whatever they are handed |
| `part4.md:56` | F-PC-07 | unrated in source | 03_PC_audit.md:204 · standing requirement (one code path) |
| `part4.md:57` | F-PC-09 | unrated in source | 03_PC_audit.md:227 · design (NERS N) |
| `part4.md:81` | F-PC-16 | unrated in source | 03_PC_audit_addendum_B.md:86 · correctness, latent in the season |
| `part4.md:82` | F-PC-20 | unrated in source | 03_PC_audit_addendum_B.md:133 · integration (the loadout rule's individual side) |
| `part4.md:83` | F-PC-21 | unrated in source | 03_PC_audit_addendum_B.md:140 · design (extends F-PC-09 and F-PC-02) |
| `part4.md:89` | F-PES-PC-08 | unrated in source | 16_PESSIMIST_PC.md:700 · robustness (customisation), latent |
| `part4.md:90` | F-PES-PC-09 | unrated in source | 16_PESSIMIST_PC.md:705 · NERS N |
| `part4.md:91` | F-PES-PC-10 | unrated in source | 16_PESSIMIST_PC.md:711 · premise (the words) |
| `part4.md:92` | F-PES-PC-12 | unrated in source | 16_PESSIMIST_PC.md:721 · standing rule, weapon level |
| `part4.md:119` | F-PC-17 | unrated in source | 03_PC_audit_addendum_B.md:100 · design (refines F-PC-13) |
| `part4.md:123` | F-PES-PC-02 | unrated in source | 16_PESSIMIST_PC.md:660 · design (NERS N, E) |
| `part4.md:124` | F-PES-PC-03 | unrated in source | 16_PESSIMIST_PC.md:668 · standing rule (R-09) |
| `part4.md:125` | F-PES-PC-04 | unrated in source | 16_PESSIMIST_PC.md:674 · calibration, a pattern defect |
| `part4.md:126` | F-PES-PC-07 | unrated in source | 16_PESSIMIST_PC.md:692 · standing rule; completeness |
| `part4.md:127` | F-PES-PC-11 | unrated in source | 16_PESSIMIST_PC.md:716 · premise (genre) |
| `part4.md:154` | F-PC-18 | unrated in source | 03_PC_audit_addendum_B.md:116 · design (an unclear passage in the intent, resolved) |
| `part4.md:155` | F-PC-19 | unrated in source | 03_PC_audit_addendum_B.md:126 · contract (Layer 1) |
| `part4.md:325` | F-MB-24 | unrated in source | 04_MB_audit_addendum_B.md:291 · Layer 1 non-conformance |
| `part5.md:42` | F-PES-FI-12 | H | 16_PESSIMIST_FI.md:770 · hygiene (performance) |
| `part5.md:43` | F-PES-FI-13 | H | 16_PESSIMIST_FI.md:771 · hygiene |
| `part5.md:91` | F-PES-FI-01 | B (blocks R-05; also degrades R-01, R-07) | 16_PESSIMIST_FI.md:759 · blocks R-05; degrades R-01, R-07 |
| `part5.md:92` | F-PES-FI-02 | D | 16_PESSIMIST_FI.md:760 · degrades R-01, R-07 |
| `part5.md:93` | F-PES-FI-03 | D | 16_PESSIMIST_FI.md:761 · degrades R-05, R-08 |
| `part5.md:94` | F-PES-FI-04 | B | 16_PESSIMIST_FI.md:762 · blocks R-07, R-08 (with F-FI-01) |
| `part5.md:95` | F-PES-FI-06 | D | 16_PESSIMIST_FI.md:764 · degrades R-09 |
| `part5.md:96` | F-PES-FI-07 | D | 16_PESSIMIST_FI.md:765 · degrades R-05, R-09 |
| `part5.md:97` | F-PES-FI-08 | D | 16_PESSIMIST_FI.md:766 · degrades R-06, R-08 |
| `part5.md:98` | F-PES-FI-09 | D | 16_PESSIMIST_FI.md:767 · degrades R-01 |
| `part5.md:99` | F-PES-FI-10 | D | 16_PESSIMIST_FI.md:768 · degrades R-01 (a warning on a scheduled edit) |
| `part5.md:100` | F-PES-FI-11 | D | 16_PESSIMIST_FI.md:769 · degrades R-09 (the standing rule) |
| `part5.md:126` | F-PES-FI-05 | D | 16_PESSIMIST_FI.md:763 · degrades R-04, R-05 |
| `part5.md:208` | F-FA-18 | unrated in source | 06_FA_audit_addendum_B.md:197 · design that exists only as prose |
| `part5.md:232` | F-FA-14 | unrated in source | 06_FA_audit_addendum_B.md:125 · design defect in a planned position |
| `part5.md:258` | F-PES-FA-11 | unrated in source | 16_PESSIMIST_FA.md:566 · a sibling proposal's interaction |
| `part5.md:510` | F-DICE-10 | unrated in source | 10_DICE_audit.md:323 · evidence, accepted |
| `part5.md:613` | F-GO-17 | unrated in source | 11_GO_audit_addendum_B.md:148 · CORRECTS SURF §3 |
| `part5.md:614` | F-GO-18 | unrated in source | 11_GO_audit_addendum_B.md:161 · CORRECTS F-GO-08 and R20 |
| `part5.md:625` | F-PES-GO-11 | unrated in source | 16_PESSIMIST_GO.md:596 · CORRECTS F-GO-16 |
| `part6.md:143` | F-VM-01 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:144` | F-VM-02 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:145` | F-VM-03 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:146` | F-VM-04 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:146` | F-VM-05 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:147` | F-VM-06 | D | 14_VERBS_MILITARY.md:101 · degrades narrative; touches R-09 |
| `part6.md:514` | F-C1A-01 | unrated in source | 17_CENSUS_C1A.md:67 · the person projection is a client read with no client (dead; batch D2). |
| `part6.md:515` | F-C1A-05 | unrated in source | 17_CENSUS_C1A.md:105 · three Layer 1 queries have no caller (extension; broken; reader owed, no proposal names |
| `part6.md:516` | F-C1A-06 | unrated in source | 17_CENSUS_C1A.md:113 · small dead matter (extension; batch D1, D3).** `cast.defects` (`data/cast.py:408-423`) has |
| `part6.md:550` | F-C1A-02 | unrated in source | 17_CENSUS_C1A.md:79 · the character sheet's spaces are entered by tests only (broken; W1, carried by GO). |
| `part6.md:551` | F-C1A-03 | unrated in source | 17_CENSUS_C1A.md:87 · six helper rows serve effects that never ran (broken; W2, carried by VERBS).** The symbols |
| `part6.md:552` | F-C1A-04 | unrated in source | 17_CENSUS_C1A.md:95 · `beneficiary:` is a validated column no decision reads (extension; broken; W4). |
| `part6.md:553` | F-C1A-07 | unrated in source | 17_CENSUS_C1A.md:122 · nine comment pointers name files that moved or were dropped (extension; mislabelled; C1). |

## Appendix E — the 297 ids of `master/eval/V12_INTAKE.md` §5, each placed

Generated by Appendix A (`intake`). An id is matched verbatim (a trailing "(b)" dropped) or by the authors' citation of its entry line (`intake `:NNN``), in an item's heading, `SOURCE:` line or position-table row. "head" = `workplan_v12.md` §3.A carries the rule (each of the 22 rows opened). "held" = the entry sits under the intake's "held / LEAVE" heading: not an item (`V12_STRUCTURE_part2.md` §5.6), a row of H2's held table (§7.9). The state is the first carrying item's. `*` marks an id the earlier scan found absent verbatim.

| intake line | lane | id | class | carried by | state |
|---|---|---|---|---|---|
| `:79` | IN | P1 | COVERED (head §3.A) | — | — |
| `:80` | IN | P2 | COVERED (head §3.A) | B20.11, B20.12, B20.19, B20.21 | BUILD |
| `:81` | IN | P3b | COVERED (head §3.A) | — | — |
| `:82` | IN | P4 | COVERED (head §3.A) | B27.19 | DESIGN-FIRST |
| `:83` | IN | P5 | COVERED (head §3.A) | — | — |
| `:84` | IN | P6 | COVERED (head §3.A) | — | — |
| `:85` | IN | P7 | COVERED (head §3.A) | — | — |
| `:86` | IN | P8 | COVERED (head §3.A) | B05.63 | BUILD |
| `:87` | IN | P9 | COVERED (head §3.A) | — | — |
| `:88` | IN | P10 | COVERED (head §3.A) | — | — |
| `:89` | IN | P11 | COVERED (head §3.A) | B21s.02 | BUILD |
| `:90` | IN | P12 | COVERED (head §3.A) | — | — |
| `:91` | IN | P14 | COVERED (head §3.A) | B12c.30 | BLOCKED |
| `:92` | IN | P15 | COVERED (head §3.A) | — | — |
| `:93` | IN | P16 | COVERED (head §3.A) | B11F2.01, B11F2.04 | POINTER |
| `:94` | IN | V1 | COVERED (head §3.A) | — | — |
| `:95` | IN | V2 | COVERED (head §3.A) | — | — |
| `:96` | IN | V3 | COVERED (head §3.A) | — | — |
| `:97` | IN | V4 | COVERED (head §3.A) | — | — |
| `:98` | IN | -00 §6 risk 2* | COVERED (head §3.A) | — | — |
| `:99` | IN | -00 §6 risk 4* | COVERED (head §3.A) | — | — |
| `:100` | IN | -00 §6 risk 6* | COVERED (head §3.A) | — | — |
| `:104` | IN | H-1 | COVERED | B00.02 | BUILD |
| `:108` | IN | V9-27 | COVERED | B02.34 | BUILD |
| `:109` | IN | DEF-8 | COVERED | B02.35 | POINTER |
| `:110` | IN | H-2 | COVERED | B02.36 | BUILD |
| `:114` | IN | IN-44 | COVERED | B03.57, B03.70, B03.71, B12b.18 | BUILD |
| `:115` | IN | CR-07 | COVERED | B03.69 | BLOCKED |
| `:115` | IN | H-89 | COVERED | B03.69 | BLOCKED |
| `:116` | IN | A1-46 | COVERED | B03.69 | BLOCKED |
| `:117` | IN | A1-81 | COVERED | B03.71 | BUILD |
| `:118` | IN | A2-40 | COVERED | B03.72 | BUILD |
| `:119` | IN | ER-C4 | COVERED | B03.73 | BUILD |
| `:120` | IN | ER-GF9 | COVERED | B03.74 | BUILD |
| `:121` | IN | H-141 | COVERED | B03.75 | BUILD |
| `:122` | IN | H-143 | COVERED | B03.76 | BUILD |
| `:123` | IN | V9-02 | COVERED | B03.77 | BUILD |
| `:124` | IN | V9-20 | COVERED | B03.78 | BUILD |
| `:125` | IN | DEF-5 | COVERED | B03.69 | BLOCKED |
| `:126` | IN | REM-26 | COVERED | B03.79 | READING |
| `:127` | IN | H-4 | COVERED | B03.80 | BUILD |
| `:131` | IN | H-249 | COVERED | B08.01, B08.04, B08.99 | BUILD |
| `:135` | IN | H-130 | COVERED | B03.84 | BUILD |
| `:136` | IN | H-137 | COVERED | B03.83 | BUILD |
| `:137` | IN | H-138 | COVERED | B03.84, B11.07, B12a.72 | BUILD |
| `:138` | IN | H-139 | COVERED | B03.84, B03.85 | BUILD |
| `:142` | IN | H-145 | COVERED | B09.09 | BUILD |
| `:142` | IN | NM-W9 | COVERED | B09.09, B09.10 | BUILD |
| `:143` | IN | IN-58 | COVERED | B09.20, B33.25 | BLOCKED |
| `:144` | IN | H-135 | COVERED | B03.83, B09.21 | BUILD |
| `:148` | IN | CL-PERSON | COVERED | B10.53, B10.58, B10.82, BA1.02 | DESIGN-FIRST |
| `:149` | IN | CR-93 | COVERED | B10.01, B10.28, B10.31, B10.51 | POINTER |
| `:150` | IN | CR-95 | COVERED | B10.52, B10.81 | DESIGN-FIRST |
| `:151` | IN | M34 | COVERED | B10.53, B10.58 | DESIGN-FIRST |
| `:152` | IN | M36 | COVERED | B10.53, B10.82 | DESIGN-FIRST |
| `:153` | IN | M40 | COVERED | B10.31, B10.53 | BUILD |
| `:154` | IN | A1-05 | COVERED | B10.74 | READING |
| `:155` | IN | H-191 | COVERED | B10.75, B10.78 | BLOCKED |
| `:156` | IN | H-198 | COVERED | B10.76 | BLOCKED |
| `:156` | IN | M9 | COVERED | B10.76 | BLOCKED |
| `:157` | IN | ER-JF10 | COVERED | B10.27, B10.77 | BUILD |
| `:158` | IN | H-180 | COVERED | B10.63 | BUILD |
| `:159` | IN | V9-11 | COVERED | B10.74 | READING |
| `:160` | IN | DEF-12 | COVERED | B10.78 | POINTER |
| `:161` | IN | B10-16 gates | COVERED | B10.79, B12c.30 | BLOCKED |
| `:161` | IN | IN-52 and `requi | COVERED | B10.79 | BLOCKED |
| `:165` | IN | CR-83 | COVERED | B11.02, B11.75, B11.78 | DESIGN-FIRST |
| `:166` | IN | A2-43 | COVERED | B11.03, B11.04 | BUILD |
| `:170` | IN | M38 | COVERED | B21.78 | POINTER |
| `:174` | IN | CR-47 | COVERED | B12a.03 | BUILD |
| `:175` | IN | G-05 | COVERED | B05.19, B12c.21, B12c.23 | BUILD |
| `:179` | IN | SE-05 | COVERED | B21b.05, B12c.09 | BUILD |
| `:183` | IN | CR-92 | COVERED | B24.41, B26.16 | DESIGN-FIRST |
| `:187` | IN | CR-106 | COVERED | B11F1.01, B11F1.02 | BUILD |
| `:191` | IN | CR-74 | COVERED | B21s.02, B33.25, B33.29 | BUILD |
| `:195` | IN | CR-51 | COVERED | B29.03 | BUILD |
| `:199` | IN | CR-104 | COVERED | B11F2.02 | BUILD |
| `:200` | IN | CR-97 | COVERED | B11F2.01, B11F2.03 | POINTER |
| `:201` | IN | CR-98 | COVERED | B11F2.05, B38.70 | BUILD |
| `:201` | IN | H-106 | COVERED | B11.07, B11F2.05 | BUILD |
| `:201` | IN | H-25 | COVERED | B11F2.05 | BUILD |
| `:202` | IN | CR-99 | COVERED | B11F2.06 | BUILD |
| `:203` | IN | CR-100 | COVERED | B11F2.07 | BUILD |
| `:204` | IN | CR-101 | COVERED | B11F2.08 | BUILD |
| `:205` | IN | CR-102 | COVERED | B11F2.09 | BUILD |
| `:206` | IN | CR-103 | COVERED | B11F2.10 | HELD |
| `:207` | IN | CR-105 | COVERED | B11F2.10, B11F2.11 | HELD |
| `:208` | IN | P16 section 3.1 rules | COVERED | B11F2.01 | POINTER |
| `:208` | IN | 3.5 dec | COVERED | B11F2.01 | POINTER |
| `:209` | IN | P16 section 3.6 owed correctio | COVERED | B11F2.04 | POINTER |
| `:213` | IN | NM-W5 | COVERED | B36.08 | BUILD |
| `:217` | IN | CL-MGMT | HELD-TABLE (for H2) | — | — |
| `:218` | IN | IN-18 | HELD-TABLE (for H2) | — | — |
| `:219` | IN | DEF-2 | HELD-TABLE (for H2) | — | — |
| `:220` | IN | DEF-10* | HELD-TABLE (for H2) | — | — |
| `:221` | IN | DEF-11* | HELD-TABLE (for H2) | — | — |
| `:222` | IN | REM-30* | HELD-TABLE (for H2) | — | — |
| `:229` | FA | H-291 | COVERED | B03.81 | BUILD |
| `:233` | FA | M8 | COVERED | B21.77, B21c.05, B21c.09 | POINTER |
| `:234` | FA | §1b-3 | COVERED | B21.77, B21c.04, B21c.05 | POINTER |
| `:235` | FA | A2-14 | COVERED | B21.77, B21c.05 | POINTER |
| `:239` | FA | IN-30 | COVERED | B21b.05, B21b.06, B21b.08 | BUILD |
| `:240` | FA | CP-T09-04 | COVERED | B21b.04, B21b.06 | BUILD |
| `:241` | FA | CP-T09-01 | COVERED | B21b.07, B21b.08, B21b.09, B21b.19 | BUILD |
| `:242` | FA | CP-T09-05 | COVERED | B21b.10 | BUILD |
| `:243` | FA | CP-T09-02 | COVERED | B21b.11, B21b.12 | BUILD |
| `:244` | FA | CP-T09-03 | COVERED | B21b.14, B21b.15 | BUILD |
| `:245` | FA | CP-T09-07 | COVERED | B21.79, B21.57, B21b.16, B21b.21 | BUILD |
| `:246` | FA | CR-09 | COVERED | B21.79, B21b.21, B21b.22 | BUILD |
| `:246` | FA | H-101 | COVERED | B21.79, B21b.21 | BUILD |
| `:247` | FA | CP-T09-09 | COVERED | B21b.17, B21b.18, B21b.19, B21b.20 | BUILD |
| `:248` | FA | H-108 | COVERED | B21b.24, B21b.25 | DESIGN-FIRST |
| `:248` | FA | IN-48 | COVERED | B21b.24, B21b.25 | DESIGN-FIRST |
| `:249` | FA | IN-36 | COVERED | B21b.01, B21b.02, B21b.03, B21b.13 | BUILD |
| `:250` | FA | FA-01 | COVERED | B11.04, B21b.26 | BUILD |
| `:251` | FA | CR-91 | COVERED | B21b.13, B21d.06, B21d.08, B38.06 | BUILD |
| `:252` | FA | §1a-M1res | COVERED | B21b.01, B21b.02 | BUILD |
| `:253` | FA | §1a-(c) | COVERED | B21b.05 | BUILD |
| `:254` | FA | FA-02 | COVERED | B21b.05 | BUILD |
| `:255` | FA | H-132 | COVERED | B21.69, B21b.27 | BUILD |
| `:256` | FA | H-133 | COVERED | B03.84, B21b.23 | BUILD |
| `:257` | FA | H-142 | COVERED | B21b.22 | BUILD |
| `:258` | FA | V9-14 | COVERED | B21b.01, B21b.02 | BUILD |
| `:259` | FA | ED-406 | COVERED | B21b.19, B21b.20 | POINTER |
| `:260` | FA | ED-407 | COVERED | B21b.20 | POINTER |
| `:261` | FA | ED-609 | COVERED | B21b.09 | POINTER |
| `:262` | FA | G-19 | COVERED | B10.72, B21b.03 | BUILD |
| `:263` | FA | TL-B5.2 | COVERED | B21b.03 | POINTER |
| `:264` | FA | §2 `covenant` formation (PR #5* | COVERED | B21b.14, B21b.15 | BUILD |
| `:268` | FA | CR-32 | COVERED | B21c.01 | BUILD |
| `:268` | FA | H-181 | COVERED | B21c.01 | BUILD |
| `:269` | FA | CR-35 | COVERED | B21c.02, B21c.03 | BUILD |
| `:269` | FA | H-217 | COVERED | B11.07, B21c.02 | BUILD |
| `:270` | FA | CR-36 | COVERED | B21.77, B21c.04, B24a.01, B27.21 | POINTER |
| `:271` | FA | CR-37 | COVERED | B21.06, B21.77, B21b.18, B21c.05 | POINTER |
| `:272` | FA | CR-38 | COVERED | B21.78, B21c.06, B21c.07, B21c.08 | POINTER |
| `:272` | FA | H-90 | COVERED | B21c.04, B21c.06, B24a.01, B24a.04 | BUILD |
| `:273` | FA | CR-39 | COVERED | B21c.08 | HELD |
| `:274` | FA | §2 `depose` (M8; the verb suit* | COVERED | B21c.05, B21c.09 | BUILD |
| `:278` | FA | CR-89 | COVERED | B21b.13, B21d.02, B21d.03, B21d.06 | BUILD |
| `:279` | FA | CR-90 | COVERED | B21d.04, B21d.07 | BUILD |
| `:280` | FA | CR-88 | COVERED | B10.30, B21d.01, B21d.05, B33.45 | BUILD |
| `:284` | FA | H-313 | COVERED | B03.81, B25.11 | BUILD |
| `:288` | FA | H-278 | COVERED | B32.23 | BUILD |
| `:292` | FA | A2-23 | COVERED | B23.16 | BUILD |
| `:293` | FA | H-229 | COVERED | B24a.01, B24a.08, B28.02, B28.06 | BUILD |
| `:297` | FA | M39 | HELD-TABLE (for H2) | — | — |
| `:298` | FA | ED-640* | HELD-TABLE (for H2) | — | — |
| `:299` | FA | ED-649* | HELD-TABLE (for H2) | — | — |
| `:300` | FA | ED-650* | HELD-TABLE (for H2) | — | — |
| `:301` | FA | ED-651* | HELD-TABLE (for H2) | — | — |
| `:302` | FA | ED-653* | HELD-TABLE (for H2) | — | — |
| `:303` | FA | G-18 | HELD-TABLE (for H2) | B05.19, B12a.16 | BUILD |
| `:304` | FA | §2 an emerged creed's `seize`* | HELD-TABLE (for H2) | — | — |
| `:305` | FA | §2 the Cardinal electorate* | HELD-TABLE (for H2) | — | — |
| `:312` | SE | CR-40 | COVERED | B12c.01 | BUILD |
| `:313` | SE | CP-T08-01 | COVERED | B12c.01, B12c.02, B38.87 | BUILD |
| `:314` | SE | CP-T08-03 | COVERED | B12c.03 | BUILD |
| `:315` | SE | CP-T08-02 | COVERED | B12a.51, B12a.54, B12b.44 | BUILD |
| `:316` | SE | CP-T08-05 | COVERED | B12c.16, B12c.17 | BUILD |
| `:317` | SE | CP-T08-06 | COVERED | B12b.26 | HELD |
| `:318` | SE | CP-T08-08 | COVERED | B12c.18 | BUILD |
| `:319` | SE | CP-T08-04 | COVERED | B12c.25 | BUILD |
| `:320` | SE | IN-52 | COVERED | B10.79, B12b.31, B12b.47, B12c.30 | BLOCKED |
| `:321` | SE | CR-22 | COVERED | B12b.44, B12b.45 | BUILD |
| `:321` | SE | H-11 | COVERED | B12b.44 | BUILD |
| `:321` | SE | H-125 | COVERED | B12b.44 | BUILD |
| `:322` | SE | CR-49 | COVERED | B12a.03, B12b.29, B12c.11, B12c.14 | BUILD |
| `:323` | SE | CR-67 | COVERED | B12a.05, B24a.02 | BUILD |
| `:324` | SE | H-171 | COVERED | B12b.17, B12b.18, B12b.21, B12b.27 | POINTER |
| `:325` | SE | DEF-7 | COVERED | B12b.47 | BUILD |
| `:326` | SE | P14 B10-16 gates | COVERED | B12c.30 | BLOCKED |
| `:326` | SE | IN-52 | COVERED | B10.79, B12b.31, B12b.47, B12c.30 | BLOCKED |
| `:326` | SE | `requ | COVERED | B12c.30 | BLOCKED |
| `:330` | SE | CR-107 | COVERED | B11F1.03, B11F1.04, B11F1.05, B11F2.01 | BUILD |
| `:331` | SE | P16 section 3.4 territory caps* | COVERED | B11F1.06 | DESIGN-FIRST |
| `:335` | SE | CP-T08-07 | COVERED | B12b.26, B33.30 | HELD |
| `:339` | SE | H-325 | COVERED | B11.01, B11.07, B11.68, B12c.10 | DESIGN-FIRST |
| `:339` | SE | H-326 | COVERED | B11.01, B12c.10 | DESIGN-FIRST |
| `:343` | SE | CP-T04-10* | HELD-TABLE (for H2) | — | — |
| `:344` | SE | H-39 | HELD-TABLE (for H2) | — | — |
| `:345` | SE | ED-507 | HELD-TABLE (for H2) | — | — |
| `:346` | SE | ED-610* | HELD-TABLE (for H2) | — | — |
| `:347` | SE | §2 the `heritage` member of `p* | HELD-TABLE (for H2) | — | — |
| `:354` | WR | CP-T10-01 | COVERED | B12b.02, B12b.04, B12b.10 | BUILD |
| `:355` | WR | CP-T10-03 | COVERED | B12b.01, B12b.44 | BUILD |
| `:356` | WR | CL-EVENTS | COVERED | B12b.43, B12b.44, B12b.45, B12b.46 | BUILD |
| `:357` | WR | CP-T10-02 | COVERED | B12b.07, B12b.08 | POINTER |
| `:361` | WR | CR-73 | COVERED | B12b.43, B21s.01 | BUILD |
| `:365` | WR | CP-T10-06 | COVERED | B37p.01 | BUILD |
| `:366` | WR | CP-T10-07 | COVERED | B37p.03 | BUILD |
| `:367` | WR | CP-T10-09 | COVERED | B37p.02 | BUILD |
| `:368` | WR | CP-T10-04 | COVERED | B37p.04, B37p.05 | BUILD |
| `:372` | WR | G-14 | COVERED | B27.18, B28.31, B38.77 | BUILD |
| `:373` | WR | TL-B4.1 | COVERED | B27.18 | BUILD |
| `:374` | WR | TL-B4.2 | COVERED | B28.32 | BUILD |
| `:378` | WR | CR-13 | COVERED | B35.03 | BUILD |
| `:379` | WR | CP-T07-02 | COVERED | B35.10 | BUILD |
| `:379` | WR | H-47 | COVERED | B35.10 | BUILD |
| `:379` | WR | H-62 | COVERED | B11.07, B35.10 | BUILD |
| `:380` | WR | CP-T07-03 | COVERED | B35.11, B35.19 | BUILD |
| `:381` | WR | CP-T07-05 | COVERED | B35.12 | BUILD |
| `:382` | WR | CP-T07-09 | COVERED | B35.13 | BUILD |
| `:383` | WR | CP-T07-04 | COVERED | B35.14 | BUILD |
| `:384` | WR | CP-T07-06 | COVERED | B35.15 | BUILD |
| `:385` | WR | CP-T07-07 | COVERED | B35.16 | BUILD |
| `:386` | WR | CP-T07-10 | COVERED | B35.17 | BUILD |
| `:387` | WR | CP-T07-08 | COVERED | B35.18 | BUILD |
| `:388` | WR | CP-T07-11 | COVERED | B35.19 | BUILD |
| `:389` | WR | WR-01 | COVERED | B35.20, B35.21 | BUILD |
| `:390` | WR | ER-GF10 | COVERED | B35.03 | BUILD |
| `:391` | WR | ED-WR-0005 | COVERED | B35.03 | BUILD |
| `:392` | WR | G-21 | COVERED | B35.21 | POINTER |
| `:396` | WR | NM-W6* | HELD-TABLE (for H2) | — | — |
| `:397` | WR | NM-W7* | HELD-TABLE (for H2) | — | — |
| `:398` | WR | NM-W8* | HELD-TABLE (for H2) | — | — |
| `:399` | WR | CL-THRUST | HELD-TABLE (for H2) | B21b.03, B27.18, B28.32, B35.21 | POINTER |
| `:400` | WR | ED-595* | HELD-TABLE (for H2) | — | — |
| `:401` | WR | ED-596* | HELD-TABLE (for H2) | — | — |
| `:402` | WR | ED-597* | HELD-TABLE (for H2) | — | — |
| `:403` | WR | ED-598* | HELD-TABLE (for H2) | — | — |
| `:404` | WR | ED-599* | HELD-TABLE (for H2) | — | — |
| `:405` | WR | ED-601* | HELD-TABLE (for H2) | — | — |
| `:406` | WR | ED-602* | HELD-TABLE (for H2) | — | — |
| `:407` | WR | G-04 | HELD-TABLE (for H2) | B22.19, B22.21, B22.26 | BUILD |
| `:408` | WR | G-09 | HELD-TABLE (for H2) | — | — |
| `:409` | WR | G-10 | HELD-TABLE (for H2) | — | — |
| `:410` | WR | G-24* | HELD-TABLE (for H2) | — | — |
| `:411` | WR | G-26 | HELD-TABLE (for H2) | B10.59 | BUILD |
| `:412` | WR | TL-B6.n | HELD-TABLE (for H2) | — | — |
| `:413` | WR | §2 the deed lie (H-198 rule (i* | HELD-TABLE (for H2) | — | — |
| `:414` | WR | §2 the Goldenfurt deck (28 car* | HELD-TABLE (for H2) | — | — |
| `:415` | WR | §2 the eleven named cards* | HELD-TABLE (for H2) | — | — |
| `:416` | WR | §2 the arcs (55 numbers, 58 ar…* | HELD-TABLE (for H2) | — | — |
| `:417` | WR | DEF-3* | HELD-TABLE (for H2) | — | — |
| `:424` | SC | H-199 | COVERED | B05.64 | BUILD |
| `:428` | SC | SC-02 | COVERED | B24.02, B27.23 | BUILD |
| `:429` | SC | H-311 | COVERED | B24.23 | BUILD |
| `:433` | SC | CR-58 | COVERED | B24a.01 | BUILD |
| `:434` | SC | CR-59 | COVERED | B24a.03 | BUILD |
| `:435` | SC | CR-60 | COVERED | B24.09, B24.10, B24a.04, B27.19 | BUILD |
| `:436` | SC | CR-61 | COVERED | B24.01, B24.10, B24a.05, B25.09 | BUILD |
| `:437` | SC | CR-62 | COVERED | B24a.06 | BUILD |
| `:438` | SC | CR-64 | COVERED | B24a.07 | BUILD |
| `:439` | SC | CR-63 | COVERED | B24a.08, B28.13 | BUILD |
| `:443` | SC | H-286 | COVERED | B28.28 | BUILD |
| `:447` | SC | CR-65 | COVERED | B27.19 | DESIGN-FIRST |
| `:448` | SC | CR-66 | COVERED | B27.20 | DESIGN-FIRST |
| `:449` | SC | SC-07 | COVERED | B27.21 | BUILD |
| `:450` | SC | A1-87 | COVERED | B27.22 | DESIGN-FIRST |
| `:450` | SC | H-222 | COVERED | B27.22 | DESIGN-FIRST |
| `:451` | SC | H-219 | COVERED | B11.07, B27.23 | BUILD |
| `:452` | SC | H-227 | COVERED | B27.24 | BUILD |
| `:453` | SC | H-153 | COVERED | B27.25 | BUILD |
| `:454` | SC | H-154 | COVERED | B27.25 | BUILD |
| `:455` | SC | H-173 | COVERED | B27.26 | BUILD |
| `:459` | SC | §2 social-contest wording rows* | HELD-TABLE (for H2) | — | — |
| `:466` | FI | CP-T06-09 | COVERED | B11.58 | BUILD |
| `:467` | FI | CR-29 | COVERED | B11.03, B11.04, B11.58, B21b.26 | BUILD |
| `:467` | FI | H-214 | COVERED | B11.03, B11.04 | BUILD |
| `:467` | FI | H-224 | COVERED | B11.03, B11.04 | BUILD |
| `:468` | FI | CP-T06-01 | COVERED | B11.59 | BUILD |
| `:469` | FI | CP-T06-03 | COVERED | B11.61 | BUILD |
| `:469` | FI | CP-T06-04 | COVERED | B11.61, B11.83 | BUILD |
| `:469` | FI | H-314 | COVERED | B11.61 | BUILD |
| `:470` | FI | CP-T06-02 | COVERED | B11.63 | BUILD |
| `:471` | FI | CP-T06-07 | COVERED | B11.64 | BUILD |
| `:472` | FI | ED-IN-0298 | COVERED | B11.03, B11.04, B21b.26 | BUILD |
| `:476` | FI | CP-T06-05 | COVERED | B25.08, B25.14, B26.01, B26.06 | POINTER |
| `:480` | FI | H-169 | COVERED | B26.08, B26.09, B26.10, B26.16 | BUILD |
| `:484` | FI | G-03 | HELD-TABLE (for H2) | B26.11 | BUILD |
| `:491` | PC | CP-T03-06 | COVERED | B14.14, B15.14 | POINTER |
| `:492` | PC | PC-21 | COVERED | B14.28 | DESIGN-FIRST |
| `:496` | PC | ED-SC-0001 | COVERED | B15.13 | READING |
| `:500` | PC | GV-G12 | COVERED | B27.27 | READING |
| `:504` | PC | CR-85 | COVERED | B14.06, B39.07, B39.35 | BUILD |
| `:508` | PC | CP-T03-10* | HELD-TABLE (for H2) | — | — |
| `:509` | PC | PC-22 | HELD-TABLE (for H2) | — | — |
| `:510` | PC | PC-08 | HELD-TABLE (for H2) | — | — |
| `:517` | MB | ED-1043 | COVERED | B19.10 | BUILD |
| `:521` | MB | ED-MB-0045 | COVERED | B19.12, B19.16 | BUILD |
| `:525` | MB | H-342 | COVERED | B23.18 | BUILD |
| `:529` | MB | CP-T04-04* | HELD-TABLE (for H2) | — | — |
| `:530` | MB | ED-606 | HELD-TABLE (for H2) | — | — |
| `:531` | MB | ED-607 | HELD-TABLE (for H2) | — | — |
| `:532` | MB | ED-820 | HELD-TABLE (for H2) | — | — |
| `:539` | GO | GO-09 | COVERED | B03g.01, B16L.99 | BUILD |
| `:540` | GO | GO-11 | COVERED | B03.18, B03.20, B03g.02 | BUILD |
| `:541` | GO | GO-01 | COVERED | B03g.03, B03g.04 | BUILD |
| `:542` | GO | GO-05 | COVERED | B03g.04 | BUILD |
| `:546` | GO | GO-10 | COVERED | B41.03 | BUILD |
| `:547` | GO | GO-12 | COVERED | B06.05, B41.02 | BUILD |
| `:548` | GO | GO-08 | COVERED | B41.06, B41.07, B41.14 | BUILD |
| `:549` | GO | GO-15 | COVERED | B41.13, B41.14 | BUILD |
| `:553` | GO | GO-06 | HELD-TABLE (for H2) | — | — |
| `:554` | GO | ED-509 | HELD-TABLE (for H2) | B03g.03 | BUILD |
| `:555` | GO | H-5 | HELD-TABLE (for H2) | — | — |

## Appendix F — the instruction suite and the codebase items (129 handles)

Generated by Appendix A (`suite`): every `IS-…` handle that heads an item or a pointer/blocked row in `master/instructions/IS_*.md`, and CI-01..CI-11, MBA-01..MBA-09, PCR-1..PCR-4. "COVERED" = an item's heading, `SOURCE:` line or position row names it.

| handle | class | carried by |
|---|---|---|
| CI-01 | COVERED | B03a.01 |
| CI-02 | COVERED | B03a.02 |
| CI-03 | COVERED | B03.12, B03.13 |
| CI-04 | COVERED | B03.14 |
| CI-05 | COVERED | B03.15 |
| CI-06 | COVERED | B03.67 |
| CI-07 | COVERED | B03c.01, B03c.02, B11.70 |
| CI-08 | COVERED | B03.11 |
| CI-09 | COVERED | B13.01 |
| CI-10 | COVERED | B03.01 |
| CI-11 | COVERED | B02.17 |
| IS-A-01 | COVERED | B02.13 |
| IS-A-02 | COVERED | B02.38 |
| IS-A-03 | COVERED | B02.19 |
| IS-A-04 | COVERED | B02.13, B02.31 |
| IS-A-05 | COVERED | B02.32, B10.12 |
| IS-A-06 | COVERED | B02.18 |
| IS-A-07 | COVERED | B02.20, B38.71, B38.99 |
| IS-A-08 | COVERED | B35.28, B35.29, B38.51, B38.84, B38.99 |
| IS-A-09 | COVERED | B22.10, B22.11 |
| IS-A-10 | COVERED | B07.05 |
| IS-A-11 | COVERED | B04.26, BA1.01, BA1.02, BA1.03, BA1.04, BA1.05 |
| IS-A-12 | COVERED | B02.37, B04.26, B05.99, B10.99, B21.99, B11.99 |
| IS-A-13 | MENTIONED | — |
| IS-B2-CHAR-01 | COVERED | B11.79 |
| IS-B2-CHAR-02 | COVERED | B10.57, BA1.04, B24.12, B24.13, B16.09 |
| IS-B2-CHAR-03 | COVERED | BA1.01, BA1.03, BA1.08, BA1.99 |
| IS-B2-CHAR-04 | COVERED | B04.25 |
| IS-B2-CHAR-05 | COVERED | B04.02 |
| IS-B2-CHAR-06 | COVERED | B05.65, B10.83, BA1.11 |
| IS-B2-CHAR-07 | COVERED | B10.58, BA1.02 |
| IS-B2-CORE-01 | COVERED | B21.76, B11.05, B11.70, B24.15, B34.04, B39.31 |
| IS-B2-CORE-02 | COVERED | B21.76, B11.06 |
| IS-B2-CORE-03 | COVERED | B02.20, B11.76, B11.81 |
| IS-B2-CORE-04 | COVERED | B02.32, B10.12 |
| IS-B2-CORE-05 | COVERED | B28.01, B28.15, B28.18, B28.29 |
| IS-B2-CORE-06 | COVERED | B03.69 |
| IS-B2-CORE-07 | COVERED | B02.09, B02.10, B02.11, B02.12, B02.26, B02.30 |
| IS-B2-FI-01 | COVERED | B11.82, B11.99 |
| IS-B2-FI-02 | COVERED | B11.57 |
| IS-B2-FI-03 | COVERED | B11.76 |
| IS-B2-FI-04 | COVERED | B11.77 |
| IS-B2-FI-05 | COVERED | B11.02, B11.78 |
| IS-B2-FI-06 | COVERED | B11.80 |
| IS-B2-FI-07 | COVERED | B11.01, B11.67, B11.68, B12c.10 |
| IS-B2-SC-01 | COVERED | B24.42, B24.99 |
| IS-B2-SC-02 | COVERED | B24.01, B24.10, B24a.05, B25.09 |
| IS-B2-SC-03 | COVERED | B24.09, B24.10, B24.30, B24a.04 |
| IS-B2-SC-04 | COVERED | B24.12, B24.13 |
| IS-B2-SC-05 | COVERED | B24a.08, B28.13, B28.18 |
| IS-B2-SC-06 | COVERED | B28.14 |
| IS-B2-SC-07 | COVERED | B25.17, B27.17 |
| IS-B2-SC-08 | COVERED | B24.38 |
| IS-B2-SC-09 | COVERED | B24.39, B24.40 |
| IS-B2-SC-10 | COVERED | B24a.06, B27.14 |
| IS-B3-FA-01 | COVERED | B21.76 |
| IS-B3-FA-02 | COVERED | B34.09 |
| IS-B3-FA-03 | COVERED | B38.72 |
| IS-B3-FA-04 | COVERED | B23.12 |
| IS-B3-FA-05 | COVERED | B21.79, B21.57, B21b.16, B21b.21 |
| IS-B3-FA-06 | COVERED | B21.66 |
| IS-B3-FA-07 | COVERED | B21.69, B21b.27 |
| IS-B3-GO-01 | COVERED | B21.76, B11.05, B11.76, B11.79, B24.38, B41.08 |
| IS-B3-GO-02 | COVERED | B11.06, B34.20 |
| IS-B3-GO-03 | COVERED | B34.21 |
| IS-B3-GO-04 | COVERED | B38.77 |
| IS-B3-GO-05 | COVERED | B41.08, B41.10 |
| IS-B3-GO-06 | COVERED | B03g.01, B03g.02, B41.01 |
| IS-B3-GO-07 | COVERED | B34.10 |
| IS-B3-SE-01 | COVERED | B12c.29 |
| IS-B3-SE-02 | COVERED | B38.89 |
| IS-B3-SE-03 | COVERED | B12a.01, B12c.31 |
| IS-B3-SE-04 | COVERED | B03.13 |
| IS-B3-SE-05 | COVERED | B12c.09 |
| IS-B3-SE-06 | COVERED | B11.01, B11.68, B12c.10 |
| IS-B3-WR-01 | COVERED | B35.10, B35.11, B35.18, B35.20, B35.26 |
| IS-B3-WR-02 | COVERED | B35.22 |
| IS-B3-WR-03 | COVERED | B35.23 |
| IS-B3-WR-04 | COVERED | B35.25 |
| IS-B3-WR-05 | COVERED | B12a.07, B35.27 |
| IS-DICE-01 | COVERED | B34.17 |
| IS-DICE-B1 | COVERED | B30.09 |
| IS-DICE-P1 | ABSENT | — |
| IS-DICE-P2 | ABSENT | — |
| IS-DICE-P3 | ABSENT | — |
| IS-DICE-P4 | ABSENT | — |
| IS-DICE-P5 | ABSENT | — |
| IS-MB-01 | COVERED | B34.18, B20.11, B20.12, B20.21 |
| IS-MB-02 | COVERED | B22.11, B22.12, B39.19 |
| IS-MB-03 | COVERED | B20.19 |
| IS-MB-04 | COVERED | B30.06 |
| IS-MB-05 | COVERED | B17.13, B20.22 |
| IS-MB-06 | MENTIONED | — |
| IS-MB-B1 | COVERED | B22.01 |
| IS-MB-B2 | COVERED | B31.01 |
| IS-MB-B3 | COVERED | B22.04 |
| IS-MB-B4 | MENTIONED | — |
| IS-MB-P1 | ABSENT | — |
| IS-MB-P2 | ABSENT | — |
| IS-MB-P3 | COVERED | B17.01 |
| IS-MB-P4 | COVERED | B17.07 |
| IS-MB-P5 | COVERED | B17.03 |
| IS-MB-P6 | ABSENT | — |
| IS-MB-P7 | COVERED | B39.19 |
| IS-PC-01 | COVERED | B16.11, B34.15 |
| IS-PC-02 | COVERED | B30.07 |
| IS-PC-03 | COVERED | B15.12, B16.12, B37.18 |
| IS-PC-04 | COVERED | B14.26 |
| IS-PC-05 | COVERED | B15.02 |
| IS-PC-B1 | ABSENT | — |
| IS-PC-B2 | COVERED | B15.10 |
| IS-PC-P1 | ABSENT | — |
| IS-PC-P2 | COVERED | B31.02, B31.03, B31.16 |
| IS-PC-P3 | COVERED | B14.02 |
| IS-PC-P4 | ABSENT | — |
| IS-PC-P5 | ABSENT | — |
| MBA-01 | COVERED | B19a.01, B19.15, B31.10, B31.15 |
| MBA-02 | COVERED | B19a.02 |
| MBA-03 | COVERED | B19a.03 |
| MBA-04 | COVERED | B05.03, B19.10, B19.11, B19.12, B19.13, B19.14 |
| MBA-05 | COVERED | B19.21, B19.51 |
| MBA-06 | COVERED | B19.62, B19.63, B19.64 |
| MBA-07 | COVERED | B30.08 |
| MBA-08 | COVERED | B19.67 |
| MBA-09 | COVERED | B31.20 |
| PCR-1 | COVERED | B15.01 |
| PCR-2 | COVERED | B16.01 |
| PCR-3 | COVERED | B16.02 |
| PCR-4 | COVERED | B04.01 |
