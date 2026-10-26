# Held-back Layer 0/1 hunks of master workplan v10

## Status: APPLIED on branch ccr-edc32cdb-2nsop2 (PR #507), one commit each, except H-L0-5, which lands with GO-14 and whose landing deletes this file.

Applied hunks and their commits (`git log --oneline --grep 'H-L0-'`); each is reverted alone by `git revert <hash>`:

| hunk | commit | subject |
|---|---|---|
| H-L0-1 | `de2f83b4` | [design] H-L0-1: CLAUDE.md §5 names the real dice_engine path |
| H-L0-2 | `f01216e1` | [design] H-L0-2: CLAUDE.md preamble points at ED-GO-0002 |
| H-L0-3 | `5c06322e` | [design] H-L0-3: CLAUDE.md §6 drops the engine_clock doc:null aside |
| H-L0-4 | `2d2b0431` | [design] H-L0-4: CLAUDE.md §6 points porting at the port gate |
| H-L0-5 | not applied | lands with GO-14's deletion of `godot/skeleton/`, in that PR |
| H-L0-6 | `32bd9ef9` | [design] H-L0-6: CLAUDE.md §0.2 retires the mc_v18 bullet |
| H-L0-7 | `9fa1685e` | [design] H-L0-7: 04 §B.2 admits Person.heritage? (PROPOSED, CR-30) |
| H-L0-8 | `2e367f34` | [design] H-L0-8: 04 §C.2 admits an election arm in the write gate |
| H-L0-9 | `3f34e32f` | [design] H-L0-9: 01_AXIOMS T-o names joint_concurrence as a "who" |
| H-L0-10 | `8d6b2361` | [design] H-L0-10: canon/03 marks the faction table as history |

The rows below keep the proposal's wording as the record; where a row's `new text` differs from what was applied, it has been corrected to the applied text (H-L0-10).

Each row is text for a Layer 0 or Layer 1 file (H-L0-10 alone is canon, `canon/03_canonical_timeline.md`, world truth). Jordan's "Confirm all" of 2026-10-26 (ED-IN-0300, ED-IN-0301) answered M11: every row but H-L0-5 was applied in PR #507, one commit each and each independently revertible; H-L0-5 lands in the PR of GO-14, which deletes `godot/skeleton/`, listed under "Layer 0/1 hunks" in that PR's body. The `(RULED)` check was made before the hunk was listed: no `(RULED)` mark sits at or within the paragraph of the anchor.

