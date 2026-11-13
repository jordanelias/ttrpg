# CHAR — the character's side of the skill surface: what a definition says to a reader, levels, bundles at a rank, and the cast row's unread keys

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-08) — the table this file would not name a path for is `references/descriptor_registry.yaml: capabilities` (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1–§2); `gloss` is a required field of that block.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row 1, §7, §7b-T; `unified/U1_GLOSSARY.md` *rank*, *ability*; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2, §3 amendment 5, §11 U1-A; `unified/U3_CONFLICT_LEDGER.md` C3-N27). Changed: the body names the decided path (`references/descriptor_registry.yaml: capabilities`) instead of "the table"; Edit 2 says `rank_at_least` reads the **capability rank** and selects levels of a use row, never a condition of attempting an act (A-11); "an ability is not a fifth kind" → "not a kind" (kinds are `skill, aptitude, trait`); Edit 5 lands once with CORE Edit 6 (one dataclass); the check gains named tests, the pin caveat and lands-it and tier. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (9); rewordings by sense (2: retired kinds `aptitude`/`trait`, traits apart, Thread Sensitivity not a skill, line-wrapped "trained").

**Lands in batch:** B04. **Depends on:** `01_CORE_capability_authoring_surface.md` Edit 1 (the block it adds `gloss` to; same batch, CORE first); B02 (the pin file).

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, §B4, F-CHAR-16,
F-CHAR-19, F-CHAR-21; B6.2 rows 4 to 6, 13, 14, 18, 22, 24). Ratifies nothing. Reference under
`CLAUDE.md` §0.05. **It adds to, and does not restate,** `10_DICE_capability_axiom_map.md` (the ten
roles, the definition row, the uses table) and `01_CORE_capability_authoring_surface.md` (the same
row, the verb column, the cast row's `capabilities:`). The file that holds the definition is decided:
`references/descriptor_registry.yaml: capabilities` (U1 §1, D-U1-07); "the capability definition table"
below means that block.

## What this changes in `engine/season/` at runtime

Nothing a season computes. Edits 1 to 3 add fields and a key that ship with no value that moves a
roll; edit 4 removes or marks cast-row keys no code reads; edit 5 widens a read-only copy; edit 6 is
text. Gate hash: `headless --case NPC-088 --seasons 2 --seed 0` prints `5405522c…`, EQUAL.

## The problem, with evidence

1. **A definition cannot be shown.** The map's row carries `kind`, `base`, `opposed_by`, `scale`,
   `untrained`, `grows_by`. `decision/sheet.py::CreationRow` shows `capability` as keys and numbers.
   A player, or a designer reading a cast row, sees `inquiry: 2` and no sentence anywhere says what
   inquiry is.
2. **The design's skills have levels that change what they do, not only how much.** The archived
   lifepath gives each skill three levels (*"Level 2 = quantitative enhancement. Level 3 =
   qualitative unlock"*). The map's `per: rank` scales an effect by rank; nothing says "this row
   applies from rank 2".
3. **A background grants nothing that rolls.** `rosters.yaml: tables.lifepath_templates` is *"A CUT,
   NOT A TRANSCRIPTION"*: every key is held at `pool_default`. By parse: 34 rows, 21 hold nothing, 7
   hold `inquiry`, 6 hold `argue`; five cast rows carry a lifepath and three of those grant nothing.
4. **The cast row authors facts nothing reads.** Non-null counts over the 46 rows of
   `references/npc_registry.yaml` (parse): `arc_trajectory` 36, `resonant_style` 18, `cultural_label`
   43 (17 at the row's top level, 26 inside its `convictions:` block), `self_other_initial` 28 (2 and
   26), `certainty` 8, `coherence` 1. A search of non-test Python finds one mention: the loader's
   comment where it steps over the two nested keys by name (`data/cast.py:220`).
5. **The player's development sheet shows less than his creation sheet.** `DevelopmentSheet` has no
   `attributes`, `thread_sensitivity`, `heritage` or tenures (`dataclasses.fields`; CORE's edit 6
   adds `attributes`).
6. **Three register rows describe a tree that has moved** (B6.1: H-46's last sentence, H-148's head,
   H-170's `body_step`).

## The resolution, decided, and the exact edits

### Edit 1 · `gloss` on the definition row (ladder step 5)

Every row of the skill definition table carries `gloss:`, one sentence in plain words saying
what the skill is. The loader refuses a row without one, as the verb loader refuses a missing
`beneficiary:`. The ten attributes gain the same key where they are defined
(`references/descriptor_registry.yaml: attributes`); three of them (Focus, Reason, Presence) carry no
description today (`rosters.yaml:1588`). Readers: `decision/sheet.py` gains
`describe(key) -> str` (the leaf's text, no `World`); the first lane's reason trail prints it beside
a skill use that fired. The four existing rows, for Jordan to correct:

| id | proposed `gloss` |
|---|---|
| `copying` | Carries a text or a message on exactly as it was given. |
| `argue` | Makes a case to someone's face and moves them by it. |
| `inquiry` | Finds things out: from a record, a place or a watched person. |
| `arms` | Fights with a weapon in hand. |

### Edit 2 · `rank_at_least` as a `when` key (step 4: the map's `when` roster)

One more member of the uses table's closed `when` keys: `rank_at_least: <n>` holds when the holder's
**skill rank** (the held rank on the row's `scale`, never a seat rank) in the row's `key` is at
least `n`. It is how a skill's higher rank changes *what* it does: two use rows on one key, the second
under `rank_at_least: 3`, selecting which levels apply. It is never a condition of attempting an act and
never a `requires` stem (A-11; U1 §3 amendment 5: Thread Sensitivity is the one `gate`); the archived
"Level 3 = qualitative unlock" is read as a different use row, not an unlocked act. One comparison in the
uses reader; no row ships.

### Edit 3 · a bundle may grant at a rank (step 4: CORE's edits 5 and 9)

In `tables.lifepath_templates`, an entry of `holds:` may be `{<id>: <rank>}` as well as a bare id; a
bare id keeps today's meaning (the untrained value). The loader checks the rank against the
skill's `scale`. No rank is authored here: which lifepath starts a person at what is content,
and it only moves a pool once CORE's edit 9 (a first rank is never a loss) has landed. The same
shape serves a martial tradition's bundle (AR-43a) when the combat module exports one.

### Edit 4 · the cast row's unread keys: read, remove or mark (steps 1, 2, 4)

| key | rows | decision | reason |
|---|---|---|---|
| `resonant_style` | 18 | **read** | `02_CHAR_which_ground_moves_whom.md` |
| `arc_trajectory` | 36 | **move and delete**: the sentence goes to the person's NPC case file as prose; the key leaves the registry | an arc is an observer's reading, never an input (ED-IN-0225); a key in the file code reads invites a reader |
| `cultural_label` | 43 | **delete**, at both levels | superseded: every row authors all fifteen pursuits directly (ED-IN-0261; `data/cast.py` refuses fewer); the template it names exists in no file code reads (a search finds the names only in the registry itself) |
| `self_other_initial` | 28 | **delete**, at both levels | superseded: `selfish_selfless` is projected from pursuits (ED-IN-0261). Whether that axis is ever weighted is the NPC research lane's open item and does not need these two values |
| `certainty`, `coherence` | 8, 1 | **keep, marked** | threadwork's tracks; no reader until that lane builds one |

`engine/season/data/cast.py` gains, beside its readers, `UNREAD_KEYS = ("certainty", "coherence")`
and refuses at build a row carrying a key that is neither read nor listed there. That is the loader's
refusal for its own data family (`CLAUDE.md` §0.05), not a new check elsewhere; it is what would have
surfaced these six on the day they were authored.

### Edit 5 · the development sheet shows the person (step 5)

`decision/sheet.py::DevelopmentSheet` gains `thread_sensitivity`, `heritage` and `tenures` (a frozen
tuple of the person's own live edges as `(kind, object)`: his seats, oaths, commits and residence).
Own state only, copies only, as its other fields are. CORE's edit 6 adds `attributes`; the two edits
are one change to one dataclass and land once, in one commit of B04 (CAP Part A names it).

### Edit 6 · three register rows (step 1)

`engine/season/hole_register.yaml`, text only: H-46's last sentence (*"`rosters.yaml` still carries
the OLD thirteen"*) is struck with the date; H-148's `hole:` opens with the CR-24 state it now
describes in a bracket; H-170's cite gains one line that `body_step` reads 10 today and its readings
were taken at 0.

## What a definition must carry, in one place

The full field list (one kind, skill, A-98; the traits are their own roster, U1 §2a), with the tradition's word for each and
its reader, is the table in the addendum's §B4 (c) as decided in U1 §2: `kind`, `gloss`, `base`,
`opposed_by`, `scale`, `untrained`, `grows_by`; a use row per effect, with `when` (now including
`rank_at_least`); and nothing about loss, because a skill is never lost. An *ability* is not a
kind: it is a skill whose use row names its scene's site (A-98), and a combat ability waits on the
combat module exporting its lever roster.

## The gate (an execution artifact)

(a) The NPC-088 headless hash and `build_realm(0)`'s build hash, EQUAL before and after. (b) A
definition row with no `gloss`, and a cast row with an unlisted key, each refuse at load with a
message naming the row. (c) `describe("inquiry")` returns the sentence; a `DevelopmentSheet` for
`p_npc_001` shows Thread Sensitivity 75. (d) With a test row `{…, when: {rank_at_least: 3}}`, a
holder at rank 2 and one at rank 3 read different levels from the generic advantage source.
The NPC-088 hash `5405522c…` is the working tree's reading before B01; every such pin moves at B01, so
the batch re-reads it on its base and quotes that (C3-N27).

**Named tests** (in `engine/season/tests/test_u1_capability_surface.py`, the B04 file of U1 §11 U1-A):
(b) `test_a_definition_row_with_no_gloss_is_refused_naming_it`, `test_a_cast_row_key_neither_read_nor_unread_listed_is_refused`;
(c) `test_describe_returns_the_gloss`, `test_development_sheet_shows_thread_sensitivity_heritage_and_tenures`
(`p_npc_001` reads Thread Sensitivity 75);
(d) `test_rank_at_least_selects_a_second_use_row` (a planted row; holders at skill rank 2 and 3 read
different levels; `==` on the level names, not `approx`). (a) is the batch's hash check.

## The falsifier

Any hash in (a) moves (an edit that was to change nothing changed something). Or, after edit 4, a
search finds a reader of a deleted key (it was not unread). Or (d)'s two holders read alike.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** From the designer's side a skill he cannot describe on the row he defines is a number;
  from the player's side the sheet is the only place he meets it; from the engine's side nothing
  changes. It holds in the two directions that have a reader and is neutral in the third.
- **R.** Customisation is the brief's own demand: a skill, its levels and the background that grants
  it are each one row. Completeness: the cast row can no longer hold a fact that silently does
  nothing.
- **S.** No new table; one key in an existing closed roster; one field on an existing row; the
  loader's own refusal.
- **E.** Six small edits, none of which moves play, in exchange for a sheet that can say what it
  shows and a registry whose every key is either read or declared unread.

## Cost class

Edit. Edit 4's deletions are content edits to a file code reads; one re-check of the build hash.

**Lands it.** The B04 batch (U1 §11 U1-A), an IN `valoria-author` session on `sonnet` (`high`), one commit
per edit after CORE Edit 1; closed by the batch's `methodology-close` once. **Hash movers.** None
(control: the batch's base tree); edit 4 re-checks `build_realm(0)`'s build hash.
