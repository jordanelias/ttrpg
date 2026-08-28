# Harvest provenance — systems integration master, 2026-08-28

## Status: PROVENANCE — append-only evidence, not canon and not reference to reason from
## Lane: IN

**What this is.** The 1,079 structured records eleven parallel harvest lanes emitted while reading the
corpus for `research/valoria_systems_integration_master_v1*.md`, plus the four briefs that governed
them. It is the evidence base for the flatten in that document's Parts 1–2.

**Why it is committed.** The master's §1.2 states that code citations from six of the eleven lanes are
advisory rather than verified. A reader who wants to check that had nothing to check against; this is
what they check against. Every code claim *reproduced into* the master was re-verified against disk
before inclusion and unverifiable ones were dropped — so **these records are upstream of that filter,
not downstream of it.**

**How to read a record.** The schema, the closed sets for `slice` / `system` / `status` / `shape`, and
the anti-fabrication rules are in `HARVEST_CONTRACT.md`. `GATE_A_BRIEF.md` is what the adversarial gate
was told to do; `CORRECTIONS.md` is the verdicts it returned, which were applied silently as edits.
`SYNTHESIS_BRIEF.md` governed the three synthesis groups.

⚠ **Do not reason from these records directly.** They are a snapshot of what eleven lanes believed on
2026-08-28, including the errors the gate later overturned — six of them traceable to a single date
window, where the lanes' design-doc sources predate thirteen commits that landed 2026-08-22 to 08-27.
**The corrected statements live in the master document.** These files exist so a claim can be traced,
not so it can be re-used.

**Do not edit.** Append-only, like the frozen ED-ledger fragments in `registers/archive/`. A record
edited after the fact stops being evidence of anything.

| file | lane beat |
|---|---|
| `H1` | `research/` — cross-scale action catalogue, personnel/muster integration master |
| `H2` | `proposals/` — social contest consolidation, throughlines and precedent, conflict architecture |
| `H3` | `systems/_architecture/` — propagation spec, derived stats, player agency, key substrate |
| `H4` | `audit/2026-07-12-governance-compendium/` — all ten files |
| `H5` | `systems/factions/` — 18 design docs + `sim/` (17 modules, 2,747 lines) read in full |
| `H6` | `systems/settlements/` + `systems/world/` |
| `H7A` / `H7B` | `scale_transitions_v30.md`, `engine/cross_scale/`, `engine/substrate/` |
| `H8A` / `H8B` | `research/` roster and historical-precedent corpus; `research/governance/` |
| `H9` | `engine/` core — `game_state`, `dice_engine`, `sigma_leverage`, `victory`, `mc_v18` |

---

## Full inventory (2026-08-28 handoff)

The session's scratchpad was 27 MB. What is here is what has continuity value; what was left out is
listed below **with the reason**, so the next session does not go looking for it.

### Committed

| path | what it is |
|---|---|
| `H1.md` … `H9.md`, `H1.yaml` | The 1,079 records as emitted by the eleven harvest lanes |
| `records.json` | **The same 1,079 records, machine-readable** — 1,079 unique ids across H1–H9. Prefer this over the `.md` for any tooling |
| `HARVEST_CONTRACT.md` | The schema, the closed sets, the anti-fabrication rules the lanes worked under |
| `GATE_A_BRIEF.md` · `CORRECTIONS.md` | What the adversarial gate was told to do, and the verdicts it returned |
| `SYNTHESIS_BRIEF.md` | What governed the three synthesis groups |
| `synthesis/SYN_GROUP_A/B/C.md` | **The three synthesis agents' raw, unedited output.** Master Parts 1–3 were assembled from these; this is what they looked like before assembly |
| `corpus_manifest.json` · `code_inventory.json` | The harvest's inputs — what was read, and what code was inventoried |
| `tools/dump.py` · `tools/extract.py` | How the records were pulled out of the agent transcripts |
| `artifact/valoria.html` | **Source of the published page** at `claude.ai/code/artifact/a186da98-967f-4c0e-a642-9ebbbdd7719d`. A session without this file cannot update that artifact |

### Deliberately not committed

| what | why |
|---|---|
| `hist-6311caa/` — 819 files, 21 MB | **Already in git.** A materialised checkout of `FORK:6311caa8`, the 2026-06-28 pre-restructure tree, taken for reading during the design-corpus passes (`personnel_muster_integration_master_v1.md:845`). Committing it would re-import the pre-restructure tree into `main`, which is exactly what `references/restructure_ledger.md` exists to prevent. Re-materialise with `git checkout 6311caa8 -- <path>` |
| `FLATTEN.md`, `WITHIN.md`, `F_AB.md`, `F_C.md`, `W_ALL.md` | **Mechanical concatenations** of the `synthesis/` files, produced by a one-line script, whose content is verbatim in `valoria_systems_integration_master_v1{,_part2,_part3}.md`. Four more copies of the same text would rot independently |
| Per-file text dumps (`fs_H*.txt`, `out_*.txt`, `ch1.txt`, `p2.txt`, `faction-strategy.txt`, …) | Copies of repository files, pulled for reading. The originals are in the tree |
| `action-catalogue.html`, `integration-master.html` | Superseded artifact drafts; `artifact/valoria.html` is the live one |
| Fetched third-party pages (`fandom_opinion.html`, `forum_courtiers.html`, `ck2_opinion_mods.txt`, `ck3_opinion.txt`, `gh_*.md`) | **Scraped web content of unclear licence.** The findings are extracted into the companion, and Part 1 §1.2's sourcing caveat already records that most fan wikis were bot-walled. Do not re-commit these |
| `recs.json` | Byte-equivalent to `records.json` at 2× the size — same 1,079 ids, different indentation |