| id | file | anchor (quoted words) | old text | new text | owner position | revert |
|---|---|---|---|---|---|---|
| H-L0-1 | `CLAUDE.md` §5 (Data to Godot pipeline), the sentence ending "Check the code first, every time." | "superseded by `degree_from_net` in `engine/autoload/dice_engine.py`" | `superseded by `degree_from_net` in `engine/autoload/dice_engine.py`). **Check the code first, every` | `superseded by `degree_from_net` in `engine/dice_engine/dice_engine.py`). **Check the code first, every` | CR-02 (c) (B10-01) | restore the old path; the owner file is `engine/dice_engine/dice_engine.py` and `engine/autoload/` does not exist in the tree, so the old text names a missing file |
| H-L0-2 | `CLAUDE.md` preamble, the "Implementation repo" paragraph | "Godot engine version is UNRESOLVED" | `⚠️ **Its Godot engine version is UNRESOLVED and nothing here may assert one** — its `project.godot` and CI pin one version, `godot/` here documents another. Awaiting a ruling; do not settle it by editing a document.` | `⚠️ **Its Godot engine version is RULED by Jordan (`ED-GO-0002`); nothing here asserts one** — that ledger row is the one owner, and `project.godot` and the CI pin in that repo are owed a move to it.` | GO-13 (B10-01) | restore the old sentence; it is false once ED-GO-0002 stands, so a revert needs ED-GO-0002 reopened first |
| H-L0-3 | `CLAUDE.md` §6 (Godot port pipeline), second paragraph | "including `engine_clock`, the temporal spine" | `modules have `doc: null` (including `engine_clock`, the temporal spine) and which resolvers are` | `modules have `doc: null` and which resolvers are` | GO-13 (B10-01) | restore the parenthesis; `references/module_contracts.yaml` sets `engine_clock`'s `doc:` (the `module: engine_clock` row), so the parenthesis is now false |
| H-L0-4 | `CLAUDE.md` §6, second paragraph, the sentence after the `[ASSUMPTION]`-grade clause | "authoring canon first" | `porting beyond the combat slice is blocked on authoring canon first, starting with `engine_clock`.` | `porting beyond the combat slice waits on the port gate (B10-20 in the active master workplan, which `CURRENT.md` names).` | GO-13 (B10-01); the gate it points at is B10-20 (GO-11, GO-15) | restore the old clause; it names a first step (`engine_clock` canon) that the row above shows done |
| H-L0-5 | `CLAUDE.md` §6, first paragraph, the sentence after "...into the `.gd` side." | "`godot/skeleton/` covers a single module" | `godot/skeleton/` covers a single module, does not compile, and `extends` a spine defined nowhere in the corpus: **never present it as a runnable head-start.**` (the whole sentence) | (removed; the paragraph ends at "into the `.gd` side.") | GO-13 (B10-01) for the text; **DEPENDENT ON H-L0-GO14** (GO-14's deletion of `godot/skeleton/`, B10-03, released from M11 with DEF-9): this hunk lands only in the same PR as GO-14's deletion and never before the tree is deleted, because until then the sentence is true and is the warning against the tree | restore the sentence; if GO-14 is not merged this hunk must not be applied |
| H-L0-6 | `CLAUDE.md` §0.2 (DONE MEANS IT RUNS), the second bullet after the table | "`mc_v18` is DEPRECATED IN PLACE" | `- ⚠ **`mc_v18` is DEPRECATED IN PLACE.** No game code imports it; do not delete it — tests in CI's blocking `sim-regression` job do. `tests/valoria/test_mc_v18_is_deprecated.py`'s `ALLOWED_IMPORTERS` is the shrink-only live list; it fails on a NEW importer and on a stale roster line. **Nothing new is built there.**` (the whole bullet, four lines) | (removed; the bullet before it, ending "It declares itself DOC-DERIVED.", is followed by the bullet beginning "For a juncture with running code") | IN-44 row 1 (B10-Z), retired under M15 (a): Jordan's 2026-09-16 and 2026-09-27 words and the `FORK:5c5d8ec6` rows for `engine/mc_v18.py` and `tests/valoria/test_mc_v18_is_deprecated.py` in `references/restructure_ledger.md` supersede it (`workplans/valoria_master_workplan_v10_part6.md` M15) | restore the four lines |
| H-L0-7 | `architecture/meta/04_CODE_ARCHITECTURE.md` §B.2, the `Person :=` block (lines 234-238) | "coherence?" | ``Person := ( id, weight, capability, body, exists, travel_leg , stance[], pursuits, scar[axis], axis_count[axis], coherence? , ledger ) -- renamed/dropped 2026-09-24, ED-IN-0261 item 1: `convictions` -> `pursuits` (season-side name only, values unchanged); `marks[]` dropped (retired write_matrix.yaml field, zero readers)`` | ``Person := ( id, weight, capability, body, exists, travel_leg , stance[], pursuits, scar[axis], axis_count[axis], coherence?, heritage? , ledger ) -- renamed/dropped 2026-09-24, ED-IN-0261 item 1: `convictions` -> `pursuits` (season-side name only, values unchanged); `marks[]` dropped (retired write_matrix.yaml field, zero readers) -- `heritage?` (PROPOSED, v10 second decision round, CR-30): the one member of the dropped `marks[]` no Tenure derives; a read-off field (§D.1.1), written at world build only, no write-matrix row; its resolver is WITNESS's `marks` term`` | CR-30 (B10-10); recommended, NOT a precondition: CR-30 builds without it (precedent: `born` and `thread_sensitivity` were added without amending `04`; the admission rule is §D.1 and §D.1.1, and §B.2's list already omits live fields) | restore the block's second line and drop the added note line; CR-30 stands without it |
| H-L0-8 | `architecture/meta/04_CODE_ARCHITECTURE.md` §C.2 (the write gate), the determination arm: lines 606-607 kept, five lines inserted after line 607 | "determination: a bench binds" | ``via IS a judging Seat, actor seated, OPENING an `oblige` on it for another person its bench's ground holds -- determination: a bench binds (`19`)`` | ``via IS a judging Seat, actor seated, OPENING an `oblige` on it for another person its bench's ground holds -- determination: a bench binds (`19`) via IS a judging Seat, actor seated, OPENING a `hold` on a vacant Seat S other than via whose `conferral` basis is filled by `determine`, for a party S's faction admits, or, for a seat whose conferral basis is inheritance, any claimant -- determination, election arm (CR-35)`` | CR-35 (B10-17): its election arm, its contested-succession arm (the clause after "faction admits") and its H-217 clause rest on this text, applied in PR #507; CR-35 builds them in the ordinary way | remove the five inserted lines; CR-35's arm loses the text it rests on, and `elected` seats keep `confer` |
| H-L0-9 | `architecture/meta/01_AXIOMS.md`, the `T-o` row's "who" cell (line 1257) | "a superior, at a venue, paying an act" | ``> \| **`T-o`** ⚠ **NEW · a REVOCATION declared on the seat** \| the **Seat's** `revocation` basis, exercised through `Act.via` \| a superior, at a venue, paying an act \|`` | ``> \| **`T-o`** ⚠ **NEW · a REVOCATION declared on the seat** \| the **Seat's** `revocation` basis, exercised through `Act.via` \| a superior, or a seat the revoked Seat's declared basis names (`joint_concurrence`: a concurring body), at a venue, paying an act \|`` | CR-37 (B10-17): applied in PR #507, so CR-37 builds in the ordinary way; `04:327` stands as written, because one seat revokes | restore the cell; CR-37 is not built and `depose` returns to PARKED with M8's trigger |
| H-L0-10 | `canon/03_canonical_timeline.md` (canon), two replacements in one file | "### Faction Starting Values (1-7 scale)" (line 147) and the row "\| Revolution \|" (line 156) | (1) ``### Faction Starting Values (1-7 scale)``; (2) ``\| Revolution \| — \| 3 \| — \| — \| — \| 3 \|`` | (1) ``### Faction Starting Values (1-7 scale) > Board-game-era starting values, kept as history. Two rows are superseded by world: **Niflhel is > dissolved** (`worldbuilding_v30.md` §3.2, §10) and **"Revolution" is the Restoration Movement** > (the rename `geography_v30.md` orders as its own item ED-061; the ledger's ED-061 is unrelated). > Faction-wide stats are not engine quantities (`architecture/meta/01_AXIOMS.md` T-a). The live roster > of polities an office belongs to is `references/names_index.yaml`'s `token_class: faction` rows; it > states no count (RULED 2026-09-19).`` followed by one blank line before the table (as applied: `canon/03_canonical_timeline.md:147-155`); (2) ``\| Restoration Movement \| — \| 3 \| — \| — \| — \| 3 \|`` | CR-42 (B10-08), which does NOT wait on it. Not proposed: striking the Niflhel row (history) or changing line 160 (Schoenland is not a playable faction) | restore the heading line (drop the note and its blank line) and the row |

Evidence for H-L0-1, read 2026-10-26: `grep -n 'engine/autoload' CLAUDE.md` finds one hit, in §5; `ls engine/autoload` fails; `engine/dice_engine/dice_engine.py` holds `degree_from_net`; `CURRENT.md`'s Dice row already names the new path.

Evidence for H-L0-2 to H-L0-5, read 2026-10-26 (GO-13); H-L0-2 to H-L0-4 applied 2026-10-26, H-L0-5 lands with GO-14. Anchors re-read by quoted words, none already fixed: `grep -n 'UNRESOLVED\|engine_clock\|authoring canon first\|skeleton' CLAUDE.md` finds the preamble sentence, the §6 `skeleton` sentence, the `engine_clock` parenthesis and the "authoring canon first" clause, each unchanged. The `(RULED)` check: `grep -n RULED CLAUDE.md` has no hit within the preamble's "Implementation repo" paragraph or within §6. `references/module_contracts.yaml` still carries `doc: null` on other modules, so only the `engine_clock` parenthesis goes, not the clause. `ED-GO-0002` is the ledger row in `registers/editorial_ledger_go.jsonl`; PR #467 is closed (reported by the orchestrator, not re-read from here, since `gh pr view` is blocked in this session), so H-L0-2 applies and is not #467's own. ED-GO-0002's description presumes this hunk: its "which now points here" is true of `CLAUDE.md`'s preamble only once H-L0-2 lands. In the table, a line break in the file's quoted text is shown as a space. `H-L0-GO14` is the id the GO-14 hunk takes in B10-03; it is not yet in this file.

Evidence for H-L0-6, read 2026-10-26: `grep -n mc_v18 CLAUDE.md` finds the bullet's first two lines in §0.2; `engine/mc_v18.py` and `tests/valoria/test_mc_v18_is_deprecated.py` are absent, each with a `FORK:5c5d8ec6` row, so the bullet names a module and a test that no longer exist. The `(RULED)` check: no mark sits within the bullet's paragraph, but §0.2's heading carries `(RULED)`; that heading is why M15 was put to Jordan and why this hunk waited on M11 (answered (a); applied 2026-10-26).

Evidence for H-L0-7 to H-L0-10, read 2026-10-26: the four anchors re-read by quoted words (`04_CODE_ARCHITECTURE.md:234-238` and `:606-607`, `01_AXIOMS.md:1257`, `canon/03_canonical_timeline.md:147` and `:156`), none already changed; the `(RULED)` grep over each anchor's paragraph (`04_CODE_ARCHITECTURE.md:225-245` and `:590-615`, `01_AXIOMS.md:1245-1265`, `canon/03_canonical_timeline.md:140-162`) prints nothing. H-L0-7 is recommended and holds nothing; H-L0-8 holds CR-35's election arm, its contested-succession arm and its H-217 clause (its last clause, "or, for a seat whose conferral basis is inheritance, any claimant", covers the contested succession, where CR-35 drops the party's faction clause for an `inheritance` seat); H-L0-9 holds CR-37; H-L0-10 holds nothing (CR-42 lands without it). The four were applied 2026-10-26 in PR #507, on M11's confirmation of D-1 (ED-IN-0300; `-05` §1a, question (d) confirmed at the default, ED-IN-0301). No amendment of AX-5 or T-c is proposed, and no hunk at `04_CODE_ARCHITECTURE.md:326` is proposed (the filling act for a nominated seat is `confer`, already listed there). In the table, `\|` is a literal `|` of the file's text; H-L0-10's new text ends in one blank line so the note does not run on into the table below it. The note's wording was corrected when applied: the rename is `geography_v30.md`'s own item ED-061, and the ledger's ED-061 ("Projectile weapon categories") is unrelated.

Exact lines for H-L0-7 to H-L0-10. The table joins each line break into a space and collapses indentation; these blocks are the text as it stands in the file now (old) and as it is to stand (new), column for column.

H-L0-7, old (`04_CODE_ARCHITECTURE.md:234-238`):
```
Person := ( id, weight, capability, body, exists, travel_leg
          , stance[], pursuits, scar[axis], axis_count[axis], coherence?
          , ledger )
-- renamed/dropped 2026-09-24, ED-IN-0261 item 1: `convictions` -> `pursuits` (season-side name
   only, values unchanged); `marks[]` dropped (retired write_matrix.yaml field, zero readers)
```
H-L0-7, new:
```
Person := ( id, weight, capability, body, exists, travel_leg
          , stance[], pursuits, scar[axis], axis_count[axis], coherence?, heritage?
          , ledger )
-- renamed/dropped 2026-09-24, ED-IN-0261 item 1: `convictions` -> `pursuits` (season-side name
   only, values unchanged); `marks[]` dropped (retired write_matrix.yaml field, zero readers)
-- `heritage?` (PROPOSED, v10 second decision round, CR-30): the one member of the dropped `marks[]` no Tenure derives; a read-off field (§D.1.1), written at world build only, no write-matrix row; its resolver is WITNESS's `marks` term
```

H-L0-8, old (`04_CODE_ARCHITECTURE.md:606-607`, kept):
```
      via IS a judging Seat, actor seated, OPENING an `oblige`
        on it for another person its bench's ground holds     -- determination: a bench binds (`19`)
```
H-L0-8, new (lines 606-607 unchanged, then five lines):
```
      via IS a judging Seat, actor seated, OPENING an `oblige`
        on it for another person its bench's ground holds     -- determination: a bench binds (`19`)
      via IS a judging Seat, actor seated, OPENING a `hold`
        on a vacant Seat S other than via whose `conferral`
        basis is filled by `determine`, for a party S's
        faction admits, or, for a seat whose conferral basis
        is inheritance, any claimant                          -- determination, election arm (CR-35)
```

H-L0-9, old (`01_AXIOMS.md:1257`):
```
> | **`T-o`** ⚠ **NEW · a REVOCATION declared on the seat** | the **Seat's** `revocation` basis, exercised through `Act.via` | a superior, at a venue, paying an act |
```
H-L0-9, new:
```
> | **`T-o`** ⚠ **NEW · a REVOCATION declared on the seat** | the **Seat's** `revocation` basis, exercised through `Act.via` | a superior, or a seat the revoked Seat's declared basis names (`joint_concurrence`: a concurring body), at a venue, paying an act |
```

H-L0-10 (1), old (`canon/03_canonical_timeline.md:147`):
```
### Faction Starting Values (1-7 scale)
```
H-L0-10 (1), new, as applied (the heading, six note lines, one blank line):
```
### Faction Starting Values (1-7 scale)
> Board-game-era starting values, kept as history. Two rows are superseded by world: **Niflhel is
> dissolved** (`worldbuilding_v30.md` §3.2, §10) and **"Revolution" is the Restoration Movement**
> (the rename `geography_v30.md` orders as its own item ED-061; the ledger's ED-061 is unrelated).
> Faction-wide stats are not engine quantities (`architecture/meta/01_AXIOMS.md` T-a). The live roster
> of polities an office belongs to is `references/names_index.yaml`'s `token_class: faction` rows; it
> states no count (RULED 2026-09-19).

```
H-L0-10 (2), old (`canon/03_canonical_timeline.md:156`):
```
| Revolution | — | 3 | — | — | — | 3 |
```
H-L0-10 (2), new:
```
| Restoration Movement | — | 3 | — | — | — | 3 |
```
